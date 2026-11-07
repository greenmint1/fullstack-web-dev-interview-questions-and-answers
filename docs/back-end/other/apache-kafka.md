# Apache Kafka Interview Questions and Answers

450 Apache Kafka interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Apache Kafka 4.x (up to 4.3): KRaft only (no ZooKeeper), the new consumer group protocol, share groups (Queues for Kafka), tiered storage and the current Java clients. Older setups like ZooKeeper mode and the classic rebalance protocol are mentioned where they still matter, since you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Apache Kafka?](#1-what-is-apache-kafka)
- [2: What are common use cases for Kafka?](#2-what-are-common-use-cases-for-kafka)
- [3: What is an event or record in Kafka?](#3-what-is-an-event-or-record-in-kafka)
- [4: What is a topic?](#4-what-is-a-topic)
- [5: What is a partition?](#5-what-is-a-partition)
- [6: What is an offset?](#6-what-is-an-offset)
- [7: What is a broker?](#7-what-is-a-broker)
- [8: What is a Kafka cluster?](#8-what-is-a-kafka-cluster)
- [9: What is a producer?](#9-what-is-a-producer)
- [10: What is a consumer?](#10-what-is-a-consumer)
- [11: What is a consumer group?](#11-what-is-a-consumer-group)
- [12: How is Kafka different from a traditional message queue like RabbitMQ?](#12-how-is-kafka-different-from-a-traditional-message-queue-like-rabbitmq)
- [13: What is KRaft?](#13-what-is-kraft)
- [14: What happened to ZooKeeper in Kafka 4.0?](#14-what-happened-to-zookeeper-in-kafka-40)
- [15: What is a controller in Kafka?](#15-what-is-a-controller-in-kafka)
- [16: What is replication in Kafka?](#16-what-is-replication-in-kafka)
- [17: What are leader and follower replicas?](#17-what-are-leader-and-follower-replicas)
- [18: What is the ISR (in-sync replicas)?](#18-what-is-the-isr-in-sync-replicas)
- [19: What is the replication factor?](#19-what-is-the-replication-factor)
- [20: How long does Kafka keep messages?](#20-how-long-does-kafka-keep-messages)
- [21: Does Kafka delete messages after they are consumed?](#21-does-kafka-delete-messages-after-they-are-consumed)
- [22: What is a record key used for?](#22-what-is-a-record-key-used-for)
- [23: How does Kafka guarantee message ordering?](#23-how-does-kafka-guarantee-message-ordering)
- [24: What is a record header?](#24-what-is-a-record-header)
- [25: What is a record timestamp?](#25-what-is-a-record-timestamp)
- [26: What is serialization in Kafka?](#26-what-is-serialization-in-kafka)
- [27: Which serializers come with the Kafka Java client?](#27-which-serializers-come-with-the-kafka-java-client)
- [28: What is a bootstrap server?](#28-what-is-a-bootstrap-server)
- [29: How do you start Kafka locally with Docker?](#29-how-do-you-start-kafka-locally-with-docker)
- [30: How do you start Kafka from the downloaded archive?](#30-how-do-you-start-kafka-from-the-downloaded-archive)
- [31: How do you create a topic from the command line?](#31-how-do-you-create-a-topic-from-the-command-line)
- [32: How do you list and describe topics?](#32-how-do-you-list-and-describe-topics)
- [33: How do you send messages with the console producer?](#33-how-do-you-send-messages-with-the-console-producer)
- [34: How do you read messages with the console consumer?](#34-how-do-you-read-messages-with-the-console-consumer)
- [35: How do you write a simple producer in Java?](#35-how-do-you-write-a-simple-producer-in-java)
- [36: How do you write a simple consumer in Java?](#36-how-do-you-write-a-simple-consumer-in-java)
- [37: How do you produce and consume messages from Node.js?](#37-how-do-you-produce-and-consume-messages-from-nodejs)
- [38: What does the poll() method do?](#38-what-does-the-poll-method-do)
- [39: What does committing an offset mean?](#39-what-does-committing-an-offset-mean)
- [40: What is auto commit?](#40-what-is-auto-commit)
- [41: Where does Kafka store committed offsets?](#41-where-does-kafka-store-committed-offsets)
- [42: What does auto.offset.reset do?](#42-what-does-autooffsetreset-do)
- [43: What is consumer lag?](#43-what-is-consumer-lag)
- [44: How do you check consumer group lag?](#44-how-do-you-check-consumer-group-lag)
- [45: What is a rebalance?](#45-what-is-a-rebalance)
- [46: What happens if a group has more consumers than partitions?](#46-what-happens-if-a-group-has-more-consumers-than-partitions)
- [47: Can two consumer groups read the same topic?](#47-can-two-consumer-groups-read-the-same-topic)
- [48: What is the acks setting on the producer?](#48-what-is-the-acks-setting-on-the-producer)
- [49: What delivery guarantees does Kafka offer?](#49-what-delivery-guarantees-does-kafka-offer)
- [50: What is at-least-once delivery?](#50-what-is-at-least-once-delivery)
- [51: What is at-most-once delivery?](#51-what-is-at-most-once-delivery)
- [52: What is exactly-once in Kafka?](#52-what-is-exactly-once-in-kafka)
- [53: What is an idempotent producer?](#53-what-is-an-idempotent-producer)
- [54: What is batching in the producer?](#54-what-is-batching-in-the-producer)
- [55: What do batch.size and linger.ms do?](#55-what-do-batchsize-and-lingerms-do)
- [56: What compression types does Kafka support?](#56-what-compression-types-does-kafka-support)
- [57: What is a log segment?](#57-what-is-a-log-segment)
- [58: What is log compaction?](#58-what-is-log-compaction)
- [59: What is a tombstone message?](#59-what-is-a-tombstone-message)
- [60: What is cleanup.policy?](#60-what-is-cleanuppolicy)
- [61: What are retention.ms and retention.bytes?](#61-what-are-retentionms-and-retentionbytes)
- [62: What is the default maximum message size?](#62-what-is-the-default-maximum-message-size)
- [63: Can you change the number of partitions of a topic?](#63-can-you-change-the-number-of-partitions-of-a-topic)
- [64: How do you delete a topic?](#64-how-do-you-delete-a-topic)
- [65: What is the Admin client?](#65-what-is-the-admin-client)
- [66: What is Kafka Connect?](#66-what-is-kafka-connect)
- [67: What are source and sink connectors?](#67-what-are-source-and-sink-connectors)
- [68: What is Kafka Streams?](#68-what-is-kafka-streams)
- [69: What are a stream and a table in Kafka Streams?](#69-what-are-a-stream-and-a-table-in-kafka-streams)
- [70: What is a Serde?](#70-what-is-a-serde)
- [71: What is MirrorMaker 2?](#71-what-is-mirrormaker-2)
- [72: What is a schema registry?](#72-what-is-a-schema-registry)
- [73: Why use Avro or Protobuf instead of plain JSON?](#73-why-use-avro-or-protobuf-instead-of-plain-json)
- [74: What is a dead letter queue?](#74-what-is-a-dead-letter-queue)
- [75: What is the __consumer_offsets topic?](#75-what-is-the-__consumer_offsets-topic)
- [76: What are internal topics?](#76-what-are-internal-topics)
- [77: What ports does Kafka use by default?](#77-what-ports-does-kafka-use-by-default)
- [78: What is a listener?](#78-what-is-a-listener)
- [79: What is advertised.listeners?](#79-what-is-advertisedlisteners)
- [80: Why can a client reach the bootstrap server but then fail to connect?](#80-why-can-a-client-reach-the-bootstrap-server-but-then-fail-to-connect)
- [81: What is a partition leader election?](#81-what-is-a-partition-leader-election)
- [82: What happens when a broker goes down?](#82-what-happens-when-a-broker-goes-down)
- [83: What is min.insync.replicas?](#83-what-is-mininsyncreplicas)
- [84: What is unclean leader election?](#84-what-is-unclean-leader-election)
- [85: What is the high watermark?](#85-what-is-the-high-watermark)
- [86: What is the log end offset?](#86-what-is-the-log-end-offset)
- [87: Is the Kafka producer thread-safe?](#87-is-the-kafka-producer-thread-safe)
- [88: Is the Kafka consumer thread-safe?](#88-is-the-kafka-consumer-thread-safe)
- [89: What is the group coordinator?](#89-what-is-the-group-coordinator)
- [90: What is a heartbeat in a consumer group?](#90-what-is-a-heartbeat-in-a-consumer-group)
- [91: What is session.timeout.ms?](#91-what-is-sessiontimeoutms)
- [92: What is max.poll.interval.ms?](#92-what-is-maxpollintervalms)
- [93: What is max.poll.records?](#93-what-is-maxpollrecords)
- [94: How do you subscribe to several topics or a pattern?](#94-how-do-you-subscribe-to-several-topics-or-a-pattern)
- [95: What is the difference between subscribe() and assign()?](#95-what-is-the-difference-between-subscribe-and-assign)
- [96: How do you read a topic from the beginning?](#96-how-do-you-read-a-topic-from-the-beginning)
- [97: What does seek() do?](#97-what-does-seek-do)
- [98: How does the producer choose a partition?](#98-how-does-the-producer-choose-a-partition)
- [99: What is the sticky partitioner?](#99-what-is-the-sticky-partitioner)
- [100: What happens when you send a record with a null key?](#100-what-happens-when-you-send-a-record-with-a-null-key)
- [101: What happens when you send a record with a null value?](#101-what-happens-when-you-send-a-record-with-a-null-value)
- [102: What is the difference between a synchronous and an asynchronous send?](#102-what-is-the-difference-between-a-synchronous-and-an-asynchronous-send)
- [103: What does flush() do on the producer?](#103-what-does-flush-do-on-the-producer)
- [104: Why should you close the producer and consumer?](#104-why-should-you-close-the-producer-and-consumer)
- [105: What is client.id?](#105-what-is-clientid)
- [106: What is group.id?](#106-what-is-groupid)
- [107: What are the main configuration files in a Kafka install?](#107-what-are-the-main-configuration-files-in-a-kafka-install)
- [108: What is node.id?](#108-what-is-nodeid)
- [109: What is process.roles?](#109-what-is-processroles)
- [110: What is a cluster ID and why do you format storage?](#110-what-is-a-cluster-id-and-why-do-you-format-storage)
- [111: What is a topic configuration override?](#111-what-is-a-topic-configuration-override)
- [112: How do you change a topic's config at runtime?](#112-how-do-you-change-a-topics-config-at-runtime)
- [113: What is kafka-configs.sh used for?](#113-what-is-kafka-configssh-used-for)
- [114: What is the difference between a topic and a queue?](#114-what-is-the-difference-between-a-topic-and-a-queue)
- [115: What are share groups (Queues for Kafka)?](#115-what-are-share-groups-queues-for-kafka)
- [116: What is the difference between a consumer group and a share group?](#116-what-is-the-difference-between-a-consumer-group-and-a-share-group)
- [117: What is publish/subscribe messaging?](#117-what-is-publishsubscribe-messaging)
- [118: Why is Kafka fast?](#118-why-is-kafka-fast)
- [119: What is a commit log?](#119-what-is-a-commit-log)
- [120: What does it mean that Kafka is distributed?](#120-what-does-it-mean-that-kafka-is-distributed)
- [121: How do you scale Kafka horizontally?](#121-how-do-you-scale-kafka-horizontally)
- [122: What language is Kafka written in and which clients exist?](#122-what-language-is-kafka-written-in-and-which-clients-exist)
- [123: What is librdkafka?](#123-what-is-librdkafka)
- [124: Which Java version does Kafka 4.x need?](#124-which-java-version-does-kafka-4x-need)
- [125: What are KIPs?](#125-what-are-kips)
- [126: What is event streaming?](#126-what-is-event-streaming)
- [127: What is event-driven architecture?](#127-what-is-event-driven-architecture)
- [128: What is a message broker?](#128-what-is-a-message-broker)
- [129: What is a rack in Kafka?](#129-what-is-a-rack-in-kafka)
- [130: What is the log.dirs setting?](#130-what-is-the-logdirs-setting)
- [131: How should you name topics?](#131-how-should-you-name-topics)
- [132: Why does Kafka warn about mixing dots and underscores in topic names?](#132-why-does-kafka-warn-about-mixing-dots-and-underscores-in-topic-names)
- [133: How do you get the earliest and latest offsets of a topic?](#133-how-do-you-get-the-earliest-and-latest-offsets-of-a-topic)
- [134: What is an offset reset?](#134-what-is-an-offset-reset)
- [135: How do you reset offsets for a consumer group?](#135-how-do-you-reset-offsets-for-a-consumer-group)
- [136: What is a producer callback?](#136-what-is-a-producer-callback)
- [137: What does RecordMetadata contain?](#137-what-does-recordmetadata-contain)
- [138: What is a record batch on disk?](#138-what-is-a-record-batch-on-disk)
- [139: What is cluster metadata?](#139-what-is-cluster-metadata)
- [140: How do clients learn about cluster metadata?](#140-how-do-clients-learn-about-cluster-metadata)
- [141: What is the difference between Apache Kafka and Confluent Platform?](#141-what-is-the-difference-between-apache-kafka-and-confluent-platform)
- [142: What are managed Kafka services?](#142-what-are-managed-kafka-services)
- [143: Which tools can you use to browse topics in a web UI?](#143-which-tools-can-you-use-to-browse-topics-in-a-web-ui)
- [144: What is JMX in Kafka?](#144-what-is-jmx-in-kafka)
- [145: What is the difference between Kafka and a database?](#145-what-is-the-difference-between-kafka-and-a-database)
- [146: Can Kafka be used as the source of truth?](#146-can-kafka-be-used-as-the-source-of-truth)
- [147: What is a poison pill message?](#147-what-is-a-poison-pill-message)
- [148: Why can producer retries create duplicates?](#148-why-can-producer-retries-create-duplicates)
- [149: What is delivery.timeout.ms?](#149-what-is-deliverytimeoutms)
- [150: What are the main parts of the Kafka ecosystem?](#150-what-are-the-main-parts-of-the-kafka-ecosystem)

### Moderate Questions (151-300)

- [151: How do you choose the number of partitions for a topic?](#151-how-do-you-choose-the-number-of-partitions-for-a-topic)
- [152: How does the default partitioner pick a partition for keyed records?](#152-how-does-the-default-partitioner-pick-a-partition-for-keyed-records)
- [153: How do you write a custom partitioner?](#153-how-do-you-write-a-custom-partitioner)
- [154: What goes wrong when you add partitions to a topic with keyed data?](#154-what-goes-wrong-when-you-add-partitions-to-a-topic-with-keyed-data)
- [155: How do you configure a producer so it does not lose data?](#155-how-do-you-configure-a-producer-so-it-does-not-lose-data)
- [156: How do acks=all and min.insync.replicas work together?](#156-how-do-acksall-and-mininsyncreplicas-work-together)
- [157: What does enable.idempotence guarantee and what does it not?](#157-what-does-enableidempotence-guarantee-and-what-does-it-not)
- [158: How does max.in.flight.requests.per.connection affect ordering?](#158-how-does-maxinflightrequestsperconnection-affect-ordering)
- [159: What is the difference between retries and delivery.timeout.ms?](#159-what-is-the-difference-between-retries-and-deliverytimeoutms)
- [160: What happens when the producer's buffer.memory is full?](#160-what-happens-when-the-producers-buffermemory-is-full)
- [161: How do you tune a producer for throughput?](#161-how-do-you-tune-a-producer-for-throughput)
- [162: How do you tune a producer for low latency?](#162-how-do-you-tune-a-producer-for-low-latency)
- [163: Which compression type should you choose?](#163-which-compression-type-should-you-choose)
- [164: Where is compression applied: producer, broker or topic?](#164-where-is-compression-applied-producer-broker-or-topic)
- [165: How do you send large messages?](#165-how-do-you-send-large-messages)
- [166: How do you commit offsets manually?](#166-how-do-you-commit-offsets-manually)
- [167: What is the difference between commitSync and commitAsync?](#167-what-is-the-difference-between-commitsync-and-commitasync)
- [168: How do you commit specific offsets?](#168-how-do-you-commit-specific-offsets)
- [169: Why is the committed offset the next offset to read and not the last one processed?](#169-why-is-the-committed-offset-the-next-offset-to-read-and-not-the-last-one-processed)
- [170: How do you handle a rebalance with ConsumerRebalanceListener?](#170-how-do-you-handle-a-rebalance-with-consumerrebalancelistener)
- [171: What is the eager rebalance protocol?](#171-what-is-the-eager-rebalance-protocol)
- [172: What is cooperative rebalancing?](#172-what-is-cooperative-rebalancing)
- [173: Which partition assignment strategies exist in the classic protocol?](#173-which-partition-assignment-strategies-exist-in-the-classic-protocol)
- [174: What is the new consumer group protocol from KIP-848?](#174-what-is-the-new-consumer-group-protocol-from-kip-848)
- [175: How do you enable the new consumer group protocol?](#175-how-do-you-enable-the-new-consumer-group-protocol)
- [176: What is static group membership?](#176-what-is-static-group-membership)
- [177: What causes frequent rebalances and how do you fix them?](#177-what-causes-frequent-rebalances-and-how-do-you-fix-them)
- [178: What is CommitFailedException and why does it happen?](#178-what-is-commitfailedexception-and-why-does-it-happen)
- [179: How do you process messages in parallel with a consumer?](#179-how-do-you-process-messages-in-parallel-with-a-consumer)
- [180: How do you stop a consumer cleanly?](#180-how-do-you-stop-a-consumer-cleanly)
- [181: How do you pause and resume consuming?](#181-how-do-you-pause-and-resume-consuming)
- [182: How do you start consuming from a specific time?](#182-how-do-you-start-consuming-from-a-specific-time)
- [183: What are fetch.min.bytes and fetch.max.wait.ms?](#183-what-are-fetchminbytes-and-fetchmaxwaitms)
- [184: What are max.partition.fetch.bytes and fetch.max.bytes?](#184-what-are-maxpartitionfetchbytes-and-fetchmaxbytes)
- [185: What is isolation.level?](#185-what-is-isolationlevel)
- [186: How do you use a share consumer?](#186-how-do-you-use-a-share-consumer)
- [187: Which acknowledgement types does a share consumer support?](#187-which-acknowledgement-types-does-a-share-consumer-support)
- [188: What happens when a record in a share group keeps failing?](#188-what-happens-when-a-record-in-a-share-group-keeps-failing)
- [189: When should you use a share group instead of a consumer group?](#189-when-should-you-use-a-share-group-instead-of-a-consumer-group)
- [190: How do you create topics with the Admin API?](#190-how-do-you-create-topics-with-the-admin-api)
- [191: How do you check a consumer group's offsets and lag with the Admin API?](#191-how-do-you-check-a-consumer-groups-offsets-and-lag-with-the-admin-api)
- [192: How do you set up a KRaft cluster with separate controllers?](#192-how-do-you-set-up-a-kraft-cluster-with-separate-controllers)
- [193: How many controllers should a KRaft cluster have?](#193-how-many-controllers-should-a-kraft-cluster-have)
- [194: What is combined mode and when is it OK to use?](#194-what-is-combined-mode-and-when-is-it-ok-to-use)
- [195: How do you check the status of the KRaft quorum?](#195-how-do-you-check-the-status-of-the-kraft-quorum)
- [196: What is a dynamic controller quorum?](#196-what-is-a-dynamic-controller-quorum)
- [197: What is the __cluster_metadata topic?](#197-what-is-the-__cluster_metadata-topic)
- [198: How do you migrate from ZooKeeper to KRaft?](#198-how-do-you-migrate-from-zookeeper-to-kraft)
- [199: How do you upgrade a Kafka cluster?](#199-how-do-you-upgrade-a-kafka-cluster)
- [200: What are metadata.version and kafka-features.sh?](#200-what-are-metadataversion-and-kafka-featuressh)
- [201: How do you reassign partitions between brokers?](#201-how-do-you-reassign-partitions-between-brokers)
- [202: What is the preferred leader and how do you rebalance leadership?](#202-what-is-the-preferred-leader-and-how-do-you-rebalance-leadership)
- [203: How do you add a broker to a cluster?](#203-how-do-you-add-a-broker-to-a-cluster)
- [204: How do you remove a broker from a cluster?](#204-how-do-you-remove-a-broker-from-a-cluster)
- [205: What is rack awareness and how do you configure it?](#205-what-is-rack-awareness-and-how-do-you-configure-it)
- [206: How can consumers read from the nearest replica?](#206-how-can-consumers-read-from-the-nearest-replica)
- [207: How do you set up log compaction for a topic?](#207-how-do-you-set-up-log-compaction-for-a-topic)
- [208: What are min.compaction.lag.ms and max.compaction.lag.ms?](#208-what-are-mincompactionlagms-and-maxcompactionlagms)
- [209: How long do tombstones stay in a compacted topic?](#209-how-long-do-tombstones-stay-in-a-compacted-topic)
- [210: When would you use cleanup.policy=compact,delete?](#210-when-would-you-use-cleanuppolicycompactdelete)
- [211: When does Kafka roll a new log segment?](#211-when-does-kafka-roll-a-new-log-segment)
- [212: How does time-based retention actually delete data?](#212-how-does-time-based-retention-actually-delete-data)
- [213: What is tiered storage?](#213-what-is-tiered-storage)
- [214: How do you enable tiered storage?](#214-how-do-you-enable-tiered-storage)
- [215: How do you organize topics in a real project?](#215-how-do-you-organize-topics-in-a-real-project)
- [216: Should different event types go into one topic or many?](#216-should-different-event-types-go-into-one-topic-or-many)
- [217: How do you handle schema evolution?](#217-how-do-you-handle-schema-evolution)
- [218: What compatibility modes does a schema registry offer?](#218-what-compatibility-modes-does-a-schema-registry-offer)
- [219: How do you use Avro with the Java producer?](#219-how-do-you-use-avro-with-the-java-producer)
- [220: What wire format do schema registry serializers use?](#220-what-wire-format-do-schema-registry-serializers-use)
- [221: How do you implement retries in a consumer?](#221-how-do-you-implement-retries-in-a-consumer)
- [222: How do you build a dead letter topic yourself?](#222-how-do-you-build-a-dead-letter-topic-yourself)
- [223: How do you deal with a poison pill that fails deserialization?](#223-how-do-you-deal-with-a-poison-pill-that-fails-deserialization)
- [224: How do you make a consumer idempotent?](#224-how-do-you-make-a-consumer-idempotent)
- [225: What is the outbox pattern?](#225-what-is-the-outbox-pattern)
- [226: What is change data capture with Kafka?](#226-what-is-change-data-capture-with-kafka)
- [227: What is the difference between standalone and distributed Kafka Connect?](#227-what-is-the-difference-between-standalone-and-distributed-kafka-connect)
- [228: Which internal topics does distributed Kafka Connect use?](#228-which-internal-topics-does-distributed-kafka-connect-use)
- [229: How do you create a connector with the REST API?](#229-how-do-you-create-a-connector-with-the-rest-api)
- [230: What are converters in Kafka Connect?](#230-what-are-converters-in-kafka-connect)
- [231: What are single message transforms?](#231-what-are-single-message-transforms)
- [232: How does error handling work in Kafka Connect?](#232-how-does-error-handling-work-in-kafka-connect)
- [233: How do you scale a connector?](#233-how-do-you-scale-a-connector)
- [234: What is exactly-once support for source connectors?](#234-what-is-exactly-once-support-for-source-connectors)
- [235: How does a Kafka Streams app work in terms of threads and tasks?](#235-how-does-a-kafka-streams-app-work-in-terms-of-threads-and-tasks)
- [236: What is application.id?](#236-what-is-applicationid)
- [237: What are the differences between KStream, KTable and GlobalKTable?](#237-what-are-the-differences-between-kstream-ktable-and-globalktable)
- [238: What are stateless operations in Kafka Streams?](#238-what-are-stateless-operations-in-kafka-streams)
- [239: How do you do aggregations in Kafka Streams?](#239-how-do-you-do-aggregations-in-kafka-streams)
- [240: What is a state store?](#240-what-is-a-state-store)
- [241: What is a changelog topic?](#241-what-is-a-changelog-topic)
- [242: What is a repartition topic?](#242-what-is-a-repartition-topic)
- [243: Which window types does Kafka Streams support?](#243-which-window-types-does-kafka-streams-support)
- [244: What is a grace period?](#244-what-is-a-grace-period)
- [245: How do you join streams and tables in Kafka Streams?](#245-how-do-you-join-streams-and-tables-in-kafka-streams)
- [246: What is co-partitioning and why do joins need it?](#246-what-is-co-partitioning-and-why-do-joins-need-it)
- [247: How do you test a Kafka Streams topology?](#247-how-do-you-test-a-kafka-streams-topology)
- [248: What is the Processor API?](#248-what-is-the-processor-api)
- [249: What does suppress() do?](#249-what-does-suppress-do)
- [250: What are interactive queries?](#250-what-are-interactive-queries)
- [251: How do you handle bad records in Kafka Streams?](#251-how-do-you-handle-bad-records-in-kafka-streams)
- [252: How does exactly-once work in Kafka Streams?](#252-how-does-exactly-once-work-in-kafka-streams)
- [253: How do you use transactions in a producer?](#253-how-do-you-use-transactions-in-a-producer)
- [254: What does read_committed actually change for consumers?](#254-what-does-read_committed-actually-change-for-consumers)
- [255: What is transactional.id?](#255-what-is-transactionalid)
- [256: How do you do a consume-transform-produce loop with transactions?](#256-how-do-you-do-a-consume-transform-produce-loop-with-transactions)
- [257: How do you secure Kafka with TLS?](#257-how-do-you-secure-kafka-with-tls)
- [258: Which SASL mechanisms does Kafka support?](#258-which-sasl-mechanisms-does-kafka-support)
- [259: How do you set up SASL/SCRAM?](#259-how-do-you-set-up-saslscram)
- [260: How do ACLs work in Kafka?](#260-how-do-acls-work-in-kafka)
- [261: How do you create ACLs?](#261-how-do-you-create-acls)
- [262: What is the StandardAuthorizer?](#262-what-is-the-standardauthorizer)
- [263: How do you configure a client to connect with SASL_SSL?](#263-how-do-you-configure-a-client-to-connect-with-sasl_ssl)
- [264: What are quotas?](#264-what-are-quotas)
- [265: How do you set quotas?](#265-how-do-you-set-quotas)
- [266: Which broker metrics should you monitor?](#266-which-broker-metrics-should-you-monitor)
- [267: Which producer and consumer metrics should you monitor?](#267-which-producer-and-consumer-metrics-should-you-monitor)
- [268: How do you monitor consumer lag in production?](#268-how-do-you-monitor-consumer-lag-in-production)
- [269: What is an under-replicated partition?](#269-what-is-an-under-replicated-partition)
- [270: What is an offline partition?](#270-what-is-an-offline-partition)
- [271: How do you look inside a log segment file?](#271-how-do-you-look-inside-a-log-segment-file)
- [272: How do you debug a "message too large" error?](#272-how-do-you-debug-a-message-too-large-error)
- [273: How do you debug a consumer that is not receiving messages?](#273-how-do-you-debug-a-consumer-that-is-not-receiving-messages)
- [274: How do you debug a producer that times out?](#274-how-do-you-debug-a-producer-that-times-out)
- [275: What happens to ordering when retries happen without idempotence?](#275-what-happens-to-ordering-when-retries-happen-without-idempotence)
- [276: How do you handle duplicates downstream?](#276-how-do-you-handle-duplicates-downstream)
- [277: How do you delete records from a topic?](#277-how-do-you-delete-records-from-a-topic)
- [278: When should you use LogAppendTime instead of CreateTime?](#278-when-should-you-use-logappendtime-instead-of-createtime)
- [279: How do you use headers for tracing?](#279-how-do-you-use-headers-for-tracing)
- [280: How do you run Kafka on Kubernetes?](#280-how-do-you-run-kafka-on-kubernetes)
- [281: What is Strimzi?](#281-what-is-strimzi)
- [282: How do you set up MirrorMaker 2?](#282-how-do-you-set-up-mirrormaker-2)
- [283: How does MirrorMaker 2 name the copied topics?](#283-how-does-mirrormaker-2-name-the-copied-topics)
- [284: How do you move consumer offsets between clusters?](#284-how-do-you-move-consumer-offsets-between-clusters)
- [285: How does Kafka compare to Amazon SQS and Kinesis?](#285-how-does-kafka-compare-to-amazon-sqs-and-kinesis)
- [286: How do you use Kafka with Spring Boot?](#286-how-do-you-use-kafka-with-spring-boot)
- [287: How do you use Kafka with NestJS?](#287-how-do-you-use-kafka-with-nestjs)
- [288: Which Node.js Kafka clients exist and which should you pick?](#288-which-nodejs-kafka-clients-exist-and-which-should-you-pick)
- [289: How do you shut down a Node.js consumer gracefully?](#289-how-do-you-shut-down-a-nodejs-consumer-gracefully)
- [290: How do you process messages in batches in Node.js?](#290-how-do-you-process-messages-in-batches-in-nodejs)
- [291: How do you write integration tests against a real Kafka?](#291-how-do-you-write-integration-tests-against-a-real-kafka)
- [292: How do you unit test producers and consumers without a broker?](#292-how-do-you-unit-test-producers-and-consumers-without-a-broker)
- [293: Can you get global ordering across a whole topic?](#293-can-you-get-global-ordering-across-a-whole-topic)
- [294: Which retention setting wins: log.retention.hours or log.retention.ms?](#294-which-retention-setting-wins-logretentionhours-or-logretentionms)
- [295: How would you configure a topic that must never lose data?](#295-how-would-you-configure-a-topic-that-must-never-lose-data)
- [296: What happens to offsets of a consumer group that stops running?](#296-what-happens-to-offsets-of-a-consumer-group-that-stops-running)
- [297: How do you delete a consumer group?](#297-how-do-you-delete-a-consumer-group)
- [298: What is the transaction coordinator?](#298-what-is-the-transaction-coordinator)
- [299: What are producer and consumer interceptors?](#299-what-are-producer-and-consumer-interceptors)
- [300: How do you choose the replication factor and min.insync.replicas?](#300-how-do-you-choose-the-replication-factor-and-mininsyncreplicas)

### Advanced Questions (301-450)

- [301: How does Kafka store data on disk?](#301-how-does-kafka-store-data-on-disk)
- [302: What are the other files in a partition directory for?](#302-what-are-the-other-files-in-a-partition-directory-for)
- [303: How do the offset and time indexes work?](#303-how-do-the-offset-and-time-indexes-work)
- [304: How does Kafka use the page cache?](#304-how-does-kafka-use-the-page-cache)
- [305: What is zero-copy and when does it not apply?](#305-what-is-zero-copy-and-when-does-it-not-apply)
- [306: How does a broker handle requests internally?](#306-how-does-a-broker-handle-requests-internally)
- [307: What is request purgatory?](#307-what-is-request-purgatory)
- [308: How does replication work at the protocol level?](#308-how-does-replication-work-at-the-protocol-level)
- [309: How does the high watermark advance?](#309-how-does-the-high-watermark-advance)
- [310: What is the leader epoch and why was it added?](#310-what-is-the-leader-epoch-and-why-was-it-added)
- [311: How does log truncation work after a leader change?](#311-how-does-log-truncation-work-after-a-leader-change)
- [312: What are eligible leader replicas (ELR)?](#312-what-are-eligible-leader-replicas-elr)
- [313: How does the Raft protocol work in KRaft?](#313-how-does-the-raft-protocol-work-in-kraft)
- [314: How do brokers get metadata in KRaft?](#314-how-do-brokers-get-metadata-in-kraft)
- [315: What are metadata snapshots?](#315-what-are-metadata-snapshots)
- [316: What happens when the active controller fails?](#316-what-happens-when-the-active-controller-fails)
- [317: How does broker fencing work in KRaft?](#317-how-does-broker-fencing-work-in-kraft)
- [318: How does the idempotent producer work internally?](#318-how-does-the-idempotent-producer-work-internally)
- [319: How do transactions work internally?](#319-how-do-transactions-work-internally)
- [320: What are transaction markers and control records?](#320-what-are-transaction-markers-and-control-records)
- [321: What is the last stable offset?](#321-what-is-the-last-stable-offset)
- [322: What is a hanging transaction and how do you fix it?](#322-what-is-a-hanging-transaction-and-how-do-you-fix-it)
- [323: What did KIP-890 change for transactions?](#323-what-did-kip-890-change-for-transactions)
- [324: What are the limits of exactly-once in Kafka?](#324-what-are-the-limits-of-exactly-once-in-kafka)
- [325: How does the group coordinator store its state?](#325-how-does-the-group-coordinator-store-its-state)
- [326: How does the KIP-848 protocol assign partitions?](#326-how-does-the-kip-848-protocol-assign-partitions)
- [327: How does the consumer's fetch path work?](#327-how-does-the-consumers-fetch-path-work)
- [328: What are incremental fetch sessions?](#328-what-are-incremental-fetch-sessions)
- [329: How does the log cleaner work?](#329-how-does-the-log-cleaner-work)
- [330: Why might compaction not run, or run slowly?](#330-why-might-compaction-not-run-or-run-slowly)
- [331: How does tiered storage work internally?](#331-how-does-tiered-storage-work-internally)
- [332: What are the trade-offs of tiered storage?](#332-what-are-the-trade-offs-of-tiered-storage)
- [333: How do share groups track the state of records?](#333-how-do-share-groups-track-the-state-of-records)
- [334: How do share groups handle ordering?](#334-how-do-share-groups-handle-ordering)
- [335: How do you size a Kafka cluster?](#335-how-do-you-size-a-kafka-cluster)
- [336: How many partitions can a Kafka cluster handle?](#336-how-many-partitions-can-a-kafka-cluster-handle)
- [337: What are the costs of having too many partitions?](#337-what-are-the-costs-of-having-too-many-partitions)
- [338: How do you deal with a hot partition?](#338-how-do-you-deal-with-a-hot-partition)
- [339: How do you tune a broker for throughput?](#339-how-do-you-tune-a-broker-for-throughput)
- [340: What do num.network.threads and num.io.threads do?](#340-what-do-numnetworkthreads-and-numiothreads-do)
- [341: How do you tune the JVM for Kafka?](#341-how-do-you-tune-the-jvm-for-kafka)
- [342: What OS and filesystem tuning helps Kafka?](#342-what-os-and-filesystem-tuning-helps-kafka)
- [343: Should you use RAID or JBOD for Kafka?](#343-should-you-use-raid-or-jbod-for-kafka)
- [344: What storage choices make sense for Kafka?](#344-what-storage-choices-make-sense-for-kafka)
- [345: How do you tune replication between brokers?](#345-how-do-you-tune-replication-between-brokers)
- [346: How do you limit the impact of partition reassignment?](#346-how-do-you-limit-the-impact-of-partition-reassignment)
- [347: How do you benchmark Kafka?](#347-how-do-you-benchmark-kafka)
- [348: How do you reduce end-to-end latency?](#348-how-do-you-reduce-end-to-end-latency)
- [349: How do you find the cause of high produce latency?](#349-how-do-you-find-the-cause-of-high-produce-latency)
- [350: What does RequestHandlerAvgIdlePercent tell you?](#350-what-does-requesthandleravgidlepercent-tell-you)
- [351: How do you troubleshoot under-replicated partitions?](#351-how-do-you-troubleshoot-under-replicated-partitions)
- [352: What can cause data loss in Kafka?](#352-what-can-cause-data-loss-in-kafka)
- [353: What can cause duplicates in Kafka?](#353-what-can-cause-duplicates-in-kafka)
- [354: How do you get exactly-once results when writing to an external system?](#354-how-do-you-get-exactly-once-results-when-writing-to-an-external-system)
- [355: How do you design a Kafka setup across several data centers?](#355-how-do-you-design-a-kafka-setup-across-several-data-centers)
- [356: What is the difference between active-passive and active-active replication?](#356-what-is-the-difference-between-active-passive-and-active-active-replication)
- [357: How do you fail consumers over to another cluster?](#357-how-do-you-fail-consumers-over-to-another-cluster)
- [358: What is a stretched cluster?](#358-what-is-a-stretched-cluster)
- [359: How do you plan disaster recovery for Kafka?](#359-how-do-you-plan-disaster-recovery-for-kafka)
- [360: How do you back up Kafka?](#360-how-do-you-back-up-kafka)
- [361: How do you secure Kafka end to end?](#361-how-do-you-secure-kafka-end-to-end)
- [362: How does OAUTHBEARER authentication work?](#362-how-does-oauthbearer-authentication-work)
- [363: How do you rotate certificates and credentials without downtime?](#363-how-do-you-rotate-certificates-and-credentials-without-downtime)
- [364: How do you run Kafka for several teams or tenants?](#364-how-do-you-run-kafka-for-several-teams-or-tenants)
- [365: How do you encrypt data at rest in Kafka?](#365-how-do-you-encrypt-data-at-rest-in-kafka)
- [366: How do you handle GDPR deletion requests with Kafka?](#366-how-do-you-handle-gdpr-deletion-requests-with-kafka)
- [367: How do you handle large payloads with the claim check pattern?](#367-how-do-you-handle-large-payloads-with-the-claim-check-pattern)
- [368: How do you design good event schemas?](#368-how-do-you-design-good-event-schemas)
- [369: What is the difference between event notification and event-carried state transfer?](#369-what-is-the-difference-between-event-notification-and-event-carried-state-transfer)
- [370: How do you implement event sourcing with Kafka?](#370-how-do-you-implement-event-sourcing-with-kafka)
- [371: How does CQRS fit with Kafka?](#371-how-does-cqrs-fit-with-kafka)
- [372: How do you implement a saga with Kafka?](#372-how-do-you-implement-a-saga-with-kafka)
- [373: How do you keep per-entity ordering safe across failures and scaling?](#373-how-do-you-keep-per-entity-ordering-safe-across-failures-and-scaling)
- [374: How do you handle out-of-order events?](#374-how-do-you-handle-out-of-order-events)
- [375: How do you implement delayed or scheduled processing with Kafka?](#375-how-do-you-implement-delayed-or-scheduled-processing-with-kafka)
- [376: How do you build retry topics with backoff?](#376-how-do-you-build-retry-topics-with-backoff)
- [377: How do you replay events?](#377-how-do-you-replay-events)
- [378: How do you reprocess data after a bug was found?](#378-how-do-you-reprocess-data-after-a-bug-was-found)
- [379: How do you move to more partitions without breaking key ordering?](#379-how-do-you-move-to-more-partitions-without-breaking-key-ordering)
- [380: How do you rename a topic?](#380-how-do-you-rename-a-topic)
- [381: How do you roll out a breaking schema change without downtime?](#381-how-do-you-roll-out-a-breaking-schema-change-without-downtime)
- [382: How does Kafka Streams assign tasks to instances?](#382-how-does-kafka-streams-assign-tasks-to-instances)
- [383: What are standby replicas in Kafka Streams?](#383-what-are-standby-replicas-in-kafka-streams)
- [384: How does RocksDB work in Kafka Streams and how do you tune it?](#384-how-does-rocksdb-work-in-kafka-streams-and-how-do-you-tune-it)
- [385: How does Kafka Streams restore state and how can you make it faster?](#385-how-does-kafka-streams-restore-state-and-how-can-you-make-it-faster)
- [386: What is the new Kafka Streams rebalance protocol?](#386-what-is-the-new-kafka-streams-rebalance-protocol)
- [387: How does Kafka Streams handle time?](#387-how-does-kafka-streams-handle-time)
- [388: What is a TimestampExtractor?](#388-what-is-a-timestampextractor)
- [389: How do foreign-key joins work in Kafka Streams?](#389-how-do-foreign-key-joins-work-in-kafka-streams)
- [390: What does topology optimization do in Kafka Streams?](#390-what-does-topology-optimization-do-in-kafka-streams)
- [391: How do you scale a Kafka Streams application?](#391-how-do-you-scale-a-kafka-streams-application)
- [392: How do you change a stateful Kafka Streams topology safely?](#392-how-do-you-change-a-stateful-kafka-streams-topology-safely)
- [393: How do you reset a Kafka Streams application?](#393-how-do-you-reset-a-kafka-streams-application)
- [394: When would you use Kafka Streams instead of Apache Flink?](#394-when-would-you-use-kafka-streams-instead-of-apache-flink)
- [395: How do you size Kafka Connect workers and tasks?](#395-how-do-you-size-kafka-connect-workers-and-tasks)
- [396: How does Kafka Connect rebalance work?](#396-how-does-kafka-connect-rebalance-work)
- [397: How do you build a custom connector?](#397-how-do-you-build-a-custom-connector)
- [398: How do you write a custom single message transform?](#398-how-do-you-write-a-custom-single-message-transform)
- [399: What happens when a producer writes to a topic that does not exist?](#399-what-happens-when-a-producer-writes-to-a-topic-that-does-not-exist)
- [400: Why should auto.create.topics.enable be turned off in production?](#400-why-should-autocreatetopicsenable-be-turned-off-in-production)
- [401: How do clients find partition leaders and handle leader changes?](#401-how-do-clients-find-partition-leaders-and-handle-leader-changes)
- [402: What happens during a rolling restart of brokers?](#402-what-happens-during-a-rolling-restart-of-brokers)
- [403: What is controlled shutdown?](#403-what-is-controlled-shutdown)
- [404: What does replica.lag.time.max.ms control?](#404-what-does-replicalagtimemaxms-control)
- [405: What happens when a broker's disk fills up?](#405-what-happens-when-a-brokers-disk-fills-up)
- [406: What happens if one of several log directories fails?](#406-what-happens-if-one-of-several-log-directories-fails)
- [407: What are cordoned log directories?](#407-what-are-cordoned-log-directories)
- [408: How do you handle one slow partition blocking a consumer?](#408-how-do-you-handle-one-slow-partition-blocking-a-consumer)
- [409: How do you avoid rebalance storms in large consumer groups?](#409-how-do-you-avoid-rebalance-storms-in-large-consumer-groups)
- [410: What happens to in-flight work during a rebalance?](#410-what-happens-to-in-flight-work-during-a-rebalance)
- [411: How do you commit offsets correctly when processing asynchronously?](#411-how-do-you-commit-offsets-correctly-when-processing-asynchronously)
- [412: How do you process a partition in parallel while keeping order per key?](#412-how-do-you-process-a-partition-in-parallel-while-keeping-order-per-key)
- [413: What problems do thousands of consumer groups cause?](#413-what-problems-do-thousands-of-consumer-groups-cause)
- [414: How do you decide between keeping state in Kafka or in a database?](#414-how-do-you-decide-between-keeping-state-in-kafka-or-in-a-database)
- [415: How do clock problems affect Kafka?](#415-how-do-clock-problems-affect-kafka)
- [416: What do log.message.timestamp.before.max.ms and after.max.ms do?](#416-what-do-logmessagetimestampbeforemaxms-and-aftermaxms-do)
- [417: What is the zombie producer problem?](#417-what-is-the-zombie-producer-problem)
- [418: How does producer fencing work?](#418-how-does-producer-fencing-work)
- [419: How do you design idempotency keys for events?](#419-how-do-you-design-idempotency-keys-for-events)
- [420: How do you handle backpressure in a Kafka-based pipeline?](#420-how-do-you-handle-backpressure-in-a-kafka-based-pipeline)
- [421: How would you design a topic for an audit log?](#421-how-would-you-design-a-topic-for-an-audit-log)
- [422: How do you test how Kafka behaves under failures?](#422-how-do-you-test-how-kafka-behaves-under-failures)
- [423: How do you measure end-to-end latency?](#423-how-do-you-measure-end-to-end-latency)
- [424: How would you set up alerting for a Kafka cluster?](#424-how-would-you-set-up-alerting-for-a-kafka-cluster)
- [425: How do you plan storage for retention?](#425-how-do-you-plan-storage-for-retention)
- [426: Why are cross-zone costs a concern and how do you reduce them?](#426-why-are-cross-zone-costs-a-concern-and-how-do-you-reduce-them)
- [427: How do quotas and throttling look from the client side?](#427-how-do-quotas-and-throttling-look-from-the-client-side)
- [428: What are the security risks of a default Kafka setup?](#428-what-are-the-security-risks-of-a-default-kafka-setup)
- [429: How do you audit who did what on a Kafka cluster?](#429-how-do-you-audit-who-did-what-on-a-kafka-cluster)
- [430: What are the pitfalls of using a compacted topic as a key-value store?](#430-what-are-the-pitfalls-of-using-a-compacted-topic-as-a-key-value-store)
- [431: How do you build a local cache from a compacted topic?](#431-how-do-you-build-a-local-cache-from-a-compacted-topic)
- [432: How do you join data from two topics without Kafka Streams?](#432-how-do-you-join-data-from-two-topics-without-kafka-streams)
- [433: Scenario: consumers are hours behind after a traffic spike. What do you do?](#433-scenario-consumers-are-hours-behind-after-a-traffic-spike-what-do-you-do)
- [434: Scenario: users report that events are processed out of order. How do you investigate?](#434-scenario-users-report-that-events-are-processed-out-of-order-how-do-you-investigate)
- [435: Scenario: a consumer reprocesses the same messages after every restart. Why?](#435-scenario-a-consumer-reprocesses-the-same-messages-after-every-restart-why)
- [436: Scenario: producers suddenly get NOT_ENOUGH_REPLICAS errors. What is going on?](#436-scenario-producers-suddenly-get-not_enough_replicas-errors-what-is-going-on)
- [437: Scenario: a consumer group rebalances every few minutes. How do you fix it?](#437-scenario-a-consumer-group-rebalances-every-few-minutes-how-do-you-fix-it)
- [438: Scenario: disk usage keeps growing on a compacted topic. Why?](#438-scenario-disk-usage-keeps-growing-on-a-compacted-topic-why)
- [439: Scenario: a read_committed consumer stops making progress but there is data. Why?](#439-scenario-a-read_committed-consumer-stops-making-progress-but-there-is-data-why)
- [440: Scenario: how would you design a notification system with Kafka?](#440-scenario-how-would-you-design-a-notification-system-with-kafka)
- [441: Scenario: how would you design an order processing pipeline with Kafka?](#441-scenario-how-would-you-design-an-order-processing-pipeline-with-kafka)
- [442: Scenario: how would you design a clickstream analytics pipeline?](#442-scenario-how-would-you-design-a-clickstream-analytics-pipeline)
- [443: Scenario: how would you migrate from RabbitMQ to Kafka?](#443-scenario-how-would-you-migrate-from-rabbitmq-to-kafka)
- [444: Scenario: one broker is much busier than the others. What do you do?](#444-scenario-one-broker-is-much-busier-than-the-others-what-do-you-do)
- [445: Scenario: a schema change broke consumers in production. How do you recover and prevent it?](#445-scenario-a-schema-change-broke-consumers-in-production-how-do-you-recover-and-prevent-it)
- [446: What changed in Kafka 4.0 that can break an upgrade?](#446-what-changed-in-kafka-40-that-can-break-an-upgrade)
- [447: What are the notable changes in Kafka 4.1 to 4.3?](#447-what-are-the-notable-changes-in-kafka-41-to-43)
- [448: When should you not use Kafka?](#448-when-should-you-not-use-kafka)
- [449: What are common anti-patterns when using Kafka?](#449-what-are-common-anti-patterns-when-using-kafka)
- [450: How would you explain Kafka's trade-offs in a design review?](#450-how-would-you-explain-kafkas-trade-offs-in-a-design-review)

---

# Easy Questions (1-150)

## 1: What is Apache Kafka?

Apache Kafka is an open source platform for storing and moving streams of events. Applications write events to Kafka, Kafka keeps them on disk for a set time, and other applications read them whenever they want.

It is often called a distributed commit log. It runs as a cluster of servers, it can handle millions of events per second, and it keeps data even after it has been read.

## 2: What are common use cases for Kafka?

- Sending events between microservices (order created, payment received, and so on).
- Collecting logs and metrics from many servers into one place.
- Tracking user activity like clicks and page views.
- Change data capture: copying database changes to other systems.
- Stream processing: filtering, joining and aggregating data as it arrives.
- Feeding data lakes, search indexes and caches.

## 3: What is an event or record in Kafka?

An event (also called a record or message) is one piece of data written to Kafka. It has:

- a **key** (optional),
- a **value** (the actual data, for example a JSON string),
- a **timestamp**,
- optional **headers** (key/value metadata).

Kafka itself does not care about the format. To the broker, the key and value are just bytes.

## 4: What is a topic?

A topic is a named stream of records, like `orders` or `user-signups`. Producers write to a topic and consumers read from it. You can think of it as a folder or a table name for a certain kind of event.

A topic is split into one or more partitions, and its data is kept according to its retention settings.

## 5: What is a partition?

A partition is an ordered, append-only log that holds part of a topic's data. A topic with 6 partitions has 6 separate logs, and they can live on different brokers.

Partitions are how Kafka scales. More partitions let more consumers read in parallel, and they spread the load across brokers. Order is only guaranteed inside one partition, not across the whole topic.

## 6: What is an offset?

An offset is the position of a record inside a partition. The first record gets offset 0, the next one 1, and so on. Offsets never change and are never reused in a partition.

Consumers use offsets to remember how far they have read. A record is uniquely identified by topic + partition + offset.

## 7: What is a broker?

A broker is a single Kafka server. It stores partitions on its disk, accepts writes from producers, and serves reads to consumers. A broker is identified by a numeric `node.id`.

## 8: What is a Kafka cluster?

A cluster is a group of brokers (and controllers) that work together. Partitions and their copies are spread across brokers, so the cluster can keep working when one server fails and can grow by adding more servers.

Production clusters usually have at least 3 brokers.

## 9: What is a producer?

A producer is a client application that writes records to Kafka topics. It decides which partition each record goes to (usually based on the key), batches records together, compresses them, and sends them to the right broker.

## 10: What is a consumer?

A consumer is a client application that reads records from Kafka topics. It asks brokers for new data (pull model), processes it, and keeps track of the offsets it has finished.

## 11: What is a consumer group?

A consumer group is a set of consumers that share the work of reading a topic. They all use the same `group.id`. Kafka assigns each partition to exactly one consumer in the group, so every record is processed once by the group.

If you start more consumers in the same group, the partitions get split between them. Different groups read the same data independently.

```text
Topic "orders" (4 partitions)

Group "billing":   consumer A -> P0, P1   consumer B -> P2, P3
Group "shipping":  consumer C -> P0, P1, P2, P3
```

## 12: How is Kafka different from a traditional message queue like RabbitMQ?

- **Storage:** Kafka keeps records for a retention period even after they are read. A classic queue usually removes a message once it is acknowledged.
- **Reading model:** Kafka consumers track their own position (offset) and can re-read old data. In a queue, the broker tracks each message's state.
- **Scaling:** Kafka scales by partitions. Parallelism inside a consumer group is limited by the partition count.
- **Routing:** RabbitMQ has rich routing (exchanges, bindings). Kafka just has topics and partitions.
- **Throughput:** Kafka is built for very high throughput and replay; RabbitMQ is often simpler for per-message work queues.

Since Kafka 4.2, share groups (Queues for Kafka) add queue-like consumption to Kafka too.

## 13: What is KRaft?

KRaft (Kafka Raft) is the way Kafka manages its own metadata: which topics exist, which broker leads each partition, configs, ACLs and so on. A small set of controller nodes store this metadata in an internal log and agree on it using a Raft-based protocol.

KRaft replaced ZooKeeper. It makes Kafka easier to run (one system instead of two) and lets clusters handle many more partitions.

## 14: What happened to ZooKeeper in Kafka 4.0?

Kafka 4.0 removed ZooKeeper support completely. Every 4.x cluster runs in KRaft mode. The `--zookeeper` options in the command line tools are gone too.

If you have an old ZooKeeper-based cluster, you have to migrate it to KRaft on a 3.x version (3.9 is the last "bridge" release) before you can upgrade to 4.x.

## 15: What is a controller in Kafka?

A controller is a node that manages cluster metadata. In KRaft there is a quorum of controllers (usually 3 or 5). One of them is the **active controller**: it handles things like creating topics, electing partition leaders, and noticing when brokers join or leave. The others are hot standbys that can take over quickly.

A node's role is set with `process.roles` (`broker`, `controller`, or both).

## 16: What is replication in Kafka?

Each partition can have several copies (replicas) on different brokers. If a broker dies, another broker that has a copy can take over, so no data is lost and clients can keep working.

The number of copies is the topic's replication factor.

## 17: What are leader and follower replicas?

For each partition, one replica is the **leader** and the rest are **followers**.

- Producers write to the leader.
- Consumers read from the leader by default (they can also read from a nearby follower if configured).
- Followers keep copying data from the leader.

If the leader's broker fails, the controller picks one of the in-sync followers as the new leader.

## 18: What is the ISR (in-sync replicas)?

The ISR is the list of replicas that are fully caught up with the leader. The leader is always in it. A follower that falls too far behind (by default, no catch-up for 30 seconds, `replica.lag.time.max.ms`) is removed from the ISR, and added back once it catches up.

Only ISR members are normally allowed to become the new leader, which is how Kafka avoids losing committed data.

## 19: What is the replication factor?

The replication factor is how many copies of each partition exist. With a replication factor of 3, each partition has one leader and two followers on three different brokers. The cluster can then lose up to two of those brokers without losing data (though writes might stop, depending on `min.insync.replicas`).

3 is the common choice for production.

## 20: How long does Kafka keep messages?

As long as the topic's retention settings say. By default it is 7 days (`log.retention.hours=168`). You can also limit by size with `retention.bytes`. Once a segment of data is older than the limit, Kafka deletes it, whether anyone read it or not.

You can also keep data forever (`retention.ms=-1`) or use log compaction to keep only the latest value per key.

## 21: Does Kafka delete messages after they are consumed?

No. Reading a message does not remove it. Kafka deletes data only based on retention (time or size) or compaction. This is why many consumer groups can read the same data, and why a consumer can go back and re-read old messages.

## 22: What is a record key used for?

The key has two main jobs:

1. **Partitioning:** records with the same key go to the same partition, so they stay in order relative to each other. For example, using `customerId` as the key keeps all events for one customer in order.
2. **Compaction:** in compacted topics, Kafka keeps the latest record for each key.

The key is optional. Records without a key are spread over partitions.

## 23: How does Kafka guarantee message ordering?

Kafka guarantees order only **within a partition**. Records in one partition are stored and read in the order they were written. There is no ordering across different partitions of a topic.

If you need order for a certain entity (an order, a user, an account), use its ID as the key so all its records land in the same partition.

## 24: What is a record header?

Headers are optional key/value pairs attached to a record, separate from the key and value. The header key is a string and the value is bytes. They are useful for metadata such as trace IDs, the event type, the source system or a schema version.

```java
ProducerRecord<String, String> record = new ProducerRecord<>("orders", "order-42", payload);
record.headers().add("trace-id", "abc123".getBytes(StandardCharsets.UTF_8));
```

## 25: What is a record timestamp?

Every record has a timestamp. It is one of two types, set per topic with `message.timestamp.type`:

- `CreateTime` (default): set by the producer, usually when the record was created.
- `LogAppendTime`: set by the broker when it writes the record.

Timestamps are used by time-based retention, by `offsetsForTimes()` to look up offsets by time, and by Kafka Streams for windowing.

## 26: What is serialization in Kafka?

Kafka stores and sends bytes. Serialization turns your objects (strings, JSON, Avro records) into bytes on the producer side. Deserialization turns bytes back into objects on the consumer side.

You set a serializer for the key and the value on the producer, and matching deserializers on the consumer. If they do not match, the consumer gets garbage or an error.

## 27: Which serializers come with the Kafka Java client?

The client includes serializers and deserializers for basic types:

- `StringSerializer` / `StringDeserializer`
- `IntegerSerializer`, `LongSerializer`, `DoubleSerializer`, `ShortSerializer`, `FloatSerializer`
- `ByteArraySerializer`, `ByteBufferSerializer`, `BytesSerializer`
- `UUIDSerializer`
- `VoidSerializer` (for null keys)

For JSON, Avro or Protobuf you write your own or use a library like Confluent's serializers.

## 28: What is a bootstrap server?

A bootstrap server is the address a client uses to make its first connection, set with `bootstrap.servers`. The client asks it for cluster metadata and learns about all the other brokers. After that it connects directly to whichever brokers lead the partitions it needs.

List more than one broker so the client can still start if one is down:

```properties
bootstrap.servers=broker1:9092,broker2:9092,broker3:9092
```

## 29: How do you start Kafka locally with Docker?

The official `apache/kafka` image starts a single-node cluster (broker and controller in one process) with a working default config:

```bash
docker run -d --name kafka -p 9092:9092 apache/kafka:4.3.1
```

Clients on your machine can then connect to `localhost:9092`. There is also an `apache/kafka-native` image built with GraalVM that starts faster and uses less memory, which is handy for tests.

## 30: How do you start Kafka from the downloaded archive?

After extracting the release, generate a cluster ID, format the storage directory, and start the server:

```bash
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format --standalone -t "$KAFKA_CLUSTER_ID" -c config/server.properties
bin/kafka-server-start.sh config/server.properties
```

You need Java 17 or newer for the server. Formatting is only done once per storage directory.

## 31: How do you create a topic from the command line?

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 \
  --create --topic orders \
  --partitions 6 --replication-factor 3 \
  --config retention.ms=604800000
```

`--partitions` and `--replication-factor` are optional; if you skip them the broker defaults are used (`num.partitions` and `default.replication.factor`).

## 32: How do you list and describe topics?

```bash
# list all topics
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

# show partitions, leaders, replicas and ISR
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic orders
```

`--describe` without `--topic` describes every topic. Useful filters are `--under-replicated-partitions` and `--unavailable-partitions`.

## 33: How do you send messages with the console producer?

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic orders
> first message
> second message
```

Each line you type becomes one record. To send keys too:

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic orders \
  --property parse.key=true --property key.separator=:
> order-1:{"amount": 20}
```

## 34: How do you read messages with the console consumer?

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \
  --topic orders --from-beginning
```

Without `--from-beginning` it only shows new messages. Add `--property print.key=true` to see keys, `--group my-group` to read as part of a consumer group, and `--max-messages 10` to stop after a few records.

## 35: How do you write a simple producer in Java?

```java
Properties props = new Properties();
props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);

try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
    ProducerRecord<String, String> record =
        new ProducerRecord<>("orders", "order-1", "{\"amount\": 20}");

    producer.send(record, (metadata, exception) -> {
        if (exception != null) {
            exception.printStackTrace();
        } else {
            System.out.printf("written to partition %d at offset %d%n",
                metadata.partition(), metadata.offset());
        }
    });
}
```

`send()` is asynchronous. Closing the producer (here with try-with-resources) sends anything still buffered.

## 36: How do you write a simple consumer in Java?

```java
Properties props = new Properties();
props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
props.put(ConsumerConfig.GROUP_ID_CONFIG, "billing");
props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
    consumer.subscribe(List.of("orders"));
    while (true) {
        ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
        for (ConsumerRecord<String, String> record : records) {
            System.out.printf("%s => %s (p%d, offset %d)%n",
                record.key(), record.value(), record.partition(), record.offset());
        }
    }
}
```

By default offsets are committed automatically every 5 seconds.

## 37: How do you produce and consume messages from Node.js?

A common choice today is Confluent's `@confluentinc/kafka-javascript`, which is built on librdkafka and offers a KafkaJS-style API:

```js
const { Kafka } = require("@confluentinc/kafka-javascript").KafkaJS;

const kafka = new Kafka({ kafkaJS: { brokers: ["localhost:9092"] } });

async function main() {
  const producer = kafka.producer();
  await producer.connect();
  await producer.send({
    topic: "orders",
    messages: [{ key: "order-1", value: JSON.stringify({ amount: 20 }) }],
  });
  await producer.disconnect();

  const consumer = kafka.consumer({
    kafkaJS: { groupId: "billing", fromBeginning: true },
  });
  await consumer.connect();
  await consumer.subscribe({ topics: ["orders"] });
  await consumer.run({
    eachMessage: async ({ partition, message }) => {
      console.log(partition, message.key.toString(), message.value.toString());
    },
  });
}

main().catch(console.error);
```

## 38: What does the poll() method do?

`poll(timeout)` is the main loop call of a consumer. It:

- fetches the next batch of records from the assigned partitions,
- takes part in the group (joining, rebalancing, and in the classic protocol, heartbeats run alongside it),
- commits offsets in the background if auto commit is on.

It returns as soon as records are available, or an empty result after the timeout. You must call it regularly; if you go longer than `max.poll.interval.ms` between calls, the consumer is removed from the group.

## 39: What does committing an offset mean?

Committing an offset means saving "this group has processed everything in this partition up to here". The committed value is the offset of the **next** record to read.

When a consumer restarts or a partition moves to another consumer, reading continues from the last committed offset. If you commit too early you can lose messages; if you commit too late you will reprocess some.

## 40: What is auto commit?

With `enable.auto.commit=true` (the default), the consumer commits the offsets returned by `poll()` every `auto.commit.interval.ms` (5 seconds by default). The commit happens inside `poll()` and on `close()`.

It is simple but can lead to duplicates after a crash (work done but not committed yet). If you hand records off to other threads, it can also lose messages (committed but not processed yet). Many apps turn it off and commit manually after processing.

## 41: Where does Kafka store committed offsets?

In an internal compacted topic called `__consumer_offsets`. It has 50 partitions by default. Each group's offsets go to one partition chosen by a hash of the `group.id`, and the leader of that partition acts as the group's coordinator.

Very old Kafka versions stored offsets in ZooKeeper, but that has not been the case for a long time.

## 42: What does auto.offset.reset do?

It tells the consumer where to start when there is no committed offset for a partition (a new group) or the committed offset no longer exists (data was deleted by retention).

- `latest` (default): start at the end, read only new records.
- `earliest`: start from the oldest available record.
- `none`: throw an exception instead of guessing.

It does nothing if a valid committed offset exists.

## 43: What is consumer lag?

Lag is how far behind a consumer group is. For each partition, it is:

```text
lag = log end offset (latest offset in the partition) - committed offset of the group
```

Growing lag means consumers cannot keep up with producers. It is one of the most important things to monitor.

## 44: How do you check consumer group lag?

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --describe --group billing
```

The output shows, for each partition, `CURRENT-OFFSET` (committed), `LOG-END-OFFSET`, `LAG`, and which consumer owns it. `--list` shows all groups.

## 45: What is a rebalance?

A rebalance is when partitions are reassigned between the consumers of a group. It happens when:

- a consumer joins or leaves,
- a consumer is considered dead (missed heartbeats or took too long between polls),
- partitions are added to a subscribed topic, or a new topic matches a subscribed pattern.

With the older "eager" style, all consumers stop during a rebalance. Newer protocols move only the partitions that need to move.

## 46: What happens if a group has more consumers than partitions?

The extra consumers sit idle. A partition is assigned to only one consumer in a group, so a topic with 4 partitions can have at most 4 active consumers in a group. The idle ones are still useful as backups that take over if an active one fails.

To get more parallelism you need more partitions (or a share group, which does not have this limit).

## 47: Can two consumer groups read the same topic?

Yes. Each group has its own committed offsets, so each group gets a full copy of the data and reads at its own speed. This is how one event can be handled by billing, shipping and analytics services at the same time.

## 48: What is the acks setting on the producer?

`acks` controls when the producer considers a write successful:

- `acks=0`: do not wait for any answer. Fastest, but messages can be lost silently.
- `acks=1`: wait for the leader to write it. Data can be lost if the leader dies before followers copy it.
- `acks=all` (or `-1`): wait until all in-sync replicas have it. Safest.

Since Kafka 3.0 the default is `acks=all`.

## 49: What delivery guarantees does Kafka offer?

- **At most once:** a message is processed zero or one times. Nothing is duplicated but things can be lost.
- **At least once:** nothing is lost, but a message can be processed more than once.
- **Exactly once:** each message affects the result once, using idempotent producers and transactions.

Which one you get depends on producer settings and on when the consumer commits offsets.

## 50: What is at-least-once delivery?

At-least-once means no message is lost, but some may be handled twice. On the producer side, retries can write the same message again. On the consumer side, you process first and commit after, so if the app crashes between the two, the message is processed again after restart.

It is the most common setup. Consumers should be idempotent so duplicates do not cause problems.

## 51: What is at-most-once delivery?

At-most-once means a message is never processed twice, but it can be lost. You get it when the consumer commits the offset **before** processing. If the app crashes after the commit but before finishing, that message is skipped.

It also happens on the producer side with `acks=0` or with retries turned off. It is only fine for data where losing a little is acceptable, like some metrics.

## 52: What is exactly-once in Kafka?

Exactly-once (often called EOS, exactly-once semantics) means each input record affects the output once, even with retries and crashes. Kafka provides it with:

- **idempotent producers**, so retries do not create duplicates in a partition,
- **transactions**, so writes to several partitions and the consumer offset commit succeed or fail together,
- **`isolation.level=read_committed`** on consumers, so they skip aborted data.

It works for Kafka-to-Kafka flows (like Kafka Streams apps). When you write to an outside system, that system also needs to handle duplicates or take part in some kind of transaction.

## 53: What is an idempotent producer?

An idempotent producer makes sure that retries do not create duplicate records in a partition. The broker gives the producer an ID, and the producer tags each batch with a sequence number per partition. If the broker sees the same sequence number twice, it drops the duplicate.

It is turned on by default since Kafka 3.0 (`enable.idempotence=true`), as long as you do not set conflicting options like `acks=1`.

## 54: What is batching in the producer?

The producer does not send each record on its own. It groups records going to the same partition into batches and sends a batch in one request. This cuts network overhead, makes compression work much better, and is a big part of why Kafka is fast.

Records wait in a memory buffer (`buffer.memory`, 32 MB by default) until their batch is sent.

## 55: What do batch.size and linger.ms do?

- `batch.size` (default 16384 bytes): the maximum size of a batch for one partition. When it is full, it is ready to send.
- `linger.ms` (default 5 ms since Kafka 4.0, it was 0 before): how long the producer waits for more records before sending a batch that is not full.

A higher `linger.ms` and bigger `batch.size` give better throughput and compression, at the cost of a bit more latency.

## 56: What compression types does Kafka support?

`none`, `gzip`, `snappy`, `lz4` and `zstd`. You set it on the producer:

```properties
compression.type=zstd
```

Compression is applied to whole batches, so it works better with bigger batches. `lz4` and `zstd` are popular choices: `lz4` for speed, `zstd` for a better ratio.

## 57: What is a log segment?

A partition is stored on disk as a set of files called segments. Each segment holds a range of offsets. Only the newest segment (the active one) is written to. When it reaches `log.segment.bytes` (1 GB by default) or gets old enough (`segment.ms`, 7 days by default), Kafka closes it and starts a new one.

Retention and compaction work on whole closed segments, which is why old data is deleted in chunks, not record by record.

## 58: What is log compaction?

Log compaction is a cleanup mode where Kafka keeps at least the latest record for each key and removes older records with the same key. The topic then works like a changelog of current values.

It is used for things like user profiles, configs, and Kafka's own `__consumer_offsets` topic. You turn it on per topic with `cleanup.policy=compact`.

```text
before: k1=a  k2=b  k1=c  k3=d  k2=e
after:  k1=c  k3=d  k2=e
```

## 59: What is a tombstone message?

A tombstone is a record with a key and a `null` value. In a compacted topic it means "delete this key". The log cleaner removes older records for that key, and later removes the tombstone itself too, after `delete.retention.ms` (1 day by default).

```java
producer.send(new ProducerRecord<>("user-profiles", "user-42", null));
```

## 60: What is cleanup.policy?

`cleanup.policy` decides how old data is removed from a topic:

- `delete` (default): delete whole segments that are older than `retention.ms` or when the partition is bigger than `retention.bytes`.
- `compact`: keep the latest value for each key.
- `compact,delete`: compact, and also delete data older than the retention time.

## 61: What are retention.ms and retention.bytes?

They are topic-level retention limits:

- `retention.ms`: how long to keep data. Default is 7 days. `-1` means forever.
- `retention.bytes`: the maximum size **per partition**. Default is `-1` (no limit).

Whichever limit is hit first causes old segments to be deleted. The broker defaults are `log.retention.hours` / `log.retention.ms` and `log.retention.bytes`.

## 62: What is the default maximum message size?

About 1 MB. The relevant settings are:

- broker `message.max.bytes` (default 1048588 bytes) and topic `max.message.bytes`,
- producer `max.request.size` (default 1 MB),
- consumer `max.partition.fetch.bytes` and `fetch.max.bytes` (the consumer can still fetch a single batch bigger than these so it never gets stuck).

To send bigger records you have to raise the producer and broker/topic limits together. Often it is better to store the large payload elsewhere and send a reference.

## 63: Can you change the number of partitions of a topic?

You can increase it, but you cannot decrease it.

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 \
  --alter --topic orders --partitions 12
```

Be careful with keyed data: after adding partitions, the same key can map to a different partition, so new records for a key may land somewhere other than its old records. To reduce partitions you have to create a new topic and move the data.

## 64: How do you delete a topic?

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic orders
```

Deletion is allowed by default (`delete.topic.enable=true`). The data is removed from disk in the background. It cannot be undone, so many teams turn this off or restrict it with ACLs in production.

## 65: What is the Admin client?

The Admin client (`org.apache.kafka.clients.admin.Admin`) is a Java API for managing a cluster from code: creating and deleting topics, changing configs, managing ACLs, describing consumer groups, listing offsets, and so on. The command line tools use it under the hood.

```java
try (Admin admin = Admin.create(Map.of("bootstrap.servers", "localhost:9092"))) {
    admin.createTopics(List.of(new NewTopic("orders", 6, (short) 3))).all().get();
}
```

## 66: What is Kafka Connect?

Kafka Connect is a framework, shipped with Kafka, for moving data between Kafka and other systems without writing producer or consumer code. You configure a **connector** (for example, a JDBC, S3 or Elasticsearch connector) with JSON, and Connect runs it, handles offsets, retries and scaling.

It is typically used for change data capture from databases, loading data into data warehouses, and similar integration jobs.

## 67: What are source and sink connectors?

- A **source connector** reads data from an outside system and writes it into Kafka. Example: Debezium reading a Postgres transaction log.
- A **sink connector** reads from Kafka and writes into an outside system. Example: writing records into Elasticsearch or S3.

## 68: What is Kafka Streams?

Kafka Streams is a Java library for building stream processing apps that read from Kafka topics, transform the data, and write results back to Kafka. It supports filtering, mapping, joins, aggregations, windows and local state, with exactly-once support.

It is a library, not a separate cluster. You run it inside your normal app and scale by starting more instances.

## 69: What are a stream and a table in Kafka Streams?

- A **stream** (`KStream`) is a sequence of independent events. Every record is a new fact, like "user 5 clicked a button".
- A **table** (`KTable`) is the latest value per key. A new record for a key replaces the old one, like "user 5's current email".

A stream can be turned into a table by aggregating it, and a table's changes can be read as a stream.

## 70: What is a Serde?

A Serde (serializer + deserializer) is the Kafka Streams way of telling the library how to turn keys and values into bytes and back. Built-in ones are in `Serdes`, like `Serdes.String()` and `Serdes.Long()`.

```java
KStream<String, Long> counts =
    builder.stream("clicks", Consumed.with(Serdes.String(), Serdes.Long()));
```

You can set defaults with `default.key.serde` and `default.value.serde`.

## 71: What is MirrorMaker 2?

MirrorMaker 2 (MM2) is a tool for copying topics from one Kafka cluster to another, for example between data centers or cloud regions. It is built on Kafka Connect. It copies data, topic configs and ACLs, and it can translate consumer group offsets so consumers can fail over to the other cluster.

The original MirrorMaker 1 was removed in Kafka 4.0.

## 72: What is a schema registry?

A schema registry is a separate service that stores schemas (Avro, Protobuf or JSON Schema) for the data in topics. Producers register the schema and put a small schema ID in each message; consumers use the ID to fetch the schema and decode the data. It also checks that new schema versions are compatible with old ones.

It is not part of Apache Kafka itself. Common options are Confluent Schema Registry, Apicurio Registry and Karapace.

## 73: Why use Avro or Protobuf instead of plain JSON?

- **Smaller messages:** binary formats do not repeat field names in every message.
- **A real contract:** producers and consumers share a defined schema.
- **Safe changes:** with a schema registry, incompatible changes are rejected before they break consumers.
- **Generated code:** you get typed classes in Java, TypeScript, Go and others.

JSON is fine for small projects or when human readability matters most, but it has no built-in way to stop a producer from breaking consumers.

## 74: What is a dead letter queue?

A dead letter queue (DLQ) is a separate topic where you put messages that could not be processed, for example because they are malformed or keep failing. The main consumer moves on instead of getting stuck, and someone can inspect, fix or replay the failed messages later.

Kafka Connect has built-in DLQ support for sink connectors. In normal consumers you usually build it yourself by producing the failed record to a topic like `orders.dlq`.

## 75: What is the __consumer_offsets topic?

It is an internal compacted topic where Kafka stores committed offsets and consumer group metadata. Each record's key is something like (group, topic, partition), and the value is the committed offset. Because it is compacted, only the latest offset per key is kept.

You should not write to it directly.

## 76: What are internal topics?

Topics Kafka and its tools create for their own use. Examples:

- `__consumer_offsets`: committed offsets and group state.
- `__transaction_state`: transaction coordinator state.
- `__share_group_state`: state for share groups.
- `__cluster_metadata`: the KRaft metadata log (this one is not a normal topic you can read with a consumer).
- Kafka Connect's config, offset and status topics.
- Kafka Streams' `-changelog` and `-repartition` topics.

## 77: What ports does Kafka use by default?

There is no hardcoded port, it depends on `listeners`. By convention:

- `9092` for client connections to brokers,
- `9093` for the controller listener in KRaft.

Kafka Connect's REST API uses `8083` by default, and Confluent Schema Registry uses `8081`.

## 78: What is a listener?

A listener is a network address and protocol a broker or controller accepts connections on. You can have several, for example one for internal traffic and one for external clients:

```properties
listeners=INTERNAL://0.0.0.0:9092,EXTERNAL://0.0.0.0:9094,CONTROLLER://0.0.0.0:9093
listener.security.protocol.map=INTERNAL:PLAINTEXT,EXTERNAL:SASL_SSL,CONTROLLER:PLAINTEXT
inter.broker.listener.name=INTERNAL
controller.listener.names=CONTROLLER
```

The protocol for each listener is one of `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT` or `SASL_SSL`.

## 79: What is advertised.listeners?

`advertised.listeners` is the address a broker tells clients to use. When a client connects to the bootstrap server, it gets metadata listing each broker's advertised address and then connects to those.

```properties
listeners=PLAINTEXT://0.0.0.0:9092
advertised.listeners=PLAINTEXT://kafka1.example.com:9092
```

`listeners` is what the broker binds to; `advertised.listeners` is what clients must be able to reach.

## 80: Why can a client reach the bootstrap server but then fail to connect?

This is almost always an `advertised.listeners` problem. The first connection works because you used a reachable address, but the broker then tells the client to use its advertised address, for example `localhost:9092` or an internal Docker hostname. From the client's machine that address is wrong, so later connections fail.

The fix is to advertise an address the client can reach, often with separate listeners for internal and external clients.

## 81: What is a partition leader election?

It is picking a new leader for a partition, usually because the current leader's broker failed or was shut down. The active controller chooses a new leader from the in-sync replicas and tells the brokers. Clients find the new leader by refreshing metadata.

Elections also happen when you move leadership back to the "preferred" replica to balance load.

## 82: What happens when a broker goes down?

1. The controller notices the broker stopped sending heartbeats.
2. For every partition that broker led, the controller elects a new leader from the ISR.
3. The failed broker is removed from the ISR of all partitions it followed.
4. Clients get errors, refresh metadata, and switch to the new leaders.

If the replication factor and `min.insync.replicas` are set well, no data is lost and clients only see a short pause. When the broker comes back, it catches up and rejoins the ISRs.

## 83: What is min.insync.replicas?

`min.insync.replicas` is the minimum number of in-sync replicas that must have a write before it is acknowledged, when the producer uses `acks=all`. If fewer replicas are in sync, writes fail with `NotEnoughReplicasException`.

A common setup is replication factor 3 with `min.insync.replicas=2`: you can lose one broker and keep writing, and every acknowledged write exists on at least two brokers. The default is 1.

## 84: What is unclean leader election?

Unclean leader election lets a replica that is **not** in the ISR become leader when no in-sync replica is available. The partition becomes available again, but any data that only the old leader had is lost.

It is off by default (`unclean.leader.election.enable=false`), which means Kafka prefers being unavailable over losing data. Turn it on only for data where availability matters more than completeness.

## 85: What is the high watermark?

The high watermark is the offset up to which all in-sync replicas have copied the data. Records below it are "committed" and safe. Consumers can only read up to the high watermark, so they never see data that could later disappear if the leader fails.

## 86: What is the log end offset?

The log end offset (LEO) is the offset that the next record written to a replica will get, so it is one past the last record. Each replica has its own LEO. The leader's LEO can be ahead of the high watermark while followers are still catching up.

## 87: Is the Kafka producer thread-safe?

Yes. A `KafkaProducer` is thread-safe and it is usually best to share one instance across threads. Sharing helps batching and saves connections and memory.

## 88: Is the Kafka consumer thread-safe?

No. A `KafkaConsumer` must be used from a single thread. The only method that is safe to call from another thread is `wakeup()`, which is used to break out of `poll()` during shutdown.

For parallel work, either run one consumer per thread or have one consumer thread hand records to worker threads (and handle offset commits carefully).

## 89: What is the group coordinator?

The group coordinator is the broker that manages a consumer group. It tracks members, handles joins and leaves, runs rebalances, and stores committed offsets. It is the leader of the `__consumer_offsets` partition that the group ID hashes to.

## 90: What is a heartbeat in a consumer group?

A heartbeat is a small request a consumer sends to the group coordinator to say "I am alive". If the coordinator does not get heartbeats within the session timeout, it removes the consumer from the group and gives its partitions to others.

In the classic protocol a background thread sends heartbeats every `heartbeat.interval.ms` (3 seconds by default). In the newer consumer protocol the interval is controlled by the broker.

## 91: What is session.timeout.ms?

It is how long the coordinator waits without a heartbeat before it considers a consumer dead. The default is 45 seconds. A lower value detects crashed consumers faster but makes false alarms more likely, for example during long GC pauses.

With the new consumer group protocol (`group.protocol=consumer`), this is set on the broker side (`group.consumer.session.timeout.ms`) instead of in the client.

## 92: What is max.poll.interval.ms?

It is the maximum time allowed between two `poll()` calls. The default is 5 minutes. If your processing of one batch takes longer than this, the consumer is treated as stuck, it leaves the group, and its partitions are reassigned. When it finally commits, it gets a `CommitFailedException`.

If processing is slow, either raise this value or lower `max.poll.records`.

## 93: What is max.poll.records?

The maximum number of records one `poll()` call returns. The default is 500. It does not change how much data is fetched from the broker, only how many records are handed to your code per call. Lower it when each record takes a long time to process, so you stay within `max.poll.interval.ms`.

## 94: How do you subscribe to several topics or a pattern?

```java
// a list of topics
consumer.subscribe(List.of("orders", "payments"));

// every topic that matches a regex
consumer.subscribe(Pattern.compile("events\\..*"));
```

With a pattern, new topics that match are picked up automatically after the next metadata refresh.

## 95: What is the difference between subscribe() and assign()?

- `subscribe()`: the consumer joins a group and Kafka decides which partitions it gets. Rebalances happen automatically.
- `assign()`: you pick the exact partitions yourself. There is no group membership and no rebalancing. You can still commit offsets if you set a `group.id`.

```java
consumer.assign(List.of(new TopicPartition("orders", 0)));
```

`assign()` is useful for tools, tests, or when you manage partition ownership yourself.

## 96: How do you read a topic from the beginning?

For a new group, set `auto.offset.reset=earliest`. For a group that already has committed offsets, either reset them with the CLI or call `seekToBeginning()` after partitions are assigned:

```java
consumer.subscribe(List.of("orders"), new ConsumerRebalanceListener() {
    public void onPartitionsRevoked(Collection<TopicPartition> parts) {}
    public void onPartitionsAssigned(Collection<TopicPartition> parts) {
        consumer.seekToBeginning(parts);
    }
});
```

## 97: What does seek() do?

`seek(partition, offset)` moves the consumer's position for a partition, so the next `poll()` reads from that offset. It does not commit anything. Related methods are `seekToBeginning()` and `seekToEnd()`.

```java
consumer.seek(new TopicPartition("orders", 0), 1500L);
```

## 98: How does the producer choose a partition?

- If you set a partition in the `ProducerRecord`, that one is used.
- If the record has a key, the producer hashes the key (murmur2) and takes it modulo the partition count. Same key, same partition.
- If there is no key, the producer uses sticky partitioning: it fills a batch for one partition, then switches to another.

You can also plug in your own `Partitioner` class.

## 99: What is the sticky partitioner?

For records without a key, the producer sticks to one partition until the current batch is full or sent, then picks another one. This creates bigger batches and lower latency than spreading every record round-robin.

Since Kafka 3.3 this logic is built into the producer and it also sends less data to slower brokers. The old `DefaultPartitioner` and `UniformStickyPartitioner` classes are deprecated.

## 100: What happens when you send a record with a null key?

The record is valid. It goes to a partition chosen by the sticky partitioning logic, so records without keys get spread over all partitions over time. There is no ordering between them. A null key also cannot be used in a compacted topic, and the broker rejects such records there.

## 101: What happens when you send a record with a null value?

A record with a `null` value is allowed. In a normal topic it is just a record with no data. In a compacted topic it is a tombstone, which tells Kafka to delete that key. Consumers must be ready for `record.value()` to be `null`.

## 102: What is the difference between a synchronous and an asynchronous send?

`send()` always returns a `Future<RecordMetadata>` right away. You choose how to wait for the result:

```java
// synchronous: block until the broker answers
RecordMetadata meta = producer.send(record).get();

// asynchronous: get notified in a callback
producer.send(record, (metadata, exception) -> {
    if (exception != null) log.error("send failed", exception);
});
```

Blocking on every send kills throughput because batching cannot work well. Use callbacks in normal code and save `.get()` for scripts or tests.

## 103: What does flush() do on the producer?

`flush()` sends all buffered records right away and blocks until every one of them has finished (succeeded or failed). It is useful before shutting down or at a checkpoint where you need all previous sends to be done. Calling it after every send defeats batching.

## 104: Why should you close the producer and consumer?

- **Producer:** `close()` sends any records still in the buffer. Without it, those records are lost when the app exits.
- **Consumer:** `close()` commits offsets (if auto commit is on) and leaves the group right away, so its partitions are reassigned quickly. Without it, the group waits for the session timeout before rebalancing.

Use try-with-resources or a shutdown hook.

## 105: What is client.id?

`client.id` is a name you give a producer or consumer. It shows up in broker logs, metrics and quotas, so you can tell which app is doing what. It does not need to be unique, but a clear name like `billing-service` makes debugging much easier.

## 106: What is group.id?

`group.id` is the name of the consumer group a consumer belongs to. All consumers with the same `group.id` share the partitions of their subscribed topics and share committed offsets. It is required for `subscribe()` and for committing offsets.

## 107: What are the main configuration files in a Kafka install?

In the `config/` folder of a Kafka 4.x release:

- `server.properties`: a combined broker + controller node.
- `broker.properties` and `controller.properties`: for running brokers and controllers as separate nodes.
- `producer.properties`, `consumer.properties`: sample client settings for the CLI tools.
- `connect-standalone.properties`, `connect-distributed.properties`: Kafka Connect workers.
- `connect-mirror-maker.properties`: MirrorMaker 2.
- `log4j2.yaml` (Kafka 4.0 moved to Log4j 2): logging.

## 108: What is node.id?

`node.id` is the unique number of a broker or controller in a KRaft cluster. It must be unique across the whole cluster and must stay the same for the life of the node. Partition replicas and controller voters are referenced by this ID.

## 109: What is process.roles?

`process.roles` tells a KRaft node what to run:

- `broker`: stores data and serves clients.
- `controller`: part of the metadata quorum.
- `broker,controller`: both in one process (combined mode), fine for development and small setups.

```properties
process.roles=broker
node.id=4
controller.quorum.bootstrap.servers=ctrl1:9093,ctrl2:9093,ctrl3:9093
```

## 110: What is a cluster ID and why do you format storage?

The cluster ID is a unique ID for a Kafka cluster. In KRaft mode you generate it once and use it to format the storage directory on every node, which writes a `meta.properties` file with the cluster ID and node ID. A node refuses to start if its storage belongs to a different cluster, which protects you from mixing up disks.

```bash
bin/kafka-storage.sh random-uuid
bin/kafka-storage.sh format -t <cluster-id> -c config/broker.properties
```

## 111: What is a topic configuration override?

Brokers have default settings like `log.retention.hours`. Each topic can override them with its own setting, like `retention.ms`. The topic setting wins. Topic overrides are stored in cluster metadata, not in `server.properties`.

Note the naming: broker defaults usually start with `log.` (`log.retention.ms`), topic settings do not (`retention.ms`).

## 112: How do you change a topic's config at runtime?

```bash
bin/kafka-configs.sh --bootstrap-server localhost:9092 \
  --entity-type topics --entity-name orders \
  --alter --add-config retention.ms=86400000

# remove the override
bin/kafka-configs.sh --bootstrap-server localhost:9092 \
  --entity-type topics --entity-name orders \
  --alter --delete-config retention.ms
```

No restart is needed. `--describe` shows the current overrides.

## 113: What is kafka-configs.sh used for?

It reads and changes dynamic configs for different entities:

- `topics`: topic settings like retention or cleanup policy.
- `brokers`: some broker settings that can change without restart (thread counts, SSL keystores, throttles).
- `users` and `clients`: quotas, and SCRAM credentials for users.
- `groups`: consumer and share group settings.

## 114: What is the difference between a topic and a queue?

In a **queue**, each message goes to one consumer and is usually removed once it is acknowledged. In a Kafka **topic**, records stay for the retention period and every consumer group gets all of them.

Inside one consumer group, a topic behaves a bit like a queue split by partition: each partition is handled by one consumer. Kafka 4.2 also made share groups production-ready, which give real queue behavior on top of topics.

## 115: What are share groups (Queues for Kafka)?

Share groups are a newer kind of group (from KIP-932, production-ready since Kafka 4.2) where consumers share partitions instead of owning them. Several consumers can read records from the same partition, and each record is acknowledged one by one. If a consumer fails or rejects a record, it can be redelivered to another consumer.

This makes Kafka work like a job queue: you can have more consumers than partitions and scale workers freely. The trade-off is that you lose per-partition ordering.

## 116: What is the difference between a consumer group and a share group?

|                      | Consumer group                     | Share group                                                 |
| -------------------- | ---------------------------------- | ----------------------------------------------------------- |
| Partition ownership  | One consumer per partition         | Many consumers per partition                                |
| Max useful consumers | Number of partitions               | Not limited by partitions                                   |
| Ordering             | Kept within a partition            | Not guaranteed                                              |
| Progress tracking    | One committed offset per partition | Per-record acknowledgement                                  |
| Redelivery           | Re-read from committed offset      | Failed records are redelivered, with a delivery count limit |
| Java client          | `KafkaConsumer`                    | `KafkaShareConsumer`                                        |

## 117: What is publish/subscribe messaging?

In pub/sub, publishers send messages to a topic without knowing who will receive them, and every subscriber gets its own copy. Kafka supports this naturally: each consumer group is a subscriber that gets all records of the topic. This decouples services, since the producer does not need to know who consumes its events.

## 118: Why is Kafka fast?

- **Sequential disk I/O:** it only appends to log files and reads them in order, which disks handle very well.
- **Page cache:** it relies on the operating system's file cache instead of its own heap cache.
- **Batching and compression:** records are sent, stored and read in compressed batches.
- **Zero-copy:** for plain (non-TLS) connections, data goes from the page cache to the network socket without being copied into the app.
- **Partitioning:** load is spread across many brokers and disks.
- **Simple broker:** the broker does not track per-message state for consumer groups; consumers track offsets.

## 119: What is a commit log?

A commit log is an append-only, ordered list of records. New records are added at the end, existing ones are never changed, and each one has a position (offset). Databases use the same idea internally for recovery and replication.

Kafka exposes this structure directly: each partition is a commit log that many readers can read at their own pace.

## 120: What does it mean that Kafka is distributed?

It means Kafka runs on many machines that act as one system. Partitions are spread across brokers, each partition is copied to several brokers, and metadata is managed by a group of controllers. No single machine has all the data or is a single point of failure, and you can add machines to handle more load.

## 121: How do you scale Kafka horizontally?

- **More brokers:** add brokers, then move some partitions onto them with partition reassignment.
- **More partitions:** give topics more partitions so more consumers can work in parallel.
- **More consumers:** add consumers to a group, up to the number of partitions.

New brokers do not get existing partitions automatically. You have to reassign partitions to use them.

## 122: What language is Kafka written in and which clients exist?

The broker is written in Java and Scala (newer code is mostly Java). The official clients that ship with Apache Kafka are Java clients: producer, consumer, admin, share consumer, plus Kafka Streams and Kafka Connect.

For other languages there are community and vendor clients, many built on librdkafka: `confluent-kafka-python`, `confluent-kafka-go`, `@confluentinc/kafka-javascript`, `confluent-kafka-dotnet`, and pure clients like `franz-go` and KafkaJS.

## 123: What is librdkafka?

librdkafka is a widely used Kafka client library written in C. Many clients for other languages are wrappers around it, including the Confluent clients for Python, Go, .NET and JavaScript. Its config names mostly match the Java client's, with a few differences.

## 124: Which Java version does Kafka 4.x need?

Starting with Kafka 4.0:

- Brokers, controllers, Kafka Connect and the command line tools need **Java 17** or newer.
- Clients and Kafka Streams need **Java 11** or newer.

Kafka 4.2 added support for Java 25.

## 125: What are KIPs?

KIPs (Kafka Improvement Proposals) are the documents used to propose and discuss bigger changes to Kafka, like new features, config changes or protocol changes. Each has a number, for example KIP-500 (removing ZooKeeper), KIP-848 (new consumer rebalance protocol) or KIP-932 (Queues for Kafka). Interviewers sometimes mention features by KIP number.

## 126: What is event streaming?

Event streaming means capturing events as they happen (orders, clicks, sensor readings, database changes), storing them as continuous streams, and processing or reacting to them in real time or later. Kafka is the most common platform for this. The main difference from batch processing is that data is handled as it arrives instead of in periodic jobs.

## 127: What is event-driven architecture?

It is a style where services talk by publishing and reacting to events instead of calling each other directly. For example, the order service publishes `OrderPlaced`, and billing, inventory and email services each react to it.

Benefits: services are loosely coupled, new consumers can be added without changing the producer, and the system handles traffic spikes better. Downsides: flows are harder to follow, and you have to deal with eventual consistency and duplicate events.

## 128: What is a message broker?

A message broker is a server that receives messages from senders and delivers them to receivers, so the two do not need to talk directly. Kafka, RabbitMQ, ActiveMQ and cloud services like Amazon SQS are examples. Kafka is a bit different from classic brokers because it stores messages as a replayable log.

## 129: What is a rack in Kafka?

A rack is a failure domain, like a server rack or a cloud availability zone. You tag each broker with `broker.rack`. Kafka then spreads replicas of a partition across different racks, so losing a whole rack or zone does not lose all copies.

```properties
broker.rack=us-east-1a
```

## 130: What is the log.dirs setting?

`log.dirs` is a comma-separated list of directories where a broker stores partition data. Despite the name, these are data directories, not application logs. With several directories (usually on different disks), the broker spreads partitions across them.

```properties
log.dirs=/data/kafka1,/data/kafka2
```

## 131: How should you name topics?

There is no official rule, but teams usually pick a consistent pattern such as `<domain>.<entity>.<event>` or `<team>.<service>.<name>`, for example `sales.orders.created`. Tips:

- Use lowercase and one separator style.
- Do not put things that change (like environment or version numbers you will bump often) in the name unless you plan for it.
- Topic names can be up to 249 characters and use letters, digits, `.`, `_` and `-`.

## 132: Why does Kafka warn about mixing dots and underscores in topic names?

Kafka metric names replace `.` with `_`. So topics `orders.created` and `orders_created` would end up with the same metric name and collide. `kafka-topics.sh` warns you, and the broker refuses to create a topic whose name collides with an existing one this way. Pick one separator and stick with it.

## 133: How do you get the earliest and latest offsets of a topic?

```bash
# latest offsets (log end) per partition
bin/kafka-get-offsets.sh --bootstrap-server localhost:9092 --topic orders --time -1

# earliest available offsets
bin/kafka-get-offsets.sh --bootstrap-server localhost:9092 --topic orders --time -2
```

The difference between the two is roughly how many records each partition currently holds (not exact for compacted or transactional topics).

## 134: What is an offset reset?

An offset reset means changing a group's committed offsets, for example to reprocess data or to skip a bad range. It can happen automatically through `auto.offset.reset` when there is no valid offset, or on purpose with `kafka-consumer-groups.sh --reset-offsets` or the Admin API.

## 135: How do you reset offsets for a consumer group?

Stop all consumers in the group first (the group must be empty), then:

```bash
# preview
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group billing --topic orders --reset-offsets --to-earliest --dry-run

# apply
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group billing --topic orders --reset-offsets --to-earliest --execute
```

Other options include `--to-latest`, `--to-offset 1000`, `--shift-by -100`, `--to-datetime 2026-01-01T00:00:00.000` and `--by-duration PT1H`.

## 136: What is a producer callback?

A callback is code that runs when the broker answers a send, either with success metadata or an exception. It runs on the producer's I/O thread, so keep it short and do not block in it.

```java
producer.send(record, (metadata, exception) -> {
    if (exception != null) {
        // retries are already done at this point; log or send to a fallback
        log.error("could not send {}", record.key(), exception);
    }
});
```

## 137: What does RecordMetadata contain?

`RecordMetadata` is returned after a successful send. It includes the topic, the partition, the offset the record got, the timestamp, and the serialized key and value sizes. With `acks=0` the offset is unknown and is returned as `-1`.

## 138: What is a record batch on disk?

Kafka stores records in **record batches** (message format v2). A batch has a header with the base offset, the producer ID, epoch and sequence (for idempotence), a transactional flag, the compression codec, timestamps and a CRC. The records inside are stored with small relative offsets and timestamps to save space.

The same batch format is used by the producer, on disk and when sending to consumers, so the broker often does not need to rewrite data. Older formats (v0 and v1) were removed in Kafka 4.0.

## 139: What is cluster metadata?

Cluster metadata is the information about the cluster itself: which brokers exist, which topics and partitions exist, who leads each partition, the replica and ISR lists, configs, ACLs, quotas and features. In KRaft it lives in the controllers' metadata log, and every broker keeps a copy in memory.

## 140: How do clients learn about cluster metadata?

Clients send a `Metadata` request to any broker. The answer lists the brokers and, for each partition of the requested topics, the current leader. Clients cache it and refresh it periodically (`metadata.max.age.ms`, 5 minutes by default) or right away when they get errors like `NOT_LEADER_OR_FOLLOWER`.

## 141: What is the difference between Apache Kafka and Confluent Platform?

Apache Kafka is the open source project from the Apache Software Foundation. Confluent was founded by Kafka's original creators and sells Confluent Platform (self-managed) and Confluent Cloud (managed). These add things like Schema Registry, ksqlDB, many connectors, a UI and enterprise security features. Some of these are under licenses that are not Apache 2.0.

## 142: What are managed Kafka services?

They are cloud services that run Kafka for you: Confluent Cloud, Amazon MSK, Azure Event Hubs (with a Kafka-compatible API), Aiven, Redpanda Cloud (Kafka API-compatible, different engine) and others. They take care of servers, upgrades, scaling and monitoring. Trade-offs are cost, less control over configs, and sometimes missing features or lagging versions.

## 143: Which tools can you use to browse topics in a web UI?

Kafka itself has no web UI. Popular open source options include Kafbat UI (the continuation of "UI for Apache Kafka"), AKHQ, Redpanda Console, and Kafdrop. They let you view topics, messages, consumer groups and lag, and some can manage ACLs and Connect. Confluent Control Center is a commercial option.

## 144: What is JMX in Kafka?

JMX (Java Management Extensions) is how Kafka brokers and Java clients expose metrics, like request rates, under-replicated partitions or consumer lag. You can read them with JConsole, or more commonly export them to Prometheus with the JMX exporter agent and build dashboards in Grafana.

```bash
JMX_PORT=9999 bin/kafka-server-start.sh config/server.properties
```

## 145: What is the difference between Kafka and a database?

Kafka stores data durably and lets you read it, but it is built for moving and processing streams, not for querying. You read by offset or time, not by arbitrary fields. There are no indexes on your data, no updates in place, and no joins at the broker. A database is built to query the current state.

Many systems use both: Kafka for events and integration, databases for queries.

## 146: Can Kafka be used as the source of truth?

It can, with care. Some systems keep all events in Kafka forever (infinite retention or compaction) and rebuild databases and caches from them. This is the idea behind event sourcing.

You need proper replication, backups or tiered storage, schema control, and a plan for deleting personal data. Many teams prefer to keep the database as the source of truth and use Kafka to publish its changes.

## 147: What is a poison pill message?

A poison pill is a record that a consumer cannot process, for example because it cannot be deserialized or it breaks a business rule. If the consumer just keeps retrying, it gets stuck on that offset forever and lag grows for the whole partition.

The usual fix is to catch the error, send the record to a dead letter topic, and move on.

## 148: Why can producer retries create duplicates?

When a producer sends a batch and the answer is lost (for example a timeout), it does not know if the write worked, so it retries. If the first write did succeed, the record is now stored twice.

The idempotent producer (on by default) fixes this within a partition by having the broker detect repeated sequence numbers. Duplicates can still happen at the application level, for example if your code calls `send()` twice for the same event after a restart.

## 149: What is delivery.timeout.ms?

It is the upper limit on how long a `send()` can take to succeed or fail, counting from when `send()` returns. That covers time in the buffer, waiting for the broker, and all retries. The default is 2 minutes. After that the callback gets a `TimeoutException`.

It must be at least `linger.ms + request.timeout.ms`. Setting it is the modern way to control retries; you normally leave `retries` at its large default.

## 150: What are the main parts of the Kafka ecosystem?

- **Brokers and controllers:** the Kafka cluster itself.
- **Client APIs:** producer, consumer, share consumer and admin.
- **Kafka Connect:** moving data in and out of Kafka with connectors.
- **Kafka Streams:** a library for stream processing in Java apps.
- **MirrorMaker 2:** replicating between clusters.
- **Command line tools:** `kafka-topics.sh`, `kafka-consumer-groups.sh` and others.

Around it there are many outside tools: schema registries, Flink and Spark for processing, Debezium for change data capture, and UIs and operators like Strimzi.

# Moderate Questions (151-300)

## 151: How do you choose the number of partitions for a topic?

Start from the throughput you need and how much one consumer can handle:

```text
partitions >= max(target throughput / per-partition producer throughput,
                  target throughput / per-consumer throughput)
```

Then add room to grow, since you cannot reduce partitions later and adding them breaks key-to-partition mapping. Other things to think about: the maximum number of consumers you want in a group, how many keys you have (too few keys means uneven partitions), and the cluster's total partition count. For many apps, something like 6 to 30 partitions is a reasonable starting point; very high numbers should be justified.

## 152: How does the default partitioner pick a partition for keyed records?

It takes the serialized key bytes, computes a murmur2 hash, makes it positive, and takes it modulo the number of partitions:

```text
partition = toPositive(murmur2(keyBytes)) % numPartitions
```

So the same key always goes to the same partition **as long as the partition count does not change**. Clients in other languages that are built on librdkafka use a different default hash (`consistent_random`), so if you mix Java and non-Java producers on one topic, set librdkafka's `partitioner=murmur2_random` to get matching results.

## 153: How do you write a custom partitioner?

Implement `Partitioner` and set it with `partitioner.class`:

```java
public class VipPartitioner implements Partitioner {
    @Override
    public int partition(String topic, Object key, byte[] keyBytes,
                         Object value, byte[] valueBytes, Cluster cluster) {
        int count = cluster.partitionsForTopic(topic).size();
        if ("vip".equals(key)) {
            return 0; // reserve partition 0 for VIP traffic
        }
        return 1 + Utils.toPositive(Utils.murmur2(keyBytes)) % (count - 1);
    }

    @Override public void configure(Map<String, ?> configs) {}
    @Override public void close() {}
}
```

```properties
partitioner.class=com.example.VipPartitioner
```

Custom partitioners are rarely needed. Picking a good key is usually enough.

## 154: What goes wrong when you add partitions to a topic with keyed data?

The formula `hash(key) % partitions` gives a different result once the count changes. New records for a key can go to a different partition than its older records. During the switch, a consumer might process the new records for a key before the old ones still sitting in another partition, so per-key order breaks. Compacted topics also end up with the same key in two partitions.

If order matters, plan partitions up front, or migrate to a new topic with more partitions in a controlled way (see question 379).

## 155: How do you configure a producer so it does not lose data?

```properties
acks=all
enable.idempotence=true
retries=2147483647
delivery.timeout.ms=120000
max.in.flight.requests.per.connection=5
```

On the topic or broker side:

```properties
replication.factor=3
min.insync.replicas=2
unclean.leader.election.enable=false
```

In the app, always check the callback or the future for errors, and call `close()` or `flush()` on shutdown. Most of the producer settings above are already the defaults since Kafka 3.0.

## 156: How do acks=all and min.insync.replicas work together?

`acks=all` means "wait for all replicas currently in the ISR". On its own that is weak: if the ISR shrinks to just the leader, `acks=all` only waits for the leader. `min.insync.replicas` sets a floor. With RF 3 and `min.insync.replicas=2`:

- 3 in sync: writes succeed after all 3 have the data.
- 2 in sync: writes still succeed.
- 1 in sync: writes fail with `NOT_ENOUGH_REPLICAS`, and the producer retries until the delivery timeout.

Consumers can still read during this time; only writes are blocked.

## 157: What does enable.idempotence guarantee and what does it not?

It guarantees that one producer instance writes each record to a partition exactly once and in order, even when retries happen. It does this using a producer ID, an epoch and per-partition sequence numbers that the broker checks.

It does **not** protect against:

- the app calling `send()` twice for the same event,
- a restarted producer resending data (it gets a new producer ID unless you use a `transactional.id`),
- duplicates across partitions or across different producers.

For those you need transactions or idempotent consumers.

## 158: How does max.in.flight.requests.per.connection affect ordering?

It limits how many unanswered requests the producer can have per broker connection. Without idempotence, if request 1 fails and request 2 succeeds, the retry of 1 lands after 2 and order is broken.

With idempotence on, the broker uses sequence numbers to keep order for up to 5 in-flight requests, so the default of 5 is safe. Setting it above 5 with idempotence turned on is not allowed. Without idempotence, you need `1` for strict order, which hurts throughput.

## 159: What is the difference between retries and delivery.timeout.ms?

`retries` is the maximum number of retry attempts, and its default is very large (`Integer.MAX_VALUE`). `delivery.timeout.ms` is the total time allowed for a record, including all retries. In practice the timeout is what stops retries.

The recommended approach is to leave `retries` alone and set `delivery.timeout.ms` to how long you are willing to wait. `retry.backoff.ms` and `retry.backoff.max.ms` control the wait between attempts (exponential backoff).

## 160: What happens when the producer's buffer.memory is full?

If records come in faster than the producer can send them, the buffer fills up. Then `send()` blocks for up to `max.block.ms` (60 seconds by default) waiting for space. If there is still no space, it throws a `TimeoutException`.

Blocking in `send()` surprises people who expect it to be fully async. Common causes are a slow or unavailable broker, or too little batching. You can raise `buffer.memory`, improve batching and compression, or slow the producer down.

## 161: How do you tune a producer for throughput?

- Raise `linger.ms` (for example 10-50 ms) so batches fill up.
- Raise `batch.size` (for example 64 KB to 256 KB).
- Turn on compression (`lz4` or `zstd`).
- Give enough `buffer.memory` for the number of partitions you write to.
- Use one shared producer per process instead of many.
- Never block on each send; use callbacks.

Measure with `kafka-producer-perf-test.sh` before and after.

## 162: How do you tune a producer for low latency?

- Keep `linger.ms` low (0 to a few ms).
- Use a fast compression type like `lz4`, or none for tiny messages.
- Keep `acks=all` unless you can accept data loss; the cost of `acks=all` is mostly the follower fetch delay, which is small on a healthy cluster.
- Avoid large batches waiting behind each other.
- Keep brokers healthy: low request queue time, enough network and I/O threads.

Latency and throughput pull against each other, so decide which one you care about more for each topic.

## 163: Which compression type should you choose?

- `lz4`: very fast, good default when you care about CPU and latency.
- `zstd`: best compression ratio at reasonable speed; good for high-volume or text-heavy data and to save network and disk.
- `snappy`: fast, older, still common.
- `gzip`: good ratio but slow and CPU-heavy.

Since Kafka 3.8 you can also set levels, for example `compression.zstd.level`. Test with your own data, since results vary a lot by payload.

## 164: Where is compression applied: producer, broker or topic?

Usually on the producer. The topic setting `compression.type` defaults to `producer`, which means "keep whatever the producer used". If you set the topic to a specific codec and the producer uses a different one, the broker decompresses and recompresses every batch, which costs CPU. Consumers decompress automatically.

## 165: How do you send large messages?

Options, from most to least recommended:

1. **Claim check:** store the payload in S3 or a database, and send a reference (URL or ID) through Kafka.
2. **Compress** the data.
3. **Split** the payload into chunks with a shared ID and reassemble it in the consumer.
4. **Raise limits:** `max.request.size` on the producer, `max.message.bytes` on the topic (or `message.max.bytes` on the broker), and check `replica.fetch.max.bytes` and consumer fetch sizes.

Very large records increase memory use and latency on brokers and clients, so raising limits should be a last resort.

## 166: How do you commit offsets manually?

Turn off auto commit and commit after processing:

```java
props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);

while (running) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
    for (ConsumerRecord<String, String> record : records) {
        process(record);
    }
    if (!records.isEmpty()) {
        consumer.commitSync();
    }
}
```

`commitSync()` with no arguments commits the offsets returned by the last `poll()`. This gives at-least-once processing.

## 167: What is the difference between commitSync and commitAsync?

- `commitSync()` blocks until the commit succeeds or fails, and retries retriable errors. Safer, but slower.
- `commitAsync()` sends the commit and returns at once. It does not retry, because an older commit could arrive after a newer one and move the offset backwards.

A common pattern is `commitAsync()` in the loop for speed and `commitSync()` on shutdown and in `onPartitionsRevoked()`:

```java
try {
    while (running) {
        var records = consumer.poll(Duration.ofMillis(500));
        records.forEach(this::process);
        consumer.commitAsync();
    }
} finally {
    try {
        consumer.commitSync();
    } finally {
        consumer.close();
    }
}
```

## 168: How do you commit specific offsets?

Pass a map of partitions to `OffsetAndMetadata`. Remember to commit the **next** offset to read, which is the last processed offset plus one:

```java
Map<TopicPartition, OffsetAndMetadata> offsets = new HashMap<>();
for (ConsumerRecord<String, String> record : records) {
    process(record);
    offsets.put(new TopicPartition(record.topic(), record.partition()),
                new OffsetAndMetadata(record.offset() + 1));
}
consumer.commitSync(offsets);
```

This is useful when you commit in the middle of a batch or per partition.

## 169: Why is the committed offset the next offset to read and not the last one processed?

Because it represents where to start next time. If you processed offset 41 and commit 41, after a restart the consumer would read 41 again. Committing 42 means "start at 42". The `+ 1` mistake is a classic bug that causes one duplicate per partition on every restart.

## 170: How do you handle a rebalance with ConsumerRebalanceListener?

Pass a listener to `subscribe()` to run code when partitions move:

```java
consumer.subscribe(List.of("orders"), new ConsumerRebalanceListener() {
    @Override
    public void onPartitionsRevoked(Collection<TopicPartition> partitions) {
        // finish work for these partitions and commit before losing them
        consumer.commitSync(currentOffsets);
    }

    @Override
    public void onPartitionsAssigned(Collection<TopicPartition> partitions) {
        // load state or seek for the new partitions
    }

    @Override
    public void onPartitionsLost(Collection<TopicPartition> partitions) {
        // partitions are already owned by someone else; do not commit
    }
});
```

The callbacks run inside `poll()` on the consumer thread.

## 171: What is the eager rebalance protocol?

In the eager approach (the old default), at the start of every rebalance all consumers give up all their partitions, then everyone gets a new assignment. For a moment nobody in the group is consuming anything, the "stop the world" effect. It is simple but painful for big groups or frequent rebalances. Assignors like `RangeAssignor` and `RoundRobinAssignor` use it.

## 172: What is cooperative rebalancing?

Cooperative (incremental) rebalancing only revokes the partitions that actually need to move. Consumers keep working on their other partitions during the rebalance. It can take two rounds: one to revoke the moving partitions, one to assign them to their new owners.

In the classic protocol you enable it with `CooperativeStickyAssignor`. The new consumer protocol (KIP-848) is incremental by design.

## 173: Which partition assignment strategies exist in the classic protocol?

Set with `partition.assignment.strategy`:

- `RangeAssignor`: for each topic, gives each consumer a continuous range of partitions. Can be uneven across many topics.
- `RoundRobinAssignor`: spreads all partitions round-robin over consumers.
- `StickyAssignor`: balanced and tries to keep previous assignments, but eager.
- `CooperativeStickyAssignor`: like sticky, but cooperative.

The default is `[RangeAssignor, CooperativeStickyAssignor]`, which allows rolling a group over to cooperative. These settings do not apply to the new consumer protocol.

## 174: What is the new consumer group protocol from KIP-848?

It is a rewrite of how consumer groups work, generally available since Kafka 4.0:

- The **broker** (group coordinator) computes the assignment instead of a group leader consumer.
- Rebalances are **incremental**: each consumer gets its changes through regular heartbeats, and there is no global "everyone stop and rejoin" barrier.
- A slow or misbehaving consumer does not block the whole group.
- Timeouts and heartbeat intervals are controlled on the broker side.

The result is faster, smoother rebalances, especially in big groups.

## 175: How do you enable the new consumer group protocol?

The broker side is enabled by default in Kafka 4.0+. On the client, set:

```properties
group.protocol=consumer
# optional: choose the server-side assignor (uniform or range)
group.remote.assignor=uniform
```

Client settings like `partition.assignment.strategy`, `session.timeout.ms` and `heartbeat.interval.ms` are not used with this protocol. Session timeout and heartbeat interval are configured on the broker (`group.consumer.session.timeout.ms`, `group.consumer.heartbeat.interval.ms`) or per group with `kafka-configs.sh`. An existing classic group can be moved to the new protocol with a rolling restart of its consumers.

## 176: What is static group membership?

With static membership you give each consumer instance a stable ID with `group.instance.id` (for example the pod name). When that consumer restarts, the coordinator recognizes it and gives back the same partitions without a rebalance, as long as it returns within the session timeout.

```properties
group.instance.id=billing-0
```

It is useful for rolling deploys in Kubernetes where consumers restart one by one. Each instance must have a unique ID.

## 177: What causes frequent rebalances and how do you fix them?

Common causes:

- **Slow processing:** time between polls exceeds `max.poll.interval.ms`. Fix: lower `max.poll.records`, process faster, or raise the interval.
- **Missed heartbeats:** long GC pauses or network trouble. Fix: tune the JVM, raise the session timeout a bit.
- **Rolling deploys:** each restart triggers a rebalance. Fix: static membership, cooperative or KIP-848 protocol.
- **Autoscaling flapping** consumers up and down.
- **Unstable pods** that crash and restart.

Look for "leaving group" or "member was removed" log messages to find which one it is.

## 178: What is CommitFailedException and why does it happen?

It is thrown when a consumer tries to commit offsets for partitions it no longer owns. The typical case: the consumer took longer than `max.poll.interval.ms` to process a batch, so the group kicked it out and reassigned its partitions. When it finally calls `commitSync()`, the commit is rejected.

The records it processed will be processed again by the new owner. Fix the root cause by making each poll loop shorter.

## 179: How do you process messages in parallel with a consumer?

Options:

1. **More consumers:** one consumer per thread or process, up to the partition count. Simplest and keeps per-partition order.
2. **Worker pool per consumer:** the consumer thread polls and hands records to workers. You must track which offsets are done and only commit up to the lowest unfinished one per partition. Use `pause()` to avoid pulling too much.
3. **Per-key parallelism:** process different keys in parallel while keeping order per key. Libraries such as Confluent's Parallel Consumer do this.
4. **Share groups:** let Kafka spread records from one partition to many consumers, if you do not need ordering.

## 180: How do you stop a consumer cleanly?

Call `wakeup()` from another thread (for example a shutdown hook). The blocked `poll()` throws `WakeupException`, and you commit and close in `finally`:

```java
Thread mainThread = Thread.currentThread();
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    consumer.wakeup();
    try { mainThread.join(); } catch (InterruptedException ignored) {}
}));

try {
    consumer.subscribe(List.of("orders"));
    while (true) {
        var records = consumer.poll(Duration.ofMillis(500));
        records.forEach(this::process);
        consumer.commitAsync();
    }
} catch (WakeupException e) {
    // expected on shutdown
} finally {
    try {
        consumer.commitSync();
    } finally {
        consumer.close();
    }
}
```

## 181: How do you pause and resume consuming?

`pause()` stops fetching from some partitions without leaving the group; `poll()` keeps the consumer alive but returns no records for those partitions. `resume()` starts fetching again.

```java
consumer.pause(consumer.assignment());
// ... wait until the downstream system recovers, keep calling poll()
consumer.resume(consumer.paused());
```

This is a simple way to apply backpressure, for example when a database is down or a worker queue is full.

## 182: How do you start consuming from a specific time?

Use `offsetsForTimes()` to find the first offset with a timestamp at or after the given time, then `seek()`:

```java
long ts = Instant.parse("2026-10-01T00:00:00Z").toEpochMilli();
Map<TopicPartition, Long> query = new HashMap<>();
for (TopicPartition tp : consumer.assignment()) {
    query.put(tp, ts);
}
consumer.offsetsForTimes(query).forEach((tp, result) -> {
    if (result != null) {
        consumer.seek(tp, result.offset());
    } else {
        consumer.seekToEnd(List.of(tp));
    }
});
```

From the CLI you can do the same with `--reset-offsets --to-datetime`.

## 183: What are fetch.min.bytes and fetch.max.wait.ms?

They control how long a broker holds a fetch request before answering:

- `fetch.min.bytes` (default 1): the broker waits until at least this much data is available.
- `fetch.max.wait.ms` (default 500): the most it will wait if there is not enough data.

Raising `fetch.min.bytes` gives bigger, more efficient fetches and fewer requests, at the cost of some latency on quiet topics.

## 184: What are max.partition.fetch.bytes and fetch.max.bytes?

- `max.partition.fetch.bytes` (default 1 MB): the max data returned per partition in one fetch.
- `fetch.max.bytes` (default 50 MB): the max data for the whole fetch response.

Both are soft limits: if the first batch is bigger, it is still returned so the consumer can make progress. Raising them helps catch up faster when there is a lot of lag, but uses more memory.

## 185: What is isolation.level?

A consumer setting that controls whether it sees records from transactions that are not committed yet:

- `read_uncommitted` (default): read everything, including records from open or aborted transactions.
- `read_committed`: only read records from committed transactions (and non-transactional records). The consumer can only read up to the last stable offset, which is the first offset of the oldest open transaction.

Use `read_committed` when consuming topics written by transactional producers, like Kafka Streams with exactly-once.

## 186: How do you use a share consumer?

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "image-workers");
props.put("key.deserializer", StringDeserializer.class.getName());
props.put("value.deserializer", StringDeserializer.class.getName());
props.put("share.acknowledgement.mode", "explicit");

try (KafkaShareConsumer<String, String> consumer = new KafkaShareConsumer<>(props)) {
    consumer.subscribe(List.of("image-jobs"));
    while (true) {
        ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
        for (ConsumerRecord<String, String> record : records) {
            try {
                resize(record.value());
                consumer.acknowledge(record, AcknowledgeType.ACCEPT);
            } catch (TemporaryException e) {
                consumer.acknowledge(record, AcknowledgeType.RELEASE);
            } catch (Exception e) {
                consumer.acknowledge(record, AcknowledgeType.REJECT);
            }
        }
        consumer.commitSync();
    }
}
```

You can run many such workers, even more than the topic's partitions. In implicit mode (the default), all records from a poll are accepted when you call `poll()` again or commit.

## 187: Which acknowledgement types does a share consumer support?

- `ACCEPT`: processed successfully. Done.
- `RELEASE`: give it back so it can be delivered again (to this or another consumer). The delivery count goes up.
- `REJECT`: cannot be processed. It is archived and will not be delivered again.
- `RENEW` (added in Kafka 4.2): keep the lock, for records that need more processing time.

If a consumer does not acknowledge a record before its acquisition lock expires (30 seconds by default), the record is released automatically.

## 188: What happens when a record in a share group keeps failing?

Each record has a delivery count. Every time it is delivered, the count goes up. When it reaches the limit (`group.share.delivery.count.limit`, default 5), the record is archived and not delivered again. This stops a poison pill from being retried forever.

Kafka does not move these records to a dead letter topic for you, so if you need one, produce the record to a DLQ topic yourself before rejecting it.

## 189: When should you use a share group instead of a consumer group?

Use a share group when:

- each record is an independent job (send an email, resize an image),
- you do not need ordering,
- you want to scale workers beyond the partition count, or the number of workers changes a lot,
- you want per-record retry and redelivery.

Stick with consumer groups when ordering per key matters, when you do stateful processing, or when you need exactly-once with transactions.

## 190: How do you create topics with the Admin API?

```java
Properties props = new Properties();
props.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");

try (Admin admin = Admin.create(props)) {
    NewTopic topic = new NewTopic("orders", 12, (short) 3)
        .configs(Map.of(
            TopicConfig.RETENTION_MS_CONFIG, "604800000",
            TopicConfig.MIN_IN_SYNC_REPLICAS_CONFIG, "2"));

    admin.createTopics(List.of(topic)).all().get();
} catch (ExecutionException e) {
    if (e.getCause() instanceof TopicExistsException) {
        // fine, it is already there
    } else {
        throw e;
    }
}
```

Admin calls return futures; `all().get()` waits for the result.

## 191: How do you check a consumer group's offsets and lag with the Admin API?

```java
try (Admin admin = Admin.create(props)) {
    Map<TopicPartition, OffsetAndMetadata> committed = admin
        .listConsumerGroupOffsets("billing")
        .partitionsToOffsetAndMetadata().get();

    Map<TopicPartition, OffsetSpec> request = new HashMap<>();
    committed.keySet().forEach(tp -> request.put(tp, OffsetSpec.latest()));
    var latest = admin.listOffsets(request).all().get();

    committed.forEach((tp, om) -> {
        long lag = latest.get(tp).offset() - om.offset();
        System.out.printf("%s lag=%d%n", tp, lag);
    });
}
```

This is how lag exporters work under the hood. `describeConsumerGroups()` gives you the members and their assigned partitions.

## 192: How do you set up a KRaft cluster with separate controllers?

Controller nodes:

```properties
process.roles=controller
node.id=1
listeners=CONTROLLER://:9093
controller.listener.names=CONTROLLER
controller.quorum.bootstrap.servers=ctrl1:9093,ctrl2:9093,ctrl3:9093
log.dirs=/var/lib/kafka/meta
```

Broker nodes:

```properties
process.roles=broker
node.id=4
listeners=PLAINTEXT://:9092
advertised.listeners=PLAINTEXT://broker4:9092
controller.listener.names=CONTROLLER
controller.quorum.bootstrap.servers=ctrl1:9093,ctrl2:9093,ctrl3:9093
log.dirs=/var/lib/kafka/data
```

Format each node with the same cluster ID. The controllers are formatted with the list of initial voters, for example `--initial-controllers` (each entry is `node-id@host:port:directory-id`), and brokers with `--no-initial-controllers`. Then start controllers first, then brokers.

## 193: How many controllers should a KRaft cluster have?

Usually **3**, or **5** for very large or critical clusters. The quorum needs a majority to work: 3 controllers survive 1 failure, 5 survive 2. An even number gives no extra safety (4 also survives only 1 failure). Put controllers in different racks or zones. More than 5 just slows down metadata commits.

## 194: What is combined mode and when is it OK to use?

Combined mode means one process is both a broker and a controller (`process.roles=broker,controller`). It saves machines and is great for local development, tests and small clusters. For production at scale, separate controllers are recommended: a busy broker can starve the controller, and you cannot scale or restart them independently.

## 195: How do you check the status of the KRaft quorum?

```bash
bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 describe --status
bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 describe --replication
```

`--status` shows the current leader (active controller), the epoch, the high watermark and the voters. `--replication` shows each voter's and observer's log end offset and lag, which tells you if any controller or broker is behind on metadata.

## 196: What is a dynamic controller quorum?

Since Kafka 3.9 (KIP-853), the set of controllers can change while the cluster is running. Instead of the fixed `controller.quorum.voters` list, nodes use `controller.quorum.bootstrap.servers` to find the quorum, and you add or remove controllers with:

```bash
bin/kafka-metadata-quorum.sh --command-config controller.properties \
  --bootstrap-controller ctrl1:9093 add-controller

bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 \
  remove-controller --controller-id 3 --controller-directory-id <dir-id>
```

This makes it possible to replace a failed controller disk or move controllers to new machines without downtime.

## 197: What is the __cluster_metadata topic?

It is the internal log where KRaft controllers store every metadata change as a record: topic created, partition leader changed, broker registered, config updated, and so on. The active controller writes to it, the other controllers replicate it through Raft, and brokers read it to keep their metadata cache up to date.

It is periodically compressed into snapshots so new or restarted nodes do not need to replay the whole history. You do not consume it with normal clients, but you can inspect it with `kafka-metadata-shell.sh`.

## 198: How do you migrate from ZooKeeper to KRaft?

Migration has to happen on Kafka 3.x (3.9 is recommended), because 4.x has no ZooKeeper code at all. Roughly:

1. Upgrade the cluster to 3.9 and set the metadata version.
2. Add KRaft controllers configured for migration (`zookeeper.metadata.migration.enable=true`).
3. Restart brokers in migration mode; the controller copies metadata from ZooKeeper (dual-write phase).
4. Restart brokers as pure KRaft brokers.
5. Restart controllers without migration settings, and stop ZooKeeper.

Only after that can you upgrade to 4.x. Practice it in a staging environment first, since rollback is only possible before the final step.

## 199: How do you upgrade a Kafka cluster?

1. Read the upgrade notes for every version you are crossing.
2. Check that clients are new enough (Kafka 4.0 dropped support for clients older than 2.1).
3. Do a rolling upgrade: stop one node, update the binaries, start it, and wait until there are no under-replicated partitions before moving on. Controllers first, then brokers is common.
4. When all nodes run the new version and things look stable, bump the feature level with `kafka-features.sh` to enable new features.

Until step 4 you can usually roll back the binaries. After the metadata version is raised, downgrade may not be possible.

## 200: What are metadata.version and kafka-features.sh?

`metadata.version` is a cluster-wide feature level that says which metadata record formats and features the cluster may use. New binaries keep using the old level until you raise it, which is what makes rolling upgrades and rollbacks safe. Other features (like `transaction.version`, `group.version`, `share.version`) work the same way.

```bash
bin/kafka-features.sh --bootstrap-server localhost:9092 describe
```

`kafka-features.sh upgrade` raises a feature level once every node supports it.

## 201: How do you reassign partitions between brokers?

Use `kafka-reassign-partitions.sh` in three steps:

```bash
# 1. generate a proposal for moving the topics in topics.json to brokers 1,2,3,4
bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 \
  --topics-to-move-json-file topics.json --broker-list "1,2,3,4" --generate

# 2. save the proposed plan to plan.json and execute it with a throttle (bytes/sec)
bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 \
  --reassignment-json-file plan.json --execute --throttle 50000000

# 3. check progress; --verify also removes the throttle when done
bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 \
  --reassignment-json-file plan.json --verify
```

The generated plan is not smart about load; many teams write the plan themselves or use a tool like Cruise Control.

## 202: What is the preferred leader and how do you rebalance leadership?

The preferred leader of a partition is the first replica in its replica list. Kafka tries to keep it as leader so leadership stays evenly spread. After a broker restart, leadership may be lopsided. With `auto.leader.rebalance.enable=true` (default) the controller moves it back periodically. You can also trigger it:

```bash
bin/kafka-leader-election.sh --bootstrap-server localhost:9092 \
  --election-type preferred --all-topic-partitions
```

## 203: How do you add a broker to a cluster?

1. Format its storage with the existing cluster ID and give it a new `node.id`.
2. Start it with the same controller quorum settings. It registers itself and joins.
3. Move partitions onto it with partition reassignment (or Cruise Control), using a throttle so the copy does not hurt production traffic.

Until step 3, the new broker only gets partitions of newly created topics.

## 204: How do you remove a broker from a cluster?

1. Move all its partitions to other brokers with partition reassignment.
2. Check that it no longer hosts any replicas.
3. Shut it down cleanly.
4. Unregister it so the controller forgets it:

```bash
bin/kafka-cluster.sh unregister --bootstrap-server localhost:9092 --id 5
```

If you just turn it off without moving data, its partitions stay under-replicated.

## 205: What is rack awareness and how do you configure it?

Set `broker.rack` on each broker to its rack or availability zone. When topics are created, Kafka spreads the replicas of each partition across different racks, so a whole zone can fail without losing all copies.

```properties
# broker in zone a
broker.rack=eu-west-1a
```

Note that partition reassignment plans you write by hand must also respect racks; the `--generate` option does this for you.

## 206: How can consumers read from the nearest replica?

By default consumers read from the leader, which may be in another zone (and cross-zone traffic costs money in the cloud). With KIP-392 they can read from a follower in their own zone:

```properties
# broker
replica.selector.class=org.apache.kafka.common.replica.RackAwareReplicaSelector

# consumer
client.rack=eu-west-1a
```

Followers may be slightly behind the leader, so end-to-end latency can go up a little, but you never read data that is not committed.

## 207: How do you set up log compaction for a topic?

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create \
  --topic user-profiles --partitions 6 --replication-factor 3 \
  --config cleanup.policy=compact \
  --config min.cleanable.dirty.ratio=0.5 \
  --config segment.ms=3600000 \
  --config delete.retention.ms=86400000
```

Every record must have a key. A smaller `segment.ms` lets compaction run sooner, because the active segment is never compacted.

## 208: What are min.compaction.lag.ms and max.compaction.lag.ms?

- `min.compaction.lag.ms`: a record must be at least this old before compaction can remove it. Gives consumers time to see every update, not just the latest.
- `max.compaction.lag.ms`: the longest a record can stay uncompacted. It forces compaction even when the dirty ratio is low, which helps for deleting data on time (for example GDPR requirements).

## 209: How long do tombstones stay in a compacted topic?

A tombstone stays at least `delete.retention.ms` (1 day by default) after the segment containing it has been compacted. This gives consumers that are reading from the start enough time to see the delete. After that the log cleaner removes it.

If a consumer reads a compacted topic slower than `delete.retention.ms`, it can miss deletes and keep stale keys.

## 210: When would you use cleanup.policy=compact,delete?

When you want the latest value per key, but you also do not want to keep keys forever. For example, a "session state" topic where you only care about sessions active in the last 7 days: compaction keeps one value per session, and time-based retention drops sessions that have not been updated in a week.

## 211: When does Kafka roll a new log segment?

The active segment is closed and a new one started when any of these happens:

- it reaches `segment.bytes` (default 1 GB),
- it is older than `segment.ms` (default 7 days),
- its offset or time index file is full (`segment.index.bytes`),
- an offset would not fit the relative offset format.

Retention and compaction only work on closed segments, so a low-traffic topic with 1 GB segments might keep data much longer than `retention.ms` suggests. Lower `segment.ms` to fix this.

## 212: How does time-based retention actually delete data?

Every `log.retention.check.interval.ms` (5 minutes by default), the broker checks each partition. A closed segment is deleted when its **largest** timestamp is older than `retention.ms`. Since the newest record in the segment must expire first, data can live up to `segment.ms` plus `retention.ms`.

Deletion first renames files with a `.deleted` suffix and removes them after `file.delete.delay.ms`. The partition's log start offset moves forward accordingly.

## 213: What is tiered storage?

Tiered storage (KIP-405, production-ready since Kafka 3.9) keeps recent data on broker disks and moves older closed segments to cheaper remote storage like S3, GCS or Azure Blob. Consumers can still read old data; the broker fetches it from remote storage when needed.

Benefits: much longer retention for less money, smaller broker disks, and faster broker recovery and rebalancing since there is less local data to copy.

## 214: How do you enable tiered storage?

Apache Kafka provides the framework but not the cloud storage plugin itself; you add a `RemoteStorageManager` implementation (for example Aiven's open source plugin for S3, GCS and Azure).

Broker:

```properties
remote.log.storage.system.enable=true
remote.log.storage.manager.class.name=<plugin class>
remote.log.storage.manager.class.path=/opt/kafka/plugins/tiered-storage/*
```

Topic:

```bash
bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter \
  --entity-type topics --entity-name clicks \
  --add-config remote.storage.enable=true,local.retention.ms=86400000,retention.ms=2592000000
```

Here data stays locally for 1 day and remotely for 30 days in total. Compacted topics cannot use tiered storage.

## 215: How do you organize topics in a real project?

Some common rules:

- One topic per event type or per entity stream (for example `orders.events`), owned by one team or service.
- A clear naming pattern that includes the domain.
- Topic configs managed as code (Terraform, Strimzi `KafkaTopic` resources, or a script), not by hand.
- `auto.create.topics.enable=false` in production so typos do not create topics.
- Separate topics for different retention or security needs.
- Document the schema and owner for each topic.

## 216: Should different event types go into one topic or many?

Put events in the **same topic** when you need ordering between them for the same entity. For example `OrderCreated`, `OrderPaid` and `OrderShipped` for one order should be in one topic keyed by `orderId`, so consumers see them in order.

Use **separate topics** when the events are unrelated, have different consumers, or need different retention or access rules. With a schema registry you can store several event types in one topic using union types or a subject naming strategy like `TopicRecordNameStrategy`.

## 217: How do you handle schema evolution?

- Use a schema format that supports evolution (Avro, Protobuf, JSON Schema) and a schema registry.
- Choose a compatibility mode per subject, usually `BACKWARD` or `FULL`.
- Make safe changes: add optional fields with defaults, do not reuse removed field names or numbers, do not change field types.
- Deploy in the right order: with backward compatibility, upgrade consumers first, then producers.
- For breaking changes, create a new topic (or a new major version) and migrate.

## 218: What compatibility modes does a schema registry offer?

In Confluent Schema Registry:

- `BACKWARD` (default): consumers using the new schema can read data written with the previous schema. Example: adding a field with a default.
- `FORWARD`: consumers using the previous schema can read data written with the new schema.
- `FULL`: both backward and forward.
- `_TRANSITIVE` variants (`BACKWARD_TRANSITIVE` and so on): checked against all previous versions, not just the last one.
- `NONE`: no checks.

## 219: How do you use Avro with the Java producer?

With Confluent's serializer:

```java
props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class);
props.put("schema.registry.url", "http://localhost:8081");

try (KafkaProducer<String, Order> producer = new KafkaProducer<>(props)) {
    Order order = Order.newBuilder().setId("o-1").setAmount(20.0).build();
    producer.send(new ProducerRecord<>("orders", order.getId(), order));
}
```

`Order` is a class generated from an `.avsc` file. On first send the serializer registers the schema (if `auto.register.schemas` is on) and caches its ID. In production, schemas are often registered from CI and auto-registration is turned off.

## 220: What wire format do schema registry serializers use?

The common Confluent format puts a small header before the encoded data:

```text
byte 0      magic byte (0)
bytes 1-4   schema ID (big-endian int)
bytes 5+    Avro / Protobuf / JSON payload
```

Protobuf also adds message index info after the ID. This is why a plain `StringDeserializer` shows odd characters at the start of such messages, and why you need the matching deserializer.

## 221: How do you implement retries in a consumer?

Separate errors into two kinds:

- **Temporary** (timeout, database down): retry with backoff. For short retries, retry in place. For longer ones, pause the partition or seek back to the failed offset so the record is fetched again later, without blocking the poll loop past `max.poll.interval.ms`.
- **Permanent** (bad data, validation error): do not retry; send to a dead letter topic.

```java
try {
    process(record);
} catch (TransientException e) {
    consumer.seek(new TopicPartition(record.topic(), record.partition()), record.offset());
    consumer.pause(List.of(new TopicPartition(record.topic(), record.partition())));
    scheduleResume(record, Duration.ofSeconds(5));
    break; // stop processing this batch for the partition
}
```

For longer delays, retry topics with increasing delays are common (see question 376).

## 222: How do you build a dead letter topic yourself?

Catch failures, send the original record to a DLQ topic with extra headers describing the error, then continue:

```java
try {
    process(record);
} catch (Exception e) {
    ProducerRecord<byte[], byte[]> dlq =
        new ProducerRecord<>("orders.dlq", record.key(), record.value());
    dlq.headers().add("error.message", String.valueOf(e.getMessage()).getBytes(UTF_8));
    dlq.headers().add("original.topic", record.topic().getBytes(UTF_8));
    dlq.headers().add("original.partition", Integer.toString(record.partition()).getBytes(UTF_8));
    dlq.headers().add("original.offset", Long.toString(record.offset()).getBytes(UTF_8));
    dlqProducer.send(dlq).get();
}
```

Use byte array deserializers for the DLQ path so even records that failed deserialization can be copied as is. Monitor the DLQ size and have a way to replay it.

## 223: How do you deal with a poison pill that fails deserialization?

If the deserializer throws, `poll()` itself throws a `RecordDeserializationException`, which includes the partition and offset. You can catch it, skip past the bad record, and continue:

```java
try {
    records = consumer.poll(Duration.ofMillis(500));
} catch (RecordDeserializationException e) {
    log.error("bad record at {} offset {}", e.topicPartition(), e.offset(), e);
    consumer.seek(e.topicPartition(), e.offset() + 1);
    continue;
}
```

A cleaner option is to consume raw bytes (`ByteArrayDeserializer`) and deserialize in your own code, so you have the full record to send to a DLQ. Spring Kafka offers `ErrorHandlingDeserializer` for the same purpose.

## 224: How do you make a consumer idempotent?

Make processing the same record twice have the same effect as once:

- **Natural idempotency:** use upserts (`INSERT ... ON CONFLICT DO UPDATE`) or set values instead of incrementing.
- **Deduplication table:** store a unique event ID (or topic-partition-offset) in the same database transaction as the result, and skip IDs you have seen.
- **Store offsets with the data:** save the last processed offset in your database in the same transaction, and on startup `seek()` to it.

```sql
INSERT INTO processed_events (event_id) VALUES ($1) ON CONFLICT DO NOTHING;
-- only apply the change if the insert above affected a row
```

## 225: What is the outbox pattern?

It solves the "write to the database and publish to Kafka" problem. Doing both separately can fail halfway, leaving them out of sync. With the outbox pattern:

1. In the same database transaction as your business change, insert the event into an `outbox` table.
2. A separate process (often Debezium reading the database log, or a poller) reads the outbox table and publishes the events to Kafka.

The database transaction guarantees the event is recorded if and only if the change happened. Publishing is at-least-once, so consumers still need to handle duplicates.

## 226: What is change data capture with Kafka?

Change data capture (CDC) streams every insert, update and delete from a database into Kafka. Log-based CDC tools like Debezium read the database's transaction log (Postgres WAL, MySQL binlog) through Kafka Connect and produce one event per row change, usually keyed by the primary key.

It is used to sync search indexes, caches and data warehouses, to implement the outbox pattern, and to split monoliths without changing their code.

## 227: What is the difference between standalone and distributed Kafka Connect?

- **Standalone:** one worker process, connector configs in local files, offsets in a local file. Good for development or simple one-machine jobs. No fault tolerance.
- **Distributed:** several workers form a group (same `group.id`), and configs, offsets and status are stored in Kafka topics. Connectors are managed through a REST API, and tasks are spread across workers and moved when a worker fails.

Use distributed mode in production.

## 228: Which internal topics does distributed Kafka Connect use?

Configured in the worker properties:

```properties
group.id=connect-cluster
config.storage.topic=connect-configs
offset.storage.topic=connect-offsets
status.storage.topic=connect-status
```

- The config topic holds connector and task configs (must have 1 partition, compacted).
- The offset topic holds source connector offsets (compacted, several partitions).
- The status topic holds connector and task states.

All three should have a replication factor of 3 in production. Sink connectors store their progress as normal consumer group offsets.

## 229: How do you create a connector with the REST API?

```bash
curl -X PUT http://localhost:8083/connectors/orders-sink/config \
  -H "Content-Type: application/json" \
  -d '{
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    "tasks.max": "3",
    "topics": "orders",
    "connection.url": "jdbc:postgresql://db:5432/shop",
    "insert.mode": "upsert",
    "pk.mode": "record_key",
    "auto.create": "true"
  }'
```

`PUT /connectors/{name}/config` creates or updates the connector, so it is safe to run repeatedly. Other useful endpoints: `GET /connectors/{name}/status`, `POST /connectors/{name}/restart`, `PUT /connectors/{name}/pause` and `GET /connector-plugins`.

## 230: What are converters in Kafka Connect?

Converters turn Connect's internal data format into the bytes stored in Kafka and back. They are set with `key.converter` and `value.converter`, on the worker or per connector:

- `org.apache.kafka.connect.json.JsonConverter` (with or without embedded schemas, `value.converter.schemas.enable`)
- `org.apache.kafka.connect.storage.StringConverter`
- `org.apache.kafka.connect.converters.ByteArrayConverter`
- Schema registry converters for Avro, Protobuf and JSON Schema.

A mismatch between the converter used to write and the one used to read is a very common cause of Connect errors.

## 231: What are single message transforms?

Single message transforms (SMTs) are small, per-record changes applied inside a connector: rename or drop fields, add a timestamp, change the topic name, extract a field as the key, and so on.

```json
{
  "transforms": "addTs,route",
  "transforms.addTs.type": "org.apache.kafka.connect.transforms.InsertField$Value",
  "transforms.addTs.timestamp.field": "ingested_at",
  "transforms.route.type": "org.apache.kafka.connect.transforms.RegexRouter",
  "transforms.route.regex": "(.*)",
  "transforms.route.replacement": "cdc.$1"
}
```

You can apply them only to some records using predicates. For anything heavier than simple changes, use a stream processor instead.

## 232: How does error handling work in Kafka Connect?

By default (`errors.tolerance=none`) a task fails on the first bad record. You can make it skip bad records and, for sink connectors, send them to a DLQ:

```json
{
  "errors.tolerance": "all",
  "errors.retry.timeout": "300000",
  "errors.log.enable": "true",
  "errors.log.include.messages": "true",
  "errors.deadletterqueue.topic.name": "orders-sink.dlq",
  "errors.deadletterqueue.context.headers.enable": "true"
}
```

This covers errors in conversion and transforms. Errors inside the connector's own write logic depend on the connector.

## 233: How do you scale a connector?

Raise `tasks.max`. The connector splits its work into up to that many tasks, and Connect spreads them over the workers. How much it can split depends on the connector: a sink connector can use up to one task per topic partition, a JDBC source might use one task per table, and some sources can only use one task. Add more workers if the existing ones run out of CPU or memory.

## 234: What is exactly-once support for source connectors?

Since Kafka 3.3 (KIP-618), source connectors can write records and their source offsets in one Kafka transaction, so after a crash the connector neither skips nor duplicates data in Kafka. You turn it on in distributed workers with:

```properties
exactly.once.source.support=enabled
```

The connector must support it, and consumers of those topics should use `read_committed`. Sink connectors get exactly-once only if the sink system and connector handle it, for example with upserts or by storing offsets in the target.

## 235: How does a Kafka Streams app work in terms of threads and tasks?

- The topology is split into **sub-topologies** (connected parts separated by repartition topics).
- Each sub-topology is split into **tasks**, one per input partition. A task owns its input partitions and its slice of state.
- Tasks run on **stream threads** (`num.stream.threads`, default 1).
- Instances with the same `application.id` share the tasks, using a consumer group under the hood.

So the max parallelism is the number of input partitions. Adding instances or threads spreads the tasks; adding more threads than tasks leaves some idle.

## 236: What is application.id?

`application.id` is the unique name of a Kafka Streams application. It is used as:

- the consumer group ID,
- the prefix for internal topics (`<application.id>-<store>-changelog`, `-repartition`),
- the prefix for client IDs.

All instances of the same app must use the same ID. Changing it is like starting a brand new app with no state and no offsets.

## 237: What are the differences between KStream, KTable and GlobalKTable?

- `KStream`: every record is an independent event.
- `KTable`: a changelog view, latest value per key, **partitioned**. Each instance holds only the keys of its partitions.
- `GlobalKTable`: a full copy of the table on **every** instance. Good for small reference data (countries, product catalog). Joins with it do not need co-partitioning and can use a key taken from the stream's value.

```java
KStream<String, Order> orders = builder.stream("orders");
KTable<String, Customer> customers = builder.table("customers");
GlobalKTable<String, Product> products = builder.globalTable("products");
```

## 238: What are stateless operations in Kafka Streams?

Operations that look at one record at a time and need no stored state: `filter`, `filterNot`, `map`, `mapValues`, `flatMap`, `flatMapValues`, `selectKey`, `peek`, `foreach`, `split` (branching), `merge`, and `to`.

```java
builder.stream("orders", Consumed.with(Serdes.String(), orderSerde))
    .filter((key, order) -> order.amount() > 100)
    .mapValues(order -> order.withFlag("big"))
    .to("big-orders", Produced.with(Serdes.String(), orderSerde));
```

Prefer `mapValues` over `map` when the key does not change; changing the key marks the stream for repartitioning.

## 239: How do you do aggregations in Kafka Streams?

Group the stream, then `count`, `reduce` or `aggregate`. The result is a `KTable` backed by a state store:

```java
KTable<String, Long> totals = orders
    .groupByKey(Grouped.with(Serdes.String(), orderSerde))
    .aggregate(
        () -> 0L,
        (customerId, order, total) -> total + order.cents(),
        Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("totals-by-customer")
            .withValueSerde(Serdes.Long()));

totals.toStream().to("customer-totals", Produced.with(Serdes.String(), Serdes.Long()));
```

`groupBy` (with a new key) causes a repartition; `groupByKey` does not if the key was not changed.

## 240: What is a state store?

A state store is local storage used by stateful operations like aggregations, joins and windows. By default it is RocksDB on local disk (in-memory stores are also available). Each task has its own store for its partitions.

State stores are backed by changelog topics in Kafka, so if an instance dies, another one can rebuild the store. You can also create your own stores for the Processor API and query them with interactive queries.

## 241: What is a changelog topic?

A compacted Kafka topic that records every update to a state store, named `<application.id>-<store>-changelog`. When a task moves to another instance, or after a crash, the store is rebuilt by replaying its changelog. You can turn logging off per store, but then the state cannot be recovered.

## 242: What is a repartition topic?

An internal topic Kafka Streams creates when data has to be re-keyed before a stateful operation, for example after `selectKey()` or `map()` followed by `groupByKey()`, or `groupBy()`. Records are written to `<application.id>-<name>-repartition` with the new key, so that all records with the same key end up in the same partition and the same task.

Repartitioning costs extra network and storage, so avoid changing keys when you do not need to.

## 243: Which window types does Kafka Streams support?

- **Tumbling:** fixed size, no overlap. `TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(5))`
- **Hopping:** fixed size, overlapping. `TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(5)).advanceBy(Duration.ofMinutes(1))`
- **Sliding:** windows defined by the time difference between records. `SlidingWindows.ofTimeDifferenceWithNoGrace(Duration.ofMinutes(5))`
- **Session:** grouped by activity with an inactivity gap. `SessionWindows.ofInactivityGapWithNoGrace(Duration.ofMinutes(30))`
- **Join windows:** for stream-stream joins. `JoinWindows.ofTimeDifferenceWithNoGrace(Duration.ofMinutes(10))`

```java
clicks.groupByKey()
    .windowedBy(TimeWindows.ofSizeAndGrace(Duration.ofMinutes(5), Duration.ofMinutes(1)))
    .count();
```

## 244: What is a grace period?

A grace period is how long a window accepts late records after the window's end. Records with timestamps inside a window that arrive after the window end + grace are dropped (and counted in a "dropped records" metric).

A longer grace handles more late data but delays final results and keeps more state. The `ofSizeWithNoGrace` / `ofSizeAndGrace` methods make you choose explicitly.

## 245: How do you join streams and tables in Kafka Streams?

```java
// stream-table: enrich each order with the current customer
KStream<String, EnrichedOrder> enriched =
    orders.join(customers, (order, customer) -> new EnrichedOrder(order, customer));

// stream-stream: match payments with orders within 10 minutes
KStream<String, Paid> paid = orders.join(
    payments,
    (order, payment) -> new Paid(order, payment),
    JoinWindows.ofTimeDifferenceWithNoGrace(Duration.ofMinutes(10)),
    StreamJoined.with(Serdes.String(), orderSerde, paymentSerde));

// table-table
KTable<String, Profile> profiles = users.join(addresses, Profile::new);
```

Inner, left and outer variants exist. Stream-table joins look up the table's current value at the time the stream record arrives; they are not windowed.

## 246: What is co-partitioning and why do joins need it?

For a `KStream`-`KTable` or `KStream`-`KStream` join, records with the same key must be in the same partition number on both sides, so the same task sees both. This requires:

- both topics have the **same number of partitions**,
- both are keyed by the same key,
- both use the same partitioning logic.

Kafka Streams checks the partition counts and fails if they differ. If not, repartition one side or use a `GlobalKTable`.

## 247: How do you test a Kafka Streams topology?

Use `TopologyTestDriver` from `kafka-streams-test-utils`. It runs the topology in memory without a broker:

```java
try (TopologyTestDriver driver = new TopologyTestDriver(topology, props)) {
    TestInputTopic<String, String> input = driver.createInputTopic(
        "text-input", new StringSerializer(), new StringSerializer());
    TestOutputTopic<String, Long> output = driver.createOutputTopic(
        "word-counts", new StringDeserializer(), new LongDeserializer());

    input.pipeInput("k", "hello hello world");

    Map<String, Long> result = output.readKeyValuesToMap();
    assertEquals(2L, result.get("hello"));
}
```

You can also control time with `advanceWallClockTime()` and read state stores directly. Use Testcontainers for full integration tests.

## 248: What is the Processor API?

The lower-level Kafka Streams API where you write processors that handle one record at a time, access state stores directly and schedule punctuations (timers). Use it when the DSL is not enough, for example for custom deduplication or timeouts.

```java
class Dedup implements Processor<String, String, String, String> {
    private ProcessorContext<String, String> ctx;
    private KeyValueStore<String, Long> seen;

    @Override
    public void init(ProcessorContext<String, String> context) {
        this.ctx = context;
        this.seen = context.getStateStore("seen");
    }

    @Override
    public void process(Record<String, String> record) {
        if (seen.putIfAbsent(record.key(), record.timestamp()) == null) {
            ctx.forward(record);
        }
    }
}

builder.addStateStore(Stores.keyValueStoreBuilder(
    Stores.persistentKeyValueStore("seen"), Serdes.String(), Serdes.Long()));
stream.process(Dedup::new, "seen").to("deduped");
```

The old `transform()` style methods are deprecated or already removed in Kafka 4.x; use `process()` and `processValues()` instead.

## 249: What does suppress() do?

By default a windowed aggregation emits an updated result every time a new record arrives (limited by caching). `suppress()` holds updates back, for example until the window closes, so you get one final result per window:

```java
counts
    .suppress(Suppressed.untilWindowCloses(Suppressed.BufferConfig.unbounded()))
    .toStream()
    .to("final-counts");
```

It is useful for alerts or billing where intermediate results would cause wrong actions. The buffer uses memory, so set limits for high-cardinality data.

## 250: What are interactive queries?

Interactive queries let you read a Kafka Streams app's state stores directly from your code, for example to expose them over HTTP:

```java
ReadOnlyKeyValueStore<String, Long> store = streams.store(
    StoreQueryParameters.fromNameAndType("totals-by-customer",
        QueryableStoreTypes.keyValueStore()));

Long total = store.get("customer-42");
```

Each instance only has some keys. Set `application.server` to each instance's host:port and use `streams.queryMetadataForKey(...)` to find which instance holds a key, then forward the request there.

## 251: How do you handle bad records in Kafka Streams?

Kafka Streams has handler settings for different stages:

```properties
# records that cannot be deserialized
deserialization.exception.handler=org.apache.kafka.streams.errors.LogAndContinueExceptionHandler
# errors thrown by your processing code
processing.exception.handler=org.apache.kafka.streams.errors.LogAndContinueProcessingExceptionHandler
# errors when writing results
production.exception.handler=org.apache.kafka.streams.errors.DefaultProductionExceptionHandler
```

The defaults fail the app, which stops it on the first bad record. `LogAndContinue...` skips and logs. Since Kafka 4.2 the handlers can also send failed records to a dead letter topic with `errors.dead.letter.queue.topic.name`. For uncaught errors, register `streams.setUncaughtExceptionHandler(...)` to decide whether to replace the thread or shut down.

## 252: How does exactly-once work in Kafka Streams?

Set:

```properties
processing.guarantee=exactly_once_v2
```

Each stream thread then uses a transactional producer. Reading input, updating state store changelogs, writing output and committing input offsets all happen in one Kafka transaction. If the app crashes, the open transaction is aborted and the work is redone from the last commit, so the output contains each result once.

It needs brokers 2.5 or newer, and downstream consumers should use `read_committed`. The older `exactly_once` and `exactly_once_beta` values were removed in Kafka 4.0. Commits happen every 100 ms by default in this mode (`commit.interval.ms`).

## 253: How do you use transactions in a producer?

```java
props.put(ProducerConfig.TRANSACTIONAL_ID_CONFIG, "order-writer-1");
KafkaProducer<String, String> producer = new KafkaProducer<>(props);
producer.initTransactions();

try {
    producer.beginTransaction();
    producer.send(new ProducerRecord<>("orders", "o-1", "created"));
    producer.send(new ProducerRecord<>("audit", "o-1", "order created"));
    producer.commitTransaction();
} catch (ProducerFencedException e) {
    producer.close(); // another instance took over this transactional.id
} catch (KafkaException e) {
    producer.abortTransaction();
}
```

Either all records in the transaction become visible to `read_committed` consumers, or none do.

## 254: What does read_committed actually change for consumers?

With `isolation.level=read_committed`:

- records from aborted transactions are filtered out,
- records from open transactions are held back until the transaction finishes,
- the consumer can only read up to the last stable offset (LSO), not the high watermark.

So a long-running or stuck transaction delays all consumers of that partition, even for non-transactional records written after it. Consumer lag metrics can look high in that case.

## 255: What is transactional.id?

`transactional.id` is a stable name for a transactional producer, kept across restarts. When a producer with that ID calls `initTransactions()`, the coordinator:

- finishes or aborts any transaction the previous instance left open,
- bumps the producer epoch, so the old instance (a "zombie") gets fenced if it is still running.

Each logical producer must have its own ID. Two live producers with the same ID will keep fencing each other.

## 256: How do you do a consume-transform-produce loop with transactions?

The key part is `sendOffsetsToTransaction`, which commits the consumer offsets as part of the producer's transaction:

```java
consumer.subscribe(List.of("orders"));   // enable.auto.commit=false, isolation.level=read_committed
producer.initTransactions();

while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
    if (records.isEmpty()) continue;

    producer.beginTransaction();
    try {
        Map<TopicPartition, OffsetAndMetadata> offsets = new HashMap<>();
        for (ConsumerRecord<String, String> r : records) {
            producer.send(new ProducerRecord<>("orders-enriched", r.key(), enrich(r.value())));
            offsets.put(new TopicPartition(r.topic(), r.partition()),
                        new OffsetAndMetadata(r.offset() + 1));
        }
        producer.sendOffsetsToTransaction(offsets, consumer.groupMetadata());
        producer.commitTransaction();
    } catch (ProducerFencedException e) {
        throw e;
    } catch (KafkaException e) {
        producer.abortTransaction();
        resetToLastCommitted(consumer); // seek back so the batch is processed again
    }
}
```

Passing `consumer.groupMetadata()` lets the broker fence zombie instances after a rebalance.

## 257: How do you secure Kafka with TLS?

Configure an SSL listener on the broker with a keystore (its certificate) and, for mutual TLS, a truststore:

```properties
listeners=SSL://:9093
ssl.keystore.type=PKCS12
ssl.keystore.location=/etc/kafka/broker.p12
ssl.keystore.password=changeit
ssl.truststore.location=/etc/kafka/truststore.p12
ssl.truststore.password=changeit
ssl.client.auth=required   # for mTLS
```

Clients:

```properties
security.protocol=SSL
ssl.truststore.location=/etc/client/truststore.p12
ssl.truststore.password=changeit
```

Hostname verification is on by default (`ssl.endpoint.identification.algorithm=https`), so broker certificates must match the advertised hostnames. Keystores can also be given as PEM.

## 258: Which SASL mechanisms does Kafka support?

- `PLAIN`: username and password. Only safe over TLS. Credentials are checked against a file or a custom callback.
- `SCRAM-SHA-256` / `SCRAM-SHA-512`: password based, with salted hashes stored in cluster metadata. Users can be managed at runtime.
- `GSSAPI`: Kerberos.
- `OAUTHBEARER`: OAuth 2 tokens, usually with an OIDC provider.

Use them with `SASL_SSL` in production so traffic is encrypted.

## 259: How do you set up SASL/SCRAM?

Create the user's credentials:

```bash
bin/kafka-configs.sh --bootstrap-server localhost:9092 --command-config admin.properties \
  --alter --entity-type users --entity-name alice \
  --add-config 'SCRAM-SHA-512=[password=alice-secret]'
```

Broker:

```properties
listeners=SASL_SSL://:9094
sasl.enabled.mechanisms=SCRAM-SHA-512
listener.name.sasl_ssl.scram-sha-512.sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required;
```

Client:

```properties
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="alice" password="alice-secret";
```

On a new KRaft cluster you can create the first admin user when formatting storage with `kafka-storage.sh format --add-scram`.

## 260: How do ACLs work in Kafka?

An ACL says: principal P is allowed (or denied) operation O on resource R, from host H. For example `User:billing` may `Read` topic `orders`.

- Resources: Topic, Group, Cluster, TransactionalId, DelegationToken, User.
- Operations: Read, Write, Create, Delete, Alter, Describe, AlterConfigs, DescribeConfigs, IdempotentWrite, All.
- Patterns: literal names or prefixes (`--resource-pattern-type prefixed`).

Deny rules win over allow rules. If no ACL matches, access is denied, unless `allow.everyone.if.no.acl.found=true`.

## 261: How do you create ACLs?

```bash
# allow billing to read orders as part of the billing group
bin/kafka-acls.sh --bootstrap-server localhost:9094 --command-config admin.properties \
  --add --allow-principal User:billing \
  --operation Read --topic orders --group billing

# allow the order service to write any topic starting with "orders."
bin/kafka-acls.sh --bootstrap-server localhost:9094 --command-config admin.properties \
  --add --allow-principal User:order-service \
  --operation Write --operation Describe \
  --topic orders. --resource-pattern-type prefixed

bin/kafka-acls.sh --bootstrap-server localhost:9094 --command-config admin.properties --list
```

Shortcuts `--producer` and `--consumer` add the usual set of ACLs for a producer or consumer.

## 262: What is the StandardAuthorizer?

It is the built-in authorizer for KRaft clusters. ACLs are stored in the cluster metadata log and every broker and controller has them in memory. Enable it on all nodes:

```properties
authorizer.class.name=org.apache.kafka.metadata.authorizer.StandardAuthorizer
super.users=User:admin;User:controller
```

The old ZooKeeper-based `AclAuthorizer` does not exist in Kafka 4.x.

## 263: How do you configure a client to connect with SASL_SSL?

```properties
bootstrap.servers=kafka.example.com:9094
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
  username="billing" password="${env:KAFKA_PASSWORD}";
ssl.truststore.location=/etc/kafka/truststore.p12
ssl.truststore.password=changeit
```

The `${env:...}` syntax works when the env config provider is enabled (`config.providers=env` with `config.providers.env.class=org.apache.kafka.common.config.provider.EnvVarConfigProvider`). Many managed services use certificates trusted by the JVM by default, so the truststore can be skipped there.

## 264: What are quotas?

Quotas limit how much a client can use so one app cannot hurt others:

- `producer_byte_rate`: bytes per second a user or client may produce.
- `consumer_byte_rate`: bytes per second it may fetch.
- `request_percentage`: share of broker request handler and network thread time.
- `controller_mutation_rate`: rate of topic and partition creation and deletion.

When a client goes over, the broker delays its responses (throttling) instead of returning errors.

## 265: How do you set quotas?

```bash
# for one user
bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter \
  --entity-type users --entity-name analytics \
  --add-config 'producer_byte_rate=1048576,consumer_byte_rate=5242880'

# default for all clients that have no specific quota
bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter \
  --entity-type clients --entity-default \
  --add-config 'producer_byte_rate=2097152'
```

Quotas are per broker, not cluster-wide: a user with 1 MB/s on a 3-broker cluster may push up to 3 MB/s in total.

## 266: Which broker metrics should you monitor?

- `UnderReplicatedPartitions` and `UnderMinIsrPartitionCount`: should be 0.
- `OfflinePartitionsCount`: should be 0.
- `ActiveControllerCount`: exactly 1 across the cluster.
- `RequestHandlerAvgIdlePercent` and `NetworkProcessorAvgIdlePercent`: low values mean the broker is overloaded.
- Request latency (`TotalTimeMs` per request type, especially Produce and Fetch).
- `BytesInPerSec`, `BytesOutPerSec`, `MessagesInPerSec`.
- `IsrShrinksPerSec` / `IsrExpandsPerSec`: frequent changes mean unstable replicas.
- OS level: disk usage, disk I/O wait, network, CPU, GC pauses.

## 267: Which producer and consumer metrics should you monitor?

Producer:

- `record-error-rate`, `record-retry-rate`
- `request-latency-avg`, `record-queue-time-avg`
- `batch-size-avg`, `compression-rate-avg`
- `buffer-available-bytes`, `bufferpool-wait-time-ns-total`

Consumer:

- `records-lag-max` and per-partition lag
- `records-consumed-rate`, `fetch-latency-avg`
- `commit-latency-avg`, `rebalance-rate-per-hour`, `failed-rebalance-total`
- `last-poll-seconds-ago`, `time-between-poll-avg`

## 268: How do you monitor consumer lag in production?

Client-side lag metrics vanish when the consumer is down, which is exactly when you need them. So measure lag from outside too:

- Burrow or Kafka Lag Exporter style tools that read committed offsets and log end offsets and export them to Prometheus.
- The Admin API (question 191) in your own exporter.
- Managed services usually expose lag in their dashboards.

Alert on lag that keeps growing, or on lag measured in time ("we are 10 minutes behind"), rather than on a fixed record count, since the right count depends on the traffic.

## 269: What is an under-replicated partition?

A partition whose ISR is smaller than its replica list, meaning at least one follower is not caught up. Causes include a broker being down, a slow disk, network trouble, or a broker overloaded with requests. It is the most important broker health metric: if more replicas drop out, you may lose availability or, with unclean elections, data.

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

## 270: What is an offline partition?

A partition with no leader. Producers and consumers cannot use it at all. It usually means all replicas in the ISR are down. With unclean leader election off, it stays offline until one of those brokers comes back. Any value above 0 for `OfflinePartitionsCount` should page someone.

## 271: How do you look inside a log segment file?

```bash
bin/kafka-dump-log.sh --files /var/lib/kafka/data/orders-0/00000000000000000000.log \
  --print-data-log
```

It prints batches with base offset, producer ID, sequence, timestamps, compression and the record contents. It also works for index files and for the `__cluster_metadata` log (with `--cluster-metadata-decoder`). Useful for debugging transactions, compaction and corrupted data.

## 272: How do you debug a "message too large" error?

Find which limit is hit:

- Producer `RecordTooLargeException`: the record is bigger than `max.request.size`, or bigger than `buffer.memory`.
- Broker error `MESSAGE_TOO_LARGE`: the batch is bigger than the topic's `max.message.bytes` (or broker `message.max.bytes`).
- Followers cannot replicate it: check `replica.fetch.max.bytes` (it is a soft limit in recent versions, but check anyway).

Remember that the limit applies to the compressed batch. Fix by compressing, splitting, or using the claim check pattern before raising limits.

## 273: How do you debug a consumer that is not receiving messages?

Check in order:

1. Is it connected? Look for `advertised.listeners` or auth errors in logs.
2. Is it subscribed to the right topic name, and does the topic have data (`kafka-get-offsets.sh`)?
3. Does it have partitions assigned? `kafka-consumer-groups.sh --describe` shows owners. More consumers than partitions leaves some idle.
4. Where is its offset? A new group with `auto.offset.reset=latest` only sees new data.
5. Is the producer using transactions while the consumer uses `read_committed` and a transaction is stuck open?
6. Are deserialization errors being swallowed?
7. Do ACLs allow `Read` on the topic and the group?

## 274: How do you debug a producer that times out?

A `TimeoutException` from the producer can mean:

- **"Topic not present in metadata after 60000 ms":** the topic does not exist (and auto-create is off), the client cannot reach brokers, or it lacks `Describe` permission.
- **"Expiring N records... since batch creation":** batches waited longer than `delivery.timeout.ms`. The leader is unreachable or slow, `min.insync.replicas` is not met, or the client is sending more than the network can carry.
- **Blocked in `send()`:** the buffer is full (`max.block.ms`).

Look at broker health, the producer's `record-queue-time-avg` and `request-latency-avg`, and network connectivity to every broker, not just the bootstrap one.

## 275: What happens to ordering when retries happen without idempotence?

Say batch A and then batch B are in flight to the same partition. A fails with a temporary error, B succeeds, then A is retried and succeeds. The log now has B before A. Without idempotence the only fix is `max.in.flight.requests.per.connection=1`, which slows things down. With idempotence (the default), the broker rejects B until A is in place, so order is kept with up to 5 in-flight requests.

## 276: How do you handle duplicates downstream?

Assume at-least-once and design for it:

- Give every event a unique ID set by the producer at creation time (not at send time).
- Make writes idempotent (upserts, conditional updates with version numbers).
- Keep a deduplication store of processed IDs, with a TTL that is longer than any realistic redelivery window.
- For Kafka-to-Kafka processing, use transactions or Kafka Streams with exactly-once.

## 277: How do you delete records from a topic?

You can delete everything before a given offset in a partition (it moves the log start offset forward):

```bash
cat > delete.json <<'EOF'
{"partitions": [{"topic": "orders", "partition": 0, "offset": 1000}], "version": 1}
EOF

bin/kafka-delete-records.sh --bootstrap-server localhost:9092 --offset-json-file delete.json
```

You cannot delete a single record in the middle of a partition. For key-based deletion, use a compacted topic and tombstones. The Admin API has `deleteRecords()` for the same thing.

## 278: When should you use LogAppendTime instead of CreateTime?

`CreateTime` (default) keeps the producer's timestamp, which is the event time and what you usually want for windowing. But producers with wrong clocks can write timestamps in the future or far past, which messes up time-based retention and `offsetsForTimes()`.

`LogAppendTime` makes the broker set the time. It is reliable and always increasing per partition, which is good for audit logs and time-based lookups, but you lose the original event time unless you also put it in the value or a header. Brokers can also reject records with timestamps too far off using `log.message.timestamp.before.max.ms` and `log.message.timestamp.after.max.ms`.

## 279: How do you use headers for tracing?

Put trace context in headers when producing and read it when consuming, so a request can be followed across services. OpenTelemetry has instrumentation for the Java Kafka clients (and others) that does this automatically using the W3C `traceparent` header.

```java
record.headers().add("traceparent", traceParent.getBytes(UTF_8));

// consumer side
Header h = consumerRecord.headers().lastHeader("traceparent");
String traceParent = h == null ? null : new String(h.value(), UTF_8);
```

## 280: How do you run Kafka on Kubernetes?

Kafka needs stable identities and persistent disks, so it runs as StatefulSets (or operator-managed pods) with PersistentVolumes. Things to get right:

- stable DNS names per broker and proper `advertised.listeners` for clients inside and outside the cluster,
- pod anti-affinity and zone spreading, matching `broker.rack`,
- PodDisruptionBudgets so upgrades do not take down several brokers at once,
- fast storage classes and enough memory for the page cache.

Most teams use an operator like Strimzi instead of writing this by hand.

## 281: What is Strimzi?

Strimzi is an open source Kubernetes operator (a CNCF project) for running Kafka. You describe the cluster with custom resources and the operator creates and manages everything:

```yaml
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: orders
  labels:
    strimzi.io/cluster: my-cluster
spec:
  partitions: 12
  replicas: 3
  config:
    retention.ms: 604800000
```

Other resources include `Kafka`, `KafkaNodePool`, `KafkaUser`, `KafkaConnect`, `KafkaConnector` and `KafkaMirrorMaker2`. It handles rolling upgrades, certificates and scaling. Recent Strimzi versions only support KRaft.

## 282: How do you set up MirrorMaker 2?

The simplest way is the dedicated MM2 driver with a properties file:

```properties
clusters = primary, backup
primary.bootstrap.servers = primary-kafka:9092
backup.bootstrap.servers = backup-kafka:9092

primary->backup.enabled = true
primary->backup.topics = orders.*, payments.*
primary->backup.groups = .*

replication.factor = 3
sync.group.offsets.enabled = true
emit.checkpoints.enabled = true
```

```bash
bin/connect-mirror-maker.sh mm2.properties
```

You can also run the MM2 connectors (`MirrorSourceConnector`, `MirrorCheckpointConnector`, `MirrorHeartbeatConnector`) in an existing Connect cluster.

## 283: How does MirrorMaker 2 name the copied topics?

With the default `DefaultReplicationPolicy`, a topic `orders` from cluster `primary` becomes `primary.orders` on the target. This prevents loops in two-way replication and makes it clear where data came from. If you want the same name on both sides (common for one-way disaster recovery), use `IdentityReplicationPolicy`, but then you must avoid replicating in both directions for the same topic.

## 284: How do you move consumer offsets between clusters?

Offsets in two clusters do not match, because each cluster assigns its own offsets. MM2's checkpoint connector keeps a mapping and writes translated offsets to a `<source>.checkpoints.internal` topic on the target. With `sync.group.offsets.enabled=true`, it also writes them directly into the target's consumer groups (for groups that are not active there).

In code you can use `RemoteClusterUtils.translateOffsets(...)`. After failover, consumers start close to where they were, but expect some reprocessing.

## 285: How does Kafka compare to Amazon SQS and Kinesis?

- **SQS:** a managed queue. Each message is handled by one consumer and deleted. Very simple to run, scales automatically, but no replay and (except FIFO queues) no ordering.
- **Kinesis Data Streams:** the closest AWS service to Kafka. Shards are like partitions, data is kept for a set time, consumers track their position. Simpler to run but with lower per-shard limits and less ecosystem.
- **Kafka:** more features (compaction, transactions, Connect, Streams), higher throughput, works across clouds, but you run it yourself or pay for a managed service.

## 286: How do you use Kafka with Spring Boot?

Add `spring-kafka`, configure in `application.yml`, then use `KafkaTemplate` and `@KafkaListener`:

```yaml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    consumer:
      group-id: billing
      auto-offset-reset: earliest
```

```java
@Service
class OrderEvents {
    private final KafkaTemplate<String, String> kafka;

    OrderEvents(KafkaTemplate<String, String> kafka) {
        this.kafka = kafka;
    }

    void publish(String orderId, String json) {
        kafka.send("orders", orderId, json);
    }

    @KafkaListener(topics = "orders", concurrency = "3")
    void onOrder(ConsumerRecord<String, String> record) {
        // process
    }
}
```

Spring Kafka adds error handlers with retries and DLQ publishing (`DefaultErrorHandler`, `DeadLetterPublishingRecoverer`) and non-blocking retry topics with `@RetryableTopic`.

## 287: How do you use Kafka with NestJS?

NestJS has a Kafka transport in `@nestjs/microservices` (it uses KafkaJS under the hood):

```ts
// main.ts
const app = await NestFactory.createMicroservice<MicroserviceOptions>(
  AppModule,
  {
    transport: Transport.KAFKA,
    options: {
      client: { brokers: ["localhost:9092"] },
      consumer: { groupId: "billing" },
    },
  },
);
await app.listen();
```

```ts
@Controller()
export class OrdersController {
  @EventPattern("orders")
  handleOrder(@Payload() order: OrderDto) {
    // process the event
  }
}
```

To produce, register a client with `ClientsModule.register(...)` and call `client.emit("orders", payload)`. For more control, some teams use a Kafka client library directly inside a Nest provider.

## 288: Which Node.js Kafka clients exist and which should you pick?

- **`@confluentinc/kafka-javascript`:** Confluent's client built on librdkafka, actively maintained, with a KafkaJS-compatible API and a node-rdkafka-style API. A good default for new projects.
- **KafkaJS:** pure JavaScript and very popular, but it has not had a release in years and does not support newer features.
- **node-rdkafka:** older librdkafka binding; the Confluent client grew out of it.
- **@platformatic/kafka:** a newer pure JavaScript client.

Native (librdkafka) clients are faster and support more features, but need native builds. Pure JS clients are easier to install.

## 289: How do you shut down a Node.js consumer gracefully?

Disconnect on process signals so the consumer commits offsets and leaves the group right away:

```js
const shutdown = async () => {
  try {
    await consumer.disconnect();
    await producer.disconnect();
  } finally {
    process.exit(0);
  }
};

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
```

In Kubernetes, make sure `terminationGracePeriodSeconds` is long enough for in-flight messages to finish.

## 290: How do you process messages in batches in Node.js?

Use `eachBatch` instead of `eachMessage`:

```js
await consumer.run({
  eachBatch: async ({ batch, heartbeat }) => {
    const rows = batch.messages.map((m) => JSON.parse(m.value.toString()));
    await db.insertMany(rows); // one database call for the whole batch
    await heartbeat();
  },
});
```

The batch's offsets are committed after the handler finishes successfully. If it throws, the batch is retried. Batching is much faster for writing to databases.

## 291: How do you write integration tests against a real Kafka?

Use Testcontainers to start Kafka in Docker for the test:

```java
@Testcontainers
class OrderFlowTest {
    @Container
    static KafkaContainer kafka = new KafkaContainer("apache/kafka-native:4.3.1");

    @Test
    void publishesOrder() {
        Map<String, Object> props = Map.of(
            "bootstrap.servers", kafka.getBootstrapServers(),
            "key.serializer", StringSerializer.class,
            "value.serializer", StringSerializer.class);
        // create producer and consumer, run the flow, assert on output
    }
}
```

`org.testcontainers.kafka.KafkaContainer` works with the `apache/kafka` and `apache/kafka-native` images. Testcontainers exists for Node.js, Python and Go as well. Spring also offers `@EmbeddedKafka` for in-process tests.

## 292: How do you unit test producers and consumers without a broker?

The Java client ships `MockProducer` and `MockConsumer`:

```java
MockProducer<String, String> producer =
    new MockProducer<>(true, null, new StringSerializer(), new StringSerializer());
OrderPublisher publisher = new OrderPublisher(producer);

publisher.publish("o-1", "created");

assertEquals(1, producer.history().size());
assertEquals("o-1", producer.history().get(0).key());
```

`MockConsumer` lets you add records and assign partitions by hand. Keep your business logic in plain classes so most tests do not need Kafka at all.

## 293: Can you get global ordering across a whole topic?

Only by using a single partition. Then every record is in one total order, but you also limit throughput to one partition and one consumer per group. Usually you do not need global order, only order per entity, which keys give you. If you really need a total order across many partitions, you have to add your own sequence numbers and reorder on the consumer side, which is complex.

## 294: Which retention setting wins: log.retention.hours or log.retention.ms?

At broker level there are three: `log.retention.ms`, `log.retention.minutes` and `log.retention.hours`. The most precise one that is set wins: ms over minutes over hours. A topic-level `retention.ms` overrides all of them for that topic. This trips people up when the hours setting is changed in `server.properties` but an ms setting is also present.

## 295: How would you configure a topic that must never lose data?

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic payments \
  --partitions 12 --replication-factor 3 \
  --config min.insync.replicas=2 \
  --config unclean.leader.election.enable=false \
  --config retention.ms=-1
```

Plus producers with `acks=all` and idempotence, brokers in at least three zones with `broker.rack`, monitoring of under-min-ISR partitions, and a second copy of the data (MirrorMaker 2 to another cluster or tiered storage). Remember that Kafka acknowledges after data is in memory on several brokers, not after `fsync`, so replication across failure domains is what protects you.

## 296: What happens to offsets of a consumer group that stops running?

Committed offsets are kept for `offsets.retention.minutes` (7 days by default), counted from when the group becomes empty. After that they are deleted. When the group starts again, it has no offsets and falls back to `auto.offset.reset`, which might mean skipping data (`latest`) or reprocessing everything (`earliest`).

If a service can be down for longer than a week, raise this setting or store offsets somewhere else.

## 297: How do you delete a consumer group?

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --delete --group old-billing
```

The group must have no active members. You can also delete offsets for one topic only with `--delete-offsets --group billing --topic orders`, which is handy after a group stops reading a topic. The Admin API has `deleteConsumerGroups()` and `deleteConsumerGroupOffsets()`.

## 298: What is the transaction coordinator?

The transaction coordinator is a broker component that manages transactions for producers. Each `transactional.id` maps to one partition of the internal `__transaction_state` topic, and the leader of that partition is its coordinator. It:

- assigns producer IDs and epochs and fences zombies,
- records which partitions are part of each transaction,
- runs the two-phase commit: writes "prepare commit" to its log, then writes commit or abort markers to every partition in the transaction,
- aborts transactions that pass `transaction.timeout.ms`.

## 299: What are producer and consumer interceptors?

Interceptors are classes that run on every record in the client, set with `interceptor.classes`:

- `ProducerInterceptor`: `onSend()` before serialization, `onAcknowledgement()` when the broker answers.
- `ConsumerInterceptor`: `onConsume()` before records are returned from `poll()`, `onCommit()` after commits.

They are used for adding headers, metrics, auditing and tracing. They should be fast and must not throw, since they run on the client's hot path.

## 300: How do you choose the replication factor and min.insync.replicas?

- **RF 3, min ISR 2:** the standard for production. Writes survive one broker failure and every acknowledged write is on two brokers.
- **RF 3, min ISR 1:** higher availability but an acknowledged write may be on a single broker.
- **RF 1:** only for development or data you can regenerate.
- **RF 5, min ISR 3:** for very critical data or stretched clusters across more zones, at the cost of more storage and network.

`min.insync.replicas` should be lower than RF, otherwise one broker restart blocks all writes.

# Advanced Questions (301-450)

## 301: How does Kafka store data on disk?

Each partition replica is a directory in one of the `log.dirs`, named `<topic>-<partition>`. Inside, the log is split into segments. Each segment is a set of files named after the first offset it contains:

```text
orders-0/
  00000000000000000000.log        record batches
  00000000000000000000.index      offset -> file position
  00000000000000000000.timeindex  timestamp -> offset
  00000000000000052310.log
  00000000000000052310.index
  00000000000000052310.timeindex
  00000000000000052310.snapshot   producer state (idempotence)
  leader-epoch-checkpoint
  partition.metadata
```

Writes only append to the newest `.log` file. Reads find the right segment by base offset, use the index to jump close to the wanted offset, then scan forward.

## 302: What are the other files in a partition directory for?

- `.snapshot`: producer state (last sequence numbers per producer ID), so idempotence still works after a restart.
- `.txnindex`: list of aborted transactions in the segment, used to filter them for `read_committed` consumers.
- `leader-epoch-checkpoint`: the leader epoch history, used for truncation after leader changes.
- `partition.metadata`: the topic ID, so a recreated topic with the same name is not confused with the old one.
- `.deleted`, `.cleaned`, `.swap`: temporary files during deletion and compaction.

## 303: How do the offset and time indexes work?

They are **sparse** indexes, memory-mapped files with fixed-size entries:

- The offset index maps a relative offset to a byte position in the `.log` file. An entry is added about every `index.interval.bytes` (4 KB) of data.
- The time index maps a timestamp to an offset, also sparse.

To find offset N, the broker binary-searches the segment list by base offset, binary-searches the index for the largest entry at or below N, then scans the log from that position. Because the index is small and memory-mapped, lookups are fast and need very little memory.

## 304: How does Kafka use the page cache?

Kafka writes to the file system and lets the OS cache the data in RAM (the page cache), instead of keeping its own cache on the JVM heap. Benefits:

- Recently written data is served to consumers straight from memory, so "tailing" consumers rarely touch the disk.
- The cache survives broker process restarts.
- The JVM heap stays small (often 4-8 GB), which keeps GC pauses short.

This is why Kafka machines should have lots of free RAM beyond the heap, and why a consumer reading old data (a cold read) can slow others by pushing hot data out of the cache. Tiered storage reads can help keep cold reads off local disks.

## 305: What is zero-copy and when does it not apply?

For fetch requests, the broker uses the `sendfile` system call (`FileChannel.transferTo` in Java) to send data straight from the page cache to the network socket, without copying it into the JVM. This saves CPU and memory bandwidth. It works because data on disk is in the same format that is sent to consumers.

It does **not** work with TLS, because the data has to be encrypted in user space first. So enabling TLS raises CPU use on brokers, though modern CPUs with AES instructions keep the cost moderate.

## 306: How does a broker handle requests internally?

1. **Acceptor thread** accepts new connections for each listener.
2. **Network threads** (`num.network.threads`, default 3) read requests from sockets and put them in a shared request queue, then later write responses back.
3. **I/O (request handler) threads** (`num.io.threads`, default 8) take requests from the queue and do the work: append to the log, read data, update metadata.
4. Requests that must wait (`acks=all` produce, fetch waiting for data) are parked in **purgatory** until they can complete or time out.
5. The response goes to a response queue and a network thread sends it.

Metrics for each step (request queue time, local time, remote time, response queue time) tell you where latency comes from.

## 307: What is request purgatory?

Purgatory is where the broker keeps requests that cannot be answered yet:

- A produce request with `acks=all` waits until all ISR followers have the data.
- A fetch request waits until `fetch.min.bytes` is available or `fetch.max.wait.ms` passes.
- Some group and transaction operations wait for other events.

It uses a hierarchical timing wheel, so tracking millions of pending requests and their timeouts is cheap. A growing purgatory size usually means slow followers or slow replication.

## 308: How does replication work at the protocol level?

Followers act like consumers: they send `Fetch` requests to the leader, asking for data from their log end offset. The leader returns new records, and the fetch offset tells the leader how far each follower has got. That is how the leader tracks follower progress, updates the ISR, and advances the high watermark. The leader includes the current high watermark in fetch responses, so followers learn it too.

Followers use `num.replica.fetchers` threads per source broker, and one fetch request covers many partitions at once.

## 309: How does the high watermark advance?

The leader knows each follower's log end offset from its fetch requests. The high watermark is the smallest log end offset among the ISR members. When the slowest ISR member fetches past a point, the high watermark moves up, and any waiting `acks=all` produce requests up to that point are completed.

A follower that is slow enough gets dropped from the ISR, after which it no longer holds the high watermark back. That is the trade-off `replica.lag.time.max.ms` controls.

## 310: What is the leader epoch and why was it added?

The leader epoch is a number that goes up every time a partition gets a new leader. Each batch is tagged with the epoch of the leader that wrote it, and each replica keeps a history of (epoch, start offset) in `leader-epoch-checkpoint`.

It was added (KIP-101) because truncating followers based only on the high watermark could lose data or leave replicas with different data after quick leader changes. With epochs, a follower asks the new leader "where did epoch X end?" and truncates to exactly that point, so all replicas end up with the same log.

## 311: How does log truncation work after a leader change?

When a follower starts following a new leader, it may have records the new leader never got (they were written to the old leader but not committed). The follower sends an `OffsetForLeaderEpoch` request (now part of the fetch protocol) with its latest epoch. The leader answers with the end offset of that epoch in its own log. The follower truncates anything after that offset and then fetches normally.

Only uncommitted data (above the high watermark) can be truncated this way, which is why `acks=all` writes are safe.

## 312: What are eligible leader replicas (ELR)?

ELR (KIP-966) is a newer feature that closes a gap in leader election. Normally, when the ISR shrinks to one replica and that one fails, the controller can only wait or do an unclean election. With ELR, the controller tracks replicas that were removed from the ISR only because the ISR fell below `min.insync.replicas`, and which are known to have all committed data. Those replicas can still be safely elected.

It also changes ISR handling so the ISR is not shrunk below `min.insync.replicas` in a way that loses this information. It shipped as a preview in 4.0 and is enabled through the `eligible.leader.replicas.version` feature; check `kafka-features.sh describe` to see if your cluster has it on.

## 313: How does the Raft protocol work in KRaft?

KRaft uses a Kafka-flavored Raft:

- Controllers are **voters**. One is elected leader for an **epoch** by getting votes from a majority.
- The leader appends metadata records to the `__cluster_metadata` log.
- Unlike classic Raft where the leader pushes data, followers and observers **pull** from the leader with fetch requests, just like partition replication.
- A record is committed when a majority of voters have it; that moves the high watermark.
- If followers stop hearing from the leader (fetch timeout), they start an election with a new epoch.

Brokers are **observers**: they fetch the log but do not vote.

## 314: How do brokers get metadata in KRaft?

Each broker fetches the `__cluster_metadata` log from the active controller and applies each record to an in-memory metadata image. Changes are pushed as deltas, so a broker only processes what changed. Brokers also send heartbeats to the controller to stay registered and unfenced.

Compared to ZooKeeper mode, there is no big "send everyone the full state" request when something changes, which is why KRaft handles many more partitions and recovers faster.

## 315: What are metadata snapshots?

Over time the metadata log gets long. Controllers and brokers periodically write a snapshot: the full metadata state at a given offset. Older log entries before the snapshot can then be deleted. A new or restarting node loads the latest snapshot and only replays records after it.

Snapshot frequency is controlled by settings like `metadata.log.max.record.bytes.between.snapshots` and `metadata.log.max.snapshot.interval.ms`.

## 316: What happens when the active controller fails?

1. The other controllers stop getting fetch responses from it.
2. After the election timeout, one of them starts an election with a higher epoch, and the controller with an up-to-date log wins a majority.
3. The new active controller already has the full metadata in memory (it was following the log), so it can start right away, unlike the old ZooKeeper controller, which had to reload everything.
4. Brokers find the new leader and continue fetching metadata.

Failover usually takes from well under a second to a few seconds. Partition leaders keep serving clients the whole time; only metadata changes are paused.

## 317: How does broker fencing work in KRaft?

Brokers send heartbeats to the active controller every `broker.heartbeat.interval.ms` (2 s). If a broker misses heartbeats for `broker.session.timeout.ms` (9 s), the controller **fences** it: marks it as not available, moves leadership of its partitions to other replicas, and removes it from ISRs. A fenced broker is not given new leaderships.

A broker that starts up is also fenced until it has caught up with metadata. During a clean shutdown, the broker asks to be fenced first so leadership moves away before it stops (controlled shutdown).

## 318: How does the idempotent producer work internally?

1. On startup the producer gets a **producer ID (PID)** and **epoch** from a broker.
2. For each partition, it numbers batches with an increasing **sequence number**.
3. The partition leader stores, per PID, the sequence numbers of the last 5 batches.
4. When a batch arrives:
   - next expected sequence: append it,
   - already seen: return success without writing again (duplicate),
   - a gap: return `OUT_OF_ORDER_SEQUENCE_NUMBER`.

This state is stored in producer snapshot files and rebuilt from the log, so it survives leader changes. Producer IDs that have been idle for `producer.id.expiration.ms` (1 day by default) are removed.

## 319: How do transactions work internally?

1. `initTransactions()`: the producer finds its coordinator (by hashing `transactional.id` onto `__transaction_state`), gets a PID and a bumped epoch; any open transaction from a previous instance is completed or aborted.
2. Before sending to a new partition in the transaction, the partition is registered with the coordinator (with KIP-890's newer transaction version, the broker handles this for the client).
3. Records are written to partitions normally, marked as transactional.
4. `sendOffsetsToTransaction()` registers the group's `__consumer_offsets` partition and writes the offsets as transactional.
5. `commitTransaction()`: the coordinator writes `PrepareCommit` to its log, then writes **commit markers** to every partition involved, then `CompleteCommit`.

Consumers in `read_committed` mode use these markers to decide what to show.

## 320: What are transaction markers and control records?

A transaction marker is a special record (a control record) written by the coordinator into each partition that was part of a transaction. It says "the transaction from PID X, epoch Y is committed" or "aborted". Control records take an offset but are never returned to applications. This is why offsets in transactional topics have gaps, and why "last offset minus first offset" does not equal the record count.

## 321: What is the last stable offset?

The last stable offset (LSO) is the first offset of the oldest transaction that is still open in a partition (or the high watermark if there is none). `read_committed` consumers can only read up to the LSO, because they do not yet know whether later records will be committed or aborted.

A transaction that stays open for a long time freezes the LSO, so `read_committed` consumers stop making progress on that partition, even for other producers' records.

## 322: What is a hanging transaction and how do you fix it?

A hanging transaction is one that was started on a partition but whose markers were never written, so the coordinator does not know about it or failed to finish it. The LSO stays stuck, `read_committed` consumers stall and compaction cannot clean past it. Older client and broker bugs could cause this.

You can find and abort them with:

```bash
bin/kafka-transactions.sh --bootstrap-server localhost:9092 find-hanging --broker-id 1
bin/kafka-transactions.sh --bootstrap-server localhost:9092 abort \
  --topic orders --partition 3 --start-offset 125000
```

Newer brokers verify partitions against the coordinator before accepting transactional writes (KIP-890), which prevents most cases.

## 323: What did KIP-890 change for transactions?

KIP-890 ("transactions server-side defense") fixes several ways transactions could hang or let zombie data in:

- **Part 1 (Kafka 3.6+):** a partition leader checks with the coordinator that a transactional write belongs to an ongoing transaction before accepting it.
- **Part 2 (Kafka 4.0, transaction version 2):** the producer epoch is bumped on every transaction, so late writes from an earlier transaction are rejected; the client no longer has to send a separate request to add partitions to the transaction.

The result is that a delayed or retried message from a previous transaction cannot sneak into a new one.

## 324: What are the limits of exactly-once in Kafka?

- It covers **Kafka to Kafka** only: reading topics, writing topics, committing offsets. Side effects like sending an email or calling an API are not undone if the transaction aborts.
- Consumers must use `read_committed`, otherwise they see aborted data.
- Transactions add latency (commit markers, waiting for the commit interval).
- One `transactional.id` per producer instance, and zombie fencing must be set up properly.
- External sinks need their own idempotency or must store offsets transactionally with the data.

## 325: How does the group coordinator store its state?

All consumer group state (members, assignments, committed offsets, and for share groups their metadata) is written as records to the `__consumer_offsets` partition that the group maps to. The coordinator keeps an in-memory view and rebuilds it by replaying the partition when it becomes leader. Since Kafka 4.0, the coordinator runtime is a rewritten, event-based component that handles both classic and new protocol groups.

Because state is in a replicated, compacted topic, coordinator failover just means another broker loads the partition.

## 326: How does the KIP-848 protocol assign partitions?

Each group has a **target assignment** computed by the broker's assignor (`uniform` or `range`). Each member sends heartbeats containing its subscription and current state. The coordinator then reconciles each member step by step:

1. If a member owns partitions that are not in its target, it is asked to revoke them.
2. When the member confirms in its next heartbeat, those partitions become free.
3. Free partitions are given to their new target owners.

Each member moves at its own pace, there is no group-wide synchronization barrier, and members that are not affected by a change keep working undisturbed. The group's **epoch** increases on every change so stale requests are rejected.

## 327: How does the consumer's fetch path work?

The consumer sends fetch requests to the leaders of its partitions (one request per broker covering many partitions). It does this in the background, ahead of time, so that the next `poll()` can usually return data straight from an internal buffer. With the new consumer threading model (used by the KIP-848 consumer), networking runs on a background thread and `poll()` mostly takes data from in-memory queues.

Settings like `fetch.min.bytes`, `fetch.max.bytes`, `max.partition.fetch.bytes` and `max.poll.records` control how much is fetched and handed to the app.

## 328: What are incremental fetch sessions?

Followers and consumers often fetch the same large set of partitions over and over. With fetch sessions (KIP-227), the broker remembers the partition list and per-partition state between requests. A client then only sends partitions that changed, and the broker only returns partitions with new data. This cuts request size and CPU for clusters with many partitions.

The broker limits the number of cached sessions with `max.incremental.fetch.session.cache.slots`.

## 329: How does the log cleaner work?

The log cleaner is a pool of background threads (`log.cleaner.threads`) that compacts topics with `cleanup.policy=compact`:

1. It picks the partition with the highest **dirty ratio** (uncompacted bytes / total bytes) above `min.cleanable.dirty.ratio`.
2. It scans the dirty section and builds an in-memory map of key -> latest offset (limited by `log.cleaner.dedupe.buffer.size`).
3. It copies segments, keeping only records whose offset matches the latest one for their key, into new segment files.
4. It swaps the new segments in.

Tombstones are removed in a later pass, after `delete.retention.ms`. The active segment and data newer than `min.compaction.lag.ms` are never touched.

## 330: Why might compaction not run, or run slowly?

- The data is all in the active segment (segments are too big or `segment.ms` too long).
- The dirty ratio stays below `min.cleanable.dirty.ratio`.
- `min.compaction.lag.ms` keeps recent data out.
- The cleaner thread died due to an error (check `log-cleaner.log` and the `time-since-last-run-ms` metric); in older versions one bad record could stop it.
- An open or hanging transaction blocks cleaning past the LSO.
- Not enough cleaner threads or dedupe buffer for the volume.

Symptoms are disk usage growing on compacted topics and slow state restores for Kafka Streams.

## 331: How does tiered storage work internally?

- When a segment is closed (rolled), the leader copies it, with its indexes and producer snapshot, to remote storage through the `RemoteStorageManager` plugin.
- Metadata about remote segments is stored through the `RemoteLogMetadataManager`, by default in an internal topic `__remote_log_metadata`.
- Local segments are deleted after `local.retention.ms` / `local.retention.bytes`, once they are safely uploaded.
- When a consumer fetches an offset that is only in remote storage, the broker reads it from the remote store (with caching of indexes) and serves it.
- Remote data is deleted when total retention (`retention.ms` / `retention.bytes`) is exceeded.

Only the leader uploads; followers only need to replicate the local part. A new follower can start from the last tiered offset instead of copying everything (Kafka 4.3 added a setting for this).

## 332: What are the trade-offs of tiered storage?

Pros:

- Much cheaper long retention.
- Smaller local disks; adding or replacing brokers moves far less data.
- Cold reads hit object storage instead of local disks, so they do not compete with hot traffic for disk I/O.

Cons:

- Reads of old data have higher latency.
- Not supported for compacted topics.
- Extra moving parts: a plugin, object storage costs and request costs.
- Once enabled on a topic, turning it off has limitations; check the docs for your version before experimenting on important topics.

## 333: How do share groups track the state of records?

For each partition, the share group keeps a window of in-flight records between the **share-partition start offset (SPSO)** and **end offset (SPEO)**. Each record in the window has a state:

- **Available:** can be delivered.
- **Acquired:** delivered to a consumer and locked for the lock duration.
- **Acknowledged:** done.
- **Archived:** rejected or delivery limit reached.

The delivery count is tracked per record. When records at the start of the window are all acknowledged or archived, the start offset moves forward. This state is stored durably by share coordinators in the `__share_group_state` topic. The size of the window is limited, which caps how far ahead consumers can get from the oldest unfinished record.

## 334: How do share groups handle ordering?

They do not guarantee it. Records from one partition can be handed to different consumers at the same time, and a released record is redelivered later, after newer ones were already processed. If you need ordering for some key, use a consumer group, or make the processing order-independent (for example with version numbers and "last write wins" logic).

## 335: How do you size a Kafka cluster?

Start from requirements and work out each resource:

- **Disk:** `ingest rate x retention x replication factor`, plus 30-40% headroom. Example: 50 MB/s x 3 days x 3 = about 39 TB, so about 55 TB with headroom.
- **Network in:** ingest x RF (producers plus replication). **Network out:** ingest x (number of consumer groups + RF - 1).
- **Memory:** heap of 4-8 GB plus enough page cache to hold the "hot" data that consumers read (a few minutes to an hour of ingest).
- **CPU:** mostly compression, TLS and request handling.
- **Partitions:** keep per-broker counts within what your version handles well.

Then divide by what one broker can do (measured, not guessed), add headroom for losing a broker, and use at least 3 brokers.

## 336: How many partitions can a Kafka cluster handle?

With KRaft, clusters can handle far more partitions than with ZooKeeper; hundreds of thousands to over a million partitions per cluster are possible. Per broker, a few thousand partition replicas is common and fine; going much higher needs testing. The practical limits come from open file handles, memory for indexes, replication threads, leader election time and controller load, so measure with your hardware and version.

## 337: What are the costs of having too many partitions?

- More open files and memory-mapped index files per broker.
- More replication work and more fetch requests.
- Longer failover: more leaders to move when a broker fails.
- Smaller batches on the producer (records spread over more partitions), so lower compression and throughput, and more producer memory.
- More consumer group overhead and slower rebalances.
- More metadata to handle for controllers and clients.

Choose partitions from real throughput needs, not "more is better".

## 338: How do you deal with a hot partition?

A hot partition gets far more traffic than others, usually because of a skewed key (one huge customer) or a bad key choice. Options:

- **Better key:** use a more fine-grained key if per-key order allows it.
- **Key salting:** add a suffix (`customer-42#0` to `#7`) to spread a big key across several partitions, and merge results downstream. You lose strict order for that key.
- **Separate topic** for the very large tenants.
- **Custom partitioner** that sends known hot keys to dedicated partitions.
- **Scale the consumer side** for that partition with per-key parallel processing.

## 339: How do you tune a broker for throughput?

- Match `num.network.threads` and `num.io.threads` to CPU cores and disks, watching the idle percentage metrics.
- Use multiple disks in `log.dirs`.
- Raise `num.replica.fetchers` if followers fall behind.
- Raise `socket.send.buffer.bytes` / `socket.receive.buffer.bytes` (or set `-1` for OS defaults) for high-latency links.
- Leave compression to producers and set topics to `compression.type=producer` to avoid recompression.
- Do not force flushes (`log.flush.interval.messages` / `.ms`); rely on replication.
- Give the OS plenty of RAM for page cache.

## 340: What do num.network.threads and num.io.threads do?

- `num.network.threads` (default 3): threads per listener that read requests from and write responses to sockets. If `NetworkProcessorAvgIdlePercent` is low (below about 30%), add more.
- `num.io.threads` (default 8): threads that actually process requests, including disk I/O. If `RequestHandlerAvgIdlePercent` is low, add more; a common starting point is about the number of disks times a small factor, or the number of cores.

Both can be changed dynamically with `kafka-configs.sh --entity-type brokers`.

## 341: How do you tune the JVM for Kafka?

- Keep the heap modest, often 4-8 GB (`-Xms` = `-Xmx`). The rest of the memory goes to page cache.
- Use G1 (the default in the start scripts), with settings like `-XX:MaxGCPauseMillis=20` and `-XX:InitiatingHeapOccupancyPercent=35`.
- Use a recent JDK (17 or 21 are common); newer versions bring GC improvements. ZGC can help with very low pause requirements.
- Monitor GC pause times; long pauses cause ISR shrinks and session timeouts.

Set them through `KAFKA_HEAP_OPTS` and `KAFKA_JVM_PERFORMANCE_OPTS`.

## 342: What OS and filesystem tuning helps Kafka?

- Use XFS or ext4. Mount with `noatime`.
- Raise the open file limit (`nofile` to 100000 or more) and `vm.max_map_count` for many partitions.
- Set `vm.swappiness=1` so the OS does not swap the JVM.
- Tune dirty page settings (`vm.dirty_background_ratio`, `vm.dirty_ratio`) so writes are flushed smoothly.
- Make sure network buffers are big enough for high bandwidth.
- Avoid putting Kafka data on the same disk as the OS or application logs.

## 343: Should you use RAID or JBOD for Kafka?

- **JBOD** (each disk as its own `log.dirs` entry): cheaper and uses all capacity. Kafka's replication already protects data. A failed disk only takes its partitions offline on that broker (KRaft supports JBOD since 3.7). Downside: data may be uneven across disks.
- **RAID 10:** survives disk failures without involving Kafka, balances I/O, but halves usable capacity and rebuilds can be slow.
- **RAID 5/6:** usually avoided due to write performance and rebuild cost.

In the cloud, network volumes (EBS and similar) are already redundant, so plain volumes are common.

## 344: What storage choices make sense for Kafka?

- **Local NVMe SSDs:** best latency and throughput; data is lost if the instance is replaced, so rely on replication.
- **Network block storage (EBS, Persistent Disk):** survives instance replacement, easier operations, but has throughput limits per volume and costs extra for high IOPS.
- **HDDs:** fine for sequential writes, but consumers reading old data cause seeks; often fine with tiered storage taking cold reads.

Kafka mainly needs sequential throughput, not random IOPS. Tiered storage lets you keep local disks small and fast.

## 345: How do you tune replication between brokers?

- `num.replica.fetchers`: more fetcher threads per source broker help followers keep up on busy brokers.
- `replica.fetch.max.bytes` and `replica.fetch.response.max.bytes`: bigger fetches for catching up.
- `replica.lag.time.max.ms`: how long a follower can lag before being dropped from the ISR. Too low causes ISR flapping, too high slows `acks=all` when a follower is stuck.
- `replica.socket.receive.buffer.bytes` for cross-zone links.

Watch `UnderReplicatedPartitions`, `IsrShrinksPerSec` and replica lag metrics.

## 346: How do you limit the impact of partition reassignment?

Reassignment copies a lot of data, which can saturate network and disks. Use replication throttles:

```bash
bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 \
  --reassignment-json-file plan.json --execute --throttle 30000000
```

This sets `leader.replication.throttled.rate` and `follower.replication.throttled.rate` on the brokers involved and marks the moving replicas as throttled. Also move a few partitions at a time, prefer quiet hours, and run `--verify` at the end so the throttle is removed. Tools like Cruise Control do this automatically.

## 347: How do you benchmark Kafka?

Use the built-in tools against a test cluster with production-like settings:

```bash
bin/kafka-producer-perf-test.sh --topic perf --num-records 10000000 \
  --record-size 1000 --throughput -1 \
  --producer-props bootstrap.servers=localhost:9092 acks=all linger.ms=10 compression.type=lz4

bin/kafka-consumer-perf-test.sh --bootstrap-server localhost:9092 \
  --topic perf --messages 10000000
```

Test with realistic record sizes, key distribution, replication factor, TLS and number of partitions. Also test with a broker down and while a consumer reads old data, because that is when things break. OpenMessaging Benchmark is a more complete option.

## 348: How do you reduce end-to-end latency?

End-to-end latency = producer batching + network + broker append + replication (for `acks=all`) + consumer fetch wait + processing.

- Producer: low `linger.ms`, avoid huge batches.
- Broker: healthy request handler idle %, fast disks, no overloaded followers, short GC pauses.
- Replication: keep replicas close (same region), enough fetcher threads.
- Consumer: low `fetch.max.wait.ms` and `fetch.min.bytes=1`, fast processing, no long `poll()` gaps.
- Avoid `read_committed` with long transactions.

Measure each stage (producer request latency, broker `TotalTimeMs`, consumer lag in time) to see where the time goes.

## 349: How do you find the cause of high produce latency?

Look at the broker's produce request metrics broken into phases:

- **RequestQueueTimeMs** high: I/O threads are busy; add threads or find what is overloading them.
- **LocalTimeMs** high: slow disk writes, check disk I/O and page cache pressure.
- **RemoteTimeMs** high: waiting for followers (`acks=all`); check follower health, network and `num.replica.fetchers`.
- **ResponseQueueTimeMs / ResponseSendTimeMs** high: network threads or network bandwidth.
- **ThrottleTimeMs**: client is over its quota.

On the producer side, compare `record-queue-time-avg` (time waiting in the buffer) with `request-latency-avg`.

## 350: What does RequestHandlerAvgIdlePercent tell you?

It shows the average fraction of time the I/O request handler threads are idle. 1.0 means completely idle. Below about 0.3 (30%), the broker is struggling to keep up and request queue times will grow. Causes include too few `num.io.threads`, slow disks, too many small requests (bad batching), many consumer groups fetching, or heavy compaction and recompression.

## 351: How do you troubleshoot under-replicated partitions?

1. Check if they are all on **one broker**: that broker is down, slow or overloaded. Look at its disk, CPU, GC and network.
2. Check if they are **spread everywhere**: likely cluster-wide load, a network problem, or too few replica fetchers.
3. Check if they belong to **one topic**: maybe a traffic spike or huge messages on that topic.
4. Look at broker logs for ISR shrink messages and fetcher errors.
5. Check if a reassignment is running with too low a throttle.

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

The goal is to find whether the problem is the leader (cannot serve fetches) or the follower (cannot keep up).

## 352: What can cause data loss in Kafka?

- Producer with `acks=0` or `acks=1` and a leader crash before replication.
- `min.insync.replicas=1` with RF 3: an acknowledged write may live on one broker only.
- Unclean leader election turned on.
- Replication factor 1.
- Producer errors that the app ignores (no callback check) or records still in the buffer when the app exits without `close()`.
- Retention or compaction deleting data before slow consumers read it.
- Offsets committed before processing (at-most-once).
- Consumer group offsets expiring and `auto.offset.reset=latest` skipping data.
- All replicas in one zone or rack that fails together, combined with data still only in page cache.

## 353: What can cause duplicates in Kafka?

- Producer retries without idempotence.
- The application re-sending after a restart or a timeout it treated as failure.
- Consumer crashing after processing but before committing.
- Rebalances, where a partition moves before the old owner commits.
- `max.poll.interval.ms` exceeded, causing the same records to be handed to another consumer.
- Offset resets or replays.
- MirrorMaker or failover between clusters.

Most of these are normal behavior under at-least-once, so the fix is idempotent processing.

## 354: How do you get exactly-once results when writing to an external system?

Kafka transactions do not include your database, so you need one of these:

- **Store offsets with the data:** in the same database transaction, write the result and the consumed offset. On startup, read the offset from the database and `seek()` to it. Do not rely on Kafka's committed offsets.
- **Idempotent writes:** use a unique event ID and upserts, so repeated processing has no extra effect.
- **Transactional outbox / inbox tables** for flows that span services.

Sink connectors often support one of these modes (for example upsert mode in JDBC sinks).

## 355: How do you design a Kafka setup across several data centers?

Main options:

- **Separate clusters per region plus replication** (MirrorMaker 2 or a vendor tool): each region is independent and fast; replication is async, so a region failure can lose the last seconds of data.
- **Stretched cluster** across 3 nearby zones or data centers: synchronous replication, no data loss on site failure, but needs low latency between sites (a few ms).
- **Aggregation pattern:** local clusters in each region forward to a central cluster for analytics.

You need to decide on RPO (how much data you can lose), RTO (how fast you must recover), whether clients can fail over, and how to deal with offsets and duplicates after failover.

## 356: What is the difference between active-passive and active-active replication?

- **Active-passive:** producers write to the primary cluster; data is replicated to a standby. On disaster, you switch clients to the standby. Simple, but the standby is idle and failback needs care.
- **Active-active:** both clusters take writes and replicate to each other (with MM2 naming topics like `east.orders` and `west.orders` to avoid loops). Consumers read both the local and the remote topic. Better use of resources and local writes, but you have to deal with conflicts and ordering across regions.

## 357: How do you fail consumers over to another cluster?

1. Replicate topics and offsets with MM2 (`sync.group.offsets.enabled=true` or checkpoints).
2. On failover, stop consumers on the primary (if it is still reachable).
3. Point consumers to the backup cluster. With synced offsets they start from the translated positions; otherwise translate them with `RemoteClusterUtils` or reset by timestamp.
4. Expect some duplicates because offset sync lags behind data replication.
5. Remember topic names may differ (`primary.orders`) unless you use `IdentityReplicationPolicy`.

Practice failover regularly; a plan that has never been tested usually fails.

## 358: What is a stretched cluster?

A single Kafka cluster whose brokers and controllers are spread across several data centers or zones. With `broker.rack` set per site, RF 3 and `min.insync.replicas=2`, every acknowledged write is in at least two sites, so a site can fail with no data loss and no client failover.

Requirements: low and stable latency between sites (because `acks=all` waits for remote replicas), at least three sites for the controller quorum to keep a majority, and enough bandwidth for replication.

## 359: How do you plan disaster recovery for Kafka?

- Decide RPO and RTO per data type; not every topic needs the same protection.
- Replicate important topics to another cluster or region (MM2), or use a stretched cluster.
- Keep topic configs, ACLs and schemas as code, so they can be recreated.
- Replicate schema registry data too.
- Plan how producers and consumers switch (DNS, config, service discovery).
- Handle offsets: translation or timestamp-based resets.
- Test failover and failback in drills.

## 360: How do you back up Kafka?

Kafka has no built-in snapshot backup. Common approaches:

- Replicate to another cluster with MirrorMaker 2.
- Use tiered storage, which keeps older segments in object storage (but it is not a separate backup of recent data and it is managed by the same cluster).
- Sink important topics to object storage with an S3 sink connector, in a format that can be replayed.
- Back up metadata as code (topics, configs, ACLs) and schemas.

Disk snapshots of brokers are rarely useful because they are not consistent across brokers.

## 361: How do you secure Kafka end to end?

- **Encryption in transit:** TLS on all listeners, including between brokers and to controllers.
- **Authentication:** mTLS, SASL/SCRAM or OAUTHBEARER for every client; no PLAINTEXT listener exposed.
- **Authorization:** `StandardAuthorizer` with least-privilege ACLs, prefixed ACLs per team, `allow.everyone.if.no.acl.found=false`.
- **Network:** private networks, firewalls, no public broker IPs if possible.
- **Quotas** to stop one client from taking down others.
- **Secrets:** use config providers instead of plain passwords in files.
- **Encryption at rest** at the disk level, or in the application for sensitive fields.
- **Audit:** log authorization decisions, keep configs in version control.

## 362: How does OAUTHBEARER authentication work?

The client gets an access token (usually a JWT) from an OAuth/OIDC provider, typically using the client credentials flow, and sends it to the broker over SASL. The broker validates the token's signature against the provider's public keys (JWKS), checks expiry, audience and issuer, and uses a claim (like `sub`) as the principal for ACLs. Clients refresh tokens before they expire.

```properties
# client
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.oauthbearer.token.endpoint.url=https://idp.example.com/oauth2/token
sasl.login.callback.handler.class=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required \
  clientId="billing" clientSecret="${env:CLIENT_SECRET}";
```

The broker side uses `sasl.oauthbearer.jwks.endpoint.url` and the validator callback handler. Newer Kafka versions also support other grant types such as JWT bearer assertions.

## 363: How do you rotate certificates and credentials without downtime?

- **TLS certificates:** add the new CA to truststores first, then replace keystores. Brokers can reload keystores dynamically by updating the listener's SSL config with `kafka-configs.sh --entity-type brokers`, without a restart.
- **SCRAM:** create a new password or user, update clients, then remove the old one. A user can have both SCRAM-SHA-256 and SHA-512 credentials during a switch.
- **OAuth:** rotate signing keys at the provider; brokers refresh the JWKS automatically.

Automate expiry monitoring; expired broker certificates are a common cause of full outages.

## 364: How do you run Kafka for several teams or tenants?

- Topic name prefixes per team and **prefixed ACLs** so each team only sees its own topics.
- Separate principals (service accounts) per application.
- **Quotas** per user or client to prevent noisy neighbors.
- Limits on partitions per team and on topic creation (through a self-service tool instead of giving `Create` rights).
- Consumer group name prefixes protected by ACLs.
- Chargeback based on bytes in/out and storage per prefix.

For strong isolation (compliance, very different load), use separate clusters.

## 365: How do you encrypt data at rest in Kafka?

Kafka does not encrypt its log files by itself. Options:

- **Disk or volume encryption** (LUKS, cloud encrypted volumes): protects against stolen disks, transparent to Kafka.
- **Application-level encryption:** producers encrypt values (or sensitive fields) before sending, consumers decrypt. Protects against anyone with broker access, but makes stream processing and compaction by value harder. Keys go in a KMS.
- **Tiered storage:** enable encryption in the object store.

Some vendors offer client-side field encryption as part of their serializers.

## 366: How do you handle GDPR deletion requests with Kafka?

Kafka logs are immutable, so deleting one person's data is hard. Options:

- **Compacted topics keyed by user ID:** send a tombstone; the data is removed after compaction (use `max.compaction.lag.ms` to bound the time).
- **Short retention** for topics with personal data, so it ages out within the allowed time.
- **Crypto shredding:** encrypt each user's personal data with a per-user key stored outside Kafka. To "delete", destroy the key; the data in Kafka becomes unreadable.
- **Keep personal data out of events:** send IDs, and store the personal data in a database where it can be deleted.

Remember copies in other clusters, tiered storage, sinks and backups.

## 367: How do you handle large payloads with the claim check pattern?

Instead of sending a 50 MB file through Kafka:

1. The producer uploads the payload to object storage (for example `s3://bucket/orders/123.json`).
2. It sends a small Kafka record with the reference, size, checksum and content type.
3. The consumer reads the record, downloads the payload, and processes it.

This keeps brokers and clients fast. You need a cleanup policy for the stored objects (for example a lifecycle rule longer than the topic's retention), and access control for the bucket.

## 368: How do you design good event schemas?

- Use explicit names in past tense (`OrderPlaced`) for events.
- Include an event ID, event type, event time, source, and a schema version or rely on the registry ID.
- Decide whether events carry full state ("fat" events) or just what changed and an ID ("thin" events).
- Use the entity ID as the record key.
- Make fields optional with defaults where possible, to allow evolution.
- Avoid generic `Map<String,String>` payloads; they remove the value of schemas.
- Consider a standard envelope like CloudEvents.

## 369: What is the difference between event notification and event-carried state transfer?

- **Event notification:** the event just says something happened, with an ID (`OrderPlaced {orderId: 7}`). Consumers call back to the source service for details. Small events, but adds coupling and load on the source.
- **Event-carried state transfer:** the event contains the data consumers need (`OrderPlaced {orderId, items, total, customer}`). Consumers can keep their own copy and work even if the source is down. Bigger events and more care with schema changes and sensitive data.

Many systems use the second for core domain events.

## 370: How do you implement event sourcing with Kafka?

In event sourcing, the state of an entity is the result of replaying its events. With Kafka:

- Store events in a topic keyed by entity ID, with long or infinite retention.
- Build current state by consuming the events into a store (a Kafka Streams `KTable`, or a database).
- Use the entity ID as the key so all events of one entity are ordered.

The hard part is writing: to check business rules ("is the balance enough?") you need the current state and protection against two writers at the same time. Kafka has no "append only if the last offset is X" operation, so teams usually use a single writer per key (for example a Streams app that owns the partition) or an event store database for writes, and Kafka for distribution.

## 371: How does CQRS fit with Kafka?

CQRS separates the write model (commands) from read models (queries). Kafka sits in between:

1. The write side saves changes and publishes events (often via the outbox pattern).
2. Each read model consumes the events and builds a view optimized for its queries: a search index, a cache, a reporting table, a Kafka Streams state store.

Read models are eventually consistent. If one is lost or its schema changes, you rebuild it by replaying the topic from the beginning, which is why retention matters.

## 372: How do you implement a saga with Kafka?

A saga is a sequence of local transactions across services, with compensating actions if a step fails.

- **Choreography:** each service listens to events and emits its own. `OrderPlaced` -> payment service charges -> `PaymentCompleted` -> inventory reserves -> `StockReserved`. If `StockFailed`, payment listens and refunds.
- **Orchestration:** one orchestrator service sends commands (`ChargePayment`) to command topics and waits for reply events, tracking saga state.

Each step must be idempotent, use the saga or order ID as the key, and use the outbox pattern to publish reliably. Orchestration is easier to follow for long flows.

## 373: How do you keep per-entity ordering safe across failures and scaling?

- Use the entity ID as the key so it stays in one partition.
- Producer: idempotence on (default) so retries do not reorder.
- Do not add partitions to the topic without a migration plan.
- Consumer: process each partition in order; if you parallelize, do it per key, not per record.
- Commit only after processing, and make processing idempotent so reprocessing after a rebalance does not create wrong state.
- Use version numbers or event sequence numbers in the data so consumers can detect old or out-of-order updates and ignore them.

## 374: How do you handle out-of-order events?

Events can come out of order across partitions, from different producers, or from late devices. Options:

- **Event time and versions:** store the last applied version or timestamp per entity and ignore older updates.
- **Buffer and reorder:** hold events for a short window and sort them (as Kafka Streams grace periods do for windows).
- **Commutative updates:** design operations so order does not matter (set-based, max, sums).
- **Single partition per entity:** prevents most reordering at the source.

## 375: How do you implement delayed or scheduled processing with Kafka?

Kafka has no built-in delayed delivery. Common patterns:

- **Delay topics:** write to `orders.delay-5m`; a consumer reads it, checks the record's timestamp, and if it is too early, pauses that partition and resumes later. Since records in the topic are in time order, it only has to wait for the head.
- **Kafka Streams punctuators** with a state store of scheduled items, checked on a timer.
- **External scheduler** (a database table with a due time, or a job scheduler) that produces to Kafka when due.

## 376: How do you build retry topics with backoff?

Use several topics with increasing delays:

```text
orders -> orders.retry-1m -> orders.retry-10m -> orders.retry-1h -> orders.dlq
```

1. The main consumer fails on a record and sends it to `orders.retry-1m` with a header counting attempts.
2. A retry consumer reads that topic, waits until the record is old enough (pause/resume on the partition, not sleep), and processes it again.
3. On failure it moves to the next retry topic, and finally the DLQ.

This keeps the main topic flowing. The downside is that ordering per key is lost for retried records. Spring Kafka's `@RetryableTopic` implements this pattern.

## 377: How do you replay events?

- **Same consumer group:** stop it, reset offsets to a time or offset, start again.
- **New consumer group:** start a new group from the earliest offset or a timestamp. The old group keeps running untouched. Good for building a new read model.
- **Replay into another topic:** a small job copies a range of records to a "replay" topic, so only specific consumers see them.

Make sure side effects (emails, payments) are not triggered again during a replay, for example with a "replay" header that consumers check, or idempotency keys.

## 378: How do you reprocess data after a bug was found?

1. Fix and deploy the consumer.
2. Find the time range or offsets affected.
3. Reset the group to the start of that range (`--to-datetime`) or run a separate group over just that range.
4. Make sure the consumer can overwrite wrong results (idempotent upserts by event ID) instead of adding on top.
5. For Kafka Streams with state, use the application reset tool and rebuild the state, or deploy with a new `application.id`.

This only works if retention still covers the range, which is a good reason to keep important topics longer.

## 379: How do you move to more partitions without breaking key ordering?

1. Create a new topic with the target partition count.
2. Run a copy job (or MirrorMaker, or a Streams app) that reads the old topic and writes to the new one with the same keys; records for a key keep their relative order.
3. Switch consumers to the new topic once it has caught up, starting at the equivalent position (by timestamp or a marker).
4. Switch producers to the new topic, and let the copy job drain the old one.

Alternatively, briefly stop producers, wait for consumers to drain the old partitions, add partitions, then restart. That is simpler but needs downtime for producers.

## 380: How do you rename a topic?

Kafka cannot rename topics. You create a new topic with the new name and same configs, copy data if needed (a mirror or a small copy job), move consumers then producers over, and delete the old topic when nobody uses it. Offsets do not carry over, so consumers start by timestamp or from the beginning. This is a good reason to agree on naming early.

## 381: How do you roll out a breaking schema change without downtime?

1. Create a new version of the event (a new topic like `orders.v2`, or a new event type).
2. Have producers write both the old and the new format during a transition (or run a converter that reads v1 and writes v2).
3. Move consumers to v2 one by one.
4. When no one reads v1, stop producing it and delete the topic after retention.

Within one topic, stick to compatible changes checked by the schema registry.

## 382: How does Kafka Streams assign tasks to instances?

In the classic setup, Kafka Streams uses its own assignor (`StreamsPartitionAssignor`) inside the consumer group protocol. It assigns tasks, not just partitions, and tries to:

- balance tasks across instances and threads,
- keep stateful tasks on instances that already have their state locally (stickiness),
- place standby replicas on different instances (and different racks if configured),
- warm up state on new instances before moving tasks to them (`max.warmup.replicas`, `acceptable.recovery.lag`, `probing.rebalance.interval.ms`).

With the new Streams rebalance protocol (KIP-1071) this assignment moves to the broker.

## 383: What are standby replicas in Kafka Streams?

Standby replicas are copies of a task's state store kept up to date on other instances by reading the changelog topic. If the active instance fails, the task moves to an instance with a standby, which can start almost right away instead of replaying the whole changelog.

```properties
num.standby.replicas=1
```

They cost extra disk, memory and changelog reads. Use them for apps with large state where long restores would be a problem.

## 384: How does RocksDB work in Kafka Streams and how do you tune it?

Each persistent state store (and each store segment for windowed stores) is a RocksDB instance on local disk. RocksDB uses memory for write buffers (memtables), block cache and index/filter blocks, which is **off-heap** and not limited by `-Xmx`.

To tune or limit it, implement `RocksDBConfigSetter`:

```java
public class BoundedMemoryRocksDBConfig implements RocksDBConfigSetter {
    private static final Cache CACHE = new LRUCache(256 * 1024 * 1024L);
    private static final WriteBufferManager WBM =
        new WriteBufferManager(64 * 1024 * 1024L, CACHE);

    @Override
    public void setConfig(String storeName, Options options, Map<String, Object> configs) {
        BlockBasedTableConfig table = (BlockBasedTableConfig) options.tableFormatConfig();
        table.setBlockCache(CACHE);
        table.setCacheIndexAndFilterBlocks(true);
        options.setWriteBufferManager(WBM);
        options.setTableFormatConfig(table);
    }

    @Override
    public void close(String storeName, Options options) {}
}
```

```properties
rocksdb.config.setter=com.example.BoundedMemoryRocksDBConfig
```

Sharing one cache across all stores bounds total memory, which matters in containers with memory limits.

## 385: How does Kafka Streams restore state and how can you make it faster?

When a stateful task starts on an instance without up-to-date local state, it reads the changelog topic from its last checkpoint (or the beginning) and writes every record into the local store before processing can start. For big stores this can take a long time.

Ways to speed it up:

- Use persistent volumes so local state survives restarts (only the tail is replayed).
- Standby replicas and warmup replicas.
- Keep changelog topics well compacted.
- Static membership and cooperative rebalancing to avoid moving tasks needlessly.
- Tune restore consumer settings (`restore.consumer.max.poll.records`) and RocksDB bulk loading.
- Split big stores across more partitions.

## 386: What is the new Kafka Streams rebalance protocol?

KIP-1071 brings a KIP-848 style protocol to Kafka Streams: the broker runs a "streams group" and computes task assignments, instead of a Streams instance doing it inside the consumer protocol. Rebalances are incremental and driven by heartbeats, and the broker becomes aware of Streams topology concepts like tasks and internal topics.

It became generally available in Kafka 4.2 with a limited feature set. You turn it on with `group.protocol=streams` in the Streams config; check the docs for which features (such as some standby and warmup behaviors) are not supported yet in your version.

## 387: How does Kafka Streams handle time?

- **Event time:** from the record's timestamp (producer or broker set). Used by default for windows and joins.
- **Stream time:** the highest event timestamp seen so far by a task. Windows close based on stream time, not the wall clock. If no new records arrive, stream time does not move, and windows do not close.
- **Wall-clock time:** system time, used for punctuations of type `WALL_CLOCK_TIME` and some timeouts.

Output records usually inherit the input timestamp; aggregations use the max timestamp of their inputs. Because stream time is per task, a partition with no traffic can delay results, which surprises people in tests.

## 388: What is a TimestampExtractor?

A `TimestampExtractor` tells Kafka Streams which time to use for a record. The default uses the record's own timestamp. If the real event time is inside the payload, write your own:

```java
public class OrderTimeExtractor implements TimestampExtractor {
    @Override
    public long extract(ConsumerRecord<Object, Object> record, long partitionTime) {
        if (record.value() instanceof Order order && order.createdAt() != null) {
            return order.createdAt().toEpochMilli();
        }
        return partitionTime; // fall back to the latest known time
    }
}
```

Set it globally with `default.timestamp.extractor` or per source with `Consumed.with(...).withTimestampExtractor(...)`.

## 389: How do foreign-key joins work in Kafka Streams?

A foreign-key join joins a `KTable` to another `KTable` using a field in the left value, not its key, for example orders (keyed by orderId) to customers (keyed by customerId):

```java
KTable<String, EnrichedOrder> enriched = orders.join(
    customers,
    order -> order.customerId(),               // foreign key extractor
    (order, customer) -> new EnrichedOrder(order, customer));
```

Internally Kafka Streams sends "subscription" records to the right table's partitions (keyed by the foreign key), joins there, and sends "response" records back to the left side via internal topics. It handles updates on both sides and removes outdated results when an order's foreign key changes. It needs no co-partitioning but creates several internal topics.

## 390: What does topology optimization do in Kafka Streams?

With `topology.optimization=all`, Kafka Streams rewrites the topology when you call `builder.build(props)`, for example:

- reusing the source topic as the changelog for a source `KTable` instead of creating a new changelog,
- merging several repartition topics into one when the same re-keyed stream is used in several places.

It saves topics and network traffic. Turning it on for an existing app can change internal topic names, so treat it like a topology change that may need a reset or migration.

```java
Properties props = new Properties();
props.put(StreamsConfig.TOPOLOGY_OPTIMIZATION_CONFIG, StreamsConfig.OPTIMIZE);
Topology topology = builder.build(props);
```

## 391: How do you scale a Kafka Streams application?

- Run more instances with the same `application.id`; tasks spread across them.
- Raise `num.stream.threads`, or add threads at runtime with `streams.addStreamThread()`.
- The max parallelism is the partition count of the input (and repartition) topics; to go further you need more partitions, which for stateful apps means a migration.
- For stateful apps, plan for state restoration when tasks move: standbys, persistent volumes and warmup settings.

## 392: How do you change a stateful Kafka Streams topology safely?

Internal topic and store names are generated from the order of operations unless you name them. Adding an operation in the middle can rename stores and repartition topics, which loses state.

- Always name stateful operators and stores (`Materialized.as("...")`, `Grouped.as("...")`, `Named.as("...")`).
- Compatible changes (stateless steps that do not shift names) can be rolled out normally.
- For incompatible changes, either run the new version with a new `application.id` from the beginning of the input and switch over, or use the reset tool and rebuild.
- Changing the value format of a state store needs a serde that can read both old and new formats, or a rebuild.

## 393: How do you reset a Kafka Streams application?

```bash
bin/kafka-streams-application-reset.sh --bootstrap-server localhost:9092 \
  --application-id order-enricher --input-topics orders,customers \
  --to-earliest
```

This resets input offsets and deletes internal topics (changelogs and repartition topics). You must also delete local state, either by calling `streams.cleanUp()` before `start()` or by deleting the `state.dir`. All instances must be stopped while you reset.

## 394: When would you use Kafka Streams instead of Apache Flink?

- **Kafka Streams:** a library in your app, no separate cluster, reads and writes Kafka only, great for microservices that do stateful processing on Kafka data. Scaling is done by running more app instances.
- **Flink:** a separate processing cluster, many sources and sinks, very large state, advanced event-time features, SQL, and both batch and streaming. More operational work, but more power for big data pipelines.

Use Kafka Streams when your input and output are Kafka and you want simple deployment. Use Flink for complex pipelines across many systems or very large stateful jobs.

## 395: How do you size Kafka Connect workers and tasks?

- Tasks are the unit of parallelism. Set `tasks.max` based on how much the source or sink can handle in parallel (partitions, tables, API limits).
- Workers host tasks. Run at least 2 or 3 workers for fault tolerance; add more when CPU, memory or network is saturated.
- Heavy converters (Avro, JSON with schemas) and SMTs cost CPU.
- Separate noisy or critical connectors into their own Connect clusters so one bad connector does not affect others.
- Monitor task status, lag of sink consumer groups, and source record rates.

## 396: How does Kafka Connect rebalance work?

Connect workers form a group and use incremental cooperative rebalancing (the default since Kafka 2.3). When a worker joins or leaves, only the affected connectors and tasks move. When a worker leaves, Connect waits up to `scheduled.rebalance.max.delay.ms` (5 minutes by default) for it to come back before giving its tasks to others, which avoids moving tasks around during short restarts.

The trade-off: tasks of a crashed worker are not running for up to that delay. Lower it if you prefer faster failover.

## 397: How do you build a custom connector?

Implement two classes:

- `SourceConnector` / `SinkConnector`: validates config (`config()` returns a `ConfigDef`), and splits work into task configs in `taskConfigs(maxTasks)`.
- `SourceTask` / `SinkTask`: does the work. A source task returns `SourceRecord`s from `poll()` with a source partition and source offset map; a sink task gets records in `put()` and flushes in `preCommit()`/`flush()`.

```java
public class MySinkTask extends SinkTask {
    @Override
    public void put(Collection<SinkRecord> records) {
        for (SinkRecord r : records) {
            client.write(r.key(), r.value());
        }
    }
    // start(), stop(), version() omitted
}
```

Package it as a plugin directory or JAR and put it on `plugin.path`. Check existing connectors first; most systems already have one.

## 398: How do you write a custom single message transform?

Implement `Transformation<R extends ConnectRecord<R>>`:

```java
public class UppercaseTopic<R extends ConnectRecord<R>> implements Transformation<R> {
    @Override
    public R apply(R record) {
        return record.newRecord(record.topic().toUpperCase(), record.kafkaPartition(),
            record.keySchema(), record.key(), record.valueSchema(), record.value(),
            record.timestamp());
    }

    @Override public ConfigDef config() { return new ConfigDef(); }
    @Override public void configure(Map<String, ?> configs) {}
    @Override public void close() {}
}
```

Returning `null` from `apply()` drops the record. Keep SMTs simple and stateless; anything complex belongs in a stream processor.

## 399: What happens when a producer writes to a topic that does not exist?

The producer asks for metadata for the topic. If the broker has `auto.create.topics.enable=true` (the default), the topic is created with the broker defaults (`num.partitions`, `default.replication.factor`). If not, the producer keeps asking until `max.block.ms` and then throws a `TimeoutException` ("Topic not present in metadata"). Consumers subscribing to a missing topic get a warning and wait, depending on `allow.auto.create.topics` on the consumer.

## 400: Why should auto.create.topics.enable be turned off in production?

- A typo in a topic name silently creates a new topic, and data goes there instead of failing.
- Auto-created topics get default partitions and replication, often 1 partition and the wrong retention.
- It makes it hard to know who owns which topic.
- Some tools probe topics and accidentally create them.

Create topics explicitly through code reviewed configs (Terraform, Strimzi, scripts), and set `auto.create.topics.enable=false`.

## 401: How do clients find partition leaders and handle leader changes?

Clients keep a metadata cache that maps each partition to its leader. When a leader moves, the old leader answers requests with `NOT_LEADER_OR_FOLLOWER` (or similar errors), and the client refreshes metadata and retries against the new leader. Newer clients and brokers (KIP-951) also include the new leader's info directly in the error response, so the client can switch without a separate metadata round trip, which shortens the pause during leader changes.

## 402: What happens during a rolling restart of brokers?

For each broker in turn:

1. The broker does a controlled shutdown: it asks the controller to move leadership of its partitions to other in-sync replicas.
2. Clients switch to the new leaders.
3. The broker stops; its partitions are temporarily under-replicated.
4. It starts, catches up from the leaders and rejoins the ISRs.
5. Preferred leader election moves leadership back.

Wait until there are no under-replicated partitions before restarting the next broker, otherwise you may drop below `min.insync.replicas` and block writes.

## 403: What is controlled shutdown?

When a broker is stopped normally (SIGTERM), it first tells the controller it is shutting down. The controller moves leadership of all partitions it leads to other ISR members and removes it from ISRs in a planned way. Only then does the broker stop. This means clients see a quick leader switch instead of waiting for timeouts, and no data is lost.

A `kill -9` or a crash skips this, so the controller only notices after the broker session timeout.

## 404: What does replica.lag.time.max.ms control?

It is the maximum time a follower can go without catching up to the leader's log end before it is removed from the ISR (default 30 seconds). It is a trade-off:

- **Too low:** short hiccups (GC pause, network blip) remove followers from the ISR and cause flapping, plus more under-replicated alerts.
- **Too high:** a stuck follower stays in the ISR, and every `acks=all` write waits for it until the timeout, so produce latency spikes.

## 405: What happens when a broker's disk fills up?

When a log directory cannot be written (out of space or I/O errors), the broker marks it as **offline**. Partitions on it go offline on that broker, and leadership moves to replicas on other brokers. If the broker has only one log directory, it effectively stops serving.

To recover: free up space (lower retention on large topics, delete unneeded topics, or add disk), and restart if needed. Prevent it with disk usage alerts (for example at 70% and 85%), retention by bytes for risky topics, and capacity planning. Never delete segment files by hand while the broker runs.

## 406: What happens if one of several log directories fails?

With JBOD (several `log.dirs`), the broker can keep running when one directory fails. It reports the failed directory to the controller, which marks the replicas on it as offline and elects new leaders elsewhere. The other directories keep working. After replacing the disk, the broker recreates those replicas by copying from leaders. KRaft supports this since Kafka 3.7.

## 407: What are cordoned log directories?

Added in Kafka 4.3 (KIP-1066), cordoning marks a log directory so no **new** partitions are placed on it, while existing ones keep working. It is useful when you plan to remove a disk or a broker: cordon it first, then move partitions off with reassignment, without new topics landing there in the meantime.

## 408: How do you handle one slow partition blocking a consumer?

In a consumer group, each partition is processed in order, so one slow record (or a slow downstream call) holds back everything behind it on that partition.

- Find the cause first: a slow external call, a huge record, a hot key.
- Add timeouts to external calls and send failures to a retry topic instead of blocking.
- Process per key in parallel within the partition (keys are independent) using a parallel consumer approach.
- Use `pause()` on that partition while you retry, so other partitions keep moving.
- If order does not matter, consider a share group.

## 409: How do you avoid rebalance storms in large consumer groups?

A rebalance storm is a chain of rebalances where each one causes timeouts that cause another rebalance.

- Move to the new consumer protocol (`group.protocol=consumer`), which avoids the group-wide barrier.
- With the classic protocol, use `CooperativeStickyAssignor` and static membership.
- Keep processing per poll short (`max.poll.records`), so members do not exceed `max.poll.interval.ms` during rebalances.
- Make `onPartitionsRevoked` fast.
- Stagger deployments and autoscaling steps.
- Split very large groups or very large topic subscriptions.

## 410: What happens to in-flight work during a rebalance?

When a partition is revoked, the consumer should finish or abandon the work for it and commit offsets in `onPartitionsRevoked`. Anything processed but not committed will be processed again by the new owner. If you hand records to worker threads, you need to wait for those workers (or cancel them) before the revoke callback returns, otherwise two consumers may process the same records at the same time.

If partitions are **lost** (the consumer was kicked out, `onPartitionsLost`), you cannot commit anymore, and duplicates are certain.

## 411: How do you commit offsets correctly when processing asynchronously?

When records are processed in parallel, they finish out of order. You must never commit an offset beyond a record that is still in progress.

- Track per partition which offsets are done.
- Commit the highest offset where every record below it is done (the "low watermark" of completed work) plus one.
- Limit the number of in-flight records and `pause()` partitions when the limit is reached.
- On revoke, wait for in-flight records of that partition or accept that they will be redone.

```text
done: 100 101 102 _ 104 105    (103 still running)
safe commit: 103               (next offset to read after 102)
```

## 412: How do you process a partition in parallel while keeping order per key?

Inside one partition, records with different keys are independent. A consumer can route each record to a worker chosen by `hash(key) % workers`, so each key is handled by one worker in order, while different keys run in parallel. Offset commits must follow the rule from question 411. Confluent's open source Parallel Consumer library implements this (key-level ordering, and it even stores incomplete offsets in commit metadata).

## 413: What problems do thousands of consumer groups cause?

- More fetch requests to brokers, and more data sent out (each group reads everything).
- More load on group coordinators and on `__consumer_offsets` (offset commits are writes).
- Cold reads if many groups read old data at different positions, pushing hot data out of page cache.
- Monitoring and lag tracking get heavy.

Fixes: batch offset commits (do not commit after every record), merge similar consumers into one service that fans out internally, use tiered storage for cold reads, and spread group coordinators by keeping `__consumer_offsets` partitions balanced.

## 414: How do you decide between keeping state in Kafka or in a database?

- **Kafka (compacted topics, Streams state stores):** good when state is derived from streams, keyed lookups are enough, and you want everything rebuildable from the log.
- **Database:** needed for ad-hoc queries, secondary indexes, transactions across many keys, and strong consistency for user-facing reads.

A common split: Kafka for events and stream processing, the database for query models built from those events.

## 415: How do clock problems affect Kafka?

Kafka's correctness (ordering, offsets, replication) does not depend on clocks. But timestamps do:

- Producers with wrong clocks write wrong `CreateTime` values, which affects time-based retention (a future timestamp can keep a segment from being deleted), `offsetsForTimes()` lookups, and stream windowing.
- Kafka Streams windows are based on event time, so skewed producers put records in the wrong windows or make them "late".

Use NTP everywhere, consider `LogAppendTime` for topics where producer clocks are not trusted, and set limits on how far off timestamps may be (next question).

## 416: What do log.message.timestamp.before.max.ms and after.max.ms do?

They reject records whose `CreateTime` timestamp is too far from the broker's clock:

- `log.message.timestamp.before.max.ms`: how far in the past a timestamp may be.
- `log.message.timestamp.after.max.ms`: how far in the future it may be.

They replaced the older single `log.message.timestamp.difference.max.ms` setting (KIP-937). Limiting future timestamps protects retention: a record dated years ahead would otherwise keep its segment from ever being deleted. Topic-level versions exist without the `log.` prefix. Be careful setting the "before" limit if you legitimately backfill old events.

## 417: What is the zombie producer problem?

A zombie is an old instance of a producer that is still running when a new instance has taken over its work, for example after a network partition or a long GC pause made it look dead. Both now write the same data, and in transactional pipelines the zombie could commit outputs for input that the new instance also processes, breaking exactly-once.

Kafka solves this with **fencing**: the `transactional.id` plus epoch for producers, and the consumer group generation passed with `sendOffsetsToTransaction()`.

## 418: How does producer fencing work?

Each `transactional.id` has a producer epoch stored by the transaction coordinator. When a new instance calls `initTransactions()`, the epoch is increased. Any request from an instance with an older epoch is rejected with `ProducerFencedException` (or `InvalidProducerEpochException`). The fenced instance must close; it cannot recover.

With `sendOffsetsToTransaction(offsets, consumer.groupMetadata())`, the group generation is also checked, so a consumer that has lost its partitions after a rebalance cannot commit offsets for them inside a transaction.

## 419: How do you design idempotency keys for events?

- Generate the ID when the event is **created** (at the source), not when it is sent, so retries reuse it.
- Make it deterministic for derived events, for example `hash(sourceEventId + stepName)`, so reprocessing produces the same ID.
- Put it in a header or the value, not only in the Kafka key (the key is for partitioning).
- Store processed IDs in the consumer's database with a unique constraint, in the same transaction as the business change.
- Expire old IDs after a window that is longer than any possible replay or retry period.

## 420: How do you handle backpressure in a Kafka-based pipeline?

Kafka itself absorbs bursts: if consumers are slower, lag grows on disk instead of crashing anything. The issues are downstream:

- Consumers should limit in-flight work and `pause()` partitions when downstream systems are slow, instead of buffering in memory.
- Use timeouts and circuit breakers on external calls.
- Size retention so the topic can hold a backlog for as long as an outage might last.
- Producers facing slow brokers block on `buffer.memory`; decide whether to block, drop or spill to disk.
- Autoscale consumers on lag, up to the partition count.

## 421: How would you design a topic for an audit log?

- One topic (or one per domain) with `cleanup.policy=delete` and long retention, or tiered storage for years of data.
- `message.timestamp.type=LogAppendTime` so times come from the broker.
- RF 3, `min.insync.replicas=2`, producers with `acks=all` and idempotence.
- Key by the entity being audited, so its history is ordered.
- Strict ACLs: write only for the audit producers, no delete rights for anyone except admins.
- Sink to immutable object storage (with object lock) for compliance and long-term search.

## 422: How do you test how Kafka behaves under failures?

- Kill brokers (cleanly and with `kill -9`) during load tests and check client errors, latency and data completeness.
- Simulate network partitions and latency with tools like Toxiproxy, `tc netem` or Chaos Mesh.
- Fill a disk on a broker.
- Restart consumers during processing and check for lost or duplicated results.
- Fail a whole zone if you run multi-zone.
- Verify data with end-to-end checks: count and checksum records produced vs consumed.

Do this in staging first, with the same configs as production.

## 423: How do you measure end-to-end latency?

- Put the creation time in the record (or use the record timestamp) and, in the consumer, measure `now - timestamp` per record. Export it as a histogram.
- Run a synthetic "canary" producer that writes a timestamped record to each partition every few seconds and a canary consumer that measures how long it takes to arrive. This catches problems even when real traffic is low.
- Track consumer lag in time, not only in offsets.

Clock sync between hosts matters for these measurements.

## 424: How would you set up alerting for a Kafka cluster?

Page someone for:

- offline partitions > 0,
- under-min-ISR partitions > 0 (writes are failing),
- no active controller, or more than one,
- broker down,
- disk usage above a high threshold,
- consumer lag (in time) growing past the SLA for critical groups.

Warn for:

- under-replicated partitions for more than a few minutes,
- request handler idle below 30%,
- ISR shrink rate spikes,
- rising produce and fetch latency,
- certificate expiry within 30 days,
- DLQ topics receiving records.

## 425: How do you plan storage for retention?

```text
storage per broker = (daily ingest after compression x retention days x replication factor)
                     / number of brokers  x  (1 + headroom)
```

Also account for: uneven partition sizes, compacted topics that hold a fixed amount of data, internal topics, the fact that segments are deleted whole (data lives up to `segment.ms` extra), and the extra space needed during reassignment (the moving partition exists on both brokers for a while). Keep 30-40% free space. Tiered storage changes the formula: local disks only need the local retention part.

## 426: Why are cross-zone costs a concern and how do you reduce them?

In the cloud, traffic between availability zones costs money, and Kafka generates a lot of it: producers sending to leaders in other zones, replication to followers in other zones, and consumers reading from leaders in other zones. For high-volume clusters this can cost more than the servers.

Ways to reduce it:

- Consumers fetch from same-zone followers (`client.rack` + `RackAwareReplicaSelector`).
- Compress well (`zstd`), since you pay for bytes.
- Rack-aware producers or partitioning, where the client library supports it, so producers mostly write to leaders in their own zone.
- Evaluate whether every topic needs RF 3 across zones.

## 427: How do quotas and throttling look from the client side?

The broker does not reject requests that exceed the quota; it computes a delay and returns `throttle_time_ms` in the response, then mutes the channel for that time. Clients also respect it. To the app, this shows up as higher latency and lower throughput, not errors. Producer and consumer metrics like `produce-throttle-time-avg` and `fetch-throttle-time-avg` show it. If an app is "mysteriously slow", check these metrics.

## 428: What are the security risks of a default Kafka setup?

- `PLAINTEXT` listeners: no encryption and no authentication; anyone who can reach the port can read and write everything.
- No authorizer: every client can create, delete and read any topic.
- `auto.create.topics.enable=true`: anyone can create topics.
- `delete.topic.enable=true` with no ACLs: anyone can delete topics.
- Open Connect REST API (port 8083) without auth, which can be used to run connectors with arbitrary configs.
- JMX ports open to the network.

Never expose a default Kafka setup outside a trusted network.

## 429: How do you audit who did what on a Kafka cluster?

- Enable authorizer logging: the `kafka.authorizer.logger` logger records allowed and denied operations (at `INFO` for denials, `DEBUG` for allowed ones, which is very verbose).
- Request logs (`kafka.request.logger`) for detailed request info, usually only temporarily.
- Keep topic, ACL and quota changes in version control and apply them through CI, so the history is in git.
- Ship logs to a central system and alert on denied operations and admin actions like topic deletion.

## 430: What are the pitfalls of using a compacted topic as a key-value store?

- Reads are not by key: you have to consume the whole topic into memory or a local store to look up values.
- Compaction is not immediate; consumers see old values and duplicates for a while.
- Deletes need tombstones, and slow readers can miss them after `delete.retention.ms`.
- Partitions grow with the number of keys; very many keys means long load times.
- No transactions across keys and no secondary indexes.
- Keys must be serialized the same way every time; different serializations create different keys.

It works well for configs, reference data and state backups, but it is not a replacement for a database.

## 431: How do you build a local cache from a compacted topic?

Read the whole topic at startup with a consumer that uses `assign()` on all partitions (not a group, since every instance needs all data), apply each record to an in-memory map (removing keys on tombstones), and keep consuming for updates. Mark the cache as ready only once the consumer has reached the end offsets captured at startup.

```java
consumer.assign(partitions);
consumer.seekToBeginning(partitions);
Map<TopicPartition, Long> end = consumer.endOffsets(partitions);

while (!caughtUp(consumer, end)) {
    for (var r : consumer.poll(Duration.ofMillis(200))) {
        if (r.value() == null) cache.remove(r.key());
        else cache.put(r.key(), r.value());
    }
}
ready = true;
```

Kafka Streams' `GlobalKTable` does exactly this for you.

## 432: How do you join data from two topics without Kafka Streams?

- **Use another engine:** Flink, Spark Structured Streaming or ksqlDB.
- **Materialize one side:** consume the smaller topic into a local cache or database, then enrich records from the other topic by looking them up.
- **Join in a database:** sink both topics into tables and query.

The hard parts are the same as in Kafka Streams: handling timing (one side arrives before the other), state size, and restarts. That is why using a stream processing library is usually better than writing your own join.

## 433: Scenario: consumers are hours behind after a traffic spike. What do you do?

1. Check that consumers are healthy and not stuck in rebalances or errors (poison pill).
2. Check where the time goes: processing code, external calls, or fetching.
3. Scale out consumers, up to the partition count.
4. Raise batch efficiency: larger `max.poll.records`, `fetch.min.bytes`, and batched writes to downstream systems.
5. Check that downstream systems (databases, APIs) are not the real bottleneck.
6. If the backlog will exceed retention, raise retention on the topic now to avoid losing data.
7. If old data is useless (for example live notifications), decide with the business whether to skip ahead by resetting offsets.

Afterwards, plan for more partitions or autoscaling on lag.

## 434: Scenario: users report that events are processed out of order. How do you investigate?

Check:

- **Keys:** are related events using the same key? Different keys means different partitions and no ordering.
- **Partition count changes:** was the topic expanded recently?
- **Producer settings:** idempotence off with `max.in.flight.requests.per.connection > 1`?
- **Multiple producers:** two services writing events for the same entity cannot be ordered relative to each other.
- **Consumer code:** is it processing records in parallel threads, or retrying failures via retry topics?
- **Partitioners:** Java and librdkafka producers writing to the same topic with different hash functions.

The fix usually involves the key choice and consumer concurrency, plus version numbers in events to detect stale updates.

## 435: Scenario: a consumer reprocesses the same messages after every restart. Why?

Likely causes:

- Offsets are never committed (auto commit off and no manual commit, or commits failing silently with `commitAsync`).
- The consumer is not closed cleanly, and with auto commit the last few seconds are not committed.
- A random or changing `group.id` (for example including a hostname or UUID), so each start is a new group reading from `earliest`.
- Committing `record.offset()` instead of `record.offset() + 1`, causing one duplicate per partition.
- Offsets expired because the group was empty longer than `offsets.retention.minutes`.
- Processing takes longer than `max.poll.interval.ms`, so commits fail with `CommitFailedException`.

Check with `kafka-consumer-groups.sh --describe` whether the committed offsets actually move.

## 436: Scenario: producers suddenly get NOT_ENOUGH_REPLICAS errors. What is going on?

The ISR for some partitions has dropped below `min.insync.replicas`, so `acks=all` writes are refused. Steps:

1. List under-min-ISR partitions with `kafka-topics.sh --describe --under-min-isr-partitions`.
2. See which brokers are missing from the ISR: down, restarting, or slow.
3. If a broker is down, bring it back or move its replicas.
4. If brokers are up but followers lag, look at disk, network and replica fetcher threads.

Do not "fix" it by lowering `min.insync.replicas` unless you accept the risk of data loss, and if you do, put it back once the cluster is healthy.

## 437: Scenario: a consumer group rebalances every few minutes. How do you fix it?

1. Look at the consumer logs around each rebalance for the reason: member left, poll timeout, session timeout, or new member joined.
2. **Poll timeout** ("consumer poll timeout has expired"): processing per batch is too slow; lower `max.poll.records`, speed up processing, or raise `max.poll.interval.ms`.
3. **Session timeout:** GC pauses, CPU throttling in containers, or network problems.
4. **Members joining and leaving:** crashing pods, liveness probes killing slow consumers, or autoscaling flapping.
5. Reduce the impact with static membership, cooperative assignment, or the new consumer protocol.

## 438: Scenario: disk usage keeps growing on a compacted topic. Why?

- The log cleaner thread has stopped (check `log-cleaner.log` and the cleaner metrics).
- The number of unique keys keeps growing (for example, keys include a timestamp or UUID), so there is nothing to compact.
- Tombstones are never sent for deleted entities.
- `min.compaction.lag.ms` or `segment.ms` are set too high, so most data is not eligible.
- An open or hanging transaction holds back the cleaner.
- `cleanup.policy` was set to `delete` by mistake, or the reverse.

Fix the cause, and consider adding `delete` to the policy if old keys never need to be kept.

## 439: Scenario: a read_committed consumer stops making progress but there is data. Why?

The partition's last stable offset is stuck behind an open transaction. Either a transactional producer started a transaction and is hanging (blocked, slow or crashed without the coordinator timing it out yet), or there is a hanging transaction from a bug.

- Look at the LSO vs high watermark for the partition (consumer lag will look stuck).
- Use `kafka-transactions.sh describe-producers --topic orders --partition 3` to see open transactions and how long they have been open.
- Wait for `transaction.timeout.ms`, fix the producer, or use `kafka-transactions.sh abort` for a hanging one.

## 440: Scenario: how would you design a notification system with Kafka?

- Services publish domain events (`OrderShipped`, `PasswordReset`) to their topics.
- A notification service consumes these events, decides which notifications to send based on user preferences (kept in a compacted topic or database), and writes "send" jobs to channel topics: `notifications.email`, `notifications.sms`, `notifications.push`.
- Channel workers send messages through providers. These are independent jobs, so share groups or many partitions work well, with retry topics and a DLQ for failures.
- Use the event ID plus channel as an idempotency key so retries do not send twice.
- Rate limit per user and per provider, and use separate topics for urgent messages (password resets) so they are not stuck behind marketing campaigns.

## 441: Scenario: how would you design an order processing pipeline with Kafka?

- Order service writes the order to its database and an `OrderPlaced` event to an outbox; Debezium or a relay publishes it to `orders` keyed by `orderId`.
- Payment, inventory and shipping services consume it and publish their own events (`PaymentCompleted`, `StockReserved`), forming a saga with compensations on failure.
- All topics keyed by `orderId` so each order's events stay in order.
- Every consumer is idempotent (event IDs stored with changes).
- A Kafka Streams app builds an order status view for the UI and detects stuck orders (no payment in 30 minutes) with windows or punctuators.
- RF 3, `min.insync.replicas=2`, schemas in a registry with backward compatibility, DLQs per consumer with alerts.

## 442: Scenario: how would you design a clickstream analytics pipeline?

- Web and mobile clients send events to a collector API (not directly to Kafka), which validates them and produces to `clicks.raw` with high batching and `zstd` compression. Key by session or user ID.
- A stream processor (Kafka Streams or Flink) cleans, enriches (geo, device, user data from a `GlobalKTable`) and writes to `clicks.enriched`.
- Windowed aggregations (page views per minute, active users) go to topics that feed dashboards.
- An S3 or data lake sink connector writes raw and enriched data in Parquet for batch analytics.
- Short retention on raw topics, tiered storage if longer replay is needed.
- Bot filtering and sampling for very high volume; quotas to protect the cluster from client bugs.

## 443: Scenario: how would you migrate from RabbitMQ to Kafka?

1. Map concepts: exchanges and routing keys become topics and keys; competing consumers become consumer groups (or share groups for work queues); per-message TTL and priorities need redesign since Kafka does not have them.
2. Decide which flows really benefit from Kafka (replay, high throughput, many consumers); simple task queues might stay or move to share groups.
3. Bridge during migration: a connector or small service copies messages from RabbitMQ to Kafka so consumers can move first.
4. Move consumers one by one, then producers. Make consumers idempotent, since duplicates during the switch are likely.
5. Rebuild retries and DLQs, which RabbitMQ handled with its own features.

## 444: Scenario: one broker is much busier than the others. What do you do?

- Check leadership balance: maybe leaders were not moved back after a restart. Run a preferred leader election.
- Check partition placement: maybe it hosts more partitions or bigger ones (new broker added without reassignment, or a hot partition).
- Check if one topic or partition receives most traffic (skewed keys).
- Check if many consumer groups read from it, for example cold reads of old data.
- Reassign partitions to balance load, ideally with a tool like Cruise Control that uses real metrics instead of just partition counts.

## 445: Scenario: a schema change broke consumers in production. How do you recover and prevent it?

Recover:

1. Roll back the producer to the old schema if possible.
2. Consumers are stuck on bad records; either deploy a consumer fix that can read both formats, or skip/redirect the bad records to a DLQ and replay them later after the fix.

Prevent:

- Use a schema registry with compatibility checks (`BACKWARD` or `FULL`) on every subject.
- Turn off auto-registration in production and register schemas through CI, where an incompatible change fails the build.
- Add consumer contract tests that read sample data produced with the new schema.
- For breaking changes, use a new topic or event version, as in question 381.

## 446: What changed in Kafka 4.0 that can break an upgrade?

- **ZooKeeper removed:** you must be on KRaft (migrate on 3.x first).
- **Java:** brokers and tools need Java 17, clients and Streams need Java 11.
- **Old clients:** protocol API versions older than Kafka 2.1 were removed, so very old clients can no longer connect.
- **Message formats v0 and v1 removed** (and related configs like `log.message.format.version`).
- **MirrorMaker 1 removed.**
- **Logging moved to Log4j 2**, so custom `log4j.properties` files need conversion.
- **Kafka Streams:** `exactly_once` and `exactly_once_beta` removed, many deprecated APIs removed.
- **Default changes**, for example the producer `linger.ms` default went from 0 to 5.

Read the "Upgrading to 4.0" notes and check every deprecated API your code uses.

## 447: What are the notable changes in Kafka 4.1 to 4.3?

- **4.1 (September 2025):** Queues for Kafka (share groups) in preview, an early version of the Kafka Streams rebalance protocol (KIP-1071), new OAuth options, and other improvements.
- **4.2 (February 2026):** share groups became production-ready (with new features like the `RENEW` acknowledgement), the Streams rebalance protocol reached general availability with a limited feature set, dead letter queue support for Kafka Streams exception handlers, and Java 25 support.
- **4.3 (May 2026):** cordoned log directories, bootstrapping new followers from the last tiered offset, buffer limits for group and share coordinators, header-aware Kafka Streams state stores, and deprecations planned for removal in 5.0 such as the `streams-scala` module.

Always read the release notes for the exact version you run.

## 448: When should you not use Kafka?

- Small apps with low traffic where a database table or a simple queue would do.
- Request/response communication where the caller needs an immediate answer.
- Per-message routing, priorities, or delayed delivery as core features (RabbitMQ or a cloud queue fits better).
- When you need to query data by arbitrary fields (use a database).
- When the team cannot run it and there is no budget for a managed service. Kafka has real operational cost.
- Very large individual payloads (files, videos).

## 449: What are common anti-patterns when using Kafka?

- Using Kafka as a database with lookups by scanning topics.
- One topic per user, per tenant or per entity instance, leading to huge numbers of topics.
- Huge messages instead of references.
- Ignoring producer callback errors.
- Committing offsets before processing without meaning to.
- No schema management, leading to broken consumers.
- Synchronous request/reply over Kafka for user-facing calls.
- Choosing keys that create hot partitions, or no keys where ordering matters.
- Treating Kafka as "fire and forget" with no monitoring of lag, DLQs or under-replicated partitions.
- Every service creating its own producer per request instead of sharing one.

## 450: How would you explain Kafka's trade-offs in a design review?

What you get:

- Very high throughput and durable storage of events.
- Replay: new consumers and fixed bugs can reprocess history.
- Decoupling: many independent consumers of the same data.
- A big ecosystem: Connect, Streams, CDC tools, managed services.

What it costs:

- Ordering only per partition, and partitions are hard to change later.
- At-least-once by default; consumers must handle duplicates, and exactly-once has limits.
- Eventual consistency between services.
- Operational complexity: capacity planning, upgrades, security, monitoring.
- No built-in querying, delays or priorities.

A good answer ties these to the actual system: what throughput, ordering, retention and failure requirements you have, and whether a simpler tool would meet them.
