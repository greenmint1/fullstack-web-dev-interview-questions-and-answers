# Node.js Microservices Interview Questions and Answers

_Last updated: October 28, 2026_

450 Node.js microservices interview questions with answers and code examples, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Node.js 24 (Active LTS) and Node.js 26 (LTS from October 2026), with current versions of the common tools: Express 5, Fastify 5, NestJS, `@grpc/grpc-js`, `amqplib` with RabbitMQ 4.x, `kafkajs` and Confluent's client with Kafka 4.x, BullMQ, OpenTelemetry JS SDK 2.x, Docker and Kubernetes. Code examples use ES modules. Older approaches are mentioned where you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a microservice?](#1-what-is-a-microservice)
- [2: What is a monolith?](#2-what-is-a-monolith)
- [3: What is the difference between a monolith and microservices?](#3-what-is-the-difference-between-a-monolith-and-microservices)
- [4: What are the main benefits of microservices?](#4-what-are-the-main-benefits-of-microservices)
- [5: What are the main drawbacks of microservices?](#5-what-are-the-main-drawbacks-of-microservices)
- [6: Why is Node.js a good fit for microservices?](#6-why-is-nodejs-a-good-fit-for-microservices)
- [7: When should you not use microservices?](#7-when-should-you-not-use-microservices)
- [8: What is a modular monolith?](#8-what-is-a-modular-monolith)
- [9: What is a distributed monolith?](#9-what-is-a-distributed-monolith)
- [10: What is a service boundary?](#10-what-is-a-service-boundary)
- [11: What is a bounded context?](#11-what-is-a-bounded-context)
- [12: What is Domain-Driven Design and how does it relate to microservices?](#12-what-is-domain-driven-design-and-how-does-it-relate-to-microservices)
- [13: What does "single responsibility" mean for a microservice?](#13-what-does-single-responsibility-mean-for-a-microservice)
- [14: How big should a microservice be?](#14-how-big-should-a-microservice-be)
- [15: What does "loose coupling" mean in microservices?](#15-what-does-loose-coupling-mean-in-microservices)
- [16: What does "high cohesion" mean in microservices?](#16-what-does-high-cohesion-mean-in-microservices)
- [17: What is synchronous communication between services?](#17-what-is-synchronous-communication-between-services)
- [18: What is asynchronous communication between services?](#18-what-is-asynchronous-communication-between-services)
- [19: When would you choose synchronous over asynchronous communication?](#19-when-would-you-choose-synchronous-over-asynchronous-communication)
- [20: What is REST?](#20-what-is-rest)
- [21: What is gRPC?](#21-what-is-grpc)
- [22: What are Protocol Buffers?](#22-what-are-protocol-buffers)
- [23: What is a message broker?](#23-what-is-a-message-broker)
- [24: What is the difference between a queue and a topic?](#24-what-is-the-difference-between-a-queue-and-a-topic)
- [25: What is event-driven architecture?](#25-what-is-event-driven-architecture)
- [26: What is the difference between an event and a command?](#26-what-is-the-difference-between-an-event-and-a-command)
- [27: What is an API gateway?](#27-what-is-an-api-gateway)
- [28: Why use an API gateway instead of letting clients call services directly?](#28-why-use-an-api-gateway-instead-of-letting-clients-call-services-directly)
- [29: What is service discovery?](#29-what-is-service-discovery)
- [30: What is the difference between client-side and server-side discovery?](#30-what-is-the-difference-between-client-side-and-server-side-discovery)
- [31: What is a load balancer?](#31-what-is-a-load-balancer)
- [32: What is a reverse proxy?](#32-what-is-a-reverse-proxy)
- [33: What does "stateless service" mean?](#33-what-does-stateless-service-mean)
- [34: What is horizontal scaling vs vertical scaling?](#34-what-is-horizontal-scaling-vs-vertical-scaling)
- [35: What is the "database per service" pattern?](#35-what-is-the-database-per-service-pattern)
- [36: Why is sharing a database between services a problem?](#36-why-is-sharing-a-database-between-services-a-problem)
- [37: What is eventual consistency?](#37-what-is-eventual-consistency)
- [38: What is the CAP theorem?](#38-what-is-the-cap-theorem)
- [39: What is a health check?](#39-what-is-a-health-check)
- [40: What is the difference between liveness and readiness?](#40-what-is-the-difference-between-liveness-and-readiness)
- [41: What is containerization and why is it used with microservices?](#41-what-is-containerization-and-why-is-it-used-with-microservices)
- [42: What does a basic Dockerfile for a Node.js service look like?](#42-what-does-a-basic-dockerfile-for-a-nodejs-service-look-like)
- [43: What is Kubernetes and why is it used for microservices?](#43-what-is-kubernetes-and-why-is-it-used-for-microservices)
- [44: What is a container orchestrator?](#44-what-is-a-container-orchestrator)
- [45: What are environment variables used for in microservices?](#45-what-are-environment-variables-used-for-in-microservices)
- [46: How do you load a .env file in Node.js without extra packages?](#46-how-do-you-load-a-env-file-in-nodejs-without-extra-packages)
- [47: What is the Twelve-Factor App?](#47-what-is-the-twelve-factor-app)
- [48: Why should logs go to stdout in a containerized service?](#48-why-should-logs-go-to-stdout-in-a-containerized-service)
- [49: What is centralized logging?](#49-what-is-centralized-logging)
- [50: What is structured logging?](#50-what-is-structured-logging)
- [51: What is a correlation ID?](#51-what-is-a-correlation-id)
- [52: What is distributed tracing?](#52-what-is-distributed-tracing)
- [53: What is OpenTelemetry?](#53-what-is-opentelemetry)
- [54: What are metrics and why do they matter?](#54-what-are-metrics-and-why-do-they-matter)
- [55: What is Prometheus?](#55-what-is-prometheus)
- [56: What are the three pillars of observability?](#56-what-are-the-three-pillars-of-observability)
- [57: Why are timeouts important in microservices?](#57-why-are-timeouts-important-in-microservices)
- [58: What is a retry and when should you retry a request?](#58-what-is-a-retry-and-when-should-you-retry-a-request)
- [59: What is exponential backoff?](#59-what-is-exponential-backoff)
- [60: What is idempotency?](#60-what-is-idempotency)
- [61: What is an idempotency key?](#61-what-is-an-idempotency-key)
- [62: What is the circuit breaker pattern?](#62-what-is-the-circuit-breaker-pattern)
- [63: What is a fallback?](#63-what-is-a-fallback)
- [64: What is graceful degradation?](#64-what-is-graceful-degradation)
- [65: What is rate limiting?](#65-what-is-rate-limiting)
- [66: Why is caching used in microservices?](#66-why-is-caching-used-in-microservices)
- [67: What is Redis and how is it used with microservices?](#67-what-is-redis-and-how-is-it-used-with-microservices)
- [68: What is a JWT?](#68-what-is-a-jwt)
- [69: How does authentication usually work in a microservices system?](#69-how-does-authentication-usually-work-in-a-microservices-system)
- [70: What is the difference between authentication and authorization?](#70-what-is-the-difference-between-authentication-and-authorization)
- [71: What is OAuth 2.0?](#71-what-is-oauth-20)
- [72: How do services authenticate each other?](#72-how-do-services-authenticate-each-other)
- [73: What is CORS and where should it be handled?](#73-what-is-cors-and-where-should-it-be-handled)
- [74: What is API versioning?](#74-what-is-api-versioning)
- [75: What is a breaking change in an API?](#75-what-is-a-breaking-change-in-an-api)
- [76: What is OpenAPI?](#76-what-is-openapi)
- [77: Why should you validate incoming requests in every service?](#77-why-should-you-validate-incoming-requests-in-every-service)
- [78: How do you return errors from a REST microservice?](#78-how-do-you-return-errors-from-a-rest-microservice)
- [79: What HTTP status codes do microservices use most?](#79-what-http-status-codes-do-microservices-use-most)
- [80: Which Node.js frameworks are commonly used to build microservices?](#80-which-nodejs-frameworks-are-commonly-used-to-build-microservices)
- [81: What is Fastify and why is it popular for microservices?](#81-what-is-fastify-and-why-is-it-popular-for-microservices)
- [82: Why do you need to listen on 0.0.0.0 inside a container?](#82-why-do-you-need-to-listen-on-0000-inside-a-container)
- [83: What is NestJS microservices?](#83-what-is-nestjs-microservices)
- [84: What is a monorepo and why is it used for microservices?](#84-what-is-a-monorepo-and-why-is-it-used-for-microservices)
- [85: What is a polyrepo?](#85-what-is-a-polyrepo)
- [86: Should microservices share code?](#86-should-microservices-share-code)
- [87: What is semantic versioning and why does it matter for services?](#87-what-is-semantic-versioning-and-why-does-it-matter-for-services)
- [88: What is CI/CD in the context of microservices?](#88-what-is-cicd-in-the-context-of-microservices)
- [89: What is a rolling deployment?](#89-what-is-a-rolling-deployment)
- [90: What is a blue-green deployment?](#90-what-is-a-blue-green-deployment)
- [91: What is a canary release?](#91-what-is-a-canary-release)
- [92: What is a feature flag?](#92-what-is-a-feature-flag)
- [93: What is graceful shutdown?](#93-what-is-graceful-shutdown)
- [94: What is SIGTERM and how do you handle it in Node.js?](#94-what-is-sigterm-and-how-do-you-handle-it-in-nodejs)
- [95: What is the Node.js cluster module?](#95-what-is-the-nodejs-cluster-module)
- [96: What is PM2?](#96-what-is-pm2)
- [97: What is the Backend for Frontend (BFF) pattern?](#97-what-is-the-backend-for-frontend-bff-pattern)
- [98: What is the difference between a microservice and a serverless function?](#98-what-is-the-difference-between-a-microservice-and-a-serverless-function)
- [99: What are webhooks?](#99-what-are-webhooks)
- [100: What is the difference between polling and push-based communication?](#100-what-is-the-difference-between-polling-and-push-based-communication)
- [101: What is RabbitMQ?](#101-what-is-rabbitmq)
- [102: What are the exchange types in RabbitMQ?](#102-what-are-the-exchange-types-in-rabbitmq)
- [103: What is Apache Kafka?](#103-what-is-apache-kafka)
- [104: What are topics, partitions and offsets in Kafka?](#104-what-are-topics-partitions-and-offsets-in-kafka)
- [105: What is a consumer group in Kafka?](#105-what-is-a-consumer-group-in-kafka)
- [106: What is BullMQ?](#106-what-is-bullmq)
- [107: What is a dead letter queue?](#107-what-is-a-dead-letter-queue)
- [108: What does acknowledging a message mean?](#108-what-does-acknowledging-a-message-mean)
- [109: What are the message delivery guarantees?](#109-what-are-the-message-delivery-guarantees)
- [110: Why should message consumers be idempotent?](#110-why-should-message-consumers-be-idempotent)
- [111: What should a message or event contain?](#111-what-should-a-message-or-event-contain)
- [112: What is CloudEvents?](#112-what-is-cloudevents)
- [113: What is the saga pattern?](#113-what-is-the-saga-pattern)
- [114: What is a compensating transaction?](#114-what-is-a-compensating-transaction)
- [115: What is the outbox pattern?](#115-what-is-the-outbox-pattern)
- [116: What is the strangler fig pattern?](#116-what-is-the-strangler-fig-pattern)
- [117: How do you run several microservices locally?](#117-how-do-you-run-several-microservices-locally)
- [118: What types of tests are used for microservices?](#118-what-types-of-tests-are-used-for-microservices)
- [119: What is contract testing?](#119-what-is-contract-testing)
- [120: Why are end-to-end tests hard with microservices?](#120-why-are-end-to-end-tests-hard-with-microservices)
- [121: What is Testcontainers?](#121-what-is-testcontainers)
- [122: What is a service mesh?](#122-what-is-a-service-mesh)
- [123: What is a sidecar?](#123-what-is-a-sidecar)
- [124: What is mutual TLS (mTLS)?](#124-what-is-mutual-tls-mtls)
- [125: How should microservices handle secrets?](#125-how-should-microservices-handle-secrets)
- [126: What is centralized configuration?](#126-what-is-centralized-configuration)
- [127: What is the difference between configuration and secrets?](#127-what-is-the-difference-between-configuration-and-secrets)
- [128: What are WebSockets and when would a microservice use them?](#128-what-are-websockets-and-when-would-a-microservice-use-them)
- [129: What are Server-Sent Events?](#129-what-are-server-sent-events)
- [130: What is API composition?](#130-what-is-api-composition)
- [131: What is CQRS?](#131-what-is-cqrs)
- [132: What is event sourcing?](#132-what-is-event-sourcing)
- [133: Is it okay to duplicate data between microservices?](#133-is-it-okay-to-duplicate-data-between-microservices)
- [134: What are sticky sessions and why are they usually avoided?](#134-what-are-sticky-sessions-and-why-are-they-usually-avoided)
- [135: What is HTTP keep-alive and why does it matter between services?](#135-what-is-http-keep-alive-and-why-does-it-matter-between-services)
- [136: How do you make HTTP calls to other services in Node.js?](#136-how-do-you-make-http-calls-to-other-services-in-nodejs)
- [137: How do you generate unique IDs in a distributed system?](#137-how-do-you-generate-unique-ids-in-a-distributed-system)
- [138: Why should services use UTC for timestamps?](#138-why-should-services-use-utc-for-timestamps)
- [139: How do you paginate results in a microservice API?](#139-how-do-you-paginate-results-in-a-microservice-api)
- [140: What is autoscaling?](#140-what-is-autoscaling)
- [141: What are SLI, SLO and SLA?](#141-what-are-sli-slo-and-sla)
- [142: What do p50, p95 and p99 latency mean?](#142-what-do-p50-p95-and-p99-latency-mean)
- [143: What is the difference between latency and throughput?](#143-what-is-the-difference-between-latency-and-throughput)
- [144: What is the bulkhead pattern?](#144-what-is-the-bulkhead-pattern)
- [145: What is Conway's Law and why does it matter for microservices?](#145-what-is-conways-law-and-why-does-it-matter-for-microservices)
- [146: What does "you build it, you run it" mean?](#146-what-does-you-build-it-you-run-it-mean)
- [147: What is the W3C Trace Context?](#147-what-is-the-w3c-trace-context)
- [148: How do you pin the Node.js version for a service?](#148-how-do-you-pin-the-nodejs-version-for-a-service)
- [149: Can you run TypeScript directly in Node.js services?](#149-can-you-run-typescript-directly-in-nodejs-services)
- [150: What is the difference between npm install and npm ci?](#150-what-is-the-difference-between-npm-install-and-npm-ci)

### Moderate Questions (151-300)

- [151: How do you implement a full graceful shutdown in a Node.js service?](#151-how-do-you-implement-a-full-graceful-shutdown-in-a-nodejs-service)
- [152: How do you implement liveness and readiness endpoints?](#152-how-do-you-implement-liveness-and-readiness-endpoints)
- [153: How do you configure Kubernetes probes for a Node.js service?](#153-how-do-you-configure-kubernetes-probes-for-a-nodejs-service)
- [154: Why do you sometimes need a delay before shutting down in Kubernetes?](#154-why-do-you-sometimes-need-a-delay-before-shutting-down-in-kubernetes)
- [155: How do you implement retries with exponential backoff and jitter?](#155-how-do-you-implement-retries-with-exponential-backoff-and-jitter)
- [156: What is retry amplification and how do you avoid it?](#156-what-is-retry-amplification-and-how-do-you-avoid-it)
- [157: How do you use a circuit breaker in Node.js?](#157-how-do-you-use-a-circuit-breaker-in-nodejs)
- [158: What is deadline propagation?](#158-what-is-deadline-propagation)
- [159: How do you tune connection pooling for outgoing HTTP calls?](#159-how-do-you-tune-connection-pooling-for-outgoing-http-calls)
- [160: How do you create a gRPC server in Node.js?](#160-how-do-you-create-a-grpc-server-in-nodejs)
- [161: How do you call a gRPC service with a deadline?](#161-how-do-you-call-a-grpc-service-with-a-deadline)
- [162: What types of gRPC calls are there?](#162-what-types-of-grpc-calls-are-there)
- [163: How do gRPC status codes map to HTTP status codes?](#163-how-do-grpc-status-codes-map-to-http-status-codes)
- [164: When would you pick gRPC over REST for service-to-service calls?](#164-when-would-you-pick-grpc-over-rest-for-service-to-service-calls)
- [165: Why can gRPC load balancing be a problem in Kubernetes?](#165-why-can-grpc-load-balancing-be-a-problem-in-kubernetes)
- [166: How do you publish messages to RabbitMQ reliably with amqplib?](#166-how-do-you-publish-messages-to-rabbitmq-reliably-with-amqplib)
- [167: How do you consume messages from RabbitMQ safely?](#167-how-do-you-consume-messages-from-rabbitmq-safely)
- [168: How do you implement delayed retries in RabbitMQ?](#168-how-do-you-implement-delayed-retries-in-rabbitmq)
- [169: What is the difference between classic and quorum queues in RabbitMQ?](#169-what-is-the-difference-between-classic-and-quorum-queues-in-rabbitmq)
- [170: How do you produce messages to Kafka from Node.js?](#170-how-do-you-produce-messages-to-kafka-from-nodejs)
- [171: How do you consume messages from Kafka and commit offsets?](#171-how-do-you-consume-messages-from-kafka-and-commit-offsets)
- [172: How do you choose a partition key in Kafka?](#172-how-do-you-choose-a-partition-key-in-kafka)
- [173: What is consumer lag and why should you monitor it?](#173-what-is-consumer-lag-and-why-should-you-monitor-it)
- [174: What is a consumer group rebalance in Kafka?](#174-what-is-a-consumer-group-rebalance-in-kafka)
- [175: What is the difference between Redis pub/sub and Redis Streams?](#175-what-is-the-difference-between-redis-pubsub-and-redis-streams)
- [176: How do you use Redis Streams with consumer groups in Node.js?](#176-how-do-you-use-redis-streams-with-consumer-groups-in-nodejs)
- [177: How do you configure retries and concurrency in BullMQ?](#177-how-do-you-configure-retries-and-concurrency-in-bullmq)
- [178: How do you implement the outbox pattern in Node.js with PostgreSQL?](#178-how-do-you-implement-the-outbox-pattern-in-nodejs-with-postgresql)
- [179: What is the difference between a polling outbox relay and CDC?](#179-what-is-the-difference-between-a-polling-outbox-relay-and-cdc)
- [180: What is the inbox pattern?](#180-what-is-the-inbox-pattern)
- [181: What is the difference between choreography and orchestration in sagas?](#181-what-is-the-difference-between-choreography-and-orchestration-in-sagas)
- [182: How would you implement a simple orchestrated saga in Node.js?](#182-how-would-you-implement-a-simple-orchestrated-saga-in-nodejs)
- [183: How do you build a simple API gateway in Node.js?](#183-how-do-you-build-a-simple-api-gateway-in-nodejs)
- [184: How do you implement rate limiting across many instances?](#184-how-do-you-implement-rate-limiting-across-many-instances)
- [185: What are the common rate limiting algorithms?](#185-what-are-the-common-rate-limiting-algorithms)
- [186: How do you verify JWTs in a Node.js service?](#186-how-do-you-verify-jwts-in-a-nodejs-service)
- [187: How do you pass user identity to downstream services?](#187-how-do-you-pass-user-identity-to-downstream-services)
- [188: How do you get and cache a token for service-to-service calls?](#188-how-do-you-get-and-cache-a-token-for-service-to-service-calls)
- [189: How do you set up Pino logging for a microservice?](#189-how-do-you-set-up-pino-logging-for-a-microservice)
- [190: What is AsyncLocalStorage and how is it used in microservices?](#190-what-is-asynclocalstorage-and-how-is-it-used-in-microservices)
- [191: How do you propagate a correlation ID to other services?](#191-how-do-you-propagate-a-correlation-id-to-other-services)
- [192: How do you set up OpenTelemetry in a Node.js service?](#192-how-do-you-set-up-opentelemetry-in-a-nodejs-service)
- [193: How do you create custom spans with OpenTelemetry?](#193-how-do-you-create-custom-spans-with-opentelemetry)
- [194: What is trace sampling and why is it needed?](#194-what-is-trace-sampling-and-why-is-it-needed)
- [195: How do you measure HTTP request duration with prom-client?](#195-how-do-you-measure-http-request-duration-with-prom-client)
- [196: What is high cardinality in metrics and why is it a problem?](#196-what-is-high-cardinality-in-metrics-and-why-is-it-a-problem)
- [197: What should you alert on in a microservices system?](#197-what-should-you-alert-on-in-a-microservices-system)
- [198: How do you write a multi-stage Dockerfile for a TypeScript service?](#198-how-do-you-write-a-multi-stage-dockerfile-for-a-typescript-service)
- [199: Which Node.js base image should you use for a service?](#199-which-nodejs-base-image-should-you-use-for-a-service)
- [200: Why does it matter which process is PID 1 in a container?](#200-why-does-it-matter-which-process-is-pid-1-in-a-container)
- [201: How does Node.js handle memory limits in containers?](#201-how-does-nodejs-handle-memory-limits-in-containers)
- [202: How should you set CPU and memory requests and limits for Node.js pods?](#202-how-should-you-set-cpu-and-memory-requests-and-limits-for-nodejs-pods)
- [203: How do you validate configuration at startup?](#203-how-do-you-validate-configuration-at-startup)
- [204: How do you validate request bodies in an Express service?](#204-how-do-you-validate-request-bodies-in-an-express-service)
- [205: How does error handling work with async routes in Express 5?](#205-how-does-error-handling-work-with-async-routes-in-express-5)
- [206: How do you design error handling across services?](#206-how-do-you-design-error-handling-across-services)
- [207: How should a service handle unhandledRejection and uncaughtException?](#207-how-should-a-service-handle-unhandledrejection-and-uncaughtexception)
- [208: How do you change an event schema without breaking consumers?](#208-how-do-you-change-an-event-schema-without-breaking-consumers)
- [209: What is the tolerant reader pattern?](#209-what-is-the-tolerant-reader-pattern)
- [210: What is a schema registry?](#210-what-is-a-schema-registry)
- [211: What does a consumer-driven contract test with Pact look like?](#211-what-does-a-consumer-driven-contract-test-with-pact-look-like)
- [212: How do you integration test a Kafka consumer?](#212-how-do-you-integration-test-a-kafka-consumer)
- [213: How do you mock other services in unit and component tests?](#213-how-do-you-mock-other-services-in-unit-and-component-tests)
- [214: How do you implement cache-aside with Redis?](#214-how-do-you-implement-cache-aside-with-redis)
- [215: How do you invalidate caches across services?](#215-how-do-you-invalidate-caches-across-services)
- [216: What is a cache stampede and how do you prevent it?](#216-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [217: Can services use HTTP caching between each other?](#217-can-services-use-http-caching-between-each-other)
- [218: How do you implement a simple distributed lock with Redis?](#218-how-do-you-implement-a-simple-distributed-lock-with-redis)
- [219: How do you handle database migrations in microservices?](#219-how-do-you-handle-database-migrations-in-microservices)
- [220: What is the expand and contract pattern for schema changes?](#220-what-is-the-expand-and-contract-pattern-for-schema-changes)
- [221: How do you query data that lives in several services?](#221-how-do-you-query-data-that-lives-in-several-services)
- [222: How do you handle partial failures when combining responses?](#222-how-do-you-handle-partial-failures-when-combining-responses)
- [223: How is GraphQL used in a microservices architecture?](#223-how-is-graphql-used-in-a-microservices-architecture)
- [224: What is GraphQL Federation?](#224-what-is-graphql-federation)
- [225: How do you decide between REST, gRPC and messaging for a new interaction?](#225-how-do-you-decide-between-rest-grpc-and-messaging-for-a-new-interaction)
- [226: How do you run HTTP and a message consumer in the same NestJS app?](#226-how-do-you-run-http-and-a-message-consumer-in-the-same-nestjs-app)
- [227: What is the difference between send and emit in a NestJS ClientProxy?](#227-what-is-the-difference-between-send-and-emit-in-a-nestjs-clientproxy)
- [228: How do you use Kafka with NestJS?](#228-how-do-you-use-kafka-with-nestjs)
- [229: What is Moleculer?](#229-what-is-moleculer)
- [230: How do you organize a Node.js microservices monorepo?](#230-how-do-you-organize-a-nodejs-microservices-monorepo)
- [231: How do you share API contracts between services?](#231-how-do-you-share-api-contracts-between-services)
- [232: How do you set up CI to build only the services that changed?](#232-how-do-you-set-up-ci-to-build-only-the-services-that-changed)
- [233: How should you tag Docker images for microservices?](#233-how-should-you-tag-docker-images-for-microservices)
- [234: What does a basic Kubernetes Deployment for a Node.js service look like?](#234-what-does-a-basic-kubernetes-deployment-for-a-nodejs-service-look-like)
- [235: How do services find each other in Kubernetes?](#235-how-do-services-find-each-other-in-kubernetes)
- [236: How do you pass ConfigMaps and Secrets to a Node.js service?](#236-how-do-you-pass-configmaps-and-secrets-to-a-nodejs-service)
- [237: What is the difference between an Ingress and the Gateway API in Kubernetes?](#237-what-is-the-difference-between-an-ingress-and-the-gateway-api-in-kubernetes)
- [238: What is Helm and why is it used for microservices?](#238-what-is-helm-and-why-is-it-used-for-microservices)
- [239: How do you control a rolling update in Kubernetes?](#239-how-do-you-control-a-rolling-update-in-kubernetes)
- [240: What is a PodDisruptionBudget?](#240-what-is-a-poddisruptionbudget)
- [241: How do you run batch jobs and scheduled tasks in Kubernetes?](#241-how-do-you-run-batch-jobs-and-scheduled-tasks-in-kubernetes)
- [242: How do you make sure a scheduled task runs only once when you have many instances?](#242-how-do-you-make-sure-a-scheduled-task-runs-only-once-when-you-have-many-instances)
- [243: What is leader election?](#243-what-is-leader-election)
- [244: How do you detect event loop blocking in a Node.js service?](#244-how-do-you-detect-event-loop-blocking-in-a-nodejs-service)
- [245: When and how do you use worker threads in a microservice?](#245-when-and-how-do-you-use-worker-threads-in-a-microservice)
- [246: How do you stream large data between services?](#246-how-do-you-stream-large-data-between-services)
- [247: How do you handle file uploads in a microservices system?](#247-how-do-you-handle-file-uploads-in-a-microservices-system)
- [248: Why should every service set request size limits?](#248-why-should-every-service-set-request-size-limits)
- [249: How do you verify webhook signatures in Node.js?](#249-how-do-you-verify-webhook-signatures-in-nodejs)
- [250: How do you process incoming webhooks reliably?](#250-how-do-you-process-incoming-webhooks-reliably)
- [251: How would you design a notification service?](#251-how-would-you-design-a-notification-service)
- [252: How do you keep a search index in sync with other services?](#252-how-do-you-keep-a-search-index-in-sync-with-other-services)
- [253: How do you pass tenant context through a multi-tenant system?](#253-how-do-you-pass-tenant-context-through-a-multi-tenant-system)
- [254: How do you delete a user's data across all services (for example for GDPR)?](#254-how-do-you-delete-a-users-data-across-all-services-for-example-for-gdpr)
- [255: How do you implement idempotency keys in an Express service?](#255-how-do-you-implement-idempotency-keys-in-an-express-service)
- [256: What is optimistic concurrency control?](#256-what-is-optimistic-concurrency-control)
- [257: How do you use ETag and If-Match to prevent lost updates in an API?](#257-how-do-you-use-etag-and-if-match-to-prevent-lost-updates-in-an-api)
- [258: Why should services offer bulk endpoints?](#258-why-should-services-offer-bulk-endpoints)
- [259: What is the N+1 problem between services and how do you fix it?](#259-what-is-the-n1-problem-between-services-and-how-do-you-fix-it)
- [260: How do you debug a slow request that goes through several services?](#260-how-do-you-debug-a-slow-request-that-goes-through-several-services)
- [261: What are ephemeral (preview) environments?](#261-what-are-ephemeral-preview-environments)
- [262: How do you make Docker Compose wait until a dependency is actually ready?](#262-how-do-you-make-docker-compose-wait-until-a-dependency-is-actually-ready)
- [263: What are Kubernetes NetworkPolicies and why use them?](#263-what-are-kubernetes-networkpolicies-and-why-use-them)
- [264: Which HTTP security headers should services and gateways set?](#264-which-http-security-headers-should-services-and-gateways-set)
- [265: How do you manage dependency vulnerabilities across many Node.js services?](#265-how-do-you-manage-dependency-vulnerabilities-across-many-nodejs-services)
- [266: How do you rotate a secret without downtime?](#266-how-do-you-rotate-a-secret-without-downtime)
- [267: What should you not put in logs?](#267-what-should-you-not-put-in-logs)
- [268: What is audit logging and how is it different from application logging?](#268-what-is-audit-logging-and-how-is-it-different-from-application-logging)
- [269: How do you keep message order in RabbitMQ when you have several consumers?](#269-how-do-you-keep-message-order-in-rabbitmq-when-you-have-several-consumers)
- [270: What is a poison message and how do you handle it?](#270-what-is-a-poison-message-and-how-do-you-handle-it)
- [271: How do you do request-reply over RabbitMQ?](#271-how-do-you-do-request-reply-over-rabbitmq)
- [272: How do you apply backpressure in a Kafka consumer?](#272-how-do-you-apply-backpressure-in-a-kafka-consumer)
- [273: How do you process Kafka messages in batches?](#273-how-do-you-process-kafka-messages-in-batches)
- [274: What do acks and idempotence mean for a Kafka producer?](#274-what-do-acks-and-idempotence-mean-for-a-kafka-producer)
- [275: What is the difference between retention and log compaction in Kafka?](#275-what-is-the-difference-between-retention-and-log-compaction-in-kafka)
- [276: How do you choose between RabbitMQ and Kafka?](#276-how-do-you-choose-between-rabbitmq-and-kafka)
- [277: What is NATS and when would you use it?](#277-what-is-nats-and-when-would-you-use-it)
- [278: How do you fan out events with Amazon SNS and SQS?](#278-how-do-you-fan-out-events-with-amazon-sns-and-sqs)
- [279: How do Node.js Lambda functions fit into a microservices system?](#279-how-do-nodejs-lambda-functions-fit-into-a-microservices-system)
- [280: What is a cold start and how do you reduce it?](#280-what-is-a-cold-start-and-how-do-you-reduce-it)
- [281: How do you monitor memory usage in a Node.js service?](#281-how-do-you-monitor-memory-usage-in-a-nodejs-service)
- [282: How do you take a heap snapshot from a service running in production?](#282-how-do-you-take-a-heap-snapshot-from-a-service-running-in-production)
- [283: How do you attach a debugger to a Node.js service in Kubernetes?](#283-how-do-you-attach-a-debugger-to-a-nodejs-service-in-kubernetes)
- [284: How do you choose between Express and Fastify for a new service?](#284-how-do-you-choose-between-express-and-fastify-for-a-new-service)
- [285: What is Hono and why do some teams use it for services?](#285-what-is-hono-and-why-do-some-teams-use-it-for-services)
- [286: Can Node.js services talk to each other over HTTP/2?](#286-can-nodejs-services-talk-to-each-other-over-http2)
- [287: What is a service catalog and why does it help with many microservices?](#287-what-is-a-service-catalog-and-why-does-it-help-with-many-microservices)
- [288: What is a service template (golden path)?](#288-what-is-a-service-template-golden-path)
- [289: How do you implement the strangler fig pattern with a Node.js proxy?](#289-how-do-you-implement-the-strangler-fig-pattern-with-a-nodejs-proxy)
- [290: What is the dual write problem?](#290-what-is-the-dual-write-problem)
- [291: How do you move data out of a monolith into a new service?](#291-how-do-you-move-data-out-of-a-monolith-into-a-new-service)
- [292: What logic belongs in an API gateway and what belongs in a BFF?](#292-what-logic-belongs-in-an-api-gateway-and-what-belongs-in-a-bff)
- [293: How should timeouts be set along a chain of services?](#293-how-should-timeouts-be-set-along-a-chain-of-services)
- [294: How do you size a database connection pool in a microservice?](#294-how-do-you-size-a-database-connection-pool-in-a-microservice)
- [295: What is PgBouncer and when do microservices need it?](#295-what-is-pgbouncer-and-when-do-microservices-need-it)
- [296: What should you know about using read replicas in a service?](#296-what-should-you-know-about-using-read-replicas-in-a-service)
- [297: How do you organize versioned routes in an Express service?](#297-how-do-you-organize-versioned-routes-in-an-express-service)
- [298: How do you design an API for a long-running operation?](#298-how-do-you-design-an-api-for-a-long-running-operation)
- [299: How do you roll back a bad deployment in Kubernetes?](#299-how-do-you-roll-back-a-bad-deployment-in-kubernetes)
- [300: How do you test how your services behave when a dependency is slow or failing?](#300-how-do-you-test-how-your-services-behave-when-a-dependency-is-slow-or-failing)

### Advanced Questions (301-450)

- [301: Why does latency in a Node.js service grow so fast when it gets close to full load?](#301-why-does-latency-in-a-nodejs-service-grow-so-fast-when-it-gets-close-to-full-load)
- [302: What is load shedding and how do you do it in Node.js?](#302-what-is-load-shedding-and-how-do-you-do-it-in-nodejs)
- [303: What are adaptive concurrency limits?](#303-what-are-adaptive-concurrency-limits)
- [304: What are hedged requests?](#304-what-are-hedged-requests)
- [305: How does fan-out make tail latency worse?](#305-how-does-fan-out-make-tail-latency-worse)
- [306: What is a retry storm and how do you stop one?](#306-what-is-a-retry-storm-and-how-do-you-stop-one)
- [307: What is a metastable failure?](#307-what-is-a-metastable-failure)
- [308: How does exactly-once processing work in Kafka, and what are its limits?](#308-how-does-exactly-once-processing-work-in-kafka-and-what-are-its-limits)
- [309: How can retries break message ordering, and how do you prevent it?](#309-how-can-retries-break-message-ordering-and-how-do-you-prevent-it)
- [310: How do you handle events that arrive out of order?](#310-how-do-you-handle-events-that-arrive-out-of-order)
- [311: How do you implement an event store with optimistic concurrency?](#311-how-do-you-implement-an-event-store-with-optimistic-concurrency)
- [312: What are snapshots in event sourcing and when do you need them?](#312-what-are-snapshots-in-event-sourcing-and-when-do-you-need-them)
- [313: How do you rebuild a projection in an event-sourced or event-driven system?](#313-how-do-you-rebuild-a-projection-in-an-event-sourced-or-event-driven-system)
- [314: What is event upcasting?](#314-what-is-event-upcasting)
- [315: How do you deal with eventual consistency in the user interface?](#315-how-do-you-deal-with-eventual-consistency-in-the-user-interface)
- [316: What isolation problems do sagas have and how do you handle them?](#316-what-isolation-problems-do-sagas-have-and-how-do-you-handle-them)
- [317: What do you do if a compensating action fails?](#317-what-do-you-do-if-a-compensating-action-fails)
- [318: What is Temporal and why must workflow code be deterministic?](#318-what-is-temporal-and-why-must-workflow-code-be-deterministic)
- [319: Why are two-phase commit and distributed transactions usually avoided in microservices?](#319-why-are-two-phase-commit-and-distributed-transactions-usually-avoided-in-microservices)
- [320: Why are distributed locks hard to get right?](#320-why-are-distributed-locks-hard-to-get-right)
- [321: Why can't you trust wall clock time to order events across services?](#321-why-cant-you-trust-wall-clock-time-to-order-events-across-services)
- [322: What are Lamport clocks and hybrid logical clocks?](#322-what-are-lamport-clocks-and-hybrid-logical-clocks)
- [323: What is consistent hashing and where is it used?](#323-what-is-consistent-hashing-and-where-is-it-used)
- [324: How would you shard the data of a single microservice?](#324-how-would-you-shard-the-data-of-a-single-microservice)
- [325: How do you design microservices to run active-active in several regions?](#325-how-do-you-design-microservices-to-run-active-active-in-several-regions)
- [326: How do you resolve conflicting writes in a multi-region system?](#326-how-do-you-resolve-conflicting-writes-in-a-multi-region-system)
- [327: What is cell-based architecture?](#327-what-is-cell-based-architecture)
- [328: How do you reduce the blast radius of failures and bad deployments?](#328-how-do-you-reduce-the-blast-radius-of-failures-and-bad-deployments)
- [329: What are the trade-offs of using a service mesh?](#329-what-are-the-trade-offs-of-using-a-service-mesh)
- [330: Should resilience logic live in a library or in the infrastructure?](#330-should-resilience-logic-live-in-a-library-or-in-the-infrastructure)
- [331: What does zero trust mean for microservices?](#331-what-does-zero-trust-mean-for-microservices)
- [332: What is SPIFFE?](#332-what-is-spiffe)
- [333: What is SSRF and why is it a risk in microservices?](#333-what-is-ssrf-and-why-is-it-a-risk-in-microservices)
- [334: What are common JWT mistakes in microservices?](#334-what-are-common-jwt-mistakes-in-microservices)
- [335: How do you revoke JWTs before they expire?](#335-how-do-you-revoke-jwts-before-they-expire)
- [336: What is the confused deputy problem in microservices?](#336-what-is-the-confused-deputy-problem-in-microservices)
- [337: How do you secure a message broker shared by many services?](#337-how-do-you-secure-a-message-broker-shared-by-many-services)
- [338: How do you protect Node.js services from supply chain attacks?](#338-how-do-you-protect-nodejs-services-from-supply-chain-attacks)
- [339: What is the Node.js permission model and is it useful for services?](#339-what-is-the-nodejs-permission-model-and-is-it-useful-for-services)
- [340: What are the risks of passing secrets as environment variables?](#340-what-are-the-risks-of-passing-secrets-as-environment-variables)
- [341: How do you prevent one tenant from slowing down everyone else (noisy neighbor)?](#341-how-do-you-prevent-one-tenant-from-slowing-down-everyone-else-noisy-neighbor)
- [342: What are the common multi-tenancy models for microservices?](#342-what-are-the-common-multi-tenancy-models-for-microservices)
- [343: How do you keep the API gateway from becoming a single point of failure?](#343-how-do-you-keep-the-api-gateway-from-becoming-a-single-point-of-failure)
- [344: How do you make a consumer idempotent when the side effect is an external API call?](#344-how-do-you-make-a-consumer-idempotent-when-the-side-effect-is-an-external-api-call)
- [345: How do you scale an outbox relay without breaking event order?](#345-how-do-you-scale-an-outbox-relay-without-breaking-event-order)
- [346: How does the Debezium outbox event router work?](#346-how-does-the-debezium-outbox-event-router-work)
- [347: How do you choose the number of partitions for a Kafka topic?](#347-how-do-you-choose-the-number-of-partitions-for-a-kafka-topic)
- [348: How do you process messages in parallel beyond the number of partitions?](#348-how-do-you-process-messages-in-parallel-beyond-the-number-of-partitions)
- [349: How do you retry failed Kafka messages without blocking the partition?](#349-how-do-you-retry-failed-kafka-messages-without-blocking-the-partition)
- [350: How do you replay messages from a dead letter queue safely?](#350-how-do-you-replay-messages-from-a-dead-letter-queue-safely)
- [351: What are backward, forward and full compatibility for schemas?](#351-what-are-backward-forward-and-full-compatibility-for-schemas)
- [352: What rules do you follow to evolve protobuf messages safely?](#352-what-rules-do-you-follow-to-evolve-protobuf-messages-safely)
- [353: How do you catch breaking contract changes at scale?](#353-how-do-you-catch-breaking-contract-changes-at-scale)
- [354: How do you deprecate and remove an API that many services use?](#354-how-do-you-deprecate-and-remove-an-api-that-many-services-use)
- [355: How do you profile CPU usage of a Node.js service in production?](#355-how-do-you-profile-cpu-usage-of-a-nodejs-service-in-production)
- [356: How can V8 garbage collection affect a service, and how do you tune it?](#356-how-can-v8-garbage-collection-affect-a-service-and-how-do-you-tune-it)
- [357: What are common causes of memory leaks in Node.js microservices?](#357-what-are-common-causes-of-memory-leaks-in-nodejs-microservices)
- [358: How do you find out if GC pauses are causing latency spikes?](#358-how-do-you-find-out-if-gc-pauses-are-causing-latency-spikes)
- [359: How expensive is JSON serialization in a Node.js service and how do you reduce it?](#359-how-expensive-is-json-serialization-in-a-nodejs-service-and-how-do-you-reduce-it)
- [360: What are the signs of an exhausted HTTP connection pool, and how do you fix it?](#360-what-are-the-signs-of-an-exhausted-http-connection-pool-and-how-do-you-fix-it)
- [361: How can DNS lookups become a bottleneck in Node.js?](#361-how-can-dns-lookups-become-a-bottleneck-in-nodejs)
- [362: What is the libuv thread pool and how can it limit a service?](#362-what-is-the-libuv-thread-pool-and-how-can-it-limit-a-service)
- [363: Why do you get intermittent ECONNRESET errors between services, and how do you fix them?](#363-why-do-you-get-intermittent-econnreset-errors-between-services-and-how-do-you-fix-them)
- [364: Which server timeouts in Node.js should you configure?](#364-which-server-timeouts-in-nodejs-should-you-configure)
- [365: How do you protect a Node.js service from slow client attacks?](#365-how-do-you-protect-a-nodejs-service-from-slow-client-attacks)
- [366: Cluster module, worker threads or more pods: how do you choose?](#366-cluster-module-worker-threads-or-more-pods-how-do-you-choose)
- [367: How does CPU throttling in containers affect Node.js?](#367-how-does-cpu-throttling-in-containers-affect-nodejs)
- [368: What are common autoscaling pitfalls for Node.js services?](#368-what-are-common-autoscaling-pitfalls-for-nodejs-services)
- [369: Why can a fresh deployment be slow at first, and how do you warm up a service?](#369-why-can-a-fresh-deployment-be-slow-at-first-and-how-do-you-warm-up-a-service)
- [370: How do you avoid connection storms when many instances start at once?](#370-how-do-you-avoid-connection-storms-when-many-instances-start-at-once)
- [371: How do you shut down a Kafka consumer without losing or duplicating too much work?](#371-how-do-you-shut-down-a-kafka-consumer-without-losing-or-duplicating-too-much-work)
- [372: How do you deploy a WebSocket service without dropping every connection?](#372-how-do-you-deploy-a-websocket-service-without-dropping-every-connection)
- [373: How do you scale WebSocket servers across many instances?](#373-how-do-you-scale-websocket-servers-across-many-instances)
- [374: How do you keep observability costs under control with many services?](#374-how-do-you-keep-observability-costs-under-control-with-many-services)
- [375: What are exemplars and how do they help?](#375-what-are-exemplars-and-how-do-they-help)
- [376: How does tracing work across a message broker?](#376-how-does-tracing-work-across-a-message-broker)
- [377: Why does trace context sometimes get lost in Node.js, and how do you fix it?](#377-why-does-trace-context-sometimes-get-lost-in-nodejs-and-how-do-you-fix-it)
- [378: How do you connect logs with traces?](#378-how-do-you-connect-logs-with-traces)
- [379: What are burn-rate alerts for SLOs?](#379-what-are-burn-rate-alerts-for-slos)
- [380: What is synthetic monitoring and why add it?](#380-what-is-synthetic-monitoring-and-why-add-it)
- [381: How would you handle an incident where failures are cascading across services?](#381-how-would-you-handle-an-incident-where-failures-are-cascading-across-services)
- [382: How do you find the critical path and weak spots in a microservices system?](#382-how-do-you-find-the-critical-path-and-weak-spots-in-a-microservices-system)
- [383: Why are circular dependencies between services a problem?](#383-why-are-circular-dependencies-between-services-a-problem)
- [384: When should you merge microservices back together?](#384-when-should-you-merge-microservices-back-together)
- [385: How do you find service boundaries in a new or existing domain?](#385-how-do-you-find-service-boundaries-in-a-new-or-existing-domain)
- [386: What is event storming?](#386-what-is-event-storming)
- [387: What is an anti-corruption layer?](#387-what-is-an-anti-corruption-layer)
- [388: What are "published language" and "shared kernel" in DDD, and how do they apply to services?](#388-what-are-published-language-and-shared-kernel-in-ddd-and-how-do-they-apply-to-services)
- [389: Should internal and external APIs be versioned the same way?](#389-should-internal-and-external-apis-be-versioned-the-same-way)
- [390: What dependency policies help in a large Node.js microservices monorepo?](#390-what-dependency-policies-help-in-a-large-nodejs-microservices-monorepo)
- [391: What is platform engineering and how does it relate to microservices?](#391-what-is-platform-engineering-and-how-does-it-relate-to-microservices)
- [392: What is traffic shadowing (mirroring) and when do you use it?](#392-what-is-traffic-shadowing-mirroring-and-when-do-you-use-it)
- [393: How does automated canary analysis work?](#393-how-does-automated-canary-analysis-work)
- [394: How do you run schema migrations on very large tables without downtime?](#394-how-do-you-run-schema-migrations-on-very-large-tables-without-downtime)
- [395: How do you backfill data across services at scale?](#395-how-do-you-backfill-data-across-services-at-scale)
- [396: What are reconciliation jobs and why do distributed systems need them?](#396-what-are-reconciliation-jobs-and-why-do-distributed-systems-need-them)
- [397: How should a microservice handle money?](#397-how-should-a-microservice-handle-money)
- [398: A call to the payment provider timed out. Did the payment happen? How do you handle it?](#398-a-call-to-the-payment-provider-timed-out-did-the-payment-happen-how-do-you-handle-it)
- [399: How do you prevent overselling inventory across services?](#399-how-do-you-prevent-overselling-inventory-across-services)
- [400: How would you design for a flash sale with a huge traffic spike?](#400-how-would-you-design-for-a-flash-sale-with-a-huge-traffic-spike)
- [401: How do you respect a third-party API rate limit shared by many instances of your service?](#401-how-do-you-respect-a-third-party-api-rate-limit-shared-by-many-instances-of-your-service)
- [402: What is queue-based load leveling?](#402-what-is-queue-based-load-leveling)
- [403: How do you handle priorities in queues without starving low-priority work?](#403-how-do-you-handle-priorities-in-queues-without-starving-low-priority-work)
- [404: How do you choose between batch processing and stream processing?](#404-how-do-you-choose-between-batch-processing-and-stream-processing)
- [405: What problems come with caching at several layers?](#405-what-problems-come-with-caching-at-several-layers)
- [406: What is cache penetration and how do you prevent it?](#406-what-is-cache-penetration-and-how-do-you-prevent-it)
- [407: How do you deal with hot keys in Redis?](#407-how-do-you-deal-with-hot-keys-in-redis)
- [408: What happens to your services if Redis goes down, and how should they behave?](#408-what-happens-to-your-services-if-redis-goes-down-and-how-should-they-behave)
- [409: What happens to producers and consumers when a Kafka broker fails?](#409-what-happens-to-producers-and-consumers-when-a-kafka-broker-fails)
- [410: What are RabbitMQ memory and disk alarms, and how do they affect publishers?](#410-what-are-rabbitmq-memory-and-disk-alarms-and-how-do-they-affect-publishers)
- [411: How do you change configuration at runtime without restarting services?](#411-how-do-you-change-configuration-at-runtime-without-restarting-services)
- [412: What is a kill switch and how do you design one?](#412-what-is-a-kill-switch-and-how-do-you-design-one)
- [413: What is the difference between north-south and east-west traffic, and what handles each?](#413-what-is-the-difference-between-north-south-and-east-west-traffic-and-what-handles-each)
- [414: When are serverless functions cheaper than containers, and when are they more expensive?](#414-when-are-serverless-functions-cheaper-than-containers-and-when-are-they-more-expensive)
- [415: How do Node.js services work with services written in other languages?](#415-how-do-nodejs-services-work-with-services-written-in-other-languages)
- [416: What performance issues can GraphQL Federation have?](#416-what-performance-issues-can-graphql-federation-have)
- [417: How do you tune gRPC performance in Node.js?](#417-how-do-you-tune-grpc-performance-in-nodejs)
- [418: How does backpressure work end to end in a streaming pipeline?](#418-how-does-backpressure-work-end-to-end-in-a-streaming-pipeline)
- [419: How would you send a notification to millions of users at once?](#419-how-would-you-send-a-notification-to-millions-of-users-at-once)
- [420: How do you schedule millions of future tasks (for example "remind the user in 3 days")?](#420-how-do-you-schedule-millions-of-future-tasks-for-example-remind-the-user-in-3-days)
- [421: When should you use a workflow engine instead of writing sagas by hand?](#421-when-should-you-use-a-workflow-engine-instead-of-writing-sagas-by-hand)
- [422: A downstream service your service depends on is down for 30 minutes. What should happen?](#422-a-downstream-service-your-service-depends-on-is-down-for-30-minutes-what-should-happen)
- [423: You find that some messages are being processed twice. How do you investigate and fix it?](#423-you-find-that-some-messages-are-being-processed-twice-how-do-you-investigate-and-fix-it)
- [424: Your Node.js pods keep getting OOMKilled. How do you debug it?](#424-your-nodejs-pods-keep-getting-oomkilled-how-do-you-debug-it)
- [425: p99 latency went up a lot after a deploy, but there are no errors. What do you check?](#425-p99-latency-went-up-a-lot-after-a-deploy-but-there-are-no-errors-what-do-you-check)
- [426: Consumer lag on a Kafka topic keeps growing. What do you do?](#426-consumer-lag-on-a-kafka-topic-keeps-growing-what-do-you-do)
- [427: Users see 502 errors from the gateway every time a service is deployed. Why, and how do you fix it?](#427-users-see-502-errors-from-the-gateway-every-time-a-service-is-deployed-why-and-how-do-you-fix-it)
- [428: A service's database has become the bottleneck. What are your options?](#428-a-services-database-has-become-the-bottleneck-what-are-your-options)
- [429: You are splitting a monolith. How do you choose the first service to extract?](#429-you-are-splitting-a-monolith-how-do-you-choose-the-first-service-to-extract)
- [430: Walk through how you would design a checkout flow across microservices.](#430-walk-through-how-you-would-design-a-checkout-flow-across-microservices)
- [431: Two teams both want to own the "customer" data. How do you resolve it?](#431-two-teams-both-want-to-own-the-customer-data-how-do-you-resolve-it)
- [432: A change requires releasing three services at the same time. How do you avoid that?](#432-a-change-requires-releasing-three-services-at-the-same-time-how-do-you-avoid-that)
- [433: A bad event schema was shipped and consumers are failing. What do you do?](#433-a-bad-event-schema-was-shipped-and-consumers-are-failing-what-do-you-do)
- [434: You find that access tokens have been written to logs for months. What do you do?](#434-you-find-that-access-tokens-have-been-written-to-logs-for-months-what-do-you-do)
- [435: Your microservices cloud bill is too high. Where do you look first?](#435-your-microservices-cloud-bill-is-too-high-where-do-you-look-first)
- [436: How would you change a chain of synchronous calls into an event-driven flow?](#436-how-would-you-change-a-chain-of-synchronous-calls-into-an-event-driven-flow)
- [437: How would you add distributed tracing to 40 existing Node.js services?](#437-how-would-you-add-distributed-tracing-to-40-existing-nodejs-services)
- [438: What happens in your system if a whole cloud region goes down?](#438-what-happens-in-your-system-if-a-whole-cloud-region-goes-down)
- [439: Redis is down and your service is returning errors on every request. How should it have been designed?](#439-redis-is-down-and-your-service-is-returning-errors-on-every-request-how-should-it-have-been-designed)
- [440: A nightly job runs twice on some nights. Why might that happen?](#440-a-nightly-job-runs-twice-on-some-nights-why-might-that-happen)
- [441: A user updates their profile but still sees old data on another page. How do you find the cause?](#441-a-user-updates-their-profile-but-still-sees-old-data-on-another-page-how-do-you-find-the-cause)
- [442: Latency through your Node.js API gateway keeps creeping up as traffic grows. What do you check?](#442-latency-through-your-nodejs-api-gateway-keeps-creeping-up-as-traffic-grows-what-do-you-check)
- [443: A Kafka consumer group keeps rebalancing and makes little progress. What is going on?](#443-a-kafka-consumer-group-keeps-rebalancing-and-makes-little-progress-what-is-going-on)
- [444: Product wants a report that joins data from four services. How do you build it?](#444-product-wants-a-report-that-joins-data-from-four-services-how-do-you-build-it)
- [445: What would you put in a production readiness checklist for a new microservice?](#445-what-would-you-put-in-a-production-readiness-checklist-for-a-new-microservice)
- [446: A downstream team says they never received some events you published. How do you debug it?](#446-a-downstream-team-says-they-never-received-some-events-you-published-how-do-you-debug-it)
- [447: A bug in one service suddenly sends 10 times more traffic to your service. How do you protect it?](#447-a-bug-in-one-service-suddenly-sends-10-times-more-traffic-to-your-service-how-do-you-protect-it)
- [448: How do you measure whether a microservices architecture is working well?](#448-how-do-you-measure-whether-a-microservices-architecture-is-working-well)
- [449: What questions would you ask before agreeing to move a system to microservices?](#449-what-questions-would-you-ask-before-agreeing-to-move-a-system-to-microservices)
- [450: What recent changes in Node.js and its ecosystem matter for building microservices?](#450-what-recent-changes-in-nodejs-and-its-ecosystem-matter-for-building-microservices)

---

# Easy Questions (1-150)

## 1: What is a microservice?

A microservice is a small application that does one job inside a larger system and runs as its own process. It has its own code, its own deployment and usually its own database. It talks to other services over the network, using HTTP, gRPC or a message broker.

For example, an online shop could have separate services for users, products, orders, payments and notifications. Each one can be changed, deployed and scaled without touching the others.

## 2: What is a monolith?

A monolith is an application where all features live in one codebase and are deployed together as one unit. The user module, the order module and the payment module all run in the same process and usually share one database.

A monolith is not bad by itself. It is simpler to build, test, deploy and debug. Problems usually show up when the codebase and the team get large: builds get slow, one bug can take down everything and teams step on each other during releases.

## 3: What is the difference between a monolith and microservices?

|               | Monolith                      | Microservices                                       |
| ------------- | ----------------------------- | --------------------------------------------------- |
| Deployment    | One unit                      | Many units, each deployed on its own                |
| Database      | Usually one shared database   | Usually one database per service                    |
| Communication | Function calls in memory      | Network calls (HTTP, gRPC, messages)                |
| Scaling       | Scale the whole app           | Scale only the services that need it                |
| Failure       | One crash can stop everything | A failure can be limited to one service             |
| Complexity    | Lower at the start            | Higher, because of the network and distributed data |

The main trade-off: microservices give teams more independence, but you pay for it with network problems, harder debugging and data consistency issues.

## 4: What are the main benefits of microservices?

- **Independent deployments:** a team can release its service without waiting for other teams.
- **Independent scaling:** a busy service can run on 20 instances while a quiet one runs on 2.
- **Fault isolation:** if the recommendation service crashes, users can still check out.
- **Smaller codebases:** each service is easier to understand on its own.
- **Technology choice:** one service can use PostgreSQL and another MongoDB, or even a different language.
- **Team ownership:** a team owns a service from code to production.

## 5: What are the main drawbacks of microservices?

- Network calls can fail, be slow or time out, which never happens with a function call.
- Data is spread across databases, so you lose simple transactions and joins.
- Debugging a request that passes through five services is much harder.
- You need more infrastructure: containers, orchestration, service discovery, monitoring, tracing, CI/CD for each service.
- Local development is harder because you need several services running.
- Bad service boundaries can create a "distributed monolith", which has the problems of both styles.

## 6: Why is Node.js a good fit for microservices?

Node.js handles I/O with a non-blocking event loop, so one process can handle many concurrent requests while it waits on databases, other services or queues. Most microservices spend their time doing exactly that kind of I/O work.

Other reasons:

- Fast startup and low memory use, which works well with containers and autoscaling.
- A large npm ecosystem with clients for every broker, database and cloud service.
- The same language (JavaScript or TypeScript) on the front end and back end.
- Good built-in support for HTTP, streams and JSON.

It is a weaker fit for CPU-heavy work like video encoding or large calculations, unless you move that work to worker threads or a separate service.

## 7: When should you not use microservices?

- When the product is new and you do not yet know where the boundaries are.
- When the team is small. Five developers managing fifteen services spend more time on infrastructure than on features.
- When you do not have automated deployments, monitoring and logging in place.
- When the domain needs strong consistency across most operations, like a simple accounting app.

A common advice is to start with a well structured monolith (a "modular monolith") and split out services later, when there is a clear reason.

## 8: What is a modular monolith?

A modular monolith is a single deployable application that is split internally into clear modules with strict boundaries. Each module has its own folder, its own public interface and ideally its own database tables or schema. Other modules can only use that public interface, not reach into the internals.

It gives you a lot of the code organization benefits of microservices without the network and operations costs. If a module later needs to scale or be released on its own, it is much easier to pull out into a separate service.

## 9: What is a distributed monolith?

A distributed monolith is a system that is split into services but still behaves like a monolith. The services cannot be deployed alone, they share a database, or one change requires updating many services at the same time.

Signs you have one:

- You must deploy services in a specific order.
- A change in one service's API breaks several others.
- Services make long chains of synchronous calls to each other for every request.
- Several services read and write the same tables.

It is often worse than a real monolith, because you have network problems on top of tight coupling.

## 10: What is a service boundary?

A service boundary is the line that defines what a service is responsible for and what it owns: its data, its business rules and its API. Everything inside the boundary can change freely. Everything that crosses it is a contract with other services.

Good boundaries follow business capabilities (orders, billing, shipping) instead of technical layers (a "database service" or a "validation service"). If two pieces of code always change together, they probably belong in the same service.

## 11: What is a bounded context?

A bounded context is a term from Domain-Driven Design. It is a part of the domain where a word or model has one clear meaning. For example, "customer" in the sales context has a name, contact details and a sales history. In the shipping context, a customer is mostly an address and delivery preferences.

Bounded contexts are a common way to find service boundaries. One bounded context often maps to one microservice, or to a small group of services owned by one team.

## 12: What is Domain-Driven Design and how does it relate to microservices?

Domain-Driven Design (DDD) is an approach to software design that puts the business domain at the center. You work with domain experts, build a shared language and model the code around real business concepts.

Ideas from DDD that are used a lot with microservices:

- **Bounded contexts** to decide service boundaries.
- **Aggregates** to decide what must be consistent inside one transaction.
- **Domain events** like `OrderPlaced` or `PaymentFailed` to communicate between services.
- **Ubiquitous language** so that code, APIs and conversations use the same terms.

## 13: What does "single responsibility" mean for a microservice?

It means a service should focus on one business capability and have one main reason to change. The payment service handles payments. It should not also send marketing emails or generate PDF invoices just because it was convenient.

This does not mean a service should be tiny. "Micro" is about a focused responsibility, not about the number of lines of code.

## 14: How big should a microservice be?

There is no fixed size. Some useful rules of thumb:

- One team should be able to own and understand it fully.
- It should cover one business capability.
- It should be possible to rewrite it in a few weeks if needed.
- It should not need to call other services for most of its work.

If services are too small, you end up with lots of network calls and coordination. If they are too big, you lose independent deployments. Start bigger and split when you see a real reason.

## 15: What does "loose coupling" mean in microservices?

Loose coupling means a service can change without forcing other services to change. Services depend only on each other's public contracts (APIs or event formats), not on internal code, internal data or databases.

Ways to keep coupling low:

- No shared databases.
- Backward compatible API changes.
- Asynchronous events instead of direct calls where possible.
- No shared libraries that contain business logic.

## 16: What does "high cohesion" mean in microservices?

High cohesion means that the code inside a service belongs together. The functions and data in the service serve the same business purpose and usually change together.

If you often need to change two services for every feature, they probably have low cohesion and should be merged or have their boundary moved.

## 17: What is synchronous communication between services?

In synchronous communication, the caller sends a request and waits for the response before it can continue. HTTP REST calls and gRPC unary calls are typical examples.

It is simple to understand and gives you an immediate answer. The downside is that the caller depends on the other service being up and fast at that exact moment. If the called service is slow, the caller is slow too.

## 18: What is asynchronous communication between services?

In asynchronous communication, the sender puts a message on a queue or topic and moves on. It does not wait for the receiver to process it. RabbitMQ, Kafka, Redis Streams, Amazon SQS and NATS are common tools.

Benefits: the services do not need to be online at the same time, spikes are absorbed by the queue and the sender is not slowed down by the receiver. Downsides: you do not get an immediate result, debugging is harder and you need to handle duplicate and out-of-order messages.

## 19: When would you choose synchronous over asynchronous communication?

Use synchronous calls when the caller needs the answer right away to continue, for example checking a user's permissions or getting a price to show on a page.

Use asynchronous messages when:

- The caller does not need the result immediately (sending an email after signup).
- Several services need to react to the same thing (an order was placed).
- You want to absorb traffic spikes.
- The work takes a long time (generating a report).

Most real systems use both.

## 20: What is REST?

REST is an architectural style for APIs that uses HTTP. Resources are identified by URLs, and you use HTTP methods to work with them: `GET` to read, `POST` to create, `PUT` or `PATCH` to update and `DELETE` to remove. Responses use standard status codes, and each request carries everything the server needs, so the server does not keep session state between requests.

```http
GET /orders/123
POST /orders
PATCH /orders/123
DELETE /orders/123
```

## 21: What is gRPC?

gRPC is an RPC framework from Google that runs on HTTP/2 and uses Protocol Buffers to define services and messages. You write a `.proto` file, and client and server code are generated or loaded from it.

It is popular for service-to-service communication because messages are small and binary, the contract is strict and typed, and it supports streaming in both directions. In Node.js the official package is `@grpc/grpc-js`.

## 22: What are Protocol Buffers?

Protocol Buffers (protobuf) is a language-neutral format for defining and serializing structured data. You describe your messages in a `.proto` file, and they are encoded into a compact binary format.

```proto
syntax = "proto3";

message User {
  string id = 1;
  string email = 2;
  int32 age = 3;
}
```

The numbers are field tags. They are used in the binary encoding instead of field names, which is why you must never reuse or change a tag once it is in use.

## 23: What is a message broker?

A message broker is a server that receives messages from producers and delivers them to consumers. It sits between services so they do not need to know about each other directly.

Popular brokers:

- **RabbitMQ:** classic queues, flexible routing with exchanges.
- **Apache Kafka:** a distributed log, great for high throughput event streams and replay.
- **NATS:** lightweight and fast, with JetStream for persistence.
- **Redis Streams:** simple streams if you already run Redis.
- **Cloud options:** Amazon SQS and SNS, Google Pub/Sub, Azure Service Bus.

## 24: What is the difference between a queue and a topic?

A **queue** delivers each message to one consumer. If you run three instances of a worker, each message is handled by only one of them. This is used for distributing work.

A **topic** (publish/subscribe) delivers each message to every subscriber. If the order service publishes `OrderPlaced`, the email service, the inventory service and the analytics service can all get a copy.

In Kafka you get both behaviours with consumer groups: each group gets every message, and inside a group each partition is read by one consumer.

## 25: What is event-driven architecture?

In event-driven architecture, services communicate by publishing events about things that already happened, like `UserRegistered` or `OrderShipped`. Other services subscribe to the events they care about and react.

The publisher does not know or care who is listening. This makes it easy to add new features: to send a welcome email, you add a service that listens to `UserRegistered` without changing the user service.

## 26: What is the difference between an event and a command?

A **command** asks a service to do something: `ChargeCard`, `SendEmail`. It has one intended receiver, and it can be rejected.

An **event** says that something has happened: `CardCharged`, `EmailSent`. It is a fact in the past tense, it can have many receivers or none, and it cannot be rejected, only reacted to.

Naming makes this clear. Commands use the imperative ("CreateOrder"), events use the past tense ("OrderCreated").

## 27: What is an API gateway?

An API gateway is a single entry point that sits in front of your services. Clients call the gateway, and it forwards each request to the right service.

It usually also handles:

- Authentication and token validation
- Rate limiting
- TLS termination
- Request routing and path rewriting
- Response caching
- Logging and metrics

Examples: Kong, NGINX, Envoy, Traefik, AWS API Gateway, or a custom gateway written in Node.js.

## 28: Why use an API gateway instead of letting clients call services directly?

- Clients only need to know one URL, not the address of every service.
- Internal services can change, split or move without breaking clients.
- Cross-cutting things like auth, rate limiting and CORS are handled in one place.
- Internal services do not need to be exposed to the public internet.
- The gateway can combine several service calls into one response for the client.

The risk is that the gateway becomes a bottleneck or a place where business logic piles up. Keep it thin.

## 29: What is service discovery?

Service discovery is how a service finds the network address of another service. In a dynamic environment, instances start and stop all the time and their IP addresses change, so you cannot hard-code them.

Common approaches:

- **DNS based:** in Kubernetes, you call `http://orders-service` and the cluster DNS resolves it.
- **Service registry:** services register themselves in Consul, etcd or Eureka, and callers look them up.
- **Platform managed:** cloud load balancers or a service mesh handle it for you.

## 30: What is the difference between client-side and server-side discovery?

In **client-side discovery**, the calling service asks a registry for the list of instances and picks one itself, doing its own load balancing.

In **server-side discovery**, the caller sends the request to a load balancer or router (like a Kubernetes Service or an AWS load balancer), and that component picks an instance.

Server-side discovery is more common today because platforms like Kubernetes provide it out of the box and the client code stays simple.

## 31: What is a load balancer?

A load balancer spreads incoming requests across several instances of a service. If one instance is unhealthy, it stops sending traffic to it.

Common algorithms:

- **Round robin:** each instance in turn.
- **Least connections:** the instance with the fewest active requests.
- **IP hash or consistent hashing:** the same client goes to the same instance.

Layer 4 balancers work with TCP connections, while layer 7 balancers understand HTTP and can route by path or header.

## 32: What is a reverse proxy?

A reverse proxy is a server that receives requests from clients and forwards them to backend servers, then sends the responses back. The client only talks to the proxy.

NGINX, HAProxy, Envoy and Traefik are common reverse proxies. They are used for TLS termination, load balancing, caching, compression and hiding the internal structure of your system. An API gateway is a reverse proxy with extra API-related features.

## 33: What does "stateless service" mean?

A stateless service does not keep any client data in its own memory between requests. Everything it needs is either in the request (like a JWT) or in an external store (a database, Redis).

This matters because any instance can handle any request. You can add or remove instances, restart them or route requests anywhere without losing data. Sessions stored in memory or files saved to the local disk break this.

## 34: What is horizontal scaling vs vertical scaling?

**Vertical scaling** means giving one machine more resources: more CPU, more RAM. It is simple but has a limit, and the machine is still a single point of failure.

**Horizontal scaling** means running more instances of the service behind a load balancer. It has no hard limit and gives you redundancy, but the service has to be stateless.

Microservices are designed mostly for horizontal scaling.

## 35: What is the "database per service" pattern?

Each service owns its data and is the only one allowed to read or write it directly. Other services must go through its API or listen to its events.

This keeps services loosely coupled: one team can change its schema or even switch databases without breaking others. The cost is that you can no longer join data across services in one query or use a single transaction across them.

It does not always mean a separate database server. Separate schemas or separate users with strict permissions on one server can work too, as long as no service touches another service's tables.

## 36: Why is sharing a database between services a problem?

- A schema change by one team can break another team's service.
- You cannot tell which service owns which data or rules.
- One service's heavy queries can slow down all the others.
- You cannot deploy or scale services independently.
- It hides coupling, because services talk through tables instead of clear APIs.

It is one of the most common reasons systems turn into a distributed monolith.

## 37: What is eventual consistency?

Eventual consistency means that after a change, different parts of the system may show different data for a short time, but they will all agree if no new changes happen.

For example, when a user changes their name in the user service, the order service may still show the old name for a second until it processes the `UserUpdated` event. In microservices you often accept this in exchange for availability and loose coupling.

## 38: What is the CAP theorem?

The CAP theorem says that when there is a network partition (P), a distributed system has to choose between consistency (C, every read gets the latest write or an error) and availability (A, every request gets a response, maybe with old data).

Since network partitions will happen in real systems, the practical choice is between CP and AP during a partition. A banking ledger usually picks consistency. A product catalog usually picks availability.

## 39: What is a health check?

A health check is an endpoint or command that tells the platform whether a service instance is working. Load balancers and orchestrators like Kubernetes call it regularly and stop sending traffic to, or restart, instances that fail.

```js
import express from "express";

const app = express();

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000);
```

## 40: What is the difference between liveness and readiness?

- **Liveness** answers "is the process stuck or broken?" If the liveness check fails, Kubernetes restarts the container.
- **Readiness** answers "can this instance take traffic right now?" If it fails, the instance is removed from the load balancer but not restarted.

A service might be alive but not ready while it is starting up, warming a cache or waiting for its database connection. Liveness checks should be simple and should not depend on other services, otherwise one database outage can make Kubernetes restart every pod.

## 41: What is containerization and why is it used with microservices?

Containerization means packaging a service and everything it needs (Node.js runtime, dependencies, config) into a container image. The container runs the same way on a laptop, in CI and in production.

With many services, containers give you one standard way to build, ship and run all of them, no matter what each service uses inside. Docker is the most common tool to build images, and Kubernetes is the most common platform to run them.

## 42: What does a basic Dockerfile for a Node.js service look like?

```dockerfile
FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
ENV NODE_ENV=production
USER node
EXPOSE 3000
CMD ["node", "src/server.js"]
```

Copying `package*.json` first lets Docker cache the `npm ci` layer, so it only reinstalls dependencies when they change. `USER node` runs the process as a non-root user. Using `CMD ["node", ...]` instead of `npm start` lets Node receive signals like `SIGTERM` directly.

## 43: What is Kubernetes and why is it used for microservices?

Kubernetes is a platform for running containers across a cluster of machines. You describe what you want (for example "run 3 copies of the orders service"), and Kubernetes keeps it that way.

It gives microservices a lot out of the box:

- Scheduling containers on machines
- Restarting failed containers
- Service discovery and load balancing through Services and DNS
- Rolling updates and rollbacks
- Autoscaling
- Config and secrets management

## 44: What is a container orchestrator?

A container orchestrator manages containers across many machines. It decides where each container runs, restarts it if it crashes, scales it up or down, connects it to the network and rolls out new versions.

Kubernetes is the most widely used one. Others include Amazon ECS, HashiCorp Nomad and Docker Swarm (much less common now). Managed Kubernetes services like EKS, GKE and AKS are popular because they remove the work of running the control plane.

## 45: What are environment variables used for in microservices?

Environment variables hold configuration that changes between environments: database URLs, ports, API keys, log levels, URLs of other services. The same image can run in dev, staging and production with different variables.

```js
const port = Number(process.env.PORT ?? 3000);
const dbUrl = process.env.DATABASE_URL;

if (!dbUrl) {
  throw new Error("DATABASE_URL is required");
}
```

Fail at startup if a required variable is missing. It is much better than failing on the first request.

## 46: How do you load a .env file in Node.js without extra packages?

Since Node.js 20.6 you can use the `--env-file` flag, and since Node 21.7 you can also call `process.loadEnvFile()`.

```bash
node --env-file=.env src/server.js
```

```js
import process from "node:process";

process.loadEnvFile(); // loads ./.env by default
```

Node 22.9 added `--env-file-if-exists`, which does not fail when the file is missing. In production, variables usually come from the platform (Kubernetes, ECS) instead of a file, so `.env` is mostly for local development. Never commit real secrets in `.env` files.

## 47: What is the Twelve-Factor App?

The Twelve-Factor App is a set of guidelines for building services that run well in the cloud. Some of the most relevant points for microservices:

- One codebase per service, many deploys.
- Explicitly declare dependencies (`package.json` and a lockfile).
- Store config in the environment.
- Treat databases and brokers as attached resources you connect to by URL.
- Run as stateless processes.
- Export services by binding to a port.
- Start fast and shut down gracefully.
- Keep dev, staging and production as similar as possible.
- Write logs to stdout and let the platform collect them.

## 48: Why should logs go to stdout in a containerized service?

In containers, the platform (Docker, Kubernetes, a cloud service) captures whatever the process writes to stdout and stderr. A log agent like Fluent Bit, Vector or the OpenTelemetry Collector then ships the logs to a central system.

If the service writes to local files instead, the logs are lost when the container is replaced, the disk can fill up and you need extra setup to collect them. Writing to stdout keeps the service simple and leaves log routing to the platform.

## 49: What is centralized logging?

Centralized logging means collecting logs from all services and instances into one place where you can search and filter them. Without it, you would have to check each container one by one.

Common tools: the ELK stack (Elasticsearch, Logstash, Kibana), OpenSearch, Grafana Loki, Datadog, Splunk and cloud services like CloudWatch Logs. For this to work well, every service should write structured JSON logs with common fields like `service`, `level`, `traceId` and `requestId`.

## 50: What is structured logging?

Structured logging means writing logs as data, usually JSON, instead of plain text sentences. Each log line has fields you can filter and search on.

```js
import pino from "pino";

const logger = pino({ base: { service: "orders" } });

logger.info({ orderId: "o_123", userId: "u_42" }, "order created");
// {"level":30,"time":...,"service":"orders","orderId":"o_123","userId":"u_42","msg":"order created"}
```

With structured logs you can easily ask questions like "show me all errors for order o_123 across all services". Pino is the most common choice in Node.js because it is fast and outputs JSON by default.

## 51: What is a correlation ID?

A correlation ID (also called a request ID) is a unique value attached to a request when it enters the system. Every service that handles the request passes it along in a header and includes it in its logs.

When something goes wrong, you search your logs for that one ID and see the full path of the request across all services. It is usually sent in a header like `x-request-id`. If you use OpenTelemetry, the trace ID in the `traceparent` header does the same job.

## 52: What is distributed tracing?

Distributed tracing records the path of a single request as it moves through many services. Each step (an HTTP call, a database query, a message being processed) is a **span**, and all spans of one request share a **trace ID**.

A tracing UI like Jaeger, Grafana Tempo, Zipkin or a vendor tool then shows the request as a timeline, so you can see which service was slow or where an error started. OpenTelemetry is the standard way to add tracing to Node.js services today.

## 53: What is OpenTelemetry?

OpenTelemetry (OTel) is an open standard and set of SDKs for collecting traces, metrics and logs. It is vendor neutral: you instrument your code once and can send the data to Jaeger, Prometheus, Grafana, Datadog, Honeycomb or any other backend that supports the OTLP protocol.

For Node.js it has auto-instrumentation packages that create spans for HTTP, Express, Fastify, gRPC, PostgreSQL, Redis, Kafka and many other libraries without changing your code.

## 54: What are metrics and why do they matter?

Metrics are numbers measured over time, like requests per second, error rate, response time percentiles, memory usage or queue length. They are cheap to store and fast to query, so they are used for dashboards and alerts.

Logs tell you what happened in one request. Metrics tell you how the whole service is doing. Most teams start with the "RED" metrics for each service: **R**ate (requests per second), **E**rrors (failed requests) and **D**uration (latency).

## 55: What is Prometheus?

Prometheus is an open source monitoring system that collects metrics by scraping an HTTP endpoint (usually `/metrics`) on each service at regular intervals. It stores them as time series and lets you query them with PromQL. Grafana is often used on top of it for dashboards.

In Node.js, the `prom-client` package exposes metrics in the Prometheus format.

```js
import express from "express";
import client from "prom-client";

client.collectDefaultMetrics();
const app = express();

app.get("/metrics", async (req, res) => {
  res.set("Content-Type", client.register.contentType);
  res.send(await client.register.metrics());
});
```

## 56: What are the three pillars of observability?

1. **Logs:** detailed records of individual events.
2. **Metrics:** numeric measurements over time.
3. **Traces:** the path and timing of a request across services.

They work best together. A metric alert tells you the error rate is high, a trace shows which service is failing, and the logs for that trace explain why. Many teams also add a fourth signal, continuous **profiling**, to see where CPU and memory go.

## 57: Why are timeouts important in microservices?

Without a timeout, a call to a slow or stuck service can wait forever. Each waiting request holds memory and sockets, and under load the calling service can run out of resources and fail too. This is how one slow service brings down others.

Every outgoing network call should have a timeout. With the built-in `fetch` in Node.js, you can use `AbortSignal.timeout()`:

```js
const res = await fetch("http://inventory:3000/stock/42", {
  signal: AbortSignal.timeout(2000),
});
```

## 58: What is a retry and when should you retry a request?

A retry means sending a failed request again, hoping the problem was temporary. Network blips, a restarting instance or a `503 Service Unavailable` often succeed on the second try.

Retry only when:

- The error is temporary (timeouts, connection resets, 502, 503, 504, 429).
- The operation is safe to repeat (idempotent), like a `GET` or a `PUT`, or a `POST` with an idempotency key.

Do not retry `400` or `404` errors, they will fail again. Always limit the number of retries and wait between them.

## 59: What is exponential backoff?

Exponential backoff means waiting longer after each failed attempt, for example 100 ms, 200 ms, 400 ms, 800 ms. This gives the failing service time to recover instead of hitting it with constant retries.

It is usually combined with **jitter**, a random part of the delay, so that many clients that failed at the same moment do not all retry at the same moment too.

## 60: What is idempotency?

An operation is idempotent if doing it once or many times gives the same result. `GET /users/1`, `PUT /users/1` and `DELETE /users/1` are idempotent by design. `POST /payments` is not, because sending it twice could charge the customer twice.

Idempotency matters in microservices because retries and message redelivery are normal. Services should be built so that handling the same request or message twice does not cause damage.

## 61: What is an idempotency key?

An idempotency key is a unique value the client sends with a request, often in an `Idempotency-Key` header. The server stores the key with the result of the first request. If the same key comes again, the server returns the stored result instead of doing the work again.

```http
POST /payments
Idempotency-Key: 6f1e7d0a-2c3b-4b8e-9f3a-1d2e3f4a5b6c
Content-Type: application/json

{ "orderId": "o_123", "amount": 4999 }
```

Payment APIs like Stripe use this so that a client can safely retry a payment request after a timeout.

## 62: What is the circuit breaker pattern?

A circuit breaker wraps calls to another service and tracks failures. It has three states:

- **Closed:** calls go through normally.
- **Open:** after too many failures, calls fail right away without hitting the service.
- **Half-open:** after a wait, a few test calls are allowed. If they succeed, the circuit closes again. If not, it opens again.

It protects both sides: the caller stops wasting time on a service that is down, and the failing service gets room to recover. In Node.js, `opossum` is the most common library for this.

## 63: What is a fallback?

A fallback is what a service does when a call to another service fails. Instead of returning an error, it returns something reasonable.

Examples:

- Show cached product data when the catalog service is down.
- Show generic recommendations when the recommendation service fails.
- Accept an order and process payment later from a queue.

Fallbacks only make sense when a degraded answer is better than an error. For a payment confirmation, an error is usually the right answer.

## 64: What is graceful degradation?

Graceful degradation means the system keeps working with reduced features when some parts fail, instead of failing completely. A product page might load without reviews or recommendations if those services are down, but the user can still see the product and buy it.

You design for it by marking which dependencies are critical and which are optional, and adding timeouts and fallbacks for the optional ones.

## 65: What is rate limiting?

Rate limiting restricts how many requests a client can make in a time window, for example 100 requests per minute per API key. Requests over the limit get a `429 Too Many Requests` response, usually with a `Retry-After` header.

It protects services from abuse, buggy clients and traffic spikes. It is often done at the API gateway, and the counters are kept in Redis so that all instances share them.

## 66: Why is caching used in microservices?

Caching keeps the result of an expensive operation so it can be reused. In microservices it reduces:

- Latency, because reading from memory or Redis is faster than a network call plus a database query.
- Load on downstream services and databases.
- Dependency on other services being available.

Common places to cache: inside the process (an in-memory LRU cache), in a shared cache like Redis, in an HTTP cache or CDN, or at the API gateway. The hard part is deciding when cached data is too old.

## 67: What is Redis and how is it used with microservices?

Redis is an in-memory data store that supports strings, hashes, lists, sets, sorted sets, streams and more. It is very fast and is used in microservices for:

- Shared caches
- Rate limit counters
- Session storage for stateless services
- Distributed locks
- Pub/sub messaging
- Job queues (BullMQ is built on Redis)
- Simple event streams with Redis Streams

In Node.js, the common clients are `ioredis` and the official `redis` package (node-redis).

## 68: What is a JWT?

A JSON Web Token (JWT) is a signed token that carries claims about a user, like their ID, roles and when the token expires. It has three parts separated by dots: header, payload and signature.

```text
eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1XzQyIiwicm9sZSI6ImFkbWluIn0.signature
```

Services can verify the signature using a shared secret or a public key, without calling the auth service. This makes JWTs popular in microservices. The payload is only encoded, not encrypted, so never put secrets in it.

## 69: How does authentication usually work in a microservices system?

A common setup:

1. The user logs in through an identity provider or auth service (Keycloak, Auth0, Okta, Cognito or your own).
2. The user gets an access token, usually a short-lived JWT.
3. The client sends it in the `Authorization: Bearer <token>` header.
4. The API gateway checks the token, and often each service checks it again.
5. Services read the user ID and roles from the token to make authorization decisions.

This way, services do not need to call the auth service on every request.

## 70: What is the difference between authentication and authorization?

**Authentication** checks who you are, for example by verifying a password or a token. **Authorization** checks what you are allowed to do, for example whether user `u_42` can cancel order `o_123`.

In microservices, authentication is often centralized at the gateway or identity provider, while authorization is usually done in each service, because each service knows its own business rules.

## 71: What is OAuth 2.0?

OAuth 2.0 is a standard for giving an application limited access to a resource on behalf of a user or of itself, using access tokens. It defines several flows (grant types):

- **Authorization code with PKCE:** for web and mobile apps where a user logs in.
- **Client credentials:** for service-to-service calls with no user involved.
- **Refresh token:** to get a new access token without logging in again.

OpenID Connect (OIDC) is a layer on top of OAuth 2.0 that adds user identity (the ID token). The older implicit and password flows are no longer recommended.

## 72: How do services authenticate each other?

Common options:

- **OAuth 2.0 client credentials:** each service gets its own client ID and secret, asks the identity provider for a token and sends it with each call.
- **Mutual TLS (mTLS):** both sides present certificates, so each knows who the other is. A service mesh like Istio or Linkerd can do this for you.
- **Signed JWTs:** a service signs a short-lived token with its private key.
- **Cloud IAM:** platforms like AWS IAM or GCP service accounts provide identities for workloads.

Shared static API keys are simple but harder to rotate and audit.

## 73: What is CORS and where should it be handled?

CORS (Cross-Origin Resource Sharing) is a browser feature that blocks a web page from calling an API on a different origin unless the API allows it with headers like `Access-Control-Allow-Origin`.

It only matters for calls from browsers. Calls between backend services are not affected by CORS. In a microservices setup, CORS is usually handled once at the API gateway or BFF, since that is the only part the browser talks to.

## 74: What is API versioning?

API versioning lets you change an API without breaking existing clients. When you make a breaking change, you release a new version and keep the old one running for a while.

Common ways:

- In the URL: `/v1/orders`, `/v2/orders`
- In a header: `Accept: application/vnd.myapp.v2+json`
- In a query parameter: `/orders?version=2`

URL versioning is the most common because it is easy to see and route. Most changes should be backward compatible though (like adding optional fields), so new versions should be rare.

## 75: What is a breaking change in an API?

A breaking change is any change that can make existing clients fail. Examples:

- Removing or renaming a field or endpoint
- Changing a field's type (number to string)
- Making an optional field required in a request
- Changing the meaning of a value or status code
- Changing error formats

Changes that are usually safe: adding new endpoints, adding optional request fields, adding new fields to responses (if clients ignore unknown fields).

## 76: What is OpenAPI?

OpenAPI (formerly Swagger) is a standard format, in YAML or JSON, for describing REST APIs: endpoints, parameters, request and response bodies, status codes and auth. The current version is OpenAPI 3.1, with 3.2 published in 2025.

```yaml
openapi: 3.1.0
info:
  title: Orders API
  version: 1.0.0
paths:
  /orders/{id}:
    get:
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: The order
```

From an OpenAPI file you can generate docs, client SDKs, request validation and mock servers. Frameworks like Fastify (with `@fastify/swagger`) and NestJS (with `@nestjs/swagger`) can generate it from code.

## 77: Why should you validate incoming requests in every service?

Each service should treat input from other services the same way it treats input from users: as untrusted. A bug in another service, an old client or an attacker who got inside the network can send bad data.

Validation catches bad input early with a clear `400` error instead of a strange crash deep in the code or bad data saved in the database. Common tools in Node.js are Zod, Valibot, Ajv (JSON Schema, used by Fastify) and class-validator in NestJS.

## 78: How do you return errors from a REST microservice?

Use the right HTTP status code and a consistent JSON body. Many teams use the Problem Details format from RFC 9457 (which replaced RFC 7807):

```http
HTTP/1.1 404 Not Found
Content-Type: application/problem+json

{
  "type": "https://example.com/problems/order-not-found",
  "title": "Order not found",
  "status": 404,
  "detail": "Order o_123 does not exist",
  "instance": "/orders/o_123"
}
```

Use the same format in all services so clients and the gateway can handle errors the same way. Do not leak stack traces or internal details in production.

## 79: What HTTP status codes do microservices use most?

- `200 OK`, `201 Created`, `202 Accepted` (work queued for later), `204 No Content`
- `400 Bad Request` for invalid input, `401 Unauthorized` for a missing or bad token, `403 Forbidden` for no permission
- `404 Not Found`, `409 Conflict` (for example a duplicate or a version conflict), `422 Unprocessable Content` for valid JSON that breaks business rules
- `429 Too Many Requests` for rate limits
- `500 Internal Server Error` for bugs
- `502 Bad Gateway` and `504 Gateway Timeout` when an upstream service fails or is too slow
- `503 Service Unavailable` when the service is overloaded or starting

Using them correctly matters because retries, circuit breakers and gateways make decisions based on them.

## 80: Which Node.js frameworks are commonly used to build microservices?

- **Express:** the most widely used, minimal and flexible. Express 5 is now the current major version.
- **Fastify:** fast, with built-in JSON Schema validation, a plugin system and good logging with Pino.
- **NestJS:** a structured framework with dependency injection and modules, plus a built-in microservices package with transports for TCP, Redis, NATS, MQTT, RabbitMQ, Kafka and gRPC.
- **Hono:** small and fast, runs on Node.js, Bun, Deno and edge runtimes.
- **Moleculer:** a framework made specifically for microservices, with built-in service discovery and a service broker.

Plain `node:http` is also an option for very small services.

## 81: What is Fastify and why is it popular for microservices?

Fastify is a Node.js web framework focused on low overhead. Reasons people pick it for microservices:

- Fast routing and JSON serialization
- Request and response validation with JSON Schema built in
- Pino logging built in, with a request ID on every log line
- A plugin system with encapsulation that keeps code organized
- Good TypeScript support

```js
import Fastify from "fastify";

const app = Fastify({ logger: true });

app.get(
  "/orders/:id",
  {
    schema: {
      params: {
        type: "object",
        properties: { id: { type: "string" } },
        required: ["id"],
      },
    },
  },
  async (request) => {
    return { id: request.params.id, status: "paid" };
  },
);

await app.listen({ port: 3000, host: "0.0.0.0" });
```

## 82: Why do you need to listen on 0.0.0.0 inside a container?

If a server listens only on `127.0.0.1` (localhost), it only accepts connections from inside the same container. Traffic from other containers or from the host comes through a different network interface and cannot reach it.

Listening on `0.0.0.0` (or `::` for IPv6) accepts connections on all interfaces. Fastify listens on localhost by default, so you need `host: '0.0.0.0'` in containers. Express and `node:http` listen on all interfaces by default when you pass only a port.

## 83: What is NestJS microservices?

NestJS has a `@nestjs/microservices` package that lets you build services that communicate over a transport other than HTTP. You define message handlers with decorators, and NestJS takes care of the transport.

```ts
import { Controller } from "@nestjs/common";
import { MessagePattern, EventPattern, Payload } from "@nestjs/microservices";

@Controller()
export class OrdersController {
  @MessagePattern("get_order")
  getOrder(@Payload() id: string) {
    return { id, status: "paid" };
  }

  @EventPattern("order_created")
  handleOrderCreated(@Payload() data: { id: string }) {
    console.log("new order", data.id);
  }
}
```

`@MessagePattern` is for request-response, `@EventPattern` is for fire-and-forget events.

## 84: What is a monorepo and why is it used for microservices?

A monorepo is one Git repository that holds many services and shared packages. In Node.js, it is usually managed with npm, pnpm or Yarn workspaces, often with a build tool like Nx or Turborepo.

Benefits: easy code sharing, one place to change shared types, atomic changes across services and consistent tooling. Downsides: the repo grows large, CI must be smart enough to build and test only what changed, and it is easier to accidentally couple services.

## 85: What is a polyrepo?

A polyrepo setup has one repository per service. Each repo has its own CI pipeline, versioning and access rules.

It gives strong separation and clear ownership, and each repo stays small. The downsides are that sharing code needs published packages, changes across services need several pull requests and tooling can drift apart between repos.

## 86: Should microservices share code?

Sharing is fine for technical code that rarely changes and has no business logic, for example logging setup, tracing setup, error classes or HTTP client helpers. These are usually published as internal npm packages or kept in a monorepo package.

Be careful with sharing business logic or domain models. If ten services depend on one shared `Order` class, a change to it forces changes everywhere, and you lose independence. Some duplication between services is usually better than tight coupling.

## 87: What is semantic versioning and why does it matter for services?

Semantic versioning (semver) uses `MAJOR.MINOR.PATCH`:

- **MAJOR** for breaking changes
- **MINOR** for new backward compatible features
- **PATCH** for backward compatible bug fixes

It matters for shared packages, client SDKs and API contracts, so that consumers know when an upgrade is safe. In `package.json`, `^1.4.0` accepts any `1.x.x` from 1.4.0 up, while `~1.4.0` accepts only `1.4.x`.

## 88: What is CI/CD in the context of microservices?

**Continuous integration (CI)** runs tests, linting and builds on every change. **Continuous delivery or deployment (CD)** automatically ships passing changes to environments, up to production.

With microservices, each service should have its own pipeline so it can be released independently. A typical pipeline: install, lint, type check, unit tests, build a Docker image, run integration and contract tests, push the image to a registry, deploy to staging, run smoke tests, then deploy to production.

## 89: What is a rolling deployment?

A rolling deployment replaces old instances with new ones a few at a time. For example, with 10 instances, Kubernetes starts 2 new ones, waits for them to be ready, then stops 2 old ones, and repeats.

There is no downtime and no need for double the capacity. The catch is that for a while both versions run at the same time, so the new version must be compatible with the old one, including the database schema and message formats.

## 90: What is a blue-green deployment?

In a blue-green deployment you have two identical environments. **Blue** runs the current version and gets all traffic. You deploy the new version to **green**, test it, then switch all traffic to green at once. If something is wrong, you switch back to blue.

It gives fast rollbacks and a clean switch, but you need double the resources while both run, and the database has to work with both versions.

## 91: What is a canary release?

A canary release sends a small part of the traffic, for example 5%, to the new version while the rest stays on the old one. You watch error rates and latency. If the new version looks good, you increase the share step by step until it gets 100%. If it looks bad, you send all traffic back to the old version.

It limits the impact of a bad release to a small group of users. Tools like Argo Rollouts, Flagger and service meshes can automate this.

## 92: What is a feature flag?

A feature flag is a switch in the code that turns a feature on or off at runtime without deploying again.

```js
if (await flags.isEnabled("new-checkout", { userId })) {
  return newCheckout(cart);
}
return oldCheckout(cart);
```

Flags let you deploy code before releasing it, release to a few users first and turn off a broken feature quickly. Tools include LaunchDarkly, Unleash, Flagsmith and the OpenFeature standard SDK. Remove old flags once a feature is fully released, or they turn into clutter.

## 93: What is graceful shutdown?

Graceful shutdown means that when a service is asked to stop, it finishes what it is doing before exiting. It stops accepting new requests, waits for in-flight requests to finish, stops consuming messages, closes database and broker connections, and then exits.

Without it, every deployment or scale-down would cut off active requests and could leave half-processed messages. In Kubernetes, the container gets `SIGTERM` first and `SIGKILL` after the grace period (30 seconds by default).

## 94: What is SIGTERM and how do you handle it in Node.js?

`SIGTERM` is the signal that orchestrators like Kubernetes and Docker send to ask a process to stop. By default Node.js exits right away, so you need to handle it yourself.

```js
import http from "node:http";

const server = http.createServer(handler);
server.listen(3000);

process.on("SIGTERM", () => {
  console.log("SIGTERM received, shutting down");
  server.close(() => {
    process.exit(0);
  });
});
```

`server.close()` stops accepting new connections and calls the callback once existing ones are done. Make sure Node runs as the main process (PID 1) or behind a small init like `tini`, otherwise the signal may not reach it.

## 95: What is the Node.js cluster module?

The `node:cluster` module lets you start several Node.js processes (workers) that share the same server port. The primary process forks workers, usually one per CPU core, and spreads connections between them.

In containerized microservices it is used less often. It is usually simpler to run one Node process per container and let Kubernetes run more containers. That way the orchestrator handles restarts, scaling and resource limits.

## 96: What is PM2?

PM2 is a process manager for Node.js. It keeps apps running, restarts them if they crash, can run them in cluster mode on all CPU cores and has log management and basic monitoring.

It is popular on plain virtual machines. In Kubernetes, the platform already restarts and scales containers, so you normally run `node` directly instead of PM2 to avoid two layers trying to manage the same process.

## 97: What is the Backend for Frontend (BFF) pattern?

A BFF is a backend service built for one specific frontend, like the web app or the mobile app. It calls the internal microservices, combines the data and returns exactly what that frontend needs.

Different clients have different needs: a mobile app wants small responses, the web app may need more data. Instead of one general API that fits nobody well, each client has its own BFF, usually owned by the frontend team. Node.js is a very common choice for BFFs.

## 98: What is the difference between a microservice and a serverless function?

A microservice is a long-running process that you deploy and scale, usually in a container. A serverless function (AWS Lambda, Google Cloud Run functions, Azure Functions) is code that the platform runs on demand for each event and scales to zero when there is no traffic.

A microservice can be built from serverless functions, but they are not the same thing. Functions have cold starts, time limits and no long-lived connections, while containers give you more control and steady performance under constant load.

## 99: What are webhooks?

A webhook is an HTTP callback: when something happens in a system, it sends a `POST` request to a URL you registered. For example, a payment provider calls your `/webhooks/stripe` endpoint when a payment succeeds.

A webhook receiver should:

- Verify the signature to make sure the request is real.
- Respond quickly with `2xx` and do the heavy work later, often by putting it on a queue.
- Handle duplicates, because providers retry on failure.

## 100: What is the difference between polling and push-based communication?

With **polling**, a service asks another service again and again if there is something new, for example every 10 seconds. It is simple, but it wastes requests and adds delay.

With **push**, the source tells the interested party when something changes, using webhooks, message brokers, WebSockets or Server-Sent Events. It is faster and more efficient, but needs more setup and handling for missed messages.

Between backend services, publishing events to a broker is usually the cleaner way to push.

## 101: What is RabbitMQ?

RabbitMQ is a popular open source message broker. It implements AMQP 0-9-1 and also supports AMQP 1.0, MQTT and STOMP. Producers publish messages to **exchanges**, exchanges route them to **queues** based on rules called **bindings**, and consumers read from queues.

It is a good fit for task queues, routing messages by type and request-reply patterns. In Node.js, the most used client is `amqplib`. RabbitMQ also has **streams**, an append-only log type for replayable messages, and **quorum queues**, a replicated queue type recommended for durable data.

## 102: What are the exchange types in RabbitMQ?

- **Direct:** routes a message to queues whose binding key exactly matches the routing key.
- **Topic:** routes by pattern, where `*` matches one word and `#` matches zero or more words. For example `order.*.created`.
- **Fanout:** sends a copy to every bound queue and ignores the routing key.
- **Headers:** routes based on message header values instead of the routing key.

There is also the default exchange (an unnamed direct exchange), which routes a message to the queue whose name matches the routing key.

## 103: What is Apache Kafka?

Kafka is a distributed event streaming platform. Instead of deleting messages after they are read, it stores them in an append-only log for a configured time (for example 7 days, or forever). Consumers track their own position (offset) and can re-read old messages.

It handles very high throughput and is used for event-driven microservices, data pipelines, activity tracking and change data capture. Recent Kafka versions (4.x) run in KRaft mode only, without ZooKeeper. In Node.js, common clients are `kafkajs` and Confluent's `@confluentinc/kafka-javascript`, which is based on librdkafka.

## 104: What are topics, partitions and offsets in Kafka?

- A **topic** is a named stream of messages, like `orders`.
- A topic is split into **partitions**. Each partition is an ordered log stored on brokers. Partitions allow parallel reading and writing.
- An **offset** is the position of a message in a partition, a number that only goes up.

Messages with the same key always go to the same partition, so order is kept per key (for example per order ID). There is no order guarantee across different partitions.

## 105: What is a consumer group in Kafka?

A consumer group is a set of consumers that share the work of reading a topic. Each partition is assigned to exactly one consumer in the group, so every message is processed once per group.

If a topic has 6 partitions and you run 3 consumers in the group, each gets 2 partitions. If you run 8 consumers, 2 will be idle. Different groups (for example `email-service` and `analytics-service`) each get all messages independently.

## 106: What is BullMQ?

BullMQ is a job queue library for Node.js built on Redis. You add jobs to a queue, and workers process them, with support for retries, delays, priorities, rate limits, repeatable jobs and job dependencies (flows).

```js
import { Queue, Worker } from "bullmq";

const connection = { host: "localhost", port: 6379 };
const emails = new Queue("emails", { connection });

await emails.add("welcome", { userId: "u_42" }, { attempts: 3 });

new Worker(
  "emails",
  async (job) => {
    await sendWelcomeEmail(job.data.userId);
  },
  { connection },
);
```

It is a good choice for background work inside one service or a small group of Node.js services. For events shared across many teams, a real broker like Kafka or RabbitMQ is more common.

## 107: What is a dead letter queue?

A dead letter queue (DLQ) is a separate queue where messages go when they cannot be processed, for example after failing too many times or being rejected.

Without a DLQ, a bad message can be retried forever and block other messages, or be dropped and lost. With a DLQ, you keep the message, set up an alert and can inspect it, fix the bug and replay it later. RabbitMQ supports this with dead letter exchanges, and SQS with redrive policies. In Kafka you usually create a separate DLQ topic yourself.

## 108: What does acknowledging a message mean?

Acknowledging (acking) a message tells the broker that the consumer has finished processing it and the broker can remove it or mark it as done.

If the consumer crashes before acking, the broker delivers the message again to another consumer. This is why you should ack only after the work is actually done, not when the message arrives. In RabbitMQ you call `channel.ack(msg)`. In Kafka, the equivalent is committing the offset.

## 109: What are the message delivery guarantees?

- **At most once:** a message is delivered zero or one time. It can be lost, but never duplicated. You get this if you ack before processing.
- **At least once:** a message is delivered one or more times. It is never lost, but can be duplicated. You get this if you ack after processing. This is the most common choice.
- **Exactly once:** each message affects the system once. True exactly-once delivery across systems is very hard. In practice, people get "effectively once" by combining at-least-once delivery with idempotent consumers.

## 110: Why should message consumers be idempotent?

With at-least-once delivery, the same message can arrive twice: the consumer may crash after doing the work but before acking, a network problem may cause a redelivery, or a producer may retry and publish it twice.

An idempotent consumer handles duplicates safely. Common ways:

- Store processed message IDs and skip ones you have already seen.
- Use upserts instead of inserts.
- Use conditions, like "set status to shipped only if it is currently paid".

## 111: What should a message or event contain?

A good event usually has:

- A unique `id` for deduplication
- A `type`, like `order.created`
- A `version` of the schema
- A `timestamp` (`occurredAt`) in UTC
- A `source` service
- A correlation or trace ID
- The `data` itself

```json
{
  "id": "0b1f8c4e-2d6a-4a6f-9c1e-7a3b2d1f0e9c",
  "type": "order.created",
  "version": 1,
  "source": "orders-service",
  "occurredAt": "2026-10-23T09:15:00.000Z",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "data": { "orderId": "o_123", "userId": "u_42", "total": 4999 }
}
```

CloudEvents is a standard format for this kind of envelope.

## 112: What is CloudEvents?

CloudEvents is a CNCF specification for describing event data in a common way. It defines standard attributes like `id`, `source`, `type`, `specversion`, `time` and `datacontenttype`, and how to send them over HTTP, Kafka, AMQP and other protocols.

Using it means different services, teams and tools can understand each other's events without custom conventions. There is an official `cloudevents` npm package for Node.js.

## 113: What is the saga pattern?

A saga is a way to handle a business process that spans several services without a distributed transaction. It is a sequence of local transactions. Each service does its step and then triggers the next one. If a step fails, the saga runs **compensating actions** to undo the steps that already succeeded.

Example for an order:

1. Orders service creates the order as `PENDING`.
2. Payments service charges the card.
3. Inventory service reserves the stock.
4. If inventory fails, payments refunds the card and orders marks the order `CANCELLED`.

## 114: What is a compensating transaction?

A compensating transaction is an action that undoes the effect of an earlier step in a saga. It is not a database rollback, because the earlier step is already committed. It is a new business operation that reverses it.

Examples: refunding a payment, releasing reserved stock, cancelling a booking. Some actions cannot be undone, like sending an email, so you either put them at the end of the saga or compensate with another action, like sending a correction email.

## 115: What is the outbox pattern?

The outbox pattern solves the problem of saving data and publishing an event reliably. If you write to the database and then publish to Kafka, the publish can fail after the write succeeds, or the other way around.

With an outbox, the service writes the business change and the event into an `outbox` table in the **same database transaction**. A separate process then reads new rows from the outbox and publishes them to the broker, marking them as sent. If publishing fails, it tries again later. This gives at-least-once publishing, so consumers must be idempotent.

## 116: What is the strangler fig pattern?

The strangler fig pattern is a way to move from a monolith to microservices step by step. You put a proxy or gateway in front of the monolith. Then you build one feature at a time as a new service and route its traffic to the new service, while the rest still goes to the monolith. Over time the monolith shrinks until it can be removed.

It avoids a risky "big bang" rewrite. The name comes from the strangler fig tree, which grows around a host tree and slowly replaces it.

## 117: How do you run several microservices locally?

The most common way is Docker Compose. You describe each service, its database, Redis, the broker and so on in a `compose.yaml` file and start everything with one command.

```yaml
services:
  orders:
    build: ./orders
    ports: ["3001:3000"]
    environment:
      DATABASE_URL: postgres://postgres:postgres@orders-db:5432/orders
    depends_on: [orders-db]
  orders-db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: postgres
```

```bash
docker compose up
```

For larger systems, teams also use tools like Tilt or Skaffold with a local Kubernetes cluster, or run only the service they work on locally and connect it to a shared dev environment.

## 118: What types of tests are used for microservices?

- **Unit tests:** test functions and classes inside a service with no network or database.
- **Integration tests:** test a service with its real database, cache or broker, often started with Testcontainers.
- **Component tests:** test one whole service through its API, with other services mocked.
- **Contract tests:** check that a provider's API matches what its consumers expect, for example with Pact.
- **End-to-end tests:** test a full user flow across several running services.

The usual advice is many unit and integration tests, some contract tests and only a few end-to-end tests, because those are slow and flaky.

## 119: What is contract testing?

Contract testing checks that two services agree on how they talk to each other, without running both at the same time.

With consumer-driven contracts (the Pact approach), the consumer writes tests that describe the requests it sends and the responses it expects. This produces a contract file. The provider then runs that contract against its real API in its own CI. If the provider changes its API in a way that breaks the consumer, the provider's build fails before deployment.

## 120: Why are end-to-end tests hard with microservices?

- You need all services, databases and brokers running in the right versions.
- Tests are slow, often minutes instead of seconds.
- They are flaky because of timing, async messages and network issues.
- When one fails, it is hard to know which service caused it.
- Test data has to be set up across many databases.

Most teams keep only a few end-to-end tests for the most important flows, like signup and checkout, and rely on contract and integration tests for the rest.

## 121: What is Testcontainers?

Testcontainers is a library that starts real Docker containers (PostgreSQL, Redis, Kafka, RabbitMQ and others) from your test code and removes them after the tests. The Node.js version is the `testcontainers` npm package, with modules like `@testcontainers/postgresql`.

```js
import { PostgreSqlContainer } from "@testcontainers/postgresql";

const container = await new PostgreSqlContainer("postgres:17").start();
const url = container.getConnectionUri();
// run migrations and tests against url
await container.stop();
```

It makes integration tests realistic without a shared test database.

## 122: What is a service mesh?

A service mesh is an infrastructure layer that handles service-to-service communication for you. It usually works by putting a proxy next to each service (a sidecar) or on each node, and all traffic goes through these proxies.

It can give you, without changing service code:

- Mutual TLS between services
- Retries, timeouts and circuit breaking
- Traffic splitting for canary releases
- Metrics and traces for every call
- Access policies (which service can call which)

Popular meshes: Istio (with both sidecar and sidecar-less "ambient" mode) and Linkerd.

## 123: What is a sidecar?

A sidecar is a helper container that runs next to the main container in the same Kubernetes pod. It shares the network and can share volumes, so it can add features without changing the main app.

Common sidecars: service mesh proxies (Envoy, linkerd-proxy), log shippers, secret fetchers and the OpenTelemetry Collector. Kubernetes now has native sidecar support (init containers with `restartPolicy: Always`), which starts sidecars before the app and stops them after it.

## 124: What is mutual TLS (mTLS)?

In normal TLS, only the server shows a certificate, so the client knows who the server is. In mutual TLS, the client also shows a certificate, so both sides prove who they are.

Between microservices, mTLS encrypts all traffic and lets a service know which service is calling it. Managing certificates for every service by hand is a lot of work, so it is usually done by a service mesh or a tool like SPIFFE/SPIRE that issues and rotates certificates automatically.

## 125: How should microservices handle secrets?

- Never commit secrets to Git or bake them into Docker images.
- Store them in a secrets manager: HashiCorp Vault, AWS Secrets Manager, Google Secret Manager, Azure Key Vault or Kubernetes Secrets (with encryption at rest turned on).
- Give each service access only to the secrets it needs.
- Rotate secrets regularly and support rotation without downtime.
- Do not log secrets or include them in error messages.

Tools like External Secrets Operator can sync secrets from a cloud manager into Kubernetes.

## 126: What is centralized configuration?

Centralized configuration means keeping service settings in one managed place instead of in each service's files. Services read their config from it at startup, and some can reload it without restarting.

Options include Kubernetes ConfigMaps, HashiCorp Consul, AWS AppConfig or Parameter Store, and Spring Cloud Config. It makes it easier to change settings across environments and to see what each service is running with. Secrets should still go to a secrets manager, not a general config store.

## 127: What is the difference between configuration and secrets?

**Configuration** is non-sensitive settings: ports, log levels, feature toggles, URLs of other services, timeouts. It is fine for many people to see it.

**Secrets** are sensitive values: passwords, API keys, private keys, tokens. They need encryption, strict access control, audit logs and rotation.

Both are often passed to the service as environment variables or files, but they should be stored and managed differently.

## 128: What are WebSockets and when would a microservice use them?

WebSockets give a long-lived, two-way connection between a client and a server over one TCP connection. They are used for real-time features like chat, live dashboards, notifications and multiplayer games.

In microservices, a dedicated real-time service (or gateway) often holds the WebSocket connections. Other services publish events to a broker or Redis pub/sub, and the real-time service pushes them to connected clients. Since connections are stateful, scaling needs care: an event must reach whichever instance holds the user's connection.

## 129: What are Server-Sent Events?

Server-Sent Events (SSE) let a server push a stream of text events to the browser over a normal HTTP connection. The browser uses the `EventSource` API and reconnects automatically.

```js
app.get("/events", (req, res) => {
  res.set({ "Content-Type": "text/event-stream", "Cache-Control": "no-cache" });
  res.flushHeaders();
  const timer = setInterval(() => res.write(`data: ${Date.now()}\n\n`), 1000);
  req.on("close", () => clearInterval(timer));
});
```

SSE is one-way (server to client) and simpler than WebSockets, so it is a good choice for notifications, progress updates and streaming AI responses.

## 130: What is API composition?

API composition is a way to answer a query that needs data from several services. A composer (the API gateway, a BFF or a dedicated service) calls each service, combines the results and returns one response.

```js
const [user, orders] = await Promise.all([
  fetch(`http://users/users/${id}`).then((r) => r.json()),
  fetch(`http://orders/orders?userId=${id}`).then((r) => r.json()),
]);
return { ...user, orders };
```

It is simple, but slow if many services are involved, and the response fails or is partial if one of them is down. For complex queries, CQRS with a read model is often better.

## 131: What is CQRS?

CQRS (Command Query Responsibility Segregation) means using separate models for writing data (commands) and reading data (queries). Writes go to a model built for business rules and consistency. Reads come from one or more models built for fast queries, often kept up to date by events.

In microservices, CQRS helps with queries that need data from several services. A service can listen to events from orders, users and products, and build its own read model that answers those queries quickly. The cost is more moving parts and eventual consistency between the write and read sides.

## 132: What is event sourcing?

In event sourcing, you do not store only the current state of an entity. You store every change as an event, in order: `AccountOpened`, `MoneyDeposited`, `MoneyWithdrawn`. The current state is calculated by replaying the events.

Benefits: a full audit log, the ability to rebuild state or build new read models from history, and easy debugging of how something got into a certain state. Costs: more complex code, schema changes for old events and the need for snapshots when an entity has many events. It is often used together with CQRS.

## 133: Is it okay to duplicate data between microservices?

Yes, and it is common. A service can keep a local copy of the data it needs from other services, kept up to date through events. For example, the orders service can store the product name and price at the time of the order instead of calling the product service every time.

The rule is that only one service **owns** the data and can change it. Other services hold read-only copies and accept that their copies may be slightly behind.

## 134: What are sticky sessions and why are they usually avoided?

Sticky sessions mean the load balancer always sends the same client to the same instance, often with a cookie. It is used when the instance keeps session state in memory.

It is usually avoided because:

- Load is not spread evenly.
- If the instance dies, the user loses their session.
- Scaling down or deploying breaks sessions.

It is better to keep services stateless and store sessions in Redis or use tokens. Sticky sessions are still used for some WebSocket setups.

## 135: What is HTTP keep-alive and why does it matter between services?

HTTP keep-alive reuses an open TCP (and TLS) connection for many requests instead of opening a new one each time. Opening a connection costs extra round trips, and with TLS even more.

Between services that call each other constantly, reusing connections lowers latency and CPU use. In Node.js, the built-in `fetch` (based on undici) keeps connections alive by default, and since Node 19 the global `http.Agent` also uses keep-alive by default.

## 136: How do you make HTTP calls to other services in Node.js?

The built-in `fetch` is available globally since Node 18 and is stable since Node 21. It is the simplest choice today.

```js
const res = await fetch("http://users:3000/users/42", {
  headers: { authorization: `Bearer ${token}` },
  signal: AbortSignal.timeout(2000),
});

if (!res.ok) {
  throw new Error(`users service responded with ${res.status}`);
}
const user = await res.json();
```

Other options are `undici` directly (more control over connection pools), `axios` and `got`. Whatever you use, always set a timeout and check the status code, since `fetch` does not throw on `4xx` or `5xx`.

## 137: How do you generate unique IDs in a distributed system?

You cannot use a single auto-increment counter across services, so IDs are usually generated by the service itself:

- **UUID v4:** random, built into Node.js as `crypto.randomUUID()`.
- **UUID v7:** starts with a timestamp, so IDs sort by time and work better as database primary keys. You can generate it with the `uuid` package (`v7()`).
- **ULID:** also time-sortable, shorter as a string.
- **Snowflake-style IDs:** 64-bit numbers with a timestamp, machine ID and sequence.

```js
import { randomUUID } from "node:crypto";

const orderId = randomUUID();
```

## 138: Why should services use UTC for timestamps?

Services run on machines in different time zones, and users are everywhere. If each service stores local time, comparing and sorting events gets messy, and daylight saving changes can create duplicate or missing hours.

Store and send timestamps in UTC, in ISO 8601 format (`2026-10-23T09:15:00.000Z`), and convert to the user's time zone only when showing them. `new Date().toISOString()` in JavaScript always returns UTC.

## 139: How do you paginate results in a microservice API?

Two common ways:

- **Offset pagination:** `GET /orders?limit=20&offset=40`. Simple, but slow on large tables and can skip or repeat items if data changes between pages.
- **Cursor (keyset) pagination:** `GET /orders?limit=20&cursor=eyJpZCI6...`. The cursor points to the last item seen, and the query uses `WHERE id > :lastId`. Faster and stable, but you cannot jump to page 50.

Always set a maximum `limit` so a caller cannot ask for a million rows.

## 140: What is autoscaling?

Autoscaling means the number of service instances changes automatically based on load. In Kubernetes, the Horizontal Pod Autoscaler (HPA) adds or removes pods based on CPU, memory or custom metrics.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: orders
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: orders
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

For queue consumers, KEDA can scale on queue length or Kafka consumer lag, which is often a better signal than CPU.

## 141: What are SLI, SLO and SLA?

- **SLI (Service Level Indicator):** a measurement, like "percentage of requests that succeed in under 300 ms".
- **SLO (Service Level Objective):** a target for that measurement, like "99.9% over 30 days".
- **SLA (Service Level Agreement):** a contract with customers that says what happens (like refunds) if you miss a target.

SLOs help teams decide when to focus on reliability. The gap between 100% and the SLO is the **error budget**. If you have used it up, you slow down releases and fix stability.

## 142: What do p50, p95 and p99 latency mean?

They are percentiles of response time:

- **p50** (median): half of requests are faster than this.
- **p95:** 95% of requests are faster, 5% are slower.
- **p99:** 99% are faster, 1% are slower.

Averages hide problems, so percentiles are used instead. In microservices, high p99 latency matters a lot: if one page calls 20 services, the chance that at least one of them hits its slow 1% is high, so tail latency of each service affects most users.

## 143: What is the difference between latency and throughput?

**Latency** is how long one request takes, for example 120 ms. **Throughput** is how many requests a service can handle per unit of time, for example 2,000 requests per second.

They are related but not the same. Batching can increase throughput while making each item wait longer. Adding instances increases throughput but does not make a single request faster.

## 144: What is the bulkhead pattern?

The bulkhead pattern isolates resources so that a problem in one part cannot use up everything. The name comes from ships, which are split into watertight sections so that one leak does not sink the whole ship.

In practice, it means separate connection pools, concurrency limits or even separate instances for different dependencies or types of work. If the reporting dependency gets slow, it can only use its own limited pool, and calls to the payment service still have capacity.

## 145: What is Conway's Law and why does it matter for microservices?

Conway's Law says that systems tend to copy the communication structure of the organization that builds them. If three teams build a compiler, you get a three-pass compiler.

For microservices, it means service boundaries and team boundaries should match. If one service is owned by four teams, it will be hard to change. Many companies use the "inverse Conway maneuver": they design team structure on purpose to get the architecture they want.

## 146: What does "you build it, you run it" mean?

It means the team that writes a service is also responsible for running it in production: deploying it, monitoring it, being on call and fixing incidents.

This gives teams a direct reason to build reliable, observable services, and it removes slow handoffs to a separate operations team. It works best with a good platform underneath, so teams do not have to build their own CI/CD, logging and Kubernetes setup from scratch.

## 147: What is the W3C Trace Context?

W3C Trace Context is a standard for passing trace information between services in HTTP headers. The main header is `traceparent`:

```text
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

It holds the version, the trace ID, the parent span ID and flags (like whether the trace is sampled). A second header, `tracestate`, holds vendor-specific data. OpenTelemetry uses this format by default, so traces work across services written in different languages.

## 148: How do you pin the Node.js version for a service?

- Use a specific base image tag in the Dockerfile, like `node:24-alpine` or a full version like `node:24.11.0-alpine`.
- Set `engines` in `package.json` so tools can warn about the wrong version.
- Add an `.nvmrc` or `.node-version` file for local development.

```json
{
  "engines": { "node": ">=24 <25" }
}
```

Run production services on an LTS release. Right now Node.js 24 is in Active LTS, Node 22 is in maintenance and Node 26 moves into LTS in October 2026.

## 149: Can you run TypeScript directly in Node.js services?

Yes, with limits. Node.js can strip TypeScript types and run `.ts` files directly. It is on by default from Node 23.6 and Node 22.18, and it became stable in Node 25.2.

```bash
node src/server.ts
```

It only removes type annotations. It does not type check, and it does not support syntax that needs code generation, like `enum` or `namespace`, unless you use `--experimental-transform-types`. For production, many teams still compile with `tsc` or a bundler, and they always run `tsc --noEmit` in CI to check types.

## 150: What is the difference between npm install and npm ci?

`npm install` installs dependencies and can update `package-lock.json` if versions in `package.json` allow newer ones.

`npm ci` installs exactly what is in `package-lock.json`, deletes `node_modules` first and fails if the lockfile does not match `package.json`. It is faster and repeatable, so it is the right choice in CI and in Dockerfiles. With `--omit=dev`, it skips dev dependencies for production images.

---

# Moderate Questions (151-300)

## 151: How do you implement a full graceful shutdown in a Node.js service?

Stop taking new work, finish the current work, close connections, then exit. Add a hard timeout in case something hangs.

```js
import http from "node:http";

const server = http.createServer(app);
server.listen(3000);

let shuttingDown = false;

async function shutdown(signal) {
  if (shuttingDown) return;
  shuttingDown = true;
  logger.info({ signal }, "shutting down");

  const forceExit = setTimeout(() => {
    logger.error("shutdown timed out, forcing exit");
    process.exit(1);
  }, 25_000);
  forceExit.unref();

  try {
    await new Promise((resolve, reject) =>
      server.close((err) => (err ? reject(err) : resolve())),
    );
    await consumer.disconnect();
    await db.end();
    await redis.quit();
    process.exit(0);
  } catch (err) {
    logger.error({ err }, "error during shutdown");
    process.exit(1);
  }
}

process.on("SIGTERM", () => shutdown("SIGTERM"));
process.on("SIGINT", () => shutdown("SIGINT"));
```

Keep the hard timeout below the Kubernetes `terminationGracePeriodSeconds` (30 seconds by default). Since Node 19, `server.close()` also closes idle keep-alive connections, and `server.closeAllConnections()` can force the rest.

## 152: How do you implement liveness and readiness endpoints?

Liveness should only check that the process can respond. Readiness should check what the service needs to do its job.

```js
let ready = false;

app.get("/livez", (req, res) => res.sendStatus(200));

app.get("/readyz", async (req, res) => {
  if (!ready || shuttingDown) return res.sendStatus(503);
  try {
    await db.query("SELECT 1");
    res.sendStatus(200);
  } catch {
    res.sendStatus(503);
  }
});

await db.connect();
await runWarmup();
ready = true;
```

Keep the readiness check cheap and give it a short timeout. Do not check other microservices in readiness: if a downstream service is down, marking every caller unready just spreads the outage.

## 153: How do you configure Kubernetes probes for a Node.js service?

```yaml
containers:
  - name: orders
    image: registry.example.com/orders:1.4.2
    ports:
      - containerPort: 3000
    startupProbe:
      httpGet: { path: /livez, port: 3000 }
      periodSeconds: 2
      failureThreshold: 30
    livenessProbe:
      httpGet: { path: /livez, port: 3000 }
      periodSeconds: 10
      failureThreshold: 3
    readinessProbe:
      httpGet: { path: /readyz, port: 3000 }
      periodSeconds: 5
      failureThreshold: 2
```

The **startup probe** gives slow-starting services time (here up to 60 seconds) before liveness checks begin. The **liveness probe** restarts a stuck container. The **readiness probe** takes the pod out of the Service while it fails. Do not set liveness too aggressive, or a long garbage collection pause or a CPU spike can cause restart loops.

## 154: Why do you sometimes need a delay before shutting down in Kubernetes?

When Kubernetes deletes a pod, two things happen at roughly the same time: the pod gets `SIGTERM`, and the pod is removed from the Service endpoints. Removing it from endpoints takes a moment to reach every node and load balancer. If the app closes its server immediately, some requests still get routed to it and fail.

A common fix is to keep serving for a few seconds after `SIGTERM`, or to add a `preStop` hook:

```yaml
lifecycle:
  preStop:
    sleep:
      seconds: 5
```

The `sleep` action is built into newer Kubernetes versions. On older ones, people use `exec` with `sleep 5`, which needs a shell in the image.

## 155: How do you implement retries with exponential backoff and jitter?

```js
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function isRetryable(err, res) {
  if (err)
    return err.name === "TimeoutError" || err.cause?.code === "ECONNRESET";
  return [429, 502, 503, 504].includes(res.status);
}

export async function fetchWithRetry(
  url,
  options = {},
  { retries = 3, baseMs = 100, maxMs = 2000 } = {},
) {
  for (let attempt = 0; ; attempt++) {
    let res, err;
    try {
      res = await fetch(url, { ...options, signal: AbortSignal.timeout(2000) });
      if (res.ok || !isRetryable(null, res)) return res;
    } catch (e) {
      err = e;
      if (!isRetryable(err)) throw err;
    }
    if (attempt >= retries) {
      if (err) throw err;
      return res;
    }
    const cap = Math.min(maxMs, baseMs * 2 ** attempt);
    await sleep(Math.random() * cap); // "full jitter"
  }
}
```

"Full jitter" picks a random delay between 0 and the backoff cap, which spreads retries out well. If the response has a `Retry-After` header, use it instead.

## 156: What is retry amplification and how do you avoid it?

Retry amplification happens when several layers each retry. If the gateway retries 3 times, the BFF retries 3 times and the orders service retries 3 times, one failing call to the database layer can turn into 27 or more requests, right when that service is already struggling.

Ways to avoid it:

- Retry at only one layer, usually the one closest to the failure or the edge.
- Use a **retry budget**: allow retries only up to a small percentage (for example 10%) of normal traffic.
- Combine retries with circuit breakers.
- Stop retrying when the overall request deadline has passed.

## 157: How do you use a circuit breaker in Node.js?

The `opossum` library wraps any async function:

```js
import CircuitBreaker from "opossum";

async function getRecommendations(userId) {
  const res = await fetch(`http://recs:3000/users/${userId}`, {
    signal: AbortSignal.timeout(1000),
  });
  if (!res.ok) throw new Error(`recs ${res.status}`);
  return res.json();
}

const breaker = new CircuitBreaker(getRecommendations, {
  timeout: 1500, // count as failure if slower than this
  errorThresholdPercentage: 50, // open when half of calls fail
  resetTimeout: 10_000, // try again after 10 seconds
  volumeThreshold: 10, // need at least 10 calls before opening
});

breaker.fallback(() => []);
breaker.on("open", () => logger.warn("recs circuit open"));

const recs = await breaker.fire("u_42");
```

Create one breaker per downstream dependency and reuse it, so it can track failures across requests. Export its state as a metric so you can see when it opens.

## 158: What is deadline propagation?

Deadline propagation means passing the remaining time budget of a request down to every service it calls. If the gateway gives a request 3 seconds and the BFF has already used 1 second, it tells the orders service it has 2 seconds left, and so on.

This stops services from doing work for a request that the caller has already given up on. gRPC has this built in with deadlines. For HTTP, you can send a header like `x-request-deadline` with an absolute timestamp and create an `AbortSignal` from it:

```js
const deadline = Number(req.get("x-request-deadline")) || Date.now() + 3000;
const remaining = Math.max(0, deadline - Date.now() - 50);
const signal = AbortSignal.timeout(remaining);
```

## 159: How do you tune connection pooling for outgoing HTTP calls?

The built-in `fetch` uses undici's global dispatcher. You can replace it with an `Agent` that has settings suited to service-to-service traffic:

```js
import { Agent, setGlobalDispatcher } from "undici";

setGlobalDispatcher(
  new Agent({
    connections: 50, // max connections per origin
    keepAliveTimeout: 10_000,
    keepAliveMaxTimeout: 60_000,
    connectTimeout: 2_000,
  }),
);
```

Too few connections and requests queue up inside your process. Too many and you can overload the downstream service. Also make sure the client's keep-alive timeout is shorter than the server's, otherwise the client may reuse a socket the server just closed and get `ECONNRESET`.

## 160: How do you create a gRPC server in Node.js?

Use `@grpc/grpc-js` with `@grpc/proto-loader` to load the `.proto` file at runtime.

```proto
// orders.proto
syntax = "proto3";
package orders;

service Orders {
  rpc GetOrder (GetOrderRequest) returns (Order);
}

message GetOrderRequest { string id = 1; }
message Order { string id = 1; string status = 2; int64 total = 3; }
```

```js
import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const def = protoLoader.loadSync("orders.proto", {
  keepCase: true,
  longs: String,
});
const proto = grpc.loadPackageDefinition(def).orders;

const server = new grpc.Server();
server.addService(proto.Orders.service, {
  GetOrder(call, callback) {
    const order = findOrder(call.request.id);
    if (!order) {
      return callback({
        code: grpc.status.NOT_FOUND,
        message: "order not found",
      });
    }
    callback(null, order);
  },
});

server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  (err) => {
    if (err) throw err;
  },
);
```

For typed code, many teams generate TypeScript from the `.proto` with tools like `ts-proto` or Buf instead of loading it at runtime.

## 161: How do you call a gRPC service with a deadline?

```js
const client = new proto.Orders(
  "orders:50051",
  grpc.credentials.createInsecure(),
);

client.GetOrder(
  { id: "o_123" },
  { deadline: Date.now() + 2000 },
  (err, order) => {
    if (err?.code === grpc.status.DEADLINE_EXCEEDED) {
      logger.warn("orders service too slow");
      return;
    }
    if (err) throw err;
    console.log(order);
  },
);
```

Always set a deadline. Without one, a gRPC call can wait forever. Create the client once and reuse it, because it keeps an HTTP/2 connection open.

## 162: What types of gRPC calls are there?

1. **Unary:** one request, one response. Like a normal function call.
2. **Server streaming:** one request, a stream of responses. For example, streaming search results or price updates.
3. **Client streaming:** a stream of requests, one response. For example, uploading many metrics and getting a summary.
4. **Bidirectional streaming:** both sides send streams at the same time. For example, chat or real-time sync.

```proto
service Prices {
  rpc Watch (WatchRequest) returns (stream PriceUpdate);
}
```

In Node.js, streaming calls are exposed as Node streams, so you can use `on('data')`, `for await` and `write()`.

## 163: How do gRPC status codes map to HTTP status codes?

gRPC has its own status codes. Common mappings when you put a REST gateway in front:

| gRPC                        | HTTP |
| --------------------------- | ---- |
| `OK`                        | 200  |
| `INVALID_ARGUMENT`          | 400  |
| `UNAUTHENTICATED`           | 401  |
| `PERMISSION_DENIED`         | 403  |
| `NOT_FOUND`                 | 404  |
| `ALREADY_EXISTS`, `ABORTED` | 409  |
| `RESOURCE_EXHAUSTED`        | 429  |
| `UNIMPLEMENTED`             | 501  |
| `UNAVAILABLE`               | 503  |
| `DEADLINE_EXCEEDED`         | 504  |
| `INTERNAL`, `UNKNOWN`       | 500  |

`UNAVAILABLE` is the code that clients usually treat as safe to retry.

## 164: When would you pick gRPC over REST for service-to-service calls?

Pick gRPC when:

- You need low latency and small payloads between many internal services.
- You want a strict, typed contract and generated clients in several languages.
- You need streaming.

Stick with REST when:

- The API is public or called from browsers (gRPC in browsers needs gRPC-Web or Connect and a proxy).
- You want easy debugging with `curl` and readable JSON.
- The team has no experience with protobuf tooling.

Many systems use REST or GraphQL at the edge and gRPC inside.

## 165: Why can gRPC load balancing be a problem in Kubernetes?

gRPC uses HTTP/2, which keeps one long-lived connection and sends many requests over it. A normal Kubernetes Service balances at the connection level (layer 4). So once a client connects to one pod, all its requests go to that pod, and new pods get no traffic.

Fixes:

- Use a headless Service and client-side load balancing in `@grpc/grpc-js` (`dns:///orders-headless:50051` with the `round_robin` policy).
- Use a layer 7 proxy or service mesh (Envoy, Istio, Linkerd) that balances per request.
- Set a max connection age on the server (`grpc.max_connection_age_ms`) so clients reconnect and spread out over time.

## 166: How do you publish messages to RabbitMQ reliably with amqplib?

Use a confirm channel, durable queues and persistent messages, and wait for the broker to confirm.

```js
import amqp from "amqplib";

const conn = await amqp.connect(process.env.AMQP_URL);
const ch = await conn.createConfirmChannel();

await ch.assertExchange("orders", "topic", { durable: true });

export function publish(routingKey, event) {
  return new Promise((resolve, reject) => {
    ch.publish(
      "orders",
      routingKey,
      Buffer.from(JSON.stringify(event)),
      {
        persistent: true,
        contentType: "application/json",
        messageId: event.id,
      },
      (err) => (err ? reject(err) : resolve()),
    );
  });
}

await publish("order.created", { id: crypto.randomUUID(), orderId: "o_123" });
```

Without confirms, `publish` only writes to a local buffer, and a message can be lost if the connection drops. If `publish` returns `false`, the buffer is full, and you should wait for the `drain` event before sending more.

## 167: How do you consume messages from RabbitMQ safely?

Set a prefetch limit, ack only after processing and decide what to do with failures.

```js
const ch = await conn.createChannel();
await ch.assertQueue("email.order-created", {
  durable: true,
  arguments: { "x-queue-type": "quorum", "x-dead-letter-exchange": "dlx" },
});
await ch.bindQueue("email.order-created", "orders", "order.created");
await ch.prefetch(10);

await ch.consume("email.order-created", async (msg) => {
  if (!msg) return; // consumer was cancelled by the broker
  try {
    const event = JSON.parse(msg.content.toString());
    await sendOrderEmail(event);
    ch.ack(msg);
  } catch (err) {
    logger.error({ err }, "failed to handle message");
    ch.nack(msg, false, false); // do not requeue, send to the dead letter exchange
  }
});
```

`prefetch(10)` means the broker sends at most 10 unacked messages to this consumer, which gives backpressure. Requeuing a broken message with `nack(msg, false, true)` can create an endless loop, so dead-lettering is usually safer.

## 168: How do you implement delayed retries in RabbitMQ?

A common way is a retry queue with a TTL that dead-letters back to the main exchange:

1. The consumer fails and publishes the message to `orders.retry` with a header like `x-retry-count`.
2. `orders.retry` has `x-message-ttl: 30000` and `x-dead-letter-exchange: orders`.
3. After 30 seconds the message expires and goes back to the main queue.
4. After N retries, the consumer sends it to the final DLQ instead.

```js
await ch.assertQueue("orders.retry", {
  durable: true,
  arguments: {
    "x-message-ttl": 30_000,
    "x-dead-letter-exchange": "orders",
  },
});
```

For different delays (10 s, 1 min, 10 min) you can use several retry queues. There is also a delayed message exchange plugin, but its maintainers mark it as not suited for large numbers of delayed messages, so check its limits first.

## 169: What is the difference between classic and quorum queues in RabbitMQ?

**Classic queues** live on one node. Since RabbitMQ 4.0, classic mirrored queues have been removed, so classic queues are not replicated.

**Quorum queues** are replicated across several nodes using the Raft algorithm. They survive node failures without losing confirmed messages, and they have built-in poison message handling with a delivery limit.

For durable business messages, quorum queues are the recommended choice. Classic queues are still fine for temporary data, like exclusive reply queues.

## 170: How do you produce messages to Kafka from Node.js?

With `kafkajs`:

```js
import { Kafka } from "kafkajs";

const kafka = new Kafka({
  clientId: "orders-service",
  brokers: ["kafka:9092"],
});
const producer = kafka.producer({ idempotent: true });
await producer.connect();

await producer.send({
  topic: "orders",
  messages: [
    {
      key: order.id,
      value: JSON.stringify({ type: "order.created", data: order }),
      headers: { "event-id": crypto.randomUUID() },
    },
  ],
});
```

The `key` decides the partition, so all events for the same order land in the same partition and stay in order. With `idempotent: true`, the broker removes duplicates caused by producer retries. Create the producer once at startup and disconnect it on shutdown.

Confluent's `@confluentinc/kafka-javascript` offers a KafkaJS-compatible API on top of librdkafka, so migrating between the two is fairly easy.

## 171: How do you consume messages from Kafka and commit offsets?

```js
const consumer = kafka.consumer({ groupId: "email-service" });
await consumer.connect();
await consumer.subscribe({ topics: ["orders"], fromBeginning: false });

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    const event = JSON.parse(message.value.toString());
    await handle(event);
    // offset is committed automatically after eachMessage resolves
  },
});
```

By default kafkajs commits offsets in the background for messages whose handler finished. If the handler throws, the message is retried. If the process crashes after handling but before the commit, the message is processed again, so handlers must be idempotent. For full control you can set `autoCommit: false` and call `consumer.commitOffsets()` yourself.

## 172: How do you choose a partition key in Kafka?

Pick a key that groups the messages that must stay in order. Usually that is the ID of the entity the events are about: `orderId`, `accountId`, `userId`.

Things to watch:

- **Hot keys:** if one key has far more traffic than others (a huge customer), one partition gets overloaded.
- **Too few distinct keys** means poor spread across partitions.
- **No key** spreads messages evenly, but you lose ordering.
- Changing the number of partitions later changes which partition a key maps to, which can break ordering during the change.

## 173: What is consumer lag and why should you monitor it?

Consumer lag is the difference between the latest offset in a partition and the last offset the consumer group has committed. It tells you how far behind the consumer is.

Growing lag means consumers cannot keep up. Users see old data, events get processed late and, if lag goes beyond the retention period, messages are deleted before they are read. Monitor it with tools like Kafka exporter for Prometheus or Burrow, alert on it and use it to autoscale consumers (for example with KEDA).

## 174: What is a consumer group rebalance in Kafka?

A rebalance happens when the set of consumers in a group changes (one joins, leaves or crashes) or the topic's partitions change. Kafka reassigns partitions between the consumers.

With the old "eager" protocol, all consumers stop processing during a rebalance, which causes pauses. Ways to reduce the pain:

- Use cooperative (incremental) rebalancing, and the newer consumer group protocol from KIP-848 where your client supports it.
- Use static group membership so a restarting pod gets its partitions back without a full rebalance.
- Keep message processing fast so consumers do not miss heartbeats and get kicked out.
- Shut down consumers gracefully so they leave the group cleanly.

## 175: What is the difference between Redis pub/sub and Redis Streams?

**Pub/sub** is fire-and-forget. A message goes to whoever is subscribed at that moment. If a subscriber is offline, it misses the message. There is no history and no acks.

**Streams** store messages in an append-only log. They support consumer groups, acks, pending message lists and reading history, similar to a small Kafka.

Use pub/sub for things where missing a message is fine, like cache invalidation hints or pushing live updates to WebSocket servers. Use Streams when messages must not be lost.

## 176: How do you use Redis Streams with consumer groups in Node.js?

```js
import { Redis } from "ioredis";

const redis = new Redis(process.env.REDIS_URL);

// producer
await redis.xadd(
  "orders",
  "*",
  "type",
  "order.created",
  "data",
  JSON.stringify(order),
);

// consumer (create the group once)
await redis
  .xgroup("CREATE", "orders", "email", "$", "MKSTREAM")
  .catch(() => {});

while (running) {
  const res = await redis.xreadgroup(
    "GROUP",
    "email",
    process.env.HOSTNAME,
    "COUNT",
    10,
    "BLOCK",
    5000,
    "STREAMS",
    "orders",
    ">",
  );
  if (!res) continue;
  for (const [, entries] of res) {
    for (const [id, fields] of entries) {
      await handle(fields);
      await redis.xack("orders", "email", id);
    }
  }
}
```

Messages that were read but never acked stay in the pending list. Use `XAUTOCLAIM` to take over messages from consumers that died.

## 177: How do you configure retries and concurrency in BullMQ?

```js
import { Queue, Worker } from "bullmq";

const connection = { host: "redis", port: 6379, maxRetriesPerRequest: null };
const queue = new Queue("invoices", { connection });

await queue.add(
  "generate",
  { orderId: "o_123" },
  {
    jobId: "invoice:o_123", // dedupe: same id is not added twice
    attempts: 5,
    backoff: { type: "exponential", delay: 1000 },
    removeOnComplete: 1000,
    removeOnFail: 5000,
  },
);

const worker = new Worker(
  "invoices",
  async (job) => {
    await generateInvoice(job.data.orderId);
  },
  { connection, concurrency: 5 },
);

worker.on("failed", (job, err) =>
  logger.error({ jobId: job?.id, err }, "job failed"),
);
```

`concurrency` is how many jobs one worker processes at the same time. Workers require `maxRetriesPerRequest: null` on the Redis connection. Clean up finished jobs with `removeOnComplete` and `removeOnFail`, or Redis memory keeps growing.

## 178: How do you implement the outbox pattern in Node.js with PostgreSQL?

Write the business row and the event in one transaction:

```js
const client = await pool.connect();
try {
  await client.query("BEGIN");
  const { rows } = await client.query(
    "INSERT INTO orders (id, user_id, total) VALUES ($1, $2, $3) RETURNING *",
    [orderId, userId, total],
  );
  await client.query(
    "INSERT INTO outbox (id, topic, key, payload) VALUES ($1, $2, $3, $4)",
    [randomUUID(), "orders", orderId, { type: "order.created", data: rows[0] }],
  );
  await client.query("COMMIT");
} catch (err) {
  await client.query("ROLLBACK");
  throw err;
} finally {
  client.release();
}
```

A relay then publishes pending rows:

```js
async function relayOnce() {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    const { rows } = await client.query(
      `SELECT * FROM outbox WHERE sent_at IS NULL
       ORDER BY created_at LIMIT 100 FOR UPDATE SKIP LOCKED`,
    );
    for (const row of rows) {
      await producer.send({
        topic: row.topic,
        messages: [
          {
            key: row.key,
            value: JSON.stringify(row.payload),
            headers: { "event-id": row.id },
          },
        ],
      });
    }
    if (rows.length) {
      await client.query(
        "UPDATE outbox SET sent_at = now() WHERE id = ANY($1)",
        [rows.map((r) => r.id)],
      );
    }
    await client.query("COMMIT");
  } catch (err) {
    await client.query("ROLLBACK");
    throw err;
  } finally {
    client.release();
  }
}
```

`FOR UPDATE SKIP LOCKED` lets several relay instances run without picking the same rows. If the relay crashes after sending but before the update, rows are sent again, so consumers must handle duplicates.

## 179: What is the difference between a polling outbox relay and CDC?

A **polling relay** queries the outbox table every second or so. It is simple and needs no extra infrastructure, but it adds some delay and some database load.

**Change data capture (CDC)** reads the database's transaction log (the PostgreSQL WAL or MySQL binlog) and turns new outbox rows into messages. Debezium is the most common tool. It has lower delay and no polling queries, but you need to run and monitor Debezium and usually Kafka Connect.

Start with polling. Move to CDC when volume or latency needs it.

## 180: What is the inbox pattern?

The inbox pattern is the consumer side of the outbox. When a message arrives, the consumer stores its ID in an `inbox` (or `processed_messages`) table in the same transaction as the business change. If the same message arrives again, the insert fails on the unique key and the consumer skips it.

```js
await client.query("BEGIN");
const { rowCount } = await client.query(
  "INSERT INTO processed_messages (id) VALUES ($1) ON CONFLICT DO NOTHING",
  [eventId],
);
if (rowCount === 0) {
  await client.query("ROLLBACK");
  return; // already processed
}
await client.query("UPDATE stock SET reserved = reserved + $1 WHERE sku = $2", [
  qty,
  sku,
]);
await client.query("COMMIT");
```

This makes a non-idempotent operation (like incrementing a counter) safe with at-least-once delivery.

## 181: What is the difference between choreography and orchestration in sagas?

In **choreography**, there is no central controller. Each service listens to events and publishes its own. Orders publishes `OrderCreated`, payments reacts and publishes `PaymentCompleted`, inventory reacts to that, and so on.

In **orchestration**, a central orchestrator (a service or workflow engine) tells each service what to do with commands and waits for replies. It keeps the state of the saga.

|            | Choreography                   | Orchestration                                |
| ---------- | ------------------------------ | -------------------------------------------- |
| Coupling   | Low, services only know events | Orchestrator knows all steps                 |
| Visibility | Flow is spread across services | Flow is in one place                         |
| Good for   | Short, simple flows            | Long flows with many steps and compensations |

## 182: How would you implement a simple orchestrated saga in Node.js?

Keep the saga state in a database so it survives restarts, and run each step with its compensation.

```js
const steps = [
  {
    name: "reserveStock",
    run: (ctx) => inventory.reserve(ctx),
    undo: (ctx) => inventory.release(ctx),
  },
  {
    name: "chargeCard",
    run: (ctx) => payments.charge(ctx),
    undo: (ctx) => payments.refund(ctx),
  },
  {
    name: "createShipment",
    run: (ctx) => shipping.create(ctx),
    undo: (ctx) => shipping.cancel(ctx),
  },
];

export async function runOrderSaga(ctx) {
  const done = [];
  for (const step of steps) {
    try {
      await step.run(ctx);
      done.push(step);
      await sagaStore.markStepDone(ctx.sagaId, step.name);
    } catch (err) {
      for (const s of done.reverse()) {
        await s.undo(ctx); // compensations must be idempotent and retried until they succeed
      }
      await sagaStore.markFailed(ctx.sagaId, step.name, err.message);
      throw err;
    }
  }
  await sagaStore.markCompleted(ctx.sagaId);
}
```

This is fine for learning, but real sagas need to resume after a crash and handle steps that time out. Workflow engines like Temporal (which has a TypeScript SDK) handle state, retries and timers for you.

## 183: How do you build a simple API gateway in Node.js?

With Fastify and `@fastify/http-proxy`:

```js
import Fastify from "fastify";
import proxy from "@fastify/http-proxy";

const app = Fastify({ logger: true });

app.addHook("onRequest", async (req, reply) => {
  if (req.url.startsWith("/public")) return;
  const user = await verifyToken(req.headers.authorization);
  if (!user) return reply.code(401).send({ error: "unauthorized" });
  req.headers["x-user-id"] = user.sub;
});

app.register(proxy, {
  upstream: "http://users:3000",
  prefix: "/api/users",
  rewritePrefix: "/users",
});
app.register(proxy, {
  upstream: "http://orders:3000",
  prefix: "/api/orders",
  rewritePrefix: "/orders",
});

await app.listen({ port: 8080, host: "0.0.0.0" });
```

With Express, `http-proxy-middleware` does the same job. For most production systems, a dedicated gateway like Kong, Envoy or a cloud gateway is easier to run, and a custom Node gateway or BFF is used where you need custom logic.

## 184: How do you implement rate limiting across many instances?

The counters must be shared, so they are kept in Redis. With Fastify, `@fastify/rate-limit` supports a Redis store:

```js
import rateLimit from "@fastify/rate-limit";
import { Redis } from "ioredis";

await app.register(rateLimit, {
  max: 100,
  timeWindow: "1 minute",
  redis: new Redis(process.env.REDIS_URL),
  keyGenerator: (req) => req.headers["x-api-key"] ?? req.ip,
});
```

For Express there is `express-rate-limit` with `rate-limit-redis`. A simple fixed-window version by hand:

```js
const key = `rl:${clientId}:${Math.floor(Date.now() / 60_000)}`;
const count = await redis.incr(key);
if (count === 1) await redis.expire(key, 60);
if (count > 100) return res.status(429).set("Retry-After", "60").end();
```

## 185: What are the common rate limiting algorithms?

- **Fixed window:** count requests per minute bucket. Simple, but allows bursts at the edges (100 at 0:59 and 100 at 1:00).
- **Sliding window log:** store a timestamp for each request and count those in the last minute. Accurate, but uses more memory.
- **Sliding window counter:** mix the current and previous window counts by weight. A good balance.
- **Token bucket:** tokens refill at a steady rate, and each request uses one. Allows short bursts up to the bucket size.
- **Leaky bucket:** requests are processed at a fixed rate, extra ones wait or are dropped. Smooths traffic.

Token bucket is popular for APIs because it allows small bursts while limiting the average rate.

## 186: How do you verify JWTs in a Node.js service?

Use the `jose` library and fetch the identity provider's public keys from its JWKS endpoint. The keys are cached and refreshed when the provider rotates them.

```js
import { createRemoteJWKSet, jwtVerify } from "jose";

const JWKS = createRemoteJWKSet(
  new URL("https://auth.example.com/.well-known/jwks.json"),
);

export async function authenticate(req, res, next) {
  const token = req.get("authorization")?.replace(/^Bearer /, "");
  if (!token) return res.sendStatus(401);
  try {
    const { payload } = await jwtVerify(token, JWKS, {
      issuer: "https://auth.example.com/",
      audience: "orders-api",
      algorithms: ["RS256"],
    });
    req.user = payload;
    next();
  } catch {
    res.sendStatus(401);
  }
}
```

Always check `iss`, `aud` and `exp`, and allow only the algorithms you expect, so a token signed with `none` or a different algorithm is rejected.

## 187: How do you pass user identity to downstream services?

Options:

1. **Forward the original token.** Each service verifies it itself. Simple and secure, as long as the token's audience allows it.
2. **Token exchange.** The gateway or service exchanges the user token for a new, narrower token for the downstream service (OAuth 2.0 Token Exchange, RFC 8693).
3. **Trusted headers.** The gateway verifies the token and sets headers like `x-user-id`. Services trust these headers only if the network guarantees that requests come from the gateway (for example with mTLS and network policies).

Option 3 is common but risky: if any service can be reached directly, an attacker can fake the headers. Never trust these headers on public routes.

## 188: How do you get and cache a token for service-to-service calls?

With the OAuth 2.0 client credentials flow, request a token and reuse it until shortly before it expires.

```js
let cached = null;

export async function getServiceToken() {
  if (cached && cached.expiresAt > Date.now() + 30_000) return cached.token;

  const res = await fetch("https://auth.example.com/oauth/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      audience: "inventory-api",
    }),
    signal: AbortSignal.timeout(3000),
  });
  if (!res.ok) throw new Error(`token request failed: ${res.status}`);
  const body = await res.json();
  cached = {
    token: body.access_token,
    expiresAt: Date.now() + body.expires_in * 1000,
  };
  return cached.token;
}
```

Asking for a new token on every call puts heavy load on the identity provider and adds latency. Also make sure that many parallel requests do not all fetch a new token at the same time, for example by caching the pending promise.

## 189: How do you set up Pino logging for a microservice?

```js
import pino from "pino";

export const logger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  base: { service: "orders", version: process.env.APP_VERSION },
  redact: {
    paths: ["req.headers.authorization", "password", "*.cardNumber"],
    censor: "[redacted]",
  },
  timestamp: pino.stdTimeFunctions.isoTime,
});

const log = logger.child({ orderId: "o_123" });
log.info("payment started");
log.error({ err }, "payment failed");
```

Child loggers add fields to every line without repeating them. `redact` stops secrets and personal data from reaching logs. In development, pipe the output through `pino-pretty` instead of changing the code. With Express, `pino-http` logs every request with its duration and status.

## 190: What is AsyncLocalStorage and how is it used in microservices?

`AsyncLocalStorage` from `node:async_hooks` keeps a value available through all async calls started from one place, without passing it as an argument. It is used to keep per-request context like the request ID, user ID or tenant ID.

```js
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";

export const context = new AsyncLocalStorage();

app.use((req, res, next) => {
  const requestId = req.get("x-request-id") ?? randomUUID();
  res.set("x-request-id", requestId);
  context.run({ requestId }, next);
});

export function currentRequestId() {
  return context.getStore()?.requestId;
}
```

Any code deeper in the call chain, like a logger or HTTP client, can now read the request ID. OpenTelemetry uses the same mechanism internally to track the active span.

## 191: How do you propagate a correlation ID to other services?

Read it from the incoming request (or create one), store it in the request context, and add it to every outgoing call and published message.

```js
export async function callService(url, init = {}) {
  const headers = new Headers(init.headers);
  const requestId = currentRequestId();
  if (requestId) headers.set("x-request-id", requestId);
  return fetch(url, {
    ...init,
    headers,
    signal: init.signal ?? AbortSignal.timeout(2000),
  });
}

await producer.send({
  topic: "orders",
  messages: [
    { key, value, headers: { "x-request-id": currentRequestId() ?? "" } },
  ],
});
```

On the consumer side, read the header from the message and start a new context with it. If you use OpenTelemetry, its propagators do this for the `traceparent` header automatically for HTTP and many messaging libraries.

## 192: How do you set up OpenTelemetry in a Node.js service?

Create an instrumentation file and load it before the app with `--import`.

```js
// instrumentation.mjs
import { NodeSDK } from "@opentelemetry/sdk-node";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { resourceFromAttributes } from "@opentelemetry/resources";
import { ATTR_SERVICE_NAME } from "@opentelemetry/semantic-conventions";

const sdk = new NodeSDK({
  resource: resourceFromAttributes({ [ATTR_SERVICE_NAME]: "orders" }),
  traceExporter: new OTLPTraceExporter(),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
process.on("SIGTERM", () => sdk.shutdown());
```

```bash
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318 \
node --import ./instrumentation.mjs src/server.js
```

It must load first so that it can patch modules like `http`, `pg` and `express` before the app imports them. For ES modules, auto-instrumentation also needs the loader hook from `@opentelemetry/instrumentation/hook.mjs`, registered with `module.register()` at the top of the instrumentation file. Check the OpenTelemetry docs for the exact setup for your SDK version, since it has changed a few times. Usually the service sends data to an OpenTelemetry Collector, which forwards it to the tracing backend.

## 193: How do you create custom spans with OpenTelemetry?

```js
import { trace, SpanStatusCode } from "@opentelemetry/api";

const tracer = trace.getTracer("orders");

export async function calculatePrice(cart) {
  return tracer.startActiveSpan("calculatePrice", async (span) => {
    try {
      span.setAttribute("cart.items", cart.items.length);
      const price = await doPricing(cart);
      span.setAttribute("cart.total", price.total);
      return price;
    } catch (err) {
      span.recordException(err);
      span.setStatus({ code: SpanStatusCode.ERROR, message: err.message });
      throw err;
    } finally {
      span.end();
    }
  });
}
```

Auto-instrumentation covers HTTP and database calls. Add custom spans for important business steps that are not I/O, so traces show where the time actually goes. Always end spans, or they will not be exported.

## 194: What is trace sampling and why is it needed?

Recording every trace in a busy system is expensive in network, storage and money. Sampling keeps only some of them.

- **Head sampling:** the decision is made at the start of the trace, for example keep 10%. Cheap, but you may drop the one trace with the error.
- **Tail sampling:** the decision is made after the whole trace is complete, usually in the OpenTelemetry Collector. You can keep all errors and slow traces and only a small share of normal ones. It costs more, since the collector has to buffer spans.

```bash
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.1
```

`parentbased` means a service follows the sampling decision of the caller, so traces are not cut in the middle.

## 195: How do you measure HTTP request duration with prom-client?

```js
import client from "prom-client";

const httpDuration = new client.Histogram({
  name: "http_server_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route", "status"],
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
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
```

Use the route pattern (`/orders/:id`), not the real URL (`/orders/o_123`), as the label. Then in Prometheus you can compute p95 latency with `histogram_quantile(0.95, sum by (le, route) (rate(http_server_request_duration_seconds_bucket[5m])))`.

## 196: What is high cardinality in metrics and why is it a problem?

Cardinality is the number of unique label combinations for a metric. Each combination is a separate time series that Prometheus has to store.

Labels like `user_id`, `order_id`, full URLs or error messages can create millions of series. That uses a lot of memory, slows queries and can crash the monitoring system or raise the bill a lot.

Keep metric labels to small, fixed sets of values (method, route pattern, status code, service). Put high-cardinality details in logs and traces instead.

## 197: What should you alert on in a microservices system?

Alert on symptoms that users feel, not on every possible cause:

- Error rate above the SLO
- Latency (p95 or p99) above the target
- Availability of key user flows
- Consumer lag or queue depth growing for a long time
- Error budget burning too fast

Things like high CPU on one pod or a single restart are better shown on dashboards than sent as pages at night. Every alert should be actionable and link to a runbook. Too many noisy alerts make people ignore the real ones.

## 198: How do you write a multi-stage Dockerfile for a TypeScript service?

```dockerfile
# syntax=docker/dockerfile:1
FROM node:24-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

FROM deps AS build
COPY tsconfig.json ./
COPY src ./src
RUN npm run build

FROM node:24-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

The build stage has the compiler and dev dependencies. The final image only has production dependencies and compiled code, so it is smaller and has fewer packages that could contain vulnerabilities.

## 199: Which Node.js base image should you use for a service?

- **`node:24-alpine`:** small, uses musl libc. Some native modules may need extra work or behave a bit differently.
- **`node:24-slim`:** Debian based with glibc, bigger than Alpine but works with almost all native modules.
- **`node:24`:** full Debian image with build tools. Good for build stages, too big for runtime.
- **Distroless (`gcr.io/distroless/nodejs24-debian12`) or hardened images:** no shell or package manager, so the attack surface is very small, but debugging inside the container is harder.

Pin the major version at least, and rebuild regularly to pick up security patches.

## 200: Why does it matter which process is PID 1 in a container?

The first process in a container is PID 1, and Linux treats it specially: signals with no handler are ignored, and it is responsible for cleaning up zombie child processes.

If you start the service with `npm start` or a shell script, `npm` or `sh` becomes PID 1 and may not forward `SIGTERM` to Node. The container then ignores the stop request and gets killed after the grace period.

Fixes:

- Use `CMD ["node", "server.js"]` in exec form.
- Run with a tiny init like `tini`, or `docker run --init`.
- If you use a shell script, end it with `exec node server.js`.

## 201: How does Node.js handle memory limits in containers?

V8 sets the default heap limit based on the memory available. Newer Node versions read the container's cgroup memory limit, but the default heap is still only a part of that limit, and the process also uses memory outside the heap (buffers, native code, thread stacks).

You can set the limit yourself:

```bash
node --max-old-space-size=768 server.js
```

Recent Node.js releases also added `--max-old-space-size-percentage`, which sets the heap as a percentage of available memory. Check that your Node version supports it before relying on it.

Leave room for non-heap memory, roughly 25% of the container limit. If the heap limit is higher than the container limit, the kernel kills the container with an OOM error before V8 can collect garbage or log a heap error.

## 202: How should you set CPU and memory requests and limits for Node.js pods?

- **Memory:** set request and limit to the same or similar value, a bit above normal peak use, and align `--max-old-space-size` with it.
- **CPU request:** what the service needs under normal load. The scheduler uses it to place pods.
- **CPU limit:** many teams do not set one or set it high, because CPU throttling causes latency spikes. If you do set it, monitor throttling metrics.

A single Node.js process mostly uses one core for JavaScript, plus some threads for GC and libuv. Giving a pod 4 CPUs rarely helps, it is better to run more pods with about 1 CPU each.

## 203: How do you validate configuration at startup?

Parse the environment with a schema and fail fast with a clear message:

```js
import { z } from "zod";

const Env = z.object({
  NODE_ENV: z
    .enum(["development", "test", "production"])
    .default("development"),
  PORT: z.coerce.number().int().default(3000),
  DATABASE_URL: z.string().url(),
  KAFKA_BROKERS: z.string().transform((s) => s.split(",")),
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]).default("info"),
});

const parsed = Env.safeParse(process.env);
if (!parsed.success) {
  console.error("Invalid configuration", parsed.error.flatten().fieldErrors);
  process.exit(1);
}

export const config = parsed.data;
```

The rest of the code imports `config` instead of reading `process.env` directly. This gives you types, defaults and one place to see every setting the service uses.

## 204: How do you validate request bodies in an Express service?

```js
import express from "express";
import { z } from "zod";

const CreateOrder = z.object({
  userId: z.string().min(1),
  items: z
    .array(
      z.object({
        sku: z.string(),
        quantity: z.number().int().positive(),
      }),
    )
    .min(1),
});

const validate = (schema) => (req, res, next) => {
  const result = schema.safeParse(req.body);
  if (!result.success) {
    return res
      .status(400)
      .json({ title: "Invalid request", errors: result.error.issues });
  }
  req.body = result.data;
  next();
};

app.post(
  "/orders",
  express.json({ limit: "100kb" }),
  validate(CreateOrder),
  async (req, res) => {
    const order = await createOrder(req.body);
    res.status(201).json(order);
  },
);
```

Validate at the edge of each service, keep the parsed result and work only with it. Also set a body size limit, so a huge payload cannot use up memory.

## 205: How does error handling work with async routes in Express 5?

In Express 4, if an `async` route handler threw or returned a rejected promise, Express did not catch it. You needed `try/catch` with `next(err)` or a wrapper package.

Express 5 handles this for you: rejected promises from handlers and middleware are passed to the error handler automatically.

```js
app.get("/orders/:id", async (req, res) => {
  const order = await ordersRepo.find(req.params.id); // if this throws, Express 5 calls the error handler
  if (!order) return res.sendStatus(404);
  res.json(order);
});

app.use((err, req, res, next) => {
  req.log?.error({ err }, "request failed");
  res
    .status(err.status ?? 500)
    .json({ title: err.expose ? err.message : "Internal Server Error" });
});
```

Express 5 also changed path matching syntax (for example `/*splat` instead of `/*`) and removed some old methods, so check the migration guide when upgrading.

## 206: How do you design error handling across services?

- Define a small set of error classes (`NotFoundError`, `ValidationError`, `ConflictError`) with an HTTP status attached.
- Map them to a consistent response format, such as Problem Details, in one error handler.
- Translate errors from downstream services instead of passing them through as is. A `404` from the inventory service may mean a `409` or `422` for your own API.
- Return `502`, `503` or `504` when the problem is a downstream service, so callers know it is not their fault.
- Log the full error with the trace ID on the server, and return a safe message to the client.

```js
class AppError extends Error {
  constructor(status, title, detail) {
    super(detail ?? title);
    this.status = status;
    this.title = title;
    this.expose = status < 500;
  }
}
```

## 207: How should a service handle unhandledRejection and uncaughtException?

Since Node 15, an unhandled promise rejection crashes the process by default, the same as an uncaught exception. That is usually the right behaviour: after an unexpected error, the process may be in a broken state.

```js
process.on("uncaughtException", (err) => {
  logger.fatal({ err }, "uncaught exception");
  process.exit(1);
});

process.on("unhandledRejection", (reason) => {
  logger.fatal({ err: reason }, "unhandled rejection");
  process.exit(1);
});
```

Log the error, then exit and let Kubernetes or your process manager start a fresh instance. Do not try to keep the process running as if nothing happened. If you can, try a short graceful shutdown before exiting so in-flight requests on that instance get a chance to finish.

## 208: How do you change an event schema without breaking consumers?

- Only make backward compatible changes to an existing event type: add optional fields, do not remove or rename fields and do not change types.
- Include a `version` in each event.
- For a breaking change, publish a new version (`order.created.v2`) alongside the old one for a while, let consumers move over, then stop publishing the old one.
- Consumers should ignore fields they do not know about.
- Use a schema registry and compatibility checks in CI to catch breaking changes before they ship.

Remember that Kafka may keep old events for days or forever. Consumers that replay history must still understand the old versions.

## 209: What is the tolerant reader pattern?

The tolerant reader pattern means a consumer reads only the fields it needs and ignores everything else. It does not fail if extra fields appear or if fields it does not use change.

```js
// tolerant: pick what you need, ignore the rest
const { orderId, total } = event.data;

// fragile: strict schema that rejects unknown fields
const Order = z.object({ orderId: z.string(), total: z.number() }).strict();
```

This lets providers add fields without coordinating with every consumer. It is one of the simplest ways to reduce coupling between services.

## 210: What is a schema registry?

A schema registry is a service that stores the schemas (Avro, Protobuf or JSON Schema) for the messages on your topics. Producers register the schema and put a small schema ID in each message. Consumers use the ID to fetch the right schema and decode the message.

It also checks compatibility rules. For example, with backward compatibility, a new schema version must be readable by consumers using the previous one. Confluent Schema Registry, Apicurio and AWS Glue Schema Registry are common. In Node.js, `@kafkajs/confluent-schema-registry` and Confluent's own schema registry client are used to encode and decode messages.

## 211: What does a consumer-driven contract test with Pact look like?

On the consumer side, you describe the interaction and test your client against a mock provider:

```js
import { PactV3, MatchersV3 } from "@pact-foundation/pact";

const provider = new PactV3({
  consumer: "web-bff",
  provider: "orders-service",
});

it("gets an order", async () => {
  provider
    .given("order o_123 exists")
    .uponReceiving("a request for order o_123")
    .withRequest({ method: "GET", path: "/orders/o_123" })
    .willRespondWith({
      status: 200,
      body: {
        id: "o_123",
        status: MatchersV3.string("paid"),
        total: MatchersV3.integer(4999),
      },
    });

  await provider.executeTest(async (mockServer) => {
    const order = await getOrder(mockServer.url, "o_123");
    expect(order.id).toBe("o_123");
  });
});
```

This produces a contract file that is published to a Pact Broker. The orders service then verifies it against its real API in CI, setting up the `order o_123 exists` state first. `can-i-deploy` checks tell you whether a version is safe to release.

## 212: How do you integration test a Kafka consumer?

Start a real Kafka with Testcontainers, produce a message and check the result:

```js
import { KafkaContainer } from "@testcontainers/kafka";
import { Kafka } from "kafkajs";

let container, kafka;

beforeAll(async () => {
  container = await new KafkaContainer("confluentinc/cp-kafka:7.7.0")
    .withKraft()
    .start();
  kafka = new Kafka({
    brokers: [`${container.getHost()}:${container.getMappedPort(9093)}`],
  });
}, 120_000);

afterAll(() => container.stop());

it("reserves stock when an order is created", async () => {
  await startConsumer(kafka);
  const producer = kafka.producer();
  await producer.connect();
  await producer.send({
    topic: "orders",
    messages: [{ key: "o_1", value: JSON.stringify(orderCreated) }],
  });

  await waitFor(async () => expect(await stockRepo.reserved("sku_1")).toBe(2));
});
```

Since processing is async, use a polling helper like `waitFor` with a timeout instead of fixed `sleep` calls.

## 213: How do you mock other services in unit and component tests?

- **undici `MockAgent`:** intercepts the built-in `fetch` and undici requests.
- **MSW (Mock Service Worker):** defines request handlers that work in Node and the browser.
- **nock:** a long-standing library for intercepting `http` requests. Newer versions also support `fetch`.
- **WireMock or Pact stub servers:** run a real fake HTTP server, useful for component tests in Docker.

```js
import { MockAgent, setGlobalDispatcher } from "undici";

const agent = new MockAgent();
agent.disableNetConnect();
setGlobalDispatcher(agent);

agent
  .get("http://users:3000")
  .intercept({ path: "/users/42", method: "GET" })
  .reply(200, { id: "42", name: "Ana" });
```

Mocks only prove your code works with what you think the other service returns. Pair them with contract tests so the mocks stay honest.

## 214: How do you implement cache-aside with Redis?

In cache-aside, the service checks the cache first. On a miss, it loads from the source and stores the result.

```js
export async function getProduct(id) {
  const key = `product:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const product = await db.products.findById(id);
  if (product) {
    await redis.set(key, JSON.stringify(product), "EX", 300);
  }
  return product;
}

export async function updateProduct(id, changes) {
  const product = await db.products.update(id, changes);
  await redis.del(`product:${id}`);
  return product;
}
```

Always set a TTL, so stale entries eventually go away even if an invalidation is missed. If Redis is down, fall back to the database instead of failing the request.

## 215: How do you invalidate caches across services?

- **TTL only:** simplest, accept that data can be stale for up to the TTL.
- **Delete on write:** the owning service deletes the key when it changes the data.
- **Event-based:** the owning service publishes `ProductUpdated`, and every service that caches products removes or updates its copy.
- **Versioned keys:** include a version in the key (`product:42:v7`), so a new version means a new key.

With in-memory caches on many instances, a delete in one instance does not clear the others, so you need events (often Redis pub/sub) to tell all instances, or you keep TTLs short.

## 216: What is a cache stampede and how do you prevent it?

A cache stampede happens when a popular key expires and many requests miss the cache at the same moment. They all hit the database together, which can overload it.

Ways to prevent it:

- **Request coalescing:** inside one process, share one pending promise for the same key.
- **Locking:** only one caller rebuilds the value (using `SET key NX PX`), others wait or use the old value.
- **Stale-while-revalidate:** keep serving the old value while one caller refreshes it in the background.
- **TTL jitter:** add a random amount to TTLs so many keys do not expire at once.

```js
const inflight = new Map();

export function getOnce(key, load) {
  if (!inflight.has(key)) {
    inflight.set(
      key,
      load().finally(() => inflight.delete(key)),
    );
  }
  return inflight.get(key);
}
```

## 217: Can services use HTTP caching between each other?

Yes. A service can return `Cache-Control`, `ETag` and `Last-Modified` headers, and callers or proxies can use them.

```js
app.get("/products/:id", async (req, res) => {
  const product = await getProduct(req.params.id);
  res.set("Cache-Control", "max-age=60");
  res.set("ETag", `"${product.version}"`);
  if (req.get("if-none-match") === `"${product.version}"`)
    return res.sendStatus(304);
  res.json(product);
});
```

The caller sends `If-None-Match` on the next request and gets a small `304 Not Modified` if nothing changed. Note that Node's built-in `fetch` does not cache by default. You need a caching layer like undici's cache interceptor, a proxy, or your own cache to benefit from `max-age`.

## 218: How do you implement a simple distributed lock with Redis?

```js
import { randomUUID } from "node:crypto";

export async function withLock(redis, key, ttlMs, fn) {
  const token = randomUUID();
  const ok = await redis.set(key, token, "PX", ttlMs, "NX");
  if (ok !== "OK") return false; // someone else holds the lock

  try {
    await fn();
    return true;
  } finally {
    // delete only if we still own the lock
    await redis.eval(
      "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",
      1,
      key,
      token,
    );
  }
}
```

The random token makes sure a process does not delete a lock that expired and was taken by someone else. This lock is fine for avoiding duplicate work, like running a job once. It is not safe for correctness-critical cases, since a pause longer than the TTL can let two processes hold it. For those, use fencing tokens or a database constraint.

## 219: How do you handle database migrations in microservices?

- Each service owns its migrations and runs them against its own database only.
- Run migrations as a separate step before the new version starts, for example a Kubernetes Job or an init container, not inside every app instance at startup (or use a lock if you do).
- Keep migrations backward compatible, because old and new versions run together during a rolling deploy.
- Version and test them in CI like normal code.

Common tools in Node.js: Prisma Migrate, Drizzle Kit, Knex migrations, node-pg-migrate, TypeORM migrations, and Flyway or Liquibase if you prefer SQL-first tools.

## 220: What is the expand and contract pattern for schema changes?

It is a way to make breaking schema changes without downtime by splitting them into safe steps. For example, renaming `name` to `full_name`:

1. **Expand:** add the new `full_name` column. Deploy code that writes to both columns and reads from the old one.
2. **Migrate:** backfill `full_name` for old rows.
3. **Switch:** deploy code that reads from `full_name` (still writing both).
4. **Contract:** deploy code that stops writing `name`, then drop the `name` column.

Each step works with the version before and after it, so rolling deployments and rollbacks are safe. The same idea applies to API fields and event schemas.

## 221: How do you query data that lives in several services?

Options, from simple to more involved:

1. **API composition:** call each service and merge results. Good for simple pages.
2. **Data duplication:** a service keeps a local copy of the fields it needs, updated by events.
3. **CQRS read model:** a dedicated query service listens to events from several services and builds a view designed for the query.
4. **Analytics store:** for reporting, stream all data into a data warehouse (BigQuery, Snowflake, ClickHouse) and query it there.

Avoid letting one service query another service's database directly, even read-only. It creates hidden coupling.

## 222: How do you handle partial failures when combining responses?

Use `Promise.allSettled` so one failing call does not fail the whole response, and decide which parts are required.

```js
const [product, reviews, recs] = await Promise.allSettled([
  catalog.getProduct(id),
  reviewsClient.list(id),
  recsClient.forProduct(id),
]);

if (product.status === "rejected") {
  throw product.reason; // product is required
}

res.json({
  ...product.value,
  reviews: reviews.status === "fulfilled" ? reviews.value : null,
  recommendations: recs.status === "fulfilled" ? recs.value : [],
  partial: reviews.status === "rejected" || recs.status === "rejected",
});
```

Give optional calls short timeouts, so a slow recommendation service does not make the whole page slow.

## 223: How is GraphQL used in a microservices architecture?

GraphQL is often used at the edge as a single API that clients query. Two common setups:

- **A GraphQL BFF or gateway:** one GraphQL server whose resolvers call REST or gRPC services underneath.
- **Federation:** each service exposes its own GraphQL subgraph, and a router combines them into one supergraph.

GraphQL lets clients ask for exactly the fields they need in one request, which works well for UIs that need data from many services. The downsides are harder caching, the risk of expensive queries (you need depth and cost limits) and the N+1 problem in resolvers.

## 224: What is GraphQL Federation?

Federation lets several teams each own a part of one GraphQL schema. Each service runs a **subgraph** with its own types and fields. A **router** (Apollo Router, Cosmo Router, Hive Gateway) builds the combined schema and splits each client query into calls to the right subgraphs.

```graphql
# users subgraph
type User @key(fields: "id") {
  id: ID!
  name: String!
}

# orders subgraph adds a field to User
type User @key(fields: "id") {
  id: ID!
  orders: [Order!]!
}
```

The `@key` directive tells the router how to join `User` across subgraphs. In Node.js, subgraphs are commonly built with `@apollo/subgraph` and Apollo Server, or with GraphQL Yoga.

## 225: How do you decide between REST, gRPC and messaging for a new interaction?

Ask a few questions:

1. **Does the caller need an answer now to continue?** If no, use messaging.
2. **Do several services need to react?** If yes, publish an event.
3. **Is it called by browsers or third parties?** Use REST (or GraphQL).
4. **Is it a high-volume internal call with a strict contract?** gRPC is a good fit.
5. **Is it long-running work?** Accept the request with `202 Accepted` and process it from a queue.

There is no single right answer for the whole system. Pick per interaction, but keep the number of different technologies small so teams can support them.

## 226: How do you run HTTP and a message consumer in the same NestJS app?

NestJS supports hybrid applications, where one app serves HTTP and also listens on one or more microservice transports.

```ts
import { NestFactory } from "@nestjs/core";
import { Transport, MicroserviceOptions } from "@nestjs/microservices";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.connectMicroservice<MicroserviceOptions>({
    transport: Transport.RMQ,
    options: {
      urls: [process.env.AMQP_URL],
      queue: "orders_queue",
      queueOptions: { durable: true },
      noAck: false,
    },
  });

  app.enableShutdownHooks();
  await app.startAllMicroservices();
  await app.listen(3000);
}
bootstrap();
```

With `noAck: false`, you ack messages yourself through the `RmqContext` in the handler. `enableShutdownHooks()` makes Nest run lifecycle hooks like `onModuleDestroy` on `SIGTERM`.

## 227: What is the difference between send and emit in a NestJS ClientProxy?

- `client.send(pattern, data)` is request-response. It returns an Observable that gives you the handler's reply. It is handled by `@MessagePattern` on the other side.
- `client.emit(pattern, data)` is fire-and-forget. It publishes an event and does not wait for a result. It is handled by `@EventPattern`.

```ts
import { firstValueFrom } from "rxjs";

const order = await firstValueFrom(
  this.ordersClient.send("get_order", id).pipe(timeout(2000)),
);

this.ordersClient.emit("order_viewed", { id, userId });
```

`send` is lazy: nothing is sent until you subscribe, for example with `firstValueFrom`. Always add a `timeout` operator, since by default it can wait a long time.

## 228: How do you use Kafka with NestJS?

```ts
app.connectMicroservice<MicroserviceOptions>({
  transport: Transport.KAFKA,
  options: {
    client: { clientId: "inventory", brokers: ["kafka:9092"] },
    consumer: { groupId: "inventory-consumer" },
  },
});
```

```ts
@Controller()
export class InventoryController {
  @EventPattern("orders.created")
  async onOrderCreated(
    @Payload() order: OrderCreated,
    @Ctx() ctx: KafkaContext,
  ) {
    await this.inventory.reserve(order);
  }
}
```

The Nest Kafka transport is built on kafkajs. It is convenient for simple cases. For fine control over commits, batching and pausing partitions, some teams use kafkajs or the Confluent client directly inside a Nest provider.

## 229: What is Moleculer?

Moleculer is a Node.js framework built specifically for microservices. Services are defined as objects with actions and event handlers, and a **service broker** takes care of discovery, load balancing, retries, circuit breakers, caching and transport.

```js
import { ServiceBroker } from "moleculer";

const broker = new ServiceBroker({ transporter: "nats://nats:4222" });

broker.createService({
  name: "math",
  actions: {
    add(ctx) {
      return ctx.params.a + ctx.params.b;
    },
  },
});

await broker.start();
const sum = await broker.call("math.add", { a: 2, b: 3 });
```

It gives you a lot out of the box, but it also ties all your services to the framework, so it fits best when the whole system is in Node.js.

## 230: How do you organize a Node.js microservices monorepo?

A common layout with pnpm (or npm) workspaces:

```text
apps/
  orders/
  payments/
  gateway/
packages/
  logger/
  tracing/
  contracts/      # OpenAPI, protobuf, event schemas
  eslint-config/
pnpm-workspace.yaml
```

```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"
```

Tools like Nx or Turborepo know the dependency graph, so CI can run only `affected` builds and tests and cache results. Set lint rules that stop one app from importing another app's code directly, only shared packages.

## 231: How do you share API contracts between services?

- Keep the contract as the source of truth: an OpenAPI file, `.proto` files or event schemas, stored in a `contracts` package or repo.
- Generate typed clients and types from it, for example with `openapi-typescript` for REST, `ts-proto` or Buf for gRPC.
- Version the contract package with semver.
- Run checks in CI that compare a contract change with the previous version and fail on breaking changes (for example `buf breaking` or OpenAPI diff tools).

This is better than copying TypeScript interfaces between services by hand, which drift apart over time.

## 232: How do you set up CI to build only the services that changed?

In a monorepo, compute which projects are affected by the commit and run jobs only for those.

```bash
# Nx
npx nx affected -t lint test build --base=origin/main

# Turborepo
npx turbo run test build --filter='...[origin/main]'
```

In GitHub Actions without these tools, you can use path filters so a workflow only runs when files in its folder or in shared packages change. Remember that a change to a shared package affects every service that depends on it.

## 233: How should you tag Docker images for microservices?

Use an immutable tag that points to the exact source code, usually the Git commit SHA, optionally with a semantic version.

```bash
docker build -t registry.example.com/orders:3f9c2a1 -t registry.example.com/orders:1.8.0 .
```

Avoid deploying `latest`. It changes over time, so you cannot tell which code is running or roll back reliably. For extra safety, deploy by image digest (`orders@sha256:...`), which can never change.

## 234: What does a basic Kubernetes Deployment for a Node.js service look like?

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders
spec:
  replicas: 3
  selector:
    matchLabels: { app: orders }
  template:
    metadata:
      labels: { app: orders }
    spec:
      terminationGracePeriodSeconds: 30
      containers:
        - name: orders
          image: registry.example.com/orders:3f9c2a1
          ports:
            - containerPort: 3000
          envFrom:
            - configMapRef: { name: orders-config }
            - secretRef: { name: orders-secrets }
          resources:
            requests: { cpu: 250m, memory: 512Mi }
            limits: { memory: 512Mi }
          readinessProbe:
            httpGet: { path: /readyz, port: 3000 }
          livenessProbe:
            httpGet: { path: /livez, port: 3000 }
```

## 235: How do services find each other in Kubernetes?

A Kubernetes **Service** gives a stable name and virtual IP to a set of pods selected by labels.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: orders
spec:
  selector: { app: orders }
  ports:
    - port: 80
      targetPort: 3000
```

Other pods in the same namespace can call `http://orders`. From another namespace, use `http://orders.<namespace>` or the full name `orders.<namespace>.svc.cluster.local`. Cluster DNS resolves the name and kube-proxy (or the CNI) spreads connections over the ready pods.

## 236: How do you pass ConfigMaps and Secrets to a Node.js service?

As environment variables:

```yaml
envFrom:
  - configMapRef: { name: orders-config }
env:
  - name: DATABASE_PASSWORD
    valueFrom:
      secretKeyRef: { name: orders-db, key: password }
```

Or as files in a mounted volume:

```yaml
volumeMounts:
  - name: db-secret
    mountPath: /etc/secrets
    readOnly: true
volumes:
  - name: db-secret
    secret: { secretName: orders-db }
```

```js
import { readFile } from "node:fs/promises";
const password = (await readFile("/etc/secrets/password", "utf8")).trim();
```

Environment variables are read once at startup. Mounted files are updated when the Secret changes, so a service that reads them again can pick up rotated values without a restart.

## 237: What is the difference between an Ingress and the Gateway API in Kubernetes?

Both expose HTTP services from the cluster to the outside.

**Ingress** is the older API. It is simple but limited, and many features depend on controller-specific annotations. The popular community ingress-nginx controller has been retired, which pushed many teams to look at alternatives.

**Gateway API** is the newer, more expressive standard. It splits responsibilities into `GatewayClass`, `Gateway` (owned by the platform team) and `HTTPRoute` or `GRPCRoute` (owned by app teams). It supports header matching, traffic splitting for canaries and more, without annotations.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: orders
spec:
  parentRefs: [{ name: public-gateway }]
  rules:
    - matches: [{ path: { type: PathPrefix, value: /api/orders } }]
      backendRefs: [{ name: orders, port: 80 }]
```

## 238: What is Helm and why is it used for microservices?

Helm is a package manager for Kubernetes. A **chart** is a set of templated Kubernetes manifests plus a `values.yaml` file with settings. You install or upgrade a release with one command and can roll it back.

With many similar Node.js services, teams often build one shared chart for "a standard web service" and give each service its own values file (image, replicas, env, resources). Alternatives are Kustomize (overlays without templates) and GitOps tools like Argo CD or Flux that apply manifests from Git.

## 239: How do you control a rolling update in Kubernetes?

```yaml
spec:
  replicas: 6
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2 # up to 2 extra pods during the update
      maxUnavailable: 0 # never go below 6 ready pods
  minReadySeconds: 10
```

`maxUnavailable: 0` with a positive `maxSurge` keeps full capacity during deploys. `minReadySeconds` waits a bit after a pod is ready before counting it as available, which catches pods that crash shortly after startup. If new pods never become ready, the rollout stops, and you can undo it with `kubectl rollout undo deployment/orders`.

## 240: What is a PodDisruptionBudget?

A PodDisruptionBudget (PDB) limits how many pods of a service can be down at the same time because of voluntary disruptions, like node upgrades or the cluster autoscaler removing a node.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders
spec:
  minAvailable: 2
  selector:
    matchLabels: { app: orders }
```

Without it, draining nodes during maintenance could stop all replicas of a service at once. It does not protect against crashes or node failures, only planned evictions.

## 241: How do you run batch jobs and scheduled tasks in Kubernetes?

Use a **Job** for one-off work, like a migration or a data backfill, and a **CronJob** for scheduled work.

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: cleanup-expired-carts
spec:
  schedule: "0 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 2
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: cleanup
              image: registry.example.com/carts:3f9c2a1
              command: ["node", "dist/jobs/cleanup.js"]
```

`concurrencyPolicy: Forbid` stops a new run from starting while the previous one is still running. The job script must exit when it is done, so close all connections at the end.

## 242: How do you make sure a scheduled task runs only once when you have many instances?

If you use `setInterval` or `node-cron` inside a service with 5 replicas, the task runs 5 times. Options:

- Move it out of the service into a Kubernetes CronJob or a cloud scheduler.
- Use a job queue with repeatable jobs, like BullMQ's job schedulers, which create one job per run no matter how many workers there are.
- Use a distributed lock so only the instance that gets the lock runs the task.
- Use leader election so one instance is responsible for all scheduled tasks.

Whatever you choose, make the task idempotent, because a retry or overlap can still make it run twice.

## 243: What is leader election?

Leader election is a way for several instances of a service to agree that one of them is the leader. The leader does work that must not run in parallel, like scheduled tasks or managing partitions. If the leader dies, another instance takes over.

It is usually done with a lease in a shared store: a Kubernetes `Lease` object, an etcd or Consul key, or a Redis key with a TTL. The leader keeps renewing the lease. If it stops renewing, the lease expires and another instance can take it. Because of pauses and clock issues, there can be a short time when two instances think they are the leader, so the work should still be safe to repeat.

## 244: How do you detect event loop blocking in a Node.js service?

Measure event loop delay with `perf_hooks`:

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  logger.info(
    {
      p50: h.percentile(50) / 1e6,
      p99: h.percentile(99) / 1e6,
      max: h.max / 1e6,
    },
    "event loop delay ms",
  );
  h.reset();
}, 10_000).unref();
```

`prom-client`'s default metrics also export event loop lag. If delay goes up, find the cause with a CPU profile (`node --cpu-prof`, Chrome DevTools or a continuous profiler). Common causes are large `JSON.parse` or `JSON.stringify` calls, sync crypto or file system calls, heavy regex and big loops over arrays.

## 245: When and how do you use worker threads in a microservice?

Use worker threads when a service has CPU-heavy work that would block the event loop, like image processing, PDF generation, compression or heavy calculations.

```js
// main.js
import { Worker } from "node:worker_threads";

export function resizeImage(buffer) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(new URL("./resize-worker.js", import.meta.url), {
      workerData: buffer,
    });
    worker.once("message", resolve);
    worker.once("error", reject);
  });
}
```

```js
// resize-worker.js
import { parentPort, workerData } from "node:worker_threads";
parentPort.postMessage(doHeavyResize(workerData));
```

Creating a worker per task is slow, so use a pool such as `piscina` in real code. If the CPU work is large or bursty, a separate service that takes jobs from a queue is often a cleaner choice.

## 246: How do you stream large data between services?

Do not load large payloads fully into memory. Stream them with `pipeline`, which also handles errors and backpressure.

```js
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";

app.get("/exports/:id", async (req, res) => {
  const upstream = await fetch(
    `http://reports:3000/reports/${req.params.id}.csv`,
  );
  if (!upstream.ok) return res.sendStatus(502);
  res.set("content-type", "text/csv");
  await pipeline(Readable.fromWeb(upstream.body), res);
});
```

For large records, use formats that can be streamed, like NDJSON (one JSON object per line) or CSV, instead of one huge JSON array. gRPC server streaming is another good option between internal services.

## 247: How do you handle file uploads in a microservices system?

Avoid sending large files through several services. A common approach with object storage (S3, GCS, Azure Blob):

1. The client asks the upload service for a pre-signed upload URL.
2. The client uploads the file directly to storage using that URL.
3. Storage sends an event (or the client calls back) when the upload is done.
4. Other services get the file's key in an event and fetch it from storage when needed.

```js
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({});
const url = await getSignedUrl(
  s3,
  new PutObjectCommand({
    Bucket: "uploads",
    Key: `avatars/${userId}.png`,
    ContentType: "image/png",
  }),
  { expiresIn: 300 },
);
```

This keeps big files off your Node.js processes and makes uploads faster for users.

## 248: Why should every service set request size limits?

Without limits, a client (or a buggy service) can send a very large body that uses up memory, blocks the event loop while parsing or fills the disk.

```js
app.use(express.json({ limit: "1mb" }));
```

```js
const app = Fastify({ bodyLimit: 1_048_576 });
```

Also limit header size (Node has `--max-http-header-size`, 16 KB by default), the number of items in arrays and string lengths in your validation schemas. Set limits at the gateway too, so huge requests are rejected before they reach the services.

## 249: How do you verify webhook signatures in Node.js?

Most providers sign the raw body with HMAC SHA-256. Compute the signature yourself and compare in constant time.

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

    const a = Buffer.from(signature, "hex");
    const b = Buffer.from(expected, "hex");
    if (a.length !== b.length || !timingSafeEqual(a, b)) {
      return res.sendStatus(401);
    }

    const event = JSON.parse(req.body.toString("utf8"));
    // store and enqueue, then answer quickly
    res.sendStatus(200);
  },
);
```

Use the raw body, not the parsed JSON, because re-serializing changes bytes and breaks the signature. Also check the timestamp in the signed data if the provider sends one, to block replays of old requests.

## 250: How do you process incoming webhooks reliably?

1. Verify the signature.
2. Store the raw event in your database with its provider event ID as a unique key.
3. Respond with `200` right away.
4. Process the stored event asynchronously from a queue or outbox.
5. Skip events whose ID you have already processed.

This keeps your response fast, so the provider does not time out and retry. It also means you do not lose events if your processing code has a bug: you can fix it and replay them. Do not assume events arrive in order. Use timestamps or fetch the latest state from the provider's API if order matters.

## 251: How would you design a notification service?

A notification service sends emails, SMS, push and in-app messages for the rest of the system. A common design:

- Other services publish domain events (`OrderShipped`, `PasswordResetRequested`) or send a `SendNotification` command to a queue.
- The notification service decides which channels to use based on user preferences it stores itself.
- It renders templates, then calls providers (SES, SendGrid, Twilio, FCM) through a per-channel queue with retries and rate limits.
- It stores a log of what was sent, with a deduplication key, so a repeated event does not send the same email twice.
- A dead letter queue catches messages that keep failing.

Keeping provider details in one place means you can switch email providers without touching other services.

## 252: How do you keep a search index in sync with other services?

Build a search indexer that listens to events and updates Elasticsearch or OpenSearch.

```js
await consumer.run({
  eachMessage: async ({ message }) => {
    const event = JSON.parse(message.value.toString());
    if (event.type === "product.deleted") {
      await es.delete(
        { index: "products", id: event.data.id },
        { ignore: [404] },
      );
      return;
    }
    await es.index({
      index: "products",
      id: event.data.id,
      document: toSearchDoc(event.data),
      version: event.data.version,
      version_type: "external",
    });
  },
});
```

Using the entity's version with `version_type: 'external'` makes the index ignore older updates that arrive late. Keep a way to rebuild the whole index from the source of truth, because sooner or later you will need it after a mapping change or a bug.

## 253: How do you pass tenant context through a multi-tenant system?

- Get the tenant ID from a trusted place, usually a claim in the JWT, not from a header the client can set freely.
- Store it in the request context (`AsyncLocalStorage`) together with the request ID.
- Send it to downstream services in the token or a header, and include it in every event.
- Every data access must filter by tenant. Many teams enforce this in the repository layer or with PostgreSQL row-level security, so a missing `WHERE tenant_id = ...` cannot leak data.
- Add the tenant ID to logs and traces, and include it in cache keys.

## 254: How do you delete a user's data across all services (for example for GDPR)?

1. The user service (the owner) receives the deletion request and marks the user as deleted.
2. It publishes a `UserDeletionRequested` event.
3. Every service that holds personal data about that user deletes or anonymizes it and publishes `UserDataDeleted` with its service name.
4. A tracker (often in the user service) waits until all expected services confirm, and alerts if one does not.

Also think about data outside databases: logs, backups, search indexes, analytics stores and events kept in Kafka. Some teams avoid putting personal data in long-lived events, or encrypt it with a per-user key that they delete ("crypto shredding").

## 255: How do you implement idempotency keys in an Express service?

Store the key with the result. Use an atomic "set if not exists" to handle two requests with the same key arriving at the same time.

```js
export function idempotent({ ttlSeconds = 86_400 } = {}) {
  return async (req, res, next) => {
    const key = req.get("idempotency-key");
    if (!key)
      return res
        .status(400)
        .json({ title: "Idempotency-Key header is required" });

    const redisKey = `idem:${req.user.sub}:${key}`;
    const created = await redis.set(
      redisKey,
      JSON.stringify({ state: "pending" }),
      "EX",
      ttlSeconds,
      "NX",
    );

    if (!created) {
      const saved = JSON.parse(await redis.get(redisKey));
      if (saved.state === "pending")
        return res.status(409).json({ title: "Request in progress" });
      return res.status(saved.status).json(saved.body);
    }

    const originalJson = res.json.bind(res);
    res.json = (body) => {
      redis
        .set(
          redisKey,
          JSON.stringify({ state: "done", status: res.statusCode, body }),
          "EX",
          ttlSeconds,
        )
        .catch((err) =>
          req.log?.error({ err }, "failed to save idempotent response"),
        );
      return originalJson(body);
    };
    next();
  };
}

app.post("/payments", idempotent(), createPaymentHandler);
```

Scope keys per user or client so one caller cannot read another's response. Some implementations also store a hash of the request body and reject the same key with a different body. If the handler fails with a `5xx`, delete the key so the client can retry.

## 256: What is optimistic concurrency control?

Optimistic concurrency lets many writers try to update a record and detects conflicts instead of locking. Each record has a `version` number. An update only succeeds if the version has not changed since it was read.

```js
const { rowCount } = await db.query(
  `UPDATE orders SET status = $1, version = version + 1
   WHERE id = $2 AND version = $3`,
  [newStatus, orderId, expectedVersion],
);

if (rowCount === 0) {
  throw new ConflictError("order was changed by someone else");
}
```

The caller can then reload and try again, or show an error. It works well in microservices because no locks are held across network calls.

## 257: How do you use ETag and If-Match to prevent lost updates in an API?

The server returns the current version as an `ETag`. The client sends it back in `If-Match` when updating. If the resource changed in between, the server answers `412 Precondition Failed`.

```js
app.get("/orders/:id", async (req, res) => {
  const order = await repo.find(req.params.id);
  res.set("ETag", `"${order.version}"`).json(order);
});

app.patch("/orders/:id", async (req, res) => {
  const ifMatch = req.get("if-match");
  if (!ifMatch) return res.sendStatus(428); // Precondition Required
  const version = Number(ifMatch.replaceAll('"', ""));
  const updated = await repo.updateIfVersion(req.params.id, req.body, version);
  if (!updated) return res.sendStatus(412);
  res.set("ETag", `"${updated.version}"`).json(updated);
});
```

This is optimistic concurrency exposed over HTTP. It stops two clients from overwriting each other's changes without knowing.

## 258: Why should services offer bulk endpoints?

If a service needs data for 100 products and the product service only has `GET /products/:id`, it has to make 100 calls. That means more latency, more connections and more load.

A bulk endpoint fixes this:

```http
GET /products?ids=p_1,p_2,p_3
POST /products/batch-get
{ "ids": ["p_1", "p_2", "p_3"] }
```

Set a maximum batch size, and decide how to report items that were not found (leave them out, return `null`, or list them in a separate field).

## 259: What is the N+1 problem between services and how do you fix it?

It is the same problem as N+1 database queries, but over the network: you fetch a list (1 call) and then make one call per item (N calls). For example, fetching 50 orders and then calling the user service 50 times to get each customer's name.

Fixes:

- Collect the IDs and use a bulk endpoint.
- Use a batching helper like `dataloader`, which groups calls made in the same tick into one batch. This is common in GraphQL resolvers.
- Store the needed data locally (the customer name in the order).

```js
import DataLoader from "dataloader";

const userLoader = new DataLoader(async (ids) => {
  const users = await usersClient.getMany(ids);
  const byId = new Map(users.map((u) => [u.id, u]));
  return ids.map((id) => byId.get(id) ?? null);
});

const names = await Promise.all(orders.map((o) => userLoader.load(o.userId)));
```

## 260: How do you debug a slow request that goes through several services?

1. Find the trace ID, from the response header, the logs or by searching for slow traces in the tracing tool.
2. Open the trace and look at the timeline: which span takes the most time, and are calls happening one after another when they could be in parallel?
3. Check whether the slow span is waiting on something (a database query, a lock, a connection pool) or using CPU.
4. Look at that service's metrics around the same time: event loop delay, pool usage, GC, CPU throttling, error rates.
5. Search logs for the trace ID to see details and errors.

Common findings: missing database indexes, sequential calls, retries hidden inside a client, a full connection pool or a cold cache.

## 261: What are ephemeral (preview) environments?

An ephemeral environment is a short-lived copy of the system, created automatically for a pull request and deleted when it is merged or closed. The changed service runs from the PR branch, while the other services use their current versions.

They let reviewers and QA test a change in a realistic setup before merging. With many services, full copies are expensive, so some teams use a shared baseline environment and route only test traffic with a special header to the PR's version of the service (request-level isolation, used by tools like Signadot).

## 262: How do you make Docker Compose wait until a dependency is actually ready?

`depends_on` alone only waits for the container to start, not for the database inside it to accept connections. Add a health check and use the `service_healthy` condition:

```yaml
services:
  orders:
    build: ./orders
    depends_on:
      orders-db:
        condition: service_healthy
  orders-db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 2s
      timeout: 3s
      retries: 15
```

Your service should still retry connections at startup, because in production there is no `depends_on`, and dependencies can restart at any time.

## 263: What are Kubernetes NetworkPolicies and why use them?

By default, any pod in a Kubernetes cluster can talk to any other pod. A NetworkPolicy restricts which pods can connect to which, like a firewall based on labels.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: payments-allow-orders
spec:
  podSelector:
    matchLabels: { app: payments }
  policyTypes: [Ingress]
  ingress:
    - from:
        - podSelector:
            matchLabels: { app: orders }
      ports:
        - port: 3000
```

This allows only the orders service to call payments. If an attacker takes over another pod, they cannot reach payments directly. Policies need a network plugin that enforces them, like Calico or Cilium.

## 264: Which HTTP security headers should services and gateways set?

For anything that serves browsers, set:

- `Strict-Transport-Security` to force HTTPS
- `Content-Security-Policy` to limit where scripts and other resources can load from
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options` or the CSP `frame-ancestors` directive to block clickjacking
- `Referrer-Policy`

In Node.js, `helmet` (Express) and `@fastify/helmet` set good defaults:

```js
import helmet from "helmet";
app.use(helmet());
```

For internal JSON APIs, most of these do not matter much, but it does not hurt to set them at the gateway. Also remove headers that reveal details, like `X-Powered-By` (`app.disable('x-powered-by')` in Express, helmet removes it too).

## 265: How do you manage dependency vulnerabilities across many Node.js services?

- Run `npm audit` (or `pnpm audit`) and a scanner like Snyk, Trivy, Grype or Docker Scout in CI for both packages and images.
- Use Renovate or Dependabot to open update PRs automatically, with tests running on them.
- Commit lockfiles and install with `npm ci`, so builds use exactly the reviewed versions.
- Generate an SBOM (software bill of materials) for each image, so you can quickly find which services use a vulnerable package.
- Rebuild images regularly to pick up base image patches, even if the code did not change.

With dozens of services, automation matters more than any single tool. Nobody can track updates by hand.

## 266: How do you rotate a secret without downtime?

The trick is to support two valid secrets during the change:

1. Create the new secret, and make the receiving side accept both old and new (for example, the database user has both passwords, or a JWT verifier accepts both keys).
2. Update the senders to use the new secret, through a rolling restart or by reloading mounted secret files.
3. Check that nothing uses the old secret anymore (logs, metrics).
4. Remove the old secret.

For JWT signing keys this is built in: the JWKS endpoint publishes several keys with different `kid` values, so verifiers accept both during rotation. Managed tools like AWS Secrets Manager can automate rotation for databases.

## 267: What should you not put in logs?

- Passwords, tokens, API keys, session cookies and private keys
- Full card numbers, CVV codes and bank details
- Personal data that you do not need: national IDs, health data, full addresses, sometimes emails and phone numbers
- Full request and response bodies by default

Use logger redaction (`redact` in Pino) for known fields, and avoid logging whole objects that can contain them. Logs are copied to many systems and kept a long time, and often more people can read them than can read the database.

## 268: What is audit logging and how is it different from application logging?

Application logs help developers debug and are often sampled, rotated or dropped. Audit logs record who did what and when, for security and compliance: "user u_42 changed the role of user u_99 to admin at 10:15 from IP x".

Audit logs should be:

- Complete (no sampling)
- Tamper resistant (append-only storage, restricted access)
- Kept for the required retention period
- Structured with actor, action, target, time and result

In microservices, each service can publish audit events to a dedicated topic, and an audit service stores them in a write-once store.

## 269: How do you keep message order in RabbitMQ when you have several consumers?

A single RabbitMQ queue delivers messages in order, but with several consumers or a prefetch above 1, messages are processed in parallel and can finish out of order. A failed message that is requeued also goes back behind newer ones.

Options:

- Use one consumer with `prefetch(1)` for queues where order matters. Simple but slow.
- Split work into several queues by key (for example with the consistent hash exchange plugin), so all messages for one order go to the same queue and one consumer.
- Use the single active consumer feature, so only one consumer reads the queue at a time, with others on standby.
- Make consumers tolerate out-of-order messages, for example by checking versions or timestamps.

## 270: What is a poison message and how do you handle it?

A poison message is a message that always fails, for example because of bad data or a bug in the consumer. If it is requeued again and again, it wastes resources and, in ordered systems, blocks every message behind it.

Handle it by:

- Limiting attempts (RabbitMQ quorum queues have a `delivery-limit`, and you can count attempts in a header).
- Moving it to a dead letter queue after the limit.
- Separating errors: a validation error will never succeed, so send it to the DLQ right away. A timeout might succeed later, so retry it.
- Alerting on DLQ size and having a tool to inspect and replay messages.

## 271: How do you do request-reply over RabbitMQ?

The client sends a message with `replyTo` set to its reply queue and a `correlationId`. The server processes it and sends the answer to `replyTo` with the same `correlationId`.

```js
// client
const { queue: replyQueue } = await ch.assertQueue("", { exclusive: true });
const pending = new Map();

await ch.consume(
  replyQueue,
  (msg) => {
    const resolve = pending.get(msg.properties.correlationId);
    if (resolve) {
      pending.delete(msg.properties.correlationId);
      resolve(JSON.parse(msg.content.toString()));
    }
  },
  { noAck: true },
);

export function call(queue, payload) {
  const correlationId = randomUUID();
  return new Promise((resolve) => {
    pending.set(correlationId, resolve);
    ch.sendToQueue(queue, Buffer.from(JSON.stringify(payload)), {
      correlationId,
      replyTo: replyQueue,
    });
  });
}
```

In real code add a timeout that removes the entry from `pending` and rejects. RabbitMQ also has a "direct reply-to" feature (`amq.rabbitmq.reply-to`) that avoids creating a reply queue. If you mostly need request-reply, consider whether plain HTTP or gRPC would be simpler.

## 272: How do you apply backpressure in a Kafka consumer?

If a consumer reads faster than it can process (for example because a downstream API is slow), memory grows and work piles up. With kafkajs you can pause and resume partitions:

```js
await consumer.run({
  eachMessage: async ({ topic, partition, message, pause }) => {
    try {
      await callSlowApi(message);
    } catch (err) {
      if (err.status === 429) {
        const resume = pause(); // pause this partition
        setTimeout(resume, 5_000);
        throw err; // message will be retried after resume
      }
      throw err;
    }
  },
});
```

You can also limit `partitionsConsumedConcurrently` and use `eachBatch` to control how much is in flight. The broker keeps the messages, so pausing is safe as long as lag stays within the retention period.

## 273: How do you process Kafka messages in batches?

Use `eachBatch` when you want to handle many messages together, for example with a bulk database insert.

```js
await consumer.run({
  eachBatchAutoResolve: false,
  eachBatch: async ({
    batch,
    resolveOffset,
    heartbeat,
    isRunning,
    isStale,
  }) => {
    const rows = [];
    for (const message of batch.messages) {
      if (!isRunning() || isStale()) break;
      rows.push(JSON.parse(message.value.toString()));
    }
    await db.bulkInsert(rows); // idempotent upsert
    for (const message of batch.messages.slice(0, rows.length)) {
      resolveOffset(message.offset);
    }
    await heartbeat();
  },
});
```

Call `heartbeat()` during long batches so the broker does not think the consumer died. If the bulk write fails, none of the offsets are resolved and the batch is retried, so the write must be idempotent.

## 274: What do acks and idempotence mean for a Kafka producer?

`acks` controls when the broker confirms a write:

- `acks=0`: no confirmation. Fastest, but messages can be lost.
- `acks=1`: the partition leader wrote it. Lost if the leader dies before followers copy it.
- `acks=all` (`-1`): all in-sync replicas wrote it. Safest, used with `min.insync.replicas=2` on the topic.

An **idempotent producer** adds a producer ID and sequence numbers, so the broker drops duplicates created by producer retries and keeps order per partition. In kafkajs, `idempotent: true` requires `acks: -1`. In the Java client and librdkafka-based clients, idempotence is on by default in recent versions.

## 275: What is the difference between retention and log compaction in Kafka?

**Retention** deletes old data by time or size, for example everything older than 7 days (`retention.ms`). It fits event streams where old events are no longer needed.

**Log compaction** (`cleanup.policy=compact`) keeps at least the latest message for each key and removes older ones with the same key. A message with a `null` value (a tombstone) deletes the key. It fits topics that represent current state, like "the latest profile for each user", so a new consumer can read the topic from the start and build the full current state.

The two can be combined with `cleanup.policy=compact,delete`.

## 276: How do you choose between RabbitMQ and Kafka?

Choose **RabbitMQ** when:

- You need task queues with flexible routing, priorities and per-message acks.
- Messages are consumed and then not needed again.
- Volumes are moderate and you want simple operations.

Choose **Kafka** when:

- You need very high throughput.
- Several consumers must read the same events independently, and new consumers must be able to replay history.
- You need ordering per key across a large stream.
- You are building data pipelines or event sourcing.

They overlap more than before: RabbitMQ has streams, and Kafka 4.x added share groups (queue-like consumption, still maturing). Team experience and managed service options often decide in the end.

## 277: What is NATS and when would you use it?

NATS is a lightweight messaging system with very low latency. Core NATS does pub/sub and request-reply with at-most-once delivery and no storage. **JetStream**, built into the NATS server, adds persistence, consumers with acks, replay and a key-value store.

```js
import { connect, StringCodec } from "nats";

const nc = await connect({ servers: "nats://nats:4222" });
const sc = StringCodec();

nc.subscribe("orders.created", {
  callback: (err, msg) => console.log(sc.decode(msg.data)),
});

nc.publish("orders.created", sc.encode(JSON.stringify({ id: "o_123" })));
```

It is a good fit when you want something simpler to run than Kafka, especially for request-reply and edge or IoT setups. The NATS JavaScript client is being split into scoped `@nats-io/*` packages, so check which package the current docs use.

## 278: How do you fan out events with Amazon SNS and SQS?

The publisher sends an event to an **SNS topic**. Each consuming service has its own **SQS queue** subscribed to the topic. SNS copies every message to every subscribed queue, and each service reads from its own queue at its own pace.

```js
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";

const sns = new SNSClient({});
await sns.send(
  new PublishCommand({
    TopicArn: process.env.ORDERS_TOPIC_ARN,
    Message: JSON.stringify(event),
    MessageAttributes: {
      type: { DataType: "String", StringValue: "order.created" },
    },
  }),
);
```

Subscription filter policies let a queue receive only some event types. Use FIFO topics and queues if you need ordering and deduplication per message group. Each queue should have its own DLQ.

## 279: How do Node.js Lambda functions fit into a microservices system?

Lambda functions are often used for:

- Event handlers: reacting to S3 uploads, SQS messages, DynamoDB streams or EventBridge events.
- Low-traffic or spiky APIs behind API Gateway.
- Scheduled jobs.
- Glue code between managed services.

A "service" can be a group of functions that share one data store and are deployed together. Things to watch: create clients (database, SDK) outside the handler so they are reused, avoid opening too many database connections (use RDS Proxy or HTTP-based databases), and set timeouts and concurrency limits so a burst does not overload downstream services.

## 280: What is a cold start and how do you reduce it?

A cold start is the extra time when a platform creates a new instance to handle a request: starting the runtime, loading code and running initialization. It happens in serverless functions and also when containers scale up from zero.

Ways to reduce it in Node.js:

- Keep the deployment small, bundle and tree-shake (esbuild), and avoid heavy dependencies.
- Load modules lazily if they are only needed for some requests.
- Do expensive setup once, outside the handler, and reuse it.
- Use features like provisioned concurrency, minimum instances or SnapStart where the platform offers them.

## 281: How do you monitor memory usage in a Node.js service?

`process.memoryUsage()` returns:

- `rss`: total memory the process uses, which is what the container limit counts
- `heapTotal` and `heapUsed`: the V8 heap
- `external` and `arrayBuffers`: memory for Buffers and native objects outside the heap

`prom-client`'s default metrics export these, plus GC duration. Watch `heapUsed` after GC over hours or days: if it keeps going up and never comes down, you probably have a leak. If `rss` grows while the heap stays flat, look at Buffers, native modules or memory fragmentation.

## 282: How do you take a heap snapshot from a service running in production?

Options:

- Start Node with `--heapsnapshot-signal=SIGUSR2`, then send the signal: `kill -USR2 <pid>`. Node writes a `.heapsnapshot` file to the working directory.
- Call `v8.writeHeapSnapshot()` from an admin-only endpoint.
- Use `--heapsnapshot-near-heap-limit=1` to write a snapshot automatically when the heap is about to run out.

Then copy the file out (for example with `kubectl cp`) and open it in Chrome DevTools. Take two or three snapshots some time apart and compare them to see what keeps growing. Writing a snapshot pauses the process and can need memory about the size of the heap, so take the pod out of traffic first if you can.

## 283: How do you attach a debugger to a Node.js service in Kubernetes?

1. Start the process with the inspector, or turn it on at runtime by sending `SIGUSR1` to the Node process.
2. Forward the inspector port to your machine:

```bash
kubectl port-forward pod/orders-7d9f8b-abcde 9229:9229
```

3. Open `chrome://inspect` in Chrome, or attach from VS Code, to `localhost:9229`.

Breakpoints pause the whole process, so never do this on a pod that serves real traffic. Remove the pod from the Service first (for example by changing its labels) or use a copy. For production problems, logs, traces, profiles and heap snapshots are usually safer than breakpoints.

## 284: How do you choose between Express and Fastify for a new service?

**Express** has the biggest ecosystem, the most examples and the most developers who already know it. Express 5 fixed async error handling, which was the biggest pain point.

**Fastify** has lower overhead per request, schema-based validation and serialization built in, Pino logging built in and a plugin system that keeps large services organized. It is a good default when performance or strict input validation matters.

For most services, the database and other network calls take far more time than the framework. Pick the one your team knows well and use it for all services, so tooling and shared packages stay simple.

## 285: What is Hono and why do some teams use it for services?

Hono is a small web framework built on Web standards (`Request`, `Response`, `fetch`). The same code runs on Node.js (with `@hono/node-server`), Bun, Deno, Cloudflare Workers and AWS Lambda.

```js
import { Hono } from "hono";
import { serve } from "@hono/node-server";

const app = new Hono();
app.get("/orders/:id", (c) => c.json({ id: c.req.param("id") }));

serve({ fetch: app.fetch, port: 3000 });
```

Teams pick it for edge functions, BFFs that may move between runtimes and small services where they want very little framework code. It also has typed RPC helpers so a client can use the server's route types.

## 286: Can Node.js services talk to each other over HTTP/2?

Yes. Node has a built-in `node:http2` module for servers and clients, and undici can use HTTP/2 when you set `allowH2: true` on its `Agent`. gRPC always uses HTTP/2.

HTTP/2 sends many requests over one connection (multiplexing) and compresses headers, which helps when services make many small calls to each other. The downsides: one connection means connection-level load balancers spread load badly (the same problem as gRPC), and inside a cluster, plain HTTP/1.1 with keep-alive is often fast enough. Many teams let a service mesh or proxy handle HTTP/2 between nodes instead of the app.

## 287: What is a service catalog and why does it help with many microservices?

A service catalog is a central list of every service with its owner team, repository, docs, API specs, dependencies, on-call contact, dashboards and runbooks. Backstage (from Spotify, now a CNCF project) is the most common open source tool for this.

With dozens or hundreds of services, people constantly need to answer "who owns this?", "where are the logs?" and "what calls this API?". A catalog gives one place to find those answers, and it can also check standards like "every service has an owner and an SLO".

## 288: What is a service template (golden path)?

A service template is a ready-made starting point for new services that already includes the company's standard setup: framework, folder structure, logging, tracing, metrics, health checks, graceful shutdown, Dockerfile, CI pipeline, Helm chart and linting.

It saves weeks of setup per service and keeps services consistent, so any engineer can move between them easily. It can be a Git template repo, a generator like Backstage software templates, or a shared internal package that does the setup (`createService({ name: 'orders' })`). Keep it maintained, or new services will start with outdated code.

## 289: How do you implement the strangler fig pattern with a Node.js proxy?

Put a routing layer in front of the monolith and move routes to new services one by one.

```js
import express from "express";
import { createProxyMiddleware } from "http-proxy-middleware";

const app = express();

const toOrders = createProxyMiddleware({
  target: "http://orders-service:3000",
  changeOrigin: true,
});
const toMonolith = createProxyMiddleware({
  target: "http://legacy-app:8080",
  changeOrigin: true,
});

// moved to the new service
app.use("/api/orders", toOrders);

// everything else still goes to the monolith
app.use("/", toMonolith);

app.listen(8080);
```

You can also move traffic gradually, for example sending only some users or a percentage of requests to the new service, and compare results. The hardest part is usually the data, not the routing.

## 290: What is the dual write problem?

The dual write problem happens when a service has to write to two systems that do not share a transaction, like its database and a message broker, or two different databases. If one write succeeds and the other fails, the systems are out of sync.

```js
await db.orders.insert(order); // succeeds
await producer.send(orderCreated); // fails, other services never hear about the order
```

Switching the order does not help: then you could publish an event for an order that was never saved. The fixes are the outbox pattern, change data capture, or making one write the source of truth and deriving the other from it.

## 291: How do you move data out of a monolith into a new service?

A common step-by-step approach:

1. Create the new service with its own database and an empty copy of the data.
2. Copy existing data with a backfill, and keep it in sync using CDC from the monolith's database (Debezium) or events published by the monolith.
3. Switch reads to the new service, while the monolith still owns writes. Compare results to find differences.
4. Switch writes to the new service. Now sync goes the other way, from the new service back to the monolith, for the parts of the monolith that still read the old tables.
5. Remove the old tables and the sync once nothing in the monolith uses them.

Avoid having both systems accept writes for the same data at the same time, because it leads to conflicts that are very hard to resolve.

## 292: What logic belongs in an API gateway and what belongs in a BFF?

The **API gateway** should handle generic, cross-cutting concerns for all traffic: TLS, routing, authentication, rate limiting, request size limits and basic logging. It should not know about business rules.

A **BFF** holds logic specific to one client: combining calls, shaping responses for a screen, handling client-specific auth flows (like cookies for the web app) and simple formatting.

Neither should hold core business rules like pricing or order validation. Those belong in the domain services, otherwise you have to duplicate them in every BFF.

## 293: How should timeouts be set along a chain of services?

Each layer's timeout should be shorter than the layer that calls it. For example:

- Client: 10 s
- API gateway: 8 s
- BFF: 6 s for the whole request, with 2 s per downstream call
- Domain service: 1.5 s per database query

If an inner timeout is longer than an outer one, the outer layer gives up first while the inner layer keeps working on a request nobody is waiting for, and retries at the outer layer then add even more load. Base timeouts on real latency data (for example a bit above p99), not on round numbers chosen by guessing.

## 294: How do you size a database connection pool in a microservice?

Total connections = pool size per instance × number of instances (× number of services using the database). With 20 pods and a pool of 20 each, that is 400 connections, which can be more than the database allows.

```js
import pg from "pg";

const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
  max: 10,
  idleTimeoutMillis: 30_000,
  connectionTimeoutMillis: 2_000,
});
```

Since Node.js runs JavaScript on one thread, a small pool (often 5 to 20) per process is usually enough. Set `connectionTimeoutMillis` so requests fail fast when the pool is exhausted instead of hanging, and include pool usage in your metrics. Remember to count the autoscaler's maximum replicas, not the normal count.

## 295: What is PgBouncer and when do microservices need it?

PgBouncer is a lightweight connection pooler that sits between your services and PostgreSQL. Many clients connect to PgBouncer, and it shares a much smaller number of real database connections between them.

You need something like it when many service instances, autoscaling or serverless functions would open more connections than PostgreSQL can handle well. In **transaction pooling** mode, a real connection is only held during a transaction, which saves the most connections. That mode breaks some session features, like session-level advisory locks and `SET` commands that are expected to last. Newer PgBouncer versions support prepared statements in transaction mode, but check your driver's settings. Cloud providers offer managed versions, like RDS Proxy.

## 296: What should you know about using read replicas in a service?

Read replicas take read load off the primary database, but they are updated asynchronously, so they can be a bit behind (replication lag).

Problems this causes:

- **Read your own writes:** a user saves something and immediately reads from a replica that does not have it yet. Fix by reading from the primary for a short time after a write, or for that user's own data.
- **Inconsistent pages:** two queries for the same page hit different replicas with different lag.

Send writes and reads that must be fresh to the primary. Send reads that can be a little old (lists, search, reports) to replicas. Monitor lag and stop using a replica that falls too far behind.

## 297: How do you organize versioned routes in an Express service?

Use a router per version and mount them under their prefixes. Share the service layer and change only what is different.

```js
import express from "express";

const v1 = express.Router();
v1.get("/orders/:id", async (req, res) => {
  const order = await ordersService.get(req.params.id);
  res.json({ id: order.id, total: order.totalCents / 100 }); // old format
});

const v2 = express.Router();
v2.get("/orders/:id", async (req, res) => {
  const order = await ordersService.get(req.params.id);
  res.json({
    id: order.id,
    total: { amount: order.totalCents, currency: order.currency },
  });
});

app.use("/v1", v1);
app.use("/v2", v2);
```

Add a `Deprecation` and `Sunset` header to old versions so clients know when they will be removed, and track who still calls them before you turn them off.

## 298: How do you design an API for a long-running operation?

Do not keep the HTTP request open for minutes. Accept the request, return `202 Accepted` with a link to check status, and do the work in the background.

```js
app.post("/reports", async (req, res) => {
  const job = await reportsQueue.add("generate", req.body);
  res
    .status(202)
    .location(`/reports/jobs/${job.id}`)
    .json({ jobId: job.id, status: "queued" });
});

app.get("/reports/jobs/:id", async (req, res) => {
  const job = await reportsQueue.getJob(req.params.id);
  if (!job) return res.sendStatus(404);
  const state = await job.getState();
  res.json({
    status: state,
    result: state === "completed" ? job.returnvalue : undefined,
  });
});
```

Clients can poll the status endpoint, or you can notify them when it is done with a webhook, WebSocket or SSE.

## 299: How do you roll back a bad deployment in Kubernetes?

```bash
kubectl rollout history deployment/orders
kubectl rollout undo deployment/orders
kubectl rollout undo deployment/orders --to-revision=12
kubectl rollout status deployment/orders
```

With GitOps (Argo CD, Flux), you revert the commit that changed the image tag instead, so Git stays the source of truth.

A rollback only restores the code. If the bad version ran a database migration, published events in a new format or wrote bad data, you have to deal with those too. That is why migrations should be backward compatible and why canary releases help: you catch problems before most data is affected.

## 300: How do you test how your services behave when a dependency is slow or failing?

- **Unit and component tests:** mock the dependency to return errors, timeouts and slow responses, and check that retries, timeouts, circuit breakers and fallbacks behave as expected.
- **Toxiproxy:** a TCP proxy from Shopify that can add latency, drop connections or limit bandwidth between your service and a real dependency in tests or local Docker setups.
- **Service mesh fault injection:** Istio and similar tools can inject delays and errors for a percentage of requests in staging.
- **Chaos experiments:** tools like Chaos Mesh or LitmusChaos kill pods or break the network in a controlled way.

Start small in non-production environments, and always have a clear idea of what you expect to happen before you run an experiment.

---

# Advanced Questions (301-450)

## 301: Why does latency in a Node.js service grow so fast when it gets close to full load?

Node runs JavaScript on one thread. Each request needs some CPU time on that thread, and while one request runs, everything else waits in the event loop queue. At low load the queue is almost empty. As CPU use gets close to 100%, the queue grows quickly, and every request waits behind the others.

This follows basic queueing theory: waiting time rises sharply as utilization nears 100%, not in a straight line. That is why a service can look fine at 60% CPU and fall apart at 90%. Keep headroom (scale out at around 60-70% CPU), keep CPU work per request small and watch event loop delay, not just CPU.

## 302: What is load shedding and how do you do it in Node.js?

Load shedding means rejecting some requests quickly when the service is overloaded, so it can still serve the rest well. Without it, an overloaded service tries to handle everything, gets slow for everyone and often falls over.

In Fastify, `@fastify/under-pressure` returns `503` when event loop delay, heap or RSS go above limits:

```js
import underPressure from "@fastify/under-pressure";

await app.register(underPressure, {
  maxEventLoopDelay: 200,
  maxHeapUsedBytes: 900 * 1024 * 1024,
  retryAfter: 5,
  pressureHandler: (req, reply, type, value) => {
    reply
      .code(503)
      .header("Retry-After", "5")
      .send({ title: "Service overloaded" });
  },
});
```

Shed cheap and less important traffic first (background sync, analytics) and protect important flows like checkout. Reject early, before doing any expensive work, otherwise shedding does not save much.

## 303: What are adaptive concurrency limits?

A fixed concurrency limit ("max 100 requests in flight") is hard to choose: too low wastes capacity, too high allows overload. Adaptive limits change the limit at runtime based on measured latency.

The idea, similar to TCP congestion control: while latency stays close to the best observed latency, slowly raise the limit. When latency rises, the service or its dependency is getting saturated, so lower the limit. Requests over the limit are rejected or queued briefly. Netflix's concurrency-limits library popularized this, and Envoy has an adaptive concurrency filter. In Node you can build it with a counter around request handling or outgoing calls, plus a latency window.

## 304: What are hedged requests?

A hedged request means sending a second copy of a request to another instance if the first one has not answered within a short time, usually around the p95 latency. You use whichever answer comes first and cancel the other.

```js
async function hedged(urls, hedgeAfterMs) {
  const controllers = urls.map(() => new AbortController());
  const attempt = (i) =>
    fetch(urls[i], { signal: controllers[i].signal }).then((r) => {
      if (!r.ok) throw new Error(String(r.status));
      return r.json();
    });

  const first = attempt(0);
  const second = new Promise((r) => setTimeout(r, hedgeAfterMs)).then(() =>
    attempt(1),
  );
  try {
    return await Promise.any([first, second]);
  } finally {
    controllers.forEach((c) => c.abort());
  }
}
```

It cuts tail latency a lot for a small cost (only around 5% extra requests if you hedge at p95). Only use it for idempotent reads, and turn it off when the backend is overloaded, or it adds load right when it hurts most. Also clear the timer so the second attempt does not start after the first one has already won.

## 305: How does fan-out make tail latency worse?

If a request calls one service whose p99 is 500 ms, 1% of requests are slow. If the request calls 50 services in parallel and waits for all of them, the chance that at least one is slow is `1 - 0.99^50`, about 40%. So the p99 of each service becomes close to the median of the whole request.

Ways to deal with it:

- Reduce fan-out with bulk endpoints or precomputed read models.
- Use hedged requests for idempotent reads.
- Give optional calls tight timeouts and return partial results.
- Work on tail latency of each service (GC pauses, cold caches, slow queries), not just its average.

## 306: What is a retry storm and how do you stop one?

A retry storm happens when a service slows down or fails and all its callers start retrying at once. The extra traffic keeps the service overloaded, so it cannot recover even after the original problem is gone. When it comes back up, all the queued retries can knock it down again (a thundering herd).

To prevent it:

- Exponential backoff with jitter in every client.
- Retry budgets or token buckets that cap retries to a share of normal traffic.
- Circuit breakers so callers stop sending traffic for a while.
- Retry at one layer only.
- Load shedding on the server, with `Retry-After` headers that clients respect.
- Ramp up traffic slowly after recovery.

## 307: What is a metastable failure?

A metastable failure is a state where a system stays broken even after the trigger that caused it is gone. The system gets stuck in a bad loop that keeps itself going.

Typical example: a short database slowdown makes requests time out, clients retry, the extra load keeps the database slow, more timeouts cause more retries. The original slowdown ended long ago, but the system does not recover until someone cuts traffic by hand.

Other loops: cache failures that send all traffic to the database, or GC pressure from piled-up requests that slows processing further. The defenses are the same tools that limit work under stress: retry budgets, load shedding, circuit breakers, bounded queues and the ability to quickly reduce incoming traffic.

## 308: How does exactly-once processing work in Kafka, and what are its limits?

Kafka supports exactly-once semantics for **read-process-write inside Kafka**. A transactional producer can write output messages and commit the consumer's input offsets in one atomic transaction. Consumers with `isolation.level=read_committed` only see committed messages.

```js
const producer = kafka.producer({
  transactionalId: "pricing-processor-1",
  idempotent: true,
  maxInFlightRequests: 1,
});
await producer.connect();

const tx = await producer.transaction();
try {
  await tx.send({ topic: "prices-calculated", messages: [{ key, value }] });
  await tx.sendOffsets({
    consumerGroupId: "pricing",
    topics: [
      { topic: "orders", partitions: [{ partition, offset: nextOffset }] },
    ],
  });
  await tx.commit();
} catch (err) {
  await tx.abort();
  throw err;
}
```

The limit: as soon as the processing touches anything outside Kafka (a database, an email API, an HTTP call), Kafka transactions do not cover it. For those, you still need idempotent writes, the inbox pattern or storing offsets in the same database transaction as the result.

## 309: How can retries break message ordering, and how do you prevent it?

On the producer side: if several batches are in flight to the same partition and the first fails and is retried, the second can land first. Kafka's idempotent producer prevents this by using sequence numbers, so keep idempotence on.

On the consumer side:

- Processing messages from one partition in parallel loses order.
- Sending a failed message to a retry topic and moving on means later messages for the same key are processed before the retried one.

If order matters per key, either block the partition until the message succeeds (simple but can stall), or keep track of keys that have a message in retry and send later messages for those keys to the retry path too. Often the better fix is to make consumers tolerant of disorder, for example by ignoring events with a version older than what they already have.

## 310: How do you handle events that arrive out of order?

- **Versions:** each event for an entity carries a version number. The consumer stores the last version it applied and ignores anything older.
- **Timestamps with care:** use the source's timestamp for "last write wins" only when clocks are reliable enough, and break ties deterministically.
- **Buffering:** hold events briefly and apply them in sequence when a gap is filled. This is complex and needs a timeout for missing events.
- **Fetch current state:** treat an event as a signal ("order o_123 changed") and fetch the latest state from the owning service.
- **Commutative operations:** design updates so order does not matter, for example adding to a set instead of overwriting a list.

```sql
UPDATE order_view SET status = $1, version = $2
WHERE order_id = $3 AND version < $2;
```

## 311: How do you implement an event store with optimistic concurrency?

An event store keeps events per stream (usually one stream per aggregate, like one order). When appending, you pass the version you expect the stream to be at, and the append fails if someone else appended first.

```sql
CREATE TABLE events (
  stream_id   text        NOT NULL,
  version     int         NOT NULL,
  type        text        NOT NULL,
  data        jsonb       NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (stream_id, version)
);
```

```js
async function append(streamId, expectedVersion, newEvents) {
  const values = newEvents.map((e, i) => [
    streamId,
    expectedVersion + i + 1,
    e.type,
    e.data,
  ]);
  try {
    await db.query(
      `INSERT INTO events (stream_id, version, type, data)
       SELECT * FROM unnest($1::text[], $2::int[], $3::text[], $4::jsonb[])`,
      [
        values.map((v) => v[0]),
        values.map((v) => v[1]),
        values.map((v) => v[2]),
        values.map((v) => v[3]),
      ],
    );
  } catch (err) {
    if (err.code === "23505") throw new ConcurrencyError(streamId); // unique violation
    throw err;
  }
}
```

The primary key on `(stream_id, version)` does the concurrency check. Dedicated databases like EventStoreDB (now Kurrent) offer this built in, with subscriptions for building projections.

## 312: What are snapshots in event sourcing and when do you need them?

To load an aggregate, you replay all its events. If an entity has thousands of events (like a long-lived account), this gets slow. A snapshot stores the aggregate's state at a certain version. To load it, you read the latest snapshot and only replay events after it.

Things to keep in mind:

- Snapshots are a performance cache, not the source of truth. You must be able to delete them and rebuild from events.
- When the aggregate's code or state shape changes, old snapshots may become invalid. Version snapshots and discard ones from old versions.
- Most aggregates have few events and do not need snapshots. Add them only where you measure a problem.

## 313: How do you rebuild a projection in an event-sourced or event-driven system?

1. Create a new, empty version of the read model (a new table or index, like `order_view_v2`).
2. Run the projection code from the first event to the latest, writing to the new version.
3. Keep it running to catch up with live events while the old one still serves reads.
4. When it has caught up, switch reads to the new version.
5. Delete the old one.

Projection handlers must be deterministic and must not cause side effects like sending emails, or a rebuild will resend them. Store the position (offset or global event number) the projection has processed in the same transaction as the read model update, so it can resume after a crash without gaps or duplicates.

## 314: What is event upcasting?

Upcasting means converting old versions of events into the current version when they are read, instead of changing stored events. Events in an event store or a compacted topic are often kept forever, so you cannot simply change their format.

```js
const upcasters = {
  "order.created": {
    1: (e) => ({ ...e, version: 2, data: { ...e.data, currency: "USD" } }),
  },
};

function upcast(event) {
  let current = event;
  while (upcasters[current.type]?.[current.version]) {
    current = upcasters[current.type][current.version](current);
  }
  return current;
}
```

The rest of the code then only deals with the latest version. Keep upcasters as pure functions and test them with real samples of old events.

## 315: How do you deal with eventual consistency in the user interface?

When writes go to one service and reads come from a read model updated by events, a user may not see their own change right away. Options:

- **Return the new state in the write response** and have the UI use it directly.
- **Optimistic UI:** update the screen right away and roll back if the write fails.
- **Read your own writes:** after a write, read from the write side (or wait for the projection to reach the version returned by the write) for that user.
- **Show progress:** "Your order is being processed" with live updates via SSE or WebSockets.

```js
// write returns the version, read waits until the projection has it
const { version } = await api.post("/orders", body);
await api.get(`/order-views/${id}?minVersion=${version}`); // server waits briefly or returns 202
```

## 316: What isolation problems do sagas have and how do you handle them?

Sagas do not have the isolation of a database transaction. Other requests can see and act on intermediate states. Problems:

- **Dirty reads:** another service reads an order that is in the middle of a saga and later gets cancelled.
- **Lost updates:** one saga overwrites changes made by another without reading them.
- **Fuzzy reads:** two steps of the same saga read different values for the same data.

Countermeasures:

- **Semantic locks:** mark records with a state like `PENDING` or `APPROVAL_PENDING`, and make other operations respect it.
- **Commutative updates:** design operations so order does not matter (debit and credit amounts instead of setting a balance).
- **Re-read values** before acting to check they did not change (optimistic checks).
- **Order steps** so that the risky or reversible ones come first and the irreversible ones come last.

## 317: What do you do if a compensating action fails?

Compensations must eventually succeed, because there is no further step to undo them. So:

- Make compensations idempotent and retry them with backoff, possibly for a long time.
- Store the saga state durably so retries continue after crashes.
- If a compensation cannot succeed (for example a refund rejected because the card is closed), move the saga to a "needs manual action" state, alert someone and give support tools to fix it.
- Design compensations that are likely to succeed: a refund to store credit may be a fallback when a card refund fails.

Workflow engines like Temporal help here because they keep retrying activities and remember where each workflow is, even across deployments.

## 318: What is Temporal and why must workflow code be deterministic?

Temporal is a workflow engine. You write workflows as normal async code with the TypeScript SDK, and Temporal records each step's result in an event history. If a worker crashes, another worker replays the workflow code from the history to rebuild its state and continues from where it stopped.

```ts
import { proxyActivities } from "@temporalio/workflow";
import type * as activities from "./activities";

const { reserveStock, chargeCard, refund, releaseStock } = proxyActivities<
  typeof activities
>({
  startToCloseTimeout: "30 seconds",
  retry: { maximumAttempts: 5 },
});

export async function orderWorkflow(order: Order): Promise<void> {
  await reserveStock(order);
  try {
    await chargeCard(order);
  } catch (err) {
    await releaseStock(order);
    throw err;
  }
}
```

Because the code is replayed, it must produce the same sequence of commands every time. Workflow code must not call `Math.random()`, read the clock or do I/O directly. Those go into **activities**. The TypeScript SDK runs workflows in a sandbox that replaces things like `Date.now()` with deterministic versions. Changing workflow code while old workflows are running requires versioning (patching).

## 319: Why are two-phase commit and distributed transactions usually avoided in microservices?

Two-phase commit (2PC) has a coordinator ask all participants to prepare, then tells them all to commit. It gives atomic commits across databases, but:

- All participants must be up at the same time, so availability drops with each one added.
- Participants hold locks while waiting for the coordinator, which hurts throughput.
- If the coordinator fails at the wrong time, participants can be stuck holding locks.
- Many modern data stores and brokers do not support XA transactions at all.
- It couples services tightly at the database level.

Sagas, outbox and idempotent consumers trade immediate consistency for availability and independence, which fits most business processes better.

## 320: Why are distributed locks hard to get right?

A lock holder can be paused at any time, by a long GC pause, CPU throttling or a network delay. If the pause is longer than the lock's TTL, the lock expires and another process takes it. Now two processes think they hold the lock.

Redlock (locking across several Redis nodes) also depends on timing assumptions, which is why people like Martin Kleppmann argued it is not safe for correctness.

The safer approach is **fencing tokens**: every time the lock is granted, it comes with a number that always increases. The protected resource (for example the database) rejects writes with a token lower than the highest one it has seen.

```sql
UPDATE jobs SET result = $1, fence = $2
WHERE id = $3 AND fence < $2;
```

Use simple Redis locks for efficiency (avoiding duplicate work). For correctness, rely on database constraints, fencing or a consensus system like etcd or ZooKeeper.

## 321: Why can't you trust wall clock time to order events across services?

Each machine has its own clock, and clocks drift. NTP keeps them close, but they can still be off by milliseconds or more, and a clock can jump backwards after a sync. Two events from different services can end up with timestamps in the wrong order.

So "last write wins" based on timestamps can silently drop the newest update. Safer options:

- Order by a sequence from one source, like a database sequence or a Kafka partition offset.
- Use version numbers per entity.
- Use logical clocks (Lamport clocks, vector clocks, hybrid logical clocks) when you need ordering across nodes.

Also use monotonic time (`performance.now()` or `process.hrtime.bigint()`) to measure durations, not `Date.now()`.

## 322: What are Lamport clocks and hybrid logical clocks?

A **Lamport clock** is a counter on each node. It goes up by one for each event, and when a node receives a message it sets its counter to `max(own, received) + 1`. If event A caused event B, A's counter is lower. It does not tell you anything about real time.

A **hybrid logical clock (HLC)** combines the physical time with a logical counter. It stays close to wall clock time, so it is readable, but it never goes backwards and still respects cause and effect between messages. Databases like CockroachDB use HLCs.

**Vector clocks** keep one counter per node and can tell when two events happened concurrently, which helps detect conflicts, at the cost of bigger metadata.

## 323: What is consistent hashing and where is it used?

Consistent hashing maps keys and servers onto the same hash ring. Each key goes to the next server on the ring. When you add or remove a server, only the keys near it move. With normal `hash(key) % N`, changing N moves almost every key.

It is used for:

- Distributing cache keys across Redis or Memcached nodes.
- Sticky routing, for example sending all requests for one user to the same instance to use a local cache.
- Partitioning data in distributed databases (Cassandra, DynamoDB).
- RabbitMQ's consistent hash exchange.

Virtual nodes (each server appears many times on the ring) make the spread more even.

## 324: How would you shard the data of a single microservice?

When one database cannot handle a service's data or write load, you split it across several databases (shards).

Decisions:

- **Shard key:** choose a key that most queries include and that spreads load evenly, like `tenant_id` or `user_id`. Queries without the key have to hit every shard.
- **Mapping:** hash-based (even spread, hard to move ranges), range-based (good for range queries, risk of hot spots) or directory-based (a lookup table, flexible but one more component).
- **Rebalancing:** plan how to move data when adding shards, for example by starting with many logical shards on few physical servers.
- **Cross-shard work:** avoid transactions across shards and use sagas or design so related data lives on one shard.

Before sharding, check simpler options: indexes, read replicas, caching, archiving old data, a bigger instance, or a database that shards for you (CockroachDB, YugabyteDB, Vitess, Citus, DynamoDB).

## 325: How do you design microservices to run active-active in several regions?

- Route users to the nearest healthy region with global DNS or anycast load balancing.
- Decide for each data type how it is shared: some data can be owned by one "home" region per user or tenant, some must be replicated everywhere.
- Use databases with multi-region support (Spanner, CockroachDB, DynamoDB global tables, Aurora Global Database) or replicate events between regional brokers (Kafka MirrorMaker 2 or Confluent Cluster Linking).
- Plan for conflicts when two regions change the same data, or avoid them by giving each record a single home region.
- Make services idempotent, since cross-region failover often replays work.
- Test region failover regularly, not only on paper.

Active-active is expensive and complex. Many systems are fine with active-passive or with per-region cells that do not share data.

## 326: How do you resolve conflicting writes in a multi-region system?

- **Last write wins (LWW):** keep the write with the latest timestamp. Simple, but it silently drops updates and depends on clocks.
- **Single owner:** every record has a home region, and only that region accepts writes for it. No conflicts, but writes from far away are slower.
- **Application merge:** keep both versions and merge with business rules (for example, combine the items of two shopping carts).
- **CRDTs:** data types like counters, sets and maps designed so that concurrent updates always merge to the same result, no matter the order. Libraries like Automerge and Yjs use them.

Pick the approach per data type. Money and inventory usually need a single owner, while likes, presence or carts can use CRDT-like merges.

## 327: What is cell-based architecture?

In a cell-based architecture, the whole system (or a big part of it) is deployed as several independent copies called **cells**. Each cell has its own services, databases and queues and serves a subset of customers. A thin routing layer sends each customer to their cell.

Benefits:

- A bad deployment or failure only affects the customers in one cell.
- You scale by adding cells instead of making everything bigger.
- Each cell has a known, tested size.

Costs: more infrastructure to run, a routing layer that must be very reliable, and extra work to move customers between cells or run queries across all cells. AWS and Slack are well-known users of this approach.

## 328: How do you reduce the blast radius of failures and bad deployments?

- Deploy gradually: canaries, one region or cell at a time, with automatic rollback on bad metrics.
- Split traffic into cells or shards so one failure only affects some customers.
- Use bulkheads: separate pools, queues and instances for different workloads and tenants.
- Feature flags with kill switches for risky features.
- Limit what each service can do: least-privilege credentials, network policies and rate limits between services.
- Keep critical paths short and remove unneeded synchronous dependencies from them.
- Make config changes go through the same gradual rollout as code, since many big outages came from config.

## 329: What are the trade-offs of using a service mesh?

Benefits: mTLS, retries, timeouts, traffic splitting, telemetry and access policies, the same for every service and language, without changing code.

Costs:

- Extra latency per hop (usually small, but it adds up across long call chains).
- Extra CPU and memory for every sidecar, or for node-level proxies in sidecar-less modes.
- A complex system to run and upgrade. When the mesh breaks, everything breaks.
- Harder debugging, since behaviour lives outside the app.
- Overlap with app-level retries and timeouts, which can cause retry amplification if both are on.

Sidecar-less designs like Istio ambient mode cut much of the resource cost. A mesh pays off with many services and strict security needs. With a few Node.js services, libraries and good defaults are often enough.

## 330: Should resilience logic live in a library or in the infrastructure?

**Library approach** (opossum, retry helpers, a shared HTTP client): the app knows the business context, so it can choose fallbacks, decide which operations are idempotent and return partial results. But each language needs its own library, and every service must upgrade it.

**Infrastructure approach** (service mesh, gateway): consistent for all services and languages, changes without redeploying apps. But the proxy does not know which requests are safe to retry or what a good fallback is.

A common split: the mesh handles mTLS, connection-level timeouts, outlier detection and telemetry. The app handles business fallbacks, idempotency and retries for specific operations. Make sure the two do not both retry the same calls.

## 331: What does zero trust mean for microservices?

Zero trust means no request is trusted just because it comes from inside the network. Every call must prove who it is and be allowed by policy.

In practice:

- Every service has a strong identity (certificates via mTLS, SPIFFE IDs or cloud workload identity).
- Every call is authenticated and encrypted, including internal ones.
- Authorization policies say which service can call which endpoint ("orders can call payments POST /charges").
- User identity is passed along and checked, not replaced by a blanket "internal" trust.
- Network policies, short-lived credentials and audit logs limit what an attacker can do after breaking into one service.

## 332: What is SPIFFE?

SPIFFE (Secure Production Identity Framework For Everyone) is a standard for giving workloads identities. Each workload gets a SPIFFE ID like `spiffe://example.com/ns/prod/sa/orders` and a short-lived document that proves it, usually an X.509 certificate (an SVID).

SPIRE is the reference implementation: it checks what a workload is (for example by Kubernetes service account) and issues and rotates its certificates. Service meshes like Istio use SPIFFE-style identities internally. It means services can authenticate each other with mTLS without managing long-lived secrets.

## 333: What is SSRF and why is it a risk in microservices?

Server-Side Request Forgery (SSRF) happens when an attacker makes your service send a request to a URL they choose. In microservices this is dangerous because your service can reach internal services, admin endpoints and cloud metadata endpoints (like `169.254.169.254`) that are not exposed to the internet.

Typical features at risk: webhooks with user-provided URLs, "import from URL", link previews and PDF generators that load remote content.

Defenses:

- Allow-list domains where possible.
- Resolve the hostname and block private, loopback and link-local IP ranges, and check again after redirects (or turn redirects off).
- Run URL fetching in a separate service with no access to internal networks.
- Use IMDSv2 on AWS, which needs a token and blocks simple SSRF to the metadata service.

## 334: What are common JWT mistakes in microservices?

- Not checking `aud`, so a token for one service is accepted by another.
- Allowing any algorithm, which opens the door to `none` or algorithm confusion attacks (HS256 with the public key as the secret).
- Long expiry times, so a stolen token works for days.
- Putting sensitive data in the payload, which anyone can decode.
- Sharing one HMAC secret across all services, so any service can create tokens for any other.
- Using JWTs as session cookies without a way to revoke them.
- Fetching JWKS on every request instead of caching, or never refreshing it, which breaks key rotation.

Use asymmetric keys (RS256, ES256, EdDSA), short-lived access tokens, strict validation options and a well-tested library like `jose`.

## 335: How do you revoke JWTs before they expire?

JWTs are checked without calling the issuer, so you cannot "delete" one. Options:

- **Short lifetimes** (5-15 minutes) with refresh tokens. Revoke the refresh token, and the access token dies soon after.
- **Deny list:** store the `jti` (token ID) of revoked tokens in Redis until their expiry, and check it on each request. It adds a lookup but keeps it cheap.
- **Token version per user:** store a `tokenVersion` for each user and put it in the token. Bump it to invalidate all of that user's tokens.
- **Introspection:** for sensitive actions, call the identity provider's introspection endpoint to check if the token is still active.
- **Opaque tokens at the edge:** the gateway turns a revocable opaque token into a short-lived internal JWT ("phantom token" pattern).

## 336: What is the confused deputy problem in microservices?

A confused deputy is a service with high privileges that gets tricked into using them on behalf of someone who should not have that access.

Example: a reporting service has full read access to the orders service. A user asks for a report on another customer's orders, and the reporting service fetches them with its own service credentials without checking whether that user is allowed.

To avoid it:

- Pass the end user's identity along and check permissions based on it, not only on the calling service's identity.
- Use token exchange to get a downstream token scoped to the user and the purpose.
- Give each service the minimum privileges it needs.

## 337: How do you secure a message broker shared by many services?

- Require authentication for every client (SASL/SCRAM, mTLS, or cloud IAM). No anonymous access.
- Use authorization per topic or queue: the orders service can write to `orders`, the email service can only read it. Kafka ACLs and RabbitMQ vhost and topic permissions support this.
- Encrypt traffic with TLS, and encrypt data at rest.
- Treat incoming messages as untrusted input and validate them like HTTP requests.
- Do not put secrets or unneeded personal data in messages. They are copied to many consumers and kept for the retention period.
- Set quotas so one producer cannot flood the cluster.
- Sign or include producer identity in messages if consumers need to trust where a message came from.

## 338: How do you protect Node.js services from supply chain attacks?

- Commit lockfiles and install with `npm ci`, so you only get reviewed versions.
- Review new dependencies: maintainers, download counts, install scripts and how much code they pull in.
- Disable install scripts where you can (`npm ci --ignore-scripts`) or allow-list them (pnpm's `onlyBuiltDependencies`), since many attacks run during install.
- Use a private registry proxy that can block or delay brand-new package versions.
- Check provenance for packages published with npm trusted publishing and provenance statements.
- Run scanners that detect known malware and vulnerabilities in CI.
- Keep build pipelines locked down: pinned action versions by SHA, minimal tokens, no long-lived publish tokens.
- Sign your own images (Sigstore cosign) and verify signatures before deployment.

## 339: What is the Node.js permission model and is it useful for services?

The permission model restricts what a Node.js process can access. You start it with `--permission` and grant only what is needed:

```bash
node --permission \
  --allow-fs-read=/app \
  --allow-fs-write=/tmp \
  src/server.js
```

Without explicit grants, file system access, child processes, worker threads, native addons and WASI are blocked. It became stable in Node 23.5 and was backported to the 22.x line. Network restrictions were added more recently (`--allow-net`), so check your version's docs.

It is a useful extra layer against compromised dependencies, but it does not replace container isolation, a non-root user and a read-only file system. The Node docs say it is not meant to protect against malicious code that is already running with the ability to bypass it in every case.

## 340: What are the risks of passing secrets as environment variables?

- Environment variables are visible to the whole process and all its child processes.
- They can show up in crash dumps, debug pages, error reporting tools and `docker inspect` or Kubernetes pod specs for anyone with access.
- Logging `process.env` by accident leaks everything at once.
- They cannot be updated without restarting the process.

Safer options: mount secrets as files with tight permissions and read them when needed, fetch them from a secrets manager at startup with workload identity, or use short-lived dynamic credentials (for example Vault database credentials). Environment variables are still common and acceptable for many teams, as long as access to pod specs and logs is controlled.

## 341: How do you prevent one tenant from slowing down everyone else (noisy neighbor)?

- **Per-tenant rate limits and quotas** at the gateway and in heavy services.
- **Fair queuing:** separate queues or partitions per tenant (or per tenant tier), and workers that take jobs round-robin across tenants instead of first-in first-out.
- **Concurrency limits per tenant**, so one tenant cannot use all database connections or worker slots.
- **Isolation for big tenants:** move them to their own cell, database or worker pool.
- **Per-tenant metrics**, so you can see who is using what. Be careful with metric cardinality if you have many tenants, and consider only tracking the top ones.

## 342: What are the common multi-tenancy models for microservices?

- **Pool (shared):** all tenants share the same services and databases, separated by a `tenant_id` column. Cheapest and simplest to run, but weaker isolation and noisy neighbor risk.
- **Silo (dedicated):** each tenant gets its own database or even its own deployment. Strong isolation, easy per-tenant backup and data residency, but much more expensive and harder to run at scale.
- **Bridge (mixed):** shared services with separate databases or schemas per tenant, or most tenants pooled with large or regulated tenants in silos.

Most SaaS products start pooled and move premium or regulated tenants to silos later, so the code should not assume one model everywhere.

## 343: How do you keep the API gateway from becoming a single point of failure?

- Run several instances across availability zones behind a load balancer, and autoscale them.
- Keep the gateway stateless, with rate limit counters and config in a highly available store.
- Make sure it fails safely if a dependency like Redis or the auth server is down (for example, verify JWTs locally with cached keys instead of calling the auth server).
- Keep logic in it small, so there is less that can break.
- Roll out gateway config changes gradually, like code.
- Consider separate gateways per domain or client type, so one bad route config does not break everything.

## 344: How do you make a consumer idempotent when the side effect is an external API call?

If the external API supports idempotency keys, use one derived from the message (`event.id` or `orderId + action`). The external system then removes duplicates.

```js
await stripe.refunds.create(
  { payment_intent: event.data.paymentIntentId },
  { idempotencyKey: `refund:${event.id}` },
);
```

If it does not:

1. Record the intent in your database first (`status = 'sending'`), keyed by the message ID.
2. Call the external API.
3. Record the result (`status = 'sent'`, with the external ID).
4. On a redelivery, check the record. If it is `sent`, skip. If it is `sending`, the earlier attempt may or may not have succeeded, so check the external system's state before trying again, or flag it for review.

Some duplicates are acceptable (a duplicate notification). Others, like payments, need this careful handling.

## 345: How do you scale an outbox relay without breaking event order?

With several relay instances and `FOR UPDATE SKIP LOCKED`, two events for the same order can be published by different instances in the wrong order.

Options:

- **One active relay** with leader election. Simple, and often fast enough.
- **Partition the outbox:** add a `partition` column computed from the aggregate ID (`hash(orderId) % 16`). Each relay instance owns some partitions and publishes their rows in order.
- **Lock per aggregate:** select the oldest unsent row per aggregate and skip aggregates that have a row in progress.
- **Use CDC:** Debezium reads the WAL in commit order, and the Kafka message key keeps order per aggregate.

Publish with the aggregate ID as the Kafka key so the order is kept on the broker side too.

## 346: How does the Debezium outbox event router work?

Debezium captures inserts into the outbox table from the database log. Its **outbox event router** transform (an SMT, single message transform) turns each outbox row into a clean Kafka message:

- The `aggregatetype` column decides the target topic (for example `outbox.event.order`).
- The `aggregateid` becomes the message key, so events for one aggregate keep their order.
- The `payload` column becomes the message value.
- Other columns, like the event `id` and `type`, can be added as headers.

Since Debezium reads from the log, you can delete outbox rows right after inserting them (in the same transaction or soon after) to keep the table small. The insert still appears in the log. Consumers must still deduplicate, because Debezium gives at-least-once delivery, for example after a connector restart.

## 347: How do you choose the number of partitions for a Kafka topic?

- Partitions set the maximum parallelism of a consumer group: with 12 partitions, at most 12 consumers in a group do work.
- Estimate throughput: if one consumer handles 500 messages per second and you need 5,000 at peak, you need at least 10 partitions, plus room to grow.
- More partitions mean more files, more memory and longer leader elections. Do not create thousands per topic without reason.
- Adding partitions later is possible, but it changes which partition a key goes to, which breaks per-key ordering for a while and can break consumers that keep local state per key.

A common approach is to pick a number with growth room (like 12, 24 or 48, which divide well across consumers) and plan for a migration to a new topic if you outgrow it.

## 348: How do you process messages in parallel beyond the number of partitions?

Within one partition, you can process messages for **different keys** in parallel and still keep order per key. Keep a small queue per key in memory and only commit an offset when all messages up to it are done.

Libraries do this for you: Confluent's Parallel Consumer for Java is the best-known one. In Node.js you can build it with a map of per-key promise chains:

```js
const chains = new Map();

function processInKeyOrder(key, fn) {
  const prev = chains.get(key) ?? Promise.resolve();
  const next = prev.then(fn, fn);
  chains.set(key, next);
  next.finally(() => {
    if (chains.get(key) === next) chains.delete(key);
  });
  return next;
}
```

The hard part is offset management: you can only commit the lowest offset that is not yet finished, so a crash may reprocess some messages. Handlers must be idempotent.

## 349: How do you retry failed Kafka messages without blocking the partition?

Use retry topics with delays:

1. The main consumer fails on a message and publishes it to `orders.retry.1m` with a header for the attempt number and the original topic, then commits the offset and moves on.
2. A retry consumer reads `orders.retry.1m`, waits until the message is at least one minute old (pausing the partition if needed), then processes it.
3. If it fails again, it goes to `orders.retry.10m`, and after the last attempt to `orders.dlq`.

This keeps the main topic flowing. The cost is that ordering per key is lost for retried messages, which matters if later events for the same key depend on the failed one. Separate errors that can never succeed (bad data) and send them straight to the DLQ.

## 350: How do you replay messages from a dead letter queue safely?

- Find and fix the root cause first, otherwise the replay just fails again.
- Check that the messages are still relevant. Some may refer to entities that changed or were deleted since.
- Make sure consumers are idempotent, because some DLQ messages may have partly succeeded before failing.
- Replay in small batches with rate limits, and watch error rates.
- Keep the original metadata (original topic, offset, first failure time, error) so you can trace what happened.
- Think about ordering: replaying an old `OrderUpdated` after a newer one can overwrite fresh data unless consumers check versions.

Have a tool or script for this ahead of time. Writing one in the middle of an incident is risky.

## 351: What are backward, forward and full compatibility for schemas?

- **Backward compatible:** consumers using the **new** schema can read data written with the **old** schema. You upgrade consumers first. Example: adding a field with a default value.
- **Forward compatible:** consumers using the **old** schema can read data written with the **new** schema. You upgrade producers first. Example: adding a field that old readers ignore.
- **Full compatible:** both at the same time.

Schema registries also have "transitive" versions, which check against all previous versions, not just the last one. This matters for topics with long retention, where a consumer might read very old messages. Full transitive compatibility is the safest choice for events shared between teams.

## 352: What rules do you follow to evolve protobuf messages safely?

- Never change the tag number of an existing field.
- Never reuse a tag number or name from a deleted field. Mark it as `reserved`.
- Do not change a field's type, except between a few documented compatible types.
- Adding fields is safe. Old code ignores unknown fields, and new code sees default values for missing fields.
- In proto3, missing scalars read as default values (0, empty string), so you cannot tell "not set" from "zero" unless you use `optional` or wrapper types.
- Be careful renaming enum values and always have a zero value like `STATUS_UNSPECIFIED`.

```proto
message Order {
  reserved 4;
  reserved "discount_code";
  string id = 1;
  string status = 2;
  int64 total_cents = 3;
  optional string coupon = 5;
}
```

Tools like `buf breaking` check these rules automatically in CI.

## 353: How do you catch breaking contract changes at scale?

With many services and teams, you cannot rely on people noticing. Automate it:

- Store all contracts (OpenAPI, protobuf, event schemas) in version control, ideally in one place with owners.
- Run breaking change checks on every pull request: `buf breaking` for protobuf, OpenAPI diff tools, and schema registry compatibility checks for events.
- Use consumer-driven contract tests with a Pact Broker and `can-i-deploy` checks before deploying.
- Collect real usage: which consumers call which endpoints and read which fields, using gateway logs or tracing data, so you know who will be affected.
- Fail the build on breaking changes unless they come with a new version and a migration plan.

## 354: How do you deprecate and remove an API that many services use?

1. Release the replacement and document how to migrate.
2. Mark the old API as deprecated: in docs, in the OpenAPI spec and with `Deprecation` and `Sunset` response headers.
3. Find every consumer using metrics, logs or traces, and contact their owners with a deadline.
4. Track usage over time on a dashboard.
5. Do brownouts: turn the old API off for short planned windows, so forgotten consumers show up before the final removal.
6. Remove it once usage is zero (or close to zero with an agreed exception).

It usually takes much longer than expected, so plan the timeline in months, not days.

## 355: How do you profile CPU usage of a Node.js service in production?

- **Continuous profiling:** tools like Grafana Pyroscope, Datadog, or other APM profilers sample stack traces with low overhead all the time. You can compare flame graphs before and after a deploy.
- **On demand:** start with `--cpu-prof` to write a `.cpuprofile` on exit, or connect the inspector and record a profile for 30 seconds.
- **Linux tools:** `perf` with `--perf-basic-prof` can profile JavaScript and native code together.

Open profiles as flame graphs and look for wide boxes: functions that use the most time. Common surprises are JSON handling, logging, validation libraries, regex, and crypto running on the main thread. Profile under realistic load, since problems often only appear under pressure.

## 356: How can V8 garbage collection affect a service, and how do you tune it?

V8 has a young generation (new objects, collected often and quickly) and an old generation (long-lived objects, collected less often but with longer work). Services that create many short-lived objects per request, like parsed JSON and strings, put pressure on the young generation. If those objects survive a couple of collections, they move to old space and make major GCs more expensive.

Things to try:

- Measure first: `--trace-gc`, GC metrics from `prom-client` or `PerformanceObserver` with `entryTypes: ['gc']`.
- Raise the young generation size with `--max-semi-space-size` (in MB). This often reduces GC time for request-heavy services at the cost of memory.
- Set `--max-old-space-size` to fit the container.
- Reduce allocation: avoid needless copying, stream large data and cache parsed results.

Test any flag change under load, because the results depend a lot on the workload.

## 357: What are common causes of memory leaks in Node.js microservices?

- Caches without a size limit or TTL (a plain `Map` that keeps growing).
- Event listeners added per request and never removed.
- Timers (`setInterval`) that are never cleared and keep references alive.
- Closures that hold large objects longer than needed.
- Per-request data stored in module-level arrays or objects, for example to "collect metrics".
- Metric labels with unbounded values, which keep creating new series in memory.
- Promises that never settle, for example waiting on a message reply that never comes.
- Unconsumed HTTP response bodies with `fetch`. If you do not read or cancel the body, the connection and memory may stay in use longer than expected.

Use bounded caches like `lru-cache`, clean up in `finally` blocks and compare heap snapshots over time to find what grows.

## 358: How do you find out if GC pauses are causing latency spikes?

1. Compare latency spikes with GC metrics (`nodejs_gc_duration_seconds` from `prom-client`) and event loop delay on the same timeline.
2. Run with `--trace-gc` in a test environment under load to see how long each collection takes.
3. Look at memory: if heap use is close to the limit, V8 runs major GCs more often and they take longer.
4. Check CPU throttling: a container that hits its CPU limit makes GC (which runs partly on extra threads) slower.

If GC is the cause, reduce allocation in hot paths, give the heap more room, tune semi-space size or move large in-memory data (like big lookup tables) out of the heap or into a separate service.

## 359: How expensive is JSON serialization in a Node.js service and how do you reduce it?

`JSON.parse` and `JSON.stringify` are fast but synchronous. With large payloads (hundreds of KB or MB), each call can block the event loop for milliseconds, and in a gateway or BFF that passes big responses around, this adds up quickly.

Ways to reduce it:

- Keep payloads small: return only needed fields and paginate.
- Use schema-based serialization, like Fastify's response schemas with `fast-json-stringify`, which can be much faster for known shapes.
- Do not parse and re-serialize data you only pass through. Stream it instead.
- Use binary formats like protobuf between internal services when payloads are large or frequent.
- Do not log big objects. Logging serializes them too.

## 360: What are the signs of an exhausted HTTP connection pool, and how do you fix it?

Signs:

- Latency of outgoing calls goes up, but the downstream service says its own latency is fine.
- Time is spent before the request is even sent (visible in traces as a gap before the HTTP span starts, or in undici's dispatcher stats).
- Timeouts increase under load while CPU is low.

Causes: the pool is too small for the concurrency, slow downstream responses keep connections busy, or response bodies that are never read keep connections from going back to the pool.

Fixes: always read or cancel response bodies (`await res.body?.cancel()`), set reasonable timeouts so stuck requests release connections, increase `connections` on the undici `Agent` if the downstream can handle it, and limit concurrency in your own code so you do not queue thousands of calls at once.

## 361: How can DNS lookups become a bottleneck in Node.js?

By default, `http` and `fetch` resolve hostnames with `dns.lookup`, which calls the OS resolver (`getaddrinfo`) on the libuv thread pool. The pool has only 4 threads by default, shared with file system calls, some crypto and zlib. Under heavy load with many new connections, DNS lookups can queue behind other work, and Node does not cache DNS results itself.

In Kubernetes, the default `ndots:5` setting also makes each lookup of a short name try several search domains first, which multiplies DNS queries.

Fixes:

- Reuse connections with keep-alive, so lookups happen rarely.
- Use fully qualified names with a trailing dot (`orders.prod.svc.cluster.local.`) or lower `ndots`.
- Run a node-local DNS cache in the cluster.
- Increase `UV_THREADPOOL_SIZE` if the pool is busy with other work.
- Cache lookups in the app (for example with `cacheable-lookup`), keeping TTLs short so you notice changes.

## 362: What is the libuv thread pool and how can it limit a service?

libuv runs some operations that cannot be done asynchronously by the OS on a small thread pool: most `fs` calls, `dns.lookup`, `crypto.pbkdf2`, `crypto.scrypt`, `crypto.randomBytes` (async version) and `zlib` compression. The default size is 4 threads.

If a service does a lot of password hashing, compression or file I/O, those tasks wait for a free thread, and unrelated things like DNS lookups wait behind them. Latency goes up while CPU might not look fully used.

You can raise it with the `UV_THREADPOOL_SIZE` environment variable (up to 1024), set before the process starts. Larger is not always better on a container with 1-2 CPUs. For heavy CPU work like hashing, a separate worker pool or service is often a better fix.

## 363: Why do you get intermittent ECONNRESET errors between services, and how do you fix them?

A very common cause is a keep-alive timeout mismatch. The client keeps an idle connection open to reuse it. The server (or a load balancer between them) closes idle connections after its own timeout. If the client sends a request on a connection at the same moment the server closes it, the request fails with `ECONNRESET` or "socket hang up".

Fixes:

- Make the client's idle timeout shorter than the server's and every proxy's idle timeout.
- Make the Node server's `keepAliveTimeout` longer than the load balancer's idle timeout (for example, AWS ALB uses 60 seconds by default), and `headersTimeout` a bit longer than `keepAliveTimeout`.
- Retry idempotent requests once on `ECONNRESET`.

```js
const server = app.listen(3000);
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000;
```

## 364: Which server timeouts in Node.js should you configure?

- `server.requestTimeout` (default 300 seconds since Node 18): maximum time to receive the whole request. Protects against slow uploads tying up sockets.
- `server.headersTimeout` (default 60 seconds): maximum time to receive the request headers. Protects against slowloris-style attacks.
- `server.keepAliveTimeout` (default 5 seconds): how long an idle keep-alive connection stays open.
- `server.timeout` (default 0, meaning off): socket inactivity timeout.

Node itself does not limit how long your handler takes to respond. Add your own per-request timeout, for example by passing an `AbortSignal` to downstream calls, and return `503` or `504` when it runs out. Set timeouts at the load balancer as well, so slow clients are cut off before they reach Node.

## 365: How do you protect a Node.js service from slow client attacks?

Slow client attacks (slowloris, slow POST) open many connections and send data very slowly, so each connection stays open and uses resources.

- Put a reverse proxy or load balancer in front that buffers requests and has strict timeouts. NGINX, Envoy and cloud load balancers handle this better than Node.
- Keep Node's `headersTimeout` and `requestTimeout` at reasonable values.
- Limit body sizes and the number of headers.
- Limit connections per IP at the edge.
- Use `server.maxRequestsPerSocket` if you want connections to be recycled.

Internal services behind a gateway are less exposed, but they should still have timeouts, since a bug in another service can behave like an attack.

## 366: Cluster module, worker threads or more pods: how do you choose?

- **More pods (one Node process each):** the default in Kubernetes. The orchestrator handles health checks, restarts and scaling, and each process is simple. Costs a bit more memory per process because each has its own runtime.
- **Cluster module or PM2 cluster mode:** several Node processes in one container or VM sharing a port. Useful on VMs with many cores where you do not have an orchestrator. In Kubernetes it hides per-process health from the platform and makes resource limits harder to set.
- **Worker threads:** threads inside one process for CPU-heavy tasks. They share memory through `SharedArrayBuffer` and can pass data cheaply. Use them to keep the main event loop free, not to handle more HTTP connections.

A common setup: one process per pod with about 1 CPU, scale with pod count, and a worker thread pool only for CPU-heavy parts.

## 367: How does CPU throttling in containers affect Node.js?

Kubernetes CPU limits are enforced with CFS quotas: a container with a 1 CPU limit can use 100 ms of CPU time per 100 ms period. Node uses several threads at once (the main thread, GC threads, libuv threads). In a burst, those threads can use up the whole quota early in the period, and then all of them are paused until the next period. The result is latency spikes of tens of milliseconds even when average CPU looks low.

What to do:

- Watch `container_cpu_cfs_throttled_periods_total` and related metrics.
- Remove CPU limits or set them well above requests, if your cluster policy allows.
- Do not set very low limits like `250m` for latency-sensitive services.
- Make sure `os.availableParallelism()` and thread pool sizes are not much higher than the CPU you actually get.

## 368: What are common autoscaling pitfalls for Node.js services?

- **Scaling on CPU only:** an I/O-bound service may have low CPU while its event loop or connection pool is saturated. Consider event loop delay, concurrency or request rate as metrics.
- **Queue consumers scaled by CPU:** scale them by queue length or consumer lag instead (KEDA).
- **Slow scale-up:** new pods need time to start, warm caches and pass readiness. By the time they are ready, the spike may have caused errors. Keep a minimum headroom and use faster startup.
- **Too aggressive scale-down:** pods are removed and added in a loop. Use stabilization windows.
- **Kafka consumers above partition count:** extra pods sit idle, and each scale event triggers a rebalance.
- **Downstream limits:** scaling out a service also multiplies database connections and calls to other services, which can move the bottleneck instead of fixing it.

## 369: Why can a fresh deployment be slow at first, and how do you warm up a service?

New instances start with empty in-memory caches, cold connection pools, JIT that has not optimized hot code yet, and lazy-loaded modules not loaded yet. The first requests are slower, and with a large rollout, a whole fleet of cold instances can hit the database at once.

Ways to warm up:

- Open database and broker connections before reporting ready.
- Preload important cache entries or config at startup.
- Send a few synthetic requests to the main endpoints before marking the pod ready.
- Use a shared cache (Redis) so a new instance does not start completely cold.
- Roll out gradually (`maxSurge` limits) and use `minReadySeconds`, so the database is not hit by all new pods together.
- Some load balancers support "slow start", sending a growing share of traffic to new instances.

## 370: How do you avoid connection storms when many instances start at once?

When dozens of pods start together (after a deploy, a node failure or a scale-up), they all open database, Redis and broker connections and run startup queries at the same moment. That can overload the dependencies.

- Add random jitter to startup and reconnect delays.
- Open pools lazily with a small minimum size and grow as needed.
- Use exponential backoff with jitter for reconnects after an outage, so instances do not reconnect in sync.
- Put a connection pooler (PgBouncer, RDS Proxy) between the services and the database.
- Limit rollout speed with `maxSurge`.

## 371: How do you shut down a Kafka consumer without losing or duplicating too much work?

1. On `SIGTERM`, stop accepting new HTTP traffic if the process also serves HTTP.
2. Call `consumer.disconnect()` (kafkajs) or `consumer.stop()`. It stops fetching, waits for the current `eachMessage` or `eachBatch` handlers to finish, commits offsets and leaves the group cleanly, so partitions are reassigned quickly.
3. Make sure handlers finish within the grace period. Long batch handlers should check `isRunning()` and stop early.
4. Then close other connections and exit.

```js
process.once("SIGTERM", async () => {
  try {
    await consumer.disconnect();
    await producer.disconnect();
  } finally {
    process.exit(0);
  }
});
```

If the process is killed before the commit, the last messages are processed again by another consumer, which is fine if handlers are idempotent. Static membership plus a quick restart can avoid a full rebalance during rolling updates.

## 372: How do you deploy a WebSocket service without dropping every connection?

WebSocket connections are long-lived, so a rolling update cuts them. To make this smooth:

- On `SIGTERM`, stop accepting new connections, then close existing ones gradually over the grace period instead of all at once, using a close code that tells clients to reconnect.
- Make clients reconnect with exponential backoff and jitter, so a deploy does not cause all clients to reconnect in the same second.
- Keep session state outside the instance (in Redis or the database), so the client can resume on any instance and fetch missed messages using the last event ID it saw.
- Raise `terminationGracePeriodSeconds` for these pods if you need more time to drain.

## 373: How do you scale WebSocket servers across many instances?

Each client is connected to one instance, but messages for that client can come from anywhere. You need a way to route messages to the right instance:

- **Pub/sub backplane:** every instance subscribes to Redis pub/sub, Redis Streams or NATS. When a message for user X arrives, it is published, and the instance holding X's connection sends it. Socket.IO has a Redis adapter (and a Redis Streams adapter) for this.
- **Connection registry:** store which instance holds which user, and send messages directly to that instance.
- **Managed services:** AWS API Gateway WebSockets, Azure Web PubSub or Ably handle connections for you, and your services just call an API to send messages.

Also tune limits for many open connections: file descriptors, memory per connection and load balancer idle timeouts.

## 374: How do you keep observability costs under control with many services?

- **Traces:** use sampling, tail-based in the collector, keeping errors and slow traces and a small share of the rest.
- **Logs:** log at `info` or higher in production, avoid logging every request body, drop noisy health check logs and set shorter retention for debug data.
- **Metrics:** watch cardinality, remove unused metrics and avoid per-user or per-ID labels.
- **Route data by value:** send everything to cheap storage (object storage) and only important data to the expensive, fast-query backend.
- Use the OpenTelemetry Collector as a central place to filter, sample and route data before it reaches a vendor.
- Show each team what their services cost in telemetry. Visibility changes behaviour.

## 375: What are exemplars and how do they help?

An exemplar is a sample trace ID attached to a metric data point. For example, a latency histogram bucket for "over 2 seconds" can carry the trace ID of one request that fell into that bucket.

In Grafana, you see dots on a latency graph, click one and jump straight to the trace that shows why that request was slow. It connects "something is slow" (metrics) with "here is a slow request" (traces) without searching. Prometheus supports exemplars with the OpenMetrics format, and `prom-client` and OpenTelemetry metrics can record them.

## 376: How does tracing work across a message broker?

The producer puts the trace context (`traceparent`) into message headers. The consumer extracts it when it processes the message.

Because a message can be consumed much later, or by many consumers, and a batch can contain messages from many traces, OpenTelemetry messaging conventions often use **span links** instead of a plain parent-child relation. The consumer's span links to the producer's span, so you can navigate between them without one trace lasting for hours.

```js
import { context, propagation, trace } from "@opentelemetry/api";

// producer
const headers = {};
propagation.inject(context.active(), headers);
await producer.send({ topic: "orders", messages: [{ key, value, headers }] });

// consumer
const parentCtx = propagation.extract(
  context.active(),
  toStringHeaders(message.headers),
);
const linkCtx = trace.getSpanContext(parentCtx);
tracer.startActiveSpan(
  "process order",
  { links: linkCtx ? [{ context: linkCtx }] : [] },
  async (span) => {
    try {
      await handle(message);
    } finally {
      span.end();
    }
  },
);
```

Kafka headers arrive as Buffers, so `toStringHeaders` converts them to strings first. Auto-instrumentation for kafkajs and amqplib can do this for you.

## 377: Why does trace context sometimes get lost in Node.js, and how do you fix it?

OpenTelemetry tracks the active span through `AsyncLocalStorage`. Context can get lost when:

- A library uses its own connection pool or queue and runs callbacks outside the original async context (some older database drivers and custom event emitters).
- Code uses callback-based APIs that are not instrumented.
- Work is scheduled in one request and runs later in a shared batch, like a manual batching layer.
- The instrumentation file is loaded after the libraries, so they were never patched.
- ESM loader hooks were not registered, so ESM imports were not instrumented.

Fixes: load instrumentation first with `--import`, keep libraries at versions supported by the instrumentation, and where a library breaks context, bind it by hand with `context.with(ctx, fn)` or `AsyncResource.bind()`. Tests that check spans have the right parent catch regressions.

## 378: How do you connect logs with traces?

Add the active trace ID and span ID to every log line. With OpenTelemetry, `@opentelemetry/instrumentation-pino` (part of the auto-instrumentations) injects `trace_id` and `span_id` into Pino logs automatically, and it can also send logs through the OpenTelemetry logs pipeline.

By hand:

```js
import { trace } from "@opentelemetry/api";

const logger = pino({
  mixin() {
    const span = trace.getActiveSpan();
    if (!span) return {};
    const { traceId, spanId } = span.spanContext();
    return { trace_id: traceId, span_id: spanId };
  },
});
```

Then you can jump from a trace to its logs and back in tools like Grafana or most APM vendors.

## 379: What are burn-rate alerts for SLOs?

A burn rate says how fast you are using up your error budget. A burn rate of 1 means you will use exactly the whole budget over the SLO window (for example 30 days). A burn rate of 14.4 means you would use it all in about 2 days.

Instead of alerting on "error rate above X for 5 minutes", you alert when the burn rate is high over two windows at once, for example:

- Page: burn rate above 14.4 over the last 1 hour **and** the last 5 minutes (fast, serious problem).
- Ticket: burn rate above 1 to 3 over the last few days (slow problem).

Using a long and a short window together means alerts fire quickly for big problems and stop quickly when they are fixed, with far fewer false alarms than fixed thresholds. This approach comes from the Google SRE workbook.

## 380: What is synthetic monitoring and why add it?

Synthetic monitoring runs scripted requests or user flows against your system on a schedule, from outside, for example "log in, add an item to the cart, start checkout" every minute from several regions.

It catches problems that internal metrics miss: DNS or certificate issues, broken routing at the edge, a flow that fails because of a bug across several services, or a region that is unreachable. It also tells you about problems at night when there is little real traffic. Tools include Checkly, Grafana synthetic monitoring, Datadog Synthetics and Playwright-based scripts.

## 381: How would you handle an incident where failures are cascading across services?

1. **Stop the bleeding first.** Find the first service that started failing (traces and dependency graphs help) and reduce load on it: turn on load shedding, open circuit breakers, turn off non-critical features with flags or scale it up if the cause is capacity.
2. **Roll back** recent changes in the affected path if a deploy or config change is likely the cause.
3. **Stop retries** that make it worse, for example by lowering retry settings or pausing consumers.
4. **Recover gradually.** Bring traffic back step by step so the recovering service is not hit by a thundering herd.
5. **Communicate** with a clear incident lead and regular updates.
6. **Afterwards,** run a blameless review and add the missing safeguards: timeouts, budgets, bulkheads, alerts.

## 382: How do you find the critical path and weak spots in a microservices system?

- Build a dependency graph from tracing data (most tracing tools have a service map) instead of relying on diagrams that may be outdated.
- For each key user flow (login, search, checkout), list the services it needs synchronously. Every one of them multiplies the risk of failure: five services at 99.9% each give about 99.5% for the flow.
- Mark which dependencies are hard (the flow fails without them) and which are soft (degrades). Turn hard ones into soft ones where you can, with caches, fallbacks or async processing.
- Look for single points of failure: one database, one Redis, one gateway, one region.
- Run game days to test what really happens when each one fails.

## 383: Why are circular dependencies between services a problem?

If service A calls B and B calls A (directly or through others), then:

- Neither can start or be deployed safely without the other being available.
- A slowdown in one feeds back into the other, which can cause both to lock up as their connection pools fill with requests waiting on each other.
- Changes to the contract between them need careful coordination in both directions.
- It is often a sign that the boundary between them is wrong.

Fixes: merge them if they are really one context, move the shared part into a third service, or replace one direction with events (B listens to A's events instead of calling it). Tracing-based service maps help find cycles.

## 384: When should you merge microservices back together?

Signs that services should be merged:

- They are almost always changed and deployed together.
- They make many chatty calls to each other for every request.
- They share data in a way that needs constant syncing.
- The same team owns both, and there is no scaling or isolation reason to keep them apart.
- Most of the incidents between them come from the network or consistency between them.

Merging is a normal, healthy refactor, not a failure. Do it like any other migration: create the combined service, move the traffic step by step and remove the old ones.

## 385: How do you find service boundaries in a new or existing domain?

- **Event storming:** a workshop where developers and domain experts map the business process as a timeline of domain events on sticky notes. Clusters of events, commands and the language used around them show natural bounded contexts.
- **Look at the business organization:** departments and capabilities (billing, fulfillment, support) often map to contexts.
- **Look at change history:** in an existing codebase, files that always change together belong together. Tools that analyse Git history can show this coupling.
- **Look at data:** which data is written together in one transaction, and which is only read from elsewhere.

Start with bigger services, and split further only when there is a clear benefit.

## 386: What is event storming?

Event storming is a workshop technique by Alberto Brandolini to explore a business domain quickly. Participants, both developers and domain experts, put domain events on a long wall in time order using orange sticky notes, such as "Order placed", "Payment failed", "Parcel shipped".

Then they add commands that trigger events, the people or systems that issue them, policies ("when payment fails, notify the customer"), read models, external systems and hotspots (open questions or conflicts).

The result shows the real process, where different parts of the business use different words for the same thing and where natural boundaries are. It is a common first step when designing microservices or planning to split a monolith.

## 387: What is an anti-corruption layer?

An anti-corruption layer (ACL) is a translation layer between your service and another system whose model you do not want leaking into your code, usually a legacy system or an external vendor API.

Your service talks only to the ACL, using your own domain model. The ACL translates calls and data to and from the other system's model.

```js
// acl/legacyCustomerAdapter.js
export async function getCustomer(id) {
  const raw = await legacyClient.get(`/CUST_MASTER?CUST_NO=${id}`);
  return {
    id: String(raw.CUST_NO),
    name: `${raw.FNAME} ${raw.LNAME}`.trim(),
    email: raw.EMAIL_ADDR?.toLowerCase() ?? null,
    isActive: raw.STATUS_CD === "A",
  };
}
```

This keeps your domain clean, and when the legacy system is replaced, only the ACL changes. It is very useful during a strangler fig migration.

## 388: What are "published language" and "shared kernel" in DDD, and how do they apply to services?

- **Published language:** a well-documented, shared format that bounded contexts use to communicate, like a set of event schemas or an OpenAPI spec. Each service keeps its own internal model and translates to and from the published language. This is how most microservices should communicate.
- **Shared kernel:** two contexts share a small part of the model in code, like a common library with some types. Changes need agreement between both teams.

In microservices, a published language is usually preferred. A shared kernel creates tight coupling and should be kept very small and stable, if it is used at all.

## 389: Should internal and external APIs be versioned the same way?

Usually not.

**External (public) APIs** have consumers you do not control and cannot contact easily. They need stable versions, long deprecation periods, changelogs and very careful compatibility. Date-based or major version URLs are common.

**Internal APIs** have consumers you can find and talk to. Prefer backward compatible changes, with contract tests and usage tracking, and migrate consumers quickly instead of keeping many versions alive. Keeping v1, v2 and v3 of an internal API running for years is a cost that is rarely worth it.

A gateway or BFF can also shield external clients from internal changes, so internal APIs can move faster.

## 390: What dependency policies help in a large Node.js microservices monorepo?

- **Single version policy:** every service uses the same version of each third-party package. It avoids subtle bugs from mixing versions and makes upgrades one PR, but big upgrades must be done for all services at once.
- **Version catalogs** (pnpm catalogs) define versions in one place while still letting packages declare what they use.
- **Module boundaries:** enforce with lint rules (Nx module boundary rules or dependency-cruiser) that apps cannot import from other apps and that domain packages cannot depend on infrastructure packages.
- **Ownership:** a `CODEOWNERS` file so changes to shared packages are reviewed by their owners.
- **Automated updates:** Renovate with grouping rules so related packages are upgraded together.

## 391: What is platform engineering and how does it relate to microservices?

Platform engineering is building an internal developer platform (IDP): a set of tools and services that product teams use to build, deploy and run their services without each team doing it from scratch. It typically includes service templates, CI/CD pipelines, Kubernetes setups, observability, secrets management and a portal like Backstage.

With microservices, each team would otherwise need to know Kubernetes, Helm, Terraform, tracing and more. A good platform hides much of that behind a "golden path", so teams can focus on their domain. The platform team treats other developers as its customers and measures success by adoption and developer productivity.

## 392: What is traffic shadowing (mirroring) and when do you use it?

Traffic shadowing copies real production requests to a new version of a service in the background. The users still get responses from the current version, and the responses from the shadow version are thrown away, or compared with the real ones.

It is useful for:

- Testing a rewrite (for example, a service extracted from the monolith) with real traffic.
- Load testing a new version with realistic patterns.
- Checking a new database or library under real queries.

The big risk is side effects: the shadow must not send emails, charge cards or write to shared databases. Mirror only reads, or point the shadow at its own isolated dependencies. Service meshes and proxies like Envoy and Istio support mirroring.

## 393: How does automated canary analysis work?

During a canary release, a tool compares metrics of the canary version with the baseline (current version) running at the same time with similar traffic:

- Error rate
- Latency percentiles
- Saturation (CPU, memory, event loop delay)
- Business metrics, like checkout success rate

If the canary is significantly worse, the rollout stops and traffic goes back to the old version automatically. If it looks fine at each step (5%, 25%, 50%), it continues.

Argo Rollouts and Flagger do this with Prometheus or other metric providers. Comparing with a baseline at the same time is better than comparing with yesterday, because traffic patterns change during the day.

## 394: How do you run schema migrations on very large tables without downtime?

- Avoid operations that lock the table for a long time. In PostgreSQL, adding a column with a default is fast in recent versions, but adding an index needs `CREATE INDEX CONCURRENTLY`, and adding a foreign key or check constraint should use `NOT VALID` followed by `VALIDATE CONSTRAINT`.
- Set `lock_timeout` in migrations so a migration that cannot get a lock fails fast instead of blocking all queries behind it.
- Use expand and contract to split breaking changes into compatible steps.
- Backfill data in small batches with pauses, not one huge `UPDATE`.
- For MySQL, tools like `gh-ost` or `pt-online-schema-change` copy the table in the background.
- Test the migration on a copy of production-sized data first to know how long it takes.

## 395: How do you backfill data across services at scale?

For example, a new field must be filled for 200 million existing records, or a new service needs historical data from another.

- Write the backfill as a resumable job: process in batches by ID range, store the last processed position and make each batch idempotent.
- Rate limit it and run it at low-traffic times, or give it its own lower-priority resources, so it does not hurt live traffic.
- Read from replicas or a data export instead of the live primary when you can.
- For data from another service, prefer a bulk export endpoint, a snapshot file or replaying its events over calling its normal API millions of times.
- Keep live updates flowing during the backfill (events or CDC), and handle the overlap where the same record arrives from both.
- Check results with counts and sample comparisons when done.

## 396: What are reconciliation jobs and why do distributed systems need them?

A reconciliation job compares data between systems that should agree and fixes or reports differences. For example, comparing payments in your database with the payment provider's records, or orders in the orders service with shipments in the shipping service.

Even with outbox, idempotency and retries, things drift: bugs, manual fixes, lost messages before a fix was deployed, edge cases nobody thought of. A daily or hourly reconciliation catches these before customers or the finance team do. It is especially important for money, inventory and anything with legal or contractual value.

## 397: How should a microservice handle money?

- Store amounts as integers in the smallest unit (cents) or with a decimal type, never as JavaScript floating point numbers. `0.1 + 0.2` is not `0.3`.
- Always store the currency with the amount.
- Use idempotency keys for every operation that moves money.
- Keep a ledger: an append-only list of entries (double-entry if possible) instead of only updating a balance field. The balance is the sum of the entries.
- Never delete or edit ledger entries. Corrections are new entries.
- Run reconciliation with payment providers and banks.
- Be explicit about rounding rules, and do conversion and tax calculations in one service.

```js
const totalCents = items.reduce((sum, i) => sum + i.priceCents * i.quantity, 0);
```

For amounts beyond `Number.MAX_SAFE_INTEGER` or for precise decimal math, use `BigInt` or a decimal library.

## 398: A call to the payment provider timed out. Did the payment happen? How do you handle it?

You do not know. The request might not have reached the provider, it might have been processed and the response lost, or it might still be processing. Treating it as failed could lead to double charging if the user retries, and treating it as success could ship unpaid orders.

The safe approach:

1. Send every payment request with an idempotency key tied to the order or payment attempt.
2. On timeout, mark the payment as `UNKNOWN`, not as failed.
3. Retry with the same idempotency key, or query the provider for the status of that payment.
4. Rely on the provider's webhook as another source of the final result.
5. Have a reconciliation job for payments stuck in `UNKNOWN`.

Tell the user that the payment is being processed instead of showing an error.

## 399: How do you prevent overselling inventory across services?

- Make the inventory service the only owner of stock levels.
- Reserve stock with an atomic, conditional update, so two orders cannot take the last item:

```sql
UPDATE stock SET available = available - $1, reserved = reserved + $1
WHERE sku = $2 AND available >= $1;
```

If no row is updated, the stock is not available.

- Give reservations an expiry, so stock from abandoned checkouts is released (a scheduled job or delayed message cancels them).
- Confirm the reservation when the payment succeeds, and release it when the saga fails.
- For very hot items, avoid row lock contention by splitting stock into several rows (buckets) or by queuing reservations for that SKU through one worker.
- Decide what is acceptable for your business: some shops allow a small oversell and handle it with backorders.

## 400: How would you design for a flash sale with a huge traffic spike?

- **Protect the core:** put a queue or virtual waiting room in front of checkout, so only as many users enter as the system can handle.
- **Pre-scale** services, databases and caches before the event instead of relying on autoscaling.
- **Cache aggressively:** product pages and stock counts (approximate) from a CDN or Redis.
- **Make inventory fast:** keep sale stock in Redis with atomic decrements (a Lua script or `DECRBY` with a check), then write the order asynchronously to the database.
- **Process orders asynchronously:** accept the order, return "processing" and handle payment through a queue.
- **Rate limit** per user to stop bots, and add bot protection.
- **Turn off non-essential features** (recommendations, reviews) with feature flags.
- **Load test** the whole flow at the expected peak before the event.

## 401: How do you respect a third-party API rate limit shared by many instances of your service?

If the provider allows 100 requests per second for your whole account and you run 10 instances, each instance limiting itself to 100 per second is not enough. The limit has to be shared.

- **Central limiter:** keep a token bucket in Redis (a Lua script that refills and takes tokens atomically) and have every instance take a token before each call.
- **Single worker queue:** send all calls to that provider through a queue with a rate-limited consumer. BullMQ has a built-in `limiter` option on workers that applies across all workers of a queue.
- **Static split:** give each instance `limit / instances`. Simple, but breaks when you autoscale.

```js
const worker = new Worker("crm-sync", syncToCrm, {
  connection,
  limiter: { max: 100, duration: 1000 },
});
```

Also handle `429` responses: respect `Retry-After`, back off and alert if you hit the limit often, because it means your usage is close to the plan's limit.

## 402: What is queue-based load leveling?

Queue-based load leveling puts a queue between a source of bursty work and the service that does it. Producers can add work as fast as they want, and the consumer processes it at a steady rate it can handle.

It turns a spike that would overload the service into a queue that grows for a while and then drains. You trade latency for stability: work is done a bit later instead of failing. It only works for tasks that do not need an immediate answer, and you should monitor queue age and length so you know when the consumers cannot keep up even on average.

## 403: How do you handle priorities in queues without starving low-priority work?

- **Separate queues per priority** with separate consumers, or with consumers that read from the high queue more often (weighted round robin), for example 4 high, 2 normal, 1 low.
- **Broker priority features:** RabbitMQ supports priority on classic queues (`x-max-priority`), and quorum queues have a simpler priority mode. BullMQ jobs take a `priority` option.
- **Aging:** raise the priority of jobs that have waited too long.
- **Reserved capacity:** keep some workers that only handle high-priority work, so a flood of low-priority jobs cannot block urgent ones.

Strict priority (always take high first) can leave low-priority work waiting forever during busy periods. Weighted schemes avoid that.

## 404: How do you choose between batch processing and stream processing?

**Batch** processes a set of data at once on a schedule, for example a nightly job that computes invoices. It is simpler, easier to rerun and works well for reporting and heavy computations where an hour or a day of delay is fine.

**Stream** processes each event as it arrives, for example updating a fraud score or a dashboard within seconds. It gives fresh results but is harder to build, test and fix, especially with state, windows and late events.

Choose based on how fresh the result must be and how complex the logic is. Many systems do both: streams for live views, and batch jobs that recompute the exact numbers later and fix any drift.

## 405: What problems come with caching at several layers?

A request might pass through a CDN cache, the gateway's cache, a BFF in-memory cache, a Redis cache in the service and the database's own buffer cache. Problems:

- **Stale data adds up:** if each layer has a 60 second TTL, data can be several minutes old in total.
- **Invalidation is hard:** clearing Redis does not clear the CDN or another instance's memory.
- **Debugging:** it is hard to know which layer served an old value.
- **Inconsistent views:** two users can see different data depending on which caches they hit.

Keep the number of layers small, define who owns invalidation for each, set TTLs with the total delay in mind, add headers like `Age` or a custom `x-cache` to show where a response came from, and avoid caching personal data in shared caches.

## 406: What is cache penetration and how do you prevent it?

Cache penetration happens when requests ask for keys that do not exist, so they always miss the cache and always hit the database. This can happen by accident (a buggy client) or on purpose (an attacker requesting random IDs).

Fixes:

- **Negative caching:** store "not found" results for a short time.

```js
const NOT_FOUND = "__nf__";
const cached = await redis.get(key);
if (cached === NOT_FOUND) return null;
if (cached) return JSON.parse(cached);

const row = await db.find(id);
await redis.set(
  key,
  row ? JSON.stringify(row) : NOT_FOUND,
  "EX",
  row ? 300 : 30,
);
return row;
```

- **Validate IDs** before looking them up (format, range).
- **Bloom filters** that tell you quickly if an ID can possibly exist.
- **Rate limiting** clients that cause many misses.

## 407: How do you deal with hot keys in Redis?

A hot key is a single key that gets a huge share of traffic, like a popular product or a global config value. In Redis Cluster, a key lives on one shard, so that shard gets overloaded while others are idle.

Options:

- Cache the hot value in each service instance's memory for a short time (a second or two), so most reads never reach Redis.
- Split the key into several copies (`product:42:copy:0` to `copy:7`) and read a random one. Writes update all copies.
- Use read replicas for read-heavy keys.
- For hot counters, use several counter keys and sum them when reading.

Find hot keys with `redis-cli --hotkeys` (needs an LFU eviction policy) or by monitoring per-shard load.

## 408: What happens to your services if Redis goes down, and how should they behave?

It depends on what Redis is used for:

- **Cache:** services should fall back to the database, with timeouts on Redis calls so a slow Redis does not slow every request. Watch out for the database being overloaded by the sudden extra traffic.
- **Rate limiting:** decide in advance whether to fail open (allow requests) or fail closed (reject). For most APIs, failing open for a short time is better than rejecting everyone.
- **Sessions:** users may get logged out. Consider tokens instead of server sessions.
- **Locks and queues (BullMQ):** jobs stop being processed. They resume when Redis comes back, if data was persisted.

Use short command timeouts, limit the client's offline queue (in ioredis, `maxRetriesPerRequest` and `enableOfflineQueue`), and run Redis with replication and automatic failover (Sentinel, Cluster or a managed service).

## 409: What happens to producers and consumers when a Kafka broker fails?

Each partition has a leader broker and follower replicas. When a broker fails:

- For partitions it led, a new leader is elected from the in-sync replicas (ISR). Producers and consumers get errors briefly, refresh their metadata and continue with the new leader. Clients retry this automatically.
- With `acks=all` and `min.insync.replicas=2` on a topic with 3 replicas, writes continue as long as 2 replicas are in sync. If too many replicas are lost, producers get `NOT_ENOUGH_REPLICAS` errors and writes stop, which protects against data loss.
- `unclean.leader.election.enable=false` (the default) stops an out-of-date replica from becoming leader. Turning it on keeps the partition available but can lose committed messages.

Producers should have enough retries and a delivery timeout that covers a leader election, and services should handle a short pause in publishing, for example with an outbox.

## 410: What are RabbitMQ memory and disk alarms, and how do they affect publishers?

When a RabbitMQ node uses more memory than its high watermark, or free disk space falls below its limit, it raises an alarm and **blocks all publishing connections** across the cluster until the alarm clears. Consumers keep working, so queues can drain.

For Node.js publishers this means `publish` calls stop being confirmed and can hang. amqplib emits `blocked` and `unblocked` events on the connection:

```js
conn.on("blocked", (reason) =>
  logger.warn({ reason }, "rabbitmq blocked publishing"),
);
conn.on("unblocked", () => logger.info("rabbitmq unblocked"));
```

Handle it with publish timeouts, an outbox or local buffer with a size limit, and alerts on queue depth. The real fix is usually consumers that are too slow or queues with no consumer at all, which keep growing until they fill memory.

## 411: How do you change configuration at runtime without restarting services?

- **Watch mounted files:** Kubernetes updates mounted ConfigMaps and Secrets after a delay. The service can watch the file (`fs.watch`) or reload it on a timer, validate it and swap it in.
- **Config service with push or polling:** Consul, etcd, AWS AppConfig or a feature flag service. The service subscribes or polls for changes.
- **Signal-based reload:** reload config on `SIGHUP`.

Rules that make it safe:

- Validate the new config completely before using it, and keep the old one if it is invalid.
- Swap the whole config object at once, so code never sees half-updated values.
- Log every change with old and new versions.
- Roll config changes out gradually, like code. Bad config has caused many big outages.

Some settings, like pool sizes or ports, are hard to change live and are better left to a restart.

## 412: What is a kill switch and how do you design one?

A kill switch is a flag that turns off a feature or a dependency immediately, without a deploy, when it is causing trouble. Examples: turn off recommendations when the recommendation service is overloaded, stop a background sync that is hammering the database, or disable a new payment method.

Design tips:

- Decide ahead of time what the system does when the switch is off (a fallback path), and test that path.
- Make the switch fast to flip and fast to take effect, with flag values cached locally and refreshed every few seconds.
- If the flag service is down, use the last known value or a safe default.
- List kill switches in runbooks so on-call engineers know they exist.

## 413: What is the difference between north-south and east-west traffic, and what handles each?

**North-south** traffic goes in and out of your system: from users, partners and the internet to your services. It is usually handled by a CDN, a load balancer and an API gateway, with a focus on authentication of end users, rate limiting, TLS and protection against attacks.

**East-west** traffic is between your own services inside the system. It is usually handled by service discovery, internal load balancing and often a service mesh, with a focus on service identity (mTLS), retries, timeouts, observability and access policies between services.

The tools overlap (Envoy can do both), but the concerns and owners are often different.

## 414: When are serverless functions cheaper than containers, and when are they more expensive?

Serverless is usually cheaper when:

- Traffic is low, spiky or irregular, since you pay nothing when idle.
- You have many small, rarely used services.
- The team is small and you want to avoid running clusters.

Containers are usually cheaper when:

- Traffic is steady and high. Paying per request or per millisecond adds up, while a well-used container runs at a flat cost.
- Requests are long or need lots of memory.
- You need long-lived connections (WebSockets, database pools, Kafka consumers).

Also count indirect costs: API gateway fees, NAT gateways, logs and the engineering time to run Kubernetes. Many companies mix both: containers for core high-traffic services and functions for event handlers and glue code.

## 415: How do Node.js services work with services written in other languages?

Keep everything that crosses service boundaries language-neutral:

- **Contracts:** OpenAPI, protobuf or JSON Schema, with code generated for each language.
- **Data formats:** JSON, protobuf or Avro, with care around types that differ between languages: 64-bit integers (JavaScript numbers lose precision above 2^53, so send them as strings or use `BigInt`), dates (ISO 8601 strings in UTC) and decimals (strings or integer cents).
- **Shared conventions:** the same headers for tracing (`traceparent`), the same error format, the same event envelope (CloudEvents).
- **Observability:** OpenTelemetry works across languages, so traces stay connected.

The int64 problem is a common bug: protobuf `int64` fields loaded with `@grpc/proto-loader` come back as `Long` objects, numbers or strings depending on the `longs` option, so set it on purpose.

## 416: What performance issues can GraphQL Federation have?

- **Query planning cost:** the router must plan how to split each query across subgraphs. Routers cache plans, but very complex or unique queries can still be slow.
- **Sequential fetches:** if a query needs data from subgraph A to know what to ask subgraph B, and then C, calls happen one after another and latency adds up.
- **Entity fetches:** the router sends `_entities` requests with a batch of keys to subgraphs. Subgraph resolvers must load those in bulk (with DataLoader), or each entity becomes a database query.
- **Expensive queries:** clients can ask for deeply nested data. You need depth limits, cost analysis or persisted queries (only allowing known queries).

Measure with router traces that show each subgraph fetch, and design the schema so common queries need few hops.

## 417: How do you tune gRPC performance in Node.js?

- **Reuse clients and channels.** Creating a client per request means new HTTP/2 connections each time.
- **Set message size limits** (`grpc.max_receive_message_length`, `grpc.max_send_message_length`) to match real payloads. The default receive limit is 4 MB.
- **Keepalive settings:** `grpc.keepalive_time_ms` and `grpc.keepalive_timeout_ms` keep connections healthy through load balancers, but servers may reject clients that ping too often, so align both sides.
- **Use streaming** for many small messages instead of thousands of unary calls.
- **Serialization cost:** `@grpc/proto-loader` uses protobufjs and has overhead on large messages. Measure, and consider precompiled code (`ts-proto`, `protobuf-es`) for hot paths.
- **Load balancing:** use `round_robin` with a headless Service or a proxy, so connections are spread across server pods.

## 418: How does backpressure work end to end in a streaming pipeline?

Backpressure means a slow consumer can make a fast producer slow down, instead of data piling up in memory somewhere in the middle.

Inside one Node process, streams handle it: `write()` returns `false` when the buffer is full, and `pipeline()` pauses the source until the destination drains. Between services:

- **HTTP:** TCP flow control slows down the sender if the receiver reads slowly, as long as both sides stream instead of buffering the full body.
- **gRPC streams:** HTTP/2 flow control and Node stream backpressure work together.
- **Brokers:** consumers pull at their own pace (Kafka) or use prefetch limits (RabbitMQ), so the broker holds the backlog.

The pipeline breaks when any step reads everything into memory (`await res.text()` on a huge body, collecting all messages into an array) or uses an unbounded in-memory queue. Look for those spots first.

## 419: How would you send a notification to millions of users at once?

Do not loop over all users in one process and call the email provider directly.

1. A request creates a **campaign** record and returns quickly.
2. A job splits the audience into **chunks** (for example 1,000 users each) by paging through the user list, and puts one message per chunk on a queue.
3. Many workers process chunks in parallel: they load preferences, render messages and send them to providers in batches, respecting provider rate limits.
4. Each send is recorded with a deduplication key (`campaignId + userId`), so retries do not send twice.
5. Progress, failures and bounces are tracked per campaign, with a DLQ for chunks that keep failing.

Use the providers' bulk APIs where available, and spread sending over time if the providers or your own systems (like the landing page the notification links to) cannot handle everything at once.

## 420: How do you schedule millions of future tasks (for example "remind the user in 3 days")?

Options:

- **Delayed jobs in a queue:** BullMQ delayed jobs or SQS delay (up to 15 minutes only). Fine for moderate volumes.
- **Database table with an index on due time:** store tasks with a `run_at` column and have workers poll for due tasks with `FOR UPDATE SKIP LOCKED`. Simple, durable and easy to inspect or cancel.
- **Time buckets:** group tasks by minute or hour in storage, and a scheduler moves each bucket to a work queue when it is due.
- **Managed schedulers:** Amazon EventBridge Scheduler, Google Cloud Tasks or a workflow engine with durable timers (Temporal).

```sql
SELECT id, payload FROM scheduled_tasks
WHERE run_at <= now() AND status = 'pending'
ORDER BY run_at
LIMIT 500
FOR UPDATE SKIP LOCKED;
```

Make tasks idempotent and check that they are still relevant when they run (the user may have already done the thing you were going to remind them about).

## 421: When should you use a workflow engine instead of writing sagas by hand?

Hand-written sagas (with events or a simple orchestrator and a state table) are fine for a few short flows with two or three steps.

A workflow engine like Temporal, AWS Step Functions or Camunda is worth it when:

- Flows have many steps, branches, waits and compensations.
- Steps can wait for hours or days (human approval, waiting for a webhook).
- You need timers, retries with backoff and timeouts for every step.
- You need to see the state of each running flow and fix stuck ones.

The engine gives you durable state, retries and visibility out of the box. The costs are another critical system to run (or pay for), a new programming model the team must learn, and rules like determinism in workflow code.

## 422: A downstream service your service depends on is down for 30 minutes. What should happen?

Good behaviour:

- Calls fail fast because of timeouts, and the circuit breaker opens after a few failures, so your service stops waiting and stops adding load.
- Requests that need the dependency get a fallback (cached data, a degraded response) or a clear `503` error, while features that do not need it keep working.
- Work that can wait (like sending to the dependency) goes to a queue or outbox and is processed after it recovers.
- Your readiness check stays green, because your service is still useful. You do not want Kubernetes to take you out of rotation too.
- Alerts fire for the dependency's owners, while your own alerts show "dependency down" instead of a flood of unrelated errors.
- When it recovers, the circuit half-opens, traffic increases gradually, and the backlog drains at a controlled rate.

Interviewers want to hear about timeouts, circuit breakers, fallbacks, queues and avoiding retry storms.

## 423: You find that some messages are being processed twice. How do you investigate and fix it?

Investigate:

- Check whether the duplicates have the same message ID (redelivery) or different IDs (the producer published twice).
- Same ID: look for consumer crashes, timeouts or rebalances around those times. A handler that takes longer than the visibility timeout (SQS) or the session timeout (Kafka) causes redelivery.
- Different IDs: look for producer retries without idempotence, the dual write problem or an outbox relay running twice on the same rows.

Fix:

- Make the consumer idempotent with an inbox table or unique constraints. This is needed anyway, since at-least-once delivery means duplicates will happen.
- Fix the cause of extra redeliveries: increase the timeout, process faster, shut down gracefully.
- Turn on producer idempotence, and use stable event IDs created once with the business change.

## 424: Your Node.js pods keep getting OOMKilled. How do you debug it?

1. **Check what the kernel killed.** `kubectl describe pod` shows `OOMKilled` with exit code 137. That means the container went over its memory limit. If Node itself ran out of heap, you would instead see a "JavaScript heap out of memory" error in the logs.
2. **Compare limits:** if `--max-old-space-size` (or the default heap limit) plus non-heap memory is above the container limit, the container dies before V8 can free memory. Lower the heap limit or raise the container limit.
3. **Look at the trend:** does memory grow slowly over hours (a leak) or jump suddenly (a big request, a big batch, a large file loaded into memory)?
4. **For leaks:** take heap snapshots over time and compare, or use `--heapsnapshot-near-heap-limit`.
5. **For spikes:** find large payloads, unbounded `Promise.all` over huge arrays, or buffering of whole streams.
6. **Check non-heap memory:** Buffers, native modules or many worker threads can use memory outside the heap that heap snapshots do not show.

## 425: p99 latency went up a lot after a deploy, but there are no errors. What do you check?

- **Compare versions:** with a canary or by comparing pods, confirm the new version is the cause.
- **Diff the change:** new dependencies, a library upgrade, new logging, extra validation, a new downstream call, a new database query or a changed index.
- **Traces:** compare slow traces from before and after. Is time spent in a new span, a database query or before any span starts (event loop or pool waits)?
- **Event loop delay and GC:** a change that allocates more or does sync work raises both.
- **Resources:** a changed CPU or memory limit, or a new base image (for example Alpine vs Debian) can change performance.
- **Cold caches:** a deploy that changed cache keys empties the cache.
- **Config:** pool sizes, timeouts or feature flags that changed together with the code.

If the cause is not clear quickly, roll back first and investigate after.

## 426: Consumer lag on a Kafka topic keeps growing. What do you do?

1. **Check if consumers are healthy:** are they running, connected and not stuck in rebalances? A rebalance loop looks like growing lag with little processing.
2. **Check if one partition is the problem:** lag on only one partition suggests a hot key or a poison message that is retried forever.
3. **Measure processing time** per message: did a downstream dependency (database, API) get slower?
4. **Check traffic:** did the producer rate go up (a campaign, a backfill)?

Fixes depending on the cause:

- Scale consumers, up to the number of partitions.
- Process in batches or with more concurrency per partition while keeping per-key order.
- Fix or skip the poison message (send it to a DLQ).
- Speed up the downstream work, for example with bulk writes.
- Add partitions if consumers are already at the partition limit, keeping in mind the effect on key ordering.

## 427: Users see 502 errors from the gateway every time a service is deployed. Why, and how do you fix it?

Common causes:

- **Pods stop before being removed from load balancing.** The pod gets `SIGTERM` and closes its server immediately, while the gateway still sends requests to it. Fix: a `preStop` sleep or keep serving for a few seconds after `SIGTERM`, then close gracefully.
- **New pods receive traffic before they are ready.** Missing or too simple readiness probes. Fix: a real readiness check that passes only after connections and warmup are done.
- **Keep-alive races.** The gateway reuses a connection that the old pod is closing. Fix: graceful close with `server.close()`, and keep-alive timeouts aligned between gateway and service.
- **Not enough capacity during rollout.** Fix: `maxUnavailable: 0` and a positive `maxSurge`.
- **The app ignores `SIGTERM`** because Node is not PID 1, so it gets killed hard. Fix: exec-form `CMD` or `tini`.

The gateway can also retry idempotent requests once on connection errors, which hides most of the remaining blips.

## 428: A service's database has become the bottleneck. What are your options?

Go roughly from cheapest to most work:

1. **Find the expensive queries** (`pg_stat_statements`, slow query logs) and fix them with indexes or better queries.
2. **Reduce load:** add caching for hot reads, stop N+1 query patterns, use bulk writes.
3. **Tune connections:** use a pooler like PgBouncer and right-size pools, since too many connections hurt performance.
4. **Read replicas** for read-heavy traffic that can be a bit stale.
5. **Scale up** the database instance.
6. **Move data:** archive old data, move search to Elasticsearch, move analytics to a warehouse, move large blobs to object storage.
7. **Split the service or its data** if it holds several things that could be separate.
8. **Shard** as a last step.

Also check whether other services are secretly querying this database, which happens more often than people admit.

## 429: You are splitting a monolith. How do you choose the first service to extract?

Good first candidates:

- **Clear boundaries:** a part with few dependencies on the rest of the monolith and its own data, like notifications, search or file processing.
- **Real benefit:** a part that needs to scale differently, changes often, or slows down monolith releases.
- **Low risk:** not the core payment flow. Learn on something where mistakes are cheaper.

Before the first extraction, set up the basics you will need for every service: CI/CD, containers, logging, tracing, monitoring and a way to route traffic (strangler proxy). The first service is as much about building this path as about the service itself. Often it also helps to first make the module boundary clean inside the monolith, then extract it.

## 430: Walk through how you would design a checkout flow across microservices.

Services: cart, orders, inventory, payments, shipping, notifications.

1. The client calls `POST /checkout` on the BFF with an idempotency key.
2. The orders service creates the order as `PENDING` and writes `OrderCreated` to its outbox in the same transaction.
3. An orchestrator (or a choreographed saga) runs the steps:
   - Inventory reserves stock with an expiry.
   - Payments charges the card using an idempotency key based on the order ID.
   - If payment succeeds, orders marks the order `CONFIRMED`. If it fails, inventory releases the stock and the order becomes `CANCELLED`.
4. Shipping listens to `OrderConfirmed` and creates the shipment. Notifications sends a confirmation email.
5. The client gets `202 Accepted` with the order ID and checks status (or receives updates by SSE), since payment can take a few seconds.

Points to mention: idempotency at each step, unknown payment outcomes after timeouts, reservation expiry, outbox for reliable events, tracing across the flow and reconciliation with the payment provider.

## 431: Two teams both want to own the "customer" data. How do you resolve it?

Usually both are right about a different part of "customer". Look at what each team actually needs:

- The account team needs identity, login and contact details.
- The billing team needs payment methods, tax IDs and invoicing addresses.
- The marketing team needs preferences and segments.

Split the concept by bounded context: each team owns the fields that belong to its context and its rules. A single customer ID links them. Each service publishes events about its part, and others keep local copies of what they need to read.

If one piece of data really must have one owner (like the email used for login), pick the team whose business rules depend on it most, and give others read access through events or an API. Write the decision down so it is not argued again every few months.

## 432: A change requires releasing three services at the same time. How do you avoid that?

Coordinated releases are a sign of tight coupling. Make the change in compatible steps instead:

1. Change the **provider** first so it supports both the old and new behaviour (a new optional field, a new endpoint or a new event version next to the old one). Deploy it.
2. Update the **consumers** one by one to use the new behaviour. Each can be deployed on its own schedule.
3. Once no consumer uses the old behaviour (check with metrics or logs), remove it from the provider.

Use feature flags if the behaviour change must be switched on for everyone at the same moment: deploy all code with the flag off, then flip the flag. If this keeps happening between the same services, revisit their boundaries.

## 433: A bad event schema was shipped and consumers are failing. What do you do?

Immediate steps:

1. **Stop the damage:** roll back the producer to the previous version, so it publishes the old format again.
2. **Protect consumers:** if they are crashing in a loop, deploy a quick fix that sends unparseable messages to a DLQ instead of blocking the partition.
3. **Handle the bad messages already published:** they are still in the topic. Either update consumers to handle them, replay them from the DLQ after a fix, or write a small job that converts them and republishes in the right format.

After the incident:

- Add schema compatibility checks in CI or a schema registry that rejects incompatible schemas.
- Add contract tests between the producer and its consumers.
- Make consumers tolerant readers, so extra or changed fields they do not use do not break them.

## 434: You find that access tokens have been written to logs for months. What do you do?

1. **Stop it:** deploy a fix that redacts the field (`redact` in Pino), and add a check in tests or CI.
2. **Assess the risk:** how long are the tokens valid? Short-lived access tokens may have expired already. Refresh tokens or API keys are much more serious.
3. **Rotate or revoke** any credentials that might still be valid, starting with the long-lived ones.
4. **Clean the logs:** delete or redact the affected entries in the logging system, backups and anywhere logs were copied (exports, tickets, vendor tools), as far as possible.
5. **Check for misuse:** look in access logs for use of those tokens from unusual places.
6. **Follow your security and legal process:** if personal data or customer credentials were exposed, there may be reporting duties.

Then look at why it happened, for example logging full request headers by default, and fix the pattern for all services, not just this one.

## 435: Your microservices cloud bill is too high. Where do you look first?

- **Over-provisioned resources:** compare CPU and memory requests with real use. Many pods request far more than they use. Rightsizing alone often saves a lot.
- **Idle environments:** dev, staging and preview environments running 24/7. Scale them down at night or remove unused ones.
- **Observability:** logs, metrics and traces are often one of the largest costs. Sample, reduce log volume and drop unused metrics.
- **Data transfer:** traffic across availability zones or regions, and NAT gateway fees. Chatty services in different zones can cost a lot.
- **Databases:** oversized instances, unused replicas, old snapshots.
- **Autoscaling settings:** minimum replica counts set too high.
- **Spot or preemptible instances** for stateless services and batch jobs, and savings plans for steady load.

Tag resources by service and team so each team can see what it spends.

## 436: How would you change a chain of synchronous calls into an event-driven flow?

Example: `POST /orders` calls inventory, then payments, then shipping, then email, all synchronously. Any slow or failing service fails the whole request.

Steps:

1. Decide what the user really needs to wait for. Often it is only "the order is accepted". Payment might also be needed right away, but shipping and email are not.
2. Keep the needed steps synchronous (or make them a saga with a quick initial response), and publish `OrderPlaced` through an outbox.
3. Move other steps to consumers: shipping and email listen to the event and do their work on their own.
4. Make each consumer idempotent and give each one a DLQ.
5. Add visibility: order status that shows progress, and tracing across the async steps.
6. Migrate gradually: publish events while the old calls still run, have new consumers run in shadow mode, compare results, then remove the sync calls one at a time.

## 437: How would you add distributed tracing to 40 existing Node.js services?

1. **Set up the backend first:** an OpenTelemetry Collector and a tracing backend (Tempo, Jaeger or a vendor), with sampling and retention decided.
2. **Create a shared package** that sets up the OpenTelemetry SDK with your defaults: service name from the environment, OTLP exporter, auto-instrumentations, sampling, and log correlation.
3. **Start with the edge:** the gateway and BFFs, so every trace has a root and propagates `traceparent`.
4. **Roll out to services** in order of importance, using `--import` in the start command so code changes are minimal. Do the busiest flows first so traces connect end to end early.
5. **Cover async paths:** make sure the broker clients propagate context in message headers.
6. **Check overhead** on a few services (CPU, latency) before rolling out everywhere.
7. **Teach teams** to use traces in incident reviews, otherwise the data goes unused.

## 438: What happens in your system if a whole cloud region goes down?

The answer depends on the setup, and an interviewer wants you to describe it honestly:

- **Single region:** the system is down until the region recovers or you rebuild elsewhere from backups. Know your RTO (how long that takes) and RPO (how much data you might lose) and whether backups are copied to another region.
- **Active-passive:** traffic fails over to a standby region. Data is replicated asynchronously, so a few seconds or minutes of recent writes may be lost. Failover may be automatic or manual and needs regular testing.
- **Active-active:** the other regions take the extra traffic. They must have enough capacity, and conflicting writes must be handled.

Also consider dependencies outside your services: DNS, identity providers, third-party APIs and the region where your CI/CD and container registry live. A failover plan that needs a deploy from a pipeline running in the dead region does not work.

## 439: Redis is down and your service is returning errors on every request. How should it have been designed?

Redis was probably on the critical path without timeouts or fallbacks. Better design:

- Short timeouts on Redis commands (tens of milliseconds for a cache), and a limited offline queue in the client, so calls fail fast instead of hanging.
- Treat cache failures as cache misses and read from the database, with a circuit breaker around Redis so you stop trying for a while.
- Protect the database from the sudden extra load: in-process caches for the hottest keys, request coalescing and load shedding.
- Decide per feature whether to fail open or closed: rate limiting can fail open, distributed locks for critical jobs should fail closed (do not run the job).
- Readiness should not depend on Redis if the service can still work without it.
- Run Redis with replication and automatic failover, and test what happens during a failover.

## 440: A nightly job runs twice on some nights. Why might that happen?

Possible causes:

- The job runs inside the service with `node-cron` or `setInterval`, and there are several replicas.
- A deploy or scale-up happened near the scheduled time, so an old and a new pod both ran it.
- A Kubernetes CronJob with `concurrencyPolicy: Allow` (the default) started a new run while a slow one was still running, or a failed run was retried after it had partly finished.
- A distributed lock expired during a long run (GC pause, slow step), and another instance took it.
- Daylight saving time: a schedule in local time can run twice (or not at all) on the night the clock changes. Use UTC or set `timeZone` on the CronJob deliberately.

Fixes: run it as a single scheduled job, set `concurrencyPolicy: Forbid`, use a lock with fencing or a database "job run" record with a unique key per date, and make the job idempotent.

## 441: A user updates their profile but still sees old data on another page. How do you find the cause?

Find out where the other page gets its data:

- **A read model** updated by events: check if the event was published (outbox), consumed (consumer lag, DLQ) and applied (version checks that may have rejected it).
- **A cache:** check TTLs and whether the update invalidated the right keys, in every layer (CDN, BFF memory, Redis).
- **A read replica:** replication lag may be the cause.
- **A local copy in another service:** that service may not subscribe to the update event, or may ignore the changed field.
- **The client:** browser or app caching, or a stale client-side store.

A trace of the update and the following read, plus the event ID, usually shows quickly where the change stopped. Then decide whether the delay is acceptable (eventual consistency) or the page needs read-your-own-writes handling.

## 442: Latency through your Node.js API gateway keeps creeping up as traffic grows. What do you check?

- **Event loop delay and CPU** on gateway instances: if they are busy, scale out and profile. Common hot spots: JWT verification for every request (cache verified tokens briefly or use faster algorithms like ES256 or EdDSA), JSON parsing and re-serializing bodies that could just be streamed through, and heavy logging.
- **Upstream connection pools:** too few connections per upstream means requests queue in the gateway. Check keep-alive is on.
- **DNS lookups** for upstreams on each new connection.
- **Middleware chains** that do sync work or extra network calls (for example calling the auth service on each request).
- **Rate limiter calls to Redis** on the hot path: check Redis latency.
- **GC pressure** from large request or response bodies.

Compare the gateway's own time with the upstream time in traces to make sure the gateway is really the slow part.

## 443: A Kafka consumer group keeps rebalancing and makes little progress. What is going on?

Common causes:

- **Processing takes too long.** If a consumer does not poll again within `max.poll.interval.ms` (or does not send heartbeats in time in kafkajs, controlled by `sessionTimeout` and `heartbeatInterval`), it is kicked out, a rebalance starts, and the same slow message is given to another consumer, which also gets kicked out.
- **Pods restarting** because of crashes, OOM kills or failing liveness probes.
- **Autoscaling** adding and removing consumers often.
- **Slow startup** that makes new members join late.

Fixes: process in smaller batches, call `heartbeat()` during long batches, increase session timeouts carefully, move very slow work to a separate queue, use static membership and cooperative rebalancing (or the new consumer protocol), and fix the crash or OOM cause.

## 444: Product wants a report that joins data from four services. How do you build it?

Do not build it by calling four APIs and joining in memory for every report request, unless the data is tiny.

Better options:

- **Reporting read model:** a reporting service listens to events from the four services and keeps a denormalized table designed for the report. Fast to query, near real time.
- **Data warehouse:** stream data from each service (CDC with Debezium, or events) into a warehouse like BigQuery, Snowflake or ClickHouse, and build the report there with SQL. This is usually best for analytical reports, filters and exports.
- **Scheduled export:** a nightly job collects data through bulk APIs, if the report does not need to be fresh.

Agree on freshness requirements first, since "real time" and "updated every morning" lead to very different designs. Make sure personal data is handled under the same rules in the reporting store.

## 445: What would you put in a production readiness checklist for a new microservice?

- **Ownership:** owner team, on-call rotation and an entry in the service catalog.
- **Health:** liveness, readiness and startup probes, plus graceful shutdown.
- **Resilience:** timeouts on all outgoing calls, retries only where safe, circuit breakers for key dependencies, idempotent handlers.
- **Observability:** structured logs with trace IDs, RED metrics, tracing, dashboards and alerts tied to SLOs.
- **Security:** authentication on all endpoints, least-privilege credentials, secrets from a secrets manager, dependency and image scanning, non-root container.
- **Data:** backups and a tested restore, migrations that are backward compatible.
- **Capacity:** load test results, resource requests and limits, autoscaling settings, PodDisruptionBudget.
- **Docs:** API contract, runbook for common problems, list of dependencies.

## 446: A downstream team says they never received some events you published. How do you debug it?

Follow the event step by step:

1. **Was it saved?** Check the outbox table (if you use one) for the event ID and whether it was marked as sent.
2. **Was it published?** Check producer logs and errors around that time. Without an outbox, look for crashes between the database write and the publish (the dual write problem).
3. **Is it on the broker?** Search the topic or queue for the event ID or key (`kcat` for Kafka, the management UI for RabbitMQ). Check retention: maybe it was deleted before they read it.
4. **Was it routed?** In RabbitMQ, a message published with a routing key that matches no binding is dropped unless you use `mandatory` or an alternate exchange.
5. **Was it consumed?** Check the consumer group's offsets, their logs and their DLQ. Maybe it was consumed and failed, or filtered out by their code.

Traces with span links across the broker make this much faster. The long-term fix is usually an outbox on the producer side and DLQs plus alerts on the consumer side.

## 447: A bug in one service suddenly sends 10 times more traffic to your service. How do you protect it?

Short term:

- Per-client rate limits or concurrency limits (based on the calling service's identity) reject the extra traffic from that caller without hurting others.
- Load shedding keeps your service responsive for the rest.
- Ask the calling team to roll back, or turn their feature off with a flag.

Design so this is handled automatically next time:

- Every service-to-service call has an identity, so you can see who is calling and limit per caller.
- Quotas per calling service at the gateway or mesh level.
- Autoscaling with a maximum, so a bug does not scale your service (and costs) without limit.
- Alerts on sudden traffic changes per caller.

Retry loops without backoff and `while` loops that poll are common causes of this kind of bug.

## 448: How do you measure whether a microservices architecture is working well?

Look at delivery and reliability, not the number of services:

- **DORA metrics:** deployment frequency, lead time for changes, change failure rate and time to restore service. Microservices should help teams deploy more often and recover faster. If they do not, something is wrong.
- **Team independence:** how often does a change need several teams or a coordinated release?
- **Reliability:** SLO attainment and incident frequency, and how often incidents spread across services.
- **Developer experience:** time to create a new service, time for a new developer to make their first change, and how long builds and tests take.
- **Cost per request** or per customer over time.

If deploys are rare, incidents spread widely and every feature touches five services, the architecture is not giving its benefits, and it may be time to revisit boundaries or merge services.

## 449: What questions would you ask before agreeing to move a system to microservices?

- What problem are we trying to solve? Slow releases, scaling limits, team conflicts or something else? Is there a cheaper fix, like a modular monolith?
- How many teams and engineers will work on it? Microservices mostly solve organizational scaling problems.
- Do we have automated CI/CD, monitoring, logging and container infrastructure, or the budget and people to build them?
- Do we understand the domain well enough to draw stable boundaries?
- Which data needs strong consistency, and how will we handle it across services?
- Who will be on call for each service?
- How will we migrate step by step without stopping feature work?

A good answer in an interview shows that you see microservices as a trade-off, not as the default.

## 450: What recent changes in Node.js and its ecosystem matter for building microservices?

- **Release schedule:** Node 24 is in Active LTS, Node 26 enters LTS in October 2026, and starting with Node 27 the project moves to one major release per year with no more odd/even split. Plan upgrades around LTS lines.
- **Built-in features that replace dependencies:** stable `fetch` and Web Streams, `--env-file` and `process.loadEnvFile()`, the built-in test runner (`node:test`) with mocking and coverage, `--watch` mode, and `AbortSignal.timeout()`.
- **TypeScript type stripping:** Node runs `.ts` files directly by default, which simplifies dev setups and small services (with the limits mentioned in question 149).
- **Permission model:** stable `--permission` flag to restrict file system, child process and other access.
- **Express 5** is the current Express line with proper async error handling. Fastify 5 requires Node 20 or newer.
- **OpenTelemetry JS SDK 2.x** raised minimum versions and changed some APIs, so older setup code may need updating.
- **Messaging:** Kafka 4.x runs without ZooKeeper and brings the new consumer rebalance protocol, and RabbitMQ 4.x removed classic mirrored queues in favour of quorum queues.

Check release notes before upgrading, because defaults keep changing between major versions.
