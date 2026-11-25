# Inside HTTPS: TLS 1.3 Handshake and Trust Chains

▶ **Watch:** https://youtu.be/B72IChtaLQk

## In the video

1. Why HTTPS matters
2. Certificates and the Chain of Trust
3. TLS 1.3 Handshake in One Round‑Trip
4. Ephemeral Diffie‑Hellman and forward secrecy
5. From handshake to encrypted HTTP

## Key facts (checked for the video)

- HTTPS is HTTP sent inside a TLS connection. TLS gives three things - confidentiality (encryption), integrity (tampering is detected), and authentication of the server.
- On plain HTTP anyone on the path (same Wi-Fi, the router, the ISP) can read and modify requests and responses.
- The padlock means the TLS connection succeeded AND the certificate is valid for that exact hostname AND chains to a trusted root. It does NOT mean the site is honest - phishing sites can get valid certificates for their own domains for free.
- A self-signed, expired or wrong-hostname certificate makes the browser show a full-page warning, not a padlock.
- An X.509 certificate contains the domain names (Subject Alternative Name), the site's public key, the issuer, a validity period, and the issuer's digital signature over all of it.
- Chain of trust - the leaf (site) certificate is signed by an intermediate CA, the intermediate is signed by a root CA. Root certificates come preinstalled in the OS or browser trust store. The server sends the leaf plus intermediates; the browser checks each signature up to a root it already trusts.
- Let's Encrypt certificates are free and valid for 90 days.
- TLS 1.3 (RFC 8446, published 2018) completes a full handshake in one round trip; TLS 1.2 needed two.
- ClientHello carries supported versions and cipher suites, a random value, the hostname (SNI), and a key_share - the client's ephemeral public key, usually X25519.
- ServerHello carries the chosen cipher suite and the server's key_share. From then on the handshake is encrypted - EncryptedExtensions, Certificate, CertificateVerify (a signature over the handshake transcript made with the certificate's private key), and Finished (a MAC over the whole transcript).
- The client checks the certificate and CertificateVerify, sends its own Finished, and can send the HTTP request immediately in that same flight.
- Key exchange is ephemeral elliptic-curve Diffie-Hellman - each side combines its own private key with the other's public key and both get the same shared secret, which is never sent over the network. HKDF turns it into the symmetric traffic keys.
- Because the Diffie-Hellman keys are thrown away after each connection, stealing the server's certificate private key later cannot decrypt recorded traffic. This is forward secrecy. TLS 1.3 removed the old RSA key exchange that lacked it.
- TLS 1.3 data ciphers are AEAD - AES-128-GCM, AES-256-GCM or ChaCha20-Poly1305 - which encrypt and authenticate each record together.
- Asymmetric crypto is used only in the handshake because it is far slower than symmetric crypto; AES with CPU hardware support runs at gigabytes per second.
- Good analogy for Diffie-Hellman - mixing paint - both mix a public colour with their secret colour, swap the mixtures, add their secret again, and end with the same final colour an eavesdropper cannot unmix.

## Files

- [`inspect_tls.py`](inspect_tls.py)

## Run it

```bash
python inspect_tls.py example.com
python inspect_tls.py github.com 443
```
