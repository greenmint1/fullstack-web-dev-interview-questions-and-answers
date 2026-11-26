# Comparing DBs Interview Questions and Answers

_Last updated: November 26, 2026_

450 interview questions with answers about the different kinds of databases, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions compare how relational, document, key-value, wide-column, graph, time-series, search, vector, columnar and distributed SQL databases are built, and when each one is the right pick. Product names and features are current as of late 2026 (for example PostgreSQL 18, MySQL 8.4 LTS, MongoDB 8, Redis 8, Cassandra 5 and Elasticsearch 9). Code examples use Node.js.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a database?](#1-what-is-a-database)
- [2: What are the main types of databases?](#2-what-are-the-main-types-of-databases)
- [3: What is a relational database?](#3-what-is-a-relational-database)
- [4: What is a NoSQL database?](#4-what-is-a-nosql-database)
- [5: What is the difference between SQL and NoSQL databases?](#5-what-is-the-difference-between-sql-and-nosql-databases)
- [6: What is a document database?](#6-what-is-a-document-database)
- [7: What is a key-value store?](#7-what-is-a-key-value-store)
- [8: What is a wide-column database?](#8-what-is-a-wide-column-database)
- [9: What is a graph database?](#9-what-is-a-graph-database)
- [10: What is a time-series database?](#10-what-is-a-time-series-database)
- [11: What is a search engine database?](#11-what-is-a-search-engine-database)
- [12: What is a vector database?](#12-what-is-a-vector-database)
- [13: What is a columnar database?](#13-what-is-a-columnar-database)
- [14: What is an in-memory database?](#14-what-is-an-in-memory-database)
- [15: What is an embedded database?](#15-what-is-an-embedded-database)
- [16: What is a distributed SQL (NewSQL) database?](#16-what-is-a-distributed-sql-newsql-database)
- [17: What does ACID stand for?](#17-what-does-acid-stand-for)
- [18: What does BASE mean?](#18-what-does-base-mean)
- [19: What is the CAP theorem?](#19-what-is-the-cap-theorem)
- [20: What is eventual consistency?](#20-what-is-eventual-consistency)
- [21: What is strong consistency?](#21-what-is-strong-consistency)
- [22: What is a schema?](#22-what-is-a-schema)
- [23: What does schema-on-write versus schema-on-read mean?](#23-what-does-schema-on-write-versus-schema-on-read-mean)
- [24: What is a primary key?](#24-what-is-a-primary-key)
- [25: What is a foreign key?](#25-what-is-a-foreign-key)
- [26: What is a join?](#26-what-is-a-join)
- [27: What is normalization?](#27-what-is-normalization)
- [28: What is denormalization?](#28-what-is-denormalization)
- [29: What is an index?](#29-what-is-an-index)
- [30: What is a transaction?](#30-what-is-a-transaction)
- [31: What is OLTP?](#31-what-is-oltp)
- [32: What is OLAP?](#32-what-is-olap)
- [33: What is the difference between OLTP and OLAP databases?](#33-what-is-the-difference-between-oltp-and-olap-databases)
- [34: What is a data warehouse?](#34-what-is-a-data-warehouse)
- [35: What is a data lake?](#35-what-is-a-data-lake)
- [36: What is a lakehouse?](#36-what-is-a-lakehouse)
- [37: What is replication?](#37-what-is-replication)
- [38: What is sharding?](#38-what-is-sharding)
- [39: What is the difference between replication and sharding?](#39-what-is-the-difference-between-replication-and-sharding)
- [40: What is vertical scaling?](#40-what-is-vertical-scaling)
- [41: What is horizontal scaling?](#41-what-is-horizontal-scaling)
- [42: What is a read replica?](#42-what-is-a-read-replica)
- [43: What is a primary-replica setup?](#43-what-is-a-primary-replica-setup)
- [44: What is failover?](#44-what-is-failover)
- [45: What is a managed database?](#45-what-is-a-managed-database)
- [46: What is a serverless database?](#46-what-is-a-serverless-database)
- [47: Give examples of popular relational databases.](#47-give-examples-of-popular-relational-databases)
- [48: What is PostgreSQL known for?](#48-what-is-postgresql-known-for)
- [49: What is MySQL known for?](#49-what-is-mysql-known-for)
- [50: What is SQLite good for?](#50-what-is-sqlite-good-for)
- [51: What is MongoDB known for?](#51-what-is-mongodb-known-for)
- [52: What is Redis known for?](#52-what-is-redis-known-for)
- [53: What is the difference between Redis and Memcached?](#53-what-is-the-difference-between-redis-and-memcached)
- [54: What is DynamoDB?](#54-what-is-dynamodb)
- [55: What is Apache Cassandra?](#55-what-is-apache-cassandra)
- [56: What is ScyllaDB?](#56-what-is-scylladb)
- [57: What is Neo4j?](#57-what-is-neo4j)
- [58: What is Elasticsearch?](#58-what-is-elasticsearch)
- [59: What is ClickHouse?](#59-what-is-clickhouse)
- [60: What are Snowflake and BigQuery?](#60-what-are-snowflake-and-bigquery)
- [61: What is DuckDB?](#61-what-is-duckdb)
- [62: What is TimescaleDB?](#62-what-is-timescaledb)
- [63: What is InfluxDB?](#63-what-is-influxdb)
- [64: What is Firestore?](#64-what-is-firestore)
- [65: What is CockroachDB?](#65-what-is-cockroachdb)
- [66: What is Google Spanner?](#66-what-is-google-spanner)
- [67: What is Amazon Aurora?](#67-what-is-amazon-aurora)
- [68: When should you use a relational database?](#68-when-should-you-use-a-relational-database)
- [69: When should you use a document database?](#69-when-should-you-use-a-document-database)
- [70: When should you use a key-value store?](#70-when-should-you-use-a-key-value-store)
- [71: When should you use a graph database?](#71-when-should-you-use-a-graph-database)
- [72: When should you use a time-series database?](#72-when-should-you-use-a-time-series-database)
- [73: When should you use a search engine like Elasticsearch?](#73-when-should-you-use-a-search-engine-like-elasticsearch)
- [74: When should you use a columnar database?](#74-when-should-you-use-a-columnar-database)
- [75: When should you use a vector database?](#75-when-should-you-use-a-vector-database)
- [76: When should you use an in-memory store like Redis?](#76-when-should-you-use-an-in-memory-store-like-redis)
- [77: What is polyglot persistence?](#77-what-is-polyglot-persistence)
- [78: What is a multi-model database?](#78-what-is-a-multi-model-database)
- [79: What is an ORM?](#79-what-is-an-orm)
- [80: How do terms map between relational and document databases?](#80-how-do-terms-map-between-relational-and-document-databases)
- [81: What is BSON?](#81-what-is-bson)
- [82: What is a TTL in a database?](#82-what-is-a-ttl-in-a-database)
- [83: What is a cache?](#83-what-is-a-cache)
- [84: Why are Redis sorted sets good for leaderboards?](#84-why-are-redis-sorted-sets-good-for-leaderboards)
- [85: What is a constraint in a database?](#85-what-is-a-constraint-in-a-database)
- [86: What does NULL mean in SQL?](#86-what-does-null-mean-in-sql)
- [87: Should you use auto-increment IDs or UUIDs?](#87-should-you-use-auto-increment-ids-or-uuids)
- [88: What is an ObjectId in MongoDB?](#88-what-is-an-objectid-in-mongodb)
- [89: What is a view in SQL?](#89-what-is-a-view-in-sql)
- [90: What is a stored procedure?](#90-what-is-a-stored-procedure)
- [91: What is a trigger?](#91-what-is-a-trigger)
- [92: What is CRUD?](#92-what-is-crud)
- [93: What is an ad hoc query?](#93-what-is-an-ad-hoc-query)
- [94: Is a document database really schemaless?](#94-is-a-document-database-really-schemaless)
- [95: What is the difference between latency and throughput?](#95-what-is-the-difference-between-latency-and-throughput)
- [96: What is a backup and why are database backups important?](#96-what-is-a-backup-and-why-are-database-backups-important)
- [97: What is point-in-time recovery?](#97-what-is-point-in-time-recovery)
- [98: What is connection pooling?](#98-what-is-connection-pooling)
- [99: What is PostGIS?](#99-what-is-postgis)
- [100: What is a ledger database?](#100-what-is-a-ledger-database)
- [101: What is the difference between structured, semi-structured and unstructured data?](#101-what-is-the-difference-between-structured-semi-structured-and-unstructured-data)
- [102: What is the difference between JSON and JSONB in PostgreSQL?](#102-what-is-the-difference-between-json-and-jsonb-in-postgresql)
- [103: Can PostgreSQL replace MongoDB?](#103-can-postgresql-replace-mongodb)
- [104: What is object storage and is it a database?](#104-what-is-object-storage-and-is-it-a-database)
- [105: Why shouldn't you store large files inside a database?](#105-why-shouldnt-you-store-large-files-inside-a-database)
- [106: What is Valkey?](#106-what-is-valkey)
- [107: Why do database licenses matter?](#107-why-do-database-licenses-matter)
- [108: What is the difference between MySQL and MariaDB?](#108-what-is-the-difference-between-mysql-and-mariadb)
- [109: What are Microsoft SQL Server and Oracle Database used for?](#109-what-are-microsoft-sql-server-and-oracle-database-used-for)
- [110: What is Supabase?](#110-what-is-supabase)
- [111: What is Neon?](#111-what-is-neon)
- [112: What is Vitess?](#112-what-is-vitess)
- [113: What are Turso and Cloudflare D1?](#113-what-are-turso-and-cloudflare-d1)
- [114: What is IndexedDB?](#114-what-is-indexeddb)
- [115: What is the difference between localStorage and a real database?](#115-what-is-the-difference-between-localstorage-and-a-real-database)
- [116: What are CouchDB and Couchbase?](#116-what-are-couchdb-and-couchbase)
- [117: What are HBase and Google Bigtable?](#117-what-are-hbase-and-google-bigtable)
- [118: What are etcd and ZooKeeper used for?](#118-what-are-etcd-and-zookeeper-used-for)
- [119: What is Prometheus?](#119-what-is-prometheus)
- [120: What is pgvector?](#120-what-is-pgvector)
- [121: What is an embedding?](#121-what-is-an-embedding)
- [122: What does a query look like in different databases?](#122-what-does-a-query-look-like-in-different-databases)
- [123: What is Cypher?](#123-what-is-cypher)
- [124: What is CQL?](#124-what-is-cql)
- [125: What is a full table scan?](#125-what-is-a-full-table-scan)
- [126: What is a query planner?](#126-what-is-a-query-planner)
- [127: What does EXPLAIN do?](#127-what-does-explain-do)
- [128: What is table partitioning in a single database?](#128-what-is-table-partitioning-in-a-single-database)
- [129: What is a hot partition?](#129-what-is-a-hot-partition)
- [130: What is the difference between a read-heavy and a write-heavy workload?](#130-what-is-the-difference-between-a-read-heavy-and-a-write-heavy-workload)
- [131: What is an upsert?](#131-what-is-an-upsert)
- [132: What is an aggregation?](#132-what-is-an-aggregation)
- [133: What is pagination and how does it differ between databases?](#133-what-is-pagination-and-how-does-it-differ-between-databases)
- [134: Is a message queue a database?](#134-is-a-message-queue-a-database)
- [135: What is vendor lock-in with databases?](#135-what-is-vendor-lock-in-with-databases)
- [136: What database would you pick for an MVP or a new startup?](#136-what-database-would-you-pick-for-an-mvp-or-a-new-startup)
- [137: What database would you use for an e-commerce site?](#137-what-database-would-you-use-for-an-e-commerce-site)
- [138: What database would you use for a chat app?](#138-what-database-would-you-use-for-a-chat-app)
- [139: What database would you use for application logs?](#139-what-database-would-you-use-for-application-logs)
- [140: What database would you use for IoT sensor data?](#140-what-database-would-you-use-for-iot-sensor-data)
- [141: What is the difference between a database and a file system?](#141-what-is-the-difference-between-a-database-and-a-file-system)
- [142: What is the difference between a cache and a database?](#142-what-is-the-difference-between-a-cache-and-a-database)
- [143: What is read-your-writes consistency?](#143-what-is-read-your-writes-consistency)
- [144: What is a secondary index?](#144-what-is-a-secondary-index)
- [145: What is a composite key?](#145-what-is-a-composite-key)
- [146: What is a document's embedded data versus a reference?](#146-what-is-a-documents-embedded-data-versus-a-reference)
- [147: What is a database driver?](#147-what-is-a-database-driver)
- [148: Why is PostgreSQL often called the default database choice?](#148-why-is-postgresql-often-called-the-default-database-choice)
- [149: What does "the right database for the job" mean in practice?](#149-what-does-the-right-database-for-the-job-mean-in-practice)
- [150: What questions should you ask before choosing a database?](#150-what-questions-should-you-ask-before-choosing-a-database)

### Moderate Questions (151-300)

- [151: How would you model a blog with posts and comments in a relational database versus MongoDB?](#151-how-would-you-model-a-blog-with-posts-and-comments-in-a-relational-database-versus-mongodb)
- [152: How do you model many-to-many relationships in different databases?](#152-how-do-you-model-many-to-many-relationships-in-different-databases)
- [153: What is access-pattern-first design and which databases need it?](#153-what-is-access-pattern-first-design-and-which-databases-need-it)
- [154: What is single-table design in DynamoDB?](#154-what-is-single-table-design-in-dynamodb)
- [155: How do you design tables in Cassandra?](#155-how-do-you-design-tables-in-cassandra)
- [156: What are the transaction isolation levels?](#156-what-are-the-transaction-isolation-levels)
- [157: What are the default isolation levels in popular databases?](#157-what-are-the-default-isolation-levels-in-popular-databases)
- [158: How do MongoDB read concern and write concern work?](#158-how-do-mongodb-read-concern-and-write-concern-work)
- [159: How does Cassandra's tunable consistency work?](#159-how-does-cassandras-tunable-consistency-work)
- [160: How do DynamoDB consistent reads work?](#160-how-do-dynamodb-consistent-reads-work)
- [161: How do transactions differ across MongoDB, DynamoDB, Redis and Cassandra?](#161-how-do-transactions-differ-across-mongodb-dynamodb-redis-and-cassandra)
- [162: How do Redis transactions differ from SQL transactions?](#162-how-do-redis-transactions-differ-from-sql-transactions)
- [163: What index types does PostgreSQL offer and when do you use them?](#163-what-index-types-does-postgresql-offer-and-when-do-you-use-them)
- [164: What is the ESR rule for MongoDB compound indexes?](#164-what-is-the-esr-rule-for-mongodb-compound-indexes)
- [165: What is the difference between a GSI and an LSI in DynamoDB?](#165-what-is-the-difference-between-a-gsi-and-an-lsi-in-dynamodb)
- [166: How does an inverted index work?](#166-how-does-an-inverted-index-work)
- [167: How does PostgreSQL full-text search compare to Elasticsearch?](#167-how-does-postgresql-full-text-search-compare-to-elasticsearch)
- [168: What is the cache-aside pattern?](#168-what-is-the-cache-aside-pattern)
- [169: What are write-through and write-behind caching?](#169-what-are-write-through-and-write-behind-caching)
- [170: How does Redis persist data?](#170-how-does-redis-persist-data)
- [171: What are Redis eviction policies?](#171-what-are-redis-eviction-policies)
- [172: What is the dual-write problem?](#172-what-is-the-dual-write-problem)
- [173: What is the transactional outbox pattern?](#173-what-is-the-transactional-outbox-pattern)
- [174: What is change data capture (CDC)?](#174-what-is-change-data-capture-cdc)
- [175: How do you get real-time updates from different databases?](#175-how-do-you-get-real-time-updates-from-different-databases)
- [176: How do you scale a relational database?](#176-how-do-you-scale-a-relational-database)
- [177: What is Citus?](#177-what-is-citus)
- [178: Why does PostgreSQL need PgBouncer more than MySQL needs a pooler?](#178-why-does-postgresql-need-pgbouncer-more-than-mysql-needs-a-pooler)
- [179: Why are serverless functions hard on traditional databases?](#179-why-are-serverless-functions-hard-on-traditional-databases)
- [180: How does PostgreSQL compare to MySQL?](#180-how-does-postgresql-compare-to-mysql)
- [181: How does MongoDB compare to DynamoDB?](#181-how-does-mongodb-compare-to-dynamodb)
- [182: How does Cassandra compare to DynamoDB?](#182-how-does-cassandra-compare-to-dynamodb)
- [183: How does Elasticsearch compare to OpenSearch?](#183-how-does-elasticsearch-compare-to-opensearch)
- [184: How does ClickHouse compare to PostgreSQL for analytics?](#184-how-does-clickhouse-compare-to-postgresql-for-analytics)
- [185: How does ClickHouse compare to Snowflake and BigQuery?](#185-how-does-clickhouse-compare-to-snowflake-and-bigquery)
- [186: How does DuckDB compare to ClickHouse?](#186-how-does-duckdb-compare-to-clickhouse)
- [187: How does TimescaleDB compare to InfluxDB?](#187-how-does-timescaledb-compare-to-influxdb)
- [188: Can a relational database handle graph queries?](#188-can-a-relational-database-handle-graph-queries)
- [189: How does pgvector compare to a dedicated vector database?](#189-how-does-pgvector-compare-to-a-dedicated-vector-database)
- [190: How does CockroachDB compare to PostgreSQL?](#190-how-does-cockroachdb-compare-to-postgresql)
- [191: How does Aurora differ from standard RDS?](#191-how-does-aurora-differ-from-standard-rds)
- [192: How does Firestore compare to Supabase?](#192-how-does-firestore-compare-to-supabase)
- [193: How does SQLite compare to PostgreSQL?](#193-how-does-sqlite-compare-to-postgresql)
- [194: How does Redis compare to DynamoDB DAX as a cache?](#194-how-does-redis-compare-to-dynamodb-dax-as-a-cache)
- [195: How do you query Neo4j from Node.js?](#195-how-do-you-query-neo4j-from-nodejs)
- [196: How do you query Elasticsearch from Node.js?](#196-how-do-you-query-elasticsearch-from-nodejs)
- [197: How do you query DynamoDB from Node.js?](#197-how-do-you-query-dynamodb-from-nodejs)
- [198: How do you query ClickHouse from Node.js?](#198-how-do-you-query-clickhouse-from-nodejs)
- [199: How do you use SQLite from Node.js?](#199-how-do-you-use-sqlite-from-nodejs)
- [200: How do schema changes differ between SQL and document databases?](#200-how-do-schema-changes-differ-between-sql-and-document-databases)
- [201: How would you handle multi-tenancy in different databases?](#201-how-would-you-handle-multi-tenancy-in-different-databases)
- [202: What is row level security in PostgreSQL?](#202-what-is-row-level-security-in-postgresql)
- [203: How does SQL injection compare to NoSQL injection?](#203-how-does-sql-injection-compare-to-nosql-injection)
- [204: How do you store money in different databases?](#204-how-do-you-store-money-in-different-databases)
- [205: How do different databases handle dates and time zones?](#205-how-do-different-databases-handle-dates-and-time-zones)
- [206: How do you do soft deletes and what do they cost?](#206-how-do-you-do-soft-deletes-and-what-do-they-cost)
- [207: How do you implement a job queue with different databases?](#207-how-do-you-implement-a-job-queue-with-different-databases)
- [208: How would you implement a rate limiter with Redis compared to a SQL database?](#208-how-would-you-implement-a-rate-limiter-with-redis-compared-to-a-sql-database)
- [209: How do counters behave in different databases?](#209-how-do-counters-behave-in-different-databases)
- [210: How do you generate IDs in a distributed database?](#210-how-do-you-generate-ids-in-a-distributed-database)
- [211: How do you migrate an app from MongoDB to PostgreSQL?](#211-how-do-you-migrate-an-app-from-mongodb-to-postgresql)
- [212: Which databases does Prisma support?](#212-which-databases-does-prisma-support)
- [213: Why are Cassandra batches not like SQL transactions?](#213-why-are-cassandra-batches-not-like-sql-transactions)
- [214: What are tombstones?](#214-what-are-tombstones)
- [215: What is near real-time search in Elasticsearch?](#215-what-is-near-real-time-search-in-elasticsearch)
- [216: What is a mapping explosion in Elasticsearch?](#216-what-is-a-mapping-explosion-in-elasticsearch)
- [217: What is the difference between Redis Sentinel and Redis Cluster?](#217-what-is-the-difference-between-redis-sentinel-and-redis-cluster)
- [218: How do MongoDB replica sets handle failover?](#218-how-do-mongodb-replica-sets-handle-failover)
- [219: What are DynamoDB's capacity modes?](#219-what-are-dynamodbs-capacity-modes)
- [220: What are the main DynamoDB limits developers hit?](#220-what-are-the-main-dynamodb-limits-developers-hit)
- [221: How does a filter expression differ from a key condition in DynamoDB?](#221-how-does-a-filter-expression-differ-from-a-key-condition-in-dynamodb)
- [222: How do backups work in different databases?](#222-how-do-backups-work-in-different-databases)
- [223: How do you test code against different databases?](#223-how-do-you-test-code-against-different-databases)
- [224: How do you implement search-as-you-type with different databases?](#224-how-do-you-implement-search-as-you-type-with-different-databases)
- [225: How do geo queries differ between databases?](#225-how-do-geo-queries-differ-between-databases)
- [226: How do joins work in MongoDB?](#226-how-do-joins-work-in-mongodb)
- [227: What is the MongoDB aggregation pipeline compared to SQL?](#227-what-is-the-mongodb-aggregation-pipeline-compared-to-sql)
- [228: How do relational and document databases handle schema validation?](#228-how-do-relational-and-document-databases-handle-schema-validation)
- [229: How do you handle hot keys in a key-value store?](#229-how-do-you-handle-hot-keys-in-a-key-value-store)
- [230: What is the difference between a materialized view in PostgreSQL and in ClickHouse?](#230-what-is-the-difference-between-a-materialized-view-in-postgresql-and-in-clickhouse)
- [231: What are continuous aggregates in TimescaleDB?](#231-what-are-continuous-aggregates-in-timescaledb)
- [232: What is downsampling and retention in time-series databases?](#232-what-is-downsampling-and-retention-in-time-series-databases)
- [233: How do you choose between Redis and Kafka for event streaming?](#233-how-do-you-choose-between-redis-and-kafka-for-event-streaming)
- [234: How do you keep a search index in sync with the primary database?](#234-how-do-you-keep-a-search-index-in-sync-with-the-primary-database)
- [235: What is eventual consistency's impact on user experience?](#235-what-is-eventual-consistencys-impact-on-user-experience)
- [236: How do optimistic and pessimistic locking compare across databases?](#236-how-do-optimistic-and-pessimistic-locking-compare-across-databases)
- [237: What is a condition expression in DynamoDB?](#237-what-is-a-condition-expression-in-dynamodb)
- [238: What happens when a document grows without limit?](#238-what-happens-when-a-document-grows-without-limit)
- [239: What is the bucket pattern?](#239-what-is-the-bucket-pattern)
- [240: How do Cassandra and DynamoDB store sorted data inside a partition?](#240-how-do-cassandra-and-dynamodb-store-sorted-data-inside-a-partition)
- [241: How do graph databases model data compared to relational ones?](#241-how-do-graph-databases-model-data-compared-to-relational-ones)
- [242: What is the difference between a property graph and RDF?](#242-what-is-the-difference-between-a-property-graph-and-rdf)
- [243: How do vector similarity metrics differ?](#243-how-do-vector-similarity-metrics-differ)
- [244: What is hybrid search?](#244-what-is-hybrid-search)
- [245: How do you filter vector search results by metadata?](#245-how-do-you-filter-vector-search-results-by-metadata)
- [246: How do you pick a partition key?](#246-how-do-you-pick-a-partition-key)
- [247: How does consistent hashing help distributed databases?](#247-how-does-consistent-hashing-help-distributed-databases)
- [248: What is the difference between hash and range partitioning?](#248-what-is-the-difference-between-hash-and-range-partitioning)
- [249: How does MongoDB sharding work?](#249-how-does-mongodb-sharding-work)
- [250: What is a scatter-gather query?](#250-what-is-a-scatter-gather-query)
- [251: How do Elasticsearch shards and replicas work?](#251-how-do-elasticsearch-shards-and-replicas-work)
- [252: Why shouldn't Elasticsearch be your primary database?](#252-why-shouldnt-elasticsearch-be-your-primary-database)
- [253: How do you choose between MySQL and PostgreSQL for a new project?](#253-how-do-you-choose-between-mysql-and-postgresql-for-a-new-project)
- [254: When would you choose MongoDB over PostgreSQL?](#254-when-would-you-choose-mongodb-over-postgresql)
- [255: When would you choose DynamoDB over a relational database?](#255-when-would-you-choose-dynamodb-over-a-relational-database)
- [256: When would you choose Cassandra or ScyllaDB?](#256-when-would-you-choose-cassandra-or-scylladb)
- [257: When should you not use a graph database?](#257-when-should-you-not-use-a-graph-database)
- [258: When should you not use Redis as a primary database?](#258-when-should-you-not-use-redis-as-a-primary-database)
- [259: How do you add caching to an app without causing stale data bugs?](#259-how-do-you-add-caching-to-an-app-without-causing-stale-data-bugs)
- [260: What is a cache stampede and how do you prevent it?](#260-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [261: How do relational databases and Cassandra handle writes differently?](#261-how-do-relational-databases-and-cassandra-handle-writes-differently)
- [262: What is the difference between B-tree and LSM-tree storage engines?](#262-what-is-the-difference-between-b-tree-and-lsm-tree-storage-engines)
- [263: What is a write-ahead log (WAL)?](#263-what-is-a-write-ahead-log-wal)
- [264: How does replication lag affect app design?](#264-how-does-replication-lag-affect-app-design)
- [265: What is the difference between synchronous and asynchronous replication?](#265-what-is-the-difference-between-synchronous-and-asynchronous-replication)
- [266: What is logical replication versus physical replication?](#266-what-is-logical-replication-versus-physical-replication)
- [267: How do you upgrade a database's major version with minimal downtime?](#267-how-do-you-upgrade-a-databases-major-version-with-minimal-downtime)
- [268: What is a covering index?](#268-what-is-a-covering-index)
- [269: How does InnoDB's clustered index affect performance?](#269-how-does-innodbs-clustered-index-affect-performance)
- [270: What is VACUUM in PostgreSQL and why do other databases not need it?](#270-what-is-vacuum-in-postgresql-and-why-do-other-databases-not-need-it)
- [271: How do you handle large text and blobs across databases?](#271-how-do-you-handle-large-text-and-blobs-across-databases)
- [272: How do analytics queries affect an OLTP database?](#272-how-do-analytics-queries-affect-an-oltp-database)
- [273: What is ETL versus ELT?](#273-what-is-etl-versus-elt)
- [274: What is Parquet and why do analytics databases like it?](#274-what-is-parquet-and-why-do-analytics-databases-like-it)
- [275: How do you pick between Snowflake, BigQuery, Redshift and Databricks?](#275-how-do-you-pick-between-snowflake-bigquery-redshift-and-databricks)
- [276: Why is SELECT star expensive in columnar databases?](#276-why-is-select-star-expensive-in-columnar-databases)
- [277: How do you handle updates and deletes in ClickHouse?](#277-how-do-you-handle-updates-and-deletes-in-clickhouse)
- [278: What is a star schema?](#278-what-is-a-star-schema)
- [279: How do you choose a database for a real-time dashboard?](#279-how-do-you-choose-a-database-for-a-real-time-dashboard)
- [280: How do you query JSON data in different databases?](#280-how-do-you-query-json-data-in-different-databases)
- [281: How do generated columns help with JSON in SQL databases?](#281-how-do-generated-columns-help-with-json-in-sql-databases)
- [282: What does it cost to add a new database to your stack?](#282-what-does-it-cost-to-add-a-new-database-to-your-stack)
- [283: How do you design for multi-region with different databases?](#283-how-do-you-design-for-multi-region-with-different-databases)
- [284: What is last-writer-wins conflict resolution?](#284-what-is-last-writer-wins-conflict-resolution)
- [285: How do different databases handle unique constraints?](#285-how-do-different-databases-handle-unique-constraints)
- [286: What is the N+1 query problem and does it apply to NoSQL?](#286-what-is-the-n1-query-problem-and-does-it-apply-to-nosql)
- [287: How does connection handling differ between SQL databases and HTTP-based databases?](#287-how-does-connection-handling-differ-between-sql-databases-and-http-based-databases)
- [288: How would you store user sessions?](#288-how-would-you-store-user-sessions)
- [289: How would you store a social feed?](#289-how-would-you-store-a-social-feed)
- [290: How would you store a product catalog with very different product types?](#290-how-would-you-store-a-product-catalog-with-very-different-product-types)
- [291: What is the entity-attribute-value (EAV) pattern and why is it discouraged?](#291-what-is-the-entity-attribute-value-eav-pattern-and-why-is-it-discouraged)
- [292: How would you store and query audit logs?](#292-how-would-you-store-and-query-audit-logs)
- [293: What is event sourcing and what database fits it?](#293-what-is-event-sourcing-and-what-database-fits-it)
- [294: What is CQRS and how does it relate to using multiple databases?](#294-what-is-cqrs-and-how-does-it-relate-to-using-multiple-databases)
- [295: How do database costs differ between pricing models?](#295-how-do-database-costs-differ-between-pricing-models)
- [296: How do you estimate whether data will fit on one database server?](#296-how-do-you-estimate-whether-data-will-fit-on-one-database-server)
- [297: How do you handle full-text search in MongoDB?](#297-how-do-you-handle-full-text-search-in-mongodb)
- [298: How do NoSQL databases handle aggregations and reports?](#298-how-do-nosql-databases-handle-aggregations-and-reports)
- [299: How do you index arrays in different databases?](#299-how-do-you-index-arrays-in-different-databases)
- [300: How do you compare databases fairly in a benchmark?](#300-how-do-you-compare-databases-fairly-in-a-benchmark)

### Advanced Questions (301-450)

- [301: How does a B-tree index work inside a database?](#301-how-does-a-b-tree-index-work-inside-a-database)
- [302: How does a read work in an LSM-tree database?](#302-how-does-a-read-work-in-an-lsm-tree-database)
- [303: What is a bloom filter and why do databases use it?](#303-what-is-a-bloom-filter-and-why-do-databases-use-it)
- [304: What are the main compaction strategies in LSM databases?](#304-what-are-the-main-compaction-strategies-in-lsm-databases)
- [305: What are read, write and space amplification?](#305-what-are-read-write-and-space-amplification)
- [306: How does MVCC differ between PostgreSQL, MySQL InnoDB and MongoDB?](#306-how-does-mvcc-differ-between-postgresql-mysql-innodb-and-mongodb)
- [307: What are HOT updates in PostgreSQL?](#307-what-are-hot-updates-in-postgresql)
- [308: What is transaction ID wraparound in PostgreSQL?](#308-what-is-transaction-id-wraparound-in-postgresql)
- [309: What is write skew?](#309-what-is-write-skew)
- [310: What is a phantom read?](#310-what-is-a-phantom-read)
- [311: What is a lost update and how do databases prevent it?](#311-what-is-a-lost-update-and-how-do-databases-prevent-it)
- [312: How does snapshot isolation differ from serializable?](#312-how-does-snapshot-isolation-differ-from-serializable)
- [313: How does PostgreSQL implement Serializable isolation?](#313-how-does-postgresql-implement-serializable-isolation)
- [314: What are gap locks and next-key locks in MySQL?](#314-what-are-gap-locks-and-next-key-locks-in-mysql)
- [315: How do databases detect and handle deadlocks?](#315-how-do-databases-detect-and-handle-deadlocks)
- [316: What is two-phase locking (2PL)?](#316-what-is-two-phase-locking-2pl)
- [317: How does the Raft consensus algorithm work?](#317-how-does-the-raft-consensus-algorithm-work)
- [318: How does Paxos compare to Raft?](#318-how-does-paxos-compare-to-raft)
- [319: What are the differences between single-leader, multi-leader and leaderless replication?](#319-what-are-the-differences-between-single-leader-multi-leader-and-leaderless-replication)
- [320: What is a sloppy quorum and hinted handoff?](#320-what-is-a-sloppy-quorum-and-hinted-handoff)
- [321: How do read repair and anti-entropy keep replicas in sync?](#321-how-do-read-repair-and-anti-entropy-keep-replicas-in-sync)
- [322: What are vector clocks?](#322-what-are-vector-clocks)
- [323: What are CRDTs and where are they used?](#323-what-are-crdts-and-where-are-they-used)
- [324: What is the difference between linearizability and serializability?](#324-what-is-the-difference-between-linearizability-and-serializability)
- [325: What is the PACELC theorem?](#325-what-is-the-pacelc-theorem)
- [326: How does Google Spanner use TrueTime?](#326-how-does-google-spanner-use-truetime)
- [327: How do databases without atomic clocks order transactions, like CockroachDB?](#327-how-do-databases-without-atomic-clocks-order-transactions-like-cockroachdb)
- [328: What is two-phase commit (2PC)?](#328-what-is-two-phase-commit-2pc)
- [329: How does TiDB implement distributed transactions?](#329-how-does-tidb-implement-distributed-transactions)
- [330: What is the saga pattern?](#330-what-is-the-saga-pattern)
- [331: What is split brain and how do databases prevent it?](#331-what-is-split-brain-and-how-do-databases-prevent-it)
- [332: What are fencing tokens?](#332-what-are-fencing-tokens)
- [333: Is Redis safe for distributed locks?](#333-is-redis-safe-for-distributed-locks)
- [334: How does Aurora's storage layer work?](#334-how-does-auroras-storage-layer-work)
- [335: What does separating storage and compute give a database?](#335-what-does-separating-storage-and-compute-give-a-database)
- [336: How does Neon split PostgreSQL into storage and compute?](#336-how-does-neon-split-postgresql-into-storage-and-compute)
- [337: How do columnar databases compress data so well?](#337-how-do-columnar-databases-compress-data-so-well)
- [338: What is vectorized query execution?](#338-what-is-vectorized-query-execution)
- [339: What is late materialization?](#339-what-is-late-materialization)
- [340: How does ClickHouse's MergeTree storage and sparse primary index work?](#340-how-does-clickhouses-mergetree-storage-and-sparse-primary-index-work)
- [341: What are data skipping indexes in ClickHouse and zone maps in general?](#341-what-are-data-skipping-indexes-in-clickhouse-and-zone-maps-in-general)
- [342: How do time-series databases compress timestamps and values?](#342-how-do-time-series-databases-compress-timestamps-and-values)
- [343: What is the high-cardinality problem in time-series databases?](#343-what-is-the-high-cardinality-problem-in-time-series-databases)
- [344: How does the HNSW vector index work?](#344-how-does-the-hnsw-vector-index-work)
- [345: What are IVF and product quantization in vector search?](#345-what-are-ivf-and-product-quantization-in-vector-search)
- [346: How do you tune the recall versus speed trade-off in vector search?](#346-how-do-you-tune-the-recall-versus-speed-trade-off-in-vector-search)
- [347: What is DiskANN and why does it matter?](#347-what-is-diskann-and-why-does-it-matter)
- [348: How do Lucene segments work in Elasticsearch?](#348-how-do-lucene-segments-work-in-elasticsearch)
- [349: What is BM25?](#349-what-is-bm25)
- [350: Why is deep pagination expensive in Elasticsearch?](#350-why-is-deep-pagination-expensive-in-elasticsearch)
- [351: What is index-free adjacency in graph databases?](#351-what-is-index-free-adjacency-in-graph-databases)
- [352: Why are graph databases hard to shard?](#352-why-are-graph-databases-hard-to-shard)
- [353: Why is Redis mostly single-threaded and how does it still scale?](#353-why-is-redis-mostly-single-threaded-and-how-does-it-still-scale)
- [354: Can Redis lose acknowledged writes?](#354-can-redis-lose-acknowledged-writes)
- [355: How does Redis Cluster route keys and handle resharding?](#355-how-does-redis-cluster-route-keys-and-handle-resharding)
- [356: How does DynamoDB partition data internally?](#356-how-does-dynamodb-partition-data-internally)
- [357: How do DynamoDB Streams and global tables work?](#357-how-do-dynamodb-streams-and-global-tables-work)
- [358: How do Cassandra nodes find each other and decide where data lives?](#358-how-do-cassandra-nodes-find-each-other-and-decide-where-data-lives)
- [359: Why must Cassandra run repairs regularly?](#359-why-must-cassandra-run-repairs-regularly)
- [360: Why are Cassandra lightweight transactions expensive?](#360-why-are-cassandra-lightweight-transactions-expensive)
- [361: How does MongoDB's WiredTiger engine manage memory and durability?](#361-how-does-mongodbs-wiredtiger-engine-manage-memory-and-durability)
- [362: What are jumbo chunks in MongoDB?](#362-what-are-jumbo-chunks-in-mongodb)
- [363: Why are replication slots in PostgreSQL risky?](#363-why-are-replication-slots-in-postgresql-risky)
- [364: What is logical decoding in PostgreSQL?](#364-what-is-logical-decoding-in-postgresql)
- [365: What is the difference between statement-based and row-based binlog replication in MySQL?](#365-what-is-the-difference-between-statement-based-and-row-based-binlog-replication-in-mysql)
- [366: What are GTIDs in MySQL?](#366-what-are-gtids-in-mysql)
- [367: What is Patroni?](#367-what-is-patroni)
- [368: Why does fsync matter for database durability?](#368-why-does-fsync-matter-for-database-durability)
- [369: What is group commit?](#369-what-is-group-commit)
- [370: Why do some databases manage their own cache instead of using the OS page cache?](#370-why-do-some-databases-manage-their-own-cache-instead-of-using-the-os-page-cache)
- [371: Why is using mmap in a database often criticized?](#371-why-is-using-mmap-in-a-database-often-criticized)
- [372: How do query optimizers estimate costs and why do they go wrong?](#372-how-do-query-optimizers-estimate-costs-and-why-do-they-go-wrong)
- [373: What join algorithms do databases use?](#373-what-join-algorithms-do-databases-use)
- [374: How do distributed databases perform joins across nodes?](#374-how-do-distributed-databases-perform-joins-across-nodes)
- [375: How do secondary indexes work in a sharded database?](#375-how-do-secondary-indexes-work-in-a-sharded-database)
- [376: What are the common approaches to rebalancing data when adding nodes?](#376-what-are-the-common-approaches-to-rebalancing-data-when-adding-nodes)
- [377: How does CockroachDB handle hot ranges?](#377-how-does-cockroachdb-handle-hot-ranges)
- [378: What are follower reads and bounded staleness?](#378-what-are-follower-reads-and-bounded-staleness)
- [379: How do you handle data residency requirements in a global database?](#379-how-do-you-handle-data-residency-requirements-in-a-global-database)
- [380: Why are clocks dangerous in distributed databases?](#380-why-are-clocks-dangerous-in-distributed-databases)
- [381: How do you make writes idempotent across databases?](#381-how-do-you-make-writes-idempotent-across-databases)
- [382: Can you get exactly-once processing between Kafka and a database?](#382-can-you-get-exactly-once-processing-between-kafka-and-a-database)
- [383: What ordering guarantees does CDC give and what can go wrong?](#383-what-ordering-guarantees-does-cdc-give-and-what-can-go-wrong)
- [384: What is the expand and contract pattern for schema changes?](#384-what-is-the-expand-and-contract-pattern-for-schema-changes)
- [385: How do online schema change tools work?](#385-how-do-online-schema-change-tools-work)
- [386: How would you migrate from one database to another with zero downtime?](#386-how-would-you-migrate-from-one-database-to-another-with-zero-downtime)
- [387: How do databases encrypt data and what is client-side field level encryption?](#387-how-do-databases-encrypt-data-and-what-is-client-side-field-level-encryption)
- [388: How do you delete personal data for GDPR in append-only or replicated systems?](#388-how-do-you-delete-personal-data-for-gdpr-in-append-only-or-replicated-systems)
- [389: How are consistent backups taken in a distributed database?](#389-how-are-consistent-backups-taken-in-a-distributed-database)
- [390: What are RPO and RTO and how do database choices affect them?](#390-what-are-rpo-and-rto-and-how-do-database-choices-affect-them)
- [391: What is Jepsen and what has it taught us about databases?](#391-what-is-jepsen-and-what-has-it-taught-us-about-databases)
- [392: What causes tail latency in distributed databases and how do you reduce it?](#392-what-causes-tail-latency-in-distributed-databases-and-how-do-you-reduce-it)
- [393: What is a thread-per-core architecture?](#393-what-is-a-thread-per-core-architecture)
- [394: How does HyperLogLog help count distinct values at scale?](#394-how-does-hyperloglog-help-count-distinct-values-at-scale)
- [395: What are streaming databases?](#395-what-are-streaming-databases)
- [396: What is HTAP?](#396-what-is-htap)
- [397: How does Apache Iceberg provide table features on top of files?](#397-how-does-apache-iceberg-provide-table-features-on-top-of-files)
- [398: Why is S3 becoming the storage layer for many databases?](#398-why-is-s3-becoming-the-storage-layer-for-many-databases)
- [399: How do long-running transactions hurt different databases?](#399-how-do-long-running-transactions-hurt-different-databases)
- [400: What happens when you delete a large amount of data in different databases?](#400-what-happens-when-you-delete-a-large-amount-of-data-in-different-databases)
- [401: How do index bloat and fragmentation differ between engines?](#401-how-do-index-bloat-and-fragmentation-differ-between-engines)
- [402: Why are secondary indexes more expensive in LSM databases?](#402-why-are-secondary-indexes-more-expensive-in-lsm-databases)
- [403: How does SSD write amplification relate to database design?](#403-how-does-ssd-write-amplification-relate-to-database-design)
- [404: How do you avoid noisy neighbors in a multi-tenant database?](#404-how-do-you-avoid-noisy-neighbors-in-a-multi-tenant-database)
- [405: How do you choose between consistency and availability per feature?](#405-how-do-you-choose-between-consistency-and-availability-per-feature)
- [406: How would you design the database for a URL shortener?](#406-how-would-you-design-the-database-for-a-url-shortener)
- [407: How would you store and query live locations for a ride-sharing app?](#407-how-would-you-store-and-query-live-locations-for-a-ride-sharing-app)
- [408: How would you design the database for a banking ledger?](#408-how-would-you-design-the-database-for-a-banking-ledger)
- [409: How would you handle inventory during a flash sale?](#409-how-would-you-handle-inventory-during-a-flash-sale)
- [410: How would you store 1 billion product analytics events per day?](#410-how-would-you-store-1-billion-product-analytics-events-per-day)
- [411: How would you design databases for a global SaaS with strict data residency?](#411-how-would-you-design-databases-for-a-global-saas-with-strict-data-residency)
- [412: How would you store messages for a chat system with hundreds of millions of users?](#412-how-would-you-store-messages-for-a-chat-system-with-hundreds-of-millions-of-users)
- [413: How would you choose databases for a recommendation engine?](#413-how-would-you-choose-databases-for-a-recommendation-engine)
- [414: How would you use databases for fraud detection?](#414-how-would-you-use-databases-for-fraud-detection)
- [415: How would you design storage for a RAG system over company documents?](#415-how-would-you-design-storage-for-a-rag-system-over-company-documents)
- [416: How would you build a global real-time leaderboard with millions of players?](#416-how-would-you-build-a-global-real-time-leaderboard-with-millions-of-players)
- [417: How would you prevent double booking in a reservation system?](#417-how-would-you-prevent-double-booking-in-a-reservation-system)
- [418: A MongoDB app gets slower as data grows. What do you check?](#418-a-mongodb-app-gets-slower-as-data-grows-what-do-you-check)
- [419: A 10 TB PostgreSQL database is hitting write limits. What are your options?](#419-a-10-tb-postgresql-database-is-hitting-write-limits-what-are-your-options)
- [420: DynamoDB is throttling requests. How do you investigate?](#420-dynamodb-is-throttling-requests-how-do-you-investigate)
- [421: Cassandra read latency suddenly spikes. What do you look at?](#421-cassandra-read-latency-suddenly-spikes-what-do-you-look-at)
- [422: An Elasticsearch cluster turns yellow or red. What does it mean and what do you do?](#422-an-elasticsearch-cluster-turns-yellow-or-red-what-does-it-mean-and-what-do-you-do)
- [423: Redis ran out of memory in production. What happened and how do you fix it?](#423-redis-ran-out-of-memory-in-production-what-happened-and-how-do-you-fix-it)
- [424: How would you choose a database for an offline-first mobile app?](#424-how-would-you-choose-a-database-for-an-offline-first-mobile-app)
- [425: How would you design an active-active multi-region e-commerce backend?](#425-how-would-you-design-an-active-active-multi-region-e-commerce-backend)
- [426: How would you store metrics with high-cardinality labels like customer id?](#426-how-would-you-store-metrics-with-high-cardinality-labels-like-customer-id)
- [427: How would you store data for audited financial reporting?](#427-how-would-you-store-data-for-audited-financial-reporting)
- [428: How would you design storage for a notification system?](#428-how-would-you-design-storage-for-a-notification-system)
- [429: How do you implement search with per-user permissions?](#429-how-do-you-implement-search-with-per-user-permissions)
- [430: How would you move from a self-hosted database to a managed service?](#430-how-would-you-move-from-a-self-hosted-database-to-a-managed-service)
- [431: How does a read-modify-write cycle break in a key-value store and how do you fix it?](#431-how-does-a-read-modify-write-cycle-break-in-a-key-value-store-and-how-do-you-fix-it)
- [432: Why do distributed SQL databases have higher latency than a single PostgreSQL?](#432-why-do-distributed-sql-databases-have-higher-latency-than-a-single-postgresql)
- [433: Why do sequences have gaps, and how do distributed databases handle them?](#433-why-do-sequences-have-gaps-and-how-do-distributed-databases-handle-them)
- [434: How is graph analytics different from graph OLTP?](#434-how-is-graph-analytics-different-from-graph-oltp)
- [435: What is local-first software and what databases support it?](#435-what-is-local-first-software-and-what-databases-support-it)
- [436: What did teams learn from big database migrations?](#436-what-did-teams-learn-from-big-database-migrations)
- [437: What is data gravity and how does it affect database choices?](#437-what-is-data-gravity-and-how-does-it-affect-database-choices)
- [438: Why is PostgreSQL growing into so many specialized areas?](#438-why-is-postgresql-growing-into-so-many-specialized-areas)
- [439: Why is vector search now part of so many general databases?](#439-why-is-vector-search-now-part-of-so-many-general-databases)
- [440: How do you evaluate a new or trendy database before adopting it?](#440-how-do-you-evaluate-a-new-or-trendy-database-before-adopting-it)
- [441: What is the difference between serializability in a single node and in a distributed database?](#441-what-is-the-difference-between-serializability-in-a-single-node-and-in-a-distributed-database)
- [442: How does Kafka's log compare to a database's write-ahead log?](#442-how-does-kafkas-log-compare-to-a-databases-write-ahead-log)
- [443: What should you think about when caching data from an eventually consistent database?](#443-what-should-you-think-about-when-caching-data-from-an-eventually-consistent-database)
- [444: How do you compare database options in a system design interview?](#444-how-do-you-compare-database-options-in-a-system-design-interview)
- [445: What are the real limits of a single relational database server today?](#445-what-are-the-real-limits-of-a-single-relational-database-server-today)
- [446: How does a document database's sharded transaction compare to a distributed SQL transaction?](#446-how-does-a-document-databases-sharded-transaction-compare-to-a-distributed-sql-transaction)
- [447: How do you decide when to denormalize in a relational database?](#447-how-do-you-decide-when-to-denormalize-in-a-relational-database)
- [448: Why do analytics databases avoid row-level indexes?](#448-why-do-analytics-databases-avoid-row-level-indexes)
- [449: What is the difference between how row stores and column stores handle a single-row update?](#449-what-is-the-difference-between-how-row-stores-and-column-stores-handle-a-single-row-update)
- [450: If you could only run one database for a typical web company, what would you pick and why?](#450-if-you-could-only-run-one-database-for-a-typical-web-company-what-would-you-pick-and-why)

---

# Easy Questions (1-150)

## 1: What is a database?

A database is an organized place to store data so programs can save it, find it and change it later. The software that runs it is called a database management system (DBMS). It handles things like storing data on disk, finding rows fast, letting many users work at once and not losing data after a crash.

## 2: What are the main types of databases?

The common groups are:

- Relational (SQL): PostgreSQL, MySQL, SQL Server, Oracle, SQLite.
- Document: MongoDB, Firestore, Couchbase.
- Key-value: Redis, DynamoDB, etcd.
- Wide-column: Cassandra, ScyllaDB, HBase, Bigtable.
- Graph: Neo4j, Amazon Neptune.
- Time-series: TimescaleDB, InfluxDB, Prometheus.
- Search engines: Elasticsearch, OpenSearch.
- Columnar analytics (OLAP): ClickHouse, BigQuery, Snowflake, DuckDB.
- Vector: Pinecone, Qdrant, Milvus, pgvector.
- Distributed SQL (NewSQL): CockroachDB, YugabyteDB, TiDB, Spanner.

## 3: What is a relational database?

A relational database stores data in tables made of rows and columns. Each table has a fixed set of columns with types, and tables are linked to each other with keys. You read and write data with SQL. It is the default choice for most business apps because it keeps data consistent and lets you ask almost any question with joins.

## 4: What is a NoSQL database?

NoSQL is a loose name for databases that don't use the classic table and SQL model. It covers document, key-value, wide-column and graph databases. Most of them were built to scale out across many machines or to store data in a shape closer to how the app uses it. Many now support some SQL-like querying too, so "not only SQL" is a better reading of the name.

## 5: What is the difference between SQL and NoSQL databases?

- Data model: SQL uses tables with a fixed schema. NoSQL uses documents, key-value pairs, wide rows or graphs, often with a flexible schema.
- Queries: SQL has one standard language with joins. NoSQL query languages differ per product and joins are limited or missing.
- Scaling: SQL databases usually scale up (bigger server). Many NoSQL databases were built to scale out (more servers).
- Consistency: SQL databases give strong ACID transactions. Many NoSQL databases give weaker or tunable consistency.

The lines have blurred. PostgreSQL stores JSON well, and MongoDB has multi-document transactions.

## 6: What is a document database?

A document database stores records as documents, usually JSON or a binary form of it like BSON. One document can hold nested objects and arrays, so data that belongs together (an order and its items) lives in one place. MongoDB, Firestore and Couchbase are examples. Documents in the same collection don't need the exact same fields.

## 7: What is a key-value store?

A key-value store saves values under a unique key, like a big hash map. You get, set and delete by key. It is very fast and simple to scale, but you usually can't query by the contents of the value. Redis, Memcached, DynamoDB (at its core) and etcd are examples.

## 8: What is a wide-column database?

A wide-column database stores data in tables, but rows are grouped by a partition key and each partition can hold many rows sorted by a clustering key. It is built for huge write volume spread over many nodes. Cassandra, ScyllaDB, HBase and Google Bigtable are examples. Don't confuse it with a columnar analytics database, which is a different thing.

## 9: What is a graph database?

A graph database stores nodes (things) and relationships (links between things), and both can have properties. It is good when the main questions are about connections, like "friends of friends" or "how is this account linked to that one". Neo4j and Amazon Neptune are examples. Queries use languages like Cypher, Gremlin or the newer ISO standard GQL.

## 10: What is a time-series database?

A time-series database is tuned for data points that come with a timestamp, like metrics, sensor readings or stock prices. Writes are mostly appends, and queries usually ask for ranges of time and aggregates like averages per minute. These databases compress the data heavily and can drop old data automatically. TimescaleDB, InfluxDB, Prometheus and QuestDB are examples.

## 11: What is a search engine database?

A search engine like Elasticsearch or OpenSearch is built for full-text search. It breaks text into words, stores an inverted index (word to list of documents) and ranks results by how well they match. It also handles typos, synonyms, filters and facets. It is usually not the main source of truth; data is copied into it from another database.

## 12: What is a vector database?

A vector database stores embeddings, which are long lists of numbers produced by machine learning models, and finds the vectors closest to a query vector. That is how semantic search and RAG (retrieval for LLM apps) work. Pinecone, Qdrant, Milvus and Weaviate are dedicated ones, and pgvector adds the same thing to PostgreSQL.

## 13: What is a columnar database?

A columnar database stores each column's values together on disk instead of storing each row together. Queries that read a few columns over millions of rows, like "total sales per month", only read the columns they need, and similar values next to each other compress very well. ClickHouse, BigQuery, Snowflake, Redshift and DuckDB work this way.

## 14: What is an in-memory database?

An in-memory database keeps its working data in RAM instead of reading it from disk. That makes reads and writes very fast, often under a millisecond. Redis, Memcached and Valkey are the common ones. Most can still save data to disk for recovery, but the size of the data is limited by how much RAM you can afford.

## 15: What is an embedded database?

An embedded database runs inside your application process as a library, not as a separate server. There is no network and no setup. SQLite is the most used database in the world for this reason: it is in every phone and browser. DuckDB (analytics), RocksDB and LevelDB (key-value) are other embedded databases.

## 16: What is a distributed SQL (NewSQL) database?

Distributed SQL databases give you SQL and ACID transactions like PostgreSQL, but they split and copy data across many nodes automatically. If a node dies, the others keep serving. CockroachDB, YugabyteDB, TiDB and Google Spanner are examples. You pay for this with higher write latency, because every write has to agree with other nodes.

## 17: What does ACID stand for?

- Atomicity: all changes in a transaction happen, or none do.
- Consistency: a transaction moves the database from one valid state to another, so rules like constraints are never broken.
- Isolation: transactions running at the same time don't see each other's half-done work.
- Durability: once a transaction commits, it stays saved even after a crash.

Relational databases are built around ACID.

## 18: What does BASE mean?

BASE stands for Basically Available, Soft state, Eventually consistent. It describes many distributed NoSQL systems: they stay up and answer requests even when parts fail, data on different nodes can differ for a short time, and the copies catch up later. It is the opposite trade-off to strict ACID.

## 19: What is the CAP theorem?

CAP says that when there is a network partition (nodes can't talk to each other), a distributed database must pick between Consistency (every read sees the latest write) and Availability (every request gets an answer). You can't have both during the partition. When the network is fine, you can have both. Partition tolerance is not really optional in a distributed system.

## 20: What is eventual consistency?

Eventual consistency means that if no new writes happen, all copies of the data will become the same after some time. Right after a write, a read from another node might return old data. Systems like Cassandra, DynamoDB (default reads) and DNS work this way. It is fine for likes counters and feeds, but not for bank balances.

## 21: What is strong consistency?

Strong consistency means every read returns the most recent committed write, no matter which node you ask. A single PostgreSQL server gives this naturally. Distributed databases give it with consensus protocols like Raft, which adds latency. DynamoDB and MongoDB let you ask for strongly consistent reads when you need them.

## 22: What is a schema?

A schema describes the shape of the data: tables, columns, types, keys and constraints. In a relational database the schema is enforced by the database. In document databases the schema is often implicit, living in the app code, though you can add validation rules.

## 23: What does schema-on-write versus schema-on-read mean?

Schema-on-write means data is checked against the schema when it is saved. Bad data is rejected right away. This is how relational databases work. Schema-on-read means data is saved as it comes, and the code that reads it decides how to interpret it. Document stores and data lakes often work like this. Schema-on-read is more flexible but moves the checks into every reader.

## 24: What is a primary key?

A primary key is a column, or set of columns, whose value is unique for each row and never null. The database uses it to find a row fast and other tables use it to point at the row. In DynamoDB and Cassandra the primary key also decides which node stores the data, so picking it is a much bigger decision there.

## 25: What is a foreign key?

A foreign key is a column that points at the primary key of another table, like `orders.user_id` pointing at `users.id`. The database checks that the referenced row exists, so you can't create an order for a missing user. Most NoSQL databases don't enforce foreign keys; the app has to keep references valid.

## 26: What is a join?

A join combines rows from two or more tables based on a matching column. For example, joining `orders` and `users` on `orders.user_id = users.id` gives you each order with its user's name. Joins are a core strength of relational databases. Document and key-value stores mostly avoid joins by storing related data together.

```sql
SELECT o.id, o.total, u.name
FROM orders o
JOIN users u ON u.id = o.user_id
WHERE o.created_at > now() - interval '7 days';
```

## 27: What is normalization?

Normalization means splitting data into tables so each fact is stored in one place. A customer's address lives in the `customers` table, not copied into every order. This avoids update problems where one copy changes and another doesn't. Relational design usually aims for third normal form (3NF).

## 28: What is denormalization?

Denormalization means copying data on purpose so reads don't need joins. For example, you store the product name inside each order item. Reads get faster and simpler, but writes get harder because you must update every copy. Document, key-value and wide-column databases rely on denormalization a lot.

## 29: What is an index?

An index is an extra data structure that helps the database find rows without scanning the whole table, like the index at the back of a book. Most databases use a B-tree index by default. Indexes speed up reads but slow down writes a little and take disk space, since every insert or update must also update the index.

## 30: What is a transaction?

A transaction is a group of operations that succeed or fail together. The classic example is moving money: subtract from one account and add to another. If anything fails in the middle, the database rolls back so no money disappears.

```js
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const client = await pool.connect();
try {
  await client.query("BEGIN");
  await client.query(
    "UPDATE accounts SET balance = balance - $1 WHERE id = $2",
    [100, 1],
  );
  await client.query(
    "UPDATE accounts SET balance = balance + $1 WHERE id = $2",
    [100, 2],
  );
  await client.query("COMMIT");
} catch (err) {
  await client.query("ROLLBACK");
  throw err;
} finally {
  client.release();
}
```

## 31: What is OLTP?

OLTP (online transaction processing) is the everyday workload of an app: many small reads and writes, each touching a few rows, like "create order" or "get user by id". It needs low latency and safe concurrent updates. Row-based relational databases like PostgreSQL and MySQL are built for it.

## 32: What is OLAP?

OLAP (online analytical processing) is the reporting workload: few queries, but each one scans millions or billions of rows to compute totals and trends. Columnar databases like ClickHouse, BigQuery, Snowflake and DuckDB are built for it. Running heavy OLAP queries on your OLTP database can slow down the app.

## 33: What is the difference between OLTP and OLAP databases?

OLTP databases store rows together, use indexes for point lookups and handle many small concurrent transactions. OLAP databases store columns together, compress heavily, scan large ranges fast and usually run fewer, bigger queries. A common setup is PostgreSQL or MySQL for the app, with data copied into a warehouse for reports.

## 34: What is a data warehouse?

A data warehouse is a database built for analytics over data collected from many sources. It is usually columnar and separates storage from compute so you can scale them on their own. Snowflake, BigQuery, Redshift and Databricks SQL are common ones. Data is loaded with ETL or ELT pipelines.

## 35: What is a data lake?

A data lake is cheap storage, usually object storage like S3, that holds raw files in any format: logs, JSON, CSV, Parquet, images. You don't need a schema up front. Query engines like Athena, Trino or Spark read the files when needed. It is cheaper than a warehouse but harder to keep clean.

## 36: What is a lakehouse?

A lakehouse puts table features on top of files in a data lake. Formats like Apache Iceberg, Delta Lake and Apache Hudi add a metadata layer over Parquet files so you get schemas, ACID commits, time travel and updates. Many engines (Spark, Trino, Snowflake, DuckDB) can read the same tables.

## 37: What is replication?

Replication means keeping copies of the same data on more than one server. It protects you from losing data when a server dies and lets you spread read traffic over several copies. Almost every production database supports it, from PostgreSQL streaming replication to MongoDB replica sets to Cassandra's built-in copies.

## 38: What is sharding?

Sharding (also called partitioning) splits the data into pieces and puts each piece on a different server. For example, users with ids 1 to 1 million go to shard A and the rest go to shard B. It lets you store more data and handle more writes than one server can. MongoDB, Cassandra, DynamoDB and distributed SQL databases shard automatically; with PostgreSQL or MySQL you usually need extra tools like Citus or Vitess.

## 39: What is the difference between replication and sharding?

Replication copies the same data to several servers. It helps with reading and with surviving failures, but every copy still holds all the data and every write goes everywhere. Sharding splits different data onto different servers. It helps with data size and write throughput. Large systems use both: each shard is replicated.

## 40: What is vertical scaling?

Vertical scaling (scaling up) means moving to a bigger machine: more CPU, more RAM, faster disks. It needs no code changes and works great for relational databases up to a point. The limits are price and the largest machine you can buy, and you still have one server that can fail.

## 41: What is horizontal scaling?

Horizontal scaling (scaling out) means adding more machines and spreading the data or traffic across them. It can grow almost without limit and handles single machine failures well. The cost is complexity: cross-node queries, rebalancing, and harder consistency. Databases like Cassandra and DynamoDB were designed around it.

## 42: What is a read replica?

A read replica is a copy of the primary database that only serves reads. The primary sends its changes to it. You point heavy read traffic, like reports or listing pages, at replicas so the primary has more room for writes. Replicas usually lag a little behind, so a read right after a write may not see it.

## 43: What is a primary-replica setup?

In a primary-replica setup (older name: master-slave), one server takes all writes and copies the changes to one or more replicas. Replicas can serve reads and can be promoted to primary if the primary fails. PostgreSQL, MySQL, MongoDB replica sets and Redis all use this model.

## 44: What is failover?

Failover is switching to a standby server when the main one stops working. It can be manual or automatic. Managed services like Amazon RDS Multi-AZ, Aurora and MongoDB Atlas do it automatically, usually within seconds to a minute. Your app needs to reconnect and retry when it happens.

## 45: What is a managed database?

A managed database is one that a cloud provider runs for you: backups, updates, failover and monitoring are handled. Examples are Amazon RDS and Aurora, Google Cloud SQL, Azure SQL, MongoDB Atlas, Neon and Supabase. You pay more than for a plain server, but you save a lot of operations work.

## 46: What is a serverless database?

A serverless database scales up and down with traffic, can scale to zero when idle, and charges by usage instead of by server. DynamoDB on-demand, Aurora Serverless v2, Neon, Firestore and Cloudflare D1 are examples. They fit spiky or small workloads. Watch for cold starts and cost at steady high load.

## 47: Give examples of popular relational databases.

- PostgreSQL: open source, very feature-rich, strong on extensions and JSON.
- MySQL: open source, very common for web apps, owned by Oracle.
- MariaDB: a community fork of MySQL.
- SQLite: embedded, file-based, zero setup.
- Microsoft SQL Server and Oracle Database: commercial, common in enterprises.

## 48: What is PostgreSQL known for?

PostgreSQL is an open source relational database known for following the SQL standard closely and for having many features: JSONB, full-text search, window functions, CTEs, partial and expression indexes, and a powerful extension system (PostGIS, pgvector, TimescaleDB, Citus). It is often the default choice for new projects.

## 49: What is MySQL known for?

MySQL is one of the most used open source databases, especially for web apps (it is the M in the LAMP stack). Its default engine, InnoDB, gives ACID transactions and row-level locks. It is simple to run, fast for common read-heavy patterns and has large-scale tooling like Vitess. It has fewer advanced SQL features than PostgreSQL.

## 50: What is SQLite good for?

SQLite stores a whole database in a single file and runs inside your app. It is great for mobile and desktop apps, tests, small websites, local caches and edge setups. It handles many readers well but only one writer at a time, so it isn't a fit for busy multi-server write workloads.

## 51: What is MongoDB known for?

MongoDB is the most popular document database. It stores BSON documents in collections, has a rich query language and an aggregation pipeline, and supports secondary indexes, replica sets, automatic sharding and multi-document ACID transactions. It is liked because data in the database looks like objects in your code.

## 52: What is Redis known for?

Redis is an in-memory data store known for speed. Values can be strings, hashes, lists, sets, sorted sets, streams, JSON and more, each with its own commands. It is used for caching, sessions, rate limiting, queues, leaderboards and pub/sub. Since Redis 8, search, JSON and time series are part of the main server. Valkey is an open source fork that many clouds now offer.

## 53: What is the difference between Redis and Memcached?

Both are in-memory key-value caches. Memcached stores only strings, is multi-threaded and very simple. Redis has many data types, persistence to disk, replication, clustering, Lua scripts and pub/sub. Pick Memcached only for a plain, simple cache; Redis covers that and much more.

## 54: What is DynamoDB?

DynamoDB is a fully managed key-value and document database from AWS. You don't manage servers; it scales by splitting data into partitions by the partition key. It gives single-digit millisecond latency at almost any scale if your access patterns are known up front. It has no joins, limited queries and a 400 KB item size limit.

## 55: What is Apache Cassandra?

Cassandra is an open source wide-column database built for very high write volume across many data centers. Every node is equal (no primary), data is spread with consistent hashing and copied to several nodes, and you choose the consistency level per query. You must design tables around your queries, because it has no joins and limited filtering.

## 56: What is ScyllaDB?

ScyllaDB is a rewrite of Cassandra in C++. It speaks the same CQL query language and protocol, but uses a shard-per-core design to get much more throughput per node and steadier latency than Cassandra's Java implementation. Teams pick it when they like the Cassandra model but want fewer nodes.

## 57: What is Neo4j?

Neo4j is the best known graph database. It stores nodes and relationships natively and uses the Cypher query language. Following a relationship is a direct pointer jump instead of an index lookup, so deep traversals stay fast. It is used for recommendations, fraud detection, knowledge graphs and network or permission models.

## 58: What is Elasticsearch?

Elasticsearch is a distributed search and analytics engine built on Apache Lucene. It stores JSON documents in indexes split into shards, and builds inverted indexes for fast full-text search. It is used for site search, log analysis (the ELK stack) and observability. OpenSearch is the fork of it run under the Linux Foundation.

## 59: What is ClickHouse?

ClickHouse is an open source columnar database for real-time analytics. It can scan billions of rows per second on a single server thanks to column storage, compression and vectorized execution. It is used for product analytics, logs and metrics. It is a poor fit for frequent single-row updates or deletes.

## 60: What are Snowflake and BigQuery?

Both are cloud data warehouses for analytics. They store data in a columnar format and separate storage from compute, so you can run big queries without managing servers. BigQuery is serverless and charges per data scanned or per reserved slot. Snowflake runs "virtual warehouses" you size and pause. Both use SQL.

## 61: What is DuckDB?

DuckDB is an embedded analytical database, often called "SQLite for analytics". It runs inside your process, stores data in columns and can query Parquet, CSV and JSON files directly. It is great for data work on a laptop, in a Lambda or in a Node.js script, without setting up a warehouse.

## 62: What is TimescaleDB?

TimescaleDB is a PostgreSQL extension for time-series data. It turns a normal table into a hypertable, which is split into chunks by time behind the scenes. You get time functions like `time_bucket`, compression, retention policies and continuous aggregates, while keeping full SQL and the rest of PostgreSQL.

## 63: What is InfluxDB?

InfluxDB is a time-series database built for metrics, events and IoT data. Data has a measurement name, tags, fields and a timestamp. It focuses on fast ingest, downsampling and retention. Newer versions (InfluxDB 3) store data in Parquet with Apache Arrow and support SQL queries.

## 64: What is Firestore?

Firestore is a serverless document database from Google (part of Firebase). Data is stored in documents grouped into collections, and documents can have subcollections. Its standout features are real-time listeners and offline support in client SDKs, so web and mobile apps can talk to it directly, protected by security rules.

## 65: What is CockroachDB?

CockroachDB is a distributed SQL database that speaks the PostgreSQL wire protocol. It splits data into ranges, keeps three or more copies of each range using the Raft protocol, and runs serializable transactions by default. It survives node and even region failures. It is used when you need SQL and transactions across many regions.

## 66: What is Google Spanner?

Spanner is Google's globally distributed relational database. It offers strong consistency and SQL across regions by using synchronized clocks (TrueTime) to order transactions. It is a managed service on Google Cloud. It is expensive compared to a single PostgreSQL server but removes the need to shard by hand.

## 67: What is Amazon Aurora?

Aurora is an AWS managed database that is compatible with MySQL or PostgreSQL. The difference is the storage layer: data is stored in a shared, distributed volume copied six times across three availability zones. This gives faster failover, up to 15 read replicas that share the same storage, and storage that grows automatically.

## 68: When should you use a relational database?

Use a relational database when your data has clear relationships, you need transactions and constraints, and you want flexible queries you can't fully predict yet. That covers most business apps: users, orders, payments, inventory, bookings. If you are unsure, PostgreSQL is a safe default.

## 69: When should you use a document database?

Use a document database when your records are naturally self-contained objects that you mostly read and write as a whole, like a product page, a user profile with preferences, or a CMS article. It also helps when different records have different fields. It is less good when you need many joins across collections or complex reporting.

## 70: When should you use a key-value store?

Use a key-value store when you always know the key and just need fast get and set: caches, sessions, feature flags, shopping carts, rate limit counters, or config. If you start needing to query by other fields, you either need secondary indexes (like DynamoDB GSIs) or a different database.

## 71: When should you use a graph database?

Use a graph database when the relationships are the main data and your queries go several hops deep: social networks, recommendations, fraud rings, access control graphs, dependency graphs, knowledge graphs. If you only need one or two joins, a relational database is usually enough.

## 72: When should you use a time-series database?

Use one when you collect lots of timestamped data points (metrics, sensor data, prices, logs) and query them by time range with aggregates. Time-series databases ingest fast, compress data 10x or more and delete old data automatically. For small volumes, a normal PostgreSQL table with a time index is fine.

## 73: When should you use a search engine like Elasticsearch?

Use it when users type free text and expect relevant results: product search, document search, autocomplete, typo tolerance, facets and filters. Also for log search. Keep your main data in a primary database and sync it to the search engine, because search engines are not built to be the system of record.

## 74: When should you use a columnar database?

Use one for analytics and reporting over large data: dashboards, product analytics, business intelligence, log analytics. If your queries look like "sum, count, group by over millions of rows", columnar stores are often 10x to 100x faster than row stores. They are a bad fit for many small row updates.

## 75: When should you use a vector database?

Use one when you need similarity search over embeddings: semantic search, RAG for LLM apps, recommendations, image or audio similarity, or duplicate detection. If you already run PostgreSQL and have up to a few million vectors, pgvector is often enough before moving to a dedicated vector database.

## 76: When should you use an in-memory store like Redis?

Use it when you need very low latency for data that fits in RAM: caching slow queries or API calls, sessions, rate limiting, leaderboards, distributed locks, short-lived queues and real-time counters. Don't use it as the only copy of important data unless you have set up persistence and replication carefully.

## 77: What is polyglot persistence?

Polyglot persistence means using different databases for different jobs in the same system. For example: PostgreSQL for orders, Redis for sessions and cache, Elasticsearch for product search and ClickHouse for analytics. Each part gets a tool that fits it. The cost is more systems to run and data to keep in sync.

## 78: What is a multi-model database?

A multi-model database supports more than one data model in one engine. For example, PostgreSQL handles relational data, JSON documents, full-text search, vectors and geospatial data. ArangoDB and SurrealDB support documents, graphs and key-value. Fewer systems to run, but each model may be weaker than a specialized database.

## 79: What is an ORM?

An ORM (object-relational mapper) lets you work with database rows as objects in your code. In Node.js, Prisma, Drizzle, TypeORM and Sequelize are common for SQL databases, and Mongoose is the usual ODM (object document mapper) for MongoDB. ORMs save boilerplate, but you should still understand the SQL they produce.

## 80: How do terms map between relational and document databases?

- Database → database.
- Table → collection.
- Row → document.
- Column → field.
- Primary key → `_id` field in MongoDB.
- Join → `$lookup` or embedding.
- Foreign key → reference (not enforced).

## 81: What is BSON?

BSON (Binary JSON) is the binary format MongoDB uses to store documents. It is like JSON but faster to scan and supports more types: dates, 64-bit integers, decimals, binary data and ObjectId. A single BSON document in MongoDB can be at most 16 MB.

## 82: What is a TTL in a database?

TTL (time to live) makes data expire and get deleted automatically after some time. Redis supports it per key (`EXPIRE`), MongoDB has TTL indexes, DynamoDB has a TTL attribute, and Cassandra supports TTL per write. It is handy for sessions, caches, temporary tokens and old logs.

## 83: What is a cache?

A cache is a fast store that keeps copies of data that is slow or costly to get, so later reads are quicker. In web apps it often sits between your code and the database, usually in Redis or in memory. The hard parts are deciding when cached data is stale and keeping it in sync with the database.

## 84: Why are Redis sorted sets good for leaderboards?

A sorted set keeps members ordered by a score. Adding or updating a score is fast (O(log N)), and getting the top 10 or a player's rank is a single command. Doing the same in SQL needs an index and can get slow at high write rates.

```js
import Redis from "ioredis";

const redis = new Redis();
await redis.zadd("leaderboard", 1500, "alice");
await redis.zincrby("leaderboard", 50, "bob");
const top10 = await redis.zrevrange("leaderboard", 0, 9, "WITHSCORES");
```

## 85: What is a constraint in a database?

A constraint is a rule the database enforces on data: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY` and `CHECK` (like `price > 0`). They stop bad data no matter which app or script writes it. Most NoSQL databases offer few constraints, so the app must enforce them.

## 86: What does NULL mean in SQL?

NULL means "unknown" or "no value", which is different from 0 or an empty string. Comparisons with NULL return unknown, so you must use `IS NULL` instead of `= NULL`. In document databases a field can be missing entirely, which is another state to handle besides being null.

## 87: Should you use auto-increment IDs or UUIDs?

Auto-increment integers are small and fast to index, but they reveal how many rows you have and need one central counter, which is a problem in distributed databases. UUIDs can be created anywhere and don't leak counts, but random UUIDv4 values spread inserts across the index and hurt performance. UUIDv7 (time-ordered) gives the best of both; PostgreSQL 18 has a built-in `uuidv7()` function.

## 88: What is an ObjectId in MongoDB?

An ObjectId is MongoDB's default `_id` value: 12 bytes made of a timestamp, a random value and a counter. It can be created on the client without asking the server and it sorts roughly by creation time. You can read the creation time back with `getTimestamp()`.

## 89: What is a view in SQL?

A view is a saved query that you can select from like a table. It hides complex joins and can limit which columns a user sees. A normal view runs its query every time. A materialized view stores the result and must be refreshed, which is faster to read but can be stale.

## 90: What is a stored procedure?

A stored procedure is code saved inside the database and run there, written in a language like PL/pgSQL or T-SQL. It cuts network round trips and keeps logic close to the data. Most modern web teams keep logic in the app instead, because it is easier to test, version and deploy.

## 91: What is a trigger?

A trigger is code the database runs automatically when a row is inserted, updated or deleted. It can keep audit logs, update a denormalized column or enforce a complex rule. Triggers are hidden from app code, so too many of them make behavior hard to follow.

## 92: What is CRUD?

CRUD stands for Create, Read, Update, Delete, the four basic operations on data. In SQL these are `INSERT`, `SELECT`, `UPDATE` and `DELETE`. In MongoDB they are `insertOne`, `find`, `updateOne` and `deleteOne`. In Redis they map to `SET`, `GET`, `SET` again and `DEL`.

## 93: What is an ad hoc query?

An ad hoc query is a question you didn't plan for when you designed the database, like "which customers in Germany bought two items last March?". Relational and columnar databases handle these well thanks to SQL and the query planner. Key-value and wide-column databases handle them badly, because data is only stored for the queries you designed for.

## 94: Is a document database really schemaless?

Not really. The database doesn't force a schema, but your code still expects certain fields and types. That schema just lives in the app instead of the database. MongoDB supports JSON Schema validation on collections and Mongoose adds schemas in code, because untracked shapes cause bugs over time.

## 95: What is the difference between latency and throughput?

Latency is how long one request takes, like 2 ms per query. Throughput is how many requests you can handle per second. Different databases trade them: Redis has very low latency, ClickHouse has huge scan throughput, and Cassandra has very high write throughput with okay latency. You need to know which one matters for your workload.

## 96: What is a backup and why are database backups important?

A backup is a copy of the data saved somewhere else so you can restore it after a mistake, bug, attack or disaster. Replication doesn't replace backups, because a bad `DELETE` is copied to replicas instantly. Test restores regularly; a backup you have never restored is only a hope.

## 97: What is point-in-time recovery?

Point-in-time recovery (PITR) lets you restore a database to any moment, like "5 minutes before someone dropped the table". It works by combining a full backup with the log of every change after it (WAL in PostgreSQL, binlog in MySQL, oplog in MongoDB). Most managed databases include it.

## 98: What is connection pooling?

Opening a database connection is slow, so apps keep a pool of open connections and reuse them. In Node.js, `pg.Pool` and `mysql2.createPool` do this. PostgreSQL uses one process per connection, so it often needs an external pooler like PgBouncer when you have many app instances or serverless functions.

## 99: What is PostGIS?

PostGIS is a PostgreSQL extension for geographic data. It adds geometry and geography types, spatial indexes and functions like "find all shops within 2 km". MongoDB, Elasticsearch and Redis also have geo features, but PostGIS is the most complete for serious mapping and GIS work.

## 100: What is a ledger database?

A ledger database keeps an append-only, verifiable history of every change, often using cryptographic hashes so tampering can be detected. It fits audit trails, financial records and supply chain data. Amazon QLDB was one but AWS ended it in 2025; today the usual approach is an append-only table in a normal database, or SQL Server's ledger tables.

## 101: What is the difference between structured, semi-structured and unstructured data?

Structured data has a fixed shape, like rows in a table. Semi-structured data has some shape but it can vary, like JSON or XML. Unstructured data has no shape the database understands, like images, videos, PDFs and free text. Relational databases suit structured data, document databases suit semi-structured data, and object storage plus a search or vector index suits unstructured data.

## 102: What is the difference between JSON and JSONB in PostgreSQL?

`json` stores the text exactly as given and parses it on every read. `jsonb` stores a parsed binary form: it drops whitespace and duplicate keys, is a bit slower to write, but is much faster to query and supports GIN indexes. Use `jsonb` in almost every case.

```sql
CREATE TABLE products (id bigint PRIMARY KEY, attrs jsonb);
CREATE INDEX ON products USING gin (attrs);
SELECT id FROM products WHERE attrs @> '{"color": "red"}';
```

## 103: Can PostgreSQL replace MongoDB?

For many apps, yes. With `jsonb` columns and GIN indexes, PostgreSQL stores and queries documents well, and you still get joins, constraints and transactions. MongoDB is still nicer when the whole app is document-shaped, when you want built-in automatic sharding, or when the team prefers its query API and tools.

## 104: What is object storage and is it a database?

Object storage (S3, Google Cloud Storage, Azure Blob) stores files as objects under keys. It is cheap and almost endlessly scalable, but it has no indexes on content, no transactions across objects and no queries. It is not a database by itself, but it is the storage layer under data lakes and many modern databases. Store files there and keep their metadata in a database.

## 105: Why shouldn't you store large files inside a database?

Large blobs make the database bigger, backups slower, replication heavier and memory caches less useful. Object storage is much cheaper per GB and serves files through a CDN. The common pattern is to upload the file to S3 and save its key, size and type in a database row.

## 106: What is Valkey?

Valkey is an open source fork of Redis created in 2024 under the Linux Foundation after Redis changed its license. It started from Redis 7.2 and keeps the BSD license. AWS ElastiCache, Google Memorystore and others offer it. It is a drop-in replacement for most Redis use, and clients like ioredis work with it.

## 107: Why do database licenses matter?

The license decides what you can do with the database, especially if you offer it as a service. PostgreSQL and SQLite have very permissive licenses. MongoDB uses SSPL, which is not accepted as open source by the OSI. CockroachDB and some others moved to source-available or commercial licenses. For most companies using a database inside their own app it doesn't matter, but it affects cloud hosting choices and forks.

## 108: What is the difference between MySQL and MariaDB?

MariaDB is a fork of MySQL started by MySQL's original creator after Oracle bought it. They were almost the same at first but have drifted apart: different optimizers, different JSON handling, different replication features. MariaDB is not a guaranteed drop-in replacement for modern MySQL anymore, so test before switching.

## 109: What are Microsoft SQL Server and Oracle Database used for?

Both are commercial relational databases common in large enterprises, banks and government. They come with strong tooling, support contracts and many advanced features. Licensing costs are high, which is one reason startups and web teams lean towards PostgreSQL and MySQL. SQL Server is tightly tied to the .NET and Azure world.

## 110: What is Supabase?

Supabase is a hosted backend platform built around PostgreSQL. You get a full Postgres database plus auto-generated REST and GraphQL APIs, authentication, file storage, real-time change feeds and edge functions. It is often seen as an open source, SQL-based alternative to Firebase.

## 111: What is Neon?

Neon is a serverless PostgreSQL service. It splits Postgres into compute and a separate storage layer, so compute can scale to zero when idle and start again on request. It also supports database branching, so you can make a copy of your database for a pull request in seconds.

## 112: What is Vitess?

Vitess is a system for sharding MySQL horizontally. It sits between the app and many MySQL servers, routes queries to the right shard and handles resharding with little downtime. It was built at YouTube. PlanetScale is a managed service built on it.

## 113: What are Turso and Cloudflare D1?

Both are SQLite-based databases for the cloud and the edge. Cloudflare D1 is a serverless SQLite database for Cloudflare Workers. Turso is built on libSQL, a fork of SQLite, and offers replicas close to users and embedded replicas inside your app. They fit read-heavy apps that want low latency and SQLite simplicity.

## 114: What is IndexedDB?

IndexedDB is a database built into web browsers. It stores JavaScript objects in object stores, supports indexes and transactions and can hold much more data than `localStorage`. Its API is clunky, so most people use a wrapper like `idb` or Dexie. It is used for offline-first apps and caching in the browser.

## 115: What is the difference between localStorage and a real database?

`localStorage` is a tiny (about 5 MB) synchronous key-value store of strings in the browser. It has no indexes, no transactions and blocks the main thread. It is fine for small settings like a theme. For real data in the browser use IndexedDB, and for shared data use a server-side database.

## 116: What are CouchDB and Couchbase?

CouchDB is a document database known for its HTTP API and multi-master sync, which made it popular for offline-first apps (with PouchDB in the browser). Couchbase is a different product: a distributed document database with a memory-first design, a SQL-like language (SQL++) and mobile sync. The names are similar but they are separate projects.

## 117: What are HBase and Google Bigtable?

Bigtable is Google's wide-column store that inspired many NoSQL databases. Rows are sorted by row key and grouped into column families. HBase is the open source version that runs on Hadoop. Both handle petabytes and huge write rates. They are mostly used for analytics backends, time-series and large web indexes.

## 118: What are etcd and ZooKeeper used for?

They are small, strongly consistent key-value stores for coordination, not general app data. They hold configuration, service discovery data, leader election and locks. Kubernetes stores all its cluster state in etcd. They use consensus (Raft for etcd, ZAB for ZooKeeper) so every node agrees, and they are not built for large data.

## 119: What is Prometheus?

Prometheus is a monitoring system with its own time-series database. It pulls (scrapes) metrics from your services every few seconds, stores them locally and lets you query them with PromQL and set alerts. Its local storage is meant for recent data; long-term storage usually goes to systems like Thanos, Mimir or VictoriaMetrics.

## 120: What is pgvector?

pgvector is a PostgreSQL extension that adds a `vector` type and similarity search. You can store embeddings next to normal columns and find the nearest ones with an index (HNSW or IVFFlat).

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE docs (id bigserial PRIMARY KEY, body text, embedding vector(1536));
CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);
SELECT id, body FROM docs ORDER BY embedding <=> $1 LIMIT 5;
```

## 121: What is an embedding?

An embedding is a list of numbers (a vector) that an ML model produces to represent text, an image or other content. Things with similar meaning end up with vectors close to each other. Vector databases store these and find the closest ones to a query vector, which is how semantic search works.

## 122: What does a query look like in different databases?

The same "find user by email" looks like this:

```js
// PostgreSQL (pg)
await pool.query("SELECT * FROM users WHERE email = $1", [email]);

// MongoDB
await db.collection("users").findOne({ email });

// DynamoDB (lib-dynamodb), with email as the partition key
await doc.send(new GetCommand({ TableName: "users", Key: { email } }));

// Redis, with a key you built yourself
await redis.hgetall(`user:email:${email}`);
```

## 123: What is Cypher?

Cypher is the query language of Neo4j and several other graph databases. It uses ASCII-art patterns to describe paths: `(a)-[:FRIEND]->(b)`. Most of it went into GQL, the ISO graph query language standard published in 2024.

```cypher
MATCH (me:User {id: $id})-[:FRIEND]->(:User)-[:FRIEND]->(fof:User)
WHERE NOT (me)-[:FRIEND]->(fof) AND fof <> me
RETURN DISTINCT fof.name LIMIT 10
```

## 124: What is CQL?

CQL (Cassandra Query Language) is the query language for Cassandra and ScyllaDB. It looks like SQL (`SELECT`, `INSERT`, `CREATE TABLE`) but behaves very differently: no joins, and `WHERE` clauses must normally use the partition key. The SQL look can trick people into designing tables the relational way, which doesn't work.

## 125: What is a full table scan?

A full table scan reads every row in a table to answer a query. It happens when there is no useful index. On small tables it is fine and even faster than using an index. On big tables it is slow and heavy on disk. In DynamoDB the same thing is called a Scan and it costs read capacity for every item read.

## 126: What is a query planner?

A query planner (or optimizer) decides how to run a SQL query: which indexes to use, which join method and in what order to read tables. It uses statistics about your data to guess costs. Relational and columnar databases have planners; key-value stores barely need one because you always ask by key.

## 127: What does EXPLAIN do?

`EXPLAIN` shows the plan the database will use for a query, like whether it uses an index or does a full scan. `EXPLAIN ANALYZE` in PostgreSQL and MySQL actually runs the query and shows real times and row counts. MongoDB has `.explain()` on queries for the same purpose. It is the first tool to use when a query is slow.

## 128: What is table partitioning in a single database?

Table partitioning splits one big table into smaller pieces on the same server, usually by date or by a key range. Queries that filter on the partition key only read the needed pieces, and you can drop old data by dropping a whole partition. PostgreSQL and MySQL support it natively. It is not the same as sharding across servers.

## 129: What is a hot partition?

A hot partition (or hot key) is a piece of data that gets far more traffic than others, like a celebrity's profile or today's date as a partition key. In DynamoDB, Cassandra or any sharded system, that one partition hits its limits while the rest sit idle. Good partition key design spreads traffic evenly.

## 130: What is the difference between a read-heavy and a write-heavy workload?

A read-heavy workload, like a blog or a product catalog, reads data far more than it writes. Caches, read replicas and indexes help a lot. A write-heavy workload, like logging, IoT or click tracking, writes constantly. It benefits from append-friendly storage like LSM trees (Cassandra, RocksDB) or columnar stores with batch inserts, and from fewer indexes.

## 131: What is an upsert?

An upsert inserts a row if it doesn't exist and updates it if it does, in one step. It avoids a race between "check" and "insert".

```js
// PostgreSQL
await pool.query(
  `INSERT INTO counters (id, hits) VALUES ($1, 1)
   ON CONFLICT (id) DO UPDATE SET hits = counters.hits + 1`,
  [pageId],
);

// MongoDB
await db
  .collection("counters")
  .updateOne({ _id: pageId }, { $inc: { hits: 1 } }, { upsert: true });
```

## 132: What is an aggregation?

An aggregation computes a summary over many rows: count, sum, average, min, max, usually grouped by something. In SQL you use `GROUP BY`. In MongoDB you use the aggregation pipeline with `$group`. Columnar databases are much faster at big aggregations because they only read the needed columns.

## 133: What is pagination and how does it differ between databases?

Pagination returns results in pages. SQL databases support `LIMIT` and `OFFSET`, but large offsets are slow, so keyset (cursor) pagination with `WHERE id > last_id` is better. DynamoDB returns a `LastEvaluatedKey` you pass back as `ExclusiveStartKey`. Cassandra uses paging state tokens. Elasticsearch uses `search_after`.

## 134: Is a message queue a database?

Not in the usual sense. Queues like RabbitMQ and SQS hold messages until a consumer takes them, then delete them. Kafka is closer to a database because it keeps an ordered, durable log for a set time and consumers can replay it, but it has no general queries. Many systems use Kafka to move changes between databases.

## 135: What is vendor lock-in with databases?

Lock-in happens when your app depends on features of one product or cloud so much that moving away is very costly. DynamoDB, Firestore, Spanner and Cosmos DB have their own APIs and data models. PostgreSQL and MySQL are available from many providers, so it is easier to move. Lock-in is a trade-off, not always bad, if the managed service saves enough work.

## 136: What database would you pick for an MVP or a new startup?

Usually PostgreSQL, through a managed service like RDS, Cloud SQL, Neon or Supabase. It handles relational data, JSON, full-text search and vectors, so one database covers most early needs. Add Redis when you need caching or queues. Pick specialized databases later, when a real problem shows up.

## 137: What database would you use for an e-commerce site?

The core (customers, orders, payments, stock) should be in a relational database like PostgreSQL or MySQL for transactions and constraints. Add Redis for carts, sessions and caching, Elasticsearch or OpenSearch for product search, and a warehouse like BigQuery or ClickHouse for sales reports.

## 138: What database would you use for a chat app?

Messages are a lot of small writes, read by conversation in time order. Small and medium apps do fine with PostgreSQL and a `(conversation_id, created_at)` index. At very large scale, wide-column stores like Cassandra or ScyllaDB fit well, with the conversation as partition key. Redis pub/sub or streams help with delivering messages live.

## 139: What database would you use for application logs?

Logs are append-only, high volume and searched by text and time. Elasticsearch or OpenSearch are common for full-text search over logs. ClickHouse and Grafana Loki are cheaper at large volume. Keep only recent logs in fast storage and move older ones to object storage.

## 140: What database would you use for IoT sensor data?

A time-series database like TimescaleDB, InfluxDB or QuestDB, or ClickHouse at larger scale. They handle steady streams of timestamped readings, compress them well, downsample old data and drop it after a retention period. Device metadata (owner, location) can live in a normal relational table.

## 141: What is the difference between a database and a file system?

A file system stores named files and lets you read and write bytes. A database understands the structure of the data, so it can index it, query it, enforce rules, run transactions and handle many concurrent writers safely. Storing app data in plain JSON files works until two requests write at the same time or you need to search.

## 142: What is the difference between a cache and a database?

A database is the source of truth; losing its data is a disaster. A cache holds copies that can be rebuilt from the database, so losing it only makes things slower. Caches trade durability and completeness for speed. Redis can play both roles, which is why you must be clear about which role it has in your system.

## 143: What is read-your-writes consistency?

It means that after you write something, your own next reads will see it, even if other users might not yet. Without it, a user updates their profile, refreshes, and sees the old data because the read went to a lagging replica. You can get it by reading from the primary after writes, or by using sticky sessions or causal consistency (MongoDB supports causal sessions).

## 144: What is a secondary index?

A secondary index is any index besides the primary key one, like an index on `email` in a `users` table. Relational databases support many of them easily. In distributed NoSQL databases they are more limited or costly: DynamoDB has GSIs and LSIs with their own capacity, and Cassandra's secondary indexes only work well with care.

## 145: What is a composite key?

A composite key is a primary key made of more than one column, like `(order_id, line_number)`. In Cassandra the primary key has a partition key part (which node) and clustering columns (sort order inside the partition). In DynamoDB, the partition key plus sort key form the composite primary key.

## 146: What is a document's embedded data versus a reference?

Embedding puts related data inside the document, like an array of addresses inside a user. Reading is one fetch, but the document can grow too big. A reference stores only the id of another document, like `authorId`, and needs a second query or `$lookup`. Embed what you read together and what stays small; reference what is shared or grows without limit.

## 147: What is a database driver?

A driver is the library your app uses to talk to a database over its network protocol. In Node.js: `pg` for PostgreSQL, `mysql2` for MySQL, `mongodb` for MongoDB, `ioredis` or `redis` for Redis, `cassandra-driver` for Cassandra, `neo4j-driver` for Neo4j and the AWS SDK for DynamoDB. ORMs sit on top of drivers.

## 148: Why is PostgreSQL often called the default database choice?

It is open source with a permissive license, very reliable, follows the SQL standard and covers many workloads through extensions: documents (`jsonb`), search, geospatial (PostGIS), vectors (pgvector), time series (TimescaleDB) and sharding (Citus). Every cloud offers it managed. Starting with it rarely turns out to be a mistake.

## 149: What does "the right database for the job" mean in practice?

It means choosing based on your data shape, access patterns, consistency needs, scale and team skills, not on hype. In practice most apps need one solid general database plus a cache. A specialized database is worth it when the general one clearly struggles, because each new database adds operations, monitoring, backups and sync work.

## 150: What questions should you ask before choosing a database?

- What does the data look like and how is it related?
- What are the main queries and how often does each run?
- How much data and how many reads and writes per second, now and in two years?
- How strict must consistency be? Can users see slightly old data?
- Do you need multiple regions or offline support?
- Who will run it and what does the team already know?
- What is the budget, and is managed hosting available?

# Moderate Questions (151-300)

## 151: How would you model a blog with posts and comments in a relational database versus MongoDB?

In SQL you would have `users`, `posts` and `comments` tables, with `comments.post_id` and `posts.author_id` as foreign keys, and join them when showing a post. In MongoDB you might embed the author's name and the first few comments in the post document, and keep all comments in a separate `comments` collection with a `postId` field, since comments can grow without limit. The SQL model is cleaner to change; the Mongo model gives one-read page loads.

## 152: How do you model many-to-many relationships in different databases?

- Relational: a join table, like `student_courses(student_id, course_id)`.
- MongoDB: an array of ids on one or both sides, like `courseIds: [...]`, if the lists stay small; otherwise a separate collection like a join table.
- DynamoDB: an adjacency list in a single table, with items for each link and a GSI that flips the keys to query the other direction.
- Graph: just a relationship, `(:Student)-[:ENROLLED_IN]->(:Course)`.

## 153: What is access-pattern-first design and which databases need it?

It means you list every query the app will run before designing tables, then shape the data so each query is one cheap lookup. DynamoDB, Cassandra and other key-value or wide-column stores need it, because they can't run flexible queries later. Relational databases let you design around the data itself and add indexes for new queries as they come.

## 154: What is single-table design in DynamoDB?

Single-table design puts several entity types (users, orders, items) into one DynamoDB table, using generic keys like `PK` and `SK` with prefixes. Related items share a partition key, so one `Query` returns a user and their orders together, which replaces a join. It is fast and cheap but harder to read and to change. For simple apps or when using GraphQL resolvers, one table per entity is often fine.

```text
PK            SK                  data
USER#42       PROFILE             { name, email }
USER#42       ORDER#2026-11-01#9  { total, status }
USER#42       ORDER#2026-11-20#13 { total, status }
```

## 155: How do you design tables in Cassandra?

You start from queries and build one table per query, duplicating data across tables as needed. The partition key decides which node holds the data and must be included in the query; clustering columns decide sort order inside the partition. Keep partitions bounded in size (a common guideline is under about 100 MB), often by adding a time bucket to the key.

```sql
CREATE TABLE messages_by_conversation (
  conversation_id uuid,
  day date,
  sent_at timeuuid,
  sender_id uuid,
  body text,
  PRIMARY KEY ((conversation_id, day), sent_at)
) WITH CLUSTERING ORDER BY (sent_at DESC);
```

## 156: What are the transaction isolation levels?

The SQL standard defines four, from weakest to strongest:

- Read Uncommitted: can see other transactions' uncommitted changes (dirty reads).
- Read Committed: only sees committed data, but the same query can return different results within a transaction.
- Repeatable Read: rows you read won't change during the transaction.
- Serializable: the result is the same as if transactions ran one after another.

Stronger levels prevent more anomalies but can cause more waiting or retries.

## 157: What are the default isolation levels in popular databases?

- PostgreSQL: Read Committed.
- MySQL InnoDB: Repeatable Read.
- SQL Server: Read Committed (locking by default, or snapshot-based if `READ_COMMITTED_SNAPSHOT` is on, which is the default in Azure SQL).
- Oracle: Read Committed.
- CockroachDB: Serializable (Read Committed is also available).
- SQLite: Serializable, since there is only one writer at a time.

Code moving between databases can behave differently because of this.

## 158: How do MongoDB read concern and write concern work?

Write concern says how many nodes must confirm a write before it returns: `w: 1` (primary only) or `w: 'majority'` (default since MongoDB 5.0). Read concern says how "safe" the data you read must be: `local`, `majority`, `linearizable` or `snapshot`. Together they let you trade speed for safety per operation.

```js
await orders.insertOne(order, { writeConcern: { w: "majority" } });
const doc = await orders.findOne(
  { _id: id },
  { readConcern: { level: "majority" } },
);
```

## 159: How does Cassandra's tunable consistency work?

Each read or write picks a consistency level: `ONE`, `QUORUM`, `LOCAL_QUORUM`, `ALL` and others. With replication factor 3, `QUORUM` means 2 replicas must answer. If read replicas plus write replicas is more than the replication factor (R + W > RF), every read overlaps with the latest write and sees it. `LOCAL_QUORUM` is the usual choice in multi-datacenter setups.

```js
import cassandra from "cassandra-driver";

const client = new cassandra.Client({
  contactPoints: ["10.0.0.1"],
  localDataCenter: "dc1",
  keyspace: "chat",
});
await client.execute("SELECT * FROM users WHERE id = ?", [userId], {
  prepare: true,
  consistency: cassandra.types.consistencies.localQuorum,
});
```

## 160: How do DynamoDB consistent reads work?

By default, `GetItem` and `Query` are eventually consistent and may return slightly old data. Passing `ConsistentRead: true` reads the latest committed value but costs twice the read capacity and is not supported on global secondary indexes. Global tables (multi-region) are eventually consistent across regions by default; a strong consistency mode for global tables is also offered.

## 161: How do transactions differ across MongoDB, DynamoDB, Redis and Cassandra?

- MongoDB: real multi-document ACID transactions across collections and shards, with a 60 second default time limit. Best kept short.
- DynamoDB: `TransactWriteItems` and `TransactGetItems` for up to 100 items, all-or-nothing, at double the capacity cost.
- Redis: `MULTI`/`EXEC` runs commands in a row without interruption, but there is no rollback if one command fails. `WATCH` adds optimistic checks.
- Cassandra: no multi-partition transactions; lightweight transactions (`IF NOT EXISTS`, `IF col = x`) give compare-and-set on one partition using Paxos.

## 162: How do Redis transactions differ from SQL transactions?

Redis `MULTI`/`EXEC` queues commands and runs them one after another with no other client in between. But if one command fails at runtime (say, wrong type), the others still run; there is no rollback. Use `WATCH` to abort if a key changed, or a Lua script or Redis Function for logic that must be atomic.

```js
await redis.watch("stock:42");
const stock = Number(await redis.get("stock:42"));
if (stock > 0) {
  const result = await redis
    .multi()
    .decr("stock:42")
    .rpush("orders", orderId)
    .exec();
  if (result === null) {
    // another client changed stock:42, retry
  }
} else {
  await redis.unwatch();
}
```

## 163: What index types does PostgreSQL offer and when do you use them?

- B-tree: default, for equality, ranges and sorting.
- Hash: only equality; rarely better than B-tree.
- GIN: for values with many parts, like `jsonb`, arrays and full-text `tsvector`.
- GiST and SP-GiST: for geometric data, ranges and nearest-neighbor searches (PostGIS uses GiST).
- BRIN: tiny index for huge tables where values follow physical order, like timestamps in append-only logs.

pgvector adds HNSW and IVFFlat for vectors.

## 164: What is the ESR rule for MongoDB compound indexes?

ESR stands for Equality, Sort, Range: put fields used for exact matches first, then fields you sort by, then fields used in range filters. For `find({ status: 'paid', total: { $gt: 100 } }).sort({ createdAt: -1 })`, a good index is `{ status: 1, createdAt: -1, total: 1 }`. The same idea applies to composite B-tree indexes in SQL databases.

## 165: What is the difference between a GSI and an LSI in DynamoDB?

A global secondary index (GSI) has its own partition and sort key, can be added any time, has its own capacity, and is always eventually consistent. A local secondary index (LSI) keeps the same partition key with a different sort key, must be created with the table, supports strongly consistent reads, and limits each partition key's data to 10 GB. GSIs are used far more often.

## 166: How does an inverted index work?

An inverted index maps each word to the list of documents that contain it, like the index at the back of a book. For the query "red shoes", the engine fetches the lists for "red" and "shoes", combines them and scores each document. Text is first run through an analyzer that lowercases, splits and stems words. Elasticsearch, OpenSearch and PostgreSQL GIN full-text indexes use this idea.

## 167: How does PostgreSQL full-text search compare to Elasticsearch?

PostgreSQL full-text search (`tsvector`, `tsquery`, GIN index) is good enough for many apps: it's transactional, needs no extra system and supports ranking and multiple languages. Elasticsearch gives better relevance tuning (BM25, boosts), typo tolerance, synonyms, autocomplete, facets and highlighting, and scales search on its own cluster. Start with Postgres and move to Elasticsearch when search quality or load demands it.

```sql
ALTER TABLE articles ADD COLUMN search tsvector
  GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || body)) STORED;
CREATE INDEX ON articles USING gin (search);
SELECT id, title FROM articles
WHERE search @@ websearch_to_tsquery('english', 'postgres replication')
ORDER BY ts_rank(search, websearch_to_tsquery('english', 'postgres replication')) DESC;
```

## 168: What is the cache-aside pattern?

The app checks the cache first. On a miss, it reads from the database, stores the result in the cache with a TTL and returns it. On writes, it updates the database and deletes the cache key. It is the most common pattern with Redis because the cache only holds data that is actually requested.

```js
async function getProduct(id) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);
  const { rows } = await pool.query("SELECT * FROM products WHERE id = $1", [
    id,
  ]);
  if (rows[0])
    await redis.set(`product:${id}`, JSON.stringify(rows[0]), "EX", 300);
  return rows[0] ?? null;
}
```

## 169: What are write-through and write-behind caching?

Write-through writes to the cache and the database at the same time, so the cache is always fresh but writes are slower. Write-behind (write-back) writes to the cache first and flushes to the database later in batches, which is fast but can lose data if the cache dies. Write-behind needs a durable queue or a cache with persistence to be safe.

## 170: How does Redis persist data?

- RDB: point-in-time snapshots saved every so often. Compact and fast to restore, but you lose changes since the last snapshot.
- AOF (append-only file): logs every write. With `appendfsync everysec` you lose at most about a second of writes.
- Both together are common. You can also turn persistence off for a pure cache.

Even with AOF, Redis is usually not the main store for critical data like payments.

## 171: What are Redis eviction policies?

When Redis reaches `maxmemory`, the eviction policy decides what to delete. `allkeys-lru` and `allkeys-lfu` remove least recently or least frequently used keys from all keys, good for caches. `volatile-*` policies only remove keys that have a TTL. `noeviction` returns errors on writes, which is right when Redis holds data you can't lose.

## 172: What is the dual-write problem?

When your code writes to two systems, like PostgreSQL and Elasticsearch, one write can succeed and the other fail, leaving them out of sync. There is no shared transaction across different databases. Fixes are the outbox pattern or change data capture, so the second system is updated from the first one's committed changes.

## 173: What is the transactional outbox pattern?

Instead of writing to the database and a message broker separately, you write the business row and an "event" row into an `outbox` table in the same transaction. A separate process reads the outbox and publishes the events to Kafka, a queue or another database, then marks them sent. If the app crashes, the event is still in the outbox, so nothing is lost.

## 174: What is change data capture (CDC)?

CDC reads a database's change log (PostgreSQL WAL through logical replication, MySQL binlog, MongoDB change streams, DynamoDB Streams) and turns each insert, update and delete into an event. Tools like Debezium send these events to Kafka, where other systems (search, cache, warehouse) consume them. It keeps databases in sync without changing app code.

## 175: How do you get real-time updates from different databases?

- PostgreSQL: `LISTEN`/`NOTIFY` for simple signals, logical replication for full change feeds (Supabase Realtime uses this).
- MongoDB: change streams with `collection.watch()`.
- DynamoDB: DynamoDB Streams, often consumed by Lambda.
- Firestore: `onSnapshot` listeners straight in the client.
- Redis: pub/sub or streams.

```js
const stream = db
  .collection("orders")
  .watch([{ $match: { operationType: "insert" } }]);
for await (const change of stream) {
  console.log("new order", change.fullDocument._id);
}
```

## 176: How do you scale a relational database?

In order of effort: add indexes and fix slow queries, add a cache, scale up the server, add read replicas, partition big tables, split different features into different databases, and finally shard the data across servers (Citus for PostgreSQL, Vitess for MySQL) or move to distributed SQL. Most apps never need the last step.

## 177: What is Citus?

Citus is a PostgreSQL extension that turns Postgres into a distributed database. You pick a distribution column (often `tenant_id`), and Citus spreads table rows across worker nodes and runs queries in parallel. It fits multi-tenant SaaS and real-time analytics. Azure offers it as a managed service.

## 178: Why does PostgreSQL need PgBouncer more than MySQL needs a pooler?

PostgreSQL starts a separate OS process for every connection, which uses several MB of memory, so a few hundred connections already cost a lot. MySQL uses a thread per connection, which is lighter. With many app servers or serverless functions, PgBouncer (or RDS Proxy, Supavisor) puts thousands of client connections onto a small pool of real ones.

## 179: Why are serverless functions hard on traditional databases?

Each function instance opens its own connection, and under load you can get thousands of short-lived connections, which can exhaust PostgreSQL or MySQL limits. Fixes are a connection pooler or proxy (RDS Proxy, PgBouncer), HTTP-based drivers (Neon serverless driver, PlanetScale), or databases with HTTP APIs like DynamoDB and Firestore that have no connection limits.

## 180: How does PostgreSQL compare to MySQL?

- Features: PostgreSQL has richer SQL (better CTEs, window functions, `jsonb`, partial indexes, many index types, extensions). MySQL is simpler.
- Storage: InnoDB stores rows in the primary key order (clustered index); PostgreSQL uses a heap with separate indexes.
- MVCC cleanup: PostgreSQL needs `VACUUM`; InnoDB uses undo logs that purge on their own.
- Replication and scaling: MySQL has mature tools like Vitess and Group Replication; PostgreSQL has Citus and logical replication.
- Defaults: MySQL is Repeatable Read, PostgreSQL is Read Committed.

Both are good. PostgreSQL is the more common pick for new projects today.

## 181: How does MongoDB compare to DynamoDB?

Both store JSON-like documents. MongoDB has rich ad hoc queries, many secondary indexes, an aggregation pipeline and runs anywhere (Atlas or self-hosted). DynamoDB is fully serverless with almost no operations work and steady latency at any scale, but you must design for known access patterns and it only runs on AWS. MongoDB is more flexible; DynamoDB is more hands-off.

## 182: How does Cassandra compare to DynamoDB?

They share ideas from the Amazon Dynamo paper: partition keys, consistent hashing, replication and tunable consistency. Cassandra is open source, runs anywhere including multiple clouds, and needs a team to operate it. DynamoDB is managed by AWS, with pay-per-request pricing and no servers. Cassandra gives more control over replication and multi-region; DynamoDB gives much less operations work.

## 183: How does Elasticsearch compare to OpenSearch?

OpenSearch was forked from Elasticsearch 7.10 in 2021 after Elastic changed its license. The core is similar (Lucene, JSON documents, query DSL), but they have drifted: different security, machine learning, vector search and dashboard features, and client libraries aren't interchangeable for newer features. Pick OpenSearch for AWS-managed or Linux Foundation projects, Elasticsearch for Elastic's newer features and Elastic Cloud.

## 184: How does ClickHouse compare to PostgreSQL for analytics?

PostgreSQL stores rows, so a query summing one column over 500 million rows reads every full row. ClickHouse reads only that column, compressed, using all CPU cores and vectorized code, so it is often 100x faster for such queries. But ClickHouse doesn't do normal transactions, and updates and deletes are heavy. A common setup is PostgreSQL for the app and ClickHouse for analytics, fed by CDC.

## 185: How does ClickHouse compare to Snowflake and BigQuery?

ClickHouse is open source and designed for low-latency, user-facing analytics: dashboards that must answer in milliseconds under many concurrent queries. Snowflake and BigQuery are managed warehouses tuned for large batch analytics and BI, with easy scaling, strong SQL and data sharing, but higher latency per query and per-use pricing. ClickHouse Cloud narrows the operations gap.

## 186: How does DuckDB compare to ClickHouse?

DuckDB is embedded and single-node: you run it in your process, query local or S3 files, and there is no server. ClickHouse is a server built for many users and large, constantly growing data. Use DuckDB for notebooks, scripts, ETL steps and small apps; use ClickHouse for shared, always-on analytics with high ingest.

## 187: How does TimescaleDB compare to InfluxDB?

TimescaleDB is PostgreSQL plus time-series features, so you get full SQL, joins with your normal tables, and Postgres tools. InfluxDB is a dedicated time-series system with a tag/field model, built for high ingest of metrics. Pick TimescaleDB if you want SQL and already run Postgres; pick InfluxDB for pure metrics pipelines, especially with its Telegraf collector ecosystem.

## 188: Can a relational database handle graph queries?

Yes, up to a point. A recursive CTE can walk a hierarchy or find friends of friends. For two or three hops on indexed tables it works well. For deep or variable-length paths over large graphs, each hop is another join or index lookup and the cost explodes, which is where Neo4j and other native graph databases win.

```sql
WITH RECURSIVE reports AS (
  SELECT id, manager_id, name FROM employees WHERE id = 1
  UNION ALL
  SELECT e.id, e.manager_id, e.name
  FROM employees e JOIN reports r ON e.manager_id = r.id
)
SELECT * FROM reports;
```

## 189: How does pgvector compare to a dedicated vector database?

pgvector keeps embeddings next to your data, so you can filter by tenant or category and join with normal tables in one SQL query, inside transactions, with no extra system. Dedicated vector databases (Pinecone, Qdrant, Milvus, Weaviate) scale further, have more index options, better filtered search at large sizes and features like hybrid search out of the box. pgvector is a good start up to a few million vectors per table.

## 190: How does CockroachDB compare to PostgreSQL?

CockroachDB speaks the PostgreSQL protocol and much of its SQL, but it is a different engine. It spreads data over many nodes with automatic sharding and Raft replication, survives node and region failures, and runs serializable transactions by default. The cost is higher latency per write (consensus round trips), missing Postgres extensions and some differences in behavior. Choose it for multi-region or very high availability needs.

## 191: How does Aurora differ from standard RDS?

Standard RDS runs a normal database engine on an instance with EBS disks; replicas copy data over the network and failover takes a minute or more. Aurora replaces the storage with a shared distributed volume across three availability zones, so replicas read the same storage, lag is usually tiny, and failover is faster. Aurora costs more and its pricing includes I/O (or a flat I/O-Optimized option).

## 192: How does Firestore compare to Supabase?

Firestore is a NoSQL document database with real-time listeners and strong offline support in mobile SDKs, but limited queries (no joins, restricted filters) and per-read pricing. Supabase is PostgreSQL with full SQL, joins, row level security, real-time changes and predictable instance pricing. Firestore suits mobile apps with simple data; Supabase suits apps with relational data or reporting needs.

## 193: How does SQLite compare to PostgreSQL?

SQLite is an embedded file, needs no server, and is very fast for local reads. It has one writer at a time, loose typing by default and fewer features. PostgreSQL is a server with many concurrent writers, strict types, users and roles, replication and extensions. Use SQLite for local, edge, test or small single-server apps; use PostgreSQL when many processes or servers share the data.

## 194: How does Redis compare to DynamoDB DAX as a cache?

DAX is a managed, write-through cache that sits in front of DynamoDB and speaks the DynamoDB API, so you get microsecond reads with almost no code changes. It only caches DynamoDB. Redis is a general cache with many data structures that you manage yourself in code, and it works with any database. Pick DAX for read-heavy DynamoDB apps; pick Redis when you need more than caching DynamoDB items.

## 195: How do you query Neo4j from Node.js?

Use the official `neo4j-driver`. `executeQuery` handles sessions, retries and routing for you.

```js
import neo4j from "neo4j-driver";

const driver = neo4j.driver(
  "neo4j://localhost:7687",
  neo4j.auth.basic("neo4j", process.env.NEO4J_PASSWORD),
);
const { records } = await driver.executeQuery(
  "MATCH (u:User {id: $id})-[:FOLLOWS]->(f:User) RETURN f.name AS name",
  { id: userId },
  { database: "neo4j" },
);
console.log(records.map((r) => r.get("name")));
await driver.close();
```

## 196: How do you query Elasticsearch from Node.js?

Use `@elastic/elasticsearch`. Since version 8 the client returns the response body directly.

```js
import { Client } from "@elastic/elasticsearch";

const es = new Client({ node: "http://localhost:9200" });
await es.index({
  index: "products",
  id: "1",
  document: { name: "Red running shoes", price: 80 },
});
const result = await es.search({
  index: "products",
  query: {
    bool: {
      must: { match: { name: { query: "red shoes", fuzziness: "AUTO" } } },
      filter: { range: { price: { lte: 100 } } },
    },
  },
});
console.log(result.hits.hits.map((h) => h._source));
```

## 197: How do you query DynamoDB from Node.js?

Use the AWS SDK v3 with the document client from `@aws-sdk/lib-dynamodb`, which converts plain JS objects for you.

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, QueryCommand } from "@aws-sdk/lib-dynamodb";

const doc = DynamoDBDocumentClient.from(new DynamoDBClient({}));
const { Items } = await doc.send(
  new QueryCommand({
    TableName: "app",
    KeyConditionExpression: "PK = :pk AND begins_with(SK, :sk)",
    ExpressionAttributeValues: { ":pk": "USER#42", ":sk": "ORDER#" },
    ScanIndexForward: false,
    Limit: 20,
  }),
);
```

## 198: How do you query ClickHouse from Node.js?

Use the official `@clickhouse/client`. Insert in batches, not row by row, because ClickHouse creates a new data part on disk for every insert.

```js
import { createClient } from "@clickhouse/client";

const ch = createClient({ url: "http://localhost:8123" });
await ch.insert({ table: "events", values: events, format: "JSONEachRow" });
const rs = await ch.query({
  query: `SELECT toStartOfHour(ts) AS hour, count() AS c
          FROM events WHERE ts > now() - INTERVAL 1 DAY
          GROUP BY hour ORDER BY hour`,
  format: "JSONEachRow",
});
console.log(await rs.json());
```

## 199: How do you use SQLite from Node.js?

Node.js has a built-in `node:sqlite` module (added in 22.5), and `better-sqlite3` is a popular, fast package. Both are synchronous, which is fine because SQLite runs in the same process and calls are very quick.

```js
import { DatabaseSync } from "node:sqlite";

const db = new DatabaseSync("app.db");
db.exec("PRAGMA journal_mode = WAL");
db.exec(
  "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, body TEXT NOT NULL)",
);
db.prepare("INSERT INTO notes (body) VALUES (?)").run("hello");
console.log(db.prepare("SELECT * FROM notes").all());
```

## 200: How do schema changes differ between SQL and document databases?

In SQL you run migrations (`ALTER TABLE`) that change every row's shape, managed by tools like Prisma Migrate, Drizzle Kit or Flyway. Big tables need care to avoid long locks. In MongoDB or DynamoDB there is no `ALTER`; old documents keep their old shape. You either backfill with a script, or migrate lazily: code reads both shapes and upgrades a document when it next writes it, often using a `schemaVersion` field.

## 201: How would you handle multi-tenancy in different databases?

- Relational: a `tenant_id` column on every table (simple, scales to many tenants), PostgreSQL row level security to enforce it, or a schema or database per tenant for stronger isolation with fewer tenants.
- MongoDB: a `tenantId` field in every document and as the first field of indexes, or a database per tenant.
- DynamoDB: the tenant id as part of the partition key, plus IAM conditions on leading keys for isolation.
- Citus: `tenant_id` as the distribution column so each tenant's data stays on one node.

## 202: What is row level security in PostgreSQL?

Row level security (RLS) lets the database filter rows per user with policies, so a query without a `WHERE tenant_id = ...` still only returns allowed rows. Supabase relies on it so clients can query the database safely. Most NoSQL databases don't have an equal feature; Firestore's security rules are the closest.

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON invoices
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

## 203: How does SQL injection compare to NoSQL injection?

SQL injection happens when user input is glued into a SQL string. NoSQL databases can be attacked too: in MongoDB, if you pass `req.body.password` straight into a query, an attacker can send `{ "$ne": null }` and match any password. Fix both by never building queries from raw input: use parameters in SQL, and validate types (for example with Zod) or cast to strings before MongoDB queries. Mongoose's `sanitizeFilter` option also helps.

## 204: How do you store money in different databases?

Never use floating point types. In SQL use `NUMERIC`/`DECIMAL` (like `numeric(12,2)`), or store integer cents in a `bigint`. In MongoDB use `Decimal128` or integer cents. In DynamoDB numbers are stored as exact decimals, but JavaScript reads them as floats, so integer cents is safest. In Node.js, keep decimals as strings or use a decimal library in calculations.

## 205: How do different databases handle dates and time zones?

PostgreSQL `timestamptz` stores an absolute moment in UTC and converts on display; plain `timestamp` has no zone and is a common bug source. MySQL `TIMESTAMP` is converted to UTC, `DATETIME` is not. MongoDB stores dates as UTC milliseconds. DynamoDB and Redis have no date type, so you store ISO 8601 strings or epoch numbers. Always store UTC and convert at the edges.

## 206: How do you do soft deletes and what do they cost?

A soft delete sets a `deleted_at` column instead of removing the row, so you can restore it and keep history. Every query must then filter `deleted_at IS NULL`, unique constraints need partial indexes, and tables keep growing. In PostgreSQL use a partial index `WHERE deleted_at IS NULL`. In DynamoDB and Cassandra soft deletes avoid tombstones but still cost storage; a TTL can clean them up later.

## 207: How do you implement a job queue with different databases?

- PostgreSQL: a `jobs` table with `SELECT ... FOR UPDATE SKIP LOCKED` so workers grab different rows. Libraries like pg-boss and Graphile Worker do this.
- Redis: lists, streams with consumer groups, or libraries like BullMQ.
- Dedicated brokers: SQS, RabbitMQ, Kafka.

A Postgres queue is great when you want jobs created in the same transaction as your data. Redis and brokers handle higher throughput.

```sql
UPDATE jobs SET status = 'running', started_at = now()
WHERE id = (
  SELECT id FROM jobs WHERE status = 'queued'
  ORDER BY created_at FOR UPDATE SKIP LOCKED LIMIT 1
)
RETURNING *;
```

## 208: How would you implement a rate limiter with Redis compared to a SQL database?

With Redis you use `INCR` with `EXPIRE` (fixed window) or a sorted set or Lua script (sliding window). It is fast, atomic and keys expire on their own. In SQL you'd update a counter row per user per window, which works but adds write load and lock contention on your main database. Rate limiting is one of the clearest wins for Redis.

```js
async function allow(userId, limit = 100) {
  const key = `rl:${userId}:${Math.floor(Date.now() / 60000)}`;
  const [[, count]] = await redis.multi().incr(key).expire(key, 60).exec();
  return count <= limit;
}
```

## 209: How do counters behave in different databases?

In PostgreSQL, many concurrent `UPDATE ... SET n = n + 1` on one row queue up on its row lock. Redis `INCR` is atomic and very fast. Cassandra has a special counter type, but counter updates aren't idempotent, so retries can double count. DynamoDB has atomic `ADD` updates, but one hot item is limited by its partition's throughput. For very hot counters, shard the counter into several rows or keys and sum them on read.

## 210: How do you generate IDs in a distributed database?

You avoid a single auto-increment counter. Options: random UUIDv4, time-ordered UUIDv7 or ULID, Snowflake-style 64-bit ids (timestamp + machine id + sequence), or the database's own scheme like MongoDB ObjectId or CockroachDB's `unique_rowid()`. Time-ordered ids keep B-tree inserts at the end of the index, but in range-sharded databases they create a hot shard, so some systems prefer random ids or hash-sharded indexes.

## 211: How do you migrate an app from MongoDB to PostgreSQL?

Map collections to tables, deciding which embedded objects become child tables and which become `jsonb` columns. Then either do a one-time export and import during downtime, or run both: backfill history, stream new changes with change streams or CDC, switch reads after checking the data matches, and finally switch writes. Rewrite queries, since aggregation pipelines don't map one to one to SQL.

## 212: Which databases does Prisma support?

Prisma supports PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, CockroachDB and MongoDB. MongoDB support has fewer features (no migrations, since there is no schema to migrate). Drizzle supports PostgreSQL, MySQL and SQLite (including Turso and D1) and stays closer to SQL. For DynamoDB and Cassandra, you use the native SDK or a library like ElectroDB or DynamoDB Toolbox.

## 213: Why are Cassandra batches not like SQL transactions?

A Cassandra `BATCH` across many partitions is not a way to speed up inserts. A logged batch makes sure all writes eventually apply, but there is no isolation, and it puts extra load on the coordinator node. Use batches only to keep the same data in several denormalized tables in sync, or for writes to a single partition. For bulk loading, send many async single writes instead.

## 214: What are tombstones?

In LSM-based databases like Cassandra, a delete doesn't remove data right away; it writes a marker called a tombstone. Reads must skip over tombstones until compaction removes them after `gc_grace_seconds` (10 days by default). Patterns with many deletes, like using a table as a queue, pile up tombstones and make reads slow or even fail. TTL'd data also becomes tombstones.

## 215: What is near real-time search in Elasticsearch?

A newly indexed document is not searchable instantly. Elasticsearch makes new documents visible at each refresh, which happens every 1 second by default. So you can write and then not find it for up to a second. You can force a refresh with `refresh: 'wait_for'` on a write, but doing that on every write hurts indexing speed.

## 216: What is a mapping explosion in Elasticsearch?

Every new field name in documents adds to the index mapping. If you index user-generated keys, like `{ "attributes": { "anything-goes": ... } }`, the mapping can grow to thousands of fields, which uses memory and slows the cluster. Elasticsearch limits fields per index to 1000 by default. Use explicit mappings, `dynamic: false` or `strict`, or the `flattened` type for arbitrary keys.

## 217: What is the difference between Redis Sentinel and Redis Cluster?

Sentinel gives high availability for a single primary with replicas: it watches them and promotes a replica if the primary fails. All data is still on one primary. Redis Cluster shards data across many primaries using 16,384 hash slots, each with its own replicas, so it scales writes and memory. In Cluster, multi-key commands only work when all keys are in the same slot; use hash tags like `{user:42}:cart` to group keys.

## 218: How do MongoDB replica sets handle failover?

A replica set has one primary and usually two or more secondaries. If the primary stops responding, the others hold an election based on Raft-like rules and a secondary with the latest data becomes primary, usually within about 10 to 12 seconds. Drivers detect the new primary and retryable writes (on by default) retry once. Writes acknowledged only by the old primary (`w: 1`) can be rolled back, which is why `w: 'majority'` is the default.

## 219: What are DynamoDB's capacity modes?

On-demand mode charges per read and write request and scales instantly; it fits unpredictable or spiky traffic and is the default for new tables. Provisioned mode charges for a set number of read and write capacity units per second, optionally with auto scaling, and is cheaper for steady traffic. You can switch between them. Reserved capacity lowers provisioned costs further.

## 220: What are the main DynamoDB limits developers hit?

- Item size: 400 KB max, including attribute names.
- Partition throughput: about 3,000 read units and 1,000 write units per second per partition.
- Query and Scan return at most 1 MB per call, then you paginate.
- Transactions: up to 100 items per transaction.
- `BatchWriteItem`: 25 items; `BatchGetItem`: 100 items.
- No joins, and filters run after reading, so they don't save capacity.

## 221: How does a filter expression differ from a key condition in DynamoDB?

A key condition (`KeyConditionExpression`) decides which items are read using the partition key and sort key, so you only pay for matching items. A filter expression runs after items are read, removing some before they come back. You still pay for everything read, and you can get an empty page with a `LastEvaluatedKey`. If you filter often by an attribute, add a GSI on it instead.

## 222: How do backups work in different databases?

- PostgreSQL: `pg_dump` for logical backups; base backups plus WAL archiving (pgBackRest, WAL-G) for PITR.
- MySQL: `mysqldump` or MySQL Shell dumps; physical backups with Percona XtraBackup plus binlogs.
- MongoDB: `mongodump` for small data; filesystem snapshots or Atlas continuous backups for large.
- DynamoDB: on-demand backups and continuous PITR for 35 days.
- Cassandra: `nodetool snapshot` per node plus incremental backups, or tools like Medusa.
- Redis: copy RDB/AOF files.

## 223: How do you test code against different databases?

Test against the real engine you use in production, not a substitute. Testcontainers can start PostgreSQL, MySQL, MongoDB, Redis or others in Docker for each test run. Using SQLite in tests while running PostgreSQL in production hides differences in types, SQL syntax and locking. For DynamoDB you can use DynamoDB Local; for MongoDB, `mongodb-memory-server` is common.

## 224: How do you implement search-as-you-type with different databases?

- Elasticsearch/OpenSearch: `search_as_you_type` field type, edge n-gram analyzers or completion suggesters.
- PostgreSQL: `pg_trgm` trigram indexes with `ILIKE '%term%'` or similarity, or prefix matching on `tsquery` with `:*`.
- Redis: the Query Engine's prefix and autocomplete features (`FT.SUGADD`/`FT.SUGGET`), or sorted sets with lexicographic ranges.
- MongoDB Atlas Search: `autocomplete` operator.

Always debounce on the client to cut down requests.

## 225: How do geo queries differ between databases?

PostGIS is the most complete: real geometry types, projections, polygons and spatial joins. MongoDB has `2dsphere` indexes with `$near` and `$geoWithin`. Redis has `GEOADD` and `GEOSEARCH` for simple radius searches over points. Elasticsearch supports `geo_point` and `geo_shape` with filters and distance sorting. For "nearby drivers" Redis is fast; for complex GIS work use PostGIS.

## 226: How do joins work in MongoDB?

MongoDB has `$lookup` in the aggregation pipeline, which works like a left outer join to another collection. It is fine for occasional use, but it's slower than SQL joins and limited in sharded setups, and needing it all the time is a hint that the data should be embedded or that a relational database fits better.

```js
await db
  .collection("orders")
  .aggregate([
    { $match: { status: "paid" } },
    {
      $lookup: {
        from: "users",
        localField: "userId",
        foreignField: "_id",
        as: "user",
      },
    },
    { $unwind: "$user" },
    { $project: { total: 1, "user.name": 1 } },
  ])
  .toArray();
```

## 227: What is the MongoDB aggregation pipeline compared to SQL?

The aggregation pipeline is a list of stages that transform documents one after another: `$match` (like `WHERE`), `$group` (`GROUP BY`), `$sort`, `$project` (`SELECT` columns), `$lookup` (join), `$unwind` (flatten arrays) and many more. It can do most things SQL can, but it reads like a data flow rather than a single statement. Put `$match` early so it can use indexes.

## 228: How do relational and document databases handle schema validation?

Relational databases enforce types, `NOT NULL`, `CHECK` and foreign keys on every write. MongoDB supports `$jsonSchema` validators on collections, with `validationLevel` and `validationAction` to choose strict or warning-only. DynamoDB only checks key attributes. Many teams validate in app code with Zod or Mongoose either way, but database rules protect against scripts and other services too.

## 229: How do you handle hot keys in a key-value store?

Spread the load: cache the hot key in app memory for a short time, add replicas for reads, or split the key into several keys (`counter:1` to `counter:10`) and combine them on read. In DynamoDB, add a random or calculated suffix to the partition key (write sharding). In Redis Cluster, a hot key sits on one shard, so client-side caching or read replicas help.

## 230: What is the difference between a materialized view in PostgreSQL and in ClickHouse?

In PostgreSQL a materialized view stores a query result and is only updated when you run `REFRESH MATERIALIZED VIEW`, which recomputes everything. In ClickHouse a materialized view is more like an insert trigger: every new batch inserted into the source table is transformed and appended to a target table, so aggregates stay current. ClickHouse's style is great for real-time rollups; Postgres's is simpler but can be stale.

## 231: What are continuous aggregates in TimescaleDB?

Continuous aggregates are materialized views over time buckets that TimescaleDB keeps updated in the background, only recalculating buckets that changed. A dashboard asking for hourly averages over a year reads a small precomputed table instead of billions of raw rows. You can also query them in real time, mixing stored buckets with recent raw data.

```sql
CREATE MATERIALIZED VIEW temps_hourly WITH (timescaledb.continuous) AS
SELECT time_bucket('1 hour', time) AS bucket, device_id, avg(temp) AS avg_temp
FROM readings GROUP BY bucket, device_id;
```

## 232: What is downsampling and retention in time-series databases?

Downsampling keeps detailed data for a short time and only summaries (like hourly averages) for older periods. Retention deletes data older than a set age. Together they keep storage stable while you still see long-term trends. TimescaleDB uses continuous aggregates plus `add_retention_policy`; InfluxDB and Prometheus-compatible systems have their own settings.

## 233: How do you choose between Redis and Kafka for event streaming?

Redis Streams are simple, very low latency and good for small to medium volumes kept in memory for a short time. Kafka stores events on disk for days or forever, handles huge throughput, supports many consumer groups replaying history and has a large connector ecosystem. Use Redis Streams for lightweight task or event flows; use Kafka as the backbone for CDC, analytics and many services.

## 234: How do you keep a search index in sync with the primary database?

Options from simple to solid: reindex on a schedule (easy but stale), write to both from app code (risk of dual-write gaps), use an outbox table processed by a worker, or use CDC (Debezium, DynamoDB Streams, MongoDB change streams) to push every change. Also keep a way to fully rebuild the index from the database, because you'll need it when mappings change.

## 235: What is eventual consistency's impact on user experience?

Users may update something and not see it right away, see an item in a list but get "not found" on the detail page, or see counts that don't match. Fix it where it matters: read from the primary right after a write, update the UI optimistically, or route a user to the same replica. Accept it where it doesn't matter, like view counts or recommendation lists.

## 236: How do optimistic and pessimistic locking compare across databases?

Pessimistic locking takes a lock before changing data, like `SELECT ... FOR UPDATE` in SQL, so others wait. Optimistic locking reads a version number and only writes if it hasn't changed. That is the only option in many NoSQL databases: DynamoDB condition expressions, MongoDB `updateOne` with the old version in the filter, Cassandra lightweight transactions and Redis `WATCH`.

```js
const res = await db
  .collection("docs")
  .updateOne(
    { _id: id, version: 7 },
    { $set: { body: newBody }, $inc: { version: 1 } },
  );
if (res.matchedCount === 0) throw new Error("Conflict, reload and try again");
```

## 237: What is a condition expression in DynamoDB?

A condition expression makes a write succeed only if a rule holds, checked atomically on the server. It's used for "create only if not exists", optimistic locking with a version number, or "only decrement stock if it's above zero".

```js
import { UpdateCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new UpdateCommand({
    TableName: "products",
    Key: { id: "p42" },
    UpdateExpression: "SET stock = stock - :one",
    ConditionExpression: "stock >= :one",
    ExpressionAttributeValues: { ":one": 1 },
  }),
);
```

## 238: What happens when a document grows without limit?

In MongoDB, a document has a 16 MB limit, and big documents are slow to read, update and send over the network even before that. In DynamoDB the limit is 400 KB. A common cause is embedding an array that keeps growing, like all comments or all events. Move such data to its own collection or items, or use the bucket pattern (one document per hour or per 100 items).

## 239: What is the bucket pattern?

The bucket pattern groups many small records into one document or partition per time window or count, like one document per sensor per hour holding an array of readings. It cuts the number of documents and index entries and makes range reads cheap. MongoDB recommends it for time-series data, and MongoDB time-series collections do it for you. Cassandra uses the same idea by adding a time bucket to the partition key.

## 240: How do Cassandra and DynamoDB store sorted data inside a partition?

Both keep items inside a partition sorted by a second key: clustering columns in Cassandra, the sort key in DynamoDB. This lets you read ranges like "last 20 messages" or "orders in November" from one partition very quickly, in either direction. Picking that sort key, often a timestamp or a prefix plus timestamp, is a core part of the data model.

## 241: How do graph databases model data compared to relational ones?

In a relational database, a relationship is a foreign key, and following it means a join through an index. In a graph database, a relationship is stored as a direct link between nodes, with its own type and properties, like `(:User)-[:BOUGHT {at: date}]->(:Product)`. Adding a new kind of relationship doesn't need a new join table, which makes graphs good for data whose connections keep changing.

## 242: What is the difference between a property graph and RDF?

A property graph (Neo4j, Neptune with openCypher/Gremlin) has nodes and relationships that both carry key-value properties. RDF (triple stores, Neptune with SPARQL) stores everything as subject-predicate-object triples with global URIs, which fits linked data and ontologies. Most app developers use property graphs; RDF is common in research, publishing and knowledge management.

## 243: How do vector similarity metrics differ?

- Cosine similarity: compares direction only, ignoring length. Most common for text embeddings.
- Dot product (inner product): direction and length; equal to cosine when vectors are normalized, and a bit faster.
- Euclidean (L2) distance: straight-line distance; common for image embeddings.

Use the metric your embedding model was trained for. In pgvector, `<=>` is cosine distance, `<#>` is negative inner product and `<->` is L2 distance.

## 244: What is hybrid search?

Hybrid search combines keyword search (BM25 on an inverted index) with vector search, then merges the results, often using reciprocal rank fusion (RRF). Keyword search is good at exact terms like product codes and names; vector search is good at meaning. Elasticsearch, OpenSearch, Weaviate, Qdrant and MongoDB Atlas support it, and in PostgreSQL you can combine `tsvector` with pgvector.

## 245: How do you filter vector search results by metadata?

You add conditions like `tenant_id = 42` or `category = 'shoes'` to the similarity search. Doing it after the search (post-filtering) can return too few results; doing it before (pre-filtering) can be slow without the right index. Dedicated vector databases have filter-aware indexes. In pgvector 0.8+, iterative index scans help return enough rows when filters are strict.

## 246: How do you pick a partition key?

A good partition key has many distinct values, spreads traffic evenly and matches your main queries so they hit one partition. User id, device id or tenant id are typical. Bad keys are low-cardinality (status, country) or time-based ("today"), which make hot partitions. For time data, combine an id with a time bucket, like `(sensor_id, day)`.

## 247: How does consistent hashing help distributed databases?

Consistent hashing places nodes and keys on a ring by their hash. Each key belongs to the next node on the ring. When a node joins or leaves, only the keys near it move, instead of almost all keys as with `hash % N`. Cassandra, DynamoDB and many caches use it, usually with many virtual nodes per server to balance load.

## 248: What is the difference between hash and range partitioning?

Hash partitioning spreads keys by their hash, so load is even, but range queries across keys hit every partition. Range partitioning keeps keys in sorted ranges, so range scans are fast, but sequential keys (like timestamps) pile up on the last range. Cassandra and DynamoDB hash the partition key; CockroachDB, TiDB, HBase and Bigtable use ranges and split hot ranges automatically.

## 249: How does MongoDB sharding work?

You choose a shard key, and MongoDB splits the collection into chunks by key ranges (or hashed key ranges). `mongos` routers send queries to the right shards; config servers store which chunk lives where; a balancer moves chunks to keep shards even. Queries that include the shard key go to one shard; others are sent to all shards and merged. You can change the shard key later with resharding, but it is heavy.

## 250: What is a scatter-gather query?

It is a query that the router must send to every shard because it doesn't include the shard or partition key, then merge the results. It works but gets slower and more expensive as you add shards, and the slowest shard decides the response time. Design keys so common queries hit a single shard, and use secondary indexes, GSIs or a separate search store for the rest.

## 251: How do Elasticsearch shards and replicas work?

An index is split into primary shards, each a separate Lucene index that can live on a different node. Each primary can have replica shards on other nodes for failover and extra read capacity. The number of primary shards is set when you create the index; changing it means reindexing (or using split and shrink APIs). Too many small shards waste memory, so aim for shards of roughly 10 to 50 GB.

## 252: Why shouldn't Elasticsearch be your primary database?

It has no multi-document transactions, writes are only visible after a refresh, and some failure scenarios can lose acknowledged writes. Mapping changes often require reindexing everything. It's built to be a fast, rebuildable index. Keep the source of truth in PostgreSQL, MySQL or MongoDB and sync to Elasticsearch.

## 253: How do you choose between MySQL and PostgreSQL for a new project?

Pick PostgreSQL if you want richer SQL, `jsonb`, extensions like PostGIS or pgvector, or advanced indexing. Pick MySQL if your team knows it well, you rely on tools built around it (Vitess, PlanetScale, many PHP frameworks), or you want its simpler operations at large scale. For most web apps both work; team experience often matters more than features.

## 254: When would you choose MongoDB over PostgreSQL?

When records are naturally nested documents read and written as a whole, when the shape varies a lot between records, when you want built-in automatic sharding and easy replica sets, or when the team is more productive with MongoDB's API and Atlas features (search, vector search, triggers). If the data is highly relational or needs complex reporting, PostgreSQL is usually the better fit.

## 255: When would you choose DynamoDB over a relational database?

When you are on AWS, access patterns are known and simple (get by key, list by key prefix), and you want steady latency at any scale with no servers to manage. It's great for user sessions, carts, device state, gaming data and serverless backends with Lambda. Avoid it when you need ad hoc queries, reports, many relationships or frequently changing access patterns.

## 256: When would you choose Cassandra or ScyllaDB?

When you have huge write volume (hundreds of thousands of writes per second or more), data measured in terabytes, a need for multi-datacenter active-active writes, and queries you can design for up front. Examples: messaging history, activity feeds, IoT, tracking events. For small data or flexible queries they are overkill and painful.

## 257: When should you not use a graph database?

When your queries are mostly simple lookups, lists and aggregates, when relationships are shallow (one or two joins), or when you need heavy analytics over all records, a graph database adds cost without benefit. Graph databases are also harder to shard. Many "graph" needs are handled fine by PostgreSQL with recursive CTEs or a few join tables.

## 258: When should you not use Redis as a primary database?

When the data is larger than you can afford to keep in RAM, when you can't lose even a second of writes, when you need ad hoc queries or relationships, or when multiple fields must change together under strict rules. Redis can be a primary store for simple, bounded data with AOF and replicas, but most teams keep it as a cache or for specific structures.

## 259: How do you add caching to an app without causing stale data bugs?

Use short TTLs as a safety net, delete (not update) cache keys after writes, and put a version or updated-at value in cache keys where possible. Cache whole computed objects rather than random fragments. Be careful with lists ("latest posts"), since one write can affect many cached lists. Monitor hit rate, and don't cache data that must always be exact, like balances.

## 260: What is a cache stampede and how do you prevent it?

A cache stampede happens when a popular key expires and many requests miss at the same time, all hitting the database together. Prevent it with a lock so only one request rebuilds the value (others wait or serve stale data), with early random refresh before expiry, or by adding random jitter to TTLs so keys don't expire together.

## 261: How do relational databases and Cassandra handle writes differently?

PostgreSQL and MySQL update data in place in B-tree pages (with MVCC copies), write the change to a log, and flush pages later. Cassandra writes to a commit log and an in-memory memtable, then flushes sorted, immutable SSTable files; it never updates in place. That makes Cassandra writes very cheap, but reads may need to merge several files.

## 262: What is the difference between B-tree and LSM-tree storage engines?

B-trees (InnoDB, PostgreSQL, WiredTiger by default) keep data in sorted pages that are updated in place. They give fast, predictable reads but random writes. LSM trees (RocksDB, Cassandra, ScyllaDB, LevelDB) buffer writes in memory, flush them as sorted files and merge files in the background. They give fast writes and good compression, but reads may check several files and compaction uses extra I/O.

## 263: What is a write-ahead log (WAL)?

Before changing data files, the database first writes the change to an append-only log on disk. If the server crashes, it replays the log to recover. PostgreSQL calls it the WAL, MySQL InnoDB has the redo log, MongoDB has its journal and Cassandra has the commit log. The same log is often used for replication and CDC.

## 264: How does replication lag affect app design?

Replicas apply changes a little after the primary, from milliseconds to seconds or more under load. If you read from a replica right after writing, you may not see your own write. Send reads that must be fresh to the primary, track the write's position and wait for the replica to catch up, or keep sticky reads to the primary for a short time after a write. Monitor lag and alert on it.

## 265: What is the difference between synchronous and asynchronous replication?

With synchronous replication, the primary waits for at least one replica to confirm before reporting success, so a primary failure loses no committed data, but writes are slower and can stall if replicas are down. With asynchronous replication, the primary confirms right away and replicas catch up later, which is faster but can lose the last writes on failover. PostgreSQL, MySQL (semi-sync) and MongoDB (`w: 'majority'`) let you choose.

## 266: What is logical replication versus physical replication?

Physical replication copies the exact disk-level changes (PostgreSQL streaming replication), so the replica is a byte-for-byte copy that must run the same major version and holds every table. Logical replication sends row-level changes (insert/update/delete) per table, so you can replicate only some tables, to a different version, or into another system. Logical replication is used for upgrades with little downtime and for CDC.

## 267: How do you upgrade a database's major version with minimal downtime?

For PostgreSQL, use `pg_upgrade` (minutes of downtime) or logical replication to a new-version server and switch over (seconds). Managed services offer blue/green deployments (RDS Blue/Green, Aurora) that do the replication for you. MongoDB upgrades replica sets one member at a time. Always test the upgrade on a copy first and check driver and ORM compatibility.

## 268: What is a covering index?

A covering index contains all the columns a query needs, so the database answers from the index alone without reading the table. In PostgreSQL you add extra columns with `INCLUDE`; MySQL InnoDB secondary indexes already include the primary key. MongoDB calls them covered queries. DynamoDB GSIs do the same with projected attributes.

```sql
CREATE INDEX orders_user_created ON orders (user_id, created_at DESC) INCLUDE (total, status);
```

## 269: How does InnoDB's clustered index affect performance?

In InnoDB, the table itself is stored as a B-tree ordered by the primary key. Lookups by primary key are very fast and range scans by it read contiguous pages. Secondary indexes store the primary key, so a large primary key makes every index bigger, and random primary keys (UUIDv4) cause page splits and fragmentation. Use a short, increasing key like `BIGINT AUTO_INCREMENT` or UUIDv7.

## 270: What is VACUUM in PostgreSQL and why do other databases not need it?

PostgreSQL keeps old row versions in the table itself after updates and deletes (for MVCC). `VACUUM`, usually run by autovacuum, marks that space as reusable and prevents transaction ID wraparound. MySQL InnoDB keeps old versions in a separate undo log that is purged in the background, and MongoDB's WiredTiger handles it inside the engine, so they don't need a user-visible vacuum. Tuning autovacuum is a common PostgreSQL task on busy tables.

## 271: How do you handle large text and blobs across databases?

PostgreSQL moves large values to a side table automatically (TOAST), so big `text` and `jsonb` values work but are slower to update. MySQL stores large `TEXT`/`BLOB` values off-page. MongoDB caps documents at 16 MB and offers GridFS for bigger files. DynamoDB caps items at 400 KB. In all cases, store files in object storage and keep only references in the database.

## 272: How do analytics queries affect an OLTP database?

Big reporting queries read lots of data, use CPU and memory, push hot data out of the cache and can hold back cleanup (like vacuum) while they run. App queries get slower. Fixes: run reports on a read replica, schedule them off-peak, use materialized views, or copy data to a warehouse or ClickHouse for analytics.

## 273: What is ETL versus ELT?

ETL (extract, transform, load) cleans and reshapes data before loading it into the warehouse. ELT (extract, load, transform) loads raw data first and transforms it inside the warehouse with SQL, often using dbt. ELT became common because cloud warehouses are powerful and cheap to scale. Tools like Fivetran, Airbyte and Debezium handle the extract and load part.

## 274: What is Parquet and why do analytics databases like it?

Parquet is an open columnar file format. It stores data by column with compression and statistics (min/max per chunk), so engines read only the columns and row groups they need. DuckDB, Spark, Trino, Athena, BigQuery, Snowflake and ClickHouse can all read it. It's the standard format for data lakes and Iceberg or Delta tables.

## 275: How do you pick between Snowflake, BigQuery, Redshift and Databricks?

Snowflake: easy to use on any cloud, good isolation between workloads with separate warehouses. BigQuery: fully serverless on Google Cloud, great for large scans and per-query pricing. Redshift: AWS-native, fits teams deep in AWS. Databricks: lakehouse built on Spark and Delta Lake, strong for data engineering and machine learning. Your cloud, team skills and pricing model usually decide.

## 276: Why is SELECT star expensive in columnar databases?

A columnar database stores each column separately. `SELECT *` forces it to read and decompress every column, removing the main benefit of column storage. In BigQuery you also pay for every byte scanned, so `SELECT *` on a wide table can cost a lot. Always select only the columns you need and filter on partition columns.

## 277: How do you handle updates and deletes in ClickHouse?

ClickHouse is built for appends. `ALTER TABLE ... UPDATE/DELETE` mutations rewrite whole data parts and are heavy. Lightweight `DELETE` marks rows as deleted, and newer versions also add lightweight updates. For changing data, the usual approach is special engines: `ReplacingMergeTree` keeps the latest version per key after merges, and `CollapsingMergeTree` cancels rows. Use `FINAL` or aggregation in queries to get correct current values.

## 278: What is a star schema?

A star schema is a classic warehouse design: a central fact table holds events or measurements (sales, clicks) with foreign keys to dimension tables (date, customer, product, store). Queries join the fact table to dimensions and aggregate. It's easy for BI tools and analysts. Columnar stores sometimes flatten it into one wide table for speed.

## 279: How do you choose a database for a real-time dashboard?

If data is small, a PostgreSQL read replica with materialized views may be enough. For large event volumes and fast queries under many users, use ClickHouse, Apache Pinot, Apache Druid or StarRocks, which are built for low-latency analytics. Warehouses like Snowflake or BigQuery are better for internal BI where a few seconds per query is fine.

## 280: How do you query JSON data in different databases?

```sql
-- PostgreSQL
SELECT id FROM events WHERE payload->>'type' = 'signup' AND (payload->'meta'->>'plan') = 'pro';

-- MySQL
SELECT id FROM events WHERE payload->>'$.type' = 'signup';
```

```js
// MongoDB
await db
  .collection("events")
  .find({ type: "signup", "meta.plan": "pro" })
  .toArray();
```

PostgreSQL also supports SQL/JSON path queries and GIN indexes on `jsonb`; MySQL indexes JSON through generated columns or functional indexes.

## 281: How do generated columns help with JSON in SQL databases?

A generated column computes its value from other columns, such as a field extracted from a JSON column. You can index it like a normal column and query it fast. This gives you document flexibility with relational speed for the fields you filter on most.

```sql
ALTER TABLE events
  ADD COLUMN event_type text GENERATED ALWAYS AS (payload->>'type') STORED;
CREATE INDEX ON events (event_type);
```

## 282: What does it cost to add a new database to your stack?

Beyond the bill: monitoring and alerts, backups and restore tests, security patches and upgrades, access control, client libraries, local dev setup, CI containers, data sync code with failure handling, and people who know how to debug it at 3 a.m. That is why "one more database" should solve a real problem the existing one can't.

## 283: How do you design for multi-region with different databases?

- Single primary with cross-region read replicas (RDS, Aurora Global Database): simple, fast local reads, writes go to one region.
- Multi-primary with conflict resolution (DynamoDB global tables, Cassandra, Cosmos DB): local writes everywhere, eventual consistency, last-writer-wins.
- Distributed SQL with consensus (Spanner, CockroachDB, YugabyteDB): strong consistency across regions, higher write latency.

Choose based on whether you need local writes and how much consistency matters.

## 284: What is last-writer-wins conflict resolution?

When two copies of the same data are updated at the same time in different places, last-writer-wins keeps the one with the latest timestamp and drops the other. Cassandra and DynamoDB global tables use it. It's simple but silently loses updates, and clock skew can pick the "wrong" winner. For data where every update matters, use conditional writes, single-region ownership or CRDTs.

## 285: How do different databases handle unique constraints?

Relational databases enforce `UNIQUE` on any column. MongoDB supports unique indexes, but on sharded collections only if the index includes the shard key. DynamoDB only guarantees uniqueness of the primary key; for a unique email you write a separate item with `PK = EMAIL#x` in the same transaction using `attribute_not_exists`. Cassandra needs lightweight transactions (`IF NOT EXISTS`).

## 286: What is the N+1 query problem and does it apply to NoSQL?

N+1 happens when you load a list (1 query) and then load related data for each item (N more queries). It's classic with ORMs in SQL, fixed with joins or eager loading. It happens in NoSQL too: fetching 50 orders then 50 separate user documents. Fix it with batch reads (`$in`, `BatchGetItem`, `MGET`), embedding or denormalizing, or a DataLoader in GraphQL.

## 287: How does connection handling differ between SQL databases and HTTP-based databases?

PostgreSQL and MySQL use long-lived TCP connections with session state, so you need pools and connection limits matter. DynamoDB, Firestore, Elasticsearch and most cloud data APIs use HTTP requests, so there's no session to hold, and serverless functions scale without exhausting connections, though you pay per request. Some providers (Neon, PlanetScale, Turso) offer HTTP drivers for SQL to bridge this.

## 288: How would you store user sessions?

Redis or Valkey is the usual choice: fast, with TTLs that expire sessions automatically. DynamoDB with TTL works well in serverless AWS setups. A SQL table works for small apps but adds write load on every request if you update "last seen". Stateless JWTs avoid storing sessions but make logout and revocation harder.

## 289: How would you store a social feed?

Two common designs: fan-out on write, where each new post is pushed into every follower's feed list (Redis lists or Cassandra rows), so reads are cheap; or fan-out on read, where you build the feed when requested by merging posts from followed users. Large systems mix both: fan-out on write for normal users, fan-out on read for celebrities with millions of followers.

## 290: How would you store a product catalog with very different product types?

Options: a relational `products` table with common columns plus a `jsonb` column for type-specific attributes; a document database where each product has its own fields; or the older entity-attribute-value (EAV) pattern, which is flexible but painful to query. The `jsonb` approach usually gives the best balance. Add a search engine for filtering and faceted search at scale.

## 291: What is the entity-attribute-value (EAV) pattern and why is it discouraged?

EAV stores data as rows of `(entity_id, attribute, value)` instead of columns, so you can add attributes without schema changes. But simple questions need many self-joins, values lose their types, constraints are hard and queries are slow. Today `jsonb` columns or document databases handle flexible attributes better. EAV still shows up in older systems like Magento.

## 292: How would you store and query audit logs?

Write audit events append-only with who, what, when and before/after values. A partitioned PostgreSQL table by month works for moderate volume and lets you drop old partitions. For large volume use ClickHouse, Elasticsearch or a log platform. For tamper evidence, add hash chaining or ship logs to write-once storage like S3 Object Lock. Don't let audit writes slow down the main transaction path.

## 293: What is event sourcing and what database fits it?

Event sourcing stores every change as an event (`OrderPlaced`, `ItemAdded`) instead of only the current state. The current state is rebuilt by replaying events, often kept in read models. The event store needs append-only writes, ordering per stream and optimistic concurrency. EventStoreDB is built for it, and PostgreSQL with a `(stream_id, version)` unique index is a common simple choice. Kafka is often used to distribute events but is a weak event store by itself.

## 294: What is CQRS and how does it relate to using multiple databases?

CQRS (Command Query Responsibility Segregation) separates the write model from the read model. Writes go to one store shaped for business rules (often relational or an event store), and changes are copied to read stores shaped for queries (Elasticsearch, Redis, a denormalized table). It allows each side to scale and be designed on its own, at the cost of eventual consistency and more moving parts.

## 295: How do database costs differ between pricing models?

- Instance-based (RDS, self-hosted): pay for servers 24/7, cheap at steady load, wasteful when idle.
- Request-based (DynamoDB on-demand, Firestore): pay per read and write, great at low or spiky traffic, expensive at high steady traffic.
- Scan-based (BigQuery on-demand, Athena): pay per byte scanned, so table design and column selection directly affect cost.
- Compute-time based (Snowflake, Neon, Aurora Serverless): pay for time compute is running.

Model your expected traffic before choosing.

## 296: How do you estimate whether data will fit on one database server?

Estimate rows per day times average row size (plus about 2-3x for indexes and overhead), project for 2-3 years, and compare with practical disk and RAM sizes. A single modern PostgreSQL or MySQL server handles several TB and tens of thousands of simple queries per second. The working set (hot data and indexes) should fit in RAM for good performance. Many apps never outgrow one well-tuned server.

## 297: How do you handle full-text search in MongoDB?

Self-hosted MongoDB has a basic `$text` index with stemming but limited relevance. MongoDB Atlas Search (built on Lucene) gives proper full-text features: fuzzy matching, autocomplete, facets, highlighting and scoring, used through the `$search` aggregation stage. MongoDB has been bringing search and vector search to self-managed Community and Enterprise editions too.

## 298: How do NoSQL databases handle aggregations and reports?

Poorly compared to SQL and columnar stores. MongoDB's aggregation pipeline is good for moderate data. DynamoDB has no aggregates, so you keep running totals with atomic counters or stream changes to another system. Cassandra supports only basic aggregates within a partition. For real reporting, copy data to a warehouse or ClickHouse.

## 299: How do you index arrays in different databases?

MongoDB creates multikey indexes automatically when you index an array field, so `{ tags: 'red' }` uses the index. PostgreSQL uses GIN indexes on array or `jsonb` columns with operators like `@>`. Elasticsearch indexes each array value as if the field had multiple values. DynamoDB can't index inside lists; you write separate items per value or use a GSI on a flattened attribute.

## 300: How do you compare databases fairly in a benchmark?

Use your real data shapes, query mix and concurrency, not vendor benchmarks. Run on similar hardware, warm up caches, measure p95 and p99 latency (not just averages) and throughput together, and test while background tasks like compaction or vacuum run. Include failure tests like killing a node. Tools: pgbench, sysbench, YCSB (for key-value and NoSQL), k6 against your API.

# Advanced Questions (301-450)

## 301: How does a B-tree index work inside a database?

A B-tree (really a B+tree in most engines) is a balanced tree of fixed-size pages, usually 8 KB in PostgreSQL and 16 KB in InnoDB. Inner pages hold keys and pointers to child pages; leaf pages hold keys and row pointers (or the rows, in a clustered index) and link to their neighbors for range scans. Because each page holds hundreds of keys, a table with a billion rows needs only 3 or 4 levels. When a page fills up it splits in two, which is why random inserts cause more splits and fragmentation than ordered inserts.

## 302: How does a read work in an LSM-tree database?

The engine checks the in-memory memtable first, then the SSTable files on disk from newest to oldest, stopping when it finds the key (or a tombstone). To avoid opening every file, each SSTable has a bloom filter that says "definitely not here" or "maybe here", and a sparse index to jump to the right block. Range reads must merge results from all overlapping files. Compaction keeps the number of files low so reads stay fast.

## 303: What is a bloom filter and why do databases use it?

A bloom filter is a small bit array plus several hash functions that answers "is this key in the set?" with either "definitely no" or "probably yes". It never gives false negatives, and the false positive rate depends on its size (about 10 bits per key gives roughly 1%). Cassandra, RocksDB and HBase keep one per SSTable so a read can skip files that don't hold the key, which saves disk reads for missing keys.

## 304: What are the main compaction strategies in LSM databases?

- Size-tiered: merges files of similar size. Cheap on writes, but a key can live in many files, so reads and temporary disk space suffer.
- Leveled: keeps levels where files don't overlap, so a read checks about one file per level. Better reads and space, but more write amplification.
- Time-window: groups data by time, great for time-series with TTL since whole old files can be dropped.

Cassandra 5.0 added the Unified Compaction Strategy, which can behave like either tiered or leveled depending on settings. RocksDB defaults to leveled.

## 305: What are read, write and space amplification?

Read amplification is how many disk reads one logical read needs. Write amplification is how many bytes are written to disk per byte of user data (logs, compaction, page rewrites). Space amplification is how much more disk is used than the live data size. Storage engines trade these against each other: B-trees favor low read amplification, LSM trees favor low write cost but pay with compaction, and you can only optimize two of the three well.

## 306: How does MVCC differ between PostgreSQL, MySQL InnoDB and MongoDB?

All three let readers see a snapshot without blocking writers, but store versions differently. PostgreSQL writes a whole new row version in the table and marks the old one dead, so `VACUUM` must clean up and indexes may need new entries. InnoDB updates the row in place and keeps the previous version in an undo log, which readers follow back as needed and a purge thread cleans. MongoDB's WiredTiger keeps update chains in memory in its cache and writes the latest version to disk at checkpoints, so long-running snapshots put pressure on cache memory.

## 307: What are HOT updates in PostgreSQL?

A heap-only tuple (HOT) update happens when an update doesn't change any indexed column and the new row version fits on the same page. Then PostgreSQL doesn't add new index entries; the old version just points to the new one in the page. This cuts write amplification a lot. To get more HOT updates, avoid indexing columns that change often and lower the table's `fillfactor` to leave free space in pages.

## 308: What is transaction ID wraparound in PostgreSQL?

PostgreSQL transaction IDs are 32-bit, so they wrap around after about 4 billion transactions. To keep old rows visible, `VACUUM` must "freeze" them before that happens. If autovacuum falls too far behind, PostgreSQL warns and eventually stops accepting writes to protect data. Busy write-heavy databases must monitor `age(datfrozenxid)` and make sure autovacuum keeps up. Long-running transactions and stuck replication slots can block freezing.

## 309: What is write skew?

Write skew is an anomaly where two transactions read the same data, each makes a decision based on it, and they write to different rows, so neither sees a conflict, yet together they break a rule. Classic example: two doctors on call each check "at least one other doctor is on call" and both go off call at the same time, leaving nobody. Snapshot isolation (PostgreSQL Repeatable Read, Oracle Serializable) allows it. Serializable isolation or explicit locks (`SELECT ... FOR UPDATE` on the rows you check) prevent it.

## 310: What is a phantom read?

A phantom read happens when a transaction runs the same range query twice and the second time sees new rows inserted by another committed transaction. Locking a range is harder than locking rows that exist. MySQL InnoDB uses next-key (gap) locks to block inserts into scanned ranges for locking reads. PostgreSQL's snapshot keeps plain reads stable, and its Serializable level detects conflicts that phantoms would cause.

## 311: What is a lost update and how do databases prevent it?

A lost update happens when two transactions read the same value, both change it in code and both write it back, so one change is overwritten. Fixes: atomic updates in the database (`SET n = n + 1`, `$inc`, `INCR`, DynamoDB `ADD`), locking reads (`SELECT ... FOR UPDATE`), optimistic checks with a version column or compare-and-set, or a stricter isolation level. PostgreSQL Repeatable Read detects it and aborts one transaction; MySQL Repeatable Read does not for plain reads.

## 312: How does snapshot isolation differ from serializable?

Snapshot isolation gives each transaction a consistent snapshot as of its start and only blocks two transactions from writing the same row. It prevents dirty reads, non-repeatable reads and lost updates, but still allows write skew. Serializable guarantees the outcome matches some one-at-a-time order, which also prevents write skew. Many databases call snapshot isolation "repeatable read" or even "serializable" (older Oracle), so check what each actually guarantees.

## 313: How does PostgreSQL implement Serializable isolation?

PostgreSQL uses Serializable Snapshot Isolation (SSI). Transactions run on snapshots as usual, but the database tracks read-write dependencies between concurrent transactions using lightweight predicate locks. If it detects a pattern that could produce a non-serializable result (a "dangerous structure"), it aborts one transaction with a serialization failure (SQLSTATE `40001`). Apps must retry those transactions. It avoids the blocking of classic two-phase locking.

## 314: What are gap locks and next-key locks in MySQL?

In InnoDB at Repeatable Read, locking reads and writes lock not only the matching index records but also the gaps between them, so other transactions can't insert into that range. A next-key lock is a record lock plus the gap before it. This prevents phantoms but can surprise people with deadlocks and blocked inserts, especially with range conditions or non-unique indexes. Read Committed turns most gap locking off.

## 315: How do databases detect and handle deadlocks?

A deadlock is when transaction A waits for a lock held by B while B waits for one held by A. PostgreSQL checks for cycles after `deadlock_timeout` (1 second by default) and aborts one transaction. InnoDB detects them right away by default and rolls back the smaller transaction. Distributed databases often use timeouts or wound-wait schemes instead of global cycle detection. Apps should retry on deadlock errors and lock rows in a consistent order.

## 316: What is two-phase locking (2PL)?

In 2PL, a transaction acquires locks as it reads and writes (shared locks for reads, exclusive for writes) and only releases them all at commit. This guarantees serializability, but readers block writers and writers block readers, so throughput drops under contention and deadlocks happen. SQL Server's default locking mode and MySQL's Serializable level work this way. MVCC databases mostly avoid it for reads.

## 317: How does the Raft consensus algorithm work?

Raft keeps a replicated log consistent across a group of nodes. One node is elected leader by majority vote for a term. The leader appends client commands to its log and sends them to followers; an entry is committed once a majority has stored it. If the leader dies, followers time out and elect a new leader, and only nodes with up-to-date logs can win. etcd, CockroachDB, TiKV, YugabyteDB, Consul and MongoDB's replication protocol use Raft or a close variant.

## 318: How does Paxos compare to Raft?

Both solve consensus with majorities and survive the failure of a minority of nodes. Paxos came first and is famously hard to understand and implement, especially Multi-Paxos for a log. Raft was designed to be easier to understand, with a strong leader and clear rules for elections and log matching. Spanner uses Paxos; Cassandra uses Paxos for lightweight transactions. In practice they offer similar guarantees and performance.

## 319: What are the differences between single-leader, multi-leader and leaderless replication?

- Single-leader: all writes go to one node, which sends changes to followers. Simple and consistent, but the leader is a bottleneck and failover needs care (PostgreSQL, MySQL, MongoDB).
- Multi-leader: several nodes accept writes and sync with each other, used across regions. Faster local writes but you must resolve conflicts (MySQL Group Replication multi-primary, CouchDB, some global tables).
- Leaderless: clients write to several replicas directly and use quorums (Cassandra, ScyllaDB, Riak, the original Dynamo). Highly available, but conflicts and stale reads need repair mechanisms.

## 320: What is a sloppy quorum and hinted handoff?

In a leaderless system, if some of a key's home replicas are down, a sloppy quorum lets the write land on other healthy nodes so it still succeeds. Those nodes keep a "hint" and hand the data back to the real replicas when they recover (hinted handoff). It increases write availability, but a quorum read might not see the write until handoff finishes, so R + W > N no longer guarantees fresh reads.

## 321: How do read repair and anti-entropy keep replicas in sync?

Read repair: when a read contacts several replicas and finds different versions, the coordinator sends the newest one to the stale replicas. It only fixes data that is read. Anti-entropy repair runs in the background and compares replicas, often using Merkle trees (hash trees over key ranges), so only differing ranges are streamed. Cassandra requires running repair regularly (at least within `gc_grace_seconds`) or deleted data can come back.

## 322: What are vector clocks?

A vector clock is a list of counters, one per node, attached to each version of a value. Comparing two vector clocks tells you whether one version happened before the other or whether they were concurrent (a real conflict). The original Dynamo and Riak used them to keep conflicting versions as "siblings" for the app to merge. Cassandra chose simpler last-writer-wins timestamps instead.

## 323: What are CRDTs and where are they used?

CRDTs (conflict-free replicated data types) are data structures designed so that concurrent updates on different replicas always merge to the same result, without coordination. Examples: grow-only counters, PN-counters, observed-remove sets and sequence types for collaborative text. Redis Enterprise uses them for active-active geo replication, Riak had them, and local-first libraries like Automerge and Yjs use them for offline and collaborative apps.

## 324: What is the difference between linearizability and serializability?

Linearizability is about single objects: once a write completes, every later read (in real time) sees it, as if there were one copy. Serializability is about transactions over many objects: the result equals some serial order, but that order doesn't have to match real time. Strict serializability (Spanner, CockroachDB's goal for single keys, FoundationDB) gives both. Many systems give one without the other.

## 325: What is the PACELC theorem?

PACELC extends CAP: if there is a Partition, choose Availability or Consistency; Else, when the system runs normally, choose Latency or Consistency. It points out that even without failures, strong consistency costs latency because replicas must coordinate. DynamoDB and Cassandra (default settings) are PA/EL; Spanner and CockroachDB are PC/EC; MongoDB with majority concerns leans PC/EC.

## 326: How does Google Spanner use TrueTime?

TrueTime is an API backed by GPS receivers and atomic clocks in Google's data centers. It returns time as an interval `[earliest, latest]` with a small, known uncertainty (a few milliseconds). When committing, Spanner picks a timestamp and then waits out the uncertainty ("commit wait") before making the result visible, so any later transaction anywhere gets a higher timestamp. That gives external consistency (strict serializability) globally, with lock-free snapshot reads at any timestamp.

## 327: How do databases without atomic clocks order transactions, like CockroachDB?

CockroachDB uses hybrid logical clocks (HLC): a mix of physical time and a logical counter, which stays close to wall time but always moves forward and carries causality between nodes. Nodes must keep clock offset under a configured maximum (500 ms by default); a node that drifts too far shuts itself down. When a read finds a value with a timestamp inside its uncertainty window, the transaction restarts at a later timestamp. This gives serializability, though not full strict serializability across unrelated keys.

## 328: What is two-phase commit (2PC)?

2PC makes a transaction atomic across several databases or shards. A coordinator asks every participant to prepare (persist the changes and promise to commit); if all say yes, it sends commit, otherwise abort. Its weakness: if the coordinator dies after prepare, participants hold locks and wait, blocked until it recovers. Distributed SQL databases run 2PC on top of Raft groups so the coordinator state itself is replicated. XA transactions are 2PC across different products, which few teams use today.

## 329: How does TiDB implement distributed transactions?

TiDB stores data in TiKV, a distributed key-value store replicated with Raft, and uses a model based on Google's Percolator. A central Placement Driver hands out timestamps. A transaction writes locks and data with a start timestamp, picks one key as the primary lock, then commits the primary with a commit timestamp; secondary locks are resolved asynchronously by checking the primary. Later versions added async commit and one-phase commit to cut latency.

## 330: What is the saga pattern?

A saga splits a long business transaction across services or databases into local transactions, each with a compensating action to undo it. For a trip booking: reserve flight, reserve hotel, charge card; if charging fails, cancel the hotel and flight. Sagas avoid distributed locks and 2PC but give no isolation, so other users can see half-finished states. They can be choreographed with events or orchestrated by a workflow engine like Temporal.

## 331: What is split brain and how do databases prevent it?

Split brain happens when a network partition makes two nodes each think they are the primary, so both accept writes and the data diverges. Prevention: require a majority (quorum) to elect a leader, so only one side of the split can have one; use leases that expire; and use fencing tokens so storage rejects writes from an old leader. Odd node counts (3 or 5) or a tie-breaking witness node help guarantee a majority exists.

## 332: What are fencing tokens?

A fencing token is a number that increases each time a lock or leadership is granted. Every write to the protected resource includes the token, and the resource rejects tokens lower than the highest it has seen. This stops a process that paused (GC, network delay) and lost its lock without knowing from corrupting data. Raft terms and etcd revision numbers can be used as fencing tokens.

## 333: Is Redis safe for distributed locks?

A single Redis `SET key value NX PX 30000` is fine for efficiency locks, where a rare double execution just wastes work. For correctness locks, it's risky: async replication can lose the lock on failover, and a client that pauses can keep working after the lock expired. Redlock (locks on several independent Redis nodes) was proposed for this but is debated because it depends on timing assumptions. For correctness, use a consensus store (etcd, ZooKeeper) with fencing tokens, or a database row lock.

## 334: How does Aurora's storage layer work?

Aurora sends only redo log records over the network, not full pages. Storage is split into 10 GB segments, each copied six times across three availability zones. A write is durable when 4 of 6 copies acknowledge it, and reads need 3 of 6, so it survives losing a whole zone plus one more copy for reads. The storage nodes apply log records to build pages themselves ("the log is the database"), which removes checkpoint and full-page write overhead from the database instance.

## 335: What does separating storage and compute give a database?

When data lives in shared durable storage (object storage or a distributed storage service) and compute nodes are stateless, you can scale compute up, down or to zero independently, start new replicas fast without copying data, and create instant branches or clones. Snowflake, BigQuery, Aurora, Neon, AlloyDB and many new systems work this way. The cost is extra network latency to storage, usually hidden with local caches.

## 336: How does Neon split PostgreSQL into storage and compute?

Neon runs normal PostgreSQL as stateless compute. WAL is sent to "safekeepers", a group that uses Paxos to store it durably. "Pageservers" read the WAL, rebuild pages on request at any point in time and push older data to object storage. Because history is kept as WAL plus image layers, branching is just pointing a new compute at an earlier point, and compute can scale to zero since it holds no data.

## 337: How do columnar databases compress data so well?

Values in one column have the same type and often repeat or change slowly, so they compress far better than mixed rows. Common methods:

- Dictionary encoding: replace repeated strings with small integer codes.
- Run-length encoding: store "value x repeated 5,000 times".
- Delta and delta-of-delta: store differences between sorted numbers or timestamps.
- Bit packing: use only as many bits as the largest value needs.
- General codecs (LZ4, ZSTD) on top.

Compression ratios of 5x to 20x are common, and less data read means faster queries.

## 338: What is vectorized query execution?

Instead of processing one row at a time through each operator (the classic "Volcano" model), a vectorized engine processes batches of values from a column, often thousands at once, in tight loops. This uses CPU caches well, cuts function call overhead and lets the compiler use SIMD instructions. ClickHouse, DuckDB, Snowflake and Velox-based engines use it, which is a big part of why they scan so fast.

## 339: What is late materialization?

In a columnar engine, late materialization means it first evaluates filters on just the needed columns, producing a list of matching row positions, and only then reads other columns for those rows. If a filter keeps 1% of rows, the other columns are read for 1% of rows only. ClickHouse's `PREWHERE` is an example: it reads filter columns first, then the rest.

## 340: How does ClickHouse's MergeTree storage and sparse primary index work?

Each insert creates an immutable "part" of data sorted by the table's `ORDER BY` key, with each column in its own file. Parts are merged in the background, like an LSM tree. The primary index is sparse: it stores one entry per granule (8,192 rows by default), not per row, so it fits in memory even for billions of rows. A query uses it to skip granules whose key ranges can't match, then scans the remaining granules. Choosing `ORDER BY` columns that match common filters is the most important tuning decision.

## 341: What are data skipping indexes in ClickHouse and zone maps in general?

A zone map stores small summaries per block of data, like min and max values, so the engine can skip blocks that can't match a filter. ClickHouse's skipping indexes extend this with `minmax`, `set` (small sets of distinct values) and bloom filter types per group of granules. Parquet row groups, Snowflake micro-partitions and BRIN indexes in PostgreSQL use the same idea. They only help when the data is somewhat clustered by the filtered column.

## 342: How do time-series databases compress timestamps and values?

Facebook's Gorilla paper introduced the methods many TSDBs use. Timestamps arrive at regular intervals, so storing delta-of-delta (often zero) needs only a bit or two per point. Floating point values change slowly, so XOR-ing each value with the previous one leaves mostly zero bits that are cheap to store. Prometheus, InfluxDB and others use variants of these and get close to 1-2 bytes per data point.

## 343: What is the high-cardinality problem in time-series databases?

Each unique combination of a metric name and its labels (tags) is a separate series. If you add labels like `user_id` or `request_id`, the number of series explodes into millions. Indexes and memory grow with series count, ingest slows and queries struggle. Keep high-cardinality values out of labels (put them in logs or traces), or use engines built for it, like ClickHouse or columnar TSDBs that don't keep a per-series index in memory.

## 344: How does the HNSW vector index work?

HNSW (Hierarchical Navigable Small World) builds a graph where each vector links to some of its nearest neighbors, in several layers. Upper layers are sparse with long links, lower layers are dense. A search starts at the top, greedily moves toward the query, then drops down a layer and repeats, until it reaches the bottom layer and collects the best candidates. It gives high recall and low latency but uses a lot of memory and is slower to build than other indexes.

## 345: What are IVF and product quantization in vector search?

IVF (inverted file) clusters vectors around centroids with k-means, and at query time searches only the closest few clusters (the `nprobe` or `lists`/`probes` setting). Product quantization (PQ) splits each vector into chunks and replaces each chunk with a short code, shrinking memory by 10x or more at some loss of accuracy. IVF-PQ combines both for billion-scale search. pgvector's IVFFlat is IVF without quantization.

## 346: How do you tune the recall versus speed trade-off in vector search?

Approximate indexes don't always return the true nearest neighbors. Settings trade recall for speed: in HNSW, `m` (links per node) and `ef_construction` affect build quality, and `ef_search` (`hnsw.ef_search` in pgvector, 40 by default) sets how many candidates a query explores. In IVF, more probes means better recall and slower queries. Measure recall against exact search on a sample of your real queries before picking values.

## 347: What is DiskANN and why does it matter?

DiskANN is a graph-based vector index from Microsoft Research designed to keep most of the index on SSD instead of RAM, using compressed vectors in memory to guide the search and full vectors on disk to refine it. It makes billion-scale vector search affordable on one machine. Variants are used in Azure Cosmos DB, SQL Server, Milvus, and the pgvectorscale extension for PostgreSQL.

## 348: How do Lucene segments work in Elasticsearch?

Lucene writes new documents into small immutable segments. Each segment has its own inverted index, stored fields and doc values. A refresh opens new segments for search; a flush makes them durable (with the translog covering the gap). Deletes and updates only mark old documents as deleted. Background merges combine small segments into bigger ones and drop deleted docs. This is why updates are costly in Elasticsearch and why force-merging read-only indexes helps.

## 349: What is BM25?

BM25 is the default relevance scoring function in Lucene, Elasticsearch, OpenSearch and many other search engines. It scores a document higher when the query terms appear more often in it (with diminishing returns), when the terms are rare across all documents (inverse document frequency), and lower when the document is long. It replaced classic TF-IDF because its term frequency saturation and length normalization give better results.

## 350: Why is deep pagination expensive in Elasticsearch?

A search is query-then-fetch: each shard returns its top `from + size` hits, and the coordinating node merges them. Asking for page 1,000 of 10 makes every shard collect and sort 10,010 hits, and the coordinator handles `shards x 10,010`. That's why `from + size` is capped at 10,000 by default (`index.max_result_window`). Use `search_after` with a point-in-time (PIT) for deep or full traversal.

## 351: What is index-free adjacency in graph databases?

In a native graph database like Neo4j, each node record stores direct pointers to its relationships, and each relationship points to its start and end nodes. Moving from a node to its neighbors is a pointer jump whose cost depends on the number of neighbors, not on the total size of the graph. In a relational database, each hop is an index lookup whose cost grows with table size (log N), which adds up over many hops.

## 352: Why are graph databases hard to shard?

Graph queries follow relationships wherever they lead, and in real graphs (social, fraud) everything is connected to everything within a few hops. Any split of the graph across machines cuts many relationships, so traversals keep crossing the network, which kills the speed advantage. Most graph databases scale reads with replicas and keep the whole graph on one machine, or shard by natural boundaries like tenant. Neo4j's composite databases and some distributed graph engines exist, but cross-shard traversals stay costly.

## 353: Why is Redis mostly single-threaded and how does it still scale?

Redis runs commands on one main thread with an event loop. That avoids locks, makes every command atomic and keeps latency predictable, and since data is in memory the CPU is rarely the bottleneck for simple commands. Since Redis 6, optional I/O threads handle reading and writing sockets in parallel. To scale beyond one core for commands, you run Redis Cluster with many shards. Valkey 8 went further with improved multi-threaded I/O.

## 354: Can Redis lose acknowledged writes?

Yes. Replication is asynchronous, so a write acknowledged by the primary can be lost if the primary fails before replicas receive it and a replica is promoted. AOF with `everysec` can also lose up to a second of writes on a crash. `WAIT numreplicas timeout` makes the client wait until replicas have the write, which reduces but doesn't fully remove the risk, since Redis is not a consensus system. Plan for this when Redis holds anything important.

## 355: How does Redis Cluster route keys and handle resharding?

Each key maps to one of 16,384 hash slots (CRC16 of the key, modulo 16,384), and each primary owns a set of slots. A client sending a command to the wrong node gets a `MOVED` reply with the right node and updates its slot map. During resharding, when a slot is being moved, a node may reply `ASK` for keys already moved, telling the client to try the target node just for that request. Cluster-aware clients like ioredis handle both.

## 356: How does DynamoDB partition data internally?

DynamoDB hashes the partition key to place items on internal partitions, each stored on replicas across three availability zones with a leader handling writes. A partition holds up to about 10 GB and serves up to 3,000 read units and 1,000 write units per second. When data or traffic grows, DynamoDB splits partitions automatically. Adaptive capacity shifts unused throughput to busy partitions and can isolate very hot items on their own partition, but a single key still can't exceed one partition's limits.

## 357: How do DynamoDB Streams and global tables work?

DynamoDB Streams records item changes in order per item for 24 hours, and Lambda or the Kinesis adapter can consume them. Global tables replicate a table across regions, so each region accepts reads and writes. With the default multi-region eventual consistency, conflicting writes to the same item are resolved with last-writer-wins, and replication usually takes about a second. AWS also offers a strong consistency mode for global tables at the cost of higher write latency.

## 358: How do Cassandra nodes find each other and decide where data lives?

Nodes share cluster state with a gossip protocol: every second each node exchanges state with a few others, so membership and health spread through the cluster. The partitioner (Murmur3 by default) hashes partition keys onto a token ring, and each node owns token ranges, usually through virtual nodes. The snitch tells Cassandra which rack and datacenter each node is in, so `NetworkTopologyStrategy` places replicas in different racks and datacenters.

## 359: Why must Cassandra run repairs regularly?

Replicas can miss writes when nodes are down, hints expire or dropped mutations happen. Read repair only fixes data that is read. If a replica misses a delete and the tombstone is purged after `gc_grace_seconds` (10 days by default) on the others, the old value on the stale replica can come back ("zombie data"). So anti-entropy repair must complete on every range within that window. Tools like Cassandra Reaper and incremental repair make this manageable.

## 360: Why are Cassandra lightweight transactions expensive?

A lightweight transaction (`INSERT ... IF NOT EXISTS`, `UPDATE ... IF`) runs a Paxos round among replicas, which needs several round trips (prepare, read, propose, commit) instead of one write. Latency is several times higher and throughput lower, and contention on the same partition makes it worse. Cassandra 4.1 added an improved Paxos v2 that cuts round trips. Use LWTs only for the few operations that need compare-and-set, like unique usernames.

## 361: How does MongoDB's WiredTiger engine manage memory and durability?

WiredTiger keeps a cache (by default about 50% of RAM minus 1 GB) holding uncompressed pages and recent version chains, and relies on the OS file cache for compressed on-disk data. Writes go to the journal (a write-ahead log) and are committed to data files at checkpoints every 60 seconds. If the cache fills with dirty data faster than it can be written out, application threads are pulled into eviction, which shows up as latency spikes. Long transactions and slow secondaries make cache pressure worse.

## 362: What are jumbo chunks in MongoDB?

A jumbo chunk is a chunk that grew beyond the max chunk size but can't be split because all its documents share the same shard key value (or very few values). The balancer can't move it easily, so data stays uneven across shards. It's a sign of a low-cardinality shard key, like `country` or `status`. Fix it by choosing a shard key with more distinct values, often a compound key, and resharding.

## 363: Why are replication slots in PostgreSQL risky?

A replication slot makes the primary keep WAL until the consumer (replica or CDC tool like Debezium) confirms it has read it. If the consumer stops or falls far behind, WAL piles up and can fill the disk, taking the database down. It can also block vacuum from cleaning rows when `hot_standby_feedback` or logical slots hold back the xmin. Set `max_slot_wal_keep_size`, monitor slot lag and drop slots that are no longer used.

## 364: What is logical decoding in PostgreSQL?

Logical decoding turns WAL records into a stream of row-level changes (insert, update, delete with values) using an output plugin like `pgoutput` or `wal2json`. It powers built-in logical replication, Debezium, Supabase Realtime and many sync tools. Updates only include old values for the key columns unless the table has `REPLICA IDENTITY FULL`. DDL changes are not streamed, so schema changes need extra coordination.

## 365: What is the difference between statement-based and row-based binlog replication in MySQL?

Statement-based replication logs the SQL statements, which is compact but can produce different results on replicas when statements are non-deterministic (like `NOW()`, `UUID()` or `LIMIT` without `ORDER BY`). Row-based replication logs the actual changed rows, which is safe and deterministic but larger for bulk updates. Row-based is the default since MySQL 5.7.7 and is needed for CDC tools. Mixed mode switches between them.

## 366: What are GTIDs in MySQL?

A global transaction identifier (GTID) gives every committed transaction a unique id made of the source server's UUID and a sequence number. Replicas track which GTIDs they have applied, so failover and re-pointing replicas don't need manual binlog file and position math. GTIDs also prevent applying the same transaction twice. Modern MySQL setups, Group Replication and most managed services rely on them.

## 367: What is Patroni?

Patroni is a popular open source tool for PostgreSQL high availability. It runs next to each Postgres node and uses a distributed configuration store (etcd, Consul or ZooKeeper) to elect a leader, so only one node can be primary at a time. It handles automatic failover, replica setup and configuration changes. Many Kubernetes operators for Postgres (Zalando's, and Crunchy's in the past) are built on it.

## 368: Why does fsync matter for database durability?

A write to a file usually lands in the OS page cache, not on disk. `fsync` forces it to stable storage. Databases call it on commit (for their log) so a power loss doesn't lose committed data. In 2018 PostgreSQL developers found that on Linux a failed `fsync` could clear the error and drop dirty pages, so retrying looked successful while data was lost; PostgreSQL now panics and recovers from WAL instead. Turning `fsync` off makes benchmarks faster and production data unsafe.

## 369: What is group commit?

Flushing the log to disk on every commit limits throughput to the disk's flush rate. With group commit, the database collects commits from many concurrent transactions and flushes them together in one `fsync`, so the flush cost is shared. PostgreSQL, MySQL and most databases do this. Settings like PostgreSQL's `synchronous_commit = off` go further and don't wait for the flush at all, risking the last few hundred milliseconds of commits on crash, but never corrupting data.

## 370: Why do some databases manage their own cache instead of using the OS page cache?

A database knows its access patterns: which pages are hot, which belong to a big scan, what can be evicted. InnoDB's buffer pool and WiredTiger's cache use direct I/O or manage pages themselves to avoid double caching and to control eviction and write-back. PostgreSQL uses a mix: `shared_buffers` plus the OS cache, which is why it's often set to only about 25% of RAM. PostgreSQL 18 added an asynchronous I/O subsystem (including `io_uring` on Linux) to read data faster.

## 371: Why is using mmap in a database often criticized?

With `mmap`, the OS loads file pages into memory on demand, which looks like free caching. But the database loses control: it can't decide eviction order, page faults block threads unexpectedly, I/O errors show up as signals, and ensuring correct write ordering for crash safety is hard. MongoDB's old MMAPv1 engine was replaced by WiredTiger partly for these reasons. LMDB is a well-known database that uses `mmap` successfully by keeping a simple copy-on-write design.

## 372: How do query optimizers estimate costs and why do they go wrong?

The optimizer estimates how many rows each step returns, using statistics like row counts, distinct values, histograms and most common values per column. It multiplies selectivities assuming columns are independent, which breaks for correlated columns (like `city` and `zip`). Bad estimates lead to wrong join orders or nested loops over millions of rows. Fixes: `ANALYZE` after big changes, extended statistics (`CREATE STATISTICS` in PostgreSQL), higher statistics targets, or rewriting the query.

## 373: What join algorithms do databases use?

- Nested loop: for each row of the outer side, look up matches on the inner side, ideally through an index. Best when the outer side is small.
- Hash join: build a hash table on the smaller side, then probe it with the other side. Best for large unsorted inputs with equality joins.
- Merge join: walk two inputs sorted on the join key together. Best when both are already sorted, such as from indexes.

Columnar and distributed engines mostly use hash joins.

## 374: How do distributed databases perform joins across nodes?

If both tables are partitioned on the join key (co-located), each node joins its own part locally, which is the cheapest case. Otherwise, a small table can be broadcast to every node, or both tables are shuffled (repartitioned) over the network by the join key. Shuffles are expensive, which is why Citus uses "reference tables" and co-location by `tenant_id`, and why picking partition keys that match common joins matters.

## 375: How do secondary indexes work in a sharded database?

Local (document-partitioned) indexes: each shard indexes only its own data. Writes are cheap, but a query by the indexed field must ask every shard (scatter-gather). MongoDB and Elasticsearch work this way. Global (term-partitioned) indexes: the index itself is partitioned by the indexed value, so a query hits one index shard, but a write may touch several shards. DynamoDB GSIs are global and updated asynchronously; distributed SQL databases update global indexes transactionally, which costs latency.

## 376: What are the common approaches to rebalancing data when adding nodes?

- Hash modulo N: simple but moves almost all keys when N changes, so avoided.
- Fixed number of partitions: create many more partitions than nodes (Redis Cluster's 16,384 slots, Elasticsearch shards, Riak) and move whole partitions.
- Dynamic splitting: split ranges when they grow or get hot, merge when they shrink (CockroachDB, TiKV, HBase, DynamoDB, MongoDB chunks).
- Consistent hashing with virtual nodes (Cassandra).

Rebalancing itself uses network and disk, so systems throttle it.

## 377: How does CockroachDB handle hot ranges?

CockroachDB stores data in ranges (512 MB max by default). It splits ranges based on load as well as size, so a range getting many requests can be split by key and the parts moved to different nodes. This doesn't help when all writes go to the very end of the key space, like with timestamps or sequential ids; for that, hash-sharded indexes (`USING HASH`) spread sequential keys over several buckets.

## 378: What are follower reads and bounded staleness?

Follower reads let a replica that isn't the leader serve reads at a slightly older timestamp, which it can prove is safe. This removes a round trip to a leader in another region. CockroachDB offers `AS OF SYSTEM TIME follower_read_timestamp()`, Spanner has stale reads with exact or bounded staleness, and YugabyteDB has similar options. They fit dashboards and listing pages that can tolerate a few seconds of staleness.

## 379: How do you handle data residency requirements in a global database?

Laws like GDPR or local rules may require some users' data to stay in a specific country or region. Options: separate database deployments per region with routing by user home region; distributed SQL with geo-partitioning, where row placement depends on a column like `region` (CockroachDB regional-by-row tables, YugabyteDB tablespaces, Spanner placement); or MongoDB zone sharding. Backups, logs, caches and analytics copies must also respect the rule, which teams often forget.

## 380: Why are clocks dangerous in distributed databases?

Server clocks drift and get adjusted by NTP, sometimes backwards, and a paused VM or process can resume with a stale view of time. Systems that use timestamps for ordering, like last-writer-wins in Cassandra, can silently drop the newer write if clocks are skewed. Leases and lock expiry based on time can let two nodes believe they hold the same lease. Safer designs use logical clocks, HLCs, bounded-uncertainty clocks (TrueTime, AWS Time Sync) or fencing tokens.

## 381: How do you make writes idempotent across databases?

Network errors mean a client often doesn't know if a write succeeded, so it retries. To make retries safe, attach an idempotency key (like a request UUID) and store it with a unique constraint or condition, so a second attempt is detected and returns the first result. In SQL: a unique index on `idempotency_key`. In DynamoDB: `attribute_not_exists` on a key item in a transaction. MongoDB retryable writes do this internally for single operations.

## 382: Can you get exactly-once processing between Kafka and a database?

Delivery itself is at-least-once in practice, so you aim for exactly-once effects. Store the consumer's offset in the same database transaction as the results, so either both commit or neither; or make every write idempotent (upserts keyed by event id). Kafka's transactions give exactly-once only within Kafka (read-process-write to topics); once you write to an outside database, you need one of these patterns.

## 383: What ordering guarantees does CDC give and what can go wrong?

CDC streams from a single database log are ordered per table row (and usually per transaction in commit order). Problems: Kafka partitions keep order only per key, so events must be keyed by primary key; at-least-once delivery means duplicates after failures, so consumers must be idempotent; initial snapshots mixed with live changes need careful handling; and schema changes can break consumers. Large transactions also arrive as big bursts.

## 384: What is the expand and contract pattern for schema changes?

It changes a schema without downtime in steps. Expand: add the new column or table while keeping the old one. Migrate: write to both, backfill old data in batches, then switch reads to the new structure. Contract: once no code uses the old structure, remove it. Each step is deployed separately, so you can roll back the app at any point. It works the same way for renaming fields in document databases.

## 385: How do online schema change tools work?

On large MySQL tables, some `ALTER TABLE` operations copy the whole table and block writes. Tools like gh-ost and pt-online-schema-change create a new table with the new schema, copy rows in small chunks, apply ongoing changes (gh-ost reads the binlog, pt-osc uses triggers), then swap the tables with a quick rename. In PostgreSQL many changes are instant, and `CREATE INDEX CONCURRENTLY` avoids blocking writes; `pg_repack` rebuilds bloated tables online.

## 386: How would you migrate from one database to another with zero downtime?

1. Set up the target and the schema mapping.
2. Start capturing changes from the source (CDC).
3. Bulk copy existing data, then apply captured changes until the target catches up.
4. Run shadow reads: query both, compare results and log differences.
5. Switch reads to the target gradually with a feature flag.
6. Switch writes; keep reverse replication to the old database for a while as a rollback path.
7. Decommission the source once stable.

Tools like AWS DMS, Debezium or custom dual-write with reconciliation can help.

## 387: How do databases encrypt data and what is client-side field level encryption?

Most databases support encryption in transit (TLS) and at rest (disk or tablespace encryption, often with keys in a KMS). Both protect against stolen disks and network sniffing, not against someone who can query the database. Client-side field level encryption encrypts sensitive fields in the app before sending them, so the database only sees ciphertext. MongoDB Queryable Encryption even allows equality and range queries on encrypted fields. In SQL databases you usually encrypt in the app and give up querying those fields, or store a hash for lookups.

## 388: How do you delete personal data for GDPR in append-only or replicated systems?

Deletes in the main database don't remove copies in backups, replicas, caches, search indexes, warehouses, logs and event streams. Approaches: keep a map of every place personal data flows; send deletion events through CDC to all consumers; set limited retention on backups; and use crypto-shredding, where each user's data is encrypted with their own key and deleting the key makes all copies unreadable. Event-sourced systems especially rely on crypto-shredding.

## 389: How are consistent backups taken in a distributed database?

Copying each node at slightly different times gives a backup that never existed as one state. Options: use the database's own distributed backup that reads at a single MVCC timestamp (CockroachDB `BACKUP`, Spanner, TiDB BR); briefly pause balancing and take snapshots in coordination (MongoDB sharded clusters); or accept per-node snapshots plus repair (Cassandra). Managed services usually handle this, but test full restores, including how long they take.

## 390: What are RPO and RTO and how do database choices affect them?

RPO (recovery point objective) is how much data you can afford to lose, measured in time. RTO (recovery time objective) is how long you can be down. Async replicas give an RPO of seconds; synchronous replication or consensus gives near-zero RPO. Automatic failover gives an RTO of seconds to a minute; restoring a large backup can take hours. Multi-region active-active designs push both down at a big cost in complexity.

## 391: What is Jepsen and what has it taught us about databases?

Jepsen is a testing framework and series of reports by Kyle Kingsbury that runs databases under network partitions, clock skew and crashes, then checks if results match the promised consistency. Many databases failed their own claims at some point: lost acknowledged writes, stale reads, broken transactions. Vendors fixed many issues afterward. The lessons: read the actual guarantees, use the safer settings (majority writes, serializable), and don't trust marketing about "strong consistency" without evidence.

## 392: What causes tail latency in distributed databases and how do you reduce it?

A request that touches many nodes waits for the slowest one, so rare slow events (GC pauses, compaction, disk hiccups, noisy neighbors, cross-region hops) show up often at p99. Ways to reduce it: hedged requests (send a second request after a short delay and take the first answer), speculative retry (Cassandra has it), fewer fan-out queries, smaller GC heaps or no GC (ScyllaDB in C++), and isolating background work from foreground traffic.

## 393: What is a thread-per-core architecture?

In a thread-per-core design, each CPU core runs one thread that owns a slice of the data, with its own memory and I/O queues, and cores talk by passing messages instead of sharing locks. ScyllaDB (on the Seastar framework), Redpanda and Dragonfly use it. It removes lock contention and context switches and gives very steady latency, but it's harder to program and a hot shard can overload one core.

## 394: How does HyperLogLog help count distinct values at scale?

HyperLogLog estimates the number of distinct items (like unique visitors) using a tiny fixed memory, around 12 KB in Redis for about 0.81% error, no matter if there are a thousand or a billion items. It hashes each item and tracks the maximum number of leading zeros seen in buckets. Sketches from different days can be merged. Redis (`PFADD`, `PFCOUNT`), ClickHouse (`uniq`), BigQuery (`APPROX_COUNT_DISTINCT`) and Postgres extensions use it.

```js
await redis.pfadd("visitors:2026-11-26", userId);
const unique = await redis.pfcount("visitors:2026-11-26");
```

## 395: What are streaming databases?

Streaming databases like Materialize and RisingWave let you define SQL materialized views over changing data (from Kafka or CDC), and keep the results up to date incrementally as each change arrives, instead of recomputing on query. You get fresh results for joins and aggregates with low latency. They fit real-time dashboards, alerts and feature pipelines that would otherwise need custom stream processing code in Flink or Kafka Streams.

## 396: What is HTAP?

HTAP (hybrid transactional/analytical processing) means one system handles both OLTP and analytics on fresh data, avoiding ETL delays. Usually it keeps a row store for transactions and a columnar copy for analytics, synced automatically. TiDB with TiFlash, SingleStore, AlloyDB's columnar engine and Oracle's in-memory option are examples. Isolating the two workloads so analytics doesn't slow transactions is the hard part.

## 397: How does Apache Iceberg provide table features on top of files?

An Iceberg table is a tree of metadata files: a table metadata file points to snapshots, each snapshot points to manifest lists, which point to manifests listing data files (Parquet) with column stats. A commit writes new files and atomically swaps the pointer to the new metadata file through a catalog. This gives ACID commits, time travel, schema evolution, hidden partitioning and file skipping, and lets many engines (Spark, Trino, Snowflake, DuckDB) share one table.

## 398: Why is S3 becoming the storage layer for many databases?

Object storage is cheap, extremely durable, scales without limit and is shared by any number of compute nodes. With S3 now offering strong read-after-write consistency and conditional writes, systems can build directly on it: warehouses, lakehouses, Neon's history, WarpStream and other Kafka-compatible systems, turbopuffer for vectors, SlateDB as an embedded LSM. The trade-off is higher latency per request, so these systems batch writes and cache hot data locally.

## 399: How do long-running transactions hurt different databases?

In PostgreSQL, a long-open transaction (even an idle one) stops vacuum from removing dead rows across the database, causing bloat and slower queries. In InnoDB, it grows the undo history list, slowing reads that must walk old versions. In MongoDB, it pins old versions in the WiredTiger cache, causing eviction pressure. In any locking system, it holds locks and blocks others. Set `idle_in_transaction_session_timeout` and statement timeouts, and keep transactions short.

## 400: What happens when you delete a large amount of data in different databases?

In PostgreSQL, a big `DELETE` creates many dead rows and WAL, and space is only reused after vacuum; dropping a partition is instant instead. In InnoDB it grows undo logs and can stall replication on replicas. In Cassandra it creates tombstones that slow reads until compaction. In ClickHouse, deletes are mutations that rewrite parts. In Elasticsearch, deleted docs stay in segments until merges. Design for bulk removal with partitions, TTLs or time-based indexes.

## 401: How do index bloat and fragmentation differ between engines?

In PostgreSQL, B-tree indexes collect dead entries from updates and deletes; vacuum removes them but pages may stay half empty, so `REINDEX CONCURRENTLY` is sometimes needed. Version 13 added deduplication, which helps. InnoDB tables and indexes fragment after random inserts and deletes, fixed with `OPTIMIZE TABLE` (an online rebuild). LSM engines don't fragment the same way since files are rewritten by compaction, but they carry obsolete versions until then.

## 402: Why are secondary indexes more expensive in LSM databases?

An LSM write is cheap because it never reads before writing. But maintaining a secondary index means you must know the old indexed value to remove its index entry, which requires a read before every update. Systems handle it differently: Cassandra's legacy secondary indexes are local to each node and hurt at scale, Storage Attached Indexes (SAI, Cassandra 5.0) attach index data to each SSTable, and RocksDB-based SQL engines (MyRocks, CockroachDB, TiDB) pay for reads during writes.

## 403: How does SSD write amplification relate to database design?

SSDs can't overwrite pages in place; they write to fresh pages and garbage-collect erase blocks, so random small writes cause internal write amplification and wear. B-trees rewriting whole pages for small changes, plus full-page writes in PostgreSQL after checkpoints, add more. LSM trees write large sequential files, which suits SSDs better. Tuning checkpoint intervals, using compression, and leaving free SSD space all reduce wear on write-heavy databases.

## 404: How do you avoid noisy neighbors in a multi-tenant database?

One big tenant can use most of the CPU, I/O or connections and slow everyone else. Options: per-tenant rate limits and query timeouts in the app; connection pool limits per tenant; resource groups or workload management (SQL Server Resource Governor, Snowflake warehouses per workload, ClickHouse quotas and settings profiles); moving large tenants to their own shard or database; and monitoring per-tenant usage so you notice it before customers do.

## 405: How do you choose between consistency and availability per feature?

Don't pick one level for the whole system. Payments, inventory reservation, account balances and unique usernames need strong consistency even if it means errors during outages. Feeds, likes, view counts, recommendations and search results can be eventually consistent and should stay available. Many databases let you choose per query (DynamoDB `ConsistentRead`, Cassandra consistency levels, MongoDB read and write concerns), so match the setting to the feature's real cost of being wrong.

## 406: How would you design the database for a URL shortener?

The main access pattern is a key-value lookup: short code to long URL, read extremely often, written rarely. Use a key-value store like DynamoDB or Redis (with persistence), or a PostgreSQL table with the code as primary key, plus a cache in front. Generate codes with a counter encoded in base62 or random codes with a uniqueness check (conditional put). Click analytics go to a separate pipeline (a stream into ClickHouse), not as updates to the main row.

## 407: How would you store and query live locations for a ride-sharing app?

Driver locations update every few seconds and are only valuable for a short time. Keep current positions in memory: Redis `GEOADD` with `GEOSEARCH` by radius, or a geohash or H3 cell key in a key-value store, so "drivers near me" is a cell lookup. Trips, payments and accounts live in a relational database. Location history goes to a time-series or columnar store, or object storage, for analytics.

## 408: How would you design the database for a banking ledger?

Use a relational database with serializable transactions (or a ledger-focused database like TigerBeetle). Use double-entry bookkeeping: every transfer writes balanced debit and credit entries in an append-only entries table, and never updates or deletes entries. Balances are derived, or kept in a balance row updated in the same transaction with row locks or conditional checks so they can't go negative. Add idempotency keys for every request, money as integer minor units, and strict audit logs.

## 409: How would you handle inventory during a flash sale?

Thousands of users try to buy the same few items at once, so one stock row becomes a hot spot. Options: an atomic conditional decrement (`UPDATE stock SET qty = qty - 1 WHERE id = $1 AND qty > 0`, or a DynamoDB condition expression); pre-loading stock into Redis and decrementing there with a Lua script, then writing orders to the database through a queue; or splitting stock into several buckets to spread contention. Always include reservation expiry for unpaid orders.

## 410: How would you store 1 billion product analytics events per day?

Don't write them to the OLTP database. Send events to Kafka or Kinesis, then batch-insert them into ClickHouse (or BigQuery, Snowflake, Druid, Pinot), ordered by `(tenant_id, event_type, timestamp)`. Partition by day for easy retention, use materialized views for rollups like daily active users, and keep raw data in object storage as Parquet for reprocessing. About 12,000 events per second average is fine for a small ClickHouse cluster if inserts are batched.

## 411: How would you design databases for a global SaaS with strict data residency?

Deploy a "cell" per region: app servers plus a regional database (PostgreSQL or a regional cluster) that holds only that region's tenants. A small global directory service maps each tenant to its home region and handles routing and login. Global data like billing plans can be replicated everywhere. If you need cross-region transactions on the same tables, distributed SQL with regional-by-row placement is an alternative but adds complexity.

## 412: How would you store messages for a chat system with hundreds of millions of users?

Messages are written constantly and read by conversation, newest first. A wide-column store fits: Cassandra or ScyllaDB with `(conversation_id, time_bucket)` as the partition key and a time-ordered message id as the clustering key. Use Snowflake-style ids for ordering, Redis or a pub/sub layer for online delivery and presence, and a separate store for user and group metadata. Discord publicly moved its messages from Cassandra to ScyllaDB at this kind of scale.

## 413: How would you choose databases for a recommendation engine?

Offline, user behavior events go into a warehouse or lakehouse where models are trained. Online, you need fast lookups: precomputed recommendations per user in a key-value store (Redis, DynamoDB), item embeddings in a vector database for "similar items", and sometimes a graph database for "people who bought this also bought". A feature store (often Redis or DynamoDB-backed) serves model features at request time.

## 414: How would you use databases for fraud detection?

Real-time checks need fast lookups of recent activity: counters and sliding windows in Redis (transactions per card per minute), a feature store, and rules or models scoring each event within milliseconds. Fraud rings show up as shared devices, cards, addresses and IPs, which a graph database finds by traversing a few hops. Historical events go to a columnar store for training models and investigations.

## 415: How would you design storage for a RAG system over company documents?

Store source files in object storage, document metadata and access rights in PostgreSQL, and chunk embeddings in a vector index (pgvector, or Qdrant, Pinecone, Weaviate at larger scale). Each chunk keeps its document id, tenant and permissions so search can filter by what the user may see. Hybrid search (BM25 plus vectors) improves results for names and codes. Re-embed when the embedding model changes, so keep the model version with each vector.

## 416: How would you build a global real-time leaderboard with millions of players?

A Redis sorted set handles millions of members with fast updates and rank queries. For very large or sharded setups, split by region or score range and merge top results, or keep a precise top-N set plus approximate ranks for everyone else (score buckets). Persist scores in a durable database and rebuild Redis from it after failures. Use separate sorted sets for daily, weekly and all-time boards with TTLs on the short ones.

## 417: How would you prevent double booking in a reservation system?

Let the database enforce it. In PostgreSQL, an exclusion constraint on a time range with btree_gist stops overlapping bookings for the same room, even under concurrency. Alternatives: a unique constraint on `(resource_id, slot)` for fixed slots, `SELECT ... FOR UPDATE` on the resource row, or a DynamoDB conditional put per slot. Add short-lived holds with expiry while users pay.

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE bookings (
  room_id int NOT NULL,
  during tstzrange NOT NULL,
  EXCLUDE USING gist (room_id WITH =, during WITH &&)
);
```

## 418: A MongoDB app gets slower as data grows. What do you check?

Run `explain('executionStats')` on slow queries from the profiler or Atlas Performance Advisor and look for `COLLSCAN` and high "docs examined vs returned" ratios; add or fix compound indexes using the ESR rule. Check document size and unbounded arrays, WiredTiger cache usage and eviction, whether the working set still fits in RAM, `$lookup`-heavy pipelines, and write concern or replication lag. If one replica set is maxed out on writes, consider sharding with a good shard key.

## 419: A 10 TB PostgreSQL database is hitting write limits. What are your options?

First measure: WAL volume, checkpoint frequency, index count on hot tables, vacuum lag, lock waits and disk I/O. Quick wins: drop unused indexes, batch writes, increase `max_wal_size`, use faster storage, partition the biggest tables. If still not enough: move high-volume data (events, logs) to a better-suited store, split features into separate databases, shard by tenant with Citus, or move to a distributed SQL database. Each step up adds more complexity than the last.

## 420: DynamoDB is throttling requests. How do you investigate?

Check CloudWatch metrics for throttled requests per table and index, and use CloudWatch Contributor Insights to find the hottest partition keys. Common causes: a hot key or low-cardinality partition key, a GSI with lower capacity than the table (which throttles base table writes), a sudden traffic spike in provisioned mode, or big scans. Fixes include better keys or write sharding, on-demand mode, raising GSI capacity, caching with DAX, and exponential backoff in clients (the SDK retries by default).

## 421: Cassandra read latency suddenly spikes. What do you look at?

Check `nodetool tablestats` and `tablehistograms` for SSTables per read, partition sizes and tombstones scanned. Big partitions and tombstone-heavy reads (queue-like patterns, frequent deletes) are common causes. Also check pending compactions, GC pauses in logs, a node that is down causing extra coordinator work, disk latency, and whether consistency levels changed. Fix the data model if partitions are unbounded; tuning alone won't save it.

## 422: An Elasticsearch cluster turns yellow or red. What does it mean and what do you do?

Yellow means all primary shards are assigned but some replicas aren't, so you have less redundancy. Red means at least one primary shard is unassigned, so some data is unavailable. Use `GET _cluster/allocation/explain` to see why: a node left, disk watermarks were hit, shard count limits, or allocation rules. Common fixes: free disk space, add nodes, reduce replicas temporarily, or restore from snapshot if a primary is truly lost.

## 423: Redis ran out of memory in production. What happened and how do you fix it?

Likely causes: keys without TTL piling up, a `noeviction` policy on a cache, large values or big collections, fork for RDB/AOF rewrite doubling memory through copy-on-write, or client output buffers from slow subscribers. Investigate with `INFO memory`, `MEMORY USAGE`, `redis-cli --bigkeys` and `--memkeys`. Fix: set TTLs, choose the right eviction policy for caches, split big keys, set `maxmemory` below actual RAM to leave room for forks, and scale out with Cluster if data really grew.

## 424: How would you choose a database for an offline-first mobile app?

The app needs a local database plus sync. Options: SQLite on the device with a sync engine (PowerSync or ElectricSQL syncing with PostgreSQL), Firestore with its built-in offline cache, Couchbase Lite with Sync Gateway, or Realm-style object stores. Think about conflict resolution (last-writer-wins, server rules or CRDTs), partial sync (only the user's data), and how schema changes reach old app versions.

## 425: How would you design an active-active multi-region e-commerce backend?

Split data by consistency needs. Product catalog and content: replicate everywhere, read locally, eventual consistency is fine. Carts and sessions: DynamoDB global tables or regional Redis, last-writer-wins is acceptable. Orders and payments: give each order a home region and write it there, or use distributed SQL with consensus for global uniqueness. Inventory is the hardest part: allocate stock per region with periodic rebalancing, or route reservations to one owner region.

## 426: How would you store metrics with high-cardinality labels like customer id?

Classic Prometheus-style TSDBs struggle with millions of series. Options: keep customer-level data out of metrics and put it in logs or traces, aggregate before storing (per plan instead of per customer), or use a columnar store like ClickHouse where high cardinality is just more rows in a sorted table. Some observability systems built on columnar storage are designed for exactly this. Set label limits to protect the TSDB.

## 427: How would you store data for audited financial reporting?

Keep the source of truth in a relational database with append-only, double-entry entries and no destructive updates; corrections are new reversing entries. Track who changed what with audit tables or CDC into immutable storage (S3 Object Lock). Load data into a warehouse for reports, with reconciled snapshots per period so reports can be reproduced. Use database-level constraints and access controls, not just app code, since auditors care about what anyone could change.

## 428: How would you design storage for a notification system?

Incoming notification requests go to a queue (SQS, Kafka) for buffering and retries. User preferences and device tokens live in a key-value or relational store. Each user's inbox is time-ordered and read by user, which fits DynamoDB (user as partition key, timestamp as sort key, TTL for old items) or Cassandra, or PostgreSQL with a good index at smaller scale. Unread counters go in Redis. Delivery attempts and status go to a log or analytics store.

## 429: How do you implement search with per-user permissions?

Filtering after the search is slow and breaks pagination. Better: store access info on each indexed document (owner, team ids, ACL group ids) and filter at query time with the user's groups (`terms` filter in Elasticsearch, metadata filters in vector stores). For very large or changing permission graphs, use a separate authorization service (like OpenFGA or SpiceDB, based on Google's Zanzibar) to compute allowed resource sets, and keep permission updates flowing into the index fast.

## 430: How would you move from a self-hosted database to a managed service?

Check feature compatibility (extensions, versions, superuser-only features you rely on), network latency from your app to the new location, and limits like max connections and storage IOPS. Migrate with native replication or a migration service (AWS DMS, Atlas Live Migration, logical replication for Postgres), keep the old system in sync until cutover, and rehearse the switch. Update backups, monitoring, secrets and runbooks, since the operational model changes.

## 431: How does a read-modify-write cycle break in a key-value store and how do you fix it?

If two clients `GET` a JSON value, change it in code and `SET` it back, one change is lost. Fixes: use server-side atomic operations (Redis `HINCRBY`, `JSON.NUMINCRBY`, DynamoDB update expressions), optimistic concurrency with versions (DynamoDB condition expressions, Redis `WATCH`, etcd compare-and-swap), or move the logic into a Lua script or Redis Function that runs atomically. Splitting data into finer-grained keys or attributes also reduces conflicts.

## 432: Why do distributed SQL databases have higher latency than a single PostgreSQL?

Every write must be replicated to a majority of replicas through consensus before commit, which adds at least one network round trip; across regions that's tens of milliseconds. Transactions touching several ranges also need a commit protocol across them, and reads may need to check timestamps or leases. A single-node PostgreSQL commits with a local disk flush. The trade is latency for automatic scaling and surviving failures.

## 433: Why do sequences have gaps, and how do distributed databases handle them?

In PostgreSQL and MySQL, a sequence value used by a rolled-back transaction is never reused, and values are cached per session, so gaps are normal; never rely on ids being gap-free. Distributed databases avoid a single global counter because it would be a bottleneck: CockroachDB defaults to `unique_rowid()`, TiDB offers `AUTO_RANDOM`, Spanner recommends UUIDs or bit-reversed sequences. If you truly need gap-free numbering (like invoice numbers), use a dedicated counter row updated in the same transaction and accept the contention.

## 434: How is graph analytics different from graph OLTP?

Graph OLTP answers local questions from a starting point: "friends of this user", "path between these two accounts", in milliseconds. Graph analytics runs algorithms over the whole graph: PageRank, community detection, shortest paths for all pairs, which can take minutes. Neo4j Graph Data Science, Spark GraphFrames and dedicated graph engines handle analytics, often on a projected copy of the graph in memory, separate from the transactional store.

## 435: What is local-first software and what databases support it?

Local-first apps keep the main copy of the user's data on their device and sync in the background, so they work offline and feel instant. Data is often stored in SQLite or IndexedDB and merged with CRDTs or server-authoritative sync. Tools include ElectricSQL and PowerSync (syncing Postgres to local SQLite), Automerge and Yjs (CRDT documents), Replicache/Zero, Triplit and Firebase's offline mode. The hard parts are conflict handling, partial sync and authorization.

## 436: What did teams learn from big database migrations?

Common lessons from public write-ups: the switch is rarely about one database being "bad"; it's about access patterns changing as the product grew. Migrations take longer than planned, mostly in data checking and edge cases, not copying. Shadow reads and dual writes with reconciliation catch bugs early. Moving to a new database brings new failure modes to learn. And sometimes fixing the data model in the existing database would have been cheaper than switching.

## 437: What is data gravity and how does it affect database choices?

Data gravity means that as data grows, apps, services and tools are pulled to wherever it lives, because moving large data is slow and costly (egress fees, transfer time). It makes the first database and cloud choice sticky. It's a reason to prefer open formats (Parquet, Iceberg) and portable engines, and to place compute near the data instead of the other way around.

## 438: Why is PostgreSQL growing into so many specialized areas?

Its extension system lets others add data types, index types and functions without forking: PostGIS, pgvector, TimescaleDB, Citus, pg_duckdb and ParadeDB-style search extensions. Many new products are Postgres-compatible (Aurora, AlloyDB, Neon, Supabase, YugabyteDB, CockroachDB's wire protocol). This makes "just use Postgres" a real strategy for longer than before, though specialized databases still win at extreme scale or specific workloads.

## 439: Why is vector search now part of so many general databases?

Once embeddings became common for search and RAG, keeping vectors in a separate system meant syncing data and permissions twice. So general databases added vector types and ANN indexes: PostgreSQL (pgvector), MongoDB Atlas Vector Search, Redis, Elasticsearch and OpenSearch, Cassandra 5.0, ClickHouse, SQL Server, Oracle and others. Dedicated vector databases now compete on scale, cost per vector, filtered search and hybrid search quality.

## 440: How do you evaluate a new or trendy database before adopting it?

Ask: what problem does it solve that our current stack can't? Read its consistency guarantees and any Jepsen or independent tests. Check its license, company health and community size, backup and restore tools, monitoring, managed hosting, client library quality for Node.js, and how hard it would be to leave. Prototype with your real workload and test failures. Adopt it first for a non-critical feature if possible.

## 441: What is the difference between serializability in a single node and in a distributed database?

On one node, the database sees all transactions and can order them with locks or SSI using local memory and a single clock. In a distributed database, transactions on different nodes must agree on an order without a shared clock or shared memory, so systems use timestamp oracles (TiDB), synchronized clocks (Spanner), HLCs with uncertainty restarts (CockroachDB) or deterministic ordering. That coordination costs latency and makes retries more frequent under contention.

## 442: How does Kafka's log compare to a database's write-ahead log?

Both are append-only, ordered logs. A database's WAL is internal: it exists for crash recovery and replication and is trimmed after checkpoints. Kafka makes the log the product: it's partitioned, replicated, kept for a configured time (or compacted by key) and read by many independent consumers at their own pace. This "log as the central data structure" idea is why Kafka is used to connect databases, caches, search indexes and warehouses through CDC.

## 443: What should you think about when caching data from an eventually consistent database?

The cache can hide or add staleness. If you fill the cache from a lagging replica right after a write, you may cache old data with a long TTL. Invalidating on writes can race with a concurrent read that refills with old data. Fixes: fill the cache from the primary after writes, include a version in the cached value and only overwrite with newer versions, use short TTLs, or update the cache from CDC events in commit order.

## 444: How do you compare database options in a system design interview?

State the requirements first: data shape, access patterns, read and write rates, size, consistency, latency, availability and regions. Then propose a primary database and explain why it fits, name one or two alternatives and why you didn't pick them, and add supporting stores (cache, search, analytics) only with a reason. Mention key design details (partition key, indexes, replication) and the trade-offs you accept. Interviewers care more about the reasoning than the product name.

## 445: What are the real limits of a single relational database server today?

Modern cloud machines offer hundreds of CPU cores, terabytes of RAM and NVMe storage with hundreds of thousands of IOPS. A well-tuned PostgreSQL or MySQL server on that hardware can handle tens of TB of data and tens of thousands of transactions per second, with read replicas for more reads. Many large companies run their main databases this way. The real limits are usually write throughput, operations on huge tables (vacuum, index builds, backups) and the blast radius of one machine.

## 446: How does a document database's sharded transaction compare to a distributed SQL transaction?

MongoDB supports multi-document transactions across shards using two-phase commit coordinated by a shard, with snapshot isolation. It works, but cross-shard transactions are slower, have time limits and MongoDB's own advice is to model data so most writes touch one document. Distributed SQL databases are built around multi-row, multi-range transactions from the start, with serializable isolation as default in CockroachDB. Both pay for distributed commits with latency.

## 447: How do you decide when to denormalize in a relational database?

Start normalized. Denormalize when you have measured a read path that's too slow or too costly with joins, the copied data changes rarely, and you have a reliable way to keep copies in sync (triggers, the same transaction, or async jobs with reconciliation). Common examples: counters like `comment_count`, the latest status on a parent row, or a read-optimized summary table. Document what's duplicated so future changes update every copy.

## 448: Why do analytics databases avoid row-level indexes?

Analytics queries read large portions of tables, where a full scan of compressed columns is faster than millions of random index lookups. Row-level B-tree indexes would also slow down bulk inserts and take lots of space. Instead, they use sort order, sparse primary indexes, zone maps and partition pruning to skip whole blocks of data. That's why picking the sort key and partition key is the main tuning step in ClickHouse, Snowflake (clustering keys) or BigQuery (partitioning and clustering).

## 449: What is the difference between how row stores and column stores handle a single-row update?

A row store finds the row through an index and changes one page: cheap and fast. A column store has the row spread across many column files, each compressed in blocks, so changing one row means rewriting parts of many files or writing a delete marker plus a new row and merging later. That's why column stores batch updates, use special merge engines, or keep a small row-based delta store that's merged into columns in the background (as in SQL Server columnstore and some HTAP systems).

## 450: If you could only run one database for a typical web company, what would you pick and why?

Most engineers would pick PostgreSQL. It handles transactional data with strong guarantees, flexible JSON documents, full-text search, geospatial queries, vector search and moderate analytics, has excellent tooling and runs managed on every cloud. Its weak spots are huge-scale analytics, extreme write throughput and global multi-region writes, which you'd handle later with ClickHouse, a wide-column store or distributed SQL. The honest answer in an interview also says: it depends on access patterns, and you'd revisit the choice as the product grows.
