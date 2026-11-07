# Design Patterns and System Architecture Interview Questions and Answers

_Last updated: October 29, 2026_

450 interview questions with answers about design patterns and system architecture, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions go from classic design patterns and SOLID, through architecture styles (monolith, microservices, event-driven, hexagonal, DDD), to system design topics like caching, databases, messaging, scaling, reliability and real interview scenarios. Code examples use TypeScript and Node.js, and the answers reflect how systems are commonly built in 2026.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a design pattern?](#1-what-is-a-design-pattern)
- [2: Why should you use design patterns?](#2-why-should-you-use-design-patterns)
- [3: What are the three categories of classic design patterns?](#3-what-are-the-three-categories-of-classic-design-patterns)
- [4: What is the Gang of Four?](#4-what-is-the-gang-of-four)
- [5: What is an anti-pattern?](#5-what-is-an-anti-pattern)
- [6: What does SOLID stand for?](#6-what-does-solid-stand-for)
- [7: What is the Single Responsibility Principle?](#7-what-is-the-single-responsibility-principle)
- [8: What is the Open/Closed Principle?](#8-what-is-the-openclosed-principle)
- [9: What is the Liskov Substitution Principle?](#9-what-is-the-liskov-substitution-principle)
- [10: What is the Interface Segregation Principle?](#10-what-is-the-interface-segregation-principle)
- [11: What is the Dependency Inversion Principle?](#11-what-is-the-dependency-inversion-principle)
- [12: What is the DRY principle?](#12-what-is-the-dry-principle)
- [13: What is the KISS principle?](#13-what-is-the-kiss-principle)
- [14: What is YAGNI?](#14-what-is-yagni)
- [15: What does "composition over inheritance" mean?](#15-what-does-composition-over-inheritance-mean)
- [16: What are coupling and cohesion?](#16-what-are-coupling-and-cohesion)
- [17: What is encapsulation?](#17-what-is-encapsulation)
- [18: What is abstraction?](#18-what-is-abstraction)
- [19: What is polymorphism?](#19-what-is-polymorphism)
- [20: What is the difference between an interface and an abstract class?](#20-what-is-the-difference-between-an-interface-and-an-abstract-class)
- [21: What is the Singleton pattern?](#21-what-is-the-singleton-pattern)
- [22: What are the problems with the Singleton pattern?](#22-what-are-the-problems-with-the-singleton-pattern)
- [23: What is the Factory Method pattern?](#23-what-is-the-factory-method-pattern)
- [24: What is the difference between a simple factory and the Factory Method pattern?](#24-what-is-the-difference-between-a-simple-factory-and-the-factory-method-pattern)
- [25: What is the Abstract Factory pattern?](#25-what-is-the-abstract-factory-pattern)
- [26: What is the Builder pattern?](#26-what-is-the-builder-pattern)
- [27: What is the Prototype pattern?](#27-what-is-the-prototype-pattern)
- [28: What is an object pool?](#28-what-is-an-object-pool)
- [29: What is the Adapter pattern?](#29-what-is-the-adapter-pattern)
- [30: What is the Decorator pattern?](#30-what-is-the-decorator-pattern)
- [31: What is the Facade pattern?](#31-what-is-the-facade-pattern)
- [32: What is the Proxy pattern?](#32-what-is-the-proxy-pattern)
- [33: What is the Composite pattern?](#33-what-is-the-composite-pattern)
- [34: What is the Bridge pattern?](#34-what-is-the-bridge-pattern)
- [35: What is the Flyweight pattern?](#35-what-is-the-flyweight-pattern)
- [36: What is the Observer pattern?](#36-what-is-the-observer-pattern)
- [37: What is the difference between Observer and Publish/Subscribe?](#37-what-is-the-difference-between-observer-and-publishsubscribe)
- [38: What is the Strategy pattern?](#38-what-is-the-strategy-pattern)
- [39: What is the Command pattern?](#39-what-is-the-command-pattern)
- [40: What is the Iterator pattern?](#40-what-is-the-iterator-pattern)
- [41: What is the State pattern?](#41-what-is-the-state-pattern)
- [42: What is the Template Method pattern?](#42-what-is-the-template-method-pattern)
- [43: What is the Chain of Responsibility pattern?](#43-what-is-the-chain-of-responsibility-pattern)
- [44: What is the Mediator pattern?](#44-what-is-the-mediator-pattern)
- [45: What is the Memento pattern?](#45-what-is-the-memento-pattern)
- [46: What is the Visitor pattern?](#46-what-is-the-visitor-pattern)
- [47: What is the Null Object pattern?](#47-what-is-the-null-object-pattern)
- [48: What is dependency injection?](#48-what-is-dependency-injection)
- [49: What is Inversion of Control?](#49-what-is-inversion-of-control)
- [50: What is a service locator and why do many people call it an anti-pattern?](#50-what-is-a-service-locator-and-why-do-many-people-call-it-an-anti-pattern)
- [51: What is the Repository pattern?](#51-what-is-the-repository-pattern)
- [52: What is the Unit of Work pattern?](#52-what-is-the-unit-of-work-pattern)
- [53: What is a DTO?](#53-what-is-a-dto)
- [54: What is MVC?](#54-what-is-mvc)
- [55: What is MVVM?](#55-what-is-mvvm)
- [56: What is MVP?](#56-what-is-mvp)
- [57: What is a layered architecture?](#57-what-is-a-layered-architecture)
- [58: What is software architecture?](#58-what-is-software-architecture)
- [59: What is the difference between architecture and design?](#59-what-is-the-difference-between-architecture-and-design)
- [60: What is a monolith?](#60-what-is-a-monolith)
- [61: What are microservices?](#61-what-are-microservices)
- [62: What is a modular monolith?](#62-what-is-a-modular-monolith)
- [63: What is the client-server model?](#63-what-is-the-client-server-model)
- [64: What is a three-tier architecture?](#64-what-is-a-three-tier-architecture)
- [65: What is serverless?](#65-what-is-serverless)
- [66: What is SOA and how is it different from microservices?](#66-what-is-soa-and-how-is-it-different-from-microservices)
- [67: What is event-driven architecture?](#67-what-is-event-driven-architecture)
- [68: What is the difference between horizontal and vertical scaling?](#68-what-is-the-difference-between-horizontal-and-vertical-scaling)
- [69: What is a load balancer?](#69-what-is-a-load-balancer)
- [70: What load balancing algorithms do you know?](#70-what-load-balancing-algorithms-do-you-know)
- [71: What is the difference between stateless and stateful services?](#71-what-is-the-difference-between-stateless-and-stateful-services)
- [72: What is caching?](#72-what-is-caching)
- [73: Where can you cache data in a web application?](#73-where-can-you-cache-data-in-a-web-application)
- [74: What is a CDN?](#74-what-is-a-cdn)
- [75: What is the cache-aside pattern?](#75-what-is-the-cache-aside-pattern)
- [76: What is TTL and why is cache invalidation hard?](#76-what-is-ttl-and-why-is-cache-invalidation-hard)
- [77: What is the difference between a forward proxy and a reverse proxy?](#77-what-is-the-difference-between-a-forward-proxy-and-a-reverse-proxy)
- [78: What is an API gateway?](#78-what-is-an-api-gateway)
- [79: What is REST?](#79-what-is-rest)
- [80: What is RPC and what is gRPC?](#80-what-is-rpc-and-what-is-grpc)
- [81: When would you choose GraphQL over REST?](#81-when-would-you-choose-graphql-over-rest)
- [82: What is a webhook?](#82-what-is-a-webhook)
- [83: What is the difference between polling, long polling, WebSockets and Server-Sent Events?](#83-what-is-the-difference-between-polling-long-polling-websockets-and-server-sent-events)
- [84: What is the difference between synchronous and asynchronous communication between services?](#84-what-is-the-difference-between-synchronous-and-asynchronous-communication-between-services)
- [85: What is a message queue?](#85-what-is-a-message-queue)
- [86: What message brokers do you know?](#86-what-message-brokers-do-you-know)
- [87: What is the difference between a queue and a topic?](#87-what-is-the-difference-between-a-queue-and-a-topic)
- [88: What is the difference between SQL and NoSQL databases?](#88-what-is-the-difference-between-sql-and-nosql-databases)
- [89: What types of NoSQL databases are there?](#89-what-types-of-nosql-databases-are-there)
- [90: What is ACID?](#90-what-is-acid)
- [91: What is BASE?](#91-what-is-base)
- [92: What is a database index?](#92-what-is-a-database-index)
- [93: What is database replication?](#93-what-is-database-replication)
- [94: What is primary-replica replication?](#94-what-is-primary-replica-replication)
- [95: What is sharding?](#95-what-is-sharding)
- [96: What is the difference between vertical and horizontal partitioning?](#96-what-is-the-difference-between-vertical-and-horizontal-partitioning)
- [97: What is normalization and denormalization?](#97-what-is-normalization-and-denormalization)
- [98: What is the CAP theorem?](#98-what-is-the-cap-theorem)
- [99: What is the difference between strong and eventual consistency?](#99-what-is-the-difference-between-strong-and-eventual-consistency)
- [100: What is the difference between latency and throughput?](#100-what-is-the-difference-between-latency-and-throughput)
- [101: What does "five nines" availability mean?](#101-what-does-five-nines-availability-mean)
- [102: What are SLA, SLO and SLI?](#102-what-are-sla-slo-and-sli)
- [103: What is a single point of failure?](#103-what-is-a-single-point-of-failure)
- [104: What are redundancy and failover?](#104-what-are-redundancy-and-failover)
- [105: What is a health check?](#105-what-is-a-health-check)
- [106: What is rate limiting?](#106-what-is-rate-limiting)
- [107: What is idempotency?](#107-what-is-idempotency)
- [108: What is retry with exponential backoff?](#108-what-is-retry-with-exponential-backoff)
- [109: Why do you need timeouts?](#109-why-do-you-need-timeouts)
- [110: What is the Circuit Breaker pattern?](#110-what-is-the-circuit-breaker-pattern)
- [111: What is observability?](#111-what-is-observability)
- [112: What is object storage?](#112-what-is-object-storage)
- [113: What role does DNS play in a system architecture?](#113-what-role-does-dns-play-in-a-system-architecture)
- [114: How do you handle user sessions when you have many app servers?](#114-how-do-you-handle-user-sessions-when-you-have-many-app-servers)
- [115: What are the trade-offs between server sessions and JWTs?](#115-what-are-the-trade-offs-between-server-sessions-and-jwts)
- [116: What is the difference between authentication and authorization?](#116-what-is-the-difference-between-authentication-and-authorization)
- [117: What are OAuth 2.0 and OpenID Connect?](#117-what-are-oauth-20-and-openid-connect)
- [118: What is the difference between batch and stream processing?](#118-what-is-the-difference-between-batch-and-stream-processing)
- [119: What are background workers and scheduled jobs?](#119-what-are-background-workers-and-scheduled-jobs)
- [120: What is the difference between offset pagination and cursor pagination?](#120-what-is-the-difference-between-offset-pagination-and-cursor-pagination)
- [121: How can you version an API?](#121-how-can-you-version-an-api)
- [122: What role do containers play in modern architecture?](#122-what-role-do-containers-play-in-modern-architecture)
- [123: What is the Twelve-Factor App?](#123-what-is-the-twelve-factor-app)
- [124: Why should configuration be kept outside the code?](#124-why-should-configuration-be-kept-outside-the-code)
- [125: What is the difference between a monorepo and a polyrepo?](#125-what-is-the-difference-between-a-monorepo-and-a-polyrepo)
- [126: What is a back-of-the-envelope estimation?](#126-what-is-a-back-of-the-envelope-estimation)
- [127: What is the difference between functional and non-functional requirements?](#127-what-is-the-difference-between-functional-and-non-functional-requirements)
- [128: How do you approach a system design interview question?](#128-how-do-you-approach-a-system-design-interview-question)
- [129: What is a bottleneck?](#129-what-is-a-bottleneck)
- [130: What is the difference between a read-heavy and a write-heavy system?](#130-what-is-the-difference-between-a-read-heavy-and-a-write-heavy-system)
- [131: What is connection pooling?](#131-what-is-connection-pooling)
- [132: What is a key-value store?](#132-what-is-a-key-value-store)
- [133: What is separation of concerns?](#133-what-is-separation-of-concerns)
- [134: What is the Law of Demeter?](#134-what-is-the-law-of-demeter)
- [135: What is the Module pattern?](#135-what-is-the-module-pattern)
- [136: What is a mixin?](#136-what-is-a-mixin)
- [137: What is the middleware pattern?](#137-what-is-the-middleware-pattern)
- [138: What is a plugin architecture?](#138-what-is-a-plugin-architecture)
- [139: What does "program to an interface, not an implementation" mean?](#139-what-does-program-to-an-interface-not-an-implementation-mean)
- [140: What is the difference between a thin client and a thick client?](#140-what-is-the-difference-between-a-thin-client-and-a-thick-client)
- [141: What is the difference between client-side rendering and server-side rendering?](#141-what-is-the-difference-between-client-side-rendering-and-server-side-rendering)
- [142: What are feature flags?](#142-what-are-feature-flags)
- [143: What is blue-green deployment?](#143-what-is-blue-green-deployment)
- [144: What is a canary deployment?](#144-what-is-a-canary-deployment)
- [145: What is a rolling deployment?](#145-what-is-a-rolling-deployment)
- [146: What is service discovery?](#146-what-is-service-discovery)
- [147: What is an ORM?](#147-what-is-an-orm)
- [148: What is the difference between Active Record and Data Mapper?](#148-what-is-the-difference-between-active-record-and-data-mapper)
- [149: What is a God Object?](#149-what-is-a-god-object)
- [150: What is premature optimization?](#150-what-is-premature-optimization)

### Moderate Questions (151-300)

- [151: How do you decide between Factory Method and Abstract Factory?](#151-how-do-you-decide-between-factory-method-and-abstract-factory)
- [152: What is the difference between Adapter, Decorator and Proxy?](#152-what-is-the-difference-between-adapter-decorator-and-proxy)
- [153: What is the difference between Strategy and State?](#153-what-is-the-difference-between-strategy-and-state)
- [154: What is the difference between Facade and Mediator?](#154-what-is-the-difference-between-facade-and-mediator)
- [155: How can the Observer pattern cause memory leaks and how do you avoid them?](#155-how-can-the-observer-pattern-cause-memory-leaks-and-how-do-you-avoid-them)
- [156: How would you implement a typed event emitter?](#156-how-would-you-implement-a-typed-event-emitter)
- [157: How do you create a singleton in Node.js, and when does it stop being a single instance?](#157-how-do-you-create-a-singleton-in-nodejs-and-when-does-it-stop-being-a-single-instance)
- [158: How do you make a builder that forces required fields at compile time?](#158-how-do-you-make-a-builder-that-forces-required-fields-at-compile-time)
- [159: How do you implement undo and redo with the Command pattern?](#159-how-do-you-implement-undo-and-redo-with-the-command-pattern)
- [160: How would you build your own middleware pipeline?](#160-how-would-you-build-your-own-middleware-pipeline)
- [161: When is the Composite pattern a good fit, and when is it not?](#161-when-is-the-composite-pattern-a-good-fit-and-when-is-it-not)
- [162: How do generators help implement the Iterator pattern?](#162-how-do-generators-help-implement-the-iterator-pattern)
- [163: What is the difference between Template Method and Strategy?](#163-what-is-the-difference-between-template-method-and-strategy)
- [164: How does a dependency injection container work?](#164-how-does-a-dependency-injection-container-work)
- [165: How does dependency injection make testing easier?](#165-how-does-dependency-injection-make-testing-easier)
- [166: When does a repository add value and when is it just extra code?](#166-when-does-a-repository-add-value-and-when-is-it-just-extra-code)
- [167: What is the Specification pattern?](#167-what-is-the-specification-pattern)
- [168: What is CQRS?](#168-what-is-cqrs)
- [169: What is event sourcing?](#169-what-is-event-sourcing)
- [170: What is hexagonal architecture?](#170-what-is-hexagonal-architecture)
- [171: What is Clean Architecture?](#171-what-is-clean-architecture)
- [172: What is the difference between Clean, Onion and Hexagonal architecture?](#172-what-is-the-difference-between-clean-onion-and-hexagonal-architecture)
- [173: What is a bounded context in Domain-Driven Design?](#173-what-is-a-bounded-context-in-domain-driven-design)
- [174: What is the difference between an entity and a value object?](#174-what-is-the-difference-between-an-entity-and-a-value-object)
- [175: What is an aggregate and an aggregate root?](#175-what-is-an-aggregate-and-an-aggregate-root)
- [176: What is a domain event?](#176-what-is-a-domain-event)
- [177: What is ubiquitous language?](#177-what-is-ubiquitous-language)
- [178: What is an anti-corruption layer?](#178-what-is-an-anti-corruption-layer)
- [179: What is an anemic domain model?](#179-what-is-an-anemic-domain-model)
- [180: What is an application service, and how is it different from a domain service?](#180-what-is-an-application-service-and-how-is-it-different-from-a-domain-service)
- [181: How do you decide how to split a system into microservices?](#181-how-do-you-decide-how-to-split-a-system-into-microservices)
- [182: What is the database-per-service pattern?](#182-what-is-the-database-per-service-pattern)
- [183: Why is a shared database between microservices a problem?](#183-why-is-a-shared-database-between-microservices-a-problem)
- [184: What is a distributed monolith?](#184-what-is-a-distributed-monolith)
- [185: What is the difference between an API gateway and a Backend for Frontend?](#185-what-is-the-difference-between-an-api-gateway-and-a-backend-for-frontend)
- [186: What is a service mesh?](#186-what-is-a-service-mesh)
- [187: What is the sidecar pattern?](#187-what-is-the-sidecar-pattern)
- [188: What is the Strangler Fig pattern?](#188-what-is-the-strangler-fig-pattern)
- [189: What is the Saga pattern?](#189-what-is-the-saga-pattern)
- [190: What is the difference between choreography and orchestration in sagas?](#190-what-is-the-difference-between-choreography-and-orchestration-in-sagas)
- [191: What is the Transactional Outbox pattern?](#191-what-is-the-transactional-outbox-pattern)
- [192: What is two-phase commit and why is it rarely used in microservices?](#192-what-is-two-phase-commit-and-why-is-it-rarely-used-in-microservices)
- [193: What are at-most-once, at-least-once and exactly-once delivery?](#193-what-are-at-most-once-at-least-once-and-exactly-once-delivery)
- [194: How do you make a message consumer idempotent?](#194-how-do-you-make-a-message-consumer-idempotent)
- [195: What is a dead letter queue?](#195-what-is-a-dead-letter-queue)
- [196: How do you keep message ordering in a queue system?](#196-how-do-you-keep-message-ordering-in-a-queue-system)
- [197: What is back-pressure?](#197-what-is-back-pressure)
- [198: How do partitions and consumer groups work in Kafka?](#198-how-do-partitions-and-consumer-groups-work-in-kafka)
- [199: What is the competing consumers pattern?](#199-what-is-the-competing-consumers-pattern)
- [200: What is the fan-out pattern?](#200-what-is-the-fan-out-pattern)
- [201: What is consistent hashing?](#201-what-is-consistent-hashing)
- [202: What are write-through, write-back and write-around caching?](#202-what-are-write-through-write-back-and-write-around-caching)
- [203: What are common cache eviction policies?](#203-what-are-common-cache-eviction-policies)
- [204: What is a cache stampede and how do you prevent it?](#204-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [205: When would you use a local in-memory cache instead of Redis?](#205-when-would-you-use-a-local-in-memory-cache-instead-of-redis)
- [206: How does HTTP caching fit into the architecture?](#206-how-does-http-caching-fit-into-the-architecture)
- [207: What problems does replication lag cause and how do you handle them?](#207-what-problems-does-replication-lag-cause-and-how-do-you-handle-them)
- [208: What is the difference between synchronous and asynchronous replication?](#208-what-is-the-difference-between-synchronous-and-asynchronous-replication)
- [209: How do you choose a good shard key?](#209-how-do-you-choose-a-good-shard-key)
- [210: Why is resharding hard?](#210-why-is-resharding-hard)
- [211: When does denormalization make sense, and what are the risks?](#211-when-does-denormalization-make-sense-and-what-are-the-risks)
- [212: What are the trade-offs of adding database indexes?](#212-what-are-the-trade-offs-of-adding-database-indexes)
- [213: What is the N+1 query problem?](#213-what-is-the-n1-query-problem)
- [214: Why can serverless functions run into database connection problems?](#214-why-can-serverless-functions-run-into-database-connection-problems)
- [215: What is the difference between optimistic and pessimistic locking?](#215-what-is-the-difference-between-optimistic-and-pessimistic-locking)
- [216: What are transaction isolation levels?](#216-what-are-transaction-isolation-levels)
- [217: What is the PACELC theorem?](#217-what-is-the-pacelc-theorem)
- [218: What rate limiting algorithms do you know?](#218-what-rate-limiting-algorithms-do-you-know)
- [219: How would you implement a token bucket rate limiter?](#219-how-would-you-implement-a-token-bucket-rate-limiter)
- [220: How do you do rate limiting across many servers?](#220-how-do-you-do-rate-limiting-across-many-servers)
- [221: How does a circuit breaker work internally?](#221-how-does-a-circuit-breaker-work-internally)
- [222: What is the Bulkhead pattern?](#222-what-is-the-bulkhead-pattern)
- [223: What is a retry storm and how does jitter help?](#223-what-is-a-retry-storm-and-how-does-jitter-help)
- [224: What is graceful degradation?](#224-what-is-graceful-degradation)
- [225: What is the difference between liveness and readiness probes?](#225-what-is-the-difference-between-liveness-and-readiness-probes)
- [226: How do you shut down a service gracefully?](#226-how-do-you-shut-down-a-service-gracefully)
- [227: What is deadline propagation?](#227-what-is-deadline-propagation)
- [228: What is distributed tracing?](#228-what-is-distributed-tracing)
- [229: What is a correlation ID?](#229-what-is-a-correlation-id)
- [230: What is structured logging and why is it better?](#230-what-is-structured-logging-and-why-is-it-better)
- [231: What types of metrics are there, and what are the RED and USE methods?](#231-what-types-of-metrics-are-there-and-what-are-the-red-and-use-methods)
- [232: What should you alert on?](#232-what-should-you-alert-on)
- [233: How would you design a URL shortener?](#233-how-would-you-design-a-url-shortener)
- [234: How would you design pagination for an infinite scroll feed?](#234-how-would-you-design-pagination-for-an-infinite-scroll-feed)
- [235: How would you design a notification system?](#235-how-would-you-design-a-notification-system)
- [236: How would you design a file upload service?](#236-how-would-you-design-a-file-upload-service)
- [237: How would you design a basic chat application?](#237-how-would-you-design-a-basic-chat-application)
- [238: How would you design a leaderboard?](#238-how-would-you-design-a-leaderboard)
- [239: How would you design search autocomplete?](#239-how-would-you-design-search-autocomplete)
- [240: How would you design a background job system?](#240-how-would-you-design-a-background-job-system)
- [241: How do you design an API for a long-running task?](#241-how-do-you-design-an-api-for-a-long-running-task)
- [242: How do idempotency keys work in a payment API?](#242-how-do-idempotency-keys-work-in-a-payment-api)
- [243: What are good practices for REST API design?](#243-what-are-good-practices-for-rest-api-design)
- [244: How do you change an API without breaking existing clients?](#244-how-do-you-change-an-api-without-breaking-existing-clients)
- [245: When would you use gRPC instead of REST between services?](#245-when-would-you-use-grpc-instead-of-rest-between-services)
- [246: What problems do you need to solve when you adopt GraphQL?](#246-what-problems-do-you-need-to-solve-when-you-adopt-graphql)
- [247: How do you scale WebSocket servers horizontally?](#247-how-do-you-scale-websocket-servers-horizontally)
- [248: When would you use Server-Sent Events instead of WebSockets?](#248-when-would-you-use-server-sent-events-instead-of-websockets)
- [249: What are micro frontends?](#249-what-are-micro-frontends)
- [250: What are the trade-offs between CSR, SSR, SSG and ISR?](#250-what-are-the-trade-offs-between-csr-ssr-ssg-and-isr)
- [251: What is edge computing in web architecture?](#251-what-is-edge-computing-in-web-architecture)
- [252: What are the trade-offs of serverless architecture?](#252-what-are-the-trade-offs-of-serverless-architecture)
- [253: What is the difference between event notification and event-carried state transfer?](#253-what-is-the-difference-between-event-notification-and-event-carried-state-transfer)
- [254: How do you version events and message schemas?](#254-how-do-you-version-events-and-message-schemas)
- [255: What multi-tenancy models do you know?](#255-what-multi-tenancy-models-do-you-know)
- [256: What problems can feature flags cause and how do you manage them?](#256-what-problems-can-feature-flags-cause-and-how-do-you-manage-them)
- [257: How do you manage configuration and secrets in a distributed system?](#257-how-do-you-manage-configuration-and-secrets-in-a-distributed-system)
- [258: How do you run database migrations with zero downtime?](#258-how-do-you-run-database-migrations-with-zero-downtime)
- [259: How does blue-green deployment work with a database?](#259-how-does-blue-green-deployment-work-with-a-database)
- [260: How do you make a stateful application horizontally scalable?](#260-how-do-you-make-a-stateful-application-horizontally-scalable)
- [261: What metrics would you use for autoscaling?](#261-what-metrics-would-you-use-for-autoscaling)
- [262: What is the difference between a Layer 4 and a Layer 7 load balancer?](#262-what-is-the-difference-between-a-layer-4-and-a-layer-7-load-balancer)
- [263: What is GeoDNS or global server load balancing?](#263-what-is-geodns-or-global-server-load-balancing)
- [264: What is the difference between active-passive and active-active multi-region setups?](#264-what-is-the-difference-between-active-passive-and-active-active-multi-region-setups)
- [265: What are RPO and RTO?](#265-what-are-rpo-and-rto)
- [266: What makes a good backup strategy?](#266-what-makes-a-good-backup-strategy)
- [267: When should you add a search engine like Elasticsearch, and how do you keep it in sync?](#267-when-should-you-add-a-search-engine-like-elasticsearch-and-how-do-you-keep-it-in-sync)
- [268: How would you design image delivery for a website with user uploads?](#268-how-would-you-design-image-delivery-for-a-website-with-user-uploads)
- [269: How would you store time-series data?](#269-how-would-you-store-time-series-data)
- [270: How do you choose a database for a new feature?](#270-how-do-you-choose-a-database-for-a-new-feature)
- [271: What is polyglot persistence?](#271-what-is-polyglot-persistence)
- [272: What is a Bloom filter and where is it used?](#272-what-is-a-bloom-filter-and-where-is-it-used)
- [273: What is the Pipes and Filters pattern?](#273-what-is-the-pipes-and-filters-pattern)
- [274: What are the common problems with a layered architecture?](#274-what-are-the-common-problems-with-a-layered-architecture)
- [275: What is vertical slice architecture?](#275-what-is-vertical-slice-architecture)
- [276: Should you organize code by feature or by layer?](#276-should-you-organize-code-by-feature-or-by-layer)
- [277: How do you enforce module boundaries in a large codebase?](#277-how-do-you-enforce-module-boundaries-in-a-large-codebase)
- [278: How do you keep a modular monolith from turning into a big ball of mud?](#278-how-do-you-keep-a-modular-monolith-from-turning-into-a-big-ball-of-mud)
- [279: What kinds of coupling exist besides code dependencies?](#279-what-kinds-of-coupling-exist-besides-code-dependencies)
- [280: What is Conway's Law?](#280-what-is-conways-law)
- [281: What is an Architecture Decision Record?](#281-what-is-an-architecture-decision-record)
- [282: What is the C4 model?](#282-what-is-the-c4-model)
- [283: How do you handle technical debt from an architecture point of view?](#283-how-do-you-handle-technical-debt-from-an-architecture-point-of-view)
- [284: What does it mean that quality attributes trade off against each other?](#284-what-does-it-mean-that-quality-attributes-trade-off-against-each-other)
- [285: Why should you wrap third-party APIs behind your own interface?](#285-why-should-you-wrap-third-party-apis-behind-your-own-interface)
- [286: Which HTTP methods are safe and which are idempotent, and why does it matter for architecture?](#286-which-http-methods-are-safe-and-which-are-idempotent-and-why-does-it-matter-for-architecture)
- [287: What is request batching or the DataLoader pattern?](#287-what-is-request-batching-or-the-dataloader-pattern)
- [288: What is an optimistic UI update?](#288-what-is-an-optimistic-ui-update)
- [289: What is an offline-first architecture?](#289-what-is-an-offline-first-architecture)
- [290: What is unidirectional data flow?](#290-what-is-unidirectional-data-flow)
- [291: What is the container and presentational components pattern?](#291-what-is-the-container-and-presentational-components-pattern)
- [292: How is reactive programming used as a design pattern?](#292-how-is-reactive-programming-used-as-a-design-pattern)
- [293: What is the producer-consumer pattern?](#293-what-is-the-producer-consumer-pattern)
- [294: How do you handle CPU-heavy work in Node.js without blocking the server?](#294-how-do-you-handle-cpu-heavy-work-in-nodejs-without-blocking-the-server)
- [295: What is lazy loading as an architectural pattern?](#295-what-is-lazy-loading-as-an-architectural-pattern)
- [296: How do you schedule delayed messages, like "send a reminder in 24 hours"?](#296-how-do-you-schedule-delayed-messages-like-send-a-reminder-in-24-hours)
- [297: How do you build reliable webhook delivery as a provider?](#297-how-do-you-build-reliable-webhook-delivery-as-a-provider)
- [298: How should an API communicate rate limits to clients?](#298-how-should-an-api-communicate-rate-limits-to-clients)
- [299: What is defense in depth and least privilege?](#299-what-is-defense-in-depth-and-least-privilege)
- [300: How do services authenticate each other in a microservice system?](#300-how-do-services-authenticate-each-other-in-a-microservice-system)

### Advanced Questions (301-450)

- [301: How would you design a news feed like Twitter or Instagram?](#301-how-would-you-design-a-news-feed-like-twitter-or-instagram)
- [302: What is the celebrity problem in feed systems and how do you solve it?](#302-what-is-the-celebrity-problem-in-feed-systems-and-how-do-you-solve-it)
- [303: How would you design a rate limiter for a large distributed API?](#303-how-would-you-design-a-rate-limiter-for-a-large-distributed-api)
- [304: How do you generate short codes for a URL shortener at very large scale?](#304-how-do-you-generate-short-codes-for-a-url-shortener-at-very-large-scale)
- [305: How do you generate unique IDs in a distributed system?](#305-how-do-you-generate-unique-ids-in-a-distributed-system)
- [306: How would you design a web crawler?](#306-how-would-you-design-a-web-crawler)
- [307: How would you design the location part of a ride-hailing app?](#307-how-would-you-design-the-location-part-of-a-ride-hailing-app)
- [308: How would you design typeahead suggestions for a very large search engine?](#308-how-would-you-design-typeahead-suggestions-for-a-very-large-search-engine)
- [309: How would you design a video streaming platform?](#309-how-would-you-design-a-video-streaming-platform)
- [310: How would you design a payment system?](#310-how-would-you-design-a-payment-system)
- [311: How would you design a ticket booking system that doesn't sell the same seat twice?](#311-how-would-you-design-a-ticket-booking-system-that-doesnt-sell-the-same-seat-twice)
- [312: How would you design a distributed job scheduler?](#312-how-would-you-design-a-distributed-job-scheduler)
- [313: How would you design a metrics and monitoring system?](#313-how-would-you-design-a-metrics-and-monitoring-system)
- [314: How would you design a collaborative editor like Google Docs?](#314-how-would-you-design-a-collaborative-editor-like-google-docs)
- [315: How would you scale a chat system to millions of users?](#315-how-would-you-scale-a-chat-system-to-millions-of-users)
- [316: How do you keep inventory correct during a checkout under heavy load?](#316-how-do-you-keep-inventory-correct-during-a-checkout-under-heavy-load)
- [317: How would you design a distributed cache?](#317-how-would-you-design-a-distributed-cache)
- [318: How would you design a Dynamo-style key-value store?](#318-how-would-you-design-a-dynamo-style-key-value-store)
- [319: How would you design an ad click aggregation system?](#319-how-would-you-design-an-ad-click-aggregation-system)
- [320: How would you design a file sync service like Dropbox?](#320-how-would-you-design-a-file-sync-service-like-dropbox)
- [321: How would you design product search for a large e-commerce site?](#321-how-would-you-design-product-search-for-a-large-e-commerce-site)
- [322: How do you deal with the noisy neighbor problem in a multi-tenant system?](#322-how-do-you-deal-with-the-noisy-neighbor-problem-in-a-multi-tenant-system)
- [323: How would you design a feature flag service?](#323-how-would-you-design-a-feature-flag-service)
- [324: How do distributed locks work and why can they be dangerous?](#324-how-do-distributed-locks-work-and-why-can-they-be-dangerous)
- [325: What is leader election and how is it done?](#325-what-is-leader-election-and-how-is-it-done)
- [326: How does the Raft consensus algorithm work at a high level?](#326-how-does-the-raft-consensus-algorithm-work-at-a-high-level)
- [327: How do quorums work in replicated databases?](#327-how-do-quorums-work-in-replicated-databases)
- [328: What are vector clocks and why are they used?](#328-what-are-vector-clocks-and-why-are-they-used)
- [329: What is wrong with last-write-wins conflict resolution?](#329-what-is-wrong-with-last-write-wins-conflict-resolution)
- [330: What are Lamport timestamps?](#330-what-are-lamport-timestamps)
- [331: What are CRDTs?](#331-what-are-crdts)
- [332: What is a gossip protocol?](#332-what-is-a-gossip-protocol)
- [333: What is split brain and how do you prevent it?](#333-what-is-split-brain-and-how-do-you-prevent-it)
- [334: What is the difference between crash faults and Byzantine faults?](#334-what-is-the-difference-between-crash-faults-and-byzantine-faults)
- [335: What is the difference between linearizability and serializability?](#335-what-is-the-difference-between-linearizability-and-serializability)
- [336: What consistency models sit between strong and eventual consistency?](#336-what-consistency-models-sit-between-strong-and-eventual-consistency)
- [337: What does "exactly-once" in Kafka really mean?](#337-what-does-exactly-once-in-kafka-really-mean)
- [338: What is change data capture?](#338-what-is-change-data-capture)
- [339: What are the Lambda and Kappa architectures?](#339-what-are-the-lambda-and-kappa-architectures)
- [340: What are windows, event time and watermarks in stream processing?](#340-what-are-windows-event-time-and-watermarks-in-stream-processing)
- [341: What problems come up with event sourcing in production?](#341-what-problems-come-up-with-event-sourcing-in-production)
- [342: How do you handle eventual consistency in the UI when using CQRS?](#342-how-do-you-handle-eventual-consistency-in-the-ui-when-using-cqrs)
- [343: What are the tricky parts of designing sagas?](#343-what-are-the-tricky-parts-of-designing-sagas)
- [344: How do you implement the outbox publisher reliably?](#344-how-do-you-implement-the-outbox-publisher-reliably)
- [345: What is the inbox pattern?](#345-what-is-the-inbox-pattern)
- [346: What is a poison message and how do you handle it?](#346-what-is-a-poison-message-and-how-do-you-handle-it)
- [347: How do you scale consumers while keeping message order per entity?](#347-how-do-you-scale-consumers-while-keeping-message-order-per-entity)
- [348: How do you deal with hot partitions or hot keys?](#348-how-do-you-deal-with-hot-partitions-or-hot-keys)
- [349: What are virtual nodes in consistent hashing, and what is rendezvous hashing?](#349-what-are-virtual-nodes-in-consistent-hashing-and-what-is-rendezvous-hashing)
- [350: What race conditions can make a cache serve stale data, and how do you avoid them?](#350-what-race-conditions-can-make-a-cache-serve-stale-data-and-how-do-you-avoid-them)
- [351: How do you handle cache warm-up and cold starts?](#351-how-do-you-handle-cache-warm-up-and-cold-starts)
- [352: What is multi-level caching and what problems does it bring?](#352-what-is-multi-level-caching-and-what-problems-does-it-bring)
- [353: What is tail latency and why does it matter more in systems with fan-out?](#353-what-is-tail-latency-and-why-does-it-matter-more-in-systems-with-fan-out)
- [354: What techniques reduce tail latency?](#354-what-techniques-reduce-tail-latency)
- [355: What is load shedding?](#355-what-is-load-shedding)
- [356: What are adaptive concurrency limits?](#356-what-are-adaptive-concurrency-limits)
- [357: What is a retry budget?](#357-what-is-a-retry-budget)
- [358: What is a cascading failure and how do you prevent it?](#358-what-is-a-cascading-failure-and-how-do-you-prevent-it)
- [359: What is a metastable failure?](#359-what-is-a-metastable-failure)
- [360: What is cell-based architecture?](#360-what-is-cell-based-architecture)
- [361: What is shuffle sharding?](#361-what-is-shuffle-sharding)
- [362: How do you reduce the blast radius of failures and changes?](#362-how-do-you-reduce-the-blast-radius-of-failures-and-changes)
- [363: What is chaos engineering?](#363-what-is-chaos-engineering)
- [364: What are the challenges of replicating data across regions?](#364-what-are-the-challenges-of-replicating-data-across-regions)
- [365: How does data residency or GDPR affect architecture?](#365-how-does-data-residency-or-gdpr-affect-architecture)
- [366: How would you scale a relational database step by step as traffic grows?](#366-how-would-you-scale-a-relational-database-step-by-step-as-traffic-grows)
- [367: How do you handle queries and transactions that cross shards?](#367-how-do-you-handle-queries-and-transactions-that-cross-shards)
- [368: How do secondary indexes work in a sharded database?](#368-how-do-secondary-indexes-work-in-a-sharded-database)
- [369: How do you change the schema of a very large table in production?](#369-how-do-you-change-the-schema-of-a-very-large-table-in-production)
- [370: How do you backfill data safely in a large production system?](#370-how-do-you-backfill-data-safely-in-a-large-production-system)
- [371: What is MVCC?](#371-what-is-mvcc)
- [372: What is the difference between B-tree and LSM-tree storage engines?](#372-what-is-the-difference-between-b-tree-and-lsm-tree-storage-engines)
- [373: What is a write-ahead log?](#373-what-is-a-write-ahead-log)
- [374: What is hot, warm and cold storage tiering?](#374-what-is-hot-warm-and-cold-storage-tiering)
- [375: When do you use materialized views or precomputed read models?](#375-when-do-you-use-materialized-views-or-precomputed-read-models)
- [376: How do you count things like likes or views at very large scale?](#376-how-do-you-count-things-like-likes-or-views-at-very-large-scale)
- [377: How do you find the top K items (heavy hitters) in a huge stream?](#377-how-do-you-find-the-top-k-items-heavy-hitters-in-a-huge-stream)
- [378: How do you reindex a search cluster with zero downtime?](#378-how-do-you-reindex-a-search-cluster-with-zero-downtime)
- [379: What goes wrong when microservices are too small?](#379-what-goes-wrong-when-microservices-are-too-small)
- [380: How would you migrate a monolith to microservices?](#380-how-would-you-migrate-a-monolith-to-microservices)
- [381: Why do long synchronous call chains hurt availability?](#381-why-do-long-synchronous-call-chains-hurt-availability)
- [382: How do you query data that lives in several services?](#382-how-do-you-query-data-that-lives-in-several-services)
- [383: What is the TCC (Try-Confirm-Cancel) pattern?](#383-what-is-the-tcc-try-confirm-cancel-pattern)
- [384: What is consumer-driven contract testing?](#384-what-is-consumer-driven-contract-testing)
- [385: What do backward and forward compatibility mean for schemas, and how do they affect deploy order?](#385-what-do-backward-and-forward-compatibility-mean-for-schemas-and-how-do-they-affect-deploy-order)
- [386: What is zero trust architecture?](#386-what-is-zero-trust-architecture)
- [387: How do you guarantee tenant data isolation in a shared database?](#387-how-do-you-guarantee-tenant-data-isolation-in-a-shared-database)
- [388: What is the difference between RBAC, ABAC and ReBAC?](#388-what-is-the-difference-between-rbac-abac-and-rebac)
- [389: How do you revoke JWTs before they expire?](#389-how-do-you-revoke-jwts-before-they-expire)
- [390: How do you rotate secrets without downtime?](#390-how-do-you-rotate-secrets-without-downtime)
- [391: What is SSRF and how do you protect a system that fetches user-provided URLs?](#391-what-is-ssrf-and-how-do-you-protect-a-system-that-fetches-user-provided-urls)
- [392: How do you protect a system from DDoS attacks at the architecture level?](#392-how-do-you-protect-a-system-from-ddos-attacks-at-the-architecture-level)
- [393: What are CDN cache keys, cache poisoning and purge strategies?](#393-what-are-cdn-cache-keys-cache-poisoning-and-purge-strategies)
- [394: How would you build a system that holds millions of WebSocket connections?](#394-how-would-you-build-a-system-that-holds-millions-of-websocket-connections)
- [395: How would you design an online presence system?](#395-how-would-you-design-an-online-presence-system)
- [396: How do you handle a slow consumer in a data pipeline?](#396-how-do-you-handle-a-slow-consumer-in-a-data-pipeline)
- [397: How do you choose between batch, micro-batch and streaming?](#397-how-do-you-choose-between-batch-micro-batch-and-streaming)
- [398: What is the difference between a data lake, a data warehouse and a lakehouse?](#398-what-is-the-difference-between-a-data-lake-a-data-warehouse-and-a-lakehouse)
- [399: Why separate OLTP and OLAP workloads?](#399-why-separate-oltp-and-olap-workloads)
- [400: What are head-based and tail-based sampling in tracing?](#400-what-are-head-based-and-tail-based-sampling-in-tracing)
- [401: What is the high cardinality problem in metrics?](#401-what-is-the-high-cardinality-problem-in-metrics)
- [402: How do error budgets guide engineering decisions?](#402-how-do-error-budgets-guide-engineering-decisions)
- [403: How do you do capacity planning?](#403-how-do-you-do-capacity-planning)
- [404: How do you take cost into account in architecture decisions?](#404-how-do-you-take-cost-into-account-in-architecture-decisions)
- [405: How do you decide what consistency level each feature needs?](#405-how-do-you-decide-what-consistency-level-each-feature-needs)
- [406: How does Google Spanner use clocks to give strong consistency?](#406-how-does-google-spanner-use-clocks-to-give-strong-consistency)
- [407: What are the trade-offs of distributed SQL databases?](#407-what-are-the-trade-offs-of-distributed-sql-databases)
- [408: What problems show up with serverless at large scale?](#408-what-problems-show-up-with-serverless-at-large-scale)
- [409: What are the pitfalls of event-driven architecture?](#409-what-are-the-pitfalls-of-event-driven-architecture)
- [410: When would you use a workflow engine like Temporal or AWS Step Functions instead of hand-written sagas?](#410-when-would-you-use-a-workflow-engine-like-temporal-or-aws-step-functions-instead-of-hand-written-sagas)
- [411: How does durable execution work in tools like Temporal?](#411-how-does-durable-execution-work-in-tools-like-temporal)
- [412: What race conditions can happen with idempotency keys and how do you handle them?](#412-what-race-conditions-can-happen-with-idempotency-keys-and-how-do-you-handle-them)
- [413: How do you get exactly-once side effects with external systems like email or payments?](#413-how-do-you-get-exactly-once-side-effects-with-external-systems-like-email-or-payments)
- [414: How do deduplication windows work, and what are their limits?](#414-how-do-deduplication-windows-work-and-what-are-their-limits)
- [415: How do you guarantee read-your-writes when reads go to replicas or read models?](#415-how-do-you-guarantee-read-your-writes-when-reads-go-to-replicas-or-read-models)
- [416: What are the trade-offs between leader-based and leaderless replication?](#416-what-are-the-trade-offs-between-leader-based-and-leaderless-replication)
- [417: What problems does multi-leader replication bring?](#417-what-problems-does-multi-leader-replication-bring)
- [418: What are sloppy quorums and hinted handoff?](#418-what-are-sloppy-quorums-and-hinted-handoff)
- [419: How are Merkle trees used for anti-entropy between replicas?](#419-how-are-merkle-trees-used-for-anti-entropy-between-replicas)
- [420: How do you know when design patterns are being overused?](#420-how-do-you-know-when-design-patterns-are-being-overused)
- [421: How do you design a public interface or SDK that can evolve for years?](#421-how-do-you-design-a-public-interface-or-sdk-that-can-evolve-for-years)
- [422: In a hexagonal architecture, where do transactions live and how do you test it?](#422-in-a-hexagonal-architecture-where-do-transactions-live-and-how-do-you-test-it)
- [423: What are the rules of thumb for designing aggregates?](#423-what-are-the-rules-of-thumb-for-designing-aggregates)
- [424: How do you handle concurrent updates to the same aggregate?](#424-how-do-you-handle-concurrent-updates-to-the-same-aggregate)
- [425: What are context mapping patterns in DDD?](#425-what-are-context-mapping-patterns-in-ddd)
- [426: What is Event Storming?](#426-what-is-event-storming)
- [427: What is the difference between domain events and integration events?](#427-what-is-the-difference-between-domain-events-and-integration-events)
- [428: What are architecture fitness functions?](#428-what-are-architecture-fitness-functions)
- [429: How do you justify an architecture decision to your team or management?](#429-how-do-you-justify-an-architecture-decision-to-your-team-or-management)
- [430: What is the difference between one-way and two-way door decisions?](#430-what-is-the-difference-between-one-way-and-two-way-door-decisions)
- [431: What problems do micro frontends cause at scale and how do you handle them?](#431-what-problems-do-micro-frontends-cause-at-scale-and-how-do-you-handle-them)
- [432: How would you structure the data layer of a large front-end application?](#432-how-would-you-structure-the-data-layer-of-a-large-front-end-application)
- [433: How do you make server-side rendering scale for a high-traffic site?](#433-how-do-you-make-server-side-rendering-scale-for-a-high-traffic-site)
- [434: How do you reduce API latency for users around the world?](#434-how-do-you-reduce-api-latency-for-users-around-the-world)
- [435: Your system gets slow under load. How do you find the bottleneck?](#435-your-system-gets-slow-under-load-how-do-you-find-the-bottleneck)
- [436: The database CPU is at 100%. What do you do?](#436-the-database-cpu-is-at-100-what-do-you-do)
- [437: Your Redis cache cluster goes down. What happens and how should the system behave?](#437-your-redis-cache-cluster-goes-down-what-happens-and-how-should-the-system-behave)
- [438: Customers report duplicate orders. How do you investigate and fix it?](#438-customers-report-duplicate-orders-how-do-you-investigate-and-fix-it)
- [439: A message queue backlog keeps growing. What do you do?](#439-a-message-queue-backlog-keeps-growing-what-do-you-do)
- [440: One slow microservice is taking the whole site down. How do you fix it now and prevent it later?](#440-one-slow-microservice-is-taking-the-whole-site-down-how-do-you-fix-it-now-and-prevent-it-later)
- [441: How would you migrate from MySQL to PostgreSQL without downtime?](#441-how-would-you-migrate-from-mysql-to-postgresql-without-downtime)
- [442: How would you prepare a system for a flash sale with 10x normal traffic?](#442-how-would-you-prepare-a-system-for-a-flash-sale-with-10x-normal-traffic)
- [443: A third-party API your product depends on is down for hours. How should your system handle it?](#443-a-third-party-api-your-product-depends-on-is-down-for-hours-how-should-your-system-handle-it)
- [444: Data between two services has become inconsistent. How do you deal with it?](#444-data-between-two-services-has-become-inconsistent-how-do-you-deal-with-it)
- [445: A deploy caused errors and included a database migration. How do you roll back?](#445-a-deploy-caused-errors-and-included-a-database-migration-how-do-you-roll-back)
- [446: How would you plan for a full region outage?](#446-how-would-you-plan-for-a-full-region-outage)
- [447: A startup asks whether to begin with a monolith or microservices. What do you recommend?](#447-a-startup-asks-whether-to-begin-with-a-monolith-or-microservices-what-do-you-recommend)
- [448: You're asked to cut cloud costs by 40%. Where do you start?](#448-youre-asked-to-cut-cloud-costs-by-40-where-do-you-start)
- [449: You inherit a legacy system with no tests and need to add features. How do you approach it?](#449-you-inherit-a-legacy-system-with-no-tests-and-need-to-add-features-how-do-you-approach-it)
- [450: What questions do you ask when reviewing an architecture proposal?](#450-what-questions-do-you-ask-when-reviewing-an-architecture-proposal)

---

# Easy Questions (1-150)

## 1: What is a design pattern?

A design pattern is a common, reusable solution to a problem that shows up again and again in software design. It is not finished code you copy. It is more like a template or an idea that you adapt to your own code. Patterns also give developers shared names, so saying "use an adapter here" is enough for the team to understand the plan.

## 2: Why should you use design patterns?

- They are tested solutions, so you don't have to reinvent them.
- They give the team a common vocabulary.
- They usually make code easier to change and to test.
- They help new developers understand the structure faster.

The catch is that a pattern used in the wrong place only adds extra classes and layers. Use a pattern when you actually have the problem it solves.

## 3: What are the three categories of classic design patterns?

The Gang of Four book splits its 23 patterns into three groups:

- **Creational:** how objects get created. Singleton, Factory Method, Abstract Factory, Builder, Prototype.
- **Structural:** how classes and objects are put together. Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.
- **Behavioral:** how objects talk to each other and share work. Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor, Interpreter.

## 4: What is the Gang of Four?

"Gang of Four" (GoF) refers to Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, who wrote _Design Patterns: Elements of Reusable Object-Oriented Software_ in 1994. The book described 23 patterns and made the idea of design patterns popular. Most pattern names we use today come from this book.

## 5: What is an anti-pattern?

An anti-pattern is a common solution that looks fine at first but causes more problems than it solves. Examples are the God Object (one class that does everything), spaghetti code, copy-paste programming, the golden hammer (using one favorite tool for every problem) and a shared database between microservices. Knowing anti-patterns helps you spot bad design early.

## 6: What does SOLID stand for?

SOLID is a set of five object-oriented design principles:

- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

Together they aim to make code easier to understand, extend and test.

## 7: What is the Single Responsibility Principle?

A class or module should have one reason to change. In other words, it should do one job. If a `UserService` validates input, saves to the database and sends emails, a change in email logic forces you to touch the same class as a change in the database. Splitting it into smaller pieces keeps changes local.

```ts
// Too many jobs
class UserService {
  register(data: UserInput) {
    /* validate, save, send email */
  }
}

// Split by responsibility
class UserValidator {
  validate(data: UserInput) {
    /* ... */
  }
}
class UserRepository {
  save(user: User) {
    /* ... */
  }
}
class WelcomeMailer {
  send(user: User) {
    /* ... */
  }
}
```

## 8: What is the Open/Closed Principle?

Code should be open for extension but closed for modification. You should be able to add new behavior without editing code that already works. A common way is to depend on an interface and add new implementations.

```ts
interface DiscountRule {
  apply(total: number): number;
}

class BlackFriday implements DiscountRule {
  apply(total: number) {
    return total * 0.7;
  }
}

function checkout(total: number, rules: DiscountRule[]) {
  return rules.reduce((sum, rule) => rule.apply(sum), total);
}
// A new discount is a new class. checkout() stays the same.
```

## 9: What is the Liskov Substitution Principle?

If `B` is a subtype of `A`, you should be able to use `B` anywhere `A` is expected without breaking the program. The classic broken example is `Square extends Rectangle`: setting the width of a square also changes its height, which surprises code written for rectangles. If a subclass has to throw "not supported" or change the meaning of a method, the inheritance is probably wrong.

## 10: What is the Interface Segregation Principle?

Clients should not be forced to depend on methods they don't use. Instead of one big interface, make several small ones.

```ts
// Too big: a basic printer must implement scan and fax
interface Machine {
  print(doc: string): void;
  scan(doc: string): void;
  fax(doc: string): void;
}

// Better
interface Printer {
  print(doc: string): void;
}
interface Scanner {
  scan(doc: string): void;
}

class SimplePrinter implements Printer {
  print(doc: string) {
    console.log(doc);
  }
}
```

## 11: What is the Dependency Inversion Principle?

High-level modules should not depend on low-level modules. Both should depend on abstractions. For example, an `OrderService` should depend on a `PaymentGateway` interface, not directly on a `StripeClient` class. Then you can swap Stripe for another provider, or a fake in tests, without touching `OrderService`.

```ts
interface PaymentGateway {
  charge(amount: number): Promise<void>;
}

class OrderService {
  constructor(private payments: PaymentGateway) {}

  async placeOrder(total: number) {
    await this.payments.charge(total);
  }
}
```

## 12: What is the DRY principle?

DRY means "Don't Repeat Yourself". Every piece of knowledge should have one clear place in the system. If the same business rule is copied in five places, you will forget to update one of them. Be careful though: two pieces of code that look the same but change for different reasons are not real duplication, and merging them can create bad coupling.

## 13: What is the KISS principle?

KISS means "Keep It Simple, Stupid". Pick the simplest solution that works. Simple code is easier to read, debug and change. Many bugs and slow teams come from clever code or architecture that was more complex than the problem needed.

## 14: What is YAGNI?

YAGNI means "You Aren't Gonna Need It". Don't build features or abstractions for needs you only imagine might appear later. Code written "just in case" still has to be read, tested and maintained, and often the future need never comes or looks different from what you guessed.

## 15: What does "composition over inheritance" mean?

It means you should prefer building objects from smaller parts (has-a) over extending base classes (is-a). Deep inheritance trees are rigid: a change in the base class affects all children, and you can only inherit from one class. With composition you can mix behaviors freely and swap them at runtime.

```ts
class Engine {
  start() {
    console.log("engine on");
  }
}

class Car {
  constructor(private engine: Engine) {}
  drive() {
    this.engine.start();
  }
}
```

## 16: What are coupling and cohesion?

- **Coupling** is how much one module depends on another. Low coupling is good because you can change one part without breaking others.
- **Cohesion** is how closely the things inside one module belong together. High cohesion is good: a module that does one clear job.

The usual goal is "low coupling, high cohesion".

## 17: What is encapsulation?

Encapsulation means keeping an object's data and the code that works on it together, and hiding internal details from the outside. Other code uses a public method instead of changing fields directly, so the object can protect its own rules.

```ts
class BankAccount {
  #balance = 0;

  deposit(amount: number) {
    if (amount <= 0) throw new Error("Amount must be positive");
    this.#balance += amount;
  }

  get balance() {
    return this.#balance;
  }
}
```

## 18: What is abstraction?

Abstraction means showing only what matters and hiding the details. When you call `fetch(url)`, you don't care about sockets, TCP or TLS. In design, abstractions are usually interfaces or abstract classes that describe what something does, not how it does it.

## 19: What is polymorphism?

Polymorphism lets you treat different types through the same interface, and each type responds in its own way. Many patterns (Strategy, State, Command) depend on it.

```ts
interface Shape {
  area(): number;
}

class Circle implements Shape {
  constructor(private r: number) {}
  area() {
    return Math.PI * this.r ** 2;
  }
}

class Square implements Shape {
  constructor(private side: number) {}
  area() {
    return this.side ** 2;
  }
}

const shapes: Shape[] = [new Circle(1), new Square(2)];
shapes.forEach((s) => console.log(s.area()));
```

## 20: What is the difference between an interface and an abstract class?

- An **interface** only describes a contract: method and property signatures. A class can implement many interfaces. In TypeScript, interfaces disappear at runtime.
- An **abstract class** can have both abstract methods and real code (shared logic, fields, constructors). A class can extend only one.

Use an interface when you just need a contract. Use an abstract class when the subclasses really share code.

## 21: What is the Singleton pattern?

Singleton makes sure a class has only one instance and gives a global way to get it. It is often used for things like a config object, a logger or a database connection pool.

```ts
class Config {
  private static instance: Config;
  private constructor(public readonly env: string) {}

  static getInstance() {
    if (!Config.instance) {
      Config.instance = new Config(process.env.NODE_ENV ?? "development");
    }
    return Config.instance;
  }
}

const a = Config.getInstance();
const b = Config.getInstance();
console.log(a === b); // true
```

In Node.js, a simple exported object already acts like a singleton because modules are cached after the first import.

## 22: What are the problems with the Singleton pattern?

- It is global state, so any code can change it and bugs are hard to trace.
- It hides dependencies: a class that calls `Config.getInstance()` inside its methods doesn't show that dependency in its constructor.
- It is hard to replace in tests.
- In multi-threaded languages, lazy creation needs locking.

Many teams prefer to create one instance and pass it around with dependency injection. You still get "only one", but without the global access.

## 23: What is the Factory Method pattern?

Factory Method lets a base class define a method for creating an object, while subclasses decide which concrete class to create. The calling code works with the result through an interface and doesn't need to know the exact type.

```ts
interface Notification {
  send(msg: string): void;
}

class EmailNotification implements Notification {
  send(msg: string) {
    console.log("email:", msg);
  }
}

class SmsNotification implements Notification {
  send(msg: string) {
    console.log("sms:", msg);
  }
}

abstract class Notifier {
  protected abstract createNotification(): Notification;

  notify(msg: string) {
    this.createNotification().send(msg);
  }
}

class EmailNotifier extends Notifier {
  protected createNotification() {
    return new EmailNotification();
  }
}
```

## 24: What is the difference between a simple factory and the Factory Method pattern?

A **simple factory** is just a function or static method with a `switch` that returns the right object. It is not a GoF pattern but it is very common.

```ts
function createNotification(type: "email" | "sms"): Notification {
  switch (type) {
    case "email":
      return new EmailNotification();
    case "sms":
      return new SmsNotification();
  }
}
```

**Factory Method** uses inheritance: subclasses override a creation method. The simple factory is enough most of the time. Factory Method makes sense when a framework or base class needs subclasses to plug in their own types.

## 25: What is the Abstract Factory pattern?

Abstract Factory creates families of related objects that are meant to be used together, without naming their concrete classes. A typical example is a UI kit: a `LightThemeFactory` creates light buttons and light inputs, and a `DarkThemeFactory` creates dark ones. The client code gets one factory and is sure all parts match.

```ts
interface Button {
  render(): string;
}
interface Input {
  render(): string;
}

interface UIFactory {
  createButton(): Button;
  createInput(): Input;
}

class DarkFactory implements UIFactory {
  createButton() {
    return { render: () => "<button class='dark'>" };
  }
  createInput() {
    return { render: () => "<input class='dark'>" };
  }
}
```

## 26: What is the Builder pattern?

Builder creates a complex object step by step. It is useful when an object has many optional parts and a constructor with ten parameters would be hard to read.

```ts
class QueryBuilder {
  private parts: string[] = [];
  private table = "";

  from(table: string) {
    this.table = table;
    return this;
  }

  where(condition: string) {
    this.parts.push(condition);
    return this;
  }

  build() {
    const where = this.parts.length ? ` WHERE ${this.parts.join(" AND ")}` : "";
    return `SELECT * FROM ${this.table}${where}`;
  }
}

const sql = new QueryBuilder().from("users").where("age > 18").build();
```

Note: this example builds a string for clarity. In real code, use parameterized queries to avoid SQL injection.

## 27: What is the Prototype pattern?

Prototype creates new objects by copying an existing object instead of building one from scratch. It helps when creating an object is expensive or when you want many objects that start from the same setup. In JavaScript you can use `structuredClone()` for a deep copy, and JavaScript's own inheritance is based on prototypes.

```ts
const defaultSettings = { theme: "light", notifications: { email: true } };

const userSettings = structuredClone(defaultSettings);
userSettings.notifications.email = false;

console.log(defaultSettings.notifications.email); // true
```

## 28: What is an object pool?

An object pool keeps a set of ready-to-use objects and hands them out instead of creating new ones every time. When you are done, you return the object to the pool. Database connection pools are the most common example, because opening a new connection for every query is slow.

## 29: What is the Adapter pattern?

Adapter converts one interface into another that the client expects. It is like a travel plug adapter. It is often used to wrap third-party libraries or old code so the rest of the app works with your own interface.

```ts
interface Logger {
  log(message: string): void;
}

// Third-party library with a different API
class FancyLogger {
  write(level: string, text: string) {
    console.log(`[${level}] ${text}`);
  }
}

class FancyLoggerAdapter implements Logger {
  constructor(private fancy: FancyLogger) {}
  log(message: string) {
    this.fancy.write("info", message);
  }
}
```

## 30: What is the Decorator pattern?

Decorator adds behavior to an object by wrapping it in another object with the same interface. You can stack several decorators. It is a flexible alternative to creating a subclass for every combination of features.

```ts
interface DataSource {
  read(): string;
}

class FileSource implements DataSource {
  read() {
    return "raw data";
  }
}

class LoggingSource implements DataSource {
  constructor(private inner: DataSource) {}
  read() {
    console.log("reading...");
    return this.inner.read();
  }
}

const source = new LoggingSource(new FileSource());
source.read();
```

This is different from TypeScript decorators (`@Something`), which are a language feature, although they are often used for the same goal.

## 31: What is the Facade pattern?

Facade gives a simple interface to a complicated subsystem. The client calls one method, and the facade handles the many classes behind it.

```ts
class VideoConverter {
  convert(file: string, format: string) {
    const video = new VideoFile(file);
    const codec = new CodecFactory().extract(video);
    const result = new BitrateReader().read(video, codec);
    return new AudioMixer().fix(result, format);
  }
}
```

The client only knows about `VideoConverter.convert()`. A service layer in a back end often acts as a facade over repositories, external APIs and queues.

## 32: What is the Proxy pattern?

A Proxy is an object that stands in for another object and controls access to it. It has the same interface as the real object. Common uses:

- **Virtual proxy:** create the real object only when needed (lazy loading).
- **Protection proxy:** check permissions before calling the real object.
- **Caching proxy:** return cached results.
- **Remote proxy:** hide that the real object is on another server.

JavaScript has a built-in `Proxy` object that can intercept property access, which is used by libraries like Vue for reactivity.

## 33: What is the Composite pattern?

Composite lets you treat single objects and groups of objects the same way, by putting them in a tree. A file system is the usual example: a folder and a file both have a `getSize()` method, and a folder's size is the sum of its children.

```ts
interface Node {
  getSize(): number;
}

class FileNode implements Node {
  constructor(private size: number) {}
  getSize() {
    return this.size;
  }
}

class Folder implements Node {
  private children: Node[] = [];
  add(child: Node) {
    this.children.push(child);
  }
  getSize() {
    return this.children.reduce((sum, c) => sum + c.getSize(), 0);
  }
}
```

UI component trees in React or Angular follow the same idea.

## 34: What is the Bridge pattern?

Bridge splits one big class hierarchy into two separate ones (an abstraction and an implementation) that can change independently. Example: you have shapes (circle, square) and renderers (SVG, canvas). Without Bridge you'd need `SvgCircle`, `CanvasCircle`, `SvgSquare` and so on. With Bridge, each shape holds a reference to a renderer, so you can combine any shape with any renderer.

```ts
interface Renderer {
  drawCircle(r: number): void;
}

class SvgRenderer implements Renderer {
  drawCircle(r: number) {
    console.log(`<circle r="${r}" />`);
  }
}

class Circle {
  constructor(
    private renderer: Renderer,
    private r: number,
  ) {}
  draw() {
    this.renderer.drawCircle(this.r);
  }
}
```

## 35: What is the Flyweight pattern?

Flyweight saves memory by sharing the parts of objects that are the same, instead of storing them in every object. In a text editor, each character on screen doesn't need its own copy of the font data. The font, size and color are shared (intrinsic state), and only the position is stored per character (extrinsic state). It is useful when you have a very large number of similar objects.

## 36: What is the Observer pattern?

Observer defines a one-to-many relationship: when one object (the subject) changes, all its subscribers (observers) get notified. DOM events, Node's `EventEmitter`, RxJS and many state management libraries are based on it.

```ts
type Listener<T> = (value: T) => void;

class Subject<T> {
  private listeners = new Set<Listener<T>>();

  subscribe(fn: Listener<T>) {
    this.listeners.add(fn);
    return () => this.listeners.delete(fn); // unsubscribe
  }

  notify(value: T) {
    this.listeners.forEach((fn) => fn(value));
  }
}

const price = new Subject<number>();
price.subscribe((p) => console.log("new price", p));
price.notify(42);
```

## 37: What is the difference between Observer and Publish/Subscribe?

In **Observer**, the subject keeps a direct list of its observers and calls them itself. They know about each other.

In **Pub/Sub**, there is a middleman (a broker or event bus). Publishers send messages to a topic, and subscribers listen to that topic. Neither side knows about the other. Pub/Sub is common across services (Redis Pub/Sub, Kafka, SNS), while Observer is usually inside one process.

## 38: What is the Strategy pattern?

Strategy defines a family of algorithms, puts each one in its own class or function, and lets you switch between them at runtime. It is a clean way to replace long `if/else` or `switch` blocks.

```ts
type ShippingStrategy = (weightKg: number) => number;

const standard: ShippingStrategy = (w) => 5 + w * 1;
const express: ShippingStrategy = (w) => 15 + w * 2;

function shippingCost(weight: number, strategy: ShippingStrategy) {
  return strategy(weight);
}

shippingCost(3, express); // 21
```

In JavaScript, a strategy is often just a function.

## 39: What is the Command pattern?

Command turns a request into an object. That object holds everything needed to run the action later. Because the action is now data, you can queue it, log it, retry it or undo it. Text editor undo, job queues and Redux actions are all close to this idea.

```ts
interface Command {
  execute(): void;
  undo(): void;
}

class AddTextCommand implements Command {
  constructor(
    private doc: string[],
    private text: string,
  ) {}
  execute() {
    this.doc.push(this.text);
  }
  undo() {
    this.doc.pop();
  }
}
```

## 40: What is the Iterator pattern?

Iterator gives a standard way to go through the items of a collection one by one, without exposing how the collection is stored. In JavaScript it is built into the language: any object with a `[Symbol.iterator]()` method works with `for...of`, spread and destructuring.

```ts
class Range {
  constructor(
    private from: number,
    private to: number,
  ) {}

  *[Symbol.iterator]() {
    for (let i = this.from; i <= this.to; i++) yield i;
  }
}

for (const n of new Range(1, 3)) console.log(n); // 1 2 3
```

## 41: What is the State pattern?

State lets an object change its behavior when its internal state changes, by moving each state's logic into its own class. Instead of one class full of `if (status === "draft")` checks, you have a `DraftState`, `PublishedState` and so on. It is related to finite state machines.

```ts
interface OrderState {
  next(order: Order): void;
}

class Pending implements OrderState {
  next(order: Order) {
    order.state = new Shipped();
  }
}

class Shipped implements OrderState {
  next(order: Order) {
    order.state = new Delivered();
  }
}

class Delivered implements OrderState {
  next() {
    throw new Error("Order already delivered");
  }
}

class Order {
  state: OrderState = new Pending();
  advance() {
    this.state.next(this);
  }
}
```

## 42: What is the Template Method pattern?

Template Method defines the steps of an algorithm in a base class and lets subclasses fill in some of the steps. The order of the steps is fixed in one place.

```ts
abstract class DataExporter {
  export() {
    const data = this.load();
    const formatted = this.format(data);
    this.save(formatted);
  }

  protected load() {
    return [{ id: 1 }];
  }
  protected abstract format(data: object[]): string;
  protected save(output: string) {
    console.log(output);
  }
}

class CsvExporter extends DataExporter {
  protected format(data: object[]) {
    return data.map((row) => Object.values(row).join(",")).join("\n");
  }
}
```

## 43: What is the Chain of Responsibility pattern?

Chain of Responsibility passes a request along a chain of handlers. Each handler decides to handle it, change it, stop it or pass it to the next one. Express and Koa middleware is a well-known example: auth, logging and validation run one after another, and any of them can stop the request.

```ts
import express from "express";

const app = express();

app.use((req, res, next) => {
  if (!req.headers.authorization) return res.status(401).end();
  next(); // pass to the next handler
});
```

## 44: What is the Mediator pattern?

Mediator puts the communication between many objects into one central object. Instead of each object talking to every other object (many-to-many), they all talk only to the mediator. A chat room is a common example: users send messages to the room, and the room delivers them. It reduces direct dependencies, but the mediator itself can grow too big if you're not careful.

## 45: What is the Memento pattern?

Memento saves a snapshot of an object's state so you can restore it later, without exposing the object's internals. It is used for undo/redo and "save points".

```ts
class Editor {
  constructor(private content = "") {}

  type(text: string) {
    this.content += text;
  }
  save() {
    return { content: this.content }; // memento
  }
  restore(m: { content: string }) {
    this.content = m.content;
  }
}
```

## 46: What is the Visitor pattern?

Visitor lets you add new operations to a set of classes without changing those classes. The operation lives in a separate visitor object, and each element "accepts" the visitor and calls the right method on it. It is common in compilers and tools that walk syntax trees (Babel and ESLint plugins use visitors over the AST). The downside is that adding a new element type means updating every visitor.

## 47: What is the Null Object pattern?

Null Object replaces `null` with an object that has the same interface but does nothing. This removes a lot of `if (x !== null)` checks.

```ts
interface Logger {
  log(msg: string): void;
}

class ConsoleLogger implements Logger {
  log(msg: string) {
    console.log(msg);
  }
}

class NullLogger implements Logger {
  log() {}
}

function run(logger: Logger = new NullLogger()) {
  logger.log("started"); // safe, no null check
}
```

## 48: What is dependency injection?

Dependency injection (DI) means a class receives the things it needs from outside, instead of creating them itself. Usually they come through the constructor. This makes the class easier to test (you can pass fakes) and easier to change.

```ts
// Without DI: hard to test
class ReportService {
  private db = new PostgresClient();
}

// With DI
class ReportServiceDI {
  constructor(private db: Database) {}
}

const service = new ReportServiceDI(new FakeDatabase());
```

Frameworks like Angular and NestJS have DI containers that create and pass these dependencies for you.

## 49: What is Inversion of Control?

Inversion of Control (IoC) means that your code doesn't control the flow or the creation of objects; a framework or container does, and it calls your code. "Don't call us, we'll call you." Dependency injection is one form of IoC. Event handlers, lifecycle hooks in React or Angular, and Express route handlers are also IoC: you write the function, the framework decides when to run it.

## 50: What is a service locator and why do many people call it an anti-pattern?

A service locator is a central registry that code asks for its dependencies: `const db = Locator.get("db")`. It works, but the dependencies are hidden inside the methods instead of being visible in the constructor. You can't tell what a class needs by looking at its signature, and tests have to set up the global registry. Dependency injection is usually preferred because it makes dependencies explicit.

## 51: What is the Repository pattern?

A repository hides the details of data storage behind a collection-like interface. The business code calls `userRepo.findById(id)` and doesn't know if the data comes from Postgres, MongoDB or an in-memory map.

```ts
interface UserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<void>;
}

class InMemoryUserRepository implements UserRepository {
  private users = new Map<string, User>();

  async findById(id: string) {
    return this.users.get(id) ?? null;
  }
  async save(user: User) {
    this.users.set(user.id, user);
  }
}
```

It makes testing easier and keeps SQL or ORM code in one place.

## 52: What is the Unit of Work pattern?

Unit of Work tracks all the changes made during one business operation (new, changed and deleted objects) and saves them together in one transaction at the end. Either everything is saved or nothing is. ORMs like Entity Framework, Hibernate and MikroORM implement it for you; in others you usually get the same effect by wrapping the work in a transaction.

## 53: What is a DTO?

A DTO (Data Transfer Object) is a simple object that only carries data between layers or over the network. It has no business logic. DTOs let you control exactly what goes in and out of an API, so you don't leak internal fields like password hashes.

```ts
class UserResponseDto {
  constructor(
    public id: string,
    public name: string,
    public email: string,
  ) {}
}
```

## 54: What is MVC?

MVC (Model-View-Controller) splits an application into three parts:

- **Model:** the data and business rules.
- **View:** what the user sees.
- **Controller:** takes user input, updates the model and picks the view.

It is common in server-side frameworks like Ruby on Rails, ASP.NET MVC, Laravel and Spring MVC. In an Express or NestJS API, controllers handle requests and the "view" is usually JSON.

## 55: What is MVVM?

MVVM (Model-View-ViewModel) is similar to MVC, but the ViewModel exposes data and commands that the View binds to directly. When the ViewModel changes, the View updates by itself through data binding. Angular components, Vue and WPF apps follow this style quite closely.

## 56: What is MVP?

MVP (Model-View-Presenter) puts a Presenter between the View and the Model. The View is passive: it shows what the Presenter tells it and forwards user actions to the Presenter. Because the View is so thin, the Presenter is easy to unit test. It was popular in Android and WinForms apps before MVVM became more common.

## 57: What is a layered architecture?

Layered (n-tier) architecture splits code into horizontal layers, each with its own job. A typical setup:

1. **Presentation:** controllers, UI.
2. **Application / service:** use cases, business flow.
3. **Domain:** business rules and entities.
4. **Data access:** repositories, database code.

Each layer only calls the layer below it. It is easy to understand and is the default for many projects. The risk is that layers become thin pass-throughs, or that all logic ends up in the service layer.

## 58: What is software architecture?

Software architecture is the high-level structure of a system: the main parts, how they talk to each other, where data lives, and the rules for how the system should grow. It covers the decisions that are hard and expensive to change later, like monolith vs microservices, which database to use, or sync vs async communication. Good architecture is mostly about trade-offs that fit the team and the business, not about following a trend.

## 59: What is the difference between architecture and design?

There is no strict line, but usually:

- **Architecture** is about the big picture: services, databases, communication, deployment, and qualities like scalability and availability.
- **Design** is about the inside of a component: classes, functions, patterns and data structures.

Architecture decisions are harder to undo. Design decisions inside one module are cheaper to change.

## 60: What is a monolith?

A monolith is an application built and deployed as one unit. All features share one codebase, one process and usually one database. Monoliths are simple to develop, test and deploy at the start, and calls between features are just function calls. Problems show up when the codebase and team get very large: slow builds, risky deploys, and the whole app has to scale together.

## 61: What are microservices?

Microservices split an application into small, independently deployable services, each owning one business area (orders, payments, users) and usually its own database. They talk over the network with HTTP, gRPC or messages.

Pros: teams can work and deploy separately, services can scale on their own, and a failure can be contained to one service.
Cons: network calls fail, data is spread out, debugging is harder, and you need good DevOps, monitoring and tracing.

## 62: What is a modular monolith?

A modular monolith is a single deployable app that is split inside into well-separated modules with clear boundaries. Each module has its own public API and ideally its own data, and other modules can't reach into its internals. You keep the simple deployment of a monolith but get much of the structure of microservices. It is a common starting point, and modules can later be pulled out into services if needed.

## 63: What is the client-server model?

In the client-server model, clients (browsers, mobile apps) send requests and a server processes them and sends responses. The server holds the shared data and logic. Almost every web app works this way. It is different from peer-to-peer, where every node can act as both client and server.

## 64: What is a three-tier architecture?

Three-tier architecture splits a system into three physical tiers:

1. **Presentation tier:** the front end (browser, mobile app).
2. **Application tier:** the back end with business logic (Node.js, Java, .NET).
3. **Data tier:** the database.

Each tier can be scaled and deployed separately. This is the classic setup of most web apps.

## 65: What is serverless?

Serverless means you run code without managing servers. You deploy functions (AWS Lambda, Azure Functions, Google Cloud Run functions, Cloudflare Workers) and the cloud provider runs them on demand, scales them, and bills you per request or per run time. Servers still exist, you just don't manage them. It is good for spiky or event-driven workloads, but has limits like cold starts, max run time and vendor lock-in.

## 66: What is SOA and how is it different from microservices?

SOA (Service-Oriented Architecture) also splits a system into services, and it was popular in big companies in the 2000s. SOA services were often larger, shared databases, and talked through a central Enterprise Service Bus (ESB) that held a lot of logic. Microservices are smaller, own their data, and prefer "smart endpoints and dumb pipes": the logic stays in the services, and the network just moves messages.

## 67: What is event-driven architecture?

In event-driven architecture, components communicate by producing and reacting to events, like `OrderPlaced` or `UserSignedUp`. The producer doesn't know who will react. Other services subscribe and do their part: send an email, update stock, start shipping. This lowers coupling and makes it easy to add new reactions, but the flow is harder to follow and data becomes eventually consistent.

## 68: What is the difference between horizontal and vertical scaling?

- **Vertical scaling (scale up):** give one machine more CPU, RAM or faster disk. Simple, but there is a hardware limit and it is still one point of failure.
- **Horizontal scaling (scale out):** add more machines and spread the load. It can grow much further and gives redundancy, but the app has to be designed for it (stateless servers, shared storage, load balancing).

## 69: What is a load balancer?

A load balancer sits in front of a group of servers and spreads incoming requests across them. It also checks server health and stops sending traffic to servers that are down. Examples: Nginx, HAProxy, AWS Elastic Load Balancing, Google Cloud Load Balancing. It is the main building block for horizontal scaling and high availability.

## 70: What load balancing algorithms do you know?

- **Round robin:** each server in turn.
- **Weighted round robin:** stronger servers get more requests.
- **Least connections:** send to the server with the fewest active connections.
- **Least response time:** send to the fastest server.
- **IP hash:** the same client IP goes to the same server.
- **Random** or **power of two choices:** pick two random servers and use the less busy one.

## 71: What is the difference between stateless and stateful services?

A **stateless** service doesn't keep client data in memory between requests. Any instance can handle any request, so you can add or remove instances freely. A **stateful** service keeps data in memory (sessions, open connections, game state), so a client must return to the same instance, and losing that instance loses the data. The usual advice is to keep app servers stateless and put state in a database, cache or another store built for it.

## 72: What is caching?

Caching means storing a copy of data in a faster place so you don't have to compute or fetch it again. For example, you can keep the result of a slow database query in Redis for 60 seconds. Caching lowers latency and load on the database, but you have to deal with stale data and decide when to invalidate it.

## 73: Where can you cache data in a web application?

- **Browser cache:** HTTP caching with `Cache-Control` and `ETag`.
- **CDN:** static files and sometimes API responses close to users.
- **Reverse proxy:** Nginx or Varnish in front of the app.
- **Application memory:** a simple in-process map or LRU cache.
- **Distributed cache:** Redis or Memcached shared by all instances.
- **Database:** its own buffer pool, plus materialized views.

## 74: What is a CDN?

A CDN (Content Delivery Network) is a network of servers spread around the world that keeps copies of your content close to users. When someone in Tokyo loads your site, they get images, JS and CSS from a nearby server instead of your origin in Europe. This cuts latency and takes load off your servers. Examples: Cloudflare, Akamai, Amazon CloudFront, Fastly.

## 75: What is the cache-aside pattern?

Cache-aside (lazy loading) is the most common caching strategy. The application checks the cache first. On a miss, it reads from the database and puts the result in the cache.

```ts
async function getProduct(id: string) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);

  const product = await db.product.findUnique({ where: { id } });
  if (product) {
    await redis.set(`product:${id}`, JSON.stringify(product), { EX: 300 });
  }
  return product;
}
```

When the product changes, you delete the cache key so the next read loads fresh data.

## 76: What is TTL and why is cache invalidation hard?

TTL (time to live) is how long a cached item stays valid before it expires. Cache invalidation is hard because the cache and the source of truth can get out of sync: updates come from many places, deletes can fail, and requests can race each other so an old value gets written back after a new one. A short TTL limits how long data stays wrong, but it also lowers the hit rate. Most systems combine a TTL with deleting keys on updates.

## 77: What is the difference between a forward proxy and a reverse proxy?

- A **forward proxy** sits in front of clients and sends requests to the internet for them. Used for company filtering, privacy or caching for users.
- A **reverse proxy** sits in front of servers and receives requests from the internet for them. Used for load balancing, TLS termination, caching, compression and hiding internal servers. Nginx is a common reverse proxy.

## 78: What is an API gateway?

An API gateway is a single entry point for clients in front of many back-end services. It routes requests to the right service and handles shared concerns like authentication, rate limiting, logging, CORS and sometimes response aggregation. Examples: Kong, AWS API Gateway, Azure API Management, or a custom gateway written in Node.js. Keep business logic out of it, or it becomes a bottleneck that every team depends on.

## 79: What is REST?

REST (Representational State Transfer) is an architectural style for APIs over HTTP. You work with resources identified by URLs, and use HTTP methods to act on them: `GET /users/1`, `POST /users`, `PATCH /users/1`, `DELETE /users/1`. REST APIs are stateless, use standard status codes and can use HTTP caching. In practice most "REST" APIs are just JSON over HTTP that follows these ideas loosely.

## 80: What is RPC and what is gRPC?

RPC (Remote Procedure Call) makes calling a function on another server look like calling a local function. gRPC is a popular modern RPC framework from Google. It uses HTTP/2 and Protocol Buffers (a compact binary format), generates client and server code from a `.proto` file, and supports streaming. It is fast and strongly typed, so it is common for service-to-service calls. Browsers can't call gRPC directly without gRPC-Web or a proxy.

## 81: When would you choose GraphQL over REST?

GraphQL lets the client ask for exactly the fields it needs in one request. It is a good fit when you have many different clients (web, mobile) with different data needs, or when a screen needs data from many resources. REST is simpler, works well with HTTP caching and is easier to rate limit and monitor. For a simple CRUD API, REST is usually enough.

## 82: What is a webhook?

A webhook is an HTTP callback: when something happens in system A, it sends an HTTP POST to a URL that system B registered. For example, Stripe calls your `/webhooks/stripe` endpoint when a payment succeeds. It saves B from asking A every few seconds whether anything changed. The receiver must check the signature, respond quickly, and handle duplicate deliveries.

## 83: What is the difference between polling, long polling, WebSockets and Server-Sent Events?

- **Polling:** the client asks the server every few seconds. Simple but wasteful.
- **Long polling:** the client asks and the server holds the request open until there is new data or a timeout, then the client asks again.
- **WebSockets:** one long-lived, two-way connection. Good for chat, games and collaboration.
- **Server-Sent Events (SSE):** one long-lived HTTP connection where only the server sends events to the client. Simpler than WebSockets and reconnects by itself. Good for notifications, live feeds and streaming AI responses.

## 84: What is the difference between synchronous and asynchronous communication between services?

- **Synchronous:** service A calls B (HTTP or gRPC) and waits for the answer. It is simple, but A is now down whenever B is down or slow.
- **Asynchronous:** A sends a message to a queue or event bus and moves on. B processes it later. This decouples the services and smooths traffic spikes, but the result is not instant and you have to handle retries, duplicates and eventual consistency.

## 85: What is a message queue?

A message queue stores messages from producers until consumers process them. It lets services work at different speeds, absorbs traffic spikes, and keeps messages if a consumer is down. A typical use: the API puts "send welcome email" in a queue and returns right away, and a worker sends the email in the background.

## 86: What message brokers do you know?

- **RabbitMQ:** a classic broker with flexible routing (exchanges, queues), good for task queues.
- **Apache Kafka:** a distributed log built for high throughput and event streaming. Messages are kept for a set time and can be re-read.
- **Amazon SQS / SNS:** managed queue and pub/sub on AWS.
- **Redis:** has Pub/Sub and Streams, and libraries like BullMQ build job queues on top of it.
- **Google Pub/Sub, Azure Service Bus, NATS:** other common options.

## 87: What is the difference between a queue and a topic?

- A **queue** delivers each message to one consumer. If you have five workers, each message is processed by only one of them. Used for spreading work.
- A **topic** (pub/sub) delivers each message to every subscriber. If three services subscribe to `OrderPlaced`, all three get it. Used for broadcasting events.

## 88: What is the difference between SQL and NoSQL databases?

- **SQL (relational):** tables with a fixed schema, relations with joins, strong ACID transactions, and a powerful query language. Examples: PostgreSQL, MySQL, SQL Server.
- **NoSQL:** many kinds of non-relational stores with flexible schemas, often built to scale horizontally. Examples: MongoDB, Redis, Cassandra, DynamoDB.

SQL is a good default for most business apps. NoSQL fits specific needs like huge write volume, very flexible data, or simple key-based access at large scale.

## 89: What types of NoSQL databases are there?

- **Key-value:** Redis, DynamoDB. Fast lookups by key.
- **Document:** MongoDB, Couchbase. JSON-like documents.
- **Wide-column:** Cassandra, ScyllaDB, HBase. Large write-heavy datasets.
- **Graph:** Neo4j, Amazon Neptune. Data with many relationships.
- **Search engines:** Elasticsearch, OpenSearch. Full-text search.
- **Time-series:** InfluxDB, TimescaleDB. Metrics and events over time.

## 90: What is ACID?

ACID describes reliable database transactions:

- **Atomicity:** all steps succeed or none do.
- **Consistency:** a transaction moves the database from one valid state to another, keeping all rules and constraints.
- **Isolation:** transactions running at the same time don't interfere with each other.
- **Durability:** once committed, data survives crashes.

Bank transfers are the classic example: money must not leave one account without arriving in the other.

## 91: What is BASE?

BASE is a looser model used by many distributed NoSQL systems:

- **Basically Available:** the system answers even during failures.
- **Soft state:** data can change over time without new input, as replicas sync.
- **Eventually consistent:** if writes stop, all replicas will end up with the same data.

It trades strict consistency for availability and scale.

## 92: What is a database index?

An index is a separate data structure (usually a B-tree) that helps the database find rows quickly without scanning the whole table, like the index at the back of a book. Indexes make reads on the indexed columns much faster, but they use disk space and slow down writes, because every insert and update must also update the index.

```sql
CREATE INDEX idx_orders_user_id ON orders (user_id);
```

## 93: What is database replication?

Replication means keeping copies of the same data on more than one database server. It improves availability (if one server dies, another has the data) and read performance (reads can go to replicas). The trade-off is that replicas can lag behind, so a read right after a write might not see the new data.

## 94: What is primary-replica replication?

In primary-replica (also called leader-follower) replication, all writes go to one primary server. The primary sends its changes to one or more replicas, which handle reads. If the primary fails, one replica can be promoted to primary. This is the default setup for PostgreSQL, MySQL and MongoDB replica sets.

## 95: What is sharding?

Sharding splits data across several database servers, where each server (shard) holds only part of the data. For example, users with IDs 1 to 1 million on shard A and the rest on shard B. It lets you grow beyond what a single machine can store or handle. The downsides: queries across shards are hard, transactions across shards are hard, and picking a bad shard key can put most of the load on one shard.

## 96: What is the difference between vertical and horizontal partitioning?

- **Vertical partitioning:** split a table by columns. For example, move large `bio` and `avatar` columns to a separate table so the main `users` table stays small.
- **Horizontal partitioning:** split a table by rows. For example, orders from 2025 in one partition and orders from 2026 in another. When the partitions live on different servers, this is called sharding.

## 97: What is normalization and denormalization?

**Normalization** organizes data so each fact is stored only once, using separate tables connected by foreign keys. It avoids duplicated data and update mistakes.

**Denormalization** copies some data on purpose to make reads faster, for example storing `authorName` on each post so you don't need a join. It speeds up reads but you must keep the copies in sync. Write-heavy systems usually stay normalized; read-heavy systems often denormalize parts.

## 98: What is the CAP theorem?

The CAP theorem says that when a network partition happens in a distributed system (some nodes can't reach others), you must choose between:

- **Consistency:** every read gets the latest write or an error.
- **Availability:** every request gets a non-error response, even if the data may be old.

Partition tolerance isn't really optional, because networks do fail. So the real choice is: during a partition, do you refuse requests to stay correct (CP), or answer with possibly stale data (AP)? When there is no partition, a system can offer both.

## 99: What is the difference between strong and eventual consistency?

- **Strong consistency:** after a write is confirmed, every read sees it. Simple to reason about, but slower and less available in a distributed system.
- **Eventual consistency:** after a write, some reads might still see old data for a short time, but all copies will catch up. Faster and more available.

A bank balance needs strong consistency. A "like" counter can be eventually consistent.

## 100: What is the difference between latency and throughput?

- **Latency** is how long one request takes, for example 120 ms.
- **Throughput** is how many requests the system handles per unit of time, for example 5,000 requests per second.

They are related but not the same. Batching can raise throughput while making each item wait longer. When people talk about latency, they usually look at percentiles like p50, p95 and p99, not just the average.

## 101: What does "five nines" availability mean?

Availability is the percentage of time a system works. Each extra "nine" allows much less downtime:

| Availability | Downtime per year |
| ------------ | ----------------- |
| 99%          | about 3.65 days   |
| 99.9%        | about 8.8 hours   |
| 99.99%       | about 53 minutes  |
| 99.999%      | about 5.3 minutes |

Every extra nine costs a lot more in redundancy and process, so pick the level the business actually needs.

## 102: What are SLA, SLO and SLI?

- **SLI (Service Level Indicator):** a measured number, like the percentage of requests that succeed or p99 latency.
- **SLO (Service Level Objective):** an internal target for that number, like "99.9% of requests succeed over 30 days".
- **SLA (Service Level Agreement):** a contract with customers, with penalties (often refunds) if the promise is broken. SLAs are usually looser than SLOs so the team has room to react.

## 103: What is a single point of failure?

A single point of failure (SPOF) is any part of the system that brings everything down when it fails. Examples: one database server with no replica, one load balancer, one region, or even one engineer who is the only person who knows how to deploy. You remove SPOFs by adding redundancy and failover.

## 104: What are redundancy and failover?

**Redundancy** means having extra copies of components (servers, databases, network links) so one can fail without taking down the system. **Failover** is the process of switching to the backup when the main one fails. It can be **active-passive** (the backup waits idle until needed) or **active-active** (all copies serve traffic all the time).

## 105: What is a health check?

A health check is an endpoint or command that tells whether a service instance is working, for example `GET /health` returning `200 OK`. Load balancers and orchestrators like Kubernetes call it regularly and stop sending traffic to, or restart, instances that fail. A good health check is fast and checks only what that instance really needs to work.

## 106: What is rate limiting?

Rate limiting caps how many requests a client can make in a time window, for example 100 requests per minute per API key. It protects the system from abuse, bugs in clients and traffic spikes, and makes usage fair between users. When the limit is reached, the server usually returns `429 Too Many Requests`, often with a `Retry-After` header.

## 107: What is idempotency?

An operation is idempotent if doing it many times gives the same result as doing it once. `GET`, `PUT` and `DELETE` are meant to be idempotent in HTTP; `POST` is not. Idempotency matters because networks fail and clients retry. If "charge the card" is not idempotent, a retry can charge the customer twice. A common fix is an idempotency key that the server remembers.

## 108: What is retry with exponential backoff?

When a call fails with a temporary error, you retry it, but you wait longer after each failure: 100 ms, 200 ms, 400 ms and so on. Adding random "jitter" stops all clients from retrying at the same moment.

```ts
async function withRetry<T>(fn: () => Promise<T>, attempts = 5): Promise<T> {
  for (let i = 0; ; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i >= attempts - 1) throw err;
      const delay = Math.random() * 100 * 2 ** i; // full jitter
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}
```

Only retry errors that are likely temporary (timeouts, 503) and only operations that are safe to repeat.

## 109: Why do you need timeouts?

Without a timeout, a call to a slow or hung service can wait forever. Each waiting request holds a thread, connection or memory, and soon the calling service runs out of resources and fails too. Always set timeouts on HTTP calls, database queries and queue operations.

```ts
const res = await fetch("https://api.example.com/data", {
  signal: AbortSignal.timeout(3000),
});
```

## 110: What is the Circuit Breaker pattern?

A circuit breaker wraps calls to another service and tracks failures. After too many failures it "opens" and fails new calls right away, without calling the broken service. After a pause it lets a few test calls through ("half-open"). If they succeed, it closes again. This stops a failing service from dragging down its callers and gives it time to recover. Libraries like `opossum` (Node.js), Resilience4j (Java) and Polly (.NET) provide it.

## 111: What is observability?

Observability is how well you can understand what is happening inside a system from the data it produces. It is usually built on three kinds of data:

- **Logs:** records of individual events.
- **Metrics:** numbers over time, like request rate, error rate and latency.
- **Traces:** the path of one request across many services.

OpenTelemetry is the common open standard for collecting all three.

## 112: What is object storage?

Object storage (Amazon S3, Google Cloud Storage, Azure Blob Storage, Cloudflare R2) stores files as objects in buckets, each with a key and metadata. It is cheap, very durable and scales almost without limit. It is the standard place for user uploads, images, videos, backups and logs. You don't put these big files in your database; you store the file in object storage and keep only its key or URL in the database.

## 113: What role does DNS play in a system architecture?

DNS turns domain names into IP addresses. In architecture it is also used for:

- Pointing a domain at a load balancer or CDN.
- Simple load balancing with several records.
- Geo-based routing, so users go to the nearest region.
- Failover, by switching records when a region is down.

DNS records are cached based on their TTL, so changes don't apply everywhere at once.

## 114: How do you handle user sessions when you have many app servers?

There are two common options:

- **Sticky sessions:** the load balancer always sends a user to the same server. Easy, but if that server dies, the session is lost and load can be uneven.
- **Shared session store:** sessions live in Redis or a database that all servers read. Any server can handle any request. This is the usual choice.

A third option is stateless tokens like JWTs, where the session data travels with the request.

## 115: What are the trade-offs between server sessions and JWTs?

- **Server sessions:** the server stores session data and the client gets a random ID in a cookie. Easy to revoke (delete the session), but every request needs a store lookup.
- **JWT:** a signed token that contains the user data. Any service can check it without a database call, which suits distributed systems. But it is hard to revoke before it expires, so tokens should be short-lived and paired with refresh tokens.

## 116: What is the difference between authentication and authorization?

- **Authentication** answers "who are you?": login with a password, a passkey, or an identity provider.
- **Authorization** answers "what are you allowed to do?": checking roles or permissions before letting the user see or change data.

Authentication always comes first. A `401 Unauthorized` response really means "not authenticated", and `403 Forbidden` means "authenticated but not allowed".

## 117: What are OAuth 2.0 and OpenID Connect?

- **OAuth 2.0** is a standard for authorization. It lets an app get limited access to a user's resources on another service (an access token) without seeing the user's password. Example: an app reading your Google Calendar.
- **OpenID Connect (OIDC)** is built on top of OAuth 2.0 and adds authentication. It returns an ID token that says who the user is. "Sign in with Google" uses OIDC.

For browser apps, the recommended flow is Authorization Code with PKCE.

## 118: What is the difference between batch and stream processing?

- **Batch processing** handles a large set of data at once, on a schedule. Example: a nightly job that builds sales reports. Simple and efficient, but results are hours old.
- **Stream processing** handles each event as it arrives, in near real time. Example: fraud detection on each payment. Fresher results, but more complex to build and run.

## 119: What are background workers and scheduled jobs?

Background workers are processes that run tasks outside the request/response cycle, like sending emails, resizing images or generating PDFs. The API puts a job in a queue and returns fast; workers pick jobs up and process them. Scheduled jobs (cron jobs) run at fixed times, like cleaning old data every night. In a system with many instances, make sure a scheduled job runs on only one instance, or that running it twice is safe.

## 120: What is the difference between offset pagination and cursor pagination?

- **Offset pagination:** `?page=3&limit=20`, which becomes `OFFSET 40 LIMIT 20` in SQL. Easy, and you can jump to any page. But it gets slow on big tables, and items shift if rows are added or deleted while paging.
- **Cursor pagination:** `?after=<lastId>&limit=20`, which becomes `WHERE id > :lastId ORDER BY id LIMIT 20`. Fast with an index and stable under changes, but you can't jump to page 50. It is the better choice for feeds and large lists.

## 121: How can you version an API?

Common ways:

- **In the URL:** `/v1/users`, `/v2/users`. Most common and easy to see.
- **In a header:** `Accept: application/vnd.myapp.v2+json` or a custom header.
- **In a query parameter:** `/users?version=2`.

Whatever you pick, try to avoid breaking changes as long as you can. Adding new fields is safe; removing or renaming them is not.

## 122: What role do containers play in modern architecture?

Containers (usually Docker) package an app with everything it needs to run, so it behaves the same on a laptop, in CI and in production. They start quickly and use fewer resources than virtual machines. Orchestrators like Kubernetes, or managed services like AWS ECS and Google Cloud Run, then run many containers, restart failed ones, scale them and route traffic to them. Containers made microservices much easier to run.

## 123: What is the Twelve-Factor App?

The Twelve-Factor App is a set of guidelines for building apps that run well in the cloud. Some key points:

- Store config in environment variables, not in code.
- Treat backing services (databases, queues) as attached resources you can swap by changing config.
- Run the app as stateless processes.
- Treat logs as event streams written to stdout.
- Keep dev, staging and production as similar as possible.
- Scale by running more processes.

## 124: Why should configuration be kept outside the code?

The same build should run in every environment (dev, staging, production), with only the config changing. If you hardcode a database URL, you need a new build for each environment and you risk committing secrets to Git. Put config in environment variables or a config service, and put secrets in a secret manager like AWS Secrets Manager, HashiCorp Vault or Kubernetes Secrets.

## 125: What is the difference between a monorepo and a polyrepo?

- **Monorepo:** many projects or services in one Git repository. Easy to share code, make changes across projects in one commit, and keep tools consistent. Needs good tooling (Nx, Turborepo, pnpm workspaces) to stay fast.
- **Polyrepo:** each project has its own repository. Clear ownership and independent pipelines, but sharing code and making changes across repos is harder.

This is about how code is stored, not how it is deployed: a monorepo can still contain many independently deployed microservices.

## 126: What is a back-of-the-envelope estimation?

It is a quick, rough calculation to check if a design makes sense. For example: 10 million daily users, each making 20 requests a day, is 200 million requests per day. Divided by about 86,400 seconds, that is around 2,300 requests per second on average, maybe 5 to 10 times that at peak. You do the same for storage and bandwidth. The goal is to know if you need one server or a hundred, not to get exact numbers.

## 127: What is the difference between functional and non-functional requirements?

- **Functional requirements** describe what the system does: "users can upload photos", "users can follow other users".
- **Non-functional requirements** describe how well it does it: latency, availability, scalability, security, cost, maintainability.

Non-functional requirements usually drive the architecture. A photo app for 100 users and one for 100 million users have the same features but very different designs.

## 128: How do you approach a system design interview question?

A common order:

1. **Clarify requirements:** features, users, scale, what matters most.
2. **Estimate:** traffic, storage, read/write ratio.
3. **Define the API:** main endpoints or operations.
4. **Sketch the high-level design:** clients, load balancer, services, databases, caches, queues.
5. **Design the data model.**
6. **Go deep** on one or two hard parts.
7. **Discuss bottlenecks, failures and trade-offs.**

Talk out loud and explain why you choose each piece.

## 129: What is a bottleneck?

A bottleneck is the part of the system that limits how much it can handle. Making other parts faster doesn't help until you fix it. Common bottlenecks are the database (CPU, locks, slow queries), network bandwidth, a single-threaded process, or a third-party API with a rate limit. You find them by measuring (metrics, profiling, load tests), not by guessing.

## 130: What is the difference between a read-heavy and a write-heavy system?

- **Read-heavy:** many more reads than writes, like a news site or product catalog. Use caching, CDNs, read replicas and denormalized data.
- **Write-heavy:** lots of writes, like logging, IoT sensors or analytics events. Use queues to buffer writes, batch inserts, append-only storage, sharding, and databases built for writes like Cassandra or ClickHouse.

Knowing the ratio early is one of the most useful things in a design discussion.

## 131: What is connection pooling?

Opening a database connection is slow (TCP, TLS and authentication). A connection pool keeps a number of open connections and reuses them for many queries. Each request borrows a connection and gives it back when done. Most database drivers and ORMs have a pool built in. You set its size so the app has enough connections but doesn't go over the database's limit.

```ts
import { Pool } from "pg";

const pool = new Pool({ max: 10 });
const { rows } = await pool.query("SELECT * FROM users WHERE id = $1", [id]);
```

## 132: What is a key-value store?

A key-value store saves data as pairs: a unique key and a value. You read and write by key, and it is extremely fast. Redis is the most famous; DynamoDB and etcd are others. It is used for caching, sessions, rate limit counters, feature flags and leaderboards. It is not good for complex queries across many records.

## 133: What is separation of concerns?

Separation of concerns means splitting a program into parts where each part handles one concern: UI, business rules, data access, logging and so on. When concerns are mixed (SQL inside a React component, for example), changing one thing breaks another. Layers, modules, MVC and microservices are all ways to apply this idea.

## 134: What is the Law of Demeter?

The Law of Demeter (principle of least knowledge) says an object should only talk to its close friends, not to friends of friends. Long chains like `order.getCustomer().getAddress().getCity()` tie your code to the inner structure of many classes. A change anywhere in the chain breaks it. A better option is to ask the nearest object for what you need, like `order.shippingCity()`.

## 135: What is the Module pattern?

The Module pattern groups related code and keeps some of it private, exposing only a public API. Before ES modules, JavaScript used closures (an IIFE) for this. Today ES modules do the same job: anything you don't `export` is private to the file.

```ts
// counter.ts
let count = 0; // private

export function increment() {
  count++;
  return count;
}
```

## 136: What is a mixin?

A mixin is a way to add a set of methods to a class without using normal inheritance. In TypeScript you write a function that takes a class and returns a new class that extends it.

```ts
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
  };
}

class User {
  constructor(public name: string) {}
}

const TimestampedUser = Timestamped(User);
const u = new TimestampedUser("Ann");
console.log(u.createdAt);
```

Mixins can make code hard to follow when there are many of them, so composition is often a cleaner choice.

## 137: What is the middleware pattern?

Middleware is a function that sits in the request pipeline and can read or change the request, end it, or pass it to the next step. It is a form of Chain of Responsibility. Express, Koa, NestJS, Next.js and Redux all use middleware for things like logging, authentication, parsing bodies and error handling.

```ts
app.use((req, res, next) => {
  const start = Date.now();
  res.on("finish", () =>
    console.log(req.method, req.url, Date.now() - start, "ms"),
  );
  next();
});
```

## 138: What is a plugin architecture?

A plugin (microkernel) architecture has a small core system and lets extra features be added as plugins that follow a defined interface. The core doesn't need to change when you add a plugin. VS Code extensions, Webpack and Vite plugins, ESLint rules and WordPress plugins all work this way. It is good for products that many people need to extend in different ways.

## 139: What does "program to an interface, not an implementation" mean?

It means your code should depend on what an object can do (its interface), not on its exact class. If a function needs something that can save files, accept a `FileStorage` interface instead of an `S3Storage` class. Then you can pass local disk storage in development, S3 in production and a fake in tests, without changing the function.

## 140: What is the difference between a thin client and a thick client?

- A **thin client** does little work itself. The server renders pages and holds the logic. Classic server-rendered web apps are thin clients.
- A **thick (fat) client** does a lot of work locally: rendering, state, sometimes offline data. Single-page apps and mobile apps are thick clients.

Many modern web apps mix both: render on the server for fast first load, then run as an app in the browser.

## 141: What is the difference between client-side rendering and server-side rendering?

- **Client-side rendering (CSR):** the server sends a mostly empty HTML page and JavaScript builds the UI in the browser. Simple hosting and rich interactivity, but slower first paint and weaker SEO by default.
- **Server-side rendering (SSR):** the server builds the HTML for each request, so users and search engines get content right away. The page then "hydrates" in the browser to become interactive. It needs a running server and more server CPU.

Frameworks like Next.js, Nuxt and Angular SSR let you choose per page.

## 142: What are feature flags?

Feature flags (feature toggles) let you turn features on or off at runtime without deploying new code. You can ship unfinished code hidden behind a flag, enable a feature for 5% of users, run A/B tests, or quickly turn off a broken feature. Tools like LaunchDarkly, Unleash, Flagsmith or a simple config table are common. Old flags should be removed once a feature is fully released, or the code fills up with dead branches.

## 143: What is blue-green deployment?

You run two identical production environments: blue (live) and green (new version). You deploy to green, test it, then switch all traffic from blue to green at once, usually at the load balancer or DNS. If something goes wrong, you switch back to blue. Rollback is fast, but you need double the resources during the deploy, and database changes must work with both versions.

## 144: What is a canary deployment?

In a canary deployment, you release the new version to a small part of traffic first, say 5%, and watch error rates and latency. If it looks good, you slowly increase traffic to 25%, 50% and 100%. If it looks bad, you roll back, and only a few users were affected. The name comes from canaries used in coal mines to detect gas early.

## 145: What is a rolling deployment?

A rolling deployment updates instances a few at a time. For example, with ten servers, you take two out of the load balancer, update them, put them back, and continue with the next two. There is no downtime and no need for extra servers. But for a while both old and new versions run at the same time, so they must be compatible with each other and with the database. This is the default strategy in Kubernetes.

## 146: What is service discovery?

In a system with many services that scale up and down, IP addresses change all the time. Service discovery lets a service find the current address of another one by name. It can be:

- **Client-side:** the client asks a registry (Consul, Eureka) and picks an instance.
- **Server-side:** the client calls a fixed address (a load balancer or DNS name) that knows where instances are.

In Kubernetes, a Service gets a stable DNS name like `orders.default.svc.cluster.local` that routes to healthy pods.

## 147: What is an ORM?

An ORM (Object-Relational Mapper) maps database tables to classes or objects in your code, so you can work with data using your programming language instead of raw SQL. Examples: Prisma, TypeORM, Sequelize, Drizzle, Hibernate and Entity Framework. ORMs speed up development and help prevent SQL injection, but they can generate slow queries (like the N+1 problem) if you don't check what SQL they produce.

## 148: What is the difference between Active Record and Data Mapper?

- **Active Record:** each model object knows how to save itself. `user.save()`. Simple and fast to write. Used by Ruby on Rails, Laravel Eloquent and Sequelize.
- **Data Mapper:** models are plain objects with no database knowledge, and a separate mapper or repository saves them. `userRepository.save(user)`. Keeps business logic independent of the database and is easier to test. Used by Hibernate, Doctrine and Entity Framework, and TypeORM supports both.

Active Record works well for CRUD apps. Data Mapper fits apps with complex business logic.

## 149: What is a God Object?

A God Object is a class that knows too much and does too much, like a `Manager` or `Utils` class with thousands of lines that every other part of the code depends on. It breaks the Single Responsibility Principle, it is hard to test, and almost any change touches it, which leads to merge conflicts and bugs. The fix is to split it into smaller classes, each with one clear job.

## 150: What is premature optimization?

Premature optimization means making code faster or more scalable before you know it is a problem. Donald Knuth called it "the root of all evil" because it adds complexity, takes time and often targets the wrong part. In architecture, an example is starting a small project with microservices, Kafka and sharding "for scale". Build the simple version, measure, then optimize the real bottlenecks.

# Moderate Questions (151-300)

## 151: How do you decide between Factory Method and Abstract Factory?

Use **Factory Method** when you need to create one kind of product and want subclasses (or a config value) to decide the concrete type. Use **Abstract Factory** when you need to create several related products that must match each other, like a button, input and modal for the same theme, or a connection, command and transaction for the same database driver. If you only have one product, Abstract Factory is overkill. In practice, a plain function that returns the right object covers most cases.

## 152: What is the difference between Adapter, Decorator and Proxy?

All three wrap another object, but for different reasons:

- **Adapter** changes the interface so an incompatible object fits what the client expects.
- **Decorator** keeps the same interface and adds new behavior, and you can stack several.
- **Proxy** keeps the same interface and controls access: lazy loading, caching, permissions or remote calls.

A quick test: if the interface changes, it is an adapter. If it stays the same and you add features, it is a decorator. If it stays the same and you guard or delay access, it is a proxy.

## 153: What is the difference between Strategy and State?

The code structure looks almost the same: a context object holds a reference to an interface with several implementations. The difference is who switches it:

- In **Strategy**, the client chooses the algorithm from outside, and the strategies don't know about each other.
- In **State**, the state objects themselves usually trigger moves to the next state, and they know about each other.

Example: choosing a sorting algorithm is Strategy. An order moving from `Pending` to `Paid` to `Shipped` is State.

## 154: What is the difference between Facade and Mediator?

- A **Facade** gives a simple interface to a subsystem. The subsystem classes don't know the facade exists, and communication goes one way: client to facade to subsystem.
- A **Mediator** coordinates communication between peer objects. The objects know about the mediator and talk through it, so communication goes in many directions.

Facade simplifies usage. Mediator reduces the connections between objects that work together.

## 155: How can the Observer pattern cause memory leaks and how do you avoid them?

The subject keeps references to its observers. If an observer (a component, for example) is destroyed but never unsubscribes, the subject still holds it, so it can't be garbage collected and its callback keeps running. This is common with DOM listeners, `EventEmitter`, RxJS subscriptions and global stores.

Ways to avoid it:

- Always return and call an unsubscribe function.
- Unsubscribe in cleanup hooks (`useEffect` cleanup, `ngOnDestroy`, or `takeUntilDestroyed()` in Angular).
- Use `AbortController` with `addEventListener` to remove many listeners at once.

```ts
const controller = new AbortController();
window.addEventListener("resize", onResize, { signal: controller.signal });
window.addEventListener("scroll", onScroll, { signal: controller.signal });

// later
controller.abort(); // removes both listeners
```

## 156: How would you implement a typed event emitter?

```ts
type Events = {
  login: { userId: string };
  logout: void;
};

class TypedEmitter<T extends Record<string, unknown>> {
  private handlers: { [K in keyof T]?: Set<(payload: T[K]) => void> } = {};

  on<K extends keyof T>(event: K, fn: (payload: T[K]) => void) {
    (this.handlers[event] ??= new Set()).add(fn);
    return () => this.handlers[event]?.delete(fn);
  }

  emit<K extends keyof T>(event: K, payload: T[K]) {
    this.handlers[event]?.forEach((fn) => fn(payload));
  }
}

const bus = new TypedEmitter<Events>();
bus.on("login", ({ userId }) => console.log(userId));
bus.emit("login", { userId: "42" });
```

The generic map makes TypeScript check that the payload matches the event name.

## 157: How do you create a singleton in Node.js, and when does it stop being a single instance?

The simplest way is to export an instance from a module. Node caches modules after the first `import`, so everyone gets the same object.

```ts
// db.ts
import { Pool } from "pg";
export const pool = new Pool({ connectionString: process.env.DATABASE_URL });
```

It stops being a single instance when:

- The module is loaded twice from different paths or package copies (two versions in `node_modules`).
- You run many processes (cluster mode, PM2, several containers). Each process has its own instance.
- Hot reload in development (Next.js, for example) re-runs the module, which is why people store a Prisma client on `globalThis` in dev.

A singleton is "one per process", never "one per system".

## 158: How do you make a builder that forces required fields at compile time?

You can track which fields are set with TypeScript generics, so `build()` only exists when required fields are present.

```ts
type Email = { to: string; subject: string; body?: string };

class EmailBuilder<T extends Partial<Email> = {}> {
  constructor(private data: T = {} as T) {}

  to(to: string) {
    return new EmailBuilder({ ...this.data, to });
  }
  subject(subject: string) {
    return new EmailBuilder({ ...this.data, subject });
  }
  body(body: string) {
    return new EmailBuilder({ ...this.data, body });
  }

  build(this: EmailBuilder<Email>): Email {
    return this.data;
  }
}

new EmailBuilder().to("a@b.com").subject("Hi").build(); // ok
// new EmailBuilder().to("a@b.com").build(); // compile error
```

For many cases, a plain object literal with a typed interface is enough and simpler than a builder.

## 159: How do you implement undo and redo with the Command pattern?

Keep two stacks. Running a command pushes it on the undo stack and clears the redo stack. Undo pops from undo, calls `undo()` and pushes onto redo. Redo does the opposite.

```ts
interface Command {
  execute(): void;
  undo(): void;
}

class History {
  private undoStack: Command[] = [];
  private redoStack: Command[] = [];

  run(cmd: Command) {
    cmd.execute();
    this.undoStack.push(cmd);
    this.redoStack = [];
  }

  undo() {
    const cmd = this.undoStack.pop();
    if (!cmd) return;
    cmd.undo();
    this.redoStack.push(cmd);
  }

  redo() {
    const cmd = this.redoStack.pop();
    if (!cmd) return;
    cmd.execute();
    this.undoStack.push(cmd);
  }
}
```

An alternative is the Memento approach: save snapshots of state instead of inverse operations. Snapshots are simpler but use more memory.

## 160: How would you build your own middleware pipeline?

```ts
type Context = { path: string; user?: string; body?: unknown };
type Next = () => Promise<void>;
type Middleware = (ctx: Context, next: Next) => Promise<void>;

function compose(middlewares: Middleware[]) {
  return (ctx: Context) => {
    const dispatch = (i: number): Promise<void> => {
      const fn = middlewares[i];
      if (!fn) return Promise.resolve();
      return fn(ctx, () => dispatch(i + 1));
    };
    return dispatch(0);
  };
}

const run = compose([
  async (ctx, next) => {
    console.log("start", ctx.path);
    await next();
    console.log("end", ctx.path);
  },
  async (ctx, next) => {
    ctx.user = "ann";
    await next();
  },
]);

run({ path: "/home" });
```

This is close to how Koa works. Because each middleware awaits `next()`, it can run code both before and after the rest of the chain.

## 161: When is the Composite pattern a good fit, and when is it not?

It fits when your data is naturally a tree and clients want to treat leaves and groups the same: file systems, menus with submenus, org charts, UI component trees, permission groups, or pricing a bundle of products. It is a poor fit when leaves and containers need very different operations, because you end up with methods like `add()` on a leaf that just throw errors. Also watch out for deep trees and recursive operations on very large structures, which can be slow or overflow the stack.

## 162: How do generators help implement the Iterator pattern?

A generator function (`function*`) returns an iterator automatically and keeps its own state between calls. This makes it easy to iterate lazily over data that is large, infinite or loaded in pages.

```ts
async function* fetchAllUsers() {
  let cursor: string | null = null;
  do {
    const url = `/api/users${cursor ? `?after=${cursor}` : ""}`;
    const page: { items: User[]; next: string | null } = await (
      await fetch(url)
    ).json();
    yield* page.items;
    cursor = page.next;
  } while (cursor);
}

for await (const user of fetchAllUsers()) {
  console.log(user.name);
}
```

The caller doesn't know about pages or cursors. It just loops.

## 163: What is the difference between Template Method and Strategy?

Both let you change parts of an algorithm.

- **Template Method** uses inheritance. The base class fixes the steps, and subclasses override some of them. It is decided at compile time and you get one combination per subclass.
- **Strategy** uses composition. The context receives an object or function and calls it. You can switch it at runtime and combine strategies freely.

Modern code usually prefers Strategy (often just passing a function), following "composition over inheritance". Template Method still shows up in frameworks with base classes and lifecycle hooks.

## 164: How does a dependency injection container work?

A DI container keeps a registry of how to create each dependency (a "provider"). When you ask for a class, the container looks at what it needs (from constructor parameter types, decorators or tokens), creates those first, and passes them in. It also manages lifetimes:

- **Singleton:** one instance for the whole app.
- **Scoped:** one instance per request.
- **Transient:** a new instance every time.

```ts
// NestJS
@Injectable()
export class OrdersService {
  constructor(
    private readonly repo: OrdersRepository,
    private readonly payments: PaymentsService,
  ) {}
}
```

Nest reads the constructor types using metadata from TypeScript decorators and builds the dependency graph at startup.

## 165: How does dependency injection make testing easier?

Because a class receives its dependencies, a test can pass fakes, stubs or mocks instead of real databases or HTTP clients. Tests become fast, deterministic and don't need network access.

```ts
class SignupService {
  constructor(
    private users: UserRepository,
    private mailer: Mailer,
  ) {}

  async signup(email: string) {
    await this.users.save({ id: crypto.randomUUID(), email });
    await this.mailer.send(email, "Welcome!");
  }
}

// test
const sent: string[] = [];
const service = new SignupService(new InMemoryUserRepository(), {
  send: async (to) => {
    sent.push(to);
  },
});

await service.signup("ann@example.com");
expect(sent).toEqual(["ann@example.com"]);
```

## 166: When does a repository add value and when is it just extra code?

It adds value when:

- You have real business logic that should not know about SQL or the ORM.
- You want to test the logic with an in-memory version.
- You need one place to put complex queries for an aggregate.

It is extra code when it only wraps an ORM method by method (`findById` calls `prisma.user.findUnique`) in a simple CRUD app. ORMs like Prisma or Entity Framework already act like a repository. Adding a generic `Repository<T>` on top usually hides useful ORM features and doesn't make swapping databases realistic. Add the layer when it solves a problem you actually have.

## 167: What is the Specification pattern?

Specification puts a business rule into its own object that answers "does this item match?". Specifications can be combined with `and`, `or` and `not`, and can be reused for checks and for queries.

```ts
interface Spec<T> {
  isSatisfiedBy(item: T): boolean;
}

const and = <T>(a: Spec<T>, b: Spec<T>): Spec<T> => ({
  isSatisfiedBy: (x) => a.isSatisfiedBy(x) && b.isSatisfiedBy(x),
});

const isActive: Spec<Customer> = { isSatisfiedBy: (c) => c.active };
const isPremium: Spec<Customer> = {
  isSatisfiedBy: (c) => c.plan === "premium",
};

const canGetDiscount = and(isActive, isPremium);
customers.filter((c) => canGetDiscount.isSatisfiedBy(c));
```

In more advanced versions, a specification can also turn itself into a SQL `WHERE` clause or ORM filter.

## 168: What is CQRS?

CQRS (Command Query Responsibility Segregation) separates the code that changes data (commands) from the code that reads data (queries). They can use different models and even different databases. The write side keeps a normalized model with all the business rules; the read side keeps views shaped exactly for the screens, often denormalized.

It helps when reads and writes have very different needs or scale, and it fits well with event sourcing. The cost: more code, two models to keep in sync, and read data that may be a little behind. For simple CRUD apps it is usually not worth it.

## 169: What is event sourcing?

With event sourcing, you don't store the current state of an entity. You store every change as an event (`AccountOpened`, `MoneyDeposited`, `MoneyWithdrawn`) in an append-only log. The current state is rebuilt by replaying the events.

```ts
type Event =
  { type: "Deposited"; amount: number } | { type: "Withdrawn"; amount: number };

function balance(events: Event[]) {
  return events.reduce(
    (sum, e) => (e.type === "Deposited" ? sum + e.amount : sum - e.amount),
    0,
  );
}
```

Pros: a full audit history, the ability to rebuild state at any point in time, and easy creation of new read models. Cons: more complexity, events can never really change once stored, and you need snapshots and projections for performance.

## 170: What is hexagonal architecture?

Hexagonal architecture (also called ports and adapters), by Alistair Cockburn, puts the business logic in the center and keeps it free of frameworks and infrastructure.

- **Ports** are interfaces defined by the core, like `OrderRepository` or `PaymentGateway`.
- **Adapters** implement those ports for real tech: a Postgres repository, a Stripe client, an HTTP controller, a CLI command.

The core never imports Express, an ORM or an SDK. You can test it with fake adapters and swap tech without touching business rules.

## 171: What is Clean Architecture?

Clean Architecture, by Robert C. Martin, organizes code in circles:

1. **Entities:** core business rules.
2. **Use cases:** application-specific actions like "place order".
3. **Interface adapters:** controllers, presenters, gateways.
4. **Frameworks and drivers:** web framework, database, UI.

The key rule is the **dependency rule**: code dependencies only point inward. Inner circles don't know anything about outer ones. Database and framework details are plugged in from the outside through interfaces.

## 172: What is the difference between Clean, Onion and Hexagonal architecture?

They share the same core idea: business logic in the middle, infrastructure on the outside, and dependencies pointing inward. The differences are mostly in naming and how many layers they describe:

- **Hexagonal** talks about ports and adapters, with an "inside" and an "outside".
- **Onion** (Jeffrey Palermo) describes rings: domain model, domain services, application services, and infrastructure.
- **Clean** (Robert C. Martin) adds entities, use cases, interface adapters, and frameworks.

In an interview it is fine to say they are variations of the same principle.

## 173: What is a bounded context in Domain-Driven Design?

A bounded context is a clear boundary inside which a model and its words have one specific meaning. "Customer" means something different to Sales (a lead with deals), to Billing (someone with invoices and a payment method) and to Support (someone with tickets). Instead of one huge shared `Customer` model, each context has its own. Bounded contexts are often a good guide for where to split modules or microservices.

## 174: What is the difference between an entity and a value object?

- An **entity** has an identity that stays the same even when its attributes change. A `User` with id 42 is still the same user after changing the email.
- A **value object** has no identity. It is defined only by its values and is usually immutable. Two `Money(10, "USD")` objects are equal. Examples: money, address, date range, email address.

```ts
class Money {
  constructor(
    readonly amount: number,
    readonly currency: string,
  ) {}

  add(other: Money) {
    if (other.currency !== this.currency) throw new Error("Currency mismatch");
    return new Money(this.amount + other.amount, this.currency);
  }

  equals(other: Money) {
    return this.amount === other.amount && this.currency === other.currency;
  }
}
```

## 175: What is an aggregate and an aggregate root?

An aggregate is a group of related objects that are treated as one unit for data changes, with one entity as the **aggregate root**. Outside code can only talk to the root, and the root makes sure the rules of the whole group are kept. Example: an `Order` (root) with its `OrderLines`. You don't add a line directly; you call `order.addLine()`, and the order checks the total, stock limits and status. One transaction should change one aggregate.

## 176: What is a domain event?

A domain event records that something important happened in the business, named in the past tense: `OrderPlaced`, `PaymentFailed`, `SubscriptionCancelled`. Other parts of the system react to it without the aggregate knowing about them. For example, after `OrderPlaced`, one handler reserves stock and another sends a confirmation email. Domain events keep aggregates focused and reduce coupling between features.

## 177: What is ubiquitous language?

Ubiquitous language is a shared vocabulary that developers and business experts use for a bounded context, in conversations, documents and the code itself. If the business says "policy holder", the class should be `PolicyHolder`, not `UserAccount2`. It reduces misunderstandings and makes the code match how the business works.

## 178: What is an anti-corruption layer?

An anti-corruption layer (ACL) is a translation layer between your system and another system with a different or messy model, like a legacy ERP or a third-party API. It converts their data and concepts into your own model, so their design doesn't leak into your code. If the external system changes, only the ACL needs updating. It is basically an adapter or facade at the boundary of a bounded context.

## 179: What is an anemic domain model?

An anemic domain model has entity classes that hold only data (getters and setters), while all the business logic lives in service classes. Martin Fowler called it an anti-pattern for complex domains, because the rules get scattered and objects can be put into invalid states.

```ts
// Anemic
order.status = "shipped"; // no checks

// Rich
class Order {
  private status: "paid" | "shipped" | "pending" = "pending";

  ship() {
    if (this.status !== "paid") throw new Error("Only paid orders can ship");
    this.status = "shipped";
  }
}
```

For simple CRUD apps, an anemic model is fine and often simpler.

## 180: What is an application service, and how is it different from a domain service?

- An **application service** runs a use case. It loads aggregates from repositories, calls domain methods, saves them, and handles transactions, permissions and events. It has little business logic itself.
- A **domain service** holds business logic that doesn't naturally fit into one entity, like calculating a transfer between two accounts or pricing with many rules.

```ts
class PlaceOrderHandler {
  constructor(
    private orders: OrderRepository,
    private pricing: PricingService, // domain service
  ) {}

  async handle(cmd: { customerId: string; items: Item[] }) {
    const total = this.pricing.calculate(cmd.items);
    const order = Order.create(cmd.customerId, cmd.items, total);
    await this.orders.save(order);
  }
}
```

## 181: How do you decide how to split a system into microservices?

Common approaches:

- **By business capability:** orders, payments, catalog, shipping. Each matches something the business does.
- **By bounded context (DDD):** where models and language naturally separate.
- **By team ownership:** one team should own a service end to end.

Signs of a good split: a service can be changed and deployed alone, it owns its data, and most requests don't need many sync calls to other services. Bad splits follow technical layers (a "database service", a "validation service") and create chatty services that must always change together. If you're unsure, start with a modular monolith and extract later.

## 182: What is the database-per-service pattern?

Each microservice owns its data and is the only one allowed to access it directly. Others get the data through its API or events. This keeps services independent: one team can change its schema or even its database type without breaking others. The cost is that you can no longer join across services or use one transaction across them. You need patterns like API composition, CQRS views, sagas and events instead.

## 183: Why is a shared database between microservices a problem?

When several services read and write the same tables:

- A schema change in one service can break the others, so they must be deployed together.
- Nobody really owns the data or its rules.
- One service's heavy queries slow down everyone else.
- You lose most of the independence that microservices are supposed to give.

It is sometimes acceptable as a temporary step while moving away from a monolith, but it should have a plan to end.

## 184: What is a distributed monolith?

A distributed monolith is a system split into services that are still tightly coupled. They share a database, call each other synchronously in long chains, and must be deployed together. You get all the costs of microservices (network failures, complex ops, hard debugging) and none of the benefits. Common causes are splitting by technical layer, sharing code libraries with business logic, and not giving each service its own data.

## 185: What is the difference between an API gateway and a Backend for Frontend?

An **API gateway** is one entry point for all clients, handling routing, auth and rate limiting.

A **Backend for Frontend (BFF)** is a separate back end built for one specific client: one for the web app, one for the mobile app. Each BFF combines calls to internal services and shapes the response for its client, so the mobile app gets small payloads and the web app gets what its pages need. The front-end team often owns its BFF. They are often used together: gateway in front, BFFs behind it.

## 186: What is a service mesh?

A service mesh handles service-to-service communication at the infrastructure level, so each service doesn't need its own code for it. Traditionally each service instance gets a sidecar proxy (like Envoy) that intercepts all its network traffic. Newer designs like Istio's ambient mode reduce or remove per-pod sidecars. The mesh gives you mutual TLS, retries, timeouts, circuit breaking, traffic splitting for canaries, and metrics and tracing. Istio and Linkerd are the best known. It adds a lot of operational complexity, so it makes sense mostly with many services.

## 187: What is the sidecar pattern?

The sidecar pattern runs a helper process next to the main application, in the same pod or host, sharing its lifecycle and network. The sidecar handles a cross-cutting task like proxying traffic, collecting logs, refreshing certificates or syncing config, so the app doesn't have to. Because it is a separate process, it works for apps in any language. Service mesh proxies and log shippers like Fluent Bit are common sidecars.

## 188: What is the Strangler Fig pattern?

Strangler Fig is a way to replace a legacy system bit by bit instead of a big rewrite. You put a routing layer (proxy or gateway) in front of the old system. Then you build new features or rewrite old ones in the new system and route those paths to it. Over time the new system takes over more paths until the old one can be turned off. The name comes from a fig tree that grows around a host tree until it replaces it. It lowers risk because each step is small and can be rolled back.

## 189: What is the Saga pattern?

A saga manages a business process that spans several services without a distributed transaction. It is a sequence of local transactions, one per service. If a step fails, the saga runs **compensating transactions** to undo the earlier steps.

Example of an order saga:

1. Order service creates the order (pending).
2. Payment service charges the card.
3. Inventory service reserves stock. It fails: out of stock.
4. Compensation: payment service refunds; order service marks the order cancelled.

Sagas give eventual consistency, not isolation, so other requests may see the in-between state.

## 190: What is the difference between choreography and orchestration in sagas?

- **Choreography:** there is no central controller. Each service listens for events and publishes its own. `OrderCreated` triggers payment, `PaymentCompleted` triggers inventory, and so on. Very decoupled, but the overall flow is hard to see and debug as it grows.
- **Orchestration:** a central orchestrator tells each service what to do and handles failures and compensations. The flow is in one place and easy to follow. The orchestrator can become a large component itself.

Orchestration is often chosen for complex flows, sometimes with a workflow engine like Temporal or AWS Step Functions.

## 191: What is the Transactional Outbox pattern?

It solves the "dual write" problem: you need to save data in the database and publish an event, but if you do them separately, one can succeed while the other fails.

With the outbox, in the same database transaction you save the business data and insert the event into an `outbox` table. A separate process reads the outbox table and publishes the events to the broker, then marks them as sent.

```sql
BEGIN;
INSERT INTO orders (id, total) VALUES ('o1', 100);
INSERT INTO outbox (id, type, payload) VALUES ('e1', 'OrderPlaced', '{"orderId":"o1"}');
COMMIT;
```

Since the publisher can crash after sending but before marking, events may be sent more than once, so consumers must be idempotent.

## 192: What is two-phase commit and why is it rarely used in microservices?

Two-phase commit (2PC) is a protocol for an atomic transaction across several databases. A coordinator first asks all participants to "prepare" (lock and promise they can commit). If all say yes, it tells them to commit; otherwise to roll back.

It is rarely used between microservices because:

- Participants hold locks while waiting, which hurts performance.
- If the coordinator fails at the wrong moment, participants can be stuck waiting.
- Many modern databases and brokers don't support it well.
- It couples services tightly in time.

Sagas with eventual consistency are the usual alternative.

## 193: What are at-most-once, at-least-once and exactly-once delivery?

- **At-most-once:** a message is delivered zero or one time. If something fails, it is lost. Fast but can lose data.
- **At-least-once:** a message is retried until acknowledged, so it is never lost but may be delivered more than once. This is the most common guarantee.
- **Exactly-once:** each message has its effect exactly once. True exactly-once delivery over a network isn't possible in general; systems get "exactly-once processing" by combining at-least-once delivery with deduplication or transactions.

In practice, design for at-least-once and make consumers idempotent.

## 194: How do you make a message consumer idempotent?

Common techniques:

- **Store processed message IDs** in a table with a unique constraint, in the same transaction as the business change. If the ID already exists, skip the message.
- **Use natural idempotency:** "set status to PAID" is safe to repeat; "add 10 to the balance" is not.
- **Use upserts** and unique keys so a repeated insert doesn't create a duplicate.
- **Check versions** so old messages can't overwrite newer state.

```ts
await db.$transaction(async (tx) => {
  const inserted = await tx.$executeRaw`
    INSERT INTO processed_messages (id) VALUES (${msg.id})
    ON CONFLICT DO NOTHING`;
  if (inserted === 0) return; // already handled

  await tx.order.update({
    where: { id: msg.orderId },
    data: { status: "PAID" },
  });
});
```

## 195: What is a dead letter queue?

A dead letter queue (DLQ) is a separate queue where messages go when they can't be processed after a set number of attempts, or are invalid or expired. This keeps a bad message from blocking the queue or being retried forever. The team monitors the DLQ, investigates the messages, fixes the bug and then replays or discards them. RabbitMQ, SQS, Azure Service Bus and most job libraries support DLQs.

## 196: How do you keep message ordering in a queue system?

Most systems only guarantee order within a certain scope:

- **Kafka** keeps order inside a partition. Use a message key (like `orderId`) so all events for one entity go to the same partition.
- **SQS FIFO** queues keep order per message group ID.
- **RabbitMQ** keeps order in a single queue with one consumer, but retries and multiple consumers can break it.

Global ordering across everything doesn't scale. Usually you only need order per entity. Consumers can also check a version number or timestamp and ignore events older than what they already have.

## 197: What is back-pressure?

Back-pressure is a way for a slow consumer to tell a fast producer to slow down, instead of letting data pile up until memory runs out. Node.js streams do this: `write()` returns `false` when the buffer is full, and you wait for the `drain` event. `pipeline()` handles it for you. In systems, a bounded queue, rate limits, or returning `429` or `503` are all forms of back-pressure.

```ts
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("big.log"),
  createGzip(),
  createWriteStream("big.log.gz"),
);
```

## 198: How do partitions and consumer groups work in Kafka?

A Kafka topic is split into partitions. Each partition is an ordered log, and partitions are spread across brokers. Producers choose a partition, usually by hashing the message key.

A consumer group is a set of consumers sharing the work for a topic. Each partition is read by only one consumer in the group, so the number of partitions limits how many consumers can work in parallel. Different groups each get all messages, which is how several services can read the same topic. Consumers commit offsets to remember where they stopped.

## 199: What is the competing consumers pattern?

Several consumer instances read from the same queue, and each message is processed by just one of them. To handle more load you add more consumers. It gives parallel processing and also fault tolerance: if one worker dies, unacknowledged messages go back to the queue for another worker. Ordering between messages is not guaranteed, and messages may be processed more than once, so handlers should be idempotent.

## 200: What is the fan-out pattern?

Fan-out sends one message to many receivers. In messaging, one event is delivered to several queues or subscribers (an SNS topic to several SQS queues, or a RabbitMQ fanout exchange). In request handling, fan-out means one request triggers many parallel calls (to shards or services) and then combines the results ("fan-in"). Fan-out is powerful, but the overall latency is limited by the slowest response.

## 201: What is consistent hashing?

With normal hashing (`hash(key) % N`), changing the number of servers N moves almost every key to a new server, which would empty a cache cluster. With consistent hashing, servers and keys are placed on a hash ring, and each key belongs to the next server clockwise. When a server is added or removed, only the keys in its part of the ring move, about `1/N` of them. It is used in distributed caches, Cassandra, DynamoDB and load balancers. Virtual nodes (each server appearing many times on the ring) make the load more even.

## 202: What are write-through, write-back and write-around caching?

- **Write-through:** write to the cache and the database at the same time. The cache is always fresh, but writes are slower.
- **Write-back (write-behind):** write to the cache only, and save to the database later in batches. Very fast writes, but you can lose data if the cache crashes.
- **Write-around:** write only to the database, and let the cache fill on the next read (cache-aside). Avoids filling the cache with data nobody reads, but the first read after a write is a miss.

## 203: What are common cache eviction policies?

When the cache is full, it must remove something:

- **LRU (Least Recently Used):** remove the item not used for the longest time. The most common default.
- **LFU (Least Frequently Used):** remove the item used least often.
- **FIFO:** remove the oldest item.
- **TTL-based:** remove expired items.
- **Random:** cheap and sometimes good enough.

Redis supports several, set with `maxmemory-policy`, like `allkeys-lru` or `volatile-ttl`.

## 204: What is a cache stampede and how do you prevent it?

A cache stampede (thundering herd) happens when a popular key expires and many requests miss the cache at the same moment, all hitting the database together. It can take the database down.

Ways to prevent it:

- **Lock or single flight:** only one request rebuilds the value; others wait or get the old value.
- **Random TTL jitter:** so many keys don't expire at once.
- **Early refresh:** refresh the value in the background before it expires.
- **Stale-while-revalidate:** serve the old value while refreshing.

```ts
const inFlight = new Map<string, Promise<unknown>>();

function singleFlight<T>(key: string, load: () => Promise<T>): Promise<T> {
  if (!inFlight.has(key)) {
    inFlight.set(
      key,
      load().finally(() => inFlight.delete(key)),
    );
  }
  return inFlight.get(key) as Promise<T>;
}
```

This only works within one process. Across many servers you need a distributed lock or a shared "refreshing" flag in Redis.

## 205: When would you use a local in-memory cache instead of Redis?

A **local cache** (a `Map` or an LRU library in the process) is the fastest option, with no network call. It is good for small, rarely changing data like config or feature flags. But each instance has its own copy, they can disagree, and the cache is lost on restart.

A **distributed cache** like Redis is shared by all instances, survives app restarts and can hold much more data, at the cost of a network hop.

Many systems use both: a short-lived local cache in front of Redis.

## 206: How does HTTP caching fit into the architecture?

HTTP caching lets browsers, CDNs and proxies reuse responses without asking your server.

- `Cache-Control: public, max-age=31536000, immutable` for hashed static files like `app.3f9a.js`.
- `Cache-Control: no-cache` plus an `ETag`: the client must check with the server, which can answer `304 Not Modified` without a body.
- `Cache-Control: private` for user-specific data so CDNs don't store it.
- `s-maxage` sets the time for shared caches like CDNs separately from browsers.
- `stale-while-revalidate` lets caches serve a slightly old copy while fetching a new one.

Good headers can take most of the load off your servers for free.

## 207: What problems does replication lag cause and how do you handle them?

With async read replicas, a user can write something and then read from a replica that hasn't received it yet, so their change seems to disappear.

Ways to handle it:

- **Read-your-writes:** after a user writes, send that user's reads to the primary for a short time.
- **Read from primary** for critical data, and from replicas for the rest.
- **Track replication position:** remember the write's log position and only read from a replica that has caught up.
- **Update the UI optimistically** so the user sees their change anyway.

## 208: What is the difference between synchronous and asynchronous replication?

- **Synchronous:** the primary waits for the replica to confirm the write before telling the client it succeeded. No data loss if the primary dies, but writes are slower and stall if a replica is slow or down.
- **Asynchronous:** the primary confirms right away and sends changes to replicas later. Fast, but recent writes can be lost if the primary fails, and replicas lag.

Many setups use **semi-synchronous**: wait for at least one replica, the rest async.

## 209: How do you choose a good shard key?

A good shard key:

- Spreads data and traffic evenly (high cardinality, no hot values).
- Matches the most common queries, so most queries hit one shard.
- Doesn't change over time for a record.

Examples: `userId` or `tenantId` is often good for user-centric apps. A timestamp is usually bad because all new writes go to the newest shard. A country code is bad if most users are in one country. Sometimes you hash the key to spread it, at the cost of losing range queries.

## 210: Why is resharding hard?

Resharding means changing how data is split, usually to add more shards. You have to move large amounts of data while the system keeps serving traffic, keep reads and writes correct during the move, and update routing everywhere. If you used `hash % N`, almost all data moves. Ways to make it easier: use consistent hashing, start with many logical shards mapped onto fewer physical servers so you only move whole logical shards, or use a database that handles it for you, like Vitess, Citus, CockroachDB or DynamoDB.

## 211: When does denormalization make sense, and what are the risks?

It makes sense when reads are much more common than writes and joins are slowing them down: a product listing that always shows the category name, a post that shows the author name, or a pre-computed `commentCount`. The risks are data getting out of sync (the author changes their name, old posts keep the old one), more complex writes, and more storage. Keep the normalized data as the source of truth and update copies through events, triggers or background jobs.

## 212: What are the trade-offs of adding database indexes?

Pros: much faster reads, filters, sorts and joins on the indexed columns.

Cons:

- Every insert, update and delete must also update each index, so writes get slower.
- Indexes use disk and memory.
- Too many indexes confuse the planner and waste resources.
- Indexes on low-cardinality columns (like a boolean) often don't help.

Index based on real query patterns, check them with `EXPLAIN`, use composite indexes in the right column order, and remove unused ones.

## 213: What is the N+1 query problem?

It happens when code runs one query to get a list, then one more query for each item in the list. For 100 posts, that is 1 query for posts and 100 for authors.

```ts
// N+1
const posts = await prisma.post.findMany();
for (const post of posts) {
  post.author = await prisma.user.findUnique({ where: { id: post.authorId } });
}

// Fixed: one query with a join or batch
const postsWithAuthors = await prisma.post.findMany({
  include: { author: true },
});
```

Fixes: eager loading (`include`, `JOIN`), batching with `WHERE id IN (...)`, or a DataLoader in GraphQL.

## 214: Why can serverless functions run into database connection problems?

Each function instance opens its own database connections. When traffic spikes, the platform starts hundreds of instances, each with its own pool, and the database hits its connection limit (Postgres handles only a few hundred well). Instances also may not close connections cleanly. Solutions:

- A connection pooler like PgBouncer, AWS RDS Proxy or Supavisor.
- Serverless-friendly databases or HTTP-based drivers (Neon, PlanetScale, Prisma Accelerate).
- Small pool size per function (often 1) and reusing the client across invocations.

## 215: What is the difference between optimistic and pessimistic locking?

- **Pessimistic locking:** lock the row when you read it (`SELECT ... FOR UPDATE`), so nobody else can change it until you finish. Safe, but others wait, and you can get deadlocks.
- **Optimistic locking:** don't lock. Store a `version` number. When updating, check that the version hasn't changed. If it has, someone else won and you retry or show a conflict.

```sql
UPDATE products
SET stock = stock - 1, version = version + 1
WHERE id = 42 AND version = 7;
-- 0 rows updated means a conflict
```

Optimistic locking fits when conflicts are rare; pessimistic when they are common and retries are expensive.

## 216: What are transaction isolation levels?

They control what a transaction can see of other running transactions:

- **Read Uncommitted:** can see uncommitted changes (dirty reads).
- **Read Committed:** sees only committed data, but the same query can return different results within one transaction. Default in PostgreSQL and SQL Server.
- **Repeatable Read:** the same rows read twice give the same values. Default in MySQL InnoDB.
- **Serializable:** behaves as if transactions ran one at a time. Safest and slowest; may abort transactions that you must retry.

Higher isolation means fewer anomalies but less concurrency.

## 217: What is the PACELC theorem?

PACELC extends CAP. It says: if there is a **P**artition, choose between **A**vailability and **C**onsistency; **E**lse (normal operation), choose between **L**atency and **C**onsistency. This is useful because partitions are rare, but the latency vs consistency trade-off happens on every request. For example, DynamoDB and Cassandra by default favor availability and low latency (PA/EL), while systems like Spanner favor consistency in both cases (PC/EC).

## 218: What rate limiting algorithms do you know?

- **Fixed window:** count requests per fixed minute. Simple, but allows bursts at window edges (100 at 12:00:59 and 100 at 12:01:00).
- **Sliding window log:** store each request's timestamp. Accurate but uses more memory.
- **Sliding window counter:** combine the current and previous window counts weighted by time. A good balance.
- **Token bucket:** tokens refill at a steady rate; each request takes one. Allows short bursts up to the bucket size.
- **Leaky bucket:** requests go into a queue that drains at a fixed rate. Smooths traffic into a steady flow.

Token bucket is the most common in APIs.

## 219: How would you implement a token bucket rate limiter?

```ts
class TokenBucket {
  private tokens: number;
  private lastRefill = Date.now();

  constructor(
    private capacity: number,
    private refillPerSecond: number,
  ) {
    this.tokens = capacity;
  }

  tryRemove(): boolean {
    const now = Date.now();
    const elapsed = (now - this.lastRefill) / 1000;
    this.tokens = Math.min(
      this.capacity,
      this.tokens + elapsed * this.refillPerSecond,
    );
    this.lastRefill = now;

    if (this.tokens >= 1) {
      this.tokens -= 1;
      return true;
    }
    return false;
  }
}

const buckets = new Map<string, TokenBucket>();

function allow(clientId: string) {
  if (!buckets.has(clientId)) buckets.set(clientId, new TokenBucket(10, 5));
  return buckets.get(clientId)!.tryRemove();
}
```

This works for one instance. With many instances, the state must live in a shared store like Redis.

## 220: How do you do rate limiting across many servers?

Keep the counters in a shared store, usually Redis, and make each check atomic so two servers can't both read "99" and allow request 101. A Lua script or a simple `INCR` with expiry works.

```ts
async function isAllowed(key: string, limit: number, windowSec: number) {
  const bucket = `rl:${key}:${Math.floor(Date.now() / 1000 / windowSec)}`;
  const count = await redis.incr(bucket);
  if (count === 1) await redis.expire(bucket, windowSec);
  return count <= limit;
}
```

This is a fixed window. For smoother limits, use a sliding window or token bucket in a Lua script. At very high scale, some systems keep local counters and sync with Redis now and then, accepting a little inaccuracy. API gateways and services like Cloudflare often handle this for you.

## 221: How does a circuit breaker work internally?

It has three states:

- **Closed:** calls pass through. Failures are counted. If failures pass a threshold (like 50% in the last 20 calls), switch to open.
- **Open:** calls fail right away without calling the service. After a cooldown, switch to half-open.
- **Half-open:** let a few test calls through. If they succeed, go to closed; if they fail, go back to open.

```ts
class CircuitBreaker {
  private failures = 0;
  private state: "closed" | "open" | "half-open" = "closed";
  private openedAt = 0;

  constructor(
    private threshold = 5,
    private cooldownMs = 10_000,
  ) {}

  async call<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === "open") {
      if (Date.now() - this.openedAt < this.cooldownMs)
        throw new Error("Circuit open");
      this.state = "half-open";
    }
    try {
      const result = await fn();
      this.failures = 0;
      this.state = "closed";
      return result;
    } catch (err) {
      this.failures++;
      if (this.state === "half-open" || this.failures >= this.threshold) {
        this.state = "open";
        this.openedAt = Date.now();
      }
      throw err;
    }
  }
}
```

## 222: What is the Bulkhead pattern?

Bulkhead isolates resources so a problem in one part can't use up everything. The name comes from ship compartments: if one floods, the ship still floats. In software, you give each dependency or type of work its own connection pool, thread pool or concurrency limit. If the slow recommendations service uses up its 20 connections, checkout still has its own 50. It can also mean separate instances or clusters for different customers or features.

## 223: What is a retry storm and how does jitter help?

A retry storm happens when a service slows down, all its clients retry, and the extra retries add even more load, so it never recovers. It gets worse with layers: if three layers each retry three times, one user request can become 27 calls at the bottom.

To avoid it:

- Use exponential backoff with **jitter** (random delay), so retries spread out instead of arriving in waves.
- Limit retries to one layer, usually the outermost or innermost, not all of them.
- Use retry budgets (only allow retries up to, say, 10% of normal traffic).
- Combine with circuit breakers.

## 224: What is graceful degradation?

Graceful degradation means that when a part of the system fails, the rest keeps working with reduced features instead of failing completely. Examples:

- Recommendations service is down: show "popular items" instead.
- Search is down: show categories.
- Reviews can't load: show the product page without them.
- Under heavy load: turn off expensive non-core features with a flag.

You plan fallbacks for each non-critical dependency ahead of time.

## 225: What is the difference between liveness and readiness probes?

They come from Kubernetes but the idea is general:

- **Liveness:** "is the process alive or stuck?" If it fails, the container is restarted. Keep it simple; don't check the database here, or a database outage will restart all your pods for nothing.
- **Readiness:** "can this instance accept traffic right now?" If it fails, the instance is taken out of the load balancer but not restarted. Use it during startup (warming caches, connecting to the database) and shutdown.

There is also a **startup probe** for slow-starting apps, which holds off the other probes until the app has started.

## 226: How do you shut down a service gracefully?

When the platform stops an instance (a deploy or scale-down), it sends `SIGTERM`. A graceful shutdown:

1. Marks the instance as not ready, so the load balancer stops sending new requests.
2. Stops accepting new connections.
3. Waits for in-flight requests and jobs to finish, with a time limit.
4. Closes database pools, queue consumers and other connections.
5. Exits.

```ts
const server = app.listen(3000);

process.on("SIGTERM", () => {
  server.close(async () => {
    await pool.end();
    process.exit(0);
  });
  setTimeout(() => process.exit(1), 25_000).unref(); // hard limit
});
```

Without this, every deploy cuts off some requests.

## 227: What is deadline propagation?

When a request passes through several services, each one should know how much time is left in total, not use its own fixed timeout. If the user's request has a 2-second budget and service A already used 1.5 seconds, service B should only get 0.5 seconds, and should give up early rather than doing work nobody will wait for. gRPC supports deadlines out of the box. With HTTP you can pass the deadline in a header and turn it into an `AbortSignal.timeout()` in each service.

## 228: What is distributed tracing?

Distributed tracing follows a single request as it moves across services. Each request gets a **trace ID**, and each operation in it (an HTTP call, a DB query) is a **span** with a start time, duration and parent span. The IDs are passed between services in headers, usually the W3C `traceparent` header. Tools like Jaeger, Grafana Tempo, Zipkin, Honeycomb or Datadog then show a timeline of where the time went. OpenTelemetry is the standard way to instrument code for this.

```ts
import { trace } from "@opentelemetry/api";

const tracer = trace.getTracer("orders");

await tracer.startActiveSpan("chargeCard", async (span) => {
  try {
    await payments.charge(order);
  } finally {
    span.end();
  }
});
```

## 229: What is a correlation ID?

A correlation ID is a unique ID attached to a request at the edge (gateway or first service) and passed to every service, queue message and log line that belongs to it. When something fails, you search the logs for that ID and see the whole story across services. Tracing systems use the trace ID for the same purpose, and many teams simply log the trace ID as the correlation ID.

```ts
import { AsyncLocalStorage } from "node:async_hooks";

const context = new AsyncLocalStorage<{ requestId: string }>();

app.use((req, res, next) => {
  const requestId = req.header("x-request-id") ?? crypto.randomUUID();
  res.setHeader("x-request-id", requestId);
  context.run({ requestId }, next);
});
```

## 230: What is structured logging and why is it better?

Structured logging writes logs as key-value data (usually JSON) instead of plain sentences. Log tools can then filter and aggregate by fields like `userId`, `orderId` or `durationMs`.

```ts
import pino from "pino";

const logger = pino();
logger.info({ orderId: "o1", userId: "u7", durationMs: 132 }, "order placed");
// {"level":30,"time":...,"orderId":"o1","userId":"u7","durationMs":132,"msg":"order placed"}
```

Good practices: use log levels, include the request or trace ID, never log secrets or personal data you don't need, and write to stdout so the platform collects it.

## 231: What types of metrics are there, and what are the RED and USE methods?

Main metric types:

- **Counter:** only goes up (requests served, errors).
- **Gauge:** goes up and down (memory used, queue length).
- **Histogram:** distribution of values in buckets (request durations), used for percentiles.

Two common ways to choose what to measure:

- **RED** for services: **R**ate (requests per second), **E**rrors, **D**uration.
- **USE** for resources like CPU, disk and pools: **U**tilization, **S**aturation, **E**rrors.

## 232: What should you alert on?

Alert on symptoms that users feel, not on every internal cause. Good alerts are things like "error rate above 2% for 5 minutes" or "p99 latency above 1 second", ideally tied to SLOs and how fast the error budget is burning. Alerting on "CPU above 80%" often wakes people up for nothing. Every alert should be actionable, have a clear owner and link to a runbook. Lower-priority issues can go to a ticket or dashboard instead of paging someone.

## 233: How would you design a URL shortener?

Requirements: create a short code for a long URL, redirect fast, maybe count clicks. It is very read-heavy.

Design:

- **API:** `POST /links { url }` returns `{ code }`. `GET /:code` returns `301` or `302` to the long URL.
- **Code generation:** take a unique number (database sequence or a distributed ID generator) and encode it in base62. Seven base62 characters give about 3.5 trillion codes. Random codes with a uniqueness check also work.
- **Storage:** a key-value table `code -> url`. Any database works; DynamoDB or Postgres with an index on `code`.
- **Caching:** most traffic is for a small set of links, so cache them in Redis and at the CDN.
- **Analytics:** don't write to the database on every click. Send click events to a queue and aggregate them.

Use `302` if you need to count every click, since browsers cache `301` redirects.

## 234: How would you design pagination for an infinite scroll feed?

Use cursor pagination. The client sends the cursor from the last page, and the server returns the next items plus a new cursor.

```ts
// GET /feed?limit=20&cursor=eyJ0IjoiMjAyNi0xMC0yOCIsImlkIjoiOTkifQ
const { createdAt, id } = decodeCursor(req.query.cursor);

const items = await db.query(
  `SELECT * FROM posts
   WHERE (created_at, id) < ($1, $2)
   ORDER BY created_at DESC, id DESC
   LIMIT 21`,
  [createdAt, id],
);
// return 20 items; if a 21st exists, there's a next page
```

Points to mention: order by a unique combination (time plus id) so items don't get skipped, make the cursor opaque (base64 encoded), index the sort columns, and fetch one extra item to know if there is more.

## 235: How would you design a notification system?

It sends messages over channels like email, SMS, push and in-app.

- Services publish events like `OrderShipped` to a queue or topic.
- A **notification service** consumes them, checks user preferences and quiet hours, picks the template and channels, and creates notification jobs.
- Each **channel worker** (email, SMS, push) has its own queue and sends through providers like SES, Twilio or FCM. Separate queues mean a slow SMS provider doesn't delay emails.
- **Retries** with backoff, a **DLQ** for failures, and **deduplication** with an idempotency key so users don't get the same message twice.
- **Rate limits** per user so nobody gets spammed.
- In-app notifications are stored in a table and pushed live over WebSockets or SSE.

## 236: How would you design a file upload service?

Don't send big files through your API servers. Use direct uploads to object storage with presigned URLs:

1. The client asks your API for an upload URL.
2. The API checks permissions and file type/size, then creates a short-lived presigned URL for S3 (or similar).
3. The client uploads straight to S3.
4. S3 triggers an event (or the client calls back) and a worker processes the file: virus scan, thumbnails, metadata.
5. The database stores the key and status, and files are served through a CDN.

```ts
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({});

const url = await getSignedUrl(
  s3,
  new PutObjectCommand({
    Bucket: "uploads",
    Key: `users/${userId}/${fileId}`,
    ContentType: "image/png",
  }),
  { expiresIn: 300 },
);
```

For very large files, use multipart upload so failed parts can be retried.

## 237: How would you design a basic chat application?

- **Connections:** clients keep a WebSocket to a chat gateway service.
- **Sending:** the client sends a message, the server saves it to the database with a server-generated ID and timestamp, then delivers it.
- **Delivery across servers:** users in the same chat may be connected to different gateway instances, so gateways publish messages to a pub/sub system (Redis Pub/Sub, NATS, Kafka) and each gateway forwards them to its local connections.
- **Offline users:** store messages, and send a push notification. When the user reconnects, they fetch messages after their last seen ID.
- **Storage:** messages partitioned by conversation ID, ordered by time. Cassandra or ScyllaDB are common at large scale; Postgres works fine at smaller scale.
- **Extras:** read receipts, typing indicators (not stored, just relayed), presence.

## 238: How would you design a leaderboard?

Use a Redis sorted set. It keeps members sorted by score, and adding a score or getting a rank is O(log N).

```ts
// add points
await redis.zIncrBy("leaderboard:2026-10", 50, "user:42");

// top 10
const top = await redis.zRangeWithScores("leaderboard:2026-10", 0, 9, {
  REV: true,
});

// rank of a user (0-based)
const rank = await redis.zRevRank("leaderboard:2026-10", "user:42");
```

Keep the database as the source of truth and rebuild the sorted set if Redis loses it. Use one key per period (daily, monthly) and let old ones expire. With hundreds of millions of players, you may need to shard the set and estimate ranks for players far from the top.

## 239: How would you design search autocomplete?

The goal is suggestions in under about 100 ms as the user types.

- Build a list of popular queries or item names from logs, with counts.
- Store them so prefix lookups are fast: a trie with the top suggestions saved at each node, a search engine with prefix or "search-as-you-type" fields (Elasticsearch, OpenSearch, Typesense, Meilisearch), or Redis sorted sets.
- Rebuild the data periodically in a background job, not on each query.
- On the client: debounce input (about 150-300 ms), cancel old requests, and cache recent results.
- Cache popular prefixes at the CDN or in memory.
- Filter offensive or personal suggestions.

## 240: How would you design a background job system?

- **Producer:** the API adds a job (type, payload, idempotency key) to a queue.
- **Queue:** Redis with BullMQ, RabbitMQ, SQS, or a Postgres table with `SELECT ... FOR UPDATE SKIP LOCKED`.
- **Workers:** separate processes pull jobs, run them and acknowledge them. Scale workers based on queue length.
- **Retries** with backoff and a max attempt count, then send to a DLQ.
- **Timeouts and heartbeats** so stuck jobs are picked up again.
- **Priorities** with separate queues for urgent and bulk work.
- **Scheduling** for delayed and repeating jobs.
- **Monitoring:** queue size, job age, failure rate.
- **Idempotent jobs**, because a job can run twice.

```ts
import { Queue, Worker } from "bullmq";

const connection = { host: "localhost", port: 6379 };

const emails = new Queue("emails", { connection });
await emails.add(
  "welcome",
  { userId: "42" },
  { attempts: 5, backoff: { type: "exponential", delay: 1000 } },
);

new Worker("emails", async (job) => sendWelcome(job.data.userId), {
  connection,
});
```

## 241: How do you design an API for a long-running task?

Don't keep the HTTP request open for minutes. Use the asynchronous request-reply pattern:

1. `POST /reports` starts the job and returns `202 Accepted` with a job ID and a `Location: /reports/jobs/123` header.
2. The client polls `GET /reports/jobs/123`, which returns the status (`pending`, `running`, `done`, `failed`) and progress.
3. When done, the response includes a link to the result, for example a presigned download URL.

Instead of polling, you can notify the client with a webhook, WebSocket, SSE or email. Make the start request idempotent so a retry doesn't start the job twice.

## 242: How do idempotency keys work in a payment API?

The client generates a unique key (a UUID) for each logical operation and sends it in a header like `Idempotency-Key`. The server:

1. Checks if it has seen this key before.
2. If yes, returns the stored response without charging again.
3. If no, saves the key as "in progress", processes the payment, then stores the response with the key.

```ts
app.post("/payments", async (req, res) => {
  const key = req.header("Idempotency-Key");
  if (!key) return res.status(400).json({ error: "Idempotency-Key required" });

  const existing = await db.idempotency.findUnique({ where: { key } });
  if (existing?.response)
    return res.status(existing.status).json(existing.response);

  // create the key row first; a unique constraint blocks parallel duplicates
  await db.idempotency.create({ data: { key } });
  const result = await charge(req.body);
  await db.idempotency.update({
    where: { key },
    data: { status: 201, response: result },
  });
  res.status(201).json(result);
});
```

Keys are stored for a limited time, like 24 hours. Stripe's API works this way.

## 243: What are good practices for REST API design?

- Use nouns for resources and plural names: `/orders`, `/orders/42/items`.
- Use HTTP methods for actions: `GET` read, `POST` create, `PUT` replace, `PATCH` partial update, `DELETE` remove.
- Return the right status codes: `200`, `201` with a `Location`, `204`, `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`.
- Use a consistent error format, such as RFC 9457 Problem Details.
- Support filtering, sorting and pagination with query parameters.
- Use consistent naming (camelCase or snake_case, pick one).
- Don't expose database internals.
- Document the API with OpenAPI.

## 244: How do you change an API without breaking existing clients?

- **Make additive changes:** add new fields and endpoints instead of changing or removing old ones.
- **Make new fields optional** in requests.
- **Clients should be tolerant readers:** ignore fields they don't know.
- **Deprecate before removing:** mark fields as deprecated in docs and with the `Deprecation` and `Sunset` headers, track who still uses them, and remove them after a notice period.
- **Version only when you must** make a breaking change, and run old and new versions side by side.
- **Use contract tests** to catch accidental breaking changes.

Mobile apps make this especially important, because old app versions stay in use for a long time.

## 245: When would you use gRPC instead of REST between services?

gRPC is a good choice for internal service-to-service calls when you want:

- Strong contracts and generated clients from `.proto` files.
- Better performance: binary Protobuf messages and HTTP/2 multiplexing.
- Streaming in either or both directions.
- Built-in deadlines and cancellation.

REST is better for public APIs and browser clients, for easy debugging with curl, and when HTTP caching matters. Many systems use REST or GraphQL at the edge and gRPC inside.

## 246: What problems do you need to solve when you adopt GraphQL?

- **N+1 queries:** each resolver fetching its own data. Use DataLoader to batch and cache per request.
- **Expensive queries:** clients can ask for deeply nested data. Use depth limits, query cost analysis, and persisted queries.
- **Caching:** everything goes through one `POST /graphql` endpoint, so HTTP caching doesn't work out of the box. Use persisted queries over `GET`, or client caches like Apollo or urql.
- **Authorization:** must be checked at the field or resolver level, not only per endpoint.
- **Error handling:** responses can be `200` with partial data and errors.
- **Many services:** use federation or a gateway to combine schemas.

## 247: How do you scale WebSocket servers horizontally?

WebSockets are long-lived connections tied to one server, which makes scaling harder than with stateless HTTP.

- **Load balancer:** must support WebSocket upgrades and long idle timeouts.
- **Cross-server messaging:** when user A on server 1 messages user B on server 2, servers need a shared pub/sub backplane like Redis, NATS or Kafka. Socket.IO has a Redis adapter for this.
- **Connection registry:** store which server each user is connected to, if you route messages directly.
- **Reconnects:** clients must reconnect with backoff and catch up on missed messages using the last received ID.
- **Deploys:** draining servers drops all their connections, so clients must handle reconnects smoothly.
- **Limits:** each connection uses memory and a file descriptor, so watch per-server connection counts.

## 248: When would you use Server-Sent Events instead of WebSockets?

Use SSE when data only needs to flow from server to client: notifications, live scores, dashboards, progress updates or streaming AI responses. SSE runs over plain HTTP, works with existing proxies and auth, and the browser's `EventSource` reconnects automatically and can resume with `Last-Event-ID`. Use WebSockets when the client also sends frequent messages, like chat, multiplayer games or collaborative editing, or when you need binary data. Over HTTP/1.1 browsers limit open connections per domain, which can affect SSE; HTTP/2 removes most of that problem.

## 249: What are micro frontends?

Micro frontends apply the microservices idea to the front end. A large web app is split into parts owned by different teams (checkout, catalog, account), and each part can be developed and deployed on its own. They are combined at build time, on the server, or at runtime in the browser with tools like Module Federation, Native Federation or single-spa. Pros: team independence and smaller codebases. Cons: bigger bundles if dependencies aren't shared, inconsistent UX, harder shared state and routing, and more complex tooling. They make sense for large organizations with many front-end teams, not for small teams.

## 250: What are the trade-offs between CSR, SSR, SSG and ISR?

- **CSR (client-side rendering):** simple static hosting, very interactive, but slow first load and weaker SEO.
- **SSR (server-side rendering):** fresh, SEO-friendly HTML on every request, but needs servers and adds work per request.
- **SSG (static site generation):** pages are built once at build time and served from a CDN. Very fast and cheap, but content is only as fresh as the last build.
- **ISR (incremental static regeneration):** static pages that get rebuilt in the background after a set time or on demand. A mix of SSG speed and fresher content (Next.js popularized it).

Modern frameworks let you choose per route: marketing pages static, product pages ISR, dashboards CSR or SSR.

## 251: What is edge computing in web architecture?

Edge computing runs code on servers close to users, usually inside the CDN's network (Cloudflare Workers, Vercel Edge Functions, Fastly Compute, CloudFront Functions). It is good for things that need low latency and little data: redirects, auth checks, A/B testing, personalizing cached pages, geolocation and simple APIs. The limits are smaller runtimes (often no full Node.js API), CPU and memory limits, and distance from your main database, so a function at the edge that calls a database in one region can end up slower than running in that region.

## 252: What are the trade-offs of serverless architecture?

Pros:

- No servers to manage.
- Scales automatically, including down to zero.
- Pay per use, which is cheap for low or spiky traffic.

Cons:

- **Cold starts** add latency when a new instance starts.
- **Limits** on run time, memory and payload size.
- **Connection problems** with traditional databases.
- **Cost** can be higher than containers at steady high traffic.
- **Vendor lock-in** and harder local testing and debugging.
- Stateless only; long-running work needs other tools.

It fits event-driven work, APIs with variable traffic, scheduled jobs and glue code.

## 253: What is the difference between event notification and event-carried state transfer?

- **Event notification:** the event is small and just says something happened, like `{ type: "CustomerUpdated", id: "42" }`. Consumers call the source service if they need details. Small events, but more calls and coupling at read time.
- **Event-carried state transfer:** the event includes the data, like the full updated customer. Consumers can keep their own local copy and never call the source. Fewer calls and better availability, but bigger events and duplicated data.

Many systems mix both depending on the event.

## 254: How do you version events and message schemas?

Events stay around for a long time (in queues, Kafka topics, event stores), so old and new consumers will see different versions.

- Prefer **backward-compatible changes**: add optional fields, don't rename or remove them.
- Include a **version** or type name in the event.
- Use a **schema registry** (Confluent Schema Registry, AWS Glue) with Avro, Protobuf or JSON Schema to check compatibility before publishing.
- For breaking changes, publish a new event type (`OrderPlacedV2`) for a while alongside the old one.
- Consumers should ignore unknown fields.

## 255: What multi-tenancy models do you know?

Multi-tenancy means one system serves many customers (tenants).

- **Shared database, shared schema:** all tenants in the same tables with a `tenant_id` column. Cheapest and easiest to run, but you must never forget the tenant filter, and one big tenant can affect others.
- **Shared database, separate schemas:** one schema per tenant. Better isolation, but migrations run for every schema.
- **Database per tenant:** the strongest isolation and easy per-tenant backups, but expensive and harder to manage at thousands of tenants.

Many SaaS products use shared tables for small customers and dedicated databases for large enterprise ones.

## 256: What problems can feature flags cause and how do you manage them?

- **Flag debt:** old flags stay in the code forever, creating dead code and confusing branches. Set an owner and expiry date for each flag and remove it after rollout.
- **Testing combinations:** many flags create many possible states. Keep flags short-lived and independent.
- **Inconsistent behavior** across services if they read flags at different times.
- **Dependency on the flag service:** if it is down, use cached values and safe defaults.
- **Performance:** evaluate flags locally with a cached rule set instead of calling a server for every check.

Separate short-lived release flags from long-lived ones like kill switches and permission flags.

## 257: How do you manage configuration and secrets in a distributed system?

- Keep non-secret config in environment variables or a config service, per environment.
- Keep secrets (API keys, DB passwords) in a secret manager: AWS Secrets Manager, Google Secret Manager, Azure Key Vault or HashiCorp Vault. Never in Git or Docker images.
- Give each service only the secrets it needs (least privilege).
- Prefer short-lived credentials and workload identity (IAM roles for service accounts) over long-lived keys.
- Rotate secrets regularly and support rotation without downtime.
- Validate config at startup and fail fast if something is missing.

## 258: How do you run database migrations with zero downtime?

Use the **expand and contract** approach so old and new app versions both work during the deploy.

Example: renaming `name` to `full_name`:

1. **Expand:** add `full_name` (nullable). Deploy code that writes to both columns and reads from `name`.
2. **Backfill:** copy old data into `full_name` in small batches.
3. **Switch:** deploy code that reads from `full_name`.
4. **Contract:** stop writing `name`, then drop the column in a later release.

Also avoid long table locks: create indexes concurrently (`CREATE INDEX CONCURRENTLY` in Postgres), add columns without heavy defaults on old versions, and run big data changes in batches.

## 259: How does blue-green deployment work with a database?

Blue and green usually share one database, because copying and syncing data is hard. That means the database schema must work with both versions at the same time. So you split schema changes into backward-compatible steps (expand and contract): first add new things the new version needs, switch traffic, and only remove old things after blue is gone. If you change the schema in a breaking way, switching back to blue will fail, and the fast rollback that blue-green promises is lost.

## 260: How do you make a stateful application horizontally scalable?

Move the state out of the app process:

- **Sessions** into Redis or a database, or use signed tokens.
- **Uploaded files** into object storage, not the local disk.
- **In-memory caches** into a shared cache, or accept that each instance has its own.
- **Scheduled jobs** into a queue or a scheduler with a lock so they run once.
- **WebSocket state** into a pub/sub backplane plus a store for anything that must survive.

Once instances are interchangeable, you can add or remove them freely behind a load balancer.

## 261: What metrics would you use for autoscaling?

- **CPU** is the default and works for CPU-bound services.
- **Memory** is rarely a good scaling signal, because many runtimes don't release memory.
- **Request rate per instance** or **concurrent requests** work well for web services.
- **Queue length** or **message age** for workers (KEDA does this in Kubernetes).
- **Latency** can be used, but it reacts late.

Also set minimum instances to handle cold starts and base load, maximum instances to protect the database and your budget, and cooldown periods so the system doesn't flap up and down. For known spikes, scale ahead of time on a schedule.

## 262: What is the difference between a Layer 4 and a Layer 7 load balancer?

- **Layer 4 (transport):** routes by IP and port, without reading the content. Very fast, works for any TCP/UDP protocol. AWS Network Load Balancer is an example.
- **Layer 7 (application):** understands HTTP. Can route by path, host or header (`/api` to one service, `/images` to another), terminate TLS, add headers, do sticky sessions with cookies, and retry. Slower and more expensive per request. AWS Application Load Balancer, Nginx and Envoy are examples.

## 263: What is GeoDNS or global server load balancing?

Global server load balancing sends users to the best data center or region, usually the nearest healthy one. It can be done with:

- **GeoDNS / latency-based DNS:** the DNS server returns a different IP depending on where the user is (Route 53 latency routing, Cloudflare Load Balancing).
- **Anycast:** many locations announce the same IP, and the internet routes each user to the nearest one. CDNs and Cloudflare use this.

Health checks remove failed regions. DNS-based routing is limited by DNS caching, so failover isn't instant.

## 264: What is the difference between active-passive and active-active multi-region setups?

- **Active-passive:** one region serves all traffic; the other is a standby with replicated data. On failure, you promote the standby. Simpler, but the standby costs money while idle, failover takes time, and it is often poorly tested.
- **Active-active:** all regions serve traffic at the same time. Lower latency for users everywhere and no idle capacity, but writes in several regions mean you must handle replication conflicts, or route each user's writes to a "home" region.

Active-active is much harder to build correctly, so start with active-passive unless you really need it.

## 265: What are RPO and RTO?

- **RPO (Recovery Point Objective):** how much data you can afford to lose, measured in time. An RPO of 5 minutes means backups or replication must be no more than 5 minutes behind.
- **RTO (Recovery Time Objective):** how long the system can be down before it must be back. An RTO of 1 hour means you must recover within an hour.

Lower values need more expensive setups: continuous replication, hot standbys and automated failover. The business should decide these numbers per system.

## 266: What makes a good backup strategy?

- **Automated, regular backups** plus point-in-time recovery from transaction logs (most managed databases have this).
- **The 3-2-1 rule:** 3 copies, on 2 different media, 1 off-site (another region or account).
- **Protection from deletion:** immutable or locked backups, so ransomware or a mistake with admin access can't delete them.
- **Encryption** at rest and in transit.
- **Retention rules** that match legal needs.
- **Regular restore tests.** A backup you've never restored is not a backup you can count on.

## 267: When should you add a search engine like Elasticsearch, and how do you keep it in sync?

Add one when you need full-text search with relevance ranking, typo tolerance, filters and facets on large data, or log search. Simple `LIKE` queries or Postgres full-text search are enough for many apps.

The database stays the source of truth, and the search index is a copy. To keep it in sync:

- Publish events on changes and have a consumer update the index.
- Use change data capture (Debezium) to stream database changes.
- Run periodic full reindexes to fix drift.

Search results will be slightly behind the database, so the UI should allow for that.

## 268: How would you design image delivery for a website with user uploads?

- Store originals in object storage.
- Generate the sizes and formats you need (WebP, AVIF, thumbnails) either at upload time with a worker, or on demand with an image service (imgproxy, Cloudinary, Cloudflare Images, Next.js image optimization) and cache the results.
- Serve everything through a CDN with long cache times and versioned URLs.
- Use `srcset` and `sizes` in HTML so browsers pick the right size.
- Strip EXIF metadata (it can contain GPS location).
- Limit upload sizes and check file types to protect the processing workers.

## 269: How would you store time-series data?

Time-series data (metrics, sensor readings, prices) is append-heavy and is usually queried by time range.

- Use a time-series database or extension: TimescaleDB (Postgres), InfluxDB, Prometheus for metrics, ClickHouse for analytics.
- Partition by time so old data can be dropped or archived cheaply.
- Downsample old data: keep per-second data for a week, per-minute for a month, per-hour for a year.
- Batch writes.
- Be careful with high-cardinality labels (like user ID as a metric label), which can blow up storage and memory.

## 270: How do you choose a database for a new feature?

Start from the access patterns and requirements, not the hype:

- **Data shape and relations:** lots of relations and joins point to relational.
- **Consistency needs:** money and inventory need transactions.
- **Query patterns:** key lookups, range scans, full-text search, graph traversals or analytics.
- **Scale:** reads and writes per second, data size, growth.
- **Operational cost:** does the team already know it, is there a managed version.

A relational database like PostgreSQL is a strong default because it covers most needs (JSON, full-text search, extensions). Add a special-purpose store only when there is a clear reason.

## 271: What is polyglot persistence?

Polyglot persistence means using different databases for different needs in the same system: Postgres for orders, Redis for sessions and caching, Elasticsearch for search, S3 for files, ClickHouse for analytics. Each data type gets a store that fits it well. The cost is more systems to run, back up, secure and keep in sync, so add each one only when the benefit is clear.

## 272: What is a Bloom filter and where is it used?

A Bloom filter is a small, memory-efficient data structure that tells you if an item is **possibly in a set** or **definitely not in a set**. It can give false positives but never false negatives. It is used to avoid expensive lookups for things that don't exist:

- Databases like Cassandra and RocksDB check it before reading files from disk.
- Checking if a username is taken, or a URL was already crawled.
- Protecting a cache from lookups of keys that don't exist in the database.

You can't remove items from a basic Bloom filter, and the false positive rate grows as it fills.

## 273: What is the Pipes and Filters pattern?

Pipes and Filters splits processing into a chain of independent steps (filters), connected by pipes that pass the output of one step to the next. Each filter does one thing and doesn't know about the others. Unix shell pipes are the classic example: `cat log | grep ERROR | sort | uniq -c`. Node.js streams, ETL pipelines and image processing pipelines work the same way. Filters are easy to reuse, reorder and scale separately.

## 274: What are the common problems with a layered architecture?

- **Sinkhole anti-pattern:** requests pass through every layer without any real logic, just copying data from one object to the next.
- **Fat service layer:** all business logic piles up in services while entities are empty (anemic model).
- **Changes cut across layers:** one feature touches the controller, service, repository and DTO folders at once.
- **Hidden coupling to the database:** if the domain depends on the data layer, the database design ends up driving the business logic.

Fixes include dependency inversion (domain defines interfaces, data layer implements them) and organizing code by feature instead of by layer.

## 275: What is vertical slice architecture?

Vertical slice architecture organizes code by feature or use case instead of by technical layer. Each slice, like "PlaceOrder" or "GetOrderHistory", contains everything it needs: the endpoint, validation, logic and data access. Slices share as little as possible. Adding or changing a feature touches one folder, and each slice can choose how simple or complex it needs to be. The risk is duplication between slices, so shared domain logic still needs a home.

## 276: Should you organize code by feature or by layer?

By layer:

```
controllers/  services/  repositories/  models/
```

By feature:

```
orders/   (controller, service, repository, model)
payments/
users/
```

Organizing by layer is easy at the start but spreads every feature across many folders. Organizing by feature keeps related code together, makes module boundaries clearer and makes it easier to later extract a feature into its own service. For anything beyond a small app, feature-based folders usually age better, and you can still have layers inside each feature.

## 277: How do you enforce module boundaries in a large codebase?

Without enforcement, boundaries erode over time as people import whatever is convenient.

- Give each module a public entry point (an `index.ts`) and forbid deep imports into its internals.
- Use lint rules: Nx `enforce-module-boundaries`, `eslint-plugin-boundaries`, or `dependency-cruiser` to block forbidden imports.
- Use separate packages in a monorepo with explicit dependencies.
- In Java and .NET, use separate projects/modules with tools like ArchUnit or NetArchTest.
- Give each module its own database schema or tables, accessed only through its own code.
- Run these checks in CI so violations fail the build.

## 278: How do you keep a modular monolith from turning into a big ball of mud?

- Define modules around business areas, with clear owners.
- Modules talk only through public APIs or in-process events, never by reaching into each other's classes or tables.
- Each module owns its data (its own schema or tables).
- Enforce rules with lint and architecture tests in CI.
- Avoid a shared "common" module that slowly collects business logic.
- Review dependencies between modules regularly and watch for cycles.

If a module is cleanly separated, extracting it to a microservice later is mostly a matter of replacing in-process calls with network calls.

## 279: What kinds of coupling exist besides code dependencies?

- **Temporal coupling:** service A only works if B is up at the same time (sync calls). Queues reduce it.
- **Data/schema coupling:** services depend on the same data format or tables.
- **Deployment coupling:** services must be released together.
- **Location coupling:** a service hardcodes where another one lives.
- **Semantic coupling:** both sides must share the same understanding of a field or status, so a change in meaning breaks the other side even if the format stays the same.

Good architecture lowers the coupling that hurts most for your situation, since you can't remove all of it.

## 280: What is Conway's Law?

Conway's Law says that organizations build systems that mirror their communication structure. If four teams build a compiler, you get a four-pass compiler. In practice, service boundaries tend to follow team boundaries. The "Inverse Conway Maneuver" uses this on purpose: design the team structure to match the architecture you want. That is why microservices only work well when each team can own its services end to end.

## 281: What is an Architecture Decision Record?

An ADR is a short document that records one important architecture decision: the context, the decision, the alternatives considered and the consequences. ADRs are usually kept as numbered markdown files in the repository.

```md
# ADR 0007: Use PostgreSQL for order data

## Status

Accepted

## Context

We need transactions across orders, payments and stock...

## Decision

Use PostgreSQL 17 on a managed service.

## Consequences

We need to plan for read replicas when traffic grows...
```

They help new team members understand why things are the way they are, and stop the same debates from repeating.

## 282: What is the C4 model?

The C4 model, by Simon Brown, is a simple way to draw software architecture at four zoom levels:

1. **Context:** the system and the people and external systems it talks to.
2. **Containers:** the deployable parts (web app, API, database, queue).
3. **Components:** the main parts inside one container.
4. **Code:** classes, usually only when needed.

Different audiences need different levels: managers look at context, developers at containers and components. Tools like Structurizr, Mermaid or PlantUML can draw C4 diagrams from text.

## 283: How do you handle technical debt from an architecture point of view?

- Make it visible: keep a list, with the cost of each item in terms the business understands (slower features, outages, onboarding time).
- Prioritize debt that slows down the areas that change most often. Debt in code nobody touches can wait.
- Pay it down continuously, as part of normal feature work, rather than waiting for a "big rewrite".
- Use the Strangler Fig pattern for large replacements.
- Prevent new debt with reviews, ADRs, architecture tests and clear module boundaries.

Some debt is a deliberate, sensible trade-off to ship faster. The problem is debt nobody knows about or tracks.

## 284: What does it mean that quality attributes trade off against each other?

Quality attributes (performance, availability, consistency, security, cost, maintainability, simplicity) often pull in different directions. Caching improves performance but risks stale data. Encryption improves security but adds latency. Multi-region improves availability but raises cost and makes consistency harder. Microservices help team scale but make operations harder. There is no "best" architecture, only one that fits the priorities. In interviews, naming the trade-off you are making and why is often more important than the choice itself.

## 285: Why should you wrap third-party APIs behind your own interface?

Calling an SDK like Stripe, SendGrid or OpenAI directly from all over your code ties your business logic to that vendor. Wrapping it in your own small interface (a gateway or adapter):

- Gives one place to handle retries, timeouts, logging and error mapping.
- Lets you switch vendors or use several at once.
- Makes testing easy with a fake implementation.
- Keeps vendor-specific types out of your domain.

```ts
interface EmailSender {
  send(to: string, subject: string, html: string): Promise<void>;
}

class SesEmailSender implements EmailSender {
  async send(to: string, subject: string, html: string) {
    // call AWS SES here, map errors to your own error types
  }
}
```

## 286: Which HTTP methods are safe and which are idempotent, and why does it matter for architecture?

- **Safe** (don't change state): `GET`, `HEAD`, `OPTIONS`.
- **Idempotent** (same result if repeated): the safe ones plus `PUT` and `DELETE`.
- **Neither:** `POST`. `PATCH` is not guaranteed to be idempotent.

It matters because proxies, load balancers, browsers and client libraries may retry or prefetch requests automatically, and they rely on these meanings. If your `GET /logout` or `GET /delete?id=5` changes data, a crawler or prefetch can trigger it. If `PUT` isn't really idempotent, retries cause bugs. Use `POST` plus idempotency keys for non-idempotent actions that need safe retries.

## 287: What is request batching or the DataLoader pattern?

DataLoader collects all the individual "load by ID" calls made during one tick of the event loop and turns them into one batched request. It also caches results for the duration of a request. It is the standard fix for N+1 problems in GraphQL resolvers.

```ts
import DataLoader from "dataloader";

const userLoader = new DataLoader(async (ids: readonly string[]) => {
  const users = await db.user.findMany({ where: { id: { in: [...ids] } } });
  const byId = new Map(users.map((u) => [u.id, u]));
  return ids.map((id) => byId.get(id) ?? null); // same order as ids
});

// in resolvers: many calls, one query
const author = await userLoader.load(post.authorId);
```

Create a new loader per request so one user's cached data isn't shared with another.

## 288: What is an optimistic UI update?

With an optimistic update, the UI shows the result of an action right away, before the server confirms it, assuming it will succeed. If the server returns an error, you roll back the change and show a message. "Like" buttons, adding items to a list and chat messages often work this way. It makes the app feel instant even on slow networks. Use it for actions that almost always succeed and are easy to undo, not for payments. Libraries like TanStack Query and React's `useOptimistic` help with this.

## 289: What is an offline-first architecture?

In an offline-first app, the client works against a local database (IndexedDB, SQLite) as its main source of data, and syncs with the server in the background when online. The UI is fast and works without a network. The hard parts are syncing and conflicts: two devices editing the same record offline. Solutions include last-write-wins, version numbers with conflict prompts, or CRDTs. Tools like PouchDB with CouchDB, Replicache, PowerSync and ElectricSQL help. Service workers cache the app shell so the app itself loads offline.

## 290: What is unidirectional data flow?

In unidirectional data flow, data moves in one direction: state goes down to the view, the view sends actions or events, and those actions update the state, which flows down again. The Flux architecture and Redux made this popular. Because there is one path for changes, it is easy to understand where a change came from and to debug it with tools like Redux DevTools. Two-way binding everywhere, by contrast, can make it hard to trace who changed what.

## 291: What is the container and presentational components pattern?

It splits UI components into two kinds:

- **Presentational (dumb) components** just render props and emit events. They don't know where data comes from. Easy to reuse, test and show in Storybook.
- **Container (smart) components** fetch data, manage state and pass it down to presentational ones.

With hooks, Angular signals and server components, the split is less strict than it used to be, but the idea of keeping most components free of data-fetching logic is still useful.

## 292: How is reactive programming used as a design pattern?

Reactive programming treats data as streams of values over time that you can combine, filter and transform. Instead of asking for values, your code reacts when new ones arrive. RxJS is the best-known library in JavaScript, and Angular uses it heavily. It is a good fit for things like search-as-you-type, websockets, and combining several async sources.

```ts
import {
  fromEvent,
  debounceTime,
  map,
  distinctUntilChanged,
  switchMap,
} from "rxjs";

fromEvent<InputEvent>(searchInput, "input")
  .pipe(
    map((e) => (e.target as HTMLInputElement).value),
    debounceTime(300),
    distinctUntilChanged(),
    switchMap((q) => fetch(`/api/search?q=${q}`).then((r) => r.json())), // cancels old requests
  )
  .subscribe(showResults);
```

Signals (in Angular, Solid, Preact and others) are a simpler reactive model for synchronous UI state.

## 293: What is the producer-consumer pattern?

Producers create work items and put them in a shared buffer or queue; consumers take items out and process them. The buffer lets the two sides work at different speeds. It is used inside one process (a bounded channel between threads) and across systems (a message queue between services). Key decisions: how big the buffer is, what happens when it is full (block, drop or reject: back-pressure), and how many consumers run in parallel.

## 294: How do you handle CPU-heavy work in Node.js without blocking the server?

Node.js runs JavaScript on one main thread, so a heavy calculation blocks all other requests.

- **Worker threads** (`node:worker_threads`) run JS in parallel threads. Use a pool (like Piscina) instead of creating a worker per task.
- **A separate worker service** behind a queue for long jobs.
- **Child processes** for running other programs.
- Split work into chunks with `setImmediate` if it must stay on the main thread.

```ts
import Piscina from "piscina";

const pool = new Piscina({
  filename: new URL("./resize-worker.js", import.meta.url).href,
});

app.post("/resize", async (req, res) => {
  const result = await pool.run({ path: req.body.path, width: 300 });
  res.json(result);
});
```

## 295: What is lazy loading as an architectural pattern?

Lazy loading delays loading or creating something until it is actually needed. Examples:

- Front end: load route bundles and heavy components with dynamic `import()` only when the user opens them.
- Images with `loading="lazy"`.
- ORMs loading related data only when you access it.
- Initializing an expensive client on first use (a virtual proxy).

It speeds up startup and saves resources, but it can move the delay to a worse moment, and lazy ORM relations are a common cause of N+1 queries.

## 296: How do you schedule delayed messages, like "send a reminder in 24 hours"?

Options:

- **Queue with delay support:** BullMQ delayed jobs, SQS delay (up to 15 minutes), RabbitMQ delayed message plugin, Azure Service Bus scheduled messages.
- **Database table + poller:** store `run_at` and have a worker query `WHERE run_at <= now()` regularly, with `FOR UPDATE SKIP LOCKED` so several workers don't take the same row.
- **Scheduler services:** AWS EventBridge Scheduler, Google Cloud Tasks.
- **Workflow engines:** Temporal with durable timers.

The job should check current state when it runs. If the user already completed the action, skip the reminder.

## 297: How do you build reliable webhook delivery as a provider?

- Store each event in the database first, then deliver it from a queue (outbox pattern).
- Sign the payload with an HMAC secret per customer and include a timestamp, so receivers can verify it and reject replays.
- Retry failed deliveries with exponential backoff for hours or days; disable endpoints that keep failing and notify the owner.
- Include a unique event ID so receivers can deduplicate.
- Use short timeouts and expect a quick `2xx`.
- Provide a dashboard or API to see and replay deliveries.
- Protect against SSRF: don't allow URLs pointing at internal IP ranges.

## 298: How should an API communicate rate limits to clients?

- Return `429 Too Many Requests` when the limit is exceeded.
- Include `Retry-After` with the number of seconds to wait.
- Include headers with the current limit status. Many APIs use `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset`. The IETF has a draft for standard `RateLimit` and `RateLimit-Policy` headers.
- Document the limits per plan and per endpoint.

Clients should read these headers and back off instead of retrying blindly.

## 299: What is defense in depth and least privilege?

- **Defense in depth** means using several layers of security, so if one fails, others still protect the system: WAF at the edge, TLS, authentication at the gateway, authorization in each service, input validation, network rules between services, encrypted data, and monitoring.
- **Least privilege** means giving every user, service and process only the access it needs and nothing more. The orders service gets read/write on its own tables, not admin on the whole database. This limits the damage when something is compromised.

## 300: How do services authenticate each other in a microservice system?

Common approaches:

- **Mutual TLS (mTLS):** both sides present certificates, so each knows who the other is. Service meshes can do this automatically. SPIFFE/SPIRE gives services identities.
- **Service tokens:** a service gets a short-lived token (OAuth 2.0 client credentials, or a cloud identity token) and sends it with each call.
- **Passing user context:** the gateway checks the user's token and passes a signed token or claims downstream, so services can make authorization decisions.

Don't rely only on "it's inside our private network". Treat internal calls as untrusted too (zero trust).

# Advanced Questions (301-450)

## 301: How would you design a news feed like Twitter or Instagram?

The main choice is when to build each user's feed:

- **Fan-out on write (push):** when someone posts, write the post ID into the feed list of every follower (often a Redis list per user). Reading a feed is then very fast. Writing is expensive for users with many followers.
- **Fan-out on read (pull):** when a user opens the feed, fetch recent posts from everyone they follow and merge them. Writes are cheap, reads are slow.
- **Hybrid:** push for normal users, pull for celebrities, and merge both at read time. Most large systems do this.

Other parts: a post service with its own storage, a social graph store, a feed cache keeping only the latest few hundred IDs per user, a ranking step, cursor pagination, and media served from a CDN. Feeds are eventually consistent; a post showing up a few seconds late is fine.

## 302: What is the celebrity problem in feed systems and how do you solve it?

If a user with 50 million followers posts, fan-out on write means 50 million feed writes for one post. That causes a huge spike, delays for everyone else, and wasted work for followers who never log in.

Solutions:

- Don't fan out posts from accounts above a follower threshold. Followers pull those posts at read time and merge them into their precomputed feed.
- Only fan out to active users; build feeds for inactive users when they come back.
- Process fan-out jobs in a separate, lower-priority queue so normal posts aren't delayed.

## 303: How would you design a rate limiter for a large distributed API?

- **Where:** at the edge or API gateway, so rejected traffic doesn't reach your services. Add per-service limits too for protection.
- **Key:** API key, user ID, IP, or a mix, with different limits per plan and endpoint.
- **Algorithm:** token bucket or sliding window counter.
- **State:** Redis (or a Redis cluster sharded by key), with atomic Lua scripts. Keep the check to one round trip.
- **Scale:** for very high traffic, use local token buckets per instance that sync with Redis periodically, accepting slight overshoot. Or give each of N instances `limit / N` locally.
- **Failure:** decide whether to fail open (allow traffic if Redis is down) or fail closed. Fail open is common for general APIs; fail closed for things like login attempts.
- **Response:** `429` with `Retry-After`, and metrics on who is being limited.

## 304: How do you generate short codes for a URL shortener at very large scale?

Options:

- **Database auto-increment + base62:** simple but one DB becomes a bottleneck, and codes are guessable.
- **Ranges per server:** a coordinator (or a table) hands each app server a block of 1,000,000 IDs. Servers generate codes locally with no coordination until the block runs out. Fast and simple. Gaps after restarts are fine.
- **Snowflake-style IDs:** unique 64-bit IDs from time + machine ID + sequence, then base62.
- **Random codes:** generate 7 random base62 characters and insert with a unique constraint, retrying on conflict. Codes aren't guessable, but conflicts increase as the space fills.

If codes must not be guessable, use random codes or shuffle the counter with a reversible permutation.

## 305: How do you generate unique IDs in a distributed system?

- **UUIDv4:** random, no coordination, but not sortable and bad for B-tree index locality.
- **UUIDv7:** starts with a millisecond timestamp, so it is time-sortable and index-friendly. Standardized in RFC 9562 and a good default today.
- **ULID:** similar idea to UUIDv7 with a different text encoding.
- **Snowflake:** 64-bit ID made of a timestamp, worker ID and per-millisecond sequence. Compact and sortable, but workers need unique IDs and clocks must not go backwards.
- **Database sequences or ranges:** simple but need a central store.

Pick sortable IDs for primary keys in large tables, and avoid exposing sequential IDs publicly if they leak business data like order counts.

## 306: How would you design a web crawler?

- **URL frontier:** a queue of URLs to crawl, with priorities, split by host so you can be polite (a delay per domain and respecting `robots.txt`).
- **Fetchers:** many workers that download pages, with timeouts and DNS caching.
- **Deduplication:** a Bloom filter or a set of normalized URL hashes to avoid crawling the same URL twice, plus content hashes to detect duplicate pages under different URLs.
- **Parser:** extracts links and content, sends new URLs back to the frontier.
- **Storage:** raw pages in object storage, metadata in a database.
- **Recrawl schedule** based on how often pages change.
- **Traps:** limit depth and URL length to avoid infinite calendars or session-ID URLs.

Partition the frontier by host hash so each worker owns a set of domains.

## 307: How would you design the location part of a ride-hailing app?

- Drivers send their location every few seconds. That is a lot of writes, so keep current locations in memory (Redis) rather than a regular database table.
- To find nearby drivers fast, use a geospatial index: geohash, Uber's H3 hexagons, quadtrees, or Redis `GEOSEARCH`. Look up the rider's cell and neighboring cells.
- Shard by city or region; most queries are local.
- Matching service picks drivers by distance, ETA and rating, and offers the ride to one driver at a time with a timeout, using a lock or atomic state change so a driver isn't matched twice.
- Location history goes to a stream (Kafka) for analytics and billing, not to the hot path.
- Push updates to the rider app over WebSockets.

## 308: How would you design typeahead suggestions for a very large search engine?

- Collect query logs and aggregate counts in a batch or streaming job (for example, hourly).
- Build a trie (or a sorted prefix table) where each prefix node stores its top-K completions, so lookups don't have to walk the subtree at request time.
- Serve the structure from memory on many replicas; shard by prefix if it doesn't fit on one machine.
- Blend in personal history and trending queries at request time.
- Cache very popular prefixes at the CDN and in the browser.
- Filter unsafe or personal content before publishing a new version.
- Swap versions atomically when a new build is ready.

Latency is the main goal, so precomputing is more important than fancy ranking at query time.

## 309: How would you design a video streaming platform?

- **Upload:** direct upload to object storage with resumable or multipart uploads.
- **Processing:** a job pipeline transcodes each video into several resolutions and bitrates and cuts them into small segments (HLS or DASH), creates thumbnails and extracts metadata. Split work into chunks so many workers transcode in parallel.
- **Delivery:** segments are served by a CDN. The player uses adaptive bitrate streaming, switching quality based on the user's bandwidth.
- **Metadata:** a database for titles, owners, permissions and status.
- **Access control:** signed URLs or signed cookies for private or paid content, DRM if required.
- **Views and analytics:** events go to a stream and are aggregated, not counted with a DB update per view.

The CDN handles almost all traffic; the origin is mainly for processing and metadata.

## 310: How would you design a payment system?

- **Idempotency keys** on every operation so retries never double-charge.
- **A ledger with double-entry accounting:** every money movement is recorded as matching debit and credit entries that sum to zero. The ledger is append-only; you never update balances in place without a record.
- **State machine** for payments (`created`, `authorized`, `captured`, `refunded`, `failed`), with valid transitions enforced.
- **External PSP calls** (Stripe, Adyen) wrapped with timeouts and a clear handling of "unknown" results: if a call times out, you don't know if it succeeded, so you query the provider or rely on webhooks before retrying.
- **Reconciliation:** a daily job compares your ledger with provider reports and flags mismatches.
- **Outbox** for publishing payment events.
- Strong consistency (a relational database with transactions), audit logs, and PCI DSS scope kept small by using the provider's tokenization so card numbers never touch your servers.

## 311: How would you design a ticket booking system that doesn't sell the same seat twice?

- When a user selects a seat, create a **temporary hold** with an expiry (say 10 minutes). The hold must be atomic: a conditional update `UPDATE seats SET held_by = ?, held_until = ? WHERE id = ? AND (held_until IS NULL OR held_until < now()) AND sold = false`, or a unique constraint on `(event_id, seat_id)` in a reservations table.
- Payment happens during the hold. On success, mark the seat sold in the same transaction that confirms the booking.
- Expired holds are released automatically (by the expiry check or a cleanup job).
- For very popular events, put users in a **virtual waiting room** queue so only a controlled number reach checkout at a time.
- Cache the seat map for viewing, but always check availability in the database when holding.

The core rule: the final "is it free" check and the write must be one atomic operation.

## 312: How would you design a distributed job scheduler?

Requirements: run jobs at set times (cron or one-off), at least once, without running the same job on many nodes.

- Store jobs in a database with `next_run_at`, status and owner.
- Scheduler nodes poll for due jobs and claim them atomically (`UPDATE ... WHERE status = 'pending' AND next_run_at <= now() ... RETURNING`, or `FOR UPDATE SKIP LOCKED`). Claims have a lease that expires if the node dies.
- Claimed jobs go to a queue for workers, so scheduling and execution scale separately.
- Partition jobs by ID across scheduler nodes if one database poll can't keep up.
- Jobs must be idempotent, because lease expiry can cause re-runs.
- Track history, retries, timeouts and alerts on missed runs.
- Handle time zones and daylight saving changes for cron expressions.

## 313: How would you design a metrics and monitoring system?

- **Collection:** agents or SDKs (OpenTelemetry) send metrics, or a server scrapes them (Prometheus pull model).
- **Ingestion:** a write path that can take millions of data points per second, buffered through a queue like Kafka.
- **Storage:** a time-series database that compresses data well (Prometheus TSDB, Mimir, VictoriaMetrics, M3), sharded by series, with downsampling and retention rules.
- **Query layer** for dashboards and alerts, with caching for common queries.
- **Alerting** evaluates rules on a schedule and sends notifications with grouping and silencing.
- **Cardinality control:** limit labels per metric, since each unique label combination is a new series.

The monitoring system should not depend on the systems it monitors, and you need a way to know if it is down too.

## 314: How would you design a collaborative editor like Google Docs?

The main problem is merging edits from many users at the same time.

- **Operational Transformation (OT):** a central server orders operations and transforms each incoming one against operations it didn't know about. Used by Google Docs. Needs a central server per document.
- **CRDTs:** data structures that merge automatically in any order and still converge. Work peer-to-peer and offline. Libraries: Yjs, Automerge.

Architecture: clients connect over WebSockets to a server that owns each document (route by document ID), the server broadcasts operations to other clients, stores an operation log plus periodic snapshots, and handles presence (cursors, who's online) as separate, non-stored messages. Offline clients sync operations when they reconnect.

## 315: How would you scale a chat system to millions of users?

- **Gateway layer** holding WebSocket connections, scaled horizontally, with a registry of which gateway each user is on (in Redis).
- **Message service** that assigns a per-conversation sequence number, stores the message, then routes it to recipients' gateways via a pub/sub or direct RPC.
- **Storage** partitioned by conversation ID, sorted by sequence: Cassandra/ScyllaDB or similar. Recent messages cached.
- **Ordering:** per conversation only, using the sequence number. Clients use it to detect gaps and refetch.
- **Delivery receipts:** sent, delivered, read, sent back as small events.
- **Group chats:** for big groups, fan out on read, or limit live fan-out.
- **Offline:** push notifications, and a sync endpoint "give me messages after sequence N".
- **Presence:** heartbeats with TTL in Redis, and only push presence changes to contacts who are online.

## 316: How do you keep inventory correct during a checkout under heavy load?

- Make the stock decrement atomic and conditional: `UPDATE stock SET qty = qty - 1 WHERE sku = ? AND qty >= 1`. If 0 rows change, it's sold out. No read-then-write.
- Reserve stock at checkout with an expiry, and confirm or release it after payment.
- For flash sales on one hot SKU, the single row becomes a bottleneck. Options: split stock into several sub-rows ("buckets") and pick one randomly, keep the counter in Redis with an atomic Lua decrement and write to the DB asynchronously, or put buyers in a queue that processes orders one by one.
- Decide the business rule for overselling: some shops accept a small oversell and cancel later; others must never oversell.
- Reconcile counts regularly against orders.

## 317: How would you design a distributed cache?

- **Partitioning:** consistent hashing with virtual nodes to spread keys across nodes, so adding a node moves only a small share of keys.
- **Client or proxy routing:** clients know the ring (like Redis Cluster with hash slots), or a proxy routes requests.
- **Replication:** each partition has replicas for availability; replicas may lag.
- **Eviction:** LRU or LFU per node, with TTLs.
- **Failure handling:** if a node dies, its keys miss until refilled, so protect the database from the sudden load with request coalescing and rate limits.
- **Hot keys:** replicate hot keys to several nodes, or add a small local cache in the app.
- **Memory:** watch fragmentation and big values; set a max value size.

Remember the cache is not the source of truth; the system must still work (slower) if it's empty.

## 318: How would you design a Dynamo-style key-value store?

- **Partitioning** with consistent hashing and virtual nodes.
- **Replication** to N nodes clockwise on the ring.
- **Tunable quorums:** a write succeeds after W replicas confirm, a read asks R replicas. With `R + W > N` reads overlap the latest write.
- **Versioning** with vector clocks or simpler last-write-wins timestamps to resolve conflicts.
- **Sloppy quorum and hinted handoff:** if a replica is down, another node accepts the write and hands it back later.
- **Anti-entropy** with Merkle trees to find and repair differences between replicas.
- **Gossip** for membership and failure detection.
- **Storage engine:** an LSM tree for fast writes.

This is the design described in Amazon's 2007 Dynamo paper and used by Cassandra and Riak (DynamoDB the service works differently internally).

## 319: How would you design an ad click aggregation system?

Requirements: count clicks per ad per minute, in near real time, accurately, at very high volume, and filter fraud.

- Clicks hit a lightweight endpoint that logs an event (with a unique click ID) to Kafka and redirects the user.
- A stream processor (Flink, Kafka Streams, Spark Structured Streaming) groups by ad ID in one-minute tumbling windows, deduplicates by click ID, and writes results to an analytics store (ClickHouse, Druid, Pinot).
- Use event time and watermarks so late clicks are counted in the right minute.
- Keep the raw events in object storage, and run a batch job to recompute and reconcile counts for billing.
- Hot ads can create hot partitions; pre-aggregate locally before sending to the final aggregator.

Billing numbers come from the reconciled batch data; dashboards use the real-time ones.

## 320: How would you design a file sync service like Dropbox?

- Split files into chunks (for example 4 MB), hash each chunk, and only upload chunks the server doesn't already have. This gives deduplication and faster sync after small edits.
- Store chunks in object storage by hash; store file metadata (path, version, list of chunk hashes) in a database.
- A sync service tracks changes per user and notifies other devices (long polling, WebSockets or push).
- Clients keep a local index and send only changes.
- Conflicts (two devices edit offline): keep both versions, creating a "conflicted copy", rather than losing data.
- Version history by keeping old chunk lists.
- Compress and encrypt chunks; resume interrupted uploads.

## 321: How would you design product search for a large e-commerce site?

- **Index:** Elasticsearch/OpenSearch (or similar) with product fields, categories, attributes, price, stock and popularity. The catalog database is the source of truth; changes flow to the index through events or CDC.
- **Query:** full-text matching with typo tolerance, synonyms and language analyzers, plus filters and facets.
- **Ranking:** text relevance blended with business signals (sales, ratings, margin, stock). Often a second re-ranking step, sometimes with machine learning or vector search for semantic matching.
- **Freshness:** price and stock change often; update those fields with small partial updates, or check them at display time.
- **Scale:** shard the index, add replicas for read load, cache popular queries.
- **Reindexing** with zero downtime using index aliases.
- Track search analytics (no-result queries, clicks) to improve results.

## 322: How do you deal with the noisy neighbor problem in a multi-tenant system?

A noisy neighbor is a tenant whose heavy usage slows down others on shared resources.

- **Per-tenant rate limits and quotas** on API calls, jobs and storage.
- **Fair queuing:** separate queues per tenant or weighted round robin, so one tenant's 1 million jobs don't block others.
- **Resource isolation:** move big tenants to dedicated database shards or clusters.
- **Shuffle sharding:** assign each tenant to a random small set of workers so a bad tenant affects few others.
- **Query limits:** timeouts and row limits per request.
- **Monitoring per tenant** so you can see who is causing the load.

Charge for usage too; pricing that matches cost discourages abuse.

## 323: How would you design a feature flag service?

- **Admin UI and API** to create flags with rules: on/off, percentage rollout, targeting by user, plan, country, etc.
- **Storage** in a database with audit logs of every change.
- **Evaluation in the client SDK, locally:** services download the full rule set and evaluate flags in memory, so a flag check is a function call, not a network call.
- **Updates** pushed to SDKs with streaming (SSE) or polling every few seconds.
- **Consistent bucketing:** hash `flagKey + userId` so a user stays in the same group across requests and services.
- **Resilience:** SDKs keep the last known rules and have hardcoded defaults if the service is unreachable.
- **Front-end flags:** evaluate on the server for sensitive rules, so you don't send all targeting rules to the browser.
- Flag lifecycle: owners, expiry and alerts on stale flags.

## 324: How do distributed locks work and why can they be dangerous?

A distributed lock lets only one process across many machines do something at a time, using Redis (`SET key value NX PX 30000`), ZooKeeper, etcd or a database row.

The danger: a lock with an expiry can expire while the holder is still working, for example after a long GC pause or network delay. Then two processes believe they hold the lock. Redis-based algorithms like Redlock have been criticized for this reason.

The fix for correctness is a **fencing token**: each time the lock is granted, the lock service returns an increasing number. The protected resource (like the database) rejects writes with a token lower than one it has already seen. If you only need a lock for efficiency (avoid doing work twice) a simple Redis lock is fine. If you need it for correctness, use fencing tokens or a database constraint instead.

## 325: What is leader election and how is it done?

Leader election picks one node among many to do a special job (coordinating writes, running scheduled tasks). If the leader dies, another must take over, and there must never be two leaders acting at once.

Ways to do it:

- Use a consensus-based store: etcd, ZooKeeper or Consul. Nodes compete to create a key with a lease; the winner renews it. Kubernetes uses Lease objects this way.
- Use a consensus algorithm built in (Raft in etcd, CockroachDB, Kafka KRaft).
- A database row with a lease and timestamp for simple cases.

Because a leader can be paused and come back after losing its lease, use fencing tokens or terms so old leaders' actions are rejected.

## 326: How does the Raft consensus algorithm work at a high level?

Raft keeps a replicated log in sync across a cluster of nodes (usually 3 or 5).

- **Leader election:** nodes are followers, candidates or the leader. If followers stop hearing heartbeats, one becomes a candidate, increases the **term** number and asks for votes. A node with a majority becomes the leader.
- **Log replication:** clients send writes to the leader. The leader appends them to its log and sends them to followers. Once a majority have stored an entry, it is committed and applied.
- **Safety:** a node only votes for candidates whose log is at least as up to date as its own, so committed entries are never lost.

A 5-node cluster keeps working with 2 nodes down. etcd, Consul, CockroachDB and Kafka's KRaft use Raft.

## 327: How do quorums work in replicated databases?

With N replicas, a write waits for W acknowledgements and a read asks R replicas.

- If `R + W > N`, every read set overlaps every write set in at least one node, so a read can find the latest value (assuming no other problems like sloppy quorums or clock-based conflicts).
- Common setting: N=3, W=2, R=2.
- W=1 gives fast writes but weaker durability; R=1 gives fast reads but possible stale data.
- Majority quorums also tolerate `N - W` failed nodes for writes.

Cassandra lets you choose per query: `ONE`, `QUORUM`, `LOCAL_QUORUM`, `ALL`.

## 328: What are vector clocks and why are they used?

A vector clock is a list of counters, one per node, attached to each version of a value. When a node updates a value, it increments its own counter. By comparing two vector clocks you can tell if one version happened before the other (all counters less or equal) or if they are concurrent (each has some counter higher). Concurrent versions are real conflicts that must be merged, by the application or a rule. They are used in Dynamo-style stores and sync systems. The downside is that the vectors grow with the number of nodes or clients.

## 329: What is wrong with last-write-wins conflict resolution?

Last-write-wins (LWW) keeps the value with the latest timestamp and throws away the other. Problems:

- **Clock skew:** machines' clocks differ, so a write that actually happened later can have an earlier timestamp and be lost.
- **Silent data loss:** concurrent writes are dropped without anyone knowing. Two users adding items to the same cart: one item disappears.
- It works only when losing concurrent updates is acceptable, like overwriting a profile photo.

Better options for important data: version checks (reject and retry), merging (CRDTs), or keeping both versions for the user to resolve.

## 330: What are Lamport timestamps?

A Lamport timestamp is a logical clock: a counter each process keeps. It increments the counter on each event, sends it with messages, and on receiving a message sets its counter to `max(own, received) + 1`. This gives a total order of events that respects cause and effect: if A caused B, A's timestamp is smaller. But the reverse isn't true; a smaller timestamp doesn't prove causality, which is what vector clocks add. Lamport clocks are used for ordering in distributed algorithms without trusting physical clocks.

## 331: What are CRDTs?

CRDTs (Conflict-free Replicated Data Types) are data structures designed so replicas can be updated independently, even offline, and always merge into the same result, no matter the order of merges. Examples:

- **G-Counter:** each node has its own counter; the value is the sum, merge takes the max per node.
- **OR-Set:** a set where adds and removes merge correctly.
- **LWW-Register**, and sequence CRDTs for text editing.

They are used in collaborative editors (Yjs, Automerge), Redis Enterprise active-active, Riak, and offline-first apps. The costs are extra metadata and the fact that not every business rule (like "balance never below zero") can be expressed as a CRDT.

## 332: What is a gossip protocol?

In a gossip protocol, each node periodically picks a few random nodes and exchanges state with them, like how rumors spread. Information reaches all nodes quickly (in roughly log N rounds) without any central server, and the protocol keeps working when nodes fail. It is used for cluster membership and failure detection (Cassandra, Consul's Serf, SWIM protocol), and for spreading metadata. The trade-off is that information spreads with a delay and is eventually consistent.

## 333: What is split brain and how do you prevent it?

Split brain happens when a network partition divides a cluster and both sides think they are in charge, for example two database primaries accepting writes. When the network heals, the data has diverged and may be lost or conflicting.

Prevention:

- **Majority quorum:** only the side with more than half the nodes can elect a leader or accept writes. That's why clusters use odd numbers (3, 5).
- **Fencing:** stop the old primary from writing, using fencing tokens or by cutting it off (STONITH: "shoot the other node in the head").
- **A witness/arbiter node** in a third location to break ties between two data centers.

## 334: What is the difference between crash faults and Byzantine faults?

- **Crash faults:** a node either works correctly or stops. It never lies. Raft and Paxos tolerate these, and need `2f + 1` nodes to survive `f` failures.
- **Byzantine faults:** a node can behave arbitrarily, sending wrong or conflicting data because of bugs or attacks. Byzantine fault tolerant algorithms (PBFT and blockchain consensus) need `3f + 1` nodes and are much more expensive.

Most company systems assume crash faults because all nodes are under one owner's control. Byzantine tolerance matters when parties don't trust each other.

## 335: What is the difference between linearizability and serializability?

- **Linearizability** is about single objects and real time: once a write completes, every later read (in real time) sees it, as if there were one copy of the data. It is the "C" in CAP.
- **Serializability** is about transactions over many objects: the result is the same as if transactions ran one after another in some order. That order doesn't have to match real time.

**Strict serializability** combines both. Spanner offers it. Many databases called "serializable" don't guarantee the real-time part.

## 336: What consistency models sit between strong and eventual consistency?

- **Read-your-writes:** a user always sees their own changes.
- **Monotonic reads:** a user never sees data go back in time (newer, then older).
- **Monotonic writes:** a user's writes are applied in the order they were made.
- **Consistent prefix:** readers see updates in an order that makes sense (an answer never shows before its question).
- **Causal consistency:** things that are causally related are seen in the same order by everyone; unrelated things may differ.

These "session guarantees" give users a sane experience at a much lower cost than full strong consistency. MongoDB causal sessions and Azure Cosmos DB consistency levels expose several of them.

## 337: What does "exactly-once" in Kafka really mean?

Kafka offers exactly-once semantics through:

- **Idempotent producers:** the broker deduplicates retries using a producer ID and sequence numbers, so a retry doesn't create a duplicate in the log.
- **Transactions:** a producer can write to several partitions and commit consumer offsets atomically. Consumers using `read_committed` only see committed messages.

This gives exactly-once for "read from Kafka, process, write to Kafka" pipelines (Kafka Streams uses it). It does not cover side effects outside Kafka, like writing to a database or calling an API. For those you still need idempotent writes or to store offsets in the same database transaction as the result.

## 338: What is change data capture?

Change data capture (CDC) reads a database's own change log (Postgres WAL, MySQL binlog, MongoDB change streams) and turns every insert, update and delete into an event, usually published to Kafka. Debezium is the best-known open-source tool; cloud services like AWS DMS do it too.

Uses: keeping search indexes, caches and data warehouses in sync, implementing the outbox pattern without polling, and migrating databases. Since it reads the log, it doesn't need changes to application code and doesn't miss writes. You need to manage schema changes and decide how to expose internal table structure (often by streaming only outbox tables).

## 339: What are the Lambda and Kappa architectures?

Both are for processing large data with fresh results.

- **Lambda:** two paths. A batch layer reprocesses all data periodically for accurate results; a speed layer processes new data in real time for fresh but approximate results. A serving layer merges both. Downside: the same logic written and maintained twice.
- **Kappa:** one path. Everything is a stream, stored in a replayable log like Kafka. To recompute, you replay the log through a new version of the stream job.

Modern stream processors (Flink) and lakehouse tools have made Kappa-style designs more common.

## 340: What are windows, event time and watermarks in stream processing?

- **Windows** group an unbounded stream into chunks to aggregate: tumbling (fixed, non-overlapping, like every minute), sliding (overlapping), and session windows (closed after a period of inactivity).
- **Event time** is when the event happened; **processing time** is when the system sees it. Mobile devices and network delays make these differ, so correct results use event time.
- **Watermarks** are the system's estimate of "we've probably seen all events up to time T", so it can close a window. Events arriving after the watermark are **late events**; you can drop them, update the result, or send them to a side output.

The trade-off is between waiting longer (more correct) and emitting faster (lower latency).

## 341: What problems come up with event sourcing in production?

- **Long streams:** replaying thousands of events for each load is slow. Use **snapshots** every N events.
- **Event schema changes:** old events can't be edited. Use **upcasting** (convert old versions on read) or versioned handlers.
- **Projections:** read models must be rebuilt when their logic changes, which can take hours on big stores. Plan for rebuild time and run old and new side by side.
- **Deleting personal data (GDPR)** in an immutable log: use crypto-shredding (encrypt personal data per user and delete the key) or store personal data outside the events.
- **Querying:** you can't query current state directly; you need projections.
- **Team learning curve** and harder debugging.

Use it for the parts of the domain where history really matters, not everywhere.

## 342: How do you handle eventual consistency in the UI when using CQRS?

After a command succeeds, the read model may not be updated yet, so a page reload may show old data. Options:

- **Return the result** from the command and update the UI from it, not from a re-read.
- **Optimistic UI** updates.
- **Wait for the projection:** the command returns a version; the client or server waits until the read model has reached that version (with a timeout).
- **Push updates** to the client over WebSockets/SSE when the projection updates.
- **UX wording:** "Your order is being processed" instead of pretending it's instant.
- Read your own writes from the write model for that user for a short time.

## 343: What are the tricky parts of designing sagas?

- **Compensations are not rollbacks.** You can't un-send an email; you send a correction. Some steps are impossible to compensate, so put them last (the "pivot" step after which the saga only moves forward).
- **No isolation:** other transactions see intermediate states. Use **semantic locks** (status `PENDING`) so other processes know a record is in the middle of a saga.
- **Failures during compensation** must be retried until they succeed, so compensations must be idempotent.
- **Timeouts:** what if a service never answers? The orchestrator needs timers.
- **Observability:** you need to see each saga's current step and history.
- **Concurrent sagas** on the same data can conflict, so use version checks.

Workflow engines handle much of the state and retry logic for you.

## 344: How do you implement the outbox publisher reliably?

Two common ways:

- **Polling publisher:** a worker regularly selects unpublished rows, ordered by ID, publishes them and marks them published. Use `FOR UPDATE SKIP LOCKED` if several workers run, or a single leader to keep order. Simple, but adds DB load and some latency.
- **CDC (log tailing):** Debezium reads new outbox rows from the database log and publishes them. Low latency, no polling, keeps commit order.

Details to handle:

- Events can be published more than once, so include an event ID for consumers to deduplicate.
- Keep per-aggregate order by using the aggregate ID as the message key.
- Clean up old outbox rows.
- Monitor the outbox size: if it grows, publishing is broken.

## 345: What is the inbox pattern?

The inbox pattern is the consumer-side partner of the outbox. When a message arrives, the consumer saves its message ID in an `inbox` table in the same transaction as the business change. If the same message arrives again, the insert fails on the unique ID and the consumer skips it. Some variations first store the whole message in the inbox and process it later from there, which also decouples receiving from processing. Together, outbox and inbox give effectively-once processing on top of at-least-once delivery.

## 346: What is a poison message and how do you handle it?

A poison message is one that always fails processing, because of bad data, an unknown schema version, or a bug. If you retry it forever, it blocks the queue (or a Kafka partition, since order must be kept) and burns resources.

Handling:

- Limit retries and move the message to a DLQ after N attempts.
- Tell apart temporary errors (retry) from permanent ones like validation errors (send straight to DLQ).
- In Kafka, use retry topics with delays and a DLQ topic, so the main partition keeps moving. Be aware this changes ordering for that key.
- Alert on DLQ growth, and have tooling to inspect, fix and replay messages.

## 347: How do you scale consumers while keeping message order per entity?

Order and parallelism conflict, so you limit order to what really needs it, usually one entity:

- **Kafka:** key messages by entity ID. All messages for one entity go to one partition, read by one consumer. More partitions give more parallelism. Choose enough partitions up front, because changing the count changes key-to-partition mapping.
- **Inside a consumer:** you can process different keys in parallel with a small in-memory queue per key, while keeping one key in order (Confluent's Parallel Consumer does this).
- **SQS FIFO:** message group ID per entity; different groups process in parallel.
- **Versions:** include a version number so consumers can detect and ignore out-of-order old events if they still happen.

## 348: How do you deal with hot partitions or hot keys?

A hot key is one key that gets far more traffic than others, overloading one shard or partition (a celebrity profile, a viral product, one huge tenant).

Fixes:

- **Cache** hot reads, including a short local in-memory cache in each app server.
- **Replicate** hot keys to several cache nodes and read from any.
- **Split the key** for writes: `counter:42:0` ... `counter:42:9`, write to a random one, sum on read.
- **Better key design:** add a suffix or hash so writes spread out.
- **Isolate** very large tenants on their own shard.
- **Request coalescing** so many identical requests turn into one backend call.

Detect them first with per-key metrics or sampling.

## 349: What are virtual nodes in consistent hashing, and what is rendezvous hashing?

With plain consistent hashing, each server owns one arc of the ring, and arcs can be very uneven. **Virtual nodes** put each server on the ring many times (100+ positions). This spreads load evenly, lets stronger servers take more virtual nodes, and when a server leaves, its load is spread across many servers instead of falling on one neighbor.

**Rendezvous (highest random weight) hashing** is an alternative: for each key, compute `hash(key, server)` for every server and pick the highest. It also moves only `1/N` of keys when servers change, needs no ring, and gives even distribution, at the cost of O(N) work per lookup.

## 350: What race conditions can make a cache serve stale data, and how do you avoid them?

Classic race with cache-aside:

1. Request A misses the cache and reads the old value from the DB.
2. Request B updates the DB and deletes the cache key.
3. Request A writes the old value into the cache.

Now the cache holds stale data until the TTL expires.

Mitigations:

- Always set a TTL so mistakes heal.
- **Delayed double delete:** delete the key after the update, then again a short time later.
- **Leases** (from Facebook's memcache paper): a miss gets a lease token, and the cache only accepts a set with a valid token; a delete invalidates the token.
- **Versioned values:** only write if the version is newer than what's cached.
- Update the cache from a CDC stream in commit order rather than from app code.

## 351: How do you handle cache warm-up and cold starts?

A cold (empty) cache after a deploy, a restart or a new region sends all traffic to the database at once.

- **Pre-warm** the cache with the most popular keys before sending traffic, from access logs or a list.
- **Ramp traffic** slowly to new nodes or regions.
- **Persistent caches:** Redis with persistence or replicas so a restart doesn't lose everything.
- **Request coalescing** to prevent stampedes on the same key.
- **Rate limit** database access and use the circuit breaker so the DB doesn't fall over.
- Don't flush all caches at once during deploys; use versioned keys and let old ones expire.

## 352: What is multi-level caching and what problems does it bring?

Multi-level caching stacks caches: browser, CDN, local in-process cache, distributed cache (Redis), and the database's own cache. Each level cuts load on the next and lowers latency.

Problems:

- **Invalidation gets harder:** you must clear or expire data at every level. Local caches on 100 servers need a broadcast (pub/sub) or very short TTLs.
- **Staleness adds up:** a 60s TTL at each of three levels can mean 3 minutes of stale data.
- **Debugging:** "which level served this?". Add headers like `X-Cache` and metrics per level.

Use short TTLs at outer levels for data that changes, and long TTLs only for versioned or immutable data.

## 353: What is tail latency and why does it matter more in systems with fan-out?

Tail latency is the latency of the slowest requests, like p99 or p99.9. If one service is slow 1% of the time, and a page calls 100 such services in parallel, about 63% of page loads will hit at least one slow call (`1 - 0.99^100`). So in fan-out systems, the rare slow case becomes the common case for users. Causes include GC pauses, noisy neighbors, cache misses, queueing and retries. That's why SLOs use percentiles, not averages.

## 354: What techniques reduce tail latency?

- **Hedged requests:** if a request hasn't answered after, say, the p95 time, send the same request to another replica and use whichever answers first. Small extra load, big tail improvement. Only for idempotent reads.
- **Tied requests:** send to two replicas, and the one that starts first cancels the other.
- **Timeouts with fallbacks** or partial results.
- **Reduce variability:** avoid GC pauses, limit background work, isolate noisy neighbors.
- **Load balancing on real load** (least outstanding requests) instead of round robin.
- **Smaller fan-out** and caching of slow dependencies.

These ideas come from Google's "The Tail at Scale" paper.

## 355: What is load shedding?

Load shedding means deliberately rejecting some requests when a system is overloaded, so it can keep serving the rest well. Without it, all requests slow down, time out, get retried, and the system collapses.

How:

- Limit concurrent requests or queue length, and return `503` or `429` quickly above the limit.
- Drop requests that have already waited longer than the client's timeout; nobody is waiting for them anymore.
- Prioritize: shed analytics and background calls before checkout and login.
- Reject early, at the edge, where it's cheap.

It feels wrong to fail requests on purpose, but serving 80% well is better than serving 100% badly.

## 356: What are adaptive concurrency limits?

Instead of a fixed limit on concurrent requests to a service (which is always either too high or too low as conditions change), the limit adjusts itself based on observed latency. Like TCP congestion control: if latency stays low, increase the limit slowly; if latency rises (a sign of queueing), cut it. Algorithms include AIMD and gradient-based ones. Netflix's `concurrency-limits` library and Envoy's adaptive concurrency filter implement this. It protects services from overload without manual tuning.

## 357: What is a retry budget?

A retry budget caps retries as a share of normal traffic, for example "retries may add at most 10% extra requests". When a downstream service is healthy, failed calls are retried as usual. When it is failing a lot, the budget runs out and further failures are not retried, so clients don't multiply the load on a struggling service. gRPC's retry throttling and Envoy's retry budgets work this way. It is safer than a fixed "retry 3 times" rule, which triples load exactly when the system is weakest.

## 358: What is a cascading failure and how do you prevent it?

A cascading failure is when a failure in one part causes failures in others, spreading through the system. Example: the database slows down, API requests wait longer, threads fill up, the API stops answering health checks, the load balancer removes instances, the remaining ones get more load and also fail.

Prevention:

- Timeouts on every call, with deadline propagation.
- Circuit breakers and bulkheads.
- Load shedding and back-pressure.
- Limited retries with backoff, jitter and budgets.
- Health checks that don't fail just because a dependency is slow.
- Capacity headroom, and autoscaling that can't scale faster than the database can handle.
- Graceful degradation for non-critical features.

## 359: What is a metastable failure?

A metastable failure is when a system stays broken even after the original cause is gone. A trigger (a traffic spike, a short outage) pushes it into a bad state, and a feedback loop keeps it there. Example: a cache outage sends traffic to the database, requests time out, clients retry, retries keep the database overloaded, and even after the cache is back, the retry load prevents recovery.

Fixes are about breaking the loop: retry budgets, load shedding, dropping expired work, and having emergency levers to cut load (turn off retries, block non-essential traffic) so the system can return to normal.

## 360: What is cell-based architecture?

Cell-based architecture splits the whole system into many independent copies called cells, each with its own app servers, databases and queues, serving a subset of customers. A thin routing layer sends each customer to their cell. If a bad deploy or overload hits one cell, only its customers are affected. You scale by adding cells instead of making one huge deployment. AWS uses this widely. Downsides: more infrastructure to manage, a routing layer that must be very reliable, and harder cross-cell features and customer moves between cells.

## 361: What is shuffle sharding?

With normal sharding, if a bad customer (a poison request or a flood) kills their shard, every other customer on that shard goes down too. With shuffle sharding, each customer is assigned a random combination of a few workers out of many. For example, 8 workers, each customer gets 2 of them: there are 28 possible pairs, so two customers rarely share both workers. When one customer's traffic breaks their two workers, most other customers still have at least one healthy worker. AWS Route 53 uses this to isolate customers.

## 362: How do you reduce the blast radius of failures and changes?

Blast radius is how much of the system or how many users are affected when something goes wrong.

- **Deploy gradually:** canary, then one zone or cell, then one region, then all, with automatic rollback on bad metrics.
- **Isolate:** cells, bulkheads, separate clusters for critical and non-critical workloads.
- **Limit config changes** the same way as code deploys; many big outages are config pushes.
- **Feature flags** to turn things off fast.
- **Regional independence:** avoid global dependencies that every region needs.
- **Limit permissions** so one mistake or compromised credential can't touch everything.

## 363: What is chaos engineering?

Chaos engineering means running controlled experiments that inject failures into a system to see how it really behaves: killing instances, adding network latency, failing a dependency, filling disks or cutting a region. You start with a hypothesis ("if one Redis node dies, checkout keeps working"), keep the blast radius small, measure, and fix what breaks. Netflix's Chaos Monkey made it famous; tools include AWS Fault Injection Service, Gremlin, Chaos Mesh and LitmusChaos. Game days (planned team exercises) are a lighter version.

## 364: What are the challenges of replicating data across regions?

- **Latency:** regions are 50-300 ms apart, so synchronous replication makes writes slow.
- **Async replication** means a failover can lose recent writes (RPO > 0).
- **Writes in several regions** create conflicts; you need conflict resolution or to route writes per record to a home region.
- **Consistency:** users may see different data in different regions.
- **Cost:** cross-region traffic is expensive.
- **Data residency laws** may forbid copying some data out of a region.
- **Failover testing:** many teams find their failover doesn't work only during a real outage.

Distributed SQL databases (Spanner, CockroachDB, Aurora DSQL, YugabyteDB) can hide some of this, at a cost in write latency.

## 365: How does data residency or GDPR affect architecture?

- **Data residency:** some customers or laws require data to stay in a country or region, so you need regional deployments and storage, and must route each user's data to their region. Logs, backups, analytics and third-party tools count too.
- **Right to erasure:** you must be able to find and delete a person's data everywhere: databases, caches, search indexes, backups (or let them expire), event logs (crypto-shredding helps).
- **Data minimization:** don't collect or log data you don't need.
- **Access control and audit logs** for personal data.
- **Data maps:** know where personal data lives and flows, including sub-processors.

Designing for this early is much cheaper than retrofitting it.

## 366: How would you scale a relational database step by step as traffic grows?

1. **Optimize first:** indexes, fix slow queries and N+1s, connection pooling.
2. **Scale up** to a bigger machine; it's often cheaper than complexity.
3. **Add caching** for hot reads.
4. **Add read replicas** and send read-only queries to them.
5. **Move workloads out:** analytics to a warehouse, search to a search engine, files to object storage, logs and events elsewhere.
6. **Split by feature (functional partitioning):** put different modules' tables on different databases.
7. **Partition big tables** by time or key within one database.
8. **Shard** by a key like tenant or user, with Citus, Vitess or app-level routing; or move to a distributed SQL database.

Each step adds complexity, so go to the next one only when measurements show you need it.

## 367: How do you handle queries and transactions that cross shards?

- **Avoid them by design:** pick a shard key so most queries stay in one shard (all of a tenant's data together).
- **Scatter-gather:** send the query to all shards and merge results. Fine for rare admin queries, bad for hot paths, and pagination and sorting across shards are tricky.
- **Secondary indexes or lookup tables** that map other attributes to shard keys.
- **Denormalized read models** (CQRS) built from events for cross-shard views.
- **Cross-shard writes:** use sagas, or a database that supports distributed transactions (Spanner, CockroachDB, Vitess with 2PC), accepting the latency.

## 368: How do secondary indexes work in a sharded database?

Two main approaches:

- **Local (document-partitioned) indexes:** each shard indexes only its own data. Writes are simple and fast, but a query by the indexed field must ask every shard (scatter-gather).
- **Global (term-partitioned) indexes:** the index is partitioned by the indexed value, separately from the data. A query by that field goes to one index partition, but a write may need to update index partitions on other nodes, which is usually done asynchronously, so the index can lag.

DynamoDB global secondary indexes are eventually consistent for this reason; local secondary indexes share the partition key with the table.

## 369: How do you change the schema of a very large table in production?

Some `ALTER TABLE` operations lock or rewrite the whole table, which can take hours on billions of rows.

- Check which operations are cheap in your database version. In Postgres, adding a nullable column, or one with a constant default (since v11), is instant; changing a column type usually rewrites the table.
- Use online schema change tools for MySQL: `gh-ost` or `pt-online-schema-change`, which build a copy of the table, keep it in sync, then swap. Postgres options include `pg_repack` and tools like `pgroll` or Reshape for expand-contract migrations.
- Create indexes with `CONCURRENTLY` in Postgres.
- Set a `lock_timeout` so a migration waiting for a lock doesn't block all queries behind it.
- Use expand and contract with the app supporting both shapes.
- Backfill in small batches with throttling.

## 370: How do you backfill data safely in a large production system?

- Make the backfill **idempotent** and **resumable**: track progress (last processed ID) so it can stop and continue.
- Process in **small batches** with short transactions, ordered by primary key.
- **Throttle** based on database load and replication lag, and pause automatically if they rise.
- Run it as a **background job**, not inside a deploy.
- Make sure **new writes** are already handled by the app (dual writes) before backfilling old data, so nothing is missed.
- **Verify** with counts or checksums afterward.
- Test on a copy of production data first.

## 371: What is MVCC?

MVCC (Multi-Version Concurrency Control) lets readers and writers work at the same time without blocking each other. Instead of overwriting a row, the database keeps several versions. Each transaction sees a snapshot of the data as of when it (or its statement) started. Writers create new versions; readers keep reading the old version that matches their snapshot. PostgreSQL, MySQL InnoDB, Oracle and many others use it. The cost is old versions that must be cleaned up later (VACUUM in Postgres, purge in InnoDB), and long-running transactions prevent that cleanup and cause table bloat.

## 372: What is the difference between B-tree and LSM-tree storage engines?

- **B-tree** (Postgres, MySQL InnoDB): data is kept in sorted pages that are updated in place. Fast reads and range scans; writes cause random disk I/O and page splits.
- **LSM-tree** (Cassandra, RocksDB, ScyllaDB, LevelDB): writes go to an in-memory table and a log, then are flushed to sorted immutable files on disk, which are merged in the background (compaction). Very fast writes; reads may check several files, helped by Bloom filters. Compaction uses CPU and I/O.

Rule of thumb: B-trees for read-heavy and general OLTP, LSM trees for very write-heavy workloads.

## 373: What is a write-ahead log?

A write-ahead log (WAL) is an append-only file where a database writes every change before applying it to the main data files. If the database crashes, it replays the log on restart to recover committed changes. Appending to a log is fast and sequential, so commits are quick. The WAL is also used for replication (replicas replay the primary's log), point-in-time recovery, and change data capture. The same idea, a durable log as the source of truth, is behind Kafka and event sourcing.

## 374: What is hot, warm and cold storage tiering?

Data is moved to cheaper storage as it gets older and less used:

- **Hot:** fast, expensive storage for current data (SSD databases, Redis).
- **Warm:** cheaper storage for older data still read sometimes (slower disks, S3 Standard-Infrequent Access).
- **Cold/archive:** very cheap storage for data kept for compliance and rarely read, with slow retrieval (S3 Glacier).

Examples: logs searchable for 14 days, then archived for a year; orders older than 3 years moved to an archive table or data lake. Lifecycle rules automate it. The architecture must handle the slower access for old data.

## 375: When do you use materialized views or precomputed read models?

When a read query is expensive (many joins, aggregations over millions of rows) and is run much more often than the data changes. Instead of computing it on every request, you store the result and update it:

- **Database materialized views** refreshed on a schedule (`REFRESH MATERIALIZED VIEW CONCURRENTLY` in Postgres).
- **Summary tables** updated by triggers or jobs.
- **Read models** updated from events (CQRS).
- **Stream processing** that keeps aggregates up to date continuously.

You trade freshness and storage for fast reads, so decide how stale the data can be.

## 376: How do you count things like likes or views at very large scale?

A single `UPDATE posts SET likes = likes + 1` row becomes a hot spot when thousands of users like the same post per second.

- **Sharded counters:** split one counter into N rows or keys, increment a random one, and sum them when reading.
- **Buffer and batch:** increment in Redis (`INCR`) or in memory, and flush totals to the database every few seconds.
- **Stream aggregation:** send events to Kafka and aggregate them in a stream job.
- **Store who liked separately** (a `likes(user_id, post_id)` table with a unique key) for correctness, and treat the count as a cached number that is periodically corrected.
- **Approximate counts** where exact numbers don't matter: HyperLogLog for unique viewers uses only about 12 KB per counter in Redis (`PFADD`, `PFCOUNT`) with about 1% error.

Users don't notice if a count is a few seconds behind, so eventual consistency is fine here.

## 377: How do you find the top K items (heavy hitters) in a huge stream?

Keeping an exact count for every item uses too much memory when there are billions of distinct items. Common approaches:

- **Count-Min Sketch:** a small 2D array of counters with several hash functions. It estimates counts with possible overcounting but never undercounting. Combined with a small min-heap of the current top K, it finds heavy hitters in fixed memory.
- **Space-Saving / Misra-Gries algorithms:** keep only K counters and replace the smallest when a new item appears.
- **Exact but split:** partition by item hash across many workers, count exactly per partition, then merge each partition's top K.

Use windows (top K per hour) and merge them for longer periods. Redis Stack has a Top-K data type built on these ideas.

## 378: How do you reindex a search cluster with zero downtime?

Changing mappings or analyzers usually needs a new index.

1. Clients always use an **alias** (`products`), never the real index name.
2. Create a new index (`products_v2`) with the new settings.
3. Start **dual writing** changes to both indexes, or record the time you started.
4. **Bulk load** all data into the new index from the source of truth (or with the reindex API).
5. Replay changes that happened during the load.
6. Check counts and run sample queries.
7. **Swap the alias** atomically to `products_v2`.
8. Keep the old index for a while for rollback, then delete it.

The same "build new, switch pointer" idea works for caches, read models and ML models.

## 379: What goes wrong when microservices are too small?

- Every user request needs many network calls, adding latency and more ways to fail.
- Features require changes to several services at once, so teams must coordinate deploys.
- Data that belongs together is spread out, so you need sagas and joins across services.
- Operational cost grows: each service needs pipelines, monitoring, alerts, on-call and upgrades.
- Hard to understand the whole system.

A good test: can most features be built by changing one service? If not, the boundaries may be wrong, and merging services is a valid fix. "Micro" should mean small enough for one team to own, not as small as possible.

## 380: How would you migrate a monolith to microservices?

1. **Have a reason:** team scaling, deploy speed, a part with different scaling needs. Not "because everyone does it".
2. **Modularize the monolith first:** find bounded contexts and make module boundaries clean inside the monolith.
3. **Build the platform:** CI/CD, observability, service templates.
4. **Pick a first candidate** that is fairly independent and valuable, and has clear data ownership. Avoid the core of the system at first.
5. **Strangler Fig:** route its traffic through a proxy to the new service.
6. **Move the data:** start with the service calling the monolith's data through an API or CDC, then give it its own database and sync.
7. **Repeat**, learning from each step. Stop when the remaining monolith is fine as it is.

Expect it to take a long time; plan for running both side by side.

## 381: Why do long synchronous call chains hurt availability?

If a request must pass through services in a chain, and each has 99.9% availability, the total availability is the product: five services give `0.999^5 ≈ 99.5%`, which is about 44 hours of downtime a year instead of 8.8. Latencies also add up, and a slowdown anywhere blocks everything.

Ways to fix it:

- Make calls async where the user doesn't need the result right away.
- Keep local copies of data you need from other services (from events) instead of calling them.
- Call independent services in parallel instead of in sequence.
- Use fallbacks so optional dependencies don't fail the whole request.
- Rethink boundaries if a chain is always needed.

## 382: How do you query data that lives in several services?

- **API composition:** a gateway, BFF or composer service calls each service and joins the results in memory. Simple, but slower, harder with filtering and sorting across services, and its availability depends on all of them.
- **CQRS read model:** a separate service subscribes to events from all involved services and keeps a denormalized view built for the query. Fast and independent, but eventually consistent and more to build.
- **Data warehouse** for reporting and analytics queries that don't need to be real time.

Use composition for simple cases with few services; build a read model when the query is frequent, needs complex filtering, or must be fast.

## 383: What is the TCC (Try-Confirm-Cancel) pattern?

TCC is a way to get transaction-like behavior across services with reservations:

1. **Try:** each service checks and reserves the resources (hold the seat, reserve the money) but doesn't commit.
2. **Confirm:** if all tries succeed, each service turns the reservation into a final change.
3. **Cancel:** if any try fails, the others release their reservations.

Compared with sagas, TCC avoids showing half-done results because things are only "reserved" until confirmed. But every service must support the three operations, reservations need timeouts, and confirm and cancel must be idempotent and retried until they succeed.

## 384: What is consumer-driven contract testing?

In microservices, end-to-end tests across all services are slow and flaky. With contract testing, each consumer writes down what it expects from a provider (requests and the response shape it relies on) as a contract. The provider's CI then runs those contracts against its real code to check it doesn't break any consumer. Pact is the most popular tool, and a broker stores contracts and tells you if it's safe to deploy a version ("can-i-deploy"). It catches breaking API changes before deploy, while each service still tests in isolation.

## 385: What do backward and forward compatibility mean for schemas, and how do they affect deploy order?

- **Backward compatible:** new consumers can read data written with the old schema. Example: adding an optional field with a default. Deploy **consumers first**, then producers.
- **Forward compatible:** old consumers can read data written with the new schema. Example: adding a field that old consumers simply ignore. Deploy **producers first**.
- **Full compatibility:** both at once, so deploy order doesn't matter. The safest choice for shared topics.

Schema registries (Confluent, Apicurio) enforce a chosen mode and reject schema changes that break it. Removing a required field or changing a type breaks compatibility and needs a new topic or event version.

## 386: What is zero trust architecture?

Zero trust means no request is trusted just because it comes from inside the network. Every request, from users or services, must be authenticated, authorized and encrypted, every time.

In practice:

- Strong identity for users (SSO, MFA) and services (mTLS, workload identity).
- Authorization checks in every service, using least privilege.
- Network segmentation and default-deny network policies.
- Device posture checks for employee access, often replacing VPNs (Google BeyondCorp is the well-known example).
- Continuous logging and monitoring.

It limits how far an attacker can move after breaking into one component.

## 387: How do you guarantee tenant data isolation in a shared database?

A missing `WHERE tenant_id = ?` in one query can leak data between customers, so don't rely only on developers remembering it.

- **Row-level security** in the database (Postgres RLS): the session sets the tenant, and the database itself filters rows.

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);

-- per request, inside a transaction
SET LOCAL app.tenant_id = '6f1c...';
```

- **Automatic scoping in the data layer:** a repository or ORM extension that always adds the tenant filter.
- **Tenant ID in composite keys and unique indexes.**
- **Tests** that try to read another tenant's data.
- **Separate caches keys and storage paths** per tenant too.
- For the highest isolation, separate schemas or databases.

Note: the app's database role must not be the table owner or a superuser, or RLS is skipped (unless `FORCE ROW LEVEL SECURITY` is set).

## 388: What is the difference between RBAC, ABAC and ReBAC?

- **RBAC (role-based):** users get roles (admin, editor, viewer), roles have permissions. Simple and common, but you end up with many roles for special cases.
- **ABAC (attribute-based):** rules use attributes of the user, resource and context: "managers can approve expenses under $5,000 in their own department during work hours". Very flexible, harder to understand and audit.
- **ReBAC (relationship-based):** access comes from relationships: "you can edit a document if you are an editor of its folder". Fits sharing models like Google Drive. Google's Zanzibar paper describes it; OpenFGA, SpiceDB and Permify implement it.

Policy engines like OPA or Cedar let you write these rules outside your app code. Many systems combine RBAC with a few ABAC rules.

## 389: How do you revoke JWTs before they expire?

JWTs are checked without a server lookup, so you can't just delete them. Options:

- **Short-lived access tokens** (5-15 minutes) with refresh tokens stored server-side. Revoke the refresh token, and the access token dies soon.
- **Denylist** of revoked token IDs (`jti`) in Redis, with TTL equal to the token's remaining life. Every service checks it; this adds a lookup but only for a small list.
- **Token version per user:** store a `tokenVersion` on the user; bump it on logout-all or password change, and reject tokens with an old version (needs a lookup, but can be cached).
- **Rotate signing keys** in an emergency, which invalidates all tokens.

For high-security actions, check the session against the server anyway.

## 390: How do you rotate secrets without downtime?

The key idea is to allow two valid secrets during the change.

1. Create the new secret (new DB password, new API key, new signing key) alongside the old one.
2. Make the consumers able to accept both (for verification keys) or switch to the new one (for credentials), usually by reloading from the secret manager without a restart.
3. Wait until all instances use the new secret.
4. Revoke the old one.

For signing keys, publish both keys (JWKS with `kid` headers) so tokens signed with either can be verified. Databases support this with two users that alternate. Managed tools like AWS Secrets Manager rotation lambdas or Vault dynamic credentials automate it. Practice rotation regularly, so it works when a leak forces you to do it quickly.

## 391: What is SSRF and how do you protect a system that fetches user-provided URLs?

SSRF (Server-Side Request Forgery) is when an attacker makes your server send requests to places it shouldn't, like internal services or the cloud metadata endpoint (`169.254.169.254`), which can expose credentials. Features at risk: webhooks, "import from URL", link previews, image fetching, PDF generators.

Protection:

- Resolve the hostname and block private, loopback, link-local and metadata IP ranges, and check again after each redirect (or disable redirects). Pin the resolved IP for the actual request to avoid DNS rebinding.
- Allow only `http`/`https` and expected ports.
- Run the fetcher in an isolated network segment or through an egress proxy with strict rules.
- Use IMDSv2 on AWS, which requires a token that SSRF usually can't get.
- Limit response size and time.

## 392: How do you protect a system from DDoS attacks at the architecture level?

- **Put a large edge network in front:** CDN and DDoS protection services (Cloudflare, AWS Shield, Google Cloud Armor, Akamai) can absorb huge volumetric attacks that no single origin could.
- **Hide the origin:** only accept traffic from the CDN's IPs.
- **WAF rules and bot detection** for application-layer attacks.
- **Rate limiting** per IP, per user and per endpoint, especially on expensive ones (login, search, checkout).
- **Cache** as much as possible so attack traffic is served from the edge.
- **Autoscaling** with sensible maximums, so an attack doesn't turn into a huge bill.
- **Make expensive work cheap to reject:** validate early, require auth, use CAPTCHAs or challenges.
- **Have a runbook** to tighten rules quickly during an attack.

## 393: What are CDN cache keys, cache poisoning and purge strategies?

- **Cache key:** what makes two requests "the same" for the CDN, by default the URL. If responses vary by header (language, device) or cookie, you must include it in the key (`Vary` or CDN config), or users get the wrong content. Including too much (all cookies, every query param) kills the hit rate.
- **Cache poisoning:** an attacker sends a request with an unkeyed input (like `X-Forwarded-Host`) that changes the response, and the CDN caches that poisoned response for everyone. Prevent it by not using unkeyed headers in responses, and by normalizing requests.
- **Purging:** use versioned file names for static assets (no purge needed), and surrogate keys/tags (purge everything tagged `product-42`) for dynamic pages. Avoid "purge everything" in production because it creates a stampede to the origin.

## 394: How would you build a system that holds millions of WebSocket connections?

- **Connection gateways:** a dedicated, simple service that only holds connections. Well-tuned servers can hold hundreds of thousands of idle connections each; raise file descriptor limits and keep per-connection memory small.
- **Separate business logic** into other services; the gateway only forwards messages.
- **Routing:** a registry (Redis) maps user or channel to gateway node, or gateways subscribe to channels on a pub/sub bus (NATS, Redis, Kafka).
- **Fan-out to big channels:** publish once per gateway, not per user; the gateway delivers to its local subscribers.
- **Load balancing:** L4 or L7 with long timeouts; spread new connections evenly.
- **Deploys and failures:** drain slowly so millions of clients don't reconnect at once; clients reconnect with jitter and resume from the last message ID.
- **Heartbeats** to detect dead connections.

Managed options: AWS API Gateway WebSockets, Ably, Pusher, Cloudflare Durable Objects.

## 395: How would you design an online presence system?

- Clients send a heartbeat every N seconds over their existing connection.
- The gateway updates `presence:user:42` in Redis with a TTL slightly longer than the heartbeat interval. If heartbeats stop, the key expires and the user is offline. No need to catch every disconnect.
- On status change (online/offline), publish an event, but only to users who care (friends who are online), not to everyone.
- **Debounce** changes so a flaky mobile connection doesn't flood friends with online/offline/online updates.
- For huge contact lists or groups, don't push presence; let clients fetch it when they open a chat.
- Accept that presence is approximate; "last seen 1 minute ago" is fine.

## 396: How do you handle a slow consumer in a data pipeline?

- **Measure lag:** consumer lag in Kafka, queue depth and message age. Alert on it.
- **Scale consumers** if processing is parallelizable, up to the number of partitions.
- **Batch** work, for example bulk inserts instead of one row at a time.
- **Back-pressure:** bounded buffers so the consumer doesn't run out of memory; producers slow down or the broker buffers on disk.
- **Separate fast and slow work:** move slow steps (external API calls) to their own queue.
- **Shed or sample** low-value data under overload.
- **Retention:** make sure the broker keeps data longer than the worst expected lag, or you lose messages.

## 397: How do you choose between batch, micro-batch and streaming?

- **Batch** (hourly or daily jobs): simplest, cheapest, easy to rerun; good when results can be hours old, like reports and billing.
- **Micro-batch** (every few seconds or minutes, like Spark Structured Streaming): near-real-time with batch-like simplicity.
- **True streaming** (per event, like Flink or Kafka Streams): lowest latency, needed for fraud detection, alerting, live dashboards; most complex (state, windows, late events, exactly-once).

Ask: how fresh must the result be, and what is it worth? Many teams run streaming for fresh but approximate numbers and a batch job for the final, correct numbers.

## 398: What is the difference between a data lake, a data warehouse and a lakehouse?

- **Data warehouse** (Snowflake, BigQuery, Redshift): structured, cleaned data in tables, optimized for SQL analytics. Fast and easy for analysts, but you must model data before loading.
- **Data lake** (files in S3 or GCS): stores raw data of any kind cheaply (JSON, logs, images, Parquet). Flexible, but without discipline it becomes a "data swamp" with no quality or schema.
- **Lakehouse** (Databricks, Apache Iceberg, Delta Lake, Apache Hudi): open table formats on top of lake storage that add transactions, schemas, time travel and good SQL performance. One copy of data for both BI and machine learning.

## 399: Why separate OLTP and OLAP workloads?

- **OLTP** (online transaction processing): many small, fast reads and writes by key, like placing an order. Row-oriented databases (Postgres, MySQL).
- **OLAP** (online analytical processing): few but huge queries scanning millions of rows and aggregating, like "revenue by region per month". Column-oriented stores (ClickHouse, BigQuery, Snowflake, DuckDB).

Running big analytical queries on the production database slows down user-facing traffic and the queries themselves are slow on row storage. So you copy data from OLTP to an OLAP store with ETL/ELT or CDC, and run analytics there.

## 400: What are head-based and tail-based sampling in tracing?

Storing every trace at high traffic is too expensive, so you sample.

- **Head-based sampling:** decide at the start of a request (keep 1%), and pass the decision to all services. Cheap and simple, but you'll probably miss the rare slow or failed requests you care about most.
- **Tail-based sampling:** collect all spans for a while, then decide after the trace is complete: keep all errors, all slow traces, and a small share of normal ones. Much more useful, but the collector must buffer spans, which costs memory and needs all spans of a trace to reach the same collector. The OpenTelemetry Collector supports this.

## 401: What is the high cardinality problem in metrics?

Each unique combination of metric name and label values is a separate time series. If you add a label like `user_id` or `request_id` to a metric, you can create millions of series. Time-series databases then use huge amounts of memory, slow down or crash, and bills go up. Rules: keep labels to small, bounded sets (status code, endpoint template like `/users/:id` not the real path, region). Put high-cardinality details in logs or traces instead, which are built for that kind of data.

## 402: How do error budgets guide engineering decisions?

If your SLO is 99.9% success over 30 days, your error budget is the 0.1% of requests that may fail. It turns reliability into a shared number:

- If plenty of budget is left, the team can ship faster and take more risk.
- If the budget is used up, the team slows down feature releases and works on reliability until it recovers.
- **Burn rate alerts:** alert when the budget is being used up much faster than normal (for example, a burn rate that would use the whole month's budget in two days), instead of alerting on every error spike.

It ends arguments between "ship faster" and "be more stable" with an agreed rule.

## 403: How do you do capacity planning?

1. **Measure current load and limits:** requests per second, CPU, memory, DB connections, queue depth, at peak, not average.
2. **Find each component's limit** with load tests: at what load does latency or errors go up?
3. **Forecast growth** from business plans and history, including seasonal peaks and marketing events.
4. **Add headroom** (often 30-50%) for spikes and for losing a zone or instance.
5. **Find the first bottleneck** (often the database) and plan for it early, since some changes take months.
6. **Review regularly**, and use autoscaling for short-term changes, but remember quotas and limits on things that can't autoscale.

## 404: How do you take cost into account in architecture decisions?

- Know the main cost drivers: compute, databases, data transfer (especially cross-region and egress to the internet), storage, managed service fees, logging and observability volume.
- Estimate cost per request, per user or per tenant, and watch it as you grow.
- Right-size instances, use autoscaling and scale to zero for dev environments.
- Use reserved or savings plans for steady load and spot instances for interruptible work.
- Cache to cut database and egress costs; use storage lifecycle rules.
- Reduce log volume and metric cardinality; they often grow quietly.
- Tag resources by team and feature so costs are visible (FinOps).

Sometimes a more expensive managed service is cheaper overall because it saves engineer time.

## 405: How do you decide what consistency level each feature needs?

Ask what goes wrong if a user sees stale or conflicting data, and how bad that is:

- **Strong consistency:** money, inventory, bookings, permissions, unique usernames. Wrong data causes real loss or security problems.
- **Read-your-writes:** profile edits, settings, posts the user just made. Users get confused if their own change disappears.
- **Eventual consistency:** like counts, view counts, recommendations, search results, analytics, feeds.

Then use the cheapest model that is acceptable per feature, instead of one level for the whole system. This often means one strongly consistent core database plus eventually consistent caches, search indexes and read models around it.

## 406: How does Google Spanner use clocks to give strong consistency?

Spanner uses TrueTime, an API backed by GPS receivers and atomic clocks in each data center, that returns the current time as an interval `[earliest, latest]` with a known small uncertainty (a few milliseconds). When a transaction commits, Spanner picks a timestamp and then **waits out the uncertainty** ("commit wait") before making it visible. This guarantees that if transaction A finishes before B starts, A's timestamp is lower, giving external consistency (strict serializability) across the globe. CockroachDB uses hybrid logical clocks instead, without special hardware, and handles uncertainty with retries.

## 407: What are the trade-offs of distributed SQL databases?

Distributed SQL (NewSQL) databases like Spanner, CockroachDB, YugabyteDB, TiDB and Aurora DSQL give SQL and ACID transactions while scaling horizontally and replicating across zones or regions.

Pros: no manual sharding, strong consistency, automatic failover, multi-region options.

Cons:

- Higher write latency, because commits need a consensus round trip, which is slow across regions.
- Cross-node transactions cost more; hot rows and sequential keys cause hotspots (use UUIDs or hashed keys).
- Not every Postgres or MySQL feature or extension is supported.
- Higher cost and operational learning curve than a single Postgres.

They make sense when you've outgrown one primary or need multi-region strong consistency, not as a default for small apps.

## 408: What problems show up with serverless at large scale?

- **Concurrency limits:** accounts have a max number of concurrent executions; one function's spike can starve others. Use reserved concurrency.
- **Downstream overload:** functions scale faster than databases or third-party APIs. Put a queue in between and limit consumer concurrency.
- **Database connections:** need a proxy or pooler.
- **Cold starts** at scale-out moments; use provisioned concurrency for latency-sensitive paths.
- **Cost** at constant high load can exceed containers.
- **Observability:** many small functions make tracing and debugging harder.
- **Timeouts and retries:** async invocations retry automatically, so handlers must be idempotent.
- **Distributed system complexity:** lots of small functions wired by events can become hard to follow.

## 409: What are the pitfalls of event-driven architecture?

- **Hard to follow the flow:** nobody can see the whole business process; it's spread across many subscribers. Document it and use tracing.
- **Event spaghetti:** services reacting to events that trigger more events, creating hidden chains and loops.
- **Eventual consistency** everywhere, which the UI and business must accept.
- **Duplicates and ordering:** consumers must be idempotent and deal with out-of-order events.
- **Schema evolution** of events is hard because you don't know all consumers.
- **Debugging and replay** need tooling.
- **Using events for commands:** "SendEmail" is a command to one receiver, not an event; mixing them up makes coupling unclear.

Use events where decoupling really helps and an orchestrator where you need a clear, controlled process.

## 410: When would you use a workflow engine like Temporal or AWS Step Functions instead of hand-written sagas?

Use one when a business process is long-running, has many steps, timers, retries, compensations or human approvals. Writing that by hand means building state tables, timeout jobs, retry logic and recovery after crashes yourself, and getting it right is hard. Workflow engines store the state of each workflow, retry steps with policies, survive crashes, give you timers ("wait 3 days") and show the history of each run. The costs are another platform to run (or pay for), learning its programming model, and, for code-based engines, rules about deterministic workflow code. For a simple two-step flow, a queue and a status column are enough.

## 411: How does durable execution work in tools like Temporal?

You write a workflow as normal code, but the engine records every step's result (activity calls, timers, signals) in an event history. If the worker crashes, another worker re-runs the workflow function from the start, and instead of really calling the activities again, it uses the recorded results from history until it reaches the point where it stopped. This is why workflow code must be **deterministic**: no direct random numbers, current time, or network calls inside the workflow itself; those go into activities or use the SDK's helpers. Activities (side effects) run at least once, so they must be idempotent. Changing workflow code while old runs are in progress needs versioning.

## 412: What race conditions can happen with idempotency keys and how do you handle them?

- **Two identical requests at the same time:** both check, both see no key, both charge. Fix: insert the key first with a unique constraint, in a "processing" state; the second insert fails and that request returns `409` or waits.
- **Same key, different body:** a client bug reuses a key. Store a hash of the request and reject a mismatch with `422`.
- **Crash after the side effect but before saving the result:** the key is stuck in "processing". Use a lock expiry, then on retry check with the downstream system (did the payment happen?) before redoing it, or pass the same idempotency key to the downstream provider so it deduplicates too.
- **Expiry:** keys deleted too early allow late retries to double-process; keep them longer than any client retry window.

## 413: How do you get exactly-once side effects with external systems like email or payments?

You can't get a true atomic transaction with an external system, so you combine techniques:

- **Pass an idempotency key** to the external API if it supports one (Stripe, many payment providers). Then retries are safe on their side.
- **Record intent first:** write "email X for order 42" to your DB with a unique key, then send. If the send succeeds, mark it done. If you crash in between, you might send twice, so decide if that's acceptable.
- **Check before retry:** ask the external system whether the action already happened.
- **Accept at-least-once** for harmless effects (a duplicate notification), and make them rare.
- **Reconcile** periodically with the provider's records.

## 414: How do deduplication windows work, and what are their limits?

Many systems deduplicate messages only within a time window, to keep storage bounded. SQS FIFO deduplicates within 5 minutes using a deduplication ID; a typical consumer might keep processed IDs in Redis for 24 hours. A duplicate that arrives after the window (a retry after a long outage, or a replay from a Kafka topic) is processed again. So:

- Choose the window based on the longest realistic delay, including replays.
- For critical operations, use permanent deduplication in the database (unique constraint on a business key, like `payment_id`).
- Make the operation itself idempotent where possible, so windows are a performance optimization, not the only protection.

## 415: How do you guarantee read-your-writes when reads go to replicas or read models?

- **Route by recency:** after a write, mark the user's session (cookie or token) and read from the primary for a few seconds.
- **Use log positions:** after a write, return the database log position (Postgres LSN, MySQL GTID). On the next read, send it along and only use a replica that has replayed past it; otherwise use the primary. MongoDB causal consistency sessions do this for you.
- **Version tokens for read models:** commands return the aggregate version; queries wait until the projection reaches it, with a timeout.
- **Client-side:** keep the written data locally and merge it into what the server returns.

## 416: What are the trade-offs between leader-based and leaderless replication?

- **Leader-based (single leader):** all writes go to one node, which orders them and replicates them. Simple consistency and no write conflicts. But the leader is a bottleneck for writes and failover takes time and can lose data with async replication. Postgres, MySQL, MongoDB, Kafka partitions.
- **Leaderless:** clients write to several replicas directly and use quorums. No failover needed, high availability for writes, good across data centers. But you need conflict resolution, read repair and anti-entropy, and consistency is weaker. Cassandra, ScyllaDB, Riak.

Choose leader-based when you need simple correctness; leaderless when write availability and multi-DC writes matter most.

## 417: What problems does multi-leader replication bring?

With multi-leader replication, several nodes (often one per region) accept writes and replicate to each other. The big problem is **write conflicts**: two users change the same record in two regions at the same time. Options:

- **Avoid conflicts:** route all writes for a record (or a user) to one home leader.
- **Last write wins:** simple but loses data.
- **Merge:** CRDTs or custom merge logic.
- **Record both versions** and let the app or user resolve.

Other issues: auto-increment IDs clash (use UUIDs), constraints like uniqueness can't be enforced across leaders synchronously, and replication topology (ring, star, all-to-all) affects ordering and failure behavior.

## 418: What are sloppy quorums and hinted handoff?

In a Dynamo-style store, each key has N "home" replicas. If some are unreachable, a strict quorum would reject the write. With a **sloppy quorum**, the write is accepted by other healthy nodes instead, so writes stay available. Those nodes keep a "hint" saying who the data really belongs to, and when the home node comes back, they send it over (**hinted handoff**). The downside: even with `R + W > N`, a read can miss the latest write because the write went to temporary nodes, so you lose the quorum's consistency guarantee until handoff finishes.

## 419: How are Merkle trees used for anti-entropy between replicas?

Replicas can drift apart (missed writes, failed handoffs). Comparing every key between two replicas would be slow. A Merkle tree is a hash tree: leaves are hashes of key ranges, and each parent is the hash of its children. Two replicas compare root hashes; if equal, they're in sync. If not, they compare children and walk down only the branches that differ, until they find the exact ranges to repair. This transfers very little data. Cassandra's repair, DynamoDB and Riak use it, and Git and blockchains use the same structure.

## 420: How do you know when design patterns are being overused?

Signs:

- Interfaces with only one implementation that will never have another.
- Factories that create one type, strategies with one strategy, abstract base classes with one child.
- Many layers that only pass calls through.
- New developers need to open ten files to follow one simple feature.
- Names that describe patterns instead of the domain (`UserManagerFactoryProvider`).

Patterns should solve a real, current problem. It's fine to start with simple code and introduce a pattern when the second or third case appears, and also to remove an abstraction when it no longer earns its place. In an interview, saying when you would not use a pattern shows experience.

## 421: How do you design a public interface or SDK that can evolve for years?

- **Keep the surface small.** Everything public is a promise; you can add later, but removing breaks users.
- **Use options objects** instead of long positional parameters, so you can add options without breaking calls.
- **Return objects, not bare values**, so you can add fields.
- **Hide implementation types**; expose interfaces.
- **Follow semantic versioning** and announce deprecations a release ahead, with warnings and migration guides.
- **Avoid leaking third-party types** in your API, so you can change dependencies.
- **Extension points** (plugins, hooks, middleware) let users add behavior without you adding features to the core.
- **Test the public API** with contract tests and type tests to catch accidental breaking changes.

## 422: In a hexagonal architecture, where do transactions live and how do you test it?

**Transactions** belong in the application layer (use case handler), because a transaction is about a use case: "place order" must save the order and the outbox event together. The domain doesn't know about transactions. The application layer uses a port like a unit of work, and the adapter implements it with the real database transaction.

```ts
class PlaceOrder {
  constructor(private uow: UnitOfWork) {}

  async execute(cmd: PlaceOrderCommand) {
    await this.uow.run(async ({ orders, outbox }) => {
      const order = Order.place(cmd);
      await orders.save(order);
      await outbox.add(order.pullEvents());
    });
  }
}
```

**Testing:**

- Domain: plain unit tests, no mocks needed.
- Use cases: tests with in-memory adapters, fast and focused on behavior.
- Adapters: integration tests against real infrastructure (Testcontainers for databases and brokers).
- A few end-to-end tests through the real HTTP adapter.

## 423: What are the rules of thumb for designing aggregates?

From Vaughn Vernon's guidance:

- **Keep aggregates small.** Big aggregates load too much data and cause concurrency conflicts.
- **Protect true invariants inside the boundary:** only rules that must be consistent immediately belong in one aggregate.
- **Reference other aggregates by ID,** not by object reference.
- **Change one aggregate per transaction;** use domain events and eventual consistency to update others.

Example: `Order` should not contain the full `Customer` object. It holds `customerId`. Updating customer loyalty points after an order happens in a separate transaction triggered by `OrderPlaced`.

## 424: How do you handle concurrent updates to the same aggregate?

Use optimistic concurrency with a version number. Load the aggregate with its version, apply changes, and save with a condition that the version is unchanged, incrementing it.

```ts
const result = await db.order.updateMany({
  where: { id: order.id, version: order.version },
  data: { status: order.status, version: { increment: 1 } },
});

if (result.count === 0)
  throw new ConcurrencyError("Order was changed by someone else");
```

On conflict: retry the whole command (reload, reapply) if it's safe, or return `409 Conflict` and let the user decide. With HTTP, `ETag` and `If-Match` headers carry the version to the client. Frequent conflicts on one aggregate usually mean it is too large or too hot and should be split.

## 425: What are context mapping patterns in DDD?

They describe how bounded contexts (and their teams) relate:

- **Shared Kernel:** two contexts share a small piece of the model; changes need agreement.
- **Customer-Supplier:** the downstream (customer) team's needs influence the upstream (supplier) team's plans.
- **Conformist:** the downstream simply accepts the upstream's model, usually because it has no influence.
- **Anti-Corruption Layer:** the downstream translates the upstream's model to protect its own.
- **Open Host Service + Published Language:** the upstream offers a well-defined API and data format for all consumers.
- **Separate Ways:** no integration at all; duplicate what's needed.

Drawing a context map helps you see dependencies and team politics, which drive many technical decisions.

## 426: What is Event Storming?

Event Storming is a workshop technique, created by Alberto Brandolini, for exploring a business domain. Developers and domain experts put sticky notes on a long wall: orange for domain events (`OrderPlaced`), blue for commands, yellow for actors, pink for problems and questions, and so on, arranged on a timeline. It quickly reveals how the business really works, where the confusion is, and where natural boundaries (bounded contexts and aggregates) are. It is useful before designing services, and works remotely with tools like Miro.

## 427: What is the difference between domain events and integration events?

- **Domain events** are internal to a bounded context or service. They can use internal types, can change freely with the code, and are often handled in the same process and even the same transaction.
- **Integration events** are published to other services through a broker. They are a public contract: stable, versioned, with only the data other services should see, and are sent after the transaction commits (via an outbox).

Don't publish your internal domain events directly to other services; map them to integration events, or every internal refactor becomes a breaking change for others.

## 428: What are architecture fitness functions?

A fitness function is an automated check that an architectural quality still holds, from the book _Building Evolutionary Architectures_. Examples:

- Lint rules or ArchUnit tests that fail if the domain imports the database layer.
- A CI check that the bundle size stays under 200 KB.
- Load tests that fail if p95 latency goes above 300 ms.
- Checks that no service calls another service's database.
- Dependency vulnerability scans.
- Chaos tests that a dependency failure doesn't take down checkout.

They turn architecture decisions into tests, so the architecture doesn't slowly decay as the code changes.

## 429: How do you justify an architecture decision to your team or management?

- **Start with the problem and the goals,** in business terms: cost, speed, risk, user experience.
- **List realistic options,** including "do nothing" and the simplest choice.
- **Compare them against the quality attributes that matter** for this case (a small table works well), including cost to build and run, team skills, and risk.
- **Be honest about trade-offs** and what you are giving up.
- **Use evidence:** load tests, prototypes, numbers from production, experience from similar systems.
- **Propose how to reduce risk:** a pilot, a phased rollout, a way back.
- **Write it down** as an ADR.

Decisions people helped shape are easier to carry out than ones handed down.

## 430: What is the difference between one-way and two-way door decisions?

The terms come from Amazon. A **two-way door** decision can be reversed cheaply: a library choice inside one service, an internal API detail, a feature flag. Make these quickly with small teams. A **one-way door** is expensive or impossible to undo: a primary database for core data, a public API contract, data model choices for event-sourced data, cloud provider lock-in, a big migration. Spend more time on these, get more opinions and prototype. A good architect also tries to turn one-way doors into two-way doors, for example with abstractions at boundaries or a strangler approach.

## 431: What problems do micro frontends cause at scale and how do you handle them?

- **Duplicate dependencies:** each app ships its own React or Angular. Share them with Module Federation singletons, with careful version rules.
- **Version mismatches** of shared libraries break at runtime, not build time. Pin and test shared versions, and keep shared libraries few.
- **Inconsistent UI:** use a shared design system distributed as a versioned package or web components.
- **Cross-app communication:** keep it minimal; use URL state, custom events or a small shared event bus, not a shared global store.
- **Routing:** a shell app owns top-level routes.
- **Performance:** more network requests and JS; monitor Web Vitals per micro frontend.
- **Testing:** contract tests for shared interfaces and end-to-end tests of the composed app.
- **Ownership:** clear owners per micro frontend and a platform team for the shell.

## 432: How would you structure the data layer of a large front-end application?

- **Separate server state from client state.** Server data (lists, details) goes in a cache library like TanStack Query, RTK Query, Apollo, or Angular's `httpResource`, which handles caching, deduplication, background refetch and invalidation. Client state (UI state, forms) stays local or in a small store.
- **Stale-while-revalidate:** show cached data immediately and refresh in the background.
- **Typed API clients** generated from OpenAPI or GraphQL schemas.
- **Normalized cache or clear invalidation keys** so updating one item updates every screen that shows it.
- **Optimistic updates** for common actions.
- **A BFF** that shapes data for the UI, so the front end doesn't stitch together ten calls.
- **Feature-based folders** with each feature owning its queries and components.

## 433: How do you make server-side rendering scale for a high-traffic site?

- **Cache rendered HTML** at the CDN for anonymous users, with short TTLs or `stale-while-revalidate`, and purge by tags when content changes.
- **Separate personalized parts:** render the page shell statically and load personalized pieces on the client, or use edge functions to fill them in.
- **Streaming SSR** (React Suspense, Angular incremental hydration) sends the first bytes fast and fills slower parts later.
- **Static or ISR** for pages that don't change per request.
- **Cache data fetching** on the server, deduplicated per request.
- **Watch CPU:** rendering is CPU-heavy; profile components, and scale horizontally.
- **Timeouts and fallbacks** so a slow API doesn't hold the whole page.

## 434: How do you reduce API latency for users around the world?

- **CDN in front of the API,** with TLS terminated near users and connections reused to the origin.
- **Cache GET responses at the edge** where possible, with `s-maxage` and `stale-while-revalidate`.
- **Regional read replicas** or a globally replicated database for reads, with writes going to a home region.
- **Multi-region deployment** of stateless services, with latency-based routing.
- **Fewer round trips:** batch calls, use a BFF or GraphQL to fetch in one request, HTTP/2 or HTTP/3.
- **Edge functions** for simple logic like auth checks and redirects.
- **Prefetch and optimistic UI** on the client to hide the latency that remains.

## 435: Your system gets slow under load. How do you find the bottleneck?

1. **Check the user-facing symptom** first: which endpoints, what percentiles, since when, and did anything change (deploy, config, traffic pattern)?
2. **Look at traces** of slow requests to see where time goes: app code, DB, a downstream service, or waiting in a queue.
3. **Check resource saturation** (USE method) on each layer: CPU, memory, GC, event loop lag, connection pools, thread pools, DB CPU and locks, network.
4. **Database:** slow query log, `pg_stat_statements`, `EXPLAIN ANALYZE`, lock waits, connection count.
5. **Look for queueing:** a small pool or a single-threaded step can cause everything behind it to wait.
6. **Reproduce** with a load test and profile (flame graphs) to confirm.
7. **Fix the biggest bottleneck, measure again,** and repeat.

Avoid guessing and changing many things at once.

## 436: The database CPU is at 100%. What do you do?

**Short term (stop the bleeding):**

- Find the top queries by total time (`pg_stat_statements`, Performance Insights). Usually one or two queries cause most of the load.
- Kill runaway queries, disable the feature or job causing them with a flag, pause batch jobs.
- Add the missing index if that's the cause (created concurrently).
- Increase caching for hot reads, or scale up the instance if possible.

**Long term:**

- Fix query patterns (N+1, `SELECT *`, missing pagination, expensive ORM queries).
- Move reads to replicas and analytics to a separate store.
- Add query timeouts and connection limits.
- Add load tests and alerts on slow-query growth so it doesn't surprise you again.

## 437: Your Redis cache cluster goes down. What happens and how should the system behave?

If the system isn't prepared, all reads go straight to the database, which may not handle the load, so the database fails too, and the whole site goes down.

A system designed for this:

- Has short timeouts on cache calls and treats cache errors as misses, not as fatal errors.
- Uses a circuit breaker so it stops waiting on a dead cache.
- Limits the load on the database during a cache outage (concurrency limits, request coalescing, load shedding of less important traffic).
- May have a small local in-memory cache for the hottest keys.
- Doesn't store anything in the cache that exists nowhere else (sessions, rate limits), or accepts the impact if it does.
- Warms the cache back gradually when it returns.

Test this with a chaos experiment before it happens for real.

## 438: Customers report duplicate orders. How do you investigate and fix it?

**Investigate:**

- Find duplicate pairs and compare timestamps, request IDs, user agents and traces. Were they two requests from the client (double click, retry after timeout, mobile app retry), or one request processed twice (queue redelivery, worker retry)?

**Fix depending on the cause:**

- **Client side:** disable the button after submit, but don't rely on that alone.
- **Idempotency key** generated by the client per checkout attempt and enforced by the server with a unique constraint.
- **Natural unique constraint,** like one order per cart ID.
- **Idempotent consumers** if a message was processed twice.
- **Clean up** existing duplicates with refunds and notify affected customers.

Add a metric or alert for duplicates so you'll catch it if it returns.

## 439: A message queue backlog keeps growing. What do you do?

1. **Check if consumers are working at all:** errors, crashes, a poison message blocking a partition, a dependency that is down.
2. **Compare rates:** has producing gone up (traffic spike, a bug producing too many messages, a retry loop) or has consuming slowed down (slow DB, slow external API)?
3. **Short term:** scale consumers (up to the partition limit), pause non-essential producers, move poison messages to a DLQ, increase batch sizes.
4. **Check retention** so messages aren't lost before they're processed.
5. **Long term:** optimize the handler, split slow steps into their own queue, add autoscaling based on lag, add alerts on message age rather than just count.

Also check whether old messages are still worth processing; sometimes it's better to skip outdated ones.

## 440: One slow microservice is taking the whole site down. How do you fix it now and prevent it later?

**Now:**

- Use a feature flag or circuit breaker to stop calling the slow service, and show a fallback.
- Lower timeouts on calls to it so callers stop piling up.
- Scale or roll back the slow service if a recent deploy caused it.

**Later:**

- Timeouts and circuit breakers on every remote call.
- Bulkheads: separate connection pools per dependency so one can't use up all threads or sockets.
- Make the dependency optional where possible (graceful degradation) or async.
- Limit retries with budgets.
- Load test with the dependency slowed down (chaos testing).
- Review whether the critical path really needs this service.

## 441: How would you migrate from MySQL to PostgreSQL without downtime?

1. **Create the schema** in Postgres and check type differences (e.g. MySQL `TINYINT(1)` vs boolean, collations, `AUTO_INCREMENT` vs identity, case sensitivity).
2. **Initial copy** of the data with a migration tool.
3. **Keep in sync** with CDC (Debezium, AWS DMS) from the MySQL binlog to Postgres.
4. **Verify** with row counts and checksums, and run shadow reads: read from both and compare results, logging differences.
5. **Make the app support both** behind a flag (a repository layer helps a lot here).
6. **Switch reads** gradually to Postgres.
7. **Cutover writes:** a short write freeze or a carefully planned switch, then reverse the CDC direction (Postgres to MySQL) so you can roll back.
8. **Decommission** MySQL after a safe period.

Practice the cutover on a staging copy first.

## 442: How would you prepare a system for a flash sale with 10x normal traffic?

- **Load test** at 10-20x with realistic traffic to find bottlenecks before the day.
- **Pre-scale** servers, databases and queues; don't rely only on autoscaling, which may be too slow. Check cloud quotas.
- **Cache aggressively:** product pages and static content on the CDN; stock shown from cache.
- **Protect the critical path:** inventory decrements atomic and fast, possibly in Redis; orders processed via a queue.
- **Virtual waiting room** to admit users at a controlled rate.
- **Rate limits and bot protection,** since bots often make up a big share of flash sale traffic.
- **Turn off non-essential features** (recommendations, heavy analytics) with flags.
- **Freeze deploys,** have a war room, dashboards and runbooks ready.
- **Tell third parties** (payment provider) about the expected load.

## 443: A third-party API your product depends on is down for hours. How should your system handle it?

- **Detect it fast:** metrics on error rate and latency for each external dependency, with alerts.
- **Circuit breaker** so you stop hammering it and fail fast.
- **Queue the work** that can wait (sending emails, syncing data) and process it when the API comes back, with idempotency so nothing is done twice.
- **Fallbacks:** a secondary provider (another payment or SMS provider), cached data, or a degraded feature.
- **Clear user messages** instead of generic errors.
- **Avoid a thundering herd** on recovery: drain the backlog at a controlled rate within the provider's rate limits.

Afterwards, review whether this dependency needs a backup provider and whether the contract or SLA with the vendor is good enough.

## 444: Data between two services has become inconsistent. How do you deal with it?

- **Find the cause:** lost events (dual-write problem without outbox), failed consumers, messages in a DLQ, out-of-order processing, a bug, or manual DB changes.
- **Fix the cause first,** for example add an outbox, idempotent consumers, or version checks.
- **Repair the data:** replay events from the broker or event store, or run a reconciliation job that compares both sides and fixes differences, with the owning service as the source of truth.
- **Add continuous reconciliation:** a scheduled job that compares counts or checksums and alerts on drift.
- **Make the drift visible** with metrics.

In distributed systems some drift will happen, so reconciliation is part of the design, not just an emergency tool.

## 445: A deploy caused errors and included a database migration. How do you roll back?

If migrations follow expand and contract, the previous app version still works with the new schema, so you just roll back the code (redeploy the old version or switch traffic back). That is why destructive changes (drop column, rename) must only happen in a later release, after the code that needs them is gone.

If the migration was destructive or incompatible:

- Rolling back the schema may lose data written since the deploy, so a "roll forward" fix is often safer.
- Restore from backup or point-in-time recovery only as a last resort, since it loses recent writes.

Prevent this with: backward-compatible migrations, deploying migrations separately from code, canary releases, feature flags to switch off new code paths, and testing migrations on a production-sized copy.

## 446: How would you plan for a full region outage?

- **Define goals:** RTO and RPO per service. Not every service needs the same level.
- **Pick a strategy:** backup and restore (cheap, slow), pilot light (minimal infrastructure ready), warm standby (scaled down but running), or active-active (expensive, fastest).
- **Replicate data** to the other region: database cross-region replicas, object storage replication, backups copied across regions.
- **Avoid hidden single-region dependencies:** DNS, identity provider, secret manager, CI/CD, container registry and monitoring must also work.
- **Automate failover** with runbooks and infrastructure as code so the second region can be brought up quickly.
- **Plan DNS/traffic switching** and its TTLs.
- **Test it regularly** with real failover drills. Untested failover plans usually fail.

## 447: A startup asks whether to begin with a monolith or microservices. What do you recommend?

Usually a **well-structured monolith** (modular monolith). Reasons:

- A small team moves much faster with one codebase, one deploy and one database.
- The domain is still changing; it's hard to know the right service boundaries early, and wrong boundaries in microservices are expensive to fix.
- Microservices need DevOps, observability and distributed systems skills the team may not have time for.
- Most startups never reach the scale where a monolith can't handle the load; a monolith on a few servers with a good database and caching handles a lot.

Keep clean module boundaries so parts can be extracted later. Exceptions: a component with very different scaling or tech needs (video processing, ML inference) can be its own service from the start.

## 448: You're asked to cut cloud costs by 40%. Where do you start?

1. **Get visibility:** break down the bill by service, team and environment using tags and cost tools. Usually a few items make up most of the cost.
2. **Quick wins:** delete unused resources (old snapshots, idle load balancers, unattached disks, forgotten environments), shut down non-production at night, right-size oversized instances and databases.
3. **Pricing:** savings plans or reserved instances for steady load, spot instances for batch and CI workloads.
4. **Data transfer:** reduce cross-zone and cross-region traffic, use a CDN, keep chatty services in the same zone.
5. **Storage:** lifecycle rules to cheaper tiers, cut log retention and verbosity, reduce metric cardinality.
6. **Architecture:** cache to reduce database size, scale to zero where possible, replace expensive managed services if the team can run cheaper ones well.

Track cost per request or per customer, so savings don't disappear as you grow.

## 449: You inherit a legacy system with no tests and need to add features. How do you approach it?

- **Understand before changing:** read the code paths you need, talk to people who know it, use logs and traces to see what's actually used.
- **Add characterization tests:** tests that record what the system currently does (even if it looks wrong) around the area you'll change, so you notice unintended changes.
- **Find seams** (places where you can swap behavior without editing much code) to add tests, like wrapping a hard dependency behind an interface. Michael Feathers' _Working Effectively with Legacy Code_ is the standard reference.
- **Make small, safe refactors** only where you're working ("leave it better than you found it").
- **Put new features in new, clean code** next to the old, and connect them through an adapter or the strangler approach.
- **Add monitoring** so problems in production are found fast.

Avoid the big rewrite unless there is a very strong reason; rewrites usually take much longer than planned and lose hidden behavior.

## 450: What questions do you ask when reviewing an architecture proposal?

- **Problem:** what problem does this solve, and for whom? What happens if we don't do it?
- **Requirements:** what scale, latency, availability and consistency are needed, with numbers?
- **Alternatives:** what simpler options were considered, and why were they rejected?
- **Data:** who owns which data, how does it flow, how is it kept consistent, how is it migrated?
- **Failure:** what happens when each dependency is slow or down? What's the blast radius?
- **Operations:** how is it deployed, monitored, debugged and scaled? Who is on call?
- **Security:** how are authentication, authorization, secrets and personal data handled?
- **Cost:** what does it cost to build and to run, now and at 10x?
- **Team:** does the team have the skills, and does it fit team boundaries?
- **Reversibility:** which parts are hard to undo, and how will we roll out and roll back?

A good review is about making the trade-offs clear, not about finding the "right" answer.
