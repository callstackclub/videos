"""See what a real TLS handshake negotiated, and the certificate chain of trust.

    python inspect_tls.py example.com
    python inspect_tls.py github.com 443

Standard library only (Python 3.13+). If verification fails on Windows with
"unable to get local issuer certificate", run `pip install certifi` and retry:
Windows downloads some root certificates on demand, so Python may not see them yet.
"""
import socket
import ssl
import sys
import tempfile
from datetime import datetime, timezone


def trust_store() -> tuple[ssl.SSLContext, str]:
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where()), "certifi (Mozilla) bundle"
    except ImportError:
        return ssl.create_default_context(), "operating system store"


def decode(der: bytes) -> dict:
    # The stdlib can only parse certificates from a file, so write the DER bytes out as PEM.
    with tempfile.NamedTemporaryFile("w", suffix=".pem", delete=False) as f:
        f.write(ssl.DER_cert_to_PEM_cert(der))
    return ssl._ssl._test_decode_cert(f.name)


def field(cert: dict, part: str) -> str:
    d = dict(x[0] for x in cert.get(part, ()))
    return d.get("commonName") or d.get("organizationName", "?")


def main(host: str, port: int = 443) -> None:
    ctx, store = trust_store()
    with socket.create_connection((host, port), timeout=10) as raw:
        # wrap_socket runs the whole handshake: ClientHello (with SNI = host and key shares),
        # ServerHello, then the encrypted certificate, CertificateVerify and Finished.
        with ctx.wrap_socket(raw, server_hostname=host) as tls:
            cipher, _, bits = tls.cipher()
            print(f"Connected to {host}:{port}")
            print(f"  protocol    : {tls.version()}")
            print(f"  cipher      : {cipher} ({bits}-bit AEAD key)")
            print(f"  trust store : {store}")

            chain = tls.get_verified_chain()
            print(f"\nChain of trust ({len(chain)} certificates, server first):")
            for i, der in enumerate(chain):
                c = decode(der)
                role = "server" if i == 0 else ("root (trusted)" if i == len(chain) - 1 else "intermediate")
                print(f"  [{i}] {role:<15} {field(c, 'subject')}")
                print(f"      signed by       {field(c, 'issuer')}")
                print(f"      valid until     {c['notAfter']}")

            leaf = tls.getpeercert()
            expires = datetime.fromtimestamp(ssl.cert_time_to_seconds(leaf["notAfter"]), timezone.utc)
            names = [v for k, v in leaf.get("subjectAltName", ()) if k == "DNS"]
            print(f"\nServer certificate covers: {', '.join(names[:5])}{' ...' if len(names) > 5 else ''}")
            print(f"It expires in {(expires - datetime.now(timezone.utc)).days} days.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 443)
