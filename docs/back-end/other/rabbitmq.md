# RabbitMQ Interview Questions and Answers

_Last updated: October 28, 2026_

450 RabbitMQ interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target current RabbitMQ: the 4.x series up to RabbitMQ 4.4 (released in October 2026), with quorum queues, streams, Khepri as the metadata store and native AMQP 1.0. Code examples use Node.js with amqplib. Older things like classic mirrored queues, lazy queues, Mnesia and the partition handling strategies are mentioned where they still matter, since you will still see them in real projects and in interviews.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is RabbitMQ?](#1-what-is-rabbitmq)
- [2: What is a message broker?](#2-what-is-a-message-broker)
- [3: Why would you use a message queue instead of calling a service directly?](#3-why-would-you-use-a-message-queue-instead-of-calling-a-service-directly)
- [4: Which protocols does RabbitMQ support?](#4-which-protocols-does-rabbitmq-support)
- [5: What is AMQP 0-9-1?](#5-what-is-amqp-0-9-1)
- [6: Why is RabbitMQ written in Erlang and why does it matter?](#6-why-is-rabbitmq-written-in-erlang-and-why-does-it-matter)
- [7: What is a producer?](#7-what-is-a-producer)
- [8: What is a consumer?](#8-what-is-a-consumer)
- [9: What is a queue in RabbitMQ?](#9-what-is-a-queue-in-rabbitmq)
- [10: What is an exchange?](#10-what-is-an-exchange)
- [11: What is a binding?](#11-what-is-a-binding)
- [12: What is a routing key?](#12-what-is-a-routing-key)
- [13: What is the difference between a routing key and a binding key?](#13-what-is-the-difference-between-a-routing-key-and-a-binding-key)
- [14: What exchange types does RabbitMQ have?](#14-what-exchange-types-does-rabbitmq-have)
- [15: How does a direct exchange work?](#15-how-does-a-direct-exchange-work)
- [16: How does a fanout exchange work?](#16-how-does-a-fanout-exchange-work)
- [17: How does a topic exchange work?](#17-how-does-a-topic-exchange-work)
- [18: What is the difference between * and # in topic bindings?](#18-what-is-the-difference-between--and--in-topic-bindings)
- [19: How does a headers exchange work?](#19-how-does-a-headers-exchange-work)
- [20: What is the default exchange?](#20-what-is-the-default-exchange)
- [21: What are the amq.* exchanges?](#21-what-are-the-amq-exchanges)
- [22: What is a virtual host (vhost)?](#22-what-is-a-virtual-host-vhost)
- [23: What is a connection in RabbitMQ?](#23-what-is-a-connection-in-rabbitmq)
- [24: What is a channel?](#24-what-is-a-channel)
- [25: Why does RabbitMQ use channels instead of many TCP connections?](#25-why-does-rabbitmq-use-channels-instead-of-many-tcp-connections)
- [26: What does a RabbitMQ message consist of?](#26-what-does-a-rabbitmq-message-consist-of)
- [27: What are the most common message properties?](#27-what-are-the-most-common-message-properties)
- [28: What is a message acknowledgment?](#28-what-is-a-message-acknowledgment)
- [29: What is the difference between automatic and manual acknowledgment?](#29-what-is-the-difference-between-automatic-and-manual-acknowledgment)
- [30: What happens if a consumer dies without acknowledging a message?](#30-what-happens-if-a-consumer-dies-without-acknowledging-a-message)
- [31: What is the difference between basic.nack and basic.reject?](#31-what-is-the-difference-between-basicnack-and-basicreject)
- [32: What does requeue mean?](#32-what-does-requeue-mean)
- [33: What is the redelivered flag?](#33-what-is-the-redelivered-flag)
- [34: What is a durable queue?](#34-what-is-a-durable-queue)
- [35: What is a persistent message?](#35-what-is-a-persistent-message)
- [36: If a queue is durable, are its messages safe after a restart?](#36-if-a-queue-is-durable-are-its-messages-safe-after-a-restart)
- [37: What is an exclusive queue?](#37-what-is-an-exclusive-queue)
- [38: What is an auto-delete queue?](#38-what-is-an-auto-delete-queue)
- [39: What is a server-named queue?](#39-what-is-a-server-named-queue)
- [40: What queue types does RabbitMQ have?](#40-what-queue-types-does-rabbitmq-have)
- [41: What is a classic queue?](#41-what-is-a-classic-queue)
- [42: What is a quorum queue?](#42-what-is-a-quorum-queue)
- [43: What is a RabbitMQ stream?](#43-what-is-a-rabbitmq-stream)
- [44: How do you run RabbitMQ locally?](#44-how-do-you-run-rabbitmq-locally)
- [45: What are the default ports used by RabbitMQ?](#45-what-are-the-default-ports-used-by-rabbitmq)
- [46: What is the management plugin?](#46-what-is-the-management-plugin)
- [47: What is the guest user?](#47-what-is-the-guest-user)
- [48: How do you create a user and give them access to a vhost?](#48-how-do-you-create-a-user-and-give-them-access-to-a-vhost)
- [49: What do configure, write and read permissions mean?](#49-what-do-configure-write-and-read-permissions-mean)
- [50: What are user tags?](#50-what-are-user-tags)
- [51: What is rabbitmqctl?](#51-what-is-rabbitmqctl)
- [52: What is rabbitmq-plugins?](#52-what-is-rabbitmq-plugins)
- [53: What is rabbitmq-diagnostics?](#53-what-is-rabbitmq-diagnostics)
- [54: What is rabbitmqadmin?](#54-what-is-rabbitmqadmin)
- [55: How do you enable a plugin?](#55-how-do-you-enable-a-plugin)
- [56: What is rabbitmq.conf?](#56-what-is-rabbitmqconf)
- [57: What is a RabbitMQ node?](#57-what-is-a-rabbitmq-node)
- [58: What is a RabbitMQ cluster?](#58-what-is-a-rabbitmq-cluster)
- [59: What is the Erlang cookie?](#59-what-is-the-erlang-cookie)
- [60: How do you connect to RabbitMQ from Node.js?](#60-how-do-you-connect-to-rabbitmq-from-nodejs)
- [61: How do you send a message to a queue in Node.js?](#61-how-do-you-send-a-message-to-a-queue-in-nodejs)
- [62: How do you consume messages in Node.js?](#62-how-do-you-consume-messages-in-nodejs)
- [63: How do you publish a message to an exchange in Node.js?](#63-how-do-you-publish-a-message-to-an-exchange-in-nodejs)
- [64: What does it mean that declaring a queue or exchange is idempotent?](#64-what-does-it-mean-that-declaring-a-queue-or-exchange-is-idempotent)
- [65: What happens if you declare an existing queue with different arguments?](#65-what-happens-if-you-declare-an-existing-queue-with-different-arguments)
- [66: What is the work queue pattern?](#66-what-is-the-work-queue-pattern)
- [67: How does RabbitMQ distribute messages between several consumers of one queue?](#67-how-does-rabbitmq-distribute-messages-between-several-consumers-of-one-queue)
- [68: What is prefetch (basic.qos)?](#68-what-is-prefetch-basicqos)
- [69: What is the publish/subscribe pattern in RabbitMQ?](#69-what-is-the-publishsubscribe-pattern-in-rabbitmq)
- [70: What is the routing pattern?](#70-what-is-the-routing-pattern)
- [71: How do you do RPC (request/reply) with RabbitMQ?](#71-how-do-you-do-rpc-requestreply-with-rabbitmq)
- [72: Why do you need a correlation ID in RPC?](#72-why-do-you-need-a-correlation-id-in-rpc)
- [73: What is message TTL?](#73-what-is-message-ttl)
- [74: What is queue TTL (x-expires)?](#74-what-is-queue-ttl-x-expires)
- [75: What is a dead letter exchange (DLX)?](#75-what-is-a-dead-letter-exchange-dlx)
- [76: When does a message get dead-lettered?](#76-when-does-a-message-get-dead-lettered)
- [77: How do you limit the length of a queue?](#77-how-do-you-limit-the-length-of-a-queue)
- [78: What happens when a queue reaches its maximum length?](#78-what-happens-when-a-queue-reaches-its-maximum-length)
- [79: What are publisher confirms?](#79-what-are-publisher-confirms)
- [80: What is the mandatory flag?](#80-what-is-the-mandatory-flag)
- [81: What happens to a message that doesn't match any binding?](#81-what-happens-to-a-message-that-doesnt-match-any-binding)
- [82: What is an alternate exchange?](#82-what-is-an-alternate-exchange)
- [83: Does RabbitMQ support message priorities?](#83-does-rabbitmq-support-message-priorities)
- [84: How do you purge a queue?](#84-how-do-you-purge-a-queue)
- [85: How do you delete a queue?](#85-how-do-you-delete-a-queue)
- [86: How do you see which queues exist and how many messages they have?](#86-how-do-you-see-which-queues-exist-and-how-many-messages-they-have)
- [87: What are queue arguments (x-arguments)?](#87-what-are-queue-arguments-x-arguments)
- [88: What is a policy?](#88-what-is-a-policy)
- [89: What is the difference between a queue argument and a policy?](#89-what-is-the-difference-between-a-queue-argument-and-a-policy)
- [90: What are heartbeats?](#90-what-are-heartbeats)
- [91: What is a delivery tag?](#91-what-is-a-delivery-tag)
- [92: What is a consumer tag?](#92-what-is-a-consumer-tag)
- [93: How do you stop a consumer without closing the connection?](#93-how-do-you-stop-a-consumer-without-closing-the-connection)
- [94: What is the difference between basic.get and basic.consume?](#94-what-is-the-difference-between-basicget-and-basicconsume)
- [95: Does RabbitMQ keep messages in order?](#95-does-rabbitmq-keep-messages-in-order)
- [96: What delivery guarantees does RabbitMQ give?](#96-what-delivery-guarantees-does-rabbitmq-give)
- [97: What is the basic difference between RabbitMQ and Kafka?](#97-what-is-the-basic-difference-between-rabbitmq-and-kafka)
- [98: What is the difference between RabbitMQ and Redis pub/sub?](#98-what-is-the-difference-between-rabbitmq-and-redis-pubsub)
- [99: What are common use cases for RabbitMQ?](#99-what-are-common-use-cases-for-rabbitmq)
- [100: When is RabbitMQ not a good choice?](#100-when-is-rabbitmq-not-a-good-choice)
- [101: Is there a limit on message size?](#101-is-there-a-limit-on-message-size)
- [102: How do you tell consumers what format the message body is in?](#102-how-do-you-tell-consumers-what-format-the-message-body-is-in)
- [103: How do you send JSON with amqplib?](#103-how-do-you-send-json-with-amqplib)
- [104: What is the management HTTP API?](#104-what-is-the-management-http-api)
- [105: What is the memory alarm?](#105-what-is-the-memory-alarm)
- [106: What is the disk alarm?](#106-what-is-the-disk-alarm)
- [107: What happens to publishers when an alarm is triggered?](#107-what-happens-to-publishers-when-an-alarm-is-triggered)
- [108: Where are RabbitMQ logs and how do you change the log level?](#108-where-are-rabbitmq-logs-and-how-do-you-change-the-log-level)
- [109: How do you check if a RabbitMQ node is running and healthy?](#109-how-do-you-check-if-a-rabbitmq-node-is-running-and-healthy)
- [110: What do rabbitmqctl stop_app and start_app do?](#110-what-do-rabbitmqctl-stop_app-and-start_app-do)
- [111: What does rabbitmqctl reset do?](#111-what-does-rabbitmqctl-reset-do)
- [112: Can exchanges be durable or auto-delete?](#112-can-exchanges-be-durable-or-auto-delete)
- [113: What is an internal exchange?](#113-what-is-an-internal-exchange)
- [114: What is an exchange-to-exchange binding?](#114-what-is-an-exchange-to-exchange-binding)
- [115: What are message headers used for?](#115-what-are-message-headers-used-for)
- [116: How do you set an expiration on a single message?](#116-how-do-you-set-an-expiration-on-a-single-message)
- [117: Why set a message ID and timestamp?](#117-why-set-a-message-id-and-timestamp)
- [118: What is the Shovel plugin?](#118-what-is-the-shovel-plugin)
- [119: What is the Federation plugin?](#119-what-is-the-federation-plugin)
- [120: Does RabbitMQ support MQTT?](#120-does-rabbitmq-support-mqtt)
- [121: Does RabbitMQ support STOMP?](#121-does-rabbitmq-support-stomp)
- [122: Can a browser connect to RabbitMQ directly?](#122-can-a-browser-connect-to-rabbitmq-directly)
- [123: What is AMQP 1.0 in RabbitMQ?](#123-what-is-amqp-10-in-rabbitmq)
- [124: What is the stream protocol?](#124-what-is-the-stream-protocol)
- [125: What are feature flags?](#125-what-are-feature-flags)
- [126: What is Khepri?](#126-what-is-khepri)
- [127: What happened to classic mirrored queues?](#127-what-happened-to-classic-mirrored-queues)
- [128: What is the current version of RabbitMQ and how often are new versions released?](#128-what-is-the-current-version-of-rabbitmq-and-how-often-are-new-versions-released)
- [129: What Erlang version does RabbitMQ need?](#129-what-erlang-version-does-rabbitmq-need)
- [130: Which Docker image tag should you use?](#130-which-docker-image-tag-should-you-use)
- [131: How do you add RabbitMQ to a Docker Compose project?](#131-how-do-you-add-rabbitmq-to-a-docker-compose-project)
- [132: What do RABBITMQ_DEFAULT_USER and RABBITMQ_DEFAULT_PASS do?](#132-what-do-rabbitmq_default_user-and-rabbitmq_default_pass-do)
- [133: What does an AMQP connection URL look like?](#133-what-does-an-amqp-connection-url-look-like)
- [134: How do you connect to RabbitMQ with TLS?](#134-how-do-you-connect-to-rabbitmq-with-tls)
- [135: Why should you close channels and connections properly?](#135-why-should-you-close-channels-and-connections-properly)
- [136: What is single active consumer?](#136-what-is-single-active-consumer)
- [137: What are consumer priorities?](#137-what-are-consumer-priorities)
- [138: What were lazy queues?](#138-what-were-lazy-queues)
- [139: What is an exclusive consumer?](#139-what-is-an-exclusive-consumer)
- [140: Can one queue have several bindings?](#140-can-one-queue-have-several-bindings)
- [141: When a message goes to several queues, is it copied?](#141-when-a-message-goes-to-several-queues-is-it-copied)
- [142: Can one consumer read from several queues?](#142-can-one-consumer-read-from-several-queues)
- [143: What is the difference between a queue and a topic conceptually?](#143-what-is-the-difference-between-a-queue-and-a-topic-conceptually)
- [144: What is the competing consumers pattern?](#144-what-is-the-competing-consumers-pattern)
- [145: What is the difference between fire-and-forget and request/reply messaging?](#145-what-is-the-difference-between-fire-and-forget-and-requestreply-messaging)
- [146: How do you delay a message in RabbitMQ?](#146-how-do-you-delay-a-message-in-rabbitmq)
- [147: What is the rabbitmq_prometheus plugin?](#147-what-is-the-rabbitmq_prometheus-plugin)
- [148: What frameworks and tools use RabbitMQ under the hood?](#148-what-frameworks-and-tools-use-rabbitmq-under-the-hood)
- [149: What is the RabbitMQ Cluster Operator for Kubernetes?](#149-what-is-the-rabbitmq-cluster-operator-for-kubernetes)
- [150: What does the "unacked" count in the management UI mean?](#150-what-does-the-unacked-count-in-the-management-ui-mean)

### Moderate Questions (151-300)

- [151: How do you publish reliably from Node.js?](#151-how-do-you-publish-reliably-from-nodejs)
- [152: What does it mean when channel.publish returns false in amqplib?](#152-what-does-it-mean-when-channelpublish-returns-false-in-amqplib)
- [153: How do you handle reconnection with amqplib?](#153-how-do-you-handle-reconnection-with-amqplib)
- [154: Why does a channel close by itself sometimes?](#154-why-does-a-channel-close-by-itself-sometimes)
- [155: What are the common AMQP error codes?](#155-what-are-the-common-amqp-error-codes)
- [156: How do you choose a prefetch value?](#156-how-do-you-choose-a-prefetch-value)
- [157: What is the difference between per-consumer and global prefetch?](#157-what-is-the-difference-between-per-consumer-and-global-prefetch)
- [158: How do you ack many messages at once?](#158-how-do-you-ack-many-messages-at-once)
- [159: What retry strategies can you use with RabbitMQ?](#159-what-retry-strategies-can-you-use-with-rabbitmq)
- [160: How do you build delayed retries with TTL and dead letter exchanges?](#160-how-do-you-build-delayed-retries-with-ttl-and-dead-letter-exchanges)
- [161: How does the quorum queue delivery limit work?](#161-how-does-the-quorum-queue-delivery-limit-work)
- [162: What is a poison message and how do you deal with it?](#162-what-is-a-poison-message-and-how-do-you-deal-with-it)
- [163: What is the x-death header?](#163-what-is-the-x-death-header)
- [164: What does x-dead-letter-routing-key do?](#164-what-does-x-dead-letter-routing-key-do)
- [165: What is the x-delivery-count header?](#165-what-is-the-x-delivery-count-header)
- [166: What does it mean for a consumer to be idempotent?](#166-what-does-it-mean-for-a-consumer-to-be-idempotent)
- [167: How do you de-duplicate messages?](#167-how-do-you-de-duplicate-messages)
- [168: How do you design routing keys for a topic exchange?](#168-how-do-you-design-routing-keys-for-a-topic-exchange)
- [169: How should you name queues and exchanges?](#169-how-should-you-name-queues-and-exchanges)
- [170: Who should declare the topology, the producer or the consumer?](#170-who-should-declare-the-topology-the-producer-or-the-consumer)
- [171: What is a definitions file?](#171-what-is-a-definitions-file)
- [172: How do you export and import definitions?](#172-how-do-you-export-and-import-definitions)
- [173: How do you write a policy and what do pattern, apply-to and priority mean?](#173-how-do-you-write-a-policy-and-what-do-pattern-apply-to-and-priority-mean)
- [174: What are operator policies?](#174-what-are-operator-policies)
- [175: What are vhost limits?](#175-what-are-vhost-limits)
- [176: What are user limits?](#176-what-are-user-limits)
- [177: How do you make new queues quorum queues by default?](#177-how-do-you-make-new-queues-quorum-queues-by-default)
- [178: How do you declare a quorum queue and what are its options?](#178-how-do-you-declare-a-quorum-queue-and-what-are-its-options)
- [179: How do you use a stream from an AMQP 0-9-1 client?](#179-how-do-you-use-a-stream-from-an-amqp-0-9-1-client)
- [180: What offset options can you use when reading a stream?](#180-what-offset-options-can-you-use-when-reading-a-stream)
- [181: How do you control how long a stream keeps data?](#181-how-do-you-control-how-long-a-stream-keeps-data)
- [182: When should you choose a classic queue, a quorum queue or a stream?](#182-when-should-you-choose-a-classic-queue-a-quorum-queue-or-a-stream)
- [183: What doesn't a quorum queue support?](#183-what-doesnt-a-quorum-queue-support)
- [184: How many replicas should a quorum queue have?](#184-how-many-replicas-should-a-quorum-queue-have)
- [185: How do priorities work in quorum queues?](#185-how-do-priorities-work-in-quorum-queues)
- [186: What is a consumer timeout?](#186-what-is-a-consumer-timeout)
- [187: How do you handle jobs that take longer than the consumer timeout?](#187-how-do-you-handle-jobs-that-take-longer-than-the-consumer-timeout)
- [188: What is the difference between per-message TTL and per-queue TTL behavior?](#188-what-is-the-difference-between-per-message-ttl-and-per-queue-ttl-behavior)
- [189: Why is the delayed message exchange plugin not recommended anymore?](#189-why-is-the-delayed-message-exchange-plugin-not-recommended-anymore)
- [190: How do you do RPC with direct reply-to?](#190-how-do-you-do-rpc-with-direct-reply-to)
- [191: How do you handle timeouts in RPC over RabbitMQ?](#191-how-do-you-handle-timeouts-in-rpc-over-rabbitmq)
- [192: When should you use durable named queues vs temporary queues for pub/sub?](#192-when-should-you-use-durable-named-queues-vs-temporary-queues-for-pubsub)
- [193: How do you send one event to several microservices?](#193-how-do-you-send-one-event-to-several-microservices)
- [194: What is the difference between commands and events in messaging?](#194-what-is-the-difference-between-commands-and-events-in-messaging)
- [195: How do you version message schemas?](#195-how-do-you-version-message-schemas)
- [196: How do you add tracing to messages?](#196-how-do-you-add-tracing-to-messages)
- [197: How do you use RabbitMQ with NestJS?](#197-how-do-you-use-rabbitmq-with-nestjs)
- [198: How do you test code that uses RabbitMQ?](#198-how-do-you-test-code-that-uses-rabbitmq)
- [199: How do you seed queues and exchanges for local development?](#199-how-do-you-seed-queues-and-exchanges-for-local-development)
- [200: How do you set up health checks for RabbitMQ in Docker and Kubernetes?](#200-how-do-you-set-up-health-checks-for-rabbitmq-in-docker-and-kubernetes)
- [201: Which rabbitmq-diagnostics checks should you know?](#201-which-rabbitmq-diagnostics-checks-should-you-know)
- [202: What metrics should you monitor in RabbitMQ?](#202-what-metrics-should-you-monitor-in-rabbitmq)
- [203: What metrics endpoints does the Prometheus plugin expose?](#203-what-metrics-endpoints-does-the-prometheus-plugin-expose)
- [204: What can you see in the management UI?](#204-what-can-you-see-in-the-management-ui)
- [205: A message is published but never reaches the consumer. How do you debug it?](#205-a-message-is-published-but-never-reaches-the-consumer-how-do-you-debug-it)
- [206: A queue keeps growing. What do you check?](#206-a-queue-keeps-growing-what-do-you-check)
- [207: What is the firehose tracer?](#207-what-is-the-firehose-tracer)
- [208: What is the rabbitmq_tracing plugin?](#208-what-is-the-rabbitmq_tracing-plugin)
- [209: How do you look at messages in a queue without losing them?](#209-how-do-you-look-at-messages-in-a-queue-without-losing-them)
- [210: How do you move messages from one queue to another?](#210-how-do-you-move-messages-from-one-queue-to-another)
- [211: What is the difference between a static and a dynamic shovel?](#211-what-is-the-difference-between-a-static-and-a-dynamic-shovel)
- [212: What is the difference between federated exchanges and federated queues?](#212-what-is-the-difference-between-federated-exchanges-and-federated-queues)
- [213: When do you use Shovel and when Federation?](#213-when-do-you-use-shovel-and-when-federation)
- [214: Why should you give connections a name?](#214-why-should-you-give-connections-a-name)
- [215: What is connection churn and why is it bad?](#215-what-is-connection-churn-and-why-is-it-bad)
- [216: What is a channel leak?](#216-what-is-a-channel-leak)
- [217: How many connections and channels should an application open?](#217-how-many-connections-and-channels-should-an-application-open)
- [218: Why use separate connections for publishing and consuming?](#218-why-use-separate-connections-for-publishing-and-consuming)
- [219: What is flow control in RabbitMQ?](#219-what-is-flow-control-in-rabbitmq)
- [220: How can a client know it is blocked by the broker?](#220-how-can-a-client-know-it-is-blocked-by-the-broker)
- [221: How do you configure the memory watermark?](#221-how-do-you-configure-the-memory-watermark)
- [222: How should you set the disk free limit?](#222-how-should-you-set-the-disk-free-limit)
- [223: How do heartbeats interact with load balancers and firewalls?](#223-how-do-heartbeats-interact-with-load-balancers-and-firewalls)
- [224: How do you authenticate clients with TLS certificates?](#224-how-do-you-authenticate-clients-with-tls-certificates)
- [225: How do you use LDAP with RabbitMQ?](#225-how-do-you-use-ldap-with-rabbitmq)
- [226: How does OAuth 2.0 authentication work in RabbitMQ?](#226-how-does-oauth-20-authentication-work-in-rabbitmq)
- [227: How do you secure a fresh RabbitMQ installation?](#227-how-do-you-secure-a-fresh-rabbitmq-installation)
- [228: How do you write permission regexes for a least-privilege setup?](#228-how-do-you-write-permission-regexes-for-a-least-privilege-setup)
- [229: What are topic permissions?](#229-what-are-topic-permissions)
- [230: How should apps get their RabbitMQ credentials?](#230-how-should-apps-get-their-rabbitmq-credentials)
- [231: How do you form a cluster manually?](#231-how-do-you-form-a-cluster-manually)
- [232: What is peer discovery?](#232-what-is-peer-discovery)
- [233: Why do node names and hostnames matter?](#233-why-do-node-names-and-hostnames-matter)
- [234: Should you put a load balancer in front of a RabbitMQ cluster?](#234-should-you-put-a-load-balancer-in-front-of-a-rabbitmq-cluster)
- [235: How can a client connect to a cluster without a load balancer?](#235-how-can-a-client-connect-to-a-cluster-without-a-load-balancer)
- [236: What happens to clients when a cluster node goes down?](#236-what-happens-to-clients-when-a-cluster-node-goes-down)
- [237: What decides where a quorum queue's leader is placed?](#237-what-decides-where-a-quorum-queues-leader-is-placed)
- [238: How do you rebalance quorum queue leaders?](#238-how-do-you-rebalance-quorum-queue-leaders)
- [239: How do you add or remove replicas of a quorum queue?](#239-how-do-you-add-or-remove-replicas-of-a-quorum-queue)
- [240: How do you do a rolling upgrade of a cluster?](#240-how-do-you-do-a-rolling-upgrade-of-a-cluster)
- [241: What is a blue-green deployment for RabbitMQ?](#241-what-is-a-blue-green-deployment-for-rabbitmq)
- [242: How do you back up RabbitMQ?](#242-how-do-you-back-up-rabbitmq)
- [243: How do you define a production-ready RabbitmqCluster in Kubernetes?](#243-how-do-you-define-a-production-ready-rabbitmqcluster-in-kubernetes)
- [244: What is the Messaging Topology Operator?](#244-what-is-the-messaging-topology-operator)
- [245: How do you keep ordering per entity while still using several consumers?](#245-how-do-you-keep-ordering-per-entity-while-still-using-several-consumers)
- [246: What is the consistent hash exchange?](#246-what-is-the-consistent-hash-exchange)
- [247: What is the x-modulus-hash exchange?](#247-what-is-the-x-modulus-hash-exchange)
- [248: What is a super stream?](#248-what-is-a-super-stream)
- [249: How does single active consumer work with streams?](#249-how-does-single-active-consumer-work-with-streams)
- [250: What is stream filtering?](#250-what-is-stream-filtering)
- [251: How do stream consumers remember where they stopped?](#251-how-do-stream-consumers-remember-where-they-stopped)
- [252: Should you use the stream protocol or AMQP to work with streams?](#252-should-you-use-the-stream-protocol-or-amqp-to-work-with-streams)
- [253: Are some exchange types faster than others?](#253-are-some-exchange-types-faster-than-others)
- [254: How do you send large payloads like files through RabbitMQ?](#254-how-do-you-send-large-payloads-like-files-through-rabbitmq)
- [255: Should you compress message bodies?](#255-should-you-compress-message-bodies)
- [256: How do you publish many messages quickly and still be safe?](#256-how-do-you-publish-many-messages-quickly-and-still-be-safe)
- [257: How do you process messages concurrently in a Node.js consumer?](#257-how-do-you-process-messages-concurrently-in-a-nodejs-consumer)
- [258: How do you shut down a consumer gracefully?](#258-how-do-you-shut-down-a-consumer-gracefully)
- [259: How do you shut down a publisher without losing messages?](#259-how-do-you-shut-down-a-publisher-without-losing-messages)
- [260: What is the transactional outbox pattern and why is it used with RabbitMQ?](#260-what-is-the-transactional-outbox-pattern-and-why-is-it-used-with-rabbitmq)
- [261: Does RabbitMQ support transactions, and should you use them?](#261-does-rabbitmq-support-transactions-and-should-you-use-them)
- [262: What does a publisher confirm mean for a message that couldn't be routed?](#262-what-does-a-publisher-confirm-mean-for-a-message-that-couldnt-be-routed)
- [263: When does a broker send a nack for a published message?](#263-when-does-a-broker-send-a-nack-for-a-published-message)
- [264: How do you track publisher confirms asynchronously?](#264-how-do-you-track-publisher-confirms-asynchronously)
- [265: What happens to an exclusive queue if its node goes down?](#265-what-happens-to-an-exclusive-queue-if-its-node-goes-down)
- [266: What are the pitfalls of auto-delete queues?](#266-what-are-the-pitfalls-of-auto-delete-queues)
- [267: How do you send real-time notifications to users connected to different API instances?](#267-how-do-you-send-real-time-notifications-to-users-connected-to-different-api-instances)
- [268: How do MQTT QoS levels map to RabbitMQ?](#268-how-do-mqtt-qos-levels-map-to-rabbitmq)
- [269: What addresses do AMQP 1.0 clients use with RabbitMQ?](#269-what-addresses-do-amqp-10-clients-use-with-rabbitmq)
- [270: What are the new RabbitMQ AMQP 1.0 client libraries?](#270-what-are-the-new-rabbitmq-amqp-10-client-libraries)
- [271: What are the main differences between AMQP 0-9-1 and AMQP 1.0 in RabbitMQ?](#271-what-are-the-main-differences-between-amqp-0-9-1-and-amqp-10-in-rabbitmq)
- [272: Can an MQTT publisher send messages to an AMQP consumer?](#272-can-an-mqtt-publisher-send-messages-to-an-amqp-consumer)
- [273: How do you give a monitoring tool read-only access?](#273-how-do-you-give-a-monitoring-tool-read-only-access)
- [274: Can you publish messages through the HTTP API?](#274-can-you-publish-messages-through-the-http-api)
- [275: Which environment variables can configure RabbitMQ?](#275-which-environment-variables-can-configure-rabbitmq)
- [276: When do you need advanced.config?](#276-when-do-you-need-advancedconfig)
- [277: What are common mistakes when starting with RabbitMQ?](#277-what-are-common-mistakes-when-starting-with-rabbitmq)
- [278: What happens to consumers when their queue is deleted?](#278-what-happens-to-consumers-when-their-queue-is-deleted)
- [279: How do you check which deprecated features a cluster is using?](#279-how-do-you-check-which-deprecated-features-a-cluster-is-using)
- [280: What are transient non-exclusive queues and why were they deprecated?](#280-what-are-transient-non-exclusive-queues-and-why-were-they-deprecated)
- [281: How do you pass extra info to a consumer about why a message failed?](#281-how-do-you-pass-extra-info-to-a-consumer-about-why-a-message-failed)
- [282: What is the difference between nack with requeue and publishing a message again?](#282-what-is-the-difference-between-nack-with-requeue-and-publishing-a-message-again)
- [283: How do you make sure a consumer doesn't lose a message when it does a database write and then acks?](#283-how-do-you-make-sure-a-consumer-doesnt-lose-a-message-when-it-does-a-database-write-and-then-acks)
- [284: How does RabbitMQ decide which consumer gets a message when one is blocked by prefetch?](#284-how-does-rabbitmq-decide-which-consumer-gets-a-message-when-one-is-blocked-by-prefetch)
- [285: What are the risks of setting a very large prefetch?](#285-what-are-the-risks-of-setting-a-very-large-prefetch)
- [286: How do you read the "state" of a connection in the management UI?](#286-how-do-you-read-the-state-of-a-connection-in-the-management-ui)
- [287: What is the difference between rabbitmqctl, rabbitmq-queues, rabbitmq-streams and rabbitmq-upgrade?](#287-what-is-the-difference-between-rabbitmqctl-rabbitmq-queues-rabbitmq-streams-and-rabbitmq-upgrade)
- [288: What is maintenance mode?](#288-what-is-maintenance-mode)
- [289: How do you rate-limit processing to protect a slow downstream API?](#289-how-do-you-rate-limit-processing-to-protect-a-slow-downstream-api)
- [290: How do you handle a slow message blocking others behind it?](#290-how-do-you-handle-a-slow-message-blocking-others-behind-it)
- [291: What is the difference between the publish rate and the deliver rate in the UI?](#291-what-is-the-difference-between-the-publish-rate-and-the-deliver-rate-in-the-ui)
- [292: How do you safely change a queue setting that can't be changed?](#292-how-do-you-safely-change-a-queue-setting-that-cant-be-changed)
- [293: Should consumers or producers handle retries?](#293-should-consumers-or-producers-handle-retries)
- [294: How do you decide which errors to retry and which to send to the DLQ?](#294-how-do-you-decide-which-errors-to-retry-and-which-to-send-to-the-dlq)
- [295: How do you replay messages from a DLQ after fixing a bug?](#295-how-do-you-replay-messages-from-a-dlq-after-fixing-a-bug)
- [296: How do you handle message ordering when using retries?](#296-how-do-you-handle-message-ordering-when-using-retries)
- [297: What should you put in a message: the full data or just an ID?](#297-what-should-you-put-in-a-message-the-full-data-or-just-an-id)
- [298: How do you handle sensitive data in messages?](#298-how-do-you-handle-sensitive-data-in-messages)
- [299: How does RabbitMQ handle a client that sends data too fast for a quorum queue?](#299-how-does-rabbitmq-handle-a-client-that-sends-data-too-fast-for-a-quorum-queue)
- [300: How do you design topology for a typical microservices system?](#300-how-do-you-design-topology-for-a-typical-microservices-system)

### Advanced Questions (301-450)

- [301: How is RabbitMQ structured internally in terms of Erlang processes?](#301-how-is-rabbitmq-structured-internally-in-terms-of-erlang-processes)
- [302: What happens step by step when a message is published to a quorum queue?](#302-what-happens-step-by-step-when-a-message-is-published-to-a-quorum-queue)
- [303: What is credit-based flow control internally?](#303-what-is-credit-based-flow-control-internally)
- [304: How does classic queue v2 store messages?](#304-how-does-classic-queue-v2-store-messages)
- [305: How do quorum queues store data on disk?](#305-how-do-quorum-queues-store-data-on-disk)
- [306: Why can a quorum queue use much more disk than the size of its messages?](#306-why-can-a-quorum-queue-use-much-more-disk-than-the-size-of-its-messages)
- [307: What happens when a quorum queue loses its majority?](#307-what-happens-when-a-quorum-queue-loses-its-majority)
- [308: Why should quorum queues have an odd number of replicas?](#308-why-should-quorum-queues-have-an-odd-number-of-replicas)
- [309: What are non-voting quorum queue members?](#309-what-are-non-voting-quorum-queue-members)
- [310: How do you tune quorum queue throughput?](#310-how-do-you-tune-quorum-queue-throughput)
- [311: How do streams work internally?](#311-how-do-streams-work-internally)
- [312: Why are streams faster than queues for some workloads?](#312-why-are-streams-faster-than-queues-for-some-workloads)
- [313: What changed for clustering now that Khepri is the only metadata store?](#313-what-changed-for-clustering-now-that-khepri-is-the-only-metadata-store)
- [314: How does RabbitMQ 4.3+ behave during a network partition?](#314-how-does-rabbitmq-43-behave-during-a-network-partition)
- [315: What were the old partition handling strategies?](#315-what-were-the-old-partition-handling-strategies)
- [316: What happens to classic queues in a cluster when their node fails?](#316-what-happens-to-classic-queues-in-a-cluster-when-their-node-fails)
- [317: What does a full "no message loss" setup look like?](#317-what-does-a-full-no-message-loss-setup-look-like)
- [318: When exactly is a publisher confirm sent for classic vs quorum queues?](#318-when-exactly-is-a-publisher-confirm-sent-for-classic-vs-quorum-queues)
- [319: How do you think about throughput vs latency in RabbitMQ?](#319-how-do-you-think-about-throughput-vs-latency-in-rabbitmq)
- [320: How do you benchmark RabbitMQ?](#320-how-do-you-benchmark-rabbitmq)
- [321: How do you size a RabbitMQ cluster?](#321-how-do-you-size-a-rabbitmq-cluster)
- [322: How many queues can RabbitMQ handle?](#322-how-many-queues-can-rabbitmq-handle)
- [323: How do you tune RabbitMQ for many connections?](#323-how-do-you-tune-rabbitmq-for-many-connections)
- [324: How do you find out what's using memory on a node?](#324-how-do-you-find-out-whats-using-memory-on-a-node)
- [325: Why are long queues a problem?](#325-why-are-long-queues-a-problem)
- [326: What is head-of-line blocking and how does it show up in RabbitMQ?](#326-what-is-head-of-line-blocking-and-how-does-it-show-up-in-rabbitmq)
- [327: One queue is a bottleneck. How do you scale it?](#327-one-queue-is-a-bottleneck-how-do-you-scale-it)
- [328: How far can you scale consumers on one queue?](#328-how-far-can-you-scale-consumers-on-one-queue)
- [329: How do you autoscale consumers based on queue length?](#329-how-do-you-autoscale-consumers-based-on-queue-length)
- [330: Can RabbitMQ give exactly-once delivery?](#330-can-rabbitmq-give-exactly-once-delivery)
- [331: How do you implement an outbox publisher reliably?](#331-how-do-you-implement-an-outbox-publisher-reliably)
- [332: How do you implement an inbox (de-duplication) on the consumer side?](#332-how-do-you-implement-an-inbox-de-duplication-on-the-consumer-side)
- [333: How would you implement a saga with RabbitMQ?](#333-how-would-you-implement-a-saga-with-rabbitmq)
- [334: Can you use RabbitMQ streams for event sourcing?](#334-can-you-use-rabbitmq-streams-for-event-sourcing)
- [335: What are the costs of message priorities?](#335-what-are-the-costs-of-message-priorities)
- [336: How did consumer timeouts change in RabbitMQ 4.3?](#336-how-did-consumer-timeouts-change-in-rabbitmq-43)
- [337: How do delayed retries work in quorum queues since 4.3?](#337-how-do-delayed-retries-work-in-quorum-queues-since-43)
- [338: What is at-least-once dead lettering in quorum queues?](#338-what-is-at-least-once-dead-lettering-in-quorum-queues)
- [339: Can dead lettering create a loop?](#339-can-dead-lettering-create-a-loop)
- [340: How do you design multi-tenancy with RabbitMQ?](#340-how-do-you-design-multi-tenancy-with-rabbitmq)
- [341: How do you set up RabbitMQ across regions or data centers?](#341-how-do-you-set-up-rabbitmq-across-regions-or-data-centers)
- [342: Why not run a RabbitMQ cluster across availability zones?](#342-why-not-run-a-rabbitmq-cluster-across-availability-zones)
- [343: How do you migrate from classic mirrored queues to quorum queues?](#343-how-do-you-migrate-from-classic-mirrored-queues-to-quorum-queues)
- [344: What's the upgrade path from RabbitMQ 3.13 to 4.4?](#344-whats-the-upgrade-path-from-rabbitmq-313-to-44)
- [345: What are the requirements for upgrading to 4.3?](#345-what-are-the-requirements-for-upgrading-to-43)
- [346: Why shouldn't a mixed-version cluster run for long?](#346-why-shouldnt-a-mixed-version-cluster-run-for-long)
- [347: How do feature flags and deprecated features work over the RabbitMQ lifecycle?](#347-how-do-feature-flags-and-deprecated-features-work-over-the-rabbitmq-lifecycle)
- [348: What would be on your RabbitMQ security hardening checklist?](#348-what-would-be-on-your-rabbitmq-security-hardening-checklist)
- [349: How do you secure inter-node and CLI communication?](#349-how-do-you-secure-inter-node-and-cli-communication)
- [350: Why is the Erlang cookie so sensitive?](#350-why-is-the-erlang-cookie-so-sensitive)
- [351: Should the management UI be exposed publicly?](#351-should-the-management-ui-be-exposed-publicly)
- [352: How do OAuth 2 scopes map to RabbitMQ permissions?](#352-how-do-oauth-2-scopes-map-to-rabbitmq-permissions)
- [353: What changed for passive declarations in RabbitMQ 4.4?](#353-what-changed-for-passive-declarations-in-rabbitmq-44)
- [354: How do you protect a broker from misbehaving clients?](#354-how-do-you-protect-a-broker-from-misbehaving-clients)
- [355: What is the event exchange plugin?](#355-what-is-the-event-exchange-plugin)
- [356: What are message interceptors?](#356-what-are-message-interceptors)
- [357: What do you need to run RabbitMQ well on Kubernetes?](#357-what-do-you-need-to-run-rabbitmq-well-on-kubernetes)
- [358: What does rabbitmq-upgrade await_online_quorum_plus_one do?](#358-what-does-rabbitmq-upgrade-await_online_quorum_plus_one-do)
- [359: How did Kubernetes peer discovery change in RabbitMQ 4.1?](#359-how-did-kubernetes-peer-discovery-change-in-rabbitmq-41)
- [360: What can go wrong with RabbitMQ networking in Kubernetes?](#360-what-can-go-wrong-with-rabbitmq-networking-in-kubernetes)
- [361: Why do stream clients have trouble behind a load balancer?](#361-why-do-stream-clients-have-trouble-behind-a-load-balancer)
- [362: What issues come up with client automatic recovery and topology recovery?](#362-what-issues-come-up-with-client-automatic-recovery-and-topology-recovery)
- [363: How can publisher retries cause duplicates, and how do you limit them?](#363-how-can-publisher-retries-cause-duplicates-and-how-do-you-limit-them)
- [364: How do you make side effects like sending emails idempotent?](#364-how-do-you-make-side-effects-like-sending-emails-idempotent)
- [365: How do you keep strict order in a pipeline with retries and multiple steps?](#365-how-do-you-keep-strict-order-in-a-pipeline-with-retries-and-multiple-steps)
- [366: When do you need global ordering and how can you get it?](#366-when-do-you-need-global-ordering-and-how-can-you-get-it)
- [367: Design an order processing flow using RabbitMQ.](#367-design-an-order-processing-flow-using-rabbitmq)
- [368: Design an email notification service with RabbitMQ.](#368-design-an-email-notification-service-with-rabbitmq)
- [369: A queue has 10 million messages and growing. What do you do?](#369-a-queue-has-10-million-messages-and-growing-what-do-you-do)
- [370: Consumers keep crashing on the same message. What do you do?](#370-consumers-keep-crashing-on-the-same-message-what-do-you-do)
- [371: A memory alarm fires in production. What do you do?](#371-a-memory-alarm-fires-in-production-what-do-you-do)
- [372: A disk alarm fires. What do you do?](#372-a-disk-alarm-fires-what-do-you-do)
- [373: The number of connections spikes and the broker gets slow. What do you check?](#373-the-number-of-connections-spikes-and-the-broker-gets-slow-what-do-you-check)
- [374: Messages were lost after a broker restart. What went wrong?](#374-messages-were-lost-after-a-broker-restart-what-went-wrong)
- [375: Consumers process some messages twice. How do you investigate and fix it?](#375-consumers-process-some-messages-twice-how-do-you-investigate-and-fix-it)
- [376: One slow consumer is affecting other workloads on the same broker. What can you do?](#376-one-slow-consumer-is-affecting-other-workloads-on-the-same-broker-what-can-you-do)
- [377: One node in a 3-node cluster goes down. What happens and what do you do?](#377-one-node-in-a-3-node-cluster-goes-down-what-happens-and-what-do-you-do)
- [378: Two nodes of a 3-node cluster are down. What happens?](#378-two-nodes-of-a-3-node-cluster-are-down-what-happens)
- [379: You need to push events to thousands of individual users. Should you create a queue per user?](#379-you-need-to-push-events-to-thousands-of-individual-users-should-you-create-a-queue-per-user)
- [380: How would you design RabbitMQ for a multi-tenant SaaS with very uneven tenants?](#380-how-would-you-design-rabbitmq-for-a-multi-tenant-saas-with-very-uneven-tenants)
- [381: A new service needs all events from the past week. How do you support that?](#381-a-new-service-needs-all-events-from-the-past-week-how-do-you-support-that)
- [382: How would you migrate from a Redis-based job queue (like BullMQ) to RabbitMQ?](#382-how-would-you-migrate-from-a-redis-based-job-queue-like-bullmq-to-rabbitmq)
- [383: Compare RabbitMQ and Kafka in depth.](#383-compare-rabbitmq-and-kafka-in-depth)
- [384: How do RabbitMQ streams compare to Kafka?](#384-how-do-rabbitmq-streams-compare-to-kafka)
- [385: How does RabbitMQ compare to Amazon SQS and SNS?](#385-how-does-rabbitmq-compare-to-amazon-sqs-and-sns)
- [386: How does RabbitMQ compare to NATS?](#386-how-does-rabbitmq-compare-to-nats)
- [387: What are the trade-offs of managed RabbitMQ (Amazon MQ, CloudAMQP) vs self-hosted?](#387-what-are-the-trade-offs-of-managed-rabbitmq-amazon-mq-cloudamqp-vs-self-hosted)
- [388: How do SQL filter expressions on streams work?](#388-how-do-sql-filter-expressions-on-streams-work)
- [389: How do super stream partitions and consumer groups keep ordering?](#389-how-do-super-stream-partitions-and-consumer-groups-keep-ordering)
- [390: How does publisher de-duplication work in streams?](#390-how-does-publisher-de-duplication-work-in-streams)
- [391: How is stream retention evaluated?](#391-how-is-stream-retention-evaluated)
- [392: How does flow control work for stream consumers?](#392-how-does-flow-control-work-for-stream-consumers)
- [393: When would you use a stream instead of fan-out to many quorum queues?](#393-when-would-you-use-a-stream-instead-of-fan-out-to-many-quorum-queues)
- [394: What are the trade-offs between the consistent hash exchange and x-modulus-hash?](#394-what-are-the-trade-offs-between-the-consistent-hash-exchange-and-x-modulus-hash)
- [395: What are local shovels?](#395-what-are-local-shovels)
- [396: How do you configure federation and avoid loops?](#396-how-do-you-configure-federation-and-avoid-loops)
- [397: What ack modes does Shovel support?](#397-what-ack-modes-does-shovel-support)
- [398: How does direct reply-to work internally and what are its limits?](#398-how-does-direct-reply-to-work-internally-and-what-are-its-limits)
- [399: Why can RPC over RabbitMQ be hard to scale?](#399-why-can-rpc-over-rabbitmq-be-hard-to-scale)
- [400: How does RabbitMQ perform with very large fan-out?](#400-how-does-rabbitmq-perform-with-very-large-fan-out)
- [401: What is cluster_exchange_limit?](#401-what-is-cluster_exchange_limit)
- [402: How does topic exchange routing work internally?](#402-how-does-topic-exchange-routing-work-internally)
- [403: Does message size affect how RabbitMQ stores and handles messages?](#403-does-message-size-affect-how-rabbitmq-stores-and-handles-messages)
- [404: How do you maximize publisher throughput?](#404-how-do-you-maximize-publisher-throughput)
- [405: How do you maximize consumer throughput?](#405-how-do-you-maximize-consumer-throughput)
- [406: How does prefetch work differently with quorum queues?](#406-how-does-prefetch-work-differently-with-quorum-queues)
- [407: What is a redelivery storm and how do you avoid it?](#407-what-is-a-redelivery-storm-and-how-do-you-avoid-it)
- [408: Why is nack with requeue=true dangerous at scale?](#408-why-is-nack-with-requeuetrue-dangerous-at-scale)
- [409: How do unacked messages affect broker memory?](#409-how-do-unacked-messages-affect-broker-memory)
- [410: What was x-cancel-on-ha-failover?](#410-what-was-x-cancel-on-ha-failover)
- [411: What does tracing cost in production, and what are the alternatives?](#411-what-does-tracing-cost-in-production-and-what-are-the-alternatives)
- [412: How do you detect slow consumers using metrics?](#412-how-do-you-detect-slow-consumers-using-metrics)
- [413: What alerts would you set up for RabbitMQ?](#413-what-alerts-would-you-set-up-for-rabbitmq)
- [414: How do you plan disk capacity for quorum queues?](#414-how-do-you-plan-disk-capacity-for-quorum-queues)
- [415: What does busy_dist_port mean?](#415-what-does-busy_dist_port-mean)
- [416: What is net_ticktime?](#416-what-is-net_ticktime)
- [417: What is the difference between TCP keepalive and AMQP heartbeats?](#417-what-is-the-difference-between-tcp-keepalive-and-amqp-heartbeats)
- [418: Why is creating an exclusive queue per request a bad idea?](#418-why-is-creating-an-exclusive-queue-per-request-a-bad-idea)
- [419: How do you notice and fix an uneven distribution of queue leaders across nodes?](#419-how-do-you-notice-and-fix-an-uneven-distribution-of-queue-leaders-across-nodes)
- [420: What happens when you change a policy on existing queues?](#420-what-happens-when-you-change-a-policy-on-existing-queues)
- [421: How do you change the type of an existing queue?](#421-how-do-you-change-the-type-of-an-existing-queue)
- [422: How do you test RabbitMQ failure scenarios?](#422-how-do-you-test-rabbitmq-failure-scenarios)
- [423: How do you design exchanges for a large microservices system?](#423-how-do-you-design-exchanges-for-a-large-microservices-system)
- [424: How do you keep event consumers compatible when event schemas evolve?](#424-how-do-you-keep-event-consumers-compatible-when-event-schemas-evolve)
- [425: How do you document message-based APIs?](#425-how-do-you-document-message-based-apis)
- [426: How do you validate messages at the consumer?](#426-how-do-you-validate-messages-at-the-consumer)
- [427: How do you design end-to-end backpressure in a system using RabbitMQ?](#427-how-do-you-design-end-to-end-backpressure-in-a-system-using-rabbitmq)
- [428: How do you handle time-sensitive messages that become useless after a while?](#428-how-do-you-handle-time-sensitive-messages-that-become-useless-after-a-while)
- [429: Is a queue length limit enough protection against unbounded growth?](#429-is-a-queue-length-limit-enough-protection-against-unbounded-growth)
- [430: How do you build tooling around dead letter queues?](#430-how-do-you-build-tooling-around-dead-letter-queues)
- [431: How do you make work processing fair between tenants or customers?](#431-how-do-you-make-work-processing-fair-between-tenants-or-customers)
- [432: When would you not use quorum queues?](#432-when-would-you-not-use-quorum-queues)
- [433: What are some hard production issues teams commonly hit with RabbitMQ?](#433-what-are-some-hard-production-issues-teams-commonly-hit-with-rabbitmq)
- [434: How do you load test an application's messaging, not just the broker?](#434-how-do-you-load-test-an-applications-messaging-not-just-the-broker)
- [435: What does "advertised host" mean for streams and why is it needed?](#435-what-does-advertised-host-mean-for-streams-and-why-is-it-needed)
- [436: How do you handle schema changes in topology without downtime?](#436-how-do-you-handle-schema-changes-in-topology-without-downtime)
- [437: What does the RabbitMQ Terraform provider or Topology Operator bring compared to app-declared topology?](#437-what-does-the-rabbitmq-terraform-provider-or-topology-operator-bring-compared-to-app-declared-topology)
- [438: How do you decide between choreography and orchestration with RabbitMQ?](#438-how-do-you-decide-between-choreography-and-orchestration-with-rabbitmq)
- [439: How would you explain prefetch, acks and redelivery together in a failure scenario?](#439-how-would-you-explain-prefetch-acks-and-redelivery-together-in-a-failure-scenario)
- [440: How does RabbitMQ use Raft in more than one place?](#440-how-does-rabbitmq-use-raft-in-more-than-one-place)
- [441: What's new in RabbitMQ 4.4 that's worth knowing?](#441-whats-new-in-rabbitmq-44-thats-worth-knowing)
- [442: What changed in RabbitMQ 4.0 that interviewers often ask about?](#442-what-changed-in-rabbitmq-40-that-interviewers-often-ask-about)
- [443: How would you explain RabbitMQ's architecture in a system design interview?](#443-how-would-you-explain-rabbitmqs-architecture-in-a-system-design-interview)
- [444: How do you secure AMQP connections that come from outside your network, like IoT devices?](#444-how-do-you-secure-amqp-connections-that-come-from-outside-your-network-like-iot-devices)
- [445: How do you think about message durability costs when designing a system?](#445-how-do-you-think-about-message-durability-costs-when-designing-a-system)
- [446: What is the difference between at-most-once and at-least-once dead lettering, and when does it matter?](#446-what-is-the-difference-between-at-most-once-and-at-least-once-dead-lettering-and-when-does-it-matter)
- [447: What are Unix domain socket listeners in RabbitMQ 4.4 good for?](#447-what-are-unix-domain-socket-listeners-in-rabbitmq-44-good-for)
- [448: Why does RabbitMQ refuse to start with a missing auth backend plugin since 4.2?](#448-why-does-rabbitmq-refuse-to-start-with-a-missing-auth-backend-plugin-since-42)
- [449: How do you decide how many queues and consumers a new feature needs?](#449-how-do-you-decide-how-many-queues-and-consumers-a-new-feature-needs)
- [450: What would you check before going live with a RabbitMQ-based system?](#450-what-would-you-check-before-going-live-with-a-rabbitmq-based-system)

---

# Easy Questions (1-150)

## 1: What is RabbitMQ?

RabbitMQ is an open source message broker. Applications send messages to it, and it stores them and passes them on to other applications that read them. This way the sender and the receiver don't need to talk to each other directly, and they don't need to be online at the same time.

It is written in Erlang, it is maintained by the RabbitMQ team at Broadcom, and it supports several protocols: AMQP 0-9-1, AMQP 1.0, MQTT, STOMP and its own stream protocol.

## 2: What is a message broker?

A message broker is a server that sits between services and moves messages from one to the other. A producer sends a message to the broker, the broker keeps it (in memory or on disk), and then delivers it to one or more consumers.

The broker takes care of things like routing, buffering when consumers are slow, retrying failed deliveries and keeping messages safe if a service crashes. RabbitMQ, Apache Kafka, ActiveMQ and Amazon SQS are common examples.

## 3: Why would you use a message queue instead of calling a service directly?

A direct HTTP call means the caller has to wait for the answer, and if the other service is down or slow, the caller fails too. A queue removes that link.

Main reasons to use one:

- **Decoupling:** the producer doesn't need to know who reads the message or how many readers there are.
- **Async work:** slow jobs (sending emails, resizing images, generating PDFs) run in the background, and the user gets a fast response.
- **Load leveling:** if traffic spikes, messages wait in the queue and consumers process them at their own pace.
- **Reliability:** if a consumer crashes, the message stays in the queue and gets delivered again later.
- **Scaling:** you can add more consumers to process messages faster.

## 4: Which protocols does RabbitMQ support?

- **AMQP 0-9-1:** the original and still the most used protocol. Most client libraries (amqplib for Node.js, Pika for Python, the Java client) use it.
- **AMQP 1.0:** supported natively in the core since RabbitMQ 4.0, on the same port as AMQP 0-9-1.
- **MQTT 3.1, 3.1.1 and 5.0:** through the MQTT plugin, mostly used for IoT devices.
- **STOMP:** a simple text protocol, through the STOMP plugin.
- **RabbitMQ Stream protocol:** a binary protocol made for streams.
- **MQTT and STOMP over WebSockets:** through the Web MQTT and Web STOMP plugins.

## 5: What is AMQP 0-9-1?

AMQP (Advanced Message Queuing Protocol) 0-9-1 is a binary protocol for messaging. It defines both the wire format and the model: exchanges, queues and bindings.

In this model, producers never send messages straight to a queue. They publish to an exchange, and the exchange uses bindings and the routing key to decide which queues get a copy. Clients can also declare exchanges, queues and bindings themselves, so the application can set up the topology it needs.

## 6: Why is RabbitMQ written in Erlang and why does it matter?

Erlang was built for telecom systems that must keep running for years without stopping. It gives RabbitMQ lightweight processes (one per queue, channel and connection), built-in clustering between nodes, and supervision trees that restart crashed parts without taking down the whole server.

For you as a user it mostly matters when installing and operating RabbitMQ: you need a supported Erlang/OTP version, nodes in a cluster authenticate using the Erlang cookie, and some tools and errors use Erlang terms. If you use the official Docker image or packages, the right Erlang version is already included.

## 7: What is a producer?

A producer (or publisher) is the application that sends messages. In AMQP 0-9-1 it publishes to an exchange with a routing key, and it doesn't know which queues will end up with the message.

```js
channel.publish("orders", "order.created", Buffer.from(JSON.stringify(order)));
```

## 8: What is a consumer?

A consumer is the application that receives and processes messages from a queue. It subscribes to a queue, RabbitMQ pushes messages to it, and the consumer acknowledges each message when it is done with it.

```js
await channel.consume("emails", async (msg) => {
  await sendEmail(JSON.parse(msg.content.toString()));
  channel.ack(msg);
});
```

## 9: What is a queue in RabbitMQ?

A queue is an ordered buffer that holds messages until a consumer takes them. Messages are stored in FIFO order (first in, first out). A queue has a name and properties like durability, plus optional arguments for TTL, length limits, dead lettering and so on.

Consumers always read from queues, never from exchanges. Several consumers can read from the same queue, and each message goes to only one of them.

## 10: What is an exchange?

An exchange receives messages from producers and routes them to queues. It doesn't store messages. If no queue matches, the message is dropped (or returned to the publisher if it was published with the `mandatory` flag).

How the exchange picks the queues depends on its type (direct, fanout, topic or headers) and on the bindings that connect it to queues.

## 11: What is a binding?

A binding is a rule that connects an exchange to a queue (or to another exchange). It says "messages from this exchange that match this condition should go to this queue". For direct and topic exchanges the condition is a binding key; for headers exchanges it is a set of header values.

```js
await channel.bindQueue("eu-orders", "orders", "order.eu.*");
```

## 12: What is a routing key?

A routing key is a string the producer attaches to each message when publishing. The exchange compares it to the binding keys to decide where the message goes. For example, a message with routing key `order.created` sent to a topic exchange will reach every queue bound with `order.created`, `order.*` or `order.#`.

Fanout exchanges ignore the routing key, and headers exchanges use message headers instead.

## 13: What is the difference between a routing key and a binding key?

The routing key belongs to the message, and the producer sets it when publishing. The binding key belongs to the binding, and it is set when a queue is bound to an exchange.

The exchange compares the two. In a direct exchange they must be equal. In a topic exchange the binding key can contain wildcards (`*` and `#`) that match parts of the routing key. People often say "routing key" for both, which is fine as long as it's clear which side you mean.

## 14: What exchange types does RabbitMQ have?

There are four built-in types:

- **direct:** routes to queues whose binding key equals the routing key.
- **fanout:** routes to every bound queue and ignores the routing key.
- **topic:** routes by matching the routing key against binding patterns with wildcards.
- **headers:** routes by message header values instead of the routing key.

Plugins and newer versions add more, like the consistent hash exchange (plugin) and the `x-modulus-hash` exchange, which moved into the core in RabbitMQ 4.3.

## 15: How does a direct exchange work?

A direct exchange sends a message to every queue whose binding key is exactly the same as the message's routing key. If two queues are bound with the same key, both get a copy.

It's a good fit when you route by a known value, for example log level:

```js
await channel.assertExchange("logs", "direct", { durable: true });
await channel.bindQueue("error-logs", "logs", "error");
channel.publish("logs", "error", Buffer.from("Disk is full"));
```

## 16: How does a fanout exchange work?

A fanout exchange copies every message to all queues bound to it. The routing key is ignored. It's the simplest way to do publish/subscribe: each subscriber has its own queue bound to the exchange, and they all get every message.

Typical uses are broadcasting cache invalidation events, sending notifications to several services, or updating several read models.

## 17: How does a topic exchange work?

A topic exchange routes by pattern matching. Routing keys are words separated by dots, like `order.eu.created`. Binding keys can use wildcards:

- `*` matches exactly one word
- `#` matches zero or more words

So a queue bound with `order.*.created` gets `order.eu.created` and `order.us.created`, and a queue bound with `order.#` gets every order event. Topic exchanges are the most common choice for event-driven systems because consumers can choose exactly what they want.

## 18: What is the difference between * and # in topic bindings?

`*` replaces exactly one word, and `#` replaces zero or more words.

| Binding key | `order.created` | `order.eu.created` | `order` |
| ----------- | --------------- | ------------------ | ------- |
| `order.*`   | yes             | no                 | no      |
| `order.#`   | yes             | yes                | yes     |
| `*.created` | yes             | no                 | no      |
| `#`         | yes             | yes                | yes     |

A binding of just `#` makes a topic exchange act like a fanout, and a binding with no wildcards makes it act like a direct exchange.

## 19: How does a headers exchange work?

A headers exchange ignores the routing key and looks at the message headers. The binding has arguments with the header values to match, plus an `x-match` argument:

- `x-match: all` (default): all listed headers must match
- `x-match: any`: at least one must match
- `all-with-x` and `any-with-x`: same, but also compare headers starting with `x-`

```js
await channel.bindQueue("pdf-reports", "reports", "", {
  "x-match": "all",
  format: "pdf",
  type: "report",
});
```

It's used when routing depends on several attributes that don't fit well in one dotted string.

## 20: What is the default exchange?

The default exchange is a direct exchange with an empty name (`""`) that every vhost has. Every queue is automatically bound to it with a binding key equal to the queue name.

That's why you can "send to a queue directly":

```js
channel.sendToQueue("tasks", Buffer.from("hello"));
// same as
channel.publish("", "tasks", Buffer.from("hello"));
```

You can't bind or unbind queues to the default exchange or delete it.

## 21: What are the amq.* exchanges?

Each vhost comes with a few predefined exchanges: `amq.direct`, `amq.fanout`, `amq.topic`, `amq.headers` and `amq.match` (also a headers exchange). Names starting with `amq.` are reserved, so you can't create your own exchange with that prefix.

`amq.topic` is used by the MQTT and STOMP plugins by default. In applications it's usually better to declare your own exchanges with clear names like `orders` or `billing.events`.

## 22: What is a virtual host (vhost)?

A vhost is a logical group inside one RabbitMQ server. Each vhost has its own exchanges, queues, bindings, policies and user permissions, so two vhosts are fully separated even though they run on the same nodes.

People use vhosts to separate environments (dev and staging on one server), teams or tenants. The default vhost is `/`. A client picks the vhost when it connects, for example `amqp://user:pass@host:5672/billing`.

## 23: What is a connection in RabbitMQ?

A connection is a long-lived TCP connection between a client and a RabbitMQ node. It's authenticated with a username and password (or a certificate or token) and is tied to one vhost.

Opening a connection is expensive (TCP handshake, maybe TLS, protocol handshake and authentication), so applications should open one at startup and keep it open, instead of connecting for every message.

## 24: What is a channel?

A channel is a lightweight virtual connection inside a real TCP connection. Almost all work happens on channels: declaring queues, publishing, consuming and acknowledging.

One connection can have many channels. Each channel has its own ID, and if something goes wrong on a channel (for example you declare a queue with conflicting arguments), RabbitMQ closes only that channel, not the whole connection.

```js
const connection = await amqp.connect("amqp://localhost");
const channel = await connection.createChannel();
```

## 25: Why does RabbitMQ use channels instead of many TCP connections?

TCP connections cost a lot: each one needs a socket, memory on both sides, handshakes and sometimes TLS. A service with 50 workers opening 50 connections would waste resources on both the client and the broker.

Channels let the client multiplex many independent "conversations" over one connection. A common setup is one connection per process and one channel per thread or per worker. Channels aren't free either, so you still shouldn't open thousands of them or open and close one per message.

## 26: What does a RabbitMQ message consist of?

A message has three parts:

- **Body (payload):** raw bytes. RabbitMQ doesn't look inside it. Usually it's JSON, but it can be anything.
- **Properties:** standard fields defined by the protocol, like `content_type`, `delivery_mode`, `message_id`, `correlation_id`, `reply_to`, `expiration`, `priority` and `timestamp`.
- **Headers:** a table of custom key-value pairs, for things like trace IDs or a schema version.

The routing key and exchange name are delivery information, not part of the stored message properties.

## 27: What are the most common message properties?

- `content_type`: format of the body, like `application/json`
- `content_encoding`: like `gzip`
- `delivery_mode`: 2 for persistent, 1 for transient
- `message_id`: an ID set by the app, useful for de-duplication
- `correlation_id`: links a reply to its request
- `reply_to`: name of the queue where the reply should go
- `expiration`: per-message TTL in milliseconds, as a string
- `priority`: used by priority queues
- `timestamp`: when the message was created
- `type` and `app_id`: free text describing the message and the sender
- `headers`: custom fields

In amqplib they're passed as options in camelCase, like `contentType`, `messageId`, `persistent`.

## 28: What is a message acknowledgment?

An acknowledgment (ack) is a signal the consumer sends to RabbitMQ to say "I processed this message, you can delete it". Until RabbitMQ gets the ack, the message stays in the queue as "unacked".

If the consumer's channel or connection closes before it acks, RabbitMQ puts the message back in the queue and delivers it again, possibly to another consumer. This is what makes it safe for a worker to crash in the middle of a job.

## 29: What is the difference between automatic and manual acknowledgment?

With automatic ack (`noAck: true` in amqplib), RabbitMQ considers a message delivered as soon as it sends it. If the consumer crashes while processing, the message is lost. It's faster, but only fine for data you can afford to lose.

With manual ack, the consumer calls `ack` after the work is done. If it crashes before that, the message gets redelivered. This is what you want for anything important.

```js
await channel.consume(
  "tasks",
  async (msg) => {
    await doWork(msg);
    channel.ack(msg);
  },
  { noAck: false },
);
```

## 30: What happens if a consumer dies without acknowledging a message?

When the consumer's channel or connection closes, RabbitMQ takes all messages that were delivered to it but not acked and puts them back in the queue. They get delivered again, usually to another consumer, with the `redelivered` flag set to `true`.

This means a message can be processed twice: once by the consumer that crashed (if it got halfway, for example sent the email but didn't ack), and again by the next consumer. That's why consumers should be idempotent.

## 31: What is the difference between basic.nack and basic.reject?

Both tell RabbitMQ that the consumer could not process a message.

- `basic.reject` is in the AMQP 0-9-1 spec and works on one message at a time.
- `basic.nack` is a RabbitMQ extension that can also reject many messages at once with the `multiple` flag.

Both take a `requeue` flag. With `requeue: true` the message goes back to the queue. With `requeue: false` it's dropped, or dead-lettered if the queue has a dead letter exchange.

```js
channel.nack(msg, false, false); // allUpTo = false, requeue = false
channel.reject(msg, true); // requeue = true
```

## 32: What does requeue mean?

Requeue means putting a rejected message back into the queue so it can be delivered again. In classic queues it goes back to its original position if possible, so it's usually redelivered quickly.

Be careful with requeueing messages that always fail (for example, bad JSON). They get redelivered again and again in a tight loop and burn CPU. Quorum queues protect against this with a delivery limit, but the better fix is to reject with `requeue: false` and send the message to a dead letter queue.

## 33: What is the redelivered flag?

`redelivered` is a flag on a delivery that tells the consumer this message was delivered before, but wasn't acked (the consumer crashed, the channel closed, or it was requeued).

It's a hint, not a guarantee that the message was already processed. The previous consumer might have done nothing with it. You can use it to be extra careful, for example to check a de-duplication table only for redelivered messages.

```js
if (msg.fields.redelivered) {
  console.log("Seen before, checking if already processed");
}
```

## 34: What is a durable queue?

A durable queue survives a broker restart. Its definition is stored on disk, so after RabbitMQ restarts, the queue is still there. A non-durable (transient) queue is deleted when the node restarts.

Durability is about the queue itself, not its messages. Messages survive a restart only if they were also published as persistent and the queue is durable. Quorum queues and streams are always durable.

```js
await channel.assertQueue("orders", { durable: true });
```

## 35: What is a persistent message?

A persistent message is one published with `delivery_mode = 2`. RabbitMQ writes it to disk, so it survives a broker restart if it's in a durable queue.

```js
channel.sendToQueue("orders", Buffer.from(body), { persistent: true });
```

Transient messages (`delivery_mode = 1`) may be kept only in memory and are lost on restart. In quorum queues and streams all messages are stored on disk anyway, no matter what `delivery_mode` says.

## 36: If a queue is durable, are its messages safe after a restart?

Not automatically. You need both:

1. A durable queue (so the queue exists after restart)
2. Persistent messages (so the messages are stored on disk)

Even then, a message is only really safe once RabbitMQ confirms it. Without publisher confirms, a message can be lost if the broker crashes right after receiving it and before writing it to disk. For important data, use durable queues (preferably quorum queues), persistent messages and publisher confirms.

## 37: What is an exclusive queue?

An exclusive queue can be used only by the connection that declared it, and it's deleted when that connection closes. Other connections can't consume from it or even declare it.

It's used for temporary, private queues, like a reply queue for RPC or a per-instance queue that receives broadcast events. Only classic queues can be exclusive; quorum queues and streams can't.

```js
const { queue } = await channel.assertQueue("", { exclusive: true });
```

## 38: What is an auto-delete queue?

An auto-delete queue is deleted automatically when its last consumer unsubscribes. If a queue never had any consumer, it isn't deleted by this rule.

Don't confuse it with exclusive queues. An exclusive queue is tied to its connection; an auto-delete queue is tied to its consumers and can be shared by several connections. For "delete if unused for some time", use queue TTL (`x-expires`) instead.

## 39: What is a server-named queue?

If you declare a queue with an empty name, RabbitMQ creates one with a random unique name like `amq.gen-JzTY20BRgKO-HjmUJj0wLg` and returns it. These are usually exclusive and used for temporary queues.

```js
const { queue } = await channel.assertQueue("", { exclusive: true });
await channel.bindQueue(queue, "notifications", "");
```

## 40: What queue types does RabbitMQ have?

RabbitMQ 4.x has three queue types:

- **Classic queues:** the original type. A queue lives on one node and isn't replicated. Good for temporary or non-critical data.
- **Quorum queues:** replicated across several nodes with the Raft algorithm. The recommended type for data that must not be lost.
- **Streams:** append-only logs where messages aren't deleted when consumed, so many consumers can read and re-read them.

You pick the type with the `x-queue-type` argument when declaring the queue, or set a default queue type for the vhost.

## 41: What is a classic queue?

A classic queue is the original RabbitMQ queue type. It's stored on a single node, so if that node goes down, the queue is unavailable until the node comes back (and transient messages are lost).

Since RabbitMQ 4.0, classic queues can no longer be mirrored. They are still a good choice for temporary queues, exclusive queues, RPC reply queues and cases where you care more about speed than safety. Since 4.3 only the version 2 storage format (CQv2) exists.

## 42: What is a quorum queue?

A quorum queue is a durable, replicated queue based on the Raft consensus algorithm. Each queue has a leader and followers on different nodes, usually three replicas in total. A message is confirmed only after a majority of replicas have written it to disk.

If the node with the leader fails, one of the followers becomes the new leader and the queue keeps working with no message loss. Quorum queues are the recommended choice for important data and replaced classic mirrored queues.

```js
await channel.assertQueue("payments", {
  durable: true,
  arguments: { "x-queue-type": "quorum" },
});
```

## 43: What is a RabbitMQ stream?

A stream is a persistent, replicated, append-only log. Unlike a queue, reading a message doesn't remove it. Each consumer chooses where to start reading (first message, last message, a specific offset or a timestamp), and old data is removed only by retention rules (size or age).

Streams are good for large fan-out (many consumers reading the same data), replaying history and very high throughput. You can use them over AMQP 0-9-1, AMQP 1.0 or the dedicated stream protocol, which is the fastest option.

## 44: How do you run RabbitMQ locally?

The easiest way is the official Docker image with the management plugin:

```bash
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  rabbitmq:4-management
```

Then the AMQP port is `localhost:5672` and the management UI is at `http://localhost:15672` (user `guest`, password `guest`). You can also install it with packages on Linux, Homebrew on macOS or the Windows installer, but then you also need a matching Erlang version.

## 45: What are the default ports used by RabbitMQ?

- `5672`: AMQP 0-9-1 and AMQP 1.0
- `5671`: AMQP over TLS
- `15672`: management UI and HTTP API
- `5552`: stream protocol (`5551` with TLS)
- `25672`: communication between cluster nodes and CLI tools
- `4369`: epmd, the Erlang port mapper used for node discovery
- `15692`: Prometheus metrics
- `1883` / `8883`: MQTT / MQTT over TLS
- `61613` / `61614`: STOMP / STOMP over TLS
- `15675` / `15674`: Web MQTT / Web STOMP

You only need to open the ports for the features you use.

## 46: What is the management plugin?

The management plugin (`rabbitmq_management`) adds a web UI and an HTTP API. In the UI you can see connections, channels, exchanges, queues, message rates and node health, and you can create users, vhosts, policies, queues and bindings, or publish and read test messages.

```bash
rabbitmq-plugins enable rabbitmq_management
```

The `rabbitmq:4-management` Docker image has it enabled already. The UI listens on port 15672.

## 47: What is the guest user?

`guest` (password `guest`) is the default user created on a fresh install. It's an administrator in the `/` vhost, but by default it can only connect from localhost.

That's why a client on another machine gets "access refused" with guest. The right fix isn't to allow remote guest access, but to create your own user with a strong password and delete guest in anything other than local development.

## 48: How do you create a user and give them access to a vhost?

```bash
rabbitmqctl add_user orders_app 'S3cret-Passw0rd'
rabbitmqctl add_vhost shop
rabbitmqctl set_permissions -p shop orders_app '.*' '.*' '.*'
rabbitmqctl set_user_tags orders_app monitoring
```

`set_permissions` takes three regular expressions: configure, write and read. You can do the same in the management UI under Admin, or with the HTTP API.

## 49: What do configure, write and read permissions mean?

Permissions are set per user per vhost, as three regular expressions matched against resource names:

- **configure:** create and delete exchanges and queues, change their settings
- **write:** publish to an exchange, bind a queue to an exchange (write on the queue side)
- **read:** consume from a queue, get messages, purge it, bind (read on the exchange side)

For example, a service that only publishes to `orders` could have configure `^$`, write `^orders$`, read `^$`. Use `^$` to give no access and `.*` to give full access.

## 50: What are user tags?

Tags control what a user can do in the management UI and HTTP API. They don't affect AMQP permissions.

- `administrator`: full access to everything
- `monitoring`: can see all connections, channels and node data
- `policymaker`: can manage policies and parameters in vhosts they have access to
- `management`: can log in and see their own vhosts
- no tag: can't use the management UI at all

```bash
rabbitmqctl set_user_tags ops_user monitoring
```

## 51: What is rabbitmqctl?

`rabbitmqctl` is the main command line tool for managing a RabbitMQ node: users, permissions, vhosts, policies, cluster membership and listing objects.

```bash
rabbitmqctl list_queues name messages consumers
rabbitmqctl list_connections name user state
rabbitmqctl list_users
rabbitmqctl cluster_status
```

It talks to the node over the Erlang distribution, so it needs the same Erlang cookie as the node.

## 52: What is rabbitmq-plugins?

`rabbitmq-plugins` enables, disables and lists plugins.

```bash
rabbitmq-plugins list
rabbitmq-plugins enable rabbitmq_management rabbitmq_prometheus
rabbitmq-plugins disable rabbitmq_stomp
```

Enabled plugins are saved in the `enabled_plugins` file, so they stay enabled after a restart. Many plugins (management, shovel, federation, MQTT, STOMP, Prometheus) come bundled with RabbitMQ.

## 53: What is rabbitmq-diagnostics?

`rabbitmq-diagnostics` is a tool for checking node health and getting information for troubleshooting.

```bash
rabbitmq-diagnostics status
rabbitmq-diagnostics ping
rabbitmq-diagnostics check_running
rabbitmq-diagnostics check_local_alarms
rabbitmq-diagnostics memory_breakdown
rabbitmq-diagnostics listeners
```

Its health check commands are often used in Docker and Kubernetes probes.

## 54: What is rabbitmqadmin?

`rabbitmqadmin` is a CLI that uses the HTTP API of the management plugin, so it can run from any machine that can reach port 15672, without the Erlang cookie. Since RabbitMQ 4.1 there's a new version (v2), shipped as a standalone binary with TOML config files.

```bash
rabbitmqadmin --host rabbit.internal --username admin --password secret list queues
rabbitmqadmin declare queue --name orders --type quorum
```

It's handy for scripts and CI pipelines.

## 55: How do you enable a plugin?

```bash
rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management
```

The change applies to the running node right away. In Docker you can mount an `enabled_plugins` file:

```erlang
[rabbitmq_management,rabbitmq_prometheus,rabbitmq_shovel].
```

Community plugins (not shipped with RabbitMQ) have to be copied into the plugins directory first, and their version must match your RabbitMQ version.

## 56: What is rabbitmq.conf?

`rabbitmq.conf` is the main config file. It uses a simple `key = value` format.

```ini
listeners.tcp.default = 5672
default_user = admin
default_pass = change_me
vm_memory_high_watermark.relative = 0.6
disk_free_limit.absolute = 2GB
log.console.level = info
```

On Linux it's usually at `/etc/rabbitmq/rabbitmq.conf`. Settings that can't be written in this format go into `advanced.config`, which uses Erlang terms.

## 57: What is a RabbitMQ node?

A node is one running RabbitMQ server (one Erlang VM). It has a name like `rabbit@hostname`, and the hostname part must be resolvable by other nodes and CLI tools.

Several nodes can be joined into a cluster. Each node has its own data directory with its metadata and queue data.

## 58: What is a RabbitMQ cluster?

A cluster is a group of nodes that share users, vhosts, exchanges, bindings, policies and queue definitions. A client can connect to any node and use any queue, even if the queue's data lives on another node, because nodes forward traffic to each other.

Clusters are used for high availability (with quorum queues and streams, data is replicated across nodes) and to spread load. A cluster usually has 3 or 5 nodes in the same data center or region.

## 59: What is the Erlang cookie?

The Erlang cookie is a shared secret that Erlang nodes use to authenticate each other. All nodes in a cluster and all CLI tools that talk to them must have the same cookie.

It's stored in a file called `.erlang.cookie` (for example `/var/lib/rabbitmq/.erlang.cookie`), and the file must be readable only by its owner. If the cookies differ, nodes can't cluster and `rabbitmqctl` fails with an authentication error. Treat it like a password, because anyone with it can control the node.

## 60: How do you connect to RabbitMQ from Node.js?

The most used library is `amqplib`:

```bash
npm install amqplib
```

```js
import amqp from "amqplib";

const connection = await amqp.connect("amqp://user:pass@localhost:5672/");
const channel = await connection.createChannel();

connection.on("error", (err) => console.error("Connection error", err));
connection.on("close", () => console.log("Connection closed"));
```

Open the connection once when the app starts and reuse it.

## 61: How do you send a message to a queue in Node.js?

```js
import amqp from "amqplib";

const connection = await amqp.connect("amqp://localhost");
const channel = await connection.createChannel();

const queue = "emails";
await channel.assertQueue(queue, { durable: true });

const payload = { to: "user@example.com", subject: "Welcome" };
channel.sendToQueue(queue, Buffer.from(JSON.stringify(payload)), {
  persistent: true,
  contentType: "application/json",
});

await channel.close();
await connection.close();
```

`sendToQueue` publishes to the default exchange with the queue name as the routing key.

## 62: How do you consume messages in Node.js?

```js
import amqp from "amqplib";

const connection = await amqp.connect("amqp://localhost");
const channel = await connection.createChannel();

await channel.assertQueue("emails", { durable: true });
await channel.prefetch(10);

await channel.consume("emails", async (msg) => {
  if (msg === null) return; // consumer was cancelled by the broker
  try {
    const data = JSON.parse(msg.content.toString());
    await sendEmail(data);
    channel.ack(msg);
  } catch (err) {
    channel.nack(msg, false, false);
  }
});
```

The callback gets `null` if RabbitMQ cancels the consumer, for example when the queue is deleted.

## 63: How do you publish a message to an exchange in Node.js?

```js
await channel.assertExchange("orders", "topic", { durable: true });

channel.publish(
  "orders",
  "order.created",
  Buffer.from(JSON.stringify({ id: 42, total: 99.5 })),
  {
    persistent: true,
    contentType: "application/json",
    messageId: "order-42-created",
  },
);
```

The arguments are exchange name, routing key, body (a Buffer) and options.

## 64: What does it mean that declaring a queue or exchange is idempotent?

Declaring (`assertQueue`, `assertExchange`) creates the object only if it doesn't exist. If it already exists with the same settings, nothing happens and the call succeeds.

That's why it's common for both producers and consumers to declare what they need on startup. It doesn't matter which one starts first, and running the declaration many times is safe.

## 65: What happens if you declare an existing queue with different arguments?

RabbitMQ refuses it with a `PRECONDITION_FAILED` error (code 406) and closes the channel. For example, if `orders` exists as a classic queue and your code declares it with `x-queue-type: quorum`, or with a different `durable` flag or TTL.

```
Channel closed by server: 406 (PRECONDITION-FAILED) with message
"PRECONDITION_FAILED - inequivalent arg 'x-queue-type' for queue 'orders'..."
```

To change those settings you have to delete and recreate the queue, or use policies for settings that can be changed at runtime.

## 66: What is the work queue pattern?

In a work queue (task queue), many workers consume from the same queue, and each message is processed by exactly one worker. This spreads slow jobs across several processes and lets you scale by adding workers.

A good work queue uses durable queues, persistent messages, manual acks and a prefetch limit, so tasks aren't lost when a worker crashes and busy workers don't get flooded.

## 67: How does RabbitMQ distribute messages between several consumers of one queue?

By default it uses round-robin: message 1 to consumer A, message 2 to consumer B, and so on. It doesn't look at how busy each consumer is.

Without a prefetch limit, one slow consumer can get a huge backlog of unacked messages while another sits idle. Setting a prefetch (for example `channel.prefetch(1)` for long jobs) makes RabbitMQ send a new message only when the consumer has room, which gives a fairer distribution.

## 68: What is prefetch (basic.qos)?

Prefetch is the maximum number of unacked messages RabbitMQ will send to a consumer at once. When the limit is reached, RabbitMQ waits until the consumer acks something before sending more.

```js
await channel.prefetch(20);
```

Without it, RabbitMQ pushes as many messages as it can, which can use a lot of client memory and make load balancing between consumers unfair. Prefetch only applies when using manual acks.

## 69: What is the publish/subscribe pattern in RabbitMQ?

In pub/sub, one message is delivered to many consumers. The producer publishes to an exchange (usually fanout or topic), and each subscriber has its own queue bound to it. Every queue gets its own copy of each message.

For example, an `order.created` event can go to a billing queue, a shipping queue and an email queue at the same time, and each service processes it independently.

## 70: What is the routing pattern?

Routing means consumers receive only a subset of messages based on the routing key. With a direct exchange, a queue bound with `error` gets only error logs, while another queue bound with `info`, `warning` and `error` gets all three.

With a topic exchange you can go further and route by patterns like `order.eu.*` or `*.payment.#`.

## 71: How do you do RPC (request/reply) with RabbitMQ?

The client sends a request message with two properties:

- `replyTo`: the queue where the server should send the response
- `correlationId`: a unique ID to match the response with the request

The server processes the request and publishes the result to the `replyTo` queue with the same `correlationId`. The client listens on that queue and matches responses by ID.

```js
const { queue: replyQueue } = await channel.assertQueue("", {
  exclusive: true,
});
const correlationId = crypto.randomUUID();

channel.sendToQueue("rpc.prices", Buffer.from(JSON.stringify({ sku: "A1" })), {
  replyTo: replyQueue,
  correlationId,
});
```

RabbitMQ also has "direct reply-to" (`amq.rabbitmq.reply-to`), which avoids creating a reply queue.

## 72: Why do you need a correlation ID in RPC?

A client often sends many requests and uses one reply queue for all of them. Responses can arrive in any order, so the client needs a way to know which response belongs to which request.

The client puts a unique `correlationId` on each request, the server copies it onto the response, and the client looks it up in a map of pending requests. Responses with an unknown ID (for example, ones that arrive after a timeout) can just be ignored.

## 73: What is message TTL?

Message TTL (time to live) is how long a message can stay in a queue before it expires. Expired messages are deleted, or dead-lettered if a dead letter exchange is set.

You can set it for the whole queue or for each message:

```js
// per queue
await channel.assertQueue("prices", { arguments: { "x-message-ttl": 60000 } });

// per message (string, in milliseconds)
channel.sendToQueue("prices", body, { expiration: "60000" });
```

If both are set, the lower value wins. It's useful for data that becomes useless after some time, like price quotes or one-time codes.

## 74: What is queue TTL (x-expires)?

Queue TTL deletes the queue itself after it has been unused for the given time. "Unused" means no consumers, no `basic.get` calls and no redeclaration during that time.

```js
await channel.assertQueue("session-123", {
  arguments: { "x-expires": 30 * 60 * 1000 },
});
```

It's a good way to clean up queues created per user or per session that might otherwise be left behind.

## 75: What is a dead letter exchange (DLX)?

A dead letter exchange is a normal exchange that receives messages that "died" in another queue. You set it on a queue with the `x-dead-letter-exchange` argument or with a policy, and you bind a queue to it (often called a dead letter queue, or DLQ) to keep those messages.

```js
await channel.assertExchange("dlx", "direct", { durable: true });
await channel.assertQueue("orders.dlq", { durable: true });
await channel.bindQueue("orders.dlq", "dlx", "orders");

await channel.assertQueue("orders", {
  durable: true,
  arguments: {
    "x-queue-type": "quorum",
    "x-dead-letter-exchange": "dlx",
    "x-dead-letter-routing-key": "orders",
  },
});
```

The DLQ lets you inspect failed messages and replay them later instead of losing them.

## 76: When does a message get dead-lettered?

A message is dead-lettered when:

1. A consumer rejects or nacks it with `requeue: false`
2. It expires because of message TTL
3. It's dropped because the queue hit its length limit (with `overflow: drop-head`)
4. In a quorum queue, it was delivered more times than the delivery limit

The reason is recorded in the `x-death` header (`rejected`, `expired`, `maxlen` or `delivery_limit`). If no DLX is set, the message is just discarded.

## 77: How do you limit the length of a queue?

Use `x-max-length` (number of messages) or `x-max-length-bytes` (total size of message bodies), as queue arguments or better as a policy:

```bash
rabbitmqctl set_policy max-len '^logs\.' '{"max-length": 100000}' --apply-to queues
```

When the limit is reached, by default the oldest messages are dropped from the front of the queue (or dead-lettered). Length limits protect the broker from running out of memory or disk when consumers stop.

## 78: What happens when a queue reaches its maximum length?

It depends on the `x-overflow` setting:

- `drop-head` (default): the oldest messages are removed from the head of the queue, and dead-lettered if a DLX is set
- `reject-publish`: new messages are refused; with publisher confirms, the publisher gets a nack
- `reject-publish-dlx`: new messages are refused and dead-lettered (classic queues only)

`reject-publish` is the right choice when losing old messages is worse than slowing down the producer.

## 79: What are publisher confirms?

Publisher confirms are a way for the broker to tell the publisher that it has taken responsibility for a message. The publisher turns on confirm mode on the channel, and RabbitMQ answers each publish with an ack (handled safely) or a nack (couldn't be handled).

For persistent messages in durable queues, the ack is sent after the message is written to disk (for quorum queues, after a majority of replicas have it). Without confirms, a publisher has no idea if a message was lost on the way.

```js
const channel = await connection.createConfirmChannel();
channel.publish("orders", "order.created", body, { persistent: true });
await channel.waitForConfirms();
```

## 80: What is the mandatory flag?

When you publish with `mandatory: true` and the message can't be routed to any queue, RabbitMQ sends it back to the publisher with a `basic.return`, instead of silently dropping it.

```js
channel.on("return", (msg) => {
  console.warn("Unroutable message", msg.fields.routingKey);
});

channel.publish("orders", "order.unknown", body, { mandatory: true });
```

This helps catch mistakes like a typo in the routing key or a missing binding.

## 81: What happens to a message that doesn't match any binding?

By default it's dropped silently. The publisher doesn't get an error, even with publisher confirms (the broker still acks it, because it handled it the way it was told to).

To avoid losing such messages, you can:

- publish with the `mandatory` flag and listen for returned messages
- set an alternate exchange on the exchange, so unroutable messages go there

## 82: What is an alternate exchange?

An alternate exchange (AE) is an exchange where messages go when they can't be routed by the original exchange. You set it with the `alternate-exchange` argument or a policy.

```js
await channel.assertExchange("unrouted", "fanout", { durable: true });
await channel.assertQueue("unrouted.messages", { durable: true });
await channel.bindQueue("unrouted.messages", "unrouted", "");

await channel.assertExchange("orders", "topic", {
  durable: true,
  alternateExchange: "unrouted",
});
```

It's a simple way to make sure no message disappears because of a routing mistake.

## 83: Does RabbitMQ support message priorities?

Yes. For classic queues you declare a priority queue with `x-max-priority` (1 to 255, but up to 10 is recommended) and publish with a `priority` property. Higher priority messages are delivered first.

```js
await channel.assertQueue("jobs", { arguments: { "x-max-priority": 5 } });
channel.sendToQueue("jobs", body, { priority: 4 });
```

Quorum queues support priorities since RabbitMQ 4.0 without any extra argument. Priority only matters when messages are waiting in the queue; if consumers are fast and the queue is empty, there's nothing to reorder.

## 84: How do you purge a queue?

Purging removes all ready messages from a queue but keeps the queue. Messages that are delivered but not yet acked aren't removed.

```bash
rabbitmqctl purge_queue orders -p shop
```

```js
await channel.purgeQueue("orders");
```

You can also click "Purge Messages" on the queue page in the management UI. Be careful, purged messages are gone for good.

## 85: How do you delete a queue?

```bash
rabbitmqctl delete_queue orders -p shop
```

```js
await channel.deleteQueue("orders", { ifUnused: true, ifEmpty: true });
```

`ifUnused` only deletes it if it has no consumers, and `ifEmpty` only if it has no messages. Deleting a queue removes its messages and bindings, and its consumers get a cancel notification.

## 86: How do you see which queues exist and how many messages they have?

```bash
rabbitmqctl list_queues -p shop name type messages messages_ready messages_unacknowledged consumers
```

Or open the Queues and Streams tab in the management UI, or call the HTTP API:

```bash
curl -u admin:secret http://localhost:15672/api/queues/shop
```

`messages_ready` are waiting to be delivered, and `messages_unacknowledged` were delivered but not acked yet.

## 87: What are queue arguments (x-arguments)?

Queue arguments are optional settings passed when declaring a queue. Their names start with `x-`. Common ones:

- `x-queue-type`: `classic`, `quorum` or `stream`
- `x-message-ttl`, `x-expires`
- `x-max-length`, `x-max-length-bytes`, `x-overflow`
- `x-dead-letter-exchange`, `x-dead-letter-routing-key`
- `x-max-priority`
- `x-single-active-consumer`
- `x-delivery-limit` (quorum queues)

Most of them can't be changed after the queue is created, except by deleting and recreating it. That's one reason policies are usually preferred.

## 88: What is a policy?

A policy applies settings to queues or exchanges whose names match a regex, without changing application code. Policies can be added, changed or removed at runtime, and existing queues pick up the change.

```bash
rabbitmqctl set_policy -p shop orders-dlx '^orders\.' \
  '{"dead-letter-exchange":"dlx","message-ttl":86400000}' \
  --apply-to queues --priority 10
```

Only one policy applies to an object at a time (the one with the highest priority), so combine all needed keys in one policy.

## 89: What is the difference between a queue argument and a policy?

Queue arguments are set by the app when it declares the queue. They're fixed for the queue's lifetime, and a mismatch on redeclare causes a channel error.

Policies are set by operators on the server and match queues by name. They can be changed anytime without redeploying apps or recreating queues.

The usual recommendation: use policies for things like TTL, length limits and DLX settings, and use arguments only for things that must be set at creation, like `x-queue-type`. If both are set for the same key, the argument usually wins (for some numeric limits, the lower value is used).

## 90: What are heartbeats?

Heartbeats are small frames that the client and server send to each other when a connection is idle, so both sides can notice a dead connection (for example when a network cable is pulled or a firewall drops the connection silently).

The client and server agree on a timeout when connecting (the server suggests 60 seconds by default). If no data or heartbeat arrives for about two intervals, the connection is considered dead and closed.

```js
const connection = await amqp.connect("amqp://localhost?heartbeat=30");
```

Don't set it to 0 (disabled) or to very low values like 1 second.

## 91: What is a delivery tag?

A delivery tag is a number RabbitMQ gives each message delivered on a channel. It starts at 1 and goes up with each delivery on that channel. The consumer uses it to ack, nack or reject that exact message.

Delivery tags are per channel, so you must ack on the same channel the message was delivered on. Acking with a tag from a different or closed channel causes a `PRECONDITION_FAILED - unknown delivery tag` error. amqplib takes care of the tag for you when you pass the `msg` object to `ack`.

## 92: What is a consumer tag?

A consumer tag is the identifier of a subscription on a channel. RabbitMQ generates one if you don't give one. You use it to cancel that consumer later.

```js
const { consumerTag } = await channel.consume("tasks", onMessage);
// later
await channel.cancel(consumerTag);
```

## 93: How do you stop a consumer without closing the connection?

Cancel it with its consumer tag. RabbitMQ stops sending new messages to it. Messages already delivered stay unacked until you ack or nack them.

```js
await channel.cancel(consumerTag);
```

This is useful during a graceful shutdown: cancel the consumer, wait for in-flight messages to finish and ack, then close the channel and connection.

## 94: What is the difference between basic.get and basic.consume?

- `basic.consume` (push) subscribes to a queue, and RabbitMQ pushes messages as they arrive. This is the normal and efficient way.
- `basic.get` (pull) asks for one message at a time with a separate request. It's slow because each message needs a round trip, and polling an empty queue wastes resources.

```js
const msg = await channel.get("tasks", { noAck: false });
if (msg) channel.ack(msg);
```

Use `get` only for scripts, tests or rare manual checks.

## 95: Does RabbitMQ keep messages in order?

Messages published on one channel to one queue are stored in the order they were published. With a single consumer, they are delivered in that order too.

Order can break when:

- there are several consumers on the queue (they process at different speeds)
- messages are requeued or redelivered after a failure
- priorities are used
- messages come from different publishers or channels

If order matters, use one consumer per queue, the single active consumer feature, or partition messages by key across several queues.

## 96: What delivery guarantees does RabbitMQ give?

With manual acks, durable queues, persistent messages and publisher confirms, RabbitMQ gives **at-least-once** delivery: a message won't be lost, but it can be delivered more than once (for example after a consumer crash or a publisher retry).

With auto ack or no confirms you get **at-most-once**: messages can be lost, but won't be duplicated by the broker.

There's no built-in exactly-once delivery. You get "effectively once" by making consumers idempotent, for example by tracking processed message IDs.

## 97: What is the basic difference between RabbitMQ and Kafka?

RabbitMQ is a message broker with smart routing. Messages go through exchanges to queues, consumers ack them, and they're deleted once processed. It's good for task queues, flexible routing, RPC and per-message handling.

Kafka is a distributed log. Messages are appended to partitions and kept for a configured time, consumers track their own offsets, and many consumer groups can read the same data. It's good for event streaming, replay and very high throughput.

RabbitMQ streams cover part of Kafka's use cases, so the line is less sharp than it used to be.

## 98: What is the difference between RabbitMQ and Redis pub/sub?

Redis pub/sub is fire-and-forget: if no subscriber is connected when a message is published, it's lost. There are no acks, no persistence and no retries.

RabbitMQ stores messages in queues until consumers ack them, supports persistence, replication, dead lettering and complex routing. Redis Streams and libraries like BullMQ give Redis more queue-like features, but RabbitMQ is still the more complete messaging system. Redis is a good fit for simple jobs when you already run Redis.

## 99: What are common use cases for RabbitMQ?

- Background jobs: emails, image processing, report generation
- Communication between microservices with events (`order.created`, `user.registered`)
- Spreading load across many workers
- Buffering traffic spikes in front of a slow service or database
- Request/reply between services
- IoT messaging over MQTT
- Fan-out of notifications to several services
- Event streams and replay with RabbitMQ streams

## 100: When is RabbitMQ not a good choice?

- When you need to keep and replay large amounts of events for months, Kafka or a similar log is usually better (though RabbitMQ streams can help)
- When you just need a simple job queue and already have Redis or a managed queue like SQS
- When the caller needs an immediate answer and there's no reason for async processing; a plain HTTP call is simpler
- When messages are very large (hundreds of MB); store the file elsewhere and send a reference
- When you can't or don't want to operate a broker and a managed service would cover your needs

## 101: Is there a limit on message size?

Yes. The maximum message size is set by `max_message_size` in `rabbitmq.conf`. The default is 16 MiB in recent versions, and the hard upper limit is 512 MiB.

```ini
max_message_size = 33554432
```

Even if you can raise it, large messages are a bad idea: they use a lot of memory, slow down replication and block other messages behind them. For files, upload them to object storage (like S3) and send only the link in the message.

## 102: How do you tell consumers what format the message body is in?

Set the `content_type` property (and `content_encoding` if the body is compressed). RabbitMQ doesn't use these values, they're just for your applications.

```js
channel.publish("events", "user.created", Buffer.from(JSON.stringify(user)), {
  contentType: "application/json",
  headers: { "schema-version": 2 },
});
```

On the consumer side, check `msg.properties.contentType` before parsing, especially if different producers send different formats.

## 103: How do you send JSON with amqplib?

The body must be a Buffer, so convert it yourself on both sides:

```js
// producer
const body = Buffer.from(JSON.stringify({ orderId: 1, items: 3 }));
channel.sendToQueue("orders", body, {
  contentType: "application/json",
  persistent: true,
});

// consumer
channel.consume("orders", (msg) => {
  const order = JSON.parse(msg.content.toString("utf8"));
  // ...
  channel.ack(msg);
});
```

Wrap `JSON.parse` in try/catch. A message with bad JSON will never parse, so it should be rejected without requeue (and sent to a DLQ), not retried forever.

## 104: What is the management HTTP API?

The management plugin exposes a REST API on port 15672. It can do almost everything the UI does: list and create queues, exchanges, bindings, users, vhosts and policies, read metrics and run health checks.

```bash
curl -u admin:secret http://localhost:15672/api/overview
curl -u admin:secret http://localhost:15672/api/queues/%2F/orders
curl -u admin:secret -X PUT -H 'content-type: application/json' \
  -d '{"durable":true,"arguments":{"x-queue-type":"quorum"}}' \
  http://localhost:15672/api/queues/%2F/orders
```

The default vhost `/` is written as `%2F` in URLs. The API is for management and monitoring, not for publishing and consuming in production.

## 105: What is the memory alarm?

RabbitMQ watches its own memory use. When it goes above the memory high watermark (by default 60% of the available RAM, `vm_memory_high_watermark.relative = 0.6`), it raises a memory alarm.

While the alarm is on, RabbitMQ blocks all connections that publish messages, across the whole cluster. Consumers keep working, so they can drain the queues and bring memory back down. When memory drops below the limit, publishers are unblocked.

## 106: What is the disk alarm?

RabbitMQ checks free disk space on the partition where it stores data. If free space drops below `disk_free_limit` (the default is 50 MB, which is far too low for production), it raises a disk alarm and blocks publishers, just like the memory alarm.

```ini
disk_free_limit.absolute = 5GB
```

Set the limit to something that gives you time to react, for example a few GB or a value close to the RAM size. Running out of disk completely can crash the node and corrupt data.

## 107: What happens to publishers when an alarm is triggered?

RabbitMQ stops reading from the sockets of connections that publish. The connection state shows as `blocking` or `blocked`. The publisher's writes just hang, and the client may not notice anything unless it listens for the `connection.blocked` notification.

```js
connection.on("blocked", (reason) =>
  console.warn("Blocked by broker:", reason),
);
connection.on("unblocked", () => console.log("Unblocked"));
```

This is one reason to use separate connections for publishing and consuming: if they share a connection, a blocked publisher could also stop the consumer from acking, and the queues never drain.

## 108: Where are RabbitMQ logs and how do you change the log level?

By default logs go to a file in the log directory (for example `/var/log/rabbitmq/rabbit@hostname.log`). In the Docker image they go to the console (stdout), so you read them with `docker logs`.

```ini
log.file.level = info
log.console = true
log.console.level = warning
```

Levels are `debug`, `info`, `warning`, `error`, `critical` and `none`. You can also change it at runtime with `rabbitmqctl set_log_level debug`. Debug is very noisy, so don't leave it on in production.

## 109: How do you check if a RabbitMQ node is running and healthy?

```bash
rabbitmq-diagnostics ping              # node is up and responding
rabbitmq-diagnostics check_running     # RabbitMQ app is running
rabbitmq-diagnostics check_local_alarms
rabbitmq-diagnostics status            # versions, memory, disk, listeners
rabbitmqctl cluster_status
```

`ping` is the lightest check and is good for a liveness probe. For readiness you can add `check_port_connectivity` to make sure the listeners accept connections.

## 110: What do rabbitmqctl stop_app and start_app do?

`stop_app` stops the RabbitMQ application but leaves the Erlang VM running, so you can still run CLI commands on the node. `start_app` starts it again.

```bash
rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@node1
rabbitmqctl start_app
```

This is used when joining a node to a cluster or resetting it. To stop the whole node, use `rabbitmqctl stop` or stop the service.

## 111: What does rabbitmqctl reset do?

`reset` wipes the node: it removes it from its cluster and deletes all data, including queues, messages, users and vhosts. The app must be stopped first.

```bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
```

Only use it when you really want to start the node from scratch, for example before rejoining a cluster. `force_reset` is deprecated since 4.1 because it doesn't work with Khepri.

## 112: Can exchanges be durable or auto-delete?

Yes.

- A **durable** exchange survives a broker restart. A transient one is deleted on restart.
- An **auto-delete** exchange is deleted when its last binding is removed.

```js
await channel.assertExchange("events", "topic", {
  durable: true,
  autoDelete: false,
});
```

If a durable queue is bound to a transient exchange, the binding is lost when the exchange disappears on restart, so keep exchanges durable for anything that matters.

## 113: What is an internal exchange?

An internal exchange can't receive messages directly from publishers. It can only receive messages from other exchanges through exchange-to-exchange bindings.

```js
await channel.assertExchange("billing.internal", "topic", {
  durable: true,
  internal: true,
});
```

It's used to build routing layers where you want to make sure clients don't bypass the main entry exchange.

## 114: What is an exchange-to-exchange binding?

RabbitMQ lets you bind an exchange to another exchange, not just to a queue. Messages routed to the destination exchange then follow that exchange's own bindings.

```js
await channel.bindExchange("audit", "orders", "#"); // destination, source, pattern
```

This lets you build layered routing: for example, a topic exchange `orders` sends everything to a fanout `audit` exchange, which copies it to several audit queues. It's a RabbitMQ extension to AMQP 0-9-1.

## 115: What are message headers used for?

Headers are custom key-value pairs on a message. Common uses:

- Tracing info like `traceparent` or a request ID
- Schema version or event type
- Tenant ID
- Retry count kept by the app
- Routing in headers exchanges

```js
channel.publish("events", "user.updated", body, {
  headers: { "x-tenant-id": "acme", "schema-version": 3 },
});
```

RabbitMQ also adds its own headers, like `x-death` when a message is dead-lettered.

## 116: How do you set an expiration on a single message?

Use the `expiration` property. The value is a string with the number of milliseconds.

```js
channel.sendToQueue("otp", body, { expiration: "30000" }); // 30 seconds
```

amqplib also accepts a number and converts it. Note that in classic queues a message with per-message TTL is only removed when it reaches the head of the queue, so expired messages behind a long-lived one can stay in the queue longer than their TTL.

## 117: Why set a message ID and timestamp?

RabbitMQ doesn't generate IDs or timestamps for you. Setting them yourself helps a lot:

- `messageId` lets consumers detect duplicates and gives you something to search for in logs.
- `timestamp` tells you how old the message is when it's processed, which helps you measure lag or skip stale messages.

```js
channel.publish("orders", "order.created", body, {
  messageId: crypto.randomUUID(),
  timestamp: Math.floor(Date.now() / 1000),
});
```

The AMQP 0-9-1 timestamp is in seconds, not milliseconds.

## 118: What is the Shovel plugin?

Shovel is a plugin that reads messages from a source (a queue) and publishes them to a destination (an exchange or queue), which can be on the same broker or on a different one. It acts like a small built-in consumer plus producer.

It's used to move messages between clusters, to migrate data to a new cluster, or to move messages from a DLQ back to the main queue. Shovels can be static (in config) or dynamic (created at runtime with a parameter or the UI).

## 119: What is the Federation plugin?

Federation lets exchanges or queues on one broker receive messages from another broker (the upstream) over AMQP, without clustering them together. The brokers can be in different data centers and have different users and versions.

- **Federated exchanges** copy messages published upstream to the downstream exchange.
- **Federated queues** let a downstream queue pull messages from an upstream queue when it has consumers and nothing to give them.

It's built for WAN links where clustering doesn't work well.

## 120: Does RabbitMQ support MQTT?

Yes, with the `rabbitmq_mqtt` plugin. It supports MQTT 3.1, 3.1.1 and 5.0. MQTT clients connect on port 1883 (8883 with TLS), and their messages are routed through the `amq.topic` exchange by default, with MQTT topic slashes mapped to dots.

```bash
rabbitmq-plugins enable rabbitmq_mqtt
```

Since 3.12 MQTT is handled natively, which made it possible to have millions of MQTT connections on one cluster. It's common for IoT devices sending data that is then processed by AMQP consumers.

## 121: Does RabbitMQ support STOMP?

Yes, with the `rabbitmq_stomp` plugin on port 61613. STOMP is a simple text protocol that some older systems and frameworks use. With `rabbitmq_web_stomp`, STOMP also works over WebSockets on port 15674, so a browser can connect directly.

Since RabbitMQ 4.4, the STOMP plugin is a standalone protocol implementation and no longer runs on top of AMQP 0-9-1 internally.

## 122: Can a browser connect to RabbitMQ directly?

Yes, using the Web STOMP or Web MQTT plugins, which accept STOMP or MQTT over WebSockets. The browser uses a client like `@stomp/stompjs` or `mqtt.js`.

In practice it's often better to keep RabbitMQ private and have your backend forward events to browsers through your own WebSocket or SSE server. That way you control authentication, rate limits and what data the browser sees, and the broker isn't exposed to the internet.

## 123: What is AMQP 1.0 in RabbitMQ?

AMQP 1.0 is a different protocol from AMQP 0-9-1 despite the name. It's an ISO/OASIS standard and doesn't define exchanges and queues the same way, it's more about links between containers.

Since RabbitMQ 4.0, AMQP 1.0 is a core protocol (no plugin needed) and runs on the same port 5672. RabbitMQ also provides new AMQP 1.0 client libraries for several languages, which can manage queues and exchanges and send and receive messages. Some newer features, like SQL filter expressions on streams, are only available over AMQP 1.0.

## 124: What is the stream protocol?

The stream protocol is a binary protocol made only for RabbitMQ streams. It runs on port 5552 with the `rabbitmq_stream` plugin and is faster than using streams over AMQP, because it's designed for things like batching, offset tracking and publisher de-duplication.

There are official stream clients for Java, .NET, Go, Rust, Python and Node.js. You still can use streams from AMQP 0-9-1 or 1.0 clients, but with lower throughput.

## 125: What are feature flags?

Feature flags control which features are enabled in a cluster, so you can do rolling upgrades with nodes running different versions for a short time. New features that change how nodes talk to each other or store data are behind a flag and are only enabled when all nodes support them.

```bash
rabbitmqctl list_feature_flags
rabbitmqctl enable_feature_flag all
```

After upgrading all nodes, enable all stable feature flags. The next upgrade often requires them, for example upgrading to 4.3 requires all flags from 4.2 and earlier to be enabled.

## 126: What is Khepri?

Khepri is the metadata store RabbitMQ uses to keep cluster data like users, vhosts, queue and exchange definitions, bindings and policies. It's based on the Raft algorithm (the same Ra library quorum queues use), so changes are agreed on by a majority of nodes.

It replaced Mnesia. It became the default for new clusters in 4.2, and since 4.3 it's the only metadata store, Mnesia was removed. One practical effect: if most nodes of the cluster are down, you can't create or delete queues, users and so on until a majority is back.

## 127: What happened to classic mirrored queues?

Classic mirrored queues (also called HA queues, set up with `ha-mode` policies) were a way to replicate classic queues across nodes. They were deprecated for years and removed in RabbitMQ 4.0.

They had real problems: data loss in some failure cases, slow and blocking resyncs, and weird behavior during network partitions. Quorum queues replaced them for replicated queues, and streams cover log-style use cases. If you still have `ha-mode` policies, you must migrate before upgrading to 4.x.

## 128: What is the current version of RabbitMQ and how often are new versions released?

At the time of writing, the latest series is RabbitMQ 4.4 (4.4.0 was released in October 2026), and 4.3 is still supported. The 4.x line started in 2024.

New minor series come out a few times a year, with patch releases in between. Each series gets community support only for a limited time, and you can usually only upgrade from the previous minor series (for example, 4.3 can only be upgraded from 4.2), so it's worth staying close to the latest version.

## 129: What Erlang version does RabbitMQ need?

Each RabbitMQ version supports a specific range of Erlang/OTP versions, listed on the "Erlang version requirements" page of the docs. For example, RabbitMQ 4.4 supports Erlang 28 and 29.

If you use the official Docker image, Kubernetes operator or the packages that bundle Erlang, you don't need to think about it. If you install Erlang yourself, check the table before upgrading either one, because an unsupported pair may not start or may behave badly.

## 130: Which Docker image tag should you use?

The official image is `rabbitmq` on Docker Hub. Tags without `-management` contain only the broker; tags with `-management` also have the management plugin enabled.

- `rabbitmq:4-management`: latest 4.x with the UI
- `rabbitmq:4.4-management`: latest 4.4.x patch
- `rabbitmq:4.4.0-management`: exact version
- `-alpine` variants are smaller

In production, pin at least the minor version (`4.4`) so a container restart doesn't pull a new series by surprise.

## 131: How do you add RabbitMQ to a Docker Compose project?

```yaml
services:
  rabbitmq:
    image: rabbitmq:4.4-management
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: app
      RABBITMQ_DEFAULT_PASS: app_password
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: .
    environment:
      AMQP_URL: amqp://app:app_password@rabbitmq:5672
    depends_on:
      rabbitmq:
        condition: service_healthy

volumes:
  rabbitmq-data:
```

The volume keeps data between restarts. Set a fixed `hostname` on the service too if you want the node name (and so its data directory) to stay the same when the container is recreated.

## 132: What do RABBITMQ_DEFAULT_USER and RABBITMQ_DEFAULT_PASS do?

They're environment variables supported by the official Docker image to create a default user with that name and password instead of `guest`, on the first start when the data directory is empty.

Newer versions prefer the `default_user` and `default_pass` keys in `rabbitmq.conf`. Either way they only apply when the node is created; changing them later doesn't change an existing user. Don't put real production passwords in plain text in compose files, use secrets.

## 133: What does an AMQP connection URL look like?

```
amqp://username:password@host:port/vhost?heartbeat=30
amqps://username:password@host:5671/vhost
```

- The default port is 5672 for `amqp` and 5671 for `amqps`.
- The vhost must be URL-encoded. The default vhost `/` is `%2F`, and leaving the path empty also uses `/`.
- Special characters in the password must be URL-encoded too.

```js
const url = `amqp://app:${encodeURIComponent(password)}@rabbit:5672/shop`;
```

## 134: How do you connect to RabbitMQ with TLS?

Use an `amqps://` URL and port 5671. On the server, configure the certificate and key:

```ini
listeners.ssl.default = 5671
ssl_options.cacertfile = /etc/rabbitmq/ca.pem
ssl_options.certfile = /etc/rabbitmq/server.pem
ssl_options.keyfile = /etc/rabbitmq/server-key.pem
ssl_options.verify = verify_peer
ssl_options.fail_if_no_peer_cert = false
```

In Node.js:

```js
import fs from "node:fs";

const connection = await amqp.connect(
  "amqps://app:secret@rabbit.example.com:5671",
  {
    ca: [fs.readFileSync("ca.pem")],
  },
);
```

Managed services like CloudAMQP and Amazon MQ give you an `amqps://` URL that works out of the box.

## 135: Why should you close channels and connections properly?

When an app exits without closing, RabbitMQ only finds out when the TCP connection drops or heartbeats time out. Until then it may keep messages assigned to that dead consumer as unacked.

Closing cleanly also makes sure pending publishes and acks are flushed. A common shutdown handler:

```js
process.on("SIGTERM", async () => {
  await channel.close();
  await connection.close();
  process.exit(0);
});
```

## 136: What is single active consumer?

Single active consumer (SAC) is a queue feature where many consumers can subscribe, but only one of them gets messages at a time. If the active consumer goes away, the next one takes over automatically.

```js
await channel.assertQueue("invoices", {
  durable: true,
  arguments: { "x-queue-type": "quorum", "x-single-active-consumer": true },
});
```

It gives you strict ordering (only one consumer processes the queue) and failover without writing your own leader election.

## 137: What are consumer priorities?

Consumer priorities let you say which consumers should get messages first. RabbitMQ sends messages to the highest-priority consumer that can take them (not blocked by its prefetch), and only uses lower-priority ones when the higher ones are full.

```js
await channel.consume("tasks", onMessage, { priority: 10 });
```

It's useful when you have a fast primary worker and slower backup workers. This is different from message priority, which orders messages inside a queue.

## 138: What were lazy queues?

Lazy queues were classic queues that moved messages to disk as early as possible to save memory, set with `x-queue-mode: lazy`. They were useful for very long queues.

Since classic queues version 2 (the only version since 4.3), classic queues already keep little in memory, so lazy mode doesn't exist anymore. In RabbitMQ 4.3+, declaring a queue with `x-queue-mode` fails. If you see it in old code or policies, remove it.

## 139: What is an exclusive consumer?

An exclusive consumer is a subscription where you ask to be the only consumer of a queue. If another consumer already exists, the request fails, and while you're subscribed, nobody else can subscribe.

```js
await channel.consume("reports", onMessage, { exclusive: true });
```

Unlike single active consumer, there's no automatic failover: if the exclusive consumer leaves, another app has to retry subscribing. Single active consumer is usually the better choice.

## 140: Can one queue have several bindings?

Yes. A queue can be bound to the same exchange with several keys, or to several exchanges. It gets a message if any of its bindings matches, but it receives only one copy even if several bindings match the same message.

```js
await channel.bindQueue("alerts", "logs", "error");
await channel.bindQueue("alerts", "logs", "critical");
await channel.bindQueue("alerts", "security", "login.failed");
```

## 141: When a message goes to several queues, is it copied?

Logically yes, each queue has its own copy and handles it independently: acking it in one queue doesn't affect the others.

Internally RabbitMQ avoids copying the body when it can. Classic queues on the same node share large message bodies in a shared message store, while quorum queues and streams each store their own copy in their log. So fan-out to many quorum queues means more disk writes than fan-out to classic queues.

## 142: Can one consumer read from several queues?

Yes. A consumer can subscribe to several queues on the same channel, each with its own consumer tag.

```js
await channel.consume("orders.eu", handleOrder);
await channel.consume("orders.us", handleOrder);
```

The prefetch limit applies per consumer by default, so each subscription gets its own limit. If the queues have very different importance, use separate channels or consumer priorities instead of relying on the order of delivery.

## 143: What is the difference between a queue and a topic conceptually?

In messaging in general, a queue means point-to-point: each message is processed by one consumer. A topic means pub/sub: each message goes to all subscribers.

RabbitMQ builds both from the same parts. Point-to-point is one queue with several consumers. Pub/sub is an exchange with several queues bound to it, one per subscriber. Note that "topic exchange" in RabbitMQ is a specific exchange type with pattern matching, not the same thing as a topic in Kafka or JMS.

## 144: What is the competing consumers pattern?

Several instances of the same service read from one queue, and they "compete" for messages: each message goes to only one instance. You scale processing by running more instances.

In RabbitMQ that's just several consumers on one queue. Combine it with manual acks and prefetch so a crashed instance doesn't lose work and a slow one doesn't take too many messages.

## 145: What is the difference between fire-and-forget and request/reply messaging?

In fire-and-forget, the producer sends a message and moves on, without waiting for a result. It's the most common style: events and background jobs.

In request/reply, the producer waits for a response message, usually with a timeout. It's used when the caller needs an answer but still wants the decoupling and load balancing of a broker. For most request/reply needs between web services, HTTP or gRPC is simpler, so use RPC over RabbitMQ only when it really helps.

## 146: How do you delay a message in RabbitMQ?

There are a few ways:

- **TTL + dead letter exchange:** publish to a "wait" queue with a TTL and no consumers. When the message expires, it's dead-lettered to the real queue. This works everywhere, but per-message TTLs only expire at the head of the queue, so you usually use one wait queue per delay value.
- **Quorum queue delayed messages:** RabbitMQ 4.4 added support for delayed delivery in quorum queues.
- **Delayed message exchange plugin:** a community plugin with an `x-delayed-message` exchange. It's no longer maintained and isn't recommended for new projects.

For long or precise delays (days, specific dates) a scheduler or database job table is often a better fit.

## 147: What is the rabbitmq_prometheus plugin?

It exposes RabbitMQ metrics in Prometheus format on port 15692 at `/metrics`. Prometheus scrapes it, and you build dashboards in Grafana (the RabbitMQ team publishes ready-made dashboards).

```bash
rabbitmq-plugins enable rabbitmq_prometheus
curl http://localhost:15692/metrics
```

It's the recommended way to monitor RabbitMQ in production, instead of relying on the management UI's metrics.

## 148: What frameworks and tools use RabbitMQ under the hood?

Many frameworks support RabbitMQ as a transport:

- **Celery** (Python background tasks)
- **NestJS microservices** with the RMQ transport
- **Spring AMQP / Spring Cloud Stream** (Java)
- **MassTransit** and **NServiceBus** (.NET)
- **Laravel queues** (with a community driver)
- **Symfony Messenger** (PHP)

These hide some details, but you still need to understand queues, acks and retries to configure them well.

## 149: What is the RabbitMQ Cluster Operator for Kubernetes?

It's an official Kubernetes operator that creates and manages RabbitMQ clusters from a `RabbitmqCluster` custom resource. It handles StatefulSets, services, config, TLS, rolling upgrades and scaling for you.

```yaml
apiVersion: rabbitmq.com/v1beta1
kind: RabbitmqCluster
metadata:
  name: my-rabbit
spec:
  replicas: 3
```

The related Messaging Topology Operator lets you define queues, exchanges, bindings, users and policies as Kubernetes resources too.

## 150: What does the "unacked" count in the management UI mean?

It's the number of messages delivered to consumers that haven't been acked or rejected yet. They're not available to other consumers.

A small, steady unacked count (roughly prefetch times the number of consumers) is normal. A count that keeps growing while consumers do nothing usually means consumers are stuck, forgot to ack in some code path, or are hanging on a slow external call.

---

# Moderate Questions (151-300)

## 151: How do you publish reliably from Node.js?

Use a confirm channel, persistent messages, durable (ideally quorum) queues and handle both the confirm and returned messages.

```js
const channel = await connection.createConfirmChannel();

channel.on("return", (msg) => {
  console.error("Unroutable:", msg.fields.exchange, msg.fields.routingKey);
});

function publish(exchange, key, payload) {
  return new Promise((resolve, reject) => {
    channel.publish(
      exchange,
      key,
      Buffer.from(JSON.stringify(payload)),
      { persistent: true, mandatory: true, messageId: crypto.randomUUID() },
      (err) => (err ? reject(err) : resolve()),
    );
  });
}

await publish("orders", "order.created", { id: 1 });
```

If the promise rejects or the connection drops before the confirm arrives, you don't know if the broker got the message, so you publish it again. That's why consumers must handle duplicates.

## 152: What does it mean when channel.publish returns false in amqplib?

`publish` and `sendToQueue` return `false` when the channel's write buffer is full. The message is still buffered and will be sent, but you should stop publishing until the channel emits `drain`. If you ignore it and keep publishing in a loop, the process memory grows until it crashes.

```js
async function publishWithBackpressure(channel, ex, key, body) {
  const ok = channel.publish(ex, key, body, { persistent: true });
  if (!ok) {
    await new Promise((resolve) => channel.once("drain", resolve));
  }
}
```

This is client-side backpressure and is different from broker flow control and confirms.

## 153: How do you handle reconnection with amqplib?

amqplib doesn't reconnect on its own. You need to listen for `close` and `error`, then reconnect with a backoff and recreate channels, topology and consumers.

```js
async function connect() {
  try {
    const conn = await amqp.connect(process.env.AMQP_URL);
    conn.on("error", (err) => console.error("AMQP error", err.message));
    conn.on("close", () => {
      console.warn("AMQP closed, reconnecting");
      setTimeout(connect, 5000);
    });
    const ch = await conn.createChannel();
    await setupTopology(ch);
    await startConsumers(ch);
  } catch (err) {
    console.error("Connect failed", err.message);
    setTimeout(connect, 5000);
  }
}
```

Libraries like `amqp-connection-manager` or `rabbitmq-client` wrap this logic for you and buffer publishes while reconnecting.

## 154: Why does a channel close by itself sometimes?

RabbitMQ closes a channel when it hits a channel-level error. Common causes:

- declaring a queue or exchange with different arguments than the existing one (406)
- publishing to an exchange that doesn't exist (404)
- acking an unknown or already acked delivery tag (406)
- consuming from a queue that doesn't exist (404)
- not having permission (403)
- the consumer didn't ack within the consumer timeout (406)

The error message is in the `close` or `error` event. After that, the channel can't be used, so create a new one. Watch for code paths that ack the same message twice; that's a very common cause.

## 155: What are the common AMQP error codes?

- **320 CONNECTION_FORCED:** the broker closed the connection (shutdown, or an admin closed it)
- **403 ACCESS_REFUSED:** missing permissions or bad login
- **404 NOT_FOUND:** exchange or queue doesn't exist
- **405 RESOURCE_LOCKED:** tried to use an exclusive queue owned by another connection
- **406 PRECONDITION_FAILED:** argument mismatch, unknown delivery tag, consumer timeout
- **530 NOT_ALLOWED:** for example the vhost doesn't exist or isn't accessible
- **541 INTERNAL_ERROR:** a broker-side failure

Codes 403, 404, 405 and 406 close only the channel. Codes like 320, 530 and 541 close the whole connection.

## 156: How do you choose a prefetch value?

It depends on how long a message takes to process:

- Slow jobs (seconds or more, like video processing): a low value, 1 to 5, so work is spread evenly and nothing waits behind a slow job.
- Fast handlers (milliseconds): a higher value, like 50 to 300, so the consumer isn't idle waiting for the next message over the network.

A rough way to think about it: prefetch should cover the network round trip time divided by processing time per message. Start with something like 10 to 50, measure, and adjust. Unlimited prefetch (0) is almost always a bad idea.

## 157: What is the difference between per-consumer and global prefetch?

In AMQP 0-9-1, `basic.qos` has a `global` flag. In RabbitMQ:

- `global = false` (default in most clients): the limit applies to each new consumer on the channel separately.
- `global = true`: the limit is shared by all consumers on the channel.

Global QoS is deprecated. Since RabbitMQ 4.3 it's denied by default, and it never worked with quorum queues. Use per-consumer prefetch, and use separate channels if you need different limits.

```js
await channel.prefetch(20); // per consumer
```

## 158: How do you ack many messages at once?

Use the `multiple` flag. It acks the given message and all earlier unacked messages on the same channel.

```js
let count = 0;
await channel.consume("metrics", (msg) => {
  buffer.push(msg);
  if (++count % 100 === 0) {
    saveBatch(buffer);
    channel.ack(msg, true); // acks this one and all before it
    buffer = [];
  }
});
```

It reduces network traffic for high-volume consumers. Be careful: if processing is concurrent, a later message could be done before an earlier one fails, and a multiple ack would ack the failed one too. Also use `ackAll()` and `nackAll()` only when you mean it.

## 159: What retry strategies can you use with RabbitMQ?

1. **Requeue immediately:** `nack` with `requeue: true`. Simple, but a failing message loops fast and hammers the failing dependency.
2. **Delivery limit:** with quorum queues, requeue but let the queue stop after N attempts and dead-letter the message.
3. **Delayed retry with TTL queues:** dead-letter to a wait queue with a TTL, which sends the message back to the main queue later. Can use several wait queues for increasing delays.
4. **Retry in the consumer:** retry the operation a few times in memory with backoff before nacking. Fine for short hiccups, but it holds the message and prefetch slot.
5. **Park in a DLQ:** after the last attempt, keep the message for manual review.

Most real systems combine an in-process retry for quick errors, delayed retries with backoff, and a final DLQ.

## 160: How do you build delayed retries with TTL and dead letter exchanges?

Use a main queue, a retry (wait) queue with a TTL that dead-letters back to the main queue, and a final DLQ.

```js
await ch.assertExchange("orders", "direct", { durable: true });
await ch.assertExchange("orders.retry", "direct", { durable: true });
await ch.assertExchange("orders.dlx", "direct", { durable: true });

await ch.assertQueue("orders.work", {
  durable: true,
  arguments: {
    "x-queue-type": "quorum",
    "x-dead-letter-exchange": "orders.retry",
  },
});
await ch.bindQueue("orders.work", "orders", "work");

await ch.assertQueue("orders.wait-30s", {
  durable: true,
  arguments: {
    "x-queue-type": "quorum",
    "x-message-ttl": 30000,
    "x-dead-letter-exchange": "orders",
    "x-dead-letter-routing-key": "work",
  },
});
await ch.bindQueue("orders.wait-30s", "orders.retry", "work");

await ch.assertQueue("orders.dlq", {
  durable: true,
  arguments: { "x-queue-type": "quorum" },
});
await ch.bindQueue("orders.dlq", "orders.dlx", "work");
```

The consumer rejects failed messages with `requeue: false` (they go to the wait queue). It reads the attempt count from `x-death`, and once it's too high, it publishes the message to `orders.dlx` itself and acks the original.

## 161: How does the quorum queue delivery limit work?

Quorum queues count how many times each message was returned to the queue after a failed delivery (nack/reject with requeue, or consumer crash). When the count goes over the delivery limit, the message is dead-lettered, or dropped if there's no DLX.

Since RabbitMQ 4.0 the default limit is 20. You can change it with the `x-delivery-limit` argument or the `delivery-limit` policy key, and since 4.4 the policy also applies to queues that already exist.

```bash
rabbitmqctl set_policy qq-limits '^jobs\.' '{"delivery-limit": 5, "dead-letter-exchange": "dlx"}' --apply-to quorum_queues
```

This stops poison messages from looping forever.

## 162: What is a poison message and how do you deal with it?

A poison message is a message the consumer can never process, for example malformed JSON, a missing required field or data that triggers a bug. If it's requeued, it fails again, forever, and can block or slow down the whole queue.

How to handle it:

- Validate input and reject bad messages without requeue right away.
- Use a quorum queue delivery limit as a safety net.
- Send failed messages to a DLQ with enough info (headers, error reason) to debug them.
- Alert on DLQ size so someone looks at it.

## 163: What is the x-death header?

When a message is dead-lettered, RabbitMQ adds or updates the `x-death` header. It's an array with one entry per queue and reason, and each entry has fields like `queue`, `reason`, `count`, `exchange`, `routing-keys` and `time`.

```js
function deathCount(msg, queue) {
  const deaths = msg.properties.headers?.["x-death"] ?? [];
  const entry = deaths.find((d) => d.queue === queue);
  return entry ? entry.count : 0;
}
```

It's used to count retry attempts in TTL-based retry setups. RabbitMQ also adds `x-first-death-queue`, `x-first-death-reason`, `x-first-death-exchange` and, in recent versions, `x-last-death-*` headers.

## 164: What does x-dead-letter-routing-key do?

By default, a dead-lettered message keeps its original routing key. `x-dead-letter-routing-key` (or the `dead-letter-routing-key` policy key) replaces it with a fixed value when the message is dead-lettered.

It's useful when one DLX handles failures from many queues and you want each queue's failures to go to its own DLQ, or when the original keys are varied (like topic keys) and you just want everything in one place.

## 165: What is the x-delivery-count header?

Quorum queues add an `x-delivery-count` header to redelivered messages. It tells the consumer how many times the message was delivered and returned before (it's not set on the first delivery).

```js
const attempts = msg.properties.headers?.["x-delivery-count"] ?? 0;
if (attempts >= 3) {
  await logPoison(msg);
  channel.nack(msg, false, false);
  return;
}
```

It's more reliable than the `redelivered` flag, which is just true or false. Classic queues don't set this header.

## 166: What does it mean for a consumer to be idempotent?

An idempotent consumer gives the same result whether it processes a message once or several times. Because RabbitMQ delivers at-least-once, duplicates happen, and the consumer must handle them.

Ways to do it:

- Make the operation naturally idempotent, like `SET status = 'paid'` instead of `balance = balance + 10`.
- Store processed message IDs in a table with a unique constraint, in the same DB transaction as the business change.
- Use upserts with a business key (order ID, payment ID).
- Pass an idempotency key to external APIs (many payment APIs support this).

## 167: How do you de-duplicate messages?

RabbitMQ queues don't de-duplicate on their own (streams have publisher de-duplication, and there's a community de-duplication plugin). Most teams do it in the consumer:

```js
await db.transaction(async (tx) => {
  const inserted = await tx.query(
    "INSERT INTO processed_messages (id) VALUES ($1) ON CONFLICT DO NOTHING",
    [msg.properties.messageId],
  );
  if (inserted.rowCount === 0) return; // duplicate
  await handleOrder(tx, payload);
});
channel.ack(msg);
```

The producer must set a stable `messageId` (for example, based on the business event, not a new random ID on each retry). Old IDs can be cleaned up after a time window.

## 168: How do you design routing keys for a topic exchange?

Pick a fixed structure and keep it everywhere, from general to specific:

```
<domain>.<entity>.<event>         orders.order.created
<domain>.<region>.<event>         payments.eu.refunded
```

Tips:

- Use lowercase and dots only between words.
- Put the parts consumers filter on most often first.
- Don't put IDs or other unbounded values in the key, they make bindings useless.
- Keep the same number of words, so `*` patterns are predictable.
- Document the scheme, since it's a contract between teams.

## 169: How should you name queues and exchanges?

Use names that say who owns them and what they hold:

- Exchanges by domain or producer: `orders`, `billing.events`
- Queues by consumer and purpose: `email-service.order-created`, `billing.invoices`
- Related queues with suffixes: `.retry`, `.dlq`, `.wait-30s`

Avoid generic names like `queue1` or `events`. The consumer service should own its queues, so you can see from the name which service to blame when a queue grows.

## 170: Who should declare the topology, the producer or the consumer?

A common rule: producers declare the exchanges they publish to, and consumers declare their own queues and bind them to those exchanges. That way the producer doesn't need to know who listens, and each consumer controls its own queue settings.

Some teams instead manage all topology outside the apps (definitions file, Terraform, the Kubernetes Messaging Topology Operator) and give apps no `configure` permission. That's stricter and easier to audit, but every change needs a deployment of the infrastructure code first.

## 171: What is a definitions file?

A definitions file is a JSON export of a broker's topology: users, vhosts, permissions, policies, exchanges, queues, bindings and parameters. It doesn't contain messages.

You can import it at startup so a new node comes up with everything set:

```ini
definitions.import_backend = local_filesystem
definitions.local.path = /etc/rabbitmq/definitions.json
```

It's handy for local development, tests and setting up new environments in a repeatable way.

## 172: How do you export and import definitions?

```bash
rabbitmqctl export_definitions /tmp/definitions.json
rabbitmqctl import_definitions /tmp/definitions.json
```

You can also use the management UI (Overview > Export/Import definitions) or the HTTP API (`GET /api/definitions`, `POST /api/definitions`).

Exported files include password hashes, so keep them safe. Exporting definitions regularly is a cheap backup of your topology.

## 173: How do you write a policy and what do pattern, apply-to and priority mean?

```bash
rabbitmqctl set_policy -p shop orders-qq \
  '^orders\.' \
  '{"dead-letter-exchange":"orders.dlx","delivery-limit":10,"max-length":500000}' \
  --apply-to quorum_queues \
  --priority 5
```

- **pattern:** a regex matched against queue or exchange names.
- **definition:** the settings to apply.
- **apply-to:** `queues`, `classic_queues`, `quorum_queues`, `streams`, `exchanges` or `all`.
- **priority:** if several policies match one object, only the highest priority one is applied.

Since policies don't merge, include every key you need in the winning policy.

## 174: What are operator policies?

Operator policies are a second kind of policy, meant for operators (for example on a hosted platform) to enforce limits that users can't override. They support a smaller set of keys, mostly limits like `max-length`, `max-length-bytes`, `message-ttl`, `expires` and `delivery-limit`.

If both a normal policy and an operator policy set the same numeric limit, the stricter (lower) value wins. This lets a platform team say "no queue can hold more than 1 million messages" while app teams still manage their own policies.

```bash
rabbitmqctl set_operator_policy cap '.*' '{"max-length": 1000000}' --apply-to queues
```

## 175: What are vhost limits?

You can limit how many connections and queues a vhost may have, so one tenant or app can't take all the broker's resources.

```bash
rabbitmqctl set_vhost_limits -p tenant_a '{"max-connections": 200, "max-queues": 1000}'
```

When the limit is reached, new connections or queue declarations are refused. Setting a limit to 0 blocks new connections or queues for that vhost, which is useful during maintenance.

## 176: What are user limits?

User limits cap how many connections and channels a single user can open. They protect the broker from a buggy client that leaks connections or channels.

```bash
rabbitmqctl set_user_limits orders_app '{"max-connections": 20, "max-channels": 200}'
```

There are also limits in `rabbitmq.conf` that apply to every client. In RabbitMQ 4.4 the `connection_max` and `channel_max` settings were renamed to `max_connections` and `max_channels` (the old names still work).

## 177: How do you make new queues quorum queues by default?

Set the default queue type on the vhost. Then queues declared without `x-queue-type` become quorum queues.

```bash
rabbitmqctl add_vhost orders --default-queue-type quorum
rabbitmqctl update_vhost_metadata orders --default-queue-type quorum
```

You can also set `default_queue_type = quorum` in `rabbitmq.conf` for new vhosts. Exclusive queues are still created as classic queues, since quorum queues can't be exclusive. Note this only affects new queues; existing classic queues stay classic.

## 178: How do you declare a quorum queue and what are its options?

```js
await channel.assertQueue("payments", {
  durable: true, // must be true for quorum queues
  arguments: {
    "x-queue-type": "quorum",
    "x-quorum-initial-group-size": 3,
    "x-delivery-limit": 10,
    "x-dead-letter-exchange": "payments.dlx",
  },
});
```

Other useful settings (most better set with policies): `x-max-length`, `x-overflow` (`drop-head` or `reject-publish`), `x-message-ttl`, `x-single-active-consumer`, `x-dead-letter-strategy` (`at-most-once` or `at-least-once`) and `x-queue-leader-locator` (`client-local` or `balanced`).

## 179: How do you use a stream from an AMQP 0-9-1 client?

Declare it with `x-queue-type: stream`, set a prefetch, use manual acks, and pass `x-stream-offset` to choose where to start.

```js
await channel.assertQueue("events.stream", {
  durable: true,
  arguments: { "x-queue-type": "stream", "x-max-age": "7D" },
});

await channel.prefetch(100);
await channel.consume(
  "events.stream",
  (msg) => {
    handle(msg);
    channel.ack(msg); // required, but it only moves the credit window
  },
  { noAck: false, arguments: { "x-stream-offset": "first" } },
);
```

Acking doesn't delete anything from a stream. It just tells RabbitMQ the consumer can take more messages.

## 180: What offset options can you use when reading a stream?

- `first`: start from the oldest message still kept
- `last`: start from the last chunk of messages (a chunk is a group of messages, so you may get a few older ones)
- `next`: only messages published after you subscribe
- a number: start from this exact offset
- a timestamp (or an interval like `1h` in AMQP clients): start from messages published around that time

Since RabbitMQ 4.4 you can also set `x-stream-initial-offset` on the stream to control the default for consumers that don't pass an offset.

## 181: How do you control how long a stream keeps data?

With retention settings, based on size, age or both:

```js
await channel.assertQueue("clicks", {
  durable: true,
  arguments: {
    "x-queue-type": "stream",
    "x-max-length-bytes": 20_000_000_000, // 20 GB
    "x-max-age": "7D",
    "x-stream-max-segment-size-bytes": 100_000_000,
  },
});
```

Data is removed by whole segment files, not message by message, so the stream can be a bit bigger or older than the limit before the oldest segment is deleted. Retention can also be set with policies (`max-length-bytes`, `max-age`).

## 182: When should you choose a classic queue, a quorum queue or a stream?

- **Quorum queue:** the default for important messages that must survive node failures, like orders, payments and jobs. Each message is processed once and then removed.
- **Stream:** when many consumers need the same data, when you need to replay history, or when you need very high throughput with large backlogs.
- **Classic queue:** temporary or exclusive queues, RPC reply queues, data you can lose, or single-node setups where replication doesn't matter.

If you're not sure, use a quorum queue.

## 183: What doesn't a quorum queue support?

- Non-durable queues (quorum queues are always durable)
- Exclusive queues
- Global QoS (prefetch shared across the channel)
- `x-max-priority` (quorum queues have their own priority handling instead)
- `reject-publish-dlx` overflow
- Lazy mode (not needed, they keep messages on disk)

They do support TTL, length limits, dead lettering, single active consumer, priorities (since 4.0) and consumer timeouts. Check the feature matrix in the docs when moving an app from classic to quorum queues.

## 184: How many replicas should a quorum queue have?

The default is 3 replicas (or fewer if the cluster has fewer nodes), set with `x-quorum-initial-group-size` or the `quorum_queue.initial_cluster_size` config. Odd numbers are best: 3 replicas survive 1 node failure, 5 survive 2.

More replicas means more safety but slower publishes and more disk and network use, since each write goes to every replica and needs a majority to confirm. For most systems, a 3-node cluster with 3 replicas is the standard; use 5 for very critical data.

## 185: How do priorities work in quorum queues?

Since RabbitMQ 4.0, quorum queues support message priority without any extra queue argument. By default they use two levels: messages with priority 0 to 4 are "normal" and 5 or above are "high". High priority messages are delivered more often, but normal ones aren't starved completely.

```js
channel.sendToQueue("jobs", body, { priority: 9 }); // high
channel.sendToQueue("jobs", body, { priority: 1 }); // normal
```

RabbitMQ 4.3 added a strict priority option, where higher priority messages always go first. If you need many fine-grained levels, separate queues per priority with dedicated consumers is still a simple option.

## 186: What is a consumer timeout?

A consumer timeout makes RabbitMQ close a channel when a delivered message hasn't been acked for too long. The default is 30 minutes (`consumer_timeout = 1800000` in ms). The unacked messages are then returned to the queue.

It protects the queue from consumers that are stuck or forgot to ack. In RabbitMQ 4.3 and later, consumer timeouts apply to quorum queues (with more control, including per queue and per consumer settings) and no longer apply to classic queues and streams.

```ini
consumer_timeout = 3600000
```

## 187: How do you handle jobs that take longer than the consumer timeout?

Options:

- Raise the timeout for that queue or consumer (with a policy or argument) if the jobs really need it.
- Split long jobs into smaller steps, each a separate message.
- Ack early and track progress elsewhere: take the message, save a job record in a DB as "in progress", ack, and have a separate process retry jobs that stay stuck too long.
- Use a dedicated job system for very long tasks.

Don't just disable the timeout everywhere, because then a stuck consumer can hold messages forever.

## 188: What is the difference between per-message TTL and per-queue TTL behavior?

With per-queue TTL (`x-message-ttl`), all messages have the same TTL, so the oldest message always expires first and RabbitMQ can remove expired messages from the head efficiently.

With per-message TTL (`expiration`), each message has its own TTL. Classic queues only check expiration when a message reaches the head of the queue. So a message with a 1 minute TTL behind one with a 1 hour TTL won't be removed until the first one is gone. Expired messages are never delivered to consumers, but they still use space until removed.

This is why TTL-based delay queues usually have one queue per delay value.

## 189: Why is the delayed message exchange plugin not recommended anymore?

The `rabbitmq_delayed_message_exchange` plugin added an `x-delayed-message` exchange that held messages until an `x-delay` header expired. It had known limits: delayed messages were stored on one node only (not replicated), it didn't handle millions of delayed messages well, and messages could be lost if that node's data was lost.

The plugin is no longer maintained and doesn't support recent RabbitMQ versions. For new work, use TTL + DLX queues, the delayed delivery support added to quorum queues in 4.4, or an external scheduler.

## 190: How do you do RPC with direct reply-to?

Direct reply-to lets the client receive replies without declaring a reply queue. The client consumes from the pseudo-queue `amq.rabbitmq.reply-to` in auto-ack mode and sets `replyTo` to the same name. RabbitMQ replaces it with a unique name for that channel, and the server just replies to whatever `replyTo` says.

```js
const pending = new Map();

await channel.consume(
  "amq.rabbitmq.reply-to",
  (msg) => {
    const resolve = pending.get(msg.properties.correlationId);
    if (resolve) {
      pending.delete(msg.properties.correlationId);
      resolve(JSON.parse(msg.content.toString()));
    }
  },
  { noAck: true },
);

function call(queue, payload) {
  const correlationId = crypto.randomUUID();
  return new Promise((resolve) => {
    pending.set(correlationId, resolve);
    channel.sendToQueue(queue, Buffer.from(JSON.stringify(payload)), {
      replyTo: "amq.rabbitmq.reply-to",
      correlationId,
    });
  });
}
```

You must start consuming before you publish the request, on the same channel.

## 191: How do you handle timeouts in RPC over RabbitMQ?

The client should never wait forever. Start a timer for each request, reject the promise when it fires and remove the request from the pending map. If the reply shows up later, just ignore it.

```js
function callWithTimeout(queue, payload, ms = 5000) {
  return Promise.race([
    call(queue, payload),
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error("RPC timeout")), ms),
    ),
  ]);
}
```

Also set an `expiration` on the request message equal to the timeout, so servers don't waste time on requests nobody is waiting for anymore.

## 192: When should you use durable named queues vs temporary queues for pub/sub?

- **Durable named queue per service** (`billing.order-events`): messages are kept while the service is down or deploying, and all instances share the work. Use it when every event must be processed.
- **Exclusive server-named queue per instance**: each running instance gets its own copy of every event, and the queue disappears when the instance stops. Use it for things like local cache invalidation or pushing live updates to that instance's WebSocket clients, where missed events don't matter.

Mixing them up is a common bug: a temporary queue for billing events means lost events during deploys.

## 193: How do you send one event to several microservices?

Publish once to a topic (or fanout) exchange and let each service bind its own queue:

```js
// producer: orders service
channel.publish("orders.events", "order.created", body, { persistent: true });

// billing service
await ch.assertQueue("billing.order-created", {
  durable: true,
  arguments: { "x-queue-type": "quorum" },
});
await ch.bindQueue("billing.order-created", "orders.events", "order.created");

// shipping service
await ch.assertQueue("shipping.orders", {
  durable: true,
  arguments: { "x-queue-type": "quorum" },
});
await ch.bindQueue("shipping.orders", "orders.events", "order.*");
```

Each service processes, retries and fails independently. Adding a new consumer means adding a queue and binding, with no change to the producer.

## 194: What is the difference between commands and events in messaging?

- A **command** asks one specific service to do something: `send-email`, `charge-card`. It has one handler, and the sender expects it to be done. It's usually sent to a specific queue (or direct exchange).
- An **event** says something already happened: `order.created`, `payment.failed`. The publisher doesn't know or care who listens, and there can be zero or many handlers. It's published to a topic or fanout exchange.

Naming them clearly (imperative for commands, past tense for events) makes the system easier to understand.

## 195: How do you version message schemas?

- Put a version in a header (`schema-version: 2`) or in the event type (`order.created.v2`).
- Prefer backward-compatible changes: add optional fields, don't remove or rename fields that consumers use.
- Consumers should ignore fields they don't know.
- For breaking changes, publish both versions for a while (or use a new routing key), migrate consumers, then stop the old version.

Some teams use Avro, Protobuf or JSON Schema with a schema registry to check compatibility automatically.

## 196: How do you add tracing to messages?

Pass the trace context in message headers. With OpenTelemetry, the producer injects the current context (the `traceparent` header) when publishing, and the consumer extracts it and starts a child span.

```js
import { context, propagation } from "@opentelemetry/api";

const headers = {};
propagation.inject(context.active(), headers);
channel.publish("orders", "order.created", body, { headers });

// consumer
const parent = propagation.extract(
  context.active(),
  msg.properties.headers ?? {},
);
```

OpenTelemetry also has auto-instrumentation for amqplib that does this for you. It lets you follow one request from the HTTP API through the queue to the worker.

## 197: How do you use RabbitMQ with NestJS?

NestJS microservices have a built-in RMQ transport (`@nestjs/microservices` with `amqplib` and `amqp-connection-manager` installed):

```ts
// main.ts
const app = await NestFactory.createMicroservice<MicroserviceOptions>(
  AppModule,
  {
    transport: Transport.RMQ,
    options: {
      urls: ["amqp://localhost:5672"],
      queue: "orders",
      queueOptions: { durable: true },
      noAck: false,
      prefetchCount: 10,
    },
  },
);
```

```ts
@EventPattern('order_created')
async handle(@Payload() data: OrderDto, @Ctx() ctx: RmqContext) {
  await this.ordersService.process(data);
  ctx.getChannelRef().ack(ctx.getMessage());
}
```

The built-in transport is simple and uses one queue per service. For topic routing and more control, many teams use `@golevelup/nestjs-rabbitmq` or plain amqplib.

## 198: How do you test code that uses RabbitMQ?

- **Unit tests:** put publishing and consuming behind your own small interface and mock it, so business logic is tested without a broker.
- **Integration tests:** start a real RabbitMQ in Docker, for example with Testcontainers, declare the topology and check that messages flow end to end.

```js
import { RabbitMQContainer } from "@testcontainers/rabbitmq";

const container = await new RabbitMQContainer(
  "rabbitmq:4.4-management",
).start();
const connection = await amqp.connect(container.getAmqpUrl());
```

Test the failure paths too: nack, DLQ routing, redelivery, and what happens when the broker restarts.

## 199: How do you seed queues and exchanges for local development?

Load a definitions file when the container starts:

```yaml
services:
  rabbitmq:
    image: rabbitmq:4.4-management
    volumes:
      - ./rabbitmq/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf:ro
      - ./rabbitmq/definitions.json:/etc/rabbitmq/definitions.json:ro
```

```ini
# rabbitmq.conf
definitions.import_backend = local_filesystem
definitions.local.path = /etc/rabbitmq/definitions.json
```

Then every developer gets the same users, vhosts, exchanges, queues and policies with one `docker compose up`. If your apps declare their own topology, this matters less, but it's still useful for users and policies.

## 200: How do you set up health checks for RabbitMQ in Docker and Kubernetes?

Use `rabbitmq-diagnostics` commands, which are cheap and don't need the HTTP API:

```yaml
# Kubernetes
livenessProbe:
  exec:
    command: ["rabbitmq-diagnostics", "-q", "ping"]
  periodSeconds: 30
  timeoutSeconds: 20
readinessProbe:
  exec:
    command: ["rabbitmq-diagnostics", "-q", "check_port_connectivity"]
  periodSeconds: 10
```

Don't use heavy checks (like alarm checks or listing queues) in a liveness probe. If the node is under load and the check times out, Kubernetes will restart a node that was actually fine, which makes things worse. The Cluster Operator sets up suitable probes for you.

## 201: Which rabbitmq-diagnostics checks should you know?

- `ping`: is the node up
- `check_running`: is the RabbitMQ app running
- `check_local_alarms` / `check_alarms`: memory or disk alarms on this node / in the cluster
- `check_port_connectivity`: can listeners accept connections
- `check_virtual_hosts`: are all vhosts running
- `check_certificate_expiration`: TLS certs about to expire
- `check_if_node_is_quorum_critical`: would stopping this node make quorum queues lose their majority
- `check_protocol_listener`: a specific listener (like AMQP or MQTT) is on

They return a non-zero exit code on failure, so they work well in scripts.

## 202: What metrics should you monitor in RabbitMQ?

- **Queues:** messages ready, messages unacked, publish rate vs deliver/ack rate, number of consumers
- **Nodes:** memory used vs watermark, free disk vs limit, file descriptors, Erlang processes
- **Connections and channels:** totals, and how fast they're opened and closed (churn)
- **Alarms:** memory and disk alarms
- **Quorum queues:** leader distribution, Raft log size
- **Clients:** publisher confirms and returns, connection blocks

The main warning signs are queues that keep growing, queues with zero consumers, high churn and memory getting close to the watermark.

## 203: What metrics endpoints does the Prometheus plugin expose?

- `/metrics`: aggregated metrics for the whole node, cheap to scrape. This is the default for dashboards.
- `/metrics/per-object`: metrics for every queue, connection and channel. Can be very large with many objects.
- `/metrics/detailed`: lets you choose which metric groups and vhosts you want, with query parameters like `family` and `vhost`.

```bash
curl 'http://localhost:15692/metrics/detailed?family=queue_coarse_metrics&vhost=shop'
```

On big clusters, use the aggregated endpoint plus `detailed` for the few queues you care about, instead of scraping everything per object.

## 204: What can you see in the management UI?

- **Overview:** message rates, totals, node health, alarms, ports
- **Connections:** client name, user, state (running, blocked, flow), TLS, client properties
- **Channels:** prefetch, unacked messages, confirm mode
- **Exchanges:** bindings, message rates, publish a test message
- **Queues and Streams:** type, messages, consumers, policies applied, get or purge messages, move messages (with Shovel)
- **Admin:** users, vhosts, policies, limits, feature flags, cluster

It's great for daily debugging but not a replacement for proper monitoring, since its metrics are short-term.

## 205: A message is published but never reaches the consumer. How do you debug it?

Check step by step:

1. Does the exchange exist and is the publisher using the right name and vhost?
2. Do bindings match the routing key? Check in the UI or `rabbitmqctl list_bindings`.
3. Publish with `mandatory: true` or set an alternate exchange to catch unroutable messages.
4. Did the message reach the queue? Look at its message count and incoming rate.
5. Is a consumer attached to that queue, and is it the queue you think it is?
6. Is the consumer stuck (unacked count high) or blocked by prefetch?
7. Did the message expire (TTL) or get dead-lettered? Check the DLQ.
8. Is the publisher blocked by an alarm?

The firehose tracer can show every publish and delivery on a vhost if you still can't find it.

## 206: A queue keeps growing. What do you check?

Compare the publish rate with the ack rate:

- **No consumers:** a service is down or crashed. Restart or fix it.
- **Consumers exist but are slow:** check what they wait on (DB, external API). Scale them out, raise prefetch for fast handlers, or optimize the handler.
- **Lots of unacked messages:** consumers are stuck or have a bug where some code paths never ack.
- **Lots of redeliveries:** messages fail and are requeued in a loop; look for a poison message.
- **Sudden publish spike:** maybe a bug in a producer, or a replay.

Also set a length limit and alerts, so a growing queue doesn't take the whole broker down with a memory or disk alarm.

## 207: What is the firehose tracer?

The firehose sends a copy of every message published or delivered in a vhost to the `amq.rabbitmq.trace` exchange, with routing keys like `publish.<exchange>` and `deliver.<queue>`. You bind a queue to it to see what's going on.

```bash
rabbitmqctl trace_on -p shop
# bind a queue to amq.rabbitmq.trace with key "#"
rabbitmqctl trace_off -p shop
```

It adds a lot of load, so only turn it on for a short time while debugging, never leave it on in production.

## 208: What is the rabbitmq_tracing plugin?

It's a management UI add-on built on top of the firehose. You can create a trace from the UI with a pattern (like `publish.orders` or `#`), and it writes the traced messages to a log file you can open in the browser.

```bash
rabbitmq-plugins enable rabbitmq_tracing
```

Like the firehose, it's for short debugging sessions only. The trace files can grow quickly, and tracing slows the broker down.

## 209: How do you look at messages in a queue without losing them?

In the management UI, open the queue and use "Get messages" with ack mode "Nack message requeue true". The messages are shown and put back.

```bash
rabbitmqadmin get messages --queue orders.dlq --count 5 --ack-mode ack_requeue_true
```

Requeueing changes the `redelivered` flag and, for quorum queues, counts as a delivery attempt. For streams it's easier, since reading never removes anything. Don't use this on large busy queues as a monitoring tool.

## 210: How do you move messages from one queue to another?

Use a shovel. In the management UI, with `rabbitmq_shovel_management` enabled, the queue page has a "Move messages" section that creates a temporary shovel. From the CLI:

```bash
rabbitmqctl set_parameter shovel move-dlq \
'{"src-protocol":"amqp091","src-uri":"amqp://","src-queue":"orders.dlq",
  "dest-protocol":"amqp091","dest-uri":"amqp://","dest-queue":"orders",
  "src-delete-after":"queue-length"}'
```

`src-delete-after: queue-length` makes the shovel move only the messages that were there when it started, and then delete itself. This is the standard way to replay a DLQ after fixing a bug.

## 211: What is the difference between a static and a dynamic shovel?

- **Static shovels** are defined in `advanced.config`. They start with the node and changing them requires a restart. They're rarely used now.
- **Dynamic shovels** are created at runtime as runtime parameters, with `rabbitmqctl set_parameter shovel ...`, the HTTP API or the management UI. They're stored in the cluster metadata, survive restarts and can be added and deleted without restarts.

Dynamic shovels are the normal choice today.

## 212: What is the difference between federated exchanges and federated queues?

- **Federated exchange:** messages published to the upstream exchange are copied to the downstream exchange, as if they were published there too. Every downstream gets a copy. Good for spreading events to several regions.
- **Federated queue:** the downstream queue pulls messages from the upstream queue only when its local consumers have nothing to do. Each message is still consumed once overall. Good for spreading work load across sites.

Both use normal AMQP connections and tolerate slow or unreliable WAN links.

## 213: When do you use Shovel and when Federation?

- **Shovel** is a low-level "move from A to B" tool. You set the exact source and destination. Good for one-off migrations, replaying DLQs, linking two specific queues between clusters or bridging protocols.
- **Federation** is higher level and manages links for you based on policies. Good for keeping exchanges in sync across clusters or spreading work across sites over time.

If you're moving messages once, use a shovel. If you're building a long-running multi-cluster topology, look at federation.

## 214: Why should you give connections a name?

By default the management UI shows connections only by IP and port, which makes it hard to know which app or pod they belong to. You can set a `connection_name` client property, and RabbitMQ shows it in the UI and CLI.

```js
const connection = await amqp.connect(process.env.AMQP_URL, {
  clientProperties: { connection_name: `orders-api-${process.env.HOSTNAME}` },
});
```

It makes debugging much faster: you can see right away which service has too many channels or a blocked connection.

## 215: What is connection churn and why is it bad?

Connection churn means connections are opened and closed very often, like a new connection for every HTTP request or every published message. Each connection costs a TCP handshake, maybe TLS, authentication and broker resources, so high churn wastes CPU and can make the node slow or unstable.

You can see it in the management UI and Prometheus as connections created/closed per second. The fix is long-lived connections shared within a process (and if a language needs it, a connection pool). The same goes for channels: reuse them instead of opening one per publish.

## 216: What is a channel leak?

A channel leak is when an app opens channels and never closes them, for example creating a new channel in each request handler. The number of channels on one connection keeps growing until it hits `channel_max` (2047 by default) or uses too much memory.

You can spot it in the UI (Channels count per connection keeps rising). Fix it by creating channels once at startup and reusing them, or closing them in a `finally` block if they really must be short-lived.

## 217: How many connections and channels should an application open?

A common setup is:

- One connection for publishing and one for consuming per process
- One channel per thread or per independent worker, created once and reused
- For publishing, one or a few channels shared through the app, since amqplib channels are fine to use from many places in single-threaded Node.js

Hundreds of connections per app, or a new channel per message, is a sign of a problem. On the broker side, each connection uses a few hundred KB of memory, so with many apps it adds up.

## 218: Why use separate connections for publishing and consuming?

When RabbitMQ raises a memory or disk alarm, or applies flow control, it blocks or slows down connections that publish. If your consumer uses the same connection, its acks and deliveries are also stuck behind the blocked socket.

This creates a bad loop: consumers can't ack, so queues can't drain, so memory stays high, so the alarm never clears. With separate connections, consumers keep working while publishers are blocked.

## 219: What is flow control in RabbitMQ?

Flow control is how RabbitMQ slows down publishers that send faster than the broker can handle. Internally it uses credit between Erlang processes: if a queue or the disk can't keep up, the channel and connection stop getting credit and RabbitMQ stops reading from that publisher's socket for a short time.

In the management UI the connection shows state `flow`. It's normal for short periods. If connections are in `flow` all the time, the broker or one queue is a bottleneck, and you should look at the queue's consumers, disk I/O or spread the load across more queues.

## 220: How can a client know it is blocked by the broker?

RabbitMQ sends `connection.blocked` (with a reason, like low memory) and later `connection.unblocked` to clients that support it. Most clients advertise support automatically.

```js
connection.on("blocked", (reason) => {
  metrics.increment("amqp.blocked");
  logger.warn({ reason }, "publishing blocked");
});
connection.on("unblocked", () => logger.info("publishing unblocked"));
```

The app can then stop accepting new work, return 503s or buffer, instead of piling up hanging publishes.

## 221: How do you configure the memory watermark?

```ini
# relative to total RAM (default 0.6)
vm_memory_high_watermark.relative = 0.6

# or an absolute value
vm_memory_high_watermark.absolute = 4GiB
```

In containers, RabbitMQ needs to know the container's memory limit, not the host's RAM. Recent versions read the cgroup limit, but setting `total_memory_available_override_value` or an absolute watermark makes it explicit. The watermark is not a hard limit; the node can briefly go above it, so leave headroom.

## 222: How should you set the disk free limit?

The default (50 MB) is only good for development. For production, set it relative to RAM or to a fixed value that gives time to react:

```ini
disk_free_limit.relative = 1.5
# or
disk_free_limit.absolute = 10GB
```

`relative = 1.5` means 1.5 times the total RAM. Quorum queues and streams write a lot to disk, so also leave room for their logs and segments. Monitor free disk and alert well before the limit.

## 223: How do heartbeats interact with load balancers and firewalls?

Many load balancers and firewalls close TCP connections that are idle for a while (for example 350 seconds on AWS NLB, or less on some corporate firewalls). If the heartbeat interval is longer than that, an idle connection is cut silently, and the client only notices on the next publish.

Set the heartbeat lower than the idle timeout of anything in between, typically 30 to 60 seconds. Also raise the load balancer's idle timeout if you can. Heartbeats below 5 seconds cause false positives under load.

## 224: How do you authenticate clients with TLS certificates?

Enable the `rabbitmq_auth_mechanism_ssl` plugin and configure TLS to require client certificates. The client then logs in with the `EXTERNAL` mechanism, and RabbitMQ takes the username from the certificate (by default the subject's distinguished name, or the CN if configured).

```ini
auth_mechanisms.1 = EXTERNAL
ssl_options.verify = verify_peer
ssl_options.fail_if_no_peer_cert = true
ssl_cert_login_from = common_name
```

The user must still exist in RabbitMQ (with any password) and have permissions. This avoids storing passwords in apps, but you need a way to issue and rotate certificates.

## 225: How do you use LDAP with RabbitMQ?

Enable `rabbitmq_auth_backend_ldap` and configure the backends and LDAP server:

```ini
auth_backends.1 = ldap
auth_backends.2 = internal
auth_ldap.servers.1 = ldap.example.com
auth_ldap.user_dn_pattern = cn=${username},ou=People,dc=example,dc=com
auth_ldap.use_ssl = true
```

RabbitMQ checks the login against LDAP. Authorization (vhost access, permissions, tags) can also be based on LDAP group membership, which needs queries in `advanced.config`. Keeping `internal` as a second backend lets you still log in with a local admin if LDAP is down.

## 226: How does OAuth 2.0 authentication work in RabbitMQ?

With the `rabbitmq_auth_backend_oauth2` plugin, clients send a JWT access token as the password (the username can be anything or empty). RabbitMQ checks the token's signature with the identity provider's keys, then reads permissions from the token's scopes.

```ini
auth_backends.1 = oauth2
auth_oauth2.resource_server_id = rabbitmq
auth_oauth2.issuer = https://login.example.com/realms/prod
```

Scopes look like `rabbitmq.read:shop/orders*` or `rabbitmq.tag:monitoring`. The management UI can also log in through the identity provider (Keycloak, Entra ID, Auth0, Okta and so on). When a token expires, the client has to refresh it, and AMQP 0-9-1 clients can update the token on an open connection.

## 227: How do you secure a fresh RabbitMQ installation?

- Delete the `guest` user or at least change its password.
- Create one user per app with only the permissions it needs.
- Turn on TLS for client connections, and for inter-node traffic if the network isn't trusted.
- Don't expose ports 15672, 25672 and 4369 to the internet. Keep the management UI behind a VPN or internal network.
- Protect the Erlang cookie file.
- Set vhost and user limits, a sensible `max_message_size` and disk/memory alarms.
- Keep RabbitMQ and Erlang up to date.

## 228: How do you write permission regexes for a least-privilege setup?

Give each app only what it uses. Examples for vhost `shop`:

```bash
# publisher: can only publish to the orders exchange
rabbitmqctl set_permissions -p shop orders_api '^$' '^orders$' '^$'

# consumer: owns queues starting with "billing.", reads them, binds to orders
rabbitmqctl set_permissions -p shop billing '^billing\..*' '^billing\..*' '^(billing\..*|orders)$'
```

Remember the regexes are matched against full resource names, so anchor them with `^` and `$`. Binding a queue to an exchange needs write on the queue and read on the exchange. Server-named queues start with `amq.gen-`, so a consumer using them needs configure on that prefix.

## 229: What are topic permissions?

Topic permissions restrict which routing keys a user can publish (write) or bind/consume with (read) on topic exchanges. They're checked in addition to the normal permissions.

```bash
rabbitmqctl set_topic_permissions -p shop tenant_acme amq.topic '^acme\..*' '^acme\..*'
```

They're mostly used with MQTT (where topics map to routing keys on `amq.topic`) or in multi-tenant setups where users share one exchange but should only see their own keys. You can use variables like `{username}` and `{vhost}` in the patterns.

## 230: How should apps get their RabbitMQ credentials?

Don't hardcode them in code or commit them to Git. Common options:

- Environment variables injected at deploy time from a secrets store
- Kubernetes Secrets, ideally synced from Vault or a cloud secrets manager
- Short-lived credentials from HashiCorp Vault's RabbitMQ secrets engine
- OAuth 2 tokens or client certificates instead of passwords

Use different credentials per service and environment, so you can revoke one without touching others, and so you can see in the UI which service owns a connection.

## 231: How do you form a cluster manually?

All nodes need the same Erlang cookie and must be able to resolve each other's hostnames. Then, on each new node:

```bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@node1
rabbitmqctl start_app
rabbitmqctl cluster_status
```

Joining resets the node, so any data on it is lost. In real deployments, peer discovery or the Kubernetes operator usually does this automatically.

## 232: What is peer discovery?

Peer discovery lets nodes find each other and form a cluster automatically on first start, instead of running `join_cluster` by hand. Supported backends include:

- a fixed list of nodes in config (`classic_config`)
- DNS (A/AAAA records)
- Kubernetes
- AWS (by tags or auto scaling group)
- Consul and etcd

```ini
cluster_formation.peer_discovery_backend = classic_config
cluster_formation.classic_config.nodes.1 = rabbit@rmq-0
cluster_formation.classic_config.nodes.2 = rabbit@rmq-1
cluster_formation.classic_config.nodes.3 = rabbit@rmq-2
```

Peer discovery only runs when a node starts with an empty data directory. A node that was already in a cluster rejoins it on restart.

## 233: Why do node names and hostnames matter?

Each node is named `rabbit@<hostname>`, and its data directory is tied to that name. If the hostname changes (for example a new container gets a random hostname), the node starts as a brand new node with empty data, and the old data looks like it's gone.

That's why in Docker you set a fixed `hostname`, and in Kubernetes RabbitMQ runs as a StatefulSet with stable pod names and a headless service. CLI tools also need to resolve the hostname to reach the node.

## 234: Should you put a load balancer in front of a RabbitMQ cluster?

It's common and fine for AMQP. A TCP load balancer (like HAProxy, an AWS NLB or a Kubernetes Service) gives clients one address and spreads connections across nodes.

Things to keep in mind:

- Use TCP (layer 4) mode, not HTTP.
- Set idle timeouts higher than the heartbeat interval.
- Clients are spread by connection, not by message, so long-lived connections can be unbalanced after a node restart.
- Stream protocol clients need direct access to nodes (they connect to the node hosting the leader or replica), so plain load balancing doesn't work well for them without extra config.

## 235: How can a client connect to a cluster without a load balancer?

Give the client a list of node addresses and let it try them in order (or shuffled) until one works. Many clients support this directly; with amqplib you do it yourself:

```js
const urls = [
  "amqp://app:pass@rmq-0:5672",
  "amqp://app:pass@rmq-1:5672",
  "amqp://app:pass@rmq-2:5672",
];

async function connectAny() {
  for (const url of urls.sort(() => Math.random() - 0.5)) {
    try {
      return await amqp.connect(url);
    } catch (err) {
      console.warn("Failed", url, err.message);
    }
  }
  throw new Error("No RabbitMQ node available");
}
```

## 236: What happens to clients when a cluster node goes down?

Clients connected to that node lose their connections and must reconnect to another node. Unacked messages from their consumers are returned to the queues.

What happens to the queues depends on their type:

- **Quorum queues and streams** with replicas on other nodes elect a new leader and keep working.
- **Classic queues** on that node are unavailable until it comes back. Durable ones keep their persistent messages; transient ones are lost.

Clients connected to other nodes are not disconnected, though consumers of affected quorum queues may see a short pause during leader election.

## 237: What decides where a quorum queue's leader is placed?

The `x-queue-leader-locator` argument, the `queue-leader-locator` policy key, or the `queue_leader_locator` config setting:

- `client-local` (default): the leader goes on the node the declaring client is connected to.
- `balanced`: the leader goes on the node with the fewest leaders (for large numbers of queues it picks randomly for speed).

With `client-local` and a load balancer that sends all apps to one node at startup, most leaders end up on one node, making it a hotspot. `balanced` avoids that.

## 238: How do you rebalance quorum queue leaders?

After a node restart, all leaders may have moved to the remaining nodes. To spread them out again:

```bash
rabbitmq-queues rebalance quorum
rabbitmq-queues rebalance all --vhost-pattern '^shop$'
```

This moves leadership (not data) so each node has about the same number of leaders. Since 4.2, leader transfers at scale are done gradually to avoid load spikes. You can run it after maintenance or let the Kubernetes operator handle it.

## 239: How do you add or remove replicas of a quorum queue?

Use `rabbitmq-queues`:

```bash
# add a replica of one queue on a node
rabbitmq-queues add_member -p shop orders rabbit@node4

# remove a replica
rabbitmq-queues delete_member -p shop orders rabbit@node2

# add replicas on a new node for all matching queues
rabbitmq-queues grow rabbit@node4 all --vhost-pattern '.*' --queue-pattern '.*'

# remove all replicas from a node (before decommissioning it)
rabbitmq-queues shrink rabbit@node2
```

Quorum queues don't move replicas automatically when nodes join, so after adding a node you have to grow the queues onto it.

## 240: How do you do a rolling upgrade of a cluster?

Upgrade one node at a time:

1. Read the release notes and check the upgrade path (usually only from the previous minor series).
2. Enable all stable feature flags on the current version.
3. Check that stopping this node is safe: `rabbitmq-diagnostics check_if_node_is_quorum_critical`.
4. Put the node into maintenance mode: `rabbitmq-upgrade drain`.
5. Stop it, upgrade RabbitMQ (and Erlang if needed), start it.
6. Wait until it's back and synced: `rabbitmq-upgrade await_online_quorum_plus_one`.
7. Repeat for the next node.
8. When all nodes are upgraded, enable the new feature flags.

Don't run a mixed-version cluster for more than a few hours.

## 241: What is a blue-green deployment for RabbitMQ?

You build a new cluster ("green") next to the old one ("blue"), copy definitions over, move consumers and publishers to green, and use shovels or federation to drain the messages left in blue. When blue is empty, you shut it down.

It's used when a rolling upgrade isn't possible, for example jumping several versions, moving from 3.13 to 4.x when you still use features that were removed, or switching hardware, region or queue types. `rabbitmqadmin` v2 (since 4.2) has commands to help with this migration.

## 242: How do you back up RabbitMQ?

- **Definitions:** export them regularly (`rabbitmqctl export_definitions`). This is cheap and covers users, vhosts, queues, exchanges, bindings and policies.
- **Messages:** there's no simple online backup. You can copy the data directory only while the node is stopped, and restoring it needs the same node name.

In practice, most teams rely on replication (quorum queues and streams) for message safety, and on definitions exports to rebuild topology. Messages in a broker are usually short-lived, so if you need long-term history, store it in a database or a stream with long retention.

## 243: How do you define a production-ready RabbitmqCluster in Kubernetes?

```yaml
apiVersion: rabbitmq.com/v1beta1
kind: RabbitmqCluster
metadata:
  name: rabbit
spec:
  replicas: 3
  image: rabbitmq:4.4-management
  resources:
    requests: { cpu: "2", memory: 4Gi }
    limits: { cpu: "2", memory: 4Gi }
  persistence:
    storageClassName: fast-ssd
    storage: 100Gi
  rabbitmq:
    additionalPlugins: [rabbitmq_shovel, rabbitmq_shovel_management]
    additionalConfig: |
      default_queue_type = quorum
      disk_free_limit.absolute = 10GB
  tls:
    secretName: rabbit-tls
```

The operator creates a StatefulSet, services, a default user secret and the config. It also sets up anti-affinity options and safe rolling updates.

## 244: What is the Messaging Topology Operator?

It's a Kubernetes operator that manages RabbitMQ objects as custom resources: `Queue`, `Exchange`, `Binding`, `User`, `Permission`, `Policy`, `Vhost`, `Shovel`, `Federation` and more.

```yaml
apiVersion: rabbitmq.com/v1beta1
kind: Queue
metadata:
  name: orders
spec:
  name: orders
  type: quorum
  durable: true
  vhost: shop
  rabbitmqClusterReference:
    name: rabbit
```

This lets you keep topology in Git and deploy it with the same tools as the rest of your app (Helm, Argo CD and so on).

## 245: How do you keep ordering per entity while still using several consumers?

You usually don't need global order, only order per order ID, per user or per account. Split messages into several queues by that key, and give each queue one active consumer.

- Use a consistent hash or `x-modulus-hash` exchange that routes by a hash of the routing key (the entity ID), bound to N queues.
- Put single active consumer on each queue.
- Or use a super stream with single active consumer per partition.

All messages for one entity land in the same queue and are processed in order, while different entities are processed in parallel.

## 246: What is the consistent hash exchange?

It's an exchange type from the `rabbitmq_consistent_hash_exchange` plugin (shipped with RabbitMQ). It hashes the routing key (or a header or property) and picks one of the bound queues. The binding key is a number that sets the queue's weight.

```js
await channel.assertExchange("orders.sharded", "x-consistent-hash", {
  durable: true,
});
for (let i = 0; i < 4; i++) {
  await channel.assertQueue(`orders.shard.${i}`, { durable: true });
  await channel.bindQueue(`orders.shard.${i}`, "orders.sharded", "1"); // weight 1
}
channel.publish("orders.sharded", `order-${orderId}`, body);
```

The same routing key always goes to the same queue (as long as the bindings don't change), which is useful for per-key ordering and spreading load.

## 247: What is the x-modulus-hash exchange?

`x-modulus-hash` routes each message to one bound queue, chosen by hashing the routing key and taking the result modulo the number of bound queues. It came from the sharding plugin and moved into the core in RabbitMQ 4.3.

It's simpler than the consistent hash exchange (no weights), and since 4.4 the routing is stable as long as the topology doesn't change. But adding or removing a queue changes where most keys go, while consistent hashing moves fewer keys.

## 248: What is a super stream?

A super stream is a logical stream made of several normal streams (partitions). Publishers pick a partition based on a routing key (by hash or by exact key), and consumers can read all partitions or join a group where each partition is read by one consumer.

```bash
rabbitmq-streams add_super_stream orders --partitions 3
```

It's the RabbitMQ version of Kafka topics with partitions: you get more throughput than one stream, and order is kept per partition (so per key).

## 249: How does single active consumer work with streams?

With streams, single active consumer is set per consumer by name (a consumer reference), not on the queue. All consumers with the same name form a group, only one reads at a time, and if it fails another one takes over from the last stored offset.

Combined with super streams, each partition has its own active consumer, so the group spreads partitions across instances, similar to a Kafka consumer group. This needs the stream protocol client libraries.

## 250: What is stream filtering?

Stream filtering lets a consumer receive only some messages from a stream without reading everything over the network. Publishers attach a filter value to each message, and the broker uses a Bloom filter per chunk to skip chunks that don't contain the wanted values.

```js
// AMQP 0-9-1: publisher sets a filter value
channel.sendToQueue("events.stream", body, {
  headers: { "x-stream-filter-value": "eu" },
});

// consumer asks for it
await channel.consume("events.stream", onMsg, {
  arguments: { "x-stream-filter": "eu", "x-stream-offset": "first" },
});
```

Because the Bloom filter can have false positives, the consumer may still get some other messages and should check the value itself. Over AMQP 1.0, RabbitMQ 4.1 added property filters and 4.2 added SQL filter expressions that are evaluated exactly on the broker.

## 251: How do stream consumers remember where they stopped?

With the stream protocol, a consumer can store its offset on the broker under a consumer name, then read it back on restart and continue from there. Client libraries can do this automatically every N messages or on demand.

Over AMQP 0-9-1 there's no server-side offset tracking, so you store the last processed offset yourself (it's in `msg.properties.headers['x-stream-offset']`) in a database and pass it as `x-stream-offset` when subscribing.

```js
const offset = msg.properties.headers["x-stream-offset"];
await saveOffset("report-builder", offset);
```

## 252: Should you use the stream protocol or AMQP to work with streams?

The stream protocol gives the best performance (often several times faster) and supports features like server-side offset tracking, publisher de-duplication, super streams and single active consumer for streams. It needs a dedicated client and port 5552 to be reachable on each node.

AMQP 0-9-1 or 1.0 is easier when you already use those clients, need moderate throughput or want to mix queues and streams in one app. AMQP 1.0 also gets the SQL filter feature. Start with whichever your team already uses, and switch to the stream protocol if throughput becomes a problem.

## 253: Are some exchange types faster than others?

Yes, though for most apps the difference doesn't matter.

- **fanout** and **direct** are the fastest, since routing is a simple lookup.
- **topic** has to match patterns. It uses an efficient trie, but many bindings with wildcards cost more.
- **headers** is usually the slowest, since it compares header tables.

Don't pick an exchange type for speed alone; pick the one that expresses your routing. If routing becomes a bottleneck, it's usually because of a huge number of bindings, not the exchange type.

## 254: How do you send large payloads like files through RabbitMQ?

Use the claim check pattern: upload the file to object storage (S3, GCS, Azure Blob) and publish a small message with the reference.

```js
const key = `uploads/${crypto.randomUUID()}.pdf`;
await s3.send(new PutObjectCommand({ Bucket: "docs", Key: key, Body: file }));

channel.publish(
  "docs",
  "document.uploaded",
  Buffer.from(JSON.stringify({ bucket: "docs", key })),
  {
    persistent: true,
  },
);
```

The consumer downloads the file when it needs it. This keeps messages small, keeps the broker fast and lets you use storage made for large files. Plan for cleanup of files that are no longer needed.

## 255: Should you compress message bodies?

It can help when messages are large (tens of KB or more) and compress well, like JSON or text. It lowers network and disk use, especially with quorum queues that replicate every message. For small messages, the CPU cost isn't worth it.

```js
import { gzipSync, gunzipSync } from "node:zlib";

channel.publish("logs", "app", gzipSync(Buffer.from(json)), {
  contentType: "application/json",
  contentEncoding: "gzip",
});

// consumer
const body =
  msg.properties.contentEncoding === "gzip"
    ? gunzipSync(msg.content)
    : msg.content;
```

## 256: How do you publish many messages quickly and still be safe?

Don't wait for a confirm after every message; that limits you to one message per round trip. Instead publish a batch, then wait for all confirms:

```js
const channel = await connection.createConfirmChannel();

for (const event of events) {
  const ok = channel.publish(
    "events",
    event.type,
    Buffer.from(JSON.stringify(event)),
    { persistent: true },
  );
  if (!ok) await new Promise((r) => channel.once("drain", r));
}
await channel.waitForConfirms(); // throws if any message was nacked
```

Or track confirms with callbacks and keep a limited number of unconfirmed messages "in flight" (for example 1000). If the batch fails, republish the unconfirmed messages.

## 257: How do you process messages concurrently in a Node.js consumer?

Node.js is single-threaded, but handlers usually wait on I/O, so you can process several messages at once. amqplib calls your callback for each delivery without waiting for the previous one to finish, so prefetch controls how many run at the same time.

```js
await channel.prefetch(20); // up to 20 messages in progress

await channel.consume("thumbnails", async (msg) => {
  try {
    await makeThumbnail(JSON.parse(msg.content.toString()));
    channel.ack(msg);
  } catch (err) {
    channel.nack(msg, false, false);
  }
});
```

For CPU-heavy work, use worker threads or several processes; otherwise one slow handler blocks the event loop and heartbeats can fail.

## 258: How do you shut down a consumer gracefully?

1. Stop taking new messages: cancel the consumer.
2. Wait for in-progress messages to finish and ack them.
3. Close the channel and connection.

```js
let inFlight = 0;
const { consumerTag } = await channel.consume("jobs", async (msg) => {
  inFlight++;
  try {
    await handle(msg);
    channel.ack(msg);
  } finally {
    inFlight--;
  }
});

process.on("SIGTERM", async () => {
  await channel.cancel(consumerTag);
  while (inFlight > 0) await new Promise((r) => setTimeout(r, 100));
  await channel.close();
  await connection.close();
  process.exit(0);
});
```

Make sure the Kubernetes `terminationGracePeriodSeconds` is long enough for your slowest job.

## 259: How do you shut down a publisher without losing messages?

Stop accepting new work (for example stop the HTTP server), then wait for all outstanding publisher confirms before closing:

```js
process.on("SIGTERM", async () => {
  await new Promise((r) => server.close(r));
  await confirmChannel.waitForConfirms();
  await confirmChannel.close();
  await connection.close();
  process.exit(0);
});
```

If you close the connection while messages are still waiting for confirms, you can't know if they reached the broker.

## 260: What is the transactional outbox pattern and why is it used with RabbitMQ?

The problem: a service saves to its database and publishes an event. If it saves and then crashes before publishing, the event is lost. If it publishes first and the DB write fails, the event is wrong. You can't have one transaction across the DB and RabbitMQ.

The outbox pattern: in the same DB transaction, write the business change and a row in an `outbox` table. A separate process reads unsent outbox rows, publishes them with publisher confirms, and marks them as sent.

```sql
BEGIN;
INSERT INTO orders (id, total) VALUES (42, 99.50);
INSERT INTO outbox (id, routing_key, payload) VALUES (gen_random_uuid(), 'order.created', '{"id":42}');
COMMIT;
```

The event is published at least once, so consumers must still handle duplicates.

## 261: Does RabbitMQ support transactions, and should you use them?

AMQP 0-9-1 has channel transactions (`tx.select`, `tx.commit`, `tx.rollback`). They group publishes and acks on a channel, so they're applied together.

They're rarely used because they're slow (each commit is a synchronous round trip and sync to disk) and they only cover RabbitMQ, not your database. Publisher confirms give the same safety for publishing with much better throughput. Use confirms and the outbox pattern instead.

## 262: What does a publisher confirm mean for a message that couldn't be routed?

If a message isn't routed to any queue, the broker confirms it (ack) right away, because there was nothing to store. If it was published with `mandatory: true`, the `basic.return` is sent before the ack.

So "confirmed" doesn't mean "delivered to a queue". To catch these cases, use `mandatory` and handle returns, or use an alternate exchange. For routed messages, the ack comes once all target queues have accepted the message.

## 263: When does a broker send a nack for a published message?

A nack means the broker couldn't take responsibility for the message. It happens in a few cases:

- The queue has `x-overflow: reject-publish` and is full.
- A quorum queue couldn't accept it, for example it doesn't have a majority of replicas online.
- An internal error in the queue process.

The publisher should treat a nack as "not stored" and decide what to do: retry later, slow down, or report an error. Not handling nacks is like not using confirms at all.

## 264: How do you track publisher confirms asynchronously?

Each published message on a confirm channel gets a sequence number. The broker confirms by sequence number, sometimes many at once (`multiple`). amqplib hides this and calls the callback you pass to `publish` for each message.

```js
let inFlight = 0;
const MAX_IN_FLIGHT = 1000;

async function publish(ch, ex, key, body) {
  while (inFlight >= MAX_IN_FLIGHT) await new Promise((r) => setTimeout(r, 5));
  inFlight++;
  ch.publish(ex, key, body, { persistent: true }, (err) => {
    inFlight--;
    if (err) retryLater(ex, key, body);
  });
}
```

This keeps throughput high (many messages in flight) and memory bounded (a limit on how many are unconfirmed).

## 265: What happens to an exclusive queue if its node goes down?

Exclusive queues are classic queues tied to one connection. If the node hosting the queue (and so the connection) goes down, the connection is gone and the queue is deleted. Its messages are lost.

When the client reconnects to another node, it declares a new exclusive queue, usually with a new server-generated name, and must rebind it. That's fine for temporary things like reply queues, but it's a reason never to keep important data in exclusive queues.

## 266: What are the pitfalls of auto-delete queues?

- An auto-delete queue that never had a consumer isn't deleted, so it can stay forever.
- If the only consumer briefly disconnects (deploy, network blip), the queue and its messages are deleted, and messages published in between are lost.
- With several consumers, it's deleted only when the last one leaves, which can be hard to predict.

For "temporary but survive short disconnects", use a normal queue with `x-expires`, so it's removed only after it's been unused for a while.

## 267: How do you send real-time notifications to users connected to different API instances?

A common setup: each API instance declares an exclusive server-named queue bound to a `notifications` exchange. When an event arrives, the instance pushes it to its local WebSocket or SSE clients.

```js
const { queue } = await channel.assertQueue("", { exclusive: true });
await channel.bindQueue(queue, "notifications", `user.#`);

await channel.consume(queue, (msg) => {
  const { userId, payload } = JSON.parse(msg.content.toString());
  for (const socket of socketsByUser.get(userId) ?? [])
    socket.send(JSON.stringify(payload));
  channel.ack(msg);
});
```

Each instance gets every notification and drops the ones for users it doesn't hold. With many instances, you can bind more selectively (for example by routing key per user when a user connects) instead of receiving everything.

## 268: How do MQTT QoS levels map to RabbitMQ?

- **QoS 0 (at most once):** messages are sent without acks, and RabbitMQ can store them as transient.
- **QoS 1 (at least once):** messages are persisted and acknowledged; subscriptions use durable queues if the session isn't clean.
- **QoS 2 (exactly once):** RabbitMQ doesn't support it and downgrades QoS 2 subscriptions to QoS 1.

MQTT sessions map to queues. Since 3.12, clean sessions that subscribe with QoS 0 can use a special MQTT QoS 0 queue type, which is very cheap in memory.

## 269: What addresses do AMQP 1.0 clients use with RabbitMQ?

In RabbitMQ 4.x, AMQP 1.0 uses "address format v2", which maps clearly to RabbitMQ objects:

- `/exchanges/orders/order.created`: publish to exchange `orders` with routing key `order.created`
- `/exchanges/orders`: publish to `orders`, routing key taken from the message's subject
- `/queues/invoices`: publish to or consume from queue `invoices`

Names must be percent-encoded. The older v1 address format (like `/amq/queue/name` or `/topic/name`) is deprecated and denied by default since 4.3.

## 270: What are the new RabbitMQ AMQP 1.0 client libraries?

Along with native AMQP 1.0 in 4.0, the RabbitMQ team released AMQP 1.0 client libraries for several languages, including Java, .NET, Go, Python and JavaScript. Besides sending and receiving, they can manage topology (declare queues, exchanges and bindings) through an HTTP-over-AMQP management API.

They also support features specific to RabbitMQ 4.x over AMQP 1.0, like stream filters, consumer settlement modes and direct reply-to (added in 4.2). For new projects, they're an option alongside the classic AMQP 0-9-1 clients like amqplib, which are still fully supported.

## 271: What are the main differences between AMQP 0-9-1 and AMQP 1.0 in RabbitMQ?

- **Model:** AMQP 0-9-1 has exchanges, queues and bindings in the protocol. AMQP 1.0 has links to addresses; RabbitMQ maps addresses to its objects.
- **Topology:** AMQP 0-9-1 declares queues with protocol methods. AMQP 1.0 clients use a separate management API.
- **Flow control:** AMQP 1.0 uses link credit, which is more precise than prefetch.
- **Settlement:** AMQP 1.0 has accepted, released, rejected and modified outcomes, so a consumer can, for example, requeue a message and add annotations.
- **Standard:** AMQP 1.0 is an ISO standard used by other brokers (Azure Service Bus, ActiveMQ Artemis), so clients are more portable.

Both run on port 5672 and can work with the same queues.

## 272: Can an MQTT publisher send messages to an AMQP consumer?

Yes. RabbitMQ converts messages between protocols internally. An MQTT message published to topic `sensors/room1/temp` arrives in the `amq.topic` exchange with routing key `sensors.room1.temp`, and an AMQP queue bound with `sensors.#` receives it.

Some details change in conversion (MQTT user properties become headers, content types may be missing), so test that the consumer reads what you expect. The same goes for STOMP and AMQP 1.0, which all share the internal message container format since RabbitMQ 3.13.

## 273: How do you give a monitoring tool read-only access?

Create a user with the `monitoring` tag and read-only permissions (or no AMQP permissions at all if it only uses the HTTP API):

```bash
rabbitmqctl add_user grafana 'long-random-password'
rabbitmqctl set_user_tags grafana monitoring
rabbitmqctl set_permissions -p / grafana '^$' '^$' '.*'
```

For Prometheus, the metrics endpoint on port 15692 doesn't need a user by default, so restrict it at the network level instead.

## 274: Can you publish messages through the HTTP API?

Yes, with `POST /api/exchanges/{vhost}/{exchange}/publish`:

```bash
curl -u admin:secret -X POST -H 'content-type: application/json' \
  http://localhost:15672/api/exchanges/%2F/amq.default/publish \
  -d '{"properties":{},"routing_key":"tasks","payload":"hello","payload_encoding":"string"}'
```

It's fine for testing or occasional manual fixes, but not for production traffic. Every request opens work on the management plugin, there are no confirms in the normal sense, and it's much slower than AMQP.

## 275: Which environment variables can configure RabbitMQ?

A few useful ones:

- `RABBITMQ_NODENAME`: node name, like `rabbit@rmq-0`
- `RABBITMQ_CONFIG_FILE`: path to `rabbitmq.conf`
- `RABBITMQ_MNESIA_BASE`: base data directory (the name is historical)
- `RABBITMQ_LOG_BASE`: log directory
- `RABBITMQ_USE_LONGNAME`: use fully qualified hostnames in node names
- `RABBITMQ_ERLANG_COOKIE` is deprecated; use the cookie file instead

They can also be set in `rabbitmq-env.conf` without the `RABBITMQ_` prefix. Most other settings belong in `rabbitmq.conf`.

## 276: When do you need advanced.config?

`advanced.config` is an Erlang-terms config file for settings that can't be expressed in `rabbitmq.conf`, usually because they need nested lists or tuples. Examples:

- LDAP authorization queries
- Static shovel definitions
- Some low-level Erlang or Ra settings

```erlang
[
  {rabbitmq_shovel, [{shovels, [
    {my_static_shovel, [
      {source, [{protocol, amqp091}, {uris, ["amqp://"]}, {queue, <<"src">>}]},
      {destination, [{protocol, amqp091}, {uris, ["amqp://remote"]}, {publish_properties, [{delivery_mode, 2}]}]}
    ]}
  ]}]}
].
```

Use `rabbitmq.conf` for everything else; it's easier to read and validate.

## 277: What are common mistakes when starting with RabbitMQ?

- Opening a new connection or channel per message
- Using auto-ack for important work
- No prefetch, so one consumer gets everything
- Requeueing failed messages forever with no DLQ
- Forgetting `persistent: true` or using non-durable queues for important data
- Not using publisher confirms
- No reconnection logic in clients
- Letting queues grow without limits or alerts
- Using classic queues for critical data in a cluster
- Assuming exactly-once delivery and not handling duplicates
- Leaving `guest/guest` or exposing the management UI publicly

## 278: What happens to consumers when their queue is deleted?

RabbitMQ sends a `basic.cancel` to the consumer (if the client supports consumer cancel notifications, which all modern ones do). In amqplib, your consume callback is called with `null`.

```js
await channel.consume("jobs", (msg) => {
  if (msg === null) {
    console.warn("Consumer cancelled by broker, resubscribing later");
    scheduleResubscribe();
    return;
  }
  // ...
});
```

The same happens when the node hosting a classic queue goes down. Handle it by redeclaring the queue (if appropriate) and subscribing again.

## 279: How do you check which deprecated features a cluster is using?

RabbitMQ tracks deprecated features and warns in the logs when they're used. You can list them:

```bash
rabbitmq-diagnostics list_deprecated_features
rabbitmq-diagnostics list_used_deprecated_features
```

Each feature has a phase: permitted by default, denied by default, disconnected or removed. Before upgrading, check that nothing you rely on becomes denied or removed in the target version. For example, in 4.3 global QoS and transient non-exclusive queues became denied by default.

## 280: What are transient non-exclusive queues and why were they deprecated?

These are queues declared with `durable: false` but not exclusive. They're deleted when their node restarts, but unlike exclusive queues they aren't tied to a connection, so they can live for a long time on a node and then vanish on restart, which surprises people.

They're deprecated and denied by default since RabbitMQ 4.3. Use exclusive queues for temporary per-connection queues, or durable queues (with `x-expires` if they should clean up after themselves) otherwise. You can re-enable them temporarily with `deprecated_features.permit.transient_nonexcl_queues = true`, but plan to migrate.

## 281: How do you pass extra info to a consumer about why a message failed?

When you dead-letter a message by rejecting it, you can't change its headers. If you want to record the error, publish a new message to the DLQ yourself with the original body and extra headers, then ack the original.

```js
async function sendToDlq(msg, err) {
  channel.publish("orders.dlx", "orders", msg.content, {
    ...msg.properties,
    headers: {
      ...msg.properties.headers,
      "x-error-message": String(err.message).slice(0, 500),
      "x-failed-at": new Date().toISOString(),
    },
  });
  channel.ack(msg);
}
```

Use a confirm channel here so the original isn't acked before the DLQ copy is safe. AMQP 1.0 clients can instead use the "modified" outcome to add annotations when dead-lettering.

## 282: What is the difference between nack with requeue and publishing a message again?

- **nack with requeue:** the same message goes back to its queue, keeps its properties and usually its position near the head. In quorum queues the delivery count goes up. It's fast but retries right away.
- **Republish and ack:** you publish a new copy (maybe to another exchange, with new headers like a retry count or delay) and ack the original. You get full control, but you need publisher confirms to avoid losing the message between the publish and the ack.

Republishing is the usual way to build custom retry logic with delays and backoff.

## 283: How do you make sure a consumer doesn't lose a message when it does a database write and then acks?

Do the DB write first, then ack only after it commits. If the process crashes between commit and ack, the message is redelivered and processed again, so make the write idempotent (unique key or processed-ID table).

```js
await channel.consume("payments", async (msg) => {
  const payment = JSON.parse(msg.content.toString());
  await db.query(
    "INSERT INTO payments (id, amount) VALUES ($1, $2) ON CONFLICT (id) DO NOTHING",
    [payment.id, payment.amount],
  );
  channel.ack(msg);
});
```

Acking before the write is wrong: a crash after the ack loses the message for good.

## 284: How does RabbitMQ decide which consumer gets a message when one is blocked by prefetch?

RabbitMQ skips consumers that have reached their prefetch limit and gives the message to the next one in round-robin order that has room. If every consumer is full, the message stays ready in the queue until one of them acks something.

With consumer priorities, it first tries the highest priority consumers with free capacity, and only then lower ones. This is why prefetch is the main tool for fair distribution between fast and slow consumers.

## 285: What are the risks of setting a very large prefetch?

- One consumer grabs a big chunk of the queue, and other consumers (even new ones you just scaled up) sit idle.
- If the consumer crashes, all those messages are redelivered at once, maybe causing duplicates and a load spike.
- Messages may wait in the client's memory long enough to hit the consumer timeout.
- Client memory usage grows, especially with large messages.

A big prefetch only helps when each message is processed very quickly and network latency is the bottleneck.

## 286: How do you read the "state" of a connection in the management UI?

- **running:** working normally
- **flow:** RabbitMQ is temporarily throttling this publisher because something downstream is slower
- **blocking:** an alarm is active, and the connection will be blocked as soon as it publishes
- **blocked:** an alarm is active and this connection published, so RabbitMQ stopped reading from it
- **closing / closed:** being closed

Many connections in `blocked` means look at node alarms (memory or disk). Constant `flow` means a queue or the disk is a bottleneck.

## 287: What is the difference between rabbitmqctl, rabbitmq-queues, rabbitmq-streams and rabbitmq-upgrade?

They're all CLI tools that talk to the node over Erlang distribution:

- `rabbitmqctl`: general admin (users, vhosts, permissions, policies, listing objects, cluster membership)
- `rabbitmq-queues`: quorum queue operations (add/remove members, grow, shrink, rebalance, check status)
- `rabbitmq-streams`: stream operations (add/remove replicas, super streams, stream status)
- `rabbitmq-upgrade`: upgrade and maintenance tasks (`drain`, `revive`, `await_online_quorum_plus_one`)
- `rabbitmq-diagnostics`: health checks and inspection
- `rabbitmq-plugins`: plugins

## 288: What is maintenance mode?

Maintenance mode prepares a node to be stopped safely. Running `rabbitmq-upgrade drain` on a node:

- stops client listeners, so no new connections come in
- closes existing client connections
- moves quorum queue leaders to other nodes
- marks the node so it won't be chosen for new queue leaders

After the work is done, `rabbitmq-upgrade revive` puts it back in service (restarting the node also revives it). It reduces disruption during upgrades and OS patching.

## 289: How do you rate-limit processing to protect a slow downstream API?

The broker doesn't have a built-in "N messages per second" limit, but you can build one:

- Limit concurrency with prefetch and the number of consumers (e.g. 2 consumers with prefetch 5 = max 10 calls in parallel).
- Add a rate limiter in the consumer (token bucket) before calling the API.
- On 429 errors, nack to a delayed retry queue instead of retrying immediately.
- Use single active consumer if the API allows only one caller at a time.

The queue absorbs bursts, and your consumers drain it at the speed the API can handle.

## 290: How do you handle a slow message blocking others behind it?

In one queue with one consumer, a slow message holds up everything behind it (head-of-line blocking). Options:

- Add more consumers (if order doesn't matter), so other messages are processed in parallel.
- Use a reasonable prefetch so one consumer can work on several messages.
- Put timeouts on external calls so a message can't hang forever.
- Split slow and fast work into separate queues, so a batch of slow jobs doesn't delay quick ones.

## 291: What is the difference between the publish rate and the deliver rate in the UI?

- **Publish (incoming) rate:** how many messages per second are routed into the queue.
- **Deliver rate:** how many per second are sent to consumers (`deliver` with manual ack, `deliver (noack)` with auto-ack, `get` for basic.get).
- **Ack rate:** how many per second consumers confirm.
- **Redeliver rate:** how many deliveries are repeats.

If publish is higher than ack over time, the queue grows. A high redeliver rate usually means failing messages being requeued.

## 292: How do you safely change a queue setting that can't be changed?

Settings given as arguments (like `x-queue-type` or `x-max-priority`) are fixed. Common ways to change them:

1. Create a new queue with the new settings (for example `orders.v2`).
2. Bind it the same way as the old queue, so new messages go to both or only the new one.
3. Move consumers to the new queue.
4. Shovel the remaining messages from the old queue into the new one.
5. Delete the old queue.

To avoid this in the future, put settings that might change into policies, not arguments.

## 293: Should consumers or producers handle retries?

Usually both, for different problems:

- **Producers** retry publishing when the connection drops or a confirm doesn't arrive, so messages aren't lost on the way in.
- **Consumers** handle processing failures: retry with delay for temporary errors, DLQ for permanent ones.

Avoid having the producer re-send because "it didn't hear back from the consumer". That couples them again and causes duplicates. If the producer needs a result, use a reply message or an event like `order.processed`.

## 294: How do you decide which errors to retry and which to send to the DLQ?

Split errors into two groups:

- **Temporary:** timeouts, connection errors, 503/429 from an API, DB deadlocks. Retry with backoff.
- **Permanent:** validation errors, malformed JSON, "not found" for an entity that will never exist, bugs. Retrying won't help; send to the DLQ right away.

```js
function isRetryable(err) {
  return (
    ["ETIMEDOUT", "ECONNRESET", "ECONNREFUSED"].includes(err.code) ||
    [429, 503].includes(err.status)
  );
}
```

This keeps retry queues from filling with messages that can never succeed.

## 295: How do you replay messages from a DLQ after fixing a bug?

1. Deploy the fix.
2. Check a few messages in the DLQ to make sure they'll now succeed.
3. Move them back with a shovel (the UI "Move messages" feature) to the main queue or its exchange.
4. Watch the main queue and the DLQ to make sure they don't fail again.

If the DLQ has messages from several problems, write a small script that reads them, filters by error header or type and republishes only the ones you want. Remember they may be old, so check whether they still make sense to process.

## 296: How do you handle message ordering when using retries?

Retries break order: if message 1 fails and goes to a retry queue, message 2 is processed first. If order matters per entity:

- Process per-entity queues with a single active consumer, and retry in place (in-process backoff) instead of moving the message away.
- Or make consumers handle out-of-order messages: use version numbers or timestamps and ignore older updates.

The second approach is usually safer, since order can break in other ways too (redelivery after a crash, multiple publishers).

## 297: What should you put in a message: the full data or just an ID?

- **Full data (event-carried state):** consumers don't need to call back the producer, and they see the data as it was at that moment. Messages are larger, and sensitive data travels through the broker.
- **Just an ID (notification):** messages are small, consumers fetch the current data from the source. It adds load on the producer's API and couples services again, and the data may have changed since the event.

A common middle ground: include the fields most consumers need plus the ID, and keep large or sensitive data in the source system.

## 298: How do you handle sensitive data in messages?

- Don't send what consumers don't need (no full card numbers, passwords or tokens).
- Use TLS for client and inter-node connections.
- Use vhosts and permissions so only the right services can read the queues.
- Encrypt sensitive fields in the payload if the broker operators shouldn't see them.
- Be careful with tracing, logging and the management UI's "get messages", since they can expose payloads.
- Remember that DLQs and streams keep data longer than normal queues.

## 299: How does RabbitMQ handle a client that sends data too fast for a quorum queue?

Quorum queues apply backpressure through flow control. Each publish needs to be replicated to a majority of replicas and written to disk, and if replicas or disks can't keep up, the queue stops giving credit and RabbitMQ stops reading from the publisher's socket for a while. Confirms also arrive later.

Clients with a limit on unconfirmed messages naturally slow down. If a single quorum queue is the bottleneck, spread the load over several queues (sharding by key) or check disk performance.

## 300: How do you design topology for a typical microservices system?

A simple, common setup:

- One durable topic exchange per domain or service that publishes events: `orders.events`, `payments.events`.
- Each consuming service has its own quorum queues, named after the service, bound to the routing keys it needs.
- Each queue has a DLX and DLQ, and maybe retry queues.
- Commands go to a direct exchange or straight to the target service's queue.
- Policies set DLX, limits and delivery limits by name pattern.
- Topology is declared by the services or kept in code (definitions, Terraform, Kubernetes operator).

This keeps producers independent from consumers and makes it easy to add new consumers later.

---

# Advanced Questions (301-450)

## 301: How is RabbitMQ structured internally in terms of Erlang processes?

RabbitMQ uses Erlang's lightweight processes heavily:

- Each client connection has a reader process, a writer process and a few helpers.
- Each channel is its own process, which does routing for messages published on it.
- Each queue (classic queue, or each replica of a quorum queue or stream) is one or more processes.
- Supervisors restart processes that crash.

A message published on a channel is routed by the channel process, which looks up the bindings and sends the message to the queue processes. Since one queue is mostly handled by one process, a single queue uses roughly one CPU core at most. That's why one very busy queue can be a bottleneck even on a big machine, and why spreading load across several queues helps.

## 302: What happens step by step when a message is published to a quorum queue?

1. The client sends `basic.publish` frames over its connection; the reader process parses them.
2. The channel process routes the message using the exchange type and bindings (metadata lives in Khepri, with fast local lookups).
3. The channel sends the message to the quorum queue's leader (possibly on another node).
4. The leader appends it to its Raft log and replicates it to followers.
5. Each replica writes it to its write-ahead log (WAL) and fsyncs.
6. When a majority has written it, the entry is committed and applied to the queue state.
7. The channel gets notified and sends `basic.ack` to the publisher (if confirms are on).
8. The leader delivers the message to a consumer with available prefetch.

So the publisher's confirm already means the message is on disk on a majority of nodes.

## 303: What is credit-based flow control internally?

Inside RabbitMQ, processes pass messages along a chain: reader to channel to queue (and to the message store or disk). Each sender gets a number of "credits" from the next process. Every message uses a credit, and the receiver gives new credits back as it handles messages.

If a queue process falls behind, it stops handing out credits, the channel blocks, then the reader blocks, and eventually RabbitMQ stops reading from the TCP socket. That's the `flow` state you see in the UI. It keeps memory bounded without dropping messages, and the pressure travels back to the publisher through TCP.

## 304: How does classic queue v2 store messages?

Classic queues version 2 (the only version since 4.3) store messages in two places:

- A **per-queue index**, which keeps the queue's order and, for small messages, the message itself embedded in the index.
- A **shared message store** per vhost, for larger messages. A message routed to several classic queues on the same node is stored once there and reference counted.

Classic queues keep only a small number of messages in memory and move the rest to disk, so they behave like the old "lazy" mode by default. RabbitMQ 4.4 introduced a new on-disk format (v2, `.sqs` files) for the shared message store; once a node has written that format, it can't be downgraded to 4.3 or earlier.

## 305: How do quorum queues store data on disk?

Quorum queues use the Ra library (Raft implementation):

- All quorum queues on a node share one **write-ahead log (WAL)**. Every new entry is written there first and fsynced, often in batches across many queues.
- Entries are later moved into per-queue **segment files**.
- Each queue takes **snapshots** of its state from time to time, and log entries older than the snapshot can be deleted.

A log can only be truncated up to the oldest message the queue still needs, so a single old unacked or unconsumed message can keep a lot of log data on disk. Since 4.3, recovery snapshots and snapshot throttling help with restart times and disk use.

## 306: Why can a quorum queue use much more disk than the size of its messages?

The Raft log contains not only messages but also every operation: enqueues, acks, returns, consumer changes. Old entries can only be removed once a snapshot covers them, and the snapshot can only move past messages that were fully settled.

If one message at the head of the queue stays unacked for hours (a stuck consumer or a very long job), the log can't be truncated, so all operations since then stay on disk. Long queues, many redeliveries and large messages make this worse. Watch disk use and Raft log metrics, keep queues short, and avoid holding messages unacked for long.

## 307: What happens when a quorum queue loses its majority?

A 3-replica quorum queue needs 2 replicas online. If 2 of 3 are down, it has no majority, so:

- It can't elect a leader or accept new messages (publishers get nacks or timeouts).
- Consumers get no deliveries.
- No data is lost; the remaining replica keeps what it had.

When enough replicas come back, a leader is elected and the queue continues. If replicas are permanently lost, an operator can force the queue to shrink to the surviving replica with `rabbitmq-queues delete_member` / `force_shrink_member_to_current_member`, accepting possible loss of uncommitted data. This is a last-resort action.

## 308: Why should quorum queues have an odd number of replicas?

Raft needs a strict majority. With 3 replicas, you need 2 (tolerates 1 failure). With 4, you need 3 (still tolerates only 1). With 5, you need 3 (tolerates 2).

So an even number adds cost (more replication, more disk, slower commits) without improving fault tolerance. The same logic applies to cluster size, especially now that Khepri (also Raft) stores the cluster metadata: 3 or 5 nodes are the usual choices.

## 309: What are non-voting quorum queue members?

A non-voting member gets a copy of the log but doesn't count toward the majority and doesn't vote in elections. New members can be added as non-voters, catch up with the log in the background, and then be promoted to voters.

This avoids a problem where adding a new replica that's far behind would slow down commits or put availability at risk while it catches up. The `quorum_queue_non_voters` feature flag is required before upgrading to 4.3.

## 310: How do you tune quorum queue throughput?

- Use fast disks with low fsync latency (local NVMe or good SSD-backed volumes). Disk latency is usually the main limit.
- Publish with many messages in flight (async confirms), not one at a time.
- Spread load over several queues so leaders are on different nodes and use more cores.
- Keep queues short; long queues and big logs slow down snapshots and recovery.
- Use reasonable prefetch values so consumers keep up.
- Avoid very large messages; split them or use claim checks.
- Make sure leaders are balanced across nodes.

Measure with PerfTest before and after changing anything.

## 311: How do streams work internally?

Streams are built on the Osiris library. Each stream has a leader (writer) and replicas, and data is stored in segment files on disk as chunks of messages, with an index file per segment.

Writes go to the leader, which appends chunks and replicates them to replicas. Consumers can read from any replica, and the stream protocol can send chunks straight from the file to the socket (using `sendfile`), which is one reason streams are very fast. Retention deletes whole old segments. Unlike quorum queues, streams don't track per-message acks, so their state is just "where's the end of the log".

## 312: Why are streams faster than queues for some workloads?

- Messages are never deleted per consumer, so there's no per-message state to update on ack.
- Data is written and read in chunks (batches), which is efficient for disks and networks.
- Consumers can read from replicas, spreading read load.
- With the stream protocol, reading can use zero-copy file transfers.
- Many consumers reading the same data don't multiply storage, unlike fan-out to many queues.

The trade-off: no per-message ack and redelivery, no TTL per message, no priorities, and consumers must manage their own position.

## 313: What changed for clustering now that Khepri is the only metadata store?

Since RabbitMQ 4.3, Mnesia is removed and all metadata (vhosts, users, queues, exchanges, bindings, policies) lives in Khepri, which uses Raft. Effects:

- Metadata changes need a majority of nodes. In a 3-node cluster with 2 nodes down, you can't declare queues, add users or change policies.
- Network partitions are handled by Raft instead of the old partition handling strategies, so there's no split brain in metadata.
- The `cluster_partition_handling` setting (pause_minority, autoheal) no longer does anything.
- `force_reset` and RAM nodes are gone.
- Upgrading to 4.3 requires the `khepri_db` feature flag to be enabled first (on 4.2).

## 314: How does RabbitMQ 4.3+ behave during a network partition?

With Khepri and quorum queues, everything important uses Raft. During a partition, the side with a majority of nodes keeps working: it can change metadata, and quorum queues whose leader is (or can be elected) on that side keep accepting and delivering messages. The minority side can't change metadata, and quorum queues there can't commit.

When the partition heals, minority nodes catch up from the majority. Classic queues, which aren't replicated, are just available or not depending on where their node is. This is much simpler and safer than the old Mnesia-based strategies.

## 315: What were the old partition handling strategies?

Before 4.3, with Mnesia, you chose how a cluster reacts to a partition with `cluster_partition_handling`:

- `ignore`: do nothing (default). Both sides kept running and diverged, and you fixed it by hand.
- `pause_minority`: nodes on the minority side paused themselves. Safest choice for 3+ nodes in one data center.
- `autoheal`: after the partition, the side with fewer clients restarted and resynced, losing its changes.
- `pause_if_all_down`: paused if certain listed nodes weren't reachable.

You'll still see these in old configs and interview questions. In 4.3+ they're ignored, and the release notes recommend removing them from `rabbitmq.conf`.

## 316: What happens to classic queues in a cluster when their node fails?

A classic queue lives on one node. Other nodes know about it from the metadata, but they don't have its messages. If that node fails:

- The queue becomes unavailable. Declaring it from another node returns an error saying its home node is down, and publishes routed to it are lost (or nacked/returned depending on settings).
- Durable queues with persistent messages come back when the node comes back.
- Non-durable queues and transient messages are lost.

This is why critical data belongs in quorum queues, and classic queues are best for temporary data.

## 317: What does a full "no message loss" setup look like?

You need every link in the chain:

1. **Publisher:** publisher confirms, retries on nack or timeout, and an outbox if the event comes from a DB change.
2. **Routing:** `mandatory` flag or an alternate exchange, so unroutable messages aren't dropped.
3. **Queues:** quorum queues (replicated, always durable) with persistent messages.
4. **Limits:** `reject-publish` overflow instead of `drop-head` if dropping is unacceptable; DLX for anything that is dropped.
5. **Consumer:** manual acks only after work is done, idempotent processing.
6. **Failures:** DLQs with alerts, delivery limits for poison messages.
7. **Operations:** 3+ nodes, enough disk, alarms set right, monitoring.

Skip any one and there's a path for messages to be lost.

## 318: When exactly is a publisher confirm sent for classic vs quorum queues?

- **Classic queue, persistent message:** after the message is written to disk (fsync) on the queue's node, or when a consumer has acked it, whichever comes first. Disk writes are batched, so confirms can take a few hundred ms under low load.
- **Classic queue, transient message:** once the queue has accepted it in memory.
- **Quorum queue:** after a majority of replicas have written it to their WAL and fsynced. Persistence flags don't matter.
- **Stream:** after a majority of replicas have it.
- **Multiple queues:** only after all target queues have confirmed.

So confirms have very different costs depending on the queue type and replication.

## 319: How do you think about throughput vs latency in RabbitMQ?

Most settings trade one for the other:

- Batching publishes and confirms raises throughput but adds a bit of latency per message.
- Large prefetch raises consumer throughput but makes distribution less fair and delays redelivery.
- Quorum queues add latency (replication and fsync) but give safety.
- Fewer, larger messages are more efficient than many tiny ones.

For user-facing paths (like RPC), keep queues short and prefetch modest. For bulk processing, batch and keep many messages in flight. Measure p50 and p99 latency, not just average throughput.

## 320: How do you benchmark RabbitMQ?

Use PerfTest (the official load testing tool, a Java app also available as a Docker image) or `stream-perf-test` for streams:

```bash
docker run -it --rm pivotalrabbitmq/perf-test:latest \
  --uri amqp://user:pass@rabbit:5672 \
  --queue-args x-queue-type=quorum --queue perf-qq \
  --producers 2 --consumers 2 --size 1000 \
  --confirm 100 --multi-ack-every 50 --qos 200 \
  --time 120
```

Test with your real message sizes, queue types, confirm and ack settings and number of queues. A benchmark with transient messages and auto-ack on a classic queue tells you nothing about a production setup with quorum queues and confirms.

## 321: How do you size a RabbitMQ cluster?

Start from the workload:

- **Message rate** (peak publishes and deliveries per second) and **message size**
- **Queue type** and replication factor (quorum queues write each message to 3 nodes)
- **Backlog** you must handle (how many messages can pile up during an outage, times size, times replicas = disk)
- **Number of connections, channels and queues** (memory per object)
- **Fan-out** (one publish going to N queues multiplies work)

Then run PerfTest on candidate hardware with a realistic setup and leave headroom (aim for under 50% of tested capacity at peak). Typical production clusters are 3 nodes, with 5 for higher fault tolerance; very large loads are often split into several independent clusters.

## 322: How many queues can RabbitMQ handle?

There's no hard limit, but every queue costs memory and some CPU, and quorum queues cost more than classic queues (each replica is a Raft member with its own state and timers). Clusters with tens of thousands of quorum queues work, but metadata operations, node restarts and leader rebalancing get slower.

Avoid designs that create one queue per user or per entity when the count can grow to hundreds of thousands. Use routing keys or headers to multiplex many logical streams over fewer queues, or use streams with filtering. RabbitMQ also lets you set limits like `cluster_exchange_limit` (4.2) and vhost `max-queues` to catch runaway designs.

## 323: How do you tune RabbitMQ for many connections?

- Raise the open file descriptor limit (each connection is a socket); for example `LimitNOFILE=1000000` in systemd.
- Reduce per-connection memory by lowering TCP buffer sizes (`tcp_listen_options.sndbuf` / `recbuf`), at some throughput cost.
- Use reasonable heartbeats (not too low).
- Set limits (`max_connections`, vhost and user limits) to protect the node.
- Spread connections across nodes with a load balancer.
- For huge numbers of IoT clients, MQTT is lighter than AMQP since 3.12.

And before tuning the broker, check whether the clients really need that many connections; connection pooling or fixing churn is often the real fix.

## 324: How do you find out what's using memory on a node?

```bash
rabbitmq-diagnostics memory_breakdown --unit mb
```

It splits memory by category: connection processes, channels, queue processes (classic and quorum), quorum queue ETS tables, metadata, binary heap (message bodies), management stats, plugins, other.

- High **binary** usually means message bodies in memory: big messages, many unacked, or slow queues.
- High **connection_other** or **connection_readers** means many connections.
- High **quorum queue** memory means many quorum queues or large in-memory state.
- High **mgmt_db** means the management plugin is collecting too many stats.

The management UI shows the same breakdown on the node page.

## 325: Why are long queues a problem?

RabbitMQ is designed for queues that are short most of the time. Long queues (millions of messages):

- use more disk, and some memory per message for indexes
- make quorum queue logs and snapshots large, slowing recovery and replication
- make restarts slower, since queues need to recover their state
- increase latency for every message behind the backlog
- make any mistake (like purging or a poison message) more expensive

A backlog during an outage is fine; a queue that's always long means consumers are under-provisioned or the queue is being used as a database. For long-term retention, use streams.

## 326: What is head-of-line blocking and how does it show up in RabbitMQ?

Head-of-line blocking is when one item at the front holds back everything behind it. In RabbitMQ:

- One slow or stuck message in a single-consumer queue delays all others.
- Per-message TTL in classic queues: an unexpired message at the head blocks expired ones behind it from being removed.
- In TTL-based delay queues with mixed delays, a long delay at the head blocks short ones.
- One unacked message in a quorum queue blocks log truncation.

Solutions are separate queues per delay or per priority, timeouts on processing, more consumers when order doesn't matter, and keeping messages acked quickly.

## 327: One queue is a bottleneck. How do you scale it?

A single queue is handled mostly by one Erlang process (and one leader for quorum queues), so it has a throughput ceiling. To go beyond it:

- Split the queue into N queues and spread messages with a consistent hash or `x-modulus-hash` exchange, or by routing key.
- Make sure the queue leaders are spread across nodes.
- Use a super stream if the workload fits the log model.
- On the consumer side, scale consumers per shard.

Ordering is then kept per shard (per key), not globally. Check first that the bottleneck is really the queue and not slow consumers or disk.

## 328: How far can you scale consumers on one queue?

Adding consumers helps until something else is the limit:

- The queue process itself (a single queue can only dispatch so many messages per second).
- Downstream systems (DB, APIs) the consumers call.
- Ordering needs, if any.

Past that point, adding consumers just adds more unacked messages and contention. If you need more, shard the queue. A good sign of over-provisioning is many consumers with low utilization; RabbitMQ shows consumer utilization (the percentage of time the queue could deliver to consumers) per queue.

## 329: How do you autoscale consumers based on queue length?

In Kubernetes, KEDA has a RabbitMQ scaler that scales a deployment based on queue length or message rate:

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: email-worker
spec:
  scaleTargetRef:
    name: email-worker
  minReplicaCount: 1
  maxReplicaCount: 20
  triggers:
    - type: rabbitmq
      metadata:
        protocol: amqp
        queueName: emails
        mode: QueueLength
        value: "100"
      authenticationRef:
        name: rabbitmq-auth
```

Make sure consumers shut down gracefully on scale-in (cancel, finish in-flight, ack), and set a maximum so autoscaling doesn't overload the database the workers write to.

## 330: Can RabbitMQ give exactly-once delivery?

No broker can guarantee exactly-once delivery across a network with failures, and RabbitMQ doesn't claim to. The publisher can't always know if a message arrived (a lost confirm means it must resend), and the consumer can crash after doing the work but before acking.

What you can achieve is exactly-once **processing effect**: at-least-once delivery plus idempotent consumers or de-duplication. Streams add publisher de-duplication on the write side, which helps avoid duplicates from publisher retries, but the consumer side still needs idempotency.

## 331: How do you implement an outbox publisher reliably?

Typical design:

1. The service writes business data and an outbox row in one transaction.
2. A relay process (in the same service or separate) polls the outbox in order, or reads it via change data capture (Debezium).
3. It publishes each row with publisher confirms.
4. After the confirm, it marks the row as sent (or deletes it).

```sql
SELECT id, routing_key, payload
FROM outbox
WHERE sent_at IS NULL
ORDER BY created_at
LIMIT 100
FOR UPDATE SKIP LOCKED;
```

`FOR UPDATE SKIP LOCKED` lets several relay instances work without picking the same rows. Use the outbox row ID as the `messageId`, so consumers can de-duplicate if a row is published twice (crash after publish but before marking).

## 332: How do you implement an inbox (de-duplication) on the consumer side?

Store processed message IDs in the same database transaction as the side effects:

```sql
CREATE TABLE inbox (
  message_id TEXT PRIMARY KEY,
  processed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

```js
await db.transaction(async (tx) => {
  const { rowCount } = await tx.query(
    "INSERT INTO inbox (message_id) VALUES ($1) ON CONFLICT DO NOTHING",
    [msg.properties.messageId],
  );
  if (rowCount === 1) await applyBusinessChange(tx, payload);
});
channel.ack(msg);
```

Clean old rows periodically (keep them longer than the longest possible redelivery window). Side effects outside the DB (emails, API calls) need their own idempotency keys.

## 333: How would you implement a saga with RabbitMQ?

A saga is a series of local transactions across services, with compensating actions if a step fails. With RabbitMQ there are two styles:

- **Choreography:** each service listens to events and publishes the next ones (`order.created` -> payment service -> `payment.completed` -> shipping service). On failure, services publish failure events and others compensate (`payment.failed` -> cancel order). Simple for short flows, hard to follow for long ones.
- **Orchestration:** an orchestrator service sends commands (`reserve-stock`, `charge-card`) and waits for replies or events, keeping saga state in its DB. Easier to understand and monitor.

Either way you need idempotent handlers, timeouts for steps that never answer, and the outbox pattern so state changes and messages stay in sync.

## 334: Can you use RabbitMQ streams for event sourcing?

You can use streams as an event log for some event-driven needs: they keep history, support replay from any offset and allow many consumers. That's enough for building read models or feeding new services with past events.

For true event sourcing (where the event log is the source of truth for each aggregate), streams are missing things like per-aggregate streams with optimistic concurrency checks ("append only if version is N") and infinite retention by design. Most teams use a database or a dedicated event store as the source of truth, and publish to RabbitMQ (queues or streams) for distribution.

## 335: What are the costs of message priorities?

- Classic priority queues keep a sub-queue per priority level, using more memory and CPU. That's why up to 10 levels are recommended, even though 255 are allowed.
- Priorities only reorder messages that are waiting. With a high prefetch, messages are already sent to consumers before a higher priority one arrives.
- Low-priority messages can be starved if high-priority traffic never stops (strict priority).
- Ordering between messages of different priority is lost by design.

Often a separate queue with dedicated consumers for urgent work is simpler and more predictable.

## 336: How did consumer timeouts change in RabbitMQ 4.3?

Before 4.3, the consumer timeout was enforced per channel for all queue types: if any delivery wasn't acked within `consumer_timeout` (30 minutes by default), the whole channel was closed with a `PRECONDITION_FAILED` error.

In 4.3, quorum queues got their own consumer timeout handling, with more control, and consumer timeouts no longer apply to classic queues and streams. If you relied on the timeout to detect stuck consumers on classic queues, you now need another approach (like your own watchdog in the consumer, or moving those queues to quorum queues).

## 337: How do delayed retries work in quorum queues since 4.3?

RabbitMQ 4.3 added delayed retry with configurable backoff to quorum queues. Instead of requeueing a failed message for immediate redelivery, the queue can hold it back for a while before making it available again, with the delay growing on each attempt.

This replaces much of the TTL + DLX "wait queue" plumbing teams used to build by hand. Combined with the delivery limit and a DLX, you get retries with backoff and a final dead letter queue in one queue's configuration. Check the quorum queue docs for the exact policy keys and arguments for your version.

## 338: What is at-least-once dead lettering in quorum queues?

By default, dead lettering is at-most-once: the queue sends the message to the DLX without waiting for confirmation that it arrived, so if the target queue is unavailable, the message can be lost.

Quorum queues support `dead-letter-strategy: at-least-once`. The source queue keeps the message until the target queue confirms it, and retries if needed. It requires `overflow: reject-publish` (not `drop-head`), and it uses more resources because dead-lettered messages stay in the source queue until confirmed.

```bash
rabbitmqctl set_policy qq-dlx '^orders$' \
  '{"dead-letter-exchange":"dlx","dead-letter-strategy":"at-least-once","overflow":"reject-publish"}' \
  --apply-to quorum_queues
```

## 339: Can dead lettering create a loop?

Yes. If queue A dead-letters to an exchange that routes back to A, or A goes to B and B back to A, messages can cycle.

RabbitMQ detects cycles where a message would be dead-lettered back to the same queue for the same reason without any rejection in between (for example, TTL-only cycles), and drops the message to stop an infinite loop. A cycle that includes a consumer rejection is allowed, since that's how TTL-based retry setups work (main queue rejects -> wait queue expires -> main queue). In those setups, you must limit the number of retries yourself using the `x-death` count.

## 340: How do you design multi-tenancy with RabbitMQ?

Options:

- **Vhost per tenant:** strong isolation of names, permissions, policies and limits. Easy to delete a tenant. Overhead per vhost is moderate, so it works up to thousands of tenants, not millions.
- **Shared vhost with tenant in routing keys or headers:** cheaper and simpler for many small tenants, with topic permissions to restrict access. Less isolation.
- **Cluster per tenant (or per group of tenants):** strongest isolation for big or noisy tenants.

In any model, set limits (connections, queues, queue length), so one tenant can't exhaust the broker, and consider fair processing so a big tenant's backlog doesn't delay small ones.

## 341: How do you set up RabbitMQ across regions or data centers?

Don't stretch one cluster across regions. Clusters expect low, stable latency between nodes, and Raft commits would wait on the slow link.

Instead, run a separate cluster per region and connect them:

- **Federation** to copy events from one region's exchanges to another.
- **Shovels** for specific queue-to-queue links or migrations.
- Application-level replication (publishing to both regions) for some cases.

For disaster recovery, decide what you need: just topology (definitions sync), or messages too (federation/shovel with possible duplicates and a few seconds of lag). Failover usually means clients switch DNS or configuration to the other region's cluster.

## 342: Why not run a RabbitMQ cluster across availability zones?

Across availability zones in the same region is fine and common, since latency is low (a few ms). It actually improves resilience: with 3 nodes in 3 AZs, quorum queues and Khepri survive the loss of a whole zone.

Across regions (tens or hundreds of ms) is not recommended. Every quorum queue write and metadata change would wait for a cross-region round trip, net tick timeouts become more likely, and a regional link failure would partition the cluster.

## 343: How do you migrate from classic mirrored queues to quorum queues?

Since mirrored queues are removed in 4.0, this must happen on 3.13 (or earlier) before upgrading. Steps:

1. Check app compatibility: no exclusive or non-durable queues, no global QoS, handling of `x-delivery-count`, priorities.
2. Create quorum queues with new names (or in a new vhost) and the same bindings.
3. Switch consumers to the new queues, then publishers, or bind both and drain the old ones with a shovel.
4. Remove `ha-mode` policies and delete old queues.

An alternative is a blue-green migration to a new 4.x cluster with quorum queues as the default type, moving messages over with shovels or federation.

## 344: What's the upgrade path from RabbitMQ 3.13 to 4.4?

RabbitMQ supports upgrading only from the previous minor series in most cases, so you go step by step: 3.13 -> 4.0 -> 4.1 -> 4.2 -> 4.3 -> 4.4, enabling all feature flags after each step. Along the way:

- Before 4.0: remove classic mirrored queues and any other removed features.
- By 4.2: enable `khepri_db` (needed before 4.3, which removes Mnesia).
- Before 4.3: stop using global QoS, transient non-exclusive queues, CQv1 and lazy mode arguments.
- Check Erlang version support at each step.
- Check client library versions (e.g. amqplib needs 0.10.7+ for 4.1+ because of `frame_max` changes).

If that's too many steps, a blue-green migration to a fresh 4.4 cluster is often simpler.

## 345: What are the requirements for upgrading to 4.3?

- The cluster must be running 4.2.x. Earlier versions can't upgrade directly.
- All feature flags from 4.2 and earlier must be enabled, including `khepri_db`, `rabbitmq_4.0.0`, `rabbitmq_4.1.0`, `rabbitmq_4.2.0`, `quorum_queue_non_voters` and `message_containers_deaths_v2`.
- No CQv1 (`x-queue-version: 1`) or `x-queue-mode` arguments.
- Transient non-exclusive queues and global QoS are denied by default; permit them explicitly if apps still need them.
- Remove `cluster_partition_handling` from config, as it no longer does anything.

Mixed 4.2 and 4.3 clusters work for a rolling upgrade, but only for a few hours.

## 346: Why shouldn't a mixed-version cluster run for long?

During a rolling upgrade, older and newer nodes run together, and feature flags keep the newer nodes from using features the old ones don't understand. This is tested for the short time it takes to restart nodes one by one.

Running mixed for days means new features stay disabled, some operations may behave differently on different nodes, bugs fixed in the new version still affect old nodes, and it's a combination that gets much less testing. Finish the upgrade and enable feature flags as soon as all nodes are on the new version.

## 347: How do feature flags and deprecated features work over the RabbitMQ lifecycle?

**Feature flags** go through stages: experimental (opt-in, may change), stable (should be enabled after upgrade), and required (enabled automatically and needed to upgrade further). Since 4.1, some required flags are enabled automatically at boot when all nodes support them.

**Deprecated features** go through phases: permitted by default (works, logs a warning), denied by default (refused unless you set `deprecated_features.permit.<name> = true`), and removed. This gives a release or more of warning before something stops working.

So for every upgrade: read the release notes, check `list_used_deprecated_features`, and enable all stable feature flags after upgrading.

## 348: What would be on your RabbitMQ security hardening checklist?

- Remove or lock down `guest`; unique users per app with least-privilege permissions
- TLS for AMQP, management, and inter-node and CLI traffic when the network isn't fully trusted
- Firewall ports: only expose 5671 (or 5672 internally) to apps; keep 15672, 25672, 4369 private
- Protect the Erlang cookie and rotate it if exposed
- Use OAuth 2, LDAP or certificates rather than shared passwords where possible
- Limits: `max_message_size`, vhost/user limits, `max_connections`
- Strict OIDC discovery checks (enforced more strictly in 4.4)
- Audit logging via the event exchange
- Regular upgrades for security fixes
- Don't put secrets in messages or definitions files committed to Git

## 349: How do you secure inter-node and CLI communication?

Nodes and CLI tools talk over Erlang distribution (port 25672, with epmd on 4369). By default it's authenticated with the cookie but not encrypted. To encrypt it, configure Erlang distribution over TLS: point the Erlang VM at an `inet_tls_dist` config with certificates, via `SERVER_ADDITIONAL_ERL_ARGS` and the CLI equivalents.

Also restrict those ports with firewalls or network policies so only cluster nodes and admin hosts can reach them. In Kubernetes, the Cluster Operator can set up TLS for inter-node traffic.

## 350: Why is the Erlang cookie so sensitive?

Anyone who knows the cookie and can reach port 25672 (and epmd) can connect to the node as a full Erlang node. That means they can run arbitrary code on the server with RabbitMQ's privileges, read all messages and change anything.

So: keep the cookie file readable only by the RabbitMQ user, don't put it in images or Git, use a long random value, firewall the distribution ports, and change it (on all nodes and CLI hosts at once) if it leaks.

## 351: Should the management UI be exposed publicly?

No. It gives full control to anyone with admin credentials, and a public login page invites brute force attacks. Keep it on an internal network, behind a VPN, or behind an authenticating proxy, and use OAuth 2 login (with MFA from the identity provider) if possible.

If it must be reachable, use TLS, strong unique passwords, few admin users, and consider enabling HSTS headers (configurable since 4.4). Read-only dashboards are better served from Grafana with Prometheus metrics.

## 352: How do OAuth 2 scopes map to RabbitMQ permissions?

Scopes in the token follow a format based on the resource server ID (for example `rabbitmq`):

- `rabbitmq.read:<vhost>/<resource pattern>` -> read permission
- `rabbitmq.write:<vhost>/<pattern>` -> write permission
- `rabbitmq.configure:<vhost>/<pattern>` -> configure permission
- `rabbitmq.tag:<tag>` -> user tags like `monitoring` or `administrator`

Topic permissions can also be included with a routing key part. If your identity provider can't issue scopes in this format, RabbitMQ can map custom scope names with `scope_aliases`, or read them from a different claim. Tokens expire, so long-lived connections must refresh them.

## 353: What changed for passive declarations in RabbitMQ 4.4?

A passive declare (`checkQueue` / `checkExchange` in amqplib) only checks whether a queue or exchange exists, without creating it. Before 4.4, any user with access to the vhost could do it, which let users discover object names they had no permissions on.

Since 4.4, a passive declaration needs at least one of configure, write or read permission on the resource. If a client with very restricted permissions uses `checkQueue` on startup, it may now get `ACCESS_REFUSED`, so check permissions when upgrading.

## 354: How do you protect a broker from misbehaving clients?

- `max_message_size` to reject huge messages
- `max_connections` and `max_channels` (4.4 names), plus vhost and user limits
- Queue length limits via operator policies
- `cluster_exchange_limit` and vhost `max-queues` to stop topology explosions
- Memory and disk alarms with sensible thresholds
- Per-protocol connection limits for MQTT, STOMP and streams (added in 4.4)
- Rate limits at the network level (firewalls, load balancers)
- Monitoring connection and channel churn to catch buggy clients early

Most incidents come from a client bug, like a connection loop or a missing ack, not from real load.

## 355: What is the event exchange plugin?

`rabbitmq_event_exchange` publishes internal broker events to the `amq.rabbitmq.event` topic exchange: connections created/closed, channels, queues and exchanges created/deleted, bindings, users created, permissions changed, policy changes, user authentication success or failure and more.

```bash
rabbitmq-plugins enable rabbitmq_event_exchange
```

You bind a queue (for example with `user.#` or `queue.*`) and forward events to your logging or SIEM system. It's useful for audit trails ("who deleted this queue?") and security monitoring.

## 356: What are message interceptors?

Added in RabbitMQ 4.2, message interceptors let the broker run code on incoming and outgoing messages for AMQP 1.0, AMQP 0-9-1 and MQTT. Two built-in interceptors exist: one that adds timestamps to outgoing messages, and one that sets the MQTT client ID of the publisher on the message.

They replace older, more limited mechanisms (like the incoming timestamp setting) and give a single place for this kind of logic. Custom interceptors are written in Erlang as plugins, so most teams use the built-in ones and keep custom logic in their apps.

## 357: What do you need to run RabbitMQ well on Kubernetes?

- A StatefulSet with stable pod names and persistent volumes (the Cluster Operator does this).
- Fast storage classes; quorum queues and streams are sensitive to disk latency.
- Pod anti-affinity or topology spread so nodes land on different hosts and zones.
- Pod disruption budgets so a drain doesn't take down a majority.
- Memory limits that match the RabbitMQ watermark settings.
- Enough termination grace period for a clean shutdown.
- Probes that are light enough not to kill healthy but busy nodes.
- Upgrade logic that checks quorum safety before restarting each pod (the operator handles this).

Running without the operator is possible but means doing all of this yourself.

## 358: What does rabbitmq-upgrade await_online_quorum_plus_one do?

It waits until every quorum queue (and Khepri) on the cluster has at least a majority plus one replica online. That means one more node can safely be stopped without any quorum queue losing its majority.

It's used in rolling restarts: after a node comes back, you run this before restarting the next one. Skipping it can cause queues to lose their majority if you restart nodes too quickly, before replicas have caught up. The `check_if_node_is_quorum_critical` health check answers the same question for one node.

## 359: How did Kubernetes peer discovery change in RabbitMQ 4.1?

Before 4.1, the Kubernetes peer discovery plugin queried the Kubernetes API to find other pods, which sometimes led to several clusters forming on first start when pods started at the same time.

Since 4.1, it no longer uses the Kubernetes API. It relies on the StatefulSet naming: every node joins the pod with index 0 (like `rabbit-server-0`) as the seed node. This is simpler and avoids the multiple-cluster problem. The change is backwards compatible with existing configs.

## 360: What can go wrong with RabbitMQ networking in Kubernetes?

- **Node names:** if nodes use pod IPs or non-stable hostnames, a restarted pod becomes a new node. Use the StatefulSet's stable DNS names via a headless service.
- **DNS caching:** stale DNS after pod restarts can make nodes or CLI tools fail to connect.
- **Stream clients:** they connect to a specific node's advertised host and port, which must be reachable from clients (configure `advertised_host` or use a load balancer-aware setup).
- **Idle timeouts** on cloud load balancers cutting AMQP connections.
- **Network policies** that block port 25672 or 4369 between pods.

## 361: Why do stream clients have trouble behind a load balancer?

Stream protocol clients first connect to any node to get metadata, then connect directly to the node hosting the stream leader (for publishing) or a replica (for consuming), using the host and port that node advertises.

Behind a load balancer or NAT, the advertised address (often an internal hostname) isn't reachable from outside, or the load balancer sends the connection to the wrong node. Solutions: configure `stream.advertised_host` and `stream.advertised_port` per node, expose each node separately, or use the client's address resolver feature to always go through the load balancer and retry until it lands on the right node.

## 362: What issues come up with client automatic recovery and topology recovery?

Many clients (Java, .NET) recover connections and re-create channels, consumers, queues and bindings automatically. Common problems:

- **Server-named queues** get a new name after recovery, so bindings and anything that stored the old name (like a `replyTo`) break.
- **Exclusive queues** lose their messages on recovery.
- Recovery can re-declare objects with old arguments that now conflict with a policy or a changed queue.
- Unacked messages from before the disconnect are redelivered, and acking them with old delivery tags fails.
- Publishes during the outage are lost unless the client buffers them.

Test recovery explicitly (kill connections from the UI) to see how your client and code behave.

## 363: How can publisher retries cause duplicates, and how do you limit them?

If a publisher sends a message and the connection drops before the confirm arrives, the publisher can't know whether the broker stored it. Republishing is the safe choice, but if the broker did store it, consumers now get it twice.

To limit the impact:

- Use a stable `messageId` across retries, so consumers can de-duplicate.
- For streams, use publisher de-duplication (publisher name + publishing ID), which lets the broker drop duplicates.
- Make consumers idempotent anyway, since duplicates also come from redeliveries.

You can't remove duplicates entirely with a broker in the middle; you can only make them harmless.

## 364: How do you make side effects like sending emails idempotent?

The email provider won't remember that you already sent an email, so you need to track it:

- Record "email for event X sent" in a DB with a unique key on the event ID, before or as part of sending.
- If the record exists, skip.
- If the provider supports an idempotency key, pass the event ID.

There's still a small gap: if the process crashes after the provider accepted the email but before you saved the record, a retry sends it again. For emails that's usually acceptable; for payments, use the provider's idempotency keys, which are designed to close this gap.

## 365: How do you keep strict order in a pipeline with retries and multiple steps?

Strict order across retries means you can't move a failed message out of the way. Options:

- One queue per key range with single active consumer, and retry in place (backoff inside the consumer) until it succeeds or you stop the line and alert.
- If a message is moved to a DLQ, also park every later message for the same key (a "parking lot" per key) until the failed one is fixed.
- Use versioning so consumers can ignore stale updates and order doesn't need to be strict.

Strict ordering always costs throughput or availability, so first confirm that the business really needs it and for what scope.

## 366: When do you need global ordering and how can you get it?

Global ordering (every message in exactly the order published) is rarely needed; per-entity ordering is enough for most systems. When you do need it:

- One publisher (or a single sequencer) on one channel.
- One queue (quorum queue for safety).
- One active consumer (single active consumer for failover).
- No priorities, no requeueing that reorders, retry in place.

This caps throughput at what one consumer can handle. A stream also gives a single ordered log that every consumer reads in the same order.

## 367: Design an order processing flow using RabbitMQ.

A reasonable design:

1. The Orders API saves the order and an outbox row in one transaction, then the relay publishes `order.created` to the `orders.events` topic exchange with confirms.
2. Payment service consumes from `payments.order-created` (quorum queue), charges the card with an idempotency key and publishes `payment.completed` or `payment.failed`.
3. Inventory service reserves stock on `order.created`, publishes `stock.reserved` or `stock.failed`.
4. An order saga (orchestrator or the Orders service) listens to these events and updates the order status, issuing compensations (refund, release stock) when something fails.
5. Notification service listens to `order.*` and `payment.*` to send emails.

Each queue has a DLX, a delivery limit and alerts. All consumers de-duplicate by message ID. Order ID is the routing-key suffix, so per-order sharding is possible later.

## 368: Design an email notification service with RabbitMQ.

- Producers publish `notification.email.requested` commands with the template, recipient and data (no full HTML, just template ID and variables).
- An `emails` quorum queue with prefetch tuned to the provider's rate limit and a few worker instances.
- Workers render and send, using the event ID for de-duplication.
- Temporary errors (provider 5xx, 429) go to delayed retry with backoff; permanent errors (invalid address) go to a DLQ and are recorded.
- A separate high-priority queue (or priority) for password resets and OTPs, so a newsletter blast doesn't delay them.
- Expiration on time-sensitive messages like OTPs.
- Metrics on queue depth, send rate, failure rate.

## 369: A queue has 10 million messages and growing. What do you do?

1. **Stop the bleeding:** check alarms, disk and memory. If close to limits, set a temporary length limit or slow producers.
2. **Find the cause:** are consumers running? Erroring? Slow because of a dependency? Is a producer misbehaving (a loop)?
3. **Fix consumers** if they're failing (poison message -> DLQ, bug -> fix and deploy).
4. **Scale consumers** if the dependency can take it, and tune prefetch.
5. **Decide what the messages are worth:** if they're stale or duplicates (from a buggy producer), purge or shovel them aside rather than processing all of them.
6. **Afterwards:** add alerts on queue depth and consumer count, length limits, and capacity planning.

Don't restart nodes in a panic; recovery of a huge queue can take a long time.

## 370: Consumers keep crashing on the same message. What do you do?

That's a poison message loop. Short term:

- Find the message (unacked or redelivered counts, consumer logs).
- Move it out of the way: if it's a quorum queue, the delivery limit will dead-letter it eventually; otherwise reject it to a DLQ or temporarily set a policy with a low `delivery-limit`.

Long term:

- Catch all errors in the handler; never let one message crash the process.
- Validate payloads and send invalid ones to a DLQ immediately.
- Keep a delivery limit on all quorum queues.
- Alert on redelivery rate and DLQ size.

## 371: A memory alarm fires in production. What do you do?

1. Check which node and what's using memory (`memory_breakdown`).
2. If it's message bodies (binary): find queues with large backlogs or many unacked messages, and get consumers draining them. Remember publishers are blocked, so consumers must keep running on separate connections.
3. If it's connections or channels: look for a client with a connection or channel leak and fix or block it.
4. If it's management stats: reduce stats collection or per-object metrics.
5. If it's real load: add memory or nodes, and spread queues.

Raising the watermark is a quick fix only if there's real headroom; otherwise the OS may kill the process.

## 372: A disk alarm fires. What do you do?

1. Check free disk on all nodes and which directories are growing (quorum queue logs, streams, classic message store, logs).
2. Look for long queues, stuck unacked messages blocking quorum log truncation, or streams without retention.
3. Drain or purge what you safely can, fix stuck consumers, set stream retention.
4. Expand the volume if needed (cloud volumes can often be resized online).
5. Raise `disk_free_limit` only as part of a fix, not instead of one.

Prevent it with alerts on disk usage, length limits on queues and retention on streams. Don't delete files from the data directory by hand.

## 373: The number of connections spikes and the broker gets slow. What do you check?

- Connection churn rate in metrics: are clients connecting and disconnecting in a loop? Often a client failing to connect (bad credentials, protocol error) retries without backoff.
- Which app: check connection names and source IPs.
- A recent deploy that opens a connection per request.
- Autoscaling that started many pods at once.

Fix: add backoff to reconnection logic, reuse connections, set user/vhost connection limits to contain one bad client, and block or scale down the offending app while fixing it.

## 374: Messages were lost after a broker restart. What went wrong?

Possible causes:

- The queue was non-durable or the messages were transient.
- Publishers didn't use confirms, so messages in flight during the crash were lost.
- Classic queue on a node whose disk was lost or replaced.
- The node got a new name/hostname and came up with an empty data directory (common in containers without a fixed hostname).
- Messages were exclusive or auto-delete queues.
- Length limits with `drop-head` or TTL removed them.

Fix by using quorum queues, persistent messages, confirms, stable node names and persistent volumes.

## 375: Consumers process some messages twice. How do you investigate and fix it?

Find out where duplicates come from:

- **Redeliveries:** consumer crashes, consumer timeouts, channel errors (like double acks) or nack with requeue. Check the `redelivered` flag and `x-delivery-count`, and look at channel close logs.
- **Publisher retries:** the same business event published twice with different message IDs. Check producer logs around connection drops.
- **Multiple queues:** a consumer bound to two queues that both receive the event.
- **Outbox relay** publishing a row twice after a crash.

Fix the obvious bugs (double acks, long processing hitting timeouts), and add idempotency with a stable message ID so duplicates have no effect.

## 376: One slow consumer is affecting other workloads on the same broker. What can you do?

- Check if it holds many unacked messages (large prefetch). Lower prefetch so other consumers on the same queue get work.
- If its queue is huge and its leader shares a node with busy queues, move leaders or rebalance.
- Put it in its own vhost with limits, or on a separate cluster if it's really noisy.
- Separate slow and fast work into different queues so slow jobs don't delay fast ones.
- Fix the slowness itself (timeouts on external calls, batching DB writes).

The broker can isolate queues from each other fairly well; usually the "noise" is a shared dependency or node resources like disk.

## 377: One node in a 3-node cluster goes down. What happens and what do you do?

What happens:

- Clients on that node reconnect elsewhere.
- Quorum queues with leaders on that node elect new leaders on the remaining two; they keep working with 2 of 3 replicas.
- Khepri still has a majority, so metadata changes keep working.
- Classic queues on that node are unavailable.

What to do: find out why it failed, bring it back or replace it. A returning node catches up automatically. If you replace it with a new node, add it to the cluster, grow quorum queues onto it, remove the old node with `rabbitmqctl forget_cluster_node`, and then rebalance leaders. While running on 2 nodes, you have no fault tolerance left, so treat it as urgent.

## 378: Two nodes of a 3-node cluster are down. What happens?

The remaining node has no majority:

- Khepri can't commit, so no metadata changes (no new queues, users, bindings).
- Quorum queues with replicas on the lost nodes can't commit new messages or deliveries.
- Clients may still connect, but most operations fail or hang.
- Classic queues on the surviving node may still work.

The fix is to bring at least one more node back. Forcing the single node to continue alone is a last resort that risks data loss and needs careful steps from the docs. This scenario is why you spread nodes across zones and use pod disruption budgets.

## 379: You need to push events to thousands of individual users. Should you create a queue per user?

Probably not for a large or growing user base. Each queue costs memory and management overhead, and queues per user often get left behind when users disconnect.

Better options:

- One queue per backend instance, and the instance routes to its connected users (WebSocket/SSE), binding only for users currently connected to it.
- MQTT (Web MQTT) where each device subscribes to its own topic; RabbitMQ's native MQTT handles many subscriptions cheaply.
- A stream with filtering when users need to catch up on history.

Queues per user can work for small numbers (a few thousand) with `x-expires` for cleanup.

## 380: How would you design RabbitMQ for a multi-tenant SaaS with very uneven tenants?

- Shared vhost for small tenants, with tenant ID in routing keys and headers.
- Dedicated vhosts (or clusters) for the largest tenants, so their load and backlog don't affect others.
- Fair processing: avoid one queue where a big tenant's 1 million messages sit in front of a small tenant's 10. Use sharded queues by tenant hash, or per-tier queues, so small tenants aren't stuck behind big ones.
- Operator policies to cap queue length per tenant.
- Per-tenant metrics (queue depth by tenant) to spot noisy neighbors.

Pick the model based on the number of tenants and isolation requirements (compliance may force dedicated resources).

## 381: A new service needs all events from the past week. How do you support that?

With normal queues, consumed messages are gone, so a new queue only gets new events. Options:

- Publish events to a **stream** (in addition to, or instead of, queues) with retention of at least a week. The new service reads from `first` or a timestamp, then keeps up with new events.
- Rebuild from the source of truth (database export) and then subscribe to live events, handling the overlap with idempotency.

If replay is a regular need, design for it: events go to a stream with retention, and services that need queue semantics consume from queues fed by the same exchange.

## 382: How would you migrate from a Redis-based job queue (like BullMQ) to RabbitMQ?

1. Map concepts: Bull queues -> RabbitMQ quorum queues; delayed jobs -> TTL/DLX or quorum queue delays; retries/backoff -> delivery limit and retry queues; job results -> reply messages or DB state.
2. Build producers and consumers behind a common interface so you can switch per job type.
3. Run both systems in parallel: new jobs go to RabbitMQ, old Bull jobs drain.
4. Move job types one by one, watching metrics.
5. Replace Bull-specific features you used (repeatable jobs -> a scheduler, job progress -> DB updates).

The main reasons to migrate are usually durability, replication, routing to many consumers and language-agnostic consumers.

## 383: Compare RabbitMQ and Kafka in depth.

|                      | RabbitMQ                                                                           | Kafka                                                    |
| -------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Model                | Broker pushes messages from queues; messages deleted after ack (streams keep them) | Distributed log; consumers pull and track offsets        |
| Routing              | Rich: exchanges, bindings, patterns, headers                                       | By topic and partition only                              |
| Per-message features | Acks, redelivery, TTL, priorities, DLX, delays                                     | None per message; retries are an app concern             |
| Ordering             | Per queue; per partition in super streams                                          | Per partition                                            |
| Replay               | Streams only                                                                       | Built in                                                 |
| Throughput           | High; streams very high                                                            | Very high                                                |
| Ops                  | Simpler for small/medium setups                                                    | More moving parts, but huge ecosystem (Connect, Streams) |

Choose RabbitMQ for task queues, complex routing, RPC and per-message handling. Choose Kafka for large-scale event streaming, long retention and stream processing. Many companies run both.

## 384: How do RabbitMQ streams compare to Kafka?

Similarities: append-only replicated logs, offsets, retention by size and time, partitioning (super streams), consumer groups (single active consumer per partition), very high throughput.

Differences:

- Streams live next to queues in the same broker, so one system can do both task queues and logs.
- RabbitMQ's routing (exchanges) can feed streams.
- Kafka's ecosystem (Kafka Connect, Kafka Streams, ksqlDB, tooling) is much larger.
- Kafka is built for very large clusters and many TB of retained data; RabbitMQ streams work well but are less proven at that scale.
- RabbitMQ 4.2 adds SQL filter expressions for AMQP 1.0 consumers on streams, which Kafka doesn't have server-side.

## 385: How does RabbitMQ compare to Amazon SQS and SNS?

- **SQS** is a fully managed queue with no servers to run, practically unlimited scale and pay per request. But it has no routing, limited message size (up to 1 MiB, with bigger payloads via S3), a visibility timeout model instead of acks over a connection, and FIFO queues with throughput limits.
- **SNS** adds pub/sub fan-out to SQS queues, Lambda, HTTP and more.
- **RabbitMQ** gives rich routing, lower latency, push delivery, priorities, many protocols, streams and works the same on any cloud or on premises, but you (or a provider like Amazon MQ or CloudAMQP) run it.

On AWS, SNS + SQS is often the easiest choice; RabbitMQ is chosen for its features, portability or existing knowledge.

## 386: How does RabbitMQ compare to NATS?

NATS is a lightweight messaging system focused on simplicity and low latency. Core NATS is fire-and-forget pub/sub (no persistence); JetStream adds persistence, streams, acks and replay.

RabbitMQ has richer routing (exchange types, headers), per-message features (DLX, TTL, priorities, delivery limits) and protocol support (AMQP, MQTT, STOMP). NATS is simpler to run, very fast and good for service-to-service communication and edge setups. Choose based on which features you need and what your team knows.

## 387: What are the trade-offs of managed RabbitMQ (Amazon MQ, CloudAMQP) vs self-hosted?

**Managed:** no servers to patch, automatic backups of config, monitoring and upgrades handled (more or less), quick to start. But you get less control over configuration and plugins (Amazon MQ doesn't allow many community plugins), upgrades follow the provider's schedule, and it can be expensive at scale.

**Self-hosted (VMs or Kubernetes with the operator):** full control over versions, plugins, tuning and cost, but you need people who know how to run, monitor and upgrade it.

For most teams without RabbitMQ experts, managed is a good default; at large scale or with special needs, self-hosting can pay off.

## 388: How do SQL filter expressions on streams work?

Since RabbitMQ 4.2, AMQP 1.0 consumers can attach a SQL-like filter when subscribing to a stream, for example on message properties and application properties:

```sql
region = 'eu' AND amount > 100 AND type IN ('order.created', 'order.paid')
```

The broker evaluates it per message and only sends matching messages to the consumer. Unlike Bloom filter stream filtering, it's exact, so the consumer doesn't need to recheck. It still reads the stream data on the broker side, so very selective filters on huge streams cost broker CPU. It's only available over AMQP 1.0.

## 389: How do super stream partitions and consumer groups keep ordering?

The producer picks a partition for each message using a routing strategy: a hash of a key (like the customer ID) or an exact key mapped to a partition. All messages with the same key go to the same partition, which is a normal stream, so they're in order there.

Consumers join with the same name and single active consumer enabled. RabbitMQ assigns each partition to one active consumer in the group, and rebalances when consumers join or leave. So each key is read by one consumer in order. Adding partitions later changes the key mapping, so plan the partition count up front.

## 390: How does publisher de-duplication work in streams?

A stream producer sets a unique producer name and gives each message an increasing publishing ID (a sequence number). The broker remembers, per producer name, the highest publishing ID it stored. If a message comes with an ID less than or equal to that, the broker drops it as a duplicate.

After a restart, the producer asks the broker for the last stored ID for its name and continues from there. This only works if publishing IDs are strictly increasing and the producer name is stable, and only one producer instance uses a given name at a time. It's available with the stream protocol clients.

## 391: How is stream retention evaluated?

Streams store data in segment files. Retention (`max-length-bytes`, `max-age`) is checked when a new segment is created: if the stream is over the size limit, or the newest message in the oldest segment is older than `max-age`, the oldest segments are deleted.

So retention is approximate: a stream can be up to about one segment over the size limit, and messages can live a bit longer than `max-age`. The current (active) segment is never deleted. A consumer reading from an offset that has been deleted starts from the oldest available data.

## 392: How does flow control work for stream consumers?

Stream protocol consumers use a credit system: the client gives the broker a number of credits, and each credit lets the broker send one chunk of messages. The client gives more credit as it processes chunks. This keeps a slow consumer from being flooded.

Over AMQP 0-9-1, prefetch plays this role, and acks just return credit (nothing is deleted). Over AMQP 1.0, link credit is used. Consumers that lag far behind don't hurt others, since they just read older data from disk, but they put more load on the disk.

## 393: When would you use a stream instead of fan-out to many quorum queues?

Fan-out to N quorum queues stores each message N times (each queue keeps its own replicated log) and does N times the work for every publish. With many consumers (say 50 services or analytics jobs), that's expensive.

A stream stores each message once (with replicas) and lets any number of consumers read it independently, with their own offsets. Use a stream when there are many consumers of the same data, when consumers need replay, or when some consumers read in batches. Stick with quorum queues when each consumer needs per-message acks, retries, DLX and competing consumers.

## 394: What are the trade-offs between the consistent hash exchange and x-modulus-hash?

- **Consistent hash exchange** (plugin): uses a hash ring with weights per binding. When you add or remove a queue, only a fraction of keys move. Supports hashing on a header or message property, not just the routing key.
- **x-modulus-hash** (core since 4.3): hash modulo the number of bound queues. Simpler, no weights. Adding or removing a queue remaps most keys.

If your number of shards changes and you care about keys staying put (for per-key ordering or caching), use the consistent hash exchange. If the shard count is fixed, either works.

## 395: What are local shovels?

Added in RabbitMQ 4.2, local shovels use the `local` protocol option instead of `amqp091` or `amqp10`. Instead of opening a real AMQP connection to the same cluster, the shovel moves messages using intra-cluster communication.

That gives higher throughput and uses fewer resources than a normal shovel looping back over TCP. It only works within one cluster, for example moving messages between queues, replaying DLQs or migrating classic queues to quorum queues on the same cluster.

## 396: How do you configure federation and avoid loops?

Define an upstream and a policy that applies federation to matching exchanges:

```bash
rabbitmqctl set_parameter federation-upstream us-east \
  '{"uri":"amqps://fed:secret@rabbit-us-east.internal","max-hops":1,"ack-mode":"on-confirm"}'

rabbitmqctl set_policy federate-events '^events\.' \
  '{"federation-upstream":"us-east"}' --apply-to exchanges
```

In a setup where regions federate from each other, messages could bounce back and forth. Federation adds an `x-received-from` header and uses `max-hops` to stop messages from crossing more links than allowed. With `max-hops: 1`, a message federated from A to B isn't federated again from B to C. Set `ack-mode: on-confirm` for safe delivery.

## 397: What ack modes does Shovel support?

- `on-confirm` (default): the shovel acks the source message only after the destination confirms it. Safe, at-least-once.
- `on-publish`: acks the source after publishing to the destination, without waiting for confirms. Faster, can lose messages if the destination fails.
- `no-ack`: consumes with auto-ack. Fastest, messages can be lost.

Use `on-confirm` unless you have a measured reason not to. With prefetch (`src-prefetch-count`) you control how many messages are in flight.

## 398: How does direct reply-to work internally and what are its limits?

When a client consumes from `amq.rabbitmq.reply-to`, no real queue is created. When it publishes a request with `replyTo: amq.rabbitmq.reply-to`, RabbitMQ replaces it with a special name that encodes the client's channel and node. A server publishing to that name sends the reply straight to that channel.

Limits:

- The consumer must use auto-ack.
- If the requester's channel is gone, the reply is dropped.
- Replies aren't stored, so there's no buffering if the client is slow.
- With the `mandatory` flag, since 4.2 the reply-to name is treated as a queue and requester presence isn't checked, so no `basic.return` is sent.

It's ideal for short, synchronous RPC calls where the caller would give up anyway if it disappeared.

## 399: Why can RPC over RabbitMQ be hard to scale?

- Every call needs a request message, a reply message and state on the caller (pending requests), so it's heavier than an HTTP call.
- Timeouts must be handled carefully; late replies and lost requests are common under load.
- A backlog in the request queue adds latency to every call, which is often worse than failing fast.
- If callers retry on timeout, you get duplicate requests and more load during an incident.
- Debugging is harder than for HTTP.

It works well for moderate load, when you want the broker to load balance workers or bridge networks. For high-volume synchronous APIs, HTTP or gRPC is usually a better fit.

## 400: How does RabbitMQ perform with very large fan-out?

Fan-out to many queues multiplies work: the channel routes to N queues, and each queue stores and delivers its copy. Classic queues on one node can share message bodies, but quorum queues each write their own copy to their logs.

RabbitMQ 4.2 improved fanout throughput significantly, but with hundreds of queues per message, consider:

- A stream that many consumers read.
- Fewer queues with more consumers each.
- Federation or a hierarchy of exchanges if the fan-out spans clusters.
- Classic queues for non-critical fan-out (like cache invalidation), since they're cheaper.

## 401: What is cluster_exchange_limit?

`cluster_exchange_limit`, added in RabbitMQ 4.2, caps the total number of exchanges in the cluster. When reached, declaring a new exchange fails.

It protects the cluster from apps that accidentally create exchanges dynamically (for example, one per user or per request), which can grow metadata and slow down the cluster. Together with vhost `max-queues`, it's a safety net against topology explosions.

## 402: How does topic exchange routing work internally?

Topic exchanges store bindings in a trie structure, where each level is a word of the binding key, with special handling for `*` and `#`. Routing walks the trie with the words of the routing key, following exact matches and wildcard branches.

This makes routing fast even with many bindings, but `#` in the middle of patterns (like `a.#.b`) can cause more branches to be explored. If you have hundreds of thousands of bindings on one topic exchange, routing and binding changes become noticeably more expensive, so it's better to split by domain into several exchanges.

## 403: Does message size affect how RabbitMQ stores and handles messages?

Yes:

- Classic queues embed small messages in the queue index and put larger ones in the shared message store. The threshold is set by `queue_index_embed_msgs_below` (4 KB by default).
- Large messages use more memory while in flight and slow down replication for quorum queues and streams.
- Very large messages can cause latency spikes for other messages on the same connection, since frames are sent in order.
- `max_message_size` caps size (16 MiB by default in recent versions).

In general, many small messages cost more CPU per byte, and very large messages cost more memory and latency. A few KB to a few hundred KB is the comfortable range.

## 404: How do you maximize publisher throughput?

- Keep many messages in flight with async confirms; don't wait per message.
- Use several channels or connections if one channel is a bottleneck (each channel is one process on the broker).
- Spread messages over several queues so routing and storage run in parallel.
- Use fast disks for durable workloads.
- Keep messages reasonably small; consider batching several logical records into one message if that suits consumers.
- Avoid `mandatory` and per-message work (like routing to many queues) unless needed.

Measure with PerfTest to know the ceiling, and monitor connection state for `flow`.

## 405: How do you maximize consumer throughput?

- Set prefetch high enough to cover network latency (for fast handlers 100-300 or more).
- Ack in batches with `multiple` when processing is sequential.
- Process concurrently within the consumer (async I/O, or worker threads/processes).
- Add consumers on different connections and machines.
- Shard hot queues.
- Make the handler fast: batch DB writes, reuse connections to downstream systems.

Often the limit is not RabbitMQ but the downstream (database). Measure where time goes before tuning the broker.

## 406: How does prefetch work differently with quorum queues?

Quorum queues use credit-based delivery to consumers internally, and prefetch maps to that credit. A few differences from classic queues:

- Global QoS isn't supported, only per-consumer prefetch.
- Since 4.1, quorum queue log reads are offloaded to the channel process, which improved consumer throughput.
- Unacked messages in a quorum queue keep the Raft log from being truncated, so very high prefetch with slow consumers makes disk usage grow.

A moderate prefetch (tens to a few hundred) usually gives the best balance with quorum queues.

## 407: What is a redelivery storm and how do you avoid it?

A redelivery storm happens when many messages come back to the queue at once and are delivered again, often causing the same failure. Examples:

- A consumer with a huge prefetch crashes, returning thousands of messages.
- Consumers hit the consumer timeout together because a dependency got slow.
- A shared dependency is down and every message fails and is requeued immediately.

The broker and the dependency both get hammered. Avoid it with moderate prefetch, delayed retries with backoff instead of immediate requeue, delivery limits, circuit breakers in consumers (stop consuming while a dependency is down) and timeouts lower than the consumer timeout.

## 408: Why is nack with requeue=true dangerous at scale?

A requeued message goes straight back to the head of a classic queue and can be delivered again within milliseconds. If the failure is permanent or the dependency is down, the consumer spins: deliver, fail, requeue, deliver again, using CPU on both sides and flooding logs.

With quorum queues, the delivery limit eventually stops it, but with the default of 20 attempts that can still be a lot of wasted work per message. Better: requeue only for errors you expect to clear in milliseconds, and use delayed retries for everything else.

## 409: How do unacked messages affect broker memory?

Unacked messages must stay available until they're acked or the consumer goes away. For classic queues, metadata about each unacked message is kept in memory, and bodies may be too. For quorum queues, the queue state tracks them, and they block log truncation.

Thousands of consumers with large prefetch values and slow processing can hold millions of messages unacked, using memory and disk without anyone working on most of them. Keep prefetch modest, and watch the unacked count as a key metric.

## 410: What was x-cancel-on-ha-failover?

It was a consumer argument for classic mirrored queues. When the mirrored queue's master failed and a mirror was promoted, consumers with `x-cancel-on-ha-failover: true` got a cancel notification so they knew a failover happened (and could check for duplicates or lost messages).

Mirrored queues are removed since 4.0, so this argument is legacy. Quorum queues handle failover transparently: consumers keep their subscription, and unacked messages from the old leader are redelivered.

## 411: What does tracing cost in production, and what are the alternatives?

The firehose and `rabbitmq_tracing` copy every message published and delivered in a vhost, which roughly doubles or more the work for each message and can fill disks with trace logs. Enabling it on a busy production vhost can cause flow control or alarms.

Better options for production:

- OpenTelemetry tracing in the clients, with sampling.
- Logging message IDs and routing keys (not bodies) in producers and consumers.
- The event exchange for topology and connection events.
- Short, targeted firehose sessions on a quiet vhost or with a narrow binding.

## 412: How do you detect slow consumers using metrics?

Look at:

- **Consumer utilization** (or consumer capacity) per queue: below 100% means the queue often had messages but no consumer able to take them (prefetch full).
- **Unacked messages** growing while the ack rate is flat.
- **Messages ready** growing while consumer count is stable.
- **Ack rate vs publish rate** over time.
- **Time in queue:** if you set timestamps, consumers can report the age of messages when processed.

Client-side metrics (processing duration per message, errors) complete the picture.

## 413: What alerts would you set up for RabbitMQ?

- Memory or disk alarm active (critical)
- Free disk below a threshold well above the alarm limit
- Node down or cluster not having all expected nodes
- Quorum queues without a majority, or not enough online replicas
- Queue with zero consumers that should have some
- Queue depth or message age above a threshold for important queues
- DLQ not empty / growing
- High connection or channel churn
- File descriptors near the limit
- TLS certificates expiring soon
- High redelivery rate

Tie alerts to queues that matter to the business, not every queue.

## 414: How do you plan disk capacity for quorum queues?

Disk usage depends on:

- The backlog you need to absorb: peak messages that can pile up × average size × replicas (each replica stores data on its own node).
- Raft log overhead: operations (enqueue, ack, return) plus segments not yet truncated.
- WAL size (shared, bounded by `raft.wal_max_size_bytes`).
- Snapshots.

A rule of thumb is to plan for several times the raw message size per replica, add headroom for incidents (consumers down for hours), and keep `disk_free_limit` large enough to stop publishers before the disk fills. Test with a realistic backlog to see real usage.

## 415: What does busy_dist_port mean?

`busy_dist_port` is an Erlang warning that the buffer for the distribution connection to another node is full. Inter-node traffic (like quorum queue replication, or a client connected to node A using a queue on node B) is waiting.

It suggests the inter-node link is a bottleneck. Fixes: raise the distribution buffer size (`RABBITMQ_DISTRIBUTION_BUFFER_SIZE`), check network bandwidth and latency between nodes, and reduce cross-node traffic by having clients connect to the node hosting the queue leader where practical.

## 416: What is net_ticktime?

`net_ticktime` is the Erlang setting for how quickly a node decides that another node is unreachable. Nodes send tick messages to each other, and if none arrive for about `net_ticktime` seconds (60 by default), the connection is considered down.

Lowering it detects failures faster but risks false failures on busy or slow networks, which with Raft can cause unneeded leader elections. Raising it makes the cluster slower to react to real failures. Leave the default unless you have a clear reason.

## 417: What is the difference between TCP keepalive and AMQP heartbeats?

- **TCP keepalive** is handled by the OS. Default timers are often very long (2 hours on Linux), it doesn't know about the application, and it can be tuned only per system or socket.
- **AMQP heartbeats** are part of the protocol. Both sides send frames when idle, and either can detect a dead peer within about two intervals, usually a minute or two.

Heartbeats are the main mechanism for detecting dead connections. TCP keepalive can be a useful extra, for example to keep NAT and load balancer sessions alive, but don't rely on it alone.

## 418: Why is creating an exclusive queue per request a bad idea?

Some RPC implementations create a temporary exclusive queue for each request and delete it after the reply. Every request then costs a queue declaration, binding and deletion, which are metadata operations. Since Khepri, metadata changes go through Raft consensus, so they're relatively expensive.

At high request rates this creates huge metadata churn and slows the cluster. Use one reply queue per client (with correlation IDs) or direct reply-to instead.

## 419: How do you notice and fix an uneven distribution of queue leaders across nodes?

Check the management UI (Queues, sorted by node) or metrics for leaders per node. Signs of imbalance: one node with much higher CPU and network use, after a restart or because of `client-local` leader placement with clients connecting to one node.

Fix it with `rabbitmq-queues rebalance quorum`, set `queue_leader_locator = balanced` for new queues, and spread client connections across nodes. Check after each maintenance, since restarts move leaders to the remaining nodes.

## 420: What happens when you change a policy on existing queues?

Policies are re-evaluated when they change, and most keys take effect on existing queues right away: TTL, length limits, DLX settings, federation, and for quorum queues, delivery limit (which since 4.4 also applies to existing queues via policy).

Some things can't be changed by policy at all, like queue type, durability and exclusivity. And remember that only one policy applies to a queue (the highest priority one). Adding a new higher-priority policy with fewer keys removes the settings from the previous one, which can silently drop a DLX or a limit.

## 421: How do you change the type of an existing queue?

You can't change a queue's type in place. You have to migrate:

1. Create a new queue with the new type (new name, or in a new vhost).
2. Bind it like the old one.
3. Move consumers.
4. Move remaining messages with a shovel (local shovels make this cheaper since 4.2).
5. Delete the old queue.

If the queue name must stay the same, you can do it in two hops (old -> temp -> recreate with the same name as quorum -> move back), or use a blue-green cluster where the new cluster has quorum as the default type.

## 422: How do you test RabbitMQ failure scenarios?

In a staging environment with production-like setup:

- Kill a node and check that quorum queues fail over and clients reconnect.
- Close client connections from the UI to test reconnection and topology recovery.
- Fill a disk or lower the watermark to trigger alarms, and check that publishers handle blocking.
- Block network between nodes (network partition).
- Inject poison messages and check DLQ handling.
- Slow down a dependency to trigger timeouts and redelivery.
- Do a rolling upgrade while traffic runs.

Watch for lost messages (count published vs consumed), duplicates and recovery time.

## 423: How do you design exchanges for a large microservices system?

- One topic exchange per bounded context (domain) that publishes events, owned by that team.
- Clear routing key convention, documented as part of the event contract.
- Consumers own their queues; queue names start with the consumer service name.
- A separate exchange or direct queues for commands.
- Internal exchanges for routing layers when you need audit copies or cross-cutting consumers.
- Policies by naming pattern for DLX, limits and delivery limits.
- No shared "one exchange for everything", which makes ownership and permissions hard.

Keep topology in code (definitions, operator resources or app declarations) and review changes like API changes.

## 424: How do you keep event consumers compatible when event schemas evolve?

- Follow the "tolerant reader" rule: consumers ignore unknown fields and don't fail on missing optional ones.
- Producers only make additive changes in a version; breaking changes get a new event type or version header.
- Run both versions in parallel during migration: publish v1 and v2, or use a routing key suffix like `order.created.v2`.
- Use contract tests (consumer-driven contracts) so a producer change that breaks a consumer fails in CI.
- Keep event documentation and examples in a central place.

## 425: How do you document message-based APIs?

AsyncAPI is the standard for describing event-driven APIs, similar to OpenAPI for HTTP. It describes channels (exchanges and routing keys), messages, payload schemas and bindings for AMQP.

```yaml
asyncapi: 3.0.0
info:
  title: Orders events
  version: 1.0.0
channels:
  orderCreated:
    address: order.created
    messages:
      orderCreated:
        payload:
          type: object
          properties:
            orderId: { type: string }
            total: { type: number }
```

Generated docs and code from AsyncAPI help teams find what events exist and what they contain.

## 426: How do you validate messages at the consumer?

Validate the payload against a schema as the first step in the handler, and treat invalid messages as permanent failures:

```js
import { z } from "zod";

const OrderCreated = z.object({
  orderId: z.string(),
  total: z.number().nonnegative(),
});

await channel.consume("billing.order-created", async (msg) => {
  const result = OrderCreated.safeParse(JSON.parse(msg.content.toString()));
  if (!result.success) {
    await sendToDlq(msg, new Error(result.error.message));
    return;
  }
  await bill(result.data);
  channel.ack(msg);
});
```

This stops bad data from going deeper into your system and makes the DLQ clearly show what was wrong.

## 427: How do you design end-to-end backpressure in a system using RabbitMQ?

Pressure should flow back to the source instead of piling up somewhere invisible:

- Consumers limit concurrency (prefetch) to what downstream can handle.
- Queues have length limits with `reject-publish`, so publishers get nacks when consumers can't keep up.
- Publishers use confirms and a bounded in-flight window, and react to nacks and `connection.blocked` by slowing down.
- The API layer returns 429 or 503 to callers when it can't publish.
- Alarms (memory, disk) are the last line of defense, not the normal mechanism.

Without this, a slow consumer leads to a huge queue, then a disk alarm, then all publishers on the cluster blocked.

## 428: How do you handle time-sensitive messages that become useless after a while?

- Set a TTL (per queue or per message) so stale messages are removed or dead-lettered instead of processed.
- Include a timestamp or deadline in the message, and have consumers skip messages past the deadline (TTL in classic queues isn't checked until the head of the queue).
- For things like price quotes or "user is typing", consider transient messages or a non-replicated classic queue for speed.
- For OTPs or password reset emails, a short TTL avoids sending a code that has already expired.

## 429: Is a queue length limit enough protection against unbounded growth?

It's a good safety net but has trade-offs:

- With `drop-head`, the oldest messages are dropped (or dead-lettered), which may be your most important ones. Dead-lettering them to a DLQ without a limit just moves the problem.
- With `reject-publish`, publishers must handle nacks, or messages are lost at the source.
- A limit sized for normal operation may be too small during an expected spike.

Combine limits with alerts on queue depth well before the limit, enough consumer capacity and clear decisions on which messages are OK to drop.

## 430: How do you build tooling around dead letter queues?

DLQs only help if someone looks at them. Useful tooling:

- An alert when a DLQ has messages or grows.
- A dashboard or internal page listing DLQ messages with headers (error, original queue, time, attempt count).
- Actions: replay one or all (shovel back to the original exchange), edit and replay, discard, export.
- Grouping by error type, so 10,000 messages from one bug show up as one problem.
- Retention: messages older than N days are archived or dropped.

Some teams store failed messages in a database instead of a DLQ for easier querying, with the DLQ consumer writing them there.

## 431: How do you make work processing fair between tenants or customers?

A single FIFO queue serves whoever published first, so one big customer can delay everyone. Options:

- Shard by tenant into several queues (consistent hash on tenant ID) with consumers on each, so a big tenant fills only its shard.
- Separate queues per tier (free, paid, enterprise) with dedicated consumers.
- Per-tenant rate limits on the publishing side.
- For a small number of tenants, a queue per tenant with consumers that round-robin across queues.

Pick based on how many tenants you have and how strict fairness must be.

## 432: When would you not use quorum queues?

- Temporary, exclusive or per-connection queues (they can't be quorum queues anyway).
- Data you can lose where speed matters more than safety, like cache invalidation, metrics or live updates.
- Very large numbers of queues (hundreds of thousands), where per-queue Raft overhead is too high.
- Single-node setups, where replication isn't possible and classic queues are lighter.
- Replay or many-reader use cases, where streams fit better.
- Workloads relying on features quorum queues don't have, such as global QoS.

## 433: What are some hard production issues teams commonly hit with RabbitMQ?

- Disk filling up because quorum queue logs couldn't be truncated due to one stuck unacked message.
- Publishers blocked by an alarm while consumers shared their connection, so queues never drained.
- Connection storms from clients reconnecting without backoff after a network blip.
- Node names changing in containers, making nodes come up "empty".
- Poison messages looping with `requeue: true`.
- Upgrades failing because feature flags weren't enabled, or a deprecated feature was still in use.
- Leaders all on one node after a restart, overloading it.
- Huge per-user queue counts slowing down the whole cluster.

## 434: How do you load test an application's messaging, not just the broker?

Broker benchmarks (PerfTest) show RabbitMQ's limits, but the app usually breaks first. To test the app:

- Generate realistic events through the real producers (or a replay of production traffic).
- Run real consumers against real dependencies (or good stand-ins).
- Measure end-to-end latency (publish timestamp to processing done), queue depth over time and error rates.
- Test the peak rate you expect plus a margin, and a sustained backlog drain (e.g. consumers down for 1 hour, then started).
- Watch both the broker (memory, disk, flow) and the dependencies (DB load).

## 435: What does "advertised host" mean for streams and why is it needed?

Stream clients connect directly to specific nodes. A node tells clients how to reach it using its advertised host and port, which default to its hostname and the stream port. If clients can't reach that address (different network, NAT, Kubernetes), they fail to connect.

```ini
stream.advertised_host = rabbit-0.example.com
stream.advertised_port = 5552
```

Set these per node to addresses clients can reach, or use a client-side address resolver that always connects through a known endpoint.

## 436: How do you handle schema changes in topology without downtime?

Treat topology changes like database migrations:

- Additive changes first: new exchange, new queue, new binding. Old consumers keep working.
- Move producers and consumers to the new topology gradually.
- Remove the old parts only after nothing uses them (no consumers, no publishes for a while).
- Use policies for settings so changes don't require recreating queues.
- Automate it (operator resources, Terraform, definition imports) and test it in staging.

Avoid changing a queue's arguments in app code without a migration plan, since apps will start failing with `PRECONDITION_FAILED`.

## 437: What does the RabbitMQ Terraform provider or Topology Operator bring compared to app-declared topology?

- **Review and audit:** changes go through pull requests.
- **Least privilege:** apps don't need `configure` permission.
- **Consistency:** every environment has the same topology.
- **Drift detection:** the tool can show when someone changed something by hand.

The downside is coordination: a new queue needs an infrastructure change before the app can use it. Many teams combine both: shared exchanges, users and policies managed centrally, and service-owned queues declared by the apps.

## 438: How do you decide between choreography and orchestration with RabbitMQ?

- **Choreography** (services react to each other's events): loose coupling, no central component, easy to add new reactions. But the overall flow is spread over many services and hard to see or change, and failures need compensating events everywhere.
- **Orchestration** (one service sends commands and tracks state): the flow is in one place, easier to monitor, timeout and change. But the orchestrator is coupled to all participants.

A common approach is choreography for simple notifications ("order created, do your thing") and orchestration for business-critical multi-step processes like checkout or onboarding.

## 439: How would you explain prefetch, acks and redelivery together in a failure scenario?

Say a consumer has prefetch 10, gets messages 1-10, acks 1-6 and crashes while working on 7.

- Messages 1-6 are done and gone.
- Messages 7-10 were delivered but not acked, so when the connection closes, RabbitMQ returns them to the queue with `redelivered = true` (quorum queues also increment `x-delivery-count`).
- Another consumer gets them. Message 7 might have been half-processed, so it must be idempotent.
- If message 7 caused the crash, it'll crash the next consumer too, until the delivery limit sends it to the DLX.

That's at-least-once delivery in practice.

## 440: How does RabbitMQ use Raft in more than one place?

Raft (via the Ra library) is used for:

- **Quorum queues:** each queue is its own Raft cluster with a leader and followers.
- **Khepri:** the metadata store is a Raft cluster over all nodes.
- **Streams:** the stream coordinator, which manages stream leaders and replicas, uses Ra (the data itself is replicated by Osiris, not Raft).

So a 3-node cluster with 1000 quorum queues runs 1000+ Raft groups. Ra shares one WAL per node across them, batching writes, which is what makes so many Raft groups practical.

## 441: What's new in RabbitMQ 4.4 that's worth knowing?

Highlights of 4.4 (October 2026):

- Delayed message support in quorum queues.
- The `delivery-limit` policy now applies to existing quorum queues.
- `x-stream-initial-offset` for streams, `x-name-prefix` for server-named queues, stable `x-modulus-hash` routing.
- A new v2 format for the classic queue shared message store (no downgrade to 4.3 after it's used).
- Unix domain socket listeners, `max_connections` / `max_channels` settings, per-protocol connection limits.
- Security: passive declares need permissions, stronger password hashing options, stricter OIDC discovery checks.
- STOMP as a standalone protocol, per-vhost limits on MQTT retained messages.
- Support for Erlang 28 and 29.

## 442: What changed in RabbitMQ 4.0 that interviewers often ask about?

- Classic mirrored queues removed; quorum queues are the replicated queue type.
- AMQP 1.0 became a core protocol, on port 5672 with no plugin.
- Quorum queues got a default delivery limit of 20, and message priorities.
- Khepri became fully supported (as an opt-in at that time).
- Many deprecated features moved closer to removal.

4.0 marked the start of a cleanup of old features, continued by 4.3 (Mnesia, partition handling, CQv1 and lazy mode removed).

## 443: How would you explain RabbitMQ's architecture in a system design interview?

Keep it at the right level:

- **Clients** (producers and consumers) open long-lived connections with channels.
- **Exchanges** receive messages and route them by type and bindings to **queues**.
- **Queues** come in three types: classic (single node), quorum (Raft-replicated, safe) and streams (replicated logs with replay).
- A **cluster** of 3 or 5 nodes shares metadata through Khepri (Raft), and replicated queues survive node failures.
- **Reliability** comes from publisher confirms, manual acks, durable replicated queues and DLX.
- **Scaling** is by more consumers, more queues (sharding) and more nodes.

Then tie it to the problem: what's published, who consumes, what happens on failure, and how you handle duplicates and ordering.

## 444: How do you secure AMQP connections that come from outside your network, like IoT devices?

- Use TLS only (5671, 8883 for MQTT), with modern ciphers.
- Prefer client certificates or short-lived tokens (OAuth 2) per device instead of shared passwords.
- Separate vhost (or cluster) for external clients, with tight permissions and topic permissions.
- Connection limits per user and per protocol, plus `max_message_size`.
- Put a TCP proxy or load balancer in front that can rate-limit and block abusive IPs.
- Don't expose management or inter-node ports.
- Forward device messages to internal systems with shovels or federation, so internal clusters aren't reachable from outside.

## 445: How do you think about message durability costs when designing a system?

Every safety feature has a cost:

- Persistent messages need disk writes; quorum queues need writes on several nodes.
- Publisher confirms add latency per message (hidden by keeping many in flight).
- Manual acks need an extra frame per message (or batch).
- Replication uses network bandwidth.

Decide per message type: payments and orders get quorum queues, confirms and idempotent consumers; metrics and live UI updates can use transient messages in classic queues with auto-ack. Using maximum safety everywhere wastes resources; using none anywhere loses data.

## 446: What is the difference between at-most-once and at-least-once dead lettering, and when does it matter?

With at-most-once (default), the source queue removes the message and sends it to the DLX in one step without confirmation. If the target queue is down or full, the message is lost.

With at-least-once (quorum queues only), the source queue keeps the message until the DLX target confirms it, retrying if needed. It can produce duplicates in the DLQ, but nothing is lost.

It matters when the DLQ is part of your reliability story (for example, failed payments must never vanish). For non-critical queues, at-most-once is fine and cheaper.

## 447: What are Unix domain socket listeners in RabbitMQ 4.4 good for?

RabbitMQ 4.4 lets AMQP listeners bind to a Unix domain socket instead of a TCP port. Clients on the same machine connect through the socket file.

This avoids TCP overhead for local clients (like sidecars or co-located services), and access can be controlled with file permissions. It's a niche feature, useful in setups where the broker and some clients always run on the same host.

## 448: Why does RabbitMQ refuse to start with a missing auth backend plugin since 4.2?

Since 4.2, if `rabbitmq.conf` configures an authentication or authorization backend that comes from a plugin (for example `auth_backends.1 = ldap`), but that plugin isn't enabled, the node refuses to start.

Before, the node could start and then fail every login, or silently fall back in confusing ways. Failing at boot makes the configuration mistake obvious right away. When upgrading, make sure the `enabled_plugins` file matches the backends in your config.

## 449: How do you decide how many queues and consumers a new feature needs?

Ask:

- How many distinct consumers (services) need the messages? One queue per consumer service.
- Does order matter, and at what scope? Per-key ordering may need sharded queues with single active consumer.
- What's the expected rate and processing time? Rate × processing time = concurrency needed, which tells you consumers × prefetch.
- Are there different priorities or SLAs? Separate queues for urgent and bulk work.
- Do consumers need replay? Consider a stream.

Start simple (one queue per consumer service, a few consumers), measure, and shard only when one queue becomes the bottleneck.

## 450: What would you check before going live with a RabbitMQ-based system?

- 3+ nodes across zones, persistent storage, stable node names
- Quorum queues for important data, DLX and delivery limits everywhere
- Publisher confirms, manual acks, idempotent consumers
- Reconnection with backoff in all clients, graceful shutdown
- Separate publisher and consumer connections, named connections
- Policies for limits and DLX; operator policies as a safety net
- Memory and disk alarm thresholds set for production
- TLS, least-privilege users, `guest` removed, management UI private
- Prometheus metrics, dashboards and alerts (queue depth, consumers, alarms, DLQs)
- A tested upgrade procedure and a definitions backup
- Load and failure tests done in staging
