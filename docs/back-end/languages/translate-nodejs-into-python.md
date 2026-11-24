# Translate Node.js into Python Interview Questions and Answers

_Last updated: November 24, 2026_

450 interview questions about translating Node.js back-end code into Python, split into three levels: 150 easy, 150 moderate and 150 advanced. Every answer shows the same idea in both languages, in this order: Node.js, then Python.

The answers target modern versions: Node.js 24 and 26 LTS with ES modules and TypeScript, and Python 3.13+ with type hints and `asyncio` (newer features from Python 3.14 and 3.15 are marked). For web code, Express and NestJS map to FastAPI, Flask and Django; Prisma maps to SQLAlchemy 2.0 and the Django ORM; Zod maps to Pydantic v2; Jest and Vitest map to pytest; npm maps to uv and pip.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does it mean to translate a Node.js app into Python?](#1-what-does-it-mean-to-translate-a-nodejs-app-into-python)
- [2: How are Node.js and Python different in nature?](#2-how-are-nodejs-and-python-different-in-nature)
- [3: How do you create a new project in each?](#3-how-do-you-create-a-new-project-in-each)
- [4: How does package.json map to pyproject.toml?](#4-how-does-packagejson-map-to-pyprojecttoml)
- [5: How do you run a script?](#5-how-do-you-run-a-script)
- [6: How do you install a dependency?](#6-how-do-you-install-a-dependency)
- [7: How do you add a dev dependency?](#7-how-do-you-add-a-dev-dependency)
- [8: What replaces package-lock.json?](#8-what-replaces-package-lockjson)
- [9: What replaces node_modules?](#9-what-replaces-node_modules)
- [10: What replaces npm scripts?](#10-what-replaces-npm-scripts)
- [11: What replaces npx?](#11-what-replaces-npx)
- [12: How do imports and exports translate?](#12-how-do-imports-and-exports-translate)
- [13: How do default exports translate?](#13-how-do-default-exports-translate)
- [14: How does CommonJS require translate?](#14-how-does-commonjs-require-translate)
- [15: How do __dirname and import.meta.dirname translate?](#15-how-do-__dirname-and-importmetadirname-translate)
- [16: How do you check if a file is the entry point?](#16-how-do-you-check-if-a-file-is-the-entry-point)
- [17: How do let and const translate?](#17-how-do-let-and-const-translate)
- [18: How do JavaScript numbers map to Python types?](#18-how-do-javascript-numbers-map-to-python-types)
- [19: How do template literals translate?](#19-how-do-template-literals-translate)
- [20: How do null and undefined translate?](#20-how-do-null-and-undefined-translate)
- [21: How does truthiness differ?](#21-how-does-truthiness-differ)
- [22: How do == and === translate?](#22-how-do--and--translate)
- [23: How do arrays translate?](#23-how-do-arrays-translate)
- [24: How do map, filter and reduce translate?](#24-how-do-map-filter-and-reduce-translate)
- [25: How do objects translate to dicts?](#25-how-do-objects-translate-to-dicts)
- [26: How does optional chaining translate?](#26-how-does-optional-chaining-translate)
- [27: How does the nullish coalescing operator translate?](#27-how-does-the-nullish-coalescing-operator-translate)
- [28: How does destructuring translate?](#28-how-does-destructuring-translate)
- [29: How does the spread operator translate?](#29-how-does-the-spread-operator-translate)
- [30: How do rest parameters translate?](#30-how-do-rest-parameters-translate)
- [31: How do default parameters translate, and what is the pitfall?](#31-how-do-default-parameters-translate-and-what-is-the-pitfall)
- [32: How do arrow functions translate?](#32-how-do-arrow-functions-translate)
- [33: How do Map and Set translate?](#33-how-do-map-and-set-translate)
- [34: How do loops translate?](#34-how-do-loops-translate)
- [35: How does switch translate?](#35-how-does-switch-translate)
- [36: How do classes translate?](#36-how-do-classes-translate)
- [37: How do private class fields translate?](#37-how-do-private-class-fields-translate)
- [38: How do getters and setters translate?](#38-how-do-getters-and-setters-translate)
- [39: How do static methods translate?](#39-how-do-static-methods-translate)
- [40: How do inheritance and super translate?](#40-how-do-inheritance-and-super-translate)
- [41: How do TypeScript interfaces translate?](#41-how-do-typescript-interfaces-translate)
- [42: How do enums translate?](#42-how-do-enums-translate)
- [43: How do TypeScript types translate to Python type hints?](#43-how-do-typescript-types-translate-to-python-type-hints)
- [44: What replaces tsc for type checking?](#44-what-replaces-tsc-for-type-checking)
- [45: How do union and optional types translate?](#45-how-do-union-and-optional-types-translate)
- [46: How do generic functions translate?](#46-how-do-generic-functions-translate)
- [47: How do object shape types translate?](#47-how-do-object-shape-types-translate)
- [48: What are dataclasses and why use them instead of plain objects?](#48-what-are-dataclasses-and-why-use-them-instead-of-plain-objects)
- [49: How do JSON.parse and JSON.stringify translate?](#49-how-do-jsonparse-and-jsonstringify-translate)
- [50: How does Date translate?](#50-how-does-date-translate)
- [51: How do Math functions and rounding translate?](#51-how-do-math-functions-and-rounding-translate)
- [52: How do common string methods translate?](#52-how-do-common-string-methods-translate)
- [53: How do regular expressions translate?](#53-how-do-regular-expressions-translate)
- [54: How does try/catch translate?](#54-how-does-trycatch-translate)
- [55: How do custom errors translate?](#55-how-do-custom-errors-translate)
- [56: How do finally and else work in Python's try?](#56-how-do-finally-and-else-work-in-pythons-try)
- [57: How does console.log translate?](#57-how-does-consolelog-translate)
- [58: How does process.env translate?](#58-how-does-processenv-translate)
- [59: How do .env files translate?](#59-how-do-env-files-translate)
- [60: How does process.argv translate?](#60-how-does-processargv-translate)
- [61: How do exit codes translate?](#61-how-do-exit-codes-translate)
- [62: How do you read a file?](#62-how-do-you-read-a-file)
- [63: How do you write a file?](#63-how-do-you-write-a-file)
- [64: How do you check if a file exists?](#64-how-do-you-check-if-a-file-exists)
- [65: How do you list a directory or glob files?](#65-how-do-you-list-a-directory-or-glob-files)
- [66: How does the path module translate?](#66-how-does-the-path-module-translate)
- [67: How do you create directories?](#67-how-do-you-create-directories)
- [68: How do Promises and async/await translate?](#68-how-do-promises-and-asyncawait-translate)
- [69: How do you run async code from the top level?](#69-how-do-you-run-async-code-from-the-top-level)
- [70: How do setTimeout and sleep translate?](#70-how-do-settimeout-and-sleep-translate)
- [71: How does Promise.all translate?](#71-how-does-promiseall-translate)
- [72: How do Node-style callbacks translate?](#72-how-do-node-style-callbacks-translate)
- [73: How do you start a basic HTTP server without a framework?](#73-how-do-you-start-a-basic-http-server-without-a-framework)
- [74: How does an Express hello world translate to FastAPI?](#74-how-does-an-express-hello-world-translate-to-fastapi)
- [75: How does an Express hello world translate to Flask?](#75-how-does-an-express-hello-world-translate-to-flask)
- [76: How do route parameters translate?](#76-how-do-route-parameters-translate)
- [77: How do query string parameters translate?](#77-how-do-query-string-parameters-translate)
- [78: How do you read a JSON request body?](#78-how-do-you-read-a-json-request-body)
- [79: How do you set status codes?](#79-how-do-you-set-status-codes)
- [80: How do you set response headers?](#80-how-do-you-set-response-headers)
- [81: How does basic middleware translate?](#81-how-does-basic-middleware-translate)
- [82: How do you serve static files?](#82-how-do-you-serve-static-files)
- [83: How does Express Router translate?](#83-how-does-express-router-translate)
- [84: How do you run a dev server with auto-reload?](#84-how-do-you-run-a-dev-server-with-auto-reload)
- [85: How does fetch translate?](#85-how-does-fetch-translate)
- [86: How do you send a POST request with JSON?](#86-how-do-you-send-a-post-request-with-json)
- [87: How does a simple unit test translate?](#87-how-does-a-simple-unit-test-translate)
- [88: How do common Jest matchers translate to pytest?](#88-how-do-common-jest-matchers-translate-to-pytest)
- [89: How do you test async functions?](#89-how-do-you-test-async-functions)
- [90: How do test file conventions translate?](#90-how-do-test-file-conventions-translate)
- [91: What replaces ESLint and Prettier?](#91-what-replaces-eslint-and-prettier)
- [92: What replaces nvm?](#92-what-replaces-nvm)
- [93: How do you pin the runtime version?](#93-how-do-you-pin-the-runtime-version)
- [94: How does the REPL translate?](#94-how-does-the-repl-translate)
- [95: How do JSDoc comments translate?](#95-how-do-jsdoc-comments-translate)
- [96: How do naming conventions differ?](#96-how-do-naming-conventions-differ)
- [97: How do code blocks and indentation work?](#97-how-do-code-blocks-and-indentation-work)
- [98: What about semicolons and long lines?](#98-what-about-semicolons-and-long-lines)
- [99: How do number formatting functions translate?](#99-how-do-number-formatting-functions-translate)
- [100: How does sorting translate?](#100-how-does-sorting-translate)
- [101: How do you copy objects and arrays?](#101-how-do-you-copy-objects-and-arrays)
- [102: How do typeof and instanceof translate?](#102-how-do-typeof-and-instanceof-translate)
- [103: How does parsing numbers from strings translate?](#103-how-does-parsing-numbers-from-strings-translate)
- [104: How do includes and indexOf translate?](#104-how-do-includes-and-indexof-translate)
- [105: How do Object.keys and Object.entries translate?](#105-how-do-objectkeys-and-objectentries-translate)
- [106: How does Object.assign translate?](#106-how-does-objectassign-translate)
- [107: How do split and join translate?](#107-how-do-split-and-join-translate)
- [108: How does array slicing translate?](#108-how-does-array-slicing-translate)
- [109: How do you create ranges of numbers?](#109-how-do-you-create-ranges-of-numbers)
- [110: How do lodash-style helpers like zip and chunk translate?](#110-how-do-lodash-style-helpers-like-zip-and-chunk-translate)
- [111: How do random values and UUIDs translate?](#111-how-do-random-values-and-uuids-translate)
- [112: How do you hash a string?](#112-how-do-you-hash-a-string)
- [113: How does base64 encoding translate?](#113-how-does-base64-encoding-translate)
- [114: How does Buffer translate?](#114-how-does-buffer-translate)
- [115: How does URL parsing translate?](#115-how-does-url-parsing-translate)
- [116: How does encodeURIComponent translate?](#116-how-does-encodeuricomponent-translate)
- [117: How does setInterval translate?](#117-how-does-setinterval-translate)
- [118: How does a basic EventEmitter translate?](#118-how-does-a-basic-eventemitter-translate)
- [119: How do globals translate?](#119-how-do-globals-translate)
- [120: How do closures translate?](#120-how-do-closures-translate)
- [121: Does Python have hoisting?](#121-does-python-have-hoisting)
- [122: How does this translate to self?](#122-how-does-this-translate-to-self)
- [123: How do module-level singletons translate?](#123-how-do-module-level-singletons-translate)
- [124: How do you print a stack trace?](#124-how-do-you-print-a-stack-trace)
- [125: How do assertions translate?](#125-how-do-assertions-translate)
- [126: How does date formatting and parsing translate?](#126-how-does-date-formatting-and-parsing-translate)
- [127: How do time zones translate?](#127-how-do-time-zones-translate)
- [128: How do you measure elapsed time?](#128-how-do-you-measure-elapsed-time)
- [129: Why can Python sleep in normal code when Node.js cannot?](#129-why-can-python-sleep-in-normal-code-when-nodejs-cannot)
- [130: How does child_process translate?](#130-how-does-child_process-translate)
- [131: How does the os module translate?](#131-how-does-the-os-module-translate)
- [132: How do you read user input in a script?](#132-how-do-you-read-user-input-in-a-script)
- [133: How do you parse command-line options?](#133-how-do-you-parse-command-line-options)
- [134: How do TextEncoder and TextDecoder translate?](#134-how-do-textencoder-and-textdecoder-translate)
- [135: How does BigInt translate?](#135-how-does-bigint-translate)
- [136: How does floating point math compare?](#136-how-does-floating-point-math-compare)
- [137: How do global error handlers translate?](#137-how-do-global-error-handlers-translate)
- [138: How does Ctrl+C handling translate?](#138-how-does-ctrlc-handling-translate)
- [139: How does a basic Dockerfile translate?](#139-how-does-a-basic-dockerfile-translate)
- [140: What replaces NODE_ENV?](#140-what-replaces-node_env)
- [141: What replaces "type": "module" in package.json?](#141-what-replaces-type-module-in-packagejson)
- [142: How does publishing a package translate?](#142-how-does-publishing-a-package-translate)
- [143: How do semver ranges translate?](#143-how-do-semver-ranges-translate)
- [144: What are the most common mistakes JavaScript developers make in Python?](#144-what-are-the-most-common-mistakes-javascript-developers-make-in-python)
- [145: How do you translate a small utility module end to end?](#145-how-do-you-translate-a-small-utility-module-end-to-end)
- [146: How do options objects translate?](#146-how-do-options-objects-translate)
- [147: How does forEach with an index translate?](#147-how-does-foreach-with-an-index-translate)
- [148: How do multiline strings translate?](#148-how-do-multiline-strings-translate)
- [149: How does the ternary operator translate?](#149-how-does-the-ternary-operator-translate)
- [150: Which Python web framework should replace Express?](#150-which-python-web-framework-should-replace-express)

### Moderate Questions (151-300)

- [151: Should you rewrite a Node.js service in Python all at once or step by step?](#151-should-you-rewrite-a-nodejs-service-in-python-all-at-once-or-step-by-step)
- [152: How does Express middleware for auth translate into FastAPI dependencies?](#152-how-does-express-middleware-for-auth-translate-into-fastapi-dependencies)
- [153: How does Express error-handling middleware translate?](#153-how-does-express-error-handling-middleware-translate)
- [154: How does Zod validation translate into Pydantic?](#154-how-does-zod-validation-translate-into-pydantic)
- [155: How do Zod refine and transform translate?](#155-how-do-zod-refine-and-transform-translate)
- [156: How do request and response DTOs translate?](#156-how-do-request-and-response-dtos-translate)
- [157: How do you load and validate configuration?](#157-how-do-you-load-and-validate-configuration)
- [158: What happens if you forget await in each language?](#158-what-happens-if-you-forget-await-in-each-language)
- [159: How does Promise.allSettled translate?](#159-how-does-promiseallsettled-translate)
- [160: How does Promise.race translate?](#160-how-does-promiserace-translate)
- [161: How does Promise.any translate?](#161-how-does-promiseany-translate)
- [162: How do timeouts translate?](#162-how-do-timeouts-translate)
- [163: How does AbortController cancellation translate?](#163-how-does-abortcontroller-cancellation-translate)
- [164: What is structured concurrency and how does it compare to Promise.all?](#164-what-is-structured-concurrency-and-how-does-it-compare-to-promiseall)
- [165: How do you limit concurrency, like p-limit?](#165-how-do-you-limit-concurrency-like-p-limit)
- [166: How does retry with backoff translate?](#166-how-does-retry-with-backoff-translate)
- [167: Why must you not call blocking libraries inside async def?](#167-why-must-you-not-call-blocking-libraries-inside-async-def)
- [168: When should a FastAPI route be def instead of async def?](#168-when-should-a-fastapi-route-be-def-instead-of-async-def)
- [169: Why should you reuse HTTP clients?](#169-why-should-you-reuse-http-clients)
- [170: How do you stream a response?](#170-how-do-you-stream-a-response)
- [171: How do file uploads translate from multer?](#171-how-do-file-uploads-translate-from-multer)
- [172: How do cookies translate?](#172-how-do-cookies-translate)
- [173: How do server sessions translate from express-session?](#173-how-do-server-sessions-translate-from-express-session)
- [174: How does CORS translate?](#174-how-does-cors-translate)
- [175: How do JWTs translate from jsonwebtoken to PyJWT?](#175-how-do-jwts-translate-from-jsonwebtoken-to-pyjwt)
- [176: How does password hashing translate?](#176-how-does-password-hashing-translate)
- [177: How do role-based guards translate?](#177-how-do-role-based-guards-translate)
- [178: How do you protect a whole group of routes?](#178-how-do-you-protect-a-whole-group-of-routes)
- [179: How does rate limiting translate?](#179-how-does-rate-limiting-translate)
- [180: How does helmet translate?](#180-how-does-helmet-translate)
- [181: How does a Prisma schema translate into SQLAlchemy models?](#181-how-does-a-prisma-schema-translate-into-sqlalchemy-models)
- [182: How do Prisma queries translate into SQLAlchemy?](#182-how-do-prisma-queries-translate-into-sqlalchemy)
- [183: How does Prisma include translate to eager loading?](#183-how-does-prisma-include-translate-to-eager-loading)
- [184: How do transactions translate?](#184-how-do-transactions-translate)
- [185: How do migrations translate from Prisma Migrate to Alembic?](#185-how-do-migrations-translate-from-prisma-migrate-to-alembic)
- [186: How do the same queries look in the Django ORM?](#186-how-do-the-same-queries-look-in-the-django-orm)
- [187: How does raw SQL with pg translate?](#187-how-does-raw-sql-with-pg-translate)
- [188: How do connection pool settings translate?](#188-how-do-connection-pool-settings-translate)
- [189: How does Mongoose translate?](#189-how-does-mongoose-translate)
- [190: How does ioredis translate?](#190-how-does-ioredis-translate)
- [191: How does memoization translate?](#191-how-does-memoization-translate)
- [192: How does BullMQ translate into Celery?](#192-how-does-bullmq-translate-into-celery)
- [193: What lighter alternatives to Celery exist?](#193-what-lighter-alternatives-to-celery-exist)
- [194: How does node-cron translate?](#194-how-does-node-cron-translate)
- [195: How does pino logging translate?](#195-how-does-pino-logging-translate)
- [196: How does AsyncLocalStorage translate?](#196-how-does-asynclocalstorage-translate)
- [197: How do WebSockets translate?](#197-how-do-websockets-translate)
- [198: How do Server-Sent Events translate?](#198-how-do-server-sent-events-translate)
- [199: How does Apollo Server translate into a Python GraphQL server?](#199-how-does-apollo-server-translate-into-a-python-graphql-server)
- [200: How does OpenAPI documentation translate?](#200-how-does-openapi-documentation-translate)
- [201: How does Supertest translate?](#201-how-does-supertest-translate)
- [202: How does jest.mock translate?](#202-how-does-jestmock-translate)
- [203: How do spies translate?](#203-how-do-spies-translate)
- [204: How do beforeEach and afterEach translate?](#204-how-do-beforeeach-and-aftereach-translate)
- [205: How does test.each translate?](#205-how-does-testeach-translate)
- [206: How do you mock outgoing HTTP calls, like nock or MSW?](#206-how-do-you-mock-outgoing-http-calls-like-nock-or-msw)
- [207: How do fake timers translate?](#207-how-do-fake-timers-translate)
- [208: How does test coverage translate?](#208-how-does-test-coverage-translate)
- [209: How do snapshot tests translate?](#209-how-do-snapshot-tests-translate)
- [210: How do integration tests with a real database translate?](#210-how-do-integration-tests-with-a-real-database-translate)
- [211: How does a strict tsconfig translate into strict type checking?](#211-how-does-a-strict-tsconfig-translate-into-strict-type-checking)
- [212: How do generic constraints translate?](#212-how-do-generic-constraints-translate)
- [213: How do discriminated unions translate?](#213-how-do-discriminated-unions-translate)
- [214: How do Partial, Pick and Omit translate?](#214-how-do-partial-pick-and-omit-translate)
- [215: How do unknown and any translate?](#215-how-do-unknown-and-any-translate)
- [216: How do type guards translate?](#216-how-do-type-guards-translate)
- [217: How does readonly translate?](#217-how-does-readonly-translate)
- [218: How do function overloads translate?](#218-how-do-function-overloads-translate)
- [219: How do callback types translate?](#219-how-do-callback-types-translate)
- [220: How do circular imports differ?](#220-how-do-circular-imports-differ)
- [221: How do barrel files translate?](#221-how-do-barrel-files-translate)
- [222: How do npm workspaces translate?](#222-how-do-npm-workspaces-translate)
- [223: How do generators translate?](#223-how-do-generators-translate)
- [224: How does for await translate?](#224-how-does-for-await-translate)
- [225: How do Node streams translate?](#225-how-do-node-streams-translate)
- [226: How do you read a large file line by line?](#226-how-do-you-read-a-large-file-line-by-line)
- [227: How does CSV parsing translate?](#227-how-does-csv-parsing-translate)
- [228: How does Buffer manipulation translate?](#228-how-does-buffer-manipulation-translate)
- [229: How does an async event bus translate?](#229-how-does-an-async-event-bus-translate)
- [230: How does spawn with streaming output translate?](#230-how-does-spawn-with-streaming-output-translate)
- [231: How do worker_threads translate for CPU-heavy work?](#231-how-do-worker_threads-translate-for-cpu-heavy-work)
- [232: How do Node cluster and PM2 translate?](#232-how-do-node-cluster-and-pm2-translate)
- [233: How does graceful shutdown translate?](#233-how-does-graceful-shutdown-translate)
- [234: How do startup hooks translate?](#234-how-do-startup-hooks-translate)
- [235: How does NestJS dependency injection translate?](#235-how-does-nestjs-dependency-injection-translate)
- [236: How do NestJS modules and controllers map to Python structure?](#236-how-do-nestjs-modules-and-controllers-map-to-python-structure)
- [237: How do NestJS interceptors translate?](#237-how-do-nestjs-interceptors-translate)
- [238: How do decorators differ between TypeScript and Python?](#238-how-do-decorators-differ-between-typescript-and-python)
- [239: How do you write a decorator that takes arguments?](#239-how-do-you-write-a-decorator-that-takes-arguments)
- [240: How do context managers compare to try/finally and using?](#240-how-do-context-managers-compare-to-tryfinally-and-using)
- [241: How does date arithmetic translate from date-fns?](#241-how-does-date-arithmetic-translate-from-date-fns)
- [242: How does Intl number and currency formatting translate?](#242-how-does-intl-number-and-currency-formatting-translate)
- [243: How do per-environment config files translate?](#243-how-do-per-environment-config-files-translate)
- [244: How does a production multi-stage Dockerfile translate?](#244-how-does-a-production-multi-stage-dockerfile-translate)
- [245: How do health check endpoints translate?](#245-how-do-health-check-endpoints-translate)
- [246: How does pagination translate?](#246-how-does-pagination-translate)
- [247: How do production web server setups compare?](#247-how-do-production-web-server-setups-compare)
- [248: How do axios interceptors translate?](#248-how-do-axios-interceptors-translate)
- [249: How do HTTP error helpers translate?](#249-how-do-http-error-helpers-translate)
- [250: How do unhandled promise rejections compare to asyncio task errors?](#250-how-do-unhandled-promise-rejections-compare-to-asyncio-task-errors)
- [251: How does debugging translate?](#251-how-does-debugging-translate)
- [252: How does CPU profiling translate?](#252-how-does-cpu-profiling-translate)
- [253: How do husky and lint-staged translate?](#253-how-do-husky-and-lint-staged-translate)
- [254: How do lodash utilities map to the standard library?](#254-how-do-lodash-utilities-map-to-the-standard-library)
- [255: How does groupBy translate?](#255-how-does-groupby-translate)
- [256: How does counting occurrences translate?](#256-how-does-counting-occurrences-translate)
- [257: How do queues translate?](#257-how-do-queues-translate)
- [258: How do priority queues translate?](#258-how-do-priority-queues-translate)
- [259: How do binary search and sorted inserts translate?](#259-how-do-binary-search-and-sorted-inserts-translate)
- [260: How do template engines translate?](#260-how-do-template-engines-translate)
- [261: How do server-rendered views translate from Express with EJS?](#261-how-do-server-rendered-views-translate-from-express-with-ejs)
- [262: How does nodemailer translate?](#262-how-does-nodemailer-translate)
- [263: How does the AWS SDK v3 translate to boto3?](#263-how-does-the-aws-sdk-v3-translate-to-boto3)
- [264: How does the 404 fallback handler translate?](#264-how-does-the-404-fallback-handler-translate)
- [265: How do form-encoded bodies translate?](#265-how-do-form-encoded-bodies-translate)
- [266: How do request body size limits translate?](#266-how-do-request-body-size-limits-translate)
- [267: How does trust proxy translate?](#267-how-does-trust-proxy-translate)
- [268: How do you run HTTPS locally?](#268-how-do-you-run-https-locally)
- [269: How do you translate a CRUD controller end to end?](#269-how-do-you-translate-a-crud-controller-end-to-end)
- [270: How does class-validator translate?](#270-how-does-class-validator-translate)
- [271: How do toJSON and custom serialization translate?](#271-how-do-tojson-and-custom-serialization-translate)
- [272: How do Decimal and big numbers serialize to JSON?](#272-how-do-decimal-and-big-numbers-serialize-to-json)
- [273: How do ID generation strategies translate?](#273-how-do-id-generation-strategies-translate)
- [274: How does parsing dates from JSON translate?](#274-how-does-parsing-dates-from-json-translate)
- [275: What is the closure-in-a-loop pitfall in each language?](#275-what-is-the-closure-in-a-loop-pitfall-in-each-language)
- [276: How does object equality translate?](#276-how-does-object-equality-translate)
- [277: Why can't you use a list or dict as a dict key?](#277-why-cant-you-use-a-list-or-dict-as-a-dict-key)
- [278: How do string length and Unicode differ?](#278-how-do-string-length-and-unicode-differ)
- [279: How do multi-key and locale-aware sorts translate?](#279-how-do-multi-key-and-locale-aware-sorts-translate)
- [280: How do integer division and modulo differ?](#280-how-do-integer-division-and-modulo-differ)
- [281: How does error cause chaining translate?](#281-how-does-error-cause-chaining-translate)
- [282: How does AggregateError translate?](#282-how-does-aggregateerror-translate)
- [283: How do you design an API error hierarchy?](#283-how-do-you-design-an-api-error-hierarchy)
- [284: How do abstract classes translate?](#284-how-do-abstract-classes-translate)
- [285: How do mixins translate?](#285-how-do-mixins-translate)
- [286: How do Symbol.iterator and similar protocols translate?](#286-how-do-symboliterator-and-similar-protocols-translate)
- [287: How does operator overloading work, which JavaScript lacks?](#287-how-does-operator-overloading-work-which-javascript-lacks)
- [288: How does custom object printing translate?](#288-how-does-custom-object-printing-translate)
- [289: How does Object.freeze translate?](#289-how-does-objectfreeze-translate)
- [290: How do WeakMap and WeakRef translate?](#290-how-do-weakmap-and-weakref-translate)
- [291: How does Proxy translate?](#291-how-does-proxy-translate)
- [292: How does reflection translate?](#292-how-does-reflection-translate)
- [293: How do dynamic imports translate?](#293-how-do-dynamic-imports-translate)
- [294: How do plugin systems translate?](#294-how-do-plugin-systems-translate)
- [295: How do CLI frameworks like commander translate?](#295-how-do-cli-frameworks-like-commander-translate)
- [296: How does the bin field translate?](#296-how-does-the-bin-field-translate)
- [297: How does a library's folder layout translate?](#297-how-does-a-librarys-folder-layout-translate)
- [298: How do TypeScript path aliases translate?](#298-how-do-typescript-path-aliases-translate)
- [299: Which runtime errors show up most after a translation?](#299-which-runtime-errors-show-up-most-after-a-translation)
- [300: How do you compare the performance of the old and new service?](#300-how-do-you-compare-the-performance-of-the-old-and-new-service)

### Advanced Questions (301-450)

- [301: How do the event loops of Node.js and asyncio differ under the hood?](#301-how-do-the-event-loops-of-nodejs-and-asyncio-differ-under-the-hood)
- [302: How do the GIL and free-threaded Python change the concurrency story?](#302-how-do-the-gil-and-free-threaded-python-change-the-concurrency-story)
- [303: Is there an equivalent of process.nextTick and microtasks in asyncio?](#303-is-there-an-equivalent-of-processnexttick-and-microtasks-in-asyncio)
- [304: What is uvloop and when does it matter?](#304-what-is-uvloop-and-when-does-it-matter)
- [305: What are WSGI and ASGI, and how do they compare to Node's http module?](#305-what-are-wsgi-and-asgi-and-how-do-they-compare-to-nodes-http-module)
- [306: How do you size worker processes compared to a Node.js cluster?](#306-how-do-you-size-worker-processes-compared-to-a-nodejs-cluster)
- [307: How do you handle CPU-bound work in each runtime?](#307-how-do-you-handle-cpu-bound-work-in-each-runtime)
- [308: How does memory management differ between V8 and CPython?](#308-how-does-memory-management-differ-between-v8-and-cpython)
- [309: How do you find memory leaks in each?](#309-how-do-you-find-memory-leaks-in-each)
- [310: How do you profile a live production process?](#310-how-do-you-profile-a-live-production-process)
- [311: How do startup times compare, and what can you do about slow imports?](#311-how-do-startup-times-compare-and-what-can-you-do-about-slow-imports)
- [312: How do serverless cold starts compare?](#312-how-do-serverless-cold-starts-compare)
- [313: How does backpressure translate?](#313-how-does-backpressure-translate)
- [314: How do you clean up async generators safely?](#314-how-do-you-clean-up-async-generators-safely)
- [315: Why must you not swallow CancelledError?](#315-why-must-you-not-swallow-cancellederror)
- [316: How do you protect work from cancellation?](#316-how-do-you-protect-work-from-cancellation)
- [317: How do nested timeouts behave?](#317-how-do-nested-timeouts-behave)
- [318: How do contextvars behave with tasks and threads compared to AsyncLocalStorage?](#318-how-do-contextvars-behave-with-tasks-and-threads-compared-to-asynclocalstorage)
- [319: What thread-safety issues appear in Python that Node.js developers don't expect?](#319-what-thread-safety-issues-appear-in-python-that-nodejs-developers-dont-expect)
- [320: How do you size database pools for async workers?](#320-how-do-you-size-database-pools-for-async-workers)
- [321: What async SQLAlchemy pitfalls catch Node.js developers?](#321-what-async-sqlalchemy-pitfalls-catch-nodejs-developers)
- [322: How do you detect and fix N+1 queries?](#322-how-do-you-detect-and-fix-n1-queries)
- [323: How do optimistic locking and isolation levels translate?](#323-how-do-optimistic-locking-and-isolation-levels-translate)
- [324: How do you run zero-downtime schema migrations during a language switch?](#324-how-do-you-run-zero-downtime-schema-migrations-during-a-language-switch)
- [325: How do you stream large query results without loading them into memory?](#325-how-do-you-stream-large-query-results-without-loading-them-into-memory)
- [326: How do distributed locks translate?](#326-how-do-distributed-locks-translate)
- [327: How do you implement idempotency keys?](#327-how-do-you-implement-idempotency-keys)
- [328: How does the transactional outbox pattern translate?](#328-how-does-the-transactional-outbox-pattern-translate)
- [329: How does KafkaJS translate?](#329-how-does-kafkajs-translate)
- [330: How does amqplib translate for RabbitMQ?](#330-how-does-amqplib-translate-for-rabbitmq)
- [331: How does gRPC translate?](#331-how-does-grpc-translate)
- [332: How does OpenTelemetry instrumentation translate?](#332-how-does-opentelemetry-instrumentation-translate)
- [333: How do Prometheus metrics differ with multiple Python workers?](#333-how-do-prometheus-metrics-differ-with-multiple-python-workers)
- [334: How do you keep log correlation across services?](#334-how-do-you-keep-log-correlation-across-services)
- [335: How does Sentry error tracking translate?](#335-how-does-sentry-error-tracking-translate)
- [336: How does SQL injection risk compare?](#336-how-does-sql-injection-risk-compare)
- [337: Is there a Python equivalent of prototype pollution?](#337-is-there-a-python-equivalent-of-prototype-pollution)
- [338: How do you prevent SSRF in each stack?](#338-how-do-you-prevent-ssrf-in-each-stack)
- [339: How do you prevent path traversal?](#339-how-do-you-prevent-path-traversal)
- [340: What dangerous dynamic execution features exist in each?](#340-what-dangerous-dynamic-execution-features-exist-in-each)
- [341: How do timing-safe comparisons translate?](#341-how-do-timing-safe-comparisons-translate)
- [342: How does regex denial of service (ReDoS) compare?](#342-how-does-regex-denial-of-service-redos-compare)
- [343: How does dependency security scanning translate?](#343-how-does-dependency-security-scanning-translate)
- [344: Is there a Python equivalent of Node's permission model?](#344-is-there-a-python-equivalent-of-nodes-permission-model)
- [345: How does CSRF protection differ between Express and Django?](#345-how-does-csrf-protection-differ-between-express-and-django)
- [346: How does Passport.js translate for OAuth and OIDC?](#346-how-does-passportjs-translate-for-oauth-and-oidc)
- [347: How do you validate untrusted input defensively at scale?](#347-how-do-you-validate-untrusted-input-defensively-at-scale)
- [348: How do you secure file uploads?](#348-how-do-you-secure-file-uploads)
- [349: How do you handle TLS client settings safely?](#349-how-do-you-handle-tls-client-settings-safely)
- [350: How do you implement a distributed rate limiter?](#350-how-do-you-implement-a-distributed-rate-limiter)
- [351: What TypeScript type features have no Python equivalent?](#351-what-typescript-type-features-have-no-python-equivalent)
- [352: How do branded types translate?](#352-how-do-branded-types-translate)
- [353: How do variance and generic protocols compare?](#353-how-do-variance-and-generic-protocols-compare)
- [354: How do you type decorators that keep the wrapped signature?](#354-how-do-you-type-decorators-that-keep-the-wrapped-signature)
- [355: How do you validate data against a type that is not a model?](#355-how-do-you-validate-data-against-a-type-that-is-not-a-model)
- [356: How do you share types between a TypeScript frontend and a Python backend?](#356-how-do-you-share-types-between-a-typescript-frontend-and-a-python-backend)
- [357: How do you prove the Python service matches the Node.js contract?](#357-how-do-you-prove-the-python-service-matches-the-nodejs-contract)
- [358: What JSON output differences break clients after a translation?](#358-what-json-output-differences-break-clients-after-a-translation)
- [359: How do you keep camelCase JSON with snake_case Python code?](#359-how-do-you-keep-camelcase-json-with-snake_case-python-code)
- [360: How do you reproduce Express's dropping of undefined fields?](#360-how-do-you-reproduce-expresss-dropping-of-undefined-fields)
- [361: How do you keep the old error response format?](#361-how-do-you-keep-the-old-error-response-format)
- [362: What breaks with large integers between Python and JavaScript clients?](#362-what-breaks-with-large-integers-between-python-and-javascript-clients)
- [363: What string handling differences can change behavior?](#363-what-string-handling-differences-can-change-behavior)
- [364: What datetime pitfalls appear when moving from JavaScript Date?](#364-what-datetime-pitfalls-appear-when-moving-from-javascript-date)
- [365: What regex syntax differences matter when porting patterns?](#365-what-regex-syntax-differences-matter-when-porting-patterns)
- [366: How do you keep rounding results identical?](#366-how-do-you-keep-rounding-results-identical)
- [367: How do you port comparator-based sorting safely?](#367-how-do-you-port-comparator-based-sorting-safely)
- [368: How do bitwise operations differ?](#368-how-do-bitwise-operations-differ)
- [369: How do you route traffic during a strangler migration?](#369-how-do-you-route-traffic-during-a-strangler-migration)
- [370: What problems come from running both services on one database?](#370-what-problems-come-from-running-both-services-on-one-database)
- [371: What is shadow traffic and how do you use it to verify a translation?](#371-what-is-shadow-traffic-and-how-do-you-use-it-to-verify-a-translation)
- [372: How do you use feature flags during a language migration?](#372-how-do-you-use-feature-flags-during-a-language-migration)
- [373: Why should you port tests before code?](#373-why-should-you-port-tests-before-code)
- [374: How do you generate SQLAlchemy models from an existing Prisma database?](#374-how-do-you-generate-sqlalchemy-models-from-an-existing-prisma-database)
- [375: How do you share sessions and auth between Node.js and Python during migration?](#375-how-do-you-share-sessions-and-auth-between-nodejs-and-python-during-migration)
- [376: Will existing password hashes keep working in Python?](#376-will-existing-password-hashes-keep-working-in-python)
- [377: How do you migrate background jobs that are already in the queue?](#377-how-do-you-migrate-background-jobs-that-are-already-in-the-queue)
- [378: What are the risks of using AI or automatic tools to translate the code?](#378-what-are-the-risks-of-using-ai-or-automatic-tools-to-translate-the-code)
- [379: When is Python slower or faster than Node.js for a backend?](#379-when-is-python-slower-or-faster-than-nodejs-for-a-backend)
- [380: How do you prevent cache stampedes in async Python?](#380-how-do-you-prevent-cache-stampedes-in-async-python)
- [381: Which async ORM should you pick when moving off Prisma?](#381-which-async-orm-should-you-pick-when-moving-off-prisma)
- [382: What are the limits of async in Django?](#382-what-are-the-limits-of-async-in-django)
- [383: How do you configure Gunicorn and Uvicorn for production?](#383-how-do-you-configure-gunicorn-and-uvicorn-for-production)
- [384: How do Kubernetes probes and graceful shutdown work for a Python service?](#384-how-do-kubernetes-probes-and-graceful-shutdown-work-for-a-python-service)
- [385: Why prefer slim images over Alpine for Python?](#385-why-prefer-slim-images-over-alpine-for-python)
- [386: How do native addons compare?](#386-how-do-native-addons-compare)
- [387: How does writing extensions in Rust compare?](#387-how-does-writing-extensions-in-rust-compare)
- [388: How do you call the old Node.js service from Python during migration?](#388-how-do-you-call-the-old-nodejs-service-from-python-during-migration)
- [389: What does pickling cost when using process pools?](#389-what-does-pickling-cost-when-using-process-pools)
- [390: How does SharedArrayBuffer translate?](#390-how-does-sharedarraybuffer-translate)
- [391: What are subinterpreters and how do they compare to worker_threads?](#391-what-are-subinterpreters-and-how-do-they-compare-to-worker_threads)
- [392: How does free-threaded Python affect libraries and your code?](#392-how-does-free-threaded-python-affect-libraries-and-your-code)
- [393: How do you debug a stuck or slow asyncio application?](#393-how-do-you-debug-a-stuck-or-slow-asyncio-application)
- [394: How do you monitor event loop lag in production?](#394-how-do-you-monitor-event-loop-lag-in-production)
- [395: Why can asyncio tasks disappear, and how do you avoid it?](#395-why-can-asyncio-tasks-disappear-and-how-do-you-avoid-it)
- [396: How do you own long-running background tasks in an ASGI app?](#396-how-do-you-own-long-running-background-tasks-in-an-asgi-app)
- [397: How do you call async code from sync code, and why does asyncio.run fail inside a running loop?](#397-how-do-you-call-async-code-from-sync-code-and-why-does-asynciorun-fail-inside-a-running-loop)
- [398: How do threads and asyncio work together?](#398-how-do-threads-and-asyncio-work-together)
- [399: Why do signals and PID 1 matter in containers for both runtimes?](#399-why-do-signals-and-pid-1-matter-in-containers-for-both-runtimes)
- [400: How do server timeout settings map between Node.js and Uvicorn?](#400-how-do-server-timeout-settings-map-between-nodejs-and-uvicorn)
- [401: Scenario: how would you translate an Express REST API with JWT auth to FastAPI?](#401-scenario-how-would-you-translate-an-express-rest-api-with-jwt-auth-to-fastapi)
- [402: Scenario: how would you translate a NestJS module with DI, guards and interceptors?](#402-scenario-how-would-you-translate-a-nestjs-module-with-di-guards-and-interceptors)
- [403: Scenario: how would you translate a BullMQ worker with retries, concurrency and rate limits to Celery?](#403-scenario-how-would-you-translate-a-bullmq-worker-with-retries-concurrency-and-rate-limits-to-celery)
- [404: Scenario: how would you translate a stream-based CSV import?](#404-scenario-how-would-you-translate-a-stream-based-csv-import)
- [405: Scenario: how would you translate a Socket.IO chat with rooms and a Redis adapter?](#405-scenario-how-would-you-translate-a-socketio-chat-with-rooms-and-a-redis-adapter)
- [406: Scenario: how would you translate a Stripe webhook handler with signature verification?](#406-scenario-how-would-you-translate-a-stripe-webhook-handler-with-signature-verification)
- [407: Scenario: how would you translate direct-to-S3 uploads with presigned URLs?](#407-scenario-how-would-you-translate-direct-to-s3-uploads-with-presigned-urls)
- [408: Scenario: how would you translate a rate-limited client for a third-party API?](#408-scenario-how-would-you-translate-a-rate-limited-client-for-a-third-party-api)
- [409: Scenario: how would you translate a GraphQL server that uses DataLoader?](#409-scenario-how-would-you-translate-a-graphql-server-that-uses-dataloader)
- [410: Scenario: how would you translate a Node.js CLI tool?](#410-scenario-how-would-you-translate-a-nodejs-cli-tool)
- [411: Scenario: how would you translate an AWS Lambda handler behind API Gateway?](#411-scenario-how-would-you-translate-an-aws-lambda-handler-behind-api-gateway)
- [412: Scenario: how would you translate a nightly report job?](#412-scenario-how-would-you-translate-a-nightly-report-job)
- [413: Scenario: how would you translate multi-tenant request scoping?](#413-scenario-how-would-you-translate-multi-tenant-request-scoping)
- [414: Scenario: how would you translate a cached aggregation endpoint?](#414-scenario-how-would-you-translate-a-cached-aggregation-endpoint)
- [415: Scenario: how would you translate a job progress endpoint that streams updates?](#415-scenario-how-would-you-translate-a-job-progress-endpoint-that-streams-updates)
- [416: What do you gain and lose by moving a backend from Node.js to Python?](#416-what-do-you-gain-and-lose-by-moving-a-backend-from-nodejs-to-python)
- [417: When should you not translate a Node.js service into Python?](#417-when-should-you-not-translate-a-nodejs-service-into-python)
- [418: How does the CI pipeline change after the migration?](#418-how-does-the-ci-pipeline-change-after-the-migration)
- [419: How do you check observability parity before cutting over?](#419-how-do-you-check-observability-parity-before-cutting-over)
- [420: How do you avoid writing "JavaScript in Python"?](#420-how-do-you-avoid-writing-javascript-in-python)
- [421: What is EAFP and how does it differ from typical JavaScript style?](#421-what-is-eafp-and-how-does-it-differ-from-typical-javascript-style)
- [422: What packaging mistakes cause production incidents in Python?](#422-what-packaging-mistakes-cause-production-incidents-in-python)
- [423: How does uv's lockfile handle different platforms?](#423-how-does-uvs-lockfile-handle-different-platforms)
- [424: How do you roll out type checking on a newly translated codebase?](#424-how-do-you-roll-out-type-checking-on-a-newly-translated-codebase)
- [425: How does Pydantic v2 performance compare to Zod, and how do you keep it fast?](#425-how-does-pydantic-v2-performance-compare-to-zod-and-how-do-you-keep-it-fast)
- [426: How do you speed up JSON handling in Python?](#426-how-do-you-speed-up-json-handling-in-python)
- [427: Where does FastAPI spend time serializing responses, and how do you reduce it?](#427-where-does-fastapi-spend-time-serializing-responses-and-how-do-you-reduce-it)
- [428: How do Python 3.14 template strings compare to JavaScript tagged templates?](#428-how-do-python-314-template-strings-compare-to-javascript-tagged-templates)
- [429: What can structural pattern matching do that JavaScript cannot?](#429-what-can-structural-pattern-matching-do-that-javascript-cannot)
- [430: How do generator send and coroutine-style generators compare to JavaScript generators?](#430-how-do-generator-send-and-coroutine-style-generators-compare-to-javascript-generators)
- [431: How do descriptors compare to Object.defineProperty?](#431-how-do-descriptors-compare-to-objectdefineproperty)
- [432: How do metaclasses and the init subclass hook compare to TypeScript class decorators?](#432-how-do-metaclasses-and-the-init-subclass-hook-compare-to-typescript-class-decorators)
- [433: Why should import-time work be avoided in Python services?](#433-why-should-import-time-work-be-avoided-in-python-services)
- [434: How does monkeypatching compare to changing prototypes?](#434-how-does-monkeypatching-compare-to-changing-prototypes)
- [435: What identity pitfalls does is have in Python?](#435-what-identity-pitfalls-does-is-have-in-python)
- [436: What are slots and how do they relate to V8 hidden classes?](#436-what-are-slots-and-how-do-they-relate-to-v8-hidden-classes)
- [437: How do key ordering rules differ between objects and dicts?](#437-how-do-key-ordering-rules-differ-between-objects-and-dicts)
- [438: What happens when StopIteration escapes a generator?](#438-what-happens-when-stopiteration-escapes-a-generator)
- [439: How do codemods compare between JavaScript and Python?](#439-how-do-codemods-compare-between-javascript-and-python)
- [440: How do you keep a large async test suite fast and reliable?](#440-how-do-you-keep-a-large-async-test-suite-fast-and-reliable)
- [441: How does property-based testing translate?](#441-how-does-property-based-testing-translate)
- [442: How do micro-benchmarks translate?](#442-how-do-micro-benchmarks-translate)
- [443: How do HTTP/2 and HTTP/3 support compare?](#443-how-do-http2-and-http3-support-compare)
- [444: How do you tune outgoing connection pools?](#444-how-do-you-tune-outgoing-connection-pools)
- [445: What goes wrong when you open connections before a server forks workers?](#445-what-goes-wrong-when-you-open-connections-before-a-server-forks-workers)
- [446: What should a code review checklist for translated code include?](#446-what-should-a-code-review-checklist-for-translated-code-include)
- [447: How do you help a Node.js team become productive in Python?](#447-how-do-you-help-a-nodejs-team-become-productive-in-python)
- [448: How do you plan rollback during the migration?](#448-how-do-you-plan-rollback-during-the-migration)
- [449: How do you know when the migration is done and the Node service can be removed?](#449-how-do-you-know-when-the-migration-is-done-and-the-node-service-can-be-removed)
- [450: What does a final Node.js to Python migration checklist look like?](#450-what-does-a-final-nodejs-to-python-migration-checklist-look-like)

---

# Easy Questions (1-150)

## 1: What does it mean to translate a Node.js app into Python?

It means rebuilding the same features and behavior with Python's language, standard library and ecosystem. You map each Node.js piece to its closest Python match: Express routes become FastAPI or Flask routes, Zod schemas become Pydantic models, Prisma becomes SQLAlchemy, and Jest tests become pytest tests.

A good translation keeps the public behavior the same (URLs, JSON shapes, status codes, errors) and changes only the code underneath. Most of the work is not syntax. It is learning where Python expects concurrency, configuration and errors to live.

| Node.js               | Python                     |
| --------------------- | -------------------------- |
| npm / package.json    | uv or pip / pyproject.toml |
| Express / NestJS      | FastAPI, Flask, Django     |
| Zod / class-validator | Pydantic                   |
| Prisma / TypeORM      | SQLAlchemy / Django ORM    |
| Jest / Vitest         | pytest                     |
| BullMQ                | Celery, RQ, Dramatiq, arq  |

## 2: How are Node.js and Python different in nature?

- **Node.js** is a JavaScript runtime built on V8 and libuv. All I/O is asynchronous by default, and a single thread runs your code on an event loop.
- **Python** is a language with a large standard library. Code is synchronous by default. Async I/O is opt-in through `asyncio` and `async def`. CPython has a Global Interpreter Lock (GIL), though Python 3.13+ offers a free-threaded build.

So in Node.js you get concurrency for free but must avoid blocking the loop. In Python you choose a model: sync code with threads or processes (Flask, Django), or async code with an event loop (FastAPI, aiohttp).

## 3: How do you create a new project in each?

**Node.js**

```bash
mkdir my-app && cd my-app
npm init -y
```

**Python**

```bash
uv init my-app      # creates pyproject.toml, .python-version, main.py
cd my-app
# or the classic way:
python -m venv .venv && source .venv/bin/activate
```

`uv` is a fast project manager written in Rust. It handles Python versions, virtual environments, dependencies and lockfiles in one tool, similar to how npm handles all of that for Node.js.

## 4: How does package.json map to pyproject.toml?

**Node.js**

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "dependencies": { "express": "^5.1.0" },
  "devDependencies": { "vitest": "^4.0.0" }
}
```

**Python**

```toml
[project]
name = "my-app"
version = "1.0.0"
requires-python = ">=3.13"
dependencies = ["fastapi>=0.120"]

[dependency-groups]
dev = ["pytest>=8"]
```

`pyproject.toml` is the standard config file for Python projects. Tools like Ruff, pytest and mypy also read their settings from it, the same way ESLint or Jest can read settings from `package.json`.

## 5: How do you run a script?

**Node.js**

```bash
node index.js
node --watch index.js   # restart on file changes
```

**Python**

```bash
python main.py
uv run main.py          # runs inside the project's virtual environment
python -m my_package    # runs my_package/__main__.py
```

`python -m` runs a module by its import name, which is the usual way to start packages and tools (`python -m pytest`, `python -m http.server`).

## 6: How do you install a dependency?

**Node.js**

```bash
npm install express
```

**Python**

```bash
uv add fastapi          # updates pyproject.toml and uv.lock
# or, without uv, inside an activated venv:
pip install fastapi
```

Plain `pip install` does not edit `pyproject.toml` for you. That is one reason teams use uv or Poetry, which behave like npm: they add the dependency to the manifest and update a lockfile.

## 7: How do you add a dev dependency?

**Node.js**

```bash
npm install --save-dev vitest
```

**Python**

```bash
uv add --dev pytest
```

uv stores dev tools in the `[dependency-groups]` table under `dev`. They are installed by default with `uv sync` and skipped with `uv sync --no-dev`, the same idea as `npm ci --omit=dev`.

## 8: What replaces package-lock.json?

**Node.js**

```bash
npm ci   # installs exactly what package-lock.json says
```

**Python**

```bash
uv lock            # writes uv.lock
uv sync --frozen   # installs exactly what uv.lock says, fails if it is out of date
```

Commit `uv.lock` like you commit `package-lock.json`. Older projects use `requirements.txt` with pinned versions (`fastapi==0.121.0`), often generated with `pip-tools` or `uv pip compile`.

## 9: What replaces node_modules?

**Node.js**

```bash
# dependencies live in ./node_modules, per project, automatically
npm install
```

**Python**

```bash
uv venv               # creates .venv
source .venv/bin/activate
# uv run and uv sync create and use .venv automatically
```

Python installs packages into an environment, not into a project folder. Without a virtual environment, `pip install` would write to the global Python. A `.venv` folder per project gives you the same isolation as `node_modules`. Add it to `.gitignore`.

## 10: What replaces npm scripts?

**Node.js**

```json
{
  "scripts": {
    "dev": "node --watch src/index.js",
    "test": "vitest"
  }
}
```

**Python**

```bash
# Python has no built-in script runner in pyproject.toml.
uv run fastapi dev app/main.py
uv run pytest
```

Teams usually put these commands in a `Makefile`, a `justfile`, or a task runner like `poethepoet` or `taskipy`, which read tasks from `pyproject.toml`:

```toml
[tool.poe.tasks]
dev = "fastapi dev app/main.py"
test = "pytest"
```

## 11: What replaces npx?

**Node.js**

```bash
npx prettier --write .
```

**Python**

```bash
uvx ruff format .        # runs a tool in a temporary environment
pipx run ruff format .   # older alternative
```

`uvx` (short for `uv tool run`) downloads and runs a command-line tool without adding it to your project, exactly like `npx`.

## 12: How do imports and exports translate?

**Node.js**

```js
// math.js
export function add(a, b) {
  return a + b;
}

// index.js
import { add } from "./math.js";
```

**Python**

```python
# math_utils.py
def add(a, b):
    return a + b

# main.py
from math_utils import add
```

In Python every top-level name in a module is importable. There is no `export` keyword. By convention, names that start with `_` are private, and `__all__` lists what `from module import *` exposes.

## 13: How do default exports translate?

**Node.js**

```js
// logger.js
export default function log(msg) {
  console.log(msg);
}

// index.js
import log from "./logger.js";
```

**Python**

```python
# logger.py
def log(msg: str) -> None:
    print(msg)

# main.py
from logger import log
import logger            # or import the whole module
logger.log("hi")
```

Python has no default export. You import names by their real name or import the module itself. Use `as` to rename: `from logger import log as write_log`.

## 14: How does CommonJS require translate?

**Node.js**

```js
const fs = require("node:fs");
const { join } = require("node:path");
module.exports = { readConfig };
```

**Python**

```python
import os
from os.path import join

def read_config(): ...
```

Both `require` and Python's `import` cache the module after the first load, so the module's top-level code runs once. Python only has one module system, so there is no CommonJS versus ES modules split to worry about.

## 15: How do __dirname and import.meta.dirname translate?

**Node.js**

```js
import { join } from "node:path";

const dataFile = join(import.meta.dirname, "data.json"); // Node 20.11+
// CommonJS: join(__dirname, "data.json")
```

**Python**

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data.json"
```

`__file__` is the path of the current module. Resolve paths from it instead of from the working directory, because the process may be started from another folder.

## 16: How do you check if a file is the entry point?

**Node.js**

```js
// ES modules, Node 24.2+
if (import.meta.main) {
  main();
}
// CommonJS
if (require.main === module) main();
```

**Python**

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

When Python runs a file directly, its `__name__` is `"__main__"`. When it is imported, `__name__` is the module name. This guard lets a file work both as a script and as an importable module.

## 17: How do let and const translate?

**Node.js**

```js
let count = 0;
const MAX_RETRIES = 3;
count += 1;
```

**Python**

```python
from typing import Final

count = 0
MAX_RETRIES: Final = 3   # type checkers flag reassignment
count += 1
```

Python has no declaration keywords. Assignment creates the variable. Constants are a naming convention (`UPPER_CASE`), and `Final` only adds a static check. Nothing stops reassignment at runtime.

## 18: How do JavaScript numbers map to Python types?

**Node.js**

```js
const a = 7 / 2; // 3.5
const b = Math.trunc(7 / 2); // 3
const big = 2n ** 64n; // BigInt
Number.isInteger(5.0); // true
```

**Python**

```python
a = 7 / 2       # 3.5 (float)
b = 7 // 2      # 3 (int, floor division)
big = 2 ** 64   # int has unlimited size
isinstance(5.0, int)  # False, 5.0 is a float
```

JavaScript has one `number` type (a 64-bit float) plus `BigInt`. Python has `int` (unlimited size), `float` (64-bit) and `decimal.Decimal` for exact decimal math. Note that `//` floors, so `-7 // 2` is `-4`, while `Math.trunc(-7 / 2)` is `-3`.

## 19: How do template literals translate?

**Node.js**

```js
const name = "Ana";
const msg = `Hello, ${name}! You have ${3 + 2} new messages.`;
```

**Python**

```python
name = "Ana"
msg = f"Hello, {name}! You have {3 + 2} new messages."
```

f-strings support any expression and format specs: `f"{price:.2f}"`, `f"{count:,}"`, `f"{value!r}"`. Python 3.14 adds t-strings (`t"..."`), which return a `Template` object instead of a string, similar to JavaScript tagged templates.

## 20: How do null and undefined translate?

**Node.js**

```js
let user = null;
let missing; // undefined
if (user === null || user === undefined) {
}
if (user == null) {
} // covers both
```

**Python**

```python
user = None
if user is None:
    ...
```

Python has a single "no value" object, `None`. There is no `undefined`. A missing dict key raises `KeyError` and a missing attribute raises `AttributeError` instead of quietly giving `undefined`. Always compare with `is None`, not `== None`.

## 21: How does truthiness differ?

**Node.js**

```js
Boolean([]); // true
Boolean({}); // true
Boolean(""); // false
Boolean(0); // false
```

**Python**

```python
bool([])   # False
bool({})   # False
bool("")   # False
bool(0)    # False
```

Empty lists, dicts, sets, tuples and strings are falsy in Python. So a JavaScript check like `if (items)` (which is always true for an array) means something different from Python's `if items:` (false when empty). When translating, ask whether the code checks "exists" or "is not empty".

## 22: How do == and === translate?

**Node.js**

```js
1 === 1; // true
"1" == 1; // true (type coercion)
"1" === 1; // false
[1] === [1]; // false (different objects)
```

**Python**

```python
1 == 1          # True
"1" == 1        # False, no coercion
[1] == [1]      # True, compares values
a = [1]; b = a
a is b          # True, same object
```

Python's `==` compares values and never coerces between strings and numbers, so it behaves like a value-based `===`. Python's `is` compares identity, which is what JavaScript's `===` does for objects.

## 23: How do arrays translate?

**Node.js**

```js
const items = [1, 2, 3];
items.push(4);
const last = items.pop();
const first = items.shift();
items.length;
items.at(-1);
```

**Python**

```python
items = [1, 2, 3]
items.append(4)
last = items.pop()
first = items.pop(0)   # O(n), use collections.deque for queues
len(items)
items[-1]
```

Python lists support negative indexes directly. Use a `tuple` (`(1, 2, 3)`) for a fixed, read-only sequence.

## 24: How do map, filter and reduce translate?

**Node.js**

```js
const nums = [1, 2, 3, 4];
const doubled = nums.map((n) => n * 2);
const evens = nums.filter((n) => n % 2 === 0);
const sum = nums.reduce((acc, n) => acc + n, 0);
```

**Python**

```python
nums = [1, 2, 3, 4]
doubled = [n * 2 for n in nums]
evens = [n for n in nums if n % 2 == 0]
total = sum(nums)
```

List comprehensions are the Pythonic way to map and filter. `map()` and `filter()` exist but return lazy iterators. For other reductions use built-ins (`sum`, `min`, `max`, `any`, `all`) or `functools.reduce` as a last resort.

## 25: How do objects translate to dicts?

**Node.js**

```js
const user = { name: "Ana", age: 30 };
user.email = "ana@example.com";
console.log(user.name, user["age"]);
delete user.age;
```

**Python**

```python
user = {"name": "Ana", "age": 30}
user["email"] = "ana@example.com"
print(user["name"], user.get("age"))
del user["age"]
```

Dict keys must be quoted and accessed with brackets, not dots. For structured data with fixed fields, use a `dataclass` or a Pydantic model instead, so you get attribute access (`user.name`) and type checking.

## 26: How does optional chaining translate?

**Node.js**

```js
const city = user?.address?.city;
const first = orders?.[0]?.id;
const result = callback?.();
```

**Python**

```python
city = (user or {}).get("address", {}).get("city")   # dicts
city = getattr(getattr(user, "address", None), "city", None)  # objects
first = orders[0]["id"] if orders else None
result = callback() if callback else None
```

Python has no `?.` operator. For dicts, chain `.get()` with defaults. For deep or messy data, validate it into a Pydantic model with optional fields first, then use plain attribute access.

## 27: How does the nullish coalescing operator translate?

**Node.js**

```js
const port = config.port ?? 3000;
const name = input || "Anonymous";
```

**Python**

```python
port = config.port if config.port is not None else 3000
name = input_value or "Anonymous"
```

Python's `or` behaves like JavaScript's `||`: it falls back on any falsy value, including `0` and `""`. There is no `??`, so when `0` or `""` are valid values, write the explicit `is not None` check.

## 28: How does destructuring translate?

**Node.js**

```js
const [first, second] = [10, 20];
const [head, ...tail] = [1, 2, 3];
const { name, age } = user;
```

**Python**

```python
first, second = 10, 20
head, *tail = [1, 2, 3]
name, age = user["name"], user["age"]
# or with structural pattern matching:
match user:
    case {"name": name, "age": age}:
        print(name, age)
```

Sequence unpacking works the same way as array destructuring. Python has no object destructuring syntax, so read keys one by one or use `match` with a mapping pattern.

## 29: How does the spread operator translate?

**Node.js**

```js
const all = [...a, ...b];
const merged = { ...defaults, ...options };
Math.max(...nums);
```

**Python**

```python
all_items = [*a, *b]
merged = {**defaults, **options}
merged = defaults | options   # Python 3.9+
max(*nums)                     # or simply max(nums)
```

`*` unpacks sequences and `**` unpacks dicts. Like JavaScript spread, both make shallow copies: nested objects are still shared.

## 30: How do rest parameters translate?

**Node.js**

```js
function log(level, ...messages) {
  console.log(level, messages.join(" "));
}

function create({ name, ...rest }) {}
```

**Python**

```python
def log(level: str, *messages: str) -> None:
    print(level, " ".join(messages))

def create(name: str, **rest: object) -> None:
    ...
```

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dict, which is the closest match to "rest of an options object".

## 31: How do default parameters translate, and what is the pitfall?

**Node.js**

```js
function addItem(item, list = []) {
  list.push(item);
  return list;
}
addItem(1); // [1]
addItem(2); // [2], a new array each call
```

**Python**

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

JavaScript evaluates default values on every call. Python evaluates them once, when the function is defined. So `def add_item(item, items=[])` shares one list across all calls and keeps growing. Use `None` as the default for lists, dicts and other mutable values.

## 32: How do arrow functions translate?

**Node.js**

```js
const square = (x) => x * x;
const byAge = users.sort((a, b) => a.age - b.age);
```

**Python**

```python
square = lambda x: x * x   # allowed, but a def is preferred
def square(x: int) -> int:
    return x * x

by_age = sorted(users, key=lambda u: u.age)
```

Python's `lambda` can only hold a single expression. Use it for short inline callbacks like `key=`. For anything named or longer, write a normal `def`. Python has no `this` binding issue, so there is no reason to prefer lambdas the way JavaScript prefers arrows.

## 33: How do Map and Set translate?

**Node.js**

```js
const cache = new Map();
cache.set("a", 1);
cache.get("a");
cache.has("a");
const tags = new Set(["js", "py", "js"]);
tags.size; // 2
```

**Python**

```python
cache: dict[str, int] = {}
cache["a"] = 1
cache.get("a")
"a" in cache
tags = {"js", "py", "js"}
len(tags)   # 2
```

Python dicts keep insertion order and accept any hashable key, so they cover both JavaScript objects and `Map`. Python sets support operators: `a | b` (union), `a & b` (intersection) and `a - b` (difference).

## 34: How do loops translate?

**Node.js**

```js
for (const item of items) console.log(item);
for (const [i, item] of items.entries()) console.log(i, item);
for (const [key, value] of Object.entries(obj)) console.log(key, value);
for (let i = 0; i < 5; i++) console.log(i);
```

**Python**

```python
for item in items:
    print(item)
for i, item in enumerate(items):
    print(i, item)
for key, value in obj.items():
    print(key, value)
for i in range(5):
    print(i)
```

Python has no C-style `for` loop. Use `range()` for counters and `enumerate()` when you need the index. Avoid `for (const k in obj)` habits: in Python, looping over a dict gives its keys.

## 35: How does switch translate?

**Node.js**

```js
switch (status) {
  case "active":
    return "Active";
  case "banned":
  case "deleted":
    return "Inactive";
  default:
    return "Unknown";
}
```

**Python**

```python
match status:
    case "active":
        return "Active"
    case "banned" | "deleted":
        return "Inactive"
    case _:
        return "Unknown"
```

`match` (Python 3.10+) has no fall-through and no `break`. It can also match shapes of data, like `case {"type": "click", "x": x}` or `case [first, *rest]`. For simple lookups, a dict is often cleaner: `labels.get(status, "Unknown")`.

## 36: How do classes translate?

**Node.js**

```js
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  greet() {
    return `Hi, ${this.name}`;
  }
}
const u = new User("Ana", "ana@example.com");
```

**Python**

```python
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def greet(self) -> str:
        return f"Hi, {self.name}"

u = User("Ana", "ana@example.com")   # no new keyword
```

`__init__` is the constructor, and every method takes `self` explicitly as its first parameter. There is no `new` keyword.

## 37: How do private class fields translate?

**Node.js**

```js
class Account {
  #balance = 0;
  deposit(amount) {
    this.#balance += amount;
  }
}
```

**Python**

```python
class Account:
    def __init__(self) -> None:
        self._balance = 0      # private by convention

    def deposit(self, amount: int) -> None:
        self._balance += amount
```

JavaScript `#fields` are truly private. Python has no real privacy. A single underscore means "internal, don't touch". A double underscore (`self.__balance`) triggers name mangling to avoid clashes in subclasses, but it is still reachable.

## 38: How do getters and setters translate?

**Node.js**

```js
class Temperature {
  #celsius = 0;
  get fahrenheit() {
    return this.#celsius * 1.8 + 32;
  }
  set fahrenheit(f) {
    this.#celsius = (f - 32) / 1.8;
  }
}
```

**Python**

```python
class Temperature:
    def __init__(self) -> None:
        self._celsius = 0.0

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, f: float) -> None:
        self._celsius = (f - 32) / 1.8
```

`@property` turns a method into a read-only attribute, and `@<name>.setter` adds the setter. For cached computed values use `functools.cached_property`.

## 39: How do static methods translate?

**Node.js**

```js
class User {
  static fromJSON(json) {
    return new User(json.name);
  }
  static count = 0;
}
```

**Python**

```python
class User:
    count = 0   # class attribute

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def from_json(cls, data: dict) -> "User":
        return cls(data["name"])

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name.strip())
```

Use `@classmethod` for alternative constructors. It receives the class (`cls`), so subclasses get instances of themselves. Use `@staticmethod` for plain helpers that need neither the class nor an instance.

## 40: How do inheritance and super translate?

**Node.js**

```js
class Admin extends User {
  constructor(name, email, level) {
    super(name, email);
    this.level = level;
  }
  greet() {
    return `${super.greet()} (admin)`;
  }
}
```

**Python**

```python
class Admin(User):
    def __init__(self, name: str, email: str, level: int) -> None:
        super().__init__(name, email)
        self.level = level

    def greet(self) -> str:
        return f"{super().greet()} (admin)"
```

Python supports multiple inheritance (`class A(B, C)`), and `super()` follows the method resolution order (`A.__mro__`). In practice, keep to single inheritance plus small mixins.

## 41: How do TypeScript interfaces translate?

**Node.js**

```ts
interface Notifier {
  send(to: string, message: string): Promise<void>;
}

class EmailNotifier implements Notifier {
  async send(to: string, message: string) {}
}
```

**Python**

```python
from typing import Protocol

class Notifier(Protocol):
    async def send(self, to: str, message: str) -> None: ...

class EmailNotifier:            # no need to inherit
    async def send(self, to: str, message: str) -> None:
        ...

def notify(n: Notifier) -> None: ...
notify(EmailNotifier())          # type checker accepts it
```

`Protocol` gives structural typing, the same "if it has the right shape, it fits" rule as TypeScript. Use `abc.ABC` with `@abstractmethod` when you want a base class that refuses to be instantiated until all methods are implemented.

## 42: How do enums translate?

**Node.js**

```ts
enum Status {
  Active = "active",
  Banned = "banned",
}
// or the more common union:
type Role = "admin" | "user";
```

**Python**

```python
from enum import StrEnum
from typing import Literal

class Status(StrEnum):
    ACTIVE = "active"
    BANNED = "banned"

Role = Literal["admin", "user"]

Status("active") is Status.ACTIVE   # True
Status.ACTIVE == "active"           # True, StrEnum compares as str
```

`StrEnum` (Python 3.11+) members are real strings, which keeps JSON output the same. Use `Literal` where TypeScript used a string union. Pydantic and FastAPI validate both.

## 43: How do TypeScript types translate to Python type hints?

**Node.js**

```ts
function total(prices: number[], tax?: number): number {
  return prices.reduce((a, b) => a + b, 0) * (1 + (tax ?? 0));
}
```

**Python**

```python
def total(prices: list[float], tax: float | None = None) -> float:
    return sum(prices) * (1 + (tax or 0))
```

Python type hints look similar but have one big difference: the interpreter ignores them at runtime. They are checked by tools like mypy or pyright, and used by libraries like Pydantic and FastAPI. Wrong types will not stop the program from running.

## 44: What replaces tsc for type checking?

**Node.js**

```bash
npx tsc --noEmit
```

**Python**

```bash
uv add --dev mypy
uv run mypy src/
# or pyright, which is what the VS Code Pylance extension uses
uvx pyright
```

Python needs no build step, so the checker only checks. Configure it in `pyproject.toml` (`[tool.mypy] strict = true`). Newer, faster checkers such as Astral's `ty` and Meta's Pyrefly are also available.

## 45: How do union and optional types translate?

**Node.js**

```ts
let id: string | number;
let nickname: string | null = null;
function find(id: string): User | undefined {}
```

**Python**

```python
user_id: str | int
nickname: str | None = None
def find(user_id: str) -> User | None: ...
```

The `X | Y` syntax works since Python 3.10. Older code writes `Union[str, int]` and `Optional[str]` from the `typing` module. Since there is no `undefined`, both `T | null` and `T | undefined` become `T | None`.

## 46: How do generic functions translate?

**Node.js**

```ts
function first<T>(items: T[]): T | undefined {
  return items[0];
}
```

**Python**

```python
def first[T](items: list[T]) -> T | None:   # Python 3.12+ syntax
    return items[0] if items else None

# older style
from typing import TypeVar
T = TypeVar("T")
def first_old(items: list[T]) -> T | None: ...
```

Python 3.12 added the bracket syntax for generic functions and classes (`class Box[T]:`), which reads almost the same as TypeScript.

## 47: How do object shape types translate?

**Node.js**

```ts
type User = {
  id: number;
  name: string;
  email?: string;
};
```

**Python**

```python
from dataclasses import dataclass
from typing import NotRequired, TypedDict

class UserDict(TypedDict):        # a typed plain dict
    id: int
    name: str
    email: NotRequired[str]

@dataclass
class User:                       # a real class with attribute access
    id: int
    name: str
    email: str | None = None
```

Use `TypedDict` when the data stays a dict (for example JSON you pass through). Use a `dataclass` for internal objects. Use a Pydantic `BaseModel` when the data comes from outside and must be validated.

## 48: What are dataclasses and why use them instead of plain objects?

**Node.js**

```js
const point = { x: 1, y: 2 };
const moved = { ...point, x: 5 };
```

**Python**

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(1, 2)
moved = replace(point, x=5)
print(point)            # Point(x=1, y=2)
point == Point(1, 2)    # True, compared by value
```

A dataclass generates `__init__`, `__repr__` and `__eq__` from the field list. `frozen=True` makes it immutable and hashable. It replaces the many small object literals JavaScript code passes around.

## 49: How do JSON.parse and JSON.stringify translate?

**Node.js**

```js
const data = JSON.parse('{"name":"Ana","tags":["a"]}');
const text = JSON.stringify(data, null, 2);
```

**Python**

```python
import json

data = json.loads('{"name": "Ana", "tags": ["a"]}')
text = json.dumps(data, indent=2)
compact = json.dumps(data, separators=(",", ":"))  # same as JSON.stringify(data)
```

`json.dumps` adds spaces after `,` and `:` by default, so its output differs from `JSON.stringify`. It also fails on `datetime`, `Decimal` and custom classes unless you pass `default=str` or use Pydantic's `model_dump_json()`. Use `json.load`/`json.dump` (no `s`) for files.

## 50: How does Date translate?

**Node.js**

```js
const now = new Date();
const iso = now.toISOString();
const tomorrow = new Date(Date.now() + 24 * 60 * 60 * 1000);
```

**Python**

```python
from datetime import datetime, timedelta, UTC

now = datetime.now(UTC)
iso = now.isoformat()            # 2026-11-24T10:00:00.123456+00:00
tomorrow = now + timedelta(days=1)
```

Always create timezone-aware datetimes with `datetime.now(UTC)`. `datetime.utcnow()` is deprecated because it returns a "naive" datetime with no timezone. Python's `isoformat()` uses microseconds and `+00:00`, while JavaScript prints milliseconds and `Z`, which matters if clients parse the exact string.

## 51: How do Math functions and rounding translate?

**Node.js**

```js
Math.round(2.5); // 3
Math.round(-2.5); // -2
Math.floor(2.7); // 2
Math.max(1, 5, 3); // 5
(3.14159).toFixed(2); // "3.14" (string)
```

**Python**

```python
import math

round(2.5)        # 2, banker's rounding (round half to even)
round(3.5)        # 4
math.floor(2.7)   # 2
max(1, 5, 3)      # 5
f"{3.14159:.2f}"  # "3.14"
```

Python's `round()` rounds halves to the nearest even number, which differs from `Math.round`. For money, use `Decimal` with `quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` so the results are exact and predictable.

## 52: How do common string methods translate?

**Node.js**

```js
s.trim();
s.toUpperCase();
s.includes("x");
s.startsWith("a");
s.split(",");
s.replaceAll("a", "b");
s.padStart(5, "0");
```

**Python**

```python
s.strip()
s.upper()
"x" in s
s.startswith("a")
s.split(",")
s.replace("a", "b")     # replaces all by default
s.rjust(5, "0")         # or s.zfill(5) for numbers
```

Note the naming: Python methods are lowercase without camelCase (`startswith`, not `startsWith`). Python's `replace` replaces every match unless you pass a count.

## 53: How do regular expressions translate?

**Node.js**

```js
const re = /(?<year>\d{4})-(?<month>\d{2})/;
const m = "2026-11".match(re);
m?.groups.year;
"a1b2".replace(/\d/g, "#");
```

**Python**

```python
import re

pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})")
m = pattern.search("2026-11")
if m:
    m.group("year")
re.sub(r"\d", "#", "a1b2")   # replaces all by default
```

Python writes named groups as `(?P<name>...)` and backreferences as `(?P=name)`. Use raw strings (`r"..."`) so backslashes are not escapes. `re.match` only matches at the start, `re.search` matches anywhere, and `re.fullmatch` matches the whole string.

## 54: How does try/catch translate?

**Node.js**

```js
try {
  const data = JSON.parse(text);
} catch (err) {
  if (err instanceof SyntaxError) console.error("Bad JSON", err.message);
  else throw err;
}
```

**Python**

```python
import json

try:
    data = json.loads(text)
except json.JSONDecodeError as err:
    print("Bad JSON", err)
```

Python catches by exception type in each `except` clause, so you don't need an `instanceof` chain. Exceptions you don't list keep propagating. Avoid a bare `except:`, which also catches `KeyboardInterrupt` and `SystemExit`.

## 55: How do custom errors translate?

**Node.js**

```js
class NotFoundError extends Error {
  constructor(resource) {
    super(`${resource} not found`);
    this.name = "NotFoundError";
  }
}
throw new NotFoundError("User");
```

**Python**

```python
class NotFoundError(Exception):
    def __init__(self, resource: str) -> None:
        super().__init__(f"{resource} not found")
        self.resource = resource

raise NotFoundError("User")
```

Inherit from `Exception`, not `BaseException`. Python uses `raise` instead of `throw`, and the class name already appears in tracebacks, so you don't set a `name` field.

## 56: How do finally and else work in Python's try?

**Node.js**

```js
try {
  const conn = await connect();
  await work(conn);
} catch (err) {
  console.error(err);
} finally {
  await cleanup();
}
```

**Python**

```python
try:
    conn = await connect()
except ConnectionError as err:
    print(err)
else:
    await work(conn)     # runs only if no exception was raised
finally:
    await cleanup()
```

`finally` works the same in both. Python adds `else`, which runs only when the `try` block succeeded. It keeps the `try` block small, so you don't accidentally catch errors from the follow-up code.

## 57: How does console.log translate?

**Node.js**

```js
console.log("User", user);
console.error("Failed", err);
console.table(rows);
```

**Python**

```python
import logging
import sys

print("User", user)
print("Failed", err, file=sys.stderr)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info("User %s", user)
log.exception("Failed")    # inside except: logs the traceback too
```

`print` is fine for scripts. For services, use the `logging` module: it has levels, per-module loggers and handlers. `logging` formats lazily with `%s` arguments, so expensive formatting is skipped when the level is disabled.

## 58: How does process.env translate?

**Node.js**

```js
const port = Number(process.env.PORT ?? 3000);
const apiKey = process.env.API_KEY;
if (!apiKey) throw new Error("API_KEY is required");
```

**Python**

```python
import os

port = int(os.environ.get("PORT", "3000"))
api_key = os.environ["API_KEY"]   # raises KeyError if missing
api_key = os.getenv("API_KEY")    # returns None if missing
```

Environment values are always strings in both languages, so convert them yourself. For larger apps, use `pydantic-settings`, which reads, converts and validates all settings in one class.

## 59: How do .env files translate?

**Node.js**

```bash
node --env-file=.env index.js    # built in since Node 20.6
```

```js
process.loadEnvFile(); // or load it in code (Node 21.7+)
```

**Python**

```python
# uv add python-dotenv
from dotenv import load_dotenv

load_dotenv()   # reads .env into os.environ, does not override existing vars
```

```bash
uv run --env-file .env main.py   # uv can load it too
```

Python has no built-in `.env` loader, so use `python-dotenv` or let `pydantic-settings` read the file with `env_file=".env"`.

## 60: How does process.argv translate?

**Node.js**

```js
// node script.js input.csv --verbose
const [, , file, ...flags] = process.argv;
```

**Python**

```python
# python script.py input.csv --verbose
import sys

file, *flags = sys.argv[1:]
```

`process.argv` starts with the Node binary and the script path. `sys.argv` starts with only the script path, so user arguments begin at index 1 instead of 2.

## 61: How do exit codes translate?

**Node.js**

```js
if (!ok) {
  console.error("Failed");
  process.exit(1);
}
process.exitCode = 0;
```

**Python**

```python
import sys

if not ok:
    sys.exit("Failed")   # prints to stderr and exits with code 1
sys.exit(0)
```

`sys.exit()` raises a `SystemExit` exception, so `finally` blocks and context managers still run. An uncaught exception exits with code 1 in both runtimes.

## 62: How do you read a file?

**Node.js**

```js
import { readFile } from "node:fs/promises";

const text = await readFile("config.json", "utf8");
```

**Python**

```python
from pathlib import Path

text = Path("config.json").read_text(encoding="utf-8")

with open("config.json", encoding="utf-8") as f:
    text = f.read()
```

Python file I/O is synchronous, which is fine for scripts and sync servers. Inside async code, small reads at startup are fine, but for large or frequent reads use `asyncio.to_thread(path.read_text)` or a library like `aiofiles` so the event loop is not blocked.

## 63: How do you write a file?

**Node.js**

```js
import { writeFile, appendFile } from "node:fs/promises";

await writeFile("out.txt", "hello\n", "utf8");
await appendFile("log.txt", "line\n");
```

**Python**

```python
from pathlib import Path

Path("out.txt").write_text("hello\n", encoding="utf-8")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("line\n")
```

The `with` block closes the file even if an error happens, like a `try/finally`. Pass `encoding="utf-8"` explicitly. Python 3.15 makes UTF-8 the default, but older versions use the system locale.

## 64: How do you check if a file exists?

**Node.js**

```js
import { existsSync } from "node:fs";
import { access } from "node:fs/promises";

if (existsSync("config.json")) {
}
```

**Python**

```python
from pathlib import Path

path = Path("config.json")
if path.exists():
    ...
path.is_file()
path.is_dir()
```

In both languages, checking before opening can race with other processes. It is often better to just open the file and handle `FileNotFoundError` (Node's `ENOENT`).

## 65: How do you list a directory or glob files?

**Node.js**

```js
import { readdir, glob } from "node:fs/promises";

const names = await readdir("src");
for await (const file of glob("src/**/*.ts")) console.log(file); // Node 22+
```

**Python**

```python
from pathlib import Path

names = [p.name for p in Path("src").iterdir()]
for file in Path("src").rglob("*.py"):
    print(file)
```

`Path.glob` and `Path.rglob` (recursive) return `Path` objects, so you can call `.read_text()`, `.stem` or `.suffix` on each result directly.

## 66: How does the path module translate?

**Node.js**

```js
import path from "node:path";

path.join("a", "b", "c.txt");
path.basename("/x/y/file.txt"); // file.txt
path.extname("file.txt"); // .txt
path.resolve("rel");
```

**Python**

```python
from pathlib import Path

Path("a") / "b" / "c.txt"
Path("/x/y/file.txt").name       # file.txt
Path("file.txt").suffix          # .txt
Path("file.txt").stem            # file
Path("rel").resolve()
```

`pathlib` is the modern, object-based API. Older code uses `os.path.join` and friends, which work on plain strings like Node's `path`.

## 67: How do you create directories?

**Node.js**

```js
import { mkdir, rm } from "node:fs/promises";

await mkdir("data/cache", { recursive: true });
await rm("tmp", { recursive: true, force: true });
```

**Python**

```python
import shutil
from pathlib import Path

Path("data/cache").mkdir(parents=True, exist_ok=True)
shutil.rmtree("tmp", ignore_errors=True)
```

`parents=True` matches `recursive: true`, and `exist_ok=True` stops it from failing when the folder already exists. Use `shutil` for copying and removing whole trees.

## 68: How do Promises and async/await translate?

**Node.js**

```js
async function getUser(id) {
  const res = await fetch(`https://api.example.com/users/${id}`);
  return res.json();
}
```

**Python**

```python
import httpx

async def get_user(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        res = await client.get(f"https://api.example.com/users/{user_id}")
        return res.json()
```

The syntax looks the same, but the behavior differs. A JavaScript Promise starts running as soon as you call the function. A Python coroutine does nothing until it is awaited or wrapped in a task. Forgetting `await` in Python means the work never happens, and you get a "coroutine was never awaited" warning.

## 69: How do you run async code from the top level?

**Node.js**

```js
// ES modules support top-level await
const data = await loadData();
console.log(data);
```

**Python**

```python
import asyncio

async def main() -> None:
    data = await load_data()
    print(data)

asyncio.run(main())
```

Node.js always has an event loop running. Python starts one explicitly with `asyncio.run()`, which creates the loop, runs the coroutine until it finishes, and closes the loop. Call it once, at the program's entry point.

## 70: How do setTimeout and sleep translate?

**Node.js**

```js
import { setTimeout as sleep } from "node:timers/promises";

await sleep(1000);
setTimeout(() => console.log("later"), 1000);
```

**Python**

```python
import asyncio
import time

await asyncio.sleep(1)       # seconds, not milliseconds
time.sleep(1)                # blocks the whole thread

loop = asyncio.get_running_loop()
loop.call_later(1, lambda: print("later"))
```

Python uses seconds. Never call `time.sleep` inside `async def` code: it freezes the event loop for everyone, just like a busy loop would in Node.js.

## 71: How does Promise.all translate?

**Node.js**

```js
const [user, orders] = await Promise.all([getUser(id), getOrders(id)]);
```

**Python**

```python
import asyncio

user, orders = await asyncio.gather(get_user(uid), get_orders(uid))

# Python 3.11+: structured concurrency
async with asyncio.TaskGroup() as tg:
    t1 = tg.create_task(get_user(uid))
    t2 = tg.create_task(get_orders(uid))
user, orders = t1.result(), t2.result()
```

`gather` returns results in order, like `Promise.all`. `TaskGroup` is safer: if one task fails, it cancels the others and raises an `ExceptionGroup`, while `Promise.all` leaves the other promises running.

## 72: How do Node-style callbacks translate?

**Node.js**

```js
import fs from "node:fs";

fs.readFile("a.txt", "utf8", (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
```

**Python**

```python
try:
    with open("a.txt", encoding="utf-8") as f:
        print(f.read())
except OSError as err:
    print(err)
```

Python never used the error-first callback style. Errors are exceptions, and you write either plain blocking code or `async`/`await` code. When translating callback APIs, convert them to direct calls or coroutines rather than copying the callbacks.

## 73: How do you start a basic HTTP server without a framework?

**Node.js**

```js
import { createServer } from "node:http";

createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello");
}).listen(3000);
```

**Python**

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello")

HTTPServer(("", 3000), Handler).serve_forever()
```

Python's `http.server` is fine for demos, but its own docs say it is not for production. Real Python services run on a production server like Uvicorn or Gunicorn behind a framework.

## 74: How does an Express hello world translate to FastAPI?

**Node.js**

```js
import express from "express";

const app = express();
app.use(express.json());
app.get("/hello", (req, res) => res.json({ message: "Hello" }));
app.listen(3000);
```

**Python**

```python
# uv add "fastapi[standard]"
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello() -> dict[str, str]:
    return {"message": "Hello"}
```

```bash
fastapi dev main.py          # dev server with reload on port 8000
fastapi run main.py          # production mode
```

FastAPI turns returned dicts and models into JSON automatically and generates OpenAPI docs at `/docs`. The app is a plain ASGI object, and a server like Uvicorn runs it.

## 75: How does an Express hello world translate to Flask?

**Node.js**

```js
app.get("/hello", (req, res) => res.json({ message: "Hello" }));
```

**Python**

```python
# uv add flask
from flask import Flask

app = Flask(__name__)

@app.get("/hello")
def hello():
    return {"message": "Hello"}
```

```bash
flask --app main run --debug
```

Flask is the closest to Express in spirit: small, synchronous and unopinionated. It is a WSGI app, so in production you run it with Gunicorn, which handles concurrency with worker processes and threads.

## 76: How do route parameters translate?

**Node.js**

```js
app.get("/users/:id", (req, res) => {
  const id = Number(req.params.id);
  res.json({ id });
});
```

**Python**

```python
# FastAPI
@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"id": user_id}

# Flask
@app.get("/users/<int:user_id>")
def get_user_flask(user_id: int):
    return {"id": user_id}
```

FastAPI converts and validates the parameter from the type hint. A non-number like `/users/abc` returns a 422 error automatically, so you don't write `Number(...)` and `isNaN` checks.

## 77: How do query string parameters translate?

**Node.js**

```js
// GET /search?q=shoes&page=2
app.get("/search", (req, res) => {
  const q = req.query.q ?? "";
  const page = Number(req.query.page ?? 1);
  res.json({ q, page });
});
```

**Python**

```python
# FastAPI
@app.get("/search")
async def search(q: str = "", page: int = 1) -> dict:
    return {"q": q, "page": page}

# Flask
from flask import request

@app.get("/search")
def search_flask():
    q = request.args.get("q", "")
    page = request.args.get("page", 1, type=int)
    return {"q": q, "page": page}
```

In FastAPI, any function parameter that is not in the path becomes a query parameter. Defaults make it optional, and the type hint handles conversion.

## 78: How do you read a JSON request body?

**Node.js**

```js
app.use(express.json());
app.post("/users", (req, res) => {
  const { name, email } = req.body;
  res.status(201).json({ name, email });
});
```

**Python**

```python
from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    name: str
    email: EmailStr     # needs the email-validator extra

@app.post("/users", status_code=201)
async def create_user(user: UserIn) -> UserIn:
    return user
```

FastAPI reads the body into the Pydantic model and validates it. In Flask, use `request.get_json()` and validate it yourself, for example with `UserIn.model_validate(request.get_json())`.

## 79: How do you set status codes?

**Node.js**

```js
res.status(201).json(user);
res.sendStatus(204);
res.status(404).json({ error: "Not found" });
```

**Python**

```python
from fastapi import HTTPException, Response, status

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item() -> dict: ...

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int) -> None: ...

@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    raise HTTPException(status_code=404, detail="Not found")
```

In FastAPI you set the default status in the decorator and raise `HTTPException` for errors. In Flask you return a tuple: `return {"error": "Not found"}, 404`.

## 80: How do you set response headers?

**Node.js**

```js
res.set("Cache-Control", "no-store");
res.set("X-Request-Id", id);
res.json(data);
```

**Python**

```python
from fastapi import Response

@app.get("/data")
async def data(response: Response) -> dict:
    response.headers["Cache-Control"] = "no-store"
    return {"ok": True}

# Flask
@app.get("/data")
def data_flask():
    return {"ok": True}, 200, {"Cache-Control": "no-store"}
```

In FastAPI, declare a `Response` parameter to change headers or cookies while still returning a normal dict. You can also return a `JSONResponse(content, headers={...})` directly.

## 81: How does basic middleware translate?

**Node.js**

```js
app.use((req, res, next) => {
  const start = Date.now();
  res.on("finish", () => {
    console.log(req.method, req.url, Date.now() - start, "ms");
  });
  next();
});
```

**Python**

```python
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    print(request.method, request.url.path, f"{ms:.1f} ms")
    return response
```

FastAPI middleware wraps the handler: code before `call_next` runs on the way in, code after it runs on the way out. Flask uses `@app.before_request` and `@app.after_request` hooks instead.

## 82: How do you serve static files?

**Node.js**

```js
app.use("/static", express.static("public"));
```

**Python**

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="public"), name="static")

# Flask serves ./static at /static automatically
app = Flask(__name__, static_folder="public", static_url_path="/static")
```

In production, serve static files from Nginx or a CDN in both stacks. Django collects them with `collectstatic`, and many teams use WhiteNoise to serve them.

## 83: How does Express Router translate?

**Node.js**

```js
// users.js
import { Router } from "express";
export const users = Router();
users.get("/", listUsers);

// app.js
app.use("/users", users);
```

**Python**

```python
# users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users() -> list[dict]: ...

# main.py
from app import users
app.include_router(users.router)
```

Flask's equivalent is a `Blueprint`, registered with `app.register_blueprint(bp, url_prefix="/users")`. Django groups routes per app in `urls.py` and joins them with `include()`.

## 84: How do you run a dev server with auto-reload?

**Node.js**

```bash
node --watch src/server.js
# or: npx nodemon src/server.js, npx tsx watch src/server.ts
```

**Python**

```bash
fastapi dev app/main.py
uvicorn app.main:app --reload
flask --app app run --debug
python manage.py runserver      # Django
```

`app.main:app` means "the `app` object inside the `app/main.py` module". This `module:object` format is how most Python servers find your application.

## 85: How does fetch translate?

**Node.js**

```js
const res = await fetch("https://api.example.com/users/1");
if (!res.ok) throw new Error(`HTTP ${res.status}`);
const user = await res.json();
```

**Python**

```python
import httpx

# async
async with httpx.AsyncClient() as client:
    res = await client.get("https://api.example.com/users/1")
    res.raise_for_status()
    user = res.json()

# sync
res = httpx.get("https://api.example.com/users/1")
```

`httpx` supports both sync and async with the same API. The older `requests` library is sync only, so it must not be used inside `async def` code. Like `fetch`, a 404 is not an error until you call `raise_for_status()`.

## 86: How do you send a POST request with JSON?

**Node.js**

```js
const res = await fetch("https://api.example.com/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  },
  body: JSON.stringify({ name: "Ana" }),
});
```

**Python**

```python
async with httpx.AsyncClient() as client:
    res = await client.post(
        "https://api.example.com/users",
        json={"name": "Ana"},
        headers={"Authorization": f"Bearer {token}"},
    )
```

The `json=` argument serializes the body and sets `Content-Type` for you. Use `data=` for form fields and `files=` for multipart uploads.

## 87: How does a simple unit test translate?

**Node.js**

```js
// sum.test.js
import { test, expect } from "vitest";
import { sum } from "./sum.js";

test("adds numbers", () => {
  expect(sum(1, 2)).toBe(3);
});
```

**Python**

```python
# test_sum.py
from sum_utils import add

def test_adds_numbers() -> None:
    assert add(1, 2) == 3
```

```bash
uv run pytest
```

pytest finds files named `test_*.py` and functions named `test_*`. It uses the plain `assert` statement and rewrites it to show both sides of a failed comparison, so you don't need a matcher library.

## 88: How do common Jest matchers translate to pytest?

**Node.js**

```js
expect(value).toBe(3);
expect(obj).toEqual({ a: 1 });
expect(list).toContain("x");
expect(fn).toThrow("bad input");
expect(num).toBeCloseTo(0.3);
```

**Python**

```python
import pytest

assert value == 3
assert obj == {"a": 1}             # == compares dicts deeply
assert "x" in items
with pytest.raises(ValueError, match="bad input"):
    fn()
assert num == pytest.approx(0.3)
```

`pytest.raises` is a context manager, and `match` is a regex checked against the error message.

## 89: How do you test async functions?

**Node.js**

```js
test("loads user", async () => {
  const user = await loadUser(1);
  expect(user.id).toBe(1);
});
```

**Python**

```python
# uv add --dev pytest-asyncio
import pytest

@pytest.mark.asyncio
async def test_loads_user() -> None:
    user = await load_user(1)
    assert user.id == 1
```

pytest cannot run coroutines by itself. Use the `pytest-asyncio` plugin (set `asyncio_mode = "auto"` in config to skip the marker), or the `anyio` plugin that comes with FastAPI's dependencies (`@pytest.mark.anyio`).

## 90: How do test file conventions translate?

**Node.js**

```text
src/
  user.service.ts
  user.service.test.ts
```

**Python**

```text
src/app/
  user_service.py
tests/
  conftest.py
  test_user_service.py
```

Python projects usually keep tests in a separate `tests/` folder. `conftest.py` holds shared fixtures that pytest loads automatically, like a global `setupFiles` in Jest.

## 91: What replaces ESLint and Prettier?

**Node.js**

```bash
npx eslint .
npx prettier --write .
```

**Python**

```bash
uv add --dev ruff
uv run ruff check . --fix
uv run ruff format .
```

```toml
[tool.ruff]
line-length = 100
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

Ruff does both linting and formatting and is very fast. Its formatter matches Black's style, so most Python code looks the same.

## 92: What replaces nvm?

**Node.js**

```bash
nvm install 24
nvm use 24
```

**Python**

```bash
uv python install 3.14
uv python pin 3.14     # writes .python-version
# alternative: pyenv install 3.14 && pyenv local 3.14
```

uv downloads Python builds on demand and uses the version in `.python-version`, the same way nvm and fnm use `.nvmrc`.

## 93: How do you pin the runtime version?

**Node.js**

```json
{ "engines": { "node": ">=24" } }
```

**Python**

```toml
[project]
requires-python = ">=3.13"
```

```text
# .python-version
3.14
```

`requires-python` says which versions the project supports. `.python-version` picks the exact one used for local development, like `.nvmrc`.

## 94: How does the REPL translate?

**Node.js**

```bash
node
> [1, 2, 3].map((x) => x * 2)
```

**Python**

```bash
python
>>> [x * 2 for x in [1, 2, 3]]
[2, 4, 6]
>>> help(str.split)
```

Python 3.13+ ships a better REPL with colors and multi-line editing. `help()` and `dir()` show docs and attributes for any object. IPython is a popular richer shell.

## 95: How do JSDoc comments translate?

**Node.js**

```js
/**
 * Adds two numbers.
 * @param {number} a
 * @param {number} b
 * @returns {number}
 */
function add(a, b) {
  return a + b;
}
```

**Python**

```python
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.
    """
    return a + b
```

A docstring is the first string inside a function, class or module. It is stored on the object (`add.__doc__`) and shown by `help()` and IDEs. Types go in the hints, not in the comment.

## 96: How do naming conventions differ?

**Node.js**

```js
const maxRetries = 3;
function getUserById(userId) {}
class UserService {}
const API_URL = "...";
// files: user-service.ts or userService.ts
```

**Python**

```python
max_retries = 3
def get_user_by_id(user_id): ...
class UserService: ...
API_URL = "..."
# files: user_service.py
```

Python uses `snake_case` for variables, functions and modules, `PascalCase` for classes, and `UPPER_CASE` for constants (PEP 8). Module file names cannot have hyphens if you want to import them.

## 97: How do code blocks and indentation work?

**Node.js**

```js
if (user) {
  if (user.isAdmin) {
    grantAccess();
  }
}
```

**Python**

```python
if user:
    if user.is_admin:
        grant_access()
```

Python uses indentation instead of braces, so indentation is part of the syntax. Use 4 spaces. A block that should do nothing needs `pass` (or `...`), because an empty block is a syntax error.

## 98: What about semicolons and long lines?

**Node.js**

```js
const total = price * quantity + shipping - discount;
const result = await client.query("SELECT * FROM users WHERE active = $1", [
  true,
]);
```

**Python**

```python
total = price * quantity + shipping - discount
result = await conn.fetch(
    "SELECT * FROM users WHERE active = $1",
    True,
)
```

Python needs no semicolons. A statement can span many lines as long as it is inside `()`, `[]` or `{}`. Avoid backslash line continuation. The trailing comma is fine and keeps diffs small.

## 99: How do number formatting functions translate?

**Node.js**

```js
(1234.5).toFixed(2); // "1234.50"
(1234567).toLocaleString("en-US"); // "1,234,567"
(0.256).toLocaleString("en-US", { style: "percent" }); // "26%"
(255).toString(16); // "ff"
```

**Python**

```python
f"{1234.5:.2f}"     # "1234.50"
f"{1234567:,}"      # "1,234,567"
f"{0.256:.0%}"      # "26%"
format(255, "x")    # "ff"
hex(255)            # "0xff"
```

The format spec mini-language after `:` covers width, padding, precision, separators and bases. For locale-aware currency formatting, use the `babel` library.

## 100: How does sorting translate?

**Node.js**

```js
[10, 9, 1].sort(); // [1, 10, 9], sorts as strings!
[10, 9, 1].sort((a, b) => a - b); // [1, 9, 10]
users.sort((a, b) => a.name.localeCompare(b.name));
```

**Python**

```python
sorted([10, 9, 1])                       # [1, 9, 10]
users.sort(key=lambda u: u.name)         # in place
newest = sorted(users, key=lambda u: u.created_at, reverse=True)
```

Python sorts numbers as numbers by default and uses a `key` function instead of a comparator. `sorted()` returns a new list, `.sort()` changes the list in place. Both are stable.

## 101: How do you copy objects and arrays?

**Node.js**

```js
const shallow = { ...user };
const listCopy = [...items];
const deep = structuredClone(user);
```

**Python**

```python
import copy

shallow = dict(user)          # or user.copy() or {**user}
list_copy = list(items)       # or items[:] or items.copy()
deep = copy.deepcopy(user)
```

Shallow copies share nested objects in both languages. `copy.deepcopy` works on almost any Python object, including class instances, which goes further than `structuredClone`.

## 102: How do typeof and instanceof translate?

**Node.js**

```js
typeof x === "string";
Array.isArray(x);
x instanceof Date;
```

**Python**

```python
from datetime import datetime

isinstance(x, str)
isinstance(x, list)
isinstance(x, datetime)
isinstance(x, (int, float))   # any of several types
type(x) is int                # exact type, rarely needed
```

`isinstance` respects inheritance, so prefer it over `type(x) == ...`. Note that `bool` is a subclass of `int` in Python, so `isinstance(True, int)` is `True`.

## 103: How does parsing numbers from strings translate?

**Node.js**

```js
parseInt("42px", 10); // 42
Number("42px"); // NaN
Number.isNaN(Number("abc")); // true
parseFloat("3.14");
```

**Python**

```python
int("42")        # 42
int("42px")      # ValueError
float("3.14")
try:
    n = int(value)
except ValueError:
    n = None
```

Python does not return `NaN` for bad input. It raises `ValueError`, so wrap conversions in `try`. `int()` also does not stop at the first bad character the way `parseInt` does.

## 104: How do includes and indexOf translate?

**Node.js**

```js
items.includes("a");
items.indexOf("a"); // -1 if missing
items.find((u) => u.id === 3);
items.some((u) => u.admin);
items.every((u) => u.active);
```

**Python**

```python
"a" in items
items.index("a")    # raises ValueError if missing
next((u for u in items if u.id == 3), None)
any(u.admin for u in items)
all(u.active for u in items)
```

`in` works on lists, tuples, sets, dict keys and substrings. On a set or dict it is O(1). `next(..., None)` is the idiomatic `find`.

## 105: How do Object.keys and Object.entries translate?

**Node.js**

```js
Object.keys(obj);
Object.values(obj);
Object.entries(obj);
Object.fromEntries(pairs);
```

**Python**

```python
list(obj.keys())
list(obj.values())
list(obj.items())
dict(pairs)
{k: v * 2 for k, v in obj.items()}   # dict comprehension
```

`keys()`, `values()` and `items()` return live views, not lists. Wrap them in `list()` when you need indexing or a snapshot before changing the dict.

## 106: How does Object.assign translate?

**Node.js**

```js
const merged = Object.assign({}, defaults, overrides);
Object.assign(target, { extra: 1 });
```

**Python**

```python
merged = defaults | overrides      # new dict
target.update({"extra": 1})        # in place
target |= {"extra": 1}             # also in place
```

Later keys win in both. Neither does a deep merge, so nested dicts are replaced, not combined.

## 107: How do split and join translate?

**Node.js**

```js
"a,b,c".split(",");
["a", "b"].join("-");
[..."hello"];
```

**Python**

```python
"a,b,c".split(",")
"-".join(["a", "b"])       # join is a string method
list("hello")
"-".join(str(n) for n in [1, 2])   # join needs strings
```

`join` lives on the separator string in Python. It raises `TypeError` for non-strings instead of converting them, so convert numbers first.

## 108: How does array slicing translate?

**Node.js**

```js
items.slice(1, 3);
items.slice(-2);
items.toReversed();
items.splice(1, 2);
```

**Python**

```python
items[1:3]
items[-2:]
items[::-1]          # reversed copy
del items[1:3]       # remove in place
items[1:3] = []      # same
```

Slices work on lists, tuples and strings with the same `[start:stop:step]` syntax. They never raise for out-of-range indexes, like `slice()`.

## 109: How do you create ranges of numbers?

**Node.js**

```js
Array.from({ length: 5 }, (_, i) => i); // [0..4]
Array.from({ length: 5 }, (_, i) => i * 2);
new Array(3).fill(0);
```

**Python**

```python
list(range(5))                 # [0, 1, 2, 3, 4]
[i * 2 for i in range(5)]
[0] * 3                        # [0, 0, 0]
[[0] * 3 for _ in range(3)]    # 3x3 grid, each row a new list
```

`range` is lazy and uses almost no memory. Don't write `[[0] * 3] * 3` for a grid: that repeats the same inner list three times.

## 110: How do lodash-style helpers like zip and chunk translate?

**Node.js**

```js
import { zip, chunk } from "lodash-es";

zip([1, 2], ["a", "b"]); // [[1,"a"],[2,"b"]]
chunk([1, 2, 3, 4, 5], 2);
```

**Python**

```python
from itertools import batched   # Python 3.12+

list(zip([1, 2], ["a", "b"]))     # [(1, 'a'), (2, 'b')]
list(batched([1, 2, 3, 4, 5], 2))  # [(1, 2), (3, 4), (5,)]
zip([1, 2], ["a"], strict=True)    # raises if lengths differ (when consumed)
```

Much of lodash is built into Python: `zip`, `enumerate`, `sorted`, `min`/`max` with `key`, and the `itertools`, `functools` and `collections` modules.

## 111: How do random values and UUIDs translate?

**Node.js**

```js
Math.random();
crypto.randomUUID();
crypto.getRandomValues(new Uint8Array(16));
```

**Python**

```python
import random
import secrets
import uuid

random.random()
str(uuid.uuid4())
uuid.uuid7()                  # Python 3.14+, time-ordered
secrets.token_bytes(16)
secrets.token_urlsafe(32)     # for tokens and API keys
```

The `random` module is not safe for security. Use `secrets` for tokens, passwords and anything an attacker should not guess, the same way you'd use `crypto` instead of `Math.random` in Node.

## 112: How do you hash a string?

**Node.js**

```js
import { createHash, createHmac } from "node:crypto";

createHash("sha256").update("hello").digest("hex");
createHmac("sha256", secret).update(body).digest("hex");
```

**Python**

```python
import hashlib
import hmac

hashlib.sha256(b"hello").hexdigest()
hashlib.sha256("hello".encode()).hexdigest()
hmac.new(secret, body, hashlib.sha256).hexdigest()
```

Python hash functions take bytes, not strings, so call `.encode()` first. `secret` and `body` in the HMAC example must also be bytes.

## 113: How does base64 encoding translate?

**Node.js**

```js
Buffer.from("hello").toString("base64");
Buffer.from("aGVsbG8=", "base64").toString("utf8");
Buffer.from(data).toString("base64url");
```

**Python**

```python
import base64

base64.b64encode(b"hello").decode()          # "aGVsbG8="
base64.b64decode("aGVsbG8=").decode()        # "hello"
base64.urlsafe_b64encode(data).rstrip(b"=")  # Node's base64url drops padding
```

`b64encode` returns bytes, so `.decode()` turns it into a string. Node's `base64url` has no `=` padding, while Python's `urlsafe_b64encode` keeps it. Strip it if you must match.

## 114: How does Buffer translate?

**Node.js**

```js
const buf = Buffer.from("héllo", "utf8");
buf.length; // 6 bytes
buf.toString("hex");
Buffer.concat([a, b]);
```

**Python**

```python
buf = "héllo".encode("utf-8")   # bytes
len(buf)        # 6
buf.hex()
a + b           # concatenate bytes
mutable = bytearray(buf)
```

`bytes` is immutable, `bytearray` is mutable, and `memoryview` gives zero-copy slices. Python keeps text (`str`) and binary (`bytes`) strictly apart and will not mix them.

## 115: How does URL parsing translate?

**Node.js**

```js
const url = new URL("https://example.com/a?x=1&y=2");
url.hostname;
url.searchParams.get("x");
url.searchParams.set("page", "3");
```

**Python**

```python
from urllib.parse import urlparse, parse_qs, urlencode

url = urlparse("https://example.com/a?x=1&y=2")
url.hostname
parse_qs(url.query)["x"][0]      # values are lists
new_query = urlencode({"page": 3})

import httpx
httpx.URL("https://example.com/a?x=1").copy_merge_params({"page": 3})
```

`parse_qs` returns lists because a key may repeat. For building URLs with changing parameters, `httpx.URL` or `yarl.URL` are easier than raw `urllib`.

## 116: How does encodeURIComponent translate?

**Node.js**

```js
encodeURIComponent("a b&c"); // "a%20b%26c"
decodeURIComponent("a%20b");
```

**Python**

```python
from urllib.parse import quote, unquote, quote_plus

quote("a b&c", safe="")   # "a%20b%26c"
unquote("a%20b")
quote_plus("a b")         # "a+b", form style
```

`quote` keeps `/` unescaped by default. Pass `safe=""` to match `encodeURIComponent`.

## 117: How does setInterval translate?

**Node.js**

```js
const timer = setInterval(() => checkHealth(), 5000);
clearInterval(timer);
```

**Python**

```python
import asyncio

async def every(seconds: float) -> None:
    while True:
        await check_health()
        await asyncio.sleep(seconds)

task = asyncio.create_task(every(5))
task.cancel()   # like clearInterval
```

asyncio has no `setInterval`. A loop with `asyncio.sleep` inside a task does the same job. Keep a reference to the task: asyncio only holds a weak reference, so an unreferenced task can be garbage collected.

## 118: How does a basic EventEmitter translate?

**Node.js**

```js
import { EventEmitter } from "node:events";

const bus = new EventEmitter();
bus.on("user:created", (user) => sendWelcome(user));
bus.emit("user:created", { id: 1 });
```

**Python**

```python
from collections import defaultdict
from typing import Callable

class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable]] = defaultdict(list)

    def on(self, event: str, handler: Callable) -> None:
        self._handlers[event].append(handler)

    def emit(self, event: str, *args) -> None:
        for handler in self._handlers[event]:
            handler(*args)

bus = EventBus()
bus.on("user:created", send_welcome)
bus.emit("user:created", {"id": 1})
```

Python has no built-in event emitter. A small class like this is common, or use `blinker` (used by Flask) or `pyee`, which copies Node's API.

## 119: How do globals translate?

**Node.js**

```js
globalThis.appVersion = "1.0";
let counter = 0;
function inc() {
  counter++;
}
```

**Python**

```python
counter = 0

def inc() -> None:
    global counter
    counter += 1
```

In Python, assigning to a name inside a function creates a local variable. To change a module-level variable, declare it `global`. Better yet, avoid mutable globals and keep state in an object you pass around.

## 120: How do closures translate?

**Node.js**

```js
function makeCounter() {
  let count = 0;
  return () => ++count;
}
```

**Python**

```python
def make_counter():
    count = 0
    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment
```

Closures work the same way, but changing an outer variable needs `nonlocal`. Without it, `count += 1` raises `UnboundLocalError`.

## 121: Does Python have hoisting?

**Node.js**

```js
greet(); // works, function declarations are hoisted
function greet() {
  console.log("hi");
}
```

**Python**

```python
def main() -> None:
    greet()          # fine, greet exists by the time main runs

def greet() -> None:
    print("hi")

main()
```

Python has no hoisting. A `def` creates the function when that line runs, so calling it earlier at module level raises `NameError`. Functions can still call each other in any order because the call happens later, when everything is defined.

## 122: How does this translate to self?

**Node.js**

```js
class Counter {
  count = 0;
  increment() {
    this.count++;
  }
}
const c = new Counter();
const inc = c.increment;
inc(); // TypeError, this is undefined
```

**Python**

```python
class Counter:
    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> None:
        self.count += 1

c = Counter()
inc = c.increment
inc()   # works, the method stays bound to c
```

`self` is an explicit parameter, and methods taken from an instance stay bound to it. That removes the whole class of `.bind(this)` bugs you see in JavaScript.

## 123: How do module-level singletons translate?

**Node.js**

```js
// db.js
import pg from "pg";
export const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
```

**Python**

```python
# db.py
import os
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(os.environ["DATABASE_URL"])
```

Modules are cached after their first import in both runtimes, so a module-level object acts as a singleton. For async resources, many Python apps create them in the app's lifespan hook instead, so they are tied to the running event loop.

## 124: How do you print a stack trace?

**Node.js**

```js
try {
  risky();
} catch (err) {
  console.error(err.stack);
}
```

**Python**

```python
import logging
import traceback

try:
    risky()
except Exception:
    traceback.print_exc()
    logging.exception("risky failed")   # logs message plus traceback
```

Python tracebacks print the most recent call last, the opposite order of a JavaScript stack. Read Python errors from the bottom up.

## 125: How do assertions translate?

**Node.js**

```js
import assert from "node:assert/strict";

assert.equal(total, 10);
assert.deepEqual(result, { ok: true });
```

**Python**

```python
assert total == 10, f"expected 10, got {total}"
assert result == {"ok": True}
```

Python's `assert` statement is removed when Python runs with `-O`. Use it for tests and internal sanity checks, never for validating user input or security checks.

## 126: How does date formatting and parsing translate?

**Node.js**

```js
new Date("2026-11-24T10:00:00Z");
new Date().toISOString();
new Intl.DateTimeFormat("en-US", { dateStyle: "medium" }).format(new Date());
```

**Python**

```python
from datetime import datetime, UTC

datetime.fromisoformat("2026-11-24T10:00:00Z")   # "Z" accepted since 3.11
datetime.now(UTC).isoformat()
datetime.now(UTC).strftime("%b %d, %Y")          # "Nov 24, 2026"
datetime.strptime("24/11/2026", "%d/%m/%Y")
```

`strftime` and `strptime` use `%` codes for format and parse. For locale-aware output, use the `babel` library.

## 127: How do time zones translate?

**Node.js**

```js
new Date().toLocaleString("en-US", { timeZone: "Asia/Tbilisi" });
// Temporal is arriving in newer runtimes for real zone math
```

**Python**

```python
from datetime import datetime
from zoneinfo import ZoneInfo

now_tbilisi = datetime.now(ZoneInfo("Asia/Tbilisi"))
in_utc = now_tbilisi.astimezone(ZoneInfo("UTC"))
```

`zoneinfo` (Python 3.9+) uses the IANA time zone database. Store UTC in the database and convert to the user's zone only for display. On Windows or slim containers, add the `tzdata` package.

## 128: How do you measure elapsed time?

**Node.js**

```js
const start = performance.now();
await work();
console.log(`${(performance.now() - start).toFixed(1)} ms`);
```

**Python**

```python
import time

start = time.perf_counter()
await work()
print(f"{(time.perf_counter() - start) * 1000:.1f} ms")
```

`time.perf_counter()` returns seconds as a float from a monotonic clock. Don't use `time.time()` for durations, because the system clock can jump.

## 129: Why can Python sleep in normal code when Node.js cannot?

**Node.js**

```js
// No blocking sleep in normal code; you await a timer
await new Promise((r) => setTimeout(r, 1000));
```

**Python**

```python
import time

time.sleep(1)   # fine in sync code: Flask, Django, scripts, threads
```

Python's sync code runs in threads or processes, so blocking one thread does not freeze the server. Node.js has one main thread, so it avoids blocking calls. The rule flips inside Python async code: there, `time.sleep` blocks the event loop and you must use `await asyncio.sleep`.

## 130: How does child_process translate?

**Node.js**

```js
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const { stdout } = await promisify(execFile)("git", ["rev-parse", "HEAD"]);
```

**Python**

```python
import subprocess

result = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    capture_output=True,
    text=True,
    check=True,    # raise CalledProcessError on non-zero exit
)
print(result.stdout.strip())
```

Pass arguments as a list and avoid `shell=True`, the same reason you prefer `execFile` over `exec`: it stops shell injection.

## 131: How does the os module translate?

**Node.js**

```js
import os from "node:os";

os.cpus().length;
os.availableParallelism();
os.hostname();
os.tmpdir();
```

**Python**

```python
import os
import socket
import tempfile

os.cpu_count()
os.process_cpu_count()   # Python 3.13+, respects CPU affinity
socket.gethostname()
tempfile.gettempdir()
```

In containers, both runtimes may report the host's CPUs instead of the container's limit, so set worker counts from config rather than trusting the number blindly.

## 132: How do you read user input in a script?

**Node.js**

```js
import * as readline from "node:readline/promises";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const name = await rl.question("Name? ");
rl.close();
```

**Python**

```python
name = input("Name? ")

import getpass
password = getpass.getpass("Password: ")   # no echo
```

`input()` blocks until the user presses Enter, which is fine in a script.

## 133: How do you parse command-line options?

**Node.js**

```js
import { parseArgs } from "node:util";

const { values } = parseArgs({
  options: {
    port: { type: "string", default: "3000" },
    verbose: { type: "boolean" },
  },
});
```

**Python**

```python
import argparse

parser = argparse.ArgumentParser(description="Start the server")
parser.add_argument("--port", type=int, default=3000)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
print(args.port, args.verbose)
```

`argparse` converts types and generates `--help` automatically. For bigger CLIs, `Typer` and `Click` play the role of `commander` or `yargs`.

## 134: How do TextEncoder and TextDecoder translate?

**Node.js**

```js
const bytes = new TextEncoder().encode("hi");
const text = new TextDecoder().decode(bytes);
```

**Python**

```python
data = "hi".encode("utf-8")
text = data.decode("utf-8")
text = data.decode("utf-8", errors="replace")   # don't fail on bad bytes
```

`decode` raises `UnicodeDecodeError` on invalid bytes by default, while `TextDecoder` replaces them. Pass `errors="replace"` to match.

## 135: How does BigInt translate?

**Node.js**

```js
const big = 9007199254740993n;
big * 2n;
Number.MAX_SAFE_INTEGER; // 9007199254740991
```

**Python**

```python
big = 9007199254740993
big * 2   # plain int, no suffix needed
```

Python's `int` has no size limit, so there is no `BigInt` split. Be careful when returning large ints in JSON: JavaScript clients lose precision above `2**53 - 1`, so send big IDs as strings.

## 136: How does floating point math compare?

**Node.js**

```js
0.1 + 0.2; // 0.30000000000000004
```

**Python**

```python
0.1 + 0.2   # 0.30000000000000004

from decimal import Decimal
Decimal("0.1") + Decimal("0.2")   # Decimal('0.3')

import math
math.isclose(0.1 + 0.2, 0.3)      # True
```

Both use IEEE 754 doubles, so float results are identical. Python's `Decimal` gives exact decimal math for money. Build it from strings, not floats.

## 137: How do global error handlers translate?

**Node.js**

```js
process.on("uncaughtException", (err) => {
  console.error("Fatal", err);
  process.exit(1);
});
process.on("unhandledRejection", (reason) => console.error(reason));
```

**Python**

```python
import sys

def handle(exc_type, exc, tb) -> None:
    print("Fatal", exc, file=sys.stderr)

sys.excepthook = handle

# asyncio tasks
loop = asyncio.get_running_loop()
loop.set_exception_handler(lambda loop, ctx: print(ctx["message"]))
```

In web apps you rarely set these. The framework catches exceptions per request and returns a 500, the way Express's error middleware does.

## 138: How does Ctrl+C handling translate?

**Node.js**

```js
process.on("SIGINT", () => {
  console.log("Stopping...");
  process.exit(0);
});
```

**Python**

```python
try:
    run_forever()
except KeyboardInterrupt:
    print("Stopping...")
```

Python turns Ctrl+C into a `KeyboardInterrupt` exception, so `finally` blocks and `with` statements clean up. For `SIGTERM` (sent by Docker and Kubernetes), use the `signal` module or your server's shutdown hooks.

## 139: How does a basic Dockerfile translate?

**Node.js**

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["node", "src/server.js"]
```

**Python**

```dockerfile
FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY . .
CMD ["uv", "run", "--no-sync", "fastapi", "run", "app/main.py", "--port", "8000"]
```

Copy the lockfile first so dependency installs are cached between builds, the same trick as copying `package*.json` first. Prefer `-slim` over `-alpine` for Python, because many packages ship prebuilt wheels only for glibc.

## 140: What replaces NODE_ENV?

**Node.js**

```js
if (process.env.NODE_ENV === "production") {
  app.set("trust proxy", 1);
}
```

**Python**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = "development"
    debug: bool = False

settings = Settings()   # reads ENVIRONMENT and DEBUG
```

Python has no standard variable like `NODE_ENV`. Each framework has its own setting (`DEBUG` in Django, `debug` in Flask), so most teams define an `APP_ENV` or `ENVIRONMENT` variable in their settings class.

## 141: What replaces "type": "module" in package.json?

**Node.js**

```json
{ "type": "module" }
```

**Python**

```text
my_app/
  __init__.py
  main.py
```

Python needs no module type switch. Every `.py` file is a module, and a folder with `__init__.py` is a regular package. Inside a package, use absolute imports (`from my_app.db import engine`) or relative ones (`from .db import engine`).

## 142: How does publishing a package translate?

**Node.js**

```bash
npm version patch
npm publish
```

**Python**

```bash
uv version --bump patch
uv build             # creates dist/*.whl and dist/*.tar.gz
uv publish           # uploads to PyPI
```

PyPI is Python's npm registry. A wheel (`.whl`) is the built, installable package, and the `.tar.gz` is the source distribution. Use trusted publishing from CI instead of long-lived tokens.

## 143: How do semver ranges translate?

**Node.js**

```json
{ "express": "^5.1.0", "zod": "~4.1.0", "pino": "9.7.0" }
```

**Python**

```toml
dependencies = [
  "fastapi>=0.120,<1",
  "pydantic~=2.12",    # >=2.12, <3
  "httpx==0.28.1",
]
```

Python has no `^`. Use `>=` with an upper bound, or `~=` (compatible release). Many Python libraries don't follow strict semver, so rely on the lockfile for reproducible installs.

## 144: What are the most common mistakes JavaScript developers make in Python?

- Using a mutable default argument like `def f(items=[])`.
- Expecting `if items:` to be true for an empty list.
- Calling a coroutine without `await` and wondering why nothing happened.
- Using `requests` or `time.sleep` inside `async def` and blocking the event loop.
- Writing `dict.key` instead of `dict["key"]`.
- Expecting `round(2.5)` to be 3.
- Forgetting the virtual environment and installing packages globally.
- Forgetting `self` as the first method parameter.

**Node.js**

```js
const counts = {};
counts[word] = (counts[word] || 0) + 1;
```

**Python**

```python
from collections import Counter

counts = Counter(words)   # the idiomatic version, not a translated one
```

## 145: How do you translate a small utility module end to end?

**Node.js**

```ts
// slug.ts
export function slugify(text: string, maxLength = 50): string {
  return text
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, maxLength);
}
```

**Python**

```python
# slug.py
import re
import unicodedata

def slugify(text: str, max_length: int = 50) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_length]
```

Translate behavior, then add a test with the same inputs and outputs as the old test suite. Small differences in regex and Unicode handling are exactly what such tests catch.

## 146: How do options objects translate?

**Node.js**

```js
function connect(host, { port = 5432, ssl = false, timeout = 5000 } = {}) {}
connect("db", { ssl: true });
```

**Python**

```python
def connect(host: str, *, port: int = 5432, ssl: bool = False, timeout: float = 5.0) -> None:
    ...

connect("db", ssl=True)
```

Python's keyword arguments replace options objects. The `*` makes everything after it keyword-only, so callers must name them, which reads just as clearly as `{ ssl: true }`.

## 147: How does forEach with an index translate?

**Node.js**

```js
items.forEach((item, i) => console.log(i, item));
```

**Python**

```python
for i, item in enumerate(items):
    print(i, item)

for i, item in enumerate(items, start=1):   # 1-based
    print(i, item)
```

Python has no `forEach` method. A plain `for` loop is the idiom, and it supports `break` and `continue`, which `forEach` does not.

## 148: How do multiline strings translate?

**Node.js**

```js
const sql = `
  SELECT id, name
  FROM users
  WHERE active = true
`;
```

**Python**

```python
import textwrap

sql = """
    SELECT id, name
    FROM users
    WHERE active = true
"""
clean = textwrap.dedent(sql).strip()
```

Triple quotes create multiline strings. Add an `f` prefix for interpolation, but never interpolate user input into SQL. Pass it as a query parameter instead.

## 149: How does the ternary operator translate?

**Node.js**

```js
const label = count === 1 ? "item" : "items";
```

**Python**

```python
label = "item" if count == 1 else "items"
```

Python writes the condition in the middle. Avoid nesting conditional expressions. Use a normal `if`/`elif` block or `match` when there are more than two cases.

## 150: Which Python web framework should replace Express?

| Need                                       | Pick                                |
| ------------------------------------------ | ----------------------------------- |
| JSON API, async I/O, typed request models  | FastAPI                             |
| Small, sync, Express-like app              | Flask                               |
| Full app with ORM, admin, auth, migrations | Django                              |
| NestJS-like structure                      | FastAPI or Django with clear layers |

**Node.js**

```js
app.get("/health", (req, res) => res.json({ ok: true }));
```

**Python**

```python
@app.get("/health")
async def health() -> dict[str, bool]:
    return {"ok": True}
```

FastAPI is the most common target for Express and NestJS APIs, because both are async and FastAPI's typed models feel like TypeScript with Zod. Pick Django when the Node app had grown its own admin panels, auth and ORM layers that Django already provides.

# Moderate Questions (151-300)

## 151: Should you rewrite a Node.js service in Python all at once or step by step?

Step by step, in almost every real system. Put a proxy or API gateway in front of the Node.js service and move one route group at a time to the Python service (the strangler fig pattern). Each step is small, testable and easy to roll back.

A full rewrite only makes sense for small services with good tests. Even then, keep the old service running until the new one passes the same contract tests against real traffic.

**Node.js**

```nginx
# before: everything goes to Node
location / { proxy_pass http://node_api:3000; }
```

**Python**

```nginx
# during migration: moved routes go to Python
location /api/reports/ { proxy_pass http://py_api:8000; }
location /            { proxy_pass http://node_api:3000; }
```

## 152: How does Express middleware for auth translate into FastAPI dependencies?

**Node.js**

```js
function requireUser(req, res, next) {
  const token = req.headers.authorization?.replace("Bearer ", "");
  if (!token) return res.status(401).json({ error: "Unauthorized" });
  req.user = verifyToken(token);
  next();
}
app.get("/me", requireUser, (req, res) => res.json(req.user));
```

**Python**

```python
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

bearer = HTTPBearer(auto_error=False)

async def current_user(
    creds: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)],
) -> User:
    if creds is None:
        raise HTTPException(401, "Unauthorized")
    return verify_token(creds.credentials)

CurrentUser = Annotated[User, Depends(current_user)]

@app.get("/me")
async def me(user: CurrentUser) -> User:
    return user
```

Instead of attaching data to `req`, a dependency returns a typed value that FastAPI passes into the handler. Dependencies can depend on other dependencies, and FastAPI caches each one per request.

## 153: How does Express error-handling middleware translate?

**Node.js**

```js
app.use((err, req, res, next) => {
  if (err instanceof NotFoundError)
    return res.status(404).json({ error: err.message });
  console.error(err);
  res.status(500).json({ error: "Internal error" });
});
```

**Python**

```python
import logging
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(NotFoundError)
async def not_found(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse({"error": str(exc)}, status_code=404)

@app.exception_handler(Exception)
async def unhandled(request: Request, exc: Exception) -> JSONResponse:
    logging.exception("Unhandled error")
    return JSONResponse({"error": "Internal error"}, status_code=500)
```

FastAPI picks the handler by exception class. Flask uses `@app.errorhandler(NotFoundError)`, and Django uses middleware or DRF's `EXCEPTION_HANDLER` setting.

## 154: How does Zod validation translate into Pydantic?

**Node.js**

```ts
import { z } from "zod";

const UserSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.email(),
  age: z.number().int().min(18).optional(),
  tags: z.array(z.string()).default([]),
});
type User = z.infer<typeof UserSchema>;
const user = UserSchema.parse(body);
```

**Python**

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int | None = Field(default=None, ge=18)
    tags: list[str] = []

user = User.model_validate(body)
```

The class is both the schema and the type, so no `z.infer` step is needed. Mutable defaults like `[]` are safe in Pydantic because it copies them for each instance. A failure raises `ValidationError` with a list of errors, similar to `ZodError.issues`.

## 155: How do Zod refine and transform translate?

**Node.js**

```ts
const Signup = z
  .object({
    email: z.string().trim().toLowerCase(),
    password: z.string().min(8),
    confirm: z.string(),
  })
  .refine((d) => d.password === d.confirm, {
    message: "Passwords differ",
    path: ["confirm"],
  });
```

**Python**

```python
from pydantic import BaseModel, Field, field_validator, model_validator

class Signup(BaseModel):
    email: str
    password: str = Field(min_length=8)
    confirm: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.strip().lower()

    @model_validator(mode="after")
    def passwords_match(self) -> "Signup":
        if self.password != self.confirm:
            raise ValueError("Passwords differ")
        return self
```

`field_validator` handles one field (like a transform or refine on that field), and `model_validator(mode="after")` handles checks that span several fields.

## 156: How do request and response DTOs translate?

**Node.js**

```ts
// NestJS
@Post()
async create(@Body() dto: CreateUserDto): Promise<UserResponseDto> {
  const user = await this.users.create(dto);
  return { id: user.id, name: user.name }; // hide passwordHash
}
```

**Python**

```python
class UserCreate(BaseModel):
    name: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)   # read ORM objects
    id: int
    name: str

@app.post("/users", response_model=UserOut, status_code=201)
async def create_user(data: UserCreate):
    return await users.create(data)   # extra fields like password_hash are dropped
```

`response_model` (or the return type) filters the output to the declared fields. This replaces manual mapping or `class-transformer`'s `@Exclude()` to hide secrets.

## 157: How do you load and validate configuration?

**Node.js**

```ts
const Env = z.object({
  DATABASE_URL: z.url(),
  PORT: z.coerce.number().default(3000),
  REDIS_URL: z.string().optional(),
});
export const env = Env.parse(process.env);
```

**Python**

```python
# uv add pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    database_url: str
    port: int = 3000
    redis_url: str | None = None

settings = Settings()   # fails fast at startup if DATABASE_URL is missing
```

Field names match environment variables case-insensitively. Types are converted automatically, so you don't need `z.coerce`.

## 158: What happens if you forget await in each language?

**Node.js**

```js
async function save() {
  db.insert(row); // missing await: still runs, errors become unhandled rejections
}
```

**Python**

```python
async def save() -> None:
    db.insert(row)   # missing await: NOTHING runs
# RuntimeWarning: coroutine 'insert' was never awaited
```

In Node.js the promise starts immediately and the call is only "fire and forget". In Python the coroutine object is created and then thrown away, so the insert never happens. Type checkers and Ruff's rules catch unawaited coroutines, so turn them on.

## 159: How does Promise.allSettled translate?

**Node.js**

```js
const results = await Promise.allSettled(urls.map((u) => fetch(u)));
for (const r of results) {
  if (r.status === "fulfilled") console.log(r.value.status);
  else console.error(r.reason);
}
```

**Python**

```python
results = await asyncio.gather(
    *(client.get(u) for u in urls),
    return_exceptions=True,
)
for r in results:
    if isinstance(r, BaseException):
        print("failed:", r)
    else:
        print(r.status_code)
```

With `return_exceptions=True`, `gather` puts exceptions into the result list instead of raising the first one.

## 160: How does Promise.race translate?

**Node.js**

```js
const winner = await Promise.race([fetchFromPrimary(), fetchFromReplica()]);
```

**Python**

```python
tasks = [asyncio.create_task(fetch_primary()), asyncio.create_task(fetch_replica())]
done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
for t in pending:
    t.cancel()
winner = done.pop().result()
```

Python makes you cancel the losers yourself, while JavaScript leaves them running in the background. Cancelling is usually what you want, so the Python version is more honest about resource use.

## 161: How does Promise.any translate?

**Node.js**

```js
const first = await Promise.any([fromCdnA(), fromCdnB()]); // first success
```

**Python**

```python
async def first_success(*coros):
    tasks = [asyncio.create_task(c) for c in coros]
    errors = []
    try:
        for next_done in asyncio.as_completed(tasks):
            try:
                return await next_done
            except Exception as e:
                errors.append(e)
        raise ExceptionGroup("all failed", errors)
    finally:
        for t in tasks:
            t.cancel()
```

asyncio has no built-in `any`. `as_completed` yields results in finish order, so return the first one that does not raise. `ExceptionGroup` plays the role of `AggregateError`.

## 162: How do timeouts translate?

**Node.js**

```js
const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

**Python**

```python
async with asyncio.timeout(5):          # Python 3.11+
    res = await client.get(url)
# raises TimeoutError after 5 seconds

result = await asyncio.wait_for(slow(), timeout=5)

# or the client's own timeout
client = httpx.AsyncClient(timeout=httpx.Timeout(5.0, connect=2.0))
```

`asyncio.timeout` cancels everything inside the block, so one timeout can cover several awaits. Set timeouts on every HTTP client and database driver. Node's `fetch` has no total timeout by default, httpx defaults to 5 seconds, and many database drivers wait forever.

## 163: How does AbortController cancellation translate?

**Node.js**

```js
const controller = new AbortController();
const p = longJob({ signal: controller.signal });
controller.abort();
```

**Python**

```python
task = asyncio.create_task(long_job())
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("cancelled")
```

Python does not pass a signal around. Calling `task.cancel()` raises `CancelledError` at the task's current `await`, and it bubbles through every function in that task. Cleanup goes in `try/finally` or `async with`.

## 164: What is structured concurrency and how does it compare to Promise.all?

**Node.js**

```js
// If getA fails, getB keeps running in the background
await Promise.all([getA(), getB()]);
```

**Python**

```python
async with asyncio.TaskGroup() as tg:
    a = tg.create_task(get_a())
    b = tg.create_task(get_b())
# leaving the block means all tasks finished;
# if one failed, the others were cancelled and an ExceptionGroup was raised
```

Structured concurrency ties task lifetimes to a code block. No task can outlive the block, so you never get stray background work. Catch failures with `except*`:

```python
try:
    async with asyncio.TaskGroup() as tg: ...
except* httpx.HTTPError as eg:
    for e in eg.exceptions:
        print(e)
```

## 165: How do you limit concurrency, like p-limit?

**Node.js**

```js
import pLimit from "p-limit";

const limit = pLimit(5);
await Promise.all(urls.map((u) => limit(() => fetch(u))));
```

**Python**

```python
sem = asyncio.Semaphore(5)

async def fetch_limited(url: str) -> httpx.Response:
    async with sem:
        return await client.get(url)

results = await asyncio.gather(*(fetch_limited(u) for u in urls))
```

All coroutines are created at once, but only 5 hold the semaphore at a time. For very large lists, use a fixed number of worker tasks reading from an `asyncio.Queue` instead, so you don't create millions of coroutine objects.

## 166: How does retry with backoff translate?

**Node.js**

```js
import pRetry from "p-retry";

const data = await pRetry(() => fetchData(), { retries: 5, minTimeout: 200 });
```

**Python**

```python
# uv add tenacity
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=0.2, max=5),
    retry=retry_if_exception_type(httpx.TransportError),
)
async def fetch_data() -> dict:
    res = await client.get(URL)
    res.raise_for_status()
    return res.json()
```

`tenacity` works on both sync and async functions. Retry only errors that are safe to retry, such as network failures and 503s, and only for idempotent requests.

## 167: Why must you not call blocking libraries inside async def?

**Node.js**

```js
// Almost every Node library is async, so this problem is rare
const data = await fs.promises.readFile(path);
```

**Python**

```python
import requests

@app.get("/bad")
async def bad():
    return requests.get(URL).json()   # blocks the event loop for every request

@app.get("/good")
async def good():
    res = await client.get(URL)        # httpx.AsyncClient
    return res.json()

@app.get("/also-good")
async def also_good():
    return await asyncio.to_thread(legacy_blocking_call)
```

Many Python libraries are sync only. Calling them in `async def` freezes the event loop, just like a `while(true)` in Node. Use an async library or move the call to a thread with `asyncio.to_thread`.

## 168: When should a FastAPI route be def instead of async def?

**Node.js**

```js
// Every handler is effectively async in Node
app.get("/report", async (req, res) => res.json(await buildReport()));
```

**Python**

```python
@app.get("/report-sync")
def report_sync():               # runs in a thread pool
    return build_report_with_sync_orm()

@app.get("/report-async")
async def report_async():        # runs on the event loop
    return await build_report_async()
```

FastAPI runs plain `def` routes in a thread pool, so blocking code is safe there. Use `async def` only when everything inside is non-blocking. Mixing them up is the most common FastAPI performance bug.

## 169: Why should you reuse HTTP clients?

**Node.js**

```js
// fetch uses a global undici agent with keep-alive by default
const res = await fetch(url);
```

**Python**

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(timeout=10)
    yield
    await app.state.http.aclose()

app = FastAPI(lifespan=lifespan)

@app.get("/proxy")
async def proxy(request: Request):
    res = await request.app.state.http.get(URL)
    return res.json()
```

Creating a new `httpx.AsyncClient` per request opens a new connection pool every time and loses keep-alive. Create one client at startup and close it on shutdown.

## 170: How do you stream a response?

**Node.js**

```js
app.get("/export", async (req, res) => {
  res.setHeader("Content-Type", "text/csv");
  for await (const row of db.streamRows()) res.write(`${row.id},${row.name}\n`);
  res.end();
});
```

**Python**

```python
from fastapi.responses import StreamingResponse

@app.get("/export")
async def export() -> StreamingResponse:
    async def rows():
        async for row in db.stream_rows():
            yield f"{row.id},{row.name}\n"
    return StreamingResponse(rows(), media_type="text/csv")
```

`StreamingResponse` sends each yielded chunk as it is produced, so memory stays flat for big exports. Flask does the same with a generator returned in a `Response`.

## 171: How do file uploads translate from multer?

**Node.js**

```js
import multer from "multer";

const upload = multer({ dest: "uploads/", limits: { fileSize: 5_000_000 } });
app.post("/avatar", upload.single("file"), (req, res) => {
  res.json({ name: req.file.originalname, size: req.file.size });
});
```

**Python**

```python
from fastapi import File, UploadFile

@app.post("/avatar")
async def avatar(file: UploadFile = File(...)) -> dict:
    data = await file.read()
    if len(data) > 5_000_000:
        raise HTTPException(413, "File too large")
    return {"name": file.filename, "size": len(data)}
```

FastAPI needs `python-multipart` installed for forms and files (included in `fastapi[standard]`). `UploadFile` spools large files to disk. For big uploads, stream them in chunks with `await file.read(1024 * 1024)` instead of reading everything.

## 172: How do cookies translate?

**Node.js**

```js
res.cookie("session", token, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  maxAge: 3600_000,
});
const session = req.cookies.session; // cookie-parser
```

**Python**

```python
from fastapi import Cookie, Response

@app.post("/login")
async def login(response: Response) -> dict:
    response.set_cookie("session", token, httponly=True, secure=True, samesite="lax", max_age=3600)
    return {"ok": True}

@app.get("/me")
async def me(session: str | None = Cookie(default=None)) -> dict:
    return {"session": session}
```

Note the units: Express's `maxAge` is in milliseconds, while Starlette's `max_age` is in seconds.

## 173: How do server sessions translate from express-session?

**Node.js**

```js
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
  }),
);
req.session.userId = user.id;
```

**Python**

```python
from starlette.middleware.sessions import SessionMiddleware

app.add_middleware(SessionMiddleware, secret_key=settings.session_secret)

@app.post("/login")
async def login(request: Request) -> dict:
    request.session["user_id"] = user.id
    return {"ok": True}
```

Starlette and Flask store the session in a signed cookie by default, not on the server. If the Node app used a Redis session store, keep that design with a server-side session library, because signed cookie sessions cannot be revoked one by one.

## 174: How does CORS translate?

**Node.js**

```js
import cors from "cors";

app.use(cors({ origin: ["https://app.example.com"], credentials: true }));
```

**Python**

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Flask uses the `flask-cors` extension and Django uses `django-cors-headers`. As in Express, never combine a wildcard origin with credentials.

## 175: How do JWTs translate from jsonwebtoken to PyJWT?

**Node.js**

```js
import jwt from "jsonwebtoken";

const token = jwt.sign({ sub: user.id }, secret, { expiresIn: "1h" });
const payload = jwt.verify(token, secret, { algorithms: ["HS256"] });
```

**Python**

```python
# uv add pyjwt
from datetime import datetime, timedelta, UTC
import jwt

token = jwt.encode(
    {"sub": str(user.id), "exp": datetime.now(UTC) + timedelta(hours=1)},
    secret,
    algorithm="HS256",
)
payload = jwt.decode(token, secret, algorithms=["HS256"])
```

PyJWT has no `expiresIn` shortcut, so you set `exp` yourself. Always pass `algorithms` when decoding. PyJWT 2.10+ also requires `sub` to be a string, so convert numeric IDs. Tokens are compatible both ways as long as the secret, algorithm and claims match.

## 176: How does password hashing translate?

**Node.js**

```js
import argon2 from "argon2";

const hash = await argon2.hash(password);
const ok = await argon2.verify(hash, password);
```

**Python**

```python
# uv add argon2-cffi
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()
hashed = ph.hash(password)
try:
    ph.verify(hashed, password)
except VerifyMismatchError:
    ...

# bcrypt hashes from Node's bcrypt package also verify in Python
import bcrypt
bcrypt.checkpw(password.encode(), node_hash.encode())
```

Both use the same standard hash formats, so existing user hashes keep working. Avoid `passlib`: it is no longer maintained. `pwdlib` is a modern wrapper used in FastAPI's docs.

## 177: How do role-based guards translate?

**Node.js**

```ts
// NestJS
@Roles("admin")
@UseGuards(AuthGuard, RolesGuard)
@Delete(":id")
remove(@Param("id") id: string) {}
```

**Python**

```python
def require_role(*roles: str):
    async def checker(user: CurrentUser) -> User:
        if user.role not in roles:
            raise HTTPException(403, "Forbidden")
        return user
    return checker

@app.delete("/users/{user_id}", dependencies=[Depends(require_role("admin"))])
async def remove(user_id: int) -> None: ...
```

A dependency factory takes the roles and returns a dependency. Add it to `dependencies=[...]` on a route, a router, or the whole app, the same way you'd attach a guard at method, controller or global level.

## 178: How do you protect a whole group of routes?

**Node.js**

```js
const admin = Router();
admin.use(requireUser, requireAdmin);
admin.get("/stats", getStats);
app.use("/admin", admin);
```

**Python**

```python
admin = APIRouter(
    prefix="/admin",
    dependencies=[Depends(require_role("admin"))],
)

@admin.get("/stats")
async def stats() -> dict: ...

app.include_router(admin)
```

Router-level dependencies run before every route in the router, just like `router.use()` in Express.

## 179: How does rate limiting translate?

**Node.js**

```js
import rateLimit from "express-rate-limit";

app.use("/api/", rateLimit({ windowMs: 60_000, limit: 100 }));
```

**Python**

```python
# uv add slowapi
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, storage_uri="redis://localhost:6379")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/items")
@limiter.limit("100/minute")
async def items(request: Request) -> list: ...
```

Use a shared store like Redis when you run several workers. With in-memory limits, each worker counts separately, the same problem as running several Node processes with `express-rate-limit`'s default store.

## 180: How does helmet translate?

**Node.js**

```js
import helmet from "helmet";

app.use(helmet());
```

**Python**

```python
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response
```

FastAPI has no built-in helmet. Add the headers yourself, use a package like `secure`, or set them at Nginx or the CDN. Django sets most of them through `SecurityMiddleware` settings, and Django 6.0 adds built-in CSP support.

## 181: How does a Prisma schema translate into SQLAlchemy models?

**Node.js**

```prisma
model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  posts     Post[]
  createdAt DateTime @default(now())
}

model Post {
  id       Int    @id @default(autoincrement())
  title    String
  author   User   @relation(fields: [authorId], references: [id])
  authorId Int
}
```

**Python**

```python
from datetime import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    name: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship(back_populates="posts")
```

SQLAlchemy 2.0 reads nullability from the type hint: `Mapped[str | None]` is nullable, `Mapped[str]` is `NOT NULL`. Prisma names tables after models (`"User"`), so set `__tablename__` to the existing name when you keep the same database.

## 182: How do Prisma queries translate into SQLAlchemy?

**Node.js**

```ts
const users = await prisma.user.findMany({
  where: { email: { endsWith: "@example.com" }, name: { not: null } },
  orderBy: { createdAt: "desc" },
  take: 10,
  skip: 20,
});
const one = await prisma.user.findUnique({ where: { id: 1 } });
```

**Python**

```python
from sqlalchemy import select

stmt = (
    select(User)
    .where(User.email.endswith("@example.com"), User.name.is_not(None))
    .order_by(User.created_at.desc())
    .limit(10)
    .offset(20)
)
users = (await session.scalars(stmt)).all()
one = await session.get(User, 1)
```

SQLAlchemy builds queries from column expressions, so typos fail at import time instead of at runtime. `session.scalars()` returns model objects, while `session.execute()` returns rows.

## 183: How does Prisma include translate to eager loading?

**Node.js**

```ts
const users = await prisma.user.findMany({ include: { posts: true } });
```

**Python**

```python
from sqlalchemy.orm import selectinload, joinedload

stmt = select(User).options(selectinload(User.posts))
users = (await session.scalars(stmt)).all()

stmt = select(Post).options(joinedload(Post.author))   # many-to-one: JOIN
```

`selectinload` runs a second `SELECT ... WHERE user_id IN (...)`, which is what Prisma does for `include`. `joinedload` uses one JOIN and fits many-to-one relations. With async sessions you must load relations eagerly, because lazy loading on attribute access is not allowed.

## 184: How do transactions translate?

**Node.js**

```ts
await prisma.$transaction(async (tx) => {
  await tx.account.update({
    where: { id: from },
    data: { balance: { decrement: amount } },
  });
  await tx.account.update({
    where: { id: to },
    data: { balance: { increment: amount } },
  });
});
```

**Python**

```python
from sqlalchemy import update

async with session.begin():   # commits on success, rolls back on exception
    await session.execute(
        update(Account).where(Account.id == from_id).values(balance=Account.balance - amount)
    )
    await session.execute(
        update(Account).where(Account.id == to_id).values(balance=Account.balance + amount)
    )
```

In Django the same pattern is `with transaction.atomic():`. Writing `balance=Account.balance - amount` sends the math to SQL, which avoids lost updates from read-then-write code.

## 185: How do migrations translate from Prisma Migrate to Alembic?

**Node.js**

```bash
npx prisma migrate dev --name add_users
npx prisma migrate deploy
```

**Python**

```bash
uv add alembic
alembic init -t async migrations
alembic revision --autogenerate -m "add users"
alembic upgrade head
```

Alembic compares your models to the database and writes a Python migration file. Always review it: autogenerate misses some changes, like renamed columns, which it sees as a drop plus an add. Django has its own system: `makemigrations` and `migrate`.

## 186: How do the same queries look in the Django ORM?

**Node.js**

```ts
await prisma.user.findMany({
  where: { isActive: true },
  orderBy: { name: "asc" },
  take: 10,
});
await prisma.user.count({ where: { isActive: true } });
await prisma.user.create({ data: { email, name } });
```

**Python**

```python
users = User.objects.filter(is_active=True).order_by("name")[:10]
count = await User.objects.filter(is_active=True).acount()
user = await User.objects.acreate(email=email, name=name)

async for u in User.objects.filter(is_active=True):
    ...
```

Django querysets are lazy and run when you iterate or call a method like `count()`. Async variants start with `a` (`aget`, `acreate`, `acount`). Field lookups use double underscores in keyword arguments, for example `email__endswith="@example.com"`.

## 187: How does raw SQL with pg translate?

**Node.js**

```js
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const { rows } = await pool.query("SELECT * FROM users WHERE id = $1", [id]);
```

**Python**

```python
# psycopg 3
import psycopg
from psycopg_pool import AsyncConnectionPool

pool = AsyncConnectionPool(DATABASE_URL, open=False)
await pool.open()
async with pool.connection() as conn:
    cur = await conn.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    row = await cur.fetchone()

# asyncpg keeps $1 placeholders
row = await asyncpg_pool.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
```

psycopg uses `%s` placeholders, asyncpg uses `$1`. Both send values separately from the SQL, so never format values into the query string.

## 188: How do connection pool settings translate?

**Node.js**

```js
new pg.Pool({
  max: 20,
  idleTimeoutMillis: 30_000,
  connectionTimeoutMillis: 2_000,
});
```

**Python**

```python
engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=10,      # up to 20 total
    pool_timeout=2,       # seconds to wait for a free connection
    pool_recycle=1800,
    pool_pre_ping=True,   # check connections before use
)
```

Each worker process has its own pool. Four Uvicorn workers with 20 connections each can open 80 connections, so size pools from the database's limit divided by the process count.

## 189: How does Mongoose translate?

**Node.js**

```js
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  age: Number,
});
const User = mongoose.model("User", userSchema);
const adults = await User.find({ age: { $gte: 18 } }).limit(10);
```

**Python**

```python
# uv add beanie  (async ODM on top of PyMongo's async API)
from beanie import Document, Indexed, init_beanie
from pymongo import AsyncMongoClient

class User(Document):
    email: Indexed(str, unique=True)
    age: int | None = None

    class Settings:
        name = "users"

client = AsyncMongoClient(MONGO_URL)
await init_beanie(database=client.app, document_models=[User])
adults = await User.find(User.age >= 18).limit(10).to_list()
```

Beanie models are Pydantic models, so validation works like Mongoose schemas. Without an ODM, use PyMongo's `AsyncMongoClient` directly with the same query documents (`{"age": {"$gte": 18}}`). Motor, the older async driver, is deprecated.

## 190: How does ioredis translate?

**Node.js**

```js
import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL);
await redis.set("key", "value", "EX", 60);
const v = await redis.get("key");
```

**Python**

```python
import redis.asyncio as redis

r = redis.from_url(REDIS_URL, decode_responses=True)
await r.set("key", "value", ex=60)
v = await r.get("key")
await r.aclose()
```

`redis-py` returns bytes unless you pass `decode_responses=True`. Options that are positional strings in ioredis (`"EX", 60`) are keyword arguments in Python.

## 191: How does memoization translate?

**Node.js**

```js
const cache = new Map();
function fib(n) {
  if (n < 2) return n;
  if (cache.has(n)) return cache.get(n);
  const v = fib(n - 1) + fib(n - 2);
  cache.set(n, v);
  return v;
}
```

**Python**

```python
from functools import cache, lru_cache

@cache
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

@lru_cache(maxsize=1024)
def get_rate(currency: str) -> float: ...
```

`functools.cache` memoizes in memory per process. It does not work on `async def` functions (it would cache the coroutine object, which can only be awaited once), so use a library like `async-lru` or a Redis cache for async code.

## 192: How does BullMQ translate into Celery?

**Node.js**

```js
import { Queue, Worker } from "bullmq";

const emails = new Queue("emails", { connection });
await emails.add(
  "welcome",
  { userId: 1 },
  { attempts: 3, backoff: { type: "exponential", delay: 1000 } },
);

new Worker("emails", async (job) => sendWelcome(job.data.userId), {
  connection,
});
```

**Python**

```python
# tasks.py
from celery import Celery

app = Celery("app", broker="redis://localhost:6379/0")

@app.task(bind=True, max_retries=3, retry_backoff=True, autoretry_for=(ConnectionError,))
def send_welcome(self, user_id: int) -> None:
    ...

# enqueue from the web app
send_welcome.delay(1)
```

```bash
celery -A tasks worker --loglevel=info
```

Celery tasks are normal sync functions by default. Pass only small, JSON-friendly arguments like IDs, as you would with BullMQ job data.

## 193: What lighter alternatives to Celery exist?

**Node.js**

```js
// BullMQ is the default; lighter options are p-queue for in-process work
```

**Python**

```python
# In-process, after the response is sent (no retries, lost on restart)
from fastapi import BackgroundTasks

@app.post("/signup")
async def signup(data: Signup, tasks: BackgroundTasks) -> dict:
    user = await create_user(data)
    tasks.add_task(send_welcome_email, user.email)
    return {"id": user.id}
```

- **FastAPI `BackgroundTasks`**: like doing work after `res.json()`. Good for small, non-critical work.
- **arq**: async jobs on Redis, closest in spirit to BullMQ.
- **RQ**: simple sync jobs on Redis.
- **Dramatiq**: Celery alternative with simpler defaults.
- **Django 6.0 tasks framework**: a standard task API with pluggable backends.

## 194: How does node-cron translate?

**Node.js**

```js
import cron from "node-cron";

cron.schedule("0 3 * * *", () => cleanupOldSessions());
```

**Python**

```python
# uv add apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = AsyncIOScheduler()
scheduler.add_job(cleanup_old_sessions, CronTrigger.from_crontab("0 3 * * *"))
scheduler.start()
```

As in Node.js, an in-process scheduler runs once per worker. With several workers or pods, use Celery beat, a Kubernetes `CronJob`, or a distributed lock so the job runs once.

## 195: How does pino logging translate?

**Node.js**

```js
import pino from "pino";

const log = pino({ level: "info" });
log.info({ userId: 1, orderId: 42 }, "order created");
```

**Python**

```python
# uv add structlog
import structlog

structlog.configure(processors=[
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.JSONRenderer(),
])
log = structlog.get_logger()
log.info("order created", user_id=1, order_id=42)
```

`structlog` gives pino-style JSON logs with key-value fields. With the standard `logging` module, pass fields through `extra={...}` and use a JSON formatter such as `python-json-logger`.

## 196: How does AsyncLocalStorage translate?

**Node.js**

```js
import { AsyncLocalStorage } from "node:async_hooks";

const als = new AsyncLocalStorage();
app.use((req, res, next) => als.run({ requestId: crypto.randomUUID() }, next));
function currentRequestId() {
  return als.getStore()?.requestId;
}
```

**Python**

```python
import uuid
from contextvars import ContextVar

request_id: ContextVar[str | None] = ContextVar("request_id", default=None)

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    token = request_id.set(request.headers.get("x-request-id", str(uuid.uuid4())))
    try:
        return await call_next(request)
    finally:
        request_id.reset(token)
```

`contextvars` follow async tasks the same way `AsyncLocalStorage` follows promises. Each asyncio task gets a copy of the context when it is created. `structlog.contextvars.bind_contextvars(request_id=...)` adds the value to every log line.

## 197: How do WebSockets translate?

**Node.js**

```js
import { WebSocketServer } from "ws";

const wss = new WebSocketServer({ server });
wss.on("connection", (ws) => {
  ws.on("message", (msg) => ws.send(`echo: ${msg}`));
});
```

**Python**

```python
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            await ws.send_text(f"echo: {msg}")
    except WebSocketDisconnect:
        pass
```

Python uses a loop that awaits messages instead of event callbacks. If the Node app used Socket.IO, use `python-socketio`, which speaks the same protocol so existing clients keep working.

## 198: How do Server-Sent Events translate?

**Node.js**

```js
app.get("/events", (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
  });
  const t = setInterval(() => res.write(`data: ${Date.now()}\n\n`), 1000);
  req.on("close", () => clearInterval(t));
});
```

**Python**

```python
@app.get("/events")
async def events(request: Request) -> StreamingResponse:
    async def stream():
        while not await request.is_disconnected():
            yield f"data: {time.time()}\n\n"
            await asyncio.sleep(1)
    return StreamingResponse(stream(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache"})
```

When the client disconnects, the server cancels the generator, so cleanup can go in a `finally` block. The `sse-starlette` package adds keep-alive pings, event names and IDs.

## 199: How does Apollo Server translate into a Python GraphQL server?

**Node.js**

```js
const typeDefs = `type Query { user(id: ID!): User } type User { id: ID! name: String! }`;
const resolvers = { Query: { user: (_, { id }) => db.user(id) } };
new ApolloServer({ typeDefs, resolvers });
```

**Python**

```python
# uv add "strawberry-graphql[fastapi]"
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class User:
    id: strawberry.ID
    name: str

@strawberry.type
class Query:
    @strawberry.field
    async def user(self, id: strawberry.ID) -> User | None:
        return await db.user(id)

schema = strawberry.Schema(query=Query)
app.include_router(GraphQLRouter(schema), prefix="/graphql")
```

Strawberry is code-first: the schema comes from type hints. If you want to keep the existing SDL file, Ariadne is schema-first like Apollo's `typeDefs` plus `resolvers`.

## 200: How does OpenAPI documentation translate?

**Node.js**

```js
// swagger-jsdoc + swagger-ui-express, or @nestjs/swagger decorators
app.use("/docs", swaggerUi.serve, swaggerUi.setup(spec));
```

**Python**

```python
app = FastAPI(title="Orders API", version="1.0.0")
# Swagger UI at /docs, ReDoc at /redoc, schema at /openapi.json, all automatic
```

FastAPI builds the OpenAPI schema from your route signatures and Pydantic models, so the docs can't drift from the code. Diff the old and new `openapi.json` files to catch contract changes during migration. For Django REST Framework, use `drf-spectacular`.

## 201: How does Supertest translate?

**Node.js**

```js
import request from "supertest";

test("GET /health", async () => {
  const res = await request(app).get("/health");
  expect(res.status).toBe(200);
  expect(res.body).toEqual({ ok: true });
});
```

**Python**

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"ok": True}
```

`TestClient` calls the app in memory without a real server. For async tests, use `httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test")`. Flask has `app.test_client()` and Django has `django.test.Client`.

## 202: How does jest.mock translate?

**Node.js**

```js
vi.mock("./mailer.js", () => ({ sendEmail: vi.fn().mockResolvedValue(true) }));
```

**Python**

```python
from unittest.mock import AsyncMock, patch

@patch("app.services.signup.send_email", new_callable=AsyncMock, return_value=True)
async def test_signup(mock_send) -> None:
    await signup("ana@example.com")
    mock_send.assert_awaited_once_with("ana@example.com")
```

Patch the name where it is used, not where it is defined. If `signup.py` does `from app.mailer import send_email`, patch `app.services.signup.send_email`. This is the most common Python mocking mistake.

## 203: How do spies translate?

**Node.js**

```js
const spy = vi.spyOn(console, "warn");
doThing();
expect(spy).toHaveBeenCalledWith("careful");
```

**Python**

```python
from unittest.mock import patch

def test_warns() -> None:
    with patch.object(logger, "warning", wraps=logger.warning) as spy:
        do_thing()
    spy.assert_called_once_with("careful")

# pytest-mock plugin
def test_warns_mocker(mocker) -> None:
    spy = mocker.spy(logger, "warning")
    do_thing()
    spy.assert_called_once()
```

`wraps=` keeps the real behavior while recording calls, the same as a spy. For logs specifically, pytest's built-in `caplog` fixture is simpler.

## 204: How do beforeEach and afterEach translate?

**Node.js**

```js
let db;
beforeEach(async () => {
  db = await createTestDb();
});
afterEach(async () => {
  await db.close();
});
```

**Python**

```python
import pytest

@pytest.fixture
async def db():
    conn = await create_test_db()
    yield conn          # the test runs here
    await conn.close()

async def test_insert(db) -> None:
    await db.insert({"id": 1})
```

A fixture is requested by naming it as a test parameter, so each test gets only the setup it needs. `scope="session"` makes it run once per test run, like `beforeAll`.

## 205: How does test.each translate?

**Node.js**

```js
test.each([
  [1, 1, 2],
  [2, 3, 5],
])("add(%i, %i) = %i", (a, b, expected) => {
  expect(add(a, b)).toBe(expected);
});
```

**Python**

```python
@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(1, 1, 2), (2, 3, 5)],
)
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected
```

Each tuple becomes its own test with its own ID in the report. Use `pytest.param(..., id="negative")` for readable names.

## 206: How do you mock outgoing HTTP calls, like nock or MSW?

**Node.js**

```js
import nock from "nock";

nock("https://api.stripe.com")
  .get("/v1/customers/cus_1")
  .reply(200, { id: "cus_1" });
```

**Python**

```python
# uv add --dev respx
import respx
import httpx

@respx.mock
async def test_customer() -> None:
    respx.get("https://api.stripe.com/v1/customers/cus_1").mock(
        return_value=httpx.Response(200, json={"id": "cus_1"})
    )
    customer = await get_customer("cus_1")
    assert customer["id"] == "cus_1"
```

`respx` mocks `httpx`. For the `requests` library use the `responses` package. Both fail the test on unexpected calls if you configure them to, like `nock.disableNetConnect()`.

## 207: How do fake timers translate?

**Node.js**

```js
vi.useFakeTimers();
vi.setSystemTime(new Date("2026-01-01"));
expect(isExpired(token)).toBe(true);
vi.useRealTimers();
```

**Python**

```python
# uv add --dev time-machine   (or freezegun)
import time_machine

@time_machine.travel("2026-01-01T00:00:00Z", tick=False)
def test_expired() -> None:
    assert is_expired(token)
```

`time-machine` and `freezegun` change what `datetime.now()` and `time.time()` return. They don't speed up `asyncio.sleep`, so for timers inside async code, inject a clock or a short delay instead.

## 208: How does test coverage translate?

**Node.js**

```bash
npx vitest run --coverage
```

**Python**

```bash
uv add --dev pytest-cov
uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

`coverage.py` (used by `pytest-cov`) measures line and branch coverage. Enable `branch = true` in `[tool.coverage.run]` to match Istanbul's branch numbers more closely.

## 209: How do snapshot tests translate?

**Node.js**

```js
expect(renderEmail(user)).toMatchSnapshot();
```

**Python**

```python
# uv add --dev syrupy
def test_email(snapshot) -> None:
    assert render_email(user) == snapshot
```

```bash
uv run pytest --snapshot-update
```

`syrupy` stores snapshots in a `__snapshots__` folder next to the tests, just like Jest. Use snapshots for large stable outputs, and plain asserts for the important fields.

## 210: How do integration tests with a real database translate?

**Node.js**

```js
import { PostgreSqlContainer } from "@testcontainers/postgresql";

const container = await new PostgreSqlContainer("postgres:17").start();
```

**Python**

```python
# uv add --dev "testcontainers[postgres]"
import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session")
def pg_url():
    with PostgresContainer("postgres:17") as pg:
        yield pg.get_connection_url()
```

Start the container once per session and wrap each test in a transaction that rolls back, so tests stay fast and isolated. `pytest-django` does the rollback for Django automatically.

## 211: How does a strict tsconfig translate into strict type checking?

**Node.js**

```json
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true } }
```

**Python**

```toml
[tool.mypy]
strict = true
plugins = ["pydantic.mypy"]

[tool.pyright]
typeCheckingMode = "strict"
```

`strict` turns on checks like "no untyped functions" and "no implicit `Any`". Python libraries without type hints come in as `Any`. Install stub packages (`types-requests`) where they exist.

## 212: How do generic constraints translate?

**Node.js**

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
```

**Python**

```python
from collections.abc import Sized

def longest[T: Sized](a: T, b: T) -> T:     # Python 3.12+
    return a if len(a) >= len(b) else b
```

`T: Sized` is the bound, like `extends` in TypeScript. You can also list allowed types: `[T: (str, bytes)]`.

## 213: How do discriminated unions translate?

**Node.js**

```ts
type Event =
  { type: "click"; x: number; y: number } | { type: "key"; key: string };

function handle(e: Event) {
  if (e.type === "click") console.log(e.x);
}
```

**Python**

```python
from typing import Annotated, Literal
from pydantic import BaseModel, Field

class Click(BaseModel):
    type: Literal["click"]
    x: int
    y: int

class Key(BaseModel):
    type: Literal["key"]
    key: str

Event = Annotated[Click | Key, Field(discriminator="type")]

def handle(e: Click | Key) -> None:
    match e:
        case Click(x=x):
            print(x)
        case Key(key=k):
            print(k)
```

Pydantic uses the discriminator to pick the right model quickly and gives clear errors. Type checkers narrow `e` inside each `case`, like TypeScript does after checking `e.type`.

## 214: How do Partial, Pick and Omit translate?

**Node.js**

```ts
type UserUpdate = Partial<Pick<User, "name" | "email">>;
```

**Python**

```python
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None

@app.patch("/users/{user_id}")
async def update(user_id: int, data: UserUpdate):
    changes = data.model_dump(exclude_unset=True)   # only fields the client sent
```

Python's type system has no mapped types, so you write the update model out. `exclude_unset=True` tells "not sent" apart from "sent as null", which is how you implement PATCH correctly.

## 215: How do unknown and any translate?

**Node.js**

```ts
function parse(input: unknown) {
  if (typeof input === "string") return input.toUpperCase();
}
let loose: any;
```

**Python**

```python
from typing import Any

def parse(value: object) -> str | None:
    if isinstance(value, str):
        return value.upper()
    return None

loose: Any
```

`object` acts like `unknown`: you must narrow it before using it. `Any` turns checking off, like TypeScript's `any`.

## 216: How do type guards translate?

**Node.js**

```ts
function isUser(x: unknown): x is User {
  return typeof x === "object" && x !== null && "email" in x;
}
```

**Python**

```python
from typing import TypeIs   # Python 3.13+, or typing_extensions

def is_user(x: object) -> TypeIs[User]:
    return isinstance(x, User)
```

`TypeIs` narrows in both branches (like TypeScript's `x is User`). The older `TypeGuard` only narrows in the `True` branch. For data from outside, validating with Pydantic is usually better than a hand-written guard.

## 217: How does readonly translate?

**Node.js**

```ts
interface Config {
  readonly port: number;
}
const roles = ["admin", "user"] as const;
```

**Python**

```python
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class Config:
    port: int

ROLES: Final = ("admin", "user")   # a tuple cannot be changed

class Settings(BaseModel):
    model_config = ConfigDict(frozen=True)
```

`frozen=True` makes assignment raise an error at runtime, which is stronger than TypeScript's compile-time-only `readonly`.

## 218: How do function overloads translate?

**Node.js**

```ts
function get(id: number): User;
function get(ids: number[]): User[];
function get(arg: number | number[]) {}
```

**Python**

```python
from typing import overload

@overload
def get(arg: int) -> User: ...
@overload
def get(arg: list[int]) -> list[User]: ...
def get(arg: int | list[int]) -> User | list[User]:
    if isinstance(arg, int):
        return find_one(arg)
    return find_many(arg)
```

Like TypeScript, `@overload` signatures exist only for the type checker, and one real implementation handles every case.

## 219: How do callback types translate?

**Node.js**

```ts
type Handler = (event: string, payload: unknown) => Promise<void>;
```

**Python**

```python
from collections.abc import Awaitable, Callable

Handler = Callable[[str, object], Awaitable[None]]

# Python 3.12+ type alias statement
type Handler2 = Callable[[str, object], Awaitable[None]]
```

For callbacks with keyword arguments or overloads, define a `Protocol` with a `__call__` method instead, since `Callable` only describes positional parameters.

## 220: How do circular imports differ?

**Node.js**

```js
// a.js imports b.js and b.js imports a.js:
// one of them sees a partially initialized module (undefined exports)
```

**Python**

```python
# a.py: from b import helper
# b.py: from a import Thing
# ImportError: cannot import name 'Thing' from partially initialized module 'a'

# fix 1: import the module, not the name
import a
def use() -> None:
    a.Thing()

# fix 2: import only for type hints
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from a import Thing
```

Python fails loudly where Node quietly gives `undefined`. The real fix is usually moving shared code into a third module. Python 3.14 evaluates annotations lazily, so type-hint-only imports cause fewer cycles.

## 221: How do barrel files translate?

**Node.js**

```ts
// services/index.ts
export * from "./user.service";
export * from "./order.service";
```

**Python**

```python
# services/__init__.py
from .user_service import UserService
from .order_service import OrderService

__all__ = ["UserService", "OrderService"]
```

`__init__.py` runs when the package is first imported, so big re-exports slow startup and make cycles more likely, the same problems barrel files cause. Keep them small, or import from the submodule directly.

## 222: How do npm workspaces translate?

**Node.js**

```json
{ "workspaces": ["packages/*", "apps/*"] }
```

**Python**

```toml
# root pyproject.toml
[tool.uv.workspace]
members = ["packages/*", "apps/*"]

# apps/api/pyproject.toml
[project]
dependencies = ["shared-models"]

[tool.uv.sources]
shared-models = { workspace = true }
```

uv workspaces share one lockfile and install local packages in editable mode, so changes in `packages/shared-models` show up immediately, like linked workspace packages in npm.

## 223: How do generators translate?

**Node.js**

```js
function* ids() {
  let i = 0;
  while (true) yield i++;
}
const gen = ids();
gen.next().value;
```

**Python**

```python
from itertools import count, islice

def ids():
    i = 0
    while True:
        yield i
        i += 1

gen = ids()
next(gen)
list(islice(ids(), 5))   # [0, 1, 2, 3, 4]
count()                  # the built-in version
```

Python generators raise `StopIteration` when done instead of returning `{ done: true }`, and `for` loops handle that for you. Generator expressions like `(x * 2 for x in items)` give lazy pipelines.

## 224: How does for await translate?

**Node.js**

```js
async function* pages(url) {
  while (url) {
    const res = await fetch(url).then((r) => r.json());
    yield res.items;
    url = res.next;
  }
}
for await (const items of pages(start)) process(items);
```

**Python**

```python
async def pages(url: str | None):
    while url:
        data = (await client.get(url)).json()
        yield data["items"]
        url = data.get("next")

async for items in pages(start):
    process(items)
```

An `async def` with `yield` is an async generator. Async comprehensions also work: `[x async for x in source()]`.

## 225: How do Node streams translate?

**Node.js**

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("big.log"),
  createGzip(),
  createWriteStream("big.log.gz"),
);
```

**Python**

```python
import gzip
import shutil

with open("big.log", "rb") as src, gzip.open("big.log.gz", "wb") as dst:
    shutil.copyfileobj(src, dst, length=1024 * 1024)
```

Python's file objects stream in chunks already, and many stdlib modules (gzip, zipfile, csv) accept file objects. For transform pipelines, chain generators: each one reads from the previous and yields to the next.

## 226: How do you read a large file line by line?

**Node.js**

```js
import { createReadStream } from "node:fs";
import { createInterface } from "node:readline";

const rl = createInterface({ input: createReadStream("big.log") });
for await (const line of rl) if (line.includes("ERROR")) console.log(line);
```

**Python**

```python
with open("big.log", encoding="utf-8") as f:
    for line in f:              # reads lazily, one line at a time
        if "ERROR" in line:
            print(line.rstrip("\n"))
```

Iterating a file object is already lazy and memory-safe. Lines keep their `\n`, unlike Node's readline.

## 227: How does CSV parsing translate?

**Node.js**

```js
import { parse } from "csv-parse";

for await (const row of createReadStream("users.csv").pipe(
  parse({ columns: true }),
)) {
  console.log(row.email);
}
```

**Python**

```python
import csv

with open("users.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["email"])
```

The `csv` module is in the standard library. Open files with `newline=""` so quoted fields with line breaks parse correctly. For heavy data work, `polars` or `pandas` read CSV much faster.

## 228: How does Buffer manipulation translate?

**Node.js**

```js
const header = Buffer.alloc(8);
header.writeUInt32BE(0xcafebabe, 0);
header.writeUInt16LE(42, 4);
header.readUInt32BE(0);
```

**Python**

```python
import struct

header = struct.pack(">IH", 0xCAFEBABE, 42)          # big-endian uint32, uint16
magic, version = struct.unpack_from(">IH", header, 0)

num = int.from_bytes(b"\x00\x2a", "big")             # 42
(42).to_bytes(2, "little")
```

`struct` packs and unpacks binary formats with format strings (`>` big-endian, `<` little-endian, `I` uint32, `H` uint16). It replaces the many `readUInt*`/`writeUInt*` methods.

## 229: How does an async event bus translate?

**Node.js**

```js
import { on } from "node:events";

for await (const [order] of on(bus, "order")) await handle(order);
```

**Python**

```python
queue: asyncio.Queue[dict] = asyncio.Queue(maxsize=1000)

async def producer(order: dict) -> None:
    await queue.put(order)        # waits if full: backpressure

async def consumer() -> None:
    while True:
        order = await queue.get()
        try:
            await handle(order)
        finally:
            queue.task_done()
```

In async Python, an `asyncio.Queue` is the usual way to pass events between tasks. Unlike an EventEmitter, a bounded queue slows producers down when consumers fall behind.

## 230: How does spawn with streaming output translate?

**Node.js**

```js
import { spawn } from "node:child_process";

const child = spawn("ffmpeg", ["-i", input, output]);
child.stderr.on("data", (d) => process.stderr.write(d));
child.on("close", (code) => console.log("exit", code));
```

**Python**

```python
proc = await asyncio.create_subprocess_exec(
    "ffmpeg", "-i", input_path, output_path,
    stderr=asyncio.subprocess.PIPE,
)
async for line in proc.stderr:
    print(line.decode().rstrip())
code = await proc.wait()
```

Use `asyncio.create_subprocess_exec` in async code and `subprocess.Popen` in sync code. Always read the pipes you open, or the child can block when the pipe buffer fills.

## 231: How do worker_threads translate for CPU-heavy work?

**Node.js**

```js
import { Worker } from "node:worker_threads";

const worker = new Worker("./resize.js", { workerData: { path } });
worker.on("message", (result) => console.log(result));
```

**Python**

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

pool = ProcessPoolExecutor(max_workers=4)

async def resize(path: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(pool, resize_image, path)  # runs in another process
```

With the standard GIL build, Python threads cannot run Python code in parallel, so CPU work goes to processes. Arguments and results are pickled between processes, so keep them small. Threads are still fine for blocking I/O and for C libraries that release the GIL, like NumPy.

## 232: How do Node cluster and PM2 translate?

**Node.js**

```bash
pm2 start dist/server.js -i max
```

**Python**

```bash
# ASGI (FastAPI): Uvicorn manages worker processes itself
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
fastapi run app/main.py --workers 4

# WSGI (Flask, Django sync): Gunicorn
gunicorn app:app --workers 4 --threads 4
```

Python servers always use a process manager for multi-core use, the same way Node uses cluster. In Kubernetes, many teams run one worker per container and scale pods instead, which keeps memory limits and health checks simple.

## 233: How does graceful shutdown translate?

**Node.js**

```js
process.on("SIGTERM", async () => {
  server.close();
  await pool.end();
  process.exit(0);
});
```

**Python**

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield                   # app is serving
    await db.disconnect()   # runs on SIGTERM after in-flight requests finish

app = FastAPI(lifespan=lifespan)
```

Uvicorn and Gunicorn handle `SIGTERM` for you: they stop accepting connections, wait for open requests (up to a timeout), then run shutdown hooks. You don't write signal handlers in a web app.

## 234: How do startup hooks translate?

**Node.js**

```js
await connectDb();
await warmCache();
app.listen(3000, () => console.log("ready"));
```

**Python**

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await create_pool()
    await warm_cache(app.state.db)
    yield
    await app.state.db.close()
```

The lifespan function replaces both "do work before `listen()`" and shutdown handlers. The older `@app.on_event("startup")` decorators are deprecated. In Django, put startup code in `AppConfig.ready()`, and keep it light.

## 235: How does NestJS dependency injection translate?

**Node.js**

```ts
@Injectable()
export class UsersService {
  constructor(private readonly repo: UsersRepository) {}
}

@Controller("users")
export class UsersController {
  constructor(private readonly users: UsersService) {}
}
```

**Python**

```python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session():
    async with SessionLocal() as session:
        yield session

def get_repo(session: Annotated[AsyncSession, Depends(get_session)]) -> UsersRepository:
    return UsersRepository(session)

def get_service(repo: Annotated[UsersRepository, Depends(get_repo)]) -> UsersService:
    return UsersService(repo)

@router.get("/{user_id}")
async def get_user(user_id: int, svc: Annotated[UsersService, Depends(get_service)]):
    return await svc.get(user_id)
```

FastAPI resolves a tree of dependency functions per request instead of a global container. Classes stay plain and take their collaborators in `__init__`, which keeps them easy to test. For a full container like Nest's, libraries such as `dependency-injector`, `dishka` or `svcs` exist.

## 236: How do NestJS modules and controllers map to Python structure?

**Node.js**

```text
src/users/
  users.module.ts
  users.controller.ts
  users.service.ts
  dto/create-user.dto.ts
  entities/user.entity.ts
```

**Python**

```text
app/users/
  __init__.py
  router.py        # controller: APIRouter routes
  service.py       # business logic
  schemas.py       # Pydantic DTOs
  models.py        # SQLAlchemy models
  dependencies.py  # Depends() factories
```

Python has no module declarations. The folder is the module, and `main.py` wires routers together with `include_router`. Django apps follow the same idea with `views.py`, `models.py`, `serializers.py` and `urls.py`.

## 237: How do NestJS interceptors translate?

**Node.js**

```ts
@Injectable()
export class TimingInterceptor implements NestInterceptor {
  intercept(ctx: ExecutionContext, next: CallHandler) {
    const start = Date.now();
    return next.handle().pipe(tap(() => console.log(Date.now() - start)));
  }
}
```

**Python**

```python
import functools
import time

def timed(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return await fn(*args, **kwargs)
        finally:
            print(fn.__name__, time.perf_counter() - start)
    return wrapper

@router.get("/slow")
@timed
async def slow() -> dict: ...
```

Use middleware for work around every request and decorators for specific handlers. `functools.wraps` keeps the original signature visible, which FastAPI needs to find the parameters.

## 238: How do decorators differ between TypeScript and Python?

**Node.js**

```ts
// TS 5 standard decorators: functions that receive the method and a context object
function log(target: Function, context: ClassMethodDecoratorContext) {
  return function (this: unknown, ...args: unknown[]) {
    console.log("call", String(context.name));
    return target.apply(this, args);
  };
}
class Svc {
  @log run() {}
}
```

**Python**

```python
import functools

def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("call", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@log
def run() -> None: ...
```

A Python decorator is just a function that takes a function and returns a replacement. It works on any function or class, not only class members, and it has been part of the language for years.

## 239: How do you write a decorator that takes arguments?

**Node.js**

```ts
function retry(times: number) {
  return function (target: Function, ctx: ClassMethodDecoratorContext) {
    return async function (this: unknown, ...args: unknown[]) {
      for (let i = 0; ; i++) {
        try {
          return await target.apply(this, args);
        } catch (e) {
          if (i >= times) throw e;
        }
      }
    };
  };
}
```

**Python**

```python
def retry(times: int):
    def decorator(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            for attempt in range(times + 1):
                try:
                    return await fn(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
        return wrapper
    return decorator

@retry(times=3)
async def fetch_data() -> dict: ...
```

A decorator with arguments is a function that returns a decorator, so there are three nested layers. Inside `except`, a bare `raise` re-raises the current exception with its original traceback.

## 240: How do context managers compare to try/finally and using?

**Node.js**

```js
// explicit resource management (Node 24+)
{
  await using conn = await pool.connect(); // disposed at block end
  await conn.query("SELECT 1");
}
```

**Python**

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def connection():
    conn = await pool.acquire()
    try:
        yield conn
    finally:
        await pool.release(conn)

async with connection() as conn:
    await conn.execute("SELECT 1")
```

Python's `with` and `async with` are the original version of what JavaScript's `using` adds. Any object with `__enter__`/`__exit__` (or the async versions) works, and `contextlib` turns a generator into one quickly.

## 241: How does date arithmetic translate from date-fns?

**Node.js**

```js
import { addDays, differenceInDays, startOfDay } from "date-fns";

addDays(new Date(), 7);
differenceInDays(end, start);
startOfDay(new Date());
```

**Python**

```python
from datetime import datetime, timedelta, UTC

now = datetime.now(UTC)
now + timedelta(days=7)
(end - start).days
now.replace(hour=0, minute=0, second=0, microsecond=0)

from dateutil.relativedelta import relativedelta   # uv add python-dateutil
now + relativedelta(months=1)                     # calendar months
```

`timedelta` handles days, hours and seconds. It has no months, because months have different lengths, so use `dateutil.relativedelta` for month math.

## 242: How does Intl number and currency formatting translate?

**Node.js**

```js
new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(
  1234.5,
);
// "1.234,50 €"
```

**Python**

```python
# uv add babel
from babel.numbers import format_currency

format_currency(1234.5, "EUR", locale="de_DE")   # "1.234,50 €"
```

Python's built-in `locale` module changes process-wide state and depends on OS locales, so it is unsafe in web servers. Babel uses CLDR data like `Intl` and is safe per call.

## 243: How do per-environment config files translate?

**Node.js**

```js
// config/default.json, config/production.json with the "config" package
import config from "config";
config.get("db.host");
```

**Python**

```python
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class DbSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__", env_file=".env")
    db: DbSettings = DbSettings()

settings = Settings()   # DB__HOST=prod-db overrides settings.db.host
```

`pydantic-settings` reads nested settings from env variables with a delimiter. That follows the twelve-factor style better than per-environment JSON files, but `env_file` can still point to `.env.production` if needed.

## 244: How does a production multi-stage Dockerfile translate?

**Node.js**

```dockerfile
FROM node:24-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:24-slim
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**Python**

```dockerfile
FROM python:3.14-slim AS build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY . .
RUN uv sync --frozen --no-dev

FROM python:3.14-slim
WORKDIR /app
COPY --from=build /app /app
ENV PATH="/app/.venv/bin:$PATH"
RUN useradd --create-home app
USER app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

The virtual environment plays the role of `node_modules`. Build it in the first stage and copy it into a clean image. Both stages must use the same Python version and OS, because compiled packages are tied to them.

## 245: How do health check endpoints translate?

**Node.js**

```js
app.get("/healthz", (req, res) => res.json({ ok: true }));
app.get("/readyz", async (req, res) => {
  try {
    await pool.query("SELECT 1");
    res.json({ ok: true });
  } catch {
    res.status(503).json({ ok: false });
  }
});
```

**Python**

```python
from sqlalchemy import text

@app.get("/healthz")
async def healthz() -> dict:
    return {"ok": True}

@app.get("/readyz")
async def readyz(session: SessionDep) -> JSONResponse:
    try:
        await session.execute(text("SELECT 1"))
        return JSONResponse({"ok": True})
    except Exception:
        return JSONResponse({"ok": False}, status_code=503)
```

Keep liveness checks simple. If a liveness probe checks the database, a database outage restarts every pod, which only makes things worse.

## 246: How does pagination translate?

**Node.js**

```js
app.get("/items", async (req, res) => {
  const limit = Math.min(Number(req.query.limit ?? 20), 100);
  const cursor = req.query.cursor ? Number(req.query.cursor) : undefined;
  const items = await prisma.item.findMany({
    take: limit,
    ...(cursor && { cursor: { id: cursor }, skip: 1 }),
    orderBy: { id: "asc" },
  });
  res.json({ items, nextCursor: items.at(-1)?.id ?? null });
});
```

**Python**

```python
from fastapi import Query

@app.get("/items")
async def items(
    session: SessionDep,
    limit: int = Query(20, le=100),
    cursor: int | None = None,
) -> dict:
    stmt = select(Item).order_by(Item.id).limit(limit)
    if cursor is not None:
        stmt = stmt.where(Item.id > cursor)
    rows = (await session.scalars(stmt)).all()
    return {"items": rows, "nextCursor": rows[-1].id if rows else None}
```

`Query(le=100)` replaces the manual `Math.min` clamp, and a larger value returns a 422. Keep the old JSON field names (like `nextCursor`) so existing clients keep working.

## 247: How do production web server setups compare?

**Node.js**

```text
Nginx/ALB -> node dist/server.js (cluster or one process per container)
```

**Python**

```text
Nginx/ALB -> uvicorn (ASGI: FastAPI, Starlette, Django async)
Nginx/ALB -> gunicorn (WSGI: Flask, Django sync)
Nginx/ALB -> gunicorn -k uvicorn_worker.UvicornWorker (ASGI with Gunicorn's process manager)
```

Node.js has the HTTP server built in. Python separates the app (a WSGI or ASGI callable) from the server, so you pick the server. Granian (written in Rust) is a newer server that handles both WSGI and ASGI.

## 248: How do axios interceptors translate?

**Node.js**

```js
const api = axios.create({ baseURL: "https://api.example.com" });
api.interceptors.request.use((config) => {
  config.headers.Authorization = `Bearer ${getToken()}`;
  return config;
});
```

**Python**

```python
class BearerAuth(httpx.Auth):
    def auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {get_token()}"
        yield request

async def log_response(response: httpx.Response) -> None:
    print(response.request.method, response.request.url, response.status_code)

api = httpx.AsyncClient(
    base_url="https://api.example.com",
    auth=BearerAuth(),
    event_hooks={"response": [log_response]},
)
```

`httpx.Auth` can also handle refresh flows: yield the request, check for a 401, refresh the token and yield the request again. `event_hooks` cover logging and metrics.

## 249: How do HTTP error helpers translate?

**Node.js**

```js
import createError from "http-errors";

throw createError(404, "User not found");
```

**Python**

```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="User not found")
# response: {"detail": "User not found"}

# Flask
from flask import abort
abort(404, description="User not found")
```

FastAPI's default error body is `{"detail": ...}`. If clients expect the Node app's shape, such as `{"error": "..."}`, add an exception handler for `HTTPException` that returns the old format.

## 250: How do unhandled promise rejections compare to asyncio task errors?

**Node.js**

```js
// Node 15+: an unhandled rejection crashes the process by default
doWork(); // no await, no catch
```

**Python**

```python
asyncio.create_task(do_work())
# if do_work fails and nobody awaits the task, the error is only logged
# when the task is garbage collected: "Task exception was never retrieved"
```

asyncio does not crash on a failed background task. It logs the error late, or never. Always await tasks, use a `TaskGroup`, or add a done-callback that logs failures right away.

## 251: How does debugging translate?

**Node.js**

```bash
node --inspect-brk src/server.js   # attach Chrome DevTools or VS Code
```

```js
debugger;
```

**Python**

```python
breakpoint()   # drops into pdb at this line
```

```bash
python -m pdb main.py
python -m debugpy --listen 5678 --wait-for-client -m uvicorn app.main:app
```

`breakpoint()` is the `debugger` statement. VS Code uses `debugpy` the same way it uses Node's inspector, and Python 3.14 can attach pdb to a running process with `python -m pdb -p <pid>`.

## 252: How does CPU profiling translate?

**Node.js**

```bash
node --cpu-prof src/script.js   # writes a .cpuprofile for DevTools
```

**Python**

```bash
python -m cProfile -s cumtime script.py
python -m cProfile -o out.prof script.py && uvx snakeviz out.prof
uvx py-spy record -o profile.svg --pid 12345   # sample a running process
```

`cProfile` traces every call and adds overhead. Sampling profilers like `py-spy` (or the `profiling.sampling` module in Python 3.15) attach to live processes with very little overhead, much like `0x` or Clinic flame graphs.

## 253: How do husky and lint-staged translate?

**Node.js**

```json
{ "lint-staged": { "*.{js,ts}": ["eslint --fix", "prettier --write"] } }
```

**Python**

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.0
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format
```

```bash
uvx pre-commit install
```

The `pre-commit` framework installs the git hook and runs each tool only on staged files, combining what husky and lint-staged do.

## 254: How do lodash utilities map to the standard library?

| lodash              | Python                                           |
| ------------------- | ------------------------------------------------ |
| `_.uniq`            | `list(dict.fromkeys(items))` (keeps order)       |
| `_.flatten`         | `list(itertools.chain.from_iterable(x))`         |
| `_.debounce`        | no stdlib equivalent; rarely needed on servers   |
| `_.pick`            | `{k: d[k] for k in keys if k in d}`              |
| `_.get(obj, "a.b")` | `glom` library, or Pydantic models               |
| `_.partition`       | two comprehensions or `more_itertools.partition` |
| `_.isEqual`         | `==`                                             |

**Node.js**

```js
_.uniqBy(users, "email");
```

**Python**

```python
unique = list({u["email"]: u for u in users}.values())   # last one wins
```

The `more-itertools` package fills most of the remaining gaps.

## 255: How does groupBy translate?

**Node.js**

```js
const byStatus = Object.groupBy(orders, (o) => o.status);
```

**Python**

```python
from collections import defaultdict

by_status: dict[str, list[Order]] = defaultdict(list)
for o in orders:
    by_status[o.status].append(o)
```

`itertools.groupby` looks similar but only groups neighboring items, so it needs sorted input. The `defaultdict` loop is the safe equivalent of `Object.groupBy`.

## 256: How does counting occurrences translate?

**Node.js**

```js
const counts = {};
for (const w of words) counts[w] = (counts[w] ?? 0) + 1;
const top = Object.entries(counts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 3);
```

**Python**

```python
from collections import Counter

counts = Counter(words)
top = counts.most_common(3)
counts["missing"]   # 0, no KeyError
```

`Counter` is a dict subclass with counting helpers. You can add and subtract counters with `+` and `-`.

## 257: How do queues translate?

**Node.js**

```js
const queue = [];
queue.push(job);
const next = queue.shift(); // O(n) for large arrays
```

**Python**

```python
from collections import deque

queue: deque[Job] = deque(maxlen=10_000)   # optional size limit
queue.append(job)
next_job = queue.popleft()                 # O(1)
```

`deque` is fast at both ends. Use `asyncio.Queue` between async tasks and `queue.Queue` between threads, since those two handle waiting and locking.

## 258: How do priority queues translate?

**Node.js**

```js
// no built-in heap; use a package or keep a sorted array
import { MinPriorityQueue } from "@datastructures-js/priority-queue";
```

**Python**

```python
import heapq

heap: list[tuple[int, str]] = []
heapq.heappush(heap, (2, "low"))
heapq.heappush(heap, (1, "high"))
heapq.heappop(heap)          # (1, 'high')
heapq.nlargest(3, scores)
```

`heapq` turns a plain list into a min-heap. Put `(priority, counter, item)` tuples in it so items with equal priority never need to be compared.

## 259: How do binary search and sorted inserts translate?

**Node.js**

```js
// hand-written binary search, or a library
```

**Python**

```python
import bisect

scores = [10, 20, 30]
bisect.insort(scores, 25)               # [10, 20, 25, 30]
i = bisect.bisect_left(scores, 20)      # 1
bisect.bisect_left(users, 30, key=lambda u: u.age)   # key= since 3.10
```

Python ships binary search in the standard library. For a sorted collection that stays sorted, the `sortedcontainers` package is a common choice.

## 260: How do template engines translate?

**Node.js**

```js
import Handlebars from "handlebars";

const tpl = Handlebars.compile(
  "Hello {{name}}! {{#each items}}<li>{{this}}</li>{{/each}}",
);
tpl({ name: "Ana", items: ["a", "b"] });
```

**Python**

```python
from jinja2 import Environment, select_autoescape

env = Environment(autoescape=select_autoescape())
tpl = env.from_string("Hello {{ name }}! {% for i in items %}<li>{{ i }}</li>{% endfor %}")
tpl.render(name="Ana", items=["a", "b"])
```

Jinja2 is the standard template engine for Flask and is supported by FastAPI and Django. Turn on autoescaping for HTML, as it is off by default in a bare `Environment`.

## 261: How do server-rendered views translate from Express with EJS?

**Node.js**

```js
app.set("view engine", "ejs");
app.get("/", (req, res) => res.render("index", { user: req.user }));
```

**Python**

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"user": None})

# Flask
from flask import render_template

@app.get("/")
def index_flask():
    return render_template("index.html", user=None)
```

For HTML-heavy apps, Django or Flask fit better than FastAPI, because they come with forms, CSRF protection and session helpers built around templates.

## 262: How does nodemailer translate?

**Node.js**

```js
const transporter = nodemailer.createTransport({
  host,
  port: 587,
  auth: { user, pass },
});
await transporter.sendMail({ from, to, subject: "Hi", text: "Hello" });
```

**Python**

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["From"], msg["To"], msg["Subject"] = sender, to, "Hi"
msg.set_content("Hello")

with smtplib.SMTP(host, 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(msg)
```

`smtplib` blocks, so call it from a background job or `asyncio.to_thread`. `aiosmtplib` is the async version. Most production apps call a provider's HTTP API instead of using SMTP directly.

## 263: How does the AWS SDK v3 translate to boto3?

**Node.js**

```js
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";

const s3 = new S3Client({ region: "eu-central-1" });
await s3.send(
  new PutObjectCommand({ Bucket: "my-bucket", Key: "a.txt", Body: "hi" }),
);
```

**Python**

```python
import boto3

s3 = boto3.client("s3", region_name="eu-central-1")
s3.put_object(Bucket="my-bucket", Key="a.txt", Body=b"hi")

url = s3.generate_presigned_url(
    "get_object", Params={"Bucket": "my-bucket", "Key": "a.txt"}, ExpiresIn=3600
)
```

boto3 is synchronous. In async code, wrap calls with `asyncio.to_thread`, or use `aioboto3`. Parameter names stay the same (`Bucket`, `Key`), which makes translation easy.

## 264: How does the 404 fallback handler translate?

**Node.js**

```js
app.use((req, res) =>
  res.status(404).json({ error: "Not found", path: req.path }),
);
```

**Python**

```python
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def http_errors(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    if exc.status_code == 404:
        return JSONResponse({"error": "Not found", "path": request.url.path}, status_code=404)
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)
```

FastAPI returns `{"detail": "Not Found"}` for unknown routes. Register the handler on Starlette's `HTTPException` (the base class) so it also catches routing 404s, not only the ones you raise.

## 265: How do form-encoded bodies translate?

**Node.js**

```js
app.use(express.urlencoded({ extended: true }));
app.post("/login", (req, res) => res.json({ user: req.body.username }));
```

**Python**

```python
from fastapi import Form

@app.post("/login")
async def login(username: str = Form(), password: str = Form()) -> dict:
    return {"user": username}
```

`Form()` reads `application/x-www-form-urlencoded` and multipart fields. In Flask they are in `request.form`. Express's `extended: true` turns nested keys like `a[b]=1` into objects. Python frameworks don't do that, so handle such keys yourself if clients send them.

## 266: How do request body size limits translate?

**Node.js**

```js
app.use(express.json({ limit: "1mb" }));
```

**Python**

```python
# Flask
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

# Django settings.py
DATA_UPLOAD_MAX_MEMORY_SIZE = 1 * 1024 * 1024
```

```nginx
# FastAPI/Uvicorn: no built-in body limit, set it at the proxy
client_max_body_size 1m;
```

Express rejects big JSON bodies by default (100 KB). FastAPI has no default limit, so set one at Nginx or the load balancer, or add a middleware that checks `Content-Length` and the streamed size.

## 267: How does trust proxy translate?

**Node.js**

```js
app.set("trust proxy", 1);
req.ip; // real client IP from X-Forwarded-For
```

**Python**

```bash
uvicorn app.main:app --proxy-headers --forwarded-allow-ips="10.0.0.0/8"
```

```python
# Flask behind one proxy
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)
```

Only trust forwarded headers from your own proxies. Otherwise any client can fake its IP, which breaks rate limits and audit logs. In FastAPI the client IP is `request.client.host`.

## 268: How do you run HTTPS locally?

**Node.js**

```js
import https from "node:https";
import fs from "node:fs";

https
  .createServer(
    { key: fs.readFileSync("key.pem"), cert: fs.readFileSync("cert.pem") },
    app,
  )
  .listen(443);
```

**Python**

```bash
uvicorn app.main:app --ssl-keyfile key.pem --ssl-certfile cert.pem --port 8443
```

`mkcert` creates trusted local certificates for both stacks. In production, TLS usually ends at the load balancer or Nginx in both cases.

## 269: How do you translate a CRUD controller end to end?

**Node.js**

```ts
// Express + Prisma
router.get("/", async (req, res) => res.json(await prisma.todo.findMany()));
router.post("/", async (req, res) => {
  const data = TodoCreate.parse(req.body);
  res.status(201).json(await prisma.todo.create({ data }));
});
router.patch("/:id", async (req, res) => {
  const data = TodoUpdate.parse(req.body);
  res.json(
    await prisma.todo.update({ where: { id: Number(req.params.id) }, data }),
  );
});
router.delete("/:id", async (req, res) => {
  await prisma.todo.delete({ where: { id: Number(req.params.id) } });
  res.sendStatus(204);
});
```

**Python**

```python
router = APIRouter(prefix="/todos")

@router.get("/")
async def list_todos(session: SessionDep) -> list[TodoOut]:
    return (await session.scalars(select(Todo))).all()

@router.post("/", status_code=201)
async def create_todo(data: TodoCreate, session: SessionDep) -> TodoOut:
    todo = Todo(**data.model_dump())
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo

@router.patch("/{todo_id}")
async def update_todo(todo_id: int, data: TodoUpdate, session: SessionDep) -> TodoOut:
    todo = await session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(404, "Todo not found")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    await session.commit()
    return todo

@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: int, session: SessionDep) -> None:
    todo = await session.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(404, "Todo not found")
    await session.delete(todo)
    await session.commit()
```

Note that Prisma throws on `update` and `delete` of a missing row, which the old app may have turned into a 404 or a 500. Check how the old service answered and keep the same status codes. The output models need `from_attributes=True` to read ORM objects.

## 270: How does class-validator translate?

**Node.js**

```ts
class CreateProductDto {
  @IsString() @Length(3, 50) name: string;
  @IsNumber() @Min(0) price: number;
  @IsOptional() @IsArray() @IsString({ each: true }) tags?: string[];
}
```

**Python**

```python
from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

class CreateProduct(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=50)]
    price: float = Field(ge=0)
    tags: list[str] | None = None
```

Constraints sit on the type instead of in stacked decorators, and the type hints are what get validated, so there is nothing to keep in sync. Use `Decimal` instead of `float` for prices.

## 271: How do toJSON and custom serialization translate?

**Node.js**

```js
class Money {
  constructor(amount, currency) {
    Object.assign(this, { amount, currency });
  }
  toJSON() {
    return `${this.amount} ${this.currency}`;
  }
}
JSON.stringify({ price: new Money(5, "USD") });
```

**Python**

```python
from pydantic import BaseModel, field_serializer

class Product(BaseModel):
    price: Money

    @field_serializer("price")
    def ser_price(self, v: Money) -> str:
        return f"{v.amount} {v.currency}"

# plain json
json.dumps(data, default=lambda o: f"{o.amount} {o.currency}" if isinstance(o, Money) else str(o))
```

Python has no `toJSON` hook. Use Pydantic serializers, or pass a `default` function to `json.dumps` for types it cannot handle, such as `datetime`, `UUID` and `Decimal`.

## 272: How do Decimal and big numbers serialize to JSON?

**Node.js**

```js
JSON.stringify({ id: 123n }); // TypeError: Do not know how to serialize a BigInt
```

**Python**

```python
from decimal import Decimal

class Invoice(BaseModel):
    total: Decimal

Invoice(total=Decimal("10.50")).model_dump_json()   # '{"total":"10.50"}'
json.dumps({"total": Decimal("10.50")})              # TypeError
```

Pydantic writes `Decimal` as a JSON string by default to avoid precision loss. If the Node API sent numbers, check what clients expect and use a serializer that returns `float` only where precision does not matter.

## 273: How do ID generation strategies translate?

**Node.js**

```js
import { randomUUID } from "node:crypto";
import { ulid } from "ulid";
import { nanoid } from "nanoid";

randomUUID();
ulid();
nanoid();
```

**Python**

```python
import secrets
import uuid

str(uuid.uuid4())
str(uuid.uuid7())            # Python 3.14+: time-ordered, good for DB keys
secrets.token_urlsafe(16)   # nanoid-like
# ULID: uv add python-ulid
```

Keep the same ID format during migration, because clients and databases may depend on its length or sort order.

## 274: How does parsing dates from JSON translate?

**Node.js**

```js
const body = JSON.parse(text);
const created = new Date(body.createdAt); // strings stay strings until you convert
```

**Python**

```python
from datetime import datetime

class Event(BaseModel):
    created_at: datetime

event = Event.model_validate_json('{"created_at": "2026-11-24T10:00:00Z"}')
event.created_at.tzinfo   # UTC
```

Pydantic parses ISO strings and Unix timestamps into `datetime`. Watch out for strings without a timezone: they become naive datetimes. Use `AwareDatetime` to reject them.

## 275: What is the closure-in-a-loop pitfall in each language?

**Node.js**

```js
const fns = [];
for (var i = 0; i < 3; i++) fns.push(() => i);
fns.map((f) => f()); // [3, 3, 3] with var
for (let j = 0; j < 3; j++) fns.push(() => j); // let fixes it: [0, 1, 2]
```

**Python**

```python
fns = [lambda: i for i in range(3)]
[f() for f in fns]          # [2, 2, 2]

fns = [lambda i=i: i for i in range(3)]
[f() for f in fns]          # [0, 1, 2]
```

Python closures capture variables, not values, and loop variables are not per-iteration like `let`. Bind the current value with a default argument or `functools.partial`.

## 276: How does object equality translate?

**Node.js**

```js
const a = { x: 1 };
const b = { x: 1 };
a === b; // false
isDeepStrictEqual(a, b); // true (node:util)
```

**Python**

```python
a = {"x": 1}
b = {"x": 1}
a == b      # True
a is b      # False

@dataclass
class P:
    x: int
P(1) == P(1)    # True, dataclasses compare fields
```

Plain classes compare by identity unless they define `__eq__`. Dataclasses, Pydantic models, dicts, lists and tuples compare by value.

## 277: Why can't you use a list or dict as a dict key?

**Node.js**

```js
const m = new Map();
m.set([1, 2], "a"); // allowed, compared by reference
```

**Python**

```python
cache = {}
cache[[1, 2]] = "a"   # TypeError: unhashable type: 'list'
cache[(1, 2)] = "a"   # tuples are hashable
cache[frozenset({"a", "b"})] = 1
```

Dict keys must be hashable, which in practice means immutable. Python compares keys by value, so `(1, 2)` always finds the same entry. That is usually what a JavaScript developer actually wanted from a `Map` keyed by arrays.

## 278: How do string length and Unicode differ?

**Node.js**

```js
"😀".length; // 2 (UTF-16 code units)
[..."😀"].length; // 1
"é".normalize("NFC");
```

**Python**

```python
len("😀")              # 1 (code points)
len("😀".encode())     # 4 bytes in UTF-8
import unicodedata
unicodedata.normalize("NFC", "é")
```

Python counts code points, JavaScript counts UTF-16 units. A "max 10 characters" check can give different results for emoji, so align validation rules and test them with non-ASCII input.

## 279: How do multi-key and locale-aware sorts translate?

**Node.js**

```js
users.sort((a, b) => a.lastName.localeCompare(b.lastName) || b.age - a.age);
```

**Python**

```python
users.sort(key=lambda u: (u.last_name.casefold(), -u.age))

from functools import cmp_to_key
users.sort(key=cmp_to_key(lambda a, b: compare(a, b)))   # when you need a comparator
```

Tuple keys sort by the first item, then the next. `casefold()` is a simple case-insensitive sort, but not a true locale sort. For that, use `PyICU` or `locale.strxfrm` in a controlled process.

## 280: How do integer division and modulo differ?

**Node.js**

```js
-7 % 3; // -1
Math.floor(-7 / 3); // -3
Math.trunc(-7 / 3); // -2
```

**Python**

```python
-7 % 3     # 2
-7 // 3    # -3
int(-7 / 3)  # -2
import math
math.fmod(-7, 3)   # -1.0, like JavaScript's %
```

Python's `%` takes the sign of the divisor, JavaScript's takes the sign of the dividend. This silently changes results for negative numbers, for example in date math or hashing.

## 281: How does error cause chaining translate?

**Node.js**

```js
try {
  await db.query(sql);
} catch (err) {
  throw new Error("Failed to load user", { cause: err });
}
```

**Python**

```python
try:
    await db.execute(sql)
except DBError as err:
    raise UserLoadError("Failed to load user") from err
```

`raise ... from err` stores the original as `__cause__`, and the traceback shows both errors. Use `from None` to hide the original when it would leak internals.

## 282: How does AggregateError translate?

**Node.js**

```js
throw new AggregateError([err1, err2], "Several uploads failed");
```

**Python**

```python
raise ExceptionGroup("Several uploads failed", [err1, err2])

try:
    await upload_all()
except* TimeoutError as group:
    print("timeouts:", len(group.exceptions))
except* PermissionError:
    print("permission problems")
```

`except*` (Python 3.11+) handles each matching subset of an `ExceptionGroup`, and several `except*` clauses can run for one group. `TaskGroup` raises these groups when tasks fail.

## 283: How do you design an API error hierarchy?

**Node.js**

```ts
class AppError extends Error {
  constructor(
    public status: number,
    public code: string,
    message: string,
  ) {
    super(message);
  }
}
class NotFound extends AppError {
  constructor(what: string) {
    super(404, "not_found", `${what} not found`);
  }
}
```

**Python**

```python
class AppError(Exception):
    status = 500
    code = "internal"

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class NotFound(AppError):
    status = 404
    code = "not_found"

@app.exception_handler(AppError)
async def app_error(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse({"error": {"code": exc.code, "message": exc.message}}, status_code=exc.status)
```

Class attributes hold the status and code, so subclasses only override what changes. One handler for the base class covers the whole tree. Domain code raises domain errors and never imports the web framework.

## 284: How do abstract classes translate?

**Node.js**

```ts
abstract class Storage {
  abstract save(key: string, data: Buffer): Promise<void>;
  async saveJson(key: string, obj: unknown) {
    await this.save(key, Buffer.from(JSON.stringify(obj)));
  }
}
```

**Python**

```python
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    async def save(self, key: str, data: bytes) -> None: ...

    async def save_json(self, key: str, obj: object) -> None:
        await self.save(key, json.dumps(obj).encode())

Storage()   # TypeError: Can't instantiate abstract class
```

Unlike TypeScript, the check happens at runtime when you create an instance. Use `ABC` when you share code in the base class, and `Protocol` when you only need a shape.

## 285: How do mixins translate?

**Node.js**

```ts
const Timestamped = <T extends new (...a: any[]) => object>(Base: T) =>
  class extends Base {
    createdAt = new Date();
  };
class User extends Timestamped(BaseModel) {}
```

**Python**

```python
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

class User(TimestampMixin, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
```

Python's multiple inheritance makes mixins a plain class listed first in the bases. SQLAlchemy and Django models use them often for shared columns.

## 286: How do Symbol.iterator and similar protocols translate?

**Node.js**

```js
class Range {
  constructor(n) {
    this.n = n;
  }
  *[Symbol.iterator]() {
    for (let i = 0; i < this.n; i++) yield i;
  }
}
[...new Range(3)];
```

**Python**

```python
class Range:
    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self):
        yield from range(self.n)

    def __len__(self) -> int:
        return self.n

    def __contains__(self, x: int) -> bool:
        return 0 <= x < self.n

list(Range(3))
2 in Range(3)
```

Python's "dunder" methods (`__iter__`, `__len__`, `__contains__`, `__getitem__`) make built-in syntax work on your objects, much like well-known symbols do in JavaScript, but there are many more of them.

## 287: How does operator overloading work, which JavaScript lacks?

**Node.js**

```js
// No operator overloading: you call methods
const total = a.add(b);
```

**Python**

```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

total = Money(Decimal("5"), "USD") + Money(Decimal("3"), "USD")
```

Use operators only where they read naturally, such as value objects like money, vectors or dates. Keep `.add()` style methods for anything with side effects.

## 288: How does custom object printing translate?

**Node.js**

```js
import { inspect } from "node:util";

class User {
  [inspect.custom]() {
    return `User<${this.id}>`;
  }
}
```

**Python**

```python
class User:
    def __init__(self, id: int, email: str) -> None:
        self.id, self.email = id, email

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"

    def __str__(self) -> str:
        return self.email
```

`__repr__` is for developers and logs, `__str__` is for users. Keep secrets out of `__repr__`, because tracebacks and debuggers print it. Pydantic's `SecretStr` hides values for you.

## 289: How does Object.freeze translate?

**Node.js**

```js
const ROLES = Object.freeze(["admin", "user"]);
const CONFIG = Object.freeze({ retries: 3 });
```

**Python**

```python
from types import MappingProxyType

ROLES = ("admin", "user")                   # tuple
ALLOWED = frozenset({"png", "jpg"})
CONFIG = MappingProxyType({"retries": 3})   # read-only view of a dict
# Python 3.15+: frozendict({"retries": 3})
```

Like `Object.freeze`, these are shallow: a tuple holding a list still lets the list change. Python 3.15 adds a built-in `frozendict` type.

## 290: How do WeakMap and WeakRef translate?

**Node.js**

```js
const meta = new WeakMap();
meta.set(obj, { seen: true });
const ref = new WeakRef(obj);
```

**Python**

```python
import weakref

meta = weakref.WeakKeyDictionary()
meta[obj] = {"seen": True}
ref = weakref.ref(obj)
ref()   # the object, or None if collected

cache = weakref.WeakValueDictionary()
```

Not every object can be weakly referenced: `int`, `str`, `tuple` and classes with `__slots__` (without `__weakref__`) cannot.

## 291: How does Proxy translate?

**Node.js**

```js
const logged = new Proxy(target, {
  get(t, prop) {
    console.log("get", prop);
    return Reflect.get(t, prop);
  },
});
```

**Python**

```python
class Logged:
    def __init__(self, target: object) -> None:
        self._target = target

    def __getattr__(self, name: str):
        print("get", name)
        return getattr(self._target, name)
```

`__getattr__` runs only when normal lookup fails, which makes it a safe hook for wrappers and lazy loading. `__getattribute__` runs on every access and is easy to get wrong.

## 292: How does reflection translate?

**Node.js**

```js
Object.keys(obj);
obj[methodName]?.();
Object.getOwnPropertyNames(Object.getPrototypeOf(obj));
```

**Python**

```python
vars(obj)                          # instance attributes as a dict
getattr(obj, method_name)()
hasattr(obj, "save")
setattr(obj, "name", "Ana")
import inspect
inspect.signature(func).parameters   # parameter names, defaults, hints
```

`inspect.signature` is how FastAPI reads your handler's parameters. Calling methods by a user-supplied name is a security risk in both languages, so check names against an allow list.

## 293: How do dynamic imports translate?

**Node.js**

```js
const { default: plugin } = await import(`./plugins/${name}.js`);
```

**Python**

```python
import importlib

plugin = importlib.import_module(f"app.plugins.{name}")
plugin.run()
```

`import_module` is synchronous and caches modules in `sys.modules`. Validate `name` against a known list first, so user input cannot load any module on the path.

## 294: How do plugin systems translate?

**Node.js**

```json
{ "keywords": ["myapp-plugin"], "main": "index.js" }
```

**Python**

```toml
# in the plugin's pyproject.toml
[project.entry-points."myapp.plugins"]
csv_export = "myapp_csv:plugin"
```

```python
from importlib.metadata import entry_points

for ep in entry_points(group="myapp.plugins"):
    plugin = ep.load()
    plugin.register(app)
```

Entry points are Python's standard way for installed packages to announce plugins. pytest, Flake8 and many CLIs find their plugins this way.

## 295: How do CLI frameworks like commander translate?

**Node.js**

```js
import { Command } from "commander";

const program = new Command();
program
  .command("import <file>")
  .option("--dry-run")
  .action((file, opts) => runImport(file, opts.dryRun));
program.parse();
```

**Python**

```python
# uv add typer
import typer

app = typer.Typer()

@app.command("import")
def import_cmd(file: str, dry_run: bool = False) -> None:
    run_import(file, dry_run)

if __name__ == "__main__":
    app()
```

Typer builds arguments and options from type hints (`dry_run: bool = False` becomes `--dry-run`). Click is the older, more explicit library that Typer is built on.

## 296: How does the bin field translate?

**Node.js**

```json
{ "bin": { "mytool": "./bin/cli.js" } }
```

**Python**

```toml
[project.scripts]
mytool = "mytool.cli:app"
```

```bash
uv tool install .      # installs mytool globally, like npm i -g
```

The installer creates a small launcher script that imports the module and calls the object, so you don't need a shebang or executable bit.

## 297: How does a library's folder layout translate?

**Node.js**

```text
my-lib/
  package.json
  src/index.ts
  dist/
  test/
```

**Python**

```text
my-lib/
  pyproject.toml
  src/my_lib/
    __init__.py
    py.typed        # tells type checkers the package has hints
  tests/
```

The `src/` layout stops tests from importing the local folder by accident instead of the installed package. `uv init --lib` creates this layout. There is no `dist/` build output to commit, because Python ships source files.

## 298: How do TypeScript path aliases translate?

**Node.js**

```json
{ "compilerOptions": { "paths": { "@/*": ["./src/*"] } } }
```

**Python**

```python
# with the package installed (uv sync installs the project in editable mode)
from my_app.users.service import UsersService
```

Python has no path aliases because you import by package name, and absolute imports from the package root already read like `@/users/service`. Avoid editing `sys.path` or `PYTHONPATH` to make imports work. Install the project instead.

## 299: Which runtime errors show up most after a translation?

**Node.js**

```js
user.profile.name; // TypeError: Cannot read properties of undefined
obj.missing; // undefined, no error
```

**Python**

```python
user["profile"]["name"]   # KeyError: 'profile'
user.profile.name         # AttributeError: 'NoneType' object has no attribute 'name'
"Total: " + 5             # TypeError: can only concatenate str (not "int") to str
int("12.5")               # ValueError
```

Python raises errors where JavaScript returns `undefined` or coerces types. That is good, because bugs surface sooner, but code that relied on JavaScript's quiet behavior must handle missing data explicitly. Type checking catches most `None` errors before runtime.

## 300: How do you compare the performance of the old and new service?

**Node.js**

```bash
npx autocannon -c 100 -d 30 http://localhost:3000/api/orders
```

**Python**

```bash
# the same load tool against both services keeps the numbers fair
k6 run --vus 100 --duration 30s load.js
uvx locust -f locustfile.py --host http://localhost:8000
```

Run the same scenario against both services with the same database, the same data and production-like worker counts. Compare p50/p95/p99 latency, throughput, error rate, CPU and memory per instance. Python often needs more processes for the same throughput, so compare cost per request, not only raw speed.

# Advanced Questions (301-450)

## 301: How do the event loops of Node.js and asyncio differ under the hood?

Node.js runs on libuv. The loop has fixed phases (timers, pending callbacks, poll, check, close), and between every callback it drains the microtask queue (`process.nextTick`, then promise jobs). File system work, DNS and some crypto run on libuv's thread pool.

asyncio's loop is written in Python (with C parts) on top of `selectors` (epoll or kqueue). It keeps a ready queue of callbacks and a heap of timers. Each loop step runs every callback that is ready, and coroutines resume as callbacks when their futures complete. There are no phases and no separate microtask queue. Files have no async OS API in asyncio, so file work goes to threads.

**Node.js**

```js
setTimeout(() => console.log("timeout"), 0);
setImmediate(() => console.log("immediate"));
Promise.resolve().then(() => console.log("microtask")); // always first
```

**Python**

```python
async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_later(0, print, "timer")
    loop.call_soon(print, "soon")   # FIFO order within the ready queue
    await asyncio.sleep(0)          # yield once to let ready callbacks run
```

## 302: How do the GIL and free-threaded Python change the concurrency story?

Node.js runs JavaScript on one thread per isolate. Parallelism needs worker threads with separate heaps that share memory only through `SharedArrayBuffer`.

Standard CPython has a Global Interpreter Lock: threads share all objects, but only one runs Python bytecode at a time. Threads still help for I/O and for C extensions that release the GIL. Python 3.13 added an experimental free-threaded build (`python3.13t`) without the GIL, and Python 3.14 made it officially supported (PEP 779). It runs threads in parallel, but single-thread code is somewhat slower and some C extensions are not ready yet.

**Node.js**

```js
new Worker("./cpu.js"); // separate heap, message passing
```

**Python**

```python
import sys
from concurrent.futures import ThreadPoolExecutor

print(sys._is_gil_enabled())   # False on a free-threaded build

with ThreadPoolExecutor(8) as ex:
    results = list(ex.map(cpu_heavy, chunks))   # parallel only without the GIL
```

## 303: Is there an equivalent of process.nextTick and microtasks in asyncio?

No. In Node.js, `process.nextTick` callbacks run before promise callbacks, and both run before the loop moves on, so a long chain of microtasks can starve I/O.

In asyncio, `await` on a coroutine that does not block runs straight through without yielding to the loop at all. A coroutine only gives up control when it awaits a future that is not done yet. To yield on purpose, use `await asyncio.sleep(0)`. `loop.call_soon` puts a callback at the end of the ready queue, which is the closest match to `setImmediate`.

**Node.js**

```js
async function busy() {
  for (let i = 0; i < 1e6; i++) await null; // each await yields to microtasks only
}
```

**Python**

```python
async def busy() -> None:
    for i in range(1_000_000):
        if i % 1000 == 0:
            await asyncio.sleep(0)   # let other tasks and I/O run
```

## 304: What is uvloop and when does it matter?

`uvloop` replaces asyncio's default loop with one built on libuv, the same library Node.js uses. It speeds up socket-heavy workloads noticeably. Uvicorn uses it automatically when it is installed (`uvicorn[standard]`). It doesn't help CPU-bound Python code, which is usually the real bottleneck.

**Node.js**

```js
// libuv is always the loop
```

**Python**

```python
import asyncio
import uvloop

asyncio.run(main(), loop_factory=uvloop.new_event_loop)   # Python 3.12+
# or simply: uvloop.run(main())
```

## 305: What are WSGI and ASGI, and how do they compare to Node's http module?

Node.js apps receive `(req, res)` from the built-in HTTP server. Python separates server and app through standard interfaces:

- **WSGI** (PEP 3333): a sync callable `app(environ, start_response)` that returns the body. One request holds one thread. Flask and classic Django use it.
- **ASGI**: an async callable `app(scope, receive, send)` that supports long-lived connections like WebSockets and streaming. FastAPI, Starlette and Django's async mode use it.

**Node.js**

```js
createServer((req, res) => res.end("hi")).listen(3000);
```

**Python**

```python
async def app(scope, receive, send):   # minimal ASGI app
    assert scope["type"] == "http"
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"text/plain")]})
    await send({"type": "http.response.body", "body": b"hi"})
# uvicorn module:app
```

Because of this split, any ASGI server runs any ASGI framework, and middleware can be shared across frameworks.

## 306: How do you size worker processes compared to a Node.js cluster?

A Node.js process handles thousands of concurrent I/O requests on one core, so you run about one process per core.

For async Python (Uvicorn), the same rule applies: one worker per core, since each worker has its own event loop. For sync Python (Gunicorn with Flask or Django), concurrency equals workers times threads, so you need more: a common start is `(2 × cores) + 1` workers, plus threads for I/O-heavy apps. Every worker is a full copy of the app in memory, so memory often limits worker count before CPU does.

**Node.js**

```bash
pm2 start server.js -i 4
```

**Python**

```bash
gunicorn app:app --workers 9 --threads 4 --timeout 30 --max-requests 2000 --max-requests-jitter 200
uvicorn app.main:app --workers 4
```

`--max-requests` restarts workers now and then, which limits slow memory leaks.

## 307: How do you handle CPU-bound work in each runtime?

In Node.js, CPU work blocks the loop, so you move it to `worker_threads` (Piscina for pools) or a separate service. In Python, CPU work in an async route blocks the loop, and threads don't run it in parallel under the GIL. Your options are:

1. `ProcessPoolExecutor` for pure-Python CPU work.
2. Libraries that run in C and release the GIL (NumPy, Pillow, hashlib, orjson). Threads work fine for these.
3. A job queue (Celery) to keep heavy work out of the request path.
4. The free-threaded build or subinterpreters for newer setups.

**Node.js**

```js
const pool = new Piscina({
  filename: new URL("./worker.js", import.meta.url).href,
});
const out = await pool.run(input);
```

**Python**

```python
pool = ProcessPoolExecutor(max_workers=os.process_cpu_count())

@app.post("/score")
async def score(data: Input) -> dict:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(pool, compute_score, data.model_dump())
```

## 308: How does memory management differ between V8 and CPython?

V8 uses a generational tracing garbage collector with a young generation (scavenged often) and an old generation (mark-sweep-compact). Memory is freed in batches, and heap size is capped by `--max-old-space-size`.

CPython uses reference counting: an object is freed as soon as its last reference goes away. A separate cyclic collector (the `gc` module) cleans up reference cycles. That gives predictable cleanup, but cycles with many objects can cause pauses, and CPython rarely returns freed memory to the OS, so the process size tends to stay at its peak.

**Node.js**

```bash
node --max-old-space-size=2048 server.js
```

**Python**

```python
import gc

gc.freeze()          # after startup: move objects out of GC tracking (helps with fork)
gc.get_count()
```

There is no heap size flag in Python. Limit memory with the container and restart workers with `--max-requests`.

## 309: How do you find memory leaks in each?

**Node.js**

```bash
node --inspect server.js     # take heap snapshots in DevTools and compare
node --heapsnapshot-signal=SIGUSR2 server.js
```

**Python**

```python
import tracemalloc

tracemalloc.start(25)
before = tracemalloc.take_snapshot()
# ... run traffic ...
after = tracemalloc.take_snapshot()
for stat in after.compare_to(before, "traceback")[:10]:
    print(stat)
```

```bash
uvx memray run -o out.bin app.py && uvx memray flamegraph out.bin
```

Common Python leaks are unbounded module-level caches, `lru_cache` on methods (it keeps `self` alive), growing lists of task references, and C extension leaks that `tracemalloc` cannot see. `memray` tracks native allocations too.

## 310: How do you profile a live production process?

**Node.js**

```bash
node --cpu-prof server.js
npx 0x server.js
```

**Python**

```bash
uvx py-spy top --pid 1234
uvx py-spy dump --pid 1234                  # stack of every thread right now
uvx py-spy record --pid 1234 -o flame.svg --duration 30
# Python 3.15: python -m profiling.sampling (the built-in sampling profiler)
```

Sampling profilers read the interpreter's stacks from outside the process, so you don't need code changes or restarts, and the overhead is tiny. `py-spy dump` is the fastest way to see what a stuck worker is doing. In containers, you may need the `SYS_PTRACE` capability.

## 311: How do startup times compare, and what can you do about slow imports?

Node.js starts quickly, and bundlers can trim the code it loads. Python imports every module at startup, and large libraries (pandas, boto3, SQLAlchemy) can add seconds, which hurts CLIs, serverless cold starts and autoscaling.

**Node.js**

```js
const { heavy } = await import("./heavy.js"); // load only when needed
```

**Python**

```python
def export_report():
    import pandas as pd       # deferred import inside the function
    ...

# Python 3.15: lazy imports (PEP 810)
lazy import pandas as pd      # loaded on first use
```

```bash
python -X importtime -c "import app.main" 2>&1 | sort -t'|' -k2 -n | tail
```

`-X importtime` shows which imports cost the most.

## 312: How do serverless cold starts compare?

Both Node.js and Python are fast-starting Lambda runtimes. Cold start time depends on package size and import work in both. Python gets slower when a function imports big libraries or ships large compiled dependencies.

**Node.js**

```js
// bundle with esbuild, create clients outside the handler
const s3 = new S3Client({});
export const handler = async (event) => ({ statusCode: 200, body: "ok" });
```

**Python**

```python
import boto3

s3 = boto3.client("s3")   # created once per container, reused across calls

def handler(event, context):
    return {"statusCode": 200, "body": "ok"}
```

Keep the deployment package small, create clients at module level, and import rarely used libraries inside the code path that needs them. Lambda SnapStart is available for Python and helps with heavy imports. For running a FastAPI app on Lambda, `Mangum` adapts ASGI to Lambda events.

## 313: How does backpressure translate?

In Node.js streams, `write()` returns `false` when the buffer is full, and `pipeline()` handles waiting for `drain` for you.

In asyncio, `StreamWriter.write()` buffers without limit, so you must `await writer.drain()` to wait for the buffer to empty. Between tasks, a bounded `asyncio.Queue` makes producers wait. In ASGI, `await send(...)` applies backpressure by waiting until the server can take more data.

**Node.js**

```js
if (!socket.write(chunk)) await once(socket, "drain");
```

**Python**

```python
reader, writer = await asyncio.open_connection(host, port)
for chunk in chunks:
    writer.write(chunk)
    await writer.drain()   # waits when the transport buffer is above its high-water mark
```

Without bounded queues and `drain()`, a slow consumer makes a fast producer fill memory until the process is killed.

## 314: How do you clean up async generators safely?

**Node.js**

```js
async function* rows() {
  const conn = await pool.connect();
  try {
    yield* conn.stream();
  } finally {
    conn.release(); // runs when the for-await loop breaks
  }
}
```

**Python**

```python
from contextlib import aclosing

async def rows():
    conn = await pool.acquire()
    try:
        async for row in conn.cursor("SELECT ..."):
            yield row
    finally:
        await pool.release(conn)

async with aclosing(rows()) as gen:
    async for row in gen:
        if done(row):
            break   # aclosing makes sure finally runs now
```

In JavaScript, breaking out of `for await` calls `return()` right away. In Python, an abandoned async generator is only finalized later by the event loop, so cleanup can be late or happen in the wrong task. Wrap generators that hold resources in `contextlib.aclosing`.

## 315: Why must you not swallow CancelledError?

Cancellation in asyncio is an exception (`CancelledError`, a `BaseException` subclass) thrown into the task at its current `await`. If your code catches and ignores it, the task keeps running. Then timeouts, `TaskGroup` and server shutdown stop working.

**Node.js**

```js
try {
  await fetch(url, { signal });
} catch (err) {
  if (err.name === "AbortError") return; // returning is fine in JS
}
```

**Python**

```python
async def worker() -> None:
    try:
        await do_work()
    except asyncio.CancelledError:
        await cleanup()
        raise              # always re-raise
    except Exception:
        log.exception("work failed")   # Exception does not catch CancelledError
```

Since Python 3.8, `CancelledError` does not inherit from `Exception`, so `except Exception` is safe. Bare `except:` and `except BaseException:` must re-raise.

## 316: How do you protect work from cancellation?

**Node.js**

```js
// just don't pass the signal to the operation that must finish
await saveAudit(entry);
```

**Python**

```python
async def handle() -> None:
    await asyncio.shield(save_audit(entry))   # the inner task keeps running if handle() is cancelled

# stronger: hand it to a task owned by something longer-lived
background_tasks: set[asyncio.Task] = set()
task = asyncio.create_task(save_audit(entry))
background_tasks.add(task)
task.add_done_callback(background_tasks.discard)
```

`shield` stops cancellation from reaching the inner task, but the outer `await` still raises `CancelledError`. Use it for short, important writes, and keep references to shielded tasks so they aren't garbage collected.

## 317: How do nested timeouts behave?

**Node.js**

```js
const signal = AbortSignal.any([AbortSignal.timeout(5000), req.signal]);
await fetch(url, { signal });
```

**Python**

```python
async with asyncio.timeout(5):              # whole request budget
    user = await get_user(uid)
    async with asyncio.timeout(1):          # tighter limit for one call
        recs = await get_recommendations(uid)

# reschedule a deadline
async with asyncio.timeout(None) as cm:
    cm.reschedule(asyncio.get_running_loop().time() + 2)
```

The inner timeout raises `TimeoutError` at its own block, and the outer one still applies. Only the context manager that fired turns the cancellation into `TimeoutError`, so nested timeouts don't confuse each other. `AbortSignal.any` is the JavaScript way to combine deadlines.

## 318: How do contextvars behave with tasks and threads compared to AsyncLocalStorage?

**Node.js**

```js
als.run({ requestId }, () => {
  setTimeout(() => console.log(als.getStore().requestId), 10); // still available
});
```

**Python**

```python
async def handler() -> None:
    request_id.set("abc")
    asyncio.create_task(child())                 # child gets a copy of the context
    await asyncio.to_thread(sync_work)           # to_thread copies the context too
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_work)  # does NOT copy it

import contextvars
ctx = contextvars.copy_context()
await loop.run_in_executor(None, ctx.run, sync_work)
```

Each task gets a copy of the context at creation, so changes in a child task don't leak back to the parent. `asyncio.to_thread` copies context, but `run_in_executor` does not, which is a common source of missing request IDs in logs.

## 319: What thread-safety issues appear in Python that Node.js developers don't expect?

Node.js code never runs two JavaScript callbacks at the same time on one thread, so shared state is safe between `await` points. Python sync web apps (Flask, Django, FastAPI `def` routes) run handlers in parallel threads that share module-level objects. Even with the GIL, `x += 1` is not atomic, and a check-then-set on a dict can race.

**Node.js**

```js
let counter = 0;
app.get("/", (req, res) => {
  counter++; // safe
  res.end();
});
```

**Python**

```python
import threading

counter = 0
lock = threading.Lock()

@app.get("/")
def index() -> dict:
    global counter
    with lock:
        counter += 1
    return {"count": counter}
```

The free-threaded build makes these races more likely. Even in pure asyncio code, state can change between two `await`s, so use `asyncio.Lock` around read-modify-write sequences that await.

## 320: How do you size database pools for async workers?

In Node.js, one process with a pool of 10-20 connections is typical. In Python, the total equals workers × pods × (pool size + overflow). With an async engine, many coroutines share a small pool. When the pool runs out, requests wait for `pool_timeout` and then fail.

**Node.js**

```js
new pg.Pool({ max: 20 });
```

**Python**

```python
engine = create_async_engine(url, pool_size=5, max_overflow=5, pool_timeout=3)
# 4 workers x 10 pods x 10 = 400 connections: probably too many for Postgres
```

Put PgBouncer in transaction mode in front of Postgres when the counts grow. With asyncpg and PgBouncer, turn off prepared statement caching (`connect_args={"statement_cache_size": 0}`) or use PgBouncer 1.21+ with prepared statement support.

## 321: What async SQLAlchemy pitfalls catch Node.js developers?

Prisma always returns plain objects. SQLAlchemy returns tracked objects tied to a session, and accessing an unloaded relation tries lazy loading. In async code that raises `MissingGreenlet`, because lazy loads would need hidden I/O.

**Node.js**

```ts
const user = await prisma.user.findUnique({ where: { id } });
user.posts; // undefined unless included: no hidden queries
```

**Python**

```python
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

user = await session.get(User, uid, options=[selectinload(User.posts)])
user.posts   # loaded

class Base(AsyncAttrs, DeclarativeBase): ...
posts = await user.awaitable_attrs.posts   # explicit async lazy load
```

Also set `expire_on_commit=False`. Otherwise reading attributes after `commit()` triggers a reload, which fails the same way. Setting `lazy="raise"` on relationships makes forgotten eager loads fail loudly in tests.

## 322: How do you detect and fix N+1 queries?

**Node.js**

```ts
const posts = await prisma.post.findMany();
for (const p of posts)
  await prisma.user.findUnique({ where: { id: p.authorId } }); // N+1
```

**Python**

```python
posts = (await session.scalars(select(Post).options(selectinload(Post.author)))).all()

# find them: log every SQL statement in development
engine = create_async_engine(url, echo=True)
```

In Django, use `select_related` for foreign keys and `prefetch_related` for reverse and many-to-many relations, and `django-debug-toolbar` or `nplusone` to spot problems. In GraphQL, use a DataLoader in both stacks.

## 323: How do optimistic locking and isolation levels translate?

**Node.js**

```ts
const res = await prisma.doc.updateMany({
  where: { id, version },
  data: { body, version: { increment: 1 } },
});
if (res.count === 0) throw new ConflictError();
```

**Python**

```python
class Doc(Base):
    __tablename__ = "docs"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str]
    version: Mapped[int] = mapped_column(default=1)
    __mapper_args__ = {"version_id_col": version}

# SQLAlchemy adds "WHERE version = :old" to updates and raises StaleDataError on conflict

engine = create_async_engine(url, isolation_level="REPEATABLE READ")
async with session.begin():
    row = await session.scalar(select(Account).where(Account.id == aid).with_for_update())
```

`version_id_col` does what the hand-written `updateMany` check did. `with_for_update()` adds `SELECT ... FOR UPDATE` for pessimistic locking.

## 324: How do you run zero-downtime schema migrations during a language switch?

Both services may use the same database for weeks, so every schema change must work with both the Node.js and the Python code. Use expand and contract:

1. Expand: add new columns or tables as nullable, with no breaking changes.
2. Deploy code that writes to both the old and new shape.
3. Backfill data in batches.
4. Switch reads to the new shape.
5. Contract: drop the old columns once no code uses them.

Pick one migration tool as the owner. If Prisma Migrate owns the schema, don't let Alembic autogenerate against it, or the two will fight. Moving ownership to Alembic is a single step: create a baseline revision and `alembic stamp head`.

**Node.js**

```bash
npx prisma migrate deploy   # owner until the cutover
```

**Python**

```bash
alembic revision -m "baseline from prisma"   # empty migration
alembic stamp head                           # mark the current DB as up to date
```

## 325: How do you stream large query results without loading them into memory?

**Node.js**

```js
import QueryStream from "pg-query-stream";

const stream = client.query(new QueryStream("SELECT * FROM events"));
for await (const row of stream) process(row);
```

**Python**

```python
result = await session.stream_scalars(
    select(Event).execution_options(yield_per=1000)
)
async for event in result:
    process(event)

# Django
for e in Event.objects.iterator(chunk_size=1000):
    process(e)
```

Server-side cursors fetch rows in batches. They hold a connection and a transaction open for the whole loop, so keep the processing fast or copy to a file first.

## 326: How do distributed locks translate?

**Node.js**

```js
import Redlock from "redlock";

const redlock = new Redlock([redis]);
await redlock.using(["lock:report"], 30_000, async () => buildReport());
```

**Python**

```python
import redis.asyncio as redis

r = redis.from_url(REDIS_URL)

async with r.lock("lock:report", timeout=30, blocking_timeout=5):
    await build_report()
```

redis-py's `Lock` uses `SET NX PX` with a unique token and a Lua script for safe release. Locks can expire while work is still running, so make the protected work idempotent or use fencing tokens. Don't treat a Redis lock as a correctness guarantee.

## 327: How do you implement idempotency keys?

**Node.js**

```js
app.post("/payments", async (req, res) => {
  const key = req.get("Idempotency-Key");
  const cached = await redis.get(`idem:${key}`);
  if (cached) return res.status(200).json(JSON.parse(cached));
  const result = await charge(req.body);
  await redis.set(`idem:${key}`, JSON.stringify(result), "EX", 86400);
  res.status(201).json(result);
});
```

**Python**

```python
from fastapi import Header

@app.post("/payments", status_code=201)
async def pay(data: PaymentIn, idempotency_key: str = Header()) -> dict:
    redis_key = f"idem:{idempotency_key}"
    if not await r.set(redis_key, "pending", nx=True, ex=86400):
        cached = await r.get(redis_key)
        if cached is None or cached in (b"pending", "pending"):
            raise HTTPException(409, "Request in progress")
        return JSONResponse(json.loads(cached), status_code=200)
    result = await charge(data)
    await r.set(redis_key, json.dumps(result), ex=86400)
    return result
```

Claim the key atomically with `SET NX` before doing the work. The Node version above checks and then writes separately, so two parallel retries can both charge the card. Translating is a good moment to fix bugs like that, but list them so reviewers know the behavior changed.

## 328: How does the transactional outbox pattern translate?

**Node.js**

```ts
await prisma.$transaction([
  prisma.order.create({ data: order }),
  prisma.outbox.create({ data: { topic: "order.created", payload: order } }),
]);
```

**Python**

```python
async with session.begin():
    session.add(Order(**order))
    session.add(Outbox(topic="order.created", payload=order))

# relay worker
async def relay() -> None:
    while True:
        async with session.begin():
            rows = (await session.scalars(
                select(Outbox).where(Outbox.sent_at.is_(None))
                .order_by(Outbox.id).limit(100).with_for_update(skip_locked=True)
            )).all()
            for row in rows:
                await producer.send_and_wait(row.topic, json.dumps(row.payload).encode())
                row.sent_at = datetime.now(UTC)
        await asyncio.sleep(1)
```

`FOR UPDATE SKIP LOCKED` lets several relay workers run without sending the same row twice. Consumers must still handle duplicates, because the relay can crash after sending but before committing.

## 329: How does KafkaJS translate?

**Node.js**

```js
const consumer = kafka.consumer({ groupId: "billing" });
await consumer.subscribe({ topic: "orders" });
await consumer.run({
  eachMessage: async ({ message }) => handle(JSON.parse(message.value)),
});
```

**Python**

```python
# uv add aiokafka
from aiokafka import AIOKafkaConsumer

consumer = AIOKafkaConsumer("orders", bootstrap_servers=BROKERS, group_id="billing",
                            enable_auto_commit=False)
await consumer.start()
try:
    async for msg in consumer:
        await handle(json.loads(msg.value))
        await consumer.commit()
finally:
    await consumer.stop()
```

`aiokafka` is pure asyncio. `confluent-kafka` wraps librdkafka and is faster, with an async API in recent versions. KafkaJS is no longer actively maintained, so many Node teams were moving to Confluent's client anyway.

## 330: How does amqplib translate for RabbitMQ?

**Node.js**

```js
const ch = await conn.createChannel();
await ch.prefetch(10);
ch.consume("emails", async (msg) => {
  await send(JSON.parse(msg.content));
  ch.ack(msg);
});
```

**Python**

```python
# uv add aio-pika
import aio_pika

conn = await aio_pika.connect_robust(AMQP_URL)
channel = await conn.channel()
await channel.set_qos(prefetch_count=10)
queue = await channel.declare_queue("emails", durable=True)

async with queue.iterator() as it:
    async for message in it:
        async with message.process(requeue=True):   # ack on success, nack on error
            await send(json.loads(message.body))
```

`connect_robust` reconnects and restores channels after network failures, which amqplib leaves to you. `message.process()` handles ack and nack in one block.

## 331: How does gRPC translate?

**Node.js**

```js
const server = new grpc.Server();
server.addService(proto.Users.service, {
  getUser: (call, cb) => cb(null, { id: call.request.id }),
});
```

**Python**

```bash
uv add grpcio grpcio-tools
python -m grpc_tools.protoc -I proto --python_out=gen --pyi_out=gen --grpc_python_out=gen proto/users.proto
```

```python
import grpc
from gen import users_pb2, users_pb2_grpc

class Users(users_pb2_grpc.UsersServicer):
    async def GetUser(self, request, context):
        return users_pb2.User(id=request.id)

server = grpc.aio.server()
users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
server.add_insecure_port("[::]:50051")
await server.start()
await server.wait_for_termination()
```

The `.proto` files stay the same, which makes gRPC services among the easiest to translate. Contract compatibility is guaranteed by the shared schema.

## 332: How does OpenTelemetry instrumentation translate?

**Node.js**

```js
// node --import ./otel.js server.js
import { NodeSDK } from "@opentelemetry/sdk-node";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";
new NodeSDK({ instrumentations: [getNodeAutoInstrumentations()] }).start();
```

**Python**

```bash
uv add opentelemetry-distro opentelemetry-exporter-otlp
uv run opentelemetry-bootstrap -a requirements   # lists instrumentations for installed libs
OTEL_SERVICE_NAME=orders opentelemetry-instrument uvicorn app.main:app
```

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("charge-card") as span:
    span.set_attribute("order.id", order_id)
```

Both auto-instrument HTTP servers, clients, database drivers and queues. Keep the same service names and span attribute names during the migration, so dashboards keep working across both services.

## 333: How do Prometheus metrics differ with multiple Python workers?

**Node.js**

```js
import client from "prom-client";

const httpRequests = new client.Counter({
  name: "http_requests_total",
  help: "...",
  labelNames: ["route"],
});
// with cluster, use AggregatorRegistry to merge workers
```

**Python**

```python
from prometheus_client import Counter, make_asgi_app

http_requests = Counter("http_requests_total", "HTTP requests", ["route"])
app.mount("/metrics", make_asgi_app())
```

```bash
# with several Gunicorn or Uvicorn workers, each process has its own counters
export PROMETHEUS_MULTIPROC_DIR=/tmp/prom
```

Each worker process keeps its own metrics, so a scrape hits one random worker and sees partial numbers. Set `PROMETHEUS_MULTIPROC_DIR` and use `MultiProcessCollector`, or push metrics through OpenTelemetry instead. This is the same problem as Node cluster, but more common, because Python almost always runs several processes.

## 334: How do you keep log correlation across services?

**Node.js**

```js
const log = pino({ mixin: () => ({ requestId: als.getStore()?.requestId }) });
```

**Python**

```python
import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars, merge_contextvars

structlog.configure(processors=[merge_contextvars, structlog.processors.JSONRenderer()])

@app.middleware("http")
async def bind_ids(request: Request, call_next):
    clear_contextvars()
    bind_contextvars(request_id=request.headers.get("x-request-id") or str(uuid.uuid4()))
    return await call_next(request)
```

Use the same field names as the Node service (`requestId` vs `request_id` matters for log queries), and pass the ID or W3C `traceparent` header on every outgoing call.

## 335: How does Sentry error tracking translate?

**Node.js**

```js
import * as Sentry from "@sentry/node";

Sentry.init({ dsn: process.env.SENTRY_DSN, tracesSampleRate: 0.1 });
```

**Python**

```python
import sentry_sdk

sentry_sdk.init(dsn=settings.sentry_dsn, traces_sample_rate=0.1, send_default_pii=False)
```

The Python SDK turns on integrations for FastAPI, Flask, Django, Celery and SQLAlchemy automatically when they are installed. Tag events with a `service.runtime` value so you can compare error rates between the old and new services.

## 336: How does SQL injection risk compare?

Both stacks are safe when you use parameters and unsafe when you build SQL strings. Python adds a trap: f-strings make string building look harmless.

**Node.js**

```js
await pool.query(`SELECT * FROM users WHERE email = '${email}'`); // unsafe
await pool.query("SELECT * FROM users WHERE email = $1", [email]); // safe
```

**Python**

```python
await session.execute(text(f"SELECT * FROM users WHERE email = '{email}'"))  # unsafe
await session.execute(text("SELECT * FROM users WHERE email = :email"), {"email": email})  # safe

# dynamic column names: allow-list them, parameters can't hold identifiers
SORTABLE = {"name": User.name, "created": User.created_at}
stmt = select(User).order_by(SORTABLE.get(sort, User.id))
```

Ruff's `S608` rule and Bandit flag string-built SQL. Django's `.extra()` and `.raw()` with string formatting have the same risk.

## 337: Is there a Python equivalent of prototype pollution?

Not directly. Python objects have no shared prototype chain that a JSON key like the proto key can change. The closest risks are:

- Using `setattr(obj, key, value)` with user-controlled keys, which can overwrite methods or internal attributes.
- Unsafe deserializers: `pickle.loads`, `yaml.load` without `SafeLoader`, and `eval` can run code.
- Mass assignment: `User(**request_json)` can set fields like `is_admin`.

**Node.js**

```js
Object.assign(user, req.body); // mass assignment and pollution risk
```

**Python**

```python
class UserUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")   # reject unknown fields
    name: str | None = None

for k, v in UserUpdate.model_validate(body).model_dump(exclude_unset=True).items():
    setattr(user, k, v)   # only allow-listed fields
```

## 338: How do you prevent SSRF in each stack?

**Node.js**

```js
// resolve, check for private ranges, then connect to the checked IP
```

**Python**

```python
import ipaddress
import socket
from urllib.parse import urlparse

def check_public(url: str) -> None:
    host = urlparse(url).hostname
    if host is None:
        raise ValueError("No host")
    for info in socket.getaddrinfo(host, None):
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            raise ValueError("Blocked address")

client = httpx.AsyncClient(follow_redirects=False, timeout=5)
```

Checking the hostname and then fetching it leaves a DNS rebinding gap in both languages. The strong fix is an egress proxy that enforces the rules, or connecting to the IP you checked. `ipaddress` makes the range checks easy. Disable redirects, or check every hop.

## 339: How do you prevent path traversal?

**Node.js**

```js
const full = path.resolve(UPLOAD_DIR, req.params.name);
if (!full.startsWith(UPLOAD_DIR + path.sep)) return res.sendStatus(400);
```

**Python**

```python
from pathlib import Path

UPLOAD_DIR = Path("/srv/uploads").resolve()

def safe_path(name: str) -> Path:
    full = (UPLOAD_DIR / name).resolve()
    if not full.is_relative_to(UPLOAD_DIR):
        raise HTTPException(400, "Invalid path")
    return full
```

`Path.is_relative_to` compares path parts, so it avoids the `/srv/uploads-evil` prefix bug that plain string checks have. Also note that `Path("/a") / "/etc/passwd"` gives `/etc/passwd`, because an absolute right side replaces the left.

## 340: What dangerous dynamic execution features exist in each?

**Node.js**

```js
eval(code);
new Function("a", code);
vm.runInNewContext(code); // not a security sandbox
```

**Python**

```python
eval(expr); exec(code)                # run arbitrary code
pickle.loads(data)                    # runs code while loading
yaml.load(text, Loader=yaml.Loader)   # can build arbitrary objects

import ast
ast.literal_eval("[1, 2, {'a': 3}]")  # safe: literals only
yaml.safe_load(text)
```

Python has no safe in-process sandbox. Never unpickle data from users, cookies or shared caches. Celery and some caches can use pickle, so configure them for JSON.

## 341: How do timing-safe comparisons translate?

**Node.js**

```js
import { timingSafeEqual } from "node:crypto";

const ok =
  a.length === b.length && timingSafeEqual(Buffer.from(a), Buffer.from(b));
```

**Python**

```python
import hmac
import secrets

hmac.compare_digest(expected_sig, received_sig)
secrets.compare_digest(a, b)   # same function
```

`compare_digest` accepts strings or bytes and handles different lengths for you, so the length check from the Node code is not needed. Use it for API keys, webhook signatures and tokens.

## 342: How does regex denial of service (ReDoS) compare?

Both V8's `RegExp` and Python's `re` are backtracking engines, so patterns like `(a+)+$` can take exponential time on bad input. In Node.js that blocks the whole server. In a Python sync server it ties up one worker thread, and in an async server it blocks the loop.

**Node.js**

```js
/^(a+)+$/.test("a".repeat(30) + "!"); // hangs
```

**Python**

```python
import re

re.match(r"^(a+)+$", "a" * 30 + "!")    # hangs too
re.match(r"^(?>a+)+$", "a" * 30 + "!")  # atomic group (3.11+) prevents backtracking
re.match(r"^a++$", "a" * 30 + "!")      # possessive quantifier (3.11+)

# uv add google-re2: linear-time engine with an re-like API
import re2
```

Limit input length before matching, avoid nested quantifiers, and use RE2 for user-supplied patterns. Python's `re` has no timeout option.

## 343: How does dependency security scanning translate?

**Node.js**

```bash
npm audit
npm ci --ignore-scripts
```

**Python**

```bash
uvx pip-audit
uv export --format requirements.txt --no-hashes | uvx pip-audit -r /dev/stdin
uv lock --upgrade-package urllib3     # bump one vulnerable dependency
```

npm `postinstall` scripts run at install time. In Python, installing a wheel runs no code, but building from a source distribution runs its build backend. Prefer wheels-only installs (`uv pip install --only-binary :all:` or uv's `no-build` setting) in CI for untrusted packages. `uv.lock` stores hashes, so tampered files fail to install.

## 344: Is there a Python equivalent of Node's permission model?

Node.js has a permission model (`--permission` with `--allow-fs-read`, `--allow-net` and similar flags) that limits what a process can do. Python has nothing like it built in. Audit hooks (`sys.addaudithook`) can log or block sensitive events, but they are not a security boundary.

**Node.js**

```bash
node --permission --allow-fs-read=/app server.js
```

**Python**

```python
import sys

def audit(event: str, args: tuple) -> None:
    if event == "subprocess.Popen":
        raise RuntimeError("subprocess blocked")

sys.addaudithook(audit)
```

For real isolation in Python, use the OS and container layer: a non-root user, a read-only filesystem, seccomp profiles, dropped capabilities and network policies.

## 345: How does CSRF protection differ between Express and Django?

Express has no CSRF protection by default (and `csurf` is deprecated), so many apps rely on `SameSite` cookies, tokens in headers, or packages like `csrf-csrf`. Django turns on CSRF middleware by default for all unsafe methods on cookie-authenticated requests.

**Node.js**

```js
res.cookie("session", id, { sameSite: "lax", httpOnly: true, secure: true });
```

**Python**

```python
# Django: on by default
MIDDLEWARE = ["django.middleware.csrf.CsrfViewMiddleware", ...]
CSRF_TRUSTED_ORIGINS = ["https://app.example.com"]
```

FastAPI has no CSRF protection either. If you move a cookie-session SPA backend from Express to Django, the frontend must start sending the `X-CSRFToken` header, or every POST returns 403. APIs that use `Authorization: Bearer` headers are not exposed to CSRF.

## 346: How does Passport.js translate for OAuth and OIDC?

**Node.js**

```js
passport.use(
  new GoogleStrategy({ clientID, clientSecret, callbackURL }, verify),
);
app.get(
  "/auth/google",
  passport.authenticate("google", { scope: ["profile", "email"] }),
);
```

**Python**

```python
# uv add authlib itsdangerous
from authlib.integrations.starlette_client import OAuth

oauth = OAuth()
oauth.register(
    "google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=settings.google_id,
    client_secret=settings.google_secret,
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/auth/google")
async def login(request: Request):
    return await oauth.google.authorize_redirect(request, request.url_for("auth_callback"))

@app.get("/auth/callback", name="auth_callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    return token["userinfo"]
```

Authlib needs `SessionMiddleware` for the state value. For Django, `django-allauth` covers what many Passport strategies do.

## 347: How do you validate untrusted input defensively at scale?

**Node.js**

```ts
const Body = z
  .object({
    name: z.string().max(200),
    tags: z.array(z.string().max(30)).max(20),
  })
  .strict();
```

**Python**

```python
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

Tag = Annotated[str, StringConstraints(max_length=30)]

class Body(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    name: str = Field(max_length=200)
    tags: list[Tag] = Field(default_factory=list, max_length=20)
```

Limit every string and list, reject unknown fields, and limit the total body size at the proxy. Pydantic's default lax mode turns `"123"` into `123`. Use `strict=True` where you need the exact types Zod enforced.

## 348: How do you secure file uploads?

**Node.js**

```js
const type = await fileTypeFromBuffer(buf); // check magic bytes, not the extension
```

**Python**

```python
import uuid
import filetype   # uv add filetype

ALLOWED = {"image/png", "image/jpeg"}

@app.post("/upload")
async def upload(file: UploadFile) -> dict:
    head = await file.read(261)
    kind = filetype.guess(head)
    if kind is None or kind.mime not in ALLOWED:
        raise HTTPException(415, "Unsupported file type")
    await file.seek(0)
    key = f"{uuid.uuid4()}.{kind.extension}"   # never trust the client filename
    ...
```

Generate your own file names, enforce size limits while streaming, store uploads outside the web root or in object storage, and re-encode images with Pillow to strip dangerous content.

## 349: How do you handle TLS client settings safely?

**Node.js**

```js
// never in production:
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
const agent = new https.Agent({ ca: fs.readFileSync("internal-ca.pem") });
```

**Python**

```python
import ssl

ctx = ssl.create_default_context(cafile="internal-ca.pem")
client = httpx.AsyncClient(verify=ctx)

httpx.AsyncClient(verify=False)   # never in production
```

Python reads trusted roots from `certifi` or the OS store, depending on the library. If internal certificates work in Node but fail in Python, add the CA to the context explicitly, or use `truststore` to use the OS certificate store, instead of turning verification off.

## 350: How do you implement a distributed rate limiter?

**Node.js**

```js
const limiter = new RateLimiterRedis({
  storeClient: redis,
  points: 100,
  duration: 60,
});
await limiter.consume(ip);
```

**Python**

```python
SCRIPT = """
local current = redis.call('INCR', KEYS[1])
if current == 1 then redis.call('EXPIRE', KEYS[1], ARGV[1]) end
return current
"""
incr = r.register_script(SCRIPT)

async def allow(key: str, limit: int = 100, window: int = 60) -> bool:
    bucket = f"rl:{key}:{int(time.time()) // window}"
    return await incr(keys=[bucket], args=[window]) <= limit
```

A Lua script makes increment and expire atomic. This fixed-window version allows bursts at the window edges. Use a sliding window or token bucket for smoother limits, or the `limits` library, which `slowapi` uses.

## 351: What TypeScript type features have no Python equivalent?

TypeScript's type system can compute types. Python's mostly cannot. Missing or weaker in Python:

- Mapped types (`{ [K in keyof T]: ... }`), so there is no `Partial<T>` or `Pick<T, K>`.
- Conditional types (`T extends U ? X : Y`) and `infer`.
- Template literal types (`` `user:${string}` ``).
- `keyof` and indexed access types (`T["id"]`).
- `satisfies`.

**Node.js**

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

**Python**

```python
# no equivalent: write the class out, or generate code,
# or create the model at runtime with Pydantic
from pydantic import create_model

UserPatch = create_model("UserPatch", **{name: (f.annotation | None, None)
                                         for name, f in User.model_fields.items()})
```

Runtime-built models work for validation, but type checkers can't see their fields. When translating heavily typed TypeScript, accept some duplication in exchange for simple, readable types.

## 352: How do branded types translate?

**Node.js**

```ts
type UserId = string & { readonly __brand: "UserId" };
type OrderId = string & { readonly __brand: "OrderId" };
function getUser(id: UserId) {}
```

**Python**

```python
from typing import NewType

UserId = NewType("UserId", str)
OrderId = NewType("OrderId", str)

def get_user(user_id: UserId) -> None: ...

get_user(UserId("u_1"))     # ok
get_user(OrderId("o_1"))    # type error
```

`NewType` is free at runtime (it returns the value unchanged) and is checked only statically, the same trade-off as TypeScript brands.

## 353: How do variance and generic protocols compare?

TypeScript checks variance structurally and mostly infers it. Python's checkers also infer variance with the 3.12 syntax, and older code declares it on `TypeVar`. The classic trap is the same in both: `list[Dog]` is not a `list[Animal]`, because lists are mutable.

**Node.js**

```ts
function feed(animals: readonly Animal[]) {}
feed(dogs); // readonly arrays are covariant
```

**Python**

```python
from collections.abc import Sequence

def feed(animals: Sequence[Animal]) -> None: ...   # read-only, covariant
feed(dogs)          # ok
def add(animals: list[Animal]) -> None: ...
add(dogs)           # error: list is invariant

class Reader[T](Protocol):    # variance inferred from usage (3.12+)
    def read(self) -> T: ...
```

Accept `Sequence`, `Mapping` and `Iterable` in parameters, and return concrete `list` or `dict`. That is the Python version of preferring `readonly` arrays in signatures.

## 354: How do you type decorators that keep the wrapped signature?

**Node.js**

```ts
function logged<A extends unknown[], R>(fn: (...a: A) => R): (...a: A) => R {
  return (...a) => {
    console.log(fn.name);
    return fn(...a);
  };
}
```

**Python**

```python
from collections.abc import Awaitable, Callable
import functools

def logged[**P, R](fn: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    @functools.wraps(fn)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(fn.__name__)
        return await fn(*args, **kwargs)
    return wrapper
```

`**P` is a `ParamSpec`, which captures the full parameter list including keyword arguments, like `A extends unknown[]` but richer. Without it, decorated functions lose their types and become `Callable[..., Any]`.

## 355: How do you validate data against a type that is not a model?

**Node.js**

```ts
const Ids = z.array(z.number().int().positive());
const ids = Ids.parse(JSON.parse(raw));
```

**Python**

```python
from typing import Annotated
from pydantic import Field, TypeAdapter

Ids = TypeAdapter(list[Annotated[int, Field(gt=0)]])
ids = Ids.validate_json(raw)          # parse and validate in one pass, in Rust
Ids.json_schema()
```

`TypeAdapter` validates any type, such as lists, unions, `TypedDict`s and dataclasses, without wrapping it in a `BaseModel`. Build adapters once at module level, since building them is slow.

## 356: How do you share types between a TypeScript frontend and a Python backend?

Before, frontend and backend could import the same TypeScript types. After the move, the OpenAPI schema becomes the shared contract.

**Node.js**

```ts
// frontend
import type { User } from "@acme/api-types";
```

**Python**

```bash
# backend publishes the schema
python -c "import json; from app.main import app; print(json.dumps(app.openapi()))" > openapi.json

# frontend generates types and a client from it
npx openapi-typescript openapi.json -o src/api/schema.d.ts
npx @hey-api/openapi-ts -i openapi.json -o src/client
```

Run the generation in CI and fail the build when the generated files change without a commit. That catches backend changes that would break the frontend. Give models clear names, because those names become the TypeScript type names.

## 357: How do you prove the Python service matches the Node.js contract?

Use contract tests that run the same HTTP checks against both services:

1. Record real requests and responses from the Node service (from logs, a proxy, or existing e2e tests).
2. Replay them against the Python service and compare status codes, headers and JSON bodies.
3. Ignore fields that are expected to differ (timestamps, generated IDs) and fail on everything else.

**Node.js**

```js
// existing e2e test, written against HTTP, not the framework
const res = await fetch(`${BASE_URL}/api/orders/42`);
expect(await res.json()).toMatchObject({ id: 42, status: "paid" });
```

**Python**

```python
@pytest.mark.parametrize("base_url", [NODE_URL, PY_URL])
def test_order_contract(base_url: str) -> None:
    res = httpx.get(f"{base_url}/api/orders/42")
    assert res.status_code == 200
    assert res.json() == snapshot_without(["updatedAt"])
```

Tools like Schemathesis generate many requests from the OpenAPI schema and catch edge cases, such as wrong 422s or 500s, that handwritten tests miss.

## 358: What JSON output differences break clients after a translation?

| Topic         | Node.js (Express)            | Python (FastAPI/Pydantic)                                                                |
| ------------- | ---------------------------- | ---------------------------------------------------------------------------------------- |
| Field names   | `camelCase`                  | `snake_case` unless aliased                                                              |
| Missing value | `undefined` keys are dropped | `None` becomes `null`                                                                    |
| Dates         | `2026-11-24T10:00:00.000Z`   | `2026-11-24T10:00:00Z`, or microseconds and `+00:00` with `json.dumps` and `isoformat()` |
| Decimals      | number                       | string (Pydantic default)                                                                |
| Floats        | `1` for `1.0`                | `1.0`                                                                                    |
| Errors        | your own shape               | `{"detail": ...}`                                                                        |
| Validation    | usually 400                  | 422                                                                                      |

**Node.js**

```js
res.json({ id: 1, nickname: undefined, price: 10.0 }); // {"id":1,"price":10}
```

**Python**

```python
class Out(BaseModel):
    id: int
    nickname: str | None = None
    price: float

Out(id=1, price=10.0).model_dump_json(exclude_none=True)   # {"id":1,"price":10.0}
```

Most clients don't care about `10` vs `10.0`, but strict schema validators and snapshot tests do. Check each row of this table against your client code.

## 359: How do you keep camelCase JSON with snake_case Python code?

**Node.js**

```js
res.json({ userId: 1, createdAt: new Date() });
```

**Python**

```python
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

class UserOut(ApiModel):
    user_id: int
    created_at: datetime

# FastAPI serializes response models by alias by default: {"userId": 1, "createdAt": "..."}
UserOut(user_id=1, created_at=now).model_dump(by_alias=True)
```

Put the config on a shared base class so every model gets it. `populate_by_name=True` lets Python code use snake_case names while JSON input in camelCase still works. Pydantic 2.11+ splits this into `validate_by_name` and `validate_by_alias`.

## 360: How do you reproduce Express's dropping of undefined fields?

**Node.js**

```js
res.json({ id: 1, email: user.email }); // email omitted if undefined
```

**Python**

```python
@app.get("/users/{user_id}", response_model=UserOut, response_model_exclude_none=True)
async def get_user(user_id: int): ...

@app.patch("/users/{user_id}", response_model=UserOut, response_model_exclude_unset=True)
async def patch_user(user_id: int, data: UserPatch): ...
```

Choose deliberately. `exclude_none` drops every `null`, which also hides fields that are null on purpose. If the Node code sometimes sent `null` and sometimes left fields out, model the difference explicitly, or clients that check `"field" in obj` will break.

## 361: How do you keep the old error response format?

**Node.js**

```js
// Node API returned 400 with:
{ "error": "ValidationError", "details": [{ "path": "email", "message": "Invalid email" }] }
```

**Python**

```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
    details = [
        {"path": ".".join(str(p) for p in err["loc"][1:]), "message": err["msg"]}
        for err in exc.errors()
    ]
    return JSONResponse({"error": "ValidationError", "details": details}, status_code=400)
```

FastAPI returns 422 with its own format by default. Override the handler so status codes and shapes match the old API. Pydantic's messages differ from Zod's, so map the common error types to the old messages if clients show them to users.

## 362: What breaks with large integers between Python and JavaScript clients?

Python ints have no limit, but JavaScript numbers lose precision above `2**53 - 1`. A Python service that returns 64-bit IDs (Snowflake IDs, Postgres `BIGINT` sequences after many rows) as JSON numbers silently corrupts them in browsers.

**Node.js**

```js
JSON.parse('{"id": 9007199254740993}').id; // 9007199254740992
```

**Python**

```python
from typing import Annotated
from pydantic import PlainSerializer

BigId = Annotated[int, PlainSerializer(lambda v: str(v), return_type=str, when_used="json")]

class Out(BaseModel):
    id: BigId     # {"id": "9007199254740993"}
```

The Node service could never produce such a number by accident, so the bug is new to the translation. Check every `BIGINT` column the API exposes.

## 363: What string handling differences can change behavior?

- Length: UTF-16 units vs code points (see emoji).
- Case: `"ß".toUpperCase()` is `"SS"` in both, but `casefold()` has no direct JavaScript match. `toLowerCase()` and `lower()` can differ for rare characters.
- Slicing: `s.slice(0, 10)` can cut an emoji in half in JavaScript, but not in Python.
- `trim()` and `strip()` treat some Unicode whitespace differently.
- `localeCompare` sorts by locale, while Python's `<` compares code points.

**Node.js**

```js
"👍🏽ok".slice(0, 2); // "👍" plus half the skin tone, or a broken surrogate
```

**Python**

```python
"👍🏽ok"[:2]   # "👍🏽", two code points: emoji plus modifier
```

Write property tests with Unicode input (Hypothesis generates it) for any field that is truncated, validated by length, or used as a key.

## 364: What datetime pitfalls appear when moving from JavaScript Date?

A JavaScript `Date` is always a UTC instant. Python `datetime` objects can be naive (no time zone) or aware. Mixing them raises `TypeError` when comparing, and naive values are read in the server's local time.

**Node.js**

```js
new Date("2026-11-24T10:00:00"); // parsed as local time
new Date("2026-11-24"); // parsed as UTC!
```

**Python**

```python
from datetime import datetime, UTC

datetime.fromisoformat("2026-11-24T10:00:00")             # naive
datetime.fromisoformat("2026-11-24T10:00:00+00:00")       # aware
datetime.now() < datetime.now(UTC)                        # TypeError

# SQLAlchemy: keep the time zone
created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
```

Use aware UTC datetimes everywhere, `timestamptz` columns, and Pydantic's `AwareDatetime` on inputs. `datetime.utcnow()` is deprecated because it returns a naive value that looks like UTC.

## 365: What regex syntax differences matter when porting patterns?

| Feature                  | JavaScript     | Python `re`                            |
| ------------------------ | -------------- | -------------------------------------- |
| Named group              | `(?<name>...)` | `(?P<name>...)`                        |
| Named backreference      | `\k<name>`     | `(?P=name)`                            |
| Global replace           | `/g` flag      | `re.sub` replaces all                  |
| Sticky `/y`              | yes            | `pattern.match(s, pos)`                |
| Unicode property `\p{L}` | with `/u`      | not supported (use `regex` package)    |
| `\d`                     | ASCII digits   | any Unicode digit unless `re.ASCII`    |
| `$`                      | end of input   | end, or before a final `\n` (use `\Z`) |

**Node.js**

```js
/^\d+$/.test("123\n"); // false
```

**Python**

```python
re.match(r"^\d+$", "123\n")         # matches! $ allows a trailing newline
re.fullmatch(r"\d+", "123\n")       # None
re.fullmatch(r"\d+", "١٢٣")         # matches Arabic-Indic digits
re.fullmatch(r"\d+", "١٢٣", re.ASCII)  # None
```

The `$` and `\d` differences are real validation bugs. Use `fullmatch` and `re.ASCII` for input validation patterns.

## 366: How do you keep rounding results identical?

**Node.js**

```js
Math.round(2.5); // 3
Math.round(-2.5); // -2
Number((1.005).toFixed(2)); // 1 (float error)
```

**Python**

```python
from decimal import Decimal, ROUND_HALF_UP
import math

round(2.5)      # 2 (half to even)

def js_round(x: float) -> int:
    return math.floor(x + 0.5)     # Math.round semantics

Decimal("1.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)   # 1.01
```

If totals, discounts or tax amounts are rounded, write tests with `.5` cases and negative numbers, and decide whether to copy JavaScript's rounding or fix it with `Decimal`. A silent change in rounding is a finance bug.

## 367: How do you port comparator-based sorting safely?

**Node.js**

```js
items.sort((a, b) => {
  if (a.pinned !== b.pinned) return a.pinned ? -1 : 1;
  return b.score - a.score || a.name.localeCompare(b.name);
});
```

**Python**

```python
items.sort(key=lambda i: (not i.pinned, -i.score, i.name))

# when a key is hard to express
from functools import cmp_to_key
items.sort(key=cmp_to_key(compare))
```

Translate comparators into key tuples where you can, as they are faster and easier to read. Both sorts are stable. A JavaScript comparator that returns `true` or `false` instead of a number is a bug in the original, so don't copy it.

## 368: How do bitwise operations differ?

**Node.js**

```js
0xffffffff | 0; // -1 (32-bit signed)
1 << 31; // -2147483648
(-1 >>> 0).toString(16); // "ffffffff"
```

**Python**

```python
0xFFFFFFFF | 0          # 4294967295
1 << 31                 # 2147483648
(-1) & 0xFFFFFFFF       # 4294967295, emulate >>> 0

def to_int32(x: int) -> int:
    x &= 0xFFFFFFFF
    return x - (1 << 32) if x & 0x80000000 else x
```

JavaScript bitwise operators convert to 32-bit integers, and Python's work on unlimited ints. Hash functions, checksums and ID encoders ported from JavaScript need explicit masking, or they produce different values.

## 369: How do you route traffic during a strangler migration?

Put a router in front that sends each route group to the right service, and move groups one by one. Start with read-only, low-risk endpoints.

**Node.js**

```js
// Option: keep Node as the edge and proxy moved routes
import { createProxyMiddleware } from "http-proxy-middleware";
app.use(
  "/api/reports",
  createProxyMiddleware({ target: "http://py-api:8000", changeOrigin: true }),
);
```

**Python**

```yaml
# Option: route at the gateway (Kubernetes Gateway API)
rules:
  - matches: [{ path: { type: PathPrefix, value: /api/reports } }]
    backendRefs: [{ name: py-api, port: 8000 }]
  - backendRefs: [{ name: node-api, port: 3000 }]
```

Routing at the gateway is cleaner than proxying through Node, because the Node service doesn't need to stay healthy for Python routes to work. Use weighted routes (for example 5% to Python) for gradual rollout.

## 370: What problems come from running both services on one database?

- Both must agree on schema, enums, defaults and time zones.
- ORM-level behavior (Prisma's `@updatedAt`, `@default(cuid())`, soft-delete middleware) is invisible in the database, so the Python side must copy it or the data drifts.
- Connection limits now cover two services.
- Caches in one service become stale when the other writes.

**Node.js**

```prisma
updatedAt DateTime @updatedAt     // set by Prisma, not by Postgres
id        String   @default(cuid())
```

**Python**

```python
updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
id: Mapped[str] = mapped_column(default=lambda: generate_cuid())
```

Move such logic into the database (triggers, defaults) where possible, so both services behave the same automatically.

## 371: What is shadow traffic and how do you use it to verify a translation?

Shadow traffic means sending a copy of real production requests to the new service, ignoring its responses for users, and comparing them with the old service's responses. It finds differences that tests miss, because it uses real data and real edge cases.

**Node.js**

```js
// old service stays the source of truth
```

**Python**

```nginx
location /api/ {
  mirror /mirror;
  proxy_pass http://node_api;
}
location = /mirror {
  internal;
  proxy_pass http://py_api$request_uri;
}
```

Only mirror safe reads (GET), or point the shadow at a copy of the database, because mirrored writes would happen twice. Diff the responses in a separate job (GitHub's Scientist library pattern) and fix differences until the rate is near zero.

## 372: How do you use feature flags during a language migration?

**Node.js**

```js
if (await flags.isEnabled("orders-python", { userId }))
  return proxyToPython(req, res);
```

**Python**

```python
# the Python side reads the same flag provider for its own toggles
from openfeature import api

client = api.get_client()
if client.get_boolean_value("orders-v2-pricing", False, ctx):
    ...
```

Flags let you move users or tenants one at a time and roll back in seconds without deploying. Use one flag provider for both services (LaunchDarkly, Unleash, Flagsmith or OpenFeature with a backend), so both see the same targeting.

## 373: Why should you port tests before code?

Tests that call the service over HTTP describe behavior, not implementation, so they work against both services without changes. Porting them first gives you a safety net and a progress meter: the translation is done when the Python service passes the same suite.

**Node.js**

```js
// unit tests that mock Prisma are tied to Node and must be rewritten
vi.mock("@prisma/client");
```

**Python**

```python
# black-box tests run unchanged against either service
BASE_URL = os.environ["API_URL"]

def test_create_order_returns_201() -> None:
    res = httpx.post(f"{BASE_URL}/api/orders", json=ORDER)
    assert res.status_code == 201
```

Write characterization tests for odd behaviors (strange status codes, rounding, sorting) before porting, so you change them on purpose instead of by accident.

## 374: How do you generate SQLAlchemy models from an existing Prisma database?

**Node.js**

```bash
npx prisma db pull   # the database is the truth
```

**Python**

```bash
uvx sqlacodegen postgresql://user:pass@localhost/app > app/models.py
python manage.py inspectdb > app/models.py   # Django
```

Generated models are a starting point. Fix the details: Prisma's quoted PascalCase table names (`"User"`), enum types, `@updatedAt` behavior, implicit many-to-many tables (`_CategoryToPost` with `A` and `B` columns), and relation names. Then use Alembic's autogenerate to check that your models match the live schema exactly.

## 375: How do you share sessions and auth between Node.js and Python during migration?

Signed cookies from `express-session` or `cookie-signature` use a format Python libraries don't read. The easiest shared auth is a JWT signed with the same key, or a server-side session store (Redis) that both services read.

**Node.js**

```js
// express-session cookie: "s:" + id + "." + HMAC-SHA256(base64, no padding)
```

**Python**

```python
import base64
import hashlib
import hmac

def unsign_express(cookie: str, secret: str) -> str | None:
    if not cookie.startswith("s:"):
        return None
    value, _, sig = cookie[2:].rpartition(".")
    expected = base64.b64encode(
        hmac.new(secret.encode(), value.encode(), hashlib.sha256).digest()
    ).decode().rstrip("=")
    return value if hmac.compare_digest(sig, expected) else None

session = json.loads(await r.get(f"sess:{unsign_express(cookie, SECRET)}") or "null")
```

Note that the cookie value is URL-encoded (`s%3A...`), so decode it first. Once both sides share the session, you can move routes without logging users out.

## 376: Will existing password hashes keep working in Python?

Yes, if you use the same algorithm. bcrypt hashes from Node's `bcrypt` or `bcryptjs` use the `$2a$` or `$2b$` prefix, and Python's `bcrypt` verifies both. Argon2 hashes use the standard PHC string format (`$argon2id$v=19$m=...`), which `argon2-cffi` reads.

**Node.js**

```js
const hash = await bcrypt.hash(password, 12); // "$2b$12$..."
```

**Python**

```python
import bcrypt

bcrypt.checkpw(password.encode(), hash_from_node.encode())   # True
```

Watch two details: bcrypt only uses the first 72 bytes, and newer versions of Python's `bcrypt` raise an error for longer passwords instead of silently cutting them, and `scrypt` or `pbkdf2` hashes built by hand in Node must be parsed with the same parameters, salt encoding and key length. Add tests with real hashes from the old system.

## 377: How do you migrate background jobs that are already in the queue?

BullMQ stores jobs in Redis in its own format, and Celery can't read them. Running both workers side by side is the safe path:

1. Stop enqueueing new BullMQ jobs and enqueue Celery tasks instead.
2. Keep the Node workers running until the BullMQ queue (including delayed and retrying jobs) is empty.
3. Then shut the Node workers down.

**Node.js**

```js
const counts = await queue.getJobCounts(
  "waiting",
  "delayed",
  "active",
  "failed",
);
```

**Python**

```python
# make the new task safe to run if a job is processed by both systems
@app.task(bind=True, acks_late=True)
def send_invoice(self, invoice_id: int) -> None:
    if Invoice.objects.filter(id=invoice_id, sent=True).exists():
        return
    ...
```

Delayed jobs can sit for days, so check for them before declaring the queue empty. Make every task idempotent, because the overlap window can process a job twice.

## 378: What are the risks of using AI or automatic tools to translate the code?

Automatic translation writes Python that looks right but carries over JavaScript habits and changes behavior in subtle ways:

- `||` becomes `or`, but `0` and `""` behave the same while `[]` and `{}` do not.
- `Math.round` becomes `round`, which changes rounding.
- `%` on negative numbers, `$` in regexes, string lengths and date parsing differ.
- Async code is translated with blocking libraries inside `async def`.
- Mutable default arguments slip in.

**Node.js**

```js
const limit = req.query.limit || 20;
```

**Python**

```python
limit = request.query_params.get("limit") or 20   # looks the same, still a string!
limit: int = Query(20)                            # idiomatic and typed
```

Use tools for the first draft, then review with this checklist, run strict type checking and Ruff, and rely on contract tests and shadow traffic to prove behavior.

## 379: When is Python slower or faster than Node.js for a backend?

V8's JIT makes pure JavaScript logic several times faster than CPython for loops and object handling. CPython 3.13+ has an experimental JIT, but it doesn't close that gap yet. For I/O-bound APIs, both spend most time waiting on databases and networks, so latency is often similar and the difference shows up as needing more Python processes.

Python is faster when the work runs in native code: NumPy, pandas, Polars, Pydantic's Rust core, orjson, image processing and machine learning libraries.

**Node.js**

```js
let sum = 0;
for (let i = 0; i < 1e8; i++) sum += i; // fast in V8
```

**Python**

```python
import numpy as np

total = np.arange(100_000_000, dtype=np.int64).sum()   # fast: runs in C
total = sum(range(100_000_000))                        # much slower in pure Python
```

Measure your real endpoints instead of guessing, and plan capacity for more instances if the service does a lot of pure-Python work.

## 380: How do you prevent cache stampedes in async Python?

**Node.js**

```js
const inflight = new Map();
function getOnce(key, load) {
  if (!inflight.has(key))
    inflight.set(
      key,
      load().finally(() => inflight.delete(key)),
    );
  return inflight.get(key);
}
```

**Python**

```python
_inflight: dict[str, asyncio.Future] = {}

async def get_once(key: str, load) -> object:
    if (cached := await cache.get(key)) is not None:
        return cached
    if key in _inflight:
        return await asyncio.shield(_inflight[key])
    fut = asyncio.ensure_future(load())
    _inflight[key] = fut
    try:
        value = await asyncio.shield(fut)
        await cache.set(key, value, ex=60)
        return value
    finally:
        _inflight.pop(key, None)
```

This removes duplicate loads within one process. `shield` keeps one cancelled waiter from cancelling the shared load for everyone. Across processes, add a Redis lock or serve stale data while one worker refreshes.

## 381: Which async ORM should you pick when moving off Prisma?

| Option                   | Fits when                                                   |
| ------------------------ | ----------------------------------------------------------- |
| SQLAlchemy 2.0 (async)   | FastAPI services, complex queries, you want full control    |
| SQLModel                 | Small FastAPI apps that want one class for ORM and Pydantic |
| Django ORM               | You chose Django, and accept some async limits              |
| Tortoise ORM             | You want a Django-like API that is async from the start     |
| No ORM (asyncpg/psycopg) | The Node app used raw SQL with `pg`                         |

**Node.js**

```ts
await prisma.user.findMany({ where: { active: true } });
```

**Python**

```python
# SQLModel: one class is both the table and the schema
from sqlmodel import Field, SQLModel, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    active: bool = True

users = (await session.exec(select(User).where(User.active))).all()
```

SQLAlchemy is the safe default: it has the largest ecosystem, and Alembic is built for it. Keep separate Pydantic models for API input and output even with SQLModel, so database columns don't leak into the API.

## 382: What are the limits of async in Django?

Django supports `async def` views and async ORM methods (`aget`, `acreate`, `async for`), but the ORM still runs queries through a thread under the hood. Async transactions are not supported yet, so `transaction.atomic()` needs sync code. Mixing sync and async needs adapters.

**Node.js**

```js
// everything is async, nothing to adapt
```

**Python**

```python
from asgiref.sync import sync_to_async
from django.db import transaction

@sync_to_async
def transfer(a_id: int, b_id: int, amount: int) -> None:
    with transaction.atomic():
        ...

async def view(request):
    await transfer(1, 2, 100)
    return JsonResponse({"ok": True})
```

Calling sync ORM code directly from an async view raises `SynchronousOnlyOperation`. Many Django teams keep views sync and run under Gunicorn with threads, and use ASGI only for WebSockets (Channels) or streaming. It is a valid choice, not a failure.

## 383: How do you configure Gunicorn and Uvicorn for production?

**Node.js**

```js
server.keepAliveTimeout = 65_000; // longer than the load balancer idle timeout
server.headersTimeout = 66_000;
```

**Python**

```python
# gunicorn.conf.py
import os

bind = "0.0.0.0:8000"
workers = int(os.environ.get("WEB_CONCURRENCY", 4))
worker_class = "uvicorn_worker.UvicornWorker"   # ASGI apps
timeout = 30                 # kill a worker stuck longer than this
graceful_timeout = 25        # time to finish requests on shutdown
keepalive = 75               # longer than the load balancer idle timeout
max_requests = 5000
max_requests_jitter = 500
preload_app = False
```

The keep-alive rule is the same as in Node.js: the server's idle timeout must be longer than the load balancer's, or you get random 502s. `uvicorn.workers.UvicornWorker` moved to the separate `uvicorn-worker` package. Standalone `uvicorn --workers` also works and restarts dead workers.

## 384: How do Kubernetes probes and graceful shutdown work for a Python service?

**Node.js**

```js
process.on("SIGTERM", () => {
  isShuttingDown = true; // fail readiness, then close the server after a delay
  setTimeout(() => server.close(), 10_000);
});
```

**Python**

```yaml
spec:
  terminationGracePeriodSeconds: 40
  containers:
    - name: api
      command:
        [
          "uvicorn",
          "app.main:app",
          "--host",
          "0.0.0.0",
          "--timeout-graceful-shutdown",
          "25",
        ]
      lifecycle:
        preStop:
          exec: { command: ["sleep", "10"] } # let endpoints update before SIGTERM
      readinessProbe: { httpGet: { path: /readyz, port: 8000 } }
      livenessProbe: { httpGet: { path: /healthz, port: 8000 } }
```

A `preStop` sleep gives the load balancer time to stop sending traffic, the same reason Node apps delay `server.close()`. Make sure `terminationGracePeriodSeconds` is longer than the sleep plus the server's graceful timeout. Run the server as PID 1 with the exec form of `CMD`, so it receives the signal.

## 385: Why prefer slim images over Alpine for Python?

Alpine uses musl libc. Many Python packages ship prebuilt wheels for glibc (`manylinux`), and musl wheels (`musllinux`) are less common. On Alpine, missing wheels mean compiling from source, which needs compilers, makes builds slow, and creates bigger images. Node.js on Alpine works well because most npm packages are pure JavaScript.

**Node.js**

```dockerfile
FROM node:24-alpine
```

**Python**

```dockerfile
FROM python:3.14-slim
# or distroless / chainguard images for a smaller attack surface
```

musl can also be slower for some Python workloads because of its memory allocator. Choose `-slim` unless you have measured a real gain from Alpine.

## 386: How do native addons compare?

**Node.js**

```bash
# node-gyp compiles C++ addons at install time, or prebuild ships binaries
npm install sharp   # downloads a prebuilt binary for your platform
```

**Python**

```bash
pip install pillow   # downloads a prebuilt wheel: pillow-...-cp314-manylinux_2_28_x86_64.whl
```

Python wheels are tagged by Python version, ABI and platform, so the installer picks the right binary. Build images with the same OS and architecture you deploy to (for example ARM64 Macs vs AMD64 servers), or wheels won't match. The free-threaded build needs its own wheels (`cp314t`).

## 387: How does writing extensions in Rust compare?

**Node.js**

```rust
// napi-rs
#[napi]
pub fn fib(n: u32) -> u32 { if n < 2 { n } else { fib(n - 1) + fib(n - 2) } }
```

**Python**

```rust
// PyO3 + maturin
use pyo3::prelude::*;

#[pyfunction]
fn fib(n: u32) -> u32 { if n < 2 { n } else { fib(n - 1) + fib(n - 2) } }

#[pymodule]
fn fastmath(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)
}
```

```bash
uvx maturin develop   # build and install into the current venv
```

PyO3 is how Pydantic, Ruff, uv and Polars are built. If the Node app had a napi-rs module, the Rust core can often be reused with a new PyO3 binding layer.

## 388: How do you call the old Node.js service from Python during migration?

Treat the Node service as just another HTTP dependency, with a typed client, timeouts, retries and a circuit breaker. Don't embed Node in the Python process.

**Node.js**

```js
// still serving /internal/pricing
app.post("/internal/pricing", pricingHandler);
```

**Python**

```python
class PricingClient:
    def __init__(self, http: httpx.AsyncClient) -> None:
        self._http = http

    async def quote(self, req: QuoteIn) -> QuoteOut:
        res = await self._http.post("/internal/pricing", json=req.model_dump(by_alias=True), timeout=2)
        res.raise_for_status()
        return QuoteOut.model_validate(res.json())
```

Wrapping the call in a class gives you one place to swap in the Python implementation later. Validate the response, because the contract between the two services is now a network boundary.

## 389: What does pickling cost when using process pools?

`worker_threads` copies data with the structured clone algorithm, or shares it with `SharedArrayBuffer`. `ProcessPoolExecutor` pickles the function and its arguments, sends them through a pipe, and pickles the result back. Large arguments (big dicts, DataFrames) can cost more than the work itself.

**Node.js**

```js
worker.postMessage(bigArrayBuffer, [bigArrayBuffer]); // transfer, no copy
```

**Python**

```python
# bad: sends the whole dataset for each task
pool.submit(score, huge_dataset, row_id)

# better: load data once per worker with an initializer
_data = None
def init(path: str) -> None:
    global _data
    _data = load(path)

pool = ProcessPoolExecutor(max_workers=4, initializer=init, initargs=("data.parquet",))
pool.submit(score_row, row_id)
```

Lambdas and local functions cannot be pickled, so worker functions must be defined at module level. On macOS and Windows, processes start with `spawn`, so the main module must be guarded with `if __name__ == "__main__":`.

## 390: How does SharedArrayBuffer translate?

**Node.js**

```js
const shared = new SharedArrayBuffer(1024);
const view = new Int32Array(shared);
Atomics.add(view, 0, 1);
```

**Python**

```python
from multiprocessing import shared_memory
import numpy as np

shm = shared_memory.SharedMemory(create=True, size=1024)
arr = np.ndarray((256,), dtype=np.int32, buffer=shm.buf)
arr[0] += 1        # not atomic: protect with a multiprocessing.Lock
# in another process: shared_memory.SharedMemory(name=shm.name)
shm.close()
shm.unlink()
```

Python has no `Atomics` equivalent for shared memory, so use locks. Shared memory is mainly useful for large numeric arrays. For most apps, Redis or a queue is simpler.

## 391: What are subinterpreters and how do they compare to worker_threads?

Python 3.14 added `concurrent.interpreters` (PEP 734) and `InterpreterPoolExecutor`. Each subinterpreter has its own GIL and module state in the same process, which is very close to a Node.js worker thread with its own isolate. They run Python code in parallel with less overhead than processes.

**Node.js**

```js
const w = new Worker("./task.js");
```

**Python**

```python
from concurrent.futures import InterpreterPoolExecutor   # Python 3.14+

with InterpreterPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(cpu_task, inputs))
```

Data is passed by copying, like `postMessage`. Many C extensions don't support subinterpreters yet, so test your dependencies before relying on them.

## 392: How does free-threaded Python affect libraries and your code?

Without the GIL, threads run in parallel, so code that was "accidentally safe" under the GIL can race. C extensions must declare that they support free threading. Otherwise, importing them turns the GIL back on, with a warning.

**Node.js**

```js
// JS objects are never shared between threads, so this problem doesn't exist
```

**Python**

```bash
uv python install 3.14t
uv run --python 3.14t python -c "import sys; print(sys._is_gil_enabled())"
PYTHON_GIL=0 python app.py   # force it off even if an extension asks for it (risky)
```

Built-in types like `dict` and `list` stay internally consistent, but compound operations still need locks. For web services that already scale with processes, free threading matters less than for CPU-heavy work that wants shared memory.

## 393: How do you debug a stuck or slow asyncio application?

**Node.js**

```bash
node --inspect server.js   # pause and inspect the call stack
```

**Python**

```bash
PYTHONASYNCIODEBUG=1 python app.py      # logs callbacks slower than 100 ms, unawaited coroutines
python -m asyncio ps <pid>               # Python 3.14: list tasks of a running process
python -m asyncio pstree <pid>           # show the await tree
uvx py-spy dump --pid <pid>
```

```python
loop = asyncio.get_running_loop()
loop.slow_callback_duration = 0.05
for task in asyncio.all_tasks():
    task.print_stack()
```

Debug mode is too slow for production, but `slow_callback_duration` warnings in staging quickly find blocking calls inside `async def` code.

## 394: How do you monitor event loop lag in production?

**Node.js**

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay();
h.enable();
setInterval(() => metrics.gauge("loop_p99_ms", h.percentile(99) / 1e6), 10_000);
```

**Python**

```python
async def monitor_lag(interval: float = 0.5) -> None:
    loop = asyncio.get_running_loop()
    while True:
        start = loop.time()
        await asyncio.sleep(interval)
        lag = loop.time() - start - interval
        LOOP_LAG.observe(lag)   # prometheus Histogram
```

Start the monitor in the lifespan hook. A growing lag means something blocks the loop: sync I/O, heavy JSON or CPU work. Pair it with `py-spy` to find the exact code.

## 395: Why can asyncio tasks disappear, and how do you avoid it?

The event loop keeps only weak references to tasks. A task created with `asyncio.create_task(...)` and not stored anywhere can be garbage collected before it finishes, and its exception may never be logged. Node.js promises can't be collected while their I/O is pending.

**Node.js**

```js
sendAnalytics(event); // fire and forget, runs to completion
```

**Python**

```python
_background: set[asyncio.Task] = set()

def fire_and_forget(coro) -> None:
    task = asyncio.create_task(coro)
    _background.add(task)
    task.add_done_callback(_on_done)

def _on_done(task: asyncio.Task) -> None:
    _background.discard(task)
    if not task.cancelled() and (exc := task.exception()):
        log.error("background task failed", exc_info=exc)
```

Better still, avoid fire-and-forget: use a `TaskGroup` owned by the app's lifespan, FastAPI `BackgroundTasks`, or a real job queue, so shutdown waits for the work.

## 396: How do you own long-running background tasks in an ASGI app?

**Node.js**

```js
const timer = setInterval(syncPrices, 60_000);
process.on("SIGTERM", () => clearInterval(timer));
```

**Python**

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with asyncio.TaskGroup() as tg:
        stop = asyncio.Event()
        tg.create_task(sync_prices_loop(stop))
        yield
        stop.set()     # ask loops to finish; TaskGroup waits for them

async def sync_prices_loop(stop: asyncio.Event) -> None:
    while not stop.is_set():
        await sync_prices()
        try:
            await asyncio.wait_for(stop.wait(), timeout=60)
        except TimeoutError:
            pass
```

The task group ties the background loop's lifetime to the app, and the stop event lets it finish cleanly. Remember that each worker runs its own copy, so jobs that must run once belong in a scheduler or queue.

## 397: How do you call async code from sync code, and why does asyncio.run fail inside a running loop?

**Node.js**

```js
// sync code can't wait for a promise; you make the caller async
```

**Python**

```python
asyncio.run(fetch_all())   # fine in a script or a sync worker thread

async def handler():
    asyncio.run(fetch_all())   # RuntimeError: asyncio.run() cannot be called from a running event loop
    await fetch_all()          # correct

# a sync library function called from a thread while a loop runs elsewhere
future = asyncio.run_coroutine_threadsafe(fetch_all(), main_loop)
result = future.result(timeout=10)
```

Don't use `nest_asyncio` to hide this error in services. Structure the code so async calls stay async all the way up, as you would in Node.js. In Django, `async_to_sync` from `asgiref` is the supported bridge.

## 398: How do threads and asyncio work together?

**Node.js**

```js
// worker posts a message back to the main thread
parentPort.postMessage(result);
```

**Python**

```python
async def main() -> None:
    loop = asyncio.get_running_loop()
    queue: asyncio.Queue[str] = asyncio.Queue()

    def on_hardware_event(data: str) -> None:        # called from another thread
        loop.call_soon_threadsafe(queue.put_nowait, data)

    start_sensor_thread(on_hardware_event)
    while True:
        print(await queue.get())
```

asyncio objects are not thread-safe. From other threads, use `loop.call_soon_threadsafe` or `asyncio.run_coroutine_threadsafe` to hand work to the loop. Calling `queue.put_nowait` directly from a thread can corrupt the queue or leave waiters sleeping.

## 399: Why do signals and PID 1 matter in containers for both runtimes?

The first process in a container (PID 1) gets no default signal handlers from the kernel. If it doesn't handle `SIGTERM`, Docker waits for the timeout and then kills it. Shell-form commands (`CMD uvicorn ...`) run under `/bin/sh`, which doesn't pass signals on.

**Node.js**

```dockerfile
CMD ["node", "server.js"]   # exec form, Node handles SIGTERM if you add a handler
# or: docker run --init
```

**Python**

```dockerfile
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]   # exec form: Uvicorn handles SIGTERM
# wrapper scripts must use: exec uvicorn ...
```

Use the exec form or `exec` in entrypoint scripts. Add `tini` (or `--init`) if the app starts child processes that could become zombies.

## 400: How do server timeout settings map between Node.js and Uvicorn?

| Node.js `http.Server`    | Uvicorn                                          |
| ------------------------ | ------------------------------------------------ |
| `keepAliveTimeout` (5 s) | `--timeout-keep-alive` (5 s)                     |
| `headersTimeout`         | no direct option, use the proxy                  |
| `requestTimeout` (300 s) | none, use `asyncio.timeout` in code or the proxy |
| `server.close()` grace   | `--timeout-graceful-shutdown`                    |
| `maxHeaderSize` (16 KB)  | `--h11-max-incomplete-event-size`                |

**Node.js**

```js
server.requestTimeout = 30_000;
```

**Python**

```python
@app.middleware("http")
async def request_timeout(request: Request, call_next):
    try:
        async with asyncio.timeout(30):
            return await call_next(request)
    except TimeoutError:
        return JSONResponse({"error": "Request timeout"}, status_code=504)
```

Uvicorn has no overall request timeout, so slow clients and slow handlers must be limited at the proxy or in middleware. Note that the timeout middleware above does not cover streaming responses after headers are sent.

## 401: Scenario: how would you translate an Express REST API with JWT auth to FastAPI?

**Node.js**

```js
const app = express();
app.use(express.json(), cors(), helmet());
app.post("/auth/login", login);
app.use("/api", requireUser);
app.use("/api/projects", projectsRouter);
app.use(errorHandler);
app.listen(3000);
```

**Python**

```python
app = FastAPI(lifespan=lifespan, title="Projects API")
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])
app.add_middleware(SecurityHeadersMiddleware)

app.include_router(auth.router, prefix="/auth")
app.include_router(projects.router, prefix="/api/projects", dependencies=[Depends(current_user)])

app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)
```

Plan:

1. Write contract tests from the Express routes, including error shapes.
2. Port config to `pydantic-settings` and Zod schemas to Pydantic models with camelCase aliases.
3. Port the auth middleware to a `current_user` dependency that reads the same JWTs (same secret and claims).
4. Port each router, keeping status codes (400 vs 422) and JSON shapes.
5. Run both behind the gateway and move route groups one by one.

## 402: Scenario: how would you translate a NestJS module with DI, guards and interceptors?

**Node.js**

```ts
@Module({
  imports: [TypeOrmModule.forFeature([Invoice])],
  providers: [InvoicesService],
  controllers: [InvoicesController],
})
export class InvoicesModule {}

@UseGuards(JwtAuthGuard, RolesGuard)
@UseInterceptors(AuditInterceptor)
@Controller("invoices")
export class InvoicesController {
  constructor(private svc: InvoicesService) {}
  @Roles("accountant") @Post() create(@Body() dto: CreateInvoiceDto) {
    return this.svc.create(dto);
  }
}
```

**Python**

```python
# invoices/dependencies.py
def get_invoices_service(session: SessionDep, audit: AuditDep) -> InvoicesService:
    return InvoicesService(InvoiceRepository(session), audit)

InvoicesServiceDep = Annotated[InvoicesService, Depends(get_invoices_service)]

# invoices/router.py
router = APIRouter(prefix="/invoices", dependencies=[Depends(current_user)], tags=["invoices"])

@router.post("/", status_code=201, dependencies=[Depends(require_role("accountant"))])
@audited("invoice.create")
async def create(dto: CreateInvoice, svc: InvoicesServiceDep) -> InvoiceOut:
    return await svc.create(dto)
```

Modules become packages, providers become dependency factories, guards become dependencies, interceptors become decorators or middleware, and pipes become Pydantic validation. Keep the service class free of FastAPI imports so it can be tested and reused in workers.

## 403: Scenario: how would you translate a BullMQ worker with retries, concurrency and rate limits to Celery?

**Node.js**

```js
new Worker("thumbnails", processThumb, {
  connection,
  concurrency: 5,
  limiter: { max: 50, duration: 1000 },
});
await queue.add(
  "thumb",
  { imageId },
  {
    attempts: 5,
    backoff: { type: "exponential", delay: 2000 },
    removeOnComplete: true,
  },
);
```

**Python**

```python
app = Celery("media", broker=REDIS_URL, backend=None)
app.conf.update(
    task_acks_late=True,                 # re-run if the worker dies mid-task
    worker_prefetch_multiplier=1,
    task_serializer="json",
    accept_content=["json"],
)

@app.task(
    bind=True,
    autoretry_for=(TransientError,),
    max_retries=5,
    retry_backoff=2,
    retry_backoff_max=300,
    retry_jitter=True,
    rate_limit="50/s",                   # per worker
)
def make_thumbnail(self, image_id: int) -> None:
    ...
```

```bash
celery -A media worker --concurrency=5 --queues=thumbnails
```

Celery's `rate_limit` is per worker, not global like BullMQ's limiter. For a global limit, use a Redis token bucket inside the task. Keep JSON serialization so tasks stay language-neutral and safe.

## 404: Scenario: how would you translate a stream-based CSV import?

**Node.js**

```js
await pipeline(
  createReadStream(file),
  parse({ columns: true }),
  batchStream(500),
  new Writable({
    objectMode: true,
    write: async (batch, _, cb) => {
      await insertMany(batch);
      cb();
    },
  }),
);
```

**Python**

```python
import csv
from itertools import batched

def import_csv(path: str) -> int:
    count = 0
    with open(path, newline="", encoding="utf-8") as f:
        for batch in batched(csv.DictReader(f), 500):
            rows = [RowIn.model_validate(r).model_dump() for r in batch]
            with engine.begin() as conn:
                conn.execute(insert(Item), rows)   # executemany
            count += len(rows)
    return count
```

Generators replace stream stages, and `batched` replaces the batching transform. Memory stays flat because each stage pulls one item at a time. Run it in a Celery task or a thread, not in an async request handler. For very large files, Postgres `COPY` (psycopg's `cursor.copy()`) is much faster than inserts.

## 405: Scenario: how would you translate a Socket.IO chat with rooms and a Redis adapter?

**Node.js**

```js
const io = new Server(httpServer, { cors: { origin: APP_URL } });
io.adapter(createAdapter(pubClient, subClient));
io.on("connection", (socket) => {
  socket.on("join", (room) => socket.join(room));
  socket.on("message", ({ room, text }) =>
    io.to(room).emit("message", { text, from: socket.id }),
  );
});
```

**Python**

```python
import socketio

mgr = socketio.AsyncRedisManager(REDIS_URL)
sio = socketio.AsyncServer(async_mode="asgi", client_manager=mgr, cors_allowed_origins=[APP_URL])
asgi_app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)

@sio.on("join")
async def join(sid: str, room: str) -> None:
    await sio.enter_room(sid, room)

@sio.on("message")
async def message(sid: str, data: dict) -> None:
    await sio.emit("message", {"text": data["text"], "from": sid}, room=data["room"])
```

`python-socketio` speaks the Socket.IO protocol, so the browser client doesn't change. The Redis manager does what the Redis adapter did. Run it with sticky sessions if clients can fall back to long polling. Note that the Python Redis manager does not use the same channel format as the Node adapter, so Node and Python servers can't share rooms during migration.

## 406: Scenario: how would you translate a Stripe webhook handler with signature verification?

**Node.js**

```js
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const event = stripe.webhooks.constructEvent(
      req.body,
      req.get("stripe-signature"),
      WEBHOOK_SECRET,
    );
    if (event.type === "checkout.session.completed") fulfill(event.data.object);
    res.sendStatus(200);
  },
);
```

**Python**

```python
import stripe

@app.post("/webhooks/stripe")
async def stripe_webhook(request: Request) -> Response:
    payload = await request.body()          # raw bytes, before any JSON parsing
    sig = request.headers.get("stripe-signature", "")
    try:
        event = stripe.Webhook.construct_event(payload, sig, settings.stripe_webhook_secret)
    except (ValueError, stripe.SignatureVerificationError):
        raise HTTPException(400, "Invalid signature")
    if event["type"] == "checkout.session.completed":
        await enqueue_fulfillment(event["data"]["object"]["id"])
    return Response(status_code=200)
```

The key detail is the same in both: verify the raw body, not re-serialized JSON. Don't declare a Pydantic body parameter on this route. Return 200 fast and do the work in a job, and store processed event IDs so Stripe's retries don't fulfill twice.

## 407: Scenario: how would you translate direct-to-S3 uploads with presigned URLs?

**Node.js**

```js
import { createPresignedPost } from "@aws-sdk/s3-presigned-post";

const { url, fields } = await createPresignedPost(s3, {
  Bucket: BUCKET,
  Key: `uploads/${userId}/${randomUUID()}`,
  Conditions: [
    ["content-length-range", 0, 10_000_000],
    ["starts-with", "$Content-Type", "image/"],
  ],
  Expires: 300,
});
```

**Python**

```python
import uuid
import boto3

s3 = boto3.client("s3")

@app.post("/uploads/presign")
async def presign(user: CurrentUser) -> dict:
    key = f"uploads/{user.id}/{uuid.uuid4()}"
    return await asyncio.to_thread(
        s3.generate_presigned_post,
        Bucket=BUCKET,
        Key=key,
        Conditions=[["content-length-range", 0, 10_000_000], ["starts-with", "$Content-Type", "image/"]],
        ExpiresIn=300,
    )
```

The response shape (`url` and `fields`) is the same, so the frontend upload code doesn't change. The server picks the key, never the client, and a follow-up event or callback confirms the upload before the file is used.

## 408: Scenario: how would you translate a rate-limited client for a third-party API?

**Node.js**

```js
import Bottleneck from "bottleneck";

const limiter = new Bottleneck({ maxConcurrent: 4, minTime: 100 });
const getUser = limiter.wrap((id) => api.get(`/users/${id}`));
```

**Python**

```python
# uv add aiolimiter
from aiolimiter import AsyncLimiter

class PartnerClient:
    def __init__(self) -> None:
        self._http = httpx.AsyncClient(base_url=PARTNER_URL, timeout=10)
        self._rate = AsyncLimiter(10, 1)          # 10 requests per second
        self._sem = asyncio.Semaphore(4)          # 4 at a time

    @retry(stop=stop_after_attempt(4), wait=wait_exponential_jitter(1, 30),
           retry=retry_if_exception_type(RetryableError))
    async def get_user(self, user_id: str) -> dict:
        async with self._sem, self._rate:
            res = await self._http.get(f"/users/{user_id}")
        if res.status_code == 429 or res.status_code >= 500:
            raise RetryableError(res.status_code)
        res.raise_for_status()
        return res.json()
```

This limits one process. With several workers or pods, keep the limit in Redis or divide the budget per process. Honor the API's `Retry-After` header when it sends one.

## 409: Scenario: how would you translate a GraphQL server that uses DataLoader?

**Node.js**

```js
const userLoader = new DataLoader(async (ids) => {
  const users = await db.user.findMany({ where: { id: { in: ids } } });
  return ids.map((id) => users.find((u) => u.id === id));
});
const resolvers = {
  Post: { author: (post, _, ctx) => ctx.userLoader.load(post.authorId) },
};
```

**Python**

```python
from strawberry.dataloader import DataLoader

async def load_users(ids: list[int]) -> list[User | None]:
    rows = (await session.scalars(select(UserRow).where(UserRow.id.in_(ids)))).all()
    by_id = {u.id: u for u in rows}
    return [by_id.get(i) for i in ids]

async def get_context() -> dict:
    return {"user_loader": DataLoader(load_fn=load_users)}   # new loader per request

@strawberry.type
class Post:
    author_id: strawberry.Private[int]

    @strawberry.field
    async def author(self, info: strawberry.Info) -> User | None:
        return await info.context["user_loader"].load(self.author_id)

graphql_app = GraphQLRouter(schema, context_getter=get_context)
```

The batching works the same way: loads in one tick are collected and sent as one query. Create the loader per request so the cache never leaks data between users. Build a dict for the results instead of the `O(n²)` `find` in the original.

## 410: Scenario: how would you translate a Node.js CLI tool?

**Node.js**

```js
#!/usr/bin/env node
import { Command } from "commander";
import ora from "ora";

new Command()
  .argument("<dir>")
  .option("-c, --concurrency <n>", "parallel uploads", "4")
  .action(async (dir, opts) => {
    const spinner = ora("Uploading").start();
    await uploadAll(dir, Number(opts.concurrency));
    spinner.succeed("Done");
  })
  .parse();
```

**Python**

```python
import asyncio
from pathlib import Path
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def upload(dir: Path, concurrency: int = typer.Option(4, "-c", "--concurrency")) -> None:
    files = [p for p in dir.rglob("*") if p.is_file()]
    with console.status("Uploading"):          # spinner, like ora
        asyncio.run(upload_all(files, concurrency))
    console.print("[green]Done[/green]")
```

```toml
[project.scripts]
uploader = "uploader.cli:app"
```

`typer` and `rich` replace `commander`, `ora` and `chalk`. Users install it with `uv tool install uploader` or run it once with `uvx uploader`, the same experience as `npx`.

## 411: Scenario: how would you translate an AWS Lambda handler behind API Gateway?

**Node.js**

```js
export const handler = async (event) => {
  const body = JSON.parse(event.body ?? "{}");
  const item = await ddb.send(
    new GetCommand({ TableName: TABLE, Key: { id: body.id } }),
  );
  return { statusCode: 200, body: JSON.stringify(item.Item ?? null) };
};
```

**Python**

```python
import json
import os
import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE"])   # created once per container

def handler(event, context):
    body = json.loads(event.get("body") or "{}")
    item = table.get_item(Key={"id": body["id"]}).get("Item")
    return {"statusCode": 200, "body": json.dumps(item, default=str)}
```

Python Lambda handlers are usually sync, which is fine because one container serves one request at a time. DynamoDB returns numbers as `Decimal` in Python, so pass `default=str` or convert them, or `json.dumps` fails. AWS Lambda Powertools has a Python version with the same logging, tracing and validation helpers.

## 412: Scenario: how would you translate a nightly report job?

**Node.js**

```js
cron.schedule("0 2 * * *", async () => {
  const rows = await db.query(REPORT_SQL);
  const csv = toCsv(rows);
  await s3.send(
    new PutObjectCommand({ Bucket, Key: `reports/${today()}.csv`, Body: csv }),
  );
  await slack.send("Report ready");
});
```

**Python**

```python
# report.py, run by a scheduler (Kubernetes CronJob, ECS scheduled task, Celery beat)
import csv
import io
from datetime import date

def main() -> None:
    with engine.connect() as conn:
        rows = conn.execute(text(REPORT_SQL)).mappings().all()
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=rows[0].keys() if rows else [])
    writer.writeheader()
    writer.writerows(rows)
    s3.put_object(Bucket=BUCKET, Key=f"reports/{date.today()}.csv", Body=buf.getvalue().encode())
    notify_slack("Report ready")

if __name__ == "__main__":
    main()
```

Move the schedule out of the web process into a platform scheduler, so it runs once and its exit code shows success or failure. Make the job safe to re-run for the same day.

## 413: Scenario: how would you translate multi-tenant request scoping?

**Node.js**

```js
app.use(async (req, res, next) => {
  const tenant = await tenants.bySubdomain(req.hostname.split(".")[0]);
  if (!tenant) return res.sendStatus(404);
  als.run({ tenantId: tenant.id }, next);
});
// Prisma extension adds where: { tenantId } to every query
```

**Python**

```python
current_tenant: ContextVar[int] = ContextVar("current_tenant")

@app.middleware("http")
async def tenant_scope(request: Request, call_next):
    sub = request.url.hostname.split(".")[0]
    tenant = await tenants.by_subdomain(sub)
    if tenant is None:
        return JSONResponse({"error": "Unknown tenant"}, status_code=404)
    token = current_tenant.set(tenant.id)
    try:
        return await call_next(request)
    finally:
        current_tenant.reset(token)

from sqlalchemy import event
from sqlalchemy.orm import Session, with_loader_criteria

@event.listens_for(Session, "do_orm_execute")
def add_tenant_filter(state) -> None:
    if state.is_select:
        state.statement = state.statement.options(
            with_loader_criteria(TenantScoped, lambda cls: cls.tenant_id == current_tenant.get(),
                                 include_aliases=True)
        )
```

`with_loader_criteria` is SQLAlchemy's version of a Prisma query extension that adds the tenant filter. For a stronger guarantee, use Postgres row-level security and set the tenant with `SET LOCAL app.tenant_id` per transaction, so a forgotten filter can't leak data.

## 414: Scenario: how would you translate a cached aggregation endpoint?

**Node.js**

```js
app.get("/stats", async (req, res) => {
  const cached = await redis.get("stats");
  if (cached) return res.type("json").send(cached);
  const stats = await computeStats();
  await redis.set("stats", JSON.stringify(stats), "EX", 60);
  res.json(stats);
});
```

**Python**

```python
@app.get("/stats")
async def stats(r: RedisDep) -> Response:
    if (cached := await r.get("stats")) is not None:
        return Response(cached, media_type="application/json")
    data = StatsOut.model_validate(await compute_stats())
    body = data.model_dump_json(by_alias=True)
    await r.set("stats", body, ex=60)
    return Response(body, media_type="application/json")
```

Return the cached bytes directly instead of parsing and re-serializing them. Store the final JSON, already in the API's format, so cached and fresh responses are byte-for-byte the same.

## 415: Scenario: how would you translate a job progress endpoint that streams updates?

**Node.js**

```js
app.get("/jobs/:id/progress", async (req, res) => {
  res.writeHead(200, { "Content-Type": "text/event-stream" });
  const sub = redis.duplicate();
  await sub.subscribe(`job:${req.params.id}`);
  sub.on("message", (_, msg) => res.write(`data: ${msg}\n\n`));
  req.on("close", () => sub.quit());
});
```

**Python**

```python
@app.get("/jobs/{job_id}/progress")
async def progress(job_id: str, r: RedisDep) -> StreamingResponse:
    async def events():
        pubsub = r.pubsub()
        await pubsub.subscribe(f"job:{job_id}")
        try:
            async for msg in pubsub.listen():
                if msg["type"] == "message":
                    data = msg["data"].decode() if isinstance(msg["data"], bytes) else msg["data"]
                    yield f"data: {data}\n\n"
        finally:
            await pubsub.unsubscribe()
            await pubsub.aclose()
    return StreamingResponse(events(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
```

When the client disconnects, the generator is cancelled and the `finally` block unsubscribes, like `req.on("close")`. `X-Accel-Buffering: no` stops Nginx from buffering the stream. Each open stream holds a Redis connection, so watch the pool size.

## 416: What do you gain and lose by moving a backend from Node.js to Python?

**Gain:**

- Direct access to the data and machine learning ecosystem (NumPy, pandas, PyTorch, scikit-learn, LLM SDKs).
- Mature frameworks with batteries included (Django admin, ORM, migrations).
- Pydantic and FastAPI give validation, typing and OpenAPI from one source.
- One language for backend, data and ML teams.

**Lose:**

- Shared TypeScript types and code between frontend and backend.
- V8's speed for pure-language logic, so you need more instances for CPU-heavy work.
- Async by default: Python mixes sync and async libraries, which creates new kinds of bugs.
- npm's huge selection for some web-specific tasks.

**Node.js**

```ts
import type { Order } from "@acme/shared"; // used by frontend and backend
```

**Python**

```python
# shared contract now lives in OpenAPI, generated for the frontend
```

The move is worth it when the business needs Python's ecosystem, not just because of team preference.

## 417: When should you not translate a Node.js service into Python?

- The service works, is rarely changed, and nobody needs Python features in it.
- It depends on real-time features where Node is a better fit (many WebSocket connections with little CPU per message) and the team has no async Python experience.
- The frontend and backend share a lot of TypeScript code, such as validation or business rules.
- There is no test coverage and no time to build it first.
- The real problem is code quality, which a rewrite in any language won't fix.

**Node.js**

```text
node-service  ->  keep, wrap with a stable API
```

**Python**

```text
new-ml-service  ->  write in Python, called by the Node service
```

Often the better move is a new Python service for the parts that need Python (ML, data processing), while the Node service stays.

## 418: How does the CI pipeline change after the migration?

**Node.js**

```yaml
- uses: actions/setup-node@v6
  with: { node-version: 24, cache: npm }
- run: npm ci
- run: npm run lint && npm run typecheck && npm test
```

**Python**

```yaml
- uses: astral-sh/setup-uv@v7
  with: { enable-cache: true }
- run: uv sync --frozen
- run: uv run ruff check . && uv run ruff format --check .
- run: uv run mypy src
- run: uv run pytest -n auto --cov=app
- run: uvx pip-audit
```

Add a job that exports `openapi.json` and checks it against the committed version, so API changes are reviewed. Cache the uv cache directory, as you cached `~/.npm`. Use `pytest-xdist` (`-n auto`) to run tests in parallel.

## 419: How do you check observability parity before cutting over?

The new service should be at least as easy to run as the old one. Check:

- Same log fields (`requestId`, `userId`, `route`, `status`, `durationMs`) and log levels.
- Same metric names and labels (`http_server_duration`, route templates like `/users/{id}`, not raw paths).
- Traces connected across services through `traceparent`.
- Errors in the same Sentry project, with release tags.
- Dashboards and alerts updated or duplicated for the new service.
- Runbooks updated with Python-specific commands (`py-spy dump`, worker restarts).

**Node.js**

```js
log.info(
  { route: req.route.path, status: res.statusCode, durationMs },
  "request",
);
```

**Python**

```python
log.info("request", route=request.scope["route"].path, status=response.status_code, durationMs=duration_ms)
```

## 420: How do you avoid writing "JavaScript in Python"?

Translated code often works but reads like JavaScript. Signs and fixes:

| JavaScript habit                     | Pythonic version                  |
| ------------------------------------ | --------------------------------- |
| `for i in range(len(items))`         | `for i, item in enumerate(items)` |
| dicts everywhere for structured data | dataclasses or Pydantic models    |
| callbacks for async flow             | `async`/`await` and generators    |
| manual try/finally cleanup           | `with` statements                 |
| getters like `get_name()`            | plain attributes or `@property`   |
| utils classes with static methods    | module-level functions            |
| `camelCase` names                    | `snake_case`                      |

**Node.js**

```js
const result = [];
for (let i = 0; i < users.length; i++) {
  if (users[i].active) result.push(users[i].email);
}
```

**Python**

```python
emails = [u.email for u in users if u.active]
```

Ruff's `UP`, `SIM`, `PERF` and `N` rule sets catch many of these automatically.

## 421: What is EAFP and how does it differ from typical JavaScript style?

EAFP ("easier to ask forgiveness than permission") means trying the operation and handling the exception. LBYL ("look before you leap") means checking first. JavaScript code tends toward LBYL because missing values give `undefined` instead of errors. Python favors EAFP, which also avoids race conditions between the check and the use.

**Node.js**

```js
if (cache.has(key)) return cache.get(key);
if (fs.existsSync(path)) data = fs.readFileSync(path);
```

**Python**

```python
try:
    return cache[key]
except KeyError:
    pass

try:
    data = Path(path).read_bytes()
except FileNotFoundError:
    data = None
```

Don't overdo it: `dict.get` is cleaner than `try/except KeyError` for simple defaults, and exceptions in hot loops cost more than checks.

## 422: What packaging mistakes cause production incidents in Python?

- Installing without the lockfile, so a new version of a dependency arrives on deploy.
- Building the image on a Mac (ARM64) and running it on AMD64 servers with native wheels.
- Forgetting a system library (`libpq`, `libjpeg`) that a source build needs.
- Using `pip install -e .` in production images.
- Relying on transitive dependencies you import directly without declaring them.

**Node.js**

```bash
npm ci   # strict install from the lockfile
```

**Python**

```bash
uv sync --frozen --no-dev        # fail if uv.lock and pyproject.toml disagree
uv pip check                     # find broken dependency requirements
uvx deptry .                     # find imported but undeclared dependencies
```

`--frozen` (or `--locked`, which also checks the lock is up to date) is Python's version of `npm ci`.

## 423: How does uv's lockfile handle different platforms?

npm's lockfile records every package, and optional platform-specific packages are filtered at install time. uv creates a universal lockfile: it resolves for all platforms and Python versions in `requires-python` and records environment markers, so one `uv.lock` works on macOS laptops and Linux servers.

**Node.js**

```json
"optionalDependencies": { "@esbuild/linux-x64": "0.25.0" }
```

**Python**

```toml
dependencies = [
  "uvloop>=0.21; sys_platform != 'win32'",
  "pywin32>=308; sys_platform == 'win32'",
]

[tool.uv]
environments = ["sys_platform == 'linux'", "sys_platform == 'darwin'"]
```

Environment markers (PEP 508) say which dependencies apply where. Limiting `environments` speeds up resolution and avoids failures for platforms you don't support.

## 424: How do you roll out type checking on a newly translated codebase?

**Node.js**

```json
{ "compilerOptions": { "strict": true } }
```

**Python**

```toml
[tool.mypy]
strict = true
plugins = ["pydantic.mypy"]

[[tool.mypy.overrides]]
module = ["app.legacy.*"]
disallow_untyped_defs = false

[[tool.mypy.overrides]]
module = ["some_untyped_lib.*"]
ignore_missing_imports = true
```

Translated code can start strict, because you are writing it fresh, which is easier than adding types later. Loosen rules only for modules that still need work, and track them as tasks. Run the checker in CI from day one. Type hints are also what Pydantic and FastAPI use at runtime, so they pay off twice.

## 425: How does Pydantic v2 performance compare to Zod, and how do you keep it fast?

Pydantic v2's core is written in Rust (`pydantic-core`), so validation is fast, usually faster than Zod on V8 for the same schema. The slow parts are usually around it: building models, extra Python-level validators, and validating the same data twice.

**Node.js**

```ts
const user = UserSchema.parse(JSON.parse(raw));
```

**Python**

```python
user = User.model_validate_json(raw)       # parse and validate in one Rust pass
# slower: User.model_validate(json.loads(raw))

trusted = User.model_construct(**row)      # skip validation for trusted internal data
```

Keep `field_validator`s for real rules, since each runs Python code. Use `model_validate_json` for raw input, and don't re-validate data your own code just produced.

## 426: How do you speed up JSON handling in Python?

V8's `JSON.parse` and `JSON.stringify` are very fast native code. Python's `json` module is slower, especially for large payloads.

**Node.js**

```js
JSON.stringify(bigArray);
```

**Python**

```python
import orjson   # uv add orjson

orjson.dumps(data)                 # returns bytes, handles datetime, UUID, dataclasses
orjson.loads(raw)

import msgspec  # uv add msgspec
class Point(msgspec.Struct):
    x: int
    y: int
msgspec.json.decode(raw, type=list[Point])   # typed decode, very fast
```

`orjson` is a drop-in speedup for dumping and loading. Its output is compact and differs slightly from `json.dumps` (no spaces, UTC as `+00:00`), so check clients and snapshots.

## 427: Where does FastAPI spend time serializing responses, and how do you reduce it?

**Node.js**

```js
res.json(rows); // one JSON.stringify call
```

**Python**

```python
@app.get("/items")
async def items() -> list[ItemOut]:     # Pydantic validates and serializes the output
    return rows

@app.get("/items-fast")
async def items_fast() -> Response:
    data = TypeAdapter(list[ItemOut]).dump_json(rows)   # one Rust pass
    return Response(data, media_type="application/json")
```

With a return type or `response_model`, FastAPI serializes through Pydantic in Rust, which is fast. Returning a plain dict without one goes through `jsonable_encoder`, which walks the data in Python and is much slower for large lists. For heavy endpoints, return a `Response` with pre-serialized bytes, and paginate.

## 428: How do Python 3.14 template strings compare to JavaScript tagged templates?

**Node.js**

```js
import sql from "./sql.js"; // tagged template: values become parameters
const rows = await sql`SELECT * FROM users WHERE email = ${email}`;
```

**Python**

```python
from string.templatelib import Interpolation, Template   # Python 3.14+

def sql(template: Template) -> tuple[str, list]:
    parts, params = [], []
    for item in template:
        if isinstance(item, Interpolation):
            parts.append(f"${len(params) + 1}")
            params.append(item.value)
        else:
            parts.append(item)
    return "".join(parts), params

query, params = sql(t"SELECT * FROM users WHERE email = {email}")
# ("SELECT * FROM users WHERE email = $1", ["ana@example.com"])
```

A `t"..."` string doesn't become a `str`. It gives the function the static parts and the values separately, exactly like a tag function. That makes safe SQL and HTML builders possible, and libraries are starting to accept templates directly.

## 429: What can structural pattern matching do that JavaScript cannot?

JavaScript has no `match` (a pattern matching proposal is still in progress). Python's `match` destructures and checks types, shapes and values in one step, which replaces long `if`/`else` chains on `type` fields.

**Node.js**

```js
if (msg.type === "move" && typeof msg.x === "number") move(msg.x, msg.y);
else if (msg.type === "chat" && msg.text?.length) say(msg.text);
else if (Array.isArray(msg) && msg[0] === "batch") msg.slice(1).forEach(handle);
```

**Python**

```python
match msg:
    case {"type": "move", "x": int(x), "y": int(y)}:
        move(x, y)
    case {"type": "chat", "text": str(text)} if text:
        say(text)
    case ["batch", *items]:
        for item in items:
            handle(item)
    case _:
        raise ValueError(f"Unknown message: {msg!r}")
```

Mapping patterns ignore extra keys, `int(x)` checks the type and binds the value, and guards (`if text`) add conditions. For untrusted input, still validate with Pydantic first and match on the models.

## 430: How do generator send and coroutine-style generators compare to JavaScript generators?

Both languages let you send values into a generator: `gen.next(value)` in JavaScript and `gen.send(value)` in Python. Python adds `yield from` to delegate to sub-generators, and generators can `return` a value that `yield from` receives.

**Node.js**

```js
function* averager() {
  let total = 0,
    count = 0,
    avg;
  while (true) {
    const value = yield avg;
    total += value;
    avg = total / ++count;
  }
}
const g = averager();
g.next();
g.next(10).value; // 10
```

**Python**

```python
def averager():
    total = count = 0
    avg = None
    while True:
        value = yield avg
        total += value
        count += 1
        avg = total / count

g = averager()
next(g)          # prime it
g.send(10)       # 10.0
g.send(20)       # 15.0
```

This style was how asyncio worked before `async def`, and you will still see it in old code. New code should use `async def` for concurrency and plain generators for lazy data.

## 431: How do descriptors compare to Object.defineProperty?

**Node.js**

```js
Object.defineProperty(obj, "email", {
  get() {
    return this._email;
  },
  set(v) {
    if (!v.includes("@")) throw new Error("bad email");
    this._email = v.toLowerCase();
  },
});
```

**Python**

```python
class Email:
    def __set_name__(self, owner, name: str) -> None:
        self.private = f"_{name}"

    def __get__(self, obj, objtype=None):
        return self if obj is None else getattr(obj, self.private)

    def __set__(self, obj, value: str) -> None:
        if "@" not in value:
            raise ValueError("bad email")
        setattr(obj, self.private, value.lower())

class User:
    email = Email()     # reusable on any class and attribute
```

A descriptor is a reusable `defineProperty` defined once on the class. `@property`, methods, `classmethod` and SQLAlchemy's mapped columns are all built on descriptors.

## 432: How do metaclasses and the init subclass hook compare to TypeScript class decorators?

**Node.js**

```ts
const registry = new Map<string, Function>();
function handler(name: string) {
  return (cls: Function) => {
    registry.set(name, cls);
  };
}
@handler("email")
class EmailHandler {}
```

**Python**

```python
class Handler:
    registry: dict[str, type["Handler"]] = {}

    def __init_subclass__(cls, *, name: str, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        Handler.registry[name] = cls

class EmailHandler(Handler, name="email"):
    ...

Handler.registry["email"]   # EmailHandler
```

`__init_subclass__` runs whenever a subclass is defined, which covers most "register this class" needs without metaclasses. Class decorators also work in Python. Metaclasses are mainly for frameworks such as ORMs, and application code rarely needs them.

## 433: Why should import-time work be avoided in Python services?

Importing a module runs its top-level code. Connecting to databases, reading secrets, or making HTTP calls at import time slows startup, breaks tests that import the module, and runs before forking in pre-fork servers. The same is true for Node.js, but Python tools (pytest collection, Alembic, Celery workers, `manage.py` commands) import your modules in more situations.

**Node.js**

```js
// db.js
export const pool = await createPool(); // top-level await connects on import
```

**Python**

```python
# bad: connects whenever anything imports this module
engine = create_engine(os.environ["DATABASE_URL"])
engine.connect()

# good: lazy, created once on first use
from functools import cache

@cache
def get_engine():
    return create_engine(get_settings().database_url, pool_pre_ping=True)
```

Keep module top levels to definitions. Create resources in the lifespan hook or in cached factory functions.

## 434: How does monkeypatching compare to changing prototypes?

**Node.js**

```js
Array.prototype.last = function () {
  return this[this.length - 1];
}; // affects every array everywhere
```

**Python**

```python
list.last = lambda self: self[-1]    # TypeError: built-in types can't be changed

import some_lib
some_lib.client.send = fake_send     # allowed for modules and normal classes
```

Python blocks patching built-in types, but modules and normal classes can be changed at runtime. Use it only in tests (`unittest.mock.patch`, pytest's `monkeypatch` fixture), where changes are undone automatically. Libraries like `gevent` patch the standard library globally, which explains strange behavior in some older Python apps.

## 435: What identity pitfalls does is have in Python?

**Node.js**

```js
"abc" === "abc"; // true, compares values for primitives
```

**Python**

```python
a = 256; b = 256
a is b            # True (small ints are cached)
a = 1000; b = int("1000")
a is b            # False: different objects with the same value
"hello" is "hello"   # may be True (interning), SyntaxWarning in recent versions
```

Use `is` only for singletons: `None`, `True`, `False`, and sentinel objects. Use `==` for values. Code that seems to work with `is` on numbers or strings breaks with larger values or strings built at runtime.

## 436: What are slots and how do they relate to V8 hidden classes?

V8 speeds up objects that always have the same properties by giving them hidden classes. CPython instances store attributes in a per-instance dict by default, which costs memory. `__slots__` declares a fixed attribute list, so instances store values in a compact array and reject new attributes.

**Node.js**

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  } // same shape for every instance: fast
}
```

**Python**

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: float
    y: float

p = Point(1, 2)
p.z = 3   # AttributeError: no __dict__
```

Slots matter when you hold millions of small objects in memory. Recent CPython versions already share dict keys between instances, so for normal app code the gain is small.

## 437: How do key ordering rules differ between objects and dicts?

**Node.js**

```js
const o = { b: 1, 2: "x", a: 2, 1: "y" };
Object.keys(o); // ["1", "2", "b", "a"]: integer-like keys come first
```

**Python**

```python
d = {"b": 1, "2": "x", "a": 2, "1": "y"}
list(d)   # ['b', '2', 'a', '1']: pure insertion order
```

JavaScript puts integer-like keys first, in numeric order. Python dicts always keep insertion order. If a client depends on key order in a JSON object (it shouldn't, but some do), the output can change after translation. Send arrays when order matters.

## 438: What happens when StopIteration escapes a generator?

Since Python 3.7 (PEP 479), a `StopIteration` raised inside a generator is turned into a `RuntimeError`. This catches a class of bugs where a call to `next()` inside a generator silently ended iteration early. JavaScript generators have no equivalent issue, since `next()` returns `{ done: true }` instead of raising.

**Node.js**

```js
function* firstOfEach(iters) {
  for (const it of iters) yield it.next().value; // undefined for empty iterators
}
```

**Python**

```python
def first_of_each(iters):
    for it in iters:
        yield next(it)            # RuntimeError for an empty iterator

def first_of_each_safe(iters):
    for it in iters:
        yield next(it, None)      # default instead of StopIteration
```

Pass a default to `next()` inside generators, or catch `StopIteration` and `return`.

## 439: How do codemods compare between JavaScript and Python?

**Node.js**

```bash
npx jscodeshift -t rename-fn.js src/
```

**Python**

```python
# uv add libcst
import libcst as cst

class RenameGetUser(cst.CSTTransformer):
    def leave_Name(self, original: cst.Name, updated: cst.Name) -> cst.Name:
        return updated.with_changes(value="fetch_user") if original.value == "get_user" else updated

tree = cst.parse_module(source)
new_source = tree.visit(RenameGetUser()).code   # keeps comments and formatting
```

`libcst` keeps formatting and comments like jscodeshift. `ast` loses them. For simple pattern rewrites, `ast-grep` works across both languages with one tool, which helps when a refactor spans the Node and Python services.

## 440: How do you keep a large async test suite fast and reliable?

**Node.js**

```bash
npx vitest run   # runs files in parallel workers by default
```

**Python**

```bash
uv add --dev pytest-xdist
uv run pytest -n auto              # parallel across CPU cores
```

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "session"
asyncio_default_test_loop_scope = "session"
```

Share one event loop per session when fixtures like database engines must live across tests, because an engine created on one loop cannot be used on another. With xdist, give each worker its own database (using the `worker_id` fixture) so parallel tests don't collide.

## 441: How does property-based testing translate?

**Node.js**

```js
import fc from "fast-check";

test("slugify is idempotent", () => {
  fc.assert(
    fc.property(fc.string(), (s) => slugify(slugify(s)) === slugify(s)),
  );
});
```

**Python**

```python
from hypothesis import given, strategies as st

@given(st.text())
def test_slugify_idempotent(s: str) -> None:
    assert slugify(slugify(s)) == slugify(s)

@given(st.builds(UserIn))   # generate valid Pydantic models
def test_create_user_roundtrip(user: UserIn) -> None:
    ...
```

Hypothesis shrinks failing inputs to the smallest example and saves them in a local database so they are re-run first next time. Running the same properties against the Node and Python versions of a function is a strong way to check a translation.

## 442: How do micro-benchmarks translate?

**Node.js**

```js
import { bench, run } from "mitata";

bench("parse", () => JSON.parse(payload));
await run();
```

**Python**

```bash
python -m timeit -s "import json; p=open('p.json').read()" "json.loads(p)"
uvx pyperf timeit -s "import json; p=open('p.json').read()" "json.loads(p)"
```

```python
# pytest-benchmark
def test_parse(benchmark) -> None:
    benchmark(json.loads, payload)
```

`pyperf` runs several processes, warms up and reports noise, so results are more trustworthy than a single `timeit`. Micro-benchmarks help you choose between implementations, but service capacity is decided by end-to-end load tests.

## 443: How do HTTP/2 and HTTP/3 support compare?

**Node.js**

```js
import http2 from "node:http2";

http2.createSecureServer({ key, cert }, app).listen(443);
```

**Python**

```bash
hypercorn app.main:app --certfile cert.pem --keyfile key.pem --bind 0.0.0.0:443   # HTTP/2, HTTP/3 with --quic-bind
granian --interface asgi --http 2 app.main:app
```

```python
client = httpx.AsyncClient(http2=True)   # needs: uv add "httpx[http2]"
```

Uvicorn speaks HTTP/1.1 only. In practice both Node and Python services usually speak HTTP/1.1 behind a load balancer or proxy that handles HTTP/2 and HTTP/3 with clients, so this rarely matters. It does matter for gRPC, which needs HTTP/2 end to end.

## 444: How do you tune outgoing connection pools?

**Node.js**

```js
import { Agent, setGlobalDispatcher } from "undici";

setGlobalDispatcher(new Agent({ connections: 50, keepAliveTimeout: 10_000 }));
```

**Python**

```python
client = httpx.AsyncClient(
    limits=httpx.Limits(max_connections=50, max_keepalive_connections=20, keepalive_expiry=10),
    timeout=httpx.Timeout(10.0, connect=2.0, pool=1.0),
)
```

When all connections are busy, httpx waits up to the `pool` timeout and then raises `PoolTimeout`. That error points to too little pool space or slow upstream calls, not network failure, so track it separately. Remember that each worker process has its own pool.

## 445: What goes wrong when you open connections before a server forks workers?

Gunicorn with `preload_app = True` imports the app once and then forks workers. Sockets, database connections, thread pools and event loops created before the fork are shared or broken in the children, which causes errors like "SSL error: decryption failed" or mixed-up query results. Node's cluster doesn't fork a running heap, so Node developers rarely meet this.

**Node.js**

```js
// each cluster worker runs the module from scratch
if (cluster.isPrimary) for (let i = 0; i < 4; i++) cluster.fork();
else startServer();
```

**Python**

```python
# gunicorn.conf.py
preload_app = True

def post_fork(server, worker):
    from app.db import engine
    engine.dispose(close=False)   # drop inherited connections, keep the parent's alone
```

Either avoid preloading, or reset pools in a `post_fork` hook. Preloading saves memory through copy-on-write, but reference counting writes to object headers, so pages get copied anyway. `gc.freeze()` before forking helps a little.

## 446: What should a code review checklist for translated code include?

- Every `async def` path uses only non-blocking libraries, or wraps blocking calls with `asyncio.to_thread`.
- No mutable default arguments. No `is` comparisons with values.
- Truthiness checks (`if x:`) match the original intent for `0`, `""` and `[]`.
- Rounding, `%`, regex anchors, string lengths and date parsing match the old behavior or were changed on purpose.
- JSON field names, `null` vs missing fields, number formats and error shapes match the contract.
- Timeouts set on every outgoing call. Pools sized for the worker count.
- Background tasks are owned and awaited, and `CancelledError` is never swallowed.
- Secrets are not in `__repr__` or logs. Inputs are limited in size.
- Type checker and Ruff pass in strict mode.

**Node.js**

```js
const page = Number(req.query.page) || 1;
```

**Python**

```python
page: int = Query(1, ge=1)   # reviewer checks: same default, same handling of 0 and junk input
```

## 447: How do you help a Node.js team become productive in Python?

- Start with the toolchain they know in spirit: uv (npm), Ruff (ESLint + Prettier), pytest (Jest), Pydantic (Zod), FastAPI (Express/Nest).
- Write a short internal style guide with the top ten differences (truthiness, defaults, async rules, `None`).
- Turn on strict type checking and Ruff rules from day one, so tools teach the idioms.
- Pair JavaScript developers with someone who knows Python for the first services.
- Port a small, low-risk service first and treat it as the reference project.

**Node.js**

```bash
npm create my-template
```

**Python**

```bash
uvx copier copy gh:acme/python-service-template my-service   # one template for every new service
```

A service template with logging, settings, health checks, tests and CI already set up removes most early mistakes.

## 448: How do you plan rollback during the migration?

Every step must be reversible in minutes:

- Route traffic with weights or flags at the gateway, so rollback is a config change, not a deploy.
- Keep the Node service deployed and warm until the Python routes have run cleanly for an agreed period.
- Keep the schema compatible with both services (expand and contract), and don't drop old columns until rollback is no longer needed.
- Don't make one-way data changes (new formats only Python understands) until after the rollback window.
- Practice the rollback once in staging.

**Node.js**

```yaml
# gateway weights during rollout
- backendRefs:
    [
      { name: node-api, port: 3000, weight: 90 },
      { name: py-api, port: 8000, weight: 10 },
    ]
```

**Python**

```yaml
# rollback: one line
- backendRefs:
    [
      { name: node-api, port: 3000, weight: 100 },
      { name: py-api, port: 8000, weight: 0 },
    ]
```

## 449: How do you know when the migration is done and the Node service can be removed?

Set exit criteria up front and measure them:

- 100% of traffic for every route served by Python for a set period (for example 2-4 weeks).
- Error rate and p95/p99 latency equal to or better than the Node baseline.
- No calls reach the Node service (check access logs and metrics, including internal callers and cron jobs).
- All background jobs drained from the old queues.
- Dashboards, alerts, runbooks and on-call docs point only to the new service.
- The database schema no longer needs Node-only columns or behavior.

**Node.js**

```bash
# final check: any traffic left?
kubectl logs deploy/node-api --since=168h | grep -c '"method"'
```

**Python**

```bash
# then remove: scale to zero first, delete after a quiet period
kubectl scale deploy/node-api --replicas=0
```

Scaling to zero before deleting gives one last cheap rollback option.

## 450: What does a final Node.js to Python migration checklist look like?

1. **Scope:** list routes, jobs, cron tasks, webhooks, WebSocket events and internal callers.
2. **Contract:** export OpenAPI from the Node service (or write it), and build contract tests that run against both services.
3. **Foundation:** set up the Python template: uv, Ruff, mypy or pyright, pytest, pydantic-settings, logging, OpenTelemetry, Sentry, Dockerfile, CI.
4. **Data:** decide schema ownership, write the baseline migration, and copy ORM-level defaults.
5. **Auth:** make sure JWTs, sessions and password hashes work in both services.
6. **Port:** route group by route group, with camelCase aliases, error shapes and status codes matched.
7. **Async review:** no blocking calls in `async def`, timeouts everywhere, owned background tasks.
8. **Verify:** contract tests, shadow traffic, load tests, and a diff of error and latency metrics.
9. **Roll out:** weighted routing or flags, with a practiced rollback.
10. **Jobs:** move queues with a drain period, and make tasks idempotent.
11. **Finish:** meet the exit criteria, scale Node to zero, then delete it and its infrastructure.

**Node.js**

```text
node-api: 100% -> 90% -> 50% -> 0% -> removed
```

**Python**

```text
py-api:     0% -> 10% -> 50% -> 100% (owner)
```
