# Caching Strategies Interview Questions and Answers

_Last updated: November 19, 2026_

450 interview questions about caching with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers cover caching on the back end and on the web in general: in-process caches, Redis and Memcached, HTTP caching (RFC 9111), CDNs, and the patterns and problems that come with them. Code examples use Node.js with TypeScript and the ioredis client, plus a few Nginx and HTTP header examples.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a cache?](#1-what-is-a-cache)
- [2: Why do we use caching?](#2-why-do-we-use-caching)
- [3: What is a cache hit and a cache miss?](#3-what-is-a-cache-hit-and-a-cache-miss)
- [4: What is the cache hit ratio?](#4-what-is-the-cache-hit-ratio)
- [5: What is the source of truth, and why should the cache not be it?](#5-what-is-the-source-of-truth-and-why-should-the-cache-not-be-it)
- [6: What are the common places where data can be cached in a web application?](#6-what-are-the-common-places-where-data-can-be-cached-in-a-web-application)
- [7: What is an in-memory cache?](#7-what-is-an-in-memory-cache)
- [8: What is the difference between a local cache and a distributed cache?](#8-what-is-the-difference-between-a-local-cache-and-a-distributed-cache)
- [9: What is TTL in caching?](#9-what-is-ttl-in-caching)
- [10: How do you pick a TTL value?](#10-how-do-you-pick-a-ttl-value)
- [11: What is cache eviction?](#11-what-is-cache-eviction)
- [12: What is an eviction policy?](#12-what-is-an-eviction-policy)
- [13: What is LRU eviction?](#13-what-is-lru-eviction)
- [14: What is LFU eviction?](#14-what-is-lfu-eviction)
- [15: What is FIFO eviction?](#15-what-is-fifo-eviction)
- [16: What is the difference between eviction and invalidation?](#16-what-is-the-difference-between-eviction-and-invalidation)
- [17: What is cache invalidation?](#17-what-is-cache-invalidation)
- [18: What is stale data?](#18-what-is-stale-data)
- [19: What is the cache-aside pattern?](#19-what-is-the-cache-aside-pattern)
- [20: What are the pros and cons of cache-aside?](#20-what-are-the-pros-and-cons-of-cache-aside)
- [21: What is the read-through pattern?](#21-what-is-the-read-through-pattern)
- [22: What is the write-through pattern?](#22-what-is-the-write-through-pattern)
- [23: What is the write-back (write-behind) pattern?](#23-what-is-the-write-back-write-behind-pattern)
- [24: What is the write-around pattern?](#24-what-is-the-write-around-pattern)
- [25: What is refresh-ahead?](#25-what-is-refresh-ahead)
- [26: What is a cache key?](#26-what-is-a-cache-key)
- [27: What is a good naming convention for cache keys?](#27-what-is-a-good-naming-convention-for-cache-keys)
- [28: What is Redis?](#28-what-is-redis)
- [29: What is Memcached?](#29-what-is-memcached)
- [30: When would you pick Memcached over Redis?](#30-when-would-you-pick-memcached-over-redis)
- [31: What is Valkey?](#31-what-is-valkey)
- [32: What is memoization?](#32-what-is-memoization)
- [33: Can you build a simple in-memory cache with TTL in Node.js?](#33-can-you-build-a-simple-in-memory-cache-with-ttl-in-nodejs)
- [34: Why is an unbounded in-memory cache a problem?](#34-why-is-an-unbounded-in-memory-cache-a-problem)
- [35: What is the lru-cache package in Node.js?](#35-what-is-the-lru-cache-package-in-nodejs)
- [36: What is HTTP caching?](#36-what-is-http-caching)
- [37: What is the Cache-Control header?](#37-what-is-the-cache-control-header)
- [38: What does max-age mean?](#38-what-does-max-age-mean)
- [39: What does s-maxage mean?](#39-what-does-s-maxage-mean)
- [40: What is the difference between no-cache and no-store?](#40-what-is-the-difference-between-no-cache-and-no-store)
- [41: What is the difference between public and private in Cache-Control?](#41-what-is-the-difference-between-public-and-private-in-cache-control)
- [42: What does must-revalidate mean?](#42-what-does-must-revalidate-mean)
- [43: What is the Expires header?](#43-what-is-the-expires-header)
- [44: What is an ETag?](#44-what-is-an-etag)
- [45: What is the Last-Modified header?](#45-what-is-the-last-modified-header)
- [46: What is a 304 Not Modified response?](#46-what-is-a-304-not-modified-response)
- [47: What is a conditional request?](#47-what-is-a-conditional-request)
- [48: What is cache revalidation?](#48-what-is-cache-revalidation)
- [49: What is the Vary header?](#49-what-is-the-vary-header)
- [50: What is the Age header?](#50-what-is-the-age-header)
- [51: What is a CDN, and how does it help with caching?](#51-what-is-a-cdn-and-how-does-it-help-with-caching)
- [52: What is the origin server?](#52-what-is-the-origin-server)
- [53: What is an edge location?](#53-what-is-an-edge-location)
- [54: What is a cache purge?](#54-what-is-a-cache-purge)
- [55: What is cache busting?](#55-what-is-cache-busting)
- [56: Why can hashed static files be cached for a very long time?](#56-why-can-hashed-static-files-be-cached-for-a-very-long-time)
- [57: What does the immutable directive do?](#57-what-does-the-immutable-directive-do)
- [58: What should the Cache-Control header be for an HTML page in a single-page app?](#58-what-should-the-cache-control-header-be-for-an-html-page-in-a-single-page-app)
- [59: What should the Cache-Control header be for a response with personal data?](#59-what-should-the-cache-control-header-be-for-a-response-with-personal-data)
- [60: What is a reverse proxy cache?](#60-what-is-a-reverse-proxy-cache)
- [61: What is Varnish?](#61-what-is-varnish)
- [62: What is browser caching?](#62-what-is-browser-caching)
- [63: What is a service worker cache?](#63-what-is-a-service-worker-cache)
- [64: What is database query caching?](#64-what-is-database-query-caching)
- [65: What is the database buffer pool or page cache?](#65-what-is-the-database-buffer-pool-or-page-cache)
- [66: What is object caching?](#66-what-is-object-caching)
- [67: What is full page caching?](#67-what-is-full-page-caching)
- [68: What is fragment caching?](#68-what-is-fragment-caching)
- [69: What is session caching?](#69-what-is-session-caching)
- [70: What is negative caching?](#70-what-is-negative-caching)
- [71: What is a cold cache?](#71-what-is-a-cold-cache)
- [72: What is a warm cache?](#72-what-is-a-warm-cache)
- [73: What is cache warming?](#73-what-is-cache-warming)
- [74: What is a cache stampede?](#74-what-is-a-cache-stampede)
- [75: What is TTL jitter, and why is it useful?](#75-what-is-ttl-jitter-and-why-is-it-useful)
- [76: What kind of data is a good fit for caching?](#76-what-kind-of-data-is-a-good-fit-for-caching)
- [77: What kind of data should you not cache?](#77-what-kind-of-data-should-you-not-cache)
- [78: What is a cache layer?](#78-what-is-a-cache-layer)
- [79: What is serialization in caching?](#79-what-is-serialization-in-caching)
- [80: What problem can happen with Date objects when caching JSON?](#80-what-problem-can-happen-with-date-objects-when-caching-json)
- [81: What is a cache-control strategy for API responses?](#81-what-is-a-cache-control-strategy-for-api-responses)
- [82: Why are GET requests cached and POST requests usually not?](#82-why-are-get-requests-cached-and-post-requests-usually-not)
- [83: Which HTTP status codes can be cached?](#83-which-http-status-codes-can-be-cached)
- [84: What is heuristic caching?](#84-what-is-heuristic-caching)
- [85: What is the difference between fresh and stale in HTTP caching?](#85-what-is-the-difference-between-fresh-and-stale-in-http-caching)
- [86: What is the stale-while-revalidate directive?](#86-what-is-the-stale-while-revalidate-directive)
- [87: What is the stale-if-error directive?](#87-what-is-the-stale-if-error-directive)
- [88: What is a cache layer in front of a third-party API?](#88-what-is-a-cache-layer-in-front-of-a-third-party-api)
- [89: What is the difference between a cache and a buffer?](#89-what-is-the-difference-between-a-cache-and-a-buffer)
- [90: What is the difference between a cache and a database?](#90-what-is-the-difference-between-a-cache-and-a-database)
- [91: What is cache memory in a CPU, and how does it relate to software caching?](#91-what-is-cache-memory-in-a-cpu-and-how-does-it-relate-to-software-caching)
- [92: What are L1 and L2 caches in application caching?](#92-what-are-l1-and-l2-caches-in-application-caching)
- [93: What is locality of reference?](#93-what-is-locality-of-reference)
- [94: What is the working set?](#94-what-is-the-working-set)
- [95: What is the 80/20 rule in caching?](#95-what-is-the-8020-rule-in-caching)
- [96: What is a hot key?](#96-what-is-a-hot-key)
- [97: What does it mean that caching trades consistency for speed?](#97-what-does-it-mean-that-caching-trades-consistency-for-speed)
- [98: What is eventual consistency in caching?](#98-what-is-eventual-consistency-in-caching)
- [99: What are the basic Redis commands used for caching?](#99-what-are-the-basic-redis-commands-used-for-caching)
- [100: How do you set a key with a TTL in Redis from Node.js?](#100-how-do-you-set-a-key-with-a-ttl-in-redis-from-nodejs)
- [101: What happens in Redis when a key with a TTL expires?](#101-what-happens-in-redis-when-a-key-with-a-ttl-expires)
- [102: Does updating a key with SET keep its TTL?](#102-does-updating-a-key-with-set-keep-its-ttl)
- [103: What is the difference between EXPIRE and SETEX?](#103-what-is-the-difference-between-expire-and-setex)
- [104: What does SET with NX do?](#104-what-does-set-with-nx-do)
- [105: What is maxmemory in Redis?](#105-what-is-maxmemory-in-redis)
- [106: What is the noeviction policy in Redis?](#106-what-is-the-noeviction-policy-in-redis)
- [107: What is the difference between allkeys-lru and volatile-lru in Redis?](#107-what-is-the-difference-between-allkeys-lru-and-volatile-lru-in-redis)
- [108: What are the main Redis eviction policies?](#108-what-are-the-main-redis-eviction-policies)
- [109: How do you check if a cache is working well?](#109-how-do-you-check-if-a-cache-is-working-well)
- [110: What does a high number of evictions tell you?](#110-what-does-a-high-number-of-evictions-tell-you)
- [111: Should the app crash if the cache is down?](#111-should-the-app-crash-if-the-cache-is-down)
- [112: What is the latency difference between memory, Redis and a database?](#112-what-is-the-latency-difference-between-memory-redis-and-a-database)
- [113: Can caching make an application slower?](#113-can-caching-make-an-application-slower)
- [114: What is the cost of a cache miss?](#114-what-is-the-cost-of-a-cache-miss)
- [115: How do you delete a cached item when the data changes?](#115-how-do-you-delete-a-cached-item-when-the-data-changes)
- [116: What is a cache-control header for images that change rarely but have no hash in the name?](#116-what-is-a-cache-control-header-for-images-that-change-rarely-but-have-no-hash-in-the-name)
- [117: How do you see in the browser if a response came from cache?](#117-how-do-you-see-in-the-browser-if-a-response-came-from-cache)
- [118: How can you tell if a response came from a CDN cache?](#118-how-can-you-tell-if-a-response-came-from-a-cdn-cache)
- [119: What is the Cache-Status header?](#119-what-is-the-cache-status-header)
- [120: What does Ctrl+F5 or a hard reload do to caching?](#120-what-does-ctrlf5-or-a-hard-reload-do-to-caching)
- [121: What is the bfcache?](#121-what-is-the-bfcache)
- [122: What is a CDN cache key?](#122-what-is-a-cdn-cache-key)
- [123: Why do tracking query parameters hurt CDN hit ratio?](#123-why-do-tracking-query-parameters-hurt-cdn-hit-ratio)
- [124: What is a cache hit at the edge vs a cache hit at the origin?](#124-what-is-a-cache-hit-at-the-edge-vs-a-cache-hit-at-the-origin)
- [125: What is prefetching, and how is it related to caching?](#125-what-is-prefetching-and-how-is-it-related-to-caching)
- [126: What is client-side data caching in front-end apps?](#126-what-is-client-side-data-caching-in-front-end-apps)
- [127: What is a cache entry?](#127-what-is-a-cache-entry)
- [128: What is the difference between absolute and sliding expiration?](#128-what-is-the-difference-between-absolute-and-sliding-expiration)
- [129: How do you implement sliding expiration in Redis?](#129-how-do-you-implement-sliding-expiration-in-redis)
- [130: What is cache size, and how do you limit it?](#130-what-is-cache-size-and-how-do-you-limit-it)
- [131: What is a cache namespace?](#131-what-is-a-cache-namespace)
- [132: How do you clear the whole Redis cache?](#132-how-do-you-clear-the-whole-redis-cache)
- [133: Why should you avoid the KEYS command in production Redis?](#133-why-should-you-avoid-the-keys-command-in-production-redis)
- [134: What is the difference between DEL and UNLINK in Redis?](#134-what-is-the-difference-between-del-and-unlink-in-redis)
- [135: What is caching computed results?](#135-what-is-caching-computed-results)
- [136: What is a CDN cache hit ratio, and what is a good value?](#136-what-is-a-cdn-cache-hit-ratio-and-what-is-a-good-value)
- [137: Why does the first request after a deploy sometimes feel slow?](#137-why-does-the-first-request-after-a-deploy-sometimes-feel-slow)
- [138: What is a CDN in front of an API, and when is it useful?](#138-what-is-a-cdn-in-front-of-an-api-and-when-is-it-useful)
- [139: What is micro-caching?](#139-what-is-micro-caching)
- [140: How does Nginx cache responses?](#140-how-does-nginx-cache-responses)
- [141: What does it mean that a cache is transparent?](#141-what-does-it-mean-that-a-cache-is-transparent)
- [142: What is the difference between caching and replication?](#142-what-is-the-difference-between-caching-and-replication)
- [143: What is caching DNS?](#143-what-is-caching-dns)
- [144: What is connection caching or pooling, and is it caching?](#144-what-is-connection-caching-or-pooling-and-is-it-caching)
- [145: What is cache coherence?](#145-what-is-cache-coherence)
- [146: Why is the phrase "there are only two hard things in computer science: cache invalidation and naming things" popular?](#146-why-is-the-phrase-there-are-only-two-hard-things-in-computer-science-cache-invalidation-and-naming-things-popular)
- [147: What is a cache read timeout, and why set one?](#147-what-is-a-cache-read-timeout-and-why-set-one)
- [148: What is the difference between a cache and a CDN?](#148-what-is-the-difference-between-a-cache-and-a-cdn)
- [149: What is the risk of caching error responses?](#149-what-is-the-risk-of-caching-error-responses)
- [150: What are the most common caching mistakes?](#150-what-are-the-most-common-caching-mistakes)

### Moderate Questions (151-300)

- [151: How would you write a reusable cache-aside helper in TypeScript?](#151-how-would-you-write-a-reusable-cache-aside-helper-in-typescript)
- [152: Why is deleting the key usually better than updating it after a write?](#152-why-is-deleting-the-key-usually-better-than-updating-it-after-a-write)
- [153: Should you delete the cache before or after updating the database?](#153-should-you-delete-the-cache-before-or-after-updating-the-database)
- [154: What is delayed double delete?](#154-what-is-delayed-double-delete)
- [155: What happens if the database write succeeds but the cache delete fails?](#155-what-happens-if-the-database-write-succeeds-but-the-cache-delete-fails)
- [156: How do you invalidate a list that contains an item that changed?](#156-how-do-you-invalidate-a-list-that-contains-an-item-that-changed)
- [157: What is the "cache IDs, not objects" approach for lists?](#157-what-is-the-cache-ids-not-objects-approach-for-lists)
- [158: What is versioned key invalidation?](#158-what-is-versioned-key-invalidation)
- [159: What is tag-based invalidation?](#159-what-is-tag-based-invalidation)
- [160: What is event-based cache invalidation?](#160-what-is-event-based-cache-invalidation)
- [161: How do you invalidate local in-memory caches across many app servers?](#161-how-do-you-invalidate-local-in-memory-caches-across-many-app-servers)
- [162: What is the downside of Redis pub/sub for cache invalidation?](#162-what-is-the-downside-of-redis-pubsub-for-cache-invalidation)
- [163: How do you cache data that depends on the user's language?](#163-how-do-you-cache-data-that-depends-on-the-users-language)
- [164: How do you cache paginated results?](#164-how-do-you-cache-paginated-results)
- [165: How do you cache search results?](#165-how-do-you-cache-search-results)
- [166: Why normalize cache keys?](#166-why-normalize-cache-keys)
- [167: How do you choose between JSON, MessagePack and other formats for cached values?](#167-how-do-you-choose-between-json-messagepack-and-other-formats-for-cached-values)
- [168: When should you compress cached values?](#168-when-should-you-compress-cached-values)
- [169: How do you read many keys at once efficiently in Redis?](#169-how-do-you-read-many-keys-at-once-efficiently-in-redis)
- [170: What is a Redis pipeline?](#170-what-is-a-redis-pipeline)
- [171: When would you use a Redis hash instead of a JSON string for a cached object?](#171-when-would-you-use-a-redis-hash-instead-of-a-json-string-for-a-cached-object)
- [172: How do you cache a leaderboard?](#172-how-do-you-cache-a-leaderboard)
- [173: How do you cache counters like view counts?](#173-how-do-you-cache-counters-like-view-counts)
- [174: How do you protect against a cache stampede with a lock?](#174-how-do-you-protect-against-a-cache-stampede-with-a-lock)
- [175: What is request coalescing (single-flight)?](#175-what-is-request-coalescing-single-flight)
- [176: What is probabilistic early expiration?](#176-what-is-probabilistic-early-expiration)
- [177: How do you implement stale-while-revalidate in an application cache?](#177-how-do-you-implement-stale-while-revalidate-in-an-application-cache)
- [178: What is the difference between a soft TTL and a hard TTL?](#178-what-is-the-difference-between-a-soft-ttl-and-a-hard-ttl)
- [179: How do you serve stale data when the database is down?](#179-how-do-you-serve-stale-data-when-the-database-is-down)
- [180: What is a cache penetration problem?](#180-what-is-a-cache-penetration-problem)
- [181: What is cache avalanche?](#181-what-is-cache-avalanche)
- [182: What is cache breakdown?](#182-what-is-cache-breakdown)
- [183: How do you cache API responses in an Express app?](#183-how-do-you-cache-api-responses-in-an-express-app)
- [184: How does Express generate ETags?](#184-how-does-express-generate-etags)
- [185: What is the difference between a strong and a weak ETag?](#185-what-is-the-difference-between-a-strong-and-a-weak-etag)
- [186: How can you avoid building the response just to compare ETags?](#186-how-can-you-avoid-building-the-response-just-to-compare-etags)
- [187: How do ETags help with concurrent updates?](#187-how-do-etags-help-with-concurrent-updates)
- [188: What problems does Vary: Cookie cause?](#188-what-problems-does-vary-cookie-cause)
- [189: Why is Vary: User-Agent bad for caching?](#189-why-is-vary-user-agent-bad-for-caching)
- [190: How do you cache pages for logged-in and logged-out users?](#190-how-do-you-cache-pages-for-logged-in-and-logged-out-users)
- [191: How do CDNs treat responses with Set-Cookie?](#191-how-do-cdns-treat-responses-with-set-cookie)
- [192: How should you cache a response to a request with an Authorization header?](#192-how-should-you-cache-a-response-to-a-request-with-an-authorization-header)
- [193: How do you set up a CDN to bypass cache for certain requests?](#193-how-do-you-set-up-a-cdn-to-bypass-cache-for-certain-requests)
- [194: What is the difference between purging by URL, by prefix and by tag?](#194-what-is-the-difference-between-purging-by-url-by-prefix-and-by-tag)
- [195: What is a soft purge?](#195-what-is-a-soft-purge)
- [196: How do you send cache tags from your origin?](#196-how-do-you-send-cache-tags-from-your-origin)
- [197: What is Surrogate-Control?](#197-what-is-surrogate-control)
- [198: How do you cache a single-page app on a CDN?](#198-how-do-you-cache-a-single-page-app-on-a-cdn)
- [199: What happens to users who have the old HTML after a deploy?](#199-what-happens-to-users-who-have-the-old-html-after-a-deploy)
- [200: How do service worker caching strategies differ?](#200-how-do-service-worker-caching-strategies-differ)
- [201: How do you implement a cache-first strategy in a service worker?](#201-how-do-you-implement-a-cache-first-strategy-in-a-service-worker)
- [202: How do you clean up old service worker caches?](#202-how-do-you-clean-up-old-service-worker-caches)
- [203: What is the Clear-Site-Data header?](#203-what-is-the-clear-site-data-header)
- [204: How do you fix a page that browsers cached with a very long max-age by mistake?](#204-how-do-you-fix-a-page-that-browsers-cached-with-a-very-long-max-age-by-mistake)
- [205: How do you cache GraphQL responses?](#205-how-do-you-cache-graphql-responses)
- [206: What is DataLoader, and is it a cache?](#206-what-is-dataloader-and-is-it-a-cache)
- [207: What is a persisted query, and how does it help caching?](#207-what-is-a-persisted-query-and-how-does-it-help-caching)
- [208: What is an ORM second-level cache?](#208-what-is-an-orm-second-level-cache)
- [209: How do materialized views relate to caching?](#209-how-do-materialized-views-relate-to-caching)
- [210: How is a CQRS read model similar to a cache?](#210-how-is-a-cqrs-read-model-similar-to-a-cache)
- [211: How do you cache results from a slow external API that has rate limits?](#211-how-do-you-cache-results-from-a-slow-external-api-that-has-rate-limits)
- [212: How do you test code that uses a cache?](#212-how-do-you-test-code-that-uses-a-cache)
- [213: How do you debug a "users see old data" bug?](#213-how-do-you-debug-a-users-see-old-data-bug)
- [214: How do you turn off caching temporarily for debugging?](#214-how-do-you-turn-off-caching-temporarily-for-debugging)
- [215: How do you monitor Redis used as a cache?](#215-how-do-you-monitor-redis-used-as-a-cache)
- [216: Why should you measure hit ratio per key type instead of only globally?](#216-why-should-you-measure-hit-ratio-per-key-type-instead-of-only-globally)
- [217: How do you decide if a new cache is worth adding?](#217-how-do-you-decide-if-a-new-cache-is-worth-adding)
- [218: Why can a cache hide a slow query instead of fixing it?](#218-why-can-a-cache-hide-a-slow-query-instead-of-fixing-it)
- [219: How do you handle cached data after a schema change in your code?](#219-how-do-you-handle-cached-data-after-a-schema-change-in-your-code)
- [220: Why can rolling deploys cause cache bugs?](#220-why-can-rolling-deploys-cause-cache-bugs)
- [221: What is the difference between Redis and Memcached for caching?](#221-what-is-the-difference-between-redis-and-memcached-for-caching)
- [222: What is Memcached's slab allocator?](#222-what-is-memcacheds-slab-allocator)
- [223: How do you share a Redis instance between caching and other uses safely?](#223-how-do-you-share-a-redis-instance-between-caching-and-other-uses-safely)
- [224: Should Redis persistence be on when Redis is only a cache?](#224-should-redis-persistence-be-on-when-redis-is-only-a-cache)
- [225: What is Redis replication, and does it help a cache?](#225-what-is-redis-replication-and-does-it-help-a-cache)
- [226: What is Redis Sentinel?](#226-what-is-redis-sentinel)
- [227: What is Redis Cluster?](#227-what-is-redis-cluster)
- [228: What are hash tags in Redis Cluster keys?](#228-what-are-hash-tags-in-redis-cluster-keys)
- [229: How do you connect to Redis Cluster with ioredis?](#229-how-do-you-connect-to-redis-cluster-with-ioredis)
- [230: What is a cache aside with read replicas problem?](#230-what-is-a-cache-aside-with-read-replicas-problem)
- [231: How do you cache data in a serverless function?](#231-how-do-you-cache-data-in-a-serverless-function)
- [232: Why can connecting to Redis from serverless functions be a problem?](#232-why-can-connecting-to-redis-from-serverless-functions-be-a-problem)
- [233: How do you cache configuration and feature flags?](#233-how-do-you-cache-configuration-and-feature-flags)
- [234: How do you cache in a multi-tenant application?](#234-how-do-you-cache-in-a-multi-tenant-application)
- [235: How do you cache permissions or authorization data?](#235-how-do-you-cache-permissions-or-authorization-data)
- [236: How long should you cache JWT validation keys (JWKS)?](#236-how-long-should-you-cache-jwt-validation-keys-jwks)
- [237: How do you cache responses that are expensive to build and rarely change, like a sitemap?](#237-how-do-you-cache-responses-that-are-expensive-to-build-and-rarely-change-like-a-sitemap)
- [238: What is the difference between precomputing and caching?](#238-what-is-the-difference-between-precomputing-and-caching)
- [239: How do you avoid caching a partial or broken result?](#239-how-do-you-avoid-caching-a-partial-or-broken-result)
- [240: How do you cache null or empty results correctly?](#240-how-do-you-cache-null-or-empty-results-correctly)
- [241: What is a write-through cache implementation in code?](#241-what-is-a-write-through-cache-implementation-in-code)
- [242: When is write-through a good choice?](#242-when-is-write-through-a-good-choice)
- [243: When is write-back a good choice?](#243-when-is-write-back-a-good-choice)
- [244: How would you implement write-back with Redis?](#244-how-would-you-implement-write-back-with-redis)
- [245: What is cache warming after a deploy, and how do you do it?](#245-what-is-cache-warming-after-a-deploy-and-how-do-you-do-it)
- [246: How do you avoid cache warming overloading the database?](#246-how-do-you-avoid-cache-warming-overloading-the-database)
- [247: How does a CDN origin shield work?](#247-how-does-a-cdn-origin-shield-work)
- [248: What is tiered caching in CDNs?](#248-what-is-tiered-caching-in-cdns)
- [249: How do you cache responses that vary by device type?](#249-how-do-you-cache-responses-that-vary-by-device-type)
- [250: How do you cache content that varies by country?](#250-how-do-you-cache-content-that-varies-by-country)
- [251: How do you cache API responses in Nginx only for anonymous users?](#251-how-do-you-cache-api-responses-in-nginx-only-for-anonymous-users)
- [252: What does proxy_cache_lock do in Nginx?](#252-what-does-proxy_cache_lock-do-in-nginx)
- [253: What does proxy_cache_use_stale do in Nginx?](#253-what-does-proxy_cache_use_stale-do-in-nginx)
- [254: How do you build a two-level cache with local memory and Redis?](#254-how-do-you-build-a-two-level-cache-with-local-memory-and-redis)
- [255: What are the trade-offs of a two-level cache?](#255-what-are-the-trade-offs-of-a-two-level-cache)
- [256: What is the difference between caching at the controller level and at the data access level?](#256-what-is-the-difference-between-caching-at-the-controller-level-and-at-the-data-access-level)
- [257: How would you add caching to a NestJS app?](#257-how-would-you-add-caching-to-a-nestjs-app)
- [258: What is cache-manager in Node.js?](#258-what-is-cache-manager-in-nodejs)
- [259: How do you choose TTLs for different layers in a multi-layer cache?](#259-how-do-you-choose-ttls-for-different-layers-in-a-multi-layer-cache)
- [260: Why does staleness add up across cache layers?](#260-why-does-staleness-add-up-across-cache-layers)
- [261: How do you invalidate several cache layers in the right order?](#261-how-do-you-invalidate-several-cache-layers-in-the-right-order)
- [262: What is a cache-control strategy for a news site's article pages?](#262-what-is-a-cache-control-strategy-for-a-news-sites-article-pages)
- [263: How do you cache an expensive dashboard query?](#263-how-do-you-cache-an-expensive-dashboard-query)
- [264: How do you cache data that is updated every second, like stock prices?](#264-how-do-you-cache-data-that-is-updated-every-second-like-stock-prices)
- [265: How do you cache user sessions in Redis with Express?](#265-how-do-you-cache-user-sessions-in-redis-with-express)
- [266: How do you cache rate limit counters?](#266-how-do-you-cache-rate-limit-counters)
- [267: How do you make sure a cached value and its TTL are set atomically?](#267-how-do-you-make-sure-a-cached-value-and-its-ttl-are-set-atomically)
- [268: What is a Lua script in Redis, and when do you use it for caching?](#268-what-is-a-lua-script-in-redis-and-when-do-you-use-it-for-caching)
- [269: Why should a cache lock store a unique token?](#269-why-should-a-cache-lock-store-a-unique-token)
- [270: What is the risk of very long TTLs?](#270-what-is-the-risk-of-very-long-ttls)
- [271: What is the risk of very short TTLs?](#271-what-is-the-risk-of-very-short-ttls)
- [272: How do you cache data from a microservice you do not own?](#272-how-do-you-cache-data-from-a-microservice-you-do-not-own)
- [273: Why is it risky for many services to cache the same data independently?](#273-why-is-it-risky-for-many-services-to-cache-the-same-data-independently)
- [274: How do you handle cache key collisions between services?](#274-how-do-you-handle-cache-key-collisions-between-services)
- [275: How do you use Redis ACLs for a cache?](#275-how-do-you-use-redis-acls-for-a-cache)
- [276: How do you size a Redis cache?](#276-how-do-you-size-a-redis-cache)
- [277: How do you find large keys in Redis?](#277-how-do-you-find-large-keys-in-redis)
- [278: How do you find hot keys in Redis?](#278-how-do-you-find-hot-keys-in-redis)
- [279: What are the trade-offs of LRU vs LFU for a web cache?](#279-what-are-the-trade-offs-of-lru-vs-lfu-for-a-web-cache)
- [280: What are the lfu-log-factor and lfu-decay-time settings in Redis?](#280-what-are-the-lfu-log-factor-and-lfu-decay-time-settings-in-redis)
- [281: How does Redis approximate LRU?](#281-how-does-redis-approximate-lru)
- [282: What happens to a cache when Redis does a failover?](#282-what-happens-to-a-cache-when-redis-does-a-failover)
- [283: How do you handle cache errors in production without flooding logs?](#283-how-do-you-handle-cache-errors-in-production-without-flooding-logs)
- [284: How does a circuit breaker help with a cache outage?](#284-how-does-a-circuit-breaker-help-with-a-cache-outage)
- [285: How do you protect the database when the cache fails?](#285-how-do-you-protect-the-database-when-the-cache-fails)
- [286: How do you cache responses of a slow endpoint without changing the code much?](#286-how-do-you-cache-responses-of-a-slow-endpoint-without-changing-the-code-much)
- [287: How do you cache file downloads from object storage like S3?](#287-how-do-you-cache-file-downloads-from-object-storage-like-s3)
- [288: How do you cache image resizing results?](#288-how-do-you-cache-image-resizing-results)
- [289: How do you cache server-side rendered pages?](#289-how-do-you-cache-server-side-rendered-pages)
- [290: What is incremental static regeneration (ISR)?](#290-what-is-incremental-static-regeneration-isr)
- [291: How do you cache data per request in a Node.js server?](#291-how-do-you-cache-data-per-request-in-a-nodejs-server)
- [292: Why is a module-level cache dangerous for user data in Node.js?](#292-why-is-a-module-level-cache-dangerous-for-user-data-in-nodejs)
- [293: How do you cache the result of an async function and avoid duplicate calls?](#293-how-do-you-cache-the-result-of-an-async-function-and-avoid-duplicate-calls)
- [294: How do you cache HTTP responses on the client side in Node.js?](#294-how-do-you-cache-http-responses-on-the-client-side-in-nodejs)
- [295: What is No-Vary-Search?](#295-what-is-no-vary-search)
- [296: How do you choose what to include in a cache key for an HTTP response?](#296-how-do-you-choose-what-to-include-in-a-cache-key-for-an-http-response)
- [297: How do you cache data for a feed or timeline?](#297-how-do-you-cache-data-for-a-feed-or-timeline)
- [298: How do you cache data that is expensive to compute and different for each user, like recommendations?](#298-how-do-you-cache-data-that-is-expensive-to-compute-and-different-for-each-user-like-recommendations)
- [299: How do you document caching behavior in a codebase?](#299-how-do-you-document-caching-behavior-in-a-codebase)
- [300: What questions do you ask before adding a cache to a feature?](#300-what-questions-do-you-ask-before-adding-a-cache-to-a-feature)

### Advanced Questions (301-450)

- [301: Describe the classic race condition in cache-aside that leaves stale data in the cache.](#301-describe-the-classic-race-condition-in-cache-aside-that-leaves-stale-data-in-the-cache)
- [302: How can you prevent the stale-set race in cache-aside?](#302-how-can-you-prevent-the-stale-set-race-in-cache-aside)
- [303: What are leases in caching, as described in Facebook's memcache paper?](#303-what-are-leases-in-caching-as-described-in-facebooks-memcache-paper)
- [304: How would you implement version-checked cache writes in Redis?](#304-how-would-you-implement-version-checked-cache-writes-in-redis)
- [305: What is a tombstone in cache invalidation?](#305-what-is-a-tombstone-in-cache-invalidation)
- [306: What is change data capture (CDC), and how is it used for cache invalidation?](#306-what-is-change-data-capture-cdc-and-how-is-it-used-for-cache-invalidation)
- [307: What are the downsides of CDC-based invalidation?](#307-what-are-the-downsides-of-cdc-based-invalidation)
- [308: How does the transactional outbox pattern help with cache invalidation?](#308-how-does-the-transactional-outbox-pattern-help-with-cache-invalidation)
- [309: Why should you invalidate after commit and not inside the transaction?](#309-why-should-you-invalidate-after-commit-and-not-inside-the-transaction)
- [310: What consistency guarantees can a cache-aside system give?](#310-what-consistency-guarantees-can-a-cache-aside-system-give)
- [311: What is read-your-writes consistency, and how do you provide it with a cache?](#311-what-is-read-your-writes-consistency-and-how-do-you-provide-it-with-a-cache)
- [312: How do you handle cache consistency across multiple regions?](#312-how-do-you-handle-cache-consistency-across-multiple-regions)
- [313: What is the risk of invalidating before the cross-region database replication completes?](#313-what-is-the-risk-of-invalidating-before-the-cross-region-database-replication-completes)
- [314: What is a hot key problem in a distributed cache, and how do you solve it?](#314-what-is-a-hot-key-problem-in-a-distributed-cache-and-how-do-you-solve-it)
- [315: How does key replication for hot keys work, and what is the cost?](#315-how-does-key-replication-for-hot-keys-work-and-what-is-the-cost)
- [316: What is a big key problem in Redis?](#316-what-is-a-big-key-problem-in-redis)
- [317: How does consistent hashing help a distributed cache?](#317-how-does-consistent-hashing-help-a-distributed-cache)
- [318: How is Redis Cluster's hash slot model different from consistent hashing?](#318-how-is-redis-clusters-hash-slot-model-different-from-consistent-hashing)
- [319: What happens to clients during a Redis Cluster resharding?](#319-what-happens-to-clients-during-a-redis-cluster-resharding)
- [320: What is Redis client-side caching (tracking)?](#320-what-is-redis-client-side-caching-tracking)
- [321: What is broadcasting mode in Redis client tracking?](#321-what-is-broadcasting-mode-in-redis-client-tracking)
- [322: What is a near cache?](#322-what-is-a-near-cache)
- [323: How do you prevent cache penetration with a Bloom filter?](#323-how-do-you-prevent-cache-penetration-with-a-bloom-filter)
- [324: What are the limits of using a Bloom filter for penetration protection?](#324-what-are-the-limits-of-using-a-bloom-filter-for-penetration-protection)
- [325: How do you size a Bloom filter?](#325-how-do-you-size-a-bloom-filter)
- [326: What is cache pollution?](#326-what-is-cache-pollution)
- [327: What is an admission policy?](#327-what-is-an-admission-policy)
- [328: What is TinyLFU and W-TinyLFU?](#328-what-is-tinylfu-and-w-tinylfu)
- [329: What is a Count-Min Sketch?](#329-what-is-a-count-min-sketch)
- [330: What is the ARC eviction algorithm?](#330-what-is-the-arc-eviction-algorithm)
- [331: What is the CLOCK algorithm?](#331-what-is-the-clock-algorithm)
- [332: What is SLRU (segmented LRU)?](#332-what-is-slru-segmented-lru)
- [333: What is scan resistance?](#333-what-is-scan-resistance)
- [334: What is Belady's optimal algorithm, and why does it matter?](#334-what-is-beladys-optimal-algorithm-and-why-does-it-matter)
- [335: How do you evaluate eviction policies for your workload?](#335-how-do-you-evaluate-eviction-policies-for-your-workload)
- [336: What is a miss ratio curve?](#336-what-is-a-miss-ratio-curve)
- [337: How do you calculate the average latency with a cache?](#337-how-do-you-calculate-the-average-latency-with-a-cache)
- [338: Why can a cache make tail latency worse even when average latency improves?](#338-why-can-a-cache-make-tail-latency-worse-even-when-average-latency-improves)
- [339: How does caching affect database capacity planning?](#339-how-does-caching-affect-database-capacity-planning)
- [340: What is metastable failure, and how can caching cause it?](#340-what-is-metastable-failure-and-how-can-caching-cause-it)
- [341: How do you design a cache to recover safely from a full flush?](#341-how-do-you-design-a-cache-to-recover-safely-from-a-full-flush)
- [342: What is cache poisoning in HTTP caches?](#342-what-is-cache-poisoning-in-http-caches)
- [343: How do you prevent web cache poisoning?](#343-how-do-you-prevent-web-cache-poisoning)
- [344: What is web cache deception?](#344-what-is-web-cache-deception)
- [345: How do you prevent web cache deception?](#345-how-do-you-prevent-web-cache-deception)
- [346: How can a cache leak data between users?](#346-how-can-a-cache-leak-data-between-users)
- [347: How can attackers use caching for denial of service?](#347-how-can-attackers-use-caching-for-denial-of-service)
- [348: How can cache timing be a security issue?](#348-how-can-cache-timing-be-a-security-issue)
- [349: What is HTTP cache partitioning in browsers?](#349-what-is-http-cache-partitioning-in-browsers)
- [350: How should a cache handle secrets and sensitive data?](#350-how-should-a-cache-handle-secrets-and-sensitive-data)
- [351: Should Redis traffic be encrypted?](#351-should-redis-traffic-be-encrypted)
- [352: Design a caching strategy for a product catalog with 10 million products.](#352-design-a-caching-strategy-for-a-product-catalog-with-10-million-products)
- [353: Design caching for a checkout flow.](#353-design-caching-for-a-checkout-flow)
- [354: Design a cache for a social media profile page that some users view millions of times.](#354-design-a-cache-for-a-social-media-profile-page-that-some-users-view-millions-of-times)
- [355: Design caching for an API that returns exchange rates updated every minute.](#355-design-caching-for-an-api-that-returns-exchange-rates-updated-every-minute)
- [356: Design a caching layer for a multi-tenant SaaS with very different tenant sizes.](#356-design-a-caching-layer-for-a-multi-tenant-saas-with-very-different-tenant-sizes)
- [357: How would you cache results of a machine learning model or LLM call?](#357-how-would-you-cache-results-of-a-machine-learning-model-or-llm-call)
- [358: What is semantic caching, and what are its risks?](#358-what-is-semantic-caching-and-what-are-its-risks)
- [359: How do you cache in an event-sourced system?](#359-how-do-you-cache-in-an-event-sourced-system)
- [360: How does immutability make caching easier?](#360-how-does-immutability-make-caching-easier)
- [361: What is content-addressable storage, and how does it relate to caching?](#361-what-is-content-addressable-storage-and-how-does-it-relate-to-caching)
- [362: How do build caches like Turborepo or Bazel work?](#362-how-do-build-caches-like-turborepo-or-bazel-work)
- [363: How do you cache Docker image layers in CI?](#363-how-do-you-cache-docker-image-layers-in-ci)
- [364: How do you cache dependencies in CI pipelines?](#364-how-do-you-cache-dependencies-in-ci-pipelines)
- [365: What are the dangers of a CI cache?](#365-what-are-the-dangers-of-a-ci-cache)
- [366: How does Redis active expiration work, and can it cause latency?](#366-how-does-redis-active-expiration-work-and-can-it-cause-latency)
- [367: Can an expired key still use memory in Redis?](#367-can-an-expired-key-still-use-memory-in-redis)
- [368: How do Redis replicas handle expired keys?](#368-how-do-redis-replicas-handle-expired-keys)
- [369: What is Redis memory fragmentation, and how do you deal with it?](#369-what-is-redis-memory-fragmentation-and-how-do-you-deal-with-it)
- [370: Why does Redis need extra memory during a snapshot (fork)?](#370-why-does-redis-need-extra-memory-during-a-snapshot-fork)
- [371: How does Redis I/O threading affect cache performance?](#371-how-does-redis-io-threading-affect-cache-performance)
- [372: Why is a single slow Redis command dangerous for a cache?](#372-why-is-a-single-slow-redis-command-dangerous-for-a-cache)
- [373: How do you implement refresh-ahead safely for many keys?](#373-how-do-you-implement-refresh-ahead-safely-for-many-keys)
- [374: When would you never expire a cache entry and instead update it in place?](#374-when-would-you-never-expire-a-cache-entry-and-instead-update-it-in-place)
- [375: How do you handle a cache stampede across many servers?](#375-how-do-you-handle-a-cache-stampede-across-many-servers)
- [376: What are the problems with distributed locks for stampede protection?](#376-what-are-the-problems-with-distributed-locks-for-stampede-protection)
- [377: What is Redlock, and do you need it for caching?](#377-what-is-redlock-and-do-you-need-it-for-caching)
- [378: How do you cache aggregated data that depends on many rows?](#378-how-do-you-cache-aggregated-data-that-depends-on-many-rows)
- [379: How would you cache a "count of unread notifications" per user?](#379-how-would-you-cache-a-count-of-unread-notifications-per-user)
- [380: How do you keep a cached counter and the database in sync?](#380-how-do-you-keep-a-cached-counter-and-the-database-in-sync)
- [381: What problems can clock skew cause in caching?](#381-what-problems-can-clock-skew-cause-in-caching)
- [382: How does HTTP/2 or HTTP/3 change caching?](#382-how-does-http2-or-http3-change-caching)
- [383: How does a CDN handle a request for an object that is being fetched from the origin?](#383-how-does-a-cdn-handle-a-request-for-an-object-that-is-being-fetched-from-the-origin)
- [384: What is hit-for-pass in Varnish?](#384-what-is-hit-for-pass-in-varnish)
- [385: What is Edge Side Includes (ESI)?](#385-what-is-edge-side-includes-esi)
- [386: How do edge functions change caching strategies?](#386-how-do-edge-functions-change-caching-strategies)
- [387: What is the Cache API in Cloudflare Workers?](#387-what-is-the-cache-api-in-cloudflare-workers)
- [388: How do you measure the effect of a CDN on user latency?](#388-how-do-you-measure-the-effect-of-a-cdn-on-user-latency)
- [389: How do you handle cache invalidation for a CDN with hundreds of edge locations?](#389-how-do-you-handle-cache-invalidation-for-a-cdn-with-hundreds-of-edge-locations)
- [390: Why can purging everything at once on a CDN cause an outage?](#390-why-can-purging-everything-at-once-on-a-cdn-cause-an-outage)
- [391: How do you cache personalized API responses at the edge safely?](#391-how-do-you-cache-personalized-api-responses-at-the-edge-safely)
- [392: How do you handle cache invalidation in a system with many read models and caches?](#392-how-do-you-handle-cache-invalidation-in-a-system-with-many-read-models-and-caches)
- [393: How do you cache data that has dependencies, like a page built from many objects?](#393-how-do-you-cache-data-that-has-dependencies-like-a-page-built-from-many-objects)
- [394: What is the dependency explosion problem with tag invalidation?](#394-what-is-the-dependency-explosion-problem-with-tag-invalidation)
- [395: How do you make cache invalidation idempotent and retryable?](#395-how-do-you-make-cache-invalidation-idempotent-and-retryable)
- [396: How would you cache data in a GraphQL server with field-level TTLs?](#396-how-would-you-cache-data-in-a-graphql-server-with-field-level-ttls)
- [397: How do normalized client caches work, like Apollo Client's?](#397-how-do-normalized-client-caches-work-like-apollo-clients)
- [398: What is the hardest part of invalidation in client-side data caches?](#398-what-is-the-hardest-part-of-invalidation-in-client-side-data-caches)
- [399: How do you cache with optimistic updates on the client?](#399-how-do-you-cache-with-optimistic-updates-on-the-client)
- [400: How do you avoid thundering herds when clients refetch at the same time?](#400-how-do-you-avoid-thundering-herds-when-clients-refetch-at-the-same-time)
- [401: How would you debug a low cache hit ratio?](#401-how-would-you-debug-a-low-cache-hit-ratio)
- [402: What is cache key cardinality, and why does it matter?](#402-what-is-cache-key-cardinality-and-why-does-it-matter)
- [403: How do you cache time-based queries like "events in the last hour"?](#403-how-do-you-cache-time-based-queries-like-events-in-the-last-hour)
- [404: How does caching interact with database transactions isolation?](#404-how-does-caching-interact-with-database-transactions-isolation)
- [405: How would you cache a permission check that is called thousands of times per request?](#405-how-would-you-cache-a-permission-check-that-is-called-thousands-of-times-per-request)
- [406: What is a consistency token (zookie) in authorization caching?](#406-what-is-a-consistency-token-zookie-in-authorization-caching)
- [407: What is the "new enemy" problem?](#407-what-is-the-new-enemy-problem)
- [408: How do you decide where in the stack a cache belongs?](#408-how-do-you-decide-where-in-the-stack-a-cache-belongs)
- [409: What is the cost of a cache in terms of system complexity?](#409-what-is-the-cost-of-a-cache-in-terms-of-system-complexity)
- [410: How do you run load tests that include caching behavior?](#410-how-do-you-run-load-tests-that-include-caching-behavior)
- [411: How do you model a realistic key distribution in a load test?](#411-how-do-you-model-a-realistic-key-distribution-in-a-load-test)
- [412: What is a cache-aside implementation that supports batch loading?](#412-what-is-a-cache-aside-implementation-that-supports-batch-loading)
- [413: How do you handle MGET across Redis Cluster slots?](#413-how-do-you-handle-mget-across-redis-cluster-slots)
- [414: How would you migrate from one cache cluster to another without downtime?](#414-how-would-you-migrate-from-one-cache-cluster-to-another-without-downtime)
- [415: How do you change the TTL or format of many existing cache keys safely?](#415-how-do-you-change-the-ttl-or-format-of-many-existing-cache-keys-safely)
- [416: How do you cache in a system where the source data is in several databases?](#416-how-do-you-cache-in-a-system-where-the-source-data-is-in-several-databases)
- [417: How does a CDN decide what to evict when its cache is full?](#417-how-does-a-cdn-decide-what-to-evict-when-its-cache-is-full)
- [418: What is the difference between max-age and how long an object actually stays in a cache?](#418-what-is-the-difference-between-max-age-and-how-long-an-object-actually-stays-in-a-cache)
- [419: How do you handle conditional requests at the CDN to reduce origin load?](#419-how-do-you-handle-conditional-requests-at-the-cdn-to-reduce-origin-load)
- [420: How do Range requests interact with caching?](#420-how-do-range-requests-interact-with-caching)
- [421: What is the risk of caching redirects?](#421-what-is-the-risk-of-caching-redirects)
- [422: How do you cache CORS preflight responses?](#422-how-do-you-cache-cors-preflight-responses)
- [423: Why is Vary: Origin important for CORS responses?](#423-why-is-vary-origin-important-for-cors-responses)
- [424: How do you cache HTML in a way that supports instant rollback of a bad deploy?](#424-how-do-you-cache-html-in-a-way-that-supports-instant-rollback-of-a-bad-deploy)
- [425: How does caching interact with A/B testing?](#425-how-does-caching-interact-with-ab-testing)
- [426: How do you cache in a mobile app talking to your API?](#426-how-do-you-cache-in-a-mobile-app-talking-to-your-api)
- [427: What is the problem with caching in long-lived clients such as mobile apps?](#427-what-is-the-problem-with-caching-in-long-lived-clients-such-as-mobile-apps)
- [428: How do you prevent a cache from returning data after a user's account is deleted?](#428-how-do-you-prevent-a-cache-from-returning-data-after-a-users-account-is-deleted)
- [429: How does a write-back cache handle crash recovery?](#429-how-does-a-write-back-cache-handle-crash-recovery)
- [430: How do you order writes in a write-back cache?](#430-how-do-you-order-writes-in-a-write-back-cache)
- [431: How do you cache results of permission-filtered queries, like search results that depend on what the user can see?](#431-how-do-you-cache-results-of-permission-filtered-queries-like-search-results-that-depend-on-what-the-user-can-see)
- [432: How do caches behave in a split-brain or network partition?](#432-how-do-caches-behave-in-a-split-brain-or-network-partition)
- [433: How would you make a local cache safe with many worker threads or processes?](#433-how-would-you-make-a-local-cache-safe-with-many-worker-threads-or-processes)
- [434: How do you avoid the "everything expires at midnight" problem?](#434-how-do-you-avoid-the-everything-expires-at-midnight-problem)
- [435: How do you atomically switch to a new set of cached data?](#435-how-do-you-atomically-switch-to-a-new-set-of-cached-data)
- [436: What is the "cache as a crutch" anti-pattern?](#436-what-is-the-cache-as-a-crutch-anti-pattern)
- [437: How do you explain to a product manager the trade-offs of caching?](#437-how-do-you-explain-to-a-product-manager-the-trade-offs-of-caching)
- [438: How do you set a caching SLO?](#438-how-do-you-set-a-caching-slo)
- [439: How do you measure cache freshness in production?](#439-how-do-you-measure-cache-freshness-in-production)
- [440: How do you design cache keys that are safe from injection?](#440-how-do-you-design-cache-keys-that-are-safe-from-injection)
- [441: What happens if two different inputs hash to the same cache key?](#441-what-happens-if-two-different-inputs-hash-to-the-same-cache-key)
- [442: How do you cache responses from POST endpoints that are really reads, like search?](#442-how-do-you-cache-responses-from-post-endpoints-that-are-really-reads-like-search)
- [443: What is the QUERY HTTP method, and how does it relate to caching?](#443-what-is-the-query-http-method-and-how-does-it-relate-to-caching)
- [444: How do you cache with Redis in an environment with very strict latency budgets, like ad serving?](#444-how-do-you-cache-with-redis-in-an-environment-with-very-strict-latency-budgets-like-ad-serving)
- [445: How would you cache data in a system that must work offline for hours?](#445-how-would-you-cache-data-in-a-system-that-must-work-offline-for-hours)
- [446: How do you decide between Redis, an in-process cache, and a CDN for a new feature?](#446-how-do-you-decide-between-redis-an-in-process-cache-and-a-cdn-for-a-new-feature)
- [447: What would you check in a code review of a new cache?](#447-what-would-you-check-in-a-code-review-of-a-new-cache)
- [448: Describe a production caching incident and how you would investigate it.](#448-describe-a-production-caching-incident-and-how-you-would-investigate-it)
- [449: What are the most important ideas to remember about caching?](#449-what-are-the-most-important-ideas-to-remember-about-caching)
- [450: If you could only use one caching technique for a new web app, which would you choose and why?](#450-if-you-could-only-use-one-caching-technique-for-a-new-web-app-which-would-you-choose-and-why)

---

# Easy Questions (1-150)

## 1: What is a cache?

A cache is a place where you keep a copy of data so you can get it faster next time. Instead of going to the slow source again (a database, another service, a disk, the network), you read the copy from somewhere quicker, usually memory.

The cache is not the source of truth. If the cache is lost, the data can be loaded again from the original source.

## 2: Why do we use caching?

The main reasons:

- Faster responses, because reading from memory is much quicker than a database query or an HTTP call.
- Less load on the database and other services, so they can handle more users.
- Lower costs, since you pay for fewer queries, less compute and less bandwidth.
- Sometimes better availability, because you can serve cached data when the source is down for a short time.

## 3: What is a cache hit and a cache miss?

A cache hit is when the data you ask for is already in the cache, so you get it straight from there. A cache miss is when it is not there, so you have to load it from the original source, and usually put it in the cache for next time.

## 4: What is the cache hit ratio?

It is the share of requests that were served from the cache:

```text
hit ratio = hits / (hits + misses)
```

If 900 out of 1,000 requests are hits, the hit ratio is 90%. A higher ratio means the cache is doing more useful work. It is one of the first numbers to check when you look at how well a cache works.

## 5: What is the source of truth, and why should the cache not be it?

The source of truth is the system that holds the real, correct data, usually a database. A cache only holds copies. Caches can lose data at any time (restarts, eviction, memory limits), so if the cache were the only place a piece of data lived, you could lose it. Always make sure the data can be rebuilt from the source.

## 6: What are the common places where data can be cached in a web application?

From closest to the user to furthest:

- The browser (HTTP cache, service worker cache, memory in the app).
- A CDN at the edge, close to the user.
- A reverse proxy in front of your servers, like Nginx or Varnish.
- The application itself, in process memory.
- A shared cache server like Redis or Memcached.
- The database, which has its own internal caches (buffer pool, page cache).

Each layer can save work for the layers behind it.

## 7: What is an in-memory cache?

An in-memory cache keeps data in RAM instead of on disk. RAM is much faster to read, so lookups take microseconds instead of milliseconds. The cost is that RAM is limited and more expensive than disk, and data in RAM is usually lost on restart unless the cache also saves it somewhere.

## 8: What is the difference between a local cache and a distributed cache?

A local cache lives inside one application process, for example a `Map` in a Node.js app. It is the fastest option, but each server has its own copy, and the data is lost when the process restarts.

A distributed (or shared) cache runs as a separate service, like Redis or Memcached, and all app servers talk to it over the network. It is a bit slower because of the network hop, but all servers see the same data and it survives app restarts.

## 9: What is TTL in caching?

TTL means time to live. It is how long a cached item stays valid before it expires. After the TTL passes, the item is treated as missing and has to be loaded again from the source.

```ts
// keep this value for 60 seconds
await redis.set("user:42", JSON.stringify(user), "EX", 60);
```

## 10: How do you pick a TTL value?

Think about how often the data changes and how bad it is to show old data. Data that changes rarely and is fine to be a bit old (a list of countries, product categories) can have a long TTL, like hours or days. Data that changes often or must be fresh (stock levels, prices during a sale) needs a short TTL or a different way to keep it fresh, like deleting the key when the data changes.

A good starting point is to ask the product owner "how old can this data be before someone notices or it causes a problem?"

## 11: What is cache eviction?

Eviction is when the cache removes items to make room for new ones because it is full. It is different from expiration: expiration removes items because their TTL ran out, eviction removes items because of memory limits, even if they have not expired yet.

## 12: What is an eviction policy?

An eviction policy is the rule the cache uses to decide which item to remove when it is full. Common ones are LRU (least recently used), LFU (least frequently used), FIFO (first in, first out), random, and removing the items closest to expiry.

## 13: What is LRU eviction?

LRU means least recently used. When the cache is full, it removes the item that nobody has read for the longest time. The idea is that if something was not used recently, it probably will not be needed soon. LRU is the most common default because it is simple and works well for most workloads.

## 14: What is LFU eviction?

LFU means least frequently used. When the cache is full, it removes the item that was read the fewest times. It keeps popular items even if they were not read in the last few seconds. It works well when some keys are always popular, but a plain LFU can keep old items that were popular a long time ago, so real implementations slowly decay the counters.

## 15: What is FIFO eviction?

FIFO means first in, first out. The cache removes the oldest added item first, no matter how often it is used. It is simple to build, but it can throw away a very popular item just because it was added early, so it usually gives a lower hit ratio than LRU or LFU.

## 16: What is the difference between eviction and invalidation?

Eviction is done by the cache itself to free memory. Invalidation is done by your code on purpose because the data is no longer correct, for example when a user updates their profile and you delete the cached profile. Eviction is about space, invalidation is about correctness.

## 17: What is cache invalidation?

Cache invalidation is removing or updating cached data when the original data changes, so users do not see old values. It can be done by deleting the key, overwriting it with the new value, or letting it expire with a TTL. It is known as one of the hard parts of caching because you have to know every place where a change can make a cached value wrong.

## 18: What is stale data?

Stale data is a cached value that is older than the current value in the source. For example, the user changed their name, but the cache still returns the old name. Some staleness is often fine and is the price you pay for speed. The question is always how stale is acceptable for this specific data.

## 19: What is the cache-aside pattern?

Cache-aside (also called lazy loading) is the most common pattern. The application checks the cache first. On a hit, it returns the cached value. On a miss, it loads from the database, saves the value in the cache, and returns it. The cache does not know about the database; the app does all the work.

```ts
async function getUser(id: string) {
  const key = `user:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const user = await db.users.findById(id);
  if (user) await redis.set(key, JSON.stringify(user), "EX", 300);
  return user;
}
```

## 20: What are the pros and cons of cache-aside?

Pros: it is simple, only data that is actually requested ends up in the cache, and if the cache goes down the app can still read from the database.

Cons: the first request for each key is slow (a miss), the data can become stale if you forget to invalidate it, and the caching code is spread around the app instead of being in one place.

## 21: What is the read-through pattern?

In read-through, the app only talks to the cache. On a miss, the cache itself loads the data from the database (through a loader function you give it), stores it and returns it. It looks like cache-aside from the outside, but the loading logic lives in the cache layer or library, not in every caller.

```ts
const cache = new ReadThroughCache(async (id) => db.users.findById(id));
const user = await cache.get("42"); // loads from DB on a miss
```

## 22: What is the write-through pattern?

In write-through, every write goes to the cache and to the database at the same time, as part of the same operation. The write is done only when both are updated. The cache always has fresh data for the keys that were written, but each write is a bit slower because it touches two systems.

## 23: What is the write-back (write-behind) pattern?

In write-back, the app writes only to the cache, and the cache saves the changes to the database later, often in batches. Writes are very fast, and many writes to the same key can be merged into one database write. The risk is data loss: if the cache crashes before it flushes, the changes that were not saved yet are gone.

## 24: What is the write-around pattern?

In write-around, writes go straight to the database and skip the cache. The cache is filled only when the data is read (usually with cache-aside). It avoids filling the cache with data that is written but rarely read, like logs. The downside is that a read right after a write is a miss.

## 25: What is refresh-ahead?

Refresh-ahead means the cache reloads a popular item before it expires, so users rarely hit a miss. For example, if an item has a 60 second TTL and someone reads it after 50 seconds, the cache returns the current value and starts a background reload. It keeps hot keys always warm, but it can waste work refreshing items that will not be read again.

## 26: What is a cache key?

A cache key is the unique name used to store and find a value in the cache, like `user:42` or `product:123:en`. A good key includes everything that makes the value different, for example the ID, the language, and the version of the data format. If two different values share the same key, users get wrong data.

## 27: What is a good naming convention for cache keys?

Use short, readable parts joined with a colon, from general to specific:

```text
<app>:<entity>:<id>[:<variant>]
shop:product:123
shop:product:123:lang=de
shop:user:42:cart
```

This makes keys easy to read in tools, easy to delete by prefix during debugging, and avoids clashes between teams or services that share the same Redis.

## 28: What is Redis?

Redis is an open source, in-memory data store. It is often used as a cache, but also for sessions, queues, rate limits, leaderboards and pub/sub. It supports many data types (strings, hashes, lists, sets, sorted sets, streams and more), has TTL on keys, and can optionally save data to disk. Most commands take well under a millisecond.

## 29: What is Memcached?

Memcached is an open source, in-memory key-value cache. It is simple: it stores strings or bytes under a key, with a TTL, and evicts old items with LRU when memory is full. It is multi-threaded and very fast, but it has no persistence, no replication and no rich data types like Redis.

## 30: When would you pick Memcached over Redis?

When you only need a plain key-value cache for strings or blobs and want something very simple that uses many CPU cores out of the box. For most new projects people pick Redis (or a Redis-compatible store like Valkey) because it also covers sessions, counters, locks and other needs, so you run one tool instead of two.

## 31: What is Valkey?

Valkey is an open source fork of Redis, created in 2024 after Redis changed its license. It is run under the Linux Foundation and is compatible with Redis commands and clients, so for caching you can usually swap one for the other. Several cloud providers offer managed Valkey.

## 32: What is memoization?

Memoization is caching the result of a function call based on its arguments, so calling the function again with the same arguments returns the saved result instead of computing it again. It is caching at the function level, usually in local memory.

```ts
const memo = new Map<number, number>();
function slowSquare(n: number) {
  if (memo.has(n)) return memo.get(n)!;
  const result = n * n; // pretend this is expensive
  memo.set(n, result);
  return result;
}
```

## 33: Can you build a simple in-memory cache with TTL in Node.js?

Yes, a `Map` with an expiry time per entry is enough for small cases:

```ts
type Entry<T> = { value: T; expiresAt: number };

class TtlCache<T> {
  private store = new Map<string, Entry<T>>();

  get(key: string): T | undefined {
    const entry = this.store.get(key);
    if (!entry) return undefined;
    if (Date.now() > entry.expiresAt) {
      this.store.delete(key);
      return undefined;
    }
    return entry.value;
  }

  set(key: string, value: T, ttlMs: number) {
    this.store.set(key, { value, expiresAt: Date.now() + ttlMs });
  }
}
```

It has no size limit, so in real apps use a library like `lru-cache` that also caps the number of items.

## 34: Why is an unbounded in-memory cache a problem?

If the cache has no size limit and keeps adding new keys, it grows until the process runs out of memory and crashes. This is a very common memory leak in Node.js apps, for example caching by user ID or URL forever. Always set a maximum size or memory limit and an eviction policy.

## 35: What is the lru-cache package in Node.js?

`lru-cache` is a popular npm package for local in-process caching. You set a maximum number of items (or total size) and an optional TTL, and it evicts the least recently used items when full.

```ts
import { LRUCache } from "lru-cache";

const cache = new LRUCache<string, object>({ max: 1000, ttl: 60_000 });
cache.set("config", { theme: "dark" });
const config = cache.get("config");
```

## 36: What is HTTP caching?

HTTP caching is when browsers, CDNs and proxies store HTTP responses and reuse them for later requests. The server controls this with response headers like `Cache-Control`, `ETag` and `Last-Modified`. The rules are defined in RFC 9111. Done right, many requests never reach your server at all.

## 37: What is the Cache-Control header?

`Cache-Control` is the main HTTP header for caching. The server uses it to say who can cache a response and for how long. For example:

```http
Cache-Control: public, max-age=3600
```

This says any cache (browser or CDN) can store the response and reuse it for one hour without asking the server again.

## 38: What does max-age mean?

`max-age=N` tells caches that the response is fresh for N seconds after it was created. While it is fresh, a cache can serve it without contacting the server. After that, it becomes stale and the cache has to check with the server (revalidate) or fetch it again.

## 39: What does s-maxage mean?

`s-maxage=N` is like `max-age`, but only for shared caches such as CDNs and proxies. Browsers ignore it. It lets you cache something for a long time at the CDN but a short time in the browser:

```http
Cache-Control: public, max-age=60, s-maxage=3600
```

## 40: What is the difference between no-cache and no-store?

`no-store` means do not save this response anywhere, ever. Use it for sensitive data.

`no-cache` is confusing by name: it means you may store the response, but you must check with the server before every reuse. If the server says it did not change (a `304 Not Modified`), the cache uses its copy. So `no-cache` still saves bandwidth, `no-store` does not.

## 41: What is the difference between public and private in Cache-Control?

`private` means only the user's own browser may cache the response. CDNs and shared proxies must not store it. Use it for responses with user-specific data.

`public` means any cache, including shared ones, may store it. It also allows caching responses that normally would not be cached, like ones to requests with an `Authorization` header.

## 42: What does must-revalidate mean?

`must-revalidate` means that once the response becomes stale, the cache must not use it without checking with the server first. Without it, some caches are allowed to serve stale responses in certain cases, like when they cannot reach the server. With it, if the server cannot be reached, the cache must return an error (usually 504) instead of the stale copy.

## 43: What is the Expires header?

`Expires` is an older header that gives an exact date and time when the response becomes stale:

```http
Expires: Wed, 19 Nov 2026 12:00:00 GMT
```

It depends on the clocks of the server and the client being in sync. If `Cache-Control: max-age` is also present, `max-age` wins. New code should use `Cache-Control`; `Expires` is mostly legacy.

## 44: What is an ETag?

An ETag (entity tag) is an identifier for a specific version of a resource, usually a hash of its content. The server sends it in the response:

```http
ETag: "a1b2c3"
```

Later the client can send it back in `If-None-Match` to ask "has this changed?". If not, the server replies `304 Not Modified` with no body, and the client uses its cached copy.

## 45: What is the Last-Modified header?

`Last-Modified` tells when the resource was last changed. The client can send it back in `If-Modified-Since` on the next request. If the resource has not changed since that time, the server replies `304 Not Modified`. It is simpler than ETags but only has one-second precision, and it is less accurate when the content can change without the date changing.

## 46: What is a 304 Not Modified response?

It is the server's answer to a conditional request (one with `If-None-Match` or `If-Modified-Since`) when the resource has not changed. It has no body, so it is small and fast. The client keeps using its cached copy and treats it as fresh again for another `max-age` period.

## 47: What is a conditional request?

A conditional request is a request that includes a condition about the version the client already has, using headers like `If-None-Match` (with an ETag) or `If-Modified-Since` (with a date). The server only sends the full body if the condition says the client's copy is outdated. This is how caches revalidate stale responses.

## 48: What is cache revalidation?

Revalidation is when a cache that holds a stale response asks the origin server whether that response is still good, instead of downloading it again. It sends a conditional request. If the server answers `304`, the cache keeps using its copy. If it answers `200` with a new body, the cache replaces its copy.

## 49: What is the Vary header?

`Vary` tells caches which request headers change the response. For example:

```http
Vary: Accept-Encoding
```

means the cache must store separate copies for different `Accept-Encoding` values (gzip, br, none), and only serve a copy to requests with a matching value. Without it, a cache could send a Brotli-compressed response to a client that does not support Brotli.

## 50: What is the Age header?

`Age` is added by shared caches like CDNs. It tells how many seconds ago the response was fetched from or validated with the origin. If you see `Age: 120` with `max-age=300`, the response has 180 seconds of freshness left. It is useful when debugging whether a response came from a cache.

## 51: What is a CDN, and how does it help with caching?

A CDN (content delivery network) is a large set of servers spread around the world. It caches your responses at locations close to users (edge locations or points of presence). A user in Tokyo gets files from a Tokyo server instead of your origin in Frankfurt, so the response is faster and your origin gets far fewer requests. Examples are Cloudflare, Amazon CloudFront, Fastly and Akamai.

## 52: What is the origin server?

The origin is your own server (or storage like S3) that holds the real content. A CDN or proxy sits in front of it. On a cache miss, the CDN fetches the content from the origin, stores it, and serves it to the user.

## 53: What is an edge location?

An edge location (or PoP, point of presence) is a CDN data center close to users. It holds cached copies of content. Big CDNs have hundreds of them in different cities, and each one has its own cache, so a file cached in London is not automatically cached in Sydney.

## 54: What is a cache purge?

A purge is telling a CDN or proxy to remove cached content before it expires, so the next request goes to the origin and gets the new version. CDNs let you purge by URL, by prefix, by tag, or purge everything. It is how you fix a cached page that shows wrong or old content.

## 55: What is cache busting?

Cache busting is changing the URL of a file when its content changes, so browsers and CDNs see it as a new file and do not use the old cached copy. The usual way is to put a content hash in the file name:

```html
<script src="/assets/app.3f9a1c.js"></script>
```

When the code changes, the build creates `app.7b2e44.js`, and the HTML points to the new name.

## 56: Why can hashed static files be cached for a very long time?

Because a file named `app.3f9a1c.js` will never have different content. If the content changes, its name changes too. So you can safely tell everyone to cache it for a year:

```http
Cache-Control: public, max-age=31536000, immutable
```

Only the HTML that references these files needs a short cache time, so users pick up new file names after a deploy.

## 57: What does the immutable directive do?

`immutable` tells the browser that the response will never change while it is fresh, so it should not revalidate it even when the user reloads the page. Without it, some browsers send conditional requests on reload, which are wasted for files with hashed names. Use it only on versioned URLs.

## 58: What should the Cache-Control header be for an HTML page in a single-page app?

The `index.html` of a SPA should not be cached for long, because it points to the current hashed JS and CSS files. A common setting is:

```http
Cache-Control: no-cache
```

The browser keeps a copy but checks with the server every time, getting a cheap `304` if nothing changed. After a deploy, users get the new HTML right away.

## 59: What should the Cache-Control header be for a response with personal data?

If the response contains data for one user, like their account page or their orders, at minimum use `private` so CDNs do not store it. If the data is sensitive (bank details, health data), use `no-store` so it is not saved anywhere, not even in the browser cache.

```http
Cache-Control: private, no-store
```

## 60: What is a reverse proxy cache?

A reverse proxy sits in front of your app servers and receives all requests first. A reverse proxy cache stores responses from the app and serves them directly for later requests. Nginx and Varnish are common examples. It works like a CDN but lives in your own infrastructure, usually in the same data center as your app.

## 61: What is Varnish?

Varnish Cache is an open source HTTP reverse proxy built for caching. You put it in front of your web servers, and it caches responses in memory. It has its own configuration language (VCL) that lets you control what to cache, for how long, and how to build cache keys. Fastly's CDN started as a Varnish-based service.

## 62: What is browser caching?

Browser caching is when the browser keeps copies of files and responses it downloaded (HTML, JS, CSS, images, API responses) and reuses them according to their HTTP caching headers. It makes repeat visits much faster and saves the user's data. The browser HTTP cache is private to that user.

## 63: What is a service worker cache?

A service worker is a script that runs in the background of a web app and can intercept network requests. Using the Cache Storage API (`caches.open`, `cache.put`, `cache.match`), it can store responses and serve them even when the user is offline. Unlike the HTTP cache, you control it fully from your own code.

## 64: What is database query caching?

It is caching the results of database queries so the same query does not hit the database again. It can be done in the app (store the query result in Redis under a key built from the query and its parameters) or inside some databases. MySQL had a built-in query cache, but it was removed in MySQL 8.0 because it scaled badly, so today this is usually done in the application layer.

## 65: What is the database buffer pool or page cache?

Databases keep recently used data pages in memory so they do not have to read them from disk each time. In PostgreSQL this is `shared_buffers` plus the operating system page cache; in MySQL InnoDB it is the buffer pool. This is a cache too, managed by the database. It is one reason why a query is often faster the second time you run it.

## 66: What is object caching?

Object caching means caching whole objects from your domain, like a user, a product or an order, usually as JSON in Redis. It is the most common kind of app-level caching. Other parts of the code can reuse the same cached object no matter which page or API needs it.

## 67: What is full page caching?

Full page caching stores the whole rendered HTML page and serves it as is to later visitors. It is very fast because the app does no work at all. It works best for pages that look the same for everyone, like blog posts, docs or product pages for logged-out users.

## 68: What is fragment caching?

Fragment caching stores only parts of a page, like the header, the sidebar or a product card. The page is still built per request, but the expensive parts are reused. It is useful when the page is mostly the same for everyone but has some personal parts, like the user's name or cart.

## 69: What is session caching?

Session caching is storing user sessions (login state, cart, preferences) in a fast store like Redis instead of in app memory or the database. This way any app server can handle any request, because they all read the session from the same place. Strictly speaking, sessions are often primary data, not a cache, so you should think about what happens if they are lost.

## 70: What is negative caching?

Negative caching means caching the fact that something does not exist. For example, if a user ID is not in the database, you cache "not found" for a short time. Without it, repeated requests for a missing item always go to the database, which wastes work and can be abused by attackers.

```ts
await redis.set(`user:${id}`, "__none__", "EX", 30);
```

## 71: What is a cold cache?

A cold cache is an empty cache, or one that does not yet hold the data that is being requested, for example right after a restart or a deploy. Almost every request is a miss, so the database gets a lot more load than usual until the cache fills up again.

## 72: What is a warm cache?

A warm cache already holds most of the data that users ask for, so the hit ratio is high and the system runs at normal speed. A cache becomes warm over time as requests fill it, or faster if you warm it on purpose.

## 73: What is cache warming?

Cache warming is filling the cache with data before users ask for it, so the first users do not get slow misses. For example, after a deploy you can run a script that loads the top 1,000 products into Redis. It is useful before planned traffic spikes like a sale or a product launch.

## 74: What is a cache stampede?

A cache stampede (or thundering herd, or dog-pile) happens when a popular key expires and many requests miss at the same moment. They all go to the database together to load the same value, which can overload it. It is a common problem with hot keys and short TTLs.

## 75: What is TTL jitter, and why is it useful?

Jitter means adding a small random amount to the TTL. If you cache 10,000 items at the same time with the same TTL, they all expire at the same time too, which causes a spike of misses. With jitter, expirations are spread out:

```ts
const ttl = 300 + Math.floor(Math.random() * 60); // 300-359 seconds
await redis.set(key, value, "EX", ttl);
```

## 76: What kind of data is a good fit for caching?

Data that is read much more often than it changes, is expensive to compute or fetch, and can be a little bit stale without causing harm. Examples: product details, user profiles, configuration, results of heavy reports, responses from slow third-party APIs, and rendered pages.

## 77: What kind of data should you not cache?

Be careful with:

- Data that must always be exact, like account balances during a payment.
- Data that changes on almost every request, so the cache would rarely hit.
- Very sensitive data, unless the cache is secured to the same level as the source.
- Data that is read only once, since caching it just wastes memory.
- Huge values that would push useful data out of the cache.

## 78: What is a cache layer?

A cache layer is a part of the system dedicated to caching, sitting between the users of data and the source of the data. It can be a Redis cluster, a CDN, or a module in your code that wraps database calls. Keeping caching in a clear layer makes it easier to change and to turn off when debugging.

## 79: What is serialization in caching?

Caches like Redis store strings or bytes, so objects have to be turned into a string before saving and back into an object after reading. This is serialization. JSON is the most common format. Others like MessagePack or Protocol Buffers are smaller and faster, but harder to read when debugging.

```ts
await redis.set("user:1", JSON.stringify(user));
const user = JSON.parse((await redis.get("user:1")) ?? "null");
```

## 80: What problem can happen with Date objects when caching JSON?

`JSON.stringify` turns a `Date` into a string, and `JSON.parse` does not turn it back into a `Date`. So after a round trip through the cache, `user.createdAt` is a string, and code like `user.createdAt.getTime()` breaks. You have to convert such fields back by hand, or use a serializer that keeps types.

## 81: What is a cache-control strategy for API responses?

It depends on the endpoint:

- Public data that changes rarely (list of countries): `public, max-age=86400`.
- Public data that changes often: short `max-age` plus `stale-while-revalidate`.
- User-specific data: `private, max-age=0` or `private, no-cache`.
- Sensitive data: `no-store`.

Many APIs default to `no-store` and only opt in to caching on endpoints where it is clearly safe.

## 82: Why are GET requests cached and POST requests usually not?

GET is meant to only read data and have no side effects, so it is safe to serve the same response again. POST usually changes data, so replaying a cached answer would be wrong. HTTP caches cache GET (and HEAD) by default when headers allow it. POST responses can technically be cached in rare cases, but in practice caches almost never do it.

## 83: Which HTTP status codes can be cached?

Some status codes are cacheable by default, meaning a cache can store them using heuristics even without explicit headers: 200, 203, 204, 206, 300, 301, 308, 404, 405, 410, 414 and 501. Others, like 302 or 500, are only cached if the response has explicit freshness headers. In practice you should always set `Cache-Control` explicitly instead of relying on defaults.

## 84: What is heuristic caching?

If a response has no `Cache-Control` max-age and no `Expires`, but has a `Last-Modified` header, caches are allowed to guess how long it stays fresh. A common guess is 10% of the time since it was last modified. This can lead to surprising caching, so it is better to always send an explicit `Cache-Control` header.

## 85: What is the difference between fresh and stale in HTTP caching?

A response is fresh while its age is lower than its freshness lifetime (from `max-age`, `s-maxage` or `Expires`). A fresh response can be served without contacting the server. Once its age goes past that lifetime, it is stale. A stale response is not deleted right away; it can still be revalidated or, in some cases, served while revalidating.

## 86: What is the stale-while-revalidate directive?

It lets a cache serve a stale response for a while after it expires, while it fetches a fresh one in the background:

```http
Cache-Control: max-age=60, stale-while-revalidate=300
```

For 60 seconds the response is fresh. For the next 300 seconds, the cache serves the old copy instantly and refreshes it behind the scenes. Users get fast responses, and the data is never more than a few minutes old.

## 87: What is the stale-if-error directive?

It allows a cache to serve a stale response when the origin returns an error (500, 502, 503, 504) or cannot be reached:

```http
Cache-Control: max-age=60, stale-if-error=86400
```

If the origin goes down, users keep getting the last good copy for up to a day instead of an error page. CDN support varies, so check the docs of the one you use.

## 88: What is a cache layer in front of a third-party API?

When your app calls an external API (weather, exchange rates, geolocation), you can cache its responses so you do not call it on every request. This makes your app faster, keeps you under the provider's rate limits and lowers costs. Check the provider's terms, because some limit how long you may keep their data.

## 89: What is the difference between a cache and a buffer?

A cache keeps copies of data so they can be read again quickly. A buffer holds data temporarily while it moves from one place to another, for example collecting writes before sending them to disk in one go. A cache is about reuse; a buffer is about smoothing out speed differences between a producer and a consumer.

## 90: What is the difference between a cache and a database?

A database is designed to store data safely and permanently, with durability and often transactions. A cache is designed for fast reads of copies and may lose data at any time. Redis can be used as both, but when you use it as a cache, you should treat everything in it as something that can disappear.

## 91: What is cache memory in a CPU, and how does it relate to software caching?

CPUs have small, very fast caches (L1, L2, L3) between the cores and main memory, because RAM is much slower than the CPU. They work on the same ideas as software caches: keep recently used data close, evict old data when full, and deal with consistency between cores. It is a good example that caching appears at every level of a computer.

## 92: What are L1 and L2 caches in application caching?

In apps, L1 usually means a local in-process cache, and L2 means a shared cache like Redis. A read checks L1 first, then L2, then the database. L1 is the fastest but small and per server; L2 is shared and bigger. This setup is called a multi-level or two-level cache.

## 93: What is locality of reference?

It is the observation that programs tend to read the same data again soon (temporal locality) and data close to what they just read (spatial locality). Caches work well because of it. If every request asked for completely random data, caching would not help much.

## 94: What is the working set?

The working set is the part of your data that is actively used in a given period. If your database has 100 GB but users only read about 2 GB of it each day, the working set is 2 GB. If your cache is big enough to hold the working set, you can get a high hit ratio without caching everything.

## 95: What is the 80/20 rule in caching?

Often a small part of the data gets most of the requests, for example 20% of products get 80% of views. This means even a fairly small cache that holds the popular items can serve most of the traffic. Real numbers vary, but this kind of uneven access is why caching works so well.

## 96: What is a hot key?

A hot key is a cache key that gets a very large share of the traffic, like the home page data or a celebrity's profile. Hot keys are good for hit ratio, but they can overload a single cache node, and when they expire they can cause a stampede.

## 97: What does it mean that caching trades consistency for speed?

When you serve data from a cache, it might not be the latest version. You get faster responses and less load, but users may see old data for a short time. Every caching decision is about how much staleness is acceptable for that data in exchange for the speed you gain.

## 98: What is eventual consistency in caching?

It means the cache will eventually have the right value, but not necessarily right away. After a change in the database, the cache may serve the old value until the key expires or is invalidated. For most data, like a product description, this short delay is fine.

## 99: What are the basic Redis commands used for caching?

```text
SET key value EX 60    # set with a 60 second TTL
GET key                # read
DEL key                # delete
EXPIRE key 60          # set or change TTL
TTL key                # seconds left before expiry
EXISTS key             # check if key exists
MGET k1 k2 k3          # read many keys at once
```

## 100: How do you set a key with a TTL in Redis from Node.js?

With ioredis:

```ts
import Redis from "ioredis";
const redis = new Redis(process.env.REDIS_URL!);

await redis.set("greeting", "hello", "EX", 60); // seconds
await redis.set("token", "abc", "PX", 1500); // milliseconds
const value = await redis.get("greeting");
```

## 101: What happens in Redis when a key with a TTL expires?

The key is removed and a `GET` returns `nil` as if it never existed. Redis removes expired keys in two ways: lazily, when someone tries to read an expired key, and actively, with a background job that checks random keys with a TTL and deletes the expired ones. So memory is freed even for keys nobody reads again.

## 102: Does updating a key with SET keep its TTL?

No. A plain `SET` removes the old TTL, so the key would never expire. If you want to keep the current TTL, use the `KEEPTTL` option, or set a new TTL in the same command:

```text
SET user:1 "new value" KEEPTTL
SET user:1 "new value" EX 300
```

This is an easy mistake that causes keys to live forever.

## 103: What is the difference between EXPIRE and SETEX?

`EXPIRE key seconds` sets a TTL on a key that already exists. `SETEX key seconds value` sets the value and the TTL in one atomic command. Today `SET key value EX seconds` is the usual way to do the same as `SETEX`, and it has more options like `NX`.

## 104: What does SET with NX do?

`NX` means "only set if the key does not exist". If the key already exists, nothing happens and Redis returns `nil`. It is used to avoid overwriting existing values and to build simple locks:

```ts
const ok = await redis.set("lock:report", "1", "EX", 30, "NX");
if (ok === "OK") {
  // we got the lock
}
```

## 105: What is maxmemory in Redis?

`maxmemory` sets how much memory Redis may use for data. When the limit is reached, Redis applies the eviction policy from `maxmemory-policy`. If you use Redis as a cache, you should always set it, otherwise Redis can use all the memory on the machine.

```text
maxmemory 2gb
maxmemory-policy allkeys-lru
```

## 106: What is the noeviction policy in Redis?

With `noeviction`, Redis does not delete anything when memory is full. Instead, write commands that would use more memory fail with an error. This is the right choice when Redis holds data you cannot lose, like a queue. For a pure cache it is usually wrong, because your writes start failing instead of old keys being dropped.

## 107: What is the difference between allkeys-lru and volatile-lru in Redis?

`allkeys-lru` can evict any key, using an approximate LRU. `volatile-lru` only evicts keys that have a TTL set. If Redis is used only as a cache, `allkeys-lru` (or `allkeys-lfu`) is the usual choice. `volatile-*` policies make sense when the same Redis also holds keys without a TTL that must not be evicted, though running separate instances is cleaner.

## 108: What are the main Redis eviction policies?

- `noeviction`: return errors on writes when full.
- `allkeys-lru` / `volatile-lru`: evict least recently used.
- `allkeys-lfu` / `volatile-lfu`: evict least frequently used.
- `allkeys-random` / `volatile-random`: evict random keys.
- `volatile-ttl`: evict keys with the shortest remaining TTL.

`allkeys-*` looks at all keys, `volatile-*` only at keys that have a TTL.

## 109: How do you check if a cache is working well?

Track at least these numbers:

- Hit ratio (hits divided by all lookups).
- Latency of cache reads and of the source on misses.
- Memory usage and number of evictions.
- Number of keys and expired keys.
- Error and timeout rate when talking to the cache.

In Redis, `INFO stats` shows `keyspace_hits`, `keyspace_misses`, `evicted_keys` and `expired_keys`.

## 110: What does a high number of evictions tell you?

It means the cache is too small for the data you are putting in it, so it keeps throwing items out before they are reused. This usually lowers the hit ratio. Fixes are to add memory, cache fewer or smaller items, shorten TTLs for rarely used data, or pick a better eviction policy.

## 111: Should the app crash if the cache is down?

Usually no. For a cache-aside setup, if Redis is not available, the app should log the error and read from the database, maybe with a short timeout on cache calls so it does not hang. It will be slower, but it keeps working. You do need to make sure the database can survive the extra load for a while.

```ts
async function safeGet(key: string) {
  try {
    return await redis.get(key);
  } catch (err) {
    logger.warn({ err }, "cache read failed");
    return null; // treat as a miss
  }
}
```

## 112: What is the latency difference between memory, Redis and a database?

Rough numbers, which vary a lot by setup:

- Local memory (a `Map` lookup): well under a microsecond.
- Redis in the same data center: around 0.2 to 1 ms, mostly network.
- A simple indexed database query: about 1 to 10 ms.
- A heavy query or a call to another region or API: tens to hundreds of ms.

This is why even a remote cache like Redis can save a lot of time.

## 113: Can caching make an application slower?

Yes. If the hit ratio is very low, every request pays for a cache lookup plus the database query. Large values that take long to serialize, a cache server that is far away, or a cache that is overloaded can also add latency. Caching only helps when the cost of a lookup is much smaller than the cost of a miss and the hit ratio is decent.

## 114: What is the cost of a cache miss?

On a miss you pay for the cache lookup, then the full cost of loading from the source, and then the cost of writing to the cache. So a miss is slightly slower than having no cache at all. That is fine when most requests are hits, but it is a reason not to cache data that is rarely read twice.

## 115: How do you delete a cached item when the data changes?

In the code that updates the data, after the database write succeeds, delete the cache key:

```ts
async function updateUser(id: string, data: Partial<User>) {
  await db.users.update(id, data);
  await redis.del(`user:${id}`);
}
```

The next read will miss and load the new value. Deleting is usually safer than writing the new value into the cache, because it avoids some race conditions.

## 116: What is a cache-control header for images that change rarely but have no hash in the name?

If the URL does not change when the image changes, a long `max-age` means users may see the old image for a long time. A middle ground:

```http
Cache-Control: public, max-age=86400, stale-while-revalidate=604800
```

The better fix is to add a version or hash to the URL, so you can cache it for a year and still update it.

## 117: How do you see in the browser if a response came from cache?

In Chrome DevTools, open the Network tab. The Size column shows `(memory cache)` or `(disk cache)` for responses served from the browser cache, and the status is often `200` with that note, or `304` if the browser revalidated. Make sure "Disable cache" is not checked, since it is often left on during development.

## 118: How can you tell if a response came from a CDN cache?

Look at the response headers. Most CDNs add a header like `X-Cache: HIT` / `MISS`, `CF-Cache-Status: HIT` on Cloudflare, or the standard `Cache-Status` header. The `Age` header also shows the response has been sitting in a cache. You can check with curl:

```bash
curl -sI https://example.com/logo.png | grep -i -E 'age|cache'
```

## 119: What is the Cache-Status header?

`Cache-Status` is a standard response header (RFC 9211) that caches add to explain what they did with a request. For example:

```http
Cache-Status: ExampleCDN; hit, ExampleProxy; fwd=uri-miss; stored
```

It replaces the many custom `X-Cache` headers with one format, though many CDNs still send their own headers too.

## 120: What does Ctrl+F5 or a hard reload do to caching?

A normal reload usually makes the browser revalidate the main page, and may still use cached sub-resources. A hard reload (Ctrl+Shift+R or Ctrl+F5) makes the browser skip its cache and fetch everything fresh from the network. It does not clear a CDN cache, so you can still get an old version from the CDN.

## 121: What is the bfcache?

The back/forward cache (bfcache) is a browser feature that keeps a whole page in memory, including its JavaScript state, when you navigate away. If you press Back, the page is restored instantly instead of being loaded again. Things like `unload` event listeners or `Cache-Control: no-store` on the page can stop a page from using it, though browsers are relaxing the `no-store` rule.

## 122: What is a CDN cache key?

It is the set of values a CDN uses to decide if two requests are "the same" and can share a cached response. By default it is usually the host, path and query string. You can often add headers, cookies or the device type, or remove query parameters that do not change the response (like `utm_source`). Fewer variations means a higher hit ratio.

## 123: Why do tracking query parameters hurt CDN hit ratio?

URLs like `/page?utm_source=twitter` and `/page?utm_source=email` return the same content, but if the CDN includes the full query string in the cache key, it stores them as separate entries and has to go to the origin for each. Removing those parameters from the cache key lets all of them share one cached copy.

## 124: What is a cache hit at the edge vs a cache hit at the origin?

An edge hit means the CDN served the response from its own cache close to the user; your servers did nothing. An origin hit means the request reached your infrastructure, but a cache there (Nginx, Redis, app cache) answered without doing the full work. Edge hits are the cheapest and fastest; origin cache hits still save database and CPU time.

## 125: What is prefetching, and how is it related to caching?

Prefetching is loading data before the user asks for it, based on a guess of what they will need next, and keeping it in a cache. For example, loading the next page of results, or using `<link rel="prefetch">` to load the next page's resources. When the user clicks, the data comes from the cache instantly.

## 126: What is client-side data caching in front-end apps?

Libraries like TanStack Query, SWR and Apollo Client keep API responses in memory in the browser, keyed by query. When a component asks for data that is already cached, it shows it at once and may refetch in the background. This avoids duplicate requests and makes navigation feel fast. It is a separate layer from the browser HTTP cache.

## 127: What is a cache entry?

A cache entry is one stored item: the key, the value, and some metadata like the time it was stored, its TTL or expiry time, and sometimes its size or access count. Eviction policies use this metadata to decide which entry to drop.

## 128: What is the difference between absolute and sliding expiration?

With absolute expiration, the item expires at a fixed time after it was stored, no matter how often it is read. With sliding expiration, every read resets the timer, so an item that keeps getting used never expires. Sliding is common for sessions (log out after 30 minutes of inactivity). For data caches, absolute is safer because the data still gets refreshed from time to time.

## 129: How do you implement sliding expiration in Redis?

Reset the TTL on every read. `GETEX` reads the value and sets a new TTL in one command:

```ts
const session = await redis.getex(`session:${id}`, "EX", 1800);
```

Before `GETEX` existed (Redis 6.2), people used `GET` followed by `EXPIRE`.

## 130: What is cache size, and how do you limit it?

Cache size is how much data the cache holds, measured in items or bytes. You limit it with settings like `maxmemory` in Redis, `-m` in Memcached, or `max` and `maxSize` in `lru-cache`. Size limits by bytes are safer than limits by count when values have very different sizes.

## 131: What is a cache namespace?

A namespace is a prefix that groups related keys, like `catalog:` or `session:`. It keeps keys from different features or services from clashing and makes it easy to find and manage them. Some caching libraries also use namespaces to invalidate a whole group at once by changing a version number in the prefix.

## 132: How do you clear the whole Redis cache?

`FLUSHDB` deletes all keys in the current database and `FLUSHALL` deletes all keys in all databases. Both are dangerous in production, because they also delete anything that is not cache, like sessions or locks, and they cause a cold cache and a load spike. Many teams rename or disable these commands in production.

## 133: Why should you avoid the KEYS command in production Redis?

`KEYS pattern` scans every key and blocks Redis while it runs, because Redis handles commands on one main thread. With millions of keys this can freeze Redis for seconds and make all other requests time out. Use `SCAN`, which goes through keys in small batches with a cursor:

```ts
const stream = redis.scanStream({ match: "product:*", count: 500 });
for await (const keys of stream) {
  if (keys.length) await redis.unlink(...keys);
}
```

## 134: What is the difference between DEL and UNLINK in Redis?

Both remove keys. `DEL` frees the memory right away on the main thread, which can block Redis if the value is large (a hash with millions of fields). `UNLINK` removes the key from the keyspace right away but frees the memory in a background thread, so it does not block. For deleting large or many keys, prefer `UNLINK`.

## 135: What is caching computed results?

Some results are expensive to calculate even if the input data is small: reports, recommendations, search facets, statistics. You can cache the result of the calculation, keyed by its inputs, so it is done once and reused. It is the same idea as memoization, but often stored in a shared cache with a TTL.

## 136: What is a CDN cache hit ratio, and what is a good value?

It is the share of requests the CDN served from its cache without going to the origin. For static assets with hashed names, 95% or more is normal. For dynamic or personal content it can be much lower. Some CDNs also show a byte hit ratio, which counts data volume instead of request count.

## 137: Why does the first request after a deploy sometimes feel slow?

Several caches may be cold at once: the app's local caches are empty after the restart, the CDN has not seen the new hashed asset files yet, and JIT compilation and connection pools are still warming up. The first users pay for all of this. Cache warming and rolling deploys help.

## 138: What is a CDN in front of an API, and when is it useful?

A CDN can cache GET API responses just like files, as long as you set proper `Cache-Control` headers. It helps with public data that many users request, like product lists, config, or exchange rates. Even a short `s-maxage` like 5 seconds can cut origin traffic a lot when an endpoint gets thousands of requests per second.

## 139: What is micro-caching?

Micro-caching is caching responses for a very short time, like 1 to 5 seconds. For a busy page, even one second of caching means the origin builds it at most once per second instead of hundreds of times. Users barely notice the staleness. It is often done in Nginx or at the CDN.

## 140: How does Nginx cache responses?

You define a cache zone and turn on caching for a location:

```nginx
proxy_cache_path /var/cache/nginx keys_zone=app:10m max_size=1g inactive=60m;

server {
  location / {
    proxy_cache app;
    proxy_cache_valid 200 10s;
    add_header X-Cache-Status $upstream_cache_status;
    proxy_pass http://app_upstream;
  }
}
```

Nginx stores responses on disk with keys in shared memory, and `$upstream_cache_status` shows HIT, MISS, STALE and so on.

## 141: What does it mean that a cache is transparent?

A transparent cache is one the caller does not need to know about. The code calls `getUser(id)` and gets the same result with or without the cache; only the speed changes. HTTP caches and read-through caches are usually transparent. Cache-aside code inside every function is less transparent, because each caller deals with the cache directly.

## 142: What is the difference between caching and replication?

Replication keeps full, managed copies of the database on other servers (replicas), kept up to date by the database itself. Caching keeps partial copies of selected data, managed by your app or a cache layer, with looser rules about freshness. Read replicas also reduce load on the primary, but they are still a database, with query support and durability.

## 143: What is caching DNS?

DNS lookups (turning a domain name into an IP address) are cached at many levels: the browser, the operating system, and DNS resolvers. Each DNS record has its own TTL. This is why changing a DNS record can take a while to reach everyone, since old answers stay in caches until their TTL runs out.

## 144: What is connection caching or pooling, and is it caching?

A connection pool keeps open database or HTTP connections so they can be reused instead of opened for every request. It is a kind of caching, but for resources, not data. It saves the time needed to set up TCP, TLS and authentication, which can be several milliseconds per connection.

## 145: What is cache coherence?

Cache coherence means that all caches holding a copy of the same data agree on its value. It is a big topic in CPUs with many cores, and it also shows up in apps with local caches on many servers. If one server updates a value, the others may still hold the old one unless you have a way to tell them.

## 146: Why is the phrase "there are only two hard things in computer science: cache invalidation and naming things" popular?

Because cache invalidation really is hard in practice. You have to know every write that can affect every cached value, deal with timing between the database and the cache, and handle many servers with their own caches. Getting it slightly wrong leads to users seeing old or wrong data, and those bugs are hard to reproduce.

## 147: What is a cache read timeout, and why set one?

It is the maximum time your app waits for the cache to answer. If Redis is slow or the network has a problem, a cache call without a timeout can hang for seconds, which is worse than just going to the database. A short timeout (tens of milliseconds) makes the app treat a slow cache as a miss and move on.

```ts
const redis = new Redis(url, { commandTimeout: 50, maxRetriesPerRequest: 1 });
```

## 148: What is the difference between a cache and a CDN?

A CDN is a specific kind of cache: a network of HTTP caches spread around the world, mainly for content sent to users. "Cache" is the general idea and can be anywhere: in memory, in Redis, in the browser, in the CPU. All CDNs cache, but not all caches are CDNs.

## 149: What is the risk of caching error responses?

If you cache a 500 or a timeout response for a long time, users keep getting the error even after the problem is fixed. Error responses should not be cached, or only for a very short time. On the other hand, caching a 404 for a short time (negative caching) is often useful to protect the backend.

## 150: What are the most common caching mistakes?

- Forgetting to invalidate after updates, so users see old data.
- No size limit on a local cache, causing memory leaks.
- Caching user-specific data in a shared cache or CDN under a shared key.
- Same TTL for many keys, so they all expire together.
- No fallback when the cache is down.
- Caching everything instead of measuring what actually needs it.

# Moderate Questions (151-300)

## 151: How would you write a reusable cache-aside helper in TypeScript?

Wrap the pattern in one function so every caller does not repeat it:

```ts
async function cached<T>(
  key: string,
  ttlSeconds: number,
  load: () => Promise<T>,
): Promise<T> {
  const hit = await redis.get(key);
  if (hit !== null) return JSON.parse(hit) as T;

  const value = await load();
  await redis.set(key, JSON.stringify(value), "EX", ttlSeconds);
  return value;
}

const product = await cached(`product:${id}`, 300, () => db.products.find(id));
```

The cache logic now lives in one place, so you can later add metrics, timeouts or stampede protection without changing callers.

## 152: Why is deleting the key usually better than updating it after a write?

If you update the cache with the new value, two writes that happen at the same time can finish in a different order in the database and in the cache, leaving the cache with the older value forever (until TTL). Deleting is idempotent: whatever the order, the key ends up gone, and the next read loads the current value from the database. Updating also wastes work if the value is not read again.

## 153: Should you delete the cache before or after updating the database?

After. If you delete first, another request can read the old value from the database and put it back in the cache before your database write finishes, so the cache holds stale data until the TTL. Deleting after the database write closes most of that window. There is still a small race left, which is covered by TTLs or by techniques like delayed double delete.

## 154: What is delayed double delete?

You delete the cache key, update the database, and then delete the key again after a short delay (for example 500 ms). The second delete removes any stale value that a concurrent reader may have put in the cache during the update. It reduces the race in cache-aside, but it is a workaround: the delay is a guess, and it adds more cache operations.

```ts
await redis.del(key);
await db.products.update(id, data);
setTimeout(() => redis.del(key).catch(() => {}), 500);
```

## 155: What happens if the database write succeeds but the cache delete fails?

The cache keeps the old value until its TTL expires. That is why every cached key should have a TTL as a safety net. You can also retry the delete, push it to a queue so it is retried later, or use change data capture to invalidate based on the database log, which does not depend on the app remembering to do it.

## 156: How do you invalidate a list that contains an item that changed?

Lists are harder than single objects, because one change can affect many cached lists (category pages, search results, "latest" lists). Common options:

- Give lists short TTLs and accept some staleness.
- Cache only the IDs in the list and load each item from its own cache, so item updates show up right away.
- Track which lists contain which items (tags) and delete those lists on change.
- Bump a version number for the whole group.

## 157: What is the "cache IDs, not objects" approach for lists?

Instead of caching a full list of product objects, cache only the list of IDs, and cache each product under its own key:

```ts
const ids: string[] = await cached(`category:${catId}:ids`, 600, () =>
  db.products.idsByCategory(catId),
);
const products = await redis.mget(ids.map((id) => `product:${id}`));
```

When a product changes, you only delete `product:<id>`, and every list shows the new data. The list of IDs only needs to change when items are added, removed or reordered.

## 158: What is versioned key invalidation?

You keep a version number for a group of keys and include it in each key. To invalidate the whole group, you increase the version. Old keys are not deleted; they just stop being used and expire on their own.

```ts
const v = (await redis.get("catalog:version")) ?? "1";
const key = `catalog:v${v}:product:${id}`;

// on a big catalog change
await redis.incr("catalog:version");
```

It is a cheap way to invalidate thousands of keys without scanning them.

## 159: What is tag-based invalidation?

You attach one or more tags to each cached entry, like `product:42` and `category:7`. When something changes, you invalidate by tag, and every entry with that tag is removed. CDNs support this with headers like `Surrogate-Key` (Fastly) or `Cache-Tag` (Cloudflare Enterprise and others). In Redis you can build it by keeping a set of keys per tag:

```ts
await redis.sadd("tag:category:7", "page:/shoes", "page:/shoes?page=2");
// invalidate
const keys = await redis.smembers("tag:category:7");
if (keys.length) await redis.unlink(...keys, "tag:category:7");
```

## 160: What is event-based cache invalidation?

When data changes, the service that owns it publishes an event (for example `ProductUpdated`) to a message bus like Kafka, RabbitMQ or Redis pub/sub. Every service that caches that data listens and deletes its own keys. It works well in microservices, because the writer does not need to know who caches what. The cost is more moving parts and a small delay before caches are cleared.

## 161: How do you invalidate local in-memory caches across many app servers?

Each server has its own copy, so deleting the key on one server is not enough. Common solutions:

- Short TTLs, so stale data does not live long.
- Redis pub/sub: the server that changed the data publishes the key, and every server deletes it from its local cache.
- Redis client-side caching with tracking, where Redis tells clients which keys changed.

```ts
sub.subscribe("invalidate");
sub.on("message", (_ch, key) => localCache.delete(key));
// after an update
await pub.publish("invalidate", `product:${id}`);
```

## 162: What is the downside of Redis pub/sub for cache invalidation?

Redis pub/sub is fire-and-forget. If a server is disconnected or restarting when the message is sent, it never gets it and keeps the stale value. So you still need a TTL on local entries. For stronger delivery you can use Redis Streams or another message broker, but for local cache invalidation, short TTL plus pub/sub is usually enough.

## 163: How do you cache data that depends on the user's language?

Include the language in the cache key, so each language has its own entry:

```ts
const key = `product:${id}:lang=${lang}`;
```

For HTTP caching, send `Vary: Accept-Language` if the response depends on that header, but this can create many variants. A cleaner way is to put the language in the URL (`/de/products/42`), so each language is a different URL and caches stay simple.

## 164: How do you cache paginated results?

Include the page parameters in the key, like `posts:page=3:size=20`. Offset pagination is tricky because adding one item shifts every page, so all pages can become stale at once; short TTLs are common. Cursor-based pagination works better with caching because a page that starts after a given ID stays mostly stable. Often only the first few pages are worth caching, since they get most of the traffic.

## 165: How do you cache search results?

Normalize the query (trim, lowercase, sort filters) so the same search always creates the same key, then hash it to keep keys short:

```ts
import { createHash } from "node:crypto";

const normalized = JSON.stringify({
  q: q.trim().toLowerCase(),
  filters: sortKeys(filters),
});
const key = "search:" + createHash("sha256").update(normalized).digest("hex");
```

Use short TTLs, because new or changed items should show up in search soon. Popular searches get good hit ratios; rare ones are mostly misses, which is fine.

## 166: Why normalize cache keys?

Different requests can mean the same thing: `?a=1&b=2` and `?b=2&a=1`, `Shoes` and `shoes`, extra spaces, default values left out or included. If you build keys from raw input, these become separate entries and your hit ratio drops. Normalizing (sorting parameters, lowercasing, removing defaults and junk parameters) makes them share one entry.

## 167: How do you choose between JSON, MessagePack and other formats for cached values?

JSON is easy to read and debug and is supported everywhere, so it is the usual default. MessagePack is binary, smaller and often faster to parse, which helps for large values or very high traffic. Protocol Buffers or Avro add a schema, which helps when several services in different languages share cached data. Measure first; for small objects the difference is often not worth the lost readability.

## 168: When should you compress cached values?

When values are large (several KB or more) and compress well, like JSON or HTML. Compression saves memory and network bandwidth, so you can fit more in the cache, at the cost of some CPU on each read and write. For small values it is not worth it. A simple rule is to compress only above a size threshold and store a flag so you know how to read it back.

```ts
import { gzipSync, gunzipSync } from "node:zlib";

const raw = Buffer.from(JSON.stringify(value));
const data =
  raw.length > 1024 ? Buffer.concat([Buffer.from("z"), gzipSync(raw)]) : raw;
```

## 169: How do you read many keys at once efficiently in Redis?

Use `MGET` for strings, or a pipeline for mixed commands. Each separate command costs a network round trip; batching saves most of that time.

```ts
const values = await redis.mget("user:1", "user:2", "user:3");

const results = await redis.pipeline().get("user:1").hgetall("cart:1").exec();
```

## 170: What is a Redis pipeline?

A pipeline sends many commands to Redis without waiting for each reply, then reads all the replies at once. It cuts the number of network round trips from N to 1, which matters a lot when latency is around a millisecond. Commands in a pipeline are not atomic; other clients' commands can run in between. For atomic groups, use `MULTI`/`EXEC` or a Lua script.

## 171: When would you use a Redis hash instead of a JSON string for a cached object?

A hash stores fields separately, so you can read or update one field (`HGET`, `HSET`) without loading and rewriting the whole object. It is useful for objects where parts change often, like counters or status fields. A JSON string is simpler when you always read the whole object. Since Redis 7.4 you can also set a TTL on individual hash fields with `HEXPIRE`.

## 172: How do you cache a leaderboard?

Use a Redis sorted set. Each member has a score, and Redis keeps them sorted:

```ts
await redis.zincrby("leaderboard:weekly", 50, "user:42");
const top10 = await redis.zrevrange("leaderboard:weekly", 0, 9, "WITHSCORES");
const rank = await redis.zrevrank("leaderboard:weekly", "user:42");
```

Reads of the top N and of a user's rank are fast even with millions of members. Strictly speaking this is often primary data kept in Redis, so plan how to rebuild it if Redis loses it.

## 173: How do you cache counters like view counts?

Increment the counter in Redis with `INCR`, which is atomic and fast, and write the total to the database from time to time instead of on every view. This is a form of write-back. You accept that if Redis loses data, you lose some views since the last flush, which is usually fine for view counts but not for money.

```ts
await redis.incr(`views:post:${postId}`);
```

## 174: How do you protect against a cache stampede with a lock?

On a miss, only one request is allowed to rebuild the value. It takes a short lock with `SET NX`. Other requests wait a little and read the cache again, or get a stale value if you keep one.

```ts
async function getWithLock(key: string, load: () => Promise<string>) {
  const hit = await redis.get(key);
  if (hit) return hit;

  const lockKey = `lock:${key}`;
  if (await redis.set(lockKey, "1", "EX", 10, "NX")) {
    try {
      const value = await load();
      await redis.set(key, value, "EX", 300);
      return value;
    } finally {
      await redis.del(lockKey);
    }
  }
  await new Promise((r) => setTimeout(r, 100));
  return getWithLock(key, load);
}
```

In real code, limit the number of retries so a stuck rebuild does not keep requests looping.

## 175: What is request coalescing (single-flight)?

Request coalescing means that if many requests in the same process ask for the same missing key at the same time, only one actually loads it, and the others wait for that same promise. It removes duplicate work inside one server without any locks in Redis.

```ts
const inFlight = new Map<string, Promise<unknown>>();

function singleFlight<T>(key: string, fn: () => Promise<T>): Promise<T> {
  const existing = inFlight.get(key);
  if (existing) return existing as Promise<T>;
  const p = fn().finally(() => inFlight.delete(key));
  inFlight.set(key, p);
  return p;
}
```

With 20 servers, you still get up to 20 loads, but not thousands.

## 176: What is probabilistic early expiration?

Each request that reads a key may decide to refresh it a bit before it expires, with a chance that grows as the expiry gets closer. Because the decision is random, usually only one request refreshes early, and the key never expires for everyone at once. The well-known version is the "XFetch" algorithm, which also takes into account how long the value takes to compute.

```ts
function shouldRefresh(expiresAt: number, computeMs: number, beta = 1) {
  return Date.now() - computeMs * beta * Math.log(Math.random()) >= expiresAt;
}
```

## 177: How do you implement stale-while-revalidate in an application cache?

Store two times with the value: when it becomes stale (soft TTL) and when it must be removed (hard TTL, the Redis TTL). If a read gets a stale-but-present value, return it right away and refresh in the background.

```ts
type Wrapped<T> = { value: T; staleAt: number };

async function swr<T>(
  key: string,
  softMs: number,
  hardSec: number,
  load: () => Promise<T>,
) {
  const raw = await redis.get(key);
  if (raw) {
    const w = JSON.parse(raw) as Wrapped<T>;
    if (Date.now() > w.staleAt) {
      singleFlight(key, async () => {
        const value = await load();
        await redis.set(
          key,
          JSON.stringify({ value, staleAt: Date.now() + softMs }),
          "EX",
          hardSec,
        );
      }).catch(() => {});
    }
    return w.value;
  }
  const value = await load();
  await redis.set(
    key,
    JSON.stringify({ value, staleAt: Date.now() + softMs }),
    "EX",
    hardSec,
  );
  return value;
}
```

## 178: What is the difference between a soft TTL and a hard TTL?

The soft TTL is when the value is considered old and should be refreshed. The hard TTL is when it is actually deleted. Between the two, you can still serve the old value, for example while refreshing in the background or when the source is down. This is the same idea as `max-age` plus `stale-while-revalidate` in HTTP.

## 179: How do you serve stale data when the database is down?

Keep values in the cache longer than their freshness time (soft TTL vs hard TTL). On a miss or stale read, try to load from the database. If that fails, return the stale value and maybe mark the response as possibly outdated. This turns a full outage into a degraded mode where users see slightly old data instead of errors.

## 180: What is a cache penetration problem?

Cache penetration is when many requests ask for keys that do not exist in the database, so the cache never has them and every request goes to the database. It can be caused by bugs or by attackers sending random IDs. Fixes are negative caching (cache "not found" for a short time), input validation, and a Bloom filter of existing keys.

## 181: What is cache avalanche?

A cache avalanche is when a large part of the cache becomes empty at the same time, so a flood of misses hits the database. Causes include many keys with the same TTL expiring together, or the cache server restarting. Fixes are TTL jitter, warming the cache, keeping the cache highly available, and rate limiting or queueing requests to the database.

## 182: What is cache breakdown?

Cache breakdown (sometimes called hotspot invalidation) is when one very hot key expires and many requests for it go to the database at the same moment. It is a stampede on a single key. Fixes are locks or single-flight, refresh-ahead, stale-while-revalidate, or not expiring that key at all and updating it in the background.

## 183: How do you cache API responses in an Express app?

For HTTP caching, set the right headers so browsers and CDNs do the work:

```ts
app.get("/api/countries", async (req, res) => {
  res.set(
    "Cache-Control",
    "public, max-age=3600, stale-while-revalidate=86400",
  );
  res.json(await getCountries());
});
```

For server-side caching, wrap the data loading in a cache-aside helper with Redis. Many apps do both: Redis to protect the database, and HTTP headers to avoid requests reaching the server at all.

## 184: How does Express generate ETags?

Express sets a weak ETag by default on responses sent with `res.send` and `res.json`, based on a hash of the body. If the request has a matching `If-None-Match`, Express answers `304` automatically. You can change this with `app.set("etag", "strong")` or turn it off with `app.set("etag", false)`. Note that the server still has to build the full response to compute the hash; the saving is only in bandwidth.

## 185: What is the difference between a strong and a weak ETag?

A strong ETag (`"abc"`) means the bytes are exactly the same. A weak ETag (`W/"abc"`) means the content is the same in meaning, but the bytes might differ, for example after a different compression or whitespace change. Weak ETags are fine for normal caching with `If-None-Match`, but strong ones are required for range requests and some conditional writes.

## 186: How can you avoid building the response just to compare ETags?

Use a version that you can get cheaply, like an `updated_at` timestamp or a version column, instead of hashing the full body. Check it before doing the heavy work:

```ts
app.get("/api/products/:id", async (req, res) => {
  const version = await db.products.getVersion(req.params.id);
  const etag = `"p${req.params.id}-v${version}"`;
  if (req.get("If-None-Match") === etag) return res.status(304).end();

  const product = await db.products.find(req.params.id);
  res.set({ ETag: etag, "Cache-Control": "no-cache" });
  res.json(product);
});
```

## 187: How do ETags help with concurrent updates?

The client sends the ETag it has in an `If-Match` header with a `PUT` or `PATCH`. The server only applies the update if the current ETag matches; otherwise it returns `412 Precondition Failed`. This prevents one user from silently overwriting another user's changes. It is optimistic locking over HTTP, and it reuses the same version ID used for caching.

## 188: What problems does Vary: Cookie cause?

Every user has different cookies, often including analytics cookies that change all the time. With `Vary: Cookie`, the cache stores a separate copy per unique cookie header, so the hit ratio drops almost to zero and memory fills with useless copies. It is better to not cache personal responses in shared caches, or to make the CDN key on one specific cookie value instead of the whole cookie header.

## 189: Why is Vary: User-Agent bad for caching?

There are thousands of different `User-Agent` strings, so the cache would store a separate copy for almost every browser version and hit ratio drops. If you need different responses for mobile and desktop, normalize the user agent into a small value (like `mobile` or `desktop`) at the CDN and vary on that, or use separate URLs.

## 190: How do you cache pages for logged-in and logged-out users?

Logged-out pages are the same for everyone, so cache them at the CDN. For logged-in users, either bypass the CDN cache (the CDN checks for a session cookie and skips the cache), or cache the shared part of the page and load the personal parts (user menu, cart) with a separate API call from the browser. Never cache a logged-in page under a shared key.

## 191: How do CDNs treat responses with Set-Cookie?

Many CDNs and proxies do not cache responses that have a `Set-Cookie` header by default, because caching it would give one user's cookie to others. Some CDNs do cache them and strip the cookie. You should know your CDN's behavior and avoid sending `Set-Cookie` on pages meant to be cached, for example by not starting a session for anonymous visitors.

## 192: How should you cache a response to a request with an Authorization header?

By default, shared caches must not store responses to requests with `Authorization`, unless the response explicitly allows it with `public`, `s-maxage` or `must-revalidate`. Usually that default is right, since the response is often specific to the user. If an authenticated endpoint returns the same data for everyone, you can opt in with `public, s-maxage=...`, but make sure that is really true.

## 193: How do you set up a CDN to bypass cache for certain requests?

Most CDNs let you write rules like "if the path starts with /api/account or the cookie `session` exists, do not cache". You can also set `Cache-Control: private` or `no-store` from the origin for those responses, which every CDN respects. Doing both is safer: the origin headers are the main protection, the CDN rules are a backup.

## 194: What is the difference between purging by URL, by prefix and by tag?

Purging by URL removes one exact cached object; it is precise but you must know every URL, including variations with query strings. Purging by prefix removes everything under a path like `/blog/`. Purging by tag removes every object that was tagged with a given key, like `product-42`, wherever it appears. Tags are the most useful for dynamic sites because one change can affect many pages.

## 195: What is a soft purge?

A soft purge marks cached objects as stale instead of deleting them. The next request triggers a revalidation, but if you also use `stale-while-revalidate` or `stale-if-error`, the CDN can still serve the old copy while it fetches the new one or if the origin fails. Fastly supports this. It avoids a burst of misses on the origin after a large purge.

## 196: How do you send cache tags from your origin?

Add a header listing the tags. The header name depends on the CDN:

```http
Surrogate-Key: product-42 category-7 home
Cache-Tag: product-42,category-7,home
```

`Surrogate-Key` is used by Fastly, `Cache-Tag` by Cloudflare and others. The CDN usually removes these headers before sending the response to the user. Then you purge by tag through the CDN's API when the data changes.

## 197: What is Surrogate-Control?

`Surrogate-Control` is a header for CDNs and reverse proxies only. It lets you give them a different caching rule than the one browsers see in `Cache-Control`, and the CDN strips it before passing the response on. There is also a newer standard, `CDN-Cache-Control` (RFC 9213), which does the same thing for CDNs in a standard way.

```http
Cache-Control: no-cache
CDN-Cache-Control: max-age=600
```

## 198: How do you cache a single-page app on a CDN?

- Hashed JS, CSS, fonts and images: `public, max-age=31536000, immutable`.
- `index.html`: `no-cache`, so the browser always checks for a new version.
- API calls: their own rules per endpoint.
- Set up the CDN so unknown routes (`/settings`) return `index.html` without caching it under a long TTL.

After a deploy, users get the new HTML on their next load, which points to the new hashed files.

## 199: What happens to users who have the old HTML after a deploy?

If you delete old hashed files on deploy, users with the old `index.html` in a tab will get 404 errors when the app lazy-loads an old chunk. To avoid this, keep old assets for a while after a deploy (S3 and most CDNs make this easy), and handle chunk load errors in the app by reloading the page.

## 200: How do service worker caching strategies differ?

- Cache first: use the cache, go to the network only on a miss. Good for static assets.
- Network first: try the network, fall back to the cache when offline. Good for HTML and fresh data.
- Stale-while-revalidate: return the cached copy at once and update it from the network in the background.
- Network only and cache only: no fallback either way.

Workbox provides these as ready-made strategies.

## 201: How do you implement a cache-first strategy in a service worker?

```js
self.addEventListener("fetch", (event) => {
  if (event.request.destination !== "image") return;
  event.respondWith(
    caches.open("images-v1").then(async (cache) => {
      const cached = await cache.match(event.request);
      if (cached) return cached;
      const response = await fetch(event.request);
      if (response.ok) cache.put(event.request, response.clone());
      return response;
    }),
  );
});
```

`response.clone()` is needed because a response body can only be read once.

## 202: How do you clean up old service worker caches?

Name caches with a version, and delete the ones you no longer use in the `activate` event:

```js
const CURRENT = ["static-v3", "images-v1"];

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((names) =>
        Promise.all(
          names
            .filter((n) => !CURRENT.includes(n))
            .map((n) => caches.delete(n)),
        ),
      ),
  );
});
```

Otherwise old caches stay in the user's browser and use storage forever.

## 203: What is the Clear-Site-Data header?

`Clear-Site-Data` tells the browser to delete data stored for your site:

```http
Clear-Site-Data: "cache", "cookies", "storage"
```

It is useful on logout, or as an emergency fix when you shipped a broken response that browsers cached for a long time. Support for the `"cache"` value differs between browsers, so do not rely on it as your only fix.

## 204: How do you fix a page that browsers cached with a very long max-age by mistake?

You cannot reach into users' caches directly. Options are: change the URL of the resource (add a version or hash), send `Clear-Site-Data: "cache"` from another page users will visit, or wait for the cache to expire. For a CDN you can purge, but browser copies stay. This is why long `max-age` should only be used on versioned URLs.

## 205: How do you cache GraphQL responses?

GraphQL is harder to cache at the HTTP level because most queries are POST requests to one URL. Options:

- Use GET for queries, or persisted queries with a hash in the URL, so CDNs can cache them.
- Cache per field or per type on the server (for example with DataLoader per request and Redis for resolvers).
- Use client caches like Apollo Client or urql, which normalize data by type and ID.
- Use `@cacheControl` hints if your server supports them, to compute a `Cache-Control` header for the response.

## 206: What is DataLoader, and is it a cache?

DataLoader batches and caches lookups within one request. If ten resolvers ask for user 42 during a single GraphQL request, DataLoader loads it once and returns the same result to all of them, and it batches different IDs into one query. Its cache lives only for one request, so it is about removing duplicate work, not about sharing data between requests.

## 207: What is a persisted query, and how does it help caching?

A persisted query is a GraphQL query that is registered on the server ahead of time and identified by a hash. The client sends the hash instead of the full query text, often as a GET request like `/graphql?id=abc123&variables=...`. Because the URL is short and stable, CDNs and browsers can cache it like a normal GET request.

## 208: What is an ORM second-level cache?

Some ORMs have two levels of cache. The first level is per session or unit of work (the same entity loaded twice in one transaction is only fetched once). The second level is shared across sessions and requests, often backed by Redis or another cache, and stores entities by ID. Hibernate is a well-known example. It is convenient, but invalidation only works if all writes go through the same ORM.

## 209: How do materialized views relate to caching?

A materialized view stores the result of a query as a table inside the database, so reading it is fast. You refresh it on a schedule or after changes (`REFRESH MATERIALIZED VIEW` in PostgreSQL). It is like caching a heavy query result, but inside the database, with SQL access and indexes. It is a good fit for reports and dashboards that can be a few minutes old.

## 210: How is a CQRS read model similar to a cache?

In CQRS you keep separate read models that are shaped for queries and updated from events or changes in the write model. Like a cache, a read model is a derived copy that can be rebuilt from the source and is usually eventually consistent. Unlike a typical cache, it is often stored durably and is designed to answer all reads, not just the hot ones.

## 211: How do you cache results from a slow external API that has rate limits?

Cache-aside with a TTL that matches how often the data changes, plus:

- Serve stale data if the API fails or you hit the rate limit.
- Use single-flight so many requests for the same item make one API call.
- Cache errors like 404 for a short time.
- Track your remaining quota and slow down refreshes when it gets low.

## 212: How do you test code that uses a cache?

- Unit tests: hide the cache behind an interface and use an in-memory fake, then check hits, misses and invalidation.
- Integration tests: run a real Redis (for example in Docker or with Testcontainers) and check TTLs, serialization and key names.
- Test that the app still works when the cache is down or slow.
- Test that writes invalidate the right keys, since that is where most bugs are.

## 213: How do you debug a "users see old data" bug?

Find which layer returned the old data. Check the response headers for `Age`, `Cache-Status`, `X-Cache` and `ETag`. Look in Redis for the key and its `TTL`. Check local caches on the servers. Then check if the write path actually invalidates that key, and if the key format used on read and write is the same. Very often the bug is a mismatch in key names, or a write path that was added later and forgot to invalidate.

## 214: How do you turn off caching temporarily for debugging?

Put caching behind a feature flag or config setting, so you can bypass it per environment or per request. Some teams support a request header like `X-Cache-Bypass` that is only honored for internal users. For HTTP caching, use DevTools "Disable cache" and `curl` with `Cache-Control: no-cache` in the request. Having a clean way to bypass caching makes it much faster to tell if a bug is caused by the cache.

## 215: How do you monitor Redis used as a cache?

Watch:

- `keyspace_hits` and `keyspace_misses` for the hit ratio.
- `used_memory` vs `maxmemory`, and `evicted_keys`.
- `connected_clients` and rejected connections.
- Latency (`LATENCY` commands, slow log with `SLOWLOG GET`).
- CPU, network and replication lag if you use replicas.

Export these with a Prometheus exporter or your cloud provider's metrics.

## 216: Why should you measure hit ratio per key type instead of only globally?

A global 90% hit ratio can hide that one important key type has a 10% hit ratio and causes most database load. Measuring per prefix (`user:`, `product:`, `search:`) shows which caches work and which are useless. You can do this in your cache helper by adding labels to metrics.

```ts
cacheHits.inc({ prefix: key.split(":")[0] });
```

## 217: How do you decide if a new cache is worth adding?

Measure first. Find the slow or heavy operations with profiling or database metrics. Check how often the same data is requested and how often it changes. If the same data is read many times between changes and the source is expensive, a cache helps. If not, look at other fixes like indexes or better queries first. A cache adds complexity and new kinds of bugs, so it should solve a real, measured problem.

## 218: Why can a cache hide a slow query instead of fixing it?

If a heavy query is cached, the app looks fast most of the time, but every miss still runs the slow query. After a cache flush or a cold start, all those slow queries run at once and the database may fall over. It is often better to fix the query (indexes, better SQL) first and add caching on top, so misses are not dangerous.

## 219: How do you handle cached data after a schema change in your code?

If the shape of a cached object changes (a renamed or new field), old cached values no longer match what the new code expects. Common fixes:

- Include a schema version in the key, like `user:v2:42`, and bump it when the format changes.
- Make the reading code tolerant of old formats.
- Flush the related keys during the deploy.

During a rolling deploy, old and new code run at the same time, so versioned keys are the safest option.

## 220: Why can rolling deploys cause cache bugs?

During a rolling deploy, servers with old code and new code share the same Redis. If the new code writes a new format under the same key, old servers may read it and crash, and the other way around. Use a version in the key, or make sure both versions can read both formats for the duration of the deploy.

## 221: What is the difference between Redis and Memcached for caching?

|                         | Redis                                          | Memcached                 |
| ----------------------- | ---------------------------------------------- | ------------------------- |
| Data types              | Many (strings, hashes, sets, sorted sets...)   | Strings only              |
| Persistence             | Optional (RDB, AOF)                            | None                      |
| Replication and cluster | Built in                                       | Client-side sharding only |
| Threads                 | Main thread for commands, I/O threads optional | Multi-threaded            |
| Max value size          | 512 MB                                         | 1 MB by default           |

For pure, simple caching both work well. Redis is more flexible; Memcached is simpler and scales across cores easily.

## 222: What is Memcached's slab allocator?

Memcached splits memory into slab classes, each holding items of a certain size range. An item goes into the class whose chunk size fits it. This avoids memory fragmentation, but it can waste memory if item sizes do not match chunk sizes well, and it can cause evictions in one slab class even when other classes have free space. Newer Memcached versions can move memory between classes automatically.

## 223: How do you share a Redis instance between caching and other uses safely?

It is better not to, but if you must: use clear key prefixes, set TTLs on all cache keys, and use a `volatile-*` eviction policy so only keys with a TTL can be evicted. Even then, the cache can push memory to the limit and cause write errors for your other data. Running separate Redis instances (or databases with separate memory limits) for cache and for durable data is much safer.

## 224: Should Redis persistence be on when Redis is only a cache?

Often no. A pure cache can be rebuilt from the database, so persistence just adds disk I/O and fork overhead. But turning on RDB snapshots can help you avoid a fully cold cache after a restart, which protects the database from a load spike. It is a trade-off between restart warm-up and runtime cost.

## 225: What is Redis replication, and does it help a cache?

Redis replication keeps one or more replicas in sync with a primary. For a cache, it helps in two ways: if the primary fails, a replica can take over without losing the warm cache, and you can send reads to replicas to spread load. Replication is asynchronous, so a replica can briefly return older data than the primary.

## 226: What is Redis Sentinel?

Sentinel is a system that watches Redis primaries and replicas, detects when a primary fails, and promotes a replica to be the new primary. Clients ask Sentinel where the current primary is. It gives high availability for a non-clustered Redis setup. Many teams now use managed Redis or Valkey services that handle this for them.

## 227: What is Redis Cluster?

Redis Cluster shards data across several primary nodes, each with its own replicas. Keys are mapped to 16,384 hash slots, and each node owns a range of slots. It lets the cache grow beyond the memory of one machine and spreads the load. Clients must be cluster-aware, and multi-key commands only work when all keys are in the same slot.

## 228: What are hash tags in Redis Cluster keys?

If a key contains `{...}`, only the part inside the braces is used to choose the hash slot. So `{user:42}:profile` and `{user:42}:cart` land on the same slot and you can use them together in `MGET`, transactions or Lua scripts. Be careful not to put too many keys under the same hash tag, or one node gets all of them.

## 229: How do you connect to Redis Cluster with ioredis?

```ts
import Redis from "ioredis";

const cluster = new Redis.Cluster(
  [
    { host: "redis-1", port: 6379 },
    { host: "redis-2", port: 6379 },
  ],
  { scaleReads: "slave" },
);

await cluster.set("product:1", "data", "EX", 60);
```

The client learns the slot map from the cluster and sends each command to the right node. `scaleReads` lets it send reads to replicas.

## 230: What is a cache aside with read replicas problem?

If you load data into the cache from a database read replica, you might read an old value because the replica is behind the primary. Right after a write and a cache delete, a reader can fill the cache from the replica with the old value, and it stays there until the TTL. A safer option is to read from the primary when refilling the cache shortly after a write, or to use short TTLs.

## 231: How do you cache data in a serverless function?

Serverless functions can keep variables between invocations while the same instance stays warm, so a module-level variable works as a small local cache. But instances come and go, and many run in parallel, so the hit ratio is unpredictable. For shared caching use an external store like Redis, Valkey or a managed service such as DynamoDB with DAX, ElastiCache or Upstash.

```ts
let configCache: { value: Config; at: number } | undefined;

export async function handler() {
  if (!configCache || Date.now() - configCache.at > 60_000) {
    configCache = { value: await loadConfig(), at: Date.now() };
  }
  // use configCache.value
}
```

## 232: Why can connecting to Redis from serverless functions be a problem?

Each function instance opens its own connection, and with high concurrency you can have thousands of instances, which can exceed Redis connection limits. Cold starts also pay the cost of setting up the connection. Solutions are reusing the connection across invocations, using a connection proxy, or using an HTTP-based Redis service designed for serverless.

## 233: How do you cache configuration and feature flags?

Config changes rarely but is read on almost every request, so cache it in local memory with a short TTL (say 30 to 60 seconds), and refresh in the background. Many feature flag SDKs do this already: they keep flags in memory and get updates by polling or streaming. If the config service is down, keep using the last known values instead of failing.

## 234: How do you cache in a multi-tenant application?

Always include the tenant ID in the key, like `tenant:7:product:42`, so one tenant never gets another tenant's data. Watch out for shared helpers that build keys without the tenant. You may also want limits per tenant, so one large tenant does not push everyone else's data out of the cache.

## 235: How do you cache permissions or authorization data?

Permissions are read on every request, so caching them helps a lot. But stale permissions are a security risk: a user whose access was removed might keep it until the cache expires. Use short TTLs, invalidate on every permission change, and for critical actions (deleting data, payments) consider checking the source directly.

## 236: How long should you cache JWT validation keys (JWKS)?

The JSON Web Key Set used to verify tokens changes rarely, so cache it in memory, for example for several hours, and respect its HTTP cache headers. When a token has a key ID (`kid`) that is not in your cache, refetch the JWKS once, with a rate limit, because the provider may have rotated keys. Libraries like `jose` do this with `createRemoteJWKSet`.

## 237: How do you cache responses that are expensive to build and rarely change, like a sitemap?

Generate it once and store it, either in Redis, in object storage, or at the CDN with a long `s-maxage`. Regenerate it on a schedule or when content changes, instead of on a user request. Users and crawlers always get the cached copy, and the heavy work runs in the background.

## 238: What is the difference between precomputing and caching?

Caching computes a value when someone asks for it and keeps it for reuse. Precomputing computes values ahead of time, before anyone asks, often on a schedule or after a change. Precomputing gives fast first requests and steady load on the source, but you may compute things nobody reads. Many systems precompute the most popular data and use caching for the rest.

## 239: How do you avoid caching a partial or broken result?

Only cache after the whole value was loaded successfully and passes basic checks. Do not cache exceptions, timeouts, or half-filled objects from a failed call to another service. If an upstream service returned a fallback or partial response, either do not cache it or cache it with a much shorter TTL.

## 240: How do you cache null or empty results correctly?

Use a special marker value to tell "cached as empty" apart from "not in cache":

```ts
const NONE = "__none__";

const hit = await redis.get(key);
if (hit === NONE) return null;
if (hit !== null) return JSON.parse(hit);

const value = await load();
await redis.set(
  key,
  value === null ? NONE : JSON.stringify(value),
  "EX",
  value === null ? 30 : 300,
);
return value;
```

Give empty results a shorter TTL, because a missing item may be created soon.

## 241: What is a write-through cache implementation in code?

```ts
async function saveProduct(product: Product) {
  await db.products.upsert(product);
  await redis.set(`product:${product.id}`, JSON.stringify(product), "EX", 3600);
}
```

The cache is updated as part of the write, so the next read is a hit with fresh data. If the cache write fails, you should delete the key or let it expire, since the cache now disagrees with the database.

## 242: When is write-through a good choice?

When data is read soon and often after it is written, and you want reads to always hit with fresh data. For example, user profiles that are updated and then shown right away. It is less useful when much of the written data is never read, since you pay to cache it anyway, and it adds latency to every write.

## 243: When is write-back a good choice?

When you have many writes to the same keys and can tolerate losing a few of them, like counters, likes, view counts, or last-seen timestamps. Write-back merges them into fewer database writes. It is a bad choice for orders, payments or anything you cannot lose or must see in the database right away.

## 244: How would you implement write-back with Redis?

Write updates to Redis and mark the key as dirty. A background worker periodically reads the dirty keys and writes them to the database in batches.

```ts
async function addLike(postId: string) {
  await redis
    .multi()
    .incr(`likes:${postId}`)
    .sadd("dirty:likes", postId)
    .exec();
}

async function flushLikes() {
  const ids = await redis.spop("dirty:likes", 500);
  for (const id of ids) {
    const count = Number(await redis.get(`likes:${id}`));
    await db.posts.updateLikes(id, count);
  }
}
```

Use Redis persistence or a stream if you need to survive a crash between flushes.

## 245: What is cache warming after a deploy, and how do you do it?

Before sending traffic to new instances, load the most used keys into the cache. You can keep a list of the hottest keys (from metrics or access logs), replay recent read requests, or run the main queries once. For local caches, do this in a startup step before the health check passes, so the load balancer only sends traffic to warm servers.

## 246: How do you avoid cache warming overloading the database?

Warm in batches with a concurrency limit, not everything at once. Warm the most popular data first and let the rest fill naturally. Spread warming across time, and do it during low traffic if possible. Warming that runs too fast can cause the same database spike you were trying to avoid.

## 247: How does a CDN origin shield work?

An origin shield is one CDN location chosen to sit between all other edge locations and your origin. When an edge misses, it asks the shield instead of the origin. The shield has a much better hit ratio because it collects requests from all edges, so the origin gets far fewer requests. CloudFront calls it Origin Shield; other CDNs call it tiered caching.

## 248: What is tiered caching in CDNs?

Tiered caching means CDN locations are arranged in levels. Lower-tier edges ask upper-tier locations on a miss, and only the top tier talks to your origin. This reduces origin traffic and improves hit ratio for content that is not popular enough to be cached at every edge. It adds a bit of latency on misses but usually saves a lot overall.

## 249: How do you cache responses that vary by device type?

Have the CDN detect the device (many CDNs provide a header like `CloudFront-Is-Mobile-Viewer`) and add it to the cache key, or rewrite the request to a different path per device type. Then the origin sends `Vary` on that normalized header only. This gives you two or three variants per URL instead of thousands.

## 250: How do you cache content that varies by country?

Most CDNs pass a country header to the origin (like `CloudFront-Viewer-Country` or `CF-IPCountry`). Add it to the cache key only for pages that really differ by country. Including it on every page multiplies the number of cache entries by the number of countries and lowers the hit ratio. Using country-specific URLs is often simpler.

## 251: How do you cache API responses in Nginx only for anonymous users?

Skip the cache when a session cookie is present:

```nginx
location /api/ {
  proxy_cache app;
  proxy_cache_valid 200 30s;
  proxy_cache_bypass $cookie_session;
  proxy_no_cache $cookie_session;
  proxy_pass http://app_upstream;
}
```

`proxy_cache_bypass` makes Nginx not read from the cache, and `proxy_no_cache` makes it not store the response.

## 252: What does proxy_cache_lock do in Nginx?

With `proxy_cache_lock on`, when many requests miss on the same key at the same time, only the first one goes to the upstream. The others wait until the response is in the cache (or until `proxy_cache_lock_timeout`). It is built-in stampede protection.

```nginx
proxy_cache_lock on;
proxy_cache_lock_timeout 5s;
```

## 253: What does proxy_cache_use_stale do in Nginx?

It lets Nginx serve a stale cached response in certain cases, like when the upstream is down or while another request is updating the cache:

```nginx
proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
proxy_cache_background_update on;
```

With `updating` and `proxy_cache_background_update`, Nginx behaves like stale-while-revalidate: one request refreshes in the background and others get the stale copy.

## 254: How do you build a two-level cache with local memory and Redis?

Check local memory first, then Redis, then the database. Fill both on the way back.

```ts
const local = new LRUCache<string, string>({ max: 5000, ttl: 10_000 });

async function get2L(key: string, load: () => Promise<string>) {
  const l1 = local.get(key);
  if (l1 !== undefined) return l1;

  const l2 = await redis.get(key);
  if (l2 !== null) {
    local.set(key, l2);
    return l2;
  }

  const value = await load();
  await redis.set(key, value, "EX", 300);
  local.set(key, value);
  return value;
}
```

Keep the local TTL short, since local copies are harder to invalidate.

## 255: What are the trade-offs of a two-level cache?

Pros: hot keys are served from memory with no network hop, and Redis load drops a lot. Cons: each server holds its own copy, so after an update some servers serve old data until the local TTL ends or an invalidation message arrives. It also uses more memory per server and adds complexity. It is worth it for very hot, rarely changing data.

## 256: What is the difference between caching at the controller level and at the data access level?

Caching at the controller (or HTTP) level stores whole responses, which skips the most work but is harder to invalidate because one response may combine many pieces of data. Caching at the data access level stores individual objects or queries, which is easier to invalidate and reuse across endpoints, but you still pay for building the response. Many apps use both.

## 257: How would you add caching to a NestJS app?

NestJS has a cache module (`@nestjs/cache-manager`) that wraps the `cache-manager` library. You can inject the cache and use it manually, or use `CacheInterceptor` to cache GET responses automatically. For Redis, configure a Redis store (the current versions use Keyv adapters such as `@keyv/redis`).

```ts
@Injectable()
export class ProductsService {
  constructor(@Inject(CACHE_MANAGER) private cache: Cache) {}

  async find(id: string) {
    const key = `product:${id}`;
    const hit = await this.cache.get<Product>(key);
    if (hit) return hit;
    const product = await this.repo.findOneBy({ id });
    await this.cache.set(key, product, 300_000); // ms in cache-manager v5+
    return product;
  }
}
```

## 258: What is cache-manager in Node.js?

`cache-manager` is a library that gives a common interface (`get`, `set`, `del`, `wrap`) over different stores, like memory or Redis, and supports multiple levels. Its `wrap` function implements cache-aside: it returns the cached value or calls your function, caches the result and returns it. Recent versions use Keyv for store adapters and TTLs in milliseconds.

## 259: How do you choose TTLs for different layers in a multi-layer cache?

Usually shorter at the outer layers close to the user and longer inside, or shorter on the layers that are hard to invalidate. For example: browser `max-age=60`, CDN `s-maxage=600` (you can purge it), Redis 1 hour (you invalidate on write), local memory 10 seconds (hard to invalidate across servers). Keep in mind that staleness adds up across layers: the worst case is roughly the sum of the TTLs.

## 260: Why does staleness add up across cache layers?

Each layer can refill itself from the layer behind it. If Redis holds a value that is 5 minutes old and the CDN fetches it right before Redis expires, the CDN can then hold that already old value for its own full TTL. So with layers of 5 minutes and 10 minutes, a user can see data that is up to about 15 minutes old. Invalidate from the inside out to avoid refilling outer layers with old data.

## 261: How do you invalidate several cache layers in the right order?

Start with the layer closest to the source and move outward: first the database is updated, then Redis, then local caches, then the CDN, and the browser last (usually through short TTLs). If you purge the CDN first, it can refill from a Redis copy that has not been cleared yet, and you are back to stale data.

## 262: What is a cache-control strategy for a news site's article pages?

Articles are read by many people and change rarely after publishing, but corrections must show up quickly. A common setup is a short browser TTL and a longer CDN TTL with purge:

```http
Cache-Control: public, max-age=60, s-maxage=3600, stale-while-revalidate=60, stale-if-error=86400
Surrogate-Key: article-123 section-politics
```

When an editor saves a change, the CMS purges `article-123` at the CDN.

## 263: How do you cache an expensive dashboard query?

Dashboards usually tolerate a few minutes of delay. Options:

- Cache the query results in Redis with a TTL of a few minutes, keyed by the filters.
- Precompute the numbers on a schedule into a summary table or materialized view.
- Show "last updated at" in the UI so users know the data is not live.

For dashboards with many users and the same filters, precomputing is often the best choice.

## 264: How do you cache data that is updated every second, like stock prices?

Classic TTL caching does not fit well, since data changes constantly. Instead, keep the latest value in Redis and update it when a new price arrives (write-through), and push updates to clients with WebSockets or server-sent events. A very short micro-cache (like 1 second) on the HTTP endpoint can still protect the backend from many readers.

## 265: How do you cache user sessions in Redis with Express?

Use `express-session` with a Redis store:

```ts
import session from "express-session";
import { RedisStore } from "connect-redis";
import { createClient } from "redis";

const client = createClient({ url: process.env.REDIS_URL });
await client.connect();

app.use(
  session({
    store: new RedisStore({ client, prefix: "sess:" }),
    secret: process.env.SESSION_SECRET!,
    resave: false,
    saveUninitialized: false,
    cookie: { secure: true, httpOnly: true, maxAge: 1000 * 60 * 60 },
  }),
);
```

The session TTL in Redis follows the cookie `maxAge`.

## 266: How do you cache rate limit counters?

Rate limits are a common Redis use, though they are counters more than cache. A simple fixed window:

```ts
async function allow(userId: string, limit = 100) {
  const key = `rl:${userId}:${Math.floor(Date.now() / 60_000)}`;
  const [[, count]] = (await redis
    .multi()
    .incr(key)
    .expire(key, 60)
    .exec()) as [[null, number]];
  return count <= limit;
}
```

For smoother limits, use a sliding window with sorted sets or a token bucket in a Lua script.

## 267: How do you make sure a cached value and its TTL are set atomically?

Use one command that sets both, like `SET key value EX 60`. If you do `SET` and then `EXPIRE` as two commands and the app crashes in between, the key has no TTL and lives forever. For several related operations, use `MULTI`/`EXEC` or a Lua script.

## 268: What is a Lua script in Redis, and when do you use it for caching?

Redis can run Lua scripts atomically on the server with `EVAL` (or, since Redis 7, with Functions). Nothing else runs while the script runs. You use it when you need read-check-write logic without races, like "set this value only if the current version is lower" or "release this lock only if I still own it".

```ts
const releaseLock = `
if redis.call("get", KEYS[1]) == ARGV[1] then
  return redis.call("del", KEYS[1])
end
return 0`;
await redis.eval(releaseLock, 1, "lock:report", token);
```

## 269: Why should a cache lock store a unique token?

If request A takes a lock and its work takes longer than the lock TTL, the lock expires and request B takes it. When A finishes and runs `DEL`, it would delete B's lock. By storing a random token and deleting only if the value still matches (atomically, with a Lua script), each request only releases its own lock.

## 270: What is the risk of very long TTLs?

Long TTLs give a high hit ratio, but if invalidation fails or is forgotten somewhere, users see stale data for a long time. They also keep rarely used data in memory longer, pushing out more useful data. A long TTL is fine when you have reliable invalidation; otherwise prefer a shorter TTL as a safety net.

## 271: What is the risk of very short TTLs?

The hit ratio drops because items expire before they are reused, so the database load goes up. Very short TTLs on hot keys also cause frequent stampedes. If you need data that is always fresh, a short TTL is often a sign that you should invalidate on writes instead.

## 272: How do you cache data from a microservice you do not own?

Find out how often the data changes and whether the owning service publishes change events. If it does, cache with a long TTL and invalidate on events. If not, use a TTL that matches the acceptable staleness, plus stale-if-error so you can survive their outages. Respect any `Cache-Control` headers the service sends. Agree with the owning team on what staleness is acceptable.

## 273: Why is it risky for many services to cache the same data independently?

Each service has its own TTL and invalidation rules, so different parts of the system can show different values for the same thing at the same time, for example the product page and the cart showing different prices. When the owning service changes the data, it has no idea who to tell. Central events, shared invalidation rules, or asking the owning service to provide the cached view help.

## 274: How do you handle cache key collisions between services?

Prefix keys with the service name (`orders:`, `catalog:`), and preferably give each service its own Redis instance or at least its own ACL user that can only access its prefix. Redis ACLs support key patterns:

```text
ACL SETUSER catalog on >secret ~catalog:* +@read +@write
```

## 275: How do you use Redis ACLs for a cache?

Create a user per app with only the commands and key patterns it needs. A cache user usually needs `GET`, `SET`, `DEL`, `MGET`, `EXPIRE` and similar, on its own prefix, and should not be able to run `FLUSHALL`, `CONFIG` or `KEYS`. This limits damage from bugs and from a leaked password.

## 276: How do you size a Redis cache?

Estimate the number of keys you want to keep and the average size of key plus value plus overhead (Redis adds tens of bytes per key). Multiply, then add room for fragmentation and replication buffers. For example, 2 million keys of about 1 KB each is about 2 GB of data, so a node with 3 to 4 GB is a reasonable start. Then watch evictions and hit ratio and adjust.

## 277: How do you find large keys in Redis?

Use `redis-cli --bigkeys` or `redis-cli --memkeys`, which scan the keyspace and report the largest keys per type. For a single key, `MEMORY USAGE key` gives its size in bytes. Large keys slow down reads, replication and deletes, and they can hurt eviction, so it is worth checking them regularly.

## 278: How do you find hot keys in Redis?

With the LFU eviction policy enabled, `redis-cli --hotkeys` reports the most accessed keys. You can also use `OBJECT FREQ key` for a single key under LFU, sample traffic with `MONITOR` (only briefly, because it is expensive), or count accesses in your app's cache helper. Managed services often have hot key metrics too.

## 279: What are the trade-offs of LRU vs LFU for a web cache?

LRU adapts quickly to change: new popular items get cached right away. But a single scan over many rarely used items (a crawler, a batch job) can push out the popular ones. LFU keeps items that are popular over time and resists scans better, but it can be slow to drop items whose popularity has passed. In Redis, try `allkeys-lfu` if a few keys are always popular and you see scan-like traffic.

## 280: What are the lfu-log-factor and lfu-decay-time settings in Redis?

Redis LFU uses a small counter per key that grows logarithmically, so it can track very popular keys in 8 bits. `lfu-log-factor` controls how fast the counter grows (higher means it takes more hits to reach the top). `lfu-decay-time` controls how many minutes it takes for the counter to decrease, so keys that stopped being popular can be evicted. The defaults work for most cases.

## 281: How does Redis approximate LRU?

Redis does not keep a full LRU list, because that would cost memory per key. Instead, when it needs to evict, it samples a few random keys (`maxmemory-samples`, default 5), and keeps a small pool of good candidates, then evicts the one that was idle the longest. With 10 samples it is very close to true LRU. This keeps eviction cheap.

## 282: What happens to a cache when Redis does a failover?

A replica becomes the new primary. Since replication is asynchronous, the last few writes before the failure may be lost, which for a cache usually just means a few extra misses. Clients have to reconnect to the new primary, which can cause a short burst of errors or timeouts. Your app should treat these as misses and keep going.

## 283: How do you handle cache errors in production without flooding logs?

Treat cache errors as misses, count them in metrics, and log them with sampling or rate limiting. If the cache is down, every request will fail to reach it, and logging each one can create millions of lines. A circuit breaker around the cache client also helps: after many failures, skip the cache for a short time instead of waiting for timeouts on every request.

## 284: How does a circuit breaker help with a cache outage?

When cache calls keep failing or timing out, the circuit breaker "opens" and the app stops calling the cache for a while, going directly to the database. This avoids paying a timeout on every request. After a pause, it lets a few calls through to check if the cache is back. Make sure the database can handle the extra load, or combine this with rate limiting.

## 285: How do you protect the database when the cache fails?

- Rate limit or queue requests to the database.
- Use single-flight so duplicate requests collapse into one.
- Serve stale data from a local or secondary cache if possible.
- Turn off expensive, non-critical features (load shedding).
- Keep the cache highly available with replicas and failover.

Without these, a cache outage often turns into a database outage.

## 286: How do you cache responses of a slow endpoint without changing the code much?

Put a cache in front of it at the HTTP level: a reverse proxy like Nginx or Varnish, or a CDN, with a `Cache-Control` header set by the app or by the proxy. This needs no changes to the business logic. It only works well if the response is the same for many users and you are fine with a TTL-based freshness.

## 287: How do you cache file downloads from object storage like S3?

Put a CDN (like CloudFront) in front of the bucket, and set `Cache-Control` on the objects when you upload them. For private files, use signed URLs or signed cookies, and make sure the signature parameters are not part of the cache key, or every signed URL becomes a separate cache entry.

```bash
aws s3 cp app.3f9a1c.js s3://my-bucket/assets/ \
  --cache-control "public, max-age=31536000, immutable"
```

## 288: How do you cache image resizing results?

Resizing on every request is expensive, so cache the output. Put the size and format in the URL (like `/img/123?w=400&fmt=webp`), let the CDN cache the result with a long TTL, and limit the allowed sizes to a fixed list so attackers cannot fill your cache with endless variants. Many CDNs offer image resizing with built-in caching.

## 289: How do you cache server-side rendered pages?

Cache the full HTML at the CDN or in a reverse proxy for anonymous users, with a short `s-maxage` and `stale-while-revalidate`. For personalized pages, cache the data the page needs instead of the HTML, or render the shared shell and load personal parts on the client. Frameworks like Next.js have their own caching layers for data and rendered routes, which you configure per route.

## 290: What is incremental static regeneration (ISR)?

ISR is a technique from frameworks like Next.js where pages are pre-rendered as static HTML and then regenerated in the background after a set time or on demand (for example with `revalidatePath` or `revalidateTag`). Users get a cached static page, and the next request after it becomes stale triggers a rebuild. It is basically stale-while-revalidate for rendered pages.

## 291: How do you cache data per request in a Node.js server?

For work that repeats within one request (like loading the current user in several places), keep a small cache that lives only for that request. You can attach it to the request object or use `AsyncLocalStorage`, so it is thrown away when the request ends and never leaks between users.

```ts
import { AsyncLocalStorage } from "node:async_hooks";

const requestCache = new AsyncLocalStorage<Map<string, unknown>>();

app.use((req, res, next) => requestCache.run(new Map(), next));
```

## 292: Why is a module-level cache dangerous for user data in Node.js?

A module-level variable is shared by every request the process handles. If you store per-user data there under a key that does not include the user (or by mistake under a fixed key), one user can see another user's data. Use per-request caches for user context, and always include the user ID in shared cache keys.

## 293: How do you cache the result of an async function and avoid duplicate calls?

Cache the promise, not the result. Then calls made while the first one is still running get the same promise:

```ts
const cache = new Map<string, Promise<Rate>>();

function getRate(currency: string) {
  let p = cache.get(currency);
  if (!p) {
    p = fetchRate(currency).catch((err) => {
      cache.delete(currency); // do not cache failures
      throw err;
    });
    cache.set(currency, p);
  }
  return p;
}
```

Add a TTL or size limit for real use.

## 294: How do you cache HTTP responses on the client side in Node.js?

Node's built-in `fetch` (undici) does not cache by default. Since undici 7 you can add a cache interceptor that follows HTTP caching rules:

```ts
import { Agent, interceptors, setGlobalDispatcher } from "undici";

setGlobalDispatcher(new Agent().compose(interceptors.cache()));
const res = await fetch("https://api.example.com/rates");
```

Otherwise, cache the parsed results yourself with cache-aside.

## 295: What is No-Vary-Search?

`No-Vary-Search` is a newer response header that tells the browser which query parameters do not change the response, so it can reuse a cached copy for URLs that differ only in those parameters:

```http
No-Vary-Search: params=("utm_source" "utm_campaign")
```

Browser support is still limited (Chromium-based browsers, mainly for prefetch and the HTTP cache). CDNs usually have their own settings to ignore query parameters.

## 296: How do you choose what to include in a cache key for an HTTP response?

Include everything that changes the response and nothing else. Usually that means the path, the query parameters that matter, and maybe the language, device class or a version. Leave out tracking parameters, unused cookies and headers. Every extra part multiplies the number of entries and lowers the hit ratio; every missing part risks serving the wrong response.

## 297: How do you cache data for a feed or timeline?

Feeds are personal, so caching a full rendered feed per user is often too much. Common approaches: cache each post by ID, keep a list of post IDs per user in Redis (often a sorted set by time, trimmed to a few hundred), and build the page from those. For users who follow very popular accounts, posts from those accounts are merged at read time instead of being pushed to millions of lists.

## 298: How do you cache data that is expensive to compute and different for each user, like recommendations?

Compute them in the background (on a schedule or after user activity) and store them per user, with a TTL of hours or days. Serve from that store, and fall back to generic recommendations if a user has none yet. Only active users need fresh results, so you can skip recomputing for users who have not visited for a long time.

## 299: How do you document caching behavior in a codebase?

For each cached thing, write down: the key format, TTL, who fills it, what invalidates it, and how stale it can be. Keep this next to the code (in the cache helper or a short doc), not only in someone's head. It makes stale-data bugs much faster to fix and stops new code from writing to the database without invalidating.

## 300: What questions do you ask before adding a cache to a feature?

- What problem are we solving, and do we have numbers for it?
- How often is the data read and how often does it change?
- How stale can it be, and what happens if it is wrong?
- Who writes this data, and can every write path invalidate the cache?
- What happens when the cache is empty or down?
- How will we know if the cache is working (metrics)?

# Advanced Questions (301-450)

## 301: Describe the classic race condition in cache-aside that leaves stale data in the cache.

1. Request A reads key `user:1`, misses, and reads the user from the database (old value).
2. Request B updates the user in the database and deletes `user:1` from the cache.
3. Request A, which was slow, now writes the old value into the cache.

The cache now holds the old value until the TTL ends, even though B did everything right. The window is small, because A's database read must happen before B's write and A's cache write after B's delete, but under heavy load it does happen.

## 302: How can you prevent the stale-set race in cache-aside?

Options, from simple to strong:

- Keep TTLs short, so the damage is limited.
- Delayed double delete after the write.
- Versioned writes: store a version with the value and only set it if the version is newer than what is in the cache (using a Lua script).
- Leases, where the cache gives a token on a miss and rejects the set if the key was deleted in the meantime.
- Invalidate from the database change log (CDC), so deletes happen after commit in order.

## 303: What are leases in caching, as described in Facebook's memcache paper?

On a miss, the cache gives the client a lease token. The client loads the data and sets it with that token. If the key was deleted while the client was loading, the token becomes invalid and the set is rejected, so a stale value can not be written. The cache also limits how often it hands out leases for the same key (for example once every 10 seconds), and other clients are told to wait briefly, which also prevents stampedes.

## 304: How would you implement version-checked cache writes in Redis?

Store the value with its version (for example the row's `updated_at` or a version column), and use a Lua script that only overwrites if the incoming version is newer:

```ts
const setIfNewer = `
local cur = redis.call("HGET", KEYS[1], "v")
if cur and tonumber(cur) >= tonumber(ARGV[1]) then return 0 end
redis.call("HSET", KEYS[1], "v", ARGV[1], "data", ARGV[2])
redis.call("EXPIRE", KEYS[1], ARGV[3])
return 1`;

await redis.eval(
  setIfNewer,
  1,
  `user:${u.id}`,
  u.version,
  JSON.stringify(u),
  300,
);
```

Combined with a delete on write, you also need a tombstone with the deleted version, otherwise an old value can still be set after the delete.

## 305: What is a tombstone in cache invalidation?

Instead of deleting the key, you replace it with a small marker that says "deleted at version N" and give it a short TTL. Late writes with an older version see the tombstone and are rejected. Without it, a delete leaves no trace, so a slow reader can put an old value back. Tombstones are a building block for avoiding the stale-set race.

## 306: What is change data capture (CDC), and how is it used for cache invalidation?

CDC reads the database's change log (the PostgreSQL WAL or the MySQL binlog) and turns each committed change into an event. A tool like Debezium publishes these events to Kafka, and a consumer deletes or updates the matching cache keys. Because it reads committed changes in order, it catches every write, including ones from scripts, admin tools or other services that would otherwise forget to invalidate.

## 307: What are the downsides of CDC-based invalidation?

- More infrastructure: connectors, Kafka or another broker, consumers.
- Some delay between the commit and the invalidation (usually milliseconds to seconds).
- You have to map table rows to cache keys, which is hard for caches built from joins or aggregates.
- If the CDC pipeline falls behind or stops, caches go stale, so you need monitoring and a fallback TTL.

## 308: How does the transactional outbox pattern help with cache invalidation?

In the same database transaction as the data change, you insert a row into an outbox table describing the change. A separate process reads the outbox and publishes invalidation events. Since the change and the outbox row commit together, you never have a committed change without an event, or an event for a rolled-back change. It solves the "database write succeeded but cache delete was lost" problem.

## 309: Why should you invalidate after commit and not inside the transaction?

If you delete the cache key inside the transaction, before commit, another request can miss, read the old committed value from the database, and refill the cache before your transaction commits. Then your commit lands and the cache is stale. Invalidating after the commit (or from the change log) avoids this. Many ORMs have after-commit hooks for exactly this reason.

## 310: What consistency guarantees can a cache-aside system give?

Usually eventual consistency, bounded by the TTL if invalidation fails. With careful design (version checks, leases, CDC), you can make stale reads rare and short, but a normal cache in front of a database cannot give linearizable reads, because the cache and the database are updated separately. If a read must reflect the latest committed write, read from the primary database, not the cache.

## 311: What is read-your-writes consistency, and how do you provide it with a cache?

Read-your-writes means a user always sees their own changes right after making them. With caching and replicas this can break: the user saves their profile and the next page shows the old one. Fixes: invalidate synchronously before returning the response, skip the cache for that user for a few seconds after a write (store a "recently wrote" marker in their session), or update local client state with the new value.

## 312: How do you handle cache consistency across multiple regions?

Each region usually has its own cache, close to its app servers. When data changes in one region, you have to invalidate caches in all regions. Common approaches: publish invalidation events across regions (through Kafka replication or a global pub/sub), use CDC in each region from the replicated database, or accept a bounded staleness with TTLs. Cross-region invalidation adds latency, so a user in another region might see old data for a moment.

## 313: What is the risk of invalidating before the cross-region database replication completes?

If region B gets the invalidation event before its database replica receives the change, the next read in region B misses, loads the old row from its replica, and caches it again. The fix is to trigger invalidation from each region's own replication stream (CDC on the local replica), so the cache is cleared only after the data is actually there.

## 314: What is a hot key problem in a distributed cache, and how do you solve it?

In a sharded cache, each key lives on one node. A very hot key sends all its traffic to that one node, which can max out its CPU or network while the other nodes are idle. Solutions:

- Add a local in-process cache in front for that key.
- Replicate the key under several names (`key#1` to `key#N`) and pick one at random on read.
- Read from replicas.
- Split the value into smaller parts if it is also large.

## 315: How does key replication for hot keys work, and what is the cost?

You write the same value under several keys, like `home:feed#0` to `home:feed#9`, which hash to different nodes. Readers pick a random copy, so the load spreads across nodes. The cost is more memory and more work on writes or invalidation, since all copies must be updated or deleted. It only makes sense for a few known hot keys.

## 316: What is a big key problem in Redis?

A big key is a single key with a very large value, like a 50 MB string or a hash with millions of fields. It causes slow commands that block Redis (Redis runs commands on one thread), network spikes when it is read, slow replication, and uneven memory across cluster nodes. Deleting it with `DEL` can also block. Split big values into smaller keys, use `UNLINK`, and avoid reading whole big collections at once.

## 317: How does consistent hashing help a distributed cache?

With plain `hash(key) % N`, adding or removing one node changes the node for almost every key, so the whole cache becomes useless at once. Consistent hashing places nodes and keys on a ring, and each key goes to the next node on the ring. Adding or removing a node only moves the keys next to it, about 1/N of them. Virtual nodes (many points per server) keep the load even.

## 318: How is Redis Cluster's hash slot model different from consistent hashing?

Redis Cluster uses a fixed number of slots (16,384). Each key maps to a slot with `CRC16(key) mod 16384`, and each node owns a set of slots. To rebalance, you move whole slots between nodes. This gives the same benefit as consistent hashing (only moved slots are affected) but makes ownership explicit and easy to manage, and clients cache the slot map.

## 319: What happens to clients during a Redis Cluster resharding?

While a slot moves, keys that already moved are on the new node. If a client asks the old node for such a key, it gets an `ASK` redirect for that one command. When the slot is fully moved, clients get a `MOVED` error, update their slot map, and send future commands to the new node. Cluster-aware clients handle this automatically, but you may see small latency spikes.

## 320: What is Redis client-side caching (tracking)?

Since Redis 6, a client can turn on tracking with `CLIENT TRACKING ON`. Redis then remembers which keys the client has read, and when any of them change, it sends the client an invalidation message. The client keeps those keys in local memory and drops them when told. This gives you a near cache with server-driven invalidation, without building your own pub/sub layer.

## 321: What is broadcasting mode in Redis client tracking?

In the default mode, Redis remembers which keys each client read, which uses memory on the server. In broadcasting mode (`CLIENT TRACKING ON BCAST PREFIX product:`), Redis does not remember keys per client; it sends invalidations for every changed key that matches the prefixes the client subscribed to. It uses less server memory but sends more messages to clients.

## 322: What is a near cache?

A near cache is a local cache on the client side of a distributed cache, holding copies of recently read entries. Reads are served locally when possible, avoiding the network. The hard part is keeping it consistent; good near caches get invalidations from the server (like Redis tracking or Hazelcast near caches). Without invalidations it is just a local cache with a TTL.

## 323: How do you prevent cache penetration with a Bloom filter?

A Bloom filter is a small structure that can say "definitely not present" or "maybe present" for a key. Add every valid ID to the filter. On a request, check the filter first; if it says not present, return 404 without touching the cache or database. False positives are possible (it may say "maybe" for a missing ID), but there are no false negatives. Redis Stack and Redis 8 include Bloom filter commands (`BF.ADD`, `BF.EXISTS`).

## 324: What are the limits of using a Bloom filter for penetration protection?

- Standard Bloom filters cannot remove items, so deleted IDs stay "maybe present" (a Cuckoo filter can delete).
- You must add every new ID to the filter when it is created, or valid IDs will be rejected.
- It must be rebuilt if it gets out of sync or too full, because its false positive rate grows as you add items.
- It only helps when the set of valid keys is known and checkable, like numeric IDs.

## 325: How do you size a Bloom filter?

You pick the expected number of items (n) and the false positive rate you accept (p). The number of bits is about `m = -n * ln(p) / (ln 2)^2` and the number of hash functions is about `k = (m / n) * ln 2`. For 10 million items with 1% false positives, that is about 96 million bits (12 MB) and 7 hash functions. Redis `BF.RESERVE` takes the error rate and capacity and does the math for you.

## 326: What is cache pollution?

Cache pollution is when the cache fills with items that will not be read again, pushing out useful items. Typical causes are crawlers walking every page, batch jobs or exports reading through many records, or caching every search query. The hit ratio drops for normal users. Fixes include not caching for certain clients or jobs, admission policies, and LFU-like eviction.

## 327: What is an admission policy?

An admission policy decides whether a new item should even enter the cache, not just what to evict. For example, only cache an item on its second request within some time, or only admit it if it is likely to be more popular than the item it would replace. It protects the cache from one-time reads. TinyLFU is a well-known admission policy.

## 328: What is TinyLFU and W-TinyLFU?

TinyLFU keeps an approximate count of how often keys are accessed (in a small Count-Min Sketch that decays over time). When a new item would evict an old one, it compares their counts and only admits the new item if it is more popular. W-TinyLFU adds a small LRU "window" in front, so new items get a chance to build up frequency. It is used by Caffeine (Java) and Ristretto (Go) and gives near-optimal hit ratios for many workloads.

## 329: What is a Count-Min Sketch?

It is a compact structure for estimating how often items appear in a stream. It uses a few rows of counters and a hash function per row; to count an item, you increment one counter in each row, and to read, you take the minimum across rows. It can overestimate but never underestimate. Caches use it to track key frequency with very little memory.

## 330: What is the ARC eviction algorithm?

ARC (Adaptive Replacement Cache) keeps two lists: one for items seen once recently and one for items seen at least twice. It also keeps "ghost" lists of keys recently evicted from each. When a ghost hit happens, it shifts more space to the list that would have kept that item. This lets it adapt between recency and frequency automatically. ZFS uses a version of ARC.

## 331: What is the CLOCK algorithm?

CLOCK is a cheap approximation of LRU. Items sit in a circle, each with a "used" bit. On access, the bit is set. When eviction is needed, a pointer moves around the circle: if an item's bit is set, it clears it and moves on; if not, it evicts that item. It avoids moving items in a linked list on every read, which makes it faster and easier to use with many threads.

## 332: What is SLRU (segmented LRU)?

SLRU splits the cache into a probation segment and a protected segment. New items go into probation. If they are read again, they move to protected. Eviction happens from probation first. This means items read only once never push out items that are read many times, which gives some scan resistance at little cost. Memcached and W-TinyLFU use ideas like this.

## 333: What is scan resistance?

A cache is scan-resistant if a large one-time scan (reading many items once) does not throw out the frequently used items. Plain LRU is not scan-resistant: a scan of 1 million items will push out everything. Algorithms like SLRU, 2Q, ARC, LFU and W-TinyLFU are designed to resist scans. It matters for databases, file systems and app caches that serve both users and batch jobs.

## 334: What is Belady's optimal algorithm, and why does it matter?

Belady's algorithm evicts the item that will be needed furthest in the future. It gives the best possible hit ratio, but it needs to know the future, so it cannot be used in practice. It is used as a benchmark: you replay a real access trace and compare your policy's hit ratio with the optimal one to see how much room there is to improve.

## 335: How do you evaluate eviction policies for your workload?

Record a trace of cache keys accessed in production (with sampling if needed). Replay it against simulated caches of different sizes and policies, and plot hit ratio against cache size. This shows which policy works best for your traffic and how much a bigger cache would help. Tools for this exist in projects like Caffeine's simulator.

## 336: What is a miss ratio curve?

A miss ratio curve shows the miss ratio for each possible cache size. It tells you how much benefit you get from adding memory. Often the curve drops steeply at first and then flattens, meaning beyond a point, more memory barely helps. It is a useful tool for sizing caches and deciding whether to pay for a larger instance.

## 337: How do you calculate the average latency with a cache?

```text
avg = hit_ratio * hit_latency + (1 - hit_ratio) * miss_latency
```

With a 95% hit ratio, 1 ms hits and 50 ms misses: `0.95 * 1 + 0.05 * 50 = 3.45 ms`. Going from 95% to 99% gives `0.99 + 0.5 = 1.49 ms`, more than twice as fast. This shows why small gains in hit ratio matter a lot when misses are expensive. Note that averages hide the tail: p99 latency is still the miss latency.

## 338: Why can a cache make tail latency worse even when average latency improves?

Most requests get fast hits, but misses still take the full time, plus the cache lookup, plus waiting behind locks during stampedes. If misses are rare but slow, the average looks great while p99 or p99.9 is bad. Also, when a cache is warm, the database may be scaled down, so misses during a cold period are even slower. Watch percentiles, not just averages.

## 339: How does caching affect database capacity planning?

If the cache handles 95% of reads, the database only needs to handle 5% of normal read traffic. Teams then size the database for that. But if the cache fails or goes cold, the database suddenly gets 20 times the load and falls over. Plan for what happens on a cold cache: either size the database to survive it for a while, or have ways to protect it (rate limiting, slow warm-up, serving stale).

## 340: What is metastable failure, and how can caching cause it?

A metastable failure is when a system enters a bad state and stays there even after the trigger is gone. Example: a brief cache outage sends load to the database, the database slows down, requests time out, retries add more load, and the cache never gets refilled because the loads keep failing. The system stays down even after the cache is back. Fixes are retry budgets, load shedding, serving stale, and refilling the cache in a controlled way.

## 341: How do you design a cache to recover safely from a full flush?

- Warm the most popular keys before sending full traffic.
- Use single-flight and locks so each key is loaded once.
- Rate limit the loads to the database.
- Serve stale or default data where possible while warming.
- Bring traffic back gradually if you control it (for example with a load balancer weight).

## 342: What is cache poisoning in HTTP caches?

Web cache poisoning is an attack where the attacker gets a malicious response stored in a shared cache under a normal URL, so other users receive it. It usually works through unkeyed inputs: headers like `X-Forwarded-Host` that change the response (for example a script URL) but are not part of the cache key. The attacker sends a request with a bad header, the response is cached, and everyone else gets it.

## 343: How do you prevent web cache poisoning?

- Make sure every input that changes the response is part of the cache key, or is ignored by the app.
- Do not trust headers like `X-Forwarded-Host` unless they come from your own proxy.
- Strip unknown headers at the CDN.
- Do not cache responses that reflect request headers.
- Keep framework and CDN config tested for these cases.

## 344: What is web cache deception?

Web cache deception tricks a cache into storing a private page as if it were a static file. For example, the attacker sends a victim a link to `/account/profile.css`. The app ignores the `.css` part and returns the victim's profile page; the CDN sees `.css` and caches it as public. The attacker then requests the same URL and gets the victim's data from the cache.

## 345: How do you prevent web cache deception?

- Send `Cache-Control: private` or `no-store` on all personal pages, and configure the CDN to respect origin headers instead of caching by file extension.
- Make the app return 404 for paths it does not really handle, instead of matching loose routes.
- Check that `Content-Type` matches the extension before caching.
- Do not cache responses to requests with a session cookie.

## 346: How can a cache leak data between users?

- Cache keys that miss the user or tenant ID.
- Shared caches storing personal responses because `private` was missing.
- A module-level variable in a server process holding per-user data.
- A CDN ignoring `Set-Cookie` and caching it.
- Error pages or redirects containing personal data being cached.

These bugs are serious because they cause data breaches, not just stale data. Review cache keys and headers for any endpoint with user data.

## 347: How can attackers use caching for denial of service?

- Cache busting: sending requests with random query strings so every request misses and hits the origin.
- Filling the cache with junk keys to push out useful data.
- Poisoning the cache with error responses so normal users get errors (cache poisoned DoS).
- Hitting endpoints that create big cache entries.

Normalize keys, limit allowed parameters, rate limit by client, and do not cache errors for long.

## 348: How can cache timing be a security issue?

A response from cache is faster than one from the origin. An attacker can measure response times to learn if something is cached, which can reveal whether another user recently visited a page or whether a record exists. Browsers partition their HTTP cache by top-level site for this reason, so one site cannot probe what you visited on another site.

## 349: What is HTTP cache partitioning in browsers?

Modern browsers key their HTTP cache not only by URL, but also by the top-level site (and sometimes the frame's site). A font from a shared CDN loaded on site A is not reused on site B. This stops cross-site tracking and timing attacks, but it means the old idea that "a popular CDN library is already cached from other sites" no longer helps.

## 350: How should a cache handle secrets and sensitive data?

Ideally do not cache them. If you must (for example cached session data with tokens), use a cache with authentication and TLS, restrict network access, use short TTLs, and consider encrypting the values. Remember that caches may write to disk (Redis persistence, swap), may be shown in debugging tools, and are often less protected than the main database.

## 351: Should Redis traffic be encrypted?

Inside a private network it was often left plain, but today TLS is recommended, especially in cloud environments and for any data with personal information. Redis supports TLS natively since version 6, and managed services offer it. TLS adds some CPU and latency, so measure, but for most apps the cost is small compared to the risk.

## 352: Design a caching strategy for a product catalog with 10 million products.

- Product details: cache-aside in Redis, key `product:<id>:v<schemaVersion>`, TTL around an hour with jitter, invalidated on product updates through events or CDC.
- Category and search pages: cache IDs only with short TTLs, load products by ID with `MGET`.
- Hot products: local LRU cache with a few seconds TTL in each app server.
- Public product pages: CDN with `s-maxage`, `stale-while-revalidate`, and purge by `product-<id>` tag.
- Prices and stock: either not cached, or cached very briefly, and checked again at checkout.

## 353: Design caching for a checkout flow.

Checkout must be correct, so cache very little on the write path. You can cache product info and shipping options for display, but at the moment of placing an order, read prices, stock and promotions from the source, inside the transaction. Cache the user's cart in Redis for speed, but treat it as primary data with persistence or back it up in the database. Never cache payment results under shared keys.

## 354: Design a cache for a social media profile page that some users view millions of times.

Use a multi-level cache: CDN for the public part of the page, Redis for profile data, and a local in-process cache for the hottest profiles with a short TTL. Watch for hot keys on a single Redis node and spread them with replicas or key copies. Use stale-while-revalidate so expiry of a celebrity's profile never causes a stampede. Counters like followers can be cached and updated asynchronously, since exact numbers are not needed in real time.

## 355: Design caching for an API that returns exchange rates updated every minute.

Fetch rates once a minute in a background job and store them in Redis (and in local memory on each server). The API reads only from the cache, never from the provider directly. Set `Cache-Control: public, max-age=30, stale-if-error=3600` so CDNs and clients can cache too. If the provider fails, keep serving the last rates and show their timestamp. This gives constant load on the provider regardless of traffic.

## 356: Design a caching layer for a multi-tenant SaaS with very different tenant sizes.

Include the tenant ID in all keys. Give each tenant a memory budget or use separate cache instances for the largest tenants, so one large tenant does not evict everyone else's data. Monitor hit ratio per tenant. Handle tenant-wide invalidation with a per-tenant version number in the keys. For data shared by all tenants (like plans or countries), use a separate global namespace.

## 357: How would you cache results of a machine learning model or LLM call?

Model calls are slow and expensive, so caching identical requests helps. Use a key built from a hash of the normalized input plus the model name and version and the parameters that affect output. Cache only deterministic or acceptable outputs. Some systems also use semantic caching, which matches similar (not identical) inputs using embeddings, but it can return answers for questions that only look similar, so set a strict similarity threshold.

## 358: What is semantic caching, and what are its risks?

Semantic caching stores responses keyed by an embedding of the request and returns a cached answer when a new request is close enough in meaning. It raises the hit ratio for things like support questions phrased differently. The risks: two questions that look similar but need different answers ("cancel my order" vs "do not cancel my order"), leaking one user's answer to another, and stale answers. Use it only for non-personal content with a high threshold.

## 359: How do you cache in an event-sourced system?

The current state of an entity is built by replaying its events. Rebuilding on every read is expensive, so you cache the state (a snapshot) at a certain event number. To read, load the snapshot and apply only newer events. Projections (read models) also act as caches built from events. Since events are immutable, cached state for a given version never becomes wrong; it just gets older.

## 360: How does immutability make caching easier?

If data never changes after it is created, any cached copy is always correct, so you can cache it forever with no invalidation. You can design for this: content-addressed URLs (hash in the name), versioned API resources (`/orders/42/v/3`), and append-only event logs. Changes become new versions with new keys. This is the idea behind hashed static assets and is very powerful for backend data too.

## 361: What is content-addressable storage, and how does it relate to caching?

In content-addressable storage, an item's key is the hash of its content. The same content always gets the same key, and different content always gets a different key. Caching this is trivial: entries never change and can be shared and kept forever. Git objects, Docker image layers, and build caches like those in Bazel or Turborepo work this way.

## 362: How do build caches like Turborepo or Bazel work?

They compute a hash of everything that affects a task's output: source files, dependencies, configuration, environment variables and the command itself. If the hash was seen before, they restore the output from a local or remote cache instead of running the task. The hard part is making sure the hash includes every input; if something is missed, you get wrong cached results.

## 363: How do you cache Docker image layers in CI?

Each Dockerfile instruction makes a layer, and a layer can be reused if the instruction and everything before it are unchanged. Put rarely changing steps first (installing dependencies) and often changing ones last (copying source code). In CI, use a remote cache like a registry cache or the GitHub Actions cache with BuildKit:

```bash
docker buildx build \
  --cache-from type=gha --cache-to type=gha,mode=max -t app .
```

## 364: How do you cache dependencies in CI pipelines?

Cache the package manager's download store, keyed by a hash of the lockfile, so the cache changes only when dependencies change:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 22
    cache: npm
```

This uses `package-lock.json` as the key. Cache the global store, not `node_modules`, since `npm ci` deletes `node_modules` anyway.

## 365: What are the dangers of a CI cache?

If the cache key does not include everything that affects the result, you can restore outdated outputs and get builds that pass in CI but fail elsewhere. Caches can also be poisoned: if an untrusted pull request can write to a cache that trusted builds read, it can inject malicious files. GitHub Actions limits cache access between branches for this reason. Scope caches carefully.

## 366: How does Redis active expiration work, and can it cause latency?

Redis runs a background cycle many times per second that samples keys with a TTL and deletes the expired ones. If many of the sampled keys are expired, it keeps going, within a time budget. When a huge number of keys expire at the same moment, this cycle can use more CPU and add latency. TTL jitter avoids that pattern. Redis also deletes expired keys lazily when they are accessed.

## 367: Can an expired key still use memory in Redis?

Yes, until either the active expiry cycle or a read removes it. If you have many keys that expire and are never read again, and the active cycle is behind, memory may stay higher than expected for a while. Eviction under `maxmemory` also considers them. In normal setups this is not a problem, but it explains why memory does not drop exactly when keys expire.

## 368: How do Redis replicas handle expired keys?

Replicas do not expire keys on their own; they wait for the primary to send a `DEL` when the key expires. But to avoid returning stale data, a replica answers reads of a logically expired key as if it did not exist. Clock differences between machines can affect this slightly. This is one more reason why reading from replicas can behave a bit differently from reading from the primary.

## 369: What is Redis memory fragmentation, and how do you deal with it?

Fragmentation is when the memory allocated by the operating system is bigger than the memory Redis actually uses for data, because of gaps left by deleted or resized values. You see it as a `mem_fragmentation_ratio` well above 1 in `INFO memory`. Redis can defragment in the background with `activedefrag yes` (when built with jemalloc). Workloads with very mixed value sizes and lots of churn fragment more.

## 370: Why does Redis need extra memory during a snapshot (fork)?

When Redis saves an RDB snapshot or rewrites the AOF, it forks a child process. The child shares memory pages with the parent through copy-on-write. Every page the parent changes while the child is working gets copied, so with heavy writes, memory use can nearly double. If the machine has no room, the fork fails or the system starts swapping. Leave headroom or turn off persistence for pure caches.

## 371: How does Redis I/O threading affect cache performance?

Redis runs commands on one main thread, but can use extra threads to read and write network data (`io-threads`). For a cache with many clients and small commands, network I/O is often the bottleneck, so I/O threads can raise throughput noticeably. Redis 8 improved this further. Command execution itself is still single-threaded, so slow commands still block everything.

## 372: Why is a single slow Redis command dangerous for a cache?

Because Redis runs commands one at a time on the main thread, a command that takes 500 ms (like `KEYS *`, `HGETALL` on a huge hash, `SMEMBERS` on a big set, or a long Lua script) blocks every other client for that time. All cache reads time out at once, and the app falls back to the database. Use `SLOWLOG` to find these, and avoid O(N) commands on large collections.

## 373: How do you implement refresh-ahead safely for many keys?

Track when each hot key will expire and refresh it in the background a bit before, only if it was read recently (so you do not refresh cold keys forever). Use a queue or a scheduler with a concurrency limit, so refreshes do not overload the source. Use single-flight so a key is refreshed once even if many servers notice. Probabilistic early refresh on read is a simpler alternative that needs no scheduler.

## 374: When would you never expire a cache entry and instead update it in place?

When the data is small, very hot, and you have a reliable update path, like the home page config, a list of active feature flags, or a leaderboard. A background job or change event writes the new value; readers always hit. Without expiry there is no stampede. You still need monitoring that the updater is running, because if it stops, the data stays old forever. A long safety TTL is a good backup.

## 375: How do you handle a cache stampede across many servers?

Single-flight only works inside one process. Across servers you need:

- A distributed lock per key (Redis `SET NX` with a short TTL).
- Stale-while-revalidate, so most requests get the old value while one refreshes.
- Probabilistic early refresh.
- Refresh-ahead from a background worker.

The best setups avoid the "miss with nothing to serve" situation entirely by always having a stale value available.

## 376: What are the problems with distributed locks for stampede protection?

If the lock holder crashes, others wait until the lock TTL ends. If the load takes longer than the TTL, two holders can run at once. Waiting requests add latency and use connections. The lock itself is a hot key. Fencing tokens and Redlock are about correctness for real mutual exclusion; for stampede protection, an occasional double load is fine, so a simple `SET NX EX` with a stale fallback is usually enough.

## 377: What is Redlock, and do you need it for caching?

Redlock is an algorithm for distributed locks across several independent Redis nodes, taking the lock on a majority. It aims to keep the lock working if one Redis node fails. It has been criticized because it relies on timing assumptions and cannot give strict safety without fencing tokens. For cache stampede protection you do not need it; a lock on a single Redis node is fine, since the worst case is some duplicate work.

## 378: How do you cache aggregated data that depends on many rows?

Aggregates (totals, counts, averages) are hard to invalidate because any row change can affect them. Options:

- Recompute on a schedule and accept staleness.
- Update the aggregate incrementally on each change (`INCRBY`, or update a summary table in the same transaction).
- Use a materialized view refreshed periodically.
- Use a stream processor that keeps the aggregate up to date from change events.

## 379: How would you cache a "count of unread notifications" per user?

Keep the count in Redis and update it with `INCR` when a notification is created and `DECR` or reset when read. Periodically, or on a cache miss, recompute it from the database to fix drift. Expose it with a short TTL or push updates to the client. Small errors are acceptable for a badge counter, but make sure the value never goes negative and that "mark all as read" resets it.

## 380: How do you keep a cached counter and the database in sync?

They will drift because of failures between the two writes. Ways to handle it:

- Treat one as the source and rebuild the other from it regularly.
- Write to the database and update the counter from CDC events, which are ordered and retried.
- Use the counter as the source for display only and the database as the truth for business logic.

Decide clearly which one is the source of truth.

## 381: What problems can clock skew cause in caching?

`Expires` headers depend on the client clock matching the server. Soft TTLs stored as timestamps depend on all app servers having similar clocks. Probabilistic refresh and lock TTLs can behave oddly when clocks jump. Prefer relative durations (`max-age`, Redis `EX`) where the time is measured by one system, and run NTP everywhere.

## 382: How does HTTP/2 or HTTP/3 change caching?

The caching rules themselves (RFC 9111) are the same for all HTTP versions. What changed is that requests are cheap to multiplex, so tricks like bundling everything into one file to save requests matter less, and finer-grained files cache better. HTTP/2 Server Push, which was supposed to push cached assets, was removed from browsers; `103 Early Hints` with `Link: rel=preload` replaced it.

## 383: How does a CDN handle a request for an object that is being fetched from the origin?

Good CDNs use request collapsing: if many requests for the same uncached object arrive at once, only one goes to the origin and the rest wait for that response. This only works if the response is cacheable. For responses marked `private` or `no-store`, the CDN cannot share them, so collapsing can make other requests wait for nothing; some CDNs then remember the object as uncacheable for a short time (hit-for-pass).

## 384: What is hit-for-pass in Varnish?

When Varnish fetches an object and finds it is not cacheable (for example it has `Set-Cookie` or `private`), it creates a short-lived "hit-for-pass" marker for that URL. Later requests for the same URL skip request collapsing and go straight to the backend in parallel. Without it, they would queue behind each other waiting for a response that can never be shared.

## 385: What is Edge Side Includes (ESI)?

ESI is a markup language that lets a CDN or proxy build a page from fragments, each with its own caching rules:

```html
<html>
  <body>
    <esi:include src="/fragments/header" />
    <main>Cached article content</main>
    <esi:include src="/fragments/user-menu" />
  </body>
</html>
```

The main page can be cached for hours while the user menu is fetched per request. Varnish, Fastly and Akamai support it. Today many teams use edge functions or client-side loading for the same goal.

## 386: How do edge functions change caching strategies?

Edge functions (Cloudflare Workers, Fastly Compute, CloudFront Functions, Vercel and Netlify edge functions) run code at the CDN. You can build custom cache keys, combine cached fragments with personal data, rewrite requests to improve hit ratio, and use edge key-value stores. This lets you cache more of a personalized page, but adds another place where cache bugs can live.

## 387: What is the Cache API in Cloudflare Workers?

Workers have access to a `caches.default` object, similar to the browser Cache API, that stores responses in the local data center's cache:

```js
export default {
  async fetch(request, env, ctx) {
    const cache = caches.default;
    let response = await cache.match(request);
    if (!response) {
      response = await fetch(request);
      response = new Response(response.body, response);
      response.headers.set("Cache-Control", "s-maxage=60");
      ctx.waitUntil(cache.put(request, response.clone()));
    }
    return response;
  },
};
```

It is per data center, not global.

## 388: How do you measure the effect of a CDN on user latency?

Use real user monitoring (RUM) to collect Time to First Byte and other timings from real browsers, broken down by region and by cache status (send the cache status from the CDN to the browser in a header and log it). Compare hits vs misses and regions with and without good coverage. Synthetic tests from many locations help too, but RUM shows what users actually get.

## 389: How do you handle cache invalidation for a CDN with hundreds of edge locations?

Purges are sent to all locations, but they are not instant; they can take from milliseconds to tens of seconds depending on the CDN. Design for this: use versioned URLs where possible so you never need to purge, purge by tags rather than many URLs, and avoid flows that depend on the purge being complete before the next user request. Check your CDN's documented purge time and limits.

## 390: Why can purging everything at once on a CDN cause an outage?

After a full purge, every edge location misses on everything at once and sends requests to the origin. The origin may get many times its normal traffic and fall over. Use soft purges, purge only what changed, keep an origin shield, and make sure the origin can survive a cold CDN, or purge in stages.

## 391: How do you cache personalized API responses at the edge safely?

Make the user identity part of the cache key in a controlled way, usually by validating a token at the edge and adding the user ID (or a coarse group like plan or role) to the key. Only do this for responses that are really the same for everyone in that group. Never key on a raw cookie or header you have not validated. Often caching by group (for example "premium users in Germany") gives most of the benefit with less risk.

## 392: How do you handle cache invalidation in a system with many read models and caches?

Keep a clear map of which caches depend on which data. Publish one change event per data change, and let each cache owner subscribe and invalidate their own keys. Make invalidation idempotent and safe to repeat. Keep TTLs as a safety net. Monitor the delay between a change and its invalidation. Without this structure, every new feature adds hidden dependencies and stale data bugs grow.

## 393: How do you cache data that has dependencies, like a page built from many objects?

Track dependencies: when you build a cached page, record which objects it used (for example as tags `product:42`, `user:7`). When any of those objects changes, invalidate every entry with that tag. This is what CDN surrogate keys and framework tag-based revalidation do. It is more precise than short TTLs, but you must make sure every dependency is recorded, or invalidation will miss cases.

## 394: What is the dependency explosion problem with tag invalidation?

A popular object, like a site-wide category or a shared author, can be a dependency of millions of cached entries. Changing it invalidates a huge part of the cache at once, which is close to a full purge and can overload the origin. Fixes: do not tag on objects that change often and affect everything, render such shared parts separately (fragments), or accept staleness for them.

## 395: How do you make cache invalidation idempotent and retryable?

Invalidation should be "make sure this key is gone" or "set version to at least N", which can be done many times without harm. Deletes are naturally idempotent. Put invalidation messages in a durable queue so they are retried on failure. Avoid invalidation actions like "decrement" that cause errors if repeated. Use version checks so an old, delayed message cannot overwrite newer data.

## 396: How would you cache data in a GraphQL server with field-level TTLs?

Each type or field gets a cache hint, for example product name 1 hour, stock 10 seconds, and the user's cart not cacheable. The server computes the response's overall cache policy as the smallest TTL among all fields used, and marks it private if any field is private. Apollo Server does this with `@cacheControl` directives and a response cache plugin. Mixing very fresh and very stale fields in one query lowers the whole response's TTL.

## 397: How do normalized client caches work, like Apollo Client's?

They split responses into individual objects keyed by type and ID (like `Product:42`) and store them in a flat map. Queries point to these objects. When a mutation returns an updated `Product:42`, every query showing that product updates automatically. Problems come with lists (adding an item to a list needs manual cache updates), and with objects that lack IDs.

## 398: What is the hardest part of invalidation in client-side data caches?

Knowing which queries a change affects. Updating one object by ID is easy, but a new item may belong in several lists with different filters and sort orders, and a deletion must be removed from all of them. Libraries offer refetching (simple but slower) or manual cache updates (fast but error-prone). Many teams refetch affected queries after mutations, using tags or query keys to target them.

## 399: How do you cache with optimistic updates on the client?

You update the client cache right away as if the server request succeeded, so the UI responds instantly. When the server responds, you replace the optimistic value with the real one, or roll back if the request failed. You need to handle concurrent changes and make sure the rollback restores the right state. TanStack Query and Apollo both support this pattern.

## 400: How do you avoid thundering herds when clients refetch at the same time?

If every client polls on the same schedule (on the minute) or refetches when the tab regains focus after a broadcast, the backend sees a spike. Add random jitter to polling intervals, use exponential backoff on errors, rely on HTTP caching so many refetches are cheap `304` responses, and consider pushing updates instead of polling.

## 401: How would you debug a low cache hit ratio?

- Check key cardinality: are keys too specific (timestamps, random IDs, full query strings)?
- Check TTLs: are items expiring before reuse?
- Check evictions: is the cache too small?
- Check access pattern: is most traffic for long-tail items read once?
- Check invalidation: is something deleting keys too often?
- Compare key formats between the reader and the writer.

Log a sample of misses with their keys to see patterns.

## 402: What is cache key cardinality, and why does it matter?

Cardinality is the number of distinct keys. If keys include things that vary a lot (exact timestamps, session IDs, full user agents), each key is rarely reused, so the hit ratio is low and memory is wasted. Reducing cardinality, by rounding, normalizing, or removing parts that do not change the result, often improves the hit ratio more than adding memory.

## 403: How do you cache time-based queries like "events in the last hour"?

The time window changes every second, so a key that includes the exact time never repeats. Round the time to buckets (for example the current minute) so all requests in that minute share a key. You can also cache per-bucket results (each minute's events) and combine the last 60 buckets on read; old buckets never change, so they can be cached for long.

## 404: How does caching interact with database transactions isolation?

The cache is outside the database's transaction, so it does not respect isolation levels. A value read from the cache may be from before or after a transaction you are in. Do not mix cached reads into logic that depends on transactional consistency, like checking a balance before a transfer. Read from the database within the transaction for those checks, and use the cache only for display.

## 405: How would you cache a permission check that is called thousands of times per request?

Cache at several levels: per request (the same check repeated in one request is computed once), in local memory with a short TTL for the user's role and permission set, and in Redis for computed permission sets. Invalidate when roles or memberships change, using events. For relationship-based systems (like Zanzibar-style authorization), use a consistency token so a check after a change does not use an older cached answer.

## 406: What is a consistency token (zookie) in authorization caching?

In Google Zanzibar and systems based on it (SpiceDB, OpenFGA), each change returns a token representing a point in time. When the client checks a permission, it can pass the token, meaning "answer as of at least this time". The server can use cached results that are newer than that point and must compute fresh results otherwise. This lets heavy caching work without the "new enemy" problem of stale permissions.

## 407: What is the "new enemy" problem?

A user removes someone from a document and then adds secret content. If the permission check for the removed person uses a stale cached answer from before the removal, they can see the secret content. The order of the two changes is broken by caching. Consistency tokens or invalidating permissions synchronously on removal prevent this.

## 408: How do you decide where in the stack a cache belongs?

As close to the user as possible while still being correct. Public, shared data can be cached at the CDN. Data shared across users but needing control goes in Redis. Very hot, rarely changing data can also go in local memory. Personal data is cached in the browser or in a per-user key. Highly consistent data is not cached at all. Caching at the outer layer saves the most work but is the hardest to invalidate.

## 409: What is the cost of a cache in terms of system complexity?

You add a new component to run, monitor and secure; new failure modes (stale data, stampedes, cold starts, leaks between users); invalidation code on every write path; and harder debugging, since the same request can behave differently depending on cache state. These costs are real, so a cache should be added for a measured reason and with a clear owner, not as a default.

## 410: How do you run load tests that include caching behavior?

Use realistic key distributions (some hot keys, a long tail), not the same request repeated, or you will get an unrealistic 100% hit ratio. Test with a cold cache as well as a warm one. Include writes so invalidation happens during the test. Test what happens when the cache is slow or down. Watch database load during cache misses, not just response times.

## 411: How do you model a realistic key distribution in a load test?

Real traffic often follows a Zipf-like distribution, where a few items get most requests and many items get few. Generate keys with a Zipf distribution using the size of your real data set, or replay sampled production logs. Uniformly random keys underestimate the hit ratio, and a single repeated key overestimates it.

## 412: What is a cache-aside implementation that supports batch loading?

When a page needs many objects, load them with one `MGET`, find which ones missed, load all the missing ones with one database query, and write them back with a pipeline:

```ts
async function getProducts(ids: string[]) {
  const keys = ids.map((id) => `product:${id}`);
  const cached = await redis.mget(keys);
  const missing = ids.filter((_, i) => cached[i] === null);

  const loaded = missing.length ? await db.products.findMany(missing) : [];
  const p = redis.pipeline();
  for (const prod of loaded)
    p.set(`product:${prod.id}`, JSON.stringify(prod), "EX", 300);
  await p.exec();

  const byId = new Map(loaded.map((x) => [x.id, x]));
  return ids.map((id, i) =>
    cached[i] ? JSON.parse(cached[i]!) : (byId.get(id) ?? null),
  );
}
```

## 413: How do you handle MGET across Redis Cluster slots?

`MGET` only works when all keys are in the same hash slot. With keys spread over slots, you either use hash tags to group keys (if it makes sense), or split the request by slot and send one `MGET` per node in parallel. ioredis Cluster does not split cross-slot `MGET` for you, and its pipelines also need all keys on the same node. A simple option is to send individual `GET`s in parallel with `Promise.all`, which ioredis routes to the right nodes; for the best speed, group keys by slot and send one `MGET` per group.

## 414: How would you migrate from one cache cluster to another without downtime?

- Write to both caches (dual write) or just invalidate in both.
- Read from the new cache; on a miss, read from the old cache, then the database, and fill the new cache.
- After the new cache is warm (hit ratio stable), stop reading from the old one.
- Remove dual writes and turn off the old cluster.

This avoids a cold cache and a spike on the database.

## 415: How do you change the TTL or format of many existing cache keys safely?

Do not try to rewrite millions of keys in place. Introduce a new key version for the new format, deploy code that reads and writes the new version, and let the old keys expire. If you need to warm the new keys, do it gradually. For TTL changes alone, new writes get the new TTL, and old keys will expire under the old one, which is usually fine.

## 416: How do you cache in a system where the source data is in several databases?

Cache the composed result if it is read often, but then invalidation must react to changes in all sources. A common approach is that each source publishes change events, and a single component builds the composed view and updates the cache (or a read model). Without that, it is easy to forget one source and serve inconsistent data.

## 417: How does a CDN decide what to evict when its cache is full?

CDNs have limited storage per location and use their own eviction, usually LRU-like with tiers between memory and SSD. Rarely requested objects get evicted even if their `max-age` is long, so a long TTL does not guarantee the object stays cached. That is why long-tail content often has low edge hit ratios, and why origin shields and tiered caching help.

## 418: What is the difference between max-age and how long an object actually stays in a cache?

`max-age` is the maximum time the response may be considered fresh. It is not a promise that the cache keeps it that long. Caches can evict objects at any time because of space, restarts or policy. So you should treat `max-age` as an upper bound of freshness, and design the origin to handle requests even for objects that "should" be cached.

## 419: How do you handle conditional requests at the CDN to reduce origin load?

When a cached object becomes stale, the CDN sends a conditional request to the origin with `If-None-Match` or `If-Modified-Since`. If your origin answers `304` quickly without building the full response, revalidation is cheap. So make ETags or `Last-Modified` cheap to compute, and support conditional requests properly, especially for large objects.

## 420: How do Range requests interact with caching?

For large files like video, clients request byte ranges (`Range: bytes=0-1048575`). Caches may store partial content and combine ranges, but that requires strong validators (strong ETag or `Last-Modified`). Many CDNs fetch whole files or fixed-size chunks from the origin and serve ranges from them. Make sure the origin returns correct `206` responses and stable validators, or caches may mix pieces from different versions.

## 421: What is the risk of caching redirects?

`301` and `308` responses are cacheable by default, and browsers may keep them for a very long time. If you set a permanent redirect by mistake, users may keep being redirected even after you remove it, and you cannot clear their browser cache. Use `302` or `307` while testing, or set an explicit `Cache-Control` on permanent redirects.

## 422: How do you cache CORS preflight responses?

The `Access-Control-Max-Age` header tells the browser how long to cache the result of an `OPTIONS` preflight request, so it does not send one before every real request:

```http
Access-Control-Max-Age: 7200
```

Browsers cap this (Chromium at 2 hours, Firefox at 24 hours). Also, if your API response depends on the `Origin` header, send `Vary: Origin` so caches do not give one origin's CORS headers to another.

## 423: Why is Vary: Origin important for CORS responses?

If the server returns `Access-Control-Allow-Origin` with the requesting origin (not `*`), the response is different for each origin. Without `Vary: Origin`, a CDN or browser may serve a response with `Access-Control-Allow-Origin: https://a.com` to a request from `https://b.com`, which the browser then blocks. Adding `Vary: Origin` makes caches keep a separate copy per origin.

## 424: How do you cache HTML in a way that supports instant rollback of a bad deploy?

Keep hashed assets for all recent versions. Serve `index.html` with `no-cache` or a short TTL, so a rollback that switches the HTML back to the previous version is picked up on the next load. At the CDN, purge the HTML after the rollback. Avoid long-lived HTML caching, since it would keep users on the broken version.

## 425: How does caching interact with A/B testing?

If the page varies by experiment group and is cached by URL only, everyone gets the variant of whoever filled the cache. Options: assign the group at the edge and add it to the cache key (a few variants per URL), keep the HTML the same and switch variants on the client, or bypass the cache for experiment pages. Avoid putting the full cookie in the cache key.

## 426: How do you cache in a mobile app talking to your API?

Mobile HTTP clients (like URLSession and OkHttp) support standard HTTP caching, so your `Cache-Control` and `ETag` headers work there too. Apps also keep local databases for offline use. Since you cannot force users to update the app, cache formats and API versions must stay compatible for a long time. Make API responses cacheable where safe, since mobile networks are slow and unreliable.

## 427: What is the problem with caching in long-lived clients such as mobile apps?

Old app versions keep running for months. If an old version cached data in a format or with assumptions that later change, you cannot fix it by deploying the server. Design the client cache to be versioned and easy to clear, have a server-driven way to tell clients to drop cached data, and keep API responses backward compatible.

## 428: How do you prevent a cache from returning data after a user's account is deleted?

Deletion must also remove cached data: invalidate all keys for that user, purge CDN entries tagged with their ID, and drop sessions. For privacy laws like GDPR, cached copies count as stored data, so they must be removed in a reasonable time. Use tags or a user-scoped key prefix so you can find everything, and keep TTLs bounded so anything missed expires.

## 429: How does a write-back cache handle crash recovery?

It needs a durable record of changes not yet saved to the database. Options: enable Redis AOF with `appendfsync everysec` (lose up to one second), write changes to a Redis Stream or Kafka topic that a consumer applies to the database, or write to a local write-ahead log. On restart, replay pending changes. Without this, a crash loses unsaved writes.

## 430: How do you order writes in a write-back cache?

If several updates to the same key are merged, the final value is written once, which is fine. But updates across keys may be applied to the database in a different order than they happened, which can break invariants (for example, an order row written before its customer row). Either keep a per-entity order (partition by key in a stream), write in dependency order, or avoid write-back for data with cross-entity rules.

## 431: How do you cache results of permission-filtered queries, like search results that depend on what the user can see?

Caching the final filtered result per user has low hit ratio. Instead, cache the unfiltered results (or IDs) and apply the permission filter per user at read time. Or group users by permission set and cache per group. Never cache filtered results under a key that ignores the user's permissions.

## 432: How do caches behave in a split-brain or network partition?

If app servers cannot reach the cache, they fall back to the database, which is safe. Worse is when different servers see different cache nodes as primary after a bad failover, so writes and invalidations go to one side and reads to the other. When the partition heals, one side's data is dropped. For a cache this mostly means stale reads for a while; for data stored only in Redis it can mean lost data.

## 433: How would you make a local cache safe with many worker threads or processes?

In Node.js each worker thread and each cluster process has its own memory, so local caches are not shared. You get one copy per worker, which multiplies memory use and makes invalidation harder. Options: keep local caches small with short TTLs, share through Redis, or use a single process with async I/O. In languages with real shared memory (Java, Go), use a concurrent cache library like Caffeine or Ristretto.

## 434: How do you avoid the "everything expires at midnight" problem?

If keys are set with TTLs that end at a fixed time (like "until end of day"), they all expire at once and create a spike. Add jitter, refresh popular keys ahead of time, or stagger by key (for example add `hash(key) % 600` seconds). For data that really changes at midnight (daily prices), precompute the new values before midnight and switch keys atomically by changing the version.

## 435: How do you atomically switch to a new set of cached data?

Build the new data under new keys (for example `prices:v2025-11-20:*`) while the old ones are still served, then change a single pointer key (`prices:current = v2025-11-20`) to the new version. Readers read the pointer first, then the data. The switch is one write, so readers never see a mix of old and new. Old keys expire later.

## 436: What is the "cache as a crutch" anti-pattern?

It is when caching is used to hide problems that should be fixed: slow queries without indexes, N+1 queries, chatty service calls, or a database that is undersized. The system looks fine until the cache misses, then fails badly. Fix the root problem first so the uncached path is acceptable, then add caching for extra speed and cost savings.

## 437: How do you explain to a product manager the trade-offs of caching?

Use concrete examples: "With a 5-minute cache, the product page loads in 50 ms instead of 400 ms and costs us less, but if you change a price, some customers may see the old price for up to 5 minutes. We can make price changes show up immediately, but it takes more engineering work." Then let them choose the acceptable staleness per type of data.

## 438: How do you set a caching SLO?

Define what matters to users, for example: "99% of product updates are visible on the site within 60 seconds" (freshness SLO) and "p95 product API latency under 100 ms" (speed SLO). Measure freshness by tracking the time between a write and when readers see it. These goals guide TTL choice and whether you need event-based invalidation.

## 439: How do you measure cache freshness in production?

Add a version or `updated_at` to cached values and compare it with the database for a sample of reads (in the background, to avoid extra load). Or write a synthetic test that updates a record and measures how long until each cache layer returns the new value. Track the distribution of staleness, not just averages.

## 440: How do you design cache keys that are safe from injection?

If keys are built from user input, a value with separators (like `:` or `*`) could collide with other keys or match broader patterns in deletions. Validate input (IDs should match an expected format), escape or hash user-provided parts, and never pass user input straight into `SCAN MATCH` patterns or Lua scripts as code.

```ts
const safe = /^[0-9a-f-]{36}$/.test(id) ? id : null;
if (!safe) throw new Error("bad id");
const key = `user:${safe}`;
```

## 441: What happens if two different inputs hash to the same cache key?

If you hash long inputs (search queries, request bodies) to make keys, a collision would return the wrong data. With a strong hash like SHA-256, collisions are not a real concern. With short or weak hashes (like 32-bit), they can happen with large key counts. Use a strong hash, and optionally store the original input with the value and compare it on read.

## 442: How do you cache responses from POST endpoints that are really reads, like search?

HTTP caches will not cache them, so cache on the server: build a key from a normalized hash of the body and cache the result in Redis. Or change the API so searches use GET with query parameters (if they fit in URL limits), which allows browser and CDN caching. Some APIs also return a result ID that can be fetched with GET and cached.

## 443: What is the QUERY HTTP method, and how does it relate to caching?

`QUERY` is a proposed HTTP method (an IETF draft) for safe, idempotent requests that carry a body, like complex searches. Unlike POST, its responses are meant to be cacheable, with the body becoming part of the cache key. Support in servers, CDNs and browsers is still limited, so for now most APIs use GET with query strings or POST with server-side caching.

## 444: How do you cache with Redis in an environment with very strict latency budgets, like ad serving?

Put a local in-process cache in front of Redis for the hottest data, use connection pooling and pipelines, keep Redis in the same availability zone, set tight timeouts (single-digit milliseconds), and treat a slow cache as a miss with a default answer instead of waiting. Precompute and push data into local memory where possible, so the request path does no remote calls at all.

## 445: How would you cache data in a system that must work offline for hours?

Treat the local cache as a full local store: sync the needed data ahead of time, record local changes in a queue, and sync them when the connection is back, with conflict resolution (last write wins, merges, or user choice). This is an offline-first design rather than a simple cache. Service workers, IndexedDB, or a local SQLite database are common tools.

## 446: How do you decide between Redis, an in-process cache, and a CDN for a new feature?

- CDN: the response is public or the same for large groups, and it is served over HTTP.
- In-process: small, very hot, rarely changing data where some per-server staleness is fine.
- Redis: shared data across servers, larger data sets, or when you need fast invalidation in one place.

Often you combine them, but start with the simplest layer that solves the measured problem.

## 447: What would you check in a code review of a new cache?

- Key includes all inputs that change the value (user, tenant, language, version).
- TTL is set, with jitter where needed.
- Every write path invalidates or updates the key.
- Errors and timeouts fall back to the source.
- No sensitive data in shared caches without good reason.
- Size limits on local caches.
- Metrics for hits, misses and errors.
- Stampede protection for hot keys.

## 448: Describe a production caching incident and how you would investigate it.

Example: after a deploy, the database CPU jumps to 100% and the site slows down. Check cache hit ratio (dropped from 95% to 30%?), recent changes to key formats (a new version prefix makes all keys miss), TTL changes, Redis memory and evictions, and whether a flush happened. A common cause is a key format change that made the whole cache cold at once. Mitigate by rolling back or rate limiting, then plan gradual key migrations.

## 449: What are the most important ideas to remember about caching?

- A cache is a copy, so plan for it being wrong, missing or down.
- Decide how stale each piece of data can be before choosing TTLs.
- Invalidate on writes, and keep TTLs as a safety net.
- Protect the source from stampedes and cold starts.
- Keep keys precise and include everything that changes the value.
- Measure hit ratio, latency and freshness, and only cache what the numbers say is worth it.

## 450: If you could only use one caching technique for a new web app, which would you choose and why?

Proper HTTP caching headers. Correct `Cache-Control` for static assets (hashed names with `immutable`), HTML (`no-cache`) and public API responses (`s-maxage` with `stale-while-revalidate`) lets browsers and a CDN handle a large share of traffic with almost no code and no extra infrastructure. It is standard, works with every client, and is easy to reason about. Application caches like Redis can come later, when measurements show a specific bottleneck.
