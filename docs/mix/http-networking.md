# HTTP Networking Interview Questions and Answers

_Last updated: October 28, 2026_

120 HTTP and networking interview questions with answers, split into three levels: 40 easy, 40 moderate and 40 advanced.

The answers follow the current HTTP specs: RFC 9110 (HTTP semantics), RFC 9111 (caching), RFC 9112 (HTTP/1.1), RFC 9113 (HTTP/2) and RFC 9114 (HTTP/3 over QUIC), plus TLS 1.3. Code examples use the Fetch API (in the browser or Node.js 18 and later), `curl` and Node.js where it makes sense.

## Table of Contents

- [Easy Questions (1-40)](#easy-questions-1-40)
- [Moderate Questions (41-80)](#moderate-questions-41-80)
- [Advanced Questions (81-120)](#advanced-questions-81-120)

### Easy Questions (1-40)

- [1: What is HTTP?](#1-what-is-http)
- [2: How does the request-response model work?](#2-how-does-the-request-response-model-work)
- [3: What are the parts of a URL?](#3-what-are-the-parts-of-a-url)
- [4: What does an HTTP request look like?](#4-what-does-an-http-request-look-like)
- [5: What does an HTTP response look like?](#5-what-does-an-http-response-look-like)
- [6: What are the main HTTP methods?](#6-what-are-the-main-http-methods)
- [7: What is the difference between GET and POST?](#7-what-is-the-difference-between-get-and-post)
- [8: What is the difference between PUT and PATCH?](#8-what-is-the-difference-between-put-and-patch)
- [9: What are the status code classes?](#9-what-are-the-status-code-classes)
- [10: When do you use 200, 201 and 204?](#10-when-do-you-use-200-201-and-204)
- [11: What is the difference between 301, 302, 307 and 308?](#11-what-is-the-difference-between-301-302-307-and-308)
- [12: What is the difference between 401 and 403?](#12-what-is-the-difference-between-401-and-403)
- [13: When do you return 400, 404, 409 and 422?](#13-when-do-you-return-400-404-409-and-422)
- [14: What is the difference between 500, 502, 503 and 504?](#14-what-is-the-difference-between-500-502-503-and-504)
- [15: What are HTTP headers?](#15-what-are-http-headers)
- [16: What is the Content-Type header?](#16-what-is-the-content-type-header)
- [17: What is content negotiation?](#17-what-is-content-negotiation)
- [18: What does it mean that HTTP is stateless?](#18-what-does-it-mean-that-http-is-stateless)
- [19: What are cookies?](#19-what-are-cookies)
- [20: What is the difference between HTTP and HTTPS?](#20-what-is-the-difference-between-http-and-https)
- [21: What is TLS and what is a certificate?](#21-what-is-tls-and-what-is-a-certificate)
- [22: What is DNS and why does HTTP need it?](#22-what-is-dns-and-why-does-http-need-it)
- [23: Why does HTTP use TCP?](#23-why-does-http-use-tcp)
- [24: What are ports 80 and 443?](#24-what-are-ports-80-and-443)
- [25: What is the difference between path parameters, query parameters and the request body?](#25-what-is-the-difference-between-path-parameters-query-parameters-and-the-request-body)
- [26: What is a safe HTTP method?](#26-what-is-a-safe-http-method)
- [27: What does idempotent mean?](#27-what-does-idempotent-mean)
- [28: What is the User-Agent header?](#28-what-is-the-user-agent-header)
- [29: How is authentication data usually sent over HTTP?](#29-how-is-authentication-data-usually-sent-over-http)
- [30: What is CORS?](#30-what-is-cors)
- [31: What is HTTP caching?](#31-what-is-http-caching)
- [32: What is a persistent connection (keep-alive)?](#32-what-is-a-persistent-connection-keep-alive)
- [33: What are the main HTTP versions?](#33-what-are-the-main-http-versions)
- [34: What is a proxy, and what is the difference between a forward and a reverse proxy?](#34-what-is-a-proxy-and-what-is-the-difference-between-a-forward-and-a-reverse-proxy)
- [35: What is a CDN?](#35-what-is-a-cdn)
- [36: How do you make an HTTP request with fetch?](#36-how-do-you-make-an-http-request-with-fetch)
- [37: How do you use curl to look at HTTP requests?](#37-how-do-you-use-curl-to-look-at-http-requests)
- [38: What is REST?](#38-what-is-rest)
- [39: What is HTTP compression?](#39-what-is-http-compression)
- [40: How do you inspect requests in the browser DevTools?](#40-how-do-you-inspect-requests-in-the-browser-devtools)

### Moderate Questions (41-80)

- [41: What are HEAD and OPTIONS used for?](#41-what-are-head-and-options-used-for)
- [42: What is a CORS preflight request and when does it happen?](#42-what-is-a-cors-preflight-request-and-when-does-it-happen)
- [43: How does CORS work with cookies and credentials?](#43-how-does-cors-work-with-cookies-and-credentials)
- [44: What do the main Cache-Control directives mean?](#44-what-do-the-main-cache-control-directives-mean)
- [45: How do ETag and 304 Not Modified work?](#45-how-do-etag-and-304-not-modified-work)
- [46: What is the difference between Last-Modified and ETag?](#46-what-is-the-difference-between-last-modified-and-etag)
- [47: What are s-maxage and stale-while-revalidate?](#47-what-are-s-maxage-and-stale-while-revalidate)
- [48: What is the Vary header?](#48-what-is-the-vary-header)
- [49: How do hashed file names help with caching?](#49-how-do-hashed-file-names-help-with-caching)
- [50: What are the main cookie attributes?](#50-what-are-the-main-cookie-attributes)
- [51: What are the SameSite values and what do they do?](#51-what-are-the-samesite-values-and-what-do-they-do)
- [52: Should you use session cookies or tokens like JWT?](#52-should-you-use-session-cookies-or-tokens-like-jwt)
- [53: What is the difference between Content-Encoding and Transfer-Encoding?](#53-what-is-the-difference-between-content-encoding-and-transfer-encoding)
- [54: How do you enable compression and what should you compress?](#54-how-do-you-enable-compression-and-what-should-you-compress)
- [55: How do range requests work?](#55-how-do-range-requests-work)
- [56: How do file uploads work over HTTP?](#56-how-do-file-uploads-work-over-http)
- [57: What are the main limitations of HTTP/1.1?](#57-what-are-the-main-limitations-of-http11)
- [58: What are the main features of HTTP/2?](#58-what-are-the-main-features-of-http2)
- [59: What is HPACK?](#59-what-is-hpack)
- [60: What happened to HTTP/2 server push, and what is 103 Early Hints?](#60-what-happened-to-http2-server-push-and-what-is-103-early-hints)
- [61: What is HTTP/3 and how is it different from HTTP/2?](#61-what-is-http3-and-how-is-it-different-from-http2)
- [62: How does a browser know a server supports HTTP/3?](#62-how-does-a-browser-know-a-server-supports-http3)
- [63: What happens during a TLS 1.3 handshake?](#63-what-happens-during-a-tls-13-handshake)
- [64: What is HSTS?](#64-what-is-hsts)
- [65: What is the Post/Redirect/Get pattern?](#65-what-is-the-postredirectget-pattern)
- [66: How do you handle rate limiting in HTTP?](#66-how-do-you-handle-rate-limiting-in-http)
- [67: How do you retry failed requests safely?](#67-how-do-you-retry-failed-requests-safely)
- [68: How do you add a timeout to fetch?](#68-how-do-you-add-a-timeout-to-fetch)
- [69: Why doesn't fetch throw on a 404 or 500?](#69-why-doesnt-fetch-throw-on-a-404-or-500)
- [70: What are preconnect, dns-prefetch and preload?](#70-what-are-preconnect-dns-prefetch-and-preload)
- [71: What are the options for real-time updates over HTTP?](#71-what-are-the-options-for-real-time-updates-over-http)
- [72: How do Server-Sent Events work?](#72-how-do-server-sent-events-work)
- [73: What is a good format for API error responses?](#73-what-is-a-good-format-for-api-error-responses)
- [74: How can you version an HTTP API?](#74-how-can-you-version-an-http-api)
- [75: How do you do pagination in an HTTP API?](#75-how-do-you-do-pagination-in-an-http-api)
- [76: What is the difference between a Layer 4 and a Layer 7 load balancer?](#76-what-is-the-difference-between-a-layer-4-and-a-layer-7-load-balancer)
- [77: How does the server find the real client IP behind a proxy?](#77-how-does-the-server-find-the-real-client-ip-behind-a-proxy)
- [78: How do you prevent lost updates when two users edit the same resource?](#78-how-do-you-prevent-lost-updates-when-two-users-edit-the-same-resource)
- [79: How does connection reuse work in Node.js?](#79-how-does-connection-reuse-work-in-nodejs)
- [80: How do you find out why a request is slow?](#80-how-do-you-find-out-why-a-request-is-slow)

### Advanced Questions (81-120)

- [81: What happens, step by step, when you type a URL into the browser and press Enter?](#81-what-happens-step-by-step-when-you-type-a-url-into-the-browser-and-press-enter)
- [82: How do TCP slow start and the congestion window affect page load?](#82-how-do-tcp-slow-start-and-the-congestion-window-affect-page-load)
- [83: How is head-of-line blocking different in HTTP/1.1, HTTP/2 and HTTP/3?](#83-how-is-head-of-line-blocking-different-in-http11-http2-and-http3)
- [84: How does QUIC connection migration work?](#84-how-does-quic-connection-migration-work)
- [85: What is 0-RTT and what are the risks?](#85-what-is-0-rtt-and-what-are-the-risks)
- [86: How does request prioritization work in HTTP/2 and HTTP/3?](#86-how-does-request-prioritization-work-in-http2-and-http3)
- [87: What is flow control in HTTP/2?](#87-what-is-flow-control-in-http2)
- [88: What is QPACK and why couldn't HTTP/3 just use HPACK?](#88-what-is-qpack-and-why-couldnt-http3-just-use-hpack)
- [89: What is HTTP request smuggling?](#89-what-is-http-request-smuggling)
- [90: What was the HTTP/2 Rapid Reset attack?](#90-what-was-the-http2-rapid-reset-attack)
- [91: What is HTTP header injection or response splitting?](#91-what-is-http-header-injection-or-response-splitting)
- [92: What is a Host header attack?](#92-what-is-a-host-header-attack)
- [93: What are web cache poisoning and web cache deception?](#93-what-are-web-cache-poisoning-and-web-cache-deception)
- [94: How do you protect against CSRF?](#94-how-do-you-protect-against-csrf)
- [95: Which security headers should a web app send?](#95-which-security-headers-should-a-web-app-send)
- [96: How does a browser validate a certificate, and what is mTLS?](#96-how-does-a-browser-validate-a-certificate-and-what-is-mtls)
- [97: What are SNI and Encrypted Client Hello?](#97-what-are-sni-and-encrypted-client-hello)
- [98: Which HTTP/1.1-era optimizations hurt you under HTTP/2 and HTTP/3?](#98-which-http11-era-optimizations-hurt-you-under-http2-and-http3)
- [99: What is HTTP/2 connection coalescing?](#99-what-is-http2-connection-coalescing)
- [100: How would you design HTTP caching for a single-page app?](#100-how-would-you-design-http-caching-for-a-single-page-app)
- [101: How do CDN cache keys and purging work?](#101-how-do-cdn-cache-keys-and-purging-work)
- [102: What is stale-if-error and how does it help resilience?](#102-what-is-stale-if-error-and-how-does-it-help-resilience)
- [103: How do browser privacy changes affect cookies and cross-site requests?](#103-how-do-browser-privacy-changes-affect-cookies-and-cross-site-requests)
- [104: What are COOP, COEP and CORP, and what is cross-origin isolation?](#104-what-are-coop-coep-and-corp-and-what-is-cross-origin-isolation)
- [105: How would you handle very large file uploads?](#105-how-would-you-handle-very-large-file-uploads)
- [106: How do you stream HTTP responses and handle backpressure?](#106-how-do-you-stream-http-responses-and-handle-backpressure)
- [107: Why can mismatched keep-alive timeouts cause random 502 errors?](#107-why-can-mismatched-keep-alive-timeouts-cause-random-502-errors)
- [108: How do you avoid retry storms?](#108-how-do-you-avoid-retry-storms)
- [109: How do idempotency keys work and how would you implement them?](#109-how-do-idempotency-keys-work-and-how-would-you-implement-them)
- [110: How do you measure network performance from real users?](#110-how-do-you-measure-network-performance-from-real-users)
- [111: How would you reduce Time to First Byte?](#111-how-would-you-reduce-time-to-first-byte)
- [112: How does gRPC use HTTP/2, and why can't browsers use it directly?](#112-how-does-grpc-use-http2-and-why-cant-browsers-use-it-directly)
- [113: What are the practical downsides of HTTP/3?](#113-what-are-the-practical-downsides-of-http3)
- [114: Why can compressing secrets in HTTPS responses be dangerous?](#114-why-can-compressing-secrets-in-https-responses-be-dangerous)
- [115: Why might SSE or streaming responses not stream through a proxy?](#115-why-might-sse-or-streaming-responses-not-stream-through-a-proxy)
- [116: An API call works in Postman but fails in the browser with a CORS error. How do you debug it?](#116-an-api-call-works-in-postman-but-fails-in-the-browser-with-a-cors-error-how-do-you-debug-it)
- [117: Users report random 502 and 504 errors. How do you investigate?](#117-users-report-random-502-and-504-errors-how-do-you-investigate)
- [118: Your API is slow for users far from your data center. What would you do?](#118-your-api-is-slow-for-users-far-from-your-data-center-what-would-you-do)
- [119: How would you design the HTTP contract for a new public API?](#119-how-would-you-design-the-http-contract-for-a-new-public-api)
- [120: How do you shut down an HTTP server without dropping requests?](#120-how-do-you-shut-down-an-http-server-without-dropping-requests)

---

# Easy Questions (1-40)

## 1: What is HTTP?

HTTP (HyperText Transfer Protocol) is the protocol browsers, apps and servers use to talk to each other on the web. A client sends a request, the server sends back a response, and both are made of a start line, headers and an optional body.

It was first made for fetching HTML pages, but today it carries almost everything: JSON APIs, images, video, file uploads and so on. HTTP itself only defines the messages and their meaning. The actual bytes travel over a transport like TCP (HTTP/1.1 and HTTP/2) or QUIC (HTTP/3).

## 2: How does the request-response model work?

The client always starts. It opens a connection to the server, sends a request ("give me `/users/42`"), and waits. The server processes it and sends back exactly one response for that request, with a status code, headers and usually a body.

The server can't send a normal HTTP response without a request first. When you need the server to push data to the client, you use something on top of HTTP like Server-Sent Events, or a different protocol like WebSockets.

## 3: What are the parts of a URL?

Take `https://api.example.com:8443/users/42?sort=name&page=2#details`:

- `https` is the scheme (which protocol to use)
- `api.example.com` is the host
- `8443` is the port (optional, defaults are 80 for http and 443 for https)
- `/users/42` is the path
- `?sort=name&page=2` is the query string
- `#details` is the fragment

The fragment is never sent to the server. The browser keeps it and uses it to scroll to an element or for client-side routing.

## 4: What does an HTTP request look like?

An HTTP/1.1 request is plain text. It has a request line (method, path, version), headers, an empty line, and an optional body:

```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 27

{"name":"Ana","age":31}
```

The `Host` header is required in HTTP/1.1 because one IP address can serve many domains. In HTTP/2 and HTTP/3 the same information is sent in binary frames, but the meaning (method, path, headers, body) is the same.

## 5: What does an HTTP response look like?

It has a status line (version, status code, reason phrase), headers, an empty line and the body:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 36
Cache-Control: no-store

{"id":42,"name":"Ana","age":31}
```

The status code tells the client what happened, the headers describe the response (type, size, caching rules, cookies), and the body holds the actual data.

## 6: What are the main HTTP methods?

- `GET` reads a resource.
- `POST` sends data to the server, often to create something or to trigger an action.
- `PUT` replaces a resource with the data you send.
- `PATCH` changes part of a resource.
- `DELETE` removes a resource.
- `HEAD` is like `GET` but returns only headers, no body.
- `OPTIONS` asks what the server allows for a URL. Browsers use it for CORS preflight requests.

There are also `CONNECT` (used to open a tunnel through a proxy, for example for HTTPS) and `TRACE` (for debugging, usually disabled).

## 7: What is the difference between GET and POST?

`GET` is for reading. Parameters go in the URL, it should not change anything on the server, and responses can be cached, bookmarked and shared as links.

`POST` is for sending data, usually in the body. It often changes server state (creating an order, sending a message), it's not cached by default, and the browser warns you before resending it on refresh.

A `GET` request with a body is allowed by the spec, but the body has no defined meaning and many servers and proxies drop it, so don't rely on it. Also don't put secrets in `GET` query strings: URLs end up in logs, browser history and `Referer` headers.

## 8: What is the difference between PUT and PATCH?

`PUT` replaces the whole resource with what you send. If you leave a field out, it should be removed or reset. `PATCH` only changes the fields you send.

```http
PUT /users/42
{"name":"Ana","email":"ana@example.com","age":31}

PATCH /users/42
{"age":32}
```

`PUT` is idempotent: sending the same request twice leaves the resource in the same state. `PATCH` is not guaranteed to be idempotent. For example, a patch like "add 1 to the counter" gives a different result each time.

## 9: What are the status code classes?

The first digit tells you the category:

- `1xx` informational, the request is still being processed (`100 Continue`, `103 Early Hints`)
- `2xx` success (`200 OK`, `201 Created`, `204 No Content`)
- `3xx` redirection (`301`, `302`, `304 Not Modified`)
- `4xx` client error, the request is wrong (`400`, `401`, `403`, `404`)
- `5xx` server error, the request looked fine but the server failed (`500`, `502`, `503`)

Clients that don't know a specific code should treat it like the `x00` code of its class. For example, an unknown `418` is handled like `400`.

## 10: When do you use 200, 201 and 204?

- `200 OK` is the general success response with a body, like the result of a `GET`.
- `201 Created` means a new resource was created, usually after a `POST`. It's good practice to send a `Location` header with the URL of the new resource.
- `204 No Content` means success but there is nothing to send back. It's common for `DELETE` or for a `PUT` where the client doesn't need the updated object.

```http
HTTP/1.1 201 Created
Location: /api/orders/981
Content-Type: application/json

{"id":981,"status":"pending"}
```

## 11: What is the difference between 301, 302, 307 and 308?

All four send the client to another URL in the `Location` header. They differ in two ways: is the move permanent, and can the client change the method?

| Code | Permanent? | Method kept?                                 |
| ---- | ---------- | -------------------------------------------- |
| 301  | Yes        | Not guaranteed (browsers turn POST into GET) |
| 302  | No         | Not guaranteed (browsers turn POST into GET) |
| 307  | No         | Yes, method and body stay the same           |
| 308  | Yes        | Yes, method and body stay the same           |

Use `301` or `308` when a URL moved for good (search engines update their index). Use `307` or `308` when you need a `POST` to stay a `POST` after the redirect.

## 12: What is the difference between 401 and 403?

`401 Unauthorized` really means "not authenticated". The server doesn't know who you are, or your credentials are missing or invalid. It should send a `WWW-Authenticate` header that says how to authenticate.

`403 Forbidden` means the server knows who you are (or doesn't care), but you're not allowed to do this. Logging in again won't help.

A simple example: no token or an expired token gives `401`. A valid token for a normal user calling an admin-only endpoint gives `403`.

## 13: When do you return 400, 404, 409 and 422?

- `400 Bad Request` means the request is broken: invalid JSON, missing required parameter, wrong type.
- `404 Not Found` means there's nothing at that URL. Some APIs also return `404` instead of `403` to hide that a resource exists.
- `409 Conflict` means the request clashes with the current state, like creating a user with an email that's already taken.
- `422 Unprocessable Content` means the request is well formed but the data fails validation, like an end date before the start date.

Teams often argue about `400` versus `422` for validation errors. Either is fine as long as the API is consistent and the error body explains what's wrong.

## 14: What is the difference between 500, 502, 503 and 504?

- `500 Internal Server Error` is a generic error in the application itself, like an unhandled exception.
- `502 Bad Gateway` comes from a proxy or load balancer that got an invalid response from the server behind it (or the connection to it was refused or reset).
- `503 Service Unavailable` means the server can't handle requests right now, usually because it's overloaded or in maintenance. It can send `Retry-After`.
- `504 Gateway Timeout` comes from a proxy that waited too long for the server behind it.

When you see `502` or `504`, the problem is usually between the proxy and your app, so check both the proxy logs and the app logs.

## 15: What are HTTP headers?

Headers are key-value pairs sent with requests and responses. They carry metadata: what format the body is in, how long it can be cached, who the client is, authentication data, cookies and so on.

Some common ones:

- Request: `Host`, `Accept`, `Authorization`, `Cookie`, `User-Agent`, `Content-Type`
- Response: `Content-Type`, `Content-Length`, `Cache-Control`, `Set-Cookie`, `Location`, `ETag`

Header names are case-insensitive. HTTP/2 and HTTP/3 require them to be sent in lowercase.

## 16: What is the Content-Type header?

It tells the other side what format the body is in, so it knows how to read it. It is a media type (also called MIME type), sometimes with a charset:

```http
Content-Type: application/json
Content-Type: text/html; charset=utf-8
Content-Type: multipart/form-data; boundary=----abc123
```

Clients send it with a body (for example on `POST`), and servers send it with responses. If it's wrong, things break in odd ways. For example, an Express app using `express.json()` ignores a JSON body sent as `text/plain`, so `req.body` ends up empty.

## 17: What is content negotiation?

It's how a client and server agree on the format of a response. The client says what it can handle with `Accept` headers, and the server picks the best match:

```http
Accept: application/json, text/html;q=0.9
Accept-Language: de, en;q=0.8
Accept-Encoding: gzip, br, zstd
```

The `q` value is a weight from 0 to 1 (1 is the default). The server replies with the chosen `Content-Type`, `Content-Language` or `Content-Encoding`. If it can't produce anything acceptable it can return `406 Not Acceptable`, though most servers just send their default format.

## 18: What does it mean that HTTP is stateless?

Each request stands on its own. The server doesn't remember anything about the previous request from the same client just because of HTTP itself.

To build things like logins and shopping carts, the client sends the state (or a reference to it) with every request. The usual ways are:

- Cookies with a session ID that points to data stored on the server
- Tokens (like a JWT) in the `Authorization` header
- Data in the URL or the request body

Statelessness is also what makes HTTP servers easy to scale: any server behind a load balancer can handle any request, as long as the shared state lives in a database or cache.

## 19: What are cookies?

Cookies are small pieces of data the server asks the browser to store with the `Set-Cookie` header. The browser then sends them back automatically on later requests to the same site in the `Cookie` header.

```http
HTTP/1.1 200 OK
Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```

```http
GET /account HTTP/1.1
Cookie: sessionId=abc123
```

They're mostly used for sessions, user preferences and tracking. Each cookie is limited to about 4 KB, and since they're sent with every matching request, large cookies slow down every request.

## 20: What is the difference between HTTP and HTTPS?

HTTPS is HTTP sent over a TLS-encrypted connection. Plain HTTP sends everything as readable text, so anyone on the network path (public Wi-Fi, an ISP, a compromised router) can read and change it.

HTTPS gives you three things:

- Encryption, so others can't read the traffic
- Integrity, so others can't change it without being noticed
- Authentication, so the client knows it's talking to the real server, thanks to the certificate

Today HTTPS is the default. Browsers mark HTTP pages as "Not secure", and many features (service workers, geolocation, HTTP/2 and HTTP/3 in browsers) only work over HTTPS.

## 21: What is TLS and what is a certificate?

TLS (Transport Layer Security) is the protocol that encrypts the connection under HTTPS. The current version is TLS 1.3. SSL is the old name, and all SSL versions are broken and disabled.

A certificate is a file that ties a public key to a domain name. It's signed by a Certificate Authority (CA) that the browser trusts. During the TLS handshake, the server sends its certificate, the browser checks that it's signed by a trusted CA, is not expired and matches the domain, and then both sides agree on keys to encrypt the rest of the connection.

Services like Let's Encrypt give out free certificates and renew them automatically.

## 22: What is DNS and why does HTTP need it?

DNS (Domain Name System) turns a name like `api.example.com` into an IP address like `93.184.215.14` that computers can connect to. Before the browser can open a connection, it has to look up the address.

The lookup goes through several caches first (browser, OS, router, the ISP's resolver). If none of them have it, the resolver asks the root servers, then the `.com` servers, then the domain's own name servers. Each record has a TTL that says how long it can be cached.

A slow DNS lookup adds directly to page load time, which is why browsers cache results and why `dns-prefetch` exists.

## 23: Why does HTTP use TCP?

HTTP/1.1 and HTTP/2 run on top of TCP because TCP gives a reliable, ordered stream of bytes. It handles lost packets, retransmissions and ordering, so HTTP doesn't have to.

Before sending data, TCP does a three-way handshake (SYN, SYN-ACK, ACK), which costs one round trip. HTTPS then adds the TLS handshake on top.

HTTP/3 is different: it uses QUIC, which runs on UDP and handles reliability itself. That lets it fix some TCP problems, like head-of-line blocking and slow connection setup.

## 24: What are ports 80 and 443?

A port is a number that tells the operating system which program on a machine should get the traffic. By convention, HTTP servers listen on port 80 and HTTPS servers on port 443, so browsers use those when the URL doesn't name a port.

`http://example.com` is the same as `http://example.com:80`, and `https://example.com` is the same as `https://example.com:443`. During development you usually see other ports like `3000`, `5173` or `8080`, because ports below 1024 need special permissions on most systems.

## 25: What is the difference between path parameters, query parameters and the request body?

- Path parameters identify a resource: `/users/42/orders/7`.
- Query parameters filter, sort or page through data: `/orders?status=paid&page=2`.
- The body carries the data you're sending, usually with `POST`, `PUT` or `PATCH`.

```js
const params = new URLSearchParams({ status: "paid", page: "2" });

await fetch(`/api/users/42/orders?${params}`);

await fetch("/api/users/42/orders", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ productId: 5, quantity: 1 }),
});
```

`URLSearchParams` takes care of encoding special characters like spaces and `&`.

## 26: What is a safe HTTP method?

A safe method is one that's only meant to read data, not change anything on the server. `GET`, `HEAD`, `OPTIONS` and `TRACE` are safe.

This matters because browsers, crawlers and proxies feel free to call safe methods on their own: prefetching links, retrying, caching. If your `GET /delete-account?id=5` actually deletes something, a crawler or link preview bot can trigger it. Things like logging and counters are fine, as long as the client didn't ask for a change.

## 27: What does idempotent mean?

A method is idempotent if sending the same request once or many times leaves the server in the same state. `GET`, `HEAD`, `OPTIONS`, `PUT` and `DELETE` are idempotent. `POST` and `PATCH` are not by default.

For example, `DELETE /orders/7` deletes the order the first time. The second call might return `404`, but the state is the same: the order is gone. Two `POST /orders` calls, on the other hand, can create two orders.

This matters for retries. If a request times out, a client can safely retry an idempotent one, but retrying a `POST` can create duplicates unless you use something like an idempotency key.

## 28: What is the User-Agent header?

It's a request header where the client says what it is, for example the browser, its version and the OS:

```http
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
```

Servers use it for analytics, bot detection and sometimes to serve different content. It's not reliable though: anyone can fake it, and browsers now freeze or reduce parts of it for privacy. Chromium browsers offer User-Agent Client Hints (`Sec-CH-UA` headers) as a more structured option. For features, check if they exist in code instead of reading the user agent.

## 29: How is authentication data usually sent over HTTP?

The most common ways are:

- A session cookie that the browser sends automatically
- A token in the `Authorization` header, usually a Bearer token like a JWT or an OAuth access token
- Basic auth, where the header holds `username:password` encoded in Base64 (only safe over HTTPS)
- An API key in a custom header like `X-API-Key`

```js
await fetch("/api/profile", {
  headers: { Authorization: `Bearer ${accessToken}` },
});
```

Base64 is not encryption, so whatever is in these headers is readable unless the connection uses HTTPS.

## 30: What is CORS?

CORS (Cross-Origin Resource Sharing) is the way a server tells the browser which other origins are allowed to read its responses. An origin is scheme + host + port, so `https://app.com` and `https://api.app.com` are different origins.

By default the browser's same-origin policy blocks JavaScript on one origin from reading responses from another. If the API sends a header like this, the browser lets the page read the response:

```http
Access-Control-Allow-Origin: https://app.com
```

CORS is enforced by the browser only. Tools like `curl` and Postman, and server-to-server calls, ignore it completely. It's not a way to protect your API from other clients.

## 31: What is HTTP caching?

Caching means storing a response and reusing it later instead of downloading it again. Caches live in the browser, in CDNs and in proxies. The server controls caching mostly with the `Cache-Control` header:

```http
Cache-Control: max-age=3600
```

This says the response is fresh for an hour. During that time the browser uses its copy without asking the server. After that, it can check with the server whether the copy is still valid, and if it is, the server answers with a tiny `304 Not Modified` instead of the full body.

Good caching cuts load time and server traffic a lot, especially for static files like JS, CSS and images.

## 32: What is a persistent connection (keep-alive)?

In early HTTP/1.0, each request opened a new TCP connection and closed it after the response. That's slow, because every new connection needs a TCP handshake and, with HTTPS, a TLS handshake.

HTTP/1.1 keeps connections open by default, so several requests can reuse the same connection one after another. The connection is closed when either side sends `Connection: close` or it stays idle too long. HTTP/2 and HTTP/3 go further and send many requests at the same time over a single connection.

## 33: What are the main HTTP versions?

- HTTP/0.9 (1991): only `GET`, no headers, only HTML.
- HTTP/1.0 (1996): headers, status codes, other content types. One request per connection.
- HTTP/1.1 (1997, updated many times, now RFC 9112): persistent connections, `Host` header, chunked transfer, better caching. Still very common.
- HTTP/2 (2015, now RFC 9113): binary framing, many requests at once over one connection, header compression.
- HTTP/3 (2022, RFC 9114): runs over QUIC (on UDP) instead of TCP, faster connection setup and no TCP head-of-line blocking.

The methods, status codes and headers mean the same thing in all of them. What changes is how messages are sent over the network.

## 34: What is a proxy, and what is the difference between a forward and a reverse proxy?

A proxy is a server that sits between the client and the target server and passes requests along.

A forward proxy works for the client. Companies use them to filter or log employee traffic, and the target server sees the proxy instead of the user.

A reverse proxy works for the server. Clients think they're talking to the real server, but the proxy (Nginx, HAProxy, Envoy, a cloud load balancer) receives the request and forwards it to one of the app servers behind it. Reverse proxies handle TLS, load balancing, caching, compression and rate limiting, so the app servers don't have to.

## 35: What is a CDN?

A CDN (Content Delivery Network) is a big network of servers in many locations around the world that cache your content close to users. When someone in Tokyo requests your image, they get it from a server in or near Tokyo instead of your origin server in Frankfurt.

This makes responses faster (shorter distance, fewer round trips) and takes load off your origin. Cloudflare, Akamai, Fastly and CloudFront are common examples. Most CDNs also give you TLS termination, DDoS protection, HTTP/3 and the option to run code at the edge.

## 36: How do you make an HTTP request with fetch?

`fetch` is built into browsers and Node.js (18 and later). It returns a promise that resolves to a `Response`:

```js
const res = await fetch("https://api.example.com/users/42");

if (!res.ok) {
  throw new Error(`Request failed with status ${res.status}`);
}

const user = await res.json();
```

For other methods, pass an options object:

```js
await fetch("https://api.example.com/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Ana" }),
});
```

Note that `fetch` only rejects on network errors. A `404` or `500` still resolves, so you have to check `res.ok` or `res.status` yourself.

## 37: How do you use curl to look at HTTP requests?

`curl` is a command-line HTTP client. A few handy options:

```bash
# show response headers and body
curl -i https://example.com

# show only headers (sends a HEAD request)
curl -I https://example.com

# show the full conversation, including TLS and request headers
curl -v https://example.com

# send JSON with POST
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana"}'

# follow redirects
curl -L http://example.com
```

It's the quickest way to see what a server really returns, without the browser's cache, CORS rules or extensions getting in the way.

## 38: What is REST?

REST (Representational State Transfer) is a style for designing APIs on top of HTTP. The main ideas are:

- Everything is a resource with its own URL (`/users/42`)
- You use HTTP methods for actions (`GET` to read, `POST` to create, `DELETE` to remove)
- Requests are stateless
- Responses say whether they can be cached
- You use standard status codes

In practice, "REST API" usually just means a JSON API that follows these conventions. Strict REST also includes HATEOAS (responses contain links to related actions), but few APIs do that.

## 39: What is HTTP compression?

The server compresses the response body before sending it, and the browser decompresses it. The client says which formats it supports, and the server says which one it used:

```http
Accept-Encoding: gzip, deflate, br, zstd
```

```http
Content-Encoding: br
```

`gzip` works everywhere. Brotli (`br`) usually gives smaller files for text. Zstandard (`zstd`) is newer, fast and supported in current Chromium and Firefox. Text files like HTML, CSS, JS and JSON often shrink by 70% or more. Images like JPEG, PNG and WebP are already compressed, so compressing them again doesn't help.

## 40: How do you inspect requests in the browser DevTools?

Open DevTools and go to the Network tab, then reload the page. Each row is one request. Clicking it shows:

- Headers: the URL, method, status code, request and response headers
- Payload: query parameters and request body
- Preview and Response: the response body
- Timing: how long each step took (queueing, DNS, connection, TLS, waiting for the server, downloading)

Useful options are "Disable cache" to skip the browser cache, throttling to simulate a slow connection, and the "Protocol" column (right-click the column headers) to see if a request used `http/1.1`, `h2` or `h3`. You can also right-click a request and use "Copy as cURL" to replay it in a terminal.

# Moderate Questions (41-80)

## 41: What are HEAD and OPTIONS used for?

`HEAD` returns the same headers as `GET` would, but no body. You use it to check if a resource exists, see its size (`Content-Length`) or check if it changed (`ETag`, `Last-Modified`) without downloading it.

`OPTIONS` asks the server what's allowed for a URL. The server can answer with an `Allow` header listing the methods. Its most common use today is the CORS preflight: the browser sends `OPTIONS` before certain cross-origin requests to ask if the real request is allowed.

```bash
curl -I https://example.com/big-file.zip
curl -X OPTIONS -i https://api.example.com/users
```

## 42: What is a CORS preflight request and when does it happen?

For requests that could have side effects, the browser first sends an `OPTIONS` request to ask the server for permission. This is the preflight. A request needs one if it's not a "simple request", for example when:

- The method is not `GET`, `HEAD` or `POST`
- It has custom headers like `Authorization` or `X-Request-Id`
- `Content-Type` is not one of `application/x-www-form-urlencoded`, `multipart/form-data` or `text/plain` (so `application/json` triggers a preflight)

```http
OPTIONS /api/orders HTTP/1.1
Origin: https://app.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type, authorization
```

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: content-type, authorization
Access-Control-Max-Age: 600
```

`Access-Control-Max-Age` lets the browser cache the preflight result so it doesn't send one before every request. Browsers cap this value (Chrome at 2 hours).

## 43: How does CORS work with cookies and credentials?

By default, cross-origin `fetch` doesn't send cookies. You have to ask for it on the client, and the server has to allow it:

```js
await fetch("https://api.app.com/me", { credentials: "include" });
```

```http
Access-Control-Allow-Origin: https://app.com
Access-Control-Allow-Credentials: true
```

With credentials, the server can't use `*` for `Access-Control-Allow-Origin`, `Access-Control-Allow-Headers` or `Access-Control-Allow-Methods`. It has to send the exact origin. If you reflect the request's `Origin` header back, check it against an allow list first, otherwise any site can make logged-in requests and read the responses. Also add `Vary: Origin` so caches don't serve one origin's response to another.

## 44: What do the main Cache-Control directives mean?

- `max-age=N`: the response is fresh for N seconds.
- `no-cache`: the cache can store it, but must check with the server before every use. It does not mean "don't cache".
- `no-store`: don't store it anywhere. Use this for sensitive data.
- `private`: only the user's browser can cache it, not CDNs or shared proxies.
- `public`: shared caches can store it, even if it would normally not be cacheable (for example a response to a request with `Authorization`).
- `must-revalidate`: once stale, the cache must not use it without checking with the server.
- `immutable`: the content will never change, so don't revalidate even on reload.
- `s-maxage=N`: like `max-age` but only for shared caches like CDNs.

```http
Cache-Control: private, no-cache
Cache-Control: public, max-age=31536000, immutable
```

## 45: How do ETag and 304 Not Modified work?

An `ETag` is an ID for a specific version of a resource, often a hash of its content. The server sends it with the response:

```http
HTTP/1.1 200 OK
ETag: "a1b2c3"
Cache-Control: no-cache
```

When the browser needs the resource again and its copy is stale (or `no-cache` is set), it asks with `If-None-Match`:

```http
GET /api/settings HTTP/1.1
If-None-Match: "a1b2c3"
```

If the resource hasn't changed, the server replies `304 Not Modified` with no body, and the browser uses its stored copy. This saves bandwidth, but it still costs a round trip. ETags that start with `W/` are weak ETags, which means "same meaning" rather than "same bytes".

## 46: What is the difference between Last-Modified and ETag?

Both let the client check if its copy is still current. `Last-Modified` is a date, and the client sends it back with `If-Modified-Since`. `ETag` is an opaque value, and the client sends it back with `If-None-Match`.

ETags are more precise. Dates only have one-second resolution, files can be touched without changing, and a file can change twice in one second. If both are present, servers check `If-None-Match` first.

One catch with ETags: if each server behind a load balancer generates them differently (for example using file inode numbers), the same file gets different ETags and revalidation fails. Base them on the content.

## 47: What are s-maxage and stale-while-revalidate?

`s-maxage` sets the freshness time for shared caches like CDNs and overrides `max-age` there. That lets you cache short in the browser and longer on the CDN:

```http
Cache-Control: public, max-age=60, s-maxage=600, stale-while-revalidate=30
```

`stale-while-revalidate=30` means that for 30 seconds after the response goes stale, the cache can still serve the old copy right away while it fetches a new one in the background. Users get a fast response and the content still gets updated. Browsers and most CDNs support it.

## 48: What is the Vary header?

`Vary` tells caches which request headers changed the response. The cache then stores separate copies for different values of those headers.

```http
Vary: Accept-Encoding
Vary: Accept-Language, Origin
```

For example, if the server sends gzip to one client and Brotli to another, it must send `Vary: Accept-Encoding`, or a cache might hand Brotli data to a client that can't read it.

Be careful with `Vary: User-Agent` or `Vary: Cookie`. There are thousands of different values, so the cache ends up with almost no hits. Many CDNs handle `Vary` in limited ways, so check your CDN docs.

## 49: How do hashed file names help with caching?

Build tools like Vite and webpack put a content hash in the file name, like `app.3f9a1c.js`. When the file changes, its name changes too. That lets you cache these files forever:

```http
Cache-Control: public, max-age=31536000, immutable
```

The HTML file that points to them is not hashed, so you cache it briefly or with `no-cache`. After a deploy, the browser gets the new HTML, sees new file names, and downloads only the files that changed. Files that didn't change keep their old names and still come from cache.

## 50: What are the main cookie attributes?

```http
Set-Cookie: sid=abc123; Domain=example.com; Path=/; Max-Age=86400; Secure; HttpOnly; SameSite=Lax
```

- `Expires` or `Max-Age`: when the cookie expires. Without them it's a session cookie that goes away when the browser session ends.
- `Domain`: which hosts get the cookie. If you leave it out, only the exact host that set it gets it. If you set it, subdomains get it too.
- `Path`: only send for URLs under this path.
- `Secure`: only send over HTTPS.
- `HttpOnly`: JavaScript can't read it with `document.cookie`, which protects it from XSS.
- `SameSite`: controls whether it's sent on cross-site requests.
- `Partitioned`: stores the cookie separately per top-level site (CHIPS), for embedded third-party content.

Cookie names starting with `__Host-` must be `Secure`, have `Path=/` and no `Domain`, which locks them to one host.

## 51: What are the SameSite values and what do they do?

`SameSite` decides if the browser sends a cookie on requests coming from other sites:

- `Strict`: only sent when the request starts on the same site. Even clicking a link from another site to yours won't include it, so the user looks logged out on that first page.
- `Lax`: sent on same-site requests and on top-level navigations with safe methods (clicking a link to your site). Not sent on cross-site `POST`, iframes, images or `fetch`. Chrome and Edge use `Lax` when the attribute is missing; Firefox and Safari don't apply that default, so set the attribute yourself.
- `None`: always sent, including cross-site. Requires `Secure`.

"Site" here means the registrable domain plus scheme, so `app.example.com` and `api.example.com` are the same site, even though they're different origins.

## 52: Should you use session cookies or tokens like JWT?

With session cookies, the server stores the session (in memory, Redis or a database) and the cookie only holds a random ID. Logging out or revoking a session is easy: delete it on the server. Using an `HttpOnly` cookie also keeps it out of reach of JavaScript.

With JWTs, the token itself holds the user data and a signature, so the server can check it without a lookup. That works well across many services, but you can't easily revoke a token before it expires, and tokens kept in `localStorage` can be stolen by XSS.

For a normal web app on one domain, `HttpOnly` session cookies are usually the simpler and safer choice. JWTs make more sense for service-to-service calls, mobile apps and third-party APIs, ideally with short lifetimes and refresh tokens.

## 53: What is the difference between Content-Encoding and Transfer-Encoding?

`Content-Encoding` is part of the resource. The body was compressed (for example `br`) and the client should decompress it. Caches store it compressed.

`Transfer-Encoding` is about how the message is sent over one HTTP/1.1 connection. The most common value is `chunked`, which sends the body in pieces with their sizes, so the server can start sending before it knows the total length:

```http
HTTP/1.1 200 OK
Transfer-Encoding: chunked

7
Hello,
6
world!
0

```

`Transfer-Encoding` only exists in HTTP/1.1. HTTP/2 and HTTP/3 split everything into frames already, so they don't need chunked encoding and don't allow the header.

## 54: How do you enable compression and what should you compress?

Most setups do it in the reverse proxy or CDN. In Nginx for example:

```nginx
gzip on;
gzip_types text/css application/javascript application/json image/svg+xml;
gzip_min_length 1024;
```

In Node.js you can use the `compression` middleware for Express, or `@fastify/compress` for Fastify.

Compress text formats: HTML, CSS, JS, JSON, SVG, XML. Skip already compressed formats (JPEG, PNG, WebP, AVIF, MP4, ZIP, WOFF2), and very small responses where the headers cost more than you save. For static files, compress them at build time with Brotli or zstd at a high level and serve the precompressed files. That gives smaller files with no CPU cost per request.

## 55: How do range requests work?

A client can ask for only part of a file with the `Range` header. The server answers with `206 Partial Content`:

```http
GET /video.mp4 HTTP/1.1
Range: bytes=1000000-1999999
```

```http
HTTP/1.1 206 Partial Content
Content-Range: bytes 1000000-1999999/52428800
Content-Length: 1000000
Accept-Ranges: bytes
```

This is how video players jump to the middle of a video, and how download managers resume broken downloads. If the range is invalid, the server returns `416 Range Not Satisfiable`. The client can send `If-Range` with an ETag so it gets the full new file if the file changed in the meantime, instead of mixing parts of two versions.

## 56: How do file uploads work over HTTP?

HTML forms and `fetch` with `FormData` send files as `multipart/form-data`. The body is split into parts by a boundary string, and each part has its own headers:

```js
const form = new FormData();
form.append("title", "Holiday");
form.append("photo", fileInput.files[0]);

await fetch("/api/photos", { method: "POST", body: form });
```

Don't set `Content-Type` yourself here. The browser sets it to `multipart/form-data; boundary=...` with the right boundary. On the server you need a parser for it, like `multer` or `busboy` in Node.js.

For big files, sending the raw file with `PUT` (often to a pre-signed S3 URL) or using resumable uploads works better than one huge multipart request.

## 57: What are the main limitations of HTTP/1.1?

- One request at a time per connection. Pipelining exists in the spec but is broken in practice, so browsers never turned it on.
- Because of that, browsers open up to 6 connections per host to load things in parallel. Each needs its own TCP and TLS handshake.
- A slow response blocks the ones after it on the same connection (head-of-line blocking).
- Headers are plain text and repeated on every request. Cookies and user agents can add several KB per request.

Developers worked around this with tricks like bundling all JS into one file, image sprites and domain sharding. HTTP/2 fixed most of these problems at the protocol level.

## 58: What are the main features of HTTP/2?

- **Binary framing.** Messages are split into binary frames instead of plain text, which is faster and safer to parse.
- **Multiplexing.** Many requests and responses (streams) share one TCP connection at the same time, mixed together as frames. No more 6-connection limit.
- **Header compression with HPACK.** Repeated headers are sent as small references instead of full text.
- **Prioritization.** The client can hint which responses matter more.
- **Flow control** per stream and per connection.

The meaning of requests didn't change, so apps don't need code changes. In practice, browsers only use HTTP/2 over TLS, and the version is agreed during the TLS handshake with ALPN (the `h2` value).

## 59: What is HPACK?

HPACK is the header compression format of HTTP/2. Headers like `user-agent`, `accept` and `cookie` are almost the same on every request, so sending them in full each time is a waste.

HPACK uses:

- A static table of 61 common headers like `:method: GET` and `accept-encoding: gzip, deflate`
- A dynamic table per connection that stores headers already sent, so later requests can just send an index number
- Huffman coding for strings

A repeated header can shrink to one or two bytes. HPACK was designed this way, instead of just gzipping headers, to avoid the CRIME attack, where compressed secrets could be guessed by watching sizes change.

## 60: What happened to HTTP/2 server push, and what is 103 Early Hints?

Server push let the server send files (like CSS) before the browser asked for them. In practice it rarely helped. Servers often pushed files the browser already had in cache, and it was hard to get right. Chrome removed support in version 106 (2022) and Firefox followed, so you shouldn't use it.

The replacement is `103 Early Hints`. While the server is still building the page, it sends an early informational response with `Link` headers, and the browser starts loading or connecting right away:

```http
HTTP/1.1 103 Early Hints
Link: </styles/main.css>; rel=preload; as=style
Link: <https://cdn.example.com>; rel=preconnect

HTTP/1.1 200 OK
Content-Type: text/html
...
```

The browser still decides whether it needs the file, so cached files aren't downloaded again.

## 61: What is HTTP/3 and how is it different from HTTP/2?

HTTP/3 has the same features as HTTP/2 (multiplexing, header compression), but it runs on QUIC instead of TCP. QUIC is a transport protocol built on UDP that handles reliability, ordering and encryption itself.

The main benefits:

- **Faster setup.** QUIC combines the transport and TLS 1.3 handshakes into one round trip, and can use 0-RTT on repeat visits.
- **No head-of-line blocking between streams.** A lost packet only delays its own stream, not all of them like in TCP.
- **Connection migration.** A connection can survive a network change, like moving from Wi-Fi to mobile data.

It helps most on slow or lossy networks like mobile. All major browsers and CDNs support it.

## 62: How does a browser know a server supports HTTP/3?

Browsers usually connect with HTTP/2 or HTTP/1.1 first, since they don't know yet if UDP works. The server advertises HTTP/3 with the `Alt-Svc` header:

```http
Alt-Svc: h3=":443"; ma=86400
```

This says "HTTP/3 is available on UDP port 443 for the next day". The browser remembers it and tries HTTP/3 on later requests.

A faster option is the DNS `HTTPS` record (RFC 9460). It can include `alpn="h3,h2"` in the DNS answer, so the browser can try HTTP/3 on the very first connection. If UDP is blocked, the browser falls back to TCP.

## 63: What happens during a TLS 1.3 handshake?

1. The client sends `ClientHello`: the TLS versions and cipher suites it supports, a key share for key exchange, the server name (SNI) and ALPN protocols (`h2`, `http/1.1`).
2. The server replies with `ServerHello` and its own key share. From this point both sides can calculate the shared keys, so the rest is encrypted.
3. The server sends its certificate, a signature proving it owns the private key, and a `Finished` message.
4. The client checks the certificate and signature, sends its own `Finished`, and can send the HTTP request right away.

That's one round trip, down from two in TLS 1.2. On reconnects, TLS 1.3 can use 0-RTT and send data in the very first message. TLS 1.3 also removed old, weak algorithms and always uses forward secrecy.

## 64: What is HSTS?

HSTS (HTTP Strict Transport Security) tells the browser to only use HTTPS for a domain from now on:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

After seeing this, the browser automatically changes any `http://` link to `https://` for that domain and doesn't let the user click through certificate errors. This stops attacks where someone on the network intercepts the first plain HTTP request and keeps the user on HTTP (SSL stripping).

The header only works after the first HTTPS visit. To protect even the first visit, you can submit the domain to the HSTS preload list (hstspreload.org), which is built into browsers. Be careful: getting off that list takes a long time.

## 65: What is the Post/Redirect/Get pattern?

After a form `POST`, the server responds with a redirect (`303 See Other`) to a page that's loaded with `GET`:

```http
POST /orders HTTP/1.1
...

HTTP/1.1 303 See Other
Location: /orders/981
```

Without this, refreshing the result page would resend the `POST` and could create a second order. With PRG, a refresh just reloads the `GET` page. `303` always tells the client to switch to `GET`, which is exactly what you want here. Use `307` or `308` when you want the opposite, keeping the method.

## 66: How do you handle rate limiting in HTTP?

When a client sends too many requests, the server returns `429 Too Many Requests`, ideally with `Retry-After` telling the client how long to wait (in seconds or as a date):

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
Content-Type: application/problem+json

{"title":"Too many requests","detail":"Limit is 100 requests per minute"}
```

Many APIs also send the current limit so clients can slow down before they hit it. Older APIs use custom `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset` headers. The IETF is working on standard `RateLimit` and `RateLimit-Policy` headers, but that's still a draft.

On the client side, respect `Retry-After` and use backoff instead of retrying right away.

## 67: How do you retry failed requests safely?

- Only retry errors that might be temporary: network errors, timeouts, `408`, `429`, `502`, `503`, `504`. Don't retry `400`, `401`, `404` or `422`, since they'll fail again.
- Only retry automatically when the request is idempotent (`GET`, `PUT`, `DELETE`), or when the API supports idempotency keys for `POST`.
- Wait longer after each try (exponential backoff), add randomness (jitter), and cap the number of tries.

```js
async function fetchWithRetry(url, options = {}, tries = 3) {
  for (let attempt = 0; ; attempt++) {
    try {
      const res = await fetch(url, options);
      if (![429, 502, 503, 504].includes(res.status) || attempt >= tries - 1) {
        return res;
      }
    } catch (err) {
      if (attempt >= tries - 1) throw err;
    }
    const delay = 2 ** attempt * 500 + Math.random() * 300;
    await new Promise((r) => setTimeout(r, delay));
  }
}
```

## 68: How do you add a timeout to fetch?

`fetch` has no timeout option, but you can pass an `AbortSignal`. `AbortSignal.timeout()` gives you a signal that aborts after the given time:

```js
try {
  const res = await fetch("/api/report", {
    signal: AbortSignal.timeout(5000),
  });
  const data = await res.json();
} catch (err) {
  if (err.name === "TimeoutError") {
    console.log("Request took longer than 5 seconds");
  } else if (err.name === "AbortError") {
    console.log("Request was cancelled");
  } else {
    throw err;
  }
}
```

To support both a timeout and manual cancel (for example when a user leaves the page), combine signals with `AbortSignal.any([controller.signal, AbortSignal.timeout(5000)])`.

## 69: Why doesn't fetch throw on a 404 or 500?

From the HTTP point of view, a `404` or `500` is a successful exchange: the server got the request and sent back a valid response. `fetch` only rejects when it couldn't get a response at all, like a network failure, DNS error, CORS block or abort.

So you have to check the status yourself:

```js
const res = await fetch("/api/users/42");

if (!res.ok) {
  const body = await res.text();
  throw new Error(`HTTP ${res.status}: ${body}`);
}

const user = await res.json();
```

`res.ok` is `true` for status 200-299. Libraries like Axios work differently and reject for any status outside 2xx by default, which is a common source of confusion when switching between them.

## 70: What are preconnect, dns-prefetch and preload?

They're hints that tell the browser to start network work early:

```html
<link rel="dns-prefetch" href="https://fonts.gstatic.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

- `dns-prefetch` only does the DNS lookup.
- `preconnect` does DNS, TCP and TLS, so the connection is ready when it's needed. Use it for a few important third-party origins only, since open connections cost resources.
- `preload` downloads a specific file the page will need soon but that the browser would find late (fonts, a hero image referenced in CSS).

The same hints can be sent as `Link` HTTP headers, including in a `103 Early Hints` response.

## 71: What are the options for real-time updates over HTTP?

- **Short polling:** the client asks every few seconds. Simple, but wasteful and slow to react.
- **Long polling:** the client sends a request and the server holds it open until there's new data, then the client sends another one. Works everywhere but uses a lot of connections.
- **Server-Sent Events (SSE):** one long HTTP response that the server keeps writing events into. Server to client only, plain HTTP, reconnects automatically.
- **WebSockets:** a two-way connection that starts as an HTTP request and then switches protocols. Good for chat, games and collaborative editing.

For notifications, live feeds or streaming AI responses, SSE is usually enough and simpler. Use WebSockets when the client also needs to send a lot of messages with low delay.

## 72: How do Server-Sent Events work?

The server responds with `Content-Type: text/event-stream` and keeps the connection open, writing events as text:

```js
// Node.js server
import http from "node:http";

http
  .createServer((req, res) => {
    res.writeHead(200, {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
    });
    const timer = setInterval(() => {
      res.write(
        `event: tick\ndata: ${JSON.stringify({ time: Date.now() })}\n\n`,
      );
    }, 1000);
    req.on("close", () => clearInterval(timer));
  })
  .listen(3000);
```

```js
// Browser
const source = new EventSource("/events");
source.addEventListener("tick", (e) => console.log(JSON.parse(e.data)));
```

`EventSource` reconnects on its own and sends the last event ID in a `Last-Event-ID` header, so the server can resume. Over HTTP/1.1 each SSE stream uses up one of the browser's 6 connections per host. HTTP/2 doesn't have this problem.

## 73: What is a good format for API error responses?

Use a consistent JSON shape. The standard one is Problem Details (RFC 9457), with media type `application/problem+json`:

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json

{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation failed",
  "status": 422,
  "detail": "The request has 2 invalid fields",
  "instance": "/orders/981",
  "errors": [
    { "field": "email", "message": "must be a valid email" },
    { "field": "quantity", "message": "must be at least 1" }
  ]
}
```

You can add your own fields like `errors` or a `traceId`. Always return the right status code too. Returning `200` with `{"error": ...}` breaks caches, monitoring and clients that check status codes. Never put stack traces or SQL errors in production responses.

## 74: How can you version an HTTP API?

- **In the URL:** `/v1/orders`, `/v2/orders`. The most common choice. Easy to see, test and route.
- **In a header:** `Api-Version: 2024-10-01` or a custom media type like `Accept: application/vnd.example.v2+json`. Keeps URLs clean but is harder to test in a browser.
- **In a query parameter:** `/orders?version=2`. Simple but easy to forget.

Whatever you pick, try to avoid breaking changes in the first place: add new fields instead of renaming or removing them, and make clients ignore unknown fields. When you do retire a version, you can warn clients with the `Deprecation` and `Sunset` headers.

## 75: How do you do pagination in an HTTP API?

Two main ways:

- **Offset:** `?limit=20&offset=40`. Easy, and you can jump to any page, but slow on big tables and gives duplicates or missed items when data changes while paging.
- **Cursor:** `?limit=20&after=eyJpZCI6OTgxfQ`. The cursor points to the last item seen. Stable and fast, but you can only go forward and back.

You can return the next links in the body or in the standard `Link` header, like the GitHub API does:

```http
Link: <https://api.example.com/orders?after=abc&limit=20>; rel="next",
      <https://api.example.com/orders?limit=20>; rel="first"
```

Always set a maximum page size on the server so a client can't ask for a million rows at once.

## 76: What is the difference between a Layer 4 and a Layer 7 load balancer?

A Layer 4 load balancer works at the TCP/UDP level. It sees IP addresses and ports, not HTTP. It just forwards connections, so it's very fast, and TLS can pass straight through to the servers. AWS NLB is an example.

A Layer 7 load balancer understands HTTP. It ends the TLS connection, reads the request, and can route by path, host or header (`/api` to one service, `/images` to another). It can also add headers, do retries, health checks on HTTP endpoints, sticky sessions with cookies, compression and caching. Nginx, Envoy and AWS ALB are examples.

Most web apps use a Layer 7 balancer, sometimes behind a Layer 4 one.

## 77: How does the server find the real client IP behind a proxy?

When a proxy or load balancer forwards a request, the app sees the proxy's IP as the remote address. Proxies add the original IP to a header:

```http
X-Forwarded-For: 203.0.113.7, 10.0.0.12
X-Forwarded-Proto: https
X-Forwarded-Host: shop.example.com
```

The standard version is the `Forwarded` header (`Forwarded: for=203.0.113.7;proto=https`), but `X-Forwarded-*` is still more common.

The client can send a fake `X-Forwarded-For`, so only trust the parts added by your own proxies. In Express, you set `app.set("trust proxy", 1)` (the number of proxies in front of the app), and then `req.ip` returns the correct value. If you trust everything, attackers can get around IP-based rate limits.

## 78: How do you prevent lost updates when two users edit the same resource?

Use conditional requests with ETags (optimistic locking). The client reads the resource and keeps its ETag. When it saves, it sends the ETag back in `If-Match`:

```http
PUT /api/docs/12 HTTP/1.1
If-Match: "v7"
Content-Type: application/json

{"title":"New title","body":"..."}
```

If someone else saved in the meantime, the ETag on the server is now `"v8"`, so the server rejects the update with `412 Precondition Failed`. The client can then reload, show the changes and let the user try again. Without this, the second save silently overwrites the first. A server can also require `If-Match` and return `428 Precondition Required` when it's missing.

## 79: How does connection reuse work in Node.js?

Opening a new TCP and TLS connection for every outgoing request is slow, so HTTP clients keep connections open in a pool and reuse them.

The built-in `fetch` in Node.js is powered by undici, which keeps connections alive and pools them per origin by default. You can tune the pool with an undici `Agent`:

```js
import { Agent, setGlobalDispatcher } from "undici";

setGlobalDispatcher(
  new Agent({
    connections: 50,
    keepAliveTimeout: 10_000,
  }),
);
```

For the older `http` and `https` modules, `http.globalAgent` has keep-alive turned on by default since Node.js 19. Connection reuse makes a big difference for services that call other APIs a lot, because it removes a handshake from almost every call.

## 80: How do you find out why a request is slow?

Look at the timing breakdown in DevTools (Network tab, Timing) or use `curl`:

```bash
curl -o /dev/null -s -w "dns: %{time_namelookup}s
connect: %{time_connect}s
tls: %{time_appconnect}s
ttfb: %{time_starttransfer}s
total: %{time_total}s
" https://api.example.com/orders
```

Then check which step is big:

- Long DNS: slow resolver or no caching.
- Long connect or TLS: far away server, no connection reuse, no CDN.
- Long TTFB (waiting for the server): slow backend code, database queries or upstream calls. Look at server logs and traces. A `Server-Timing` header helps here.
- Long download: big response, no compression, slow network.
- Long "Queueing" or "Stalled" in the browser: too many requests to one host on HTTP/1.1, or lower priority.

# Advanced Questions (81-120)

## 81: What happens, step by step, when you type a URL into the browser and press Enter?

1. **Parse the input.** The browser decides if it's a URL or a search. If the domain is on the HSTS list, `http` becomes `https` right away.
2. **Check caches.** A service worker or the HTTP cache may answer without any network request.
3. **DNS lookup.** Browser cache, OS cache, then the configured resolver. It may also fetch the `HTTPS` record to learn about HTTP/3 support.
4. **Connect.** TCP handshake and then TLS handshake (or a single QUIC handshake for HTTP/3). ALPN picks `h2` or `http/1.1`.
5. **Send the request** with headers and cookies for that site.
6. **Server side.** The request passes through a CDN, load balancer and reverse proxy before it reaches the app, which may call databases and other services.
7. **Receive the response.** The browser reads the status and headers (redirects, cookies, caching rules) and starts parsing the HTML as it streams in.
8. **Load subresources.** The preload scanner finds CSS, JS, fonts and images and requests them, reusing the open connection where it can.
9. **Render.** Build the DOM and CSSOM, run scripts, lay out, paint and composite.

A good answer shows you know where time goes: DNS, handshakes, server time, download size and render-blocking resources.

## 82: How do TCP slow start and the congestion window affect page load?

A new TCP connection doesn't know how fast the network is, so it starts slowly. The sender can only send a limited amount of data before it has to wait for acknowledgments. This limit is the congestion window. On modern systems it starts at 10 packets, roughly 14 KB.

Each round trip with no packet loss roughly doubles the window. So a 100 KB response on a new connection needs several round trips even on a fast network, and on a high-latency mobile connection each round trip can take 100 ms or more.

What this means in practice:

- Try to fit the critical HTML and inline CSS in the first ~14 KB.
- Reuse warm connections instead of opening new ones (keep-alive, HTTP/2, fewer origins).
- Use a CDN so round trips are shorter.

## 83: How is head-of-line blocking different in HTTP/1.1, HTTP/2 and HTTP/3?

- **HTTP/1.1:** blocking at the HTTP level. Responses on one connection come in order, so a slow response holds up the ones behind it.
- **HTTP/2:** fixes that with multiplexing, but all streams still share one TCP connection. TCP delivers bytes in order, so if one packet is lost, TCP holds back everything after it, even frames that belong to other streams, until the lost packet is resent. On lossy networks HTTP/2 can be slower than HTTP/1.1 with 6 connections.
- **HTTP/3:** QUIC knows about streams. A lost packet only delays the stream it belongs to, and other streams keep going.

This is the main reason HTTP/3 exists. Fixing it inside TCP wasn't realistic, because TCP is built into operating systems and network hardware everywhere.

## 84: How does QUIC connection migration work?

A TCP connection is identified by four values: source IP, source port, destination IP and destination port. When a phone switches from Wi-Fi to mobile data, its IP changes, the connection breaks, and every request has to start over with new handshakes.

QUIC identifies connections by connection IDs instead. When the client's address changes, it keeps sending packets with a connection ID the server knows, the server checks that the new path works, and the connection continues. Requests in progress don't fail.

The endpoints swap between several connection IDs, so someone watching the network can't easily link the old and new paths to the same user. One catch for operators: load balancers must route by connection ID instead of IP address, or packets after migration end up on the wrong server.

## 85: What is 0-RTT and what are the risks?

With TLS 1.3 and QUIC, a client that connected to a server before can send its first HTTP request together with the first handshake message, using a key from the previous session. That saves a full round trip.

The risk is replay. An attacker who records that early data can send it to the server again, and the server can't tell it apart from the original. That's fine for `GET /home`, but dangerous for `POST /transfer`.

How to deal with it:

- Only allow safe, idempotent requests in early data. Many CDNs and servers do this by default.
- Proxies mark early data requests with `Early-Data: 1`, and the app can reply `425 Too Early` to make the client retry after the handshake finishes.

## 86: How does request prioritization work in HTTP/2 and HTTP/3?

The original HTTP/2 priority system used a tree of dependencies and weights. It was complex, browsers used it differently, and many servers ignored it. RFC 9113 deprecated it.

The newer scheme (RFC 9218, Extensible Priorities) works for both HTTP/2 and HTTP/3. It has two parameters: urgency `u` from 0 (highest) to 7 (default 3), and incremental `i`, which says whether the response can be used in pieces (like a progressive image):

```http
Priority: u=1, i
```

Browsers set these based on resource type. You can influence them from HTML with `fetchpriority`:

```html
<img src="/hero.avif" fetchpriority="high" alt="" />
<script src="/analytics.js" fetchpriority="low" async></script>
```

```js
fetch("/api/prefetch", { priority: "low" });
```

The server or CDN still has to respect priorities. If it sends responses as they become ready, a big low-priority image can still slow down a critical CSS file.

## 87: What is flow control in HTTP/2?

Since many streams share one connection, a fast sender could fill up a slow receiver's buffers, or one big download could take all the bandwidth. HTTP/2 flow control lets the receiver say how much data it can take.

Each stream and the whole connection have a window, by default 65,535 bytes. The sender can't send more `DATA` bytes than the window allows. The receiver sends `WINDOW_UPDATE` frames as it reads data, which opens the window again.

This mostly matters for servers and proxies. If the windows are too small, throughput on fast, high-latency links gets capped, so servers often set larger initial windows. QUIC has its own flow control built in, so HTTP/3 doesn't need its own.

## 88: What is QPACK and why couldn't HTTP/3 just use HPACK?

HPACK assumes all frames arrive in order, which TCP guarantees. The dynamic table changes as headers are sent, and each header block can refer to entries added just before it.

In QUIC, streams arrive independently. If a request refers to a table entry from a packet that was lost, the decoder can't read it. With HPACK, that would bring back head-of-line blocking between streams.

QPACK (RFC 9204) sends table updates on separate one-way streams, and each header block says which table state it needs. The encoder can decide to use only entries the decoder has confirmed, which avoids blocking completely, or to accept some blocking for better compression. The server limits how many streams can be blocked at once.

## 89: What is HTTP request smuggling?

It happens when a front-end proxy and a back-end server disagree about where one request ends and the next one starts on a shared connection. The classic case is a request with both `Content-Length` and `Transfer-Encoding: chunked`, where one server uses one header and the other server uses the other.

```http
POST / HTTP/1.1
Host: example.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

The leftover bytes (`SMUGGLED...`) get treated as the start of the next request, which could belong to another user. Attackers use this to get around security checks, poison caches or steal other users' requests.

Defenses:

- Use HTTP/2 end to end, which has clear frame lengths.
- Reject ambiguous requests (both headers, duplicate `Content-Length`, odd whitespace).
- Keep proxies and servers up to date.
- Normalize requests at the edge.

## 90: What was the HTTP/2 Rapid Reset attack?

In October 2023 (CVE-2023-44487), attackers found they could open an HTTP/2 stream and cancel it right away with `RST_STREAM`, over and over, on many connections. A canceled stream no longer counts against `SETTINGS_MAX_CONCURRENT_STREAMS`, so the limit didn't help, but the server had already started work for each request.

This led to the largest DDoS attacks seen at that time, hundreds of millions of requests per second against Google, Cloudflare and AWS.

Servers fixed it by counting resets per connection and closing connections (with `GOAWAY`) that reset too many streams too fast. In 2024 a similar class of problems showed up with `CONTINUATION` frames, where endless header frames used up server memory. The lesson: protocol-level limits on stream counts aren't enough. Servers also need limits on how much work each connection can cause.

## 91: What is HTTP header injection or response splitting?

It happens when user input ends up in a response header without filtering out line breaks (`\r\n`). An attacker can then add their own headers, or even end the headers and write their own body:

```js
// Vulnerable if lang comes from the query string unchecked
res.setHeader("Set-Cookie", `lang=${req.query.lang}`);
// lang = "en\r\nSet-Cookie: admin=true"
```

This can be used to set cookies, change redirects, poison caches or inject scripts.

Modern frameworks and Node.js reject header values that contain `\r` or `\n` and throw an error, which blocks most of this. You should still validate input that goes into headers and redirect URLs, because the same bug can show up in custom servers, proxies and older stacks.

## 92: What is a Host header attack?

Apps sometimes use the `Host` header to build absolute URLs, like links in password reset emails. If the server accepts any `Host`, an attacker can send a reset request with `Host: evil.com`. The victim gets a real email from your app, but the link points to `evil.com/reset?token=...`. If they click, the attacker gets the token.

The same bug can cause cache poisoning, if a cache stores a page with links built from a fake host, and can let attackers reach internal virtual hosts.

Fixes:

- Build absolute URLs from a configured base URL, not from the request.
- Have the reverse proxy only accept known host names and reject the rest.
- Be careful with `X-Forwarded-Host`. Only trust it when your own proxy sets it.

## 93: What are web cache poisoning and web cache deception?

**Cache poisoning:** the attacker gets a harmful response stored in a shared cache, which then serves it to everyone. It usually uses an "unkeyed" input, meaning a header that changes the response but isn't part of the cache key. For example, if the app uses `X-Forwarded-Host` to build a script URL and the CDN ignores that header when caching, one poisoned request can make every visitor load the attacker's script.

**Cache deception:** the attacker tricks the cache into storing a private page. They send the victim to `https://site.com/account/profile.css`. The app ignores the `.css` part and returns the victim's account page, and the CDN caches it because it looks like a static file. The attacker then loads the same URL and gets the cached private data.

Defenses:

- Include every input that changes the response in the cache key, or don't use it.
- Send `Cache-Control: private` or `no-store` on personal responses.
- Configure the CDN to cache based on the origin's `Cache-Control` headers, not just on file extensions.
- Return `404` for unexpected path suffixes.

## 94: How do you protect against CSRF?

CSRF (Cross-Site Request Forgery) works because browsers attach cookies automatically. A page on `evil.com` can submit a form to `bank.com/transfer`, and the user's session cookie goes along with it.

Layers of defense:

- **SameSite cookies.** `Lax` (or `Strict`) stops the cookie from being sent on cross-site `POST` requests. Set it yourself, since not all browsers apply `Lax` by default.
- **CSRF tokens.** A random token tied to the session goes in a hidden form field or custom header, and the server checks it. Another site can't read it.
- **Check `Origin` or `Sec-Fetch-Site`.** Browsers send these on requests, and the server can reject state-changing requests that come from other sites.
- **Never change state on `GET`.**

Remember that SameSite works by site, not origin. A vulnerable subdomain on the same site can still send same-site requests, so SameSite alone isn't always enough.

## 95: Which security headers should a web app send?

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-r4nd0m'; object-src 'none'; frame-ancestors 'none'; base-uri 'self'
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Opener-Policy: same-origin
```

- **HSTS** forces HTTPS.
- **CSP** limits where scripts, styles and other resources can come from, which is the strongest defense against XSS. `frame-ancestors` replaces the older `X-Frame-Options` for clickjacking protection.
- **nosniff** stops browsers from guessing content types, so an uploaded text file can't run as a script.
- **Referrer-Policy** controls how much of the URL leaks to other sites.
- **Permissions-Policy** turns off browser features you don't use.
- **COOP** isolates your window from cross-origin popups.

`X-XSS-Protection` is obsolete. Browsers removed the XSS filter it controlled, so don't bother with it.

## 96: How does a browser validate a certificate, and what is mTLS?

The browser checks that:

- The certificate chain leads up to a root CA in its trust store, with each certificate signed by the next one up.
- The domain matches one of the names in the certificate's Subject Alternative Name list (the old Common Name field is ignored).
- The certificate is within its valid dates.
- It was logged in public Certificate Transparency logs (Chrome and Safari require this).
- It hasn't been revoked. Browsers mostly use their own revocation lists for this today. OCSP is fading out: Let's Encrypt shut down its OCSP service in 2025.

Certificate lifetimes are also shrinking. The CA/Browser Forum agreed to cut the maximum step by step from 398 days to 47 days by 2029, so automatic renewal is basically required.

With mutual TLS (mTLS), the server also asks the client for a certificate and checks it. It's common for service-to-service traffic, often handled by a service mesh, and for high-security APIs. It's rarely used for browsers because managing client certificates there is painful.

## 97: What are SNI and Encrypted Client Hello?

SNI (Server Name Indication) is a field in the TLS `ClientHello` where the client says which host name it wants. One IP address can host many HTTPS sites, so the server needs to know which certificate to send before encryption starts.

The problem is that SNI is sent as plain text, so anyone on the network can see which site you're visiting even with HTTPS. Encrypted DNS (DoH, DoT) hides the DNS lookup, but SNI still leaked the name.

Encrypted Client Hello (ECH) fixes this. The client gets the server's public key from the DNS `HTTPS` record and encrypts the real `ClientHello`, including the SNI. The visible outer `ClientHello` shows only a shared public name, like the CDN's. Chrome and Firefox support it, and Cloudflare turns it on for many sites.

## 98: Which HTTP/1.1-era optimizations hurt you under HTTP/2 and HTTP/3?

- **Domain sharding.** Spreading files over `static1.example.com`, `static2.example.com` to get more parallel connections. With HTTP/2 this means extra DNS lookups and handshakes, and it breaks prioritization because the files no longer share one connection. Coalescing can undo it partly, but only if the domains share an IP and certificate.
- **One giant bundle.** Fewer requests mattered a lot in HTTP/1.1. With multiplexing, a few medium chunks cache better: changing one module only invalidates its chunk.
- **Image sprites and inlining everything.** Inlined assets can't be cached on their own.

Some old advice still holds: requests aren't free (each has headers, server work and priority overhead), so thousands of tiny unbundled modules are still slow. The goal is sensible chunking, not maximum splitting.

## 99: What is HTTP/2 connection coalescing?

A browser can reuse an existing HTTP/2 (or HTTP/3) connection for a different host name if both:

- Resolve to an IP address the connection is already using
- Are covered by the connection's certificate (for example a wildcard `*.example.com` or a SAN list with both names)

So requests to `www.example.com` and `static.example.com` can share one connection, saving a DNS lookup and handshakes.

It can surprise you. If the server behind that connection isn't set up for the other host name, requests can go to the wrong place. The server should then respond with `421 Misdirected Request`, and the browser retries on a new connection. This shows up with CDNs, wildcard certificates and setups where different hosts use different TLS settings.

## 100: How would you design HTTP caching for a single-page app?

Split files by how they change:

```http
# index.html (entry point, not hashed)
Cache-Control: no-cache

# /assets/app.3f9a1c.js, /assets/main.a8d2e0.css (hashed)
Cache-Control: public, max-age=31536000, immutable

# /api/products (public, changes often)
Cache-Control: public, max-age=0, s-maxage=60, stale-while-revalidate=300

# /api/me (personal)
Cache-Control: private, no-store
```

- The HTML always revalidates, so a new deploy shows up right away. Its ETag keeps that check cheap.
- Hashed assets never revalidate.
- Public API data is cached on the CDN for a short time, and stale copies are served while refreshing.
- Personal data never goes into shared caches.

Keep old hashed assets on the server for a while after a deploy. Users with the old HTML still open will request the old chunk names, and if those are gone they get errors when the app lazy-loads a route.

## 101: How do CDN cache keys and purging work?

The cache key decides which requests share a cached response. By default it's usually the scheme, host, path and query string, plus whatever `Vary` and your CDN config add.

Tuning tips:

- Remove query parameters that don't change the response (`utm_source`, `fbclid`), so marketing links don't split the cache.
- Sort query parameters so `?a=1&b=2` and `?b=2&a=1` share an entry.
- Add a header or cookie to the key only when the response really depends on it.

For purging, URL-by-URL purges don't scale when one product change affects hundreds of pages. Many CDNs support tags (often called surrogate keys or cache tags): the origin tags responses, for example with `Surrogate-Key: product-42 category-7` (Fastly) or `Cache-Tag` (Cloudflare), and you purge everything with a tag in one call. The other option is to cache briefly and rely on `stale-while-revalidate`.

## 102: What is stale-if-error and how does it help resilience?

`stale-if-error` lets a cache serve a stale response when the origin fails (a `5xx` error or no connection) instead of passing the error to users:

```http
Cache-Control: public, max-age=60, stale-while-revalidate=60, stale-if-error=86400
```

Here, content is fresh for a minute, refreshed in the background for another minute, and if the origin is down, the cache can keep serving the last good copy for up to a day.

For read-heavy pages like product pages, blog posts and public API data, this can turn an origin outage into a non-event for users. Support varies between CDNs, and some have their own setting for it (like "serve stale" options), so check how yours works.

## 103: How do browser privacy changes affect cookies and cross-site requests?

- **Third-party cookies.** Safari and Firefox block them by default. Chrome dropped its plan to remove them and keeps them on unless the user turns them off. So a cross-site cookie flow may work in Chrome and fail in Safari.
- **Partitioned cookies (CHIPS).** A cookie set with `Partitioned` (plus `Secure` and `SameSite=None`) is stored separately for each top-level site. An embedded chat widget keeps its state on `a.com` and `b.com`, but the two can't be linked.
- **Storage partitioning.** Browsers also partition `localStorage`, IndexedDB, the HTTP cache and even connections by top-level site. A shared CDN file is no longer reused from cache across different sites.

The safest setup for your own app is to keep the front end and API on the same site (for example `app.example.com` and `api.example.com`) so cookies are first-party.

## 104: What are COOP, COEP and CORP, and what is cross-origin isolation?

- **CORP** (`Cross-Origin-Resource-Policy: same-origin | same-site | cross-origin`) is set on a resource and says which origins may embed it.
- **COEP** (`Cross-Origin-Embedder-Policy: require-corp` or `credentialless`) is set on a document. It only allows cross-origin resources that opt in through CORP or CORS.
- **COOP** (`Cross-Origin-Opener-Policy: same-origin`) puts the document in its own browsing context group, cutting the link to cross-origin popups and openers.

When a page sends both `COOP: same-origin` and `COEP: require-corp` (or `credentialless`), it becomes cross-origin isolated. That turns on powerful features like `SharedArrayBuffer` and more precise timers, which were locked after the Spectre attacks. Check with `self.crossOriginIsolated`. The cost: every third-party script, image or iframe must support it, which often breaks ads, analytics and embeds.

## 105: How would you handle very large file uploads?

One big `POST` breaks easily. A network drop at 95% means starting over, and proxies often have body size limits and timeouts. Better options:

- **Direct upload to storage.** The API returns a pre-signed URL and the client uploads straight to S3, GCS or Azure Blob. Your servers don't handle the bytes at all.
- **Multipart or chunked uploads.** Split the file into parts (S3 multipart upload uses parts of 5 MB to 5 GB), upload them in parallel, retry only failed parts, then complete.
- **Resumable uploads.** The tus protocol, or similar, lets the client ask how much the server already has and continue from there. The IETF is also standardizing resumable uploads for HTTP.

For uploads that go through your own server, the client can send `Expect: 100-continue`, so the server can reject a request (too big, not allowed) before the client sends gigabytes of data. Also check size and type on the server, not only on the client.

## 106: How do you stream HTTP responses and handle backpressure?

On the server, write the response in pieces instead of building it all in memory first. In Node.js, use streams with `pipeline`, which handles backpressure: if the client reads slowly, the source pauses instead of filling memory.

```js
import { createReadStream } from "node:fs";
import { pipeline } from "node:stream/promises";
import http from "node:http";

http
  .createServer(async (req, res) => {
    res.writeHead(200, { "Content-Type": "text/csv" });
    try {
      await pipeline(createReadStream("./export.csv"), res);
    } catch (err) {
      res.destroy(err);
    }
  })
  .listen(3000);
```

On the client, `response.body` is a `ReadableStream`, so you can process data as it arrives, which is useful for AI token streams or large NDJSON exports:

```js
const res = await fetch("/api/stream");
const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();

while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  console.log(value);
}
```

Once you've sent the status and headers, you can't change them. A failure halfway through can only be signaled by cutting the connection or by an error format inside the stream.

## 107: Why can mismatched keep-alive timeouts cause random 502 errors?

A load balancer keeps idle connections to your app open to reuse them. If the app closes an idle connection at the exact moment the load balancer sends a new request on it, the request fails and the load balancer returns `502`.

This happens when the app's keep-alive timeout is shorter than the load balancer's idle timeout. Node.js closes idle connections after 5 seconds by default, while AWS ALB keeps them for 60 seconds. So the app always closes first, and under load some requests hit that race.

The fix is to make the app's timeout longer than the load balancer's:

```js
const server = app.listen(3000);
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000;
```

`headersTimeout` should be a bit larger than `keepAliveTimeout`. The same rule applies to any proxy chain: each hop should keep idle connections open longer than the hop in front of it.

## 108: How do you avoid retry storms?

When a service slows down, clients time out and retry. Each retry adds load, which makes the service slower, which causes more retries. With several layers that each retry 3 times, one user request can turn into 27 calls to the bottom service.

Ways to avoid it:

- **Exponential backoff with jitter.** Random delays spread retries out instead of having them all arrive together.
- **Retry at one layer only,** usually the one closest to the user or the client library, not at every hop.
- **Retry budgets.** Limit retries to a small percentage of total traffic.
- **Circuit breakers.** After many failures, stop calling the service for a while and fail fast, then let a few test requests through.
- **Respect `Retry-After`** and `503` or `429` from the server.
- **Deadlines.** Pass the remaining time budget down the chain, so services don't keep working on requests the client already gave up on.

## 109: How do idempotency keys work and how would you implement them?

The client creates a unique key (like a UUID) for an action and sends it with the request. If the request times out and the client retries with the same key, the server returns the original result instead of doing the action again.

```http
POST /payments HTTP/1.1
Idempotency-Key: 8e03978e-40d5-43e8-bc93-6894a57f9324
Content-Type: application/json

{"amount": 4999, "currency": "EUR"}
```

On the server:

1. Store the key (scoped to the user) with a "processing" status, using a unique constraint so two parallel requests can't both start.
2. Do the work, then save the response status and body with the key.
3. On a repeat with the same key, return the saved response. If it's still processing, return `409` so the client tries again later.
4. If the same key comes with a different body, reject it with `422`.
5. Expire keys after some time, like 24 hours.

This is how payment APIs like Stripe work, and there's an IETF draft standardizing the `Idempotency-Key` header.

## 110: How do you measure network performance from real users?

DevTools and lab tests only show your own machine. For real users, use the browser's Resource Timing and Navigation Timing APIs:

```js
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(entry.name, {
      dns: entry.domainLookupEnd - entry.domainLookupStart,
      connect: entry.connectEnd - entry.connectStart,
      ttfb: entry.responseStart - entry.requestStart,
      protocol: entry.nextHopProtocol,
      transferSize: entry.transferSize,
    });
  }
});
observer.observe({ type: "resource", buffered: true });
```

The server can add its own timings with `Server-Timing`, and they show up in DevTools and in `entry.serverTiming`:

```http
Server-Timing: db;dur=53, cache;desc="miss", app;dur=120
```

For cross-origin resources, most detailed fields are zero unless the server sends `Timing-Allow-Origin`. `transferSize` of 0 usually means the response came from cache. Send this data to your analytics in batches, for example with `navigator.sendBeacon`.

## 111: How would you reduce Time to First Byte?

TTFB covers everything from sending the request to getting the first byte back: redirects, DNS, connection setup, and the server's work. Look at each part:

- **Network:** serve from a CDN close to users, use HTTP/3 and TLS 1.3, avoid redirect chains (like `http` to `https` to `www`).
- **Caching:** cache full HTML at the edge where possible, even briefly or with `stale-while-revalidate`.
- **Server work:** find slow queries and slow upstream calls with tracing and `Server-Timing`. Run independent calls in parallel. Add caching for expensive data.
- **Streaming:** send the `<head>` early (HTML streaming, React SSR streaming) so the browser starts loading CSS and JS while the server builds the rest.
- **Early Hints:** send `103` with preload and preconnect links while the server is still working.
- **Cold starts:** serverless functions and scaled-to-zero containers can add seconds. Keep instances warm for critical paths.

## 112: How does gRPC use HTTP/2, and why can't browsers use it directly?

gRPC sends Protobuf messages over HTTP/2. Each call is a `POST` to `/package.Service/Method` with `content-type: application/grpc`. Streaming calls use the HTTP/2 stream for many messages in both directions. The final status (`grpc-status`, `grpc-message`) is sent in HTTP trailers, which are headers that come after the body.

Browsers don't give JavaScript access to HTTP/2 frames or trailers, and `fetch` can't do full two-way streaming. So browsers use gRPC-Web, which puts trailers inside the body, or the Connect protocol, which also supports plain JSON over HTTP. These usually need a proxy like Envoy or server support.

Compared to REST with JSON, gRPC gives typed contracts, smaller messages and streaming, which makes it popular between backend services. REST is easier to debug, cache and call from anywhere.

## 113: What are the practical downsides of HTTP/3?

- **UDP gets blocked or throttled** on some company networks and firewalls. Browsers fall back to TCP, but the first attempt can cost time.
- **CPU cost.** QUIC runs in user space and encrypts every packet, so it often uses more CPU per byte than TCP, which the kernel and network cards have been optimized for over decades.
- **Harder to debug.** Almost everything, including transport headers, is encrypted. Tools like Wireshark need key logs (`SSLKEYLOGFILE`), and some network monitoring tools can't see inside.
- **Load balancing.** You need UDP support and routing by connection ID.
- **Less benefit on good networks.** On fast, stable connections HTTP/2 and HTTP/3 perform about the same.

Most teams get HTTP/3 by turning it on at the CDN, which handles these issues, while the origin stays on HTTP/1.1 or HTTP/2.

## 114: Why can compressing secrets in HTTPS responses be dangerous?

Compression makes the output smaller when content repeats. If a response contains both a secret (like a CSRF token) and text the attacker controls (like a search term echoed back), the attacker can guess the secret one character at a time. A correct guess repeats part of the secret, so the response gets slightly smaller. By watching encrypted response sizes, they learn the secret. This is the BREACH attack. CRIME was the same idea against TLS-level compression, which is why TLS compression was removed.

Defenses:

- Don't put secrets and user-controlled input in the same compressed response.
- Change CSRF tokens on each request, or mask them with a random value each time.
- Rely on `SameSite` cookies so the attacker can't make authenticated requests in the first place.
- Add random padding as an extra layer.

Turning off compression completely works too, but costs a lot of bandwidth, so it's rarely done.

## 115: Why might SSE or streaming responses not stream through a proxy?

Many reverse proxies buffer the upstream response and only send it to the client when it's done, or when the buffer fills. For normal responses that's fine. For SSE or token streaming, the user sees nothing and then everything at once.

Common causes and fixes:

- **Nginx buffering.** Turn off `proxy_buffering` for that location, or send `X-Accel-Buffering: no` from the app.
- **Compression middleware** waits for enough bytes to compress. Skip compression for `text/event-stream` or flush after each event.
- **CDNs** may buffer or cache. Use `Cache-Control: no-cache` and check the CDN's streaming support.
- **Idle timeouts.** Proxies close connections with no traffic, often after 60 seconds. Send a comment line like `: ping` every 15 to 30 seconds.

```nginx
location /events {
  proxy_pass http://app;
  proxy_http_version 1.1;
  proxy_buffering off;
  proxy_read_timeout 1h;
}
```

## 116: An API call works in Postman but fails in the browser with a CORS error. How do you debug it?

Postman doesn't enforce CORS, so the difference is almost always CORS or browser-only behavior. Steps:

1. **Read the console error.** It says which header is missing or wrong.
2. **Check the Network tab for an `OPTIONS` preflight.** If it returns `404`, `401` or `405`, the server doesn't handle `OPTIONS` or runs auth before the CORS middleware. Preflights don't carry credentials, so auth must not block them.
3. **Compare headers.** `Access-Control-Allow-Origin` must exactly match the page's origin, including scheme and port. `Access-Control-Allow-Headers` must list every custom header you send, like `authorization` or `content-type`.
4. **Credentials.** With `credentials: "include"`, you need `Access-Control-Allow-Credentials: true` and an exact origin, not `*`.
5. **Error responses.** If the server or proxy returns a `500` without CORS headers, the browser shows a CORS error that hides the real problem. Add CORS headers to error responses too.
6. **Duplicate headers.** If both the proxy and the app add `Access-Control-Allow-Origin`, the browser rejects the response.

In development, a dev server proxy (like Vite's `server.proxy`) avoids CORS by making the API look same-origin.

## 117: Users report random 502 and 504 errors. How do you investigate?

1. **Find who returns them.** `502` and `504` come from a proxy, CDN or load balancer, not your app. Check headers like `Server` or `Via` and the error page to see which layer.
2. **Look at timing and patterns.** Do they happen after deploys, under load, on long requests, or at random?
3. **Random `502`s at low load** often mean keep-alive timeout mismatches: the app closes idle connections before the load balancer does.
4. **`502` during deploys** means the instance is removed after it stopped, or added before it's ready. Fix health checks and graceful shutdown.
5. **`504`s** mean the app is too slow for the proxy's timeout. Find the slow endpoints with tracing. Raise timeouts only if the work really needs it. Long jobs should become async with a `202 Accepted` and polling.
6. **App crashes or memory limits** (OOM kills) show up as `502`. Check container restarts.
7. **Connect the logs.** Pass a request ID (`X-Request-Id` or `traceparent`) through every layer, so you can follow one failed request from the CDN to the app.

## 118: Your API is slow for users far from your data center. What would you do?

Start by measuring which part is slow: network or server. Then:

- **Put a CDN or edge proxy in front.** Even for uncacheable API calls, the TCP and TLS handshakes end near the user, and the edge keeps warm connections back to the origin over fast backbone networks.
- **Cache what you can at the edge.** Public data with short `s-maxage` and `stale-while-revalidate`.
- **Turn on HTTP/3 and TLS 1.3** to cut handshake round trips.
- **Cut round trips in the API.** Combine chatty calls into one endpoint, avoid request waterfalls, and avoid redirects.
- **Move compute closer.** Edge functions for simple logic, or deploy the app in more regions, with read replicas for data. Writes usually still go to one primary region.
- **Shrink payloads.** Compression, only the fields the client needs, pagination.

A rough rule: each round trip from Europe to Australia costs around 250-300 ms, so cutting round trips usually matters more than making the server faster.

## 119: How would you design the HTTP contract for a new public API?

- **Resources and methods.** Plural nouns (`/orders/{id}`), standard methods, `POST` for actions that don't fit (`/orders/{id}/cancel`).
- **Status codes.** `201` with `Location` for creates, `204` for empty success, `4xx` for client errors and `5xx` only for real server failures.
- **Errors.** One format everywhere, ideally Problem Details (`application/problem+json`), with a request ID.
- **Safety.** HTTPS only, HSTS, tokens in the `Authorization` header, never secrets in URLs.
- **Idempotency.** Support `Idempotency-Key` on `POST` endpoints that create things or move money.
- **Concurrency.** ETags with `If-Match` for updates.
- **Caching.** `Cache-Control` and ETags on read endpoints.
- **Limits.** Pagination with a max page size, rate limits with `429` and `Retry-After`.
- **Versioning and deprecation.** A clear version scheme, `Deprecation` and `Sunset` headers, and a changelog.
- **Docs.** An OpenAPI spec as the source of truth, so clients and tests can be generated from it.

## 120: How do you shut down an HTTP server without dropping requests?

When a deploy or autoscaler stops an instance, requests in progress shouldn't fail. A graceful shutdown looks like this:

1. **Stop getting new traffic.** Fail the readiness check, or wait for the load balancer or Kubernetes to remove the instance. In Kubernetes there's a short delay before endpoints update, so a small sleep in a `preStop` hook helps.
2. **Stop accepting new connections** but let current requests finish. For keep-alive connections, send `Connection: close` (HTTP/1.1) or `GOAWAY` (HTTP/2), so clients open new connections elsewhere.
3. **Wait with a deadline,** then force close what's left.
4. **Close resources** like database pools and message consumers.

```js
const server = app.listen(3000);

process.on("SIGTERM", () => {
  server.close(() => {
    db.end().then(() => process.exit(0));
  });
  server.closeIdleConnections();
  setTimeout(() => process.exit(1), 25_000).unref();
});
```

`server.close()` stops new connections and calls the callback once the existing ones close. `closeIdleConnections()` closes keep-alive connections that aren't serving a request. Keep the total time below the platform's grace period (30 seconds by default in Kubernetes).
