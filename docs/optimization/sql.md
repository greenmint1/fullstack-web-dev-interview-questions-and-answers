# SQL Optimization Interview Questions and Answers

_Last updated: November 25, 2026_

450 interview questions with answers about making SQL queries and relational databases fast, split into three levels: 150 easy, 150 moderate and 150 advanced. They cover indexes, reading query plans, writing better queries, schema design, locking, configuration, and scaling.

Most answers apply to any SQL database. Where the details differ, the examples use PostgreSQL 19 and MySQL 9.7 LTS (InnoDB). Older behavior, like the MySQL query cache, is mentioned only where you will still run into it.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does SQL query optimization mean?](#1-what-does-sql-query-optimization-mean)
- [2: What are the most common reasons a SQL query is slow?](#2-what-are-the-most-common-reasons-a-sql-query-is-slow)
- [3: What is an index?](#3-what-is-an-index)
- [4: How does a B-tree index make a lookup faster?](#4-how-does-a-b-tree-index-make-a-lookup-faster)
- [5: What is a full table scan?](#5-what-is-a-full-table-scan)
- [6: What are the downsides of indexes?](#6-what-are-the-downsides-of-indexes)
- [7: How do you create an index?](#7-how-do-you-create-an-index)
- [8: Is a primary key indexed automatically?](#8-is-a-primary-key-indexed-automatically)
- [9: Are foreign key columns indexed automatically?](#9-are-foreign-key-columns-indexed-automatically)
- [10: What is a unique index?](#10-what-is-a-unique-index)
- [11: What is a composite index?](#11-what-is-a-composite-index)
- [12: What is the leftmost prefix rule?](#12-what-is-the-leftmost-prefix-rule)
- [13: What is EXPLAIN?](#13-what-is-explain)
- [14: What is the difference between EXPLAIN and EXPLAIN ANALYZE?](#14-what-is-the-difference-between-explain-and-explain-analyze)
- [15: What is a query plan?](#15-what-is-a-query-plan)
- [16: What is the query planner (optimizer)?](#16-what-is-the-query-planner-optimizer)
- [17: What is cost-based optimization?](#17-what-is-cost-based-optimization)
- [18: What are table statistics?](#18-what-are-table-statistics)
- [19: How do you update table statistics?](#19-how-do-you-update-table-statistics)
- [20: Why should you avoid SELECT *?](#20-why-should-you-avoid-select-)
- [21: What is the slow query log in MySQL?](#21-what-is-the-slow-query-log-in-mysql)
- [22: How do you find slow queries in PostgreSQL?](#22-how-do-you-find-slow-queries-in-postgresql)
- [23: What is the N+1 query problem?](#23-what-is-the-n1-query-problem)
- [24: How do you fix the N+1 problem?](#24-how-do-you-fix-the-n1-problem)
- [25: What does sargable mean?](#25-what-does-sargable-mean)
- [26: Why does wrapping a column in a function stop the index from being used?](#26-why-does-wrapping-a-column-in-a-function-stop-the-index-from-being-used)
- [27: Why doesn't LIKE '%abc' use a normal index?](#27-why-doesnt-like-abc-use-a-normal-index)
- [28: How does LIMIT help performance?](#28-how-does-limit-help-performance)
- [29: Why is OFFSET pagination slow on later pages?](#29-why-is-offset-pagination-slow-on-later-pages)
- [30: What is keyset pagination?](#30-what-is-keyset-pagination)
- [31: Should a filter go in WHERE or HAVING?](#31-should-a-filter-go-in-where-or-having)
- [32: Why do joins get slow?](#32-why-do-joins-get-slow)
- [33: Should you index join columns?](#33-should-you-index-join-columns)
- [34: Is INNER JOIN faster than LEFT JOIN?](#34-is-inner-join-faster-than-left-join)
- [35: What is normalization?](#35-what-is-normalization)
- [36: What is denormalization and when should you use it?](#36-what-is-denormalization-and-when-should-you-use-it)
- [37: How do data types affect performance?](#37-how-do-data-types-affect-performance)
- [38: Why shouldn't you store dates or numbers as strings?](#38-why-shouldnt-you-store-dates-or-numbers-as-strings)
- [39: What is implicit type conversion and why is it bad for performance?](#39-what-is-implicit-type-conversion-and-why-is-it-bad-for-performance)
- [40: What is a covering index?](#40-what-is-a-covering-index)
- [41: What is an index-only scan?](#41-what-is-an-index-only-scan)
- [42: What is index selectivity?](#42-what-is-index-selectivity)
- [43: When will the database ignore an index even though one exists?](#43-when-will-the-database-ignore-an-index-even-though-one-exists)
- [44: What is the difference between a clustered and a non-clustered index?](#44-what-is-the-difference-between-a-clustered-and-a-non-clustered-index)
- [45: How is a PostgreSQL table stored?](#45-how-is-a-postgresql-table-stored)
- [46: What is the difference between a sequential scan, an index scan and a bitmap scan?](#46-what-is-the-difference-between-a-sequential-scan-an-index-scan-and-a-bitmap-scan)
- [47: Why is inserting rows one by one slow?](#47-why-is-inserting-rows-one-by-one-slow)
- [48: Why can many small transactions be slow?](#48-why-can-many-small-transactions-be-slow)
- [49: How does transaction length affect performance?](#49-how-does-transaction-length-affect-performance)
- [50: What is a lock in a database?](#50-what-is-a-lock-in-a-database)
- [51: What is a deadlock?](#51-what-is-a-deadlock)
- [52: What is connection pooling?](#52-what-is-connection-pooling)
- [53: Why is opening a new database connection expensive?](#53-why-is-opening-a-new-database-connection-expensive)
- [54: What is a prepared statement and does it help performance?](#54-what-is-a-prepared-statement-and-does-it-help-performance)
- [55: Does MySQL have a query cache?](#55-does-mysql-have-a-query-cache)
- [56: How can application-level caching help database performance?](#56-how-can-application-level-caching-help-database-performance)
- [57: Does a view make a query faster?](#57-does-a-view-make-a-query-faster)
- [58: What is a materialized view?](#58-what-is-a-materialized-view)
- [59: What is a subquery?](#59-what-is-a-subquery)
- [60: Is a JOIN faster than a subquery?](#60-is-a-join-faster-than-a-subquery)
- [61: What is the difference between IN and EXISTS?](#61-what-is-the-difference-between-in-and-exists)
- [62: What is the problem with NOT IN and NULL?](#62-what-is-the-problem-with-not-in-and-null)
- [63: What is the difference between UNION and UNION ALL?](#63-what-is-the-difference-between-union-and-union-all)
- [64: Why can DISTINCT be expensive?](#64-why-can-distinct-be-expensive)
- [65: What is the difference between COUNT(*), COUNT(1) and COUNT(column)?](#65-what-is-the-difference-between-count-count1-and-countcolumn)
- [66: Why is SELECT COUNT(*) slow on a big PostgreSQL table?](#66-why-is-select-count-slow-on-a-big-postgresql-table)
- [67: Why is ORDER BY sometimes slow?](#67-why-is-order-by-sometimes-slow)
- [68: How can an index remove the need to sort?](#68-how-can-an-index-remove-the-need-to-sort)
- [69: How does the database run GROUP BY?](#69-how-does-the-database-run-group-by)
- [70: What is a temporary table and when does it help?](#70-what-is-a-temporary-table-and-when-does-it-help)
- [71: What is a CTE?](#71-what-is-a-cte)
- [72: Do CTEs make queries slower?](#72-do-ctes-make-queries-slower)
- [73: What is table partitioning?](#73-what-is-table-partitioning)
- [74: What is the difference between partitioning and sharding?](#74-what-is-the-difference-between-partitioning-and-sharding)
- [75: What is a read replica?](#75-what-is-a-read-replica)
- [76: What is replication lag?](#76-what-is-replication-lag)
- [77: What is VACUUM in PostgreSQL?](#77-what-is-vacuum-in-postgresql)
- [78: What is autovacuum?](#78-what-is-autovacuum)
- [79: What is table bloat?](#79-what-is-table-bloat)
- [80: What is MVCC?](#80-what-is-mvcc)
- [81: What is the buffer pool or shared buffers?](#81-what-is-the-buffer-pool-or-shared-buffers)
- [82: Why is disk I/O usually the biggest cost in a query?](#82-why-is-disk-io-usually-the-biggest-cost-in-a-query)
- [83: What is a page (block) in a database?](#83-what-is-a-page-block-in-a-database)
- [84: What is a partial index?](#84-what-is-a-partial-index)
- [85: What is an expression (functional) index?](#85-what-is-an-expression-functional-index)
- [86: How do you find unused indexes?](#86-how-do-you-find-unused-indexes)
- [87: How can an ORM cause slow SQL?](#87-how-can-an-orm-cause-slow-sql)
- [88: How do you see the SQL an ORM generates?](#88-how-do-you-see-the-sql-an-orm-generates)
- [89: How do you set a time limit for queries?](#89-how-do-you-set-a-time-limit-for-queries)
- [90: What is the fastest way to check if a row exists?](#90-what-is-the-fastest-way-to-check-if-a-row-exists)
- [91: What is the difference between DELETE and TRUNCATE for performance?](#91-what-is-the-difference-between-delete-and-truncate-for-performance)
- [92: How do you delete millions of rows without hurting the database?](#92-how-do-you-delete-millions-of-rows-without-hurting-the-database)
- [93: What is the fastest way to load a lot of data?](#93-what-is-the-fastest-way-to-load-a-lot-of-data)
- [94: What is an upsert?](#94-what-is-an-upsert)
- [95: How do OR conditions affect index use?](#95-how-do-or-conditions-affect-index-use)
- [96: Can an index be used for IS NULL?](#96-can-an-index-be-used-for-is-null)
- [97: What is a nested loop join?](#97-what-is-a-nested-loop-join)
- [98: What is a hash join?](#98-what-is-a-hash-join)
- [99: What is a merge join?](#99-what-is-a-merge-join)
- [100: What does the rows number mean in EXPLAIN?](#100-what-does-the-rows-number-mean-in-explain)
- [101: What does cost mean in PostgreSQL EXPLAIN output?](#101-what-does-cost-mean-in-postgresql-explain-output)
- [102: What does actual time mean in EXPLAIN ANALYZE?](#102-what-does-actual-time-mean-in-explain-analyze)
- [103: What does Using filesort mean in MySQL EXPLAIN?](#103-what-does-using-filesort-mean-in-mysql-explain)
- [104: What does Using temporary mean in MySQL EXPLAIN?](#104-what-does-using-temporary-mean-in-mysql-explain)
- [105: What does the type column mean in MySQL EXPLAIN?](#105-what-does-the-type-column-mean-in-mysql-explain)
- [106: What do possible_keys and key mean in MySQL EXPLAIN?](#106-what-do-possible_keys-and-key-mean-in-mysql-explain)
- [107: Why can very wide tables be slow?](#107-why-can-very-wide-tables-be-slow)
- [108: Should you store large files in the database?](#108-should-you-store-large-files-in-the-database)
- [109: What is pg_stat_activity?](#109-what-is-pg_stat_activity)
- [110: How do you see running queries in MySQL?](#110-how-do-you-see-running-queries-in-mysql)
- [111: How do you stop a long-running query?](#111-how-do-you-stop-a-long-running-query)
- [112: Is an index on a boolean column useful?](#112-is-an-index-on-a-boolean-column-useful)
- [113: Does the sort direction of an index matter?](#113-does-the-sort-direction-of-an-index-matter)
- [114: Should you use auto-increment IDs or UUIDs as primary keys?](#114-should-you-use-auto-increment-ids-or-uuids-as-primary-keys)
- [115: What is UUIDv7 and why is it better for indexes?](#115-what-is-uuidv7-and-why-is-it-better-for-indexes)
- [116: Is CHAR faster than VARCHAR?](#116-is-char-faster-than-varchar)
- [117: Why does choosing the right integer size matter?](#117-why-does-choosing-the-right-integer-size-matter)
- [118: How should you filter by date so an index can be used?](#118-how-should-you-filter-by-date-so-an-index-can-be-used)
- [119: How can adding an index lock a production table?](#119-how-can-adding-an-index-lock-a-production-table)
- [120: Is adding a column to a big table slow?](#120-is-adding-a-column-to-a-big-table-slow)
- [121: How do foreign keys affect write performance?](#121-how-do-foreign-keys-affect-write-performance)
- [122: Do triggers slow down writes?](#122-do-triggers-slow-down-writes)
- [123: Are stored procedures faster than queries from the app?](#123-are-stored-procedures-faster-than-queries-from-the-app)
- [124: What is a chatty application and why is it slow?](#124-what-is-a-chatty-application-and-why-is-it-slow)
- [125: Why should an API never return all rows of a table?](#125-why-should-an-api-never-return-all-rows-of-a-table)
- [126: How do you benchmark a database?](#126-how-do-you-benchmark-a-database)
- [127: What is the difference between latency and throughput for a database?](#127-what-is-the-difference-between-latency-and-throughput-for-a-database)
- [128: Why look at p95 and p99 query times instead of the average?](#128-why-look-at-p95-and-p99-query-times-instead-of-the-average)
- [129: Which queries should you optimize first?](#129-which-queries-should-you-optimize-first)
- [130: Why should you measure before optimizing?](#130-why-should-you-measure-before-optimizing)
- [131: What is a hot row?](#131-what-is-a-hot-row)
- [132: What does SELECT ... FOR UPDATE do?](#132-what-does-select--for-update-do)
- [133: What is a lock wait timeout?](#133-what-is-a-lock-wait-timeout)
- [134: How does the isolation level affect performance?](#134-how-does-the-isolation-level-affect-performance)
- [135: What are typical signs of a missing index?](#135-what-are-typical-signs-of-a-missing-index)
- [136: How many indexes are too many?](#136-how-many-indexes-are-too-many)
- [137: What is a redundant index?](#137-what-is-a-redundant-index)
- [138: How do you index a low-cardinality column that is always filtered on?](#138-how-do-you-index-a-low-cardinality-column-that-is-always-filtered-on)
- [139: Why is LIKE '%word%' a bad way to build search?](#139-why-is-like-word-a-bad-way-to-build-search)
- [140: What is full-text search in PostgreSQL and MySQL?](#140-what-is-full-text-search-in-postgresql-and-mysql)
- [141: Should you use json or jsonb in PostgreSQL?](#141-should-you-use-json-or-jsonb-in-postgresql)
- [142: What is a GIN index?](#142-what-is-a-gin-index)
- [143: What is the write-ahead log (WAL)?](#143-what-is-the-write-ahead-log-wal)
- [144: What is a checkpoint?](#144-what-is-a-checkpoint)
- [145: What is work_mem in PostgreSQL?](#145-what-is-work_mem-in-postgresql)
- [146: What is innodb_buffer_pool_size?](#146-what-is-innodb_buffer_pool_size)
- [147: What is a query hint?](#147-what-is-a-query-hint)
- [148: Can upgrading the database version make queries faster?](#148-can-upgrading-the-database-version-make-queries-faster)
- [149: How does hardware affect database performance?](#149-how-does-hardware-affect-database-performance)
- [150: What steps do you take when someone says a query is slow?](#150-what-steps-do-you-take-when-someone-says-a-query-is-slow)

### Moderate Questions (151-300)

- [151: How do you read a PostgreSQL EXPLAIN ANALYZE output?](#151-how-do-you-read-a-postgresql-explain-analyze-output)
- [152: What does the BUFFERS option show?](#152-what-does-the-buffers-option-show)
- [153: What does Rows Removed by Filter tell you?](#153-what-does-rows-removed-by-filter-tell-you)
- [154: What is the difference between Index Cond and Filter in a plan?](#154-what-is-the-difference-between-index-cond-and-filter-in-a-plan)
- [155: How do you see real timings in MySQL?](#155-how-do-you-see-real-timings-in-mysql)
- [156: How do you choose the column order in a composite index?](#156-how-do-you-choose-the-column-order-in-a-composite-index)
- [157: Why does a range condition stop later index columns from being used for seeking?](#157-why-does-a-range-condition-stop-later-index-columns-from-being-used-for-seeking)
- [158: How do you index a query with WHERE, ORDER BY and LIMIT?](#158-how-do-you-index-a-query-with-where-order-by-and-limit)
- [159: Can an index help GROUP BY?](#159-can-an-index-help-group-by)
- [160: What is the difference between INCLUDE columns and adding columns to the index key?](#160-what-is-the-difference-between-include-columns-and-adding-columns-to-the-index-key)
- [161: Why is a secondary index in InnoDB often covering for the primary key?](#161-why-is-a-secondary-index-in-innodb-often-covering-for-the-primary-key)
- [162: What is index condition pushdown in MySQL?](#162-what-is-index-condition-pushdown-in-mysql)
- [163: What is index merge in MySQL?](#163-what-is-index-merge-in-mysql)
- [164: What are BitmapAnd and BitmapOr in PostgreSQL plans?](#164-what-are-bitmapand-and-bitmapor-in-postgresql-plans)
- [165: How do you enforce uniqueness only for active rows?](#165-how-do-you-enforce-uniqueness-only-for-active-rows)
- [166: How do soft deletes affect query performance?](#166-how-do-soft-deletes-affect-query-performance)
- [167: How do you make case-insensitive lookups fast?](#167-how-do-you-make-case-insensitive-lookups-fast)
- [168: Why doesn't LIKE 'abc%' use my index in PostgreSQL?](#168-why-doesnt-like-abc-use-my-index-in-postgresql)
- [169: How do you speed up LIKE '%abc%' in PostgreSQL?](#169-how-do-you-speed-up-like-abc-in-postgresql)
- [170: How do you index jsonb data?](#170-how-do-you-index-jsonb-data)
- [171: How do you index JSON values in MySQL?](#171-how-do-you-index-json-values-in-mysql)
- [172: What are generated columns and how do they help performance?](#172-what-are-generated-columns-and-how-do-they-help-performance)
- [173: What is a BRIN index?](#173-what-is-a-brin-index)
- [174: When would you use a hash index in PostgreSQL?](#174-when-would-you-use-a-hash-index-in-postgresql)
- [175: What is a GiST index used for?](#175-what-is-a-gist-index-used-for)
- [176: What is an invisible index in MySQL?](#176-what-is-an-invisible-index-in-mysql)
- [177: How do you check the size of tables and indexes?](#177-how-do-you-check-the-size-of-tables-and-indexes)
- [178: How do you tune autovacuum for a big, busy table?](#178-how-do-you-tune-autovacuum-for-a-big-busy-table)
- [179: What are HOT updates in PostgreSQL?](#179-what-are-hot-updates-in-postgresql)
- [180: Why can updates be expensive in PostgreSQL when a table has many indexes?](#180-why-can-updates-be-expensive-in-postgresql-when-a-table-has-many-indexes)
- [181: How do you remove bloat from a PostgreSQL table?](#181-how-do-you-remove-bloat-from-a-postgresql-table)
- [182: How do you fix a bloated index?](#182-how-do-you-fix-a-bloated-index)
- [183: What does OPTIMIZE TABLE do in MySQL?](#183-what-does-optimize-table-do-in-mysql)
- [184: What are extended statistics in PostgreSQL?](#184-what-are-extended-statistics-in-postgresql)
- [185: How do you get more detailed statistics for one column?](#185-how-do-you-get-more-detailed-statistics-for-one-column)
- [186: What are histograms in MySQL?](#186-what-are-histograms-in-mysql)
- [187: Why do estimates go wrong when you filter on several related columns?](#187-why-do-estimates-go-wrong-when-you-filter-on-several-related-columns)
- [188: What are generic and custom plans in PostgreSQL?](#188-what-are-generic-and-custom-plans-in-postgresql)
- [189: Why can the same query be fast for one value and slow for another?](#189-why-can-the-same-query-be-fast-for-one-value-and-slow-for-another)
- [190: How do you rewrite a correlated subquery that runs once per row?](#190-how-do-you-rewrite-a-correlated-subquery-that-runs-once-per-row)
- [191: What is a LATERAL join and when does it help?](#191-what-is-a-lateral-join-and-when-does-it-help)
- [192: How can window functions replace self-joins?](#192-how-can-window-functions-replace-self-joins)
- [193: What are the ways to get the top N rows per group, and which is fastest?](#193-what-are-the-ways-to-get-the-top-n-rows-per-group-and-which-is-fastest)
- [194: What is DISTINCT ON in PostgreSQL?](#194-what-is-distinct-on-in-postgresql)
- [195: How do you rewrite an OR across different columns so indexes are used?](#195-how-do-you-rewrite-an-or-across-different-columns-so-indexes-are-used)
- [196: Why should you aggregate before joining?](#196-why-should-you-aggregate-before-joining)
- [197: What is join fan-out and how does it break aggregates?](#197-what-is-join-fan-out-and-how-does-it-break-aggregates)
- [198: How do you show a total count with paginated results without a slow COUNT(*)?](#198-how-do-you-show-a-total-count-with-paginated-results-without-a-slow-count)
- [199: How do you update many rows from another table in one statement?](#199-how-do-you-update-many-rows-from-another-table-in-one-statement)
- [200: How large should a batch be for bulk inserts?](#200-how-large-should-a-batch-be-for-bulk-inserts)
- [201: How do you insert many rows from an app in PostgreSQL with one parameterized query?](#201-how-do-you-insert-many-rows-from-an-app-in-postgresql-with-one-parameterized-query)
- [202: What is the problem with a huge IN list?](#202-what-is-the-problem-with-a-huge-in-list)
- [203: How do you size a connection pool?](#203-how-do-you-size-a-connection-pool)
- [204: What are the pool modes in PgBouncer?](#204-what-are-the-pool-modes-in-pgbouncer)
- [205: Why do serverless apps often run out of database connections?](#205-why-do-serverless-apps-often-run-out-of-database-connections)
- [206: What does idle in transaction mean and why is it bad?](#206-what-does-idle-in-transaction-mean-and-why-is-it-bad)
- [207: How do you find which query is blocking others in PostgreSQL?](#207-how-do-you-find-which-query-is-blocking-others-in-postgresql)
- [208: How do you find lock waits in MySQL?](#208-how-do-you-find-lock-waits-in-mysql)
- [209: How does SKIP LOCKED help with job queues?](#209-how-does-skip-locked-help-with-job-queues)
- [210: What does NOWAIT do?](#210-what-does-nowait-do)
- [211: What is optimistic locking and how does it reduce lock contention?](#211-what-is-optimistic-locking-and-how-does-it-reduce-lock-contention)
- [212: What are gap locks and next-key locks in InnoDB?](#212-what-are-gap-locks-and-next-key-locks-in-innodb)
- [213: How do you reduce deadlocks?](#213-how-do-you-reduce-deadlocks)
- [214: What are advisory locks in PostgreSQL?](#214-what-are-advisory-locks-in-postgresql)
- [215: How do you add a NOT NULL constraint to a big PostgreSQL table without a long lock?](#215-how-do-you-add-a-not-null-constraint-to-a-big-postgresql-table-without-a-long-lock)
- [216: How do you add a foreign key to a big table without blocking writes?](#216-how-do-you-add-a-foreign-key-to-a-big-table-without-blocking-writes)
- [217: What are online schema change tools for MySQL?](#217-what-are-online-schema-change-tools-for-mysql)
- [218: Why is a long-running migration dangerous even if it takes a "light" lock?](#218-why-is-a-long-running-migration-dangerous-even-if-it-takes-a-light-lock)
- [219: How do you refresh a materialized view without blocking readers?](#219-how-do-you-refresh-a-materialized-view-without-blocking-readers)
- [220: What is a summary (rollup) table?](#220-what-is-a-summary-rollup-table)
- [221: What is the cache-aside pattern?](#221-what-is-the-cache-aside-pattern)
- [222: How do you route reads to replicas without showing stale data?](#222-how-do-you-route-reads-to-replicas-without-showing-stale-data)
- [223: When does partition pruning work?](#223-when-does-partition-pruning-work)
- [224: How do you choose a partition key?](#224-how-do-you-choose-a-partition-key)
- [225: Can you have too many partitions?](#225-can-you-have-too-many-partitions)
- [226: How do you manage time-based partitions over time?](#226-how-do-you-manage-time-based-partitions-over-time)
- [227: How do indexes work on partitioned tables?](#227-how-do-indexes-work-on-partitioned-tables)
- [228: How does parallel query work in PostgreSQL?](#228-how-does-parallel-query-work-in-postgresql)
- [229: Why might PostgreSQL not use parallel query?](#229-why-might-postgresql-not-use-parallel-query)
- [230: What is JIT compilation in PostgreSQL?](#230-what-is-jit-compilation-in-postgresql)
- [231: How should you set shared_buffers and effective_cache_size?](#231-how-should-you-set-shared_buffers-and-effective_cache_size)
- [232: What is random_page_cost and why change it?](#232-what-is-random_page_cost-and-why-change-it)
- [233: What is maintenance_work_mem?](#233-what-is-maintenance_work_mem)
- [234: How do you tune checkpoints in PostgreSQL?](#234-how-do-you-tune-checkpoints-in-postgresql)
- [235: What does synchronous_commit = off do?](#235-what-does-synchronous_commit--off-do)
- [236: What does innodb_flush_log_at_trx_commit control?](#236-what-does-innodb_flush_log_at_trx_commit-control)
- [237: Why does the redo log size matter in MySQL?](#237-why-does-the-redo-log-size-matter-in-mysql)
- [238: What are tmp_table_size and max_heap_table_size in MySQL?](#238-what-are-tmp_table_size-and-max_heap_table_size-in-mysql)
- [239: How can you tell that a query spilled to disk?](#239-how-can-you-tell-that-a-query-spilled-to-disk)
- [240: What is auto_explain?](#240-what-is-auto_explain)
- [241: What are Performance Schema and the sys schema in MySQL?](#241-what-are-performance-schema-and-the-sys-schema-in-mysql)
- [242: How do you find tables that are scanned too often in PostgreSQL?](#242-how-do-you-find-tables-that-are-scanned-too-often-in-postgresql)
- [243: What is the cache hit ratio and how do you check it?](#243-what-is-the-cache-hit-ratio-and-how-do-you-check-it)
- [244: How does pg_stat_statements group queries?](#244-how-does-pg_stat_statements-group-queries)
- [245: How do you run EXPLAIN ANALYZE safely in production?](#245-how-do-you-run-explain-analyze-safely-in-production)
- [246: Why should you test queries on production-sized data?](#246-why-should-you-test-queries-on-production-sized-data)
- [247: How do you catch query performance regressions after a deploy?](#247-how-do-you-catch-query-performance-regressions-after-a-deploy)
- [248: What is TOAST in PostgreSQL and how does it affect queries?](#248-what-is-toast-in-postgresql-and-how-does-it-affect-queries)
- [249: What are the trade-offs of storing data in JSON columns instead of normal columns?](#249-what-are-the-trade-offs-of-storing-data-in-json-columns-instead-of-normal-columns)
- [250: What is the EAV pattern and why is it slow?](#250-what-is-the-eav-pattern-and-why-is-it-slow)
- [251: Should you store statuses as text, enums or a lookup table?](#251-should-you-store-statuses-as-text-enums-or-a-lookup-table)
- [252: Should money be stored as numeric, float or integer?](#252-should-money-be-stored-as-numeric-float-or-integer)
- [253: How do you make COUNT(DISTINCT ...) faster?](#253-how-do-you-make-countdistinct--faster)
- [254: What is TABLESAMPLE?](#254-what-is-tablesample)
- [255: How should you design indexes for a multi-tenant table?](#255-how-should-you-design-indexes-for-a-multi-tenant-table)
- [256: How does PostgreSQL row-level security affect performance?](#256-how-does-postgresql-row-level-security-affect-performance)
- [257: What is a cartesian explosion when an ORM eager-loads several collections?](#257-what-is-a-cartesian-explosion-when-an-orm-eager-loads-several-collections)
- [258: How do you detect N+1 queries automatically?](#258-how-do-you-detect-n1-queries-automatically)
- [259: How do you replace JOIN plus DISTINCT with EXISTS?](#259-how-do-you-replace-join-plus-distinct-with-exists)
- [260: What is the difference between NOT EXISTS and LEFT JOIN ... IS NULL?](#260-what-is-the-difference-between-not-exists-and-left-join--is-null)
- [261: Why are "optional filter" conditions like (col = $1 OR $1 IS NULL) slow?](#261-why-are-optional-filter-conditions-like-col--1-or-1-is-null-slow)
- [262: Why is ORDER BY RAND() slow, and what can you use instead?](#262-why-is-order-by-rand-slow-and-what-can-you-use-instead)
- [263: How do recursive CTEs perform and how do you make them faster?](#263-how-do-recursive-ctes-perform-and-how-do-you-make-them-faster)
- [264: What are faster ways to store trees than parent_id alone?](#264-what-are-faster-ways-to-store-trees-than-parent_id-alone)
- [265: Does an upsert have hidden costs?](#265-does-an-upsert-have-hidden-costs)
- [266: What is the MERGE statement?](#266-what-is-the-merge-statement)
- [267: How does RETURNING save round trips?](#267-how-does-returning-save-round-trips)
- [268: What does PostgreSQL 19's ON CONFLICT DO SELECT solve?](#268-what-does-postgresql-19s-on-conflict-do-select-solve)
- [269: How should you archive old data?](#269-how-should-you-archive-old-data)
- [270: What are unlogged tables in PostgreSQL?](#270-what-are-unlogged-tables-in-postgresql)
- [271: When should you use a temporary table instead of a CTE or subquery?](#271-when-should-you-use-a-temporary-table-instead-of-a-cte-or-subquery)
- [272: Why does a type or collation mismatch on join columns slow things down?](#272-why-does-a-type-or-collation-mismatch-on-join-columns-slow-things-down)
- [273: What are prefix indexes in MySQL?](#273-what-are-prefix-indexes-in-mysql)
- [274: How do you index a very long text value for exact lookups?](#274-how-do-you-index-a-very-long-text-value-for-exact-lookups)
- [275: What is the index length limit in MySQL with utf8mb4?](#275-what-is-the-index-length-limit-in-mysql-with-utf8mb4)
- [276: How do you speed up time-series aggregation queries?](#276-how-do-you-speed-up-time-series-aggregation-queries)
- [277: Why can adding LIMIT make a query slower?](#277-why-can-adding-limit-make-a-query-slower)
- [278: How does the visibility map affect index-only scans?](#278-how-does-the-visibility-map-affect-index-only-scans)
- [279: How do you monitor replication lag?](#279-how-do-you-monitor-replication-lag)
- [280: Why can long queries on a PostgreSQL replica be cancelled?](#280-why-can-long-queries-on-a-postgresql-replica-be-cancelled)
- [281: What extra EXPLAIN options are useful in PostgreSQL?](#281-what-extra-explain-options-are-useful-in-postgresql)
- [282: How does the network affect query performance?](#282-how-does-the-network-affect-query-performance)
- [283: How do you fetch a very large result set without running out of memory?](#283-how-do-you-fetch-a-very-large-result-set-without-running-out-of-memory)
- [284: What is a covering index in MySQL and how do you see it in EXPLAIN?](#284-what-is-a-covering-index-in-mysql-and-how-do-you-see-it-in-explain)
- [285: How do you enable the hypergraph optimizer in MySQL 9.7?](#285-how-do-you-enable-the-hypergraph-optimizer-in-mysql-97)
- [286: What is pg_plan_advice in PostgreSQL 19?](#286-what-is-pg_plan_advice-in-postgresql-19)
- [287: Why should you avoid functions in the SELECT list that run a query per row?](#287-why-should-you-avoid-functions-in-the-select-list-that-run-a-query-per-row)
- [288: How do you choose between a materialized view and a cache like Redis?](#288-how-do-you-choose-between-a-materialized-view-and-a-cache-like-redis)
- [289: How can the app reduce load on the database?](#289-how-can-the-app-reduce-load-on-the-database)
- [290: What is LISTEN/NOTIFY and how can it replace polling?](#290-what-is-listennotify-and-how-can-it-replace-polling)
- [291: How do you find duplicate indexes in PostgreSQL?](#291-how-do-you-find-duplicate-indexes-in-postgresql)
- [292: Why is it a bad idea to run analytics queries on the main OLTP database?](#292-why-is-it-a-bad-idea-to-run-analytics-queries-on-the-main-oltp-database)
- [293: What is the difference between OLTP and OLAP workloads?](#293-what-is-the-difference-between-oltp-and-olap-workloads)
- [294: How do you make a slow dashboard query fast?](#294-how-do-you-make-a-slow-dashboard-query-fast)
- [295: What is a "Nested Loop" with a high loops count telling you?](#295-what-is-a-nested-loop-with-a-high-loops-count-telling-you)
- [296: How do you test if an index change helps without affecting production?](#296-how-do-you-test-if-an-index-change-helps-without-affecting-production)
- [297: How do you avoid locking problems when backfilling a new column?](#297-how-do-you-avoid-locking-problems-when-backfilling-a-new-column)
- [298: What is lock escalation and does it happen in PostgreSQL or MySQL?](#298-what-is-lock-escalation-and-does-it-happen-in-postgresql-or-mysql)
- [299: Why might a query be slow only the first time it runs?](#299-why-might-a-query-be-slow-only-the-first-time-it-runs)
- [300: How would you approach a slow page in a web app from start to finish?](#300-how-would-you-approach-a-slow-page-in-a-web-app-from-start-to-finish)

### Advanced Questions (301-450)

- [301: How does PostgreSQL estimate how many rows match WHERE col = value?](#301-how-does-postgresql-estimate-how-many-rows-match-where-col--value)
- [302: How does the planner estimate the size of a join?](#302-how-does-the-planner-estimate-the-size-of-a-join)
- [303: Why do estimate errors get worse in queries with many joins?](#303-why-do-estimate-errors-get-worse-in-queries-with-many-joins)
- [304: How does PostgreSQL choose the join order?](#304-how-does-postgresql-choose-the-join-order)
- [305: What is GEQO?](#305-what-is-geqo)
- [306: How does the planner decide between an index scan and a sequential scan?](#306-how-does-the-planner-decide-between-an-index-scan-and-a-sequential-scan)
- [307: What is correlation in pg_stats and why does it matter?](#307-what-is-correlation-in-pg_stats-and-why-does-it-matter)
- [308: What does the CLUSTER command do in PostgreSQL?](#308-what-does-the-cluster-command-do-in-postgresql)
- [309: How do page splits work in InnoDB and why do they hurt?](#309-how-do-page-splits-work-in-innodb-and-why-do-they-hurt)
- [310: Why are random UUID primary keys especially bad in InnoDB?](#310-why-are-random-uuid-primary-keys-especially-bad-in-innodb)
- [311: What is B-tree deduplication in PostgreSQL?](#311-what-is-b-tree-deduplication-in-postgresql)
- [312: What is bottom-up index deletion?](#312-what-is-bottom-up-index-deletion)
- [313: How does skip scan work in PostgreSQL 18?](#313-how-does-skip-scan-work-in-postgresql-18)
- [314: What is asynchronous I/O in PostgreSQL 18 and 19?](#314-what-is-asynchronous-io-in-postgresql-18-and-19)
- [315: What is transaction ID wraparound in PostgreSQL?](#315-what-is-transaction-id-wraparound-in-postgresql)
- [316: What is an aggressive (anti-wraparound) vacuum and why can it hurt?](#316-what-is-an-aggressive-anti-wraparound-vacuum-and-why-can-it-hurt)
- [317: What are MultiXacts and how can they cause problems?](#317-what-are-multixacts-and-how-can-they-cause-problems)
- [318: What holds back the xmin horizon and why does it matter?](#318-what-holds-back-the-xmin-horizon-and-why-does-it-matter)
- [319: How can a replication slot fill up the disk?](#319-how-can-a-replication-slot-fill-up-the-disk)
- [320: What is the InnoDB history list length?](#320-what-is-the-innodb-history-list-length)
- [321: What is the InnoDB purge process?](#321-what-is-the-innodb-purge-process)
- [322: What happened to the InnoDB change buffer and adaptive hash index?](#322-what-happened-to-the-innodb-change-buffer-and-adaptive-hash-index)
- [323: What is the InnoDB doublewrite buffer?](#323-what-is-the-innodb-doublewrite-buffer)
- [324: Why does PostgreSQL write full page images to the WAL, and how does that affect write volume?](#324-why-does-postgresql-write-full-page-images-to-the-wal-and-how-does-that-affect-write-volume)
- [325: How can many concurrent commits be made cheaper?](#325-how-can-many-concurrent-commits-be-made-cheaper)
- [326: What does innodb_io_capacity control?](#326-what-does-innodb_io_capacity-control)
- [327: Why use huge pages for a database server?](#327-why-use-huge-pages-for-a-database-server)
- [328: How do you plan memory so the server doesn't run out?](#328-how-do-you-plan-memory-so-the-server-doesnt-run-out)
- [329: What is hash_mem_multiplier?](#329-what-is-hash_mem_multiplier)
- [330: What happens when a hash join's data is skewed?](#330-what-happens-when-a-hash-joins-data-is-skewed)
- [331: What is the Memoize node in PostgreSQL?](#331-what-is-the-memoize-node-in-postgresql)
- [332: What is incremental sort?](#332-what-is-incremental-sort)
- [333: What are partitionwise joins and aggregates?](#333-what-are-partitionwise-joins-and-aggregates)
- [334: What is run-time partition pruning?](#334-what-is-run-time-partition-pruning)
- [335: Why can queries on tables with many partitions get slow even with pruning?](#335-why-can-queries-on-tables-with-many-partitions-get-slow-even-with-pruning)
- [336: When does planning time matter more than execution time?](#336-when-does-planning-time-matter-more-than-execution-time)
- [337: What is cursor_tuple_fraction?](#337-what-is-cursor_tuple_fraction)
- [338: How do you get statistics on an expression?](#338-how-do-you-get-statistics-on-an-expression)
- [339: What are optimization fences and when would you use one on purpose?](#339-what-are-optimization-fences-and-when-would-you-use-one-on-purpose)
- [340: How do IN lists with different lengths affect query statistics tools?](#340-how-do-in-lists-with-different-lengths-affect-query-statistics-tools)
- [341: What causes a query plan to suddenly change, and how do you investigate it?](#341-what-causes-a-query-plan-to-suddenly-change-and-how-do-you-investigate-it)
- [342: How can you keep plans stable for important queries?](#342-how-can-you-keep-plans-stable-for-important-queries)
- [343: Why can sequences or auto-increment become a bottleneck?](#343-why-can-sequences-or-auto-increment-become-a-bottleneck)
- [344: What is right-edge contention on an index?](#344-what-is-right-edge-contention-on-an-index)
- [345: How do you measure write amplification from indexes?](#345-how-do-you-measure-write-amplification-from-indexes)
- [346: When is a BRIN index better than a B-tree for time-series data, and when is it worse?](#346-when-is-a-brin-index-better-than-a-b-tree-for-time-series-data-and-when-is-it-worse)
- [347: Why do you need an index on the child column for ON DELETE CASCADE?](#347-why-do-you-need-an-index-on-the-child-column-for-on-delete-cascade)
- [348: How do you delete a large tree of related data efficiently?](#348-how-do-you-delete-a-large-tree-of-related-data-efficiently)
- [349: What semi-join strategies does MySQL use for IN subqueries?](#349-what-semi-join-strategies-does-mysql-use-for-in-subqueries)
- [350: What is derived table merging and condition pushdown in MySQL?](#350-what-is-derived-table-merging-and-condition-pushdown-in-mysql)
- [351: What is the MySQL optimizer trace?](#351-what-is-the-mysql-optimizer-trace)
- [352: What are index dives in MySQL?](#352-what-are-index-dives-in-mysql)
- [353: How does InnoDB calculate index statistics, and why might they be wrong?](#353-how-does-innodb-calculate-index-statistics-and-why-might-they-be-wrong)
- [354: How does InnoDB keep a big table scan from flushing the buffer pool?](#354-how-does-innodb-keep-a-big-table-scan-from-flushing-the-buffer-pool)
- [355: How does PostgreSQL protect its cache from large sequential scans?](#355-how-does-postgresql-protect-its-cache-from-large-sequential-scans)
- [356: What is pg_prewarm used for?](#356-what-is-pg_prewarm-used-for)
- [357: Why is a high max_connections bad in PostgreSQL?](#357-why-is-a-high-max_connections-bad-in-postgresql)
- [358: What is a cache stampede and how do you prevent it?](#358-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [359: How do you choose a sharding key?](#359-how-do-you-choose-a-sharding-key)
- [360: What problems come with cross-shard queries?](#360-what-problems-come-with-cross-shard-queries)
- [361: What are Citus and Vitess?](#361-what-are-citus-and-vitess)
- [362: How do you generate unique IDs across shards?](#362-how-do-you-generate-unique-ids-across-shards)
- [363: What is a hot shard and how do you fix it?](#363-what-is-a-hot-shard-and-how-do-you-fix-it)
- [364: What is the cost of synchronous replication?](#364-what-is-the-cost-of-synchronous-replication)
- [365: How can logical replication help with big migrations?](#365-how-can-logical-replication-help-with-big-migrations)
- [366: What is CQRS and how does it relate to database performance?](#366-what-is-cqrs-and-how-does-it-relate-to-database-performance)
- [367: How do you handle very high write rates for counters?](#367-how-do-you-handle-very-high-write-rates-for-counters)
- [368: How should you design a job queue table in PostgreSQL?](#368-how-should-you-design-a-job-queue-table-in-postgresql)
- [369: What is the expand-and-contract pattern for schema changes?](#369-what-is-the-expand-and-contract-pattern-for-schema-changes)
- [370: What happens if CREATE INDEX CONCURRENTLY fails?](#370-what-happens-if-create-index-concurrently-fails)
- [371: How does column order affect row size in PostgreSQL?](#371-how-does-column-order-affect-row-size-in-postgresql)
- [372: How much space do NULLs take?](#372-how-much-space-do-nulls-take)
- [373: How does compression help database performance?](#373-how-does-compression-help-database-performance)
- [374: How do you make full-text search fast and avoid recomputing tsvector?](#374-how-do-you-make-full-text-search-fast-and-avoid-recomputing-tsvector)
- [375: How do you find the nearest matches by similarity quickly?](#375-how-do-you-find-the-nearest-matches-by-similarity-quickly)
- [376: How do you make geospatial queries fast?](#376-how-do-you-make-geospatial-queries-fast)
- [377: How do you implement keyset pagination when the sort column isn't unique or can be NULL?](#377-how-do-you-implement-keyset-pagination-when-the-sort-column-isnt-unique-or-can-be-null)
- [378: How do you do keyset pagination with mixed sort directions?](#378-how-do-you-do-keyset-pagination-with-mixed-sort-directions)
- [379: What is a deferred join and how does it speed up OFFSET pagination in MySQL?](#379-what-is-a-deferred-join-and-how-does-it-speed-up-offset-pagination-in-mysql)
- [380: What does Serializable isolation cost in PostgreSQL?](#380-what-does-serializable-isolation-cost-in-postgresql)
- [381: How should the app handle serialization failures and deadlocks?](#381-how-should-the-app-handle-serialization-failures-and-deadlocks)
- [382: What is write skew?](#382-what-is-write-skew)
- [383: How do foreign key checks cause lock contention?](#383-how-do-foreign-key-checks-cause-lock-contention)
- [384: Which ALTER TABLE operations take the strongest lock in PostgreSQL?](#384-which-alter-table-operations-take-the-strongest-lock-in-postgresql)
- [385: When will the planner use a partial index?](#385-when-will-the-planner-use-a-partial-index)
- [386: What rules apply to expression indexes?](#386-what-rules-apply-to-expression-indexes)
- [387: How does function volatility affect performance in PostgreSQL?](#387-how-does-function-volatility-affect-performance-in-postgresql)
- [388: Why are simple SQL functions faster than PL/pgSQL functions inside queries?](#388-why-are-simple-sql-functions-faster-than-plpgsql-functions-inside-queries)
- [389: How do you fix bad row estimates for set-returning functions?](#389-how-do-you-fix-bad-row-estimates-for-set-returning-functions)
- [390: What are the main sort methods in PostgreSQL and when does each appear?](#390-what-are-the-main-sort-methods-in-postgresql-and-when-does-each-appear)
- [391: How does collation affect sorting and comparison speed?](#391-how-does-collation-affect-sorting-and-comparison-speed)
- [392: Why might a query be fast in psql but slow from the application?](#392-why-might-a-query-be-fast-in-psql-but-slow-from-the-application)
- [393: What is pipeline mode and how does it reduce latency?](#393-what-is-pipeline-mode-and-how-does-it-reduce-latency)
- [394: How do JDBC driver settings affect batch insert speed?](#394-how-do-jdbc-driver-settings-affect-batch-insert-speed)
- [395: How do you plan database capacity for growth?](#395-how-do-you-plan-database-capacity-for-growth)
- [396: When should you scale up, add replicas, or shard?](#396-when-should-you-scale-up-add-replicas-or-shard)
- [397: What mistakes make database benchmarks misleading?](#397-what-mistakes-make-database-benchmarks-misleading)
- [398: A query was fast for months and is now slow. How do you investigate?](#398-a-query-was-fast-for-months-and-is-now-slow-how-do-you-investigate)
- [399: The database CPU is at 100%. What do you do?](#399-the-database-cpu-is-at-100-what-do-you-do)
- [400: The disk I/O is saturated. What are the likely causes?](#400-the-disk-io-is-saturated-what-are-the-likely-causes)
- [401: The app gets "too many connections" errors. How do you fix it properly?](#401-the-app-gets-too-many-connections-errors-how-do-you-fix-it-properly)
- [402: Replica lag keeps growing. What can cause it?](#402-replica-lag-keeps-growing-what-can-cause-it)
- [403: The WAL directory is filling the disk. What are the usual causes?](#403-the-wal-directory-is-filling-the-disk-what-are-the-usual-causes)
- [404: A table keeps bloating even though autovacuum is on. What do you check?](#404-a-table-keeps-bloating-even-though-autovacuum-is-on-what-do-you-check)
- [405: Deadlocks started after a deploy. How do you find the cause?](#405-deadlocks-started-after-a-deploy-how-do-you-find-the-cause)
- [406: A query is fast on staging but slow in production. Why?](#406-a-query-is-fast-on-staging-but-slow-in-production-why)
- [407: How would you design a social feed so it loads fast?](#407-how-would-you-design-a-social-feed-so-it-loads-fast)
- [408: How would you build a leaderboard with frequent score updates?](#408-how-would-you-build-a-leaderboard-with-frequent-score-updates)
- [409: How do you make a search page with many optional filters and sort options fast?](#409-how-do-you-make-a-search-page-with-many-optional-filters-and-sort-options-fast)
- [410: How would you store and query audit logs at large scale?](#410-how-would-you-store-and-query-audit-logs-at-large-scale)
- [411: How do you deal with a noisy neighbor in a multi-tenant database?](#411-how-do-you-deal-with-a-noisy-neighbor-in-a-multi-tenant-database)
- [412: How do you change a primary key from int to bigint on a huge table?](#412-how-do-you-change-a-primary-key-from-int-to-bigint-on-a-huge-table)
- [413: A table with heavy soft deletes is getting slow. What would you do?](#413-a-table-with-heavy-soft-deletes-is-getting-slow-what-would-you-do)
- [414: A query with WHERE status IN (...) ORDER BY created_at LIMIT 20 is slow. How do you fix it?](#414-a-query-with-where-status-in--order-by-created_at-limit-20-is-slow-how-do-you-fix-it)
- [415: A product search with LIKE '%term%' became slow as the catalog grew. What are your options?](#415-a-product-search-with-like-term-became-slow-as-the-catalog-grew-what-are-your-options)
- [416: A report joining six tables uses nested loops and takes minutes. What do you look at?](#416-a-report-joining-six-tables-uses-nested-loops-and-takes-minutes-what-do-you-look-at)
- [417: How would you handle very high-volume event ingestion in a SQL database?](#417-how-would-you-handle-very-high-volume-event-ingestion-in-a-sql-database)
- [418: How do you handle a flash sale where many users buy the same product at once?](#418-how-do-you-handle-a-flash-sale-where-many-users-buy-the-same-product-at-once)
- [419: How do you stop one bad query from taking down the database?](#419-how-do-you-stop-one-bad-query-from-taking-down-the-database)
- [420: Which database metrics should you monitor?](#420-which-database-metrics-should-you-monitor)
- [421: What are wait events and how do they help diagnose slowness?](#421-what-are-wait-events-and-how-do-they-help-diagnose-slowness)
- [422: What should you do after a major version upgrade to avoid slow queries?](#422-what-should-you-do-after-a-major-version-upgrade-to-avoid-slow-queries)
- [423: How do you decide between denormalizing, caching and changing the database?](#423-how-do-you-decide-between-denormalizing-caching-and-changing-the-database)
- [424: What are the performance trade-offs of using an ORM versus raw SQL?](#424-what-are-the-performance-trade-offs-of-using-an-orm-versus-raw-sql)
- [425: What do you check when reviewing a pull request that changes SQL or the schema?](#425-what-do-you-check-when-reviewing-a-pull-request-that-changes-sql-or-the-schema)
- [426: How do you make sure index changes don't break other queries?](#426-how-do-you-make-sure-index-changes-dont-break-other-queries)
- [427: How do generic plans interact with partitioned tables and prepared statements?](#427-how-do-generic-plans-interact-with-partitioned-tables-and-prepared-statements)
- [428: Why might an index-only scan still be slow?](#428-why-might-an-index-only-scan-still-be-slow)
- [429: How can the planner use a CHECK constraint to skip work?](#429-how-can-the-planner-use-a-check-constraint-to-skip-work)
- [430: What is join removal?](#430-what-is-join-removal)
- [431: How do you speed up a query that uses OFFSET-based pagination in an admin panel you can't fully rewrite?](#431-how-do-you-speed-up-a-query-that-uses-offset-based-pagination-in-an-admin-panel-you-cant-fully-rewrite)
- [432: When can't keyset pagination be used, and what are the alternatives?](#432-when-cant-keyset-pagination-be-used-and-what-are-the-alternatives)
- [433: How does the WAL affect replicas and backups, and how can you reduce its volume?](#433-how-does-the-wal-affect-replicas-and-backups-and-how-can-you-reduce-its-volume)
- [434: Why can UPDATE that sets a column to the same value still cost a lot?](#434-why-can-update-that-sets-a-column-to-the-same-value-still-cost-a-lot)
- [435: What are the performance trade-offs of using natural keys versus surrogate keys?](#435-what-are-the-performance-trade-offs-of-using-natural-keys-versus-surrogate-keys)
- [436: How do you size and tune autovacuum for a large, write-heavy database?](#436-how-do-you-size-and-tune-autovacuum-for-a-large-write-heavy-database)
- [437: What is the difference between logical and physical reads, and why does it matter for tuning?](#437-what-is-the-difference-between-logical-and-physical-reads-and-why-does-it-matter-for-tuning)
- [438: How do you reason about the cost of an index before creating it?](#438-how-do-you-reason-about-the-cost-of-an-index-before-creating-it)
- [439: What is a "loose index scan" and how do you emulate it in PostgreSQL?](#439-what-is-a-loose-index-scan-and-how-do-you-emulate-it-in-postgresql)
- [440: How do you handle the "latest value per device" query on a huge table?](#440-how-do-you-handle-the-latest-value-per-device-query-on-a-huge-table)
- [441: What is the risk of using SELECT FOR UPDATE on rows found through a range scan in InnoDB?](#441-what-is-the-risk-of-using-select-for-update-on-rows-found-through-a-range-scan-in-innodb)
- [442: Why is it a problem to call external services inside a database transaction?](#442-why-is-it-a-problem-to-call-external-services-inside-a-database-transaction)
- [443: What is the outbox pattern and how does it relate to database load?](#443-what-is-the-outbox-pattern-and-how-does-it-relate-to-database-load)
- [444: How do column stores differ from row stores for analytical queries?](#444-how-do-column-stores-differ-from-row-stores-for-analytical-queries)
- [445: How does the choice of isolation level affect replication consistency on replicas?](#445-how-does-the-choice-of-isolation-level-affect-replication-consistency-on-replicas)
- [446: How can you reduce lock waits caused by foreign keys on hot parent rows?](#446-how-can-you-reduce-lock-waits-caused-by-foreign-keys-on-hot-parent-rows)
- [447: What should a team do to keep database performance good over time?](#447-what-should-a-team-do-to-keep-database-performance-good-over-time)
- [448: How do you explain a query plan problem to someone who isn't a database expert?](#448-how-do-you-explain-a-query-plan-problem-to-someone-who-isnt-a-database-expert)
- [449: What are common myths about SQL performance?](#449-what-are-common-myths-about-sql-performance)
- [450: If you had one week to improve the performance of an unfamiliar database, what would you do?](#450-if-you-had-one-week-to-improve-the-performance-of-an-unfamiliar-database-what-would-you-do)

---

# Easy Questions (1-150)

## 1: What does SQL query optimization mean?

It means making queries return the same result while using less time, CPU, memory and disk I/O. Usually you do it by adding the right indexes, rewriting the query so the database can use those indexes, fetching less data, and fixing the schema or server settings when needed. The rule is simple: measure, change one thing, measure again.

## 2: What are the most common reasons a SQL query is slow?

- A missing index, so the database reads the whole table.
- The query is written in a way that can't use an existing index (a function on the column, a type mismatch, a leading `%` in `LIKE`).
- It returns or processes far more rows than needed.
- Old or wrong statistics, so the planner picks a bad plan.
- Waiting on locks held by other transactions.
- Too little memory, so sorts and joins spill to disk.
- The app runs too many queries (the N+1 problem).

## 3: What is an index?

An index is a separate data structure that stores the values of one or more columns in sorted order, with a pointer to the matching row. It works like the index at the back of a book: instead of reading every page, you look up the word and jump to the right page. Most indexes in PostgreSQL and MySQL are B-tree indexes.

## 4: How does a B-tree index make a lookup faster?

A B-tree keeps keys sorted in a balanced tree of pages. To find a value, the database starts at the root page and follows one branch down to a leaf page, so it reads only a few pages even for millions of rows (the tree is usually 3-4 levels deep). Because the leaves are sorted and linked, the same index also works for range conditions (`>`, `<`, `BETWEEN`) and for `ORDER BY`.

## 5: What is a full table scan?

A full table scan (in PostgreSQL, a sequential scan) means the database reads every row of the table to find the ones that match. On a small table this is fine and can even be the fastest option. On a big table it is often the reason a query is slow, and the usual fix is an index on the filtered column.

## 6: What are the downsides of indexes?

- Every `INSERT`, `UPDATE` and `DELETE` must also update each index, so writes get slower.
- Indexes take disk space and memory.
- The planner has more options to consider.
- Unused indexes are pure cost.

So you add indexes for the queries you actually run, not for every column.

## 7: How do you create an index?

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
```

In PostgreSQL, use `CONCURRENTLY` on a busy table so writes are not blocked while the index builds:

```sql
CREATE INDEX CONCURRENTLY idx_orders_customer_id ON orders (customer_id);
```

## 8: Is a primary key indexed automatically?

Yes. Both PostgreSQL and MySQL create a unique index for the primary key. In MySQL InnoDB, the table itself is stored in primary key order (it is the clustered index). In PostgreSQL, the table is a heap and the primary key is a normal separate B-tree index.

## 9: Are foreign key columns indexed automatically?

In PostgreSQL, no. The referenced (parent) column must have a unique index, but the referencing (child) column does not get one. You usually need to add it yourself, or joins and deletes on the parent will be slow. MySQL InnoDB creates an index on the foreign key column automatically if one does not already exist.

## 10: What is a unique index?

A unique index does not allow two rows with the same value in the indexed columns. It enforces a rule and also speeds up lookups. The planner knows that at most one row can match, which helps it pick better join plans.

```sql
CREATE UNIQUE INDEX idx_users_email ON users (email);
```

## 11: What is a composite index?

A composite (multi-column) index covers more than one column, for example `(customer_id, created_at)`. It is sorted by the first column, then by the second inside each first value, and so on. It helps queries that filter on the first column, or on the first column and then the next ones.

```sql
CREATE INDEX idx_orders_customer_created ON orders (customer_id, created_at);
```

## 12: What is the leftmost prefix rule?

A composite index on `(a, b, c)` can be used efficiently for filters on `a`, on `a` and `b`, or on `a`, `b` and `c`. It is much less useful for a filter only on `b` or only on `c`, because the index is sorted by `a` first. Newer versions can sometimes use "skip scan" (MySQL 8.0.13+, PostgreSQL 18+) to work around a missing leading column, but only when the first column has few distinct values.

## 13: What is EXPLAIN?

`EXPLAIN` shows the plan the database will use to run a query: which tables it reads, in what order, with which indexes, and which join and sort methods. It does not run the query. It is the first tool you use to understand why a query is slow.

```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;
```

## 14: What is the difference between EXPLAIN and EXPLAIN ANALYZE?

`EXPLAIN` shows the estimated plan without running the query. `EXPLAIN ANALYZE` actually runs it and shows real row counts and real timings next to the estimates. Be careful: `EXPLAIN ANALYZE` on an `UPDATE` or `DELETE` really changes data, so wrap it in a transaction and roll back.

```sql
BEGIN;
EXPLAIN ANALYZE DELETE FROM logs WHERE created_at < '2024-01-01';
ROLLBACK;
```

## 15: What is a query plan?

A query plan (execution plan) is the list of steps the database takes to produce the result, shown as a tree. Leaf nodes read data (scans), and upper nodes join, sort, group or limit it. The same SQL can have many possible plans, and the database picks the one it thinks is cheapest.

## 16: What is the query planner (optimizer)?

The planner is the part of the database that turns your SQL into a plan. It looks at the possible ways to run the query (which indexes, which join order, which join method), estimates the cost of each using table statistics, and picks the cheapest one. Most slow queries come from the planner not having a good option (missing index) or having wrong information (bad estimates).

## 17: What is cost-based optimization?

The planner gives each possible plan a cost number based on how many pages it expects to read, how many rows it expects to process, and settings like `random_page_cost` in PostgreSQL. It then picks the plan with the lowest cost. The cost is not in milliseconds. It is a relative number used only to compare plans for the same query.

## 18: What are table statistics?

Statistics are summary data the database keeps about each table and column: number of rows, number of distinct values, most common values, a histogram of value spread, and the share of NULLs. The planner uses them to guess how many rows each step will return. If statistics are old, the guesses are wrong and the plan can be bad.

## 19: How do you update table statistics?

PostgreSQL:

```sql
ANALYZE orders;
```

MySQL:

```sql
ANALYZE TABLE orders;
```

Both databases also refresh statistics automatically (autovacuum in PostgreSQL, persistent stats auto recalculation in InnoDB), but after a big data load or delete it is a good idea to run it by hand.

## 20: Why should you avoid SELECT *?

- It sends columns you don't need over the network.
- It can stop the database from using an index-only scan, because it has to visit the table to get every column.
- It reads large columns (text, JSON, blobs) that may be stored separately and are expensive to fetch.
- Your code can break or slow down when someone adds a column.

List only the columns you need.

## 21: What is the slow query log in MySQL?

It is a log of queries that take longer than `long_query_time` seconds. You turn it on, wait, and then look at which queries show up most often or take the most total time. `mysqldumpslow` or `pt-query-digest` can group similar queries together.

```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 0.5;
```

## 22: How do you find slow queries in PostgreSQL?

- Set `log_min_duration_statement` (for example to `500ms`) to log every query slower than that.
- Use the `pg_stat_statements` extension, which tracks total time, calls and mean time for each normalized query.
- Look at `pg_stat_activity` for queries running right now.

```sql
SELECT query, calls, total_exec_time, mean_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

## 23: What is the N+1 query problem?

It happens when code runs one query to get a list of N rows, then runs one more query for each row to get related data. For 100 orders you end up with 101 queries. Each query might be fast, but the round trips add up and the page gets slow. It is very common with ORMs and lazy loading.

## 24: How do you fix the N+1 problem?

Load the related data in one go. Use a `JOIN`, or one extra query with `IN (...)` for all the IDs at once. Most ORMs have a way to do this, like `include` in Prisma, `select_related`/`prefetch_related` in Django, or `JOIN FETCH` in JPA.

```sql
SELECT * FROM order_items WHERE order_id IN (1, 2, 3, 4, 5);
```

## 25: What does sargable mean?

A sargable condition ("search argument able") is one the database can answer by seeking into an index. `created_at >= '2026-01-01'` is sargable. `YEAR(created_at) = 2026` is not, because the database has to compute `YEAR()` for every row before comparing. Writing sargable conditions is one of the easiest wins in query tuning.

## 26: Why does wrapping a column in a function stop the index from being used?

The index stores the raw column values, not the result of the function. For `WHERE LOWER(email) = 'a@b.com'`, the index on `email` is sorted by the original value, so the database can't seek into it. Fix it by rewriting the condition, or by creating an index on the expression.

```sql
-- Instead of WHERE DATE(created_at) = '2026-05-01'
WHERE created_at >= '2026-05-01' AND created_at < '2026-05-02'
```

## 27: Why doesn't LIKE '%abc' use a normal index?

A B-tree index is sorted from the first character. `LIKE 'abc%'` knows where to start in the sorted list, so it can use the index. `LIKE '%abc'` or `LIKE '%abc%'` can start anywhere in the string, so the database has to check every row. For contains-style search, use a trigram index (`pg_trgm` in PostgreSQL) or full-text search.

## 28: How does LIMIT help performance?

`LIMIT` tells the database it needs only a few rows. If an index matches the `ORDER BY`, the database can read the first rows from the index and stop early instead of reading and sorting the whole result. Without a matching index, it still has to find and sort all matching rows before it can return the top ones, so `LIMIT` alone does not always help.

## 29: Why is OFFSET pagination slow on later pages?

With `LIMIT 20 OFFSET 100000`, the database still has to find and step over the first 100,000 rows before returning 20. The deeper the page, the slower the query. It can also show duplicates or skip rows if data changes between page loads.

## 30: What is keyset pagination?

Keyset (cursor) pagination remembers the last row the user saw and asks for rows after it. With an index on the sort column, every page is as fast as the first one.

```sql
SELECT id, title, created_at
FROM posts
WHERE (created_at, id) < ('2026-11-01 10:00:00', 5321)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

The downside is that you can't jump straight to page 500.

## 31: Should a filter go in WHERE or HAVING?

Put it in `WHERE` whenever possible. `WHERE` filters rows before grouping, so fewer rows get grouped. `HAVING` filters after grouping and should be used only for conditions on aggregates like `COUNT(*) > 5`.

```sql
-- Better
SELECT status, COUNT(*) FROM orders WHERE status <> 'cancelled' GROUP BY status;
```

## 32: Why do joins get slow?

Joins get slow when the database has to compare a lot of rows, for example when the join column has no index, when one side is filtered poorly so huge row sets are joined, or when the planner picks the wrong join order because of bad estimates. Joins on columns with different data types can also stop index use.

## 33: Should you index join columns?

Usually yes, at least on the side that gets looked up. If you join `orders.customer_id = customers.id`, `customers.id` is already the primary key, but `orders.customer_id` often needs its own index, especially when you go from a customer to their orders.

## 34: Is INNER JOIN faster than LEFT JOIN?

Not by itself, but `INNER JOIN` gives the planner more freedom. With an inner join it can reorder the tables in any way, while a `LEFT JOIN` forces some order. Use `LEFT JOIN` only when you really need rows with no match. Also, a `WHERE` condition on the right table of a `LEFT JOIN` silently turns it into an inner join.

## 35: What is normalization?

Normalization means splitting data into tables so each fact is stored once, for example keeping customer details in `customers` and referring to them by ID from `orders`. It avoids duplicated data and update mistakes. The trade-off is that reading often needs joins.

## 36: What is denormalization and when should you use it?

Denormalization means storing some data more than once on purpose to make reads faster, for example keeping `order_count` on the `customers` table or copying the customer name into `orders`. Use it when a read is very frequent and the join or aggregate is too slow, and accept that you now have to keep the copies in sync.

## 37: How do data types affect performance?

Smaller types mean smaller rows and indexes, so more of them fit in memory and fewer pages are read. Use `integer` instead of `bigint` when the range is enough, `date` instead of `timestamp` when you don't need time, and proper numeric or date types instead of text. Comparing numbers is also faster than comparing strings.

## 38: Why shouldn't you store dates or numbers as strings?

String comparison is slower and sorts wrong (`'10'` comes before `'9'`). Range queries like "last 7 days" don't work well, and the database can't check the values are valid. You also end up converting the values in queries, which breaks index use.

## 39: What is implicit type conversion and why is it bad for performance?

It happens when you compare values of different types and the database converts one side for you. If it converts the column, the index on that column can't be used. A classic MySQL example is a `VARCHAR` phone column compared to a number: `WHERE phone = 5551234` converts every row. Pass values with the same type as the column.

```sql
-- Bad: phone is VARCHAR
SELECT * FROM users WHERE phone = 5551234;
-- Good
SELECT * FROM users WHERE phone = '5551234';
```

## 40: What is a covering index?

A covering index contains every column the query needs, so the database can answer from the index alone without reading the table. In PostgreSQL you can add extra non-key columns with `INCLUDE`.

```sql
CREATE INDEX idx_orders_customer ON orders (customer_id) INCLUDE (total, status);
SELECT total, status FROM orders WHERE customer_id = 42;
```

## 41: What is an index-only scan?

It is a plan step where the database gets all the data from the index and skips the table. It is much faster because the table pages are not touched. In PostgreSQL it also needs the visibility map to be up to date (VACUUM keeps it current), otherwise it still has to check the table for row visibility. In MySQL EXPLAIN it shows up as `Using index`.

## 42: What is index selectivity?

Selectivity is how well an index narrows down the rows. A column like `email` with all unique values is highly selective. A column like `is_active` with two values is not. The planner uses an index when it expects to return a small share of the table. For low-selectivity columns, a full scan is often cheaper.

## 43: When will the database ignore an index even though one exists?

- The query returns a big part of the table, so a full scan is cheaper.
- The column is wrapped in a function or converted to another type.
- `LIKE` starts with `%`.
- The index columns are in the wrong order for the query.
- Statistics are wrong, so the planner thinks the index won't help.
- The table is tiny.

## 44: What is the difference between a clustered and a non-clustered index?

A clustered index decides the physical order of the rows, so the table data lives inside it. MySQL InnoDB always clusters the table on the primary key. A non-clustered (secondary) index is a separate structure that points to the rows. In InnoDB, a secondary index stores the primary key value, so a lookup goes through the secondary index and then the primary key.

## 45: How is a PostgreSQL table stored?

PostgreSQL stores table rows in a heap, which has no special order. Every index, including the primary key, is separate and points to a row location (a TID). Updates write a new version of the row instead of changing it in place, which is how PostgreSQL supports MVCC.

## 46: What is the difference between a sequential scan, an index scan and a bitmap scan?

- **Sequential scan:** read every page of the table in order.
- **Index scan:** walk the index and fetch each matching row from the table one by one. Good for few rows.
- **Bitmap scan:** collect matching row locations from one or more indexes into a bitmap, sort them by page, then read those pages in order. Good for a medium number of rows, and it can combine several indexes.

## 47: Why is inserting rows one by one slow?

Each single-row `INSERT` is a round trip to the server, and in autocommit mode each one is also its own transaction that has to be flushed to disk. Inserting many rows per statement, or many statements in one transaction, cuts that overhead a lot.

```sql
INSERT INTO events (user_id, type) VALUES
  (1, 'login'), (2, 'login'), (3, 'logout');
```

## 48: Why can many small transactions be slow?

Each commit has to make the change durable, which usually means writing and flushing the log (WAL in PostgreSQL, redo log in InnoDB) to disk. Thousands of tiny commits per second can be limited by disk flush speed. Grouping related writes into one transaction reduces the number of flushes.

## 49: How does transaction length affect performance?

Long transactions hold locks longer, so other queries wait. In PostgreSQL they also stop VACUUM from cleaning up dead rows, which causes bloat. In MySQL they keep old row versions in the undo log longer. Keep transactions short, and never wait for user input or an HTTP call inside one.

## 50: What is a lock in a database?

A lock stops other transactions from changing (or sometimes reading) data while one transaction works on it. Row locks are taken by `UPDATE`, `DELETE` and `SELECT ... FOR UPDATE`. Table locks are taken by some schema changes. Locks keep data correct, but when many sessions want the same rows, they wait for each other and queries get slow even if the SQL itself is fine.

## 51: What is a deadlock?

A deadlock happens when two transactions each hold a lock the other one needs, so neither can continue. For example, transaction A locks row 1 and waits for row 2, while transaction B locks row 2 and waits for row 1. The database detects this and cancels one of them with an error. The app should retry, and you reduce deadlocks by always locking rows in the same order.

## 52: What is connection pooling?

A connection pool keeps a set of open database connections and hands them out to requests, instead of opening a new connection for every request. It saves the cost of connecting and stops the app from opening more connections than the database can handle. Examples are PgBouncer for PostgreSQL, ProxySQL for MySQL, and the built-in pools in most drivers.

## 53: Why is opening a new database connection expensive?

It needs a network handshake, often TLS, and authentication. In PostgreSQL each connection is a separate server process, which uses memory and takes time to start. Opening a connection per request can take longer than the query itself, and thousands of connections can slow the whole server down.

## 54: What is a prepared statement and does it help performance?

A prepared statement sends the SQL once with placeholders, then runs it many times with different values. The server can skip parsing (and sometimes planning) on later runs, which saves time for queries that run very often. The bigger reason to use them is safety: they prevent SQL injection.

```sql
PREPARE get_user (int) AS SELECT * FROM users WHERE id = $1;
EXECUTE get_user(42);
```

## 55: Does MySQL have a query cache?

Not anymore. The query cache was removed in MySQL 8.0 because it did not scale: every write to a table cleared all cached results for that table, and the cache had a global lock. Today you cache results in the application or in something like Redis. PostgreSQL never had a result cache like that.

## 56: How can application-level caching help database performance?

If the same data is read often and changes rarely, you can store the result in memory (in the app, in Redis, or in a CDN for API responses) and skip the database for most reads. The hard part is invalidation: deciding when cached data is stale. Cache only what can be a little out of date, or clear the cache when the data changes.

## 57: Does a view make a query faster?

No. A normal view is just a saved query. When you select from it, the database puts the view's SQL into your query and plans the whole thing. It helps with code reuse, not speed. A view that joins many tables can even make things slower if you only need one of them, although the planner can sometimes remove unused joins.

## 58: What is a materialized view?

A materialized view stores the result of a query on disk, like a table. Reads are fast because the work is already done, but the data is only as fresh as the last refresh. It is good for heavy reports and dashboards.

```sql
CREATE MATERIALIZED VIEW daily_sales AS
SELECT date_trunc('day', created_at) AS day, SUM(total) AS revenue
FROM orders GROUP BY 1;

REFRESH MATERIALIZED VIEW daily_sales;
```

MySQL does not have materialized views; you use a summary table that you update yourself.

## 59: What is a subquery?

A subquery is a query inside another query, for example in `WHERE`, in `FROM`, or in the `SELECT` list. A correlated subquery refers to columns from the outer query, so in the worst case it runs once per outer row. Modern planners turn many subqueries into joins, but not all of them.

## 60: Is a JOIN faster than a subquery?

Often they end up the same, because the planner rewrites many subqueries as joins. When it can't, a correlated subquery that runs once per row can be much slower than a join. Check the plan with `EXPLAIN` instead of assuming. Write whichever form is clearer, then rewrite only if the plan is bad.

## 61: What is the difference between IN and EXISTS?

`IN` checks if a value is in a list or in the result of a subquery. `EXISTS` checks if a subquery returns at least one row and stops at the first match. Modern PostgreSQL and MySQL usually plan both as a semi-join, so speed is often the same. `EXISTS` is a safe choice for "is there any related row" checks.

```sql
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

## 62: What is the problem with NOT IN and NULL?

If the subquery in `NOT IN` returns even one `NULL`, the whole condition becomes unknown and the query returns no rows. Because of this rule, the planner also has a harder time turning `NOT IN` into a fast anti-join. Use `NOT EXISTS` instead; it handles NULLs the way people expect and plans well. (PostgreSQL 19 can turn some `NOT IN` cases into anti-joins when it can prove no NULLs are possible.)

```sql
SELECT * FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

## 63: What is the difference between UNION and UNION ALL?

`UNION` removes duplicate rows, which needs a sort or a hash step over the whole result. `UNION ALL` just appends the results. If you know there are no duplicates, or you don't care, use `UNION ALL`; it is faster and uses less memory.

## 64: Why can DISTINCT be expensive?

To remove duplicates the database has to sort or hash all the rows, which takes memory and can spill to disk. `DISTINCT` is often added to hide duplicates caused by a wrong join. Fix the join (for example use `EXISTS`) instead of piling `DISTINCT` on top.

## 65: What is the difference between COUNT(*), COUNT(1) and COUNT(column)?

`COUNT(*)` and `COUNT(1)` both count rows and perform the same in PostgreSQL and MySQL. `COUNT(column)` counts only rows where that column is not NULL, so it can give a different answer and sometimes has to read the column. Use `COUNT(*)` when you want the number of rows.

## 66: Why is SELECT COUNT(*) slow on a big PostgreSQL table?

Because of MVCC, different transactions can see different rows, so PostgreSQL can't keep a single stored row count. It has to scan the table or an index to count the visible rows. If an approximate number is enough, read the planner's estimate:

```sql
SELECT reltuples::bigint AS estimate FROM pg_class WHERE relname = 'orders';
```

For exact counts that are needed often, keep a counter in a separate table.

## 67: Why is ORDER BY sometimes slow?

Sorting needs all the matching rows before it can return the first one. If the rows don't fit in the sort memory (`work_mem` in PostgreSQL, `sort_buffer_size` in MySQL), the sort spills to temporary files on disk. Sorting large text values is also slower than sorting numbers.

## 68: How can an index remove the need to sort?

A B-tree index is already sorted, so if the index order matches the `ORDER BY`, the database can read rows in that order and skip the sort step. Combined with `LIMIT`, this means reading only a few rows.

```sql
CREATE INDEX idx_posts_created ON posts (created_at DESC);
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10;
```

## 69: How does the database run GROUP BY?

It uses one of two main methods. **Hash aggregate** builds a hash table with one entry per group, which is fast when the number of groups fits in memory. **Sort (group) aggregate** sorts the rows by the group key and then counts each run of equal values; it can use an index that is already sorted. You see which one was picked in `EXPLAIN`.

## 70: What is a temporary table and when does it help?

A temporary table exists only for the current session and is dropped at the end. It helps when you have a complex multi-step job: you compute a middle result once, maybe index it, and then use it in later queries instead of repeating the same heavy subquery. Remember to run `ANALYZE` on it in PostgreSQL, since autovacuum does not process temp tables.

## 71: What is a CTE?

A CTE (common table expression) is a named subquery written with `WITH`. It makes long queries easier to read and can be recursive.

```sql
WITH recent AS (
  SELECT * FROM orders WHERE created_at > now() - interval '7 days'
)
SELECT customer_id, COUNT(*) FROM recent GROUP BY customer_id;
```

## 72: Do CTEs make queries slower?

Not usually anymore. Before PostgreSQL 12, every CTE was computed on its own and stored, so filters from the outer query could not be pushed into it. Since PostgreSQL 12, a CTE that is used once and has no side effects is inlined like a subquery. You can still force either behavior with `MATERIALIZED` or `NOT MATERIALIZED`. MySQL 8+ also merges or materializes CTEs based on cost.

## 73: What is table partitioning?

Partitioning splits one big table into smaller pieces (partitions) by a key, often a date range. Queries that filter on that key only read the matching partitions (partition pruning), and old data can be dropped by dropping a whole partition, which is much faster than a big `DELETE`. To your app it still looks like one table.

```sql
CREATE TABLE events (id bigint, created_at timestamptz, data jsonb)
PARTITION BY RANGE (created_at);

CREATE TABLE events_2026_11 PARTITION OF events
FOR VALUES FROM ('2026-11-01') TO ('2026-12-01');
```

## 74: What is the difference between partitioning and sharding?

Partitioning splits a table into pieces on the same database server. Sharding splits data across several separate servers, with each server holding part of the rows. Sharding spreads load and storage over more machines but adds a lot of complexity: cross-shard queries, transactions and rebalancing. Try indexes, partitioning, caching and read replicas first.

## 75: What is a read replica?

A read replica is a copy of the main database that receives changes through replication and serves read-only queries. You send reads (reports, listings) to replicas and writes to the primary, which takes load off the primary. It does not help with write load.

## 76: What is replication lag?

Replication lag is the delay between a change on the primary and that change showing up on the replica. If a user saves something and the next page reads from a lagging replica, they won't see their change. Common fixes are reading from the primary right after a write, or waiting until the replica has caught up.

## 77: What is VACUUM in PostgreSQL?

When a row is updated or deleted in PostgreSQL, the old version stays in the table as a dead row. `VACUUM` marks the space used by dead rows as free for reuse, updates the visibility map (needed for index-only scans), and prevents transaction ID wraparound. Plain `VACUUM` does not lock out reads or writes.

## 78: What is autovacuum?

Autovacuum is a background process in PostgreSQL that runs `VACUUM` and `ANALYZE` automatically when enough rows in a table have changed. It should almost always stay on. On busy tables you often have to tune it to run more often, otherwise dead rows pile up and tables bloat.

## 79: What is table bloat?

Bloat is wasted space inside a table or index: dead rows or empty space that hasn't been reused. A bloated table has more pages to read, so scans get slower and less of the useful data fits in memory. It is caused by heavy updates and deletes with vacuum not keeping up, or by long transactions blocking cleanup.

## 80: What is MVCC?

MVCC (multi-version concurrency control) means the database keeps several versions of a row so readers don't block writers and writers don't block readers. Each transaction sees a consistent snapshot of the data. The cost is that old versions must be cleaned up later: by VACUUM in PostgreSQL and by the purge thread in InnoDB.

## 81: What is the buffer pool or shared buffers?

It is the memory area where the database keeps recently used table and index pages. Reading from memory is much faster than reading from disk, so if your working data fits in this cache, most queries avoid disk entirely. In MySQL it is `innodb_buffer_pool_size`; in PostgreSQL it is `shared_buffers`, plus the operating system file cache.

## 82: Why is disk I/O usually the biggest cost in a query?

CPU and memory work is cheap compared to reading pages from disk, even on SSDs. Most optimizations come down to reading fewer pages: using indexes to skip rows, keeping rows and indexes small, and keeping the hot data in memory. That is why plans are compared mainly by how many pages they read.

## 83: What is a page (block) in a database?

A page is the unit the database reads from and writes to disk: 8 KB in PostgreSQL and 16 KB by default in InnoDB. Even if you need one row, the whole page is read. Smaller rows mean more rows per page and fewer pages to read for the same data.

## 84: What is a partial index?

A partial index covers only the rows that match a condition. It is smaller and faster to maintain, and great when queries always filter on the same condition. PostgreSQL supports it directly; MySQL does not.

```sql
CREATE INDEX idx_orders_pending ON orders (created_at)
WHERE status = 'pending';
```

## 85: What is an expression (functional) index?

It is an index on the result of an expression instead of a raw column. Queries that use the same expression can then use the index.

```sql
-- PostgreSQL
CREATE INDEX idx_users_lower_email ON users (LOWER(email));
-- MySQL 8.0.13+
CREATE INDEX idx_users_lower_email ON users ((LOWER(email)));

SELECT * FROM users WHERE LOWER(email) = 'ann@example.com';
```

## 86: How do you find unused indexes?

PostgreSQL tracks how many times each index was scanned:

```sql
SELECT relname, indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0;
```

In MySQL, use `sys.schema_unused_indexes`. Check over a long enough period (and on replicas too) before dropping, because an index might only be used by a monthly report.

## 87: How can an ORM cause slow SQL?

- N+1 queries from lazy loading.
- Selecting every column when you need two.
- Loading thousands of rows into memory to count them or filter them in code.
- Generating queries with functions or casts that break index use.
- Running many small writes instead of one batch.

The ORM is not the problem by itself, but you have to look at the SQL it generates.

## 88: How do you see the SQL an ORM generates?

Turn on query logging in the ORM (for example `log: ['query']` in Prisma, `echo=True` in SQLAlchemy, `DEBUG` SQL logging in Hibernate), or look at the database side with `pg_stat_statements`, the slow query log, or `pg_stat_activity`. Then copy the query and run `EXPLAIN` on it.

## 89: How do you set a time limit for queries?

Set a timeout so a bad query can't run forever and hold connections and locks.

```sql
-- PostgreSQL, per session or per role
SET statement_timeout = '5s';

-- MySQL, SELECT only, in milliseconds
SET SESSION max_execution_time = 5000;
```

You can also set them per user, which is useful for app accounts versus reporting accounts.

## 90: What is the fastest way to check if a row exists?

Use `EXISTS`, which stops at the first match, instead of `COUNT(*)`, which counts every match.

```sql
SELECT EXISTS (SELECT 1 FROM orders WHERE customer_id = 42);
```

## 91: What is the difference between DELETE and TRUNCATE for performance?

`DELETE` removes rows one by one, writes each change to the log, fires triggers, and (in PostgreSQL) leaves dead rows for vacuum. `TRUNCATE` removes all rows at once by dropping the table's data files, so it is almost instant. `TRUNCATE` takes a strong lock and can't have a `WHERE` clause.

## 92: How do you delete millions of rows without hurting the database?

Delete in small batches, with a short pause between them, so each transaction is short, locks are released quickly, and replicas and vacuum can keep up.

```sql
-- PostgreSQL, repeat until 0 rows deleted
DELETE FROM logs
WHERE id IN (
  SELECT id FROM logs WHERE created_at < '2025-01-01' LIMIT 5000
);
```

If the data is partitioned by date, just drop the old partition.

## 93: What is the fastest way to load a lot of data?

Use the bulk loading tools: `COPY` in PostgreSQL and `LOAD DATA INFILE` in MySQL. They are much faster than `INSERT` statements. For very large loads it also helps to drop or delay secondary indexes and build them after loading, then run `ANALYZE`.

```sql
COPY orders (id, customer_id, total) FROM '/data/orders.csv' WITH (FORMAT csv, HEADER);
```

## 94: What is an upsert?

An upsert inserts a row, or updates it if it already exists, in one statement. It is faster and safer than "select, then insert or update" from the app, which needs two round trips and has race conditions.

```sql
-- PostgreSQL
INSERT INTO stock (product_id, qty) VALUES (1, 5)
ON CONFLICT (product_id) DO UPDATE SET qty = stock.qty + EXCLUDED.qty;

-- MySQL
INSERT INTO stock (product_id, qty) VALUES (1, 5) AS new
ON DUPLICATE KEY UPDATE qty = stock.qty + new.qty;
```

## 95: How do OR conditions affect index use?

`WHERE a = 1 OR b = 2` can't use a single index on `a` alone. The database may combine two indexes (bitmap OR in PostgreSQL, index merge in MySQL), or it may fall back to a full scan. If that happens, rewriting as a `UNION ALL` of two indexed queries (taking care of rows that match both) can be much faster. `OR` on the same column is fine; it is the same as `IN`.

## 96: Can an index be used for IS NULL?

Yes, in both PostgreSQL and MySQL a B-tree index stores NULLs, so `WHERE col IS NULL` can use it. If you only ever look up the NULL rows, a partial index in PostgreSQL is even better: `CREATE INDEX ... ON tasks (id) WHERE finished_at IS NULL`.

## 97: What is a nested loop join?

For each row from the outer table, the database looks up matching rows in the inner table. It is very fast when the outer side has few rows and the inner side has an index on the join column. It is very slow when both sides are large and there is no index, because the work grows as outer rows times inner rows.

## 98: What is a hash join?

The database reads the smaller table and builds an in-memory hash table on the join key, then scans the bigger table and looks up each row in the hash table. It is good for joining large sets on equality conditions and doesn't need indexes. It needs memory; if the hash table doesn't fit, it spills to disk in batches. MySQL has supported hash joins since 8.0.18.

## 99: What is a merge join?

Both inputs are sorted on the join key, then the database walks through them side by side, like merging two sorted lists. It is efficient for large inputs that are already sorted (for example from an index). If the inputs have to be sorted first, that sort can be expensive. PostgreSQL uses merge joins; MySQL does not.

## 100: What does the rows number mean in EXPLAIN?

It is the planner's estimate of how many rows that step will return. In `EXPLAIN ANALYZE` you also see the real number. A big gap between estimated and actual rows (for example 10 estimated and 500,000 actual) is the most common sign that the planner chose a bad plan because of wrong statistics.

## 101: What does cost mean in PostgreSQL EXPLAIN output?

Each node shows `cost=startup..total`. The startup cost is the work before the first row comes out (for example a sort must finish first). The total cost is the work to return all rows. The units are arbitrary, based on settings like `seq_page_cost = 1`, so you only use them to compare plans for the same query, not as time.

```
Seq Scan on orders  (cost=0.00..1834.00 rows=100000 width=40)
```

## 102: What does actual time mean in EXPLAIN ANALYZE?

`actual time=0.02..15.3` shows milliseconds until the first row and until the last row for that node, per loop. Also check `loops`: if a node ran 10,000 times, multiply its time by the loops to get the real total. Since PostgreSQL 18, `EXPLAIN ANALYZE` also shows buffer usage by default, which tells you how many pages were read from cache or disk.

## 103: What does Using filesort mean in MySQL EXPLAIN?

It means MySQL has to sort the rows itself because it can't read them in the needed order from an index. The name is misleading: the sort can happen in memory, and it uses disk only if the data is too big. On a large result it is a hint that an index matching the `ORDER BY` could help.

## 104: What does Using temporary mean in MySQL EXPLAIN?

MySQL needs an internal temporary table to run the query, often for `GROUP BY`, `DISTINCT`, `UNION` or sorting on columns from different tables. It's fine for small results, but on big ones it costs memory and may go to disk. An index that matches the `GROUP BY` columns can often remove it.

## 105: What does the type column mean in MySQL EXPLAIN?

It shows how MySQL reads each table. From best to worst, roughly:

- `const` / `system`: at most one row, found by primary key or unique key.
- `eq_ref`: one row per row of the previous table, through a unique index.
- `ref`: several rows through a non-unique index.
- `range`: an index range scan (`BETWEEN`, `>`, `IN`).
- `index`: a full scan of the index.
- `ALL`: a full table scan.

`ALL` on a big table is usually the first thing to fix.

## 106: What do possible_keys and key mean in MySQL EXPLAIN?

`possible_keys` lists the indexes MySQL could use for that table. `key` is the one it actually chose. If `possible_keys` has values but `key` is NULL, MySQL decided a full scan was cheaper. If `possible_keys` is NULL, no index fits the query at all.

## 107: Why can very wide tables be slow?

A table with dozens of columns and large text or JSON fields has big rows, so fewer rows fit on each page. Every scan reads more pages and less of the table fits in memory, even for queries that need only a few columns. Moving rarely used or large columns to a separate table can help the common queries.

## 108: Should you store large files in the database?

Usually not. Images, PDFs and videos make tables and backups huge, fill the cache with data that is rarely queried, and slow down replication. Store files in object storage (like S3) and keep only the path, size and metadata in the database.

## 109: What is pg_stat_activity?

It is a PostgreSQL view that shows one row per connection: who is connected, what query is running, when it started, its state, and what it is waiting on. It is the first place to look when the database is slow right now.

```sql
SELECT pid, now() - query_start AS runtime, state, wait_event_type, query
FROM pg_stat_activity
WHERE state <> 'idle'
ORDER BY runtime DESC;
```

## 110: How do you see running queries in MySQL?

Use `SHOW PROCESSLIST` (or `SHOW FULL PROCESSLIST` for the whole query text), or query `performance_schema.processlist`, which avoids a global lock. The `Time` column shows how long each query has been running and `State` shows what it is doing.

## 111: How do you stop a long-running query?

PostgreSQL:

```sql
SELECT pg_cancel_backend(12345);    -- cancel the query
SELECT pg_terminate_backend(12345); -- close the whole connection
```

MySQL:

```sql
KILL QUERY 42;  -- cancel the query
KILL 42;        -- close the connection
```

Cancelling a big write rolls it back, which can also take time.

## 112: Is an index on a boolean column useful?

Usually not on its own. If half the rows are `true` and half `false`, the index doesn't narrow things down and a full scan is cheaper. It helps only when one value is rare, for example `is_flagged = true` for 0.1% of rows. In PostgreSQL, a partial index (`WHERE is_flagged`) is the better choice for that.

## 113: Does the sort direction of an index matter?

For a single-column index, no: a B-tree can be read forward or backward. For a composite index it can matter. A query with `ORDER BY a ASC, b DESC` needs an index with the same mix of directions (or the exact opposite) to skip the sort.

```sql
CREATE INDEX idx_scores ON scores (game_id ASC, points DESC);
```

MySQL supports real descending indexes since 8.0.

## 114: Should you use auto-increment IDs or UUIDs as primary keys?

Auto-increment integers are small (4 or 8 bytes) and always insert at the end of the index, which keeps the index compact. Random UUIDs (v4) are 16 bytes and insert at random spots, which causes page splits, a bigger index and more cache misses, especially in InnoDB where the table is clustered on the key. If you need UUIDs, use time-ordered ones like UUIDv7.

## 115: What is UUIDv7 and why is it better for indexes?

UUIDv7 starts with a timestamp, so new values are roughly increasing, like an auto-increment ID. Inserts go to the end of the index, so you avoid the random page splits of UUIDv4 while keeping globally unique IDs. PostgreSQL 18 added a built-in `uuidv7()` function.

```sql
CREATE TABLE orders (id uuid PRIMARY KEY DEFAULT uuidv7(), total numeric);
```

## 116: Is CHAR faster than VARCHAR?

In PostgreSQL, no: `char(n)`, `varchar(n)` and `text` are stored the same way, and `char(n)` can even be slower because of padding. Just use `text` or `varchar`. In MySQL, `CHAR` can save a little for truly fixed-length values like country codes, but the difference is small.

## 117: Why does choosing the right integer size matter?

Every byte is repeated in every row and in every index that includes the column. A `bigint` foreign key in a table with a billion rows, plus a few indexes on it, adds many gigabytes compared to `int`. Use `int` when the range is enough, but use `bigint` for IDs of tables that may grow past 2 billion rows, because changing it later is painful.

## 118: How should you filter by date so an index can be used?

Use a range on the raw column instead of wrapping it in a function.

```sql
-- Can't use an index on created_at
WHERE EXTRACT(YEAR FROM created_at) = 2026

-- Can use the index
WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01'
```

Using `<` on the next day (instead of `<=` with 23:59:59) also avoids missing rows with fractional seconds.

## 119: How can adding an index lock a production table?

A normal `CREATE INDEX` in PostgreSQL blocks writes to the table until it finishes, which on a big table can mean minutes of failed requests. Use `CREATE INDEX CONCURRENTLY`, which takes longer but lets writes continue. In MySQL InnoDB, adding a secondary index is an online operation by default (`ALGORITHM=INPLACE, LOCK=NONE`).

## 120: Is adding a column to a big table slow?

Not anymore in most cases. Since PostgreSQL 11, adding a column with a constant default is instant because the default is stored in the catalog, not written to every row. MySQL 8.0 can add columns with `ALGORITHM=INSTANT`. Changing a column type, though, usually rewrites the whole table.

## 121: How do foreign keys affect write performance?

On every insert or update in the child table, the database checks that the parent row exists. On every delete or key update in the parent, it checks the child table for references. These checks are cheap with the right indexes, but without an index on the child column, each parent delete scans the whole child table. PostgreSQL 19 made foreign key checks faster for bulk inserts.

## 122: Do triggers slow down writes?

Yes. A trigger runs extra code for every affected row (or statement), inside the same transaction. A trigger that writes to an audit table doubles the writes. They also hide work from people reading the app code. Keep them small, and prefer statement-level triggers with transition tables in PostgreSQL for bulk changes.

## 123: Are stored procedures faster than queries from the app?

They can be when the work needs many queries in a row, because everything runs on the server without network round trips between steps. For a single query, there is little difference. The downside is that logic in the database is harder to test, version and scale out.

## 124: What is a chatty application and why is it slow?

A chatty app talks to the database in many tiny requests, for example running 50 queries to build one page. Even if each query takes 1 ms, network latency for each round trip adds up. Fewer, larger queries (joins, `IN` lists, batch inserts) are usually faster than many small ones.

## 125: Why should an API never return all rows of a table?

As the table grows, the query, the network transfer, the JSON encoding and the client all get slower, and memory use can crash the server. Always paginate list endpoints, set a maximum page size, and filter on the server instead of in the client.

## 126: How do you benchmark a database?

Use a load tool that runs a realistic mix of queries at a set level of concurrency and reports throughput and latency. `pgbench` comes with PostgreSQL and `sysbench` is common for MySQL. Test on data similar in size to production, warm up the cache first, and change only one thing between runs.

```bash
pgbench -i -s 50 mydb
pgbench -c 20 -j 4 -T 60 mydb
```

## 127: What is the difference between latency and throughput for a database?

Latency is how long one query takes. Throughput is how many queries the database finishes per second. They are related but not the same: adding more connections may raise throughput up to a point and then make latency much worse as queries wait for CPU, disk or locks.

## 128: Why look at p95 and p99 query times instead of the average?

The average hides the slow cases. If 99 queries take 2 ms and one takes 2 seconds, the average looks fine but some users wait 2 seconds. Percentiles like p95 and p99 show what the slowest 5% or 1% of requests feel like, and those are often caused by locks, cache misses or bad plans for certain values.

## 129: Which queries should you optimize first?

Sort queries by total time (calls times average time), not by the slowest single run. A 5 ms query that runs a million times a day costs more than a 10-second report that runs once. `pg_stat_statements` and `performance_schema` (or `sys.statement_analysis` in MySQL) give you this list.

## 130: Why should you measure before optimizing?

Guesses about what is slow are often wrong. Without numbers, you might add indexes that are never used or rewrite queries that were not the problem. Measure first (slow log, `pg_stat_statements`, `EXPLAIN ANALYZE`), fix the biggest problem, and measure again to confirm the change helped.

## 131: What is a hot row?

A hot row is a single row that many transactions update at the same time, like a global counter or a stock row for a popular product. Each update has to wait for the row lock held by the one before it, so the updates run one at a time. Fixes include splitting the counter into several rows and summing them, or collecting changes and applying them in batches.

## 132: What does SELECT ... FOR UPDATE do?

It reads rows and locks them so other transactions can't change or lock them until you commit. You use it when you read a value and then update it based on what you read. Lock as few rows as possible and keep the transaction short, because other sessions wanting those rows will wait.

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

## 133: What is a lock wait timeout?

It is the longest time a query will wait for a lock before giving up with an error. In MySQL it is `innodb_lock_wait_timeout` (50 seconds by default); in PostgreSQL it is `lock_timeout` (off by default). Setting a short lock timeout for schema changes is a good habit, so a migration fails fast instead of blocking everything behind it.

```sql
SET lock_timeout = '3s';
ALTER TABLE orders ADD COLUMN note text;
```

## 134: How does the isolation level affect performance?

Higher isolation levels give stronger guarantees but can cost more. `SERIALIZABLE` may cancel transactions that conflict, so you need retries. In MySQL, `REPEATABLE READ` (the default) uses gap locks on ranges, which can cause more lock waits than `READ COMMITTED`. Most web apps work fine with `READ COMMITTED` (the PostgreSQL default).

## 135: What are typical signs of a missing index?

- A full table scan (`Seq Scan` or `type: ALL`) on a big table in a query that returns few rows.
- A query that gets slower as the table grows.
- High rows examined compared to rows sent in the MySQL slow log.
- High `seq_scan` counts on a large table in `pg_stat_user_tables`.

## 136: How many indexes are too many?

There is no fixed number. Each index costs write time, disk and memory, so a write-heavy table should have few indexes and a read-mostly table can have more. A good rule is that every index should serve real, frequent queries. If you can't name the query an index is for, it is probably not needed.

## 137: What is a redundant index?

An index that another index already covers. If you have an index on `(customer_id, created_at)`, a separate index on just `(customer_id)` is usually redundant, because the composite index can serve the same lookups. Exact duplicates also happen, often created by ORMs or migrations. Drop them to save write time and space.

## 138: How do you index a low-cardinality column that is always filtered on?

Put it in a composite index together with a more selective column, in the order your queries use. For example, `WHERE tenant_id = ? AND status = 'open' ORDER BY created_at` fits an index on `(tenant_id, status, created_at)`. On its own, the `status` column wouldn't be worth indexing.

## 139: Why is LIKE '%word%' a bad way to build search?

It can't use a normal index, so it scans every row, and it doesn't handle word forms, ranking or typos. For real search, use the database's full-text search, a trigram index for fuzzy matching, or a separate search engine like Elasticsearch or OpenSearch for large or complex cases.

## 140: What is full-text search in PostgreSQL and MySQL?

It is built-in search that splits text into words, handles word forms, and can rank results, with a special index that makes it fast.

```sql
-- PostgreSQL
CREATE INDEX idx_posts_fts ON posts USING GIN (to_tsvector('english', body));
SELECT * FROM posts WHERE to_tsvector('english', body) @@ to_tsquery('english', 'index & tuning');

-- MySQL
ALTER TABLE posts ADD FULLTEXT INDEX ft_body (body);
SELECT * FROM posts WHERE MATCH(body) AGAINST ('index tuning');
```

## 141: Should you use json or jsonb in PostgreSQL?

Use `jsonb` in almost all cases. `json` stores the raw text and has to parse it on every access. `jsonb` stores a parsed binary form, so reading keys is faster, and it supports GIN indexes for containment and key searches. `json` is only useful if you must keep the exact original text, key order and duplicates.

## 142: What is a GIN index?

GIN (generalized inverted index) maps each element inside a value (a word, an array item, a JSON key or value) to the rows that contain it. It is used for full-text search, arrays and `jsonb` in PostgreSQL. Lookups are fast, but GIN indexes are bigger and slower to update than B-trees.

```sql
CREATE INDEX idx_products_attrs ON products USING GIN (attributes);
SELECT * FROM products WHERE attributes @> '{"color": "red"}';
```

## 143: What is the write-ahead log (WAL)?

Before changing data pages, the database writes a record of the change to a log on disk: the WAL in PostgreSQL, the redo log in InnoDB. If the server crashes, it replays the log to recover. The log is written sequentially, which is fast, and the data pages can be written later. The speed of flushing this log often limits how many commits per second the server can do.

## 144: What is a checkpoint?

A checkpoint is when the database writes all changed pages from memory to the data files, so older log records are no longer needed for recovery. Checkpoints cause bursts of disk writes. If they happen too often, write performance drops, so on busy servers you usually raise `max_wal_size` in PostgreSQL to space them out.

## 145: What is work_mem in PostgreSQL?

`work_mem` is the memory each sort, hash join or hash aggregate step may use before spilling to temporary files on disk (default 4 MB). Raising it can make big sorts and joins much faster. But it applies per operation, per connection, so a high value with many connections can run the server out of memory. A common approach is a modest global value and a higher one per session for heavy reports.

## 146: What is innodb_buffer_pool_size?

It is the amount of memory InnoDB uses to cache table and index pages. It is the most important MySQL memory setting. On a server dedicated to MySQL, it is often set to around 50-75% of RAM. If your working data fits in it, most reads never touch the disk.

## 147: What is a query hint?

A hint tells the optimizer how to run a query, for example which index to use or which join order to follow. MySQL supports them directly:

```sql
SELECT /*+ INDEX(o idx_orders_customer) */ *
FROM orders o WHERE customer_id = 42;
```

PostgreSQL core has no hint comments; you need an extension (like `pg_hint_plan`) or settings like `enable_seqscan`. Hints are a last resort, because they don't adapt when data changes.

## 148: Can upgrading the database version make queries faster?

Often yes. Each major release improves the planner, adds new plan types and speeds up common operations. For example, PostgreSQL 18 added skip scan and asynchronous I/O, and PostgreSQL 19 added faster foreign key checks and radix sort. Test your important queries on the new version first, because a few may get a different (sometimes worse) plan.

## 149: How does hardware affect database performance?

- **RAM:** the more of your working data fits in memory, the fewer disk reads.
- **Disk:** SSDs (especially NVMe) have much lower latency and higher random I/O than HDDs.
- **CPU:** matters for sorting, hashing, compression and many connections.
- **Network:** latency between app and database adds to every query.

Hardware helps, but a missing index can't be fixed by a bigger server for long.

## 150: What steps do you take when someone says a query is slow?

1. Get the exact query and parameters, and check how slow it is and how often it runs.
2. Run `EXPLAIN ANALYZE` (on a copy if it writes).
3. Look for full scans on big tables, big gaps between estimated and actual rows, sorts or hashes that spill to disk, and nested loops over many rows.
4. Check indexes, statistics and locks.
5. Make one change, run it again, and compare.

# Moderate Questions (151-300)

## 151: How do you read a PostgreSQL EXPLAIN ANALYZE output?

Read it from the most indented lines (the leaves) up to the top. For each node, compare estimated `rows` with actual `rows`, multiply time by `loops`, and find the node where most of the time goes. Then ask why: is it a scan reading too much, a join with a bad estimate, or a sort spilling to disk?

```
Limit  (actual time=812.1..812.1 rows=10 loops=1)
  ->  Sort  (actual time=812.1..812.1 rows=10 loops=1)
        Sort Method: top-N heapsort  Memory: 26kB
        ->  Seq Scan on orders  (actual time=0.01..640.2 rows=2000000 loops=1)
              Filter: (status = 'paid')
```

Here the sequential scan is the problem; an index on `(status, created_at)` would fix it.

## 152: What does the BUFFERS option show?

It shows how many 8 KB pages each node touched: `shared hit` means found in PostgreSQL's cache, `read` means fetched from the OS or disk, and `dirtied`/`written` cover writes. A query can be fast in testing because everything was cached and slow in production because of reads. Buffers show the real amount of work regardless of timing. Since PostgreSQL 18 they are on by default with `ANALYZE`.

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE customer_id = 42;
```

## 153: What does Rows Removed by Filter tell you?

It shows how many rows a node read and then threw away because they didn't match a condition. A large number means the database is reading far more rows than it returns. That usually means the filter column needs an index, or an existing index is missing a column so the condition is checked after the fetch.

## 154: What is the difference between Index Cond and Filter in a plan?

`Index Cond` is a condition used to search the index, so only matching entries are read. `Filter` is a condition checked after the row is fetched. If an important condition shows as a `Filter` on an index scan, the index doesn't include that column (or the column order is wrong), and the database is fetching rows it then discards.

## 155: How do you see real timings in MySQL?

Use `EXPLAIN ANALYZE` (MySQL 8.0.18+). It runs the query and prints a tree with estimated cost and rows next to actual time, rows and loops for each step. `EXPLAIN FORMAT=TREE` shows the same tree without running it.

```sql
EXPLAIN ANALYZE
SELECT c.name, COUNT(*) FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.name;
```

## 156: How do you choose the column order in a composite index?

A common rule is: columns used with equality (`=`) first, then the column used for a range or sort. For `WHERE tenant_id = ? AND status = ? AND created_at > ? ORDER BY created_at`, use `(tenant_id, status, created_at)`. Among equality columns, order matters less for that query, so pick the order that also helps your other queries.

## 157: Why does a range condition stop later index columns from being used for seeking?

In an index on `(a, b)`, rows are sorted by `a`, and by `b` only within each value of `a`. With `a > 10 AND b = 5`, the matching `b` values are spread over many different `a` values, so the database can't jump straight to them. It scans the whole `a > 10` range and checks `b` on each entry. Put the equality column first: `(b, a)`.

## 158: How do you index a query with WHERE, ORDER BY and LIMIT?

Build one index that starts with the equality filter columns and ends with the sort column, in the same direction. Then the database reads the first few matching entries already in order and stops.

```sql
CREATE INDEX idx_msgs_chat_created ON messages (chat_id, created_at DESC);

SELECT * FROM messages
WHERE chat_id = 7
ORDER BY created_at DESC
LIMIT 50;
```

## 159: Can an index help GROUP BY?

Yes. If the index is sorted by the `GROUP BY` columns, the database can read rows already grouped and use a sort-based aggregate without a separate sort step. If the index also contains every column the query needs, it can be an index-only scan. MySQL can sometimes use a "loose index scan" for `MIN`/`MAX` per group, reading just one entry per group.

## 160: What is the difference between INCLUDE columns and adding columns to the index key?

Key columns are sorted and can be used for searching and ordering. `INCLUDE` columns are stored only in the leaf pages, just to make the index covering. They keep the upper levels of the tree smaller and don't affect uniqueness, so you can add them to a unique index without changing what counts as a duplicate.

```sql
CREATE UNIQUE INDEX idx_users_email ON users (email) INCLUDE (name);
```

MySQL has no `INCLUDE`; you add the columns to the key instead.

## 161: Why is a secondary index in InnoDB often covering for the primary key?

Every InnoDB secondary index stores the primary key value next to each entry, because that is how it finds the row. So an index on `(email)` actually holds `(email, id)`. A query like `SELECT id FROM users WHERE email = ?` is answered from the index alone. This is also why a long primary key makes every secondary index bigger.

## 162: What is index condition pushdown in MySQL?

Index condition pushdown (ICP) lets InnoDB check conditions on index columns while reading the index, before fetching the full row. For an index on `(last_name, first_name)` and `WHERE last_name = 'Smith' AND first_name LIKE '%an%'`, the `first_name` check happens in the index, so fewer full rows are read. It shows as `Using index condition` in `EXPLAIN`.

## 163: What is index merge in MySQL?

It lets MySQL use several single-column indexes for one table and combine the results with union, intersection or sort-union. It shows as `type: index_merge`. It can help with `OR` conditions on different columns, but if you see an intersection often, a composite index covering both columns is usually faster.

## 164: What are BitmapAnd and BitmapOr in PostgreSQL plans?

PostgreSQL can scan several indexes, build a bitmap of matching row locations from each, and combine them with AND or OR before reading the table. This lets it use separate indexes on `a` and `b` for `WHERE a = 1 AND b = 2` or `WHERE a = 1 OR b = 2`. It works, but a composite index matching a frequent `AND` query is usually faster.

## 165: How do you enforce uniqueness only for active rows?

Use a partial unique index in PostgreSQL. This is common with soft deletes, where a deleted user's email should be free for reuse.

```sql
CREATE UNIQUE INDEX idx_users_email_active ON users (email)
WHERE deleted_at IS NULL;
```

In MySQL, a common trick is a generated column that is NULL for deleted rows and unique on that, since a unique index allows many NULLs.

## 166: How do soft deletes affect query performance?

With soft deletes, every query needs `WHERE deleted_at IS NULL`, and the deleted rows still take space in the table and indexes. As deleted rows pile up, scans read more dead data. Use partial indexes on active rows (PostgreSQL), include the flag in composite indexes (MySQL), and archive or hard-delete old soft-deleted rows from time to time.

## 167: How do you make case-insensitive lookups fast?

- PostgreSQL: index `LOWER(email)` and query with `LOWER(email) = LOWER($1)`, or use the `citext` type, or a nondeterministic collation.
- MySQL: the default collations (like `utf8mb4_0900_ai_ci`) are already case-insensitive, so a normal index works.

```sql
CREATE INDEX idx_users_email_lower ON users (LOWER(email));
SELECT * FROM users WHERE LOWER(email) = LOWER('Ann@Example.com');
```

## 168: Why doesn't LIKE 'abc%' use my index in PostgreSQL?

If the database uses a locale-aware collation (like `en_US.UTF-8`), a normal B-tree index can't be used for `LIKE` prefix matching, because its sort order doesn't follow simple character order. Create the index with the pattern operator class, or use the `C` collation for that column.

```sql
CREATE INDEX idx_products_sku_pattern ON products (sku text_pattern_ops);
```

## 169: How do you speed up LIKE '%abc%' in PostgreSQL?

Use the `pg_trgm` extension with a GIN (or GiST) trigram index. It splits strings into three-character pieces and can find rows containing a substring without a full scan. It also supports similarity search for typos.

```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX idx_products_name_trgm ON products USING GIN (name gin_trgm_ops);
SELECT * FROM products WHERE name ILIKE '%phone%';
```

It works best for search terms of three or more characters.

## 170: How do you index jsonb data?

It depends on how you query it.

```sql
-- Many different keys with @> containment: GIN on the whole column
CREATE INDEX idx_events_data ON events USING GIN (data jsonb_path_ops);
SELECT * FROM events WHERE data @> '{"type": "click"}';

-- One key you filter on often: B-tree on an expression
CREATE INDEX idx_events_type ON events ((data->>'type'));
SELECT * FROM events WHERE data->>'type' = 'click';
```

`jsonb_path_ops` makes a smaller, faster GIN index but supports fewer operators than the default `jsonb_ops`.

## 171: How do you index JSON values in MySQL?

MySQL can't index a JSON column directly. Use a functional index on an extracted value (with a cast), a generated column with an index, or a multi-valued index for JSON arrays.

```sql
ALTER TABLE events ADD INDEX idx_type ((CAST(data->>'$.type' AS CHAR(32)) COLLATE utf8mb4_bin));

-- Multi-valued index for an array of tags
ALTER TABLE posts ADD INDEX idx_tags ((CAST(data->'$.tags' AS CHAR(32) ARRAY)));
SELECT * FROM posts WHERE 'sql' MEMBER OF (data->'$.tags');
```

## 172: What are generated columns and how do they help performance?

A generated column is computed from other columns. A stored generated column is saved on disk and can be indexed, so you compute something once on write instead of on every read.

```sql
-- PostgreSQL
ALTER TABLE users ADD COLUMN email_domain text
  GENERATED ALWAYS AS (split_part(email, '@', 2)) STORED;
CREATE INDEX idx_users_domain ON users (email_domain);
```

PostgreSQL 18 also added virtual generated columns (the new default), which are computed on read and save space. MySQL supports both `VIRTUAL` and `STORED`, and can index virtual columns too.

## 173: What is a BRIN index?

BRIN (block range index) stores only the minimum and maximum value for each range of table pages. It is tiny, often a few kilobytes for a huge table. It works well when the column's values follow the physical order of the rows, like `created_at` in an append-only log table. On randomly ordered data it doesn't help.

```sql
CREATE INDEX idx_logs_created_brin ON logs USING BRIN (created_at);
```

## 174: When would you use a hash index in PostgreSQL?

Hash indexes only support `=`. They can be smaller than a B-tree for long values like URLs or tokens, since they store a 4-byte hash instead of the full value. They have been crash-safe and replicated since PostgreSQL 10. In most cases a B-tree is still the default choice because it supports ranges, sorting and uniqueness.

## 175: What is a GiST index used for?

GiST is a general index framework used for data that isn't simply sorted: geometric shapes and PostGIS geography, ranges (like booking periods), nearest-neighbor search, and full-text. It also powers exclusion constraints, such as "no two bookings for the same room may overlap".

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;
ALTER TABLE bookings ADD CONSTRAINT no_overlap
  EXCLUDE USING GIST (room_id WITH =, period WITH &&);
```

## 176: What is an invisible index in MySQL?

An invisible index is kept up to date but ignored by the optimizer. It lets you test what happens if you drop an index without actually dropping it. If performance stays fine, drop it; if something gets slow, make it visible again instantly instead of rebuilding.

```sql
ALTER TABLE orders ALTER INDEX idx_status INVISIBLE;
ALTER TABLE orders ALTER INDEX idx_status VISIBLE;
```

## 177: How do you check the size of tables and indexes?

```sql
-- PostgreSQL
SELECT relname,
       pg_size_pretty(pg_table_size(relid))   AS table_size,
       pg_size_pretty(pg_indexes_size(relid)) AS index_size
FROM pg_stat_user_tables ORDER BY pg_total_relation_size(relid) DESC;

-- MySQL
SELECT table_name, data_length, index_length
FROM information_schema.tables WHERE table_schema = 'shop';
```

If indexes are much bigger than the table, look for unused or bloated indexes.

## 178: How do you tune autovacuum for a big, busy table?

By default autovacuum runs when about 20% of a table's rows are dead, which for a 500-million-row table is far too late. Set lower thresholds on that table so it runs more often and does smaller amounts of work each time.

```sql
ALTER TABLE events SET (
  autovacuum_vacuum_scale_factor = 0.01,
  autovacuum_analyze_scale_factor = 0.02
);
```

You may also need more autovacuum workers or a higher `autovacuum_vacuum_cost_limit` so it can keep up.

## 179: What are HOT updates in PostgreSQL?

A HOT (heap-only tuple) update happens when an update doesn't change any indexed column and the new row version fits on the same page. Then PostgreSQL doesn't need to add new entries to any index, which saves a lot of work and bloat. You can help HOT updates by not indexing frequently updated columns and by leaving free space on pages with `fillfactor`.

```sql
ALTER TABLE sessions SET (fillfactor = 80);
```

## 180: Why can updates be expensive in PostgreSQL when a table has many indexes?

PostgreSQL writes a new row version on every update. Unless it is a HOT update, every index on the table needs a new entry pointing to that new version, even indexes on columns that didn't change. A table with 10 indexes can turn one update into 11 writes. That is why updating an indexed column on a hot table is costly.

## 181: How do you remove bloat from a PostgreSQL table?

- `VACUUM` makes dead space reusable but doesn't shrink the file much.
- `VACUUM FULL` rewrites the table compactly but locks it for the whole time.
- `pg_repack` (an extension) rebuilds the table online with only short locks.
- PostgreSQL 19 added a `REPACK` command with a `CONCURRENTLY` option that does the same job in core.

The real fix is preventing bloat: keep autovacuum tuned and avoid long transactions.

## 182: How do you fix a bloated index?

Rebuild it without blocking writes:

```sql
REINDEX INDEX CONCURRENTLY idx_orders_customer_id;
```

Or create a new index concurrently and drop the old one. Index bloat often comes from many updates or deletes on the indexed column. B-tree deduplication (PostgreSQL 13+) and bottom-up index deletion (14+) reduce it but don't remove the need for an occasional rebuild.

## 183: What does OPTIMIZE TABLE do in MySQL?

For InnoDB it rebuilds the table and its indexes (it maps to `ALTER TABLE ... FORCE`), which removes fragmentation and frees space after big deletes. It runs mostly online, but it does a full copy, so on a big table it takes time and disk space. Run it only after large deletes, not on a schedule.

## 184: What are extended statistics in PostgreSQL?

By default PostgreSQL assumes columns are independent. If `city` and `zip_code` are related, it multiplies their selectivities and badly underestimates rows. Extended statistics teach the planner about relations between columns.

```sql
CREATE STATISTICS stats_addr (dependencies, ndistinct, mcv)
ON city, zip_code FROM addresses;
ANALYZE addresses;
```

## 185: How do you get more detailed statistics for one column?

Raise the statistics target, which controls how many most-common values and histogram buckets are kept (default 100). It helps when a column has a skewed spread of values and estimates are off.

```sql
ALTER TABLE orders ALTER COLUMN status SET STATISTICS 1000;
ANALYZE orders;
```

`default_statistics_target` changes it for all columns, but raising it everywhere makes `ANALYZE` and planning slower.

## 186: What are histograms in MySQL?

MySQL 8.0+ can store histograms for columns that are not indexed, so the optimizer knows how values are spread and can better estimate how many rows a condition returns. This helps pick a good join order. Histograms are not updated automatically by default, so refresh them after big data changes.

```sql
ANALYZE TABLE orders UPDATE HISTOGRAM ON status WITH 64 BUCKETS;
```

## 187: Why do estimates go wrong when you filter on several related columns?

The planner usually multiplies the selectivity of each condition, as if columns were independent. For `WHERE country = 'DE' AND city = 'Berlin'`, it treats them as unrelated and estimates far fewer rows than reality. Wrong estimates lead to wrong join methods, like a nested loop over a large set. Extended statistics in PostgreSQL or histograms in MySQL can fix this.

## 188: What are generic and custom plans in PostgreSQL?

For prepared statements, PostgreSQL plans the first five runs with the real parameter values (custom plans). After that, it may switch to one generic plan that ignores the values if that plan looks about as cheap. That's faster to plan, but if data is skewed, the generic plan can be terrible for some values. You can control this with `plan_cache_mode`.

```sql
SET plan_cache_mode = force_custom_plan;
```

## 189: Why can the same query be fast for one value and slow for another?

Because of data skew. `WHERE status = 'failed'` might match 50 rows and use an index, while `WHERE status = 'done'` matches 10 million rows and should use a full scan. If the planner caches one plan for all values, or estimates poorly, one of them gets the wrong plan. Check the plan with the slow value specifically.

## 190: How do you rewrite a correlated subquery that runs once per row?

Turn it into a join with a pre-aggregated subquery, so the work is done once for all rows.

```sql
-- Slow: subquery runs for every customer
SELECT c.id,
  (SELECT SUM(total) FROM orders o WHERE o.customer_id = c.id) AS spent
FROM customers c;

-- Faster for many customers
SELECT c.id, COALESCE(o.spent, 0) AS spent
FROM customers c
LEFT JOIN (
  SELECT customer_id, SUM(total) AS spent FROM orders GROUP BY customer_id
) o ON o.customer_id = c.id;
```

If you only need a few customers, the correlated version with an index can be faster, so check the plan.

## 191: What is a LATERAL join and when does it help?

A `LATERAL` subquery can refer to columns from tables earlier in the `FROM` list, so it runs per row like a loop. It is great for "top N per group" when there is a matching index, because each lookup reads only N index entries.

```sql
SELECT c.id, o.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT id, total, created_at FROM orders
  WHERE customer_id = c.id
  ORDER BY created_at DESC LIMIT 3
) o;
```

MySQL supports `LATERAL` since 8.0.14.

## 192: How can window functions replace self-joins?

A self-join to compare a row with the previous one, or to compute a running total, reads the table twice and can blow up in size. Window functions do it in one pass.

```sql
SELECT id, created_at, total,
       total - LAG(total) OVER (ORDER BY created_at) AS diff,
       SUM(total) OVER (ORDER BY created_at) AS running_total
FROM orders;
```

## 193: What are the ways to get the top N rows per group, and which is fastest?

- `ROW_NUMBER() OVER (PARTITION BY ...)` and filter `rn <= N`: simple, but computes the number for every row.
- `LATERAL` with `ORDER BY ... LIMIT N` and an index on `(group, sort)`: fastest when there are few groups compared to rows.
- `DISTINCT ON` in PostgreSQL for N = 1.

With many groups and few rows per group, the window function is often fine. With few groups and millions of rows each, use `LATERAL`.

## 194: What is DISTINCT ON in PostgreSQL?

It returns the first row for each distinct value of the given columns, based on the `ORDER BY`. It is a short way to get "latest row per group".

```sql
SELECT DISTINCT ON (customer_id) customer_id, id, created_at
FROM orders
ORDER BY customer_id, created_at DESC;
```

An index on `(customer_id, created_at DESC)` lets it avoid a sort.

## 195: How do you rewrite an OR across different columns so indexes are used?

Split it into two queries that each use an index, and combine them. Use `UNION` to remove rows that match both, or `UNION ALL` with an extra condition to avoid duplicates.

```sql
SELECT * FROM users WHERE email = 'a@b.com'
UNION ALL
SELECT * FROM users WHERE phone = '555' AND email IS DISTINCT FROM 'a@b.com';
```

Check first: the planner may already combine the indexes with a bitmap OR or index merge.

## 196: Why should you aggregate before joining?

If you join a big table first and group after, the join produces many rows that then get grouped. If you group the big table first, the join works on far fewer rows.

```sql
SELECT p.name, s.qty
FROM products p
JOIN (SELECT product_id, SUM(qty) AS qty FROM sales GROUP BY product_id) s
  ON s.product_id = p.id;
```

## 197: What is join fan-out and how does it break aggregates?

When you join a parent to two different child tables at once, each parent row repeats for every combination of children. Sums and counts get multiplied, and the query gets slower. People often "fix" it with `DISTINCT`, which hides the bug and adds cost. Instead, aggregate each child table separately in subqueries and then join the results.

## 198: How do you show a total count with paginated results without a slow COUNT(*)?

- Don't show an exact total; show "next page" only, or "more than 1,000 results".
- Use the planner's estimate from `EXPLAIN` or `pg_class.reltuples` when the number can be approximate.
- Cache the count for a short time.
- Keep a counter table updated by the app or a trigger when exact numbers are needed.

Running an exact `COUNT(*)` on every page load is often more expensive than the page query itself.

## 199: How do you update many rows from another table in one statement?

```sql
-- PostgreSQL
UPDATE products p
SET price = n.price
FROM new_prices n
WHERE n.product_id = p.id;

-- MySQL
UPDATE products p
JOIN new_prices n ON n.product_id = p.id
SET p.price = n.price;
```

One set-based update is much faster than looping in the app and sending one `UPDATE` per row.

## 200: How large should a batch be for bulk inserts?

Large enough to cut round trips, small enough to keep transactions short and memory reasonable. A few hundred to a few thousand rows per statement usually works well. Very big batches can hit packet size limits (`max_allowed_packet` in MySQL), the parameter limit (65,535 bind parameters in PostgreSQL), long lock times, and replication lag. Measure with your real data.

## 201: How do you insert many rows from an app in PostgreSQL with one parameterized query?

Pass arrays and use `unnest`. The query text stays the same no matter how many rows you send, so it can be prepared once, and you avoid the bind parameter limit.

```sql
INSERT INTO events (user_id, type)
SELECT * FROM unnest($1::int[], $2::text[]);
```

For very large loads, `COPY` through the driver (like `copyFrom` in pg-copy-streams or `copy_expert` in psycopg) is faster still.

## 202: What is the problem with a huge IN list?

A query with `IN (...)` and thousands of literal values is slow to parse and plan, every different list length creates a different query text (which defeats plan caching and fills `pg_stat_statements`), and you may hit parameter limits. Better options are an array parameter with `= ANY($1)` in PostgreSQL, or loading the values into a temporary table and joining to it.

```sql
SELECT * FROM products WHERE id = ANY($1::bigint[]);
```

## 203: How do you size a connection pool?

More connections is not better. The database can only run about as many queries at once as it has CPU cores and disk capacity; past that, connections just wait and compete. A common starting point is a pool of around 2-4 connections per CPU core on the database server, shared across all app instances, then tune by measuring. Remember to multiply by the number of app servers or pods.

## 204: What are the pool modes in PgBouncer?

- **Session:** a client keeps one server connection for its whole session. Safest, but saves little.
- **Transaction:** a server connection is given to a client only for one transaction. Many clients can share few connections. Session state like `SET`, temp tables and `LISTEN` doesn't work reliably.
- **Statement:** a connection per statement; multi-statement transactions are not allowed.

Transaction mode is the usual choice for web apps. Recent PgBouncer versions (1.21+) can also track protocol-level prepared statements in transaction mode with `max_prepared_statements`.

## 205: Why do serverless apps often run out of database connections?

Each function instance opens its own connections, and a traffic spike can start hundreds of instances at once. The database hits `max_connections` and new requests fail. Use an external pooler (PgBouncer, RDS Proxy, or the provider's pooled connection string), keep the pool size per instance at 1-2, and reuse the client across invocations.

## 206: What does idle in transaction mean and why is it bad?

A session in the `idle in transaction` state has started a transaction and is doing nothing, often because the app forgot to commit or is waiting on something else. It keeps holding its locks, and in PostgreSQL it stops VACUUM from removing dead rows, which causes bloat across the database. Fix the code, and set a timeout as a safety net.

```sql
ALTER DATABASE app SET idle_in_transaction_session_timeout = '60s';
```

## 207: How do you find which query is blocking others in PostgreSQL?

```sql
SELECT blocked.pid  AS blocked_pid,
       blocked.query AS blocked_query,
       blocking.pid  AS blocking_pid,
       blocking.query AS blocking_query
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocking
  ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));
```

Often the blocker is an idle-in-transaction session or a long migration. Setting `log_lock_waits = on` also logs any lock wait longer than `deadlock_timeout`.

## 208: How do you find lock waits in MySQL?

Use the `sys` schema, which reads from `performance_schema.data_lock_waits`:

```sql
SELECT waiting_pid, waiting_query, blocking_pid, blocking_query, wait_age
FROM sys.innodb_lock_waits;
```

For deadlocks, `SHOW ENGINE INNODB STATUS` shows the latest one, and `innodb_print_all_deadlocks = ON` writes every deadlock to the error log.

## 209: How does SKIP LOCKED help with job queues?

Without it, workers that try to grab the next job all wait on the same locked row. `SKIP LOCKED` tells each worker to skip rows another worker already locked and take the next free one, so many workers can pull jobs in parallel.

```sql
UPDATE jobs SET status = 'running', started_at = now()
WHERE id = (
  SELECT id FROM jobs WHERE status = 'queued'
  ORDER BY id
  FOR UPDATE SKIP LOCKED
  LIMIT 1
)
RETURNING *;
```

MySQL 8.0 supports `SKIP LOCKED` too.

## 210: What does NOWAIT do?

`SELECT ... FOR UPDATE NOWAIT` fails right away with an error if a row is already locked, instead of waiting. Use it when it is better to tell the user "someone else is editing this" than to make them wait.

## 211: What is optimistic locking and how does it reduce lock contention?

Instead of locking a row while a user edits it, you keep a `version` column. When saving, you update only if the version hasn't changed. If zero rows were updated, someone else changed it first and you retry or show a conflict. No locks are held between read and write.

```sql
UPDATE documents
SET body = $1, version = version + 1
WHERE id = $2 AND version = $3;
```

## 212: What are gap locks and next-key locks in InnoDB?

In `REPEATABLE READ`, when InnoDB locks rows found by a range search, it also locks the gaps between index entries so no one can insert a new row into that range (preventing phantom rows). A next-key lock is a row lock plus the gap before it. These locks can block inserts you didn't expect and cause deadlocks. Using `READ COMMITTED` turns off most gap locking.

## 213: How do you reduce deadlocks?

- Access tables and rows in the same order in every code path, for example sort IDs before updating.
- Keep transactions short.
- Use indexes on the columns in `WHERE` of updates, so fewer rows get locked (in InnoDB, a scan without an index locks many rows).
- Retry the transaction when a deadlock error happens; it is a normal event, not a crash.

## 214: What are advisory locks in PostgreSQL?

They are locks on a number that you choose, with no table behind them. Your app decides what the number means, for example "only one worker may run the nightly report". They are cheap and are released at the end of the session or transaction.

```sql
SELECT pg_try_advisory_lock(42);  -- true if you got it
SELECT pg_advisory_unlock(42);
```

MySQL has a similar feature with `GET_LOCK('name', timeout)`.

## 215: How do you add a NOT NULL constraint to a big PostgreSQL table without a long lock?

`ALTER TABLE ... SET NOT NULL` scans the whole table while holding a strong lock. Add a `CHECK` constraint as `NOT VALID` first (instant), validate it (scans, but allows writes), then set `NOT NULL`, which PostgreSQL 12+ can do without a scan because the validated check proves it.

```sql
ALTER TABLE orders ADD CONSTRAINT orders_customer_nn CHECK (customer_id IS NOT NULL) NOT VALID;
ALTER TABLE orders VALIDATE CONSTRAINT orders_customer_nn;
ALTER TABLE orders ALTER COLUMN customer_id SET NOT NULL;
ALTER TABLE orders DROP CONSTRAINT orders_customer_nn;
```

## 216: How do you add a foreign key to a big table without blocking writes?

Add it as `NOT VALID`, which only checks new rows and is fast, then validate it in a separate step that scans existing rows with a weaker lock.

```sql
ALTER TABLE orders ADD CONSTRAINT fk_orders_customer
  FOREIGN KEY (customer_id) REFERENCES customers (id) NOT VALID;
ALTER TABLE orders VALIDATE CONSTRAINT fk_orders_customer;
```

## 217: What are online schema change tools for MySQL?

`gh-ost` and `pt-online-schema-change` change big MySQL tables without long locks. They create a new table with the new structure, copy rows in small chunks, keep it in sync with ongoing changes (gh-ost reads the binlog, pt-osc uses triggers), and then swap the tables. Many changes can now run natively with `ALGORITHM=INSTANT` or `INPLACE`, so check that first.

## 218: Why is a long-running migration dangerous even if it takes a "light" lock?

In PostgreSQL, a waiting `ALTER TABLE` sits in the lock queue, and every query that comes after it has to wait behind it, even simple `SELECT`s. So if the migration waits for a long-running query to finish, the whole table becomes unavailable. Always set `lock_timeout` for migrations and retry, instead of waiting forever.

## 219: How do you refresh a materialized view without blocking readers?

Use `REFRESH MATERIALIZED VIEW CONCURRENTLY`. It builds the new data and applies only the differences, so reads keep working during the refresh. It needs a unique index on the view, and it can be slower than a normal refresh when most rows change.

```sql
CREATE UNIQUE INDEX ON daily_sales (day);
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_sales;
```

## 220: What is a summary (rollup) table?

It is a table that stores pre-computed aggregates, like sales per day per product, updated by a job or as new data arrives. Dashboards read the small summary table instead of aggregating millions of raw rows every time. Unlike a materialized view, you can update it incrementally (only the newest day), which works well for growing data.

```sql
INSERT INTO sales_daily (day, product_id, qty)
SELECT created_at::date, product_id, SUM(qty) FROM sales
WHERE created_at >= current_date GROUP BY 1, 2
ON CONFLICT (day, product_id) DO UPDATE SET qty = EXCLUDED.qty;
```

## 221: What is the cache-aside pattern?

The app first looks in the cache. On a miss, it reads from the database, stores the result in the cache with a TTL, and returns it. On writes, it updates the database and deletes the cache key. It is simple and the most common pattern. Watch out for many requests missing at the same time and all hitting the database (a cache stampede).

## 222: How do you route reads to replicas without showing stale data?

Send most reads to replicas, but read from the primary for a short time after a user writes (for example, a session flag for a few seconds). Another option is to track the WAL or GTID position of the write and wait until the replica has replayed it. PostgreSQL 19 added `WAIT FOR LSN` for this on standbys; MySQL has `WAIT_FOR_EXECUTED_GTID_SET()`.

## 223: When does partition pruning work?

Pruning happens when the query filters on the partition key in a way the planner can understand: comparisons with constants, parameters, or values known at run time (PostgreSQL can also prune during execution). It doesn't work if you wrap the partition key in a function, or filter on a different column. Check `EXPLAIN` to see which partitions are scanned.

```sql
-- Prunes to one partition
SELECT * FROM events WHERE created_at >= '2026-11-01' AND created_at < '2026-11-02';
```

## 224: How do you choose a partition key?

Pick the column most queries filter on and that matches how data ages out. For logs and events that is usually time. For multi-tenant data it may be tenant (list or hash partitioning). A bad key means most queries scan every partition, which is slower than an unpartitioned table.

## 225: Can you have too many partitions?

Yes. Each partition adds planning time, open files and memory, and queries that can't prune have to touch all of them. Thousands of small partitions make things slower, not faster. Aim for partitions that are large enough (many gigabytes) and a count in the dozens or low hundreds.

## 226: How do you manage time-based partitions over time?

Create future partitions ahead of time and drop or archive old ones on a schedule. In PostgreSQL, `pg_partman` automates this. Detaching a partition can be done without blocking queries:

```sql
ALTER TABLE events DETACH PARTITION events_2025_01 CONCURRENTLY;
DROP TABLE events_2025_01;
```

## 227: How do indexes work on partitioned tables?

In PostgreSQL, creating an index on the partitioned table creates a matching index on each partition (and on future ones). A unique index or primary key must include the partition key, because uniqueness is only checked within each partition. MySQL has the same rule for unique keys. Partitions can also have extra indexes of their own.

## 228: How does parallel query work in PostgreSQL?

For big scans, joins and aggregates, PostgreSQL can start extra worker processes that each handle part of the table, then combine their results in a `Gather` node. It can make large reporting queries several times faster. The number of workers per step is limited by `max_parallel_workers_per_gather`.

```sql
SET max_parallel_workers_per_gather = 4;
EXPLAIN SELECT COUNT(*) FROM big_table;
```

## 229: Why might PostgreSQL not use parallel query?

- The table is smaller than `min_parallel_table_scan_size`.
- `max_parallel_workers_per_gather` is 0, or all workers are busy.
- The query writes data in a way that isn't parallel safe, or calls a function marked `PARALLEL UNSAFE`.
- The query returns rows through a cursor.
- The planner thinks the startup cost of workers isn't worth it.

## 230: What is JIT compilation in PostgreSQL?

JIT (using LLVM) compiles parts of a query, like expression evaluation, into machine code at run time. It helps long analytical queries that process millions of rows, but compiling takes time, which can make short queries slower. PostgreSQL 19 turned JIT off by default. You can enable it for reporting sessions with `SET jit = on`.

## 231: How should you set shared_buffers and effective_cache_size?

`shared_buffers` is PostgreSQL's own page cache; a common starting value is about 25% of RAM. The OS file cache holds much of the rest. `effective_cache_size` doesn't allocate memory; it tells the planner how much cache (PostgreSQL plus OS) is likely available, so it can judge how cheap index scans will be. It is often set to 50-75% of RAM.

## 232: What is random_page_cost and why change it?

It tells the PostgreSQL planner how expensive a random page read is compared to a sequential one (`seq_page_cost = 1`). The default of 4 was chosen for spinning disks. On SSDs random reads are almost as fast as sequential ones, so lowering it to around 1.1 makes the planner more willing to use index scans.

```sql
ALTER SYSTEM SET random_page_cost = 1.1;
SELECT pg_reload_conf();
```

## 233: What is maintenance_work_mem?

It is the memory used by maintenance jobs like `CREATE INDEX`, `VACUUM` and adding foreign keys. Raising it (for example to 1-2 GB on a large server) makes index builds and vacuum faster. Only a few of these jobs run at once, so it is safer to set high than `work_mem`. Autovacuum workers use `autovacuum_work_mem` if it is set.

## 234: How do you tune checkpoints in PostgreSQL?

If checkpoints happen too often, the server writes the same pages again and again and writes full page images to the WAL after each one. Raise `max_wal_size` so checkpoints are triggered by time (`checkpoint_timeout`) rather than WAL volume, and keep `checkpoint_completion_target` at 0.9 to spread the writes out. The server log warns you if checkpoints happen too frequently.

## 235: What does synchronous_commit = off do?

The commit returns before the WAL is flushed to disk. Commits get much faster, but if the server crashes, the last fraction of a second of committed transactions can be lost. The database stays consistent; you just lose some recent data. It can be set per transaction, so you can use it only for data you can afford to lose, like analytics events.

```sql
SET LOCAL synchronous_commit = off;
```

## 236: What does innodb_flush_log_at_trx_commit control?

It controls when InnoDB flushes the redo log to disk:

- `1` (default): flush on every commit. Fully durable.
- `2`: write to the OS on commit, flush about once a second. Survives a MySQL crash but can lose about a second on an OS crash or power loss.
- `0`: write and flush about once a second. Fastest, least safe.

Use `1` unless you clearly accept data loss for speed.

## 237: Why does the redo log size matter in MySQL?

If the redo log is too small, InnoDB must flush dirty pages early to free log space, which causes write stalls under heavy load. Since MySQL 8.0.30 you set it with `innodb_redo_log_capacity` (it replaced `innodb_log_file_size`) and can change it at run time. A rule of thumb is enough capacity for about an hour of writes at peak.

## 238: What are tmp_table_size and max_heap_table_size in MySQL?

They limit how large an in-memory internal temporary table (used for `GROUP BY`, `DISTINCT`, derived tables and so on) can get before MySQL moves it to disk. The smaller of the two applies to some table types. If `Created_tmp_disk_tables` keeps rising, raising them may help, but fixing the query or adding an index is usually better.

## 239: How can you tell that a query spilled to disk?

- PostgreSQL `EXPLAIN ANALYZE` shows `Sort Method: external merge  Disk: 120000kB` or hash `Batches: 8`.
- `log_temp_files = 0` logs every temp file created.
- `pg_stat_database.temp_bytes` shows totals.
- In MySQL, check `Created_tmp_disk_tables` and `Sort_merge_passes`, or the `sys.statements_with_temp_tables` and `sys.statements_with_sorting` views.

## 240: What is auto_explain?

`auto_explain` is a PostgreSQL module that logs the execution plan of any query slower than a threshold. It's useful because the plan in production can differ from the one you get when you run `EXPLAIN` by hand later.

```
shared_preload_libraries = 'auto_explain'
auto_explain.log_min_duration = '1s'
auto_explain.log_analyze = on
auto_explain.log_buffers = on
```

`log_analyze` adds timing overhead to every query, so use it with care.

## 241: What are Performance Schema and the sys schema in MySQL?

Performance Schema collects low-level data about statements, waits, locks, memory and I/O. The `sys` schema is a set of easier views on top of it. Useful ones are `sys.statement_analysis` (top queries by total time), `sys.statements_with_full_table_scans`, `sys.schema_unused_indexes` and `sys.innodb_lock_waits`.

## 242: How do you find tables that are scanned too often in PostgreSQL?

`pg_stat_user_tables` counts sequential and index scans per table. A big table with many sequential scans that read lots of rows likely needs an index.

```sql
SELECT relname, seq_scan, seq_tup_read, idx_scan, n_live_tup
FROM pg_stat_user_tables
ORDER BY seq_tup_read DESC
LIMIT 10;
```

## 243: What is the cache hit ratio and how do you check it?

It's the share of page reads served from memory instead of disk. For an OLTP database you want it close to 99%. A low ratio means the hot data doesn't fit in memory, or some queries scan huge amounts of data.

```sql
SELECT sum(heap_blks_hit) * 100.0 / nullif(sum(heap_blks_hit) + sum(heap_blks_read), 0)
FROM pg_statio_user_tables;
```

PostgreSQL only sees its own cache, so an OS-cache hit still counts as a "read" here.

## 244: How does pg_stat_statements group queries?

It normalizes queries by replacing constants with placeholders, so `WHERE id = 1` and `WHERE id = 2` are counted as one entry with a single `queryid`. It tracks calls, total and mean time, rows, and buffer usage. Reset it with `pg_stat_statements_reset()` before and after a change to compare clean numbers.

## 245: How do you run EXPLAIN ANALYZE safely in production?

- Use plain `EXPLAIN` first; it doesn't run the query.
- For writes, wrap `EXPLAIN ANALYZE` in `BEGIN ... ROLLBACK`.
- Set a `statement_timeout` so a bad query doesn't run for an hour.
- Run it on a replica or a recent copy when possible.
- Remember that `EXPLAIN ANALYZE` with timing adds overhead, so the numbers are a bit higher than normal.

## 246: Why should you test queries on production-sized data?

On a small dev database, every table fits in memory and full scans are fast, so a missing index stays hidden. The planner also picks different plans for different table sizes and value distributions. Test with a copy (masked for privacy) or generated data of similar size and shape.

## 247: How do you catch query performance regressions after a deploy?

Track query metrics over time: `pg_stat_statements` snapshots, APM tools, or slow query log digests. Compare top queries by total time before and after the release. Also review migrations and new queries in code review, and run `EXPLAIN` on new queries against realistic data before merging.

## 248: What is TOAST in PostgreSQL and how does it affect queries?

When a row value is large (over about 2 KB), PostgreSQL compresses it and/or moves it to a separate TOAST table. The main table stays small, which keeps scans fast. But reading a TOASTed column means extra lookups and decompression, so `SELECT *` on a table with big text or JSON columns can be much slower than selecting only the small columns. PostgreSQL 19 uses lz4 compression by default, which is faster than the old pglz.

## 249: What are the trade-offs of storing data in JSON columns instead of normal columns?

JSON is flexible, but the planner has poor statistics on values inside it, so estimates are often wrong. Each row repeats the key names, so storage is larger, and updating one key rewrites the whole value. Constraints and foreign keys don't work inside it. Use real columns for data you filter, join or sort on, and JSON for loosely structured extras.

## 250: What is the EAV pattern and why is it slow?

EAV (entity-attribute-value) stores each attribute as its own row: `(entity_id, attribute, value)`. It looks flexible, but rebuilding one object needs many rows or self-joins, values are stored as text so types and indexes don't work well, and filtering on several attributes needs a join per attribute. A `jsonb` column or proper columns are usually better.

## 251: Should you store statuses as text, enums or a lookup table?

- **Text:** simple and flexible, but bigger and typos can slip in (add a `CHECK` constraint).
- **Enum type:** stored as 4 bytes in PostgreSQL (1-2 bytes in MySQL), checked by the database, but adding or reordering values needs a schema change.
- **Lookup table with an integer ID:** small, easy to extend, can hold extra data, but needs a join to show the name.

The performance gap is small for most apps. Pick based on how often the list changes.

## 252: Should money be stored as numeric, float or integer?

Never use float for money; it can't store values like 0.10 exactly and errors add up. `numeric`/`decimal` is exact but a bit slower to compute. Storing amounts as integer cents (`bigint`) is exact and fast, and common in high-volume systems. Pick one and use it everywhere.

## 253: How do you make COUNT(DISTINCT ...) faster?

`COUNT(DISTINCT col)` has to sort or hash every value, which is heavy on big tables. Options:

- An index on the column so values are read in order.
- Pre-aggregated or summary tables.
- Approximate counts with HyperLogLog (`postgresql-hll` extension, or tools outside the database) when a small error is fine.
- Counting distinct over a smaller, pre-filtered set.

## 254: What is TABLESAMPLE?

It reads a random sample of a table's pages or rows instead of the whole thing. It is handy for fast approximate stats on huge tables.

```sql
SELECT AVG(total) FROM orders TABLESAMPLE SYSTEM (1);
```

`SYSTEM` samples whole pages (fast, less random); `BERNOULLI` samples rows (slower, more random). MySQL doesn't have it.

## 255: How should you design indexes for a multi-tenant table?

Put `tenant_id` first in nearly every index, because almost every query filters on it. Then add the columns for each query's filters and sort. This keeps each tenant's data close together in the index and stops one tenant's query from scanning others' rows. In MySQL, making the primary key `(tenant_id, id)` also clusters each tenant's rows together on disk.

## 256: How does PostgreSQL row-level security affect performance?

RLS adds the policy condition to every query on the table. If the policy is simple (`tenant_id = current_setting('app.tenant')::int`) and that column is indexed, the cost is small. If the policy calls a function or runs a subquery for every row, queries can get much slower. Mark helper functions as `STABLE` or wrap them in a `SELECT` so they are evaluated once, not per row.

```sql
CREATE POLICY tenant_isolation ON orders
USING (tenant_id = (SELECT current_setting('app.tenant_id')::int));
```

## 257: What is a cartesian explosion when an ORM eager-loads several collections?

If you load a post with its comments and its tags in one joined query, the result has comments times tags rows per post. With 100 comments and 20 tags, that's 2,000 rows to build one object. ORMs usually let you split this into separate queries per collection (for example `AsSplitQuery()` in EF Core or `prefetch_related` in Django), which is much faster.

## 258: How do you detect N+1 queries automatically?

- Count queries per request in tests and fail when the count grows (for example, Django's `assertNumQueries`).
- Use tools that warn about it, like Bullet for Rails or nplusone for Python.
- Look in APM traces for many identical queries inside one request.
- In `pg_stat_statements`, a simple query with a huge `calls` count is a hint.

## 259: How do you replace JOIN plus DISTINCT with EXISTS?

If you join only to filter and then use `DISTINCT` to remove duplicates, `EXISTS` does the same without producing duplicates in the first place.

```sql
-- Instead of
SELECT DISTINCT c.* FROM customers c JOIN orders o ON o.customer_id = c.id;

-- Use
SELECT c.* FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

## 260: What is the difference between NOT EXISTS and LEFT JOIN ... IS NULL?

Both find rows without a match, and modern planners usually turn both into an anti-join with the same speed. `NOT EXISTS` states the intent more clearly and can't be broken by a column that is allowed to be NULL in the right table. Avoid `NOT IN` with a subquery for this, because of the NULL problem.

```sql
SELECT c.* FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
```

## 261: Why are "optional filter" conditions like (col = $1 OR $1 IS NULL) slow?

The planner must make one plan that works whether `$1` is NULL or not, so it often can't use the index on `col` and falls back to a scan. This is common in search endpoints with many optional filters. Build the SQL dynamically and only add the conditions that were actually provided (still with bind parameters).

```js
const where = [];
const params = [];
if (status) {
  params.push(status);
  where.push(`status = $${params.length}`);
}
if (from) {
  params.push(from);
  where.push(`created_at >= $${params.length}`);
}
const sql = `SELECT * FROM orders ${where.length ? "WHERE " + where.join(" AND ") : ""}`;
```

## 262: Why is ORDER BY RAND() slow, and what can you use instead?

`ORDER BY RAND()` (or `random()`) gives every row a random number and sorts the whole table just to take one row. For one random row, pick a random ID within the ID range and take the first row at or after it, or use `TABLESAMPLE` in PostgreSQL.

```sql
SELECT * FROM products
WHERE id >= (SELECT floor(random() * (SELECT max(id) FROM products))::bigint)
ORDER BY id LIMIT 1;
```

This is fast but not perfectly uniform if there are gaps in IDs.

## 263: How do recursive CTEs perform and how do you make them faster?

A recursive CTE runs its second part again and again, once per level, joining on the rows found in the previous level. It is fast if the join column (like `parent_id`) is indexed and the tree isn't too deep. Without an index, each level scans the whole table. Always add a depth limit or cycle check to avoid infinite loops.

```sql
WITH RECURSIVE tree AS (
  SELECT id, parent_id, 1 AS depth FROM categories WHERE id = 1
  UNION ALL
  SELECT c.id, c.parent_id, t.depth + 1
  FROM categories c JOIN tree t ON c.parent_id = t.id
  WHERE t.depth < 20
)
SELECT * FROM tree;
```

## 264: What are faster ways to store trees than parent_id alone?

- **Materialized path:** store the path like `1/4/9/`; subtree queries become prefix searches (`ltree` in PostgreSQL has its own index support).
- **Closure table:** one row per ancestor-descendant pair; reads are simple joins, but writes touch more rows.
- **Nested sets:** fast reads, slow and complex writes.

`parent_id` with a recursive CTE is fine for small or shallow trees.

## 265: Does an upsert have hidden costs?

Yes. In PostgreSQL, `ON CONFLICT DO UPDATE` writes a new row version even if the values didn't change, which creates dead rows; add `WHERE` to skip no-op updates. In MySQL, `INSERT ... ON DUPLICATE KEY UPDATE` can use up auto-increment values even when it updates, leaving gaps, and takes extra locks. Both need a unique index to detect conflicts.

```sql
INSERT INTO prices (id, price) VALUES (1, 9.99)
ON CONFLICT (id) DO UPDATE SET price = EXCLUDED.price
WHERE prices.price IS DISTINCT FROM EXCLUDED.price;
```

## 266: What is the MERGE statement?

`MERGE` (PostgreSQL 15+) compares a source with a target table and inserts, updates or deletes rows in one statement, based on whether they match. It's useful for syncing tables from a staging load. PostgreSQL 17 added `RETURNING` to it. For simple single-row upserts, `INSERT ... ON CONFLICT` is usually simpler and handles concurrency better.

```sql
MERGE INTO products p
USING staging s ON s.id = p.id
WHEN MATCHED THEN UPDATE SET price = s.price
WHEN NOT MATCHED THEN INSERT (id, name, price) VALUES (s.id, s.name, s.price);
```

## 267: How does RETURNING save round trips?

`RETURNING` gives back columns from rows you just inserted, updated or deleted, in the same statement. You don't need a second `SELECT` to get the new ID or computed values.

```sql
INSERT INTO orders (customer_id, total) VALUES (42, 99.50)
RETURNING id, created_at;
```

MySQL doesn't support `RETURNING`; you use `LAST_INSERT_ID()` for the auto-increment value.

## 268: What does PostgreSQL 19's ON CONFLICT DO SELECT solve?

A common "get or create" pattern needs an insert and then, if the row already existed, a separate select to get it. `INSERT ... ON CONFLICT DO SELECT` returns the existing conflicting row instead, so you get the row in one statement either way, without the dead row that `DO UPDATE SET x = x` would create.

## 269: How should you archive old data?

Move rows that are rarely read (old orders, logs) out of the hot tables into archive tables, a separate database, or cheap storage like Parquet files in object storage. The hot tables and their indexes stay small and cached. With partitioning, archiving is as simple as detaching an old partition. Without it, move rows in small batches.

## 270: What are unlogged tables in PostgreSQL?

Unlogged tables don't write to the WAL, so writes are much faster. The cost is that they are emptied after a crash and are not copied to replicas. They are good for staging data during imports, caches, or other data you can rebuild.

```sql
CREATE UNLOGGED TABLE import_staging (LIKE products INCLUDING ALL);
```

## 271: When should you use a temporary table instead of a CTE or subquery?

Use a temp table when a middle result is reused in several later queries, when it is large and would benefit from its own index, or when the planner keeps misjudging a complex subquery (a temp table plus `ANALYZE` gives it real statistics). For a single query used once, a CTE or subquery is simpler.

## 272: Why does a type or collation mismatch on join columns slow things down?

If `orders.customer_id` is `bigint` and `customers.id` is `int`, or two `VARCHAR` columns in MySQL use different character sets or collations, the database has to convert one side for every comparison. That can stop index use on the converted side and turn an index join into a scan. Keep join columns the same type, charset and collation.

## 273: What are prefix indexes in MySQL?

A prefix index indexes only the first N characters of a string column. It is smaller, which helps for long `VARCHAR` or `TEXT` columns (TEXT can only be indexed with a prefix). The downsides: it can't be a covering index, it can't help `ORDER BY` fully, and if many values share the same prefix it isn't selective.

```sql
CREATE INDEX idx_urls_url ON urls (url(100));
```

## 274: How do you index a very long text value for exact lookups?

Store a hash of the value (like SHA-256 or MD5) in a separate column and index the hash. Look up by hash and compare the full value to rule out collisions. In PostgreSQL, a hash index or an expression index on `md5(value)` works too.

```sql
CREATE INDEX idx_urls_hash ON urls ((md5(url)));
SELECT * FROM urls WHERE md5(url) = md5($1) AND url = $1;
```

## 275: What is the index length limit in MySQL with utf8mb4?

InnoDB with the `DYNAMIC` row format allows index keys up to 3072 bytes. With `utf8mb4` each character can take up to 4 bytes, so a single `VARCHAR(768)` column is the max that fits fully. Longer columns need a prefix index. Choosing column lengths that match real data keeps indexes smaller.

## 276: How do you speed up time-series aggregation queries?

- Partition or use a BRIN index on the time column.
- Index `(series_id, time)` for per-series queries.
- Pre-aggregate into hourly or daily rollup tables.
- Use `date_trunc` (PostgreSQL) to group into buckets.
- Consider TimescaleDB for continuous aggregates and compression on very large data.

```sql
SELECT date_trunc('hour', ts) AS hour, AVG(value)
FROM metrics
WHERE sensor_id = 7 AND ts >= now() - interval '1 day'
GROUP BY 1 ORDER BY 1;
```

## 277: Why can adding LIMIT make a query slower?

With a small `LIMIT`, the planner may choose to walk an index in `ORDER BY` order and stop after N matches, expecting matches to be spread evenly. If the matching rows are rare or all at the end of the index, it walks almost the whole index before finding N rows. The fix is often a composite index that includes the filter column before the sort column.

## 278: How does the visibility map affect index-only scans?

An index doesn't store whether a row version is visible to your transaction. For an index-only scan, PostgreSQL checks the visibility map: if the page is marked all-visible, it trusts the index; if not, it reads the table page. `Heap Fetches` in `EXPLAIN ANALYZE` shows how often it had to. Frequent VACUUM keeps pages all-visible and index-only scans truly index-only.

## 279: How do you monitor replication lag?

```sql
-- PostgreSQL, on the primary
SELECT client_addr, replay_lag FROM pg_stat_replication;

-- PostgreSQL, on the replica
SELECT now() - pg_last_xact_replay_timestamp() AS lag;
```

In MySQL, `SHOW REPLICA STATUS` shows `Seconds_Behind_Source`. Alert on lag, because big batch writes, long queries on the replica or a slow replica disk can make it grow quickly.

## 280: Why can long queries on a PostgreSQL replica be cancelled?

When the primary vacuums away row versions that a query on the replica still needs, the replica must either delay replaying WAL or cancel that query ("canceling statement due to conflict with recovery"). You can raise `max_standby_streaming_delay` to wait longer (more lag) or set `hot_standby_feedback = on` (the primary keeps those rows, which can cause bloat on the primary).

## 281: What extra EXPLAIN options are useful in PostgreSQL?

```sql
EXPLAIN (ANALYZE, BUFFERS, SETTINGS, WAL, VERBOSE, FORMAT JSON) SELECT ...;
```

- `SETTINGS` shows non-default planner settings that affected the plan.
- `WAL` shows how much WAL a write query produced.
- `VERBOSE` shows output columns and schema-qualified names.
- `FORMAT JSON` is handy for visual tools like explain.dalibo.com.
- `SERIALIZE` (PostgreSQL 17+) includes the cost of converting output rows to send to the client.

## 282: How does the network affect query performance?

Every query pays for the round trip between app and database. A 1 ms query over a 5 ms link takes 6 ms, and 100 sequential queries take more than half a second. Keep the app and database in the same region and zone, reduce the number of round trips, and avoid sending large result sets you then filter in the app.

## 283: How do you fetch a very large result set without running out of memory?

Stream it instead of loading everything at once. Use a server-side cursor or the driver's streaming mode and process rows in chunks.

```sql
BEGIN;
DECLARE big_cursor CURSOR FOR SELECT * FROM events WHERE day = '2026-11-01';
FETCH 1000 FROM big_cursor;
-- repeat FETCH until empty
CLOSE big_cursor;
COMMIT;
```

Or use keyset pagination in batches, which avoids a long-open transaction.

## 284: What is a covering index in MySQL and how do you see it in EXPLAIN?

When all the columns a query needs are in the index (remember InnoDB secondary indexes include the primary key), the `Extra` column shows `Using index`. That means MySQL never touched the table rows.

```sql
CREATE INDEX idx_orders_cust_status ON orders (customer_id, status);
EXPLAIN SELECT id, status FROM orders WHERE customer_id = 42;
-- Extra: Using index
```

## 285: How do you enable the hypergraph optimizer in MySQL 9.7?

The hypergraph optimizer is a newer join optimizer that is better at planning complex queries with many joins. In MySQL 9.7 LTS it's available in the Community Edition. You turn it on per session or per query:

```sql
SET optimizer_switch = 'hypergraph_optimizer=on';
```

Test it on your real workload first, because plans can change.

## 286: What is pg_plan_advice in PostgreSQL 19?

It is a new PostgreSQL 19 feature that lets you give the planner advice about how to run a query, for example a join order or scan type, to keep plans stable. Before it, PostgreSQL users relied on the third-party `pg_hint_plan` extension. Like any hint, use it only after fixing statistics and indexes, and check it again when data changes.

## 287: Why should you avoid functions in the SELECT list that run a query per row?

A function that runs its own `SELECT` (or an ORM property that triggers a query) inside the select list runs once for every row returned. It hides an N+1 problem inside the database. Rewrite it as a join or a `LATERAL` subquery so the planner can see and optimize all of the work.

## 288: How do you choose between a materialized view and a cache like Redis?

A materialized view stays inside the database, can be queried with SQL, joined and indexed, and is refreshed as a whole (or concurrently). Redis is faster for key lookups, can be updated per key and takes load off the database entirely, but it's another system to run and keep in sync. Use a materialized view for heavy reports; use Redis for hot, small, per-key data.

## 289: How can the app reduce load on the database?

- Cache repeated reads.
- Batch writes and reads.
- Move heavy reports to replicas or a data warehouse.
- Use queues to smooth out write spikes.
- Paginate everything.
- Avoid polling the database in tight loops; use `LISTEN/NOTIFY` or a message broker instead.

## 290: What is LISTEN/NOTIFY and how can it replace polling?

In PostgreSQL, a session can `LISTEN` on a channel, and any transaction can `NOTIFY` that channel with a payload when it commits. Workers then wake up only when there is something to do instead of running `SELECT` every second. Notifications are not stored, so combine it with a table for durability.

```sql
LISTEN new_job;
NOTIFY new_job, '123';
```

## 291: How do you find duplicate indexes in PostgreSQL?

Look for indexes on the same table with the same columns, or where one's columns are a leading prefix of another's.

```sql
SELECT indrelid::regclass AS table_name,
       array_agg(indexrelid::regclass) AS indexes
FROM pg_index
GROUP BY indrelid, indkey
HAVING count(*) > 1;
```

Keep the ones that enforce constraints (primary key, unique) and drop the extra ones.

## 292: Why is it a bad idea to run analytics queries on the main OLTP database?

Big reports scan and sort millions of rows, use lots of CPU, memory and I/O, push useful pages out of the cache, and (in PostgreSQL) hold back vacuum during long runs. That slows down normal user requests. Run them on a replica, or copy data into a warehouse or column store (like ClickHouse, BigQuery, or DuckDB on exports) built for that work.

## 293: What is the difference between OLTP and OLAP workloads?

OLTP (online transaction processing) is many short queries that read or write a few rows, like web app requests; row stores with B-tree indexes are built for this. OLAP (online analytical processing) is fewer, heavy queries that scan and aggregate many rows across a few columns; columnar storage and parallel scans fit this better. Tuning for one often hurts the other.

## 294: How do you make a slow dashboard query fast?

1. Check what the dashboard really needs (often daily totals, not raw rows).
2. Add indexes for its filters and date range.
3. Pre-compute aggregates into a rollup table or materialized view.
4. Cache the result for a short time.
5. Move it to a replica or warehouse if it is still heavy.

Usually step 3 gives the biggest win.

## 295: What is a "Nested Loop" with a high loops count telling you?

The inner side ran once per outer row. If the planner expected 10 outer rows but got 100,000, the inner index lookup ran 100,000 times and the query is slow. The root cause is usually a bad row estimate on the outer side, so fix the statistics (ANALYZE, extended stats) and the planner will pick a hash join instead.

## 296: How do you test if an index change helps without affecting production?

- Try it on a staging copy with production-sized data.
- In PostgreSQL, the `hypopg` extension creates hypothetical indexes that `EXPLAIN` can consider without building them.
- In MySQL, make an existing index invisible to test dropping it.
- Compare `EXPLAIN ANALYZE` and buffer numbers before and after, with a warm cache in both runs.

## 297: How do you avoid locking problems when backfilling a new column?

Update in small batches by primary key range, commit after each batch, and pause between batches so replicas and vacuum keep up. Don't run one giant `UPDATE` on the whole table.

```sql
UPDATE users SET email_domain = split_part(email, '@', 2)
WHERE id BETWEEN 1 AND 10000 AND email_domain IS NULL;
```

## 298: What is lock escalation and does it happen in PostgreSQL or MySQL?

Lock escalation means the database turns many row locks into one table lock to save memory, as SQL Server does. PostgreSQL and InnoDB don't escalate: PostgreSQL stores row locks in the row itself, and InnoDB keeps them in an efficient structure. Locking many rows still costs memory and blocks others, but you won't suddenly get a table lock.

## 299: Why might a query be slow only the first time it runs?

The first run reads pages from disk; later runs find them in memory (a "cold" versus "warm" cache). It might also pay for planning, JIT compilation, or loading catalog data into a new connection. If production queries are often cold, look at memory size and how much data the query touches, not just the warm-run timing.

## 300: How would you approach a slow page in a web app from start to finish?

1. Use APM or logs to see where the time goes: database, app code, or external calls.
2. List the queries the page runs and their count (look for N+1).
3. Take the slowest or most repeated ones and run `EXPLAIN ANALYZE`.
4. Fix with indexes, query rewrites, batching, or fetching less data.
5. Add caching where data can be slightly stale.
6. Measure the page again under realistic load.

# Advanced Questions (301-450)

## 301: How does PostgreSQL estimate how many rows match WHERE col = value?

It checks `pg_stats` for that column. If the value is in the most common values list (`most_common_vals`), it uses its stored frequency. If not, it takes the share of rows not covered by the common values and divides it evenly across the remaining distinct values (`n_distinct`). For ranges it uses the histogram bounds. NULL share comes from `null_frac`.

```sql
SELECT most_common_vals, most_common_freqs, n_distinct, null_frac
FROM pg_stats WHERE tablename = 'orders' AND attname = 'status';
```

## 302: How does the planner estimate the size of a join?

For an equality join, it roughly takes rows of the left side times rows of the right side, divided by the larger number of distinct values in the two join columns, then applies the remaining filters. It assumes values match up evenly. With skewed data (a few customers with millions of orders), the estimate can be far off in either direction.

## 303: Why do estimate errors get worse in queries with many joins?

Each join's output estimate becomes the input estimate for the next join. If each step is off by 10x, three joins can be off by 1000x. The planner then picks nested loops where a hash join was needed (or the other way around), and the query that should take 100 ms takes minutes. Fixing the first wrong estimate (usually at a scan with correlated filters) often fixes the whole plan.

## 304: How does PostgreSQL choose the join order?

For a small number of tables it tries the possible orders using dynamic programming and picks the cheapest. Two settings limit the search: `from_collapse_limit` and `join_collapse_limit` (default 8). Above that, explicit `JOIN`s are planned closer to the written order. Above `geqo_threshold` (default 12) tables, it switches to the genetic optimizer, which is faster to plan but may miss the best order.

## 305: What is GEQO?

GEQO (genetic query optimizer) is PostgreSQL's fallback for queries with many tables (12 or more by default). Trying every join order would take too long, so it uses a randomized search to find a good order. Plans can differ between runs and may be worse than the true best. For huge generated queries you can raise `geqo_threshold`, or lower `join_collapse_limit` and write joins in a good order yourself.

## 306: How does the planner decide between an index scan and a sequential scan?

It compares estimated costs. A sequential scan reads all pages in order at `seq_page_cost` each. An index scan reads index pages plus a table page per matching row at `random_page_cost`, reduced when the table order matches the index order (correlation) and when pages are likely cached (`effective_cache_size`). As the share of matching rows grows, the index scan cost passes the seq scan cost; that crossover is often at just a few percent of the table.

## 307: What is correlation in pg_stats and why does it matter?

`correlation` (from -1 to 1) shows how well the physical order of rows matches the sorted order of the column. Near 1 or -1 (like `created_at` on an append-only table) means an index range scan reads pages mostly in order and touches few of them. Near 0 means each matching row is on a different random page, so index scans for many rows are expensive and the planner prefers bitmap or sequential scans.

## 308: What does the CLUSTER command do in PostgreSQL?

`CLUSTER table USING index` rewrites the table in the order of that index, so correlation becomes 1 and range scans read fewer pages. But it takes an exclusive lock, and the order is not kept for new rows, so you have to repeat it. `pg_repack` or the PostgreSQL 19 `REPACK` command can do the same reordering with less locking.

## 309: How do page splits work in InnoDB and why do they hurt?

InnoDB stores rows in primary key order inside 16 KB pages. When a new row must go into a full page in the middle of the tree, InnoDB splits the page into two half-full pages. Splits cost extra I/O and leave pages half empty, so the table grows larger than needed and caches less data. Monotonic keys (auto-increment, UUIDv7) insert at the end and avoid most splits.

## 310: Why are random UUID primary keys especially bad in InnoDB?

The table is clustered on the primary key, so random UUIDs scatter inserts across the whole table. Every insert may need a different page in memory, which pushes out useful pages, causes many page splits, and turns writes into random I/O. Every secondary index also stores the 16-byte key. Once the table is bigger than the buffer pool, insert speed can drop sharply. Use auto-increment or UUIDv7, stored as `BINARY(16)`, not a 36-character string.

## 311: What is B-tree deduplication in PostgreSQL?

Since PostgreSQL 13, when many index entries have the same key value, B-tree indexes store the key once with a list of row pointers instead of repeating the key. Indexes on columns with many duplicates (like `status` or a foreign key) become much smaller. It's on by default. Unique indexes use it too, to hold several versions of the same row during bursts of updates.

## 312: What is bottom-up index deletion?

Added in PostgreSQL 14, it reduces index bloat from updates that aren't HOT. When an index page is about to split because of many versions of the same logical row, PostgreSQL first checks if some of those versions are already dead and removes them, avoiding the split. It keeps indexes on frequently updated tables from growing without limit between vacuums.

## 313: How does skip scan work in PostgreSQL 18?

For a composite index on `(a, b)` and a query on just `b`, skip scan treats the index as a set of small sections, one per distinct value of `a`. It jumps to `(a1, b)`, then `(a2, b)`, and so on, instead of reading the whole index. It works well when `a` has few distinct values. When `a` has many values, a full index or table scan is still cheaper, so the right index order still matters.

## 314: What is asynchronous I/O in PostgreSQL 18 and 19?

PostgreSQL 18 added an asynchronous I/O system: instead of reading one page and waiting, it can issue many reads at once. It mainly speeds up sequential scans, bitmap heap scans and vacuum, especially on cloud storage with high latency. You choose the method with `io_method` (`worker` by default, `io_uring` on Linux, or `sync`). In PostgreSQL 19, the number of I/O workers can scale automatically between `io_min_workers` and `io_max_workers`.

## 315: What is transaction ID wraparound in PostgreSQL?

PostgreSQL transaction IDs are 32-bit, so they cycle after about 4 billion. To keep old rows visible, VACUUM "freezes" old rows, marking them as visible to everyone. If vacuum can't keep up (long transactions, disabled autovacuum, huge tables), the database gets close to wraparound, forces aggressive vacuums, and in the worst case stops accepting writes until a manual vacuum finishes. Monitor `age(datfrozenxid)`.

```sql
SELECT datname, age(datfrozenxid) FROM pg_database ORDER BY 2 DESC;
```

## 316: What is an aggressive (anti-wraparound) vacuum and why can it hurt?

When a table's oldest unfrozen transaction ID passes `autovacuum_freeze_max_age` (200 million by default), autovacuum runs an aggressive vacuum that must scan every page not already marked all-frozen. On a huge table this can take hours of heavy I/O, it can't be skipped, and it isn't cancelled by lock conflicts. Regular vacuuming and freezing ahead of time (for example lower `vacuum_freeze_min_age` on append-only tables) spreads out that work.

## 317: What are MultiXacts and how can they cause problems?

When several transactions lock the same row at once (for example with `FOR SHARE`, or foreign key checks that take `FOR KEY SHARE`), PostgreSQL stores the group of lockers as a MultiXact ID. Heavy use creates many MultiXacts, which have their own storage and their own wraparound limit, and lookups into them can become a bottleneck under high concurrency. Hot parent rows referenced by many concurrent child inserts are a common cause.

## 318: What holds back the xmin horizon and why does it matter?

VACUUM can only remove dead rows older than the oldest snapshot that might still need them (the xmin horizon). That horizon is held back by long-running transactions, idle-in-transaction sessions, abandoned prepared transactions (`pg_prepared_xacts`), replication slots with `hot_standby_feedback`, and lagging logical slots. While it's held back, dead rows pile up in every table, which causes bloat and slower queries everywhere.

```sql
SELECT pid, backend_xmin, now() - xact_start AS age, state
FROM pg_stat_activity WHERE backend_xmin IS NOT NULL ORDER BY age DESC;
```

## 319: How can a replication slot fill up the disk?

A replication slot makes the primary keep all WAL that the consumer hasn't confirmed yet. If a replica or a CDC tool (like Debezium) stops reading, WAL keeps piling up until the disk is full and the database stops. Monitor slots and set `max_slot_wal_keep_size` to cap how much WAL a slot may hold.

```sql
SELECT slot_name, active,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS retained
FROM pg_replication_slots;
```

## 320: What is the InnoDB history list length?

When rows change, InnoDB keeps old versions in the undo log for transactions that might still need them. The history list length counts undo records not yet purged. A long-running transaction (even a read in `REPEATABLE READ`) stops purging, the list grows, and queries slow down because they have to walk longer version chains to find the row version they can see. Check it in `SHOW ENGINE INNODB STATUS` or `information_schema.innodb_metrics` (`trx_rseg_history_len`).

## 321: What is the InnoDB purge process?

Purge is the background job that removes old row versions from the undo log and removes delete-marked rows from indexes once no transaction needs them. It is InnoDB's version of vacuum. If writes are heavy and purge falls behind, the history list grows. You can add purge threads with `innodb_purge_threads`, but the most common fix is finding and ending long transactions.

## 322: What happened to the InnoDB change buffer and adaptive hash index?

Both are disabled by default since MySQL 8.4. The change buffer delayed secondary index updates for pages not in memory, which helped on spinning disks but added overhead and complexity on SSDs. The adaptive hash index built hash lookups on hot index pages automatically, but it caused latch contention on many workloads. You can turn them back on (`innodb_change_buffering`, `innodb_adaptive_hash_index`) if benchmarks show a gain for your workload.

## 323: What is the InnoDB doublewrite buffer?

Before writing a page to its real place, InnoDB first writes it to a doublewrite area. If the server crashes in the middle of a page write (a torn page), InnoDB can recover the full page from that copy. It roughly doubles page write I/O, but the writes are sequential so the cost is modest. Disabling it is only safe on storage that guarantees atomic 16 KB writes.

## 324: Why does PostgreSQL write full page images to the WAL, and how does that affect write volume?

With `full_page_writes = on`, the first time a page changes after a checkpoint, the whole 8 KB page goes into the WAL, protecting against torn pages. Right after each checkpoint, WAL volume spikes. Fewer checkpoints (bigger `max_wal_size`) means fewer full page images, and `wal_compression` (`lz4` or `zstd`) shrinks them, which also helps replication and backups.

## 325: How can many concurrent commits be made cheaper?

Databases use group commit: when many transactions commit at about the same time, one disk flush covers all of them. PostgreSQL's `commit_delay` can wait a few microseconds to gather more commits per flush when many are active. In MySQL, binlog group commit does the same, with `binlog_group_commit_sync_delay` as an option. Fast storage with low flush latency helps more than any setting.

## 326: What does innodb_io_capacity control?

It tells InnoDB how many I/O operations per second the storage can handle for background work like flushing dirty pages and merging. If it's too low on fast SSDs, dirty pages pile up and you get flush storms and stalls. If it's too high, background writes compete with user queries. Set it close to what your storage sustains, with `innodb_io_capacity_max` for bursts.

## 327: Why use huge pages for a database server?

Large shared memory areas (shared buffers, buffer pool) need many page table entries with normal 4 KB pages, which costs memory and CPU on TLB misses. Huge pages (2 MB) cut that overhead, and on big-memory servers they give a measurable gain. PostgreSQL uses them with `huge_pages = try` or `on` once the OS reserves them. Transparent huge pages, on the other hand, are usually recommended off for databases because of latency spikes.

## 328: How do you plan memory so the server doesn't run out?

Add up shared memory (shared buffers or buffer pool), plus per-connection memory times the number of connections, plus memory for maintenance and the OS. In PostgreSQL, one query can use `work_mem` several times (once per sort or hash node, and per parallel worker), and hash nodes can use `work_mem * hash_mem_multiplier`. Too high a setting with many connections can trigger the Linux OOM killer, which may restart the whole database.

## 329: What is hash_mem_multiplier?

It lets hash-based operations (hash joins, hash aggregates) use more memory than sorts: `work_mem * hash_mem_multiplier` (default 2.0 since PostgreSQL 15). Hash operations slow down a lot when they spill, while sorts degrade more gently, so giving hashes extra memory is usually a good trade. Raise it if `EXPLAIN ANALYZE` shows hash `Batches` above 1.

## 330: What happens when a hash join's data is skewed?

A hash join splits rows into batches by hash value when memory is short. If one join key value is very common, all its rows land in the same batch, which may not fit in memory no matter how many batches are created. That batch spills repeatedly or uses far more memory than planned. Filtering out the hot value, handling it separately, or more memory can help.

## 331: What is the Memoize node in PostgreSQL?

Added in PostgreSQL 14, Memoize sits on the inner side of a nested loop and caches results of the inner lookup by parameter value. If the outer side has many repeated join keys, later lookups for the same key are served from the cache instead of hitting the index again. Its success depends on a good estimate of distinct values; you can turn it off with `enable_memoize = off` to compare.

## 332: What is incremental sort?

Since PostgreSQL 13, if the input is already sorted by the first columns of the `ORDER BY` (say from an index on `a`), and you need `ORDER BY a, b`, PostgreSQL sorts only within each group of equal `a` values instead of sorting everything. With a `LIMIT`, it can return the first rows after sorting only the first few groups, which can be much faster than a full sort.

## 333: What are partitionwise joins and aggregates?

If two tables are partitioned the same way and you join them on the partition key, PostgreSQL can join each pair of matching partitions separately (`enable_partitionwise_join`). Similarly, it can aggregate each partition separately (`enable_partitionwise_aggregate`). Each piece is smaller and fits in memory better, and the pieces can run in parallel. Both are off by default because they add planning time.

## 334: What is run-time partition pruning?

When the partition key value isn't known at planning time (a parameter in a generic plan, or a value from a subquery or join), PostgreSQL can still skip partitions during execution. In `EXPLAIN ANALYZE` you see `Subplans Removed: N` or partitions marked `(never executed)`. Without it, generic plans on partitioned tables would scan every partition.

## 335: Why can queries on tables with many partitions get slow even with pruning?

Planning has to look at every partition before pruning, and the query must take locks on all partitions it might touch. With thousands of partitions, planning time and lock manager overhead can exceed the actual execution time, especially for short OLTP queries. Recent versions reduced this cost, but keeping the partition count moderate is still the best defense.

## 336: When does planning time matter more than execution time?

For very fast queries (well under a millisecond to run) on complex schemas: many joins, many partitions, many indexes to consider, or big `IN` lists. `EXPLAIN ANALYZE` shows `Planning Time` separately. Prepared statements that reuse a plan, fewer partitions, and simpler queries help. If planning is 5 ms and execution is 0.2 ms, a prepared statement is the obvious fix.

## 337: What is cursor_tuple_fraction?

When you use a cursor, PostgreSQL assumes you will fetch only part of the result (10% by default) and prefers plans that return the first rows fast, like an index scan in sort order, even if the full result would be slower to get. If you always fetch everything through the cursor, set it to 1.0 so the planner optimizes for total time.

## 338: How do you get statistics on an expression?

PostgreSQL collects statistics for expression indexes automatically on `ANALYZE`, so a query using `LOWER(email)` gets good estimates once that index exists. Since PostgreSQL 14 you can also create statistics on an expression without an index:

```sql
CREATE STATISTICS stats_order_day ON (date_trunc('day', created_at)) FROM orders;
ANALYZE orders;
```

## 339: What are optimization fences and when would you use one on purpose?

A fence stops the planner from merging part of a query into the rest. In PostgreSQL, `WITH ... AS MATERIALIZED` and the old trick `OFFSET 0` in a subquery act as fences. You might use one when the planner keeps pushing a filter into a subquery in a way that leads to a bad plan, forcing it to compute that part first. It's a workaround; better statistics are the cleaner fix.

```sql
WITH active AS MATERIALIZED (
  SELECT id FROM users WHERE last_login > now() - interval '1 day'
)
SELECT * FROM orders o JOIN active a ON a.id = o.user_id;
```

## 340: How do IN lists with different lengths affect query statistics tools?

Each different number of values produces a different query text, so in older versions `pg_stat_statements` tracked `IN ($1, $2)` and `IN ($1, $2, $3)` as separate entries and the real cost of the query was spread across hundreds of rows. PostgreSQL 18 groups lists of constants into one entry. Using `= ANY($1)` with an array avoids the problem on any version and also allows plan reuse.

## 341: What causes a query plan to suddenly change, and how do you investigate it?

Common causes: statistics changed after `ANALYZE` (new data crossed a threshold), the data grew, a generic plan replaced custom plans, an index was added or dropped, or a setting changed. Compare the old and new plans (from `auto_explain` logs), check `pg_stats` for the columns involved, and look at the estimated versus actual rows at the first node that differs.

## 342: How can you keep plans stable for important queries?

- Keep statistics accurate (tuned autovacuum analyze, extended stats, higher targets on skewed columns).
- Design indexes so the good plan is clearly cheapest.
- Avoid optional-filter queries that need different plans for different inputs.
- Use `plan_cache_mode` carefully.
- As a last resort, use hints: `pg_plan_advice` (PostgreSQL 19) or `pg_hint_plan`, or optimizer hints in MySQL.

## 343: Why can sequences or auto-increment become a bottleneck?

Every insert needs a new value. In PostgreSQL, a sequence call is cheap but shared, and under extreme insert rates you can use `CACHE` so each session grabs a block of values. In MySQL, `innodb_autoinc_lock_mode = 2` (the default since 8.0) uses lightweight allocation and allows high concurrency, at the cost of IDs not being consecutive within a multi-row insert. IDs are never gap-free, so don't rely on that.

## 344: What is right-edge contention on an index?

With an increasing key (auto-increment ID or timestamp), every concurrent insert goes to the last page of the index. Under very high insert concurrency, sessions compete for the lock on that one page. It's usually only a problem at very high write rates. Workarounds include hash partitioning, adding a small random or per-worker prefix to the key, or batching inserts.

## 345: How do you measure write amplification from indexes?

Compare the WAL generated by a write to the size of the data written. In PostgreSQL, `EXPLAIN (ANALYZE, WAL)` shows WAL records and bytes for a statement, and `pg_stat_wal` shows totals. Run the same update with and without an index and compare. If each 100-byte update writes several kilobytes of WAL, too many indexes or non-HOT updates are often the reason.

## 346: When is a BRIN index better than a B-tree for time-series data, and when is it worse?

BRIN is better when data arrives in time order, the table is huge, and queries ask for ranges (a day, a week): the index is tiny and cheap to maintain. It is worse for point lookups or small ranges, because it narrows down only to blocks of pages (128 by default), and useless if rows arrive out of order or get updated and moved. Many systems use BRIN on the time column plus a B-tree on `(series_id, time)`.

## 347: Why do you need an index on the child column for ON DELETE CASCADE?

When a parent row is deleted, the database must find all child rows that reference it. Without an index on the child's foreign key column, each parent delete scans the whole child table. Deleting 1,000 parents means 1,000 full scans of the child table, and these happen inside the delete transaction, holding locks the whole time.

## 348: How do you delete a large tree of related data efficiently?

A cascading delete of a customer with millions of related rows runs as one huge transaction: long locks, lots of WAL, replica lag. Instead, delete from the leaves up in batches (order items, then orders, then the customer), commit between batches, and make sure every foreign key column is indexed. Partitioning by tenant lets you drop all their data at once.

## 349: What semi-join strategies does MySQL use for IN subqueries?

For `WHERE x IN (SELECT ...)`, MySQL can use: table pull-out (turn it into a join when the subquery side is unique), FirstMatch (stop at the first match per outer row), LooseScan (read one entry per distinct value from an index), Materialization (build a temp table of the subquery result, with an index), and DuplicateWeedout (do a normal join and remove duplicates). `EXPLAIN` shows which one was picked, and `optimizer_switch` can turn each off for testing.

## 350: What is derived table merging and condition pushdown in MySQL?

MySQL tries to merge a derived table (a subquery in `FROM`) into the outer query, so it can use indexes of the underlying table. If the derived table can't be merged (it has `GROUP BY`, `LIMIT` and so on), it's materialized into a temp table. Since 8.0.22, MySQL can push outer `WHERE` conditions into a materialized derived table, so fewer rows are materialized.

## 351: What is the MySQL optimizer trace?

It's a detailed JSON log of how the optimizer made its decisions for one query: which indexes it considered, their estimated costs, the join orders it tried, and why it picked the final plan. Use it when `EXPLAIN` shows a choice you don't understand.

```sql
SET optimizer_trace = 'enabled=on';
SELECT * FROM orders WHERE customer_id = 42 AND status = 'paid';
SELECT trace FROM information_schema.optimizer_trace;
SET optimizer_trace = 'enabled=off';
```

## 352: What are index dives in MySQL?

To estimate how many rows match a range or an `IN` list, MySQL can "dive" into the index and count entries for each range, which is accurate but costs time. When an `IN` list has more values than `eq_range_index_dive_limit` (200 by default), it switches to using index statistics, which is faster but can be much less accurate. Very long `IN` lists can therefore get worse plans.

## 353: How does InnoDB calculate index statistics, and why might they be wrong?

InnoDB samples a number of random index pages (`innodb_stats_persistent_sample_pages`, default 20) and extrapolates the number of distinct values. On large tables with skewed data, a small sample can be far off, leading to bad plans. Raise the sample size for that table and run `ANALYZE TABLE`.

```sql
ALTER TABLE orders STATS_SAMPLE_PAGES = 200;
ANALYZE TABLE orders;
```

## 354: How does InnoDB keep a big table scan from flushing the buffer pool?

The buffer pool uses an LRU list split into a "young" and an "old" part. New pages enter at the midpoint, in the old part, and move to the young part only if they're accessed again after `innodb_old_blocks_time` (1 second by default). A one-time full scan reads pages through the old part and they get evicted first, so the hot working set stays in memory.

## 355: How does PostgreSQL protect its cache from large sequential scans?

For sequential scans of tables bigger than a quarter of `shared_buffers`, and for VACUUM and bulk writes like `COPY`, PostgreSQL uses a small ring buffer (a few hundred kilobytes to a few megabytes) and recycles those buffers instead of filling the whole cache. That stops one big scan from evicting everyone else's hot pages. It also means a big table won't get cached just by scanning it.

## 356: What is pg_prewarm used for?

`pg_prewarm` loads a table or index into the cache on demand. With its `autoprewarm` background worker, it also saves the list of cached pages periodically and reloads them after a restart, so the server doesn't start with a cold cache and slow queries.

```sql
CREATE EXTENSION pg_prewarm;
SELECT pg_prewarm('orders');
```

## 357: Why is a high max_connections bad in PostgreSQL?

Each connection is a process with its own memory, and some internal structures scale with the total connection count, like the work to build a snapshot. Thousands of mostly idle connections still cost memory and CPU, and when many become active, they fight for CPU and locks and throughput drops. Keep `max_connections` modest (a few hundred at most) and put a pooler in front.

## 358: What is a cache stampede and how do you prevent it?

When a popular cache key expires, many requests miss at once and all run the same expensive query, which can overload the database. Ways to prevent it:

- Let one request rebuild the value while others wait or get the old value (a lock or "single flight").
- Refresh hot keys in the background before they expire.
- Add random jitter to TTLs so keys don't expire together.

## 359: How do you choose a sharding key?

A good shard key spreads data and load evenly, is present in almost every query so requests go to one shard, and keeps data that is queried together on the same shard. For SaaS, `tenant_id` is the common choice. A bad key (like a date) sends all new writes to one shard, or forces most queries to visit every shard.

## 360: What problems come with cross-shard queries?

A query without the shard key must go to every shard and combine the results, so latency equals the slowest shard and load grows with the shard count. Joins between tables on different shards need data to move over the network. Transactions across shards need two-phase commit or have weaker guarantees. Global unique constraints and sorting across shards are also harder.

## 361: What are Citus and Vitess?

Both add sharding on top of an existing database. Citus is a PostgreSQL extension that distributes tables across worker nodes by a distribution column, pushes queries down to the shards, and supports co-located joins and reference tables copied to every node. Vitess sits in front of MySQL, routing queries to shards, handling resharding, and pooling connections. Both work best when queries include the shard key.

## 362: How do you generate unique IDs across shards?

- UUIDv7: no coordination needed, roughly time-ordered, 16 bytes.
- Snowflake-style 64-bit IDs: timestamp plus machine ID plus sequence; compact and ordered.
- Per-shard sequences with a shard prefix or with each shard using a different offset.

Avoid a single central ID service in the write path, since it becomes a bottleneck and a single point of failure.

## 363: What is a hot shard and how do you fix it?

A hot shard gets much more traffic than the others, often because one tenant is huge or the shard key is badly chosen. Fixes include moving the big tenant to its own shard, splitting it with a compound key (tenant plus something else), adding read replicas for that shard, or caching its hot data.

## 364: What is the cost of synchronous replication?

With synchronous replication, the primary waits for at least one replica to confirm the WAL before the commit returns. You don't lose committed data if the primary dies, but every commit now pays the network round trip to the replica, and if the replica is slow or down, commits stall. PostgreSQL lets you set `synchronous_commit` per transaction, so only important writes pay that cost.

## 365: How can logical replication help with big migrations?

Logical replication copies row changes, not physical pages, so the target can be a different major version or have a different layout. You can set up a new server, let it catch up, then switch the app over with only seconds of downtime. It is used for major version upgrades, moving to new hardware, and splitting databases. PostgreSQL 19 also replicates sequence values, which removed a manual step at cutover.

## 366: What is CQRS and how does it relate to database performance?

CQRS (command query responsibility segregation) separates the write model from the read model. Writes go to normalized tables, and read-optimized copies (denormalized tables, search indexes, caches) are updated from them, often asynchronously. Each side can be tuned separately. The cost is complexity and eventual consistency between writes and reads.

## 367: How do you handle very high write rates for counters?

A single row like `views = views + 1` serializes every writer on its lock. Options:

- Split the counter into N rows (`counter_id, slot`) and update a random slot; sum them when reading.
- Buffer increments in memory or Redis and write aggregates every few seconds.
- Insert events into an append-only table and aggregate periodically.

## 368: How should you design a job queue table in PostgreSQL?

Keep it small: delete or move finished jobs quickly so the table and its indexes stay in memory. Use a partial index on queued jobs, `FOR UPDATE SKIP LOCKED` for claiming, and short transactions. Tune autovacuum to run very often, because a queue table creates dead rows constantly. Long transactions elsewhere in the database will cause bloat here first.

```sql
CREATE INDEX idx_jobs_queued ON jobs (run_at) WHERE status = 'queued';
```

## 369: What is the expand-and-contract pattern for schema changes?

It's a way to change a schema without downtime, in steps: (1) expand: add the new column or table alongside the old one; (2) deploy code that writes to both; (3) backfill old rows in batches; (4) switch reads to the new structure; (5) contract: stop writing to the old one and drop it. Each step is safe on its own and can be rolled back.

## 370: What happens if CREATE INDEX CONCURRENTLY fails?

It leaves behind an index marked `INVALID`. That index is still updated on every write (costing write time) but is never used by queries. Find it, drop it, and try again.

```sql
SELECT indexrelid::regclass FROM pg_index WHERE NOT indisvalid;
DROP INDEX CONCURRENTLY idx_orders_customer_id;
```

Common causes are a unique violation during the build, a deadlock, or a cancelled statement.

## 371: How does column order affect row size in PostgreSQL?

PostgreSQL aligns fixed-size columns to their size: a `bigint` must start on an 8-byte boundary. Putting a `boolean` before a `bigint` adds 7 bytes of padding. Ordering columns from largest fixed-width (`bigint`, `timestamptz`) to smaller ones (`int`, `smallint`, `boolean`), and variable-width (`text`, `numeric`) last, can shrink each row by several bytes, which adds up over billions of rows.

## 372: How much space do NULLs take?

In PostgreSQL, a NULL takes no space in the data area; it's marked in a null bitmap, which exists only if the row has at least one NULL (one bit per column). In InnoDB's compact and dynamic formats, NULLs are also tracked in a bitmap and take no data space. So sparse, mostly NULL columns are cheap, although very wide tables have other costs.

## 373: How does compression help database performance?

Compressed data takes fewer pages, so more fits in memory and less I/O is needed, at the cost of CPU to compress and decompress. PostgreSQL compresses large values via TOAST (lz4 by default in PostgreSQL 19), and WAL can be compressed with `wal_compression`. InnoDB supports table and page compression. For analytics, columnar formats compress much better than row storage.

## 374: How do you make full-text search fast and avoid recomputing tsvector?

Store the `tsvector` in a generated column and index it, so it's computed once on write. Ranking (`ts_rank`) still has to read every matching row's vector, so for broad searches limit the candidate set first.

```sql
ALTER TABLE posts ADD COLUMN search tsvector
  GENERATED ALWAYS AS (to_tsvector('english', coalesce(title, '') || ' ' || coalesce(body, ''))) STORED;
CREATE INDEX idx_posts_search ON posts USING GIN (search);

SELECT id, title FROM posts
WHERE search @@ websearch_to_tsquery('english', 'index tuning')
ORDER BY ts_rank(search, websearch_to_tsquery('english', 'index tuning')) DESC
LIMIT 20;
```

## 375: How do you find the nearest matches by similarity quickly?

GiST indexes support "nearest neighbor" ordering with the `<->` distance operator, so the database reads only the closest entries instead of computing distance for every row. This works for trigrams (`pg_trgm`) and for geography (PostGIS).

```sql
CREATE INDEX idx_products_name_gist ON products USING GIST (name gist_trgm_ops);
SELECT name FROM products ORDER BY name <-> 'iphne' LIMIT 5;
```

## 376: How do you make geospatial queries fast?

Use PostGIS with a GiST index on the geometry or geography column. Use index-aware functions like `ST_DWithin` for "within X meters" (not `ST_Distance(...) < X`, which can't use the index), and `<->` with `ORDER BY ... LIMIT` for nearest neighbors.

```sql
CREATE INDEX idx_shops_geo ON shops USING GIST (location);
SELECT name FROM shops
WHERE ST_DWithin(location, ST_MakePoint(13.40, 52.52)::geography, 1000);
```

## 377: How do you implement keyset pagination when the sort column isn't unique or can be NULL?

Add a unique tie-breaker (usually the primary key) to both the `ORDER BY` and the cursor, and compare with a row value. For NULLs, either make the column `NOT NULL`, use `COALESCE` with a matching expression index, or handle the NULL group as a separate step. The index must match the full sort: `(created_at, id)`.

```sql
SELECT id, created_at FROM posts
WHERE (created_at, id) > ($1, $2)
ORDER BY created_at, id
LIMIT 20;
```

## 378: How do you do keyset pagination with mixed sort directions?

A row comparison like `(a, b) > (x, y)` only works when all columns sort the same way. For `ORDER BY score DESC, id ASC`, write the condition out, and make sure the index has the same mixed order.

```sql
CREATE INDEX idx_players_score_id ON players (score DESC, id ASC);

SELECT id, score FROM players
WHERE score < $1 OR (score = $1 AND id > $2)
ORDER BY score DESC, id ASC
LIMIT 20;
```

Alternatively, sort by `-score` with an expression index so all directions match.

## 379: What is a deferred join and how does it speed up OFFSET pagination in MySQL?

Instead of fetching full rows for all skipped records, first find just the IDs of the wanted page using a covering index, then join back to get the full rows only for those IDs.

```sql
SELECT p.* FROM posts p
JOIN (
  SELECT id FROM posts ORDER BY created_at DESC LIMIT 20 OFFSET 50000
) page USING (id)
ORDER BY p.created_at DESC;
```

The inner query still skips 50,000 entries, but only in the small index, not by reading 50,000 full rows.

## 380: What does Serializable isolation cost in PostgreSQL?

PostgreSQL's Serializable uses SSI (serializable snapshot isolation). It doesn't block more than Repeatable Read, but it tracks read dependencies with predicate locks and aborts transactions that could produce a result impossible in some serial order. Costs are memory for predicate locks, extra CPU, and more failed transactions under contention, so the app must retry. Index scans give finer-grained predicate locks than sequential scans, which reduces false conflicts.

## 381: How should the app handle serialization failures and deadlocks?

Treat them as normal and retry the whole transaction from the start, with a small random delay and a limit on attempts. In PostgreSQL the error codes are `40001` (serialization failure) and `40P01` (deadlock); in MySQL deadlock is error 1213. Don't retry only the failed statement, because the earlier reads in the transaction may now be stale.

## 382: What is write skew?

Two transactions each read the same data, make a decision based on it, and write to different rows, so neither sees the other's write. Example: two doctors both check "at least one other doctor is on call" and both go off call. Repeatable Read (snapshot isolation) doesn't stop this. Fix it with Serializable, by locking the rows you read (`FOR UPDATE`), or with a constraint that catches the conflict.

## 383: How do foreign key checks cause lock contention?

Inserting a child row takes a `FOR KEY SHARE` lock on the parent row in PostgreSQL (a shared lock in InnoDB) to make sure it isn't deleted meanwhile. Many concurrent inserts referencing the same parent all lock that one row, creating MultiXacts in PostgreSQL. An update to the parent's key or a delete then waits for all of them. Hot parent rows (one tenant, one popular product) are where this shows up.

## 384: Which ALTER TABLE operations take the strongest lock in PostgreSQL?

Most `ALTER TABLE` forms take an `ACCESS EXCLUSIVE` lock, which blocks even reads. Many are fast (adding a nullable column, adding a column with a constant default, dropping a column), so the lock is brief, as long as it doesn't wait in the queue. Others rewrite the table while holding the lock, like changing a column type in most cases or adding a volatile default. Some forms use weaker locks, like `VALIDATE CONSTRAINT` and `SET STATISTICS`.

## 385: When will the planner use a partial index?

Only when it can prove from the query that the query's `WHERE` clause implies the index's condition. `WHERE status = 'pending' AND ...` matches an index with `WHERE status = 'pending'`. A parameter (`status = $1`) usually doesn't match in a generic plan, because the planner can't know the value. Write the condition literally in the query for partial indexes to be used reliably.

## 386: What rules apply to expression indexes?

The expression in the query must match the index expression exactly (same functions, same argument order, same casts). The functions must be `IMMUTABLE`, meaning the same input always gives the same output; for example, a timestamp-to-text conversion that depends on the session time zone isn't allowed. Expression indexes add cost to every write that changes the involved columns.

## 387: How does function volatility affect performance in PostgreSQL?

- `VOLATILE` (default): may return different values each call, so it runs for every row and blocks many optimizations.
- `STABLE`: same result within one statement; can be used in index scans with parameters.
- `IMMUTABLE`: always the same for the same input; can be folded at plan time and used in index expressions.

Marking your functions with the correct, strictest level lets the planner do more. Marking them wrongly gives wrong results.

## 388: Why are simple SQL functions faster than PL/pgSQL functions inside queries?

A simple `LANGUAGE sql` function with a single `SELECT` can be inlined: the planner pastes its body into the calling query and optimizes everything together, including using indexes. A PL/pgSQL function is a black box to the planner, runs separately for each call, and its row estimate is a fixed guess. For helpers used in `WHERE` or `FROM`, prefer inlinable SQL functions.

## 389: How do you fix bad row estimates for set-returning functions?

The planner assumes a set-returning function returns 1000 rows (the default `ROWS` setting) unless told otherwise, which can lead to bad join choices. Set a realistic `ROWS` value on the function, or for more control, attach a planner support function (written in C). Another option is putting the result in a temp table and running `ANALYZE` on it.

```sql
ALTER FUNCTION active_user_ids() ROWS 50;
```

## 390: What are the main sort methods in PostgreSQL and when does each appear?

- **quicksort:** everything fits in `work_mem`.
- **top-N heapsort:** `ORDER BY ... LIMIT N`; keeps only the N best rows, using little memory.
- **external merge:** data doesn't fit; sorted runs are written to disk and merged.
- **incremental sort:** input is already partly sorted.

An external merge in a frequent query is a sign to add an index for the order, reduce the data sorted, or give that query more `work_mem`.

## 391: How does collation affect sorting and comparison speed?

Linguistic collations (like `en_US` via glibc or ICU) compare strings using language rules, which is much slower than the `C` collation's byte comparison. Sorts and B-tree operations on text get slower, and some index uses like `LIKE` prefix need special handling. For columns that never need linguistic sorting (codes, hashes, IDs), use `COLLATE "C"`. PostgreSQL 17 also added a `builtin` collation provider with a fast `C.UTF-8` locale.

## 392: Why might a query be fast in psql but slow from the application?

- The app uses a prepared statement and gets a generic plan, while psql plans with real values.
- The app sends parameters with a different type (for example `numeric` or `text` instead of `bigint`), which forces casts and blocks index use.
- Different session settings (`search_path`, `work_mem`, time zone, `jit`).
- The app's ORM adds extra clauses or wraps it differently.
- The app fetches all rows over the network, while psql timing excluded that.

Log the exact query with `auto_explain` to see the plan the app actually gets.

## 393: What is pipeline mode and how does it reduce latency?

Normally a client sends a query, waits for the result, then sends the next one. In pipeline mode (libpq since PostgreSQL 14, supported by drivers like psycopg 3 and pgx), the client sends many queries without waiting and reads the results later. For many small independent queries over a network with real latency, this can cut total time a lot. Errors stop the rest of the pipeline until a sync point.

## 394: How do JDBC driver settings affect batch insert speed?

By default, JDBC batches may still send one statement per row. With MySQL Connector/J, `rewriteBatchedStatements=true` rewrites batches into multi-row `INSERT`s. With the PostgreSQL JDBC driver, `reWriteBatchedInserts=true` does the same. Both can make bulk inserts many times faster. Check your ORM's batch size settings too (for example `hibernate.jdbc.batch_size`), and note that identity-generated IDs can disable batching in Hibernate.

## 395: How do you plan database capacity for growth?

Track table and index size growth, query rate, and peak CPU, I/O and connections over months. Project when the working set will outgrow memory and when the disk will fill. Know the limits of your current setup (biggest instance, replica count) so you start partitioning, archiving or sharding before you hit them, not during an outage.

## 396: When should you scale up, add replicas, or shard?

- **Scale up** (bigger server) first: it's simple and modern servers are huge.
- **Add replicas** when reads dominate and can tolerate a little lag.
- **Partition and archive** when tables are huge but most queries touch recent data.
- **Shard** only when writes or data size exceed what one primary can handle even after tuning.

Each step adds more operational work than the one before it.

## 397: What mistakes make database benchmarks misleading?

- Data much smaller than production, so everything is cached.
- One client thread, when production has hundreds.
- Unrealistic query mix or uniform data with no skew.
- No warm-up, or comparing a cold run to a warm one.
- Measuring only averages instead of percentiles.
- Running the load generator on the same machine as the database.
- Changing several settings at once.

## 398: A query was fast for months and is now slow. How do you investigate?

1. Compare the current plan with an old one (from `auto_explain` logs or memory).
2. Check data growth: maybe it crossed a size where the plan changed or data no longer fits in memory.
3. Check statistics freshness (`last_autoanalyze`) and estimate accuracy.
4. Check for bloat on the table and its indexes.
5. Check if a dropped index, a new index, a version upgrade or a setting change happened.
6. Check for lock waits rather than slow execution.

## 399: The database CPU is at 100%. What do you do?

Look at what is running right now (`pg_stat_activity`, `SHOW PROCESSLIST`) and at the top queries by total time (`pg_stat_statements`, `sys.statement_analysis`). Usually one or two queries cause most of it, often a new query with a missing index or a query whose plan changed. Kill runaway queries if needed, then fix the cause. Also check for a jump in connections or request volume, and for many concurrent sessions spinning on locks.

## 400: The disk I/O is saturated. What are the likely causes?

- The working set no longer fits in memory, so reads go to disk.
- Queries doing large sequential scans or sorts spilling to disk.
- Heavy writes: many indexes, frequent checkpoints, large full page writes.
- Autovacuum or a backup running at the same time as peak load.
- Bloat making tables much larger than the live data.

Check buffer hit ratios, temp file usage, checkpoint stats and per-query buffer reads to tell which one it is.

## 401: The app gets "too many connections" errors. How do you fix it properly?

Raising `max_connections` is a short-term patch that often makes things worse. Find who holds the connections (`pg_stat_activity` grouped by application and state). Common causes are leaked connections that are never returned to the pool, too many app instances each with a big pool, idle-in-transaction sessions, or slow queries holding connections longer. Put a pooler like PgBouncer in front, size pools from the database side, and fix the leaks.

## 402: Replica lag keeps growing. What can cause it?

- The primary writes more than the replica can replay (replay is often single-threaded in PostgreSQL).
- Big batch writes or index builds on the primary.
- Long queries on the replica that conflict with replay and get it to pause.
- A slower disk or a smaller instance on the replica.
- Network limits between regions.

In MySQL, enabling parallel replication (`replica_parallel_workers`) helps a lot. In both, break big writes into smaller batches.

## 403: The WAL directory is filling the disk. What are the usual causes?

- An inactive or lagging replication slot holding WAL.
- WAL archiving (`archive_command` or `archive_library`) failing, so files are never removed.
- `max_wal_size` or `wal_keep_size` set very high.
- A burst of writes (big migration, bulk load) producing WAL faster than checkpoints recycle it.

Check `pg_replication_slots` and `pg_stat_archiver` first. Never delete WAL files by hand.

## 404: A table keeps bloating even though autovacuum is on. What do you check?

1. Is something holding back the xmin horizon (long transactions, idle-in-transaction sessions, old prepared transactions, slots with feedback)?
2. Is autovacuum running often enough for this table (`last_autovacuum`, `n_dead_tup`), or are thresholds too high?
3. Is it being throttled too much by cost limits?
4. Is it getting cancelled by lock conflicts (frequent DDL or `LOCK TABLE`)?
5. Are all autovacuum workers busy with other big tables?

## 405: Deadlocks started after a deploy. How do you find the cause?

Read the deadlock details: PostgreSQL logs both statements and the locks involved; MySQL shows them in `SHOW ENGINE INNODB STATUS` or the error log with `innodb_print_all_deadlocks`. Look for the new code path that touches the same tables in a different order, a new missing index that makes updates lock more rows (in InnoDB), or a new foreign key. Fix the lock order, add the index, or shorten the transaction.

## 406: A query is fast on staging but slow in production. Why?

- Production has far more data, so the plan is different or the data doesn't fit in memory.
- Different data distribution (skew) changes estimates.
- Statistics are stale in production.
- Production has concurrent load and lock waits.
- Different versions, settings or indexes between the two environments.
- Production tables are bloated.

Get the real plan in production with `EXPLAIN (ANALYZE, BUFFERS)` (carefully) or `auto_explain`.

## 407: How would you design a social feed so it loads fast?

Two main approaches:

- **Fan-out on read:** when a user opens the feed, query the latest posts from everyone they follow. Simple, but slow for users who follow thousands of accounts.
- **Fan-out on write:** when someone posts, insert a row into each follower's feed table. Reads become a simple indexed query by `(user_id, created_at)`, but writes are heavy for accounts with millions of followers.

Most large systems mix them: fan-out on write for normal accounts, fan-out on read for huge ones, with keyset pagination for the feed.

## 408: How would you build a leaderboard with frequent score updates?

A query like `ORDER BY score DESC LIMIT 100` with an index on `score` is fast for the top list. Getting one user's rank (`COUNT(*) WHERE score > x`) is slower on huge tables, since it counts rows. Options: cache the top N, compute ranks periodically into a table, or use a Redis sorted set for real-time ranks and store the source of truth in SQL. Batch score updates if they arrive very often.

## 409: How do you make a search page with many optional filters and sort options fast?

- Build the `WHERE` clause dynamically with only the filters used.
- Index the most common filter combinations, with the tenant or most selective column first.
- Limit the sort options to ones you can support with indexes.
- Use keyset pagination and avoid exact total counts.
- For free text plus many facets, move the search to a search engine and keep SQL for the source of truth.

## 410: How would you store and query audit logs at large scale?

Make the table append-only, partition it by time, and use BRIN on the timestamp plus B-tree indexes on the few columns people search by (like `entity_id` or `actor_id`). Store the variable details in `jsonb`. Drop or archive old partitions on a schedule. Write logs asynchronously or in batches so they don't slow down user requests. Very large volumes may belong in a log or column store instead.

## 411: How do you deal with a noisy neighbor in a multi-tenant database?

One tenant's heavy queries slow everyone else. Options:

- Set per-role or per-tenant `statement_timeout` and connection limits.
- Rate-limit expensive endpoints per tenant.
- Send that tenant's reports to a replica.
- Move the big tenant to its own database or shard.
- Make sure every index starts with `tenant_id` so small tenants aren't affected by big tenants' data.

## 412: How do you change a primary key from int to bigint on a huge table?

A direct `ALTER COLUMN TYPE bigint` rewrites the table and all indexes under an exclusive lock, which can take hours. A safer path: add a new `bigint` column, keep it in sync with a trigger, backfill it in batches, build a unique index on it concurrently, then in a short maintenance step swap it in as the primary key (using that index) and update foreign keys. In MySQL, tools like gh-ost do the copy online. Use `bigint` from the start to avoid this.

## 413: A table with heavy soft deletes is getting slow. What would you do?

Most rows are probably deleted, but every index still includes them. Use partial indexes with `WHERE deleted_at IS NULL` (PostgreSQL), or put the deleted flag in composite indexes (MySQL). Move soft-deleted rows older than a retention period to an archive table in batches. If deleted rows are rarely needed, consider moving them to a separate table at delete time instead of flagging them.

## 414: A query with WHERE status IN (...) ORDER BY created_at LIMIT 20 is slow. How do you fix it?

With an index on `(status, created_at)` the database has to merge several sorted ranges, one per status. PostgreSQL might read all matching rows and sort them. Options: an index on `created_at` with a partial condition for those statuses, or rewrite as a `UNION ALL` of one `LIMIT 20` query per status, then sort and limit the small combined result.

```sql
SELECT * FROM (
  (SELECT * FROM orders WHERE status = 'new'     ORDER BY created_at DESC LIMIT 20)
  UNION ALL
  (SELECT * FROM orders WHERE status = 'pending' ORDER BY created_at DESC LIMIT 20)
) t ORDER BY created_at DESC LIMIT 20;
```

## 415: A product search with LIKE '%term%' became slow as the catalog grew. What are your options?

1. In PostgreSQL, add a `pg_trgm` GIN index; this often turns seconds into milliseconds.
2. If users type words, switch to full-text search with a stored `tsvector` and GIN index.
3. For typo tolerance, ranking, synonyms and facets at scale, use a search engine (OpenSearch, Meilisearch, and so on) fed from the database.

In MySQL, use a `FULLTEXT` index, since there's no trigram index.

## 416: A report joining six tables uses nested loops and takes minutes. What do you look at?

Find the node where estimated rows are far below actual rows. Nested loops are chosen when the planner thinks the outer side is small. Fix the estimate with `ANALYZE`, extended statistics for correlated filter columns, or a higher statistics target. Check that join columns have matching types and indexes. As a test, `SET enable_nestloop = off` for the session shows if a hash join plan would be faster, which confirms the problem is estimates.

## 417: How would you handle very high-volume event ingestion in a SQL database?

- Insert in batches with `COPY` or multi-row inserts.
- Keep indexes on the ingest table to a minimum.
- Partition by time and drop old partitions.
- Use BRIN for time ranges.
- Consider `synchronous_commit = off` for events you can afford to lose a little of.
- Put a queue (Kafka, SQS) in front to absorb spikes.
- Aggregate into rollup tables for reads.

If volume keeps growing, a time-series or column store may fit better.

## 418: How do you handle a flash sale where many users buy the same product at once?

The stock row becomes a hot row. Options:

- Do the decrement in one atomic statement with a condition, so no read-then-write race: `UPDATE stock SET qty = qty - 1 WHERE product_id = $1 AND qty > 0`.
- Keep the transaction tiny; don't call payment APIs while holding the lock.
- Split stock into several rows (buckets) to spread the lock.
- Reserve stock in Redis first and write orders to the database through a queue.

## 419: How do you stop one bad query from taking down the database?

- Set `statement_timeout` (and `idle_in_transaction_session_timeout`) per role.
- Use separate database users for the app, background jobs and reports, each with its own limits.
- Cap connections per user or pool.
- Run heavy queries on replicas.
- Review new queries before deploy.
- Alert on long-running queries so a human can step in early.

## 420: Which database metrics should you monitor?

- Query latency (p50, p95, p99) and throughput.
- Top queries by total time.
- Active and idle-in-transaction connections.
- CPU, memory, disk I/O, disk space.
- Cache hit ratio and temp file usage.
- Lock waits and deadlocks.
- Replication lag and slot retained WAL.
- Dead tuples, autovacuum activity and transaction ID age (PostgreSQL), history list length (InnoDB).
- Checkpoint frequency.

## 421: What are wait events and how do they help diagnose slowness?

In PostgreSQL, `pg_stat_activity.wait_event_type` and `wait_event` show what an active session is waiting on: `Lock` (row or table locks), `LWLock` (internal contention), `IO` (disk reads or WAL writes), `Client` (waiting for the app), and so on. Sampling them over time (with tools like `pg_wait_sampling` or your monitoring platform) shows where time goes across the whole server, not just in one query. MySQL exposes the same idea in `performance_schema` wait tables.

## 422: What should you do after a major version upgrade to avoid slow queries?

Run `ANALYZE` on the whole database if statistics weren't carried over (PostgreSQL 18+ `pg_upgrade` keeps most planner statistics, but extended statistics still need a fresh `ANALYZE`). Compare top query plans and timings with the old version. Check for changed defaults (for example JIT off by default in PostgreSQL 19, or InnoDB changes in MySQL 8.4). Keep a way to roll back or a replica on the old version until you're confident.

## 423: How do you decide between denormalizing, caching and changing the database?

Start with the cheapest change that fixes the measured problem. If a query is slow because of a missing index or a bad plan, fix that. If it's correct but does too much work on every request, cache or pre-compute it (materialized view, rollup table). Denormalize when a join is on a very hot path and the copied data rarely changes. Change or add a database type only when the workload is truly different (full-text search, analytics, time series).

## 424: What are the performance trade-offs of using an ORM versus raw SQL?

ORMs save time and make simple CRUD consistent, and most generate fine SQL for basic queries. The risks are hidden N+1 queries, over-fetching, and awkward SQL for complex reports. Raw SQL gives full control for the hard cases. A common approach is to use the ORM for everyday work, write raw SQL or a query builder for complex or hot queries, and always check generated SQL in logs.

## 425: What do you check when reviewing a pull request that changes SQL or the schema?

- Does every new query have an index that supports its filter and sort?
- Is there any query in a loop (N+1)?
- Are results paginated and limited?
- Does the migration lock a big table (index without `CONCURRENTLY`, type changes, NOT NULL)?
- Are there backfills that need batching?
- Are data types and join column types consistent?
- Do new foreign keys have indexes on the child column?
- Has someone run `EXPLAIN` on realistic data?

## 426: How do you make sure index changes don't break other queries?

Before dropping an index, check its usage (`pg_stat_user_indexes`, `sys.schema_unused_indexes`) over a full business cycle, on the primary and all replicas. In MySQL, make it invisible first. Before adding one, consider write cost and whether it replaces an older index. After the change, watch top query metrics for regressions and keep the rollback (re-create statement) ready.

## 427: How do generic plans interact with partitioned tables and prepared statements?

With a generic plan, the partition key value isn't known at planning time, so pruning has to happen at execution (run-time pruning). Planning still considers all partitions, and older versions also locked all of them, which hurt with many partitions. If you see slow prepared statements on a partitioned table, check `plan_cache_mode`, the partition count, and whether the plan shows `Subplans Removed`.

## 428: Why might an index-only scan still be slow?

If many pages aren't marked all-visible, it falls back to reading the table for those rows (look at `Heap Fetches` in `EXPLAIN ANALYZE`). That happens on tables with frequent updates or when vacuum hasn't run recently. A bloated index, or an index with many columns being scanned over a large range, can also be slow. Vacuum more often, or narrow the range.

## 429: How can the planner use a CHECK constraint to skip work?

With `constraint_exclusion` (default `partition`), PostgreSQL can skip tables whose `CHECK` constraints prove that no rows can match, which was how old inheritance-based partitioning pruned. Modern declarative partitioning uses its own faster pruning. Constraints also help in other ways: `NOT NULL` lets the planner simplify `NOT IN`, and unique constraints let it remove unneeded left joins.

## 430: What is join removal?

If you `LEFT JOIN` a table on its unique key but don't use any of its columns, the join can't change the result, so PostgreSQL removes it from the plan. This makes wide views cheaper when you only need a few columns from them. It only works when uniqueness is proven by a unique index or primary key, so adding the right constraint can make queries faster.

## 431: How do you speed up a query that uses OFFSET-based pagination in an admin panel you can't fully rewrite?

Limit how deep users can go (for example the first 100 pages), use a deferred join so skipped rows are read only from a covering index, add an index matching the sort, and drop the exact total count or estimate it. If deep pages are truly needed, add keyset pagination as a new API and move clients over.

## 432: When can't keyset pagination be used, and what are the alternatives?

When users need to jump to an arbitrary page number, or when the sort is on a computed value (like a relevance score) that can't be indexed. Alternatives: cap the page depth, take a snapshot of result IDs into a temporary results table or cache and page through that, or let a search engine handle the ranking and paging.

## 433: How does the WAL affect replicas and backups, and how can you reduce its volume?

Every byte of WAL is sent to replicas and archived for backups, so more WAL means more network, storage and lag. Reduce it by: fewer indexes and more HOT updates, fewer checkpoints (fewer full page images), `wal_compression`, avoiding no-op updates, using unlogged tables for throwaway data, and batching changes.

## 434: Why can UPDATE that sets a column to the same value still cost a lot?

In PostgreSQL, an `UPDATE` creates a new row version even if no values change, writes WAL, possibly updates indexes, fires triggers, and leaves a dead row. ORMs that update every column on save make this worse. Add a condition so unchanged rows are skipped, and have the ORM update only changed fields.

```sql
UPDATE users SET name = $1 WHERE id = $2 AND name IS DISTINCT FROM $1;
```

## 435: What are the performance trade-offs of using natural keys versus surrogate keys?

Natural keys (like email or a product code) avoid an extra unique index and can make some joins unnecessary, but they're often long strings, and changing them means updating every reference. Surrogate keys (integer or UUIDv7) are small and never change, keeping foreign keys and indexes compact. Most systems use surrogate primary keys plus unique constraints on natural keys.

## 436: How do you size and tune autovacuum for a large, write-heavy database?

- Raise `autovacuum_max_workers` (needs a restart in older versions) so big tables don't block small ones.
- Raise `autovacuum_vacuum_cost_limit` or lower `autovacuum_vacuum_cost_delay` so each worker does more per second on fast storage.
- Lower scale factors on large tables.
- Give `autovacuum_work_mem` enough memory.
- In PostgreSQL 19, parallel index vacuuming by autovacuum (`autovacuum_max_parallel_workers`) can speed up tables with many indexes.

Watch `n_dead_tup` and the age of the oldest transaction ID to confirm it keeps up.

## 437: What is the difference between logical and physical reads, and why does it matter for tuning?

A logical read is a page request served by the database cache. A physical read goes to the OS or disk. A query with millions of logical reads is doing too much work even if it's fast now, because once the data stops fitting in memory, those become physical reads and the query gets slow. Tune queries to reduce total pages touched, not just to make them fast on a warm cache.

## 438: How do you reason about the cost of an index before creating it?

Estimate its size (key width times rows, plus overhead), how many writes per second will need to update it, and how many queries it will speed up and by how much. Check whether an existing index could be extended instead. For a write-heavy table, one composite index that serves several queries is usually better than several narrow ones. Use `hypopg` to see if the planner would even pick it.

## 439: What is a "loose index scan" and how do you emulate it in PostgreSQL?

It reads just one entry per distinct value of the leading index column, jumping over duplicates, which is fast for `SELECT DISTINCT a` when `a` has few distinct values in a huge table. MySQL does this natively for some `GROUP BY` and `DISTINCT` queries. In PostgreSQL (before skip scan covered more cases) you emulate it with a recursive CTE:

```sql
WITH RECURSIVE t AS (
  (SELECT status FROM orders ORDER BY status LIMIT 1)
  UNION ALL
  SELECT (SELECT status FROM orders WHERE status > t.status ORDER BY status LIMIT 1)
  FROM t WHERE t.status IS NOT NULL
)
SELECT status FROM t WHERE status IS NOT NULL;
```

## 440: How do you handle the "latest value per device" query on a huge table?

`SELECT DISTINCT ON (device_id) ... ORDER BY device_id, ts DESC` must still go through many rows. Faster options: loop over the device list with `LATERAL ... ORDER BY ts DESC LIMIT 1` and an index on `(device_id, ts DESC)`, or keep a separate `device_latest` table updated with an upsert on every new reading, so the query reads one row per device.

## 441: What is the risk of using SELECT FOR UPDATE on rows found through a range scan in InnoDB?

Under `REPEATABLE READ`, InnoDB locks every index record it scans plus the gaps between them, not just the rows that end up matching. Without a good index, `SELECT ... FOR UPDATE WHERE status = 'new'` may lock a big part of the table and block inserts. Use a precise index, `READ COMMITTED`, smaller ranges, or `SKIP LOCKED`.

## 442: Why is it a problem to call external services inside a database transaction?

The transaction stays open while you wait for the HTTP call, holding row locks and a database connection, and (in PostgreSQL) holding back vacuum. A slow payment API then turns into lock waits and connection pool exhaustion for unrelated requests. Do the external call before or after the transaction, and use patterns like the outbox table to tie them together reliably.

## 443: What is the outbox pattern and how does it relate to database load?

Instead of writing to the database and then publishing a message (which can fail halfway), you insert the message into an `outbox` table in the same transaction. A separate process reads the outbox and publishes. The outbox behaves like a queue table, so keep it small, delete processed rows, index unprocessed ones, and vacuum it often.

## 444: How do column stores differ from row stores for analytical queries?

A row store keeps all columns of a row together, which is great for reading or writing whole rows. A column store keeps each column together, so a query that sums one column out of fifty reads only that column, and similar values compress very well. Analytical queries can be 10-100x faster in a column store. Many teams keep OLTP data in PostgreSQL or MySQL and copy it to a column store for analytics.

## 445: How does the choice of isolation level affect replication consistency on replicas?

Replicas apply changes in commit order, so a query on a replica sees a consistent state, but possibly an old one. A transaction that reads from both the primary and a replica can see data from two different moments. For flows that need consistent reads (like checking a balance and then showing history), read everything from one server. Also note that PostgreSQL doesn't support the Serializable level on standbys at all.

## 446: How can you reduce lock waits caused by foreign keys on hot parent rows?

- Avoid updating the parent's key columns (PostgreSQL's `FOR KEY SHARE` doesn't conflict with non-key updates).
- Avoid frequent updates to the hot parent row itself, for example move counters off it.
- In extreme cases, check the reference in the app and drop the foreign key for that table, accepting the risk.
- Batch child inserts so fewer lock acquisitions happen.

## 447: What should a team do to keep database performance good over time?

- Make query metrics visible (dashboards with top queries).
- Review SQL and migrations like code.
- Test with production-sized data.
- Set timeouts and limits.
- Track slow queries as bugs with owners.
- Clean up unused indexes and old data on a schedule.
- Keep the database version reasonably current.

Performance problems are cheaper to prevent than to fix during an incident.

## 448: How do you explain a query plan problem to someone who isn't a database expert?

Show the one number that matters: "the database expected to find 10 rows here and found 2 million, so it chose a method that's good for 10 rows". Then the fix: "we updated its statistics" or "we added an index so it can go straight to the rows it needs". Before and after timings make the case better than plan details.

## 449: What are common myths about SQL performance?

- "More indexes always help." They slow writes and can confuse the planner.
- "`COUNT(1)` is faster than `COUNT(*)`." They're the same.
- "Joins are always slow." Indexed joins are very fast.
- "Stored procedures are always faster." Only when they save round trips.
- "Bigger hardware fixes it." Not if a query reads the whole table.
- "`EXISTS` is always faster than `IN`." Modern planners often treat them the same.

## 450: If you had one week to improve the performance of an unfamiliar database, what would you do?

1. Turn on `pg_stat_statements` or Performance Schema digests and the slow query log.
2. Collect a few days of data, then list the top 10 queries by total time.
3. Run `EXPLAIN ANALYZE` on each and fix the clear wins (missing indexes, N+1, bad rewrites).
4. Check config basics: memory settings, connection count and pooling, autovacuum or purge health.
5. Look for bloat, unused indexes and long transactions.
6. Measure again and write down what changed, so the next person can continue.
