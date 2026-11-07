# Express.js Interview Questions and Answers

_Last updated: October 28, 2026_

450 Express.js interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for **Express 5** (5.x), which needs Node.js 18 or newer. A lot of projects still run Express 4, so when something works differently there (async errors, route path syntax, removed methods), the answer says so.

Code examples use JavaScript with CommonJS (`require`) unless the question is about ES modules or TypeScript. Third-party packages like `cors`, `helmet`, `multer` and `zod` are named in the examples where they are used.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Express.js?](#1-what-is-expressjs)
- [2: Why would you use Express instead of the plain `http` module?](#2-why-would-you-use-express-instead-of-the-plain-http-module)
- [3: How do you install Express?](#3-how-do-you-install-express)
- [4: What does a minimal Express app look like?](#4-what-does-a-minimal-express-app-look-like)
- [5: How do you use Express with ES modules instead of CommonJS?](#5-how-do-you-use-express-with-es-modules-instead-of-commonjs)
- [6: What is the `app` object?](#6-what-is-the-app-object)
- [7: What does `app.listen()` do?](#7-what-does-applisten-do)
- [8: What is routing in Express?](#8-what-is-routing-in-express)
- [9: Which HTTP methods can you define routes for?](#9-which-http-methods-can-you-define-routes-for)
- [10: What is the difference between PUT and PATCH in an Express API?](#10-what-is-the-difference-between-put-and-patch-in-an-express-api)
- [11: What are route parameters?](#11-what-are-route-parameters)
- [12: How do you read query string values?](#12-how-do-you-read-query-string-values)
- [13: What is the difference between `req.params` and `req.query`?](#13-what-is-the-difference-between-reqparams-and-reqquery)
- [14: What is `req.body` and how do you get it?](#14-what-is-reqbody-and-how-do-you-get-it)
- [15: What does `express.json()` do?](#15-what-does-expressjson-do)
- [16: What does `express.urlencoded()` do?](#16-what-does-expressurlencoded-do)
- [17: What is the request object (`req`)?](#17-what-is-the-request-object-req)
- [18: What is the response object (`res`)?](#18-what-is-the-response-object-res)
- [19: What is the difference between `res.send()` and `res.json()`?](#19-what-is-the-difference-between-ressend-and-resjson)
- [20: How do you set the response status code?](#20-how-do-you-set-the-response-status-code)
- [21: What does `res.sendStatus()` do?](#21-what-does-ressendstatus-do)
- [22: How do you redirect a request?](#22-how-do-you-redirect-a-request)
- [23: What is middleware in Express?](#23-what-is-middleware-in-express)
- [24: What does `next()` do?](#24-what-does-next-do)
- [25: What does `app.use()` do?](#25-what-does-appuse-do)
- [26: Why does the order of middleware matter?](#26-why-does-the-order-of-middleware-matter)
- [27: What kinds of middleware are there in Express?](#27-what-kinds-of-middleware-are-there-in-express)
- [28: What is `express.Router()`?](#28-what-is-expressrouter)
- [29: Why split routes into routers?](#29-why-split-routes-into-routers)
- [30: How do you serve static files?](#30-how-do-you-serve-static-files)
- [31: How do you serve static files under a path prefix?](#31-how-do-you-serve-static-files-under-a-path-prefix)
- [32: Why use an absolute path with `express.static`?](#32-why-use-an-absolute-path-with-expressstatic)
- [33: How do you handle 404 Not Found in Express?](#33-how-do-you-handle-404-not-found-in-express)
- [34: How do you write an error-handling middleware?](#34-how-do-you-write-an-error-handling-middleware)
- [35: How do you pass an error to the error handler?](#35-how-do-you-pass-an-error-to-the-error-handler)
- [36: What does Express do with an error if you have no error handler?](#36-what-does-express-do-with-an-error-if-you-have-no-error-handler)
- [37: What is `NODE_ENV` and how does Express use it?](#37-what-is-node_env-and-how-does-express-use-it)
- [38: How do you read the port from an environment variable?](#38-how-do-you-read-the-port-from-an-environment-variable)
- [39: How do you load environment variables from a `.env` file?](#39-how-do-you-load-environment-variables-from-a-env-file)
- [40: How do you restart the server automatically during development?](#40-how-do-you-restart-the-server-automatically-during-development)
- [41: What is `express-generator`?](#41-what-is-express-generator)
- [42: How do you send HTML from Express?](#42-how-do-you-send-html-from-express)
- [43: What is a template engine?](#43-what-is-a-template-engine)
- [44: What does `res.render()` do?](#44-what-does-resrender-do)
- [45: What does `res.sendFile()` do?](#45-what-does-ressendfile-do)
- [46: What is the difference between `res.sendFile()` and `res.download()`?](#46-what-is-the-difference-between-ressendfile-and-resdownload)
- [47: How do you read request headers?](#47-how-do-you-read-request-headers)
- [48: How do you set response headers?](#48-how-do-you-set-response-headers)
- [49: How do you get the full URL path of a request?](#49-how-do-you-get-the-full-url-path-of-a-request)
- [50: How do you get the client IP address?](#50-how-do-you-get-the-client-ip-address)
- [51: What does `app.all()` do?](#51-what-does-appall-do)
- [52: What does `app.route()` do?](#52-what-does-approute-do)
- [53: Can a route have more than one handler?](#53-can-a-route-have-more-than-one-handler)
- [54: What is the difference between `app.use()` and `app.get()`?](#54-what-is-the-difference-between-appuse-and-appget)
- [55: How does path matching work with `app.use('/api', ...)`?](#55-how-does-path-matching-work-with-appuseapi-)
- [56: How do you match any path with a wildcard in Express 5?](#56-how-do-you-match-any-path-with-a-wildcard-in-express-5)
- [57: How do you write an optional route parameter in Express 5?](#57-how-do-you-write-an-optional-route-parameter-in-express-5)
- [58: Can you use regular expressions in route paths?](#58-can-you-use-regular-expressions-in-route-paths)
- [59: What does `req.method` contain?](#59-what-does-reqmethod-contain)
- [60: What does `res.end()` do?](#60-what-does-resend-do)
- [61: Can you send two responses for one request?](#61-can-you-send-two-responses-for-one-request)
- [62: What is `res.headersSent`?](#62-what-is-resheaderssent)
- [63: What are `app.locals` and `res.locals`?](#63-what-are-applocals-and-reslocals)
- [64: What are app settings and how do you change them?](#64-what-are-app-settings-and-how-do-you-change-them)
- [65: How do you remove the `X-Powered-By` header?](#65-how-do-you-remove-the-x-powered-by-header)
- [66: What do the `case sensitive routing` and `strict routing` settings do?](#66-what-do-the-case-sensitive-routing-and-strict-routing-settings-do)
- [67: What is CORS and how do you enable it in Express?](#67-what-is-cors-and-how-do-you-enable-it-in-express)
- [68: What is `morgan`?](#68-what-is-morgan)
- [69: What is `helmet`?](#69-what-is-helmet)
- [70: How do you read cookies in Express?](#70-how-do-you-read-cookies-in-express)
- [71: How do you set a cookie?](#71-how-do-you-set-a-cookie)
- [72: How do you delete a cookie?](#72-how-do-you-delete-a-cookie)
- [73: What are signed cookies?](#73-what-are-signed-cookies)
- [74: What is `express-session`?](#74-what-is-express-session)
- [75: How do you upload files in Express?](#75-how-do-you-upload-files-in-express)
- [76: What is REST and how does it map to Express routes?](#76-what-is-rest-and-how-does-it-map-to-express-routes)
- [77: Which status codes should a REST API in Express return?](#77-which-status-codes-should-a-rest-api-in-express-return)
- [78: How do you set the `Content-Type` of a response?](#78-how-do-you-set-the-content-type-of-a-response)
- [79: What does `req.is()` do?](#79-what-does-reqis-do)
- [80: What does `req.accepts()` do?](#80-what-does-reqaccepts-do)
- [81: What does `res.format()` do?](#81-what-does-resformat-do)
- [82: What does `req.protocol` contain?](#82-what-does-reqprotocol-contain)
- [83: What is the difference between `req.hostname` and `req.host`?](#83-what-is-the-difference-between-reqhostname-and-reqhost)
- [84: What is `req.subdomains`?](#84-what-is-reqsubdomains)
- [85: How do you test an Express API?](#85-how-do-you-test-an-express-api)
- [86: Why should you separate creating the app from starting the server?](#86-why-should-you-separate-creating-the-app-from-starting-the-server)
- [87: How do you add a health check endpoint?](#87-how-do-you-add-a-health-check-endpoint)
- [88: How do you see what Express is doing internally?](#88-how-do-you-see-what-express-is-doing-internally)
- [89: What is the difference between `req.originalUrl` and `req.url`?](#89-what-is-the-difference-between-reqoriginalurl-and-requrl)
- [90: How do you validate input in Express?](#90-how-do-you-validate-input-in-express)
- [91: What is `express-validator`?](#91-what-is-express-validator)
- [92: What does `express.raw()` do?](#92-what-does-expressraw-do)
- [93: What does `express.text()` do?](#93-what-does-expresstext-do)
- [94: Is `body-parser` still needed?](#94-is-body-parser-still-needed)
- [95: What is the difference between `res.json()` and `res.jsonp()`?](#95-what-is-the-difference-between-resjson-and-resjsonp)
- [96: How do you send a response with no content?](#96-how-do-you-send-a-response-with-no-content)
- [97: How do you return a `Location` header after creating a resource?](#97-how-do-you-return-a-location-header-after-creating-a-resource)
- [98: What is the request-response cycle in Express?](#98-what-is-the-request-response-cycle-in-express)
- [99: How do you organize an Express project?](#99-how-do-you-organize-an-express-project)
- [100: What is a controller in an Express app?](#100-what-is-a-controller-in-an-express-app)
- [101: What are the main differences between Express 4 and Express 5?](#101-what-are-the-main-differences-between-express-4-and-express-5)
- [102: How do you upgrade an app from Express 4 to Express 5?](#102-how-do-you-upgrade-an-app-from-express-4-to-express-5)
- [103: What is `req.param()` and why was it removed?](#103-what-is-reqparam-and-why-was-it-removed)
- [104: How do you mount one router inside another?](#104-how-do-you-mount-one-router-inside-another)
- [105: What does `mergeParams` do in `express.Router()`?](#105-what-does-mergeparams-do-in-expressrouter)
- [106: What does `next('route')` do?](#106-what-does-nextroute-do)
- [107: What does `next('router')` do?](#107-what-does-nextrouter-do)
- [108: What does `app.param()` do?](#108-what-does-appparam-do)
- [109: How do you write middleware that takes options?](#109-how-do-you-write-middleware-that-takes-options)
- [110: How do you add data to the request in middleware?](#110-how-do-you-add-data-to-the-request-in-middleware)
- [111: What is `compression` middleware?](#111-what-is-compression-middleware)
- [112: How do you use Express with TypeScript?](#112-how-do-you-use-express-with-typescript)
- [113: What does `res.attachment()` do?](#113-what-does-resattachment-do)
- [114: What does `res.vary()` do?](#114-what-does-resvary-do)
- [115: What is ETag and how does Express use it?](#115-what-is-etag-and-how-does-express-use-it)
- [116: What are `req.fresh` and `req.stale`?](#116-what-are-reqfresh-and-reqstale)
- [117: How do you set cache headers for static files?](#117-how-do-you-set-cache-headers-for-static-files)
- [118: What are the useful options of `express.static`?](#118-what-are-the-useful-options-of-expressstatic)
- [119: Can you serve files from more than one folder?](#119-can-you-serve-files-from-more-than-one-folder)
- [120: How do you serve a single page application (SPA) from Express?](#120-how-do-you-serve-a-single-page-application-spa-from-express)
- [121: How do you create an HTTPS server with Express?](#121-how-do-you-create-an-https-server-with-express)
- [122: What does `http.createServer(app)` have to do with Express?](#122-what-does-httpcreateserverapp-have-to-do-with-express)
- [123: What is the default value of `req.query` when there is no query string?](#123-what-is-the-default-value-of-reqquery-when-there-is-no-query-string)
- [124: How does Express parse nested query strings?](#124-how-does-express-parse-nested-query-strings)
- [125: How do you get a number out of a route parameter safely?](#125-how-do-you-get-a-number-out-of-a-route-parameter-safely)
- [126: What is `req.route`?](#126-what-is-reqroute)
- [127: What is `req.xhr`?](#127-what-is-reqxhr)
- [128: How do you return JSON with a custom format, like pretty printing?](#128-how-do-you-return-json-with-a-custom-format-like-pretty-printing)
- [129: What happens when a client sends invalid JSON?](#129-what-happens-when-a-client-sends-invalid-json)
- [130: What happens when the body is bigger than the limit?](#130-what-happens-when-the-body-is-bigger-than-the-limit)
- [131: How do you apply middleware to only some routes?](#131-how-do-you-apply-middleware-to-only-some-routes)
- [132: How do you run middleware for all routes except some?](#132-how-do-you-run-middleware-for-all-routes-except-some)
- [133: What is `res.locals` used for in an API?](#133-what-is-reslocals-used-for-in-an-api)
- [134: How do you return errors in a consistent format?](#134-how-do-you-return-errors-in-a-consistent-format)
- [135: How do you create an error with a status code?](#135-how-do-you-create-an-error-with-a-status-code)
- [136: What does `res.links()` do?](#136-what-does-reslinks-do)
- [137: How do you implement simple pagination?](#137-how-do-you-implement-simple-pagination)
- [138: What is the `views` setting?](#138-what-is-the-views-setting)
- [139: How do you use EJS with Express?](#139-how-do-you-use-ejs-with-express)
- [140: How do you use a template engine that has a different file extension?](#140-how-do-you-use-a-template-engine-that-has-a-different-file-extension)
- [141: What does `req.ips` contain?](#141-what-does-reqips-contain)
- [142: What is the difference between `app.get('/x')` and `app.get('x')`?](#142-what-is-the-difference-between-appgetx-and-appgetx)
- [143: What is `req.cookies` when you do not use `cookie-parser`?](#143-what-is-reqcookies-when-you-do-not-use-cookie-parser)
- [144: What is the difference between authentication and authorization in an Express app?](#144-what-is-the-difference-between-authentication-and-authorization-in-an-express-app)
- [145: How do you protect a route with a simple token check?](#145-how-do-you-protect-a-route-with-a-simple-token-check)
- [146: What is Passport.js?](#146-what-is-passportjs)
- [147: What does `res.append()` do?](#147-what-does-resappend-do)
- [148: How do you stop an Express server?](#148-how-do-you-stop-an-express-server)
- [149: Is Express still maintained?](#149-is-express-still-maintained)
- [150: What are some alternatives to Express?](#150-what-are-some-alternatives-to-express)

### Moderate Questions (151-300)

- [151: How did people handle async errors in Express 4, and do you still need that in Express 5?](#151-how-did-people-handle-async-errors-in-express-4-and-do-you-still-need-that-in-express-5)
- [152: Does Express 5 catch errors thrown inside callbacks or timers?](#152-does-express-5-catch-errors-thrown-inside-callbacks-or-timers)
- [153: How do you create custom error classes for an Express API?](#153-how-do-you-create-custom-error-classes-for-an-express-api)
- [154: What is the difference between operational errors and programmer errors?](#154-what-is-the-difference-between-operational-errors-and-programmer-errors)
- [155: Can you have more than one error-handling middleware?](#155-can-you-have-more-than-one-error-handling-middleware)
- [156: Can an error handler be put on a router?](#156-can-an-error-handler-be-put-on-a-router)
- [157: How do you write a reusable validation middleware with zod?](#157-how-do-you-write-a-reusable-validation-middleware-with-zod)
- [158: Why can't you assign to `req.query` in Express 5, and how do you work around it?](#158-why-cant-you-assign-to-reqquery-in-express-5-and-how-do-you-work-around-it)
- [159: How does JWT authentication usually work in an Express API?](#159-how-does-jwt-authentication-usually-work-in-an-express-api)
- [160: How do you handle refresh tokens in Express?](#160-how-do-you-handle-refresh-tokens-in-express)
- [161: Should you store JWTs in localStorage or cookies?](#161-should-you-store-jwts-in-localstorage-or-cookies)
- [162: How do you use a Redis store with `express-session`?](#162-how-do-you-use-a-redis-store-with-express-session)
- [163: What do `resave` and `saveUninitialized` mean in `express-session`?](#163-what-do-resave-and-saveuninitialized-mean-in-express-session)
- [164: Why should you regenerate the session ID after login?](#164-why-should-you-regenerate-the-session-id-after-login)
- [165: How do you log a user out with `express-session`?](#165-how-do-you-log-a-user-out-with-express-session)
- [166: How do you set up Passport with a local strategy?](#166-how-do-you-set-up-passport-with-a-local-strategy)
- [167: How does a CORS preflight request work, and how does Express handle it?](#167-how-does-a-cors-preflight-request-work-and-how-does-express-handle-it)
- [168: How do you allow several origins with CORS?](#168-how-do-you-allow-several-origins-with-cors)
- [169: How do you add rate limiting to an Express app?](#169-how-do-you-add-rate-limiting-to-an-express-app)
- [170: How do you rate limit login attempts differently from the rest of the API?](#170-how-do-you-rate-limit-login-attempts-differently-from-the-rest-of-the-api)
- [171: How do you configure Content Security Policy with helmet?](#171-how-do-you-configure-content-security-policy-with-helmet)
- [172: How do you protect an Express app against CSRF?](#172-how-do-you-protect-an-express-app-against-csrf)
- [173: How do you add a request ID to every request?](#173-how-do-you-add-a-request-id-to-every-request)
- [174: How do you set up structured logging with pino?](#174-how-do-you-set-up-structured-logging-with-pino)
- [175: What should you never log in an Express app?](#175-what-should-you-never-log-in-an-express-app)
- [176: How do you connect Express to PostgreSQL?](#176-how-do-you-connect-express-to-postgresql)
- [177: Why should you not open a new database connection per request?](#177-why-should-you-not-open-a-new-database-connection-per-request)
- [178: How do you run a database transaction inside an Express route?](#178-how-do-you-run-a-database-transaction-inside-an-express-route)
- [179: How do you use Mongoose with Express?](#179-how-do-you-use-mongoose-with-express)
- [180: How do you use Prisma with Express?](#180-how-do-you-use-prisma-with-express)
- [181: Should you start the server before or after connecting to the database?](#181-should-you-start-the-server-before-or-after-connecting-to-the-database)
- [182: How do you do dependency injection in an Express app without a framework?](#182-how-do-you-do-dependency-injection-in-an-express-app-without-a-framework)
- [183: How do you write unit tests for a single middleware?](#183-how-do-you-write-unit-tests-for-a-single-middleware)
- [184: How do you write integration tests with a real database?](#184-how-do-you-write-integration-tests-with-a-real-database)
- [185: How do you test routes that need authentication?](#185-how-do-you-test-routes-that-need-authentication)
- [186: Why does Jest say it "did not exit" after Express tests?](#186-why-does-jest-say-it-did-not-exit-after-express-tests)
- [187: How do you store uploads in memory with multer and send them to S3?](#187-how-do-you-store-uploads-in-memory-with-multer-and-send-them-to-s3)
- [188: How do you check the type of an uploaded file?](#188-how-do-you-check-the-type-of-an-uploaded-file)
- [189: How do you handle multer errors?](#189-how-do-you-handle-multer-errors)
- [190: How do you stream a large file in a response?](#190-how-do-you-stream-a-large-file-in-a-response)
- [191: How do you stream database rows as JSON?](#191-how-do-you-stream-database-rows-as-json)
- [192: How do you implement Server-Sent Events (SSE) in Express?](#192-how-do-you-implement-server-sent-events-sse-in-express)
- [193: How do you add WebSockets to an Express app?](#193-how-do-you-add-websockets-to-an-express-app)
- [194: How do you share the Express session with Socket.IO?](#194-how-do-you-share-the-express-session-with-socketio)
- [195: How do you shut down an Express server gracefully?](#195-how-do-you-shut-down-an-express-server-gracefully)
- [196: Why should Kubernetes readiness checks fail during shutdown?](#196-why-should-kubernetes-readiness-checks-fail-during-shutdown)
- [197: What is PM2 and when would you use it with Express?](#197-what-is-pm2-and-when-would-you-use-it-with-express)
- [198: How do you write a Dockerfile for an Express app?](#198-how-do-you-write-a-dockerfile-for-an-express-app)
- [199: Why put Nginx in front of an Express app?](#199-why-put-nginx-in-front-of-an-express-app)
- [200: How does the `trust proxy` setting work in detail?](#200-how-does-the-trust-proxy-setting-work-in-detail)
- [201: How do you version an Express API?](#201-how-do-you-version-an-express-api)
- [202: How do you add OpenAPI (Swagger) docs to an Express app?](#202-how-do-you-add-openapi-swagger-docs-to-an-express-app)
- [203: How do you validate requests against an OpenAPI spec?](#203-how-do-you-validate-requests-against-an-openapi-spec)
- [204: How does Express handle `HEAD` requests?](#204-how-does-express-handle-head-requests)
- [205: How does Express handle `OPTIONS` requests by default?](#205-how-does-express-handle-options-requests-by-default)
- [206: How do you return 405 Method Not Allowed?](#206-how-do-you-return-405-method-not-allowed)
- [207: How do you redirect URLs with a trailing slash?](#207-how-do-you-redirect-urls-with-a-trailing-slash)
- [208: How do you route by subdomain or host?](#208-how-do-you-route-by-subdomain-or-host)
- [209: What is a sub-app in Express, and how is it different from a router?](#209-what-is-a-sub-app-in-express-and-how-is-it-different-from-a-router)
- [210: How do you proxy requests from Express to another service?](#210-how-do-you-proxy-requests-from-express-to-another-service)
- [211: How do you run an Express app on AWS Lambda or other serverless platforms?](#211-how-do-you-run-an-express-app-on-aws-lambda-or-other-serverless-platforms)
- [212: How do you use all CPU cores with Express?](#212-how-do-you-use-all-cpu-cores-with-express)
- [213: How do you cache API responses with Redis?](#213-how-do-you-cache-api-responses-with-redis)
- [214: How do you set HTTP caching headers on API responses?](#214-how-do-you-set-http-caching-headers-on-api-responses)
- [215: What timeouts does a Node HTTP server have, and how do you set them on Express?](#215-what-timeouts-does-a-node-http-server-have-and-how-do-you-set-them-on-express)
- [216: How do you add a timeout to a single slow route?](#216-how-do-you-add-a-timeout-to-a-single-slow-route)
- [217: How do you stop work when the client disconnects?](#217-how-do-you-stop-work-when-the-client-disconnects)
- [218: How do you call another HTTP API from an Express route?](#218-how-do-you-call-another-http-api-from-an-express-route)
- [219: How do you read the raw body and also parse JSON?](#219-how-do-you-read-the-raw-body-and-also-parse-json)
- [220: Why does a webhook signature check fail when you use `express.json()`?](#220-why-does-a-webhook-signature-check-fail-when-you-use-expressjson)
- [221: How do you make `express.json()` accept other content types?](#221-how-do-you-make-expressjson-accept-other-content-types)
- [222: Does Express support compressed request bodies?](#222-does-express-support-compressed-request-bodies)
- [223: How do you prevent NoSQL injection in an Express + MongoDB app?](#223-how-do-you-prevent-nosql-injection-in-an-express--mongodb-app)
- [224: How do you prevent XSS in an Express app that renders HTML?](#224-how-do-you-prevent-xss-in-an-express-app-that-renders-html)
- [225: What is HTTP parameter pollution and how does it affect Express?](#225-what-is-http-parameter-pollution-and-how-does-it-affect-express)
- [226: How do you validate environment variables at startup?](#226-how-do-you-validate-environment-variables-at-startup)
- [227: How do you separate routes, controllers and services?](#227-how-do-you-separate-routes-controllers-and-services)
- [228: Why should you not send database models directly in responses?](#228-why-should-you-not-send-database-models-directly-in-responses)
- [229: How do you implement cursor-based pagination?](#229-how-do-you-implement-cursor-based-pagination)
- [230: How do you let clients sort and filter safely?](#230-how-do-you-let-clients-sort-and-filter-safely)
- [231: What is an idempotency key and how do you add it to an Express API?](#231-what-is-an-idempotency-key-and-how-do-you-add-it-to-an-express-api)
- [232: How do you use `AsyncLocalStorage` for request context in Express?](#232-how-do-you-use-asynclocalstorage-for-request-context-in-express)
- [233: How do you add types for custom properties on `req` in TypeScript?](#233-how-do-you-add-types-for-custom-properties-on-req-in-typescript)
- [234: How do you type `req.body`, `req.params` and `req.query` in TypeScript?](#234-how-do-you-type-reqbody-reqparams-and-reqquery-in-typescript)
- [235: What does an Express handler do with its return value?](#235-what-does-an-express-handler-do-with-its-return-value)
- [236: How do you share middleware between several apps or services?](#236-how-do-you-share-middleware-between-several-apps-or-services)
- [237: How do you serve uploaded files safely?](#237-how-do-you-serve-uploaded-files-safely)
- [238: How do you prevent path traversal with `res.sendFile()`?](#238-how-do-you-prevent-path-traversal-with-ressendfile)
- [239: How do you handle `res.sendFile()` errors?](#239-how-do-you-handle-ressendfile-errors)
- [240: How do you add a method like PUT to an HTML form?](#240-how-do-you-add-a-method-like-put-to-an-html-form)
- [241: How do you add flash messages to a server-rendered Express app?](#241-how-do-you-add-flash-messages-to-a-server-rendered-express-app)
- [242: How do you use layouts and partials with EJS?](#242-how-do-you-use-layouts-and-partials-with-ejs)
- [243: Why are templates slow in development but fast in production?](#243-why-are-templates-slow-in-development-but-fast-in-production)
- [244: How do you debug an Express app with breakpoints?](#244-how-do-you-debug-an-express-app-with-breakpoints)
- [245: How do you find which middleware is slow?](#245-how-do-you-find-which-middleware-is-slow)
- [246: How do you add OpenTelemetry tracing to Express?](#246-how-do-you-add-opentelemetry-tracing-to-express)
- [247: How do you expose Prometheus metrics from Express?](#247-how-do-you-expose-prometheus-metrics-from-express)
- [248: How do you report errors to a service like Sentry?](#248-how-do-you-report-errors-to-a-service-like-sentry)
- [249: What should you do on `uncaughtException` and `unhandledRejection`?](#249-what-should-you-do-on-uncaughtexception-and-unhandledrejection)
- [250: How do you make an Express app return JSON 404 for the API and an HTML page for the website?](#250-how-do-you-make-an-express-app-return-json-404-for-the-api-and-an-html-page-for-the-website)
- [251: How do you write middleware that runs after the response is sent?](#251-how-do-you-write-middleware-that-runs-after-the-response-is-sent)
- [252: What is the difference between Express middleware and Koa middleware?](#252-what-is-the-difference-between-express-middleware-and-koa-middleware)
- [253: How do you compose several middleware into one?](#253-how-do-you-compose-several-middleware-into-one)
- [254: How do you run middleware only when a condition is true?](#254-how-do-you-run-middleware-only-when-a-condition-is-true)
- [255: How do you handle JSON body for some routes and raw body for others?](#255-how-do-you-handle-json-body-for-some-routes-and-raw-body-for-others)
- [256: How does a body parser know the body was already parsed?](#256-how-does-a-body-parser-know-the-body-was-already-parsed)
- [257: How do you write a simple in-memory cache middleware?](#257-how-do-you-write-a-simple-in-memory-cache-middleware)
- [258: What is the downside of patching `res.json` or `res.send` in middleware?](#258-what-is-the-downside-of-patching-resjson-or-ressend-in-middleware)
- [259: How do you implement soft authentication (user is optional)?](#259-how-do-you-implement-soft-authentication-user-is-optional)
- [260: How do you implement role-based access control in Express?](#260-how-do-you-implement-role-based-access-control-in-express)
- [261: How do you check that a user owns the resource they want to change?](#261-how-do-you-check-that-a-user-owns-the-resource-they-want-to-change)
- [262: How do you hash passwords in an Express app?](#262-how-do-you-hash-passwords-in-an-express-app)
- [263: How do you implement "login with Google" in Express?](#263-how-do-you-implement-login-with-google-in-express)
- [264: How do you send emails from an Express app without slowing requests?](#264-how-do-you-send-emails-from-an-express-app-without-slowing-requests)
- [265: How do you run background jobs alongside Express?](#265-how-do-you-run-background-jobs-alongside-express)
- [266: How do you return a file generated on the fly, like a CSV?](#266-how-do-you-return-a-file-generated-on-the-fly-like-a-csv)
- [267: How do you enable gzip only for big responses?](#267-how-do-you-enable-gzip-only-for-big-responses)
- [268: Why can compression break Server-Sent Events?](#268-why-can-compression-break-server-sent-events)
- [269: How do you limit how many requests an Express process handles at once?](#269-how-do-you-limit-how-many-requests-an-express-process-handles-at-once)
- [270: How do you serve different API responses based on `Accept-Language`?](#270-how-do-you-serve-different-api-responses-based-on-accept-language)
- [271: What is the `json replacer` setting used for?](#271-what-is-the-json-replacer-setting-used-for)
- [272: Why does `res.json()` throw on BigInt values?](#272-why-does-resjson-throw-on-bigint-values)
- [273: How do you write a request logger that skips health checks?](#273-how-do-you-write-a-request-logger-that-skips-health-checks)
- [274: What are the trade-offs between sessions and JWTs for an Express app?](#274-what-are-the-trade-offs-between-sessions-and-jwts-for-an-express-app)
- [275: How do you implement API key authentication?](#275-how-do-you-implement-api-key-authentication)
- [276: Why should you use `crypto.timingSafeEqual` when comparing secrets?](#276-why-should-you-use-cryptotimingsafeequal-when-comparing-secrets)
- [277: How do you verify a webhook HMAC signature in Express?](#277-how-do-you-verify-a-webhook-hmac-signature-in-express)
- [278: How do you make sure cookies work behind a proxy with `secure: true`?](#278-how-do-you-make-sure-cookies-work-behind-a-proxy-with-secure-true)
- [279: What cookie settings should an auth cookie have?](#279-what-cookie-settings-should-an-auth-cookie-have)
- [280: How do you share code between route handlers without repeating `try/catch`?](#280-how-do-you-share-code-between-route-handlers-without-repeating-trycatch)
- [281: How do you map database errors to HTTP errors in one place?](#281-how-do-you-map-database-errors-to-http-errors-in-one-place)
- [282: How do you return validation errors in a useful format?](#282-how-do-you-return-validation-errors-in-a-useful-format)
- [283: How do you make an Express app handle both JSON and form submissions on the same route?](#283-how-do-you-make-an-express-app-handle-both-json-and-form-submissions-on-the-same-route)
- [284: How do you mock a service in a supertest test?](#284-how-do-you-mock-a-service-in-a-supertest-test)
- [285: How do you test error handling middleware?](#285-how-do-you-test-error-handling-middleware)
- [286: How do you test file uploads with supertest?](#286-how-do-you-test-file-uploads-with-supertest)
- [287: How do you run Express tests in parallel without conflicts?](#287-how-do-you-run-express-tests-in-parallel-without-conflicts)
- [288: How do you use the built-in `node:test` runner with Express?](#288-how-do-you-use-the-built-in-nodetest-runner-with-express)
- [289: How do you handle CORS errors when the frontend and API run on different ports in development?](#289-how-do-you-handle-cors-errors-when-the-frontend-and-api-run-on-different-ports-in-development)
- [290: How do you add security headers if you do not use helmet?](#290-how-do-you-add-security-headers-if-you-do-not-use-helmet)
- [291: What does `Strict-Transport-Security` do and when should you be careful with it?](#291-what-does-strict-transport-security-do-and-when-should-you-be-careful-with-it)
- [292: How do you handle long-running requests like report generation?](#292-how-do-you-handle-long-running-requests-like-report-generation)
- [293: How do you return `201 Created` with the new resource and the right headers?](#293-how-do-you-return-201-created-with-the-new-resource-and-the-right-headers)
- [294: How do you implement conditional updates with ETags to avoid lost updates?](#294-how-do-you-implement-conditional-updates-with-etags-to-avoid-lost-updates)
- [295: How do you build a batch endpoint?](#295-how-do-you-build-a-batch-endpoint)
- [296: How do you add a maintenance mode to an Express app?](#296-how-do-you-add-a-maintenance-mode-to-an-express-app)
- [297: How do you use feature flags in Express routes?](#297-how-do-you-use-feature-flags-in-express-routes)
- [298: How do you avoid blocking the event loop in a route?](#298-how-do-you-avoid-blocking-the-event-loop-in-a-route)
- [299: How do you check event loop delay in an Express app?](#299-how-do-you-check-event-loop-delay-in-an-express-app)
- [300: How do you document and enforce a consistent API style in an Express codebase?](#300-how-do-you-document-and-enforce-a-consistent-api-style-in-an-express-codebase)

### Advanced Questions (301-450)

- [301: How does the Express router work inside?](#301-how-does-the-express-router-work-inside)
- [302: How does Express know that a middleware is an error handler?](#302-how-does-express-know-that-a-middleware-is-an-error-handler)
- [303: What happens inside Express when no route matches?](#303-what-happens-inside-express-when-no-route-matches)
- [304: How does Express add its methods to `req` and `res`?](#304-how-does-express-add-its-methods-to-req-and-res)
- [305: How does `path-to-regexp` v8 change routing in Express 5?](#305-how-does-path-to-regexp-v8-change-routing-in-express-5)
- [306: What was the path-to-regexp ReDoS issue, and why does it matter for Express?](#306-what-was-the-path-to-regexp-redos-issue-and-why-does-it-matter-for-express)
- [307: What is prototype pollution, and how can it affect an Express app?](#307-what-is-prototype-pollution-and-how-can-it-affect-an-express-app)
- [308: How can `res.redirect()` lead to an open redirect, and how do you prevent it?](#308-how-can-resredirect-lead-to-an-open-redirect-and-how-do-you-prevent-it)
- [309: How do you prevent SSRF in an Express endpoint that fetches URLs?](#309-how-do-you-prevent-ssrf-in-an-express-endpoint-that-fetches-urls)
- [310: How do slowloris attacks affect Node and Express, and how do you defend against them?](#310-how-do-slowloris-attacks-affect-node-and-express-and-how-do-you-defend-against-them)
- [311: What is HTTP request smuggling, and does it affect Express apps?](#311-what-is-http-request-smuggling-and-does-it-affect-express-apps)
- [312: How can large or deeply nested JSON bodies hurt an Express app, and how do you protect it?](#312-how-can-large-or-deeply-nested-json-bodies-hurt-an-express-app-and-how-do-you-protect-it)
- [313: How do you prevent header injection (response splitting) in Express?](#313-how-do-you-prevent-header-injection-response-splitting-in-express)
- [314: How do you use a per-request CSP nonce with helmet?](#314-how-do-you-use-a-per-request-csp-nonce-with-helmet)
- [315: What are common JWT mistakes in Express apps?](#315-what-are-common-jwt-mistakes-in-express-apps)
- [316: How do you verify JWTs from an external identity provider in Express?](#316-how-do-you-verify-jwts-from-an-external-identity-provider-in-express)
- [317: Why is Express slower than Fastify in benchmarks, and does it matter?](#317-why-is-express-slower-than-fastify-in-benchmarks-and-does-it-matter)
- [318: How does the number of middleware and routes affect Express performance?](#318-how-does-the-number-of-middleware-and-routes-affect-express-performance)
- [319: How do you make JSON responses faster in Express?](#319-how-do-you-make-json-responses-faster-in-express)
- [320: What does the ETag cost, and when should you turn it off?](#320-what-does-the-etag-cost-and-when-should-you-turn-it-off)
- [321: How do you find a memory leak in an Express app?](#321-how-do-you-find-a-memory-leak-in-an-express-app)
- [322: Why is the default `express-session` MemoryStore not for production?](#322-why-is-the-default-express-session-memorystore-not-for-production)
- [323: How do you scale an Express app horizontally?](#323-how-do-you-scale-an-express-app-horizontally)
- [324: How do you calculate the right database pool size when scaling Express?](#324-how-do-you-calculate-the-right-database-pool-size-when-scaling-express)
- [325: How do you do zero-downtime deploys with Express?](#325-how-do-you-do-zero-downtime-deploys-with-express)
- [326: Does Express support HTTP/2?](#326-does-express-support-http2)
- [327: Why is HTTP/1.1 keep-alive between the load balancer and Express important?](#327-why-is-http11-keep-alive-between-the-load-balancer-and-express-important)
- [328: How does Express 5 handle a handler that returns a rejected promise after it already sent a response?](#328-how-does-express-5-handle-a-handler-that-returns-a-rejected-promise-after-it-already-sent-a-response)
- [329: How would you design a modular Express monolith?](#329-how-would-you-design-a-modular-express-monolith)
- [330: How do you apply hexagonal (ports and adapters) architecture to an Express app?](#330-how-do-you-apply-hexagonal-ports-and-adapters-architecture-to-an-express-app)
- [331: When would you pick NestJS over plain Express?](#331-when-would-you-pick-nestjs-over-plain-express)
- [332: How do you add multi-tenancy to an Express API?](#332-how-do-you-add-multi-tenancy-to-an-express-api)
- [333: What is the risk of trusting `X-Forwarded-For` blindly?](#333-what-is-the-risk-of-trusting-x-forwarded-for-blindly)
- [334: How do you run Express behind several proxies (CDN, then load balancer)?](#334-how-do-you-run-express-behind-several-proxies-cdn-then-load-balancer)
- [335: How do you prevent the same request being processed twice when a client retries after a timeout?](#335-how-do-you-prevent-the-same-request-being-processed-twice-when-a-client-retries-after-a-timeout)
- [336: A route is sometimes very slow under load but fast alone. How do you investigate?](#336-a-route-is-sometimes-very-slow-under-load-but-fast-alone-how-do-you-investigate)
- [337: Users get random 502 errors from the load balancer, but the app logs show no errors. What could cause it?](#337-users-get-random-502-errors-from-the-load-balancer-but-the-app-logs-show-no-errors-what-could-cause-it)
- [338: Requests sometimes hang forever. What would you look for?](#338-requests-sometimes-hang-forever-what-would-you-look-for)
- [339: You see "Cannot set headers after they are sent to the client". How do you fix it?](#339-you-see-cannot-set-headers-after-they-are-sent-to-the-client-how-do-you-fix-it)
- [340: CPU sits at 100% on one Express instance. How do you find the cause?](#340-cpu-sits-at-100-on-one-express-instance-how-do-you-find-the-cause)
- [341: How does Express 5 encode URLs in `res.redirect()` and `res.location()`?](#341-how-does-express-5-encode-urls-in-resredirect-and-reslocation)
- [342: How do you make Express routes work with custom `RegExp` safely?](#342-how-do-you-make-express-routes-work-with-custom-regexp-safely)
- [343: How do you handle requests where the client sends `Expect: 100-continue`?](#343-how-do-you-handle-requests-where-the-client-sends-expect-100-continue)
- [344: How do you implement range requests for video streaming?](#344-how-do-you-implement-range-requests-for-video-streaming)
- [345: How do you handle backpressure when writing large responses manually?](#345-how-do-you-handle-backpressure-when-writing-large-responses-manually)
- [346: What happens to a streaming response if the source stream fails halfway?](#346-what-happens-to-a-streaming-response-if-the-source-stream-fails-halfway)
- [347: How would you build rate limiting that is fair across many instances?](#347-how-would-you-build-rate-limiting-that-is-fair-across-many-instances)
- [348: What is the difference between rate limiting and load shedding?](#348-what-is-the-difference-between-rate-limiting-and-load-shedding)
- [349: How do you return useful `Retry-After` and rate limit headers?](#349-how-do-you-return-useful-retry-after-and-rate-limit-headers)
- [350: How do you design an Express API that sends events to other services reliably?](#350-how-do-you-design-an-express-api-that-sends-events-to-other-services-reliably)
- [351: How does Express 5 decide whether a handler returned a promise?](#351-how-does-express-5-decide-whether-a-handler-returned-a-promise)
- [352: What happens if an async middleware calls `next()` and then throws?](#352-what-happens-if-an-async-middleware-calls-next-and-then-throws)
- [353: How is `req.query` computed in Express 5?](#353-how-is-reqquery-computed-in-express-5)
- [354: Why did Express 5 change the default query parser from `extended` to `simple`?](#354-why-did-express-5-change-the-default-query-parser-from-extended-to-simple)
- [355: How do you plug in a custom query string parser?](#355-how-do-you-plug-in-a-custom-query-string-parser)
- [356: How does `express.static` (serve-static) work internally?](#356-how-does-expressstatic-serve-static-work-internally)
- [357: Why is `express.static` slower than Nginx or a CDN for static files?](#357-why-is-expressstatic-slower-than-nginx-or-a-cdn-for-static-files)
- [358: How do you serve pre-compressed static files (`.br`, `.gz`) from Express?](#358-how-do-you-serve-pre-compressed-static-files-br-gz-from-express)
- [359: What is the cost of `app.use(compression())` in Node, and when should you not use it?](#359-what-is-the-cost-of-appusecompression-in-node-and-when-should-you-not-use-it)
- [360: What are the risks of Brotli or gzip on responses that contain secrets?](#360-what-are-the-risks-of-brotli-or-gzip-on-responses-that-contain-secrets)
- [361: How do you protect an Express app from a "zip bomb" request body?](#361-how-do-you-protect-an-express-app-from-a-zip-bomb-request-body)
- [362: How would you implement a request-scoped database transaction across several services?](#362-how-would-you-implement-a-request-scoped-database-transaction-across-several-services)
- [363: What are the downsides of using global middleware to open a transaction per request?](#363-what-are-the-downsides-of-using-global-middleware-to-open-a-transaction-per-request)
- [364: How do you design error handling for an Express API used by many teams?](#364-how-do-you-design-error-handling-for-an-express-api-used-by-many-teams)
- [365: How do you make error responses include the request ID for support?](#365-how-do-you-make-error-responses-include-the-request-id-for-support)
- [366: How do you safely log errors that may contain circular references or huge objects?](#366-how-do-you-safely-log-errors-that-may-contain-circular-references-or-huge-objects)
- [367: What is the event loop impact of synchronous logging in Express?](#367-what-is-the-event-loop-impact-of-synchronous-logging-in-express)
- [368: How do you implement graceful shutdown when there are open WebSocket or SSE connections?](#368-how-do-you-implement-graceful-shutdown-when-there-are-open-websocket-or-sse-connections)
- [369: How do you keep Socket.IO working with several Express instances?](#369-how-do-you-keep-socketio-working-with-several-express-instances)
- [370: How do you secure a WebSocket upgrade in an Express app?](#370-how-do-you-secure-a-websocket-upgrade-in-an-express-app)
- [371: How would you build a gateway in Express in front of several microservices?](#371-how-would-you-build-a-gateway-in-express-in-front-of-several-microservices)
- [372: How do you add a circuit breaker around calls to another service in an Express route?](#372-how-do-you-add-a-circuit-breaker-around-calls-to-another-service-in-an-express-route)
- [373: How do you add retries to outgoing calls without making things worse?](#373-how-do-you-add-retries-to-outgoing-calls-without-making-things-worse)
- [374: How do you design an Express service to handle a sudden traffic spike?](#374-how-do-you-design-an-express-service-to-handle-a-sudden-traffic-spike)
- [375: How do you load test an Express API?](#375-how-do-you-load-test-an-express-api)
- [376: What is the "thundering herd" problem with caching, and how do you avoid it in Express?](#376-what-is-the-thundering-herd-problem-with-caching-and-how-do-you-avoid-it-in-express)
- [377: How do you handle cache invalidation when data changes?](#377-how-do-you-handle-cache-invalidation-when-data-changes)
- [378: How would you migrate a large Express 4 codebase to Express 5 safely?](#378-how-would-you-migrate-a-large-express-4-codebase-to-express-5-safely)
- [379: Why can async wrappers like `express-async-errors` cause problems after moving to Express 5?](#379-why-can-async-wrappers-like-express-async-errors-cause-problems-after-moving-to-express-5)
- [380: How do you make an Express app ready for containers and Kubernetes?](#380-how-do-you-make-an-express-app-ready-for-containers-and-kubernetes)
- [381: Why should you not use `npm start` as the container command?](#381-why-should-you-not-use-npm-start-as-the-container-command)
- [382: How does Node decide the heap size in a container, and why does it matter for Express?](#382-how-does-node-decide-the-heap-size-in-a-container-and-why-does-it-matter-for-express)
- [383: How do you safely run database migrations when deploying an Express app?](#383-how-do-you-safely-run-database-migrations-when-deploying-an-express-app)
- [384: How would you implement API request signing for partners?](#384-how-would-you-implement-api-request-signing-for-partners)
- [385: How do you implement mutual TLS (mTLS) with Express?](#385-how-do-you-implement-mutual-tls-mtls-with-express)
- [386: How do you protect admin endpoints beyond normal authentication?](#386-how-do-you-protect-admin-endpoints-beyond-normal-authentication)
- [387: How do you build an audit log for an Express API?](#387-how-do-you-build-an-audit-log-for-an-express-api)
- [388: How do you handle personal data (GDPR) in an Express app?](#388-how-do-you-handle-personal-data-gdpr-in-an-express-app)
- [389: How do you avoid leaking stack traces in production?](#389-how-do-you-avoid-leaking-stack-traces-in-production)
- [390: What is the security risk of `res.send()` with user-controlled content?](#390-what-is-the-security-risk-of-ressend-with-user-controlled-content)
- [391: How do you handle timezones and dates in an Express API?](#391-how-do-you-handle-timezones-and-dates-in-an-express-api)
- [392: How do you return money values in an Express API?](#392-how-do-you-return-money-values-in-an-express-api)
- [393: How would you design file upload for very large files (several GB)?](#393-how-would-you-design-file-upload-for-very-large-files-several-gb)
- [394: What problems can come from mounting the same router in two places?](#394-what-problems-can-come-from-mounting-the-same-router-in-two-places)
- [395: How do you hot-reload routes without restarting the server?](#395-how-do-you-hot-reload-routes-without-restarting-the-server)
- [396: How would you add GraphQL to an existing Express REST API?](#396-how-would-you-add-graphql-to-an-existing-express-rest-api)
- [397: How do you protect a GraphQL endpoint in Express from expensive queries?](#397-how-do-you-protect-a-graphql-endpoint-in-express-from-expensive-queries)
- [398: How do you share one Express app between HTTP and serverless functions in a monorepo?](#398-how-do-you-share-one-express-app-between-http-and-serverless-functions-in-a-monorepo)
- [399: How do Lambda cold starts affect Express, and how do you reduce them?](#399-how-do-lambda-cold-starts-affect-express-and-how-do-you-reduce-them)
- [400: How do you handle the `X-Forwarded-*` headers when Express runs on Lambda behind API Gateway?](#400-how-do-you-handle-the-x-forwarded--headers-when-express-runs-on-lambda-behind-api-gateway)
- [401: How does the libuv thread pool affect an Express app?](#401-how-does-the-libuv-thread-pool-affect-an-express-app)
- [402: How do you move CPU-heavy work off the main thread in an Express route?](#402-how-do-you-move-cpu-heavy-work-off-the-main-thread-in-an-express-route)
- [403: What is the difference between using `cluster` and `worker_threads` for an Express app?](#403-what-is-the-difference-between-using-cluster-and-worker_threads-for-an-express-app)
- [404: How does the cluster module share one port between worker processes?](#404-how-does-the-cluster-module-share-one-port-between-worker-processes)
- [405: How do you write middleware that is safe to use in both Express 4 and Express 5?](#405-how-do-you-write-middleware-that-is-safe-to-use-in-both-express-4-and-express-5)
- [406: How do you add custom methods to `res` for all apps without monkey patching globally?](#406-how-do-you-add-custom-methods-to-res-for-all-apps-without-monkey-patching-globally)
- [407: What is the cost of `Object.setPrototypeOf` on every request?](#407-what-is-the-cost-of-objectsetprototypeof-on-every-request)
- [408: How do you handle errors from response streams after `res.json()` is called?](#408-how-do-you-handle-errors-from-response-streams-after-resjson-is-called)
- [409: How do you build a plugin system on top of Express?](#409-how-do-you-build-a-plugin-system-on-top-of-express)
- [410: How do you make sure no route is left without authentication by mistake?](#410-how-do-you-make-sure-no-route-is-left-without-authentication-by-mistake)
- [411: How can you list all routes in an Express app?](#411-how-can-you-list-all-routes-in-an-express-app)
- [412: How would you design an Express API that has to serve both web and mobile clients?](#412-how-would-you-design-an-express-api-that-has-to-serve-both-web-and-mobile-clients)
- [413: How do you deprecate an endpoint without breaking clients?](#413-how-do-you-deprecate-an-endpoint-without-breaking-clients)
- [414: How do you prevent mass assignment in Express handlers?](#414-how-do-you-prevent-mass-assignment-in-express-handlers)
- [415: How do you handle partial updates (PATCH) safely with JSON Merge Patch?](#415-how-do-you-handle-partial-updates-patch-safely-with-json-merge-patch)
- [416: How do you avoid N+1 queries in Express endpoints?](#416-how-do-you-avoid-n1-queries-in-express-endpoints)
- [417: How do you handle very slow clients reading large responses?](#417-how-do-you-handle-very-slow-clients-reading-large-responses)
- [418: What happens if you `await` something after the client already disconnected?](#418-what-happens-if-you-await-something-after-the-client-already-disconnected)
- [419: How would you implement long polling in Express?](#419-how-would-you-implement-long-polling-in-express)
- [420: How do you handle request cancellation when using a database that supports it?](#420-how-do-you-handle-request-cancellation-when-using-a-database-that-supports-it)
- [421: How do you test that your Express app handles graceful shutdown correctly?](#421-how-do-you-test-that-your-express-app-handles-graceful-shutdown-correctly)
- [422: How would you design health checks that do not cause outages?](#422-how-would-you-design-health-checks-that-do-not-cause-outages)
- [423: How would you debug a production issue where only some requests fail with 500?](#423-how-would-you-debug-a-production-issue-where-only-some-requests-fail-with-500)
- [424: What is the difference between `res.on('finish')` and `res.on('close')`?](#424-what-is-the-difference-between-resonfinish-and-resonclose)
- [425: Why might middleware order cause a security bug?](#425-why-might-middleware-order-cause-a-security-bug)
- [426: How do you safely use `app.set('trust proxy', true)` in development and something stricter in production?](#426-how-do-you-safely-use-appsettrust-proxy-true-in-development-and-something-stricter-in-production)
- [427: What are the trade-offs of using Express for a high-throughput internal microservice?](#427-what-are-the-trade-offs-of-using-express-for-a-high-throughput-internal-microservice)
- [428: How do you measure Express overhead in your own app?](#428-how-do-you-measure-express-overhead-in-your-own-app)
- [429: How would you implement a simple API gateway feature: request aggregation?](#429-how-would-you-implement-a-simple-api-gateway-feature-request-aggregation)
- [430: How do you propagate trace context from Express to other services?](#430-how-do-you-propagate-trace-context-from-express-to-other-services)
- [431: How do you ensure logs from one request are grouped together across async calls?](#431-how-do-you-ensure-logs-from-one-request-are-grouped-together-across-async-calls)
- [432: What is a common mistake with `AsyncLocalStorage` in Express middleware?](#432-what-is-a-common-mistake-with-asynclocalstorage-in-express-middleware)
- [433: How would you handle tenant-specific configuration and rate limits in a multi-tenant Express app?](#433-how-would-you-handle-tenant-specific-configuration-and-rate-limits-in-a-multi-tenant-express-app)
- [434: How do you prevent cache poisoning in an Express app behind a CDN?](#434-how-do-you-prevent-cache-poisoning-in-an-express-app-behind-a-cdn)
- [435: How do you test security headers and CORS behavior automatically?](#435-how-do-you-test-security-headers-and-cors-behavior-automatically)
- [436: How do you keep Express dependencies secure over time?](#436-how-do-you-keep-express-dependencies-secure-over-time)
- [437: How would you approach replacing Express with Fastify in a large app?](#437-how-would-you-approach-replacing-express-with-fastify-in-a-large-app)
- [438: What makes an Express codebase hard to maintain, and how do you avoid it?](#438-what-makes-an-express-codebase-hard-to-maintain-and-how-do-you-avoid-it)
- [439: A request body is sometimes `undefined` in Express 5. Why?](#439-a-request-body-is-sometimes-undefined-in-express-5-why)
- [440: How do you handle requests with a JSON body that is a primitive, like `"hello"` or `42`?](#440-how-do-you-handle-requests-with-a-json-body-that-is-a-primitive-like-hello-or-42)
- [441: How do you add response validation to catch bugs in development?](#441-how-do-you-add-response-validation-to-catch-bugs-in-development)
- [442: What are the risks of `app.use(express.static('.'))` or similar?](#442-what-are-the-risks-of-appuseexpressstatic-or-similar)
- [443: How do you make an Express app work with ES modules and top-level await at startup?](#443-how-do-you-make-an-express-app-work-with-es-modules-and-top-level-await-at-startup)
- [444: How do you use Express with Bun or Deno?](#444-how-do-you-use-express-with-bun-or-deno)
- [445: How would you design request validation, error format, and docs so they never drift apart?](#445-how-would-you-design-request-validation-error-format-and-docs-so-they-never-drift-apart)
- [446: You need to add authentication to an existing public API that many clients use. How do you roll it out?](#446-you-need-to-add-authentication-to-an-existing-public-api-that-many-clients-use-how-do-you-roll-it-out)
- [447: An Express app's memory grows until it is OOM killed every few hours. Walk through your approach.](#447-an-express-apps-memory-grows-until-it-is-oom-killed-every-few-hours-walk-through-your-approach)
- [448: What would you change in an Express app before a big launch?](#448-what-would-you-change-in-an-express-app-before-a-big-launch)
- [449: How do you explain the Express request lifecycle end to end, from socket to response?](#449-how-do-you-explain-the-express-request-lifecycle-end-to-end-from-socket-to-response)
- [450: What do you think are the most important habits for building good Express apps?](#450-what-do-you-think-are-the-most-important-habits-for-building-good-express-apps)

---

## Easy Questions (1-150)

### 1: What is Express.js?

Express is a small web framework for Node.js. It gives you routing, middleware and helpers for requests and responses on top of the built-in `http` module. It does not force a project structure, an ORM or a template engine on you, so you pick the pieces you need. It is one of the oldest and most used Node.js frameworks, and many other tools (NestJS by default, for example) run on top of it.

### 2: Why would you use Express instead of the plain `http` module?

With plain `http` you have to parse URLs, match routes, read the body, set headers and handle errors yourself. Express does that for you with a simple API: `app.get('/users/:id', handler)`, `res.json(data)`, `express.json()` for bodies and a clear way to plug in middleware. You still have full access to the raw Node request and response objects when you need them.

### 3: How do you install Express?

Create a project and add Express as a dependency:

```bash
mkdir my-api && cd my-api
npm init -y
npm install express
```

Express 5 needs Node.js 18 or newer. `npm install express` installs version 5 now, since it is the `latest` tag on npm.

### 4: What does a minimal Express app look like?

```js
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3000, () => {
  console.log("Listening on http://localhost:3000");
});
```

`express()` creates the app, `app.get` adds a route, and `app.listen` starts an HTTP server on port 3000.

### 5: How do you use Express with ES modules instead of CommonJS?

Set `"type": "module"` in `package.json` (or use `.mjs` files) and use `import`:

```js
import express from "express";

const app = express();

app.get("/", (req, res) => res.send("ok"));

app.listen(3000);
```

Both styles work with Express. Just do not mix `require` and `import` in the same file.

### 6: What is the `app` object?

`app` is what `express()` returns. It is the main object of your application. You use it to add routes (`app.get`, `app.post`), add middleware (`app.use`), change settings (`app.set`), store app-wide values (`app.locals`) and start the server (`app.listen`). It is also a plain function `(req, res)` so you can pass it to `http.createServer`.

### 7: What does `app.listen()` do?

It creates a Node HTTP server, passes `app` to it as the request handler and starts listening on the given port. It returns the `http.Server` instance, which you can keep to close the server later.

```js
const server = app.listen(3000, () => console.log("started"));
```

It is a shortcut for `http.createServer(app).listen(3000)`. In Express 5, if listening fails (for example the port is in use) the error is passed to the callback as the first argument.

### 8: What is routing in Express?

Routing is deciding which code runs for a given HTTP method and URL path. A route is made of a method, a path and one or more handler functions:

```js
app.get("/products", listProducts);
app.post("/products", createProduct);
app.delete("/products/:id", deleteProduct);
```

Express checks routes in the order you added them and runs the first one that matches (unless that handler calls `next()`).

### 9: Which HTTP methods can you define routes for?

Express has a method for every HTTP verb that Node supports, written in lowercase: `app.get`, `app.post`, `app.put`, `app.patch`, `app.delete`, `app.options`, `app.head` and others. There is also `app.all`, which matches every method. In Express 5, `app.del` (an old alias for delete) was removed, so use `app.delete`.

### 10: What is the difference between PUT and PATCH in an Express API?

That is an HTTP difference, not an Express one, but it shows up often. `PUT` usually replaces the whole resource with what the client sent. `PATCH` updates only the fields that were sent. Express does not enforce this; it is up to your handlers. A common setup is `app.put('/users/:id', replaceUser)` and `app.patch('/users/:id', updateUser)`.

### 11: What are route parameters?

They are named parts of the path that start with `:`. Express puts their values in `req.params`:

```js
app.get("/users/:userId/books/:bookId", (req, res) => {
  res.json(req.params); // { userId: '34', bookId: '8989' }
});
```

Values are always strings, so convert them yourself if you need numbers.

### 12: How do you read query string values?

Use `req.query`. For `/search?term=shoes&page=2`:

```js
app.get("/search", (req, res) => {
  const { term, page } = req.query; // 'shoes', '2'
  res.send(`Searching ${term} on page ${page}`);
});
```

Values are strings (or arrays if a key appears more than once). In Express 5, `req.query` is a getter, so you cannot assign to it directly anymore.

### 13: What is the difference between `req.params` and `req.query`?

`req.params` holds values from the path, defined by the route, like `/users/:id`. `req.query` holds values after the `?` in the URL, like `?sort=name`. Params usually identify a resource. Query values usually filter, sort or paginate a list.

### 14: What is `req.body` and how do you get it?

`req.body` holds the data sent in the request body (for POST, PUT, PATCH). Express does not parse the body by default, so you need body-parsing middleware:

```js
app.use(express.json());

app.post("/users", (req, res) => {
  res.status(201).json(req.body);
});
```

In Express 5, `req.body` is `undefined` if no parser ran. In Express 4 it was `{}`.

### 15: What does `express.json()` do?

It is built-in middleware that reads requests with a `Content-Type` of `application/json`, parses the body and puts the result in `req.body`. If the JSON is broken, it passes a 400 error to the error handler. You can set options like a size limit:

```js
app.use(express.json({ limit: "100kb" }));
```

The default limit is `100kb`.

### 16: What does `express.urlencoded()` do?

It parses bodies sent as `application/x-www-form-urlencoded`, which is what a normal HTML form sends. The result goes to `req.body`.

```js
app.use(express.urlencoded({ extended: false }));
```

`extended: false` uses Node's `querystring` and gives flat values. `extended: true` uses the `qs` library and supports nested objects like `user[name]=Ann`. In Express 5 the default is `false`.

### 17: What is the request object (`req`)?

`req` represents the incoming HTTP request. It is Node's `IncomingMessage` with extra properties and methods added by Express: `req.params`, `req.query`, `req.body` (after parsing), `req.path`, `req.ip`, `req.get()` for headers, `req.is()` for content type checks and more.

### 18: What is the response object (`res`)?

`res` represents the response you send back. It is Node's `ServerResponse` with Express helpers added: `res.status()`, `res.send()`, `res.json()`, `res.redirect()`, `res.render()`, `res.sendFile()`, `res.set()`, `res.cookie()` and others.

### 19: What is the difference between `res.send()` and `res.json()`?

`res.send()` sends almost anything: a string, a Buffer, an object or an array. For strings it sets `Content-Type` to `text/html` unless you set it. `res.json()` always turns the value into JSON with `JSON.stringify` and sets `Content-Type: application/json`. Use `res.json()` in APIs so the intent is clear, and so `null` and numbers are handled as JSON too.

### 20: How do you set the response status code?

Use `res.status()`, which returns `res` so you can chain:

```js
res.status(404).json({ error: "Not found" });
```

If you do not set it, the status is 200. In Express 5, `res.status()` throws if the code is not an integer from 100 to 999.

### 21: What does `res.sendStatus()` do?

It sets the status code and sends the standard text for it as the body:

```js
res.sendStatus(204); // no body for 204
res.sendStatus(403); // body is "Forbidden"
```

In Express 4 you could call `res.send(404)` with a number. That was removed in Express 5, so use `res.sendStatus(404)` or `res.status(404).send(...)`.

### 22: How do you redirect a request?

Use `res.redirect()`. The default status is 302:

```js
res.redirect("/login");
res.redirect(301, "https://example.com/new-page");
```

In Express 5 the status comes first. The old `res.redirect(url, status)` order and the magic `'back'` value were removed. To go back, use `res.redirect(req.get('Referrer') || '/')`.

### 23: What is middleware in Express?

Middleware is a function that runs during the request-response cycle. It gets `req`, `res` and `next`. It can read or change the request and response, end the request by sending a response, or call `next()` to pass control to the next function.

```js
app.use((req, res, next) => {
  console.log(req.method, req.url);
  next();
});
```

Almost everything in Express, including body parsing and routes, is built from middleware.

### 24: What does `next()` do?

It passes control to the next matching middleware or route handler. If a middleware does not send a response and does not call `next()`, the request hangs until the client times out. Calling `next(err)` with an argument skips normal handlers and goes to error-handling middleware.

### 25: What does `app.use()` do?

It mounts middleware. Without a path, the middleware runs for every request. With a path, it runs for requests that start with that path:

```js
app.use(express.json()); // every request
app.use("/admin", requireAdmin); // /admin, /admin/users, ...
app.use("/api", apiRouter); // mount a router
```

`app.use` matches any HTTP method.

### 26: Why does the order of middleware matter?

Express runs middleware and routes in the order they are added. If you add `express.json()` after your routes, those routes see no parsed body. If you put an auth check after the route it should protect, it never runs for that route. A 404 handler must be near the end, and error handlers last.

### 27: What kinds of middleware are there in Express?

- Application-level: added with `app.use()` or `app.METHOD()`.
- Router-level: added to an `express.Router()` instance.
- Error-handling: functions with four arguments `(err, req, res, next)`.
- Built-in: `express.json`, `express.urlencoded`, `express.static`, `express.raw`, `express.text`.
- Third-party: packages like `cors`, `helmet`, `morgan`, `cookie-parser`.

### 28: What is `express.Router()`?

It creates a router, which is like a small app that only has middleware and routes. You use it to split routes into files and mount them under a path:

```js
// routes/users.js
const { Router } = require("express");
const router = Router();

router.get("/", listUsers);
router.get("/:id", getUser);

module.exports = router;

// app.js
app.use("/users", require("./routes/users"));
```

Now `GET /users/5` is handled by `router.get('/:id')`.

### 29: Why split routes into routers?

Putting every route in one file gets messy fast. Routers let you group routes by feature (users, orders, auth), keep files small, apply middleware to a whole group (like auth on `/admin`) and change the mount path in one place. It also makes testing a group of routes easier.

### 30: How do you serve static files?

Use the built-in `express.static` middleware with a folder:

```js
app.use(express.static("public"));
```

Now `public/logo.png` is served at `/logo.png`. If the file is not found, it calls `next()` so later routes can still run.

### 31: How do you serve static files under a path prefix?

Pass a mount path to `app.use`:

```js
app.use("/static", express.static("public"));
```

Now `public/logo.png` is at `/static/logo.png`. The prefix does not have to exist as a folder.

### 32: Why use an absolute path with `express.static`?

A relative path like `'public'` is resolved from the folder where you start the `node` process, not from the file that has the code. If you start the app from another folder, it breaks. Use an absolute path:

```js
const path = require("node:path");
app.use(express.static(path.join(__dirname, "public")));
```

In ES modules use `import.meta.dirname` (Node 20.11+) instead of `__dirname`.

### 33: How do you handle 404 Not Found in Express?

Express sends a basic 404 when nothing matches, but you usually want your own. Add a middleware after all routes:

```js
app.use((req, res) => {
  res.status(404).json({ error: "Not found" });
});
```

It only runs when no earlier route sent a response.

### 34: How do you write an error-handling middleware?

Give it four arguments. Express knows it is an error handler by the number of arguments:

```js
app.use((err, req, res, next) => {
  console.error(err);
  res.status(err.status || 500).json({ error: "Something went wrong" });
});
```

Add it after all other middleware and routes. You must keep all four arguments, even if you do not use `next`.

### 35: How do you pass an error to the error handler?

Call `next(err)`, or in Express 5, throw it or return a rejected promise from the handler:

```js
app.get("/users/:id", async (req, res) => {
  const user = await db.findUser(req.params.id); // if this throws, Express 5 calls next(err)
  res.json(user);
});
```

In Express 4 you had to catch errors in async handlers and call `next(err)` yourself.

### 36: What does Express do with an error if you have no error handler?

It uses its default error handler. It sets the status from `err.status` or `err.statusCode` (or 500), and sends a simple HTML page. In development it includes the stack trace. When `NODE_ENV` is `production`, it only shows the status message. You will almost always want your own handler that returns JSON for an API.

### 37: What is `NODE_ENV` and how does Express use it?

`NODE_ENV` is an environment variable that tells the app which environment it runs in. Express reads it into the `env` setting (`app.get('env')`), which defaults to `'development'`. In production mode Express caches view templates and hides stack traces in the default error handler. Always set `NODE_ENV=production` on production servers.

### 38: How do you read the port from an environment variable?

```js
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on ${port}`));
```

Most hosting platforms set `PORT` for you, so do not hardcode it.

### 39: How do you load environment variables from a `.env` file?

Newer Node versions can do it without extra packages:

```bash
node --env-file=.env app.js
```

You can also use the `dotenv` package and call `require('dotenv').config()` at the top of your entry file. Never commit `.env` files with real secrets.

### 40: How do you restart the server automatically during development?

Use Node's built-in watch mode or `nodemon`:

```bash
node --watch app.js
# or
npx nodemon app.js
```

Both restart the process when files change. `node --watch` is stable in current Node versions, so many projects no longer need `nodemon`.

### 41: What is `express-generator`?

It is a CLI tool that creates a starter Express project with folders for routes, views and public files:

```bash
npx express-generator --view=pug myapp
```

It is handy for learning, but the generated code is quite old in style. Many teams start from a blank project or their own template instead.

### 42: How do you send HTML from Express?

Send a string, which Express sends as `text/html`:

```js
app.get("/", (req, res) => res.send("<h1>Hello</h1>"));
```

For real pages, use a template engine with `res.render()`, or send a file with `res.sendFile()`.

### 43: What is a template engine?

A template engine fills an HTML template with data on the server. Common ones with Express are EJS, Pug and Handlebars. You set it up and then call `res.render`:

```js
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/", (req, res) => {
  res.render("index", { title: "Home" }); // views/index.ejs
});
```

### 44: What does `res.render()` do?

It renders a view with the configured template engine and sends the HTML. You pass the view name and an object with data. You can also pass a callback to get the HTML string instead of sending it right away:

```js
res.render("email", { name: "Ann" }, (err, html) => {
  if (err) return next(err);
  sendEmail(html);
  res.sendStatus(204);
});
```

### 45: What does `res.sendFile()` do?

It sends a file from disk and sets `Content-Type` based on the file extension. The path must be absolute, or you must give a `root` option:

```js
res.sendFile("report.pdf", { root: path.join(__dirname, "files") });
```

It supports range requests and caching headers. In Express 5 the old lowercase `res.sendfile()` was removed.

### 46: What is the difference between `res.sendFile()` and `res.download()`?

`res.sendFile()` sends the file so the browser may show it inline (an image or PDF opens in a tab). `res.download()` sets `Content-Disposition: attachment`, so the browser saves it as a file. You can also give a different file name:

```js
res.download("/data/r-123.pdf", "report.pdf");
```

### 47: How do you read request headers?

Use `req.get()` (or its alias `req.header()`). It is case-insensitive:

```js
const auth = req.get("Authorization");
const type = req.get("content-type");
```

You can also read `req.headers`, which is the raw Node object with lowercase keys.

### 48: How do you set response headers?

Use `res.set()` (alias `res.header()`):

```js
res.set("Cache-Control", "no-store");
res.set({ "X-Request-Id": id, "X-Version": "1.2.0" });
```

`res.append()` adds a value to a header instead of replacing it, which is useful for `Set-Cookie` or `Link`.

### 49: How do you get the full URL path of a request?

There are a few properties:

- `req.originalUrl`: the full URL as sent, including the query string, even inside routers.
- `req.baseUrl`: the path where the current router is mounted.
- `req.path`: the path part relative to the mount point, without the query string.

For a router mounted at `/api` and a request to `/api/users?x=1`: `originalUrl` is `/api/users?x=1`, `baseUrl` is `/api`, `path` is `/users`.

### 50: How do you get the client IP address?

Use `req.ip`. Behind a proxy or load balancer it shows the proxy's address unless you set `trust proxy`:

```js
app.set("trust proxy", 1); // trust the first proxy
app.get("/", (req, res) => res.send(req.ip));
```

With `trust proxy` set, Express reads the client IP from the `X-Forwarded-For` header.

### 51: What does `app.all()` do?

It adds a route that matches every HTTP method for a path. It is often used for checks that should run for all methods on a path:

```js
app.all("/admin/*splat", requireAdmin);
```

The handler can call `next()` to let the more specific routes run after it.

### 52: What does `app.route()` do?

It lets you chain handlers for different methods on the same path, so you do not repeat the path:

```js
app.route("/books").get(listBooks).post(createBook);

app.route("/books/:id").get(getBook).put(updateBook).delete(deleteBook);
```

`router.route()` works the same way on a router.

### 53: Can a route have more than one handler?

Yes. You can pass several functions, or an array. Each one calls `next()` to go to the next:

```js
app.get("/profile", authenticate, loadUser, (req, res) => {
  res.json(req.user);
});
```

This is a common way to add route-specific middleware like auth or validation.

### 54: What is the difference between `app.use()` and `app.get()`?

`app.get()` matches only GET requests and the path must match fully (`/users` does not match `/users/5`). `app.use()` matches any method and matches the path as a prefix (`/users` matches `/users/5` too). `app.use()` is for middleware and routers; `app.get()` is for route handlers.

### 55: How does path matching work with `app.use('/api', ...)`?

`app.use('/api', fn)` runs for `/api`, `/api/` and anything under `/api/`, but not for `/apiv2`. Inside `fn`, `req.url` has the `/api` part removed, and `req.baseUrl` holds `/api`. That is why a router mounted at `/api` can define its routes as `/users` instead of `/api/users`.

### 56: How do you match any path with a wildcard in Express 5?

Express 5 uses `path-to-regexp` v8, where a wildcard must have a name and start with `*`:

```js
app.get("/files/*filepath", (req, res) => {
  // /files/a/b/c.txt -> req.params.filepath is ['a', 'b', 'c.txt']
  res.send(req.params.filepath.join("/"));
});
```

The old Express 4 style `app.get('/files/*')` throws an error in Express 5. To also match `/files` itself, wrap it: `'/files{/*filepath}'`.

### 57: How do you write an optional route parameter in Express 5?

Use braces around the optional part:

```js
app.get("/posts{/:page}", (req, res) => {
  const page = req.params.page ?? "1";
  res.send(`Page ${page}`);
});
```

This matches both `/posts` and `/posts/3`. Express 4 used `/posts/:page?`, but the `?` syntax does not work in Express 5.

### 58: Can you use regular expressions in route paths?

Yes, you can pass a `RegExp` as the path:

```js
app.get(/.*fly$/, (req, res) => res.send("ends with fly"));
```

In Express 5 you cannot put regex characters inside string paths anymore (like `'/user/:id(\\d+)'`). Use a `RegExp` object, or validate the parameter inside the handler or with a validation library.

### 59: What does `req.method` contain?

The HTTP method in uppercase, like `'GET'`, `'POST'` or `'DELETE'`. It is useful in logging and in middleware that should only act on some methods:

```js
app.use((req, res, next) => {
  if (req.method === "GET") return next();
  checkCsrf(req, res, next);
});
```

### 60: What does `res.end()` do?

It ends the response without any Express formatting. It comes from Node's `ServerResponse`. Use it when you want to end with no body, for example `res.status(204).end()`. For sending data, prefer `res.send()` or `res.json()`, which set headers for you.

### 61: Can you send two responses for one request?

No. Once a response is sent, calling `res.send()` or `res.json()` again throws "Cannot set headers after they are sent to the client". This often happens when you forget `return` after sending:

```js
if (!user) {
  return res.status(404).json({ error: "Not found" }); // return stops the function
}
res.json(user);
```

### 62: What is `res.headersSent`?

A boolean that is `true` once the headers have been sent. You can check it before trying to send a response, for example in an error handler:

```js
app.use((err, req, res, next) => {
  if (res.headersSent) return next(err);
  res.status(500).json({ error: "Server error" });
});
```

Passing to `next(err)` here lets Express close the connection properly.

### 63: What are `app.locals` and `res.locals`?

Both are objects for storing values that templates and handlers can read. `app.locals` lives for the whole app, good for things like the site name. `res.locals` lives for one request, good for things like the current user set by an auth middleware. Values in both are available inside `res.render()` templates.

```js
app.locals.siteName = "My Shop";

app.use((req, res, next) => {
  res.locals.user = req.user;
  next();
});
```

### 64: What are app settings and how do you change them?

Settings are named options that change how Express works. You change them with `app.set()` and read them with `app.get()`:

```js
app.set("view engine", "pug");
app.set("trust proxy", 1);
app.get("env"); // 'development' or 'production'
```

Boolean settings also have `app.enable('name')`, `app.disable('name')`, `app.enabled()` and `app.disabled()`.

### 65: How do you remove the `X-Powered-By` header?

Express adds `X-Powered-By: Express` by default. Turn it off so you do not tell everyone what you run:

```js
app.disable("x-powered-by");
```

The `helmet` package also removes it.

### 66: What do the `case sensitive routing` and `strict routing` settings do?

By default `/Users` and `/users` are the same route, and `/users` and `/users/` are the same too. With `app.enable('case sensitive routing')` they are different by case. With `app.enable('strict routing')` the trailing slash matters. You can also set these per router with `express.Router({ caseSensitive: true, strict: true })`.

### 67: What is CORS and how do you enable it in Express?

CORS is a browser rule that blocks a web page from reading responses from another origin unless the server allows it with `Access-Control-Allow-*` headers. The usual way in Express is the `cors` package:

```js
const cors = require("cors");

app.use(cors({ origin: "https://app.example.com", credentials: true }));
```

`cors()` with no options allows every origin, which is fine for public APIs but not for APIs that use cookies.

### 68: What is `morgan`?

`morgan` is HTTP request logging middleware. It prints one line per request with method, URL, status and time:

```js
const morgan = require("morgan");
app.use(morgan("dev")); // short colored output for development
app.use(morgan("combined")); // Apache style log for production
```

For structured JSON logs in production, many teams use `pino-http` instead.

### 69: What is `helmet`?

`helmet` is a middleware that sets security-related HTTP headers, like `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options` and `X-Frame-Options`, and removes `X-Powered-By`:

```js
const helmet = require("helmet");
app.use(helmet());
```

It does not make your app secure on its own, but it is a cheap and good default.

### 70: How do you read cookies in Express?

Express does not parse cookies by itself. Use `cookie-parser`, then read `req.cookies`:

```js
const cookieParser = require("cookie-parser");
app.use(cookieParser());

app.get("/", (req, res) => {
  res.send(`Theme: ${req.cookies.theme}`);
});
```

### 71: How do you set a cookie?

Use `res.cookie(name, value, options)`:

```js
res.cookie("session", token, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  maxAge: 24 * 60 * 60 * 1000, // in milliseconds
});
```

`maxAge` in `res.cookie` is in milliseconds, not seconds.

### 72: How do you delete a cookie?

Use `res.clearCookie()` with the same `path` and `domain` you used to set it, otherwise the browser keeps it:

```js
res.clearCookie("session", { path: "/" });
```

In Express 5, `clearCookie` ignores `maxAge` and `expires` options, because it always sets the cookie to expire in the past.

### 73: What are signed cookies?

Signed cookies have a signature added, so you can tell if the client changed the value. Give `cookie-parser` a secret and set `signed: true`:

```js
app.use(cookieParser(process.env.COOKIE_SECRET));
res.cookie("userId", "42", { signed: true });
// later
req.signedCookies.userId; // '42', or false if it was changed
```

Signing does not hide the value. It only detects tampering.

### 74: What is `express-session`?

It is middleware that adds sessions. It stores a session ID in a cookie and keeps the data on the server. You read and write data through `req.session`:

```js
const session = require("express-session");

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: { httpOnly: true, secure: true },
  }),
);

app.post("/login", (req, res) => {
  req.session.userId = user.id;
  res.sendStatus(204);
});
```

The default memory store is only for development; use Redis or a database store in production.

### 75: How do you upload files in Express?

Express does not parse `multipart/form-data`. Use a library like `multer`:

```js
const multer = require("multer");
const upload = multer({
  dest: "uploads/",
  limits: { fileSize: 5 * 1024 * 1024 },
});

app.post("/avatar", upload.single("avatar"), (req, res) => {
  res.json({ file: req.file.filename });
});
```

`req.file` has the uploaded file info, and the other form fields are in `req.body`.

### 76: What is REST and how does it map to Express routes?

REST is a style for HTTP APIs where URLs name resources and methods say what to do with them. In Express that usually looks like:

```js
router.get("/", list); // GET /articles
router.post("/", create); // POST /articles
router.get("/:id", show); // GET /articles/1
router.patch("/:id", update); // PATCH /articles/1
router.delete("/:id", remove); // DELETE /articles/1
```

### 77: Which status codes should a REST API in Express return?

Common ones:

- `200 OK` for normal reads and updates.
- `201 Created` after creating something, often with a `Location` header.
- `204 No Content` when there is nothing to return, like after a delete.
- `400 Bad Request` for invalid input.
- `401 Unauthorized` when not logged in, `403 Forbidden` when not allowed.
- `404 Not Found`, `409 Conflict`.
- `422 Unprocessable Content` is also used for validation errors by some teams.
- `500` for unexpected server errors.

### 78: How do you set the `Content-Type` of a response?

Use `res.type()`:

```js
res.type("json"); // application/json; charset=utf-8
res.type("html");
res.type("text/csv").send(csv);
```

`res.json()` and `res.send()` with a string set it for you, but you can always set it yourself first.

### 79: What does `req.is()` do?

It checks the `Content-Type` of the request:

```js
if (!req.is("application/json")) {
  return res.status(415).send("Send JSON");
}
```

It returns the matching type, or `false`. It returns `null` if the request has no body.

### 80: What does `req.accepts()` do?

It checks the `Accept` header to see what the client can handle and returns the best match, or `false`:

```js
const type = req.accepts(["json", "html"]);
if (type === "json") res.json(data);
else res.render("page", data);
```

There are also `req.acceptsEncodings()`, `req.acceptsCharsets()` and `req.acceptsLanguages()`. In Express 5 the old singular versions like `req.acceptsCharset()` were removed.

### 81: What does `res.format()` do?

It sends a different response based on the `Accept` header:

```js
res.format({
  "application/json": () => res.json(user),
  "text/html": () => res.render("user", { user }),
  default: () => res.status(406).send("Not Acceptable"),
});
```

It also sets the `Vary: Accept` header.

### 82: What does `req.protocol` contain?

`'http'` or `'https'`. Behind a proxy that ends TLS, it says `'http'` unless you set `trust proxy`, in which case it reads `X-Forwarded-Proto`. `req.secure` is a shortcut for `req.protocol === 'https'`.

### 83: What is the difference between `req.hostname` and `req.host`?

`req.hostname` is the host name from the `Host` header without the port, like `example.com`. In Express 5, `req.host` returns the host including the port, like `example.com:3000`. With `trust proxy` set, both can come from `X-Forwarded-Host`.

### 84: What is `req.subdomains`?

An array of subdomains in the host name. For `tobi.ferrets.example.com`, it is `['ferrets', 'tobi']`. The `subdomain offset` setting (default 2) says how many parts at the end to ignore. It is useful for apps that use subdomains for tenants.

### 85: How do you test an Express API?

A common choice is `supertest` with a test runner like Jest, Vitest or `node:test`. You export the `app` without calling `listen`, and supertest calls it directly:

```js
const request = require("supertest");
const app = require("./app");

test("GET /health", async () => {
  const res = await request(app).get("/health");
  expect(res.status).toBe(200);
  expect(res.body).toEqual({ status: "ok" });
});
```

### 86: Why should you separate creating the app from starting the server?

If `app.js` only builds and exports the app, and `server.js` calls `listen`, your tests can import the app without opening a real port. It also makes it easy to run the same app in different ways, for example with HTTPS or in a serverless wrapper.

```js
// server.js
const app = require("./app");
app.listen(process.env.PORT || 3000);
```

### 87: How do you add a health check endpoint?

Add a simple route that load balancers and Kubernetes can call:

```js
app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});
```

Keep it fast. A separate "readiness" check can also test the database connection.

### 88: How do you see what Express is doing internally?

Express uses the `debug` package. Set the `DEBUG` environment variable to see logs about routing and middleware:

```bash
DEBUG=express:* node app.js
```

You can narrow it, like `DEBUG=express:router`.

### 89: What is the difference between `req.originalUrl` and `req.url`?

`req.url` can be changed while the request passes through Express. Inside a mounted router, the mount path is cut off it. `req.originalUrl` keeps the full URL as it came in. Use `req.originalUrl` for logging and redirects back to the same page.

### 90: How do you validate input in Express?

Express has no built-in validation. You check the input yourself, or use a library like `zod`, `joi` or `express-validator`:

```js
const { z } = require("zod");

const CreateUser = z.object({
  email: z.string().email(),
  name: z.string().min(1),
});

app.post("/users", (req, res) => {
  const result = CreateUser.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.issues });
  }
  // use result.data
});
```

### 91: What is `express-validator`?

It is a set of middleware for validating and cleaning request data, based on the `validator` library:

```js
const { body, validationResult } = require("express-validator");

app.post(
  "/signup",
  body("email").isEmail().normalizeEmail(),
  body("password").isLength({ min: 8 }),
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    res.sendStatus(201);
  },
);
```

### 92: What does `express.raw()` do?

It reads the body as a Buffer and puts it in `req.body`. It is often used for webhooks (like Stripe) where you need the exact bytes to check a signature:

```js
app.post("/webhook", express.raw({ type: "application/json" }), (req, res) => {
  verifySignature(req.body, req.get("Stripe-Signature"));
  res.sendStatus(200);
});
```

### 93: What does `express.text()` do?

It reads the body as a string into `req.body`. By default it handles `text/plain`:

```js
app.post("/notes", express.text(), (req, res) => {
  res.send(`Got ${req.body.length} characters`);
});
```

### 94: Is `body-parser` still needed?

Usually no. Since Express 4.16, the main parsers are built in as `express.json()`, `express.urlencoded()`, `express.raw()` and `express.text()`. These use `body-parser` inside. You only install `body-parser` yourself in old code or if you want to pin a specific version.

### 95: What is the difference between `res.json()` and `res.jsonp()`?

`res.jsonp()` wraps the JSON in a JavaScript function call so old browsers could load it with a `<script>` tag from another domain (JSONP). It is legacy now that CORS exists. Use `res.json()` and set up CORS instead.

### 96: How do you send a response with no content?

```js
res.status(204).end();
// or
res.sendStatus(204);
```

A 204 response must not have a body, and Express removes any body you pass.

### 97: How do you return a `Location` header after creating a resource?

Use `res.location()` and status 201:

```js
app.post("/orders", async (req, res) => {
  const order = await createOrder(req.body);
  res.location(`/orders/${order.id}`).status(201).json(order);
});
```

### 98: What is the request-response cycle in Express?

A request comes in, Express runs matching middleware and routes in order, and each one either sends a response or calls `next()`. The cycle ends when a response is sent. If something calls `next(err)` or throws, Express skips to error handlers. If nothing sends a response, Express's final handler sends a 404.

### 99: How do you organize an Express project?

There is no single required structure. A common one is:

```text
src/
  app.js          # create app, add middleware, mount routers
  server.js       # start the server
  routes/         # routers per feature
  controllers/    # request handlers
  services/       # business logic
  models/         # database models
  middleware/     # auth, validation, error handlers
  config/
```

Some teams group by feature instead (`users/`, `orders/`), with routes, controller and service inside each folder.

### 100: What is a controller in an Express app?

A controller is a module with the handler functions for a group of routes. It keeps route files short and focused on paths:

```js
// controllers/users.js
exports.getUser = async (req, res) => {
  const user = await userService.findById(req.params.id);
  if (!user) return res.sendStatus(404);
  res.json(user);
};

// routes/users.js
router.get("/:id", usersController.getUser);
```

Controllers should handle HTTP details and call services for the actual business logic.

### 101: What are the main differences between Express 4 and Express 5?

The ones people hit most often:

- Rejected promises from async handlers go to the error handler automatically.
- Route path syntax changed (`path-to-regexp` v8): wildcards need a name (`/*splat`), optional parts use braces (`{/:id}`), and regex characters in strings are not allowed.
- `req.body` is `undefined` when no parser ran, and `req.query` is read-only.
- Old methods were removed: `app.del`, `req.param()`, `res.sendfile`, `res.send(status)`, `res.json(obj, status)`, `res.redirect('back')`.
- `express.urlencoded` uses `extended: false` by default.
- Node.js 18 or newer is required.

### 102: How do you upgrade an app from Express 4 to Express 5?

Read the official migration guide, then:

1. Update Node.js to 18+ and run `npm install express@5`.
2. Fix route paths: `*` to `*splat`, `:id?` to `{/:id}`, remove regex from strings.
3. Replace removed methods (`res.send(404)` to `res.sendStatus(404)`, `req.param('id')` to `req.params.id`, and so on).
4. Check code that writes to `req.query` or expects `req.body` to be `{}`.
5. Remove manual async wrappers if you want, since Express 5 handles rejected promises.

There is also a community codemod (`npx @expressjs/codemod upgrade`) that fixes some of these.

### 103: What is `req.param()` and why was it removed?

In Express 4, `req.param('id')` looked for a value in `req.params`, then `req.body`, then `req.query`. It was removed in Express 5 because it was unclear where the value came from, which could lead to bugs or security issues. Read the exact place instead: `req.params.id`, `req.body.id` or `req.query.id`.

### 104: How do you mount one router inside another?

Use `router.use()`:

```js
const api = express.Router();
const v1 = express.Router();

v1.get("/users", listUsers);
api.use("/v1", v1);
app.use("/api", api);
// GET /api/v1/users
```

### 105: What does `mergeParams` do in `express.Router()`?

By default, a router cannot see route params from the parent path. `mergeParams: true` makes them available:

```js
const commentsRouter = express.Router({ mergeParams: true });

commentsRouter.get("/", (req, res) => {
  res.send(`Comments for post ${req.params.postId}`);
});

app.use("/posts/:postId/comments", commentsRouter);
```

Without `mergeParams`, `req.params.postId` would be `undefined` inside `commentsRouter`.

### 106: What does `next('route')` do?

It skips the rest of the handlers for the current route and moves on to the next route that matches. It only works in handlers added with `app.METHOD()` or `router.METHOD()`, not in `app.use()`:

```js
app.get(
  "/user/:id",
  (req, res, next) => {
    if (req.params.id === "0") return next("route");
    next();
  },
  (req, res) => res.send("regular user"),
);

app.get("/user/:id", (req, res) => res.send("special user"));
```

### 107: What does `next('router')` do?

It skips the rest of the current router and goes back to the parent, continuing after the place where the router was mounted. It is useful when a router decides that the request is not for it:

```js
router.use((req, res, next) => {
  if (!req.get("X-Api-Key")) return next("router");
  next();
});
```

### 108: What does `app.param()` do?

It runs a function whenever a route with a given parameter matches. It is often used to load a record once for all routes that have `:userId`:

```js
app.param("userId", async (req, res, next, id) => {
  const user = await User.findById(id);
  if (!user) return res.sendStatus(404);
  req.user = user;
  next();
});

app.get("/users/:userId", (req, res) => res.json(req.user));
```

It runs only once per request, even if several routes match. `router.param()` works the same on a router.

### 109: How do you write middleware that takes options?

Write a function that returns the middleware. This is how most third-party middleware works:

```js
function requireRole(role) {
  return (req, res, next) => {
    if (req.user?.role !== role) return res.sendStatus(403);
    next();
  };
}

app.delete("/users/:id", requireRole("admin"), deleteUser);
```

### 110: How do you add data to the request in middleware?

Set a property on `req` (or `res.locals`) and call `next()`. Later handlers can read it:

```js
app.use((req, res, next) => {
  req.requestTime = Date.now();
  next();
});

app.get("/", (req, res) => res.send(`Requested at ${req.requestTime}`));
```

With TypeScript you also need to extend the `Request` type so the new property is known.

### 111: What is `compression` middleware?

It compresses response bodies with gzip or deflate (and Brotli in recent versions) when the client supports it:

```js
const compression = require("compression");
app.use(compression());
```

It makes JSON and HTML responses smaller. Many setups do compression in a reverse proxy like Nginx instead, which saves CPU in Node.

### 112: How do you use Express with TypeScript?

Install the type definitions and use the `Request`, `Response` and `NextFunction` types:

```bash
npm install express
npm install -D typescript @types/express @types/node
```

```ts
import express, { Request, Response } from "express";

const app = express();

app.get("/users/:id", (req: Request<{ id: string }>, res: Response) => {
  res.json({ id: req.params.id });
});
```

Make sure the `@types/express` major version matches the Express version (v5 for Express 5).

### 113: What does `res.attachment()` do?

It sets `Content-Disposition: attachment` so the browser downloads the response. If you pass a file name, it also sets the `Content-Type` from the extension:

```js
res.attachment("users.csv");
res.send(csvString);
```

### 114: What does `res.vary()` do?

It adds a field to the `Vary` header, which tells caches that the response depends on that request header:

```js
res.vary("Accept-Language");
```

In Express 5 it throws an error if you call it without a field.

### 115: What is ETag and how does Express use it?

An ETag is a value that identifies a version of a response. Express adds a weak ETag to responses sent with `res.send()` by default. If the client sends the same value back in `If-None-Match`, Express replies `304 Not Modified` with no body. You can change it with `app.set('etag', 'strong')` or turn it off with `app.set('etag', false)`.

### 116: What are `req.fresh` and `req.stale`?

`req.fresh` is `true` when the client's cached copy is still valid, based on `If-None-Match` / `If-Modified-Since` and the response's `ETag` / `Last-Modified`. `req.stale` is the opposite. You can use it to skip work:

```js
res.set("ETag", etag);
if (req.fresh) return res.sendStatus(304);
```

### 117: How do you set cache headers for static files?

`express.static` has options for this:

```js
app.use(
  express.static("public", {
    maxAge: "1d",
    immutable: true,
  }),
);
```

`maxAge` sets `Cache-Control: max-age`. Use `immutable` and long caching only for files with a hash in the name, like `app.3f9a2c.js`.

### 118: What are the useful options of `express.static`?

- `maxAge` and `immutable` for caching.
- `index`: the file to serve for a folder (default `index.html`), or `false`.
- `dotfiles`: what to do with files starting with a dot. In Express 5 the default is `'ignore'`.
- `extensions`: try extensions when a file is not found, like `['html']`.
- `fallthrough`: call `next()` on errors instead of returning them (default `true`).
- `setHeaders`: a function to add custom headers.
- `etag` and `lastModified`.

### 119: Can you serve files from more than one folder?

Yes. Add `express.static` more than once. Express looks in them in order:

```js
app.use(express.static("public"));
app.use(express.static("uploads"));
```

If `public/a.png` and `uploads/a.png` both exist, the one in `public` wins.

### 120: How do you serve a single page application (SPA) from Express?

Serve the build folder, then send `index.html` for any other GET request so the client-side router can handle it:

```js
const dist = path.join(__dirname, "dist");

app.use("/api", apiRouter);
app.use(express.static(dist));

app.get("/*splat", (req, res) => {
  res.sendFile(path.join(dist, "index.html"));
});
```

Mount the API first, so API routes do not get `index.html`.

### 121: How do you create an HTTPS server with Express?

Pass the app to Node's `https` module with a certificate:

```js
const https = require("node:https");
const fs = require("node:fs");

https
  .createServer(
    {
      key: fs.readFileSync("key.pem"),
      cert: fs.readFileSync("cert.pem"),
    },
    app,
  )
  .listen(443);
```

In production, TLS is often handled by a load balancer or reverse proxy, and the Express app listens on plain HTTP behind it.

### 122: What does `http.createServer(app)` have to do with Express?

The Express `app` is a function with the signature `(req, res)`, so Node's HTTP server can call it for each request. This is useful when you need the server object, for example to attach Socket.IO or WebSockets to the same port:

```js
const server = http.createServer(app);
const io = new Server(server);
server.listen(3000);
```

### 123: What is the default value of `req.query` when there is no query string?

It is an empty object `{}`. So `req.query.page` is `undefined` when not given. Always provide a default, like `const page = Number(req.query.page) || 1`.

### 124: How does Express parse nested query strings?

That depends on the `query parser` setting. In Express 5 the default is `'simple'`, which uses Node's `querystring`. So `?a[b]=1` gives `{ 'a[b]': '1' }`. If you want nested objects, set it to `'extended'`, which uses `qs`:

```js
app.set("query parser", "extended");
// ?filter[status]=open  ->  { filter: { status: 'open' } }
```

In Express 4 the default was `'extended'`.

### 125: How do you get a number out of a route parameter safely?

Route params are strings, so convert and check them:

```js
app.get("/items/:id", (req, res) => {
  const id = Number.parseInt(req.params.id, 10);
  if (Number.isNaN(id))
    return res.status(400).json({ error: "id must be a number" });
  res.json({ id });
});
```

A schema library like `zod` (`z.coerce.number().int()`) does this more cleanly.

### 126: What is `req.route`?

It holds the route that matched the request, including its `path` (the pattern like `/users/:id`) and the methods. It is handy in logs and metrics because you can group requests by route pattern instead of the actual URL:

```js
res.on("finish", () => {
  console.log(req.method, req.route?.path, res.statusCode);
});
```

### 127: What is `req.xhr`?

A boolean that is `true` when the `X-Requested-With` header is `XMLHttpRequest`. Old jQuery code sent this header. Modern `fetch` does not send it, so do not rely on it to detect API calls.

### 128: How do you return JSON with a custom format, like pretty printing?

Use the `json spaces` setting:

```js
app.set("json spaces", 2);
```

There are also `json replacer` and `json escape` settings. `json escape` escapes `<`, `>` and `&` in JSON output, which helps when JSON is placed in HTML.

### 129: What happens when a client sends invalid JSON?

`express.json()` fails to parse it and calls `next(err)` with an error that has `status: 400` and `type: 'entity.parse.failed'`. Your error handler can check it:

```js
app.use((err, req, res, next) => {
  if (err.type === "entity.parse.failed") {
    return res.status(400).json({ error: "Invalid JSON" });
  }
  next(err);
});
```

### 130: What happens when the body is bigger than the limit?

The body parser stops and passes an error with `status: 413` and `type: 'entity.too.large'`. The default error handler responds with `413 Payload Too Large`. Raise the limit only on routes that need it:

```js
app.post("/import", express.json({ limit: "5mb" }), importData);
```

### 131: How do you apply middleware to only some routes?

You can add it to the route, to a path, or to a router:

```js
app.get("/me", authenticate, getMe); // one route
app.use("/admin", authenticate); // a path prefix
adminRouter.use(authenticate); // every route in a router
```

### 132: How do you run middleware for all routes except some?

Check the path inside the middleware, or mount it after the public routes:

```js
const publicPaths = new Set(["/health", "/login"]);

app.use((req, res, next) => {
  if (publicPaths.has(req.path)) return next();
  authenticate(req, res, next);
});
```

Splitting public and private routes into separate routers is usually cleaner.

### 133: What is `res.locals` used for in an API?

Even without templates, it is a safe place to pass data between middleware for one request, like the request ID or the logged in user. Unlike adding random properties to `req`, it is clearly meant for this and does not clash with Express's own properties.

### 134: How do you return errors in a consistent format?

Send every error through one error handler that builds the same JSON shape:

```js
app.use((err, req, res, next) => {
  const status = err.status || 500;
  res.status(status).json({
    error: {
      message: status === 500 ? "Internal Server Error" : err.message,
      code: err.code,
    },
  });
});
```

Some APIs use the RFC 9457 "problem details" format (`type`, `title`, `status`, `detail`) with `Content-Type: application/problem+json`.

### 135: How do you create an error with a status code?

Make an error and set `status`, or use the `http-errors` package:

```js
const createError = require("http-errors");

app.get("/users/:id", async (req, res) => {
  const user = await findUser(req.params.id);
  if (!user) throw createError(404, "User not found");
  res.json(user);
});
```

Express's default handler and most custom ones read `err.status`.

### 136: What does `res.links()` do?

It sets the `Link` header, which is often used for pagination:

```js
res.links({
  next: "/users?page=3",
  prev: "/users?page=1",
});
// Link: </users?page=3>; rel="next", </users?page=1>; rel="prev"
```

### 137: How do you implement simple pagination?

Read page and size from the query, set limits, and return the data with some info:

```js
app.get("/articles", async (req, res) => {
  const page = Math.max(1, Number(req.query.page) || 1);
  const limit = Math.min(100, Number(req.query.limit) || 20);
  const { rows, total } = await Article.findPage({
    offset: (page - 1) * limit,
    limit,
  });
  res.json({ data: rows, page, limit, total });
});
```

Always cap `limit` so a client cannot ask for a million rows.

### 138: What is the `views` setting?

It is the folder (or array of folders) where `res.render()` looks for templates. The default is `views` in the current working directory. Set it with an absolute path:

```js
app.set("views", path.join(__dirname, "views"));
```

### 139: How do you use EJS with Express?

Install `ejs`, set it as the view engine and render:

```js
app.set("view engine", "ejs");

app.get("/hello", (req, res) => {
  res.render("hello", { name: "Ann" });
});
```

```html
<!-- views/hello.ejs -->
<h1>Hello <%= name %></h1>
```

`<%= %>` escapes HTML. `<%- %>` does not, so only use it with trusted content.

### 140: How do you use a template engine that has a different file extension?

Register it with `app.engine()`:

```js
const { engine } = require("express-handlebars");

app.engine("hbs", engine({ extname: ".hbs" }));
app.set("view engine", "hbs");
```

`app.engine(ext, fn)` tells Express which function renders files with that extension.

### 141: What does `req.ips` contain?

When `trust proxy` is set, `req.ips` is an array of the IP addresses from the `X-Forwarded-For` header, starting with the client and followed by each proxy on the way. When `trust proxy` is off, it is an empty array. `req.ip` is the first trusted address from this list, so you usually read `req.ip` and use `req.ips` only for debugging proxy setups:

```js
app.set("trust proxy", 2);
app.get("/debug/ip", (req, res) => res.json({ ip: req.ip, ips: req.ips }));
```

### 142: What is the difference between `app.get('/x')` and `app.get('x')`?

Paths should start with `/`. `app.get('x', ...)` will not match `/x`, because request paths always start with a slash. This is a simple mistake that leads to routes that never run.

### 143: What is `req.cookies` when you do not use `cookie-parser`?

It is `undefined`. Express does not parse the `Cookie` header itself. You would have to read `req.get('Cookie')` and parse the string. Use `cookie-parser` or a session library.

### 144: What is the difference between authentication and authorization in an Express app?

Authentication checks who the user is, usually by checking a session cookie or a token in the `Authorization` header. Authorization checks what that user is allowed to do, like being an admin. In Express both are usually middleware: one sets `req.user`, the other checks `req.user` before the handler runs.

### 145: How do you protect a route with a simple token check?

```js
function authenticate(req, res, next) {
  const header = req.get("Authorization") || "";
  const token = header.startsWith("Bearer ") ? header.slice(7) : null;
  if (!token) return res.sendStatus(401);
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    res.sendStatus(401);
  }
}

app.get("/me", authenticate, (req, res) => res.json(req.user));
```

This uses the `jsonwebtoken` package.

### 146: What is Passport.js?

Passport is authentication middleware for Express. It uses "strategies" for different login methods: username and password (`passport-local`), JWT, Google, GitHub and many more. It plugs into Express with `passport.initialize()` and, for sessions, `passport.session()`. It is common in older and mid-size apps, though some teams now write simple auth themselves or use a hosted service.

### 147: What does `res.append()` do?

It adds a value to a response header. If the header already exists, the new value is added instead of replacing it:

```js
res.append("Link", ["<http://localhost/>", "<http://localhost:3000/>"]);
res.append("Set-Cookie", "foo=bar; Path=/; HttpOnly");
```

`res.set()` would replace the old value.

### 148: How do you stop an Express server?

Call `close()` on the server returned by `app.listen()`. It stops new connections and waits for open ones to finish:

```js
const server = app.listen(3000);

process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
});
```

### 149: Is Express still maintained?

Yes. Express is part of the OpenJS Foundation and has an active technical committee. Express 5.0 was released in October 2024 after many years of work, and 5.x releases have followed since. Express 4 is in maintenance mode, which means only security fixes until its end-of-life date (check the Express support page for the exact dates). New projects should use Express 5.

### 150: What are some alternatives to Express?

- Fastify: faster, with built-in schema validation and a plugin system.
- Koa: made by the original Express team, smaller, with async middleware.
- Hono: small and runs on many runtimes (Node, Bun, Deno, Cloudflare Workers).
- NestJS: a full framework with modules and dependency injection, which uses Express (or Fastify) under the hood.

Express is still a good choice when you want something simple with a huge number of tutorials and middleware packages.

## Moderate Questions (151-300)

### 151: How did people handle async errors in Express 4, and do you still need that in Express 5?

In Express 4, a rejected promise in a handler was not caught, so the request hung and Node logged an unhandled rejection. People wrapped handlers:

```js
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

app.get(
  "/users",
  asyncHandler(async (req, res) => {
    res.json(await User.findAll());
  }),
);
```

Packages like `express-async-handler` and `express-async-errors` did the same. In Express 5 you do not need this, because the router catches rejected promises from handlers and middleware and calls `next(err)`.

### 152: Does Express 5 catch errors thrown inside callbacks or timers?

No. Express 5 only catches errors thrown directly in the handler and rejected promises returned by it. An error thrown inside a `setTimeout` callback or an old callback-style API happens later, outside Express:

```js
app.get("/bad", (req, res) => {
  setTimeout(() => {
    throw new Error("boom"); // crashes the process, not handled by Express
  }, 10);
});
```

Pass these errors to `next(err)` yourself, or turn the callback API into a promise with `util.promisify` and `await` it.

### 153: How do you create custom error classes for an Express API?

Make a base class with a status code and extend it:

```js
class AppError extends Error {
  constructor(message, status = 500, code = "INTERNAL") {
    super(message);
    this.name = this.constructor.name;
    this.status = status;
    this.code = code;
  }
}

class NotFoundError extends AppError {
  constructor(message = "Not found") {
    super(message, 404, "NOT_FOUND");
  }
}

app.use((err, req, res, next) => {
  if (err instanceof AppError) {
    return res
      .status(err.status)
      .json({ error: { code: err.code, message: err.message } });
  }
  req.log?.error(err);
  res
    .status(500)
    .json({ error: { code: "INTERNAL", message: "Internal Server Error" } });
});
```

Services throw these errors, and the single error handler decides how they look to the client.

### 154: What is the difference between operational errors and programmer errors?

Operational errors are expected problems: bad input, a missing record, a timeout from another service. You handle them and return a proper 4xx or 5xx. Programmer errors are bugs: reading a property of `undefined`, a wrong argument. You cannot really recover from those, so log them, return 500, and fix the code. If the process gets into a bad state (for example an `uncaughtException`), it is safer to let it restart.

### 155: Can you have more than one error-handling middleware?

Yes. They run in order, and each one can respond or pass the error on with `next(err)`. This is a clean way to split handling by type:

```js
app.use(logErrors);
app.use(handleValidationErrors);
app.use(handleDatabaseErrors);
app.use(finalErrorHandler);
```

Each handler checks the error and either handles it or calls `next(err)`.

### 156: Can an error handler be put on a router?

Yes. An error handler added with `router.use((err, req, res, next) => ...)` handles errors from routes in that router. If it calls `next(err)`, the error goes up to the app's error handlers. This is useful when one part of the app needs a different error format, like an HTML section and a JSON API in the same app.

### 157: How do you write a reusable validation middleware with zod?

```js
const validate = (schema) => (req, res, next) => {
  const result = schema.safeParse({
    body: req.body,
    params: req.params,
    query: req.query,
  });
  if (!result.success) {
    return res.status(400).json({ errors: result.error.issues });
  }
  req.valid = result.data;
  next();
};

const getUserSchema = z.object({
  params: z.object({ id: z.coerce.number().int().positive() }),
  body: z.any(),
  query: z.object({}).passthrough(),
});

router.get("/:id", validate(getUserSchema), (req, res) => {
  res.json({ id: req.valid.params.id });
});
```

Store the parsed data on a separate property. In Express 5 you cannot assign to `req.query`, so writing parsed values back there does not work.

### 158: Why can't you assign to `req.query` in Express 5, and how do you work around it?

In Express 5, `req.query` is a getter that parses the query string each time it is read. There is no setter, so `req.query = parsed` throws in strict mode or is ignored. Some old middleware (like `express-mongo-sanitize`) did this and broke. Workarounds:

- Store cleaned data on another property, like `req.validatedQuery`.
- If you really must, use `Object.defineProperty(req, 'query', { value: parsed, writable: true })`, but this is a hack.

### 159: How does JWT authentication usually work in an Express API?

1. The client sends credentials to `POST /login`.
2. The server checks them and signs a short-lived access token (for example 15 minutes) with `jsonwebtoken`.
3. The client sends the token in `Authorization: Bearer <token>` on each request.
4. A middleware verifies the token and sets `req.user`.
5. When it expires, the client gets a new one with a refresh token.

```js
const token = jwt.sign(
  { sub: user.id, role: user.role },
  process.env.JWT_SECRET,
  {
    expiresIn: "15m",
  },
);
```

Always set `algorithms` when verifying, like `jwt.verify(token, secret, { algorithms: ['HS256'] })`.

### 160: How do you handle refresh tokens in Express?

A common setup:

- Issue a long-lived refresh token in an `httpOnly`, `secure`, `sameSite` cookie, limited to a path like `/auth/refresh`.
- Store a hash of it in the database with the user and an expiry.
- On `POST /auth/refresh`, check the cookie against the database, issue a new access token and a new refresh token, and delete the old one (rotation).
- If an old refresh token is used again, treat it as stolen and revoke all tokens for that user.

This lets you log users out and revoke access, which plain JWTs cannot do.

### 161: Should you store JWTs in localStorage or cookies?

`localStorage` is easy but any XSS bug can read it. An `httpOnly` cookie cannot be read by JavaScript, which protects the token from XSS, but then you need to think about CSRF (use `sameSite: 'lax'` or `'strict'`, and CSRF tokens for risky cases). Many teams keep the access token in memory on the client and the refresh token in an `httpOnly` cookie.

### 162: How do you use a Redis store with `express-session`?

Install `connect-redis` and a Redis client:

```js
const session = require("express-session");
const { RedisStore } = require("connect-redis");
const { createClient } = require("redis");

const redisClient = createClient({ url: process.env.REDIS_URL });
await redisClient.connect();

app.use(
  session({
    store: new RedisStore({ client: redisClient, prefix: "sess:" }),
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: { httpOnly: true, secure: true, sameSite: "lax", maxAge: 86400000 },
  }),
);
```

With a shared store, any app instance can read any session, so you can run many instances behind a load balancer.

### 163: What do `resave` and `saveUninitialized` mean in `express-session`?

- `resave: true` saves the session back to the store on every request, even if it did not change. This can cause race conditions with parallel requests. Use `false` if your store supports `touch`.
- `saveUninitialized: true` saves new sessions that have no data yet. Use `false` to avoid filling the store with empty sessions and to only set a cookie after login, which also helps with cookie consent rules.

### 164: Why should you regenerate the session ID after login?

To prevent session fixation. If an attacker got the victim to use a known session ID before login, that ID would become logged in. Regenerating gives a new ID:

```js
app.post("/login", async (req, res, next) => {
  const user = await checkCredentials(req.body);
  if (!user) return res.sendStatus(401);
  req.session.regenerate((err) => {
    if (err) return next(err);
    req.session.userId = user.id;
    req.session.save((err) => (err ? next(err) : res.sendStatus(204)));
  });
});
```

### 165: How do you log a user out with `express-session`?

Destroy the session and clear the cookie:

```js
app.post("/logout", (req, res, next) => {
  req.session.destroy((err) => {
    if (err) return next(err);
    res.clearCookie("connect.sid");
    res.sendStatus(204);
  });
});
```

`connect.sid` is the default cookie name. Use whatever `name` you set in the session options.

### 166: How do you set up Passport with a local strategy?

```js
const passport = require("passport");
const { Strategy: LocalStrategy } = require("passport-local");

passport.use(
  new LocalStrategy(async (username, password, done) => {
    try {
      const user = await User.findByUsername(username);
      if (!user || !(await user.checkPassword(password)))
        return done(null, false);
      done(null, user);
    } catch (err) {
      done(err);
    }
  }),
);

passport.serializeUser((user, done) => done(null, user.id));
passport.deserializeUser((id, done) =>
  User.findById(id).then((u) => done(null, u), done),
);

app.use(session({/* ... */}));
app.use(passport.session());

app.post(
  "/login",
  passport.authenticate("local", { failureRedirect: "/login" }),
  (req, res) => {
    res.redirect("/");
  },
);
```

`serializeUser` decides what goes in the session, and `deserializeUser` loads the user on each request into `req.user`.

### 167: How does a CORS preflight request work, and how does Express handle it?

For "non-simple" requests (like `PUT`, `DELETE`, JSON bodies or custom headers), the browser first sends an `OPTIONS` request with `Access-Control-Request-Method` and `Access-Control-Request-Headers`. The server must answer with the allowed origin, methods and headers. The `cors` middleware handles this when added with `app.use(cors(...))`. You can set `maxAge` so the browser caches the preflight result:

```js
app.use(cors({ origin: "https://app.example.com", maxAge: 600 }));
```

### 168: How do you allow several origins with CORS?

Pass an array, a regex, or a function:

```js
const allowed = new Set([
  "https://app.example.com",
  "https://admin.example.com",
]);

app.use(
  cors({
    origin(origin, callback) {
      // origin is undefined for same-origin requests and tools like curl
      if (!origin || allowed.has(origin)) return callback(null, true);
      callback(null, false);
    },
    credentials: true,
  }),
);
```

When `credentials: true`, the response cannot use `*` as the allowed origin, so the `cors` package echoes back the specific origin.

### 169: How do you add rate limiting to an Express app?

Use `express-rate-limit`:

```js
const { rateLimit } = require("express-rate-limit");

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 100,
  standardHeaders: "draft-8",
  legacyHeaders: false,
});

app.use("/api", limiter);
```

The default store is in memory, so each instance counts on its own. With many instances, use a shared store like `rate-limit-redis`. Set `trust proxy` correctly, or every client will look like the proxy's IP.

### 170: How do you rate limit login attempts differently from the rest of the API?

Create a stricter limiter and put it only on the login route. You can key it by user name too, not just IP:

```js
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 5,
  keyGenerator: (req) => `${req.ip}:${req.body?.email ?? ""}`,
  skipSuccessfulRequests: true,
});

app.post("/login", express.json(), loginLimiter, login);
```

The body parser must run before the limiter if the key uses `req.body`. Recent versions of `express-rate-limit` warn when a custom key uses `req.ip` without the `ipKeyGenerator` helper, because of IPv6 ranges, so read its docs for your version.

### 171: How do you configure Content Security Policy with helmet?

Pass directives to `helmet.contentSecurityPolicy` or to `helmet()`:

```js
app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "https://cdn.example.com"],
        imgSrc: ["'self'", "data:", "https://images.example.com"],
        connectSrc: ["'self'", "https://api.example.com"],
      },
    },
  }),
);
```

For a pure JSON API, CSP matters less. For apps that render HTML, a strict CSP is one of the best protections against XSS.

### 172: How do you protect an Express app against CSRF?

CSRF matters when the browser sends credentials automatically, like with session cookies. Options:

- Set session cookies with `sameSite: 'lax'` or `'strict'`. This blocks most cross-site requests.
- Use CSRF tokens for forms, for example with `csrf-csrf` (double submit cookie) or `csrf-sync` (synchronizer token).
- Check the `Origin` header on state-changing requests.

The old `csurf` package is deprecated and should not be used in new code. APIs that only use `Authorization` headers (not cookies) are not open to CSRF in the same way.

### 173: How do you add a request ID to every request?

Generate or reuse an ID, put it on the request and response, and include it in logs:

```js
const { randomUUID } = require("node:crypto");

app.use((req, res, next) => {
  req.id = req.get("X-Request-Id") || randomUUID();
  res.set("X-Request-Id", req.id);
  next();
});
```

This makes it easy to find all log lines for one request, and to trace it across services. `pino-http` can do this with its `genReqId` option.

### 174: How do you set up structured logging with pino?

```js
const pino = require("pino");
const pinoHttp = require("pino-http");

const logger = pino({ level: process.env.LOG_LEVEL || "info" });

app.use(pinoHttp({ logger }));

app.get("/", (req, res) => {
  req.log.info({ userId: req.user?.id }, "loading home");
  res.send("ok");
});
```

`pino-http` logs every request with status and time, and gives you `req.log` with request info attached. JSON logs are easy to search in tools like Loki, Elasticsearch or CloudWatch. Use `pino-pretty` only in development.

### 175: What should you never log in an Express app?

Passwords, full tokens, session IDs, API keys, credit card numbers and other personal data you do not need. Be careful with logging the whole `req.body` or `req.headers` (which contain `Authorization` and `Cookie`). Pino has a `redact` option:

```js
pino({
  redact: ["req.headers.authorization", "req.headers.cookie", "body.password"],
});
```

### 176: How do you connect Express to PostgreSQL?

Use a connection pool from the `pg` package, created once at startup:

```js
const { Pool } = require("pg");
const pool = new Pool({ connectionString: process.env.DATABASE_URL, max: 10 });

app.get("/users/:id", async (req, res) => {
  const { rows } = await pool.query(
    "SELECT id, name FROM users WHERE id = $1",
    [req.params.id],
  );
  if (!rows[0]) return res.sendStatus(404);
  res.json(rows[0]);
});
```

Always use parameters (`$1`) instead of putting values into the SQL string, to avoid SQL injection.

### 177: Why should you not open a new database connection per request?

Opening a connection is slow (TCP, TLS, auth) and databases have a limit on connections. Under load you would run out quickly. A pool keeps a few connections open and lends them to requests. Create the pool once when the app starts and share it.

### 178: How do you run a database transaction inside an Express route?

Take one client from the pool, run `BEGIN`, do your queries, then `COMMIT` or `ROLLBACK`, and always release the client:

```js
app.post("/transfer", async (req, res) => {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    await client.query(
      "UPDATE accounts SET balance = balance - $1 WHERE id = $2",
      [req.body.amount, req.body.from],
    );
    await client.query(
      "UPDATE accounts SET balance = balance + $1 WHERE id = $2",
      [req.body.amount, req.body.to],
    );
    await client.query("COMMIT");
    res.sendStatus(204);
  } catch (err) {
    await client.query("ROLLBACK");
    throw err;
  } finally {
    client.release();
  }
});
```

Better yet, move this into a service function so the route only handles HTTP.

### 179: How do you use Mongoose with Express?

Connect once before starting the server, then use models in handlers:

```js
const mongoose = require("mongoose");

await mongoose.connect(process.env.MONGO_URL);

app.get("/posts", async (req, res) => {
  const posts = await Post.find().sort({ createdAt: -1 }).limit(20).lean();
  res.json(posts);
});

app.listen(3000);
```

`.lean()` returns plain objects, which is faster when you only send JSON.

### 180: How do you use Prisma with Express?

Create one `PrismaClient` and reuse it:

```js
const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

app.get("/users/:id", async (req, res) => {
  const user = await prisma.user.findUnique({
    where: { id: Number(req.params.id) },
  });
  if (!user) return res.sendStatus(404);
  res.json(user);
});
```

Creating a new client per request would create new connection pools and quickly exhaust database connections. Newer Prisma versions generate the client to a path you choose, so the import path may be different in your project.

### 181: Should you start the server before or after connecting to the database?

Usually after. Connect first, then call `listen`. That way the app does not accept traffic it cannot serve, and a bad connection string fails fast at startup:

```js
async function main() {
  await db.connect();
  app.listen(process.env.PORT || 3000);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

### 182: How do you do dependency injection in an Express app without a framework?

Build the app with a factory function that takes its dependencies:

```js
function createApp({ userService, logger }) {
  const app = express();
  app.use(express.json());
  app.get("/users/:id", async (req, res) => {
    const user = await userService.get(req.params.id);
    if (!user) return res.sendStatus(404);
    res.json(user);
  });
  return app;
}

// production
const app = createApp({ userService: new UserService(pool), logger });

// tests
const app = createApp({
  userService: { get: async () => ({ id: 1 }) },
  logger: console,
});
```

This makes testing simple without mocking modules. Libraries like `awilix` can help in bigger apps.

### 183: How do you write unit tests for a single middleware?

Call it with fake `req`, `res` and `next`:

```js
test("requireRole blocks non-admin", () => {
  const req = { user: { role: "user" } };
  const res = { sendStatus: vi.fn() };
  const next = vi.fn();

  requireRole("admin")(req, res, next);

  expect(res.sendStatus).toHaveBeenCalledWith(403);
  expect(next).not.toHaveBeenCalled();
});
```

For more complete fake objects, `node-mocks-http` creates `req` and `res` that behave like the real ones.

### 184: How do you write integration tests with a real database?

- Use a separate test database (often in Docker, or with Testcontainers).
- Run migrations before the tests.
- Clean data between tests: truncate tables, or wrap each test in a transaction and roll it back.
- Use `supertest` against the real app.

```js
beforeEach(async () => {
  await pool.query("TRUNCATE users RESTART IDENTITY CASCADE");
});

test("creates a user", async () => {
  const res = await request(app)
    .post("/users")
    .send({ email: "a@b.com", name: "A" });
  expect(res.status).toBe(201);
});
```

### 185: How do you test routes that need authentication?

Create a valid token or session in the test and send it:

```js
const token = jwt.sign({ sub: 1, role: "admin" }, process.env.JWT_SECRET);

const res = await request(app)
  .get("/admin/stats")
  .set("Authorization", `Bearer ${token}`);
```

For session-based apps, use `request.agent(app)`, which keeps cookies between calls, so you can log in once and then call protected routes.

### 186: Why does Jest say it "did not exit" after Express tests?

Something is still open: a server you started with `listen`, a database pool, or a Redis client. Fixes:

- Pass `app` to `supertest` instead of calling `listen`.
- Close pools and clients in `afterAll`.

```js
afterAll(async () => {
  await pool.end();
  await redis.quit();
});
```

`--detectOpenHandles` helps find what is still open.

### 187: How do you store uploads in memory with multer and send them to S3?

```js
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 10 * 1024 * 1024 },
});

app.post("/files", upload.single("file"), async (req, res) => {
  await s3.send(
    new PutObjectCommand({
      Bucket: process.env.BUCKET,
      Key: `uploads/${randomUUID()}`,
      Body: req.file.buffer,
      ContentType: req.file.mimetype,
    }),
  );
  res.sendStatus(201);
});
```

Memory storage holds the whole file in RAM, so keep a small limit. For big files, stream them, or let the client upload directly to S3 with a presigned URL.

### 188: How do you check the type of an uploaded file?

Do not trust the file name or `req.file.mimetype`, because the client sets them. Use multer's `fileFilter` for a first check, then check the actual bytes (magic numbers), for example with the `file-type` package:

```js
const upload = multer({
  fileFilter(req, file, cb) {
    cb(null, ["image/png", "image/jpeg"].includes(file.mimetype));
  },
});
```

Also limit size, never use the original name as a path on disk, and serve uploads from a different domain if possible.

### 189: How do you handle multer errors?

Multer passes errors to `next(err)`. Errors from its limits are `multer.MulterError` with a `code` like `LIMIT_FILE_SIZE`:

```js
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    return res.status(400).json({ error: err.code });
  }
  next(err);
});
```

### 190: How do you stream a large file in a response?

Use streams with `pipeline` so memory stays low and errors are handled:

```js
const { pipeline } = require("node:stream/promises");
const fs = require("node:fs");

app.get("/export", async (req, res) => {
  res.type("text/csv").attachment("export.csv");
  await pipeline(fs.createReadStream("/data/export.csv"), res);
});
```

For files on disk, `res.sendFile()` already streams and also supports range requests.

### 191: How do you stream database rows as JSON?

Write the response bit by bit instead of building one big array:

```js
app.get("/events", async (req, res) => {
  res.type("json");
  res.write("[");
  let first = true;
  for await (const row of db.streamEvents()) {
    if (!first) res.write(",");
    res.write(JSON.stringify(row));
    first = false;
  }
  res.end("]");
});
```

For very large data, also respect backpressure: when `res.write()` returns `false`, wait for the `'drain'` event. Newline-delimited JSON (NDJSON) is often easier for clients to process as a stream.

### 192: How do you implement Server-Sent Events (SSE) in Express?

Set the right headers, keep the response open and write events:

```js
app.get("/stream", (req, res) => {
  res.set({
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });
  res.flushHeaders();

  const timer = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  req.on("close", () => clearInterval(timer));
});
```

Turn off compression for this route, or flush after each write, otherwise events get buffered.

### 193: How do you add WebSockets to an Express app?

Express does not handle WebSockets itself. Create an HTTP server from the app and attach a WebSocket library to it:

```js
const http = require("node:http");
const { WebSocketServer } = require("ws");

const server = http.createServer(app);
const wss = new WebSocketServer({ server });

wss.on("connection", (socket) => {
  socket.on("message", (msg) => socket.send(`echo: ${msg}`));
});

server.listen(3000);
```

Socket.IO works the same way: `new Server(server)`.

### 194: How do you share the Express session with Socket.IO?

Reuse the session middleware on the Socket.IO engine:

```js
const sessionMiddleware = session({/* ... */});
app.use(sessionMiddleware);

io.engine.use(sessionMiddleware);

io.on("connection", (socket) => {
  const userId = socket.request.session.userId;
});
```

This way both HTTP routes and sockets use the same login.

### 195: How do you shut down an Express server gracefully?

On `SIGTERM`, stop accepting new connections, let current requests finish, then close database pools and exit:

```js
const server = app.listen(port);

process.on("SIGTERM", () => {
  server.close(async () => {
    await pool.end();
    process.exit(0);
  });
  server.closeIdleConnections();
  setTimeout(() => process.exit(1), 10_000).unref();
});
```

`server.close()` waits for keep-alive connections too, so `closeIdleConnections()` (Node 18.2+) helps it finish faster. The timeout makes sure the process does not hang forever.

### 196: Why should Kubernetes readiness checks fail during shutdown?

When a pod gets `SIGTERM`, the load balancer may still send it traffic for a few seconds. If the readiness endpoint starts returning 503 right away, Kubernetes removes the pod from the service before the server closes, so fewer requests fail:

```js
let shuttingDown = false;
app.get("/ready", (req, res) => res.sendStatus(shuttingDown ? 503 : 200));
process.on("SIGTERM", () => {
  shuttingDown = true; /* then close */
});
```

### 197: What is PM2 and when would you use it with Express?

PM2 is a process manager for Node. It restarts the app if it crashes, can run several copies with cluster mode, and handles logs:

```bash
pm2 start server.js -i max --name api
```

It is common on plain VMs. In Docker or Kubernetes, the platform already restarts and scales containers, so people usually run one `node` process per container without PM2.

### 198: How do you write a Dockerfile for an Express app?

```dockerfile
FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

Copy `package*.json` first so the dependency layer is cached. Run as a non-root user, and use the exec form of `CMD` so the Node process gets signals like `SIGTERM`.

### 199: Why put Nginx in front of an Express app?

A reverse proxy like Nginx can handle TLS, compress responses, serve static files fast, buffer slow clients, limit request sizes and spread traffic over several Node processes. Node then only handles the app logic. When you do this, set `trust proxy` in Express so `req.ip` and `req.protocol` are correct.

### 200: How does the `trust proxy` setting work in detail?

It tells Express which proxies to trust when reading `X-Forwarded-For`, `X-Forwarded-Proto` and `X-Forwarded-Host`. Values:

- `false` (default): ignore these headers.
- `true`: trust everything. Dangerous, because clients can fake `X-Forwarded-For`.
- A number: trust that many hops, like `1` for one load balancer.
- IPs or subnets: `'loopback, 10.0.0.0/8'`.
- A function `(ip) => boolean`.

Set it to match your real setup. A wrong value can let attackers fake their IP, which breaks rate limiting and logs.

### 201: How do you version an Express API?

The most common way is a version in the URL, with one router per version:

```js
app.use("/api/v1", v1Router);
app.use("/api/v2", v2Router);
```

Other options are a header (`Accept: application/vnd.myapp.v2+json`) or a custom header like `Api-Version`. URL versions are the easiest to cache, test and see in logs. Try to keep versions few by making changes that do not break old clients, like adding new fields instead of renaming.

### 202: How do you add OpenAPI (Swagger) docs to an Express app?

Write or generate an OpenAPI file and serve it with `swagger-ui-express`:

```js
const swaggerUi = require("swagger-ui-express");
const openapi = require("./openapi.json");

app.use("/docs", swaggerUi.serve, swaggerUi.setup(openapi));
```

You can generate the spec from JSDoc comments (`swagger-jsdoc`) or from zod schemas (`@asteasolutions/zod-to-openapi`). Generating it from the same schemas you use for validation keeps docs and code in sync.

### 203: How do you validate requests against an OpenAPI spec?

Use `express-openapi-validator`. It reads the spec and checks params, query, body and (optionally) responses:

```js
const OpenApiValidator = require("express-openapi-validator");

app.use(express.json());
app.use(
  OpenApiValidator.middleware({
    apiSpec: "./openapi.yaml",
    validateRequests: true,
    validateResponses: false,
  }),
);
```

Invalid requests get passed to your error handler with a `status` of 400. This is a "spec-first" approach where the spec is the source of truth.

### 204: How does Express handle `HEAD` requests?

If there is no `app.head()` route, Express runs the matching `GET` route for a `HEAD` request and Node drops the body, sending only headers. So you rarely need to write `HEAD` handlers. If you define `app.head()` for a path, it is used instead, as long as it comes before the `GET` route.

### 205: How does Express handle `OPTIONS` requests by default?

If no route handles `OPTIONS` for a path, Express responds automatically with status 200 and an `Allow` header that lists the methods defined for that path (for example `GET, HEAD, POST`). The `cors` middleware replaces this behavior for preflight requests when it is mounted with `app.use`.

### 206: How do you return 405 Method Not Allowed?

Express returns 404 when the path exists but the method does not. To return 405, add an `all` handler at the end of a route chain:

```js
app
  .route("/users")
  .get(listUsers)
  .post(createUser)
  .all((req, res) => {
    res.set("Allow", "GET, POST").sendStatus(405);
  });
```

### 207: How do you redirect URLs with a trailing slash?

Express treats `/about` and `/about/` the same unless `strict routing` is on. If you want one form for SEO, redirect in a middleware:

```js
app.use((req, res, next) => {
  if (req.path.length > 1 && req.path.endsWith("/")) {
    const query = req.url.slice(req.path.length);
    return res.redirect(301, req.path.slice(0, -1) + query);
  }
  next();
});
```

### 208: How do you route by subdomain or host?

Check `req.hostname` in a middleware, or use the `vhost` package to mount different apps:

```js
const vhost = require("vhost");

app.use(vhost("api.example.com", apiApp));
app.use(vhost("admin.example.com", adminApp));
```

### 209: What is a sub-app in Express, and how is it different from a router?

You can mount a full Express app inside another with `app.use('/blog', blogApp)`. A sub-app has its own settings (view engine, `trust proxy`, and so on), its own `app.locals` and its own `mount` event. A router is lighter and shares the parent's settings. Use a router for splitting routes, and a sub-app when a part really needs different settings.

```js
const blog = express();
blog.on("mount", (parent) => console.log("blog mounted at", blog.mountpath));
app.use("/blog", blog);
```

### 210: How do you proxy requests from Express to another service?

Use `http-proxy-middleware`:

```js
const { createProxyMiddleware } = require("http-proxy-middleware");

app.use(
  "/api",
  createProxyMiddleware({
    target: "http://orders-service:4000",
    changeOrigin: true,
  }),
);
```

Mount it before `express.json()`, or the body will already be read and the proxy will forward an empty body. If you need to parse the body too, use the library's `fixRequestBody` helper.

### 211: How do you run an Express app on AWS Lambda or other serverless platforms?

Wrap the app with an adapter like `serverless-http` (or `@codegenie/serverless-express`):

```js
const serverless = require("serverless-http");
const app = require("./app");

module.exports.handler = serverless(app);
```

Keep the app setup outside the handler so it is reused between warm calls. Be careful with things that need a long-running process, like WebSockets, in-memory caches and background timers.

### 212: How do you use all CPU cores with Express?

Node runs your JavaScript on one thread, so one process uses about one core. Options:

- Run several processes with Node's `cluster` module or PM2 cluster mode.
- Run several containers or pods behind a load balancer.

```js
const cluster = require("node:cluster");
const os = require("node:os");

if (cluster.isPrimary) {
  for (let i = 0; i < os.availableParallelism(); i++) cluster.fork();
} else {
  require("./server");
}
```

Each process has its own memory, so sessions, rate limits and caches must live in a shared store like Redis.

### 213: How do you cache API responses with Redis?

Check the cache first, then fall back to the database and save the result with a TTL:

```js
app.get("/products/:id", async (req, res) => {
  const key = `product:${req.params.id}`;
  const cached = await redis.get(key);
  if (cached) return res.type("json").send(cached);

  const product = await Product.findById(req.params.id);
  if (!product) return res.sendStatus(404);

  const body = JSON.stringify(product);
  await redis.set(key, body, { EX: 60 });
  res.type("json").send(body);
});
```

Delete or update the key when the product changes.

### 214: How do you set HTTP caching headers on API responses?

Set `Cache-Control` per route based on how often data changes:

```js
app.get("/countries", (req, res) => {
  res.set("Cache-Control", "public, max-age=3600");
  res.json(countries);
});

app.get("/me", (req, res) => {
  res.set("Cache-Control", "private, no-store");
  res.json(req.user);
});
```

Use `private` or `no-store` for user-specific data so CDNs and shared caches do not store it.

### 215: What timeouts does a Node HTTP server have, and how do you set them on Express?

They are on the server returned by `app.listen()`:

- `server.requestTimeout`: max time to receive the whole request (default 300000 ms).
- `server.headersTimeout`: max time to receive headers (default 60000 ms).
- `server.keepAliveTimeout`: how long an idle keep-alive connection stays open (default 5000 ms).
- `server.timeout`: socket inactivity timeout (default 0, disabled).

```js
const server = app.listen(3000);
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000;
```

Behind an AWS load balancer, `keepAliveTimeout` should be longer than the balancer's idle timeout (60 s by default), or you get random 502 errors.

### 216: How do you add a timeout to a single slow route?

Node's server timeouts are global. For one route, you can race the work against a timer or use `AbortSignal.timeout`:

```js
app.get("/report", async (req, res) => {
  const signal = AbortSignal.timeout(5000);
  try {
    const data = await fetch(REPORT_URL, { signal }).then((r) => r.json());
    res.json(data);
  } catch (err) {
    if (err.name === "TimeoutError")
      return res.status(504).json({ error: "Timed out" });
    throw err;
  }
});
```

There is also the `connect-timeout` middleware, but it only sets a flag; your code still has to stop the work.

### 217: How do you stop work when the client disconnects?

Listen for the `close` event and use an `AbortController`:

```js
app.get("/search", async (req, res) => {
  const controller = new AbortController();
  req.on("close", () => {
    if (!res.writableEnded) controller.abort();
  });

  const results = await searchService.run(req.query.q, {
    signal: controller.signal,
  });
  if (!controller.signal.aborted) res.json(results);
});
```

This saves CPU and database time on requests that nobody is waiting for anymore.

### 218: How do you call another HTTP API from an Express route?

Node 18+ has a global `fetch`:

```js
app.get("/weather/:city", async (req, res) => {
  const url = `https://api.example.com/weather?city=${encodeURIComponent(req.params.city)}`;
  const response = await fetch(url, { signal: AbortSignal.timeout(3000) });
  if (!response.ok) return res.status(502).json({ error: "Upstream error" });
  res.json(await response.json());
});
```

Always set a timeout, encode user input in URLs, and map upstream errors to 502 or 504 instead of passing them through as is.

### 219: How do you read the raw body and also parse JSON?

Use the `verify` option of `express.json()`, which gets the raw buffer before parsing:

```js
app.use(
  express.json({
    verify(req, res, buf) {
      req.rawBody = buf;
    },
  }),
);
```

This is handy for webhooks that sign the raw body, when you still want `req.body` as an object.

### 220: Why does a webhook signature check fail when you use `express.json()`?

The signature is computed over the exact bytes the sender sent. Once you parse and re-stringify the JSON, spaces and key order may change, so the signature does not match. Use `express.raw({ type: 'application/json' })` on the webhook route (before any global `express.json()`), or save the raw body with the `verify` option.

### 221: How do you make `express.json()` accept other content types?

Use the `type` option. It can be a string, an array or a function:

```js
app.use(express.json({ type: ["application/json", "application/*+json"] }));
```

By default it only parses `application/json`. This is useful for things like `application/merge-patch+json` or `application/problem+json`.

### 222: Does Express support compressed request bodies?

Yes. The body parsers handle `Content-Encoding: gzip` and `deflate`, and Express 5 (with body-parser 2) also handles `br` (Brotli). You can turn this off with `inflate: false`, which makes the parser reject compressed bodies with 415. Keep the `limit` in mind, because it applies to the size after decompression.

### 223: How do you prevent NoSQL injection in an Express + MongoDB app?

Attackers can send objects instead of strings, like `{ "email": { "$ne": null } }`, which can change the meaning of a query. Fixes:

- Validate input with a schema, so `email` must be a string.
- Cast values, like `String(req.body.email)`.
- Use Mongoose's `sanitizeFilter` option, which wraps `$` keys in `$eq`.

```js
mongoose.set("sanitizeFilter", true);
```

Be careful with old sanitizer middleware that writes to `req.query`, because that breaks in Express 5.

### 224: How do you prevent XSS in an Express app that renders HTML?

- Let the template engine escape values (`<%= %>` in EJS, `{{ }}` in Handlebars). Avoid the unescaped forms with user data.
- Set a strict Content Security Policy with `helmet`.
- Set `httpOnly` on cookies so scripts cannot read them.
- Sanitize user HTML with a library like `DOMPurify` (with `jsdom`) or `sanitize-html` if you must allow some HTML.

For a JSON API, make sure `Content-Type` is `application/json` so browsers do not treat the response as HTML.

### 225: What is HTTP parameter pollution and how does it affect Express?

Clients can send the same query key twice, like `?sort=name&sort=age`. Then `req.query.sort` is an array, not a string. Code that calls `req.query.sort.toLowerCase()` will crash, and checks like `=== 'asc'` may be bypassed. Validate types with a schema, or use the `hpp` middleware to keep only the last value.

### 226: How do you validate environment variables at startup?

Check them once and fail fast if something is missing:

```js
const { z } = require("zod");

const env = z
  .object({
    NODE_ENV: z
      .enum(["development", "test", "production"])
      .default("development"),
    PORT: z.coerce.number().default(3000),
    DATABASE_URL: z.string().url(),
    JWT_SECRET: z.string().min(32),
  })
  .parse(process.env);

module.exports = env;
```

This avoids problems like the app starting fine and then failing on the first request that needs the missing variable.

### 227: How do you separate routes, controllers and services?

- Route files map paths and methods to controller functions and add middleware.
- Controllers read `req`, call services and write `res`.
- Services contain business logic and know nothing about HTTP.
- Repositories or models talk to the database.

```js
// service
async function registerUser({ email, password }) {
  if (await users.findByEmail(email)) throw new ConflictError("Email taken");
  return users.create({ email, passwordHash: await hash(password) });
}

// controller
exports.register = async (req, res) => {
  const user = await userService.registerUser(req.valid.body);
  res.status(201).json({ id: user.id, email: user.email });
};
```

Services can then be reused from scripts, jobs or tests without fake `req` and `res`.

### 228: Why should you not send database models directly in responses?

Models often have fields you should not show, like `passwordHash`, internal flags or other users' data. Also, your API would change every time the database changes. Map the model to a response object:

```js
const toUserResponse = (u) => ({ id: u.id, email: u.email, name: u.name });
res.json(toUserResponse(user));
```

### 229: How do you implement cursor-based pagination?

Use the last item's sort key as the cursor instead of an offset:

```js
app.get("/messages", async (req, res) => {
  const limit = Math.min(Number(req.query.limit) || 20, 100);
  const cursor = req.query.cursor ? Number(req.query.cursor) : null;

  const rows = await db.query(
    `SELECT id, text FROM messages
     WHERE ($1::bigint IS NULL OR id < $1)
     ORDER BY id DESC LIMIT $2`,
    [cursor, limit + 1],
  );

  const hasMore = rows.length > limit;
  const data = rows.slice(0, limit);
  res.json({ data, nextCursor: hasMore ? data.at(-1).id : null });
});
```

It stays fast on big tables and does not skip or repeat rows when new data is added.

### 230: How do you let clients sort and filter safely?

Use an allow list for field names and never put raw input into a query:

```js
const SORT_FIELDS = new Set(["createdAt", "price", "name"]);

app.get("/products", async (req, res) => {
  const sort = SORT_FIELDS.has(req.query.sort) ? req.query.sort : "createdAt";
  const order = req.query.order === "asc" ? "asc" : "desc";
  const products = await prisma.product.findMany({
    orderBy: { [sort]: order },
    take: 50,
  });
  res.json(products);
});
```

### 231: What is an idempotency key and how do you add it to an Express API?

It is a unique key the client sends with a request (often `Idempotency-Key` header) so a retry does not repeat the action, like charging a card twice. The server stores the result for that key and returns it again on retry:

```js
app.post("/payments", async (req, res) => {
  const key = req.get("Idempotency-Key");
  if (!key) return res.status(400).json({ error: "Idempotency-Key required" });

  const saved = await redis.get(`idem:${key}`);
  if (saved) {
    const { status, body } = JSON.parse(saved);
    return res.status(status).json(body);
  }

  const payment = await createPayment(req.body);
  await redis.set(
    `idem:${key}`,
    JSON.stringify({ status: 201, body: payment }),
    { EX: 86400 },
  );
  res.status(201).json(payment);
});
```

In real code, also lock the key while the first request runs, so two parallel retries do not both run.

### 232: How do you use `AsyncLocalStorage` for request context in Express?

It lets you read request data (like the request ID or user) anywhere in the call chain without passing it through every function:

```js
const { AsyncLocalStorage } = require("node:async_hooks");
const context = new AsyncLocalStorage();

app.use((req, res, next) => {
  context.run({ requestId: req.id }, next);
});

function log(msg) {
  const store = context.getStore();
  console.log(JSON.stringify({ requestId: store?.requestId, msg }));
}
```

Loggers and tracing tools use this inside.

### 233: How do you add types for custom properties on `req` in TypeScript?

Extend the `Express.Request` interface in a declaration file:

```ts
// src/types/express.d.ts
import "express";

declare global {
  namespace Express {
    interface Request {
      user?: { id: string; role: "admin" | "user" };
      id?: string;
    }
  }
}
```

Make sure the file is included in `tsconfig.json`. Then `req.user` is typed in every handler.

### 234: How do you type `req.body`, `req.params` and `req.query` in TypeScript?

`Request` takes generics in this order: params, response body, request body, query:

```ts
import type { Request, Response } from "express";

type Params = { id: string };
type Body = { name: string };
type Query = { include?: string };

app.put(
  "/users/:id",
  (req: Request<Params, unknown, Body, Query>, res: Response) => {
    req.params.id; // string
    req.body.name; // string
    req.query.include;
    res.sendStatus(204);
  },
);
```

These are only types. Nothing checks them at runtime, so you still need validation.

### 235: What does an Express handler do with its return value?

Express ignores normal return values. In Express 5 it checks if the return value is a promise, and if it rejects, it calls `next(err)`. That is why `return res.json(x)` works fine: the `return` just stops the function. Returning data does not send it; you must call a `res` method.

### 236: How do you share middleware between several apps or services?

Put it in a package or a shared folder, and export factory functions that take options:

```js
// @acme/express-common
exports.requestId = () => (req, res, next) => {
  /* ... */
};
exports.errorHandler =
  ({ logger }) =>
  (err, req, res, next) => {
    /* ... */
  };
```

Make `express` a `peerDependency` so the services do not end up with two copies of Express.

### 237: How do you serve uploaded files safely?

- Do not serve the upload folder with `express.static` if users can upload HTML or SVG, since that can run scripts on your domain.
- Store files with random names, outside the web root.
- Serve them with a route that checks permission and sets safe headers:

```js
app.get("/files/:id", authenticate, async (req, res) => {
  const file = await File.findForUser(req.params.id, req.user.id);
  if (!file) return res.sendStatus(404);
  res.set("X-Content-Type-Options", "nosniff");
  res.download(file.storagePath, file.originalName);
});
```

A separate domain or a storage service (S3 with signed URLs) is even better.

### 238: How do you prevent path traversal with `res.sendFile()`?

Never pass user input straight into a file path. Use the `root` option, which makes Express refuse paths that leave that folder:

```js
app.get("/docs/:name", (req, res) => {
  res.sendFile(req.params.name, { root: path.join(__dirname, "docs") });
});
```

With `root`, a path containing `..` gets a 403. If you build the path yourself, resolve it and check it still starts with the base folder. Do not count on route params to block slashes: params are URL-decoded, so `..%2F..%2Fetc%2Fpasswd` arrives as `../../etc/passwd`.

### 239: How do you handle `res.sendFile()` errors?

Pass a callback, or in Express 5 let it go to the error handler. A missing file gives an error with `status: 404`:

```js
res.sendFile(filePath, (err) => {
  if (err) next(err);
});
```

Do not try to send another response if `res.headersSent` is already true, because part of the file may have been sent.

### 240: How do you add a method like PUT to an HTML form?

HTML forms only send GET and POST. The `method-override` package lets a hidden field or header change the method:

```js
const methodOverride = require("method-override");
app.use(express.urlencoded({ extended: false }));
app.use(methodOverride("_method"));
```

```html
<form method="POST" action="/posts/1?_method=DELETE">
  <button>Delete</button>
</form>
```

In modern apps, `fetch` can send any method, so this is mostly for server-rendered pages.

### 241: How do you add flash messages to a server-rendered Express app?

Flash messages are stored in the session and shown once on the next page. Use `connect-flash` or write it yourself:

```js
app.use((req, res, next) => {
  res.locals.flash = req.session.flash;
  delete req.session.flash;
  next();
});

app.post("/posts", async (req, res) => {
  await createPost(req.body);
  req.session.flash = { type: "success", text: "Post created" };
  res.redirect("/posts");
});
```

### 242: How do you use layouts and partials with EJS?

EJS supports includes:

```html
<%- include('partials/header', { title }) %>
<main>...</main>
<%- include('partials/footer') %>
```

For real layouts (one file wrapping every page), use a package like `express-ejs-layouts`, or switch to an engine with built-in layouts like Pug or Handlebars.

### 243: Why are templates slow in development but fast in production?

The `view cache` setting is enabled when `NODE_ENV` is `production`. Then Express compiles each template once and reuses it. In development it re-reads and re-compiles templates on each render so you see changes right away. Forgetting to set `NODE_ENV=production` makes rendering much slower in production.

### 244: How do you debug an Express app with breakpoints?

Start Node with the inspector:

```bash
node --inspect app.js
```

Then open `chrome://inspect` in Chrome, or use VS Code's debugger (a "JavaScript Debug Terminal" works with no config). You can put breakpoints in route handlers and middleware and inspect `req` and `res`.

### 245: How do you find which middleware is slow?

- Log time per request with `pino-http` or `morgan` (`:response-time`).
- Use the `Server-Timing` header to show durations in the browser's DevTools.
- Use OpenTelemetry's Express instrumentation, which creates a span per middleware and route.
- Profile with `node --cpu-prof` or Clinic.js when you see high CPU.

### 246: How do you add OpenTelemetry tracing to Express?

Load the SDK before anything else, with the auto-instrumentations package:

```js
// tracing.js
const { NodeSDK } = require("@opentelemetry/sdk-node");
const {
  getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");

new NodeSDK({ instrumentations: [getNodeAutoInstrumentations()] }).start();
```

```bash
node --require ./tracing.js server.js
```

It creates spans for incoming requests, Express routes and middleware, database calls and outgoing HTTP calls. The exporter (OTLP to Jaeger, Tempo, Datadog and so on) is set with environment variables.

### 247: How do you expose Prometheus metrics from Express?

Use `prom-client` and record a histogram per request:

```js
const client = require("prom-client");
client.collectDefaultMetrics();

const httpDuration = new client.Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route", "status"],
});

app.use((req, res, next) => {
  const end = httpDuration.startTimer();
  res.on("finish", () => {
    end({
      method: req.method,
      route: req.route?.path ?? "unknown",
      status: res.statusCode,
    });
  });
  next();
});

app.get("/metrics", async (req, res) => {
  res.type(client.register.contentType).send(await client.register.metrics());
});
```

Use the route pattern, not the real URL, as a label, or you will create a new time series for every ID.

### 248: How do you report errors to a service like Sentry?

Most error trackers have Express support. With Sentry, you initialize it first and then add its error handler before your own:

```js
// instrument.js, loaded first
const Sentry = require("@sentry/node");
Sentry.init({ dsn: process.env.SENTRY_DSN });

// app.js
Sentry.setupExpressErrorHandler(app); // after routes, before your error handler
app.use(myErrorHandler);
```

Report only unexpected errors (5xx), not normal 404s and validation errors, or the real problems get lost.

### 249: What should you do on `uncaughtException` and `unhandledRejection`?

Log the error and exit, and let the process manager (Docker, Kubernetes, PM2) start a fresh process:

```js
process.on("uncaughtException", (err) => {
  logger.fatal(err, "uncaught exception");
  process.exit(1);
});

process.on("unhandledRejection", (reason) => {
  logger.fatal({ reason }, "unhandled rejection");
  process.exit(1);
});
```

After an uncaught exception, the app may be in a broken state, so keeping it running is risky. Since Node 15, unhandled rejections crash the process by default anyway.

### 250: How do you make an Express app return JSON 404 for the API and an HTML page for the website?

Put a 404 handler on the API router and another at the app level:

```js
api.use((req, res) => res.status(404).json({ error: "Not found" }));
app.use("/api", api);

app.use(express.static("public"));
app.use((req, res) => res.status(404).render("404"));
```

Because the API router ends every unmatched `/api` request itself, website handlers never see those requests.

### 251: How do you write middleware that runs after the response is sent?

Listen to the `finish` event on `res` (and `close` for aborted requests):

```js
app.use((req, res, next) => {
  const start = process.hrtime.bigint();
  res.on("finish", () => {
    const ms = Number(process.hrtime.bigint() - start) / 1e6;
    console.log(
      `${req.method} ${req.originalUrl} ${res.statusCode} ${ms.toFixed(1)}ms`,
    );
  });
  next();
});
```

Code after `next()` in a middleware does not wait for the response, because Express middleware is not "onion" style like Koa.

### 252: What is the difference between Express middleware and Koa middleware?

In Koa, middleware is `async (ctx, next) => {}` and `await next()` waits for everything downstream to finish, so you can run code before and after (the "onion" model). In Express, `next()` just calls the next function and returns right away; it does not wait for later async work. To run code after the response in Express, use `res.on('finish')`.

### 253: How do you compose several middleware into one?

Express accepts arrays, so you can group middleware:

```js
const protect = [authenticate, requireRole("admin"), rateLimiter];

app.delete("/users/:id", protect, deleteUser);
app.use("/admin", protect, adminRouter);
```

You can also make a router that has the middleware and mount it, since a router is itself a middleware.

### 254: How do you run middleware only when a condition is true?

Wrap it:

```js
const when = (cond, mw) => (req, res, next) =>
  cond(req) ? mw(req, res, next) : next();

app.use(when((req) => !req.path.startsWith("/health"), morgan("combined")));
```

This is handy for skipping logging or auth on health checks.

### 255: How do you handle JSON body for some routes and raw body for others?

Mount the raw parser on the special route before the global JSON parser, or do not use a global parser at all:

```js
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  stripeWebhook,
);

app.use(express.json());
app.use("/api", apiRouter);
```

Once a body parser reads the stream, the next parser sees it as already read and skips it.

### 256: How does a body parser know the body was already parsed?

The body parsers mark the request as read (they check an internal flag and whether the stream was consumed). If an earlier parser already read the body, later parsers call `next()` without doing anything. They also skip when the `Content-Type` does not match their `type` option, or when the request has no body.

### 257: How do you write a simple in-memory cache middleware?

```js
function cache(ttlMs) {
  const store = new Map();
  return (req, res, next) => {
    if (req.method !== "GET") return next();
    const hit = store.get(req.originalUrl);
    if (hit && hit.expires > Date.now()) return res.json(hit.body);

    const json = res.json.bind(res);
    res.json = (body) => {
      if (res.statusCode === 200)
        store.set(req.originalUrl, { body, expires: Date.now() + ttlMs });
      return json(body);
    };
    next();
  };
}

app.get("/stats", cache(30_000), getStats);
```

It is per process and grows without limit, so use an LRU cache or Redis in real apps.

### 258: What is the downside of patching `res.json` or `res.send` in middleware?

It is easy to break things: other middleware may patch the same method, `res.send` calls `res.json` in some paths, and streaming responses never go through it. It is also hard to read. Prefer clear options, like having the handler call a cache service directly, or using `res.on('finish')` for things that only need to observe.

### 259: How do you implement soft authentication (user is optional)?

Set `req.user` if a valid token is there, but never block:

```js
function optionalAuth(req, res, next) {
  const token = req.get("Authorization")?.replace(/^Bearer /, "");
  if (token) {
    try {
      req.user = jwt.verify(token, process.env.JWT_SECRET, {
        algorithms: ["HS256"],
      });
    } catch {
      // ignore bad token, treat as anonymous
    }
  }
  next();
}
```

Useful for pages that show extra data to logged in users.

### 260: How do you implement role-based access control in Express?

Store roles on the user, put them in the token or session, and check them in middleware:

```js
const permissions = {
  admin: ["users:read", "users:write", "orders:read"],
  support: ["users:read", "orders:read"],
};

const can = (perm) => (req, res, next) => {
  if (!req.user) return res.sendStatus(401);
  if (!permissions[req.user.role]?.includes(perm)) return res.sendStatus(403);
  next();
};

router.delete("/users/:id", can("users:write"), deleteUser);
```

Checking permissions instead of role names makes it easier to change roles later.

### 261: How do you check that a user owns the resource they want to change?

Load the resource and compare the owner in the handler or service. Role checks are not enough for this:

```js
router.patch("/posts/:id", authenticate, async (req, res) => {
  const post = await Post.findById(req.params.id);
  if (!post) return res.sendStatus(404);
  if (post.authorId !== req.user.id && req.user.role !== "admin")
    return res.sendStatus(403);
  await post.update(req.body);
  res.json(post);
});
```

Missing this check is called IDOR (insecure direct object reference) and is one of the most common API bugs. Some teams return 404 instead of 403 so they do not reveal that the record exists.

### 262: How do you hash passwords in an Express app?

Use a slow password hash like `argon2` or `bcrypt`. Never store plain or fast hashes (MD5, SHA-256):

```js
const argon2 = require("argon2");

const hash = await argon2.hash(password);
const ok = await argon2.verify(hash, passwordFromLogin);
```

These are CPU-heavy, but the libraries run the work on the libuv thread pool, so they do not block the event loop.

### 263: How do you implement "login with Google" in Express?

Use OAuth 2.0 / OpenID Connect with a library like `passport-google-oauth20` or `openid-client`:

1. `GET /auth/google` redirects to Google with your client ID, scopes, a `state` and a PKCE challenge.
2. Google redirects back to `/auth/google/callback?code=...`.
3. The server checks `state`, exchanges the code for tokens and reads the user's ID token.
4. Find or create the user, then start your own session.

Never trust user info from the query string; always get it from the token exchange.

### 264: How do you send emails from an Express app without slowing requests?

Do not send them inside the request if you can avoid it. Put a job on a queue and return right away:

```js
app.post("/signup", async (req, res) => {
  const user = await createUser(req.body);
  await emailQueue.add("welcome", { userId: user.id }); // BullMQ, for example
  res.status(201).json({ id: user.id });
});
```

A worker process sends the email with retries. If the email provider is slow or down, signup still works.

### 265: How do you run background jobs alongside Express?

For small tasks you can use timers or `node-cron` in the same process, but they run on every instance and stop when the app restarts. For real jobs, use a queue like BullMQ (Redis) and a separate worker process. That way jobs survive restarts, can be retried, and heavy work does not slow down API requests.

### 266: How do you return a file generated on the fly, like a CSV?

Set the headers and stream the data:

```js
const { stringify } = require("csv-stringify");
const { pipeline } = require("node:stream/promises");

app.get("/users.csv", async (req, res) => {
  res.type("text/csv").attachment("users.csv");
  await pipeline(db.streamUsers(), stringify({ header: true }), res);
});
```

Streaming means you do not hold the whole file in memory.

### 267: How do you enable gzip only for big responses?

`compression` has a `threshold` option (default `1kb`) and a `filter` function:

```js
app.use(
  compression({
    threshold: 2048,
    filter: (req, res) => {
      if (req.get("x-no-compression")) return false;
      return compression.filter(req, res);
    },
  }),
);
```

Small responses are not worth the CPU time, and already compressed data like images gains nothing.

### 268: Why can compression break Server-Sent Events?

`compression` buffers output to compress it in chunks, so SSE messages get stuck until the buffer fills. Either skip compression for `text/event-stream` (the default filter does compress it), or call `res.flush()`, which `compression` adds to `res`, after each event:

```js
res.write(`data: ${json}\n\n`);
res.flush?.();
```

### 269: How do you limit how many requests an Express process handles at once?

Node itself has no limit. You can:

- Set `server.maxConnections`.
- Add a concurrency limit for expensive routes with a simple counter or a library like `p-limit`.
- Return `503` with `Retry-After` when overloaded, for example with `overload-protection` or by checking event loop delay.

```js
let active = 0;
const MAX = 50;

app.use("/reports", (req, res, next) => {
  if (active >= MAX) return res.set("Retry-After", "5").sendStatus(503);
  active++;
  res.on("close", () => active--);
  next();
});
```

### 270: How do you serve different API responses based on `Accept-Language`?

Use `req.acceptsLanguages()` to pick the best supported language:

```js
const supported = ["en", "de", "fr"];

app.use((req, res, next) => {
  req.lang = req.acceptsLanguages(...supported) || "en";
  res.vary("Accept-Language");
  next();
});
```

Then pass `req.lang` to your translation library, like `i18next`. Setting `Vary` keeps caches from mixing languages.

### 271: What is the `json replacer` setting used for?

It is passed as the second argument to `JSON.stringify` in `res.json()`. You can use it to hide fields or convert types globally:

```js
app.set("json replacer", (key, value) => {
  if (key === "passwordHash") return undefined;
  if (typeof value === "bigint") return value.toString();
  return value;
});
```

It runs for every key of every response, so keep it simple. Explicit response mapping is usually clearer.

### 272: Why does `res.json()` throw on BigInt values?

`JSON.stringify` cannot serialize `BigInt` and throws `TypeError: Do not know how to serialize a BigInt`. This often shows up with databases that return 64-bit integers (Prisma `BigInt` columns, for example). Convert them to strings or numbers before sending, or use the `json replacer` setting.

### 273: How do you write a request logger that skips health checks?

With `morgan`, use the `skip` option:

```js
app.use(
  morgan("combined", {
    skip: (req) => req.path === "/health" || req.path === "/ready",
  }),
);
```

With `pino-http`, use `autoLogging: { ignore: (req) => req.url === '/health' }`.

### 274: What are the trade-offs between sessions and JWTs for an Express app?

Sessions keep data on the server and send only an ID cookie. They are easy to revoke and small, but need a shared store when you scale. JWTs keep data in the token, so any service with the key can check them without a lookup. But they are hard to revoke before they expire, can get large, and the claims can become old (for example a role changed). For one web app with a browser client, sessions are often simpler. For many services or third-party clients, short-lived JWTs are common.

### 275: How do you implement API key authentication?

Give each client a random key, store only its hash, and check it in middleware:

```js
const crypto = require("node:crypto");

async function apiKeyAuth(req, res, next) {
  const key = req.get("X-Api-Key");
  if (!key) return res.sendStatus(401);
  const hash = crypto.createHash("sha256").update(key).digest("hex");
  const client = await ApiKey.findOne({ hash, revoked: false });
  if (!client) return res.sendStatus(401);
  req.client = client;
  next();
}
```

A fast hash like SHA-256 is fine here because the keys are long random values, not human passwords.

### 276: Why should you use `crypto.timingSafeEqual` when comparing secrets?

A normal `===` stops at the first different character, so the time it takes can leak how much of a secret is correct. `timingSafeEqual` always takes the same time:

```js
const a = Buffer.from(given);
const b = Buffer.from(expected);
const ok = a.length === b.length && crypto.timingSafeEqual(a, b);
```

Use it for webhook signatures, static tokens and HMAC checks.

### 277: How do you verify a webhook HMAC signature in Express?

```js
app.post(
  "/webhooks/github",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const expected =
      "sha256=" +
      crypto
        .createHmac("sha256", process.env.GITHUB_WEBHOOK_SECRET)
        .update(req.body)
        .digest("hex");
    const given = req.get("X-Hub-Signature-256") || "";

    const ok =
      given.length === expected.length &&
      crypto.timingSafeEqual(Buffer.from(given), Buffer.from(expected));
    if (!ok) return res.sendStatus(401);

    const event = JSON.parse(req.body.toString("utf8"));
    handleEvent(event);
    res.sendStatus(204);
  },
);
```

Answer webhooks quickly and do slow work in a background job, or the sender may time out and retry.

### 278: How do you make sure cookies work behind a proxy with `secure: true`?

`express-session` (and `res.cookie` with `secure`) only sends secure cookies when it thinks the connection is HTTPS. Behind a proxy that ends TLS, Express sees HTTP. Set `trust proxy` so it reads `X-Forwarded-Proto`:

```js
app.set("trust proxy", 1);
app.use(session({ cookie: { secure: true } /* ... */ }));
```

Without it, the session cookie is never set and logins seem to "not stick".

### 279: What cookie settings should an auth cookie have?

- `httpOnly: true` so JavaScript cannot read it.
- `secure: true` so it is only sent over HTTPS.
- `sameSite: 'lax'` (or `'strict'`) to limit cross-site sending.
- A short `maxAge`, plus server-side expiry.
- A narrow `path` if possible.
- Optionally the `__Host-` name prefix, which requires `secure`, `path=/` and no `domain`.

### 280: How do you share code between route handlers without repeating `try/catch`?

In Express 5 you do not need `try/catch` for errors you want to pass on; just let them throw. Catch only when you want to change the error, like turning a database "unique violation" into a 409:

```js
router.post("/", async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json(user);
  } catch (err) {
    if (err.code === "23505") throw new ConflictError("Email already used");
    throw err;
  }
});
```

Even better, do this mapping once in the error handler or the repository layer.

### 281: How do you map database errors to HTTP errors in one place?

Check the error type in an error handler before the final one:

```js
app.use((err, req, res, next) => {
  if (err.code === "23505")
    return res.status(409).json({ error: "Already exists" }); // Postgres unique
  if (err.code === "P2025") return res.status(404).json({ error: "Not found" }); // Prisma record not found
  if (err.name === "CastError")
    return res.status(400).json({ error: "Invalid id" }); // Mongoose
  next(err);
});
```

Do not send raw database messages to clients, since they can show table names and other details.

### 282: How do you return validation errors in a useful format?

Return 400 (or 422) with a list of errors, each pointing to a field:

```json
{
  "error": "ValidationError",
  "details": [
    { "path": "email", "message": "Invalid email" },
    { "path": "password", "message": "Must be at least 8 characters" }
  ]
}
```

Clients can then show the message next to the right form field. Keep the format the same across all endpoints.

### 283: How do you make an Express app handle both JSON and form submissions on the same route?

Add both parsers. Each only runs for its own `Content-Type`:

```js
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.post("/contact", (req, res) => {
  // works for application/json and application/x-www-form-urlencoded
  saveMessage(req.body);
  res.format({
    json: () => res.status(201).json({ ok: true }),
    html: () => res.redirect("/thanks"),
  });
});
```

### 284: How do you mock a service in a supertest test?

If the app is built with a factory, pass a fake:

```js
const app = createApp({
  paymentService: { charge: vi.fn().mockResolvedValue({ id: "p_1" }) },
});

const res = await request(app).post("/checkout").send({ amount: 100 });
expect(res.status).toBe(201);
```

Otherwise, use your test runner's module mocking (`vi.mock`, `jest.mock`). Mocking at the HTTP edge (with `nock` or MSW) is good for testing calls to third-party APIs.

### 285: How do you test error handling middleware?

Make a test-only route that throws, then check the response:

```js
const app = createApp();
app.get("/boom", () => {
  throw new Error("test");
});
app.use(errorHandler);

const res = await request(app).get("/boom");
expect(res.status).toBe(500);
expect(res.body).toEqual({
  error: { code: "INTERNAL", message: "Internal Server Error" },
});
```

Make sure the error handler is added after the test route.

### 286: How do you test file uploads with supertest?

Use `.attach()` for files and `.field()` for other form fields:

```js
const res = await request(app)
  .post("/avatar")
  .set("Authorization", `Bearer ${token}`)
  .field("description", "me")
  .attach("avatar", Buffer.from("fake image"), "me.png");

expect(res.status).toBe(201);
```

### 287: How do you run Express tests in parallel without conflicts?

- Do not listen on fixed ports; pass `app` to supertest.
- Give each test worker its own database or schema (using the worker ID, like `JEST_WORKER_ID` or `VITEST_POOL_ID`).
- Avoid shared global state in modules, or reset it in `beforeEach`.
- Use random data like unique emails so tests do not collide.

### 288: How do you use the built-in `node:test` runner with Express?

```js
const { test } = require("node:test");
const assert = require("node:assert/strict");
const request = require("supertest");
const app = require("../app");

test("GET /health returns ok", async () => {
  const res = await request(app).get("/health");
  assert.equal(res.status, 200);
  assert.deepEqual(res.body, { status: "ok" });
});
```

Run it with `node --test`. No extra test framework is needed.

### 289: How do you handle CORS errors when the frontend and API run on different ports in development?

Either allow the dev origin with `cors({ origin: 'http://localhost:5173' })`, or use a dev server proxy so the browser thinks it is the same origin. With Vite:

```js
// vite.config.js
export default {
  server: { proxy: { "/api": "http://localhost:3000" } },
};
```

The proxy approach is often closer to production, where the frontend and API may share a domain.

### 290: How do you add security headers if you do not use helmet?

Set them in a middleware:

```js
app.use((req, res, next) => {
  res.set({
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer",
    "X-Frame-Options": "DENY",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
  });
  next();
});
```

`helmet` covers more headers and keeps up with changes, so it is usually easier.

### 291: What does `Strict-Transport-Security` do and when should you be careful with it?

HSTS tells browsers to only use HTTPS for your domain for a period of time. It prevents downgrade attacks. Be careful: once a browser has seen it, it will refuse plain HTTP for that domain until it expires. With `includeSubDomains`, every subdomain must support HTTPS. Start with a short `max-age` and raise it once you are sure.

### 292: How do you handle long-running requests like report generation?

Do not keep the HTTP request open for minutes. Instead:

1. `POST /reports` creates a job and returns `202 Accepted` with a job ID and a `Location` like `/reports/123`.
2. A worker builds the report.
3. The client polls `GET /reports/123` (or gets notified by SSE, WebSocket or webhook).
4. When done, the status endpoint returns a link to download the file.

```js
app.post("/reports", async (req, res) => {
  const job = await reportQueue.add("build", req.body);
  res
    .location(`/reports/${job.id}`)
    .status(202)
    .json({ id: job.id, status: "queued" });
});
```

### 293: How do you return `201 Created` with the new resource and the right headers?

```js
router.post("/", async (req, res) => {
  const product = await productService.create(req.valid.body);
  res.status(201).location(`${req.baseUrl}/${product.id}`).json(product);
});
```

Using `req.baseUrl` keeps the link right even if you mount the router at a different path.

### 294: How do you implement conditional updates with ETags to avoid lost updates?

Return an ETag with the resource, and require clients to send it back in `If-Match` when updating:

```js
router.put("/:id", async (req, res) => {
  const doc = await Doc.findById(req.params.id);
  if (!doc) return res.sendStatus(404);
  const etag = `"${doc.version}"`;
  if (req.get("If-Match") !== etag) return res.sendStatus(412); // Precondition Failed
  const updated = await doc.updateWithVersion(req.body, doc.version);
  res.set("ETag", `"${updated.version}"`).json(updated);
});
```

This is optimistic locking over HTTP: if someone else changed it, the second writer gets 412 instead of overwriting.

### 295: How do you build a batch endpoint?

Accept an array, check its size, and report results per item:

```js
router.post("/batch", async (req, res) => {
  const items = req.body.items;
  if (!Array.isArray(items) || items.length > 100) {
    return res.status(400).json({ error: "Send 1 to 100 items" });
  }
  const results = await Promise.allSettled(items.map((i) => service.create(i)));
  res
    .status(207)
    .json(
      results.map((r) =>
        r.status === "fulfilled"
          ? { ok: true, id: r.value.id }
          : { ok: false, error: r.reason.message },
      ),
    );
});
```

Limit the size, or one request can take down the server. If many items run at once, also limit concurrency.

### 296: How do you add a maintenance mode to an Express app?

A middleware early in the stack can return 503 for most routes:

```js
app.use((req, res, next) => {
  if (process.env.MAINTENANCE === "true" && req.path !== "/health") {
    return res
      .set("Retry-After", "600")
      .status(503)
      .json({ error: "Down for maintenance" });
  }
  next();
});
```

Reading a flag from Redis or a feature flag service lets you switch it on without restarting.

### 297: How do you use feature flags in Express routes?

Check the flag in middleware or the handler, and keep the check in one place:

```js
const flag = (name) => async (req, res, next) => {
  if (await flags.isEnabled(name, { userId: req.user?.id })) return next();
  res.sendStatus(404);
};

router.get("/new-dashboard", flag("new-dashboard"), newDashboard);
```

Tools like Unleash, LaunchDarkly or a simple database table can store flags. Remove old flags once a feature is fully released.

### 298: How do you avoid blocking the event loop in a route?

Do not run heavy CPU work (big JSON parsing, image resizing, sync crypto, large loops) in a handler. Options:

- Use async APIs (`fs.promises`, async `crypto` functions).
- Move CPU work to `worker_threads` (for example with `piscina`).
- Move it to a background job.
- Use streaming for large data.

While one request blocks the loop, every other request on that process waits.

### 299: How do you check event loop delay in an Express app?

Use `perf_hooks.monitorEventLoopDelay`:

```js
const { monitorEventLoopDelay } = require("node:perf_hooks");

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

app.get("/debug/loop", (req, res) => {
  res.json({
    p50: h.percentile(50) / 1e6,
    p99: h.percentile(99) / 1e6,
    maxMs: h.max / 1e6,
  });
});
```

Values are in nanoseconds, so divide by 1e6 for milliseconds. A high p99 means something is blocking. `prom-client` default metrics also report event loop lag.

### 300: How do you document and enforce a consistent API style in an Express codebase?

- Write down conventions: URL style, status codes, error format, pagination, dates in ISO 8601.
- Put shared pieces in code: a common error handler, a validation helper, response mappers.
- Keep an OpenAPI spec and lint it with a tool like Spectral.
- Add contract or integration tests for each endpoint.
- Review new endpoints against the conventions in code review.

## Advanced Questions (301-450)

### 301: How does the Express router work inside?

A router keeps a stack of "layers". Each `app.use()` or `app.get()` call adds a layer with a path matcher and a handler. For a route, the handler is a `Route` object, which has its own stack of method-specific handlers. When a request comes in, the router walks the stack from the top, checks if the layer's path matches, and for routes also checks the method. It calls the first matching layer and gives it a `next` function that continues the walk from the next position. Since Express 5, this logic lives in the separate `router` package (from the `pillarjs` project).

### 302: How does Express know that a middleware is an error handler?

It looks at `fn.length`, the number of declared parameters. If it is 4, the layer is treated as an error handler and only runs when there is an error. This has some sharp edges:

```js
// NOT an error handler: default param makes length 3
app.use((err, req, res, next = () => {}) => {
  /* ... */
});

// NOT an error handler: rest params have length 0
app.use((...args) => {
  /* ... */
});
```

Wrapping an error handler in another function (for logging or tracing) can also change `length`. Always write error handlers with exactly four plain parameters.

### 303: What happens inside Express when no route matches?

When the router reaches the end of its stack without anyone sending a response, it calls the final callback, which comes from the `finalhandler` package. If there was an error, it uses `err.status` or `err.statusCode` (or 500). If there was no error, it sends 404 with `Cannot GET /path`. It also handles cases like the headers already being sent by closing the socket.

### 304: How does Express add its methods to `req` and `res`?

Express has its own `request` and `response` prototypes that inherit from Node's `http.IncomingMessage.prototype` and `http.ServerResponse.prototype`. At the start of each request, an internal init step changes the prototype of the real `req` and `res` objects with `Object.setPrototypeOf`, so they get methods like `res.json()` and getters like `req.ip`. Each app has its own copies (`app.request`, `app.response`), so you can add methods to one app without affecting others:

```js
app.response.success = function (data) {
  return this.json({ ok: true, data });
};
```

### 305: How does `path-to-regexp` v8 change routing in Express 5?

Express 5 uses `path-to-regexp` v8, which removed most regex features from string paths:

- Named wildcards only: `/*splat`, and the value is an array of segments.
- Optional parts use braces: `/users{/:id}`, `/file{.:ext}`.
- No inline regex like `/:id(\\d+)` and no `?`, `+`, `*` modifiers on params.
- Characters like `(`, `)`, `[`, `]`, `?`, `+`, `!` are reserved and must be escaped with `\\` to match literally.

This was done to make route matching safe from ReDoS and easier to understand. If you need regex, pass a real `RegExp` object as the path.

### 306: What was the path-to-regexp ReDoS issue, and why does it matter for Express?

In 2024, a ReDoS bug (CVE-2024-45296) was found in older `path-to-regexp` versions. Some route patterns with two params in one segment, like `/:a-:b`, produced regexes with catastrophic backtracking. A crafted URL could make matching take a very long time and block the event loop. Express 4 got patched versions. Express 5 uses v8, which has a much simpler syntax that does not generate these regexes. Keep Express up to date, and be careful with custom `RegExp` routes, since those are yours to make safe.

### 307: What is prototype pollution, and how can it affect an Express app?

Prototype pollution is when an attacker sets keys like `__proto__` or `constructor.prototype` in an object, changing `Object.prototype` for the whole process. In Express apps it usually comes from deep merging user input into objects:

```js
// dangerous
deepMerge(config, req.body); // body: {"__proto__": {"isAdmin": true}}
```

After this, `({}).isAdmin` may be `true` everywhere. Protect against it by validating input with strict schemas, not merging user objects into important objects, using `Object.create(null)` or `Map` for user-keyed data, and keeping libraries like `qs` and lodash up to date. `JSON.parse` itself creates an own `__proto__` property and does not pollute; the danger is in what you do with the result.

### 308: How can `res.redirect()` lead to an open redirect, and how do you prevent it?

If you redirect to a URL from user input, attackers can make links on your domain that send users to a phishing site:

```js
// bad
app.get("/login", (req, res) => res.redirect(req.query.next));
// /login?next=https://evil.example
```

Only allow relative paths on your site, or check against an allow list:

```js
function safeNext(next) {
  if (typeof next !== "string") return "/";
  if (!next.startsWith("/") || next.startsWith("//") || next.startsWith("/\\"))
    return "/";
  return next;
}
res.redirect(safeNext(req.query.next));
```

Express encodes the URL with `encodeurl` but does not check where it points.

### 309: How do you prevent SSRF in an Express endpoint that fetches URLs?

If users can make your server fetch any URL, they can reach internal services, like the cloud metadata endpoint at `169.254.169.254`. To protect against it:

- Allow only known hosts if you can.
- Resolve the host name and block private, loopback and link-local IP ranges, and check again after redirects (or turn redirects off).
- Allow only `https:`.
- Run the fetcher with network rules that block internal ranges.

Checking the URL string alone is not enough, because DNS can point a harmless-looking name at an internal IP.

### 310: How do slowloris attacks affect Node and Express, and how do you defend against them?

A slowloris attack opens many connections and sends headers very slowly, keeping sockets busy. Node has defenses with `server.headersTimeout` (default 60 s) and `server.requestTimeout` (default 300 s). You can lower them for an API:

```js
server.headersTimeout = 20_000;
server.requestTimeout = 30_000;
```

In production a reverse proxy or load balancer usually buffers requests and drops slow clients before they reach Node, which is the best defense.

### 311: What is HTTP request smuggling, and does it affect Express apps?

Request smuggling happens when a proxy and the backend disagree on where one request ends, often because of `Content-Length` and `Transfer-Encoding` headers that conflict. An attacker can then hide a second request inside the first. Node's HTTP parser (`llhttp`) is strict and rejects most bad inputs, and these issues get fixed in Node security releases. Keep Node up to date, do not turn on `insecureHTTPParser`, and make sure your proxy normalizes requests.

### 312: How can large or deeply nested JSON bodies hurt an Express app, and how do you protect it?

`JSON.parse` is synchronous, so a large body blocks the event loop while it parses. Deep nesting can also make your own recursive code (validation, sanitizers) slow or crash with a stack overflow. Protections:

- Keep `limit` small (the 100kb default is fine for most APIs) and raise it only on routes that need it.
- Use strict schemas that reject unknown or deep structures.
- For big uploads, use streaming parsers or direct uploads to storage.

`express.urlencoded` in Express 5 also has a `depth` option (default 32) for nested keys when `extended` is true.

### 313: How do you prevent header injection (response splitting) in Express?

Response splitting used to be possible when user input with `\r\n` went into headers. Node now throws `ERR_INVALID_CHAR` if a header value has CR or LF, so `res.set()` cannot be used for this. You should still validate values you put in headers, such as file names in `Content-Disposition`. `res.attachment()` and `res.download()` encode the name for you through the `content-disposition` package.

### 314: How do you use a per-request CSP nonce with helmet?

Generate a random nonce per request, put it in `res.locals`, and use it in the CSP and in your templates:

```js
const crypto = require("node:crypto");

app.use((req, res, next) => {
  res.locals.cspNonce = crypto.randomBytes(16).toString("base64");
  next();
});

app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        scriptSrc: ["'self'", (req, res) => `'nonce-${res.locals.cspNonce}'`],
      },
    },
  }),
);
```

```html
<script nonce="<%= cspNonce %>">
  /* inline code */
</script>
```

Only scripts with the right nonce run, so injected inline scripts are blocked.

### 315: What are common JWT mistakes in Express apps?

- Not setting `algorithms` in `jwt.verify`, which can allow algorithm confusion in some setups.
- Using a short or guessable secret for HS256.
- Long-lived access tokens with no way to revoke them.
- Putting sensitive data in the payload (it is only base64, not encrypted).
- Not checking `aud` and `iss` when tokens come from an identity provider.
- Using `jwt.decode` instead of `jwt.verify`, which skips the signature check.
- Accepting the token from many places (query string, body) where it can leak into logs.

### 316: How do you verify JWTs from an external identity provider in Express?

Fetch the provider's public keys from its JWKS endpoint and verify the signature and claims. The `jose` library does this well:

```js
const { createRemoteJWKSet, jwtVerify } = require("jose");

const JWKS = createRemoteJWKSet(
  new URL("https://auth.example.com/.well-known/jwks.json"),
);

async function authenticate(req, res, next) {
  const token = req.get("Authorization")?.replace(/^Bearer /, "");
  if (!token) return res.sendStatus(401);
  try {
    const { payload } = await jwtVerify(token, JWKS, {
      issuer: "https://auth.example.com/",
      audience: "my-api",
    });
    req.user = payload;
    next();
  } catch {
    res.sendStatus(401);
  }
}
```

`createRemoteJWKSet` caches keys and refetches when it sees a new key ID, so key rotation works.

### 317: Why is Express slower than Fastify in benchmarks, and does it matter?

Express does more work per request: it changes object prototypes, walks a middleware stack one layer at a time, and uses plain `JSON.stringify`. Fastify uses a radix tree router, compiles JSON serializers from schemas and has a lighter request lifecycle. In "hello world" benchmarks Fastify can be a few times faster. In real apps, most time usually goes to database calls, network and your own code, so the framework overhead is often a small part. It matters more for very high traffic, low-latency services.

### 318: How does the number of middleware and routes affect Express performance?

The router checks layers in order, so every request pays for each `app.use()` before it, and route matching is linear. With hundreds of routes in one router, matching becomes noticeable. Tips:

- Mount routers under prefixes (`/api/users`) so whole groups are skipped quickly.
- Put rarely needed middleware on the routes that need it, not globally.
- Put hot routes and static files early.
- Avoid expensive global middleware, like sessions for public static files.

### 319: How do you make JSON responses faster in Express?

- Send less data: pick only the fields you need, paginate, and avoid deep objects.
- Use `.lean()` (Mongoose) or plain objects instead of heavy model instances.
- For hot endpoints with a known shape, use a compiled serializer like `fast-json-stringify` and send the string with `res.type('json').send(str)`.
- Cache serialized responses when data does not change often.
- Let a proxy or CDN compress and cache.

Avoid `json spaces` in production, since it makes responses bigger.

### 320: What does the ETag cost, and when should you turn it off?

For `res.send()` bodies, Express computes the ETag by hashing the whole body for each response. For large responses this costs CPU, and it only helps if clients send `If-None-Match`. If your API responses are rarely cached by clients, or you set caching headers at a CDN, you can turn it off with `app.set('etag', false)`. Static files from `express.static` use a cheap ETag based on file size and modification time.

### 321: How do you find a memory leak in an Express app?

1. Watch memory over time (RSS and heap used) in your metrics. A leak keeps growing and never drops after GC.
2. Reproduce with a load test.
3. Take heap snapshots at different times with `node --inspect` and Chrome DevTools, or with `v8.writeHeapSnapshot()`, and compare them.
4. Look for objects that keep growing, and follow their retainers.

Common causes in Express apps: module-level caches or `Map`s that never shrink, event listeners added per request and never removed, closures holding big objects, timers not cleared, and the default `express-session` MemoryStore.

### 322: Why is the default `express-session` MemoryStore not for production?

It keeps all sessions in the process memory, never removes expired ones properly, and grows without limit, which leads to memory leaks. It also does not work with more than one process, because each one has its own sessions. `express-session` itself prints a warning about this when `NODE_ENV` is `production`. Use Redis, a database or another real store.

### 323: How do you scale an Express app horizontally?

Make each instance stateless: keep sessions, caches, rate limits, uploaded files and job queues in shared services (Redis, a database, S3). Then you can run many instances behind a load balancer and add or remove them freely. Things to watch: database connection limits (pool size × number of instances), sticky sessions for Socket.IO's long polling, and making background jobs run once (use a queue, not a timer in every instance).

### 324: How do you calculate the right database pool size when scaling Express?

Total connections = pool size per process × processes per container × number of containers. This must stay under the database's `max_connections`, leaving room for admin tools and migrations. Bigger is not always better: a database usually performs best with a limited number of active connections. If you need many app instances, use a connection pooler like PgBouncer (or RDS Proxy) between the app and the database.

### 325: How do you do zero-downtime deploys with Express?

- Run at least two instances behind a load balancer.
- Deploy new instances, wait for their readiness checks to pass, then remove old ones (rolling or blue-green).
- On `SIGTERM`, the old instance fails readiness, stops taking new connections, finishes current requests, closes pools and exits.
- Make database migrations backward compatible, so old and new code can run at the same time (expand, then contract).

### 326: Does Express support HTTP/2?

Not directly. Express is built around the `http` module's request and response objects, and the `http2` module has a different API. The `http2` compatibility API mostly works with simple Express apps, but there are known gaps, so it is not officially supported. The usual setup is to let a reverse proxy, load balancer or CDN speak HTTP/2 or HTTP/3 with clients and talk HTTP/1.1 to Express. If you really need HTTP/2 inside Node, Fastify has built-in support.

### 327: Why is HTTP/1.1 keep-alive between the load balancer and Express important?

Without keep-alive, each request opens a new TCP connection, which adds latency and CPU. With keep-alive, the balancer reuses connections. The catch: if Node closes an idle connection at the same moment the balancer sends a request on it, the balancer gets a reset and returns 502. That is why `server.keepAliveTimeout` should be longer than the balancer's idle timeout, and `headersTimeout` a bit longer than `keepAliveTimeout`.

### 328: How does Express 5 handle a handler that returns a rejected promise after it already sent a response?

The router still calls `next(err)`. Your error handler runs, but `res.headersSent` is `true`. If you try to send another response, you get "Cannot set headers after they are sent". A good final error handler checks for this and calls `next(err)` (or just logs) so Express's final handler can close the connection. This usually points to a bug, like doing work after `res.json()` that is not awaited properly.

### 329: How would you design a modular Express monolith?

Split the code by business area (users, billing, catalog), not by technical layer only. Each module has its own router, services, data access and tests, and exposes a small public API to other modules. The main `app.js` only mounts module routers and shared middleware:

```js
app.use("/users", usersModule.router);
app.use("/billing", billingModule.router);
```

Rules like "modules do not import each other's internals" can be checked with lint rules (for example `eslint-plugin-boundaries`). This keeps the option to split a module into a service later.

### 330: How do you apply hexagonal (ports and adapters) architecture to an Express app?

Treat Express as one adapter at the edge. The core has use cases and domain logic with no Express or database imports. Ports are interfaces the core needs (like `UserRepository`, `EmailSender`). Adapters implement them (Postgres repository, SMTP sender). Express handlers only turn HTTP into use case calls and results back into HTTP:

```js
router.post("/", async (req, res) => {
  const result = await registerUser(deps)(req.valid.body);
  res.status(201).json(result);
});
```

Then the core is easy to test and can be reused from CLI tools or queue consumers.

### 331: When would you pick NestJS over plain Express?

When the team is large, the app will be big, and you want a fixed structure: modules, dependency injection, decorators for validation and docs, and many built-in features like guards and interceptors. Plain Express is better when the service is small, the team prefers less magic, or you need full control. NestJS uses Express by default under the hood, so Express middleware still works there.

### 332: How do you add multi-tenancy to an Express API?

Find the tenant early in a middleware (from subdomain, header, or token claim), load its config and put it in the request context:

```js
app.use(async (req, res, next) => {
  const slug = req.subdomains.at(-1);
  const tenant = slug && (await tenants.findBySlug(slug));
  if (!tenant) return res.sendStatus(404);
  req.tenant = tenant;
  next();
});
```

Then every query must filter by tenant. You can enforce this in the data layer (scoped repositories, Postgres row-level security, or one schema or database per tenant). Never trust a tenant ID from the request body.

### 333: What is the risk of trusting `X-Forwarded-For` blindly?

The client can send its own `X-Forwarded-For` header. If `trust proxy` is `true`, Express picks the leftmost address, which the client controls. Then rate limits can be bypassed by changing the header, and IP allow lists can be fooled. Set `trust proxy` to the exact number of proxies or their IP ranges, so Express takes the address added by your own proxy.

### 334: How do you run Express behind several proxies (CDN, then load balancer)?

Each proxy adds the address it sees to `X-Forwarded-For`. Set `trust proxy` to the number of hops you control, or list their subnets:

```js
app.set("trust proxy", 2); // CDN + load balancer
// or
app.set("trust proxy", ["loopback", "10.0.0.0/8", "130.176.0.0/16"]);
```

Then check by logging `req.ip` and `req.ips` for a known client. Some CDNs also send their own header with the client IP (like `CF-Connecting-IP`), which you can read when the request is known to come from the CDN.

### 335: How do you prevent the same request being processed twice when a client retries after a timeout?

Use idempotency keys for unsafe operations, plus a database constraint as a backup:

- Client sends `Idempotency-Key`.
- Server inserts a row with that key and status `processing` inside a unique index. A second request with the same key either waits, gets `409`, or gets the saved result.
- After processing, save the response with the key.

A unique constraint (like one order per cart) protects you even if the key logic has a bug.

### 336: A route is sometimes very slow under load but fast alone. How do you investigate?

Check, in order:

- Event loop delay: if it is high, something is blocking the loop.
- Pool wait time: requests may be waiting for a free database connection.
- Downstream latency: slow external APIs without timeouts.
- GC pauses: big allocations, like loading huge results into memory.
- Locks in the database (long transactions, row locks).

Tracing (OpenTelemetry) shows where time goes per request. A CPU profile (`--cpu-prof` or Clinic.js flame) under load shows hot functions.

### 337: Users get random 502 errors from the load balancer, but the app logs show no errors. What could cause it?

Common causes:

- `keepAliveTimeout` in Node is shorter than the balancer's idle timeout, so Node closes connections the balancer still uses.
- The process restarted (crash, out-of-memory kill, deploy) while requests were in flight.
- The app took longer than the balancer's response timeout.
- Response headers too large for the proxy.

Check container restarts and OOM kills, compare timeout settings, and look at the balancer's logs, which often say exactly why it gave 502.

### 338: Requests sometimes hang forever. What would you look for?

- A middleware or handler path that neither sends a response nor calls `next()`, often in an `if` branch.
- An error thrown in a callback or timer that Express does not catch.
- A promise that never settles (waiting for a callback that never fires).
- A database query waiting for a pool connection that is never released (missing `client.release()`).
- An outgoing request with no timeout.

Add a request timeout log (log any request still open after N seconds with its route) to find the path quickly.

### 339: You see "Cannot set headers after they are sent to the client". How do you fix it?

Something tries to send a second response. Typical causes:

- Missing `return` after `res.json()` in an `if`.
- Calling `next()` after sending a response, so another handler also responds.
- Sending in a callback and also after it.
- An error after a response was sent, reaching the error handler, which tries to send again.

The stack trace shows where the second send happens. Check `res.headersSent` in the error handler, and use `return res...` as a habit.

### 340: CPU sits at 100% on one Express instance. How do you find the cause?

Take a CPU profile while it is happening. Options: `node --cpu-prof`, connecting DevTools with `--inspect`, sending `SIGUSR1` to enable the inspector on a running process, or using tools like Clinic.js or your APM. Look for:

- Regex backtracking (custom route regexes, validation regexes).
- Big `JSON.parse` or `JSON.stringify` calls.
- Sync crypto or compression.
- A loop over a large array per request.
- Heavy logging with pretty printing in production.

### 341: How does Express 5 encode URLs in `res.redirect()` and `res.location()`?

Both pass the URL through `encodeurl`, which encodes characters that are not allowed in URLs (like spaces) but leaves already encoded sequences (`%20`) alone. It does not validate the target. In Express 5, `res.location('back')` and `res.redirect('back')` no longer have special meaning, so use the `Referrer` header yourself if you need that. Since you control the value, always validate user-supplied redirect targets.

### 342: How do you make Express routes work with custom `RegExp` safely?

Keep regexes simple and anchored, avoid nested quantifiers like `(a+)+`, and test them with tools like `safe-regex` or `recheck`. Remember that a regex route runs on every request that reaches it, with input the attacker controls. Often it is safer to match a simple param (`/:id`) and validate it in code or with a schema.

### 343: How do you handle requests where the client sends `Expect: 100-continue`?

Node's HTTP server automatically answers `100 Continue` unless you listen for the `checkContinue` event. If you want to reject large uploads early (before the client sends the body), handle it yourself:

```js
const server = http.createServer(app);
server.on("checkContinue", (req, res) => {
  if (Number(req.headers["content-length"]) > 10 * 1024 * 1024) {
    res.writeHead(413).end();
    return;
  }
  res.writeContinue();
  app(req, res);
});
```

This is rare, but useful for big file upload APIs.

### 344: How do you implement range requests for video streaming?

`res.sendFile()` and `express.static` already support `Range` headers and return `206 Partial Content`. If the file lives in S3, pass the `Range` header to S3 and stream the result back:

```js
app.get("/videos/:id", async (req, res) => {
  const out = await s3.send(
    new GetObjectCommand({
      Bucket: BUCKET,
      Key: `videos/${req.params.id}.mp4`,
      Range: req.get("Range"),
    }),
  );
  res.status(req.get("Range") ? 206 : 200).set({
    "Content-Type": "video/mp4",
    "Accept-Ranges": "bytes",
    "Content-Length": out.ContentLength,
    ...(out.ContentRange && { "Content-Range": out.ContentRange }),
  });
  out.Body.pipe(res);
});
```

Often it is better to give the client a signed URL and let it stream from S3 or a CDN directly.

### 345: How do you handle backpressure when writing large responses manually?

`res.write()` returns `false` when the internal buffer is full. You should wait for `'drain'` before writing more:

```js
const { once } = require("node:events");

for await (const chunk of source) {
  if (!res.write(chunk)) await once(res, "drain");
}
res.end();
```

Or use `stream.pipeline`, which handles backpressure and errors for you. Ignoring backpressure with a slow client can fill memory.

### 346: What happens to a streaming response if the source stream fails halfway?

The status and headers were already sent, so you cannot send a 500. The best you can do is end the connection so the client sees an incomplete response, and log the error. `pipeline` destroys `res` on error, which closes the socket. With chunked encoding, the client sees the stream end without the final chunk and knows it failed. For important downloads, add a checksum or length so clients can verify.

### 347: How would you build rate limiting that is fair across many instances?

Use a shared store with atomic operations, usually Redis. A fixed window counter (`INCR` plus `EXPIRE`) is simple. A sliding window (sorted sets or two windows combined) or token bucket (a Lua script) is smoother. `express-rate-limit` with `rate-limit-redis` gives you this. Key by user ID or API key when known, not only IP, because many users can share one IP behind NAT. Also limit at the edge (CDN or gateway) to stop big floods before they reach Node.

### 348: What is the difference between rate limiting and load shedding?

Rate limiting controls how much one client can do, to be fair and stop abuse. Load shedding protects the whole server when it is overloaded, by rejecting some requests early (with 503) no matter who sends them. You often need both: a rate limit per key, and load shedding based on event loop delay, queue length or in-flight requests.

### 349: How do you return useful `Retry-After` and rate limit headers?

When you return 429 or 503, tell the client when to try again:

```js
res
  .set("Retry-After", String(secondsUntilReset))
  .status(429)
  .json({ error: "Too many requests" });
```

`express-rate-limit` can also send the standard `RateLimit` and `RateLimit-Policy` headers (`standardHeaders: 'draft-8'`), so clients can slow down before hitting the limit.

### 350: How do you design an Express API that sends events to other services reliably?

Do not publish to the message broker right after saving to the database inside the request, because one of them can fail and leave things out of sync. Use the transactional outbox pattern: save the business change and an "outbox" row in the same database transaction. A separate worker reads the outbox and publishes to Kafka, RabbitMQ or SNS, and marks rows as sent. Consumers must handle duplicates, since a message may be published more than once.

### 351: How does Express 5 decide whether a handler returned a promise?

After calling a handler, the router checks if the return value is "thenable" (an object with a `then` function). If it is, it attaches a rejection handler that calls `next(err)`. If the promise resolves, nothing else happens; the router does not call `next()` for you. So an `async` middleware still has to call `next()` itself when it is done:

```js
app.use(async (req, res, next) => {
  req.user = await loadUser(req);
  next(); // still required
});
```

### 352: What happens if an async middleware calls `next()` and then throws?

The router has already moved on to the next handler when `next()` was called. If the same function then throws (or its promise rejects), Express calls `next(err)` again for that request. Now two paths are running at once, and you can get a double response or confusing errors. Make sure an async middleware either calls `next()` as its last step or catches errors that happen after it.

### 353: How is `req.query` computed in Express 5?

`req.query` is a getter on the request prototype. Each time you read it, Express takes the query string from the URL and runs the configured `query parser` function on it. The default in Express 5 is `'simple'`, which uses `node:querystring`. Because it is a getter, writing to it does not work, and reading it many times in a hot loop does repeated work, so keep a local copy if you read it often.

### 354: Why did Express 5 change the default query parser from `extended` to `simple`?

The `extended` parser (`qs`) turns strings like `a[b][c]=1` into nested objects and arrays. That is convenient, but it lets clients send objects where you expect strings, which caused NoSQL injection, type confusion and some denial of service bugs. The `simple` parser only creates strings and arrays of strings, so code is safer by default. You can switch back with `app.set('query parser', 'extended')` if you need nested queries, and then validate them strictly.

### 355: How do you plug in a custom query string parser?

Set the `query parser` setting to a function that takes the raw string and returns an object:

```js
const qs = require("qs");

app.set("query parser", (str) =>
  qs.parse(str, {
    depth: 2,
    arrayLimit: 20,
    parameterLimit: 100,
    allowPrototypes: false,
  }),
);
```

This lets you keep nested queries but with tight limits.

### 356: How does `express.static` (serve-static) work internally?

It uses the `send` package. For each request it builds a file path from the URL under the root, rejects paths with `..` that leave the root, and checks `dotfiles` rules. It runs `fs.stat` to find the file. If it is a directory, it tries `index.html` or redirects to add a trailing slash. Then it sets `Content-Type`, `ETag`, `Last-Modified` and `Cache-Control`, handles conditional requests (304) and range requests (206), and streams the file with `fs.createReadStream`. If nothing is found, it calls `next()`.

### 357: Why is `express.static` slower than Nginx or a CDN for static files?

Each file request goes through the JavaScript middleware stack, does a `stat` call and streams the file through Node streams. Nginx uses `sendfile` and kernel-level optimizations, and a CDN serves from caches close to the user. For small apps `express.static` is fine. For heavy traffic, put static files on a CDN or let a reverse proxy serve them, and keep Node for dynamic requests.

### 358: How do you serve pre-compressed static files (`.br`, `.gz`) from Express?

`express.static` does not do this. Options:

- Use `express-static-gzip`, which checks `Accept-Encoding` and serves `app.js.br` or `app.js.gz` if they exist.
- Let Nginx (`gzip_static`, `brotli_static`) or your CDN do it.

Pre-compressing at build time with the highest level gives smaller files without spending CPU at request time.

### 359: What is the cost of `app.use(compression())` in Node, and when should you not use it?

The zlib work runs on the libuv thread pool, but it still uses CPU for every compressible response, and the stream handling adds work on the main thread too. Under high traffic this cuts how many requests one process can handle. Skip it when a proxy or CDN already compresses (doing it twice wastes CPU), for responses that are already compressed (images, video, zip), and for SSE or streaming responses unless you flush correctly.

### 360: What are the risks of Brotli or gzip on responses that contain secrets?

Compressing responses that mix secrets (like CSRF tokens) with data the attacker controls can leak the secret through the compressed size (BREACH attack). The attacker needs to make many requests and see sizes, which is hard but possible. Mitigations: do not reflect user input in pages with secrets, mask CSRF tokens per request (random XOR), or turn off compression for those responses.

### 361: How do you protect an Express app from a "zip bomb" request body?

A small compressed body can expand into gigabytes. The body parsers apply `limit` to the decompressed size and stop reading when it is reached, so keep `limit` low. If you handle compressed uploads yourself (like `zlib.createGunzip()` on a stream), count bytes as you read and abort when it gets too large. You can also refuse compressed request bodies with `inflate: false`.

### 362: How would you implement a request-scoped database transaction across several services?

Start the transaction in the handler (or a middleware), and pass the transaction client down, or put it in `AsyncLocalStorage` so repositories pick it up automatically:

```js
const als = new AsyncLocalStorage();

async function withTransaction(fn) {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    const result = await als.run({ client }, fn);
    await client.query("COMMIT");
    return result;
  } catch (err) {
    await client.query("ROLLBACK");
    throw err;
  } finally {
    client.release();
  }
}

const db = () => als.getStore()?.client ?? pool;
```

Avoid starting a transaction for every request in global middleware, because it holds connections longer than needed.

### 363: What are the downsides of using global middleware to open a transaction per request?

Every request, even reads and health checks, takes a connection for the whole request, including time spent calling other APIs or waiting on slow clients. Under load the pool runs out and requests queue up. Long transactions also hold locks longer. Open transactions only around the work that needs them, and keep them short.

### 364: How do you design error handling for an Express API used by many teams?

- One error format for all endpoints (for example RFC 9457 problem details).
- Stable machine-readable error codes (`USER_NOT_FOUND`), not only messages.
- Clear mapping of error types to status codes in one error handler.
- No internal details (stack traces, SQL) in responses; log them with a request ID instead, and return that ID to the client.
- Document the error codes in the OpenAPI spec.
- Tests that check the error format for each endpoint.

### 365: How do you make error responses include the request ID for support?

Add it to every error response and to the logs:

```js
app.use((err, req, res, next) => {
  const status = err.status ?? 500;
  req.log.error({ err, requestId: req.id }, "request failed");
  if (res.headersSent) return next(err);
  res.status(status).json({
    type: "about:blank",
    title: status === 500 ? "Internal Server Error" : err.message,
    status,
    requestId: req.id,
  });
});
```

When a user reports a problem, the ID lets you find the exact log lines.

### 366: How do you safely log errors that may contain circular references or huge objects?

`JSON.stringify` throws on circular objects, and logging a full Axios or database error can dump huge objects with config and secrets. Use a logger with error serializers (pino has `err` serializers that pick `message`, `stack` and `type`), and redact sensitive fields. Avoid `console.log(req)` in production, because `req` has circular references and a lot of data.

### 367: What is the event loop impact of synchronous logging in Express?

`console.log` to a file or a pipe can be synchronous in Node, which blocks the event loop while writing. With heavy logging this adds latency to every request. Pino writes asynchronously with a buffered destination (`pino.destination({ sync: false })`) or sends logs to a worker thread with transports. Keep log volume reasonable in production and avoid pretty printing there.

### 368: How do you implement graceful shutdown when there are open WebSocket or SSE connections?

`server.close()` waits for every connection to end, and long-lived connections may never end on their own. On shutdown:

1. Stop accepting new connections (`server.close()`).
2. Tell SSE clients to reconnect elsewhere (send an event, then `res.end()`), and close WebSockets with a close code like 1001 ("going away").
3. Call `server.closeIdleConnections()` and, after a grace period, `server.closeAllConnections()`.
4. Close pools and exit.

Clients should have reconnect logic, so they connect to another instance.

### 369: How do you keep Socket.IO working with several Express instances?

Two things are needed:

- Sticky sessions at the load balancer if clients use HTTP long polling, because one session's requests must reach the same instance. Using only the WebSocket transport avoids this.
- An adapter so events reach clients on other instances, like `@socket.io/redis-adapter` or `@socket.io/redis-streams-adapter`.

```js
const { createAdapter } = require("@socket.io/redis-adapter");
io.adapter(createAdapter(pubClient, subClient));
```

### 370: How do you secure a WebSocket upgrade in an Express app?

The upgrade request is a normal HTTP request, so check it before accepting:

- Check the `Origin` header against an allow list (browsers do not apply CORS to WebSockets).
- Authenticate using the session cookie or a short-lived token.
- Limit message size and rate.

```js
server.on("upgrade", (req, socket, head) => {
  if (!allowedOrigins.has(req.headers.origin)) return socket.destroy();
  sessionParser(req, {}, () => {
    if (!req.session?.userId) return socket.destroy();
    wss.handleUpgrade(req, socket, head, (ws) =>
      wss.emit("connection", ws, req),
    );
  });
});
```

Use `new WebSocketServer({ noServer: true })` for this manual upgrade.

### 371: How would you build a gateway in Express in front of several microservices?

Use Express for auth, rate limits, request IDs and routing, and proxy the rest:

```js
app.use(requestId, authenticate, rateLimiter);
app.use(
  "/orders",
  createProxyMiddleware({ target: ORDERS_URL, changeOrigin: true }),
);
app.use(
  "/users",
  createProxyMiddleware({ target: USERS_URL, changeOrigin: true }),
);
```

Pass identity to the services in headers they trust only from the gateway (and strip those headers from incoming requests). For higher traffic or more features (retries, circuit breaking, metrics), a dedicated gateway like Envoy, Kong or a cloud API gateway is often a better fit.

### 372: How do you add a circuit breaker around calls to another service in an Express route?

Use a library like `opossum`:

```js
const CircuitBreaker = require("opossum");

const breaker = new CircuitBreaker(
  (id) =>
    fetch(`${INVENTORY_URL}/items/${id}`, {
      signal: AbortSignal.timeout(2000),
    }).then((r) => {
      if (!r.ok) throw new Error(`status ${r.status}`);
      return r.json();
    }),
  { errorThresholdPercentage: 50, resetTimeout: 10_000 },
);
breaker.fallback(() => ({ stock: null }));

app.get("/items/:id/stock", async (req, res) => {
  res.json(await breaker.fire(req.params.id));
});
```

When the other service keeps failing, the breaker "opens" and fails fast with the fallback, so your app does not pile up waiting requests.

### 373: How do you add retries to outgoing calls without making things worse?

- Retry only safe or idempotent requests, or ones with an idempotency key.
- Retry only on errors that may pass (timeouts, 502, 503, 429), not on 400 or 404.
- Use exponential backoff with jitter.
- Limit attempts and total time, and respect `Retry-After`.
- Make sure the total retry time fits within your own request timeout.

Retries at many layers (client, gateway, service) multiply, which can turn a small problem into an outage.

### 374: How do you design an Express service to handle a sudden traffic spike?

- Keep instances stateless so autoscaling can add more quickly.
- Cache hot reads (CDN, Redis) and use HTTP caching headers.
- Set timeouts everywhere and use load shedding (return 503 early when overloaded).
- Protect the database with pool limits, read replicas, and queues for writes that can wait.
- Rate limit per client at the edge.
- Load test before big events to know the limits.

### 375: How do you load test an Express API?

Use a tool like `k6`, `autocannon` or `artillery`. Test real scenarios (login, browse, checkout), not only one endpoint. Watch p95/p99 latency, error rate, event loop delay, CPU, memory, and database metrics. Increase load step by step to find the point where latency jumps. `autocannon` is quick for local checks:

```bash
npx autocannon -c 100 -d 30 http://localhost:3000/products
```

Run tests against an environment that looks like production; a laptop gives very different numbers.

### 376: What is the "thundering herd" problem with caching, and how do you avoid it in Express?

When a popular cache key expires, many requests miss at the same time and all hit the database. Fixes:

- Request coalescing: only one request rebuilds the value, others wait for the same promise.
- Add random jitter to TTLs.
- Refresh in the background before the key expires ("stale while revalidate").

```js
const inflight = new Map();

async function getCached(key, load) {
  const hit = await redis.get(key);
  if (hit) return JSON.parse(hit);
  if (!inflight.has(key)) {
    inflight.set(
      key,
      load()
        .then(async (v) => {
          await redis.set(key, JSON.stringify(v), {
            EX: 60 + Math.floor(Math.random() * 10),
          });
          return v;
        })
        .finally(() => inflight.delete(key)),
    );
  }
  return inflight.get(key);
}
```

This coalesces within one process. Across instances, use a short Redis lock.

### 377: How do you handle cache invalidation when data changes?

Pick a strategy per type of data:

- Delete keys after writes ("cache aside"). Simple, but you must find every key that depends on the data.
- Short TTLs for data that can be a bit old.
- Versioned keys (`product:42:v7`), where a write bumps the version.
- Events: publish a "product changed" event and let caches subscribe.

Delete the cache after the database commit, not before, or a parallel read can put old data back.

### 378: How would you migrate a large Express 4 codebase to Express 5 safely?

1. Upgrade Node first, and update all Express-related packages to versions that support v5 (`@types/express` v5, `cors`, `helmet`, sanitizers, Passport).
2. Run the codemods, then search for route patterns with `*`, `?`, `(`, regex groups and fix them.
3. Search for removed APIs (`req.param`, `res.send(status)`, `res.json(obj, status)`, `res.sendfile`, `'back'` redirects, `app.del`).
4. Check middleware that writes to `req.query`, and code that assumes `req.body` is `{}`.
5. Run the full test suite, plus tests for 404 behavior and error handling.
6. Deploy to a canary and compare error rates and 404 counts before full rollout.

### 379: Why can async wrappers like `express-async-errors` cause problems after moving to Express 5?

`express-async-errors` patches Express's internal `Layer` to catch promise rejections. In Express 5 the router is a different package with different internals, so the patch may do nothing or break. Since Express 5 does this itself, remove the package. Plain wrapper functions like `asyncHandler(fn)` still work, but they are no longer needed.

### 380: How do you make an Express app ready for containers and Kubernetes?

- Read config from environment variables and validate it at startup.
- Log to stdout in JSON.
- Expose `/health` (liveness) and `/ready` (readiness) endpoints.
- Handle `SIGTERM` with graceful shutdown, and run `node` directly (not through `npm start`, which may not forward signals) or use `--init`/`tini`.
- Run as a non-root user with a small image.
- Set memory limits and match V8's heap with `--max-old-space-size` if needed.
- Keep instances stateless.

### 381: Why should you not use `npm start` as the container command?

`npm` runs your app as a child process. Older npm versions did not forward signals like `SIGTERM` to the child, and even now there is an extra process in between. Kubernetes sends `SIGTERM`, and if the Node process never sees it, it gets killed with `SIGKILL` after the grace period, which drops in-flight requests. Use `CMD ["node", "server.js"]` so Node is the main process and handles signals itself.

### 382: How does Node decide the heap size in a container, and why does it matter for Express?

Recent Node versions look at the container's memory limit (cgroups) when they pick a default heap size, but the defaults may still not fit your app. If the heap can grow past the container limit, the kernel kills the process (OOMKilled) without a JavaScript error. Set `--max-old-space-size` (in MB) below the container limit to leave room for buffers and native memory:

```dockerfile
CMD ["node", "--max-old-space-size=384", "server.js"]
```

Then the app fails with a clear heap error (or runs GC more often) instead of being killed silently.

### 383: How do you safely run database migrations when deploying an Express app?

Run them as a separate step (a Kubernetes Job, a CI step, or an init container), not in every app instance on startup, where several instances may run them at once. Make changes backward compatible: add a column, deploy code that writes both, backfill, then remove old columns in a later release. That way old and new instances can run side by side during a rolling deploy.

### 384: How would you implement API request signing for partners?

Give each partner a secret, and have them sign the method, path, timestamp and body hash with HMAC-SHA256. On the server:

1. Read the raw body.
2. Check the timestamp is within a few minutes, to stop replays.
3. Rebuild the string, compute the HMAC, and compare with `timingSafeEqual`.
4. Optionally store the request ID or nonce for a short time to reject exact replays.

```js
const payload = `${req.method}\n${req.originalUrl}\n${timestamp}\n${sha256(req.rawBody)}`;
const expected = crypto
  .createHmac("sha256", partner.secret)
  .update(payload)
  .digest("hex");
```

This proves who sent the request and that nothing changed on the way.

### 385: How do you implement mutual TLS (mTLS) with Express?

Usually mTLS is handled by a proxy or service mesh. If Node handles it, use the `https` module with `requestCert`:

```js
https
  .createServer(
    {
      key,
      cert,
      ca: [partnerCa],
      requestCert: true,
      rejectUnauthorized: true,
    },
    app,
  )
  .listen(8443);

app.use((req, res, next) => {
  const peer = req.socket.getPeerCertificate();
  req.clientName = peer.subject?.CN;
  next();
});
```

Behind a proxy, the proxy checks the certificate and passes the client identity in a header that only the proxy can set.

### 386: How do you protect admin endpoints beyond normal authentication?

- Put them on a separate router, and if possible a separate host or port reachable only from a VPN or internal network.
- Require strong auth (SSO with MFA) and short sessions.
- Check fine-grained permissions on each action.
- Log every admin action with who, what and when (audit log).
- Rate limit and alert on unusual activity.
- Do not expose them in public API docs.

### 387: How do you build an audit log for an Express API?

Record who did what on which resource, with before and after values for important changes. Write it in the same transaction as the change, or through the outbox pattern, so it cannot be lost. Include the user ID, IP, request ID and time:

```js
await db.tx(async (t) => {
  const before = await t.orders.find(id);
  const after = await t.orders.update(id, changes);
  await t.audit.insert({
    actor: req.user.id,
    action: "order.update",
    entityId: id,
    before,
    after,
    requestId: req.id,
  });
});
```

Make the audit table append-only, and limit who can read it.

### 388: How do you handle personal data (GDPR) in an Express app?

- Collect only what you need.
- Do not log personal data, or redact it.
- Encrypt sensitive fields at rest and always use HTTPS.
- Build endpoints for data export and deletion, and make deletion reach caches, backups policy and third parties.
- Keep track of which services and processors hold user data.
- Set cookie consent where needed (for example `saveUninitialized: false` for sessions until consent).

### 389: How do you avoid leaking stack traces in production?

Set `NODE_ENV=production` so Express's default handler hides them, and make your own error handler return only safe messages for 500 errors. Also check third-party middleware that may send details, and do not send `err.message` from database or library errors to clients, because these can include table names, file paths or queries.

### 390: What is the security risk of `res.send()` with user-controlled content?

If you send a user string with `res.send()`, Express sets `Content-Type: text/html` by default. If that string contains `<script>`, the browser runs it: a reflected XSS. Examples are echoing query params or error messages. Use `res.json()` for data, set `Content-Type` to `text/plain` for plain text, escape HTML in templates, and set `X-Content-Type-Options: nosniff`.

```js
// bad: /hello?name=<script>alert(1)</script>
app.get("/hello", (req, res) => res.send(`Hello ${req.query.name}`));
```

### 391: How do you handle timezones and dates in an Express API?

Store and send dates in UTC as ISO 8601 strings (`2026-10-26T12:00:00.000Z`), which is what `JSON.stringify` does with `Date`. Let clients convert to local time. When you accept dates, validate the format and be clear about whether a value is a date only (`2026-10-26`) or a moment in time. Do business logic that depends on a local day (like "orders today") with an explicit timezone, using `Temporal` (where available) or a library like `date-fns-tz`.

### 392: How do you return money values in an Express API?

Do not use floating point numbers for money in JSON, since `0.1 + 0.2` is not `0.3`. Store amounts as integers in the smallest unit (cents) or as decimal types in the database, and send them as integers with a currency code, or as strings:

```json
{ "amount": 1999, "currency": "EUR" }
```

Be careful with database drivers that return `DECIMAL` or `BIGINT` values as strings; keep them as strings or convert on purpose.

### 393: How would you design file upload for very large files (several GB)?

Do not send them through Express. Use direct uploads to object storage:

1. Client asks `POST /uploads` for an upload.
2. Express checks permissions, creates a record, and returns a presigned URL (or a multipart upload with presigned part URLs for S3).
3. Client uploads straight to S3, with resume support.
4. S3 sends an event (or the client calls `POST /uploads/:id/complete`) and a worker processes the file.

The Node process never holds the file, so memory and bandwidth stay low.

### 394: What problems can come from mounting the same router in two places?

A router object holds its own stack, so mounting it twice (`app.use('/a', r)` and `app.use('/b', r)`) works and both paths share the same handlers and `router.param` callbacks. But `req.baseUrl` differs, so links built from a fixed path may be wrong. Code that runs once per router (like adding middleware later) affects both places. If one path needs different middleware, create two routers with a factory function instead.

### 395: How do you hot-reload routes without restarting the server?

In development, `node --watch` restart is simplest and reliable. Real hot reloading in Node is tricky: you have to clear `require.cache` (CommonJS) and swap the router, and old closures, timers and connections may stay around. Some tools (like Vite's SSR mode or `vite-node`) do it, but it is rarely worth doing for an API. In production, use rolling restarts instead.

### 396: How would you add GraphQL to an existing Express REST API?

Mount a GraphQL server on its own path, reuse the same auth middleware and services:

```js
const { ApolloServer } = require("@apollo/server");
const { expressMiddleware } = require("@as-integrations/express5");

const server = new ApolloServer({ typeDefs, resolvers });
await server.start();

app.use(
  "/graphql",
  authenticate,
  express.json(),
  expressMiddleware(server, {
    context: async ({ req }) => ({ user: req.user, services }),
  }),
);
```

Resolvers call the same service layer as REST controllers, so business logic stays in one place. The Express 5 integration package is separate from the older Express 4 one, so pick the one matching your Express version.

### 397: How do you protect a GraphQL endpoint in Express from expensive queries?

GraphQL lets clients ask for deep and wide data in one request. Add limits: maximum query depth, query cost or complexity analysis, a limit on list sizes, timeouts, persisted queries (only allow known queries in production), and the DataLoader pattern to avoid N+1 database calls. Also consider turning off introspection in production for private APIs.

### 398: How do you share one Express app between HTTP and serverless functions in a monorepo?

Export a `createApp()` from a shared package, and have thin entry points:

```js
// apps/api/server.js
createApp(deps).listen(process.env.PORT);

// apps/api/lambda.js
const serverless = require("serverless-http");
module.exports.handler = serverless(createApp(deps));
```

Keep startup work (DB connections, config parsing) outside the Lambda handler but lazy, and avoid anything that needs a long-lived process in the shared app code.

### 399: How do Lambda cold starts affect Express, and how do you reduce them?

On a cold start, Lambda loads your code, runs module setup and builds the app before handling the first request. A large Express app with many dependencies can take hundreds of milliseconds or more. To reduce it: bundle and tree-shake with esbuild, remove unused dependencies, lazy-load rarely used modules, keep setup small, choose more memory (which also gives more CPU), and use provisioned concurrency or SnapStart where supported for latency-sensitive endpoints.

### 400: How do you handle the `X-Forwarded-*` headers when Express runs on Lambda behind API Gateway?

API Gateway and ALB pass client info in the event (and add `X-Forwarded-For`), and the adapter maps the event to a Node request. Set `trust proxy` so `req.ip` and `req.protocol` use those headers. Check the adapter docs, because the source IP may also be available directly in the event's request context, which is more reliable than headers.

### 401: How does the libuv thread pool affect an Express app?

Some async operations in Node run on a small thread pool (4 threads by default): `fs` calls, `dns.lookup`, `crypto.pbkdf2`, `scrypt`, bcrypt/argon2 native bindings, and zlib. If many requests hash passwords or read files at once, they wait for a free thread, even though the event loop is not blocked. You can raise the size with `UV_THREADPOOL_SIZE` (set before Node starts), but more threads also compete for CPU. For heavy work, move it to worker threads or other services.

### 402: How do you move CPU-heavy work off the main thread in an Express route?

Use a worker pool like `piscina`:

```js
const Piscina = require("piscina");
const pool = new Piscina({ filename: require.resolve("./resize-worker.js") });

app.post(
  "/resize",
  express.raw({ type: "image/*", limit: "10mb" }),
  async (req, res) => {
    const output = await pool.run({ image: req.body, width: 300 });
    res.type("png").send(Buffer.from(output));
  },
);
```

The event loop stays free to handle other requests while the worker does the work. Limit the queue size so a burst of work cannot use all memory.

### 403: What is the difference between using `cluster` and `worker_threads` for an Express app?

`cluster` runs several separate Node processes that share the listening port, each with its own Express app, memory and event loop. It scales request handling across CPU cores. `worker_threads` run JavaScript in other threads inside one process; they share the process and can transfer memory, and are good for CPU-heavy tasks, not for running whole HTTP servers. In containers, people often skip `cluster` and run more containers instead.

### 404: How does the cluster module share one port between worker processes?

The primary process creates the listening socket. By default on Linux and macOS it accepts connections and hands them to workers in round-robin order. Workers call `app.listen()` as normal, but the call goes through the primary. On Windows the default is to let the OS spread connections. Because each worker is a separate process, anything in memory (sessions, caches, rate limits, WebSocket clients) is not shared.

### 405: How do you write middleware that is safe to use in both Express 4 and Express 5?

- Do not assign to `req.query`.
- Do not depend on `req.body` being `{}`.
- Avoid removed methods (`req.param`, `res.send(status)`).
- Handle your own promise errors and call `next(err)`, so it also works in Express 4.
- Do not touch router internals.
- Declare `express` as a peer dependency with a range like `^4.21.0 || ^5.0.0` and test with both.

### 406: How do you add custom methods to `res` for all apps without monkey patching globally?

Add them per app on `app.response`, which is the prototype for that app's `res` objects:

```js
app.response.problem = function (status, title, detail) {
  return this.status(status)
    .type("application/problem+json")
    .json({ status, title, detail });
};

app.get("/x", (req, res) => res.problem(404, "Not Found", "No such x"));
```

For TypeScript, also extend `Express.Response`. A plain helper function (`sendProblem(res, ...)`) is often clearer and easier to type.

### 407: What is the cost of `Object.setPrototypeOf` on every request?

Changing an object's prototype can make V8 drop some optimizations for that object, because its hidden class changes. Express does this for every `req` and `res`. It is one of the reasons Express is slower than frameworks that wrap the request in a new object instead. For most apps the cost is small compared to I/O, but it shows in micro benchmarks.

### 408: How do you handle errors from response streams after `res.json()` is called?

`res.json()` writes the body and ends the response. Errors after that (like the client closing the connection) show up as `error` or `close` events on `res`, not in the error handler. Usually you can ignore a client disconnect. If you need to know whether the response was fully sent, check `res.writableFinished` in a `close` listener:

```js
res.on("close", () => {
  if (!res.writableFinished)
    req.log.warn("client disconnected before response finished");
});
```

### 409: How do you build a plugin system on top of Express?

Define a plugin as a function that gets the app (or a router) and some shared services:

```js
// plugin
module.exports = function auditPlugin({ router, services }) {
  router.use(services.auth.required);
  router.get("/audit", async (req, res) =>
    res.json(await services.audit.list()),
  );
};

// app
for (const plugin of plugins) {
  const router = express.Router();
  plugin({ router, services });
  app.use(`/plugins/${plugin.name}`, router);
}
```

Giving each plugin its own router under its own prefix keeps them apart. Load order, config validation and dependencies between plugins become your job, which is something Fastify's plugin system does for you.

### 410: How do you make sure no route is left without authentication by mistake?

Make the safe option the default: add authentication globally, and opt out for public routes in a clear list:

```js
const PUBLIC = [
  { method: "GET", path: "/health" },
  { method: "POST", path: "/login" },
];

app.use((req, res, next) => {
  if (PUBLIC.some((p) => p.method === req.method && p.path === req.path))
    return next();
  authenticate(req, res, next);
});
```

Add a test that walks the router stack or calls every route without a token and expects 401, except the public ones.

### 411: How can you list all routes in an Express app?

There is no official API. You can walk `app.router.stack` (Express 5) or `app._router.stack` (Express 4), and look at layers that have a `route`. These are internals and change between versions, so only use this for debugging or tests. A cleaner way is to keep routes in a table that you both register and document:

```js
const routes = [
  { method: "get", path: "/users", handler: listUsers },
  { method: "post", path: "/users", handler: createUser },
];
routes.forEach((r) => router[r.method](r.path, r.handler));
```

### 412: How would you design an Express API that has to serve both web and mobile clients?

- Keep one core API with stable resources and versioning, because mobile apps stay on old versions for a long time.
- Support pagination, filtering and sparse fields so mobile clients can fetch less.
- Use token-based auth with refresh tokens for mobile, and cookies for web.
- Add a "backend for frontend" layer if the clients need very different shapes.
- Keep old versions running until usage drops, and send deprecation headers (`Deprecation`, `Sunset`).

### 413: How do you deprecate an endpoint without breaking clients?

Announce it, keep it working, and add headers so clients can detect it:

```js
router.get(
  "/v1/orders",
  (req, res, next) => {
    res.set("Deprecation", "@1767225600"); // RFC 9745 date format
    res.set("Sunset", "Thu, 01 Jul 2027 00:00:00 GMT"); // RFC 8594
    res.set("Link", '</v2/orders>; rel="successor-version"');
    next();
  },
  listOrdersV1,
);
```

Track who still calls it (by API key or user agent), contact them, and remove it only after usage is gone or the sunset date passes.

### 414: How do you prevent mass assignment in Express handlers?

Mass assignment is when you pass `req.body` straight into a create or update, so clients can set fields like `role` or `isAdmin`:

```js
// bad
await User.update(req.params.id, req.body);
```

Only pick the allowed fields, ideally with a schema that strips unknown keys:

```js
const UpdateProfile = z
  .object({ name: z.string().max(100), bio: z.string().max(500) })
  .strict();
const data = UpdateProfile.parse(req.body);
await User.update(req.user.id, data);
```

### 415: How do you handle partial updates (PATCH) safely with JSON Merge Patch?

With `application/merge-patch+json` (RFC 7396), fields in the body replace fields in the resource, and `null` means delete. Validate the patch against a schema of allowed fields, apply it to the current resource, then validate the full result before saving:

```js
router.patch(
  "/:id",
  express.json({ type: "application/merge-patch+json" }),
  async (req, res) => {
    const patch = PatchSchema.parse(req.body);
    const current = await repo.get(req.params.id);
    const next = applyMergePatch(current, patch);
    const valid = ProductSchema.parse(next);
    res.json(await repo.save(valid));
  },
);
```

### 416: How do you avoid N+1 queries in Express endpoints?

N+1 is when you load a list, then run one query per item to load related data. Fix it by loading related data in one query: SQL joins, `IN (...)` queries, ORM `include` (Prisma) or `populate` (Mongoose). For GraphQL or nested resolvers, use DataLoader to batch lookups within a request. Log query counts per request in development to spot the problem.

### 417: How do you handle very slow clients reading large responses?

A slow client keeps the socket and your buffers open. Node streams with backpressure prevent memory from growing, but the connection still stays open. Put a reverse proxy in front with response buffering, so Node can send everything quickly to the proxy and move on. Also set limits on response size and use pagination.

### 418: What happens if you `await` something after the client already disconnected?

Your code keeps running, finishes the work, and then writes to a closed socket. `res.json()` will not throw in most cases; the data is just dropped. The wasted work can add up under load. Use `req.on('close')` (or check `req.socket.destroyed`) with an `AbortController` to cancel long work, especially database queries and outgoing calls that support abort signals.

### 419: How would you implement long polling in Express?

Keep the request open until data is ready or a timeout passes:

```js
const waiters = new Map(); // topic -> Set of res

app.get("/poll/:topic", (req, res) => {
  const set = waiters.get(req.params.topic) ?? new Set();
  waiters.set(req.params.topic, set);
  set.add(res);

  const timer = setTimeout(() => {
    set.delete(res);
    res.sendStatus(204);
  }, 25_000);
  req.on("close", () => {
    clearTimeout(timer);
    set.delete(res);
  });
});

function publish(topic, data) {
  for (const res of waiters.get(topic) ?? []) res.json(data);
  waiters.delete(topic);
}
```

This only works within one process. With many instances, use Redis pub/sub to notify all of them. SSE or WebSockets are usually better choices today.

### 420: How do you handle request cancellation when using a database that supports it?

Pass an abort signal or cancel the query when the client disconnects. With `pg`, you can cancel a running query with `pg_cancel_backend`, and some query builders support abort signals. Also set a `statement_timeout` on the database side so a runaway query is stopped no matter what the app does:

```js
const pool = new Pool({ connectionString, statement_timeout: 5000 });
```

### 421: How do you test that your Express app handles graceful shutdown correctly?

Start the real server in a test, open a slow request, send `SIGTERM` (or call your shutdown function), and check:

- The slow request still completes with 200.
- New connections are refused or get 503.
- The process exits within the timeout.
- Pools and clients were closed.

Running this in CI catches regressions where a new connection (Redis, a queue) is not closed and blocks shutdown.

### 422: How would you design health checks that do not cause outages?

Liveness should be cheap and only check that the process can respond; never check the database in liveness, or a database blip will restart every pod at once. Readiness can check critical dependencies, but with short timeouts and maybe cached results, so many checks do not overload the database. Do not make readiness fail because of optional dependencies. Return details only on an internal endpoint.

### 423: How would you debug a production issue where only some requests fail with 500?

1. Find the failing requests by status and route in logs or traces, and look at their request IDs.
2. Look for patterns: one instance, one route, one user, one input shape, a time window after a deploy.
3. Read the full error and stack trace for those IDs.
4. Reproduce with the same input in a staging or local environment.
5. Check dependencies used by that path (a specific database shard, external API).
6. Add a test for the case and fix it.

### 424: What is the difference between `res.on('finish')` and `res.on('close')`?

`finish` fires when the whole response was handed to the operating system, meaning it was sent successfully. `close` fires when the underlying connection or response is closed, whether the response finished or the client went away. In Node 18+ `close` fires in both cases, so to detect aborted responses, check `res.writableFinished` in the `close` handler. For metrics, listening to `close` and checking `writableFinished` covers both outcomes.

### 425: Why might middleware order cause a security bug?

Examples:

- `express.static` or a public router added before auth means those files are served without checks, which is fine for public assets but bad for private folders.
- A CORS middleware after a route means that route does not send CORS headers.
- Rate limiting after the expensive body parsing means attackers still make you parse large bodies.
- An error handler before some routes means errors from those routes reach the default handler and may leak details.

Review the order in `app.js` as part of security reviews.

### 426: How do you safely use `app.set('trust proxy', true)` in development and something stricter in production?

Make it a config value:

```js
const trustProxy = process.env.TRUST_PROXY ?? "loopback";
app.set(
  "trust proxy",
  /^\d+$/.test(trustProxy) ? Number(trustProxy) : trustProxy,
);
```

Then production sets `TRUST_PROXY=1` (or a subnet list) based on the real network setup, and nobody uses `true` by accident.

### 427: What are the trade-offs of using Express for a high-throughput internal microservice?

Pros: everyone knows it, many middleware packages, easy to debug. Cons: higher per-request overhead than Fastify or Hono, no built-in schema validation or serialization, no structure for plugins and lifecycle hooks, and no native HTTP/2. For a service doing tens of thousands of requests per second per instance with tight latency goals, the overhead may matter. For most services, the time is in I/O and Express is fine.

### 428: How do you measure Express overhead in your own app?

Benchmark a trivial route (like `/ping` that returns `ok`) with all your global middleware, and compare it with a plain `http` server returning the same thing. Then remove middleware one by one to see what each costs. Use `autocannon` with the same settings each time, and run on hardware close to production. Often the biggest costs are logging, sessions and body parsing on routes that do not need them, not Express itself.

### 429: How would you implement a simple API gateway feature: request aggregation?

One endpoint calls several services in parallel and combines the results:

```js
app.get("/dashboard", authenticate, async (req, res) => {
  const opts = {
    signal: AbortSignal.timeout(2000),
    headers: { "X-User-Id": req.user.id },
  };
  const [profile, orders, notifications] = await Promise.allSettled([
    fetch(`${USERS}/me`, opts).then((r) => r.json()),
    fetch(`${ORDERS}/recent`, opts).then((r) => r.json()),
    fetch(`${NOTIFY}/unread`, opts).then((r) => r.json()),
  ]);
  res.json({
    profile: profile.value ?? null,
    orders: orders.value ?? [],
    notifications: notifications.value ?? [],
    partial: [profile, orders, notifications].some(
      (r) => r.status === "rejected",
    ),
  });
});
```

`allSettled` lets the page still load when one service fails.

### 430: How do you propagate trace context from Express to other services?

With OpenTelemetry, the HTTP instrumentation reads `traceparent` from incoming requests and adds it to outgoing `http` and `fetch` calls, so traces connect across services. If you do it by hand, read `traceparent` (W3C Trace Context) from `req` and forward it on outgoing requests. Also include the trace ID in your logs so logs and traces link together.

### 431: How do you ensure logs from one request are grouped together across async calls?

Use a child logger per request and pass it through `AsyncLocalStorage`, or use `req.log` from `pino-http`. Everything logged during the request then has the same request ID and trace ID:

```js
const als = new AsyncLocalStorage();
app.use((req, res, next) =>
  als.run({ log: logger.child({ reqId: req.id }) }, next),
);
const log = () => als.getStore()?.log ?? logger;
```

Code deep in services calls `log().info(...)` without needing `req`.

### 432: What is a common mistake with `AsyncLocalStorage` in Express middleware?

A few common ones:

- Setting the store after `next()` was already called. Later middleware never sees it. Wrap `next` in `als.run(store, next)` instead.
- Using `als.enterWith()` in middleware, which can leak the store into code that is not part of the request.
- Libraries that queue callbacks and run them later from shared objects (some connection pools, event emitters created at startup). Those callbacks may run with the wrong store or none.

Test that the context is present in the deepest calls you care about, like database query logs.

### 433: How would you handle tenant-specific configuration and rate limits in a multi-tenant Express app?

Load tenant config once per request (cached in memory with a short TTL, or in Redis) in an early middleware. Build rate limiters keyed by tenant and plan:

```js
const limiter = rateLimit({
  windowMs: 60_000,
  limit: (req) => (req.tenant.plan === "pro" ? 1000 : 100),
  keyGenerator: (req) => `tenant:${req.tenant.id}`,
  store: new RedisStore({ sendCommand: (...args) => redis.sendCommand(args) }),
});
```

`express-rate-limit` accepts a function for `limit`, which makes per-plan limits easy.

### 434: How do you prevent cache poisoning in an Express app behind a CDN?

The CDN caches by URL (and some headers). If your response depends on a header the CDN does not include in its cache key (like `X-Forwarded-Host` or `Accept-Language`), an attacker can make you return a bad response that the CDN then serves to everyone. Fixes: do not build URLs or content from untrusted headers, set `Vary` correctly, mark user-specific responses `private` or `no-store`, and configure the CDN's cache key to include headers that change the response.

### 435: How do you test security headers and CORS behavior automatically?

Write tests with supertest that check headers:

```js
test("preflight from unknown origin is not allowed", async () => {
  const res = await request(app)
    .options("/api/orders")
    .set("Origin", "https://evil.example")
    .set("Access-Control-Request-Method", "POST");
  expect(res.headers["access-control-allow-origin"]).toBeUndefined();
});

test("security headers present", async () => {
  const res = await request(app).get("/");
  expect(res.headers["x-content-type-options"]).toBe("nosniff");
  expect(res.headers["x-powered-by"]).toBeUndefined();
});
```

Tools like OWASP ZAP can scan a running staging app for more issues.

### 436: How do you keep Express dependencies secure over time?

- Run `npm audit` and tools like Dependabot, Renovate or Snyk in CI.
- Use a lock file and `npm ci` in builds.
- Remove unused packages; many small middleware packages are no longer maintained.
- Watch the Express security releases and the Node security release schedule.
- Avoid packages that patch Express internals.
- Pin and review major updates with tests.

### 437: How would you approach replacing Express with Fastify in a large app?

Do it step by step. Fastify has `@fastify/express` (and `@fastify/middie`) to run Express middleware and routers inside Fastify, so you can move the server first and then migrate routes over time. Rewrite hot routes first to get the benefit, using Fastify schemas for validation and serialization. Keep the business logic in services that do not depend on either framework, which makes this kind of change much easier. Measure before and after, to make sure the change is worth it.

### 438: What makes an Express codebase hard to maintain, and how do you avoid it?

Common problems: business logic in route handlers, global mutable state, many small middleware that change `req` in hidden ways, inconsistent error handling, no validation, and huge `app.js` files. Fix it with clear layers (routes, services, data access), one error handler, schemas for input, a factory for the app with injected dependencies, typed request properties, and tests at the HTTP level. Keep middleware that adds data to `req` few and well documented.

### 439: A request body is sometimes `undefined` in Express 5. Why?

In Express 5, `req.body` stays `undefined` until a body parser sets it. Causes:

- No parser mounted, or mounted after the route.
- The `Content-Type` does not match the parser's `type` (for example a client sends `text/plain` with JSON).
- The request has no body (GET, or `Content-Length: 0`).
- Another middleware (like a proxy) already read the stream.

Code like `const { name } = req.body` then throws. Validate with a schema that handles a missing body, or default it: `const body = req.body ?? {}`.

### 440: How do you handle requests with a JSON body that is a primitive, like `"hello"` or `42`?

By default `express.json()` has `strict: true`, which only accepts objects and arrays and rejects other values with 400. If you need to accept primitives, set `strict: false`. Either way, validate the shape, because code that expects an object will break on a number or a string.

### 441: How do you add response validation to catch bugs in development?

Validate outgoing data against the same schema you document, but only in development and test, because it costs CPU:

```js
const isDev = process.env.NODE_ENV !== "production";

function sendValid(res, schema, data) {
  if (isDev) schema.parse(data); // throws if the handler returns the wrong shape
  res.json(data);
}
```

`express-openapi-validator` also has `validateResponses`. This catches leaked fields and wrong types before clients do.

### 442: What are the risks of `app.use(express.static('.'))` or similar?

Serving the project root exposes everything: source code, `.env` files (if `dotfiles` is not ignored), `package.json`, the `.git` folder in some setups, and config files with secrets. Always serve a dedicated `public` folder with only the files meant to be public, built by your build step.

### 443: How do you make an Express app work with ES modules and top-level await at startup?

With `"type": "module"`, you can use top-level `await` for setup:

```js
// server.js
import { createApp } from "./app.js";
import { connectDb } from "./db.js";

const db = await connectDb(process.env.DATABASE_URL);
const app = createApp({ db });

const server = app.listen(process.env.PORT ?? 3000);
```

If the connection fails, the module throws and the process exits with an error, which is what you want. Use `import.meta.dirname` in place of `__dirname` for paths.

### 444: How do you use Express with Bun or Deno?

Both run most Express apps through their Node compatibility layers: `bun run server.js` works with `express` from npm, and Deno can `import express from 'npm:express'`. Performance and compatibility are usually good, but some native modules, `node:http` edge cases and less common middleware may behave differently. Test your full app, not just a hello world, before switching runtimes in production.

### 445: How would you design request validation, error format, and docs so they never drift apart?

Use one source of truth. Either:

- Schema-first: write OpenAPI, validate requests with `express-openapi-validator`, and generate client types from the spec.
- Code-first: write zod schemas, use them for validation and TypeScript types, and generate OpenAPI from them.

Also generate the error responses from the same error classes. Add a CI check that the generated spec is up to date, and contract tests that call each endpoint and check responses against the spec.

### 446: You need to add authentication to an existing public API that many clients use. How do you roll it out?

1. Add auth middleware in "observe" mode: accept requests without credentials but log who sends them.
2. Give clients API keys or OAuth credentials, and announce a deadline.
3. Return a warning header to unauthenticated callers.
4. Turn on enforcement for new clients first, then for everyone after the deadline.
5. Watch 401 rates and contact clients who are still failing.

Doing it step by step avoids breaking everyone at once.

### 447: An Express app's memory grows until it is OOM killed every few hours. Walk through your approach.

1. Confirm it is the JS heap (`process.memoryUsage().heapUsed`) and not native memory (RSS grows, heap stays flat, which points to Buffers or native modules).
2. Check for known culprits: MemoryStore sessions, unbounded `Map` caches, per-request listeners on long-lived emitters, large in-flight responses.
3. Take two or three heap snapshots some time apart under load and compare which object types grow.
4. Follow the retainer chain to the code that keeps them.
5. Fix and verify memory stays flat in a long load test.

Meanwhile, set `--max-old-space-size` and a restart policy so the impact is smaller.

### 448: What would you change in an Express app before a big launch?

- Load test and fix the top bottlenecks.
- Set timeouts on the server and all outgoing calls.
- Add rate limits and load shedding.
- Make sure logs, metrics, traces and alerts work, with dashboards for latency and errors.
- Check graceful shutdown and health checks.
- Turn on CDN caching for static and public data.
- Review security headers, CORS, auth on every route, and dependency audits.
- Prepare a rollback plan and feature flags to turn off heavy features.

### 449: How do you explain the Express request lifecycle end to end, from socket to response?

1. Node's HTTP server accepts the TCP connection and parses the request with `llhttp`.
2. It emits `request` with `IncomingMessage` and `ServerResponse`.
3. The Express app function runs: it sets the prototypes of `req` and `res` to Express's own, and adds properties like `res.locals`.
4. The router walks its layers: global middleware, mounted routers, matching routes, each calling `next()`.
5. A handler calls `res.json()` or similar, which sets headers, serializes the body, maybe computes an ETag, and writes to the socket.
6. If something throws or calls `next(err)`, the router jumps to error handlers.
7. If nobody responds, `finalhandler` sends 404 or the error response.
8. `finish` and `close` events fire, and the socket is kept alive for the next request or closed.

### 450: What do you think are the most important habits for building good Express apps?

Keep Express at the edge and the business logic in plain modules. Validate every input with schemas. Handle errors in one place with a stable format. Configure security (helmet, CORS, cookie flags, `trust proxy`, rate limits) on purpose instead of copying snippets. Set timeouts, log in JSON with request IDs, and expose health checks and metrics. Shut down gracefully. Write HTTP-level tests with supertest. Keep Node, Express and middleware up to date, and read the migration guide when a new major version comes out.
