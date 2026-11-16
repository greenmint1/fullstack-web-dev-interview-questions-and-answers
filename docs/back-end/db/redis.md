# Redis Interview Questions and Answers

_Last updated: November 5, 2026_

450 Redis interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Redis 8.x (Redis Open Source 8.0 up to 8.6). In Redis 8, JSON, the Query Engine (search and vector search), time series and probabilistic data types are part of the main server, so you no longer need Redis Stack for them. Node.js examples use `ioredis` or `node-redis`, and older behavior is mentioned where you will still run into it.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Redis?](#1-what-is-redis)
- [2: What does the name Redis stand for?](#2-what-does-the-name-redis-stand-for)
- [3: What are the most common use cases for Redis?](#3-what-are-the-most-common-use-cases-for-redis)
- [4: Why is Redis so fast?](#4-why-is-redis-so-fast)
- [5: Is Redis single-threaded?](#5-is-redis-single-threaded)
- [6: What is the default port of Redis?](#6-what-is-the-default-port-of-redis)
- [7: How do you run Redis locally with Docker?](#7-how-do-you-run-redis-locally-with-docker)
- [8: What is redis-cli?](#8-what-is-redis-cli)
- [9: What does the PING command do?](#9-what-does-the-ping-command-do)
- [10: How do you set and get a value?](#10-how-do-you-set-and-get-a-value)
- [11: What data types does Redis support?](#11-what-data-types-does-redis-support)
- [12: What is a Redis string?](#12-what-is-a-redis-string)
- [13: What does binary-safe mean in Redis?](#13-what-does-binary-safe-mean-in-redis)
- [14: How do you delete a key?](#14-how-do-you-delete-a-key)
- [15: What is the difference between DEL and UNLINK?](#15-what-is-the-difference-between-del-and-unlink)
- [16: How do you check if a key exists?](#16-how-do-you-check-if-a-key-exists)
- [17: How do you set an expiration on a key?](#17-how-do-you-set-an-expiration-on-a-key)
- [18: How do you check how much time a key has left?](#18-how-do-you-check-how-much-time-a-key-has-left)
- [19: How do you remove an expiration from a key?](#19-how-do-you-remove-an-expiration-from-a-key)
- [20: What does EXPIRETIME return?](#20-what-does-expiretime-return)
- [21: What options does the SET command have?](#21-what-options-does-the-set-command-have)
- [22: What is SETNX and what should you use instead?](#22-what-is-setnx-and-what-should-you-use-instead)
- [23: How do INCR and DECR work?](#23-how-do-incr-and-decr-work)
- [24: Are INCR operations safe when many clients run them at once?](#24-are-incr-operations-safe-when-many-clients-run-them-at-once)
- [25: How do you work with floating point numbers?](#25-how-do-you-work-with-floating-point-numbers)
- [26: How do MSET and MGET work?](#26-how-do-mset-and-mget-work)
- [27: What do APPEND and STRLEN do?](#27-what-do-append-and-strlen-do)
- [28: What are GETRANGE and SETRANGE?](#28-what-are-getrange-and-setrange)
- [29: What do GETDEL and GETEX do?](#29-what-do-getdel-and-getex-do)
- [30: What is a Redis list?](#30-what-is-a-redis-list)
- [31: What is the difference between LPUSH and RPUSH?](#31-what-is-the-difference-between-lpush-and-rpush)
- [32: How do LPOP and RPOP work?](#32-how-do-lpop-and-rpop-work)
- [33: How do you use a list as a queue and as a stack?](#33-how-do-you-use-a-list-as-a-queue-and-as-a-stack)
- [34: How does LRANGE work?](#34-how-does-lrange-work)
- [35: How do you get the length of a list?](#35-how-do-you-get-the-length-of-a-list)
- [36: What does LTRIM do?](#36-what-does-ltrim-do)
- [37: What are LINDEX, LSET and LINSERT?](#37-what-are-lindex-lset-and-linsert)
- [38: How do you remove specific values from a list?](#38-how-do-you-remove-specific-values-from-a-list)
- [39: What is BLPOP?](#39-what-is-blpop)
- [40: What does LMOVE do?](#40-what-does-lmove-do)
- [41: What is a Redis set?](#41-what-is-a-redis-set)
- [42: What set operations does Redis support?](#42-what-set-operations-does-redis-support)
- [43: How do you count and sample items in a set?](#43-how-do-you-count-and-sample-items-in-a-set)
- [44: How do you remove items from a set or move them to another set?](#44-how-do-you-remove-items-from-a-set-or-move-them-to-another-set)
- [45: What is a sorted set?](#45-what-is-a-sorted-set)
- [46: How do you get the top players from a sorted set?](#46-how-do-you-get-the-top-players-from-a-sorted-set)
- [47: How do you get a member's score and rank?](#47-how-do-you-get-a-members-score-and-rank)
- [48: How do you increase a member's score?](#48-how-do-you-increase-a-members-score)
- [49: How do you query a sorted set by score range?](#49-how-do-you-query-a-sorted-set-by-score-range)
- [50: How do you remove members from a sorted set?](#50-how-do-you-remove-members-from-a-sorted-set)
- [51: What options does ZADD support?](#51-what-options-does-zadd-support)
- [52: What is a Redis hash?](#52-what-is-a-redis-hash)
- [53: What are the main hash commands?](#53-what-are-the-main-hash-commands)
- [54: When should you use a hash instead of a JSON string?](#54-when-should-you-use-a-hash-instead-of-a-json-string)
- [55: Can you set a TTL on a single hash field?](#55-can-you-set-a-ttl-on-a-single-hash-field)
- [56: What is a Redis stream?](#56-what-is-a-redis-stream)
- [57: What does the * mean in XADD?](#57-what-does-the--mean-in-xadd)
- [58: How do you read new entries from a stream?](#58-how-do-you-read-new-entries-from-a-stream)
- [59: What is pub/sub in Redis?](#59-what-is-pubsub-in-redis)
- [60: What is the difference between SUBSCRIBE and PSUBSCRIBE?](#60-what-is-the-difference-between-subscribe-and-psubscribe)
- [61: What is a bitmap?](#61-what-is-a-bitmap)
- [62: What is HyperLogLog?](#62-what-is-hyperloglog)
- [63: How do you store and search locations?](#63-how-do-you-store-and-search-locations)
- [64: What is the JSON data type?](#64-what-is-the-json-data-type)
- [65: What is a vector set?](#65-what-is-a-vector-set)
- [66: What is the time series data type?](#66-what-is-the-time-series-data-type)
- [67: What is a Bloom filter?](#67-what-is-a-bloom-filter)
- [68: How do you list keys?](#68-how-do-you-list-keys)
- [69: Why should you not use KEYS in production?](#69-why-should-you-not-use-keys-in-production)
- [70: What does the TYPE command do?](#70-what-does-the-type-command-do)
- [71: How do you rename a key?](#71-how-do-you-rename-a-key)
- [72: What does COPY do?](#72-what-does-copy-do)
- [73: What are Redis databases?](#73-what-are-redis-databases)
- [74: What is the difference between FLUSHDB and FLUSHALL?](#74-what-is-the-difference-between-flushdb-and-flushall)
- [75: How do you count the keys in a database?](#75-how-do-you-count-the-keys-in-a-database)
- [76: What is a good key naming convention?](#76-what-is-a-good-key-naming-convention)
- [77: How big can a key or a value be?](#77-how-big-can-a-key-or-a-value-be)
- [78: What is RESP?](#78-what-is-resp)
- [79: How do you connect to Redis from Node.js?](#79-how-do-you-connect-to-redis-from-nodejs)
- [80: How do you connect to Redis from Python?](#80-how-do-you-connect-to-redis-from-python)
- [81: What is caching?](#81-what-is-caching)
- [82: What is the cache-aside pattern?](#82-what-is-the-cache-aside-pattern)
- [83: What is a cache hit and a cache miss?](#83-what-is-a-cache-hit-and-a-cache-miss)
- [84: Why should cached keys have a TTL?](#84-why-should-cached-keys-have-a-ttl)
- [85: How is Redis used as a session store?](#85-how-is-redis-used-as-a-session-store)
- [86: What is the difference between Redis and Memcached?](#86-what-is-the-difference-between-redis-and-memcached)
- [87: Can Redis be used as a primary database?](#87-can-redis-be-used-as-a-primary-database)
- [88: What is persistence in Redis?](#88-what-is-persistence-in-redis)
- [89: What is an RDB snapshot?](#89-what-is-an-rdb-snapshot)
- [90: What is AOF?](#90-what-is-aof)
- [91: What is the difference between SAVE and BGSAVE?](#91-what-is-the-difference-between-save-and-bgsave)
- [92: What is the redis.conf file?](#92-what-is-the-redisconf-file)
- [93: How do you read and change config at runtime?](#93-how-do-you-read-and-change-config-at-runtime)
- [94: What does the INFO command show?](#94-what-does-the-info-command-show)
- [95: What is maxmemory?](#95-what-is-maxmemory)
- [96: What is eviction?](#96-what-is-eviction)
- [97: How do you set a password on Redis?](#97-how-do-you-set-a-password-on-redis)
- [98: What are ACLs in Redis?](#98-what-are-acls-in-redis)
- [99: What is protected mode?](#99-what-is-protected-mode)
- [100: What is replication in Redis?](#100-what-is-replication-in-redis)
- [101: What is Redis Sentinel?](#101-what-is-redis-sentinel)
- [102: What is Redis Cluster?](#102-what-is-redis-cluster)
- [103: What is the difference between Sentinel and Cluster?](#103-what-is-the-difference-between-sentinel-and-cluster)
- [104: What is a transaction in Redis?](#104-what-is-a-transaction-in-redis)
- [105: Does a Redis transaction roll back on error?](#105-does-a-redis-transaction-roll-back-on-error)
- [106: What is pipelining?](#106-what-is-pipelining)
- [107: What is Lua scripting in Redis?](#107-what-is-lua-scripting-in-redis)
- [108: What are Redis Functions?](#108-what-are-redis-functions)
- [109: What is Redis Insight?](#109-what-is-redis-insight)
- [110: What does MONITOR do?](#110-what-does-monitor-do)
- [111: What is the slow log?](#111-what-is-the-slow-log)
- [112: How do you see which clients are connected?](#112-how-do-you-see-which-clients-are-connected)
- [113: What is a distributed lock?](#113-what-is-a-distributed-lock)
- [114: How do you build a simple rate limiter?](#114-how-do-you-build-a-simple-rate-limiter)
- [115: How do you build a leaderboard?](#115-how-do-you-build-a-leaderboard)
- [116: How do you build a simple job queue?](#116-how-do-you-build-a-simple-job-queue)
- [117: What is a keyspace notification?](#117-what-is-a-keyspace-notification)
- [118: What does OBJECT ENCODING show?](#118-what-does-object-encoding-show)
- [119: What does TOUCH do?](#119-what-does-touch-do)
- [120: What does RANDOMKEY do?](#120-what-does-randomkey-do)
- [121: How do you check the server time and Redis version?](#121-how-do-you-check-the-server-time-and-redis-version)
- [122: How do you stop a Redis server safely?](#122-how-do-you-stop-a-redis-server-safely)
- [123: What does ECHO do?](#123-what-does-echo-do)
- [124: What is Redis Open Source, Redis Software and Redis Cloud?](#124-what-is-redis-open-source-redis-software-and-redis-cloud)
- [125: What is Valkey?](#125-what-is-valkey)
- [126: What license is Redis under?](#126-what-license-is-redis-under)
- [127: What was Redis Stack?](#127-what-was-redis-stack)
- [128: What does WATCH do?](#128-what-does-watch-do)
- [129: How do you count unique daily visitors cheaply?](#129-how-do-you-count-unique-daily-visitors-cheaply)
- [130: What does SRANDMEMBER with a negative count do?](#130-what-does-srandmember-with-a-negative-count-do)
- [131: What does ZRANGE BYLEX do?](#131-what-does-zrange-bylex-do)
- [132: How do you get a random member from a sorted set?](#132-how-do-you-get-a-random-member-from-a-sorted-set)
- [133: What do ZPOPMIN and ZPOPMAX do?](#133-what-do-zpopmin-and-zpopmax-do)
- [134: What does XLEN return?](#134-what-does-xlen-return)
- [135: How do you limit the size of a stream?](#135-how-do-you-limit-the-size-of-a-stream)
- [136: What is the difference between a list and a stream for queues?](#136-what-is-the-difference-between-a-list-and-a-stream-for-queues)
- [137: What does SCAN return when the cursor is 0?](#137-what-does-scan-return-when-the-cursor-is-0)
- [138: Can SCAN return the same key twice?](#138-can-scan-return-the-same-key-twice)
- [139: What are HSCAN, SSCAN and ZSCAN?](#139-what-are-hscan-sscan-and-zscan)
- [140: How do you see how much memory a key uses?](#140-how-do-you-see-how-much-memory-a-key-uses)
- [141: What is the difference between EX and PX?](#141-what-is-the-difference-between-ex-and-px)
- [142: What happens to the TTL when you modify a key?](#142-what-happens-to-the-ttl-when-you-modify-a-key)
- [143: What is the EXPIRE NX option?](#143-what-is-the-expire-nx-option)
- [144: How do you check what commands a user can run?](#144-how-do-you-check-what-commands-a-user-can-run)
- [145: How do you back up Redis?](#145-how-do-you-back-up-redis)
- [146: What happens when Redis restarts?](#146-what-happens-when-redis-restarts)
- [147: What are good use cases for sets?](#147-what-are-good-use-cases-for-sets)
- [148: What is the difference between a set and a sorted set?](#148-what-is-the-difference-between-a-set-and-a-sorted-set)
- [149: Can you nest data structures in Redis?](#149-can-you-nest-data-structures-in-redis)
- [150: What are common mistakes beginners make with Redis?](#150-what-are-common-mistakes-beginners-make-with-redis)

### Moderate Questions (151-300)

- [151: What are the main caching strategies and how do they differ?](#151-what-are-the-main-caching-strategies-and-how-do-they-differ)
- [152: How do you keep the cache in sync with the database on updates?](#152-how-do-you-keep-the-cache-in-sync-with-the-database-on-updates)
- [153: What is a cache stampede?](#153-what-is-a-cache-stampede)
- [154: How do you add TTL jitter and why?](#154-how-do-you-add-ttl-jitter-and-why)
- [155: How do you prevent a stampede with a lock?](#155-how-do-you-prevent-a-stampede-with-a-lock)
- [156: What is negative caching?](#156-what-is-negative-caching)
- [157: How do you choose between a string and a hash to cache an object?](#157-how-do-you-choose-between-a-string-and-a-hash-to-cache-an-object)
- [158: How do you cache API responses in an Express app?](#158-how-do-you-cache-api-responses-in-an-express-app)
- [159: How do you invalidate a group of related cache keys?](#159-how-do-you-invalidate-a-group-of-related-cache-keys)
- [160: How does pipelining improve performance?](#160-how-does-pipelining-improve-performance)
- [161: What is the difference between pipelining, MULTI/EXEC and Lua scripts?](#161-what-is-the-difference-between-pipelining-multiexec-and-lua-scripts)
- [162: How do you use WATCH for optimistic locking?](#162-how-do-you-use-watch-for-optimistic-locking)
- [163: How do KEYS and ARGV work in Lua scripts?](#163-how-do-keys-and-argv-work-in-lua-scripts)
- [164: What is the difference between EVAL and EVALSHA?](#164-what-is-the-difference-between-eval-and-evalsha)
- [165: What is the difference between redis.call and redis.pcall in Lua?](#165-what-is-the-difference-between-rediscall-and-redispcall-in-lua)
- [166: How do you define a reusable script in ioredis?](#166-how-do-you-define-a-reusable-script-in-ioredis)
- [167: When should you use Functions instead of EVAL?](#167-when-should-you-use-functions-instead-of-eval)
- [168: How do you write a Redis Function library?](#168-how-do-you-write-a-redis-function-library)
- [169: How does SCAN work with MATCH, COUNT and TYPE?](#169-how-does-scan-work-with-match-count-and-type)
- [170: How do you delete keys by pattern safely?](#170-how-do-you-delete-keys-by-pattern-safely)
- [171: What eviction policies are there?](#171-what-eviction-policies-are-there)
- [172: Which eviction policy should you pick for a cache?](#172-which-eviction-policy-should-you-pick-for-a-cache)
- [173: Why do job queue libraries like BullMQ require noeviction?](#173-why-do-job-queue-libraries-like-bullmq-require-noeviction)
- [174: How accurate is LRU eviction in Redis?](#174-how-accurate-is-lru-eviction-in-redis)
- [175: How does LFU eviction work?](#175-how-does-lfu-eviction-work)
- [176: How do you configure RDB snapshots?](#176-how-do-you-configure-rdb-snapshots)
- [177: What are the AOF fsync options?](#177-what-are-the-aof-fsync-options)
- [178: What is AOF rewrite?](#178-what-is-aof-rewrite)
- [179: What is multi-part AOF?](#179-what-is-multi-part-aof)
- [180: What is the RDB preamble in AOF?](#180-what-is-the-rdb-preamble-in-aof)
- [181: Should you use RDB, AOF or both?](#181-should-you-use-rdb-aof-or-both)
- [182: How do you set up a replica?](#182-how-do-you-set-up-a-replica)
- [183: Can you read from replicas?](#183-can-you-read-from-replicas)
- [184: What does the WAIT command do?](#184-what-does-the-wait-command-do)
- [185: What is WAITAOF?](#185-what-is-waitaof)
- [186: How do you configure Sentinel?](#186-how-do-you-configure-sentinel)
- [187: How does a client connect through Sentinel?](#187-how-does-a-client-connect-through-sentinel)
- [188: How are keys distributed in Redis Cluster?](#188-how-are-keys-distributed-in-redis-cluster)
- [189: What are hash tags?](#189-what-are-hash-tags)
- [190: What is a CROSSSLOT error?](#190-what-is-a-crossslot-error)
- [191: What are MOVED and ASK redirects?](#191-what-are-moved-and-ask-redirects)
- [192: How do you create a Redis Cluster?](#192-how-do-you-create-a-redis-cluster)
- [193: How do you connect to a cluster from Node.js?](#193-how-do-you-connect-to-a-cluster-from-nodejs)
- [194: How do you add a node to a cluster and move slots to it?](#194-how-do-you-add-a-node-to-a-cluster-and-move-slots-to-it)
- [195: What is sharded pub/sub?](#195-what-is-sharded-pubsub)
- [196: What are the limits of Redis pub/sub?](#196-what-are-the-limits-of-redis-pubsub)
- [197: How do you subscribe to a channel in Node.js?](#197-how-do-you-subscribe-to-a-channel-in-nodejs)
- [198: What is a consumer group in streams?](#198-what-is-a-consumer-group-in-streams)
- [199: How do consumers read and acknowledge entries?](#199-how-do-consumers-read-and-acknowledge-entries)
- [200: How do you handle entries that a crashed consumer never acknowledged?](#200-how-do-you-handle-entries-that-a-crashed-consumer-never-acknowledged)
- [201: How do you inspect a stream and its groups?](#201-how-do-you-inspect-a-stream-and-its-groups)
- [202: How do you write a stream consumer in Node.js?](#202-how-do-you-write-a-stream-consumer-in-nodejs)
- [203: When should you use pub/sub, lists or streams for messaging?](#203-when-should-you-use-pubsub-lists-or-streams-for-messaging)
- [204: How do you build a sliding window rate limiter with a sorted set?](#204-how-do-you-build-a-sliding-window-rate-limiter-with-a-sorted-set)
- [205: How do you build a token bucket rate limiter?](#205-how-do-you-build-a-token-bucket-rate-limiter)
- [206: How do you release a lock safely?](#206-how-do-you-release-a-lock-safely)
- [207: What problems can a Redis lock still have?](#207-what-problems-can-a-redis-lock-still-have)
- [208: How do you extend a lock while work is still running?](#208-how-do-you-extend-a-lock-while-work-is-still-running)
- [209: How do you build a delayed job queue?](#209-how-do-you-build-a-delayed-job-queue)
- [210: How do you build a reliable queue with lists?](#210-how-do-you-build-a-reliable-queue-with-lists)
- [211: What is BullMQ and how does it use Redis?](#211-what-is-bullmq-and-how-does-it-use-redis)
- [212: How do you store sessions in Redis with Express?](#212-how-do-you-store-sessions-in-redis-with-express)
- [213: How should a Node.js app manage Redis connections?](#213-how-should-a-nodejs-app-manage-redis-connections)
- [214: How do you handle reconnects in ioredis?](#214-how-do-you-handle-reconnects-in-ioredis)
- [215: How do you handle reconnects in node-redis?](#215-how-do-you-handle-reconnects-in-node-redis)
- [216: What happens to your app if Redis goes down?](#216-what-happens-to-your-app-if-redis-goes-down)
- [217: How do you use Redis transactions in node-redis?](#217-how-do-you-use-redis-transactions-in-node-redis)
- [218: What is client-side caching?](#218-what-is-client-side-caching)
- [219: What are the client tracking modes?](#219-what-are-the-client-tracking-modes)
- [220: What is RESP3 and why does it matter?](#220-what-is-resp3-and-why-does-it-matter)
- [221: How do you use keyspace notifications to react to expired keys?](#221-how-do-you-use-keyspace-notifications-to-react-to-expired-keys)
- [222: What letters can you use in notify-keyspace-events?](#222-what-letters-can-you-use-in-notify-keyspace-events)
- [223: How do you create ACL users for different services?](#223-how-do-you-create-acl-users-for-different-services)
- [224: What do key permissions like %R~ and %W~ mean?](#224-what-do-key-permissions-like-r-and-w-mean)
- [225: How do you turn on TLS?](#225-how-do-you-turn-on-tls)
- [226: How should you secure a Redis server?](#226-how-should-you-secure-a-redis-server)
- [227: What replaced rename-command?](#227-what-replaced-rename-command)
- [228: How do you find big keys?](#228-how-do-you-find-big-keys)
- [229: What is a hot key and how do you find one?](#229-what-is-a-hot-key-and-how-do-you-find-one)
- [230: How do you deal with a hot key?](#230-how-do-you-deal-with-a-hot-key)
- [231: How do you use the latency monitor?](#231-how-do-you-use-the-latency-monitor)
- [232: How do you measure latency from the client side?](#232-how-do-you-measure-latency-from-the-client-side)
- [233: What are the most useful INFO fields to monitor?](#233-what-are-the-most-useful-info-fields-to-monitor)
- [234: What are the internal encodings of each type?](#234-what-are-the-internal-encodings-of-each-type)
- [235: What config settings control compact encodings?](#235-what-config-settings-control-compact-encodings)
- [236: How do you save memory with many small objects?](#236-how-do-you-save-memory-with-many-small-objects)
- [237: How do you query JSON documents with JSONPath?](#237-how-do-you-query-json-documents-with-jsonpath)
- [238: What is the Redis Query Engine?](#238-what-is-the-redis-query-engine)
- [239: How do you create a search index and query it?](#239-how-do-you-create-a-search-index-and-query-it)
- [240: How do you index JSON documents?](#240-how-do-you-index-json-documents)
- [241: What is FT.AGGREGATE used for?](#241-what-is-ftaggregate-used-for)
- [242: How do you add vector search to an index?](#242-how-do-you-add-vector-search-to-an-index)
- [243: What is the difference between vector sets and vector fields in the Query Engine?](#243-what-is-the-difference-between-vector-sets-and-vector-fields-in-the-query-engine)
- [244: How do you downsample time series data?](#244-how-do-you-downsample-time-series-data)
- [245: What other probabilistic data types are there?](#245-what-other-probabilistic-data-types-are-there)
- [246: How do you use BITFIELD?](#246-how-do-you-use-bitfield)
- [247: How do you combine bitmaps?](#247-how-do-you-combine-bitmaps)
- [248: How do you paginate a sorted set?](#248-how-do-you-paginate-a-sorted-set)
- [249: How do ZUNIONSTORE and ZINTERSTORE work?](#249-how-do-zunionstore-and-zinterstore-work)
- [250: What do LMPOP, ZMPOP and SINTERCARD do?](#250-what-do-lmpop-zmpop-and-sintercard-do)
- [251: How do you model a "users who viewed this item" feature?](#251-how-do-you-model-a-users-who-viewed-this-item-feature)
- [252: How do you build a news feed in Redis?](#252-how-do-you-build-a-news-feed-in-redis)
- [253: How do you build autocomplete with Redis?](#253-how-do-you-build-autocomplete-with-redis)
- [254: How do you store an object with an expiring field, like a one-time code?](#254-how-do-you-store-an-object-with-an-expiring-field-like-a-one-time-code)
- [255: How do HSETEX and HGETEX work?](#255-how-do-hsetex-and-hgetex-work)
- [256: How do you run Redis with Docker Compose for development?](#256-how-do-you-run-redis-with-docker-compose-for-development)
- [257: How do you test code that uses Redis?](#257-how-do-you-test-code-that-uses-redis)
- [258: How do you run Redis in Kubernetes?](#258-how-do-you-run-redis-in-kubernetes)
- [259: How do you migrate data between two Redis servers?](#259-how-do-you-migrate-data-between-two-redis-servers)
- [260: What does the MIGRATE command do?](#260-what-does-the-migrate-command-do)
- [261: What are DUMP and RESTORE?](#261-what-are-dump-and-restore)
- [262: How do you check replication lag?](#262-how-do-you-check-replication-lag)
- [263: What are min-replicas-to-write and min-replicas-max-lag?](#263-what-are-min-replicas-to-write-and-min-replicas-max-lag)
- [264: How do you see the cluster state and topology?](#264-how-do-you-see-the-cluster-state-and-topology)
- [265: How do you read from replicas in Redis Cluster?](#265-how-do-you-read-from-replicas-in-redis-cluster)
- [266: How does failover work in Redis Cluster?](#266-how-does-failover-work-in-redis-cluster)
- [267: What is cluster-require-full-coverage?](#267-what-is-cluster-require-full-coverage)
- [268: Can you use transactions and Lua scripts in Redis Cluster?](#268-can-you-use-transactions-and-lua-scripts-in-redis-cluster)
- [269: Can you use multiple databases in Redis Cluster?](#269-can-you-use-multiple-databases-in-redis-cluster)
- [270: How do you serialize values for Redis?](#270-how-do-you-serialize-values-for-redis)
- [271: How do you store dates and numbers in Redis?](#271-how-do-you-store-dates-and-numbers-in-redis)
- [272: What is the OBJECT command used for?](#272-what-is-the-object-command-used-for)
- [273: How can you find keys without a TTL?](#273-how-can-you-find-keys-without-a-ttl)
- [274: How do you rename keys or change structure without downtime?](#274-how-do-you-rename-keys-or-change-structure-without-downtime)
- [275: What is the difference between RENAME and COPY plus DEL?](#275-what-is-the-difference-between-rename-and-copy-plus-del)
- [276: How do you atomically swap in a new version of a big collection?](#276-how-do-you-atomically-swap-in-a-new-version-of-a-big-collection)
- [277: How do you count events per minute for a dashboard?](#277-how-do-you-count-events-per-minute-for-a-dashboard)
- [278: How do you implement idempotency keys for an API?](#278-how-do-you-implement-idempotency-keys-for-an-api)
- [279: How do you deduplicate events or messages?](#279-how-do-you-deduplicate-events-or-messages)
- [280: How do you avoid race conditions in read-modify-write code?](#280-how-do-you-avoid-race-conditions-in-read-modify-write-code)
- [281: What is the compare-and-set support added in Redis 8.4?](#281-what-is-the-compare-and-set-support-added-in-redis-84)
- [282: How do you set many keys with a TTL in one command?](#282-how-do-you-set-many-keys-with-a-ttl-in-one-command)
- [283: How do you limit concurrent jobs per user?](#283-how-do-you-limit-concurrent-jobs-per-user)
- [284: How do you use Redis with NestJS for caching?](#284-how-do-you-use-redis-with-nestjs-for-caching)
- [285: How do you choose the right data type for a problem?](#285-how-do-you-choose-the-right-data-type-for-a-problem)
- [286: What happens when you run a command on the wrong type?](#286-what-happens-when-you-run-a-command-on-the-wrong-type)
- [287: How do you limit the number of client connections?](#287-how-do-you-limit-the-number-of-client-connections)
- [288: How do you close idle connections?](#288-how-do-you-close-idle-connections)
- [289: What is the Redis query buffer and output buffer?](#289-what-is-the-redis-query-buffer-and-output-buffer)
- [290: How do you configure client output buffer limits?](#290-how-do-you-configure-client-output-buffer-limits)
- [291: What does CONFIG RESETSTAT do?](#291-what-does-config-resetstat-do)
- [292: How do you see per-command statistics?](#292-how-do-you-see-per-command-statistics)
- [293: How do you load a lot of data into Redis quickly?](#293-how-do-you-load-a-lot-of-data-into-redis-quickly)
- [294: How do you run a Lua script from a file with redis-cli?](#294-how-do-you-run-a-lua-script-from-a-file-with-redis-cli)
- [295: How do you debug a Lua script?](#295-how-do-you-debug-a-lua-script)
- [296: Can Lua scripts call any Redis command?](#296-can-lua-scripts-call-any-redis-command)
- [297: How do you store a large list of IDs for a user efficiently?](#297-how-do-you-store-a-large-list-of-ids-for-a-user-efficiently)
- [298: What is the difference between EXPIRE on a key and a TTL in a sorted set score?](#298-what-is-the-difference-between-expire-on-a-key-and-a-ttl-in-a-sorted-set-score)
- [299: How do you check the health of Redis from a load balancer or Kubernetes?](#299-how-do-you-check-the-health-of-redis-from-a-load-balancer-or-kubernetes)
- [300: What should you monitor and alert on in production?](#300-what-should-you-monitor-and-alert-on-in-production)

### Advanced Questions (301-450)

- [301: How does the Redis event loop work?](#301-how-does-the-redis-event-loop-work)
- [302: What do I/O threads do and when should you turn them on?](#302-what-do-io-threads-do-and-when-should-you-turn-them-on)
- [303: What work does Redis do in background threads?](#303-what-work-does-redis-do-in-background-threads)
- [304: How does BGSAVE use fork and copy-on-write?](#304-how-does-bgsave-use-fork-and-copy-on-write)
- [305: Why should you disable Transparent Huge Pages for Redis?](#305-why-should-you-disable-transparent-huge-pages-for-redis)
- [306: Why does Redis recommend vm.overcommit_memory = 1?](#306-why-does-redis-recommend-vmovercommit_memory--1)
- [307: How does key expiration work internally?](#307-how-does-key-expiration-work-internally)
- [308: How do replicas handle expired keys?](#308-how-do-replicas-handle-expired-keys)
- [309: How are TTLs stored and how precise are they?](#309-how-are-ttls-stored-and-how-precise-are-they)
- [310: How does the Redis dictionary (hash table) work?](#310-how-does-the-redis-dictionary-hash-table-work)
- [311: What is SDS?](#311-what-is-sds)
- [312: What is the difference between embstr and raw encoding?](#312-what-is-the-difference-between-embstr-and-raw-encoding)
- [313: How is a sorted set implemented?](#313-how-is-a-sorted-set-implemented)
- [314: What is a listpack and why did it replace ziplist?](#314-what-is-a-listpack-and-why-did-it-replace-ziplist)
- [315: What is a quicklist?](#315-what-is-a-quicklist)
- [316: How are streams stored internally?](#316-how-are-streams-stored-internally)
- [317: How does Redis decide when to convert compact encodings?](#317-how-does-redis-decide-when-to-convert-compact-encodings)
- [318: How does memory fragmentation happen and how do you fix it?](#318-how-does-memory-fragmentation-happen-and-how-do-you-fix-it)
- [319: How does active defragmentation work?](#319-how-does-active-defragmentation-work)
- [320: What is the memory overhead per key?](#320-what-is-the-memory-overhead-per-key)
- [321: How does Redis compute used memory against maxmemory?](#321-how-does-redis-compute-used-memory-against-maxmemory)
- [322: How does the eviction process work step by step?](#322-how-does-the-eviction-process-work-step-by-step)
- [323: Why can a write still fail with OOM when eviction is on?](#323-why-can-a-write-still-fail-with-oom-when-eviction-is-on)
- [324: How does replication work?](#324-how-does-replication-work)
- [325: What is the replication ID and offset?](#325-what-is-the-replication-id-and-offset)
- [326: What is the replication backlog and how big should it be?](#326-what-is-the-replication-backlog-and-how-big-should-it-be)
- [327: What is diskless replication?](#327-what-is-diskless-replication)
- [328: What happens when a primary without persistence restarts?](#328-what-happens-when-a-primary-without-persistence-restarts)
- [329: How does Sentinel detect failures and fail over?](#329-how-does-sentinel-detect-failures-and-fail-over)
- [330: Why do you need a majority of Sentinels for failover?](#330-why-do-you-need-a-majority-of-sentinels-for-failover)
- [331: What is split brain in Redis and how do you limit it?](#331-what-is-split-brain-in-redis-and-how-do-you-limit-it)
- [332: How does Redis Cluster's gossip protocol work?](#332-how-does-redis-clusters-gossip-protocol-work)
- [333: What are config epochs in Redis Cluster?](#333-what-are-config-epochs-in-redis-cluster)
- [334: How does slot migration work in Redis Cluster?](#334-how-does-slot-migration-work-in-redis-cluster)
- [335: What consistency guarantees does Redis Cluster give?](#335-what-consistency-guarantees-does-redis-cluster-give)
- [336: Does WAIT make Redis strongly consistent?](#336-does-wait-make-redis-strongly-consistent)
- [337: Why is a long-running Lua script dangerous?](#337-why-is-a-long-running-lua-script-dangerous)
- [338: How are Lua scripts replicated?](#338-how-are-lua-scripts-replicated)
- [339: What are script and function flags?](#339-what-are-script-and-function-flags)
- [340: Why must all keys be passed in KEYS even if Redis does not enforce it?](#340-why-must-all-keys-be-passed-in-keys-even-if-redis-does-not-enforce-it)
- [341: How do Lua scripts handle errors and partial writes?](#341-how-do-lua-scripts-handle-errors-and-partial-writes)
- [342: What are the risks of big keys?](#342-what-are-the-risks-of-big-keys)
- [343: How do you safely delete a huge key?](#343-how-do-you-safely-delete-a-huge-key)
- [344: What lazyfree options exist and when should you enable them?](#344-what-lazyfree-options-exist-and-when-should-you-enable-them)
- [345: What are the main causes of latency spikes in Redis?](#345-what-are-the-main-causes-of-latency-spikes-in-redis)
- [346: How can mass expiration cause latency?](#346-how-can-mass-expiration-cause-latency)
- [347: How does AOF fsync cause latency with everysec?](#347-how-does-aof-fsync-cause-latency-with-everysec)
- [348: How do you tell if Redis is swapping?](#348-how-do-you-tell-if-redis-is-swapping)
- [349: How do slow subscribers affect pub/sub?](#349-how-do-slow-subscribers-affect-pubsub)
- [350: How do you plan Redis capacity?](#350-how-do-you-plan-redis-capacity)
- [351: When should you shard Redis?](#351-when-should-you-shard-redis)
- [352: What are the options for sharding Redis?](#352-what-are-the-options-for-sharding-redis)
- [353: How do you design keys for Redis Cluster?](#353-how-do-you-design-keys-for-redis-cluster)
- [354: How would you build a global leaderboard with 100 million players?](#354-how-would-you-build-a-global-leaderboard-with-100-million-players)
- [355: How would you design a rate limiter for a large API gateway?](#355-how-would-you-design-a-rate-limiter-for-a-large-api-gateway)
- [356: What is the Redlock algorithm?](#356-what-is-the-redlock-algorithm)
- [357: What are the criticisms of Redlock?](#357-what-are-the-criticisms-of-redlock)
- [358: What is a fencing token?](#358-what-is-a-fencing-token)
- [359: How would you design a reliable job queue on Redis streams?](#359-how-would-you-design-a-reliable-job-queue-on-redis-streams)
- [360: How do you handle poison messages in a stream?](#360-how-do-you-handle-poison-messages-in-a-stream)
- [361: What does at-least-once delivery mean in Redis streams, and how do you get exactly-once effects?](#361-what-does-at-least-once-delivery-mean-in-redis-streams-and-how-do-you-get-exactly-once-effects)
- [362: How do streams compare to Kafka?](#362-how-do-streams-compare-to-kafka)
- [363: How do you scale a stream beyond one node?](#363-how-do-you-scale-a-stream-beyond-one-node)
- [364: How does consumer group lag work?](#364-how-does-consumer-group-lag-work)
- [365: How would you design a session store for millions of users?](#365-how-would-you-design-a-session-store-for-millions-of-users)
- [366: How do you implement "log out from all devices"?](#366-how-do-you-implement-log-out-from-all-devices)
- [367: How do you cache data that is expensive to compute and must never be stale for long?](#367-how-do-you-cache-data-that-is-expensive-to-compute-and-must-never-be-stale-for-long)
- [368: What is probabilistic early expiration?](#368-what-is-probabilistic-early-expiration)
- [369: How do you keep a cache consistent with the database in a write-heavy system?](#369-how-do-you-keep-a-cache-consistent-with-the-database-in-a-write-heavy-system)
- [370: How do you warm a cache after a restart or a deploy?](#370-how-do-you-warm-a-cache-after-a-restart-or-a-deploy)
- [371: How do you handle multi-region setups with Redis?](#371-how-do-you-handle-multi-region-setups-with-redis)
- [372: What are CRDTs in Active-Active Redis?](#372-what-are-crdts-in-active-active-redis)
- [373: What is client-side caching invalidation like at scale?](#373-what-is-client-side-caching-invalidation-like-at-scale)
- [374: How does Redis handle many clients reading a key that a client is tracking in OPTIN mode?](#374-how-does-redis-handle-many-clients-reading-a-key-that-a-client-is-tracking-in-optin-mode)
- [375: What is the Redis threat model for an exposed server?](#375-what-is-the-redis-threat-model-for-an-exposed-server)
- [376: What are the protected configs in Redis 7+?](#376-what-are-the-protected-configs-in-redis-7)
- [377: How do you design ACLs for least privilege?](#377-how-do-you-design-acls-for-least-privilege)
- [378: What are ACL selectors?](#378-what-are-acl-selectors)
- [379: What does ACL LOG show?](#379-what-does-acl-log-show)
- [380: What security issues have affected Lua scripting?](#380-what-security-issues-have-affected-lua-scripting)
- [381: How do you secure Redis in a multi-tenant setup?](#381-how-do-you-secure-redis-in-a-multi-tenant-setup)
- [382: How do you encrypt data at rest?](#382-how-do-you-encrypt-data-at-rest)
- [383: How should you store sensitive data in Redis?](#383-how-should-you-store-sensitive-data-in-redis)
- [384: How do you upgrade Redis with no downtime?](#384-how-do-you-upgrade-redis-with-no-downtime)
- [385: How do you move from Redis to Valkey or the other way?](#385-how-do-you-move-from-redis-to-valkey-or-the-other-way)
- [386: What are Dragonfly and KeyDB?](#386-what-are-dragonfly-and-keydb)
- [387: How would you design a semantic cache for an LLM app?](#387-how-would-you-design-a-semantic-cache-for-an-llm-app)
- [388: How do you store embeddings in a Redis hash for vector search?](#388-how-do-you-store-embeddings-in-a-redis-hash-for-vector-search)
- [389: What is HNSW and what are its parameters?](#389-what-is-hnsw-and-what-are-its-parameters)
- [390: How do vector sets reduce memory?](#390-how-do-vector-sets-reduce-memory)
- [391: How do you filter results in a vector set search?](#391-how-do-you-filter-results-in-a-vector-set-search)
- [392: How does the Query Engine scale in Redis Cluster?](#392-how-does-the-query-engine-scale-in-redis-cluster)
- [393: How do you keep a search index small and fast?](#393-how-do-you-keep-a-search-index-small-and-fast)
- [394: How do you change a search index schema?](#394-how-do-you-change-a-search-index-schema)
- [395: What happens to data structure invariants when you mix TTLs and big collections?](#395-what-happens-to-data-structure-invariants-when-you-mix-ttls-and-big-collections)
- [396: How does Redis Functions differ in persistence and replication from EVAL?](#396-how-does-redis-functions-differ-in-persistence-and-replication-from-eval)
- [397: How does the HOTKEYS command help with performance problems?](#397-how-does-the-hotkeys-command-help-with-performance-problems)
- [398: What are the new LRM eviction policies for?](#398-what-are-the-new-lrm-eviction-policies-for)
- [399: How does CLUSTER SLOT-STATS help with uneven load?](#399-how-does-cluster-slot-stats-help-with-uneven-load)
- [400: How do you choose between hashes, JSON and the Query Engine for a product catalog?](#400-how-do-you-choose-between-hashes-json-and-the-query-engine-for-a-product-catalog)
- [401: Your Redis CPU is at 100% but ops per second are low. What do you check?](#401-your-redis-cpu-is-at-100-but-ops-per-second-are-low-what-do-you-check)
- [402: Memory keeps growing even though you set TTLs. What could be wrong?](#402-memory-keeps-growing-even-though-you-set-ttls-what-could-be-wrong)
- [403: Why can building Lua scripts with string concatenation cause memory problems?](#403-why-can-building-lua-scripts-with-string-concatenation-cause-memory-problems)
- [404: Replicas keep doing full syncs in a loop. Why?](#404-replicas-keep-doing-full-syncs-in-a-loop-why)
- [405: After a failover, some recent writes are missing. Why?](#405-after-a-failover-some-recent-writes-are-missing-why)
- [406: Clients get "LOADING Redis is loading the dataset in memory" errors. What does it mean?](#406-clients-get-loading-redis-is-loading-the-dataset-in-memory-errors-what-does-it-mean)
- [407: Your app sees random timeouts to Redis but Redis latency looks fine. What do you check?](#407-your-app-sees-random-timeouts-to-redis-but-redis-latency-looks-fine-what-do-you-check)
- [408: How do you find out which client is sending bad traffic?](#408-how-do-you-find-out-which-client-is-sending-bad-traffic)
- [409: What does CLIENT PAUSE do and when would you use it?](#409-what-does-client-pause-do-and-when-would-you-use-it)
- [410: How would you do a planned failover with no data loss?](#410-how-would-you-do-a-planned-failover-with-no-data-loss)
- [411: What does the FAILOVER command do?](#411-what-does-the-failover-command-do)
- [412: How do you test that your app handles Redis failover?](#412-how-do-you-test-that-your-app-handles-redis-failover)
- [413: How should clients retry commands safely?](#413-how-should-clients-retry-commands-safely)
- [414: What happens if you run a blocking command on a shared connection?](#414-what-happens-if-you-run-a-blocking-command-on-a-shared-connection)
- [415: How do keyspace notifications behave in Redis Cluster?](#415-how-do-keyspace-notifications-behave-in-redis-cluster)
- [416: Why do expired events arrive late?](#416-why-do-expired-events-arrive-late)
- [417: What is the difference between a primary's view and a replica's view of time-based data?](#417-what-is-the-difference-between-a-primarys-view-and-a-replicas-view-of-time-based-data)
- [418: How do you avoid the thundering herd when a Redis node restarts?](#418-how-do-you-avoid-the-thundering-herd-when-a-redis-node-restarts)
- [419: How would you design a real-time "who is online" feature?](#419-how-would-you-design-a-real-time-who-is-online-feature)
- [420: How would you design a ride-sharing driver location service?](#420-how-would-you-design-a-ride-sharing-driver-location-service)
- [421: How would you count unique visitors per page per day for millions of pages?](#421-how-would-you-count-unique-visitors-per-page-per-day-for-millions-of-pages)
- [422: How would you implement a "trending" list of topics?](#422-how-would-you-implement-a-trending-list-of-topics)
- [423: How would you build a shopping cart in Redis?](#423-how-would-you-build-a-shopping-cart-in-redis)
- [424: How would you build a flash sale inventory counter that never oversells?](#424-how-would-you-build-a-flash-sale-inventory-counter-that-never-oversells)
- [425: How would you implement a distributed counter that handles millions of increments per second?](#425-how-would-you-implement-a-distributed-counter-that-handles-millions-of-increments-per-second)
- [426: How would you implement a job scheduler that runs cron-like tasks only once across many servers?](#426-how-would-you-implement-a-job-scheduler-that-runs-cron-like-tasks-only-once-across-many-servers)
- [427: How do you handle the clock in distributed algorithms on Redis?](#427-how-do-you-handle-the-clock-in-distributed-algorithms-on-redis)
- [428: What is the cost of a full sync on a big primary?](#428-what-is-the-cost-of-a-full-sync-on-a-big-primary)
- [429: How do you back up a large Redis instance without affecting latency?](#429-how-do-you-back-up-a-large-redis-instance-without-affecting-latency)
- [430: How do you recover from a corrupted AOF or RDB file?](#430-how-do-you-recover-from-a-corrupted-aof-or-rdb-file)
- [431: How do you replay or inspect the AOF to find out who changed a key?](#431-how-do-you-replay-or-inspect-the-aof-to-find-out-who-changed-a-key)
- [432: Why can SORT be dangerous?](#432-why-can-sort-be-dangerous)
- [433: What are Redis modules?](#433-what-are-redis-modules)
- [434: How does Redis handle very large numbers of databases or keys for expiration?](#434-how-does-redis-handle-very-large-numbers-of-databases-or-keys-for-expiration)
- [435: How does the hz setting affect Redis?](#435-how-does-the-hz-setting-affect-redis)
- [436: What are the trade-offs of using Redis as the primary database?](#436-what-are-the-trade-offs-of-using-redis-as-the-primary-database)
- [437: How would you migrate a large Redis setup from standalone to Cluster?](#437-how-would-you-migrate-a-large-redis-setup-from-standalone-to-cluster)
- [438: How do you measure Redis performance correctly?](#438-how-do-you-measure-redis-performance-correctly)
- [439: How does pipelining interact with Redis Cluster?](#439-how-does-pipelining-interact-with-redis-cluster)
- [440: How do you choose the number of shards and replicas?](#440-how-do-you-choose-the-number-of-shards-and-replicas)
- [441: How do you handle a cross-slot operation that you can't avoid?](#441-how-do-you-handle-a-cross-slot-operation-that-you-cant-avoid)
- [442: What are the differences between RESP2 and RESP3 that affect client code?](#442-what-are-the-differences-between-resp2-and-resp3-that-affect-client-code)
- [443: How would you design caching for a GraphQL or REST API with many query variations?](#443-how-would-you-design-caching-for-a-graphql-or-rest-api-with-many-query-variations)
- [444: How do you prevent cache poisoning?](#444-how-do-you-prevent-cache-poisoning)
- [445: How do you do zero-downtime config changes in a large Redis deployment?](#445-how-do-you-do-zero-downtime-config-changes-in-a-large-redis-deployment)
- [446: What would you check before going to production with Redis?](#446-what-would-you-check-before-going-to-production-with-redis)
- [447: How do you explain the CAP trade-off Redis makes?](#447-how-do-you-explain-the-cap-trade-off-redis-makes)
- [448: When would you not use Redis?](#448-when-would-you-not-use-redis)
- [449: What changed in Redis 8 that matters for an interview?](#449-what-changed-in-redis-8-that-matters-for-an-interview)
- [450: How would you explain Redis to a non-technical stakeholder in one minute?](#450-how-would-you-explain-redis-to-a-non-technical-stakeholder-in-one-minute)

---

# Easy Questions (1-150)

## 1: What is Redis?

Redis is an in-memory data store. It keeps data in RAM, so reads and writes are very fast, usually well under a millisecond. It is used as a cache, a database, a message broker and a queue.

Unlike a plain key-value store, the values can be different data structures: strings, lists, sets, sorted sets, hashes, streams, JSON documents and more.

## 2: What does the name Redis stand for?

It stands for **RE**mote **DI**ctionary **S**erver. Salvatore Sanfilippo (antirez) started it in 2009 to solve a performance problem in a real-time analytics product.

## 3: What are the most common use cases for Redis?

- Caching database queries, API responses or rendered pages.
- Storing user sessions.
- Rate limiting.
- Leaderboards and rankings (sorted sets).
- Counters and simple analytics.
- Job queues and background tasks.
- Pub/sub and real-time messaging.
- Event logs with streams.
- Distributed locks.
- Vector search and semantic caching for AI apps.

## 4: Why is Redis so fast?

- Data lives in memory, so there is no disk read on the hot path.
- Commands run on one main thread, so there are no locks or context switches between threads for data access.
- It uses an event loop with non-blocking I/O (epoll/kqueue) to serve many clients at once.
- The data structures are simple and well tuned, and small values use compact encodings.
- The protocol (RESP) is simple and cheap to parse.

## 5: Is Redis single-threaded?

Command execution is single-threaded: one main thread runs all commands one after another. That is why each command is atomic.

But Redis is not fully single-threaded. Background threads handle things like freeing big keys, closing files and fsync. Since Redis 6 you can also turn on I/O threads (`io-threads`) to read from and write to sockets in parallel. The commands themselves still run on the main thread.

## 6: What is the default port of Redis?

`6379`. Redis Sentinel uses `26379` by default. In a cluster, each node also opens a cluster bus port, which is the data port plus 10000 (for example `16379`).

## 7: How do you run Redis locally with Docker?

```bash
docker run -d --name redis -p 6379:6379 redis:8
```

Then connect with the CLI inside the container:

```bash
docker exec -it redis redis-cli
```

## 8: What is redis-cli?

`redis-cli` is the command line client that ships with Redis. You can run commands interactively or pass them as arguments.

```bash
redis-cli -h localhost -p 6379
redis-cli SET greeting "hello"
redis-cli -u redis://user:pass@host:6379 PING
```

It also has helpers like `--scan`, `--bigkeys`, `--latency` and `--stat`.

## 9: What does the PING command do?

It checks that the connection works. The server replies `PONG`. If you pass an argument, it echoes it back.

```bash
127.0.0.1:6379> PING
PONG
127.0.0.1:6379> PING hello
"hello"
```

## 10: How do you set and get a value?

```bash
SET user:1:name "Ann"
GET user:1:name   # "Ann"
GET missing       # (nil)
```

`SET` overwrites any existing value and any old TTL on the key.

## 11: What data types does Redis support?

Core types:

- Strings
- Lists
- Sets
- Sorted sets
- Hashes
- Streams
- Bitmaps and bitfields (built on strings)
- HyperLogLog
- Geospatial indexes (built on sorted sets)

Added in Redis 8 as part of the main server: JSON, time series, vector sets, and probabilistic types (Bloom filter, Cuckoo filter, Count-min sketch, Top-K, t-digest).

## 12: What is a Redis string?

A string is the simplest type. It holds a sequence of bytes up to 512 MB. It can store text, numbers, serialized JSON or binary data like images. If the string looks like an integer, you can use commands like `INCR` on it.

## 13: What does binary-safe mean in Redis?

It means Redis does not care what bytes are in a key or value. It stores the length separately, so values can contain any bytes, including `\0`. You can store a JPEG or a protobuf message the same way you store `"hello"`.

## 14: How do you delete a key?

```bash
DEL user:1:name
DEL key1 key2 key3   # returns the number of keys removed
```

For big keys, use `UNLINK` instead. It removes the key right away but frees the memory in a background thread.

## 15: What is the difference between DEL and UNLINK?

Both remove the key from the keyspace immediately. `DEL` frees the memory on the main thread, which can block Redis for a while if the value is a huge list or hash. `UNLINK` frees the memory in a background thread, so the main thread stays free. For small values there is almost no difference.

## 16: How do you check if a key exists?

```bash
EXISTS user:1         # 1 or 0
EXISTS a b c          # number of existing keys
```

If you pass the same key twice, it is counted twice.

## 17: How do you set an expiration on a key?

```bash
SET session:abc "data" EX 3600   # expire in 3600 seconds
EXPIRE cart:42 600               # set TTL on an existing key
PEXPIRE cart:42 600000           # same, in milliseconds
EXPIREAT promo 1767225600        # expire at a Unix timestamp
```

When the TTL runs out, Redis deletes the key.

## 18: How do you check how much time a key has left?

```bash
TTL session:abc    # seconds left
PTTL session:abc   # milliseconds left
```

`TTL` returns `-1` if the key exists but has no expiration, and `-2` if the key does not exist.

## 19: How do you remove an expiration from a key?

```bash
PERSIST session:abc
```

After that the key lives until you delete it. Running `SET` on the key without `KEEPTTL` also removes the TTL.

## 20: What does EXPIRETIME return?

`EXPIRETIME` (Redis 7.0+) returns the absolute Unix time, in seconds, when the key will expire. `PEXPIRETIME` returns it in milliseconds. Like `TTL`, it returns `-1` for keys with no expiration and `-2` for missing keys.

## 21: What options does the SET command have?

```bash
SET key value EX 60       # TTL in seconds
SET key value PX 60000    # TTL in milliseconds
SET key value EXAT 1767225600  # expire at Unix time (seconds)
SET key value NX          # only set if the key does not exist
SET key value XX          # only set if the key already exists
SET key value KEEPTTL     # keep the current TTL
SET key value GET         # return the old value
```

You can combine them, for example `SET lock:job1 token NX PX 30000`.

## 22: What is SETNX and what should you use instead?

`SETNX key value` sets the key only if it does not exist. It is an old command. Today you use `SET key value NX`, because it lets you add a TTL in the same atomic command (`SET key value NX EX 30`). With `SETNX` you need a separate `EXPIRE`, and if the client crashes in between, the key never expires.

## 23: How do INCR and DECR work?

They treat the string value as a 64-bit signed integer and add or subtract 1. If the key does not exist, it starts from 0.

```bash
INCR page:views      # 1
INCR page:views      # 2
INCRBY page:views 10 # 12
DECR page:views      # 11
DECRBY page:views 5  # 6
```

If the value is not an integer, you get an error.

## 24: Are INCR operations safe when many clients run them at once?

Yes. Each command runs to completion before the next one starts, so `INCR` is atomic. If 100 clients each run `INCR counter` once, the counter ends at 100. This is why Redis is a common choice for counters.

## 25: How do you work with floating point numbers?

Use `INCRBYFLOAT`:

```bash
SET balance 10.50
INCRBYFLOAT balance 0.25   # "10.75"
INCRBYFLOAT balance -5     # "5.75"
```

There is no `DECRBYFLOAT`. You pass a negative number instead.

## 26: How do MSET and MGET work?

They set or get several keys in one round trip.

```bash
MSET user:1:name Ann user:2:name Bob
MGET user:1:name user:2:name user:3:name
# 1) "Ann"
# 2) "Bob"
# 3) (nil)
```

`MSET` is atomic: all keys are set at once. `MSETNX` sets all keys only if none of them exist.

## 27: What do APPEND and STRLEN do?

`APPEND` adds text to the end of a string and returns the new length. If the key does not exist, it creates it. `STRLEN` returns the length in bytes.

```bash
APPEND log "line1;"   # 6
APPEND log "line2;"   # 12
STRLEN log            # 12
```

## 28: What are GETRANGE and SETRANGE?

`GETRANGE` returns part of a string by byte offset. `SETRANGE` overwrites part of a string starting at an offset.

```bash
SET msg "Hello World"
GETRANGE msg 0 4        # "Hello"
SETRANGE msg 6 "Redis"
GET msg                 # "Hello Redis"
```

## 29: What do GETDEL and GETEX do?

- `GETDEL key` returns the value and deletes the key in one step. Useful for one-time tokens.
- `GETEX key EX 60` returns the value and changes its TTL. You can also use `PERSIST` with it to remove the TTL. Useful for sliding sessions.

Both were added in Redis 6.2.

## 30: What is a Redis list?

A list is an ordered collection of strings, kept in insertion order. You can push and pop from both ends fast (O(1)). Lists work well for queues, stacks and "latest N items" feeds.

```bash
RPUSH tasks "a" "b" "c"
LRANGE tasks 0 -1   # a b c
```

## 31: What is the difference between LPUSH and RPUSH?

`LPUSH` adds items to the head (left). `RPUSH` adds to the tail (right).

```bash
LPUSH l 1 2 3   # list is 3 2 1
RPUSH r 1 2 3   # list is 1 2 3
```

`LPUSHX` and `RPUSHX` only push if the list already exists.

## 32: How do LPOP and RPOP work?

They remove and return an item from the head or tail. Since Redis 6.2 you can pop several at once with a count.

```bash
RPUSH q a b c d
LPOP q      # "a"
LPOP q 2    # "b" "c"
RPOP q      # "d"
```

When the last item is removed, the key is deleted.

## 33: How do you use a list as a queue and as a stack?

- Queue (FIFO): push on one side, pop from the other. `RPUSH` + `LPOP`.
- Stack (LIFO): push and pop on the same side. `LPUSH` + `LPOP`.

## 34: How does LRANGE work?

`LRANGE key start stop` returns items between two indexes, both included. Negative indexes count from the end, so `-1` is the last item.

```bash
LRANGE feed 0 9     # first 10 items
LRANGE feed 0 -1    # whole list
LRANGE feed -3 -1   # last 3 items
```

Be careful with `0 -1` on very long lists, since it returns everything.

## 35: How do you get the length of a list?

```bash
LLEN tasks
```

It is O(1) and returns 0 if the key does not exist.

## 36: What does LTRIM do?

`LTRIM` keeps only the items in a given range and drops the rest. A common pattern is a capped list of the latest N items:

```bash
LPUSH recent:user:1 "item-99"
LTRIM recent:user:1 0 99   # keep the newest 100
```

## 37: What are LINDEX, LSET and LINSERT?

- `LINDEX key index` reads an item by position.
- `LSET key index value` replaces an item at a position.
- `LINSERT key BEFORE|AFTER pivot value` inserts a value next to the first item equal to `pivot`.

All of these are O(N) in the worst case, because Redis has to walk the list.

## 38: How do you remove specific values from a list?

`LREM key count value`:

- `count > 0`: remove the first `count` matches from the head.
- `count < 0`: remove `count` matches from the tail.
- `count = 0`: remove all matches.

```bash
LREM tasks 0 "done-task"
```

## 39: What is BLPOP?

`BLPOP` is a blocking pop. If the list is empty, the client waits until an item arrives or the timeout ends. This lets workers wait for jobs without polling.

```bash
BLPOP jobs 5    # wait up to 5 seconds
BLPOP jobs 0    # wait forever
```

It returns the key name and the value. `BRPOP` is the same from the tail.

## 40: What does LMOVE do?

`LMOVE source destination LEFT|RIGHT LEFT|RIGHT` pops an item from one list and pushes it to another in one atomic step. `BLMOVE` is the blocking version. It replaced the older `RPOPLPUSH`.

```bash
LMOVE jobs processing LEFT RIGHT
```

It is the base of the reliable queue pattern, where a job stays in a "processing" list until a worker confirms it.

## 41: What is a Redis set?

A set is an unordered collection of unique strings. Adding an item that already exists does nothing. Checking membership is O(1).

```bash
SADD tags:post:1 redis cache db
SADD tags:post:1 redis       # 0, already there
SMEMBERS tags:post:1
SISMEMBER tags:post:1 cache  # 1
```

## 42: What set operations does Redis support?

```bash
SINTER a b        # items in both
SUNION a b        # items in either
SDIFF a b         # items in a but not in b
SINTERSTORE dst a b
SUNIONSTORE dst a b
SDIFFSTORE dst a b
```

For example, "friends in common" is `SINTER friends:1 friends:2`.

## 43: How do you count and sample items in a set?

```bash
SCARD tags            # number of items
SRANDMEMBER tags 3    # 3 random items, not removed
SPOP tags             # remove and return a random item
SMISMEMBER tags a b c # check several items at once
```

`SPOP` is handy for things like picking a random winner.

## 44: How do you remove items from a set or move them to another set?

```bash
SREM online:users user:7
SMOVE pending done job:15
```

`SMOVE` is atomic, so the item is never in both sets or in neither.

## 45: What is a sorted set?

A sorted set is like a set, but each member has a numeric score. Members are unique and kept ordered by score (and by member name when scores are equal). Adding and removing is O(log N). It is the go-to type for leaderboards, priority queues and time-based indexes.

```bash
ZADD leaderboard 100 ann 250 bob 180 cid
ZRANGE leaderboard 0 -1 WITHSCORES
```

## 46: How do you get the top players from a sorted set?

```bash
ZRANGE leaderboard 0 9 REV WITHSCORES
```

`REV` returns the highest scores first. Before Redis 6.2 people used `ZREVRANGE`, which still works but is deprecated.

## 47: How do you get a member's score and rank?

```bash
ZSCORE leaderboard bob      # "250"
ZRANK leaderboard bob       # rank from lowest, starts at 0
ZREVRANK leaderboard bob    # rank from highest, starts at 0
```

Since Redis 7.2, `ZRANK` and `ZREVRANK` accept `WITHSCORE` to return the score too.

## 48: How do you increase a member's score?

```bash
ZINCRBY leaderboard 15 ann
```

If the member does not exist, it is added with that score. This is how you add points to a player.

## 49: How do you query a sorted set by score range?

```bash
ZRANGE scores 50 100 BYSCORE              # score between 50 and 100
ZRANGE scores (50 100 BYSCORE             # 50 excluded
ZRANGE scores -inf +inf BYSCORE LIMIT 0 10
ZCOUNT scores 50 100                      # how many
```

Older code uses `ZRANGEBYSCORE`, which still works.

## 50: How do you remove members from a sorted set?

```bash
ZREM leaderboard ann
ZREMRANGEBYSCORE events -inf 1700000000   # by score
ZREMRANGEBYRANK leaderboard 0 -101        # keep only top 100
```

`ZCARD` gives the number of members.

## 51: What options does ZADD support?

```bash
ZADD lb NX 10 ann     # only add new members, never update
ZADD lb XX 20 ann     # only update existing members
ZADD lb GT 15 ann     # update only if the new score is greater
ZADD lb LT 5 ann      # update only if the new score is lower
ZADD lb CH 30 ann     # return number of changed members, not just added
ZADD lb INCR 5 ann    # act like ZINCRBY
```

`GT` is useful for "keep the best score" leaderboards.

## 52: What is a Redis hash?

A hash maps field names to values inside one key. It is a good fit for objects like a user or a product.

```bash
HSET user:1 name "Ann" email "ann@example.com" age 31
HGET user:1 name       # "Ann"
HGETALL user:1
```

Small hashes use a compact encoding, so they take little memory.

## 53: What are the main hash commands?

```bash
HSET user:1 city "Berlin"
HMGET user:1 name city
HDEL user:1 age
HEXISTS user:1 email
HLEN user:1
HKEYS user:1
HVALS user:1
HINCRBY user:1 logins 1
HINCRBYFLOAT user:1 balance 2.5
HSETNX user:1 created_at 1767225600
```

`HMSET` is deprecated. `HSET` accepts several field-value pairs.

## 54: When should you use a hash instead of a JSON string?

Use a hash when you often read or update single fields, because you can change one field without reading and rewriting the whole object. Use a JSON string when you always read and write the object as a whole, or when it has nested data. If you need nested data and partial updates, use the JSON data type (`JSON.SET`, `JSON.GET`).

## 55: Can you set a TTL on a single hash field?

Yes, since Redis 7.4.

```bash
HSET session:1 token abc csrf xyz
HEXPIRE session:1 300 FIELDS 1 csrf
HTTL session:1 FIELDS 1 csrf
HPERSIST session:1 FIELDS 1 csrf
```

Redis 8.0 added `HSETEX` and `HGETEX` to set or read fields and change their TTL in one command, and `HGETDEL` to read and delete fields.

## 56: What is a Redis stream?

A stream is an append-only log. Each entry has a unique ID and a set of field-value pairs. You can read entries by ID range, wait for new ones, and use consumer groups to split work between workers. Streams are like a small Kafka inside Redis.

```bash
XADD orders * user 1 total 49.90
XRANGE orders - +
```

## 57: What does the * mean in XADD?

It tells Redis to generate the entry ID. The ID looks like `1767225600123-0`: a millisecond timestamp and a sequence number for entries in the same millisecond. IDs always increase.

## 58: How do you read new entries from a stream?

```bash
XREAD COUNT 10 BLOCK 5000 STREAMS orders $
```

`$` means "only entries added after I start waiting". `BLOCK 5000` waits up to 5 seconds. To continue from where you stopped, pass the last ID you saw instead of `$`.

## 59: What is pub/sub in Redis?

Pub/sub lets clients send messages to channels and other clients receive them in real time.

```bash
# client 1
SUBSCRIBE news

# client 2
PUBLISH news "hello"
```

Messages are not stored. If no one is subscribed, the message is lost. A connection in subscribe mode can only run subscribe-related commands (with RESP2).

## 60: What is the difference between SUBSCRIBE and PSUBSCRIBE?

`SUBSCRIBE` listens to exact channel names. `PSUBSCRIBE` listens to glob patterns.

```bash
PSUBSCRIBE news.*    # matches news.sport, news.tech
```

## 61: What is a bitmap?

A bitmap is a string treated as an array of bits. You set and read single bits by offset. It is very compact for yes/no data, like "did user N log in today?".

```bash
SETBIT logins:2026-11-05 1001 1
GETBIT logins:2026-11-05 1001   # 1
BITCOUNT logins:2026-11-05      # users who logged in
```

10 million users fit in about 1.2 MB.

## 62: What is HyperLogLog?

HyperLogLog is a structure that counts unique items approximately, using at most about 12 KB per key, no matter how many items you add. The standard error is around 0.81%.

```bash
PFADD visitors:today user1 user2 user3 user1
PFCOUNT visitors:today    # 3
PFMERGE visitors:week visitors:mon visitors:tue
```

You cannot get the items back, only the count.

## 63: How do you store and search locations?

Use the geo commands. They store coordinates in a sorted set.

```bash
GEOADD shops 13.405 52.52 shop:1 13.41 52.53 shop:2
GEOSEARCH shops FROMLONLAT 13.40 52.52 BYRADIUS 2 km ASC WITHDIST
GEODIST shops shop:1 shop:2 km
GEOPOS shops shop:1
```

Longitude comes first, then latitude.

## 64: What is the JSON data type?

It lets you store JSON documents and read or change parts of them with JSONPath, without sending the whole document back and forth. In Redis 8 it is built in.

```bash
JSON.SET user:1 $ '{"name":"Ann","tags":["admin"],"age":31}'
JSON.GET user:1 $.name
JSON.NUMINCRBY user:1 $.age 1
JSON.ARRAPPEND user:1 $.tags '"editor"'
```

## 65: What is a vector set?

A vector set is a data type added in Redis 8.0. It stores elements with a vector (embedding) each, and lets you find the most similar elements.

```bash
VADD items VALUES 3 0.1 0.2 0.3 item:1
VADD items VALUES 3 0.1 0.25 0.31 item:2
VSIM items VALUES 3 0.1 0.2 0.3 COUNT 5 WITHSCORES
```

It is used for recommendations and semantic search.

## 66: What is the time series data type?

It stores timestamped numeric samples, like metrics or sensor data. It supports retention, labels, and aggregation queries.

```bash
TS.CREATE temp:room1 RETENTION 86400000 LABELS room 1
TS.ADD temp:room1 * 21.5
TS.RANGE temp:room1 - + AGGREGATION avg 60000
```

## 67: What is a Bloom filter?

A Bloom filter tells you if an item is "definitely not there" or "probably there". It uses little memory but can give false positives, never false negatives.

```bash
BF.RESERVE emails 0.01 1000000
BF.ADD emails ann@example.com
BF.EXISTS emails ann@example.com   # 1
BF.EXISTS emails bob@example.com   # 0 (almost always)
```

Common use: checking if a username is taken before hitting the database.

## 68: How do you list keys?

Use `SCAN`, not `KEYS`, on any real server.

```bash
SCAN 0 MATCH user:* COUNT 100
```

`SCAN` returns a cursor and a batch of keys. You call it again with the new cursor until the cursor is `0`.

## 69: Why should you not use KEYS in production?

`KEYS pattern` walks the entire keyspace in one go. With millions of keys it blocks Redis for a long time, and every other client waits. `SCAN` does the same work in small steps, so other commands can run in between.

## 70: What does the TYPE command do?

It returns the type of the value stored at a key: `string`, `list`, `set`, `zset`, `hash`, `stream`, or a module type like `ReJSON-RL`. It returns `none` if the key does not exist.

## 71: How do you rename a key?

```bash
RENAME old new      # overwrites "new" if it exists
RENAMENX old new    # only if "new" does not exist
```

The TTL moves with the key. In a cluster, both keys must be in the same hash slot.

## 72: What does COPY do?

`COPY source destination` copies a value to a new key (Redis 6.2+). Add `REPLACE` to overwrite the destination, or `DB n` to copy into another database.

```bash
COPY config:v1 config:v2
```

## 73: What are Redis databases?

A standalone Redis server has 16 numbered databases by default (0 to 15). They are separate keyspaces. You switch with `SELECT`.

```bash
SELECT 1
```

Redis Cluster only supports database 0. Most teams use one database and key prefixes instead.

## 74: What is the difference between FLUSHDB and FLUSHALL?

`FLUSHDB` deletes all keys in the current database. `FLUSHALL` deletes all keys in all databases. Both accept `ASYNC` to free memory in the background. They are dangerous in production, so many teams block them with ACLs.

## 75: How do you count the keys in a database?

```bash
DBSIZE
```

It is O(1). `INFO keyspace` shows the key count and keys with TTL per database.

## 76: What is a good key naming convention?

Use a prefix with colons as separators, from general to specific:

```
user:1001
user:1001:sessions
order:2026:11:05:abc123
cache:product:42
```

It makes keys readable, easy to scan with `MATCH`, and easy to split by app or team. Keep keys short but clear, since very long keys waste memory.

## 77: How big can a key or a value be?

Both a key and a string value can be up to 512 MB. In practice you should keep keys short and values small. Big values slow down the network, block the main thread on read or delete, and make replication harder.

## 78: What is RESP?

RESP (REdis Serialization Protocol) is the protocol clients use to talk to Redis. It is a simple text-based format with type prefixes like `+` for simple strings, `-` for errors, `:` for integers, `$` for bulk strings and `*` for arrays. RESP3, added in Redis 6, adds more types such as maps, sets, doubles and push messages.

## 79: How do you connect to Redis from Node.js?

With `node-redis` (the official client):

```js
import { createClient } from "redis";

const client = createClient({ url: "redis://localhost:6379" });
client.on("error", (err) => console.error("Redis error", err));
await client.connect();

await client.set("greeting", "hello");
console.log(await client.get("greeting"));
```

With `ioredis`:

```js
import Redis from "ioredis";

const redis = new Redis("redis://localhost:6379");
await redis.set("greeting", "hello");
console.log(await redis.get("greeting"));
```

## 80: How do you connect to Redis from Python?

```python
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
r.set("greeting", "hello")
print(r.get("greeting"))  # hello
```

Without `decode_responses=True` you get `bytes` back instead of `str`.

## 81: What is caching?

Caching is keeping a copy of data in a fast place so you do not have to fetch or compute it again. Redis is often put in front of a database: the app checks Redis first, and only goes to the database on a miss.

## 82: What is the cache-aside pattern?

The app manages the cache itself:

1. Read from Redis.
2. On a hit, return it.
3. On a miss, read from the database, write it to Redis with a TTL, and return it.

```js
async function getUser(id) {
  const key = `user:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const user = await db.users.findById(id);
  await redis.set(key, JSON.stringify(user), "EX", 300);
  return user;
}
```

It is the most common caching pattern.

## 83: What is a cache hit and a cache miss?

A hit means the data was found in the cache. A miss means it was not, so you had to go to the source. The hit ratio (`keyspace_hits / (keyspace_hits + keyspace_misses)` from `INFO stats`) shows how useful the cache is.

## 84: Why should cached keys have a TTL?

- Data in the cache does not stay stale forever.
- Unused data goes away, so memory does not fill up.
- If your invalidation code has a bug, the TTL limits the damage.

Pick the TTL based on how fresh the data needs to be.

## 85: How is Redis used as a session store?

Each session is a key like `session:<id>` with a TTL. The value is a hash or a JSON string with the user data. Every app server reads the same Redis, so users stay logged in no matter which server handles the request. When the session expires, Redis deletes it.

## 86: What is the difference between Redis and Memcached?

- Redis has many data types. Memcached only has strings.
- Redis can persist data to disk and replicate it. Memcached cannot.
- Redis has pub/sub, streams, Lua scripting, transactions and clustering built in.
- Memcached is multi-threaded and very simple, which can be fine for a plain cache.

For most new projects people choose Redis (or a Redis-compatible store).

## 87: Can Redis be used as a primary database?

It can, if the data fits in memory and you set up persistence and replication properly. Some apps use it as the main store for things like sessions, counters, leaderboards or real-time data. But it is not a relational database: no joins, no complex queries (unless you use the Query Engine), and durability depends on your persistence settings. Most teams use it alongside a main database.

## 88: What is persistence in Redis?

Persistence means saving data to disk so it survives a restart. Redis has two options:

- **RDB**: point-in-time snapshots of the whole dataset.
- **AOF**: a log of every write command.

You can use one, both, or none (for a pure cache).

## 89: What is an RDB snapshot?

An RDB file (`dump.rdb`) is a compact binary copy of all data at one moment. Redis creates it by forking a child process that writes the file while the parent keeps serving clients. It is fast to load and good for backups, but you can lose writes made after the last snapshot.

## 90: What is AOF?

AOF (Append Only File) logs every write command. On restart, Redis replays the log to rebuild the data. With `appendfsync everysec` (the default when AOF is on) you lose at most about one second of writes. AOF files are larger than RDB and slower to load.

## 91: What is the difference between SAVE and BGSAVE?

`SAVE` creates an RDB snapshot on the main thread and blocks all clients until it is done. `BGSAVE` forks a child process to do it in the background. In production you almost always use `BGSAVE`. `LASTSAVE` returns the time of the last successful save.

## 92: What is the redis.conf file?

It is the main config file. You start Redis with it like `redis-server /etc/redis/redis.conf`. It sets things like port, bind address, password, persistence, memory limit and eviction policy. Many settings can also be changed at runtime with `CONFIG SET`.

## 93: How do you read and change config at runtime?

```bash
CONFIG GET maxmemory
CONFIG SET maxmemory 2gb
CONFIG REWRITE   # save current settings to redis.conf
```

Without `CONFIG REWRITE`, changes made with `CONFIG SET` are lost after a restart.

## 94: What does the INFO command show?

`INFO` returns server stats grouped in sections: `server`, `clients`, `memory`, `persistence`, `stats`, `replication`, `cpu`, `keyspace` and more.

```bash
INFO memory
INFO replication
```

It is the main source for monitoring tools.

## 95: What is maxmemory?

`maxmemory` is the memory limit for data. When Redis reaches it, it either removes keys based on the eviction policy or rejects writes with an error. Without a limit, Redis can use all RAM and the OS may kill it.

```
maxmemory 4gb
maxmemory-policy allkeys-lru
```

## 96: What is eviction?

Eviction is Redis removing keys on its own when it reaches `maxmemory`, to make room for new writes. Which keys go depends on `maxmemory-policy`, for example least recently used (`allkeys-lru`) or least frequently used (`allkeys-lfu`). The default is `noeviction`, which removes nothing and returns errors on writes.

## 97: How do you set a password on Redis?

The old way is `requirepass` in redis.conf, which sets the password of the `default` user. The modern way is ACL users:

```bash
ACL SETUSER app on >s3cret ~app:* +@all -@dangerous
```

Clients then log in with `AUTH app s3cret`.

## 98: What are ACLs in Redis?

ACLs (Access Control Lists), added in Redis 6, let you create several users with their own passwords and permissions. You can limit which commands a user can run and which keys they can touch.

```bash
ACL SETUSER reporter on >pass ~stats:* +@read
ACL LIST
ACL WHOAMI
```

## 99: What is protected mode?

Protected mode is on by default. If Redis has no password and is not bound to specific addresses, it only accepts connections from localhost. It stops people from accidentally exposing an open Redis to the internet.

## 100: What is replication in Redis?

Replication copies data from a primary (master) to one or more replicas. The replicas get every write and can serve reads. If the primary fails, a replica can be promoted. Replication is asynchronous by default.

```bash
REPLICAOF 10.0.0.1 6379
```

## 101: What is Redis Sentinel?

Sentinel is a separate process that watches a primary and its replicas. If the primary goes down, Sentinels agree on it and promote a replica to be the new primary. Clients ask Sentinel for the current primary address. You usually run at least three Sentinels so they can vote.

## 102: What is Redis Cluster?

Redis Cluster splits data across several primary nodes, each with its own replicas. Keys are mapped to 16384 hash slots, and each primary owns a range of slots. It gives you more memory and write throughput than one server, plus automatic failover.

## 103: What is the difference between Sentinel and Cluster?

- **Sentinel**: one primary holds all the data. You get high availability, but not more capacity.
- **Cluster**: data is split over many primaries. You get high availability and you can scale writes and memory.

If your data fits on one machine, Sentinel (or a managed service) is simpler.

## 104: What is a transaction in Redis?

A transaction groups commands with `MULTI` and `EXEC`. All queued commands run one after another without other clients' commands in between.

```bash
MULTI
INCR orders:count
LPUSH orders:recent order:99
EXEC
```

`DISCARD` cancels the queued commands.

## 105: Does a Redis transaction roll back on error?

No. If a command fails at runtime (for example `INCR` on a list), the other commands still run. Redis only aborts the whole transaction if there is an error while queueing, like a wrong number of arguments. You need to check each reply in the `EXEC` result.

## 106: What is pipelining?

Pipelining means sending several commands without waiting for each reply, then reading all replies at the end. It cuts the number of network round trips.

```js
const results = await redis.pipeline().set("a", 1).incr("a").get("a").exec();
// [[null, "OK"], [null, 2], [null, "2"]]
```

Unlike a transaction, other clients' commands can run between the piped commands.

## 107: What is Lua scripting in Redis?

You can send a Lua script that Redis runs on the server. The whole script runs atomically, so no other command runs in the middle. It lets you do read-check-write logic in one step.

```bash
EVAL "return redis.call('GET', KEYS[1])" 1 user:1:name
```

## 108: What are Redis Functions?

Functions (Redis 7.0+) are Lua code that you load once into the server as a library and call by name. Unlike `EVAL` scripts, they are stored with the data, persisted and replicated.

```bash
FUNCTION LOAD "#!lua name=mylib
redis.register_function('hello', function(keys, args) return 'Hello ' .. args[1] end)"

FCALL hello 0 Ann   # "Hello Ann"
```

## 109: What is Redis Insight?

Redis Insight is a free desktop and web GUI for Redis. You can browse keys, run commands, look at memory usage, read the slow log and work with JSON, search indexes and streams. It is handy for debugging.

## 110: What does MONITOR do?

`MONITOR` streams every command the server receives, in real time. It is useful for debugging in development. Do not leave it running in production: it slows Redis down and can show sensitive data.

## 111: What is the slow log?

The slow log records commands that took longer than a set time to execute (not including network time).

```bash
CONFIG SET slowlog-log-slower-than 10000   # 10 ms, in microseconds
SLOWLOG GET 10
SLOWLOG RESET
```

It helps you find heavy commands like big `HGETALL` or `LRANGE 0 -1`.

## 112: How do you see which clients are connected?

```bash
CLIENT LIST
CLIENT INFO        # current connection
CLIENT KILL ID 42
CLIENT SETNAME worker-1
```

Setting a name on each connection makes `CLIENT LIST` much easier to read.

## 113: What is a distributed lock?

A distributed lock makes sure only one process across many servers does a task at a time. The simple Redis version is:

```bash
SET lock:report token123 NX PX 30000
```

`NX` means only one client gets it. `PX` makes it expire if the holder crashes. To release it, the holder deletes the key only if the value still matches its token.

## 114: How do you build a simple rate limiter?

A fixed window counter:

```js
async function allow(userId, limit = 100) {
  const key = `rate:${userId}:${Math.floor(Date.now() / 60000)}`;
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, 60);
  return count <= limit;
}
```

Each user gets `limit` requests per minute. The key goes away after the window.

## 115: How do you build a leaderboard?

Use a sorted set with the score as the score.

```bash
ZADD game:lb 1500 ann 1720 bob 1600 cid
ZINCRBY game:lb 50 ann
ZRANGE game:lb 0 9 REV WITHSCORES   # top 10
ZREVRANK game:lb ann                # ann's position
```

## 116: How do you build a simple job queue?

Producers `LPUSH` jobs to a list, workers block on `BRPOP`:

```bash
LPUSH jobs '{"type":"email","to":"ann@example.com"}'
BRPOP jobs 0
```

If a worker crashes after popping, the job is lost. For real projects use `BLMOVE` into a processing list, streams with consumer groups, or a library like BullMQ.

## 117: What is a keyspace notification?

Redis can publish a pub/sub message when keys change, for example when a key is set, deleted or expires. It is off by default.

```bash
CONFIG SET notify-keyspace-events Ex
PSUBSCRIBE __keyevent@0__:expired
```

`E` turns on keyevent messages and `x` selects expired events.

## 118: What does OBJECT ENCODING show?

It shows how Redis stores a value internally.

```bash
SET n 123
OBJECT ENCODING n         # "int"
RPUSH l a b
OBJECT ENCODING l         # "listpack"
```

Small values use compact encodings like `listpack` or `intset`, and Redis switches to bigger structures like `hashtable` or `skiplist` when they grow.

## 119: What does TOUCH do?

`TOUCH key [key ...]` updates the last access time of keys without reading them. It matters for LRU eviction and for `OBJECT IDLETIME`. It returns how many keys exist.

## 120: What does RANDOMKEY do?

It returns a random key from the current database, or nil if it is empty. It can be useful when looking at what kind of data is in an unknown database.

## 121: How do you check the server time and Redis version?

```bash
TIME             # Unix seconds and microseconds
INFO server      # redis_version, uptime, os, etc.
```

From the shell, `redis-server --version` or `redis-cli --version`.

## 122: How do you stop a Redis server safely?

```bash
SHUTDOWN
```

By default it saves an RDB snapshot if save points are configured, flushes AOF, and then exits. `SHUTDOWN NOSAVE` skips the save. Killing the process with `kill -9` skips everything and can lose data.

## 123: What does ECHO do?

`ECHO message` returns the same message. It is mostly used to test a connection or a client library.

## 124: What is Redis Open Source, Redis Software and Redis Cloud?

- **Redis Open Source**: the free server you download and run yourself.
- **Redis Software**: the paid self-managed product (formerly Redis Enterprise) with extra features like active-active geo replication.
- **Redis Cloud**: the managed service run by Redis Ltd. on AWS, GCP and Azure.

Cloud providers also have their own managed services, like AWS ElastiCache, Azure Managed Redis and Google Memorystore.

## 125: What is Valkey?

Valkey is a fork of Redis 7.2.4, created under the Linux Foundation in 2024 after Redis changed its license. It stays under the BSD license and is mostly compatible with Redis commands and clients. AWS, Google and others back it, and some managed services now run Valkey under the hood.

## 126: What license is Redis under?

Up to 7.2, Redis was BSD. From 7.4 it was dual licensed under RSALv2 and SSPLv1, which are not OSI open source licenses. Since Redis 8.0 you can also choose AGPLv3, which is an open source license. For most companies that just use Redis in their own app, this changes little. It matters more for companies that sell Redis as a service.

## 127: What was Redis Stack?

Redis Stack was a bundle of Redis plus modules like RedisJSON, RediSearch, RedisTimeSeries and RedisBloom. In Redis 8 these features are part of the main Redis Open Source distribution, so you get JSON, search, time series and probabilistic types without installing anything extra.

## 128: What does WATCH do?

`WATCH` marks keys before a `MULTI`. If any watched key changes before `EXEC`, the transaction is aborted and `EXEC` returns nil. This is optimistic locking: you retry if someone else changed the data.

```bash
WATCH balance:1
GET balance:1
MULTI
SET balance:1 90
EXEC
```

## 129: How do you count unique daily visitors cheaply?

Use HyperLogLog:

```bash
PFADD uv:2026-11-05 user:1 user:2 user:3
PFCOUNT uv:2026-11-05
PFCOUNT uv:2026-11-04 uv:2026-11-05   # union count over two days
```

If you need an exact count and the number of users is small, a set or bitmap works too.

## 130: What does SRANDMEMBER with a negative count do?

A positive count returns up to that many distinct members. A negative count returns exactly that many members and may repeat the same member.

```bash
SRANDMEMBER colors 3    # 3 different items (or fewer if the set is small)
SRANDMEMBER colors -5   # 5 items, may repeat
```

## 131: What does ZRANGE BYLEX do?

When all members have the same score, `BYLEX` lets you query by lexicographic (alphabetical) range. It is used for autocomplete.

```bash
ZADD names 0 anna 0 andrew 0 bob
ZRANGE names [an (ao BYLEX   # andrew, anna
```

`[` means included, `(` means excluded, `-` and `+` mean the lowest and highest values.

## 132: How do you get a random member from a sorted set?

```bash
ZRANDMEMBER leaderboard          # one random member
ZRANDMEMBER leaderboard 3 WITHSCORES
```

It was added in Redis 6.2.

## 133: What do ZPOPMIN and ZPOPMAX do?

They remove and return the members with the lowest or highest score. `BZPOPMIN` and `BZPOPMAX` are blocking versions. They are useful for priority queues.

```bash
ZADD tasks 1 low 10 high 5 mid
ZPOPMAX tasks    # "high" "10"
```

## 134: What does XLEN return?

The number of entries in a stream. It is O(1).

```bash
XLEN orders
```

## 135: How do you limit the size of a stream?

Trim when adding, or trim later:

```bash
XADD events MAXLEN ~ 10000 * type click
XTRIM events MAXLEN ~ 10000
XTRIM events MINID 1767225600000-0
```

The `~` lets Redis trim a bit more loosely, which is much faster.

## 136: What is the difference between a list and a stream for queues?

A list is simple: push, pop, done. Once popped, the item is gone, and there is no built-in acknowledgment. A stream keeps entries, gives each an ID, supports consumer groups, tracks which entries were delivered but not acknowledged, and lets you replay history. Use streams when you need reliable processing or several consumers.

## 137: What does SCAN return when the cursor is 0?

A returned cursor of `0` means the iteration is complete. You always start with cursor `0`, and you stop when Redis gives you `0` back. A batch can be empty even when there are more keys to come, so do not stop on an empty batch.

## 138: Can SCAN return the same key twice?

Yes. If the keyspace changes during the scan (for example, the hash table resizes), a key can show up more than once. Your code should handle duplicates, for example by putting results in a set. A key that exists for the whole scan is always returned at least once.

## 139: What are HSCAN, SSCAN and ZSCAN?

They work like `SCAN`, but iterate over the fields of a hash, the members of a set, or the members of a sorted set. Use them instead of `HGETALL`, `SMEMBERS` or `ZRANGE 0 -1` on big collections.

```bash
HSCAN user:1 0 MATCH addr* COUNT 100
```

## 140: How do you see how much memory a key uses?

```bash
MEMORY USAGE user:1
```

It returns bytes, including some overhead. For a whole picture use `INFO memory` or `redis-cli --bigkeys` and `redis-cli --memkeys`.

## 141: What is the difference between EX and PX?

`EX` sets the TTL in seconds, `PX` in milliseconds. `EXAT` and `PXAT` take an absolute Unix time in seconds or milliseconds.

## 142: What happens to the TTL when you modify a key?

Commands that overwrite the value, like `SET`, `GETSET` or `RENAME` onto the key, clear or replace the TTL. Commands that change the value in place, like `INCR`, `LPUSH`, `HSET` or `APPEND`, keep the TTL. `SET ... KEEPTTL` overwrites the value but keeps the TTL.

## 143: What is the EXPIRE NX option?

Since Redis 7.0, `EXPIRE` has options:

- `NX`: set only if the key has no TTL.
- `XX`: set only if the key already has a TTL.
- `GT`: set only if the new TTL is greater.
- `LT`: set only if the new TTL is smaller.

`INCR key` followed by `EXPIRE key 60 NX` is a clean way to start a counter window.

## 144: How do you check what commands a user can run?

```bash
ACL GETUSER app
ACL CAT              # list command categories
ACL CAT dangerous    # commands in a category
ACL DRYRUN app GET secret:1
```

`ACL DRYRUN` (Redis 7.0+) tells you if a user is allowed to run a command without running it.

## 145: How do you back up Redis?

The simple way is to copy the RDB file. Run `BGSAVE` (or rely on save points), wait until it finishes, then copy `dump.rdb` somewhere safe. With AOF, copy the whole AOF directory. Many teams take backups from a replica so the primary is not affected.

## 146: What happens when Redis restarts?

If persistence is on, Redis loads the data on startup. If AOF is enabled, it loads from AOF, because AOF usually has the most recent data. Otherwise it loads the RDB file. If persistence is off, it starts empty.

## 147: What are good use cases for sets?

- Tags on an item.
- Unique visitors (when the number is not huge).
- Users who liked a post.
- Online users.
- Friends and "friends in common" with `SINTER`.
- Tracking which IDs were already processed.

## 148: What is the difference between a set and a sorted set?

Both keep members unique. A set has no order and no scores. A sorted set has a score per member and keeps them ordered, so you can query by rank or score range. Sorted sets use more memory and most operations are O(log N) instead of O(1).

## 149: Can you nest data structures in Redis?

Not directly. A list cannot contain a hash, for example. Values inside lists, sets and hashes are strings. To model nested data you either serialize it (JSON string), use several keys that reference each other (`user:1`, `user:1:orders`), or use the JSON data type, which supports nested objects and arrays.

## 150: What are common mistakes beginners make with Redis?

- Using `KEYS *` in production.
- Not setting `maxmemory`, or using it as a cache with `noeviction`.
- Forgetting TTLs on cache keys.
- Storing huge values or collections in one key.
- Exposing Redis to the internet without a password.
- Opening a new connection per request instead of reusing one.
- Assuming transactions roll back on errors.

# Moderate Questions (151-300)

## 151: What are the main caching strategies and how do they differ?

- **Cache-aside (lazy loading)**: the app reads the cache, and on a miss loads from the database and fills the cache.
- **Read-through**: the cache layer itself loads from the database on a miss. The app only talks to the cache layer.
- **Write-through**: every write goes to the cache and the database at the same time.
- **Write-behind (write-back)**: writes go to the cache first and are written to the database later in batches.
- **Write-around**: writes go only to the database, and the cache fills on read.

Cache-aside is the most common with Redis because it is simple and the app stays in control.

## 152: How do you keep the cache in sync with the database on updates?

The usual approach is: update the database first, then delete the cache key (not update it). The next read loads fresh data.

```js
async function updateUser(id, data) {
  await db.users.update(id, data);
  await redis.del(`user:${id}`);
}
```

Deleting is safer than writing the new value, because two concurrent writers could otherwise leave the older value in the cache. Keep a TTL as a safety net.

## 153: What is a cache stampede?

A cache stampede (or dog-piling) happens when a popular key expires and many requests miss at the same time. They all hit the database at once to rebuild the same value, which can overload it.

Common fixes:

- A short lock so only one request rebuilds the value while others wait or serve stale data.
- Refreshing the value early before it expires.
- Adding random jitter to TTLs so many keys do not expire at the same moment.

## 154: How do you add TTL jitter and why?

If you cache 10,000 items with exactly 3600 seconds TTL at startup, they all expire together and hit the database together. Adding a random amount spreads them out:

```js
const ttl = 3600 + Math.floor(Math.random() * 300); // 60-65 minutes
await redis.set(key, value, "EX", ttl);
```

## 155: How do you prevent a stampede with a lock?

```js
async function getWithLock(key, loader, ttl = 300) {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const lockKey = `lock:${key}`;
  const gotLock = await redis.set(lockKey, "1", "NX", "PX", 5000);

  if (gotLock) {
    try {
      const value = await loader();
      await redis.set(key, JSON.stringify(value), "EX", ttl);
      return value;
    } finally {
      await redis.del(lockKey);
    }
  }

  // someone else is loading, wait a bit and retry
  await new Promise((r) => setTimeout(r, 100));
  return getWithLock(key, loader, ttl);
}
```

In real code, limit the number of retries.

## 156: What is negative caching?

Caching the fact that something does not exist. If many requests ask for `user:999999` and it is not in the database, each one misses the cache and hits the database. Storing a short-lived marker like `"__none__"` for missing items stops this. Keep the TTL short, so new items show up quickly.

## 157: How do you choose between a string and a hash to cache an object?

- String with JSON: one `GET` and one `SET`, easy to use, works with any shape, but you must rewrite the whole object to change one field.
- Hash: you can read or update one field, increment numbers in place, and small hashes are very memory efficient. But values are flat strings, so nested data needs extra work.

For read-mostly cache entries, a JSON string is usually fine.

## 158: How do you cache API responses in an Express app?

```js
function cache(ttl) {
  return async (req, res, next) => {
    const key = `cache:${req.originalUrl}`;
    const hit = await redis.get(key);
    if (hit) return res.type("json").send(hit);

    const send = res.json.bind(res);
    res.json = (body) => {
      if (res.statusCode === 200) {
        redis.set(key, JSON.stringify(body), "EX", ttl).catch(() => {});
      }
      return send(body);
    };
    next();
  };
}

app.get("/products", cache(60), listProducts);
```

Be careful not to cache responses that depend on the logged-in user unless the key includes the user ID.

## 159: How do you invalidate a group of related cache keys?

Options:

- **Versioned prefix**: keep a version number like `cache:v:products = 7` and build keys as `products:v7:...`. Bump the version to make all old keys unused; they expire on their own.
- **Tag sets**: store related keys in a set (`tag:products`) and delete them all with `SMEMBERS` + `UNLINK`.
- **SCAN + UNLINK** by pattern, which works but is slower and should be done carefully.

Versioning is the cheapest because it does not delete anything.

## 160: How does pipelining improve performance?

Each command normally costs one network round trip. If the round trip is 1 ms, 1000 commands take at least 1 second. With a pipeline, you send all 1000 at once and read 1000 replies, so it might take a few milliseconds. It also lowers the number of system calls on the server. Do not put millions of commands in one pipeline, since replies are buffered in memory; send them in chunks of a few hundred or thousand.

## 161: What is the difference between pipelining, MULTI/EXEC and Lua scripts?

- **Pipeline**: saves round trips. Not atomic, other clients can run commands in between.
- **MULTI/EXEC**: commands run together without interruption, but you cannot use a result from one command to decide the next inside the transaction.
- **Lua script / Function**: runs atomically on the server and can read values and make decisions.

A transaction can also be pipelined, which is what most clients do.

## 162: How do you use WATCH for optimistic locking?

```js
async function transfer(from, to, amount) {
  for (let attempt = 0; attempt < 5; attempt++) {
    await redis.watch(from);
    const balance = Number(await redis.get(from));
    if (balance < amount) {
      await redis.unwatch();
      throw new Error("Insufficient funds");
    }
    const result = await redis
      .multi()
      .decrby(from, amount)
      .incrby(to, amount)
      .exec();
    if (result) return; // null means a watched key changed
  }
  throw new Error("Too much contention");
}
```

Use a dedicated connection for this, because `WATCH` state belongs to the connection.

## 163: How do KEYS and ARGV work in Lua scripts?

You pass key names and other arguments separately:

```bash
EVAL "return redis.call('SET', KEYS[1], ARGV[1], 'EX', ARGV[2])" 1 user:1 Ann 60
```

The number after the script (`1`) is how many of the following values are keys. Always pass key names through `KEYS`, never build them inside the script. Redis Cluster uses `KEYS` to route the script to the right node, and ACLs use it to check key permissions.

## 164: What is the difference between EVAL and EVALSHA?

`EVAL` sends the full script each time. `EVALSHA` sends only the SHA1 hash of a script that was loaded before with `SCRIPT LOAD` (or run with `EVAL`). It saves bandwidth. If the server does not have the script (for example after a restart), you get a `NOSCRIPT` error and have to send it again. Most client libraries handle this for you.

```bash
SCRIPT LOAD "return redis.call('GET', KEYS[1])"
# "a42059b356c875f0717db19a51f6aaca9ae659ea"
EVALSHA a42059b356c875f0717db19a51f6aaca9ae659ea 1 key
```

## 165: What is the difference between redis.call and redis.pcall in Lua?

`redis.call` raises an error if the command fails, and the script stops with that error. `redis.pcall` catches the error and returns it as a table, so the script can keep running and decide what to do. Note that writes made before an error are not rolled back.

## 166: How do you define a reusable script in ioredis?

```js
redis.defineCommand("releaseLock", {
  numberOfKeys: 1,
  lua: `
    if redis.call("GET", KEYS[1]) == ARGV[1] then
      return redis.call("DEL", KEYS[1])
    end
    return 0
  `,
});

await redis.releaseLock("lock:report", token);
```

ioredis uses `EVALSHA` and falls back to `EVAL` automatically.

## 167: When should you use Functions instead of EVAL?

Use Functions when the logic is part of your app and many services call it. Functions are loaded once, stored in the RDB/AOF, replicated to replicas, and called by name with `FCALL`. Scripts sent with `EVAL` are just a cache; they disappear on restart and every client has to ship them. Functions also let you mark code as read-only (`no-writes` flag) so it can run with `FCALL_RO` on replicas.

## 168: How do you write a Redis Function library?

```lua
#!lua name=counters

local function incr_capped(keys, args)
  local max = tonumber(args[1])
  local current = tonumber(redis.call('GET', keys[1]) or '0')
  if current >= max then
    return current
  end
  return redis.call('INCR', keys[1])
end

redis.register_function('incr_capped', incr_capped)
```

```bash
cat counters.lua | redis-cli -x FUNCTION LOAD REPLACE
redis-cli FCALL incr_capped 1 visits 1000
```

## 169: How does SCAN work with MATCH, COUNT and TYPE?

```bash
SCAN 0 MATCH session:* COUNT 1000 TYPE string
```

- `MATCH` filters by glob pattern. The filter is applied after keys are fetched, so batches can be small or empty.
- `COUNT` is a hint for how much work to do per call, not an exact number of results. Default is 10.
- `TYPE` (Redis 6.0+) returns only keys of that type.

## 170: How do you delete keys by pattern safely?

```js
let cursor = "0";
do {
  const [next, keys] = await redis.scan(
    cursor,
    "MATCH",
    "cache:old:*",
    "COUNT",
    500,
  );
  cursor = next;
  if (keys.length) await redis.unlink(...keys);
} while (cursor !== "0");
```

From the shell:

```bash
redis-cli --scan --pattern 'cache:old:*' | xargs -L 500 redis-cli UNLINK
```

In a cluster, run it against every primary node.

## 171: What eviction policies are there?

- `noeviction`: do not evict, return an error on writes (default).
- `allkeys-lru`: evict the least recently used key from all keys.
- `allkeys-lfu`: evict the least frequently used key from all keys.
- `allkeys-random`: evict random keys.
- `volatile-lru`, `volatile-lfu`, `volatile-random`: same, but only among keys with a TTL.
- `volatile-ttl`: evict keys with a TTL, shortest TTL first.

Redis 8.6 added `allkeys-lrm` and `volatile-lrm`, which evict the least recently _modified_ keys, so keys that are only read but not written can still be evicted.

## 172: Which eviction policy should you pick for a cache?

For a pure cache, `allkeys-lru` is a safe default. If some keys are much more popular than others over time, `allkeys-lfu` often gives a better hit ratio. Use `volatile-*` policies if the same Redis also holds data without TTL that must never be evicted. If no key qualifies under a `volatile-*` policy, writes fail like with `noeviction`.

## 173: Why do job queue libraries like BullMQ require noeviction?

Queues store job data, job state and locks in Redis. If Redis evicts one of those keys, jobs can be lost or get stuck in a broken state. With `noeviction`, Redis returns an error when memory is full, so you see the problem instead of silently losing jobs. It is a good reason to keep queue data and cache data in separate Redis instances.

## 174: How accurate is LRU eviction in Redis?

It is an approximation. Redis does not keep a full list of keys by access time. When it needs to evict, it samples a few keys (`maxmemory-samples`, default 5) and evicts the best candidate from a pool it maintains. Raising the sample size to 10 gets closer to true LRU at a small CPU cost.

## 175: How does LFU eviction work?

Each key has a small counter that grows when the key is accessed. The counter grows on a logarithmic curve, so it can represent very high access rates in 8 bits. It also decays over time, so keys that were popular long ago lose their score. You can tune it with `lfu-log-factor` and `lfu-decay-time`. `OBJECT FREQ key` shows the counter when an LFU policy is active.

## 176: How do you configure RDB snapshots?

```
save 3600 1 300 100 60 10000
dbfilename dump.rdb
dir /var/lib/redis
rdbcompression yes
stop-writes-on-bgsave-error yes
```

`save 3600 1 300 100 60 10000` means: snapshot if at least 1 change in an hour, 100 changes in 5 minutes, or 10000 changes in 1 minute. `save ""` turns snapshots off.

## 177: What are the AOF fsync options?

```
appendonly yes
appendfsync everysec
```

- `always`: fsync after every write. Safest, slowest.
- `everysec`: fsync once per second in the background. You can lose about one second of writes. This is the default and a good balance.
- `no`: let the OS decide when to flush, usually every ~30 seconds. Fastest, least safe.

## 178: What is AOF rewrite?

Over time the AOF grows with many commands for the same keys (100 `INCR`s for one counter). A rewrite builds a new, minimal AOF from the current data, so the file shrinks. Redis does it in a child process. It can run automatically:

```
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
```

Or manually with `BGREWRITEAOF`.

## 179: What is multi-part AOF?

Since Redis 7.0, AOF is stored as several files in a directory (`appenddirname`, default `appendonlydir`): a base file (RDB or AOF format), one or more incremental files with new commands, and a manifest that lists them. During a rewrite, new writes go to a new incremental file instead of a memory buffer, which uses less memory and less disk I/O than before.

## 180: What is the RDB preamble in AOF?

With `aof-use-rdb-preamble yes` (the default), the base part of the AOF is written in RDB format. Loading is much faster because RDB is compact, and you still get AOF's durability for new writes appended after it.

## 181: Should you use RDB, AOF or both?

- Pure cache that can be rebuilt: often neither, or RDB only for faster warm restarts.
- Data you can lose a few minutes of: RDB.
- Data where losing more than a second is a problem: AOF with `everysec`, usually together with RDB for backups.

Using both is the common choice when Redis holds real data.

## 182: How do you set up a replica?

On the replica:

```
replicaof 10.0.0.1 6379
masterauth s3cret
masteruser replicator
replica-read-only yes
```

Or at runtime with `REPLICAOF 10.0.0.1 6379`. `REPLICAOF NO ONE` turns a replica back into a primary. Check status with `INFO replication`.

## 183: Can you read from replicas?

Yes. Replicas accept read commands by default (`replica-read-only yes` stops writes, not reads). Reading from replicas spreads load, but replication is asynchronous, so a replica can be a little behind. A user might write something and not see it on the next read if that read goes to a replica. Use the primary for reads that must be fresh.

## 184: What does the WAIT command do?

`WAIT numreplicas timeout` blocks until the previous writes of this connection were acknowledged by at least `numreplicas` replicas, or the timeout passes. It returns how many replicas acknowledged.

```bash
SET order:1 paid
WAIT 1 1000
```

It lowers the chance of losing a write on failover, but it does not make Redis strongly consistent.

## 185: What is WAITAOF?

`WAITAOF numlocal numreplicas timeout` (Redis 7.2+) waits until previous writes are fsynced to the AOF on the local server and/or on replicas. It gives you a way to make sure a write is on disk before telling the user it succeeded.

```bash
WAITAOF 1 1 1000
```

## 186: How do you configure Sentinel?

```
port 26379
sentinel monitor mymaster 10.0.0.1 6379 2
sentinel auth-pass mymaster s3cret
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1
```

The `2` is the quorum: how many Sentinels must agree the primary is down before a failover can start. Run Sentinels on separate machines.

## 187: How does a client connect through Sentinel?

The client gets a list of Sentinel addresses and the master name. It asks a Sentinel for the current primary, connects to it, and reconnects when Sentinel reports a failover.

```js
import Redis from "ioredis";

const redis = new Redis({
  sentinels: [
    { host: "10.0.0.11", port: 26379 },
    { host: "10.0.0.12", port: 26379 },
    { host: "10.0.0.13", port: 26379 },
  ],
  name: "mymaster",
  password: process.env.REDIS_PASSWORD,
});
```

From the CLI: `SENTINEL GET-MASTER-ADDR-BY-NAME mymaster`.

## 188: How are keys distributed in Redis Cluster?

Redis computes `CRC16(key) mod 16384` to get a hash slot. Each primary node owns a set of slots. The client sends the command to the node that owns the key's slot.

```bash
CLUSTER KEYSLOT user:1001
```

## 189: What are hash tags?

If a key contains `{...}`, only the part inside the braces is hashed. Keys with the same hash tag go to the same slot, so multi-key commands work on them.

```
{user:1001}:profile
{user:1001}:cart
{user:1001}:orders
```

Don't put too many keys under one tag, or that slot becomes a hot spot.

## 190: What is a CROSSSLOT error?

In Redis Cluster, a multi-key command (`MGET`, `SUNION`, `MULTI` with several keys, a Lua script with several keys) fails with `CROSSSLOT` if the keys are in different hash slots. Fix it with hash tags, or split the work into single-key commands per node.

## 191: What are MOVED and ASK redirects?

- `MOVED 3999 10.0.0.5:6379`: the slot lives on another node permanently. The client should update its slot map and retry there.
- `ASK 3999 10.0.0.5:6379`: the slot is being migrated. The client should send `ASKING` and then the command to that node, just this once, without updating its map.

Cluster-aware clients handle both automatically.

## 192: How do you create a Redis Cluster?

Start six Redis servers with `cluster-enabled yes`, then:

```bash
redis-cli --cluster create \
  10.0.0.1:6379 10.0.0.2:6379 10.0.0.3:6379 \
  10.0.0.4:6379 10.0.0.5:6379 10.0.0.6:6379 \
  --cluster-replicas 1
```

That gives three primaries with one replica each. Check with `redis-cli --cluster check 10.0.0.1:6379` or `CLUSTER INFO`.

## 193: How do you connect to a cluster from Node.js?

```js
import Redis from "ioredis";

const cluster = new Redis.Cluster(
  [
    { host: "10.0.0.1", port: 6379 },
    { host: "10.0.0.2", port: 6379 },
  ],
  { redisOptions: { password: process.env.REDIS_PASSWORD } },
);

await cluster.set("user:1", "Ann");
```

With node-redis, use `createCluster({ rootNodes: [{ url: "redis://10.0.0.1:6379" }] })`. The client discovers the rest of the nodes.

## 194: How do you add a node to a cluster and move slots to it?

```bash
redis-cli --cluster add-node 10.0.0.7:6379 10.0.0.1:6379
redis-cli --cluster reshard 10.0.0.1:6379
# or spread slots evenly:
redis-cli --cluster rebalance 10.0.0.1:6379 --cluster-use-empty-masters
```

Keys move slot by slot while the cluster keeps serving traffic.

## 195: What is sharded pub/sub?

In regular cluster pub/sub, every message is sent to every node, which does not scale. Sharded pub/sub (Redis 7.0+) maps a channel to a hash slot like a key, so the message only goes to the shard that owns it.

```bash
SSUBSCRIBE orders:{eu}
SPUBLISH orders:{eu} "new order"
```

## 196: What are the limits of Redis pub/sub?

- No persistence: messages are lost if no one is listening.
- No acknowledgments or retries.
- A slow subscriber builds up an output buffer on the server; if it gets too large, Redis disconnects the client.
- A subscriber that reconnects misses everything sent while it was away.

For anything that must not be lost, use streams.

## 197: How do you subscribe to a channel in Node.js?

A subscribing connection cannot run normal commands, so use a separate connection.

```js
import Redis from "ioredis";

const sub = new Redis();
const pub = new Redis();

await sub.subscribe("chat:room1");
sub.on("message", (channel, message) => {
  console.log(channel, message);
});

await pub.publish("chat:room1", "hello");
```

With node-redis: `const sub = client.duplicate(); await sub.connect(); await sub.subscribe("chat:room1", (msg) => ...)`.

## 198: What is a consumer group in streams?

A consumer group lets several consumers share the work of one stream. Each entry is delivered to only one consumer in the group. Redis remembers the last delivered ID and keeps a pending entries list (PEL) of entries delivered but not yet acknowledged.

```bash
XGROUP CREATE orders billing $ MKSTREAM
```

`$` starts from new entries. Use `0` to process the whole history.

## 199: How do consumers read and acknowledge entries?

```bash
XREADGROUP GROUP billing worker-1 COUNT 10 BLOCK 5000 STREAMS orders >
# process entries...
XACK orders billing 1767225600123-0
```

`>` means "give me entries never delivered to anyone in this group". Once acknowledged, the entry leaves the pending list.

## 200: How do you handle entries that a crashed consumer never acknowledged?

Look at the pending list and claim old entries for another consumer:

```bash
XPENDING orders billing
XPENDING orders billing - + 10
XAUTOCLAIM orders billing worker-2 60000 0-0 COUNT 10
```

`XAUTOCLAIM` takes entries that have been pending for more than 60 seconds and gives them to `worker-2`. A consumer can also read its own pending entries again with `XREADGROUP ... STREAMS orders 0`.

## 201: How do you inspect a stream and its groups?

```bash
XINFO STREAM orders
XINFO GROUPS orders
XINFO CONSUMERS orders billing
```

They show the length, first and last entries, the groups, how many entries are pending, the lag, and how long each consumer has been idle.

## 202: How do you write a stream consumer in Node.js?

```js
import Redis from "ioredis";

const redis = new Redis();
const stream = "orders";
const group = "billing";
const consumer = `worker-${process.pid}`;

try {
  await redis.xgroup("CREATE", stream, group, "$", "MKSTREAM");
} catch (err) {
  if (!String(err.message).includes("BUSYGROUP")) throw err;
}

while (true) {
  const res = await redis.xreadgroup(
    "GROUP",
    group,
    consumer,
    "COUNT",
    10,
    "BLOCK",
    5000,
    "STREAMS",
    stream,
    ">",
  );
  if (!res) continue;

  for (const [, entries] of res) {
    for (const [id, fields] of entries) {
      await handleOrder(fields); // fields is ["user", "1", "total", "49.90"]
      await redis.xack(stream, group, id);
    }
  }
}
```

## 203: When should you use pub/sub, lists or streams for messaging?

- **Pub/sub**: live notifications where losing a message is fine (chat typing indicators, live dashboards, cache invalidation broadcasts).
- **Lists**: simple work queues with one consumer per job and no history.
- **Streams**: when you need durability, acknowledgments, retries, several consumer groups, or replay.

## 204: How do you build a sliding window rate limiter with a sorted set?

Store each request as a member with the timestamp as score, remove old ones, then count.

```js
async function allow(userId, limit, windowMs) {
  const key = `rl:${userId}`;
  const now = Date.now();
  const [, , [, count]] = await redis
    .multi()
    .zremrangebyscore(key, 0, now - windowMs)
    .zadd(key, now, `${now}-${Math.random()}`)
    .zcard(key)
    .pexpire(key, windowMs)
    .exec();
  return count <= limit;
}
```

This counts rejected requests too. If you don't want that, do the check and add inside a Lua script.

## 205: How do you build a token bucket rate limiter?

Keep tokens and the last refill time in a hash, and update them atomically in Lua:

```lua
-- KEYS[1] bucket key, ARGV: capacity, refill_per_sec, now_ms
local capacity = tonumber(ARGV[1])
local rate = tonumber(ARGV[2])
local now = tonumber(ARGV[3])

local data = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(data[1]) or capacity
local ts = tonumber(data[2]) or now

tokens = math.min(capacity, tokens + (now - ts) / 1000 * rate)
local allowed = 0
if tokens >= 1 then
  tokens = tokens - 1
  allowed = 1
end

redis.call('HSET', KEYS[1], 'tokens', tokens, 'ts', now)
redis.call('PEXPIRE', KEYS[1], math.ceil(capacity / rate * 1000))
return allowed
```

Token bucket allows short bursts up to `capacity` while keeping the average rate.

## 206: How do you release a lock safely?

Only delete the lock if it still holds your token. Otherwise you could delete a lock that expired and was taken by someone else.

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
  return redis.call("DEL", KEYS[1])
else
  return 0
end
```

Since Redis 8.4 you can do the same without Lua: `DELEX lock:job IFEQ <token>`.

## 207: What problems can a Redis lock still have?

- If the work takes longer than the TTL, the lock expires and another process takes it while the first is still working.
- A long GC pause or network delay can make a process think it still holds the lock when it does not.
- With async replication, the primary can fail before the lock key reaches the replica, and the new primary has no lock.

For correctness-critical work, add fencing tokens or use a system built for consensus. For "avoid doing the same work twice" cases, a Redis lock is usually fine.

## 208: How do you extend a lock while work is still running?

Refresh the TTL only if you still own it:

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
  return redis.call("PEXPIRE", KEYS[1], ARGV[2])
else
  return 0
end
```

Run it on a timer, for example every TTL/3. If it returns 0, you lost the lock and should stop the work.

## 209: How do you build a delayed job queue?

Use a sorted set with the run time as the score.

```bash
ZADD delayed 1767225660000 '{"id":1,"type":"reminder"}'
```

A worker polls for due jobs and moves them atomically with a Lua script:

```lua
-- KEYS[1] delayed zset, KEYS[2] ready list, ARGV[1] now
local jobs = redis.call('ZRANGE', KEYS[1], '-inf', ARGV[1], 'BYSCORE', 'LIMIT', 0, 100)
for _, job in ipairs(jobs) do
  redis.call('ZREM', KEYS[1], job)
  redis.call('RPUSH', KEYS[2], job)
end
return #jobs
```

## 210: How do you build a reliable queue with lists?

Move the job to a processing list instead of just popping it:

```bash
BLMOVE jobs jobs:processing RIGHT LEFT 0
# after the job is done:
LREM jobs:processing 1 <job>
```

If the worker dies, the job is still in `jobs:processing`. A cleanup process can push stuck jobs back to `jobs`. Streams with consumer groups give you the same thing with less code.

## 211: What is BullMQ and how does it use Redis?

BullMQ is a Node.js job queue built on Redis. It stores jobs in hashes, uses lists, sorted sets and streams for waiting, delayed and completed jobs, and uses Lua scripts so state changes are atomic. It gives you retries, backoff, priorities, rate limits, repeatable jobs and flows on top of plain Redis.

```js
import { Queue, Worker } from "bullmq";

const connection = { host: "localhost", port: 6379 };
const queue = new Queue("emails", { connection });
await queue.add("welcome", { to: "ann@example.com" }, { attempts: 3 });

new Worker("emails", async (job) => sendEmail(job.data), { connection });
```

## 212: How do you store sessions in Redis with Express?

```js
import express from "express";
import session from "express-session";
import { createClient } from "redis";
import { RedisStore } from "connect-redis";

const client = createClient({ url: process.env.REDIS_URL });
await client.connect();

const app = express();
app.use(
  session({
    store: new RedisStore({ client, prefix: "sess:" }),
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: { httpOnly: true, secure: true, maxAge: 86400000 },
  }),
);
```

`connect-redis` sets a TTL on each session key that matches the cookie's `maxAge`. Older versions used a default export instead of `{ RedisStore }`.

## 213: How should a Node.js app manage Redis connections?

Create one client when the app starts and reuse it for all requests. Redis connections are cheap for the server but slow to open, and one connection can handle many concurrent commands because the client pipelines them. You need extra connections only for blocking commands (`BLPOP`, `XREAD BLOCK`), pub/sub subscribers, and `WATCH` transactions.

## 214: How do you handle reconnects in ioredis?

ioredis reconnects automatically. You can control the delay with `retryStrategy`:

```js
const redis = new Redis({
  host: "localhost",
  retryStrategy(times) {
    return Math.min(times * 200, 5000); // ms before next try
  },
  maxRetriesPerRequest: 3,
});

redis.on("error", (err) => console.error("redis", err.message));
redis.on("reconnecting", () => console.log("reconnecting"));
```

`maxRetriesPerRequest` stops single commands from waiting forever while Redis is down.

## 215: How do you handle reconnects in node-redis?

```js
const client = createClient({
  url: process.env.REDIS_URL,
  socket: {
    reconnectStrategy: (retries) => Math.min(retries * 100, 3000),
    connectTimeout: 5000,
  },
});

client.on("error", (err) => console.error(err));
await client.connect();
```

Always add an `error` listener. Without it, a connection error can crash the Node.js process.

## 216: What happens to your app if Redis goes down?

That depends on how you wrote it. For a cache, the app should catch errors and fall back to the database, maybe with a short timeout so requests do not hang. For sessions, queues or locks, Redis is a hard dependency, so you need high availability (Sentinel, Cluster or a managed service) and clear errors when it is unavailable.

```js
async function cachedGet(key, loader) {
  try {
    const hit = await redis.get(key);
    if (hit) return JSON.parse(hit);
  } catch {
    // cache down, continue to source
  }
  return loader();
}
```

## 217: How do you use Redis transactions in node-redis?

```js
const [count, list] = await client
  .multi()
  .incr("orders:count")
  .lPush("orders:recent", "order:99")
  .exec();
```

For a pipeline without `MULTI/EXEC`, use `.execAsPipeline()`. node-redis also pipelines commands sent in the same tick automatically, so `Promise.all` over many commands is already efficient.

## 218: What is client-side caching?

Client-side caching (Redis 6+) lets the client keep values in its own memory, and Redis tells it when those keys change. You turn it on with `CLIENT TRACKING ON`. Redis remembers which keys each client read and sends invalidation messages when they are modified. It removes network round trips for hot keys.

## 219: What are the client tracking modes?

- **Default mode**: Redis remembers exactly which keys each client read. Precise, but uses server memory.
- **Broadcast mode** (`BCAST PREFIX user:`): Redis does not track reads. It sends invalidations for every change to keys with the given prefixes. Uses no per-key memory but sends more messages.
- **OPTIN / OPTOUT**: the client decides per command whether a read should be tracked, using `CLIENT CACHING yes|no`.

## 220: What is RESP3 and why does it matter?

RESP3 is the newer protocol version. It adds proper types such as maps, sets, doubles, booleans and null, so clients don't have to guess. It also adds push messages, which let pub/sub and client tracking invalidations arrive on the same connection as normal commands. You switch with `HELLO 3`.

## 221: How do you use keyspace notifications to react to expired keys?

```bash
CONFIG SET notify-keyspace-events Ex
```

```js
const sub = new Redis();
await sub.psubscribe("__keyevent@0__:expired");
sub.on("pmessage", (_pattern, _channel, key) => {
  console.log("expired:", key);
});
```

The expired event fires when Redis actually deletes the key, not exactly at the TTL time, and it is not delivered if your subscriber is disconnected. Don't use it for anything that must run on time.

## 222: What letters can you use in notify-keyspace-events?

- `K`: keyspace events (`__keyspace@0__:mykey`), `E`: keyevent events (`__keyevent@0__:del`).
- `g`: generic commands (DEL, EXPIRE, RENAME), `$`: strings, `l`: lists, `s`: sets, `h`: hashes, `z`: sorted sets, `t`: streams.
- `x`: expired, `e`: evicted, `m`: key miss, `n`: new key.
- `A`: alias for most classes.

You need at least `K` or `E`, plus at least one class.

## 223: How do you create ACL users for different services?

```bash
ACL SETUSER api on >api-pass ~cache:* ~session:* +@read +@write -@dangerous
ACL SETUSER worker on >worker-pass ~queue:* +@all -@admin -@dangerous
ACL SETUSER metrics on >m-pass resetkeys +info +ping +client|list
ACL SETUSER default off
```

Store them in an ACL file with `aclfile /etc/redis/users.acl` and save changes with `ACL SAVE`. Turning off the `default` user forces every client to log in.

## 224: What do key permissions like %R~ and %W~ mean?

Since Redis 7.0 you can give read-only or write-only access to key patterns:

```bash
ACL SETUSER reporter on >pass %R~orders:* %RW~reports:* +@all
```

`%R~orders:*` means the user can read but not write `orders:*` keys. `~` alone is read and write.

## 225: How do you turn on TLS?

```
port 0
tls-port 6379
tls-cert-file /etc/redis/redis.crt
tls-key-file /etc/redis/redis.key
tls-ca-cert-file /etc/redis/ca.crt
tls-auth-clients optional
```

Clients connect with `rediss://` (two s). `tls-replication yes` and `tls-cluster yes` encrypt replication and cluster bus traffic too.

## 226: How should you secure a Redis server?

- Never expose it to the public internet. Bind to private interfaces and use firewalls or security groups.
- Keep protected mode on.
- Use ACL users with strong passwords, and disable the `default` user.
- Block dangerous commands (`FLUSHALL`, `CONFIG`, `DEBUG`, `KEYS`) for app users with ACLs.
- Turn on TLS when traffic leaves a trusted network.
- Run Redis as a non-root user.
- Keep it updated for security fixes.

## 227: What replaced rename-command?

In older setups people used `rename-command FLUSHALL ""` in redis.conf to disable commands. It still works but it is considered legacy: it breaks tools that expect the real names and applies to every user. ACLs are the modern way, since you can allow or deny commands per user.

## 228: How do you find big keys?

```bash
redis-cli --bigkeys       # biggest key per type, by element count
redis-cli --memkeys       # biggest keys by memory
MEMORY USAGE some:key
```

These use `SCAN`, so they are safe to run on a live server, though they add some load. Tools like Redis Insight can also analyze memory.

## 229: What is a hot key and how do you find one?

A hot key is a single key that gets a big share of all traffic. Since one key lives on one node, it can max out that node's CPU or network even if the rest of the cluster is idle.

To find them: `redis-cli --hotkeys` (needs an LFU eviction policy), `OBJECT FREQ`, `MONITOR` samples in a test environment, client-side metrics, and since Redis 8.6 the `HOTKEYS` command, which tracks keys using a lot of CPU or network.

## 230: How do you deal with a hot key?

- Cache it in the app's memory for a short time, or use client-side caching.
- Read from replicas.
- Split it into several keys (`counter:1` ... `counter:10`) and combine them on read.
- For a hot counter, buffer increments in the app and flush them in batches.

## 231: How do you use the latency monitor?

```bash
CONFIG SET latency-monitor-threshold 100   # ms
LATENCY LATEST
LATENCY HISTORY command
LATENCY DOCTOR
```

It records events like slow commands, fork, AOF fsync and expire cycles that went over the threshold. `LATENCY DOCTOR` gives a readable report with hints.

## 232: How do you measure latency from the client side?

```bash
redis-cli --latency -h host
redis-cli --latency-history -i 5
redis-cli --intrinsic-latency 10   # run on the server host
```

`--intrinsic-latency` measures the latency of the machine itself (scheduler, virtualization), which is the lowest latency Redis can get there.

## 233: What are the most useful INFO fields to monitor?

- `used_memory`, `used_memory_rss`, `mem_fragmentation_ratio`, `maxmemory`.
- `connected_clients`, `blocked_clients`, `rejected_connections`.
- `instantaneous_ops_per_sec`, `keyspace_hits`, `keyspace_misses`.
- `evicted_keys`, `expired_keys`.
- `rdb_last_bgsave_status`, `aof_last_write_status`, `latest_fork_usec`.
- `master_link_status`, `master_repl_offset`, replica lag.

## 234: What are the internal encodings of each type?

- String: `int`, `embstr`, `raw`.
- List: `listpack` (small), `quicklist` (large).
- Set: `intset` (small, all integers), `listpack` (small), `hashtable`.
- Hash: `listpack` (small), `hashtable`.
- Sorted set: `listpack` (small), `skiplist` (a skip list plus a hash table).

Redis converts from the compact encoding to the full one automatically when a collection grows past the configured limits.

## 235: What config settings control compact encodings?

```
hash-max-listpack-entries 128
hash-max-listpack-value 64
zset-max-listpack-entries 128
zset-max-listpack-value 64
set-max-intset-entries 512
set-max-listpack-entries 128
set-max-listpack-value 64
list-max-listpack-size -2
```

Raising them saves memory but makes operations on those collections slower, since listpacks are scanned linearly. Older versions used `ziplist` in the names; those names are still accepted as aliases.

## 236: How do you save memory with many small objects?

- Keep keys short.
- Group small values into hashes so they use the listpack encoding. For example, instead of millions of `user:1234:name` keys, use buckets like `HSET users:12 34 "Ann"`.
- Store numbers as integers so they use the `int` encoding.
- Compress large values (gzip, zstd) in the client.
- Use bitmaps or HyperLogLog for flags and counts.
- Remove data you don't need with TTLs.

## 237: How do you query JSON documents with JSONPath?

```bash
JSON.SET order:1 $ '{"items":[{"sku":"A","qty":2},{"sku":"B","qty":1}],"status":"new"}'
JSON.GET order:1 '$.items[*].sku'          # ["A","B"]
JSON.GET order:1 '$.items[?(@.qty>1)]'     # items with qty > 1
JSON.SET order:1 $.status '"paid"'
JSON.DEL order:1 '$.items[1]'
JSON.TYPE order:1 $.items
```

Paths starting with `$` return arrays of matches. The older `.` path syntax returns a single value.

## 238: What is the Redis Query Engine?

It is the search engine built into Redis 8 (formerly the RediSearch module). You create an index over hashes or JSON documents with a key prefix, and Redis keeps it updated as you write. You can then search by text, numbers, tags, geo and vectors, sort, paginate and aggregate.

## 239: How do you create a search index and query it?

```bash
FT.CREATE idx:products ON HASH PREFIX 1 product: SCHEMA
  name TEXT SORTABLE
  price NUMERIC SORTABLE
  category TAG

HSET product:1 name "Red shoes" price 49 category shoes
HSET product:2 name "Blue shirt" price 25 category shirts

FT.SEARCH idx:products "@category:{shoes} @price:[0 100]" SORTBY price ASC LIMIT 0 10
```

`TEXT` fields are full-text searchable, `TAG` fields are exact matches, `NUMERIC` fields support ranges.

## 240: How do you index JSON documents?

```bash
FT.CREATE idx:users ON JSON PREFIX 1 user: SCHEMA
  $.name AS name TEXT
  $.age AS age NUMERIC
  $.tags[*] AS tags TAG

JSON.SET user:1 $ '{"name":"Ann","age":31,"tags":["admin","beta"]}'
FT.SEARCH idx:users "@tags:{admin} @age:[30 40]"
```

`AS` gives the JSONPath a short field name for queries.

## 241: What is FT.AGGREGATE used for?

It runs grouping and reduction queries over an index, like SQL `GROUP BY`.

```bash
FT.AGGREGATE idx:products "*"
  GROUPBY 1 @category
  REDUCE COUNT 0 AS count
  REDUCE AVG 1 @price AS avg_price
  SORTBY 2 @count DESC
```

## 242: How do you add vector search to an index?

```bash
FT.CREATE idx:docs ON HASH PREFIX 1 doc: SCHEMA
  content TEXT
  embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 768 DISTANCE_METRIC COSINE

FT.SEARCH idx:docs "*=>[KNN 5 @embedding $vec AS score]"
  PARAMS 2 vec <768 float32 bytes>
  SORTBY score
  RETURN 2 content score
  DIALECT 2
```

The vector is stored as raw float32 bytes in the hash. You can combine KNN with filters, like `(@category:{faq})=>[KNN 5 @embedding $vec]`.

## 243: What is the difference between vector sets and vector fields in the Query Engine?

Vector sets (`VADD`, `VSIM`) are a standalone data type: one key holds many elements with vectors and optional JSON attributes for filtering. They are simple and quick to start with. Vector fields in the Query Engine are part of a full index over hashes or JSON, so you can mix vector search with text, tag and numeric filters, aggregations and sorting. Pick vector sets for simple similarity lookups, and the Query Engine when vectors are one part of a larger search.

## 244: How do you downsample time series data?

Create a rule that writes aggregated data into another series:

```bash
TS.CREATE temp:raw RETENTION 86400000
TS.CREATE temp:hourly RETENTION 31536000000
TS.CREATERULE temp:raw temp:hourly AGGREGATION avg 3600000

TS.MRANGE - + FILTER room=1
```

Raw data is kept for a day, hourly averages for a year. `TS.MRANGE` queries several series by label.

## 245: What other probabilistic data types are there?

- **Cuckoo filter** (`CF.ADD`, `CF.EXISTS`, `CF.DEL`): like a Bloom filter but supports deletes.
- **Count-min sketch** (`CMS.INCRBY`, `CMS.QUERY`): approximate counts per item.
- **Top-K** (`TOPK.ADD`, `TOPK.LIST`): keeps the K most frequent items.
- **t-digest** (`TDIGEST.ADD`, `TDIGEST.QUANTILE`): approximate percentiles, for example p99 latency.

They trade a little accuracy for far less memory.

## 246: How do you use BITFIELD?

`BITFIELD` reads and writes integers of any bit width inside a string. It is good for packing many small counters in one key.

```bash
BITFIELD stats:user:1 SET u8 0 100 INCRBY u8 8 1 GET u8 0
BITFIELD counters OVERFLOW SAT INCRBY u4 0 20   # saturates at 15
```

`u8` is an unsigned 8-bit integer, `i16` a signed 16-bit one. The offset is in bits (use `#n` to count in units of the type).

## 247: How do you combine bitmaps?

```bash
BITOP AND active:both logins:mon logins:tue   # logged in both days
BITOP OR active:any logins:mon logins:tue
BITCOUNT active:both
BITPOS logins:mon 1                           # first user who logged in
```

This answers questions like "how many users were active every day this week" with very little memory.

## 248: How do you paginate a sorted set?

```bash
ZRANGE posts:by_date +inf -inf BYSCORE REV LIMIT 0 20
```

For stable pagination, use the last score you saw as the next start (keyset pagination), instead of offsets. Offsets get slower on deep pages and skip or repeat items when new ones are added.

```bash
ZRANGE posts:by_date (1767225600 -inf BYSCORE REV LIMIT 0 20
```

## 249: How do ZUNIONSTORE and ZINTERSTORE work?

They combine sorted sets into a new one. Scores are summed by default, and you can use weights and other aggregates.

```bash
ZUNIONSTORE lb:week 7 lb:mon lb:tue lb:wed lb:thu lb:fri lb:sat lb:sun
ZINTERSTORE matches 2 skills:js skills:remote WEIGHTS 1 0 AGGREGATE SUM
```

`ZUNION`, `ZINTER` and `ZDIFF` (Redis 6.2+) return the result without storing it.

## 250: What do LMPOP, ZMPOP and SINTERCARD do?

These came in Redis 7.0:

- `LMPOP 2 queue:high queue:low LEFT COUNT 10` pops from the first non-empty list.
- `ZMPOP 1 tasks MIN COUNT 5` pops several lowest-scored members.
- `SINTERCARD 2 a b LIMIT 100` returns only the size of the intersection, stopping early at the limit.

`BLMPOP` and `BZMPOP` are the blocking versions.

## 251: How do you model a "users who viewed this item" feature?

A sorted set per item, with the view time as the score:

```bash
ZADD viewed:item:42 1767225600 user:7
ZREMRANGEBYRANK viewed:item:42 0 -1001    # keep last 1000 viewers
ZRANGE viewed:item:42 0 19 REV            # 20 most recent
```

Re-viewing updates the score, so each user appears once and the list stays ordered by most recent.

## 252: How do you build a news feed in Redis?

A simple version: each user has a list or sorted set of post IDs (`feed:user:1`). When someone posts, you push the post ID into each follower's feed (fan-out on write) and trim it to the last N items. Post content lives in hashes (`post:99`). For users with millions of followers, you skip the fan-out and merge their posts into the feed when it is read (fan-out on read).

## 253: How do you build autocomplete with Redis?

Options:

- A sorted set with all scores `0` and `ZRANGE ... BYLEX` on a prefix range.
- A sorted set per prefix, scored by popularity.
- The Query Engine with a `TEXT` field and prefix queries (`FT.SEARCH idx "@name:app*"`), or the suggestion commands `FT.SUGADD` and `FT.SUGGET`.

```bash
FT.SUGADD ac "apple" 100
FT.SUGADD ac "application" 50
FT.SUGGET ac "app" FUZZY MAX 5
```

## 254: How do you store an object with an expiring field, like a one-time code?

Use hash field expiration:

```bash
HSET user:1 name Ann otp 482913
HEXPIRE user:1 300 FIELDS 1 otp
HGETDEL user:1 FIELDS 1 otp     # read and remove in one step (Redis 8.0+)
```

Before Redis 7.4 you had to store the code in a separate key with its own TTL.

## 255: How do HSETEX and HGETEX work?

They were added in Redis 8.0.

```bash
HSETEX session:1 EX 1800 FIELDS 2 user 7 role admin
HGETEX session:1 EX 1800 FIELDS 1 user     # read and refresh the TTL
HGETEX session:1 PERSIST FIELDS 1 user     # read and remove the TTL
```

`HSETEX` also supports `FNX` (only if none of the fields exist) and `FXX` (only if all exist).

## 256: How do you run Redis with Docker Compose for development?

```yaml
services:
  redis:
    image: redis:8
    ports:
      - "6379:6379"
    command:
      [
        "redis-server",
        "--appendonly",
        "yes",
        "--maxmemory",
        "256mb",
        "--maxmemory-policy",
        "allkeys-lru",
      ]
    volumes:
      - redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      retries: 5

volumes:
  redis-data:
```

## 257: How do you test code that uses Redis?

- Integration tests against a real Redis in Docker, for example with Testcontainers. This catches real behavior like TTLs and Lua errors.
- `ioredis-mock` or similar fakes for fast unit tests, but they don't support every command and can behave differently.
- Use a separate database or key prefix per test run and clean up with `FLUSHDB` on a test-only server.

## 258: How do you run Redis in Kubernetes?

For a cache, a single Deployment or StatefulSet with a Service is enough. For data you care about, use a StatefulSet with persistent volumes, or an operator or Helm chart that sets up replication with Sentinel or Cluster. Many teams skip all of this and use a managed service. Remember that Redis Cluster nodes announce IPs, so you may need `cluster-announce-ip` settings when pod IPs change.

## 259: How do you migrate data between two Redis servers?

- Make the new one a replica of the old one (`REPLICAOF`), wait for sync, then promote it.
- Copy the RDB file and start the new server with it.
- Use `MIGRATE` for single keys or small sets of keys.
- Use tools like RIOT or `redis-shake` for large or cross-version moves.

Replication is the easiest when both servers can reach each other.

## 260: What does the MIGRATE command do?

It moves keys from the current server to another one atomically: it serializes the key, sends it, restores it on the target and deletes it locally.

```bash
MIGRATE 10.0.0.9 6379 "" 0 5000 KEYS user:1 user:2
```

Add `COPY` to keep the local key or `REPLACE` to overwrite on the target. `DUMP` and `RESTORE` let you do the same in two steps.

## 261: What are DUMP and RESTORE?

`DUMP key` returns the value in Redis's internal serialized format. `RESTORE key ttl payload` creates a key from that data. They are useful for copying keys between servers or making manual backups of a few keys. The format is versioned, so a dump from a newer Redis may not restore on an older one.

## 262: How do you check replication lag?

On the primary, `INFO replication` lists each replica with its `offset` and `lag` (seconds since last ack). Compare the replica's offset to `master_repl_offset`. On the replica, check `master_link_status:up` and `master_last_io_seconds_ago`.

## 263: What are min-replicas-to-write and min-replicas-max-lag?

```
min-replicas-to-write 1
min-replicas-max-lag 10
```

With these, the primary refuses writes if fewer than 1 replica has acknowledged within the last 10 seconds. It limits how many writes you can lose if the primary gets cut off from the replicas, at the cost of availability.

## 264: How do you see the cluster state and topology?

```bash
CLUSTER INFO      # state, slots assigned, known nodes
CLUSTER NODES     # one line per node with role and slots
CLUSTER SHARDS    # structured view of shards (Redis 7.0+)
CLUSTER COUNTKEYSINSLOT 1234
CLUSTER GETKEYSINSLOT 1234 10
```

`cluster_state:ok` means all slots are covered.

## 265: How do you read from replicas in Redis Cluster?

By default replicas in a cluster redirect every command to the primary. A client must send `READONLY` on its connection to a replica to read from it. Libraries expose this as an option, for example `scaleReads: "slave"` in ioredis or `useReplicas: true` in node-redis.

## 266: How does failover work in Redis Cluster?

Nodes ping each other over the cluster bus. If a majority of primaries can't reach a primary for `cluster-node-timeout`, it is marked as failed. One of its replicas asks the other primaries for votes, and if it gets a majority, it becomes the new primary and takes over the slots. You can also trigger it with `CLUSTER FAILOVER` on a replica for planned maintenance.

## 267: What is cluster-require-full-coverage?

When `yes` (default), the cluster stops accepting queries if any slot is not served, for example when a primary and all its replicas are down. When `no`, the remaining nodes keep serving the slots they own. Setting it to `no` keeps part of your app working at the cost of some keys being unavailable.

## 268: Can you use transactions and Lua scripts in Redis Cluster?

Yes, but all keys used in one `MULTI/EXEC` or script must be in the same hash slot. Use hash tags to put related keys together. Scripts must pass every key they touch in `KEYS`, so the client can route the call.

## 269: Can you use multiple databases in Redis Cluster?

No. Cluster only supports database 0, and `SELECT` with any other number fails. If you used databases to separate apps, switch to key prefixes or separate clusters.

## 270: How do you serialize values for Redis?

Common choices:

- JSON: readable and easy to debug, but larger and slower for big objects.
- MessagePack or Protocol Buffers: smaller and faster, but not readable in the CLI.
- Plain strings and numbers for simple values, so you can use `INCR` and similar commands.

Whatever you pick, version your format (`user:v2:1`) so you can change it later without breaking old cache entries.

## 271: How do you store dates and numbers in Redis?

Everything is stored as a string, but numbers that fit in a 64-bit integer use a compact encoding and work with `INCR`. Store dates as Unix timestamps (seconds or milliseconds), not formatted strings. Timestamps sort correctly, work as sorted set scores, and compare easily in Lua.

## 272: What is the OBJECT command used for?

```bash
OBJECT ENCODING key   # internal encoding
OBJECT IDLETIME key   # seconds since last access (LRU policies)
OBJECT FREQ key       # access frequency counter (LFU policies)
OBJECT REFCOUNT key   # reference count
```

`OBJECT IDLETIME` helps you find keys no one has read for a long time.

## 273: How can you find keys without a TTL?

Scan and check each key:

```bash
redis-cli --scan --pattern 'cache:*' | while read key; do
  ttl=$(redis-cli TTL "$key")
  [ "$ttl" = "-1" ] && echo "$key"
done
```

In code, do the same with `SCAN` and pipeline the `TTL` calls. `INFO keyspace` tells you how many keys have an expiration (`expires=`), so you can see the scale of the problem first.

## 274: How do you rename keys or change structure without downtime?

Write to both the old and the new format for a while, read from the new one with a fallback to the old one, then backfill old keys with a script using `SCAN`. When everything is migrated, remove the old reads and writes. For a cache, you can often just change the key prefix and let the old keys expire.

## 275: What is the difference between RENAME and COPY plus DEL?

`RENAME` is atomic and O(1) (unless it overwrites a big key, which must then be freed). `COPY` duplicates the value, so it is O(N) for big collections, and then `DEL` frees the old one. Use `RENAME` when you just want a new name, and `COPY` when you need both keys to exist.

## 276: How do you atomically swap in a new version of a big collection?

Build the new data under a temporary key, then rename it over the live key:

```bash
DEL lb:tmp
ZADD lb:tmp 100 ann 90 bob ...
RENAME lb:tmp lb:live
```

Readers see either the old or the new data, never a half-built one. With `lazyfree-lazy-server-del yes`, the old value is freed in the background.

## 277: How do you count events per minute for a dashboard?

Use one key per minute, or one hash per hour with a field per minute:

```bash
HINCRBY stats:signups:2026-11-05T14 37 1
EXPIRE stats:signups:2026-11-05T14 172800 NX
HGETALL stats:signups:2026-11-05T14
```

For larger needs or real metrics, the time series type with `TS.INCRBY` and aggregation is a better fit.

## 278: How do you implement idempotency keys for an API?

When a request comes in with an `Idempotency-Key` header, try to claim the key:

```js
const claimed = await redis.set(`idem:${key}`, "processing", "NX", "EX", 86400);
if (!claimed) {
  const stored = await redis.get(`idem:${key}`);
  if (stored === "processing") return res.status(409).send("In progress");
  return res.json(JSON.parse(stored));
}

const result = await createPayment(req.body);
await redis.set(`idem:${key}`, JSON.stringify(result), "EX", 86400);
res.json(result);
```

Retries with the same key get the saved result instead of creating a second payment.

## 279: How do you deduplicate events or messages?

Store the IDs you have processed with `SET NX` and a TTL that is longer than the time a duplicate could arrive:

```bash
SET seen:evt:abc123 1 NX EX 86400
```

If it returns `OK`, process the event. If it returns nil, skip it. For huge volumes where a small error rate is OK, a Bloom filter uses much less memory.

## 280: How do you avoid race conditions in read-modify-write code?

Don't read a value into the app, change it, and write it back with separate commands. Instead:

- Use atomic commands (`INCR`, `HINCRBY`, `SADD`, `ZADD GT`, `SET NX`).
- Use `WATCH` + `MULTI` for optimistic locking.
- Use a Lua script or Function when the logic is more complex.
- Since Redis 8.4, `SET key new IFEQ old` does a compare-and-set on strings.

## 281: What is the compare-and-set support added in Redis 8.4?

Redis 8.4 added conditions to `SET` and a new `DELEX` command:

```bash
SET config:v "new" IFEQ "old"     # set only if current value equals "old"
SET config:v "new" IFNE "old"     # set only if current value is different
DELEX lock:job IFEQ token123      # delete only if value matches
DIGEST config:v                   # hash of the value
```

`IFDEQ` and `IFDNE` compare against a digest instead of the full value, which helps with large values. These remove the need for small Lua scripts in many lock and config cases.

## 282: How do you set many keys with a TTL in one command?

Before Redis 8.4 you had to pipeline `SET ... EX` for each key, because `MSET` has no TTL option. Redis 8.4 added `MSETEX`, which sets several keys and their expiration in one atomic command. On older servers, a pipeline or a `MULTI` with several `SET ... EX` calls does the job.

## 283: How do you limit concurrent jobs per user?

Use a counter with a safety TTL:

```lua
-- KEYS[1] counter, ARGV[1] max, ARGV[2] ttl
local current = tonumber(redis.call('GET', KEYS[1]) or '0')
if current >= tonumber(ARGV[1]) then
  return 0
end
redis.call('INCR', KEYS[1])
redis.call('EXPIRE', KEYS[1], ARGV[2])
return 1
```

Decrement when the job finishes. The TTL cleans up if a worker dies. A more exact version stores job IDs in a sorted set with a timeout as score.

## 284: How do you use Redis with NestJS for caching?

NestJS has a cache module that can use a Redis store through Keyv:

```ts
import { CacheModule } from "@nestjs/cache-manager";
import KeyvRedis from "@keyv/redis";

@Module({
  imports: [
    CacheModule.registerAsync({
      useFactory: () => ({
        stores: [new KeyvRedis("redis://localhost:6379")],
        ttl: 60_000,
      }),
    }),
  ],
})
export class AppModule {}
```

Then inject `CACHE_MANAGER` or use `CacheInterceptor` on controllers. For anything beyond simple caching, inject your own Redis client.

## 285: How do you choose the right data type for a problem?

Ask what you need to do with the data:

- Get/set a value or count: string.
- Object with fields: hash (or JSON for nested data).
- Ordered by insertion, push/pop at the ends: list.
- Unique items, membership checks: set.
- Ordered by a number, ranges, rankings: sorted set.
- Event log with consumers: stream.
- Approximate counts with tiny memory: HyperLogLog, Bloom, count-min sketch.
- Search by many fields: JSON or hash plus a Query Engine index.

## 286: What happens when you run a command on the wrong type?

You get a `WRONGTYPE` error:

```bash
LPUSH mylist a
GET mylist
# (error) WRONGTYPE Operation against a key holding the wrong kind of value
```

It usually means two parts of the code use the same key name for different things. Key prefixes per feature help avoid this.

## 287: How do you limit the number of client connections?

`maxclients` (default 10000) caps open connections. When the limit is reached, new connections get an error. The real limit can be lower if the OS file descriptor limit is lower. Watch `connected_clients` and `rejected_connections`, and fix apps that open a new connection per request.

## 288: How do you close idle connections?

```
timeout 300
tcp-keepalive 300
```

`timeout` closes client connections idle for that many seconds (0 means never). `tcp-keepalive` sends TCP keepalives so dead peers are detected and half-open connections get cleaned up. Pub/sub and blocked clients are not closed by `timeout`.

## 289: What is the Redis query buffer and output buffer?

Each client has a query buffer for commands it sent that are not yet parsed, and an output buffer for replies waiting to be sent. A client that sends huge commands or reads replies slowly grows these buffers. `client-query-buffer-limit` and `client-output-buffer-limit` protect the server by closing clients that go over the limits.

## 290: How do you configure client output buffer limits?

```
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit replica 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
```

The format is `class hard-limit soft-limit soft-seconds`. A client is disconnected if it goes over the hard limit, or stays over the soft limit for that many seconds. If replicas keep disconnecting during a full sync on a busy primary, the replica limit is often too low.

## 291: What does CONFIG RESETSTAT do?

It resets the counters shown by `INFO`, like `keyspace_hits`, `keyspace_misses`, command stats and error stats. It is handy before a load test so you only see numbers for that test.

## 292: How do you see per-command statistics?

```bash
INFO commandstats
```

It shows for each command how many times it was called, total and average time in microseconds, and how many calls failed. It is a fast way to see which commands use the most CPU time.

## 293: How do you load a lot of data into Redis quickly?

Use pipe mode with a file in RESP or plain command format:

```bash
cat data.txt | redis-cli --pipe
```

`data.txt` has one command per line, like `SET key:1 value1`. `--pipe` sends everything as fast as possible and reports errors at the end. From code, use large pipelines in chunks.

## 294: How do you run a Lua script from a file with redis-cli?

```bash
redis-cli --eval rate_limit.lua rl:user:1 , 100 60
```

Keys come before the comma, arguments after it. Note the spaces around the comma.

## 295: How do you debug a Lua script?

- Use `redis.log(redis.LOG_WARNING, "value: " .. tostring(x))` to write to the Redis log.
- Return intermediate values from the script while developing.
- `redis-cli --ldb --eval script.lua key , arg` starts the Lua debugger, with step, breakpoints and variable printing. Use it on a dev server only, since it can block the server in sync mode.

## 296: Can Lua scripts call any Redis command?

Most commands, but not all. Blocking commands like `BLPOP` don't block inside scripts, and some commands like `SUBSCRIBE` are not allowed. Scripts also cannot access the network or files; they run in a sandbox. Since Redis 7.0, scripts can declare flags in a shebang line (`#!lua flags=no-writes`) to tell Redis how they behave.

## 297: How do you store a large list of IDs for a user efficiently?

If the IDs are integers and you only need membership, a set of integers uses the compact `intset` encoding up to 512 members. For bigger sets of dense integer IDs, a bitmap is even smaller. If you need ordering, use a sorted set. If you only need "have we seen it" with a small error rate, use a Bloom filter.

## 298: What is the difference between EXPIRE on a key and a TTL in a sorted set score?

A key TTL deletes the whole key. Storing an expiry time as a sorted set score lets you expire single members, by removing them with `ZREMRANGEBYSCORE key -inf <now>` when you read or on a timer. This is how you get per-member expiration for sets and lists, which have no native field TTL. Hashes have native field TTLs since Redis 7.4.

## 299: How do you check the health of Redis from a load balancer or Kubernetes?

Use `PING` for liveness. For readiness, check more: that the node is a primary or a synced replica (`INFO replication`, `master_link_status:up`), that persistence is not failing (`rdb_last_bgsave_status:ok`), and that the dataset is loaded (`loading:0` in `INFO persistence`).

```bash
redis-cli -a "$REDIS_PASSWORD" PING
```

## 300: What should you monitor and alert on in production?

- Memory near `maxmemory` and rising `evicted_keys` (if you don't expect eviction).
- Fragmentation ratio far above 1.5 or below 1.
- Latency (p99), slow log entries and blocked clients.
- Connection count and rejected connections.
- Replication link down or lag growing.
- Failed RDB or AOF writes.
- Cache hit ratio dropping.
- CPU usage of the main thread near 100%.

# Advanced Questions (301-450)

## 301: How does the Redis event loop work?

Redis uses its own small event library (`ae`). The main thread waits on epoll (Linux) or kqueue (macOS/BSD) for sockets that are ready to read or write, and for timers. When a socket is readable, Redis reads the data into the client's query buffer, parses full commands, runs them and puts replies in the output buffer. Timers run `serverCron` (by default 10 times per second, set by `hz`) for background work like expiring keys, stats and rehashing. Because everything runs on one thread, one slow command delays all clients.

## 302: What do I/O threads do and when should you turn them on?

With `io-threads N`, Redis uses extra threads to read from sockets, parse commands and write replies. The main thread still runs every command, so atomicity does not change. It helps when the server is limited by network work, for example many clients and large replies, on a machine with spare cores. It does not help if the bottleneck is slow commands. Redis 8 reworked the threading model and gets much better throughput from I/O threads than older versions. Start with about one thread less than the number of cores you can give Redis, and measure.

## 303: What work does Redis do in background threads?

The BIO (background I/O) threads handle:

- Closing files, for example the old AOF after a rewrite.
- `fsync` of the AOF with `appendfsync everysec`.
- Lazy freeing of large values (`UNLINK`, `FLUSHALL ASYNC`, and lazy eviction or expiry when enabled).

Forked child processes (not threads) handle RDB snapshots, AOF rewrites and disk-based full syncs.

## 304: How does BGSAVE use fork and copy-on-write?

`BGSAVE` calls `fork()`. The child gets a copy of the parent's memory pages, but the OS shares them until one side writes to a page. The child writes the snapshot from its frozen view, while the parent keeps serving. Every page the parent changes during the snapshot gets copied, so memory use can grow up to twice the dataset in a write-heavy workload. The fork itself is not free either: copying page tables for a 50 GB process can take hundreds of milliseconds and blocks the main thread (`latest_fork_usec` in `INFO`).

## 305: Why should you disable Transparent Huge Pages for Redis?

With THP, the OS uses 2 MB pages. After a fork, a write to any byte copies the whole 2 MB page instead of 4 KB, which makes copy-on-write much more expensive and causes latency spikes and memory growth. Redis logs a warning at startup if THP is enabled. Set it to `never` or `madvise`:

```bash
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

## 306: Why does Redis recommend vm.overcommit_memory = 1?

When Redis forks for a snapshot, the kernel may refuse the fork if it thinks there is not enough memory to copy everything, even though copy-on-write will only copy a small part. With `vm.overcommit_memory = 1`, the kernel allows the fork. Without it, `BGSAVE` can fail with "Cannot allocate memory" on a machine that has plenty of free RAM for the real copy.

## 307: How does key expiration work internally?

Redis uses two methods:

- **Lazy (passive)**: when a client touches a key, Redis checks the TTL and deletes the key if it has expired.
- **Active**: a periodic job samples keys that have a TTL and deletes the expired ones. If many of the sampled keys were expired, it keeps going, within a time budget, so it does not block the server for long.

This means expired keys that nobody reads can stay in memory for a while. `active-expire-effort` (1-10) makes the active cycle more aggressive at the cost of CPU.

## 308: How do replicas handle expired keys?

Replicas don't expire keys on their own. The primary deletes the key (lazily or actively) and sends a `DEL` (or `UNLINK`) to replicas. To avoid returning stale data, a replica treats a logically expired key as missing when a client reads it, even before the `DEL` arrives. This keeps the dataset consistent between primary and replicas.

## 309: How are TTLs stored and how precise are they?

TTLs are stored as absolute Unix times in milliseconds in a separate dictionary (the expires dict), keyed by the same key. Because they are absolute, the clock matters: if the server's clock jumps forward, keys expire early. When an RDB is loaded, expired keys are dropped (on a primary). Precision is milliseconds, but deletion can happen later than the exact time because of the sampling.

## 310: How does the Redis dictionary (hash table) work?

The main keyspace and the `hashtable` encoding use a hash table with chaining. When it gets too full, Redis grows it, but it does not rehash everything at once. It keeps two tables and moves buckets a few at a time on each operation and in the cron job (incremental rehashing). During rehashing, lookups check both tables. This avoids long pauses on huge tables. In Redis 8 the internal hash table implementation was reworked to use less memory per key, but the idea of incremental resizing stays.

## 311: What is SDS?

SDS (Simple Dynamic String) is the string type Redis uses internally. It stores the length and the free space in a header before the bytes. This makes `STRLEN` O(1), makes strings binary-safe, and avoids repeated reallocations because appends reserve extra space. There are several header sizes so short strings have small overhead.

## 312: What is the difference between embstr and raw encoding?

Both store strings. `embstr` is used for strings up to 44 bytes: the Redis object header and the SDS string are allocated in one block, which is faster and uses less memory. `raw` is used for longer strings, with two separate allocations. A string that is modified (for example with `APPEND`) is converted to `raw`. Small integers use `int` encoding, and Redis keeps shared objects for integers 0-9999 when eviction policy allows it.

## 313: How is a sorted set implemented?

Large sorted sets use two structures together: a skip list ordered by score (and member), and a hash table from member to score. The hash table gives O(1) `ZSCORE`. The skip list gives O(log N) inserts, deletes and range queries, plus rank lookups because each level stores span counts. Small sorted sets use a listpack, which stores members and scores next to each other in one block of memory.

## 314: What is a listpack and why did it replace ziplist?

A listpack is a compact sequence of entries in one contiguous block of memory. Each entry stores its own length at the end, so you can walk backwards. The old ziplist stored the length of the previous entry in each entry, so growing one entry could force updates to all following entries (cascade update). Listpack avoids that. Since Redis 7.0, listpack is used for small hashes, sorted sets and list nodes; ziplist remains only for loading old RDB files.

## 315: What is a quicklist?

A quicklist is the encoding for larger lists. It is a doubly linked list where each node is a listpack holding several items. You get cheap pushes and pops at both ends from the linked list, and good memory use from the listpacks. `list-max-listpack-size` sets the node size, and `list-compress-depth` can LZF-compress inner nodes that are rarely touched.

## 316: How are streams stored internally?

A stream uses a radix tree (rax) keyed by entry ID. Each node of the tree points to a listpack that holds many entries. Entries in the same listpack share a "master entry" with field names, so if all your entries have the same fields, the field names are stored once. This makes streams very memory efficient. Consumer groups have their own structures: the last delivered ID and a pending entries list stored in another radix tree.

## 317: How does Redis decide when to convert compact encodings?

On every write to a small collection, Redis checks the limits (`*-max-listpack-entries` and `*-max-listpack-value`). If the new element count or element size goes over the limit, it converts the whole collection to the full encoding. The conversion is one-way in most cases; deleting elements does not convert back. A single big value added to a hash can turn it into a hash table permanently.

## 318: How does memory fragmentation happen and how do you fix it?

Redis uses jemalloc. When you delete or resize many values, freed memory is left in small gaps that the allocator can't always give back to the OS. `used_memory_rss` (what the OS sees) becomes much bigger than `used_memory`. `mem_fragmentation_ratio` above about 1.5 is a sign of this.

Fixes:

- Turn on active defrag (`activedefrag yes`), which moves values into fewer pages while the server runs.
- Restart a replica and fail over to it.
- Avoid workloads that create and delete many differently sized values if you can.

A ratio below 1 means Redis is swapping, which is worse.

## 319: How does active defragmentation work?

When enabled, Redis checks fragmentation in the cron job. If it is over thresholds (`active-defrag-ignore-bytes`, `active-defrag-threshold-lower`), it walks the keyspace and reallocates values that live in poorly used pages, using jemalloc hints. It spends a limited share of CPU (`active-defrag-cycle-min`, `active-defrag-cycle-max`) so it doesn't hurt latency much. It only works with the jemalloc build that Redis ships.

## 320: What is the memory overhead per key?

Each key costs more than its name and value: the dictionary entry, the Redis object header, the SDS headers, an entry in the expires dictionary if it has a TTL, and allocator rounding. In older versions that added up to roughly 50-90 bytes per key for small strings. Redis 8 reduced this overhead, but with tens of millions of tiny keys it still adds up. That is why grouping small values into hashes saves so much memory.

## 321: How does Redis compute used memory against maxmemory?

`used_memory` counts what Redis allocated, including data, client buffers, replication backlog, and Lua and module memory. When comparing against `maxmemory`, Redis subtracts replica output buffers and AOF buffers, so those don't cause eviction of data. Still, big client output buffers or the replication backlog can push the real process size well above `maxmemory`. Leave headroom on the machine for that and for copy-on-write during forks.

## 322: How does the eviction process work step by step?

Before running a command that may use memory, Redis checks if it's over `maxmemory`. If so, and the policy allows eviction, it samples keys from the right dictionary (all keys or keys with TTL), scores them by idle time, frequency or TTL, and keeps the best candidates in a pool of 16. It evicts the best candidate and repeats until memory is under the limit or a time limit is hit. If it can't free enough, the command fails with an OOM error. With `lazyfree-lazy-eviction yes`, the freeing happens in a background thread.

## 323: Why can a write still fail with OOM when eviction is on?

- The policy is `volatile-*` and no keys have a TTL.
- The command needs more memory than eviction can free in its time slice.
- Memory is used by things that can't be evicted, like client buffers or Lua.
- The policy is `noeviction`.

The error is `OOM command not allowed when used memory > 'maxmemory'`. Read-only commands still work.

## 324: How does replication work?

1. The replica connects and sends `PSYNC` with the replication ID and offset it has.
2. If the primary can continue from that offset (same ID and the data is still in the backlog), it sends only the missing commands (partial sync).
3. Otherwise it does a full sync: it creates an RDB snapshot, sends it, and buffers new writes, which it sends after the RDB.
4. After that, the primary streams every write command to the replica, and the replica acknowledges its offset every second.

## 325: What is the replication ID and offset?

Each primary has a random replication ID that names its history, and an offset that grows with every byte of the replication stream. A replica with the same ID and an offset still in the backlog can resume with a partial sync. When a replica is promoted, it gets a new ID but remembers the old one, so other replicas of the old primary can still do a partial sync against it.

## 326: What is the replication backlog and how big should it be?

The backlog is a circular buffer on the primary with the most recent replication stream. If a replica disconnects briefly and its offset is still in the backlog, it only needs a partial sync. If the gap is bigger than the backlog, it needs a full sync, which is expensive. The default `repl-backlog-size` is 1 MB, which is small for busy servers. Size it as write throughput times the longest disconnect you want to survive, for example 10 MB/s × 60 s = 600 MB.

## 327: What is diskless replication?

With `repl-diskless-sync yes` (the default in recent versions), the primary streams the RDB directly over the socket to replicas instead of writing it to disk first. It helps when disks are slow. `repl-diskless-sync-delay` waits a few seconds so several replicas can share one transfer. On the replica side, `repl-diskless-load` can load the RDB straight from the socket into memory instead of saving it to disk first.

## 328: What happens when a primary without persistence restarts?

This is a classic data loss case. If the primary has persistence off and restarts quickly (for example, by a process supervisor), it comes up empty. Its replicas see it back, sync with it, and wipe their own data. Everything is gone. If you run a primary without persistence, don't let it restart automatically, or make sure Sentinel fails over to a replica first.

## 329: How does Sentinel detect failures and fail over?

1. Each Sentinel pings the primary. If it gets no valid reply within `down-after-milliseconds`, it marks it **subjectively down** (SDOWN).
2. It asks other Sentinels. If at least `quorum` agree, the primary is **objectively down** (ODOWN).
3. Sentinels elect a leader for this failover. The leader needs votes from a majority of all Sentinels, not just the quorum.
4. The leader picks the best replica (priority, replication offset, run ID), promotes it, and points the other replicas to it.
5. Clients learn the new primary from Sentinel.

Each failover has a configuration epoch, so the newest config wins.

## 330: Why do you need a majority of Sentinels for failover?

The quorum only decides when a primary is considered down. To actually perform a failover, the leader needs a majority of all known Sentinels. With 3 Sentinels, you need 2. This prevents a single isolated Sentinel from promoting a replica on its own. With only 2 Sentinels, losing one machine means no majority, so no failover can happen.

## 331: What is split brain in Redis and how do you limit it?

If the network splits so the old primary is on one side with some clients and the Sentinels promote a replica on the other side, you have two primaries. Clients on the old side keep writing, and when the network heals, the old primary becomes a replica and those writes are lost. `min-replicas-to-write` and `min-replicas-max-lag` make the old primary stop accepting writes when it can't reach its replicas, which limits the loss to a short window.

## 332: How does Redis Cluster's gossip protocol work?

Each node keeps a TCP connection to every other node on the cluster bus. Nodes send ping and pong messages that include info about themselves and a few random other nodes. This spreads knowledge about who is alive, who owns which slots and the config epochs. Failure reports also travel this way: when enough primaries report a node as failing, it is marked as `FAIL` and the failover starts.

## 333: What are config epochs in Redis Cluster?

Every primary has a config epoch, a number that works like a version. When a replica wins a failover, it gets a new epoch higher than any other. If two nodes claim the same slot, the one with the higher epoch wins. This is how the cluster settles conflicts after failovers or network splits.

## 334: How does slot migration work in Redis Cluster?

The classic process: the target node marks the slot as `IMPORTING`, the source marks it as `MIGRATING`. Then keys are moved in batches with `MIGRATE`. During this, the source answers for keys it still has and sends `ASK` redirects for keys already moved. When all keys are moved, both nodes run `CLUSTER SETSLOT <slot> NODE <target>` and the change spreads. Multi-key operations on a slot under migration can fail with `TRYAGAIN`.

Redis 8.4 added atomic slot migration (`CLUSTER MIGRATION`), where the target streams the whole slot and takes ownership in one step, which avoids most of the `ASK` and `TRYAGAIN` handling.

## 335: What consistency guarantees does Redis Cluster give?

Redis Cluster is not strongly consistent. Replication is asynchronous, so a primary can confirm a write, crash before sending it to the replica, and the replica that takes over won't have it. During a network split, a primary on the minority side keeps accepting writes until `cluster-node-timeout`, and those writes are lost when it is demoted. `WAIT` reduces but does not remove these windows. Redis aims for high availability and low latency, not linearizability.

## 336: Does WAIT make Redis strongly consistent?

No. `WAIT` only tells you that a number of replicas received the write. A failover can still pick a replica that didn't get it, if more than one replica exists and they are at different offsets. And `WAIT` doesn't roll back anything if it times out: the write is already done on the primary. It improves durability, but you should still not treat Redis as a consensus system.

## 337: Why is a long-running Lua script dangerous?

A script blocks the whole server until it finishes, because nothing else runs on the main thread in the meantime. After `busy-reply-threshold` (default 5 seconds), Redis starts answering other clients with a `BUSY` error. You can stop a read-only script with `SCRIPT KILL`. If the script already wrote data, it can't be killed, since that would leave a half-applied change; the only way out is `SHUTDOWN NOSAVE`. Keep scripts short and bounded, and never loop over large or unbounded collections.

## 338: How are Lua scripts replicated?

Since Redis 7.0, scripts are always replicated by their effects: the primary sends the write commands the script actually ran (wrapped in `MULTI/EXEC`), not the script itself. Before that, scripts could be replicated as the script text, which required them to be deterministic (no random values, no time-based logic) so replicas would get the same result. Effects replication removes that restriction.

## 339: What are script and function flags?

Flags declare how code behaves, so Redis can decide where it may run:

- `no-writes`: the script only reads. It can run on replicas and with `EVAL_RO` / `FCALL_RO`, and it is allowed during OOM.
- `allow-oom`: allows writes even when over `maxmemory`.
- `allow-stale`: allows running on a stale replica.
- `no-cluster`: refuses to run in cluster mode.
- `allow-cross-slot-keys`: allows touching keys in different slots on the same node.

```lua
#!lua flags=no-writes
return redis.call('GET', KEYS[1])
```

## 340: Why must all keys be passed in KEYS even if Redis does not enforce it?

In standalone mode, a script can technically build key names and access them. But in cluster mode the script runs on one node, chosen by the keys in `KEYS`. If it accesses a key in another slot, it fails or touches the wrong data. ACL key permissions are also checked against declared keys. And future features (like better routing) rely on it. Treat undeclared keys as a bug.

## 341: How do Lua scripts handle errors and partial writes?

If a script fails halfway, the writes it already made stay. There is no rollback. To be safe, do all checks and reads first, then all writes at the end, so an error is likely to happen before anything is changed. Use `redis.pcall` if you want to handle an error and keep going. Return errors with `redis.error_reply("message")`.

## 342: What are the risks of big keys?

- `DEL`, `HGETALL`, `SMEMBERS` or `LRANGE 0 -1` on them block the main thread.
- They make memory hard to balance in a cluster, since one key can't be split across nodes.
- Migrating a big key between slots blocks both nodes during `MIGRATE`.
- Eviction of one big key frees a lot of memory at once and can cause a latency spike.
- Replicating or reading them saturates the network.

Rule of thumb: keep strings under about 1 MB and collections under a few thousand to tens of thousands of elements, and split anything larger.

## 343: How do you safely delete a huge key?

Use `UNLINK`, which frees memory in a background thread. If you're on an old version or need to control the pace, delete it in pieces:

```js
// delete a big hash in batches
let cursor = "0";
do {
  const [next, fields] = await redis.hscan("big:hash", cursor, "COUNT", 500);
  cursor = next;
  const names = fields.filter((_, i) => i % 2 === 0);
  if (names.length) await redis.hdel("big:hash", ...names);
} while (cursor !== "0");
```

For lists use `LTRIM` in steps, for sorted sets `ZREMRANGEBYRANK`.

## 344: What lazyfree options exist and when should you enable them?

```
lazyfree-lazy-eviction yes
lazyfree-lazy-expire yes
lazyfree-lazy-server-del yes
lazyfree-lazy-user-del yes
lazyfree-lazy-user-flush yes
replica-lazy-flush yes
```

They make Redis free memory in the background for evictions, expirations, implicit deletes (like `SET` overwriting a big key or `RENAME`), user `DEL` calls, `FLUSHALL`/`FLUSHDB`, and replica flushes during full sync. Turning them on helps latency when you have big values. The cost is that memory goes down a little later.

## 345: What are the main causes of latency spikes in Redis?

- Slow commands (O(N) on big collections, `KEYS`, big `SORT`).
- Fork for RDB or AOF rewrite on a large dataset.
- AOF fsync stalls on a slow or busy disk.
- Swapping (the OS moved Redis memory to disk).
- Transparent Huge Pages.
- Expiring many keys at the same time.
- Evicting or deleting big values on the main thread.
- Noisy neighbors on virtual machines.
- Network problems or a saturated NIC.

Use `LATENCY DOCTOR`, the slow log and `--intrinsic-latency` to narrow it down.

## 346: How can mass expiration cause latency?

If millions of keys share the same expire time (for example, all created by a batch job with the same TTL), the active expire cycle finds that most sampled keys are expired and keeps working in a loop. Redis caps the time per cycle, but it still uses a lot of CPU, and clients see higher latency for a while. Adding random jitter to TTLs avoids this.

## 347: How does AOF fsync cause latency with everysec?

With `everysec`, a background thread calls `fsync` once per second. If the disk is slow and the previous `fsync` is still running after two seconds, the main thread waits before the next write to the AOF, so commands get delayed. This shows up as `aof-fsync-always`/`aof-write-pending-fsync` latency events. `no-appendfsync-on-rewrite yes` skips fsync during rewrites, which helps latency but risks more data loss if the server crashes then.

## 348: How do you tell if Redis is swapping?

Check `mem_fragmentation_ratio` in `INFO memory`: below 1 usually means part of Redis's memory is on disk. Also check `/proc/<pid>/smaps` for `Swap` values or use `vmstat`. Swapping kills Redis latency. Fix it by setting `maxmemory` with room to spare, reducing the dataset, adding RAM, or lowering `vm.swappiness`.

## 349: How do slow subscribers affect pub/sub?

Redis pushes messages to every subscriber's output buffer. If a subscriber can't read fast enough, its buffer grows in Redis's memory. When it passes the `client-output-buffer-limit pubsub` limits, Redis disconnects it and the messages in the buffer are lost. With many slow subscribers, memory can grow fast. Watch `omem` in `CLIENT LIST` and keep subscriber processing fast or hand work off to a queue.

## 350: How do you plan Redis capacity?

1. Estimate the number of keys and average size per key, including overhead (measure with `MEMORY USAGE` on samples).
2. Add memory for client buffers, the replication backlog and fragmentation (often 20-30%).
3. If you use RDB or AOF rewrite, leave room for copy-on-write, up to the dataset size in heavy write loads.
4. Measure ops per second per core in a benchmark that looks like your traffic.
5. Plan for growth and decide when to shard.

A common rule is to keep `maxmemory` at no more than about half to two thirds of the machine's RAM when persistence is on.

## 351: When should you shard Redis?

When one node can't keep up: the dataset doesn't fit in the memory you can give a single server, the main thread CPU is close to 100% on writes, or the network of one node is saturated. If only reads are the problem, replicas or client-side caching may be enough. Sharding adds complexity (multi-key limits, more nodes to operate), so first make sure the problem isn't a few slow commands or big keys.

## 352: What are the options for sharding Redis?

- **Redis Cluster**: built-in, automatic failover, slot-based routing in the client.
- **Client-side sharding**: the app hashes keys to independent Redis servers (consistent hashing). Simple but no automatic rebalancing.
- **Proxy-based sharding**: a proxy (like Twemproxy or Envoy's Redis proxy) routes commands, so clients don't need cluster support.
- **Managed services**: most managed offerings use Cluster or their own proxy layer.

Cluster is the default choice today.

## 353: How do you design keys for Redis Cluster?

- Keep data used together under the same hash tag, like `{user:42}:cart` and `{user:42}:profile`, so you can use transactions and scripts on them.
- Don't put everything under a few hash tags, or a few slots get all the load.
- Avoid one global key that every request touches (a global counter or a global sorted set). Split it into many keys and merge on read.
- Plan multi-key operations up front, because cross-slot commands will fail.

## 354: How would you build a global leaderboard with 100 million players?

A single sorted set with 100 million members uses several GB and lives on one node, which may be fine for memory but makes that node hot. Options:

- Keep one sorted set if one node can handle it, and use replicas for reads like "top 100".
- Shard players into N sorted sets by hash, and compute the top K by fetching the top K from each and merging.
- For a player's global rank, sum their rank in each shard (`ZCOUNT` of higher scores per shard).
- Keep "top 1000" in a separate small sorted set that's updated when a score crosses the threshold.

Approximate ranks ("top 5%") from score buckets are often good enough for most players.

## 355: How would you design a rate limiter for a large API gateway?

- Use a sliding window counter: two fixed windows (current and previous minute) weighted by time, which is cheap and close to a true sliding window.
- Keep each user's keys under a hash tag so they live on one node.
- Do the check and increment in one Lua script or Function to avoid races and round trips.
- Set TTLs on all counters.
- Decide what to do if Redis is down (fail open or fail closed).
- For very hot keys, allow a small local budget per gateway instance and sync with Redis less often.

```lua
-- KEYS[1] current window, KEYS[2] previous window
-- ARGV: limit, window_ms, elapsed_ms_in_current
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local elapsed = tonumber(ARGV[3])

local prev = tonumber(redis.call('GET', KEYS[2]) or '0')
local curr = tonumber(redis.call('GET', KEYS[1]) or '0')
local estimate = prev * ((window - elapsed) / window) + curr

if estimate >= limit then
  return 0
end
redis.call('INCR', KEYS[1])
redis.call('PEXPIRE', KEYS[1], window * 2)
return 1
```

## 356: What is the Redlock algorithm?

Redlock tries to get a lock on N independent Redis primaries (usually 5). The client sets the same random value with `SET NX PX` on each, and it holds the lock if it got a majority within a time much shorter than the TTL. The valid lock time is the TTL minus the time spent getting it. To release, it runs the safe delete script on all nodes. The idea is that the lock survives the failure of a minority of nodes.

## 357: What are the criticisms of Redlock?

Martin Kleppmann's critique points out that Redlock depends on timing assumptions: bounded network delay, bounded process pauses and clocks that don't jump. A GC pause longer than the TTL lets two clients think they hold the lock. Clock jumps on a Redis node can make a lock expire early. His conclusion: for efficiency locks (avoiding duplicate work), a single Redis lock is enough; for correctness locks, use fencing tokens and a system with real consensus like ZooKeeper or etcd. Antirez replied that the assumptions are reasonable in practice. Interviewers mostly want you to know the debate and the trade-off.

## 358: What is a fencing token?

A number that increases each time the lock is granted (for example from `INCR lock:job:token`). The lock holder sends this token with every write to the protected resource, and the resource rejects any write with a lower token than one it has already seen. If an old holder wakes up after a pause and tries to write, its token is lower, so the write is refused. Redis can hand out the token, but the resource itself has to check it.

## 359: How would you design a reliable job queue on Redis streams?

- Producers `XADD` jobs with `MAXLEN ~` or `MINID` trimming.
- Workers in one consumer group use `XREADGROUP ... >` with `BLOCK`.
- After success, `XACK` (or `XACKDEL` on newer versions to ack and delete in one step).
- A reaper uses `XAUTOCLAIM` to take entries idle for too long.
- Track delivery count from `XPENDING`; after N failed attempts, move the entry to a dead letter stream and ack it.
- Make handlers idempotent, because an entry can be processed twice if a worker crashes after doing the work but before acking.

## 360: How do you handle poison messages in a stream?

A poison message is one that always fails and keeps getting reclaimed. Use the delivery counter that Redis keeps for each pending entry:

```bash
XPENDING jobs workers - + 100
# each row: id, consumer, idle ms, delivery count
```

If the count is above a limit, copy the entry to `jobs:dead` with `XADD`, then `XACK` it in the main group. Someone can inspect the dead letter stream later.

## 361: What does at-least-once delivery mean in Redis streams, and how do you get exactly-once effects?

With consumer groups, an entry stays pending until it is acknowledged. If a consumer crashes after processing but before `XACK`, the entry is delivered again, so you get at-least-once delivery. To get exactly-once effects, make processing idempotent: store the entry ID (or a business ID) in the same transaction as the result, or check a dedup key before acting. On the producer side, Redis 8.6 added `IDMP` and `IDMPAUTO` options to `XADD`, which drop duplicate adds from producer retries.

## 362: How do streams compare to Kafka?

Both are append-only logs with consumer groups. Redis streams are simpler to run, have very low latency, and are good for moderate volumes that fit in memory. Kafka stores data on disk, keeps months of history cheaply, partitions topics across many brokers, and handles huge throughput with strong ordering per partition. A single Redis stream lives on one node, so to scale you need to split it into several streams yourself. Pick Redis streams for job queues and short-lived event logs; pick Kafka for large event pipelines and long retention.

## 363: How do you scale a stream beyond one node?

Split it into several streams, for example `events:{0}` to `events:{15}`, and choose the stream by hashing an ID (like the user ID) so related events stay ordered in one stream. Each stream lands on a slot, spread over the cluster. Consumers run one group per stream, or a worker pool that reads from all of them. Ordering is only guaranteed inside one stream.

## 364: How does consumer group lag work?

Since Redis 7.0, `XINFO GROUPS` shows `entries-read` and `lag` for each group. Lag is how many entries in the stream have not been delivered to the group yet. It is accurate as long as there were no deletions in a way Redis can't track; otherwise it may be shown as null. Monitor it to see if consumers are falling behind.

## 365: How would you design a session store for millions of users?

- One hash per session (`sess:<id>`) with a TTL, or a string with a serialized session if it is always read whole.
- Sliding expiration with `GETEX` or `EXPIRE` on each request, maybe only when the TTL is below half to reduce writes.
- Index sessions per user (`user:42:sessions` set) to support "log out everywhere".
- High availability through replicas and Sentinel or Cluster.
- `allkeys-lru` is risky because it can log people out; size memory properly and use `volatile-lru` or `noeviction`.
- Use AOF `everysec` if losing sessions on restart is a problem.

## 366: How do you implement "log out from all devices"?

Keep a set of session IDs per user:

```bash
SADD user:42:sessions sess:abc sess:def
```

To log out everywhere, read the set and delete each session plus the set:

```js
const ids = await redis.smembers("user:42:sessions");
await redis.unlink(...ids, "user:42:sessions");
```

Clean up the set when single sessions expire, or store a "session version" per user that every request checks; bumping the version invalidates all sessions at once.

## 367: How do you cache data that is expensive to compute and must never be stale for long?

- Short TTL plus background refresh: a job refreshes keys before they expire, so users never wait.
- Stale-while-revalidate: store the value with a "soft" expiry inside it and a longer real TTL. If the soft expiry passed, return the old value and trigger a refresh with a lock.
- Event-based invalidation: delete or update the key when the source changes (via CDC or app events).

## 368: What is probabilistic early expiration?

Also called XFetch. Each request may decide to recompute the value before it expires, with a probability that rises as the expiry gets closer. With `delta` being how long the recompute takes and `beta` around 1:

```js
function shouldRefresh(expiresAt, delta, beta = 1) {
  return Date.now() - delta * beta * Math.log(Math.random()) >= expiresAt;
}
```

`Math.log(Math.random())` is negative, so this subtracts a random amount of time. Usually only one request refreshes a bit early, and the stampede never happens.

## 369: How do you keep a cache consistent with the database in a write-heavy system?

Race example: request A reads old data from the DB (cache miss), request B updates the DB and deletes the cache, then A writes the old data into the cache. The cache is now stale until the TTL.

Ways to reduce it:

- Short TTLs.
- Delayed double delete: delete the key, update the DB, and delete it again after a short delay.
- Write the cache with a version or timestamp and only overwrite if newer (Lua or `SET ... IFEQ`).
- Drive invalidation from the database change stream (CDC with Debezium, for example), so the order follows the DB commit order.

## 370: How do you warm a cache after a restart or a deploy?

A cold cache sends all traffic to the database at once. Options:

- Keep persistence on so Redis restarts with data.
- Run a warm-up job that loads the most popular keys before sending traffic.
- Shift traffic gradually to new instances.
- Use stampede protection (locks or request coalescing) so each key is loaded once.
- Replicate from the old instance before switching.

## 371: How do you handle multi-region setups with Redis?

Redis Open Source has no built-in multi-primary replication. Common setups:

- One primary region, replicas in other regions for local reads, and writes sent to the primary region. Failover is manual or scripted.
- Separate independent caches per region, each filled from a local database copy.
- Redis Software or Redis Cloud Active-Active, which uses CRDTs so each region can take writes and conflicts are merged automatically.

Cross-region replication adds lag, so design reads that can accept stale data.

## 372: What are CRDTs in Active-Active Redis?

CRDTs (Conflict-free Replicated Data Types) are data types designed so concurrent updates in different regions can be merged without coordination and always end in the same state. For example, a counter merges by adding all increments, and a set can use "add wins" when one region adds and another removes the same member at the same time. Active-Active Redis (in Redis Software and Redis Cloud) builds the Redis data types on top of CRDTs.

## 373: What is client-side caching invalidation like at scale?

With default tracking, Redis keeps a table of keys and which clients read them. This uses memory, capped by `tracking-table-max-keys`; when the table is full, Redis invalidates old entries to make room. Each write to a tracked key sends invalidation messages to all clients that read it. For very hot keys that change often, this can create lots of messages. Broadcast mode with prefixes avoids the tracking table but sends more invalidations. Also, the client must drop its whole local cache when its connection to Redis breaks, because it may have missed invalidations.

## 374: How does Redis handle many clients reading a key that a client is tracking in OPTIN mode?

In `OPTIN` mode, Redis only tracks a read if the client sent `CLIENT CACHING yes` right before it. This lets the client cache only the keys it chooses, which keeps the server tracking table small and avoids invalidations for keys the client doesn't care about. It is the best mode when only a few keys are hot.

## 375: What is the Redis threat model for an exposed server?

Redis assumes it runs in a trusted network. An exposed server without a password lets attackers:

- Read and delete all data.
- Use `CONFIG SET dir` and `CONFIG SET dbfilename` plus `SAVE` to write files on disk, for example an SSH key into `authorized_keys` or a cron file, which can lead to remote code execution.
- Load malicious modules with `MODULE LOAD` if allowed.
- Use the server for cryptomining via Lua or modules.

Since Redis 7.0, `enable-protected-configs`, `enable-module-command` and `enable-debug-command` default to `no`, which blocks changing sensitive paths and loading modules at runtime. Still, never expose Redis to the internet.

## 376: What are the protected configs in Redis 7+?

```
enable-protected-configs no
enable-debug-command no
enable-module-command no
```

With these defaults, `CONFIG SET` can't change dangerous settings like `dir` and `dbfilename`, `DEBUG` is disabled, and `MODULE LOAD` is disabled at runtime. You can set them to `local` to allow only local connections. These close several classic attack paths.

## 377: How do you design ACLs for least privilege?

- Turn off the `default` user, or give it no permissions.
- One user per service with only the key patterns it uses (`~orders:*`).
- Remove whole categories like `-@dangerous` and `-@admin`, then add back only what's needed.
- Give admin and monitoring tools their own users.
- Use `%R~` for read-only access to shared data.
- Use selectors when a user needs different command sets for different keys.
- Check `ACL LOG` for denied commands to find gaps or attacks.

## 378: What are ACL selectors?

Selectors (Redis 7.0+) let a user have several sets of rules. A command is allowed if it matches the root permissions or any selector.

```bash
ACL SETUSER svc on >pass +@read ~public:* (+@write ~svc:*)
```

This user can read `public:*` keys, and can read and write `svc:*` keys. Without selectors, the write permission would apply to all key patterns.

## 379: What does ACL LOG show?

It lists recent denied commands and failed logins: the user, the client, the command, the key or channel, and how many times it happened. It is useful for debugging ACLs and spotting brute-force attempts.

```bash
ACL LOG 10
ACL LOG RESET
```

## 380: What security issues have affected Lua scripting?

Several CVEs over the years were bugs in the embedded Lua interpreter or its libraries (`cjson`, `cmsgpack`, `struct`, `bit`) that let a user who can run scripts crash the server or run code. In 2025, a critical use-after-free bug in the Lua parser (CVE-2025-49844) allowed remote code execution by any authenticated user who could run Lua. The lesson: keep Redis patched, and deny `@scripting` in ACLs to users who don't need it.

## 381: How do you secure Redis in a multi-tenant setup?

Real isolation needs separate Redis instances per tenant, since all keys share the same memory, CPU and main thread. One tenant's slow command affects everyone. If you share an instance, use ACL users with key prefixes per tenant, deny `KEYS`, `FLUSHALL`, `CONFIG`, `DEBUG` and scripting, and enforce rate limits in your app. Managed services often give each tenant a database on a shared cluster with resource limits.

## 382: How do you encrypt data at rest?

Redis Open Source does not encrypt RDB or AOF files itself. Options:

- Encrypted disks or volumes (LUKS, cloud provider disk encryption).
- Encrypt sensitive values in the app before storing them.
- Managed services usually encrypt storage by default.

Remember that backups and RDB files copied elsewhere also need protection.

## 383: How should you store sensitive data in Redis?

- Don't put secrets or personal data in key names, since they show up in logs, `MONITOR`, the slow log and `--bigkeys` output.
- Encrypt or hash sensitive values (store a hashed token, not the raw token).
- Set TTLs on everything sensitive.
- Use TLS on the network.
- Restrict who can run `MONITOR`, `KEYS` and `DEBUG`.

## 384: How do you upgrade Redis with no downtime?

With replication:

1. Upgrade a replica, let it sync.
2. Fail over to it (`SENTINEL FAILOVER mymaster` or `CLUSTER FAILOVER` on the replica).
3. Upgrade the old primary, which is now a replica.

Replicas can usually run a newer version than the primary, but not older. Check release notes for changed defaults, removed configs and RDB format changes, since a newer RDB can't be loaded by an older Redis.

## 385: How do you move from Redis to Valkey or the other way?

They share the same RDB format and protocol up to the fork point (7.2.4), so you can replicate between them or load an RDB from one into the other, as long as the versions are compatible. Newer versions of both have added features and RDB changes the other may not support, so test with your exact versions. Check that the commands and modules you use exist on the target, especially JSON, search and other features that are part of Redis 8.

## 386: What are Dragonfly and KeyDB?

- **KeyDB**: a multithreaded fork of Redis, by Snap. It runs commands on several threads with locks. Development has slowed.
- **Dragonfly**: a newer in-memory store written from scratch, compatible with the Redis and Memcached protocols. It uses a shared-nothing, multi-threaded design and claims much higher throughput per server.

Both can replace Redis for many workloads, but check compatibility with the commands, Lua behavior and cluster features you use.

## 387: How would you design a semantic cache for an LLM app?

1. Embed the user's prompt into a vector.
2. Search a vector index (Query Engine or a vector set) for cached prompts within a similarity threshold.
3. If one is close enough, return its cached answer.
4. Otherwise call the model, then store the prompt vector, the answer and metadata with a TTL.

Filter by things that change the answer, like the model, system prompt version or user permissions. Tune the threshold carefully, since a loose threshold returns wrong answers for different questions.

## 388: How do you store embeddings in a Redis hash for vector search?

Store the vector as raw little-endian float32 bytes:

```python
import numpy as np
import redis

r = redis.Redis()
vec = np.random.rand(768).astype(np.float32)
r.hset("doc:1", mapping={"content": "Redis is fast", "embedding": vec.tobytes()})
```

The index's `DIM`, `TYPE` and `DISTANCE_METRIC` must match how you generate the vectors. With JSON documents, you store the vector as a JSON array of numbers instead.

## 389: What is HNSW and what are its parameters?

HNSW (Hierarchical Navigable Small World) is a graph-based approximate nearest neighbor index. It builds layers of graphs where higher layers have fewer nodes, and a search goes from the top layer down. Parameters:

- `M`: max connections per node. Higher means better recall and more memory.
- `EF_CONSTRUCTION`: how many candidates to consider when building. Higher means better quality and slower inserts.
- `EF_RUNTIME`: how many candidates to consider at query time. Higher means better recall and slower queries.

`FLAT` is the exact alternative: brute force, perfect recall, slow on large data.

## 390: How do vector sets reduce memory?

By default, vector sets quantize vectors to 8-bit integers (`Q8`), which uses about a quarter of the memory of float32 with a small loss in accuracy. You can use `NOQUANT` to keep full precision or `BIN` for binary quantization, which is even smaller and faster but less accurate. `VADD ... REDUCE <dim>` uses random projection to reduce the number of dimensions.

## 391: How do you filter results in a vector set search?

You attach JSON attributes to elements and pass a filter expression to `VSIM`:

```bash
VADD movies VALUES 3 0.1 0.2 0.3 movie:1 SETATTR '{"year": 1999, "genre": "scifi"}'
VSIM movies VALUES 3 0.1 0.2 0.3 COUNT 10 FILTER '.year > 1990 and .genre == "scifi"'
```

`FILTER-EF` controls how many candidates are checked to find enough matches when the filter is strict.

## 392: How does the Query Engine scale in Redis Cluster?

In open source cluster mode, each shard indexes its own keys, and a query is sent to all shards and the results are merged. This works, but every query touches every shard. Redis Software and Redis Cloud have additional options to scale query processing separately from data. For big search workloads, keep indexes lean (index only fields you query) and test query latency with your shard count.

## 393: How do you keep a search index small and fast?

- Index only fields you filter or search on. Use `NOINDEX` on sortable fields you only return.
- Use `TAG` instead of `TEXT` for exact values like status or category.
- Avoid `SORTABLE` on fields you don't sort by, since it copies values into the index.
- Use specific prefixes so the index doesn't scan unrelated keys.
- For vectors, pick the smallest dimension and type that keeps quality acceptable.
- Check `FT.INFO` for index size and indexing failures.

## 394: How do you change a search index schema?

`FT.ALTER` can add fields to an existing index, which triggers indexing of existing documents for the new field. For other changes (removing or changing field types), create a new index with a new name, wait for it to finish indexing (`FT.INFO` shows `percent_indexed`), and then switch the app to it. Using `FT.ALIASADD` and `FT.ALIASUPDATE` lets you switch indexes without changing the app config.

## 395: What happens to data structure invariants when you mix TTLs and big collections?

The TTL applies to the whole key. When a big collection expires, Redis has to free all its elements. If lazy expiry freeing is off, that happens on the main thread and can take a long time, causing a spike. Turn on `lazyfree-lazy-expire` if you have big keys with TTLs, or keep collections small.

## 396: How does Redis Functions differ in persistence and replication from EVAL?

Functions are part of the dataset: they are saved in RDB and AOF, sent to replicas, and loaded on restart. Scripts loaded with `SCRIPT LOAD` live only in the script cache, which is not persisted or replicated to replicas reliably, and is cleared on restart or `SCRIPT FLUSH`. That makes Functions the right place for logic the app depends on. `FUNCTION DUMP` and `FUNCTION RESTORE` let you copy libraries between servers.

## 397: How does the HOTKEYS command help with performance problems?

`HOTKEYS` (Redis 8.6+) reports keys that use a big share of CPU time or network traffic on the server. Before it, you had to guess with `--hotkeys` (which only uses LFU counters and needs an LFU policy), `MONITOR` samples, or app-side metrics. Knowing the hot keys tells you where to add local caching, split keys or move traffic to replicas.

## 398: What are the new LRM eviction policies for?

Redis 8.6 added `allkeys-lrm` and `volatile-lrm`. LRM stands for least recently modified: the eviction looks at when a key was last written, not read. This helps in workloads where some keys are read all the time but are really stale, for example caches with long-lived, frequently read entries where you'd rather keep fresh writes. LRU would keep those old keys because they are read often.

## 399: How does CLUSTER SLOT-STATS help with uneven load?

`CLUSTER SLOT-STATS` reports per-slot metrics, such as key count, CPU time and network bytes. With it you can see which slots are hot and decide which ones to move to less loaded nodes. Before it, you only had per-node stats and had to guess which slots caused the load.

## 400: How do you choose between hashes, JSON and the Query Engine for a product catalog?

- Hashes: fast, small, flat fields. Good if you look products up by ID and maybe index a few fields.
- JSON: nested data like variants and attributes, partial updates with JSONPath.
- Either one plus a Query Engine index if you need filtering, full-text search, facets and sorting.

For a catalog with search, JSON documents with an index on the fields you filter on is a common choice. Keep the database as the source of truth and sync changes into Redis.

## 401: Your Redis CPU is at 100% but ops per second are low. What do you check?

1. `SLOWLOG GET` and `INFO commandstats` to find commands with high `usec_per_call`.
2. Look for `KEYS`, `SMEMBERS`, `HGETALL`, `LRANGE 0 -1`, `SORT` or `ZRANGE` on big keys.
3. Look for heavy Lua scripts or Functions.
4. Check for mass expiration (`expired_keys` jumping) or active defrag using CPU.
5. Check for a hot key with `HOTKEYS` or `--hotkeys`.
6. Check if `MONITOR` is running (`CLIENT LIST` with `cmd=monitor`).

Low ops with high CPU almost always means a few expensive commands, not too much traffic.

## 402: Memory keeps growing even though you set TTLs. What could be wrong?

- Some keys have no TTL (`INFO keyspace` shows `keys` vs `expires`).
- Keys get rewritten with `SET` without `EX`, which removes the TTL.
- Collections keep growing because TTL is reset on each write (`EXPIRE` on every `LPUSH`).
- Client output buffers are large (slow pub/sub subscribers, `MONITOR`).
- The replication backlog or AOF buffers are big.
- Fragmentation: `used_memory_rss` is much higher than `used_memory`.
- Lua script cache growing because scripts are built with values inside instead of using `ARGV`.

## 403: Why can building Lua scripts with string concatenation cause memory problems?

Each distinct script text is cached by its SHA1. If you put values into the script body (`"return redis.call('GET', 'user:" + id + "')"`), every call creates a new script, and the script cache grows forever. It also wastes CPU on compiling. Always keep the script body constant and pass values through `KEYS` and `ARGV`. Since Redis 7.4, scripts sent with `EVAL` are evicted from the cache when there are too many of them, but you should still avoid this pattern.

## 404: Replicas keep doing full syncs in a loop. Why?

Common causes:

- The replication backlog is too small for the write rate, so short disconnects can't be resumed.
- The replica output buffer limit on the primary is too low, so the primary drops the replica during the RDB transfer, and it starts again.
- `repl-timeout` is too short for the time it takes to send and load a big RDB.
- The replica runs out of memory while loading.

Check the logs on both sides for "Client ... scheduled to be closed ASAP for overcoming of output buffer limits" or timeout messages.

## 405: After a failover, some recent writes are missing. Why?

Replication is asynchronous. The primary confirmed those writes to clients, but they hadn't reached the replica that got promoted. When the old primary comes back as a replica, it syncs from the new one and drops the writes it had. To reduce this, use `WAIT` on important writes, `min-replicas-to-write`, and AOF on replicas. If you can't accept any loss, Redis isn't the right store for that data.

## 406: Clients get "LOADING Redis is loading the dataset in memory" errors. What does it mean?

Redis is starting up and reading the RDB or AOF. Until that's done, it refuses most commands. With a big dataset this can take minutes. Options: use a fast RDB preamble for AOF, use replicas so traffic goes elsewhere during restarts, make health checks wait for `loading:0`, and make clients retry with backoff.

## 407: Your app sees random timeouts to Redis but Redis latency looks fine. What do you check?

- Client-side issues: the Node.js event loop is blocked, so replies are read late. Measure event loop lag.
- Too few connections or a connection pool that is exhausted (in clients that use pools).
- Large replies taking long to transfer.
- Network: packet loss, DNS, TLS handshakes for every request, NAT or load balancer idle timeouts closing connections.
- Blocking commands sharing the same connection as normal commands.

Redis's own latency only covers command execution, not what happens in the network or in the client.

## 408: How do you find out which client is sending bad traffic?

```bash
CLIENT LIST
```

Look at `addr`, `name`, `user`, `cmd` (last command), `age`, `idle`, `qbuf` and `omem`. Name your connections with `CLIENT SETNAME` (most libraries support a `connectionName` option) so you can tell services apart. `CLIENT NO-EVICT` and `CLIENT KILL` let you protect or remove specific clients. `MONITOR` in a short window can also help, if the server can take the extra load.

## 409: What does CLIENT PAUSE do and when would you use it?

`CLIENT PAUSE 5000 WRITE` stops processing write commands (or all commands without `WRITE`) for the given time, while still accepting connections. It is used during manual failovers: pause writes on the primary, wait for the replica to catch up, then promote the replica. This avoids losing writes during a planned switch. `CLIENT UNPAUSE` ends it early.

## 410: How would you do a planned failover with no data loss?

With Sentinel: `SENTINEL FAILOVER mymaster` does a forced failover but can lose the last writes. A safer manual process:

1. `CLIENT PAUSE <ms> WRITE` on the primary.
2. Wait until the replica's offset equals the primary's (`INFO replication`).
3. Promote the replica (`REPLICAOF NO ONE`) and repoint others.
4. Update clients (Sentinel or DNS).

Redis Cluster's `CLUSTER FAILOVER` (without `FORCE`) does these steps for you: it waits for the replica to catch up before switching.

## 411: What does the FAILOVER command do?

`FAILOVER` (Redis 6.2+) runs a coordinated failover from a primary to one of its replicas in standalone setups without Sentinel. The primary pauses writes, waits for the replica to catch up, then makes it the primary and turns itself into a replica.

```bash
FAILOVER TO 10.0.0.2 6379 TIMEOUT 5000
```

## 412: How do you test that your app handles Redis failover?

- In staging, kill the primary process or the whole node and watch app errors and recovery time.
- Use `DEBUG SLEEP` or network tools (tc, toxiproxy) to simulate slow or broken connections.
- Trigger `SENTINEL FAILOVER` or `CLUSTER FAILOVER` during load tests.
- Check that clients reconnect, refresh topology, and that retries don't duplicate non-idempotent work.

Measure how many errors users would see and how long it takes to recover.

## 413: How should clients retry commands safely?

Retry on connection errors, `LOADING`, `TRYAGAIN`, `CLUSTERDOWN` and timeouts, with exponential backoff and jitter. Be careful with non-idempotent commands: an `INCR` that timed out may have run on the server, so retrying it can count twice. For those, use idempotency keys or a Lua script that checks before it writes. Don't retry `OOM` or `WRONGTYPE`; those are not temporary.

## 414: What happens if you run a blocking command on a shared connection?

`BLPOP`, `XREAD BLOCK` and similar commands hold the connection until they return. Every other command queued on that connection waits. In a Node.js app with one shared client, a `BLPOP 0` would freeze all Redis calls. Use a dedicated connection (`client.duplicate()` or a new ioredis instance) for blocking commands, pub/sub and `WATCH`.

## 415: How do keyspace notifications behave in Redis Cluster?

Each node only sends notifications for keys it owns, and only to clients connected to that node. To receive all events, a client must subscribe on every primary (and handle topology changes). This makes keyspace notifications harder to use in a cluster. For reliable change events, write to a stream from your app instead.

## 416: Why do expired events arrive late?

The `expired` event is sent when Redis actually deletes the key, either when someone accesses it or when the active expire cycle finds it. If no one touches the key and the cycle doesn't sample it right away, the event can come seconds or more after the TTL. On replicas, expire events are not generated at all. Use a sorted set of due times with a poller if you need timely triggers.

## 417: What is the difference between a primary's view and a replica's view of time-based data?

Replicas don't expire keys themselves, and they serve reads using their own clock to decide if a key is logically expired. If the clocks differ, a key can look expired on one node and alive on the other for a short time. TTL commands on a replica return values based on the primary's absolute expire time and the replica's clock. Keep clocks synced with NTP.

## 418: How do you avoid the thundering herd when a Redis node restarts?

When the node comes back, every client reconnects at the same time, and if the cache is empty, they all hit the database. Use reconnect backoff with jitter, persistence so the node restarts warm, replicas so traffic fails over instead of waiting for the restart, and stampede protection on cache loads. In a big fleet, also limit the number of connections each app instance opens.

## 419: How would you design a real-time "who is online" feature?

Each client sends a heartbeat every N seconds. Store presence in a sorted set with the last heartbeat time:

```bash
ZADD online 1767225600 user:42
ZRANGE online (1767225540 +inf BYSCORE    # seen in the last 60 s
ZREMRANGEBYSCORE online -inf 1767225540   # cleanup
```

For "friends online", intersect with the user's friend set using a Lua script or `ZINTER` with a friends sorted set. For huge counts, shard the set by user ID or use one key per user with a TTL.

## 420: How would you design a ride-sharing driver location service?

- Drivers send their location every few seconds: `GEOADD drivers:city:berlin <lon> <lat> driver:7`.
- Find nearby drivers: `GEOSEARCH drivers:city:berlin FROMLONLAT <lon> <lat> BYRADIUS 3 km ASC COUNT 20 WITHDIST`.
- Remove stale drivers: keep a second sorted set with last update time and remove drivers not seen for a while from both.
- Split by city or geohash region so no single key gets all updates.
- Driver status (free, busy) in a hash, or separate geo sets for free and busy drivers.

## 421: How would you count unique visitors per page per day for millions of pages?

One HyperLogLog per page per day: `PFADD uv:page:123:2026-11-05 <visitor>`. Each is at most 12 KB, and sparse ones are much smaller. Merge days with `PFCOUNT` over several keys, or `PFMERGE` into a weekly key. Set a TTL on daily keys. If memory is still too high, keep HLLs only for top pages and store the rest in your analytics database.

## 422: How would you implement a "trending" list of topics?

Use time-bucketed sorted sets, one per minute or hour:

```bash
ZINCRBY trending:2026-11-05T14 1 topic:redis
```

To get trending now, combine the last N buckets with weights that favor recent ones:

```bash
ZUNIONSTORE trending:now 3 trending:2026-11-05T14 trending:2026-11-05T13 trending:2026-11-05T12 WEIGHTS 3 2 1
ZRANGE trending:now 0 9 REV WITHSCORES
```

Expire old buckets. For very high volume, a Top-K sketch per bucket uses less memory.

## 423: How would you build a shopping cart in Redis?

A hash per cart, with product ID as field and quantity as value:

```bash
HINCRBY cart:user:42 product:9 1
HDEL cart:user:42 product:9
HGETALL cart:user:42
EXPIRE cart:user:42 2592000
```

For guests, use the session ID and merge into the user cart at login (`HGETALL` the guest cart, `HINCRBY` into the user cart in a Lua script, then delete the guest cart). Keep prices out of the cart; read them fresh at checkout.

## 424: How would you build a flash sale inventory counter that never oversells?

Keep the stock in Redis and decrement it atomically with a check:

```lua
-- KEYS[1] stock key, KEYS[2] buyers set, ARGV[1] user id
if redis.call('SISMEMBER', KEYS[2], ARGV[1]) == 1 then
  return -1 -- already bought
end
local stock = tonumber(redis.call('GET', KEYS[1]) or '0')
if stock <= 0 then
  return 0 -- sold out
end
redis.call('DECR', KEYS[1])
redis.call('SADD', KEYS[2], ARGV[1])
return 1
```

Use the same hash tag for both keys in a cluster. Then create the order in the database asynchronously (through a stream), and give stock back if payment fails. Persist with AOF so a restart doesn't reset the stock.

## 425: How would you implement a distributed counter that handles millions of increments per second?

A single key on a single node will become the bottleneck. Options:

- Shard the counter into N keys (`views:{1}` ... `views:{N}` with different hash tags) and increment a random shard. Read by summing all shards.
- Batch in the app: count locally and flush with `INCRBY` every second.
- If an approximate count is fine, combine local batching with a periodic flush.

Reads get a little more expensive, but writes scale with the number of shards.

## 426: How would you implement a job scheduler that runs cron-like tasks only once across many servers?

Each server computes the next run time. When it is due, all servers try to claim it:

```bash
SET cron:daily-report:2026-11-05 server-3 NX EX 86400
```

Only one gets `OK` and runs the job. The key includes the run time, so each run is claimed once, and the TTL cleans up. For long jobs, add a separate lock with a refresh loop. Libraries like BullMQ repeatable jobs handle this for you.

## 427: How do you handle the clock in distributed algorithms on Redis?

Prefer the Redis server's clock over each app server's clock, since app clocks can differ. In Lua scripts, `redis.call('TIME')` gives server time, and since effects replication is the default, using it is safe. Avoid comparing timestamps from different app servers when correctness depends on order. For leases and locks, use relative TTLs (`PX`) instead of absolute times.

## 428: What is the cost of a full sync on a big primary?

The primary forks and writes (or streams) the whole dataset, so it uses CPU, copy-on-write memory and network bandwidth. The replica flushes its data, receives the RDB and loads it, which can take minutes for tens of GB. While this happens, the primary buffers new writes for that replica. If several replicas resync at once, the load multiplies. Plan the backlog size and buffer limits to avoid full syncs, and add replicas at quiet times.

## 429: How do you back up a large Redis instance without affecting latency?

Run `BGSAVE` on a replica, not the primary, so the fork and disk writes happen there. Copy the RDB to object storage. Test restores regularly. For AOF, copy the AOF directory files listed in the manifest. Watch the replica's memory, since a fork on a nearly full machine can fail. Managed services usually offer automatic snapshots that run in a similar way.

## 430: How do you recover from a corrupted AOF or RDB file?

- `redis-check-aof --fix <file>` truncates the AOF at the first bad command, so you lose writes after that point. Check what will be removed first.
- `redis-check-rdb <file>` checks an RDB file.
- `aof-load-truncated yes` (the default) lets Redis start if the AOF was cut off at the end, for example after a crash during a write.

Always keep the original file before running a fix, and prefer restoring from a known good backup.

## 431: How do you replay or inspect the AOF to find out who changed a key?

The AOF incremental files are plain RESP text. You can grep for a key name to see which commands touched it and in what order. There are no timestamps by default, but `aof-timestamp-enabled yes` (Redis 7.0+) adds timestamp annotations, which also allows point-in-time recovery by truncating the AOF at a timestamp with `redis-check-aof --truncate-to-timestamp`.

## 432: Why can SORT be dangerous?

`SORT` can sort a list, set or sorted set and also look up other keys with `BY` and `GET` patterns. It is O(N + M log M) and runs on the main thread, so on big collections it blocks Redis. With `BY` and `GET` it touches keys not declared in the command, which doesn't work in a cluster. Use `SORT_RO` for read-only use, keep collections small, or do the sorting in the app or with a sorted set.

## 433: What are Redis modules?

Modules are shared libraries that add new commands and data types to Redis, written in C (or other languages through the module API). JSON, search, time series and Bloom were modules before Redis 8 bundled them. You load modules with `loadmodule` in redis.conf. Loading at runtime with `MODULE LOAD` is disabled by default since Redis 7.0. Modules run in the server process, so a bug in a module can crash Redis.

## 434: How does Redis handle very large numbers of databases or keys for expiration?

Expiration is handled per database. The active expire cycle visits each database in turn with a time budget. With many databases or hundreds of millions of keys with TTL, it may not keep up, so expired keys pile up in memory. You'll see it in `INFO` as a high `expired_stale_perc`. Raising `hz` or `active-expire-effort` helps at the cost of CPU. Redis 8 also improved how keys with TTL are tracked to make this cheaper.

## 435: How does the hz setting affect Redis?

`hz` sets how many times per second `serverCron` runs (default 10). Higher values make expiration, timeouts and other background tasks more responsive, but use more idle CPU. `dynamic-hz yes` (default) raises the frequency automatically when there are many clients. You rarely need to change it; values above 100 are not recommended.

## 436: What are the trade-offs of using Redis as the primary database?

Pros: very low latency, simple data structures that fit many problems, built-in TTLs, and in Redis 8, JSON and search. Cons: all data must fit in RAM, so it is expensive at scale; durability depends on fsync settings and you can still lose some writes on failover; no SQL joins or multi-key constraints; cluster limits on multi-key operations; backups and restores of large datasets are slow. It is a good primary store for data with simple access patterns and moderate size, and a poor one for complex relational data.

## 437: How would you migrate a large Redis setup from standalone to Cluster?

1. Audit the code for multi-key commands, transactions, scripts and `SELECT`, and add hash tags where keys must stay together.
2. Switch clients to cluster-aware libraries and test against a cluster in staging.
3. Create the cluster and copy data with a tool that reads from the old instance and writes to the cluster (for example RIOT or redis-shake), using replication-style sync to keep up with new writes.
4. Switch reads and writes to the cluster, keep the old instance read-only for a rollback window.
5. Remove the old instance after verifying key counts and samples.

## 438: How do you measure Redis performance correctly?

Use `redis-benchmark` or `memtier_benchmark` against a machine like production, with your real command mix, value sizes, pipelining and number of clients:

```bash
redis-benchmark -h host -c 50 -n 1000000 -P 16 -t set,get -d 256
memtier_benchmark -s host --ratio=1:4 --data-size=512 --pipeline=8 -c 50 -t 4
```

Run the client on a different machine, so it doesn't compete for CPU. Look at latency percentiles, not just ops per second. A benchmark with tiny values and huge pipelines tells you little about a real app.

## 439: How does pipelining interact with Redis Cluster?

A pipeline can only go to one node. Cluster clients split a pipeline by node: they group commands by slot owner, send each group, and put replies back in order. If a slot moves in the middle, some commands get `MOVED` and the client retries them. Transactions in a pipeline must still use keys from one slot. The bigger the cluster, the less a single pipeline helps, since the commands are spread over more nodes.

## 440: How do you choose the number of shards and replicas?

- Shards: enough so each primary stays well under its memory limit (leave room for growth and forks) and under the CPU limit of one main thread for your write rate. Many teams target under about 25 GB per shard to keep full syncs and restarts quick.
- Replicas: at least one per primary for failover; two if you need to survive losing a replica during maintenance, or for read scaling.
- Spread primaries and their replicas across availability zones.

Start with more, smaller shards than you need, since resharding later is slower than starting right.

## 441: How do you handle a cross-slot operation that you can't avoid?

- Split it into per-slot operations and combine results in the app.
- Store a copy of the needed data under the same hash tag (denormalize).
- Use the Query Engine, which can search across shards.
- Accept that the operation isn't atomic across slots and design for it, with idempotent steps and compensation if one part fails.

## 442: What are the differences between RESP2 and RESP3 that affect client code?

With RESP3, `HGETALL` returns a map instead of a flat array, scores can come back as doubles, and booleans and nulls have their own types. Pub/sub and tracking invalidations arrive as push messages on a normal connection, so one connection can both subscribe and run commands. Clients usually hide this, but when you switch protocols, check code that parses raw replies. Some features like client-side caching in default mode work best with RESP3.

## 443: How would you design caching for a GraphQL or REST API with many query variations?

Cache at the right level:

- Cache entities by ID (`product:42`) and build responses from them. Invalidation is simple: delete the entity key.
- Cache whole responses only for public, popular queries, with the key built from a hash of the normalized query and variables.
- Use short TTLs for query results and tag them with entity IDs (sets of response keys per entity) so you can invalidate them when an entity changes.
- Never cache user-specific responses under keys without the user or permission scope.

## 444: How do you prevent cache poisoning?

Cache poisoning means bad or attacker-controlled data ends up in the cache and is served to others. Avoid it by:

- Building cache keys only from validated inputs, and including everything that changes the response (user, locale, permissions).
- Not caching error responses or partial data, or caching them only briefly.
- Validating data before writing it to the cache.
- Restricting write access to Redis with ACLs so other services can't write your keys.

## 445: How do you do zero-downtime config changes in a large Redis deployment?

Most settings can be changed with `CONFIG SET` without a restart, then saved with `CONFIG REWRITE`. Apply changes to one replica first and watch it. For settings that need a restart (like some cluster or TLS settings), do a rolling restart: restart replicas one at a time, then fail over and restart the old primary. Keep the config in version control and apply it with automation so all nodes match.

## 446: What would you check before going to production with Redis?

- `maxmemory` and the right eviction policy for each instance's role.
- Persistence settings match the data's importance.
- High availability with automatic failover, tested.
- ACL users, no `default` user with full access, TLS where needed.
- Not reachable from the internet.
- THP off, `vm.overcommit_memory = 1`, enough file descriptors.
- Monitoring and alerts on memory, latency, replication and persistence.
- Backups that are copied off the machine and tested.
- Clients with timeouts, retries and reconnect logic.
- No `KEYS` or other O(N) calls on big data in the code.

## 447: How do you explain the CAP trade-off Redis makes?

During a network partition, Redis keeps accepting writes on the primary for a while (until it notices it lost its replicas or the cluster marks it failed), and a replica on the other side may get promoted. So it favors availability and low latency, and can lose writes and briefly have two primaries. It is not a CP system like etcd. With `min-replicas-to-write` you move a little toward consistency by refusing writes when isolated, at the cost of availability.

## 448: When would you not use Redis?

- Data much larger than the RAM you can afford.
- Complex queries, joins and transactions across many entities: use a relational database.
- Strong consistency or consensus (leader election, critical locks): use etcd, ZooKeeper or a database.
- Long-term event storage and replay at high volume: use Kafka or similar.
- Large files or blobs: use object storage.
- Analytics over billions of rows: use a columnar database.

Redis works best next to these systems, not instead of them.

## 449: What changed in Redis 8 that matters for an interview?

- JSON, the Query Engine, time series and probabilistic types are part of Redis Open Source, so no separate Redis Stack.
- New vector set data type for similarity search.
- AGPLv3 added as a license option, making Redis open source again.
- New hash commands: `HGETDEL`, `HGETEX`, `HSETEX`.
- Big performance improvements, especially with I/O threads, and lower memory per key.
- Later 8.x releases added compare-and-set for strings (`IFEQ`, `DELEX`), `MSETEX`, atomic slot migration, `HOTKEYS`, idempotent `XADD` and LRM eviction policies.

## 450: How would you explain Redis to a non-technical stakeholder in one minute?

Redis is a very fast, temporary memory for our application. Instead of asking the main database every time, which is slower and more expensive, we keep frequently used data in Redis, so pages load faster and the database is under less load. It also helps with things that need to happen quickly, like counting, rate limits, queues of background work and real-time updates. The main trade-off is that memory costs more than disk, so we keep in Redis only what needs to be fast, and keep the main copy of important data in the database.
