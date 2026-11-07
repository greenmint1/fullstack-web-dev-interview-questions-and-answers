# NestJS Interview Questions and Answers

_Last updated: October 28, 2026_

450 NestJS interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for **NestJS 12** (released in August 2026). Most of them also apply to NestJS 10 and 11. When something works differently in a recent version, the answer says so.

Code examples use TypeScript. Test examples use Vitest (`vi.fn()`); with Jest, replace `vi` with `jest`.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is NestJS?](#1-what-is-nestjs)
- [2: Why would you pick NestJS over plain Express?](#2-why-would-you-pick-nestjs-over-plain-express)
- [3: What is the current major version of NestJS and what are the headline changes?](#3-what-is-the-current-major-version-of-nestjs-and-what-are-the-headline-changes)
- [4: Which Node.js version do you need for NestJS 12?](#4-which-nodejs-version-do-you-need-for-nestjs-12)
- [5: How do you install the Nest CLI and create a new project?](#5-how-do-you-install-the-nest-cli-and-create-a-new-project)
- [6: What files does a new Nest project contain?](#6-what-files-does-a-new-nest-project-contain)
- [7: What does `main.ts` usually look like?](#7-what-does-maints-usually-look-like)
- [8: What is `NestFactory`?](#8-what-is-nestfactory)
- [9: What is a module in NestJS?](#9-what-is-a-module-in-nestjs)
- [10: What properties does the `@Module()` decorator accept?](#10-what-properties-does-the-module-decorator-accept)
- [11: What is a controller?](#11-what-is-a-controller)
- [12: What is a provider?](#12-what-is-a-provider)
- [13: What is a service in NestJS?](#13-what-is-a-service-in-nestjs)
- [14: What does `@Injectable()` do?](#14-what-does-injectable-do)
- [15: What is dependency injection?](#15-what-is-dependency-injection)
- [16: How does Nest know what to inject in a constructor?](#16-how-does-nest-know-what-to-inject-in-a-constructor)
- [17: What is the default scope of a provider?](#17-what-is-the-default-scope-of-a-provider)
- [18: What are the HTTP method decorators in Nest?](#18-what-are-the-http-method-decorators-in-nest)
- [19: How do you read a route parameter?](#19-how-do-you-read-a-route-parameter)
- [20: How do you read query string values?](#20-how-do-you-read-query-string-values)
- [21: How do you read the request body?](#21-how-do-you-read-the-request-body)
- [22: What is a DTO?](#22-what-is-a-dto)
- [23: Why should DTOs be classes and not interfaces?](#23-why-should-dtos-be-classes-and-not-interfaces)
- [24: How do you get the full request object?](#24-how-do-you-get-the-full-request-object)
- [25: How do you read request headers?](#25-how-do-you-read-request-headers)
- [26: How do you change the response status code?](#26-how-do-you-change-the-response-status-code)
- [27: How do you set a custom response header?](#27-how-do-you-set-a-custom-response-header)
- [28: How do you redirect from a route?](#28-how-do-you-redirect-from-a-route)
- [29: Can a controller method be `async`?](#29-can-a-controller-method-be-async)
- [30: What happens when a controller method returns an object?](#30-what-happens-when-a-controller-method-returns-an-object)
- [31: What does `@Res()` do and why is it not recommended?](#31-what-does-res-do-and-why-is-it-not-recommended)
- [32: How do you register a controller?](#32-how-do-you-register-a-controller)
- [33: How do you generate files with the CLI?](#33-how-do-you-generate-files-with-the-cli)
- [34: What does `nest g resource` do?](#34-what-does-nest-g-resource-do)
- [35: How do you run a Nest app in watch mode?](#35-how-do-you-run-a-nest-app-in-watch-mode)
- [36: What does `nest build` do?](#36-what-does-nest-build-do)
- [37: What is `nest-cli.json` used for?](#37-what-is-nest-clijson-used-for)
- [38: What does the `exports` array in a module do?](#38-what-does-the-exports-array-in-a-module-do)
- [39: How do you use a service from another module?](#39-how-do-you-use-a-service-from-another-module)
- [40: What is a shared module?](#40-what-is-a-shared-module)
- [41: What is a global module?](#41-what-is-a-global-module)
- [42: What is a feature module?](#42-what-is-a-feature-module)
- [43: Can a module re-export a module it imports?](#43-can-a-module-re-export-a-module-it-imports)
- [44: What are pipes?](#44-what-are-pipes)
- [45: Which built-in pipes does Nest provide?](#45-which-built-in-pipes-does-nest-provide)
- [46: How do you use `ParseIntPipe`?](#46-how-do-you-use-parseintpipe)
- [47: How do you give a query parameter a default value?](#47-how-do-you-give-a-query-parameter-a-default-value)
- [48: What is `ParseDatePipe`?](#48-what-is-parsedatepipe)
- [49: How do you validate the request body with `class-validator`?](#49-how-do-you-validate-the-request-body-with-class-validator)
- [50: What does `whitelist: true` do in `ValidationPipe`?](#50-what-does-whitelist-true-do-in-validationpipe)
- [51: What does `transform: true` do in `ValidationPipe`?](#51-what-does-transform-true-do-in-validationpipe)
- [52: What is Standard Schema validation in NestJS 12?](#52-what-is-standard-schema-validation-in-nestjs-12)
- [53: What are guards?](#53-what-are-guards)
- [54: How do you apply a guard?](#54-how-do-you-apply-a-guard)
- [55: What happens when a guard returns `false`?](#55-what-happens-when-a-guard-returns-false)
- [56: What are interceptors?](#56-what-are-interceptors)
- [57: How do you apply an interceptor?](#57-how-do-you-apply-an-interceptor)
- [58: What is middleware in NestJS?](#58-what-is-middleware-in-nestjs)
- [59: How do you register middleware?](#59-how-do-you-register-middleware)
- [60: How do you add middleware for all routes?](#60-how-do-you-add-middleware-for-all-routes)
- [61: What is functional middleware?](#61-what-is-functional-middleware)
- [62: What are exception filters?](#62-what-are-exception-filters)
- [63: What does the default error response look like?](#63-what-does-the-default-error-response-look-like)
- [64: How do you throw an HTTP error?](#64-how-do-you-throw-an-http-error)
- [65: Name some built-in HTTP exceptions.](#65-name-some-built-in-http-exceptions)
- [66: How do you throw an `HttpException` with a custom body?](#66-how-do-you-throw-an-httpexception-with-a-custom-body)
- [67: What is the `cause` option on exceptions?](#67-what-is-the-cause-option-on-exceptions)
- [68: What is the `errorCode` option added in Nest 12?](#68-what-is-the-errorcode-option-added-in-nest-12)
- [69: How do you enable CORS?](#69-how-do-you-enable-cors)
- [70: How do you add a global prefix like `/api`?](#70-how-do-you-add-a-global-prefix-like-api)
- [71: How do you read environment variables in Nest?](#71-how-do-you-read-environment-variables-in-nest)
- [72: What is the difference between `ConfigService.get()` and `getOrThrow()`?](#72-what-is-the-difference-between-configserviceget-and-getorthrow)
- [73: How do you use the built-in logger?](#73-how-do-you-use-the-built-in-logger)
- [74: What log levels does the Nest logger have?](#74-what-log-levels-does-the-nest-logger-have)
- [75: How do you print logs as JSON?](#75-how-do-you-print-logs-as-json)
- [76: What is structured logging in Nest 12?](#76-what-is-structured-logging-in-nest-12)
- [77: How do you switch from Express to Fastify?](#77-how-do-you-switch-from-express-to-fastify)
- [78: Which Express and Fastify versions does Nest use now?](#78-which-express-and-fastify-versions-does-nest-use-now)
- [79: What is a platform-agnostic framework?](#79-what-is-a-platform-agnostic-framework)
- [80: What are the main building blocks of a Nest app?](#80-what-are-the-main-building-blocks-of-a-nest-app)
- [81: In what order do middleware, guards, interceptors, pipes and filters run?](#81-in-what-order-do-middleware-guards-interceptors-pipes-and-filters-run)
- [82: What is a decorator?](#82-what-is-a-decorator)
- [83: Does NestJS work with JavaScript instead of TypeScript?](#83-does-nestjs-work-with-javascript-instead-of-typescript)
- [84: What TypeScript compiler options does Nest need?](#84-what-typescript-compiler-options-does-nest-need)
- [85: How do you serve static files?](#85-how-do-you-serve-static-files)
- [86: How do you upload a single file?](#86-how-do-you-upload-a-single-file)
- [87: How do you upload several files?](#87-how-do-you-upload-several-files)
- [88: How do you read cookies?](#88-how-do-you-read-cookies)
- [89: How do you set a cookie?](#89-how-do-you-set-a-cookie)
- [90: How do you write a simple unit test for a service?](#90-how-do-you-write-a-simple-unit-test-for-a-service)
- [91: Which test runner does Nest use?](#91-which-test-runner-does-nest-use)
- [92: What is `Test.createTestingModule()`?](#92-what-is-testcreatetestingmodule)
- [93: How do you mock a dependency in a unit test?](#93-how-do-you-mock-a-dependency-in-a-unit-test)
- [94: What is an end-to-end (e2e) test in Nest?](#94-what-is-an-end-to-end-e2e-test-in-nest)
- [95: What is the difference between `app.init()` and `app.listen()`?](#95-what-is-the-difference-between-appinit-and-applisten)
- [96: How do you add Swagger docs to a Nest app?](#96-how-do-you-add-swagger-docs-to-a-nest-app)
- [97: What does `@ApiProperty()` do?](#97-what-does-apiproperty-do)
- [98: How do you connect to a SQL database with TypeORM?](#98-how-do-you-connect-to-a-sql-database-with-typeorm)
- [99: How do you inject a TypeORM repository?](#99-how-do-you-inject-a-typeorm-repository)
- [100: How do you connect to MongoDB?](#100-how-do-you-connect-to-mongodb)
- [101: How do you use Prisma with Nest?](#101-how-do-you-use-prisma-with-nest)
- [102: What is the difference between `providers` and `controllers` in a module?](#102-what-is-the-difference-between-providers-and-controllers-in-a-module)
- [103: Can you inject a provider into another provider?](#103-can-you-inject-a-provider-into-another-provider)
- [104: What happens if Nest cannot find a dependency?](#104-what-happens-if-nest-cannot-find-a-dependency)
- [105: What is the root module?](#105-what-is-the-root-module)
- [106: How do you enable versioning of routes?](#106-how-do-you-enable-versioning-of-routes)
- [107: What is `@nestjs/terminus` for?](#107-what-is-nestjsterminus-for)
- [108: How do you cache responses?](#108-how-do-you-cache-responses)
- [109: How do you run a job on a schedule?](#109-how-do-you-run-a-job-on-a-schedule)
- [110: What is `@nestjs/event-emitter` used for?](#110-what-is-nestjsevent-emitter-used-for)
- [111: What is a WebSocket gateway?](#111-what-is-a-websocket-gateway)
- [112: What is a microservice in NestJS?](#112-what-is-a-microservice-in-nestjs)
- [113: What is the difference between `@MessagePattern()` and `@EventPattern()`?](#113-what-is-the-difference-between-messagepattern-and-eventpattern)
- [114: Does Nest support GraphQL?](#114-does-nest-support-graphql)
- [115: What is a resolver in Nest GraphQL?](#115-what-is-a-resolver-in-nest-graphql)
- [116: How do you get the client IP address?](#116-how-do-you-get-the-client-ip-address)
- [117: What does `@All()` do?](#117-what-does-all-do)
- [118: How do wildcard routes work in Nest 11 and 12?](#118-how-do-wildcard-routes-work-in-nest-11-and-12)
- [119: How do you make a route parameter optional in Express 5 style paths?](#119-how-do-you-make-a-route-parameter-optional-in-express-5-style-paths)
- [120: What is `@HostParam()`?](#120-what-is-hostparam)
- [121: How do you read a value from the session?](#121-how-do-you-read-a-value-from-the-session)
- [122: How do you close a Nest app?](#122-how-do-you-close-a-nest-app)
- [123: What does `app.enableShutdownHooks()` do?](#123-what-does-appenableshutdownhooks-do)
- [124: What are lifecycle hooks?](#124-what-are-lifecycle-hooks)
- [125: How do you use `onModuleInit()`?](#125-how-do-you-use-onmoduleinit)
- [126: What is an entity?](#126-what-is-an-entity)
- [127: What is the difference between an entity and a DTO?](#127-what-is-the-difference-between-an-entity-and-a-dto)
- [128: How do you make all properties of a DTO optional for update requests?](#128-how-do-you-make-all-properties-of-a-dto-optional-for-update-requests)
- [129: What does the `@Optional()` decorator do?](#129-what-does-the-optional-decorator-do)
- [130: What does `@Inject()` do?](#130-what-does-inject-do)
- [131: What is a custom provider with `useValue`?](#131-what-is-a-custom-provider-with-usevalue)
- [132: How do you protect against common web attacks with headers?](#132-how-do-you-protect-against-common-web-attacks-with-headers)
- [133: How do you add rate limiting?](#133-how-do-you-add-rate-limiting)
- [134: What is `@SkipThrottle()`?](#134-what-is-skipthrottle)
- [135: What does `nest info` show?](#135-what-does-nest-info-show)
- [136: How do you upgrade a project to the latest Nest version?](#136-how-do-you-upgrade-a-project-to-the-latest-nest-version)
- [137: Should Nest packages be on the same version?](#137-should-nest-packages-be-on-the-same-version)
- [138: What does `ESM` mean for Nest 12 users?](#138-what-does-esm-mean-for-nest-12-users)
- [139: What is the SWC builder?](#139-what-is-the-swc-builder)
- [140: What is Rspack in the Nest CLI?](#140-what-is-rspack-in-the-nest-cli)
- [141: What is the difference between `Get()` and `Get('')`?](#141-what-is-the-difference-between-get-and-get)
- [142: Can two controllers share the same route path?](#142-can-two-controllers-share-the-same-route-path)
- [143: How do you return a file download?](#143-how-do-you-return-a-file-download)
- [144: How do you render an HTML template?](#144-how-do-you-render-an-html-template)
- [145: What does `@nestjs/axios` provide?](#145-what-does-nestjsaxios-provide)
- [146: Can you use the native `fetch` instead of `@nestjs/axios`?](#146-can-you-use-the-native-fetch-instead-of-nestjsaxios)
- [147: What is a monorepo in Nest CLI terms?](#147-what-is-a-monorepo-in-nest-cli-terms)
- [148: How do you get a provider instance outside of DI, for example in `main.ts`?](#148-how-do-you-get-a-provider-instance-outside-of-di-for-example-in-maints)
- [149: What is a standalone application?](#149-what-is-a-standalone-application)
- [150: Where can you find official help and docs?](#150-where-can-you-find-official-help-and-docs)

### Moderate Questions (151-300)

- [151: What kinds of custom providers are there?](#151-what-kinds-of-custom-providers-are-there)
- [152: When would you use `useClass` with a different class than the token?](#152-when-would-you-use-useclass-with-a-different-class-than-the-token)
- [153: How do you write a factory provider that depends on other providers?](#153-how-do-you-write-a-factory-provider-that-depends-on-other-providers)
- [154: What is an async provider?](#154-what-is-an-async-provider)
- [155: What does `useExisting` do?](#155-what-does-useexisting-do)
- [156: Why use a `Symbol` or an `InjectionToken` instead of a string token?](#156-why-use-a-symbol-or-an-injectiontoken-instead-of-a-string-token)
- [157: How do you inject an interface implementation?](#157-how-do-you-inject-an-interface-implementation)
- [158: What is a dynamic module?](#158-what-is-a-dynamic-module)
- [159: What is the difference between `forRoot`, `register` and `forFeature`?](#159-what-is-the-difference-between-forroot-register-and-forfeature)
- [160: What is `forRootAsync` and why is it useful?](#160-what-is-forrootasync-and-why-is-it-useful)
- [161: What is `ConfigurableModuleBuilder`?](#161-what-is-configurablemodulebuilder)
- [162: How do you rename the generated method to `forRoot` with `ConfigurableModuleBuilder`?](#162-how-do-you-rename-the-generated-method-to-forroot-with-configurablemodulebuilder)
- [163: What are the injection scopes?](#163-what-are-the-injection-scopes)
- [164: What is scope bubbling?](#164-what-is-scope-bubbling)
- [165: How do you get the current request inside a service?](#165-how-do-you-get-the-current-request-inside-a-service)
- [166: What is the downside of request-scoped providers?](#166-what-is-the-downside-of-request-scoped-providers)
- [167: What does `INQUIRER` do?](#167-what-does-inquirer-do)
- [168: What is a circular dependency and how do you solve it in Nest?](#168-what-is-a-circular-dependency-and-how-do-you-solve-it-in-nest)
- [169: What is `ModuleRef`?](#169-what-is-moduleref)
- [170: What is the difference between `moduleRef.get()` and `moduleRef.resolve()`?](#170-what-is-the-difference-between-modulerefget-and-modulerefresolve)
- [171: What does `moduleRef.create()` do?](#171-what-does-modulerefcreate-do)
- [172: What are the different binding levels for pipes, guards, interceptors and filters?](#172-what-are-the-different-binding-levels-for-pipes-guards-interceptors-and-filters)
- [173: Why use `APP_GUARD` instead of `app.useGlobalGuards()`?](#173-why-use-app_guard-instead-of-appuseglobalguards)
- [174: In what order do multiple guards run?](#174-in-what-order-do-multiple-guards-run)
- [175: In what order do interceptors run before and after the handler?](#175-in-what-order-do-interceptors-run-before-and-after-the-handler)
- [176: In what order do exception filters run?](#176-in-what-order-do-exception-filters-run)
- [177: What is `ExecutionContext`?](#177-what-is-executioncontext)
- [178: What is `ArgumentsHost`?](#178-what-is-argumentshost)
- [179: How do you write a custom exception filter?](#179-how-do-you-write-a-custom-exception-filter)
- [180: How do you catch every exception, not just `HttpException`?](#180-how-do-you-catch-every-exception-not-just-httpexception)
- [181: How do you extend the built-in exception filter?](#181-how-do-you-extend-the-built-in-exception-filter)
- [182: How do you create your own exception class?](#182-how-do-you-create-your-own-exception-class)
- [183: How do you write a custom pipe?](#183-how-do-you-write-a-custom-pipe)
- [184: What is in `ArgumentMetadata`?](#184-what-is-in-argumentmetadata)
- [185: How do you write a guard that checks roles?](#185-how-do-you-write-a-guard-that-checks-roles)
- [186: What is the difference between `Reflector.createDecorator()` and `SetMetadata()`?](#186-what-is-the-difference-between-reflectorcreatedecorator-and-setmetadata)
- [187: What is the difference between `getAllAndOverride` and `getAllAndMerge`?](#187-what-is-the-difference-between-getallandoverride-and-getallandmerge)
- [188: How do you make some routes public when you have a global auth guard?](#188-how-do-you-make-some-routes-public-when-you-have-a-global-auth-guard)
- [189: How do you create a custom parameter decorator?](#189-how-do-you-create-a-custom-parameter-decorator)
- [190: Do pipes run on custom parameter decorators?](#190-do-pipes-run-on-custom-parameter-decorators)
- [191: How do you combine several decorators into one?](#191-how-do-you-combine-several-decorators-into-one)
- [192: How do you implement JWT authentication without Passport?](#192-how-do-you-implement-jwt-authentication-without-passport)
- [193: How do you use Passport with Nest?](#193-how-do-you-use-passport-with-nest)
- [194: How do you implement refresh tokens?](#194-how-do-you-implement-refresh-tokens)
- [195: How do you validate nested objects?](#195-how-do-you-validate-nested-objects)
- [196: How do you validate an array of DTOs in the body?](#196-how-do-you-validate-an-array-of-dtos-in-the-body)
- [197: What does `enableImplicitConversion` do?](#197-what-does-enableimplicitconversion-do)
- [198: How do you write a custom `class-validator` rule?](#198-how-do-you-write-a-custom-class-validator-rule)
- [199: How do you make a `class-validator` constraint use Nest DI (for example to check the database)?](#199-how-do-you-make-a-class-validator-constraint-use-nest-di-for-example-to-check-the-database)
- [200: What is the `errorFormat` option on `ValidationPipe` in Nest 12?](#200-what-is-the-errorformat-option-on-validationpipe-in-nest-12)
- [201: How do you change the error response of `StandardSchemaValidationPipe`?](#201-how-do-you-change-the-error-response-of-standardschemavalidationpipe)
- [202: Is it safe to bind `StandardSchemaValidationPipe` globally?](#202-is-it-safe-to-bind-standardschemavalidationpipe-globally)
- [203: Can you use `ValidationPipe` and `StandardSchemaValidationPipe` together?](#203-can-you-use-validationpipe-and-standardschemavalidationpipe-together)
- [204: What are mapped types?](#204-what-are-mapped-types)
- [205: How do you hide fields like `password` in responses?](#205-how-do-you-hide-fields-like-password-in-responses)
- [206: What does `@SerializeOptions()` do?](#206-what-does-serializeoptions-do)
- [207: How do you write an interceptor that wraps every response in `{ data: ... }`?](#207-how-do-you-write-an-interceptor-that-wraps-every-response-in--data--)
- [208: How do you add a timeout to every request?](#208-how-do-you-add-a-timeout-to-every-request)
- [209: How can an interceptor return a response without calling the handler?](#209-how-can-an-interceptor-return-a-response-without-calling-the-handler)
- [210: How do you map database errors to HTTP errors in one place?](#210-how-do-you-map-database-errors-to-http-errors-in-one-place)
- [211: How do you exclude routes from middleware?](#211-how-do-you-exclude-routes-from-middleware)
- [212: Can middleware use dependency injection?](#212-can-middleware-use-dependency-injection)
- [213: When should you use middleware vs a guard vs an interceptor?](#213-when-should-you-use-middleware-vs-a-guard-vs-an-interceptor)
- [214: How do you use namespaced configuration with `registerAs`?](#214-how-do-you-use-namespaced-configuration-with-registeras)
- [215: How do you validate environment variables at startup?](#215-how-do-you-validate-environment-variables-at-startup)
- [216: What options does `ConfigModule.forRoot()` have that are useful in practice?](#216-what-options-does-configmoduleforroot-have-that-are-useful-in-practice)
- [217: How do you add a typed `ConfigService`?](#217-how-do-you-add-a-typed-configservice)
- [218: What changed in caching in Nest 11 and is still true in 12?](#218-what-changed-in-caching-in-nest-11-and-is-still-true-in-12)
- [219: How do you use the cache manager directly?](#219-how-do-you-use-the-cache-manager-directly)
- [220: How do you change the cache key or TTL for one route?](#220-how-do-you-change-the-cache-key-or-ttl-for-one-route)
- [221: Which requests does `CacheInterceptor` cache?](#221-which-requests-does-cacheinterceptor-cache)
- [222: How do you use several rate limits at once with the throttler?](#222-how-do-you-use-several-rate-limits-at-once-with-the-throttler)
- [223: How do you share rate limit counters across several app instances?](#223-how-do-you-share-rate-limit-counters-across-several-app-instances)
- [224: How do you rate limit by user instead of IP?](#224-how-do-you-rate-limit-by-user-instead-of-ip)
- [225: What versioning types does Nest support?](#225-what-versioning-types-does-nest-support)
- [226: How do you serve two versions of the same route?](#226-how-do-you-serve-two-versions-of-the-same-route)
- [227: What is `defaultVersion` in versioning?](#227-what-is-defaultversion-in-versioning)
- [228: What is `RouterModule`?](#228-what-is-routermodule)
- [229: How do you document authentication and responses in Swagger?](#229-how-do-you-document-authentication-and-responses-in-swagger)
- [230: What does the Swagger CLI plugin do?](#230-what-does-the-swagger-cli-plugin-do)
- [231: How do you validate uploaded files?](#231-how-do-you-validate-uploaded-files)
- [232: How do you send Server-Sent Events?](#232-how-do-you-send-server-sent-events)
- [233: How do you get the raw request body, for example for webhook signatures?](#233-how-do-you-get-the-raw-request-body-for-example-for-webhook-signatures)
- [234: What changed about query string parsing with Express 5?](#234-what-changed-about-query-string-parsing-with-express-5)
- [235: How do you add body size limits?](#235-how-do-you-add-body-size-limits)
- [236: How do you use BullMQ queues in Nest?](#236-how-do-you-use-bullmq-queues-in-nest)
- [237: How do you add or remove cron jobs at runtime?](#237-how-do-you-add-or-remove-cron-jobs-at-runtime)
- [238: What is a problem with `@Cron()` when you run several app instances?](#238-what-is-a-problem-with-cron-when-you-run-several-app-instances)
- [239: How do you make event listeners async and catch their errors?](#239-how-do-you-make-event-listeners-async-and-catch-their-errors)
- [240: How do you send messages to a room with WebSocket gateways?](#240-how-do-you-send-messages-to-a-room-with-websocket-gateways)
- [241: How do you handle connect and disconnect in a gateway?](#241-how-do-you-handle-connect-and-disconnect-in-a-gateway)
- [242: How do you authenticate WebSocket connections?](#242-how-do-you-authenticate-websocket-connections)
- [243: How do you throw errors in a gateway?](#243-how-do-you-throw-errors-in-a-gateway)
- [244: How do you send a message from one microservice to another?](#244-how-do-you-send-a-message-from-one-microservice-to-another)
- [245: How do you create a microservice listener?](#245-how-do-you-create-a-microservice-listener)
- [246: Is `ClientProxy.send()` lazy?](#246-is-clientproxysend-lazy)
- [247: How do you read transport-specific data in a handler?](#247-how-do-you-read-transport-specific-data-in-a-handler)
- [248: How do you return errors from a microservice handler?](#248-how-do-you-return-errors-from-a-microservice-handler)
- [249: What is a hybrid application?](#249-what-is-a-hybrid-application)
- [250: What changed about the NATS transport in Nest 12?](#250-what-changed-about-the-nats-transport-in-nest-12)
- [251: How do you listen to the connection status of a microservice client?](#251-how-do-you-listen-to-the-connection-status-of-a-microservice-client)
- [252: What is the difference between code-first and schema-first in Nest GraphQL?](#252-what-is-the-difference-between-code-first-and-schema-first-in-nest-graphql)
- [253: How do you set up GraphQL with Apollo (code-first)?](#253-how-do-you-set-up-graphql-with-apollo-code-first)
- [254: What is `@ResolveField()`?](#254-what-is-resolvefield)
- [255: What is the N+1 problem in GraphQL and how do you fix it in Nest?](#255-what-is-the-n1-problem-in-graphql-and-how-do-you-fix-it-in-nest)
- [256: How do you write a mutation with an input type?](#256-how-do-you-write-a-mutation-with-an-input-type)
- [257: Which IDE does Nest GraphQL show by default now?](#257-which-ide-does-nest-graphql-show-by-default-now)
- [258: How do you get the request in a GraphQL guard?](#258-how-do-you-get-the-request-in-a-graphql-guard)
- [259: How do you override a provider in a test without rewriting the module?](#259-how-do-you-override-a-provider-in-a-test-without-rewriting-the-module)
- [260: What does `useMocker()` do in testing?](#260-what-does-usemocker-do-in-testing)
- [261: How do you test a guard on its own?](#261-how-do-you-test-a-guard-on-its-own)
- [262: How do you replace a global guard in e2e tests?](#262-how-do-you-replace-a-global-guard-in-e2e-tests)
- [263: How do you test with a real database in e2e tests?](#263-how-do-you-test-with-a-real-database-in-e2e-tests)
- [264: Why does Jest fail with `ERR_REQUIRE_ASYNC_MODULE` on Nest 12?](#264-why-does-jest-fail-with-err_require_async_module-on-nest-12)
- [265: How do you set up Vitest for a Nest project?](#265-how-do-you-set-up-vitest-for-a-nest-project)
- [266: What is `HttpAdapterHost` used for?](#266-what-is-httpadapterhost-used-for)
- [267: How do you register Fastify plugins?](#267-how-do-you-register-fastify-plugins)
- [268: Does `FileInterceptor` work with Fastify?](#268-does-fileinterceptor-work-with-fastify)
- [269: What is `@Res({ passthrough: true })` good for?](#269-what-is-res-passthrough-true--good-for)
- [270: How do you implement a transaction with TypeORM in a service?](#270-how-do-you-implement-a-transaction-with-typeorm-in-a-service)
- [271: How do you run TypeORM migrations in a Nest project?](#271-how-do-you-run-typeorm-migrations-in-a-nest-project)
- [272: How do you connect to two databases with TypeORM?](#272-how-do-you-connect-to-two-databases-with-typeorm)
- [273: How do you add Mongoose middleware (hooks) in Nest?](#273-how-do-you-add-mongoose-middleware-hooks-in-nest)
- [274: How do you handle the Prisma client shutdown?](#274-how-do-you-handle-the-prisma-client-shutdown)
- [275: How do you write a health check in Terminus for Nest 12?](#275-how-do-you-write-a-health-check-in-terminus-for-nest-12)
- [276: How does graceful shutdown work in a Nest app?](#276-how-does-graceful-shutdown-work-in-a-nest-app)
- [277: What does `bufferLogs` do?](#277-what-does-bufferlogs-do)
- [278: How do you write a custom logger?](#278-how-do-you-write-a-custom-logger)
- [279: How do you use `ConsoleLogger` options from Nest 11 and up?](#279-how-do-you-use-consolelogger-options-from-nest-11-and-up)
- [280: How do you add a request ID to every log line?](#280-how-do-you-add-a-request-id-to-every-log-line)
- [281: What is `nestjs-cls` and why is it popular?](#281-what-is-nestjs-cls-and-why-is-it-popular)
- [282: What is CQRS in NestJS?](#282-what-is-cqrs-in-nestjs)
- [283: What is a saga in `@nestjs/cqrs`?](#283-what-is-a-saga-in-nestjscqrs)
- [284: How do you use a different config per environment?](#284-how-do-you-use-a-different-config-per-environment)
- [285: How do you build an app where a guard needs a request-scoped service?](#285-how-do-you-build-an-app-where-a-guard-needs-a-request-scoped-service)
- [286: How do you load a module only in some environments?](#286-how-do-you-load-a-module-only-in-some-environments)
- [287: What does `nest start --debug` do?](#287-what-does-nest-start---debug-do)
- [288: How do you pass a custom header version and default for missing headers?](#288-how-do-you-pass-a-custom-header-version-and-default-for-missing-headers)
- [289: How do you prevent CSRF in a cookie-based Nest app?](#289-how-do-you-prevent-csrf-in-a-cookie-based-nest-app)
- [290: How do you set up compression?](#290-how-do-you-set-up-compression)
- [291: How do you set `trust proxy` in Nest?](#291-how-do-you-set-trust-proxy-in-nest)
- [292: How do you check which routes exist in an app?](#292-how-do-you-check-which-routes-exist-in-an-app)
- [293: What is the route specificity option in Nest 12?](#293-what-is-the-route-specificity-option-in-nest-12)
- [294: How do you return a custom status code from an exception filter in GraphQL?](#294-how-do-you-return-a-custom-status-code-from-an-exception-filter-in-graphql)
- [295: How do you inject config into a dynamic module with `registerAsync` using a class?](#295-how-do-you-inject-config-into-a-dynamic-module-with-registerasync-using-a-class)
- [296: Can you inject a provider into a module class?](#296-can-you-inject-a-provider-into-a-module-class)
- [297: How do you test a request-scoped provider?](#297-how-do-you-test-a-request-scoped-provider)
- [298: What does `abortOnError: false` do?](#298-what-does-abortonerror-false-do)
- [299: How do you run code once after the app starts listening?](#299-how-do-you-run-code-once-after-the-app-starts-listening)
- [300: How do you stop a long query when the client disconnects?](#300-how-do-you-stop-a-long-query-when-the-client-disconnects)

### Advanced Questions (301-450)

- [301: What happens inside Nest when you call `NestFactory.create()`?](#301-what-happens-inside-nest-when-you-call-nestfactorycreate)
- [302: How does Nest use `reflect-metadata`?](#302-how-does-nest-use-reflect-metadata)
- [303: Why can `import type` break dependency injection?](#303-why-can-import-type-break-dependency-injection)
- [304: Why does a circular file import (not a DI cycle) produce `undefined` dependencies?](#304-why-does-a-circular-file-import-not-a-di-cycle-produce-undefined-dependencies)
- [305: How does Nest decide the instance identity of a dynamic module?](#305-how-does-nest-decide-the-instance-identity-of-a-dynamic-module)
- [306: What are durable providers?](#306-what-are-durable-providers)
- [307: How do you write a `ContextIdStrategy` for multi-tenancy?](#307-how-do-you-write-a-contextidstrategy-for-multi-tenancy)
- [308: What are the main ways to build multi-tenant apps in Nest?](#308-what-are-the-main-ways-to-build-multi-tenant-apps-in-nest)
- [309: How does `AsyncLocalStorage` compare to request-scoped providers?](#309-how-does-asynclocalstorage-compare-to-request-scoped-providers)
- [310: What is the `DiscoveryService` and how do you build a custom decorator with it?](#310-what-is-the-discoveryservice-and-how-do-you-build-a-custom-decorator-with-it)
- [311: Why should explorers skip non-static wrappers?](#311-why-should-explorers-skip-non-static-wrappers)
- [312: How do you lazy load a module?](#312-how-do-you-lazy-load-a-module)
- [313: How do you reduce cold start time for Nest on serverless?](#313-how-do-you-reduce-cold-start-time-for-nest-on-serverless)
- [314: How do you run Nest on AWS Lambda?](#314-how-do-you-run-nest-on-aws-lambda)
- [315: How do you write a custom transport strategy?](#315-how-do-you-write-a-custom-transport-strategy)
- [316: How does gRPC work in Nest?](#316-how-does-grpc-work-in-nest)
- [317: How do you handle streaming in gRPC with Nest?](#317-how-do-you-handle-streaming-in-grpc-with-nest)
- [318: How do you return proper gRPC status codes for errors?](#318-how-do-you-return-proper-grpc-status-codes-for-errors)
- [319: What should you know about Kafka in Nest?](#319-what-should-you-know-about-kafka-in-nest)
- [320: How do you commit Kafka offsets manually?](#320-how-do-you-commit-kafka-offsets-manually)
- [321: How do you make RabbitMQ consumers reliable?](#321-how-do-you-make-rabbitmq-consumers-reliable)
- [322: What is the outbox pattern and how would you do it in Nest?](#322-what-is-the-outbox-pattern-and-how-would-you-do-it-in-nest)
- [323: How do you make a consumer idempotent?](#323-how-do-you-make-a-consumer-idempotent)
- [324: How would you implement an idempotency key interceptor for POST requests?](#324-how-would-you-implement-an-idempotency-key-interceptor-for-post-requests)
- [325: How do microservice exception filters differ from HTTP ones?](#325-how-do-microservice-exception-filters-differ-from-http-ones)
- [326: How do you scale WebSocket gateways across several instances?](#326-how-do-you-scale-websocket-gateways-across-several-instances)
- [327: What changed for request-scoped WebSocket gateways in Nest 12?](#327-what-changed-for-request-scoped-websocket-gateways-in-nest-12)
- [328: How do you do GraphQL subscriptions in Nest 12?](#328-how-do-you-do-graphql-subscriptions-in-nest-12)
- [329: How do you protect a GraphQL API from expensive queries?](#329-how-do-you-protect-a-graphql-api-from-expensive-queries)
- [330: What is GraphQL federation and how does Nest support it?](#330-what-is-graphql-federation-and-how-does-nest-support-it)
- [331: How do you build a request-scoped DataLoader without making everything request-scoped?](#331-how-do-you-build-a-request-scoped-dataloader-without-making-everything-request-scoped)
- [332: What are the practical steps to move a Nest app to ESM?](#332-what-are-the-practical-steps-to-move-a-nest-app-to-esm)
- [333: How can a CommonJS app use ESM-only Nest 12 packages?](#333-how-can-a-commonjs-app-use-esm-only-nest-12-packages)
- [334: What are the risks with ESM and decorators metadata order?](#334-what-are-the-risks-with-esm-and-decorators-metadata-order)
- [335: Why might the Swagger CLI plugin not work with TypeScript 7?](#335-why-might-the-swagger-cli-plugin-not-work-with-typescript-7)
- [336: How do you build a reusable Nest library for other teams?](#336-how-do-you-build-a-reusable-nest-library-for-other-teams)
- [337: Why must `@nestjs/*` be peer dependencies in libraries?](#337-why-must-nestjs-be-peer-dependencies-in-libraries)
- [338: How do you use `setExtras` in `ConfigurableModuleBuilder`?](#338-how-do-you-use-setextras-in-configurablemodulebuilder)
- [339: How do you extend the generated `register` method with extra providers?](#339-how-do-you-extend-the-generated-register-method-with-extra-providers)
- [340: What does the `strict` option do in `app.get()` and `moduleRef.get()`?](#340-what-does-the-strict-option-do-in-appget-and-modulerefget)
- [341: What does `app.select()` do?](#341-what-does-appselect-do)
- [342: What is Nest Devtools and what does `snapshot: true` do?](#342-what-is-nest-devtools-and-what-does-snapshot-true-do)
- [343: What is `preview` mode?](#343-what-is-preview-mode)
- [344: How do you debug "Nest can't resolve dependencies" errors fast?](#344-how-do-you-debug-nest-cant-resolve-dependencies-errors-fast)
- [345: What changed with `@Optional()` and inheritance in Nest 12?](#345-what-changed-with-optional-and-inheritance-in-nest-12)
- [346: What changed about lifecycle hook order in Nest 12?](#346-what-changed-about-lifecycle-hook-order-in-nest-12)
- [347: How does inheritance work with Nest decorators?](#347-how-does-inheritance-work-with-nest-decorators)
- [348: How do you build a generic CRUD controller with inheritance?](#348-how-do-you-build-a-generic-crud-controller-with-inheritance)
- [349: How do you write a mixin interceptor that takes options and still uses DI?](#349-how-do-you-write-a-mixin-interceptor-that-takes-options-and-still-uses-di)
- [350: Why does passing an instance vs a class to `@UseGuards()` matter?](#350-why-does-passing-an-instance-vs-a-class-to-useguards-matter)
- [351: How does Nest create pipes, guards and interceptors that are passed as classes?](#351-how-does-nest-create-pipes-guards-and-interceptors-that-are-passed-as-classes)
- [352: How would you implement soft multi-version deprecation in an API?](#352-how-would-you-implement-soft-multi-version-deprecation-in-an-api)
- [353: How do you implement field-level authorization (for example with CASL)?](#353-how-do-you-implement-field-level-authorization-for-example-with-casl)
- [354: What security issues should a Nest API watch for beyond auth?](#354-what-security-issues-should-a-nest-api-watch-for-beyond-auth)
- [355: How would you stop users from reading other users' data in a REST API?](#355-how-would-you-stop-users-from-reading-other-users-data-in-a-rest-api)
- [356: How do you store secrets safely in a Nest app?](#356-how-do-you-store-secrets-safely-in-a-nest-app)
- [357: How do you load secrets from a secret manager before modules start?](#357-how-do-you-load-secrets-from-a-secret-manager-before-modules-start)
- [358: How do you handle very large file uploads without loading them into memory?](#358-how-do-you-handle-very-large-file-uploads-without-loading-them-into-memory)
- [359: How do you stream a large response, like a CSV export, without high memory use?](#359-how-do-you-stream-a-large-response-like-a-csv-export-without-high-memory-use)
- [360: How do you find and fix a memory leak in a Nest app?](#360-how-do-you-find-and-fix-a-memory-leak-in-a-nest-app)
- [361: How do you use all CPU cores with Nest?](#361-how-do-you-use-all-cpu-cores-with-nest)
- [362: When would you use worker threads in a Nest app?](#362-when-would-you-use-worker-threads-in-a-nest-app)
- [363: How do you measure event loop blocking?](#363-how-do-you-measure-event-loop-blocking)
- [364: How do you add OpenTelemetry tracing to a Nest app?](#364-how-do-you-add-opentelemetry-tracing-to-a-nest-app)
- [365: How do you expose Prometheus metrics?](#365-how-do-you-expose-prometheus-metrics)
- [366: How do you set up liveness and readiness probes properly?](#366-how-do-you-set-up-liveness-and-readiness-probes-properly)
- [367: Why might requests fail during deploys even with graceful shutdown?](#367-why-might-requests-fail-during-deploys-even-with-graceful-shutdown)
- [368: How do you share a database transaction across several services without passing the manager everywhere?](#368-how-do-you-share-a-database-transaction-across-several-services-without-passing-the-manager-everywhere)
- [369: What problems come with distributed transactions across microservices?](#369-what-problems-come-with-distributed-transactions-across-microservices)
- [370: How do you implement event sourcing with `@nestjs/cqrs`?](#370-how-do-you-implement-event-sourcing-with-nestjscqrs)
- [371: How do you test code that uses `ConfigService` without `.env` files?](#371-how-do-you-test-code-that-uses-configservice-without-env-files)
- [372: How do you write integration tests with Testcontainers?](#372-how-do-you-write-integration-tests-with-testcontainers)
- [373: How do you test an interceptor that uses RxJS?](#373-how-do-you-test-an-interceptor-that-uses-rxjs)
- [374: How do you test a microservice handler end to end?](#374-how-do-you-test-a-microservice-handler-end-to-end)
- [375: How do you mock an ES module dependency in Vitest?](#375-how-do-you-mock-an-es-module-dependency-in-vitest)
- [376: Why can `useDefineForClassFields` break Nest code?](#376-why-can-usedefineforclassfields-break-nest-code)
- [377: What is property-based injection and when is it used?](#377-what-is-property-based-injection-and-when-is-it-used)
- [378: What is `IntrinsicException`?](#378-what-is-intrinsicexception)
- [379: How do you catch errors that happen outside the request cycle?](#379-how-do-you-catch-errors-that-happen-outside-the-request-cycle)
- [380: Why is a fire-and-forget promise inside a handler dangerous?](#380-why-is-a-fire-and-forget-promise-inside-a-handler-dangerous)
- [381: How do you use the stricter pipe types in Nest 12?](#381-how-do-you-use-the-stricter-pipe-types-in-nest-12)
- [382: How would you write your own pipe that validates a Standard Schema?](#382-how-would-you-write-your-own-pipe-that-validates-a-standard-schema)
- [383: How do you read the `schema` attached to a parameter inside your own pipe in Nest 12?](#383-how-do-you-read-the-schema-attached-to-a-parameter-inside-your-own-pipe-in-nest-12)
- [384: What is the cost of `class-validator` + `class-transformer` per request?](#384-what-is-the-cost-of-class-validator--class-transformer-per-request)
- [385: How can Fastify make JSON responses faster?](#385-how-can-fastify-make-json-responses-faster)
- [386: How do you tune a Nest app for high throughput?](#386-how-do-you-tune-a-nest-app-for-high-throughput)
- [387: How do you prevent cache stampede?](#387-how-do-you-prevent-cache-stampede)
- [388: How do you invalidate cache entries reliably?](#388-how-do-you-invalidate-cache-entries-reliably)
- [389: How do you use ETags or conditional requests in Nest?](#389-how-do-you-use-etags-or-conditional-requests-in-nest)
- [390: How do you implement optimistic locking with TypeORM?](#390-how-do-you-implement-optimistic-locking-with-typeorm)
- [391: How do you implement cursor pagination?](#391-how-do-you-implement-cursor-pagination)
- [392: How do you add soft delete globally?](#392-how-do-you-add-soft-delete-globally)
- [393: How do you add audit logs for every change?](#393-how-do-you-add-audit-logs-for-every-change)
- [394: How do you use read replicas with TypeORM in Nest?](#394-how-do-you-use-read-replicas-with-typeorm-in-nest)
- [395: How do you choose the database pool size for a Nest app?](#395-how-do-you-choose-the-database-pool-size-for-a-nest-app)
- [396: How do you set query timeouts to protect the app?](#396-how-do-you-set-query-timeouts-to-protect-the-app)
- [397: How do you call another HTTP service with retries and a circuit breaker?](#397-how-do-you-call-another-http-service-with-retries-and-a-circuit-breaker)
- [398: How do you set a timeout on `ClientProxy.send()`?](#398-how-do-you-set-a-timeout-on-clientproxysend)
- [399: How would you build an API gateway or BFF with Nest?](#399-how-would-you-build-an-api-gateway-or-bff-with-nest)
- [400: How do you migrate an existing Express app to Nest step by step?](#400-how-do-you-migrate-an-existing-express-app-to-nest-step-by-step)
- [401: How would you organize a large Nest codebase?](#401-how-would-you-organize-a-large-nest-codebase)
- [402: How do you apply hexagonal (ports and adapters) architecture in Nest?](#402-how-do-you-apply-hexagonal-ports-and-adapters-architecture-in-nest)
- [403: What is a sign that a Nest module has become a "god module"?](#403-what-is-a-sign-that-a-nest-module-has-become-a-god-module)
- [404: How do you decouple features with domain events?](#404-how-do-you-decouple-features-with-domain-events)
- [405: How do you design a plugin system for a Nest app?](#405-how-do-you-design-a-plugin-system-for-a-nest-app)
- [406: Can you add providers to the DI container after the app has started?](#406-can-you-add-providers-to-the-di-container-after-the-app-has-started)
- [407: How do you create a custom handler type that still runs guards and interceptors?](#407-how-do-you-create-a-custom-handler-type-that-still-runs-guards-and-interceptors)
- [408: What is the Nest REPL?](#408-what-is-the-nest-repl)
- [409: How do you build a command line tool with Nest?](#409-how-do-you-build-a-command-line-tool-with-nest)
- [410: How do you run BullMQ processors with concurrency and rate limits?](#410-how-do-you-run-bullmq-processors-with-concurrency-and-rate-limits)
- [411: How do you handle retries and failed jobs in BullMQ?](#411-how-do-you-handle-retries-and-failed-jobs-in-bullmq)
- [412: Why should CPU-heavy BullMQ jobs use sandboxed processors?](#412-why-should-cpu-heavy-bullmq-jobs-use-sandboxed-processors)
- [413: How do you run the queue workers separately from the API?](#413-how-do-you-run-the-queue-workers-separately-from-the-api)
- [414: What is a BullMQ flow and when would you use it?](#414-what-is-a-bullmq-flow-and-when-would-you-use-it)
- [415: How do you implement feature flags in Nest?](#415-how-do-you-implement-feature-flags-in-nest)
- [416: Can you change configuration without restarting the app?](#416-can-you-change-configuration-without-restarting-the-app)
- [417: How do you add internationalized error messages?](#417-how-do-you-add-internationalized-error-messages)
- [418: How would you make `errorCode` from Nest 12 consistent across the whole API?](#418-how-would-you-make-errorcode-from-nest-12-consistent-across-the-whole-api)
- [419: How should you upgrade a large app from Nest 11 to 12?](#419-how-should-you-upgrade-a-large-app-from-nest-11-to-12)
- [420: What were the main Express 5 pitfalls when moving to Nest 11 or later?](#420-what-were-the-main-express-5-pitfalls-when-moving-to-nest-11-or-later)
- [421: What does "stricter `isHttpError`" in Nest 12 mean for custom errors?](#421-what-does-stricter-ishttperror-in-nest-12-mean-for-custom-errors)
- [422: How do you prevent memory growth in throttler or caches keyed by user input?](#422-how-do-you-prevent-memory-growth-in-throttler-or-caches-keyed-by-user-input)
- [423: How do you rate limit WebSocket messages?](#423-how-do-you-rate-limit-websocket-messages)
- [424: How do you deal with backpressure in WebSockets or SSE?](#424-how-do-you-deal-with-backpressure-in-websockets-or-sse)
- [425: How do you scale SSE endpoints?](#425-how-do-you-scale-sse-endpoints)
- [426: How do you build a typed event system on top of `@nestjs/event-emitter`?](#426-how-do-you-build-a-typed-event-system-on-top-of-nestjsevent-emitter)
- [427: How do you make sure `@OnEvent` handlers are registered before events fire at startup?](#427-how-do-you-make-sure-onevent-handlers-are-registered-before-events-fire-at-startup)
- [428: What is the difference between `nest build` with `tsc`, `swc` and `rspack`?](#428-what-is-the-difference-between-nest-build-with-tsc-swc-and-rspack)
- [429: How do you build all apps of a Nest monorepo quickly?](#429-how-do-you-build-all-apps-of-a-nest-monorepo-quickly)
- [430: When would you choose Nx over the Nest CLI monorepo?](#430-when-would-you-choose-nx-over-the-nest-cli-monorepo)
- [431: How do you share DTOs between a Nest backend and a frontend?](#431-how-do-you-share-dtos-between-a-nest-backend-and-a-frontend)
- [432: How do you create an OpenAPI spec in CI without starting the server?](#432-how-do-you-create-an-openapi-spec-in-ci-without-starting-the-server)
- [433: How do you do contract testing between Nest services?](#433-how-do-you-do-contract-testing-between-nest-services)
- [434: What does a good testing strategy for a Nest app look like?](#434-what-does-a-good-testing-strategy-for-a-nest-app-look-like)
- [435: How do you test that a guard is applied to all routes that need it?](#435-how-do-you-test-that-a-guard-is-applied-to-all-routes-that-need-it)
- [436: How do you keep e2e tests fast?](#436-how-do-you-keep-e2e-tests-fast)
- [437: How do you test an exception filter?](#437-how-do-you-test-an-exception-filter)
- [438: How would you implement your own `@Transactional()` decorator?](#438-how-would-you-implement-your-own-transactional-decorator)
- [439: Why can a method decorator that wraps a function break Nest route decorators?](#439-why-can-a-method-decorator-that-wraps-a-function-break-nest-route-decorators)
- [440: How does the Nest router handle the same path for different versions and hosts?](#440-how-does-the-nest-router-handle-the-same-path-for-different-versions-and-hosts)
- [441: How do you use `routeConflictPolicy` in CI?](#441-how-do-you-use-routeconflictpolicy-in-ci)
- [442: What is `nest deploy`?](#442-what-is-nest-deploy)
- [443: How do you write a production Dockerfile for a Nest app?](#443-how-do-you-write-a-production-dockerfile-for-a-nest-app)
- [444: How do you handle schema migrations safely with zero downtime?](#444-how-do-you-handle-schema-migrations-safely-with-zero-downtime)
- [445: How do you run Nest with Bun or Deno?](#445-how-do-you-run-nest-with-bun-or-deno)
- [446: How do you avoid loading every module in a big app when you only need a few, for example in a worker?](#446-how-do-you-avoid-loading-every-module-in-a-big-app-when-you-only-need-a-few-for-example-in-a-worker)
- [447: How do you implement API keys for machine-to-machine access alongside JWT for users?](#447-how-do-you-implement-api-keys-for-machine-to-machine-access-alongside-jwt-for-users)
- [448: How would you implement single-session or token revocation with JWTs?](#448-how-would-you-implement-single-session-or-token-revocation-with-jwts)
- [449: What would you check when a Nest app is slow only under load?](#449-what-would-you-check-when-a-nest-app-is-slow-only-under-load)
- [450: What are the things you would say make a Nest codebase healthy in the long run?](#450-what-are-the-things-you-would-say-make-a-nest-codebase-healthy-in-the-long-run)

---

## Easy Questions (1-150)

### 1: What is NestJS?

NestJS is a framework for building server-side applications with Node.js. It is written in TypeScript and uses a structure based on modules, controllers and providers. Under the hood it runs on an HTTP server library, Express by default, with Fastify as an option. Besides REST APIs, you can use it for GraphQL, WebSockets, microservices and command line apps.

### 2: Why would you pick NestJS over plain Express?

Express gives you routing and middleware and nothing else, so every team ends up inventing its own folder layout, way to share services and way to handle errors. Nest gives you that structure out of the box: dependency injection, modules, validation pipes, guards, exception filters, a testing module and a CLI. That makes large codebases more consistent and easier to test. You can still use any Express middleware inside Nest.

### 3: What is the current major version of NestJS and what are the headline changes?

NestJS 12 was released in August 2026. The main changes are:

- All official packages ship as ES modules. CommonJS apps keep working because Node.js supports `require()` of ES modules.
- Route parameter decorators like `@Body()` accept a `schema` option that works with any Standard Schema library (Zod, Valibot, ArkType).
- New projects can use Vitest and oxlint, and Rspack replaces webpack as the bundler option.
- Structured logging, error codes on HTTP exceptions, and graceful shutdown for the Express adapter.

Version 11 (January 2025) moved to Express 5 and Fastify 5, so those changes also still matter.

### 4: Which Node.js version do you need for NestJS 12?

To run a Nest 12 app you need Node.js 20.19 or newer, or 22.12 or newer on the 22 line. Node 21 is not supported. The CLI commands such as `nest new` and `nest generate` need a newer Node version (22.22.3+, 24.15+ or 26+).

### 5: How do you install the Nest CLI and create a new project?

```bash
npm i -g @nestjs/cli
nest new my-app
```

The CLI asks which package manager you want (npm, yarn, pnpm or bun) and, since version 12, whether the project should be CommonJS or ESM. It then creates the files and installs the packages.

### 6: What files does a new Nest project contain?

The `src` folder has:

- `main.ts` - the entry point that creates and starts the app.
- `app.module.ts` - the root module.
- `app.controller.ts` - a sample controller with one route.
- `app.service.ts` - a sample service.
- `app.controller.spec.ts` - a unit test for the controller.

There is also a `test` folder for end-to-end tests, `nest-cli.json` for CLI settings, and the usual `package.json` and `tsconfig.json`.

### 7: What does `main.ts` usually look like?

```ts
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

`NestFactory.create()` builds the app from the root module, and `listen()` starts the HTTP server.

### 8: What is `NestFactory`?

`NestFactory` is a class from `@nestjs/core` with static methods that create application instances. `create()` makes an HTTP app, `createMicroservice()` makes a microservice, and `createApplicationContext()` makes an app without any network listener (useful for scripts and cron jobs).

### 9: What is a module in NestJS?

A module is a class marked with `@Module()`. It groups related controllers and providers together. Every app has at least one module, the root module, and Nest builds its dependency graph starting from it.

```ts
import { Module } from "@nestjs/common";
import { CatsController } from "./cats.controller";
import { CatsService } from "./cats.service";

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

### 10: What properties does the `@Module()` decorator accept?

- `imports` - other modules whose exported providers this module needs.
- `controllers` - controllers that belong to this module.
- `providers` - providers that Nest will create and that can be injected inside this module.
- `exports` - providers (or modules) that this module makes available to modules that import it.

### 11: What is a controller?

A controller handles incoming requests and returns responses. You mark a class with `@Controller()` and its methods with HTTP method decorators. The controller should stay thin: it reads the input and calls a service that does the real work.

```ts
import { Controller, Get } from "@nestjs/common";

@Controller("cats")
export class CatsController {
  @Get()
  findAll() {
    return "This returns all cats";
  }
}
```

### 12: What is a provider?

A provider is anything Nest can inject: a service, repository, factory, helper or even a plain value. Most providers are classes marked with `@Injectable()`. You register them in a module's `providers` array, and Nest creates them and passes them to the classes that need them.

### 13: What is a service in NestJS?

A service is a provider that holds business logic, like reading from the database or calling another API. It is a normal class with `@Injectable()`. There is nothing special about the word "service"; it is just a naming convention for this kind of provider.

```ts
import { Injectable } from "@nestjs/common";

@Injectable()
export class CatsService {
  private readonly cats: string[] = [];

  create(name: string) {
    this.cats.push(name);
  }

  findAll() {
    return this.cats;
  }
}
```

### 14: What does `@Injectable()` do?

It marks a class so Nest can manage it with its dependency injection container. Together with TypeScript's `emitDecoratorMetadata` setting, it lets Nest read the constructor parameter types and inject the right instances.

### 15: What is dependency injection?

Dependency injection means a class does not create its own dependencies. It declares them, usually in the constructor, and something else (the Nest container) provides them. This keeps classes loosely coupled and makes testing easy because you can pass in fakes.

```ts
@Controller("cats")
export class CatsController {
  constructor(private readonly catsService: CatsService) {}
}
```

### 16: How does Nest know what to inject in a constructor?

TypeScript emits the constructor parameter types as metadata when `emitDecoratorMetadata` is on. Nest reads that metadata, finds the matching provider by class (the class is the token), and passes the instance in. If the type is an interface or a string, there is no runtime class, so you have to use `@Inject('TOKEN')` instead.

### 17: What is the default scope of a provider?

Singleton. Nest creates one instance when the app starts and shares it everywhere it is injected. This is the fastest option and is right for most services.

### 18: What are the HTTP method decorators in Nest?

`@Get()`, `@Post()`, `@Put()`, `@Patch()`, `@Delete()`, `@Options()`, `@Head()` and `@All()`. Each one takes an optional path.

```ts
@Controller("users")
export class UsersController {
  @Get(":id")
  findOne() {}

  @Post()
  create() {}

  @Delete(":id")
  remove() {}
}
```

### 19: How do you read a route parameter?

Use `@Param()`. You can get one parameter by name or all of them as an object.

```ts
@Get(':id')
findOne(@Param('id') id: string) {
  return `Cat #${id}`;
}
```

Route params are always strings unless you convert them with a pipe like `ParseIntPipe`.

### 20: How do you read query string values?

Use `@Query()`.

```ts
@Get()
findAll(@Query('page') page: string, @Query('limit') limit: string) {
  return { page, limit };
}
```

For `GET /cats?page=2&limit=10` this returns `{ page: '2', limit: '10' }`.

### 21: How do you read the request body?

Use `@Body()`, usually typed with a DTO class.

```ts
@Post()
create(@Body() createCatDto: CreateCatDto) {
  return this.catsService.create(createCatDto);
}
```

### 22: What is a DTO?

DTO stands for Data Transfer Object. It describes the shape of the data that comes into or goes out of your API. In Nest it is common to write DTOs as classes (not interfaces) because classes exist at runtime, so the validation pipe can read decorators on them.

```ts
import { IsInt, IsString } from "class-validator";

export class CreateCatDto {
  @IsString()
  name: string;

  @IsInt()
  age: number;
}
```

### 23: Why should DTOs be classes and not interfaces?

TypeScript interfaces are removed when the code is compiled, so nothing about them exists at runtime. Pipes like `ValidationPipe` need runtime information to validate and transform data. A class stays in the compiled JavaScript and keeps its decorators, so validation works.

### 24: How do you get the full request object?

Inject it with `@Req()`. The type depends on the platform, for example `Request` from `express`.

```ts
import { Request } from 'express';

@Get()
findAll(@Req() req: Request) {
  return req.headers['user-agent'];
}
```

Most of the time it is better to use the specific decorators like `@Body()`, `@Query()` and `@Headers()`.

### 25: How do you read request headers?

```ts
@Get()
findAll(@Headers('authorization') auth: string) {
  return auth;
}
```

Calling `@Headers()` without a name gives you all headers as an object.

### 26: How do you change the response status code?

Use `@HttpCode()`. By default `POST` returns 201 and everything else returns 200.

```ts
@Post('login')
@HttpCode(200)
login() {
  return { ok: true };
}
```

You can also use the `HttpStatus` enum: `@HttpCode(HttpStatus.NO_CONTENT)`.

### 27: How do you set a custom response header?

Use `@Header()`.

```ts
@Get()
@Header('Cache-Control', 'no-store')
findAll() {
  return [];
}
```

### 28: How do you redirect from a route?

Use `@Redirect()`. You can also return an object with `url` and `statusCode` to change the target at runtime.

```ts
@Get('docs')
@Redirect('https://docs.nestjs.com', 302)
getDocs(@Query('version') version?: string) {
  if (version === '5') {
    return { url: 'https://docs.nestjs.com/v5/' };
  }
}
```

### 29: Can a controller method be `async`?

Yes. Nest waits for the promise and sends the resolved value as the response.

```ts
@Get()
async findAll(): Promise<Cat[]> {
  return this.catsService.findAll();
}
```

You can also return an RxJS Observable. Nest subscribes to it and sends the last emitted value.

### 30: What happens when a controller method returns an object?

Nest serializes it to JSON automatically and sets the `Content-Type` header to `application/json`. If it returns a string or number, Nest sends it as is.

### 31: What does `@Res()` do and why is it not recommended?

`@Res()` gives you the raw response object from Express or Fastify. Once you use it, Nest stops handling the response for that route, so you must call `res.send()` or `res.json()` yourself. You also lose features like interceptors and `@HttpCode()`. If you only need to set a cookie or header, use `@Res({ passthrough: true })` and still return the value normally.

```ts
@Get()
findAll(@Res({ passthrough: true }) res: Response) {
  res.cookie('seen', '1');
  return [];
}
```

### 32: How do you register a controller?

Add it to the `controllers` array of a module. If the controller is not in any module that is part of the app graph, its routes will not exist.

### 33: How do you generate files with the CLI?

```bash
nest generate module cats
nest generate controller cats
nest generate service cats
# short form
nest g mo cats
nest g co cats
nest g s cats
```

The CLI creates the file, a test file, and adds the class to the closest module.

### 34: What does `nest g resource` do?

It generates a full CRUD feature: a module, controller, service, DTOs, an entity file and tests. It asks which transport you want (REST, GraphQL, microservice or WebSockets) and whether to generate the CRUD entry points.

```bash
nest g resource users
```

### 35: How do you run a Nest app in watch mode?

```bash
npm run start:dev
# which runs
nest start --watch
```

The app restarts each time you save a file.

### 36: What does `nest build` do?

It compiles the TypeScript project into JavaScript, by default into the `dist` folder. You can choose the builder with `--builder` (`tsc`, `swc` or `rspack`). For production you then run `node dist/main`.

### 37: What is `nest-cli.json` used for?

It holds CLI settings: where the source code is (`sourceRoot`), the compiler options (builder, type checking, plugins), assets to copy on build, and in a monorepo the list of apps and libraries.

```json
{
  "$schema": "https://json.schemastore.org/nest-cli",
  "collection": "@nestjs/schematics",
  "sourceRoot": "src",
  "compilerOptions": {
    "deleteOutDir": true
  }
}
```

### 38: What does the `exports` array in a module do?

It makes providers available to other modules that import this module. Providers that are not exported stay private to their module.

```ts
@Module({
  providers: [CatsService],
  exports: [CatsService],
})
export class CatsModule {}
```

### 39: How do you use a service from another module?

Export the service from its module, then import that module where you need it.

```ts
@Module({
  imports: [CatsModule],
  controllers: [OwnersController],
})
export class OwnersModule {}
```

Now `OwnersController` can inject `CatsService`.

### 40: What is a shared module?

In Nest every module is shared by default. Once a module exports a provider, any module that imports it gets the same instance (because providers are singletons). So a "shared module" is simply a module that exports some providers for others to use.

### 41: What is a global module?

A module marked with `@Global()`. Its exported providers can be injected anywhere without importing the module. It should be imported once, usually in the root module. Use it sparingly, for things like config or database connections, because it hides where dependencies come from.

```ts
@Global()
@Module({
  providers: [ConfigService],
  exports: [ConfigService],
})
export class ConfigModule {}
```

### 42: What is a feature module?

A module that groups code for one part of the business, like `UsersModule`, `OrdersModule` or `PaymentsModule`. Splitting the app this way keeps related code together and makes the boundaries clear.

### 43: Can a module re-export a module it imports?

Yes. Put the module in both `imports` and `exports`.

```ts
@Module({
  imports: [CommonModule],
  exports: [CommonModule],
})
export class CoreModule {}
```

Anything that imports `CoreModule` now also gets what `CommonModule` exports.

### 44: What are pipes?

Pipes run before the route handler and work on its arguments. They do two jobs: transformation (for example turning `"5"` into `5`) and validation (throwing an error if the input is wrong).

### 45: Which built-in pipes does Nest provide?

`ValidationPipe`, `StandardSchemaValidationPipe`, `ParseIntPipe`, `ParseFloatPipe`, `ParseBoolPipe`, `ParseArrayPipe`, `ParseUUIDPipe`, `ParseEnumPipe`, `ParseDatePipe`, `DefaultValuePipe` and `ParseFilePipe`. They all come from `@nestjs/common`.

### 46: How do you use `ParseIntPipe`?

```ts
@Get(':id')
findOne(@Param('id', ParseIntPipe) id: number) {
  return this.catsService.findOne(id);
}
```

If the value is not a number, Nest responds with `400 Bad Request` and the handler is not called.

### 47: How do you give a query parameter a default value?

Use `DefaultValuePipe` before the parse pipe.

```ts
@Get()
findAll(
  @Query('page', new DefaultValuePipe(1), ParseIntPipe) page: number,
) {
  return this.catsService.findAll(page);
}
```

### 48: What is `ParseDatePipe`?

It was added in Nest 11. It turns a string (or number) into a `Date` object and throws a 400 error if the value is not a valid date.

```ts
@Get()
findByDate(@Query('from', ParseDatePipe) from: Date) {
  return this.eventsService.findFrom(from);
}
```

### 49: How do you validate the request body with `class-validator`?

Install the packages, add decorators to the DTO and enable `ValidationPipe`.

```bash
npm i class-validator class-transformer
```

```ts
// main.ts
app.useGlobalPipes(new ValidationPipe());
```

```ts
export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  password: string;
}
```

If validation fails, Nest returns 400 with a list of error messages.

### 50: What does `whitelist: true` do in `ValidationPipe`?

It strips any property from the body that does not have a validation decorator in the DTO. This stops clients from sending extra fields like `isAdmin: true`.

```ts
app.useGlobalPipes(new ValidationPipe({ whitelist: true }));
```

Add `forbidNonWhitelisted: true` if you want to reject the request instead of silently removing the fields.

### 51: What does `transform: true` do in `ValidationPipe`?

It turns the plain JSON object into an instance of your DTO class and converts primitive values to the declared types where it can (for example a route param `"5"` into the number `5` when the parameter is typed as `number`).

```ts
app.useGlobalPipes(new ValidationPipe({ transform: true }));
```

### 52: What is Standard Schema validation in NestJS 12?

Nest 12 lets you validate parameters with any library that follows the Standard Schema spec, such as Zod, Valibot or ArkType. You pass the schema in the decorator and register `StandardSchemaValidationPipe`.

```ts
import { z } from 'zod';

export const createUserSchema = z.object({
  email: z.email(),
  password: z.string().min(8),
});
export type CreateUserDto = z.infer<typeof createUserSchema>;

@Post()
create(@Body({ schema: createUserSchema }) dto: CreateUserDto) {
  return this.usersService.create(dto);
}
```

```ts
// main.ts
app.useGlobalPipes(new StandardSchemaValidationPipe());
```

The old `class-validator` approach still works.

### 53: What are guards?

Guards decide if a request is allowed to reach the route handler. They implement `CanActivate` and return `true` or `false` (or a promise or observable of it). They are mostly used for authentication and authorization.

```ts
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    return Boolean(request.headers.authorization);
  }
}
```

### 54: How do you apply a guard?

With `@UseGuards()` on a controller or a method, or globally.

```ts
@Controller("cats")
@UseGuards(AuthGuard)
export class CatsController {}
```

```ts
app.useGlobalGuards(new AuthGuard());
```

### 55: What happens when a guard returns `false`?

Nest throws a `ForbiddenException`, so the client gets `403 Forbidden`. If you want a different response, like 401, throw that exception yourself inside the guard.

### 56: What are interceptors?

Interceptors wrap the route handler. They can run code before and after it, change the result, change thrown errors, add caching or timing, or skip the handler entirely. They implement `NestInterceptor` and use RxJS.

```ts
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const start = Date.now();
    return next
      .handle()
      .pipe(tap(() => console.log(`Took ${Date.now() - start}ms`)));
  }
}
```

### 57: How do you apply an interceptor?

```ts
@UseInterceptors(LoggingInterceptor)
@Controller("cats")
export class CatsController {}
```

Or globally with `app.useGlobalInterceptors(new LoggingInterceptor())`.

### 58: What is middleware in NestJS?

Middleware is a function that runs before the route handler, same as Express middleware. It gets `req`, `res` and `next`. In Nest you can write it as a class that implements `NestMiddleware` or as a plain function.

```ts
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log(`${req.method} ${req.originalUrl}`);
    next();
  }
}
```

### 59: How do you register middleware?

Middleware is not listed in `@Module()`. You set it up in the module class with the `configure()` method.

```ts
@Module({ controllers: [CatsController] })
export class CatsModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes("cats");
  }
}
```

### 60: How do you add middleware for all routes?

Either with `app.use()` in `main.ts` (function middleware only) or with `forRoutes('*splat')` in a module. Since Nest 11 uses Express 5, wildcards need a name.

```ts
consumer.apply(LoggerMiddleware).forRoutes("{*splat}");
```

Wrapping it in braces (`{*splat}`) also matches the root path.

### 61: What is functional middleware?

Middleware written as a plain function instead of a class. Use it when the middleware does not need any injected dependencies.

```ts
export function logger(req: Request, res: Response, next: NextFunction) {
  console.log("Request...");
  next();
}

consumer.apply(logger).forRoutes(CatsController);
```

### 62: What are exception filters?

Exception filters catch errors thrown during a request and decide what response to send. Nest has a built-in global filter that turns `HttpException` into the right JSON response and anything else into `500 Internal Server Error`. You can write your own to change the response format or log errors.

### 63: What does the default error response look like?

```json
{
  "statusCode": 404,
  "message": "Cat not found",
  "error": "Not Found"
}
```

For unknown errors (not an `HttpException`) the client gets `{"statusCode":500,"message":"Internal server error"}`.

### 64: How do you throw an HTTP error?

Throw one of the built-in exceptions.

```ts
@Get(':id')
async findOne(@Param('id', ParseIntPipe) id: number) {
  const cat = await this.catsService.findOne(id);
  if (!cat) {
    throw new NotFoundException('Cat not found');
  }
  return cat;
}
```

### 65: Name some built-in HTTP exceptions.

`BadRequestException`, `UnauthorizedException`, `ForbiddenException`, `NotFoundException`, `ConflictException`, `GoneException`, `PayloadTooLargeException`, `UnsupportedMediaTypeException`, `UnprocessableEntityException`, `InternalServerErrorException`, `NotImplementedException`, `BadGatewayException`, `ServiceUnavailableException`, `GatewayTimeoutException`, `RequestTimeoutException`, `MethodNotAllowedException`, `NotAcceptableException`, `PreconditionFailedException`, `ImATeapotException`.

### 66: How do you throw an `HttpException` with a custom body?

```ts
throw new HttpException(
  { status: HttpStatus.FORBIDDEN, error: "You cannot do this" },
  HttpStatus.FORBIDDEN,
);
```

The first argument becomes the response body when it is an object.

### 67: What is the `cause` option on exceptions?

The third argument (or second for built-in exceptions) accepts an options object. `cause` stores the original error for logging. It is not sent to the client.

```ts
try {
  await this.repo.save(user);
} catch (error) {
  throw new BadRequestException("Could not save user", { cause: error });
}
```

### 68: What is the `errorCode` option added in Nest 12?

It lets you attach a machine-readable code to an HTTP exception so clients can react to it without parsing the message.

```ts
throw new BadRequestException("Password is too weak", {
  errorCode: "WEAK_PASSWORD",
});
```

### 69: How do you enable CORS?

```ts
const app = await NestFactory.create(AppModule);
app.enableCors({
  origin: ["https://my-frontend.com"],
  credentials: true,
});
```

You can also pass `{ cors: true }` to `NestFactory.create()`.

### 70: How do you add a global prefix like `/api`?

```ts
app.setGlobalPrefix("api");
```

Now `GET /cats` becomes `GET /api/cats`. You can exclude routes, for example a health check:

```ts
app.setGlobalPrefix("api", { exclude: ["health"] });
```

### 71: How do you read environment variables in Nest?

Use `@nestjs/config`.

```bash
npm i @nestjs/config
```

```ts
@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true })],
})
export class AppModule {}
```

```ts
@Injectable()
export class DbService {
  constructor(private config: ConfigService) {}

  getUrl() {
    return this.config.get<string>("DATABASE_URL");
  }
}
```

By default it loads the `.env` file from the project root.

### 72: What is the difference between `ConfigService.get()` and `getOrThrow()`?

`get()` returns `undefined` (or a default value you pass) when the key is missing. `getOrThrow()` throws an error instead. Use `getOrThrow()` for required settings so the app fails early instead of running with a missing value.

```ts
const secret = this.config.getOrThrow<string>("JWT_SECRET");
```

### 73: How do you use the built-in logger?

```ts
import { Logger } from "@nestjs/common";

@Injectable()
export class CatsService {
  private readonly logger = new Logger(CatsService.name);

  findAll() {
    this.logger.log("Finding all cats");
    this.logger.warn("This is a warning");
    this.logger.error("Something failed");
  }
}
```

Passing the class name as the context makes it show up in each log line.

### 74: What log levels does the Nest logger have?

`log`, `error`, `warn`, `debug`, `verbose` and `fatal`. You can limit which levels are printed:

```ts
const app = await NestFactory.create(AppModule, {
  logger: ["error", "warn", "log"],
});
```

### 75: How do you print logs as JSON?

Since Nest 11 the built-in `ConsoleLogger` supports JSON output, which is handy in containers and log tools.

```ts
const app = await NestFactory.create(AppModule, {
  logger: new ConsoleLogger({ json: true }),
});
```

### 76: What is structured logging in Nest 12?

In Nest 12, if you pass a plain object after the message, the logger treats it as structured data instead of a context string. With JSON output those fields end up as separate keys, which log tools can search.

```ts
this.logger.log("User created", { userId: 1, email: "foo@bar.com" });
```

It is on by default. You can turn it off with `structuredParams: false` in the logger options.

### 77: How do you switch from Express to Fastify?

Install the adapter and pass it to `NestFactory.create()`.

```bash
npm i @nestjs/platform-fastify
```

```ts
import {
  FastifyAdapter,
  NestFastifyApplication,
} from "@nestjs/platform-fastify";

const app = await NestFactory.create<NestFastifyApplication>(
  AppModule,
  new FastifyAdapter(),
);
await app.listen(3000, "0.0.0.0");
```

Fastify listens on `localhost` only by default, so pass `'0.0.0.0'` when running in Docker.

### 78: Which Express and Fastify versions does Nest use now?

Since Nest 11, `@nestjs/platform-express` uses Express 5 and `@nestjs/platform-fastify` uses Fastify 5. Nest 12 keeps them.

### 79: What is a platform-agnostic framework?

It means your Nest code (controllers, services, guards and so on) does not depend directly on Express or Fastify. Nest talks to the server through an adapter, so you can switch the HTTP library with very few code changes. Only code that touches `@Req()`/`@Res()` or platform middleware needs to change.

### 80: What are the main building blocks of a Nest app?

Modules, controllers, providers, middleware, guards, interceptors, pipes and exception filters. Decorators tie them together.

### 81: In what order do middleware, guards, interceptors, pipes and filters run?

For an incoming request:

1. Middleware
2. Guards
3. Interceptors (the "before" part)
4. Pipes
5. Route handler
6. Interceptors (the "after" part)
7. Exception filters (only if something threw)

### 82: What is a decorator?

A decorator is a function you attach to a class, method, property or parameter with the `@` syntax. It can add metadata or change behavior. Nest uses decorators everywhere, for example `@Controller()`, `@Get()`, `@Injectable()` and `@Body()`.

### 83: Does NestJS work with JavaScript instead of TypeScript?

Yes, but it is rare. You need Babel to support decorators, and you lose type-based injection, so you have to declare dependencies by hand with `@Dependencies()` or `@Inject()`. Almost all Nest projects use TypeScript.

### 84: What TypeScript compiler options does Nest need?

`experimentalDecorators: true` and `emitDecoratorMetadata: true`. Without the second one, Nest cannot read constructor parameter types and dependency injection breaks. The default `tsconfig.json` from `nest new` already has both.

### 85: How do you serve static files?

Install `@nestjs/serve-static` and import the module.

```ts
import { ServeStaticModule } from "@nestjs/serve-static";
import { join } from "path";

@Module({
  imports: [
    ServeStaticModule.forRoot({
      rootPath: join(__dirname, "..", "public"),
    }),
  ],
})
export class AppModule {}
```

With Express you can also call `app.useStaticAssets()` on a `NestExpressApplication`.

### 86: How do you upload a single file?

Use `FileInterceptor` and `@UploadedFile()`. This uses `multer` and works with the Express adapter.

```ts
import { FileInterceptor } from '@nestjs/platform-express';

@Post('upload')
@UseInterceptors(FileInterceptor('file'))
upload(@UploadedFile() file: Express.Multer.File) {
  return { name: file.originalname, size: file.size };
}
```

Install `@types/multer` to get the `Express.Multer.File` type.

### 87: How do you upload several files?

```ts
@Post('photos')
@UseInterceptors(FilesInterceptor('photos', 10))
uploadMany(@UploadedFiles() files: Express.Multer.File[]) {
  return files.map((f) => f.originalname);
}
```

The second argument is the max number of files.

### 88: How do you read cookies?

Install `cookie-parser`, register it, then read cookies from the request.

```ts
import cookieParser from "cookie-parser";
app.use(cookieParser());
```

```ts
@Get()
findAll(@Req() req: Request) {
  return req.cookies['token'];
}
```

### 89: How do you set a cookie?

```ts
@Post('login')
login(@Res({ passthrough: true }) res: Response) {
  res.cookie('token', 'abc', { httpOnly: true, secure: true });
  return { ok: true };
}
```

### 90: How do you write a simple unit test for a service?

```ts
import { Test } from "@nestjs/testing";

describe("CatsService", () => {
  let service: CatsService;

  beforeEach(async () => {
    const moduleRef = await Test.createTestingModule({
      providers: [CatsService],
    }).compile();

    service = moduleRef.get(CatsService);
  });

  it("starts empty", () => {
    expect(service.findAll()).toEqual([]);
  });
});
```

### 91: Which test runner does Nest use?

Older projects and CommonJS projects use Jest. Since Nest 12, ESM projects created with the CLI use Vitest by default. The `@nestjs/testing` package works with either one.

### 92: What is `Test.createTestingModule()`?

It builds a small Nest module just for the test. You list the providers and controllers you need, call `.compile()`, and then get instances with `moduleRef.get()`. You can swap real providers for fakes before compiling.

### 93: How do you mock a dependency in a unit test?

Give the provider a fake value.

```ts
const moduleRef = await Test.createTestingModule({
  controllers: [CatsController],
  providers: [
    {
      provide: CatsService,
      useValue: { findAll: vi.fn().mockResolvedValue(["Tom"]) },
    },
  ],
}).compile();
```

With Jest use `jest.fn()` instead of `vi.fn()`.

### 94: What is an end-to-end (e2e) test in Nest?

A test that starts the whole app (or a large part of it) and sends real HTTP requests to it, usually with `supertest`.

```ts
import request from "supertest";

describe("Cats (e2e)", () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = moduleRef.createNestApplication();
    await app.init();
  });

  it("GET /cats", () => {
    return request(app.getHttpServer()).get("/cats").expect(200);
  });

  afterAll(async () => {
    await app.close();
  });
});
```

### 95: What is the difference between `app.init()` and `app.listen()`?

`init()` sets up the app (runs lifecycle hooks, registers routes) without opening a port. `listen()` does the same and also starts the HTTP server. In e2e tests `init()` is enough because `supertest` uses the server object directly.

### 96: How do you add Swagger docs to a Nest app?

```bash
npm i @nestjs/swagger
```

```ts
import { DocumentBuilder, SwaggerModule } from "@nestjs/swagger";

const config = new DocumentBuilder()
  .setTitle("Cats API")
  .setVersion("1.0")
  .addBearerAuth()
  .build();
const document = SwaggerModule.createDocument(app, config);
SwaggerModule.setup("docs", app, document);
```

The UI is then available at `/docs`.

### 97: What does `@ApiProperty()` do?

It tells Swagger about a DTO property so it shows up in the docs with its type, example and description.

```ts
export class CreateCatDto {
  @ApiProperty({ example: "Tom" })
  name: string;

  @ApiProperty({ required: false })
  age?: number;
}
```

The Swagger CLI plugin can add most of these for you automatically.

### 98: How do you connect to a SQL database with TypeORM?

```bash
npm i @nestjs/typeorm typeorm pg
```

```ts
@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: "postgres",
      url: process.env.DATABASE_URL,
      autoLoadEntities: true,
      synchronize: false,
    }),
  ],
})
export class AppModule {}
```

Keep `synchronize` off in production and use migrations instead.

### 99: How do you inject a TypeORM repository?

Register the entity in the feature module with `forFeature()` and inject it with `@InjectRepository()`.

```ts
@Module({
  imports: [TypeOrmModule.forFeature([User])],
  providers: [UsersService],
})
export class UsersModule {}
```

```ts
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User) private readonly usersRepo: Repository<User>,
  ) {}

  findAll() {
    return this.usersRepo.find();
  }
}
```

### 100: How do you connect to MongoDB?

Use `@nestjs/mongoose`.

```ts
@Module({
  imports: [MongooseModule.forRoot("mongodb://localhost/nest")],
})
export class AppModule {}
```

```ts
@Schema()
export class Cat {
  @Prop({ required: true })
  name: string;
}
export const CatSchema = SchemaFactory.createForClass(Cat);
```

```ts
@Module({
  imports: [MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }])],
})
export class CatsModule {}
```

Inject the model with `@InjectModel(Cat.name) private catModel: Model<Cat>`.

### 101: How do you use Prisma with Nest?

Prisma has no official Nest module. The usual way is a service that extends (or wraps) the Prisma client.

```ts
@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit {
  async onModuleInit() {
    await this.$connect();
  }
}
```

Add `PrismaService` to a module, export it, and inject it wherever you need database access.

### 102: What is the difference between `providers` and `controllers` in a module?

Controllers handle routes and are created by Nest but are not injectable into other classes. Providers are injectable classes or values. A controller can inject providers, but you cannot inject a controller into a provider.

### 103: Can you inject a provider into another provider?

Yes. A service can inject other services, repositories or config through its constructor, as long as they are available in the same module or exported by an imported module.

### 104: What happens if Nest cannot find a dependency?

The app fails on startup with an error like:

```
Nest can't resolve dependencies of the CatsService (?). Please make sure that
the argument UsersService at index [0] is available in the CatsModule context.
```

The fix is usually to add the provider to the module, or export it from its own module and import that module.

### 105: What is the root module?

The module you pass to `NestFactory.create()`, usually `AppModule`. Nest starts from it and walks through all imports to build the app.

### 106: How do you enable versioning of routes?

```ts
app.enableVersioning({ type: VersioningType.URI });
```

```ts
@Controller({ path: "cats", version: "1" })
export class CatsV1Controller {}
```

Now the route is `/v1/cats`. Other types are header, media type and custom.

### 107: What is `@nestjs/terminus` for?

It adds health check endpoints that tools like Kubernetes or load balancers can call. It has ready-made checks for HTTP endpoints, databases, memory and disk.

```ts
@Controller("health")
export class HealthController {
  constructor(
    private health: HealthCheckService,
    private db: TypeOrmHealthIndicator,
  ) {}

  @Get()
  @HealthCheck()
  check() {
    return this.health.check([() => this.db.pingCheck("database")]);
  }
}
```

### 108: How do you cache responses?

Install `@nestjs/cache-manager` and `cache-manager`, register the module and use `CacheInterceptor`.

```ts
@Module({
  imports: [CacheModule.register({ ttl: 5000 })],
})
export class AppModule {}
```

```ts
@Controller("cats")
@UseInterceptors(CacheInterceptor)
export class CatsController {
  @Get()
  findAll() {
    return this.catsService.findAll();
  }
}
```

Since cache-manager v6 (used from Nest 11), `ttl` is in milliseconds.

### 109: How do you run a job on a schedule?

Use `@nestjs/schedule`.

```ts
@Module({ imports: [ScheduleModule.forRoot()] })
export class AppModule {}
```

```ts
@Injectable()
export class TasksService {
  @Cron(CronExpression.EVERY_HOUR)
  cleanup() {
    // runs every hour
  }

  @Interval(10_000)
  ping() {}

  @Timeout(5_000)
  once() {}
}
```

### 110: What is `@nestjs/event-emitter` used for?

It lets one part of your app publish an event and other parts react to it, without them knowing about each other.

```ts
this.eventEmitter.emit("order.created", new OrderCreatedEvent(order.id));
```

```ts
@OnEvent('order.created')
handleOrderCreated(event: OrderCreatedEvent) {
  // send email
}
```

Register `EventEmitterModule.forRoot()` in the root module.

### 111: What is a WebSocket gateway?

A class marked with `@WebSocketGateway()` that handles real-time messages, similar to how a controller handles HTTP requests.

```ts
@WebSocketGateway()
export class ChatGateway {
  @SubscribeMessage("message")
  handleMessage(@MessageBody() data: string): string {
    return data;
  }
}
```

It uses Socket.IO by default (`@nestjs/platform-socket.io`), or plain `ws` with `@nestjs/platform-ws`.

### 112: What is a microservice in NestJS?

A Nest app that talks to other services over a transport other than HTTP, like TCP, Redis, NATS, RabbitMQ, Kafka, MQTT or gRPC. Instead of routes it has message handlers marked with `@MessagePattern()` or `@EventPattern()`. The package is `@nestjs/microservices`.

### 113: What is the difference between `@MessagePattern()` and `@EventPattern()`?

`@MessagePattern()` is for request-response: the caller waits for a reply. `@EventPattern()` is for events: the caller sends it and does not wait for any answer.

### 114: Does Nest support GraphQL?

Yes, through `@nestjs/graphql` with Apollo or Mercurius drivers. You can write resolvers in code-first style (TypeScript classes generate the schema) or schema-first style (you write the `.graphql` files and Nest generates types).

### 115: What is a resolver in Nest GraphQL?

A class that handles GraphQL queries, mutations and field values. It is the GraphQL version of a controller.

```ts
@Resolver(() => Author)
export class AuthorsResolver {
  constructor(private authorsService: AuthorsService) {}

  @Query(() => Author)
  author(@Args("id", { type: () => Int }) id: number) {
    return this.authorsService.findOne(id);
  }
}
```

### 116: How do you get the client IP address?

```ts
@Get()
whoAmI(@Ip() ip: string) {
  return ip;
}
```

If the app is behind a proxy, enable `trust proxy` on Express so the IP comes from `X-Forwarded-For`.

### 117: What does `@All()` do?

It maps a route to every HTTP method, so `GET`, `POST`, `PUT` and the rest all hit the same handler.

### 118: How do wildcard routes work in Nest 11 and 12?

With Express 5, a bare `*` is not allowed anymore. Wildcards must have a name.

```ts
@Get('files/*path')
getFile(@Param('path') path: string[]) {
  return path.join('/');
}
```

The matched segments come back as an array. Use `{*path}` if the wildcard should also match an empty path.

### 119: How do you make a route parameter optional in Express 5 style paths?

Use braces instead of a question mark.

```ts
// old: @Get('users/:id?')
@Get('users{/:id}')
find(@Param('id') id?: string) {}
```

### 120: What is `@HostParam()`?

You can limit a controller to a host name and read parts of the host.

```ts
@Controller({ host: ":account.example.com" })
export class AccountController {
  @Get()
  getInfo(@HostParam("account") account: string) {
    return account;
  }
}
```

### 121: How do you read a value from the session?

With `express-session` registered, use `@Session()`.

```ts
@Get()
visits(@Session() session: Record<string, any>) {
  session.visits = (session.visits ?? 0) + 1;
  return session.visits;
}
```

### 122: How do you close a Nest app?

Call `await app.close()`. This runs the shutdown lifecycle hooks and closes the HTTP server and connections.

### 123: What does `app.enableShutdownHooks()` do?

It makes Nest listen for system signals like `SIGTERM`. When one arrives, Nest calls `onModuleDestroy`, `beforeApplicationShutdown` and `onApplicationShutdown` on your providers so you can close connections cleanly. It is off by default because it adds signal listeners.

```ts
app.enableShutdownHooks();
```

### 124: What are lifecycle hooks?

Methods Nest calls at certain moments:

- `onModuleInit()` - after the module's dependencies are resolved.
- `onApplicationBootstrap()` - after all modules are initialized, before listening.
- `onModuleDestroy()` - after a shutdown signal is received.
- `beforeApplicationShutdown()` - after all `onModuleDestroy()` calls finish.
- `onApplicationShutdown()` - after connections are closed.

### 125: How do you use `onModuleInit()`?

Implement the interface and the method. It can be async, and Nest waits for it.

```ts
@Injectable()
export class CacheWarmer implements OnModuleInit {
  async onModuleInit() {
    await this.loadData();
  }
}
```

### 126: What is an entity?

A class that maps to a database table (TypeORM, MikroORM) or collection. It is not a Nest concept itself, but `nest g resource` creates an `entities` folder for it.

```ts
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  email: string;
}
```

### 127: What is the difference between an entity and a DTO?

An entity describes how data is stored. A DTO describes what the API receives or returns. Keeping them separate means you do not accidentally expose database fields like `passwordHash` or let clients set fields like `id`.

### 128: How do you make all properties of a DTO optional for update requests?

Use `PartialType`.

```ts
import { PartialType } from "@nestjs/mapped-types";

export class UpdateCatDto extends PartialType(CreateCatDto) {}
```

Import it from `@nestjs/swagger` instead if you use Swagger, so the docs stay correct.

### 129: What does the `@Optional()` decorator do?

It tells Nest that a dependency is not required. If no provider is found, Nest injects `undefined` instead of failing.

```ts
constructor(@Optional() @Inject('HTTP_OPTIONS') private options?: HttpOptions) {}
```

### 130: What does `@Inject()` do?

It tells Nest which token to inject when the type alone is not enough, for example when the provider is registered with a string or symbol token.

```ts
constructor(@Inject('API_KEY') private apiKey: string) {}
```

### 131: What is a custom provider with `useValue`?

It registers a fixed value under a token.

```ts
@Module({
  providers: [{ provide: "API_KEY", useValue: "secret-key" }],
})
export class AppModule {}
```

It is often used for constants and for mocks in tests.

### 132: How do you protect against common web attacks with headers?

Use `helmet`, which sets security headers like `Content-Security-Policy` and `X-Frame-Options`.

```ts
import helmet from "helmet";
app.use(helmet());
```

For Fastify, use `@fastify/helmet` and register it with `app.register()`.

### 133: How do you add rate limiting?

Use `@nestjs/throttler`.

```ts
@Module({
  imports: [ThrottlerModule.forRoot([{ ttl: 60_000, limit: 10 }])],
  providers: [{ provide: APP_GUARD, useClass: ThrottlerGuard }],
})
export class AppModule {}
```

This allows 10 requests per minute per client. `ttl` is in milliseconds.

### 134: What is `@SkipThrottle()`?

It turns off rate limiting for a controller or route, for example a health check.

```ts
@SkipThrottle()
@Get('health')
health() {
  return 'ok';
}
```

### 135: What does `nest info` show?

It prints the installed Nest package versions, Node version and OS. It is useful when filing bug reports or checking upgrades.

### 136: How do you upgrade a project to the latest Nest version?

In Nest 12 the CLI has an `upgrade` command.

```bash
npm i -g @nestjs/cli@latest
nest upgrade --dry-run
nest upgrade
```

It updates all `@nestjs/*` packages together. Then read the migration guide for breaking changes.

### 137: Should Nest packages be on the same version?

Yes. `@nestjs/common`, `@nestjs/core` and the platform packages should share the same major and ideally minor version. Mixing versions can cause strange DI errors because each package may end up with its own copy of shared classes.

### 138: What does `ESM` mean for Nest 12 users?

All Nest packages are now published as ES modules. Existing CommonJS apps still work because current Node versions can `require()` ES modules. Moving your own app to ESM is optional. If you do, you add `"type": "module"` to `package.json` and use `.js` extensions in relative imports.

### 139: What is the SWC builder?

SWC is a fast compiler written in Rust. Nest can use it instead of `tsc` to build and run the app much faster in development.

```bash
npm i -D @swc/cli @swc/core
nest start -b swc --watch
```

SWC does not type check, so you can add `--type-check` or run `tsc --noEmit` in CI.

### 140: What is Rspack in the Nest CLI?

Rspack is a fast bundler compatible with webpack. Since Nest 12 it replaces webpack as the bundling option (`--builder rspack`), and it is the default for monorepos. The `--webpack` flag is deprecated.

### 141: What is the difference between `Get()` and `Get('')`?

Nothing. Both map to the controller's base path.

### 142: Can two controllers share the same route path?

They can share a prefix, but if two handlers match the exact same method and path, only the first one registered handles the request. In Nest 12 you can turn on route conflict checks to catch this at startup (`routeConflictPolicy` in `NestFactory.create()` options).

### 143: How do you return a file download?

Return a `StreamableFile`.

```ts
@Get('report')
getReport(): StreamableFile {
  const file = createReadStream(join(process.cwd(), 'report.pdf'));
  return new StreamableFile(file, {
    type: 'application/pdf',
    disposition: 'attachment; filename="report.pdf"',
  });
}
```

Interceptors still run because you are not using `@Res()`.

### 144: How do you render an HTML template?

With Express, set a view engine and use `@Render()`.

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.setBaseViewsDir(join(__dirname, "..", "views"));
app.setViewEngine("hbs");
```

```ts
@Get()
@Render('index')
root() {
  return { message: 'Hello world!' };
}
```

### 145: What does `@nestjs/axios` provide?

An `HttpService` that wraps Axios and returns Observables. You usually turn them into promises with `firstValueFrom`.

```ts
@Injectable()
export class WeatherService {
  constructor(private http: HttpService) {}

  async getWeather(city: string) {
    const { data } = await firstValueFrom(
      this.http.get(`https://api.example.com/weather?city=${city}`),
    );
    return data;
  }
}
```

Import `HttpModule` in the module.

### 146: Can you use the native `fetch` instead of `@nestjs/axios`?

Yes. Node 20+ has `fetch` built in, and you can call it from any service. `@nestjs/axios` is just a convenience if you want Axios features like interceptors and module-level config.

### 147: What is a monorepo in Nest CLI terms?

A workspace with several apps and shared libraries in one repository. You create it by generating a second app or a library.

```bash
nest g app admin
nest g library shared
```

Libraries are imported with path aliases like `@app/shared`.

### 148: How do you get a provider instance outside of DI, for example in `main.ts`?

Use `app.get()`.

```ts
const app = await NestFactory.create(AppModule);
const config = app.get(ConfigService);
await app.listen(config.get("PORT") ?? 3000);
```

### 149: What is a standalone application?

A Nest app without an HTTP server. You create it with `NestFactory.createApplicationContext()` and use it for scripts, CLI tools or workers.

```ts
const app = await NestFactory.createApplicationContext(AppModule);
const seeder = app.get(SeederService);
await seeder.run();
await app.close();
```

### 150: Where can you find official help and docs?

The official docs are at docs.nestjs.com. The source and issues are on GitHub at `nestjs/nest`, and there is an official Discord server. Each major release has a migration guide in the docs.

## Moderate Questions (151-300)

### 151: What kinds of custom providers are there?

- `useClass` - provide a class, possibly a different one than the token.
- `useValue` - provide a fixed value or object.
- `useFactory` - provide whatever a function returns. The function can be async and can inject other providers.
- `useExisting` - make a token an alias for another provider.

### 152: When would you use `useClass` with a different class than the token?

When you want to switch the implementation based on the environment or for tests, while the rest of the code keeps injecting the same token.

```ts
const configServiceProvider = {
  provide: ConfigService,
  useClass:
    process.env.NODE_ENV === "development"
      ? DevelopmentConfigService
      : ProductionConfigService,
};
```

### 153: How do you write a factory provider that depends on other providers?

```ts
{
  provide: 'DB_CONNECTION',
  useFactory: async (config: ConfigService) => {
    const conn = await createConnection(config.getOrThrow('DATABASE_URL'));
    return conn;
  },
  inject: [ConfigService],
}
```

The items in `inject` are passed to the factory in the same order. A dependency can be marked optional: `inject: [{ token: 'LOGGER', optional: true }]`.

### 154: What is an async provider?

A factory provider whose `useFactory` returns a promise. Nest waits for the promise to resolve before creating any class that depends on it. This is how database connections are usually set up, so nothing uses the connection before it is ready.

### 155: What does `useExisting` do?

It creates an alias. Both tokens resolve to the same instance.

```ts
@Module({
  providers: [
    LoggerService,
    { provide: "AliasedLogger", useExisting: LoggerService },
  ],
})
export class AppModule {}
```

### 156: Why use a `Symbol` or an `InjectionToken` instead of a string token?

String tokens can clash if two libraries use the same name. A `Symbol` is always unique. It is common to keep tokens in a separate file so they can be imported without circular imports.

```ts
export const PAYMENT_GATEWAY = Symbol("PAYMENT_GATEWAY");

@Module({
  providers: [{ provide: PAYMENT_GATEWAY, useClass: StripeGateway }],
})
export class PaymentsModule {}
```

### 157: How do you inject an interface implementation?

Interfaces do not exist at runtime, so you cannot use them as tokens. Use a token (symbol or string) or an abstract class instead.

```ts
export abstract class PaymentGateway {
  abstract charge(amount: number): Promise<void>;
}

@Module({
  providers: [{ provide: PaymentGateway, useClass: StripeGateway }],
})
export class PaymentsModule {}

@Injectable()
export class OrdersService {
  constructor(private gateway: PaymentGateway) {}
}
```

An abstract class works as a token without `@Inject()`.

### 158: What is a dynamic module?

A module that is configured when it is imported. It has a static method (by convention `forRoot`, `register` or `forFeature`) that returns a `DynamicModule` object with providers built from the options.

```ts
@Module({})
export class MailModule {
  static register(options: MailOptions): DynamicModule {
    return {
      module: MailModule,
      providers: [{ provide: "MAIL_OPTIONS", useValue: options }, MailService],
      exports: [MailService],
    };
  }
}
```

### 159: What is the difference between `forRoot`, `register` and `forFeature`?

They are conventions, not rules:

- `forRoot` - configure once for the whole app, like a database connection.
- `register` - configure for the module that imports it; each import can have its own config.
- `forFeature` - reuse the `forRoot` setup but add something for one feature, like specific repositories.

### 160: What is `forRootAsync` and why is it useful?

It lets you build the module options with a factory that can inject other providers, most often `ConfigService`. That way options come from env vars that are loaded at runtime.

```ts
TypeOrmModule.forRootAsync({
  imports: [ConfigModule],
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    type: "postgres",
    url: config.getOrThrow("DATABASE_URL"),
    autoLoadEntities: true,
  }),
});
```

### 161: What is `ConfigurableModuleBuilder`?

A helper that generates the boilerplate for a dynamic module, including `register` and `registerAsync`, the options token and the types.

```ts
export interface MailModuleOptions {
  apiKey: string;
}

export const {
  ConfigurableModuleClass,
  MODULE_OPTIONS_TOKEN,
  OPTIONS_TYPE,
  ASYNC_OPTIONS_TYPE,
} = new ConfigurableModuleBuilder<MailModuleOptions>().build();
```

```ts
@Module({
  providers: [MailService],
  exports: [MailService],
})
export class MailModule extends ConfigurableModuleClass {}

@Injectable()
export class MailService {
  constructor(
    @Inject(MODULE_OPTIONS_TOKEN) private options: MailModuleOptions,
  ) {}
}
```

Now you can call `MailModule.register({...})` or `MailModule.registerAsync({...})`.

### 162: How do you rename the generated method to `forRoot` with `ConfigurableModuleBuilder`?

```ts
new ConfigurableModuleBuilder<MailModuleOptions>()
  .setClassMethodName("forRoot")
  .build();
```

You can also use `setFactoryMethodName('createMailOptions')` to change the name of the method that options factory classes must implement.

### 163: What are the injection scopes?

- `DEFAULT` - one shared instance for the whole app (singleton).
- `REQUEST` - a new instance for each incoming request.
- `TRANSIENT` - a new instance for each class that injects it.

```ts
@Injectable({ scope: Scope.REQUEST })
export class RequestContextService {}
```

### 164: What is scope bubbling?

If a provider depends on a request-scoped provider, it becomes request-scoped too, and so does anything that depends on it, all the way up to the controller. So one request-scoped service deep in the tree can make a large part of your app get recreated on every request.

### 165: How do you get the current request inside a service?

Make the service request-scoped and inject `REQUEST`.

```ts
@Injectable({ scope: Scope.REQUEST })
export class AuditService {
  constructor(@Inject(REQUEST) private request: Request) {}

  user() {
    return this.request.user;
  }
}
```

Many teams use `AsyncLocalStorage` (for example through `nestjs-cls`) instead, to avoid the cost of request scope.

### 166: What is the downside of request-scoped providers?

They are created for every request, together with everything that bubbles up from them. That adds CPU work and memory churn. For most apps it is small, but on hot paths it adds up. They also cannot be used in places that run outside a request, like cron jobs, without extra work.

### 167: What does `INQUIRER` do?

In a transient provider you can inject `INQUIRER` to find out which class asked for it. This is handy for loggers that want the class name as context.

```ts
@Injectable({ scope: Scope.TRANSIENT })
export class ContextLogger {
  constructor(@Inject(INQUIRER) private parent: object) {}

  log(message: string) {
    console.log(`[${this.parent?.constructor?.name}] ${message}`);
  }
}
```

### 168: What is a circular dependency and how do you solve it in Nest?

It happens when A needs B and B needs A. Nest cannot create either first. You can break the cycle with `forwardRef()` on both sides:

```ts
@Injectable()
export class CatsService {
  constructor(
    @Inject(forwardRef(() => CommonService))
    private commonService: CommonService,
  ) {}
}
```

For modules: `imports: [forwardRef(() => CatsModule)]`. Often the better fix is to move the shared logic into a third service so the cycle goes away.

### 169: What is `ModuleRef`?

A class you can inject to look up providers at runtime instead of through the constructor.

```ts
@Injectable()
export class HandlerService {
  constructor(private moduleRef: ModuleRef) {}

  run() {
    const service = this.moduleRef.get(SomeService, { strict: false });
    return service.doWork();
  }
}
```

`strict: false` searches the whole app, not only the current module.

### 170: What is the difference between `moduleRef.get()` and `moduleRef.resolve()`?

`get()` returns existing singleton instances. It throws for request-scoped or transient providers. `resolve()` is async and creates (or returns) a scoped instance. Each call to `resolve()` without a context ID gives a new instance.

```ts
const contextId = ContextIdFactory.create();
const a = await this.moduleRef.resolve(TransientService, contextId);
const b = await this.moduleRef.resolve(TransientService, contextId);
// a === b because they share a context id
```

### 171: What does `moduleRef.create()` do?

It creates a new instance of a class that is not registered as a provider, and still injects its dependencies. Useful for plugin-style code where the class is chosen at runtime.

```ts
const strategy = await this.moduleRef.create(CsvExportStrategy);
```

### 172: What are the different binding levels for pipes, guards, interceptors and filters?

- Global - `app.useGlobalX()` or an `APP_X` provider.
- Controller - `@UseX()` on the class.
- Method - `@UseX()` on the handler.
- Parameter - pipes only, for example `@Param('id', ParseIntPipe)`.

### 173: Why use `APP_GUARD` instead of `app.useGlobalGuards()`?

Guards registered with `useGlobalGuards()` in `main.ts` are created outside any module, so they cannot use dependency injection. Registering with `APP_GUARD` in a module lets Nest create the guard with its dependencies. The same goes for `APP_PIPE`, `APP_INTERCEPTOR` and `APP_FILTER`.

```ts
@Module({
  providers: [{ provide: APP_GUARD, useClass: JwtAuthGuard }],
})
export class AppModule {}
```

E2e tests also pick these up automatically because they live in the module.

### 174: In what order do multiple guards run?

Global guards first, then controller guards, then method guards. Within the same `@UseGuards(A, B)` they run left to right. If one returns `false` or throws, the rest are skipped.

### 175: In what order do interceptors run before and after the handler?

Before the handler, global runs first, then controller, then method. After the handler the order is reversed (method, controller, global), because each one wraps the next like layers of an onion.

### 176: In what order do exception filters run?

The opposite way: Nest looks for a filter on the method first, then the controller, then global. The first one whose `@Catch()` matches the error handles it and the rest are skipped.

### 177: What is `ExecutionContext`?

It extends `ArgumentsHost` and gives info about the current call: which class and handler are running (`getClass()`, `getHandler()`) and what kind of request it is (`getType()` returns `'http'`, `'rpc'`, `'ws'` or `'graphql'` with the GraphQL package). Guards and interceptors receive it.

### 178: What is `ArgumentsHost`?

An object that wraps the arguments passed to a handler. Because Nest supports HTTP, RPC and WebSockets, you switch to the right context first.

```ts
const ctx = host.switchToHttp();
const request = ctx.getRequest<Request>();
const response = ctx.getResponse<Response>();
```

Use `switchToRpc()` or `switchToWs()` for other transports.

### 179: How do you write a custom exception filter?

```ts
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();
    const status = exception.getStatus();

    response.status(status).json({
      statusCode: status,
      path: request.url,
      timestamp: new Date().toISOString(),
      message: exception.message,
    });
  }
}
```

Apply it with `@UseFilters(HttpExceptionFilter)` or globally.

### 180: How do you catch every exception, not just `HttpException`?

Leave `@Catch()` empty. To stay platform-agnostic, use `HttpAdapterHost` instead of the Express response.

```ts
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  constructor(private readonly httpAdapterHost: HttpAdapterHost) {}

  catch(exception: unknown, host: ArgumentsHost) {
    const { httpAdapter } = this.httpAdapterHost;
    const ctx = host.switchToHttp();
    const status =
      exception instanceof HttpException
        ? exception.getStatus()
        : HttpStatus.INTERNAL_SERVER_ERROR;

    httpAdapter.reply(
      ctx.getResponse(),
      { statusCode: status, path: httpAdapter.getRequestUrl(ctx.getRequest()) },
      status,
    );
  }
}
```

### 181: How do you extend the built-in exception filter?

Extend `BaseExceptionFilter` and call `super.catch()` for anything you do not handle.

```ts
@Catch()
export class LoggingFilter extends BaseExceptionFilter {
  private readonly logger = new Logger(LoggingFilter.name);

  catch(exception: unknown, host: ArgumentsHost) {
    this.logger.error(exception);
    super.catch(exception, host);
  }
}
```

When registered globally in `main.ts`, pass the adapter: `new LoggingFilter(httpAdapter)`.

### 182: How do you create your own exception class?

Extend `HttpException` or one of the built-in ones.

```ts
export class InsufficientFundsException extends BadRequestException {
  constructor(balance: number) {
    super(`Balance too low: ${balance}`, { errorCode: "INSUFFICIENT_FUNDS" });
  }
}
```

### 183: How do you write a custom pipe?

Implement `PipeTransform`.

```ts
@Injectable()
export class TrimPipe implements PipeTransform<string, string> {
  transform(value: string, metadata: ArgumentMetadata): string {
    if (typeof value !== "string") {
      throw new BadRequestException("Expected a string");
    }
    return value.trim();
  }
}
```

In Nest 12 the `transform` types are stricter and `ArgumentMetadata` is generic, so declare the input and output types.

### 184: What is in `ArgumentMetadata`?

- `type` - `'body'`, `'query'`, `'param'` or `'custom'`.
- `metatype` - the declared TypeScript type of the parameter, like `CreateCatDto` or `Number`.
- `data` - the string passed to the decorator, like `'id'` in `@Param('id')`.

### 185: How do you write a guard that checks roles?

Store the roles with a decorator, read them in the guard with `Reflector`.

```ts
export const Roles = Reflector.createDecorator<string[]>();
```

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
    return roles.some((role) => user?.roles?.includes(role));
  }
}
```

```ts
@Post()
@Roles(['admin'])
create() {}
```

### 186: What is the difference between `Reflector.createDecorator()` and `SetMetadata()`?

Both store metadata. `SetMetadata('roles', [...])` uses a string key, so you have to repeat the key in the guard and there is no type checking. `Reflector.createDecorator<T>()` creates a typed decorator that you pass directly to `reflector.get()`, so the type flows through.

### 187: What is the difference between `getAllAndOverride` and `getAllAndMerge`?

Both read metadata from several targets (usually the handler and the class). `getAllAndOverride` returns the first value it finds, so the method setting wins over the class. `getAllAndMerge` combines the values into one array or object.

### 188: How do you make some routes public when you have a global auth guard?

Add a `@Public()` decorator and skip the check in the guard.

```ts
export const IS_PUBLIC_KEY = "isPublic";
export const Public = () => SetMetadata(IS_PUBLIC_KEY, true);
```

```ts
canActivate(context: ExecutionContext) {
  const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
    context.getHandler(),
    context.getClass(),
  ]);
  if (isPublic) return true;
  // check token...
}
```

### 189: How do you create a custom parameter decorator?

Use `createParamDecorator`.

```ts
export const CurrentUser = createParamDecorator(
  (data: keyof User | undefined, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest();
    return data ? request.user?.[data] : request.user;
  },
);
```

```ts
@Get('me')
me(@CurrentUser() user: User) {
  return user;
}

@Get('my-email')
email(@CurrentUser('email') email: string) {
  return email;
}
```

### 190: Do pipes run on custom parameter decorators?

Yes, if you pass them in, like `@CurrentUser(new ValidationPipe())`. For global `ValidationPipe` to validate a custom decorator value, set `validateCustomDecorators: true`.

### 191: How do you combine several decorators into one?

Use `applyDecorators`.

```ts
export function Auth(...roles: string[]) {
  return applyDecorators(
    Roles(roles),
    UseGuards(JwtAuthGuard, RolesGuard),
    ApiBearerAuth(),
    ApiUnauthorizedResponse({ description: 'Unauthorized' }),
  );
}

@Get('users')
@Auth('admin')
findAll() {}
```

### 192: How do you implement JWT authentication without Passport?

Use `@nestjs/jwt` and a guard.

```ts
@Module({
  imports: [
    JwtModule.register({
      global: true,
      secret: process.env.JWT_SECRET,
      signOptions: { expiresIn: "15m" },
    }),
  ],
})
export class AuthModule {}
```

```ts
@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private jwtService: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const [type, token] = request.headers.authorization?.split(" ") ?? [];
    if (type !== "Bearer" || !token) throw new UnauthorizedException();
    try {
      request.user = await this.jwtService.verifyAsync(token);
    } catch {
      throw new UnauthorizedException();
    }
    return true;
  }
}
```

Sign tokens with `await this.jwtService.signAsync({ sub: user.id })`.

### 193: How do you use Passport with Nest?

Install `@nestjs/passport` and a strategy, write a class that extends `PassportStrategy`, and protect routes with `AuthGuard('<name>')`.

```ts
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor(config: ConfigService) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: config.getOrThrow("JWT_SECRET"),
    });
  }

  validate(payload: { sub: string; email: string }) {
    return { id: payload.sub, email: payload.email };
  }
}
```

```ts
@UseGuards(AuthGuard('jwt'))
@Get('profile')
profile(@Req() req) {
  return req.user;
}
```

Whatever `validate()` returns is put on `request.user`.

### 194: How do you implement refresh tokens?

Issue two tokens at login: a short-lived access token (minutes) and a long-lived refresh token (days). Store a hash of the refresh token in the database. When the access token expires, the client calls a `/refresh` endpoint with the refresh token; you verify it, compare it to the stored hash, issue new tokens and replace the stored hash (rotation). On logout, delete the stored hash. Use a different secret for each token type.

### 195: How do you validate nested objects?

Use `@ValidateNested()` and `@Type()` from `class-transformer` so the nested object becomes a class instance.

```ts
class AddressDto {
  @IsString()
  city: string;
}

export class CreateUserDto {
  @ValidateNested()
  @Type(() => AddressDto)
  address: AddressDto;
}
```

Without `@Type()`, the nested object stays a plain object and its rules are ignored.

### 196: How do you validate an array of DTOs in the body?

Either wrap it in a DTO with `@ValidateNested({ each: true })`, or use `ParseArrayPipe`.

```ts
@Post('bulk')
createBulk(
  @Body(new ParseArrayPipe({ items: CreateUserDto }))
  dtos: CreateUserDto[],
) {}
```

Generic types like `CreateUserDto[]` lose their item type at runtime, which is why `ValidationPipe` alone does not validate them.

### 197: What does `enableImplicitConversion` do?

In `transformOptions`, it makes `class-transformer` convert values based on the TypeScript type, so query strings like `"10"` become numbers without `@Type(() => Number)`.

```ts
new ValidationPipe({
  transform: true,
  transformOptions: { enableImplicitConversion: true },
});
```

Be careful with booleans: the string `"false"` becomes `true` because any non-empty string is truthy.

### 198: How do you write a custom `class-validator` rule?

```ts
@ValidatorConstraint({ name: "isStrongPassword", async: false })
export class IsStrongPasswordConstraint implements ValidatorConstraintInterface {
  validate(value: string) {
    return /[A-Z]/.test(value) && /\d/.test(value) && value.length >= 8;
  }
  defaultMessage() {
    return "Password must have 8+ chars, a capital letter and a number";
  }
}

export function IsStrongPassword(options?: ValidationOptions) {
  return (object: object, propertyName: string) =>
    registerDecorator({
      target: object.constructor,
      propertyName,
      options,
      validator: IsStrongPasswordConstraint,
    });
}
```

### 199: How do you make a `class-validator` constraint use Nest DI (for example to check the database)?

Make the constraint `@Injectable()`, register it as a provider, and tell class-validator to use Nest's container.

```ts
// main.ts
useContainer(app.select(AppModule), { fallbackOnErrors: true });
```

The constraint can then inject a repository and be `async: true`.

### 200: What is the `errorFormat` option on `ValidationPipe` in Nest 12?

It controls the shape of validation errors. `'list'` (the default) returns an array of strings. `'grouped'` returns an object keyed by property path, with the messages for each field.

```ts
app.useGlobalPipes(new ValidationPipe({ errorFormat: "grouped" }));
```

This is easier for front-ends that show errors next to each form field.

### 201: How do you change the error response of `StandardSchemaValidationPipe`?

Pass an `exceptionFactory` that receives the schema issues.

```ts
app.useGlobalPipes(
  new StandardSchemaValidationPipe({
    exceptionFactory: (issues) =>
      new UnprocessableEntityException({
        errors: issues.map((issue) => ({
          path: issue.path
            ?.map((p) => (typeof p === "object" ? p.key : p))
            .join("."),
          message: issue.message,
        })),
      }),
  }),
);
```

### 202: Is it safe to bind `StandardSchemaValidationPipe` globally?

Yes. It only validates parameters that declare a `schema` option, and leaves the others alone. By default it passes the schema output (for example coerced numbers) to the handler. Set `transform: false` to pass the original input instead.

### 203: Can you use `ValidationPipe` and `StandardSchemaValidationPipe` together?

Yes. Some teams move from `class-validator` to Zod one endpoint at a time. Both pipes can be global; `ValidationPipe` works on class DTOs and the standard schema pipe works on parameters with a `schema` option. Just make sure a single parameter is not validated twice in conflicting ways.

### 204: What are mapped types?

Helpers that build a new DTO class from an existing one, keeping the validation decorators.

- `PartialType(Dto)` - all fields optional.
- `PickType(Dto, ['a', 'b'])` - only some fields.
- `OmitType(Dto, ['password'])` - all fields except some.
- `IntersectionType(A, B)` - fields from both.

```ts
export class UpdateUserDto extends PartialType(
  OmitType(CreateUserDto, ["email"] as const),
) {}
```

### 205: How do you hide fields like `password` in responses?

Use `ClassSerializerInterceptor` with `class-transformer` decorators, and return class instances (not plain objects).

```ts
export class UserEntity {
  id: number;
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

### 206: What does `@SerializeOptions()` do?

It passes options to `ClassSerializerInterceptor` for a controller or route. With `type` you can return plain objects and still have them turned into a class before serializing.

```ts
@SerializeOptions({ type: UserEntity })
@Get(':id')
findOne(@Param('id') id: string) {
  return this.usersService.findOne(id); // plain object
}
```

In Nest 12 it also accepts a Standard Schema with `StandardSchemaSerializerInterceptor`:

```ts
@UseInterceptors(StandardSchemaSerializerInterceptor)
@SerializeOptions({ schema: userResponseSchema })
@Get(':id')
findOne(@Param('id') id: string) {}
```

### 207: How do you write an interceptor that wraps every response in `{ data: ... }`?

```ts
@Injectable()
export class WrapInterceptor<T> implements NestInterceptor<T, { data: T }> {
  intercept(
    context: ExecutionContext,
    next: CallHandler<T>,
  ): Observable<{ data: T }> {
    return next.handle().pipe(map((data) => ({ data })));
  }
}
```

### 208: How do you add a timeout to every request?

```ts
@Injectable()
export class TimeoutInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler) {
    return next.handle().pipe(
      timeout(5000),
      catchError((err) =>
        err instanceof TimeoutError
          ? throwError(() => new RequestTimeoutException())
          : throwError(() => err),
      ),
    );
  }
}
```

### 209: How can an interceptor return a response without calling the handler?

Return your own Observable and do not call `next.handle()`. This is how caching interceptors work.

```ts
intercept(context: ExecutionContext, next: CallHandler) {
  const cached = this.cache.get(key);
  if (cached) return of(cached);
  return next.handle().pipe(tap((value) => this.cache.set(key, value)));
}
```

### 210: How do you map database errors to HTTP errors in one place?

Use an interceptor with `catchError` or an exception filter.

```ts
return next.handle().pipe(
  catchError((err) => {
    if (err?.code === "23505") {
      return throwError(() => new ConflictException("Already exists"));
    }
    return throwError(() => err);
  }),
);
```

`23505` is the Postgres unique violation code.

### 211: How do you exclude routes from middleware?

```ts
consumer
  .apply(LoggerMiddleware)
  .exclude({ path: "health", method: RequestMethod.GET }, "auth/{*splat}")
  .forRoutes(CatsController);
```

### 212: Can middleware use dependency injection?

Yes, class-based middleware can inject providers from the module where it is registered.

```ts
@Injectable()
export class TenantMiddleware implements NestMiddleware {
  constructor(private tenants: TenantsService) {}

  async use(req: Request, res: Response, next: NextFunction) {
    req["tenant"] = await this.tenants.findByHost(req.hostname);
    next();
  }
}
```

### 213: When should you use middleware vs a guard vs an interceptor?

- Middleware: generic request work that does not need to know which handler will run (logging, body parsing, setting a request ID).
- Guard: allow or deny access. It knows the target handler and its metadata.
- Interceptor: wrap the handler to change input/output, add timing, caching or error mapping.

### 214: How do you use namespaced configuration with `registerAs`?

```ts
export default registerAs("database", () => ({
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT ?? "5432", 10),
}));
```

```ts
ConfigModule.forRoot({ load: [databaseConfig] });
```

```ts
constructor(
  @Inject(databaseConfig.KEY)
  private dbConfig: ConfigType<typeof databaseConfig>,
) {}
```

`ConfigType` gives you full typing of the returned object.

### 215: How do you validate environment variables at startup?

Pass a schema to `validationSchema`. In Nest 12 (`@nestjs/config` for v12) any Standard Schema works, so Zod is common:

```ts
ConfigModule.forRoot({
  validationSchema: z.object({
    NODE_ENV: z
      .enum(["development", "production", "test"])
      .default("development"),
    PORT: z.coerce.number().default(3000),
    DATABASE_URL: z.string(),
  }),
});
```

Joi still works too (v18 or newer is required). If validation fails, the app does not start.

### 216: What options does `ConfigModule.forRoot()` have that are useful in practice?

- `isGlobal` - no need to import it in every module.
- `envFilePath` - one path or a list, like `['.env.local', '.env']`.
- `ignoreEnvFile` - read only `process.env`, common in containers.
- `load` - custom config factories.
- `cache` - cache values read from `process.env`.
- `expandVariables` - allow `${VAR}` inside `.env` values.
- `validationSchema` / `validate` - check the values.

### 217: How do you add a typed `ConfigService`?

Pass a type for the whole config and `true` as the second generic to say that values are validated (so no `undefined`).

```ts
interface EnvVars {
  PORT: number;
  DATABASE_URL: string;
}

constructor(private config: ConfigService<EnvVars, true>) {}

const port = this.config.get('PORT', { infer: true }); // number
```

### 218: What changed in caching in Nest 11 and is still true in 12?

`@nestjs/cache-manager` moved to `cache-manager` v6, which uses Keyv stores. TTL values are in milliseconds, and you configure stores as Keyv instances.

```ts
CacheModule.registerAsync({
  isGlobal: true,
  useFactory: async () => ({
    stores: [
      new Keyv({ store: new CacheableMemory({ ttl: 60_000, lruSize: 5000 }) }),
      createKeyv("redis://localhost:6379"),
    ],
  }),
});
```

`createKeyv` comes from `@keyv/redis`. With several stores, reads go through them in order.

### 219: How do you use the cache manager directly?

```ts
@Injectable()
export class ProductsService {
  constructor(@Inject(CACHE_MANAGER) private cache: Cache) {}

  async getProduct(id: string) {
    const key = `product:${id}`;
    const cached = await this.cache.get<Product>(key);
    if (cached) return cached;

    const product = await this.repo.findOneBy({ id });
    await this.cache.set(key, product, 60_000);
    return product;
  }
}
```

`Cache` is imported from `cache-manager`.

### 220: How do you change the cache key or TTL for one route?

```ts
@Get()
@CacheKey('all-products')
@CacheTTL(30_000)
findAll() {}
```

To build keys from the request (for example per user), extend `CacheInterceptor` and override `trackBy()`.

### 221: Which requests does `CacheInterceptor` cache?

Only `GET` requests. Routes that use `@Res()` are not cached either, because the interceptor cannot see the response body.

### 222: How do you use several rate limits at once with the throttler?

Give each limit a name.

```ts
ThrottlerModule.forRoot([
  { name: "short", ttl: 1000, limit: 3 },
  { name: "long", ttl: 60_000, limit: 100 },
]);
```

Override them per route:

```ts
@Throttle({ short: { limit: 1, ttl: 1000 } })
@Post('login')
login() {}
```

### 223: How do you share rate limit counters across several app instances?

The throttler stores counters in memory by default, so each instance counts on its own. Use a shared storage, such as a Redis storage package for `@nestjs/throttler`, by passing it in the `storage` option.

### 224: How do you rate limit by user instead of IP?

Extend `ThrottlerGuard` and override `getTracker()`.

```ts
@Injectable()
export class UserThrottlerGuard extends ThrottlerGuard {
  protected async getTracker(req: Record<string, any>): Promise<string> {
    return req.user?.id ?? req.ip;
  }
}
```

### 225: What versioning types does Nest support?

- `VersioningType.URI` - `/v1/cats`.
- `VersioningType.HEADER` - version in a custom header you name.
- `VersioningType.MEDIA_TYPE` - in the `Accept` header, like `application/json;v=2`.
- `VersioningType.CUSTOM` - you provide an `extractor` function.

### 226: How do you serve two versions of the same route?

```ts
@Controller("cats")
export class CatsController {
  @Version("1")
  @Get()
  findAllV1() {}

  @Version("2")
  @Get()
  findAllV2() {}
}
```

You can also pass an array, `@Version(['1', '2'])`, or `VERSION_NEUTRAL` for a route that answers any version.

### 227: What is `defaultVersion` in versioning?

The version used for controllers and routes that do not declare one.

```ts
app.enableVersioning({
  type: VersioningType.URI,
  defaultVersion: "1",
});
```

### 228: What is `RouterModule`?

It lets you set path prefixes per module instead of per controller.

```ts
@Module({
  imports: [
    AdminModule,
    RouterModule.register([{ path: "admin", module: AdminModule }]),
  ],
})
export class AppModule {}
```

All controllers in `AdminModule` now live under `/admin`. Routes can be nested with `children`.

### 229: How do you document authentication and responses in Swagger?

```ts
@ApiTags("users")
@ApiBearerAuth()
@Controller("users")
export class UsersController {
  @Get(":id")
  @ApiOkResponse({ type: UserDto })
  @ApiNotFoundResponse({ description: "User not found" })
  findOne(@Param("id") id: string) {}
}
```

### 230: What does the Swagger CLI plugin do?

It reads your DTO and controller files at compile time and adds `@ApiProperty()` and response metadata for you. It can also turn JSDoc comments into descriptions. Enable it in `nest-cli.json`:

```json
{
  "compilerOptions": {
    "plugins": [
      { "name": "@nestjs/swagger", "options": { "introspectComments": true } }
    ]
  }
}
```

It only works when the build goes through the Nest CLI (or you set it up in your own build).

### 231: How do you validate uploaded files?

Use `ParseFilePipe` with validators, or `ParseFilePipeBuilder`.

```ts
@Post('avatar')
@UseInterceptors(FileInterceptor('file'))
upload(
  @UploadedFile(
    new ParseFilePipe({
      validators: [
        new MaxFileSizeValidator({ maxSize: 2 * 1024 * 1024 }),
        new FileTypeValidator({ fileType: /^image\/(png|jpeg)$/ }),
      ],
    }),
  )
  file: Express.Multer.File,
) {}
```

Recent versions of `FileTypeValidator` check the file's magic bytes, not just the header the client sent.

### 232: How do you send Server-Sent Events?

Use `@Sse()` and return an Observable of `MessageEvent`.

```ts
@Sse('events')
events(): Observable<MessageEvent> {
  return interval(1000).pipe(map((n) => ({ data: { tick: n } }) as MessageEvent));
}
```

The browser reads it with `new EventSource('/events')`.

### 233: How do you get the raw request body, for example for webhook signatures?

Enable `rawBody` and read `req.rawBody`.

```ts
const app = await NestFactory.create(AppModule, { rawBody: true });
```

```ts
@Post('webhook')
handle(@Req() req: RawBodyRequest<Request>) {
  const raw = req.rawBody; // Buffer
}
```

There is also a `@RawBody()` parameter decorator.

### 234: What changed about query string parsing with Express 5?

Express 5 uses the `simple` query parser by default, so nested query strings like `?filter[name]=tom` are not parsed into objects anymore. If you need that, switch back to the extended parser:

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.set("query parser", "extended");
```

### 235: How do you add body size limits?

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.useBodyParser("json", { limit: "5mb" });
```

In Nest 12 the parser type is inferred, so you do not pass a generic type argument to `useBodyParser` anymore.

### 236: How do you use BullMQ queues in Nest?

```bash
npm i @nestjs/bullmq bullmq
```

```ts
@Module({
  imports: [
    BullModule.forRoot({ connection: { host: "localhost", port: 6379 } }),
    BullModule.registerQueue({ name: "emails" }),
  ],
})
export class AppModule {}
```

```ts
@Injectable()
export class EmailsService {
  constructor(@InjectQueue("emails") private queue: Queue) {}

  sendWelcome(userId: string) {
    return this.queue.add("welcome", { userId }, { attempts: 3 });
  }
}
```

```ts
@Processor("emails")
export class EmailsProcessor extends WorkerHost {
  async process(job: Job) {
    if (job.name === "welcome") {
      // send the email
    }
  }
}
```

### 237: How do you add or remove cron jobs at runtime?

Use `SchedulerRegistry`.

```ts
@Injectable()
export class JobsService {
  constructor(private registry: SchedulerRegistry) {}

  addJob(name: string, cronTime: string) {
    const job = new CronJob(cronTime, () => console.log(`${name} ran`));
    this.registry.addCronJob(name, job);
    job.start();
  }

  removeJob(name: string) {
    this.registry.deleteCronJob(name);
  }
}
```

Name a decorated job with `@Cron('0 * * * *', { name: 'cleanup' })` to control it later with `getCronJob('cleanup')`.

### 238: What is a problem with `@Cron()` when you run several app instances?

Every instance runs the job, so the work happens several times. Fixes include a distributed lock (for example in Redis), running scheduled work in a single worker process, or using a queue with repeatable jobs (BullMQ) so only one worker picks each run.

### 239: How do you make event listeners async and catch their errors?

```ts
@OnEvent('order.created', { async: true, suppressErrors: false })
async handle(event: OrderCreatedEvent) {
  await this.mailer.send(event.email);
}
```

To wait for all listeners, use `await this.eventEmitter.emitAsync('order.created', event)`.

### 240: How do you send messages to a room with WebSocket gateways?

```ts
@WebSocketGateway({ cors: { origin: "*" } })
export class ChatGateway {
  @WebSocketServer()
  server: Server;

  @SubscribeMessage("join")
  join(@ConnectedSocket() client: Socket, @MessageBody() room: string) {
    client.join(room);
  }

  @SubscribeMessage("chat")
  chat(@MessageBody() data: { room: string; text: string }) {
    this.server.to(data.room).emit("chat", data.text);
  }
}
```

### 241: How do you handle connect and disconnect in a gateway?

Implement `OnGatewayConnection` and `OnGatewayDisconnect`. Since Nest 12, `handleDisconnect` also gets the disconnect reason.

```ts
@WebSocketGateway()
export class EventsGateway implements OnGatewayConnection, OnGatewayDisconnect {
  handleConnection(client: Socket) {
    console.log("connected", client.id);
  }

  handleDisconnect(client: Socket, reason?: string) {
    console.log("disconnected", client.id, reason);
  }
}
```

### 242: How do you authenticate WebSocket connections?

Check the token in `handleConnection` (or in middleware on the Socket.IO server) and disconnect if it is invalid. Guards also work on `@SubscribeMessage()` handlers, but they run per message, not on connect.

```ts
async handleConnection(client: Socket) {
  try {
    const token = client.handshake.auth?.token;
    client.data.user = await this.jwt.verifyAsync(token);
  } catch {
    client.disconnect();
  }
}
```

### 243: How do you throw errors in a gateway?

Throw `WsException`. The built-in filter sends an `exception` event to the client.

```ts
throw new WsException("Invalid room");
```

### 244: How do you send a message from one microservice to another?

Register a client and use `send()` for request-response or `emit()` for events.

```ts
@Module({
  imports: [
    ClientsModule.register([
      {
        name: "MATH_SERVICE",
        transport: Transport.TCP,
        options: { port: 3001 },
      },
    ]),
  ],
})
export class AppModule {}
```

```ts
@Injectable()
export class AppService {
  constructor(@Inject("MATH_SERVICE") private client: ClientProxy) {}

  sum(numbers: number[]) {
    return firstValueFrom(this.client.send<number>({ cmd: "sum" }, numbers));
  }

  notify() {
    this.client.emit("user_created", { id: 1 });
  }
}
```

### 245: How do you create a microservice listener?

```ts
const app = await NestFactory.createMicroservice<MicroserviceOptions>(
  AppModule,
  {
    transport: Transport.TCP,
    options: { port: 3001 },
  },
);
await app.listen();
```

```ts
@Controller()
export class MathController {
  @MessagePattern({ cmd: "sum" })
  sum(@Payload() data: number[]) {
    return data.reduce((a, b) => a + b, 0);
  }
}
```

### 246: Is `ClientProxy.send()` lazy?

Yes. `send()` returns a cold Observable, so nothing is sent until you subscribe (or call `firstValueFrom`). `emit()` sends right away, even if you do not subscribe.

### 247: How do you read transport-specific data in a handler?

Use `@Ctx()` to get the context object for the transport.

```ts
@MessagePattern('orders.created')
handle(@Payload() data: any, @Ctx() context: RmqContext) {
  const channel = context.getChannelRef();
  const message = context.getMessage();
  channel.ack(message);
}
```

Other contexts: `KafkaContext`, `NatsContext`, `RedisContext`, `MqttContext`, `TcpContext`.

### 248: How do you return errors from a microservice handler?

Throw `RpcException`. The client gets the error through the Observable.

```ts
throw new RpcException({ code: "NOT_FOUND", message: "Order not found" });
```

On the HTTP side, catch it and map it to an HTTP error if needed.

### 249: What is a hybrid application?

An HTTP app that also listens on one or more microservice transports.

```ts
const app = await NestFactory.create(AppModule);
app.connectMicroservice<MicroserviceOptions>(
  { transport: Transport.REDIS, options: { host: "localhost", port: 6379 } },
  { inheritAppConfig: true },
);
await app.startAllMicroservices();
await app.listen(3000);
```

`inheritAppConfig: true` applies global pipes, guards and filters to the microservice handlers too.

### 250: What changed about the NATS transport in Nest 12?

It moved to the NATS v3 client. You uninstall `nats` and install `@nats-io/transport-node`. `StringCodec` and `JSONCodec` are gone, `headers()` comes from `@nats-io/nats-core`, and custom deserializers receive the full message, so you read the payload with `msg.json()`.

### 251: How do you listen to the connection status of a microservice client?

Since Nest 11, clients and servers expose a `status` Observable.

```ts
this.client.status.subscribe((status) => {
  console.log("Client status:", status); // e.g. 'connected', 'disconnected'
});
```

You can also get the underlying library client with `this.client.unwrap()`.

### 252: What is the difference between code-first and schema-first in Nest GraphQL?

In code-first you write TypeScript classes with decorators and Nest generates the `.graphql` schema. In schema-first you write the SDL by hand and Nest can generate TypeScript types from it. Code-first keeps one source of truth in TypeScript; schema-first is nice when the schema is designed separately or shared with other teams.

### 253: How do you set up GraphQL with Apollo (code-first)?

```ts
GraphQLModule.forRoot<ApolloDriverConfig>({
  driver: ApolloDriver,
  autoSchemaFile: join(process.cwd(), "src/schema.gql"),
  sortSchema: true,
});
```

```ts
@ObjectType()
export class Author {
  @Field(() => Int)
  id: number;

  @Field()
  name: string;
}
```

### 254: What is `@ResolveField()`?

It resolves one field of a type, usually a relation, only when the client asks for it.

```ts
@Resolver(() => Author)
export class AuthorsResolver {
  @ResolveField(() => [Post])
  posts(@Parent() author: Author) {
    return this.postsService.findByAuthor(author.id);
  }
}
```

### 255: What is the N+1 problem in GraphQL and how do you fix it in Nest?

If a query returns 50 authors and each one resolves `posts` with its own database query, you run 1 + 50 queries. DataLoader fixes this by collecting all IDs requested in one tick and loading them with one query. In Nest you create a DataLoader per request (request-scoped provider or in the GraphQL context) so cached data does not leak between users.

### 256: How do you write a mutation with an input type?

```ts
@InputType()
export class CreatePostInput {
  @Field()
  @IsString()
  title: string;
}

@Mutation(() => Post)
createPost(@Args('input') input: CreatePostInput) {
  return this.postsService.create(input);
}
```

`ValidationPipe` works on GraphQL args too.

### 257: Which IDE does Nest GraphQL show by default now?

Since Nest 12, GraphiQL is the default. You configure it with a `graphiql` object.

```ts
GraphQLModule.forRoot<ApolloDriverConfig>({
  driver: ApolloDriver,
  autoSchemaFile: true,
  graphiql: {
    url: "/graphql",
    shouldPersistHeaders: true,
  },
});
```

### 258: How do you get the request in a GraphQL guard?

Convert the context first.

```ts
@Injectable()
export class GqlAuthGuard implements CanActivate {
  canActivate(context: ExecutionContext) {
    const ctx = GqlExecutionContext.create(context);
    const { req } = ctx.getContext();
    return Boolean(req.user);
  }
}
```

For Passport, extend `AuthGuard('jwt')` and override `getRequest()` in the same way.

### 259: How do you override a provider in a test without rewriting the module?

Use `overrideProvider()` before `compile()`.

```ts
const moduleRef = await Test.createTestingModule({
  imports: [AppModule],
})
  .overrideProvider(PaymentsService)
  .useValue({ charge: vi.fn().mockResolvedValue({ ok: true }) })
  .compile();
```

There are also `overrideGuard()`, `overrideInterceptor()`, `overridePipe()`, `overrideFilter()` and `overrideModule()`.

### 260: What does `useMocker()` do in testing?

It provides a fallback for any dependency you did not list, so you do not have to mock every one by hand.

```ts
const moduleRef = await Test.createTestingModule({
  controllers: [CatsController],
})
  .useMocker((token) => {
    if (token === CatsService) {
      return { findAll: vi.fn().mockResolvedValue([]) };
    }
  })
  .compile();
```

Libraries like `@golevelup/ts-jest` or `@golevelup/ts-vitest` give a `createMock()` that you can pass here.

### 261: How do you test a guard on its own?

Create the guard with fake dependencies and a fake `ExecutionContext`.

```ts
it("denies when user has no admin role", () => {
  const reflector = { getAllAndOverride: vi.fn().mockReturnValue(["admin"]) };
  const guard = new RolesGuard(reflector as any);
  const context = {
    getHandler: () => null,
    getClass: () => null,
    switchToHttp: () => ({ getRequest: () => ({ user: { roles: ["user"] } }) }),
  } as any;

  expect(guard.canActivate(context)).toBe(false);
});
```

### 262: How do you replace a global guard in e2e tests?

A guard registered with `APP_GUARD` and `useClass` is hard to override, because `overrideGuard()` does not reach it. The usual fix is to register it with `useExisting`, so the guard class is also a normal provider you can override:

```ts
providers: [
  { provide: APP_GUARD, useExisting: JwtAuthGuard },
  JwtAuthGuard,
],
```

```ts
.overrideProvider(JwtAuthGuard)
.useValue({ canActivate: () => true })
```

### 263: How do you test with a real database in e2e tests?

Run a throwaway database, for example with Docker or Testcontainers, point the config at it, run migrations before the tests and clean up after. Wrap each test in a transaction that you roll back, or truncate tables between tests, so tests do not affect each other.

### 264: Why does Jest fail with `ERR_REQUIRE_ASYNC_MODULE` on Nest 12?

Nest 12 packages are ESM. Jest (in CommonJS mode) loads them with `require()`, which only works for these packages on Node 24.9 or newer. On older Node, either upgrade Node or switch to Vitest, which handles ESM natively.

### 265: How do you set up Vitest for a Nest project?

Vitest's default transformer (esbuild) does not emit decorator metadata, so Nest DI would break. New Nest 12 ESM projects come configured with a transformer that supports decorators (OXC). For existing projects, a common setup is `unplugin-swc`:

```ts
// vitest.config.ts
import swc from "unplugin-swc";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: { globals: true, root: "./" },
  plugins: [swc.vite({ module: { type: "es6" } })],
});
```

### 266: What is `HttpAdapterHost` used for?

It gives you access to the underlying HTTP adapter (Express or Fastify) inside providers, for example in a global exception filter, without depending on a specific platform.

```ts
constructor(private adapterHost: HttpAdapterHost) {}

const instance = this.adapterHost.httpAdapter.getInstance();
```

### 267: How do you register Fastify plugins?

```ts
const app = await NestFactory.create<NestFastifyApplication>(
  AppModule,
  new FastifyAdapter(),
);
await app.register(fastifyCookie, { secret: "my-secret" });
await app.register(helmet);
```

Use the Fastify versions of plugins (`@fastify/cookie`, `@fastify/helmet`, `@fastify/multipart`) instead of Express middleware.

### 268: Does `FileInterceptor` work with Fastify?

No. `FileInterceptor` is built on `multer`, which is Express only. With Fastify you use `@fastify/multipart` and handle the file stream yourself, or use a community package that adds interceptors for it.

### 269: What is `@Res({ passthrough: true })` good for?

It lets you touch the native response (set cookies or headers) while Nest still sends the return value. Interceptors and `@HttpCode()` keep working.

### 270: How do you implement a transaction with TypeORM in a service?

```ts
@Injectable()
export class TransfersService {
  constructor(private dataSource: DataSource) {}

  async transfer(fromId: number, toId: number, amount: number) {
    await this.dataSource.transaction(async (manager) => {
      await manager.decrement(Account, { id: fromId }, "balance", amount);
      await manager.increment(Account, { id: toId }, "balance", amount);
    });
  }
}
```

If anything inside throws, the whole transaction is rolled back. All queries must go through `manager`, not the injected repositories.

### 271: How do you run TypeORM migrations in a Nest project?

Create a separate `DataSource` file for the TypeORM CLI, using the same settings as the app.

```ts
// data-source.ts
export default new DataSource({
  type: "postgres",
  url: process.env.DATABASE_URL,
  entities: ["dist/**/*.entity.js"],
  migrations: ["dist/migrations/*.js"],
});
```

```bash
npx typeorm migration:generate -d dist/data-source.js src/migrations/AddUsers
npx typeorm migration:run -d dist/data-source.js
```

You can also set `migrationsRun: true` in the module config, but running them as a separate deploy step is safer.

### 272: How do you connect to two databases with TypeORM?

Give each connection a name and use it in `forFeature()` and `@InjectRepository()`.

```ts
TypeOrmModule.forRoot({ name: 'analytics', type: 'postgres', url: '...' });
TypeOrmModule.forFeature([Event], 'analytics');

constructor(@InjectRepository(Event, 'analytics') private events: Repository<Event>) {}
```

### 273: How do you add Mongoose middleware (hooks) in Nest?

Use `forFeatureAsync` and add hooks in the factory.

```ts
MongooseModule.forFeatureAsync([
  {
    name: User.name,
    useFactory: () => {
      const schema = UserSchema;
      schema.pre("save", async function () {
        if (this.isModified("password")) {
          this.password = await hash(this.password, 10);
        }
      });
      return schema;
    },
  },
]);
```

### 274: How do you handle the Prisma client shutdown?

Implement `OnModuleDestroy` (or rely on `enableShutdownHooks()` and `onApplicationShutdown`).

```ts
@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  async onModuleInit() {
    await this.$connect();
  }
  async onModuleDestroy() {
    await this.$disconnect();
  }
}
```

### 275: How do you write a health check in Terminus for Nest 12?

The old `HealthIndicator` base class and `HealthCheckError` were removed. Use `HealthIndicatorService`.

```ts
@Injectable()
export class RedisHealthIndicator {
  constructor(
    private readonly redis: RedisService,
    private readonly healthIndicatorService: HealthIndicatorService,
  ) {}

  async isHealthy(key: string) {
    const indicator = this.healthIndicatorService.check(key);
    try {
      await this.redis.ping();
      return indicator.up();
    } catch (e) {
      return indicator.down({ message: (e as Error).message });
    }
  }
}
```

For simple checks there is a shorter form: `.check(key).attempt(() => this.redis.ping()).withTimeout(1000)`.

### 276: How does graceful shutdown work in a Nest app?

Call `app.enableShutdownHooks()`. When the process gets `SIGTERM`, Nest runs `onModuleDestroy`, then `beforeApplicationShutdown`, closes the HTTP server, then runs `onApplicationShutdown`. In Nest 12 the Express adapter also waits for in-flight requests to finish before closing. Use these hooks to stop consumers, flush logs and close database connections.

### 277: What does `bufferLogs` do?

It holds startup logs until you attach a custom logger, so the very first log lines also go through it.

```ts
const app = await NestFactory.create(AppModule, { bufferLogs: true });
app.useLogger(app.get(MyLogger));
```

### 278: How do you write a custom logger?

Implement `LoggerService`, or extend `ConsoleLogger` to change only parts.

```ts
@Injectable()
export class MyLogger extends ConsoleLogger {
  error(message: any, ...rest: any[]) {
    // send to an error tracker
    super.error(message, ...rest);
  }
}
```

Register it with `app.useLogger(app.get(MyLogger))`. Many teams use `nestjs-pino` instead of writing their own.

### 279: How do you use `ConsoleLogger` options from Nest 11 and up?

```ts
new ConsoleLogger({
  json: true, // JSON lines
  colors: false, // turn off colors
  prefix: "Orders", // instead of "Nest"
  compact: true,
  timestamp: true,
});
```

### 280: How do you add a request ID to every log line?

Generate an ID in middleware (or read `x-request-id`), store it in `AsyncLocalStorage`, and have your logger read it. `nestjs-cls` and `nestjs-pino` both make this easy. Return the ID in a response header so clients can report it.

### 281: What is `nestjs-cls` and why is it popular?

It wraps Node's `AsyncLocalStorage` so you can store request data (user, tenant, request ID, transaction) and read it anywhere in the same async call chain, without request-scoped providers. Services stay singletons, which is faster.

```ts
ClsModule.forRoot({ global: true, middleware: { mount: true } });

@Injectable()
export class AuditService {
  constructor(private cls: ClsService) {}
  userId() {
    return this.cls.get("userId");
  }
}
```

### 282: What is CQRS in NestJS?

Command Query Responsibility Segregation splits writes (commands) from reads (queries). `@nestjs/cqrs` gives you `CommandBus`, `QueryBus`, `EventBus`, handlers and sagas.

```ts
export class CreateOrderCommand extends Command<{ id: string }> {
  constructor(public readonly items: string[]) {
    super();
  }
}

@CommandHandler(CreateOrderCommand)
export class CreateOrderHandler implements ICommandHandler<CreateOrderCommand> {
  async execute(command: CreateOrderCommand) {
    return { id: "order-1" };
  }
}

const result = await this.commandBus.execute(new CreateOrderCommand(["a"]));
```

Since `@nestjs/cqrs` v11, extending `Command<T>` makes `execute()` return the right type.

### 283: What is a saga in `@nestjs/cqrs`?

A saga listens to events and returns new commands, so you can chain steps without the services knowing about each other.

```ts
@Injectable()
export class OrderSagas {
  @Saga()
  orderCreated = (events$: Observable<any>): Observable<ICommand> =>
    events$.pipe(
      ofType(OrderCreatedEvent),
      map((event) => new ReserveStockCommand(event.orderId)),
    );
}
```

### 284: How do you use a different config per environment?

Load several env files in order, so more specific files win.

```ts
ConfigModule.forRoot({
  envFilePath: [
    `.env.${process.env.NODE_ENV}.local`,
    `.env.${process.env.NODE_ENV}`,
    ".env",
  ],
});
```

In production, rely on real environment variables and set `ignoreEnvFile: true`.

### 285: How do you build an app where a guard needs a request-scoped service?

Guards are created once per scope of their dependencies. If you inject a request-scoped service into a guard, the guard becomes request-scoped too. It works, but costs a new guard per request. Often it is simpler to read what you need from the request (or from CLS) in a singleton guard.

### 286: How do you load a module only in some environments?

Build the `imports` list conditionally, or use `ConditionalModule` from `@nestjs/config`.

```ts
@Module({
  imports: [ConditionalModule.registerWhen(DevToolsModule, "ENABLE_DEVTOOLS")],
})
export class AppModule {}
```

The module is loaded only when the env variable is truthy (or when your callback returns true).

### 287: What does `nest start --debug` do?

It starts the app with the Node inspector enabled, so you can attach a debugger from VS Code or Chrome. Combine with `--watch` for development.

### 288: How do you pass a custom header version and default for missing headers?

```ts
app.enableVersioning({
  type: VersioningType.HEADER,
  header: "X-API-Version",
  defaultVersion: "1",
});
```

Requests without the header use version 1.

### 289: How do you prevent CSRF in a cookie-based Nest app?

Use a CSRF package that works with your platform, such as `csrf-csrf` for Express or `@fastify/csrf-protection` for Fastify, and set cookies with `SameSite=Lax` or `Strict`. If your API only uses bearer tokens in headers (not cookies), CSRF is not a concern for those routes.

### 290: How do you set up compression?

With Express:

```ts
import compression from "compression";
app.use(compression());
```

With Fastify use `@fastify/compress`. In production, a reverse proxy like Nginx often does compression instead, which is cheaper for the Node process.

### 291: How do you set `trust proxy` in Nest?

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
app.set("trust proxy", 1);
```

Needed behind a load balancer so `req.ip`, `req.protocol` and secure cookies work correctly. For Fastify, pass `{ trustProxy: true }` to `new FastifyAdapter()`.

### 292: How do you check which routes exist in an app?

Nest logs each mapped route on startup (`Mapped {/cats, GET} route`). For more detail, enable `snapshot: true` and use Nest Devtools, or inspect the router of the HTTP adapter. In Nest 12 you can also turn on route conflict diagnostics to warn about duplicate or shadowed routes.

### 293: What is the route specificity option in Nest 12?

By default routes are matched in the order they are registered, so `@Get(':id')` declared before `@Get('me')` would swallow `/me`. With `routeResolutionStrategy: 'specificity'`, static segments win over params no matter the order.

```ts
const app = await NestFactory.create(AppModule, {
  routeResolutionStrategy: "specificity",
  routeConflictPolicy: { duplicate: "error", shadow: "warn" },
});
```

### 294: How do you return a custom status code from an exception filter in GraphQL?

GraphQL usually returns 200 with an `errors` array, so HTTP status codes do not apply in the same way. Implement `GqlExceptionFilter` and return an error (for example `GraphQLError` with `extensions.code`) instead of writing to a response.

```ts
@Catch(HttpException)
export class GqlHttpFilter implements GqlExceptionFilter {
  catch(exception: HttpException) {
    return new GraphQLError(exception.message, {
      extensions: { code: exception.getStatus() },
    });
  }
}
```

### 295: How do you inject config into a dynamic module with `registerAsync` using a class?

Use `useClass` (or `useExisting`) with a class that implements the options factory.

```ts
@Injectable()
export class MailConfig implements ConfigurableModuleOptionsFactory<
  MailModuleOptions,
  "create"
> {
  constructor(private config: ConfigService) {}
  create(): MailModuleOptions {
    return { apiKey: this.config.getOrThrow("MAIL_API_KEY") };
  }
}

MailModule.registerAsync({ useClass: MailConfig });
```

### 296: Can you inject a provider into a module class?

Yes. Module classes can have constructors that inject providers, for example to run setup code. But a module class itself cannot be injected into providers, and injecting into modules can cause circular dependency issues, so keep it simple.

### 297: How do you test a request-scoped provider?

Create a context ID and use `resolve()`.

```ts
const contextId = ContextIdFactory.create();
vi.spyOn(ContextIdFactory, "getByRequest").mockImplementation(() => contextId);

const service = await moduleRef.resolve(RequestScopedService, contextId);
```

Spying on `getByRequest` makes the app use the same context, so instances created during an e2e request match the one you resolved.

### 298: What does `abortOnError: false` do?

By default, if the app fails during startup (for example a missing dependency), Nest prints the error and calls `process.exit(1)`. With `abortOnError: false`, it throws the error instead, so you can catch it, for example in tests.

```ts
await NestFactory.create(AppModule, { abortOnError: false });
```

### 299: How do you run code once after the app starts listening?

Use `onApplicationBootstrap()` for work before listening. For work after `listen()` resolves, put it right after `await app.listen()` in `main.ts`, or listen to `HttpAdapterHost.listen$` which emits once the server is listening.

### 300: How do you stop a long query when the client disconnects?

In Express, listen to `req.on('close')` and cancel the work, for example with an `AbortController` passed to your database or HTTP client.

```ts
@Get('report')
async report(@Req() req: Request) {
  const controller = new AbortController();
  req.on('close', () => controller.abort());
  return this.reports.generate({ signal: controller.signal });
}
```

## Advanced Questions (301-450)

### 301: What happens inside Nest when you call `NestFactory.create()`?

Roughly:

1. The scanner walks the module tree from the root module, reading `@Module()` metadata, and registers each module, provider, controller and injectable in the `NestContainer`.
2. The instance loader creates the instances. The injector reads constructor metadata (`design:paramtypes` and `@Inject()` tokens), resolves dependencies recursively and caches the instances in each module's wrapper map.
3. The router explorer reads route metadata from controllers and registers routes on the HTTP adapter, wrapping each handler with the guards, interceptors, pipes and filters that apply to it.
4. `onModuleInit` and `onApplicationBootstrap` hooks run.

`listen()` then starts the server.

### 302: How does Nest use `reflect-metadata`?

Decorators store data on classes and methods with `Reflect.defineMetadata()`. TypeScript, with `emitDecoratorMetadata`, adds `design:paramtypes` (constructor parameter types), `design:type` and `design:returntype`. Nest reads `design:paramtypes` to find constructor dependencies, and reads its own keys (like route paths, guards, `self:paramtypes` for `@Inject()` overrides) when building the app.

### 303: Why can `import type` break dependency injection?

`import type { UsersService } from './users.service'` is erased at compile time, so TypeScript has no runtime value to emit in `design:paramtypes`. It writes `Object` instead, and Nest cannot resolve the dependency. The same happens with `isolatedModules` setups where the compiler cannot tell if an import is a type. Always import injectable classes as values. Linters with "consistent-type-imports" rules can cause this by converting imports automatically.

### 304: Why does a circular file import (not a DI cycle) produce `undefined` dependencies?

If `a.ts` imports `b.ts` and `b.ts` imports `a.ts`, one of them is still undefined when the other's class is decorated, so `design:paramtypes` contains `undefined`. Nest reports "can't resolve dependencies ... at index [0]" with `undefined`. `forwardRef()` delays the lookup until both are loaded. Barrel files (`index.ts` exporting everything) are a common hidden cause. SWC is stricter here than `tsc`, so cycles that worked with `tsc` may fail under SWC.

### 305: How does Nest decide the instance identity of a dynamic module?

Nest builds a token for each module from the class and its dynamic metadata. Two imports of the same dynamic module with the same options share one instance. In Nest 11 this was changed to use the object reference of the dynamic module instead of hashing its serialized options, which made startup faster. As a result, if you call `MyModule.forRoot(opts)` twice in two places, you get two separate module instances. Store the result in a constant and import that constant if you want one shared instance.

### 306: What are durable providers?

Request-scoped providers that are shared between requests with the same key (for example the same tenant), instead of being created for every request. You enable them with `durable: true` and a `ContextIdStrategy` that maps requests to sub-trees.

```ts
@Injectable({ scope: Scope.REQUEST, durable: true })
export class TenantDbService {
  constructor(@Inject(REQUEST) private payload: { tenantId: string }) {}
}
```

When `durable` is set, `REQUEST` holds the payload from the strategy, not the actual request.

### 307: How do you write a `ContextIdStrategy` for multi-tenancy?

```ts
const tenants = new Map<string, ContextId>();

export class AggregateByTenantContextIdStrategy implements ContextIdStrategy {
  attach(contextId: ContextId, request: Request) {
    const tenantId = request.headers["x-tenant-id"] as string;
    let tenantSubTreeId = tenants.get(tenantId);
    if (!tenantSubTreeId) {
      tenantSubTreeId = ContextIdFactory.create();
      tenants.set(tenantId, tenantSubTreeId);
    }
    return {
      resolve: (info: HostComponentInfo) =>
        info.isTreeDurable ? tenantSubTreeId : contextId,
      payload: { tenantId },
    };
  }
}
```

```ts
// main.ts
ContextIdFactory.apply(new AggregateByTenantContextIdStrategy());
```

Be careful with the map: an unknown tenant ID from a header can grow it forever. Validate tenant IDs first.

### 308: What are the main ways to build multi-tenant apps in Nest?

- Shared database with a `tenantId` column: filter every query by tenant, often through a repository wrapper or ORM global filters, with the tenant read from CLS.
- Schema per tenant: switch the Postgres `search_path` or connection per request.
- Database per tenant: keep a pool of connections keyed by tenant, created lazily, often with durable providers.

The hard parts are making sure no query forgets the tenant filter, and closing idle tenant connections.

### 309: How does `AsyncLocalStorage` compare to request-scoped providers?

Request scope creates new provider instances per request and bubbles up the graph, which costs CPU and makes some things (cron jobs, event handlers) awkward. `AsyncLocalStorage` keeps singletons and stores per-request data in the async context, so it is cheaper and works anywhere in the call chain. The risk is losing the context through code that breaks async tracking (some old callback libraries or connection pools), and that the dependency on request data is hidden instead of declared.

### 310: What is the `DiscoveryService` and how do you build a custom decorator with it?

`DiscoveryService` (from `@nestjs/core`, via `DiscoveryModule`) lets you list all providers and controllers and find those with certain metadata. This is how you build things like "run every method marked with `@OnJob()`".

```ts
export const OnJob = DiscoveryService.createDecorator<string>();

@Injectable()
export class JobExplorer implements OnModuleInit {
  constructor(
    private discovery: DiscoveryService,
    private scanner: MetadataScanner,
    private reflector: Reflector,
  ) {}

  onModuleInit() {
    for (const wrapper of this.discovery.getProviders()) {
      const { instance } = wrapper;
      if (!instance || !Object.getPrototypeOf(instance)) continue;
      for (const method of this.scanner.getAllMethodNames(
        Object.getPrototypeOf(instance),
      )) {
        const jobName = this.reflector.get(OnJob, instance[method]);
        if (jobName) this.register(jobName, instance[method].bind(instance));
      }
    }
  }
}
```

If the decorator is applied to classes, `this.discovery.getProviders({ metadataKey: OnJob.KEY })` filters them for you.

### 311: Why should explorers skip non-static wrappers?

Request-scoped and transient providers do not have a single instance at startup, so `wrapper.instance` may be a prototype-only placeholder or undefined. Calling methods on it can fail or act on the wrong object. Check `wrapper.isDependencyTreeStatic()` (or skip non-default scopes) before using the instance.

### 312: How do you lazy load a module?

Use `LazyModuleLoader`. The module is loaded the first time you need it, which can cut cold start time in serverless functions.

```ts
@Injectable()
export class ReportsService {
  constructor(private lazyModuleLoader: LazyModuleLoader) {}

  async generate() {
    const { PdfModule } = await import("./pdf/pdf.module");
    const moduleRef = await this.lazyModuleLoader.load(() => PdfModule);
    const pdf = moduleRef.get(PdfService);
    return pdf.render();
  }
}
```

Lazy-loaded modules cannot register controllers, resolvers or gateways, and lifecycle hooks are not called for lazy-loaded modules and their providers.

### 313: How do you reduce cold start time for Nest on serverless?

- Cache the created app between invocations (create it once outside the handler).
- Use Fastify and avoid heavy modules you do not need.
- Lazy load rarely used modules.
- Bundle the app (Rspack or another bundler) so fewer files are read at startup.
- Avoid `synchronize` and other slow startup checks.
- Use `snapshot`/Devtools to see what gets created at startup.

On AWS Lambda with CommonJS and Nest 12, set `NODE_OPTIONS=--experimental-require-module` so the ESM packages can load.

### 314: How do you run Nest on AWS Lambda?

```ts
import serverlessExpress from "@codegenie/serverless-express";

let server: Handler;

async function bootstrap(): Promise<Handler> {
  const app = await NestFactory.create(AppModule);
  await app.init();
  const expressApp = app.getHttpAdapter().getInstance();
  return serverlessExpress({ app: expressApp });
}

export const handler: Handler = async (event, context, callback) => {
  server = server ?? (await bootstrap());
  return server(event, context, callback);
};
```

Keeping `server` in module scope reuses the app across warm invocations.

### 315: How do you write a custom transport strategy?

Extend `Server` and implement `CustomTransportStrategy`. `listen()` connects to your broker and calls handlers, `close()` cleans up. In Nest 11+ you also implement `on()` for status events and `unwrap()` to expose the native client.

```ts
export class SqsServer extends Server implements CustomTransportStrategy {
  async listen(callback: () => void) {
    this.consumer = createConsumer(async (msg) => {
      const handler = this.messageHandlers.get(msg.pattern);
      if (!handler) return;
      const result$ = this.transformToObservable(
        await handler(msg.data, new BaseRpcContext([msg])),
      );
      await lastValueFrom(result$);
    });
    callback();
  }

  async close() {
    await this.consumer?.stop();
  }

  on() {
    throw new Error("Not supported");
  }

  unwrap<T>(): T {
    return this.consumer as T;
  }
}
```

```ts
NestFactory.createMicroservice(AppModule, { strategy: new SqsServer() });
```

For the client side, extend `ClientProxy` and implement `connect`, `close`, `publish` and `dispatchEvent`.

### 316: How does gRPC work in Nest?

You define services in `.proto` files, and Nest maps RPC methods to handlers with `@GrpcMethod()`.

```ts
NestFactory.createMicroservice<MicroserviceOptions>(AppModule, {
  transport: Transport.GRPC,
  options: {
    package: "hero",
    protoPath: join(__dirname, "hero/hero.proto"),
    url: "0.0.0.0:5000",
  },
});
```

```ts
@Controller()
export class HeroesController {
  @GrpcMethod("HeroesService", "FindOne")
  findOne(data: { id: number }, metadata: Metadata) {
    return { id: data.id, name: "John" };
  }
}
```

On the client, use `ClientGrpc.getService<HeroesService>('HeroesService')`.

### 317: How do you handle streaming in gRPC with Nest?

Use `@GrpcStreamMethod()` for streams handled as Observables, or `@GrpcStreamCall()` for raw duplex streams.

```ts
@GrpcStreamMethod('HeroesService', 'FindMany')
findMany(data$: Observable<HeroById>): Observable<Hero> {
  const subject = new Subject<Hero>();
  data$.subscribe({
    next: (hero) => subject.next({ id: hero.id, name: 'Hero' }),
    complete: () => subject.complete(),
  });
  return subject.asObservable();
}
```

### 318: How do you return proper gRPC status codes for errors?

Throw `RpcException` with a `code` from `@grpc/grpc-js` `status`. In Nest 12 you can also use the built-in `GrpcExceptionFilter`, which maps exceptions to the right gRPC status codes so you do not have to write that mapping yourself.

```ts
throw new RpcException({ code: status.NOT_FOUND, message: "Hero not found" });
```

### 319: What should you know about Kafka in Nest?

- Each Nest Kafka server joins a consumer group (`consumer.groupId`). Instances in the same group split partitions; Nest appends `-server`/`-client` suffixes unless you set `postfixId`.
- Request-response over Kafka needs reply topics (`<topic>.reply`), which adds latency and partition assignment issues. Events (`emit`) fit Kafka better.
- Use `KafkaContext` to read the partition, offset and headers.
- Message order is only kept within a partition, so use a key (for example the order ID) for related messages.
- Since Nest 12, `@MessagePattern()` and `@EventPattern()` accept a `RegExp` to subscribe to several topics.
- Handlers should be idempotent, because Kafka delivers at least once.

### 320: How do you commit Kafka offsets manually?

Set `run: { autoCommit: false }` and commit after processing.

```ts
@EventPattern('orders')
async handle(@Payload() data: any, @Ctx() context: KafkaContext) {
  await this.process(data);
  const { offset } = context.getMessage();
  const partition = context.getPartition();
  const topic = context.getTopic();
  await context.getConsumer().commitOffsets([
    { topic, partition, offset: (Number(offset) + 1).toString() },
  ]);
}
```

### 321: How do you make RabbitMQ consumers reliable?

Set `noAck: false` and ack only after the work succeeds. Set `prefetchCount` to limit how many messages one consumer holds. Use durable queues (`queueOptions: { durable: true }`) and a dead-letter exchange for messages that keep failing. On failure, `nack` the message (with or without requeue) instead of letting it hang.

```ts
@EventPattern('invoice.created')
async handle(@Payload() data: any, @Ctx() ctx: RmqContext) {
  const channel = ctx.getChannelRef();
  const msg = ctx.getMessage();
  try {
    await this.invoices.process(data);
    channel.ack(msg);
  } catch {
    channel.nack(msg, false, false); // send to DLX
  }
}
```

### 322: What is the outbox pattern and how would you do it in Nest?

The problem: you save an order and publish `order.created`. If the publish fails after the commit, or the commit fails after the publish, the database and the message bus disagree. With an outbox, you write the event into an `outbox` table in the same transaction as the order. A separate worker (a cron job, BullMQ repeatable job, or CDC tool like Debezium) reads unsent rows, publishes them with a `ClientProxy`, and marks them sent. Consumers must be idempotent because a row can be sent twice.

### 323: How do you make a consumer idempotent?

Store a processed-message key (message ID or business key) in a table with a unique constraint, inside the same transaction as the side effect. If inserting the key fails with a duplicate error, skip the message. For HTTP endpoints, the same idea works with an `Idempotency-Key` header and a stored response.

### 324: How would you implement an idempotency key interceptor for POST requests?

```ts
@Injectable()
export class IdempotencyInterceptor implements NestInterceptor {
  constructor(@Inject(CACHE_MANAGER) private cache: Cache) {}

  async intercept(context: ExecutionContext, next: CallHandler) {
    const req = context.switchToHttp().getRequest();
    const key = req.headers["idempotency-key"];
    if (!key) return next.handle();

    const cacheKey = `idem:${req.user?.id}:${key}`;
    const stored = await this.cache.get(cacheKey);
    if (stored) return of(stored);

    return next
      .handle()
      .pipe(tap((body) => this.cache.set(cacheKey, body, 24 * 60 * 60 * 1000)));
  }
}
```

A production version also stores an "in progress" marker (with a lock) so two parallel requests with the same key do not both run.

### 325: How do microservice exception filters differ from HTTP ones?

They return an Observable instead of writing a response.

```ts
@Catch(RpcException)
export class RpcFilter implements RpcExceptionFilter<RpcException> {
  catch(exception: RpcException): Observable<any> {
    return throwError(() => exception.getError());
  }
}
```

Note that `useGlobalFilters()` on a hybrid app does not apply to microservices unless you use `inheritAppConfig: true`.

### 326: How do you scale WebSocket gateways across several instances?

Each instance only knows its own connections. Use the Redis adapter for Socket.IO so broadcasts reach all instances.

```ts
export class RedisIoAdapter extends IoAdapter {
  private adapterConstructor: ReturnType<typeof createAdapter>;

  async connectToRedis() {
    const pub = createClient({ url: "redis://localhost:6379" });
    const sub = pub.duplicate();
    await Promise.all([pub.connect(), sub.connect()]);
    this.adapterConstructor = createAdapter(pub, sub);
  }

  createIOServer(port: number, options?: ServerOptions) {
    const server = super.createIOServer(port, options);
    server.adapter(this.adapterConstructor);
    return server;
  }
}
```

```ts
const adapter = new RedisIoAdapter(app);
await adapter.connectToRedis();
app.useWebSocketAdapter(adapter);
```

The load balancer also needs sticky sessions if clients use long-polling.

### 327: What changed for request-scoped WebSocket gateways in Nest 12?

Before 12, gateways had to be singletons, so you could not inject request-scoped providers into them. Nest 12 allows request-scoped gateways, and you can inject the socket through the `REQUEST` token. Keep in mind that a "request" here is tied to the socket events, and per-message instance creation has a cost on busy sockets.

### 328: How do you do GraphQL subscriptions in Nest 12?

`subscriptions-transport-ws` was removed. Use `graphql-ws`.

```ts
GraphQLModule.forRoot<ApolloDriverConfig>({
  driver: ApolloDriver,
  autoSchemaFile: true,
  subscriptions: { "graphql-ws": true },
});
```

```ts
const pubSub = new PubSub();

@Subscription(() => Comment)
commentAdded() {
  return pubSub.asyncIterableIterator('commentAdded');
}

@Mutation(() => Comment)
async addComment(@Args('input') input: CommentInput) {
  const comment = await this.comments.create(input);
  await pubSub.publish('commentAdded', { commentAdded: comment });
  return comment;
}
```

The in-memory `PubSub` only works with one instance. Use a Redis-based PubSub in production.

### 329: How do you protect a GraphQL API from expensive queries?

- Limit query depth and complexity (for example with a complexity plugin and `@Field({ complexity: 5 })`).
- Use DataLoader so nested lists do not explode into N+1 queries.
- Paginate list fields and cap `first`/`limit` values.
- Disable introspection in production if the API is not public.
- Use persisted queries for known clients.
- Rate limit by user, not just by request count.

### 330: What is GraphQL federation and how does Nest support it?

Federation splits one GraphQL graph into several subgraphs owned by different services, and a gateway (or router) combines them. In Nest, each subgraph uses `ApolloFederationDriver` and marks types with `@Directive('@key(fields: "id")')` and `@ResolveReference()`. The gateway uses `ApolloGatewayDriver` or an external router like Apollo Router.

```ts
@ObjectType()
@Directive('@key(fields: "id")')
export class User {
  @Field(() => ID)
  id: string;
}

@Resolver(() => User)
export class UsersResolver {
  @ResolveReference()
  resolveReference(ref: { __typename: string; id: string }) {
    return this.users.findById(ref.id);
  }
}
```

### 331: How do you build a request-scoped DataLoader without making everything request-scoped?

Create the loaders in the GraphQL `context` factory, so each request gets new loaders while resolvers stay singletons.

```ts
GraphQLModule.forRootAsync<ApolloDriverConfig>({
  driver: ApolloDriver,
  imports: [PostsModule],
  inject: [PostsService],
  useFactory: (posts: PostsService) => ({
    autoSchemaFile: true,
    context: ({ req }) => ({
      req,
      loaders: {
        postsByAuthor: new DataLoader((ids: readonly number[]) =>
          posts.findByAuthorIds(ids),
        ),
      },
    }),
  }),
});
```

```ts
@ResolveField(() => [Post])
posts(@Parent() author: Author, @Context('loaders') loaders) {
  return loaders.postsByAuthor.load(author.id);
}
```

### 332: What are the practical steps to move a Nest app to ESM?

1. Add `"type": "module"` to `package.json`.
2. In `tsconfig.json` set `"module": "nodenext"` and `"moduleResolution": "nodenext"` (add `"resolvePackageJsonExports": true` on older setups).
3. Add `.js` to relative imports: `import { AppModule } from './app.module.js'`.
4. Replace `__dirname` with `import.meta.dirname`.
5. Use `createRequire(import.meta.url)` where you still need `require()`.
6. Move tests to Vitest (or set up Jest in ESM mode).
7. Watch for libraries that are CommonJS only and check their default import behavior.

This is optional in Nest 12. CommonJS apps keep working.

### 333: How can a CommonJS app use ESM-only Nest 12 packages?

Node.js supports `require()` of ES modules (from 20.19 and 22.12). So your compiled CommonJS code can still `require('@nestjs/core')`. The limit is that the required ESM module must not use top-level `await`; if it does, Node throws `ERR_REQUIRE_ASYNC_MODULE`. That is also why some tooling (like older Jest setups) has trouble.

### 334: What are the risks with ESM and decorators metadata order?

ESM imports are hoisted and evaluated in dependency order, and cycles behave differently than in CommonJS. A class referenced in a decorator (like `@Type(() => Address)` or `forwardRef`) may not be initialized yet. Always use arrow functions for type references in decorators so the lookup happens later, and avoid circular file imports, especially through barrel files.

### 335: Why might the Swagger CLI plugin not work with TypeScript 7?

The Nest CLI plugins (Swagger, GraphQL) use the TypeScript compiler API to transform code. TypeScript 7 (the Go-based compiler) does not provide that programmatic API in the same way. You can type check with TypeScript 7, but builds that rely on CLI plugins still need the JavaScript-based TypeScript (Nest 12 uses TypeScript 6 by default).

### 336: How do you build a reusable Nest library for other teams?

- Put it in a monorepo library or its own package.
- Expose a dynamic module made with `ConfigurableModuleBuilder` (`forRoot`/`forRootAsync`).
- List `@nestjs/common` and `@nestjs/core` as `peerDependencies`, not `dependencies`, so the app and the library share one copy.
- Export only the public providers and types.
- Use symbols for tokens and export them.
- Ship type declarations and test it against the Nest versions you support.

### 337: Why must `@nestjs/*` be peer dependencies in libraries?

If a library has its own copy of `@nestjs/common` or `@nestjs/core`, then classes like `Reflector`, `ModuleRef` or `HttpException` are different objects from the ones in the app. DI lookups by class token fail, `instanceof HttpException` returns false, and you get errors like "Nest can't resolve dependencies of ... (Reflector)".

### 338: How do you use `setExtras` in `ConfigurableModuleBuilder`?

To add options that change the module definition rather than being passed to providers, like `isGlobal`.

```ts
export const { ConfigurableModuleClass, MODULE_OPTIONS_TOKEN } =
  new ConfigurableModuleBuilder<MailOptions>()
    .setExtras({ isGlobal: false }, (definition, extras) => ({
      ...definition,
      global: extras.isGlobal,
    }))
    .build();
```

```ts
MailModule.register({ apiKey: "x", isGlobal: true });
```

Extras are not included in the object injected with `MODULE_OPTIONS_TOKEN`.

### 339: How do you extend the generated `register` method with extra providers?

Override the static method and call `super`.

```ts
@Module({})
export class MailModule extends ConfigurableModuleClass {
  static register(options: typeof OPTIONS_TYPE): DynamicModule {
    const base = super.register(options);
    return {
      ...base,
      providers: [...(base.providers ?? []), MailService, TemplateRenderer],
      exports: [MailService],
    };
  }
}
```

### 340: What does the `strict` option do in `app.get()` and `moduleRef.get()`?

It controls where Nest looks for the provider. On `moduleRef.get()`, `strict: true` (the default) looks only in the current module, while `strict: false` searches the whole graph. On `app.get()` the default is to search all modules, and `strict: true` limits it to the module you selected (for example with `app.select()`).

```ts
const tasks = app.select(TasksModule).get(TasksService, { strict: true });
const anyLogger = this.moduleRef.get(LoggerService, { strict: false });
```

Strict lookups avoid getting the wrong instance when two modules provide the same token.

### 341: What does `app.select()` do?

It returns a `ModuleRef`-like context for one module, so you can get providers from that module specifically.

```ts
const tasks = app.select(TasksModule).get(TasksService, { strict: true });
```

Useful when the same class is provided in several modules with different configs.

### 342: What is Nest Devtools and what does `snapshot: true` do?

With `snapshot: true` Nest records the full dependency graph, routes and class metadata, and the `DevtoolsModule` (from `@nestjs/devtools-integration`) serves it to the Devtools web UI. You can browse the module graph, find why a dependency failed, see route entry points and test-run handlers. Only enable it in development.

```ts
const app = await NestFactory.create(AppModule, { snapshot: true });
```

### 343: What is `preview` mode?

`NestFactory.create(AppModule, { snapshot: true, preview: true })` builds the dependency graph without creating any instances (no constructors or lifecycle hooks run). It is used with Devtools in CI to check the graph quickly without connecting to databases.

### 344: How do you debug "Nest can't resolve dependencies" errors fast?

Read the error carefully: it names the class, the argument index and the module. Then check:

1. Is the dependency in the `providers` of that module, or exported by an imported module?
2. Is it imported as a type only (`import type`)?
3. Is there a circular file import making it `undefined`?
4. Is a module imported in `providers` by mistake (or a provider in `imports`)?
5. Are there two versions of `@nestjs/*` installed (`npm ls @nestjs/core`)?
6. Is it a custom token that needs `@Inject()`?

### 345: What changed with `@Optional()` and inheritance in Nest 12?

`@Optional()` is not inherited anymore. If a subclass has no constructor of its own, the parent's optional markers do not apply, and a missing dependency throws `UnknownDependenciesException` where v11 returned `undefined`. Fix it by declaring the constructor in the subclass:

```ts
@Injectable()
class Child extends Base {
  constructor(@Optional() options?: Options) {
    super(options);
  }
}
```

### 346: What changed about lifecycle hook order in Nest 12?

Hooks like `onModuleInit` and the shutdown hooks now run by the component's level in the module hierarchy, not just by module registration order. Deeper modules (dependencies) run first on init. If your code relied on one module's hook running before another's in a specific order, test it again after upgrading. Better still, do not depend on hook order across modules; make the dependency explicit by injecting the provider and awaiting a method on it.

### 347: How does inheritance work with Nest decorators?

Class-level metadata (like `@Controller()` path) and method decorators are inherited through the prototype chain, so a base controller's routes show up in subclasses. Constructor injection metadata is read from the class itself; if a subclass has no constructor, TypeScript does not emit `design:paramtypes` for it and Nest falls back to the parent's. Property-level and parameter decorators can behave in surprising ways with overrides, so it is safer to redeclare constructors in subclasses.

### 348: How do you build a generic CRUD controller with inheritance?

Use a mixin function that returns a class, because decorators need concrete types at runtime.

```ts
export function CrudController<T, C, U>(
  createDto: Type<C>,
  updateDto: Type<U>,
) {
  @Controller()
  abstract class BaseController {
    constructor(protected readonly service: CrudService<T, C, U>) {}

    @Get()
    findAll() {
      return this.service.findAll();
    }

    @Post()
    create(@Body(new ValidationPipe({ expectedType: createDto })) dto: C) {
      return this.service.create(dto);
    }
  }
  return BaseController;
}

@Controller("cats")
export class CatsController extends CrudController(CreateCatDto, UpdateCatDto) {
  constructor(service: CatsService) {
    super(service);
  }
}
```

`expectedType` is needed because the generic `C` becomes `Object` at runtime.

### 349: How do you write a mixin interceptor that takes options and still uses DI?

```ts
export function CacheFor(ttl: number): Type<NestInterceptor> {
  @Injectable()
  class MixinInterceptor implements NestInterceptor {
    constructor(@Inject(CACHE_MANAGER) private cache: Cache) {}

    async intercept(context: ExecutionContext, next: CallHandler) {
      // use ttl and this.cache
      return next.handle();
    }
  }
  return mixin(MixinInterceptor);
}

@UseInterceptors(CacheFor(30_000))
```

`mixin()` gives each generated class a unique name so Nest treats them as different injectables.

### 350: Why does passing an instance vs a class to `@UseGuards()` matter?

`@UseGuards(AuthGuard)` passes the class. Nest creates it with DI and can reuse the instance. `@UseGuards(new AuthGuard())` passes an instance you created, so Nest cannot inject anything into it. Prefer classes unless the guard needs constructor arguments you build by hand.

### 351: How does Nest create pipes, guards and interceptors that are passed as classes?

They are "injectables" that are created in the context of the module that owns the controller. Nest registers them as part of that module, so they can inject anything visible in that module. If they depend on request-scoped providers, a new instance is created per request.

### 352: How would you implement soft multi-version deprecation in an API?

Use versioning to serve both versions, and add headers to old versions so clients know they should move.

```ts
@Injectable()
export class DeprecationInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler) {
    const res = context.switchToHttp().getResponse();
    res.setHeader("Deprecation", "true");
    res.setHeader("Sunset", "Wed, 31 Dec 2026 23:59:59 GMT");
    return next.handle();
  }
}

@Controller({ path: "orders", version: "1" })
@UseInterceptors(DeprecationInterceptor)
export class OrdersV1Controller {}
```

Track usage per version in your metrics before removing the old one.

### 353: How do you implement field-level authorization (for example with CASL)?

Build an ability per user in a factory, check it in a guard for the action, and filter fields in the service or serializer.

```ts
@Injectable()
export class CaslAbilityFactory {
  createForUser(user: User) {
    const { can, cannot, build } = new AbilityBuilder(createMongoAbility);
    if (user.isAdmin) {
      can("manage", "all");
    } else {
      can("read", "Article");
      can("update", "Article", { authorId: user.id });
      cannot("update", "Article", ["published"]);
    }
    return build();
  }
}
```

The guard checks the action (`can('update', 'Article')`), and the service checks the loaded entity (`ability.can('update', article)`), because conditions like `authorId` need the actual row.

### 354: What security issues should a Nest API watch for beyond auth?

- Mass assignment: use `whitelist` and separate DTOs from entities.
- Prototype pollution: avoid merging untrusted objects; Express 5's simple query parser helps.
- SSRF: validate URLs before your server fetches them.
- Injection: always use parameterized queries in raw SQL.
- Big payloads: set body size limits and file size limits.
- Leaking errors: do not send stack traces or database errors to clients.
- Insecure direct object references: check that the user owns the resource, not just that they are logged in.
- Rate limits on login, signup and password reset.

### 355: How would you stop users from reading other users' data in a REST API?

Never trust IDs from the URL alone. Scope queries by the current user (`where: { id, ownerId: user.id }`), or load the resource and check ownership in a guard or policy. Return 404 instead of 403 if you do not want to reveal that the resource exists. Write e2e tests that try to access another user's resource.

### 356: How do you store secrets safely in a Nest app?

Do not commit `.env` files with real secrets. Load secrets from the environment or a secret manager (AWS Secrets Manager, Vault, GCP Secret Manager) at startup with an async config factory. Validate them with the config schema, and avoid logging the whole config object. Rotate secrets and support two keys during rotation for things like JWT signing.

### 357: How do you load secrets from a secret manager before modules start?

Use an async factory in `ConfigModule.forRoot({ load: [...] })` or a `forRootAsync` that fetches the values.

```ts
export default registerAs("secrets", async () => {
  const client = new SecretsManagerClient({});
  const res = await client.send(
    new GetSecretValueCommand({ SecretId: "prod/api" }),
  );
  return JSON.parse(res.SecretString ?? "{}");
});
```

Because async factories are awaited during startup, modules that inject this config get the resolved values.

### 358: How do you handle very large file uploads without loading them into memory?

Do not use multer memory storage. Stream the upload directly to storage (for example S3 multipart upload) using `busboy` (Express) or `@fastify/multipart` streams, with limits on size and count. Even better, have the client upload directly to S3 using a pre-signed URL from your API, so the file never passes through the Nest process.

### 359: How do you stream a large response, like a CSV export, without high memory use?

Stream rows from the database with a cursor and pipe them through a transform into the response, respecting backpressure.

```ts
@Get('export')
async export(): Promise<StreamableFile> {
  const rows = this.repo.createQueryBuilder('o').stream(); // Readable
  const csv = rows.pipe(new CsvTransform());
  return new StreamableFile(csv, {
    type: 'text/csv',
    disposition: 'attachment; filename="orders.csv"',
  });
}
```

Avoid building the whole file as a string or loading all rows with `find()`.

### 360: How do you find and fix a memory leak in a Nest app?

Watch memory over time. Take heap snapshots (`--inspect` and Chrome DevTools, or `node --heapsnapshot-signal`) at intervals and compare what grows. Common causes in Nest apps: caches without limits (maps keyed by user or tenant), event listeners added per request, request-scoped objects kept in singletons, RxJS subscriptions never unsubscribed, and timers not cleared on shutdown.

### 361: How do you use all CPU cores with Nest?

Node runs your JavaScript on one thread. Run several processes: Node `cluster`, PM2 in cluster mode, or (most common) several containers behind a load balancer. Make the app stateless (sessions, caches, rate limits and WebSocket state in Redis) so any instance can serve any request. For CPU-heavy tasks, use worker threads or a separate worker service with a queue.

### 362: When would you use worker threads in a Nest app?

When a request needs heavy CPU work (image processing, PDF generation, big JSON parsing, crypto) that would block the event loop and slow down every other request. Move the work into a worker pool (for example `piscina`) wrapped in a provider, so the main thread stays free for I/O.

### 363: How do you measure event loop blocking?

Use `perf_hooks.monitorEventLoopDelay()` and export the percentiles as metrics. Spikes in event loop delay mean something is blocking. Then profile with `--cpu-prof` or clinic.js to find the code. Common causes are sync crypto, `JSON.stringify` on huge objects, regex backtracking and sync file system calls.

### 364: How do you add OpenTelemetry tracing to a Nest app?

Start the OpenTelemetry SDK before Nest is imported, so auto-instrumentations can patch `http`, Express/Fastify, database drivers and so on.

```ts
// tracing.ts, loaded first
const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({ url: process.env.OTLP_URL }),
  instrumentations: [getNodeAutoInstrumentations(), new NestInstrumentation()],
});
sdk.start();
```

```bash
node --import ./dist/tracing.js dist/main.js
```

Put trace IDs in logs so you can jump from a log line to its trace. Nest 12 also has an `instrument` option on `NestFactory.create()` that the `@nestjs/observe` SDK hooks into.

### 365: How do you expose Prometheus metrics?

Use `prom-client` (or a wrapper like `@willsoto/nestjs-prometheus`), register counters and histograms as providers, and record request duration in an interceptor or middleware. Expose `/metrics` on a separate port or protect it, so it is not public. Label metrics by route pattern (`/users/:id`), not raw URL, to avoid too many label values.

### 366: How do you set up liveness and readiness probes properly?

- Liveness: is the process healthy? Keep it cheap and do not check dependencies, or a database outage will restart every pod.
- Readiness: can it serve traffic now? Check the database and other critical dependencies.
- On shutdown, fail readiness first, then wait a few seconds before closing so the load balancer stops sending traffic.

With Terminus, make two endpoints with different checks.

### 367: Why might requests fail during deploys even with graceful shutdown?

The load balancer may keep sending traffic for a few seconds after `SIGTERM`. If the app closes the server right away, those requests fail. Also keep-alive connections can stay open. Fixes: delay shutdown a little after `SIGTERM` (or use a preStop hook), mark readiness as failing, let in-flight requests finish (Nest 12 does this for Express), and set server keep-alive timeouts lower than the load balancer's.

### 368: How do you share a database transaction across several services without passing the manager everywhere?

Store the transaction (entity manager or Prisma transaction client) in `AsyncLocalStorage` and have repositories read it from there. `nestjs-cls` has a transactional plugin (`@nestjs-cls/transactional`) with adapters for TypeORM, Prisma, Knex and others.

```ts
@Injectable()
export class OrdersService {
  constructor(private txHost: TransactionHost<TransactionalAdapterPrisma>) {}

  @Transactional()
  async placeOrder(dto: PlaceOrderDto) {
    const order = await this.txHost.tx.order.create({ data: dto });
    await this.stock.reserve(order.id); // uses the same transaction
    return order;
  }
}
```

### 369: What problems come with distributed transactions across microservices?

You cannot hold a database transaction across services. Instead you use sagas: a series of local transactions, each publishing an event, with compensating actions to undo earlier steps if a later one fails. You must handle retries, timeouts, duplicate messages and partial failure. Orchestrated sagas (one coordinator) are easier to follow; choreographed sagas (services react to events) have less coupling but are harder to trace.

### 370: How do you implement event sourcing with `@nestjs/cqrs`?

Use `AggregateRoot`. Methods apply events, event handlers inside the aggregate change state, and you save the events (not the state).

```ts
export class Account extends AggregateRoot {
  balance = 0;

  deposit(amount: number) {
    this.apply(new MoneyDeposited(this.id, amount));
  }

  onMoneyDeposited(event: MoneyDeposited) {
    this.balance += event.amount;
  }
}
```

To rebuild, load past events and call `account.loadFromHistory(events)`. After saving new events, call `account.commit()` so they go to the `EventBus` (merge the object with `EventPublisher.mergeObjectContext()`). Nest does not provide an event store; you pick one or build it on a database table.

### 371: How do you test code that uses `ConfigService` without `.env` files?

Pass values directly.

```ts
const moduleRef = await Test.createTestingModule({
  imports: [
    ConfigModule.forRoot({
      ignoreEnvFile: true,
      load: [() => ({ JWT_SECRET: "test", PORT: 0 })],
    }),
  ],
  providers: [AuthService],
}).compile();
```

Or override `ConfigService` with a `useValue` that has a `get` function.

### 372: How do you write integration tests with Testcontainers?

Start the container before the test module, then pass its connection info to the app.

```ts
let container: StartedPostgreSqlContainer;
let app: INestApplication;

beforeAll(async () => {
  container = await new PostgreSqlContainer("postgres:17").start();
  process.env.DATABASE_URL = container.getConnectionUri();

  const moduleRef = await Test.createTestingModule({
    imports: [AppModule],
  }).compile();
  app = moduleRef.createNestApplication();
  await app.init();
  await app.get(DataSource).runMigrations();
}, 60_000);

afterAll(async () => {
  await app.close();
  await container.stop();
});
```

### 373: How do you test an interceptor that uses RxJS?

Call `intercept()` with a fake `CallHandler` and check the Observable.

```ts
it("wraps the response", async () => {
  const interceptor = new WrapInterceptor();
  const next = { handle: () => of({ id: 1 }) };
  const result = await lastValueFrom(interceptor.intercept({} as any, next));
  expect(result).toEqual({ data: { id: 1 } });
});
```

### 374: How do you test a microservice handler end to end?

Create the microservice with the real transport (for example in a Testcontainers Redis or NATS), connect a `ClientProxy` in the test, and send messages.

```ts
const moduleRef = await Test.createTestingModule({
  imports: [AppModule],
}).compile();
const app = moduleRef.createNestMicroservice<MicroserviceOptions>({
  transport: Transport.TCP,
  options: { port: 4001 },
});
await app.listen();

const client = ClientProxyFactory.create({
  transport: Transport.TCP,
  options: { port: 4001 },
});
await client.connect();
const result = await firstValueFrom(client.send({ cmd: "sum" }, [1, 2]));
expect(result).toBe(3);
```

### 375: How do you mock an ES module dependency in Vitest?

Use `vi.mock()` at the top of the test file. Vitest hoists it above the imports.

```ts
vi.mock("./mailer.js", () => ({
  sendMail: vi.fn().mockResolvedValue(true),
}));

import { sendMail } from "./mailer.js";
```

In Nest code, prefer injecting a provider and overriding it in the testing module; module mocking is for code outside DI.

### 376: Why can `useDefineForClassFields` break Nest code?

When TypeScript targets ES2022 or newer, `useDefineForClassFields` defaults to `true`. Class fields are then defined with `Object.defineProperty` after the parent constructor runs, so a field declared without a value (like `name: string;` in a DTO or `@Inject() private service: X;`) is reset to `undefined`. This can break property injection and some `class-transformer` setups. Fixes: declare such fields with `declare` or `!`, avoid property injection, or set `useDefineForClassFields: false` in `tsconfig.json`. Check this when you move the target to a newer ES version.

### 377: What is property-based injection and when is it used?

Instead of the constructor, you mark a property with `@Inject()`.

```ts
@Injectable()
export class BaseService {
  @Inject(LoggerService)
  protected readonly logger: LoggerService;
}
```

It is mostly used in base classes, so subclasses do not have to pass dependencies through `super()`. The downside is that the dependency is not visible in the constructor, is not available inside the constructor, and is harder to set in tests. Prefer constructor injection.

### 378: What is `IntrinsicException`?

Added in Nest 11, it is a base class for exceptions that the framework should not log automatically. Normally, the built-in filter logs non-HTTP errors. If you throw something that extends `IntrinsicException`, Nest treats it as expected and does not log it. Useful for control-flow errors that a filter handles.

### 379: How do you catch errors that happen outside the request cycle?

Exception filters only cover errors in handlers (HTTP, RPC, WS). Errors in cron jobs, event listeners, queue processors, timers or un-awaited promises are not caught by them. Wrap those in try/catch and log them, add `process.on('unhandledRejection')` and `process.on('uncaughtException')` handlers that log and exit, and use your error tracker's Node integration. For `@OnEvent` listeners, set `suppressErrors: false` only if the emitter awaits them, otherwise the error just becomes an unhandled rejection.

### 380: Why is a fire-and-forget promise inside a handler dangerous?

```ts
@Post()
create(@Body() dto: CreateOrderDto) {
  this.mailer.sendConfirmation(dto.email); // not awaited
  return this.orders.create(dto);
}
```

If `sendConfirmation` rejects, nothing catches it; on recent Node versions an unhandled rejection crashes the process. It also escapes request context (and transactions), and is lost if the process stops. Either await it, catch it explicitly, or move it to a queue.

### 381: How do you use the stricter pipe types in Nest 12?

`PipeTransform<TInput, TOutput>` and the generic `ArgumentMetadata` let you type what a pipe accepts and returns, and the compiler checks pipes used with parameters more strictly. When upgrading, custom pipes that used `any` everywhere may need explicit types.

```ts
@Injectable()
export class ParseSlugPipe implements PipeTransform<string, string> {
  transform(value: string, metadata: ArgumentMetadata): string {
    if (!/^[a-z0-9-]+$/.test(value)) {
      throw new BadRequestException(`Invalid ${metadata.data}`);
    }
    return value;
  }
}
```

### 382: How would you write your own pipe that validates a Standard Schema?

The Standard Schema spec gives every library the same `~standard.validate()` method, so one pipe works with Zod, Valibot or ArkType.

```ts
import type { StandardSchemaV1 } from '@standard-schema/spec';

@Injectable()
export class SchemaPipe<T extends StandardSchemaV1> implements PipeTransform {
  constructor(private readonly schema: T) {}

  async transform(value: unknown): Promise<StandardSchemaV1.InferOutput<T>> {
    const result = await this.schema['~standard'].validate(value);
    if (result.issues) {
      throw new BadRequestException(result.issues.map((i) => i.message));
    }
    return result.value;
  }
}

@Post()
create(@Body(new SchemaPipe(createUserSchema)) dto: CreateUserDto) {}
```

In Nest 12 you usually do not need this because of the built-in `schema` option and `StandardSchemaValidationPipe`, but it shows how they work.

### 383: How do you read the `schema` attached to a parameter inside your own pipe in Nest 12?

The `schema` option only stores metadata; a pipe reads it and does the validation. The built-in `StandardSchemaValidationPipe` does exactly this. If you need custom behavior (like logging or a special error shape) you can extend that pipe or use its `exceptionFactory`, instead of reading the metadata yourself. This keeps you on the public API and safe across upgrades.

### 384: What is the cost of `class-validator` + `class-transformer` per request?

For every validated parameter, `class-transformer` builds a class instance from the plain object (walking nested objects), and `class-validator` runs every decorator. On big or deeply nested payloads, or high request rates, this adds noticeable CPU. Ways to reduce it: keep DTOs flat, avoid `transform` where you do not need it, use schema libraries that compile validators, or use Fastify's built-in JSON schema validation for hot endpoints.

### 385: How can Fastify make JSON responses faster?

Fastify can serialize responses with `fast-json-stringify` when you give it a response schema, which is much faster than `JSON.stringify` and also drops fields not in the schema. In Nest you can attach route-level Fastify config, or for very hot routes use the Fastify instance directly. In most apps the bigger wins are in the database and caching, so measure first.

### 386: How do you tune a Nest app for high throughput?

- Use Fastify if the HTTP layer shows up in profiles.
- Keep providers singleton; avoid request scope on hot paths.
- Turn off things you do not need per request (heavy logging, deep serialization).
- Cache reads, and use connection pooling sized for your database.
- Avoid sync work on the event loop.
- Run several processes or containers.
- Measure with a load tool (autocannon, k6) and profile before and after each change.

### 387: How do you prevent cache stampede?

When a hot key expires, many requests miss at the same time and all hit the database. Fixes:

- Lock on miss: one request rebuilds the value, others wait or get the stale value.
- Stale-while-revalidate: keep serving the old value while one worker refreshes it.
- Add random jitter to TTLs so many keys do not expire together.
- Pre-warm important keys before they expire.

Keyv-based `cache-manager` v6 supports refresh thresholds for background refresh.

### 388: How do you invalidate cache entries reliably?

Delete or update the cache in the same place that changes the data, after the database commit succeeds. Use clear key naming (`user:123`, `user:123:orders`) so you know what to delete. For lists, use version keys (store `users:version` and include it in list keys, bump it on writes) instead of trying to find every affected key. Keep TTLs as a safety net in case an invalidation is missed.

### 389: How do you use ETags or conditional requests in Nest?

Express already adds weak ETags to responses and answers `304 Not Modified` when `If-None-Match` matches, for responses it sends itself. For stronger control, compute an ETag from the resource version (`updatedAt` or a version column) in an interceptor, compare it to `If-None-Match`, and return 304 early. For updates, require `If-Match` and return `412 Precondition Failed` when the version changed, which gives you optimistic concurrency over HTTP.

### 390: How do you implement optimistic locking with TypeORM?

Add a `@VersionColumn()` and check it on update.

```ts
@Entity()
export class Product {
  @PrimaryGeneratedColumn()
  id: number;

  @VersionColumn()
  version: number;
}
```

```ts
const result = await this.repo.update(
  { id, version: dto.version },
  { price: dto.price, version: () => "version + 1" },
);
if (result.affected === 0) {
  throw new ConflictException("Product was changed by someone else");
}
```

### 391: How do you implement cursor pagination?

Return items after a cursor (usually an encoded sort key + ID) instead of using offset, which gets slow and skips or repeats rows when data changes.

```ts
async list(limit: number, cursor?: string) {
  const qb = this.repo.createQueryBuilder('p').orderBy('p.createdAt', 'DESC').addOrderBy('p.id', 'DESC').take(limit + 1);
  if (cursor) {
    const { createdAt, id } = JSON.parse(Buffer.from(cursor, 'base64url').toString());
    qb.where('(p.createdAt, p.id) < (:createdAt, :id)', { createdAt, id });
  }
  const rows = await qb.getMany();
  const hasMore = rows.length > limit;
  const items = rows.slice(0, limit);
  const last = items.at(-1);
  return {
    items,
    nextCursor: hasMore && last
      ? Buffer.from(JSON.stringify({ createdAt: last.createdAt, id: last.id })).toString('base64url')
      : null,
  };
}
```

### 392: How do you add soft delete globally?

TypeORM has `@DeleteDateColumn()`, and `softDelete()`/`restore()`; normal `find` calls skip soft-deleted rows. With Prisma you can use a client extension that turns deletes into updates and adds `deletedAt: null` to reads. Remember unique constraints: a soft-deleted row still holds its unique email unless you use a partial unique index (`WHERE deleted_at IS NULL`).

### 393: How do you add audit logs for every change?

Options:

- ORM subscribers (`EntitySubscriberInterface` in TypeORM) that write an audit row on insert, update and remove. Read the user from CLS.
- An interceptor on mutating routes that records who called what. This is simpler but does not see changes made outside HTTP.
- Database triggers or CDC, which catch everything but do not know the app user unless you pass it in a session variable.

For compliance needs, store audit rows in the same transaction as the change.

### 394: How do you use read replicas with TypeORM in Nest?

Configure replication in the data source. TypeORM sends writes to the master and reads to slaves by default for `find` queries.

```ts
TypeOrmModule.forRoot({
  type: "postgres",
  replication: {
    master: { url: process.env.DB_PRIMARY_URL },
    slaves: [{ url: process.env.DB_REPLICA_URL }],
  },
});
```

Watch out for replication lag: right after a write, reading from a replica may return old data. Read your own writes from the master when it matters (for example by using a query runner on `'master'`).

### 395: How do you choose the database pool size for a Nest app?

Total connections = pool size x number of app instances (and workers). It must stay below the database limit, leaving room for migrations and admin tools. Bigger is not better: too many connections cause contention in the database. Start with a small pool (around 10), measure wait time for connections and query latency, and use a pooler like PgBouncer if you run many instances or serverless functions.

### 396: How do you set query timeouts to protect the app?

Set a statement timeout at the database level (Postgres `statement_timeout`, passed in connection options) and a timeout in your ORM or driver. Combine with an HTTP timeout interceptor so slow requests return an error instead of hanging. Without timeouts, one slow query pattern can use up the pool and take down every endpoint.

### 397: How do you call another HTTP service with retries and a circuit breaker?

Retry only safe (idempotent) calls with backoff, and stop calling a failing service for a while with a circuit breaker (for example `opossum`).

```ts
@Injectable()
export class PricingClient {
  private breaker: CircuitBreaker;

  constructor(private http: HttpService) {
    this.breaker = new CircuitBreaker((sku: string) => this.fetchPrice(sku), {
      timeout: 2000,
      errorThresholdPercentage: 50,
      resetTimeout: 10_000,
    });
    this.breaker.fallback(() => null);
  }

  private fetchPrice(sku: string) {
    return firstValueFrom(
      this.http
        .get(`/prices/${sku}`)
        .pipe(
          retry({ count: 2, delay: (_, attempt) => timer(200 * 2 ** attempt) }),
        ),
    );
  }

  getPrice(sku: string) {
    return this.breaker.fire(sku);
  }
}
```

### 398: How do you set a timeout on `ClientProxy.send()`?

Add the RxJS `timeout` operator; otherwise a missing reply can hang forever.

```ts
const result = await firstValueFrom(
  this.client.send({ cmd: "get_user" }, id).pipe(timeout(3000)),
);
```

### 399: How would you build an API gateway or BFF with Nest?

A Nest app that receives client requests, checks auth once, and calls internal services with `ClientProxy` or HTTP. It combines results for the client (BFF = backend for frontend). Keep it thin: no business logic, only routing, auth, aggregation, rate limiting and caching. Use timeouts, circuit breakers and partial responses so one slow service does not break the whole page. For GraphQL, federation with a router is often a better fit.

### 400: How do you migrate an existing Express app to Nest step by step?

Nest runs on Express, so you can mount the old app inside Nest and move routes one by one.

```ts
const app = await NestFactory.create<NestExpressApplication>(AppModule);
await app.init();
const expressInstance = app.getHttpAdapter().getInstance();
expressInstance.use(legacyRouter); // old routes still work
await app.listen(3000);
```

Move one feature at a time into Nest modules, add tests around it, and delete the old route when the new one is live. Shared things (auth, DB connection) can be wrapped in providers so old and new code use the same instances.

### 401: How would you organize a large Nest codebase?

Group by feature (domain), not by type. Each feature module has its controllers, services, DTOs and entities, and exports only what other features may use. Shared technical code (config, logging, database) lives in core or shared modules. In a monorepo, put shared code in libraries and enforce boundaries with lint rules (Nx module boundaries or dependency-cruiser) so features do not reach into each other's internals.

### 402: How do you apply hexagonal (ports and adapters) architecture in Nest?

Define ports as abstract classes in the domain layer, implement them as adapters in infrastructure, and bind them in modules.

```ts
// domain
export abstract class OrderRepository {
  abstract save(order: Order): Promise<void>;
  abstract findById(id: string): Promise<Order | null>;
}

// infrastructure
@Injectable()
export class PrismaOrderRepository implements OrderRepository {
  constructor(private prisma: PrismaService) {}
  async save(order: Order) {}
  async findById(id: string) {
    return null;
  }
}

// module
@Module({
  providers: [
    PlaceOrderUseCase,
    { provide: OrderRepository, useClass: PrismaOrderRepository },
  ],
})
export class OrdersModule {}
```

The use case depends only on `OrderRepository`, so you can test it with an in-memory version and change the database without touching domain code. Keep Nest decorators out of the domain classes if you want them fully framework-free.

### 403: What is a sign that a Nest module has become a "god module"?

It imports most other modules, exports a lot of unrelated providers, has services with many constructor parameters, and most changes touch it. Often it was used to dodge circular dependencies. Fix it by splitting by business capability, moving shared logic into small focused modules, and using events for cross-feature reactions instead of direct calls.

### 404: How do you decouple features with domain events?

Instead of `OrdersService` calling `EmailService`, `LoyaltyService` and `AnalyticsService`, it publishes `OrderPlaced`. Each feature listens and reacts. In-process you can use `@nestjs/event-emitter` or the CQRS `EventBus`. If reactions must survive a crash, write the event to an outbox and process it with a queue. The trade-off: flows are harder to follow, so log and trace events.

### 405: How do you design a plugin system for a Nest app?

Define a plugin interface and a decorator, let plugins be normal providers in their own modules, and find them at startup with `DiscoveryService`.

```ts
export const Plugin = DiscoveryService.createDecorator<{ name: string }>();

@Plugin({ name: "slack" })
@Injectable()
export class SlackNotifier implements Notifier {
  send(msg: string) {}
}

@Injectable()
export class NotifierRegistry implements OnModuleInit {
  private notifiers = new Map<string, Notifier>();
  constructor(private discovery: DiscoveryService) {}

  onModuleInit() {
    for (const w of this.discovery.getProviders({ metadataKey: Plugin.KEY })) {
      const meta = this.discovery.getMetadataByDecorator(Plugin, w);
      this.notifiers.set(meta!.name, w.instance);
    }
  }
}
```

Plugin modules are added through a dynamic `PluginsModule.register([...])` call so the host app chooses which to load.

### 406: Can you add providers to the DI container after the app has started?

Not in a supported way. The container is built at bootstrap. For runtime needs, you can lazy load whole modules with `LazyModuleLoader`, create class instances with `moduleRef.create()`, or keep a registry provider (a `Map`) that you fill at runtime. For per-tenant connections, use a factory service that creates and caches them on demand.

### 407: How do you create a custom handler type that still runs guards and interceptors?

`ExternalContextCreator` from `@nestjs/core` wraps a method with the same pipes, guards and interceptors pipeline that Nest uses for controllers. Libraries use it for things like custom message consumers.

```ts
const handler = this.externalContextCreator.create(
  instance,
  instance[methodName],
  methodName,
  undefined,
  undefined,
  undefined,
  undefined,
  undefined,
  "custom-type",
);
await handler(payload);
```

It is an internal-ish API; check the signature in the version you use, and keep the usage in one place.

### 408: What is the Nest REPL?

A built-in REPL that boots your app context and lets you call providers from the terminal, handy for debugging and one-off admin tasks.

```ts
// src/repl.ts
import { repl } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  await repl(AppModule);
}
bootstrap();
```

```bash
npm run start -- --entryFile repl
> await get(UsersService).findAll()
```

### 409: How do you build a command line tool with Nest?

Use a standalone app context, or a library like `nest-commander` that maps commands to classes with DI.

```ts
@Command({ name: "seed", description: "Seed the database" })
export class SeedCommand extends CommandRunner {
  constructor(private seeder: SeederService) {
    super();
  }
  async run() {
    await this.seeder.run();
  }
}

await CommandFactory.run(AppModule);
```

### 410: How do you run BullMQ processors with concurrency and rate limits?

```ts
@Processor("emails", {
  concurrency: 10,
  limiter: { max: 100, duration: 1000 },
})
export class EmailsProcessor extends WorkerHost {
  async process(job: Job) {}
}
```

Concurrency is per worker process; total throughput is concurrency x number of processes. The limiter is global across workers because it is stored in Redis.

### 411: How do you handle retries and failed jobs in BullMQ?

Set `attempts` and `backoff` when adding jobs, and listen for failures.

```ts
await this.queue.add("charge", data, {
  attempts: 5,
  backoff: { type: "exponential", delay: 1000 },
  removeOnComplete: 1000,
  removeOnFail: 5000,
});
```

```ts
@Processor("payments")
export class PaymentsProcessor extends WorkerHost {
  async process(job: Job) {}

  @OnWorkerEvent("failed")
  onFailed(job: Job, err: Error) {
    if (job.attemptsMade >= (job.opts.attempts ?? 1)) {
      // alert or move to a manual review list
    }
  }
}
```

Throw `UnrecoverableError` for errors that should not be retried.

### 412: Why should CPU-heavy BullMQ jobs use sandboxed processors?

A heavy job running in the main process blocks the event loop, which delays other jobs and HTTP requests in the same process, and can make BullMQ lose job locks (the job gets marked stalled and runs twice). Sandboxed processors run the job in a separate process or worker thread. Another option is to run workers in a separate deployment from the API.

### 413: How do you run the queue workers separately from the API?

Create two entry points that share modules. The API imports the module that registers queues and producers. The worker entry point is a standalone app (`createApplicationContext`) that imports the processors. Deploy them separately so you can scale workers based on queue length and API instances based on traffic.

### 414: What is a BullMQ flow and when would you use it?

A flow is a parent job with child jobs. The parent runs only after all children finish, and it can read their results. Use it for "do these steps in parallel, then combine" work, like processing image sizes and then updating the record.

```ts
await this.flowProducer.add({
  name: "publish-post",
  queueName: "posts",
  data: { postId },
  children: [
    { name: "resize", queueName: "images", data: { postId, size: "sm" } },
    { name: "resize", queueName: "images", data: { postId, size: "lg" } },
  ],
});
```

Register it with `BullModule.registerFlowProducer({ name: 'flows' })` and inject with `@InjectFlowProducer('flows')`.

### 415: How do you implement feature flags in Nest?

Wrap a flag provider (LaunchDarkly, Unleash, OpenFeature, or a simple config table) in a service. Check flags in services for logic, and add a guard plus a decorator to hide whole routes.

```ts
export const Feature = Reflector.createDecorator<string>();

@Injectable()
export class FeatureGuard implements CanActivate {
  constructor(
    private reflector: Reflector,
    private flags: FlagsService,
  ) {}

  async canActivate(ctx: ExecutionContext) {
    const flag = this.reflector.get(Feature, ctx.getHandler());
    if (!flag) return true;
    const user = ctx.switchToHttp().getRequest().user;
    if (!(await this.flags.isEnabled(flag, user)))
      throw new NotFoundException();
    return true;
  }
}
```

### 416: Can you change configuration without restarting the app?

`ConfigService` values are loaded at startup and providers often read them once, so no. For values that must change at runtime (limits, flags), store them in a database or a config service and read them with short caching, or subscribe to change notifications. Things like database URLs or ports should stay startup-only.

### 417: How do you add internationalized error messages?

Use `nestjs-i18n` or your own translation service. Detect the language from `Accept-Language` (or user settings) in middleware or a resolver, throw errors with a message key, and translate the key in an exception filter. With `class-validator`, use keys as messages and translate them in the `exceptionFactory` of `ValidationPipe`.

### 418: How would you make `errorCode` from Nest 12 consistent across the whole API?

Keep error codes in one enum or const object, throw exceptions with those codes, and have a global exception filter put the code in a fixed response shape (for example `{ statusCode, errorCode, message, requestId }`). For errors that are not `HttpException`, map known cases (like unique violations) to codes and send `INTERNAL_ERROR` for everything else. Document the codes in Swagger so clients can rely on them.

### 419: How should you upgrade a large app from Nest 11 to 12?

1. Update Node to a supported version (20.19+ or 22.12+; newer for the CLI).
2. Run `nest upgrade --dry-run`, then `nest upgrade`, and update third-party Nest libraries to versions that support 12.
3. Fix the breaking changes: NATS v3, GraphQL `graphql-ws`, Terminus `HealthIndicatorService`, `@nestjs/config` `libraryOptions` and Joi 18, `@Optional()` inheritance, stricter pipe types, `useBodyParser` typing.
4. Check lifecycle hook order assumptions.
5. Run tests. If Jest fails with `ERR_REQUIRE_ASYNC_MODULE`, use Node 24.9+ or switch to Vitest.
6. Leave the ESM migration of your own code for later; it is optional.

### 420: What were the main Express 5 pitfalls when moving to Nest 11 or later?

- Wildcards must be named (`*splat`), and `?` for optional params becomes `{/:param}`.
- Regex characters in route paths are not supported.
- The default query parser is `simple`, so nested query objects are not parsed.
- `req.body` is `undefined` (not `{}`) when no body parser ran.
- Some removed Express 4 methods (like `res.redirect('back')`, `req.param()`) are gone.
- Rejected promises in middleware are forwarded to error handlers automatically.

### 421: What does "stricter `isHttpError`" in Nest 12 mean for custom errors?

Nest checks if an error looks like an HTTP error (has a valid status) when it decides how to respond. In Nest 12 that check is stricter, so plain objects or errors from libraries with a `status` field may no longer be treated as HTTP errors and could become 500 responses. If you relied on that, throw real `HttpException` subclasses or map those errors in a filter.

### 422: How do you prevent memory growth in throttler or caches keyed by user input?

Any in-memory map keyed by IP, user or header grows with traffic. Use stores with TTL and size limits (LRU), or move them to Redis with TTLs. Validate keys (like tenant IDs) before using them as cache keys, so attackers cannot fill memory with random values.

### 423: How do you rate limit WebSocket messages?

`ThrottlerGuard` is built for HTTP. For sockets, extend it and read the client from the WS context, or write a small guard that counts messages per socket in a sliding window and throws `WsException` when the limit is hit. Also limit message size in the adapter options and disconnect clients that keep misbehaving.

### 424: How do you deal with backpressure in WebSockets or SSE?

If the server sends faster than a client reads, messages pile up in memory. Check the socket buffer (`ws.bufferedAmount` or Socket.IO's volatile emits) and drop or merge updates for slow clients. Send diffs or the latest state instead of every event. Set limits and disconnect clients whose buffers stay full.

### 425: How do you scale SSE endpoints?

Each SSE connection is a long-lived HTTP request, so it holds memory and a file descriptor. Fan out events with Redis pub/sub (or a broker) so any instance can push to its own clients. Configure proxies and load balancers not to buffer or time out the stream, send heartbeat comments regularly, and set `X-Accel-Buffering: no` behind Nginx.

### 426: How do you build a typed event system on top of `@nestjs/event-emitter`?

Map event names to payload types and wrap the emitter.

```ts
interface Events {
  "order.created": { orderId: string };
  "user.deleted": { userId: string };
}

@Injectable()
export class TypedEvents {
  constructor(private emitter: EventEmitter2) {}

  emit<K extends keyof Events>(name: K, payload: Events[K]) {
    return this.emitter.emitAsync(name, payload);
  }
}
```

Listeners still use `@OnEvent('order.created')`, but the payload type now comes from one place.

### 427: How do you make sure `@OnEvent` handlers are registered before events fire at startup?

Listeners are attached during `onApplicationBootstrap`. Events emitted earlier (for example in an `onModuleInit`) can be missed. Emit startup events in `onApplicationBootstrap` or later, or wait for `EventEmitterReadinessWatcher.waitUntilReady()` before emitting.

### 428: What is the difference between `nest build` with `tsc`, `swc` and `rspack`?

- `tsc`: type checks and compiles file by file. Slowest, but no surprises. Supports CLI plugins.
- `swc`: compiles very fast without type checking (add `--type-check` or run `tsc --noEmit` separately). Supports CLI plugins through a separate metadata step. Stricter about circular imports.
- `rspack`: bundles the app (and its node_modules if configured) into fewer files. Good for monorepos, serverless and faster startup. Replaced webpack in Nest 12.

### 429: How do you build all apps of a Nest monorepo quickly?

Nest 12 can build all projects in parallel:

```bash
nest build --all --parallel 4
```

Use `includeLibraryAssets` in `nest-cli.json` if libraries have assets (like templates) that must be copied into the app output.

### 430: When would you choose Nx over the Nest CLI monorepo?

When you need caching of builds and tests, running only affected projects in CI, module boundary rules, many apps in different frameworks (for example Nest plus React), or code generators across the workspace. The Nest CLI monorepo is simpler and fine for a few Nest apps sharing libraries.

### 431: How do you share DTOs between a Nest backend and a frontend?

Put them in a shared library. But `class-validator` decorators pull backend packages into the frontend bundle. Options: share plain TypeScript types only, generate a client from the OpenAPI spec (`openapi-typescript`, orval), or use schemas (like Zod) that run in both places. Nest 12's Standard Schema support makes the last option easy, because the same schema validates in the browser and in the API.

### 432: How do you create an OpenAPI spec in CI without starting the server?

Write a small script that creates the app (with `preview: true` or mocked heavy providers), generates the document and writes it to a file.

```ts
const app = await NestFactory.create(AppModule, {
  logger: false,
  abortOnError: false,
});
const document = SwaggerModule.createDocument(
  app,
  new DocumentBuilder().build(),
);
writeFileSync("openapi.json", JSON.stringify(document, null, 2));
await app.close();
```

Diff the generated file in pull requests to catch breaking API changes.

### 433: How do you do contract testing between Nest services?

With a tool like Pact. The consumer writes tests that describe the requests it sends and the responses it expects; this produces a contract file. The provider (a Nest service) runs a verification test that replays the contract against the real app with test data. This catches breaking changes before deploy without full end-to-end environments.

### 434: What does a good testing strategy for a Nest app look like?

- Unit tests for domain logic and complex services, with DI fakes.
- Integration tests for repositories and modules against a real database (Testcontainers).
- E2E tests through HTTP for main flows, auth and error handling.
- Contract tests for service-to-service APIs.
- A few smoke tests in a deployed environment.

Avoid mocking everything in "unit" tests of thin services; testing them through HTTP with a real database is often more useful.

### 435: How do you test that a guard is applied to all routes that need it?

Use Devtools graph data or `DiscoveryService` in a test to list all controllers and handlers, read their guard metadata (`'__guards__'`), and fail if a route without `@Public()` lacks the auth guard. With a global `APP_GUARD` and a `@Public()` opt-out, the risk is lower, so many teams just write e2e tests that call each route without a token and expect 401.

### 436: How do you keep e2e tests fast?

Create the app once per test file (or once globally) instead of per test, reuse one database container across files, reset data with truncation or transactions instead of re-running migrations, run test files in parallel with separate databases or schemas, and mock only slow external HTTP services (for example with `nock` or MSW).

### 437: How do you test an exception filter?

Create the filter, fake `ArgumentsHost`, call `catch()` and check the response mock.

```ts
it("formats HttpException", () => {
  const json = vi.fn();
  const status = vi.fn().mockReturnValue({ json });
  const host = {
    switchToHttp: () => ({
      getResponse: () => ({ status }),
      getRequest: () => ({ url: "/cats" }),
    }),
  } as any;

  new HttpExceptionFilter().catch(new NotFoundException("nope"), host);

  expect(status).toHaveBeenCalledWith(404);
  expect(json).toHaveBeenCalledWith(expect.objectContaining({ path: "/cats" }));
});
```

### 438: How would you implement your own `@Transactional()` decorator?

Use `AsyncLocalStorage` to hold the transaction, and a method decorator that starts one if none is active.

```ts
export const txStorage = new AsyncLocalStorage<EntityManager>();

export function Transactional(): MethodDecorator {
  return (target, key, descriptor: PropertyDescriptor) => {
    const original = descriptor.value;
    descriptor.value = async function (...args: unknown[]) {
      if (txStorage.getStore()) return original.apply(this, args);
      const dataSource: DataSource = (this as any).dataSource;
      return dataSource.transaction((manager) =>
        txStorage.run(manager, () => original.apply(this, args)),
      );
    };
    return descriptor;
  };
}
```

Repositories call `txStorage.getStore() ?? this.dataSource.manager`. Note that replacing `descriptor.value` drops metadata set by other decorators on the method, so copy metadata over (`Reflect.getMetadataKeys`) if you combine it with Nest decorators.

### 439: Why can a method decorator that wraps a function break Nest route decorators?

Nest stores route, guard and param metadata on the function object (`descriptor.value`). If your decorator replaces the function with a new one, and runs after Nest's decorators, that metadata is on the old function and Nest no longer sees it. Fix it by copying all metadata keys from the old function to the new one, or by applying your decorator first (decorators run bottom to top).

### 440: How does the Nest router handle the same path for different versions and hosts?

Each handler is registered on the adapter with its path, method, version and host filters. For versioning, Nest registers one route and picks the right handler at request time based on the extracted version; if none matches, it returns 404. Host filters are checked the same way. That is why the order in which modules and controllers are registered can still matter for overlapping patterns, unless you use `routeResolutionStrategy: 'specificity'` in Nest 12.

### 441: How do you use `routeConflictPolicy` in CI?

Set `duplicate: 'error'` so the app fails to start when two handlers have the same method and path, and `shadow: 'warn'` or `'error'` for routes that can never be hit because an earlier one matches first. Running the e2e suite (or a boot script) in CI then catches these mistakes before release.

### 442: What is `nest deploy`?

In Nest 12 the CLI has a `deploy` command that forwards to Mau, the official Nest deployment platform for AWS. It is optional; you can still deploy any Nest app as a normal Node process or container.

### 443: How do you write a production Dockerfile for a Nest app?

Use a multi-stage build: install and build in one stage, copy only `dist`, production `node_modules` and `package.json` into a small runtime image, and run as a non-root user.

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/package*.json ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/main.js"]
```

Run the process directly with `node` (not `npm start`) so it receives `SIGTERM` for graceful shutdown.

### 444: How do you handle schema migrations safely with zero downtime?

Use the expand and contract pattern. First deploy a migration that only adds (new column, nullable or with default, new table). Deploy code that writes to both old and new. Backfill data. Deploy code that reads from the new one. Finally remove the old column in a later release. Run migrations as a separate step before rolling out new pods, never on app startup from several instances at once.

### 445: How do you run Nest with Bun or Deno?

Nest 12's CLI supports `bun` as a package manager, and Nest apps generally run on Bun because it implements most Node APIs. Deno can run Nest through its Node compatibility layer. Decorator metadata needs a compiler that emits it, and some native modules or edge cases may not work, so test your full stack and keep Node for production unless you have a strong reason.

### 446: How do you avoid loading every module in a big app when you only need a few, for example in a worker?

Design modules so the worker can import only what it needs: a `QueueWorkerModule` that imports the domain modules and infrastructure it uses, without controllers or HTTP-only modules. Avoid a single `AppModule` that everything depends on. Global modules make this harder, because they hide what is needed.

### 447: How do you implement API keys for machine-to-machine access alongside JWT for users?

Write two guards (or Passport strategies) and accept either.

```ts
@Injectable()
export class ApiKeyOrJwtGuard implements CanActivate {
  constructor(
    private apiKeys: ApiKeysService,
    private jwt: JwtService,
  ) {}

  async canActivate(ctx: ExecutionContext) {
    const req = ctx.switchToHttp().getRequest();
    const apiKey = req.headers["x-api-key"];
    if (apiKey) {
      req.principal = await this.apiKeys.verify(apiKey); // hashed lookup
      return Boolean(req.principal);
    }
    const token = req.headers.authorization?.replace("Bearer ", "");
    if (!token) throw new UnauthorizedException();
    req.principal = await this.jwt.verifyAsync(token);
    return true;
  }
}
```

Store API keys hashed, give them scopes, and log which key made each call.

### 448: How would you implement single-session or token revocation with JWTs?

JWTs are valid until they expire, so you need some state. Options: keep access tokens short-lived and revoke refresh tokens in the database; keep a deny-list of revoked token IDs (`jti`) in Redis until their expiry; or store a `tokenVersion` on the user and put it in the token, then reject tokens whose version is older. Each one adds a lookup per request, so cache it.

### 449: What would you check when a Nest app is slow only under load?

- Event loop delay (blocking code).
- Database pool waits and slow queries (pool too small or missing indexes).
- Request-scoped providers on hot paths.
- Logging volume (sync logging to stdout can block).
- GC pauses from large allocations (big JSON, no streaming).
- External calls without timeouts.
- Lock contention in the database or Redis.

Profile under load with a load generator and compare flame graphs, instead of guessing.

### 450: What are the things you would say make a Nest codebase healthy in the long run?

Clear module boundaries by feature, constructor injection with small services, DTOs or schemas separate from entities, validation and error formats set globally, config validated at startup, no hidden global state, tests at the right levels, graceful shutdown and health checks, structured logs with request IDs, and keeping Nest and its packages up to date by reading each migration guide when a new major version comes out.
