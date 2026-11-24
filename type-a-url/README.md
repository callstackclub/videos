# What Really Happens When You Hit Enter on a URL

▶ **Watch:** https://youtu.be/iv0UmwpeehU

## In the video

1. Parsing the Input
2. Resolving the Hostname
3. Establishing a Secure Connection
4. Sending the HTTP Request
5. Rendering the Page

## Key facts (checked for the video)

- The browser first parses the input: if it is not a valid URL it becomes a search query. A URL has a scheme (https), a host (example.com), an optional port, a path and an optional query string.
- Typing a bare domain usually leads to HTTPS: browsers try or upgrade to HTTPS, and sites on the HSTS preload list are always contacted over HTTPS without ever trying plain HTTP.
- DNS turns the hostname into an IP address. The browser checks its own cache, then the operating system cache (and hosts file), then asks a recursive resolver (usually the ISP's, or a public one like 1.1.1.1 or 8.8.8.8).
- On a cache miss the recursive resolver walks the hierarchy - a root server points to the TLD servers (.com), which point to the domain's authoritative name servers, which return the A record (IPv4) or AAAA record (IPv6).
- Every DNS answer has a TTL (time to live) in seconds that says how long it may be cached. Because of caching, most lookups never leave the local machine or the resolver.
- Classic DNS travels over UDP port 53 unencrypted; DNS over HTTPS (DoH) and DNS over TLS (DoT, port 853) encrypt it.
- For HTTP/1.1 and HTTP/2 the browser opens a TCP connection to port 443 with the three-way handshake - SYN, SYN-ACK, ACK - which costs one round trip before any data.
- Then TLS 1.3 adds one more round trip - ClientHello, then ServerHello plus the encrypted certificate and Finished - after which the HTTP request is sent encrypted. The SNI field in ClientHello tells the server which hostname is wanted.
- HTTP/3 runs over QUIC on UDP and combines the transport and TLS 1.3 handshakes into a single round trip. Browsers learn a site supports HTTP/3 from the Alt-Svc header or an HTTPS DNS record.
- The HTTP request is a method (GET), a path, and headers such as Host, User-Agent, Accept and Cookie. In HTTP/2 and HTTP/3 the headers are compressed and many requests share one connection.
- Large sites put a CDN or load balancer in front: the DNS answer often points to a nearby CDN edge server, which may answer from its cache or forward the request to the origin servers.
- The response has a status code (200 OK, 301 or 308 redirect, 304 Not Modified, 404 Not Found, 500 server error), headers like Content-Type and Cache-Control, and the body, usually HTML.
- The browser parses HTML into the DOM and CSS into the CSSOM, combines them into a render tree, runs layout to compute positions and sizes, then paints and composites pixels on screen.
- Discovering CSS, JavaScript, images and fonts in the HTML triggers more requests; a classic script tag without async or defer pauses HTML parsing until the script is downloaded and run.
- Connections are reused (keep-alive), and repeat visits are faster because DNS answers, TLS session tickets and cached files are reused.
