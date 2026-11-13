# NestJS Security Interview Questions and Answers

_Last updated: November 13, 2026_

450 interview questions with answers about securing NestJS applications, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for **NestJS 11 and 12** with the Express adapter, unless an answer says otherwise. Most of them also apply to NestJS 10. Code examples use TypeScript.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the difference between authentication and authorization?](#1-what-is-the-difference-between-authentication-and-authorization)
- [2: Where does security logic usually live in a NestJS app?](#2-where-does-security-logic-usually-live-in-a-nestjs-app)
- [3: What is a guard in NestJS?](#3-what-is-a-guard-in-nestjs)
- [4: How do you apply a guard to a route?](#4-how-do-you-apply-a-guard-to-a-route)
- [5: How do you make a guard global?](#5-how-do-you-make-a-guard-global)
- [6: In what order does Nest run middleware, guards, interceptors and pipes?](#6-in-what-order-does-nest-run-middleware-guards-interceptors-and-pipes)
- [7: What is Passport and why is it used with Nest?](#7-what-is-passport-and-why-is-it-used-with-nest)
- [8: Do you need Passport to do authentication in Nest?](#8-do-you-need-passport-to-do-authentication-in-nest)
- [9: What is a JWT?](#9-what-is-a-jwt)
- [10: What should you never put in a JWT payload?](#10-what-should-you-never-put-in-a-jwt-payload)
- [11: Which package does Nest provide for working with JWTs?](#11-which-package-does-nest-provide-for-working-with-jwts)
- [12: How do you sign a JWT when a user logs in?](#12-how-do-you-sign-a-jwt-when-a-user-logs-in)
- [13: What is the difference between jwtService.decode and jwtService.verify?](#13-what-is-the-difference-between-jwtservicedecode-and-jwtserviceverify)
- [14: Where should the client send the access token?](#14-where-should-the-client-send-the-access-token)
- [15: What does the exp claim do?](#15-what-does-the-exp-claim-do)
- [16: Why should access tokens be short-lived?](#16-why-should-access-tokens-be-short-lived)
- [17: What is a refresh token?](#17-what-is-a-refresh-token)
- [18: What is the local strategy in Passport?](#18-what-is-the-local-strategy-in-passport)
- [19: What does the validate method in a Passport strategy return?](#19-what-does-the-validate-method-in-a-passport-strategy-return)
- [20: What is the JWT strategy in Passport?](#20-what-is-the-jwt-strategy-in-passport)
- [21: How do you protect a route with the Passport JWT strategy?](#21-how-do-you-protect-a-route-with-the-passport-jwt-strategy)
- [22: Why should ignoreExpiration stay false?](#22-why-should-ignoreexpiration-stay-false)
- [23: What status code should you return for a missing or bad token?](#23-what-status-code-should-you-return-for-a-missing-or-bad-token)
- [24: How do you get the current user inside a controller?](#24-how-do-you-get-the-current-user-inside-a-controller)
- [25: What is a public route decorator and why do you need it?](#25-what-is-a-public-route-decorator-and-why-do-you-need-it)
- [26: What is the Reflector used for in guards?](#26-what-is-the-reflector-used-for-in-guards)
- [27: What is RBAC?](#27-what-is-rbac)
- [28: How do you build a Roles decorator in modern Nest?](#28-how-do-you-build-a-roles-decorator-in-modern-nest)
- [29: How does a roles guard work?](#29-how-does-a-roles-guard-work)
- [30: What is ABAC?](#30-what-is-abac)
- [31: What is CASL?](#31-what-is-casl)
- [32: What is the ValidationPipe?](#32-what-is-the-validationpipe)
- [33: Why does input validation matter for security?](#33-why-does-input-validation-matter-for-security)
- [34: What is a DTO?](#34-what-is-a-dto)
- [35: What does the whitelist option of ValidationPipe do?](#35-what-does-the-whitelist-option-of-validationpipe-do)
- [36: What does forbidNonWhitelisted do?](#36-what-does-forbidnonwhitelisted-do)
- [37: What is mass assignment?](#37-what-is-mass-assignment)
- [38: What does the transform option of ValidationPipe do?](#38-what-does-the-transform-option-of-validationpipe-do)
- [39: Which built-in pipes help validate route params?](#39-which-built-in-pipes-help-validate-route-params)
- [40: How do you validate nested objects?](#40-how-do-you-validate-nested-objects)
- [41: What is serialization in NestJS?](#41-what-is-serialization-in-nestjs)
- [42: How do you hide a field like password from responses?](#42-how-do-you-hide-a-field-like-password-from-responses)
- [43: Why doesn't @Exclude work when you return a plain object?](#43-why-doesnt-exclude-work-when-you-return-a-plain-object)
- [44: What is Helmet?](#44-what-is-helmet)
- [45: Why should you call app.use(helmet()) before other routes are set up?](#45-why-should-you-call-appusehelmet-before-other-routes-are-set-up)
- [46: What is CORS?](#46-what-is-cors)
- [47: How do you enable CORS in Nest?](#47-how-do-you-enable-cors-in-nest)
- [48: Is CORS a security feature that protects your API?](#48-is-cors-a-security-feature-that-protects-your-api)
- [49: What is CSRF?](#49-what-is-csrf)
- [50: Do you need CSRF protection if you use Bearer tokens in headers?](#50-do-you-need-csrf-protection-if-you-use-bearer-tokens-in-headers)
- [51: Which package should you use for CSRF protection in a Nest app on Express?](#51-which-package-should-you-use-for-csrf-protection-in-a-nest-app-on-express)
- [52: What is rate limiting?](#52-what-is-rate-limiting)
- [53: How do you add rate limiting to a Nest app?](#53-how-do-you-add-rate-limiting-to-a-nest-app)
- [54: How do you change the rate limit for one route?](#54-how-do-you-change-the-rate-limit-for-one-route)
- [55: What status code does the throttler return when the limit is reached?](#55-what-status-code-does-the-throttler-return-when-the-limit-is-reached)
- [56: Why must you never store passwords in plain text?](#56-why-must-you-never-store-passwords-in-plain-text)
- [57: Why not use SHA-256 to hash passwords?](#57-why-not-use-sha-256-to-hash-passwords)
- [58: How do you hash and check a password with bcrypt?](#58-how-do-you-hash-and-check-a-password-with-bcrypt)
- [59: How do you hash and check a password with argon2?](#59-how-do-you-hash-and-check-a-password-with-argon2)
- [60: What is a salt?](#60-what-is-a-salt)
- [61: What is a pepper?](#61-what-is-a-pepper)
- [62: What is an API key?](#62-what-is-an-api-key)
- [63: How would you check an API key in Nest?](#63-how-would-you-check-an-api-key-in-nest)
- [64: What is OAuth 2.0?](#64-what-is-oauth-20)
- [65: What is OpenID Connect?](#65-what-is-openid-connect)
- [66: What is SSO?](#66-what-is-sso)
- [67: Which Passport strategy would you use for Google login?](#67-which-passport-strategy-would-you-use-for-google-login)
- [68: What is the ConfigModule?](#68-what-is-the-configmodule)
- [69: Why shouldn't you commit the .env file?](#69-why-shouldnt-you-commit-the-env-file)
- [70: What does ConfigService.getOrThrow do?](#70-what-does-configservicegetorthrow-do)
- [71: Why validate environment variables at startup?](#71-why-validate-environment-variables-at-startup)
- [72: What is HTTPS and why is it needed?](#72-what-is-https-and-why-is-it-needed)
- [73: Where is TLS usually terminated for a Nest app?](#73-where-is-tls-usually-terminated-for-a-nest-app)
- [74: What is HSTS?](#74-what-is-hsts)
- [75: What is encryption at rest?](#75-what-is-encryption-at-rest)
- [76: What is SQL injection?](#76-what-is-sql-injection)
- [77: How does TypeORM protect you from SQL injection?](#77-how-does-typeorm-protect-you-from-sql-injection)
- [78: Is Prisma safe from SQL injection?](#78-is-prisma-safe-from-sql-injection)
- [79: What is NoSQL injection?](#79-what-is-nosql-injection)
- [80: How does class-validator help against NoSQL injection?](#80-how-does-class-validator-help-against-nosql-injection)
- [81: What is XSS?](#81-what-is-xss)
- [82: Is a JSON API safe from XSS?](#82-is-a-json-api-safe-from-xss)
- [83: What is output encoding?](#83-what-is-output-encoding)
- [84: How do you accept a file upload in Nest?](#84-how-do-you-accept-a-file-upload-in-nest)
- [85: Why set a file size limit on uploads?](#85-why-set-a-file-size-limit-on-uploads)
- [86: How do you validate an uploaded file's size and type?](#86-how-do-you-validate-an-uploaded-files-size-and-type)
- [87: Can you trust the file name the client sends?](#87-can-you-trust-the-file-name-the-client-sends)
- [88: What is an exception filter?](#88-what-is-an-exception-filter)
- [89: What does Nest return for an unknown error by default?](#89-what-does-nest-return-for-an-unknown-error-by-default)
- [90: Why is error leakage a security problem?](#90-why-is-error-leakage-a-security-problem)
- [91: What should a security log contain?](#91-what-should-a-security-log-contain)
- [92: Which logger is common in production Nest apps?](#92-which-logger-is-common-in-production-nest-apps)
- [93: What is audit logging?](#93-what-is-audit-logging)
- [94: How do you protect a WebSocket gateway in Nest?](#94-how-do-you-protect-a-websocket-gateway-in-nest)
- [95: What is WsException?](#95-what-is-wsexception)
- [96: How do you get the request inside a GraphQL guard?](#96-how-do-you-get-the-request-inside-a-graphql-guard)
- [97: What is a query depth limit in GraphQL?](#97-what-is-a-query-depth-limit-in-graphql)
- [98: Should GraphQL introspection be on in production?](#98-should-graphql-introspection-be-on-in-production)
- [99: What is mTLS?](#99-what-is-mtls)
- [100: How can microservices in Nest authenticate each other?](#100-how-can-microservices-in-nest-authenticate-each-other)
- [101: What is multi-tenancy?](#101-what-is-multi-tenancy)
- [102: What are the common ways to store data for many tenants?](#102-what-are-the-common-ways-to-store-data-for-many-tenants)
- [103: What does the httpOnly cookie flag do?](#103-what-does-the-httponly-cookie-flag-do)
- [104: What does the Secure cookie flag do?](#104-what-does-the-secure-cookie-flag-do)
- [105: What does the SameSite cookie attribute do?](#105-what-does-the-samesite-cookie-attribute-do)
- [106: How do you set a secure cookie in a Nest controller?](#106-how-do-you-set-a-secure-cookie-in-a-nest-controller)
- [107: How do you read cookies in Nest with Express?](#107-how-do-you-read-cookies-in-nest-with-express)
- [108: What is a request size limit?](#108-what-is-a-request-size-limit)
- [109: What is a DoS attack?](#109-what-is-a-dos-attack)
- [110: What does npm audit do?](#110-what-does-npm-audit-do)
- [111: What is Snyk?](#111-what-is-snyk)
- [112: What is a supply-chain attack?](#112-what-is-a-supply-chain-attack)
- [113: Why should you commit the lockfile?](#113-why-should-you-commit-the-lockfile)
- [114: What is the OWASP Top 10?](#114-what-is-the-owasp-top-10)
- [115: Which item has been number one on the OWASP Top 10 recently?](#115-which-item-has-been-number-one-on-the-owasp-top-10-recently)
- [116: What is IDOR?](#116-what-is-idor)
- [117: How do you test that a route needs authentication?](#117-how-do-you-test-that-a-route-needs-authentication)
- [118: What is a session in web authentication?](#118-what-is-a-session-in-web-authentication)
- [119: How do sessions compare to JWTs?](#119-how-do-sessions-compare-to-jwts)
- [120: Which package is used for sessions with Nest on Express?](#120-which-package-is-used-for-sessions-with-nest-on-express)
- [121: Why set saveUninitialized to false?](#121-why-set-saveuninitialized-to-false)
- [122: What is brute force and how do you slow it down on login?](#122-what-is-brute-force-and-how-do-you-slow-it-down-on-login)
- [123: What is credential stuffing?](#123-what-is-credential-stuffing)
- [124: What is MFA?](#124-what-is-mfa)
- [125: What is a passkey?](#125-what-is-a-passkey)
- [126: Why should login error messages be vague?](#126-why-should-login-error-messages-be-vague)
- [127: What should the password reset flow look like?](#127-what-should-the-password-reset-flow-look-like)
- [128: What is the difference between encoding, hashing and encryption?](#128-what-is-the-difference-between-encoding-hashing-and-encryption)
- [129: What does X-Content-Type-Options: nosniff do?](#129-what-does-x-content-type-options-nosniff-do)
- [130: What does Content-Security-Policy do?](#130-what-does-content-security-policy-do)
- [131: Why remove the X-Powered-By header?](#131-why-remove-the-x-powered-by-header)
- [132: How do you get the Express-specific app type in Nest?](#132-how-do-you-get-the-express-specific-app-type-in-nest)
- [133: What does trust proxy do?](#133-what-does-trust-proxy-do)
- [134: What is the principle of least privilege?](#134-what-is-the-principle-of-least-privilege)
- [135: What is defense in depth?](#135-what-is-defense-in-depth)
- [136: What is secure by default in the context of guards?](#136-what-is-secure-by-default-in-the-context-of-guards)
- [137: What is session fixation?](#137-what-is-session-fixation)
- [138: What is clickjacking?](#138-what-is-clickjacking)
- [139: Why is the default JwtModule secret a problem if it's hard-coded?](#139-why-is-the-default-jwtmodule-secret-a-problem-if-its-hard-coded)
- [140: How long should a JWT HMAC secret be?](#140-how-long-should-a-jwt-hmac-secret-be)
- [141: What does the crypto module in Node give you for security work?](#141-what-does-the-crypto-module-in-node-give-you-for-security-work)
- [142: Why use crypto.randomBytes instead of Math.random for tokens?](#142-why-use-cryptorandombytes-instead-of-mathrandom-for-tokens)
- [143: What is the difference between a 401 and a 403 when using guards?](#143-what-is-the-difference-between-a-401-and-a-403-when-using-guards)
- [144: What is a security header you might add that Helmet doesn't set by default?](#144-what-is-a-security-header-you-might-add-that-helmet-doesnt-set-by-default)
- [145: What is a WAF?](#145-what-is-a-waf)
- [146: Why disable stack traces in production logs sent to clients but keep them in server logs?](#146-why-disable-stack-traces-in-production-logs-sent-to-clients-but-keep-them-in-server-logs)
- [147: What is a CVE?](#147-what-is-a-cve)
- [148: What is a security.txt file?](#148-what-is-a-securitytxt-file)
- [149: Why should you keep Nest and Node.js up to date?](#149-why-should-you-keep-nest-and-nodejs-up-to-date)
- [150: What is the first thing you check in a NestJS security review?](#150-what-is-the-first-thing-you-check-in-a-nestjs-security-review)

### Moderate Questions (151-300)

- [151: How do you write a JWT auth guard without Passport?](#151-how-do-you-write-a-jwt-auth-guard-without-passport)
- [152: How do you make the Passport JWT guard respect a Public decorator?](#152-how-do-you-make-the-passport-jwt-guard-respect-a-public-decorator)
- [153: How do you configure JwtModule with ConfigService?](#153-how-do-you-configure-jwtmodule-with-configservice)
- [154: Why should you check iss and aud claims?](#154-why-should-you-check-iss-and-aud-claims)
- [155: Why should you set the algorithms option when verifying JWTs?](#155-why-should-you-set-the-algorithms-option-when-verifying-jwts)
- [156: When would you choose RS256 over HS256?](#156-when-would-you-choose-rs256-over-hs256)
- [157: How do you sign tokens with RS256 in Nest?](#157-how-do-you-sign-tokens-with-rs256-in-nest)
- [158: How do you use different secrets for access and refresh tokens?](#158-how-do-you-use-different-secrets-for-access-and-refresh-tokens)
- [159: How do you store refresh tokens on the server?](#159-how-do-you-store-refresh-tokens-on-the-server)
- [160: What is refresh token rotation?](#160-what-is-refresh-token-rotation)
- [161: What is refresh token reuse detection?](#161-what-is-refresh-token-reuse-detection)
- [162: How would you write a refresh endpoint?](#162-how-would-you-write-a-refresh-endpoint)
- [163: How do you log a user out when you use JWTs?](#163-how-do-you-log-a-user-out-when-you-use-jwts)
- [164: How do you revoke all tokens for a user, for example after a password change?](#164-how-do-you-revoke-all-tokens-for-a-user-for-example-after-a-password-change)
- [165: Where should a browser app keep the access token?](#165-where-should-a-browser-app-keep-the-access-token)
- [166: How do you set up Passport sessions in Nest?](#166-how-do-you-set-up-passport-sessions-in-nest)
- [167: Why serialize only the user id into the session?](#167-why-serialize-only-the-user-id-into-the-session)
- [168: How do you use Redis as a session store?](#168-how-do-you-use-redis-as-a-session-store)
- [169: How do you regenerate the session id at login?](#169-how-do-you-regenerate-the-session-id-at-login)
- [170: How do you combine an auth guard and a roles guard globally?](#170-how-do-you-combine-an-auth-guard-and-a-roles-guard-globally)
- [171: Why should roles be checked against the database instead of only the token?](#171-why-should-roles-be-checked-against-the-database-instead-of-only-the-token)
- [172: How do you define a CASL ability factory in Nest?](#172-how-do-you-define-a-casl-ability-factory-in-nest)
- [173: How do you check a CASL rule in a service?](#173-how-do-you-check-a-casl-rule-in-a-service)
- [174: What is a policies guard?](#174-what-is-a-policies-guard)
- [175: How do you limit which fields a user can update with CASL?](#175-how-do-you-limit-which-fields-a-user-can-update-with-casl)
- [176: How do you fetch only records the user may read with CASL and Prisma?](#176-how-do-you-fetch-only-records-the-user-may-read-with-casl-and-prisma)
- [177: What are good ValidationPipe options for a public API?](#177-what-are-good-validationpipe-options-for-a-public-api)
- [178: What does forbidUnknownValues do?](#178-what-does-forbidunknownvalues-do)
- [179: Why is enableImplicitConversion risky?](#179-why-is-enableimplicitconversion-risky)
- [180: How do you validate query parameters safely?](#180-how-do-you-validate-query-parameters-safely)
- [181: Why should every string field have a max length?](#181-why-should-every-string-field-have-a-max-length)
- [182: How can a regular expression in a DTO cause a DoS?](#182-how-can-a-regular-expression-in-a-dto-cause-a-dos)
- [183: How do you validate a DTO with different rules for create and update?](#183-how-do-you-validate-a-dto-with-different-rules-for-create-and-update)
- [184: How do you use validation groups for different roles?](#184-how-do-you-use-validation-groups-for-different-roles)
- [185: How do you return a user without the password using @Exclude and groups?](#185-how-do-you-return-a-user-without-the-password-using-exclude-and-groups)
- [186: What is the safest default for serialization?](#186-what-is-the-safest-default-for-serialization)
- [187: How do you register ClassSerializerInterceptor globally?](#187-how-do-you-register-classserializerinterceptor-globally)
- [188: How do you hide fields when you use Prisma?](#188-how-do-you-hide-fields-when-you-use-prisma)
- [189: How do you hide fields with Mongoose?](#189-how-do-you-hide-fields-with-mongoose)
- [190: How do you configure Helmet's CSP for an API with Swagger UI?](#190-how-do-you-configure-helmets-csp-for-an-api-with-swagger-ui)
- [191: How do you use Helmet with the Fastify adapter?](#191-how-do-you-use-helmet-with-the-fastify-adapter)
- [192: Why does Helmet's CSP break the GraphQL playground or Apollo Sandbox?](#192-why-does-helmets-csp-break-the-graphql-playground-or-apollo-sandbox)
- [193: How do you allow CORS for several origins safely?](#193-how-do-you-allow-cors-for-several-origins-safely)
- [194: Why can't you use origin: '*' with credentials: true?](#194-why-cant-you-use-origin--with-credentials-true)
- [195: What's wrong with checking CORS origins with a regex like /example.com/?](#195-whats-wrong-with-checking-cors-origins-with-a-regex-like-examplecom)
- [196: How do you set up csrf-csrf in a Nest app?](#196-how-do-you-set-up-csrf-csrf-in-a-nest-app)
- [197: Which HTTP methods need CSRF protection?](#197-which-http-methods-need-csrf-protection)
- [198: Is SameSite=Lax enough to stop CSRF?](#198-is-samesitelax-enough-to-stop-csrf)
- [199: How do you use several rate limits at once?](#199-how-do-you-use-several-rate-limits-at-once)
- [200: How do you store throttler counters in Redis?](#200-how-do-you-store-throttler-counters-in-redis)
- [201: How do you rate limit by user instead of by IP?](#201-how-do-you-rate-limit-by-user-instead-of-by-ip)
- [202: Why can rate limiting by IP alone be a problem?](#202-why-can-rate-limiting-by-ip-alone-be-a-problem)
- [203: How do you limit failed logins per account?](#203-how-do-you-limit-failed-logins-per-account)
- [204: What bcrypt cost factor should you pick?](#204-what-bcrypt-cost-factor-should-you-pick)
- [205: What is the 72-byte limit in bcrypt?](#205-what-is-the-72-byte-limit-in-bcrypt)
- [206: Why is password hashing done asynchronously in Node?](#206-why-is-password-hashing-done-asynchronously-in-node)
- [207: How do you upgrade old password hashes to a new algorithm?](#207-how-do-you-upgrade-old-password-hashes-to-a-new-algorithm)
- [208: How do you compare API keys without timing leaks?](#208-how-do-you-compare-api-keys-without-timing-leaks)
- [209: Why is SHA-256 fine for API keys but not for passwords?](#209-why-is-sha-256-fine-for-api-keys-but-not-for-passwords)
- [210: What should an API key system support?](#210-what-should-an-api-key-system-support)
- [211: How do you add Google login with Passport in Nest?](#211-how-do-you-add-google-login-with-passport-in-nest)
- [212: What is the state parameter in OAuth?](#212-what-is-the-state-parameter-in-oauth)
- [213: What is PKCE?](#213-what-is-pkce)
- [214: Which OAuth flows should you not use anymore?](#214-which-oauth-flows-should-you-not-use-anymore)
- [215: How do you validate tokens issued by an external identity provider?](#215-how-do-you-validate-tokens-issued-by-an-external-identity-provider)
- [216: How do you validate external tokens with the jose library?](#216-how-do-you-validate-external-tokens-with-the-jose-library)
- [217: What is the client credentials flow?](#217-what-is-the-client-credentials-flow)
- [218: How do you check OAuth scopes in a guard?](#218-how-do-you-check-oauth-scopes-in-a-guard)
- [219: How do you validate env variables with Joi?](#219-how-do-you-validate-env-variables-with-joi)
- [220: How do you validate env variables with class-validator?](#220-how-do-you-validate-env-variables-with-class-validator)
- [221: How do you load secrets from AWS Secrets Manager or Vault into Nest?](#221-how-do-you-load-secrets-from-aws-secrets-manager-or-vault-into-nest)
- [222: Why is it risky to log the whole config at startup?](#222-why-is-it-risky-to-log-the-whole-config-at-startup)
- [223: How do you serve Nest over HTTPS directly?](#223-how-do-you-serve-nest-over-https-directly)
- [224: How do you redirect HTTP to HTTPS when behind a proxy?](#224-how-do-you-redirect-http-to-https-when-behind-a-proxy)
- [225: How do you encrypt a field before storing it?](#225-how-do-you-encrypt-a-field-before-storing-it)
- [226: Why use AES-GCM instead of AES-CBC?](#226-why-use-aes-gcm-instead-of-aes-cbc)
- [227: How can you search a column that is encrypted?](#227-how-can-you-search-a-column-that-is-encrypted)
- [228: How do you plug field encryption into TypeORM?](#228-how-do-you-plug-field-encryption-into-typeorm)
- [229: How do you build a dynamic ORDER BY safely in TypeORM?](#229-how-do-you-build-a-dynamic-order-by-safely-in-typeorm)
- [230: How do you write a safe raw query in Prisma?](#230-how-do-you-write-a-safe-raw-query-in-prisma)
- [231: How do you write a safe raw query in TypeORM?](#231-how-do-you-write-a-safe-raw-query-in-typeorm)
- [232: Is the Raw operator in TypeORM safe?](#232-is-the-raw-operator-in-typeorm-safe)
- [233: How do you protect Mongoose queries from operator injection?](#233-how-do-you-protect-mongoose-queries-from-operator-injection)
- [234: Why shouldn't you use $where in MongoDB queries with user input?](#234-why-shouldnt-you-use-where-in-mongodb-queries-with-user-input)
- [235: Why doesn't express-mongo-sanitize work well with Nest 11 and later?](#235-why-doesnt-express-mongo-sanitize-work-well-with-nest-11-and-later)
- [236: How do you sanitize HTML that users submit, like blog posts?](#236-how-do-you-sanitize-html-that-users-submit-like-blog-posts)
- [237: How can you sanitize input with a decorator in a DTO?](#237-how-can-you-sanitize-input-with-a-decorator-in-a-dto)
- [238: Why can javascript: URLs be an XSS problem even with escaping?](#238-why-can-javascript-urls-be-an-xss-problem-even-with-escaping)
- [239: How do you stop uploaded files from being served as HTML?](#239-how-do-you-stop-uploaded-files-from-being-served-as-html)
- [240: Why isn't the client's MIME type enough to check a file?](#240-why-isnt-the-clients-mime-type-enough-to-check-a-file)
- [241: How do you build file validation with ParseFilePipeBuilder?](#241-how-do-you-build-file-validation-with-parsefilepipebuilder)
- [242: Which Multer limits should you set besides fileSize?](#242-which-multer-limits-should-you-set-besides-filesize)
- [243: Should you use memory storage or disk storage for uploads?](#243-should-you-use-memory-storage-or-disk-storage-for-uploads)
- [244: How do you scan uploads for malware?](#244-how-do-you-scan-uploads-for-malware)
- [245: How do you avoid path traversal when saving files to disk?](#245-how-do-you-avoid-path-traversal-when-saving-files-to-disk)
- [246: How do you write a global filter that hides internal errors?](#246-how-do-you-write-a-global-filter-that-hides-internal-errors)
- [247: How do you turn a Prisma unique constraint error into a safe response?](#247-how-do-you-turn-a-prisma-unique-constraint-error-into-a-safe-response)
- [248: Can a 409 "email already exists" response be a problem?](#248-can-a-409-email-already-exists-response-be-a-problem)
- [249: How do you add a request id to every log line?](#249-how-do-you-add-a-request-id-to-every-log-line)
- [250: How do you hide secrets in nestjs-pino logs?](#250-how-do-you-hide-secrets-in-nestjs-pino-logs)
- [251: How do you build an audit log with an interceptor?](#251-how-do-you-build-an-audit-log-with-an-interceptor)
- [252: Why log denied requests from guards?](#252-why-log-denied-requests-from-guards)
- [253: How do you authenticate a Socket.IO connection in a Nest gateway?](#253-how-do-you-authenticate-a-socketio-connection-in-a-nest-gateway)
- [254: How do you use Socket.IO middleware for authentication in Nest?](#254-how-do-you-use-socketio-middleware-for-authentication-in-nest)
- [255: How do you write a guard for WebSocket messages?](#255-how-do-you-write-a-guard-for-websocket-messages)
- [256: Do pipes and validation work on WebSocket messages?](#256-do-pipes-and-validation-work-on-websocket-messages)
- [257: How do you stop users from joining rooms they don't belong to?](#257-how-do-you-stop-users-from-joining-rooms-they-dont-belong-to)
- [258: Why set CORS on the WebSocket gateway separately?](#258-why-set-cors-on-the-websocket-gateway-separately)
- [259: How do you add a depth limit to Nest GraphQL with Apollo?](#259-how-do-you-add-a-depth-limit-to-nest-graphql-with-apollo)
- [260: How do you set field complexity in a code-first GraphQL schema?](#260-how-do-you-set-field-complexity-in-a-code-first-graphql-schema)
- [261: How do you write a query complexity plugin for Apollo in Nest?](#261-how-do-you-write-a-query-complexity-plugin-for-apollo-in-nest)
- [262: How do you apply a guard to a GraphQL resolver?](#262-how-do-you-apply-a-guard-to-a-graphql-resolver)
- [263: How do you write a param decorator that works for both REST and GraphQL?](#263-how-do-you-write-a-param-decorator-that-works-for-both-rest-and-graphql)
- [264: How do you protect a single GraphQL field?](#264-how-do-you-protect-a-single-graphql-field)
- [265: What is a GraphQL batching or aliasing attack?](#265-what-is-a-graphql-batching-or-aliasing-attack)
- [266: How do you secure a Nest TCP microservice with TLS?](#266-how-do-you-secure-a-nest-tcp-microservice-with-tls)
- [267: How do you connect to RabbitMQ securely from Nest?](#267-how-do-you-connect-to-rabbitmq-securely-from-nest)
- [268: How do you set up Kafka authentication in a Nest microservice?](#268-how-do-you-set-up-kafka-authentication-in-a-nest-microservice)
- [269: How do you use guards on microservice message handlers?](#269-how-do-you-use-guards-on-microservice-message-handlers)
- [270: How do you pass the user identity from a gateway to an internal service?](#270-how-do-you-pass-the-user-identity-from-a-gateway-to-an-internal-service)
- [271: How do you get the tenant id for a request?](#271-how-do-you-get-the-tenant-id-for-a-request)
- [272: How do you carry the tenant id through the app without passing it everywhere?](#272-how-do-you-carry-the-tenant-id-through-the-app-without-passing-it-everywhere)
- [273: How do you make sure every query filters by tenant?](#273-how-do-you-make-sure-every-query-filters-by-tenant)
- [274: How do you add the tenant filter with a Prisma client extension?](#274-how-do-you-add-the-tenant-filter-with-a-prisma-client-extension)
- [275: What does the __Host- cookie prefix do?](#275-what-does-the-__host--cookie-prefix-do)
- [276: How do you use signed cookies in Nest?](#276-how-do-you-use-signed-cookies-in-nest)
- [277: How do you clear an auth cookie correctly?](#277-how-do-you-clear-an-auth-cookie-correctly)
- [278: How do you change the JSON body limit in Nest?](#278-how-do-you-change-the-json-body-limit-in-nest)
- [279: How do you allow a large body on one route only?](#279-how-do-you-allow-a-large-body-on-one-route-only)
- [280: How do you set server timeouts to protect against slow clients?](#280-how-do-you-set-server-timeouts-to-protect-against-slow-clients)
- [281: How do you add a timeout to slow handlers?](#281-how-do-you-add-a-timeout-to-slow-handlers)
- [282: How do you run npm audit in CI without blocking on low issues?](#282-how-do-you-run-npm-audit-in-ci-without-blocking-on-low-issues)
- [283: What does npm audit signatures check?](#283-what-does-npm-audit-signatures-check)
- [284: Why use --ignore-scripts for installs?](#284-why-use---ignore-scripts-for-installs)
- [285: How do you write an e2e test that logs in and calls a protected route?](#285-how-do-you-write-an-e2e-test-that-logs-in-and-calls-a-protected-route)
- [286: How do you test that one user can't read another user's data?](#286-how-do-you-test-that-one-user-cant-read-another-users-data)
- [287: How do you override a guard in a unit or e2e test?](#287-how-do-you-override-a-guard-in-a-unit-or-e2e-test)
- [288: Why should e2e tests apply the same global setup as main.ts?](#288-why-should-e2e-tests-apply-the-same-global-setup-as-maints)
- [289: How do you test the ValidationPipe whitelist behavior?](#289-how-do-you-test-the-validationpipe-whitelist-behavior)
- [290: How do you test that responses don't contain sensitive fields?](#290-how-do-you-test-that-responses-dont-contain-sensitive-fields)
- [291: How do you check that security headers are present in tests?](#291-how-do-you-check-that-security-headers-are-present-in-tests)
- [292: How do you scan a running Nest API automatically?](#292-how-do-you-scan-a-running-nest-api-automatically)
- [293: Where does Nest code map to OWASP Top 10 categories?](#293-where-does-nest-code-map-to-owasp-top-10-categories)
- [294: What is SSRF and how can it happen in Nest?](#294-what-is-ssrf-and-how-can-it-happen-in-nest)
- [295: How do you safely call user-supplied webhook URLs?](#295-how-do-you-safely-call-user-supplied-webhook-urls)
- [296: How do you sign outgoing webhooks so receivers can trust them?](#296-how-do-you-sign-outgoing-webhooks-so-receivers-can-trust-them)
- [297: How do you verify an incoming webhook signature in Nest?](#297-how-do-you-verify-an-incoming-webhook-signature-in-nest)
- [298: How do you keep Swagger docs from exposing internal endpoints?](#298-how-do-you-keep-swagger-docs-from-exposing-internal-endpoints)
- [299: Why should NODE_ENV be production in production?](#299-why-should-node_env-be-production-in-production)
- [300: How do you run Nest in Docker with fewer privileges?](#300-how-do-you-run-nest-in-docker-with-fewer-privileges)

### Advanced Questions (301-450)

- [301: Why can't a guard rely on the validated DTO, and how do you handle that?](#301-why-cant-a-guard-rely-on-the-validated-dto-and-how-do-you-handle-that)
- [302: How do you write one auth guard that works for HTTP, WebSockets, RPC and GraphQL?](#302-how-do-you-write-one-auth-guard-that-works-for-http-websockets-rpc-and-graphql)
- [303: In what order do APP_GUARD providers run when they come from different modules?](#303-in-what-order-do-app_guard-providers-run-when-they-come-from-different-modules)
- [304: What goes wrong if a guard is request-scoped?](#304-what-goes-wrong-if-a-guard-is-request-scoped)
- [305: How would you design auth for an app with a web SPA and a mobile app?](#305-how-would-you-design-auth-for-an-app-with-a-web-spa-and-a-mobile-app)
- [306: What is the backend-for-frontend (BFF) pattern for auth?](#306-what-is-the-backend-for-frontend-bff-pattern-for-auth)
- [307: How would you design JWT revocation for millions of users?](#307-how-would-you-design-jwt-revocation-for-millions-of-users)
- [308: How do you rotate JWT signing keys without logging everyone out?](#308-how-do-you-rotate-jwt-signing-keys-without-logging-everyone-out)
- [309: How do you expose a JWKS endpoint from a Nest auth service?](#309-how-do-you-expose-a-jwks-endpoint-from-a-nest-auth-service)
- [310: What is a sender-constrained token and why would you use DPoP?](#310-what-is-a-sender-constrained-token-and-why-would-you-use-dpop)
- [311: How do you handle parallel refresh requests from several browser tabs with rotation?](#311-how-do-you-handle-parallel-refresh-requests-from-several-browser-tabs-with-rotation)
- [312: How do you make refresh token rotation safe from race conditions in the database?](#312-how-do-you-make-refresh-token-rotation-safe-from-race-conditions-in-the-database)
- [313: Should the auth guard fail open or fail closed when Redis is down?](#313-should-the-auth-guard-fail-open-or-fail-closed-when-redis-is-down)
- [314: What happens to rate limiting if the Redis throttler storage is down?](#314-what-happens-to-rate-limiting-if-the-redis-throttler-storage-is-down)
- [315: How does @nestjs/throttler count requests internally?](#315-how-does-nestjsthrottler-count-requests-internally)
- [316: Why can the default throttler tracker be wrong behind a proxy?](#316-why-can-the-default-throttler-tracker-be-wrong-behind-a-proxy)
- [317: How do you rate limit by the target account on login and not just by IP?](#317-how-do-you-rate-limit-by-the-target-account-on-login-and-not-just-by-ip)
- [318: How do you prevent memory growth from the in-memory throttler?](#318-how-do-you-prevent-memory-growth-from-the-in-memory-throttler)
- [319: How can a timing difference leak whether a user exists?](#319-how-can-a-timing-difference-leak-whether-a-user-exists)
- [320: What Argon2id parameters would you choose and why?](#320-what-argon2id-parameters-would-you-choose-and-why)
- [321: How can password hashing itself become a DoS vector?](#321-how-can-password-hashing-itself-become-a-dos-vector)
- [322: What is a password breach check and how do you add it without sending the password?](#322-what-is-a-password-breach-check-and-how-do-you-add-it-without-sending-the-password)
- [323: How would you design API key scopes and enforcement?](#323-how-would-you-design-api-key-scopes-and-enforcement)
- [324: How do you design API key rotation for customers?](#324-how-do-you-design-api-key-rotation-for-customers)
- [325: How do you detect leaked API keys?](#325-how-do-you-detect-leaked-api-keys)
- [326: What are the risks of implementing OAuth login callbacks yourself?](#326-what-are-the-risks-of-implementing-oauth-login-callbacks-yourself)
- [327: Why is linking accounts by email dangerous in social login?](#327-why-is-linking-accounts-by-email-dangerous-in-social-login)
- [328: How do you prevent open redirects after login?](#328-how-do-you-prevent-open-redirects-after-login)
- [329: How do you use openid-client in a Nest app?](#329-how-do-you-use-openid-client-in-a-nest-app)
- [330: How would you support SSO for many enterprise customers in one Nest app?](#330-how-would-you-support-sso-for-many-enterprise-customers-in-one-nest-app)
- [331: What is SCIM and why does it matter for security?](#331-what-is-scim-and-why-does-it-matter-for-security)
- [332: How do you handle back-channel logout from an identity provider?](#332-how-do-you-handle-back-channel-logout-from-an-identity-provider)
- [333: How would you design authorization for a large app with many rules?](#333-how-would-you-design-authorization-for-a-large-app-with-many-rules)
- [334: When would you use relationship-based access control (ReBAC)?](#334-when-would-you-use-relationship-based-access-control-rebac)
- [335: Why is checking permissions only in guards not enough for list endpoints?](#335-why-is-checking-permissions-only-in-guards-not-enough-for-list-endpoints)
- [336: How do you avoid a TOCTOU bug in authorization checks?](#336-how-do-you-avoid-a-toctou-bug-in-authorization-checks)
- [337: What problems come from returning 403 versus 404 for records a user can't see?](#337-what-problems-come-from-returning-403-versus-404-for-records-a-user-cant-see)
- [338: How would you handle impersonation ("log in as user") for support staff securely?](#338-how-would-you-handle-impersonation-log-in-as-user-for-support-staff-securely)
- [339: How does the ValidationPipe actually validate, and what does that mean for performance?](#339-how-does-the-validationpipe-actually-validate-and-what-does-that-mean-for-performance)
- [340: How can class-transformer be abused with prototype pollution?](#340-how-can-class-transformer-be-abused-with-prototype-pollution)
- [341: Why is validating only the DTO not enough for a PATCH endpoint?](#341-why-is-validating-only-the-dto-not-enough-for-a-patch-endpoint)
- [342: How do you validate a discriminated union body in class-validator?](#342-how-do-you-validate-a-discriminated-union-body-in-class-validator)
- [343: When would you use Standard Schema validation in Nest 12 instead of class-validator?](#343-when-would-you-use-standard-schema-validation-in-nest-12-instead-of-class-validator)
- [344: How do you make sure no route accepts an unvalidated body by mistake?](#344-how-do-you-make-sure-no-route-accepts-an-unvalidated-body-by-mistake)
- [345: Why does ValidationPipe skip validation when the parameter type is an interface?](#345-why-does-validationpipe-skip-validation-when-the-parameter-type-is-an-interface)
- [346: How can serialization leak data through relations?](#346-how-can-serialization-leak-data-through-relations)
- [347: Why are dedicated response DTOs safer than returning entities?](#347-why-are-dedicated-response-dtos-safer-than-returning-entities)
- [348: What is a "BOLA" bug in an API and how do you design to avoid it?](#348-what-is-a-bola-bug-in-an-api-and-how-do-you-design-to-avoid-it)
- [349: What is BFLA and how does it show up in Nest?](#349-what-is-bfla-and-how-does-it-show-up-in-nest)
- [350: How would you scan your Nest routes to find missing authorization?](#350-how-would-you-scan-your-nest-routes-to-find-missing-authorization)
- [351: How does Helmet's default CSP differ for an API compared to a website?](#351-how-does-helmets-default-csp-differ-for-an-api-compared-to-a-website)
- [352: How do you use CSP nonces in a Nest app that renders HTML?](#352-how-do-you-use-csp-nonces-in-a-nest-app-that-renders-html)
- [353: How do you roll out a strict CSP without breaking a live site?](#353-how-do-you-roll-out-a-strict-csp-without-breaking-a-live-site)
- [354: Why is a dynamic CORS origin function a common source of bugs?](#354-why-is-a-dynamic-cors-origin-function-a-common-source-of-bugs)
- [355: What should the Vary header be when CORS origins are dynamic?](#355-what-should-the-vary-header-be-when-cors-origins-are-dynamic)
- [356: How do you protect a cookie-based API against CSRF without tokens?](#356-how-do-you-protect-a-cookie-based-api-against-csrf-without-tokens)
- [357: Why does requiring a JSON content type help against CSRF?](#357-why-does-requiring-a-json-content-type-help-against-csrf)
- [358: What is login CSRF and how do you prevent it?](#358-what-is-login-csrf-and-how-do-you-prevent-it)
- [359: How would you implement step-up authentication for sensitive actions?](#359-how-would-you-implement-step-up-authentication-for-sensitive-actions)
- [360: How do you implement TOTP MFA securely?](#360-how-do-you-implement-totp-mfa-securely)
- [361: How do you design account recovery without making it the weakest link?](#361-how-do-you-design-account-recovery-without-making-it-the-weakest-link)
- [362: Why should key material for encryption not be stored in the same database as encrypted data?](#362-why-should-key-material-for-encryption-not-be-stored-in-the-same-database-as-encrypted-data)
- [363: What is envelope encryption?](#363-what-is-envelope-encryption)
- [364: How would you rotate an application-level encryption key?](#364-how-would-you-rotate-an-application-level-encryption-key)
- [365: How do you enforce TLS between Nest and the database?](#365-how-do-you-enforce-tls-between-nest-and-the-database)
- [366: When should traffic behind the load balancer also use TLS?](#366-when-should-traffic-behind-the-load-balancer-also-use-tls)
- [367: How do you build a SQL injection-safe dynamic filter API in TypeORM?](#367-how-do-you-build-a-sql-injection-safe-dynamic-filter-api-in-typeorm)
- [368: How can Prisma.raw or $queryRawUnsafe sneak injection into a "safe" Prisma codebase?](#368-how-can-prismaraw-or-queryrawunsafe-sneak-injection-into-a-safe-prisma-codebase)
- [369: Can Prisma's where input be abused if you pass request data directly?](#369-can-prismas-where-input-be-abused-if-you-pass-request-data-directly)
- [370: How do NoSQL injection risks look with Mongoose populate and aggregation?](#370-how-do-nosql-injection-risks-look-with-mongoose-populate-and-aggregation)
- [371: Why is regex search with user input risky in MongoDB?](#371-why-is-regex-search-with-user-input-risky-in-mongodb)
- [372: How do you prevent header injection when setting values from user input?](#372-how-do-you-prevent-header-injection-when-setting-values-from-user-input)
- [373: What is server-side template injection and can it happen in Nest?](#373-what-is-server-side-template-injection-and-can-it-happen-in-nest)
- [374: How do you prevent CSV or formula injection in exports?](#374-how-do-you-prevent-csv-or-formula-injection-in-exports)
- [375: Why are SVG uploads especially risky?](#375-why-are-svg-uploads-especially-risky)
- [376: How do you safely process uploaded images?](#376-how-do-you-safely-process-uploaded-images)
- [377: How do you protect against zip bombs when users upload archives?](#377-how-do-you-protect-against-zip-bombs-when-users-upload-archives)
- [378: How would you design direct-to-S3 uploads securely from Nest?](#378-how-would-you-design-direct-to-s3-uploads-securely-from-nest)
- [379: How do exception filters interact with errors from guards and interceptors?](#379-how-do-exception-filters-interact-with-errors-from-guards-and-interceptors)
- [380: How do you return consistent error codes without leaking details?](#380-how-do-you-return-consistent-error-codes-without-leaking-details)
- [381: Why can validation error messages leak information?](#381-why-can-validation-error-messages-leak-information)
- [382: How do you handle errors from a third-party API without leaking its details?](#382-how-do-you-handle-errors-from-a-third-party-api-without-leaking-its-details)
- [383: How do you make security logs useful for incident response?](#383-how-do-you-make-security-logs-useful-for-incident-response)
- [384: How do you make audit logs tamper-evident?](#384-how-do-you-make-audit-logs-tamper-evident)
- [385: How do you avoid logging personal data while keeping logs useful?](#385-how-do-you-avoid-logging-personal-data-while-keeping-logs-useful)
- [386: Why do guards not run on WebSocket handleConnection, and what's the impact?](#386-why-do-guards-not-run-on-websocket-handleconnection-and-whats-the-impact)
- [387: How do you handle token expiry on a long-lived WebSocket connection?](#387-how-do-you-handle-token-expiry-on-a-long-lived-websocket-connection)
- [388: How do you rate limit WebSocket messages?](#388-how-do-you-rate-limit-websocket-messages)
- [389: What is cross-site WebSocket hijacking?](#389-what-is-cross-site-websocket-hijacking)
- [390: How do you scale secure broadcasts across many gateway instances?](#390-how-do-you-scale-secure-broadcasts-across-many-gateway-instances)
- [391: How do you protect GraphQL against expensive list arguments?](#391-how-do-you-protect-graphql-against-expensive-list-arguments)
- [392: What are persisted queries and how do they help security?](#392-what-are-persisted-queries-and-how-do-they-help-security)
- [393: How does the N+1 problem relate to GraphQL DoS?](#393-how-does-the-n1-problem-relate-to-graphql-dos)
- [394: How do you hide GraphQL error details in production?](#394-how-do-you-hide-graphql-error-details-in-production)
- [395: What is GraphQL field suggestion leakage?](#395-what-is-graphql-field-suggestion-leakage)
- [396: How do you make sure field resolvers check authorization, not just the root query?](#396-how-do-you-make-sure-field-resolvers-check-authorization-not-just-the-root-query)
- [397: Do Nest guards run for GraphQL field resolvers?](#397-do-nest-guards-run-for-graphql-field-resolvers)
- [398: How does CSRF apply to GraphQL APIs?](#398-how-does-csrf-apply-to-graphql-apis)
- [399: How do you authenticate gRPC microservices in Nest?](#399-how-do-you-authenticate-grpc-microservices-in-nest)
- [400: Why is a message queue not a trust boundary by itself?](#400-why-is-a-message-queue-not-a-trust-boundary-by-itself)
- [401: How do you sign messages between microservices?](#401-how-do-you-sign-messages-between-microservices)
- [402: What is the confused deputy problem in microservices?](#402-what-is-the-confused-deputy-problem-in-microservices)
- [403: How does a service mesh change what Nest needs to do for security?](#403-how-does-a-service-mesh-change-what-nest-needs-to-do-for-security)
- [404: How do you use PostgreSQL row-level security with Nest for multi-tenancy?](#404-how-do-you-use-postgresql-row-level-security-with-nest-for-multi-tenancy)
- [405: What breaks RLS-based tenant isolation?](#405-what-breaks-rls-based-tenant-isolation)
- [406: Why are request-scoped providers a common but costly way to do multi-tenancy?](#406-why-are-request-scoped-providers-a-common-but-costly-way-to-do-multi-tenancy)
- [407: How do durable providers work for multi-tenancy?](#407-how-do-durable-providers-work-for-multi-tenancy)
- [408: How do you keep caches from leaking data across tenants or users?](#408-how-do-you-keep-caches-from-leaking-data-across-tenants-or-users)
- [409: How do you isolate background jobs per tenant?](#409-how-do-you-isolate-background-jobs-per-tenant)
- [410: What are the trade-offs of SameSite=Strict for session cookies?](#410-what-are-the-trade-offs-of-samesitestrict-for-session-cookies)
- [411: When do you need SameSite=None and what does it cost?](#411-when-do-you-need-samesitenone-and-what-does-it-cost)
- [412: What are CHIPS (partitioned cookies)?](#412-what-are-chips-partitioned-cookies)
- [413: How can a subdomain attack your cookies?](#413-how-can-a-subdomain-attack-your-cookies)
- [414: How does Express's JSON body parser protect against huge payloads, and where does it fall short?](#414-how-does-expresss-json-body-parser-protect-against-huge-payloads-and-where-does-it-fall-short)
- [415: How do slowloris attacks affect Node servers and how do you stop them?](#415-how-do-slowloris-attacks-affect-node-servers-and-how-do-you-stop-them)
- [416: How do you find event loop blocking that attackers could trigger?](#416-how-do-you-find-event-loop-blocking-that-attackers-could-trigger)
- [417: How do you protect expensive endpoints like exports or reports from abuse?](#417-how-do-you-protect-expensive-endpoints-like-exports-or-reports-from-abuse)
- [418: How do you add per-tenant quotas, not just rate limits?](#418-how-do-you-add-per-tenant-quotas-not-just-rate-limits)
- [419: How would you respond to a compromised npm package in your dependency tree?](#419-how-would-you-respond-to-a-compromised-npm-package-in-your-dependency-tree)
- [420: How do you reduce the chance of installing a freshly hijacked package version?](#420-how-do-you-reduce-the-chance-of-installing-a-freshly-hijacked-package-version)
- [421: What is dependency confusion?](#421-what-is-dependency-confusion)
- [422: What is an SBOM and why would a Nest team generate one?](#422-what-is-an-sbom-and-why-would-a-nest-team-generate-one)
- [423: How do you handle a vulnerability in a transitive dependency with no fix from the direct dependency?](#423-how-do-you-handle-a-vulnerability-in-a-transitive-dependency-with-no-fix-from-the-direct-dependency)
- [424: Why is npm audit output often noisy, and how do you make it useful?](#424-why-is-npm-audit-output-often-noisy-and-how-do-you-make-it-useful)
- [425: How do you protect the CI pipeline as part of supply-chain security?](#425-how-do-you-protect-the-ci-pipeline-as-part-of-supply-chain-security)
- [426: How would you map a NestJS codebase to OWASP ASVS for a security review?](#426-how-would-you-map-a-nestjs-codebase-to-owasp-asvs-for-a-security-review)
- [427: What should an e2e security test suite for a Nest API cover?](#427-what-should-an-e2e-security-test-suite-for-a-nest-api-cover)
- [428: How do you generate auth tests for every route automatically?](#428-how-do-you-generate-auth-tests-for-every-route-automatically)
- [429: How do you test JWT tampering in e2e tests?](#429-how-do-you-test-jwt-tampering-in-e2e-tests)
- [430: How would you fuzz a Nest API?](#430-how-would-you-fuzz-a-nest-api)
- [431: A user reports they can see another company's invoices. How do you investigate?](#431-a-user-reports-they-can-see-another-companys-invoices-how-do-you-investigate)
- [432: Your logs show many failed logins across thousands of accounts from rotating IPs. What do you do?](#432-your-logs-show-many-failed-logins-across-thousands-of-accounts-from-rotating-ips-what-do-you-do)
- [433: You find a JWT secret committed to a public repo six months ago. What's the plan?](#433-you-find-a-jwt-secret-committed-to-a-public-repo-six-months-ago-whats-the-plan)
- [434: An endpoint returns 500 with a stack trace in production. What's wrong and how do you fix it?](#434-an-endpoint-returns-500-with-a-stack-trace-in-production-whats-wrong-and-how-do-you-fix-it)
- [435: How would you secure an admin panel built into the same Nest app?](#435-how-would-you-secure-an-admin-panel-built-into-the-same-nest-app)
- [436: How do you prevent privilege escalation through a "update my profile" endpoint?](#436-how-do-you-prevent-privilege-escalation-through-a-update-my-profile-endpoint)
- [437: How would you design secure file downloads for user documents?](#437-how-would-you-design-secure-file-downloads-for-user-documents)
- [438: What security concerns come with using Nest's built-in HttpModule for outgoing requests?](#438-what-security-concerns-come-with-using-nests-built-in-httpmodule-for-outgoing-requests)
- [439: How do you secure Nest apps running in Kubernetes?](#439-how-do-you-secure-nest-apps-running-in-kubernetes)
- [440: What should a health check endpoint expose?](#440-what-should-a-health-check-endpoint-expose)
- [441: How do you protect against secrets leaking through error tracking tools like Sentry?](#441-how-do-you-protect-against-secrets-leaking-through-error-tracking-tools-like-sentry)
- [442: How would you handle GDPR "right to be forgotten" securely in a Nest app?](#442-how-would-you-handle-gdpr-right-to-be-forgotten-securely-in-a-nest-app)
- [443: How do you think about trust boundaries when designing a new Nest feature?](#443-how-do-you-think-about-trust-boundaries-when-designing-a-new-nest-feature)
- [444: What is STRIDE and how would you apply it to a Nest login feature?](#444-what-is-stride-and-how-would-you-apply-it-to-a-nest-login-feature)
- [445: What are the security trade-offs of putting roles and permissions in the JWT?](#445-what-are-the-security-trade-offs-of-putting-roles-and-permissions-in-the-jwt)
- [446: How do you design an API for both public consumers and internal services without weakening security?](#446-how-do-you-design-an-api-for-both-public-consumers-and-internal-services-without-weakening-security)
- [447: Why should you avoid writing your own crypto, even in small helpers?](#447-why-should-you-avoid-writing-your-own-crypto-even-in-small-helpers)
- [448: How would you add security checks to code review for a Nest team?](#448-how-would-you-add-security-checks-to-code-review-for-a-nest-team)
- [449: How do you balance security with developer speed in a Nest codebase?](#449-how-do-you-balance-security-with-developer-speed-in-a-nest-codebase)
- [450: If you had one week to improve the security of an existing Nest API, what would you do?](#450-if-you-had-one-week-to-improve-the-security-of-an-existing-nest-api-what-would-you-do)

---

# Easy Questions (1-150)

## 1: What is the difference between authentication and authorization?

Authentication checks who the user is, for example by checking a password or a token. Authorization checks what that user is allowed to do, for example whether they can delete an order. In Nest you usually do both in guards: one guard reads the token and attaches the user to the request, and another checks roles or permissions.

## 2: Where does security logic usually live in a NestJS app?

Most of it goes into guards (who can call a route), pipes (is the input valid), interceptors (what goes out, logging), exception filters (what errors look like) and middleware (Helmet, CORS, cookies, body limits). Business rules like "a user can only edit their own post" usually live in services or in a policy layer like CASL.

## 3: What is a guard in NestJS?

A guard is a class that implements `CanActivate`. Its `canActivate()` method returns `true` to let the request through or `false` (or throws) to block it. When it returns `false`, Nest responds with `403 Forbidden`.

```ts
@Injectable()
export class AdminGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const req = context.switchToHttp().getRequest();
    return req.user?.role === "admin";
  }
}
```

## 4: How do you apply a guard to a route?

Use `@UseGuards()` on a method or on the whole controller.

```ts
@Controller("admin")
@UseGuards(AuthGuard, AdminGuard)
export class AdminController {
  @Get("stats")
  stats() {
    return this.statsService.get();
  }
}
```

## 5: How do you make a guard global?

Either call `app.useGlobalGuards(new MyGuard())` in `main.ts`, or register it as a provider with the `APP_GUARD` token. The `APP_GUARD` way is better because the guard can use dependency injection.

```ts
@Module({
  providers: [{ provide: APP_GUARD, useClass: AuthGuard }],
})
export class AppModule {}
```

## 6: In what order does Nest run middleware, guards, interceptors and pipes?

Middleware runs first, then guards, then interceptors (the "before" part), then pipes, then the route handler. After that the interceptors run their "after" part. Exception filters handle any error thrown along the way. This matters for security: guards run before pipes, so a guard can't rely on the body being validated yet.

## 7: What is Passport and why is it used with Nest?

Passport is a popular Node.js authentication library with hundreds of "strategies" for things like username and password, JWT, Google login and SAML. The `@nestjs/passport` package wraps it so each strategy becomes an injectable class and you protect routes with `AuthGuard('strategy-name')`.

## 8: Do you need Passport to do authentication in Nest?

No. The official docs show a simple approach where you write your own guard that reads a JWT and verifies it with `JwtService`. Passport is useful when you need many strategies or ready-made OAuth providers, but for a single JWT check a small custom guard is often easier to read.

## 9: What is a JWT?

A JSON Web Token is a string made of three base64url parts separated by dots: a header, a payload with claims, and a signature. The server signs it with a secret or a private key, and later checks the signature to make sure nobody changed it. The payload is only encoded, not encrypted, so anyone can read it.

## 10: What should you never put in a JWT payload?

Anything secret: passwords, password hashes, API keys, full card numbers, or personal data you wouldn't want in logs. The payload can be decoded by anyone who has the token. Keep it small, usually the user id (`sub`), maybe roles, and the standard claims like `exp`, `iat`, `iss` and `aud`.

## 11: Which package does Nest provide for working with JWTs?

`@nestjs/jwt`. It gives you `JwtModule` and `JwtService` with `sign`, `signAsync`, `verify`, `verifyAsync` and `decode`.

```ts
@Module({
  imports: [
    JwtModule.register({
      secret: process.env.JWT_SECRET,
      signOptions: { expiresIn: "15m" },
    }),
  ],
})
export class AuthModule {}
```

## 12: How do you sign a JWT when a user logs in?

After checking the password, build a payload and call `signAsync`.

```ts
async login(user: User) {
  const payload = { sub: user.id, role: user.role };
  return { access_token: await this.jwtService.signAsync(payload) };
}
```

## 13: What is the difference between jwtService.decode and jwtService.verify?

`decode` only reads the payload and does not check the signature or expiry, so it must never be used to trust a token. `verify` (and `verifyAsync`) checks the signature, the expiry and other options, and throws if anything is wrong.

## 14: Where should the client send the access token?

Usually in the `Authorization` header as `Bearer <token>`. Another common option is an httpOnly cookie. The header is simple for mobile apps and APIs used by other servers. Cookies are often better for browser apps because JavaScript can't read them, but then you need CSRF protection.

## 15: What does the exp claim do?

It's the expiry time as a Unix timestamp in seconds. After that time `verify` throws a `TokenExpiredError`. You set it with the `expiresIn` sign option, for example `'15m'` or `3600`.

## 16: Why should access tokens be short-lived?

A JWT is usually valid until it expires and the server doesn't keep track of it. If one gets stolen, the attacker can use it until `exp`. A short lifetime like 5 to 15 minutes limits the damage. A longer-lived refresh token is used to get new access tokens.

## 17: What is a refresh token?

A long-lived token that the client uses only to get a new access token when the old one expires. It is sent to one endpoint (like `POST /auth/refresh`), not with every request, so it is exposed less. The server should store it (or its hash) so it can revoke it.

## 18: What is the local strategy in Passport?

It's the username and password strategy from `passport-local`. You extend `PassportStrategy(Strategy)` and implement `validate`, which returns the user or throws.

```ts
@Injectable()
export class LocalStrategy extends PassportStrategy(Strategy) {
  constructor(private authService: AuthService) {
    super({ usernameField: "email" });
  }

  async validate(email: string, password: string) {
    const user = await this.authService.validateUser(email, password);
    if (!user) throw new UnauthorizedException();
    return user;
  }
}
```

## 19: What does the validate method in a Passport strategy return?

Whatever it returns is attached to the request as `req.user`. If it throws or returns a falsy value, Passport treats the authentication as failed and Nest responds with `401 Unauthorized`.

## 20: What is the JWT strategy in Passport?

It comes from `passport-jwt`. It reads the token from the request, checks the signature and expiry, and then calls your `validate` with the decoded payload.

```ts
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor(config: ConfigService) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      ignoreExpiration: false,
      secretOrKey: config.getOrThrow("JWT_SECRET"),
    });
  }

  validate(payload: { sub: string; role: string }) {
    return { id: payload.sub, role: payload.role };
  }
}
```

## 21: How do you protect a route with the Passport JWT strategy?

Use the built-in `AuthGuard` from `@nestjs/passport` with the strategy name.

```ts
@UseGuards(AuthGuard('jwt'))
@Get('me')
me(@Req() req) {
  return req.user;
}
```

## 22: Why should ignoreExpiration stay false?

If it's `true`, expired tokens are still accepted, so a stolen token works forever. It's sometimes set to `true` by mistake when copying examples or while debugging. Keep it `false` and let the client refresh.

## 23: What status code should you return for a missing or bad token?

`401 Unauthorized`. That means "we don't know who you are". Use `403 Forbidden` when the user is known but isn't allowed to do the action. Nest has `UnauthorizedException` and `ForbiddenException` for these.

## 24: How do you get the current user inside a controller?

Read `req.user`, or better, create a small custom decorator so controllers don't touch the raw request.

```ts
export const CurrentUser = createParamDecorator(
  (_data: unknown, ctx: ExecutionContext) => ctx.switchToHttp().getRequest().user,
);

@Get('me')
me(@CurrentUser() user: User) {
  return user;
}
```

## 25: What is a public route decorator and why do you need it?

When the auth guard is global, every route needs a token, including login and health checks. A `@Public()` decorator sets metadata, and the guard skips routes that have it.

```ts
export const IS_PUBLIC_KEY = "isPublic";
export const Public = () => SetMetadata(IS_PUBLIC_KEY, true);
```

## 26: What is the Reflector used for in guards?

`Reflector` reads metadata set by decorators like `@SetMetadata()` or `@Roles()`. A guard uses it to find out, for example, which roles a route needs or whether it's public. `getAllAndOverride` checks the handler first and then the class.

```ts
const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
  context.getHandler(),
  context.getClass(),
]);
```

## 27: What is RBAC?

Role-based access control. Users get roles like `admin`, `editor` or `viewer`, and routes say which roles they allow. It's simple and fits most apps where permissions don't depend on the data itself.

## 28: How do you build a Roles decorator in modern Nest?

Use `Reflector.createDecorator`, which gives you a typed decorator and a typed key in one line.

```ts
export const Roles = Reflector.createDecorator<string[]>();

@Roles(['admin'])
@Delete(':id')
remove(@Param('id') id: string) {}
```

## 29: How does a roles guard work?

It reads the required roles from metadata, reads the user from the request, and checks if the user has at least one of them.

```ts
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const roles = this.reflector.getAllAndOverride(Roles, [
      context.getHandler(),
      context.getClass(),
    ]);
    if (!roles) return true;
    const { user } = context.switchToHttp().getRequest();
    return roles.some((r) => user?.roles?.includes(r));
  }
}
```

## 30: What is ABAC?

Attribute-based access control. The decision depends on attributes of the user, the resource and sometimes the environment, for example "a user can edit an article if they are its author and it isn't published yet". It's more flexible than RBAC but harder to manage.

## 31: What is CASL?

CASL is a JavaScript library for permissions. You describe what a user can do with rules like `can('update', 'Article', { authorId: user.id })`, and then check with `ability.can('update', article)`. The Nest docs show how to use it with guards for ABAC-style rules.

## 32: What is the ValidationPipe?

A built-in pipe that validates incoming data against DTO classes using `class-validator` decorators. If validation fails, it throws a `400 Bad Request` with the error messages. It's usually turned on globally.

```ts
app.useGlobalPipes(new ValidationPipe({ whitelist: true }));
```

## 33: Why does input validation matter for security?

Most attacks start with unexpected input: wrong types, extra fields, very long strings, or objects where a string was expected. Validating type, length, format and allowed fields at the edge stops many injection, mass assignment and DoS problems before the data reaches services or the database.

## 34: What is a DTO?

A data transfer object is a class that describes the shape of data coming into (or going out of) an endpoint. With `class-validator` decorators it also describes the rules.

```ts
export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(12)
  @MaxLength(128)
  password: string;
}
```

## 35: What does the whitelist option of ValidationPipe do?

It strips any property that has no validation decorator in the DTO. So if a client sends `{ "email": "...", "isAdmin": true }` and the DTO has no `isAdmin`, that field is removed before your handler sees it.

## 36: What does forbidNonWhitelisted do?

Instead of silently removing unknown properties, it rejects the request with a `400` error. It only works together with `whitelist: true`. It's useful when you want clients to know they sent something wrong.

## 37: What is mass assignment?

It's when a client sets fields it shouldn't, like `role` or `isVerified`, because the server copies the whole body into a database entity. In Nest you prevent it with `whitelist: true`, separate DTOs for create and update, and by not passing request bodies straight into `repository.save()`.

## 38: What does the transform option of ValidationPipe do?

It turns the plain body object into an instance of the DTO class and converts primitive params, so `@Param('id') id: number` really becomes a number. It doesn't by itself make things safer, but it means the types in your code match what you actually got.

## 39: Which built-in pipes help validate route params?

`ParseIntPipe`, `ParseFloatPipe`, `ParseBoolPipe`, `ParseUUIDPipe`, `ParseEnumPipe`, `ParseArrayPipe` and `ParseDatePipe`. They throw a `400` if the value can't be parsed.

```ts
@Get(':id')
findOne(@Param('id', ParseUUIDPipe) id: string) {}
```

## 40: How do you validate nested objects?

Use `@ValidateNested()` together with `@Type()` from `class-transformer`. Without `@Type()`, the nested value stays a plain object and its rules are not checked.

```ts
export class OrderDto {
  @ValidateNested({ each: true })
  @Type(() => ItemDto)
  @ArrayMaxSize(100)
  items: ItemDto[];
}
```

## 41: What is serialization in NestJS?

It's the step where your return value is turned into the response body. Nest gives you `ClassSerializerInterceptor`, which uses `class-transformer` so you can hide or rename fields with decorators. It's the main way to make sure things like password hashes never leave the server.

## 42: How do you hide a field like password from responses?

Mark it with `@Exclude()` and use `ClassSerializerInterceptor`.

```ts
export class UserEntity {
  id: string;
  email: string;

  @Exclude()
  password: string;

  constructor(partial: Partial<UserEntity>) {
    Object.assign(this, partial);
  }
}
```

```ts
@UseInterceptors(ClassSerializerInterceptor)
@Get(':id')
async findOne(@Param('id') id: string) {
  return new UserEntity(await this.usersService.findOne(id));
}
```

## 43: Why doesn't @Exclude work when you return a plain object?

`ClassSerializerInterceptor` uses `instanceToPlain`, which only knows about decorators on class instances. A plain object from Prisma or a raw query has no class, so nothing is excluded. You must wrap the data in the class, or select only the fields you need from the database.

## 44: What is Helmet?

Helmet is middleware that sets security-related HTTP headers, like `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options` and `X-Frame-Options`. It removes `X-Powered-By` too.

```ts
import helmet from "helmet";

app.use(helmet());
```

## 45: Why should you call app.use(helmet()) before other routes are set up?

Middleware applies only to routes registered after it. If you call `app.use(helmet())` after something like a static assets route is set up, that route won't get the headers. Put it near the top of `bootstrap()`.

## 46: What is CORS?

Cross-Origin Resource Sharing is a browser rule. By default a page on `https://a.com` can't read responses from `https://api.b.com`. The server can allow it by sending headers like `Access-Control-Allow-Origin`. CORS only affects browsers; it doesn't stop curl or other servers.

## 47: How do you enable CORS in Nest?

Call `app.enableCors()` with options, or pass `cors` to `NestFactory.create`.

```ts
app.enableCors({
  origin: ["https://app.example.com"],
  credentials: true,
});
```

## 48: Is CORS a security feature that protects your API?

Not really. It protects users of browsers from other sites reading your API responses with their cookies. It doesn't stop anyone from calling your API directly. You still need authentication and authorization on every route.

## 49: What is CSRF?

Cross-site request forgery. A malicious site makes the user's browser send a request to your site, and the browser attaches your site's cookies automatically. If your API trusts cookies alone, the request runs as the user. It matters when you use cookie-based auth.

## 50: Do you need CSRF protection if you use Bearer tokens in headers?

Usually no. The browser doesn't add `Authorization` headers on its own, so a forged cross-site request won't carry the token. CSRF is a problem when auth is based on cookies, which the browser sends automatically.

## 51: Which package should you use for CSRF protection in a Nest app on Express?

The old `csurf` package is deprecated, so don't use it. The Nest docs now point to `csrf-csrf`, which uses the double submit cookie pattern. On Fastify, use `@fastify/csrf-protection`.

## 52: What is rate limiting?

Limiting how many requests a client can make in a time window, for example 100 requests per minute per IP. It slows down brute-force login attempts, credential stuffing, scraping and simple DoS attacks.

## 53: How do you add rate limiting to a Nest app?

Install `@nestjs/throttler`, configure `ThrottlerModule`, and register `ThrottlerGuard` globally. The `ttl` is in milliseconds.

```ts
@Module({
  imports: [ThrottlerModule.forRoot([{ ttl: 60_000, limit: 100 }])],
  providers: [{ provide: APP_GUARD, useClass: ThrottlerGuard }],
})
export class AppModule {}
```

## 54: How do you change the rate limit for one route?

Use `@Throttle()` with the throttler name and new values. Use `@SkipThrottle()` to turn it off for a route or controller.

```ts
@Throttle({ default: { limit: 5, ttl: 60_000 } })
@Post('login')
login(@Body() dto: LoginDto) {}

@SkipThrottle()
@Get('health')
health() {}
```

## 55: What status code does the throttler return when the limit is reached?

`429 Too Many Requests`. It also sends headers that tell the client the limit, how many requests are left and when it resets, so well-behaved clients can slow down.

## 56: Why must you never store passwords in plain text?

If the database leaks, every account is taken over right away, and because people reuse passwords, their accounts on other sites too. You store a slow, salted hash instead, so the original password can't be read back.

## 57: Why not use SHA-256 to hash passwords?

SHA-256 is fast on purpose. Attackers with GPUs can try billions of guesses per second against a leaked hash. Password hashing needs a slow algorithm with a work factor, like Argon2id, bcrypt or scrypt.

## 58: How do you hash and check a password with bcrypt?

```ts
import * as bcrypt from "bcrypt";

const hash = await bcrypt.hash(password, 12);
const ok = await bcrypt.compare(password, hash);
```

The second argument to `hash` is the cost factor. Each step up doubles the work. 10 to 12 is common today.

## 59: How do you hash and check a password with argon2?

```ts
import * as argon2 from "argon2";

const hash = await argon2.hash(password); // argon2id by default
const ok = await argon2.verify(hash, password);
```

The `argon2` package uses Argon2id by default, which is what OWASP recommends first.

## 60: What is a salt?

A random value added to each password before hashing, so two users with the same password get different hashes. It stops attackers from using precomputed tables. bcrypt and argon2 create the salt for you and store it inside the hash string.

## 61: What is a pepper?

A secret value added to passwords before hashing that is stored outside the database, for example in a secrets manager. If only the database leaks, the hashes can't be cracked without the pepper. It's optional and adds key management work.

## 62: What is an API key?

A long random string that identifies a client application, usually sent in a header like `x-api-key`. It's simpler than OAuth and fits server-to-server calls. It doesn't identify a person and is often long-lived, so it needs to be stored and rotated carefully.

## 63: How would you check an API key in Nest?

With a guard that reads the header and compares it to stored keys.

```ts
@Injectable()
export class ApiKeyGuard implements CanActivate {
  constructor(private keys: ApiKeysService) {}

  async canActivate(ctx: ExecutionContext) {
    const req = ctx.switchToHttp().getRequest();
    const key = req.headers["x-api-key"];
    if (typeof key !== "string") throw new UnauthorizedException();
    req.client = await this.keys.findValid(key);
    if (!req.client) throw new UnauthorizedException();
    return true;
  }
}
```

## 64: What is OAuth 2.0?

A standard that lets a user give an app limited access to their data on another service without sharing their password. For example, your app can read a user's Google calendar after the user agrees on Google's page. OAuth itself is about access (authorization), not login.

## 65: What is OpenID Connect?

OIDC is a layer on top of OAuth 2.0 that adds login. Besides the access token you get an ID token, a JWT that tells you who the user is. "Sign in with Google" or Microsoft Entra ID login use OIDC.

## 66: What is SSO?

Single sign-on means a user logs in once with an identity provider (like Okta, Entra ID or Keycloak) and then can use many apps without logging in again. The apps trust the identity provider through OIDC or SAML.

## 67: Which Passport strategy would you use for Google login?

`passport-google-oauth20`. You give it your client ID, client secret and callback URL, and its `validate` gets the user profile, where you find or create the local user.

## 68: What is the ConfigModule?

`@nestjs/config` loads environment variables (from the process and from `.env` files) and gives you `ConfigService` to read them. It's the standard place to keep secrets like database passwords and JWT keys out of the code.

```ts
ConfigModule.forRoot({ isGlobal: true });
```

## 69: Why shouldn't you commit the .env file?

It usually contains real secrets. Anything pushed to git stays in the history even after you delete it, and bots scan public repos for keys within minutes. Commit a `.env.example` with fake values and add `.env` to `.gitignore`.

## 70: What does ConfigService.getOrThrow do?

It returns the value or throws if the variable is missing. That makes the app fail at startup instead of running with `undefined` as a JWT secret, which is a real bug people ship.

```ts
const secret = config.getOrThrow<string>("JWT_SECRET");
```

## 71: Why validate environment variables at startup?

If a secret is missing, too short or has a typo, you want the app to refuse to start, not to fail later in a strange way or run with an unsafe default. `ConfigModule.forRoot` accepts a `validationSchema` (Joi) or a `validate` function for this.

## 72: What is HTTPS and why is it needed?

HTTPS is HTTP over TLS. It encrypts traffic between the client and server and proves the server's identity with a certificate. Without it, anyone on the network can read or change tokens, cookies and passwords.

## 73: Where is TLS usually terminated for a Nest app?

Most often at a load balancer, reverse proxy or ingress (like Nginx, AWS ALB or Cloudflare). The proxy handles certificates and talks to Nest over plain HTTP in a private network, or over TLS again if the network isn't trusted.

## 74: What is HSTS?

HTTP Strict Transport Security is a header that tells browsers to only use HTTPS for your domain for a set time. It stops downgrade attacks where someone forces the first request to plain HTTP. Helmet sets it by default.

## 75: What is encryption at rest?

Encrypting data stored on disk: databases, backups, file storage. Cloud databases and S3 can do this with a switch. For very sensitive fields you can also encrypt in the app before saving, so even someone with database access can't read them.

## 76: What is SQL injection?

When user input is put into a SQL string and changes the meaning of the query. For example `"... WHERE email = '" + email + "'"` with `email = "' OR 1=1 --"` returns all users. The fix is parameterized queries, which every major ORM supports.

## 77: How does TypeORM protect you from SQL injection?

Methods like `find`, `findOneBy` and `save` use parameters for values. In the query builder you must use named parameters instead of string concatenation.

```ts
// safe
qb.where("user.email = :email", { email });

// unsafe
qb.where(`user.email = '${email}'`);
```

## 78: Is Prisma safe from SQL injection?

The normal client methods (`findMany`, `create` and so on) are. `$queryRaw` used as a tagged template is also safe because values become parameters. `$queryRawUnsafe` and `$executeRawUnsafe` take plain strings and are dangerous with user input.

## 79: What is NoSQL injection?

Sending query operators instead of plain values. For example, a login body `{ "email": "a@b.com", "password": { "$ne": null } }` sent to MongoDB can match any password if the code passes it straight into a filter. Validating that fields are strings stops it.

## 80: How does class-validator help against NoSQL injection?

`@IsString()` rejects objects, so `{ "$ne": null }` fails validation before it reaches Mongoose. Combined with `whitelist: true`, unknown keys are removed too.

## 81: What is XSS?

Cross-site scripting. An attacker gets their script to run in another user's browser, usually by saving something like `<script>` in a comment that is later shown without escaping. The script can then steal data or act as the user.

## 82: Is a JSON API safe from XSS?

Mostly the risk moves to the frontend, which must escape data when it renders it. The API should still send `Content-Type: application/json`, set `X-Content-Type-Options: nosniff`, and never reflect user input in HTML responses. If you store rich text, sanitize it on the server.

## 83: What is output encoding?

Escaping data for the place where it's displayed. In HTML, `<` becomes `&lt;`. In a URL, special characters are percent-encoded. Template engines like Handlebars escape by default with `{{ }}`; triple braces `{{{ }}}` don't escape and are risky.

## 84: How do you accept a file upload in Nest?

Use `FileInterceptor` (based on Multer) and `@UploadedFile()`.

```ts
@Post('avatar')
@UseInterceptors(FileInterceptor('file', { limits: { fileSize: 2 * 1024 * 1024 } }))
upload(@UploadedFile() file: Express.Multer.File) {
  return { size: file.size };
}
```

## 85: Why set a file size limit on uploads?

Without a limit, someone can upload huge files to fill your disk or memory and crash the server. Multer's `limits.fileSize` stops reading the stream once the size is passed.

## 86: How do you validate an uploaded file's size and type?

Use `ParseFilePipe` with the built-in validators.

```ts
@UploadedFile(
  new ParseFilePipe({
    validators: [
      new MaxFileSizeValidator({ maxSize: 2 * 1024 * 1024 }),
      new FileTypeValidator({ fileType: /^image\/(png|jpeg)$/ }),
    ],
  }),
)
file: Express.Multer.File
```

## 87: Can you trust the file name the client sends?

No. It can contain `../` to escape a folder, very long names, or odd characters. Generate your own file name (like a UUID) and keep the original name only as data, after cleaning it.

## 88: What is an exception filter?

A class that catches errors and builds the response. Nest has a built-in global filter. You write your own with `@Catch()` to change the response format, add logging, or map database errors to HTTP errors.

## 89: What does Nest return for an unknown error by default?

For anything that isn't an `HttpException`, the built-in filter returns:

```json
{ "statusCode": 500, "message": "Internal server error" }
```

It doesn't include the stack trace or the original message, which is good. The risk comes when you write your own filter that sends `exception.message` to the client.

## 90: Why is error leakage a security problem?

Stack traces, SQL errors and file paths tell attackers which libraries, versions, table names and code paths you use. That makes other attacks easier. Show a generic message to the client and log the details on the server.

## 91: What should a security log contain?

Who did what, when and from where: user id, action, resource, result (allowed or denied), timestamp, IP and a request id. Log failed logins, permission denials, password changes and admin actions. Never log passwords, tokens or full card numbers.

## 92: Which logger is common in production Nest apps?

`nestjs-pino` (using Pino) is very common because it's fast and logs JSON. It has a `redact` option to hide fields like the `Authorization` header. The built-in `ConsoleLogger` also supports JSON output in recent versions.

## 93: What is audit logging?

A record of important actions kept for later review, for example "admin X changed user Y's role at time Z". Audit logs should be append-only, kept longer than normal logs, and hard for app users (even admins) to change.

## 94: How do you protect a WebSocket gateway in Nest?

Guards work on gateway message handlers with `@UseGuards()`, the same as on controllers. Inside the guard you use `context.switchToWs()` to get the client and the data. You also need to check the user at connection time, because guards don't run on the connection itself.

## 95: What is WsException?

The exception class from `@nestjs/websockets` for gateway errors. When you throw it, Nest sends an `exception` event to the client instead of an HTTP response.

```ts
throw new WsException("Not allowed");
```

## 96: How do you get the request inside a GraphQL guard?

GraphQL uses a different context, so use `GqlExecutionContext`.

```ts
@Injectable()
export class GqlAuthGuard extends AuthGuard("jwt") {
  getRequest(context: ExecutionContext) {
    return GqlExecutionContext.create(context).getContext().req;
  }
}
```

## 97: What is a query depth limit in GraphQL?

A rule that rejects queries nested deeper than a set number of levels. Without it, a client can send a query like `user { friends { friends { friends ... } } }` that makes the server do a huge amount of work.

## 98: Should GraphQL introspection be on in production?

Usually not for private APIs. Introspection lets anyone download your whole schema, which makes it easier to find weak spots. Turn it off with `introspection: false` in production, while keeping it on in development. For a public API it can be fine.

## 99: What is mTLS?

Mutual TLS. In normal TLS only the server shows a certificate. In mTLS the client shows one too, so both sides prove who they are. It's common between microservices and is often handled by a service mesh like Istio or Linkerd.

## 100: How can microservices in Nest authenticate each other?

With TLS or mTLS on the transport, with credentials in the broker (RabbitMQ user and password, Kafka SASL), or by passing a signed token in the message metadata. Many teams use more than one of these.

## 101: What is multi-tenancy?

One app serving many customers (tenants), where each tenant's data must stay separate. The main security risk is a bug that lets tenant A see tenant B's data.

## 102: What are the common ways to store data for many tenants?

A separate database per tenant, a separate schema per tenant, or one shared schema with a `tenant_id` column on every table. Separate databases give the strongest isolation but cost more. A shared schema is cheapest but every query must filter by tenant.

## 103: What does the httpOnly cookie flag do?

It stops JavaScript from reading the cookie through `document.cookie`. So if an XSS bug happens, the script can't steal the session or refresh token directly.

## 104: What does the Secure cookie flag do?

The browser only sends the cookie over HTTPS. That stops it from leaking over plain HTTP.

## 105: What does the SameSite cookie attribute do?

It controls whether the browser sends the cookie on cross-site requests. `Strict` never sends it cross-site, `Lax` sends it only on top-level GET navigations, and `None` always sends it (and requires `Secure`). `Lax` or `Strict` blocks most CSRF attacks.

## 106: How do you set a secure cookie in a Nest controller?

Use the response object with `passthrough: true` so Nest still sends your return value.

```ts
@Post('login')
async login(@Body() dto: LoginDto, @Res({ passthrough: true }) res: Response) {
  const { accessToken, refreshToken } = await this.auth.login(dto);
  res.cookie('refresh_token', refreshToken, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    path: '/auth/refresh',
    maxAge: 7 * 24 * 60 * 60 * 1000,
  });
  return { accessToken };
}
```

## 107: How do you read cookies in Nest with Express?

Install `cookie-parser` and register it. Then cookies are in `req.cookies`.

```ts
import cookieParser from "cookie-parser";

app.use(cookieParser());
```

## 108: What is a request size limit?

The largest request body the server will accept. Express's JSON parser in Nest has a default limit of 100 KB. Big or unlimited bodies let attackers use up memory and CPU with a few requests.

## 109: What is a DoS attack?

Denial of service: making an app unavailable to real users by overloading it, for example with many requests, huge payloads or expensive queries. In the app you defend with rate limits, size limits, timeouts and query limits. Big network attacks (DDoS) are handled in front of the app by a CDN or cloud provider.

## 110: What does npm audit do?

It checks your installed packages against a database of known vulnerabilities and lists which ones are affected and how serious they are. `npm audit fix` updates packages within the allowed version ranges.

## 111: What is Snyk?

A commercial tool (with a free tier) that scans dependencies, code, containers and infrastructure files for known vulnerabilities. It can run in CI and open pull requests with fixes. Dependabot and Renovate do similar things for dependency updates.

## 112: What is a supply-chain attack?

An attack through the code you depend on, not your own code. For example a popular npm package gets hijacked and a new version steals tokens during install. In 2025 several widely used npm packages were taken over this way, so this risk is very real.

## 113: Why should you commit the lockfile?

It pins the exact version of every package, including nested ones. Without it, a fresh install can pull a new, possibly malicious, version. In CI use `npm ci`, which installs exactly what the lockfile says and fails if it doesn't match `package.json`.

## 114: What is the OWASP Top 10?

A list from OWASP of the ten most common and serious web app security risks, such as broken access control, injection and security misconfiguration. It's updated every few years and is a common checklist in interviews and security reviews.

## 115: Which item has been number one on the OWASP Top 10 recently?

Broken access control. It covers bugs like a user reading another user's data by changing an id in the URL, or calling admin endpoints without being an admin. In Nest that usually means missing guards or missing ownership checks.

## 116: What is IDOR?

Insecure direct object reference. The API trusts an id from the client without checking that the user owns that object. For example `GET /invoices/123` returns invoice 123 to anyone logged in. The fix is to always filter by the current user or check ownership.

## 117: How do you test that a route needs authentication?

Write an e2e test with `supertest` that calls it without a token and expects `401`.

```ts
it("rejects requests without a token", () => {
  return request(app.getHttpServer()).get("/users/me").expect(401);
});
```

## 118: What is a session in web authentication?

The server stores data about a logged-in user (in memory, Redis or a database) and gives the browser a cookie with a random session id. On each request the server looks up the session by that id. Logging out simply deletes the session.

## 119: How do sessions compare to JWTs?

Sessions are easy to revoke and keep little data on the client, but need shared storage when you have many servers. JWTs don't need a lookup on each request but are hard to revoke before they expire. For a browser-only app with one backend, sessions are often the simpler and safer choice.

## 120: Which package is used for sessions with Nest on Express?

`express-session`, usually with a store like `connect-redis`, because the default memory store leaks memory and isn't meant for production.

```ts
app.use(
  session({
    secret: config.getOrThrow("SESSION_SECRET"),
    resave: false,
    saveUninitialized: false,
    cookie: { httpOnly: true, secure: true, sameSite: "lax" },
  }),
);
```

## 121: Why set saveUninitialized to false?

It stops the server from creating and storing a session for every visitor who hasn't logged in. That saves storage, avoids setting cookies before consent, and makes it harder to fill your session store with junk.

## 122: What is brute force and how do you slow it down on login?

Trying many passwords until one works. Use a strict rate limit on the login route, limit attempts per account (not just per IP), add growing delays or a CAPTCHA after failures, and require strong passwords or MFA.

## 123: What is credential stuffing?

Using username and password pairs leaked from other sites to log in, because people reuse passwords. Defenses are rate limits, checking passwords against known breach lists (like Have I Been Pwned), MFA and alerts on unusual logins.

## 124: What is MFA?

Multi-factor authentication: the user needs something beyond the password, like a TOTP code from an app, a passkey or a hardware key. SMS codes are better than nothing but weaker. MFA blocks most attacks based on stolen passwords.

## 125: What is a passkey?

A login method based on WebAuthn. The device keeps a private key, and the server stores only the public key. Login is a signature check, so there's no password to phish or leak. In Node, `@simplewebauthn/server` is a common library for it.

## 126: Why should login error messages be vague?

If "user not found" and "wrong password" are different messages, an attacker can find out which emails have accounts. Use one message like "Invalid email or password" for both.

## 127: What should the password reset flow look like?

The user enters an email, and you always reply "if the account exists, we sent a link". The link has a random, single-use token that expires soon (for example 30 minutes). Store only a hash of the token. After a reset, end the user's other sessions and refresh tokens.

## 128: What is the difference between encoding, hashing and encryption?

Encoding (like base64) changes the format and anyone can reverse it. Hashing is one-way and is used for passwords and checks. Encryption is two-way but needs a key to reverse. A common mistake is thinking base64 or a JWT payload hides data.

## 129: What does X-Content-Type-Options: nosniff do?

It tells the browser not to guess the content type and to trust the `Content-Type` header. Without it, a browser might treat an uploaded text file as HTML or script. Helmet sets it by default.

## 130: What does Content-Security-Policy do?

It tells the browser where scripts, styles, images and other resources may load from. A good CSP makes XSS much harder because injected inline scripts won't run. Helmet sets a default CSP that you can change.

## 131: Why remove the X-Powered-By header?

Express sends `X-Powered-By: Express`, which tells attackers what you run. It's a small thing but free to fix. Helmet removes it, or you can call `app.disable('x-powered-by')` on the Express instance.

## 132: How do you get the Express-specific app type in Nest?

Pass the type to `NestFactory.create`. Then you can use Express methods like `set` and `disable`.

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.set("trust proxy", 1);
```

## 133: What does trust proxy do?

When your app is behind a load balancer, `req.ip` is the proxy's IP. With `trust proxy` set, Express reads the real client IP from `X-Forwarded-For`. Rate limiting and logs depend on the correct IP, so this setting matters.

## 134: What is the principle of least privilege?

Give every user, service and database account only the access it really needs. For example, the app's database user shouldn't be able to drop tables, and a reporting service should get a read-only account.

## 135: What is defense in depth?

Having several layers of protection so one mistake doesn't expose everything. For example validation in DTOs plus parameterized queries plus a limited database user plus a WAF. If one layer fails, the others still help.

## 136: What is secure by default in the context of guards?

Make every route protected unless someone explicitly marks it as public. With a global auth guard and a `@Public()` decorator, a developer who forgets a decorator gets a locked route, not an open one.

## 137: What is session fixation?

The attacker gives the victim a session id they know, the victim logs in with it, and now the attacker shares the session. The fix is to create a new session id at login with `req.session.regenerate()`.

## 138: What is clickjacking?

Loading your site inside an invisible iframe on another site so the user clicks buttons without knowing. You stop it with `X-Frame-Options: DENY` or the CSP `frame-ancestors 'none'` directive. Helmet sets these.

## 139: Why is the default JwtModule secret a problem if it's hard-coded?

If the secret is in the code, everyone with repo access (and anyone who ever sees the repo) can create valid tokens for any user. Read it from config or a secrets manager, and use a long random value.

## 140: How long should a JWT HMAC secret be?

At least 256 bits (32 random bytes) for HS256. Generate it with a secure random source, for example `node -e "console.log(require('crypto').randomBytes(32).toString('base64'))"`. Short or dictionary secrets can be cracked offline from a single token.

## 141: What does the crypto module in Node give you for security work?

Secure random values (`randomBytes`, `randomUUID`), hashing and HMAC (`createHash`, `createHmac`), encryption (`createCipheriv`), key derivation (`scrypt`, `pbkdf2`) and safe compare (`timingSafeEqual`). You rarely need an extra library for basics.

## 142: Why use crypto.randomBytes instead of Math.random for tokens?

`Math.random` isn't cryptographically secure, and its output can be predicted. Tokens for sessions, password resets and API keys must come from `crypto.randomBytes` or `crypto.randomUUID`.

## 143: What is the difference between a 401 and a 403 when using guards?

If a guard returns `false`, Nest throws `ForbiddenException` (403). To return 401, throw `UnauthorizedException` yourself. The auth guard should throw 401 for missing or bad tokens, and the roles guard should return 403.

## 144: What is a security header you might add that Helmet doesn't set by default?

`Permissions-Policy`, which turns off browser features like camera, microphone or geolocation for your pages. You can add it with a small middleware. For a JSON API, `Cache-Control: no-store` on sensitive responses is also worth adding.

## 145: What is a WAF?

A web application firewall sits in front of the app and blocks common attack patterns, like obvious SQL injection strings or known bad bots. Cloudflare, AWS WAF and similar services provide one. It helps, but it doesn't replace secure code.

## 146: Why disable stack traces in production logs sent to clients but keep them in server logs?

Clients and attackers shouldn't see internals, but developers need them to fix bugs. So the response gets a short message and a request id, and the server log keeps the full stack trace linked by the same id.

## 147: What is a CVE?

A Common Vulnerabilities and Exposures id, like `CVE-2024-12345`, is a public id for a known security bug. `npm audit`, Snyk and GitHub advisories refer to CVEs so you can look up details.

## 148: What is a security.txt file?

A file at `/.well-known/security.txt` that tells security researchers how to report bugs to you. It's simple to serve from Nest or a static host and shows you take reports seriously.

## 149: Why should you keep Nest and Node.js up to date?

Security fixes land in new versions, and old major versions stop getting them. Node.js versions reach end of life on a fixed schedule. Running an unsupported Node or Nest version means known bugs stay open.

## 150: What is the first thing you check in a NestJS security review?

Whether every route is protected as it should be: is there a global auth guard, which routes are public, and do the routes that load data by id check that the user owns it. Broken access control is the most common serious bug, so it's the best place to start.

# Moderate Questions (151-300)

## 151: How do you write a JWT auth guard without Passport?

Read the Bearer token, verify it with `JwtService`, and put the payload on the request.

```ts
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(
    private jwt: JwtService,
    private reflector: Reflector,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
      context.getHandler(),
      context.getClass(),
    ]);
    if (isPublic) return true;

    const req = context.switchToHttp().getRequest();
    const [type, token] = req.headers.authorization?.split(" ") ?? [];
    if (type !== "Bearer" || !token) throw new UnauthorizedException();

    try {
      req.user = await this.jwt.verifyAsync(token);
    } catch {
      throw new UnauthorizedException();
    }
    return true;
  }
}
```

## 152: How do you make the Passport JWT guard respect a Public decorator?

Extend `AuthGuard('jwt')` and check the metadata before calling `super.canActivate`.

```ts
@Injectable()
export class JwtAuthGuard extends AuthGuard("jwt") {
  constructor(private reflector: Reflector) {
    super();
  }

  canActivate(context: ExecutionContext) {
    const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
      context.getHandler(),
      context.getClass(),
    ]);
    return isPublic ? true : super.canActivate(context);
  }
}
```

## 153: How do you configure JwtModule with ConfigService?

Use `registerAsync` so the secret comes from config at startup.

```ts
JwtModule.registerAsync({
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    secret: config.getOrThrow("JWT_ACCESS_SECRET"),
    signOptions: {
      expiresIn: "15m",
      issuer: "api.example.com",
      audience: "web",
    },
    verifyOptions: {
      algorithms: ["HS256"],
      issuer: "api.example.com",
      audience: "web",
    },
  }),
});
```

## 154: Why should you check iss and aud claims?

If several services share a signing key or trust the same identity provider, a token made for service A could be replayed against service B. Checking `iss` (who issued it) and `aud` (who it's for) makes sure the token was meant for your API.

## 155: Why should you set the algorithms option when verifying JWTs?

Without it, some libraries trust the `alg` from the token header. That led to attacks with `alg: none` and with switching RS256 to HS256 and using the public key as the HMAC secret. Always pin the algorithm list on verify, for example `algorithms: ['RS256']`.

## 156: When would you choose RS256 over HS256?

HS256 uses one shared secret for signing and verifying, so every service that verifies tokens can also create them. RS256 (or ES256) signs with a private key and verifies with a public key, so only the auth service can create tokens. Use asymmetric keys when more than one service checks tokens.

## 157: How do you sign tokens with RS256 in Nest?

Give `JwtModule` a private key for signing and a public key for verifying.

```ts
JwtModule.register({
  privateKey: fs.readFileSync("keys/private.pem"),
  publicKey: fs.readFileSync("keys/public.pem"),
  signOptions: { algorithm: "RS256", expiresIn: "15m", keyid: "2026-11" },
  verifyOptions: { algorithms: ["RS256"] },
});
```

## 158: How do you use different secrets for access and refresh tokens?

Pass the secret in the call instead of using only the module default.

```ts
const accessToken = await this.jwt.signAsync(payload, {
  secret: this.config.getOrThrow("JWT_ACCESS_SECRET"),
  expiresIn: "15m",
});
const refreshToken = await this.jwt.signAsync(
  { sub: user.id, jti: randomUUID() },
  { secret: this.config.getOrThrow("JWT_REFRESH_SECRET"), expiresIn: "7d" },
);
```

Different secrets mean a refresh token can't be used as an access token.

## 159: How do you store refresh tokens on the server?

Store a hash of the token (or its `jti`), the user id, expiry, device info and a revoked flag in a table or Redis. Never store the raw token. On refresh, look it up by `jti`, compare the hash, and check it isn't revoked or expired.

## 160: What is refresh token rotation?

Each time a refresh token is used, the server issues a new refresh token and marks the old one as used. A refresh token is only good once. If a stolen token is used, either the attacker or the real user will later present an already used token, and you can detect that.

## 161: What is refresh token reuse detection?

If a refresh token that was already rotated is used again, something is wrong: two parties have it. The safe response is to revoke the whole token family (every token issued from the same login) and make the user log in again.

## 162: How would you write a refresh endpoint?

```ts
@Public()
@Post('refresh')
async refresh(@Req() req: Request, @Res({ passthrough: true }) res: Response) {
  const token = req.cookies['refresh_token'];
  if (!token) throw new UnauthorizedException();
  const { accessToken, refreshToken } = await this.auth.rotate(token);
  res.cookie('refresh_token', refreshToken, refreshCookieOptions);
  return { accessToken };
}
```

`rotate` verifies the token, checks the stored record, marks it used, and issues a new pair. If the record is already used, it revokes the family and throws.

## 163: How do you log a user out when you use JWTs?

Delete or revoke the refresh token on the server and clear the cookie. The access token stays valid until it expires, which is why it should be short. If you need instant logout, keep a denylist of access token ids (`jti`) in Redis until they expire.

## 164: How do you revoke all tokens for a user, for example after a password change?

Store a `tokenVersion` (or `passwordChangedAt`) on the user and put it in the token. In the guard or strategy `validate`, load it and reject tokens with an older version. That costs one lookup per request, so many teams cache it in Redis.

## 165: Where should a browser app keep the access token?

A common setup is: access token in memory (a JavaScript variable), refresh token in an httpOnly, Secure, SameSite cookie scoped to the refresh path. `localStorage` is readable by any script on the page, so an XSS bug can steal tokens from it.

## 166: How do you set up Passport sessions in Nest?

Enable sessions in the module, add a serializer, and log the user in from the guard.

```ts
@Injectable()
export class SessionSerializer extends PassportSerializer {
  serializeUser(user: User, done: Function) {
    done(null, user.id);
  }
  async deserializeUser(id: string, done: Function) {
    done(null, await this.users.findById(id));
  }
}

@Injectable()
export class LocalAuthGuard extends AuthGuard("local") {
  async canActivate(context: ExecutionContext) {
    const ok = (await super.canActivate(context)) as boolean;
    await super.logIn(context.switchToHttp().getRequest());
    return ok;
  }
}
```

In `main.ts` add `express-session`, then `passport.initialize()` and `passport.session()`.

## 167: Why serialize only the user id into the session?

The session store then holds a small value, and every request loads fresh user data, so role changes or bans apply at once. If you store the whole user, an old role can stay in the session until it expires.

## 168: How do you use Redis as a session store?

```ts
import { RedisStore } from "connect-redis";
import { createClient } from "redis";

const client = createClient({ url: process.env.REDIS_URL });
await client.connect();

app.use(
  session({
    store: new RedisStore({ client, prefix: "sess:" }),
    secret: config.getOrThrow("SESSION_SECRET"),
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: true,
      sameSite: "lax",
      maxAge: 86_400_000,
    },
  }),
);
```

## 169: How do you regenerate the session id at login?

Call `req.session.regenerate` before saving the user in it. With Passport 0.6 and later, `req.logIn` does this for you.

```ts
await new Promise<void>((resolve, reject) =>
  req.session.regenerate((err) => (err ? reject(err) : resolve())),
);
req.session.userId = user.id;
```

## 170: How do you combine an auth guard and a roles guard globally?

Register both with `APP_GUARD`. They run in the order they are registered, so the auth guard must come first and set `req.user`.

```ts
providers: [
  { provide: APP_GUARD, useClass: JwtAuthGuard },
  { provide: APP_GUARD, useClass: RolesGuard },
],
```

## 171: Why should roles be checked against the database instead of only the token?

Roles in a token are fixed until it expires. If you remove someone's admin role, they keep it for up to the token lifetime. For short-lived tokens that's often fine. For sensitive actions, load the current roles from the database or a cache.

## 172: How do you define a CASL ability factory in Nest?

```ts
type Actions = "manage" | "create" | "read" | "update" | "delete";
type Subjects = InferSubjects<typeof Article | typeof User> | "all";
export type AppAbility = MongoAbility<[Actions, Subjects]>;

@Injectable()
export class CaslAbilityFactory {
  createForUser(user: User) {
    const { can, cannot, build } = new AbilityBuilder<AppAbility>(
      createMongoAbility,
    );

    if (user.isAdmin) {
      can("manage", "all");
    } else {
      can("read", Article, { isPublished: true });
      can("update", Article, { authorId: user.id });
      cannot("delete", Article, { isPublished: true });
    }

    return build({
      detectSubjectType: (item) =>
        item.constructor as ExtractSubjectType<Subjects>,
    });
  }
}
```

## 173: How do you check a CASL rule in a service?

Build the ability for the user, load the record, and check it.

```ts
async update(user: User, id: string, dto: UpdateArticleDto) {
  const article = await this.repo.findOneByOrFail({ id });
  const ability = this.abilities.createForUser(user);
  if (ability.cannot('update', article)) throw new ForbiddenException();
  return this.repo.save({ ...article, ...dto });
}
```

The check needs the real record, which is why ownership checks often live in services instead of guards.

## 174: What is a policies guard?

A pattern from the Nest docs. A `@CheckPolicies()` decorator attaches small handler functions to a route, and a guard builds the CASL ability and runs each handler. It works well for checks that don't need the actual record, like "can create Article".

```ts
@UseGuards(PoliciesGuard)
@CheckPolicies((ability: AppAbility) => ability.can('create', Article))
@Post()
create(@Body() dto: CreateArticleDto) {}
```

## 175: How do you limit which fields a user can update with CASL?

CASL supports field-level rules, and `permittedFieldsOf` returns the allowed fields.

```ts
can("update", User, ["name", "avatar"], { id: user.id });

const fields = permittedFieldsOf(ability, "update", userRecord, {
  fieldsFrom: (rule) => rule.fields ?? Object.keys(dto),
});
const safeDto = pick(dto, fields);
```

## 176: How do you fetch only records the user may read with CASL and Prisma?

Use `@casl/prisma`. `accessibleBy` turns the rules into a Prisma `where` filter, so the database only returns allowed rows.

```ts
const ability = createPrismaAbility([...rules]);
const posts = await prisma.post.findMany({
  where: accessibleBy(ability).Post,
});
```

## 177: What are good ValidationPipe options for a public API?

```ts
app.useGlobalPipes(
  new ValidationPipe({
    whitelist: true,
    forbidNonWhitelisted: true,
    transform: true,
    forbidUnknownValues: true,
    disableErrorMessages: process.env.NODE_ENV === "production",
  }),
);
```

`disableErrorMessages` is optional. Many teams keep messages because they help clients and don't leak much.

## 178: What does forbidUnknownValues do?

It makes validation fail when the object being checked isn't a known class instance, for example when a value that should be an object is something unexpected. It defaults to `true` in class-validator 0.14 and later because the old default let some bad input through without any checks.

## 179: Why is enableImplicitConversion risky?

With `transformOptions: { enableImplicitConversion: true }`, class-transformer converts values based on the TypeScript type. For example the string `"false"` turns into `true` for a `boolean` field because any non-empty string is truthy. Prefer explicit `@Type()` or `@Transform()` on fields that need conversion.

## 180: How do you validate query parameters safely?

Use a DTO for the query and keep `transform: true` so numbers become numbers. Put limits on everything that controls cost, like page size.

```ts
export class ListQueryDto {
  @Type(() => Number)
  @IsInt()
  @Min(1)
  @Max(100)
  limit = 20;

  @IsOptional()
  @IsIn(["createdAt", "name"])
  sort?: "createdAt" | "name";
}
```

## 181: Why should every string field have a max length?

Without it, a client can send megabytes in one field. That uses memory, slows down regex checks, fills the database and can break other systems. `@MaxLength()` on every string is a cheap rule that blocks a lot of abuse.

## 182: How can a regular expression in a DTO cause a DoS?

Some patterns with nested repetition, like `/^(a+)+$/`, take exponential time on certain inputs. This is called ReDoS. One request can block the Node event loop for seconds. Keep patterns simple, limit input length first, and test regexes with a tool like `safe-regex` or `recheck`.

## 183: How do you validate a DTO with different rules for create and update?

Use mapped types from `@nestjs/mapped-types` (or `@nestjs/swagger`) to derive the update DTO from the create DTO, and leave sensitive fields out of both.

```ts
export class UpdateUserDto extends PartialType(
  OmitType(CreateUserDto, ["email"] as const),
) {}
```

## 184: How do you use validation groups for different roles?

class-validator supports `groups`. You can pass groups to `ValidationPipe`, but the pipe's options are fixed when it's created, so per-user groups usually mean a custom pipe or separate DTOs. Many teams find separate DTOs (like `AdminUpdateUserDto`) easier to read.

## 185: How do you return a user without the password using @Exclude and groups?

Use `@Expose({ groups })` for fields only some users should see, and set groups with `@SerializeOptions`.

```ts
export class UserEntity {
  id: string;
  name: string;

  @Expose({ groups: ['admin'] })
  email: string;

  @Exclude()
  passwordHash: string;
}

@SerializeOptions({ groups: ['admin'] })
@Get('admin/users/:id')
findForAdmin() {}
```

## 186: What is the safest default for serialization?

An allowlist: only send fields you marked. Use `@SerializeOptions({ excludeExtraneousValues: true })` (or set it globally on the interceptor) and mark each public field with `@Expose()`. New database columns then stay hidden until someone exposes them on purpose.

## 187: How do you register ClassSerializerInterceptor globally?

```ts
app.useGlobalInterceptors(new ClassSerializerInterceptor(app.get(Reflector)));
```

Or register it with `APP_INTERCEPTOR` in a module.

## 188: How do you hide fields when you use Prisma?

Prisma returns plain objects, so `@Exclude` alone does nothing. Either use `select` or the `omit` option to leave the field out of the query, or map results into a class before returning them.

```ts
const user = await prisma.user.findUnique({
  where: { id },
  omit: { passwordHash: true },
});
```

## 189: How do you hide fields with Mongoose?

Set `select: false` on the schema field so it isn't returned unless you ask for it with `.select('+password')`. You can also use a `toJSON` transform to delete it.

```ts
@Prop({ required: true, select: false })
password: string;
```

## 190: How do you configure Helmet's CSP for an API with Swagger UI?

Swagger UI needs inline styles and scripts. Either relax the CSP only on the docs route or turn on the directives it needs. Many teams simply serve docs only outside production.

```ts
app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        imgSrc: ["'self'", "data:"],
      },
    },
  }),
);
```

## 191: How do you use Helmet with the Fastify adapter?

Use `@fastify/helmet` and register it as a Fastify plugin.

```ts
import helmet from "@fastify/helmet";

const app = await NestFactory.create<NestFastifyApplication>(
  AppModule,
  new FastifyAdapter(),
);
await app.register(helmet);
```

## 192: Why does Helmet's CSP break the GraphQL playground or Apollo Sandbox?

Those tools load scripts and styles from a CDN or inline. The default CSP blocks them. Either set `contentSecurityPolicy: false` only in development, or add the needed sources. Don't turn CSP off in production just to make a dev tool work.

## 193: How do you allow CORS for several origins safely?

Pass an array or a function. Don't reflect any origin the browser sends.

```ts
const allowed = new Set(config.getOrThrow<string>("CORS_ORIGINS").split(","));

app.enableCors({
  origin: (origin, cb) => {
    if (!origin || allowed.has(origin)) return cb(null, true);
    cb(new Error("Not allowed by CORS"), false);
  },
  credentials: true,
  methods: ["GET", "POST", "PUT", "PATCH", "DELETE"],
  maxAge: 600,
});
```

## 194: Why can't you use origin: '*' with credentials: true?

Browsers refuse to send credentials to `Access-Control-Allow-Origin: *`. Some people "fix" this by reflecting the request's `Origin` back, which allows every site to read responses with the user's cookies. That's a real vulnerability. Use an explicit list.

## 195: What's wrong with checking CORS origins with a regex like /example.com/?

It matches `example.com.attacker.net` and `attackerexample.com`. Use exact string matches, or anchor the regex and escape the dots, like `/^https:\/\/([a-z0-9-]+\.)?example\.com$/`.

## 196: How do you set up csrf-csrf in a Nest app?

```ts
import { doubleCsrf } from "csrf-csrf";

const { doubleCsrfProtection, generateCsrfToken } = doubleCsrf({
  getSecret: () => config.getOrThrow("CSRF_SECRET"),
  getSessionIdentifier: (req) => req.session.id,
  cookieName: "__Host-csrf",
  cookieOptions: { sameSite: "strict", secure: true, httpOnly: true },
});

app.use(cookieParser());
app.use(doubleCsrfProtection);
```

Expose an endpoint that returns `generateCsrfToken(req, res)`. The frontend sends it back in the `x-csrf-token` header on unsafe requests.

## 197: Which HTTP methods need CSRF protection?

State-changing ones: `POST`, `PUT`, `PATCH`, `DELETE`. `GET`, `HEAD` and `OPTIONS` should never change data, so they are skipped. If a `GET` route does change data, that's a bug to fix first.

## 198: Is SameSite=Lax enough to stop CSRF?

It stops most of it, but not all. `Lax` still sends cookies on top-level `GET` navigations, and requests from your own subdomains count as same-site. For cookie-based auth on sensitive actions, use SameSite plus a CSRF token or a check of the `Origin` header.

## 199: How do you use several rate limits at once?

Give each throttler a name. All of them apply to every request.

```ts
ThrottlerModule.forRoot([
  { name: "short", ttl: 1000, limit: 5 },
  { name: "long", ttl: 60_000, limit: 100 },
]);
```

Override one with `@Throttle({ short: { limit: 2, ttl: 1000 } })`.

## 200: How do you store throttler counters in Redis?

The default storage is in memory, so each instance counts on its own. With several instances, use a shared store like `@nest-lab/throttler-storage-redis`.

```ts
ThrottlerModule.forRootAsync({
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    throttlers: [{ ttl: 60_000, limit: 100 }],
    storage: new ThrottlerStorageRedisService(config.getOrThrow("REDIS_URL")),
  }),
});
```

## 201: How do you rate limit by user instead of by IP?

Extend `ThrottlerGuard` and override `getTracker`.

```ts
@Injectable()
export class UserThrottlerGuard extends ThrottlerGuard {
  protected async getTracker(req: Record<string, any>): Promise<string> {
    return req.user?.id ?? req.ip;
  }
}
```

The guard needs `req.user`, so it must run after the auth guard.

## 202: Why can rate limiting by IP alone be a problem?

Many users can share one IP (offices, mobile carriers), so they get blocked together. Attackers can spread requests over many IPs with botnets or proxies. A mix works better: per IP for anonymous routes, per user or per API key for logged-in routes, and per target account on login.

## 203: How do you limit failed logins per account?

Count failures in Redis with a key like `login-fail:<email>` and a TTL. After a few failures add a delay or require a CAPTCHA, and after more lock the account for a short time. Reset the counter on success. Use a temporary lock, not a permanent one, or attackers can lock out real users.

## 204: What bcrypt cost factor should you pick?

Pick the highest that keeps a hash at around 100-300 ms on your production hardware, then measure. 12 is a common start. Bump it over time as hardware gets faster, and rehash on the next successful login.

## 205: What is the 72-byte limit in bcrypt?

bcrypt only uses the first 72 bytes of the input. Longer passwords are cut silently, and some versions behave oddly with very long input. Limit password length in the DTO (for example 128 characters) and prefer Argon2id for new systems.

## 206: Why is password hashing done asynchronously in Node?

Hashing is slow on purpose. The sync versions (`hashSync`) block the event loop, so one login would stall every other request. `bcrypt.hash` and `argon2.hash` run the work in the libuv thread pool.

## 207: How do you upgrade old password hashes to a new algorithm?

On a successful login, you have the plain password. Check it against the old hash, then hash it with the new algorithm and save it. Users who don't log in can be forced to reset after a while. With argon2, `argon2.needsRehash(hash, options)` tells you when parameters changed.

## 208: How do you compare API keys without timing leaks?

Hash the key with SHA-256 and look it up by hash. That avoids comparing secrets byte by byte. If you must compare, use `crypto.timingSafeEqual` on buffers of the same length.

```ts
const hash = createHash("sha256").update(apiKey).digest("hex");
const record = await this.repo.findOneBy({
  keyHash: hash,
  revokedAt: IsNull(),
});
```

## 209: Why is SHA-256 fine for API keys but not for passwords?

API keys are long random values with lots of entropy, so guessing is impossible even with fast hashes. Passwords are short and chosen by humans, so attackers can try common ones fast. Slow hashes are only needed for low-entropy secrets.

## 210: What should an API key system support?

A prefix so you can tell keys apart (like `sk_live_`), storing only a hash, showing the full key once at creation, scopes, expiry, last-used time, and easy revocation and rotation. A prefix also helps secret scanners find leaked keys.

## 211: How do you add Google login with Passport in Nest?

```ts
@Injectable()
export class GoogleStrategy extends PassportStrategy(Strategy, "google") {
  constructor(
    config: ConfigService,
    private auth: AuthService,
  ) {
    super({
      clientID: config.getOrThrow("GOOGLE_CLIENT_ID"),
      clientSecret: config.getOrThrow("GOOGLE_CLIENT_SECRET"),
      callbackURL: config.getOrThrow("GOOGLE_CALLBACK_URL"),
      scope: ["email", "profile"],
    });
  }

  async validate(_at: string, _rt: string, profile: Profile) {
    return this.auth.findOrCreateFromGoogle(profile);
  }
}
```

Use `@UseGuards(AuthGuard('google'))` on both the start route and the callback route.

## 212: What is the state parameter in OAuth?

A random value your app sends with the authorization request and checks when the provider redirects back. It stops an attacker from making the user finish a login flow the attacker started (login CSRF). Most Passport OAuth strategies support `state: true` with a session.

## 213: What is PKCE?

Proof Key for Code Exchange. The client makes a random `code_verifier`, sends its hash (`code_challenge`) when starting the login, and sends the verifier when exchanging the code. A stolen authorization code is useless without the verifier. OAuth 2.1 requires PKCE for all clients.

## 214: Which OAuth flows should you not use anymore?

The implicit flow (tokens in the URL fragment) and the resource owner password flow (the app collects the user's password). Use the authorization code flow with PKCE for apps, and client credentials for server-to-server.

## 215: How do you validate tokens issued by an external identity provider?

Fetch the provider's public keys from its JWKS URL, verify the signature, and check `iss`, `aud` and `exp`. With `passport-jwt` you can use `jwks-rsa`.

```ts
super({
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
  secretOrKeyProvider: passportJwtSecret({
    jwksUri: "https://login.example.com/.well-known/jwks.json",
    cache: true,
    rateLimit: true,
  }),
  issuer: "https://login.example.com/",
  audience: "api://orders",
  algorithms: ["RS256"],
});
```

## 216: How do you validate external tokens with the jose library?

```ts
import { createRemoteJWKSet, jwtVerify } from "jose";

const jwks = createRemoteJWKSet(
  new URL("https://login.example.com/.well-known/jwks.json"),
);

const { payload } = await jwtVerify(token, jwks, {
  issuer: "https://login.example.com/",
  audience: "api://orders",
});
```

`jose` caches the keys and refetches them when it sees an unknown `kid`.

## 217: What is the client credentials flow?

An OAuth flow for machine-to-machine calls. A service sends its client id and secret to the token endpoint and gets an access token, with no user involved. Your Nest API then checks that token like any other JWT, usually looking at scopes instead of roles.

## 218: How do you check OAuth scopes in a guard?

```ts
export const Scopes = Reflector.createDecorator<string[]>();

@Injectable()
export class ScopesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(ctx: ExecutionContext) {
    const needed = this.reflector.get(Scopes, ctx.getHandler()) ?? [];
    const granted: string[] = (
      ctx.switchToHttp().getRequest().user?.scope ?? ""
    ).split(" ");
    return needed.every((s) => granted.includes(s));
  }
}
```

## 219: How do you validate env variables with Joi?

```ts
ConfigModule.forRoot({
  isGlobal: true,
  validationSchema: Joi.object({
    NODE_ENV: Joi.string()
      .valid("development", "production", "test")
      .required(),
    DATABASE_URL: Joi.string().uri().required(),
    JWT_ACCESS_SECRET: Joi.string().min(32).required(),
  }),
  validationOptions: { abortEarly: false },
});
```

## 220: How do you validate env variables with class-validator?

Pass a `validate` function that turns the config into a class and validates it.

```ts
class EnvVars {
  @IsString()
  @MinLength(32)
  JWT_ACCESS_SECRET: string;

  @IsUrl({ require_tld: false })
  DATABASE_URL: string;
}

export function validate(config: Record<string, unknown>) {
  const env = plainToInstance(EnvVars, config, {
    enableImplicitConversion: true,
  });
  const errors = validateSync(env, { skipMissingProperties: false });
  if (errors.length) throw new Error(errors.toString());
  return env;
}
```

## 221: How do you load secrets from AWS Secrets Manager or Vault into Nest?

Use a custom config loader in `ConfigModule.forRoot({ load: [...] })` that fetches secrets at startup, or a provider with `useFactory` that returns them. The app's runtime role gets read access only to its own secrets. Avoid writing them to disk or logging the config object.

## 222: Why is it risky to log the whole config at startup?

It's a common debugging habit, and it writes every secret into your log system, where many people and tools can read them, and where they live for a long time. If you need a startup summary, log only names and whether each one is set.

## 223: How do you serve Nest over HTTPS directly?

Pass `httpsOptions` to `NestFactory.create`.

```ts
const app = await NestFactory.create(AppModule, {
  httpsOptions: {
    key: fs.readFileSync("secrets/server.key"),
    cert: fs.readFileSync("secrets/server.crt"),
  },
});
```

In most production setups a proxy terminates TLS instead.

## 224: How do you redirect HTTP to HTTPS when behind a proxy?

Check `X-Forwarded-Proto` (with `trust proxy` set so Express fills `req.secure`). Often it's easier and safer to do the redirect at the load balancer and send HSTS from the app.

```ts
app.use((req, res, next) => {
  if (!req.secure)
    return res.redirect(301, `https://${req.headers.host}${req.url}`);
  next();
});
```

## 225: How do you encrypt a field before storing it?

Use AES-256-GCM with a random IV per value and store the IV and the auth tag with the ciphertext.

```ts
const key = Buffer.from(config.getOrThrow("FIELD_KEY"), "base64"); // 32 bytes

export function encrypt(text: string): string {
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const data = Buffer.concat([cipher.update(text, "utf8"), cipher.final()]);
  return [iv, cipher.getAuthTag(), data]
    .map((b) => b.toString("base64"))
    .join(".");
}

export function decrypt(payload: string): string {
  const [iv, tag, data] = payload
    .split(".")
    .map((s) => Buffer.from(s, "base64"));
  const decipher = createDecipheriv("aes-256-gcm", key, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(data), decipher.final()]).toString(
    "utf8",
  );
}
```

## 226: Why use AES-GCM instead of AES-CBC?

GCM encrypts and also checks integrity with the auth tag, so changed ciphertext fails to decrypt. CBC only encrypts, and without a separate MAC it's open to padding oracle attacks. GCM is the usual default today.

## 227: How can you search a column that is encrypted?

Random-IV encryption gives different output each time, so you can't search it. A common fix is to store a separate "blind index", an HMAC of the normalized value with its own key, and search by that. It allows exact matches only.

## 228: How do you plug field encryption into TypeORM?

Use a column `transformer`, which runs on save and load.

```ts
@Column({
  type: 'text',
  transformer: { to: (v: string) => v && encrypt(v), from: (v: string) => v && decrypt(v) },
})
taxId: string;
```

## 229: How do you build a dynamic ORDER BY safely in TypeORM?

Column names can't be parameters, so map user input to an allowlist.

```ts
const sortable = { name: "user.name", created: "user.createdAt" } as const;
const column = sortable[query.sort] ?? "user.createdAt";
qb.orderBy(column, query.dir === "asc" ? "ASC" : "DESC");
```

## 230: How do you write a safe raw query in Prisma?

Use `$queryRaw` as a tagged template. Use `Prisma.sql` and `Prisma.join` to build parts.

```ts
const users = await prisma.$queryRaw<User[]>`
  SELECT id, email FROM "User" WHERE email = ${email} AND "orgId" IN (${Prisma.join(orgIds)})
`;
```

## 231: How do you write a safe raw query in TypeORM?

Pass parameters as the second argument. With PostgreSQL the placeholders are `$1`, `$2`; with MySQL they are `?`.

```ts
await dataSource.query("SELECT * FROM users WHERE email = $1", [email]);
```

## 232: Is the Raw operator in TypeORM safe?

Only if you use its parameter argument. A callback that returns fixed SQL, like `alias > NOW()`, is fine. Putting user input inside the string is SQL injection.

```ts
where: {
  name: Raw((alias) => `LOWER(${alias}) = LOWER(:name)`, { name });
}
```

## 233: How do you protect Mongoose queries from operator injection?

Validate types in DTOs, and turn on Mongoose's `sanitizeFilter`, which wraps values with `$` keys in `$eq` so they are treated as plain values.

```ts
mongoose.set("sanitizeFilter", true);
// or per query
User.findOne({ email, password }).setOptions({ sanitizeFilter: true });
```

## 234: Why shouldn't you use $where in MongoDB queries with user input?

`$where` runs JavaScript on the database server. Putting user input into it is code injection. MongoDB has deprecated server-side JavaScript in newer versions. Use normal query operators or the aggregation pipeline.

## 235: Why doesn't express-mongo-sanitize work well with Nest 11 and later?

Nest 11 uses Express 5, where `req.query` is a getter and can't be reassigned the way older middleware expects. That breaks some sanitize middleware. Validating with DTOs and using Mongoose's `sanitizeFilter` is a better approach anyway.

## 236: How do you sanitize HTML that users submit, like blog posts?

Use an allowlist sanitizer such as `sanitize-html` or DOMPurify (via `isomorphic-dompurify` on the server) with a small set of allowed tags and attributes.

```ts
import sanitizeHtml from "sanitize-html";

const clean = sanitizeHtml(dto.body, {
  allowedTags: ["p", "b", "i", "a", "ul", "ol", "li", "code", "pre"],
  allowedAttributes: { a: ["href"] },
  allowedSchemes: ["http", "https", "mailto"],
});
```

## 237: How can you sanitize input with a decorator in a DTO?

Use `@Transform` from class-transformer, which runs when `transform: true` is on.

```ts
export class CommentDto {
  @Transform(({ value }) => sanitizeHtml(value, { allowedTags: [] }))
  @IsString()
  @MaxLength(2000)
  text: string;
}
```

Usually it's better to store the raw text and escape on output, and to sanitize only when you really store HTML.

## 238: Why can javascript: URLs be an XSS problem even with escaping?

If a user can set a profile link and the frontend renders `<a href="{{url}}">`, escaping doesn't help because `javascript:alert(1)` has no special HTML characters. Validate URLs on input with `@IsUrl({ protocols: ['http', 'https'], require_protocol: true })`.

## 239: How do you stop uploaded files from being served as HTML?

Store them in object storage (like S3) on a separate domain, set the right `Content-Type`, add `Content-Disposition: attachment` for unknown types, and send `X-Content-Type-Options: nosniff`. Never serve uploads from the same origin as your app without these headers.

## 240: Why isn't the client's MIME type enough to check a file?

`file.mimetype` comes from the request and the client can set it to anything. Check the actual bytes (magic numbers) with a library like `file-type`. Recent Nest versions of `FileTypeValidator` also look at the file's magic bytes, not only the claimed type.

## 241: How do you build file validation with ParseFilePipeBuilder?

```ts
@UploadedFile(
  new ParseFilePipeBuilder()
    .addFileTypeValidator({ fileType: 'image/png' })
    .addMaxSizeValidator({ maxSize: 1_000_000 })
    .build({ errorHttpStatusCode: HttpStatus.UNPROCESSABLE_ENTITY }),
)
file: Express.Multer.File
```

## 242: Which Multer limits should you set besides fileSize?

`files` (number of files), `fields` (number of non-file fields), `fieldSize` (max size of a field value), `parts` and `headerPairs`. Without them a multipart request with thousands of small fields can still use a lot of memory and CPU.

```ts
FileInterceptor("file", {
  limits: { fileSize: 5_000_000, files: 1, fields: 10, fieldSize: 100_000 },
});
```

## 243: Should you use memory storage or disk storage for uploads?

Memory storage (the default when you don't set `dest` or `storage`) keeps the whole file in RAM, which is fine for small files with strict limits. For bigger files, stream to disk or straight to object storage. Never accept large files into memory without a limit.

## 244: How do you scan uploads for malware?

Send the file to a scanner like ClamAV (for example via a `clamd` client) or a cloud scanning service before marking it as available. A common pattern is upload to a quarantine bucket, scan in a background job, then move clean files to the real bucket.

## 245: How do you avoid path traversal when saving files to disk?

Never build a path from user input. Generate the name yourself and keep it inside one folder.

```ts
const name = `${randomUUID()}${extFromMime(file.mimetype)}`;
const target = path.join(UPLOAD_DIR, name);
if (!target.startsWith(UPLOAD_DIR + path.sep)) throw new BadRequestException();
```

## 246: How do you write a global filter that hides internal errors?

```ts
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  private readonly logger = new Logger(AllExceptionsFilter.name);

  constructor(private readonly adapterHost: HttpAdapterHost) {}

  catch(exception: unknown, host: ArgumentsHost) {
    const { httpAdapter } = this.adapterHost;
    const ctx = host.switchToHttp();
    const req = ctx.getRequest();

    const status =
      exception instanceof HttpException ? exception.getStatus() : 500;
    const body =
      exception instanceof HttpException
        ? exception.getResponse()
        : {
            statusCode: 500,
            message: "Internal server error",
            requestId: req.id,
          };

    if (status >= 500)
      this.logger.error(exception, undefined, `requestId=${req.id}`);
    httpAdapter.reply(ctx.getResponse(), body, status);
  }
}
```

## 247: How do you turn a Prisma unique constraint error into a safe response?

Catch `PrismaClientKnownRequestError` and map the code. Don't send `exception.message`, which includes the query details.

```ts
@Catch(Prisma.PrismaClientKnownRequestError)
export class PrismaFilter implements ExceptionFilter {
  catch(e: Prisma.PrismaClientKnownRequestError, host: ArgumentsHost) {
    const res = host.switchToHttp().getResponse();
    if (e.code === "P2002")
      return res
        .status(409)
        .json({ statusCode: 409, message: "Already exists" });
    if (e.code === "P2025")
      return res.status(404).json({ statusCode: 404, message: "Not found" });
    res.status(500).json({ statusCode: 500, message: "Internal server error" });
  }
}
```

## 248: Can a 409 "email already exists" response be a problem?

Yes, it lets anyone check which emails are registered. On sign-up you can instead always say "check your email" and send either a welcome mail or a "you already have an account" mail. Whether that's worth the extra work depends on how sensitive account existence is for your product.

## 249: How do you add a request id to every log line?

Generate an id in middleware (or reuse an incoming `X-Request-Id` after checking its format), put it on the request and in the response header, and include it in logs. `nestjs-pino` does this with the `genReqId` option. `nestjs-cls` can carry it to code that has no access to the request.

## 250: How do you hide secrets in nestjs-pino logs?

Use `redact` with the paths to remove.

```ts
LoggerModule.forRoot({
  pinoHttp: {
    redact: {
      paths: [
        "req.headers.authorization",
        "req.headers.cookie",
        "req.body.password",
        'res.headers["set-cookie"]',
      ],
      censor: "[REDACTED]",
    },
  },
});
```

Note that pino-http doesn't log bodies by default; only add them if you need them.

## 251: How do you build an audit log with an interceptor?

```ts
@Injectable()
export class AuditInterceptor implements NestInterceptor {
  constructor(
    private audit: AuditService,
    private reflector: Reflector,
  ) {}

  intercept(ctx: ExecutionContext, next: CallHandler) {
    const action = this.reflector.get(AuditAction, ctx.getHandler());
    if (!action) return next.handle();
    const req = ctx.switchToHttp().getRequest();
    return next.handle().pipe(
      tap({
        next: () =>
          this.audit.record({
            action,
            userId: req.user?.id,
            ip: req.ip,
            ok: true,
          }),
        error: (e) =>
          this.audit.record({
            action,
            userId: req.user?.id,
            ip: req.ip,
            ok: false,
            error: e?.name,
          }),
      }),
    );
  }
}
```

## 252: Why log denied requests from guards?

A burst of 403s from one user or IP often means someone is probing for access control bugs. Logging them (with user, route and reason) lets you alert on it. Keep the log line small so an attacker can't fill your logs cheaply.

## 253: How do you authenticate a Socket.IO connection in a Nest gateway?

Check the token in `handleConnection` and disconnect if it's bad.

```ts
@WebSocketGateway({
  cors: { origin: ["https://app.example.com"], credentials: true },
})
export class ChatGateway implements OnGatewayConnection {
  constructor(private jwt: JwtService) {}

  async handleConnection(client: Socket) {
    try {
      const token = client.handshake.auth?.token;
      client.data.user = await this.jwt.verifyAsync(token);
    } catch {
      client.disconnect(true);
    }
  }
}
```

## 254: How do you use Socket.IO middleware for authentication in Nest?

Register it in `afterInit`. Middleware runs before the connection is accepted, so an unauthenticated client never connects at all.

```ts
afterInit(server: Server) {
  server.use(async (socket, next) => {
    try {
      socket.data.user = await this.jwt.verifyAsync(socket.handshake.auth?.token);
      next();
    } catch {
      next(new Error('unauthorized'));
    }
  });
}
```

## 255: How do you write a guard for WebSocket messages?

```ts
@Injectable()
export class WsAuthGuard implements CanActivate {
  canActivate(context: ExecutionContext) {
    const client = context.switchToWs().getClient<Socket>();
    if (!client.data.user) throw new WsException('Unauthorized');
    return true;
  }
}

@UseGuards(WsAuthGuard)
@SubscribeMessage('send')
send(@MessageBody() data: SendDto, @ConnectedSocket() client: Socket) {}
```

## 256: Do pipes and validation work on WebSocket messages?

Yes. You can use `@UsePipes(new ValidationPipe())` on a gateway or handler. A failed validation throws a `BadRequestException`, which the default WS filter doesn't map well, so set `exceptionFactory` to throw a `WsException` instead.

```ts
@UsePipes(new ValidationPipe({ whitelist: true, exceptionFactory: (errors) => new WsException(errors) }))
```

## 257: How do you stop users from joining rooms they don't belong to?

Check membership on the server every time a client asks to join a room. Never trust a room name from the client by itself.

```ts
@SubscribeMessage('join')
async join(@MessageBody() { roomId }: JoinDto, @ConnectedSocket() client: Socket) {
  if (!(await this.rooms.isMember(roomId, client.data.user.sub))) {
    throw new WsException('Forbidden');
  }
  await client.join(`room:${roomId}`);
}
```

## 258: Why set CORS on the WebSocket gateway separately?

The gateway runs its own server setup, and `app.enableCors()` doesn't configure Socket.IO. Set `cors` in `@WebSocketGateway()` options. Note that native WebSocket connections aren't covered by CORS at all, so also check the `Origin` header on the handshake.

## 259: How do you add a depth limit to Nest GraphQL with Apollo?

Use `graphql-depth-limit` (or a similar package) in `validationRules`.

```ts
import depthLimit from "graphql-depth-limit";

GraphQLModule.forRoot<ApolloDriverConfig>({
  driver: ApolloDriver,
  autoSchemaFile: true,
  validationRules: [depthLimit(7)],
  introspection: process.env.NODE_ENV !== "production",
});
```

## 260: How do you set field complexity in a code-first GraphQL schema?

Use the `complexity` option on `@Field()`, then a plugin that adds up complexity per query and rejects ones that are too expensive.

```ts
@Field(() => [Post], { complexity: (opts) => opts.childComplexity * (opts.args.take ?? 10) })
posts: Post[];
```

## 261: How do you write a query complexity plugin for Apollo in Nest?

The Nest docs show this approach with `graphql-query-complexity`.

```ts
@Plugin()
export class ComplexityPlugin implements ApolloServerPlugin {
  constructor(private gqlSchemaHost: GraphQLSchemaHost) {}

  async requestDidStart(): Promise<GraphQLRequestListener<any>> {
    const { schema } = this.gqlSchemaHost;
    return {
      async didResolveOperation({ request, document }) {
        const complexity = getComplexity({
          schema,
          operationName: request.operationName,
          query: document,
          variables: request.variables,
          estimators: [
            fieldExtensionsEstimator(),
            simpleEstimator({ defaultComplexity: 1 }),
          ],
        });
        if (complexity > 500) {
          throw new GraphQLError(
            `Query is too complex: ${complexity}. Max is 500.`,
          );
        }
      },
    };
  }
}
```

## 262: How do you apply a guard to a GraphQL resolver?

The same way as a controller, but the guard must read the GraphQL context.

```ts
@Resolver(() => Order)
@UseGuards(GqlAuthGuard)
export class OrdersResolver {
  @Query(() => [Order])
  myOrders(@CurrentUser() user: User) {
    return this.orders.findByUser(user.id);
  }
}
```

Your `CurrentUser` decorator must also support `GqlExecutionContext`.

## 263: How do you write a param decorator that works for both REST and GraphQL?

Check the context type.

```ts
export const CurrentUser = createParamDecorator(
  (_: unknown, ctx: ExecutionContext) => {
    if (ctx.getType<GqlContextType>() === "graphql") {
      return GqlExecutionContext.create(ctx).getContext().req.user;
    }
    return ctx.switchToHttp().getRequest().user;
  },
);
```

## 264: How do you protect a single GraphQL field?

Use field middleware or put the field in a `@ResolveField()` with a check. Field middleware is lightweight.

```ts
const adminOnly: FieldMiddleware = async (ctx, next) => {
  if (ctx.context.req.user?.role !== 'admin') return null;
  return next();
};

@Field({ middleware: [adminOnly] })
internalNotes: string;
```

Returning `null` hides it; throwing an error is clearer if the client should know.

## 265: What is a GraphQL batching or aliasing attack?

A client sends one request with hundreds of aliased operations, like `a1: login(...)`, `a2: login(...)`, and so on. Rate limits per HTTP request don't see it. Limit the number of aliases and operations, include them in complexity, and turn off array batching if you don't need it.

## 266: How do you secure a Nest TCP microservice with TLS?

Since Nest 11 the TCP transport accepts `tlsOptions` on the server and the client.

```ts
app.connectMicroservice<MicroserviceOptions>({
  transport: Transport.TCP,
  options: {
    host: "0.0.0.0",
    port: 4000,
    tlsOptions: {
      key: fs.readFileSync("certs/server.key"),
      cert: fs.readFileSync("certs/server.crt"),
      ca: [fs.readFileSync("certs/ca.crt")],
      requestCert: true,
      rejectUnauthorized: true,
    },
  },
});
```

With `requestCert` and `rejectUnauthorized`, clients must present a certificate signed by your CA, which is mTLS.

## 267: How do you connect to RabbitMQ securely from Nest?

Use `amqps://` URLs with a user that only has access to its own virtual host and queues. Don't use the default `guest` user.

```ts
ClientsModule.register([
  {
    name: "ORDERS",
    transport: Transport.RMQ,
    options: {
      urls: [config.getOrThrow("RMQ_URL")], // amqps://orders-svc:***@mq.internal:5671/orders
      queue: "orders",
    },
  },
]);
```

## 268: How do you set up Kafka authentication in a Nest microservice?

Pass KafkaJS `ssl` and `sasl` options.

```ts
options: {
  client: {
    brokers: ['kafka-1:9093'],
    ssl: true,
    sasl: { mechanism: 'scram-sha-512', username: 'orders', password: config.getOrThrow('KAFKA_PASSWORD') },
  },
  consumer: { groupId: 'orders' },
}
```

On the broker side, use ACLs so each service can only read and write its own topics.

## 269: How do you use guards on microservice message handlers?

Guards work on `@MessagePattern` and `@EventPattern` handlers. Read the data with `switchToRpc()` and throw `RpcException` on failure.

```ts
@Injectable()
export class RpcAuthGuard implements CanActivate {
  constructor(private jwt: JwtService) {}

  async canActivate(ctx: ExecutionContext) {
    const data = ctx.switchToRpc().getData();
    try {
      data.user = await this.jwt.verifyAsync(data.token);
      return true;
    } catch {
      throw new RpcException("Unauthorized");
    }
  }
}
```

## 270: How do you pass the user identity from a gateway to an internal service?

Either forward the original access token, or have the gateway create a short-lived internal token with the user id and the calling service in it. Don't send a plain `userId` field and trust it, because any service that can publish a message could then act as any user.

## 271: How do you get the tenant id for a request?

From something the client can't fake: a claim in the verified JWT, the API key's owner, or the verified subdomain mapped to a tenant. A plain `X-Tenant-Id` header is only safe if you check that the user belongs to that tenant.

## 272: How do you carry the tenant id through the app without passing it everywhere?

Use `AsyncLocalStorage`, usually through `nestjs-cls`. Set the tenant in middleware or a guard, then read it in repositories.

```ts
ClsModule.forRoot({
  global: true,
  middleware: {
    mount: true,
    setup: (cls, req) => cls.set("tenantId", req.user?.tenantId),
  },
});
```

The middleware runs before guards, so if the tenant comes from the auth guard, set it in the guard or an interceptor instead.

## 273: How do you make sure every query filters by tenant?

Don't depend on developers remembering. Wrap the repository or use a Prisma client extension that adds `tenantId` to every query, and add tests that check cross-tenant reads fail. Database row-level security adds a second layer.

## 274: How do you add the tenant filter with a Prisma client extension?

```ts
export function forTenant(prisma: PrismaClient, tenantId: string) {
  return prisma.$extends({
    query: {
      $allModels: {
        async $allOperations({ args, query, operation }) {
          if (
            [
              "findMany",
              "findFirst",
              "count",
              "updateMany",
              "deleteMany",
            ].includes(operation)
          ) {
            args.where = { ...args.where, tenantId };
          }
          if (operation === "create") {
            args.data = { ...args.data, tenantId };
          }
          return query(args);
        },
      },
    },
  });
}
```

`findUnique`, `update` and `delete` need care because their `where` must match a unique key. Many teams add a compound unique key `(tenantId, id)` for that.

## 275: What does the __Host- cookie prefix do?

A cookie named `__Host-something` is only accepted if it has `Secure`, `Path=/` and no `Domain`. That means a subdomain can't set or override it. It's a cheap way to protect session and CSRF cookies.

## 276: How do you use signed cookies in Nest?

Pass a secret to `cookie-parser` and set `signed: true`. Signed values appear in `req.signedCookies`. Signing stops changes but doesn't hide the value.

```ts
app.use(cookieParser(config.getOrThrow("COOKIE_SECRET")));
res.cookie("pref", "dark", { signed: true, httpOnly: true, secure: true });
```

## 277: How do you clear an auth cookie correctly?

Call `res.clearCookie` with the same `path` and `domain` used when it was set, or the browser keeps the old one.

```ts
res.clearCookie("refresh_token", {
  path: "/auth/refresh",
  httpOnly: true,
  secure: true,
  sameSite: "strict",
});
```

## 278: How do you change the JSON body limit in Nest?

On Express, use `useBodyParser`. On Fastify, set `bodyLimit` in the adapter.

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.useBodyParser("json", { limit: "1mb" });
app.useBodyParser("urlencoded", { limit: "100kb", extended: false });
```

```ts
new FastifyAdapter({ bodyLimit: 1_048_576 });
```

## 279: How do you allow a large body on one route only?

Turn off the global parser and add parsers per route with middleware, or keep a small global limit and put the big upload on a route that streams (like a multipart upload with Multer limits). Raising the global limit for one route makes every route weaker.

## 280: How do you set server timeouts to protect against slow clients?

Set Node's HTTP server timeouts so slow or idle connections are closed.

```ts
const server = app.getHttpServer();
server.requestTimeout = 30_000;
server.headersTimeout = 10_000;
server.keepAliveTimeout = 5_000;
```

A reverse proxy in front should also have its own timeouts.

## 281: How do you add a timeout to slow handlers?

Use an interceptor with RxJS `timeout`, so one stuck call to another service doesn't hold resources forever.

```ts
@Injectable()
export class TimeoutInterceptor implements NestInterceptor {
  intercept(_ctx: ExecutionContext, next: CallHandler) {
    return next.handle().pipe(
      timeout(10_000),
      catchError((err) =>
        err instanceof TimeoutError
          ? throwError(() => new RequestTimeoutException())
          : throwError(() => err),
      ),
    );
  }
}
```

This stops the response, but not the work already running, so also use timeouts on database and HTTP clients.

## 282: How do you run npm audit in CI without blocking on low issues?

Fail only on high and critical issues, and only for production packages.

```bash
npm audit --omit=dev --audit-level=high
```

Review the rest on a schedule.

## 283: What does npm audit signatures check?

It checks that installed packages have valid registry signatures and, where available, provenance attestations. It helps catch packages that were changed after publishing.

## 284: Why use --ignore-scripts for installs?

Many supply-chain attacks run code in `postinstall` scripts. `npm ci --ignore-scripts` stops that. Some packages (like `bcrypt` or `argon2`, which need native builds or prebuilt binaries) need their scripts, so allow those on purpose. pnpm doesn't run dependency build scripts unless you allow them.

## 285: How do you write an e2e test that logs in and calls a protected route?

```ts
it("returns the profile for a logged in user", async () => {
  const login = await request(app.getHttpServer())
    .post("/auth/login")
    .send({ email: "a@test.dev", password: "correct horse battery" })
    .expect(201);

  await request(app.getHttpServer())
    .get("/users/me")
    .set("Authorization", `Bearer ${login.body.accessToken}`)
    .expect(200);
});
```

## 286: How do you test that one user can't read another user's data?

Create two users, create a record as user A, and request it as user B. Expect `404` or `403`. This one test pattern catches the most common serious bug.

```ts
await request(server)
  .get(`/invoices/${invoiceOfA.id}`)
  .set("Authorization", `Bearer ${tokenB}`)
  .expect(404);
```

## 287: How do you override a guard in a unit or e2e test?

Use `overrideGuard` on the testing module.

```ts
const moduleRef = await Test.createTestingModule({ imports: [AppModule] })
  .overrideGuard(JwtAuthGuard)
  .useValue({
    canActivate: (ctx) => {
      ctx.switchToHttp().getRequest().user = testUser;
      return true;
    },
  })
  .compile();
```

Keep a few e2e tests that use the real guard, or you never test authentication itself.

## 288: Why should e2e tests apply the same global setup as main.ts?

`Test.createTestingModule` doesn't run `main.ts`. If `ValidationPipe`, Helmet, cookie parsing and global filters are set in `main.ts`, the tests run without them and miss bugs. Move that setup into a shared `configureApp(app)` function and call it in both places.

## 289: How do you test the ValidationPipe whitelist behavior?

```ts
it("rejects unknown fields", () => {
  return request(server)
    .post("/users")
    .send({ email: "a@test.dev", password: "long-enough-pass", role: "admin" })
    .expect(400);
});
```

## 290: How do you test that responses don't contain sensitive fields?

Assert on the response body.

```ts
const res = await request(server)
  .get("/users/me")
  .set("Authorization", bearer)
  .expect(200);
expect(res.body).not.toHaveProperty("passwordHash");
expect(JSON.stringify(res.body)).not.toMatch(/\$argon2|\$2b\$/);
```

## 291: How do you check that security headers are present in tests?

```ts
const res = await request(server).get("/health");
expect(res.headers["x-content-type-options"]).toBe("nosniff");
expect(res.headers["strict-transport-security"]).toBeDefined();
expect(res.headers["x-powered-by"]).toBeUndefined();
```

## 292: How do you scan a running Nest API automatically?

Run a DAST tool like OWASP ZAP against a test environment in CI. Feed it your OpenAPI file from `@nestjs/swagger` so it knows the endpoints, and give it a test token so it can reach protected routes.

## 293: Where does Nest code map to OWASP Top 10 categories?

Broken access control: guards, ownership checks. Cryptographic failures: TLS, hashing, field encryption. Injection: DTO validation, ORM parameters. Insecure design: threat modeling. Misconfiguration: Helmet, CORS, debug flags. Vulnerable components: `npm audit`, updates. Authentication failures: Passport, JWT checks, rate limits. Integrity failures: lockfiles, signed packages. Logging failures: audit logs. SSRF: URL allowlists for outgoing requests.

## 294: What is SSRF and how can it happen in Nest?

Server-side request forgery: your server fetches a URL the user gave, like a webhook or image URL, and the attacker points it at internal addresses such as `http://169.254.169.254/` (cloud metadata) or `http://localhost:6379`. Validate the scheme and host, resolve DNS and block private ranges, and don't follow redirects to other hosts.

## 295: How do you safely call user-supplied webhook URLs?

Allow only `https`, resolve the host and reject private, loopback and link-local IPs, use a short timeout, limit the response size, and turn off redirects. Running webhook calls from a separate worker with no access to internal networks is even safer.

## 296: How do you sign outgoing webhooks so receivers can trust them?

Send an HMAC of the body and a timestamp in a header. The receiver recomputes it and rejects old timestamps.

```ts
const ts = Math.floor(Date.now() / 1000);
const sig = createHmac("sha256", secret).update(`${ts}.${body}`).digest("hex");
headers["X-Signature"] = `t=${ts},v1=${sig}`;
```

## 297: How do you verify an incoming webhook signature in Nest?

You need the raw body, because re-serialized JSON may differ. Enable `rawBody` and compare with `timingSafeEqual`.

```ts
const app = await NestFactory.create(AppModule, { rawBody: true });

@Post('webhooks/stripe')
handle(@Req() req: RawBodyRequest<Request>, @Headers('stripe-signature') sig: string) {
  const event = this.stripe.webhooks.constructEvent(req.rawBody!, sig, this.secret);
}
```

## 298: How do you keep Swagger docs from exposing internal endpoints?

Serve Swagger only outside production, or protect the docs route with basic auth or SSO. Use `@ApiExcludeController()` or `@ApiExcludeEndpoint()` for internal routes. Remember that hiding docs isn't a security control; the routes still need guards.

## 299: Why should NODE_ENV be production in production?

Some libraries change behavior based on it. Express and template engines turn on caching and hide detailed errors, and some tools skip debug features. Your own code may also use it to turn off Swagger, introspection and verbose errors. Forgetting it can expose debug output.

## 300: How do you run Nest in Docker with fewer privileges?

Use a small base image, run as a non-root user, install only production dependencies, and don't copy `.env` files into the image.

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY dist ./dist
USER node
CMD ["node", "dist/main.js"]
```

# Advanced Questions (301-450)

## 301: Why can't a guard rely on the validated DTO, and how do you handle that?

Guards run before pipes, so `req.body` in a guard is the raw, unvalidated input. If a guard reads `req.body.orgId` to check access, an attacker can send an array or object there. Either validate the value inside the guard, move the check into the service after validation, or read ids from route params with a parse pipe applied in the guard's own logic.

## 302: How do you write one auth guard that works for HTTP, WebSockets, RPC and GraphQL?

Branch on `context.getType()` to find where the credentials live, then share the verify logic.

```ts
private extract(ctx: ExecutionContext): string | undefined {
  switch (ctx.getType<string>()) {
    case 'http':
      return ctx.switchToHttp().getRequest().headers.authorization?.replace(/^Bearer /, '');
    case 'ws':
      return ctx.switchToWs().getClient().handshake?.auth?.token;
    case 'rpc':
      return ctx.switchToRpc().getData()?.token;
    case 'graphql':
      return GqlExecutionContext.create(ctx).getContext().req?.headers.authorization?.replace(/^Bearer /, '');
  }
}
```

Throw the right exception per type too: `UnauthorizedException`, `WsException` or `RpcException`.

## 303: In what order do APP_GUARD providers run when they come from different modules?

They run in the order Nest registers them, which follows module order during scanning. That's easy to get wrong when guards live in different feature modules. Keep all global guards in one module (like `AppModule` or a `SecurityModule`) so the order is visible, or have one composite guard that calls the others in a fixed order.

## 304: What goes wrong if a guard is request-scoped?

If a guard injects a request-scoped provider, the guard becomes request-scoped too, and Nest creates it for every request. That costs performance, and global guards registered with `useGlobalGuards(new X())` can't be request-scoped at all. Prefer reading the request from `ExecutionContext` and using `nestjs-cls` for request data.

## 305: How would you design auth for an app with a web SPA and a mobile app?

For the SPA, a backend-for-frontend with an httpOnly session or refresh cookie and CSRF protection keeps tokens out of JavaScript. For mobile, use the authorization code flow with PKCE and keep tokens in the OS keychain. The API itself accepts short-lived access tokens either way, so the same guards work for both.

## 306: What is the backend-for-frontend (BFF) pattern for auth?

A small server, often in Nest, that handles the OAuth flow, keeps the access and refresh tokens on the server side, and gives the browser only a session cookie. The browser calls the BFF, which adds the access token to calls to the real APIs. It removes token theft by XSS, at the cost of one more service and CSRF work.

## 307: How would you design JWT revocation for millions of users?

Keep access tokens very short (5 minutes) and accept that window. For instant revocation, store revoked `jti` values in Redis with a TTL equal to the token's remaining life, so the list stays small. For "log out everywhere", store a per-user `revokedBefore` timestamp and reject tokens with an older `iat`. Cache these lookups in memory for a few seconds to reduce Redis load.

## 308: How do you rotate JWT signing keys without logging everyone out?

Use a `kid` header on every token and keep several keys active. Steps: add a new key and publish it in JWKS, wait until all verifiers have fetched it, switch signing to the new key, then remove the old key after the longest token lifetime has passed. Verifiers pick the key by `kid`.

## 309: How do you expose a JWKS endpoint from a Nest auth service?

Export the public keys as JWK with `jose` and serve them on a public route with caching headers.

```ts
@Public()
@Get('.well-known/jwks.json')
@Header('Cache-Control', 'public, max-age=300')
async jwks() {
  const keys = await Promise.all(
    this.keys.active().map(async (k) => ({ ...(await exportJWK(k.publicKey)), kid: k.kid, alg: 'RS256', use: 'sig' })),
  );
  return { keys };
}
```

## 310: What is a sender-constrained token and why would you use DPoP?

A normal bearer token works for whoever holds it. With DPoP, the client signs each request with a private key, and the token is bound to that key's thumbprint. A stolen token is useless without the key. It's worth it for high-risk APIs, like banking, but adds complexity on both sides.

## 311: How do you handle parallel refresh requests from several browser tabs with rotation?

Two tabs can send the same refresh token at the same time. The second looks like reuse and logs the user out. Options: a short grace period where the just-rotated token can still return the same new pair, a lock in the client so only one tab refreshes (for example with the `BroadcastChannel` or Web Locks API), or both.

## 312: How do you make refresh token rotation safe from race conditions in the database?

Do the check and the update in one atomic step. For example, update the row only if it's still unused and check the affected row count.

```ts
const result = await this.repo
  .createQueryBuilder()
  .update(RefreshToken)
  .set({ usedAt: () => "now()" })
  .where("id = :id AND used_at IS NULL AND revoked_at IS NULL", { id: jti })
  .execute();

if (result.affected !== 1) {
  await this.revokeFamily(familyId);
  throw new UnauthorizedException();
}
```

## 313: Should the auth guard fail open or fail closed when Redis is down?

For auth checks like a token denylist, failing open means revoked tokens work again during an outage, while failing closed means nobody can use the app. Many teams fail open for the denylist on short-lived tokens but fail closed for high-risk actions. Decide it on purpose and document it; don't let the default error handling decide.

## 314: What happens to rate limiting if the Redis throttler storage is down?

The storage call throws, and the guard's error becomes a 500 for every request unless you handle it. You can wrap the storage in a version that falls back to in-memory counting per instance, so limits are looser but the app keeps working. Alert on the fallback.

## 315: How does @nestjs/throttler count requests internally?

For each request it builds a key from the throttler name, the route (class and handler names) and the tracker (IP by default), hashes it, and calls `storage.increment` with the TTL. The storage returns the hit count and time left. If the count is over the limit, the guard throws `ThrottlerException`. With `blockDuration` set, the key stays blocked for that time even after the window resets.

## 316: Why can the default throttler tracker be wrong behind a proxy?

The tracker is `req.ip`. Without `trust proxy`, every request shows the load balancer's IP, so all users share one limit. With `trust proxy` set to `true` but a client-controlled `X-Forwarded-For`, attackers can fake a new IP each request. Set `trust proxy` to the exact number of proxies in front of the app, or to their IP ranges.

## 317: How do you rate limit by the target account on login and not just by IP?

Override `getTracker` for that route or use a separate counter keyed on the normalized email. Combine with the IP limit so neither a botnet nor one IP can hammer one account.

```ts
@Injectable()
export class LoginThrottlerGuard extends ThrottlerGuard {
  protected async getTracker(req: Record<string, any>) {
    const email = String(req.body?.email ?? "")
      .trim()
      .toLowerCase();
    return `login:${email}`;
  }
}
```

The body isn't validated yet here, so the guard turns it into a string itself.

## 318: How do you prevent memory growth from the in-memory throttler?

Every unique tracker creates a key. If the tracker comes from something an attacker controls (a random header, a long email), they can create millions of keys. Use a bounded store or Redis with TTLs, hash or cut long tracker values, and validate inputs before using them as keys.

## 319: How can a timing difference leak whether a user exists?

If the login code returns right away for an unknown email but runs a slow password hash for a known one, response times differ by hundreds of milliseconds. Attackers can measure that. Fix it by hashing against a dummy hash when the user doesn't exist.

```ts
const DUMMY = await argon2.hash('dummy-password-for-timing');

async validateUser(email: string, password: string) {
  const user = await this.users.findByEmail(email);
  const ok = await argon2.verify(user?.passwordHash ?? DUMMY, password);
  return user && ok ? user : null;
}
```

## 320: What Argon2id parameters would you choose and why?

OWASP lists several equal options, for example 19 MiB memory with 2 iterations and 1 degree of parallelism, or 46 MiB with 1 iteration. More memory makes GPU attacks much more expensive. Pick the setting your server can handle under peak login load, measure the time per hash, and make sure memory per hash times concurrent logins fits in RAM.

## 321: How can password hashing itself become a DoS vector?

Each hash is slow and uses memory on purpose. An attacker sending thousands of login or sign-up requests can use all CPU and the libuv thread pool, which also blocks file and DNS work. Rate limit before hashing, cap password length, and consider raising `UV_THREADPOOL_SIZE` or moving hashing to a worker pool.

## 322: What is a password breach check and how do you add it without sending the password?

Have I Been Pwned's range API uses k-anonymity: you send only the first 5 characters of the SHA-1 hash of the password and get back all suffixes with that prefix. You check locally whether the full hash is in the list. Do this at sign-up and password change, and fail open if the API is down.

## 323: How would you design API key scopes and enforcement?

Store scopes with each key, like `orders:read` and `orders:write`. The API key guard puts the key's scopes on the request, and a scopes guard checks them against route metadata. Keep scopes coarse enough to manage and allow a key only on its own tenant's data, enforced in the data layer too.

## 324: How do you design API key rotation for customers?

Let a customer have two active keys at the same time. They create a new key, update their systems, then revoke the old one. Show last-used time on each key so they know when the old one is no longer in use. Support an expiry date and email reminders before it.

## 325: How do you detect leaked API keys?

Give keys a recognizable prefix and register the format with GitHub secret scanning partner program if you're a provider, or use scanners like gitleaks or trufflehog in your own CI. Watch for use from new IPs or countries and unusual request patterns, and have a one-click revoke.

## 326: What are the risks of implementing OAuth login callbacks yourself?

Missing `state` checks (login CSRF), missing PKCE, not checking the ID token's `aud`, `iss`, `nonce` and `exp`, open redirects through a `returnTo` parameter, and linking accounts by unverified email. Using a certified library like `openid-client` or a Passport strategy avoids most of these.

## 327: Why is linking accounts by email dangerous in social login?

If a provider lets users set an unverified email, an attacker can create an account there with the victim's email and log into the victim's account in your app. Only link when the provider says the email is verified (`email_verified: true`), and ask the user to confirm linking from their existing account.

## 328: How do you prevent open redirects after login?

Don't redirect to any URL from a query parameter. Accept only relative paths, or compare against an allowlist of hosts.

```ts
function safeReturnTo(value?: string) {
  if (
    !value ||
    !value.startsWith("/") ||
    value.startsWith("//") ||
    value.includes("\\")
  )
    return "/";
  return value;
}
```

## 329: How do you use openid-client in a Nest app?

Version 6 of `openid-client` has a function-based API. Discover the provider once at startup, then build the authorization URL with PKCE and exchange the code in the callback.

```ts
const oidc = await client.discovery(new URL(issuerUrl), clientId, clientSecret);

// login route
const verifier = client.randomPKCECodeVerifier();
const challenge = await client.calculatePKCECodeChallenge(verifier);
const state = client.randomState();
req.session.oidc = { verifier, state };
const url = client.buildAuthorizationUrl(oidc, {
  redirect_uri: callbackUrl,
  scope: "openid email profile",
  code_challenge: challenge,
  code_challenge_method: "S256",
  state,
});

// callback route
const tokens = await client.authorizationCodeGrant(
  oidc,
  new URL(req.originalUrl, baseUrl),
  {
    pkceCodeVerifier: req.session.oidc.verifier,
    expectedState: req.session.oidc.state,
  },
);
const claims = tokens.claims();
```

## 330: How would you support SSO for many enterprise customers in one Nest app?

Store an identity provider config per tenant (OIDC issuer, client id and secret, or SAML metadata). On login, find the tenant from the email domain or subdomain, then run the flow against that tenant's provider. Only accept users whose ID token issuer matches that tenant's config, so one tenant's IdP can't log users into another tenant. Many teams use a broker like Keycloak, Auth0 or WorkOS to avoid building this.

## 331: What is SCIM and why does it matter for security?

SCIM is a standard API that identity providers use to create, update and deactivate users in your app. With it, when a company removes an employee in Okta or Entra ID, your app disables them right away instead of waiting for them to try logging in. You implement it as a set of protected REST endpoints in Nest.

## 332: How do you handle back-channel logout from an identity provider?

With OIDC back-channel logout, the IdP sends a signed logout token to your endpoint. Verify it like an ID token (signature, `iss`, `aud`, `iat`, the `events` claim), then find and delete the sessions with that `sid` or `sub`. Keep a mapping from IdP session id to your sessions so you can find them.

## 333: How would you design authorization for a large app with many rules?

Keep the rules in one place, not spread over controllers. A policy layer (CASL, or a service like OpenFGA, Cerbos or OPA) answers "can user X do action Y on resource Z". Guards handle coarse checks (logged in, has role), services call the policy layer with the loaded record, and list queries use the policy to build filters. Test policies on their own.

## 334: When would you use relationship-based access control (ReBAC)?

When permissions come from relationships, like Google Drive: a user can edit a doc because they're in a group that owns the folder that contains it. Encoding that in roles explodes quickly. ReBAC systems such as OpenFGA or SpiceDB (based on Google's Zanzibar paper) store relationships and answer checks fast. Nest calls them from guards or services.

## 335: Why is checking permissions only in guards not enough for list endpoints?

A guard can say "user may list invoices", but it can't filter which invoices. If the service runs `findMany()` without a filter, the user sees everyone's data. List queries need the permission rules turned into a `where` clause, like CASL's `accessibleBy` or a tenant filter.

## 336: How do you avoid a TOCTOU bug in authorization checks?

Time-of-check to time-of-use: you check that a user owns record 5, then update it later, but meanwhile ownership changed. Put the ownership condition in the update itself, for example `UPDATE ... WHERE id = $1 AND owner_id = $2`, and check the affected row count. That way check and use are one step.

## 337: What problems come from returning 403 versus 404 for records a user can't see?

A 403 tells the attacker the record exists. For private data, return 404 for both "doesn't exist" and "not yours", which is what you get anyway if you filter queries by owner. Use 403 when existence isn't secret, like an admin-only page.

## 338: How would you handle impersonation ("log in as user") for support staff securely?

Issue a special token that has both the support agent's id and the target user's id (for example an `act` claim). Log every impersonation start and every action with both ids. Limit it to some roles, make it short-lived, block dangerous actions like password changes, and show a banner in the UI. Never just give staff the user's password or normal token.

## 339: How does the ValidationPipe actually validate, and what does that mean for performance?

It uses `class-transformer`'s `plainToInstance` to build the DTO class, then `class-validator`'s `validate` walks the metadata of each decorator. Deep nested arrays with many items mean many checks per request. Use `@ArrayMaxSize` and body size limits so one request can't create millions of objects.

## 340: How can class-transformer be abused with prototype pollution?

Older versions of some libraries let keys like `__proto__` or `constructor.prototype` change object prototypes, which can change app behavior globally. Keep class-transformer and class-validator updated, use `whitelist: true` so unknown keys are dropped, and on Fastify keep the default `onProtoPoisoning: 'error'`. Don't use deep merge helpers on raw request data.

## 341: Why is validating only the DTO not enough for a PATCH endpoint?

With `PartialType`, every field is optional, so empty objects or `null` values may pass. Also, the DTO says nothing about whether this user may change these fields on this record. Check for an empty update, decide how `null` is handled, and run field-level authorization after validation.

## 342: How do you validate a discriminated union body in class-validator?

Use `@Type` with a `discriminator` so the right class is built for each variant, and keep `whitelist` so each variant's fields are checked.

```ts
export class PaymentDto {
  @ValidateNested()
  @Type(() => BasePayment, {
    keepDiscriminatorProperty: true,
    discriminator: {
      property: "kind",
      subTypes: [
        { value: CardPayment, name: "card" },
        { value: BankPayment, name: "bank" },
      ],
    },
  })
  method: CardPayment | BankPayment;
}
```

## 343: When would you use Standard Schema validation in Nest 12 instead of class-validator?

When you already use Zod or Valibot schemas shared with the frontend, or want stricter parsing (Zod objects strip unknown keys by default, and `.strict()` rejects them). Nest 12 lets you pass `schema` in `@Body()` and use `StandardSchemaValidationPipe`. Security-wise both work; the important part is that every input goes through one of them, with lengths and limits set.

## 344: How do you make sure no route accepts an unvalidated body by mistake?

Keep the `ValidationPipe` global and add a lint rule or a test that fails when a handler uses `@Body()` with a type that isn't a class (like `any`, an interface, or `Record<string, unknown>`). Interfaces have no runtime metadata, so the pipe silently skips them.

## 345: Why does ValidationPipe skip validation when the parameter type is an interface?

TypeScript interfaces disappear at runtime. The pipe reads `metatype` from the emitted design metadata, and for an interface that's `Object`. The pipe skips primitive and `Object` metatypes, so the body passes through untouched. Always use classes (or Standard Schema) for DTOs.

## 346: How can serialization leak data through relations?

If an entity loads relations like `user.organization.members`, `ClassSerializerInterceptor` serializes them too, along with fields you only excluded on the top-level class. Each related class needs its own `@Exclude` rules, and only plain-object relations bypass them completely. Use response DTOs built on purpose instead of returning ORM entities.

## 347: Why are dedicated response DTOs safer than returning entities?

Entities change when the database changes. A new column like `resetToken` gets returned the next day without anyone noticing. A response DTO lists exactly what goes out, and changes to it show up in code review. It also avoids lazy loading or circular data surprises.

## 348: What is a "BOLA" bug in an API and how do you design to avoid it?

Broken object level authorization, the API version of IDOR, is first on the OWASP API Security Top 10. Design so every data access goes through a function that takes the current user or tenant as a required argument, for example `findInvoice(user, id)`. Then a missing check becomes a type error, not a silent leak.

## 349: What is BFLA and how does it show up in Nest?

Broken function level authorization: a normal user calls an admin function, like `POST /users/:id/role`. In Nest it happens when an admin controller is missing `@Roles`, or a route was added to a normal controller. Put admin routes in separate controllers with a class-level guard, and test that each admin route rejects normal users.

## 350: How would you scan your Nest routes to find missing authorization?

At startup or in a test, use `DiscoveryService` and `MetadataScanner` to list every controller method and its metadata. Fail the build if a route has neither `@Public()` nor any roles or policies metadata.

```ts
for (const wrapper of discovery.getControllers()) {
  const proto = Object.getPrototypeOf(wrapper.instance);
  for (const name of scanner.getAllMethodNames(proto)) {
    const handler = proto[name];
    const isPublic = reflector.getAllAndOverride(IS_PUBLIC_KEY, [
      handler,
      wrapper.metatype,
    ]);
    const roles = reflector.getAllAndOverride(Roles, [
      handler,
      wrapper.metatype,
    ]);
    if (!isPublic && !roles) missing.push(`${wrapper.name}.${name}`);
  }
}
```

## 351: How does Helmet's default CSP differ for an API compared to a website?

For a JSON API, the CSP header barely matters because browsers don't render JSON as a page. A strict policy like `default-src 'none'; frame-ancestors 'none'` is a safe default there. For a site that renders HTML, the CSP needs real work: nonces or hashes for scripts, no `unsafe-inline` for scripts, and a reporting endpoint.

## 352: How do you use CSP nonces in a Nest app that renders HTML?

Generate a nonce per request in middleware, pass it to Helmet as a function, and give it to the template.

```ts
app.use((req, res, next) => {
  res.locals.cspNonce = randomBytes(16).toString("base64");
  next();
});
app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        scriptSrc: [
          "'self'",
          (_req, res) => `'nonce-${(res as any).locals.cspNonce}'`,
        ],
      },
    },
  }),
);
```

Templates then add `nonce="{{cspNonce}}"` to their script tags.

## 353: How do you roll out a strict CSP without breaking a live site?

Start with `Content-Security-Policy-Report-Only` and a reporting endpoint, collect violations for a while, fix them, then switch to the enforcing header. Helmet supports `reportOnly: true`. Keep the reporting endpoint rate-limited because anyone can post to it.

## 354: Why is a dynamic CORS origin function a common source of bugs?

People write checks like `origin.endsWith('example.com')`, which also matches `evilexample.com`, or accept `null` as the origin, which sandboxed iframes and some redirects send. Parse the origin with `new URL()`, compare the full hostname, require `https`, and don't allow `null` when credentials are on.

## 355: What should the Vary header be when CORS origins are dynamic?

`Vary: Origin`. Without it, a CDN or browser cache might store a response with `Access-Control-Allow-Origin: https://a.com` and serve it to `https://b.com`, either breaking it or exposing it. The `cors` package used by Nest sets `Vary: Origin` when the origin isn't a fixed string.

## 356: How do you protect a cookie-based API against CSRF without tokens?

Check `Origin` (or `Referer` as fallback) on every state-changing request and compare it to an allowlist, and also look at `Sec-Fetch-Site`. Combined with `SameSite=Lax` or `Strict` cookies and requiring `Content-Type: application/json` (which forces a CORS preflight for cross-site requests), this blocks CSRF in modern browsers.

```ts
@Injectable()
export class OriginGuard implements CanActivate {
  canActivate(ctx: ExecutionContext) {
    const req = ctx.switchToHttp().getRequest();
    if (["GET", "HEAD", "OPTIONS"].includes(req.method)) return true;
    const site = req.headers["sec-fetch-site"];
    if (site && site !== "same-origin" && site !== "same-site") return false;
    return !req.headers.origin || ALLOWED.has(req.headers.origin);
  }
}
```

## 357: Why does requiring a JSON content type help against CSRF?

HTML forms can only send `application/x-www-form-urlencoded`, `multipart/form-data` or `text/plain` without a preflight. A cross-site `fetch` with `Content-Type: application/json` triggers a CORS preflight, which your CORS policy rejects. So if the API refuses other content types on unsafe methods, simple CSRF can't reach it. Make sure the body parser doesn't also accept `text/plain` as JSON.

## 358: What is login CSRF and how do you prevent it?

The attacker logs the victim into the attacker's account without them noticing. The victim then adds data (like a credit card) to the attacker's account. Protect the login form with a CSRF token or origin check too, and use the OAuth `state` parameter for social login.

## 359: How would you implement step-up authentication for sensitive actions?

Record when the user last confirmed their password or MFA (an `auth_time` claim or a session field). For actions like changing email or payout details, a guard checks that this happened in the last few minutes, and otherwise returns a specific error that makes the client ask for MFA again.

```ts
@Injectable()
export class RecentAuthGuard implements CanActivate {
  canActivate(ctx: ExecutionContext) {
    const { user } = ctx.switchToHttp().getRequest();
    if (Date.now() / 1000 - user.auth_time > 300) {
      throw new UnauthorizedException({
        message: "Re-authentication required",
        errorCode: "STEP_UP_REQUIRED",
      });
    }
    return true;
  }
}
```

## 360: How do you implement TOTP MFA securely?

Generate a secret per user, show it as a QR code once, and confirm setup with a first code. Store the secret encrypted, not hashed, because you need it to check codes. Allow a small time window, block reuse of the same code within that window, rate limit attempts, and give recovery codes stored as hashes.

## 361: How do you design account recovery without making it the weakest link?

Recovery is often easier to attack than login. Use single-use, short-lived, hashed tokens sent to a verified channel, require MFA or a recovery code for accounts with MFA, notify the user on all channels when recovery happens, and add a delay or manual review for high-value accounts. Don't let support staff reset MFA based on easy-to-find facts.

## 362: Why should key material for encryption not be stored in the same database as encrypted data?

If someone dumps the database, they get both the ciphertext and the key, and encryption adds nothing. Keep keys in a KMS (AWS KMS, Google Cloud KMS, Azure Key Vault) or Vault, and give only the app's runtime identity permission to use them.

## 363: What is envelope encryption?

You encrypt data with a random data key (DEK), then encrypt the DEK with a master key (KEK) in a KMS, and store the encrypted DEK next to the data. To decrypt, you ask the KMS to decrypt the DEK. The master key never leaves the KMS, rotating it only needs re-wrapping DEKs, and you avoid a KMS call for every row if you cache DEKs briefly.

## 364: How would you rotate an application-level encryption key?

Store a key id with each encrypted value, for example `v2:iv:tag:data`. Decrypt with the key that matches the id, and always encrypt with the newest key. A background job re-encrypts old rows in batches. When no rows use the old key, retire it.

## 365: How do you enforce TLS between Nest and the database?

Use the driver's SSL options and verify the server certificate. Don't set `rejectUnauthorized: false` in production, which turns off the check and allows man-in-the-middle attacks.

```ts
TypeOrmModule.forRoot({
  type: "postgres",
  url: process.env.DATABASE_URL,
  ssl: {
    ca: fs.readFileSync("certs/rds-ca.pem").toString(),
    rejectUnauthorized: true,
  },
});
```

For Prisma, add `sslmode=verify-full` and the CA path in the connection string.

## 366: When should traffic behind the load balancer also use TLS?

When the internal network isn't fully trusted: shared clusters, multi-tenant cloud networks, compliance rules like PCI DSS, or any setup where other workloads could sniff traffic. A service mesh with automatic mTLS makes this easy without changing Nest code.

## 367: How do you build a SQL injection-safe dynamic filter API in TypeORM?

Map each allowed filter to a known column and operator, and pass all values as parameters with unique names.

```ts
const FILTERS = {
  status: (qb, v, i) =>
    qb.andWhere(`o.status = :status${i}`, { [`status${i}`]: v }),
  minTotal: (qb, v, i) =>
    qb.andWhere(`o.total >= :min${i}`, { [`min${i}`]: Number(v) }),
} as const;

for (const [i, [key, value]] of Object.entries(query.filters).entries()) {
  const apply = FILTERS[key as keyof typeof FILTERS];
  if (!apply) throw new BadRequestException(`Unknown filter ${key}`);
  apply(qb, value, i);
}
```

Never let users send raw column names, operators or SQL fragments.

## 368: How can Prisma.raw or $queryRawUnsafe sneak injection into a "safe" Prisma codebase?

Developers use `Prisma.raw()` to insert a column name or `$queryRawUnsafe` for a dynamic table, and then a user value slips in. Search the code for these and put a lint rule on them. If you must use dynamic identifiers, map them through an allowlist first.

## 369: Can Prisma's where input be abused if you pass request data directly?

Yes. If you pass `dto.where` straight into `findMany`, a client can send filters on fields it shouldn't see, like `{ passwordHash: { startsWith: '$2b' } }`, and learn data one character at a time from what comes back. Build the `where` object from known fields only.

## 370: How do NoSQL injection risks look with Mongoose populate and aggregation?

User input in `$lookup`, `$expr`, `$function` or a `populate` path can expose other collections or run code. Never let clients choose collection names, field paths or pipeline stages. For search, map input to fixed stages and pass only values, and turn off server-side JavaScript in MongoDB if you don't need it.

## 371: Why is regex search with user input risky in MongoDB?

If you build `new RegExp(userInput)`, users can send patterns that are slow to run (ReDoS on the database) or that match far more than intended, like `.*`. Escape the input before building the regex, cap its length, and prefer text indexes or prefix search with an index.

```ts
const escaped = input.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
User.find({ name: { $regex: `^${escaped}`, $options: "i" } });
```

## 372: How do you prevent header injection when setting values from user input?

Node rejects header values with newline characters, which blocks classic response splitting. Still, validate values you put in headers like `Content-Disposition` filenames, because quotes and odd characters can break parsing. Encode filenames with RFC 5987 (`filename*=UTF-8''...`) and strip control characters.

## 373: What is server-side template injection and can it happen in Nest?

If a Nest app renders views (Handlebars, Pug, EJS) and builds the template string itself from user input, the user can run template code. Always pass user data as variables to a fixed template, never compile templates from user input. The same goes for email templates built in services.

## 374: How do you prevent CSV or formula injection in exports?

When users open a CSV in Excel, cells starting with `=`, `+`, `-`, `@`, tab or carriage return can run formulas. Prefix such values with a single quote or a space when you export.

```ts
const safeCell = (v: string) => (/^[=+\-@\t\r]/.test(v) ? `'${v}` : v);
```

## 375: Why are SVG uploads especially risky?

SVG is XML that can contain `<script>` and event handlers. If served from your origin as `image/svg+xml`, it runs like an HTML page. Either reject SVG, sanitize it with an SVG-aware sanitizer like DOMPurify, convert it to PNG, or serve it from a separate domain with `Content-Disposition: attachment`.

## 376: How do you safely process uploaded images?

Re-encode them with a library like `sharp`, which strips metadata (including GPS data) and blocks some file-format tricks. Limit pixel dimensions, since a small compressed file can expand into a huge image in memory (a decompression bomb). `sharp` has a `limitInputPixels` option for this.

## 377: How do you protect against zip bombs when users upload archives?

Don't trust the archive's own size fields. Extract in a streaming way and stop when total extracted bytes, file count or compression ratio pass a limit. Reject entries with absolute paths or `..` to avoid "zip slip" path traversal. Do it in a worker with memory limits, not in the request handler.

## 378: How would you design direct-to-S3 uploads securely from Nest?

Nest creates a presigned POST (or PUT) URL with strict conditions: exact key chosen by the server, content type, and a `content-length-range`. The client uploads directly to S3. An S3 event or a callback tells Nest the upload is done, and Nest checks the object (size, type, malware scan) before linking it to the user's data.

## 379: How do exception filters interact with errors from guards and interceptors?

Exceptions thrown in guards, interceptors, pipes and handlers all go to the exception filters. Errors in middleware go to filters too in Nest. But errors thrown before the Nest router (for example inside an Express middleware added with `app.use`) go to Express's error handler, which may print stack traces in development mode. Make sure those paths also end in safe responses.

## 380: How do you return consistent error codes without leaking details?

Use a small set of stable codes clients can rely on (`INVALID_CREDENTIALS`, `RATE_LIMITED`, `VALIDATION_FAILED`), log the real cause with the request id, and never include raw exception messages from libraries. In Nest 12 you can pass `errorCode` in `HttpException` options and have your global filter add it to every response.

## 381: Why can validation error messages leak information?

Messages like "role must be one of: user, admin, superadmin" reveal hidden enum values and internal field names. Errors from nested DTOs also show your internal structure. For public APIs, review messages, or use an `exceptionFactory` that returns field names and short codes only.

## 382: How do you handle errors from a third-party API without leaking its details?

Catch the error at the client wrapper, log the status and a safe part of the body, and throw your own exception, usually `BadGatewayException` or `ServiceUnavailableException`. Never forward the third-party error message, which can include their internal URLs, request ids or even your API key in some badly built SDKs.

## 383: How do you make security logs useful for incident response?

Use structured JSON with consistent field names, a request id and a user id on every line, and UTC timestamps. Ship logs to a central store that app admins can't delete. Keep them long enough for your detection time (often 90 days or more). Write runbooks for common queries like "all actions by this user in the last 24 hours".

## 384: How do you make audit logs tamper-evident?

Write them to append-only storage (like S3 with Object Lock, or a separate database where the app only has insert rights). You can also chain entries by storing a hash of the previous entry in each row, so deleting or changing one breaks the chain. Check the chain on a schedule.

## 385: How do you avoid logging personal data while keeping logs useful?

Log stable ids instead of names and emails, hash or mask values you need for matching (like the last 4 digits), redact known fields at the logger level, and review new log lines in code review. GDPR and similar laws treat logs as personal data too, so they need retention limits.

## 386: Why do guards not run on WebSocket handleConnection, and what's the impact?

`handleConnection` is a lifecycle hook, not a message handler, so Nest doesn't run the guard and pipe chain for it. If you only put `@UseGuards` on message handlers, unauthenticated clients can still connect, hold sockets open and receive broadcasts to rooms they're in. Authenticate in Socket.IO middleware or `handleConnection` and disconnect failures.

## 387: How do you handle token expiry on a long-lived WebSocket connection?

A socket authenticated at connect time stays open after the token expires. Store the expiry on `client.data`, check it in the message guard, and either disconnect or ask the client to send a fresh token over a `reauth` event. Also disconnect sockets when the user logs out or is banned, using a Redis pub/sub event across instances.

## 388: How do you rate limit WebSocket messages?

`ThrottlerGuard` is built around HTTP. For gateways, extend it and override `getTracker` and how it reads the request, or write a small guard with a token bucket per socket or per user in Redis. Also set Socket.IO's `maxHttpBufferSize` to limit message size.

```ts
@WebSocketGateway({ maxHttpBufferSize: 64 * 1024 })
```

## 389: What is cross-site WebSocket hijacking?

A malicious page opens a WebSocket to your server from the victim's browser. The browser sends cookies with the handshake, and WebSockets aren't blocked by CORS. If your gateway authenticates with cookies only, the attacker's page gets an authenticated socket. Check the `Origin` header in the handshake, or require a token sent in the handshake auth payload.

## 390: How do you scale secure broadcasts across many gateway instances?

Use the Socket.IO Redis adapter so instances share rooms. Authorization still happens when a socket joins a room, but also make sure server code that emits to a room only includes data that every member may see. Don't emit full records and rely on clients to filter.

## 391: How do you protect GraphQL against expensive list arguments?

Put a hard max on `first`, `take` or `limit` arguments in the args DTO, and make complexity depend on them. Without limits, `users(first: 1000000) { posts(first: 1000) { ... } }` multiplies into billions of resolver calls.

```ts
@ArgsType()
export class PageArgs {
  @Field(() => Int, { defaultValue: 20 })
  @Min(1)
  @Max(100)
  take: number;
}
```

## 392: What are persisted queries and how do they help security?

The client sends a hash of a known query instead of the query text. With an allowlist (sometimes called trusted documents), the server only runs queries that were registered at build time, so attackers can't send arbitrary queries. It's a strong defense for first-party clients but doesn't fit public APIs.

## 393: How does the N+1 problem relate to GraphQL DoS?

A query that lists 100 users, each with posts, can cause 101 database queries, or many more with deeper nesting. Attackers can use that to load your database. DataLoader batches the calls, and complexity limits stop the worst queries, but both are needed.

## 394: How do you hide GraphQL error details in production?

Use `formatError` to remove stack traces and internal messages for unknown errors while keeping your own error codes.

```ts
GraphQLModule.forRoot<ApolloDriverConfig>({
  driver: ApolloDriver,
  includeStacktraceInErrorResponses: false,
  formatError: (formatted, error) => {
    const code = formatted.extensions?.code;
    if (code === "INTERNAL_SERVER_ERROR") {
      return { message: "Internal server error", extensions: { code } };
    }
    return formatted;
  },
});
```

## 395: What is GraphQL field suggestion leakage?

When a query has a typo, servers often reply "Did you mean `secretAdminField`?", which leaks field names even with introspection off. Some setups remove these suggestions in `formatError` or with a plugin. Treat schema secrecy as a weak control anyway and rely on authorization.

## 396: How do you make sure field resolvers check authorization, not just the root query?

A user may access `order(id)` legitimately, but `order.customer.paymentMethods` might be off limits. Each `@ResolveField` that returns sensitive data needs its own check, or the parent type must only expose safe fields. Guards at class level on the resolver apply to its field resolvers too, so plan which resolver class owns each field.

## 397: Do Nest guards run for GraphQL field resolvers?

By default, guards, interceptors and filters don't run for `@ResolveField` methods, for performance. You can turn them on with `fieldResolverEnhancers: ['guards', 'interceptors', 'filters']` in the GraphQL module options. Without it, field-level checks must be done inside the resolver or with field middleware.

## 398: How does CSRF apply to GraphQL APIs?

If you use cookie auth and accept GET queries or `multipart/form-data` (for uploads), a cross-site form can send a mutation. Apollo Server has `csrfPrevention` turned on by default in recent versions, which requires a preflight-triggering header. Don't turn it off, and avoid enabling GraphQL uploads unless you need them.

## 399: How do you authenticate gRPC microservices in Nest?

Use TLS or mTLS through gRPC credentials, and pass a token in metadata. A guard reads the metadata with `switchToRpc().getContext()`.

```ts
app.connectMicroservice<MicroserviceOptions>({
  transport: Transport.GRPC,
  options: {
    package: "orders",
    protoPath: join(__dirname, "orders.proto"),
    url: "0.0.0.0:5000",
    credentials: ServerCredentials.createSsl(
      caCert,
      [{ private_key: key, cert_chain: cert }],
      true,
    ),
  },
});
```

The last argument `true` makes the server require client certificates.

## 400: Why is a message queue not a trust boundary by itself?

Any service with publish rights on a queue can send any message. If the payments service trusts every message on `refunds`, a bug or breach in a less critical service that can also publish there becomes a payments problem. Lock down publish rights per queue or topic and sign or authenticate important messages.

## 401: How do you sign messages between microservices?

Add a JWT or HMAC to the message, created by the sender with its own key, and verify it in a guard on the receiver. Include the message id, the sender, a timestamp and a hash of the payload, so messages can't be changed or replayed later. Reject old timestamps and keep a short list of seen ids for replay protection.

## 402: What is the confused deputy problem in microservices?

Service A has permission to do something, and B asks A to do it for a user who isn't allowed. If A only checks "is B allowed to call me", the user gets access through B. Pass the end user's identity along and have A check the user's permissions too, not only the calling service.

## 403: How does a service mesh change what Nest needs to do for security?

A mesh like Istio or Linkerd gives automatic mTLS between pods, service identity and network policies, so Nest doesn't handle TLS internally. Nest still needs user-level authorization, input validation and business rules. Some teams also read the caller's service identity from mesh headers, but only when the mesh guarantees those headers can't be set by the caller.

## 404: How do you use PostgreSQL row-level security with Nest for multi-tenancy?

Turn on RLS for tenant tables with a policy that compares `tenant_id` to a session setting. In each request, set the setting inside the transaction before running queries.

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

```ts
await prisma.$transaction(async (tx) => {
  await tx.$executeRaw`SELECT set_config('app.tenant_id', ${tenantId}, true)`;
  return tx.invoice.findMany();
});
```

The third argument `true` keeps the setting local to the transaction, so pooled connections don't keep it.

## 405: What breaks RLS-based tenant isolation?

The app connects as the table owner or a superuser, which bypass RLS unless you use `FORCE ROW LEVEL SECURITY`. Settings set without the transaction-local flag leak to the next request on the same pooled connection. Background jobs forget to set the tenant. Use a separate, non-owner database role for the app and test these cases.

## 406: Why are request-scoped providers a common but costly way to do multi-tenancy?

Making a `TenantConnection` provider `Scope.REQUEST` makes every provider that depends on it request-scoped too, so Nest builds large parts of the graph per request. Durable providers with a custom `ContextIdStrategy` let Nest build one tree per tenant instead of per request, which is much cheaper.

## 407: How do durable providers work for multi-tenancy?

You write a `ContextIdStrategy` that groups requests by tenant id and returns a shared context id for each tenant. Providers marked `durable: true` are created once per tenant and reused.

```ts
export class TenantContextStrategy implements ContextIdStrategy {
  private tenants = new Map<string, ContextId>();

  attach(contextId: ContextId, request: Request) {
    const tenantId = request.headers["x-tenant-id"] as string;
    let tenantSubTreeId = this.tenants.get(tenantId);
    if (!tenantSubTreeId) {
      tenantSubTreeId = ContextIdFactory.create();
      this.tenants.set(tenantId, tenantSubTreeId);
    }
    return {
      resolve: (info) => (info.isTreeDurable ? tenantSubTreeId : contextId),
      payload: { tenantId },
    };
  }
}
```

The tenant id here comes from a header for brevity; in real code read it from something verified, and limit the map size so made-up tenant ids can't grow it forever.

## 408: How do you keep caches from leaking data across tenants or users?

Every cache key must include the tenant id and, for user-specific data, the user id. The Nest `CacheInterceptor` keys by URL by default, so it can serve one user's response to another when the URL is the same. Override `trackBy` or don't cache authenticated responses with it. Also send `Cache-Control: private` or `no-store` so CDNs don't cache them.

## 409: How do you isolate background jobs per tenant?

Put the tenant id in every job payload, set it in the CLS context at the start of the job, and run the same tenant filters as HTTP requests. Never let a job process "all tenants" with the same code path that normal requests use without making that explicit. Fair queues per tenant also stop one tenant from starving others.

## 410: What are the trade-offs of SameSite=Strict for session cookies?

`Strict` gives the best CSRF protection, but users who click a link to your site from email or another site arrive logged out on that first request, which feels broken. A common setup is a `Lax` session cookie for navigation plus a `Strict` cookie checked for sensitive actions, or `Lax` plus CSRF tokens.

## 411: When do you need SameSite=None and what does it cost?

When the frontend and API are on different sites (not just different subdomains) and the API uses cookies, for example an embedded widget. It requires `Secure`, gives no CSRF protection, and third-party cookies are blocked or limited in many browsers. Prefer putting the API on a subdomain of the app's site, or use tokens instead.

## 412: What are CHIPS (partitioned cookies)?

Cookies with the `Partitioned` attribute are stored per top-level site, so a third-party embed gets a separate cookie jar on each site that embeds it. That's how embedded widgets can keep state while browsers block normal third-party cookies. Express's `res.cookie` supports the `partitioned` option in recent versions.

## 413: How can a subdomain attack your cookies?

A page on `evil.example.com` (for example a user-hosted site or a taken-over abandoned subdomain) can set cookies for `.example.com`, which your app on `app.example.com` will receive. It can overwrite or "toss" session or CSRF cookies. Use the `__Host-` prefix, don't set `Domain` unless needed, and watch for dangling DNS records.

## 414: How does Express's JSON body parser protect against huge payloads, and where does it fall short?

It checks `Content-Length` and stops reading once the limit is passed, returning `413`. But many small requests, deeply nested JSON within the limit, or very large arrays of small items can still be expensive to parse and validate. Combine size limits with rate limits and `@ArrayMaxSize` on DTOs.

## 415: How do slowloris attacks affect Node servers and how do you stop them?

The attacker opens many connections and sends headers very slowly, keeping sockets open. Node's `headersTimeout` and `requestTimeout` help, but the best defense is a reverse proxy (Nginx, a cloud load balancer) that buffers requests and only passes complete ones to Node.

## 416: How do you find event loop blocking that attackers could trigger?

Measure event loop delay with `perf_hooks.monitorEventLoopDelay()` and alert when it spikes. Profile with `--cpu-prof` or Clinic.js under load. Usual suspects are sync crypto, big `JSON.parse` or `JSON.stringify` calls, bad regexes and large sorts. Move heavy work to worker threads or queues.

## 417: How do you protect expensive endpoints like exports or reports from abuse?

Move them to a queue (for example BullMQ) and return a job id, limit how many jobs one user or tenant can have running, put stricter rate limits on the trigger endpoint, and cap the size of results. That keeps request threads free and turns a DoS attempt into a long queue for one user only.

## 418: How do you add per-tenant quotas, not just rate limits?

Rate limits protect short-term load; quotas limit total use per plan, like 100,000 API calls a month. Count usage in Redis or a database with atomic increments, check in a guard, and return `429` or `402` with a clear code. Run billing-grade counting asynchronously from logs if exactness matters more than real-time blocking.

## 419: How would you respond to a compromised npm package in your dependency tree?

Find which versions you installed and when (lockfile history, CI logs). Pin or remove the bad version, rebuild from a clean lockfile, and rotate every secret that was available where the package ran: CI tokens, npm tokens, cloud keys and `.env` values on developer machines. Check logs for unusual outgoing connections. Treat it as an incident, not just an upgrade.

## 420: How do you reduce the chance of installing a freshly hijacked package version?

Use lockfiles and `npm ci`, wait a few days before taking new versions (pnpm has a `minimumReleaseAge` setting, and Renovate has a similar delay option), block install scripts by default, and review dependency updates. Most malicious versions are found and removed within days, so a short delay avoids a lot.

## 421: What is dependency confusion?

If your company uses private packages like `@acme/utils` or unscoped `acme-utils`, an attacker can publish a public package with the same name and a higher version. A misconfigured install pulls the public one. Use scoped names tied to your private registry in `.npmrc`, and claim your scope on the public registry.

## 422: What is an SBOM and why would a Nest team generate one?

A software bill of materials lists every package and version in your build. When a new vulnerability is announced, you can check right away whether you're affected. Tools like `npm sbom` (built into npm), CycloneDX or Syft can generate it in CI.

## 423: How do you handle a vulnerability in a transitive dependency with no fix from the direct dependency?

Check if it's reachable from your code at all. If it is, use `overrides` in `package.json` (or `pnpm.overrides`) to force a fixed version, then run tests. Open an issue or PR on the direct dependency. Document the override so it gets removed later.

```json
{
  "overrides": {
    "vulnerable-lib": "^2.4.1"
  }
}
```

## 424: Why is npm audit output often noisy, and how do you make it useful?

Many reports are for dev-only tools or code paths you never call, and some are disputed. Teams that block every build on every finding end up ignoring the tool. Separate prod and dev dependencies, gate on high severity in production packages, use reachability analysis from tools like Snyk or Socket where available, and track accepted risks with an expiry date.

## 425: How do you protect the CI pipeline as part of supply-chain security?

Pin third-party GitHub Actions to a commit SHA, give the workflow token only the permissions it needs, don't expose secrets to pull requests from forks, use OIDC to get short-lived cloud credentials instead of stored keys, and publish packages with provenance. A compromised CI runner can ship code directly to production.

## 426: How would you map a NestJS codebase to OWASP ASVS for a security review?

ASVS (Application Security Verification Standard) is a detailed checklist, unlike the Top 10. Pick a level (L1 for most apps, L2 for sensitive data), then go chapter by chapter: authentication (strategies, password rules), session management (cookies, token lifetimes), access control (guards, ownership checks), validation (pipes), cryptography, error handling (filters), logging, data protection, and configuration. For each item, find the code or test that proves it.

## 427: What should an e2e security test suite for a Nest API cover?

Unauthenticated access to every non-public route returns 401, wrong-role access returns 403, cross-user and cross-tenant access returns 404, unknown fields are rejected, oversized bodies return 413, rate limits return 429, responses don't contain secrets, security headers are set, CORS rejects unknown origins, and expired or tampered tokens are rejected.

## 428: How do you generate auth tests for every route automatically?

Use the route discovery approach (with `DiscoveryService` or the Swagger document from `SwaggerModule.createDocument`) to list routes, then for each non-public route send a request without a token and assert `401`. This catches new routes that someone forgot to protect.

```ts
const doc = SwaggerModule.createDocument(app, new DocumentBuilder().build());
for (const [path, methods] of Object.entries(doc.paths)) {
  for (const method of Object.keys(methods)) {
    if (PUBLIC.has(`${method} ${path}`)) continue;
    const url = path.replace(
      /{[^}]+}/g,
      "00000000-0000-0000-0000-000000000000",
    );
    await (request(server) as any)[method](url).expect(401);
  }
}
```

## 429: How do you test JWT tampering in e2e tests?

Take a valid token, change one character in the payload, and expect `401`. Also try a token signed with a different secret, an expired one, one with `alg: none`, and one with the wrong `aud`. These tests protect against someone later loosening verify options.

```ts
const [h, p, s] = validToken.split(".");
const payload = JSON.parse(Buffer.from(p, "base64url").toString());
payload.role = "admin";
const forged = [
  h,
  Buffer.from(JSON.stringify(payload)).toString("base64url"),
  s,
].join(".");
await request(server)
  .get("/admin/stats")
  .set("Authorization", `Bearer ${forged}`)
  .expect(401);
```

## 430: How would you fuzz a Nest API?

Use the OpenAPI document with a tool like Schemathesis or RESTler to send many generated inputs: wrong types, huge strings, boundary numbers, unexpected nulls. Look for 500s, slow responses and data in errors. 500s usually point to missing validation or unhandled cases.

## 431: A user reports they can see another company's invoices. How do you investigate?

Reproduce with two tenants in a test environment. Check the route's guards, how the tenant id is found, whether the service filters by tenant, caches keyed only by URL, and whether a background job wrote data with the wrong tenant. Search the access logs for other users who hit the same endpoint with ids outside their tenant to see if it was exploited. Fix the bug, add a regression test, and follow your data breach process.

## 432: Your logs show many failed logins across thousands of accounts from rotating IPs. What do you do?

That's credential stuffing. Short term: tighten per-account limits, add a CAPTCHA or proof-of-work after failures, block known bad IP ranges or ASNs at the WAF, and force resets for accounts that logged in successfully from those sources. Longer term: check passwords against breach lists, push MFA and passkeys, and alert on login success rate drops.

## 433: You find a JWT secret committed to a public repo six months ago. What's the plan?

Assume it's been used. Generate a new secret and deploy it, which logs everyone out. Remove the secret from the repo history (it's still public in forks and caches, so rotation is what really fixes it). Review logs for tokens with unusual claims or users. Add secret scanning to CI and pre-commit, and move the secret to a secret manager.

## 434: An endpoint returns 500 with a stack trace in production. What's wrong and how do you fix it?

Something bypasses the safe error path: a custom filter that returns `exception.stack`, Express's default error handler with `NODE_ENV` not set to production, or an error thrown in raw Express middleware. Set `NODE_ENV=production`, add a catch-all filter, and test that a forced error returns a generic body.

## 435: How would you secure an admin panel built into the same Nest app?

Put it under separate controllers with class-level role guards, require MFA and step-up auth for admin users, restrict it by network (VPN or IP allowlist) if possible, log every admin action to the audit log, and give admins narrow roles instead of one "superadmin". Consider a separate deployment so a bug in the public API can't reach admin routes.

## 436: How do you prevent privilege escalation through a "update my profile" endpoint?

Use a DTO with only the fields users may change, with `whitelist` and `forbidNonWhitelisted`. Never spread the body into the user entity. Update by the current user's id from the token, not an id from the body or URL. Add a test that sends `role`, `tenantId` and `emailVerified` and checks nothing changed.

## 437: How would you design secure file downloads for user documents?

Don't expose storage paths or public bucket URLs. A download route checks that the user may read the document, then returns a short-lived presigned URL (minutes, not days) or streams the file with `StreamableFile`. Set `Content-Disposition: attachment` and the correct type. Log downloads of sensitive documents.

```ts
@Get('documents/:id/download')
async download(@CurrentUser() user: User, @Param('id', ParseUUIDPipe) id: string) {
  const doc = await this.docs.findForUser(user, id); // throws 404 if not allowed
  return { url: await this.storage.presignGet(doc.key, { expiresIn: 300 }) };
}
```

## 438: What security concerns come with using Nest's built-in HttpModule for outgoing requests?

The main risks are SSRF when URLs come from users, missing timeouts that tie up resources, following redirects into internal networks, and logging full requests that include API keys. Set a default `timeout` and `maxRedirects` on `HttpModule.register`, validate target hosts, and redact auth headers in logs.

## 439: How do you secure Nest apps running in Kubernetes?

Run as non-root with a read-only root filesystem, drop Linux capabilities, set resource limits, use NetworkPolicies so pods only talk to what they need, load secrets from a secret manager or sealed secrets (not plain ConfigMaps), and use workload identity for cloud access. Liveness and health endpoints should not reveal versions or config.

## 440: What should a health check endpoint expose?

A simple `ok` for load balancers is enough publicly. Detailed checks (database, Redis, disk) are useful for operators but reveal internal names and versions, so put them on a separate port, an internal network path, or behind auth. `@nestjs/terminus` makes both easy.

## 441: How do you protect against secrets leaking through error tracking tools like Sentry?

Error trackers capture request headers, bodies, local variables and breadcrumbs. Use the SDK's `beforeSend` hook to strip `Authorization`, cookies and known sensitive fields, turn off sending default PII, and review a sample of real events. Limit who can view them; they often hold more data than your logs.

## 442: How would you handle GDPR "right to be forgotten" securely in a Nest app?

Build one deletion flow that removes or anonymizes the user's data across all stores (database, search index, caches, file storage, analytics), and record that it happened in the audit log without keeping the deleted data. Backups age out on their normal schedule. Require recent authentication to request it, and protect the admin version against abuse.

## 443: How do you think about trust boundaries when designing a new Nest feature?

Draw where data comes from and where it crosses into something that trusts it: browser to API, API to database, API to third parties, queue to worker. At each boundary ask: who can send data here, how is it authenticated, how is it validated, and what happens if it's bad. That quick threat model usually finds missing guards and validation before coding.

## 444: What is STRIDE and how would you apply it to a Nest login feature?

STRIDE stands for spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege. For login: spoofing (credential stuffing, so rate limits and MFA), tampering (token changes, so signature checks), repudiation (audit logs of logins), information disclosure (user enumeration, so generic errors), DoS (expensive hashing, so limits), elevation (role in token, so server-side checks).

## 445: What are the security trade-offs of putting roles and permissions in the JWT?

Pros: no database lookup per request, and other services can read them. Cons: changes don't apply until the token expires, tokens grow large with many permissions, and every service now depends on the token format. A middle ground is keeping roles in the token and looking up fine-grained permissions with a cache.

## 446: How do you design an API for both public consumers and internal services without weakening security?

Use separate auth types: user tokens, API keys for public consumers, and service tokens or mTLS for internal services. Don't give internal services a "bypass all checks" flag. Internal-only routes go in separate controllers, ideally on a separate port or deployment that isn't exposed through the public ingress.

## 447: Why should you avoid writing your own crypto, even in small helpers?

Small mistakes break everything: reusing an IV with GCM, comparing MACs with `===`, using ECB mode, deriving keys from passwords with a single SHA-256, or forgetting to check the auth tag. Use Node's `crypto` with standard modes, `jose` for JWT and JWE, and well-known libraries for passwords. Get crypto code reviewed by someone who knows it.

## 448: How would you add security checks to code review for a Nest team?

Keep a short checklist in the PR template: new routes have guards or `@Public()` with a reason, DTOs have limits, queries filter by user or tenant, no raw SQL with user input, no secrets in code or logs, response DTOs don't leak fields. Back it with automation: a route-coverage test, `npm audit`, secret scanning, and a static analyzer like Semgrep with Node rules.

## 449: How do you balance security with developer speed in a Nest codebase?

Make the safe path the easy path: a global auth guard with `@Public()` opt-out, a global `ValidationPipe` with strict defaults, base repositories that always add tenant filters, response DTOs generated from one place, and shared test helpers for auth tests. Developers then get security by default and only need to think hard about the exceptions.

## 450: If you had one week to improve the security of an existing Nest API, what would you do?

Day 1: check that every route has auth and ownership checks, and add a route-coverage test. Day 2: turn on strict `ValidationPipe` options and add limits to DTOs. Day 3: Helmet, CORS allowlist, cookie flags, body limits, rate limits on login and expensive routes. Day 4: secrets out of code, env validation, key rotation plan. Day 5: dependency audit, CI secret scanning, safe error filter, audit logging for sensitive actions. Then write down what's left as tickets.
