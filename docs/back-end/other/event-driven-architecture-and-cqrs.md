# Event-Driven Architecture and CQRS Interview Questions and Answers

_Last updated: November 19, 2026_

450 interview questions with answers about event-driven architecture, CQRS and event sourcing, split into three levels: 150 easy, 150 moderate and 150 advanced.

These are patterns, not one product, so the answers are not tied to a version. Code examples use TypeScript on Node.js, with PostgreSQL where a database is needed. When a specific tool matters, the answers name it: Apache Kafka, RabbitMQ, AWS SQS, SNS and EventBridge, KurrentDB (formerly EventStoreDB), Marten, Axon and the NestJS CQRS module.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is event-driven architecture?](#1-what-is-event-driven-architecture)
- [2: What is an event?](#2-what-is-an-event)
- [3: What is the difference between an event, a command and a message?](#3-what-is-the-difference-between-an-event-a-command-and-a-message)
- [4: What is an event producer?](#4-what-is-an-event-producer)
- [5: What is an event consumer?](#5-what-is-an-event-consumer)
- [6: What is an event broker?](#6-what-is-an-event-broker)
- [7: Why would a team choose an event-driven architecture?](#7-why-would-a-team-choose-an-event-driven-architecture)
- [8: What are the downsides of event-driven architecture?](#8-what-are-the-downsides-of-event-driven-architecture)
- [9: What does loose coupling mean in an event-driven system?](#9-what-does-loose-coupling-mean-in-an-event-driven-system)
- [10: What is the difference between synchronous and asynchronous communication?](#10-what-is-the-difference-between-synchronous-and-asynchronous-communication)
- [11: What is the publish/subscribe pattern?](#11-what-is-the-publishsubscribe-pattern)
- [12: What is the difference between a queue and pub/sub?](#12-what-is-the-difference-between-a-queue-and-pubsub)
- [13: What is a topic?](#13-what-is-a-topic)
- [14: What is the event notification pattern?](#14-what-is-the-event-notification-pattern)
- [15: What is event-carried state transfer?](#15-what-is-event-carried-state-transfer)
- [16: What is event sourcing?](#16-what-is-event-sourcing)
- [17: What is CQRS?](#17-what-is-cqrs)
- [18: Why would you separate reads from writes?](#18-why-would-you-separate-reads-from-writes)
- [19: What is a command in CQRS?](#19-what-is-a-command-in-cqrs)
- [20: What is a query in CQRS?](#20-what-is-a-query-in-cqrs)
- [21: What is a command handler?](#21-what-is-a-command-handler)
- [22: What is a query handler?](#22-what-is-a-query-handler)
- [23: What is the write model?](#23-what-is-the-write-model)
- [24: What is the read model?](#24-what-is-the-read-model)
- [25: What is a projection?](#25-what-is-a-projection)
- [26: What is eventual consistency?](#26-what-is-eventual-consistency)
- [27: Are CQRS and event sourcing the same thing?](#27-are-cqrs-and-event-sourcing-the-same-thing)
- [28: Can you use CQRS without event sourcing?](#28-can-you-use-cqrs-without-event-sourcing)
- [29: What is CQS, and how is CQRS related to it?](#29-what-is-cqs-and-how-is-cqrs-related-to-it)
- [30: Why are events named in the past tense?](#30-why-are-events-named-in-the-past-tense)
- [31: What does a typical event look like?](#31-what-does-a-typical-event-look-like)
- [32: Why should events be immutable?](#32-why-should-events-be-immutable)
- [33: What is an event store?](#33-what-is-an-event-store)
- [34: What is an aggregate?](#34-what-is-an-aggregate)
- [35: What is the difference between a domain event and an integration event?](#35-what-is-the-difference-between-a-domain-event-and-an-integration-event)
- [36: What is a message queue?](#36-what-is-a-message-queue)
- [37: When should you not use an event-driven architecture?](#37-when-should-you-not-use-an-event-driven-architecture)
- [38: When should you not use CQRS?](#38-when-should-you-not-use-cqrs)
- [39: What is an event bus?](#39-what-is-an-event-bus)
- [40: How does Node's EventEmitter relate to event-driven design?](#40-how-does-nodes-eventemitter-relate-to-event-driven-design)
- [41: What is fan-out?](#41-what-is-fan-out)
- [42: What is an event schema?](#42-what-is-an-event-schema)
- [43: What formats are commonly used for events?](#43-what-formats-are-commonly-used-for-events)
- [44: What is a dead letter queue?](#44-what-is-a-dead-letter-queue)
- [45: Why do consumers retry failed events?](#45-why-do-consumers-retry-failed-events)
- [46: What are at-most-once, at-least-once and exactly-once delivery?](#46-what-are-at-most-once-at-least-once-and-exactly-once-delivery)
- [47: What is idempotency?](#47-what-is-idempotency)
- [48: Why must event consumers be idempotent?](#48-why-must-event-consumers-be-idempotent)
- [49: What is message acknowledgment?](#49-what-is-message-acknowledgment)
- [50: Why does message ordering matter?](#50-why-does-message-ordering-matter)
- [51: What is a partition in Kafka, and why does it matter for events?](#51-what-is-a-partition-in-kafka-and-why-does-it-matter-for-events)
- [52: What is a consumer group?](#52-what-is-a-consumer-group)
- [53: Is a webhook event-driven?](#53-is-a-webhook-event-driven)
- [54: How is event-driven communication different from request-response?](#54-how-is-event-driven-communication-different-from-request-response)
- [55: What is choreography?](#55-what-is-choreography)
- [56: What is orchestration?](#56-what-is-orchestration)
- [57: What is a saga?](#57-what-is-a-saga)
- [58: What is a compensating action?](#58-what-is-a-compensating-action)
- [59: What is the transactional outbox pattern?](#59-what-is-the-transactional-outbox-pattern)
- [60: What is change data capture?](#60-what-is-change-data-capture)
- [61: What is a materialized view?](#61-what-is-a-materialized-view)
- [62: Where can a read model be stored?](#62-where-can-a-read-model-be-stored)
- [63: Why might a user see old data after making a change in a CQRS system?](#63-why-might-a-user-see-old-data-after-making-a-change-in-a-cqrs-system)
- [64: What is an event handler?](#64-what-is-an-event-handler)
- [65: What is event replay?](#65-what-is-event-replay)
- [66: What is a snapshot in event sourcing?](#66-what-is-a-snapshot-in-event-sourcing)
- [67: What is event versioning?](#67-what-is-event-versioning)
- [68: What is a stream in event sourcing?](#68-what-is-a-stream-in-event-sourcing)
- [69: What is an append-only log?](#69-what-is-an-append-only-log)
- [70: What is a correlation id?](#70-what-is-a-correlation-id)
- [71: What is a causation id?](#71-what-is-a-causation-id)
- [72: What are the benefits of event sourcing?](#72-what-are-the-benefits-of-event-sourcing)
- [73: What are the downsides of event sourcing?](#73-what-are-the-downsides-of-event-sourcing)
- [74: What is domain-driven design, and how does it relate to CQRS?](#74-what-is-domain-driven-design-and-how-does-it-relate-to-cqrs)
- [75: What is a bounded context?](#75-what-is-a-bounded-context)
- [76: Why does it help to name events with business language?](#76-why-does-it-help-to-name-events-with-business-language)
- [77: What is the mediator pattern in CQRS code?](#77-what-is-the-mediator-pattern-in-cqrs-code)
- [78: What does the NestJS CQRS module provide?](#78-what-does-the-nestjs-cqrs-module-provide)
- [79: What is a command bus?](#79-what-is-a-command-bus)
- [80: What is a query bus?](#80-what-is-a-query-bus)
- [81: Can a command return a value?](#81-can-a-command-return-a-value)
- [82: Should a query ever change state?](#82-should-a-query-ever-change-state)
- [83: Where should you validate a command?](#83-where-should-you-validate-a-command)
- [84: What is backpressure?](#84-what-is-backpressure)
- [85: What is consumer lag?](#85-what-is-consumer-lag)
- [86: What is a poison message?](#86-what-is-a-poison-message)
- [87: What is message TTL?](#87-what-is-message-ttl)
- [88: What is a durable subscription?](#88-what-is-a-durable-subscription)
- [89: What is the difference between push and pull consumers?](#89-what-is-the-difference-between-push-and-pull-consumers)
- [90: What is the difference between event streaming and messaging?](#90-what-is-the-difference-between-event-streaming-and-messaging)
- [91: What is an event-driven microservice?](#91-what-is-an-event-driven-microservice)
- [92: Can a monolith be event-driven?](#92-can-a-monolith-be-event-driven)
- [93: How do serverless platforms support event-driven architecture?](#93-how-do-serverless-platforms-support-event-driven-architecture)
- [94: What is Amazon EventBridge?](#94-what-is-amazon-eventbridge)
- [95: How does the SNS and SQS fan-out pattern work?](#95-how-does-the-sns-and-sqs-fan-out-pattern-work)
- [96: What is AsyncAPI?](#96-what-is-asyncapi)
- [97: What is CloudEvents?](#97-what-is-cloudevents)
- [98: What is the difference between event time and processing time?](#98-what-is-the-difference-between-event-time-and-processing-time)
- [99: How do you test a simple event handler?](#99-how-do-you-test-a-simple-event-handler)
- [100: Is a database read replica the same as a CQRS read model?](#100-is-a-database-read-replica-the-same-as-a-cqrs-read-model)
- [101: What is the difference between a background job and an event?](#101-what-is-the-difference-between-a-background-job-and-an-event)
- [102: What does fire and forget mean?](#102-what-does-fire-and-forget-mean)
- [103: What happens to events when a consumer is down?](#103-what-happens-to-events-when-a-consumer-is-down)
- [104: What is message durability?](#104-what-is-message-durability)
- [105: What is a policy (or reactor) in event-driven design?](#105-what-is-a-policy-or-reactor-in-event-driven-design)
- [106: What is temporal coupling?](#106-what-is-temporal-coupling)
- [107: How can a UI see read model changes without refreshing?](#107-how-can-a-ui-see-read-model-changes-without-refreshing)
- [108: What is event storming?](#108-what-is-event-storming)
- [109: What is a process manager?](#109-what-is-a-process-manager)
- [110: What happens when a command is rejected?](#110-what-happens-when-a-command-is-rejected)
- [111: What is optimistic concurrency?](#111-what-is-optimistic-concurrency)
- [112: What is an expected version in event sourcing?](#112-what-is-an-expected-version-in-event-sourcing)
- [113: Does CQRS require two databases?](#113-does-cqrs-require-two-databases)
- [114: What does it mean to rebuild a read model?](#114-what-does-it-mean-to-rebuild-a-read-model)
- [115: Why have one read model per screen or use case?](#115-why-have-one-read-model-per-screen-or-use-case)
- [116: What is the difference between a thin event and a fat event?](#116-what-is-the-difference-between-a-thin-event-and-a-fat-event)
- [117: Why should events be kept reasonably small?](#117-why-should-events-be-kept-reasonably-small)
- [118: What is a schema registry?](#118-what-is-a-schema-registry)
- [119: What does backward compatibility mean for events?](#119-what-does-backward-compatibility-mean-for-events)
- [120: What is a message key?](#120-what-is-a-message-key)
- [121: What is a delayed message?](#121-what-is-a-delayed-message)
- [122: How do events help with auditing?](#122-how-do-events-help-with-auditing)
- [123: What is distributed tracing, and why is it useful in event-driven systems?](#123-what-is-distributed-tracing-and-why-is-it-useful-in-event-driven-systems)
- [124: What is a long-running process?](#124-what-is-a-long-running-process)
- [125: What is the inbox pattern?](#125-what-is-the-inbox-pattern)
- [126: What is message deduplication?](#126-what-is-message-deduplication)
- [127: What is the difference between a queue and a log?](#127-what-is-the-difference-between-a-queue-and-a-log)
- [128: Can you replay events in Kafka and RabbitMQ?](#128-can-you-replay-events-in-kafka-and-rabbitmq)
- [129: Give examples of events in an e-commerce system.](#129-give-examples-of-events-in-an-e-commerce-system)
- [130: What are common beginner mistakes with events and CQRS?](#130-what-are-common-beginner-mistakes-with-events-and-cqrs)
- [131: How should commands be named?](#131-how-should-commands-be-named)
- [132: What are message headers used for?](#132-what-are-message-headers-used-for)
- [133: What is content-based filtering?](#133-what-is-content-based-filtering)
- [134: What is a routing key in RabbitMQ?](#134-what-is-a-routing-key-in-rabbitmq)
- [135: What are competing consumers?](#135-what-are-competing-consumers)
- [136: Why do brokers keep copies of data on several servers?](#136-why-do-brokers-keep-copies-of-data-on-several-servers)
- [137: How do you handle a deadline in an event-driven process?](#137-how-do-you-handle-a-deadline-in-an-event-driven-process)
- [138: Can you send commands through a broker?](#138-can-you-send-commands-through-a-broker)
- [139: Why does every event need a unique id?](#139-why-does-every-event-need-a-unique-id)
- [140: How is event-driven processing different from batch processing?](#140-how-is-event-driven-processing-different-from-batch-processing)
- [141: What is an offset in Kafka?](#141-what-is-an-offset-in-kafka)
- [142: What is the visibility timeout in Amazon SQS?](#142-what-is-the-visibility-timeout-in-amazon-sqs)
- [143: What is the difference between strong and eventual consistency?](#143-what-is-the-difference-between-strong-and-eventual-consistency)
- [144: What does "source of truth" mean in an event-sourced system?](#144-what-does-source-of-truth-mean-in-an-event-sourced-system)
- [145: How is CQRS different from a standard CRUD design?](#145-how-is-cqrs-different-from-a-standard-crud-design)
- [146: What is event retention?](#146-what-is-event-retention)
- [147: What should happen if an event handler fails halfway?](#147-what-should-happen-if-an-event-handler-fails-halfway)
- [148: Why is sharing one database between services a problem, and how do events help?](#148-why-is-sharing-one-database-between-services-a-problem-and-how-do-events-help)
- [149: How can an order status be driven by events?](#149-how-can-an-order-status-be-driven-by-events)
- [150: How would you explain CQRS to a non-technical person?](#150-how-would-you-explain-cqrs-to-a-non-technical-person)

### Moderate Questions (151-300)

- [151: What is the dual write problem?](#151-what-is-the-dual-write-problem)
- [152: How do you implement the transactional outbox in PostgreSQL?](#152-how-do-you-implement-the-transactional-outbox-in-postgresql)
- [153: How does an outbox relay work, and what are the options?](#153-how-does-an-outbox-relay-work-and-what-are-the-options)
- [154: How do you write a simple polling outbox relay?](#154-how-do-you-write-a-simple-polling-outbox-relay)
- [155: How do you make a consumer idempotent with a processed-messages table?](#155-how-do-you-make-a-consumer-idempotent-with-a-processed-messages-table)
- [156: How do idempotency keys work for commands sent over HTTP?](#156-how-do-idempotency-keys-work-for-commands-sent-over-http)
- [157: How do you implement retries with exponential backoff and jitter?](#157-how-do-you-implement-retries-with-exponential-backoff-and-jitter)
- [158: How should you handle messages in a dead letter queue?](#158-how-should-you-handle-messages-in-a-dead-letter-queue)
- [159: How do you keep events for the same entity in order?](#159-how-do-you-keep-events-for-the-same-entity-in-order)
- [160: How do you handle events that arrive out of order?](#160-how-do-you-handle-events-that-arrive-out-of-order)
- [161: How do you design an event envelope?](#161-how-do-you-design-an-event-envelope)
- [162: What strategies exist for versioning events?](#162-what-strategies-exist-for-versioning-events)
- [163: What is upcasting?](#163-what-is-upcasting)
- [164: How do Avro compatibility rules affect event changes?](#164-how-do-avro-compatibility-rules-affect-event-changes)
- [165: How do you choose between event notification and event-carried state transfer?](#165-how-do-you-choose-between-event-notification-and-event-carried-state-transfer)
- [166: How do you write a projection that updates a read model?](#166-how-do-you-write-a-projection-that-updates-a-read-model)
- [167: How does a projection know where it stopped?](#167-how-does-a-projection-know-where-it-stopped)
- [168: How do you rebuild a read model without downtime?](#168-how-do-you-rebuild-a-read-model-without-downtime)
- [169: What is read-your-own-writes, and how do you get it in CQRS?](#169-what-is-read-your-own-writes-and-how-do-you-get-it-in-cqrs)
- [170: How do you handle eventual consistency in the UI?](#170-how-do-you-handle-eventual-consistency-in-the-ui)
- [171: What is the difference between command validation and domain invariants?](#171-what-is-the-difference-between-command-validation-and-domain-invariants)
- [172: How big should an aggregate be?](#172-how-big-should-an-aggregate-be)
- [173: How do you implement an event-sourced aggregate in TypeScript?](#173-how-do-you-implement-an-event-sourced-aggregate-in-typescript)
- [174: How do you load an event-sourced aggregate?](#174-how-do-you-load-an-event-sourced-aggregate)
- [175: How do you save events with optimistic concurrency in PostgreSQL?](#175-how-do-you-save-events-with-optimistic-concurrency-in-postgresql)
- [176: When should you use snapshots?](#176-when-should-you-use-snapshots)
- [177: How does a choreography-based saga work for an order?](#177-how-does-a-choreography-based-saga-work-for-an-order)
- [178: How do you build an orchestrated saga?](#178-how-do-you-build-an-orchestrated-saga)
- [179: Is a compensating action always an exact undo?](#179-is-a-compensating-action-always-an-exact-undo)
- [180: What is the difference between a process manager and a choreographed saga?](#180-what-is-the-difference-between-a-process-manager-and-a-choreographed-saga)
- [181: How do you handle timeouts in a saga?](#181-how-do-you-handle-timeouts-in-a-saga)
- [182: How do you write a command handler with NestJS CQRS?](#182-how-do-you-write-a-command-handler-with-nestjs-cqrs)
- [183: How do sagas work in the NestJS CQRS module?](#183-how-do-sagas-work-in-the-nestjs-cqrs-module)
- [184: How do you write a query handler with NestJS CQRS?](#184-how-do-you-write-a-query-handler-with-nestjs-cqrs)
- [185: How do event handlers work in NestJS CQRS?](#185-how-do-event-handlers-work-in-nestjs-cqrs)
- [186: How does Kafka consumer group rebalancing affect event processing?](#186-how-does-kafka-consumer-group-rebalancing-affect-event-processing)
- [187: Why should you commit Kafka offsets only after processing?](#187-why-should-you-commit-kafka-offsets-only-after-processing)
- [188: How do you publish events with a RabbitMQ topic exchange?](#188-how-do-you-publish-events-with-a-rabbitmq-topic-exchange)
- [189: How do SQS FIFO queues help with ordering?](#189-how-do-sqs-fifo-queues-help-with-ordering)
- [190: How do EventBridge rules match events?](#190-how-do-eventbridge-rules-match-events)
- [191: How do you choose between Kafka, RabbitMQ and SQS?](#191-how-do-you-choose-between-kafka-rabbitmq-and-sqs)
- [192: How do you test an event-sourced aggregate?](#192-how-do-you-test-an-event-sourced-aggregate)
- [193: What is contract testing for events?](#193-what-is-contract-testing-for-events)
- [194: How do you integration test event flows?](#194-how-do-you-integration-test-event-flows)
- [195: How do you pass trace context through a broker?](#195-how-do-you-pass-trace-context-through-a-broker)
- [196: How should you log in an event-driven system?](#196-how-should-you-log-in-an-event-driven-system)
- [197: What metrics should you watch for event consumers?](#197-what-metrics-should-you-watch-for-event-consumers)
- [198: How do you tell transient errors from permanent ones?](#198-how-do-you-tell-transient-errors-from-permanent-ones)
- [199: How do retry topics work in Kafka?](#199-how-do-retry-topics-work-in-kafka)
- [200: How do you turn domain events into integration events?](#200-how-do-you-turn-domain-events-into-integration-events)
- [201: What is an anti-corruption layer for events?](#201-what-is-an-anti-corruption-layer-for-events)
- [202: How fine-grained should events be?](#202-how-fine-grained-should-events-be)
- [203: Why are CRUD-style events like EntityUpdated considered an anti-pattern?](#203-why-are-crud-style-events-like-entityupdated-considered-an-anti-pattern)
- [204: What naming conventions work well for events and topics?](#204-what-naming-conventions-work-well-for-events-and-topics)
- [205: Where should event schemas live?](#205-where-should-event-schemas-live)
- [206: What is the risk of a shared library for event classes?](#206-what-is-the-risk-of-a-shared-library-for-event-classes)
- [207: Can you have several read models for the same events?](#207-can-you-have-several-read-models-for-the-same-events)
- [208: How do you choose a store for a read model?](#208-how-do-you-choose-a-store-for-a-read-model)
- [209: How can PostgreSQL materialized views be used as a simple form of CQRS?](#209-how-can-postgresql-materialized-views-be-used-as-a-simple-form-of-cqrs)
- [210: What are the trade-offs of updating the read model in the same transaction as the write?](#210-what-are-the-trade-offs-of-updating-the-read-model-in-the-same-transaction-as-the-write)
- [211: What is the difference between inline and async projections?](#211-what-is-the-difference-between-inline-and-async-projections)
- [212: How do you handle the right to be forgotten in an event-sourced system?](#212-how-do-you-handle-the-right-to-be-forgotten-in-an-event-sourced-system)
- [213: What options exist for an event store?](#213-what-options-exist-for-an-event-store)
- [214: How do you read events by stream and by global position?](#214-how-do-you-read-events-by-stream-and-by-global-position)
- [215: What are catch-up and persistent subscriptions?](#215-what-are-catch-up-and-persistent-subscriptions)
- [216: How should a command API look in REST?](#216-how-should-a-command-api-look-in-rest)
- [217: When should an API return 202 Accepted?](#217-when-should-an-api-return-202-accepted)
- [218: How does a client learn the result of an async command?](#218-how-does-a-client-learn-the-result-of-an-async-command)
- [219: How does request-reply work over a message broker?](#219-how-does-request-reply-work-over-a-message-broker)
- [220: What is the claim check pattern?](#220-what-is-the-claim-check-pattern)
- [221: How does a service keep a local copy of another service's data?](#221-how-does-a-service-keep-a-local-copy-of-another-services-data)
- [222: What does it mean that one service owns the data?](#222-what-does-it-mean-that-one-service-owns-the-data)
- [223: How do you answer a query that needs data from several services?](#223-how-do-you-answer-a-query-that-needs-data-from-several-services)
- [224: How do you control how many messages a consumer handles at once?](#224-how-do-you-control-how-many-messages-a-consumer-handles-at-once)
- [225: What is the trade-off between consumer concurrency and ordering?](#225-what-is-the-trade-off-between-consumer-concurrency-and-ordering)
- [226: When should a consumer process events in batches?](#226-when-should-a-consumer-process-events-in-batches)
- [227: Why should handlers use the event's timestamp instead of the current time?](#227-why-should-handlers-use-the-events-timestamp-instead-of-the-current-time)
- [228: Why must projections be free of side effects?](#228-why-must-projections-be-free-of-side-effects)
- [229: How do you avoid repeating side effects when replaying events?](#229-how-do-you-avoid-repeating-side-effects-when-replaying-events)
- [230: How can a new service get historical data when it starts?](#230-how-can-a-new-service-get-historical-data-when-it-starts)
- [231: What is Kafka log compaction, and when is it useful?](#231-what-is-kafka-log-compaction-and-when-is-it-useful)
- [232: How does retention affect your design?](#232-how-does-retention-affect-your-design)
- [233: How do you secure who can send commands and publish events?](#233-how-do-you-secure-who-can-send-commands-and-publish-events)
- [234: How can you protect sensitive data inside events?](#234-how-can-you-protect-sensitive-data-inside-events)
- [235: What should you keep in mind about personal data in events?](#235-what-should-you-keep-in-mind-about-personal-data-in-events)
- [236: How do you validate events when consuming them?](#236-how-do-you-validate-events-when-consuming-them)
- [237: What should a consumer do with event types it doesn't know?](#237-what-should-a-consumer-do-with-event-types-it-doesnt-know)
- [238: What is the tolerant reader pattern?](#238-what-is-the-tolerant-reader-pattern)
- [239: What is the difference between producer-driven and consumer-driven contracts?](#239-what-is-the-difference-between-producer-driven-and-consumer-driven-contracts)
- [240: How do you move an existing CRUD application to CQRS step by step?](#240-how-do-you-move-an-existing-crud-application-to-cqrs-step-by-step)
- [241: How can events help when replacing a legacy system?](#241-how-can-events-help-when-replacing-a-legacy-system)
- [242: What are the pitfalls of using CDC to produce domain events?](#242-what-are-the-pitfalls-of-using-cdc-to-produce-domain-events)
- [243: In what order should you deploy producers and consumers when an event changes?](#243-in-what-order-should-you-deploy-producers-and-consumers-when-an-event-changes)
- [244: What happens to events if the broker is down?](#244-what-happens-to-events-if-the-broker-is-down)
- [245: What does Kafka's exactly-once support actually cover?](#245-what-does-kafkas-exactly-once-support-actually-cover)
- [246: What does "effectively once" mean?](#246-what-does-effectively-once-mean)
- [247: When would you use locks instead of optimistic concurrency in command handling?](#247-when-would-you-use-locks-instead-of-optimistic-concurrency-in-command-handling)
- [248: How do you enforce uniqueness, like a unique email, in an event-sourced system?](#248-how-do-you-enforce-uniqueness-like-a-unique-email-in-an-event-sourced-system)
- [249: What is the problem with validating commands against the read model?](#249-what-is-the-problem-with-validating-commands-against-the-read-model)
- [250: How do you handle a command that needs to change several aggregates?](#250-how-do-you-handle-a-command-that-needs-to-change-several-aggregates)
- [251: What is a domain service, and when do you need one in the write model?](#251-what-is-a-domain-service-and-when-do-you-need-one-in-the-write-model)
- [252: What is event enrichment?](#252-what-is-event-enrichment)
- [253: Should you put a cache in front of a read model?](#253-should-you-put-a-cache-in-front-of-a-read-model)
- [254: How do you paginate a read model correctly?](#254-how-do-you-paginate-a-read-model-correctly)
- [255: What should a projection do when it fails on an event?](#255-what-should-a-projection-do-when-it-fails-on-an-event)
- [256: How do you know how far behind a projection is?](#256-how-do-you-know-how-far-behind-a-projection-is)
- [257: How do you add logging or validation around every command handler?](#257-how-do-you-add-logging-or-validation-around-every-command-handler)
- [258: Why should domain events be published only after the transaction commits?](#258-why-should-domain-events-be-published-only-after-the-transaction-commits)
- [259: How do entities raise domain events in code?](#259-how-do-entities-raise-domain-events-in-code)
- [260: Should in-process event handlers run before or after the transaction commits?](#260-should-in-process-event-handlers-run-before-or-after-the-transaction-commits)
- [261: How do you keep correlation ids across a saga?](#261-how-do-you-keep-correlation-ids-across-a-saga)
- [262: How do you handle partial batch failures with Lambda and SQS?](#262-how-do-you-handle-partial-batch-failures-with-lambda-and-sqs)
- [263: How can you make a Lambda consumer idempotent?](#263-how-can-you-make-a-lambda-consumer-idempotent)
- [264: How do you push read model updates to the browser with SSE?](#264-how-do-you-push-read-model-updates-to-the-browser-with-sse)
- [265: What are schema registry compatibility modes?](#265-what-are-schema-registry-compatibility-modes)
- [266: How do you describe an event in AsyncAPI?](#266-how-do-you-describe-an-event-in-asyncapi)
- [267: What does an event in CloudEvents format look like?](#267-what-does-an-event-in-cloudevents-format-look-like)
- [268: How can business events be used for analytics?](#268-how-can-business-events-be-used-for-analytics)
- [269: How do you debug a flow where "nothing happened" after an event?](#269-how-do-you-debug-a-flow-where-nothing-happened-after-an-event)
- [270: What is a hot partition?](#270-what-is-a-hot-partition)
- [271: How do you choose the number of partitions for a topic?](#271-how-do-you-choose-the-number-of-partitions-for-a-topic)
- [272: What do you do when a consumer is too slow?](#272-what-do-you-do-when-a-consumer-is-too-slow)
- [273: How do you find the state of an aggregate at a point in the past?](#273-how-do-you-find-the-state-of-an-aggregate-at-a-point-in-the-past)
- [274: How do you correct a mistake in an event-sourced system?](#274-how-do-you-correct-a-mistake-in-an-event-sourced-system)
- [275: What is the "closing the books" pattern?](#275-what-is-the-closing-the-books-pattern)
- [276: How can you apply CQRS inside one service with one database?](#276-how-can-you-apply-cqrs-inside-one-service-with-one-database)
- [277: How does CQRS relate to GraphQL?](#277-how-does-cqrs-relate-to-graphql)
- [278: Who should own events and topics in a team setup?](#278-who-should-own-events-and-topics-in-a-team-setup)
- [279: How do you document which services publish and consume which events?](#279-how-do-you-document-which-services-publish-and-consume-which-events)
- [280: What would you check when reviewing an event handler in a pull request?](#280-what-would-you-check-when-reviewing-an-event-handler-in-a-pull-request)
- [281: How is Redis pub/sub different from a real event broker?](#281-how-is-redis-pubsub-different-from-a-real-event-broker)
- [282: Can PostgreSQL LISTEN and NOTIFY be used for events?](#282-can-postgresql-listen-and-notify-be-used-for-events)
- [283: Do message priorities fit an event-driven design?](#283-do-message-priorities-fit-an-event-driven-design)
- [284: How do you stop a consumer from overloading a downstream API?](#284-how-do-you-stop-a-consumer-from-overloading-a-downstream-api)
- [285: How do you shut down a consumer gracefully?](#285-how-do-you-shut-down-a-consumer-gracefully)
- [286: How do you health-check a consumer service?](#286-how-do-you-health-check-a-consumer-service)
- [287: How do you catch up on a large backlog after an outage?](#287-how-do-you-catch-up-on-a-large-backlog-after-an-outage)
- [288: What is the decider pattern in event sourcing?](#288-what-is-the-decider-pattern-in-event-sourcing)
- [289: How do you model events that happen because time passed?](#289-how-do-you-model-events-that-happen-because-time-passed)
- [290: How do you delete an entity in an event-sourced system?](#290-how-do-you-delete-an-entity-in-an-event-sourced-system)
- [291: How should a read model handle deleted entities?](#291-how-should-a-read-model-handle-deleted-entities)
- [292: What is the "listen to yourself" pattern, and how does it compare to an outbox?](#292-what-is-the-listen-to-yourself-pattern-and-how-does-it-compare-to-an-outbox)
- [293: How does Debezium's outbox event router work?](#293-how-does-debeziums-outbox-event-router-work)
- [294: What are workflow engines, and how do they relate to sagas?](#294-what-are-workflow-engines-and-how-do-they-relate-to-sagas)
- [295: How do you choose between choreography and orchestration?](#295-how-do-you-choose-between-choreography-and-orchestration)
- [296: How do you test a saga?](#296-how-do-you-test-a-saga)
- [297: How do you run an event-driven system locally for development?](#297-how-do-you-run-an-event-driven-system-locally-for-development)
- [298: What tools help you inspect messages in a broker?](#298-what-tools-help-you-inspect-messages-in-a-broker)
- [299: What is the difference between a domain event inside an aggregate and a notification to a user?](#299-what-is-the-difference-between-a-domain-event-inside-an-aggregate-and-a-notification-to-a-user)
- [300: In an interview, how would you explain when you'd choose event sourcing?](#300-in-an-interview-how-would-you-explain-when-youd-choose-event-sourcing)

### Advanced Questions (301-450)

- [301: What is the difference between global ordering and per-stream ordering?](#301-what-is-the-difference-between-global-ordering-and-per-stream-ordering)
- [302: Can Kafka be used as an event store for event sourcing?](#302-can-kafka-be-used-as-an-event-store-for-event-sourcing)
- [303: Why can a projection miss events when reading by an auto-increment position in PostgreSQL?](#303-why-can-a-projection-miss-events-when-reading-by-an-auto-increment-position-in-postgresql)
- [304: How do you fix the gap problem in a SQL event store?](#304-how-do-you-fix-the-gap-problem-in-a-sql-event-store)
- [305: How do you keep outbox order when running several relay instances?](#305-how-do-you-keep-outbox-order-when-running-several-relay-instances)
- [306: How do you keep an outbox table healthy at high volume?](#306-how-do-you-keep-an-outbox-table-healthy-at-high-volume)
- [307: What are the risks of CDC with PostgreSQL logical replication?](#307-what-are-the-risks-of-cdc-with-postgresql-logical-replication)
- [308: How does Kafka's consume-transform-produce exactly-once work?](#308-how-does-kafkas-consume-transform-produce-exactly-once-work)
- [309: What is zombie fencing in Kafka transactions?](#309-what-is-zombie-fencing-in-kafka-transactions)
- [310: How do you design an idempotency store that's safe under concurrency?](#310-how-do-you-design-an-idempotency-store-thats-safe-under-concurrency)
- [311: What isolation problems can sagas have, and how do you reduce them?](#311-what-isolation-problems-can-sagas-have-and-how-do-you-reduce-them)
- [312: What is the pivot transaction in a saga?](#312-what-is-the-pivot-transaction-in-a-saga)
- [313: What do you do when a compensating action itself fails?](#313-what-do-you-do-when-a-compensating-action-itself-fails)
- [314: How do you persist saga state safely?](#314-how-do-you-persist-saga-state-safely)
- [315: How do you spot and avoid tangled choreography?](#315-how-do-you-spot-and-avoid-tangled-choreography)
- [316: How do you roll out a breaking change to a widely used event?](#316-how-do-you-roll-out-a-breaking-change-to-a-widely-used-event)
- [317: How do you implement a chain of upcasters?](#317-how-do-you-implement-a-chain-of-upcasters)
- [318: When would you do a copy-and-transform migration of an event store?](#318-when-would-you-do-a-copy-and-transform-migration-of-an-event-store)
- [319: How do you migrate to a new event store technology?](#319-how-do-you-migrate-to-a-new-event-store-technology)
- [320: Why do snapshots need versioning?](#320-why-do-snapshots-need-versioning)
- [321: How should you think about stream design in event sourcing?](#321-how-should-you-think-about-stream-design-in-event-sourcing)
- [322: How do you scale read models?](#322-how-do-you-scale-read-models)
- [323: How do you rebuild a projection over billions of events quickly?](#323-how-do-you-rebuild-a-projection-over-billions-of-events-quickly)
- [324: How do you build a projection that needs data from several streams?](#324-how-do-you-build-a-projection-that-needs-data-from-several-streams)
- [325: How do you keep several read models consistent with each other?](#325-how-do-you-keep-several-read-models-consistent-with-each-other)
- [326: How do you enforce a rule that spans several aggregates?](#326-how-do-you-enforce-a-rule-that-spans-several-aggregates)
- [327: What is a hot aggregate, and how do you deal with it?](#327-what-is-a-hot-aggregate-and-how-do-you-deal-with-it)
- [328: How does crypto shredding work in practice?](#328-how-does-crypto-shredding-work-in-practice)
- [329: How do you handle retention and legal hold for events?](#329-how-do-you-handle-retention-and-legal-hold-for-events)
- [330: How do you stop someone from publishing fake events?](#330-how-do-you-stop-someone-from-publishing-fake-events)
- [331: How do you design an event-driven system for multiple tenants?](#331-how-do-you-design-an-event-driven-system-for-multiple-tenants)
- [332: How do you handle a noisy tenant in shared queues?](#332-how-do-you-handle-a-noisy-tenant-in-shared-queues)
- [333: What is a poison pill in an ordered partition, and why is it worse there?](#333-what-is-a-poison-pill-in-an-ordered-partition-and-why-is-it-worse-there)
- [334: Why do retry topics break ordering, and what can you do about it?](#334-why-do-retry-topics-break-ordering-and-what-can-you-do-about-it)
- [335: What is head-of-line blocking in event processing?](#335-what-is-head-of-line-blocking-in-event-processing)
- [336: How do rebalances cause trouble at scale, and how do newer Kafka protocols help?](#336-how-do-rebalances-cause-trouble-at-scale-and-how-do-newer-kafka-protocols-help)
- [337: Why are timestamps unreliable for ordering events from different services?](#337-why-are-timestamps-unreliable-for-ordering-events-from-different-services)
- [338: What is a Lamport clock, and when is it useful?](#338-what-is-a-lamport-clock-and-when-is-it-useful)
- [339: What are watermarks in stream processing?](#339-what-are-watermarks-in-stream-processing)
- [340: What kinds of windows exist in stream processing?](#340-what-kinds-of-windows-exist-in-stream-processing)
- [341: When would you use Kafka Streams or Flink instead of plain consumers?](#341-when-would-you-use-kafka-streams-or-flink-instead-of-plain-consumers)
- [342: What is the stream-table duality?](#342-what-is-the-stream-table-duality)
- [343: How do joins between streams and tables work in stream processing?](#343-how-do-joins-between-streams-and-tables-work-in-stream-processing)
- [344: What race can happen when events invalidate a cache?](#344-what-race-can-happen-when-events-invalidate-a-cache)
- [345: How can you provide read-your-writes across services?](#345-how-can-you-provide-read-your-writes-across-services)
- [346: What is causal consistency, and why does it matter in event-driven systems?](#346-what-is-causal-consistency-and-why-does-it-matter-in-event-driven-systems)
- [347: What are monotonic reads, and how can CQRS break them?](#347-what-are-monotonic-reads-and-how-can-cqrs-break-them)
- [348: How do you test eventual consistency and failure handling?](#348-how-do-you-test-eventual-consistency-and-failure-handling)
- [349: How do you load test an event pipeline?](#349-how-do-you-load-test-an-event-pipeline)
- [350: How do traces work for async consumers that process batches?](#350-how-do-traces-work-for-async-consumers-that-process-batches)
- [351: What SLOs make sense for an event-driven system?](#351-what-slos-make-sense-for-an-event-driven-system)
- [352: How do you detect a stuck consumer?](#352-how-do-you-detect-a-stuck-consumer)
- [353: How do you plan disaster recovery for an event-driven system?](#353-how-do-you-plan-disaster-recovery-for-an-event-driven-system)
- [354: What problems come with active-active multi-region event-driven systems?](#354-what-problems-come-with-active-active-multi-region-event-driven-systems)
- [355: What happens to consumer offsets when you replicate Kafka topics to another cluster?](#355-what-happens-to-consumer-offsets-when-you-replicate-kafka-topics-to-another-cluster)
- [356: What are CRDTs, and how do they relate to event-driven systems?](#356-what-are-crdts-and-how-do-they-relate-to-event-driven-systems)
- [357: What does it mean to treat events as products?](#357-what-does-it-mean-to-treat-events-as-products)
- [358: What does event governance include?](#358-what-does-event-governance-include)
- [359: What are common anti-patterns in event-driven systems?](#359-what-are-common-anti-patterns-in-event-driven-systems)
- [360: How can events lead to a distributed monolith?](#360-how-can-events-lead-to-a-distributed-monolith)
- [361: How can failures cascade in an event-driven system?](#361-how-can-failures-cascade-in-an-event-driven-system)
- [362: What is an event storm or feedback loop, and how do you prevent it?](#362-what-is-an-event-storm-or-feedback-loop-and-how-do-you-prevent-it)
- [363: Should consumers use circuit breakers?](#363-should-consumers-use-circuit-breakers)
- [364: How do broker quotas protect a shared cluster?](#364-how-do-broker-quotas-protect-a-shared-cluster)
- [365: What drives the cost of an event-driven system?](#365-what-drives-the-cost-of-an-event-driven-system)
- [366: How do you decide which parts of a system should use event sourcing?](#366-how-do-you-decide-which-parts-of-a-system-should-use-event-sourcing)
- [367: How do you migrate an existing CRUD aggregate to event sourcing?](#367-how-do-you-migrate-an-existing-crud-aggregate-to-event-sourcing)
- [368: What happens if you roll back a deploy after it stored new event types?](#368-what-happens-if-you-roll-back-a-deploy-after-it-stored-new-event-types)
- [369: What is forward compatibility, and why does it matter for events?](#369-what-is-forward-compatibility-and-why-does-it-matter-for-events)
- [370: What do you do when a bug produced wrong events?](#370-what-do-you-do-when-a-bug-produced-wrong-events)
- [371: How do you fix a read model after a projection bug?](#371-how-do-you-fix-a-read-model-after-a-projection-bug)
- [372: What if a side-effect handler ran on wrong data?](#372-what-if-a-side-effect-handler-ran-on-wrong-data)
- [373: Why must process managers be deterministic when replayed?](#373-why-must-process-managers-be-deterministic-when-replayed)
- [374: How does event sourcing help with debugging production issues?](#374-how-does-event-sourcing-help-with-debugging-production-issues)
- [375: What affects the write performance of an event store?](#375-what-affects-the-write-performance-of-an-event-store)
- [376: How do you tune a PostgreSQL table used as an event store?](#376-how-do-you-tune-a-postgresql-table-used-as-an-event-store)
- [377: How do you run one projection in parallel without breaking order?](#377-how-do-you-run-one-projection-in-parallel-without-breaking-order)
- [378: How do you make sure only one instance runs a projection?](#378-how-do-you-make-sure-only-one-instance-runs-a-projection)
- [379: How do you use a PostgreSQL advisory lock for a single projection runner?](#379-how-do-you-use-a-postgresql-advisory-lock-for-a-single-projection-runner)
- [380: How do you store the projection checkpoint together with the read model update?](#380-how-do-you-store-the-projection-checkpoint-together-with-the-read-model-update)
- [381: What if the read model lives in a different database than the checkpoint?](#381-what-if-the-read-model-lives-in-a-different-database-than-the-checkpoint)
- [382: How can concurrent handlers cause lost updates in a read model?](#382-how-can-concurrent-handlers-cause-lost-updates-in-a-read-model)
- [383: What happens to ordering if you add partitions to an existing Kafka topic?](#383-what-happens-to-ordering-if-you-add-partitions-to-an-existing-kafka-topic)
- [384: How do you choose a key for an event that involves several entities?](#384-how-do-you-choose-a-key-for-an-event-that-involves-several-entities)
- [385: What is fan-out explosion, and how do you avoid it?](#385-what-is-fan-out-explosion-and-how-do-you-avoid-it)
- [386: When should you compress events?](#386-when-should-you-compress-events)
- [387: How do producer batching settings trade latency for throughput?](#387-how-do-producer-batching-settings-trade-latency-for-throughput)
- [388: What should you tune for RabbitMQ consumers under heavy load?](#388-what-should-you-tune-for-rabbitmq-consumers-under-heavy-load)
- [389: What limits should you know about SQS FIFO?](#389-what-limits-should-you-know-about-sqs-fifo)
- [390: Should integration events be replayable by consumers?](#390-should-integration-events-be-replayable-by-consumers)
- [391: How do you keep a public event contract stable over years?](#391-how-do-you-keep-a-public-event-contract-stable-over-years)
- [392: What problems come with event-carried state transfer at scale?](#392-what-problems-come-with-event-carried-state-transfer-at-scale)
- [393: What is a reconciliation job, and why do event-driven systems need one?](#393-what-is-a-reconciliation-job-and-why-do-event-driven-systems-need-one)
- [394: How can a consumer detect that it missed an event?](#394-how-can-a-consumer-detect-that-it-missed-an-event)
- [395: What are heartbeat events used for?](#395-what-are-heartbeat-events-used-for)
- [396: How does a transactional inbox help with ordering and retries?](#396-how-does-a-transactional-inbox-help-with-ordering-and-retries)
- [397: What are the limits of broker-side deduplication?](#397-what-are-the-limits-of-broker-side-deduplication)
- [398: How do you build a time-ordered view from events produced by several services?](#398-how-do-you-build-a-time-ordered-view-from-events-produced-by-several-services)
- [399: Why can't you rely on the broker as a permanent backup of your data?](#399-why-cant-you-rely-on-the-broker-as-a-permanent-backup-of-your-data)
- [400: How do you handle schema evolution for events stored for a very long time?](#400-how-do-you-handle-schema-evolution-for-events-stored-for-a-very-long-time)
- [401: How would you design the order, payment and inventory flow for an online shop?](#401-how-would-you-design-the-order-payment-and-inventory-flow-for-an-online-shop)
- [402: A user updates their profile, the page reloads and shows the old data. How do you fix it?](#402-a-user-updates-their-profile-the-page-reloads-and-shows-the-old-data-how-do-you-fix-it)
- [403: Consumer lag keeps growing during peak hours. What do you check?](#403-consumer-lag-keeps-growing-during-peak-hours-what-do-you-check)
- [404: Customers report receiving two confirmation emails. What happened, and how do you fix it?](#404-customers-report-receiving-two-confirmation-emails-what-happened-and-how-do-you-fix-it)
- [405: A producer changed an event and a consumer started failing. How do you handle it?](#405-a-producer-changed-an-event-and-a-consumer-started-failing-how-do-you-handle-it)
- [406: The business wants a report on how many customers removed items from their cart before buying, over the last two years. How do you do it?](#406-the-business-wants-a-report-on-how-many-customers-removed-items-from-their-cart-before-buying-over-the-last-two-years-how-do-you-do-it)
- [407: Rebuilding a projection takes several days. How do you make it faster?](#407-rebuilding-a-projection-takes-several-days-how-do-you-make-it-faster)
- [408: One aggregate's stream has a million events and loading it is slow. What do you do?](#408-one-aggregates-stream-has-a-million-events-and-loading-it-is-slow-what-do-you-do)
- [409: The broker was down for an hour during a sale. What happens, and what do you check afterwards?](#409-the-broker-was-down-for-an-hour-during-a-sale-what-happens-and-what-do-you-check-afterwards)
- [410: Two services disagree about an order's status. How do you investigate?](#410-two-services-disagree-about-an-orders-status-how-do-you-investigate)
- [411: Ordering broke after you scaled a consumer from one instance to many. Why?](#411-ordering-broke-after-you-scaled-a-consumer-from-one-instance-to-many-why)
- [412: How would you model a bank account with event sourcing and a no-overdraft rule?](#412-how-would-you-model-a-bank-account-with-event-sourcing-and-a-no-overdraft-rule)
- [413: How would you prevent double-booking seats for a popular concert?](#413-how-would-you-prevent-double-booking-seats-for-a-popular-concert)
- [414: How would you design stock reservations that expire?](#414-how-would-you-design-stock-reservations-that-expire)
- [415: How would you start moving a monolith to an event-driven design?](#415-how-would-you-start-moving-a-monolith-to-an-event-driven-design)
- [416: How would you design ingestion for millions of IoT sensor events per minute?](#416-how-would-you-design-ingestion-for-millions-of-iot-sensor-events-per-minute)
- [417: Auditors need a complete, tamper-evident history of changes. How do events help?](#417-auditors-need-a-complete-tamper-evident-history-of-changes-how-do-events-help)
- [418: Your team wants to use CQRS and event sourcing everywhere. How do you respond?](#418-your-team-wants-to-use-cqrs-and-event-sourcing-everywhere-how-do-you-respond)
- [419: How do you bring third-party webhooks into your event-driven system?](#419-how-do-you-bring-third-party-webhooks-into-your-event-driven-system)
- [420: How would you design a notification service driven by events?](#420-how-would-you-design-a-notification-service-driven-by-events)
- [421: How do you keep a search index in sync with your database?](#421-how-do-you-keep-a-search-index-in-sync-with-your-database)
- [422: How would you build a multi-day approval workflow?](#422-how-would-you-build-a-multi-day-approval-workflow)
- [423: A downstream API goes down and your consumers' retries make the recovery harder. What do you change?](#423-a-downstream-api-goes-down-and-your-consumers-retries-make-the-recovery-harder-what-do-you-change)
- [424: A projection rebuild accidentally sent thousands of emails. What went wrong, and how do you prevent it?](#424-a-projection-rebuild-accidentally-sent-thousands-of-emails-what-went-wrong-and-how-do-you-prevent-it)
- [425: An event handler needs data from another service that isn't in the event. What are your options?](#425-an-event-handler-needs-data-from-another-service-that-isnt-in-the-event-what-are-your-options)
- [426: The business needs gapless invoice numbers. How do you generate them in an event-driven system?](#426-the-business-needs-gapless-invoice-numbers-how-do-you-generate-them-in-an-event-driven-system)
- [427: How would you model a shopping cart with event sourcing?](#427-how-would-you-model-a-shopping-cart-with-event-sourcing)
- [428: How would you build a reporting database from events?](#428-how-would-you-build-a-reporting-database-from-events)
- [429: How would you design outgoing webhooks for your customers?](#429-how-would-you-design-outgoing-webhooks-for-your-customers)
- [430: How can you do event sourcing on a serverless AWS stack?](#430-how-can-you-do-event-sourcing-on-a-serverless-aws-stack)
- [431: How do you append events with optimistic concurrency in DynamoDB?](#431-how-do-you-append-events-with-optimistic-concurrency-in-dynamodb)
- [432: When would you use Redis Streams for events?](#432-when-would-you-use-redis-streams-for-events)
- [433: What is NATS JetStream, and how does it compare to Kafka?](#433-what-is-nats-jetstream-and-how-does-it-compare-to-kafka)
- [434: How do database isolation levels affect event handlers?](#434-how-do-database-isolation-levels-affect-event-handlers)
- [435: The outbox relay has fallen behind by millions of rows. What do you do?](#435-the-outbox-relay-has-fallen-behind-by-millions-of-rows-what-do-you-do)
- [436: How do you safely replace a consumer with a rewritten version?](#436-how-do-you-safely-replace-a-consumer-with-a-rewritten-version)
- [437: You need to split one large topic into two. How do you do it without breaking consumers?](#437-you-need-to-split-one-large-topic-into-two-how-do-you-do-it-without-breaking-consumers)
- [438: How do you rename an event type that's already stored and published?](#438-how-do-you-rename-an-event-type-thats-already-stored-and-published)
- [439: A payment provider sends webhook events duplicated and out of order. How do you handle it?](#439-a-payment-provider-sends-webhook-events-duplicated-and-out-of-order-how-do-you-handle-it)
- [440: How do you make sure a confirmation email is sent once and only once?](#440-how-do-you-make-sure-a-confirmation-email-is-sent-once-and-only-once)
- [441: How do you test a new version of a projection before switching to it?](#441-how-do-you-test-a-new-version-of-a-projection-before-switching-to-it)
- [442: Customer support wants a full timeline of an order across all services. How do you build it?](#442-customer-support-wants-a-full-timeline-of-an-order-across-all-services-how-do-you-build-it)
- [443: A legacy system only produces nightly batch files. How do you connect it to an event-driven platform?](#443-a-legacy-system-only-produces-nightly-batch-files-how-do-you-connect-it-to-an-event-driven-platform)
- [444: How do you enforce "at most 3 password resets per day" in an event-sourced system?](#444-how-do-you-enforce-at-most-3-password-resets-per-day-in-an-event-sourced-system)
- [445: How do you safely retire a service that publishes events?](#445-how-do-you-safely-retire-a-service-that-publishes-events)
- [446: A tenant asks for an export of all their data. How do events make it easier or harder?](#446-a-tenant-asks-for-an-export-of-all-their-data-how-do-events-make-it-easier-or-harder)
- [447: A Kafka consumer keeps getting kicked out of its group while processing long tasks. What's going on?](#447-a-kafka-consumer-keeps-getting-kicked-out-of-its-group-while-processing-long-tasks-whats-going-on)
- [448: What are the main questions to ask before choosing EDA, CQRS or event sourcing?](#448-what-are-the-main-questions-to-ask-before-choosing-eda-cqrs-or-event-sourcing)
- [449: How do EDA, CQRS and event sourcing fit together in one system?](#449-how-do-eda-cqrs-and-event-sourcing-fit-together-in-one-system)
- [450: You join a team with an existing event-driven system. What do you look at first?](#450-you-join-a-team-with-an-existing-event-driven-system-what-do-you-look-at-first)

---

# Easy Questions (1-150)

## 1: What is event-driven architecture?

Event-driven architecture (EDA) is a way of building systems where parts of the system talk to each other by sending events. When something happens, like "an order was placed", the service that did it publishes an event. Other services that care about it react to it on their own.

The sender does not know who listens and does not wait for them. This makes services less dependent on each other, but it also makes the flow of the system harder to follow.

## 2: What is an event?

An event is a record of something that already happened in the system. For example `OrderPlaced`, `PaymentFailed` or `UserRegistered`. It has a name, some data about what happened and some metadata like an id and a timestamp.

Since it describes the past, an event is a fact. You can't reject it or change it, you can only react to it.

## 3: What is the difference between an event, a command and a message?

- A **message** is any piece of data sent from one part of a system to another. Commands and events are both messages.
- A **command** asks someone to do something: `PlaceOrder`, `CancelSubscription`. It has one receiver, and the receiver can say no.
- An **event** says that something already happened: `OrderPlaced`, `SubscriptionCancelled`. It can have zero, one or many listeners, and nobody can say no to it.

A simple way to remember: commands are in the imperative ("do this"), events are in the past tense ("this happened").

## 4: What is an event producer?

A producer (also called a publisher) is the part of the system that creates an event and sends it out. For example, the order service publishes `OrderPlaced` after it saves a new order.

The producer should not care who reads the event. Its only job is to publish correct events reliably.

## 5: What is an event consumer?

A consumer (also called a subscriber or listener) is the part of the system that receives events and does something with them. For example, the email service listens for `OrderPlaced` and sends a confirmation email.

A consumer decides by itself what to do with an event. Many consumers can react to the same event in different ways.

## 6: What is an event broker?

An event broker is the server in the middle that receives events from producers and delivers them to consumers. It stores events (at least for a while), routes them to the right places and handles things like retries.

Common brokers are Apache Kafka, RabbitMQ, Amazon SQS and SNS, Amazon EventBridge, Google Pub/Sub, Azure Service Bus, NATS and Apache Pulsar.

## 7: Why would a team choose an event-driven architecture?

The main reasons are:

- **Loose coupling.** Services don't call each other directly, so one can change or go down without breaking the others right away.
- **Easy to extend.** A new feature can subscribe to existing events without touching the producer.
- **Scaling.** Consumers can be scaled on their own and can process work at their own pace.
- **Resilience.** If a consumer is down, events wait in the broker until it comes back.
- **Real-time reactions.** Things can happen as soon as an event occurs instead of on a schedule.

## 8: What are the downsides of event-driven architecture?

- The flow is harder to follow, since there is no single place that shows "what happens after an order is placed".
- Data is eventually consistent, not immediately consistent.
- You have to deal with duplicate events, events that come in the wrong order and failed events.
- Debugging needs good logging, tracing and correlation ids.
- You run and pay for one more piece of infrastructure: the broker.
- Changing the shape of an event is harder, because you may not know all of its consumers.

## 9: What does loose coupling mean in an event-driven system?

It means services know as little about each other as possible. The producer does not know who consumes its events, and the consumer does not know the internals of the producer. They only share the event format.

Because of this, you can add a new consumer, move a service to a new server or rewrite it in another language without changing the other side, as long as the event format stays the same.

## 10: What is the difference between synchronous and asynchronous communication?

In synchronous communication the caller sends a request and waits for the answer, like an HTTP call. If the other service is slow or down, the caller is slow or fails too.

In asynchronous communication the sender puts a message somewhere (usually a broker) and continues its work. The receiver processes it later. Events are almost always sent asynchronously.

## 11: What is the publish/subscribe pattern?

In publish/subscribe (pub/sub), a publisher sends a message to a topic, not to a specific receiver. Every subscriber of that topic gets its own copy of the message.

So if three services subscribe to `order-events`, all three get every order event. The publisher doesn't know or care how many subscribers there are.

## 12: What is the difference between a queue and pub/sub?

With a **queue** (point-to-point), each message is handled by only one consumer. If you run five workers on the same queue, they share the work, and each message goes to one of them. This is good for jobs and commands.

With **pub/sub**, each subscriber gets its own copy of every message. This is good for events that many services care about.

Many brokers combine both: in Kafka, each consumer group gets every message (pub/sub), and inside a group the partitions are split between the instances (queue-like). In AWS you can send to an SNS topic that fans out to several SQS queues.

## 13: What is a topic?

A topic is a named channel that events are published to, like `orders` or `user-events`. Producers write to a topic and consumers subscribe to it.

How a topic works depends on the broker. In Kafka a topic is a log split into partitions. In RabbitMQ you get a similar effect with a topic exchange and bound queues. In SNS a topic is a fan-out point that pushes messages to its subscribers.

## 14: What is the event notification pattern?

In the event notification pattern, the event only says that something changed and includes very little data, often just an id:

```json
{ "type": "CustomerAddressChanged", "customerId": "c-42" }
```

If a consumer needs the new address, it calls the customer service to get it. Events stay small and the source of truth stays in one place. The downside is that consumers have to call back, which adds load and coupling to the producer.

## 15: What is event-carried state transfer?

In event-carried state transfer, the event contains all the data consumers need, so they don't need to call back:

```json
{
  "type": "CustomerAddressChanged",
  "customerId": "c-42",
  "address": { "street": "1 Main St", "city": "Berlin", "zip": "10115" }
}
```

Consumers can keep their own local copy of the data. This removes runtime calls between services, but events get bigger and each consumer holds a copy that can be slightly out of date.

## 16: What is event sourcing?

Event sourcing is a way of storing data. Instead of saving only the current state of an object (like a row in a table), you save every change as an event, in order. The current state is built by replaying those events.

For a bank account you store `AccountOpened`, `MoneyDeposited`, `MoneyWithdrawn`, and the balance is the result of applying them one after another. The list of events is the source of truth.

## 17: What is CQRS?

CQRS stands for Command Query Responsibility Segregation. It means you use one model to change data (commands) and a different model to read data (queries).

The write side focuses on business rules and keeping data correct. The read side focuses on returning data quickly in the shape the screen or API needs. The two sides can live in the same database or in different ones.

## 18: Why would you separate reads from writes?

Reads and writes usually have different needs:

- Writes need validation, business rules and transactions.
- Reads need speed, joins, filters, search and data shaped for the UI.
- Most systems read much more than they write, so you may want to scale reads separately.

With one model for both, the model often becomes a compromise that is not great at either. Splitting them lets each side be simple for its own job.

## 19: What is a command in CQRS?

A command is a request to change the state of the system, like `RegisterUser` or `ChangeShippingAddress`. It carries the data needed to do the change.

```ts
class ChangeShippingAddress {
  constructor(
    public readonly orderId: string,
    public readonly address: string,
  ) {}
}
```

A command is handled by exactly one handler. It can succeed or be rejected, for example if the order was already shipped.

## 20: What is a query in CQRS?

A query asks for data and never changes anything. For example `GetOrderById` or `ListOrdersForCustomer`.

```ts
class GetOrderById {
  constructor(public readonly orderId: string) {}
}
```

Because queries have no side effects, you can cache them, run them on replicas and call them as many times as you want.

## 21: What is a command handler?

A command handler is the code that receives one type of command and carries it out. It usually loads the needed data, checks the business rules, makes the change and saves it.

```ts
class ChangeShippingAddressHandler {
  constructor(private orders: OrderRepository) {}

  async execute(cmd: ChangeShippingAddress): Promise<void> {
    const order = await this.orders.getById(cmd.orderId);
    order.changeShippingAddress(cmd.address); // throws if already shipped
    await this.orders.save(order);
  }
}
```

## 22: What is a query handler?

A query handler receives a query and returns data. It should not contain business rules or change anything. Often it is just a direct, simple database query against the read model.

```ts
class GetOrderByIdHandler {
  constructor(private db: Pool) {}

  async execute(q: GetOrderById) {
    const { rows } = await this.db.query(
      "SELECT * FROM order_view WHERE id = $1",
      [q.orderId],
    );
    return rows[0] ?? null;
  }
}
```

## 23: What is the write model?

The write model is the part of a CQRS system that handles commands. It holds the business rules and makes sure the data stays valid. In domain-driven design it is usually made of aggregates.

It is not built for showing data. It only needs to load what is needed to decide whether a change is allowed.

## 24: What is the read model?

The read model is the data that queries read from. It is shaped for how the data is shown, often flat and denormalized, so a screen can get everything it needs with one simple query.

It is usually built from events coming from the write side. You can have many read models for the same data, one for each screen or use case.

## 25: What is a projection?

A projection is the code that reads events and builds or updates a read model from them. For example, a projection listens to `OrderPlaced`, `OrderShipped` and `OrderCancelled` and keeps an `order_summary` table up to date.

The word is also used for the resulting read model itself. If a projection has a bug, you can fix it and run it again over all events to rebuild the data.

## 26: What is eventual consistency?

Eventual consistency means that after a change, not every part of the system sees it right away, but all parts will see it after a short time, if no new changes happen.

In CQRS, the write side saves a change, then an event updates the read side a few milliseconds or seconds later. During that gap, a query can still return old data.

## 27: Are CQRS and event sourcing the same thing?

No. They are two separate patterns that often go together.

- CQRS is about having separate models for reads and writes.
- Event sourcing is about storing state as a list of events.

Event sourcing almost always needs CQRS, because querying a list of events directly is hard, so you build read models from them. But CQRS works fine without event sourcing, with a normal database on the write side.

## 28: Can you use CQRS without event sourcing?

Yes, and that is the more common case. The write side stores data in normal tables. The read side can be:

- the same tables queried with different, read-only code,
- database views or materialized views,
- a separate database or search index updated by events or by change data capture.

Starting this way gives most of the benefits of CQRS without the extra work of event sourcing.

## 29: What is CQS, and how is CQRS related to it?

CQS (Command Query Separation) is an idea from Bertrand Meyer: a method should either change state (a command) or return data (a query), but not both.

CQRS, named by Greg Young, takes the same idea and applies it at the level of the architecture. Instead of separating methods, you separate whole models, and sometimes whole databases, for reads and writes.

## 30: Why are events named in the past tense?

Because an event describes something that has already happened. `OrderPlaced` is a fact. `PlaceOrder` would be a request that might fail.

Past tense names also make the meaning clear to consumers: they can't stop or reject the event, they can only react to it. Good event names use business language, like `InvoicePaid`, not technical words like `InvoiceRowUpdated`.

## 31: What does a typical event look like?

An event usually has two parts: metadata about the event and the data (payload) about what happened.

```json
{
  "id": "6f1c2e9a-3b4d-4c55-9a1e-0f8f7d2b6c11",
  "type": "OrderPlaced",
  "version": 1,
  "occurredAt": "2026-11-19T10:15:30Z",
  "source": "order-service",
  "correlationId": "req-81f2",
  "data": {
    "orderId": "o-1001",
    "customerId": "c-42",
    "total": 59.9,
    "currency": "EUR"
  }
}
```

## 32: Why should events be immutable?

An event is a record of the past, and the past doesn't change. If you could edit events, consumers that already processed the old version would have different data than ones that read the new version, and your history would no longer be trustworthy.

If something was wrong, you publish a new event that corrects it, like `OrderTotalCorrected`, instead of editing the old one.

## 33: What is an event store?

An event store is a database built to save events in order and read them back. It supports appending events to a stream, reading a stream from the start, and subscribing to new events.

Examples are KurrentDB (formerly EventStoreDB), Marten on PostgreSQL and Axon Server. Many teams also build a simple one on top of a PostgreSQL table.

## 34: What is an aggregate?

An aggregate is a term from domain-driven design. It is a group of objects that are changed together as one unit and protect their own rules. For example, an `Order` with its order lines is one aggregate.

Each command changes one aggregate, and the aggregate decides if the change is allowed. In event sourcing, each aggregate has its own stream of events.

## 35: What is the difference between a domain event and an integration event?

A **domain event** is used inside one service or bounded context. It can contain internal details and can change freely as the code changes.

An **integration event** is published for other services. It is a public contract, so it should be stable, versioned and contain only what other services need.

Often a service handles its domain events internally and then publishes a smaller, cleaner integration event to the broker.

## 36: What is a message queue?

A message queue is a buffer that holds messages until a consumer takes them. Producers add messages at the end, consumers take them from the front. Once a message is processed and acknowledged, it is removed.

Examples are RabbitMQ queues, Amazon SQS and Azure Service Bus queues. Queues are good for spreading work across several workers and for smoothing out traffic spikes.

## 37: When should you not use an event-driven architecture?

- When the system is small and simple, and one app with one database is enough.
- When the user needs the result right away and the steps must succeed or fail together, like a simple form save.
- When the team has no experience running a broker and debugging async flows.
- When strong consistency is required and you can do it in one database transaction.

Events add moving parts. Use them where the loose coupling actually pays off.

## 38: When should you not use CQRS?

CQRS is not a good fit for simple CRUD screens where reads and writes look the same. It adds more classes, more code paths and often eventual consistency, which you then have to explain to users and handle in the UI.

Use it in the parts of the system that have complex business rules or very different read and write needs, not across the whole app by default.

## 39: What is an event bus?

An event bus is a component that lets parts of an application publish events and subscribe to them without knowing each other. It can be:

- **in-process**: a simple object in memory that calls handlers, like Node's `EventEmitter` or the `EventBus` in NestJS CQRS,
- **distributed**: a broker like Kafka, RabbitMQ or EventBridge that delivers events between services.

An in-process bus is fast but loses events if the app crashes. A distributed bus is durable but slower and more complex.

## 40: How does Node's EventEmitter relate to event-driven design?

`EventEmitter` is an in-process example of the same idea: one part of the code emits an event, and listeners react to it.

```ts
import { EventEmitter } from "node:events";

const bus = new EventEmitter();

bus.on("orderPlaced", (order) => console.log("send email for", order.id));
bus.on("orderPlaced", (order) => console.log("update stats for", order.id));

bus.emit("orderPlaced", { id: "o-1001" });
```

Listeners run synchronously in the order they were added, and nothing is stored. If the process crashes, events are lost. That's why services use a broker for events that must not be lost.

## 41: What is fan-out?

Fan-out means one event is delivered to many consumers. For example, one `OrderPlaced` event goes to billing, shipping, email and analytics.

Brokers support this in different ways: SNS topics push to many SQS queues, RabbitMQ fanout or topic exchanges copy messages to many queues, and Kafka lets many consumer groups read the same topic.

## 42: What is an event schema?

An event schema is the definition of an event's structure: which fields it has, their types, and which ones are required. It is the contract between producers and consumers.

You can describe it with JSON Schema, Avro or Protobuf. Having a written schema lets you validate events and check if a change will break consumers.

## 43: What formats are commonly used for events?

- **JSON**: easy to read and debug, supported everywhere, but bigger and has no built-in schema.
- **Avro**: binary and compact, has a schema, and is popular with Kafka and a schema registry.
- **Protobuf**: binary, compact, strongly typed and good across many languages.

Many teams start with JSON plus JSON Schema, and move to Avro or Protobuf when volume or strict contracts matter.

## 44: What is a dead letter queue?

A dead letter queue (DLQ) is a separate queue where messages go when they can't be processed, for example after failing a set number of times or when they are malformed.

This stops one bad message from being retried forever and blocking others. Someone can then look at the DLQ, fix the issue and send the messages back for processing.

## 45: Why do consumers retry failed events?

Many failures are temporary: a database timeout, a network blip, a service restarting. Retrying after a short wait often makes the event succeed without anyone doing anything.

Retries should have a limit and a growing delay between attempts. After the last attempt, the event should go to a dead letter queue so it doesn't block the rest.

## 46: What are at-most-once, at-least-once and exactly-once delivery?

- **At-most-once**: each message is delivered zero or one time. Fast, but messages can be lost.
- **At-least-once**: each message is delivered one or more times. Nothing is lost, but you can get duplicates. This is the most common setting.
- **Exactly-once**: each message has its effect exactly one time. It's hard to get end-to-end, and usually means at-least-once delivery plus idempotent processing.

## 47: What is idempotency?

An operation is idempotent if doing it once or many times gives the same result. "Set status to shipped" is idempotent. "Add 10 to balance" is not, because doing it twice adds 20.

In event-driven systems, idempotency matters because the same event can arrive more than once.

## 48: Why must event consumers be idempotent?

Most brokers deliver at least once. A consumer can process an event, crash before it acknowledges it, and get the same event again after restart. Retries and rebalances also cause duplicates.

If the consumer is not idempotent, the customer might get charged twice or receive two emails. So consumers either use naturally idempotent operations or keep track of which event ids they already handled.

## 49: What is message acknowledgment?

An acknowledgment (ack) is how a consumer tells the broker "I finished processing this message". After the ack, the broker can remove the message or move the consumer's position forward.

If the consumer crashes before acking, the broker delivers the message again. That's why you should ack only after the work is done, not when the message arrives.

## 50: Why does message ordering matter?

Some events only make sense in order. If `OrderCancelled` is processed before `OrderPlaced`, the consumer might create an order that should be cancelled.

Most brokers only guarantee order in a limited scope: within one Kafka partition, one SQS FIFO message group or one RabbitMQ queue with a single consumer. So you usually make sure all events for the same entity go to the same partition or group, for example by using the order id as the key.

## 51: What is a partition in Kafka, and why does it matter for events?

A Kafka topic is split into partitions. Each partition is an ordered log, and Kafka keeps the order of events only inside one partition, not across the whole topic.

When you publish with a key, like an order id, all events with that key go to the same partition. That's how you keep events for one order in order while still spreading the load across many partitions.

## 52: What is a consumer group?

A consumer group is a set of consumer instances that work together to read a topic. Each partition is read by only one instance in the group, so the instances share the work.

Different groups are independent. The billing group and the email group both read every event, each at its own pace, and each keeps its own position in the topic.

## 53: Is a webhook event-driven?

Yes, in a simple form. A webhook is an HTTP call that one system makes to another when something happens, like Stripe calling your API when a payment succeeds.

It's event-driven because you react to something that happened, but it's still a direct HTTP call. If your endpoint is down, you depend on the sender's retry policy. Many teams receive webhooks, store them quickly, return 200, and then publish them to their own broker for further processing.

## 54: How is event-driven communication different from request-response?

In request-response, service A calls service B and waits for an answer. A knows about B, and if B is down, A's request fails.

In event-driven communication, A publishes an event and moves on. A doesn't know who reacts. If a consumer is down, the event waits in the broker. The cost is that A doesn't get an answer, so you can't use events when you need a result right now.

## 55: What is choreography?

Choreography is a way to coordinate several services where there is no central controller. Each service listens for events and decides by itself what to do next, then publishes its own events.

For example: the order service publishes `OrderPlaced`, the payment service reacts and publishes `PaymentCompleted`, then the shipping service reacts to that. It's simple for short flows but hard to follow when many steps are involved.

## 56: What is orchestration?

Orchestration uses one central component, the orchestrator, that tells each service what to do and waits for their replies. For example, an order orchestrator sends `ChargePayment`, waits for the result, then sends `ReserveStock`, and so on.

The whole flow is visible in one place, which makes it easier to understand and change. The downside is that the orchestrator knows about many services and becomes an important part to keep running.

## 57: What is a saga?

A saga is a way to handle a business process that spans several services, where you can't use one database transaction. The process is split into local steps. Each step updates one service and triggers the next step.

If a step fails, the saga runs compensating actions to undo the earlier steps. A saga can be built with choreography (services react to events) or orchestration (a central coordinator).

## 58: What is a compensating action?

A compensating action is a step that undoes the effect of an earlier step in a saga. For example, if the payment was charged but stock could not be reserved, the compensating action is to refund the payment.

It's not a database rollback. The earlier step really happened and other people may have seen it, so the compensation is a new business action, like a refund or a cancellation email.

## 59: What is the transactional outbox pattern?

The outbox pattern solves this problem: you need to save data to your database and publish an event, and both must happen or neither.

Instead of publishing to the broker directly, you save the event in an `outbox` table in the same database transaction as your data. A separate process then reads the outbox table and publishes the events to the broker. If the app crashes, the event is still in the table and will be sent later.

## 60: What is change data capture?

Change data capture (CDC) is a way to detect changes in a database and send them somewhere else as events. It usually reads the database's transaction log, like PostgreSQL's WAL or MySQL's binlog, so the app doesn't have to do anything.

Debezium is a popular open source tool for this. CDC is often used to publish outbox events, to sync data to a search index or to pull events out of a legacy system.

## 61: What is a materialized view?

A materialized view is a precomputed result of a query that is stored so it can be read quickly. In databases like PostgreSQL it's a real feature: `CREATE MATERIALIZED VIEW` stores the result and `REFRESH MATERIALIZED VIEW` updates it.

In CQRS, the read model is often called a materialized view too, even when it's a normal table kept up to date by a projection.

## 62: Where can a read model be stored?

Anywhere that fits the queries you need:

- a table in PostgreSQL or MySQL, often in the same database as the write side,
- a document database like MongoDB for nested data,
- Elasticsearch or OpenSearch for full-text search,
- Redis for very fast lookups,
- a data warehouse for reporting.

Different read models in the same system can use different stores.

## 63: Why might a user see old data after making a change in a CQRS system?

Because the read model is updated after the write side, often a little later through events. If the UI saves a change and immediately asks the read model for data, the projection might not have processed the event yet.

Common fixes are: update the UI with the data you just sent (optimistic UI), return the new state or version from the command, or wait until the read model has caught up to that version.

## 64: What is an event handler?

An event handler is a function that runs when a specific event arrives. A consumer service usually has one handler per event type.

```ts
async function onOrderPlaced(event: OrderPlaced) {
  await emailService.sendOrderConfirmation(
    event.data.customerId,
    event.data.orderId,
  );
}
```

A good handler does one thing, is idempotent and doesn't assume what other handlers do.

## 65: What is event replay?

Event replay means reading old events again from the start or from a given point and processing them a second time. You do it to rebuild a read model, to fix data after a bug, or to fill a new service with historical data.

It works only if the events are still stored, like in an event store or a Kafka topic with long retention. Handlers that send emails or charge cards must not run their side effects again during a replay.

## 66: What is a snapshot in event sourcing?

A snapshot is the saved state of an aggregate at a certain event number. When loading the aggregate, you start from the latest snapshot and replay only the events after it, instead of every event from the beginning.

Snapshots are an optimization for long streams. They are not the source of truth, so you can delete them and build them again from events.

## 67: What is event versioning?

Event versioning is how you handle changes to the structure of an event over time. For example, `OrderPlaced` v1 had `price` and v2 has `amount` and `currency`.

Since old events stay stored and old consumers may still run, you need a plan: add only optional fields, publish a new event type, or convert old events into the new shape when reading them (upcasting).

## 68: What is a stream in event sourcing?

A stream is an ordered list of events that belong to one thing, usually one aggregate. For example, all events of order `o-1001` are in the stream `order-o-1001`.

Each event in a stream has a version number: 1, 2, 3 and so on. To load the order you read its stream. To save, you append new events to the end.

## 69: What is an append-only log?

An append-only log is a data structure where you can only add new entries at the end. You never update or delete existing entries.

Event stores and Kafka topics work this way. Appending is fast, history is never lost, and readers can keep a simple position (offset) to know where they stopped.

## 70: What is a correlation id?

A correlation id is an id that is shared by all messages that belong to the same business flow, such as one checkout. The first request creates it, and every command and event caused by it carries the same id.

With it, you can search your logs for one id and see the whole flow across all services.

## 71: What is a causation id?

A causation id is the id of the message that directly caused the current one. If command `C1` caused event `E1`, then `E1` has causation id `C1`. If `E1` caused command `C2`, `C2` has causation id `E1`.

The correlation id groups the whole flow. The causation id shows the exact chain of what caused what inside it.

## 72: What are the benefits of event sourcing?

- **Full history.** You know every change and when it happened, which is great for audit.
- **Time travel.** You can rebuild the state at any point in the past.
- **New read models from old data.** You can build a new report from events that happened before the report existed.
- **Debugging.** You can replay the exact events that led to a bug.
- **Natural fit for events.** The events you store are also the ones you publish.

## 73: What are the downsides of event sourcing?

- It's harder to learn and harder to explain to new team members.
- You can't just query the current state, you need projections.
- Changing event structure is harder, because old events stay forever.
- Deleting personal data needs special techniques.
- Long streams need snapshots.
- Many common tools and ORMs are built for CRUD, not for events.

It's worth it for parts of a system where history really matters, not for everything.

## 74: What is domain-driven design, and how does it relate to CQRS?

Domain-driven design (DDD) is an approach to software where the code follows the business domain closely, using the same words as the business. It brings ideas like aggregates, domain events and bounded contexts.

CQRS and event sourcing grew up in the DDD community. Aggregates fit the write side, domain events fit event sourcing and integration, and bounded contexts help decide where CQRS is worth it. You can use CQRS without full DDD, though.

## 75: What is a bounded context?

A bounded context is a part of the system where a set of terms and rules has one clear meaning. "Customer" in billing (who pays, tax id) is different from "customer" in shipping (address, delivery notes).

Each bounded context owns its data and model. Events are often how bounded contexts talk to each other, which is why integration events are designed per context.

## 76: Why does it help to name events with business language?

Events named in business terms, like `InvoiceSent` or `SeatReserved`, are easy for both developers and business people to understand. They can be discussed in meetings and match what the business actually cares about.

Technical names like `InvoiceTableUpdated` hide the reason for the change, so consumers have to guess what happened.

## 77: What is the mediator pattern in CQRS code?

A mediator is an object that receives a command or query and finds the right handler for it. The caller only knows the mediator, not the handler.

```ts
await commandBus.execute(new PlaceOrder(customerId, items));
const order = await queryBus.execute(new GetOrderById(orderId));
```

Libraries like MediatR in .NET and the `@nestjs/cqrs` module in NestJS work this way. It keeps controllers thin and makes it easy to add things like logging or validation around every handler.

## 78: What does the NestJS CQRS module provide?

The `@nestjs/cqrs` package gives you three buses and decorators to connect handlers to them:

- `CommandBus` with `@CommandHandler()` and `ICommandHandler`,
- `QueryBus` with `@QueryHandler()` and `IQueryHandler`,
- `EventBus` with `@EventsHandler()` and `IEventHandler`.

It also has `AggregateRoot` for collecting events and sagas built with RxJS. All of this is in-process. To send events between services you still need a broker.

## 79: What is a command bus?

A command bus takes a command object and sends it to the one handler registered for that command type. If no handler exists, it throws an error.

It separates the code that wants something done (a controller) from the code that does it (the handler), and it's a good place to add shared behavior like logging, validation, transactions or retries.

## 80: What is a query bus?

A query bus is the same idea as a command bus, but for queries. It finds the handler for a query type, runs it and returns the result.

Some teams skip the query bus and just call a read service directly, since queries are simple. Using a bus gives a consistent style and a place for things like caching.

## 81: Can a command return a value?

In strict CQRS, a command returns nothing or only success or failure. In practice, many teams let a command return small things like the id of a new entity or the new version number, because it saves a round trip and doesn't break anything important.

What a command should not do is return the full read model, because that mixes the write and read sides again.

## 82: Should a query ever change state?

No. A query should only read. If it changes something, calling it twice could give different results, caching it would be unsafe, and running it on a read replica could fail.

Things like logging that a query happened or counting requests are usually fine, because they don't change business state.

## 83: Where should you validate a command?

Usually in two places:

1. **Input validation** before the handler: required fields, formats, lengths. This can be done with a schema library or in a middleware.
2. **Business rules** inside the aggregate or domain: "you can't cancel an order that's already shipped".

Input validation is cheap and catches bad requests early. Business rules need the current state, so they live in the write model.

## 84: What is backpressure?

Backpressure is a way for a slow consumer to say "slow down" so it isn't overwhelmed by more messages than it can handle.

With brokers this is mostly built in for pull-based consumers: they only fetch new messages when they are ready. In push-based setups you limit how many unacknowledged messages a consumer can have, like RabbitMQ's prefetch count.

## 85: What is consumer lag?

Consumer lag is how far behind a consumer is compared to the newest message in the topic or queue. In Kafka it's the difference between the latest offset and the consumer group's committed offset.

Growing lag means the consumer can't keep up. Then read models get more and more stale. It's one of the most important metrics to watch in an event-driven system.

## 86: What is a poison message?

A poison message is a message that always fails, no matter how many times it's retried. It might have a bad format, missing fields or data that triggers a bug.

If you keep retrying it, it blocks the queue or partition and wastes resources. After a few failed attempts it should be moved to a dead letter queue.

## 87: What is message TTL?

TTL (time to live) is how long a message can stay in a queue before the broker throws it away or moves it to a dead letter queue. For example, a "price changed" notification might be useless after one hour.

Kafka uses retention instead: messages are kept for a configured time or size, whether they were read or not.

## 88: What is a durable subscription?

A durable subscription keeps messages for a subscriber even while it's offline. When the subscriber comes back, it receives everything it missed.

A non-durable subscription only delivers messages while the subscriber is connected. In RabbitMQ this is the difference between a durable named queue and a temporary exclusive queue. Kafka consumer groups are durable by nature because they store their offset.

## 89: What is the difference between push and pull consumers?

With **push**, the broker sends messages to the consumer as they arrive. RabbitMQ, SNS and EventBridge work this way.

With **pull**, the consumer asks the broker for messages when it's ready. Kafka and SQS work this way.

Pull gives the consumer control over its speed. Push can have lower latency but needs limits so the consumer isn't flooded.

## 90: What is the difference between event streaming and messaging?

**Messaging** (like RabbitMQ or SQS) focuses on delivering messages to consumers. Once a message is processed and acked, it's usually gone.

**Event streaming** (like Kafka or Pulsar) keeps events in a log for a set time, even after they are read. Many consumers can read them at their own pace, and you can rewind and replay.

Streaming is better when you need replay or many independent readers. Messaging is simpler for work queues.

## 91: What is an event-driven microservice?

It's a microservice that mostly talks to other services through events instead of direct calls. It reacts to events it subscribes to, updates its own database, and publishes events about its own changes.

Each such service owns its data, and other services keep the parts they need as local copies built from events.

## 92: Can a monolith be event-driven?

Yes. A monolith can use an in-process event bus so modules react to each other's events without direct calls. For example, the orders module publishes `OrderPlaced`, and the loyalty module adds points.

This keeps modules loosely coupled and makes it easier to split them into services later. You still need to think about what happens if the process crashes between saving data and running handlers.

## 93: How do serverless platforms support event-driven architecture?

Serverless functions are triggered by events by design. In AWS, a Lambda function can run when a message lands in SQS, a file is uploaded to S3, a row changes in DynamoDB (through DynamoDB Streams) or an event matches an EventBridge rule.

You don't manage servers or consumers. The platform scales functions up and down with the number of events. You still need to handle retries, duplicates and failures.

## 94: What is Amazon EventBridge?

Amazon EventBridge is a serverless event bus in AWS. Producers send events to a bus, and rules match events by their content (like `source` and `detail-type`) and route them to targets such as Lambda, SQS, Step Functions or HTTP endpoints.

It also receives events from many AWS services and some SaaS partners, and has a schema registry and archive and replay features.

## 95: How does the SNS and SQS fan-out pattern work?

You publish an event to one SNS topic. Several SQS queues subscribe to that topic, one per consumer service. SNS copies the event into each queue.

Each service reads from its own queue at its own pace. If one service is down, its messages wait in its queue, and other services are not affected. You can also add a filter policy so each queue gets only the events it needs.

## 96: What is AsyncAPI?

AsyncAPI is a specification for describing event-driven APIs, similar to what OpenAPI does for REST APIs. You describe channels (topics), the messages sent on them and their schemas in a YAML or JSON file.

From that file, tools can generate documentation and code. It helps teams see what events exist and what they look like.

## 97: What is CloudEvents?

CloudEvents is a CNCF specification for a common format of event metadata. It defines standard attributes like `id`, `source`, `type`, `specversion`, `time` and `datacontenttype`, and how to map them to HTTP, Kafka, AMQP and other protocols.

Using it makes events from different systems look the same, so tools and routers can handle them without custom code for each producer.

## 98: What is the difference between event time and processing time?

**Event time** is when the event actually happened, for example when the user clicked "buy". **Processing time** is when a consumer handles it, which can be seconds or hours later.

For reports and business logic you usually want event time. For example, a sale that happened at 23:59 belongs to that day even if it was processed at 00:01.

## 99: How do you test a simple event handler?

Call the handler directly with a fake event and check the result, using test doubles for outside dependencies.

```ts
import { test } from "node:test";
import assert from "node:assert/strict";

test("sends confirmation email on OrderPlaced", async () => {
  const sent: string[] = [];
  const email = { send: async (to: string) => void sent.push(to) };
  const handler = new OrderPlacedHandler(email);

  await handler.handle({
    id: "e1",
    type: "OrderPlaced",
    data: { customerEmail: "a@b.com" },
  });

  assert.deepEqual(sent, ["a@b.com"]);
});
```

You can also test that handling the same event twice sends only one email.

## 100: Is a database read replica the same as a CQRS read model?

No. A read replica is an exact copy of the same database with the same tables. It helps scale reads, but the data has the same shape as the write side.

A CQRS read model has its own shape, built for queries. It can be a different table, a different database or a search index. A read replica can be part of a CQRS setup, but it's not the whole idea.

## 101: What is the difference between a background job and an event?

A **background job** is a task you want done later, like "resize this image" or "send this email". It's a command put on a queue, and one worker should do it.

An **event** is a fact that something happened, like "image uploaded". Any number of services can react to it.

A common flow uses both: the upload service publishes `ImageUploaded`, and the image service reacts by putting a `ResizeImage` job on its own work queue.

## 102: What does fire and forget mean?

Fire and forget means you send a message and don't wait for any response or confirmation that it was processed. Publishing events usually works like this from the producer's point of view.

It's fine for events, but you should still make sure the broker actually received the message, for example by waiting for the broker's acknowledgment or using an outbox. Otherwise "forget" can turn into "lost".

## 103: What happens to events when a consumer is down?

With a durable broker, the events wait. In a queue they stay until a consumer takes them. In Kafka they stay in the topic, and the consumer group continues from its last committed offset when it comes back.

The consumer then has a backlog to work through, so lag goes up for a while. If it's down longer than the retention time or message TTL, events can be lost, so retention must be longer than any expected outage.

## 104: What is message durability?

Durability means a message survives a broker restart or crash. The broker writes it to disk, and often copies it to other broker nodes, before confirming to the producer.

In RabbitMQ you need a durable queue (quorum queues are the usual choice today) and persistent messages. In Kafka you set a replication factor above one and use `acks=all` on the producer. Without durability, events can disappear when a server restarts.

## 105: What is a policy (or reactor) in event-driven design?

A policy is a rule of the form "when this event happens, do that". For example, "when `PaymentFailed`, send `NotifyCustomer`" or "when `OrderPlaced`, send `ReserveStock`".

In code it's an event handler that sends commands. It contains business logic about what should happen next, as opposed to a projection, which only updates a read model.

## 106: What is temporal coupling?

Temporal coupling means two services must both be running at the same time for something to work. With a direct HTTP call, if the receiving service is down, the call fails.

Async messaging removes temporal coupling. The producer can publish while the consumer is down, and the consumer processes the message when it comes back.

## 107: How can a UI see read model changes without refreshing?

The server pushes updates to the browser when the read model changes, usually with WebSockets or Server-Sent Events (SSE). A projection updates the read model and then also sends a message to connected clients.

Simpler options are polling the API every few seconds, or refetching after a command succeeds. Push is nicer for live dashboards, chat or order tracking.

## 108: What is event storming?

Event storming is a workshop technique by Alberto Brandolini. Developers and business people stand at a long wall and put sticky notes for every domain event they can think of, like "Order placed" or "Payment refunded", in time order.

Then they add commands, actors, policies, read models and problem areas. It's a fast way to understand a business process and find the events and boundaries for an event-driven design.

## 109: What is a process manager?

A process manager is a component that keeps track of a long business process and decides what to do next based on events it receives. It has its own state, like "payment done, waiting for stock".

For each event it updates its state and may send new commands. Many people use "process manager" and "orchestrated saga" for nearly the same thing.

## 110: What happens when a command is rejected?

The command handler doesn't change anything and returns an error, for example "order already shipped". No event is stored or published, since nothing happened.

If the command came from an API, the client gets an error response like 409 or 422. If it came from a queue, it's either logged as a business failure or answered with a failure event like `OrderCancellationRejected` if someone needs to know.

## 111: What is optimistic concurrency?

Optimistic concurrency is a way to stop two users from overwriting each other's changes without locking. Each record has a version number. When you save, you say "save only if the version is still the one I read".

If someone else saved in between, the version doesn't match, the save fails, and you retry or show an error. It works well when conflicts are rare.

## 112: What is an expected version in event sourcing?

When you append events to a stream, you pass the version you expect the stream to be at, the version you had when you loaded the aggregate. If the stream has moved on because someone else added events, the append fails.

```ts
await eventStore.append("order-o-1001", newEvents, { expectedVersion: 5 });
```

This is optimistic concurrency for event streams. It makes sure business rules were checked against the latest state.

## 113: Does CQRS require two databases?

No. You can keep the write tables and read tables in the same database, and even update them in the same transaction. That gives you strong consistency and is much simpler to run.

You move the read model to a separate database only when you need it, for example for search, for very different scaling needs or when it belongs to another service.

## 114: What does it mean to rebuild a read model?

You delete the read model data and run the projection again over all events from the start. At the end the read model matches what the events say, with the latest projection code.

You do it after fixing a projection bug, after changing the read model's shape or when creating a brand new read model. It needs all events to be stored, so it works naturally with event sourcing or long Kafka retention.

## 115: Why have one read model per screen or use case?

Each screen needs different data. An order list needs ids, dates, totals and status. An order details page needs lines, addresses and history. A dashboard needs counts.

If each one has its own read model, each query is a simple lookup with no joins, and changing one screen doesn't affect the others. The cost is more projections to maintain, so don't split further than you need.

## 116: What is the difference between a thin event and a fat event?

A **thin event** carries only ids and the minimum needed: `{ "type": "OrderPlaced", "orderId": "o-1" }`. Consumers call back to get details.

A **fat event** carries all relevant data: customer, lines, totals, address. Consumers don't need to call back.

Thin events keep the contract small but add calls and load. Fat events remove calls but make the contract bigger and harder to change. Most teams use something in between: what consumers usually need, not everything.

## 117: Why should events be kept reasonably small?

Brokers have size limits. Kafka's default maximum message size is about 1 MB, SQS and SNS allow 256 KB, and EventBridge also allows 256 KB per entry. Big messages are also slower to send, store and process.

If you need to share a large file or document, store it in object storage like S3 and put only a link in the event. This is called the claim check pattern.

## 118: What is a schema registry?

A schema registry is a service that stores the schemas of your events with versions. Producers register a schema and add its id to each message. Consumers use the id to fetch the right schema and read the message.

It can also check every new schema version against compatibility rules, so a breaking change is rejected before it goes to production. Confluent Schema Registry, Apicurio and AWS Glue Schema Registry are common ones.

## 119: What does backward compatibility mean for events?

A schema change is backward compatible if consumers using the new schema can still read events written with the old schema. For example, adding a new optional field with a default value is backward compatible.

Removing a required field or changing a field's type usually breaks compatibility. Since old events stay in storage and old producers may still run, events should change in compatible ways whenever possible.

## 120: What is a message key?

A message key is a value attached to a message that the broker uses for routing. In Kafka, the key decides which partition a message goes to, so all messages with the same key stay in order.

You usually pick the id of the entity the event is about, like the order id or account id. In SQS FIFO the similar idea is the message group id.

## 121: What is a delayed message?

A delayed message is one that should only be delivered after some time. For example, "send a reminder if the cart is still not paid after 24 hours".

Support differs: SQS has a delay of up to 15 minutes, Azure Service Bus has scheduled messages, and RabbitMQ needs a plugin or TTL plus a dead letter exchange. For long delays, many teams store the due time in a database and run a scheduler, or use a workflow engine.

## 122: How do events help with auditing?

If every change is recorded as an event with who did it and when, you get an audit trail for free. You can answer questions like "who changed this price and what was it before?".

With event sourcing, the audit log is the actual data, so it can't be out of sync with the state. Without event sourcing, you can still store published events in a log or warehouse for audit.

## 123: What is distributed tracing, and why is it useful in event-driven systems?

Distributed tracing follows one request as it moves through many services. Each step creates a span, and spans share a trace id, so a tool like Jaeger, Tempo or a commercial APM can show the full path and timing.

In event-driven systems the path goes through brokers, so the producer adds trace context (usually the W3C `traceparent` header) to message headers, and the consumer continues the trace from it. OpenTelemetry has libraries that do this for most brokers.

## 124: What is a long-running process?

It's a business process that takes minutes, days or weeks and involves several steps, like an order that waits for payment, then shipping, then delivery confirmation, or a loan application waiting for approval.

You can't keep a database transaction or HTTP request open that long. Instead, you store the process state and move it forward as events arrive, using a saga, a process manager or a workflow engine.

## 125: What is the inbox pattern?

The inbox pattern is the consumer-side partner of the outbox. When a message arrives, the consumer first saves its id in an `inbox` table, in the same transaction as the work it does.

If the same message arrives again, the insert fails because the id already exists, and the consumer skips it. This makes processing idempotent even if the broker delivers duplicates.

## 126: What is message deduplication?

Deduplication means detecting and dropping messages that were already received. It's done by keeping track of message ids, either in the broker or in the consumer.

Some brokers help: SQS FIFO drops duplicates with the same deduplication id within 5 minutes, and Kafka's idempotent producer prevents duplicates caused by producer retries. Consumers should still be idempotent, because broker deduplication only covers some cases.

## 127: What is the difference between a queue and a log?

In a **queue**, a message is removed once it's acknowledged. Each message is processed by one consumer, and you can't go back.

In a **log**, messages stay for a retention period, even after they are read. Each consumer group keeps its own position and can rewind to read again.

RabbitMQ classic and quorum queues and SQS are queues. Kafka, Pulsar, RabbitMQ streams and Redis Streams are logs.

## 128: Can you replay events in Kafka and RabbitMQ?

In Kafka, yes. Events stay in the topic for the retention period, so a consumer group can reset its offset to an earlier point or to the beginning and read again.

In RabbitMQ queues, no. Once a message is acked, it's gone. RabbitMQ streams do keep messages and allow reading from an offset, similar to Kafka. If you need replay with a classic queue setup, you have to store events somewhere else too.

## 129: Give examples of events in an e-commerce system.

- `CustomerRegistered`, `CustomerAddressChanged`
- `ProductAddedToCart`, `CartAbandoned`
- `OrderPlaced`, `OrderCancelled`
- `PaymentAuthorized`, `PaymentFailed`, `RefundIssued`
- `StockReserved`, `StockReleased`, `ItemOutOfStock`
- `ShipmentDispatched`, `ShipmentDelivered`

From `OrderPlaced` alone, payment, inventory, email, analytics and a fraud check can all start their own work.

## 130: What are common beginner mistakes with events and CQRS?

- Publishing events after the database commit without an outbox, so events get lost on crashes.
- Writing consumers that are not idempotent.
- Using CQRS and event sourcing for every simple CRUD screen.
- Naming events like database operations: `OrderUpdated` with the whole row.
- Assuming events arrive in order across different keys or topics.
- Forgetting that the read model is stale for a moment, so the UI looks broken right after a save.
- No correlation ids, so nobody can debug a flow.

## 131: How should commands be named?

Commands should be named as imperative verbs in business language: `PlaceOrder`, `ApproveLoan`, `ChangeEmail`, `CancelBooking`. The name should say what the user wants, not how data changes.

Avoid generic names like `UpdateOrder`. A specific command makes the intent clear, is easier to validate and leads to a clear event like `OrderCancelled`.

## 132: What are message headers used for?

Headers are key-value pairs sent with a message, separate from the body. They carry metadata that infrastructure and consumers need without parsing the body, such as:

- event type and schema version,
- correlation id and causation id,
- trace context (`traceparent`),
- content type,
- tenant id.

Kafka, RabbitMQ, SQS (message attributes) and most other brokers support headers.

## 133: What is content-based filtering?

Content-based filtering means a subscriber only receives events whose content matches some rules, instead of every event on a topic. For example, a queue only wants `OrderPlaced` events where `country` is `DE`.

SNS filter policies and EventBridge rules support this. It saves consumers from receiving and ignoring lots of events they don't care about.

## 134: What is a routing key in RabbitMQ?

A routing key is a string a producer attaches to a message when sending it to an exchange. The exchange uses it to decide which queues get the message.

With a topic exchange, queues bind with patterns like `order.*` or `order.#`, so a message with routing key `order.placed` goes to every queue whose pattern matches. This is how RabbitMQ does pub/sub with filtering.

## 135: What are competing consumers?

Competing consumers are several instances of the same consumer reading from the same queue. Each message goes to only one of them, so they share the work.

It's the usual way to scale processing: if one instance can handle 100 messages per second and you need 500, you run five. The trade-off is that ordering between messages is lost unless you partition by key.

## 136: Why do brokers keep copies of data on several servers?

So that losing one server doesn't lose messages or stop the system. Kafka replicates each partition to several brokers, and RabbitMQ quorum queues replicate to several nodes using the Raft protocol.

The producer is told "saved" only after enough copies exist. If the leader server dies, another copy takes over.

## 137: How do you handle a deadline in an event-driven process?

You schedule a check for when the deadline passes. For example, when `OrderPlaced` arrives, the saga schedules "check payment in 30 minutes". When that time comes, if payment hasn't arrived, it cancels the order.

You can use delayed messages, a database table with due times checked by a scheduler, or timer features of a workflow engine like Temporal or AWS Step Functions.

## 138: Can you send commands through a broker?

Yes. You can put a command on a queue so that one specific service carries it out later, like `GenerateInvoice` on the billing queue. This is common in orchestrated sagas and for background work.

The difference from events is that a command goes to one known receiver, and the sender expects it to be done. Use a queue, not a pub/sub topic, so only one consumer handles it.

## 139: Why does every event need a unique id?

The id lets consumers detect duplicates: if they've seen this id before, they skip it. It also lets you find a specific event in logs, link events through causation ids and trace a problem back to one message.

Use a UUID (v4 or v7) or a similar unique value, generated once when the event is created and never changed on retries.

## 140: How is event-driven processing different from batch processing?

Batch processing collects data and handles it all at once on a schedule, like a nightly job that calculates sales totals. Results are only as fresh as the last run.

Event-driven processing handles each event as soon as it arrives, so results are fresh within seconds. Batch is simpler and good for heavy reports. Event-driven is better when you need quick reactions.

## 141: What is an offset in Kafka?

An offset is the position number of a message inside a partition. The first message is 0, the next is 1, and so on.

A consumer group commits the offset it has processed up to. After a restart, it continues from that point. Resetting the offset to an earlier value is how you replay events.

## 142: What is the visibility timeout in Amazon SQS?

When a consumer receives a message from SQS, the message isn't deleted. It's hidden from other consumers for the visibility timeout (30 seconds by default).

If the consumer deletes the message within that time, it's done. If not, for example because it crashed, the message becomes visible again and another consumer gets it. Set the timeout longer than your normal processing time, or you'll get duplicates.

## 143: What is the difference between strong and eventual consistency?

With **strong consistency**, after a write finishes, every read sees it. A single database transaction gives you this.

With **eventual consistency**, reads may return old data for a short time after a write, but all copies agree in the end.

Event-driven systems are mostly eventually consistent between services. Inside one service and one database you can still have strong consistency where you need it.

## 144: What does "source of truth" mean in an event-sourced system?

It means the event store holds the real, official data. Everything else, like read models, caches and search indexes, is derived from the events and can be rebuilt from them.

If a read model and the events disagree, the events are right and the read model has a bug or is behind.

## 145: How is CQRS different from a standard CRUD design?

In CRUD, one model and usually one set of tables is used for creating, reading, updating and deleting. The same entity class is loaded for a list page and for an update.

In CQRS, writes go through commands and a model built for business rules, while reads go through queries and models built for display. This adds code, but each side can change and scale on its own.

## 146: What is event retention?

Retention is how long a broker keeps events. Kafka keeps them for a configured time (7 days by default) or until a size limit, whether consumers read them or not. Queues keep messages until they are processed or their TTL runs out.

Retention decides how long consumers can be down without losing data and how far back you can replay. Event stores used for event sourcing keep events forever.

## 147: What should happen if an event handler fails halfway?

Ideally nothing should be left half done. Keep the handler's work in one database transaction where possible, so either everything is saved or nothing is. Then don't ack the message, so it's retried.

If the handler calls several outside systems, make each step idempotent so a retry can safely run the whole handler again.

## 148: Why is sharing one database between services a problem, and how do events help?

If many services read and write the same tables, a schema change in one service can break the others, and nobody really owns the data. You end up with tight coupling through the database.

With events, each service owns its own database. Other services get the data they need from events and store their own copy, in the shape they need.

## 149: How can an order status be driven by events?

The order's status changes only as a reaction to events, following allowed transitions, like a state machine:

```ts
type Status = "placed" | "paid" | "shipped" | "cancelled";

function apply(status: Status, eventType: string): Status {
  if (status === "placed" && eventType === "PaymentCompleted") return "paid";
  if (status === "paid" && eventType === "OrderShipped") return "shipped";
  if (status !== "shipped" && eventType === "OrderCancelled")
    return "cancelled";
  return status; // ignore events that don't apply in this state
}
```

The current status is always the result of the events that happened, which makes it easy to explain and debug.

## 150: How would you explain CQRS to a non-technical person?

Think of a restaurant. Waiters take orders and pass them to the kitchen, where cooks follow recipes and rules. That's the write side. The menu on the wall is what guests read. It's printed in a simple form and changed after the kitchen decides on new dishes. That's the read side.

The guest doesn't read the kitchen's recipe book to choose food, and the kitchen doesn't cook from the menu. Each side is built for its own job, and the menu might be a little behind for a short while.

# Moderate Questions (151-300)

## 151: What is the dual write problem?

The dual write problem happens when one operation has to write to two systems that don't share a transaction, like your database and a broker:

```ts
await db.query("INSERT INTO orders ...");
await broker.publish("OrderPlaced", order); // what if the app crashes here?
```

If the app crashes between the two calls, the order exists but no event is sent. If you publish first and the insert fails, consumers react to an order that doesn't exist. Retrying doesn't fully fix it. The outbox pattern or change data capture are the usual solutions.

## 152: How do you implement the transactional outbox in PostgreSQL?

Save the event in an outbox table in the same transaction as the business data:

```sql
CREATE TABLE outbox (
  id           uuid PRIMARY KEY,
  aggregate_id text        NOT NULL,
  type         text        NOT NULL,
  payload      jsonb       NOT NULL,
  created_at   timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz
);
```

```ts
const client = await pool.connect();
try {
  await client.query("BEGIN");
  await client.query(
    "INSERT INTO orders (id, customer_id, total) VALUES ($1, $2, $3)",
    [order.id, order.customerId, order.total],
  );
  await client.query(
    "INSERT INTO outbox (id, aggregate_id, type, payload) VALUES ($1, $2, $3, $4)",
    [randomUUID(), order.id, "OrderPlaced", JSON.stringify(order)],
  );
  await client.query("COMMIT");
} catch (err) {
  await client.query("ROLLBACK");
  throw err;
} finally {
  client.release();
}
```

A separate relay then reads unpublished rows, sends them to the broker and marks them as published.

## 153: How does an outbox relay work, and what are the options?

There are two common ways to move outbox rows to the broker:

- **Polling**: a worker runs every few hundred milliseconds, selects unpublished rows in order, publishes them and marks them as sent. Simple and works with any database, but adds load and some delay.
- **Change data capture**: a tool like Debezium reads the database's transaction log and publishes new outbox rows as they are committed. Lower delay and no polling, but one more component to run.

Both give at-least-once delivery. If the relay crashes after publishing but before marking a row, the event is sent again, so consumers must be idempotent.

## 154: How do you write a simple polling outbox relay?

```ts
async function relayOnce(pool: Pool, publish: (e: OutboxRow) => Promise<void>) {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    const { rows } = await client.query<OutboxRow>(
      `SELECT * FROM outbox
       WHERE published_at IS NULL
       ORDER BY created_at
       LIMIT 100
       FOR UPDATE SKIP LOCKED`,
    );
    for (const row of rows) {
      await publish(row); // wait for the broker's ack
      await client.query(
        "UPDATE outbox SET published_at = now() WHERE id = $1",
        [row.id],
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

`FOR UPDATE SKIP LOCKED` lets several relay instances run without picking the same rows, but then strict order across instances is not guaranteed. Clean up old published rows with a scheduled delete.

## 155: How do you make a consumer idempotent with a processed-messages table?

Record the event id in the same transaction as the work. If the id already exists, skip the event.

```ts
async function handle(event: OrderPlaced) {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    const res = await client.query(
      "INSERT INTO processed_events (event_id) VALUES ($1) ON CONFLICT DO NOTHING",
      [event.id],
    );
    if (res.rowCount === 0) {
      await client.query("ROLLBACK");
      return; // already handled
    }
    await client.query(
      "INSERT INTO loyalty_points (customer_id, points) VALUES ($1, $2)",
      [event.data.customerId, Math.floor(event.data.total)],
    );
    await client.query("COMMIT");
  } catch (err) {
    await client.query("ROLLBACK");
    throw err;
  } finally {
    client.release();
  }
}
```

The unique key on `event_id` also protects you if two instances process the same event at the same time.

## 156: How do idempotency keys work for commands sent over HTTP?

The client generates a unique key for each logical operation and sends it in a header, often `Idempotency-Key`. The server stores the key with the result of the first request. If the same key comes again, it returns the stored result instead of running the command again.

This protects against double clicks and client retries after a timeout. Stripe's API is a well-known example. Store the key with a unique constraint, and keep keys for a limited time, like 24 hours.

## 157: How do you implement retries with exponential backoff and jitter?

Wait longer after each failure, and add some randomness so many consumers don't retry at the same moment:

```ts
async function withRetry<T>(fn: () => Promise<T>, maxAttempts = 5): Promise<T> {
  for (let attempt = 1; ; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt >= maxAttempts || !isTransient(err)) throw err;
      const base = 200 * 2 ** (attempt - 1); // 200, 400, 800, 1600 ms
      const delay = Math.random() * base; // "full jitter"
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}
```

Only retry errors that might go away, like timeouts. Retrying a validation error just wastes time. After the last attempt, send the message to a dead letter queue.

## 158: How should you handle messages in a dead letter queue?

- Alert when the DLQ is not empty, so failures don't go unnoticed.
- Keep the original message plus error details, attempt count and the time it failed.
- Find the cause: a bug, bad data or a downstream outage.
- Fix the cause first, then move the messages back to the main queue (SQS calls this a redrive).
- Make sure the consumer is idempotent before redriving, since some messages may have been partly processed.

Don't just delete DLQ messages. Each one is a business action that didn't happen.

## 159: How do you keep events for the same entity in order?

Send all events for one entity through the same ordered lane:

- In Kafka, use the entity id as the message key so they go to the same partition.
- In SQS FIFO, use the entity id as the `MessageGroupId`.
- In Azure Service Bus, use sessions with the entity id as the session id.

Inside each lane, process messages one at a time. Different entities can still be processed in parallel, which keeps throughput high.

## 160: How do you handle events that arrive out of order?

Give each event a version or sequence number per entity. The consumer stores the last version it applied and checks new events against it:

```sql
UPDATE order_view
SET status = $2, version = $3
WHERE id = $1 AND version < $3;
```

If an older event arrives after a newer one, the update matches no rows and is ignored. If an event arrives too early (a gap in versions), the consumer can retry later or put it aside until the missing one arrives.

## 161: How do you design an event envelope?

Use a consistent wrapper for all events so infrastructure code can handle them the same way, and keep business data in a separate field:

```ts
interface EventEnvelope<T> {
  id: string; // unique, used for dedup
  type: string; // "OrderPlaced"
  version: number; // schema version of data
  occurredAt: string; // ISO timestamp, event time
  source: string; // producing service
  subject: string; // entity id, e.g. order id
  correlationId: string;
  causationId?: string;
  data: T;
}
```

This is close to CloudEvents, which you can use directly if you want a standard format.

## 162: What strategies exist for versioning events?

- **Add only optional fields.** Old consumers ignore them, new ones handle missing values. This covers most changes.
- **New event type.** For a real change in meaning, publish `OrderPlacedV2` or a new name, and keep the old one for a while.
- **Upcasting.** Store old events as they are, and convert them to the new shape when reading.
- **Copy and transform.** Rewrite the whole stream into a new one with the new shape. Rare and heavy.
- **Weak schema.** Consumers read fields by name and use defaults when missing.

Pick the simplest option that keeps old events readable.

## 163: What is upcasting?

Upcasting means converting an old version of an event into the current version at the time you read it. The stored event doesn't change.

```ts
function upcast(e: StoredEvent): StoredEvent {
  if (e.type === "OrderPlaced" && e.version === 1) {
    return {
      ...e,
      version: 2,
      data: { ...e.data, amount: e.data.price, currency: "EUR" },
    };
  }
  return e;
}
```

The rest of the code only knows the latest version. Upcasters can be chained: v1 to v2, then v2 to v3.

## 164: How do Avro compatibility rules affect event changes?

With Avro and a schema registry:

- Adding a field is backward compatible only if it has a default value.
- Removing a field is forward compatible only if it had a default.
- Renaming a field breaks things unless you use aliases.
- Changing a type is usually breaking, except for some allowed promotions like `int` to `long`.

The registry can enforce a mode such as `BACKWARD`, `FORWARD` or `FULL`, and reject a new schema version that breaks it.

## 165: How do you choose between event notification and event-carried state transfer?

Use **event notification** (thin events) when:

- consumers rarely need the details,
- the data is large or sensitive,
- consumers must always use the latest data anyway.

Use **event-carried state transfer** (fat events) when:

- many consumers need the same data,
- you don't want consumers to depend on the producer being up,
- consumers keep a local copy for fast reads.

Many systems use both, depending on the event.

## 166: How do you write a projection that updates a read model?

Handle each event type and update the read table, keeping it idempotent:

```ts
async function project(event: EventEnvelope<any>, db: Pool) {
  switch (event.type) {
    case "OrderPlaced":
      await db.query(
        `INSERT INTO order_summary (id, customer_id, total, status, version)
         VALUES ($1, $2, $3, 'placed', $4)
         ON CONFLICT (id) DO NOTHING`,
        [
          event.subject,
          event.data.customerId,
          event.data.total,
          event.data.streamVersion,
        ],
      );
      break;
    case "OrderShipped":
      await db.query(
        `UPDATE order_summary SET status = 'shipped', version = $2
         WHERE id = $1 AND version < $2`,
        [event.subject, event.data.streamVersion],
      );
      break;
    default:
    // ignore events this projection doesn't need
  }
}
```

## 167: How does a projection know where it stopped?

It stores a checkpoint: the position of the last event it processed, like a global position in the event store or an offset in Kafka. After a restart it reads from that position.

The safest way is to save the checkpoint in the same transaction as the read model update. Then the checkpoint and the data never disagree, even after a crash.

## 168: How do you rebuild a read model without downtime?

Use a blue-green approach:

1. Create a new table or index, like `order_summary_v2`.
2. Run the new projection from the first event into it, while the old one keeps serving queries.
3. When the new one catches up with live events, switch queries to it (change a view, an alias or a config value).
4. Drop the old one after a while.

Elasticsearch aliases and PostgreSQL views make the switch a quick, atomic step.

## 169: What is read-your-own-writes, and how do you get it in CQRS?

Read-your-own-writes means a user always sees their own changes right after making them, even if other users see them a bit later.

Ways to get it:

- Return the new state or version from the command and use it in the UI.
- Pass the expected version to the query and wait (with a timeout) until the read model reaches it.
- Read from the write model for that one user's own data right after a change.
- Update the read model in the same transaction for the data that needs it.

## 170: How do you handle eventual consistency in the UI?

- **Optimistic UI**: show the change right away, based on what the user sent, and fix it if the command fails.
- **Show progress**: "Your order is being processed" with a status that updates later.
- **Push updates** with WebSockets or SSE when the read model changes.
- **Poll** until the expected version appears.
- **Design the flow** so the user doesn't immediately need the updated data, for example redirect to a confirmation page that doesn't need the read model.

Talk with product people early. Many "consistency" problems are solved by a small change in the UI.

## 171: What is the difference between command validation and domain invariants?

Command validation checks the command itself, without the current state: is the email in a valid format, is the quantity positive, is the id present. It can be done before loading anything.

Domain invariants are rules that must always be true for the aggregate, based on its state: an order can't have more than 50 lines, an account balance can't go below zero. Only the aggregate can check these, because only it knows the current state.

## 172: How big should an aggregate be?

As small as possible while still protecting the rules that must be checked together in one transaction. Large aggregates cause more concurrency conflicts, load slowly and lock more than needed.

A common guideline: one aggregate per transaction, and other aggregates are referenced by id, not loaded together. Rules that span aggregates are handled with eventual consistency, like a policy or saga.

## 173: How do you implement an event-sourced aggregate in TypeScript?

The aggregate records new events and changes its state only by applying events:

```ts
type AccountEvent =
  | { type: "AccountOpened"; data: { id: string } }
  | { type: "MoneyDeposited"; data: { amount: number } }
  | { type: "MoneyWithdrawn"; data: { amount: number } };

class Account {
  id = "";
  balance = 0;
  version = 0;
  pending: AccountEvent[] = [];

  withdraw(amount: number) {
    if (amount <= 0) throw new Error("Amount must be positive");
    if (amount > this.balance) throw new Error("Insufficient funds");
    this.raise({ type: "MoneyWithdrawn", data: { amount } });
  }

  deposit(amount: number) {
    if (amount <= 0) throw new Error("Amount must be positive");
    this.raise({ type: "MoneyDeposited", data: { amount } });
  }

  private raise(e: AccountEvent) {
    this.apply(e);
    this.pending.push(e);
  }

  apply(e: AccountEvent) {
    if (e.type === "AccountOpened") this.id = e.data.id;
    if (e.type === "MoneyDeposited") this.balance += e.data.amount;
    if (e.type === "MoneyWithdrawn") this.balance -= e.data.amount;
  }
}
```

Methods check rules and raise events. `apply` only changes state and never throws.

## 174: How do you load an event-sourced aggregate?

Read its stream and apply every event in order:

```ts
async function loadAccount(store: EventStore, id: string): Promise<Account> {
  const events = await store.readStream(`account-${id}`);
  const account = new Account();
  for (const e of events) {
    account.apply(e);
    account.version++;
  }
  return account;
}
```

Then you call a command method, and save the `pending` events with `expectedVersion = account.version`. If you use snapshots, start from the latest snapshot and read only the events after it.

## 175: How do you save events with optimistic concurrency in PostgreSQL?

Use a unique constraint on stream id and version. If two writers try to add the same version, one gets a unique violation.

```sql
CREATE TABLE events (
  global_position bigserial PRIMARY KEY,
  stream_id       text        NOT NULL,
  version         int         NOT NULL,
  type            text        NOT NULL,
  data            jsonb       NOT NULL,
  metadata        jsonb       NOT NULL DEFAULT '{}',
  created_at      timestamptz NOT NULL DEFAULT now(),
  UNIQUE (stream_id, version)
);
```

```ts
async function append(
  client: PoolClient,
  streamId: string,
  expectedVersion: number,
  events: NewEvent[],
) {
  let v = expectedVersion;
  for (const e of events) {
    v++;
    await client.query(
      "INSERT INTO events (stream_id, version, type, data) VALUES ($1, $2, $3, $4)",
      [streamId, v, e.type, JSON.stringify(e.data)],
    );
  }
}
```

Run it in a transaction. On error code `23505` (unique violation), reload the aggregate and retry the command, or return a conflict error.

## 176: When should you use snapshots?

Only when loading aggregates is measurably slow because their streams are long. Many aggregates have tens of events, and replaying them is fast enough.

If you add snapshots, save one every N events (like every 100), store the stream version with it, and version the snapshot format. If the aggregate's code changes in a way that affects state, delete old snapshots and let them be rebuilt. Often, a very long stream is a sign the aggregate should be split or the stream should be "closed" periodically.

## 177: How does a choreography-based saga work for an order?

1. Order service saves the order as pending and publishes `OrderPlaced`.
2. Payment service handles it, charges the card and publishes `PaymentCompleted` or `PaymentFailed`.
3. Inventory service handles `PaymentCompleted`, reserves stock and publishes `StockReserved` or `StockReservationFailed`.
4. Order service handles `StockReserved` and marks the order confirmed.
5. On `StockReservationFailed`, payment service refunds and publishes `PaymentRefunded`, and order service marks the order cancelled.

No service controls the whole flow. Each one only knows which events it reacts to.

## 178: How do you build an orchestrated saga?

An orchestrator holds the saga state and sends commands step by step:

```ts
class OrderSaga {
  constructor(
    private bus: CommandBus,
    private repo: SagaRepository,
  ) {}

  async onOrderPlaced(e: OrderPlaced) {
    await this.repo.save({ orderId: e.data.orderId, step: "charging" });
    await this.bus.send(new ChargePayment(e.data.orderId, e.data.total));
  }

  async onPaymentCompleted(e: PaymentCompleted) {
    await this.repo.update(e.data.orderId, { step: "reserving" });
    await this.bus.send(new ReserveStock(e.data.orderId));
  }

  async onStockReservationFailed(e: StockReservationFailed) {
    await this.repo.update(e.data.orderId, { step: "compensating" });
    await this.bus.send(new RefundPayment(e.data.orderId));
    await this.bus.send(new CancelOrder(e.data.orderId));
  }
}
```

The saga state must be saved durably, and sending commands should go through an outbox so a crash doesn't leave the saga stuck.

## 179: Is a compensating action always an exact undo?

No. Some steps can't be undone. An email that was sent stays sent, and a shipped package is already on a truck. Compensation is whatever the business considers the right correction: a refund, a "sorry, your order was cancelled" email, a return label.

When designing a saga, put steps that are hard to compensate as late as possible, after the steps that are likely to fail.

## 180: What is the difference between a process manager and a choreographed saga?

In a choreographed saga, the logic is spread across services. Each one reacts to events and nobody holds the full state of the process.

A process manager is one component with its own stored state that receives events and decides which commands to send next. It's the orchestration style. It makes the process visible in one place and easier to change, but it's one more thing to build and run.

## 181: How do you handle timeouts in a saga?

When the saga starts waiting for something, schedule a timeout message. If the expected event arrives first, cancel or ignore the timeout. If the timeout arrives first, run the failure path, for example cancel the order and release the stock.

The timeout handler must check the current saga state, because the expected event may have arrived just before it. Without timeouts, a lost event can leave a saga waiting forever.

## 182: How do you write a command handler with NestJS CQRS?

```ts
import { CommandHandler, ICommandHandler, EventPublisher } from "@nestjs/cqrs";

export class CancelOrderCommand {
  constructor(public readonly orderId: string) {}
}

@CommandHandler(CancelOrderCommand)
export class CancelOrderHandler implements ICommandHandler<CancelOrderCommand> {
  constructor(
    private readonly repo: OrderRepository,
    private readonly publisher: EventPublisher,
  ) {}

  async execute({ orderId }: CancelOrderCommand) {
    const order = this.publisher.mergeObjectContext(
      await this.repo.findById(orderId),
    );
    order.cancel(); // calls this.apply(new OrderCancelledEvent(...)) inside
    await this.repo.save(order);
    order.commit(); // publishes the collected events to the EventBus
  }
}
```

The controller calls `this.commandBus.execute(new CancelOrderCommand(id))`. Remember that `commit()` publishes in-process only. For other services, write to an outbox.

## 183: How do sagas work in the NestJS CQRS module?

A NestJS saga is a function decorated with `@Saga()` that takes the stream of events and returns a stream of commands, using RxJS:

```ts
import { Injectable } from "@nestjs/common";
import { ICommand, ofType, Saga } from "@nestjs/cqrs";
import { Observable, map } from "rxjs";

@Injectable()
export class OrderSagas {
  @Saga()
  orderPlaced = (events$: Observable<any>): Observable<ICommand> =>
    events$.pipe(
      ofType(OrderPlacedEvent),
      map((e) => new ReserveStockCommand(e.orderId)),
    );
}
```

It's a policy that runs in memory. It doesn't store state, so for long processes that must survive restarts, you need a persistent process manager.

## 184: How do you write a query handler with NestJS CQRS?

```ts
import { IQueryHandler, QueryHandler } from "@nestjs/cqrs";

export class GetOrderQuery {
  constructor(public readonly orderId: string) {}
}

@QueryHandler(GetOrderQuery)
export class GetOrderHandler implements IQueryHandler<GetOrderQuery> {
  constructor(private readonly db: OrderReadRepository) {}

  execute({ orderId }: GetOrderQuery) {
    return this.db.findSummary(orderId);
  }
}
```

The controller calls `this.queryBus.execute(new GetOrderQuery(id))`. The handler reads from the read model and doesn't touch aggregates.

## 185: How do event handlers work in NestJS CQRS?

```ts
import { EventsHandler, IEventHandler } from "@nestjs/cqrs";

@EventsHandler(OrderCancelledEvent)
export class OrderCancelledHandler implements IEventHandler<OrderCancelledEvent> {
  constructor(private readonly mailer: Mailer) {}

  async handle(event: OrderCancelledEvent) {
    await this.mailer.sendCancellation(event.orderId);
  }
}
```

One event can have many handlers. Since the `EventBus` is in memory, errors in a handler don't make the command fail, and events can be lost on a crash. Use it for in-process reactions and an outbox plus broker for anything that must not be lost.

## 186: How does Kafka consumer group rebalancing affect event processing?

When instances join or leave a group, Kafka moves partitions between them. During the move, some or all partitions can pause, and a partition can move to a new instance before the old one has committed its last offsets.

The new owner then starts from the last committed offset and reprocesses some events. So you get duplicates around rebalances. Commit offsets often, handle shutdown gracefully, and make handlers idempotent. Kafka 4.x's new consumer group protocol makes rebalances more incremental, which reduces pauses.

## 187: Why should you commit Kafka offsets only after processing?

If you commit before processing and the consumer crashes, the event is skipped forever (at-most-once). If you commit after processing, a crash means the event is processed again (at-least-once), which is safe with idempotent handlers.

With KafkaJS you can turn off auto commit and commit after the work (Confluent's `@confluentinc/kafka-javascript` sets `autoCommit` in the consumer config instead):

```ts
await consumer.run({
  autoCommit: false,
  eachMessage: async ({ topic, partition, message }) => {
    await handle(JSON.parse(message.value!.toString()));
    await consumer.commitOffsets([
      { topic, partition, offset: (BigInt(message.offset) + 1n).toString() },
    ]);
  },
});
```

The committed offset is the next one to read, which is why you add one.

## 188: How do you publish events with a RabbitMQ topic exchange?

The producer publishes to a topic exchange with a routing key. Each consumer has its own queue bound with a pattern.

```ts
import amqp from "amqplib";

const conn = await amqp.connect("amqp://localhost");
const ch = await conn.createConfirmChannel();
await ch.assertExchange("events", "topic", { durable: true });

// consumer side: own queue, bound by pattern
await ch.assertQueue("billing.order-events", {
  durable: true,
  arguments: { "x-queue-type": "quorum" },
});
await ch.bindQueue("billing.order-events", "events", "order.*");

// producer side
ch.publish("events", "order.placed", Buffer.from(JSON.stringify(event)), {
  persistent: true,
  messageId: event.id,
  contentType: "application/json",
});
await ch.waitForConfirms();
```

Publisher confirms tell you the broker has safely received the message.

## 189: How do SQS FIFO queues help with ordering?

SQS FIFO queues keep messages in order within a message group. You set `MessageGroupId` to the entity id, and SQS delivers messages from one group in order, one batch at a time, while other groups are processed in parallel.

They also drop duplicates with the same `MessageDeduplicationId` within a 5-minute window. FIFO queues have lower throughput limits than standard queues and the queue name must end with `.fifo`. SNS FIFO topics can fan out to SQS FIFO queues.

## 190: How do EventBridge rules match events?

A rule has an event pattern in JSON. EventBridge compares each event with the pattern and sends matching events to the rule's targets.

```json
{
  "source": ["com.shop.orders"],
  "detail-type": ["OrderPlaced"],
  "detail": {
    "total": [{ "numeric": [">", 1000] }],
    "country": ["DE", "AT"]
  }
}
```

This sends only large German and Austrian orders to the target, like a fraud-check Lambda. Patterns can also match on prefixes, existence of fields and more.

## 191: How do you choose between Kafka, RabbitMQ and SQS?

- **Kafka**: high throughput, events stored for replay, many independent consumer groups, stream processing. Heavier to run, unless you use a managed service.
- **RabbitMQ**: flexible routing, work queues, per-message acks, request-reply, lower latency for small volumes. Streams add replay if needed.
- **SQS/SNS**: fully managed, nothing to run, scales automatically, pay per use. Limited ordering (FIFO) and no replay of consumed messages.

Pick based on replay needs, volume, routing complexity, your cloud and what the team can operate.

## 192: How do you test an event-sourced aggregate?

Use the given-when-then style: given past events, when a command runs, then expect new events or an error.

```ts
test("cannot withdraw more than the balance", () => {
  const account = new Account();
  account.apply({ type: "AccountOpened", data: { id: "a1" } });
  account.apply({ type: "MoneyDeposited", data: { amount: 50 } });

  assert.throws(() => account.withdraw(100), /Insufficient funds/);
  assert.equal(account.pending.length, 0);
});

test("withdraw raises MoneyWithdrawn", () => {
  const account = new Account();
  account.apply({ type: "MoneyDeposited", data: { amount: 50 } });

  account.withdraw(20);

  assert.deepEqual(account.pending, [
    { type: "MoneyWithdrawn", data: { amount: 20 } },
  ]);
});
```

These tests are fast, need no database, and read like business rules.

## 193: What is contract testing for events?

Contract testing checks that a producer's events still match what consumers expect, without running both services together. The consumer writes down what it needs from an event, and the producer's build checks it can still produce that.

Pact supports this for messages: consumer tests produce a pact file, and the provider verifies against it. With a schema registry, compatibility checks give similar protection at the schema level.

## 194: How do you integration test event flows?

Run real infrastructure in containers, for example with Testcontainers, which starts Kafka, RabbitMQ or PostgreSQL from your test code. Then:

1. Publish a test event or send a command.
2. Wait until the expected result appears (a row in the read model, a message on another topic), with a timeout.
3. Assert on the result.

Avoid fixed `sleep` calls. Poll for the result until it shows up or the timeout ends. That makes tests both faster and less flaky.

## 195: How do you pass trace context through a broker?

The producer injects the current trace context into message headers, and the consumer extracts it and starts its span as a child or with a link. With OpenTelemetry:

```ts
import { context, propagation, trace } from "@opentelemetry/api";

// producer
const headers: Record<string, string> = {};
propagation.inject(context.active(), headers);
await producer.send({ topic: "orders", messages: [{ key, value, headers }] });

// consumer
const parentCtx = propagation.extract(
  context.active(),
  toStringHeaders(message.headers),
);
await context.with(parentCtx, () =>
  trace
    .getTracer("billing")
    .startActiveSpan("process OrderPlaced", async (span) => {
      try {
        await handle(message);
      } finally {
        span.end();
      }
    }),
);
```

OpenTelemetry instrumentation packages for common clients can do this for you.

## 196: How should you log in an event-driven system?

- Use structured logs (JSON) with fields, not just text.
- Always include the event id, event type, correlation id and the entity id.
- Log when an event is received, when it's done and when it fails, with the attempt number.
- Don't log full payloads with personal data.
- Send logs to one central place so you can search one correlation id across all services.

Good logging is what makes a flow across five services debuggable.

## 197: What metrics should you watch for event consumers?

- **Consumer lag** or queue depth, and how it changes over time.
- **Processing rate** and **error rate** per event type.
- **Processing time** per message (p50, p95, p99).
- **DLQ size** and how fast it grows.
- **Retry count**.
- **End-to-end latency**: time from `occurredAt` to the moment the consumer finished.

Alert on lag that keeps growing and on any messages in the DLQ.

## 198: How do you tell transient errors from permanent ones?

**Transient** errors may go away on retry: timeouts, connection resets, HTTP 503, deadlocks, rate limits.

**Permanent** errors won't: invalid JSON, a missing required field, an unknown customer id, a business rule violation.

Retry transient errors with backoff. Send permanent errors to the DLQ right away. Throw different error classes in your code so the retry logic can decide easily.

## 199: How do retry topics work in Kafka?

Kafka has no built-in delayed redelivery, so a common pattern is to use extra topics: `orders`, `orders.retry.1m`, `orders.retry.10m`, `orders.dlq`. When processing fails, the consumer publishes the message to the next retry topic and commits the original offset.

A retry consumer waits until the message is old enough, then processes it again. This keeps the main topic moving, but it breaks ordering for that entity, so it's not a fit when strict order matters.

## 200: How do you turn domain events into integration events?

Inside the service, handle the domain event and map it to a smaller public event, then write it to the outbox:

```ts
function toIntegrationEvent(e: OrderPlacedDomainEvent): OrderPlacedV1 {
  return {
    orderId: e.order.id,
    customerId: e.order.customerId,
    total: e.order.total.amount,
    currency: e.order.total.currency,
    placedAt: e.occurredAt.toISOString(),
  };
}
```

This keeps internal details like discount rules or internal ids out of the public contract, so you can refactor the domain without breaking other teams.

## 201: What is an anti-corruption layer for events?

An anti-corruption layer is code at the edge of a service that translates events from another system into the service's own terms. For example, a legacy system publishes `CUST_UPD` with odd field names, and the layer turns it into `CustomerAddressChanged` in your own model.

It keeps someone else's model and naming from leaking into your code. If the other system changes its events, you only update the translation layer.

## 202: How fine-grained should events be?

Each event should match one meaningful business change. Too fine, like `OrderLineQuantityFieldChanged`, and consumers have to piece together many events to understand what happened. Too coarse, like `OrderChanged`, and consumers can't tell what actually happened.

A good test: would a business person recognize the event as something that happened? `ItemAddedToOrder`, `ShippingAddressChanged` and `OrderCancelled` pass. `OrderRowUpdated` doesn't.

## 203: Why are CRUD-style events like EntityUpdated considered an anti-pattern?

An `OrderUpdated` event with the full new row tells consumers that something changed, but not what or why. Every consumer has to compare old and new values to guess the meaning, and each one may guess differently.

It also ties consumers to your table structure. Events like `OrderShippingAddressChanged` or `OrderCancelled` carry intent, are easier to handle and survive internal refactoring. CRUD-style events are fine only for simple data sync, like copying reference data.

## 204: What naming conventions work well for events and topics?

- Event types in PascalCase past tense: `OrderPlaced`, `PaymentRefunded`.
- A namespace or source to avoid clashes: `com.shop.orders.OrderPlaced` or a `source` field.
- Topics named by domain and data, not by consumer: `orders.order-events`, not `billing-input`.
- Version in the type or a separate field, used the same way everywhere.

Write the convention down once and check it in code review. Mixed naming across teams gets messy fast.

## 205: Where should event schemas live?

Common options:

- In a **schema registry**, as the single source, with compatibility checks.
- In a **shared contracts repository**, from which each language generates its types.
- In the **producer's repository**, published as a package or AsyncAPI document.

The producer owns its events' schemas. Consumers should depend on the schema, not on the producer's code. Generate types from the schema instead of writing them by hand in every service.

## 206: What is the risk of a shared library for event classes?

If all services import the same library with event classes, every change to it forces updates and redeploys across services, and services start sharing more than just the contract, like helper code or base classes. This can turn microservices into a distributed monolith.

A safer way is to share only schemas (JSON Schema, Avro, Protobuf) and let each service generate or write its own types. Keep any shared library very thin and change it rarely.

## 207: Can you have several read models for the same events?

Yes, and it's one of the main benefits. The same order events can feed:

- an `order_summary` table for the customer's order list,
- an Elasticsearch index for support staff search,
- a daily sales table for reports,
- a Redis key for the live order status.

Each projection reads the same events and builds its own model. Adding a new one doesn't affect the others.

## 208: How do you choose a store for a read model?

Look at the queries the read model has to serve:

- Simple lookups and lists with filters: a relational table.
- Full-text search, fuzzy matching, facets: Elasticsearch or OpenSearch.
- Very fast key lookups or counters: Redis.
- Nested documents read as a whole: a document database.
- Graph traversal like "friends of friends": a graph database.
- Big analytical queries: a data warehouse.

Start with what you already run. Add a new store only when a real query needs it.

## 209: How can PostgreSQL materialized views be used as a simple form of CQRS?

You keep normal tables for writes and create a materialized view shaped for reads:

```sql
CREATE MATERIALIZED VIEW customer_order_stats AS
SELECT c.id, c.name, count(o.id) AS order_count, coalesce(sum(o.total), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name;

CREATE UNIQUE INDEX ON customer_order_stats (id);

REFRESH MATERIALIZED VIEW CONCURRENTLY customer_order_stats;
```

`CONCURRENTLY` lets reads continue during the refresh but needs a unique index. The view is only as fresh as the last refresh, which works well for dashboards and reports without any events or brokers.

## 210: What are the trade-offs of updating the read model in the same transaction as the write?

**Pros**: the read model is always consistent with the write side, there's no lag, and no extra infrastructure.

**Cons**: writes get slower because they also update read tables, a failing projection fails the command, both models must be in the same database, and scaling them separately is harder.

It's a good choice for read models the user needs right after a change. Slower, less critical read models can still be updated asynchronously.

## 211: What is the difference between inline and async projections?

**Inline** projections run as part of saving events, in the same transaction. The read model is always up to date, but writes do more work.

**Async** projections run in the background after events are saved. Writes stay fast, but the read model lags a little.

Marten, an event store library for .NET on PostgreSQL, has both modes (inline, async and live). You can use inline for a few critical views and async for the rest.

## 212: How do you handle the right to be forgotten in an event-sourced system?

Events should not be edited, but laws like the GDPR say you must delete personal data on request. Common solutions:

- **Crypto shredding**: encrypt personal data in events with a key per person, and delete the key when asked. The data becomes unreadable.
- **Keep personal data out of events**: store it in a normal table and put only a reference in the event, then delete the row.
- **Rewrite the stream** with personal data removed, as a last resort.

Read models and backups also need to be cleaned. Talk to your legal team about what "deleted" must mean for you.

## 213: What options exist for an event store?

- **KurrentDB** (formerly EventStoreDB): a database built for event sourcing, with streams, subscriptions and projections.
- **Marten**: a .NET library that uses PostgreSQL as a document and event store.
- **Axon Server**: part of the Axon framework for Java.
- **A PostgreSQL or MySQL table** with a unique constraint on stream and version.
- **DynamoDB** with conditional writes, using the stream id as the partition key and the version as the sort key.

Kafka is often suggested too, but it lacks per-stream optimistic concurrency and fast reads of a single stream, so it's rarely a good event store on its own.

## 214: How do you read events by stream and by global position?

You need two kinds of reads:

```sql
-- load one aggregate
SELECT type, data, version FROM events
WHERE stream_id = $1
ORDER BY version;

-- feed projections with all events after the checkpoint
SELECT global_position, stream_id, type, data FROM events
WHERE global_position > $1
ORDER BY global_position
LIMIT 500;
```

The first needs an index on `(stream_id, version)`, which the unique constraint gives you. The second uses the primary key. Be aware that with a plain sequence, rows can commit out of order, so a reader can miss events. This is covered in the advanced section.

## 215: What are catch-up and persistent subscriptions?

A **catch-up subscription** is driven by the client. The client says "give me events starting at position X", reads the history until it's caught up, then gets live events. The client stores its own checkpoint. Projections usually use this.

A **persistent subscription** (also called a competing consumer subscription) is managed by the server. The server tracks the position and delivers events to a group of clients, with acks and retries, like a queue. It's useful for spreading work but doesn't guarantee strict order.

KurrentDB offers both. Kafka consumer groups are closer to server-tracked catch-up subscriptions.

## 216: How should a command API look in REST?

Name endpoints after the action, especially for actions that aren't simple field changes:

```http
POST /orders                    -> PlaceOrder
POST /orders/o-1001/cancel      -> CancelOrder
POST /orders/o-1001/shipping-address -> ChangeShippingAddress
GET  /orders/o-1001             -> GetOrder (query)
```

Compared to a generic `PATCH /orders/o-1001` with any fields, this keeps the user's intent, makes validation and permissions clear per action, and maps directly to commands and events.

## 217: When should an API return 202 Accepted?

Return `202 Accepted` when the command was received and queued but not processed yet. The response should tell the client how to check the result, like a `Location` header pointing to a status resource:

```http
HTTP/1.1 202 Accepted
Location: /operations/op-7781
```

If the command is processed synchronously before responding, return `200`, `201` or `204` as usual. Don't return 202 just because events are published later, if the command itself already succeeded.

## 218: How does a client learn the result of an async command?

- **Polling**: the client calls a status endpoint until it says done or failed.
- **Push**: the server sends the result through a WebSocket or SSE connection.
- **Callback**: for server-to-server, the client gives a webhook URL to call when done.
- **Wait with timeout**: the API waits a short time for the result, and returns 202 if it isn't ready.

Store the operation status in a small table keyed by an operation id, so all these options can read it.

## 219: How does request-reply work over a message broker?

The requester sends a message with a `replyTo` address (a queue) and a `correlationId`. The responder handles it and sends the answer to the `replyTo` queue with the same `correlationId`. The requester matches replies to pending requests by that id.

RabbitMQ supports this directly, including a "direct reply-to" feature. It's useful when you want queue benefits like load balancing but still need an answer. If you use it everywhere, you get RPC with extra steps, so use it carefully.

## 220: What is the claim check pattern?

When a message would be too large for the broker, you store the big payload somewhere else, like S3, and send only a reference (the "claim check") in the event:

```json
{
  "type": "ReportGenerated",
  "reportId": "r-55",
  "location": "s3://reports/r-55.pdf",
  "sizeBytes": 18200000
}
```

Consumers download the payload if they need it. Make sure the stored file lives at least as long as the event can be processed or replayed, and that consumers have permission to read it.

## 221: How does a service keep a local copy of another service's data?

It subscribes to the other service's events and stores the fields it needs in its own table. For example, the shipping service listens to `CustomerAddressChanged` and keeps `customer_id` and `address`.

```sql
INSERT INTO customer_addresses (customer_id, address, version)
VALUES ($1, $2, $3)
ON CONFLICT (customer_id) DO UPDATE
SET address = EXCLUDED.address, version = EXCLUDED.version
WHERE customer_addresses.version < EXCLUDED.version;
```

Shipping now works even if the customer service is down. The copy can be a little out of date, and you need a way to fill it at the start, usually by replaying events or a one-time import.

## 222: What does it mean that one service owns the data?

Only one service is allowed to change a piece of data and publish events about it. For example, only the customer service changes customer addresses. Other services may keep copies, but they never write to the original or publish `CustomerAddressChanged`.

Clear ownership avoids conflicts where two services both think they hold the truth. If another service needs a change, it sends a command or calls the owner's API.

## 223: How do you answer a query that needs data from several services?

Two main options:

- **API composition**: a gateway or backend-for-frontend calls each service and joins the results in memory. Simple, always fresh, but slower and fails if one service is down.
- **Replicated read model**: a service subscribes to events from all the needed services and builds one combined read model. Fast and resilient, but eventually consistent and more work to build.

Use composition for low-traffic or rarely joined data, and a replicated read model for heavy screens like search pages.

## 224: How do you control how many messages a consumer handles at once?

Limit the number of messages in progress:

- RabbitMQ: set a prefetch count with `channel.prefetch(n)`, so the broker sends at most `n` unacked messages.
- Kafka: tune `max.poll.records` and control how many partitions or messages you process in parallel.
- SQS: choose the batch size and number of concurrent pollers, or for Lambda, the batch size and maximum concurrency.

Too low wastes throughput. Too high overloads the consumer or its database. Tune it with load tests and watch processing time and lag.

## 225: What is the trade-off between consumer concurrency and ordering?

More parallel processing means more throughput, but messages can finish in a different order than they arrived. If two events for the same order are processed at the same time, the older one might finish last.

The usual fix is to process in parallel across keys but sequentially within a key: partition by entity id and keep one in-flight message per key. Libraries like Confluent's Parallel Consumer for Java do exactly this on top of Kafka.

## 226: When should a consumer process events in batches?

Batching helps when each event causes a write to a database or API that's much cheaper per item in bulk, like inserting 500 rows in one statement or bulk-indexing in Elasticsearch.

The downsides: higher latency for the first event in a batch, and one bad event can fail the whole batch. Handle that by retrying the batch item by item, or by reporting which items failed, like Lambda's partial batch response for SQS.

## 227: Why should handlers use the event's timestamp instead of the current time?

If a handler uses `new Date()`, the result depends on when it runs. During a replay or after a long outage, a sale from last Tuesday would be counted as today.

Use `event.occurredAt` for business logic like "which day does this belong to" or "was the payment late". The current time is only fine for technical things like "processed at".

## 228: Why must projections be free of side effects?

Projections are meant to be replayed: when you rebuild a read model, every event runs through the projection again. If a projection sends emails, charges cards or calls other APIs, a rebuild would repeat all of that.

Keep projections focused on updating their own read model. Put side effects in separate handlers (reactors or policies) that track their own progress and don't run during replays.

## 229: How do you avoid repeating side effects when replaying events?

- Keep side-effect handlers separate from projections, with their own checkpoint, and only replay projections.
- Make side effects idempotent, with an idempotency key based on the event id, so the outside system ignores repeats.
- Have a "replay mode" flag that makes side-effect handlers skip work.
- Check a "sent" table before sending.

The first option is the cleanest: replays are something only projections should go through.

## 230: How can a new service get historical data when it starts?

- **Replay events** from the beginning, if the broker or event store still has them (Kafka with long retention or compaction, an event store).
- **Snapshot plus events**: load a one-time export from the owner service, then subscribe to events from the point the export was taken.
- **Ask the owner to republish** current state as special "snapshot" events.

Whatever you choose, make sure no events are lost or doubled between the initial load and the live stream, for example by starting the subscription from a position recorded at export time.

## 231: What is Kafka log compaction, and when is it useful?

With log compaction, Kafka keeps at least the latest message for each key and removes older ones in the background. A message with a key and a `null` value (a tombstone) marks the key as deleted.

It's useful for topics that represent current state, like `customer-profiles` keyed by customer id. A new consumer can read the whole topic and get the latest state of every customer without the full history. It's not useful when you need every event, like for event sourcing.

## 232: How does retention affect your design?

Retention decides:

- how long a consumer can be down before it loses events,
- how far back you can replay to fix a bug or build a new read model,
- how much storage you pay for.

Short retention, like Kafka's default of 7 days, means you can't rebuild from Kafka alone, so you need another source of history: an event store, a data lake or compaction. Set retention on purpose for each topic, not just the default.

## 233: How do you secure who can send commands and publish events?

- **Commands**: check authentication and permission at the API, and again in the command handler for business-level rules like "only the owner can cancel".
- **Brokers**: use ACLs or IAM so only the owning service can write to its topics, and only allowed services can read them.
- **Transport**: use TLS between clients and brokers.
- **Events**: include who triggered the change in metadata, so consumers and audits can see it.

Treat a topic like an API: being able to publish `PaymentCompleted` is a lot of power.

## 234: How can you protect sensitive data inside events?

- Don't put it in the event at all if consumers don't need it. Send an id instead.
- Encrypt sensitive fields in the payload, so only consumers with the key can read them.
- Use broker features: encryption at rest, TLS, and access control per topic.
- Mask or remove sensitive fields before sending events to analytics or logs.

Remember that events are often copied to many places: DLQs, logs, data lakes and backups. Sensitive data spreads quickly.

## 235: What should you keep in mind about personal data in events?

Personal data in events ends up in every consumer, every copy and every backup. When a user asks to be deleted, you have to find it everywhere.

Put only what consumers really need in events, use ids instead of names or emails where possible, mark personal fields in your schemas, and plan deletion from day one, for example with crypto shredding or by keeping personal data in one owned table.

## 236: How do you validate events when consuming them?

Parse and validate the payload at the edge of the consumer, before business logic sees it. With zod:

```ts
import { z } from "zod";

const OrderPlaced = z.object({
  id: z.string().uuid(),
  type: z.literal("OrderPlaced"),
  occurredAt: z.string().datetime(),
  data: z.object({
    orderId: z.string(),
    customerId: z.string(),
    total: z.number().nonnegative(),
  }),
});

function parse(raw: Buffer) {
  const result = OrderPlaced.safeParse(JSON.parse(raw.toString()));
  if (!result.success) throw new PermanentError(result.error.message); // to DLQ
  return result.data;
}
```

A message that fails validation won't succeed on retry, so send it straight to the DLQ.

## 237: What should a consumer do with event types it doesn't know?

Usually ignore them and ack. Producers add new event types over time, and consumers that crash or DLQ on unknown types make every new event a breaking change.

Log unknown types at a low level or count them in a metric, so you notice if you're missing something you should handle. Only reject unknown types if the topic is supposed to contain a fixed, known set.

## 238: What is the tolerant reader pattern?

A tolerant reader takes only the fields it needs from a message and ignores everything else. It doesn't fail on extra fields, and it uses sensible defaults for optional missing fields.

This lets producers add fields freely without breaking consumers. The opposite, strict deserialization into a class that rejects unknown fields, makes every change risky.

## 239: What is the difference between producer-driven and consumer-driven contracts?

With **producer-driven** contracts, the producer designs the event and consumers adapt to it. It's simple, but the producer may not know what consumers actually use.

With **consumer-driven** contracts, each consumer states what it needs, and the producer checks it still provides that before releasing. The producer then knows exactly which fields it can change safely.

In practice, the producer still owns the event, but consumer contracts tell it the impact of changes.

## 240: How do you move an existing CRUD application to CQRS step by step?

1. Separate read and write code in the same app: query services that only read, command handlers that only write.
2. Add read-optimized queries or views for slow screens.
3. Publish events from the write side, using an outbox.
4. Build new read models from those events, one screen at a time, and switch queries to them.
5. Consider event sourcing only for parts where history really matters.

Each step is useful on its own. You don't need a big rewrite.

## 241: How can events help when replacing a legacy system?

With the strangler fig approach, you build new functions around the old system and move traffic piece by piece. Events help keep both sides in sync:

- Use CDC on the legacy database to publish changes as events.
- New services build their own data from those events.
- When the new service takes over a function, it publishes events that the legacy side can consume, if it still needs the data.

This lets you move one feature at a time while both systems run.

## 242: What are the pitfalls of using CDC to produce domain events?

CDC captures row changes, not business intent. An `UPDATE orders SET status = 'cancelled'` becomes "row changed", and consumers have to guess it was a cancellation. One business action can also touch several tables, producing several unrelated change events.

CDC events also expose your table structure, so a schema change breaks consumers. To avoid this, use CDC on an outbox table (where you write proper events), or put a translation step between raw CDC events and the public topic.

## 243: In what order should you deploy producers and consumers when an event changes?

For a new field or a new event type: deploy consumers first, so they're ready to handle it (or ignore it), then deploy the producer.

For removing a field: stop consumers from using it first, then remove it from the producer.

For a breaking change: publish both old and new versions for a while, move consumers to the new version one by one, then stop publishing the old one. Never assume all services are deployed at the same time.

## 244: What happens to events if the broker is down?

If you publish directly, the publish fails. Either the request fails too, or you lose the event if you only log the error.

With an outbox, the events stay safely in your database. The relay keeps retrying, and when the broker comes back, everything is sent in order. This is one of the strongest reasons to use an outbox: your service can keep accepting work during a broker outage.

## 245: What does Kafka's exactly-once support actually cover?

Kafka has an idempotent producer, which stops duplicates caused by producer retries, and transactions, which let you write to several partitions and commit consumer offsets atomically. Together they give exactly-once for "read from Kafka, process, write to Kafka" flows, like Kafka Streams with `processing.guarantee=exactly_once_v2`.

It doesn't cover side effects outside Kafka. If your consumer writes to PostgreSQL or calls an API, a crash can still cause a repeat. For that you need idempotent writes on your side.

## 246: What does "effectively once" mean?

Effectively once means that each message may be delivered more than once, but its effect happens only once. You get it by combining at-least-once delivery with idempotent processing: dedup by event id, use upserts, compare versions.

This is what most real systems aim for, since true exactly-once delivery across different systems is not possible in general.

## 247: When would you use locks instead of optimistic concurrency in command handling?

Optimistic concurrency works best when conflicts are rare: you read, decide and save, and retry if someone else got there first.

Pessimistic locking, like `SELECT ... FOR UPDATE`, is better when conflicts are frequent on the same record, like a popular product's stock counter, because constant retries would waste work. Locks reduce throughput and can cause deadlocks, so hold them only for a short time inside one transaction.

## 248: How do you enforce uniqueness, like a unique email, in an event-sourced system?

An aggregate only knows its own stream, so it can't check all other users' emails. Common solutions:

- A **unique constraint in a lookup table** updated in the same transaction as appending the event.
- A **reservation**: first reserve the email in a table with a unique index, then create the user. Release the reservation if creation fails.
- **Check the read model** before creating, and accept a rare duplicate that's fixed later by a compensating action.

The first two give a hard guarantee. The third is acceptable only if duplicates are cheap to fix.

## 249: What is the problem with validating commands against the read model?

The read model can be behind. If you check "is this username free?" against the read model, two users can both pass the check before either event reaches the projection, and both get the same name.

Use the read model for helpful checks in the UI, but enforce real invariants on the write side, with the aggregate, a unique constraint or a reservation.

## 250: How do you handle a command that needs to change several aggregates?

The usual rule is one aggregate per transaction. If a command really needs to change two, you have options:

- Change one aggregate, publish an event, and let a policy change the other one later (eventual consistency).
- Use a saga if the second change can fail and the first needs compensation.
- If both must always change together, they may belong in one aggregate. Rethink the boundaries.

Changing several aggregates in one database transaction works technically, but it increases conflicts and couples them tightly.

## 251: What is a domain service, and when do you need one in the write model?

A domain service holds business logic that doesn't belong to one aggregate. For example, calculating shipping cost based on the order, the customer's country and current carrier rates.

The command handler calls the domain service and passes the result to the aggregate, which still makes the final decision and raises the event. Keep domain services free of infrastructure code, so they're easy to test.

## 252: What is event enrichment?

Event enrichment means adding extra data to an event before it reaches consumers, so they don't have to look it up. For example, a stream processor takes `OrderPlaced` with only a `customerId` and adds the customer's segment and country, then publishes `OrderPlacedEnriched`.

It can happen in the producer before publishing, or in a separate step using stream processing. It saves many consumers from each doing the same lookup.

## 253: Should you put a cache in front of a read model?

Often you don't need to, since a read model is already shaped for fast reads. If you still need a cache for very hot data, the events themselves tell you when to update or remove entries: when the projection updates a row, it also deletes or refreshes the cache key.

Be careful with ordering. If an older update writes to the cache after a newer one, the cache holds stale data. Store a version with the cached value, or just delete the key and let the next read fill it.

## 254: How do you paginate a read model correctly?

Use keyset (cursor) pagination instead of `OFFSET`, because the read model keeps changing while users page through it, and offsets can skip or repeat rows:

```sql
SELECT id, placed_at, total FROM order_summary
WHERE customer_id = $1
  AND (placed_at, id) < ($2, $3)
ORDER BY placed_at DESC, id DESC
LIMIT 20;
```

The client sends back the last `placed_at` and `id` as the cursor. Add an index on `(customer_id, placed_at DESC, id DESC)` so this stays fast.

## 255: What should a projection do when it fails on an event?

It depends on whether order matters for that read model:

- **Stop and alert**: the projection waits on the failing event, retries, and someone fixes the bug. Data stays correct but becomes stale.
- **Skip and record**: the event goes to a parked list and the projection continues. Data stays fresh but may be wrong for that entity.

For read models where correctness matters, stopping is safer. Either way, fix the bug and rebuild or replay the affected events.

## 256: How do you know how far behind a projection is?

Compare the projection's checkpoint with the latest event position, and track the time of the last processed event:

- **Position lag**: latest global position minus the checkpoint.
- **Time lag**: now minus `occurredAt` of the last processed event.

Expose both as metrics and alert when they keep growing. Time lag is easier for people to understand, like "order list is 40 seconds behind".

## 257: How do you add logging or validation around every command handler?

Wrap the command bus or handlers with middleware, sometimes called pipeline behaviors:

```ts
type Handler<C> = (cmd: C) => Promise<unknown>;
type Middleware = <C>(next: Handler<C>) => Handler<C>;

const logging: Middleware = (next) => async (cmd) => {
  const start = Date.now();
  try {
    return await next(cmd);
  } finally {
    logger.info({ command: cmd.constructor.name, ms: Date.now() - start });
  }
};

const validation: Middleware = (next) => async (cmd) => {
  await validateOrThrow(cmd);
  return next(cmd);
};

const pipeline = [logging, validation].reduceRight<Handler<any>>(
  (next, mw) => mw(next),
  (cmd) => dispatchToHandler(cmd),
);
```

Every command now gets the same cross-cutting behavior without changing each handler. MediatR in .NET calls these pipeline behaviors. In NestJS you can use interceptors at the controller level.

## 258: Why should domain events be published only after the transaction commits?

If you publish during the transaction and it later rolls back, consumers react to something that never happened. If you publish after commit without an outbox, a crash right after commit loses the event.

So: collect events while handling the command, save them to the outbox in the same transaction, and let the relay publish them after commit. For in-process handlers that must see committed data, run them after the commit too.

## 259: How do entities raise domain events in code?

A common way is to let the aggregate collect events in a list, and let the repository or unit of work pull them out when saving:

```ts
abstract class AggregateRoot {
  private events: DomainEvent[] = [];
  protected addEvent(e: DomainEvent) {
    this.events.push(e);
  }
  pullEvents(): DomainEvent[] {
    const out = this.events;
    this.events = [];
    return out;
  }
}

class Order extends AggregateRoot {
  cancel(reason: string) {
    if (this.status === "shipped") throw new Error("Already shipped");
    this.status = "cancelled";
    this.addEvent(new OrderCancelled(this.id, reason));
  }
}

// in the repository, inside the transaction
await saveOrderRow(tx, order);
await saveToOutbox(tx, order.pullEvents());
```

The entity doesn't know about brokers. It only records what happened.

## 260: Should in-process event handlers run before or after the transaction commits?

**Before commit** (in the same transaction): the handler's changes succeed or fail together with the command. Good for keeping related data consistent, like updating a read table. But a slow or failing handler slows or breaks the command.

**After commit**: the command is safe and fast, but if the handler fails, its work is lost unless you store it somewhere to retry, like an outbox.

Use "before" for consistency-critical updates in the same database, and "after, through an outbox" for everything else.

## 261: How do you keep correlation ids across a saga?

Every message the saga sends copies the correlation id from the message that triggered it, and sets the causation id to that message's id:

```ts
function follow(
  cause: EventEnvelope<unknown>,
  type: string,
  data: unknown,
): EventEnvelope<unknown> {
  return {
    id: randomUUID(),
    type,
    version: 1,
    occurredAt: new Date().toISOString(),
    source: "order-saga",
    subject: cause.subject,
    correlationId: cause.correlationId,
    causationId: cause.id,
    data,
  };
}
```

Put this in a helper so nobody forgets it. With it, a search for one correlation id shows every step of the saga.

## 262: How do you handle partial batch failures with Lambda and SQS?

By default, if a Lambda function fails, the whole SQS batch is returned to the queue, including messages that succeeded. Enable `ReportBatchItemFailures` on the event source mapping and return the ids of only the failed messages:

```ts
import type { SQSBatchResponse, SQSEvent } from "aws-lambda";

export const handler = async (event: SQSEvent): Promise<SQSBatchResponse> => {
  const batchItemFailures: { itemIdentifier: string }[] = [];
  for (const record of event.Records) {
    try {
      await process(JSON.parse(record.body));
    } catch {
      batchItemFailures.push({ itemIdentifier: record.messageId });
    }
  }
  return { batchItemFailures };
};
```

Only the failed messages come back. With FIFO queues, stop at the first failure and report it and all the messages after it, to keep order.

## 263: How can you make a Lambda consumer idempotent?

Store a record per processed event and skip repeats. Powertools for AWS Lambda (TypeScript) has an idempotency utility that does this with DynamoDB:

```ts
import { makeIdempotent } from "@aws-lambda-powertools/idempotency";
import { DynamoDBPersistenceLayer } from "@aws-lambda-powertools/idempotency/dynamodb";

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: "idempotency",
});

const processOrder = makeIdempotent(
  async (event: { id: string; orderId: string }) => {
    await chargeCard(event.orderId);
    return { ok: true };
  },
  { persistenceStore },
);
```

It hashes the input (or a chosen key, like the event id), stores the result, and returns the saved result for repeats within the expiry window.

## 264: How do you push read model updates to the browser with SSE?

The server keeps an SSE connection per client and writes a message whenever the projection updates something the client cares about:

```ts
import express from "express";

const app = express();
const clients = new Map<string, express.Response>();

app.get("/orders/:id/events", (req, res) => {
  res.set({
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });
  res.flushHeaders();
  clients.set(req.params.id, res);
  req.on("close", () => clients.delete(req.params.id));
});

// called by the projection after it updates order_summary
export function notifyOrderChanged(orderId: string, status: string) {
  clients
    .get(orderId)
    ?.write(`data: ${JSON.stringify({ orderId, status })}\n\n`);
}
```

In the browser, `new EventSource("/orders/o-1001/events")` receives the updates. With several server instances, use Redis pub/sub or the broker to reach the instance holding the connection.

## 265: What are schema registry compatibility modes?

They control which schema changes the registry accepts:

- **BACKWARD** (Confluent's default): new consumers can read data written with the previous schema. Deploy consumers first.
- **FORWARD**: old consumers can read data written with the new schema. Deploy producers first.
- **FULL**: both directions.
- **\_TRANSITIVE** variants: check against all earlier versions, not just the last one.
- **NONE**: no checks.

For event topics that are kept for a long time, a transitive mode is safer, since consumers may read very old events during a replay.

## 266: How do you describe an event in AsyncAPI?

```yaml
asyncapi: 3.0.0
info:
  title: Order Service Events
  version: 1.0.0
channels:
  orderEvents:
    address: orders.order-events
    messages:
      orderPlaced:
        $ref: "#/components/messages/OrderPlaced"
operations:
  publishOrderPlaced:
    action: send
    channel:
      $ref: "#/channels/orderEvents"
components:
  messages:
    OrderPlaced:
      payload:
        type: object
        required: [orderId, customerId, total]
        properties:
          orderId: { type: string }
          customerId: { type: string }
          total: { type: number }
```

Keep the file in the producer's repository and publish generated docs, so other teams can find events without asking.

## 267: What does an event in CloudEvents format look like?

In structured JSON mode:

```json
{
  "specversion": "1.0",
  "id": "6f1c2e9a-3b4d-4c55-9a1e-0f8f7d2b6c11",
  "source": "/services/orders",
  "type": "com.shop.orders.OrderPlaced",
  "subject": "o-1001",
  "time": "2026-11-19T10:15:30Z",
  "datacontenttype": "application/json",
  "data": { "orderId": "o-1001", "total": 59.9 }
}
```

`specversion`, `id`, `source` and `type` are required. In binary mode, the attributes go in protocol headers (like `ce-type` in HTTP or Kafka) and the body is only `data`.

## 268: How can business events be used for analytics?

The same events that drive services can be streamed into a data warehouse or data lake, using a Kafka connector, Firehose or a simple consumer. Analysts then get a full history of business actions, not just snapshots of current state.

Things to watch: keep event schemas stable and documented, include event time, remove or mask personal data, and don't let analytics needs make operational events too large.

## 269: How do you debug a flow where "nothing happened" after an event?

1. Find the event: was it published at all? Check the outbox and the producer's logs.
2. Check the broker: is it on the right topic, with the right routing key or filter?
3. Check the consumer: is it subscribed, is it running, what's its lag?
4. Check the DLQ for the event id.
5. Search logs by correlation id or event id across all services.
6. Look at the trace, if you have tracing, to see where the chain stopped.

Most "lost events" are a wrong topic name, a filter that doesn't match, or an error that was swallowed.

## 270: What is a hot partition?

A hot partition is one that gets much more traffic than the others because many messages share the same key, like all events of one huge customer or one popular product. Only one consumer can read a partition at a time, so that consumer falls behind while others are idle.

Fixes: choose a key with better spread, split a hot key into sub-keys if ordering allows it, or handle the big entity in a separate topic.

## 271: How do you choose the number of partitions for a topic?

The number of partitions is the maximum number of consumers in a group that can work in parallel. Estimate it from target throughput divided by what one consumer can handle, then add room to grow.

Adding partitions later changes which partition a key goes to, which breaks ordering for existing keys. So it's better to start with enough, but not thousands, since many partitions add overhead to the cluster.

## 272: What do you do when a consumer is too slow?

- Find where the time goes: a slow database query, an outside API, one-by-one inserts.
- Scale out: add instances (up to the number of partitions for Kafka).
- Batch writes to the database.
- Process different keys in parallel while keeping order within each key.
- Move heavy, non-urgent work to a separate queue.
- Check that retries of failing messages aren't eating all the capacity.

Measure lag and processing time before and after each change.

## 273: How do you find the state of an aggregate at a point in the past?

Replay its events only up to that time or version:

```ts
async function accountAt(store: EventStore, id: string, at: Date) {
  const account = new Account();
  for (const e of await store.readStream(`account-${id}`)) {
    if (new Date(e.occurredAt) > at) break;
    account.apply(e);
  }
  return account;
}
```

This is one of the useful things you get from event sourcing: "what was the balance on March 1?" is just a replay with a cutoff.

## 274: How do you correct a mistake in an event-sourced system?

You don't edit the old event. You add a new event that corrects the state, like `PriceCorrected` or `PaymentAmountAdjusted`, with a reason.

For accounting-like domains you often use a reversal: one event cancels the wrong entry and another adds the right one. The history then shows both the mistake and the fix, which is exactly what auditors want.

## 275: What is the "closing the books" pattern?

Some streams grow forever, like a cash register or a long-lived account. Instead of one endless stream, you end a stream at a business boundary (end of day, end of month) with a closing event that holds the final state, and start a new stream with an opening event that carries it over.

Each stream stays short and fast to load, and you don't need snapshots. It also matches how many businesses already work.

## 276: How can you apply CQRS inside one service with one database?

Keep writes and reads in separate code paths:

- Commands go through handlers that load aggregates with an ORM and enforce rules.
- Queries use plain SQL or a light query builder, return DTOs shaped for the screen and never load aggregates.

```ts
// write side
await commandBus.execute(new ChangeShippingAddress(orderId, address));

// read side: direct SQL, no domain objects
const { rows } = await db.query(
  "SELECT o.id, o.status, c.name FROM orders o JOIN customers c ON c.id = o.customer_id WHERE o.id = $1",
  [orderId],
);
```

There's no eventual consistency and no extra infrastructure, and you still get simpler code on both sides.

## 277: How does CQRS relate to GraphQL?

GraphQL already splits operations into queries and mutations, which maps nicely to CQRS. Mutations become commands with specific names, like `cancelOrder`, not a generic `updateOrder`. Queries resolve against read models.

Be careful with mutations that return the updated object: if the read model is updated asynchronously, the returned data may be old. Return what the command result knows, or read from the write side for that response.

## 278: Who should own events and topics in a team setup?

The team that owns the service producing the events owns their schemas, documentation and the topic. They decide on changes, run compatibility checks and announce deprecations.

Consuming teams own their consumers, queues and read models. A small platform team often runs the broker itself and sets shared rules like naming and security. Clear ownership avoids the "nobody knows who uses this topic" problem.

## 279: How do you document which services publish and consume which events?

- Keep AsyncAPI files in each service's repository.
- Use an event catalog tool, like EventCatalog, to show events, owners, schemas and who consumes what.
- Generate diagrams of flows from those docs.
- Track consumers with broker metadata (consumer groups, subscriptions) to catch undocumented ones.

Without this, nobody can safely change an event, because nobody knows who depends on it.

## 280: What would you check when reviewing an event handler in a pull request?

- Is it idempotent? What happens if the same event comes twice?
- What happens if events arrive out of order?
- Are transient and permanent errors handled differently?
- Is the work in one transaction, or can it leave half-done state?
- Does it use the event time, not the current time, for business logic?
- Does it log the event id and correlation id?
- Does it validate the payload and ignore unknown fields?
- Does it have side effects that would repeat during a replay?

## 281: How is Redis pub/sub different from a real event broker?

Redis pub/sub delivers messages only to subscribers connected at that moment. Nothing is stored, there are no acks, and a subscriber that's down or reconnecting misses messages. It's at-most-once.

It's fine for live notifications, like pushing updates to WebSocket servers. For events that must not be lost, use Redis Streams (which store messages and support consumer groups) or a proper broker.

## 282: Can PostgreSQL LISTEN and NOTIFY be used for events?

Yes, for simple cases. A transaction runs `NOTIFY channel, 'payload'`, and connections that ran `LISTEN channel` get the message after the transaction commits.

Limits: the payload must be under 8000 bytes by default, messages are not stored, so listeners that are disconnected miss them, and there's no retry. A common pattern is to use NOTIFY only as a "wake up" signal for an outbox relay, while the data itself stays in the outbox table.

## 283: Do message priorities fit an event-driven design?

Some brokers support priorities. RabbitMQ classic queues can be declared with `x-max-priority` so higher priority messages are delivered first, and quorum queues support two levels, normal and high. Kafka and SQS have no priorities.

Priorities on events are rare, since events are facts, not tasks. For work queues, a simpler and more predictable approach is often separate queues for urgent and normal work, each with its own consumers.

## 284: How do you stop a consumer from overloading a downstream API?

Limit the rate in the consumer, not just the number of consumers:

- Use a rate limiter or token bucket before each call.
- Limit concurrency with prefetch or a semaphore.
- Respect `429 Too Many Requests` and `Retry-After`, and back off.
- Pause consuming (most clients have `pause()`) while the downstream is unhealthy, and resume later.

Otherwise, a backlog after an outage turns into a flood that takes the downstream service down again.

## 285: How do you shut down a consumer gracefully?

On `SIGTERM`:

1. Stop fetching new messages.
2. Let in-flight messages finish, with a time limit.
3. Commit offsets or ack the finished messages.
4. Close the connection to the broker, so it can reassign partitions or messages quickly.

```ts
process.on("SIGTERM", async () => {
  await consumer.disconnect(); // most clients finish the current batch and commit
  await pool.end();
  process.exit(0);
});
```

Without this, every deploy causes redelivery and duplicate processing.

## 286: How do you health-check a consumer service?

A consumer usually has no HTTP traffic, so "the process is up" says little. Better checks:

- **Liveness**: the process isn't stuck. The main loop has run recently.
- **Readiness**: it's connected to the broker and its database.
- **Progress**: it has committed offsets or processed messages recently, if there were messages to process.

Report lag as a metric, not as a health check. A consumer with lag is healthy but slow, and restarting it won't help.

## 287: How do you catch up on a large backlog after an outage?

- Scale out consumers temporarily, up to the partition count.
- Raise batch sizes for bulk writes.
- Watch downstream systems so the catch-up doesn't overload them.
- If some events are now pointless, like old "price changed" notifications for live dashboards, consider skipping them for that consumer.
- For read models, it's sometimes faster to rebuild from scratch in bulk than to replay one by one.

Tell users that some data is delayed while you catch up.

## 288: What is the decider pattern in event sourcing?

The decider pattern writes an aggregate as pure functions instead of a class:

- `decide(command, state)`: returns new events or throws.
- `evolve(state, event)`: returns the new state.
- `initialState`: the starting state.

```ts
type State = { balance: number };
const initialState: State = { balance: 0 };

function evolve(s: State, e: AccountEvent): State {
  if (e.type === "MoneyDeposited")
    return { balance: s.balance + e.data.amount };
  if (e.type === "MoneyWithdrawn")
    return { balance: s.balance - e.data.amount };
  return s;
}

function decide(
  cmd: { type: "Withdraw"; amount: number },
  s: State,
): AccountEvent[] {
  if (cmd.amount > s.balance) throw new Error("Insufficient funds");
  return [{ type: "MoneyWithdrawn", data: { amount: cmd.amount } }];
}

const state = history.reduce(evolve, initialState);
const newEvents = decide({ type: "Withdraw", amount: 20 }, state);
```

Pure functions are easy to test and reuse, and the same `evolve` can drive projections.

## 289: How do you model events that happen because time passed?

Things like "subscription expired" or "invoice overdue" aren't triggered by a user, but they're still business events. A scheduler or delayed message triggers a command like `ExpireSubscription` at the due time. The aggregate checks it's still valid, for example not renewed in the meantime, and then raises `SubscriptionExpired`.

Treat the timer as just another command source. The event goes into the stream like any other, so history shows exactly when the expiry happened.

## 290: How do you delete an entity in an event-sourced system?

You don't delete the stream. You append an event like `CustomerDeleted` or `ProductDiscontinued`. The aggregate marks itself as deleted and rejects further commands. Projections remove the entity from read models or mark it as deleted.

If data really must disappear, for legal reasons for example, use crypto shredding or a careful stream deletion, but treat that as a separate, deliberate process.

## 291: How should a read model handle deleted entities?

Two choices:

- **Hard delete** the row when the delete event arrives. Simple, but if an older event arrives later (out of order), it might recreate the row.
- **Soft delete** with a `deleted_at` column and keep the version. Queries filter deleted rows out, and late events are ignored because their version is older.

Soft delete is safer with out-of-order delivery. You can clean up old soft-deleted rows with a scheduled job.

## 292: What is the "listen to yourself" pattern, and how does it compare to an outbox?

In the listen-to-yourself pattern, a service doesn't write to its database directly. It publishes an event to the broker first, then consumes its own event to update its database. The broker becomes the single write, so there's no dual write.

The downside is that the service's own data is eventually consistent, so a user who just made a change may not see it right away, and validation against current state is harder. The outbox pattern keeps the database write immediate and is usually easier to work with.

## 293: How does Debezium's outbox event router work?

You write events to an outbox table with columns like `id`, `aggregatetype`, `aggregateid`, `type` and `payload`. Debezium reads inserts from the database's log, and its outbox event router transform turns each row into a Kafka message:

- the topic is based on `aggregatetype` (for example `outbox.event.Order`),
- the key is `aggregateid`, so events for one aggregate stay in order,
- the value is `payload`, and the event id and type go into headers.

You can delete outbox rows right after insert, since Debezium reads the log, not the table.

## 294: What are workflow engines, and how do they relate to sagas?

Workflow engines like Temporal, AWS Step Functions and Camunda run long business processes for you. You describe the steps in code or a definition, and the engine stores the state, handles retries, timeouts and waits, and resumes after crashes.

They're a ready-made way to build orchestrated sagas. Instead of writing your own process manager with state tables and timers, you write a workflow. The trade-off is a new platform to learn and run (or pay for).

## 295: How do you choose between choreography and orchestration?

Choose **choreography** when:

- the flow is short (two or three steps),
- services are owned by different teams that shouldn't depend on a central coordinator,
- steps are mostly independent reactions.

Choose **orchestration** when:

- the flow has many steps, branches or timeouts,
- you need to see and change the process in one place,
- compensation logic is complex.

Many systems mix both: choreography between domains and orchestration inside one domain's process.

## 296: How do you test a saga?

Test it like an aggregate with events in and commands out:

```ts
test("refunds payment when stock reservation fails", async () => {
  const sent: object[] = [];
  const saga = new OrderSaga(
    { send: async (c) => void sent.push(c) },
    new InMemorySagaRepo(),
  );

  await saga.onOrderPlaced(orderPlaced("o-1", 50));
  await saga.onPaymentCompleted(paymentCompleted("o-1"));
  await saga.onStockReservationFailed(stockFailed("o-1"));

  assert.deepEqual(
    sent.map((c) => c.constructor.name),
    ["ChargePayment", "ReserveStock", "RefundPayment", "CancelOrder"],
  );
});
```

Also test timeouts, duplicate events and events arriving in an unexpected order. Workflow engines like Temporal have their own test tools that can skip time.

## 297: How do you run an event-driven system locally for development?

- Run the broker and databases with Docker Compose: Kafka (KRaft mode, no ZooKeeper), RabbitMQ, PostgreSQL.
- For AWS services, use LocalStack to emulate SQS, SNS, EventBridge and Lambda.
- Seed some test events with a script.
- Use a UI tool to look at topics and queues, like the RabbitMQ management UI or a Kafka UI.
- Run only the services you're working on, and stub the rest with simple fake consumers.

Make the setup one command, or people will stop testing flows end to end.

## 298: What tools help you inspect messages in a broker?

- RabbitMQ management UI: queues, bindings, rates, and you can peek at messages.
- Kafka CLI tools like `kafka-console-consumer.sh` and `kafka-consumer-groups.sh`, or UIs like Kafbat UI (the community fork of Kafka UI) and Redpanda Console.
- AWS console and CLI for SQS: receive messages, see DLQ contents, start a redrive.
- `kcat` (formerly kafkacat) for quick reads and writes from the terminal.

Be careful with tools that consume messages: on a queue, reading can remove a message or make it invisible for a while.

## 299: What is the difference between a domain event inside an aggregate and a notification to a user?

A domain event like `OrderShipped` is a fact for the system. A notification like "Your order is on its way" email is a side effect that some handler decides to send because of that event.

Keep them separate. The domain shouldn't know about emails or push notifications. A notification service listens to events and decides what to send, through which channel and in which language.

## 300: In an interview, how would you explain when you'd choose event sourcing?

I'd choose event sourcing for a part of a system when history is part of the business itself, for example banking, accounting, bookings, inventory movements or anything with heavy audit needs. It also fits when the business keeps asking new questions about past behavior, since you can build new read models from old events.

I wouldn't use it for simple CRUD data like user settings or product descriptions. Even inside one system, I'd use it only in the bounded contexts that need it, and use normal tables everywhere else.

# Advanced Questions (301-450)

## 301: What is the difference between global ordering and per-stream ordering?

**Per-stream ordering** means events of one aggregate are in order, which you always need. **Global ordering** means all events in the whole store have one total order, so a projection that reads from many streams sees them in the same order every time.

Global ordering is useful for projections that combine streams and for deterministic rebuilds, but it limits write scaling, because every append has to agree on one sequence. Kafka gives only per-partition order. Most event stores give a global position, but often with gaps or caveats.

## 302: Can Kafka be used as an event store for event sourcing?

It can store events, but it lacks two things event sourcing needs:

- **Optimistic concurrency per stream.** You can't say "append only if this aggregate is at version 5".
- **Fast reads of one stream.** Loading one aggregate means scanning a partition that holds many other aggregates.

Teams that use Kafka here usually keep aggregate state elsewhere (for example in Kafka Streams state stores or a database) and use Kafka as the event log for integration. A common design is a real event store or database for the write side, and Kafka for distributing events.

## 303: Why can a projection miss events when reading by an auto-increment position in PostgreSQL?

Sequence values are assigned when a row is inserted, not when the transaction commits. Transaction A gets position 10, transaction B gets 11, B commits first. A projection reads up to 11 and saves checkpoint 11. Then A commits position 10, and the projection never sees it.

This is a real bug in naive SQL event stores and outbox relays under concurrent writes. It shows up only under load, which makes it hard to notice.

## 304: How do you fix the gap problem in a SQL event store?

Common solutions:

- **Serialize appends** with a lock (like an advisory lock), so positions commit in order. Simple, but limits write throughput.
- **Track transaction ids**: store `pg_current_xact_id()` with each event and only read events from transactions older than the oldest still running one, using `pg_snapshot_xmin(pg_current_snapshot())`. Marten and some other libraries use ideas like this.
- **Wait on gaps**: when the reader sees a gap, wait a short time for it to fill before moving on. If it doesn't fill, assume the transaction rolled back.

Each trades latency, throughput and complexity differently.

## 305: How do you keep outbox order when running several relay instances?

With `SKIP LOCKED`, two relays can publish events of the same aggregate in the wrong order. Options:

- Run a **single active relay** using leader election or an advisory lock. Simplest, and enough for many systems.
- **Partition the outbox** by aggregate id hash, and let each relay own some partitions.
- Use **CDC** (Debezium), which reads the log in commit order with one connector task per database.

Also, the relay must publish to a broker partition keyed by aggregate id, or the order is lost on the broker side anyway.

## 306: How do you keep an outbox table healthy at high volume?

- Delete published rows quickly, in small batches, or use table partitioning by time and drop old partitions.
- With CDC, delete rows right after insert, since the log already has them.
- Index only what the relay needs, like a partial index on unpublished rows: `CREATE INDEX ON outbox (created_at) WHERE published_at IS NULL`.
- Watch for bloat and autovacuum lag, since outbox tables have lots of inserts and deletes.
- Alert on the age of the oldest unpublished row.

## 307: What are the risks of CDC with PostgreSQL logical replication?

- A replication slot keeps WAL until the consumer confirms it. If Debezium stops for a long time, WAL grows until the disk fills and the database goes down. Monitor slot lag and set `max_slot_wal_keep_size`.
- Failover to a replica can lose the slot, depending on version and setup. PostgreSQL 17 added failover slots to help with this.
- Schema changes need care, since the connector must understand the new table structure.
- Large transactions arrive only after commit, which can cause delays and memory spikes.

## 308: How does Kafka's consume-transform-produce exactly-once work?

The application uses a transactional producer with a stable `transactional.id`. For each batch it:

1. Begins a transaction.
2. Produces output messages.
3. Adds the consumed offsets to the transaction (`sendOffsetsToTransaction`).
4. Commits the transaction.

Consumers downstream use `isolation.level=read_committed`, so they only see messages from committed transactions. If the app crashes, the transaction is aborted and the input is read again from the last committed offsets, with no duplicate output visible.

## 309: What is zombie fencing in Kafka transactions?

A "zombie" is an old instance of a producer that's still running after it was thought dead, for example after a long GC pause. If both the old and new instance write, you'd get duplicates.

Each transactional producer registers with its `transactional.id` and gets an epoch number. When a new instance starts with the same id, the epoch goes up, and the broker rejects writes from the old epoch. That's fencing: the zombie can no longer commit anything.

## 310: How do you design an idempotency store that's safe under concurrency?

The naive "check if processed, then process, then mark processed" has a race: two instances check at the same time, both see "not processed" and both run.

Safer designs:

- **Insert first** with a unique constraint, in the same transaction as the work. The second insert fails or waits.
- For outside side effects, insert a row with status `in_progress` and a lease time. Others see it and back off. On success set `done`, on failure delete it or let the lease expire.
- Store the result, so repeats can return it.
- Expire old keys with a TTL, longer than the longest possible redelivery window.

## 311: What isolation problems can sagas have, and how do you reduce them?

A saga's steps commit separately, so other transactions can see its partial results. Problems include:

- **Lost updates**: one saga overwrites changes made by another.
- **Dirty reads**: someone reads data a saga will later compensate.
- **Fuzzy reads**: a saga reads the same data twice and gets different values.

Countermeasures from the saga literature: semantic locks (a `PENDING` status that others respect), commutative updates (like increments that can be applied in any order), re-reading values before updating, version checks, and ordering steps so risky ones come last.

## 312: What is the pivot transaction in a saga?

The pivot transaction is the step after which the saga is committed to going forward. Steps before it can be compensated. Steps after it are expected to always succeed eventually, so they're retried until they do instead of being compensated.

For an order, charging the card might be the pivot: before it, you can cancel freely. After it, shipping and emails must be retried until done. Designing around the pivot makes failure handling much clearer.

## 313: What do you do when a compensating action itself fails?

Retry it, since compensations should be idempotent and must eventually succeed. If retries keep failing, the saga moves to a "needs attention" state and alerts a person, because the system is now inconsistent in a way the business must know about.

Don't let a saga silently give up. Keep the full history of steps and failures, so an operator can see what happened and fix it by hand or with a tool.

## 314: How do you persist saga state safely?

Store saga state in a table keyed by saga id, with a version column for optimistic concurrency, because two events for the same saga can arrive at once. Save the state change and the outgoing commands (through an outbox) in one transaction.

Make handlers idempotent by recording which event ids the saga already handled. Keep completed sagas for a while for debugging, then archive them.

## 315: How do you spot and avoid tangled choreography?

Signs of trouble:

- Nobody can say what happens after an event without reading many repositories.
- Events trigger events that trigger events, sometimes looping back.
- Small changes need coordinated changes in several services.

Ways to fix it: draw the flow from traces or event catalogs, move complex flows into an orchestrator, keep choreography for short reactions, and watch for cycles where service A reacts to B and B reacts to A.

## 316: How do you roll out a breaking change to a widely used event?

1. Add the new event version alongside the old one, and publish both (often from the same outbox entry, mapped twice).
2. Announce it with a deprecation date.
3. Move consumers to the new version, one by one. Track who still reads the old one from broker metrics or consumer registrations.
4. Stop publishing the old version once nobody consumes it.
5. Keep upcasters or readers for old stored events, since replays will still see them.

Plan for weeks or months, not one deploy.

## 317: How do you implement a chain of upcasters?

Register one function per version step, and apply them in order until the event reaches the latest version:

```ts
type Upcaster = (data: any) => any;

const upcasters: Record<string, Record<number, Upcaster>> = {
  OrderPlaced: {
    1: (d) => ({ ...d, currency: "EUR" }), // v1 -> v2
    2: (d) => ({ ...d, total: { amount: d.total, currency: d.currency } }), // v2 -> v3
  },
};

const latest: Record<string, number> = { OrderPlaced: 3 };

function upcast(type: string, version: number, data: any) {
  let v = version;
  let d = data;
  while (v < (latest[type] ?? v)) {
    d = upcasters[type][v](d);
    v++;
  }
  return { version: v, data: d };
}
```

Each upcaster only knows two neighboring versions, so adding v4 means adding one function. Test each step with real stored examples.

## 318: When would you do a copy-and-transform migration of an event store?

When upcasting at read time becomes too slow or complex: many versions, structural changes like splitting one stream into two, or renaming event types everywhere.

You read every stream, transform the events and write them to a new store or new streams. Then you switch the application to the new store, often with a short write freeze or by catching up the tail. It's heavy and risky, so keep the old store until you've verified the new one, and use it rarely.

## 319: How do you migrate to a new event store technology?

1. Build a migration process that reads all streams from the old store and writes them to the new one, keeping stream ids, versions and timestamps.
2. Keep it running to copy new events until the tail is small.
3. Pause writes briefly, copy the last events, and switch the application to the new store.
4. Rebuild projections from the new store's positions, since global positions differ between stores.
5. Keep the old store read-only for a while for rollback.

Compare event counts and checksums per stream before you switch.

## 320: Why do snapshots need versioning?

A snapshot is the aggregate's state in some serialized shape. If you change the aggregate's fields or the way it applies events, old snapshots may no longer match what replaying events would give.

Store a snapshot schema version with each snapshot. When the version doesn't match the current code, ignore the snapshot and replay from events (then save a new one). This keeps snapshots as a pure cache that can always be thrown away.

## 321: How should you think about stream design in event sourcing?

Usually one stream per aggregate instance, like `order-o-1001`. This matches the consistency boundary: you check the expected version for exactly the data the rules need.

Other designs, like one stream per aggregate type, cause constant concurrency conflicts and slow loads. On the other hand, too-fine streams make you need multi-stream transactions. If you find yourself wanting to append to two streams atomically all the time, your aggregate boundaries are probably wrong.

## 322: How do you scale read models?

- Put different read models in different stores, each scaled for its own load.
- Add read replicas for a read model that's queried heavily.
- Shard a read model by tenant or by key if one database isn't enough.
- Cache hot results with versioned keys.
- Run separate projection workers per read model so one slow projection doesn't hold up others.

Since read models can be rebuilt, you can also change their storage later without a risky data migration.

## 323: How do you rebuild a projection over billions of events quickly?

- Partition the work by stream id hash. Events of one stream stay in order within one worker, and workers run in parallel.
- Write to the read store in large batches and turn off things like indexes or refresh intervals during the rebuild, then turn them back on.
- Read events in big pages using the global position index.
- Write to a new table or index and switch at the end, so the old one keeps serving.
- After the bulk rebuild, switch to normal one-by-one processing for live events.

This only works if the projection doesn't depend on order across streams.

## 324: How do you build a projection that needs data from several streams?

Example: an order list that shows the customer's name, which comes from customer events. Options:

- The projection keeps its own small lookup table, like `customer_names`, updated from customer events, and uses it when handling order events. When a name changes, it updates all affected rows.
- Put the needed data into the order events when they're created (enrichment), and accept that later name changes need their own handling.
- Join at query time if both tables are in the same database.

Be careful with ordering: an order event can arrive before the customer event it depends on.

## 325: How do you keep several read models consistent with each other?

You usually can't make them update at exactly the same time, since each projection runs at its own speed. A screen that reads from two read models might see one updated and the other not.

Options: build one read model per screen so it only reads from one place, have both projections run in the same process and transaction from one event feed, or return the checkpoint position with each read and let the client wait until both reach the same position.

## 326: How do you enforce a rule that spans several aggregates?

First, ask if it really needs to be immediately consistent. Many cross-aggregate rules, like "a customer can't have more than 5 open orders", can be checked eventually and fixed by a policy if broken.

If it must be strict:

- Make a new aggregate that owns the rule, like `CustomerOrderLimit`, and route the relevant commands through it.
- Use a database constraint or lock in the same transaction.
- Use a reservation step before the main command.

Changing aggregate boundaries is often the real fix.

## 327: What is a hot aggregate, and how do you deal with it?

A hot aggregate gets many concurrent commands, like a concert's seat inventory when tickets go on sale. With optimistic concurrency, most commands conflict and retry, and throughput drops.

Options:

- Split it: one aggregate per section or block of seats.
- Queue commands for that aggregate and process them one at a time.
- Use commutative operations that don't conflict, like counters.
- Use a pessimistic lock for that one case.
- Pre-allocate stock into several buckets that can be reserved independently.

## 328: How does crypto shredding work in practice?

Each data subject gets their own encryption key, stored in a key store (a database table or a KMS). When writing an event, personal fields are encrypted with that person's key. When reading, they're decrypted.

To "forget" a person, you delete their key. All their personal data in events, copies and backups becomes unreadable. Readers must handle missing keys, for example by showing "deleted user". Watch out for personal data that leaks unencrypted into read models, logs and search indexes, since those must be cleaned separately.

## 329: How do you handle retention and legal hold for events?

Different events have different legal needs: some must be kept for years (financial records), some must be deleted after a period (personal data). Plan this per event type:

- Mark event types with their retention class.
- Separate streams or topics by retention needs.
- Archive old events to cheaper storage instead of deleting, where allowed.
- Support legal holds that pause deletion for specific subjects.

An event store that keeps everything forever is simple but may break privacy laws.

## 330: How do you stop someone from publishing fake events?

- Restrict write access to each topic to its owning service, using broker ACLs or IAM.
- Authenticate clients with mTLS or SASL, not shared passwords.
- For very sensitive events, sign the payload, and let consumers verify the signature with the producer's public key.
- Validate events on consumption: does this order actually exist, is the amount sensible?
- Don't let external input, like webhooks, be republished on internal topics without verification.

Consumers trust events a lot, so a fake `PaymentCompleted` could ship goods for free.

## 331: How do you design an event-driven system for multiple tenants?

Decide how isolated tenants must be:

- **Shared topics** with a tenant id in every event and header. Cheapest, but one noisy tenant can slow everyone, and bugs can leak data between tenants.
- **Topics or queues per tenant**. Better isolation, but many topics and more operations work.
- **Separate clusters** for large or regulated tenants.

Always carry the tenant id in metadata, check it in every handler, and partition by tenant plus entity so one tenant's burst doesn't block others.

## 332: How do you handle a noisy tenant in shared queues?

One big tenant can fill the queue and delay everyone else. Options:

- Partition by tenant so their events go to their own partitions, and other tenants keep flowing.
- Use fair scheduling in the consumer: round-robin across tenants instead of strict FIFO.
- Rate limit per tenant at the producer.
- Move very large tenants to dedicated queues or consumers.

Measure lag per tenant, not just overall, or you won't notice small tenants waiting.

## 333: What is a poison pill in an ordered partition, and why is it worse there?

In an ordered partition, you can't skip ahead: if one message keeps failing, every message behind it in that partition waits. With a regular queue, other messages could still be processed.

Options: after a few retries, move it to a DLQ and continue (accepting that later events for that key may now be out of order), or park all following events for the same key until the failed one is fixed. The second keeps per-key order without blocking other keys.

## 334: Why do retry topics break ordering, and what can you do about it?

If event 1 for order A fails and goes to a retry topic, the consumer moves on and processes event 2 for order A. Now event 2 is applied before event 1.

Fixes:

- When an event for a key is sent to retry, also send all later events for that key to retry until the first succeeds. You need to keep a list of "blocked keys".
- Retry in place (block the partition) for a short time before giving up.
- Design consumers to tolerate order changes, for example with version checks that ignore older events.

## 335: What is head-of-line blocking in event processing?

Head-of-line blocking happens when the first message in a lane is slow or stuck, and everything behind it has to wait, even if those messages could be processed quickly.

In Kafka this happens per partition. Fixes include processing different keys in parallel within a partition (keeping order only per key), moving slow work to a separate queue, and putting timeouts on outside calls so one slow message can't hold up the lane for minutes.

## 336: How do rebalances cause trouble at scale, and how do newer Kafka protocols help?

In the classic "eager" protocol, every rebalance made all consumers give up all partitions and stop, then get a new assignment. In a large group with frequent deploys or autoscaling, this caused long pauses and lots of reprocessing.

The cooperative sticky assignor moved only the partitions that needed to move. Kafka 4.x makes the new consumer group protocol (KIP-848) generally available, where the broker manages assignments and changes them one by one, so other consumers keep working. Static group membership (`group.instance.id`) also avoids rebalances on quick restarts.

## 337: Why are timestamps unreliable for ordering events from different services?

Each server has its own clock, and clocks drift, even with NTP. Two events 5 ms apart on different servers can have timestamps in the wrong order. Clocks can also jump backwards after a sync.

For ordering within an entity, use version numbers from the single owner. For causal order across services, use causation ids or logical clocks like Lamport timestamps or vector clocks. Use wall-clock time only for human-facing information and time windows.

## 338: What is a Lamport clock, and when is it useful?

A Lamport clock is a counter each process keeps. It goes up by one for every event the process creates. When a process receives a message with counter `n`, it sets its own counter to `max(own, n) + 1`.

This guarantees that if event A caused event B, then A's counter is smaller than B's. It doesn't tell you if two events with different counters are actually related. Vector clocks can detect that, at the cost of storing one counter per process. They're useful in systems that need to merge concurrent updates.

## 339: What are watermarks in stream processing?

A watermark is the stream processor's estimate that "no more events with an event time earlier than T will arrive". When the watermark passes the end of a time window, the window can be closed and its result published.

Watermarks let you aggregate by event time even with late and out-of-order events. Events that arrive after the watermark are "late". You can drop them, send them to a side output or update the already-published result.

## 340: What kinds of windows exist in stream processing?

- **Tumbling**: fixed size, no overlap, like every 5 minutes.
- **Hopping** (or sliding with a step): fixed size, overlapping, like 10-minute windows every minute.
- **Session**: grows while events keep coming for a key and closes after a period of inactivity, like a user session.
- **Sliding** (in Kafka Streams): defined by the time difference between records, used for joins and "within N minutes" logic.

Windows let you answer questions like "orders per minute per country" on a stream of events.

## 341: When would you use Kafka Streams or Flink instead of plain consumers?

When the logic is stateful and continuous, for example:

- aggregations and windows (counts per minute),
- joins between streams (orders with payments within 30 minutes),
- enrichment from a table built from another topic,
- exactly-once processing within Kafka.

Kafka Streams is a Java library that runs inside your app, with state stored locally and backed up to Kafka. Flink is a separate cluster with more power for large jobs. For simple "read event, write to DB" handlers, plain consumers are easier.

## 342: What is the stream-table duality?

A stream of change events can be turned into a table by applying each change to the latest value per key. A table can be turned into a stream by emitting every change made to it.

Kafka Streams builds on this: a `KStream` is a stream of events, and a `KTable` is the latest value per key built from a topic. It's the same idea as event sourcing and projections, just at the stream processing level.

## 343: How do joins between streams and tables work in stream processing?

- **Stream-table join**: each event in a stream is joined with the current value of a table for its key, like enriching each order with the customer's current tier.
- **Stream-stream join**: events from two streams are matched if they share a key and arrive within a time window, like matching orders with payments within 30 minutes.
- **Table-table join**: the result is a table that updates whenever either side changes.

Joined data must be partitioned the same way (same key, same partition count), or the processor has to repartition it first.

## 344: What race can happen when events invalidate a cache?

A reader misses the cache and loads value v1 from the database. Before it writes to the cache, a write updates the database to v2, and the invalidation event deletes the cache key. Then the reader writes v1 to the cache. The cache now has stale data until it expires.

Fixes: store the version with the cached value and refuse to overwrite a newer version, delete the key again a short time after the update (delayed double delete), or use short TTLs as a safety net.

## 345: How can you provide read-your-writes across services?

- The command returns a version token or position. The client sends it with later queries, and the read side waits until it has processed at least that position, or answers from the write side if it times out.
- Route a user's reads to the same replica or region they wrote to for a short time (sticky sessions).
- Keep the user's own recent changes in the client and merge them with server data.

The version-token approach is the most precise and works well with CQRS read models.

## 346: What is causal consistency, and why does it matter in event-driven systems?

Causal consistency means that if event B was caused by event A, everyone who sees B also sees A. For example, if a reply to a comment exists, the comment must exist too.

In event-driven systems, A and B may travel through different topics or partitions and arrive in the wrong order. To protect causality, put related events on the same key, carry causation ids and let consumers wait for missing causes, or make consumers tolerate the effect arriving first, for example by creating a placeholder.

## 347: What are monotonic reads, and how can CQRS break them?

Monotonic reads means a user never sees data go back in time. If they saw status "shipped", a later read should not show "paid".

With several read replicas or read models updated at different speeds, two requests from the same user can hit different copies, and the second can be older. Fixes: sticky routing per user, passing the last seen version and refusing to answer from a copy that's behind, or having the client ignore older versions than it already has.

## 348: How do you test eventual consistency and failure handling?

- **Fault injection**: kill consumers, drop broker connections, slow down the database, and check that the system recovers without lost or doubled effects.
- **Duplicate and reorder tests**: feed handlers the same events twice and in shuffled order, and assert the final state is the same.
- **Property-based tests**: generate random event sequences and check invariants after projection.
- **Chaos testing** in staging with tools that kill pods or add latency.

Assert on the eventual result with a timeout, never immediately after sending.

## 349: How do you load test an event pipeline?

1. Generate realistic events (types, sizes, key distribution, including hot keys) at the target rate, and above it.
2. Measure end-to-end latency from `occurredAt` to the moment the final consumer finishes, not just broker throughput.
3. Watch consumer lag, broker CPU and disk, database load and DLQ size.
4. Test catch-up: stop consumers, build a backlog, start them and see how long recovery takes.
5. Test rebalances and deploys during load.

The question to answer is not "how fast is it" but "where does it break and how does it recover".

## 350: How do traces work for async consumers that process batches?

A batch consumer handles many messages, each with its own trace context. A span can only have one parent, so you can't make the batch span a child of all of them.

OpenTelemetry solves this with span links: the batch processing span links to the producer spans of each message. Tracing tools can then show the connection without forcing one parent. For per-message processing inside the batch, you can create a child span per message with its own parent context.

## 351: What SLOs make sense for an event-driven system?

Request-based SLOs like "99.9% of API calls under 300 ms" don't cover async work. Add:

- **Freshness**: 99% of read model updates visible within N seconds of the event.
- **End-to-end latency**: time from event creation to the final effect, like "confirmation email sent within 2 minutes".
- **Completeness**: share of events processed without ending in a DLQ.
- **Saga completion**: share of orders that reach a final state within a time limit.

These match what users actually notice: "my order status didn't update".

## 352: How do you detect a stuck consumer?

A stuck consumer may look healthy: the process is running, connected, no errors. Signs:

- lag growing while the committed offset doesn't move,
- no successful processing for N minutes while messages are waiting,
- one partition with growing lag while others are fine (a poison pill or hot key),
- in-flight message count stuck at the prefetch limit.

Alert on "lag growing and no progress", not just "lag above X". A heartbeat metric updated after each successful message makes this easy.

## 353: How do you plan disaster recovery for an event-driven system?

Decide what is the source of truth and how to restore it:

- **Event store or database**: regular backups plus point-in-time recovery. Read models can be rebuilt from it.
- **Broker**: replicate to another cluster or region, or accept that in-flight messages can be republished from outboxes.
- **Consumers**: must be able to restart from a known position after a restore, and handle duplicates.

Restore drills matter. After restoring a database to an earlier point, consumers and other services may have seen events that "no longer happened", which you need a plan for.

## 354: What problems come with active-active multi-region event-driven systems?

- The same entity can be changed in two regions at the same time, causing conflicts.
- Events from two regions arrive in a different order in each region.
- Replication between regions adds delay, so regions see different states.
- Replicated events can loop back to the region they came from.

Common solutions: give each entity a home region that owns its writes, tag events with their origin region to avoid loops, and use conflict resolution rules or CRDTs where both regions must accept writes.

## 355: What happens to consumer offsets when you replicate Kafka topics to another cluster?

Offsets in the target cluster are different from the source, because the replica topics are separate logs. A consumer group that fails over can't just reuse its source offset.

MirrorMaker 2 solves this with offset syncs and checkpoints: it translates committed offsets from the source to matching offsets in the target, and can sync them to target consumer groups. Translation isn't always exact, so consumers may reprocess some events after failover. Idempotent handlers make that safe.

## 356: What are CRDTs, and how do they relate to event-driven systems?

CRDTs (conflict-free replicated data types) are data structures that can be updated independently in different places and always merge to the same result, no matter the order of updates. Examples are grow-only counters, sets with add and remove tags, and last-writer-wins registers.

They're useful when several regions or offline clients must accept writes and later sync through events. They remove the need for coordination, but only work for data that fits their merge rules.

## 357: What does it mean to treat events as products?

In a data mesh or large organization, important event streams are treated like a product for other teams: they have an owner, documentation, a stable schema, a version policy, quality guarantees and a support channel.

This shifts thinking from "we publish whatever our code produces" to "other teams depend on this, so we design and maintain it carefully". It usually goes together with an event catalog and schema registry.

## 358: What does event governance include?

- Naming and versioning rules for events and topics.
- Schema registry with compatibility checks in CI.
- Ownership: each topic has a team.
- Data classification: which fields are personal or sensitive.
- Access control: who can publish and who can read.
- Retention rules per topic.
- A deprecation process.

Light governance prevents chaos. Too much makes teams avoid events and call each other directly instead.

## 359: What are common anti-patterns in event-driven systems?

- **Event-driven RPC**: an event that's really a command waiting for a reply, like `PleaseCalculateTaxEvent`.
- **Passive-aggressive events**: an event that pretends to be a fact but expects a specific receiver to act, like `InvoiceShouldBeSent`.
- **CRUD events** that just mirror table rows.
- **Events as the only API**: forcing everything through events, even simple queries.
- **Giant shared event library** that couples all services.
- **No idempotency**, relying on exactly-once delivery that doesn't exist end to end.

## 360: How can events lead to a distributed monolith?

If services must be deployed together because of shared event classes, if one event schema change breaks five services, or if a business flow needs eight services to respond in a fixed sequence, you have a distributed monolith: all the costs of distribution and none of the independence.

Prevent it with clear bounded contexts, stable public events separate from internal ones, tolerant readers and avoiding long chains where each service depends on the previous one's exact behavior.

## 361: How can failures cascade in an event-driven system?

Async messaging stops many cascades, but not all:

- A consumer retries hard against a failing database and makes it worse.
- A backlog builds during an outage, and when the downstream comes back, the flood takes it down again.
- A bug publishes a burst of bad events that fill DLQs and trigger mass retries everywhere.
- A slow consumer blocks a shared broker resource, like disk on a node.

Protect with backoff, rate limits, circuit breakers, per-consumer quotas and alerting on unusual event volume.

## 362: What is an event storm or feedback loop, and how do you prevent it?

A feedback loop is when service A reacts to an event by publishing an event that makes service B publish an event that makes A react again, forever. For example, two services syncing the same field back and forth.

Prevent it by:

- not publishing an event if nothing actually changed,
- tagging events with their origin and ignoring changes you caused yourself,
- giving each piece of data one owner,
- limiting causation chain depth and alerting on sudden spikes in event rates.

## 363: Should consumers use circuit breakers?

Yes, when they call downstream services. If a downstream API is failing, a circuit breaker stops calling it for a while instead of failing every message one by one.

For consumers, when the circuit is open it's usually better to pause consuming than to send messages to the DLQ, since the problem is not the messages. When the circuit closes, resume. This keeps messages in the broker and avoids a pile of DLQ entries that need redriving.

## 364: How do broker quotas protect a shared cluster?

Kafka supports quotas on produce and fetch bandwidth and request rate, per user or client id. If a client exceeds them, the broker slows its responses.

Without quotas, one misbehaving producer or a consumer replaying a huge topic can use all the disk or network and slow every other team. On shared clusters, set quotas per service and monitor which clients hit them. Managed services often have their own similar limits.

## 365: What drives the cost of an event-driven system?

- Broker capacity: storage (retention times replication factor), network, number of partitions.
- Per-request pricing on managed services (SQS, SNS, EventBridge, Pub/Sub), where chatty designs get expensive.
- Data transfer between zones and regions.
- Duplicate storage: events in the broker, event store, data lake, read models and backups.
- Operations: people to run and debug it.

Batch small messages, compress, choose retention on purpose and watch cross-zone traffic, which is often a surprise item on cloud bills.

## 366: How do you decide which parts of a system should use event sourcing?

Go through each bounded context and ask:

- Is the history of changes valuable to the business, not just the current state?
- Are there audit or legal needs to show how state came to be?
- Will we likely need new views of past behavior?
- Are the business rules complex, with meaningful state changes?

Use event sourcing where several answers are yes. Use plain tables where it's mostly CRUD. The contexts still talk to each other with integration events either way.

## 367: How do you migrate an existing CRUD aggregate to event sourcing?

1. For each existing record, create one starting event like `OrderMigrated` or `OrderImported` that holds the current state. You can't invent the real history.
2. From then on, every change is a real domain event.
3. Run both models side by side for a while, and compare the state from events with the old table.
4. Build read models from the new events.
5. Switch reads, then remove the old write path.

Be honest in the event name that this is a migration snapshot, not a real business event.

## 368: What happens if you roll back a deploy after it stored new event types?

The old code version now meets events it doesn't know, like a new `OrderSplit` event. If it fails on unknown events, aggregates with those events can't be loaded, and the rollback breaks things worse than the bug.

Prevent it:

- Deploy reading support for new events first, in a release that doesn't produce them yet.
- Then deploy the change that produces them.
- Make aggregates and projections tolerant: unknown events either fail loudly in a controlled way or are ignored, depending on whether they affect state.

## 369: What is forward compatibility, and why does it matter for events?

Forward compatibility means old code can read data written by newer code. For events, an old consumer must handle events from a newer producer, for example by ignoring new fields.

It matters because producers and consumers are deployed independently, and during rollbacks old code reads newer events. Use tolerant readers, add only optional fields, and use a schema registry mode that checks forward or full compatibility.

## 370: What do you do when a bug produced wrong events?

The events are part of history and other services may already have reacted to them. So:

1. Fix the bug so no more wrong events are produced.
2. Find the affected streams.
3. Append correcting events, like `ShippingFeeCorrected`, with a reason that links to the incident.
4. Check what downstream services did with the wrong events, and whether they need correction too (refunds, emails).

Editing or deleting the stored events is a last resort, and only if no one outside has consumed them.

## 371: How do you fix a read model after a projection bug?

1. Fix the projection code and add a test for the case that broke.
2. If the bug only affects some entities, replay just their streams into the read model.
3. If it affects everything, rebuild the whole read model into a new table and switch over.
4. Check that side-effect handlers are not part of the replay.

This is one of the strongest points of event sourcing and stored events: read model bugs are always fixable, because the source data is intact.

## 372: What if a side-effect handler ran on wrong data?

Unlike read models, side effects like emails, payments or API calls to partners can't be replayed away. You need business compensation:

- Identify affected cases by event ids and correlation ids from logs.
- Run compensating actions: refunds, correction emails, calls to partner APIs.
- If possible, build this as a one-off command run through the normal command path, so it creates proper events and audit records.

This is why it pays to keep side effects few, idempotent and well logged.

## 373: Why must process managers be deterministic when replayed?

If a process manager is event-sourced (its state is built from events it received), loading it means replaying those events. If its decision logic depends on the current time, random values or external calls during replay, the rebuilt state may differ from what it originally was.

Keep decisions based only on the events and stored data. Record results of external calls as events. Workflow engines like Temporal enforce this rule for workflow code for the same reason.

## 374: How does event sourcing help with debugging production issues?

You can take the exact events of the stream that misbehaved and replay them locally, in a test or debugger, to see the state after each event. This reproduces the issue exactly, without guessing what the data looked like.

You can also write a regression test from the real events. Make sure to anonymize personal data before copying events out of production.

## 375: What affects the write performance of an event store?

- Append path: one insert per event, index maintenance on `(stream_id, version)` and the global position.
- Concurrency control: unique constraint checks or locks per stream.
- Global ordering: if appends are serialized to avoid gaps, that becomes the bottleneck.
- Durability: fsync on commit and replication.
- Event size: big JSON payloads cost more I/O.

Batching several events per transaction, keeping payloads small and avoiding a global lock when possible are the main levers.

## 376: How do you tune a PostgreSQL table used as an event store?

- Use `bigint` positions and keep the main indexes few: primary key on position, unique `(stream_id, version)`.
- Partition by time or position range if the table grows huge, so old partitions can be archived.
- A BRIN index on `created_at` is tiny and works well for append-only, time-ordered data.
- Use `jsonb` for payloads, but don't index into them unless a query really needs it.
- Tune autovacuum less aggressively than for update-heavy tables, since rows are rarely updated or deleted.

Measure with real volumes. Many systems run fine on one PostgreSQL instance with hundreds of millions of events.

## 377: How do you run one projection in parallel without breaking order?

Split it by stream id: each worker handles streams whose `hash(stream_id) % N` equals its number. Events of one stream stay in order within one worker, and workers run in parallel.

Each worker keeps its own checkpoint. This only works if the projection doesn't need order across different streams. If it does, like a projection that tracks totals across all orders in time order, it has to stay single-threaded or be redesigned.

## 378: How do you make sure only one instance runs a projection?

If you run several copies of a service for availability, only one should run a given projection, or they'll process the same events in parallel. Options:

- A lock in the database, like a PostgreSQL advisory lock, held while running.
- A lease with expiry in a table or in a tool like etcd or Consul.
- Kubernetes leader election.
- Let the broker do it: one partition per projection in a consumer group.

The instance that holds the lock runs the projection. Others wait and take over if it dies.

## 379: How do you use a PostgreSQL advisory lock for a single projection runner?

```ts
const LOCK_ID = 42_001; // one fixed number per projection

async function runIfLeader(pool: Pool) {
  const client = await pool.connect();
  try {
    const { rows } = await client.query(
      "SELECT pg_try_advisory_lock($1) AS ok",
      [LOCK_ID],
    );
    if (!rows[0].ok) return; // another instance is running it
    await runProjectionLoop(client); // keep using this same connection
  } finally {
    await client
      .query("SELECT pg_advisory_unlock($1)", [LOCK_ID])
      .catch(() => {});
    client.release();
  }
}
```

Session-level advisory locks are released when the connection closes, so if the leader crashes, another instance gets the lock on its next try. Be careful with connection poolers like PgBouncer in transaction mode, which don't keep session locks.

## 380: How do you store the projection checkpoint together with the read model update?

Do both in one transaction, so a crash can't leave them out of sync:

```ts
async function applyBatch(pool: Pool, events: StoredEvent[]) {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");
    for (const e of events) {
      await project(client, e);
    }
    await client.query(
      `INSERT INTO projection_checkpoints (name, position) VALUES ('order_summary', $1)
       ON CONFLICT (name) DO UPDATE SET position = EXCLUDED.position`,
      [events[events.length - 1].globalPosition],
    );
    await client.query("COMMIT");
  } catch (err) {
    await client.query("ROLLBACK");
    throw err;
  } finally {
    client.release();
  }
}
```

After a crash, the projection restarts from exactly the last committed checkpoint, and the read model matches it. This gives exactly-once updates for the read model.

## 381: What if the read model lives in a different database than the checkpoint?

You can't use one transaction, so make each update idempotent and safe to repeat:

- Store the stream version on each read model row and only update when the incoming version is newer.
- Use upserts instead of inserts.
- Save the checkpoint after the read model write. If you crash in between, some events are replayed, and the version check ignores them.

For Elasticsearch, external versioning (`version_type=external`) does this check in the store itself.

## 382: How can concurrent handlers cause lost updates in a read model?

If two workers process events for the same entity at the same time and both do "read row, change in memory, write row", the second write overwrites the first. For example, two `ItemAdded` events each add an item, but only one ends up in the list.

Fixes: process events for one entity in one worker (partition by entity id), use atomic database operations like `UPDATE ... SET count = count + 1` or `jsonb` array appends, or check versions on write.

## 383: What happens to ordering if you add partitions to an existing Kafka topic?

Kafka picks a partition by hashing the key modulo the partition count. When the count changes, many keys map to a different partition. New events for an order can go to a new partition while older events for it still wait in the old one, and a different consumer may process them first.

To change partition count safely: create a new topic with the new count, stop producers, let consumers drain the old topic, then switch to the new one. Or accept short reordering if consumers handle it with version checks.

## 384: How do you choose a key for an event that involves several entities?

Pick the entity whose order matters most for consumers. For `MoneyTransferred` between accounts A and B, keying by A keeps A's events in order but not B's.

Options:

- Split it into two events, `MoneyDebited` for A and `MoneyCredited` for B, each keyed by its own account.
- Key by the transfer id and let consumers handle ordering per account with versions.
- Publish to two topics with different keys.

There's no perfect answer. Choose based on what the important consumers need.

## 385: What is fan-out explosion, and how do you avoid it?

One event triggers many events, and each of those triggers more. For example, `PriceListUpdated` for 100,000 products causes 100,000 `ProductPriceChanged` events, each causing cache updates, search reindexing and notifications.

Avoid it by publishing a summary event and letting consumers fetch what they need in bulk, by batching downstream work, by rate limiting producers of bulk events, and by giving bulk operations their own topic so they don't delay normal traffic.

## 386: When should you compress events?

Compression helps when events are text-heavy (JSON) and volume is high: it cuts network, disk and cross-zone costs. Kafka compresses whole batches on the producer, with `compression.type` set to `lz4`, `zstd`, `snappy` or `gzip`. Larger batches compress better.

Zstd gives a good ratio, LZ4 is very fast. Compression costs some CPU on producers and consumers. For small volumes it doesn't matter much, and switching to a binary format like Avro or Protobuf may save more than compression does.

## 387: How do producer batching settings trade latency for throughput?

Kafka producers group messages per partition into batches. `linger.ms` is how long to wait for more messages before sending, and `batch.size` is the max batch size in bytes. Since Kafka 4.0, the default `linger.ms` is 5 ms (it used to be 0).

A higher `linger.ms` means bigger batches, better compression and fewer requests, but each message waits a bit longer. For user-facing flows, keep it low. For bulk pipelines, raise it. Measure end-to-end latency, not just producer throughput.

## 388: What should you tune for RabbitMQ consumers under heavy load?

- **Prefetch**: high enough to keep the consumer busy, low enough not to hoard messages that other consumers could take. Start around 10 to 100 and measure.
- **Queue type**: quorum queues for durability, streams for replay and large fan-out.
- **Queue length limits** and overflow behavior, so a stuck consumer can't fill the broker's memory or disk.
- **Acks in batches** (`multiple: true`) for high throughput.
- **Several queues** instead of one huge queue, since one queue is handled by one Erlang process and can become a bottleneck.

## 389: What limits should you know about SQS FIFO?

- Throughput is limited per message group and per queue. High-throughput mode raises the queue limit a lot, but each message group is still processed one batch at a time.
- Deduplication works only within a 5-minute window.
- A message that keeps failing blocks its whole group until it succeeds or moves to the DLQ.
- Moving a message to the DLQ breaks ordering for that group.

Use many message groups (one per entity) to get parallelism, and don't put everything in one group unless you really need total order.

## 390: Should integration events be replayable by consumers?

It depends on what they're for. If integration events carry state (event-carried state transfer), new consumers want to replay them to build their local copy, so keep them in a log with long retention or compaction.

If they're notifications, replay is less useful, and consumers should get current state from an API or a snapshot topic instead. Decide per topic and document it, so consumers know if they can rely on history being there.

## 391: How do you keep a public event contract stable over years?

- Publish integration events separate from internal domain events.
- Include only what consumers need, using business terms.
- Only add optional fields, never change meaning or types.
- Version explicitly and support old versions for an announced period.
- Run compatibility checks in CI against all published versions.
- Have consumer contract tests or at least a list of known consumers.

Treat the event schema with the same care as a public REST API.

## 392: What problems come with event-carried state transfer at scale?

- Every consumer has its own copy of the data, and copies can drift if an event is missed or handled wrongly.
- Bootstrapping a new consumer needs full history or a snapshot.
- Personal data spreads to many services.
- Changing the event means changing every copy's schema.

Add reconciliation jobs that compare copies with the source, use compacted topics so new consumers can bootstrap, and carry only the fields consumers really need.

## 393: What is a reconciliation job, and why do event-driven systems need one?

A reconciliation job periodically compares data between systems and fixes or reports differences. For example, every night it compares order totals in the order service with invoices in billing.

Even with outboxes and idempotency, bugs, manual fixes and edge cases cause drift. Reconciliation is the safety net that catches it. It can emit correction events or open a ticket for a human.

## 394: How can a consumer detect that it missed an event?

If the producer adds a sequence number per entity (the stream version), the consumer can check that each event's version is exactly one more than the last it saw. A gap means an event was lost or is delayed.

On a gap, the consumer can wait a little for the missing event, fetch the current state from the owner's API, or request a replay. Without sequence numbers, missed events are invisible until a reconciliation job finds the difference.

## 395: What are heartbeat events used for?

A heartbeat event is a regular event, like every minute, that says "I'm alive and here's my latest position". Consumers and monitoring use it to tell "nothing happened" apart from "the producer is broken".

In stream processing, heartbeats or periodic watermarks also let time windows close when there are no real events. Without them, a quiet partition can hold back the watermark and delay every window.

## 396: How does a transactional inbox help with ordering and retries?

The consumer first saves every incoming message to an inbox table and acks it right away. A separate worker then processes inbox rows in order per entity, with its own retries and backoff.

This separates receiving from processing: the broker is never blocked, ordering per entity is handled in your database, and failed messages stay in the inbox with their error, ready to retry. The cost is more database writes and one more component.

## 397: What are the limits of broker-side deduplication?

- It only works within a time window (5 minutes for SQS FIFO).
- It only catches duplicates that have the same dedup id, so retries that generate a new id slip through.
- It only covers the broker hop, not duplicates caused by consumer crashes or reprocessing.
- Kafka's idempotent producer stops duplicates from producer retries in one producer session, not from application-level resends.

So broker dedup reduces duplicates but never replaces idempotent consumers.

## 398: How do you build a time-ordered view from events produced by several services?

Merging streams by timestamp is unreliable because of clock differences and delivery delays. Options:

- Accept rough order and sort by event time within a tolerance, with late events inserted later.
- Use a stream processor with watermarks to wait a bounded time for late events before emitting.
- If exact causal order matters, use causation ids to order related events and only sort unrelated ones by time.

Tell users of the view what level of order they can rely on.

## 399: Why can't you rely on the broker as a permanent backup of your data?

Brokers keep events only for their retention period, compaction can remove old values, and topics can be deleted or misconfigured. Replication protects against node failure, not against a bad delete, a bug that writes bad data or a full cluster loss.

Keep the source of truth in a database or event store with real backups, or archive topics to object storage (Kafka tiered storage or a sink connector). Test that you can restore from those archives.

## 400: How do you handle schema evolution for events stored for a very long time?

- Store the schema version with every event.
- Keep all old schemas in the registry, never delete them.
- Use transitive compatibility checks, so any old version can still be read.
- Maintain upcasters for every version step, with tests using real old events.
- Every few years, consider a copy-and-transform migration to drop very old versions.

The rule of thumb: assume any event you store today will be read by code written five years from now.

## 401: How would you design the order, payment and inventory flow for an online shop?

1. `PlaceOrder` creates the order in `pending` state and writes `OrderPlaced` to the outbox.
2. An orchestrator (or workflow engine) starts. It sends `ReserveStock` first, since it's easy to undo, and sets a timeout.
3. On `StockReserved`, it sends `AuthorizePayment`. Authorizing instead of charging keeps payment easy to undo.
4. On `PaymentAuthorized`, the order is confirmed. Capture happens at shipping. This is the pivot.
5. On any failure or timeout, it compensates: release stock, void the authorization, mark the order cancelled.

All handlers are idempotent, messages are keyed by order id and the saga state is persisted with a version.

## 402: A user updates their profile, the page reloads and shows the old data. How do you fix it?

The page reads from a read model that hasn't processed the event yet. Fixes from simplest to most involved:

- The frontend keeps the values it just saved and shows them without refetching.
- The command returns the new version, and the query waits briefly until the read model has that version.
- The profile read model is updated in the same transaction as the write, since it's small and user-facing.
- After saving, the page reads that one profile from the write side.

I'd ask first if the read model needs to be async at all. For a profile page, often it doesn't.

## 403: Consumer lag keeps growing during peak hours. What do you check?

1. Is it all partitions or one? One means a hot key or a poison message.
2. What's the processing time per message, and where does it go (database, external API)?
3. Are there many retries or errors eating capacity?
4. Is the consumer CPU-bound, I/O-bound or waiting on locks?
5. Are there enough partitions to scale out?

Then: scale out, batch writes, parallelize per key, move slow work to a separate queue, and fix the slow query. Add autoscaling based on lag, not CPU.

## 404: Customers report receiving two confirmation emails. What happened, and how do you fix it?

Likely causes: the consumer crashed or rebalanced after sending but before committing, the visibility timeout was shorter than processing time, the outbox relay published twice, or two handlers both send emails.

Fix: make the email handler idempotent with a record keyed by event id (or by order id plus email type), written before or atomically with sending, and pass an idempotency key to the email provider if it supports one. Then check the root cause, such as raising the visibility timeout or committing more often.

## 405: A producer changed an event and a consumer started failing. How do you handle it?

Short term: roll back the producer or publish the old format again, and redrive the failed messages from the DLQ after the consumer is fixed or the producer is reverted.

Long term:

- Put schemas in a registry with compatibility checks in CI.
- Use tolerant readers in consumers.
- Add consumer contract tests to the producer's pipeline.
- Agree on the rule that breaking changes go through a new version with an overlap period.

## 406: The business wants a report on how many customers removed items from their cart before buying, over the last two years. How do you do it?

If the cart is event-sourced, or `ItemRemovedFromCart` events were stored somewhere long-term, write a new projection and run it over the historical events. That's exactly the kind of question event sourcing makes possible.

If only the current state of carts was stored, the history is gone. You can start capturing the events now and report from now on. This is a good example to use when explaining why storing events can be worth it.

## 407: Rebuilding a projection takes several days. How do you make it faster?

- Parallelize by stream id hash, if the projection allows it.
- Batch writes to the read store and disable expensive indexes during the rebuild.
- Read events in large pages.
- Skip event types the projection doesn't use, ideally with a filtered read on the server side.
- Profile the projection code. Often it's one slow query per event.
- Start from a recent snapshot of the read model if one exists, and replay only newer events.

Also ask whether the projection really needs every event from the beginning.

## 408: One aggregate's stream has a million events and loading it is slow. What do you do?

First, check if the aggregate is designed well. A stream that large often means the aggregate collects things that don't need to be checked together, like an account that holds every transaction forever.

Options:

- Split the aggregate, for example one per month or per sub-entity.
- Close the books periodically and start a new stream with the carried-over state.
- Add snapshots as a quick fix.
- Cache loaded aggregates in memory, with version checks.

## 409: The broker was down for an hour during a sale. What happens, and what do you check afterwards?

With outboxes, services kept accepting orders, and events piled up in outbox tables. When the broker came back, relays sent the backlog.

Afterwards, check:

- Outbox backlogs drained and oldest unpublished age is back to normal.
- Consumer lag is back to normal, and downstream systems survived the burst.
- DLQs for errors caused by the burst, like timeouts.
- Sagas that hit timeouts during the outage and cancelled orders that were actually fine.
- Any service that published directly without an outbox and lost events.

The saga timeouts are the easy one to forget.

## 410: Two services disagree about an order's status. How do you investigate?

1. Get the order's event history from the owner service (or its outbox log).
2. Check which events the other service received and processed, using logs by order id and its inbox or processed-events table.
3. Look for missed events, events processed out of order or a failed message in a DLQ.
4. Check if the other service changed the status itself, which breaks single ownership.

Fix the data with a correcting event or by resyncing from the owner, then fix the cause. Add a reconciliation job if this can happen again.

## 411: Ordering broke after you scaled a consumer from one instance to many. Why?

With one instance, messages were processed one at a time, so order was kept by accident. With several instances on a plain queue (or SQS standard), messages for the same entity go to different instances and finish in any order.

Fix by keeping order per key: use Kafka partitions or SQS FIFO message groups keyed by entity id, or RabbitMQ consistent hash exchanges or single active consumer per queue. Also make handlers check versions so a late older event can't overwrite newer data.

## 412: How would you model a bank account with event sourcing and a no-overdraft rule?

The account is an aggregate with its own stream. The `Withdraw` command loads the account, checks `amount <= balance` and appends `MoneyWithdrawn` with the expected version.

If two withdrawals run at the same time, one fails on the version check and retries with the new balance, so the rule can't be broken. Transfers between accounts use a saga: debit A, then credit B, and if crediting fails, reverse the debit with a compensating event. A balance read model is built from the events for fast display.

## 413: How would you prevent double-booking seats for a popular concert?

The seat or section is the consistency boundary. Options:

- Model each section as an aggregate. A booking command reserves specific seats with optimistic concurrency. Conflicts retry with fresh state.
- Use a database unique constraint on `(event_id, seat_id)` in a reservation table. The second insert fails.
- Put a queue in front and process bookings for one section one at a time.

Reservations get an expiry, like 10 minutes. A timeout releases seats if payment doesn't complete. The seat map shown to users is a read model that may be a second behind, so the final check is always on the write side.

## 414: How would you design stock reservations that expire?

`ReserveStock` decreases available stock and creates a reservation with an expiry time, all in one aggregate or transaction. A scheduler or delayed message sends `ExpireReservation` at the expiry time.

When it runs, the handler checks the reservation's state. If it's still pending, it releases the stock and publishes `ReservationExpired`. If it was already confirmed or cancelled, it does nothing. Confirming must also check that the reservation hasn't expired, since the two can race.

## 415: How would you start moving a monolith to an event-driven design?

1. Find the bounded contexts inside the monolith.
2. Add an in-process event bus and publish domain events at key points, using an outbox.
3. Make modules react to events instead of calling each other directly.
4. Start sending integration events to a broker.
5. Extract one context at a time into a service that consumes those events and owns its data.
6. Use CDC on the monolith's database where adding events in code is too hard.

Start with a part that has clear boundaries and low risk, and get the operational basics (tracing, DLQs, alerts) right before moving important flows.

## 416: How would you design ingestion for millions of IoT sensor events per minute?

- Devices send to a gateway or MQTT broker that forwards into Kafka, Kinesis or a similar log, keyed by device id.
- Validate and enrich in a stream processor, and drop or quarantine bad data.
- Aggregate in time windows (per minute, per hour) for dashboards, using event time and watermarks.
- Store raw events in cheap object storage for later analysis.
- Raise alert events only when thresholds are crossed, not for every reading.

Don't run a database write per reading. Batch everything, and plan for late and duplicate messages from devices with poor connections.

## 417: Auditors need a complete, tamper-evident history of changes. How do events help?

Event sourcing gives a complete history by design: every change is an event with who, what and when. To make it tamper-evident:

- Make the event table append-only in the database, with no update or delete permissions for the application.
- Chain events with hashes, where each event stores a hash of the previous one, and store periodic checkpoints somewhere separate.
- Archive to write-once storage, like S3 Object Lock.

Even without full event sourcing, you can store all published events in such an archive for audit.

## 418: Your team wants to use CQRS and event sourcing everywhere. How do you respond?

I'd ask what problem each part of the system has. Most parts are simple CRUD with no complex rules and no need for history, and full CQRS with event sourcing would add a lot of code, eventual consistency and a learning curve without benefit.

I'd suggest using it where it pays off, like the core domain with complex rules or audit needs, and simple layered CRUD elsewhere. We could start with "CQRS-lite" (separate read and write code in one database) and add more only when there's a clear reason.

## 419: How do you bring third-party webhooks into your event-driven system?

1. Receive the webhook, verify its signature, and store the raw payload with the provider's event id.
2. Return 2xx quickly, before doing any business work.
3. Translate it into your own event or command in an anti-corruption layer, and publish through your outbox.
4. Deduplicate by the provider's event id, since providers retry.
5. Don't rely on their order. Fetch the current state from their API if needed.

Keep the raw payloads for a while, for debugging and replays.

## 420: How would you design a notification service driven by events?

- It subscribes to business events like `OrderShipped` and `PasswordChanged`.
- A rules step decides who to notify, through which channels (email, SMS, push), based on user preferences, which it keeps as a local copy from user events.
- It renders templates per language and creates one job per channel.
- Channel workers send through providers, with retries, rate limits and idempotency keys per notification.
- It records every notification sent, for support and to avoid duplicates.

Business services never call email or SMS providers directly. They only publish events.

## 421: How do you keep a search index in sync with your database?

- A projection consumes domain events (or CDC events from an outbox) and updates the index.
- Use the entity version as an external version in Elasticsearch or OpenSearch, so older updates can't overwrite newer ones.
- Use bulk requests for throughput.
- Have a full reindex process into a new index plus an alias switch, for mapping changes and recovery.
- Run a reconciliation job that compares counts or checksums with the source.

Never update the index from the request handler directly, or a failed index call means the index silently drifts.

## 422: How would you build a multi-day approval workflow?

Use a workflow engine or a persisted process manager:

1. `SubmitRequest` starts the process and records `RequestSubmitted`.
2. It sends tasks to approvers and waits for `RequestApproved` or `RequestRejected`, with reminders after N days and escalation after M days, scheduled as timers.
3. Each decision is a command, checked against the current step (only the right approver, only once).
4. When all approvals are in, it publishes `RequestFullyApproved` and other services react.

State survives restarts and deploys, and the full history of who approved what and when is kept.

## 423: A downstream API goes down and your consumers' retries make the recovery harder. What do you change?

The retries create a retry storm: when the API starts recovering, it gets hit by everything at once and falls over again.

Changes:

- Exponential backoff with jitter and a cap.
- A circuit breaker that pauses consumption while the API is down.
- A rate limit on calls, especially during catch-up.
- Retry budgets: limit retries to a share of normal traffic.
- Respect `Retry-After` headers.

The goal is that recovery traffic ramps up slowly instead of arriving as one big wave.

## 424: A projection rebuild accidentally sent thousands of emails. What went wrong, and how do you prevent it?

The rebuild replayed events through a handler that had a side effect. Either the email logic lived inside the projection, or the email handler shared the projection's subscription and checkpoint.

Prevention:

- Keep side effects in separate handlers with their own checkpoints, never reset during rebuilds.
- Make sending idempotent per event id, stored in a table that rebuilds don't clear.
- Add a guard that skips side effects for events older than a threshold.
- Review and test rebuild procedures on staging first.

Then handle the incident: tell affected customers and check for other side effects that ran.

## 425: An event handler needs data from another service that isn't in the event. What are your options?

- Call the other service's API when handling the event. Simple, but adds runtime coupling and fails if it's down. Use retries.
- Keep a local copy of that data, built from the other service's events. Fast and resilient, but more work and slightly stale.
- Ask the producer to add the field to the event, if many consumers need it.
- Use an enrichment step in a stream processor that joins the data in.

For data that rarely changes, a local copy is usually best. For data that must be fresh, call the API.

## 426: The business needs gapless invoice numbers. How do you generate them in an event-driven system?

Gapless numbers need one place that hands them out in order, so they can't be generated freely in parallel. Options:

- A counter row per series in the database, incremented in the same transaction that issues the invoice (`UPDATE ... RETURNING`). It serializes invoice creation, which is usually acceptable for invoice volumes.
- Assign the number in a single consumer of `InvoiceIssued` events, processed one at a time per series.

Don't use database sequences, because rolled-back transactions leave gaps. Assign the number only when the invoice is final, not when a draft is created.

## 427: How would you model a shopping cart with event sourcing?

Each cart is a stream with events like `CartCreated`, `ItemAdded`, `ItemQuantityChanged`, `ItemRemoved`, `CouponApplied` and `CartCheckedOut`. The aggregate checks rules like maximum quantity and no changes after checkout.

The checkout command produces `CartCheckedOut`, which starts the order flow. Read models give the current cart view, and analytics get abandoned-cart and removed-item data for free. Carts that are never checked out can be closed with a `CartExpired` event after some time.

## 428: How would you build a reporting database from events?

- A set of consumers write events into a warehouse or analytics database, either as raw event tables or as modeled fact and dimension tables.
- Use bulk loads or a connector instead of row-by-row inserts.
- Keep event time, ids and versions so reports can be rebuilt and deduplicated.
- Handle schema changes with versioned tables or flexible columns.
- Mask personal data that analysts don't need.

Reports then use the same business events as the services, so numbers match what actually happened.

## 429: How would you design outgoing webhooks for your customers?

- Internal events feed a webhook service that matches them to customer subscriptions.
- Each delivery is a job with a unique event id, signed with an HMAC secret per customer, and a timestamp to prevent replays.
- Retry with exponential backoff for a day or more, and disable endpoints that keep failing, with a notice to the customer.
- Keep a delivery log customers can see, and a way to resend events.
- Rate limit per endpoint so one slow customer doesn't slow others.

Tell customers that deliveries can be duplicated and out of order, and that they should dedupe by event id.

## 430: How can you do event sourcing on a serverless AWS stack?

- Store events in DynamoDB with the stream id as partition key and version as sort key.
- Use conditional writes for optimistic concurrency.
- Turn on DynamoDB Streams, and let a Lambda read new events and update read models or publish to EventBridge or SNS.
- Read models live in DynamoDB tables, OpenSearch or S3, shaped for queries.

DynamoDB Streams keep records for 24 hours, so for full replay you also need the table itself (scan or query by stream) or an archive in S3. Items are limited to 400 KB.

## 431: How do you append events with optimistic concurrency in DynamoDB?

Write each new event as an item with a condition that its key doesn't exist yet. For several events, use a transaction:

```ts
import {
  DynamoDBClient,
  TransactWriteItemsCommand,
} from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({});

async function append(
  streamId: string,
  expectedVersion: number,
  events: { type: string; data: unknown }[],
) {
  await client.send(
    new TransactWriteItemsCommand({
      TransactItems: events.map((e, i) => ({
        Put: {
          TableName: "events",
          Item: {
            streamId: { S: streamId },
            version: { N: String(expectedVersion + i + 1) },
            type: { S: e.type },
            data: { S: JSON.stringify(e.data) },
          },
          ConditionExpression: "attribute_not_exists(version)",
        },
      })),
    }),
  );
}
```

If another writer already added that version, the transaction fails with a `TransactionCanceledException`, and you reload and retry. A transaction can hold up to 100 items.

## 432: When would you use Redis Streams for events?

Redis Streams are an append-only log inside Redis, with consumer groups (`XREADGROUP`), acknowledgments (`XACK`) and a pending list for messages that were read but not acked, which you can claim with `XAUTOCLAIM`.

They're good for moderate volume, low latency and teams that already run Redis. Limits: data lives in memory (trim streams with `MAXLEN` or `MINID`), durability depends on Redis persistence settings, and they lack the long retention and ecosystem of Kafka. For critical business events, check that your Redis setup really won't lose data on failover.

## 433: What is NATS JetStream, and how does it compare to Kafka?

NATS is a lightweight messaging system, and JetStream is its persistence layer. It adds streams that store messages, consumers with acks and redelivery, replay from a point, deduplication by message id within a window and key-value and object stores on top.

Compared to Kafka, it's simpler to run, starts as a single small binary and has low latency, with flexible subject-based routing. Kafka has a bigger ecosystem (connectors, stream processing) and is more proven for very high throughput and long retention. JetStream is a good fit for edge, IoT and smaller platforms.

## 434: How do database isolation levels affect event handlers?

Under `READ COMMITTED` (PostgreSQL's default), two handlers can read the same row, both decide based on it and both write, causing lost updates or broken rules. For example, two "reserve stock" handlers both see 1 item left.

Options: use atomic statements (`UPDATE stock SET qty = qty - 1 WHERE id = $1 AND qty > 0`), row locks with `SELECT ... FOR UPDATE`, version checks, or `SERIALIZABLE` isolation with retries on serialization failures. Atomic conditional updates are usually the simplest and fastest.

## 435: The outbox relay has fallen behind by millions of rows. What do you do?

1. Find out why: broker slow, relay slow, a stuck row, a big batch insert or slow queries due to table bloat.
2. Make sure the relay's query uses an index on unpublished rows.
3. Publish in batches and wait for broker acks per batch, not per message.
4. Partition the work by aggregate id across several relay workers, keeping order per aggregate.
5. Consider switching to CDC, which doesn't need to query the table.

While catching up, warn downstream teams, since a sudden burst of old events may hit their consumers.

## 436: How do you safely replace a consumer with a rewritten version?

Run both side by side for a while:

1. The new consumer reads the same events in its own consumer group, but writes to a shadow store or runs with side effects turned off.
2. Compare its results with the old consumer's, automatically where possible.
3. Fix differences until they match.
4. Switch: stop the old consumer and enable the new one's side effects, starting from the right offset so nothing is skipped or doubled.

Keep the old one ready to turn back on for a short period.

## 437: You need to split one large topic into two. How do you do it without breaking consumers?

1. Create the new topics.
2. Make the producer publish to both the old topic and the new ones (through the outbox, so it's consistent).
3. Move consumers one by one to the new topics, starting each from a point that matches its position on the old topic. A time-based offset lookup helps.
4. When no one reads the old topic, stop publishing to it and delete it after retention.

If consumers need history, backfill the new topics from the old one before switching.

## 438: How do you rename an event type that's already stored and published?

Renaming is a breaking change for consumers and stored events. Steps:

- For stored events, map the old name to the new one when reading (a type alias or upcaster), without changing stored data.
- For consumers, publish both names for a while, or have consumers accept both.
- Update the schema registry and docs, and mark the old name deprecated.
- Remove the old name only when no consumers use it, but keep the read mapping forever for stored events.

Often it's not worth it. A slightly odd name is cheaper than a migration.

## 439: A payment provider sends webhook events duplicated and out of order. How do you handle it?

- Deduplicate by the provider's event id.
- Don't trust the order of events. Use the timestamp or version in the payment object if there is one, and ignore events older than what you have.
- For important state changes, fetch the current object from the provider's API instead of trusting the event payload.
- Model the payment as a state machine that only allows valid transitions, so a late "pending" after "succeeded" is ignored.

Stripe, for example, documents that it doesn't guarantee delivery order and that you should handle duplicates.

## 440: How do you make sure a confirmation email is sent once and only once?

You can't guarantee exactly once with an external provider, but you can get very close:

1. Consume `OrderPlaced` with at-least-once delivery.
2. Insert a row `(order_id, 'confirmation')` with a unique constraint and status `sending` before sending. If it exists and is `sent`, skip.
3. Send with an idempotency key, if the provider supports one.
4. Mark the row `sent`.

If the process crashes between sending and marking, a retry finds `sending` and has to decide: risk a duplicate or risk no email. For a confirmation, a rare duplicate is the better choice.

## 441: How do you test a new version of a projection before switching to it?

Build the new version into a separate read model alongside the old one, from the same events. Then:

- Compare the two automatically: row counts, checksums and a sample of entities.
- Route a small share of read traffic to the new one, or compare responses in the background (shadow reads).
- Look at differences: each one is either an intended change or a bug.

Switch only when differences are explained. Since both are built from events, you can repeat this as often as needed.

## 442: Customer support wants a full timeline of an order across all services. How do you build it?

Build a timeline read model:

- A projection subscribes to events from all relevant services (orders, payments, shipping, support tickets).
- It stores entries keyed by order id with event time, type, source and a short human-readable description.
- It uses correlation ids to link events that don't carry the order id directly.
- The support tool reads the timeline sorted by event time.

Make it tolerant of late and out-of-order events, and don't copy sensitive data support shouldn't see.

## 443: A legacy system only produces nightly batch files. How do you connect it to an event-driven platform?

Write an adapter that:

1. Picks up the file when it arrives and records that it was processed (to avoid double imports).
2. Compares each record with the previous state, if the file is a full dump, to find what changed.
3. Turns each change into a proper event, like `PriceChanged`, with the file's business date as event time.
4. Publishes through an outbox, in batches.

Consumers then don't know or care that the source is a batch file, and the adapter can be replaced if the legacy system ever gets a real API.

## 444: How do you enforce "at most 3 password resets per day" in an event-sourced system?

Model a small aggregate per user for this rule, like `PasswordResetLimiter`, with events `PasswordResetRequested`. Its state is the list of request times in the last 24 hours (old ones are dropped when applying events).

The command checks the count and either appends the event or rejects. Optimistic concurrency makes sure two parallel requests can't both pass. Keeping this rule out of the main user aggregate avoids conflicts with unrelated user changes.

## 445: How do you safely retire a service that publishes events?

1. Find all consumers of its topics, from broker metrics, consumer groups, docs and an event catalog.
2. Agree on where the data will come from in future: a new owner service or nowhere.
3. If a new service takes over, have it publish the same events (or new versions) and move consumers.
4. Mark the topics deprecated, monitor for remaining readers and set a removal date.
5. Archive the topic data if it may be needed for replay or audit.

The hard part is usually finding the forgotten consumer that nobody documented.

## 446: A tenant asks for an export of all their data. How do events make it easier or harder?

Easier: with event sourcing, you have the full history per entity, and if events carry a tenant id, you can export everything with one filtered read, including history if they want it.

Harder: their data is also copied into many read models, caches and other services' local copies. A complete export means collecting from the owning services (which hold the truth), not from every copy. Good data ownership makes this clear: export from owners only.

## 447: A Kafka consumer keeps getting kicked out of its group while processing long tasks. What's going on?

The consumer has to call `poll()` again within `max.poll.interval.ms` (5 minutes by default). If processing a batch takes longer, the broker thinks it's dead, starts a rebalance and gives its partitions to others. The work is then repeated, which can loop.

Fixes: lower `max.poll.records` so batches are smaller, raise `max.poll.interval.ms` if tasks are legitimately long, move very long work to a separate job queue and only commit the hand-off, or pause the partition while working and keep polling.

## 448: What are the main questions to ask before choosing EDA, CQRS or event sourcing?

- Do different parts of the system need to evolve and scale independently? (EDA)
- Are reads and writes really different in shape or load? (CQRS)
- Does the business need the history of changes, not just current state? (event sourcing)
- Can users accept some delay before seeing changes elsewhere?
- Does the team have the experience and tools to run brokers and debug async flows?
- Is there a simpler option, like one database with views, that solves the problem?

If most answers point to "no", a well-structured monolith with a single database is the better choice.

## 449: How do EDA, CQRS and event sourcing fit together in one system?

- **Event sourcing** stores the write side of a service as events.
- **CQRS** builds read models from those events for queries.
- **Event-driven architecture** publishes integration events so other services can react.

Each can be used without the others. A common setup is: most services use normal tables with an outbox to publish events, a few core services use event sourcing internally, and CQRS read models exist wherever queries need a different shape.

## 450: You join a team with an existing event-driven system. What do you look at first?

1. Is there a list of events, producers and consumers? If not, build one from the broker and code.
2. How are events published: outbox or direct? Where can events be lost?
3. Are consumers idempotent? Check a few handlers.
4. What's in the DLQs right now, and does anyone get alerted?
5. Can you follow one business flow end to end by correlation id or trace?
6. What's the consumer lag, and how is it monitored?
7. How are schema changes handled and checked?

The answers quickly show where the next incident is likely to come from.
