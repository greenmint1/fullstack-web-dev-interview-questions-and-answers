# Fastify Interview Questions and Answers

_Last updated: October 29, 2026_

450 Fastify interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Fastify v5 (5.12 at the time of writing), which needs Node.js 20 or newer. Changes from v4 are pointed out where they matter, since a lot of projects still run v4 or are in the middle of upgrading. Fastify v6 is in alpha and is not covered here.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Fastify?](#1-what-is-fastify)
- [2: Why is Fastify called fast?](#2-why-is-fastify-called-fast)
- [3: How do you install Fastify and create a basic server?](#3-how-do-you-install-fastify-and-create-a-basic-server)
- [4: Which Node.js version does Fastify v5 need?](#4-which-nodejs-version-does-fastify-v5-need)
- [5: How do you start the server with listen()?](#5-how-do-you-start-the-server-with-listen)
- [6: Why does the default host matter when running Fastify in Docker?](#6-why-does-the-default-host-matter-when-running-fastify-in-docker)
- [7: How do you define a GET route?](#7-how-do-you-define-a-get-route)
- [8: What is the full route declaration with app.route()?](#8-what-is-the-full-route-declaration-with-approute)
- [9: What are the request and reply objects?](#9-what-are-the-request-and-reply-objects)
- [10: How do you read route params?](#10-how-do-you-read-route-params)
- [11: How do you read query string values?](#11-how-do-you-read-query-string-values)
- [12: How do you read the request body?](#12-how-do-you-read-the-request-body)
- [13: Which content types does Fastify parse out of the box?](#13-which-content-types-does-fastify-parse-out-of-the-box)
- [14: How do you send a response?](#14-how-do-you-send-a-response)
- [15: How do you set the status code?](#15-how-do-you-set-the-status-code)
- [16: How do you set response headers?](#16-how-do-you-set-response-headers)
- [17: How do you read request headers?](#17-how-do-you-read-request-headers)
- [18: How do you redirect in Fastify?](#18-how-do-you-redirect-in-fastify)
- [19: What is a plugin in Fastify?](#19-what-is-a-plugin-in-fastify)
- [20: What does app.register() do?](#20-what-does-appregister-do)
- [21: How do you add a prefix to all routes in a plugin?](#21-how-do-you-add-a-prefix-to-all-routes-in-a-plugin)
- [22: What is encapsulation in Fastify?](#22-what-is-encapsulation-in-fastify)
- [23: What is fastify-plugin used for?](#23-what-is-fastify-plugin-used-for)
- [24: What is a decorator?](#24-what-is-a-decorator)
- [25: What is the difference between decorate, decorateRequest and decorateReply?](#25-what-is-the-difference-between-decorate-decoraterequest-and-decoratereply)
- [26: What are hooks in Fastify?](#26-what-are-hooks-in-fastify)
- [27: What is the onRequest hook used for?](#27-what-is-the-onrequest-hook-used-for)
- [28: What is the preHandler hook used for?](#28-what-is-the-prehandler-hook-used-for)
- [29: What is the onResponse hook used for?](#29-what-is-the-onresponse-hook-used-for)
- [30: How does logging work in Fastify?](#30-how-does-logging-work-in-fastify)
- [31: How do you set the log level?](#31-how-do-you-set-the-log-level)
- [32: How do you get pretty logs during development?](#32-how-do-you-get-pretty-logs-during-development)
- [33: What is JSON Schema used for in Fastify?](#33-what-is-json-schema-used-for-in-fastify)
- [34: How do you validate a request body?](#34-how-do-you-validate-a-request-body)
- [35: What does a validation error response look like?](#35-what-does-a-validation-error-response-look-like)
- [36: How do you validate query strings and params?](#36-how-do-you-validate-query-strings-and-params)
- [37: How do you validate request headers?](#37-how-do-you-validate-request-headers)
- [38: Why must schemas be full JSON Schemas in v5?](#38-why-must-schemas-be-full-json-schemas-in-v5)
- [39: What is a response schema?](#39-what-is-a-response-schema)
- [40: Can a response schema use status code ranges?](#40-can-a-response-schema-use-status-code-ranges)
- [41: How does error handling work in an async handler?](#41-how-does-error-handling-work-in-an-async-handler)
- [42: How do you return a 404 for a missing resource?](#42-how-do-you-return-a-404-for-a-missing-resource)
- [43: What is setErrorHandler?](#43-what-is-seterrorhandler)
- [44: What is setNotFoundHandler?](#44-what-is-setnotfoundhandler)
- [45: What does Fastify return when a route does not exist?](#45-what-does-fastify-return-when-a-route-does-not-exist)
- [46: What is app.inject()?](#46-what-is-appinject)
- [47: How do you write a simple test for a Fastify route?](#47-how-do-you-write-a-simple-test-for-a-fastify-route)
- [48: What does app.ready() do?](#48-what-does-appready-do)
- [49: How do you stop a Fastify server?](#49-how-do-you-stop-a-fastify-server)
- [50: What is app.after()?](#50-what-is-appafter)
- [51: How do you serve static files?](#51-how-do-you-serve-static-files)
- [52: How do you enable CORS?](#52-how-do-you-enable-cors)
- [53: How do you add security headers?](#53-how-do-you-add-security-headers)
- [54: How do you parse form data (urlencoded)?](#54-how-do-you-parse-form-data-urlencoded)
- [55: How do you handle file uploads?](#55-how-do-you-handle-file-uploads)
- [56: How do you work with cookies?](#56-how-do-you-work-with-cookies)
- [57: How do you add JWT authentication?](#57-how-do-you-add-jwt-authentication)
- [58: What is @fastify/sensible?](#58-what-is-fastifysensible)
- [59: Can you use callbacks instead of async/await in handlers?](#59-can-you-use-callbacks-instead-of-asyncawait-in-handlers)
- [60: Should you both return a value and call reply.send() in an async handler?](#60-should-you-both-return-a-value-and-call-replysend-in-an-async-handler)
- [61: What happens if an async handler returns undefined?](#61-what-happens-if-an-async-handler-returns-undefined)
- [62: How do you send an empty response with 204?](#62-how-do-you-send-an-empty-response-with-204)
- [63: How do you send HTML?](#63-how-do-you-send-html)
- [64: How do you render templates?](#64-how-do-you-render-templates)
- [65: What is request.id?](#65-what-is-requestid)
- [66: How do you get the client IP address?](#66-how-do-you-get-the-client-ip-address)
- [67: What other useful properties does the request object have?](#67-what-other-useful-properties-does-the-request-object-have)
- [68: What is the difference between request.hostname and request.host in v5?](#68-what-is-the-difference-between-requesthostname-and-requesthost-in-v5)
- [69: What is the default body size limit?](#69-what-is-the-default-body-size-limit)
- [70: What does printRoutes() do?](#70-what-does-printroutes-do)
- [71: Why do GET routes also respond to HEAD?](#71-why-do-get-routes-also-respond-to-head)
- [72: How do you match any route with a wildcard?](#72-how-do-you-match-any-route-with-a-wildcard)
- [73: How do you make a route param optional?](#73-how-do-you-make-a-route-param-optional)
- [74: Can you use regular expressions in route params?](#74-can-you-use-regular-expressions-in-route-params)
- [75: How does Fastify handle trailing slashes?](#75-how-does-fastify-handle-trailing-slashes)
- [76: Are routes case sensitive?](#76-are-routes-case-sensitive)
- [77: What is @fastify/autoload?](#77-what-is-fastifyautoload)
- [78: What is fastify-cli?](#78-what-is-fastify-cli)
- [79: How do you use Fastify with CommonJS?](#79-how-do-you-use-fastify-with-commonjs)
- [80: How do you use Fastify with TypeScript?](#80-how-do-you-use-fastify-with-typescript)
- [81: What is a type provider?](#81-what-is-a-type-provider)
- [82: What is the onClose hook?](#82-what-is-the-onclose-hook)
- [83: What is the onReady hook?](#83-what-is-the-onready-hook)
- [84: What is the onRoute hook?](#84-what-is-the-onroute-hook)
- [85: What is app.server?](#85-what-is-appserver)
- [86: How do you get the address the server is listening on?](#86-how-do-you-get-the-address-the-server-is-listening-on)
- [87: How do you run Fastify over HTTPS?](#87-how-do-you-run-fastify-over-https)
- [88: Does Fastify support HTTP/2?](#88-does-fastify-support-http2)
- [89: What does reply.sent tell you?](#89-what-does-replysent-tell-you)
- [90: How do you get the response time of a request?](#90-how-do-you-get-the-response-time-of-a-request)
- [91: What is the difference between app.log and request.log?](#91-what-is-the-difference-between-applog-and-requestlog)
- [92: Does Fastify log requests automatically?](#92-does-fastify-log-requests-automatically)
- [93: How do you redact sensitive data from logs?](#93-how-do-you-redact-sensitive-data-from-logs)
- [94: What does reply.hijack() do?](#94-what-does-replyhijack-do)
- [95: How do you send a stream?](#95-how-do-you-send-a-stream)
- [96: Can you send a Buffer?](#96-can-you-send-a-buffer)
- [97: How does Fastify compare to Express at a high level?](#97-how-does-fastify-compare-to-express-at-a-high-level)
- [98: Can you use Express middleware in Fastify?](#98-can-you-use-express-middleware-in-fastify)
- [99: What are the route-level hooks?](#99-what-are-the-route-level-hooks)
- [100: What does the route config option do?](#100-what-does-the-route-config-option-do)
- [101: What is request.routeOptions?](#101-what-is-requestrouteoptions)
- [102: How do you read environment variables in Fastify?](#102-how-do-you-read-environment-variables-in-fastify)
- [103: What is fastify.version?](#103-what-is-fastifyversion)
- [104: What is the plugin options object?](#104-what-is-the-plugin-options-object)
- [105: What is the difference between async and callback style plugins?](#105-what-is-the-difference-between-async-and-callback-style-plugins)
- [106: How do you register many routes from one file?](#106-how-do-you-register-many-routes-from-one-file)
- [107: How do you check if a decorator exists?](#107-how-do-you-check-if-a-decorator-exists)
- [108: What is hasPlugin()?](#108-what-is-hasplugin)
- [109: What is hasRoute()?](#109-what-is-hasroute)
- [110: How do you add compression?](#110-how-do-you-add-compression)
- [111: How do you add rate limiting?](#111-how-do-you-add-rate-limiting)
- [112: How do you generate OpenAPI docs?](#112-how-do-you-generate-openapi-docs)
- [113: How do you add a description and tags for OpenAPI docs?](#113-how-do-you-add-a-description-and-tags-for-openapi-docs)
- [114: How do you add a health check endpoint?](#114-how-do-you-add-a-health-check-endpoint)
- [115: What is @fastify/under-pressure?](#115-what-is-fastifyunder-pressure)
- [116: How do you connect to PostgreSQL in Fastify?](#116-how-do-you-connect-to-postgresql-in-fastify)
- [117: How do you connect to MongoDB?](#117-how-do-you-connect-to-mongodb)
- [118: How do you connect to Redis?](#118-how-do-you-connect-to-redis)
- [119: What is the this keyword inside a handler?](#119-what-is-the-this-keyword-inside-a-handler)
- [120: How do you access the Fastify instance from a request?](#120-how-do-you-access-the-fastify-instance-from-a-request)
- [121: How do you send JSON with a custom content type?](#121-how-do-you-send-json-with-a-custom-content-type)
- [122: What is the default JSON serializer?](#122-what-is-the-default-json-serializer)
- [123: How do you set a default value for a query param?](#123-how-do-you-set-a-default-value-for-a-query-param)
- [124: How do you accept only certain values for a field?](#124-how-do-you-accept-only-certain-values-for-a-field)
- [125: How do you reuse a schema across routes?](#125-how-do-you-reuse-a-schema-across-routes)
- [126: What formats can you use for strings in schemas?](#126-what-formats-can-you-use-for-strings-in-schemas)
- [127: What does Fastify do with extra fields in the body?](#127-what-does-fastify-do-with-extra-fields-in-the-body)
- [128: What is type coercion in Fastify validation?](#128-what-is-type-coercion-in-fastify-validation)
- [129: How do you handle a POST with an empty body?](#129-how-do-you-handle-a-post-with-an-empty-body)
- [130: What are the main official Fastify plugins?](#130-what-are-the-main-official-fastify-plugins)
- [131: How do you add WebSocket support?](#131-how-do-you-add-websocket-support)
- [132: What does app.prefix return?](#132-what-does-appprefix-return)
- [133: What does initialConfig show?](#133-what-does-initialconfig-show)
- [134: How do you add a custom header to every response?](#134-how-do-you-add-a-custom-header-to-every-response)
- [135: What is the onSend hook?](#135-what-is-the-onsend-hook)
- [136: What is the preSerialization hook?](#136-what-is-the-preserialization-hook)
- [137: What is the onError hook?](#137-what-is-the-onerror-hook)
- [138: How do you register several plugins in order?](#138-how-do-you-register-several-plugins-in-order)
- [139: Can you await app.register()?](#139-can-you-await-appregister)
- [140: Is Fastify a good fit for serverless?](#140-is-fastify-a-good-fit-for-serverless)
- [141: What does app.routing do?](#141-what-does-approuting-do)
- [142: How do you add a route for all HTTP methods?](#142-how-do-you-add-a-route-for-all-http-methods)
- [143: What HTTP methods does Fastify support by default?](#143-what-http-methods-does-fastify-support-by-default)
- [144: How do you add a custom HTTP method?](#144-how-do-you-add-a-custom-http-method)
- [145: How do you return a different status for validation errors?](#145-how-do-you-return-a-different-status-for-validation-errors)
- [146: How do you set up a project in TypeScript quickly?](#146-how-do-you-set-up-a-project-in-typescript-quickly)
- [147: How does Fastify handle JSON parse errors?](#147-how-does-fastify-handle-json-parse-errors)
- [148: Can Fastify serve both an API and a frontend?](#148-can-fastify-serve-both-an-api-and-a-frontend)
- [149: What are the Fastify request lifecycle steps in short?](#149-what-are-the-fastify-request-lifecycle-steps-in-short)
- [150: Where should you look when you need a Fastify plugin?](#150-where-should-you-look-when-you-need-a-fastify-plugin)

### Moderate Questions (151-300)

- [151: In what order do hooks run when they are added at different levels?](#151-in-what-order-do-hooks-run-when-they-are-added-at-different-levels)
- [152: What is the difference between async hooks and callback hooks?](#152-what-is-the-difference-between-async-hooks-and-callback-hooks)
- [153: How do you stop the request from a hook and send a response?](#153-how-do-you-stop-the-request-from-a-hook-and-send-a-response)
- [154: How do you return an error from a hook?](#154-how-do-you-return-an-error-from-a-hook)
- [155: What is the preParsing hook used for?](#155-what-is-the-preparsing-hook-used-for)
- [156: What is the preValidation hook used for?](#156-what-is-the-prevalidation-hook-used-for)
- [157: When should you use onRequest vs preHandler for authentication?](#157-when-should-you-use-onrequest-vs-prehandler-for-authentication)
- [158: What is the onTimeout hook?](#158-what-is-the-ontimeout-hook)
- [159: What is the onRequestAbort hook?](#159-what-is-the-onrequestabort-hook)
- [160: What are the preClose and onClose hooks and how do they differ?](#160-what-are-the-preclose-and-onclose-hooks-and-how-do-they-differ)
- [161: What is the onListen hook?](#161-what-is-the-onlisten-hook)
- [162: What is the onRegister hook?](#162-what-is-the-onregister-hook)
- [163: How do you add hooks that only apply to some routes?](#163-how-do-you-add-hooks-that-only-apply-to-some-routes)
- [164: Why does a decorator added in one plugin not appear in another?](#164-why-does-a-decorator-added-in-one-plugin-not-appear-in-another)
- [165: What are the common use cases for fastify-plugin?](#165-what-are-the-common-use-cases-for-fastify-plugin)
- [166: What do the name and dependencies options of fastify-plugin do?](#166-what-do-the-name-and-dependencies-options-of-fastify-plugin-do)
- [167: How do you write a plugin that accepts options with defaults?](#167-how-do-you-write-a-plugin-that-accepts-options-with-defaults)
- [168: Can plugin options be a function?](#168-can-plugin-options-be-a-function)
- [169: How do you decorate the request with a per-request object safely?](#169-how-do-you-decorate-the-request-with-a-per-request-object-safely)
- [170: What error do you get if you decorate after the server starts?](#170-what-error-do-you-get-if-you-decorate-after-the-server-starts)
- [171: What does the dependencies argument of decorate do?](#171-what-does-the-dependencies-argument-of-decorate-do)
- [172: What are getDecorator and setDecorator?](#172-what-are-getdecorator-and-setdecorator)
- [173: How do you add types for custom decorators in TypeScript?](#173-how-do-you-add-types-for-custom-decorators-in-typescript)
- [174: How do you type route params, body and query in TypeScript without a type provider?](#174-how-do-you-type-route-params-body-and-query-in-typescript-without-a-type-provider)
- [175: How do you use Zod with Fastify?](#175-how-do-you-use-zod-with-fastify)
- [176: Why does withTypeProvider need to be called in each plugin?](#176-why-does-withtypeprovider-need-to-be-called-in-each-plugin)
- [177: How do you write a typed plugin in TypeScript?](#177-how-do-you-write-a-typed-plugin-in-typescript)
- [178: What does schemaErrorFormatter do?](#178-what-does-schemaerrorformatter-do)
- [179: How do you return all validation errors instead of only the first?](#179-how-do-you-return-all-validation-errors-instead-of-only-the-first)
- [180: How do you detect a validation error in the error handler?](#180-how-do-you-detect-a-validation-error-in-the-error-handler)
- [181: How do you create typed errors with @fastify/error?](#181-how-do-you-create-typed-errors-with-fastifyerror)
- [182: How does the default error handler build its response?](#182-how-does-the-default-error-handler-build-its-response)
- [183: How do error handlers work with encapsulation?](#183-how-do-error-handlers-work-with-encapsulation)
- [184: Can you call setErrorHandler twice in the same plugin?](#184-can-you-call-seterrorhandler-twice-in-the-same-plugin)
- [185: What is the errorHandler route option?](#185-what-is-the-errorhandler-route-option)
- [186: Why should you not send a response inside onError?](#186-why-should-you-not-send-a-response-inside-onerror)
- [187: What happens if you call reply.send() twice?](#187-what-happens-if-you-call-replysend-twice)
- [188: How do you handle errors from a stream sent in the reply?](#188-how-do-you-handle-errors-from-a-stream-sent-in-the-reply)
- [189: What are custom content type parsers?](#189-what-are-custom-content-type-parsers)
- [190: How do you get the raw body for webhook signature checks?](#190-how-do-you-get-the-raw-body-for-webhook-signature-checks)
- [191: How do you make a catch-all content type parser?](#191-how-do-you-make-a-catch-all-content-type-parser)
- [192: How do you remove or replace the default JSON parser?](#192-how-do-you-remove-or-replace-the-default-json-parser)
- [193: How do you use the bodyLimit inside a custom parser?](#193-how-do-you-use-the-bodylimit-inside-a-custom-parser)
- [194: What are custom log serializers?](#194-what-are-custom-log-serializers)
- [195: How do you use a custom Pino instance?](#195-how-do-you-use-a-custom-pino-instance)
- [196: How do you change how request IDs are generated?](#196-how-do-you-change-how-request-ids-are-generated)
- [197: What does requestIdHeader do?](#197-what-does-requestidheader-do)
- [198: How do you change the label of the request ID in logs?](#198-how-do-you-change-the-label-of-the-request-id-in-logs)
- [199: What is LogController?](#199-what-is-logcontroller)
- [200: How do you log only slow requests?](#200-how-do-you-log-only-slow-requests)
- [201: How do you set the log level for one plugin?](#201-how-do-you-set-the-log-level-for-one-plugin)
- [202: What does trustProxy do?](#202-what-does-trustproxy-do)
- [203: How do you set the number of trusted proxy hops?](#203-how-do-you-set-the-number-of-trusted-proxy-hops)
- [204: What is the difference between connectionTimeout, keepAliveTimeout and requestTimeout?](#204-what-is-the-difference-between-connectiontimeout-keepalivetimeout-and-requesttimeout)
- [205: Why should keepAliveTimeout be higher than the load balancer's idle timeout?](#205-why-should-keepalivetimeout-be-higher-than-the-load-balancers-idle-timeout)
- [206: How do you do a graceful shutdown?](#206-how-do-you-do-a-graceful-shutdown)
- [207: What does return503OnClosing do?](#207-what-does-return503onclosing-do)
- [208: What does forceCloseConnections do?](#208-what-does-forcecloseconnections-do)
- [209: What is the pluginTimeout option?](#209-what-is-the-plugintimeout-option)
- [210: How do you find which plugin failed to load?](#210-how-do-you-find-which-plugin-failed-to-load)
- [211: What does findRoute() do?](#211-what-does-findroute-do)
- [212: How do you print the routes with more details?](#212-how-do-you-print-the-routes-with-more-details)
- [213: What are route constraints?](#213-what-are-route-constraints)
- [214: How do you version routes with the Accept-Version header?](#214-how-do-you-version-routes-with-the-accept-version-header)
- [215: How do you add a custom constraint?](#215-how-do-you-add-a-custom-constraint)
- [216: How do you build URLs with a prefix in a reusable plugin?](#216-how-do-you-build-urls-with-a-prefix-in-a-reusable-plugin)
- [217: How do prefixes handle the "/" route?](#217-how-do-prefixes-handle-the--route)
- [218: How do you test plugins in isolation?](#218-how-do-you-test-plugins-in-isolation)
- [219: How do you build the app for tests and production from the same code?](#219-how-do-you-build-the-app-for-tests-and-production-from-the-same-code)
- [220: How do you send a POST with JSON in inject()?](#220-how-do-you-send-a-post-with-json-in-inject)
- [221: Can you chain inject() calls?](#221-can-you-chain-inject-calls)
- [222: How do you test with a real HTTP server?](#222-how-do-you-test-with-a-real-http-server)
- [223: Which test runners work well with Fastify?](#223-which-test-runners-work-well-with-fastify)
- [224: How do you mock an outgoing HTTP call in tests?](#224-how-do-you-mock-an-outgoing-http-call-in-tests)
- [225: How do you add authentication to many routes with @fastify/auth?](#225-how-do-you-add-authentication-to-many-routes-with-fastifyauth)
- [226: How do you write an authenticate decorator with @fastify/jwt?](#226-how-do-you-write-an-authenticate-decorator-with-fastifyjwt)
- [227: How do you read a JWT from a cookie with @fastify/jwt?](#227-how-do-you-read-a-jwt-from-a-cookie-with-fastifyjwt)
- [228: How do you add role-based access checks?](#228-how-do-you-add-role-based-access-checks)
- [229: What is the difference between @fastify/session and @fastify/secure-session?](#229-what-is-the-difference-between-fastifysession-and-fastifysecure-session)
- [230: How do you set up server-side sessions with Redis?](#230-how-do-you-set-up-server-side-sessions-with-redis)
- [231: How do you protect against CSRF?](#231-how-do-you-protect-against-csrf)
- [232: How do you proxy requests to another service?](#232-how-do-you-proxy-requests-to-another-service)
- [233: How do you send Server-Sent Events?](#233-how-do-you-send-server-sent-events)
- [234: Can you return a Web ReadableStream or a Response object?](#234-can-you-return-a-web-readablestream-or-a-response-object)
- [235: How do you add ETag support?](#235-how-do-you-add-etag-support)
- [236: How do you set caching headers per route?](#236-how-do-you-set-caching-headers-per-route)
- [237: How do you implement pagination with validation?](#237-how-do-you-implement-pagination-with-validation)
- [238: How do you use Prisma with Fastify?](#238-how-do-you-use-prisma-with-fastify)
- [239: How do you structure a medium-size Fastify project?](#239-how-do-you-structure-a-medium-size-fastify-project)
- [240: How do you share schemas between files with $ref?](#240-how-do-you-share-schemas-between-files-with-ref)
- [241: What do getSchema and getSchemas return?](#241-what-do-getschema-and-getschemas-return)
- [242: How can you use TypeBox schemas without the type provider?](#242-how-can-you-use-typebox-schemas-without-the-type-provider)
- [243: What is fluent-json-schema?](#243-what-is-fluent-json-schema)
- [244: How do you add custom Ajv keywords or plugins?](#244-how-do-you-add-custom-ajv-keywords-or-plugins)
- [245: How do you change Ajv options like coerceTypes?](#245-how-do-you-change-ajv-options-like-coercetypes)
- [246: Why might coerceTypes cause surprises?](#246-why-might-coercetypes-cause-surprises)
- [247: Does Fastify validate response data against the response schema?](#247-does-fastify-validate-response-data-against-the-response-schema)
- [248: What happens when a response object does not match the response schema types?](#248-what-happens-when-a-response-object-does-not-match-the-response-schema-types)
- [249: How do you skip the response schema for one route?](#249-how-do-you-skip-the-response-schema-for-one-route)
- [250: What is setReplySerializer?](#250-what-is-setreplyserializer)
- [251: How do you handle content negotiation for different formats?](#251-how-do-you-handle-content-negotiation-for-different-formats)
- [252: How do you set a response schema per content type?](#252-how-do-you-set-a-response-schema-per-content-type)
- [253: How do you handle multipart fields and files together?](#253-how-do-you-handle-multipart-fields-and-files-together)
- [254: What does attachFieldsToBody do in @fastify/multipart?](#254-what-does-attachfieldstobody-do-in-fastifymultipart)
- [255: How do you limit file size and count with multipart?](#255-how-do-you-limit-file-size-and-count-with-multipart)
- [256: How do you migrate an Express app to Fastify step by step?](#256-how-do-you-migrate-an-express-app-to-fastify-step-by-step)
- [257: How do Express middleware concepts map to Fastify?](#257-how-do-express-middleware-concepts-map-to-fastify)
- [258: What are the main breaking changes when upgrading from v4 to v5?](#258-what-are-the-main-breaking-changes-when-upgrading-from-v4-to-v5)
- [259: How should you approach a v4 to v5 upgrade?](#259-how-should-you-approach-a-v4-to-v5-upgrade)
- [260: Why was useSemicolonDelimiter changed to false?](#260-why-was-usesemicolondelimiter-changed-to-false)
- [261: Why does req.params no longer have a prototype in v5?](#261-why-does-reqparams-no-longer-have-a-prototype-in-v5)
- [262: How do you use a custom query string parser?](#262-how-do-you-use-a-custom-query-string-parser)
- [263: What does maxParamLength do?](#263-what-does-maxparamlength-do)
- [264: What is rewriteUrl?](#264-what-is-rewriteurl)
- [265: What is frameworkErrors used for?](#265-what-is-frameworkerrors-used-for)
- [266: What is clientErrorHandler?](#266-what-is-clienterrorhandler)
- [267: How do you serve a single-page app and API routes from one Fastify app with fallback?](#267-how-do-you-serve-a-single-page-app-and-api-routes-from-one-fastify-app-with-fallback)
- [268: How do you use different not-found handlers for different prefixes?](#268-how-do-you-use-different-not-found-handlers-for-different-prefixes)
- [269: Can hooks run on the not-found handler?](#269-can-hooks-run-on-the-not-found-handler)
- [270: How do you call the not-found handler from a route?](#270-how-do-you-call-the-not-found-handler-from-a-route)
- [271: How do you register a WebSocket route that requires auth?](#271-how-do-you-register-a-websocket-route-that-requires-auth)
- [272: How do you broadcast a message to all WebSocket clients?](#272-how-do-you-broadcast-a-message-to-all-websocket-clients)
- [273: How do you add OpenAPI security schemes with @fastify/swagger?](#273-how-do-you-add-openapi-security-schemes-with-fastifyswagger)
- [274: How do you make @fastify/swagger use your shared $ref schemas?](#274-how-do-you-make-fastifyswagger-use-your-shared-ref-schemas)
- [275: How do you load env config before other plugins need it?](#275-how-do-you-load-env-config-before-other-plugins-need-it)
- [276: How do you use dependency injection in Fastify?](#276-how-do-you-use-dependency-injection-in-fastify)
- [277: How do you store data per request without passing it around?](#277-how-do-you-store-data-per-request-without-passing-it-around)
- [278: How do you run a database transaction per request?](#278-how-do-you-run-a-database-transaction-per-request)
- [279: How do you add request timing headers for debugging?](#279-how-do-you-add-request-timing-headers-for-debugging)
- [280: How do you write a plugin that works for both v4 and v5?](#280-how-do-you-write-a-plugin-that-works-for-both-v4-and-v5)
- [281: What is the then() method on reply used for?](#281-what-is-the-then-method-on-reply-used-for)
- [282: How do you send HTTP trailers?](#282-how-do-you-send-http-trailers)
- [283: What is reply.writeEarlyHints()?](#283-what-is-replywriteearlyhints)
- [284: How do you check if a header is already set on the reply?](#284-how-do-you-check-if-a-header-is-already-set-on-the-reply)
- [285: How do you add a route with the same handler for GET and POST?](#285-how-do-you-add-a-route-with-the-same-handler-for-get-and-post)
- [286: Why do you get FST_ERR_DUPLICATED_ROUTE?](#286-why-do-you-get-fst_err_duplicated_route)
- [287: How do you get the matched route pattern for metrics?](#287-how-do-you-get-the-matched-route-pattern-for-metrics)
- [288: How do you expose Prometheus metrics?](#288-how-do-you-expose-prometheus-metrics)
- [289: How do you run Fastify in Docker the right way?](#289-how-do-you-run-fastify-in-docker-the-right-way)
- [290: How do you serve compressed static files that are already built?](#290-how-do-you-serve-compressed-static-files-that-are-already-built)
- [291: How do you set different body limits for different content types?](#291-how-do-you-set-different-body-limits-for-different-content-types)
- [292: How do you use the async iterator style with request.files()?](#292-how-do-you-use-the-async-iterator-style-with-requestfiles)
- [293: How do you define a route schema in a separate file?](#293-how-do-you-define-a-route-schema-in-a-separate-file)
- [294: How do you validate that two fields match, like password and confirmPassword?](#294-how-do-you-validate-that-two-fields-match-like-password-and-confirmpassword)
- [295: How do you run code once on startup that needs all plugins loaded?](#295-how-do-you-run-code-once-on-startup-that-needs-all-plugins-loaded)
- [296: How do you send a 201 with a Location header?](#296-how-do-you-send-a-201-with-a-location-header)
- [297: How do you handle errors thrown inside setTimeout in a handler?](#297-how-do-you-handle-errors-thrown-inside-settimeout-in-a-handler)
- [298: How do you implement a simple API key check for a group of routes?](#298-how-do-you-implement-a-simple-api-key-check-for-a-group-of-routes)
- [299: How do you log the request body for debugging only?](#299-how-do-you-log-the-request-body-for-debugging-only)
- [300: How do you handle CORS preflight for a route with custom headers?](#300-how-do-you-handle-cors-preflight-for-a-route-with-custom-headers)

### Advanced Questions (301-450)

- [301: How does Fastify load plugins internally?](#301-how-does-fastify-load-plugins-internally)
- [302: How is encapsulation implemented under the hood?](#302-how-is-encapsulation-implemented-under-the-hood)
- [303: How does fastify-plugin skip encapsulation internally?](#303-how-does-fastify-plugin-skip-encapsulation-internally)
- [304: Why do decorators help performance?](#304-why-do-decorators-help-performance)
- [305: Why can't you decorate request or reply with an object value in v5?](#305-why-cant-you-decorate-request-or-reply-with-an-object-value-in-v5)
- [306: How does find-my-way route matching work?](#306-how-does-find-my-way-route-matching-work)
- [307: Why are regex params slower and what are the risks?](#307-why-are-regex-params-slower-and-what-are-the-risks)
- [308: How does fast-json-stringify make serialization faster?](#308-how-does-fast-json-stringify-make-serialization-faster)
- [309: Are there cases where fast-json-stringify is slower than JSON.stringify?](#309-are-there-cases-where-fast-json-stringify-is-slower-than-jsonstringify)
- [310: How are validation functions compiled and when?](#310-how-are-validation-functions-compiled-and-when)
- [311: How do you reduce startup time caused by schema compilation?](#311-how-do-you-reduce-startup-time-caused-by-schema-compilation)
- [312: What is the schemaController option?](#312-what-is-the-schemacontroller-option)
- [313: How does setValidatorCompiler work?](#313-how-does-setvalidatorcompiler-work)
- [314: How do you use different Ajv settings for body and query string?](#314-how-do-you-use-different-ajv-settings-for-body-and-query-string)
- [315: How do you validate data manually with a route's schema?](#315-how-do-you-validate-data-manually-with-a-routes-schema)
- [316: How do you serialize data manually with a schema?](#316-how-do-you-serialize-data-manually-with-a-schema)
- [317: What is prototype poisoning and how does Fastify protect against it?](#317-what-is-prototype-poisoning-and-how-does-fastify-protect-against-it)
- [318: What security risks come with trustProxy: true?](#318-what-security-risks-come-with-trustproxy-true)
- [319: How can reply.redirect be abused, and how do you prevent it?](#319-how-can-replyredirect-be-abused-and-how-do-you-prevent-it)
- [320: How do you avoid path traversal when serving files?](#320-how-do-you-avoid-path-traversal-when-serving-files)
- [321: Why should you keep Fastify patched, using recent CVEs as an example?](#321-why-should-you-keep-fastify-patched-using-recent-cves-as-an-example)
- [322: How would you design rate limiting for a multi-instance deployment?](#322-how-would-you-design-rate-limiting-for-a-multi-instance-deployment)
- [323: What is handlerTimeout and how is it different from connectionTimeout?](#323-what-is-handlertimeout-and-how-is-it-different-from-connectiontimeout)
- [324: How do you cancel work when a request times out or the client goes away?](#324-how-do-you-cancel-work-when-a-request-times-out-or-the-client-goes-away)
- [325: How do you customize the response when handlerTimeout fires?](#325-how-do-you-customize-the-response-when-handlertimeout-fires)
- [326: How do you find what is blocking the event loop in a Fastify app?](#326-how-do-you-find-what-is-blocking-the-event-loop-in-a-fastify-app)
- [327: How do you benchmark a Fastify route?](#327-how-do-you-benchmark-a-fastify-route)
- [328: How much does logging cost and how do you reduce it?](#328-how-much-does-logging-cost-and-how-do-you-reduce-it)
- [329: What are Pino transports and why do they run in a worker thread?](#329-what-are-pino-transports-and-why-do-they-run-in-a-worker-thread)
- [330: How do you run CPU-heavy work without blocking requests?](#330-how-do-you-run-cpu-heavy-work-without-blocking-requests)
- [331: Should you use Node.js cluster with Fastify?](#331-should-you-use-nodejs-cluster-with-fastify)
- [332: How do you make outgoing HTTP calls efficient from Fastify?](#332-how-do-you-make-outgoing-http-calls-efficient-from-fastify)
- [333: How do you avoid duplicate work when many requests ask for the same data at once?](#333-how-do-you-avoid-duplicate-work-when-many-requests-ask-for-the-same-data-at-once)
- [334: How do you stream a large database result as JSON?](#334-how-do-you-stream-a-large-database-result-as-json)
- [335: How do you upload a large file straight to S3 without storing it on disk?](#335-how-do-you-upload-a-large-file-straight-to-s3-without-storing-it-on-disk)
- [336: How does @fastify/compress interact with streams and onSend hooks?](#336-how-does-fastifycompress-interact-with-streams-and-onsend-hooks)
- [337: What problems can happen with HEAD routes in v5?](#337-what-problems-can-happen-with-head-routes-in-v5)
- [338: What happens when you throw something that is not an Error?](#338-what-happens-when-you-throw-something-that-is-not-an-error)
- [339: What happens if the error handler itself throws?](#339-what-happens-if-the-error-handler-itself-throws)
- [340: How do you make sure no internal details leak in 500 responses?](#340-how-do-you-make-sure-no-internal-details-leak-in-500-responses)
- [341: How do you test that hooks run in the expected order?](#341-how-do-you-test-that-hooks-run-in-the-expected-order)
- [342: How does light-my-request work?](#342-how-does-light-my-request-work)
- [343: When is inject() not enough for testing?](#343-when-is-inject-not-enough-for-testing)
- [344: How do you test a plugin that is wrapped with fastify-plugin?](#344-how-do-you-test-a-plugin-that-is-wrapped-with-fastify-plugin)
- [345: What is Symbol.asyncDispose on the Fastify instance used for?](#345-what-is-symbolasyncdispose-on-the-fastify-instance-used-for)
- [346: What is the diagnostics channel support in Fastify?](#346-what-is-the-diagnostics-channel-support-in-fastify)
- [347: How do you add OpenTelemetry tracing to Fastify?](#347-how-do-you-add-opentelemetry-tracing-to-fastify)
- [348: How do you correlate logs with traces?](#348-how-do-you-correlate-logs-with-traces)
- [349: What does setChildLoggerFactory do?](#349-what-does-setchildloggerfactory-do)
- [350: What does setGenReqId do?](#350-what-does-setgenreqid-do)
- [351: How would you structure a large Fastify app into modules?](#351-how-would-you-structure-a-large-fastify-app-into-modules)
- [352: How do you share code between modules without breaking encapsulation?](#352-how-do-you-share-code-between-modules-without-breaking-encapsulation)
- [353: What is the difference between using decorators and module imports for dependencies?](#353-what-is-the-difference-between-using-decorators-and-module-imports-for-dependencies)
- [354: How would you build a multi-tenant API with Fastify?](#354-how-would-you-build-a-multi-tenant-api-with-fastify)
- [355: How do you implement idempotency keys for POST requests?](#355-how-do-you-implement-idempotency-keys-for-post-requests)
- [356: How do you design background processing triggered by an HTTP request?](#356-how-do-you-design-background-processing-triggered-by-an-http-request)
- [357: How do you make WebSockets work across several Fastify instances?](#357-how-do-you-make-websockets-work-across-several-fastify-instances)
- [358: How would you set up GraphQL on Fastify?](#358-how-would-you-set-up-graphql-on-fastify)
- [359: How does NestJS use Fastify?](#359-how-does-nestjs-use-fastify)
- [360: What is Platformatic and how does it relate to Fastify?](#360-what-is-platformatic-and-how-does-it-relate-to-fastify)
- [361: How do you serve a Vite-based frontend with server-side rendering in Fastify?](#361-how-do-you-serve-a-vite-based-frontend-with-server-side-rendering-in-fastify)
- [362: How would you investigate a memory leak in a Fastify app?](#362-how-would-you-investigate-a-memory-leak-in-a-fastify-app)
- [363: Why should you never call register() or addHook() inside a handler?](#363-why-should-you-never-call-register-or-addhook-inside-a-handler)
- [364: How do you add routes dynamically at runtime?](#364-how-do-you-add-routes-dynamically-at-runtime)
- [365: What happens if a plugin throws during boot?](#365-what-happens-if-a-plugin-throws-during-boot)
- [366: How do you load a plugin only in some environments?](#366-how-do-you-load-a-plugin-only-in-some-environments)
- [367: How would you handle zero-downtime deploys?](#367-how-would-you-handle-zero-downtime-deploys)
- [368: What is the difference between readiness and liveness probes for a Fastify app?](#368-what-is-the-difference-between-readiness-and-liveness-probes-for-a-fastify-app)
- [369: Why can you get 502 errors from a load balancer in front of Fastify?](#369-why-can-you-get-502-errors-from-a-load-balancer-in-front-of-fastify)
- [370: How do you use a custom HTTP server with serverFactory?](#370-how-do-you-use-a-custom-http-server-with-serverfactory)
- [371: How do you run Fastify on AWS Lambda?](#371-how-do-you-run-fastify-on-aws-lambda)
- [372: How do you avoid N+1 queries in Fastify routes?](#372-how-do-you-avoid-n1-queries-in-fastify-routes)
- [373: What is the risk of sharing a DataLoader across requests?](#373-what-is-the-risk-of-sharing-a-dataloader-across-requests)
- [374: How do you limit query string complexity to protect the app?](#374-how-do-you-limit-query-string-complexity-to-protect-the-app)
- [375: How does Fastify handle very large JSON bodies safely?](#375-how-does-fastify-handle-very-large-json-bodies-safely)
- [376: How do you validate a body with a discriminator?](#376-how-do-you-validate-a-body-with-a-discriminator)
- [377: Why is removeAdditional dangerous with anyOf or oneOf?](#377-why-is-removeadditional-dangerous-with-anyof-or-oneof)
- [378: How do you handle nullable fields in schemas?](#378-how-do-you-handle-nullable-fields-in-schemas)
- [379: How are Date objects serialized with a response schema?](#379-how-are-date-objects-serialized-with-a-response-schema)
- [380: How do you send BigInt values in JSON?](#380-how-do-you-send-bigint-values-in-json)
- [381: How does fast-json-stringify handle integers that are floats?](#381-how-does-fast-json-stringify-handle-integers-that-are-floats)
- [382: What happens with circular references in a response?](#382-what-happens-with-circular-references-in-a-response)
- [383: How do response schemas help with security?](#383-how-do-response-schemas-help-with-security)
- [384: How do you return different shapes from one route with response schemas?](#384-how-do-you-return-different-shapes-from-one-route-with-response-schemas)
- [385: How do you handle errors in a custom content type parser?](#385-how-do-you-handle-errors-in-a-custom-content-type-parser)
- [386: How does the content type parser pick a match?](#386-how-does-the-content-type-parser-pick-a-match)
- [387: How do you add an async content type parser?](#387-how-do-you-add-an-async-content-type-parser)
- [388: How do you handle the request body as a stream in a route?](#388-how-do-you-handle-the-request-body-as-a-stream-in-a-route)
- [389: How do you write a custom route constraint that is async?](#389-how-do-you-write-a-custom-route-constraint-that-is-async)
- [390: How would you build API versioning for a large API?](#390-how-would-you-build-api-versioning-for-a-large-api)
- [391: How do you prevent duplicate routes when composing route plugins?](#391-how-do-you-prevent-duplicate-routes-when-composing-route-plugins)
- [392: How do you enforce that every route has a response schema?](#392-how-do-you-enforce-that-every-route-has-a-response-schema)
- [393: How do you add default options to every route?](#393-how-do-you-add-default-options-to-every-route)
- [394: How do you share a hook across routes but skip it for some?](#394-how-do-you-share-a-hook-across-routes-but-skip-it-for-some)
- [395: Why are hooks with closures over the request a common source of leaks?](#395-why-are-hooks-with-closures-over-the-request-a-common-source-of-leaks)
- [396: How would you implement a circuit breaker for a downstream service?](#396-how-would-you-implement-a-circuit-breaker-for-a-downstream-service)
- [397: How do you protect the server when a downstream dependency is slow?](#397-how-do-you-protect-the-server-when-a-downstream-dependency-is-slow)
- [398: How does @fastify/under-pressure decide when to return 503?](#398-how-does-fastifyunder-pressure-decide-when-to-return-503)
- [399: How do you implement a secure file download with access checks?](#399-how-do-you-implement-a-secure-file-download-with-access-checks)
- [400: How do you prevent header injection when setting headers from user input?](#400-how-do-you-prevent-header-injection-when-setting-headers-from-user-input)
- [401: How do you safely store passwords in a Fastify app?](#401-how-do-you-safely-store-passwords-in-a-fastify-app)
- [402: How do you implement JWT refresh tokens with Fastify?](#402-how-do-you-implement-jwt-refresh-tokens-with-fastify)
- [403: What are the risks of using HS256 JWTs across services?](#403-what-are-the-risks-of-using-hs256-jwts-across-services)
- [404: How do you lock down which algorithms @fastify/jwt accepts?](#404-how-do-you-lock-down-which-algorithms-fastifyjwt-accepts)
- [405: How do you secure cookies properly?](#405-how-do-you-secure-cookies-properly)
- [406: How do you rotate cookie or session secrets without logging everyone out?](#406-how-do-you-rotate-cookie-or-session-secrets-without-logging-everyone-out)
- [407: What is a good Content Security Policy setup with @fastify/helmet?](#407-what-is-a-good-content-security-policy-setup-with-fastifyhelmet)
- [408: How do you enforce HTTPS behind a load balancer?](#408-how-do-you-enforce-https-behind-a-load-balancer)
- [409: How do you validate the Host header to prevent host header attacks?](#409-how-do-you-validate-the-host-header-to-prevent-host-header-attacks)
- [410: How would you audit a Fastify app for security issues?](#410-how-would-you-audit-a-fastify-app-for-security-issues)
- [411: How do you write a reusable plugin that adds hooks only to routes that opt in?](#411-how-do-you-write-a-reusable-plugin-that-adds-hooks-only-to-routes-that-opt-in)
- [412: How do you make a plugin's options type-safe and validated at boot?](#412-how-do-you-make-a-plugins-options-type-safe-and-validated-at-boot)
- [413: How do you publish a plugin to npm the right way?](#413-how-do-you-publish-a-plugin-to-npm-the-right-way)
- [414: Why can two copies of Fastify in node_modules cause problems?](#414-why-can-two-copies-of-fastify-in-node_modules-cause-problems)
- [415: How does TypeScript inference work with type providers internally?](#415-how-does-typescript-inference-work-with-type-providers-internally)
- [416: How do you type the reply so TypeScript checks what you return?](#416-how-do-you-type-the-reply-so-typescript-checks-what-you-return)
- [417: How do you type handlers defined in separate files?](#417-how-do-you-type-handlers-defined-in-separate-files)
- [418: How do you type a decorator that only exists in an encapsulated context?](#418-how-do-you-type-a-decorator-that-only-exists-in-an-encapsulated-context)
- [419: How do you handle errors in TypeScript with proper types?](#419-how-do-you-handle-errors-in-typescript-with-proper-types)
- [420: What is the difference between FastifyPluginAsync and FastifyPluginCallback?](#420-what-is-the-difference-between-fastifypluginasync-and-fastifyplugincallback)
- [421: How would you approach performance tuning of a slow endpoint step by step?](#421-how-would-you-approach-performance-tuning-of-a-slow-endpoint-step-by-step)
- [422: When is a response schema not worth it for performance?](#422-when-is-a-response-schema-not-worth-it-for-performance)
- [423: How do you choose between sync and async handlers for performance?](#423-how-do-you-choose-between-sync-and-async-handlers-for-performance)
- [424: How does Fastify handle request pipelining and keep-alive?](#424-how-does-fastify-handle-request-pipelining-and-keep-alive)
- [425: How do you spread load when clients keep long-lived keep-alive connections?](#425-how-do-you-spread-load-when-clients-keep-long-lived-keep-alive-connections)
- [426: How do you design a plugin that needs async setup and a clean shutdown?](#426-how-do-you-design-a-plugin-that-needs-async-setup-and-a-clean-shutdown)
- [427: How do you avoid a slow plugin from delaying startup too much?](#427-how-do-you-avoid-a-slow-plugin-from-delaying-startup-too-much)
- [428: What happens to in-flight requests when a hook rejects after the handler started?](#428-what-happens-to-in-flight-requests-when-a-hook-rejects-after-the-handler-started)
- [429: How do you handle a client that disconnects in the middle of a long stream?](#429-how-do-you-handle-a-client-that-disconnects-in-the-middle-of-a-long-stream)
- [430: How would you implement server-side caching of whole responses?](#430-how-would-you-implement-server-side-caching-of-whole-responses)
- [431: How do you support both JSON and protobuf on the same endpoint?](#431-how-do-you-support-both-json-and-protobuf-on-the-same-endpoint)
- [432: How do you build an API gateway on Fastify?](#432-how-do-you-build-an-api-gateway-on-fastify)
- [433: How do you ensure correct behavior when the same plugin is registered in two places?](#433-how-do-you-ensure-correct-behavior-when-the-same-plugin-is-registered-in-two-places)
- [434: What are the trade-offs of @fastify/autoload in a big project?](#434-what-are-the-trade-offs-of-fastifyautoload-in-a-big-project)
- [435: How do you bundle a Fastify app with esbuild or similar?](#435-how-do-you-bundle-a-fastify-app-with-esbuild-or-similar)
- [436: How do you migrate a large Express codebase where middleware depends on req and res mutations?](#436-how-do-you-migrate-a-large-express-codebase-where-middleware-depends-on-req-and-res-mutations)
- [437: How do you run Express and Fastify side by side during a migration without @fastify/express?](#437-how-do-you-run-express-and-fastify-side-by-side-during-a-migration-without-fastifyexpress)
- [438: How do you implement request signing verification as a reusable plugin?](#438-how-do-you-implement-request-signing-verification-as-a-reusable-plugin)
- [439: How do you handle very high cardinality logging fields without hurting performance?](#439-how-do-you-handle-very-high-cardinality-logging-fields-without-hurting-performance)
- [440: What happens to hooks and the handler when you call reply.hijack() in onRequest?](#440-what-happens-to-hooks-and-the-handler-when-you-call-replyhijack-in-onrequest)
- [441: How do you test error handling for errors thrown in hooks, handlers and serialization?](#441-how-do-you-test-error-handling-for-errors-thrown-in-hooks-handlers-and-serialization)
- [442: How would you design a plugin system for third-party extensions in your own Fastify product?](#442-how-would-you-design-a-plugin-system-for-third-party-extensions-in-your-own-fastify-product)
- [443: Is encapsulation a security boundary?](#443-is-encapsulation-a-security-boundary)
- [444: How do you handle schema evolution without breaking clients?](#444-how-do-you-handle-schema-evolution-without-breaking-clients)
- [445: How do you generate client types from a Fastify API?](#445-how-do-you-generate-client-types-from-a-fastify-api)
- [446: How do you handle timezone and date formats in v5 validation?](#446-how-do-you-handle-timezone-and-date-formats-in-v5-validation)
- [447: What are the risks of setting requestIdHeader in a public API?](#447-what-are-the-risks-of-setting-requestidheader-in-a-public-api)
- [448: How do you debug a request that hangs and never responds?](#448-how-do-you-debug-a-request-that-hangs-and-never-responds)
- [449: What should you check before upgrading to a new Fastify major version, such as v6?](#449-what-should-you-check-before-upgrading-to-a-new-fastify-major-version-such-as-v6)
- [450: If you had to explain why a team should choose Fastify for a new API, what would you say?](#450-if-you-had-to-explain-why-a-team-should-choose-fastify-for-a-new-api-what-would-you-say)

---

# Easy Questions (1-150)

## 1: What is Fastify?

Fastify is a web framework for Node.js focused on speed and low overhead. You use it to build HTTP APIs and web servers, the same kind of work you would do with Express.

Its main ideas are:

- A plugin system where everything (routes, database clients, auth) is a plugin
- JSON Schema for validating requests and serializing responses
- Hooks to run code at each step of the request lifecycle
- Built-in logging with Pino
- Good TypeScript support

It is maintained by the Fastify team and is part of the OpenJS Foundation.

## 2: Why is Fastify called fast?

A few design choices make it fast:

- Routing uses `find-my-way`, a radix tree router that is much faster than looping over a list of regular expressions.
- Responses with a schema are serialized with `fast-json-stringify`, which compiles a serializer function from the schema. This is faster than `JSON.stringify`.
- Validation uses Ajv, which compiles schemas to plain JavaScript functions once at startup.
- The logger, Pino, is one of the fastest JSON loggers for Node.js.
- The core is small and avoids extra work per request.

In benchmarks Fastify usually handles several times more requests per second than Express on the same hardware.

## 3: How do you install Fastify and create a basic server?

Install it with npm:

```bash
npm install fastify
```

Then create a server:

```js
import Fastify from "fastify";

const app = Fastify({ logger: true });

app.get("/", async () => {
  return { hello: "world" };
});

await app.listen({ port: 3000 });
```

Run it with `node server.js` (with `"type": "module"` in `package.json` for ESM) and open `http://localhost:3000`.

## 4: Which Node.js version does Fastify v5 need?

Fastify v5 needs Node.js 20 or newer. Node.js 18 support was dropped in v5. If you are stuck on an older Node.js version you have to stay on Fastify v4, but v4 is out of support since June 2025, so upgrading Node.js is the better path.

## 5: How do you start the server with listen()?

`listen()` takes an options object and returns a promise:

```js
await app.listen({ port: 3000, host: "0.0.0.0" });
```

Common options are `port`, `host`, `path` (for a Unix socket) and `backlog`. In v5 the old style `app.listen(3000)` with positional arguments was removed, so you must pass an object.

You can also pass a callback instead of awaiting:

```js
app.listen({ port: 3000 }, (err, address) => {
  if (err) {
    app.log.error(err);
    process.exit(1);
  }
});
```

## 6: Why does the default host matter when running Fastify in Docker?

By default Fastify listens on `localhost`, which means it only accepts connections from inside the same machine or container. In Docker, traffic comes from outside the container, so requests never reach the app.

Set the host to `0.0.0.0` (or `::` for IPv6) to listen on all interfaces:

```js
await app.listen({ port: 3000, host: "0.0.0.0" });
```

## 7: How do you define a GET route?

Use the shorthand method `app.get(path, [options], handler)`:

```js
app.get("/users", async (request, reply) => {
  return [{ id: 1, name: "Ana" }];
});
```

There are shorthand methods for all common verbs: `get`, `post`, `put`, `patch`, `delete`, `head`, `options` and `all`.

## 8: What is the full route declaration with app.route()?

`app.route()` takes one object with all route settings. The shorthand methods are just wrappers around it.

```js
app.route({
  method: "GET",
  url: "/users/:id",
  schema: {
    params: {
      type: "object",
      properties: { id: { type: "integer" } },
    },
  },
  handler: async (request) => {
    return { id: request.params.id };
  },
});
```

`method` can also be an array, for example `['GET', 'HEAD']`.

## 9: What are the request and reply objects?

Every handler receives two arguments:

- `request` is Fastify's wrapper around the Node.js `IncomingMessage`. It has `params`, `query`, `body`, `headers`, `id`, `log`, `ip` and more.
- `reply` is Fastify's wrapper around the Node.js `ServerResponse`. You use it to set the status code, headers and send the response.

The raw Node.js objects are still available as `request.raw` and `reply.raw`, but you should rarely need them.

## 10: How do you read route params?

Define a param with a colon in the path and read it from `request.params`:

```js
app.get("/posts/:postId/comments/:commentId", async (request) => {
  const { postId, commentId } = request.params;
  return { postId, commentId };
});
```

Params are strings unless you add a schema with a number or integer type. Then Ajv converts them for you.

## 11: How do you read query string values?

Use `request.query`:

```js
// GET /search?term=fastify&page=2
app.get("/search", async (request) => {
  const { term, page } = request.query;
  return { term, page };
});
```

Without a schema, every value is a string. With a querystring schema you get type coercion, defaults and validation.

## 12: How do you read the request body?

Use `request.body`. Fastify parses JSON and plain text bodies by default:

```js
app.post("/users", async (request, reply) => {
  const { name, email } = request.body;
  reply.code(201);
  return { name, email };
});
```

Other content types like `application/x-www-form-urlencoded` or `multipart/form-data` need a plugin (`@fastify/formbody` and `@fastify/multipart`) or a custom content type parser.

## 13: Which content types does Fastify parse out of the box?

Only two:

- `application/json`
- `text/plain`

If a request comes with another content type and there is no parser for it, Fastify returns `415 Unsupported Media Type`.

## 14: How do you send a response?

You have two options.

Return a value from an async handler:

```js
app.get("/", async () => ({ ok: true }));
```

Or call `reply.send()`:

```js
app.get("/", (request, reply) => {
  reply.send({ ok: true });
});
```

Objects are serialized to JSON, strings are sent as text, and buffers and streams are sent as they are.

## 15: How do you set the status code?

Use `reply.code()` (or its alias `reply.status()`):

```js
app.post("/items", async (request, reply) => {
  const item = await createItem(request.body);
  reply.code(201);
  return item;
});
```

The default status code is 200.

## 16: How do you set response headers?

Use `reply.header()` for one header or `reply.headers()` for several:

```js
app.get("/file", async (request, reply) => {
  reply
    .header("Cache-Control", "no-store")
    .headers({ "X-Request-Id": request.id, "X-Version": "1" });
  return { ok: true };
});
```

`reply.type('text/html')` is a shortcut for setting `Content-Type`.

## 17: How do you read request headers?

Use `request.headers`. Header names are always lowercase because Node.js lowercases them:

```js
app.get("/me", async (request) => {
  const auth = request.headers.authorization;
  const agent = request.headers["user-agent"];
  return { auth, agent };
});
```

## 18: How do you redirect in Fastify?

Use `reply.redirect(url, [code])`. The default status is 302:

```js
app.get("/old", async (request, reply) => {
  return reply.redirect("/new", 301);
});
```

In v4 the code came first (`reply.redirect(301, '/new')`). v5 changed the order, so the URL is always first.

## 19: What is a plugin in Fastify?

A plugin is a function that receives a Fastify instance and options, and adds things to it: routes, hooks, decorators or other plugins.

```js
async function usersRoutes(app, opts) {
  app.get("/users", async () => []);
  app.post("/users", async (request) => request.body);
}

app.register(usersRoutes, { prefix: "/api" });
```

In Fastify almost everything is a plugin. This is how you split a large app into small parts.

## 20: What does app.register() do?

`register()` loads a plugin. Fastify creates a new child context (a new encapsulated instance) for the plugin and calls the plugin function with it. Plugins are loaded in the order they are registered, and loading happens asynchronously when you call `listen()`, `ready()` or `await` the register call.

```js
app.register(import("./routes/users.js"), { prefix: "/users" });
```

## 21: How do you add a prefix to all routes in a plugin?

Pass `prefix` in the register options:

```js
app.register(
  async (app) => {
    app.get("/", async () => "list"); // GET /v1/users
    app.get("/:id", async () => "one"); // GET /v1/users/:id
  },
  { prefix: "/v1/users" },
);
```

Prefixes stack. If a plugin with prefix `/v1` registers another plugin with prefix `/users`, the routes inside end up under `/v1/users`.

## 22: What is encapsulation in Fastify?

Encapsulation means each plugin gets its own child context. Anything a plugin adds (decorators, hooks, content type parsers, error handlers) is visible to that plugin and its children, but not to its parent or siblings.

```js
app.register(async (child) => {
  child.decorate("secret", 42);
  child.get("/a", async () => child.secret); // works
});

app.get("/b", async () => app.secret); // undefined, the parent cannot see it
```

This keeps plugins isolated, so one part of the app cannot accidentally break another.

## 23: What is fastify-plugin used for?

`fastify-plugin` wraps a plugin so it skips encapsulation. Whatever the plugin adds is attached to the parent context, so siblings and the parent can use it.

```js
import fp from "fastify-plugin";

async function dbPlugin(app) {
  app.decorate("db", createDbClient());
}

export default fp(dbPlugin, { name: "db" });
```

Use it for shared things like a database client, config or auth helpers. Do not use it for route plugins, since you usually want those encapsulated.

## 24: What is a decorator?

A decorator adds a custom property or method to the Fastify instance, the request or the reply:

```js
app.decorate("config", { env: "prod" });
app.decorateRequest("user", null);
app.decorateReply("sendOk", function () {
  return this.send({ ok: true });
});
```

Decorators are the supported way to extend Fastify objects. Using them instead of adding properties at random keeps object shapes stable, which helps V8 optimize the code.

## 25: What is the difference between decorate, decorateRequest and decorateReply?

- `decorate` adds to the Fastify instance (`app.db`, `app.config`).
- `decorateRequest` adds to every request object (`request.user`).
- `decorateReply` adds to every reply object (`reply.sendError()`).

All three follow encapsulation rules unless the plugin is wrapped with `fastify-plugin`.

## 26: What are hooks in Fastify?

Hooks let you run code at specific points of the request lifecycle or the app lifecycle. You add them with `app.addHook()`:

```js
app.addHook("onRequest", async (request, reply) => {
  request.log.info("got a request");
});
```

Request hooks include `onRequest`, `preParsing`, `preValidation`, `preHandler`, `preSerialization`, `onSend`, `onResponse`, `onError`, `onTimeout` and `onRequestAbort`. App hooks include `onReady`, `onListen`, `preClose`, `onClose`, `onRoute` and `onRegister`.

## 27: What is the onRequest hook used for?

`onRequest` is the first hook in the request lifecycle. It runs before the body is parsed, so `request.body` is always `undefined` here.

It is a good place for cheap checks that do not need the body: checking an API key or token, rate limiting, or adding request timing.

```js
app.addHook("onRequest", async (request, reply) => {
  if (!request.headers["x-api-key"]) {
    return reply.code(401).send({ error: "Missing API key" });
  }
});
```

## 28: What is the preHandler hook used for?

`preHandler` runs right before the route handler, after the body is parsed and validated. Use it when you need the validated body or params, for example to load a resource and check that the user owns it.

```js
app.addHook("preHandler", async (request, reply) => {
  request.log.info({ body: request.body }, "about to handle");
});
```

## 29: What is the onResponse hook used for?

`onResponse` runs after the response has been sent to the client. You cannot change the response anymore. It is used for logging, metrics and cleanup.

```js
app.addHook("onResponse", async (request, reply) => {
  request.log.info({ ms: reply.elapsedTime }, "done");
});
```

## 30: How does logging work in Fastify?

Fastify uses Pino. Turn it on with `logger: true`:

```js
const app = Fastify({ logger: true });

app.get("/", async (request) => {
  request.log.info("handling /");
  return "ok";
});
```

`app.log` is the app logger. `request.log` is a child logger that adds the request ID to every line, so you can trace all logs of one request. Logs are JSON by default.

## 31: How do you set the log level?

Pass an object to `logger`:

```js
const app = Fastify({
  logger: { level: "warn" },
});
```

Levels from lowest to highest are `trace`, `debug`, `info`, `warn`, `error` and `fatal`. You can also set a log level per route with the `logLevel` route option or per plugin in the register options.

## 32: How do you get pretty logs during development?

Install `pino-pretty` and use it as a transport:

```js
const app = Fastify({
  logger: {
    transport: {
      target: "pino-pretty",
      options: { translateTime: "HH:MM:ss", ignore: "pid,hostname" },
    },
  },
});
```

Do not use it in production. JSON logs are faster and easier for log tools to parse. You can also pipe output instead: `node server.js | pino-pretty`.

## 33: What is JSON Schema used for in Fastify?

Fastify uses JSON Schema for two things:

1. **Validation** of incoming data: body, querystring, params and headers. Invalid requests get a 400 response before the handler runs.
2. **Serialization** of outgoing data. With a response schema, Fastify uses `fast-json-stringify` to turn objects into JSON faster, and only fields listed in the schema are sent.

The same schemas can also generate OpenAPI docs with `@fastify/swagger`.

## 34: How do you validate a request body?

Add a `body` schema to the route:

```js
app.post(
  "/users",
  {
    schema: {
      body: {
        type: "object",
        required: ["email", "name"],
        properties: {
          email: { type: "string", format: "email" },
          name: { type: "string", minLength: 1 },
          age: { type: "integer", minimum: 0 },
        },
      },
    },
  },
  async (request) => {
    return request.body;
  },
);
```

If the body does not match, Fastify replies with 400 and a message describing the problem.

## 35: What does a validation error response look like?

By default Fastify returns a 400 with a JSON body like this:

```json
{
  "statusCode": 400,
  "code": "FST_ERR_VALIDATION",
  "error": "Bad Request",
  "message": "body must have required property 'email'"
}
```

You can change the message format with `schemaErrorFormatter` or handle validation errors yourself in a custom error handler.

## 36: How do you validate query strings and params?

Use `querystring` and `params` in the schema:

```js
app.get(
  "/products/:id",
  {
    schema: {
      params: {
        type: "object",
        properties: { id: { type: "integer" } },
        required: ["id"],
      },
      querystring: {
        type: "object",
        properties: {
          fields: { type: "string" },
          limit: { type: "integer", default: 10, maximum: 100 },
        },
      },
    },
  },
  async (request) => {
    return { id: request.params.id, limit: request.query.limit };
  },
);
```

Thanks to type coercion, `id` and `limit` arrive as numbers, not strings.

## 37: How do you validate request headers?

Use the `headers` schema. Header names in the schema should be lowercase:

```js
app.get(
  "/secure",
  {
    schema: {
      headers: {
        type: "object",
        properties: { "x-api-key": { type: "string", minLength: 10 } },
        required: ["x-api-key"],
      },
    },
  },
  async () => "ok",
);
```

## 38: Why must schemas be full JSON Schemas in v5?

In v4 you could write a shorthand like `querystring: { name: { type: 'string' } }` and Fastify wrapped it in an object schema for you (the `jsonShorthand` option). v5 removed this. Now `body`, `querystring`, `params`, `headers` and `response` schemas must be complete, with `type: 'object'` and `properties`.

```js
// v5
querystring: {
  type: 'object',
  properties: { name: { type: 'string' } }
}
```

## 39: What is a response schema?

A response schema describes what the route sends back, per status code:

```js
app.get(
  "/users/:id",
  {
    schema: {
      response: {
        200: {
          type: "object",
          properties: {
            id: { type: "integer" },
            name: { type: "string" },
          },
        },
      },
    },
  },
  async () => {
    return { id: 1, name: "Ana", passwordHash: "abc" };
  },
);
```

The client receives only `id` and `name`. `passwordHash` is dropped because it is not in the schema. Serialization is also faster.

## 40: Can a response schema use status code ranges?

Yes. You can use `2xx`, `4xx` and so on, or `default`:

```js
schema: {
  response: {
    '2xx': { type: 'object', properties: { data: { type: 'array' } } },
    '4xx': {
      type: 'object',
      properties: { message: { type: 'string' } }
    }
  }
}
```

An exact code like `201` wins over `2xx`, and `2xx` wins over `default`.

## 41: How does error handling work in an async handler?

If an async handler throws, or a returned promise rejects, Fastify catches it and sends an error response:

```js
app.get("/fail", async () => {
  throw new Error("Something broke");
});
```

The client gets a 500 with a JSON body. If the error has a `statusCode` property (for example 404), Fastify uses that status instead.

## 42: How do you return a 404 for a missing resource?

Set the code and return, or throw an error with a `statusCode`:

```js
app.get("/users/:id", async (request, reply) => {
  const user = await findUser(request.params.id);
  if (!user) {
    return reply.code(404).send({ message: "User not found" });
  }
  return user;
});
```

With `@fastify/sensible` you can write `throw app.httpErrors.notFound('User not found')`.

## 43: What is setErrorHandler?

`setErrorHandler` sets a custom function that handles errors for all routes in the current context:

```js
app.setErrorHandler((error, request, reply) => {
  request.log.error(error);
  const status = error.statusCode ?? 500;
  reply.code(status).send({
    message: status === 500 ? "Internal Server Error" : error.message,
  });
});
```

It catches errors from handlers, hooks and validation. Because of encapsulation, a plugin can set its own error handler that only applies to its routes.

## 44: What is setNotFoundHandler?

It sets the handler used when no route matches the URL:

```js
app.setNotFoundHandler((request, reply) => {
  reply
    .code(404)
    .send({ message: `Route ${request.method} ${request.url} not found` });
});
```

You can set different not-found handlers per prefix by calling it inside plugins with a prefix.

## 45: What does Fastify return when a route does not exist?

By default it returns a 404 with a JSON body:

```json
{
  "message": "Route GET:/nope not found",
  "error": "Not Found",
  "statusCode": 404
}
```

## 46: What is app.inject()?

`app.inject()` sends a fake HTTP request to your app without starting a real server. It uses `light-my-request` under the hood. It is the standard way to test Fastify apps.

```js
const res = await app.inject({
  method: "GET",
  url: "/users/1",
});

console.log(res.statusCode); // 200
console.log(res.json()); // parsed body
```

It is fast because no network socket is used.

## 47: How do you write a simple test for a Fastify route?

Build the app, then use `inject()` with any test runner. Here with the Node.js built-in test runner:

```js
import { test } from "node:test";
import assert from "node:assert";
import Fastify from "fastify";

function build() {
  const app = Fastify();
  app.get("/ping", async () => ({ pong: true }));
  return app;
}

test("GET /ping", async (t) => {
  const app = build();
  t.after(() => app.close());

  const res = await app.inject({ method: "GET", url: "/ping" });
  assert.strictEqual(res.statusCode, 200);
  assert.deepStrictEqual(res.json(), { pong: true });
});
```

## 48: What does app.ready() do?

`ready()` loads all registered plugins and runs `onReady` hooks, but does not start listening. It returns a promise.

```js
await app.ready();
```

You use it in tests or when you need everything loaded before doing something, like printing routes. `listen()` and `inject()` call `ready()` for you.

## 49: How do you stop a Fastify server?

Call `app.close()`. It stops accepting new connections, waits for in-flight requests and runs `preClose` and `onClose` hooks:

```js
await app.close();
```

Plugins use `onClose` to close database connections and other resources.

## 50: What is app.after()?

`after()` runs a callback (or resolves a promise) once the plugins registered before it are loaded:

```js
app.register(dbPlugin);

await app.after();
// dbPlugin is loaded here, so app.db exists
```

In most code you do not need it, because Fastify loads plugins in order anyway. It is useful when you need to use something a previous plugin added at the top level.

## 51: How do you serve static files?

Use `@fastify/static`:

```js
import path from "node:path";
import fastifyStatic from "@fastify/static";

app.register(fastifyStatic, {
  root: path.join(import.meta.dirname, "public"),
  prefix: "/public/",
});
```

Now `public/logo.png` is served at `/public/logo.png`. You can also call `reply.sendFile('file.html')` from a handler.

## 52: How do you enable CORS?

Use `@fastify/cors`:

```js
import cors from "@fastify/cors";

await app.register(cors, {
  origin: ["https://myapp.com"],
  credentials: true,
});
```

`origin` can be a string, an array, a regular expression, `true` (reflect the request origin) or a function. Avoid `origin: true` together with `credentials: true` in production unless you really mean to allow any site.

## 53: How do you add security headers?

Use `@fastify/helmet`, which sets headers like `Content-Security-Policy`, `X-Content-Type-Options`, `Strict-Transport-Security` and others:

```js
import helmet from "@fastify/helmet";

await app.register(helmet);
```

You can turn off or change any header through options, for example `contentSecurityPolicy: false` for an API that does not serve HTML.

## 54: How do you parse form data (urlencoded)?

Register `@fastify/formbody`:

```js
import formbody from "@fastify/formbody";

app.register(formbody);

app.post("/login", async (request) => {
  const { username, password } = request.body;
  return { username };
});
```

It adds a parser for `application/x-www-form-urlencoded`.

## 55: How do you handle file uploads?

Use `@fastify/multipart`:

```js
import multipart from "@fastify/multipart";
import { pipeline } from "node:stream/promises";
import fs from "node:fs";

app.register(multipart, { limits: { fileSize: 10 * 1024 * 1024 } });

app.post("/upload", async (request) => {
  const data = await request.file();
  await pipeline(data.file, fs.createWriteStream(`./uploads/${data.filename}`));
  return { uploaded: data.filename };
});
```

`request.file()` gives you the first file as a stream. Use `request.files()` to loop over several files. Never trust `data.filename` as is in real code, since it comes from the client.

## 56: How do you work with cookies?

Use `@fastify/cookie`:

```js
import cookie from "@fastify/cookie";

app.register(cookie, { secret: process.env.COOKIE_SECRET });

app.get("/set", async (request, reply) => {
  reply.setCookie("theme", "dark", { path: "/", httpOnly: true, signed: true });
  return "set";
});

app.get("/read", async (request) => {
  const result = request.unsignCookie(request.cookies.theme);
  return { valid: result.valid, value: result.value };
});
```

## 57: How do you add JWT authentication?

Use `@fastify/jwt`:

```js
import jwt from "@fastify/jwt";

app.register(jwt, { secret: process.env.JWT_SECRET });

app.post("/login", async (request) => {
  const token = app.jwt.sign({ sub: "user-1" }, { expiresIn: "15m" });
  return { token };
});

app.get(
  "/profile",
  {
    onRequest: async (request) => {
      await request.jwtVerify();
    },
  },
  async (request) => {
    return request.user;
  },
);
```

`request.jwtVerify()` throws a 401 error if the token is missing or invalid.

## 58: What is @fastify/sensible?

It adds common helpers:

- `app.httpErrors` and `reply.notFound()`, `reply.badRequest()` and similar for creating HTTP errors
- `app.assert()` for throwing an HTTP error if a condition is false
- `request.forwarded()`, `request.is()`, `reply.vary()` and cache helpers
- `app.to()` for promise error handling without try/catch

```js
import sensible from "@fastify/sensible";

app.register(sensible);

app.get("/item/:id", async (request) => {
  const item = await getItem(request.params.id);
  if (!item) throw app.httpErrors.notFound("Item not found");
  return item;
});
```

## 59: Can you use callbacks instead of async/await in handlers?

Yes. A sync handler gets `request` and `reply` and calls `reply.send()`:

```js
app.get("/", (request, reply) => {
  reply.send({ hello: "world" });
});
```

For async work in this style you must remember to call `reply.send()` in every branch, including errors. Most new code uses async handlers because they are simpler.

## 60: Should you both return a value and call reply.send() in an async handler?

No. Pick one. If you call `reply.send()` inside an async handler, return the `reply` object (or `await reply`) so Fastify knows the response is handled:

```js
app.get("/", async (request, reply) => {
  reply.send({ ok: true });
  return reply;
});
```

If you call `reply.send()` and also return a different value, Fastify logs a warning about the reply being already sent.

## 61: What happens if an async handler returns undefined?

If an async handler returns `undefined` and did not call `reply.send()`, Fastify logs an error saying the promise resolved with undefined and the request may hang. A request should end with either a returned value or `reply.send()`.

If you really want an empty body, use `reply.code(204).send()`.

## 62: How do you send an empty response with 204?

```js
app.delete("/users/:id", async (request, reply) => {
  await deleteUser(request.params.id);
  return reply.code(204).send();
});
```

204 means "No Content", so the body must be empty.

## 63: How do you send HTML?

Set the content type and send a string:

```js
app.get("/", async (request, reply) => {
  reply.type("text/html");
  return "<h1>Hello</h1>";
});
```

For real templates use `@fastify/view` with an engine like EJS, Handlebars, Pug or Eta.

## 64: How do you render templates?

Use `@fastify/view`:

```js
import view from "@fastify/view";
import ejs from "ejs";

app.register(view, {
  engine: { ejs },
  root: "./views",
});

app.get("/", async (request, reply) => {
  return reply.view("index.ejs", { title: "Home" });
});
```

## 65: What is request.id?

Every request gets an ID, available as `request.id`. It is also added to every log line from `request.log`, which makes tracing easy.

By default IDs are increasing numbers like `req-1`, `req-2`. You can change how IDs are made with the `genReqId` option, or read them from a header with `requestIdHeader`.

## 66: How do you get the client IP address?

Use `request.ip`:

```js
app.get("/ip", async (request) => ({ ip: request.ip }));
```

If your app runs behind a proxy or load balancer, set `trustProxy` so Fastify reads the IP from the `X-Forwarded-For` header. Otherwise you get the proxy's IP.

## 67: What other useful properties does the request object have?

Some common ones:

- `request.method` and `request.url`
- `request.hostname`, `request.host` and `request.port`
- `request.protocol` (`http` or `https`)
- `request.ips` (all IPs from `X-Forwarded-For` when `trustProxy` is set)
- `request.routeOptions` (the matched route's url, method, config, schema)
- `request.server` (the Fastify instance)
- `request.socket` (the raw socket)

## 68: What is the difference between request.hostname and request.host in v5?

In v5:

- `request.host` is the host including the port, for example `example.com:3000`.
- `request.hostname` is the host without the port, `example.com`.
- `request.port` is the port, `3000`.

In v4, `request.hostname` included the port. This is a breaking change to watch out for when upgrading.

## 69: What is the default body size limit?

1 MiB (1048576 bytes). Bigger bodies get a `413 Payload Too Large`. You can change it for the whole app or per route:

```js
const app = Fastify({ bodyLimit: 5 * 1024 * 1024 });

app.post("/big", { bodyLimit: 50 * 1024 * 1024 }, async () => "ok");
```

## 70: What does printRoutes() do?

It prints a tree of all registered routes. Call it after the app is ready:

```js
await app.ready();
console.log(app.printRoutes());
```

Output looks like:

```
└── /
    ├── users (GET, HEAD, POST)
    │   └── /:id (GET, HEAD, DELETE)
    └── health (GET, HEAD)
```

It is handy for debugging missing routes or wrong prefixes.

## 71: Why do GET routes also respond to HEAD?

The `exposeHeadRoutes` option is `true` by default. For every GET route, Fastify creates a matching HEAD route that returns the same headers with no body. You can turn it off globally or per route with `exposeHeadRoutes: false`.

## 72: How do you match any route with a wildcard?

Use `*`:

```js
app.get("/files/*", async (request) => {
  return { path: request.params["*"] };
});
```

A request to `/files/a/b/c.txt` gives `{ path: 'a/b/c.txt' }`.

## 73: How do you make a route param optional?

Add `?` after the last param:

```js
app.get("/posts/:id?", async (request) => {
  return request.params.id ? `post ${request.params.id}` : "all posts";
});
```

Only the last param of a path can be optional.

## 74: Can you use regular expressions in route params?

Yes, put the regex in parentheses after the param name:

```js
app.get("/orders/:id(^\\d+)", async (request) => {
  return { id: request.params.id };
});
```

`/orders/123` matches and `/orders/abc` does not. Regex routes are slower than plain params, so use them only when needed. A schema with `type: 'integer'` is often a better choice.

## 75: How does Fastify handle trailing slashes?

By default `/users` and `/users/` are different routes. To treat them the same, set `ignoreTrailingSlash` inside `routerOptions`:

```js
const app = Fastify({
  routerOptions: { ignoreTrailingSlash: true },
});
```

There is also `ignoreDuplicateSlashes` to treat `//users` as `/users`.

## 76: Are routes case sensitive?

Yes, by default `/Users` and `/users` are different. You can change this with `routerOptions: { caseSensitive: false }`. Param values keep their original case either way.

## 77: What is @fastify/autoload?

It loads plugins and routes from folders automatically, so you do not have to register every file by hand:

```js
import autoload from "@fastify/autoload";
import path from "node:path";

app.register(autoload, {
  dir: path.join(import.meta.dirname, "plugins"),
});

app.register(autoload, {
  dir: path.join(import.meta.dirname, "routes"),
});
```

In the `routes` folder, the folder structure becomes the URL prefix. For example `routes/users/index.js` is registered under `/users`.

## 78: What is fastify-cli?

`fastify-cli` is the official command line tool. It can:

- Create a new project: `npx fastify-cli generate my-app` (add `--lang=ts` for TypeScript)
- Run an app: `fastify start -l info app.js`
- Watch files and restart in dev: `fastify start -w app.js`
- Generate plugins and readme files

Projects made with it use `@fastify/autoload` with `plugins/` and `routes/` folders.

## 79: How do you use Fastify with CommonJS?

```js
const fastify = require("fastify");

const app = fastify({ logger: true });

app.get("/", async () => ({ hello: "world" }));

app.listen({ port: 3000 });
```

Fastify supports both CommonJS and ES modules.

## 80: How do you use Fastify with TypeScript?

Fastify ships its own types, so no `@types` package is needed:

```ts
import Fastify from "fastify";

const app = Fastify({ logger: true });

interface Params {
  id: string;
}

app.get<{ Params: Params }>("/users/:id", async (request) => {
  return { id: request.params.id };
});

await app.listen({ port: 3000 });
```

The generic accepts `Params`, `Querystring`, `Body`, `Headers` and `Reply`.

## 81: What is a type provider?

A type provider lets TypeScript infer request types from your validation schema, so you write the shape once instead of a schema plus an interface.

```ts
import Fastify from "fastify";
import { TypeBoxTypeProvider } from "@fastify/type-provider-typebox";
import { Type } from "typebox";

const app = Fastify().withTypeProvider<TypeBoxTypeProvider>();

app.post(
  "/users",
  {
    schema: {
      body: Type.Object({ name: Type.String(), age: Type.Integer() }),
    },
  },
  async (request) => {
    request.body.name; // string
    request.body.age; // number
    return request.body;
  },
);
```

Official providers exist for TypeBox, json-schema-to-ts and Zod.

## 82: What is the onClose hook?

`onClose` runs when `app.close()` is called, after the server stops taking new requests. It is used to release resources:

```js
app.addHook("onClose", async (instance) => {
  await instance.db.end();
});
```

`onClose` hooks in child plugins run before the ones in their parent, so a database plugin can close its pool before the root hooks run.

## 83: What is the onReady hook?

`onReady` runs once, after all plugins are loaded and before the server starts listening. It is good for things like warming caches or checking that a database is reachable:

```js
app.addHook("onReady", async function () {
  await this.db.query("SELECT 1");
});
```

If an `onReady` hook throws, `ready()` and `listen()` reject.

## 84: What is the onRoute hook?

`onRoute` runs every time a route is registered. It gets the route options and can change them:

```js
app.addHook("onRoute", (routeOptions) => {
  console.log(routeOptions.method, routeOptions.url);
});
```

It is synchronous and must be added before the routes you want to catch. Plugins like `@fastify/swagger` use it to collect routes.

## 85: What is app.server?

`app.server` is the underlying Node.js `http.Server` (or `https`/`http2` server). You can use it to attach things that need the raw server, like some WebSocket or Socket.IO setups:

```js
await app.ready();
console.log(app.server.address());
```

## 86: How do you get the address the server is listening on?

`listen()` resolves with the address string, and `app.addresses()` returns all bound addresses:

```js
const address = await app.listen({ port: 0 });
console.log(address); // http://127.0.0.1:54321
console.log(app.addresses()); // [{ address: '127.0.0.1', family: 'IPv4', port: 54321 }]
```

Port `0` asks the OS for a free port, which is useful in tests.

## 87: How do you run Fastify over HTTPS?

Pass `https` options with the key and certificate:

```js
import fs from "node:fs";
import Fastify from "fastify";

const app = Fastify({
  https: {
    key: fs.readFileSync("./key.pem"),
    cert: fs.readFileSync("./cert.pem"),
  },
});
```

In many production setups TLS ends at a load balancer or reverse proxy instead, and Fastify runs plain HTTP behind it.

## 88: Does Fastify support HTTP/2?

Yes. Set `http2: true`. Browsers only use HTTP/2 over TLS, so you usually also pass `https`:

```js
const app = Fastify({
  http2: true,
  https: {
    allowHTTP1: true,
    key: fs.readFileSync("./key.pem"),
    cert: fs.readFileSync("./cert.pem"),
  },
});
```

`allowHTTP1: true` lets older clients still connect over HTTP/1.1.

## 89: What does reply.sent tell you?

`reply.sent` is `true` once the response has been sent (or the reply was hijacked). You can read it to avoid sending twice:

```js
if (!reply.sent) {
  reply.send({ ok: true });
}
```

In v5 you cannot set `reply.sent = true` anymore. Use `reply.hijack()` if you want to take over the response yourself.

## 90: How do you get the response time of a request?

Use `reply.elapsedTime`, which is the time in milliseconds since Fastify got the request:

```js
app.addHook("onResponse", async (request, reply) => {
  request.log.info({ ms: reply.elapsedTime }, "request done");
});
```

In v4 this was the method `reply.getResponseTime()`, which was removed in v5.

## 91: What is the difference between app.log and request.log?

`app.log` is the main logger. `request.log` is a child logger created for each request, with the request ID bound to it. Use `request.log` inside handlers and hooks, so every log line can be traced back to its request.

## 92: Does Fastify log requests automatically?

Yes, when logging is on, Fastify logs "incoming request" when a request comes in and "request completed" with the status code and response time when it ends. To turn these off use a `LogController` with `disableRequestLogging: true`. The older top-level `disableRequestLogging` option still works in v5 but is deprecated.

## 93: How do you redact sensitive data from logs?

Pino has a `redact` option that hides fields by path:

```js
const app = Fastify({
  logger: {
    redact: [
      "req.headers.authorization",
      "req.headers.cookie",
      "body.password",
    ],
  },
});
```

Redacted values show as `[Redacted]`. You can also pass `{ paths: [...], remove: true }` to drop them.

## 94: What does reply.hijack() do?

`hijack()` tells Fastify you will handle the response yourself through `reply.raw`. Fastify will skip its own sending logic and the remaining hooks:

```js
app.get("/raw", (request, reply) => {
  reply.hijack();
  reply.raw.writeHead(200, { "Content-Type": "text/plain" });
  reply.raw.end("handled manually");
});
```

You lose features like `onSend` hooks and logging of the response, so use it only when needed.

## 95: How do you send a stream?

Pass a readable stream to `reply.send()` or return it:

```js
import fs from "node:fs";

app.get("/download", async (request, reply) => {
  reply.type("application/pdf");
  return fs.createReadStream("./report.pdf");
});
```

Fastify pipes the stream to the response and handles errors on it.

## 96: Can you send a Buffer?

Yes:

```js
app.get("/image", async (request, reply) => {
  const buf = await fs.promises.readFile("./logo.png");
  reply.type("image/png");
  return buf;
});
```

If you do not set a content type, Fastify uses `application/octet-stream` for buffers.

## 97: How does Fastify compare to Express at a high level?

| Area           | Fastify                       | Express                        |
| -------------- | ----------------------------- | ------------------------------ |
| Speed          | Much faster in benchmarks     | Slower                         |
| Validation     | Built in with JSON Schema     | Needs a library                |
| Async handlers | First class                   | Supported in Express 5         |
| Extending      | Plugins with encapsulation    | Middleware in one global chain |
| Logging        | Built in (Pino)               | Not built in                   |
| TypeScript     | Types included                | Through `@types/express`       |
| Ecosystem      | Smaller but covers most needs | Very large                     |

## 98: Can you use Express middleware in Fastify?

Yes, with `@fastify/express` or `@fastify/middie`:

```js
import middie from "@fastify/middie";

await app.register(middie);
app.use(require("cors")());
```

This is mostly for migrations or reusing a package that has no Fastify version. Middleware does not get the Fastify `request` and `reply` objects, and native Fastify plugins and hooks are faster.

## 99: What are the route-level hooks?

You can attach hooks to a single route through route options:

```js
app.get(
  "/admin",
  {
    onRequest: async (request) => {
      await request.jwtVerify();
    },
    preHandler: [checkAdmin, loadSettings],
  },
  async () => "admin page",
);
```

Each can be a function or an array. They run after the app-level hooks of the same type.

## 100: What does the route config option do?

`config` lets you attach custom data to a route. You read it from `request.routeOptions.config`:

```js
app.get("/public", { config: { auth: false } }, async () => "hi");

app.addHook("onRequest", async (request, reply) => {
  if (request.routeOptions.config.auth === false) return;
  await request.jwtVerify();
});
```

This is a common way to mark routes as public, set rate limits per route and so on.

## 101: What is request.routeOptions?

It holds info about the matched route:

- `url` (the route pattern, like `/users/:id`)
- `method`
- `config`
- `schema`
- `bodyLimit`, `logLevel`, `exposeHeadRoute`, `prefixTrailingSlash`, `handlerTimeout` and more

In v5 it replaced `request.routerPath`, `request.routerMethod`, `request.routeConfig` and `request.routeSchema`.

## 102: How do you read environment variables in Fastify?

You can read `process.env` directly, but the common Fastify way is `@fastify/env`, which validates env vars with a JSON Schema and puts them on the instance:

```js
import fastifyEnv from "@fastify/env";

await app.register(fastifyEnv, {
  dotenv: true,
  schema: {
    type: "object",
    required: ["DATABASE_URL"],
    properties: {
      PORT: { type: "integer", default: 3000 },
      DATABASE_URL: { type: "string" },
    },
  },
});

console.log(app.config.PORT);
```

If a required variable is missing, the app fails to start.

## 103: What is fastify.version?

It is a string with the version of Fastify in use, for example `'5.12.7'`. It is useful in health endpoints or when a plugin needs to check compatibility.

## 104: What is the plugin options object?

The second argument to `register()` is passed to the plugin function as `opts`:

```js
async function greet(app, opts) {
  app.get("/hi", async () => `Hi, ${opts.name}`);
}

app.register(greet, { name: "Ana", prefix: "/greet" });
```

Some keys are reserved by Fastify: `prefix`, `logLevel` and `logSerializers`.

## 105: What is the difference between async and callback style plugins?

An async plugin is an async function that finishes when its promise resolves:

```js
async function plugin(app, opts) {
  await connect();
}
```

A callback plugin gets a `done` argument it must call:

```js
function plugin(app, opts, done) {
  connect().then(() => done(), done);
}
```

In v5 you cannot mix them. An async plugin must not take `done`.

## 106: How do you register many routes from one file?

Export a plugin that defines all the routes for a resource:

```js
// routes/products.js
export default async function (app) {
  app.get("/", listProducts);
  app.get("/:id", getProduct);
  app.post("/", createProduct);
  app.delete("/:id", deleteProduct);
}

// app.js
app.register(import("./routes/products.js"), { prefix: "/products" });
```

## 107: How do you check if a decorator exists?

Use `hasDecorator`, `hasRequestDecorator` and `hasReplyDecorator`:

```js
if (!app.hasDecorator("db")) {
  throw new Error("db plugin is required");
}
```

## 108: What is hasPlugin()?

`app.hasPlugin(name)` returns `true` if a plugin with that name (set through `fastify-plugin`) was registered in the current context or a parent:

```js
if (!app.hasPlugin("@fastify/cookie")) {
  app.register(cookie);
}
```

## 109: What is hasRoute()?

It checks if a route is already registered:

```js
app.hasRoute({ method: "GET", url: "/users/:id" }); // true or false
```

In v5 you must pass the route pattern as written (`/users/:id`), not a real URL like `/users/5`. To match a real URL use `findRoute()`.

## 110: How do you add compression?

Use `@fastify/compress`:

```js
import compress from "@fastify/compress";

await app.register(compress, { global: true, threshold: 1024 });
```

It compresses responses with gzip, deflate or brotli based on the `Accept-Encoding` header. Many teams let a reverse proxy like Nginx do compression instead.

## 111: How do you add rate limiting?

Use `@fastify/rate-limit`:

```js
import rateLimit from "@fastify/rate-limit";

await app.register(rateLimit, {
  max: 100,
  timeWindow: "1 minute",
});

app.get(
  "/login",
  {
    config: { rateLimit: { max: 5, timeWindow: "1 minute" } },
  },
  async () => "ok",
);
```

By default counters are stored in memory. For several instances use a Redis store so limits are shared.

## 112: How do you generate OpenAPI docs?

Use `@fastify/swagger` with `@fastify/swagger-ui`:

```js
import swagger from "@fastify/swagger";
import swaggerUi from "@fastify/swagger-ui";

await app.register(swagger, {
  openapi: {
    info: { title: "My API", version: "1.0.0" },
  },
});

await app.register(swaggerUi, { routePrefix: "/docs" });
```

It reads the schemas of your routes and builds the spec. The UI is available at `/docs`. Register swagger before your routes.

## 113: How do you add a description and tags for OpenAPI docs?

Add them to the route schema:

```js
app.get(
  "/users",
  {
    schema: {
      description: "List all users",
      tags: ["users"],
      summary: "List users",
      response: {
        200: { type: "array", items: { type: "object" } },
      },
    },
  },
  listUsers,
);
```

These fields are ignored by validation and used only by `@fastify/swagger`. Add `hide: true` to leave a route out of the docs.

## 114: How do you add a health check endpoint?

A simple route is enough:

```js
app.get("/health", { logLevel: "warn" }, async () => {
  return { status: "ok", uptime: process.uptime() };
});
```

Setting the route `logLevel` to `warn` stops it from filling logs with info lines on every probe. For deeper checks look at `@fastify/under-pressure`.

## 115: What is @fastify/under-pressure?

It watches event loop delay, heap usage, RSS and event loop use. When a limit is passed, it answers new requests with 503 so the server does not get overloaded:

```js
import underPressure from "@fastify/under-pressure";

app.register(underPressure, {
  maxEventLoopDelay: 1000,
  maxHeapUsedBytes: 1_000_000_000,
  exposeStatusRoute: "/status",
});
```

Load balancers can then route traffic to healthier instances.

## 116: How do you connect to PostgreSQL in Fastify?

The official plugin is `@fastify/postgres`, which wraps the `pg` pool:

```js
import pg from "@fastify/postgres";

app.register(pg, { connectionString: process.env.DATABASE_URL });

app.get("/users", async () => {
  const { rows } = await app.pg.query("SELECT id, name FROM users");
  return rows;
});
```

Many teams instead write a small plugin around an ORM like Prisma or Drizzle.

## 117: How do you connect to MongoDB?

Use `@fastify/mongodb`:

```js
import mongodb from "@fastify/mongodb";

app.register(mongodb, { url: process.env.MONGO_URL, forceClose: true });

app.get("/books", async function () {
  return this.mongo.db.collection("books").find().toArray();
});
```

`forceClose: true` closes the connection when the app closes.

## 118: How do you connect to Redis?

Use `@fastify/redis`, which wraps `ioredis`:

```js
import redis from "@fastify/redis";

app.register(redis, { url: process.env.REDIS_URL });

app.get("/count", async () => {
  const count = await app.redis.incr("visits");
  return { count };
});
```

## 119: What is the this keyword inside a handler?

In a handler written with `function` (not an arrow function), `this` is the Fastify instance of the context where the route was registered:

```js
app.get("/", async function () {
  return this.config.env;
});
```

With an arrow function, `this` is whatever it was outside, so use `request.server` instead.

## 120: How do you access the Fastify instance from a request?

Use `request.server`:

```js
app.get("/users", async (request) => {
  return request.server.db.users.findMany();
});
```

This works well with arrow functions and in handlers defined in other files.

## 121: How do you send JSON with a custom content type?

Set the type and send an object. Fastify serializes it to JSON as long as the content type looks like JSON:

```js
app.get("/problem", async (request, reply) => {
  reply.code(400).type("application/problem+json");
  return { type: "about:blank", title: "Bad input", status: 400 };
});
```

## 122: What is the default JSON serializer?

Without a response schema, Fastify uses `JSON.stringify`. With a response schema, it uses a function compiled by `fast-json-stringify`, which is faster and drops fields that are not in the schema.

## 123: How do you set a default value for a query param?

Use `default` in the querystring schema. Ajv's `useDefaults` option, which Fastify turns on, fills it in:

```js
schema: {
  querystring: {
    type: 'object',
    properties: {
      page: { type: 'integer', default: 1 },
      limit: { type: 'integer', default: 20 }
    }
  }
}
```

`/items` gives `{ page: 1, limit: 20 }` in `request.query`.

## 124: How do you accept only certain values for a field?

Use `enum`:

```js
schema: {
  querystring: {
    type: 'object',
    properties: {
      sort: { type: 'string', enum: ['asc', 'desc'] }
    }
  }
}
```

Any other value fails validation with a 400.

## 125: How do you reuse a schema across routes?

Add it with `addSchema` and give it an `$id`, then reference it with `$ref`:

```js
app.addSchema({
  $id: "user",
  type: "object",
  properties: {
    id: { type: "integer" },
    name: { type: "string" },
  },
});

app.get(
  "/users/:id",
  {
    schema: { response: { 200: { $ref: "user#" } } },
  },
  getUser,
);
```

## 126: What formats can you use for strings in schemas?

Fastify's Ajv setup includes `ajv-formats`, so you can use `email`, `uri`, `uuid`, `date`, `date-time`, `time`, `ipv4`, `ipv6`, `hostname` and others:

```js
properties: {
  id: { type: 'string', format: 'uuid' },
  createdAt: { type: 'string', format: 'date-time' }
}
```

In v5, `date-time` and `time` require a timezone. Use `iso-date-time` or `iso-time` if the timezone is optional.

## 127: What does Fastify do with extra fields in the body?

By default Fastify configures Ajv with `removeAdditional: true`. This removes extra properties only if the schema has `additionalProperties: false`. Without that keyword, extra fields are kept.

```js
body: {
  type: 'object',
  additionalProperties: false,
  properties: { name: { type: 'string' } }
}
```

With this schema, sending `{ name: 'a', isAdmin: true }` gives the handler just `{ name: 'a' }`.

## 128: What is type coercion in Fastify validation?

Ajv is set up with `coerceTypes: 'array'`. It converts values to the type in the schema when possible. For example the query string `?limit=10` comes in as the string `"10"` and becomes the number `10`. A single value is also turned into an array if the schema expects an array.

This is why params and query values have the right types inside handlers when you have a schema.

## 129: How do you handle a POST with an empty body?

If the body is optional, do not add `required` to the schema and do not set a body schema that needs fields. Also note: if the client sends `Content-Type: application/json` with an empty body, Fastify returns a 400 error (`FST_ERR_CTP_EMPTY_JSON_BODY`). Clients should not send a JSON content type with no body.

## 130: What are the main official Fastify plugins?

Some of the most used ones:

- `@fastify/cors`, `@fastify/helmet`, `@fastify/rate-limit` for security
- `@fastify/jwt`, `@fastify/auth`, `@fastify/cookie`, `@fastify/session`, `@fastify/secure-session`
- `@fastify/static`, `@fastify/view`, `@fastify/compress`
- `@fastify/multipart`, `@fastify/formbody`
- `@fastify/swagger`, `@fastify/swagger-ui`
- `@fastify/postgres`, `@fastify/mongodb`, `@fastify/redis`
- `@fastify/websocket`
- `@fastify/autoload`, `@fastify/env`, `@fastify/sensible`
- `@fastify/under-pressure`, `@fastify/http-proxy`

## 131: How do you add WebSocket support?

Use `@fastify/websocket`:

```js
import websocket from "@fastify/websocket";

await app.register(websocket);

app.get("/ws", { websocket: true }, (socket, request) => {
  socket.on("message", (message) => {
    socket.send(`echo: ${message}`);
  });
});
```

The handler gets the WebSocket and the request. Normal hooks like `onRequest` run before the upgrade, so you can do auth there.

## 132: What does app.prefix return?

`app.prefix` is the full prefix of the current context. Inside a plugin registered with `prefix: '/api'` that registers another with `prefix: '/v1'`, the inner `this.prefix` is `/api/v1`. It is useful when building links.

## 133: What does initialConfig show?

`app.initialConfig` is a frozen, read-only object with the options the instance was created with (only some safe ones, like `bodyLimit`, `connectionTimeout`, `keepAliveTimeout`, `trustProxy`, `http2`, `routerOptions` and so on). Plugins can read it to adjust their behavior.

## 134: How do you add a custom header to every response?

Use an `onSend` or `onRequest` hook:

```js
app.addHook("onRequest", async (request, reply) => {
  reply.header("X-Powered-By", "my-api");
});
```

Setting it early in `onRequest` means even error responses carry it.

## 135: What is the onSend hook?

`onSend` runs after serialization, right before the response is written. It gets the payload (a string, buffer or stream) and can return a new one:

```js
app.addHook("onSend", async (request, reply, payload) => {
  reply.header("X-Length", Buffer.byteLength(payload ?? ""));
  return payload;
});
```

You can change headers here, but not the status code of an already decided error path.

## 136: What is the preSerialization hook?

It runs before the payload is serialized, only when the payload is not a string, buffer, stream or null. It can change the object:

```js
app.addHook("preSerialization", async (request, reply, payload) => {
  return { data: payload, requestId: request.id };
});
```

This is a common way to wrap all responses in an envelope.

## 137: What is the onError hook?

`onError` runs when an error happens, before the error handler sends the response. It is for logging or reporting only. You cannot change the response from it:

```js
app.addHook("onError", async (request, reply, error) => {
  reportToSentry(error);
});
```

To change the error response, use `setErrorHandler`.

## 138: How do you register several plugins in order?

Call `register()` for each. Fastify loads them in that order:

```js
app.register(envPlugin);
app.register(dbPlugin); // can use app.config
app.register(authPlugin); // can use app.db
app.register(routes);
```

Each plugin can rely on the ones registered before it (as long as they are shared with `fastify-plugin`).

## 139: Can you await app.register()?

Yes. Awaiting it loads that plugin (and the ones before it) right away:

```js
await app.register(dbPlugin);
console.log(app.db); // available now
```

Without `await`, registration is queued and runs when `ready()` or `listen()` is called.

## 140: Is Fastify a good fit for serverless?

Yes. Fastify starts fast and there are adapters for AWS Lambda (`@fastify/aws-lambda`) and others. For Google Cloud Functions and Vercel you can pass requests to `app.server.emit('request', req, res)` after `await app.ready()`. Keep the app instance outside the handler so warm starts reuse it.

## 141: What does app.routing do?

`app.routing(req, res)` sends a raw Node.js request into Fastify's router. It is used with a custom server or in serverless setups where you already have `req` and `res` objects. Most apps never call it directly.

## 142: How do you add a route for all HTTP methods?

Use `app.all()`:

```js
app.all("/echo", async (request) => {
  return { method: request.method };
});
```

It registers the route for every method Fastify supports.

## 143: What HTTP methods does Fastify support by default?

`GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`. Some extra methods like `PROPFIND`, `SEARCH` and `TRACE` were removed from the defaults in v5. You can add them back with `app.addHttpMethod()`.

## 144: How do you add a custom HTTP method?

Use `addHttpMethod`:

```js
app.addHttpMethod("SEARCH", { hasBody: true });

app.route({
  method: "SEARCH",
  url: "/items",
  handler: async (request) => ({ query: request.body }),
});
```

`hasBody: true` tells Fastify to parse a body for that method.

## 145: How do you return a different status for validation errors?

Use the `attachValidation` route option and check `request.validationError` in the handler:

```js
app.post(
  "/items",
  {
    attachValidation: true,
    schema: { body: { type: "object", required: ["name"] } },
  },
  async (request, reply) => {
    if (request.validationError) {
      return reply.code(422).send({ message: request.validationError.message });
    }
    return "ok";
  },
);
```

A global error handler that checks `error.validation` is often cleaner, though.

## 146: How do you set up a project in TypeScript quickly?

Use the CLI:

```bash
npx fastify-cli generate my-api --lang=ts
cd my-api
npm install
npm run dev
```

This gives a project with `@fastify/autoload`, `plugins/` and `routes/` folders, tests and a `tsconfig.json`.

## 147: How does Fastify handle JSON parse errors?

If the body is not valid JSON, Fastify replies with 400 and the code `FST_ERR_CTP_INVALID_JSON_BODY` (or a Bad Request with the parse message). The handler never runs. You can catch it in your error handler to change the message.

## 148: Can Fastify serve both an API and a frontend?

Yes. Serve the built frontend with `@fastify/static` and keep API routes under a prefix:

```js
app.register(fastifyStatic, { root: path.join(import.meta.dirname, "dist") });
app.register(apiRoutes, { prefix: "/api" });

app.setNotFoundHandler((request, reply) => {
  if (request.url.startsWith("/api")) {
    return reply.code(404).send({ message: "Not found" });
  }
  return reply.sendFile("index.html");
});
```

The not-found handler returns `index.html` for client-side routes.

## 149: What are the Fastify request lifecycle steps in short?

1. Incoming request, route lookup
2. `onRequest` hooks
3. `preParsing` hooks
4. Body parsing
5. `preValidation` hooks
6. Validation
7. `preHandler` hooks
8. Handler
9. `preSerialization` hooks
10. Serialization
11. `onSend` hooks
12. Response sent
13. `onResponse` hooks

`onError` runs when an error happens, `onTimeout` when the socket times out and `onRequestAbort` when the client closes the connection early.

## 150: Where should you look when you need a Fastify plugin?

Start with the official plugins under the `@fastify` npm scope. Then check the "Ecosystem" page on fastify.dev, which lists both core and community plugins. Before using a community plugin, check that it supports Fastify v5, since many plugins have separate major versions for v4 and v5.

# Moderate Questions (151-300)

## 151: In what order do hooks run when they are added at different levels?

Hooks run from the outermost context to the innermost, in the order they were added. For one request, the `onRequest` hooks from the root run first, then the ones from the plugin, then the route-level `onRequest` hooks. The same applies to every other request hook type.

```js
app.addHook("onRequest", async () => console.log("root"));

app.register(async (child) => {
  child.addHook("onRequest", async () => console.log("child"));
  child.get(
    "/x",
    { onRequest: async () => console.log("route") },
    async () => "ok",
  );
});
// GET /x prints: root, child, route
```

## 152: What is the difference between async hooks and callback hooks?

Async hooks return a promise:

```js
app.addHook("preHandler", async (request, reply) => {
  await checkSomething(request);
});
```

Callback hooks get a `done` function as the last argument:

```js
app.addHook("preHandler", (request, reply, done) => {
  checkSomething(request).then(() => done(), done);
});
```

You cannot use both in one hook. If an async hook also declares `done`, Fastify throws `FST_ERR_HOOK_INVALID_ASYNC_HANDLER` at startup.

## 153: How do you stop the request from a hook and send a response?

Call `reply.send()` and, in an async hook, return the reply:

```js
app.addHook("onRequest", async (request, reply) => {
  if (isBlocked(request.ip)) {
    return reply.code(403).send({ message: "Forbidden" });
  }
});
```

After the reply is sent, Fastify skips the remaining hooks and the handler. In a callback hook, call `reply.send()` and do not call `done()`.

## 154: How do you return an error from a hook?

Throw it in an async hook, or pass it to `done` in a callback hook:

```js
app.addHook("preHandler", async (request) => {
  if (!request.user) {
    const err = new Error("Unauthorized");
    err.statusCode = 401;
    throw err;
  }
});
```

The error goes to the error handler, which sends the response.

## 155: What is the preParsing hook used for?

`preParsing` runs before the body is parsed. It receives the raw payload stream and can return a new stream. You use it to decompress, decrypt or measure the incoming body:

```js
import zlib from "node:zlib";

app.addHook("preParsing", async (request, reply, payload) => {
  if (request.headers["content-encoding"] === "gzip") {
    const unzipped = payload.pipe(zlib.createGunzip());
    unzipped.receivedEncodedLength = 0;
    return unzipped;
  }
  return payload;
});
```

If you return a new stream, set `receivedEncodedLength` on it so the body limit checks keep working.

## 156: What is the preValidation hook used for?

`preValidation` runs after the body is parsed but before schema validation. You can change `request.body` here, for example to trim strings or map an old field name to a new one before the schema checks it:

```js
app.addHook("preValidation", async (request) => {
  if (request.body && typeof request.body.email === "string") {
    request.body.email = request.body.email.trim().toLowerCase();
  }
});
```

## 157: When should you use onRequest vs preHandler for authentication?

Use `onRequest` when you only need headers or cookies, like checking a JWT. It runs before body parsing, so a bad request is rejected before Fastify spends time reading and parsing a large body.

Use `preHandler` when the auth check needs the parsed and validated body or params, like checking that the user owns the resource in `request.params.id`.

## 158: What is the onTimeout hook?

`onTimeout` runs when the socket times out because of `connectionTimeout`. At that point the connection is gone and you cannot send anything. It is useful for logging and metrics:

```js
app.addHook("onTimeout", async (request) => {
  request.log.warn({ url: request.url }, "socket timed out");
});
```

## 159: What is the onRequestAbort hook?

`onRequestAbort` runs when the client closes the connection before the response is complete. You can use it to log the event or stop work that is no longer needed:

```js
app.addHook("onRequestAbort", async (request) => {
  request.log.info("client aborted the request");
});
```

It is not reliable for every abort case (for example when the abort is detected only after the response is done), so do not build critical logic on it.

## 160: What are the preClose and onClose hooks and how do they differ?

- `preClose` runs when `close()` is called, before the server stops accepting connections. It is for things that must happen while in-flight requests are still running, like closing WebSocket connections so they do not block shutdown.
- `onClose` runs after the server has stopped and in-flight requests are done. It is for closing database pools and other resources.

## 161: What is the onListen hook?

`onListen` runs once the server starts listening. It is good for logging the URL or doing work that should only happen once the server is reachable. Errors thrown in `onListen` are logged but do not stop the server.

```js
app.addHook("onListen", async function () {
  this.log.info(`listening on ${this.listeningOrigin}`);
});
```

## 162: What is the onRegister hook?

`onRegister` runs every time a new encapsulated context is created by `register()`. It receives the new instance and the plugin options. It does not run for plugins wrapped with `fastify-plugin`, since they do not create a new context.

```js
app.addHook("onRegister", (instance, opts) => {
  instance.log.debug({ prefix: opts.prefix }, "new context");
});
```

## 163: How do you add hooks that only apply to some routes?

Put the routes and the hook in the same plugin without `fastify-plugin`:

```js
app.register(
  async (admin) => {
    admin.addHook("onRequest", requireAdmin);
    admin.get("/stats", getStats);
    admin.delete("/users/:id", deleteUser);
  },
  { prefix: "/admin" },
);

app.get("/public", async () => "open"); // requireAdmin does not run
```

Or attach the hook to each route in its options.

## 164: Why does a decorator added in one plugin not appear in another?

Because of encapsulation. A decorator added in plugin A only exists in plugin A and its children. Sibling plugins and the parent cannot see it.

Fix it by:

1. Wrapping plugin A with `fastify-plugin`, so the decorator goes to the parent.
2. Or moving the decorator up to a common parent context.

## 165: What are the common use cases for fastify-plugin?

Use `fastify-plugin` when the plugin provides something the rest of the app needs:

- Database or cache clients (`app.db`, `app.redis`)
- Config (`app.config`)
- Auth helpers (`app.authenticate`)
- Global hooks like request timing or CORS
- Shared schemas added with `addSchema`

Do not use it for groups of routes, since you usually want their hooks and error handlers to stay local.

## 166: What do the name and dependencies options of fastify-plugin do?

```js
import fp from "fastify-plugin";

export default fp(
  async function authPlugin(app) {
    app.decorate("authenticate", async (request) => request.jwtVerify());
  },
  {
    name: "auth",
    fastify: "5.x",
    dependencies: ["@fastify/jwt"],
    decorators: { fastify: ["jwt"] },
  },
);
```

- `name` makes the plugin show up in `hasPlugin()`, error messages and dependency checks.
- `fastify` is a semver range. Fastify throws if the running version does not match.
- `dependencies` lists plugin names that must be registered first.
- `decorators` lists decorators that must already exist on the instance, request or reply.

## 167: How do you write a plugin that accepts options with defaults?

```js
import fp from "fastify-plugin";

async function cachePlugin(app, opts) {
  const ttl = opts.ttl ?? 60;
  const store = new Map();

  app.decorate("cache", {
    get: (key) => store.get(key),
    set: (key, value) => {
      store.set(key, value);
      setTimeout(() => store.delete(key), ttl * 1000).unref();
    },
  });
}

export default fp(cachePlugin, { name: "cache" });
```

```js
app.register(cachePlugin, { ttl: 120 });
```

## 168: Can plugin options be a function?

Yes. If you pass a function, Fastify calls it with the parent instance, so you can use values from earlier plugins:

```js
app.register(dbPlugin, (parent) => ({
  connectionString: parent.config.DATABASE_URL,
}));
```

This is handy when options depend on config that is loaded by another plugin.

## 169: How do you decorate the request with a per-request object safely?

In v5 you cannot pass an object or array as the decorator value, because it would be shared by every request. Use one of these:

```js
// 1. Declare with null, set in a hook
app.decorateRequest("ctx", null);
app.addHook("onRequest", async (request) => {
  request.ctx = { startedAt: Date.now() };
});

// 2. Use a getter that builds a fresh value
app.decorateRequest("tags", {
  getter() {
    return [];
  },
});
```

Note that with a getter, a new array is created every time you read the property. For a value that should persist through the request, use the first approach.

## 170: What error do you get if you decorate after the server starts?

`FST_ERR_DEC_AFTER_START`. Decorators must be added while plugins are loading, before `ready()` finishes. This keeps object shapes stable for all requests.

## 171: What does the dependencies argument of decorate do?

The third argument lists decorators that must already exist:

```js
app.decorate("userService", createUserService(app.db), ["db"]);
```

If `db` is not defined, Fastify throws `FST_ERR_DEC_MISSING_DEPENDENCY` at startup. It makes missing setup obvious early.

## 172: What are getDecorator and setDecorator?

`getDecorator(name)` returns a decorator and throws `FST_ERR_DEC_UNDECLARED` if it does not exist. That is safer than reading `app.db` and getting `undefined` silently:

```js
const db = app.getDecorator("db");
```

`setDecorator(name, value)` sets a request decorator's value and also throws if it was never declared:

```js
app.decorateRequest("user", null);

app.addHook("onRequest", async (request) => {
  request.setDecorator("user", await loadUser(request));
});
```

Both accept TypeScript generics for typing.

## 173: How do you add types for custom decorators in TypeScript?

Use declaration merging on Fastify's interfaces:

```ts
import "fastify";
import type { Pool } from "pg";

declare module "fastify" {
  interface FastifyInstance {
    db: Pool;
  }
  interface FastifyRequest {
    user: { id: string; role: string } | null;
  }
}
```

Put this in the plugin file or a `.d.ts` file. The types are global, so they show up even in contexts where the decorator does not exist at runtime. `getDecorator<T>()` is an alternative that types the value at the call site.

## 174: How do you type route params, body and query in TypeScript without a type provider?

Pass a `RouteGenericInterface`-shaped generic:

```ts
interface CreateUser {
  Params: { orgId: string };
  Querystring: { notify?: boolean };
  Body: { name: string; email: string };
  Reply: { 201: { id: string }; 400: { message: string } };
}

app.post<CreateUser>("/orgs/:orgId/users", async (request, reply) => {
  const { name } = request.body;
  return reply.code(201).send({ id: "1" });
});
```

The downside is the types and the schema are separate and can drift apart.

## 175: How do you use Zod with Fastify?

Use `@fastify/type-provider-zod`. It brings a validator and serializer compiler for Zod schemas and the type provider:

```ts
import Fastify from "fastify";
import {
  serializerCompiler,
  validatorCompiler,
  type ZodTypeProvider,
} from "@fastify/type-provider-zod";
import { z } from "zod";

const app = Fastify();
app.setValidatorCompiler(validatorCompiler);
app.setSerializerCompiler(serializerCompiler);

app.withTypeProvider<ZodTypeProvider>().post(
  "/users",
  {
    schema: {
      body: z.object({ name: z.string().min(1), age: z.number().int() }),
      response: { 201: z.object({ id: z.string() }) },
    },
  },
  async (request, reply) => {
    return reply.code(201).send({ id: request.body.name });
  },
);
```

Zod is easier to read for many teams, but it is slower than Ajv with compiled schemas, and you lose the `fast-json-stringify` speedup.

## 176: Why does withTypeProvider need to be called in each plugin?

Type providers are a TypeScript-only feature, and TypeScript cannot know that a child instance created by `register()` has the same provider. The plugin's `app` parameter is typed as a plain `FastifyInstance`.

To fix it, type the plugin with the provider's plugin type:

```ts
import type { FastifyPluginAsyncTypebox } from "@fastify/type-provider-typebox";

const routes: FastifyPluginAsyncTypebox = async (app) => {
  // app already uses the TypeBox provider here
};
```

Or call `app.withTypeProvider<TypeBoxTypeProvider>()` at the top of each plugin.

## 177: How do you write a typed plugin in TypeScript?

```ts
import fp from "fastify-plugin";
import type { FastifyPluginAsync } from "fastify";

interface Options {
  prefix?: string;
  apiKey: string;
}

const apiKeyAuth: FastifyPluginAsync<Options> = async (app, opts) => {
  app.addHook("onRequest", async (request, reply) => {
    if (request.headers["x-api-key"] !== opts.apiKey) {
      return reply.code(401).send({ message: "Invalid API key" });
    }
  });
};

export default fp(apiKeyAuth, { name: "api-key-auth" });
```

## 178: What does schemaErrorFormatter do?

It lets you change the error object created when validation fails:

```js
const app = Fastify({
  schemaErrorFormatter: (errors, dataVar) => {
    const first = errors[0];
    return new Error(`${dataVar}${first.instancePath} ${first.message}`);
  },
});
```

`errors` is the array from Ajv and `dataVar` is `body`, `querystring`, `params` or `headers`. It can also be set per route or per plugin with `app.setSchemaErrorFormatter()`.

## 179: How do you return all validation errors instead of only the first?

Turn on Ajv's `allErrors` option:

```js
const app = Fastify({
  ajv: {
    customOptions: { allErrors: true },
  },
});
```

Then format them in the error handler:

```js
app.setErrorHandler((error, request, reply) => {
  if (error.validation) {
    return reply.code(400).send({
      message: "Validation failed",
      errors: error.validation.map((e) => ({
        path: e.instancePath,
        message: e.message,
      })),
    });
  }
  reply.send(error);
});
```

Be careful: `allErrors` makes validation of very large or nested payloads more expensive.

## 180: How do you detect a validation error in the error handler?

Validation errors have a `validation` array and a `validationContext` (`body`, `params`, `querystring` or `headers`):

```js
app.setErrorHandler((error, request, reply) => {
  if (error.validation) {
    return reply.code(422).send({
      where: error.validationContext,
      issues: error.validation,
    });
  }
  throw error;
});
```

The code is `FST_ERR_VALIDATION`.

## 181: How do you create typed errors with @fastify/error?

`@fastify/error` creates error classes with a code, message template and status:

```js
import createError from "@fastify/error";

const UserNotFound = createError(
  "APP_USER_NOT_FOUND",
  "User %s not found",
  404,
);

app.get("/users/:id", async (request) => {
  const user = await findUser(request.params.id);
  if (!user) throw new UserNotFound(request.params.id);
  return user;
});
```

Fastify uses `statusCode` from the error, so the client gets a 404 with `code: 'APP_USER_NOT_FOUND'`.

## 182: How does the default error handler build its response?

It sends a JSON body with `statusCode`, `code` (if present), `error` (the HTTP status text) and `message`. The status comes from `error.statusCode` or `error.status` if it is 400 or above, otherwise 500.

It logs 5xx errors at `error` level and 4xx errors at `info` level. For 5xx, consider hiding `message` in production with a custom error handler, since it can leak internal details.

## 183: How do error handlers work with encapsulation?

Each context can have its own error handler. An error goes to the closest error handler in the plugin tree. If that handler throws, the error goes to the parent's error handler.

```js
app.setErrorHandler(rootHandler);

app.register(async (api) => {
  api.setErrorHandler((error, request, reply) => {
    if (error.code === "P2025") {
      return reply.code(404).send({ message: "Not found" });
    }
    throw error; // goes to rootHandler
  });
  api.register(routes);
});
```

## 184: Can you call setErrorHandler twice in the same plugin?

Not by default in v5. Calling it twice in the same context throws `FST_ERR_ERROR_HANDLER_ALREADY_SET`, because the second call would silently replace the first. Set `allowErrorHandlerOverride: true` in the server options if you really need to replace it in the same scope. Different child plugins can still each set their own handler.

## 185: What is the errorHandler route option?

You can set an error handler for just one route:

```js
app.get(
  "/legacy",
  {
    errorHandler: (error, request, reply) => {
      reply.code(500).send({ legacyError: error.message });
    },
  },
  legacyHandler,
);
```

It takes priority over the context error handler for that route.

## 186: Why should you not send a response inside onError?

`onError` is for side effects like logging. Calling `reply.send()` there throws `FST_ERR_SEND_INSIDE_ONERR`. To control the response, use `setErrorHandler` or the route's `errorHandler`.

## 187: What happens if you call reply.send() twice?

The second call is ignored and Fastify logs a warning with `FST_ERR_REP_ALREADY_SENT`. This usually means a bug, like a missing `return` after sending in an early exit:

```js
app.get("/", async (request, reply) => {
  if (!request.query.id) {
    reply.code(400).send({ message: "id required" }); // missing return
  }
  return { ok: true }; // second send
});
```

Use `return reply.code(400).send(...)` to fix it.

## 188: How do you handle errors from a stream sent in the reply?

Fastify listens for `error` on streams passed to `reply.send()`. If the stream fails before headers are sent, Fastify sends a 500. If headers are already sent, it destroys the connection, since a status code cannot be changed after the response has started. Check that a file exists before streaming it if you want a clean 404.

## 189: What are custom content type parsers?

They let Fastify parse bodies of other content types. Register them with `addContentTypeParser`:

```js
import { XMLParser } from "fast-xml-parser";

const xml = new XMLParser();

app.addContentTypeParser(
  "application/xml",
  { parseAs: "string" },
  (request, body, done) => {
    try {
      done(null, xml.parse(body));
    } catch (err) {
      err.statusCode = 400;
      done(err);
    }
  },
);
```

`parseAs` can be `'string'` or `'buffer'`. Without it, you get the raw stream.

## 190: How do you get the raw body for webhook signature checks?

Services like Stripe sign the exact raw body. Add a parser that keeps the raw buffer and also parses JSON:

```js
app.addContentTypeParser(
  "application/json",
  { parseAs: "buffer" },
  (request, body, done) => {
    request.rawBody = body;
    try {
      done(null, JSON.parse(body.toString()));
    } catch (err) {
      err.statusCode = 400;
      done(err);
    }
  },
);
```

Put it inside the webhook plugin so it only affects those routes. The community plugin `fastify-raw-body` does the same thing with route config.

## 191: How do you make a catch-all content type parser?

Use `'*'`:

```js
app.addContentTypeParser("*", (request, payload, done) => {
  let data = "";
  payload.on("data", (chunk) => {
    data += chunk;
  });
  payload.on("end", () => done(null, data));
  payload.on("error", done);
});
```

It is used when no other parser matches. You can also pass a regex as the content type, for example `/^image\/.*/`.

## 192: How do you remove or replace the default JSON parser?

```js
app.removeContentTypeParser("application/json");
app.addContentTypeParser("application/json", { parseAs: "string" }, myParser);
```

`removeAllContentTypeParsers()` removes all of them, including `text/plain`. If you want Fastify's JSON parser with different options, use `app.getDefaultJsonParser('ignore', 'ignore')` which returns a parser with custom proto and constructor poisoning settings.

## 193: How do you use the bodyLimit inside a custom parser?

Pass `bodyLimit` in the parser options:

```js
app.addContentTypeParser(
  "text/csv",
  { parseAs: "string", bodyLimit: 10 * 1024 * 1024 },
  parseCsv,
);
```

When `parseAs` is set, Fastify reads the body for you and enforces the limit. If you read the stream yourself, you must check the size yourself.

## 194: What are custom log serializers?

Pino serializers decide how objects like `req`, `res` and `err` look in logs. You can override them:

```js
const app = Fastify({
  logger: {
    serializers: {
      req(request) {
        return {
          method: request.method,
          url: request.url,
          ip: request.ip,
          userAgent: request.headers["user-agent"],
        };
      },
    },
  },
});
```

Routes and plugins can also set `logSerializers` to change serializers for that part of the app.

## 195: How do you use a custom Pino instance?

Pass it with `loggerInstance`:

```js
import pino from "pino";

const logger = pino({ level: "info", base: { service: "orders" } });

const app = Fastify({ loggerInstance: logger });
```

In v5 `logger` only takes `true`, `false` or a config object. Passing a logger instance to `logger` was removed.

## 196: How do you change how request IDs are generated?

Use `genReqId`:

```js
import { randomUUID } from "node:crypto";

const app = Fastify({
  logger: true,
  genReqId: (req) => req.headers["x-request-id"] ?? randomUUID(),
});
```

`genReqId` receives the raw Node.js request. If you use an incoming header, remember a client can set it to anything, so validate it if it ends up in logs or other systems.

## 197: What does requestIdHeader do?

It tells Fastify to use the value of a header as the request ID:

```js
const app = Fastify({ requestIdHeader: "x-request-id" });
```

In v5 the default is `false`, so Fastify does not read any header unless you set this. When set, `genReqId` is only used if the header is missing.

## 198: How do you change the label of the request ID in logs?

By default the field is `reqId`. In v5 the recommended way is a `LogController`:

```js
import Fastify, { LogController } from "fastify";

const app = Fastify({
  logger: true,
  logController: new LogController({ requestIdLogLabel: "traceId" }),
});
```

The old top-level `requestIdLogLabel` option still works but is deprecated and will be removed in v6.

## 199: What is LogController?

`LogController` is a class exported by Fastify that controls Fastify's own log lines (incoming request, request completed, route not found and error logs). You can pass options to it or extend it and override methods like `incomingRequest` or `requestCompleted`:

```js
import Fastify, { LogController } from "fastify";

class QuietHealth extends LogController {
  constructor() {
    super({ disableRequestLogging: (req) => req.url === "/health" });
  }
}

const app = Fastify({ logger: true, logController: new QuietHealth() });
```

It replaces the top-level `disableRequestLogging` and `requestIdLogLabel` options, which are deprecated.

## 200: How do you log only slow requests?

Turn off the default request logs and add your own `onResponse` hook:

```js
const app = Fastify({
  logger: true,
  logController: new LogController({ disableRequestLogging: true }),
});

app.addHook("onResponse", async (request, reply) => {
  if (reply.elapsedTime > 500) {
    request.log.warn(
      { url: request.url, ms: reply.elapsedTime },
      "slow request",
    );
  }
});
```

## 201: How do you set the log level for one plugin?

Pass `logLevel` in the register options:

```js
app.register(noisyRoutes, { prefix: "/metrics", logLevel: "warn" });
```

All routes in that plugin use a logger with level `warn`.

## 202: What does trustProxy do?

When your app runs behind a proxy, the TCP connection comes from the proxy, not the client. `trustProxy` tells Fastify to read `X-Forwarded-For`, `X-Forwarded-Proto` and `X-Forwarded-Host` to fill `request.ip`, `request.ips`, `request.protocol` and `request.host`.

```js
const app = Fastify({ trustProxy: true });
```

It can be `true`, a number of hops, a list of IPs or CIDR ranges, or a function. Using `true` when the app is reachable without a proxy lets clients fake their IP, so a specific value is safer.

## 203: How do you set the number of trusted proxy hops?

Pass a number:

```js
const app = Fastify({ trustProxy: 1 });
```

With `1`, Fastify trusts only the last entry added by your one proxy. This is a good choice when you know there is exactly one load balancer in front of the app.

## 204: What is the difference between connectionTimeout, keepAliveTimeout and requestTimeout?

- `connectionTimeout` (default 0, off): the socket timeout. If no data is sent or received for this long, the socket is closed.
- `keepAliveTimeout` (default 72000 ms): how long an idle keep-alive connection is kept open after a response.
- `requestTimeout` (default 0, off): the maximum time to receive the whole request from the client. Setting it protects against slow clients.

There is also `handlerTimeout`, which limits the whole request lifecycle at the application level.

## 205: Why should keepAliveTimeout be higher than the load balancer's idle timeout?

If the app closes an idle connection at the same time the load balancer sends a new request on it, the request fails with a 502. Keep the app's keep-alive timeout longer than the load balancer's idle timeout. For example, AWS ALB defaults to 60 seconds, which is why Fastify's default of 72 seconds works well.

## 206: How do you do a graceful shutdown?

Listen for termination signals and call `app.close()`:

```js
const signals = ["SIGINT", "SIGTERM"];

for (const signal of signals) {
  process.once(signal, async () => {
    app.log.info({ signal }, "shutting down");
    try {
      await app.close();
      process.exit(0);
    } catch (err) {
      app.log.error(err);
      process.exit(1);
    }
  });
}
```

The package `close-with-grace` wraps this with a timeout and handles uncaught errors too.

## 207: What does return503OnClosing do?

When `close()` is called, Fastify keeps processing in-flight requests. With `return503OnClosing: true` (the default), any new request that arrives on an existing keep-alive connection during shutdown gets a 503 with a `Connection: close` header. This tells clients and load balancers to go elsewhere.

## 208: What does forceCloseConnections do?

It controls what happens to open connections on `close()`:

- `'idle'` (default when supported): idle keep-alive connections are closed right away; active ones are allowed to finish.
- `true`: all connections are destroyed, including active ones.
- `false`: Fastify waits for all connections to close on their own.

The default avoids shutdown hanging on idle keep-alive sockets.

## 209: What is the pluginTimeout option?

`pluginTimeout` (default 10000 ms) is the maximum time a plugin can take to load. If a plugin does not finish in time (for example it forgot to call `done` or its promise never resolves), Fastify throws `FST_ERR_PLUGIN_TIMEOUT` and names the plugin. Raise it if a plugin legitimately needs more time, like waiting for a slow database.

## 210: How do you find which plugin failed to load?

The error usually names the plugin. If it doesn't, give your plugins names with `fastify-plugin` or named functions, and print the plugin tree:

```js
await app.ready();
console.log(app.printPlugins());
```

Also check for plugins that mix `async` with `done`, or callback plugins that never call `done`.

## 211: What does findRoute() do?

`findRoute()` returns the route that would match a given method and URL pattern, with its params, or `null`:

```js
const route = app.findRoute({ method: "GET", url: "/users/:id" });
```

It is useful in tests and tooling. Like `hasRoute()`, it uses the route pattern.

## 212: How do you print the routes with more details?

`printRoutes()` takes options:

```js
console.log(
  app.printRoutes({
    commonPrefix: false,
    includeHooks: true,
    includeMeta: ["errorHandler"],
  }),
);
console.log(app.printRoutes({ method: "POST" }));
```

`commonPrefix: false` prints full paths instead of a compressed tree. `includeHooks` lists hooks on each route.

## 213: What are route constraints?

Constraints let you register the same path more than once and pick the handler based on something other than the URL, like the `Host` header or an `Accept-Version` header:

```js
app.get("/", { constraints: { host: "api.example.com" } }, apiHome);
app.get("/", { constraints: { host: "admin.example.com" } }, adminHome);
```

Fastify has built-in `host` and `version` constraints, and you can add your own.

## 214: How do you version routes with the Accept-Version header?

Use the `version` constraint:

```js
app.get("/users", { constraints: { version: "1.0.0" } }, async () => "v1");
app.get("/users", { constraints: { version: "2.0.0" } }, async () => "v2");
```

A request with `Accept-Version: 2.x` gets v2. Fastify also adds `Vary: Accept-Version` to the response. In v5 the old `version` route option was removed; use `constraints.version`.

Many APIs use URL versioning (`/v1`, `/v2`) instead, which you can do with prefixes.

## 215: How do you add a custom constraint?

Use `addConstraintStrategy`:

```js
app.addConstraintStrategy({
  name: "tenant",
  storage() {
    const map = new Map();
    return {
      get: (key) => map.get(key) ?? null,
      set: (key, value) => map.set(key, value),
    };
  },
  deriveConstraint: (req) => req.headers["x-tenant"],
  mustMatchWhenDerived: true,
});

app.get("/config", { constraints: { tenant: "acme" } }, acmeConfig);
```

## 216: How do you build URLs with a prefix in a reusable plugin?

Use `this.prefix` or `app.prefix` so the plugin works no matter where it is mounted:

```js
export default async function (app) {
  app.post("/", async (request, reply) => {
    const user = await createUser(request.body);
    reply.header("Location", `${app.prefix}/${user.id}`).code(201);
    return user;
  });
}
```

## 217: How do prefixes handle the "/" route?

If a plugin with prefix `/users` defines `app.get('/')`, Fastify registers both `/users` and `/users/` by default. The route option `prefixTrailingSlash` controls this: `'both'` (default), `'slash'` (only `/users/`) or `'no-slash'` (only `/users`).

## 218: How do you test plugins in isolation?

Create a small Fastify instance with only that plugin and the decorators it depends on:

```js
import { test } from "node:test";
import assert from "node:assert";
import Fastify from "fastify";
import usersRoutes from "../routes/users.js";

test("GET /users returns users", async (t) => {
  const app = Fastify();
  app.decorate("db", { users: { findMany: async () => [{ id: 1 }] } });
  app.register(usersRoutes, { prefix: "/users" });
  t.after(() => app.close());

  const res = await app.inject({ url: "/users" });
  assert.deepStrictEqual(res.json(), [{ id: 1 }]);
});
```

Faking a decorator like `db` is a simple way to mock dependencies.

## 219: How do you build the app for tests and production from the same code?

Put app setup in a function that returns the instance without listening:

```js
// app.js
import Fastify from "fastify";

export function buildApp(opts = {}) {
  const app = Fastify(opts);
  app.register(import("./plugins/db.js"));
  app.register(import("./routes/index.js"));
  return app;
}

// server.js
import { buildApp } from "./app.js";

const app = buildApp({ logger: true });
await app.listen({ port: Number(process.env.PORT) || 3000, host: "0.0.0.0" });
```

Tests call `buildApp()` and use `inject()`.

## 220: How do you send a POST with JSON in inject()?

Pass `payload` as an object, and inject sets the JSON content type:

```js
const res = await app.inject({
  method: "POST",
  url: "/users",
  payload: { name: "Ana" },
  headers: { authorization: `Bearer ${token}` },
});

assert.strictEqual(res.statusCode, 201);
```

You can also use `body` instead of `payload`, and `query` for query string values.

## 221: Can you chain inject() calls?

Yes, there is a chain API:

```js
const res = await app
  .inject()
  .post("/users")
  .headers({ "x-api-key": "test" })
  .payload({ name: "Ana" })
  .end();
```

It is the same as passing an options object. Use whichever reads better.

## 222: How do you test with a real HTTP server?

Listen on port 0 and use `fetch`:

```js
const address = await app.listen({ port: 0 });
const res = await fetch(`${address}/health`);
assert.strictEqual(res.status, 200);
await app.close();
```

This is useful for testing things `inject()` does not cover well, like real sockets, timeouts or WebSockets.

## 223: Which test runners work well with Fastify?

Any of them. Common choices:

- The Node.js built-in `node:test`, which the Fastify team uses in many of its own packages
- `tap` / `borp`
- Vitest
- Jest

What matters is that you create a fresh app per test or per file and close it after, so state and open handles do not leak between tests.

## 224: How do you mock an outgoing HTTP call in tests?

Use `undici`'s `MockAgent`, which works with Node's global `fetch`:

```js
import { MockAgent, setGlobalDispatcher } from "undici";

const agent = new MockAgent();
agent.disableNetConnect();
setGlobalDispatcher(agent);

agent
  .get("https://api.weather.com")
  .intercept({ path: "/today", method: "GET" })
  .reply(200, { temp: 21 });
```

Then call your Fastify route with `inject()`. For other HTTP clients, `nock` is a common choice.

## 225: How do you add authentication to many routes with @fastify/auth?

`@fastify/auth` combines several auth functions with OR or AND logic:

```js
import auth from "@fastify/auth";

await app.register(auth);

app.decorate("verifyJwt", async (request) => {
  await request.jwtVerify();
});

app.decorate("verifyApiKey", async (request) => {
  if (request.headers["x-api-key"] !== process.env.API_KEY) {
    throw new Error("Invalid API key");
  }
});

app.get(
  "/data",
  {
    onRequest: app.auth([app.verifyJwt, app.verifyApiKey]),
  },
  async () => "secret",
);
```

By default it passes if any function succeeds. Use `{ relation: 'and' }` to require all.

## 226: How do you write an authenticate decorator with @fastify/jwt?

```js
import fp from "fastify-plugin";
import jwt from "@fastify/jwt";

export default fp(
  async (app) => {
    app.register(jwt, { secret: app.config.JWT_SECRET });

    app.decorate("authenticate", async (request, reply) => {
      try {
        await request.jwtVerify();
      } catch {
        return reply.code(401).send({ message: "Unauthorized" });
      }
    });
  },
  { name: "auth" },
);
```

```js
app.get(
  "/me",
  { onRequest: [app.authenticate] },
  async (request) => request.user,
);
```

## 227: How do you read a JWT from a cookie with @fastify/jwt?

Register `@fastify/cookie` and pass the cookie option:

```js
app.register(cookie);
app.register(jwt, {
  secret: process.env.JWT_SECRET,
  cookie: { cookieName: "token", signed: false },
});

app.post("/login", async (request, reply) => {
  const token = await reply.jwtSign({ sub: "user-1" });
  reply.setCookie("token", token, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
  });
  return { ok: true };
});
```

`request.jwtVerify()` will now read the token from the cookie when there is no `Authorization` header.

## 228: How do you add role-based access checks?

Use route config plus a hook:

```js
app.addHook("preHandler", async (request, reply) => {
  const roles = request.routeOptions.config.roles;
  if (!roles) return;
  if (!request.user || !roles.includes(request.user.role)) {
    return reply.code(403).send({ message: "Forbidden" });
  }
});

app.delete(
  "/users/:id",
  {
    onRequest: [app.authenticate],
    config: { roles: ["admin"] },
  },
  deleteUser,
);
```

## 229: What is the difference between @fastify/session and @fastify/secure-session?

- `@fastify/session` stores session data on the server (in memory by default, or in Redis or another store) and sends only a session ID in a cookie. You can revoke sessions and store large data.
- `@fastify/secure-session` stores the whole session in an encrypted cookie (libsodium). No server storage is needed, but the cookie size limits how much you can store, and you cannot revoke one session without rotating the key.

Never use the default memory store of `@fastify/session` in production.

## 230: How do you set up server-side sessions with Redis?

```js
import cookie from "@fastify/cookie";
import session from "@fastify/session";
import { RedisStore } from "connect-redis";
import { Redis } from "ioredis";

const redis = new Redis(process.env.REDIS_URL);

app.register(cookie);
app.register(session, {
  secret: process.env.SESSION_SECRET, // at least 32 characters
  cookie: { secure: true, httpOnly: true, sameSite: "lax", maxAge: 86400000 },
  store: new RedisStore({ client: redis }),
  saveUninitialized: false,
});

app.post("/login", async (request) => {
  request.session.userId = "user-1";
  return { ok: true };
});
```

## 231: How do you protect against CSRF?

Use `@fastify/csrf-protection` with cookies or sessions:

```js
import csrf from "@fastify/csrf-protection";

await app.register(cookie);
await app.register(csrf, { cookieOpts: { signed: true } });

app.get("/form", async (request, reply) => {
  const token = reply.generateCsrf();
  return { token };
});

app.post("/transfer", { onRequest: app.csrfProtection }, async () => "done");
```

APIs that only use `Authorization` headers (not cookies) are not exposed to CSRF in the same way, so they usually do not need this.

## 232: How do you proxy requests to another service?

Use `@fastify/http-proxy`:

```js
import proxy from "@fastify/http-proxy";

app.register(proxy, {
  upstream: "http://users-service:3001",
  prefix: "/users",
  rewritePrefix: "/api/users",
});
```

A request to `/users/42` goes to `http://users-service:3001/api/users/42`. For full control from a handler, use `@fastify/reply-from` and call `reply.from(url)`.

## 233: How do you send Server-Sent Events?

Write to the raw response after hijacking:

```js
app.get("/events", (request, reply) => {
  reply.hijack();
  reply.raw.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });

  const timer = setInterval(() => {
    reply.raw.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  request.raw.on("close", () => clearInterval(timer));
});
```

You can also send a readable stream, or use a community plugin like `fastify-sse-v2`.

## 234: Can you return a Web ReadableStream or a Response object?

Yes. `reply.send()` accepts a Web `ReadableStream` and a Web `Response`:

```js
app.get("/proxy", async (request, reply) => {
  const upstream = await fetch("https://example.com/data.json");
  return reply.send(upstream);
});
```

With a `Response`, Fastify copies the status and headers and streams the body. This is handy when your handler already uses `fetch`.

## 235: How do you add ETag support?

Use `@fastify/etag`:

```js
import etag from "@fastify/etag";

app.register(etag);
```

It hashes the response body and adds an `ETag` header. If the client sends a matching `If-None-Match`, it replies with 304 and no body, saving bandwidth.

## 236: How do you set caching headers per route?

Set them in the handler or use `@fastify/caching`:

```js
app.get("/countries", async (request, reply) => {
  reply.header("Cache-Control", "public, max-age=3600");
  return countries;
});
```

For a shared default, `@fastify/caching` lets you set `privacy` and `expiresIn` globally and adds an in-memory cache on `app.cache`.

## 237: How do you implement pagination with validation?

```js
const paginationSchema = {
  type: "object",
  properties: {
    page: { type: "integer", minimum: 1, default: 1 },
    pageSize: { type: "integer", minimum: 1, maximum: 100, default: 20 },
  },
};

app.get(
  "/products",
  { schema: { querystring: paginationSchema } },
  async (request) => {
    const { page, pageSize } = request.query;
    const offset = (page - 1) * pageSize;
    const [items, total] = await Promise.all([
      app.db.products.list({ limit: pageSize, offset }),
      app.db.products.count(),
    ]);
    return { items, total, page, pageSize };
  },
);
```

## 238: How do you use Prisma with Fastify?

Wrap the client in a plugin:

```js
import fp from "fastify-plugin";
import { PrismaClient } from "@prisma/client";

export default fp(
  async (app) => {
    const prisma = new PrismaClient();
    await prisma.$connect();

    app.decorate("prisma", prisma);

    app.addHook("onClose", async (instance) => {
      await instance.prisma.$disconnect();
    });
  },
  { name: "prisma" },
);
```

Then use `app.prisma` or `request.server.prisma` in routes.

## 239: How do you structure a medium-size Fastify project?

A common layout:

```
src/
  app.js            # builds the instance
  server.js         # starts listening
  plugins/          # shared plugins (db, auth, config), wrapped with fastify-plugin
  routes/
    users/
      index.js      # route definitions
      schemas.js    # JSON schemas for these routes
    orders/
      index.js
  services/         # business logic, no Fastify imports
test/
```

`@fastify/autoload` loads `plugins/` and `routes/`. Keeping business logic in plain modules makes it easier to test without HTTP.

## 240: How do you share schemas between files with $ref?

Register them once with `addSchema`, using `$id`, and reference them:

```js
// plugins/schemas.js (wrapped with fastify-plugin)
app.addSchema({
  $id: 'common',
  type: 'object',
  definitions: {
    id: { type: 'string', format: 'uuid' },
    error: {
      type: 'object',
      properties: { message: { type: 'string' } }
    }
  }
})

// routes
schema: {
  params: {
    type: 'object',
    properties: { id: { $ref: 'common#/definitions/id' } }
  },
  response: { 404: { $ref: 'common#/definitions/error' } }
}
```

## 241: What do getSchema and getSchemas return?

`app.getSchemas()` returns all schemas added with `addSchema` in the current context (including parents). `app.getSchema(id)` returns one by its `$id`. Like everything else, schemas follow encapsulation: a schema added in a child plugin is not visible to the parent.

## 242: How can you use TypeBox schemas without the type provider?

TypeBox produces plain JSON Schema objects, so Fastify can use them directly:

```js
import { Type } from "typebox";

const User = Type.Object({
  id: Type.Integer(),
  name: Type.String(),
});

app.get("/users/:id", { schema: { response: { 200: User } } }, getUser);
```

The type provider only adds TypeScript inference. Validation and serialization work the same either way.

## 243: What is fluent-json-schema?

`fluent-json-schema` is a builder for JSON Schema with a chained API, maintained by the Fastify team:

```js
import S from "fluent-json-schema";

const bodySchema = S.object()
  .prop("email", S.string().format(S.FORMATS.EMAIL).required())
  .prop("age", S.integer().minimum(18));

app.post("/signup", { schema: { body: bodySchema } }, signup);
```

It is an option if you write JavaScript and find raw JSON Schema too long. In TypeScript projects TypeBox is more common because it also gives types.

## 244: How do you add custom Ajv keywords or plugins?

Use `ajv.plugins` in the server options:

```js
import ajvErrors from "ajv-errors";

const app = Fastify({
  ajv: {
    customOptions: { allErrors: true },
    plugins: [ajvErrors],
  },
});

app.post(
  "/x",
  {
    schema: {
      body: {
        type: "object",
        required: ["age"],
        properties: { age: { type: "integer", minimum: 18 } },
        errorMessage: { properties: { age: "You must be at least 18" } },
      },
    },
  },
  handler,
);
```

`ajv-errors` needs `allErrors: true`.

## 245: How do you change Ajv options like coerceTypes?

Pass `ajv.customOptions`:

```js
const app = Fastify({
  ajv: {
    customOptions: {
      coerceTypes: false,
      removeAdditional: "all",
      useDefaults: true,
    },
  },
});
```

These replace Fastify's defaults (`coerceTypes: 'array'`, `useDefaults: true`, `removeAdditional: true`, `allErrors: false`) for the options you set.

## 246: Why might coerceTypes cause surprises?

Coercion changes your data quietly. For example, with a body schema of `{ type: 'integer' }`, the JSON string `"42"` becomes `42`, and `"true"` can become `true` for a boolean field. Some teams want JSON bodies to be strict and only coerce query strings and params. To do that, use a custom validator compiler with different Ajv instances per part of the request.

## 247: Does Fastify validate response data against the response schema?

No. The response schema is used for serialization, not validation. If a required field is missing, `fast-json-stringify` throws a serialization error, but types are coerced and extra fields are dropped without any error. If you want strict response checks (for example in tests), add a validator like `@fastify/response-validation`.

## 248: What happens when a response object does not match the response schema types?

`fast-json-stringify` tries to coerce. For example, a number `5` for a `string` field becomes `"5"`, and a string `"abc"` for an `integer` field can throw a serialization error. Missing required fields throw. Extra fields are dropped. This is why response schemas should match your real data closely.

## 249: How do you skip the response schema for one route?

Do not set `response` in the schema. Or, to force plain `JSON.stringify` for a reply, use `reply.serializer(JSON.stringify)`:

```js
app.get(
  "/raw",
  { schema: { response: { 200: userSchema } } },
  async (request, reply) => {
    reply.serializer(JSON.stringify);
    return bigObject;
  },
);
```

## 250: What is setReplySerializer?

It sets the default serializer for replies that have no response schema in the current context:

```js
app.setReplySerializer((payload, statusCode) => {
  return JSON.stringify({ status: statusCode, data: payload });
});
```

Routes with a response schema still use the compiled serializer for that schema.

## 251: How do you handle content negotiation for different formats?

Check the `Accept` header and serialize based on it. You can use `@fastify/accepts`:

```js
import accepts from "@fastify/accepts";

app.register(accepts);

app.get("/report", async (request, reply) => {
  const type = request.accepts().type(["json", "csv"]);
  if (type === "csv") {
    reply.type("text/csv");
    return toCsv(data);
  }
  return data;
});
```

Response schemas can also be set per content type using the `content` key under a status code.

## 252: How do you set a response schema per content type?

```js
schema: {
  response: {
    200: {
      content: {
        'application/json': { schema: { type: 'object', properties: { id: { type: 'integer' } } } },
        'text/plain': { schema: { type: 'string' } }
      }
    }
  }
}
```

Fastify picks the schema based on the `Content-Type` the reply ends up with.

## 253: How do you handle multipart fields and files together?

```js
app.post("/profile", async (request) => {
  const parts = request.parts();
  const fields = {};
  const files = [];

  for await (const part of parts) {
    if (part.type === "file") {
      const name = `${randomUUID()}.bin`;
      await pipeline(part.file, fs.createWriteStream(`./uploads/${name}`));
      files.push(name);
    } else {
      fields[part.fieldname] = part.value;
    }
  }
  return { fields, files };
});
```

You must consume every file stream, or the request will hang.

## 254: What does attachFieldsToBody do in @fastify/multipart?

With `attachFieldsToBody: true`, the plugin parses the whole multipart body and puts fields and files on `request.body`, so you can use a JSON Schema for the body:

```js
app.register(multipart, { attachFieldsToBody: "keyValues" });
```

With `'keyValues'`, fields become plain values and files become buffers. This is simple but loads files into memory, so it is only good for small files.

## 255: How do you limit file size and count with multipart?

Pass `limits`:

```js
app.register(multipart, {
  limits: {
    fileSize: 5 * 1024 * 1024,
    files: 3,
    fields: 20,
  },
});
```

When a file is too big, `data.file.truncated` becomes `true`, or an error is thrown when using `toBuffer()` or `saveRequestFiles()`. Always check limits before trusting an upload.

## 256: How do you migrate an Express app to Fastify step by step?

1. Create a Fastify app and register `@fastify/express`.
2. Mount the existing Express app or router with `app.use(expressApp)`.
3. Move routes one by one to native Fastify routes, adding schemas as you go.
4. Replace Express middleware with Fastify plugins and hooks (`cors`, `helmet`, auth).
5. Remove `@fastify/express` once everything is moved.

This lets you ship along the way instead of doing one big rewrite.

## 257: How do Express middleware concepts map to Fastify?

| Express                                  | Fastify                                        |
| ---------------------------------------- | ---------------------------------------------- |
| `app.use(mw)` (global)                   | `addHook('onRequest', ...)` in a shared plugin |
| Router                                   | Plugin with `prefix`                           |
| Error middleware `(err, req, res, next)` | `setErrorHandler`                              |
| `req.body` via body-parser               | Built in for JSON                              |
| `res.json()`                             | `return obj` or `reply.send(obj)`              |
| `res.status(201)`                        | `reply.code(201)`                              |
| `req.app.locals`                         | `app.decorate()`                               |

## 258: What are the main breaking changes when upgrading from v4 to v5?

- Node.js 20+ is required.
- Full JSON Schema is required for `querystring`, `params`, `body` and `response`.
- `logger` no longer accepts an instance; use `loggerInstance`.
- `listen()` only accepts an options object.
- `reply.redirect(url, code)` has the arguments in a new order.
- `request.routerPath`, `routeConfig`, `routeSchema`, `context` are replaced by `request.routeOptions`.
- `request.connection` is removed; use `request.socket`.
- `reply.getResponseTime()` is replaced by `reply.elapsedTime`.
- `request.hostname` no longer includes the port.
- `useSemicolonDelimiter` defaults to `false`.
- Decorating request or reply with objects or arrays is not allowed.
- Plugins cannot mix `async` and `done`.

## 259: How should you approach a v4 to v5 upgrade?

1. Upgrade to the last v4 version and fix all deprecation warnings first. Anything deprecated in v4 is gone in v5.
2. Upgrade Node.js to 20 or newer.
3. Upgrade every `@fastify/*` plugin to the version that supports v5.
4. Upgrade Fastify and go through the migration guide.
5. Run the tests, paying attention to schemas, `hostname`, redirects and logger setup.

## 260: Why was useSemicolonDelimiter changed to false?

In v4, Fastify treated `;` as a query string separator by default, so `/path?a=1;b=2` gave two params. That is not standard behavior and can cause bugs or security issues where a proxy and the app parse a URL differently. In v5 the default is `false`. You can turn it back on with `routerOptions: { useSemicolonDelimiter: true }`.

## 261: Why does req.params no longer have a prototype in v5?

`request.params` is created with `Object.create(null)`. This prevents prototype pollution through param names and makes lookups safer. The side effect is that `request.params.hasOwnProperty('id')` throws. Use `Object.hasOwn(request.params, 'id')` instead.

## 262: How do you use a custom query string parser?

Set `querystringParser` in `routerOptions`:

```js
import qs from "qs";

const app = Fastify({
  routerOptions: {
    querystringParser: (str) => qs.parse(str, { allowDots: true }),
  },
});
```

With `qs`, `?filter[status]=active&filter[type]=a` becomes `{ filter: { status: 'active', type: 'a' } }`. Remember to limit depth and array size, since nested parsing can be abused.

## 263: What does maxParamLength do?

It limits the length of each URL param (default 100 characters). If a param is longer, the route does not match and the client gets a 404 (or your `onMaxParamLength` handler runs). This protects the router from very long, slow-to-match URLs. Set it in `routerOptions`.

## 264: What is rewriteUrl?

`rewriteUrl` is a server option that changes the URL before routing. It gets the raw request and returns the new URL:

```js
const app = Fastify({
  rewriteUrl(req) {
    return req.url.startsWith("/api/v1")
      ? req.url.replace("/api/v1", "/api")
      : req.url;
  },
});
```

It runs before any hooks. The original URL is kept in `request.originalUrl`.

## 265: What is frameworkErrors used for?

It lets you handle errors that Fastify raises before your route runs, like a bad URL or a too-long param, which normally use a default response:

```js
const app = Fastify({
  frameworkErrors(error, request, reply) {
    reply.code(400).send({ message: "Bad request", code: error.code });
  },
});
```

Only some errors go here (`FST_ERR_BAD_URL`, `FST_ERR_ASYNC_CONSTRAINT` and similar).

## 266: What is clientErrorHandler?

It handles `clientError` events from the Node.js server, which happen on broken HTTP requests like malformed headers. The default sends a 400 and closes the socket. You can provide your own function `(err, socket) => {}`. At this point there is no `request` or `reply`, only the raw socket.

## 267: How do you serve a single-page app and API routes from one Fastify app with fallback?

```js
app.register(fastifyStatic, {
  root: path.join(import.meta.dirname, "dist"),
  wildcard: false,
});

app.register(apiRoutes, { prefix: "/api" });

app.setNotFoundHandler(async (request, reply) => {
  if (request.method === "GET" && !request.url.startsWith("/api")) {
    return reply.sendFile("index.html");
  }
  return reply.code(404).send({ message: "Not found" });
});
```

`wildcard: false` makes `@fastify/static` register a route per file at startup instead of a wildcard, so unmatched paths fall to the not-found handler.

## 268: How do you use different not-found handlers for different prefixes?

Call `setNotFoundHandler` inside plugins with a prefix:

```js
app.register(
  async (api) => {
    api.setNotFoundHandler((request, reply) => {
      reply.code(404).send({ error: "API route not found" });
    });
    api.register(apiRoutes);
  },
  { prefix: "/api" },
);
```

Unmatched URLs under `/api` use this handler. Other unmatched URLs use the root one.

## 269: Can hooks run on the not-found handler?

Yes, hooks registered in the context where `setNotFoundHandler` is called run for 404 requests too. You can also pass hooks directly:

```js
app.setNotFoundHandler(
  {
    preHandler: app.rateLimit(),
  },
  (request, reply) => {
    reply.code(404).send({ message: "Not found" });
  },
);
```

Rate limiting 404s helps against scanners.

## 270: How do you call the not-found handler from a route?

Use `reply.callNotFound()`:

```js
app.get("/files/:name", async (request, reply) => {
  const exists = await fileExists(request.params.name);
  if (!exists) return reply.callNotFound();
  return reply.sendFile(request.params.name);
});
```

This keeps 404 responses consistent with the rest of the app.

## 271: How do you register a WebSocket route that requires auth?

Hooks run before the upgrade, so `onRequest` or `preValidation` can reject the request:

```js
app.register(async (ws) => {
  ws.addHook("preValidation", async (request, reply) => {
    try {
      await request.jwtVerify();
    } catch {
      return reply.code(401).send({ message: "Unauthorized" });
    }
  });

  ws.get("/chat", { websocket: true }, (socket, request) => {
    socket.send(`hello ${request.user.sub}`);
  });
});
```

Browsers cannot set custom headers on WebSocket connections, so tokens are often sent in a cookie or a query param.

## 272: How do you broadcast a message to all WebSocket clients?

Use `app.websocketServer.clients`:

```js
function broadcast(message) {
  for (const client of app.websocketServer.clients) {
    if (client.readyState === 1) {
      client.send(message);
    }
  }
}
```

This only reaches clients connected to this process. With several instances you need a pub/sub system like Redis to share messages.

## 273: How do you add OpenAPI security schemes with @fastify/swagger?

```js
await app.register(swagger, {
  openapi: {
    info: { title: "API", version: "1.0.0" },
    components: {
      securitySchemes: {
        bearerAuth: { type: "http", scheme: "bearer", bearerFormat: "JWT" },
      },
    },
    security: [{ bearerAuth: [] }],
  },
});

app.get("/public", { schema: { security: [] } }, publicHandler);
```

An empty `security` array on a route marks it as public in the docs.

## 274: How do you make @fastify/swagger use your shared $ref schemas?

Schemas added with `addSchema` are included in `components.schemas`. Give them an `$id` and optionally a `title`. Set `refResolver.buildLocalReference` if you want custom names:

```js
await app.register(swagger, {
  openapi: { info: { title: "API", version: "1.0.0" } },
  refResolver: {
    buildLocalReference(json, baseUri, fragment, i) {
      return json.$id || `def-${i}`;
    },
  },
});
```

## 275: How do you load env config before other plugins need it?

Register `@fastify/env` first and await it, or rely on plugin order:

```js
await app.register(fastifyEnv, { schema: envSchema, dotenv: true });

app.register(dbPlugin); // can use app.config.DATABASE_URL
```

Since `@fastify/env` is not encapsulated, `app.config` is available to every plugin registered after it.

## 276: How do you use dependency injection in Fastify?

Most apps use decorators as a simple form of DI: plugins put services on the instance, and routes use them. For a real DI container, `@fastify/awilix` integrates Awilix:

```js
import { fastifyAwilixPlugin, diContainer } from "@fastify/awilix";
import { asClass, Lifetime } from "awilix";

app.register(fastifyAwilixPlugin);

diContainer.register({
  userService: asClass(UserService, { lifetime: Lifetime.SINGLETON }),
});

app.get("/users", async (request) => {
  return request.diScope.resolve("userService").list();
});
```

## 277: How do you store data per request without passing it around?

Use `@fastify/request-context`, which uses `AsyncLocalStorage`:

```js
import {
  fastifyRequestContext,
  requestContext,
} from "@fastify/request-context";

app.register(fastifyRequestContext);

app.addHook("onRequest", async (request) => {
  request.requestContext.set("userId", request.headers["x-user-id"]);
});

// deep in a service, no request needed
export function audit(action) {
  const userId = requestContext.get("userId");
  console.log(userId, action);
}
```

## 278: How do you run a database transaction per request?

Start it in a hook and commit or roll back at the end, or simply wrap the handler code:

```js
app.post("/transfer", async (request) => {
  return app.prisma.$transaction(async (tx) => {
    await tx.account.update({
      where: { id: request.body.from },
      data: { balance: { decrement: request.body.amount } },
    });
    await tx.account.update({
      where: { id: request.body.to },
      data: { balance: { increment: request.body.amount } },
    });
    return { ok: true };
  });
});
```

Wrapping only the routes that need it is simpler and avoids holding transactions open for read-only requests.

## 279: How do you add request timing headers for debugging?

```js
app.addHook("onSend", async (request, reply, payload) => {
  reply.header("Server-Timing", `app;dur=${reply.elapsedTime.toFixed(1)}`);
  return payload;
});
```

Browsers show `Server-Timing` in the network tab, which helps when debugging slow pages.

## 280: How do you write a plugin that works for both v4 and v5?

It is usually not worth it. The official plugins publish separate major versions per Fastify major. If you must, avoid APIs that changed (`routerPath`, `getResponseTime`, `redirect` arg order) and set `fastify: '4.x || 5.x'` in `fastify-plugin` metadata. Test against both versions in CI.

## 281: What is the then() method on reply used for?

`reply` is thenable. Awaiting it resolves when the response is finished sending, and rejects if writing fails:

```js
app.get("/", async (request, reply) => {
  reply.send(bigPayload);
  await reply;
  request.log.info("response sent");
});
```

## 282: How do you send HTTP trailers?

Use `reply.trailer()` with an async function:

```js
app.get("/data", async (request, reply) => {
  reply.trailer("Server-Timing", async () => `total;dur=${reply.elapsedTime}`);
  return largeData;
});
```

Trailers are sent after the body, so they only work with chunked transfer encoding. In v5 trailer functions must be async or use a callback; returning the value directly is not allowed.

## 283: What is reply.writeEarlyHints()?

It sends a `103 Early Hints` response so the browser can start loading resources while the server is still building the page:

```js
app.get("/", async (request, reply) => {
  reply.writeEarlyHints({
    Link: "</style.css>; rel=preload; as=style",
  });
  return renderPage();
});
```

The final response is sent as usual after it. You can pass a callback as the second argument to know when the hints were written.

## 284: How do you check if a header is already set on the reply?

Use `reply.hasHeader()`, `reply.getHeader()` and `reply.getHeaders()`:

```js
app.addHook("onSend", async (request, reply, payload) => {
  if (!reply.hasHeader("Cache-Control")) {
    reply.header("Cache-Control", "no-store");
  }
  return payload;
});
```

`reply.removeHeader()` removes one.

## 285: How do you add a route with the same handler for GET and POST?

Use `route()` with an array of methods:

```js
app.route({
  method: ["GET", "POST"],
  url: "/search",
  handler: async (request) => {
    const params = request.method === "GET" ? request.query : request.body;
    return search(params);
  },
});
```

## 286: Why do you get FST_ERR_DUPLICATED_ROUTE?

You registered the same method and path twice in the same router, with the same constraints. It often happens when a plugin is registered twice or two route files define the same path. Check with `printRoutes()`. Encapsulation does not help here, since all contexts share one router.

## 287: How do you get the matched route pattern for metrics?

Use `request.routeOptions.url`, not `request.url`:

```js
app.addHook("onResponse", async (request, reply) => {
  metrics.observe(
    {
      route: request.routeOptions.url ?? "not_found",
      method: request.method,
      status: reply.statusCode,
    },
    reply.elapsedTime,
  );
});
```

Using the real URL creates a new label per user ID or param value, which can blow up your metrics storage.

## 288: How do you expose Prometheus metrics?

The community plugin `fastify-metrics` adds route timing histograms and a `/metrics` endpoint using `prom-client`:

```js
import metricsPlugin from "fastify-metrics";

await app.register(metricsPlugin, { endpoint: "/metrics" });
```

It uses the route pattern as a label by default. Protect `/metrics` or expose it on a separate port in production.

## 289: How do you run Fastify in Docker the right way?

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
ENV NODE_ENV=production
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

Key points: listen on `0.0.0.0`, run `node` directly (not `npm start`) so `SIGTERM` reaches the app, handle shutdown with `app.close()`, and run as a non-root user.

## 290: How do you serve compressed static files that are already built?

`@fastify/static` can serve pre-compressed files:

```js
app.register(fastifyStatic, {
  root: path.join(import.meta.dirname, "dist"),
  preCompressed: true,
});
```

If `app.js.br` or `app.js.gz` exists next to `app.js` and the client accepts it, that file is sent. This avoids compressing on every request.

## 291: How do you set different body limits for different content types?

Set `bodyLimit` on the content type parser or on the route:

```js
app.post("/upload-json", { bodyLimit: 10 * 1024 * 1024 }, handler);

app.addContentTypeParser(
  "text/csv",
  { parseAs: "string", bodyLimit: 50 * 1024 * 1024 },
  csvParser,
);
```

The route's `bodyLimit` wins over the server default.

## 292: How do you use the async iterator style with request.files()?

```js
app.post("/batch-upload", async (request) => {
  const saved = [];
  for await (const file of request.files()) {
    const name = `${randomUUID()}${path.extname(file.filename)}`;
    await pipeline(
      file.file,
      fs.createWriteStream(path.join(UPLOAD_DIR, name)),
    );
    saved.push(name);
  }
  return { saved };
});
```

Each file must be fully consumed before the loop continues to the next one.

## 293: How do you define a route schema in a separate file?

```js
// routes/users/schemas.js
export const createUserSchema = {
  body: {
    type: "object",
    required: ["email"],
    properties: { email: { type: "string", format: "email" } },
  },
  response: {
    201: {
      type: "object",
      properties: { id: { type: "string" }, email: { type: "string" } },
    },
  },
};

// routes/users/index.js
import { createUserSchema } from "./schemas.js";

export default async function (app) {
  app.post("/", { schema: createUserSchema }, createUser);
}
```

## 294: How do you validate that two fields match, like password and confirmPassword?

JSON Schema has no simple way to compare two fields. Use a `preHandler` or check in the handler:

```js
app.post(
  "/register",
  {
    schema: { body: registerSchema },
    preHandler: async (request, reply) => {
      if (request.body.password !== request.body.confirmPassword) {
        return reply.code(400).send({ message: "Passwords do not match" });
      }
    },
  },
  register,
);
```

Ajv's `$data` option can do some cross-field checks, but it is harder to read.

## 295: How do you run code once on startup that needs all plugins loaded?

Use an `onReady` hook or `await app.ready()` before `listen()`:

```js
app.addHook("onReady", async function () {
  await this.cache.warmUp();
});
```

`onReady` is better in a plugin because the plugin owns its setup, and tests that call `ready()` will run it too.

## 296: How do you send a 201 with a Location header?

```js
app.post("/articles", async (request, reply) => {
  const article = await createArticle(request.body);
  return reply
    .code(201)
    .header("Location", `/articles/${article.id}`)
    .send(article);
});
```

## 297: How do you handle errors thrown inside setTimeout in a handler?

Fastify can only catch errors from the handler's promise chain. An error thrown inside a plain `setTimeout` callback is outside that chain and will crash the process as an uncaught exception. Use promise-based timers instead:

```js
import { setTimeout as sleep } from "node:timers/promises";

app.get("/delayed", async () => {
  await sleep(100);
  throw new Error("caught by Fastify");
});
```

## 298: How do you implement a simple API key check for a group of routes?

```js
app.register(
  async (partner) => {
    partner.addHook("onRequest", async (request, reply) => {
      const key = request.headers["x-api-key"];
      const partnerInfo = key && (await partner.db.partners.findByKey(key));
      if (!partnerInfo) {
        return reply.code(401).send({ message: "Invalid API key" });
      }
      request.partner = partnerInfo;
    });

    partner.get("/orders", listPartnerOrders);
  },
  { prefix: "/partner" },
);
```

Decorate `partner` on the request first (`app.decorateRequest('partner', null)`) to keep the request shape stable. Compare keys stored as hashes rather than plain text.

## 299: How do you log the request body for debugging only?

Use a `preHandler` hook at `debug` level, so it is off by default in production:

```js
app.addHook("preHandler", async (request) => {
  request.log.debug({ body: request.body }, "request body");
});
```

Combine it with `redact` for fields like passwords, and never log full bodies at `info` in production.

## 300: How do you handle CORS preflight for a route with custom headers?

`@fastify/cors` handles `OPTIONS` preflight requests for you. Make sure the custom headers and methods are allowed:

```js
await app.register(cors, {
  origin: ["https://app.example.com"],
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization", "X-Request-Id"],
  exposedHeaders: ["X-Total-Count"],
  maxAge: 600,
});
```

`exposedHeaders` lists response headers the browser JavaScript is allowed to read. `maxAge` lets the browser cache the preflight result.

# Advanced Questions (301-450)

## 301: How does Fastify load plugins internally?

Fastify uses a library called `avvio` to load plugins. When you call `register()`, the plugin is added to a queue instead of running right away. When `ready()`, `listen()` or `await register()` is called, avvio runs the plugins one by one in order. Each plugin can register more plugins, which are loaded before avvio moves on to the next sibling. This builds a tree, and the order is depth-first.

This is why plugins are always loaded in a predictable order, and why a plugin can rely on everything registered before it.

## 302: How is encapsulation implemented under the hood?

When a plugin is registered, Fastify creates a child instance with `Object.create(parent)`. The child inherits everything from the parent through the prototype chain, but new properties set on the child (decorators, hooks arrays, schemas, error handler) do not affect the parent.

Things like hooks and content type parsers are copied into new arrays or objects for the child, so adding a hook in the child does not change the parent's list.

## 303: How does fastify-plugin skip encapsulation internally?

`fastify-plugin` sets a special symbol, `Symbol.for('skip-override')`, on the plugin function. When avvio sees it, Fastify does not create a child instance and passes the parent instance to the plugin directly. Everything the plugin adds lands on the parent.

It also sets `Symbol.for('fastify.display-name')` and the plugin metadata used for dependency and version checks.

## 304: Why do decorators help performance?

V8 optimizes code based on the "shape" (hidden class) of objects. If every request object has the same set of properties in the same order, V8 can use fast property access.

Fastify builds a `Request` and `Reply` constructor per context, with all decorators defined up front. Every request object created in that context has the same shape. If you add properties to `request` at random inside handlers, objects end up with different shapes and V8 falls back to slower lookups. This is also why decorating after start is not allowed.

## 305: Why can't you decorate request or reply with an object value in v5?

The decorator value is set on the prototype, so every request would share the same object. If one request does `request.cache.user = x`, every other request sees it. This leaked data between users in real apps. v5 throws `FST_ERR_DEC_REFERENCE_TYPE` for objects and arrays. Use `null` and set the value in a hook, or use a getter.

## 306: How does find-my-way route matching work?

`find-my-way` stores routes in a radix tree (a compressed prefix tree), one per HTTP method. Static parts of paths share nodes, and params and wildcards are special node types. Matching walks the tree character by character, so the cost depends on the URL length, not the number of routes.

Static routes are checked before param routes, and param routes before wildcards. So `/users/me` wins over `/users/:id` regardless of registration order.

## 307: Why are regex params slower and what are the risks?

A regex param is checked by running the regular expression against that part of the URL, which is slower than a plain tree lookup. The bigger risk is ReDoS: a badly written regex with nested quantifiers can take exponential time on a crafted input.

By default `find-my-way` rejects unsafe regexes using `safe-regex2` (`allowUnsafeRegex: false`). Prefer simple patterns, or a plain param plus schema validation.

## 308: How does fast-json-stringify make serialization faster?

At startup, `fast-json-stringify` reads the response schema and generates a JavaScript function that writes JSON for exactly that shape. Instead of `JSON.stringify` walking every key and checking every type at runtime, the generated code knows which keys exist and what type each has:

```js
// roughly what gets generated for { id: integer, name: string }
function serialize(obj) {
  return '{"id":' + asInteger(obj.id) + ',"name":' + asString(obj.name) + "}";
}
```

The gain is biggest for objects with many known fields. For objects with `additionalProperties` or complex `anyOf`, the gain is smaller.

## 309: Are there cases where fast-json-stringify is slower than JSON.stringify?

Yes. Schemas with heavy `anyOf` or `oneOf` need to check the data against each branch at runtime using Ajv, which can be slower than plain `JSON.stringify`. Very large arrays of simple values and schemas with `additionalProperties: true` also gain less. Always benchmark if serialization is on a hot path.

## 310: How are validation functions compiled and when?

Fastify compiles a validation function for every schema part of every route (body, params, querystring, headers) with Ajv when the route is registered, during startup. At request time, it just calls the compiled function. Compiling is relatively slow, which is why apps with hundreds of routes and big schemas can take a while to start.

## 311: How do you reduce startup time caused by schema compilation?

A few options:

- Share schemas with `addSchema` and `$ref` so they are compiled once.
- Use standalone mode: generate validation and serialization code at build time and load it at startup. `@fastify/ajv-compiler` and `@fastify/fast-json-stringify-compiler` support this.
- Lazy load rarely used parts of the app in separate plugins.

Standalone mode is common for serverless, where cold start time matters.

## 312: What is the schemaController option?

`schemaController` lets you replace how Fastify stores schemas and which compilers it uses:

```js
const app = Fastify({
  schemaController: {
    bucket: (parentSchemas) => myBucket(parentSchemas),
    compilersFactory: {
      buildValidator: myValidatorFactory,
      buildSerializer: mySerializerFactory,
    },
  },
});
```

- `bucket` stores schemas added with `addSchema` per context.
- `compilersFactory` builds the validator and serializer compilers, for example to use standalone precompiled code.

## 313: How does setValidatorCompiler work?

`setValidatorCompiler` replaces the function that turns a schema into a validation function for the current context. It receives `{ schema, method, url, httpPart }` and returns `(data) => result`:

```js
import Joi from "joi";

app.setValidatorCompiler(({ schema }) => {
  return (data) => schema.validate(data);
});

app.post(
  "/x",
  {
    schema: { body: Joi.object({ name: Joi.string().required() }) },
  },
  handler,
);
```

The returned function can return `{ value, error }`, return `true`/`false`, or throw. This is how Zod, Joi and other libraries plug in.

## 314: How do you use different Ajv settings for body and query string?

Return a different Ajv instance per `httpPart` in the validator compiler:

```js
import Ajv from "ajv";
import addFormats from "ajv-formats";

const strict = addFormats(
  new Ajv({ coerceTypes: false, removeAdditional: true, useDefaults: true }),
);
const loose = addFormats(new Ajv({ coerceTypes: "array", useDefaults: true }));

app.setValidatorCompiler(({ schema, httpPart }) => {
  const ajv = httpPart === "body" ? strict : loose;
  return ajv.compile(schema);
});
```

Shared schemas added with `addSchema` must also be added to these Ajv instances yourself, since you are bypassing Fastify's compiler.

## 315: How do you validate data manually with a route's schema?

Request objects have helpers that reuse the route's compiled functions:

```js
app.post("/import", { schema: { body: importSchema } }, async (request) => {
  const validateItem = request.compileValidationSchema(itemSchema);
  const bad = request.body.items.filter((item) => !validateItem(item));
  return { invalid: bad.length };
});
```

There are also `request.getValidationFunction(schemaOrHttpPart)` and `request.validateInput(data, schema)`. Compiled functions are cached per schema object, so pass the same object, not a new one each time.

## 316: How do you serialize data manually with a schema?

The reply has matching helpers:

```js
app.get("/export", async (request, reply) => {
  const serialize = reply.compileSerializationSchema(rowSchema);
  const lines = rows.map((row) => serialize(row)).join("\n");
  reply.type("application/x-ndjson");
  return lines;
});
```

Also `reply.getSerializationFunction(schemaOrStatus)` and `reply.serializeInput(data, schema)`. This is handy for NDJSON streams where each line has the same shape.

## 317: What is prototype poisoning and how does Fastify protect against it?

Prototype poisoning is when JSON like `{"__proto__": {"isAdmin": true}}` is parsed and later merged into an object, which can change the prototype of other objects. `JSON.parse` keeps `__proto__` as a normal key, and a later `Object.assign` or deep merge can apply it.

Fastify parses JSON with `secure-json-parse`. By default (`onProtoPoisoning: 'error'`) a body with `__proto__` gets a 400. `onConstructorPoisoning: 'error'` does the same for `constructor.prototype`. Keep these defaults.

## 318: What security risks come with trustProxy: true?

With `true`, Fastify trusts every `X-Forwarded-*` header. If the app can be reached directly (not only through your proxy), a client can send `X-Forwarded-For: 1.2.3.4` and fake its IP. That breaks IP-based rate limits, allow-lists and audit logs. It can also fake `X-Forwarded-Proto` and `X-Forwarded-Host`, which matters for building URLs and secure cookie logic.

Set `trustProxy` to the exact number of hops or the IP ranges of your proxies, and block direct access at the network level.

## 319: How can reply.redirect be abused, and how do you prevent it?

If you redirect to a URL taken from user input, like `/login?next=https://evil.com`, you create an open redirect, which is used in phishing. Validate the target:

```js
app.get("/login/callback", async (request, reply) => {
  const next = request.query.next ?? "/";
  const safe = next.startsWith("/") && !next.startsWith("//") ? next : "/";
  return reply.redirect(safe);
});
```

Only allow relative paths or a list of known hosts.

## 320: How do you avoid path traversal when serving files?

Never build file paths from user input without checks. `@fastify/static` and `reply.sendFile()` already reject paths that escape `root`. If you read files yourself:

```js
import path from "node:path";

const base = path.resolve("uploads");

app.get("/files/:name", async (request, reply) => {
  const full = path.resolve(base, request.params.name);
  if (!full.startsWith(base + path.sep)) {
    return reply.code(400).send({ message: "Bad path" });
  }
  return reply.sendFile(path.relative(base, full), base);
});
```

Also be careful with URL-encoded sequences like `%2e%2e%2f`, which decode to `../`.

## 321: Why should you keep Fastify patched, using recent CVEs as an example?

Fastify has had security fixes in content type parsing, where a crafted `Content-Type` header could make Fastify pick a different parser, or skip body validation, in older versions. Fixes were released for both v5 and the v6 alphas. These bugs are in the framework, not your code, so the only fix is upgrading. Use `npm audit`, Dependabot or Renovate, and follow the Fastify security advisories on GitHub.

## 322: How would you design rate limiting for a multi-instance deployment?

- Use `@fastify/rate-limit` with a Redis store so all instances share counters.
- Pick a good key: user ID for logged-in users, API key for partners, IP only as a fallback.
- Set stricter limits on expensive or sensitive routes (login, password reset, search).
- Use `trustProxy` correctly so IP-based keys are real client IPs.
- Return `Retry-After` and rate limit headers so clients can back off.
- Add a limit for 404s to slow down scanners.

```js
await app.register(rateLimit, {
  redis: new Redis(process.env.REDIS_URL),
  max: 300,
  timeWindow: "1 minute",
  keyGenerator: (request) => request.user?.id ?? request.ip,
});
```

For very high traffic, rate limiting at the gateway or CDN is cheaper than in Node.js.

## 323: What is handlerTimeout and how is it different from connectionTimeout?

`handlerTimeout` limits how long the full request lifecycle can take, from routing to the end of the handler. When it fires, Fastify sends a 503 (error code `FST_ERR_HANDLER_TIMEOUT`) and aborts `request.signal`.

`connectionTimeout` is a socket-level timeout. It closes idle sockets and does not work well with keep-alive, since the same socket serves many requests. `handlerTimeout` is per request and works with keep-alive.

```js
const app = Fastify({ handlerTimeout: 10_000 });

app.get("/report", { handlerTimeout: 60_000 }, buildReport);
```

A route-level value overrides the server value. It does not apply to not-found handlers.

## 324: How do you cancel work when a request times out or the client goes away?

Pass `request.signal` to anything that accepts an `AbortSignal`:

```js
app.get("/search", { handlerTimeout: 5000 }, async (request) => {
  const res = await fetch(
    `${SEARCH_URL}?q=${encodeURIComponent(request.query.q)}`,
    {
      signal: request.signal,
    },
  );
  return res.json();
});
```

When the timeout fires, `fetch` is aborted. The cancellation is cooperative: Fastify cannot stop your code, so CPU loops or APIs that ignore the signal will keep running. Check `request.signal.aborted` in long loops.

## 325: How do you customize the response when handlerTimeout fires?

Handle `FST_ERR_HANDLER_TIMEOUT` in the error handler:

```js
app.setErrorHandler((error, request, reply) => {
  if (error.code === "FST_ERR_HANDLER_TIMEOUT") {
    return reply.code(504).send({ message: "The request took too long" });
  }
  reply.send(error);
});
```

## 326: How do you find what is blocking the event loop in a Fastify app?

1. Watch event loop delay, for example with `@fastify/under-pressure` or `perf_hooks.monitorEventLoopDelay()`.
2. Reproduce under load with `autocannon`.
3. Profile with `node --cpu-prof`, Clinic.js (`clinic flame`) or `0x` to get a flame graph.
4. Look for wide stacks in your code: sync crypto (`pbkdf2Sync`), large `JSON.parse`/`JSON.stringify`, sync file reads, big regexes, heavy loops.

Move CPU-heavy work to worker threads or a separate service.

## 327: How do you benchmark a Fastify route?

Use `autocannon`, which is made by the same people:

```bash
npx autocannon -c 100 -d 20 -p 10 http://localhost:3000/users
```

`-c` is connections, `-d` duration in seconds, `-p` pipelining. Tips:

- Run with `NODE_ENV=production` and logging at `warn` or off, or the logger can be a big part of the cost.
- Run the load generator on a different machine or core than the server.
- Compare before and after one change at a time.
- Check p99 latency, not only requests per second.

## 328: How much does logging cost and how do you reduce it?

Pino is fast, but writing two log lines per request still costs CPU, especially with pretty printing or many serializers. To reduce it:

- Never use `pino-pretty` in production.
- Log at `info` or higher in production.
- Turn off per-request logs for health checks and other noisy routes with `LogController`.
- Keep custom serializers small.
- Write logs to stdout and let the platform ship them, or use a Pino transport that runs in a worker thread.

## 329: What are Pino transports and why do they run in a worker thread?

A transport takes log lines and sends them somewhere (a file, a log service, pretty output). Pino runs transports in a separate worker thread, so formatting and network calls do not block the main event loop:

```js
const app = Fastify({
  logger: {
    level: "info",
    transport: {
      targets: [
        { target: "pino/file", options: { destination: 1 } },
        {
          target: "pino-loki",
          options: { host: "http://loki:3100" },
          level: "warn",
        },
      ],
    },
  },
});
```

If the process crashes hard, logs still in the worker queue can be lost, so log fatal errors synchronously where it matters.

## 330: How do you run CPU-heavy work without blocking requests?

Use a worker thread pool. `piscina` is a common choice and there is a Fastify plugin, `fastify-piscina`:

```js
import piscinaPlugin from "fastify-piscina";

app.register(piscinaPlugin, {
  filename: new URL("./workers/resize.js", import.meta.url).href,
  maxThreads: 4,
});

app.post("/resize", async (request) => {
  return app.runTask({ image: request.body.image, width: 300 });
});
```

For long jobs (minutes), use a job queue like BullMQ and return a job ID instead of waiting in the request.

## 331: Should you use Node.js cluster with Fastify?

It depends on the platform:

- On Kubernetes or a container platform, run one Fastify process per container and scale replicas. It is simpler to monitor and restart.
- On a single big VM, `node:cluster` or a process manager like PM2 can use all cores.

In both cases the app must be stateless (sessions, rate limits and WebSocket fan-out in Redis or similar), since requests from one client can hit different processes.

## 332: How do you make outgoing HTTP calls efficient from Fastify?

- Reuse connections. Node's `fetch` uses `undici` with a global pool, so do not create new agents per request.
- For heavy traffic to one host, use an `undici.Pool` with tuned `connections` and `pipelining`.
- Set timeouts and pass `request.signal` so calls stop when the request is cancelled.
- Run independent calls in parallel with `Promise.all`.
- For proxying, use `@fastify/reply-from`, which uses undici and streams the response.

## 333: How do you avoid duplicate work when many requests ask for the same data at once?

Use request coalescing: if a fetch for key X is already running, new requests wait for the same promise instead of starting a new fetch. `async-cache-dedupe` (by the Fastify team) does this with optional caching:

```js
import { createCache } from "async-cache-dedupe";

const cache = createCache({ ttl: 5, storage: { type: "memory" } });

cache.define("getProduct", async (id) => app.db.products.findById(id));

app.get("/products/:id", async (request) =>
  cache.getProduct(request.params.id),
);
```

This protects the database from a burst of identical queries when a cache entry expires.

## 334: How do you stream a large database result as JSON?

Do not load all rows into memory. Stream them and write JSON yourself, or use NDJSON:

```js
import { Readable } from "node:stream";

app.get("/export", async (request, reply) => {
  const cursor = app.db.collection("events").find().stream();

  async function* lines() {
    for await (const doc of cursor) {
      yield JSON.stringify(doc) + "\n";
    }
  }

  reply.type("application/x-ndjson");
  return Readable.from(lines());
});
```

Streams handle backpressure, so memory stays flat even for millions of rows.

## 335: How do you upload a large file straight to S3 without storing it on disk?

Pipe the multipart file stream to the S3 upload:

```js
import { Upload } from "@aws-sdk/lib-storage";

app.post("/upload", async (request) => {
  const file = await request.file();
  const key = `uploads/${randomUUID()}`;

  await new Upload({
    client: s3,
    params: {
      Bucket: process.env.BUCKET,
      Key: key,
      Body: file.file,
      ContentType: file.mimetype,
    },
  }).done();

  if (file.file.truncated) {
    throw app.httpErrors.payloadTooLarge();
  }
  return { key };
});
```

Check the size limit and delete the object if the file was truncated. For very large files, presigned URLs that let the browser upload directly to S3 take the load off your server entirely.

## 336: How does @fastify/compress interact with streams and onSend hooks?

`@fastify/compress` uses an `onSend` hook to wrap the payload in a compression stream. Things to know:

- Hooks registered after it see the compressed payload, so order matters.
- It skips small payloads below `threshold` and content types that are not compressible.
- For already compressed content (images, zip), compression only costs CPU.
- With `reply.hijack()` or writing to `reply.raw`, nothing is compressed.

Many teams compress at the reverse proxy or CDN to save CPU in Node.js.

## 337: What problems can happen with HEAD routes in v5?

With `exposeHeadRoutes: true`, Fastify creates a HEAD route for each GET route. If you also define your own HEAD route for the same path after the GET, you get a duplicate route error. Either register the custom HEAD route before the GET, or set `exposeHeadRoutes: false` on the GET route.

## 338: What happens when you throw something that is not an Error?

If you throw a string or a plain object, Fastify still sends an error response, but you lose the stack trace and logs are harder to read. If you call `reply.send()` with `undefined` as an error in the error handler path, you get `FST_ERR_SEND_UNDEFINED_ERR`. Always throw `Error` objects (or classes from `@fastify/error`), with a `statusCode` when it should not be a 500.

## 339: What happens if the error handler itself throws?

The error is passed to the parent context's error handler. If the root error handler throws, Fastify falls back to its default error handler, which sends a 500. This lets a child plugin handle only the errors it knows about and rethrow everything else.

## 340: How do you make sure no internal details leak in 500 responses?

Use a root error handler that hides messages for server errors:

```js
app.setErrorHandler((error, request, reply) => {
  const status = error.statusCode >= 400 ? error.statusCode : 500;

  if (status >= 500) {
    request.log.error({ err: error }, "unhandled error");
    return reply.code(status).send({
      statusCode: status,
      message: "Internal Server Error",
      requestId: request.id,
    });
  }

  reply
    .code(status)
    .send({ statusCode: status, code: error.code, message: error.message });
});
```

Returning `requestId` lets support find the full error in the logs.

## 341: How do you test that hooks run in the expected order?

Record calls in an array and check it after an injected request:

```js
test("hook order", async () => {
  const calls = [];
  const app = Fastify();

  app.addHook("onRequest", async () => {
    calls.push("root onRequest");
  });
  app.register(async (child) => {
    child.addHook("onRequest", async () => {
      calls.push("child onRequest");
    });
    child.addHook("preHandler", async () => {
      calls.push("child preHandler");
    });
    child.get("/", async () => {
      calls.push("handler");
      return "ok";
    });
  });

  await app.inject("/");
  assert.deepStrictEqual(calls, [
    "root onRequest",
    "child onRequest",
    "child preHandler",
    "handler",
  ]);
});
```

## 342: How does light-my-request work?

`light-my-request` creates fake Node.js `IncomingMessage` and `ServerResponse` objects in memory and passes them to Fastify's request handler directly, the same way the HTTP server would. No socket or TCP is used. It collects what is written to the response and returns it as an object with `statusCode`, `headers`, `body`, `json()` and so on.

Because there is no network, some things behave differently: there are no real socket timeouts, `request.ip` is `127.0.0.1` by default, and client aborts are simulated.

## 343: When is inject() not enough for testing?

- Socket-level behavior: `connectionTimeout`, `keepAliveTimeout`, real aborts.
- HTTP/2 specific behavior.
- WebSockets (use `app.injectWS()` from `@fastify/websocket`, or a real client against a real port).
- TLS setup.
- Behavior of a reverse proxy in front of the app.

For these, start the server on port 0 and use a real client.

## 344: How do you test a plugin that is wrapped with fastify-plugin?

Register it on a fresh instance and check that it exposes what it should:

```js
test("db plugin decorates the instance and closes", async () => {
  const app = Fastify();
  await app.register(dbPlugin, { url: TEST_DB_URL });

  assert.ok(app.hasDecorator("db"));
  await app.close();
  assert.strictEqual(app.db.isClosed, true);
});
```

Because it skips encapsulation, the decorator is visible on the root test instance.

## 345: What is Symbol.asyncDispose on the Fastify instance used for?

The Fastify instance implements `Symbol.asyncDispose`, which calls `close()`. With `await using` (explicit resource management), the app closes when it goes out of scope:

```js
test("ping", async () => {
  await using app = buildApp();
  const res = await app.inject("/ping");
  assert.strictEqual(res.statusCode, 200);
}); // app.close() runs here
```

`await using` needs a Node.js version that supports explicit resource management (Node.js 24 or newer). You can also register an object with `Symbol.asyncDispose` as an `onClose` hook.

## 346: What is the diagnostics channel support in Fastify?

Fastify publishes events on Node.js `diagnostics_channel`:

- `fastify.initialization` when an instance is created, with the instance. Tracing tools use it to add hooks without changing your code.
- Tracing channel events for each request handler: `tracing:fastify.request.handler:start`, `:end`, `:asyncStart`, `:asyncEnd` and `:error`. Each gets the request, reply and the route `{ url, method }`.

```js
import dc from "node:diagnostics_channel";

dc.subscribe("tracing:fastify.request.handler:error", ({ request, error }) => {
  request.log.error({ err: error }, "handler failed");
});
```

APM tools use this instead of monkey patching.

## 347: How do you add OpenTelemetry tracing to Fastify?

Use `@fastify/otel`, the official instrumentation. It creates spans for the request, each hook and the handler:

```js
import { NodeSDK } from "@opentelemetry/sdk-node";
import FastifyOtelInstrumentation from "@fastify/otel";

const fastifyOtel = new FastifyOtelInstrumentation();

const sdk = new NodeSDK({ instrumentations: [fastifyOtel] });
sdk.start();

const app = Fastify();
await app.register(fastifyOtel.plugin());

app.get("/health", { config: { otel: false } }, async () => "ok");
```

Register it before other plugins and routes so it can see them. Set the service name with `OTEL_SERVICE_NAME`. Add HTTP client and database instrumentations to see the full trace.

## 348: How do you correlate logs with traces?

Put the trace ID in the logs. Options:

- Use `@opentelemetry/instrumentation-pino`, which adds `trace_id` and `span_id` to Pino log lines.
- Or set `genReqId` to read the `traceparent` header and use part of it as the request ID.
- Or add a `mixin` to the Pino config that reads the active span.

Then your log tool can jump from a trace to its logs.

## 349: What does setChildLoggerFactory do?

It controls how the per-request child logger is created. By default Fastify calls `logger.child({ reqId })`. You can add more fields:

```js
app.setChildLoggerFactory(function (logger, bindings, opts, rawReq) {
  bindings.tenant = rawReq.headers["x-tenant-id"];
  return logger.child(bindings, opts);
});
```

Every `request.log` call then includes the tenant. It follows encapsulation, so you can set it per plugin.

## 350: What does setGenReqId do?

`app.setGenReqId(fn)` sets the request ID generator for the current context, while the `genReqId` server option sets it for the whole app. This lets one plugin use a different ID scheme, for example a plugin for webhooks that takes the ID from the provider's delivery header.

## 351: How would you structure a large Fastify app into modules?

One common approach is a modular monolith built on encapsulation:

```
src/
  app.js
  plugins/            # shared: config, db, auth, swagger
  modules/
    billing/
      index.js        # plugin: registers routes, hooks, error handler
      routes.js
      service.js
      schemas.js
    catalog/
      ...
```

Each module is one plugin (not wrapped with `fastify-plugin`), with its own prefix, hooks and error handler. Modules talk to each other through services passed as decorators or through events, not by reaching into each other's files. This keeps boundaries clear and makes splitting out a microservice later easier.

## 352: How do you share code between modules without breaking encapsulation?

Put the shared parts in a plugin wrapped with `fastify-plugin` and register it at the root, before the modules. Each module can then use the decorator. For things only two modules need, a plain JavaScript module (a service file) imported by both is often simpler than a Fastify decorator.

## 353: What is the difference between using decorators and module imports for dependencies?

- Decorators are set up by Fastify at boot, follow the plugin tree, can be replaced in tests by decorating a fake, and are closed with `onClose`.
- Module imports are simpler and work outside Fastify, but they are singletons for the whole process, which makes per-test replacement harder and ties lifecycle to the module system.

A common split: use decorators for resources with a lifecycle (db pools, clients, config), and plain imports for pure functions and business logic.

## 354: How would you build a multi-tenant API with Fastify?

1. Identify the tenant early in `onRequest` (subdomain, header or JWT claim).
2. Store it on the request with a declared decorator (`request.tenant`).
3. Pick the right database connection or schema for that tenant, often from a pool cache keyed by tenant ID.
4. Add tenant ID to logs with `setChildLoggerFactory`.
5. Use `@fastify/request-context` if deep code needs the tenant.
6. Rate limit per tenant.

```js
app.decorateRequest("tenant", null);

app.addHook("onRequest", async (request, reply) => {
  const tenant = await app.tenants.resolve(request.host);
  if (!tenant) return reply.code(404).send({ message: "Unknown tenant" });
  request.tenant = tenant;
});
```

For host-based tenants, route `host` constraints can split different tenants' routes, but most apps share routes and switch data by tenant.

## 355: How do you implement idempotency keys for POST requests?

Clients send an `Idempotency-Key` header. Store the result of the first request and return it again for repeats:

```js
app.post(
  "/payments",
  {
    preHandler: async (request, reply) => {
      const key = request.headers["idempotency-key"];
      if (!key)
        return reply.code(400).send({ message: "Idempotency-Key required" });

      const cached = await app.redis.get(`idem:${key}`);
      if (cached) {
        const { status, body } = JSON.parse(cached);
        return reply.code(status).send(body);
      }

      const locked = await app.redis.set(
        `idem-lock:${key}`,
        "1",
        "EX",
        30,
        "NX",
      );
      if (!locked)
        return reply.code(409).send({ message: "Request in progress" });
    },
  },
  async (request, reply) => {
    const body = await createPayment(request.body);
    await app.redis.set(
      `idem:${request.headers["idempotency-key"]}`,
      JSON.stringify({ status: 201, body }),
      "EX",
      86400,
    );
    return reply.code(201).send(body);
  },
);
```

Also scope the key to the user so one user cannot replay another's key.

## 356: How do you design background processing triggered by an HTTP request?

Do not run long tasks inside the request, and do not start "fire and forget" promises that can be lost on restart. Instead:

1. Validate the request and write a job to a queue (BullMQ, SQS, RabbitMQ) or an outbox table.
2. Return `202 Accepted` with a job ID or status URL.
3. Process the job in a worker (separate process or service).
4. Let the client poll a status route or get notified by webhook, SSE or WebSocket.

```js
app.post("/reports", async (request, reply) => {
  const job = await app.queue.add("report", {
    userId: request.user.id,
    range: request.body.range,
  });
  return reply
    .code(202)
    .header("Location", `/reports/${job.id}`)
    .send({ id: job.id });
});
```

## 357: How do you make WebSockets work across several Fastify instances?

Each instance only knows its own connections. To send a message to all users:

- Publish events to Redis pub/sub (or NATS, Kafka). Every instance subscribes and forwards messages to its local sockets.
- Store presence (who is online where) in Redis if needed.
- Use sticky sessions at the load balancer only if your protocol needs it (for example Socket.IO with long polling). Plain WebSockets do not need it once connected.

## 358: How would you set up GraphQL on Fastify?

The main option is Mercurius, a GraphQL adapter built for Fastify:

```js
import mercurius from "mercurius";

app.register(mercurius, {
  schema: `
    type Query { add(x: Int!, y: Int!): Int! }
  `,
  resolvers: {
    Query: { add: async (_, { x, y }) => x + y },
  },
  graphiql: process.env.NODE_ENV !== "production",
});
```

It supports JIT compiled queries, loaders to fix N+1 problems, subscriptions over WebSockets and federation. You can also use GraphQL Yoga or Apollo Server with their Fastify integrations.

## 359: How does NestJS use Fastify?

NestJS can run on Express (default) or Fastify through `@nestjs/platform-fastify`:

```ts
import { NestFactory } from "@nestjs/core";
import {
  FastifyAdapter,
  NestFastifyApplication,
} from "@nestjs/platform-fastify";

const app = await NestFactory.create<NestFastifyApplication>(
  AppModule,
  new FastifyAdapter(),
);
await app.listen({ port: 3000, host: "0.0.0.0" });
```

You get Fastify's faster HTTP layer, but NestJS's own pipes, guards and interceptors still run on top, so you lose some of the raw speed. Fastify plugins are registered with `app.register()`. Express-only middleware will not work.

## 360: What is Platformatic and how does it relate to Fastify?

Platformatic is a set of tools by members of the Fastify team, built on Fastify. Its Watt application server can run several Node.js services (Fastify apps, Next.js and others) in one process with worker threads, with shared config, logging and metrics. It is an option for teams that want a ready-made setup instead of building everything around plain Fastify.

## 361: How do you serve a Vite-based frontend with server-side rendering in Fastify?

Use `@fastify/vite`, which integrates Vite's dev server in development and serves the built files in production. It supports React, Vue and other renderers. The idea:

```js
import FastifyVite from "@fastify/vite";

await app.register(FastifyVite, {
  root: import.meta.dirname,
  dev: process.argv.includes("--dev"),
  spa: false,
});

await app.vite.ready();
```

Routes then call `reply.html()` to render. It gives you SSR without moving to a full meta-framework.

## 362: How would you investigate a memory leak in a Fastify app?

1. Confirm it: watch heap used over time under steady load. A sawtooth that keeps rising is a leak.
2. Take heap snapshots (`node --heapsnapshot-signal=SIGUSR2` or Chrome DevTools) at two points and compare them.
3. Look for objects that keep growing: arrays or Maps used as caches with no limit, listeners added per request (`process.on`, `emitter.on`), closures holding request objects in long-lived structures, timers not cleared.
4. Check plugin code that registers hooks or decorators per request instead of at boot.
5. Fix and verify with the same load test.

## 363: Why should you never call register() or addHook() inside a handler?

Plugins, hooks, routes and decorators must be set up during boot. After `ready()`, calling `register()` throws `FST_ERR_ROOT_PLG_BOOTED`, and adding routes throws too. Even where it does not throw, adding things per request would grow arrays forever and change behavior for all future requests, which is a leak and a bug.

## 364: How do you add routes dynamically at runtime?

You cannot add routes after the server has started. Options:

- Register a generic route with a param or wildcard and dispatch inside the handler:

```js
app.all("/hooks/:name", async (request, reply) => {
  const handler = dynamicHandlers.get(request.params.name);
  if (!handler) return reply.callNotFound();
  return handler(request, reply);
});
```

- Or rebuild a new Fastify instance with the new routes and swap it in front of traffic (blue/green style), which is how some platforms do hot reloading.

## 365: What happens if a plugin throws during boot?

The error is passed through avvio and `ready()`/`listen()` reject with it. The server does not start. This is good: a missing env var or unreachable database should stop the process early, so the orchestrator shows a crash instead of a half-working service. Log the error and exit with a non-zero code.

## 366: How do you load a plugin only in some environments?

Use a normal `if`:

```js
if (app.config.NODE_ENV !== "production") {
  await app.register(swaggerUi, { routePrefix: "/docs" });
}
```

With `@fastify/autoload` you can use `ignorePattern` or `matchFilter` to skip files. Be careful not to make the plugin tree too different between environments, or bugs only appear in production.

## 367: How would you handle zero-downtime deploys?

1. Run at least two instances behind a load balancer.
2. On `SIGTERM`, mark the instance as not ready (fail the readiness probe) so the load balancer stops sending new traffic.
3. Wait a few seconds for the load balancer to notice.
4. Call `app.close()`, which drains in-flight requests (and returns 503 with `Connection: close` for new requests on keep-alive sockets).
5. Close database pools in `onClose`.
6. Set a hard timeout so the process exits even if something hangs.

`close-with-grace` handles the signal, timeout and error parts:

```js
import closeWithGrace from "close-with-grace";

closeWithGrace({ delay: 10_000 }, async ({ err }) => {
  if (err) app.log.error({ err }, "closing because of error");
  await app.close();
});
```

## 368: What is the difference between readiness and liveness probes for a Fastify app?

- Liveness: "is the process alive and not stuck?" A simple route that returns 200 is enough. It should not check the database, or a database outage restarts every pod for nothing.
- Readiness: "can this instance take traffic?" It can check critical dependencies and should start failing during shutdown.

```js
let shuttingDown = false;

app.get("/live", async () => ({ ok: true }));
app.get("/ready", async (request, reply) => {
  if (shuttingDown) return reply.code(503).send({ ready: false });
  await app.db.query("SELECT 1");
  return { ready: true };
});

app.addHook("preClose", async () => {
  shuttingDown = true;
});
```

## 369: Why can you get 502 errors from a load balancer in front of Fastify?

Common causes:

- The app closes keep-alive connections before the load balancer does. Fix: `keepAliveTimeout` longer than the LB idle timeout.
- The app is restarting or shutting down without draining. Fix: graceful shutdown and readiness probes.
- The app crashes on an uncaught exception.
- `requestTimeout` or `handlerTimeout` set lower than the LB timeout, so the app cuts the connection.
- Headers too large for the app (`maxHeaderSize` in Node.js) while the LB accepts them.

## 370: How do you use a custom HTTP server with serverFactory?

`serverFactory` lets you create the server yourself, for example to wrap it or use a different server:

```js
import http from "node:http";

const app = Fastify({
  serverFactory: (handler) => {
    return http.createServer((req, res) => {
      handler(req, res);
    });
  },
});
```

Fastify calls `serverFactory` with its request handler and uses whatever server you return. It is used for special cases like running behind another framework or custom TLS handling.

## 371: How do you run Fastify on AWS Lambda?

Use `@fastify/aws-lambda`:

```js
import awsLambdaFastify from "@fastify/aws-lambda";
import { buildApp } from "./app.js";

const app = buildApp();
const proxy = awsLambdaFastify(app);

await app.ready();

export const handler = proxy;
```

Tips: create the app outside the handler so warm invocations reuse it, keep plugins light, consider standalone compiled schemas for faster cold starts, and remember there is no long-lived WebSocket or background work in Lambda.

## 372: How do you avoid N+1 queries in Fastify routes?

The framework does not help directly; it is about how you query. Options:

- Load related data with joins or `IN (...)` queries.
- Use the ORM's include or relation loading.
- In GraphQL with Mercurius, use loaders, which batch lookups per request.
- Use a per-request DataLoader stored on the request (declared with a decorator and created in `onRequest`), so it is not shared between users.

## 373: What is the risk of sharing a DataLoader across requests?

DataLoader caches results. If one instance is shared across requests, user A can get data cached for user B, and the cache grows without limit. Always create a new loader per request:

```js
app.decorateRequest("loaders", null);
app.addHook("onRequest", async (request) => {
  request.loaders = {
    user: new DataLoader((ids) => app.db.users.findByIds(ids)),
  };
});
```

## 374: How do you limit query string complexity to protect the app?

- Use a schema with `additionalProperties: false` on the querystring.
- Set `maxItems` on array params.
- If you use `qs` as a custom parser, set `depth`, `arrayLimit` and `parameterLimit`.
- Limit URL length at the proxy.

Deeply nested query objects can be used for denial of service or to sneak in unexpected keys like `__proto__`.

## 375: How does Fastify handle very large JSON bodies safely?

- `bodyLimit` stops reading once the limit is reached and sends 413.
- If `Content-Length` is larger than the limit, Fastify rejects it before reading.
- `secure-json-parse` blocks prototype poisoning.

But parsing a 1 MB JSON still blocks the event loop briefly. For endpoints that need large bodies, consider streaming formats like NDJSON, or uploading files to object storage.

## 376: How do you validate a body with a discriminator?

Use `oneOf` with a `discriminator` keyword, which Ajv supports when `discriminator: true` is set:

```js
const app = Fastify({ ajv: { customOptions: { discriminator: true } } });

const paymentSchema = {
  type: "object",
  discriminator: { propertyName: "method" },
  required: ["method"],
  oneOf: [
    {
      properties: { method: { const: "card" }, cardToken: { type: "string" } },
      required: ["cardToken"],
    },
    {
      properties: { method: { const: "bank" }, iban: { type: "string" } },
      required: ["iban"],
    },
  ],
};
```

With a discriminator Ajv checks only the matching branch, which gives clearer errors and is faster than a plain `oneOf`.

## 377: Why is removeAdditional dangerous with anyOf or oneOf?

With `removeAdditional: true`, Ajv removes properties not listed in `properties` when `additionalProperties: false` is set. With `anyOf`, Ajv checks the first branch, which may strip properties that belong to the second branch, and then the second branch fails because the data has been changed. The data is mutated while being validated.

Fixes: avoid `additionalProperties: false` inside `anyOf`/`oneOf` branches, use a `discriminator`, or set `removeAdditional: false` and reject extra properties instead.

## 378: How do you handle nullable fields in schemas?

Use a type array:

```js
properties: {
  middleName: {
    type: ["string", "null"];
  }
}
```

`fast-json-stringify` supports this too. Ajv also supports `nullable: true` (an OpenAPI 3.0 keyword) when used together with `type`. The type array form is plain JSON Schema and works in both validation and serialization.

## 379: How are Date objects serialized with a response schema?

Use `type: 'string'` with `format: 'date-time'` (or `date`, `time`). `fast-json-stringify` turns a `Date` into an ISO string:

```js
response: {
  200: {
    type: 'object',
    properties: { createdAt: { type: 'string', format: 'date-time' } }
  }
}
```

Without a format, a `Date` is serialized with its `toJSON()` method, which also gives an ISO string. With `format: 'date'` you get only the date part.

## 380: How do you send BigInt values in JSON?

`JSON.stringify` throws on `BigInt`. Options:

- Convert to a string in your code before returning (safest for JavaScript clients, since big numbers lose precision as `number`).
- `fast-json-stringify` supports `BigInt` for `integer` fields in a response schema.

For IDs from databases (like Postgres `bigint`), sending them as strings is the usual choice.

## 381: How does fast-json-stringify handle integers that are floats?

For `type: 'integer'`, it truncates decimals by default (`Math.trunc`). You can change this with the `rounding` option (`'trunc'`, `'round'`, `'floor'`, `'ceil'`) through `serializerOpts`:

```js
const app = Fastify({ serializerOpts: { rounding: "round" } });
```

This can silently change data, so use `type: 'number'` for values that may have decimals.

## 382: What happens with circular references in a response?

`JSON.stringify` throws on circular structures, and so does a compiled serializer if the schema allows nesting into the cycle. The error becomes a 500. Fix it by returning a plain object built for the response (a DTO) instead of ORM objects that link back to their parents. A response schema helps, since it only follows listed properties.

## 383: How do response schemas help with security?

They act as an allow-list for output. Only fields in the schema are sent, so adding a column like `password_hash` or `internal_notes` to a table does not leak it through an endpoint that returns the whole row. Without a schema, whatever object you return is fully sent. This makes response schemas a good default for every route returning data from a database.

## 384: How do you return different shapes from one route with response schemas?

Use different status codes with their own schemas, or use `anyOf`:

```js
response: {
  200: {
    anyOf: [
      { type: 'object', properties: { type: { const: 'user' }, name: { type: 'string' } } },
      { type: 'object', properties: { type: { const: 'org' }, title: { type: 'string' } } }
    ]
  }
}
```

`anyOf` in serialization needs runtime checks to pick the branch, so it is slower. If the shapes are very different, separate routes are often cleaner.

## 385: How do you handle errors in a custom content type parser?

Set a `statusCode` on the error so it is not a 500:

```js
app.addContentTypeParser(
  "application/x-yaml",
  { parseAs: "string" },
  (request, body, done) => {
    try {
      done(null, yaml.parse(body));
    } catch (err) {
      err.statusCode = 400;
      done(err);
    }
  },
);
```

Errors from parsers go to the error handler like any other error. Also limit the size with `bodyLimit` so a huge YAML body cannot block the event loop.

## 386: How does the content type parser pick a match?

Fastify first looks for an exact match on the media type (without parameters like `charset`). Then it tries string parsers that match the start, and then regex parsers, in the order they were added. If nothing matches, the `'*'` parser is used if there is one; otherwise you get a 415.

Newer versions are stricter about the format of the `Content-Type` header to avoid tricks where a malformed header matches a different parser than expected.

## 387: How do you add an async content type parser?

The parser can return a promise instead of using `done`:

```js
app.addContentTypeParser(
  "application/msgpack",
  { parseAs: "buffer" },
  async (request, body) => {
    return msgpack.decode(body);
  },
);
```

Do not mix the two styles in one function.

## 388: How do you handle the request body as a stream in a route?

Add a parser that passes the raw stream through, inside an encapsulated plugin:

```js
app.register(async (uploads) => {
  uploads.addContentTypeParser("*", (request, payload, done) =>
    done(null, payload),
  );

  uploads.put("/blob/:key", async (request) => {
    await pipeline(
      request.body,
      fs.createWriteStream(path.join(DIR, safeName(request.params.key))),
    );
    return { ok: true };
  });
});
```

Now `request.body` is the raw stream. `bodyLimit` is not applied for you here, so add your own size check.

## 389: How do you write a custom route constraint that is async?

Constraint strategies can have an async `deriveConstraint` with a callback:

```js
app.addConstraintStrategy({
  name: "plan",
  storage() {
    /* same as sync */
  },
  deriveConstraint(req, ctx, done) {
    lookupPlan(req.headers.authorization)
      .then((plan) => done(null, plan))
      .catch(done);
  },
  mustMatchWhenDerived: true,
});
```

Async constraints run on every request for that path before routing, so they add latency. Errors become `FST_ERR_ASYNC_CONSTRAINT`, which you can handle with `frameworkErrors`. Usually it is simpler to route normally and branch in a hook.

## 390: How would you build API versioning for a large API?

Options:

1. URL versions (`/v1`, `/v2`) with prefixes. Easy to see, cache and document. Most common.
2. Header versions (`Accept-Version`) with the `version` constraint. Clean URLs, but harder to test in a browser and needs `Vary` headers for caches.
3. Media type versions (`Accept: application/vnd.app.v2+json`) with a custom constraint.

With prefixes, you can share most handlers and only override what changed:

```js
app.register(v1Routes, { prefix: "/v1" });
app.register(
  async (v2) => {
    v2.register(v1Routes); // reuse
    v2.register(v2Overrides); // changed routes
  },
  { prefix: "/v2" },
);
```

Watch for duplicate routes if `v2Overrides` defines the same path as `v1Routes`. Use a shared list of handlers and register the v2 version only.

## 391: How do you prevent duplicate routes when composing route plugins?

Fastify throws `FST_ERR_DUPLICATED_ROUTE` at boot, which is good. To compose without clashes, build route lists as data and merge them before registering:

```js
const v1 = { "GET /users": listUsersV1, "GET /users/:id": getUser };
const v2 = { ...v1, "GET /users": listUsersV2 };

function routesFrom(map) {
  return async (app) => {
    for (const [key, handler] of Object.entries(map)) {
      const [method, url] = key.split(" ");
      app.route({ method, url, handler });
    }
  };
}

app.register(routesFrom(v2), { prefix: "/v2" });
```

## 392: How do you enforce that every route has a response schema?

Use the `onRoute` hook to check at boot:

```js
app.addHook("onRoute", (route) => {
  if (route.url.startsWith("/docs")) return;
  if (!route.schema?.response) {
    throw new Error(
      `Route ${route.method} ${route.url} has no response schema`,
    );
  }
});
```

Add this hook before the routes are registered. Throwing at boot catches it in CI instead of in production.

## 393: How do you add default options to every route?

Use `onRoute` to fill in defaults:

```js
app.addHook("onRoute", (route) => {
  route.config ??= {};
  route.config.auth ??= true;
  route.schema ??= {};
  route.schema.tags ??= [route.prefix.split("/")[1] || "root"];
});
```

This keeps route files short and makes defaults consistent. Since `onRoute` follows encapsulation, a hook added in a plugin only affects that plugin's routes.

## 394: How do you share a hook across routes but skip it for some?

Use route config and check it in the hook:

```js
app.addHook("onRequest", async (request) => {
  if (request.routeOptions.config.public) return;
  await request.jwtVerify();
});

app.get("/health", { config: { public: true } }, health);
```

This "secure by default" approach is safer than adding auth route by route, because a new route is protected unless someone marks it public.

## 395: Why are hooks with closures over the request a common source of leaks?

If a hook stores the request or reply in a structure that lives longer than the request (a global Map, an emitter listener, a cache), they cannot be garbage collected. Requests hold sockets, buffers and parsed bodies, so this leaks memory fast.

```js
// bad: listener added per request, never removed
app.addHook("onRequest", async (request) => {
  process.on("message", (msg) => request.log.info(msg));
});
```

Remove listeners in `onResponse`, use `WeakMap` keyed by request, or avoid long-lived references entirely.

## 396: How would you implement a circuit breaker for a downstream service?

Use a library like `opossum`, wrapped in a plugin:

```js
import CircuitBreaker from "opossum";

const breaker = new CircuitBreaker(
  (id, signal) =>
    fetch(`${PRICES_URL}/${id}`, { signal }).then((r) => r.json()),
  { timeout: 2000, errorThresholdPercentage: 50, resetTimeout: 10_000 },
);
breaker.fallback(() => ({ price: null, stale: true }));

app.decorate("prices", breaker);

app.get("/products/:id/price", async (request) => {
  return app.prices.fire(request.params.id, request.signal);
});
```

When the downstream fails too often, the breaker opens and calls the fallback right away, so your app does not pile up waiting requests.

## 397: How do you protect the server when a downstream dependency is slow?

- Set timeouts on every outgoing call.
- Use `handlerTimeout` as a backstop and pass `request.signal` along.
- Limit concurrency to the dependency (a pool or semaphore).
- Use a circuit breaker.
- Use `@fastify/under-pressure` so the instance sheds load with 503 when the event loop lags.
- Cache what can be cached.

Without these, slow responses hold sockets and memory until the process falls over.

## 398: How does @fastify/under-pressure decide when to return 503?

It samples the event loop delay, heap used, RSS and event loop use at a set interval (`sampleInterval`). If any value is above its configured limit (`maxEventLoopDelay`, `maxHeapUsedBytes`, `maxRssBytes`, `maxEventLoopUtilization`), new requests get 503 with a `Retry-After` header. You can also add a `healthCheck` function for custom checks, and a `pressureHandler` to customize the response.

## 399: How do you implement a secure file download with access checks?

```js
app.get(
  "/documents/:id/download",
  { onRequest: [app.authenticate] },
  async (request, reply) => {
    const doc = await app.db.documents.findById(request.params.id);
    if (!doc || doc.ownerId !== request.user.sub) {
      return reply.code(404).send({ message: "Not found" });
    }

    const filename = doc.originalName.replace(/["\r\n]/g, "");
    reply
      .header("Content-Disposition", `attachment; filename="${filename}"`)
      .type(doc.mimeType);
    return fs.createReadStream(path.join(STORAGE_DIR, doc.storageKey));
  },
);
```

Points: return 404 instead of 403 so you do not reveal that the file exists, never use the user's filename as a path, and strip characters that could break the header. For large scale, redirect to a short-lived signed URL from object storage.

## 400: How do you prevent header injection when setting headers from user input?

Node.js already throws if a header value contains `\r` or `\n`, which prevents classic response splitting. Still:

- Validate or encode user values before putting them in headers.
- For `Content-Disposition`, use the `filename*` form with UTF-8 encoding for non-ASCII names.
- Do not reflect arbitrary user input into headers like `Location` or `Set-Cookie`.

## 401: How do you safely store passwords in a Fastify app?

Fastify has nothing built in. Use `argon2` or `bcrypt`, and do the hashing asynchronously so it does not block the event loop:

```js
import argon2 from "argon2";

app.post(
  "/register",
  { schema: { body: registerSchema } },
  async (request, reply) => {
    const hash = await argon2.hash(request.body.password);
    await app.db.users.create({
      email: request.body.email,
      passwordHash: hash,
    });
    return reply.code(201).send({ ok: true });
  },
);
```

Never use sync versions like `bcrypt.hashSync` in handlers. Rate limit login and registration routes, and use a response schema so the hash is never returned.

## 402: How do you implement JWT refresh tokens with Fastify?

- Short-lived access token (5-15 minutes), sent in the `Authorization` header or a cookie.
- Long-lived refresh token in an `httpOnly`, `secure`, `sameSite` cookie with a narrow `path` like `/auth/refresh`.
- Store a hash of refresh tokens (or a token ID) in the database so you can revoke them.
- On refresh, rotate: issue a new refresh token and invalidate the old one. If an old one is used again, revoke the whole family, since it was probably stolen.

`@fastify/jwt` supports multiple namespaces, so you can sign access and refresh tokens with different secrets:

```js
app.register(jwt, { secret: ACCESS_SECRET, namespace: "access" });
app.register(jwt, {
  secret: REFRESH_SECRET,
  namespace: "refresh",
  cookie: { cookieName: "rt", signed: false },
});
```

## 403: What are the risks of using HS256 JWTs across services?

With HS256, every service that verifies tokens needs the same secret, and any of them can also create tokens. If one service leaks the secret, an attacker can mint tokens for all services. With RS256 or EdDSA, only the auth service has the private key, and others verify with the public key (often fetched from a JWKS endpoint). `@fastify/jwt` supports public/private keys with `secret: { private, public }` or a function, and `get-jwks` can fetch keys from a JWKS URL.

## 404: How do you lock down which algorithms @fastify/jwt accepts?

Pass `verify.algorithms`:

```js
app.register(jwt, {
  secret: { public: publicKey },
  verify: {
    algorithms: ["RS256"],
    allowedIss: "https://auth.example.com",
    allowedAud: "orders-api",
  },
});
```

Restricting algorithms prevents attacks where a token is signed with a different algorithm than expected. Checking issuer and audience prevents tokens meant for another service from being accepted.

## 405: How do you secure cookies properly?

```js
reply.setCookie("session", value, {
  httpOnly: true, // JS cannot read it
  secure: true, // HTTPS only
  sameSite: "lax", // basic CSRF protection
  path: "/",
  maxAge: 60 * 60 * 24,
  signed: true, // detects tampering, needs a secret on @fastify/cookie
});
```

Use the `__Host-` prefix on the name for extra protection (requires `secure`, `path: '/'` and no `domain`). Behind a proxy, set `trustProxy` so Fastify knows the original request was HTTPS.

## 406: How do you rotate cookie or session secrets without logging everyone out?

`@fastify/cookie` and `@fastify/session` accept an array of secrets. The first is used to sign, all are tried to verify:

```js
app.register(cookie, {
  secret: [process.env.COOKIE_SECRET_NEW, process.env.COOKIE_SECRET_OLD],
});
```

Deploy with the new secret first in the list, wait until old cookies expire, then remove the old one.

## 407: What is a good Content Security Policy setup with @fastify/helmet?

For an API that returns JSON only, a strict policy is easy:

```js
await app.register(helmet, {
  contentSecurityPolicy: {
    directives: { defaultSrc: ["'none'"], frameAncestors: ["'none'"] },
  },
});
```

For HTML pages with inline scripts, use nonces:

```js
await app.register(helmet, { enableCSPNonces: true });

app.get("/", async (request, reply) => {
  return reply.view("index", { nonce: reply.cspNonce.script });
});
```

## 408: How do you enforce HTTPS behind a load balancer?

The load balancer usually ends TLS and forwards plain HTTP. Set `trustProxy` and redirect when `request.protocol` is `http`:

```js
app.addHook("onRequest", async (request, reply) => {
  if (request.protocol === "http") {
    return reply.redirect(`https://${request.host}${request.url}`, 301);
  }
});
```

Better yet, do the redirect at the load balancer, and send HSTS (`Strict-Transport-Security`) with helmet so browsers stop trying HTTP.

## 409: How do you validate the Host header to prevent host header attacks?

If you build absolute URLs (password reset links, redirects) from `request.host`, an attacker can send a fake `Host` header. Never trust it for that. Use a configured base URL instead:

```js
const resetLink = `${app.config.PUBLIC_URL}/reset?token=${token}`;
```

You can also use route `host` constraints or an `onRequest` hook to reject unknown hosts.

## 410: How would you audit a Fastify app for security issues?

- Check that every route has a body/params/querystring schema and a response schema.
- Check auth is on by default (hook with route config opt-out).
- Review `trustProxy`, `bodyLimit`, `requestIdHeader` and timeouts.
- Look for raw SQL with string concatenation, file paths from input and redirects from input.
- Check CORS origins and cookie flags.
- Make sure errors do not leak stack traces.
- Confirm rate limits on login, signup, password reset and expensive routes.
- Run `npm audit` and confirm Fastify and plugins are on patched versions.

## 411: How do you write a reusable plugin that adds hooks only to routes that opt in?

Use `onRoute` to attach a hook only to routes with a config flag:

```js
import fp from "fastify-plugin";

export default fp(
  async (app, opts) => {
    app.addHook("onRoute", (route) => {
      if (!route.config?.audit) return;
      const hook = async (request, reply) => {
        app.auditLog.write({
          user: request.user?.sub,
          route: route.url,
          status: reply.statusCode,
        });
      };
      route.onResponse = [].concat(route.onResponse ?? [], hook);
    });
  },
  { name: "audit" },
);
```

Routes without `config.audit` pay no cost, since the hook is never attached to them.

## 412: How do you make a plugin's options type-safe and validated at boot?

Validate options with a schema when the plugin loads:

```js
import fp from "fastify-plugin";
import Ajv from "ajv";

const validate = new Ajv().compile({
  type: "object",
  required: ["url"],
  properties: {
    url: { type: "string" },
    poolSize: { type: "integer", minimum: 1 },
  },
});

export default fp(
  async (app, opts) => {
    if (!validate(opts)) {
      throw new Error(`Invalid db options: ${JSON.stringify(validate.errors)}`);
    }
    // ...
  },
  { name: "db" },
);
```

In TypeScript, type the options with `FastifyPluginAsync<Options>` too. The runtime check still matters for JavaScript users and env-based config.

## 413: How do you publish a plugin to npm the right way?

- Name it `fastify-something` (community) and wrap it with `fastify-plugin` if it should not be encapsulated.
- Set `fastify: '5.x'` in the plugin metadata.
- Declare `fastify` as a peer dependency or dev dependency, not a regular dependency, so users do not get two copies.
- Ship TypeScript types with declaration merging for decorators.
- Close resources in `onClose`.
- Test with `inject()` on the supported Node.js versions.

## 414: Why can two copies of Fastify in node_modules cause problems?

Fastify and its plugins use symbols and instance checks. If a plugin depends on a different copy of `fastify` than the app, version checks can fail, types do not match, and some internal symbols differ. This is why plugins should not list `fastify` as a regular dependency. Use `npm ls fastify` to find duplicates.

## 415: How does TypeScript inference work with type providers internally?

A type provider is an interface with a mapping from a schema type to a TypeScript type, using a `schema` input and `validator` and `serializer` outputs in v5:

```ts
import type { FastifyTypeProvider } from "fastify";
import type { Static, TSchema } from "typebox";

interface MyTypeBoxProvider extends FastifyTypeProvider {
  validator: this["schema"] extends TSchema ? Static<this["schema"]> : unknown;
  serializer: this["schema"] extends TSchema ? Static<this["schema"]> : unknown;
}
```

Fastify plugs the route's schema into `this['schema']` and reads `validator` for request types and `serializer` for reply types. In v4 this was a single `output` property with `this['input']`.

## 416: How do you type the reply so TypeScript checks what you return?

Use a response schema with a type provider, or the `Reply` generic:

```ts
app.withTypeProvider<TypeBoxTypeProvider>().get(
  "/users/:id",
  {
    schema: {
      params: Type.Object({ id: Type.String() }),
      response: {
        200: Type.Object({ id: Type.String(), name: Type.String() }),
        404: Type.Object({ message: Type.String() }),
      },
    },
  },
  async (request, reply) => {
    const user = await findUser(request.params.id);
    if (!user) return reply.code(404).send({ message: "Not found" });
    return { id: user.id, name: user.name };
  },
);
```

TypeScript checks that the return value and `reply.code(404).send()` match the schema for that status.

## 417: How do you type handlers defined in separate files?

Use the request and reply types with the route generic, or the type provider helpers:

```ts
import type { FastifyReply, FastifyRequest } from "fastify";

type GetUserRequest = FastifyRequest<{ Params: { id: string } }>;

export async function getUser(request: GetUserRequest, reply: FastifyReply) {
  return request.server.db.users.find(request.params.id);
}
```

With TypeBox, `@fastify/type-provider-typebox` exports `FastifyRequestTypeBox` and `FastifyReplyTypeBox` helpers that take the schema type, so the separate handler still infers from the schema.

## 418: How do you type a decorator that only exists in an encapsulated context?

Declaration merging makes the type global, which is a lie in contexts without the decorator. Options:

- Accept it and make the type optional (`db?: Db`) so code has to check.
- Use `app.getDecorator<Db>('db')`, which throws at runtime if missing and types the value at the call site.
- Create a typed instance for the plugin: `type AppWithDb = FastifyInstance & { db: Db }`.

Most teams use declaration merging for global decorators and `getDecorator` for local ones.

## 419: How do you handle errors in TypeScript with proper types?

The error handler gets `FastifyError`, which has `statusCode`, `code` and `validation`:

```ts
import type { FastifyError } from "fastify";

app.setErrorHandler((error: FastifyError, request, reply) => {
  if (error.validation) {
    return reply
      .code(400)
      .send({ message: "Invalid input", details: error.validation });
  }
  reply.code(error.statusCode ?? 500).send({ message: error.message });
});
```

Errors made with `@fastify/error` are typed as `FastifyError` too, and you can check them with `instanceof`.

## 420: What is the difference between FastifyPluginAsync and FastifyPluginCallback?

They are the TypeScript types for the two plugin styles:

```ts
const a: FastifyPluginAsync<Opts> = async (app, opts) => {
  /* ... */
};

const b: FastifyPluginCallback<Opts> = (app, opts, done) => {
  done();
};
```

Both accept generics for options and the server type. The TypeBox, Zod and json-schema-to-ts providers have their own variants (for example `FastifyPluginAsyncTypebox`) so the instance inside is already typed with the provider.

## 421: How would you approach performance tuning of a slow endpoint step by step?

1. Measure: get p50/p95/p99 from metrics or logs for that route.
2. Reproduce locally with `autocannon` against the same data shape.
3. Profile with `clinic flame` or `--cpu-prof` to see where time goes.
4. Separate waiting (database, network) from CPU (serialization, loops).
5. For waiting: add indexes, batch queries, cache, run calls in parallel.
6. For CPU: add a response schema, avoid big object copies, move heavy work to workers.
7. Measure again and keep the change only if it helped.

## 422: When is a response schema not worth it for performance?

When the route returns tiny payloads, strings or buffers, or the cost is all in the database. Then serialization is a small part of the total time. It is still worth it for security (it filters fields) and documentation, so most teams add response schemas anyway and do not do it only for speed.

## 423: How do you choose between sync and async handlers for performance?

Async functions add a small overhead because of promise creation. For extremely hot routes returning a constant, a sync handler with `reply.send()` can be slightly faster. In real apps where handlers do I/O, the difference is noise. Choose async for readability and correct error handling.

## 424: How does Fastify handle request pipelining and keep-alive?

Node.js's HTTP server handles keep-alive and pipelining at the socket level. Fastify processes each request as it comes. With keep-alive, many requests share one socket, which saves TCP and TLS handshakes. `maxRequestsPerSocket` can cap how many requests one socket serves, which helps spread load after scaling events, since long-lived connections otherwise stick to old instances.

## 425: How do you spread load when clients keep long-lived keep-alive connections?

When you add new instances, existing keep-alive connections stay on old ones. Options:

- Set `maxRequestsPerSocket` so clients reconnect after N requests.
- Set a reasonable `keepAliveTimeout`.
- Use a load balancer that balances per request (HTTP/2 or L7 load balancers) instead of per connection.

## 426: How do you design a plugin that needs async setup and a clean shutdown?

```js
import fp from "fastify-plugin";
import { Kafka } from "kafkajs";

export default fp(
  async function kafkaPlugin(app, opts) {
    const kafka = new Kafka({ brokers: opts.brokers });
    const producer = kafka.producer();

    await producer.connect();
    app.decorate("kafka", { producer });

    app.addHook("onClose", async () => {
      await producer.disconnect();
    });
  },
  { name: "kafka" },
);
```

The plugin connects during boot (so the app fails fast if Kafka is down), exposes the client through a decorator and disconnects in `onClose`. Use `preClose` instead if the client must stop before in-flight requests finish.

## 427: How do you avoid a slow plugin from delaying startup too much?

- Increase `pluginTimeout` only for that reason, not as a habit.
- Connect lazily if the dependency is optional, and report readiness through the readiness probe.
- Run independent setup in parallel inside one plugin with `Promise.all`, since plugins themselves load in order.
- Add retries with backoff for dependencies that might be starting at the same time (common in Docker Compose).

## 428: What happens to in-flight requests when a hook rejects after the handler started?

Hooks before the handler (`onRequest` to `preHandler`) stop the lifecycle and go to the error handler. Hooks after the handler (`preSerialization`, `onSend`) can also fail, and then the error handler runs instead of sending the original payload. `onResponse` runs after sending, so errors there are only logged. This means an `onSend` bug can turn successful responses into 500s, so keep those hooks simple.

## 429: How do you handle a client that disconnects in the middle of a long stream?

When the client disconnects, the response stream is destroyed. If you used `reply.send(stream)`, Fastify destroys your source stream too, which stops the work (for example closing a DB cursor). If you write to `reply.raw` yourself, listen for `close` and clean up:

```js
request.raw.on("close", () => {
  if (!reply.raw.writableEnded) {
    cursor.close();
  }
});
```

Also `request.signal` aborts in this case, which works with fetch and many drivers.

## 430: How would you implement server-side caching of whole responses?

For GET routes with responses that are the same for everyone:

```js
app.addHook("onRequest", async (request, reply) => {
  if (request.method !== "GET" || !request.routeOptions.config.cache) return;
  const hit = await app.redis.get(`page:${request.url}`);
  if (hit) {
    reply.header("X-Cache", "HIT").type("application/json");
    return reply.send(hit);
  }
});

app.addHook("onSend", async (request, reply, payload) => {
  const ttl = request.routeOptions.config.cache;
  if (
    ttl &&
    reply.statusCode === 200 &&
    typeof payload === "string" &&
    !reply.hasHeader("X-Cache")
  ) {
    await app.redis.set(`page:${request.url}`, payload, "EX", ttl);
  }
  return payload;
});
```

Never cache responses that depend on the user unless the user is part of the key. A CDN with `Cache-Control` headers is often simpler.

## 431: How do you support both JSON and protobuf on the same endpoint?

Add a parser for protobuf and pick the serializer based on `Accept`:

```js
app.addContentTypeParser(
  "application/x-protobuf",
  { parseAs: "buffer" },
  async (request, body) => {
    return Order.decode(body);
  },
);

app.post("/orders", async (request, reply) => {
  const order = await createOrder(request.body);
  if (request.headers.accept === "application/x-protobuf") {
    reply.type("application/x-protobuf");
    return Buffer.from(Order.encode(order).finish());
  }
  return order;
});
```

JSON Schema validation does not apply to protobuf bodies, so validate them after decoding.

## 432: How do you build an API gateway on Fastify?

Combine:

- `@fastify/http-proxy` or `@fastify/reply-from` for forwarding.
- Auth in an `onRequest` hook, with the user ID forwarded in a header to upstreams.
- `@fastify/rate-limit` with Redis.
- `@fastify/otel` for tracing across services.
- Circuit breakers and timeouts per upstream.

```js
app.register(proxy, {
  upstream: "http://orders:3000",
  prefix: "/orders",
  preHandler: app.authenticate,
  replyOptions: {
    rewriteRequestHeaders: (req, headers) => ({
      ...headers,
      "x-user-id": req.user.sub,
    }),
  },
});
```

Make sure upstreams only accept traffic from the gateway, since they trust the `x-user-id` header.

## 433: How do you ensure correct behavior when the same plugin is registered in two places?

Without `fastify-plugin`, each registration creates a separate context, so the plugin runs twice with separate state. That is fine for route plugins mounted under different prefixes. For shared resources (a db client), registering twice opens two pools. Use `fastify-plugin` with a `name` and check `app.hasPlugin(name)` in callers, or register it once at the root.

## 434: What are the trade-offs of @fastify/autoload in a big project?

Pros: less boilerplate, folder structure drives prefixes, consistent layout.

Cons: harder to see the full plugin tree from one file, plugin order depends on file names and `dependencies` metadata, and bundlers struggle with dynamic imports. Use `autoHooks`, `cascadeHooks` and `dependencies` carefully, and print the tree with `printPlugins()` to check it matches what you expect.

## 435: How do you bundle a Fastify app with esbuild or similar?

It is possible, but watch for:

- Dynamic `import()` in `@fastify/autoload` (bundlers cannot see those files). Register plugins explicitly instead.
- Pino transports, which load files by path in a worker thread. Use `pino`'s bundler support or keep `node_modules` for transports.
- Native modules (argon2, sodium) that cannot be bundled.

Many teams skip bundling for servers and ship `node_modules`, using bundling only for serverless cold starts.

## 436: How do you migrate a large Express codebase where middleware depends on req and res mutations?

1. Wrap the Express app with `@fastify/express` and run it inside Fastify.
2. Note that middleware mutations to `req` are visible on `request.raw`, not on Fastify's `request`.
3. Replace cross-cutting middleware (auth, logging, CORS) with Fastify hooks first, decorating `request` with values like `user`.
4. Move routes by area into Fastify plugins with schemas.
5. Add tests with `inject()` for each moved area before deleting the Express version.
6. Remove `@fastify/express` at the end.

The hard part is usually auth and error handling, so plan those first.

## 437: How do you run Express and Fastify side by side during a migration without @fastify/express?

Put a reverse proxy (Nginx, the cloud load balancer) in front and route paths to the two apps. This keeps them fully separate, which avoids mixing middleware semantics, at the cost of running two services. It also lets you roll back by changing a routing rule.

## 438: How do you implement request signing verification as a reusable plugin?

```js
import fp from "fastify-plugin";
import crypto from "node:crypto";

export default fp(
  async (app, opts) => {
    app.decorate("verifySignature", async (request, reply) => {
      const signature = request.headers["x-signature"];
      const expected = crypto
        .createHmac("sha256", opts.secret)
        .update(request.rawBody)
        .digest("hex");
      const a = Buffer.from(signature ?? "", "hex");
      const b = Buffer.from(expected, "hex");
      if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) {
        return reply.code(401).send({ message: "Bad signature" });
      }
    });
  },
  { name: "signature", dependencies: ["raw-body"] },
);
```

Use `timingSafeEqual` to avoid timing attacks, verify the raw body (not re-serialized JSON) and also check a timestamp header to block replays.

## 439: How do you handle very high cardinality logging fields without hurting performance?

- Do not log full bodies or headers at `info`.
- Put large or high-cardinality data at `debug` and keep it off in production.
- Use `redact` with `remove: true` instead of custom serializers that copy objects.
- Sample: log details for a small percent of requests, and always for errors and slow requests.

## 440: What happens to hooks and the handler when you call reply.hijack() in onRequest?

After `hijack()`, Fastify stops the normal lifecycle. Later hooks and the handler do not run, `onSend` and `onResponse` are skipped, and `handlerTimeout` is cleared. You are fully responsible for writing and ending `reply.raw`. Logging of the response status also does not happen, so log it yourself if needed.

## 441: How do you test error handling for errors thrown in hooks, handlers and serialization?

Write one test per source of error and check the status and body:

```js
test("serialization error becomes 500", async () => {
  const app = Fastify();
  app.get(
    "/",
    {
      schema: {
        response: {
          200: {
            type: "object",
            required: ["id"],
            properties: { id: { type: "integer" } },
          },
        },
      },
    },
    async () => ({}),
  );

  const res = await app.inject("/");
  assert.strictEqual(res.statusCode, 500);
});
```

Do the same for hooks throwing, validation failing and async errors in parsers. These paths are easy to forget and often have different log levels.

## 442: How would you design a plugin system for third-party extensions in your own Fastify product?

- Give each extension its own encapsulated context with a prefix like `/ext/:name`.
- Expose a small, stable API through decorators instead of the full app (for example `app.ext.storage`, `app.ext.events`).
- Validate extension options with schemas at load time.
- Set `pluginTimeout` so a broken extension cannot hang boot, and catch boot errors per extension if you want to skip bad ones.
- Use `onRoute` to enforce rules (every extension route needs auth and a schema).
- Run untrusted code in a separate process, since encapsulation is not a security sandbox.

## 443: Is encapsulation a security boundary?

No. Encapsulation controls what a plugin can see through the Fastify API, but it is all one JavaScript process. A plugin can import any module, read `process.env`, change prototypes or reach the parent instance through the prototype chain. It is a tool for organizing code, not for isolating untrusted code. Use separate processes, containers or worker threads with limited permissions for that.

## 444: How do you handle schema evolution without breaking clients?

- Add new fields as optional. Old clients ignore them.
- Do not remove or rename response fields in the same version. Mark them deprecated in OpenAPI first.
- For request bodies, accept old and new field names for a while, mapping old ones in `preValidation`.
- Keep `additionalProperties: false` for requests only if you are ready to reject unknown fields; otherwise new clients sending new fields to old servers fail.
- Use API versions when a breaking change is unavoidable.

## 445: How do you generate client types from a Fastify API?

Generate an OpenAPI spec from `@fastify/swagger` (for example in a build script with `await app.ready(); app.swagger()`), then generate clients with tools like `openapi-typescript` or `orval`:

```js
const app = await buildApp();
await app.ready();
await fs.promises.writeFile(
  "openapi.json",
  JSON.stringify(app.swagger(), null, 2),
);
```

Because the spec comes from the same schemas used for validation, the client types match what the server enforces. Run this in CI and fail if the committed spec is out of date.

## 446: How do you handle timezone and date formats in v5 validation?

In v5, `format: 'date-time'` and `format: 'time'` require a timezone (like `Z` or `+02:00`). A value like `2026-10-29T10:00:00` without a timezone now fails. If you must accept values without a timezone, use `iso-date-time` or `iso-time`. Prefer requiring timezones, since a time without one is ambiguous and leads to bugs across regions.

## 447: What are the risks of setting requestIdHeader in a public API?

The client can set the request ID to any value. This can:

- Make different requests share an ID and confuse tracing.
- Put very long or strange strings into logs.
- Be used to inject content into log systems that render it.

Only use `requestIdHeader` when the header comes from your own gateway, which overwrites any client value. Otherwise, use `genReqId` and validate the incoming value (length, characters) before using it.

## 448: How do you debug a request that hangs and never responds?

Common causes:

- A callback-style hook or handler that never calls `done()` or `reply.send()`.
- An async handler that returns `undefined` without sending (Fastify logs a warning).
- A file stream from multipart that is never consumed.
- A promise that never resolves (a DB pool exhausted, waiting forever for a connection).

To find it, turn on `debug` logs, add `handlerTimeout` so hung requests fail with a clear error, and add logs in each hook. Check pool usage metrics for exhausted connections.

## 449: What should you check before upgrading to a new Fastify major version, such as v6?

- Read the migration guide and the release notes for each alpha or release candidate.
- Fix all deprecation warnings on the current major first. For example, v5 already warns about the top-level `disableRequestLogging` and `requestIdLogLabel` options, which are set to be removed in v6.
- Check that every `@fastify/*` and community plugin has a compatible version.
- Check the required Node.js version.
- Run the full test suite and a load test, since defaults (timeouts, parsing strictness) can change.
- Roll out to a small part of traffic first.

## 450: If you had to explain why a team should choose Fastify for a new API, what would you say?

- It is fast, and the speed comes with no extra work: schemas give both validation and faster serialization.
- JSON Schema makes inputs safe and outputs filtered, and the same schemas generate OpenAPI docs and TypeScript types.
- The plugin system with encapsulation keeps a large codebase organized and lets features have their own hooks and error handlers.
- Logging, testing with `inject()` and graceful shutdown are built in.
- The official plugins cover most needs (auth, CORS, rate limiting, uploads, OpenAPI, WebSockets).
- It is maintained under the OpenJS Foundation with a clear LTS policy.

The trade-offs are a smaller ecosystem than Express and a learning curve around encapsulation, which is the part new team members most often get wrong.
