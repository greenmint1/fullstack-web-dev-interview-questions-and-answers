# Back-End Debugging Interview Questions and Answers

_Last updated: November 6, 2026_

450 back-end debugging interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover the general way to debug (not tied to any tool), Node.js and the event loop, frameworks and APIs (Express, Fastify, NestJS, REST, GraphQL), databases and ORMs (SQL, Prisma, Mongoose, MongoDB, DynamoDB, Redis), queues (Kafka, RabbitMQ, BullMQ), microservices and observability, infrastructure (Docker, Kubernetes, Nginx, AWS, Azure, GCP, Terraform, GitHub Actions), security, JWT and auth, TLS and certificates, and how to debug safely in production without leaking secrets or personal data. Examples target current Node.js LTS versions (22 and 24), Express 5, Fastify 5 and NestJS 11.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is debugging, and how is it different from testing?](#1-what-is-debugging-and-how-is-it-different-from-testing)
- [2: What steps do you follow when you start debugging a bug?](#2-what-steps-do-you-follow-when-you-start-debugging-a-bug)
- [3: Why is reproducing a bug the first thing to do?](#3-why-is-reproducing-a-bug-the-first-thing-to-do)
- [4: What is a minimal reproduction?](#4-what-is-a-minimal-reproduction)
- [5: What is the difference between a symptom and a root cause?](#5-what-is-the-difference-between-a-symptom-and-a-root-cause)
- [6: What is binary search debugging?](#6-what-is-binary-search-debugging)
- [7: How does git bisect help find a bug?](#7-how-does-git-bisect-help-find-a-bug)
- [8: What is rubber duck debugging?](#8-what-is-rubber-duck-debugging)
- [9: What questions should you ask when a bug report comes in?](#9-what-questions-should-you-ask-when-a-bug-report-comes-in)
- [10: Why should you change only one thing at a time while debugging?](#10-why-should-you-change-only-one-thing-at-a-time-while-debugging)
- [11: What is the difference between logs, metrics, and traces?](#11-what-is-the-difference-between-logs-metrics-and-traces)
- [12: What are log levels and when do you use each?](#12-what-are-log-levels-and-when-do-you-use-each)
- [13: What is structured logging?](#13-what-is-structured-logging)
- [14: What is a stack trace and how do you read it?](#14-what-is-a-stack-trace-and-how-do-you-read-it)
- [15: What is a breakpoint?](#15-what-is-a-breakpoint)
- [16: What is the difference between step over, step into, and step out?](#16-what-is-the-difference-between-step-over-step-into-and-step-out)
- [17: What is a conditional breakpoint and a logpoint?](#17-what-is-a-conditional-breakpoint-and-a-logpoint)
- [18: How do you write a good bug report for a back-end issue?](#18-how-do-you-write-a-good-bug-report-for-a-back-end-issue)
- [19: What is a regression?](#19-what-is-a-regression)
- [20: Why should you write a test that reproduces a bug before fixing it?](#20-why-should-you-write-a-test-that-reproduces-a-bug-before-fixing-it)
- [21: How do you start Node.js with the inspector?](#21-how-do-you-start-nodejs-with-the-inspector)
- [22: What is the difference between --inspect and --inspect-brk?](#22-what-is-the-difference-between---inspect-and---inspect-brk)
- [23: How do you debug Node.js in VS Code?](#23-how-do-you-debug-nodejs-in-vs-code)
- [24: How do you connect Chrome DevTools to a Node.js process?](#24-how-do-you-connect-chrome-devtools-to-a-nodejs-process)
- [25: What does the debugger statement do?](#25-what-does-the-debugger-statement-do)
- [26: What is the Node.js event loop, in simple words?](#26-what-is-the-nodejs-event-loop-in-simple-words)
- [27: What does it mean to block the event loop?](#27-what-does-it-mean-to-block-the-event-loop)
- [28: What are common things that block the event loop?](#28-what-are-common-things-that-block-the-event-loop)
- [29: What is the difference between an uncaught exception and an unhandled promise rejection?](#29-what-is-the-difference-between-an-uncaught-exception-and-an-unhandled-promise-rejection)
- [30: What happens by default when a promise rejection is not handled in Node.js?](#30-what-happens-by-default-when-a-promise-rejection-is-not-handled-in-nodejs)
- [31: Why should you always await or return promises?](#31-why-should-you-always-await-or-return-promises)
- [32: What is the NODE_DEBUG environment variable?](#32-what-is-the-node_debug-environment-variable)
- [33: What is the debug package and how is it used?](#33-what-is-the-debug-package-and-how-is-it-used)
- [34: Why do async stack traces sometimes look incomplete?](#34-why-do-async-stack-traces-sometimes-look-incomplete)
- [35: What are source maps, and why do they matter when debugging TypeScript on the server?](#35-what-are-source-maps-and-why-do-they-matter-when-debugging-typescript-on-the-server)
- [36: What does console.time do, and when is it useful?](#36-what-does-consoletime-do-and-when-is-it-useful)
- [37: What does "Cannot find module" mean and how do you fix it?](#37-what-does-cannot-find-module-mean-and-how-do-you-fix-it)
- [38: What does EADDRINUSE mean?](#38-what-does-eaddrinuse-mean)
- [39: What do ECONNREFUSED, ECONNRESET and ETIMEDOUT mean?](#39-what-do-econnrefused-econnreset-and-etimedout-mean)
- [40: What is "JavaScript heap out of memory"?](#40-what-is-javascript-heap-out-of-memory)
- [41: How do you debug an Express route that returns 404?](#41-how-do-you-debug-an-express-route-that-returns-404)
- [42: What is error-handling middleware in Express?](#42-what-is-error-handling-middleware-in-express)
- [43: What does "Cannot set headers after they are sent to the client" mean?](#43-what-does-cannot-set-headers-after-they-are-sent-to-the-client-mean)
- [44: Why does an Express request hang without a response?](#44-why-does-an-express-request-hang-without-a-response)
- [45: How does Express 5 handle errors thrown in async handlers?](#45-how-does-express-5-handle-errors-thrown-in-async-handlers)
- [46: Why is req.body undefined in Express?](#46-why-is-reqbody-undefined-in-express)
- [47: How do you turn on logging in Fastify?](#47-how-do-you-turn-on-logging-in-fastify)
- [48: What is request.log in Fastify?](#48-what-is-requestlog-in-fastify)
- [49: How do you see registered routes in Fastify?](#49-how-do-you-see-registered-routes-in-fastify)
- [50: What does "Nest can't resolve dependencies" mean in NestJS?](#50-what-does-nest-cant-resolve-dependencies-mean-in-nestjs)
- [51: How do you use the built-in Logger in NestJS?](#51-how-do-you-use-the-built-in-logger-in-nestjs)
- [52: How do you run a NestJS app in debug mode?](#52-how-do-you-run-a-nestjs-app-in-debug-mode)
- [53: What do the 4xx status codes tell you when debugging an API?](#53-what-do-the-4xx-status-codes-tell-you-when-debugging-an-api)
- [54: What do 500, 502, 503 and 504 usually mean?](#54-what-do-500-502-503-and-504-usually-mean)
- [55: How do you use curl to debug an API?](#55-how-do-you-use-curl-to-debug-an-api)
- [56: What is a correlation ID or request ID?](#56-what-is-a-correlation-id-or-request-id)
- [57: How do you debug a GraphQL query that returns null?](#57-how-do-you-debug-a-graphql-query-that-returns-null)
- [58: Why does GraphQL often return 200 even when there are errors?](#58-why-does-graphql-often-return-200-even-when-there-are-errors)
- [59: What is the N+1 problem in GraphQL and how do you spot it?](#59-what-is-the-n1-problem-in-graphql-and-how-do-you-spot-it)
- [60: How do you debug a REST API contract mismatch between client and server?](#60-how-do-you-debug-a-rest-api-contract-mismatch-between-client-and-server)
- [61: How do you see the SQL queries an app runs?](#61-how-do-you-see-the-sql-queries-an-app-runs)
- [62: What does EXPLAIN do in SQL?](#62-what-does-explain-do-in-sql)
- [63: What is a slow query log?](#63-what-is-a-slow-query-log)
- [64: How do you enable query logging in Prisma?](#64-how-do-you-enable-query-logging-in-prisma)
- [65: What does Prisma error P2002 mean?](#65-what-does-prisma-error-p2002-mean)
- [66: What does Prisma error P2025 mean?](#66-what-does-prisma-error-p2025-mean)
- [67: How do you see the queries Mongoose sends?](#67-how-do-you-see-the-queries-mongoose-sends)
- [68: What is a Mongoose CastError?](#68-what-is-a-mongoose-casterror)
- [69: Why does Mongoose say "buffering timed out after 10000ms"?](#69-why-does-mongoose-say-buffering-timed-out-after-10000ms)
- [70: What does explain() show in MongoDB?](#70-what-does-explain-show-in-mongodb)
- [71: What is the difference between COLLSCAN and IXSCAN?](#71-what-is-the-difference-between-collscan-and-ixscan)
- [72: What is a DynamoDB ConditionalCheckFailedException?](#72-what-is-a-dynamodb-conditionalcheckfailedexception)
- [73: What does ProvisionedThroughputExceededException mean in DynamoDB?](#73-what-does-provisionedthroughputexceededexception-mean-in-dynamodb)
- [74: How do you check if Redis is reachable?](#74-how-do-you-check-if-redis-is-reachable)
- [75: What is the Redis SLOWLOG?](#75-what-is-the-redis-slowlog)
- [76: Why should you not run KEYS * in production?](#76-why-should-you-not-run-keys--in-production)
- [77: What does the WRONGTYPE error mean in Redis?](#77-what-does-the-wrongtype-error-mean-in-redis)
- [78: What is a database connection pool and how can it cause bugs?](#78-what-is-a-database-connection-pool-and-how-can-it-cause-bugs)
- [79: How can missing transactions cause bugs?](#79-how-can-missing-transactions-cause-bugs)
- [80: How do you debug a failed database migration?](#80-how-do-you-debug-a-failed-database-migration)
- [81: What is a message queue and why are queue bugs hard to debug?](#81-what-is-a-message-queue-and-why-are-queue-bugs-hard-to-debug)
- [82: What is consumer lag in Kafka?](#82-what-is-consumer-lag-in-kafka)
- [83: How do you read messages from a Kafka topic to see what is in it?](#83-how-do-you-read-messages-from-a-kafka-topic-to-see-what-is-in-it)
- [84: What is a dead letter queue?](#84-what-is-a-dead-letter-queue)
- [85: What is a poison message?](#85-what-is-a-poison-message)
- [86: What does "unacked" mean in RabbitMQ?](#86-what-does-unacked-mean-in-rabbitmq)
- [87: How do you check queues in RabbitMQ?](#87-how-do-you-check-queues-in-rabbitmq)
- [88: What is a failed job in BullMQ, and how do you see why it failed?](#88-what-is-a-failed-job-in-bullmq-and-how-do-you-see-why-it-failed)
- [89: What is a stalled job in BullMQ?](#89-what-is-a-stalled-job-in-bullmq)
- [90: What does at-least-once delivery mean for debugging?](#90-what-does-at-least-once-delivery-mean-for-debugging)
- [91: Why is debugging microservices harder than debugging a monolith?](#91-why-is-debugging-microservices-harder-than-debugging-a-monolith)
- [92: What is distributed tracing?](#92-what-is-distributed-tracing)
- [93: What is a span and a trace?](#93-what-is-a-span-and-a-trace)
- [94: What is OpenTelemetry?](#94-what-is-opentelemetry)
- [95: What is the traceparent header?](#95-what-is-the-traceparent-header)
- [96: What is a health check endpoint?](#96-what-is-a-health-check-endpoint)
- [97: What are the RED and USE metrics?](#97-what-are-the-red-and-use-metrics)
- [98: What is the difference between monitoring and observability?](#98-what-is-the-difference-between-monitoring-and-observability)
- [99: Why should every network call have a timeout?](#99-why-should-every-network-call-have-a-timeout)
- [100: What is a cascading failure?](#100-what-is-a-cascading-failure)
- [101: How do you see the logs of a Docker container?](#101-how-do-you-see-the-logs-of-a-docker-container)
- [102: How do you get a shell inside a running container?](#102-how-do-you-get-a-shell-inside-a-running-container)
- [103: What does docker inspect show?](#103-what-does-docker-inspect-show)
- [104: What does exit code 137 mean for a container?](#104-what-does-exit-code-137-mean-for-a-container)
- [105: Why does an app work locally but not inside Docker?](#105-why-does-an-app-work-locally-but-not-inside-docker)
- [106: How do you see the full output of a Docker build?](#106-how-do-you-see-the-full-output-of-a-docker-build)
- [107: How do you see the logs of a Kubernetes pod?](#107-how-do-you-see-the-logs-of-a-kubernetes-pod)
- [108: What does kubectl describe pod show?](#108-what-does-kubectl-describe-pod-show)
- [109: What is CrashLoopBackOff?](#109-what-is-crashloopbackoff)
- [110: What is ImagePullBackOff?](#110-what-is-imagepullbackoff)
- [111: Why does a pod stay in Pending?](#111-why-does-a-pod-stay-in-pending)
- [112: What is the difference between liveness and readiness probes?](#112-what-is-the-difference-between-liveness-and-readiness-probes)
- [113: How do you reach a pod or service from your laptop for debugging?](#113-how-do-you-reach-a-pod-or-service-from-your-laptop-for-debugging)
- [114: How do you test an Nginx config?](#114-how-do-you-test-an-nginx-config)
- [115: Where are Nginx logs and what is in them?](#115-where-are-nginx-logs-and-what-is-in-them)
- [116: What does a 502 Bad Gateway from Nginx usually mean?](#116-what-does-a-502-bad-gateway-from-nginx-usually-mean)
- [117: What does a 413 Request Entity Too Large mean?](#117-what-does-a-413-request-entity-too-large-mean)
- [118: What is CloudWatch Logs?](#118-what-is-cloudwatch-logs)
- [119: How do you check which AWS identity your code or CLI is using?](#119-how-do-you-check-which-aws-identity-your-code-or-cli-is-using)
- [120: What does AccessDenied in AWS usually mean and where do you look?](#120-what-does-accessdenied-in-aws-usually-mean-and-where-do-you-look)
- [121: What are Application Insights and Log Analytics in Azure?](#121-what-are-application-insights-and-log-analytics-in-azure)
- [122: What are Cloud Logging and Cloud Trace in GCP?](#122-what-are-cloud-logging-and-cloud-trace-in-gcp)
- [123: How do you see more detail when Terraform fails?](#123-how-do-you-see-more-detail-when-terraform-fails)
- [124: What does terraform plan tell you?](#124-what-does-terraform-plan-tell-you)
- [125: What is a Terraform state lock error?](#125-what-is-a-terraform-state-lock-error)
- [126: How do you turn on debug logging in GitHub Actions?](#126-how-do-you-turn-on-debug-logging-in-github-actions)
- [127: Why does a workflow pass locally but fail in GitHub Actions?](#127-why-does-a-workflow-pass-locally-but-fail-in-github-actions)
- [128: How are secrets masked in GitHub Actions logs?](#128-how-are-secrets-masked-in-github-actions-logs)
- [129: What is the difference between 401 and 403 when debugging auth?](#129-what-is-the-difference-between-401-and-403-when-debugging-auth)
- [130: What is a CORS error and is it a back-end problem?](#130-what-is-a-cors-error-and-is-it-a-back-end-problem)
- [131: What is a JWT made of?](#131-what-is-a-jwt-made-of)
- [132: How do you look inside a JWT safely?](#132-how-do-you-look-inside-a-jwt-safely)
- [133: What does "jwt expired" mean?](#133-what-does-jwt-expired-mean)
- [134: What does "invalid signature" mean for a JWT?](#134-what-does-invalid-signature-mean-for-a-jwt)
- [135: What is clock skew and how does it affect JWT checks?](#135-what-is-clock-skew-and-how-does-it-affect-jwt-checks)
- [136: Why might a cookie-based session not work?](#136-why-might-a-cookie-based-session-not-work)
- [137: What is TLS and what is a certificate?](#137-what-is-tls-and-what-is-a-certificate)
- [138: What does "certificate has expired" mean?](#138-what-does-certificate-has-expired-mean)
- [139: What does "self signed certificate in certificate chain" mean?](#139-what-does-self-signed-certificate-in-certificate-chain-mean)
- [140: How do you check a server's certificate from the command line?](#140-how-do-you-check-a-servers-certificate-from-the-command-line)
- [141: What is NODE_TLS_REJECT_UNAUTHORIZED=0 and why is it dangerous?](#141-what-is-node_tls_reject_unauthorized0-and-why-is-it-dangerous)
- [142: Why should you not log secrets?](#142-why-should-you-not-log-secrets)
- [143: What counts as personal data (PII) in logs?](#143-what-counts-as-personal-data-pii-in-logs)
- [144: What should never be written to logs?](#144-what-should-never-be-written-to-logs)
- [145: Why should tokens not be put in URLs?](#145-why-should-tokens-not-be-put-in-urls)
- [146: What is log redaction?](#146-what-is-log-redaction)
- [147: Why is debugging in production risky?](#147-why-is-debugging-in-production-risky)
- [148: How is debugging in staging different from debugging in production?](#148-how-is-debugging-in-staging-different-from-debugging-in-production)
- [149: How does a feature flag help with debugging?](#149-how-does-a-feature-flag-help-with-debugging)
- [150: What is a rollback, and when is it better than debugging live?](#150-what-is-a-rollback-and-when-is-it-better-than-debugging-live)

### Moderate Questions (151-300)

- [151: How do you debug a bug that only happens sometimes?](#151-how-do-you-debug-a-bug-that-only-happens-sometimes)
- [152: How do you debug "works on my machine" problems?](#152-how-do-you-debug-works-on-my-machine-problems)
- [153: How do you use the "what changed" approach after a deploy?](#153-how-do-you-use-the-what-changed-approach-after-a-deploy)
- [154: How do you form and test a hypothesis while debugging?](#154-how-do-you-form-and-test-a-hypothesis-while-debugging)
- [155: How do you debug a performance regression?](#155-how-do-you-debug-a-performance-regression)
- [156: How do you decide between adding logs and using a debugger?](#156-how-do-you-decide-between-adding-logs-and-using-a-debugger)
- [157: What makes a log line useful?](#157-what-makes-a-log-line-useful)
- [158: How do you debug a problem you cannot reproduce locally?](#158-how-do-you-debug-a-problem-you-cannot-reproduce-locally)
- [159: How do you write a postmortem for a production bug?](#159-how-do-you-write-a-postmortem-for-a-production-bug)
- [160: How do you debug a bug that seems to be in a third-party library?](#160-how-do-you-debug-a-bug-that-seems-to-be-in-a-third-party-library)
- [161: How do you debug problems caused by dependency upgrades?](#161-how-do-you-debug-problems-caused-by-dependency-upgrades)
- [162: How do you debug environment variable and config problems?](#162-how-do-you-debug-environment-variable-and-config-problems)
- [163: How do you debug a Node.js app running in Docker or Kubernetes with the inspector?](#163-how-do-you-debug-a-nodejs-app-running-in-docker-or-kubernetes-with-the-inspector)
- [164: How do you attach a debugger to a running Node.js process that was not started with --inspect?](#164-how-do-you-attach-a-debugger-to-a-running-nodejs-process-that-was-not-started-with---inspect)
- [165: How do you measure event loop lag?](#165-how-do-you-measure-event-loop-lag)
- [166: What is event loop utilization (ELU)?](#166-what-is-event-loop-utilization-elu)
- [167: How do you find what is blocking the event loop?](#167-how-do-you-find-what-is-blocking-the-event-loop)
- [168: How do you take a CPU profile in Node.js?](#168-how-do-you-take-a-cpu-profile-in-nodejs)
- [169: How do you read a flame graph?](#169-how-do-you-read-a-flame-graph)
- [170: How do you take a heap snapshot in Node.js?](#170-how-do-you-take-a-heap-snapshot-in-nodejs)
- [171: How do you find a memory leak in Node.js?](#171-how-do-you-find-a-memory-leak-in-nodejs)
- [172: What are common causes of memory leaks in Node.js?](#172-what-are-common-causes-of-memory-leaks-in-nodejs)
- [173: What is a diagnostic report in Node.js?](#173-what-is-a-diagnostic-report-in-nodejs)
- [174: How do you find where an unhandled promise rejection came from?](#174-how-do-you-find-where-an-unhandled-promise-rejection-came-from)
- [175: How do you debug a Node.js process that exits without an error?](#175-how-do-you-debug-a-nodejs-process-that-exits-without-an-error)
- [176: How do you debug a Node.js process that never exits?](#176-how-do-you-debug-a-nodejs-process-that-never-exits)
- [177: How does AsyncLocalStorage help with request logs?](#177-how-does-asynclocalstorage-help-with-request-logs)
- [178: How do you debug libuv thread pool saturation?](#178-how-do-you-debug-libuv-thread-pool-saturation)
- [179: What do the fields of process.memoryUsage() mean?](#179-what-do-the-fields-of-processmemoryusage-mean)
- [180: How do you debug ESM and CommonJS errors in Node.js?](#180-how-do-you-debug-esm-and-commonjs-errors-in-nodejs)
- [181: How do you debug a MaxListenersExceededWarning?](#181-how-do-you-debug-a-maxlistenersexceededwarning)
- [182: How do you debug fetch errors in Node.js?](#182-how-do-you-debug-fetch-errors-in-nodejs)
- [183: How do you debug middleware order problems in Express?](#183-how-do-you-debug-middleware-order-problems-in-express)
- [184: How do you log every request and response in Express safely?](#184-how-do-you-log-every-request-and-response-in-express-safely)
- [185: How do you debug a "trust proxy" problem in Express?](#185-how-do-you-debug-a-trust-proxy-problem-in-express)
- [186: What route path changes in Express 5 can break routes?](#186-what-route-path-changes-in-express-5-can-break-routes)
- [187: How do you debug encapsulation problems with Fastify plugins?](#187-how-do-you-debug-encapsulation-problems-with-fastify-plugins)
- [188: What does the "Reply was already sent" error mean in Fastify?](#188-what-does-the-reply-was-already-sent-error-mean-in-fastify)
- [189: How do you debug schema validation errors in Fastify?](#189-how-do-you-debug-schema-validation-errors-in-fastify)
- [190: Why are some fields missing from a Fastify response?](#190-why-are-some-fields-missing-from-a-fastify-response)
- [191: How do you debug a plugin timeout in Fastify?](#191-how-do-you-debug-a-plugin-timeout-in-fastify)
- [192: How do you debug circular dependencies in NestJS?](#192-how-do-you-debug-circular-dependencies-in-nestjs)
- [193: In what order do middleware, guards, interceptors and pipes run in NestJS?](#193-in-what-order-do-middleware-guards-interceptors-and-pipes-run-in-nestjs)
- [194: How do you debug exceptions in NestJS with exception filters?](#194-how-do-you-debug-exceptions-in-nestjs-with-exception-filters)
- [195: How do you debug ValidationPipe problems in NestJS?](#195-how-do-you-debug-validationpipe-problems-in-nestjs)
- [196: How do you debug duplicate records caused by retries in a REST API?](#196-how-do-you-debug-duplicate-records-caused-by-retries-in-a-rest-api)
- [197: How do you debug HTTP caching problems?](#197-how-do-you-debug-http-caching-problems)
- [198: How do you debug timeouts between a client and your API?](#198-how-do-you-debug-timeouts-between-a-client-and-your-api)
- [199: How do you debug GraphQL resolver errors?](#199-how-do-you-debug-graphql-resolver-errors)
- [200: How do you use DataLoader to fix N+1 and check that it worked?](#200-how-do-you-use-dataloader-to-fix-n1-and-check-that-it-worked)
- [201: What does "Cannot return null for non-nullable field" mean in GraphQL?](#201-what-does-cannot-return-null-for-non-nullable-field-mean-in-graphql)
- [202: How do you debug webhooks you receive?](#202-how-do-you-debug-webhooks-you-receive)
- [203: How do you read an EXPLAIN ANALYZE plan in PostgreSQL?](#203-how-do-you-read-an-explain-analyze-plan-in-postgresql)
- [204: How do you find slow queries in PostgreSQL with pg_stat_statements?](#204-how-do-you-find-slow-queries-in-postgresql-with-pg_stat_statements)
- [205: How do you see running queries and locks in PostgreSQL?](#205-how-do-you-see-running-queries-and-locks-in-postgresql)
- [206: How do you debug a deadlock in SQL?](#206-how-do-you-debug-a-deadlock-in-sql)
- [207: How do you debug "too many connections" errors?](#207-how-do-you-debug-too-many-connections-errors)
- [208: What does "idle in transaction" mean and why is it a problem?](#208-what-does-idle-in-transaction-mean-and-why-is-it-a-problem)
- [209: How do you debug a query that is fast in dev but slow in production?](#209-how-do-you-debug-a-query-that-is-fast-in-dev-but-slow-in-production)
- [210: How do you debug slow queries and locks in MySQL?](#210-how-do-you-debug-slow-queries-and-locks-in-mysql)
- [211: What do Prisma errors P1001 and P2024 mean?](#211-what-do-prisma-errors-p1001-and-p2024-mean)
- [212: How do you debug Prisma connection problems in serverless?](#212-how-do-you-debug-prisma-connection-problems-in-serverless)
- [213: How do you debug Prisma migration drift?](#213-how-do-you-debug-prisma-migration-drift)
- [214: How do you debug a Mongoose ValidationError?](#214-how-do-you-debug-a-mongoose-validationerror)
- [215: Why does Mongoose populate return null?](#215-why-does-mongoose-populate-return-null)
- [216: Why does Mongoose middleware (hooks) not run?](#216-why-does-mongoose-middleware-hooks-not-run)
- [217: How do you use the MongoDB profiler?](#217-how-do-you-use-the-mongodb-profiler)
- [218: How do you find long-running operations in MongoDB?](#218-how-do-you-find-long-running-operations-in-mongodb)
- [219: How do you debug a MongoDB duplicate key error E11000?](#219-how-do-you-debug-a-mongodb-duplicate-key-error-e11000)
- [220: How do you debug stale reads in MongoDB?](#220-how-do-you-debug-stale-reads-in-mongodb)
- [221: How do you debug DynamoDB throttling?](#221-how-do-you-debug-dynamodb-throttling)
- [222: How do you debug a DynamoDB TransactionCanceledException?](#222-how-do-you-debug-a-dynamodb-transactioncanceledexception)
- [223: How do you see how much capacity a DynamoDB request uses?](#223-how-do-you-see-how-much-capacity-a-dynamodb-request-uses)
- [224: How do you debug Redis latency?](#224-how-do-you-debug-redis-latency)
- [225: How do you find big keys and memory use in Redis?](#225-how-do-you-find-big-keys-and-memory-use-in-redis)
- [226: How do you debug Redis OOM errors?](#226-how-do-you-debug-redis-oom-errors)
- [227: How do you check consumer group lag and partition assignment in Kafka?](#227-how-do-you-check-consumer-group-lag-and-partition-assignment-in-kafka)
- [228: How do you debug frequent consumer rebalances in Kafka?](#228-how-do-you-debug-frequent-consumer-rebalances-in-kafka)
- [229: How do you debug message ordering problems in Kafka?](#229-how-do-you-debug-message-ordering-problems-in-kafka)
- [230: How do you debug duplicate message processing in Kafka?](#230-how-do-you-debug-duplicate-message-processing-in-kafka)
- [231: How do you debug a Kafka producer that fails to send?](#231-how-do-you-debug-a-kafka-producer-that-fails-to-send)
- [232: How do you replay messages in Kafka for debugging?](#232-how-do-you-replay-messages-in-kafka-for-debugging)
- [233: How do you debug messages piling up as unacked in RabbitMQ?](#233-how-do-you-debug-messages-piling-up-as-unacked-in-rabbitmq)
- [234: How does prefetch affect RabbitMQ consumers?](#234-how-does-prefetch-affect-rabbitmq-consumers)
- [235: How do you debug PRECONDITION_FAILED errors in RabbitMQ?](#235-how-do-you-debug-precondition_failed-errors-in-rabbitmq)
- [236: How do you debug messages that disappear in RabbitMQ?](#236-how-do-you-debug-messages-that-disappear-in-rabbitmq)
- [237: How do you debug a blocked publisher in RabbitMQ?](#237-how-do-you-debug-a-blocked-publisher-in-rabbitmq)
- [238: How do you debug BullMQ jobs stuck in waiting?](#238-how-do-you-debug-bullmq-jobs-stuck-in-waiting)
- [239: Why does BullMQ require maxRetriesPerRequest: null?](#239-why-does-bullmq-require-maxretriesperrequest-null)
- [240: How do you add logs and progress to BullMQ jobs?](#240-how-do-you-add-logs-and-progress-to-bullmq-jobs)
- [241: How do you add OpenTelemetry tracing to a Node.js service?](#241-how-do-you-add-opentelemetry-tracing-to-a-nodejs-service)
- [242: How do you connect logs with traces?](#242-how-do-you-connect-logs-with-traces)
- [243: How do you find which service is slow in a request chain?](#243-how-do-you-find-which-service-is-slow-in-a-request-chain)
- [244: How do you debug a retry storm?](#244-how-do-you-debug-a-retry-storm)
- [245: How do you debug timeouts that do not fit together across services?](#245-how-do-you-debug-timeouts-that-do-not-fit-together-across-services)
- [246: How do you debug DNS and service discovery problems between services?](#246-how-do-you-debug-dns-and-service-discovery-problems-between-services)
- [247: Why should you look at p95 and p99 latency instead of averages?](#247-why-should-you-look-at-p95-and-p99-latency-instead-of-averages)
- [248: How can trace sampling hide bugs?](#248-how-can-trace-sampling-hide-bugs)
- [249: How do you debug a problem that affects only one instance or pod?](#249-how-do-you-debug-a-problem-that-affects-only-one-instance-or-pod)
- [250: How do you trace a request through a message queue?](#250-how-do-you-trace-a-request-through-a-message-queue)
- [251: How do you debug a circuit breaker that stays open?](#251-how-do-you-debug-a-circuit-breaker-that-stays-open)
- [252: How do you debug data that does not match across services in an eventually consistent system?](#252-how-do-you-debug-data-that-does-not-match-across-services-in-an-eventually-consistent-system)
- [253: How do you debug a container that has no shell, such as a distroless image?](#253-how-do-you-debug-a-container-that-has-no-shell-such-as-a-distroless-image)
- [254: Why does a Node.js container take a long time to stop or lose requests on deploy?](#254-why-does-a-nodejs-container-take-a-long-time-to-stop-or-lose-requests-on-deploy)
- [255: How do you debug a Node.js app that gets OOM killed in a container?](#255-how-do-you-debug-a-nodejs-app-that-gets-oom-killed-in-a-container)
- [256: How do you use Kubernetes events for debugging?](#256-how-do-you-use-kubernetes-events-for-debugging)
- [257: How do you debug a Kubernetes Service that does not send traffic to pods?](#257-how-do-you-debug-a-kubernetes-service-that-does-not-send-traffic-to-pods)
- [258: How do CPU limits cause slow responses in Kubernetes?](#258-how-do-cpu-limits-cause-slow-responses-in-kubernetes)
- [259: How do you check and undo a bad rollout in Kubernetes?](#259-how-do-you-check-and-undo-a-bad-rollout-in-kubernetes)
- [260: What causes a 504 Gateway Timeout from Nginx and how do you fix it?](#260-what-causes-a-504-gateway-timeout-from-nginx-and-how-do-you-fix-it)
- [261: How does a trailing slash in proxy_pass change the request path in Nginx?](#261-how-does-a-trailing-slash-in-proxy_pass-change-the-request-path-in-nginx)
- [262: How do you log upstream timing in Nginx?](#262-how-do-you-log-upstream-timing-in-nginx)
- [263: Why do you get random 502 errors behind a load balancer with Node.js?](#263-why-do-you-get-random-502-errors-behind-a-load-balancer-with-nodejs)
- [264: How do you read the Lambda REPORT log line?](#264-how-do-you-read-the-lambda-report-log-line)
- [265: How do you debug Lambda timeouts?](#265-how-do-you-debug-lambda-timeouts)
- [266: How do you get a shell in a running ECS task?](#266-how-do-you-get-a-shell-in-a-running-ecs-task)
- [267: How do you debug an AWS SDK call that fails?](#267-how-do-you-debug-an-aws-sdk-call-that-fails)
- [268: How do you see live logs for Azure App Service and Container Apps?](#268-how-do-you-see-live-logs-for-azure-app-service-and-container-apps)
- [269: How do you debug a Cloud Run service on GCP?](#269-how-do-you-debug-a-cloud-run-service-on-gcp)
- [270: How do you find drift between Terraform state and real infrastructure?](#270-how-do-you-find-drift-between-terraform-state-and-real-infrastructure)
- [271: How do you inspect Terraform state and expressions?](#271-how-do-you-inspect-terraform-state-and-expressions)
- [272: How do you debug "resource already exists" errors in Terraform?](#272-how-do-you-debug-resource-already-exists-errors-in-terraform)
- [273: Why are secrets empty in GitHub Actions for pull requests from forks?](#273-why-are-secrets-empty-in-github-actions-for-pull-requests-from-forks)
- [274: How do you debug "Resource not accessible by integration" in GitHub Actions?](#274-how-do-you-debug-resource-not-accessible-by-integration-in-github-actions)
- [275: How do you debug cache and artifact problems in GitHub Actions?](#275-how-do-you-debug-cache-and-artifact-problems-in-github-actions)
- [276: How do you debug networking between containers in Docker Compose?](#276-how-do-you-debug-networking-between-containers-in-docker-compose)
- [277: How do you debug a CORS preflight failure?](#277-how-do-you-debug-a-cors-preflight-failure)
- [278: How do you debug a CSRF token mismatch?](#278-how-do-you-debug-a-csrf-token-mismatch)
- [279: Why does a rate limiter block many users at once?](#279-why-does-a-rate-limiter-block-many-users-at-once)
- [280: How do you debug a JWT rejected because of audience or issuer?](#280-how-do-you-debug-a-jwt-rejected-because-of-audience-or-issuer)
- [281: How do you debug JWKS and key rotation errors?](#281-how-do-you-debug-jwks-and-key-rotation-errors)
- [282: Why is the Authorization header missing on the server?](#282-why-is-the-authorization-header-missing-on-the-server)
- [283: How do you debug random logouts with refresh tokens?](#283-how-do-you-debug-random-logouts-with-refresh-tokens)
- [284: How do you debug common OAuth errors like redirect_uri_mismatch and invalid_grant?](#284-how-do-you-debug-common-oauth-errors-like-redirect_uri_mismatch-and-invalid_grant)
- [285: Why does TLS work in the browser but fail in Node.js?](#285-why-does-tls-work-in-the-browser-but-fail-in-nodejs)
- [286: How do you make Node.js trust a private or company CA?](#286-how-do-you-make-nodejs-trust-a-private-or-company-ca)
- [287: What does ERR_TLS_CERT_ALTNAME_INVALID mean?](#287-what-does-err_tls_cert_altname_invalid-mean)
- [288: How do you debug TLS errors when connecting to a database?](#288-how-do-you-debug-tls-errors-when-connecting-to-a-database)
- [289: How do you debug mutual TLS (mTLS) errors?](#289-how-do-you-debug-mutual-tls-mtls-errors)
- [290: How do you check that a certificate and private key match?](#290-how-do-you-check-that-a-certificate-and-private-key-match)
- [291: Why can logging an HTTP client error leak a token?](#291-why-can-logging-an-http-client-error-leak-a-token)
- [292: How do you keep personal data out of error tracking tools like Sentry?](#292-how-do-you-keep-personal-data-out-of-error-tracking-tools-like-sentry)
- [293: How do you log request and response bodies safely when you need them?](#293-how-do-you-log-request-and-response-bodies-safely-when-you-need-them)
- [294: How do you turn on debug logs for one user or one request without flooding production?](#294-how-do-you-turn-on-debug-logs-for-one-user-or-one-request-without-flooding-production)
- [295: How do you run queries against a production database safely while debugging?](#295-how-do-you-run-queries-against-a-production-database-safely-while-debugging)
- [296: How do you share logs in a ticket or chat safely?](#296-how-do-you-share-logs-in-a-ticket-or-chat-safely)
- [297: Who should be able to read production logs, and for how long should logs be kept?](#297-who-should-be-able-to-read-production-logs-and-for-how-long-should-logs-be-kept)
- [298: How can secrets leak in CI/CD logs even when they are masked?](#298-how-can-secrets-leak-in-cicd-logs-even-when-they-are-masked)
- [299: How do you debug with production data without exposing personal data?](#299-how-do-you-debug-with-production-data-without-exposing-personal-data)
- [300: How do you change the log level of a running service without restarting it?](#300-how-do-you-change-the-log-level-of-a-running-service-without-restarting-it)

### Advanced Questions (301-450)

- [301: After a deploy, p99 latency doubled but there are no errors. How do you investigate?](#301-after-a-deploy-p99-latency-doubled-but-there-are-no-errors-how-do-you-investigate)
- [302: Errors spike at the same minute every hour. What do you check?](#302-errors-spike-at-the-same-minute-every-hour-what-do-you-check)
- [303: A service works fine at normal traffic but falls over at peak. How do you debug it?](#303-a-service-works-fine-at-normal-traffic-but-falls-over-at-peak-how-do-you-debug-it)
- [304: Adding logs makes a bug disappear. How do you debug it?](#304-adding-logs-makes-a-bug-disappear-how-do-you-debug-it)
- [305: How do race conditions happen in single-threaded Node.js, and how do you debug them?](#305-how-do-race-conditions-happen-in-single-threaded-nodejs-and-how-do-you-debug-them)
- [306: You find corrupted data that was written days ago. How do you trace the cause?](#306-you-find-corrupted-data-that-was-written-days-ago-how-do-you-trace-the-cause)
- [307: During an incident, how do you balance fixing the cause with stopping the impact?](#307-during-an-incident-how-do-you-balance-fixing-the-cause-with-stopping-the-impact)
- [308: How do you compare good and bad requests to find the cause?](#308-how-do-you-compare-good-and-bad-requests-to-find-the-cause)
- [309: When do you stop investigating and accept a workaround?](#309-when-do-you-stop-investigating-and-accept-a-workaround)
- [310: A problem appears only after days of uptime. How do you debug it?](#310-a-problem-appears-only-after-days-of-uptime-how-do-you-debug-it)
- [311: A third-party API changed its behavior without notice. How do you prove it and protect your service?](#311-a-third-party-api-changed-its-behavior-without-notice-how-do-you-prove-it-and-protect-your-service)
- [312: How do you design a back-end service so it is easy to debug?](#312-how-do-you-design-a-back-end-service-so-it-is-easy-to-debug)
- [313: How does garbage collection affect latency in Node.js, and how do you see it?](#313-how-does-garbage-collection-affect-latency-in-nodejs-and-how-do-you-see-it)
- [314: In a heap snapshot, what is the difference between shallow size and retained size?](#314-in-a-heap-snapshot-what-is-the-difference-between-shallow-size-and-retained-size)
- [315: How do closures cause memory leaks, and how do they show in a heap snapshot?](#315-how-do-closures-cause-memory-leaks-and-how-do-they-show-in-a-heap-snapshot)
- [316: RSS keeps growing but the JS heap is flat. How do you debug it?](#316-rss-keeps-growing-but-the-js-heap-is-flat-how-do-you-debug-it)
- [317: How do you debug a Node.js crash in native code (exit code 139)?](#317-how-do-you-debug-a-nodejs-crash-in-native-code-exit-code-139)
- [318: How do you profile a Node.js service in production safely?](#318-how-do-you-profile-a-nodejs-service-in-production-safely)
- [319: How do you take a CPU profile from code without restarting the process?](#319-how-do-you-take-a-cpu-profile-from-code-without-restarting-the-process)
- [320: What is microtask starvation and how do you debug it?](#320-what-is-microtask-starvation-and-how-do-you-debug-it)
- [321: How do you find and fix a ReDoS problem?](#321-how-do-you-find-and-fix-a-redos-problem)
- [322: Why does AsyncLocalStorage sometimes lose the request context?](#322-why-does-asynclocalstorage-sometimes-lose-the-request-context)
- [323: How can diagnostics_channel help with debugging?](#323-how-can-diagnostics_channel-help-with-debugging)
- [324: How do you debug problems with worker threads?](#324-how-do-you-debug-problems-with-worker-threads)
- [325: Why does an unhandled 'error' event crash a Node.js process?](#325-why-does-an-unhandled-error-event-crash-a-nodejs-process)
- [326: How do you debug stream problems like hanging uploads or memory growth?](#326-how-do-you-debug-stream-problems-like-hanging-uploads-or-memory-growth)
- [327: How do you debug EMFILE "too many open files" errors?](#327-how-do-you-debug-emfile-too-many-open-files-errors)
- [328: How do you debug "socket hang up" errors on outgoing requests?](#328-how-do-you-debug-socket-hang-up-errors-on-outgoing-requests)
- [329: How do you debug a request that hangs forever because a promise never resolves?](#329-how-do-you-debug-a-request-that-hangs-forever-because-a-promise-never-resolves)
- [330: How do you find which code allocates the most memory?](#330-how-do-you-find-which-code-allocates-the-most-memory)
- [331: Code got slower after upgrading Node.js. How do you debug it?](#331-code-got-slower-after-upgrading-nodejs-how-do-you-debug-it)
- [332: The process crashes at startup in production and logs show nothing. What do you do?](#332-the-process-crashes-at-startup-in-production-and-logs-show-nothing-what-do-you-do)
- [333: How do you debug a memory leak that comes from a framework-level pattern in Express or Fastify?](#333-how-do-you-debug-a-memory-leak-that-comes-from-a-framework-level-pattern-in-express-or-fastify)
- [334: In what order do Fastify hooks run, and what are the common mistakes?](#334-in-what-order-do-fastify-hooks-run-and-what-are-the-common-mistakes)
- [335: How can request-scoped providers in NestJS cause performance problems?](#335-how-can-request-scoped-providers-in-nestjs-cause-performance-problems)
- [336: How do you debug slow NestJS startup?](#336-how-do-you-debug-slow-nestjs-startup)
- [337: How do you debug "There is no matching message handler" in NestJS microservices?](#337-how-do-you-debug-there-is-no-matching-message-handler-in-nestjs-microservices)
- [338: Why do NestJS shutdown hooks not run?](#338-why-do-nestjs-shutdown-hooks-not-run)
- [339: How do you debug a GraphQL API that gets slow because of expensive queries?](#339-how-do-you-debug-a-graphql-api-that-gets-slow-because-of-expensive-queries)
- [340: Why do GraphQL subscriptions or WebSocket messages not reach all clients?](#340-why-do-graphql-subscriptions-or-websocket-messages-not-reach-all-clients)
- [341: How do you debug errors in a federated GraphQL setup?](#341-how-do-you-debug-errors-in-a-federated-graphql-setup)
- [342: How do you debug 431 Request Header Fields Too Large?](#342-how-do-you-debug-431-request-header-fields-too-large)
- [343: Why do Server-Sent Events or streamed responses arrive all at once behind Nginx?](#343-why-do-server-sent-events-or-streamed-responses-arrive-all-at-once-behind-nginx)
- [344: How do you debug WebSocket connections that drop after some time?](#344-how-do-you-debug-websocket-connections-that-drop-after-some-time)
- [345: How do you debug compression problems, like broken responses or a wrong Content-Length?](#345-how-do-you-debug-compression-problems-like-broken-responses-or-a-wrong-content-length)
- [346: How do you debug an endpoint that returns a very large JSON response slowly?](#346-how-do-you-debug-an-endpoint-that-returns-a-very-large-json-response-slowly)
- [347: How do you debug lost updates when two clients edit the same resource?](#347-how-do-you-debug-lost-updates-when-two-clients-edit-the-same-resource)
- [348: Which built-in Node.js HTTP server timeouts can cut off requests?](#348-which-built-in-nodejs-http-server-timeouts-can-cut-off-requests)
- [349: How do you safely replay production traffic to reproduce a bug?](#349-how-do-you-safely-replay-production-traffic-to-reproduce-a-bug)
- [350: A schema migration in PostgreSQL caused an outage. What happened and how do you prevent it?](#350-a-schema-migration-in-postgresql-caused-an-outage-what-happened-and-how-do-you-prevent-it)
- [351: How do you debug lock contention on hot rows in PostgreSQL?](#351-how-do-you-debug-lock-contention-on-hot-rows-in-postgresql)
- [352: How do you debug table bloat and autovacuum problems in PostgreSQL?](#352-how-do-you-debug-table-bloat-and-autovacuum-problems-in-postgresql)
- [353: How do you debug serialization failures in PostgreSQL?](#353-how-do-you-debug-serialization-failures-in-postgresql)
- [354: Why does a prepared query become slow after a few runs in PostgreSQL?](#354-why-does-a-prepared-query-become-slow-after-a-few-runs-in-postgresql)
- [355: How do you debug replication lag and read-after-write bugs with PostgreSQL read replicas?](#355-how-do-you-debug-replication-lag-and-read-after-write-bugs-with-postgresql-read-replicas)
- [356: How do you use auto_explain to catch bad plans in production?](#356-how-do-you-use-auto_explain-to-catch-bad-plans-in-production)
- [357: What breaks when you put PgBouncer in transaction pooling mode?](#357-what-breaks-when-you-put-pgbouncer-in-transaction-pooling-mode)
- [358: How do you debug slow queries generated by an ORM?](#358-how-do-you-debug-slow-queries-generated-by-an-orm)
- [359: How do you debug Prisma interactive transaction timeouts?](#359-how-do-you-debug-prisma-interactive-transaction-timeouts)
- [360: How do you trace Prisma queries with OpenTelemetry?](#360-how-do-you-trace-prisma-queries-with-opentelemetry)
- [361: How do you debug a slow MongoDB aggregation pipeline?](#361-how-do-you-debug-a-slow-mongodb-aggregation-pipeline)
- [362: MongoDB picks the wrong index for a query. How do you debug it?](#362-mongodb-picks-the-wrong-index-for-a-query-how-do-you-debug-it)
- [363: How do you debug write conflicts in MongoDB transactions?](#363-how-do-you-debug-write-conflicts-in-mongodb-transactions)
- [364: How do you debug MongoDB connection pool and server selection errors in Node.js?](#364-how-do-you-debug-mongodb-connection-pool-and-server-selection-errors-in-nodejs)
- [365: How do you debug memory and CPU problems with Mongoose on large result sets?](#365-how-do-you-debug-memory-and-cpu-problems-with-mongoose-on-large-result-sets)
- [366: How do you debug hot partitions in DynamoDB in depth?](#366-how-do-you-debug-hot-partitions-in-dynamodb-in-depth)
- [367: Why does a DynamoDB GSI return old data right after a write?](#367-why-does-a-dynamodb-gsi-return-old-data-right-after-a-write)
- [368: How do you debug a DynamoDB Streams consumer (Lambda) that falls behind?](#368-how-do-you-debug-a-dynamodb-streams-consumer-lambda-that-falls-behind)
- [369: How do you debug Redis Cluster errors like MOVED and CROSSSLOT?](#369-how-do-you-debug-redis-cluster-errors-like-moved-and-crossslot)
- [370: Why can writes be lost after a Redis failover?](#370-why-can-writes-be-lost-after-a-redis-failover)
- [371: How do you confirm and fix a cache stampede in production?](#371-how-do-you-confirm-and-fix-a-cache-stampede-in-production)
- [372: How do you debug a Redis-based distributed lock that lets two workers in?](#372-how-do-you-debug-a-redis-based-distributed-lock-that-lets-two-workers-in)
- [373: Redis returns OOM errors even though an eviction policy is set. Why?](#373-redis-returns-oom-errors-even-though-an-eviction-policy-is-set-why)
- [374: A Kafka consumer is stuck on one partition while others are fine. How do you debug it?](#374-a-kafka-consumer-is-stuck-on-one-partition-while-others-are-fine-how-do-you-debug-it)
- [375: How do you debug Kafka transactions and "exactly-once" problems?](#375-how-do-you-debug-kafka-transactions-and-exactly-once-problems)
- [376: How do you debug under-replicated partitions in Kafka?](#376-how-do-you-debug-under-replicated-partitions-in-kafka)
- [377: A new consumer group did not process old messages. Why?](#377-a-new-consumer-group-did-not-process-old-messages-why)
- [378: Messages were deleted before consumers processed them. How do you debug it?](#378-messages-were-deleted-before-consumers-processed-them-how-do-you-debug-it)
- [379: How do you debug a message that is redelivered over and over in RabbitMQ?](#379-how-do-you-debug-a-message-that-is-redelivered-over-and-over-in-rabbitmq)
- [380: How do you debug RabbitMQ cluster problems like network partitions?](#380-how-do-you-debug-rabbitmq-cluster-problems-like-network-partitions)
- [381: How do you debug too many connections or channels in RabbitMQ?](#381-how-do-you-debug-too-many-connections-or-channels-in-rabbitmq)
- [382: What does "delivery acknowledgement timed out" mean in RabbitMQ?](#382-what-does-delivery-acknowledgement-timed-out-mean-in-rabbitmq)
- [383: Why do BullMQ jobs keep stalling, and how do you fix it?](#383-why-do-bullmq-jobs-keep-stalling-and-how-do-you-fix-it)
- [384: Why is a BullMQ job processed twice, and how do you prevent it?](#384-why-is-a-bullmq-job-processed-twice-and-how-do-you-prevent-it)
- [385: BullMQ is using more and more Redis memory. How do you debug it?](#385-bullmq-is-using-more-and-more-redis-memory-how-do-you-debug-it)
- [386: How do you stop BullMQ from losing or repeating jobs during deploys?](#386-how-do-you-stop-bullmq-from-losing-or-repeating-jobs-during-deploys)
- [387: An order was saved but its event was never published. How do you debug and fix this?](#387-an-order-was-saved-but-its-event-was-never-published-how-do-you-debug-and-fix-this)
- [388: Why does a request that calls many services in parallel have high latency even when each service is usually fast?](#388-why-does-a-request-that-calls-many-services-in-parallel-have-high-latency-even-when-each-service-is-usually-fast)
- [389: After an outage, the service fails again as soon as it comes back. What is happening?](#389-after-an-outage-the-service-fails-again-as-soon-as-it-comes-back-what-is-happening)
- [390: What is a metastable failure and how do you recognize it?](#390-what-is-a-metastable-failure-and-how-do-you-recognize-it)
- [391: How can metrics labels break your monitoring, and how do you debug it?](#391-how-can-metrics-labels-break-your-monitoring-and-how-do-you-debug-it)
- [392: What are exemplars and how do they help debugging?](#392-what-are-exemplars-and-how-do-they-help-debugging)
- [393: Spans are missing or traces are broken into pieces. How do you debug it?](#393-spans-are-missing-or-traces-are-broken-into-pieces-how-do-you-debug-it)
- [394: In a trace, a child span starts before its parent. What does it mean?](#394-in-a-trace-a-child-span-starts-before-its-parent-what-does-it-mean)
- [395: How do you use Envoy or service mesh access logs to debug 503 errors?](#395-how-do-you-use-envoy-or-service-mesh-access-logs-to-debug-503-errors)
- [396: How do you debug gRPC errors between Node.js services?](#396-how-do-you-debug-grpc-errors-between-nodejs-services)
- [397: A producer changed its message format and consumers started failing. How do you debug and prevent it?](#397-a-producer-changed-its-message-format-and-consumers-started-failing-how-do-you-debug-and-prevent-it)
- [398: Users in one region see errors while others do not. How do you debug it?](#398-users-in-one-region-see-errors-while-others-do-not-how-do-you-debug-it)
- [399: How do you write alerts that help debugging instead of creating noise?](#399-how-do-you-write-alerts-that-help-debugging-instead-of-creating-noise)
- [400: What are wide events and why do they help with debugging?](#400-what-are-wide-events-and-why-do-they-help-with-debugging)
- [401: Logs or traces are missing or arrive late. How do you debug the observability pipeline itself?](#401-logs-or-traces-are-missing-or-arrive-late-how-do-you-debug-the-observability-pipeline-itself)
- [402: How do you tell an OOM kill from an eviction in Kubernetes?](#402-how-do-you-tell-an-oom-kill-from-an-eviction-in-kubernetes)
- [403: DNS lookups in Kubernetes are sometimes slow or time out. How do you debug it?](#403-dns-lookups-in-kubernetes-are-sometimes-slow-or-time-out-how-do-you-debug-it)
- [404: Pods cannot reach an external service, or calls fail only under load. What do you check?](#404-pods-cannot-reach-an-external-service-or-calls-fail-only-under-load-what-do-you-check)
- [405: Why do you get a few connection errors on every Kubernetes deploy, and how do you fix it?](#405-why-do-you-get-a-few-connection-errors-on-every-kubernetes-deploy-and-how-do-you-fix-it)
- [406: The Horizontal Pod Autoscaler does not scale. How do you debug it?](#406-the-horizontal-pod-autoscaler-does-not-scale-how-do-you-debug-it)
- [407: How do you debug a problem on the Kubernetes node itself?](#407-how-do-you-debug-a-problem-on-the-kubernetes-node-itself)
- [408: What does CreateContainerConfigError mean in Kubernetes?](#408-what-does-createcontainerconfigerror-mean-in-kubernetes)
- [409: A container fails with "exec format error". What is wrong?](#409-a-container-fails-with-exec-format-error-what-is-wrong)
- [410: How do you check whether a secret leaked into a Docker image?](#410-how-do-you-check-whether-a-secret-leaked-into-a-docker-image)
- [411: How do you fix "upstream sent too big header while reading response header from upstream" in Nginx?](#411-how-do-you-fix-upstream-sent-too-big-header-while-reading-response-header-from-upstream-in-nginx)
- [412: Nginx serves the wrong site or the wrong certificate. How do you debug it?](#412-nginx-serves-the-wrong-site-or-the-wrong-certificate-how-do-you-debug-it)
- [413: How do you get Nginx debug logs for just one client?](#413-how-do-you-get-nginx-debug-logs-for-just-one-client)
- [414: How do you tell if 5xx errors come from an AWS load balancer or from your app?](#414-how-do-you-tell-if-5xx-errors-come-from-an-aws-load-balancer-or-from-your-app)
- [415: An AWS IAM policy looks correct but access is still denied. What else do you check?](#415-an-aws-iam-policy-looks-correct-but-access-is-still-denied-what-else-do-you-check)
- [416: How do you debug network connectivity inside an AWS VPC?](#416-how-do-you-debug-network-connectivity-inside-an-aws-vpc)
- [417: How do you debug workload identity failures in Kubernetes (IRSA, GKE Workload Identity, Azure Workload Identity)?](#417-how-do-you-debug-workload-identity-failures-in-kubernetes-irsa-gke-workload-identity-azure-workload-identity)
- [418: Terraform plan always shows a change even after apply. How do you debug it?](#418-terraform-plan-always-shows-a-change-even-after-apply-how-do-you-debug-it)
- [419: How do you debug a Terraform dependency cycle or wrong ordering?](#419-how-do-you-debug-a-terraform-dependency-cycle-or-wrong-ordering)
- [420: Why is Terraform state sensitive, and how do you debug without exposing secrets in it?](#420-why-is-terraform-state-sensitive-and-how-do-you-debug-without-exposing-secrets-in-it)
- [421: How do you debug a failed OIDC login from GitHub Actions to a cloud provider?](#421-how-do-you-debug-a-failed-oidc-login-from-github-actions-to-a-cloud-provider)
- [422: How do JWT algorithm confusion bugs happen, and how do you check for them?](#422-how-do-jwt-algorithm-confusion-bugs-happen-and-how-do-you-check-for-them)
- [423: Login works on one instance but fails on another. What do you check?](#423-login-works-on-one-instance-but-fails-on-another-what-do-you-check)
- [424: You suspect a security incident while debugging. What do you do differently?](#424-you-suspect-a-security-incident-while-debugging-what-do-you-do-differently)
- [425: How do you debug a suspected broken access control (IDOR) bug?](#425-how-do-you-debug-a-suspected-broken-access-control-idor-bug)
- [426: How do you debug TLS handshake failures?](#426-how-do-you-debug-tls-handshake-failures)
- [427: Certificate checks fail only on some machines or old images. Why?](#427-certificate-checks-fail-only-on-some-machines-or-old-images-why)
- [428: How do you debug a certificate that did not renew automatically?](#428-how-do-you-debug-a-certificate-that-did-not-renew-automatically)
- [429: Why do you get an endless redirect loop after enabling HTTPS behind a load balancer?](#429-why-do-you-get-an-endless-redirect-loop-after-enabling-https-behind-a-load-balancer)
- [430: How does SNI cause wrong certificate errors?](#430-how-does-sni-cause-wrong-certificate-errors)
- [431: Several unrelated auth features started failing at the same time. Could the clock be the cause?](#431-several-unrelated-auth-features-started-failing-at-the-same-time-could-the-clock-be-the-cause)
- [432: How do you debug a SignatureDoesNotMatch error for signed requests or URLs?](#432-how-do-you-debug-a-signaturedoesnotmatch-error-for-signed-requests-or-urls)
- [433: A secret rotation caused an outage. How do you debug it and avoid it next time?](#433-a-secret-rotation-caused-an-outage-how-do-you-debug-it-and-avoid-it-next-time)
- [434: Token validation makes every request slow. How do you debug it?](#434-token-validation-makes-every-request-slow-how-do-you-debug-it)
- [435: How do you debug a 403 that comes from a WAF and not from your app?](#435-how-do-you-debug-a-403-that-comes-from-a-waf-and-not-from-your-app)
- [436: A user reports an auth problem. How do you debug it without asking for their password or token?](#436-a-user-reports-an-auth-problem-how-do-you-debug-it-without-asking-for-their-password-or-token)
- [437: What should a logging policy for a back-end team include?](#437-what-should-a-logging-policy-for-a-back-end-team-include)
- [438: You found a token in production logs. What do you do?](#438-you-found-a-token-in-production-logs-what-do-you-do)
- [439: Why are heap snapshots, core dumps and diagnostic reports sensitive?](#439-why-are-heap-snapshots-core-dumps-and-diagnostic-reports-sensitive)
- [440: If you must attach a debugger in production, how do you do it safely?](#440-if-you-must-attach-a-debugger-in-production-how-do-you-do-it-safely)
- [441: What is break-glass access and why is it used for production debugging?](#441-what-is-break-glass-access-and-why-is-it-used-for-production-debugging)
- [442: Is it safe to SSH into a CI runner to debug a failing job?](#442-is-it-safe-to-ssh-into-a-ci-runner-to-debug-a-failing-job)
- [443: Is hashing user IDs or emails in logs enough to protect personal data?](#443-is-hashing-user-ids-or-emails-in-logs-enough-to-protect-personal-data)
- [444: What are the risks of logging the full event in serverless functions?](#444-what-are-the-risks-of-logging-the-full-event-in-serverless-functions)
- [445: Why should audit logs be kept separate from debug logs?](#445-why-should-audit-logs-be-kept-separate-from-debug-logs)
- [446: How do data deletion requests affect logs?](#446-how-do-data-deletion-requests-affect-logs)
- [447: How can APM and monitoring agents leak data, and how do you configure them?](#447-how-can-apm-and-monitoring-agents-leak-data-and-how-do-you-configure-them)
- [448: What debug features must not be left on in production?](#448-what-debug-features-must-not-be-left-on-in-production)
- [449: How do you return useful errors to API clients without leaking internal details?](#449-how-do-you-return-useful-errors-to-api-clients-without-leaking-internal-details)
- [450: An engineer accidentally logged full request bodies, including passwords, in production for two days. What do you do?](#450-an-engineer-accidentally-logged-full-request-bodies-including-passwords-in-production-for-two-days-what-do-you-do)

---

# Easy Questions (1-150)

## 1: What is debugging, and how is it different from testing?

Debugging is finding out why something does not work and fixing the cause. Testing tells you that something is broken. Debugging tells you why. A failing test is often the starting point of debugging, and a new test is often the end of it, so the bug does not come back.

## 2: What steps do you follow when you start debugging a bug?

A simple order that works for most bugs:

1. Understand the expected behavior and the actual behavior.
2. Reproduce the bug.
3. Collect facts: logs, errors, metrics, recent changes.
4. Make a guess (hypothesis) about the cause.
5. Test the guess with one small change or one extra log.
6. Fix the cause, not only the symptom.
7. Add a test and check that the fix works where the bug happened.

## 3: Why is reproducing a bug the first thing to do?

If you can reproduce a bug, you can check your guesses and confirm the fix. Without a reproduction you are guessing and you cannot prove that the fix worked. Even a reproduction that works only one time in ten is much better than none.

## 4: What is a minimal reproduction?

It is the smallest piece of code, data or steps that still shows the bug. You get it by removing things until the bug goes away, then putting back the last thing you removed. A small reproduction often shows the cause directly, and it is also what library maintainers ask for when you open an issue.

## 5: What is the difference between a symptom and a root cause?

The symptom is what you see, for example "the API returns 500". The root cause is why it happens, for example "the database pool is too small, so requests time out waiting for a connection". If you only fix symptoms (for example by adding a retry), the bug often comes back in another form.

## 6: What is binary search debugging?

You split the search space in half and check which half has the problem, then repeat. It works on code (comment out half), on data (process half the records), on time (which deploy between Monday and Friday broke it) and on config. Each step cuts the problem in half, so even big search spaces become small quickly.

## 7: How does git bisect help find a bug?

`git bisect` does a binary search over commits. You mark one commit as good and one as bad, and git checks out commits in the middle until it finds the first bad one.

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.4.0
# test, then mark each step:
git bisect good   # or: git bisect bad
git bisect reset
```

You can automate it with `git bisect run npm test` if a script can tell good from bad.

## 8: What is rubber duck debugging?

You explain the problem out loud, line by line, to someone or something (the "rubber duck"). While explaining, you often notice the wrong assumption yourself. It works because it forces you to say what the code really does, not what you think it does.

## 9: What questions should you ask when a bug report comes in?

- What exactly happened, and what was expected?
- When did it start? Did anything change at that time (deploy, config, traffic, data)?
- Who is affected: all users, one customer, one region, one browser?
- Can it be reproduced? With what input?
- Is there an error message, request ID or timestamp?

The "what changed" and "who is affected" questions narrow the search the most.

## 10: Why should you change only one thing at a time while debugging?

If you change three things and the bug goes away, you do not know which change fixed it, and one of the other changes may add a new bug. One change at a time keeps cause and effect clear. Revert changes that did not help so they do not pile up.

## 11: What is the difference between logs, metrics, and traces?

- **Logs** are records of single events, like "user 42 failed to log in".
- **Metrics** are numbers over time, like request rate, error rate and latency.
- **Traces** show the path of one request across functions and services, with timing for each step.

Metrics tell you that something is wrong, traces tell you where, and logs tell you the details of what happened.

## 12: What are log levels and when do you use each?

Common levels from most to least serious:

- `fatal`: the app cannot continue.
- `error`: an operation failed and needs attention.
- `warn`: something unexpected, but the app handled it.
- `info`: normal important events (server started, job finished).
- `debug`: details for developers.
- `trace`: very detailed, step by step.

Production usually runs at `info`. You turn on `debug` for a short time when you need more detail.

## 13: What is structured logging?

Structured logging writes logs as key-value data (usually JSON) instead of free text. That makes logs easy to search and filter by fields like `userId`, `requestId` or `statusCode`.

```js
import pino from "pino";
const logger = pino();

logger.info({ orderId: "o-123", durationMs: 87 }, "order created");
// {"level":30,"time":...,"orderId":"o-123","durationMs":87,"msg":"order created"}
```

## 14: What is a stack trace and how do you read it?

A stack trace is the list of function calls that were active when an error happened. The top line is the error message, the next line is where the error was thrown, and the lines below are the callers. Look for the first line that points to your own code, not to `node_modules` or Node internals, because that is usually where to start.

## 15: What is a breakpoint?

A breakpoint is a marker on a line of code that pauses the program when it reaches that line. While paused you can look at variables, the call stack and step through the code. It is useful when logs are not enough and you need to see the state at an exact moment.

## 16: What is the difference between step over, step into, and step out?

- **Step over** runs the current line, including any function calls, and stops at the next line.
- **Step into** goes inside the function called on the current line.
- **Step out** runs the rest of the current function and stops back in the caller.

## 17: What is a conditional breakpoint and a logpoint?

A conditional breakpoint pauses only when an expression is true, for example `userId === 42`. This is handy in loops or busy request handlers. A logpoint does not pause at all. It prints a message when the line runs, like adding a `console.log` without editing the code.

## 18: How do you write a good bug report for a back-end issue?

Include:

- Steps to reproduce, with the exact request (method, URL, body) or command.
- Expected and actual result.
- Error message, status code and stack trace.
- Time of the error, environment and version.
- Request ID or trace ID so others can find the logs.

Remove tokens, passwords and personal data before you paste anything.

## 19: What is a regression?

A regression is a bug in a feature that used to work. It is usually caused by a recent change. To find it, compare the working and broken versions, look at recent deploys, or use `git bisect`.

## 20: Why should you write a test that reproduces a bug before fixing it?

The failing test proves you understand the bug and gives you a quick way to check your fix. After the fix the test passes and stays in the suite, so the same bug cannot come back silently. It also documents the edge case for the next developer.

## 21: How do you start Node.js with the inspector?

Use the `--inspect` flag. By default it listens on `127.0.0.1:9229`.

```bash
node --inspect server.js
node --inspect=0.0.0.0:9229 server.js   # listen on all interfaces, e.g. inside Docker
```

Then connect a debugger such as Chrome DevTools or VS Code. Only listen on `0.0.0.0` in a safe, private network, because the inspector gives full control over the process.

## 22: What is the difference between --inspect and --inspect-brk?

`--inspect` starts the app and lets a debugger attach at any time. `--inspect-brk` starts the inspector and pauses on the first line of your code, so you can debug startup code before it runs. Newer Node versions also have `--inspect-wait`, which waits for a debugger to attach but does not pause on the first line.

## 23: How do you debug Node.js in VS Code?

The easiest way is the JavaScript Debug Terminal: open it and run your usual command (`npm run dev`), and VS Code attaches by itself. You can also add a `launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug server",
      "program": "${workspaceFolder}/src/server.js"
    }
  ]
}
```

Use `"request": "attach"` with a `port` to connect to a process that is already running with `--inspect`.

## 24: How do you connect Chrome DevTools to a Node.js process?

Start Node with `--inspect`, open `chrome://inspect` in Chrome and click "inspect" under your target. You can also click the green Node icon in a normal DevTools window. You get the Sources, Console, Memory and Performance tabs for the Node process.

## 25: What does the debugger statement do?

`debugger;` works like a breakpoint written in code. If a debugger is attached, execution pauses there. If no debugger is attached, nothing happens. Do not commit it, and a lint rule like `no-debugger` helps catch it.

## 26: What is the Node.js event loop, in simple words?

Node runs your JavaScript on one main thread. The event loop is the loop that takes the next ready task (a timer, a finished I/O operation, an incoming request) and runs its callback. While a callback runs, nothing else on that thread can run. That is why one slow callback slows down every request.

## 27: What does it mean to block the event loop?

It means some code runs for a long time without giving control back. During that time Node cannot accept requests, run timers or process responses. Symptoms are high latency for all requests, timeouts and health checks failing, even though CPU usage may only be at one core.

## 28: What are common things that block the event loop?

- Sync APIs like `fs.readFileSync` or `crypto.pbkdf2Sync` inside request handlers.
- `JSON.parse` or `JSON.stringify` on very large objects.
- Heavy loops, sorting or image processing on the main thread.
- Regular expressions with catastrophic backtracking (ReDoS).
- Huge synchronous logging.

Move heavy work to worker threads, a queue, or split it into smaller chunks.

## 29: What is the difference between an uncaught exception and an unhandled promise rejection?

An uncaught exception is a thrown error that no `try/catch` caught in synchronous code or a callback. An unhandled rejection is a rejected promise that nobody handled with `await` inside `try/catch` or with `.catch()`. Node reports them through the `uncaughtException` and `unhandledRejection` process events.

## 30: What happens by default when a promise rejection is not handled in Node.js?

Since Node.js 15 the default mode is `throw`: an unhandled rejection is raised as an uncaught exception and the process exits with an error. You can change this with `--unhandled-rejections` (`strict`, `warn`, `none` and others), but the right fix is to handle the rejection in code.

## 31: Why should you always await or return promises?

If you call an async function without `await` or `return`, errors from it are not caught by your `try/catch`, and the code after it may run before it finishes. This causes unhandled rejections, missing data and race conditions. The ESLint rule `@typescript-eslint/no-floating-promises` catches this.

```js
// bug: error not caught, response sent before save finishes
try {
  saveOrder(order);
} catch (e) {
  /* never runs */
}

// fixed
try {
  await saveOrder(order);
} catch (e) {
  logger.error(e);
}
```

## 32: What is the NODE_DEBUG environment variable?

`NODE_DEBUG` turns on debug output from Node's own core modules. You give it a comma-separated list of module names.

```bash
NODE_DEBUG=http,net node server.js
NODE_DEBUG=tls node client.js
```

It is useful when you suspect a problem at the network level, below your own code.

## 33: What is the debug package and how is it used?

`debug` is a small npm package used by many libraries, including Express. It prints messages only when the `DEBUG` environment variable matches the namespace.

```bash
DEBUG=express:* node app.js
DEBUG=myapp:*,-myapp:noisy node app.js
```

```js
import createDebug from "debug";
const debug = createDebug("myapp:orders");
debug("creating order %o", { id: 1 });
```

## 34: Why do async stack traces sometimes look incomplete?

When code continues after an `await` or in a callback, the original caller may already be gone from the stack. V8 can rebuild async stack traces for `async/await` code, but not for plain callbacks or for errors created far from where they are thrown. Use `async/await`, pass the original error as `cause`, and add context to logs to make up for it.

## 35: What are source maps, and why do they matter when debugging TypeScript on the server?

Source maps connect compiled JavaScript lines back to your original TypeScript lines. Without them, stack traces point to `dist/` files that are hard to read. Turn them on in `tsconfig.json` with `"sourceMap": true` and run Node with `--enable-source-maps`.

```bash
node --enable-source-maps dist/server.js
```

## 36: What does console.time do, and when is it useful?

`console.time(label)` starts a timer and `console.timeEnd(label)` prints how long it took. It is a quick way to see which part of the code is slow while you debug locally.

```js
console.time("load-users");
const users = await db.user.findMany();
console.timeEnd("load-users"); // load-users: 152.3ms
```

For real measurement in production, use metrics or tracing instead.

## 37: What does "Cannot find module" mean and how do you fix it?

Node could not find a file or package you imported. Common causes: the package is not installed, a typo in the path, a wrong case in the file name (works on macOS, fails on Linux), missing file extension in ESM imports, or the build output is missing. Check `npm ls <pkg>`, the exact path and the `"type"` field in `package.json`.

## 38: What does EADDRINUSE mean?

`EADDRINUSE` means the port you want to listen on is already used by another process, often an old copy of your server. Find it and stop it, or use another port.

```bash
lsof -i :3000
kill <pid>
```

## 39: What do ECONNREFUSED, ECONNRESET and ETIMEDOUT mean?

- `ECONNREFUSED`: nothing is listening on that host and port, or a firewall rejected the connection.
- `ECONNRESET`: the other side closed the connection suddenly, for example a crash, a proxy timeout or an idle connection being dropped.
- `ETIMEDOUT`: no answer came in time, often a firewall dropping packets or a wrong address.

The error includes the address and port, so check that first.

## 40: What is "JavaScript heap out of memory"?

The V8 heap reached its size limit and the process crashed. It is caused by a memory leak or by loading too much data at once (for example a whole table into an array). You can raise the limit with `--max-old-space-size=4096`, but first find out why memory grows, using heap snapshots or memory metrics.

## 41: How do you debug an Express route that returns 404?

- Check the HTTP method and the exact path, including trailing slashes and prefixes from `app.use('/api', router)`.
- Check that the router is mounted before any catch-all or 404 handler.
- Run with `DEBUG=express:*` to see how routes are matched.
- Log `req.method` and `req.originalUrl` in a first middleware.

## 42: What is error-handling middleware in Express?

It is middleware with four arguments `(err, req, res, next)`. Express calls it when a handler throws or calls `next(err)`. It must be registered after all routes.

```js
app.use((err, req, res, next) => {
  req.log?.error({ err }, "request failed");
  res.status(err.status ?? 500).json({ error: "Internal Server Error" });
});
```

If you define it with three arguments, Express treats it as a normal middleware and it will not catch errors.

## 43: What does "Cannot set headers after they are sent to the client" mean?

The code tried to send a second response for the same request (error code `ERR_HTTP_HEADERS_SENT`). It usually happens when you forget `return` after `res.send()`, call `next()` after responding, or both a callback and a promise send a response. Look at the stack trace to find the second send.

```js
if (!user) {
  return res.status(404).send("Not found"); // without return, code continues
}
res.json(user);
```

## 44: Why does an Express request hang without a response?

The handler never called `res.send()` / `res.json()` / `res.end()` or `next()`. Common reasons are a missing `next()` in a middleware, a branch of an `if` that does not respond, or a promise that never resolves (for example waiting for a database connection). Add a request timeout and log at the start and end of each request to see where it stops.

## 45: How does Express 5 handle errors thrown in async handlers?

In Express 5, if an async handler returns a rejected promise, Express passes the error to `next(err)` for you, so your error middleware handles it. In Express 4 you had to catch the error and call `next(err)` yourself, or use a helper like `express-async-errors`. If you still see unhandled rejections in Express 5, check that the promise is returned or awaited inside the handler.

## 46: Why is req.body undefined in Express?

Express does not parse the body by default. You need a body parser that matches the `Content-Type`:

```js
app.use(express.json()); // application/json
app.use(express.urlencoded({ extended: false })); // form data
```

Also check that the client sends the right `Content-Type` header and that the parser is registered before the routes. In Express 5, `req.body` is `undefined` (not `{}`) when no parser ran.

## 47: How do you turn on logging in Fastify?

Fastify uses Pino. Pass `logger` when you create the app:

```js
import Fastify from "fastify";

const app = Fastify({
  logger: { level: process.env.LOG_LEVEL ?? "info" },
});
```

With logging on, Fastify logs each incoming request and its response with a request ID.

## 48: What is request.log in Fastify?

`request.log` is a child logger bound to the current request. Every line it writes includes the request ID (`reqId`), so you can find all logs for one request.

```js
app.get("/orders/:id", async (request) => {
  request.log.info({ orderId: request.params.id }, "loading order");
  return getOrder(request.params.id);
});
```

## 49: How do you see registered routes in Fastify?

Call `app.printRoutes()` after the app is ready. It prints a tree of all routes, which helps when a route returns 404 because of a wrong prefix or plugin.

```js
await app.ready();
console.log(app.printRoutes());
```

`app.printPlugins()` prints the plugin tree in the same way.

## 50: What does "Nest can't resolve dependencies" mean in NestJS?

Nest could not find a provider to inject into a class constructor. The message shows which argument is missing and in which module. Usually the provider is not in that module's `providers`, the module that provides it does not `export` it, or the module is not in the `imports`. A `?` in the message can also point to a circular import or an undefined value at import time.

## 51: How do you use the built-in Logger in NestJS?

Create a `Logger` with a context name, usually the class name. The context shows in each line, so you know where it came from.

```ts
import { Injectable, Logger } from "@nestjs/common";

@Injectable()
export class OrdersService {
  private readonly logger = new Logger(OrdersService.name);

  create(dto: CreateOrderDto) {
    this.logger.debug(`creating order for ${dto.customerId}`);
  }
}
```

You choose which levels print when you create the app: `NestFactory.create(AppModule, { logger: ['error', 'warn', 'log', 'debug'] })`.

## 52: How do you run a NestJS app in debug mode?

Use the Nest CLI with `--debug`, which starts Node with the inspector:

```bash
nest start --debug --watch
```

Then attach VS Code or Chrome DevTools on port 9229. You can also use the VS Code JavaScript Debug Terminal and run `npm run start:dev`.

## 53: What do the 4xx status codes tell you when debugging an API?

4xx codes mean the server thinks the client did something wrong:

- `400` Bad Request: invalid input or malformed body.
- `401` Unauthorized: no valid credentials (missing or bad token).
- `403` Forbidden: credentials are valid but not allowed.
- `404` Not Found: wrong path or the resource does not exist.
- `409` Conflict: for example a duplicate or a version conflict.
- `422` Unprocessable Content: body parsed fine but failed validation.
- `429` Too Many Requests: rate limited.

Look at the response body for details, and check the request that was really sent.

## 54: What do 500, 502, 503 and 504 usually mean?

- `500` Internal Server Error: your app threw an error. Check app logs.
- `502` Bad Gateway: a proxy or load balancer got a bad or no response from your app (app crashed, closed the connection, wrong port).
- `503` Service Unavailable: no healthy instance, overloaded, or in maintenance.
- `504` Gateway Timeout: the proxy waited too long for your app.

For 502 and 504, look at the proxy logs first, because your app may not have logged anything.

## 55: How do you use curl to debug an API?

curl lets you send the exact request without a browser or client code in the way.

```bash
curl -v https://api.example.com/orders/1 \
  -H "Authorization: Bearer $TOKEN"

curl -i -X POST https://api.example.com/orders \
  -H "Content-Type: application/json" \
  -d '{"item":"book","qty":1}'
```

`-v` shows the TLS handshake and all headers, `-i` shows response headers. Be careful when sharing `-v` output, since it contains your token.

## 56: What is a correlation ID or request ID?

It is a unique ID given to each request, usually at the edge (load balancer or first service). It is added to every log line and passed to other services in a header such as `x-request-id`. When a user reports an error, you search for that one ID and see everything that happened for that request.

## 57: How do you debug a GraphQL query that returns null?

Look at the `errors` array in the response first, since GraphQL may return `null` data together with an error. If there are no errors, check that the resolver returns a value (and awaits it), that the field name in the resolver matches the schema, and that the parent object has the field. Log inside the resolver for that field to see what it gets and returns.

## 58: Why does GraphQL often return 200 even when there are errors?

Over HTTP, a GraphQL server often returns `200 OK` with an `errors` array when the request reached the server and was executed, even if some fields failed. So you cannot rely only on HTTP status codes in monitoring. Check the `errors` field, log resolver errors on the server and track them as a separate metric. Newer servers using the `application/graphql-response+json` media type return 4xx codes for requests that fail before execution, like parse or validation errors.

## 59: What is the N+1 problem in GraphQL and how do you spot it?

It happens when a list query runs one query for the list and then one more query per item for a nested field. 100 items become 101 database queries. You spot it by turning on query logging and seeing many almost identical queries for one request, or by seeing many short child spans in a trace. DataLoader is the usual fix.

## 60: How do you debug a REST API contract mismatch between client and server?

Compare what the client sends with what the server expects: field names, types, required fields, date formats and headers. An OpenAPI spec helps, since you can validate requests and responses against it in tests. Log validation errors with the field path (not the full body) so you can see which field is wrong.

## 61: How do you see the SQL queries an app runs?

Turn on query logging in the ORM or driver (Prisma `log`, Sequelize `logging`, TypeORM `logging`, Knex `debug`). On the database side, PostgreSQL can log statements with `log_min_duration_statement`, and `pg_stat_statements` shows which queries run most. Avoid logging query parameters in production, since they can contain personal data.

## 62: What does EXPLAIN do in SQL?

`EXPLAIN` shows the plan the database will use to run a query: which indexes, which join type and the estimated rows. `EXPLAIN ANALYZE` in PostgreSQL actually runs the query and shows real time and row counts.

```sql
EXPLAIN ANALYZE
SELECT * FROM orders WHERE customer_id = 42 ORDER BY created_at DESC LIMIT 20;
```

A `Seq Scan` on a big table where you expected an index scan is a common sign of a missing index. Be careful with `EXPLAIN ANALYZE` on `UPDATE` or `DELETE`, because it really changes data unless you run it inside a transaction and roll back.

## 63: What is a slow query log?

It is a database log of queries that take longer than a set time. In MySQL you turn on `slow_query_log` and set `long_query_time`. In PostgreSQL you set `log_min_duration_statement`, for example to `500` milliseconds. It shows which queries to look at first.

## 64: How do you enable query logging in Prisma?

Pass `log` when you create the client:

```ts
const prisma = new PrismaClient({
  log: ["query", "info", "warn", "error"],
});
```

To get duration and params as data, use event logging:

```ts
const prisma = new PrismaClient({ log: [{ emit: "event", level: "query" }] });
prisma.$on("query", (e) => {
  console.log(`${e.duration}ms ${e.query}`);
});
```

## 65: What does Prisma error P2002 mean?

`P2002` is a unique constraint violation: you tried to insert or update a row with a value that already exists in a unique column. The error's `meta` tells you which constraint or fields. Handle it in code (often returning `409 Conflict`) instead of letting it become a 500.

```ts
import { Prisma } from "@prisma/client";

try {
  await prisma.user.create({ data });
} catch (e) {
  if (e instanceof Prisma.PrismaClientKnownRequestError && e.code === "P2002") {
    throw new ConflictError("Email already used");
  }
  throw e;
}
```

## 66: What does Prisma error P2025 mean?

`P2025` means a record that the operation needed was not found, for example `update` or `delete` with a `where` that matches nothing. It is also thrown by `findUniqueOrThrow` and `findFirstOrThrow`. Usually you map it to `404`.

## 67: How do you see the queries Mongoose sends?

Turn on debug mode:

```js
mongoose.set("debug", true);
```

It prints each collection method with its filter and options. You can pass a function instead of `true` to send the output to your logger, and you should turn it off in production because filters can contain personal data.

## 68: What is a Mongoose CastError?

Mongoose could not convert a value to the type in the schema. The most common case is passing a string that is not a valid ObjectId to `findById`, for example `/users/abc`. Validate IDs before querying (`mongoose.isValidObjectId(id)`) and return `400` or `404` instead of `500`.

## 69: Why does Mongoose say "buffering timed out after 10000ms"?

Mongoose buffers commands until it is connected. If the connection never succeeds, the command waits 10 seconds and then fails with this message. The real problem is the connection: wrong URI, the database is down, a firewall, an IP allowlist in MongoDB Atlas, or `mongoose.connect()` was never called. Listen to connection errors and log them.

```js
mongoose.connection.on("error", (err) => logger.error({ err }, "mongo error"));
await mongoose.connect(process.env.MONGO_URL);
```

## 70: What does explain() show in MongoDB?

`explain()` shows how MongoDB runs a query: which index it chose, how many keys and documents it read, and how long it took.

```js
db.orders
  .find({ customerId: 42 })
  .sort({ createdAt: -1 })
  .explain("executionStats");
```

Compare `nReturned` with `totalDocsExamined`. If MongoDB reads many more documents than it returns, the query needs a better index.

## 71: What is the difference between COLLSCAN and IXSCAN?

In a MongoDB plan, `COLLSCAN` means MongoDB read every document in the collection. `IXSCAN` means it used an index. `COLLSCAN` on a big collection is a common cause of slow queries and high CPU, and the fix is usually an index that matches the filter and sort.

## 72: What is a DynamoDB ConditionalCheckFailedException?

It means a `ConditionExpression` on a write was false, so DynamoDB did not do the write. For example `attribute_not_exists(pk)` fails when the item already exists. This is often expected (duplicates, optimistic locking), so handle it in code. You can set `ReturnValuesOnConditionCheckFailure: 'ALL_OLD'` to get the current item and see why the check failed.

## 73: What does ProvisionedThroughputExceededException mean in DynamoDB?

The table or index got more reads or writes than its capacity allows, so DynamoDB throttled the request. The AWS SDK retries throttled requests with backoff, but if it keeps happening you need more capacity, on-demand mode, or a better key design to spread traffic. On-demand tables can also throttle (as `ThrottlingException` or with this error), for example on a hot partition or a sudden big spike.

## 74: How do you check if Redis is reachable?

Use `redis-cli` with the same host, port and password as the app:

```bash
redis-cli -h my-redis -p 6379 -a "$REDIS_PASSWORD" PING
# PONG
```

If it hangs, it is often a network or security group problem. If it fails with an auth error, check the password or ACL user. If the server needs TLS, add `--tls`.

## 75: What is the Redis SLOWLOG?

The slow log keeps recent commands that took longer than `slowlog-log-slower-than` microseconds to run. It only counts the time to run the command, not network time.

```bash
redis-cli SLOWLOG GET 10
redis-cli SLOWLOG RESET
```

It quickly shows heavy commands like `KEYS`, big `HGETALL` or `SMEMBERS` calls.

## 76: Why should you not run KEYS * in production?

`KEYS` scans all keys in one go, and Redis runs commands one at a time on its main thread. With millions of keys it blocks Redis for seconds, and every other client waits. Use `SCAN` with a `MATCH` pattern, which works in small steps.

```bash
redis-cli --scan --pattern 'session:*' | head
```

## 77: What does the WRONGTYPE error mean in Redis?

`WRONGTYPE Operation against a key holding the wrong kind of value` means you ran a command for one data type on a key that has another type, for example `HGET` on a string key. Often two parts of the code use the same key name for different things. Use `TYPE key` to check and use clear key prefixes.

## 78: What is a database connection pool and how can it cause bugs?

A pool keeps a set of open connections that requests reuse. Problems happen when the pool is too small (requests wait and time out), too big (the database runs out of connections), or when connections are not given back (a leak, often from transactions that never end). Watch pool metrics like active, idle and waiting connections.

## 79: How can missing transactions cause bugs?

If two related writes are not in a transaction, one can succeed and the other fail, leaving data half updated. For example, the order is created but the stock is not reduced. These bugs look random because they only show up when something fails in the middle. Wrap related writes in a transaction, and check that every query inside really uses the transaction client.

## 80: How do you debug a failed database migration?

Read the exact error and the statement that failed. Check which migrations the database thinks are applied (for example Prisma's `_prisma_migrations` table or `prisma migrate status`). Common causes are data that breaks a new constraint, a lock held by a running app, a timeout on a big table, or a migration edited after it was applied. Test migrations on a copy of production-sized data first.

## 81: What is a message queue and why are queue bugs hard to debug?

A message queue lets one service send messages that another service processes later. Bugs are hard to debug because the producer and consumer run at different times and in different processes, errors are not returned to the caller, and messages can be retried, duplicated or delayed. You need IDs in messages, logs on both sides and metrics on queue size.

## 82: What is consumer lag in Kafka?

Consumer lag is how many messages are in a partition that the consumer group has not yet processed. It is the latest offset minus the committed offset. Growing lag means consumers are too slow, stuck or crashing. It is one of the most important Kafka metrics to watch.

## 83: How do you read messages from a Kafka topic to see what is in it?

Use the console consumer that comes with Kafka:

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic orders --from-beginning --max-messages 10 \
  --property print.key=true --property print.timestamp=true
```

Do not use the group name of your real consumers, or you will take messages away from them and change their offsets. Without `--group`, the tool uses a temporary group.

## 84: What is a dead letter queue?

A dead letter queue (DLQ) is a place where messages go after they fail too many times. They stop blocking the main queue, and you can look at them later to find the cause. A DLQ only helps if someone watches it, so add an alert on its size.

## 85: What is a poison message?

It is a message that always fails, for example because of bad data or a bug in the handler. If it is retried forever, it can block a partition or queue, or fill logs with the same error. Limit retries and send it to a dead letter queue with the error reason.

## 86: What does "unacked" mean in RabbitMQ?

An unacked message has been delivered to a consumer but the consumer has not yet confirmed it with an ack. If the consumer dies or its channel closes, RabbitMQ sends the message again. Many unacked messages usually mean the consumer forgot to ack, is very slow, or is stuck.

## 87: How do you check queues in RabbitMQ?

Use the management UI (port 15672 by default) or the CLI:

```bash
rabbitmqctl list_queues name messages_ready messages_unacknowledged consumers
```

`messages_ready` waiting with `consumers` at 0 means nobody is consuming. A high `messages_unacknowledged` means consumers took messages but are not finishing them.

## 88: What is a failed job in BullMQ, and how do you see why it failed?

A job fails when its processor throws an error or the promise rejects, and it has no more retry attempts. BullMQ saves `failedReason`, `stacktrace` and `attemptsMade` on the job.

```js
const failed = await queue.getFailed(0, 10);
for (const job of failed) {
  console.log(job.id, job.attemptsMade, job.failedReason);
}
```

A UI like Bull Board also shows failed jobs and their errors.

## 89: What is a stalled job in BullMQ?

A job is stalled when the worker that took it stops renewing its lock, for example because the worker crashed or the event loop was blocked for too long. BullMQ then moves the job back to waiting so another worker can try it. If a job stalls more than `maxStalledCount` times, it fails. Frequent stalls usually mean CPU-heavy work on the main thread.

## 90: What does at-least-once delivery mean for debugging?

It means a message will be delivered one or more times, never zero, but duplicates are possible after retries, crashes or rebalances. So "this order was processed twice" is not always a bug in the queue. Handlers should be idempotent, for example by checking a unique message ID before doing the work.

## 91: Why is debugging microservices harder than debugging a monolith?

One user request may pass through many services, each with its own logs, deploys and failures. The cause may be in a service far from where the error shows up. Networks add timeouts, retries and partial failures. You need request IDs, distributed tracing and central logs to follow a request.

## 92: What is distributed tracing?

Distributed tracing follows one request across services. Each service records spans with timing, and they share a trace ID passed in request headers. A tracing UI like Jaeger, Grafana Tempo, Zipkin or a cloud tool shows the whole request as a timeline, so you can see which service is slow or failing.

## 93: What is a span and a trace?

A span is one unit of work, like "HTTP GET /orders" or "SELECT from users", with a start time, duration, status and attributes. A trace is the tree of all spans for one request, connected by a shared trace ID and parent span IDs.

## 94: What is OpenTelemetry?

OpenTelemetry (OTel) is an open standard and set of SDKs for traces, metrics and logs. You add it to your services once and send data to any compatible backend (Jaeger, Grafana, Datadog, cloud tools). For Node.js there are auto-instrumentations for HTTP, Express, Fastify, database drivers and more.

## 95: What is the traceparent header?

`traceparent` is the W3C Trace Context header that carries the trace ID and parent span ID between services.

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

The parts are version, trace ID, parent span ID and flags (`01` means sampled). If a service does not pass it on, the trace breaks into separate pieces.

## 96: What is a health check endpoint?

It is an endpoint like `/health` that load balancers and orchestrators call to see if an instance is OK. A liveness check answers "is the process alive?", while a readiness check answers "can it take traffic now?" (for example, is the database connected). A health check that is too strict or too slow can cause restarts that look like random outages.

## 97: What are the RED and USE metrics?

RED is for services: **R**ate (requests per second), **E**rrors (failed requests) and **D**uration (latency). USE is for resources like CPU, memory and disk: **U**tilization, **S**aturation and **E**rrors. Looking at RED for each service and USE for each host is a quick way to find where a problem is.

## 98: What is the difference between monitoring and observability?

Monitoring checks known things: dashboards and alerts for problems you expected, like high CPU. Observability means your system gives enough data (logs, metrics, traces with useful fields) that you can answer new questions you did not plan for, like "why are only EU users with large carts slow?".

## 99: Why should every network call have a timeout?

Without a timeout, a call to a slow or dead service can wait for a very long time, holding memory, sockets and pool connections. Many such calls can take down your service too. Set timeouts on HTTP clients, database queries and queue operations, and log when they fire.

```js
const res = await fetch(url, { signal: AbortSignal.timeout(3000) });
```

## 100: What is a cascading failure?

It is when a failure in one part spreads to others. For example, the database gets slow, so API requests pile up, so API instances run out of memory, so the load balancer sends all traffic to fewer instances, which then also fail. Timeouts, limits, circuit breakers and load shedding stop the spread.

## 101: How do you see the logs of a Docker container?

```bash
docker logs my-api
docker logs -f --tail 100 my-api        # follow, last 100 lines
docker logs --since 10m my-api
docker compose logs -f api
```

Docker only captures what the app writes to stdout and stderr. If the app writes logs to a file inside the container, `docker logs` will show nothing.

## 102: How do you get a shell inside a running container?

```bash
docker exec -it my-api sh      # or bash if the image has it
```

Inside you can check env vars, files, DNS (`nslookup db`) and network (`wget -qO- http://localhost:3000/health`). Minimal images like distroless have no shell. For those, use `docker debug` (Docker Desktop) or start a separate debug container that shares the same network.

## 103: What does docker inspect show?

`docker inspect` prints the full configuration and state of a container or image as JSON: env vars, mounts, networks, IP addresses, health check status, exit code and whether it was OOM killed.

```bash
docker inspect my-api --format '{{.State.ExitCode}} {{.State.OOMKilled}}'
```

The output contains env vars, so it may contain secrets. Do not paste it in a ticket.

## 104: What does exit code 137 mean for a container?

137 is 128 + 9, which means the process was killed with `SIGKILL`. Most often the container went over its memory limit and was OOM killed. It can also mean it did not stop in time after `SIGTERM` and was force killed. Check `docker inspect` for `OOMKilled`, or `kubectl describe pod` in Kubernetes. Exit code 143 (128 + 15) means it stopped after `SIGTERM`.

## 105: Why does an app work locally but not inside Docker?

Common reasons:

- The server listens on `127.0.0.1`, so it is not reachable from outside the container. Listen on `0.0.0.0`.
- It uses `localhost` to reach the database, but inside the container `localhost` is the container itself. Use the service name, like `db`.
- Missing env vars or files that were on your machine.
- Different Node version or OS (native modules built for macOS).
- `.dockerignore` or the build skipped files you need.

## 106: How do you see the full output of a Docker build?

BuildKit hides most output by default. Use plain progress and skip the cache to see every step:

```bash
docker build --progress=plain --no-cache -t my-api .
```

This shows the full output of each `RUN` command, so you can see why `npm ci` or a build step failed.

## 107: How do you see the logs of a Kubernetes pod?

```bash
kubectl logs my-pod
kubectl logs my-pod -c api              # one container in a multi-container pod
kubectl logs -f deploy/my-api           # follow logs of a deployment pod
kubectl logs my-pod --previous          # logs of the last crashed container
kubectl logs -l app=my-api --tail=50    # by label
```

`--previous` is key for crash loops, because the current container may have just started and has no useful logs yet.

## 108: What does kubectl describe pod show?

It shows the pod's status, each container's state and last state (with exit code and reason like `OOMKilled`), restart count, probes, resource requests and limits, volumes and the recent events. Events at the bottom often explain the problem directly, like failed scheduling, image pull errors or failing probes.

## 109: What is CrashLoopBackOff?

It means a container keeps starting and crashing, and Kubernetes waits longer between each restart. It is a symptom, not a cause. Check `kubectl logs --previous` for the error and `kubectl describe pod` for the exit code. Common causes are a missing env var or secret, a failing liveness probe, a wrong command, or the app crashing at startup.

## 110: What is ImagePullBackOff?

Kubernetes could not pull the container image. Usually the image name or tag is wrong, the tag was never pushed, the registry needs credentials (`imagePullSecrets`) that are missing, or the node cannot reach the registry. `kubectl describe pod` shows the exact error from the registry.

## 111: Why does a pod stay in Pending?

The scheduler could not place it on any node. Common reasons are not enough CPU or memory for the pod's requests, node taints without matching tolerations, node selectors or affinity that no node matches, or a PersistentVolumeClaim that cannot be bound. The events in `kubectl describe pod` say which one.

## 112: What is the difference between liveness and readiness probes?

- A **readiness** probe failing removes the pod from Service endpoints, so it gets no traffic, but it is not restarted.
- A **liveness** probe failing makes Kubernetes restart the container.
- A **startup** probe holds off the other probes until the app has started.

A common mistake is checking the database in the liveness probe. When the database is slow, all pods restart at once and make things worse.

## 113: How do you reach a pod or service from your laptop for debugging?

Use `kubectl port-forward`:

```bash
kubectl port-forward svc/my-api 8080:80
curl http://localhost:8080/health
```

This tunnels traffic through the Kubernetes API, so you do not need to expose the service publicly. It is good for quick checks, not for load.

## 114: How do you test an Nginx config?

```bash
nginx -t        # check syntax and that files exist
nginx -T        # check and print the full config, including included files
nginx -s reload # reload after a successful test
```

Always run `nginx -t` before reloading. `nginx -T` is helpful when you are not sure which `server` block or included file is really used.

## 115: Where are Nginx logs and what is in them?

By default on many Linux installs they are in `/var/log/nginx/access.log` and `/var/log/nginx/error.log`. In the official Docker image they go to stdout and stderr. The access log has one line per request (client IP, method, path, status, size, time). The error log has problems like upstream connection failures, timeouts and config errors, which is where 502 and 504 causes show up.

## 116: What does a 502 Bad Gateway from Nginx usually mean?

Nginx could not get a valid response from the upstream app. Check the error log for messages like `connect() failed (111: Connection refused)` (app not running or wrong port) or `upstream prematurely closed connection` (app crashed or closed the connection). Also check that `proxy_pass` points to the right host and port.

## 117: What does a 413 Request Entity Too Large mean?

The request body is bigger than Nginx allows. The default `client_max_body_size` is 1 MB. Raise it where needed:

```nginx
location /upload {
    client_max_body_size 20m;
    proxy_pass http://app;
}
```

Your app or body parser may have its own limit too, for example `express.json({ limit: '1mb' })`.

## 118: What is CloudWatch Logs?

CloudWatch Logs is the AWS service that stores logs from Lambda, ECS, EC2 agents and other services. Logs are grouped into log groups and log streams. CloudWatch Logs Insights lets you query them:

```
fields @timestamp, @message
| filter level = "error"
| sort @timestamp desc
| limit 50
```

## 119: How do you check which AWS identity your code or CLI is using?

```bash
aws sts get-caller-identity
```

It returns the account ID and the ARN of the user or role. Many "access denied" problems happen because the code uses a different profile, role or account than you think. In code, the SDK reads credentials from env vars, a profile, or an attached role, in that kind of order.

## 120: What does AccessDenied in AWS usually mean and where do you look?

The identity making the call is not allowed to do that action on that resource. Read the full error: it often names the action, the resource and which kind of policy denied it. Then check the IAM role policies, resource policies (like S3 bucket policies or KMS key policies), SCPs and permission boundaries. CloudTrail shows the failed call with the exact identity and error.

## 121: What are Application Insights and Log Analytics in Azure?

Application Insights is the Azure Monitor feature for app telemetry: requests, dependencies, exceptions and traces. Log Analytics stores logs in a workspace, and you query them with KQL (Kusto Query Language):

```kusto
AppExceptions
| where TimeGenerated > ago(1h)
| summarize count() by ProblemId
| order by count_ desc
```

Azure Monitor now recommends the OpenTelemetry-based distro for Node.js (`@azure/monitor-opentelemetry`).

## 122: What are Cloud Logging and Cloud Trace in GCP?

Cloud Logging collects logs from Cloud Run, GKE, Cloud Functions and other services, and you can search them in the Logs Explorer. Cloud Trace stores distributed traces. Error Reporting groups similar errors. If you write JSON logs to stdout, Cloud Logging parses fields like `severity` and `message`, and a `logging.googleapis.com/trace` field links a log line to a trace.

## 123: How do you see more detail when Terraform fails?

Set `TF_LOG` to get debug logs:

```bash
TF_LOG=DEBUG terraform plan
TF_LOG=TRACE TF_LOG_PATH=./tf.log terraform apply
```

`TF_LOG_CORE` and `TF_LOG_PROVIDER` let you set the level for Terraform itself and for providers separately. These logs can contain secrets and tokens, so do not share them as they are.

## 124: What does terraform plan tell you?

It shows what Terraform will create, change or destroy to make real infrastructure match your code. When debugging, it tells you if the code and the real state are different. Read lines marked `-/+` (replace) carefully, because they often mean a resource will be destroyed and recreated.

## 125: What is a Terraform state lock error?

Terraform locks the state file during operations so two runs do not change it at the same time. If a run crashed or was cancelled, the lock can stay. First make sure no other run is really active. Then remove it with the lock ID from the error:

```bash
terraform force-unlock <LOCK_ID>
```

Removing a lock while another run is active can break the state.

## 126: How do you turn on debug logging in GitHub Actions?

Re-run the failed job with "Enable debug logging" checked, or set repository secrets or variables:

- `ACTIONS_STEP_DEBUG` = `true` for detailed step logs.
- `ACTIONS_RUNNER_DEBUG` = `true` for runner diagnostic logs.

In a workflow, `runner.debug` is `'1'` when debug logging is on, so your scripts can print extra info only then.

## 127: Why does a workflow pass locally but fail in GitHub Actions?

Common reasons: a different Node or OS version, a missing env var or secret, a file that is not committed (it exists only on your machine), a different working directory, a case-sensitive file system on Linux runners, missing services like a database, or a cache restoring old dependencies. Print versions and env names (not values) at the start of the job to compare.

## 128: How are secrets masked in GitHub Actions logs?

GitHub replaces the values of secrets with `***` in logs. Values you create at runtime are not masked unless you mask them:

```bash
echo "::add-mask::$TEMP_TOKEN"
```

Masking is not perfect. If a secret is changed (for example base64-encoded or split), the new form is not masked. So do not print secrets at all.

## 129: What is the difference between 401 and 403 when debugging auth?

`401 Unauthorized` means the server does not know who you are: the token is missing, expired, or invalid. `403 Forbidden` means the server knows who you are, but you are not allowed to do this. So for 401 check the token and how it is sent, and for 403 check roles, scopes and permissions.

## 130: What is a CORS error and is it a back-end problem?

A CORS error happens when a browser blocks a page from reading a response from another origin because the server did not send the right `Access-Control-Allow-*` headers. The browser enforces it, but the fix is on the server: return the right headers and answer the `OPTIONS` preflight. Tools like curl do not check CORS, so a request can work in curl and fail in the browser.

## 131: What is a JWT made of?

A JWT has three base64url parts separated by dots: `header.payload.signature`. The header says the algorithm (`alg`) and often a key ID (`kid`). The payload has claims like `sub`, `exp`, `iat`, `iss` and `aud`. The signature proves the first two parts were not changed. The payload is only encoded, not encrypted, so anyone can read it.

## 132: How do you look inside a JWT safely?

Decode the header and payload locally without verifying:

```js
import { decodeJwt, decodeProtectedHeader } from "jose";

console.log(decodeProtectedHeader(token)); // { alg, kid, typ }
console.log(decodeJwt(token)); // { sub, exp, iss, aud, ... }
```

Or in a shell: `echo "$TOKEN" | cut -d. -f2 | base64 -d` (you may need to add `=` padding). Avoid pasting real production tokens into websites, since the token still works for anyone who has it until it expires.

## 133: What does "jwt expired" mean?

The token's `exp` time is in the past. With the `jsonwebtoken` package you get a `TokenExpiredError` with an `expiredAt` field. With `jose` you get a `JWTExpired` error. The client should refresh the token. If tokens expire much earlier than expected, check the server clock and the token lifetime setting.

## 134: What does "invalid signature" mean for a JWT?

The signature does not match the header and payload with the key you used to verify. Usually the wrong key or secret is used (different environment, rotated key, wrong `kid`), the algorithm does not match, or the token was changed. Compare the `iss`, `kid` and `alg` in the token header with your server config.

## 135: What is clock skew and how does it affect JWT checks?

Clock skew is when the clocks of two servers are slightly different. If the server that creates a token is ahead, another server may reject a fresh token as "not valid yet" (`nbf` or `iat`), or accept it a bit after it expired. Keep clocks in sync with NTP and allow a small tolerance, like 30 seconds.

```js
await jwtVerify(token, key, { clockTolerance: 30 }); // seconds
```

## 136: Why might a cookie-based session not work?

Check:

- `Secure` cookies are only sent over HTTPS.
- `SameSite=Lax` or `Strict` blocks the cookie on many cross-site requests; cross-site needs `SameSite=None; Secure`.
- The `Domain` and `Path` must match the request.
- For cross-origin `fetch`, the client needs `credentials: 'include'` and the server needs `Access-Control-Allow-Credentials: true` and a specific origin.
- Behind a proxy, Express needs `trust proxy` or it thinks the request is HTTP and will not set `Secure` cookies.

## 137: What is TLS and what is a certificate?

TLS encrypts traffic between a client and a server and lets the client check the server's identity. A certificate holds the server's public key and its names (in the Subject Alternative Name), and it is signed by a certificate authority (CA). The client trusts the certificate if it can build a chain from it, through intermediate certificates, to a root CA it trusts.

## 138: What does "certificate has expired" mean?

The certificate's "not after" date is in the past. In Node the error code is `CERT_HAS_EXPIRED`. Check the dates:

```bash
echo | openssl s_client -connect api.example.com:443 -servername api.example.com 2>/dev/null \
  | openssl x509 -noout -dates
```

If the certificate looks valid, check the clock on the client machine, because a wrong clock gives the same error. An expired intermediate certificate can also cause it.

## 139: What does "self signed certificate in certificate chain" mean?

The chain ends in a certificate that your client does not trust, often a company proxy that inspects traffic, or a private CA. The code in Node is `SELF_SIGNED_CERT_IN_CHAIN`. The fix is to trust that CA, for example with `NODE_EXTRA_CA_CERTS=/path/to/ca.pem`, not to turn off verification.

## 140: How do you check a server's certificate from the command line?

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com -showcerts
curl -vI https://api.example.com
```

`openssl s_client` shows the chain the server sends and whether verification passed (`Verify return code: 0 (ok)`). `-servername` sends SNI, which you need when one IP serves many domains. curl `-v` shows the certificate subject, issuer, dates and any error.

## 141: What is NODE_TLS_REJECT_UNAUTHORIZED=0 and why is it dangerous?

Setting it to `0` turns off TLS certificate checks for the whole Node process. Node prints a warning when you do this. Any server, including an attacker in the middle, can then pretend to be your API or database, and your app will send it tokens and data. Never use it in production. Fix the real cause, such as a missing CA or intermediate certificate.

## 142: Why should you not log secrets?

Logs are copied to many places: log services, backups, developer laptops, tickets and third-party tools. More people can read them than can read your secret store, and they are kept for a long time. A password or token in a log is a leak, and you then need to rotate it.

## 143: What counts as personal data (PII) in logs?

Anything that can identify a person, alone or together with other data: names, emails, phone numbers, addresses, IP addresses, user IDs linked to a person, ID numbers, payment details, health data and precise location. Laws like GDPR apply to logs too, including rules on how long you keep them and who can see them.

## 144: What should never be written to logs?

- Passwords, even wrong ones.
- Access tokens, refresh tokens, API keys, session cookies.
- `Authorization` and `Cookie` headers.
- Private keys and connection strings with passwords.
- Full card numbers, CVV, bank details.
- Full request and response bodies of sensitive endpoints.

Log an ID or a short safe summary instead.

## 145: Why should tokens not be put in URLs?

URLs are logged in many places: access logs on proxies and load balancers, browser history, analytics and the `Referer` header sent to other sites. A token in a query string like `?token=abc` will end up in those logs. Send tokens in headers or the request body.

## 146: What is log redaction?

Redaction removes or masks sensitive fields before a log line is written. With Pino you list the paths to hide:

```js
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
```

Redaction is a safety net. The better rule is to not pass sensitive data to the logger in the first place.

## 147: Why is debugging in production risky?

Your actions affect real users and real data. A breakpoint pauses the whole process, extra logging can slow the app and leak data, a wrong query can lock tables, and a quick fix without review can break more. Prefer read-only checks, short and controlled changes, and tools made for production like logs, metrics, traces and feature flags.

## 148: How is debugging in staging different from debugging in production?

In staging you can use a debugger, turn on full logs, restart services and use test data. In production you mostly read: logs, metrics, traces and read-only queries, with access controls and audit. The problem is that staging often does not have the same data size, traffic or config, so some bugs only show in production.

## 149: How does a feature flag help with debugging?

A feature flag lets you turn code on or off without a deploy. If a new feature causes errors, you turn it off and the problem stops while you investigate. You can also turn on a feature, or extra debug logging, for only some users or for internal accounts, which limits the impact.

## 150: What is a rollback, and when is it better than debugging live?

A rollback puts the previous working version back. If a new deploy clearly caused errors for users, roll back first and debug after, because the users stop being affected right away. Debug live only when a rollback is not possible, for example after a database change that the old version cannot handle.

# Moderate Questions (151-300)

## 151: How do you debug a bug that only happens sometimes?

Intermittent bugs usually depend on timing, load, data or a specific instance. Collect every case you can and look for what they share: same instance, same time of day, same input size, same customer, concurrent requests. Add logs with IDs and timings around the suspected code. Then try to make it happen more often, for example by running the test in a loop, adding load, or adding small delays to change timing.

```bash
for i in $(seq 1 200); do npm test -- orders.spec.ts || break; done
```

## 152: How do you debug "works on my machine" problems?

List what is different between your machine and the failing environment: runtime version, OS, env vars, config files, dependency versions (lockfile), data, network access and permissions. Print these at startup (without secret values) in both places and compare. Running the app in the same container image locally removes most of the differences.

## 153: How do you use the "what changed" approach after a deploy?

Most production bugs come from a change. Line up the time the problem started with deploys, config changes, feature flag changes, dependency updates, infrastructure changes, traffic changes and data imports. Look at the diff between the last good version and the current one. If one change matches the start time, it is the main suspect, and rolling it back is often the quickest test.

## 154: How do you form and test a hypothesis while debugging?

Write down a clear guess, like "requests fail because the token cache returns an expired token after 1 hour". Then decide what you would see if the guess is true and what you would see if it is false. Run the cheapest check that tells them apart: a log line, a query, a test. If the result does not match, drop the guess and pick the next one instead of bending the evidence to fit.

## 155: How do you debug a performance regression?

1. Confirm it with numbers: which endpoint, which percentile (p50, p95, p99), since when.
2. Compare traces of a slow request before and after the change to see which span grew.
3. Check for new queries, missing indexes, bigger payloads, removed caching, or new sync code.
4. Profile the slow path (CPU profile, `EXPLAIN ANALYZE`).
5. Fix and compare with the same load and the same data.

## 156: How do you decide between adding logs and using a debugger?

Use a debugger when you can reproduce the bug locally and need to see a lot of state at one moment. Use logs when the bug happens only in deployed environments, involves timing or many requests, or crosses several services, since a debugger pauses the process and changes timing. Logs also stay after the fix and help next time, so add the useful ones permanently.

## 157: What makes a log line useful?

A useful log line has a clear message, the right level, a timestamp, the request or trace ID, and the IDs of the things involved (order ID, job ID), plus the values that explain the decision the code made. It should be structured (JSON) so you can filter on fields. It should not contain secrets or personal data, and should not repeat for every item in a big loop.

```js
logger.warn(
  { orderId, paymentId, attempt, statusCode: res.status },
  "payment provider returned error, will retry",
);
```

## 158: How do you debug a problem you cannot reproduce locally?

Use what the failing environment can tell you: logs around the time, traces of failed requests, metrics, and the exact input if you can get it safely. Compare the environment with yours (versions, config, data size). Add more targeted logging behind a flag and deploy it, then wait for the problem to happen again. Sometimes you can reproduce it with a copy of the data that has personal data removed.

## 159: How do you write a postmortem for a production bug?

Keep it blameless and factual. Include a short summary, the impact (who, how long, how bad), a timeline, the root cause and the things that made it worse, how it was found and fixed, and action items with owners. The goal is to fix the system and the process, for example by adding a missing alert or test, not to blame a person.

## 160: How do you debug a bug that seems to be in a third-party library?

First make sure it is really the library: build a minimal reproduction with only your code calling the library. Check the library's issue tracker and changelog for the version you use. Read the library source in `node_modules` and set breakpoints there, or add logs temporarily. If it is a real bug, pin a working version, use a workaround, or apply a patch with `patch-package` or `npm`'s built-in overrides until a fix is released.

## 161: How do you debug problems caused by dependency upgrades?

Look at the lockfile diff to see which packages really changed, including indirect ones. `npm ls <pkg>` shows which versions are installed and why. Read the changelogs for breaking changes. If many things changed, upgrade in smaller steps or bisect the lockfile. Use `npm ci` in CI so builds always use the lockfile.

```bash
npm ls axios
npm explain axios
```

## 162: How do you debug environment variable and config problems?

Validate config at startup and fail fast with a clear message if something is missing or wrong, instead of failing later on the first request. Log which config source was loaded and the names of variables that are set, not their values. Watch for common mistakes: env vars are always strings (`"false"` is truthy), extra spaces or quotes, a `.env` file that is not loaded in production, and different names between environments.

```js
import { z } from "zod";

const env = z
  .object({
    DATABASE_URL: z.string().url(),
    PORT: z.coerce.number().default(3000),
    FEATURE_X: z.enum(["true", "false"]).transform((v) => v === "true"),
  })
  .parse(process.env);
```

## 163: How do you debug a Node.js app running in Docker or Kubernetes with the inspector?

Start Node with `--inspect=0.0.0.0:9229` so it listens outside the container, then publish or forward the port to your machine only.

```bash
docker run -p 127.0.0.1:9229:9229 my-api node --inspect=0.0.0.0:9229 server.js
kubectl port-forward pod/my-api-abc 9229:9229
```

Then attach from VS Code or `chrome://inspect`. Do this in dev or staging. In production, a paused process stops serving traffic and the inspector port lets anyone who reaches it run code.

## 164: How do you attach a debugger to a running Node.js process that was not started with --inspect?

On Linux and macOS, send `SIGUSR1` to the process. Node then starts the inspector on the default port 9229.

```bash
kill -USR1 <pid>
```

Then attach as usual. In a container, run this inside the container and port-forward 9229. It is useful when a process is already in a bad state and you do not want to restart it and lose that state.

## 165: How do you measure event loop lag?

Use `monitorEventLoopDelay` from `perf_hooks`. It measures how late timers fire, which shows how long the loop was busy.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  logger.info(
    {
      p50ms: h.percentile(50) / 1e6,
      p99ms: h.percentile(99) / 1e6,
      maxMs: h.max / 1e6,
    },
    "event loop delay",
  );
  h.reset();
}, 10_000);
```

Values are in nanoseconds. A p99 of hundreds of milliseconds means something is blocking the loop.

## 166: What is event loop utilization (ELU)?

ELU is the share of time the event loop was busy running code instead of waiting for I/O, from 0 to 1. It is a better load signal for Node than CPU percent, because it is about the one main thread.

```js
import { performance } from "node:perf_hooks";

let last = performance.eventLoopUtilization();
setInterval(() => {
  const now = performance.eventLoopUtilization(last);
  console.log("ELU", now.utilization.toFixed(2));
  last = performance.eventLoopUtilization();
}, 5000);
```

ELU close to 1 means the process cannot take more work, even if the machine has free CPU cores.

## 167: How do you find what is blocking the event loop?

Take a CPU profile while the problem happens and look for long functions on the main thread. Search the code for sync APIs (`readFileSync`, `execSync`, `*Sync` crypto), big `JSON.parse` / `JSON.stringify` calls, and regex used on user input. Log the duration of suspected handlers. Event loop delay metrics together with request logs show which requests ran when the lag spiked.

## 168: How do you take a CPU profile in Node.js?

Some options:

```bash
node --cpu-prof server.js            # writes a .cpuprofile file when the process exits
node --cpu-prof --cpu-prof-dir=./profiles server.js
```

Or attach Chrome DevTools, open the Performance tab, record while you send load, then stop. Open `.cpuprofile` files in Chrome DevTools or VS Code. Profile with realistic load, because a profile of an idle server shows nothing useful.

## 169: How do you read a flame graph?

Each box is a function. The width shows how much total time was spent in it and in the functions it called. Boxes on top are called by the boxes below. Look for wide boxes, especially wide boxes at the top of a stack with nothing above them, since those are functions using CPU themselves. Height is just call depth and does not mean slow.

## 170: How do you take a heap snapshot in Node.js?

- Chrome DevTools: attach, open the Memory tab, take a heap snapshot.
- From code: `v8.writeHeapSnapshot()` writes a `.heapsnapshot` file.
- On a signal: start with `--heapsnapshot-signal=SIGUSR2`, then `kill -USR2 <pid>`.
- Before a crash: `--heapsnapshot-near-heap-limit=1`.

Writing a snapshot pauses the process and needs a lot of extra memory, so it can itself crash a process that is near its limit.

## 171: How do you find a memory leak in Node.js?

1. Confirm it: heap used keeps growing over time and does not drop after garbage collection.
2. Take a heap snapshot, run traffic, take a second one, run more traffic, take a third.
3. In DevTools, compare snapshots and sort by "Size Delta" or "# New" to see which objects keep growing.
4. Open the retainers of those objects to see what keeps them alive, for example a global `Map` or an event listener.

Use the same load each time so the numbers are comparable.

## 172: What are common causes of memory leaks in Node.js?

- Caches or maps that grow forever with no size limit or TTL.
- Event listeners added per request and never removed.
- Timers and intervals that are never cleared.
- Closures that keep large objects alive.
- Storing request data in module-level variables.
- Promises that never settle and keep their context alive.
- Unbounded queues in memory when consumers are slower than producers.

## 173: What is a diagnostic report in Node.js?

It is a JSON file with the JavaScript and native stacks, heap stats, resource usage, loaded libraries, libuv handles and environment variables at that moment. You can create it on demand or on crashes:

```bash
node --report-uncaught-exception --report-on-fatalerror --report-on-signal --report-dir=/tmp/reports server.js
```

```js
process.report.writeReport();
```

Because it contains env vars and command line arguments, a report can contain secrets. Treat it as sensitive.

## 174: How do you find where an unhandled promise rejection came from?

Log the reason with its stack in a `unhandledRejection` handler, then let the process exit:

```js
process.on("unhandledRejection", (reason) => {
  logger.fatal({ err: reason }, "unhandled rejection");
  process.exit(1);
});
```

If the reason is not an `Error` (for example a rejected string), there is no stack, so always reject with `Error` objects. Running with `--trace-warnings` and `--trace-uncaught` also prints more stack details.

## 175: How do you debug a Node.js process that exits without an error?

Check the exit code first (`echo $?`, or the container's exit code). Code 0 with no output often means the event loop had nothing left to do, for example the server never started listening or the main promise finished early. A non-zero code with no logs can mean `process.exit()` was called somewhere, a kill signal from outside (OOM, orchestrator), or logs were not flushed before exit. Add a `process.on('exit', code => ...)` log and search the code for `process.exit`.

## 176: How do you debug a Node.js process that never exits?

Something keeps the event loop alive: an open server, a database pool, a Redis client, a timer or an open socket. `process.getActiveResourcesInfo()` lists the types of active resources, and the `why-is-node-running` package shows where they were created. In tests this often shows up as Jest saying it did not exit, which you fix by closing connections in `afterAll`.

```js
setTimeout(() => console.log(process.getActiveResourcesInfo()), 5000).unref();
```

## 177: How does AsyncLocalStorage help with request logs?

`AsyncLocalStorage` keeps data that follows one request through all its async calls, so any log line can include the request ID without passing it through every function.

```js
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";

const als = new AsyncLocalStorage();

app.use((req, res, next) => {
  const requestId = req.get("x-request-id") ?? randomUUID();
  als.run({ requestId }, next);
});

export const log = (msg, data = {}) =>
  logger.info({ ...data, requestId: als.getStore()?.requestId }, msg);
```

OpenTelemetry uses the same idea to keep the current span.

## 178: How do you debug libuv thread pool saturation?

Some Node APIs run on the libuv thread pool, which has 4 threads by default: `fs` operations, `dns.lookup`, and CPU-heavy `crypto` and `zlib` calls. If many of these run at once, they wait in line, and even unrelated DNS lookups or file reads get slow. Symptoms are slow `fs` or DNS calls while the event loop itself is not busy. Raise `UV_THREADPOOL_SIZE` (set it before the pool is first used, ideally as an env var at startup), and avoid many parallel heavy operations like bcrypt hashing.

## 179: What do the fields of process.memoryUsage() mean?

- `rss`: total memory the process uses in RAM, including code, stacks, heap and native memory.
- `heapTotal`: memory V8 has reserved for the JavaScript heap.
- `heapUsed`: the part of the heap actually used by objects.
- `external`: memory for C++ objects tied to JS objects, like Buffers.
- `arrayBuffers`: memory for `ArrayBuffer` and `Buffer` data (part of `external`).

If `rss` grows but `heapUsed` stays flat, the leak is probably outside the JS heap, for example in Buffers or a native module.

## 180: How do you debug ESM and CommonJS errors in Node.js?

Common ones:

- `ERR_REQUIRE_ESM`: older Node versions could not `require()` an ES module. Node 22.12+ and 20.19+ support `require(esm)` for modules without top-level `await`. Otherwise, use `import()` or switch your project to ESM.
- `ERR_MODULE_NOT_FOUND` in ESM: relative imports need the full file extension, like `./utils.js`.
- `__dirname is not defined in ES module scope`: use `import.meta.dirname` and `import.meta.filename`.
- `Cannot use import statement outside a module`: the file is treated as CommonJS. Set `"type": "module"` or use `.mjs`.

## 181: How do you debug a MaxListenersExceededWarning?

Node warns when more than 10 listeners are added for the same event on one emitter. It is often a leak: a listener added on every request or every reconnect and never removed. Run with `--trace-warnings` to get a stack trace of where the listener was added. Fix the code that keeps adding listeners. Only raise the limit with `setMaxListeners` if many listeners are really expected.

## 182: How do you debug fetch errors in Node.js?

Node's `fetch` (based on undici) throws `TypeError: fetch failed` for network errors. The real reason is in `error.cause`, so always log it.

```js
try {
  await fetch("http://payments:8080/charge", {
    signal: AbortSignal.timeout(5000),
  });
} catch (err) {
  logger.error({ err, cause: err.cause }, "payment call failed");
  // cause.code: ECONNREFUSED, ENOTFOUND, UND_ERR_CONNECT_TIMEOUT, ...
}
```

A timeout from `AbortSignal.timeout` throws a `TimeoutError` instead. Remember that `fetch` does not throw on 4xx or 5xx responses, so check `res.ok`.

## 183: How do you debug middleware order problems in Express?

Express runs middleware in the order you register it. Problems happen when, for example, the auth middleware runs after the router, the body parser is added after the routes, the static file middleware answers before your route, or the error handler is not last. Print or review the order of `app.use` calls, and add a temporary logging middleware between steps to see how far a request gets.

## 184: How do you log every request and response in Express safely?

Use a request logger like `pino-http`, which logs method, URL, status and duration with a request ID. Configure redaction for sensitive headers, and do not log bodies by default.

```js
import pinoHttp from "pino-http";

app.use(
  pinoHttp({
    redact: [
      "req.headers.authorization",
      "req.headers.cookie",
      'res.headers["set-cookie"]',
    ],
    customLogLevel: (req, res, err) =>
      err || res.statusCode >= 500
        ? "error"
        : res.statusCode >= 400
          ? "warn"
          : "info",
  }),
);
```

Also be careful with query strings, since some clients put tokens or emails there.

## 185: How do you debug a "trust proxy" problem in Express?

Behind a load balancer, Express sees the proxy's IP and protocol unless you tell it to trust the proxy. Symptoms: `req.ip` is always the same internal IP (so rate limiting blocks everyone at once), `req.protocol` is `http` on an HTTPS site, and `Secure` cookies are not set. Set `trust proxy` to the number of proxies in front of the app, not just `true`, because `true` lets clients fake their IP with `X-Forwarded-For`.

```js
app.set("trust proxy", 1); // one proxy (for example the load balancer)
```

## 186: What route path changes in Express 5 can break routes?

Express 5 uses a newer `path-to-regexp`, so some old patterns fail or behave differently:

- A bare `*` wildcard must be named: `/files/*splat`, and use `/{*splat}` to also match the root.
- Optional parts use braces: `/users{/:id}` instead of `/users/:id?`.
- Regex characters like `(`, `)` or `+` inside path strings are not supported.

If routes stop matching after an upgrade, check every path with wildcards or optional params.

## 187: How do you debug encapsulation problems with Fastify plugins?

In Fastify, each `register` creates a new context. Decorators, hooks and plugins added inside it are visible to that plugin and its children, but not to the parent or sibling plugins. So a decorator like `app.db` can be `undefined` in a route outside the plugin. If a plugin should share things with the whole app, wrap it with `fastify-plugin`.

```js
import fp from "fastify-plugin";

export default fp(async (app) => {
  app.decorate("db", createDb());
});
```

`app.printPlugins()` shows the plugin tree.

## 188: What does the "Reply was already sent" error mean in Fastify?

The handler tried to send a response twice (`FST_ERR_REP_ALREADY_SENT`). A common cause is an async handler that calls `reply.send()` and then also returns a value, or calls `reply.send()` inside a callback after the handler already finished. In an async handler, either return the value, or call `reply.send()` and `return reply`.

```js
app.get("/a", async (request, reply) => {
  return { ok: true }; // good
});

app.get("/b", async (request, reply) => {
  setTimeout(() => reply.send({ ok: true }), 10);
  return reply; // tells Fastify you will send later
});
```

## 189: How do you debug schema validation errors in Fastify?

Fastify validates `body`, `querystring`, `params` and `headers` against your JSON schemas with Ajv and returns `400` with a message naming the failed field. To see more, use a custom error handler that logs `error.validation`:

```js
app.setErrorHandler((error, request, reply) => {
  if (error.validation) {
    request.log.warn(
      { validation: error.validation, context: error.validationContext },
      "validation failed",
    );
    return reply.status(400).send({ message: error.message });
  }
  reply.send(error);
});
```

Also remember that Ajv in Fastify coerces types by default, so `"5"` can become `5` in querystrings.

## 190: Why are some fields missing from a Fastify response?

If a route has a response schema, Fastify serializes the response with `fast-json-stringify` and only includes properties listed in the schema. Fields you forgot to add to the schema are removed silently. Check the `response` schema for that status code, and remember that `additionalProperties` does not add unknown fields back in for serialization.

## 191: How do you debug a plugin timeout in Fastify?

The error `FST_ERR_PLUGIN_TIMEOUT` means a plugin did not finish loading within `pluginTimeout` (10 seconds by default). Usually a callback-style plugin forgot to call `done()`, an async plugin also takes `done` and never calls it, or the plugin waits for a database that is not reachable. Make plugins either async or callback-style, not both, and add timeouts to connection code inside them.

## 192: How do you debug circular dependencies in NestJS?

Nest shows errors like "A circular dependency between modules" or a dependency at some index is `undefined`. It happens when two modules import each other or two providers inject each other, and it can also come from barrel files (`index.ts`) that import in a loop. The best fix is to move the shared code into a third module. If that is not possible, use `forwardRef` on both sides.

```ts
@Module({ imports: [forwardRef(() => UsersModule)] })
export class OrdersModule {}

constructor(@Inject(forwardRef(() => UsersService)) private users: UsersService) {}
```

## 193: In what order do middleware, guards, interceptors and pipes run in NestJS?

For a request the order is: middleware, guards, interceptors (before the handler), pipes, the route handler, interceptors (after the handler), and exception filters if something throws. Global ones run before controller-level ones, which run before route-level ones. If a guard rejects, pipes and the handler never run, which explains why validation logs never show for unauthorized requests.

## 194: How do you debug exceptions in NestJS with exception filters?

Unknown errors become a generic `500 Internal server error` response, which hides the cause from the client. Add a global filter that logs the full error with the request ID and returns a safe message.

```ts
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  private readonly logger = new Logger("Exceptions");

  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const req = ctx.getRequest();
    const res = ctx.getResponse();
    const status =
      exception instanceof HttpException ? exception.getStatus() : 500;
    this.logger.error(
      `${req.method} ${req.url} failed`,
      (exception as Error)?.stack,
    );
    res.status(status).json({
      statusCode: status,
      message:
        status === 500
          ? "Internal error"
          : (exception as HttpException).message,
    });
  }
}
```

This example uses the Express adapter. With Fastify, the response object is different (`reply.status().send()`).

## 195: How do you debug ValidationPipe problems in NestJS?

Common issues:

- Validation does not run because the pipe is not registered (`app.useGlobalPipes(new ValidationPipe())`).
- Nested objects are not validated without `@ValidateNested()` and `@Type(() => Child)`.
- Numbers from query params stay strings without `transform: true`.
- Unknown fields pass through unless `whitelist: true` is set; `forbidNonWhitelisted: true` returns an error for them.

The `400` response lists the failing constraints, which tells you which decorator rejected the value.

## 196: How do you debug duplicate records caused by retries in a REST API?

When a client or proxy retries a `POST` after a timeout, the first request may have succeeded, so you get two orders. Look for pairs of requests with the same body a few seconds apart in the logs. The fix is idempotency: the client sends an `Idempotency-Key` header, the server stores the key with the result and returns the same result for repeats. A unique constraint in the database is a good last line of defense.

## 197: How do you debug HTTP caching problems?

Check the response headers with `curl -I`: `Cache-Control`, `ETag`, `Last-Modified`, `Vary` and `Age`. An `Age` header or a header like `X-Cache: HIT` means a CDN or proxy served it. Common bugs are user-specific responses cached publicly (missing `private` or `Vary`), old data after a deploy, and `304 Not Modified` responses when the ETag did not change though the data did. Test once directly against the origin and once through the CDN to see where the cached copy comes from.

## 198: How do you debug timeouts between a client and your API?

Find out which layer times out first: the client, a proxy, a load balancer or the app. Each has its own timeout, and the shortest one wins. Compare the client's error with proxy logs (for example a 504 with a request time of exactly 60 seconds points to a proxy timeout) and with app logs (did the request even arrive, and when did it finish?). Then decide if the work should be faster, or moved to a background job with a status endpoint.

## 199: How do you debug GraphQL resolver errors?

Each item in the `errors` array has a `message`, a `path` that shows which field failed (like `["user", "orders", 2, "total"]`), and `extensions` such as an error code. Log errors on the server with the path, operation name and request ID. In Apollo Server, `formatError` lets you log the original error and hide internal details from clients. Stack traces should not be sent to clients in production.

## 200: How do you use DataLoader to fix N+1 and check that it worked?

DataLoader collects all `load(id)` calls made in the same tick and calls your batch function once with all IDs. Create a new loader per request so data is not shared between users.

```js
import DataLoader from 'dataloader';

const createLoaders = () => ({
  user: new DataLoader(async (ids) => {
    const users = await db.user.findMany({ where: { id: { in: ids } } });
    const byId = new Map(users.map((u) => [u.id, u]));
    return ids.map((id) => byId.get(id) ?? null); // same order as ids
  }),
});

// resolver
author: (post, _args, ctx) => ctx.loaders.user.load(post.authorId),
```

To check, count queries per request in the logs or the trace: it should go from N+1 to 2.

## 201: What does "Cannot return null for non-nullable field" mean in GraphQL?

A resolver returned `null` (or threw) for a field marked non-null with `!` in the schema. GraphQL then sets the closest nullable parent to `null`, which can wipe out a large part of the response. Find the field in the error `path`. Then check if the resolver forgot to `await` or `return`, if the data is really missing, or if the field should be nullable in the schema.

## 202: How do you debug webhooks you receive?

- Check the sender's dashboard for delivery attempts, response codes and payloads.
- Log the event ID, type and your response status, and make the handler idempotent because senders retry.
- If signature checks fail, it is often because a body parser changed the raw body. Most providers sign the exact raw bytes.

```js
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  (req, res) => {
    const event = stripe.webhooks.constructEvent(
      req.body,
      req.get("stripe-signature"),
      secret,
    );
    // ...
    res.sendStatus(200);
  },
);
```

For local testing, use the provider's CLI or a tunnel, and replay a saved test event.

## 203: How do you read an EXPLAIN ANALYZE plan in PostgreSQL?

Read it from the innermost (most indented) node outwards. For each node compare the estimated `rows` with the `actual rows`. A big difference means statistics are wrong, so the planner chose a bad plan; run `ANALYZE` on the table. Look for `Seq Scan` on big tables, `Rows Removed by Filter` with large numbers, sorts that spill to disk (`external merge`), and nested loops with many loops. `EXPLAIN (ANALYZE, BUFFERS)` also shows how much data was read from memory or disk.

## 204: How do you find slow queries in PostgreSQL with pg_stat_statements?

`pg_stat_statements` collects stats for each normalized query. Sort by total time to find the queries that cost the most overall.

```sql
SELECT calls,
       round(total_exec_time) AS total_ms,
       round(mean_exec_time, 1) AS mean_ms,
       rows,
       left(query, 120) AS query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

A query with a small mean time but millions of calls can matter more than one slow query. It must be added to `shared_preload_libraries` and created with `CREATE EXTENSION pg_stat_statements`.

## 205: How do you see running queries and locks in PostgreSQL?

```sql
SELECT pid, state, wait_event_type, wait_event,
       now() - query_start AS running_for,
       pg_blocking_pids(pid) AS blocked_by,
       left(query, 100) AS query
FROM pg_stat_activity
WHERE state <> 'idle'
ORDER BY running_for DESC;
```

`blocked_by` shows which session holds the lock. You can stop a query with `pg_cancel_backend(pid)` or close the session with `pg_terminate_backend(pid)`. Be careful: terminating a session rolls back its transaction.

## 206: How do you debug a deadlock in SQL?

A deadlock is when two transactions each hold a lock the other needs. The database kills one of them; in PostgreSQL the error is `deadlock detected` (SQLSTATE `40P01`), and the database log shows both statements. Common causes are updating the same rows in different orders, or long transactions. Fixes: always lock rows in the same order (for example sorted by ID), keep transactions short, and retry the failed transaction in code.

## 207: How do you debug "too many connections" errors?

The database has a connection limit (PostgreSQL `max_connections` is 100 by default). Count your connections: pool size multiplied by the number of app instances, plus workers, cron jobs and migrations. Autoscaling or serverless functions can multiply this fast. Check `pg_stat_activity` grouped by `application_name` or client address to see who uses them. Fixes are smaller pools, a connection pooler like PgBouncer or RDS Proxy, and closing connections that leak.

## 208: What does "idle in transaction" mean and why is it a problem?

The session started a transaction and is not running a query, but has not committed or rolled back. It still holds its locks and blocks vacuum cleanup. It usually comes from app code that opens a transaction and then waits for something slow (like an HTTP call) or forgets to commit on an error path. Set `idle_in_transaction_session_timeout`, and find the code from the last query shown in `pg_stat_activity`.

## 209: How do you debug a query that is fast in dev but slow in production?

Production has more data, a different data distribution, more concurrent load and maybe different indexes or settings. Run `EXPLAIN (ANALYZE, BUFFERS)` against production (or a replica with the same data) and compare the plans. Check that the index exists there, that statistics are up to date, and whether the query waits on locks instead of doing work. Parameter values matter too: a query for a huge customer can use a different plan than one for a small customer.

## 210: How do you debug slow queries and locks in MySQL?

- Turn on the slow query log (`slow_query_log`, `long_query_time`).
- Use `EXPLAIN` or `EXPLAIN ANALYZE` (MySQL 8.0.18+) on slow queries.
- `SHOW FULL PROCESSLIST` lists running queries.
- `SHOW ENGINE INNODB STATUS` shows the latest deadlock.
- `sys.innodb_lock_waits` shows who is waiting for whom.

Error `1205` is a lock wait timeout and `1213` is a deadlock.

## 211: What do Prisma errors P1001 and P2024 mean?

- `P1001`: Prisma cannot reach the database server. Check the host, port, network, security groups, and whether the database is running.
- `P2024`: timed out waiting for a free connection from the pool. All connections are busy, often because of slow queries, long transactions, a small pool, or too many concurrent requests.

For `P2024`, look at query times and pool usage before simply making the pool bigger. With the built-in engine, pool settings are URL parameters like `connection_limit` and `pool_timeout`. With driver adapters (the default in newer Prisma versions), you set the pool in the driver, for example `pg`'s `Pool`.

## 212: How do you debug Prisma connection problems in serverless?

Each function instance creates its own client and pool, so a traffic spike opens many connections and hits the database limit. Create the client once outside the handler so warm calls reuse it, keep the pool per instance small, and put a pooler in front of the database (PgBouncer, RDS Proxy, or Prisma Accelerate). Log connection errors with the function's request ID to see how they line up with concurrency.

## 213: How do you debug Prisma migration drift?

Drift means the database schema does not match what the migration history says. Common causes are manual changes in the database, or migrations edited after they were applied.

```bash
npx prisma migrate status
npx prisma migrate diff --from-config-datasource --to-schema prisma/schema.prisma --script
```

`migrate dev` will offer to reset the dev database. In production never reset. Write a migration that fixes the difference, and use `prisma migrate resolve` to mark a migration as applied or rolled back when you fixed it by hand. The flags of `migrate diff` changed between Prisma versions, so check `--help` for yours.

## 214: How do you debug a Mongoose ValidationError?

The error has an `errors` object with one entry per failed path, each with a `kind` and `message`.

```js
try {
  await User.create(data);
} catch (err) {
  if (err instanceof mongoose.Error.ValidationError) {
    for (const [path, e] of Object.entries(err.errors)) {
      logger.warn({ path, kind: e.kind }, "validation failed");
    }
  }
}
```

Note that update queries like `updateOne` and `findOneAndUpdate` do not run validators unless you pass `runValidators: true`. That explains why invalid data sometimes gets into the database.

## 215: Why does Mongoose populate return null?

Check:

- The `ref` in the schema matches the model name exactly.
- The referenced document still exists (it may be deleted).
- The stored value has the right type, for example an ObjectId and not a string that looks like one.
- Both models are registered on the same connection.
- A `match` option in `populate` may filter it out.

Turn on `mongoose.set('debug', true)` to see the query `populate` sends.

## 216: Why does Mongoose middleware (hooks) not run?

- `pre('save')` runs on `save()` and `create()`, but not on `updateOne`, `findOneAndUpdate` or `insertMany`. Those have their own query or model middleware.
- Hooks must be added to the schema before you call `mongoose.model()`.
- Arrow functions do not get `this`, so use normal functions.
- In query middleware, `this` is the query, not the document.

## 217: How do you use the MongoDB profiler?

The profiler records slow operations into `system.profile`.

```js
db.setProfilingLevel(1, { slowms: 100 }); // log ops slower than 100 ms
db.system.profile.find().sort({ ts: -1 }).limit(5).pretty();
db.setProfilingLevel(0); // turn off
```

Level 2 records everything and adds load, so avoid it in production. MongoDB also writes slow operations to its log by default. MongoDB Atlas has a Query Profiler and Performance Advisor that show the same data without turning on the profiler yourself.

## 218: How do you find long-running operations in MongoDB?

```js
db.currentOp({ active: true, secs_running: { $gte: 5 } });
db.killOp(opid);
```

On newer versions you can also use the `$currentOp` aggregation stage on the `admin` database. Look at the `ns`, the `command`, `secs_running` and whether it is waiting for a lock. Kill operations only when you understand what they are, for example a runaway report query.

## 219: How do you debug a MongoDB duplicate key error E11000?

The error says which index and which value is duplicated, like `E11000 duplicate key error collection: app.users index: email_1 dup key: { email: "..." }`. Usually two requests created the same record at the same time, or a retry repeated an insert. Handle code `11000` in your app and return a conflict. Note that the message contains the actual value, which may be personal data, so be careful logging the raw message. Also, Mongoose's `unique: true` creates an index; it is not a validator.

## 220: How do you debug stale reads in MongoDB?

If you read from secondaries (`readPreference: 'secondary'` or `secondaryPreferred`), a read right after a write can return old data because of replication lag. Check the read preference in the connection string and code, and check replication lag with `rs.printSecondaryReplicationInfo()`. For read-after-write cases, read from the primary, or use a causally consistent session with `majority` read and write concern.

## 221: How do you debug DynamoDB throttling?

Look at CloudWatch metrics for the table and each GSI: `ThrottledRequests`, `ReadThrottleEvents`, `WriteThrottleEvents` and consumed vs provisioned capacity. If total capacity is fine but you still get throttled, you probably have a hot key. A GSI without enough write capacity can also throttle writes to the base table. Turn on CloudWatch Contributor Insights to see the most used keys. In code, log the SDK's retry count (`$metadata.attempts`) to see how often requests are retried.

## 222: How do you debug a DynamoDB TransactionCanceledException?

The whole transaction failed, and the exception has a `CancellationReasons` array with one entry per item in the same order as your request. Each has a `Code` like `None`, `ConditionalCheckFailed`, `TransactionConflict` or `ValidationError`.

```js
try {
  await ddb.send(new TransactWriteItemsCommand(params));
} catch (err) {
  if (err.name === "TransactionCanceledException") {
    logger.warn(
      { reasons: err.CancellationReasons?.map((r) => r.Code) },
      "tx cancelled",
    );
  }
}
```

`TransactionConflict` means another request was changing the same item at the same time, so a retry often works.

## 223: How do you see how much capacity a DynamoDB request uses?

Pass `ReturnConsumedCapacity: 'TOTAL'` (or `'INDEXES'` for per-index detail) and log the result.

```js
const res = await ddb.send(
  new QueryCommand({ ...params, ReturnConsumedCapacity: "TOTAL" }),
);
logger.info(
  {
    rcu: res.ConsumedCapacity?.CapacityUnits,
    count: res.Count,
    scanned: res.ScannedCount,
  },
  "query",
);
```

If `ScannedCount` is much bigger than `Count`, a `FilterExpression` is throwing away most items after reading them, and you pay for all of them. A `Scan` reads the whole table, so it is often the cause of high cost and throttling.

## 224: How do you debug Redis latency?

First check if it is Redis or the client:

```bash
redis-cli --latency -h my-redis          # round trip from this machine
redis-cli SLOWLOG GET 20                  # slow commands inside Redis
redis-cli INFO commandstats               # time per command type
```

If Redis is fast but the app sees slow calls, the app's own event loop may be blocked, or the network is slow. Inside Redis, look for heavy commands on big keys, `KEYS`, Lua scripts, and fork time for persistence (`latest_fork_usec` in `INFO stats`). `LATENCY DOCTOR` gives a summary if `latency-monitor-threshold` is set.

## 225: How do you find big keys and memory use in Redis?

```bash
redis-cli --bigkeys          # biggest key per type, by element count
redis-cli --memkeys          # biggest keys by memory
redis-cli MEMORY USAGE user:42:feed
redis-cli INFO memory
```

These tools use `SCAN`, so they are safe-ish to run, but they still add load, so run them off-peak or on a replica. In `INFO memory`, a high `mem_fragmentation_ratio` means Redis uses much more RAM than its data needs.

## 226: How do you debug Redis OOM errors?

`OOM command not allowed when used memory > 'maxmemory'` means Redis hit its memory limit and the eviction policy does not allow it to free space (for example `noeviction`). Check `INFO memory` and `INFO keyspace`: if many keys have no expiry, something is writing keys without a TTL. Find large or fast-growing key patterns with `--bigkeys`. For a cache, use an eviction policy like `allkeys-lru`. For queues like BullMQ, keep `noeviction` and add memory instead.

## 227: How do you check consumer group lag and partition assignment in Kafka?

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --describe --group orders-service
```

The output shows each partition with `CURRENT-OFFSET`, `LOG-END-OFFSET`, `LAG` and which consumer owns it. Lag on only one partition points to a hot key or a stuck consumer. No consumer IDs means no members are running. Lag on all partitions means consumers are too slow overall.

## 228: How do you debug frequent consumer rebalances in Kafka?

Rebalances stop consumption, so frequent ones show up as lag and duplicate messages. Common causes:

- Processing one poll's messages takes longer than `max.poll.interval.ms`, so the consumer is kicked out.
- Heartbeats are missed (`session.timeout.ms`), for example because of a blocked event loop or long GC.
- Pods restart or scale up and down often, or a rolling deploy restarts every member.

Look at consumer logs for "rebalancing" messages and their timing. Process less per poll, make processing faster, or use static membership (`group.instance.id`). Kafka 4.0 also brings the new consumer group protocol (KIP-848), which makes rebalances less disruptive.

## 229: How do you debug message ordering problems in Kafka?

Kafka only keeps order inside one partition. Check that related messages use the same key so they go to the same partition. Changing the number of partitions changes which partition a key goes to. On the consumer side, processing messages in parallel (for example with `Promise.all` over a batch) breaks the order even if Kafka delivered it in order. On the producer side, keep idempotence on so retries do not reorder messages.

## 230: How do you debug duplicate message processing in Kafka?

Duplicates are normal with at-least-once delivery. They happen when a consumer processes a message but crashes or gets rebalanced before committing the offset, or when a producer retries without idempotence. Log the topic, partition and offset with every processed message, then look for the same offset processed twice. Fix it with idempotent handlers (for example a processed-messages table keyed by a message ID). Commit offsets after processing, not before.

## 231: How do you debug a Kafka producer that fails to send?

Read the error code:

- `MESSAGE_TOO_LARGE` / `RecordTooLargeException`: the message is bigger than the broker or topic allows (about 1 MB by default).
- `NOT_ENOUGH_REPLICAS`: with `acks=all`, fewer in-sync replicas are available than `min.insync.replicas`.
- `UNKNOWN_TOPIC_OR_PARTITION`: the topic does not exist and auto-create is off.
- Auth or SASL errors: wrong credentials or ACLs.

If the client connects to the bootstrap server but then fails or times out, check `advertised.listeners` on the broker. The broker may tell clients to use an internal hostname they cannot reach, which is a classic problem with Kafka in Docker.

## 232: How do you replay messages in Kafka for debugging?

Reset the consumer group's offsets. The group must have no active members while you do it.

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group orders-service --topic orders \
  --reset-offsets --to-datetime 2026-11-01T10:00:00.000 --dry-run

# then replace --dry-run with --execute
```

Other options are `--to-earliest`, `--to-offset` and `--shift-by`. Replaying sends the messages to your real handlers again, so make sure they are idempotent. For pure inspection, use a separate debug group or the console consumer.

## 233: How do you debug messages piling up as unacked in RabbitMQ?

The consumer received messages but did not ack them. Check that every code path acks or nacks, including errors. An exception before `channel.ack(msg)` leaves the message unacked until the channel closes.

```js
channel.consume("orders", async (msg) => {
  try {
    await handle(JSON.parse(msg.content.toString()));
    channel.ack(msg);
  } catch (err) {
    logger.error({ err }, "failed");
    channel.nack(msg, false, false); // send to dead letter exchange, no requeue
  }
});
```

Acking on a different channel than the one that received the message gives `PRECONDITION_FAILED - unknown delivery tag` and closes the channel.

## 234: How does prefetch affect RabbitMQ consumers?

Prefetch (`channel.prefetch(n)`) limits how many unacked messages a consumer can hold. Without it, RabbitMQ pushes as many messages as it can, so one consumer can take everything while others stay idle, and memory grows. With prefetch 1, throughput can be low because the consumer waits for each round trip. If one consumer is busy and others idle, or memory grows on consumers, check prefetch first. A value around 10 to 50 is a common starting point.

## 235: How do you debug PRECONDITION_FAILED errors in RabbitMQ?

The most common one is `inequivalent arg` when you declare a queue or exchange that already exists with different settings, like `durable`, `x-queue-type` or `x-dead-letter-exchange`. RabbitMQ does not change an existing queue, it closes the channel. Compare the arguments in code with the existing queue in the management UI. To change them, create a new queue or delete and recreate the old one (or use policies for settings that allow it).

## 236: How do you debug messages that disappear in RabbitMQ?

If a message is published to an exchange and no binding matches its routing key, RabbitMQ drops it silently. Check the bindings in the management UI and the exact routing key. Publish with the `mandatory` flag to get unroutable messages returned, or set an alternate exchange to catch them. Use publisher confirms so you know the broker really accepted the message.

```js
const ch = await conn.createConfirmChannel();
ch.publish("orders", "order.created", Buffer.from(body), { mandatory: true });
ch.on("return", (msg) =>
  logger.warn({ key: msg.fields.routingKey }, "unroutable"),
);
await ch.waitForConfirms();
```

## 237: How do you debug a blocked publisher in RabbitMQ?

When RabbitMQ hits its memory high watermark or disk free limit, it raises an alarm and blocks connections that publish. Publishers then hang without an error. Check with `rabbitmq-diagnostics alarms` or the management UI. In `amqplib`, listen for the `blocked` and `unblocked` events on the connection and log them. The fix is to drain queues (start consumers, fix the stuck ones), add resources, or limit queue length.

## 238: How do you debug BullMQ jobs stuck in waiting?

Check:

- A worker is running for that exact queue name, with the same Redis and the same `prefix`.
- The queue is not paused (`await queue.isPaused()`).
- All worker slots are not taken by stuck active jobs.
- A rate limiter is not holding jobs back.
- The jobs are not in `delayed` or `prioritized` instead of `waiting`.

```js
console.log(
  await queue.getJobCounts(
    "waiting",
    "active",
    "delayed",
    "prioritized",
    "failed",
    "paused",
  ),
);
```

## 239: Why does BullMQ require maxRetriesPerRequest: null?

Workers use blocking Redis commands to wait for jobs. With the ioredis default (20 retries per request), a short Redis outage makes those commands fail with a retry error and the worker stops working properly. BullMQ requires `maxRetriesPerRequest: null` on worker connections and throws an error if it is missing, so ioredis keeps retrying until Redis is back.

```js
import IORedis from "ioredis";
const connection = new IORedis(process.env.REDIS_URL, {
  maxRetriesPerRequest: null,
});
const worker = new Worker("emails", processor, { connection });
```

## 240: How do you add logs and progress to BullMQ jobs?

Use `job.log()` to save log lines on the job itself, and `job.updateProgress()` to show progress. Both show up in UIs like Bull Board, which is handy when many workers run in different pods.

```js
const worker = new Worker(
  "reports",
  async (job) => {
    await job.log(`starting report ${job.data.reportId}`);
    for (let i = 0; i < 10; i++) {
      await processChunk(job.data, i);
      await job.updateProgress((i + 1) * 10);
    }
  },
  { connection },
);

const { logs } = await queue.getJobLogs(jobId);
```

Do not put personal data or secrets in job data or job logs, since they are stored in Redis and shown in UIs.

## 241: How do you add OpenTelemetry tracing to a Node.js service?

Load the SDK before any other code, so the instrumentations can patch modules like `http`, `express` and `pg`.

```js
// instrumentation.js
const { NodeSDK } = require("@opentelemetry/sdk-node");
const {
  getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");
const {
  OTLPTraceExporter,
} = require("@opentelemetry/exporter-trace-otlp-http");

const sdk = new NodeSDK({
  serviceName: "orders-api",
  traceExporter: new OTLPTraceExporter(), // uses OTEL_EXPORTER_OTLP_ENDPOINT
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start();
```

```bash
node --require ./instrumentation.js server.js
```

If no spans show up, check that it loads first, that the exporter endpoint is reachable, and the sampler settings. ES module apps need extra loader setup, so follow the OpenTelemetry docs for ESM.

## 242: How do you connect logs with traces?

Add the trace ID and span ID to every log line. The OpenTelemetry instrumentations for Pino and Winston do this for you. You can also do it by hand:

```js
import { trace } from "@opentelemetry/api";

function withTrace(fields = {}) {
  const ctx = trace.getActiveSpan()?.spanContext();
  return ctx
    ? { ...fields, trace_id: ctx.traceId, span_id: ctx.spanId }
    : fields;
}
logger.info(withTrace({ orderId }), "order saved");
```

Then from a slow trace you can open its logs, and from an error log you can open its trace.

## 243: How do you find which service is slow in a request chain?

Open a trace of a slow request and look at the waterfall. Find the longest spans on the critical path, the chain of spans the request had to wait for. Gaps between spans with no child spans usually mean time in code that is not instrumented, waiting for a pool connection, or queueing. Compare with a trace of a fast request for the same endpoint to see which span is different.

## 244: How do you debug a retry storm?

A retry storm happens when many clients retry a failing service at the same time, adding more load to a service that is already struggling. Signs are request rate going up while user traffic is flat, and many repeated requests in the logs. Retries at several layers multiply: 3 retries in each of 3 layers is up to 27 calls for one request. Retry at one layer only, use exponential backoff with jitter, cap the number of retries, and use a retry budget or circuit breaker.

## 245: How do you debug timeouts that do not fit together across services?

If service A waits 5 seconds for B, but B waits 10 seconds for C, A gives up while B is still working. B's work is wasted and may even finish after A has retried. Map out the timeouts of every hop. Each caller's timeout should be longer than what it calls, plus some margin. Better still, pass a deadline down the chain (gRPC does this with deadlines) so each service knows how much time is left.

## 246: How do you debug DNS and service discovery problems between services?

From inside the calling container, check that the name resolves and the port answers:

```bash
nslookup orders.default.svc.cluster.local
wget -qO- http://orders.default.svc.cluster.local:8080/health
```

`ENOTFOUND` means the name does not resolve (wrong name, wrong namespace, DNS down). `EAI_AGAIN` is a temporary DNS failure, often under load. Keep-alive connections can keep using an old IP after a target moved, which looks like random failures after deploys. In Kubernetes, `ndots:5` in `resolv.conf` causes several lookups for short names, which adds latency.

## 247: Why should you look at p95 and p99 latency instead of averages?

The average hides slow requests. If 98% of requests take 50 ms and 2% take 5 seconds, the average looks fine at about 150 ms, but many users see 5 seconds. Percentiles show this: p99 is the time that 99% of requests are faster than. Also, a page that makes many backend calls is likely to hit at least one slow one, so tail latency affects most users.

## 248: How can trace sampling hide bugs?

Most systems keep only a small share of traces, for example 1%, decided at the start of the request (head sampling). A rare error may then never be in any saved trace. Tail sampling decides after the request is done, so you can keep all errors and slow requests, and only sample the normal ones. The OpenTelemetry Collector supports tail sampling. Also, logs and metrics should not be sampled the same way, so you still have the counts.

## 249: How do you debug a problem that affects only one instance or pod?

Break down your metrics by instance (pod, host, zone) instead of looking at the total. One instance with high errors or latency points to a local problem: a bad node, a full disk, a memory leak in that process, a stuck connection, or a different version after a half-finished deploy. Compare its config and version with a healthy instance. Taking it out of the load balancer (instead of restarting it) keeps its state for investigation while users stop being affected.

## 250: How do you trace a request through a message queue?

HTTP instrumentation passes trace context in headers, but for queues you must put it in the message headers. Many instrumentations (Kafka, RabbitMQ) do this automatically. Otherwise do it by hand with the OpenTelemetry propagation API.

```js
import { context, propagation } from "@opentelemetry/api";

// producer
const headers = {};
propagation.inject(context.active(), headers);
await producer.send({ topic: "orders", messages: [{ value, headers }] });

// consumer
const parentCtx = propagation.extract(
  context.active(),
  toStringHeaders(message.headers),
);
await context.with(parentCtx, () => handle(message));
```

Here `toStringHeaders` is your helper that converts Kafka's Buffer header values to strings. Then the trace shows the consumer's work under the original request, even if it ran minutes later.

## 251: How do you debug a circuit breaker that stays open?

Log every state change of the breaker (closed, open, half-open) with the reason, and expose its state as a metric. Then check whether the downstream service is really still failing, or whether the breaker settings are too strict: too low an error threshold, too few requests in the window so a few errors trip it, or a half-open test request that always fails because of a short timeout. Also check what counts as a failure. Treating `404` or validation errors as failures can keep it open even when the service is healthy.

## 252: How do you debug data that does not match across services in an eventually consistent system?

Follow one entity's history across services using its ID: which events were published, which were consumed, in what order and when. Common causes are lost events (published outside the database transaction), events processed out of order, duplicates applied twice, or a failed step in a saga whose compensation never ran. The outbox pattern, idempotent handlers and a version number on each entity make these bugs easier to prevent and to spot.

## 253: How do you debug a container that has no shell, such as a distroless image?

In Kubernetes, add an ephemeral debug container to the running pod. With `--target` it shares the process namespace of your app container, so you can see its processes.

```bash
kubectl debug -it my-pod --image=busybox:1.36 --target=api
# or debug a copy of the pod, so the real one is not touched
kubectl debug my-pod -it --copy-to=my-pod-debug --container=debug --image=busybox:1.36
```

With plain Docker, run a tool container in the same network and PID namespace: `docker run -it --network container:my-api --pid container:my-api busybox`.

## 254: Why does a Node.js container take a long time to stop or lose requests on deploy?

Docker and Kubernetes send `SIGTERM`, wait (10 seconds in Docker, 30 seconds by default in Kubernetes), then send `SIGKILL`. If Node runs as PID 1 without a `SIGTERM` handler, the signal is ignored, so it is killed after the wait. If `npm start` is PID 1, it may not pass the signal on to Node. Run `node` directly (or use `--init` / tini), and handle `SIGTERM` by stopping new requests and finishing current ones.

```js
process.on("SIGTERM", () => {
  server.close(async () => {
    await db.$disconnect();
    process.exit(0);
  });
});
```

## 255: How do you debug a Node.js app that gets OOM killed in a container?

If the container is killed with `OOMKilled` (exit 137) but there is no "heap out of memory" error, the total process memory went over the container limit before V8 hit its heap limit. V8's heap limit and the container limit are separate. Set `--max-old-space-size` to about 70-80% of the container memory so Node fails with a clear heap error first, and leave room for Buffers and native memory. Then watch `rss` and `heapUsed` over time to see whether it is a leak or just too small a limit.

## 256: How do you use Kubernetes events for debugging?

Events show what Kubernetes did and why: scheduling, pulling images, probe failures, OOM kills, scaling.

```bash
kubectl get events -n my-ns --sort-by=.lastTimestamp
kubectl get events -n my-ns --field-selector involvedObject.name=my-pod
```

Events are only kept for a short time (one hour by default), so look early or ship them to your logging system.

## 257: How do you debug a Kubernetes Service that does not send traffic to pods?

1. Check that the Service selector matches the pod labels exactly.
2. Check the endpoints: `kubectl get endpointslices -l kubernetes.io/service-name=my-svc`. Empty means no ready pods match.
3. Check that pods are Ready, since pods failing readiness are left out.
4. Check that `targetPort` matches the port the container listens on.
5. Test from another pod with `wget` or `curl` to the Service name.

A NetworkPolicy can also block traffic even when all of the above is right.

## 258: How do CPU limits cause slow responses in Kubernetes?

With a CPU limit, the container gets a fixed amount of CPU time per short period. If it uses it up (for example during a GC pause or a burst of requests), it is throttled until the next period, which adds latency spikes even when average CPU looks low. Check the `container_cpu_cfs_throttled_periods_total` metric. Options are raising or removing the CPU limit (keeping a request), or doing less CPU work per request.

## 259: How do you check and undo a bad rollout in Kubernetes?

```bash
kubectl rollout status deploy/my-api
kubectl rollout history deploy/my-api
kubectl rollout undo deploy/my-api                 # back to the previous revision
kubectl rollout undo deploy/my-api --to-revision=3
```

If the rollout is stuck, the new pods are usually failing readiness or not scheduling, so look at the new ReplicaSet's pods. If you use GitOps (Argo CD, Flux), roll back in Git, or the tool will put the bad version back.

## 260: What causes a 504 Gateway Timeout from Nginx and how do you fix it?

Nginx waited longer than `proxy_read_timeout` (60 seconds by default) for the app to send a response. The error log says `upstream timed out (110: Connection timed out) while reading response header from upstream`. First find out why the app is slow, using its logs and traces. Raise the timeout only for endpoints that really need it, and move long work to background jobs.

```nginx
location /reports/ {
    proxy_read_timeout 120s;
    proxy_pass http://app;
}
```

## 261: How does a trailing slash in proxy_pass change the request path in Nginx?

If `proxy_pass` has a URI part (even just `/`), Nginx replaces the matched `location` prefix with it. Without it, the original path is passed as is.

```nginx
location /api/ {
    proxy_pass http://app;    # /api/users -> http://app/api/users
}
location /api/ {
    proxy_pass http://app/;   # /api/users -> http://app/users
}
```

This one character is a common cause of 404s after adding a proxy. Log the upstream path in the app to confirm what it receives.

## 262: How do you log upstream timing in Nginx?

Add upstream variables to the access log format. They show whether time was spent in Nginx, connecting to the app, or waiting for the app.

```nginx
log_format timed '$remote_addr "$request" $status '
                 'rt=$request_time uct=$upstream_connect_time '
                 'uht=$upstream_header_time urt=$upstream_response_time '
                 'ua=$upstream_addr us=$upstream_status';
access_log /var/log/nginx/access.log timed;
```

If `$request_time` is much bigger than `$upstream_response_time`, the time is spent sending to a slow client, not in your app.

## 263: Why do you get random 502 errors behind a load balancer with Node.js?

Often it is a keep-alive mismatch. Node's HTTP server closes idle keep-alive connections after 5 seconds by default (`server.keepAliveTimeout`). Many load balancers keep idle connections longer, for example 60 seconds for an AWS ALB. The load balancer sends a request on a connection that Node is just closing, and returns 502. Make Node's timeout longer than the load balancer's.

```js
const server = app.listen(3000);
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000; // must be larger than keepAliveTimeout
```

## 264: How do you read the Lambda REPORT log line?

At the end of each invocation Lambda writes a line like:

```
REPORT RequestId: 3f1c... Duration: 812.40 ms Billed Duration: 813 ms Memory Size: 512 MB Max Memory Used: 498 MB Init Duration: 640.11 ms
```

`Init Duration` appears only on cold starts. `Max Memory Used` close to `Memory Size` means you are near the limit. A `Duration` close to the configured timeout means the function is almost timing out. Search by `RequestId` to get all log lines of that invocation.

## 265: How do you debug Lambda timeouts?

The log shows `Task timed out after X seconds`. The default timeout is only 3 seconds. Common causes are a slow downstream call without its own timeout, a cold start doing heavy init, and a function in a VPC trying to reach the internet or an AWS service without a NAT gateway or VPC endpoint (the call just hangs). Set client timeouts shorter than the function timeout and log `context.getRemainingTimeInMillis()` before slow calls.

## 266: How do you get a shell in a running ECS task?

Use ECS Exec. The service must have `enableExecuteCommand` turned on and the task role must allow the SSM messages actions.

```bash
aws ecs execute-command --cluster prod --task <task-id> \
  --container api --interactive --command "sh"
```

ECS Exec can log sessions to CloudWatch or S3, which you should turn on in production so there is an audit trail of what was run.

## 267: How do you debug an AWS SDK call that fails?

Log the error name, message, HTTP status and request ID from `$metadata`. AWS support needs the request ID, and it links to CloudTrail.

```js
try {
  await s3.send(new GetObjectCommand({ Bucket, Key }));
} catch (err) {
  logger.error(
    {
      name: err.name,
      status: err.$metadata?.httpStatusCode,
      requestId: err.$metadata?.requestId,
      attempts: err.$metadata?.attempts,
    },
    "s3 get failed",
  );
}
```

For the CLI, `--debug` prints the full request flow, including which credentials provider was used. The output includes signed headers, so do not share it.

## 268: How do you see live logs for Azure App Service and Container Apps?

```bash
az webapp log tail --name my-api --resource-group my-rg
az containerapp logs show --name my-api --resource-group my-rg --follow
```

For App Service you must turn on application logging first. The Kudu console (`https://<app>.scm.azurewebsites.net`) gives you files, process info and a shell. For older data, query the Log Analytics workspace with KQL.

## 269: How do you debug a Cloud Run service on GCP?

Read the logs for the service and revision:

```bash
gcloud logging read \
  'resource.type="cloud_run_revision" AND resource.labels.service_name="orders" AND severity>=ERROR' \
  --limit 50
```

Common problems: the container must listen on the port in the `PORT` env var (8080 by default), or the revision fails to start. With request-based billing, CPU is throttled outside of requests, so background work after sending the response may stall. Check the revision settings and whether a new revision is getting traffic.

## 270: How do you find drift between Terraform state and real infrastructure?

Run a refresh-only plan. It shows what changed outside Terraform, without proposing changes to match your code.

```bash
terraform plan -refresh-only
```

If the change outside Terraform was correct, update your code to match. If not, a normal `apply` puts it back. Someone editing resources in the cloud console is the usual cause, so limit console write access in production.

## 271: How do you inspect Terraform state and expressions?

```bash
terraform state list
terraform state show aws_db_instance.main
terraform output
terraform console     # evaluate expressions, e.g. local.subnets
```

`terraform console` is useful to see what a complex expression or a `for` loop really produces. Remember that state holds attribute values in plain text, including passwords, so `state show` output can contain secrets.

## 272: How do you debug "resource already exists" errors in Terraform?

The resource exists in the cloud but not in Terraform state, for example it was created by hand or by another state. Do not delete it. Import it with an `import` block (Terraform 1.5+), then run plan to check that your code matches.

```hcl
import {
  to = aws_s3_bucket.logs
  id = "my-company-logs"
}
```

`terraform plan -generate-config-out=generated.tf` can write a first version of the resource code for you.

## 273: Why are secrets empty in GitHub Actions for pull requests from forks?

For security, workflows triggered by `pull_request` from a fork do not get repository secrets, and `GITHUB_TOKEN` is read-only. So steps that need secrets fail only for outside contributors. Do not switch to `pull_request_target` and check out the PR code to "fix" this, because that runs untrusted code with your secrets. Split the workflow: test without secrets, and run steps that need secrets only after a maintainer approves or after merge.

## 274: How do you debug "Resource not accessible by integration" in GitHub Actions?

The `GITHUB_TOKEN` does not have the permission the step needs. The default may be read-only for the repo or org. Add only the permissions the job needs:

```yaml
permissions:
  contents: read
  pull-requests: write # comment on PRs
  id-token: write # OIDC login to a cloud provider
```

Setting `permissions` at all removes the permissions you did not list, so a job can lose access it had before.

## 275: How do you debug cache and artifact problems in GitHub Actions?

For caches, print the cache key and the `cache-hit` output to see if it was restored. A key that never changes restores old dependencies, and a key that always changes never hits. To get files out of a failed job, upload them as artifacts only on failure:

```yaml
- uses: actions/upload-artifact@v4
  if: failure()
  with:
    name: test-logs
    path: |
      test-results/
      logs/
    retention-days: 7
```

Check what goes into artifacts, since anyone with read access to the repo can download them.

## 276: How do you debug networking between containers in Docker Compose?

Services in the same Compose project share a network and reach each other by service name, not by `localhost`. Check the name and the container port (not the published host port). Use `depends_on` with a `condition: service_healthy` health check if the app starts before the database is ready.

```bash
docker compose exec api sh -c "nc -zv db 5432"
docker compose ps
docker network inspect myproject_default
```

## 277: How do you debug a CORS preflight failure?

Look at the `OPTIONS` request in the browser's Network tab. It must return a 2xx status with `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers` that cover the real request. Common causes: the auth middleware rejects `OPTIONS` with 401, a custom header is not in the allowed headers, or `Access-Control-Allow-Origin: *` is used together with credentials. Also, if your API returns a 500 without CORS headers, the browser shows a CORS error that hides the real error, so check the server logs too.

## 278: How do you debug a CSRF token mismatch?

The token in the request does not match the one stored for the session. Check that the session cookie is really sent (`SameSite`, `Secure`, domain), that all instances use a shared session store, that the token comes from the same session (not a cached page), and that the client sends it in the header or field the server reads. Log whether the session exists and whether a token was present, never the token values.

## 279: Why does a rate limiter block many users at once?

The limiter probably keys on the wrong IP. Behind a proxy without `trust proxy`, every request has the proxy's IP, so all users share one limit. With `trust proxy` set to `true`, attackers can fake `X-Forwarded-For` to get around the limit. Set the correct number of trusted proxies and log `req.ip` together with the raw header for a few requests to check. With several app instances, the limiter also needs a shared store like Redis, or each instance counts separately.

## 280: How do you debug a JWT rejected because of audience or issuer?

The token's `aud` or `iss` claim does not match what the API expects. Decode the token and compare with the server config. Common causes are a token for another API, a different environment (staging issuer against production), or a trailing slash difference in the issuer URL. `jose` throws `JWTClaimValidationFailed` with a `claim` field, and `jsonwebtoken` says something like `jwt audience invalid`.

```js
await jwtVerify(token, JWKS, {
  issuer: "https://auth.example.com/",
  audience: "orders-api",
});
```

## 281: How do you debug JWKS and key rotation errors?

When the identity provider rotates keys, tokens are signed with a new `kid`. If your service caches the old key set and does not refresh it, verification fails with "no matching key". `jose`'s `createRemoteJWKSet` refetches the key set when it sees an unknown `kid` (with a cooldown). Check the token's `kid`, compare it with the provider's JWKS URL, and make sure the service can reach that URL from its network.

## 282: Why is the Authorization header missing on the server?

- A proxy, API gateway or load balancer drops or renames it.
- A redirect to another origin: `fetch` removes `Authorization` when it follows a cross-origin redirect, for example `http` to `https` or a missing trailing slash redirect to another host.
- CORS: the browser will not send it if `Authorization` is not in `Access-Control-Allow-Headers`.
- The client sends `Bearer` without a space or with the wrong case of the header name in some custom code.

Log whether the header is present (`Boolean(req.headers.authorization)`), not its value, at each layer you control.

## 283: How do you debug random logouts with refresh tokens?

If refresh tokens rotate (each refresh gives a new one and the old one stops working), two requests that refresh at the same time will race. The second uses an already used token, and reuse detection may log the user out. Look for two refresh calls within milliseconds for the same user. Fix it on the client by allowing only one refresh at a time, and consider a short grace period on the server for the previous token.

## 284: How do you debug common OAuth errors like redirect_uri_mismatch and invalid_grant?

- `redirect_uri_mismatch`: the redirect URI in the request does not exactly match a registered one (scheme, host, port, path, trailing slash).
- `invalid_grant`: the authorization code was already used, expired, belongs to another client, or the PKCE `code_verifier` does not match. Retries that reuse the same code cause this often.
- `invalid_client`: wrong client ID or secret, or wrong auth method.

Read the `error_description` from the provider, and never log the code, tokens or client secret.

## 285: Why does TLS work in the browser but fail in Node.js?

Often the server does not send its intermediate certificate. Browsers can fill the gap using cached intermediates or by downloading them, but Node, curl and most server clients cannot, so they fail with `UNABLE_TO_VERIFY_LEAF_SIGNATURE`. Check with `openssl s_client -showcerts`: if only one certificate is sent, configure the server with the full chain (for example `fullchain.pem` with Let's Encrypt).

## 286: How do you make Node.js trust a private or company CA?

Point `NODE_EXTRA_CA_CERTS` to a PEM file with the CA. It is read once when the process starts, so set it before Node runs.

```bash
NODE_EXTRA_CA_CERTS=/etc/ssl/certs/company-ca.pem node server.js
```

For one client only, pass `ca` in the TLS options. Newer Node versions also have `--use-system-ca` to use the operating system's trust store. All of these are better than turning off verification.

## 287: What does ERR_TLS_CERT_ALTNAME_INVALID mean?

The host name you connected to is not in the certificate's Subject Alternative Names. It happens when you connect by IP address, by an internal name, or by a name the certificate does not list. A wildcard like `*.example.com` covers `api.example.com` but not `example.com` or `a.b.example.com`. Connect with a name in the certificate, or get a certificate that includes the name you use.

```bash
openssl s_client -connect 10.0.1.5:443 -servername api.example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```

## 288: How do you debug TLS errors when connecting to a database?

Check whether the database requires TLS and what the driver does by default. For PostgreSQL, `sslmode=verify-full` checks both the CA and the host name, and you usually need the provider's CA bundle (for example the AWS RDS bundle).

```js
import fs from "node:fs";
import pg from "pg";

const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { ca: fs.readFileSync("/certs/rds-global-bundle.pem", "utf8") },
});
```

Errors after a provider rotates its CA usually mean you are using an old bundle. Note that drivers do not always read `sslmode` the same way `libpq` does, so check your driver's docs.

## 289: How do you debug mutual TLS (mTLS) errors?

In mTLS the server also checks the client's certificate. Errors like `certificate required`, `unknown ca` or `bad certificate` usually mean the client did not send a certificate, the server does not trust the client's CA, or the client certificate has expired. Test with openssl:

```bash
openssl s_client -connect api.internal:443 -cert client.pem -key client.key -CAfile ca.pem
```

In a Node server, `req.socket.authorized` and `req.socket.authorizationError` tell you why a client was rejected.

## 290: How do you check that a certificate and private key match?

Compare the hash of the public key from each. If they differ, the server fails to start or the handshake fails.

```bash
openssl x509 -in cert.pem -noout -pubkey | openssl sha256
openssl pkey -in key.pem -pubout | openssl sha256
openssl x509 -in cert.pem -noout -subject -issuer -dates -ext subjectAltName
```

Never paste private keys into tickets or online tools to check them.

## 291: Why can logging an HTTP client error leak a token?

Some error objects carry the full request. An `AxiosError`, for example, has `config` with all request headers, including `Authorization`, and logging the whole object (or calling `toJSON()`) writes the token to the log. Log only the fields you need:

```js
catch (err) {
  logger.error({
    message: err.message,
    code: err.code,
    status: err.response?.status,
    url: err.config?.url,
  }, 'upstream call failed');
}
```

Also check what your error serializer includes, and add redact paths like `err.config.headers.Authorization` as a backup.

## 292: How do you keep personal data out of error tracking tools like Sentry?

Keep `sendDefaultPii` off (it is off by default), scrub fields in `beforeSend`, and turn on server-side data scrubbing in the tool.

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

Also watch error messages themselves, since `Invalid email: anna@example.com` puts the email into the tool.

## 293: How do you log request and response bodies safely when you need them?

Do not log bodies by default. When you need them to debug, log them only for chosen routes, only for a short time, and only after masking fields with an allowlist (log only the fields you named) instead of a blocklist (hide fields you thought of). Cut long values, skip binary uploads, and never log bodies of auth, payment or profile endpoints. Remove the extra logging when you are done.

## 294: How do you turn on debug logs for one user or one request without flooding production?

Use a feature flag or a signed debug header that only internal staff can set. When it is on, create a child logger at `debug` level for that request only.

```js
app.use((req, res, next) => {
  const debugOn = flags.isEnabled("debug-logs", { userId: req.user?.id });
  req.log = logger.child(
    { requestId: req.id },
    { level: debugOn ? "debug" : "info" },
  );
  next();
});
```

The debug logs still follow the same redaction rules, and the flag should turn itself off after some time.

## 295: How do you run queries against a production database safely while debugging?

Use a read replica if you have one, a read-only database user, and a statement timeout so a bad query cannot run for long.

```sql
SET statement_timeout = '5s';
BEGIN TRANSACTION READ ONLY;
SELECT status, count(*) FROM orders WHERE created_at > now() - interval '1 hour' GROUP BY status;
COMMIT;
```

Select only the columns you need instead of `SELECT *`, so you see less personal data. Write changes go through a reviewed script, not ad hoc commands.

## 296: How do you share logs in a ticket or chat safely?

Share links to the log system or the request and trace IDs, so access control still applies. If you paste lines, remove tokens, cookies, emails, names, IP addresses and anything from request bodies first. Chat and ticket tools are often searchable by many people and kept forever, so treat them as public inside the company.

## 297: Who should be able to read production logs, and for how long should logs be kept?

Give access only to people who need it for their job, and log who searched what in the log system. Keep logs only as long as you need them for debugging, security and legal reasons, for example 14 to 30 days for app logs, and longer for audit logs. Personal data laws such as GDPR expect a clear retention period and the ability to delete data, which is much easier if logs contain IDs instead of personal details.

## 298: How can secrets leak in CI/CD logs even when they are masked?

- `set -x` in shell scripts prints commands with expanded variables.
- Printing `env` or a whole config object.
- Tools that print their config in verbose mode.
- Secrets passed as Docker `--build-arg` stay in the image history.
- A secret written to a file that is then uploaded as an artifact.

For Docker builds use BuildKit secrets instead of build args:

```bash
docker build --secret id=npm,src=$HOME/.npmrc -t my-api .
# Dockerfile: RUN --mount=type=secret,id=npm,target=/root/.npmrc npm ci
```

## 299: How do you debug with production data without exposing personal data?

Do not copy production data to dev machines as is. Use an anonymized copy where names, emails, phone numbers and addresses are replaced by fake values, while IDs, sizes and relations stay real so the bug still shows. Often you only need the shape of the data, like the number of rows or a specific edge case, which you can recreate with made-up values. If you really need real data, look at it in production with controlled, audited access.

## 300: How do you change the log level of a running service without restarting it?

Restarting can clear the state you want to see. Let the service change its level at runtime, for example from a config value it reloads, an admin endpoint protected by auth, or a signal.

```js
process.on("SIGUSR2", () => {
  logger.level = logger.level === "debug" ? "info" : "debug";
  logger.info({ level: logger.level }, "log level changed");
});
```

Note that `SIGUSR1` is used by Node for the inspector, so use another signal. Set a reminder or a timer to switch the level back.

# Advanced Questions (301-450)

## 301: After a deploy, p99 latency doubled but there are no errors. How do you investigate?

1. Confirm the timing lines up with the deploy and check if all endpoints or only some got slower.
2. Compare traces of the same endpoint before and after: find the span that grew.
3. Check the diff for new queries, removed indexes, new sync code, bigger payloads, new middleware, or a changed dependency version.
4. Check resource metrics: event loop delay, GC time, CPU throttling, pool wait time.
5. If it is clear the deploy caused it and users are affected, roll back first, then reproduce under load in staging.

No errors usually means something waits longer, not something fails, so look at waiting: pools, locks, the event loop and downstream calls.

## 302: Errors spike at the same minute every hour. What do you check?

Something scheduled is the likely cause. Check cron jobs and scheduled tasks (reports, cleanups, backups), cache entries that all expire at the same time because they were set together, tokens or credentials with a one-hour lifetime that are refreshed late, log rotation, and batch jobs in other teams that share the database. Line up the spike with the scheduler logs. Fixes often include adding random jitter to TTLs and schedules, and refreshing tokens before they expire.

## 303: A service works fine at normal traffic but falls over at peak. How do you debug it?

Latency rises slowly until a resource is almost full, then it jumps, because requests start queueing. Find which resource fills first: DB pool, libuv thread pool, event loop, CPU limit, memory, file descriptors, downstream rate limits. Load test in staging while watching all of these, and increase load step by step until it breaks. The first metric that hits its limit is your bottleneck. Then add limits and backpressure so the service rejects extra work early instead of falling over.

## 304: Adding logs makes a bug disappear. How do you debug it?

That points to a timing problem, because logging changes timing (a "heisenbug"). Use cheaper observation that changes timing less: collect events in memory and print them later, use counters, or use sampling tools like a CPU profiler. Look for shared state touched by concurrent async operations, missing `await`, and code that depends on the order in which promises finish. Tests that add random delays (or run many times in parallel) can make the race show up more often.

## 305: How do race conditions happen in single-threaded Node.js, and how do you debug them?

JavaScript runs one callback at a time, but every `await` is a point where other requests can run. A read-then-write over an `await` can lose updates:

```js
// two requests at the same time can both read 10 and both write 9
const item = await db.item.findUnique({ where: { id } });
await db.item.update({ where: { id }, data: { stock: item.stock - 1 } });
```

To debug, log a timestamp and request ID at each step and look for interleaving. Fix it with atomic updates (`stock: { decrement: 1 }` with a `where` on stock), database locks, or optimistic version checks, not with in-memory locks, which break with more than one instance.

## 306: You find corrupted data that was written days ago. How do you trace the cause?

First stop more damage: find out if it is still happening. Then find when each bad record was last changed (`updated_at`, audit tables, database logs, change streams or CDC events). Look at the deploys, jobs and scripts that ran around those times, and at which code paths write those fields. Check the backups to see the record's history. Once you know the cause, write a fix script, test it on a copy, and keep a backup of the bad state before running it.

## 307: During an incident, how do you balance fixing the cause with stopping the impact?

Stop the impact first, find the cause after. Mitigations like rolling back, turning off a feature flag, scaling up, failing over, or blocking an abusive client are often faster than a fix and are usually safe. While mitigating, save what you will need later: logs, a heap snapshot or a pod taken out of rotation instead of deleted. Keep one person coordinating, write down actions with timestamps, and avoid many people changing things at once.

## 308: How do you compare good and bad requests to find the cause?

Take a set of failing requests and a set of working requests and compare their fields: endpoint, version, instance, region, customer, client version, payload size, feature flags. The field whose values are very different between the two sets is a strong lead. This works best when logs or traces have many fields per request (high-cardinality data like customer ID and build version), which is why wide, structured events are so useful.

## 309: When do you stop investigating and accept a workaround?

When the impact is gone, the cost of more digging is higher than the risk of it coming back, and you have a way to notice if it does. For example, a rare bug in an old library you are replacing next month. Write down what you know, what you tried, and the workaround, add an alert or metric that would show it again, and open a ticket. Do not accept workarounds for data loss or security bugs without finding the cause.

## 310: A problem appears only after days of uptime. How do you debug it?

Things that grow slowly are the usual cause: memory leaks, caches without limits, file descriptors, connection counts, timer counts, log file size, counters that overflow, or tokens that expire after a long time. Graph these metrics over the whole uptime, not just the last hour. Take heap snapshots hours apart and compare them. To reproduce faster, run the same work at a higher rate in a test environment.

## 311: A third-party API changed its behavior without notice. How do you prove it and protect your service?

Log the request ID, status code, latency and the relevant response fields (not personal data) for calls to the API, and keep enough history to compare before and after. Compare one of today's responses with an old recorded one. Contract tests or schema validation of responses catch the change early next time. Protect your service with timeouts, validation of responses, a fallback, and alerts on the API's error rate. Then send the provider the request IDs and timestamps.

## 312: How do you design a back-end service so it is easy to debug?

- Structured logs with a request ID and trace ID on every line.
- Tracing across HTTP calls, queues and database calls.
- RED metrics per endpoint and USE metrics per resource, with useful labels.
- Clear error types and messages that say what failed and with which IDs.
- Config validated at startup, and version and build info exposed on an endpoint.
- Timeouts and limits everywhere, so failures are fast and visible.
- Runtime log level changes and feature flags.
- Safe defaults for logging so secrets and personal data stay out.

## 313: How does garbage collection affect latency in Node.js, and how do you see it?

V8 pauses JavaScript during parts of garbage collection. Young generation collections are short, but full collections of a big old generation can take tens or hundreds of milliseconds, which shows up as latency spikes. See GC events with `--trace-gc`, or measure them in code:

```js
import { PerformanceObserver } from "node:perf_hooks";

new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.duration > 50)
      logger.warn({ kind: e.detail?.kind, ms: e.duration }, "long gc");
  }
}).observe({ entryTypes: ["gc"] });
```

Lots of GC usually means lots of short-lived allocations or a heap that is too close to its limit.

## 314: In a heap snapshot, what is the difference between shallow size and retained size?

Shallow size is the memory of the object itself. Retained size is the memory that would be freed if that object were removed, including everything only it keeps alive. A small `Map` can have a huge retained size because it holds many objects. When looking for leaks, sort by retained size, then follow the "Retainers" panel up to a root you recognize, like a module-level variable, an event emitter or a timer.

## 315: How do closures cause memory leaks, and how do they show in a heap snapshot?

A closure keeps alive the variables of the scope it was created in. If a long-lived object (a global cache, an emitter listener, an interval) holds a closure, all those variables stay in memory too, even large ones the closure does not use, because V8 can share one context object between closures of the same scope.

```js
function handle(req) {
  const big = loadBigReport(); // large object
  const id = req.id;
  emitter.on("done", () => console.log(id)); // listener never removed: keeps the scope alive
}
```

In the snapshot you see many `(closure)` entries and `system / Context` objects whose retainers lead back to the emitter's listener array.

## 316: RSS keeps growing but the JS heap is flat. How do you debug it?

The memory is outside the V8 heap. Check `external` and `arrayBuffers` in `process.memoryUsage()` for Buffer growth (for example Buffers kept in a cache, or many slices holding big parent buffers). Native modules (image processing, compression, database drivers) can leak too. With many threads, glibc's allocator can also make RSS grow because of memory fragmentation across arenas; setting `MALLOC_ARENA_MAX=2` or using jemalloc sometimes helps. To narrow it down, turn off features one by one in a test environment and watch RSS.

## 317: How do you debug a Node.js crash in native code (exit code 139)?

139 means `SIGSEGV`, a crash in native code, so JavaScript error handlers do not run. Run with `--report-on-fatalerror` to get a diagnostic report with the native stack. Allow core dumps (`ulimit -c unlimited`) and analyze them with `llnode` or `gdb`. The cause is usually a native addon (bcrypt, sharp, a database driver) built for another Node version or with a bug. Rebuild native modules (`npm rebuild`), update them, and check if the crash goes away with a pure JavaScript version of the module.

## 318: How do you profile a Node.js service in production safely?

Sampling CPU profilers have a small overhead and are usually fine for short periods. Options are a continuous profiling tool (with an agent that samples all the time at low overhead) or a short on-demand profile from one instance. Take the instance out of the load balancer first if the profile could slow it down, and avoid heap snapshots on busy instances because they pause the process. Profile files show code paths and can include strings from memory, so store them like other sensitive data.

## 319: How do you take a CPU profile from code without restarting the process?

Use the `node:inspector` module to talk to the built-in profiler, for example from a protected admin endpoint.

```js
import { Session } from "node:inspector/promises";
import { writeFile } from "node:fs/promises";

export async function profile(ms = 10_000) {
  const session = new Session();
  session.connect();
  await session.post("Profiler.enable");
  await session.post("Profiler.start");
  await new Promise((r) => setTimeout(r, ms));
  const { profile } = await session.post("Profiler.stop");
  await writeFile(
    `/tmp/profile-${Date.now()}.cpuprofile`,
    JSON.stringify(profile),
  );
  session.disconnect();
}
```

Open the file in Chrome DevTools or VS Code. Protect the endpoint well, and limit how often it can be called.

## 320: What is microtask starvation and how do you debug it?

Node runs all queued `process.nextTick` callbacks and promise microtasks before it moves to the next event loop phase. If code keeps adding new microtasks (for example a recursive `async` function that never awaits real I/O), timers and I/O never get a turn. Symptoms are a process with 100% CPU that does not answer requests or fire timers. A CPU profile shows the same async function over and over. Fix it by yielding with `setImmediate` in long loops.

```js
for (let i = 0; i < items.length; i++) {
  process(items[i]);
  if (i % 1000 === 0) await new Promise((r) => setImmediate(r));
}
```

## 321: How do you find and fix a ReDoS problem?

A regular expression with nested quantifiers, like `/^(a+)+$/`, can take exponential time on some inputs, blocking the event loop. Signs are CPU spikes tied to certain requests, and a CPU profile showing time inside `RegExp` code. Find the request input that triggered it, test the regex with it, and fix the pattern (remove nested or overlapping quantifiers), limit the input length before matching, or use a safe regex engine like RE2. Linters such as `eslint-plugin-regexp` can catch risky patterns.

## 322: Why does AsyncLocalStorage sometimes lose the request context?

The context follows async operations created inside `als.run()`. It can get lost when a library queues callbacks and runs them later from a different context, for example some connection pools, custom thenables, or event emitters created outside the request. Then `getStore()` returns `undefined` and logs lose their request ID. Fix it by binding callbacks with `AsyncResource.bind()` or `AsyncLocalStorage.bind()`, or by updating the library. Node 24 changed the internal implementation of AsyncLocalStorage, so check behavior after upgrading.

## 323: How can diagnostics_channel help with debugging?

`diagnostics_channel` is a built-in way for libraries to publish internal events that you can subscribe to without changing their code. For example, undici (Node's `fetch`) publishes channels for request creation, headers and errors.

```js
import diagnosticsChannel from "node:diagnostics_channel";

diagnosticsChannel.subscribe("undici:request:create", ({ request }) => {
  logger.debug(
    { method: request.method, origin: request.origin, path: request.path },
    "outgoing request",
  );
});
diagnosticsChannel.subscribe("undici:request:error", ({ request, error }) => {
  logger.warn(
    { origin: request.origin, err: error },
    "outgoing request failed",
  );
});
```

Tracing tools use these channels too. Be careful not to log query strings or headers that hold tokens.

## 324: How do you debug problems with worker threads?

Listen to the worker's `error` and `exit` events, since an uncaught error in a worker does not crash the main thread by itself, and work can silently stop.

```js
const worker = new Worker(new URL("./resize.js", import.meta.url), {
  resourceLimits: { maxOldGenerationSizeMb: 256 },
});
worker.on("error", (err) => logger.error({ err }, "worker failed"));
worker.on(
  "exit",
  (code) => code !== 0 && logger.warn({ code }, "worker exited"),
);
```

Each worker has its own heap, so memory adds up per worker. You can debug a worker with the inspector like the main thread. Data passed with `postMessage` is copied, so very large messages are slow; transfer `ArrayBuffer`s instead.

## 325: Why does an unhandled 'error' event crash a Node.js process?

If an `EventEmitter` emits `error` and there is no `error` listener, Node throws the error, which usually crashes the process. Streams, sockets, database clients and Redis clients all emit `error`. A crash with a stack trace that starts in an emitter, with no clear caller in your code, is often this. Add `error` listeners to every long-lived client and stream, and use `stream.pipeline` so stream errors are handled and streams are cleaned up.

## 326: How do you debug stream problems like hanging uploads or memory growth?

If you write to a stream faster than it can accept data and ignore the return value of `write()`, data piles up in memory. If one stream in a chain fails and you used `.pipe()`, other streams are not closed and the request can hang. Use `pipeline`, which handles backpressure, errors and cleanup:

```js
import { pipeline } from "node:stream/promises";
import { createGzip } from "node:zlib";
import { createReadStream } from "node:fs";

await pipeline(createReadStream(file), createGzip(), res);
```

Log `error`, `close` and `finish` events while debugging to see which stream stops.

## 327: How do you debug EMFILE "too many open files" errors?

The process has hit its limit of file descriptors, which includes files, sockets and pipes. Count what is open and what kind:

```bash
ls /proc/<pid>/fd | wc -l
lsof -p <pid> | awk '{print $5}' | sort | uniq -c | sort -rn
ulimit -n
```

A slow climb means a leak, for example sockets to a downstream service that are never closed, or files opened without being closed. A sudden peak means too much work in parallel; limit concurrency. Raise the limit only after you know it is not a leak.

## 328: How do you debug "socket hang up" errors on outgoing requests?

"socket hang up" (`ECONNRESET`) means the server closed the connection before sending a full response. A common hidden cause is keep-alive: since Node 19 the default HTTP agent keeps connections alive, and if the server closes an idle connection at the same moment the client reuses it, the request fails. Other causes are server crashes, proxies with short idle timeouts and request bodies that are too large. Make the client's idle timeout shorter than the server's, and retry idempotent requests once on this error.

## 329: How do you debug a request that hangs forever because a promise never resolves?

Find which await it is stuck on: log before and after each step with the request ID, or take a snapshot of what is pending. Common causes are a pool where code acquires a second connection while holding the first (deadlock when the pool is full), a missing `resolve` in a hand-written `new Promise`, an event that is never emitted, and a call without a timeout. Add timeouts to every external wait so a hang becomes an error with a stack trace.

```js
const timeout = (ms) =>
  new Promise((_, rej) =>
    setTimeout(() => rej(new Error(`timeout ${ms}ms`)), ms),
  );
await Promise.race([waitForLock(key), timeout(5000)]);
```

## 330: How do you find which code allocates the most memory?

Use the sampling heap profiler. It records where allocations happen with low overhead.

```bash
node --heap-prof server.js     # writes a .heapprofile file on exit
```

You can also record "Allocation sampling" in the DevTools Memory tab while sending load. Open the result to see functions sorted by allocated bytes. High allocation is not a leak, but it causes more GC, so reducing it (reusing buffers, avoiding big temporary arrays, streaming instead of loading all) lowers CPU and latency.

## 331: Code got slower after upgrading Node.js. How do you debug it?

Compare CPU profiles on both versions with the same load and the same code. Look for functions that got wider. V8 changes can affect how hot functions are optimized; V8 flags like `--trace-deopt` show functions that get de-optimized, which can point to code with mixed types. Also check dependency differences, since an upgrade often comes with new native module builds, and changed defaults (for example keep-alive, DNS result order, or stricter TLS settings). Read the release notes for the versions you skipped.

## 332: The process crashes at startup in production and logs show nothing. What do you do?

Logs may be lost because the process exits before an asynchronous logger flushes. Make fatal errors write synchronously to stderr before exit, and run with `--report-uncaught-exception` to get a report file. Check the orchestrator's view: exit code, `OOMKilled`, and logs of the previous container (`kubectl logs --previous`). Run the same image locally with the production config (without real secrets) to see the error. Missing env vars, failed config validation and a wrong start command are the most common causes.

## 333: How do you debug a memory leak that comes from a framework-level pattern in Express or Fastify?

Common patterns: storing per-request objects in a module-level array or `Map` (for example for "active requests" tracking) without removing them on `close`, adding listeners to `process` or a shared emitter inside a route, creating a new client (Redis, HTTP agent, Prisma) per request instead of once, and caching responses keyed by URLs with query strings that are always unique. Heap snapshot comparison usually shows `IncomingMessage` or `ServerResponse` objects that should have been freed. Check their retainers.

## 334: In what order do Fastify hooks run, and what are the common mistakes?

The request lifecycle is: `onRequest`, `preParsing`, `preValidation`, `preHandler`, the handler, `preSerialization`, `onSend`, `onResponse`. `onError` runs when an error happens, before the error reply is sent. Common mistakes:

- Reading `request.body` in `onRequest`, where it is not parsed yet.
- Doing auth in `preHandler` after expensive validation, instead of in `onRequest`.
- Expecting to change the response in `onResponse`, which runs after the response is sent.
- Mixing `async` hooks with a `done` callback.

## 335: How can request-scoped providers in NestJS cause performance problems?

A request-scoped provider is created for each request, and every provider that depends on it also becomes request-scoped, all the way up to the controller. So one request-scoped logger can make big parts of the app create new instances on every request, which adds CPU and GC load. If latency went up after adding `Scope.REQUEST`, this is the likely cause. Use `AsyncLocalStorage` (for example via `nestjs-cls`) for request data instead, or durable providers for multi-tenant cases.

## 336: How do you debug slow NestJS startup?

Nest logs each module as it initializes. Look for large gaps between those lines. `onModuleInit` and `onApplicationBootstrap` hooks are awaited, so a slow database connection, a migration or a remote config fetch there delays startup. Async providers with `useFactory` are awaited too. A CPU profile with `--cpu-prof` of the startup also shows heavy import-time work. Slow startup matters because readiness probes and autoscaling depend on it.

## 337: How do you debug "There is no matching message handler" in NestJS microservices?

The client sent a message with a pattern that no handler on the server listens to. Compare the pattern exactly, including object patterns like `{ cmd: 'get_user' }`, where key names and value types must match. Check that the server connects to the same transport (same queue, topic or host) and that the controller with `@MessagePattern` is registered in a module the microservice loads. Also check that you did not mix up `@MessagePattern` (request-response) and `@EventPattern` (events).

## 338: Why do NestJS shutdown hooks not run?

Nest only listens for termination signals if you call `app.enableShutdownHooks()`. Without it, `onModuleDestroy`, `beforeApplicationShutdown` and `onApplicationShutdown` are not called on `SIGTERM`, so connections are not closed and in-flight work is lost on deploy. Also make sure Node is PID 1 or the signal is passed on, and that your shutdown finishes before the orchestrator's grace period ends.

## 339: How do you debug a GraphQL API that gets slow because of expensive queries?

Clients can send deeply nested or very wide queries that fan out into thousands of resolver calls. Log the operation name and a hash of the query with its duration, and look for the slow operations. Per-resolver tracing shows where the time goes. Protect the API with depth limits, query cost analysis, pagination limits on list fields, and persisted queries (only known queries allowed) for first-party clients.

## 340: Why do GraphQL subscriptions or WebSocket messages not reach all clients?

With more than one server instance, an in-memory PubSub only sends events to clients connected to the same instance. Use a shared PubSub (Redis, Kafka, a managed service). Also check the proxy: WebSockets need HTTP/1.1 upgrade headers, and idle connections are closed after the proxy's read timeout.

```nginx
location /graphql {
    proxy_pass http://app;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 1h;
}
```

Use ping/pong keepalives so idle connections do not get dropped.

## 341: How do you debug errors in a federated GraphQL setup?

In federation, a router or gateway builds a query plan and calls several subgraphs. An error may come from the router (composition or planning) or from one subgraph. Check which subgraph the error came from (routers usually add the service name in error extensions), look at the query plan, and trace the request across the router and subgraphs. Many problems come from schema changes in one subgraph that break composition, which schema checks in CI should catch.

## 342: How do you debug 431 Request Header Fields Too Large?

The request headers are bigger than the server allows. Node's default limit is 16 KB for all headers together, and you can change it with `--max-http-header-size`. The usual cause is large cookies or a big JWT, often many cookies set for the whole domain by different apps. Check the header sizes in the browser or with curl, remove old cookies, keep JWTs small (put less data in claims), and only raise the limit as a last step. Proxies have their own limits, like Nginx `large_client_header_buffers`.

## 343: Why do Server-Sent Events or streamed responses arrive all at once behind Nginx?

Nginx buffers upstream responses by default, so it waits for the buffer to fill or the response to end before sending to the client. Turn buffering off for streaming routes, or send the `X-Accel-Buffering: no` header from the app.

```nginx
location /events {
    proxy_pass http://app;
    proxy_buffering off;
    proxy_cache off;
    proxy_read_timeout 1h;
}
```

Compression middleware in the app can also buffer, so flush after each event or disable compression for that route.

## 344: How do you debug WebSocket connections that drop after some time?

If they drop after a fixed time, like 60 seconds of no messages, it is an idle timeout in a proxy or load balancer. Send ping/pong frames more often than the shortest idle timeout in the path. If they drop on deploy, it is the server shutting down; clients need reconnect logic with backoff and jitter. Log close codes on both sides: `1006` means the connection closed without a proper close frame, which points to the network or a proxy.

## 345: How do you debug compression problems, like broken responses or a wrong Content-Length?

Common issues: double compression (the app and the proxy both gzip, so the client gets garbage), a `Content-Length` that does not match the compressed body, compressing already compressed files, or a CDN serving a compressed copy to a client that did not ask for it because `Vary: Accept-Encoding` is missing. Check with `curl -sv -H 'Accept-Encoding: gzip' url -o /dev/null` and look at `Content-Encoding` and `Content-Length`. Compress in one place only, usually the proxy.

## 346: How do you debug an endpoint that returns a very large JSON response slowly?

`JSON.stringify` on a big object blocks the event loop, and the response may sit in memory several times over (object, string, buffer). Measure the time spent in serialization with a CPU profile. Fixes: paginate, return fewer fields, stream the response (for example NDJSON from a database cursor), or use a faster serializer with a schema (Fastify's response schemas). Also check that the database query does not load more rows than you return.

## 347: How do you debug lost updates when two clients edit the same resource?

Two clients read version 1, both change it, and the last write wins, losing the other change. Logs show two updates close together on the same ID. Fix it with optimistic concurrency: the client sends the version it read (`If-Match` with an ETag), and the server only updates if the version still matches, returning `412 Precondition Failed` otherwise.

```sql
UPDATE documents SET body = $1, version = version + 1
WHERE id = $2 AND version = $3;
-- 0 rows updated means someone else changed it first
```

## 348: Which built-in Node.js HTTP server timeouts can cut off requests?

- `server.headersTimeout` (60 seconds by default): time to receive all request headers.
- `server.requestTimeout` (300 seconds by default since Node 18): time to receive the whole request.
- `server.keepAliveTimeout` (5 seconds by default): how long an idle keep-alive connection stays open.
- `server.timeout` (0, meaning none, by default): socket inactivity timeout.

A long upload that fails at exactly 5 minutes, or slow clients cut off at 60 seconds, point to these. Your framework and proxy have their own timeouts too.

## 349: How do you safely replay production traffic to reproduce a bug?

Record requests at the edge or from logs, but remove or replace tokens, cookies and personal data before storing them. Replay against a staging environment with its own data and with outgoing side effects (emails, payments, webhooks) turned off or pointed at fakes. Shadow traffic (sending a copy of live requests to a new version and throwing away its responses) is another option, but it has the same side-effect and privacy concerns, so start with read-only endpoints.

## 350: A schema migration in PostgreSQL caused an outage. What happened and how do you prevent it?

Many `ALTER TABLE` commands need an `ACCESS EXCLUSIVE` lock. If a long query is running on the table, the migration waits for the lock, and every new query on that table waits behind the migration, so the table looks frozen. Prevent it by setting `lock_timeout` so the migration gives up quickly and can retry, using `CREATE INDEX CONCURRENTLY`, adding columns without volatile defaults, and splitting changes into steps (add column, backfill in batches, add constraint as `NOT VALID`, then `VALIDATE CONSTRAINT`).

```sql
SET lock_timeout = '3s';
ALTER TABLE orders ADD COLUMN note text;
```

## 351: How do you debug lock contention on hot rows in PostgreSQL?

Many transactions updating the same row (a counter, a balance, a "last updated" field on a parent) wait on each other. In `pg_stat_activity` you see many sessions with `wait_event_type = 'Lock'` and `wait_event = 'transactionid'` or `'tuple'`, all blocked by the same few PIDs. Fixes: keep the transaction that touches the hot row as short as possible and do it last, use atomic `UPDATE ... SET n = n + 1` instead of read-then-write, spread the counter over several rows and sum them, or move the counting to a queue or Redis.

## 352: How do you debug table bloat and autovacuum problems in PostgreSQL?

Updates and deletes leave dead rows that vacuum has to clean. If vacuum falls behind, tables and indexes grow and queries get slower.

```sql
SELECT relname, n_live_tup, n_dead_tup, last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC
LIMIT 10;
```

If dead rows keep growing even though autovacuum runs, something is holding back the cleanup horizon: a long-running or idle-in-transaction session, an unused replication slot, or an old prepared transaction. Find and end it, then tune autovacuum for busy tables.

## 353: How do you debug serialization failures in PostgreSQL?

With `REPEATABLE READ` or `SERIALIZABLE` isolation, PostgreSQL aborts a transaction when it would see or create an inconsistent result, with SQLSTATE `40001` ("could not serialize access"). This is expected behavior, not a bug: the app must retry the whole transaction. If you see many of them, transactions are too long or touch the same rows. Log the SQLSTATE and the retry count to see how often it happens.

```js
for (let attempt = 1; attempt <= 3; attempt++) {
  try {
    return await runTransfer();
  } catch (e) {
    if (e.code !== "40001" || attempt === 3) throw e;
  }
}
```

## 354: Why does a prepared query become slow after a few runs in PostgreSQL?

For prepared statements, PostgreSQL uses custom plans for the first five runs, then may switch to a generic plan that ignores the actual parameter values. If data is very uneven (one customer has millions of rows, most have a few), the generic plan can be bad for some values. Drivers and ORMs often use prepared statements without you noticing. Compare `EXPLAIN` with real values and with `$1` placeholders, and try `SET plan_cache_mode = force_custom_plan` for that session or query to confirm.

## 355: How do you debug replication lag and read-after-write bugs with PostgreSQL read replicas?

On the primary, `pg_stat_replication` shows `write_lag`, `flush_lag` and `replay_lag` per replica. On a replica, `now() - pg_last_xact_replay_timestamp()` gives a rough lag. Lag grows with big writes, long queries on the replica that conflict with replay, or a slow network. If users see their own changes disappear, the app reads from a replica right after writing. Send reads that must see the latest data to the primary, or route a user to the primary for a short time after they write.

## 356: How do you use auto_explain to catch bad plans in production?

`auto_explain` writes the plan of slow queries to the PostgreSQL log, so you see the plan that actually ran, with real parameters.

```sql
LOAD 'auto_explain';
SET auto_explain.log_min_duration = '500ms';
SET auto_explain.log_analyze = on;   -- real timings, adds overhead
```

For all sessions, set it in `session_preload_libraries` or `shared_preload_libraries`. `log_analyze` adds timing overhead to every query, so use it with care. Plans in logs can include parameter values, so check what they expose.

## 357: What breaks when you put PgBouncer in transaction pooling mode?

In transaction mode a client gets a server connection only for one transaction, so session state does not stay: `SET` commands, session advisory locks, `LISTEN/NOTIFY`, temporary tables and (on older PgBouncer versions) prepared statements. Symptoms are errors like "prepared statement does not exist" or settings that randomly do not apply. Use `SET LOCAL` inside transactions, use transaction-level advisory locks, and on PgBouncer 1.21+ turn on `max_prepared_statements`. Some ORMs had a special flag for PgBouncer, so check your ORM's docs.

## 358: How do you debug slow queries generated by an ORM?

Log the generated SQL with timings and find the slow or repeated ones. Typical problems are N+1 loops (a query inside a `for` loop over results), loading whole relations when you need a count, selecting all columns, and filters the ORM cannot turn into indexed SQL. Run `EXPLAIN ANALYZE` on the generated SQL. Fix with `include` or joins (Prisma has a `relationLoadStrategy` option to choose between joins and separate queries), `select` for only the needed fields, or a raw SQL query for the hot path.

## 359: How do you debug Prisma interactive transaction timeouts?

Interactive transactions have a `maxWait` (time to get a connection, 2 seconds by default) and a `timeout` (time the transaction may run, 5 seconds by default). When exceeded, you get error `P2028`. Usually the transaction does slow work inside, like HTTP calls, or the pool is busy. Move slow work outside the transaction, and only raise the limits if the work really belongs inside.

```ts
await prisma.$transaction(
  async (tx) => {
    const order = await tx.order.create({ data });
    await tx.stock.update({
      where: { id: data.itemId },
      data: { qty: { decrement: 1 } },
    });
    return order;
  },
  { maxWait: 5000, timeout: 10000 },
);
```

## 360: How do you trace Prisma queries with OpenTelemetry?

Add `@prisma/instrumentation` to your OpenTelemetry setup. It creates spans for each Prisma operation and the underlying database queries, so you can see in a trace which query is slow and how long the connection wait took.

```ts
import { PrismaInstrumentation } from "@prisma/instrumentation";

const sdk = new NodeSDK({
  instrumentations: [
    getNodeAutoInstrumentations(),
    new PrismaInstrumentation(),
  ],
});
```

Older Prisma versions needed the `tracing` preview feature in the schema; newer versions have it built in.

## 361: How do you debug a slow MongoDB aggregation pipeline?

Run `explain('executionStats')` on the aggregation. Check that the first `$match` and `$sort` stages can use an index. Stages after `$group`, `$unwind` or `$project` usually cannot. Put `$match` as early as possible, `$project` away big fields early, and avoid `$lookup` on fields without an index on the other collection. Stages that use more than 100 MB of memory write to disk (allowed by default since MongoDB 6.0), which is much slower; the explain output shows when that happens.

```js
db.orders
  .explain("executionStats")
  .aggregate([
    { $match: { status: "paid", createdAt: { $gte: ISODate("2026-10-01") } } },
    { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  ]);
```

## 362: MongoDB picks the wrong index for a query. How do you debug it?

MongoDB tries candidate plans and caches the winner for a query shape. If data changes, the cached plan can become bad. Use `explain('allPlansExecution')` to see the candidates, test the better index with `hint()`, and clear the cache for the collection to check if a fresh choice helps.

```js
db.orders
  .find({ status: "paid", customerId: 42 })
  .hint({ customerId: 1, createdAt: -1 })
  .explain("executionStats");
db.orders.getPlanCache().clear();
```

Long term, fix the indexes (often a compound index in equality, sort, range order) instead of hardcoding `hint()` in code.

## 363: How do you debug write conflicts in MongoDB transactions?

When two transactions change the same document, one fails with a `WriteConflict` error that has the `TransientTransactionError` label. The fix is to retry the whole transaction. `session.withTransaction()` does that for you, while hand-written `startTransaction`/`commitTransaction` code often does not.

```js
const session = client.startSession();
try {
  await session.withTransaction(async () => {
    await accounts.updateOne(
      { _id: from },
      { $inc: { balance: -amount } },
      { session },
    );
    await accounts.updateOne(
      { _id: to },
      { $inc: { balance: amount } },
      { session },
    );
  });
} finally {
  await session.endSession();
}
```

Many conflicts mean hot documents; keep transactions short and touch hot documents last.

## 364: How do you debug MongoDB connection pool and server selection errors in Node.js?

`MongoServerSelectionError` after 30 seconds (`serverSelectionTimeoutMS`) means the driver could not find a suitable server: network, DNS, TLS, IP allowlist, or wrong replica set name. If connections work but requests wait, the pool may be full: `maxPoolSize` is 100 by default, and by default requests wait in the queue without a timeout. Set `waitQueueTimeoutMS` so waiting fails with a clear error, and listen to the driver's connection pool events to log checkouts and waits.

```js
client.on("connectionCheckOutFailed", (e) =>
  logger.warn({ reason: e.reason }, "pool checkout failed"),
);
```

## 365: How do you debug memory and CPU problems with Mongoose on large result sets?

Full Mongoose documents are much heavier than plain objects, because each has change tracking, getters and methods. Loading 100,000 documents can use a lot of memory and CPU. Use `.lean()` for read-only queries, `select` only needed fields, and a cursor to process big sets one by one.

```js
for await (const doc of Order.find({ status: "paid" })
  .select("amount customerId")
  .lean()
  .cursor()) {
  await handle(doc);
}
```

Compare `process.memoryUsage().heapUsed` before and after to see the difference.

## 366: How do you debug hot partitions in DynamoDB in depth?

Each partition has limits (around 3,000 read units and 1,000 write units per second). If one partition key gets most of the traffic, it is throttled even when the table has spare capacity. Adaptive capacity helps for uneven load, but not when one single key goes over the per-partition limit. Use CloudWatch Contributor Insights to find the hottest keys. Fixes are a better key design, write sharding (adding a suffix like `#0` to `#9` to a hot key and reading all shards), caching hot reads, or batching writes.

## 367: Why does a DynamoDB GSI return old data right after a write?

Global secondary indexes are updated asynchronously and only support eventually consistent reads. You cannot use `ConsistentRead: true` on a GSI. So a query on a GSI right after a write may not see the new item yet. If you need read-after-write, read from the base table by primary key, or design the flow so the client does not need to query the index right away.

## 368: How do you debug a DynamoDB Streams consumer (Lambda) that falls behind?

Watch the `IteratorAge` metric: growing age means the function is not keeping up or is stuck. A record that always fails blocks its shard, because Lambda retries the batch until the records expire. Use `BisectBatchOnFunctionError`, a limit on `MaximumRetryAttempts` and `MaximumRecordAgeInSeconds`, an on-failure destination, and `ReportBatchItemFailures` so only the failed records are retried.

```js
export const handler = async (event) => {
  const batchItemFailures = [];
  for (const record of event.Records) {
    try {
      await handle(record);
    } catch (err) {
      batchItemFailures.push({
        itemIdentifier: record.dynamodb.SequenceNumber,
      });
    }
  }
  return { batchItemFailures };
};
```

## 369: How do you debug Redis Cluster errors like MOVED and CROSSSLOT?

- `MOVED` and `ASK` mean the key's slot is on another node. A cluster-aware client handles them; seeing them as errors means the client is not in cluster mode.
- `CROSSSLOT Keys in request don't hash to the same slot` means a multi-key command (like `MGET`, a transaction or a Lua script) used keys in different slots.

Use hash tags so related keys go to the same slot: only the part inside `{}` is hashed.

```
SET {user:42}:profile "..."
SET {user:42}:settings "..."
MGET {user:42}:profile {user:42}:settings
```

Be careful: putting too many keys under one tag creates a hot slot.

## 370: Why can writes be lost after a Redis failover?

Redis replication is asynchronous. The primary confirms a write before replicas have it. If the primary fails right after, a replica that did not get the write becomes the new primary, and the write is gone. You see this as data "rolling back" after a failover event. `WAIT numreplicas timeout` makes the client wait until replicas confirm, which lowers the risk but does not make Redis strongly consistent. Do not use Redis as the only store for data you cannot lose.

## 371: How do you confirm and fix a cache stampede in production?

Signs: right after a popular key expires (or after a deploy or Redis restart), database load spikes with many identical queries, and latency rises. Metrics show the cache hit rate dropping at the same moment. Fixes: let only one request rebuild the value (a short lock with `SET key NX PX`), serve the stale value while one request refreshes it, add random jitter to TTLs so keys do not expire together, and warm important keys before traffic returns.

## 372: How do you debug a Redis-based distributed lock that lets two workers in?

The common cause is the lock expiring while the first worker is still working (because of a slow call or a GC pause), so a second worker gets it. Another cause is deleting the lock without checking that you still own it. Log when the lock is taken, renewed and released, with the worker ID and timing. Release only if the value is yours, renew long locks, and for real safety use fencing tokens: an increasing number that the protected resource checks, so a late worker's write is rejected.

```lua
-- release only if we still own it
if redis.call('GET', KEYS[1]) == ARGV[1] then
  return redis.call('DEL', KEYS[1])
end
return 0
```

## 373: Redis returns OOM errors even though an eviction policy is set. Why?

`volatile-lru`, `volatile-lfu`, `volatile-ttl` and `volatile-random` only evict keys that have a TTL. If most keys have no TTL, Redis has nothing to evict and returns OOM. Check `INFO keyspace` for the share of keys with `expires`, and `evicted_keys` in `INFO stats`. Also check memory used outside data, like client output buffers for slow subscribers or replicas (`client_recent_max_output_buffer` in `INFO clients`), which can push Redis over `maxmemory`.

## 374: A Kafka consumer is stuck on one partition while others are fine. How do you debug it?

Check `kafka-consumer-groups.sh --describe`: if the current offset of that partition does not move, the consumer is failing on one message and retrying it forever (a poison message), or it is blocked on a slow call. Read that offset with the console consumer to see the message (watch out for personal data). Look at the consumer logs for repeated errors at the same offset. Fix the handler, or skip the message by sending it to a dead letter topic and committing the offset.

## 375: How do you debug Kafka transactions and "exactly-once" problems?

Exactly-once in Kafka covers reading from Kafka, processing, and writing back to Kafka within one transaction. It does not cover side effects like database writes or HTTP calls. Consumers that should not see aborted messages need `isolation.level=read_committed`. A producer transaction left open (for example after a crash, until its timeout) holds back what `read_committed` consumers can read, which looks like lag. Each producer instance needs a stable, unique `transactional.id` so old "zombie" instances get fenced off.

## 376: How do you debug under-replicated partitions in Kafka?

An under-replicated partition has fewer in-sync replicas than its replication factor. Check the `UnderReplicatedPartitions` broker metric and:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

Causes are a broker that is down or slow (disk, network, GC), or a broker that cannot keep up after a restart. While partitions are under-replicated, producers with `acks=all` may fail with `NOT_ENOUGH_REPLICAS` if fewer than `min.insync.replicas` are in sync, so this often shows up first as producer errors.

## 377: A new consumer group did not process old messages. Why?

When a group has no committed offset, `auto.offset.reset` decides where it starts, and the default is `latest`. So a new group only sees messages produced after it started. Changing the group ID (for example by renaming a service) has the same effect. Set `auto.offset.reset=earliest` if a new group should start from the beginning, or reset offsets on purpose with `kafka-consumer-groups.sh --reset-offsets`.

## 378: Messages were deleted before consumers processed them. How do you debug it?

Kafka deletes old messages by retention (`retention.ms`, `retention.bytes`), whether or not they were consumed. If a consumer was down longer than the retention period, its committed offset now points to deleted data. The consumer gets an offset-out-of-range condition, and `auto.offset.reset` moves it to the earliest or latest offset, which silently skips messages. Compare the group's committed offsets with the topic's earliest offsets, and alert on lag in time (how old the oldest unprocessed message is), not only in message count.

## 379: How do you debug a message that is redelivered over and over in RabbitMQ?

If a consumer calls `nack` or `reject` with `requeue: true` on an error, the message goes back to the queue and is delivered again right away, creating a busy loop that burns CPU and fills logs. Check the `redelivered` flag and look for the same message ID in logs. Use `requeue: false` with a dead letter exchange, and handle retries with a delay queue. Quorum queues have a delivery limit (20 by default since RabbitMQ 4.0) after which the message is dropped or dead-lettered, but classic queues do not.

## 380: How do you debug RabbitMQ cluster problems like network partitions?

Check the cluster state with `rabbitmq-diagnostics cluster_status` and look in the broker logs for partition messages. During a partition, nodes cannot see each other and queues may become unavailable or, with older settings, both sides may accept writes. Quorum queues use Raft and need a majority of members to be up, so with three nodes one can be lost. Classic mirrored queues were removed in RabbitMQ 4.0, so old clusters that relied on them need to move to quorum queues.

## 381: How do you debug too many connections or channels in RabbitMQ?

The management UI shows connections and channels per client. A count that grows means a leak: code that opens a new connection or channel per message or per request and never closes it. Each connection uses memory on the broker, and churn (constant open and close) costs CPU. Open one connection per process, reuse a small number of channels (one per consumer, separate ones for publishing), and close them on shutdown. Set a connection name in client properties so you can see which service owns each connection.

## 382: What does "delivery acknowledgement timed out" mean in RabbitMQ?

RabbitMQ closes a channel if a consumer holds an unacked message longer than `consumer_timeout`, which is 30 minutes by default. The error is `PRECONDITION_FAILED - delivery acknowledgement on channel X timed out`, and the message goes back to the queue. The consumer then fails on the next ack because the channel is closed. Either the job really takes that long (move long work to a different pattern, or raise the timeout for that queue), or the consumer forgot to ack on some code path.

## 383: Why do BullMQ jobs keep stalling, and how do you fix it?

A worker holds a lock on each active job and renews it in the background. If the event loop is blocked longer than `lockDuration` (30 seconds by default), the lock cannot be renewed, the job is seen as stalled, and it may be given to another worker while the first is still running it. Check event loop delay on the workers when stalls happen. Fixes: break CPU-heavy work into async chunks, move it to sandboxed processors (a separate process or worker thread) or raise `lockDuration` for jobs that are known to be heavy.

```js
const worker = new Worker("video", new URL("./processor.js", import.meta.url), {
  connection,
  useWorkerThreads: true,
});
```

## 384: Why is a BullMQ job processed twice, and how do you prevent it?

Possible reasons: the job stalled and another worker picked it up while the first was still running; the processor did the work but crashed before BullMQ marked it complete, so it was retried; or the same job was added twice. Check the job's `attemptsMade` and logs from both workers. Prevent duplicates when adding by setting a custom `jobId` (adding a job with an existing ID is ignored while it exists), and make the processor idempotent so a second run does no harm.

## 385: BullMQ is using more and more Redis memory. How do you debug it?

By default, completed and failed jobs stay in Redis forever, with their data and logs. Check counts with `queue.getJobCounts()` and big keys with `redis-cli --bigkeys`. Set retention when adding jobs:

```js
await queue.add("email", data, {
  removeOnComplete: { age: 3600, count: 1000 },
  removeOnFail: { age: 7 * 24 * 3600 },
});
```

Also keep job data small: store an ID and load the big payload from the database instead of putting it in the job.

## 386: How do you stop BullMQ from losing or repeating jobs during deploys?

On `SIGTERM`, call `await worker.close()`, which stops taking new jobs and waits for active ones to finish. If the orchestrator kills the process before that, active jobs stall and run again later. Make sure the grace period is longer than your longest job, or split long jobs into steps. Log when shutdown starts and how many jobs were still active, so you can match it with stalled-job events.

```js
process.on("SIGTERM", async () => {
  await worker.close();
  await connection.quit();
  process.exit(0);
});
```

## 387: An order was saved but its event was never published. How do you debug and fix this?

This is the dual-write problem: the code writes to the database and then publishes to the broker, and if the publish fails or the process crashes between the two, the event is lost (or the event is sent but the transaction rolls back). Look for errors or restarts at the time of that order. The fix is the outbox pattern: write the event to an `outbox` table in the same transaction as the order, and have a separate process publish rows from the outbox and mark them as sent. Change data capture tools can also read the outbox.

## 388: Why does a request that calls many services in parallel have high latency even when each service is usually fast?

The request is as slow as the slowest call. If each of 20 services has a 1% chance of being slow, about 18% of requests will hit at least one slow call. So the tail latency of each dependency becomes the typical latency of the whole request. Look at the trace to see which call finished last. Reduce fan-out, set tight per-call timeouts with fallbacks, cache, or use hedged requests (send a second request if the first is slow) for idempotent reads.

## 389: After an outage, the service fails again as soon as it comes back. What is happening?

This is often a thundering herd: all clients reconnect and retry at the same moment, caches are cold, and the sudden load knocks the service over again. Signs are a big spike in connections and requests right after recovery. Clients should reconnect with exponential backoff and random jitter. On the service side, use rate limiting and admission control, warm caches, and bring traffic back step by step.

## 390: What is a metastable failure and how do you recognize it?

A metastable failure is when a short trigger (a spike, a slow deploy) pushes the system into a bad state that keeps itself going after the trigger is gone. For example, timeouts cause retries, retries add load, load causes more timeouts. You recognize it when the original cause is fixed but the system does not recover, and the load is much higher than user traffic would explain. You get out of it by cutting load: stop retries, shed traffic, or scale out a lot, then bring traffic back slowly.

## 391: How can metrics labels break your monitoring, and how do you debug it?

Each unique combination of label values is a separate time series. Labels like user ID, request ID, full URL or error message create millions of series, which makes Prometheus slow, uses a lot of memory and raises costs. Signs are dashboards that time out and memory alerts on the metrics system. Find the metric with the most series and remove or bucket the label, for example use the route template `/users/:id` instead of the real path. Put high-cardinality data in logs and traces instead.

## 392: What are exemplars and how do they help debugging?

An exemplar is a sample trace ID attached to a metric data point, for example to a latency histogram bucket. In a dashboard you click a spike in p99 latency and jump straight to a trace of one of those slow requests. This links metrics (which show that something is wrong) with traces (which show why). OpenTelemetry and Prometheus support exemplars, but they must be turned on in both the app and the metrics backend.

## 393: Spans are missing or traces are broken into pieces. How do you debug it?

Check each hop: does the caller send `traceparent`, does the receiver read it, and does any proxy, gateway or queue drop it? Inside a service, context can get lost when work is done in callbacks or libraries that are not instrumented, so new spans start a fresh trace. Make sure the instrumentation loads before other modules and that all services use the same propagator (W3C Trace Context). Also be careful with `baggage`: it is sent to every downstream service, so never put personal data or secrets in it.

## 394: In a trace, a child span starts before its parent. What does it mean?

Spans from different services use each service's own clock, so clock differences make timings across services look wrong. Within one service, timings are correct. Check that all hosts use NTP and are in sync. When reading such a trace, trust durations within each service more than the gaps between services. Some tracing backends try to adjust for skew, but they cannot fix large differences.

## 395: How do you use Envoy or service mesh access logs to debug 503 errors?

Envoy's access logs include response flags that say why it returned an error, for example:

- `UH`: no healthy upstream hosts.
- `UF`: upstream connection failure.
- `UO`: upstream overflow (circuit breaking or connection limits).
- `NR`: no route configured.
- `URX`: retry or connect attempt limit reached.
- `UT`: upstream request timeout.

So a 503 with `UH` is a health or endpoint problem, while `UO` is a limits problem. The app may not have logged anything because the request never reached it.

## 396: How do you debug gRPC errors between Node.js services?

Read the gRPC status code, not just the message. `DEADLINE_EXCEEDED` means the caller's deadline ran out; `UNAVAILABLE` means the connection failed or the server is down, and is usually safe to retry; `UNIMPLEMENTED` usually means a wrong method name or mismatched proto. For `@grpc/grpc-js`, turn on internal logs:

```bash
GRPC_TRACE=all GRPC_VERBOSITY=DEBUG node client.js
```

Also check that proxies in between support HTTP/2 end to end, because gRPC breaks when a proxy downgrades to HTTP/1.1.

## 397: A producer changed its message format and consumers started failing. How do you debug and prevent it?

The consumer logs show parse or validation errors starting at the time of the producer's deploy. Find the first failing message and compare it with an old one. To prevent it, use a schema registry with a compatibility rule (for example backward compatible, which only allows changes old consumers can still read, like adding optional fields), validate messages in the producer's tests, and include a version in each message so consumers can handle several versions during a migration.

## 398: Users in one region see errors while others do not. How do you debug it?

Break down errors and latency by region and zone. Check what is different there: a regional deploy or config, a cloud provider incident, a regional dependency (database replica, cache, third-party endpoint), DNS routing sending traffic to the wrong place, or certificate or network issues at that edge. If you have failover, move traffic away from the region first to stop the impact, then investigate with the region drained.

## 399: How do you write alerts that help debugging instead of creating noise?

Alert on symptoms users feel, like error rate and latency against an SLO (burn rate alerts), not on every cause like high CPU. Each alert should say what is affected, link to a dashboard and a runbook with first steps, and include labels like service and region. Alerts that fire often without action should be fixed or removed, because people learn to ignore them. Cause-based metrics are still useful on dashboards for debugging after an alert fires.

## 400: What are wide events and why do they help with debugging?

A wide event is one structured log record per request (or per unit of work) that holds many fields: route, status, duration, user tier, build version, feature flags, cache hit, number of DB queries, downstream timings, and so on. Instead of searching many small log lines, you can filter and group these events by any field to find what failing requests have in common. Keep personal data out of them, using IDs and categories instead of names or emails.

```js
res.on("finish", () => {
  logger.info(
    {
      route: req.route?.path, // Express; in Fastify use request.routeOptions.url
      status: res.statusCode,
      durationMs: Date.now() - start,
      dbQueries: req.ctx.dbQueries,
      cacheHit: req.ctx.cacheHit,
      version: process.env.BUILD_VERSION,
    },
    "request",
  );
});
```

## 401: Logs or traces are missing or arrive late. How do you debug the observability pipeline itself?

Follow the data from the app to the backend: does the app write the log (check stdout in the container), does the agent or collector pick it up, does it send it, and does the backend accept it? Collectors and agents have their own metrics for dropped, queued and failed items, so watch those. Common causes are lines too long for the agent, invalid JSON, rate limits or quotas in the backend, a full buffer under load, and the app crashing before it flushes. Monitor the pipeline, or you will find out it was broken during an incident.

## 402: How do you tell an OOM kill from an eviction in Kubernetes?

An OOM kill happens when a container goes over its own memory limit: the container is restarted and `kubectl describe pod` shows `Last State: Terminated, Reason: OOMKilled`. An eviction happens when the node runs low on memory or disk: the kubelet removes whole pods, which show status `Evicted` with a message like "The node was low on resource: memory". Pods with no requests or limits (QoS class `BestEffort`) are evicted first, then `Burstable` ones using more than they requested. Setting memory requests equal to limits gives the `Guaranteed` class.

## 403: DNS lookups in Kubernetes are sometimes slow or time out. How do you debug it?

Measure lookup time from inside a pod, and check the CoreDNS pods' logs, CPU and restarts. Common causes: `ndots:5` making short names go through several search domains first (use fully qualified names ending with a dot, or lower `ndots`), CoreDNS not having enough replicas, and a known conntrack race with UDP that causes 5 second delays on some kernels. NodeLocal DNSCache helps with the last two. In Node.js, there is no built-in DNS cache, so each new connection does a lookup on the libuv thread pool.

## 404: Pods cannot reach an external service, or calls fail only under load. What do you check?

If it never works, check NetworkPolicy egress rules, security groups, route tables, NAT and the firewall on the other side, and test from a debug pod with `curl -v`. If it fails only under load, suspect source port (SNAT) exhaustion at the NAT gateway: many connections to the same destination IP and port use up the available ports. On AWS the NAT gateway's `ErrorPortAllocation` metric shows this. Fix it with connection reuse (keep-alive and pooling), fewer short-lived connections, or more NAT IPs.

## 405: Why do you get a few connection errors on every Kubernetes deploy, and how do you fix it?

When a pod is being terminated, removing it from the Service endpoints and sending it `SIGTERM` happen at the same time, and load balancers and kube-proxy take a moment to update. So the pod may stop accepting connections while traffic is still sent to it. Fixes: add a short `preStop` delay so the pod keeps serving while endpoints update, then shut down gracefully, and make sure the grace period covers both.

```yaml
lifecycle:
  preStop:
    sleep:
      seconds: 10 # native sleep action in newer Kubernetes; older versions use exec with "sleep"
terminationGracePeriodSeconds: 45
```

## 406: The Horizontal Pod Autoscaler does not scale. How do you debug it?

```bash
kubectl describe hpa my-api
kubectl top pods
```

The HPA's conditions and events say why. Common reasons: metrics-server is not installed or failing, the pods have no CPU or memory `requests` (CPU percent is calculated from requests), custom metrics are not exposed through an adapter, or it is already at `maxReplicas`. Also check that the metric actually goes up under load; a Node service limited by the event loop may have low CPU percent on a multi-core request while still being slow.

## 407: How do you debug a problem on the Kubernetes node itself?

Start a debug pod on the node. It gets access to the host file system under `/host`.

```bash
kubectl debug node/ip-10-0-1-23 -it --image=ubuntu
chroot /host
journalctl -u kubelet --since "30 min ago"
df -h
```

Look at kubelet logs, the container runtime logs, disk usage (disk pressure causes evictions) and kernel messages (`dmesg`) for OOM kills. `kubectl describe node` shows conditions like `MemoryPressure` and `DiskPressure`. Delete the debug pod afterwards, since it has wide access to the node.

## 408: What does CreateContainerConfigError mean in Kubernetes?

Kubernetes could not build the container's config, most often because a referenced Secret or ConfigMap, or a key inside it, does not exist. `kubectl describe pod` names the missing one. Check the namespace (Secrets are per namespace), the exact key names, and whether the Secret is created by another tool (like External Secrets) that has not synced yet. Do not print Secret values to debug; check the key names with `kubectl get secret my-secret -o jsonpath='{.data}' | jq 'keys'`.

## 409: A container fails with "exec format error". What is wrong?

The image was built for a different CPU architecture than the node, for example built on an Apple Silicon Mac (`arm64`) and run on an `amd64` server. Check and build for the right platform:

```bash
docker image inspect my-api:1.4 --format '{{.Os}}/{{.Architecture}}'
docker buildx build --platform linux/amd64,linux/arm64 -t registry/my-api:1.4 --push .
```

It can also mean a script is missing its shebang line or has Windows line endings.

## 410: How do you check whether a secret leaked into a Docker image?

Each layer of an image keeps the files that were added in it, even if a later layer deletes them. Build args and `ENV` values are also stored in the image metadata.

```bash
docker history --no-trunc my-api:1.4
docker image inspect my-api:1.4 --format '{{json .Config.Env}}'
```

Tools like `dive` show the files in each layer. If you find a secret, rotate it right away, because anyone who pulled the image has it. Then rebuild with BuildKit secret mounts and multi-stage builds so secrets never get into a layer.

## 411: How do you fix "upstream sent too big header while reading response header from upstream" in Nginx?

The response headers from the app are bigger than Nginx's buffer, often because of large `Set-Cookie` headers or big tokens in headers. Nginx returns 502. Raise the buffers for that location, and also look at why the headers are so big.

```nginx
proxy_buffer_size 16k;
proxy_buffers 8 16k;
proxy_busy_buffers_size 32k;
```

## 412: Nginx serves the wrong site or the wrong certificate. How do you debug it?

Nginx picks a `server` block by listen address and port, then by `server_name` matching the `Host` header (or SNI for TLS). If nothing matches, it uses the `default_server` for that port, or the first one defined. Print the full config with `nginx -T` and look for duplicate or overlapping `server_name` values. Test with the exact host name:

```bash
curl -v --resolve api.example.com:443:203.0.113.10 https://api.example.com/
```

## 413: How do you get Nginx debug logs for just one client?

Debug logging needs Nginx built with `--with-debug` (check `nginx -V`; the official Docker image includes an `nginx-debug` binary). To avoid huge logs, turn it on for one client IP only:

```nginx
events {
    debug_connection 203.0.113.25;
}
error_log /var/log/nginx/error.log info;
```

Debug logs include headers, so they can contain cookies and tokens. Turn them off when done and delete the log.

## 414: How do you tell if 5xx errors come from an AWS load balancer or from your app?

CloudWatch has separate metrics: `HTTPCode_ELB_5XX_Count` for errors the load balancer created itself, and `HTTPCode_Target_5XX_Count` for errors your targets returned. ALB access logs have both `elb_status_code` and `target_status_code`; if the target code is `-`, the request never got a response from your app. ELB 502s often come from targets closing connections (keep-alive mismatch) or crashing, 503 from no healthy targets, and 504 from targets being too slow.

## 415: An AWS IAM policy looks correct but access is still denied. What else do you check?

The final decision combines several policy types, and an explicit `Deny` anywhere wins. Check:

- Service control policies (SCPs) and resource control policies in AWS Organizations.
- Permission boundaries on the role.
- Session policies when assuming a role.
- Resource policies (S3, KMS, SQS), which must allow cross-account access.
- Conditions like `aws:SourceIp`, `aws:PrincipalTag`, VPC endpoint policies, or required encryption.

Some services return an encoded message that you can read with `aws sts decode-authorization-message --encoded-message <msg>`. The IAM policy simulator helps test single actions.

## 416: How do you debug network connectivity inside an AWS VPC?

- Security groups are stateful: allow inbound on the target and outbound on the source.
- Network ACLs are stateless: they need rules for return traffic on ephemeral ports too.
- Route tables: private subnets need a NAT gateway or VPC endpoints to reach the internet or AWS services.
- VPC Flow Logs show `ACCEPT` or `REJECT` for each connection attempt.
- VPC Reachability Analyzer checks a path between two resources and tells you which component blocks it.

A connection that hangs (timeout) usually means something drops the packets, while "connection refused" means the packets got there but nothing listens.

## 417: How do you debug workload identity failures in Kubernetes (IRSA, GKE Workload Identity, Azure Workload Identity)?

The pod should get cloud credentials from its Kubernetes service account. Check that the pod uses the right service account, that the account has the right annotation or association (for example `eks.amazonaws.com/role-arn` for IRSA, or an EKS Pod Identity association; `iam.gke.io/gcp-service-account` on GKE; `azure.workload.identity/client-id` on AKS), and that the cloud side trusts that exact namespace and service account name. Then ask the cloud who you are from inside the pod, for example `aws sts get-caller-identity`. If it shows the node's role, the pod is not using workload identity at all.

## 418: Terraform plan always shows a change even after apply. How do you debug it?

This is a perpetual diff. The provider or API changes the value after it is set: JSON policies are reformatted, a list comes back in a different order, a default is added, a value's case is changed, or another system (an autoscaler, a tag policy) changes the resource. Look at exactly which attribute changes in the plan. Fixes: write values the way the API returns them (use `jsonencode` or a policy document data source), use `lifecycle { ignore_changes = [...] }` for attributes managed elsewhere, or upgrade the provider if it is a known bug.

## 419: How do you debug a Terraform dependency cycle or wrong ordering?

A `Cycle` error lists the resources involved. Usually two resources reference each other, often through security group rules or outputs. Break the cycle by moving the cross-reference into a separate resource (for example a standalone security group rule). For ordering problems where Terraform creates things too early, check that the dependency is expressed through a real reference, and add `depends_on` only when there is no reference to use. `terraform graph` outputs the dependency graph in DOT format if you need to see it.

## 420: Why is Terraform state sensitive, and how do you debug without exposing secrets in it?

State holds every attribute of every resource in plain text, including generated passwords, keys and connection strings, even when they are marked `sensitive` (that only hides them in CLI output). Store state in an encrypted remote backend with limited access, and do not commit it or paste `terraform show` output. Newer Terraform versions (1.10+) have ephemeral resources and values, and 1.11+ adds write-only arguments, which let you pass secrets to providers without saving them in state.

## 421: How do you debug a failed OIDC login from GitHub Actions to a cloud provider?

The cloud checks claims in GitHub's OIDC token against the trust policy. The usual cause is a `sub` claim that does not match, since it changes with the trigger: `repo:my-org/my-repo:ref:refs/heads/main` for a branch, `repo:my-org/my-repo:environment:prod` when the job uses an environment, `repo:my-org/my-repo:pull_request` for PRs. Also check the audience (`aud`), and that the job has `permissions: id-token: write`. On AWS the error is "Not authorized to perform sts:AssumeRoleWithWebIdentity". Print the token's claims (not the token) in a debug step to compare.

## 422: How do JWT algorithm confusion bugs happen, and how do you check for them?

If the server lets the token's header choose the algorithm, an attacker can send `alg: none` or switch from RS256 to HS256 and sign with the public key as the HMAC secret. Check your verification code: it must set the allowed algorithms explicitly and use the right key type.

```js
await jwtVerify(token, publicKey, { algorithms: ["RS256"] });
// jsonwebtoken: jwt.verify(token, publicKey, { algorithms: ['RS256'] })
```

Write a test that sends a token with `alg: none` and one signed with HS256, and expect both to be rejected.

## 423: Login works on one instance but fails on another. What do you check?

Something differs per instance: a different JWT secret or key (for example a secret generated at startup, or one instance still running the old config after a rotation), an in-memory session store that is not shared, a different clock, or a different version during a rolling deploy. Log the instance ID with auth failures and the key ID (`kid`) used, then compare config between a good and a bad instance. Sessions must be in a shared store like Redis when you run more than one instance.

## 424: You suspect a security incident while debugging. What do you do differently?

Stop treating it as a normal bug. Tell the security team or follow the incident process. Keep evidence: do not delete pods, logs or instances, take snapshots instead and isolate affected systems from the network rather than wiping them. Do not alert the attacker by making visible changes before a plan exists, unless you must stop active damage. Write down everything you see and do with timestamps, and do not discuss details in public channels.

## 425: How do you debug a suspected broken access control (IDOR) bug?

Find out if one user can read or change another user's data by changing an ID in the request. Reproduce with two test accounts: get user A's resource ID and request it with user B's token. Check the code path: does it load the record by ID only (`findUnique({ where: { id } })`) instead of by ID and owner? Search access logs for requests where the user ID and the owner of the resource differ, to see if it was used. Add tests that check access is denied for other users.

## 426: How do you debug TLS handshake failures?

Get the exact error and test the handshake directly:

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com -tls1_2
openssl s_client -connect api.example.com:443 -servername api.example.com -tls1_3
NODE_DEBUG=tls node client.js
```

Common causes: the client and server have no TLS version or cipher in common (an old client against a server that only allows TLS 1.2+), missing SNI, or an mTLS server that wants a client certificate. `ERR_SSL_WRONG_VERSION_NUMBER` often means you are speaking TLS to a plain HTTP port, for example using `https://` with port 80.

## 427: Certificate checks fail only on some machines or old images. Why?

Each machine trusts the roots in its own CA store. Old base images or old systems may have an outdated store that is missing new roots, or still prefers an old expired chain. The expiry of the DST Root CA X3 root in 2021 broke many old clients this way. Check the `ca-certificates` package version in the image, update the base image, and compare the chain from `openssl s_client` with what the client trusts. Node.js uses its own bundled CA list by default, so updating the OS store alone may not change Node's behavior.

## 428: How do you debug a certificate that did not renew automatically?

With cert-manager, check its resources in order: `kubectl describe certificate`, then the `CertificateRequest`, the `Order` and the `Challenge`. The challenge status says why it failed, for example the HTTP-01 path is blocked by a redirect or auth, a WAF blocks the ACME server, or DNS-01 cannot create the record because of missing permissions. Also check rate limits from the CA. Prevent surprises with an alert on the number of days until expiry for every public certificate.

## 429: Why do you get an endless redirect loop after enabling HTTPS behind a load balancer?

TLS ends at the load balancer, which sends plain HTTP to the app. The app sees `http`, redirects to `https`, the load balancer sends it as HTTP again, and so on. The app should trust the proxy and read `X-Forwarded-Proto`:

```js
app.set("trust proxy", 1);
app.use((req, res, next) =>
  req.secure
    ? next()
    : res.redirect(301, `https://${req.get("host")}${req.originalUrl}`),
);
```

Or do the redirect at the load balancer only. Check with `curl -v -L --max-redirs 5` to see the chain of `Location` headers.

## 430: How does SNI cause wrong certificate errors?

When one IP address serves many domains, the client tells the server which name it wants with SNI during the handshake. If the client does not send SNI (some old clients, or tools used without the option), the server returns its default certificate, which does not match the name. That is why `openssl s_client` needs `-servername`. In Node, `tls.connect` sets SNI from `host` automatically, but if you connect by IP, set `servername` yourself.

## 431: Several unrelated auth features started failing at the same time. Could the clock be the cause?

Yes. Many security checks depend on time: JWT `exp` and `nbf`, SAML assertion validity windows, TOTP codes (30-second windows), signed URLs, AWS request signatures (rejected if more than 15 minutes off, `RequestTimeTooSkewed`), and certificate validity. If several of these fail on one host at once, check its clock and NTP status (`timedatectl`). Containers use the host's clock, so the problem is on the node or VM.

## 432: How do you debug a SignatureDoesNotMatch error for signed requests or URLs?

The server calculated a different signature than the client. Common causes: wrong secret or key, a different region or service in the signature, the URL or headers changed after signing (a proxy adding or changing headers, re-encoding the path, changing `+` and `%20`), a different `Content-Type` than the one signed, or a clock difference. AWS error responses include the string the server signed (the canonical request), which you can compare with what your client signed. Sign as late as possible, after all headers are final.

## 433: A secret rotation caused an outage. How do you debug it and avoid it next time?

Some service still uses the old secret: it cached it at startup, reads it from an old config, or was not restarted. Find which clients fail and what credential they send (by key ID or version, not the value). Next time, rotate in steps: add the new secret while the old one still works, move all clients to the new one, confirm with metrics or logs that the old one is no longer used, then remove the old one. For JWT keys, publish the new key in the JWKS before you start signing with it.

## 434: Token validation makes every request slow. How do you debug it?

Profile or trace the auth middleware. Common causes: fetching the JWKS from the identity provider on every request instead of caching it, calling an introspection endpoint for every request without a cache, or running bcrypt or another slow hash on each request (for example API keys stored as bcrypt hashes and checked on every call). Cache the key set, cache introspection results for a short time, and use a fast hash (like SHA-256 of a long random key) for API key lookup.

## 435: How do you debug a 403 that comes from a WAF and not from your app?

If your app logs show no such request, something in front of it blocked it. Check the WAF logs (AWS WAF, Cloudflare, Azure Front Door) for the request by time, IP or a request ID header. They show which rule matched. False positives are common with JSON bodies that contain SQL-like or HTML-like text, large bodies and unusual headers. Fix it with a narrow exception for that rule and path, not by turning the WAF off.

## 436: A user reports an auth problem. How do you debug it without asking for their password or token?

Never ask users to send passwords, tokens or session cookies. Use the request ID or time of their failed attempt, their user ID, and your logs and identity provider logs to see what happened (account locked, wrong tenant, expired session, MFA failure). If you need to see what they see, use an impersonation feature that is limited to support staff, requires a reason, and is audited. Or reproduce it with a test account in the same setup.

## 437: What should a logging policy for a back-end team include?

- Which events to log at each level, and the default level in each environment.
- Required fields: timestamp, service, version, request ID, trace ID.
- A list of data that must never be logged (secrets, tokens, passwords, card data) and data that must be masked (emails, names, IPs).
- Shared redaction config in a common logger package.
- Retention periods and who can access logs.
- How to report and handle a leak.

A shared logger setup makes the safe way the easy way, so people do not have to remember rules.

## 438: You found a token in production logs. What do you do?

1. Revoke or rotate the token right away; deleting the log line does not make it safe.
2. Find out how long it has been happening and which tokens or users are affected.
3. Fix the code that logs it and add a redaction rule as a backup.
4. Delete or mask the affected log data in every place it was copied (log backend, archives, exports), if your tools allow it.
5. Check access logs for use of the leaked tokens, and follow the incident process if personal data was involved.

Add a test or a log scanner that alerts on token patterns, so it is caught earlier next time.

## 439: Why are heap snapshots, core dumps and diagnostic reports sensitive?

A heap snapshot or core dump contains everything in memory: secrets loaded from config, database passwords, tokens of in-flight requests and users' personal data. A diagnostic report contains environment variables. Treat these files like production data: store them encrypted with limited access, do not attach them to public issues, do not copy them to personal laptops without permission, and delete them when the investigation is done.

## 440: If you must attach a debugger in production, how do you do it safely?

Avoid it if logs, traces and profiles can answer the question. If not:

1. Pick one instance and remove it from the load balancer, so pausing it affects no users.
2. Keep the inspector bound to `127.0.0.1` and reach it with `kubectl port-forward` or an SSH tunnel, never a public port.
3. Prefer logpoints over breakpoints so the process does not pause.
4. Get approval and log what you did.
5. Restart or replace the instance afterwards so it does not stay in debug mode.

## 441: What is break-glass access and why is it used for production debugging?

Break-glass access is emergency access with higher permissions (for example write access to the production database) that is not normally given to anyone. Using it requires a reason, is time-limited, alerts other people, and is fully audited. It lets engineers fix serious incidents quickly while keeping day-to-day access small. Review every use afterwards.

## 442: Is it safe to SSH into a CI runner to debug a failing job?

Tools that open a remote shell into a GitHub Actions runner (like tmate actions) are handy, but the shell has access to everything the job has: secrets, the `GITHUB_TOKEN` and cloud credentials from OIDC. Only do it in private repositories, only on failure, limit access to your own GitHub user (most such tools have an option for this), and set a short timeout. Often a better first step is to reproduce locally with the same container image, or with a tool like `act`, using test credentials.

## 443: Is hashing user IDs or emails in logs enough to protect personal data?

Not always. A plain hash of an email can be reversed by hashing a list of known emails and comparing. Use a keyed hash (HMAC) with a secret key so the same user always gets the same value (good for debugging and counting) but it cannot be reversed without the key. Even then, it is still personal data under laws like GDPR if you can link it back, so retention and access rules still apply. Often an internal user ID is simpler and enough.

```js
import { createHmac } from "node:crypto";
const pseudo = (value) =>
  createHmac("sha256", process.env.LOG_HASH_KEY)
    .update(value)
    .digest("hex")
    .slice(0, 16);
logger.info({ user: pseudo(email) }, "password reset requested");
```

## 444: What are the risks of logging the full event in serverless functions?

A common habit is `console.log(JSON.stringify(event))` at the start of a Lambda or Cloud Function. For API events, that includes headers with `Authorization` tokens and cookies, the full body (passwords, personal data) and query strings. For queue or stream events, it includes the whole payload. Log selected fields instead (route, request ID, record IDs, sizes), and if you need the full event to debug, log it only in non-production environments or behind a short-lived flag with redaction.

## 445: Why should audit logs be kept separate from debug logs?

They have different purposes and rules. Audit logs record who did what (logins, permission changes, data exports) for security and compliance, must be complete and tamper-resistant, and are often kept for a long time. Debug logs are for engineers, can be sampled or dropped, and should be kept for a short time. Mixing them means either keeping noisy debug data for years or losing audit data when you reduce log volume.

## 446: How do data deletion requests affect logs?

Under laws like GDPR, a user can ask for their personal data to be deleted, and that includes copies in logs, backups and analytics, unless there is a legal reason to keep them. Deleting single entries from logs is hard, which is why the best approach is to keep personal data out of logs, use internal IDs, and set short retention so old logs expire on their own. Document what your logs contain so you can answer these requests.

## 447: How can APM and monitoring agents leak data, and how do you configure them?

APM agents capture a lot by default or with one setting: SQL statements with parameters, HTTP headers, request bodies, URLs with query strings, and error messages. All of it is sent to a third party. Check the agent's capture settings and turn off or mask parameters, headers and bodies. Look at what really arrives in the APM tool for a few requests. Treat the vendor as a data processor, which may need an agreement and a review.

## 448: What debug features must not be left on in production?

- Stack traces in API error responses (they reveal code paths and library versions).
- Debug or admin endpoints without auth, like `/debug`, heap dump or profile endpoints.
- GraphQL introspection and playgrounds on private APIs, if you do not want the schema public.
- The Node inspector port open to the network.
- Verbose logging levels left on after an incident.
- Test users, backdoor flags or "skip auth" settings.

Check for these in a release checklist or automated tests, for example a test that a 500 response body has no stack trace when `NODE_ENV=production`.

## 449: How do you return useful errors to API clients without leaking internal details?

Send the client a stable error code, a short safe message and the request ID. Keep the stack trace, SQL error and internal details in your logs, linked by that same request ID. So support can find the full error from what the client reports, while attackers learn nothing about your internals.

```json
{
  "error": {
    "code": "PAYMENT_PROVIDER_UNAVAILABLE",
    "message": "Payment could not be processed. Please try again.",
    "requestId": "req_7f3a2c"
  }
}
```

Validation errors can be more detailed (which field is wrong), since that information is about the client's own input.

## 450: An engineer accidentally logged full request bodies, including passwords, in production for two days. What do you do?

1. Stop it: deploy the fix or turn off the logging right away.
2. Find out the scope: which endpoints, which time window, how many users, and which systems got copies (log backend, archives, APM, alerting tools, exports).
3. Delete or mask the data everywhere it went, and record what could not be deleted.
4. Treat the passwords as exposed: force password resets for affected users and revoke their sessions. Revoke any tokens or keys that were in the logs.
5. Check who accessed the logs during that time.
6. Follow the incident process, including legal or privacy teams, since data protection laws may require notifying authorities or users.
7. Write a blameless postmortem and add guards: redaction in the shared logger, a log scanner for password and token patterns, and review rules for logging changes.
