# MongoDB Interview Questions and Answers

_Last updated: October 28, 2026_

This is a list of 450 MongoDB interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers are based on MongoDB 8.x (with notes where a feature appeared in a specific version), `mongosh`, and the current official drivers.

Code examples use `mongosh` syntax unless they say otherwise. Examples for drivers use the Node.js driver v6 and PyMongo.

## Table of Contents

- [Easy Questions](#easy-questions)
- [Moderate Questions](#moderate-questions)
- [Advanced Questions](#advanced-questions)

### Easy Questions (1-150)

- [1: What is MongoDB?](#1-what-is-mongodb)
- [2: What is a document in MongoDB?](#2-what-is-a-document-in-mongodb)
- [3: What is a collection?](#3-what-is-a-collection)
- [4: What is a database in MongoDB?](#4-what-is-a-database-in-mongodb)
- [5: What is BSON?](#5-what-is-bson)
- [6: What is the difference between JSON and BSON?](#6-what-is-the-difference-between-json-and-bson)
- [7: What is the `_id` field?](#7-what-is-the-_id-field)
- [8: What is an ObjectId?](#8-what-is-an-objectid)
- [9: What is mongosh?](#9-what-is-mongosh)
- [10: What is the default port of MongoDB?](#10-what-is-the-default-port-of-mongodb)
- [11: How do you create a database?](#11-how-do-you-create-a-database)
- [12: How do you create a collection?](#12-how-do-you-create-a-collection)
- [13: How do you insert one document?](#13-how-do-you-insert-one-document)
- [14: How do you insert many documents?](#14-how-do-you-insert-many-documents)
- [15: Is `db.collection.insert()` still used?](#15-is-dbcollectioninsert-still-used)
- [16: How do you find all documents in a collection?](#16-how-do-you-find-all-documents-in-a-collection)
- [17: How do you find one document?](#17-how-do-you-find-one-document)
- [18: How do you filter documents by a field value?](#18-how-do-you-filter-documents-by-a-field-value)
- [19: What are comparison operators in MongoDB?](#19-what-are-comparison-operators-in-mongodb)
- [20: What are logical operators in MongoDB?](#20-what-are-logical-operators-in-mongodb)
- [21: How do you update one document?](#21-how-do-you-update-one-document)
- [22: How do you update many documents?](#22-how-do-you-update-many-documents)
- [23: What is the difference between `updateOne()` and `replaceOne()`?](#23-what-is-the-difference-between-updateone-and-replaceone)
- [24: What does `$set` do?](#24-what-does-set-do)
- [25: What does `$unset` do?](#25-what-does-unset-do)
- [26: What does `$inc` do?](#26-what-does-inc-do)
- [27: How do you delete documents?](#27-how-do-you-delete-documents)
- [28: How do you drop a collection?](#28-how-do-you-drop-a-collection)
- [29: How do you drop a database?](#29-how-do-you-drop-a-database)
- [30: How do you list databases and collections?](#30-how-do-you-list-databases-and-collections)
- [31: What is projection?](#31-what-is-projection)
- [32: How do you sort query results?](#32-how-do-you-sort-query-results)
- [33: How do you limit the number of results?](#33-how-do-you-limit-the-number-of-results)
- [34: How do you skip documents?](#34-how-do-you-skip-documents)
- [35: How do you count documents?](#35-how-do-you-count-documents)
- [36: How do you find distinct values of a field?](#36-how-do-you-find-distinct-values-of-a-field)
- [37: What data types does MongoDB support?](#37-what-data-types-does-mongodb-support)
- [38: How do you store a date in MongoDB?](#38-how-do-you-store-a-date-in-mongodb)
- [39: What is an embedded document?](#39-what-is-an-embedded-document)
- [40: What is dot notation?](#40-what-is-dot-notation)
- [41: How do you query an array field?](#41-how-do-you-query-an-array-field)
- [42: What does `$push` do?](#42-what-does-push-do)
- [43: What does `$addToSet` do?](#43-what-does-addtoset-do)
- [44: What does `$pull` do?](#44-what-does-pull-do)
- [45: What does `$pop` do?](#45-what-does-pop-do)
- [46: What is an upsert?](#46-what-is-an-upsert)
- [47: What does `$exists` do?](#47-what-does-exists-do)
- [48: How do you find documents where a field is null?](#48-how-do-you-find-documents-where-a-field-is-null)
- [49: What does `$type` do?](#49-what-does-type-do)
- [50: How do you search with a regular expression?](#50-how-do-you-search-with-a-regular-expression)
- [51: What is an index in MongoDB?](#51-what-is-an-index-in-mongodb)
- [52: How do you create an index?](#52-how-do-you-create-an-index)
- [53: How do you list and drop indexes?](#53-how-do-you-list-and-drop-indexes)
- [54: What is a unique index?](#54-what-is-a-unique-index)
- [55: What is the default index in MongoDB?](#55-what-is-the-default-index-in-mongodb)
- [56: What is a cursor?](#56-what-is-a-cursor)
- [57: What is the difference between `find()` and `findOne()`?](#57-what-is-the-difference-between-find-and-findone)
- [58: What is the `pretty()` method?](#58-what-is-the-pretty-method)
- [59: What is schema-less (flexible schema) design?](#59-what-is-schema-less-flexible-schema-design)
- [60: What are the main advantages of MongoDB?](#60-what-are-the-main-advantages-of-mongodb)
- [61: When is MongoDB not a good choice?](#61-when-is-mongodb-not-a-good-choice)
- [62: What is the difference between SQL and MongoDB terms?](#62-what-is-the-difference-between-sql-and-mongodb-terms)
- [63: What is a replica set?](#63-what-is-a-replica-set)
- [64: What is sharding?](#64-what-is-sharding)
- [65: What is MongoDB Atlas?](#65-what-is-mongodb-atlas)
- [66: What is `mongod`?](#66-what-is-mongod)
- [67: What is `mongos`?](#67-what-is-mongos)
- [68: What is a connection string?](#68-what-is-a-connection-string)
- [69: What is the default storage engine?](#69-what-is-the-default-storage-engine)
- [70: How do you check the MongoDB server version?](#70-how-do-you-check-the-mongodb-server-version)
- [71: What is the maximum size of a document?](#71-what-is-the-maximum-size-of-a-document)
- [72: What is GridFS?](#72-what-is-gridfs)
- [73: What is a capped collection?](#73-what-is-a-capped-collection)
- [74: What is a TTL index?](#74-what-is-a-ttl-index)
- [75: What is the aggregation framework?](#75-what-is-the-aggregation-framework)
- [76: What does `$match` do?](#76-what-does-match-do)
- [77: What does `$group` do?](#77-what-does-group-do)
- [78: What does `$project` do?](#78-what-does-project-do)
- [79: What does `$sort` do in an aggregation?](#79-what-does-sort-do-in-an-aggregation)
- [80: What does `$limit` and `$skip` do in aggregation?](#80-what-does-limit-and-skip-do-in-aggregation)
- [81: What does `$unwind` do?](#81-what-does-unwind-do)
- [82: What does `$lookup` do?](#82-what-does-lookup-do)
- [83: What does `$count` stage do?](#83-what-does-count-stage-do)
- [84: What does `$addFields` (or `$set`) do?](#84-what-does-addfields-or-set-do)
- [85: What is the difference between `$project` and `$addFields`?](#85-what-is-the-difference-between-project-and-addfields)
- [86: What is a write concern?](#86-what-is-a-write-concern)
- [87: What is a read preference?](#87-what-is-a-read-preference)
- [88: What is the `explain()` method?](#88-what-is-the-explain-method)
- [89: What is `COLLSCAN`?](#89-what-is-collscan)
- [90: What is `IXSCAN`?](#90-what-is-ixscan)
- [91: How do you rename a field in all documents?](#91-how-do-you-rename-a-field-in-all-documents)
- [92: How do you rename a collection?](#92-how-do-you-rename-a-collection)
- [93: What does `$min` and `$max` do in an update?](#93-what-does-min-and-max-do-in-an-update)
- [94: What does `$mul` do?](#94-what-does-mul-do)
- [95: What does `$currentDate` do?](#95-what-does-currentdate-do)
- [96: What is `$setOnInsert`?](#96-what-is-setoninsert)
- [97: How do you update a specific element in an array?](#97-how-do-you-update-a-specific-element-in-an-array)
- [98: What does `$elemMatch` do?](#98-what-does-elemmatch-do)
- [99: What does `$size` do?](#99-what-does-size-do)
- [100: What is `$expr`?](#100-what-is-expr)
- [101: What is a compound index?](#101-what-is-a-compound-index)
- [102: What is a multikey index?](#102-what-is-a-multikey-index)
- [103: What is a text index?](#103-what-is-a-text-index)
- [104: What is a geospatial index?](#104-what-is-a-geospatial-index)
- [105: What is a sparse index?](#105-what-is-a-sparse-index)
- [106: What is a partial index?](#106-what-is-a-partial-index)
- [107: What is a hashed index?](#107-what-is-a-hashed-index)
- [108: What is the `admin` database?](#108-what-is-the-admin-database)
- [109: What is the `local` database?](#109-what-is-the-local-database)
- [110: What is the `config` database?](#110-what-is-the-config-database)
- [111: How do you enable authentication?](#111-how-do-you-enable-authentication)
- [112: How do you create a user?](#112-how-do-you-create-a-user)
- [113: What are built-in roles in MongoDB?](#113-what-are-built-in-roles-in-mongodb)
- [114: What is `mongodump`?](#114-what-is-mongodump)
- [115: What is `mongorestore`?](#115-what-is-mongorestore)
- [116: What is `mongoexport` and `mongoimport`?](#116-what-is-mongoexport-and-mongoimport)
- [117: What is MongoDB Compass?](#117-what-is-mongodb-compass)
- [118: What is the oplog?](#118-what-is-the-oplog)
- [119: Does MongoDB support transactions?](#119-does-mongodb-support-transactions)
- [120: Is a single document update atomic?](#120-is-a-single-document-update-atomic)
- [121: What is `bulkWrite()`?](#121-what-is-bulkwrite)
- [122: What is the difference between ordered and unordered bulk writes?](#122-what-is-the-difference-between-ordered-and-unordered-bulk-writes)
- [123: How do you check the stats of a collection?](#123-how-do-you-check-the-stats-of-a-collection)
- [124: How do you check the stats of a database?](#124-how-do-you-check-the-stats-of-a-database)
- [125: What does `db.serverStatus()` show?](#125-what-does-dbserverstatus-show)
- [126: How do you see currently running operations?](#126-how-do-you-see-currently-running-operations)
- [127: How do you kill a running operation?](#127-how-do-you-kill-a-running-operation)
- [128: What is a namespace in MongoDB?](#128-what-is-a-namespace-in-mongodb)
- [129: Are field names case sensitive?](#129-are-field-names-case-sensitive)
- [130: Can a field name start with `$` or contain a dot?](#130-can-a-field-name-start-with--or-contain-a-dot)
- [131: What is `$in` used for?](#131-what-is-in-used-for)
- [132: What is the difference between `$in` and `$all`?](#132-what-is-the-difference-between-in-and-all)
- [133: How do you return only some elements of an array?](#133-how-do-you-return-only-some-elements-of-an-array)
- [134: How do you check if a document was updated?](#134-how-do-you-check-if-a-document-was-updated)
- [135: What is `findOneAndUpdate()`?](#135-what-is-findoneandupdate)
- [136: What is `findOneAndDelete()`?](#136-what-is-findoneanddelete)
- [137: What is `findOneAndReplace()`?](#137-what-is-findoneandreplace)
- [138: How do you see indexes used in a query plan?](#138-how-do-you-see-indexes-used-in-a-query-plan)
- [139: How do you hide an index?](#139-how-do-you-hide-an-index)
- [140: What is a covered query?](#140-what-is-a-covered-query)
- [141: What is `$nin`?](#141-what-is-nin)
- [142: What is the difference between `$ne` and `$not`?](#142-what-is-the-difference-between-ne-and-not)
- [143: How do you use `$or` with an index?](#143-how-do-you-use-or-with-an-index)
- [144: How do you check if MongoDB is running?](#144-how-do-you-check-if-mongodb-is-running)
- [145: Where is MongoDB configuration stored?](#145-where-is-mongodb-configuration-stored)
- [146: What is `bindIp`?](#146-what-is-bindip)
- [147: What format are MongoDB logs in?](#147-what-format-are-mongodb-logs-in)
- [148: What is the MongoDB Node.js driver?](#148-what-is-the-mongodb-nodejs-driver)
- [149: What is Mongoose?](#149-what-is-mongoose)
- [150: What is the Stable API?](#150-what-is-the-stable-api)

### Moderate Questions (151-300)

- [151: How do you decide between embedding and referencing?](#151-how-do-you-decide-between-embedding-and-referencing)
- [152: How do you model a one-to-many relationship?](#152-how-do-you-model-a-one-to-many-relationship)
- [153: How do you model a many-to-many relationship?](#153-how-do-you-model-a-many-to-many-relationship)
- [154: What is the extended reference pattern?](#154-what-is-the-extended-reference-pattern)
- [155: What is the subset pattern?](#155-what-is-the-subset-pattern)
- [156: What is the bucket pattern?](#156-what-is-the-bucket-pattern)
- [157: What is the computed pattern?](#157-what-is-the-computed-pattern)
- [158: What is the outlier pattern?](#158-what-is-the-outlier-pattern)
- [159: What is the schema versioning pattern?](#159-what-is-the-schema-versioning-pattern)
- [160: What is the polymorphic pattern?](#160-what-is-the-polymorphic-pattern)
- [161: What is the attribute pattern?](#161-what-is-the-attribute-pattern)
- [162: How do you add schema validation to a collection?](#162-how-do-you-add-schema-validation-to-a-collection)
- [163: How do you add validation to an existing collection?](#163-how-do-you-add-validation-to-an-existing-collection)
- [164: What is the difference between `validationLevel` strict and moderate?](#164-what-is-the-difference-between-validationlevel-strict-and-moderate)
- [165: What is the difference between `validationAction` error and warn?](#165-what-is-the-difference-between-validationaction-error-and-warn)
- [166: How do you find documents that do not match the current validator?](#166-how-do-you-find-documents-that-do-not-match-the-current-validator)
- [167: What is the ESR rule for compound indexes?](#167-what-is-the-esr-rule-for-compound-indexes)
- [168: What is an index prefix?](#168-what-is-an-index-prefix)
- [169: Does the sort direction in a compound index matter?](#169-does-the-sort-direction-in-a-compound-index-matter)
- [170: What is a blocking sort?](#170-what-is-a-blocking-sort)
- [171: How do you read the `executionStats` in explain output?](#171-how-do-you-read-the-executionstats-in-explain-output)
- [172: What are the three explain verbosity modes?](#172-what-are-the-three-explain-verbosity-modes)
- [173: What is the query plan cache?](#173-what-is-the-query-plan-cache)
- [174: What is `hint()`?](#174-what-is-hint)
- [175: How do you create an index without blocking the collection?](#175-how-do-you-create-an-index-without-blocking-the-collection)
- [176: What is a wildcard index?](#176-what-is-a-wildcard-index)
- [177: What are collation settings?](#177-what-are-collation-settings)
- [178: How do you do case-insensitive search efficiently?](#178-how-do-you-do-case-insensitive-search-efficiently)
- [179: How does `$lookup` with a pipeline work?](#179-how-does-lookup-with-a-pipeline-work)
- [180: How do you flatten the `$lookup` result into the main document?](#180-how-do-you-flatten-the-lookup-result-into-the-main-document)
- [181: What is `$facet`?](#181-what-is-facet)
- [182: What is `$bucket` and `$bucketAuto`?](#182-what-is-bucket-and-bucketauto)
- [183: What is `$replaceRoot` / `$replaceWith`?](#183-what-is-replaceroot--replacewith)
- [184: What is `$out`?](#184-what-is-out)
- [185: What is `$merge`?](#185-what-is-merge)
- [186: What is the difference between `$out` and `$merge`?](#186-what-is-the-difference-between-out-and-merge)
- [187: What is a view?](#187-what-is-a-view)
- [188: What is an on-demand materialized view?](#188-what-is-an-on-demand-materialized-view)
- [189: What does `$sortByCount` do?](#189-what-does-sortbycount-do)
- [190: What does `$sample` do?](#190-what-does-sample-do)
- [191: What does `$unionWith` do?](#191-what-does-unionwith-do)
- [192: What does `$graphLookup` do?](#192-what-does-graphlookup-do)
- [193: What are window functions in MongoDB?](#193-what-are-window-functions-in-mongodb)
- [194: What do `$first`, `$last`, `$top`, `$bottom`, `$firstN` and `$topN` do?](#194-what-do-first-last-top-bottom-firstn-and-topn-do)
- [195: How do you get the median or a percentile?](#195-how-do-you-get-the-median-or-a-percentile)
- [196: How do you work with dates in aggregation?](#196-how-do-you-work-with-dates-in-aggregation)
- [197: How do you use conditional logic in aggregation?](#197-how-do-you-use-conditional-logic-in-aggregation)
- [198: How do you work with arrays in aggregation without `$unwind`?](#198-how-do-you-work-with-arrays-in-aggregation-without-unwind)
- [199: What is the aggregation pipeline memory limit?](#199-what-is-the-aggregation-pipeline-memory-limit)
- [200: Can an aggregation pipeline be used in an update?](#200-can-an-aggregation-pipeline-be-used-in-an-update)
- [201: How does the positional operator `$[]` work?](#201-how-does-the-positional-operator--work)
- [202: How does the filtered positional operator `$[<identifier>]` work?](#202-how-does-the-filtered-positional-operator-identifier-work)
- [203: How do you keep an array sorted and limited in size?](#203-how-do-you-keep-an-array-sorted-and-limited-in-size)
- [204: How do you insert at a specific position in an array?](#204-how-do-you-insert-at-a-specific-position-in-an-array)
- [205: Can `updateOne()` choose which document to update when many match?](#205-can-updateone-choose-which-document-to-update-when-many-match)
- [206: What is the new `bulkWrite` command in MongoDB 8.0?](#206-what-is-the-new-bulkwrite-command-in-mongodb-80)
- [207: How do you use a multi-document transaction?](#207-how-do-you-use-a-multi-document-transaction)
- [208: What are the limits of transactions?](#208-what-are-the-limits-of-transactions)
- [209: What are `TransientTransactionError` and `UnknownTransactionCommitResult`?](#209-what-are-transienttransactionerror-and-unknowntransactioncommitresult)
- [210: What are read concern levels?](#210-what-are-read-concern-levels)
- [211: What is causal consistency?](#211-what-is-causal-consistency)
- [212: What are retryable writes?](#212-what-are-retryable-writes)
- [213: What are retryable reads?](#213-what-are-retryable-reads)
- [214: How does replica set election work?](#214-how-does-replica-set-election-work)
- [215: What is an arbiter?](#215-what-is-an-arbiter)
- [216: What is a hidden member?](#216-what-is-a-hidden-member)
- [217: What is a delayed member?](#217-what-is-a-delayed-member)
- [218: Why should a replica set have an odd number of voting members?](#218-why-should-a-replica-set-have-an-odd-number-of-voting-members)
- [219: How do you set up a replica set?](#219-how-do-you-set-up-a-replica-set)
- [220: How do you check replication lag?](#220-how-do-you-check-replication-lag)
- [221: What is a rollback in a replica set?](#221-what-is-a-rollback-in-a-replica-set)
- [222: What is `rs.stepDown()`?](#222-what-is-rsstepdown)
- [223: What is the oplog window?](#223-what-is-the-oplog-window)
- [224: What is initial sync?](#224-what-is-initial-sync)
- [225: What is a change stream?](#225-what-is-a-change-stream)
- [226: How do you resume a change stream after a failure?](#226-how-do-you-resume-a-change-stream-after-a-failure)
- [227: How do you get the full document in an update change event?](#227-how-do-you-get-the-full-document-in-an-update-change-event)
- [228: What levels can you open a change stream on?](#228-what-levels-can-you-open-a-change-stream-on)
- [229: What is a time series collection?](#229-what-is-a-time-series-collection)
- [230: What are the limits of time series collections?](#230-what-are-the-limits-of-time-series-collections)
- [231: What is a clustered collection?](#231-what-is-a-clustered-collection)
- [232: How do you paginate efficiently in MongoDB?](#232-how-do-you-paginate-efficiently-in-mongodb)
- [233: How do you implement an auto-increment field?](#233-how-do-you-implement-an-auto-increment-field)
- [234: How do you store a UUID?](#234-how-do-you-store-a-uuid)
- [235: Why use `Decimal128` for money?](#235-why-use-decimal128-for-money)
- [236: What is the difference between `Int32`, `Int64` and `Double` in mongosh?](#236-what-is-the-difference-between-int32-int64-and-double-in-mongosh)
- [237: What is a sharded cluster made of?](#237-what-is-a-sharded-cluster-made-of)
- [238: What is a shard key?](#238-what-is-a-shard-key)
- [239: What makes a good shard key?](#239-what-makes-a-good-shard-key)
- [240: What is the difference between ranged and hashed sharding?](#240-what-is-the-difference-between-ranged-and-hashed-sharding)
- [241: What is a chunk?](#241-what-is-a-chunk)
- [242: What is the balancer?](#242-what-is-the-balancer)
- [243: What is a targeted query vs a scatter-gather (broadcast) query?](#243-what-is-a-targeted-query-vs-a-scatter-gather-broadcast-query)
- [244: How do you shard a collection?](#244-how-do-you-shard-a-collection)
- [245: What are jumbo chunks?](#245-what-are-jumbo-chunks)
- [246: What are zones in sharding?](#246-what-are-zones-in-sharding)
- [247: What is WiredTiger cache?](#247-what-is-wiredtiger-cache)
- [248: What compression does WiredTiger use?](#248-what-compression-does-wiredtiger-use)
- [249: What is the journal?](#249-what-is-the-journal)
- [250: What does `j: true` mean in a write concern?](#250-what-does-j-true-mean-in-a-write-concern)
- [251: What is the working set?](#251-what-is-the-working-set)
- [252: How do you find slow queries?](#252-how-do-you-find-slow-queries)
- [253: What does `$indexStats` show?](#253-what-does-indexstats-show)
- [254: Why should you avoid too many indexes?](#254-why-should-you-avoid-too-many-indexes)
- [255: Can MongoDB use more than one index for a query?](#255-can-mongodb-use-more-than-one-index-for-a-query)
- [256: What is index selectivity?](#256-what-is-index-selectivity)
- [257: How do you use `$text` search scores?](#257-how-do-you-use-text-search-scores)
- [258: What is Atlas Search?](#258-what-is-atlas-search)
- [259: What is the difference between `$text` and `$search`?](#259-what-is-the-difference-between-text-and-search)
- [260: What is Atlas Vector Search?](#260-what-is-atlas-vector-search)
- [261: How do you define a vector search index?](#261-how-do-you-define-a-vector-search-index)
- [262: How do you connect to MongoDB from Python?](#262-how-do-you-connect-to-mongodb-from-python)
- [263: How do you connect to MongoDB from Java?](#263-how-do-you-connect-to-mongodb-from-java)
- [264: Why should you reuse a `MongoClient` instance?](#264-why-should-you-reuse-a-mongoclient-instance)
- [265: What is the connection pool and how do you tune it?](#265-what-is-the-connection-pool-and-how-do-you-tune-it)
- [266: What timeouts should you set in a driver?](#266-what-timeouts-should-you-set-in-a-driver)
- [267: What is `maxTimeMS`?](#267-what-is-maxtimems)
- [268: How do you handle duplicate key errors in code?](#268-how-do-you-handle-duplicate-key-errors-in-code)
- [269: What is the difference between `deleteMany({})` and `drop()`?](#269-what-is-the-difference-between-deletemany-and-drop)
- [270: How do you copy a collection?](#270-how-do-you-copy-a-collection)
- [271: How do you convert a field type for all documents?](#271-how-do-you-convert-a-field-type-for-all-documents)
- [272: What is `$getField` and `$setField`?](#272-what-is-getfield-and-setfield)
- [273: How do you turn an object into an array and back?](#273-how-do-you-turn-an-object-into-an-array-and-back)
- [274: How do you join on more than one field with `$lookup`?](#274-how-do-you-join-on-more-than-one-field-with-lookup)
- [275: Does `$lookup` use indexes?](#275-does-lookup-use-indexes)
- [276: Can you `$lookup` into a sharded collection?](#276-can-you-lookup-into-a-sharded-collection)
- [277: How do you see why an aggregation is slow?](#277-how-do-you-see-why-an-aggregation-is-slow)
- [278: What pipeline optimizations does MongoDB do automatically?](#278-what-pipeline-optimizations-does-mongodb-do-automatically)
- [279: How do you get the last N records per group?](#279-how-do-you-get-the-last-n-records-per-group)
- [280: How do you deduplicate documents?](#280-how-do-you-deduplicate-documents)
- [281: What are the default users and roles after installing MongoDB?](#281-what-are-the-default-users-and-roles-after-installing-mongodb)
- [282: How do you create a custom role?](#282-how-do-you-create-a-custom-role)
- [283: What authentication mechanisms does MongoDB support?](#283-what-authentication-mechanisms-does-mongodb-support)
- [284: How do you enable TLS?](#284-how-do-you-enable-tls)
- [285: What is encryption at rest?](#285-what-is-encryption-at-rest)
- [286: What is Client-Side Field Level Encryption (CSFLE)?](#286-what-is-client-side-field-level-encryption-csfle)
- [287: What is Queryable Encryption?](#287-what-is-queryable-encryption)
- [288: What is auditing in MongoDB?](#288-what-is-auditing-in-mongodb)
- [289: How do you protect MongoDB from NoSQL injection?](#289-how-do-you-protect-mongodb-from-nosql-injection)
- [290: Is server-side JavaScript still recommended?](#290-is-server-side-javascript-still-recommended)
- [291: Why was map-reduce deprecated?](#291-why-was-map-reduce-deprecated)
- [292: How do you take a consistent backup of a replica set?](#292-how-do-you-take-a-consistent-backup-of-a-replica-set)
- [293: How do you upgrade a replica set?](#293-how-do-you-upgrade-a-replica-set)
- [294: What is the feature compatibility version (FCV)?](#294-what-is-the-feature-compatibility-version-fcv)
- [295: What is the MongoDB release schedule?](#295-what-is-the-mongodb-release-schedule)
- [296: How do you limit the size of a result in a driver?](#296-how-do-you-limit-the-size-of-a-result-in-a-driver)
- [297: What is `allowDiskUse`?](#297-what-is-allowdiskuse)
- [298: What are `$sum`, `$avg` and `$count` as accumulators?](#298-what-are-sum-avg-and-count-as-accumulators)
- [299: How do you group by multiple fields?](#299-how-do-you-group-by-multiple-fields)
- [300: How do you get the size of an array in a query or aggregation?](#300-how-do-you-get-the-size-of-an-array-in-a-query-or-aggregation)

### Advanced Questions (301-450)

- [301: How does WiredTiger handle concurrency?](#301-how-does-wiredtiger-handle-concurrency)
- [302: What locks does MongoDB still use?](#302-what-locks-does-mongodb-still-use)
- [303: What are concurrent transaction tickets (read/write tickets)?](#303-what-are-concurrent-transaction-tickets-readwrite-tickets)
- [304: What is the slot-based query execution engine (SBE)?](#304-what-is-the-slot-based-query-execution-engine-sbe)
- [305: What are query settings in MongoDB 8.0?](#305-what-are-query-settings-in-mongodb-80)
- [306: What is a query shape?](#306-what-is-a-query-shape)
- [307: What are express query stages in MongoDB 8.0?](#307-what-are-express-query-stages-in-mongodb-80)
- [308: How does the query planner choose a plan?](#308-how-does-the-query-planner-choose-a-plan)
- [309: What is the cost-based ranker in newer MongoDB versions?](#309-what-is-the-cost-based-ranker-in-newer-mongodb-versions)
- [310: What does `totalKeysExamined` higher than `nReturned` tell you?](#310-what-does-totalkeysexamined-higher-than-nreturned-tell-you)
- [311: What does a `FETCH` stage with a `filter` after `IXSCAN` mean?](#311-what-does-a-fetch-stage-with-a-filter-after-ixscan-mean)
- [312: Why is a multikey index sometimes slow with range queries?](#312-why-is-a-multikey-index-sometimes-slow-with-range-queries)
- [313: What are the rules for compound multikey indexes?](#313-what-are-the-rules-for-compound-multikey-indexes)
- [314: How does sorting on a multikey field work?](#314-how-does-sorting-on-a-multikey-field-work)
- [315: How do partial indexes and unique constraints work together?](#315-how-do-partial-indexes-and-unique-constraints-work-together)
- [316: Why does a unique index fail when many documents lack the field?](#316-why-does-a-unique-index-fail-when-many-documents-lack-the-field)
- [317: How do you build an index on a large production replica set with minimum impact?](#317-how-do-you-build-an-index-on-a-large-production-replica-set-with-minimum-impact)
- [318: What is `commitQuorum` for index builds?](#318-what-is-commitquorum-for-index-builds)
- [319: How do you find and resume interrupted index builds?](#319-how-do-you-find-and-resume-interrupted-index-builds)
- [320: Why can a large `$in` list be slow?](#320-why-can-a-large-in-list-be-slow)
- [321: What is the "explode for sort" optimization?](#321-what-is-the-explode-for-sort-optimization)
- [322: What causes a write conflict, and how do you reduce it?](#322-what-causes-a-write-conflict-and-how-do-you-reduce-it)
- [323: How do transactions work in a sharded cluster?](#323-how-do-transactions-work-in-a-sharded-cluster)
- [324: What is snapshot isolation in transactions?](#324-what-is-snapshot-isolation-in-transactions)
- [325: How long can a transaction hold its snapshot, and why does it matter?](#325-how-long-can-a-transaction-hold-its-snapshot-and-why-does-it-matter)
- [326: What is `atClusterTime` and when would you use it?](#326-what-is-atclustertime-and-when-would-you-use-it)
- [327: What are the trade-offs of `w: "majority"`?](#327-what-are-the-trade-offs-of-w-majority)
- [328: What happens to majority writes when a secondary goes down in a PSA set?](#328-what-happens-to-majority-writes-when-a-secondary-goes-down-in-a-psa-set)
- [329: What is `writeConcernMajorityJournalDefault`?](#329-what-is-writeconcernmajorityjournaldefault)
- [330: How does Raft relate to MongoDB elections?](#330-how-does-raft-relate-to-mongodb-elections)
- [331: Can there be two primaries at the same time?](#331-can-there-be-two-primaries-at-the-same-time)
- [332: What are `priority` and `votes` in a replica set config?](#332-what-are-priority-and-votes-in-a-replica-set-config)
- [333: What is chained replication?](#333-what-is-chained-replication)
- [334: How do you design a replica set across data centers?](#334-how-do-you-design-a-replica-set-across-data-centers)
- [335: What are read preference tags and `maxStalenessSeconds`?](#335-what-are-read-preference-tags-and-maxstalenessseconds)
- [336: What is hedged reads?](#336-what-is-hedged-reads)
- [337: What is mirrored reads?](#337-what-is-mirrored-reads)
- [338: How does resharding work?](#338-how-does-resharding-work)
- [339: What is refining a shard key?](#339-what-is-refining-a-shard-key)
- [340: How do you analyze a candidate shard key?](#340-how-do-you-analyze-a-candidate-shard-key)
- [341: What are `moveCollection` and `unshardCollection` in 8.0?](#341-what-are-movecollection-and-unshardcollection-in-80)
- [342: What is the primary shard of a database?](#342-what-is-the-primary-shard-of-a-database)
- [343: What are orphaned documents?](#343-what-are-orphaned-documents)
- [344: How does a chunk migration work?](#344-how-does-a-chunk-migration-work)
- [345: How does `mongos` know where data lives?](#345-how-does-mongos-know-where-data-lives)
- [346: How do you handle a monotonically increasing shard key like a timestamp?](#346-how-do-you-handle-a-monotonically-increasing-shard-key-like-a-timestamp)
- [347: What are the downsides of a hashed shard key?](#347-what-are-the-downsides-of-a-hashed-shard-key)
- [348: What is a sharded time series collection?](#348-what-is-a-sharded-time-series-collection)
- [349: What is the `$shardedDataDistribution` stage?](#349-what-is-the-shardeddatadistribution-stage)
- [350: What is a config shard?](#350-what-is-a-config-shard)
- [351: How do you design a multi-tenant application in MongoDB?](#351-how-do-you-design-a-multi-tenant-application-in-mongodb)
- [352: How many collections and indexes can MongoDB handle?](#352-how-many-collections-and-indexes-can-mongodb-handle)
- [353: How do you handle a document that keeps growing?](#353-how-do-you-handle-a-document-that-keeps-growing)
- [354: What happens internally when you update a document in WiredTiger?](#354-what-happens-internally-when-you-update-a-document-in-wiredtiger)
- [355: What is WiredTiger cache eviction, and what are signs of trouble?](#355-what-is-wiredtiger-cache-eviction-and-what-are-signs-of-trouble)
- [356: What is a checkpoint in WiredTiger?](#356-what-is-a-checkpoint-in-wiredtiger)
- [357: What is the `storageEngine` `directoryPerDB` and `directoryForIndexes`?](#357-what-is-the-storageengine-directoryperdb-and-directoryforindexes)
- [358: How do you size the oplog?](#358-how-do-you-size-the-oplog)
- [359: Which operations produce many oplog entries?](#359-which-operations-produce-many-oplog-entries)
- [360: How do you safely run a large data migration on a live cluster?](#360-how-do-you-safely-run-a-large-data-migration-on-a-live-cluster)
- [361: What does `$changeStreamSplitLargeEvent` do?](#361-what-does-changestreamsplitlargeevent-do)
- [362: How do you scale change stream consumers?](#362-how-do-you-scale-change-stream-consumers)
- [363: What are the guarantees of change streams?](#363-what-are-the-guarantees-of-change-streams)
- [364: What is Atlas Stream Processing?](#364-what-is-atlas-stream-processing)
- [365: How do you implement an outbox pattern in MongoDB?](#365-how-do-you-implement-an-outbox-pattern-in-mongodb)
- [366: How do you implement optimistic concurrency control?](#366-how-do-you-implement-optimistic-concurrency-control)
- [367: How do you implement a reliable job queue in MongoDB?](#367-how-do-you-implement-a-reliable-job-queue-in-mongodb)
- [368: How do you make an idempotent upsert under concurrency?](#368-how-do-you-make-an-idempotent-upsert-under-concurrency)
- [369: How do you implement soft deletes properly?](#369-how-do-you-implement-soft-deletes-properly)
- [370: How do you model hierarchical data (trees)?](#370-how-do-you-model-hierarchical-data-trees)
- [371: How do you store and query versioned documents (history)?](#371-how-do-you-store-and-query-versioned-documents-history)
- [372: How do you handle large arrays and index size?](#372-how-do-you-handle-large-arrays-and-index-size)
- [373: What is the difference between `$lookup` and application-side joins in terms of performance?](#373-what-is-the-difference-between-lookup-and-application-side-joins-in-terms-of-performance)
- [374: How do you query documents by a field inside an array of objects and return only matching elements?](#374-how-do-you-query-documents-by-a-field-inside-an-array-of-objects-and-return-only-matching-elements)
- [375: How do you write a recursive aggregation with limited depth and filters?](#375-how-do-you-write-a-recursive-aggregation-with-limited-depth-and-filters)
- [376: How do you fill gaps in time series data?](#376-how-do-you-fill-gaps-in-time-series-data)
- [377: How do you compute a moving average?](#377-how-do-you-compute-a-moving-average)
- [378: How do you compute differences between consecutive documents?](#378-how-do-you-compute-differences-between-consecutive-documents)
- [379: How do aggregation pipelines run in a sharded cluster?](#379-how-do-aggregation-pipelines-run-in-a-sharded-cluster)
- [380: What is `$documents`?](#380-what-is-documents)
- [381: How do you use `$$NOW`, `$$ROOT`, `$$CURRENT` and `$$REMOVE`?](#381-how-do-you-use-now-root-current-and-remove)
- [382: How do you pass variables to an aggregation without building strings?](#382-how-do-you-pass-variables-to-an-aggregation-without-building-strings)
- [383: What is `$setUnion`, `$setIntersection` and `$setDifference`?](#383-what-is-setunion-setintersection-and-setdifference)
- [384: How do you sort an array inside a document?](#384-how-do-you-sort-an-array-inside-a-document)
- [385: How do you do a full outer join in MongoDB?](#385-how-do-you-do-a-full-outer-join-in-mongodb)
- [386: What is the difference between `$group` + `$push: "$$ROOT"` and `$topN`?](#386-what-is-the-difference-between-group--push-root-and-topn)
- [387: How do you handle the 16 MB limit in aggregation results?](#387-how-do-you-handle-the-16-mb-limit-in-aggregation-results)
- [388: What is `$expr` performance like with indexes?](#388-what-is-expr-performance-like-with-indexes)
- [389: What does `$regex` do with an index?](#389-what-does-regex-do-with-an-index)
- [390: How does the `$or` query get optimized?](#390-how-does-the-or-query-get-optimized)
- [391: What is the `$jsonSchema` `additionalProperties: false` gotcha?](#391-what-is-the-jsonschema-additionalproperties-false-gotcha)
- [392: How do you get details of why a document failed validation?](#392-how-do-you-get-details-of-why-a-document-failed-validation)
- [393: How do you enforce relationships (like foreign keys)?](#393-how-do-you-enforce-relationships-like-foreign-keys)
- [394: How do you encrypt a field with CSFLE in Node.js?](#394-how-do-you-encrypt-a-field-with-csfle-in-nodejs)
- [395: How is Queryable Encryption different from CSFLE?](#395-how-is-queryable-encryption-different-from-csfle)
- [396: What is the principle of least privilege in MongoDB, with an example?](#396-what-is-the-principle-of-least-privilege-in-mongodb-with-an-example)
- [397: How do you rotate keys and passwords without downtime?](#397-how-do-you-rotate-keys-and-passwords-without-downtime)
- [398: What security checklist would you follow for a self-managed deployment?](#398-what-security-checklist-would-you-follow-for-a-self-managed-deployment)
- [399: What is `setParameter` and `setClusterParameter`?](#399-what-is-setparameter-and-setclusterparameter)
- [400: How do you control log verbosity per component?](#400-how-do-you-control-log-verbosity-per-component)
- [401: What metrics would you monitor in production?](#401-what-metrics-would-you-monitor-in-production)
- [402: What are `mongostat` and `mongotop`?](#402-what-are-mongostat-and-mongotop)
- [403: What causes a sudden spike in connections, and how do you fix it?](#403-what-causes-a-sudden-spike-in-connections-and-how-do-you-fix-it)
- [404: How do you troubleshoot high CPU on a MongoDB server?](#404-how-do-you-troubleshoot-high-cpu-on-a-mongodb-server)
- [405: How do you troubleshoot replication lag?](#405-how-do-you-troubleshoot-replication-lag)
- [406: What is flow control?](#406-what-is-flow-control)
- [407: What is the effect of a long-running query on a secondary?](#407-what-is-the-effect-of-a-long-running-query-on-a-secondary)
- [408: What happens during a failover from the application's point of view?](#408-what-happens-during-a-failover-from-the-applications-point-of-view)
- [409: Why are `updateMany` and `deleteMany` not retryable?](#409-why-are-updatemany-and-deletemany-not-retryable)
- [410: How do you design for zero-downtime schema changes?](#410-how-do-you-design-for-zero-downtime-schema-changes)
- [411: How do you test a MongoDB-based application?](#411-how-do-you-test-a-mongodb-based-application)
- [412: What is the Atlas Local deployment?](#412-what-is-the-atlas-local-deployment)
- [413: How does `$out` behave with indexes and concurrent readers?](#413-how-does-out-behave-with-indexes-and-concurrent-readers)
- [414: How does `$merge` behave on failure?](#414-how-does-merge-behave-on-failure)
- [415: How do you build a near real-time materialized view?](#415-how-do-you-build-a-near-real-time-materialized-view)
- [416: How do you calculate distinct counts at scale?](#416-how-do-you-calculate-distinct-counts-at-scale)
- [417: What is the `$queryStats` stage?](#417-what-is-the-querystats-stage)
- [418: What is Performance Advisor in Atlas?](#418-what-is-performance-advisor-in-atlas)
- [419: What are Atlas cluster tiers and auto-scaling?](#419-what-are-atlas-cluster-tiers-and-auto-scaling)
- [420: What is Online Archive and Atlas Data Federation?](#420-what-is-online-archive-and-atlas-data-federation)
- [421: What is the oplog entry for a multi-document transaction?](#421-what-is-the-oplog-entry-for-a-multi-document-transaction)
- [422: How does MongoDB guarantee durability with `w: "majority"` and `j: true`?](#422-how-does-mongodb-guarantee-durability-with-w-majority-and-j-true)
- [423: What is the majority commit point?](#423-what-is-the-majority-commit-point)
- [424: What happens if you read from a secondary without majority read concern?](#424-what-happens-if-you-read-from-a-secondary-without-majority-read-concern)
- [425: What is `linearizable` read concern, and when do you use it?](#425-what-is-linearizable-read-concern-and-when-do-you-use-it)
- [426: How do sessions work, and what is `lsid`?](#426-how-do-sessions-work-and-what-is-lsid)
- [427: How can you trace a request from the app to the database log?](#427-how-can-you-trace-a-request-from-the-app-to-the-database-log)
- [428: How does the driver discover and monitor servers (SDAM)?](#428-how-does-the-driver-discover-and-monitor-servers-sdam)
- [429: What is load balancer mode in drivers?](#429-what-is-load-balancer-mode-in-drivers)
- [430: What happens if a cursor times out in the middle of iteration?](#430-what-happens-if-a-cursor-times-out-in-the-middle-of-iteration)
- [431: How does `estimatedDocumentCount()` differ from `countDocuments({})` internally?](#431-how-does-estimateddocumentcount-differ-from-countdocuments-internally)
- [432: How do you implement full text search with relevance and autocomplete in MongoDB?](#432-how-do-you-implement-full-text-search-with-relevance-and-autocomplete-in-mongodb)
- [433: How do you combine vector search and keyword search (hybrid search)?](#433-how-do-you-combine-vector-search-and-keyword-search-hybrid-search)
- [434: What is vector quantization in vector search?](#434-what-is-vector-quantization-in-vector-search)
- [435: What are `numCandidates` and `limit` in `$vectorSearch`?](#435-what-are-numcandidates-and-limit-in-vectorsearch)
- [436: What is the difference between `mongodump` and file system snapshots for large datasets?](#436-what-is-the-difference-between-mongodump-and-file-system-snapshots-for-large-datasets)
- [437: How do you restore to a point in time?](#437-how-do-you-restore-to-a-point-in-time)
- [438: How do you move data between clusters with minimum downtime?](#438-how-do-you-move-data-between-clusters-with-minimum-downtime)
- [439: What is the Relational Migrator?](#439-what-is-the-relational-migrator)
- [440: What is the difference between data modeling for reads vs writes?](#440-what-is-the-difference-between-data-modeling-for-reads-vs-writes)
- [441: How do you keep duplicated (denormalized) data in sync?](#441-how-do-you-keep-duplicated-denormalized-data-in-sync)
- [442: Why is `_id` choice important for performance?](#442-why-is-_id-choice-important-for-performance)
- [443: What is the impact of very large documents on performance?](#443-what-is-the-impact-of-very-large-documents-on-performance)
- [444: What are the main improvements in MongoDB 8.0?](#444-what-are-the-main-improvements-in-mongodb-80)
- [445: What are some notable features from 8.1 and 8.2?](#445-what-are-some-notable-features-from-81-and-82)
- [446: What changed in the Node.js driver in recent major versions?](#446-what-changed-in-the-nodejs-driver-in-recent-major-versions)
- [447: How would you debug "Sort exceeded memory limit" or `usedDisk` problems?](#447-how-would-you-debug-sort-exceeded-memory-limit-or-useddisk-problems)
- [448: Explain a real case where an index made a query slower.](#448-explain-a-real-case-where-an-index-made-a-query-slower)
- [449: How would you design an order system that handles inventory correctly under concurrency?](#449-how-would-you-design-an-order-system-that-handles-inventory-correctly-under-concurrency)
- [450: How would you approach a MongoDB performance review for an existing application?](#450-how-would-you-approach-a-mongodb-performance-review-for-an-existing-application)

---

## Easy Questions

### 1: What is MongoDB?

MongoDB is a document database. Instead of storing data in rows and tables like a relational database, it stores data as documents inside collections. Documents look like JSON objects and are stored on disk in a binary format called BSON.

It is open source (Community Edition, under the SSPL license), and there is also a paid Enterprise Edition and a managed cloud service called MongoDB Atlas.

### 2: What is a document in MongoDB?

A document is a single record. It is a set of field and value pairs, similar to a JSON object.

```javascript
{
  _id: ObjectId("66f1c2a8e4b0a1b2c3d4e5f6"),
  name: "Anna",
  age: 29,
  skills: ["javascript", "mongodb"],
  address: { city: "Berlin", zip: "10115" }
}
```

Values can be strings, numbers, dates, arrays, other documents and more.

### 3: What is a collection?

A collection is a group of documents. It is similar to a table in a relational database. Unlike a table, a collection does not force all documents to have the same fields, unless you add schema validation.

### 4: What is a database in MongoDB?

A database is a container for collections. One MongoDB server (or cluster) can hold many databases. Each database has its own set of files on disk and its own permissions.

```javascript
use shop          // switch to (or create) the "shop" database
db.getName()      // "shop"
```

### 5: What is BSON?

BSON stands for Binary JSON. It is the format MongoDB uses to store documents and send them over the network. It supports more types than JSON, for example `Date`, `ObjectId`, `Decimal128`, `Int32`, `Int64`, `Binary` and `Timestamp`. It is also faster to scan because field lengths are stored in the data.

### 6: What is the difference between JSON and BSON?

- JSON is text. BSON is binary.
- JSON only has strings, numbers, booleans, null, arrays and objects. BSON adds dates, 32-bit and 64-bit integers, doubles, decimals, ObjectId, binary data and others.
- BSON can be a bit bigger than JSON for small documents because it stores extra info like lengths, but it is faster to parse.

### 7: What is the `_id` field?

Every document must have an `_id` field. It is the primary key of the document and must be unique inside the collection. If you insert a document without `_id`, the driver or server adds one with an `ObjectId` value. MongoDB automatically creates a unique index on `_id`.

### 8: What is an ObjectId?

An ObjectId is a 12-byte value that is used as the default `_id`. It is made of:

- 4 bytes: timestamp in seconds since the Unix epoch
- 5 bytes: random value unique to the machine and process
- 3 bytes: incrementing counter

Because the first part is a timestamp, ObjectIds created later are generally larger, and you can get the creation time from it:

```javascript
const id = ObjectId();
id.getTimestamp(); // ISODate("2026-...")
```

### 9: What is mongosh?

`mongosh` is the MongoDB Shell. It is a JavaScript and Node.js based command line tool used to connect to MongoDB, run queries and do admin tasks. It replaced the old `mongo` shell, which was removed in MongoDB 6.0.

```bash
mongosh "mongodb://localhost:27017"
```

### 10: What is the default port of MongoDB?

The default port is `27017`. When you start `mongod` with `--shardsvr` the default is `27018`, and with `--configsvr` it is `27019`. You can set any port with the `--port` option or `net.port` in the config file.

### 11: How do you create a database?

You do not create it explicitly. You switch to it with `use`, and it is created when you first store data in it.

```javascript
use library
db.books.insertOne({ title: "Dune" })   // now the "library" database exists
```

### 12: How do you create a collection?

A collection is created automatically when you insert the first document. You can also create it explicitly, which is useful when you want to set options like validation or a capped size.

```javascript
db.createCollection("logs");

db.createCollection("events", { capped: true, size: 1048576 });
```

### 13: How do you insert one document?

Use `insertOne()`.

```javascript
db.users.insertOne({ name: "Tom", email: "tom@example.com" });
// { acknowledged: true, insertedId: ObjectId("...") }
```

### 14: How do you insert many documents?

Use `insertMany()` with an array.

```javascript
db.users.insertMany([
  { name: "Ann", age: 31 },
  { name: "Bob", age: 25 },
]);
```

By default the insert is ordered. If one document fails, the rest after it are not inserted. Pass `{ ordered: false }` to keep going after errors.

### 15: Is `db.collection.insert()` still used?

No. `insert()` is deprecated in mongosh and the drivers. Use `insertOne()`, `insertMany()` or `bulkWrite()` instead.

### 16: How do you find all documents in a collection?

```javascript
db.users.find();
db.users.find({}); // same thing
```

`find()` returns a cursor. In mongosh it prints the first 20 documents and you can type `it` to see more.

### 17: How do you find one document?

Use `findOne()`. It returns the first matching document or `null`.

```javascript
db.users.findOne({ email: "tom@example.com" });
```

### 18: How do you filter documents by a field value?

Pass a filter document to `find()`.

```javascript
db.users.find({ age: 25 });
db.users.find({ "address.city": "Berlin" }); // field inside a sub-document
```

### 19: What are comparison operators in MongoDB?

They compare field values:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `$eq`    | equal                    |
| `$ne`    | not equal                |
| `$gt`    | greater than             |
| `$gte`   | greater than or equal    |
| `$lt`    | less than                |
| `$lte`   | less than or equal       |
| `$in`    | value is in an array     |
| `$nin`   | value is not in an array |

```javascript
db.products.find({ price: { $gte: 10, $lte: 50 } });
db.products.find({ category: { $in: ["books", "music"] } });
```

### 20: What are logical operators in MongoDB?

`$and`, `$or`, `$nor` and `$not`.

```javascript
db.users.find({ $or: [{ age: { $lt: 18 } }, { age: { $gt: 65 } }] });

db.users.find({ age: { $not: { $gt: 30 } } });
```

When you list several fields in one filter, MongoDB already joins them with AND, so `$and` is only needed when you repeat the same field or combine several `$or` blocks.

### 21: How do you update one document?

Use `updateOne()` with a filter and an update document that uses update operators.

```javascript
db.users.updateOne({ name: "Tom" }, { $set: { age: 30 } });
```

### 22: How do you update many documents?

Use `updateMany()`.

```javascript
db.products.updateMany({ category: "books" }, { $inc: { price: 2 } });
```

### 23: What is the difference between `updateOne()` and `replaceOne()`?

`updateOne()` changes only the fields you mention using operators like `$set`. `replaceOne()` replaces the whole document (except `_id`) with a new one.

```javascript
db.users.replaceOne(
  { name: "Tom" },
  { name: "Tom", email: "new@example.com" }, // other old fields are gone
);
```

### 24: What does `$set` do?

`$set` sets the value of a field. If the field does not exist, it is added.

```javascript
db.users.updateOne(
  { _id: 1 },
  { $set: { status: "active", "profile.lang": "en" } },
);
```

### 25: What does `$unset` do?

It removes a field from a document.

```javascript
db.users.updateOne({ _id: 1 }, { $unset: { tempToken: "" } });
```

The value you give (`""` here) does not matter.

### 26: What does `$inc` do?

It increases (or decreases with a negative number) a numeric field. If the field does not exist, it is created with that value.

```javascript
db.posts.updateOne({ _id: 5 }, { $inc: { views: 1, likes: -1 } });
```

### 27: How do you delete documents?

Use `deleteOne()` or `deleteMany()`.

```javascript
db.users.deleteOne({ email: "tom@example.com" });
db.logs.deleteMany({ level: "debug" });
db.logs.deleteMany({}); // deletes all documents but keeps the collection and its indexes
```

### 28: How do you drop a collection?

```javascript
db.logs.drop();
```

This removes the collection, all its documents and its indexes.

### 29: How do you drop a database?

```javascript
use oldapp
db.dropDatabase()
```

### 30: How do you list databases and collections?

```javascript
show dbs              // list databases
show collections      // list collections in the current db
db.getCollectionNames()
```

### 31: What is projection?

Projection lets you choose which fields come back from a query. Use `1` to include and `0` to exclude.

```javascript
db.users.find({}, { name: 1, email: 1 }); // _id is included by default
db.users.find({}, { name: 1, email: 1, _id: 0 }); // hide _id
db.users.find({}, { password: 0 }); // everything except password
```

You cannot mix include and exclude in the same projection, except for `_id`.

### 32: How do you sort query results?

Use `sort()` with `1` for ascending and `-1` for descending.

```javascript
db.products.find().sort({ price: -1, name: 1 });
```

### 33: How do you limit the number of results?

```javascript
db.products.find().limit(10);
```

### 34: How do you skip documents?

```javascript
db.products.find().sort({ _id: 1 }).skip(20).limit(10); // page 3 with 10 per page
```

`skip()` is fine for small offsets, but with large offsets it gets slow because the server still has to walk past the skipped documents.

### 35: How do you count documents?

Use `countDocuments()` for an exact count with a filter, or `estimatedDocumentCount()` for a fast count of the whole collection based on metadata.

```javascript
db.orders.countDocuments({ status: "paid" });
db.orders.estimatedDocumentCount();
```

The old `count()` method is deprecated.

### 36: How do you find distinct values of a field?

```javascript
db.products.distinct("category");
db.products.distinct("category", { inStock: true });
```

### 37: What data types does MongoDB support?

Common BSON types are:

- String
- Int32, Int64 (Long), Double, Decimal128
- Boolean
- Date
- ObjectId
- Array
- Object (embedded document)
- Null
- Binary data (including UUID)
- Regular expression
- Timestamp (mostly internal)
- MinKey and MaxKey

### 38: How do you store a date in MongoDB?

Use a BSON `Date`. In mongosh you can use `new Date()` or `ISODate()`. Dates are stored as milliseconds since the Unix epoch in UTC.

```javascript
db.events.insertOne({ title: "Launch", at: new Date("2026-03-01T10:00:00Z") });
db.events.find({ at: { $gte: ISODate("2026-01-01") } });
```

Do not store dates as strings if you want to sort or compare them correctly.

### 39: What is an embedded document?

It is a document inside another document.

```javascript
{
  name: "Anna",
  address: { street: "Main St 1", city: "Berlin" }
}
```

You query embedded fields with dot notation: `{ "address.city": "Berlin" }`.

### 40: What is dot notation?

Dot notation is how you reach fields inside embedded documents or elements of arrays.

```javascript
db.users.find({ "address.city": "Berlin" });
db.users.find({ "tags.0": "admin" }); // first element of the tags array
```

Field paths with dots must be in quotes.

### 41: How do you query an array field?

If you query an array field with a single value, MongoDB matches documents where any element equals that value.

```javascript
db.posts.find({ tags: "mongodb" }); // any element is "mongodb"
db.posts.find({ tags: ["mongodb", "nosql"] }); // exact array, same order
db.posts.find({ tags: { $all: ["mongodb", "nosql"] } }); // contains both, any order
```

### 42: What does `$push` do?

It adds a value to the end of an array.

```javascript
db.posts.updateOne({ _id: 1 }, { $push: { tags: "database" } });

// add several values
db.posts.updateOne({ _id: 1 }, { $push: { tags: { $each: ["a", "b"] } } });
```

### 43: What does `$addToSet` do?

It adds a value to an array only if it is not already there.

```javascript
db.posts.updateOne({ _id: 1 }, { $addToSet: { tags: "mongodb" } });
```

### 44: What does `$pull` do?

It removes all array elements that match a value or condition.

```javascript
db.posts.updateOne({ _id: 1 }, { $pull: { tags: "old" } });
db.carts.updateOne({ _id: 1 }, { $pull: { items: { qty: 0 } } });
```

### 45: What does `$pop` do?

It removes the first or last element of an array. `1` removes the last, `-1` removes the first.

```javascript
db.queue.updateOne({ _id: 1 }, { $pop: { jobs: -1 } });
```

### 46: What is an upsert?

An upsert is an update that inserts a new document if nothing matches the filter.

```javascript
db.stats.updateOne({ page: "/home" }, { $inc: { hits: 1 } }, { upsert: true });
```

If `/home` does not exist, a new document `{ page: "/home", hits: 1 }` is created.

### 47: What does `$exists` do?

It matches documents that have (or do not have) a field.

```javascript
db.users.find({ phone: { $exists: true } });
db.users.find({ phone: { $exists: false } });
```

Note: a field set to `null` still exists.

### 48: How do you find documents where a field is null?

```javascript
db.users.find({ phone: null });
```

This matches documents where `phone` is `null` and also documents where `phone` is missing. To match only real `null` values, use `{ phone: { $type: "null" } }`.

### 49: What does `$type` do?

It matches documents where a field has a given BSON type.

```javascript
db.items.find({ price: { $type: "string" } }); // find bad data
db.items.find({ price: { $type: ["int", "double"] } });
```

### 50: How do you search with a regular expression?

```javascript
db.users.find({ name: /^an/i });
db.users.find({ name: { $regex: "^an", $options: "i" } });
```

A regex that starts with `^` and is case sensitive can use an index well. Case-insensitive regex or regex without a prefix usually scans the whole index or collection.

### 51: What is an index in MongoDB?

An index is a data structure (a B-tree) that keeps a sorted copy of some field values with pointers to the documents. It lets MongoDB find matching documents without reading every document in the collection.

```javascript
db.users.createIndex({ email: 1 });
```

### 52: How do you create an index?

Use `createIndex()`. `1` means ascending, `-1` means descending.

```javascript
db.orders.createIndex({ customerId: 1 });
db.orders.createIndex({ customerId: 1, createdAt: -1 });
db.users.createIndex({ email: 1 }, { unique: true, name: "email_unique" });
```

The old `ensureIndex()` was removed. Use `createIndex()`.

### 53: How do you list and drop indexes?

```javascript
db.orders.getIndexes();
db.orders.dropIndex("customerId_1");
db.orders.dropIndex({ customerId: 1 });
db.orders.dropIndexes(); // drops all indexes except _id
```

### 54: What is a unique index?

A unique index makes sure no two documents have the same value for the indexed field (or fields).

```javascript
db.users.createIndex({ email: 1 }, { unique: true });
db.users.insertOne({ email: "a@b.com" });
db.users.insertOne({ email: "a@b.com" }); // E11000 duplicate key error
```

### 55: What is the default index in MongoDB?

Every collection has a unique index on `_id`. You cannot drop it.

### 56: What is a cursor?

A cursor is a pointer to the result set of a query. `find()` returns a cursor and the driver fetches documents from the server in batches as you iterate.

```javascript
const cursor = db.users.find({ age: { $gt: 20 } });
while (cursor.hasNext()) {
  printjson(cursor.next());
}

// or
db.users.find().forEach((doc) => print(doc.name));
```

Idle cursors are closed by the server after 10 minutes by default.

### 57: What is the difference between `find()` and `findOne()`?

`find()` returns a cursor that can point to many documents. `findOne()` returns a single document (the first match) or `null`.

### 58: What is the `pretty()` method?

In the old `mongo` shell, `pretty()` formatted output to be easier to read. In `mongosh`, output is already formatted, so `pretty()` is not needed, though it still works.

### 59: What is schema-less (flexible schema) design?

It means MongoDB does not force documents in one collection to have the same fields or types. You can add a new field to some documents without a migration. In real projects you still usually have a schema in your application code, and you can add JSON Schema validation in MongoDB to enforce rules.

### 60: What are the main advantages of MongoDB?

- Flexible document model that maps well to objects in code
- Easy to store nested data and arrays without joins
- Built-in replication for high availability
- Built-in sharding for horizontal scaling
- Rich query language and aggregation framework
- Secondary indexes of many kinds (compound, text, geo, wildcard, TTL)
- Multi-document ACID transactions when you need them

### 61: When is MongoDB not a good choice?

- When the data is highly relational with many joins across many tables and strict relational constraints are central to the app.
- When you need complex multi-table reporting that SQL tools handle better (although MongoDB has `$lookup` and Atlas SQL).
- When the team only knows SQL and the data fits a fixed schema well.

MongoDB can handle many of these cases, but a relational database may be simpler.

### 62: What is the difference between SQL and MongoDB terms?

| SQL         | MongoDB                 |
| ----------- | ----------------------- |
| Database    | Database                |
| Table       | Collection              |
| Row         | Document                |
| Column      | Field                   |
| Index       | Index                   |
| JOIN        | `$lookup` or embedding  |
| Primary key | `_id`                   |
| GROUP BY    | `$group` in aggregation |

### 63: What is a replica set?

A replica set is a group of `mongod` processes that hold the same data. One is the primary that receives writes, and the others are secondaries that copy data from the primary. If the primary goes down, the secondaries elect a new primary. This gives high availability and data redundancy.

### 64: What is sharding?

Sharding splits data across several servers (shards) so that one machine does not have to hold all the data or handle all the traffic. MongoDB uses a shard key to decide which shard a document goes to.

### 65: What is MongoDB Atlas?

Atlas is MongoDB's fully managed cloud database service. It runs on AWS, Google Cloud and Azure. It handles setup, backups, upgrades, monitoring and scaling. It also offers features like Atlas Search, Atlas Vector Search, and Online Archive.

### 66: What is `mongod`?

`mongod` is the main database server process. It stores data, handles queries and manages replication.

### 67: What is `mongos`?

`mongos` is the query router in a sharded cluster. Applications connect to `mongos`, and it sends each request to the right shard or shards and merges the results.

### 68: What is a connection string?

It is a URI that tells a client how to connect to MongoDB.

```text
mongodb://user:pass@host1:27017,host2:27017/mydb?replicaSet=rs0&authSource=admin
mongodb+srv://user:pass@cluster0.abcde.mongodb.net/mydb?retryWrites=true&w=majority
```

The `mongodb+srv` form uses DNS SRV records to find the hosts, and is the usual format for Atlas.

### 69: What is the default storage engine?

WiredTiger. It has been the default since MongoDB 3.2. The old MMAPv1 engine was removed in 4.2.

### 70: How do you check the MongoDB server version?

```javascript
db.version();
```

Or from the command line:

```bash
mongod --version
```

### 71: What is the maximum size of a document?

16 MB. If you need to store bigger files, use GridFS or store the file in object storage (like S3) and keep a reference in MongoDB.

### 72: What is GridFS?

GridFS is a way to store files larger than 16 MB. It splits a file into chunks (255 KB by default) and stores them in two collections: `fs.files` for metadata and `fs.chunks` for the binary data. Drivers provide a GridFS API.

```javascript
// Node.js driver
const bucket = new GridFSBucket(db, { bucketName: "uploads" });
fs.createReadStream("./video.mp4").pipe(bucket.openUploadStream("video.mp4"));
```

### 73: What is a capped collection?

A capped collection has a fixed size. When it is full, the oldest documents are overwritten. Documents are kept in insertion order. It is used for things like logs or caches.

```javascript
db.createCollection("recentLogs", { capped: true, size: 10485760, max: 5000 });
```

For most new use cases, a TTL index on a normal collection is often a better fit because capped collections have some limits (for example, they cannot be sharded).

### 74: What is a TTL index?

A TTL (time to live) index removes documents automatically after some time. It works on a date field.

```javascript
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });
```

A background task runs about every 60 seconds, so documents are not deleted at the exact second.

### 75: What is the aggregation framework?

It is a way to process documents in steps called stages. Each stage changes the documents and passes them to the next stage. It is used for grouping, filtering, reshaping, joining and computing values.

```javascript
db.orders.aggregate([
  { $match: { status: "paid" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } },
]);
```

### 76: What does `$match` do?

`$match` filters documents, like `find()` does. Put it as early as you can in the pipeline so fewer documents go through the later stages and so it can use indexes.

### 77: What does `$group` do?

`$group` groups documents by a key (`_id`) and computes values for each group using accumulators like `$sum`, `$avg`, `$min`, `$max`, `$push`, `$first` and `$count`.

```javascript
db.sales.aggregate([
  {
    $group: {
      _id: "$region",
      revenue: { $sum: "$amount" },
      orders: { $count: {} },
    },
  },
]);
```

Use `_id: null` to group all documents into one group.

### 78: What does `$project` do?

`$project` chooses, renames or computes fields.

```javascript
db.users.aggregate([
  {
    $project: {
      _id: 0,
      fullName: { $concat: ["$first", " ", "$last"] },
      age: 1,
    },
  },
]);
```

### 79: What does `$sort` do in an aggregation?

It sorts documents by one or more fields.

```javascript
{
  $sort: {
    createdAt: -1;
  }
}
```

### 80: What does `$limit` and `$skip` do in aggregation?

`$limit` passes only the first N documents. `$skip` drops the first N documents.

```javascript
db.posts.aggregate([{ $sort: { date: -1 } }, { $skip: 10 }, { $limit: 10 }]);
```

### 81: What does `$unwind` do?

It splits an array field into one document per element.

```javascript
// { _id: 1, tags: ["a", "b"] }
db.posts.aggregate([{ $unwind: "$tags" }]);
// { _id: 1, tags: "a" }
// { _id: 1, tags: "b" }
```

### 82: What does `$lookup` do?

`$lookup` joins documents from another collection in the same database.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer",
    },
  },
]);
```

The result is always an array in the `as` field.

### 83: What does `$count` stage do?

It returns a single document with the number of documents that reached that stage.

```javascript
db.orders.aggregate([{ $match: { status: "paid" } }, { $count: "paidOrders" }]);
// { paidOrders: 312 }
```

### 84: What does `$addFields` (or `$set`) do?

It adds new fields or overwrites existing ones while keeping all the other fields. `$set` is an alias for `$addFields` in aggregation.

```javascript
db.orders.aggregate([
  { $set: { totalWithTax: { $multiply: ["$total", 1.2] } } },
]);
```

### 85: What is the difference between `$project` and `$addFields`?

`$addFields` keeps all existing fields and adds new ones. `$project` returns only the fields you list (when using include mode). Use `$addFields` (or `$set`) when you just want to add a computed value.

### 86: What is a write concern?

Write concern tells MongoDB how many members must confirm a write before it is reported as successful.

```javascript
db.orders.insertOne(
  { item: "book" },
  { writeConcern: { w: "majority", wtimeout: 5000 } },
);
```

- `w: 1` means the primary confirmed.
- `w: "majority"` means most voting members confirmed. This is the default since MongoDB 5.0 for most setups.
- `w: 0` means no confirmation.

### 87: What is a read preference?

Read preference decides which replica set member a read goes to.

- `primary` (default)
- `primaryPreferred`
- `secondary`
- `secondaryPreferred`
- `nearest`

```text
mongodb://host1,host2,host3/?replicaSet=rs0&readPreference=secondaryPreferred
```

### 88: What is the `explain()` method?

`explain()` shows how MongoDB runs a query, for example whether it used an index.

```javascript
db.users.find({ email: "a@b.com" }).explain("executionStats");
```

Look for `IXSCAN` (index scan) versus `COLLSCAN` (collection scan), and compare `totalDocsExamined` with `nReturned`.

### 89: What is `COLLSCAN`?

It means the query read every document in the collection because no suitable index was found. It is fine for small collections but slow for big ones.

### 90: What is `IXSCAN`?

It means the query used an index to find the matching documents.

### 91: How do you rename a field in all documents?

Use `$rename`.

```javascript
db.users.updateMany({}, { $rename: { fname: "firstName" } });
```

### 92: How do you rename a collection?

```javascript
db.oldName.renameCollection("newName");
```

### 93: What does `$min` and `$max` do in an update?

They update a field only if the new value is lower (`$min`) or higher (`$max`) than the current value.

```javascript
db.scores.updateOne({ _id: 1 }, { $max: { highScore: 950 } });
```

### 94: What does `$mul` do?

It multiplies a field by a number.

```javascript
db.products.updateMany({}, { $mul: { price: 1.1 } });
```

### 95: What does `$currentDate` do?

It sets a field to the current date.

```javascript
db.users.updateOne({ _id: 1 }, { $currentDate: { lastLogin: true } });
```

### 96: What is `$setOnInsert`?

It sets fields only when an upsert creates a new document. On a normal update it does nothing.

```javascript
db.users.updateOne(
  { email: "a@b.com" },
  { $set: { lastSeen: new Date() }, $setOnInsert: { createdAt: new Date() } },
  { upsert: true },
);
```

### 97: How do you update a specific element in an array?

Use the positional operator `$`. It points to the first element that matched the filter.

```javascript
db.students.updateOne(
  { _id: 1, "grades.subject": "math" },
  { $set: { "grades.$.score": 95 } },
);
```

### 98: What does `$elemMatch` do?

It matches documents where at least one array element meets all the given conditions.

```javascript
db.students.find({
  grades: { $elemMatch: { subject: "math", score: { $gte: 90 } } },
});
```

Without `$elemMatch`, the conditions could be met by different elements.

### 99: What does `$size` do?

It matches arrays with an exact number of elements.

```javascript
db.posts.find({ tags: { $size: 3 } });
```

It does not accept ranges. For "more than 3", use `{ "tags.3": { $exists: true } }` or `$expr` with `$size`.

### 100: What is `$expr`?

`$expr` lets you use aggregation expressions in a normal query, for example to compare two fields in the same document.

```javascript
db.budgets.find({ $expr: { $gt: ["$spent", "$limit"] } });
```

### 101: What is a compound index?

An index on more than one field.

```javascript
db.orders.createIndex({ customerId: 1, createdAt: -1 });
```

It helps queries that filter on `customerId`, or on `customerId` and `createdAt`, and sorts on `createdAt` within one customer. The order of fields matters.

### 102: What is a multikey index?

When you index a field that holds an array, MongoDB creates an index entry for each element. This is called a multikey index. You create it the normal way, MongoDB detects the array.

```javascript
db.posts.createIndex({ tags: 1 });
db.posts.find({ tags: "mongodb" }); // uses the index
```

### 103: What is a text index?

A text index supports search on words in string fields.

```javascript
db.articles.createIndex({ title: "text", body: "text" });
db.articles.find({ $text: { $search: "mongodb index" } });
```

A collection can have only one text index. For real search features (fuzzy matching, autocomplete, relevance tuning), MongoDB recommends Atlas Search or the self-managed search (`mongot`) available in newer versions.

### 104: What is a geospatial index?

It is used for location queries. The common type is `2dsphere`, which works with GeoJSON points, lines and polygons on a sphere.

```javascript
db.places.createIndex({ location: "2dsphere" });
db.places.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [13.405, 52.52] },
      $maxDistance: 1000,
    },
  },
});
```

GeoJSON coordinates are `[longitude, latitude]`.

### 105: What is a sparse index?

A sparse index only has entries for documents that have the indexed field. Documents without the field are skipped. Partial indexes (with `partialFilterExpression`) give more control and are usually preferred now.

```javascript
db.users.createIndex({ phone: 1 }, { sparse: true });
```

### 106: What is a partial index?

A partial index only indexes documents that match a filter. It uses less space and is faster to update.

```javascript
db.orders.createIndex(
  { createdAt: 1 },
  { partialFilterExpression: { status: "active" } },
);
```

A query must include a condition that matches the filter for the index to be used.

### 107: What is a hashed index?

A hashed index stores the hash of a field value. It is mostly used for hashed sharding to spread data evenly. It supports equality matches, not range queries.

```javascript
db.users.createIndex({ userId: "hashed" });
```

### 108: What is the `admin` database?

It is a special database for administrative commands and for storing users who have cluster-wide roles. Commands like `shutdown`, `replSetGetStatus` and `listDatabases` run against `admin`.

### 109: What is the `local` database?

It stores data that is specific to one server and is not replicated. The most important collection in it is the oplog (`local.oplog.rs`) in a replica set.

### 110: What is the `config` database?

In a sharded cluster, it stores metadata about shards, chunks, databases and collections. It is stored on the config servers. It is also used internally for things like sessions and transactions.

### 111: How do you enable authentication?

Create an admin user first, then start `mongod` with access control turned on.

```yaml
# mongod.conf
security:
  authorization: enabled
```

```javascript
use admin
db.createUser({
  user: "admin",
  pwd: passwordPrompt(),
  roles: [{ role: "root", db: "admin" }]
})
```

### 112: How do you create a user?

```javascript
use shop
db.createUser({
  user: "shopApp",
  pwd: passwordPrompt(),
  roles: [{ role: "readWrite", db: "shop" }]
})
```

### 113: What are built-in roles in MongoDB?

Some common ones:

- `read`, `readWrite` (per database)
- `dbAdmin`, `userAdmin`, `dbOwner` (per database)
- `readAnyDatabase`, `readWriteAnyDatabase`, `userAdminAnyDatabase`, `dbAdminAnyDatabase`
- `clusterAdmin`, `clusterManager`, `clusterMonitor`, `hostManager`
- `backup`, `restore`
- `root`

### 114: What is `mongodump`?

`mongodump` exports data from MongoDB into BSON files. It is part of MongoDB Database Tools.

```bash
mongodump --uri="mongodb://localhost:27017" --db=shop --out=/backups/shop
```

### 115: What is `mongorestore`?

It loads data created by `mongodump` back into MongoDB.

```bash
mongorestore --uri="mongodb://localhost:27017" /backups/shop
mongorestore --uri="..." --nsInclude="shop.orders" --drop /backups/shop
```

### 116: What is `mongoexport` and `mongoimport`?

They export and import data as JSON or CSV. They are useful for moving data to other tools, but they do not keep all BSON types as reliably as `mongodump`.

```bash
mongoexport --uri="mongodb://localhost/shop" --collection=users --out=users.json
mongoimport --uri="mongodb://localhost/shop" --collection=users --file=users.json
mongoimport --uri="..." --collection=items --type=csv --headerline --file=items.csv
```

### 117: What is MongoDB Compass?

Compass is the official GUI for MongoDB. You can browse data, run queries, build aggregation pipelines, view explain plans, manage indexes and check schema. It also has an embedded mongosh.

### 118: What is the oplog?

The oplog (operations log) is a special capped collection in the `local` database. The primary writes every change to it, and secondaries read and apply those changes to stay in sync.

### 119: Does MongoDB support transactions?

Yes. Single-document operations have always been atomic. Multi-document ACID transactions are supported on replica sets (since 4.0) and sharded clusters (since 4.2).

### 120: Is a single document update atomic?

Yes. A write to one document is atomic, even if it changes many fields or embedded documents inside it. Other operations either see the whole change or none of it.

### 121: What is `bulkWrite()`?

It sends many write operations in one call.

```javascript
db.products.bulkWrite(
  [
    { insertOne: { document: { _id: 1, name: "Pen" } } },
    { updateOne: { filter: { _id: 2 }, update: { $inc: { stock: -1 } } } },
    { deleteOne: { filter: { _id: 3 } } },
  ],
  { ordered: false },
);
```

### 122: What is the difference between ordered and unordered bulk writes?

- Ordered (default): operations run one after another. If one fails, the rest are stopped.
- Unordered: MongoDB can run them in any order and continues after errors. It is usually faster.

### 123: How do you check the stats of a collection?

```javascript
db.orders.stats(); // still works in mongosh
db.orders.aggregate([{ $collStats: { storageStats: {} } }]);
```

`db.collection.stats()` and the `collStats` command are deprecated in newer versions. The `$collStats` aggregation stage is the recommended way.

### 124: How do you check the stats of a database?

```javascript
db.stats();
```

It shows the number of collections, objects, data size, storage size and index size.

### 125: What does `db.serverStatus()` show?

It returns a lot of runtime info about the server: connections, operation counts, memory, WiredTiger cache, replication, locks and more. It is often used for monitoring.

```javascript
db.serverStatus().connections;
```

### 126: How do you see currently running operations?

```javascript
db.currentOp({ active: true, secs_running: { $gt: 5 } });
// or
db.getSiblingDB("admin").aggregate([
  { $currentOp: {} },
  { $match: { active: true } },
]);
```

### 127: How do you kill a running operation?

```javascript
db.killOp(12345); // opid from currentOp
```

### 128: What is a namespace in MongoDB?

A namespace is the full name of a collection: `database.collection`, for example `shop.orders`.

### 129: Are field names case sensitive?

Yes. `Name` and `name` are different fields. Collection and database names are also case sensitive, although on some file systems database names that differ only in case can still cause conflicts.

### 130: Can a field name start with `$` or contain a dot?

Since MongoDB 5.0, field names with `$` prefixes or dots are allowed in stored documents, but they are hard to work with and many query features do not support them well. You need special operators like `$getField` and `$setField` to read them. It is best to avoid them.

### 131: What is `$in` used for?

It matches any value from a list.

```javascript
db.orders.find({ status: { $in: ["paid", "shipped"] } });
```

It is often cleaner than several `$or` conditions on the same field.

### 132: What is the difference between `$in` and `$all`?

`$in` matches if the field equals any of the listed values. `$all` matches if an array field contains all the listed values.

```javascript
db.posts.find({ tags: { $in: ["a", "b"] } }); // has a OR b
db.posts.find({ tags: { $all: ["a", "b"] } }); // has a AND b
```

### 133: How do you return only some elements of an array?

Use `$slice` in a projection.

```javascript
db.posts.find({}, { comments: { $slice: 5 } }); // first 5
db.posts.find({}, { comments: { $slice: -5 } }); // last 5
db.posts.find({}, { comments: { $slice: [10, 5] } }); // skip 10, take 5
```

You can also use `$elemMatch` in a projection to return the first matching element.

### 134: How do you check if a document was updated?

The result of an update has counters:

```javascript
const res = db.users.updateOne({ _id: 1 }, { $set: { active: true } });
// { acknowledged: true, matchedCount: 1, modifiedCount: 1, upsertedId: null, upsertedCount: 0 }
```

`matchedCount` can be 1 while `modifiedCount` is 0 if the value was already the same.

### 135: What is `findOneAndUpdate()`?

It updates one document and returns it, either the version before or after the update.

```javascript
db.counters.findOneAndUpdate(
  { _id: "orderId" },
  { $inc: { seq: 1 } },
  { returnDocument: "after", upsert: true },
);
```

In mongosh and the Node.js driver (v6+) the option is `returnDocument: "after"` or `"before"`.

### 136: What is `findOneAndDelete()`?

It deletes one document and returns it. It is useful for simple job queues.

```javascript
db.jobs.findOneAndDelete({ status: "ready" }, { sort: { priority: -1 } });
```

### 137: What is `findOneAndReplace()`?

It replaces one document and returns the old or new version.

```javascript
db.config.findOneAndReplace(
  { _id: "app" },
  { _id: "app", theme: "dark" },
  { returnDocument: "after" },
);
```

### 138: How do you see indexes used in a query plan?

Run `explain()` and look at the `winningPlan`. The `IXSCAN` stage includes `indexName` and `keyPattern`.

```javascript
db.orders.find({ customerId: 5 }).explain().queryPlanner.winningPlan;
```

### 139: How do you hide an index?

A hidden index is kept up to date but the query planner does not use it. It is a safe way to test what happens if you drop an index.

```javascript
db.orders.hideIndex("customerId_1");
db.orders.unhideIndex("customerId_1");
```

### 140: What is a covered query?

A query is covered when all the fields in the filter and the projection are in the same index. MongoDB answers it from the index alone without reading documents.

```javascript
db.users.createIndex({ email: 1, name: 1 });
db.users.find({ email: "a@b.com" }, { _id: 0, email: 1, name: 1 });
```

In the explain output, `totalDocsExamined` is `0`.

### 141: What is `$nin`?

It matches documents where the field value is not in the list, or the field does not exist.

```javascript
db.users.find({ role: { $nin: ["admin", "staff"] } });
```

### 142: What is the difference between `$ne` and `$not`?

`$ne` checks that a value is not equal to something. `$not` reverses another operator expression.

```javascript
db.items.find({ qty: { $ne: 0 } });
db.items.find({ qty: { $not: { $gt: 100 } } }); // qty <= 100 or missing
```

### 143: How do you use `$or` with an index?

Each clause of `$or` can use its own index. For a query to use indexes, every clause must have a supporting index, otherwise MongoDB does a collection scan.

```javascript
db.users.createIndex({ email: 1 });
db.users.createIndex({ phone: 1 });
db.users.find({ $or: [{ email: "a@b.com" }, { phone: "123" }] });
```

### 144: How do you check if MongoDB is running?

```bash
mongosh --eval "db.runCommand({ ping: 1 })"
```

A healthy server returns `{ ok: 1 }`.

### 145: Where is MongoDB configuration stored?

In a YAML config file, usually `/etc/mongod.conf` on Linux.

```yaml
storage:
  dbPath: /var/lib/mongodb
systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true
net:
  port: 27017
  bindIp: 127.0.0.1
```

### 146: What is `bindIp`?

It sets which network interfaces `mongod` listens on. By default it is `127.0.0.1`, so only local connections work. To allow remote clients, add the server's IP. Never expose MongoDB to the internet without authentication, TLS and firewall rules.

### 147: What format are MongoDB logs in?

Since 4.4, server logs are structured JSON. Each line is one JSON object with fields like `t` (time), `s` (severity), `c` (component), `msg` and `attr`. This makes them easy to parse with tools like `jq`.

### 148: What is the MongoDB Node.js driver?

It is the official library to use MongoDB from Node.js. All methods return Promises (callbacks were removed in v5).

```javascript
import { MongoClient } from "mongodb";

const client = new MongoClient("mongodb://localhost:27017");
await client.connect();
const users = client.db("shop").collection("users");
const user = await users.findOne({ email: "a@b.com" });
await client.close();
```

### 149: What is Mongoose?

Mongoose is a popular ODM (Object Data Modeling) library for Node.js. It adds schemas, validation, middleware (hooks), and model methods on top of the official driver.

```javascript
import mongoose from "mongoose";

await mongoose.connect("mongodb://localhost:27017/shop");
const User = mongoose.model(
  "User",
  new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, unique: true },
  }),
);
await User.create({ name: "Ann", email: "ann@example.com" });
```

### 150: What is the Stable API?

The Stable API (formerly called Versioned API) lets an application declare an API version (currently `"1"`). MongoDB promises that commands in that version will keep working the same way across server upgrades, so you can upgrade the server without changing code.

```javascript
const client = new MongoClient(uri, {
  serverApi: { version: "1", strict: true, deprecationErrors: true },
});
```

## Moderate Questions

### 151: How do you decide between embedding and referencing?

Embed when:

- The data is read together most of the time.
- The child data belongs to one parent (one-to-one or one-to-few).
- The embedded array will not grow without limit.

Reference when:

- The related data is large or grows without a limit (for example, all log entries of a user).
- The data is shared by many parents (many-to-many).
- You often need to read or update the child data on its own.

A common rule: "data that is accessed together should be stored together".

### 152: How do you model a one-to-many relationship?

It depends on how many "many" there are.

One-to-few: embed.

```javascript
{ _id: 1, name: "Ann", addresses: [{ city: "Berlin" }, { city: "Paris" }] }
```

One-to-many (hundreds or thousands): store references in the child.

```javascript
// products
{ _id: 10, name: "Phone" }
// reviews
{ _id: 501, productId: 10, rating: 5, text: "Good" }
```

One-to-squillions (unbounded): always keep the reference on the child side, never an array of ids in the parent.

### 153: How do you model a many-to-many relationship?

Store arrays of references on one or both sides, or use a separate linking collection if the relationship has its own data.

```javascript
// students
{ _id: 1, name: "Ann", courseIds: [101, 102] }
// courses
{ _id: 101, title: "Databases" }
```

```javascript
db.students.aggregate([
  { $match: { _id: 1 } },
  {
    $lookup: {
      from: "courses",
      localField: "courseIds",
      foreignField: "_id",
      as: "courses",
    },
  },
]);
```

### 154: What is the extended reference pattern?

You copy a few frequently used fields of a related document into the referencing document, to avoid a `$lookup` on common reads.

```javascript
// order
{
  _id: 1,
  customer: { _id: 55, name: "Ann", city: "Berlin" },  // copied fields
  items: [...]
}
```

The trade-off is that you need to update the copies if the source changes, so pick fields that rarely change.

### 155: What is the subset pattern?

You keep only the most used part of a large list inside the main document, and store the full list in another collection. For example, keep the 10 newest reviews in the product document and all reviews in a `reviews` collection. This keeps the main document small so it fits better in memory.

### 156: What is the bucket pattern?

You group many small related items into one document, for example all sensor readings for one hour.

```javascript
{
  sensorId: 7,
  start: ISODate("2026-05-01T10:00:00Z"),
  count: 3,
  readings: [{ t: ISODate("..."), v: 21.5 }, { t: ISODate("..."), v: 21.7 }, { t: ISODate("..."), v: 21.6 }]
}
```

It reduces the number of documents and index size. For time-based data, time series collections now do this for you automatically.

### 157: What is the computed pattern?

You store a computed value (like a total or an average) at write time so reads do not have to compute it each time.

```javascript
db.products.updateOne(
  { _id: 10 },
  { $inc: { "rating.count": 1, "rating.sum": 5 } },
);
// average = sum / count, computed cheaply or stored as well
```

### 158: What is the outlier pattern?

Most documents follow the normal shape, but a few "outliers" would get too big (for example a celebrity with millions of followers). You mark those documents with a flag and store the extra data in overflow documents.

```javascript
{ _id: "book1", buyers: [/* first 1000 ids */], hasOverflow: true }
```

### 159: What is the schema versioning pattern?

You add a field like `schemaVersion` to documents. The application knows how to read each version and can migrate documents slowly over time instead of all at once.

```javascript
{ _id: 1, schemaVersion: 2, name: { first: "Ann", last: "Lee" } }
```

### 160: What is the polymorphic pattern?

Documents with different shapes but a similar purpose are kept in one collection. A field like `type` tells them apart.

```javascript
{ type: "book", title: "Dune", pages: 412 }
{ type: "movie", title: "Dune", durationMin: 155 }
```

### 161: What is the attribute pattern?

When documents have many similar fields that you want to search on, you turn them into an array of key-value pairs so you can use one index.

```javascript
// instead of { releaseUS: date, releaseFR: date, releaseDE: date }
{
  releases: [
    { k: "US", v: ISODate("...") },
    { k: "FR", v: ISODate("...") },
  ];
}

db.movies.createIndex({ "releases.k": 1, "releases.v": 1 });
```

### 162: How do you add schema validation to a collection?

Use `$jsonSchema` in the `validator` option.

```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string", pattern: "^.+@.+$" },
        age: { bsonType: "int", minimum: 0 },
      },
    },
  },
  validationLevel: "strict",
  validationAction: "error",
});
```

### 163: How do you add validation to an existing collection?

Use the `collMod` command.

```javascript
db.runCommand({
  collMod: "users",
  validator: { $jsonSchema: { bsonType: "object", required: ["email"] } },
  validationLevel: "moderate",
});
```

### 164: What is the difference between `validationLevel` strict and moderate?

- `strict` (default): validation runs on all inserts and updates.
- `moderate`: validation runs on inserts and on updates to documents that are already valid. Existing invalid documents can still be updated without being checked.
- `off`: no validation.

### 165: What is the difference between `validationAction` error and warn?

- `error` (default): invalid writes are rejected.
- `warn`: invalid writes are allowed but a warning is written to the log.
- `errorAndLog` (added in 8.1): invalid writes are rejected and also logged.

### 166: How do you find documents that do not match the current validator?

```javascript
const { validator } = db.getCollectionInfos({ name: "users" })[0].options;
db.users.find({ $nor: [validator] });
```

### 167: What is the ESR rule for compound indexes?

ESR stands for Equality, Sort, Range. When building a compound index, put fields in this order:

1. Fields used for equality matches
2. Fields used for sorting
3. Fields used for range filters

```javascript
// query
db.orders
  .find({ status: "paid", amount: { $gt: 100 } })
  .sort({ createdAt: -1 });

// good index
db.orders.createIndex({ status: 1, createdAt: -1, amount: 1 });
```

This lets MongoDB avoid an in-memory sort and scan fewer keys.

### 168: What is an index prefix?

A prefix is the first field(s) of a compound index. An index `{ a: 1, b: 1, c: 1 }` can support queries on `a`, on `a, b`, and on `a, b, c`. It cannot efficiently support a query only on `b` or `c`.

### 169: Does the sort direction in a compound index matter?

For a single field index, no, because MongoDB can walk the index in both directions. For a compound index it matters when you sort on more than one field. An index `{ a: 1, b: -1 }` supports `sort({ a: 1, b: -1 })` and `sort({ a: -1, b: 1 })`, but not `sort({ a: 1, b: 1 })`.

### 170: What is a blocking sort?

When MongoDB cannot use an index for a sort, it has to load the documents and sort them in memory. This is a blocking sort (`SORT` stage in explain). If it needs more than 100 MB of memory, the query fails unless disk use is allowed. Since MongoDB 6.0, `allowDiskUseByDefault` is `true`, so large sorts spill to disk instead of failing, but they are still slow.

### 171: How do you read the `executionStats` in explain output?

Important fields:

- `nReturned`: documents returned
- `totalKeysExamined`: index keys scanned
- `totalDocsExamined`: documents read
- `executionTimeMillis`: time taken
- `winningPlan.stage`: for example `IXSCAN`, `FETCH`, `COLLSCAN`, `SORT`

A good query has `totalKeysExamined` and `totalDocsExamined` close to `nReturned`.

### 172: What are the three explain verbosity modes?

- `queryPlanner` (default): shows the plan picked, without running the query.
- `executionStats`: runs the winning plan and shows stats.
- `allPlansExecution`: runs and shows stats for all candidate plans too.

### 173: What is the query plan cache?

When there are several possible indexes, the query planner tries them, picks the best, and stores that choice in a plan cache for that query shape. Later queries with the same shape reuse it. The cache is cleared when indexes change or the server restarts.

```javascript
db.orders.getPlanCache().list();
db.orders.getPlanCache().clear();
```

### 174: What is `hint()`?

`hint()` forces the query to use a specific index.

```javascript
db.orders.find({ status: "paid", customerId: 5 }).hint({ customerId: 1 });
```

Use it carefully. A better long-term fix is usually a better index. Since MongoDB 8.0 you can also use query settings (`setQuerySettings`) to set an index hint for a query shape without changing application code.

### 175: How do you create an index without blocking the collection?

Since MongoDB 4.2, all index builds use an optimized process that holds an exclusive lock only at the start and end. Reads and writes can continue during the build. The old `background: true` option is ignored now. On large collections, index builds still use CPU and I/O, so run them in quiet hours when you can.

### 176: What is a wildcard index?

A wildcard index indexes all fields (or all fields under a path). It is useful when documents have unknown or changing field names.

```javascript
db.products.createIndex({ "attributes.$**": 1 });
db.products.find({ "attributes.color": "red" });
```

Since MongoDB 7.0 you can make compound wildcard indexes, for example `{ tenantId: 1, "attributes.$**": 1 }`.

### 177: What are collation settings?

Collation sets language rules for string comparison, such as case and accent sensitivity.

```javascript
db.users.createIndex({ name: 1 }, { collation: { locale: "en", strength: 2 } });
db.users.find({ name: "anna" }).collation({ locale: "en", strength: 2 }); // matches "Anna"
```

`strength: 1` ignores case and accents, `strength: 2` ignores case only. The query must use the same collation as the index for the index to be used.

### 178: How do you do case-insensitive search efficiently?

Use a case-insensitive collation with an index instead of a regex with the `i` flag.

```javascript
db.users.createIndex(
  { email: 1 },
  { collation: { locale: "en", strength: 2 } },
);
db.users
  .find({ email: "ANN@EXAMPLE.COM" })
  .collation({ locale: "en", strength: 2 });
```

Another option is to store a lowercase copy of the field and index that.

### 179: How does `$lookup` with a pipeline work?

You can run a sub-pipeline on the joined collection, with variables from the outer document.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productIds",
      foreignField: "_id",
      let: { minStock: 5 },
      pipeline: [
        { $match: { $expr: { $gte: ["$stock", "$$minStock"] } } },
        { $project: { name: 1, price: 1 } },
      ],
      as: "products",
    },
  },
]);
```

Since 5.0 you can use `localField`/`foreignField` together with `pipeline`.

### 180: How do you flatten the `$lookup` result into the main document?

Use `$unwind` (for one match) or `$replaceRoot` with `$mergeObjects`.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer",
    },
  },
  { $unwind: { path: "$customer", preserveNullAndEmptyArrays: true } },
]);
```

### 181: What is `$facet`?

`$facet` runs several sub-pipelines on the same input and returns their results in one document. It is useful for search pages with counts and results.

```javascript
db.products.aggregate([
  { $match: { category: "laptops" } },
  {
    $facet: {
      results: [{ $sort: { price: 1 } }, { $limit: 20 }],
      total: [{ $count: "n" }],
      byBrand: [{ $group: { _id: "$brand", n: { $sum: 1 } } }],
    },
  },
]);
```

The output of `$facet` is one document, so it must stay under 16 MB.

### 182: What is `$bucket` and `$bucketAuto`?

They group documents into ranges.

```javascript
db.products.aggregate([
  {
    $bucket: {
      groupBy: "$price",
      boundaries: [0, 50, 100, 500],
      default: "500+",
      output: { count: { $sum: 1 } },
    },
  },
]);

db.products.aggregate([{ $bucketAuto: { groupBy: "$price", buckets: 4 } }]);
```

### 183: What is `$replaceRoot` / `$replaceWith`?

They replace the whole document with an embedded document or an expression.

```javascript
db.users.aggregate([{ $replaceWith: "$profile" }]);
db.users.aggregate([
  { $replaceWith: { $mergeObjects: [{ name: "$name" }, "$profile"] } },
]);
```

### 184: What is `$out`?

`$out` writes the pipeline result to a collection, replacing it if it exists. It must be the last stage.

```javascript
db.orders.aggregate([
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $out: "customerTotals" },
]);
```

It can write to a different database too: `{ $out: { db: "reports", coll: "totals" } }`. It can also create a time series collection if you pass `timeseries` options.

### 185: What is `$merge`?

`$merge` writes pipeline results into a collection, but unlike `$out` it can merge with existing documents. It is used for incremental materialized views.

```javascript
db.orders.aggregate([
  { $match: { createdAt: { $gte: ISODate("2026-10-01") } } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  {
    $merge: {
      into: "customerTotals",
      on: "_id",
      whenMatched: [{ $set: { total: { $add: ["$total", "$$new.total"] } } }],
      whenNotMatched: "insert",
    },
  },
]);
```

### 186: What is the difference between `$out` and `$merge`?

- `$out` replaces the whole target collection.
- `$merge` can insert, replace, merge, keep or fail on each document, and can use a custom pipeline.
- `$merge` can write to a sharded collection. `$out` cannot.

### 187: What is a view?

A view is a read-only virtual collection defined by an aggregation pipeline. It runs the pipeline every time you query it.

```javascript
db.createView("activeUsers", "users", [
  { $match: { active: true } },
  { $project: { password: 0 } },
]);
db.activeUsers.find({ country: "DE" });
```

### 188: What is an on-demand materialized view?

It is a real collection that you fill with `$merge` or `$out` from an aggregation, usually on a schedule. Reads are fast because results are stored, but data is only as fresh as the last run.

### 189: What does `$sortByCount` do?

It groups by an expression, counts, and sorts by count descending.

```javascript
db.posts.aggregate([{ $unwind: "$tags" }, { $sortByCount: "$tags" }]);
```

It is the same as `$group` with `$sum: 1` followed by `$sort`.

### 190: What does `$sample` do?

It returns random documents.

```javascript
db.questions.aggregate([{ $sample: { size: 5 } }]);
```

### 191: What does `$unionWith` do?

It adds the documents of another collection (optionally after a pipeline) to the current pipeline, like `UNION ALL` in SQL.

```javascript
db.sales2025.aggregate([
  {
    $unionWith: { coll: "sales2026", pipeline: [{ $match: { region: "EU" } }] },
  },
  { $group: { _id: "$region", total: { $sum: "$amount" } } },
]);
```

### 192: What does `$graphLookup` do?

It performs a recursive search, for example to find all managers above an employee or all items in a category tree.

```javascript
db.employees.aggregate([
  { $match: { name: "Ann" } },
  {
    $graphLookup: {
      from: "employees",
      startWith: "$managerId",
      connectFromField: "managerId",
      connectToField: "_id",
      as: "managers",
      maxDepth: 5,
    },
  },
]);
```

### 193: What are window functions in MongoDB?

`$setWindowFields` (added in 5.0) computes values over a window of documents, like running totals, moving averages and ranks.

```javascript
db.sales.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$store",
      sortBy: { date: 1 },
      output: {
        runningTotal: {
          $sum: "$amount",
          window: { documents: ["unbounded", "current"] },
        },
        rank: { $rank: {} },
      },
    },
  },
]);
```

### 194: What do `$first`, `$last`, `$top`, `$bottom`, `$firstN` and `$topN` do?

They are accumulators to pick values from a group.

- `$first` / `$last`: value from the first or last document in the group (based on the order coming in).
- `$top` / `$bottom` (5.2+): pick based on their own `sortBy`.
- `$firstN`, `$lastN`, `$topN`, `$bottomN`, `$minN`, `$maxN`: return N values.

```javascript
db.scores.aggregate([
  {
    $group: {
      _id: "$gameId",
      top3: {
        $topN: { n: 3, sortBy: { score: -1 }, output: ["$player", "$score"] },
      },
    },
  },
]);
```

### 195: How do you get the median or a percentile?

Use `$median` and `$percentile` (added in 7.0).

```javascript
db.requests.aggregate([
  {
    $group: {
      _id: "$endpoint",
      p50: { $median: { input: "$latencyMs", method: "approximate" } },
      p95: {
        $percentile: { input: "$latencyMs", p: [0.95], method: "approximate" },
      },
    },
  },
]);
```

### 196: How do you work with dates in aggregation?

There are many date operators: `$year`, `$month`, `$dayOfMonth`, `$dateToString`, `$dateFromString`, `$dateTrunc`, `$dateAdd`, `$dateSubtract`, `$dateDiff`.

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: {
        $dateTrunc: {
          date: "$createdAt",
          unit: "day",
          timezone: "Europe/Berlin",
        },
      },
      orders: { $sum: 1 },
    },
  },
  { $sort: { _id: 1 } },
]);
```

### 197: How do you use conditional logic in aggregation?

Use `$cond`, `$switch` and `$ifNull`.

```javascript
db.orders.aggregate([
  {
    $project: {
      size: {
        $switch: {
          branches: [
            { case: { $lt: ["$total", 50] }, then: "small" },
            { case: { $lt: ["$total", 500] }, then: "medium" },
          ],
          default: "large",
        },
      },
      discount: { $cond: [{ $gte: ["$total", 100] }, 10, 0] },
      note: { $ifNull: ["$note", "none"] },
    },
  },
]);
```

### 198: How do you work with arrays in aggregation without `$unwind`?

Use array expression operators like `$filter`, `$map`, `$reduce`, `$size`, `$arrayElemAt`, `$in`, `$sortArray`.

```javascript
db.orders.aggregate([
  {
    $project: {
      expensiveItems: {
        $filter: {
          input: "$items",
          as: "i",
          cond: { $gt: ["$$i.price", 100] },
        },
      },
      itemNames: { $map: { input: "$items", as: "i", in: "$$i.name" } },
      total: {
        $reduce: {
          input: "$items",
          initialValue: 0,
          in: { $add: ["$$value", "$$this.price"] },
        },
      },
    },
  },
]);
```

This is often faster than `$unwind` + `$group`.

### 199: What is the aggregation pipeline memory limit?

Each stage can use up to 100 MB of RAM. If a stage needs more (for example a large `$group` or `$sort`), it can write temporary files to disk. Since 6.0 `allowDiskUseByDefault` is `true` on the server. You can still set it per query:

```javascript
db.events.aggregate(pipeline, { allowDiskUse: true });
```

### 200: Can an aggregation pipeline be used in an update?

Yes, since 4.2. This lets you set fields based on other fields of the same document.

```javascript
db.users.updateMany({}, [
  { $set: { fullName: { $concat: ["$firstName", " ", "$lastName"] } } },
  { $unset: ["firstName", "lastName"] },
]);
```

Only some stages are allowed: `$addFields`/`$set`, `$project`/`$unset`, `$replaceRoot`/`$replaceWith`.

### 201: How does the positional operator `$[]` work?

`$[]` updates all elements of an array.

```javascript
db.students.updateOne({ _id: 1 }, { $inc: { "grades.$[].score": 5 } });
```

### 202: How does the filtered positional operator `$[<identifier>]` work?

It updates only the array elements that match `arrayFilters`.

```javascript
db.students.updateMany(
  {},
  { $set: { "grades.$[g].passed": true } },
  { arrayFilters: [{ "g.score": { $gte: 50 } }] },
);
```

It also works with nested arrays:

```javascript
db.courses.updateOne(
  { _id: 1 },
  { $set: { "modules.$[m].lessons.$[l].done": true } },
  { arrayFilters: [{ "m.id": 3 }, { "l.id": { $in: [1, 2] } }] },
);
```

### 203: How do you keep an array sorted and limited in size?

Use `$push` with `$each`, `$sort` and `$slice`.

```javascript
db.players.updateOne(
  { _id: 1 },
  {
    $push: {
      recentScores: {
        $each: [{ score: 88, at: new Date() }],
        $sort: { at: -1 },
        $slice: 10,
      },
    },
  },
);
```

This keeps only the 10 newest scores.

### 204: How do you insert at a specific position in an array?

Use `$push` with `$position`.

```javascript
db.lists.updateOne(
  { _id: 1 },
  { $push: { items: { $each: ["first"], $position: 0 } } },
);
```

### 205: Can `updateOne()` choose which document to update when many match?

Since MongoDB 8.0, `updateOne()` and `replaceOne()` accept a `sort` option. Before that, you had to use `findOneAndUpdate()` for that.

```javascript
db.tasks.updateOne(
  { status: "queued" },
  { $set: { status: "running" } },
  { sort: { priority: -1, createdAt: 1 } },
);
```

### 206: What is the new `bulkWrite` command in MongoDB 8.0?

Since 8.0 there is a server command `bulkWrite` that can write to many collections (even in different databases) in a single request. Drivers expose it as a client-level bulk write.

```javascript
// Node.js driver 6.10+
await client.bulkWrite([
  {
    namespace: "shop.orders",
    name: "insertOne",
    document: { _id: 1, total: 20 },
  },
  {
    namespace: "shop.stock",
    name: "updateOne",
    filter: { sku: "A1" },
    update: { $inc: { qty: -1 } },
  },
  {
    namespace: "audit.log",
    name: "insertOne",
    document: { action: "order", at: new Date() },
  },
]);
```

In mongosh it is available as `db.getMongo().bulkWrite([...])`.

### 207: How do you use a multi-document transaction?

You start a session, start a transaction, run operations with that session, and commit. The recommended way is `withTransaction()`, which retries on transient errors.

```javascript
const session = client.startSession();
try {
  await session.withTransaction(async () => {
    const accounts = client.db("bank").collection("accounts");
    await accounts.updateOne(
      { _id: "A" },
      { $inc: { balance: -100 } },
      { session },
    );
    await accounts.updateOne(
      { _id: "B" },
      { $inc: { balance: 100 } },
      { session },
    );
  });
} finally {
  await session.endSession();
}
```

### 208: What are the limits of transactions?

- By default a transaction must finish within 60 seconds (`transactionLifetimeLimitSeconds`).
- They add overhead, so keep them short and touch few documents.
- They need a replica set or sharded cluster, not a standalone server.
- Some operations are not allowed, for example writing to capped collections or `system.*` collections, or running `count` (use `countDocuments` which uses an aggregation).
- Creating collections and indexes inside a transaction is allowed since 4.4 with some rules.

### 209: What are `TransientTransactionError` and `UnknownTransactionCommitResult`?

- `TransientTransactionError`: the whole transaction can be retried from the start (for example a write conflict or a primary change).
- `UnknownTransactionCommitResult`: the commit may or may not have happened, so you retry the commit only.

`session.withTransaction()` handles both of these for you.

### 210: What are read concern levels?

Read concern controls how "committed" the data you read must be.

- `local`: the latest data on the node, may be rolled back. Default for reads on primary.
- `available`: like `local`, but for sharded clusters it can return orphan documents. Fastest.
- `majority`: data that a majority of members confirmed, will not be rolled back.
- `linearizable`: reads reflect all majority-committed writes that finished before the read began. Only on primary, and slow.
- `snapshot`: reads from a single point in time. Used in transactions and with `atClusterTime`.

### 211: What is causal consistency?

In a causally consistent session, reads respect the order of your own writes. If you write and then read (even from a secondary), the read sees the write. It needs `readConcern: "majority"` and `writeConcern: "majority"` to give full guarantees.

```javascript
const session = client.startSession({ causalConsistency: true });
await coll.insertOne({ _id: 1 }, { session, writeConcern: { w: "majority" } });
await coll.findOne(
  { _id: 1 },
  { session, readPreference: "secondary", readConcern: { level: "majority" } },
);
```

### 212: What are retryable writes?

If a write fails because of a network error or a primary change, the driver automatically retries it once. The server makes sure the write is not applied twice. Retryable writes are on by default (`retryWrites=true`) in modern drivers.

### 213: What are retryable reads?

Drivers automatically retry a read once if it fails because of a network error or a primary change. It is on by default (`retryReads=true`).

### 214: How does replica set election work?

When the primary is not reachable for longer than `electionTimeoutMillis` (10 seconds by default), an eligible secondary calls an election. Members vote, and the candidate that gets a majority of votes becomes the new primary. Members with higher priority are preferred, and a member must have the latest data among voters to win.

### 215: What is an arbiter?

An arbiter is a replica set member that only votes in elections and holds no data. It is used to get an odd number of voters cheaply. MongoDB does not recommend arbiters for production when you use `w: "majority"`, because they can cause problems with majority writes if a data member goes down. A third data-bearing member is better.

### 216: What is a hidden member?

A hidden member holds a copy of the data but is not visible to client applications and cannot become primary (priority 0). It is used for backups or reporting.

```javascript
cfg = rs.conf();
cfg.members[2].priority = 0;
cfg.members[2].hidden = true;
rs.reconfig(cfg);
```

### 217: What is a delayed member?

A delayed member is a hidden member that applies the oplog with a time delay, for example one hour. If someone deletes data by mistake, you can recover it from the delayed member.

```javascript
cfg.members[3].priority = 0;
cfg.members[3].hidden = true;
cfg.members[3].secondaryDelaySecs = 3600;
rs.reconfig(cfg);
```

The old option name was `slaveDelay`.

### 218: Why should a replica set have an odd number of voting members?

Elections need a strict majority. With an even number, a network split could leave both sides with half the votes and no primary. Three or five voting members are common. A replica set can have up to 50 members, but only 7 can vote.

### 219: How do you set up a replica set?

Start each `mongod` with the same `replSetName`, then initiate.

```bash
mongod --replSet rs0 --port 27017 --dbpath /data/rs0-0 --bind_ip localhost,host1
```

```javascript
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "host1:27017" },
    { _id: 1, host: "host2:27017" },
    { _id: 2, host: "host3:27017" },
  ],
});
rs.status();
```

### 220: How do you check replication lag?

```javascript
rs.printSecondaryReplicationInfo();
rs.status().members.map((m) => ({
  name: m.name,
  state: m.stateStr,
  optime: m.optimeDate,
}));
```

Lag is the difference between the primary's latest optime and a secondary's optime.

### 221: What is a rollback in a replica set?

If a primary accepts writes that did not replicate to a majority, and then it steps down, those writes may be rolled back when it rejoins. Rolled-back documents are written to files in a `rollback` folder. Using `w: "majority"` prevents your acknowledged writes from being rolled back.

### 222: What is `rs.stepDown()`?

It makes the current primary step down so that another member becomes primary. It is used for maintenance.

```javascript
rs.stepDown(60); // do not try to become primary again for 60 seconds
```

### 223: What is the oplog window?

It is the time span between the oldest and newest entry in the oplog. If a secondary falls behind more than this window, it can no longer catch up and needs a full initial sync. You can see it with `rs.printReplicationInfo()` and resize the oplog with `replSetResizeOplog`.

### 224: What is initial sync?

When a new member joins (or a member falls too far behind), it copies all data from another member, builds indexes, and then applies the oplog to catch up. Since 5.2 there is also a file copy based initial sync in Enterprise, which is faster for large data sets.

### 225: What is a change stream?

A change stream lets an application listen to inserts, updates, deletes and other changes in real time. It is built on the oplog and needs a replica set or sharded cluster.

```javascript
const stream = db
  .collection("orders")
  .watch([{ $match: { operationType: { $in: ["insert", "update"] } } }]);
for await (const change of stream) {
  console.log(change.operationType, change.documentKey);
}
```

### 226: How do you resume a change stream after a failure?

Each event has a resume token in `_id`. Save it and pass it back as `resumeAfter` or `startAfter`.

```javascript
const stream = coll.watch([], { resumeAfter: savedToken });
```

`startAfter` can also resume after an `invalidate` event. You can also use `startAtOperationTime`. Resuming only works if the token is still inside the oplog window.

### 227: How do you get the full document in an update change event?

Use `fullDocument: "updateLookup"` to get the current version of the document, or use pre and post images (6.0+) for the exact before and after state.

```javascript
db.runCommand({
  collMod: "orders",
  changeStreamPreAndPostImages: { enabled: true },
});

const stream = coll.watch([], {
  fullDocument: "whenAvailable",
  fullDocumentBeforeChange: "whenAvailable",
});
```

### 228: What levels can you open a change stream on?

- A collection: `db.coll.watch()`
- A database: `db.watch()`
- The whole deployment: `client.watch()` (mongosh: `db.getMongo().watch()`)

### 229: What is a time series collection?

A collection type optimized for measurements over time (metrics, IoT, logs). MongoDB groups data internally into buckets by a metadata field and time, which saves storage and speeds up time queries.

```javascript
db.createCollection("weather", {
  timeseries: {
    timeField: "ts",
    metaField: "sensor",
    granularity: "minutes",
  },
  expireAfterSeconds: 60 * 60 * 24 * 30,
});

db.weather.insertOne({
  ts: new Date(),
  sensor: { id: 7, type: "temp" },
  value: 21.4,
});
```

### 230: What are the limits of time series collections?

They improved a lot over versions, but some rules still apply:

- The `timeField` must be a date and you cannot change it after insert.
- Updates and deletes are allowed (fully since 7.0), but they are slower than inserts and are best done on the `metaField`.
- Granularity can only be increased (for example `seconds` to `minutes`), or you can use custom `bucketMaxSpanSeconds` and `bucketRoundingSeconds`.
- You cannot open a change stream on a time series collection, and you cannot write to one inside a transaction.
- They cannot be capped collections.

Check the docs for your exact version, because limits keep getting removed.

### 231: What is a clustered collection?

A clustered collection (5.3+) stores documents in order of a clustered index key, which is `_id`. Queries on `_id` ranges are faster and there is no separate `_id` index to maintain.

```javascript
db.createCollection("events", {
  clusteredIndex: { key: { _id: 1 }, unique: true, name: "events_clustered" },
  expireAfterSeconds: 86400,
});
```

This works best when `_id` values grow over time, like ObjectId or a timestamp.

### 232: How do you paginate efficiently in MongoDB?

Avoid big `skip()` values. Use range-based (keyset) pagination based on the last value you saw.

```javascript
// first page
const page = await coll
  .find({})
  .sort({ createdAt: -1, _id: -1 })
  .limit(20)
  .toArray();
const last = page.at(-1);

// next page
await coll
  .find({
    $or: [
      { createdAt: { $lt: last.createdAt } },
      { createdAt: last.createdAt, _id: { $lt: last._id } },
    ],
  })
  .sort({ createdAt: -1, _id: -1 })
  .limit(20)
  .toArray();
```

Create an index on `{ createdAt: -1, _id: -1 }`.

### 233: How do you implement an auto-increment field?

MongoDB has no built-in auto-increment. Use a counters collection with `findOneAndUpdate` and `$inc`.

```javascript
function nextSeq(name) {
  return db.counters.findOneAndUpdate(
    { _id: name },
    { $inc: { seq: 1 } },
    { upsert: true, returnDocument: "after" },
  ).seq;
}
db.invoices.insertOne({ _id: nextSeq("invoice"), total: 50 });
```

Remember this creates a hot document under heavy write load. ObjectId or UUID is usually a better primary key.

### 234: How do you store a UUID?

Use the BSON Binary subtype 4.

```javascript
db.users.insertOne({ _id: UUID(), name: "Ann" });
db.users.find({ _id: UUID("9b2b3c3e-...") });
```

In drivers, set `uuidRepresentation: "standard"` where needed (Node.js driver uses standard by default for the `UUID` class). MongoDB 8.0 also added the `$toUUID` expression to convert strings.

### 235: Why use `Decimal128` for money?

`Double` cannot represent some decimal values exactly (`0.1 + 0.2` is not `0.3`). `Decimal128` stores exact decimal numbers, which is what you want for money.

```javascript
db.payments.insertOne({ amount: NumberDecimal("19.99") });
db.payments.aggregate([{ $group: { _id: null, sum: { $sum: "$amount" } } }]);
```

Another common way is to store amounts as integers in cents.

### 236: What is the difference between `Int32`, `Int64` and `Double` in mongosh?

In mongosh, a plain number like `5` is stored as a `Double` by default. If you need an integer type, use `NumberInt(5)` (Int32) or `NumberLong(5)` (Int64). Drivers usually map their own integer types correctly.

```javascript
db.t.insertOne({ a: 5, b: NumberInt(5), c: NumberLong(5) });
db.t.find({ a: { $type: "double" } });
```

### 237: What is a sharded cluster made of?

- Shards: each is a replica set that holds part of the data.
- Config servers: a replica set that stores cluster metadata.
- `mongos` routers: route queries from the application to the right shards.

Since 8.0, the config server replica set can also store application data as a "config shard", which saves hardware in small clusters.

### 238: What is a shard key?

It is a field (or fields) in every document that decides which shard the document belongs to. Since 5.0 you can change the shard key with resharding, and since 4.4 you can refine it by adding suffix fields, but picking a good one at the start is still important.

### 239: What makes a good shard key?

- High cardinality: many different values.
- Low frequency: no value appears in a huge number of documents.
- Non-monotonic writes: values do not always grow (like timestamps), otherwise all new writes go to one shard.
- Matches your common queries, so most queries go to one shard instead of all of them.

A common choice is a compound key like `{ customerId: 1, orderDate: 1 }` or a hashed key.

### 240: What is the difference between ranged and hashed sharding?

- Ranged sharding splits data by ranges of the shard key value. Range queries on the key are efficient, but monotonic keys create hot spots.
- Hashed sharding uses the hash of the key. It spreads writes evenly, but range queries go to all shards.

```javascript
sh.shardCollection("shop.orders", { customerId: 1, orderDate: 1 });
sh.shardCollection("shop.events", { deviceId: "hashed" });
```

### 241: What is a chunk?

A chunk is a contiguous range of shard key values that belongs to one shard. Since 7.0 the balancer works on data size per shard instead of chunk counts, and chunks can be much larger than the old 128 MB default.

### 242: What is the balancer?

The balancer is a background process (on the config server primary) that moves data between shards so each shard holds a similar amount. You can stop it or set a balancing window.

```javascript
sh.getBalancerState();
sh.stopBalancer();
sh.startBalancer();
```

### 243: What is a targeted query vs a scatter-gather (broadcast) query?

- Targeted: the query includes the shard key (or its prefix), so `mongos` sends it only to the shards that hold the data.
- Scatter-gather: the query does not include the shard key, so `mongos` sends it to all shards and merges the results. It gets slower as you add shards.

### 244: How do you shard a collection?

```javascript
sh.enableSharding("shop"); // optional since 6.0
db.orders.createIndex({ customerId: 1, orderDate: 1 });
sh.shardCollection("shop.orders", { customerId: 1, orderDate: 1 });
sh.status();
```

### 245: What are jumbo chunks?

A jumbo chunk is a chunk that grew too big but cannot be split because all documents in it have the same shard key value. The balancer cannot move it easily. It happens with low cardinality shard keys. Fixing it usually means refining or changing the shard key.

### 246: What are zones in sharding?

Zones let you pin ranges of shard key values to specific shards. A common use is keeping EU customers' data on shards in Europe.

```javascript
sh.addShardToZone("shardEU", "EU");
sh.updateZoneKeyRange(
  "shop.users",
  { region: "EU", _id: MinKey },
  { region: "EU", _id: MaxKey },
  "EU",
);
```

### 247: What is WiredTiger cache?

WiredTiger keeps recently used data and indexes in its own memory cache. By default it uses the larger of 50% of (RAM - 1 GB) or 256 MB. The OS file system cache is also used. Your working set (hot data and indexes) should fit in RAM for good performance.

### 248: What compression does WiredTiger use?

- Collections: `snappy` by default. `zstd` and `zlib` are available.
- Indexes: prefix compression.
- Journal: `snappy` by default.

```javascript
db.createCollection("archive", {
  storageEngine: { wiredTiger: { configString: "block_compressor=zstd" } },
});
```

### 249: What is the journal?

The journal is a write-ahead log. WiredTiger writes changes to it before they are part of a checkpoint. If the server crashes, it replays the journal on startup to recover. Since 6.1 journaling is always on and cannot be turned off. A checkpoint is written about every 60 seconds.

### 250: What does `j: true` mean in a write concern?

It means the write must be written to the on-disk journal before it is acknowledged. With `w: "majority"`, the default is to wait for the journal on the majority of members (controlled by `writeConcernMajorityJournalDefault`).

```javascript
db.payments.insertOne(doc, { writeConcern: { w: "majority", j: true } });
```

### 251: What is the working set?

The working set is the data and indexes your application uses most often. If it fits in RAM (WiredTiger cache plus file system cache), most reads are served from memory. If it does not, the server reads from disk a lot and performance drops.

### 252: How do you find slow queries?

Use the database profiler or the slow query log. By default, operations slower than 100 ms are written to the log.

```javascript
db.setProfilingLevel(1, { slowms: 50 }); // profile ops slower than 50 ms
db.system.profile.find().sort({ ts: -1 }).limit(5);
db.setProfilingLevel(0);
```

Levels: `0` off, `1` slow operations only, `2` all operations. Level 2 adds a lot of overhead. In Atlas, use the Query Profiler and Performance Advisor.

### 253: What does `$indexStats` show?

It shows how many times each index was used since the server started. It helps find unused indexes.

```javascript
db.orders.aggregate([
  { $indexStats: {} },
  { $project: { name: 1, "accesses.ops": 1 } },
]);
```

### 254: Why should you avoid too many indexes?

Each index:

- Slows down inserts, updates and deletes, because it must be updated too.
- Takes disk space and RAM.
- Gives the query planner more choices to evaluate.

Keep only indexes that your queries need. Remove indexes that are prefixes of other indexes (for example `{ a: 1 }` when you also have `{ a: 1, b: 1 }`), unless they are unique.

### 255: Can MongoDB use more than one index for a query?

Usually a query uses one index. MongoDB can do index intersection in some cases (`AND_SORTED`, `AND_HASH` stages) and uses one index per clause for `$or`, but in practice a well designed compound index is much better than relying on index intersection.

### 256: What is index selectivity?

Selectivity is how well an index narrows down results. An index on `email` (unique values) is very selective. An index on `isActive` (two values) is not. Low selectivity indexes often do not help much, unless they are part of a compound index or partial index.

### 257: How do you use `$text` search scores?

```javascript
db.articles
  .find(
    { $text: { $search: "replica set election" } },
    { score: { $meta: "textScore" } },
  )
  .sort({ score: { $meta: "textScore" } });
```

You can search for a phrase with quotes (`"\"replica set\""`) and exclude words with `-` (`"mongodb -sql"`).

### 258: What is Atlas Search?

Atlas Search is full-text search built on Apache Lucene, available inside MongoDB. You define a search index and query it with the `$search` aggregation stage. It supports fuzzy search, autocomplete, facets, highlighting and custom scoring. Since MongoDB 8.2, search and vector search are also available for self-managed Community and Enterprise deployments through the `mongot` process.

```javascript
db.movies.aggregate([
  {
    $search: {
      index: "default",
      text: {
        query: "space adventure",
        path: ["title", "plot"],
        fuzzy: { maxEdits: 1 },
      },
    },
  },
  { $limit: 10 },
  { $project: { title: 1, score: { $meta: "searchScore" } } },
]);
```

### 259: What is the difference between `$text` and `$search`?

- `$text` uses the built-in text index. It is basic: stemming and stop words, no fuzzy matching, one text index per collection.
- `$search` uses a Lucene-based search index (Atlas Search or `mongot`). It has many more features and better relevance, but needs a separate search process.

### 260: What is Atlas Vector Search?

It lets you store vector embeddings in documents and find similar documents with the `$vectorSearch` stage. It is used for semantic search and RAG applications.

```javascript
db.docs.aggregate([
  {
    $vectorSearch: {
      index: "vector_index",
      path: "embedding",
      queryVector: [0.12, -0.03 /* ... */],
      numCandidates: 200,
      limit: 10,
      filter: { lang: "en" },
    },
  },
  { $project: { title: 1, score: { $meta: "vectorSearchScore" } } },
]);
```

### 261: How do you define a vector search index?

```javascript
db.docs.createSearchIndex({
  name: "vector_index",
  type: "vectorSearch",
  definition: {
    fields: [
      {
        type: "vector",
        path: "embedding",
        numDimensions: 1536,
        similarity: "cosine",
      },
      { type: "filter", path: "lang" },
    ],
  },
});
```

Search indexes are managed with `createSearchIndex`, `updateSearchIndex`, `dropSearchIndex` and `$listSearchIndexes`.

### 262: How do you connect to MongoDB from Python?

Use PyMongo (sync) or PyMongo's async API (the separate Motor driver is deprecated in favor of `AsyncMongoClient` in PyMongo).

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.shop
db.users.insert_one({"name": "Ann"})
for u in db.users.find({"age": {"$gt": 20}}).sort("name", 1):
    print(u["name"])
```

```python
from pymongo import AsyncMongoClient

client = AsyncMongoClient("mongodb://localhost:27017")
user = await client.shop.users.find_one({"name": "Ann"})
```

### 263: How do you connect to MongoDB from Java?

```java
try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
    MongoCollection<Document> users = client.getDatabase("shop").getCollection("users");
    users.insertOne(new Document("name", "Ann").append("age", 31));
    Document ann = users.find(Filters.eq("name", "Ann")).first();
}
```

Spring Data MongoDB is a common choice in Spring Boot apps.

### 264: Why should you reuse a `MongoClient` instance?

`MongoClient` holds a connection pool and monitors the servers. Creating a new client for each request is slow and can open too many connections. Create one client when the app starts and share it.

### 265: What is the connection pool and how do you tune it?

The driver keeps a pool of open connections per server. Common options:

- `maxPoolSize` (default 100)
- `minPoolSize`
- `maxIdleTimeMS`
- `waitQueueTimeoutMS`
- `maxConnecting` (default 2)

```text
mongodb://host/?maxPoolSize=50&minPoolSize=5&maxIdleTimeMS=60000
```

### 266: What timeouts should you set in a driver?

- `serverSelectionTimeoutMS` (default 30 s): how long to wait to find a suitable server.
- `connectTimeoutMS`: time to open a socket.
- `socketTimeoutMS`: time to wait on a socket read.
- `timeoutMS` (Client Side Operation Timeout, newer drivers): one timeout for the whole operation including retries. It replaces many older options.

```javascript
const client = new MongoClient(uri, { timeoutMS: 5000 });
await coll.find({}, { timeoutMS: 2000 }).toArray();
```

### 267: What is `maxTimeMS`?

It sets a server-side time limit for an operation. If the operation takes longer, the server stops it.

```javascript
db.orders.find({ status: "paid" }).maxTimeMS(2000);
db.orders.aggregate(pipeline, { maxTimeMS: 5000 });
```

You can also set a default with the `defaultMaxTimeMS` cluster parameter (8.0+).

### 268: How do you handle duplicate key errors in code?

Catch the error and check the code `11000`.

```javascript
try {
  await users.insertOne({ email: "a@b.com" });
} catch (err) {
  if (err.code === 11000) {
    console.log("Email already exists", err.keyValue);
  } else {
    throw err;
  }
}
```

### 269: What is the difference between `deleteMany({})` and `drop()`?

- `deleteMany({})` deletes documents one by one, writes each delete to the oplog, keeps indexes and collection options. It is slow on large collections.
- `drop()` removes the collection, its data and indexes in one fast operation.

### 270: How do you copy a collection?

Use an aggregation with `$out` or `$merge`.

```javascript
db.orders.aggregate([{ $match: {} }, { $out: "orders_backup" }]);
```

`$out` does not copy indexes, so create them again. `db.collection.copyTo()` and `db.cloneCollection()` were removed.

### 271: How do you convert a field type for all documents?

Use an update with an aggregation pipeline and `$convert` or helpers like `$toInt`, `$toDate`, `$toDecimal`.

```javascript
db.products.updateMany({ price: { $type: "string" } }, [
  {
    $set: {
      price: { $convert: { input: "$price", to: "decimal", onError: null } },
    },
  },
]);
```

### 272: What is `$getField` and `$setField`?

They read and set fields whose names are dynamic or contain special characters like `.` or `$`.

```javascript
db.inventory.aggregate([
  { $match: { $expr: { $gt: [{ $getField: "price.usd" }, 100] } } },
]);
```

### 273: How do you turn an object into an array and back?

Use `$objectToArray` and `$arrayToObject`.

```javascript
db.config.aggregate([
  { $project: { pairs: { $objectToArray: "$settings" } } },
  // settings: { a: 1, b: 2 } -> pairs: [{ k: "a", v: 1 }, { k: "b", v: 2 }]
]);
```

This is useful when you need to filter or loop over unknown field names.

### 274: How do you join on more than one field with `$lookup`?

Use a pipeline with `let` and `$expr`.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "prices",
      let: { sku: "$sku", region: "$region" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$sku", "$$sku"] },
                { $eq: ["$region", "$$region"] },
              ],
            },
          },
        },
      ],
      as: "price",
    },
  },
]);
```

Create a compound index on `{ sku: 1, region: 1 }` in `prices`.

### 275: Does `$lookup` use indexes?

Yes. With `localField`/`foreignField`, an index on the `foreignField` is used for each lookup. In a pipeline `$lookup`, `$match` with `$expr` and `$eq` can use indexes on the joined collection. Without an index, each input document causes a scan of the foreign collection, which is very slow. Since 6.0, the slot based query engine also speeds up `$lookup` and can use hash join when there is no index.

### 276: Can you `$lookup` into a sharded collection?

Yes, since MongoDB 5.1 the `from` collection can be sharded. Before that it had to be unsharded.

### 277: How do you see why an aggregation is slow?

```javascript
db.orders.explain("executionStats").aggregate(pipeline);
```

Check if the first stages use an index (`IXSCAN`), how many documents each stage processes, and whether `$group` or `$sort` spill to disk (`usedDisk: true`).

### 278: What pipeline optimizations does MongoDB do automatically?

- Moves `$match` earlier when it only depends on fields that are not changed.
- Merges `$sort` + `$limit` into a top-N sort.
- Combines several `$match`, `$skip` or `$limit` stages.
- Moves `$project` / `$addFields` after a `$match` when possible.
- Coalesces `$lookup` + `$unwind` into one step.

You still should write pipelines in a sensible order, starting with `$match` and `$sort` that can use indexes.

### 279: How do you get the last N records per group?

Use `$sort` and `$group` with `$topN` (or `$firstN` after sort).

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: "$customerId",
      lastOrders: {
        $topN: { n: 3, sortBy: { createdAt: -1 }, output: "$$ROOT" },
      },
    },
  },
]);
```

### 280: How do you deduplicate documents?

Find duplicates with `$group`, then delete the extra ones.

```javascript
db.users
  .aggregate([
    { $group: { _id: "$email", ids: { $push: "$_id" }, n: { $sum: 1 } } },
    { $match: { n: { $gt: 1 } } },
  ])
  .forEach((g) => {
    g.ids.shift(); // keep the first
    db.users.deleteMany({ _id: { $in: g.ids } });
  });
```

Then add a unique index so it does not happen again.

### 281: What are the default users and roles after installing MongoDB?

There are no users and authorization is off by default in self-managed MongoDB. The "localhost exception" lets you create the first user from localhost when auth is enabled and no users exist. Always create an admin user and turn on authorization before exposing the server.

### 282: How do you create a custom role?

```javascript
use admin
db.createRole({
  role: "ordersReader",
  privileges: [
    { resource: { db: "shop", collection: "orders" }, actions: ["find"] }
  ],
  roles: []
})
db.grantRolesToUser("reportUser", [{ role: "ordersReader", db: "admin" }])
```

### 283: What authentication mechanisms does MongoDB support?

- SCRAM-SHA-256 (default) and SCRAM-SHA-1
- X.509 certificates
- LDAP proxy (Enterprise, deprecated in 8.0 in favor of OIDC)
- Kerberos (Enterprise)
- OpenID Connect / OIDC (Enterprise and Atlas, for workforce identity)
- AWS IAM (Atlas)

### 284: How do you enable TLS?

```yaml
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

Clients connect with `tls=true` in the connection string. The old `ssl` options are deprecated.

### 285: What is encryption at rest?

It encrypts data files on disk. In MongoDB Enterprise, WiredTiger can encrypt data with AES256 and a key from a KMIP server or local key file. In Atlas, data is encrypted at rest by default and you can bring your own key (customer key management).

### 286: What is Client-Side Field Level Encryption (CSFLE)?

With CSFLE, the driver encrypts specific fields before sending them to the server, so the server never sees the plain values. Keys are stored in a key vault collection and protected by a KMS (AWS KMS, Azure, GCP, KMIP or local key). Deterministic encryption allows equality queries.

### 287: What is Queryable Encryption?

Queryable Encryption is a newer form of client-side encryption that uses randomized encryption but still allows queries on encrypted fields. It became GA in 7.0 for equality queries, and 8.0 added range queries (`$lt`, `$gt`, etc.). Prefix, suffix and substring queries were added later as previews.

```javascript
const encryptedFields = {
  fields: [
    { path: "ssn", bsonType: "string", queries: { queryType: "equality" } },
    {
      path: "salary",
      bsonType: "int",
      queries: { queryType: "range", min: 0, max: 1000000 },
    },
  ],
};
```

### 288: What is auditing in MongoDB?

Auditing (Enterprise and Atlas) records events like authentication, user changes, schema changes and optionally CRUD operations to a log. You can filter which events are recorded.

```yaml
auditLog:
  destination: file
  format: JSON
  path: /var/log/mongodb/audit.json
```

### 289: How do you protect MongoDB from NoSQL injection?

Never pass raw user input objects into queries. An attacker could send `{ "$ne": null }` instead of a password string.

```javascript
// bad
users.findOne({ user: req.body.user, pass: req.body.pass });

// better: force types
users.findOne({ user: String(req.body.user) });
```

Also validate input with a schema library, avoid `$where` and `$function` with user data, and use the least privileged user for the app. Mongoose has the `sanitizeFilter` option.

### 290: Is server-side JavaScript still recommended?

No. `$where`, `$function`, `$accumulator` and map-reduce run JavaScript on the server. They are slow and are deprecated starting in MongoDB 8.0. Use the aggregation framework instead.

### 291: Why was map-reduce deprecated?

Map-reduce has been deprecated since 5.0. It runs JavaScript, which is slow, and every map-reduce job can be written as an aggregation pipeline (`$group`, `$merge`, `$accumulator` if needed) that runs faster.

### 292: How do you take a consistent backup of a replica set?

Options:

- `mongodump --oplog` against a member, and restore with `mongorestore --oplogReplay`. Works for small data, not for sharded clusters.
- File system snapshots (LVM, EBS) with journaling on the same volume.
- `db.fsyncLock()` on a secondary, copy files, then `db.fsyncUnlock()`.
- Atlas backups or Ops Manager / Cloud Manager for continuous backup with point-in-time restore.

### 293: How do you upgrade a replica set?

Do a rolling upgrade:

1. Upgrade secondaries one at a time (stop, replace binaries, start, wait for `SECONDARY` state).
2. Step down the primary with `rs.stepDown()`.
3. Upgrade the old primary.
4. When everything runs the new version and is stable, set the feature compatibility version.

```javascript
db.adminCommand({ setFeatureCompatibilityVersion: "8.0", confirm: true });
```

You must upgrade one major version at a time (for example 7.0 to 8.0).

### 294: What is the feature compatibility version (FCV)?

FCV controls which features that change data on disk are enabled. After upgrading binaries, FCV stays at the old version so you can still downgrade. When you are sure, you raise the FCV to enable new features.

```javascript
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 });
```

### 295: What is the MongoDB release schedule?

MongoDB has major releases (like 7.0, 8.0) about once a year, which are supported long term and run on self-managed and Atlas. In between there are rapid releases (like 8.1, 8.2, 8.3) that are mostly for Atlas. Starting with 8.2, some minor releases are also supported for self-managed deployments, so check the support policy for your version.

### 296: How do you limit the size of a result in a driver?

Use `limit()`, `batchSize()` and projection. `batchSize` controls how many documents the server sends in each network round trip.

```javascript
const cursor = coll
  .find({ type: "a" }, { projection: { name: 1 } })
  .batchSize(500)
  .limit(5000);
for await (const doc of cursor) {
  /* ... */
}
```

### 297: What is `allowDiskUse`?

It lets aggregation stages and sorts write temporary data to disk when they exceed 100 MB of memory. Since 6.0 the server parameter `allowDiskUseByDefault` is `true`, so you rarely need to set it.

### 298: What are `$sum`, `$avg` and `$count` as accumulators?

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: "$status",
      orders: { $count: {} }, // same as $sum: 1
      revenue: { $sum: "$total" },
      avgOrder: { $avg: "$total" },
    },
  },
]);
```

### 299: How do you group by multiple fields?

Use an object as `_id`.

```javascript
db.sales.aggregate([
  {
    $group: {
      _id: { year: { $year: "$date" }, region: "$region" },
      total: { $sum: "$amount" },
    },
  },
  { $sort: { "_id.year": 1, "_id.region": 1 } },
]);
```

### 300: How do you get the size of an array in a query or aggregation?

```javascript
db.posts.aggregate([
  {
    $project: {
      title: 1,
      commentCount: { $size: { $ifNull: ["$comments", []] } },
    },
  },
]);

db.posts.find({
  $expr: { $gt: [{ $size: { $ifNull: ["$comments", []] } }, 10] },
});
```

`$size` fails if the field is missing, so wrap it with `$ifNull`. If you query this often, store the count in a field and index it.

## Advanced Questions

### 301: How does WiredTiger handle concurrency?

WiredTiger uses document-level concurrency. Many clients can write to different documents in the same collection at the same time. It uses MVCC (multi-version concurrency control): readers see a consistent snapshot, and writers create new versions instead of blocking readers. If two operations try to change the same document at the same time, one gets a write conflict and is retried internally.

### 302: What locks does MongoDB still use?

MongoDB uses intent locks at the global, database and collection level (`IS`, `IX`) for normal reads and writes, so they do not block each other. Exclusive locks (`X`) are only needed for some operations like dropping a collection or the start and end of an index build. Since 5.0, many read operations use a lock-free path and do not take collection locks at all.

### 303: What are concurrent transaction tickets (read/write tickets)?

WiredTiger limits how many operations can run inside the storage engine at once using tickets. Before 7.0 the default was 128 read and 128 write tickets. Since 7.0, MongoDB adjusts the number of tickets dynamically to avoid overload. The algorithm is called throughput probing and is part of a feature called execution control. If tickets run out, operations queue, which you can see in `serverStatus().queues` (8.0) or `wiredTiger.concurrentTransactions` (older).

### 304: What is the slot-based query execution engine (SBE)?

SBE is a newer query engine that MongoDB introduced in 5.1 for some queries. It is faster for certain operations like `$group` and `$lookup` because it uses a more efficient execution model. In 7.0+ it is used for eligible `find` and aggregation queries that start with `$group` or `$lookup`. The classic engine is still used for other queries. Explain output shows which engine was used (`explainVersion: "2"` means SBE).

### 305: What are query settings in MongoDB 8.0?

Query settings let you attach settings to a query shape without changing application code. For example, you can force an index or reject a bad query. They replace index filters, which are deprecated.

```javascript
db.adminCommand({
  setQuerySettings: {
    find: "orders",
    filter: { status: "paid", customerId: 1 },
    $db: "shop",
  },
  settings: {
    indexHints: {
      ns: { db: "shop", coll: "orders" },
      allowedIndexes: ["status_1_customerId_1"],
    },
  },
});

db.adminCommand({
  setQuerySettings: {
    find: "orders",
    filter: { note: { $regex: "x" } },
    $db: "shop",
  },
  settings: { reject: true },
});

db.aggregate([{ $querySettings: {} }]); // list them
```

### 306: What is a query shape?

A query shape is the query with literal values removed. `{ status: "paid", total: { $gt: 10 } }` and `{ status: "new", total: { $gt: 99 } }` have the same shape. MongoDB uses shapes for the plan cache, query settings and `$queryStats` (Atlas). Since 8.0 there is also a `queryShapeHash` field in explain and logs.

### 307: What are express query stages in MongoDB 8.0?

For very simple queries like an equality match on `_id` or on a unique index, MongoDB 8.0 skips normal query planning and uses an "express" path (`EXPRESS_IXSCAN`, `EXPRESS_CLUSTERED_IXSCAN`, `EXPRESS_UPDATE`, `EXPRESS_DELETE`). This reduces latency for point lookups.

### 308: How does the query planner choose a plan?

1. It finds all indexes that could answer the query and builds candidate plans.
2. If there is only one candidate, it uses it.
3. Otherwise it runs all candidates in a trial period for a small amount of work (up to 10,000 works or until one returns 101 results).
4. It scores each plan by results per unit of work (productivity), with bonuses for no fetch and no blocking sort.
5. The winning plan is cached for that query shape.

Cached plans are re-evaluated if they become much less efficient than when cached (the replanning mechanism).

### 309: What is the cost-based ranker in newer MongoDB versions?

In recent versions (8.x), MongoDB has been adding a cost-based plan ranker that estimates plan costs from statistics (sampling or histograms) instead of only running trial executions. It helps when trial runs give misleading results, for example when the first matching documents are not representative. This work is still being rolled out, so check the release notes for your exact version before relying on it.

### 310: What does `totalKeysExamined` higher than `nReturned` tell you?

The index is not selective enough for the query, or fields are in the wrong order in a compound index (for example the range field comes before the equality field). MongoDB scans many index keys and throws most away. Reorder the index using the ESR rule, or add the missing fields.

### 311: What does a `FETCH` stage with a `filter` after `IXSCAN` mean?

MongoDB used the index to find candidate documents, but some conditions were not in the index, so it had to load each document and check the rest of the filter. If `docsExamined` is much bigger than `nReturned`, add those fields to the index.

### 312: Why is a multikey index sometimes slow with range queries?

For a range query on an array field, MongoDB cannot always combine bounds from both ends of the range, because different array elements could match different parts. The explain shows bounds like `[10, inf]` instead of `[10, 20]`. Use `$elemMatch` so both conditions apply to the same element and the bounds can be combined.

```javascript
db.t.find({ scores: { $elemMatch: { $gte: 10, $lte: 20 } } });
```

### 313: What are the rules for compound multikey indexes?

A compound index can have at most one field that is an array in any given document. You cannot insert a document where two indexed fields are both arrays (`cannot index parallel arrays`). It is fine if `a` is an array in one document and `b` is an array in another.

### 314: How does sorting on a multikey field work?

When you sort by an array field, MongoDB uses the minimum element for ascending and the maximum element for descending sort. A multikey index can support a sort only if the sort and the bounds do not need the multikey field in a way that breaks ordering. Check explain for a `SORT` stage.

### 315: How do partial indexes and unique constraints work together?

A unique partial index enforces uniqueness only for documents that match the filter. This is how you make a field unique only when it exists or only for active records.

```javascript
db.users.createIndex(
  { username: 1 },
  { unique: true, partialFilterExpression: { deletedAt: { $exists: false } } },
);
```

Deleted users can now share a username with an active user.

### 316: Why does a unique index fail when many documents lack the field?

A normal unique index stores missing fields as `null`, so only one document can be missing the field. Use a partial index with `{ field: { $exists: true } }` (or a `$type` filter) to allow many documents without it. Sparse unique indexes also work but partial is more flexible.

### 317: How do you build an index on a large production replica set with minimum impact?

Normal index builds (4.4+) are replicated and built at the same time on all data-bearing members, and the primary waits for a commit quorum. To reduce the impact:

- Build during low traffic.
- Make sure there is enough disk and memory (`maxIndexBuildMemoryUsageMegabytes`).
- Use `commitQuorum` if you want to control which members must finish.
- For very large builds, the rolling method still works: take each secondary out of the set, build the index as a standalone, rejoin, then step down the primary and do the same.

```javascript
db.orders.createIndex({ sku: 1 }, {}, "majority"); // commitQuorum
```

### 318: What is `commitQuorum` for index builds?

It says how many data-bearing voting members must finish the index build before the primary commits it. Default is `"votingMembers"` (all voting data members). You can set a number or `"majority"`. You can change it while a build runs with `setIndexCommitQuorum`.

### 319: How do you find and resume interrupted index builds?

Since 5.0, index builds that were in progress when a node shut down are resumed automatically from where they stopped (if the shutdown was clean). You can see builds in progress in `db.currentOp({ "command.createIndexes": { $exists: true } })` and stop them with `dropIndexes` on the index name.

### 320: Why can a large `$in` list be slow?

Each value in `$in` becomes a separate index seek. With thousands of values the planner has more work, and combining `$in` with a sort can turn into an in-memory sort (or a `SORT_MERGE` of many ranges). Keep `$in` lists reasonable, batch large lists, or redesign so that you can use a range or a join.

### 321: What is the "explode for sort" optimization?

If a query has `$in` on a prefix field and sorts on the next field of a compound index, MongoDB can do one index scan per `$in` value and merge them in order (`SORT_MERGE`) instead of a blocking sort. It works when the number of combinations is below a limit (200 by default).

### 322: What causes a write conflict, and how do you reduce it?

Two operations try to modify the same document at the same time. WiredTiger retries the losing operation internally (outside transactions), but in a transaction you get a `WriteConflict` error with label `TransientTransactionError`. To reduce conflicts:

- Avoid "hot" documents that everyone updates (for example one global counter). Split the counter into several documents and sum them.
- Keep transactions short.
- Touch documents in a consistent order.

### 323: How do transactions work in a sharded cluster?

When a transaction touches more than one shard, `mongos` coordinates a two-phase commit. One shard becomes the transaction coordinator. All participant shards prepare, then the coordinator tells them to commit. If only one shard is involved, it is a normal single-shard commit, which is faster. Cross-shard transactions have more latency, so design the shard key so related data lives on the same shard.

### 324: What is snapshot isolation in transactions?

Transactions with `readConcern: "snapshot"` read data from one point in time. They do not see changes committed by others after the transaction started. Writes from the transaction become visible to others only after commit. If someone else changes a document you also write, you get a write conflict.

### 325: How long can a transaction hold its snapshot, and why does it matter?

WiredTiger keeps old versions of documents in its cache as long as an open snapshot needs them. Long transactions (or long snapshot reads) cause cache pressure. That is why `transactionLifetimeLimitSeconds` defaults to 60 seconds, and `minSnapshotHistoryWindowInSeconds` (default 300) controls how much history is kept for snapshot reads at a past time.

### 326: What is `atClusterTime` and when would you use it?

You can run a read at a specific cluster time with `readConcern: { level: "snapshot", atClusterTime: <Timestamp> }`. It gives a consistent view across several queries, for example for a report or export, without a transaction. The time must be within the snapshot history window.

```javascript
db.runCommand({
  find: "orders",
  filter: { status: "paid" },
  readConcern: { level: "snapshot", atClusterTime: Timestamp(1761200000, 1) },
});
```

### 327: What are the trade-offs of `w: "majority"`?

Pros:

- Acknowledged writes will not be rolled back.
- Works with causal consistency and majority reads.

Cons:

- Higher latency, because you wait for replication.
- If a majority of data members is not reachable, writes wait until `wtimeout` or never return.

### 328: What happens to majority writes when a secondary goes down in a PSA set?

In a Primary-Secondary-Arbiter set, the majority of voters is 2, but there are only 2 data-bearing members. If the secondary goes down, the primary stays primary (it has the arbiter's vote), but `w: "majority"` writes cannot be acknowledged. Also, the majority commit point stops moving, so the WiredTiger cache fills with history and performance drops. That is why PSS is preferred over PSA.

### 329: What is `writeConcernMajorityJournalDefault`?

It is a replica set setting. When `true` (the default), `w: "majority"` waits for the write to be in the journal on a majority of members. Setting it to `false` is risky because a power failure on several members could lose majority acknowledged writes.

### 330: How does Raft relate to MongoDB elections?

MongoDB's replication protocol (protocol version 1, `pv1`) is based on Raft ideas. It uses terms (election numbers), a majority vote, and checks that the candidate's oplog is at least as up to date as the voter's. Each node votes at most once per term. This avoids two primaries accepting majority writes at the same time.

### 331: Can there be two primaries at the same time?

For a short time, yes. If an old primary is cut off from the network, it may not know yet that a new primary was elected. It will step down once it notices it cannot reach a majority. Writes it accepts in that window cannot reach majority and will be rolled back. Using `w: "majority"` and `readConcern: "majority"` (or `linearizable`) protects you from acting on this stale primary.

### 332: What are `priority` and `votes` in a replica set config?

- `priority`: how likely the member is to become primary. `0` means it can never be primary.
- `votes`: `1` or `0`. Only up to 7 members can vote.

A member with `votes: 0` must also have `priority: 0`.

### 333: What is chained replication?

Secondaries can sync from other secondaries instead of the primary, to reduce load on the primary or save cross-datacenter bandwidth. It is enabled by default. You can disable it with `settings.chainingAllowed: false`. You can see a member's sync source in `rs.status()` (`syncSourceHost`).

### 334: How do you design a replica set across data centers?

- Put members in at least three locations so a single data center outage does not lose the majority (for example 2 + 2 + 1).
- Give higher priority to members in the main data center.
- Use tags and read preference tags to read from nearby members.
- Use `w: "majority"` and consider tag-based custom write concerns to make sure data reaches more than one site.

```javascript
cfg.settings.getLastErrorModes = { multiDC: { dc: 2 } };
// write with { w: "multiDC" }
```

### 335: What are read preference tags and `maxStalenessSeconds`?

Tags let you send reads to specific members (for example `{ dc: "eu" }`). `maxStalenessSeconds` (at least 90) stops reads from going to secondaries that are too far behind.

```text
mongodb://h1,h2,h3/?replicaSet=rs0&readPreference=secondary&readPreferenceTags=dc:eu&maxStalenessSeconds=120
```

### 336: What is hedged reads?

Hedged reads send a read with `nearest` preference to two members at once and use the first answer, to reduce tail latency in sharded clusters. They are deprecated in 8.0, so do not build new designs on them.

### 337: What is mirrored reads?

The primary sends a sample of the reads it receives to electable secondaries (default 1%) so that their caches stay warm. After a failover, the new primary already has hot data in memory. It is configured with `mirrorReads`.

### 338: How does resharding work?

`reshardCollection` (5.0+) changes the shard key while the application keeps working. MongoDB creates a new hidden collection with the new shard key, copies all data, applies ongoing changes from the oplog, and when it is nearly caught up, blocks writes briefly (about 2 seconds by default) to switch over. In 8.0 resharding is much faster because it can copy data in parallel.

```javascript
db.adminCommand({
  reshardCollection: "shop.orders",
  key: { customerId: 1, orderId: 1 },
});
```

You need enough free storage (about 1.2x the collection) on the shards during resharding.

### 339: What is refining a shard key?

`refineCollectionShardKey` (4.4+) adds fields to the end of an existing shard key. It is quick because it only changes metadata. It helps when the current key has low cardinality and causes jumbo chunks.

```javascript
db.adminCommand({
  refineCollectionShardKey: "shop.orders",
  key: { customerId: 1, orderId: 1 },
});
```

You need an index that supports the new key first.

### 340: How do you analyze a candidate shard key?

Since 7.0 you can use `analyzeShardKey` and `configureQueryAnalyzer`. They report cardinality, frequency, monotonicity and, with sampled queries, how many queries would be targeted.

```javascript
db.adminCommand({
  configureQueryAnalyzer: "shop.orders",
  mode: "full",
  samplesPerSecond: 10,
});

db.adminCommand({
  analyzeShardKey: "shop.orders",
  key: { customerId: 1 },
  keyCharacteristics: true,
  readWriteDistribution: true,
});
```

### 341: What are `moveCollection` and `unshardCollection` in 8.0?

- `moveCollection` moves an unsharded collection from one shard to another without downtime.
- `unshardCollection` turns a sharded collection back into an unsharded collection on one shard.

```javascript
db.adminCommand({ moveCollection: "shop.settings", toShard: "shard02" });
db.adminCommand({ unshardCollection: "shop.audit", toShard: "shard01" });
```

Before 8.0 an unsharded collection always lived on its database's primary shard. Now you can place it where you want.

### 342: What is the primary shard of a database?

Each database has a primary shard that holds its unsharded collections by default. You can change it with `movePrimary`. In 8.0 you can also move individual unsharded collections with `moveCollection`, which gives more control.

### 343: What are orphaned documents?

Orphaned documents are copies of documents left on a shard after a chunk migration failed or before cleanup ran. Reads through `mongos` with normal read concerns filter them out. Since 6.0, the range deleter cleans them up automatically, and the old `cleanupOrphaned` command is no longer needed.

### 344: How does a chunk migration work?

1. The balancer picks a chunk (range) to move.
2. The destination shard copies the documents from the source.
3. Changes made during the copy are sent and applied.
4. A short critical section blocks writes to that range, the last changes are applied, and the config server metadata is updated.
5. The source shard deletes the old documents (range deletion) after open queries finish.

### 345: How does `mongos` know where data lives?

`mongos` caches the routing table (chunk ranges to shards) from the config servers. Each request includes a shard version. If a shard sees that the `mongos` has an old version, it returns a stale config error and `mongos` refreshes its cache and retries.

### 346: How do you handle a monotonically increasing shard key like a timestamp?

All new inserts go to the chunk with the highest range, which lives on one shard (a hot shard). Options:

- Use a hashed shard key on the field: `{ createdAt: "hashed" }`.
- Use a compound key with a well distributed first field: `{ tenantId: 1, createdAt: 1 }`.
- Pre-split data for an initial load using `numInitialChunks` (hashed) or `presplitHashedZones`.

### 347: What are the downsides of a hashed shard key?

- Range queries on that field go to all shards (scatter-gather).
- Sorting by the field is not targeted.
- You lose data locality for related documents.

Compound hashed shard keys (4.4+) like `{ country: 1, userId: "hashed" }` help keep some locality.

### 348: What is a sharded time series collection?

Time series collections can be sharded (5.1+). The shard key must use the `metaField` (or its subfields) and optionally the `timeField`. MongoDB shards the internal buckets collection.

```javascript
sh.shardCollection("iot.readings", { "sensor.id": 1, ts: 1 }, false, {
  timeseries: { timeField: "ts", metaField: "sensor", granularity: "seconds" },
});
```

### 349: What is the `$shardedDataDistribution` stage?

It returns how much data each sharded collection has on each shard, which helps check balance.

```javascript
db.getSiblingDB("admin").aggregate([{ $shardedDataDistribution: {} }]);
```

`sh.status()` and `db.collection.getShardDistribution()` give similar information.

### 350: What is a config shard?

From 8.0, a config server replica set can also act as a shard and store application data. This is useful for small clusters where you do not want a separate set of three servers just for metadata. You can switch with `transitionFromDedicatedConfigServer` and back with `transitionToDedicatedConfigServer`.

### 351: How do you design a multi-tenant application in MongoDB?

Common options:

1. Database per tenant: strong isolation and easy per-tenant backup, but thousands of databases mean many files and more overhead.
2. Collection per tenant: similar issues with very many collections.
3. Shared collections with a `tenantId` field: scales best. Put `tenantId` first in every index and use it as the first field of the shard key.

```javascript
db.orders.createIndex({ tenantId: 1, createdAt: -1 });
sh.shardCollection("app.orders", { tenantId: 1, _id: 1 });
```

With option 3, the application must always filter by `tenantId`. A wrapper in the data access layer or a view per tenant helps prevent mistakes.

### 352: How many collections and indexes can MongoDB handle?

There is no hard limit, but each collection and index is a WiredTiger file (table), which uses file handles and memory. Tens of thousands of collections and indexes on one node can slow startup, checkpoints and the cache. As a rule of thumb, keep the total below roughly 10,000 per replica set and prefer shared collections with a tenant field. A collection can have at most 64 indexes.

### 353: How do you handle a document that keeps growing?

Unbounded growth (for example pushing every comment into a post) leads to big documents, slower updates and eventually the 16 MB limit. Fixes:

- Move the growing part into its own collection with a reference.
- Use the bucket pattern (one document per N items or per time period).
- Keep a capped recent list with `$push` + `$slice` and store the full history elsewhere.

### 354: What happens internally when you update a document in WiredTiger?

WiredTiger does not update the document in place on disk. It writes a new version in the in-memory B-tree page as an update structure. Later, during eviction or a checkpoint, the page is reconciled and written to a new location on disk. This is why small updates to very large documents are expensive: the whole document is rewritten at reconciliation. For the oplog, MongoDB writes a diff (delta) of the change for many updates (since 5.0), which keeps oplog entries small.

### 355: What is WiredTiger cache eviction, and what are signs of trouble?

When the cache fills to about 80%, background eviction threads write dirty pages out and remove clean pages. If usage goes above 95% (or dirty data above 20%), application threads are forced to help with eviction, which causes latency spikes. Signs:

- `wiredTiger.cache["bytes currently in the cache"]` close to the maximum
- high "pages evicted by application threads"
- high dirty cache percentage

Fixes include more RAM, fewer or smaller indexes, shorter transactions and less write load.

### 356: What is a checkpoint in WiredTiger?

A checkpoint writes a consistent snapshot of all data to disk, by default every 60 seconds. After a crash, MongoDB recovers from the last checkpoint and then replays the journal. Large checkpoints can cause I/O spikes, which you see as periodic latency increases.

### 357: What is the `storageEngine` `directoryPerDB` and `directoryForIndexes`?

- `directoryPerDB: true` stores each database's files in its own folder.
- `wiredTiger.engineConfig.directoryForIndexes: true` stores indexes in a separate folder from collection data.

They let you put data and indexes on different volumes. They must be set when the data directory is created.

### 358: How do you size the oplog?

The oplog should cover enough time for maintenance and for a secondary to recover after downtime, usually at least 24 to 72 hours. Look at `rs.printReplicationInfo()` for the current window. Resize without restart:

```javascript
db.adminCommand({ replSetResizeOplog: 1, size: 51200 }); // MB
db.adminCommand({ replSetResizeOplog: 1, minRetentionHours: 48 });
```

`minRetentionHours` (4.4+) keeps entries for at least that time even if the size limit is reached.

### 359: Which operations produce many oplog entries?

- `updateMany` and `deleteMany` produce one oplog entry per document changed.
- Large `insertMany` produces one entry per document (batched in applyOps for transactions).
- Updates that use `$set` on arrays in big documents can produce large diffs.

Massive multi-updates can shrink the oplog window quickly and cause replication lag. Batch them and throttle when running big migrations.

### 360: How do you safely run a large data migration on a live cluster?

- Process documents in batches (for example 1,000 at a time by `_id` ranges).
- Use `bulkWrite` with `ordered: false`.
- Watch replication lag and cache usage between batches and pause if needed.
- Use `w: "majority"` so you do not overload secondaries.
- Make the code idempotent so it can be restarted.

```javascript
let lastId = MinKey;
while (true) {
  const batch = db.users
    .find({ _id: { $gt: lastId }, v: { $ne: 2 } })
    .sort({ _id: 1 })
    .limit(1000)
    .toArray();
  if (!batch.length) break;
  db.users.bulkWrite(
    batch.map((d) => ({
      updateOne: {
        filter: { _id: d._id },
        update: [
          { $set: { fullName: { $concat: ["$first", " ", "$last"] }, v: 2 } },
        ],
      },
    })),
    { ordered: false, writeConcern: { w: "majority" } },
  );
  lastId = batch.at(-1)._id;
}
```

### 361: What does `$changeStreamSplitLargeEvent` do?

Change events have the same 16 MB limit as documents. If pre and post images make an event too large, the stream fails. The `$changeStreamSplitLargeEvent` stage (7.0+) splits big events into fragments that you join in your application.

```javascript
const stream = coll.watch([{ $changeStreamSplitLargeEvent: {} }], {
  fullDocument: "required",
});
```

### 362: How do you scale change stream consumers?

- Use one stream per collection or a filtered `$match` per consumer.
- Store the resume token after each processed event, ideally in the same transaction as the side effect, or make processing idempotent.
- On sharded clusters, `mongos` merges events from all shards in order, which adds latency. Shards that receive no writes still send no-op entries every few seconds to keep things moving.
- For very high volume, use the MongoDB Kafka connector or Atlas Stream Processing.

### 363: What are the guarantees of change streams?

- Events are delivered in the order they were applied to the cluster.
- Only majority-committed changes are returned, so they will not be rolled back.
- A stream can be resumed with a resume token as long as the token is still in the oplog.
- Change events from a multi-document transaction contain `txnNumber` and `lsid`, and all events in it are delivered together.

### 364: What is Atlas Stream Processing?

It is a service that runs continuous aggregation pipelines over streaming data from Kafka or change streams. You can use windows (`$tumblingWindow`, `$hoppingWindow`), validate data and write results with `$merge` or `$emit` to Kafka. It uses the same aggregation syntax you already know.

### 365: How do you implement an outbox pattern in MongoDB?

Write the business change and an event document in the same transaction, then a separate process reads the outbox (via a change stream or polling) and publishes to the message broker.

```javascript
await session.withTransaction(async () => {
  await orders.insertOne(order, { session });
  await outbox.insertOne(
    { type: "OrderCreated", payload: order, createdAt: new Date() },
    { session },
  );
});
```

Often you can skip the outbox and use a change stream on `orders` directly, since change streams are already a durable ordered log.

### 366: How do you implement optimistic concurrency control?

Add a version field and include it in the update filter.

```javascript
const doc = await coll.findOne({ _id: id });
const res = await coll.updateOne(
  { _id: id, version: doc.version },
  { $set: { status: "approved" }, $inc: { version: 1 } },
);
if (res.matchedCount === 0)
  throw new Error("Document was changed by someone else");
```

Mongoose supports this with `optimisticConcurrency: true`.

### 367: How do you implement a reliable job queue in MongoDB?

Use `findOneAndUpdate` to atomically claim a job, with a lease time so crashed workers do not keep jobs forever.

```javascript
const job = await jobs.findOneAndUpdate(
  {
    $or: [
      { status: "ready" },
      { status: "running", leaseUntil: { $lt: new Date() } },
    ],
  },
  {
    $set: {
      status: "running",
      leaseUntil: new Date(Date.now() + 60000),
      worker: workerId,
    },
  },
  { sort: { priority: -1, createdAt: 1 }, returnDocument: "after" },
);
```

Index `{ status: 1, priority: -1, createdAt: 1 }` and `{ status: 1, leaseUntil: 1 }`.

### 368: How do you make an idempotent upsert under concurrency?

Two concurrent upserts with the same filter can both insert, unless there is a unique index on the filter fields. With a unique index, one of them gets a duplicate key error and the server retries it as an update automatically in many cases (since 4.2). Always back upserts with a unique index.

```javascript
db.dailyStats.createIndex({ userId: 1, day: 1 }, { unique: true });
db.dailyStats.updateOne(
  { userId: 7, day: "2026-10-23" },
  { $inc: { clicks: 1 } },
  { upsert: true },
);
```

### 369: How do you implement soft deletes properly?

Add an `isDeleted` flag (and a `deletedAt` date), filter on it everywhere, and use partial indexes so deleted documents do not take space in the indexes used by normal queries.

```javascript
db.users.updateOne(
  { _id: id },
  { $set: { isDeleted: true, deletedAt: new Date() } },
);

db.users.createIndex(
  { email: 1 },
  { unique: true, partialFilterExpression: { isDeleted: false } },
);
db.users.find({ email: "a@b.com", isDeleted: false }); // uses the partial index
```

New documents must be inserted with `isDeleted: false`, otherwise they are not in the index.

You can also add a TTL index on `deletedAt` to purge them later.

### 370: How do you model hierarchical data (trees)?

Common patterns:

- Parent reference: `{ _id: "mongodb", parent: "databases" }`. Easy to update, use `$graphLookup` for subtrees.
- Child references: `{ _id: "databases", children: ["mongodb", "postgres"] }`.
- Array of ancestors: `{ _id: "mongodb", ancestors: ["root", "tech", "databases"], parent: "databases" }`. Fast to find all descendants with an index on `ancestors`.
- Materialized path: `{ _id: "mongodb", path: ",root,tech,databases," }`. Query with a prefix regex.

```javascript
db.categories.find({ ancestors: "tech" }); // all under tech
db.categories.find({ path: /^,root,tech,/ }); // same with path
```

### 371: How do you store and query versioned documents (history)?

Common approaches:

- Keep the current version in the main collection and copy the old version into a `history` collection on each change (in a transaction or using change streams with pre-images).
- Store each version as a separate document with `{ docId, version, validFrom, validTo }` and index `{ docId: 1, version: -1 }`.

The first keeps reads of the current state simple and fast.

### 372: How do you handle large arrays and index size?

Each array element in an indexed field creates an index key. A document with 10,000 tags creates 10,000 index entries, and every update to the array may update many keys. Keep indexed arrays small, or move items into separate documents.

### 373: What is the difference between `$lookup` and application-side joins in terms of performance?

`$lookup` runs on the server, saves round trips and can use indexes on the foreign collection. Application-side joins (two queries, then merge in code) can be faster when the second query is a single `$in` on an indexed field, and when results can be cached. In a sharded cluster, `$lookup` may need to talk to many shards. Measure both for hot paths, but for most cases embedding or the extended reference pattern avoids the join entirely.

### 374: How do you query documents by a field inside an array of objects and return only matching elements?

Use `$filter` in an aggregation (the projection `$elemMatch` returns only the first match).

```javascript
db.orders.aggregate([
  { $match: { "items.sku": "A1" } },
  {
    $project: {
      items: {
        $filter: {
          input: "$items",
          as: "it",
          cond: { $eq: ["$$it.sku", "A1"] },
        },
      },
    },
  },
]);
```

### 375: How do you write a recursive aggregation with limited depth and filters?

`$graphLookup` supports `maxDepth`, `depthField` and `restrictSearchWithMatch`.

```javascript
db.users.aggregate([
  { $match: { _id: "ann" } },
  {
    $graphLookup: {
      from: "users",
      startWith: "$follows",
      connectFromField: "follows",
      connectToField: "_id",
      as: "network",
      maxDepth: 2,
      depthField: "level",
      restrictSearchWithMatch: { active: true },
    },
  },
]);
```

`$graphLookup` must fit in 100 MB of memory unless `allowDiskUse` is on, and it does not use indexes as well as `$lookup`. Index `connectToField`.

### 376: How do you fill gaps in time series data?

Use `$densify` to create missing time points and `$fill` to fill values.

```javascript
db.readings.aggregate([
  { $match: { sensorId: 7 } },
  {
    $densify: {
      field: "ts",
      range: { step: 1, unit: "minute", bounds: "full" },
    },
  },
  {
    $fill: {
      sortBy: { ts: 1 },
      output: { value: { method: "linear" }, sensorId: { value: 7 } },
    },
  },
]);
```

### 377: How do you compute a moving average?

```javascript
db.prices.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$symbol",
      sortBy: { date: 1 },
      output: {
        ma7: { $avg: "$close", window: { range: [-6, 0], unit: "day" } },
      },
    },
  },
]);
```

You can also use `$expMovingAvg` for an exponential moving average.

### 378: How do you compute differences between consecutive documents?

Use `$shift` in `$setWindowFields`.

```javascript
db.meter.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$meterId",
      sortBy: { ts: 1 },
      output: { prev: { $shift: { output: "$reading", by: -1 } } },
    },
  },
  {
    $set: {
      usage: { $subtract: ["$reading", { $ifNull: ["$prev", "$reading"] }] },
    },
  },
]);
```

`$derivative` and `$integral` are also available for rate calculations.

### 379: How do aggregation pipelines run in a sharded cluster?

`mongos` splits the pipeline into a shard part and a merge part. Stages like `$match`, `$project` and partial `$group` run on each shard in parallel. The results are sent to a merging node (`mongos` or a shard) which runs the rest (for example the final `$group` combine and `$sort`). Explain shows `splitPipeline` with `shardsPart` and `mergerPart`. Putting `$match` on the shard key first lets `mongos` target only the needed shards.

### 380: What is `$documents`?

`$documents` (5.1+) starts a pipeline from literal documents instead of a collection. It is useful for testing and for joining against a fixed list.

```javascript
db.aggregate([
  { $documents: [{ sku: "A1" }, { sku: "B2" }] },
  {
    $lookup: {
      from: "products",
      localField: "sku",
      foreignField: "sku",
      as: "p",
    },
  },
]);
```

### 381: How do you use `$$NOW`, `$$ROOT`, `$$CURRENT` and `$$REMOVE`?

- `$$NOW`: current time, same for the whole operation.
- `$$ROOT`: the whole top-level document.
- `$$CURRENT`: the current document (same as `$$ROOT` unless changed).
- `$$REMOVE`: removes a field when used as a value.

```javascript
db.users.updateMany({}, [
  {
    $set: {
      updatedAt: "$$NOW",
      nickname: {
        $cond: [{ $eq: ["$nickname", ""] }, "$$REMOVE", "$nickname"],
      },
    },
  },
]);
```

### 382: How do you pass variables to an aggregation without building strings?

Use the `let` option of `aggregate`, `find`, `update` and `delete` (5.0+). This avoids injection risks and keeps query shapes stable.

```javascript
db.orders.aggregate(
  [{ $match: { $expr: { $gte: ["$total", "$$minTotal"] } } }],
  { let: { minTotal: 100 } },
);
```

### 383: What is `$setUnion`, `$setIntersection` and `$setDifference`?

They treat arrays as sets.

```javascript
db.users.aggregate([
  {
    $project: {
      common: { $setIntersection: ["$skills", ["mongodb", "node"]] },
      missing: { $setDifference: [["mongodb", "node"], "$skills"] },
    },
  },
]);
```

### 384: How do you sort an array inside a document?

Use `$sortArray` (5.2+).

```javascript
db.teams.aggregate([
  {
    $project: {
      players: { $sortArray: { input: "$players", sortBy: { score: -1 } } },
    },
  },
]);
```

### 385: How do you do a full outer join in MongoDB?

There is no direct operator. Combine two `$lookup` passes with `$unionWith` and then group.

```javascript
db.a.aggregate([
  { $project: { key: 1, aVal: "$val" } },
  {
    $unionWith: {
      coll: "b",
      pipeline: [{ $project: { key: 1, bVal: "$val" } }],
    },
  },
  { $group: { _id: "$key", aVal: { $max: "$aVal" }, bVal: { $max: "$bVal" } } },
]);
```

### 386: What is the difference between `$group` + `$push: "$$ROOT"` and `$topN`?

`$push: "$$ROOT"` keeps every document in memory for each group, which can exceed 100 MB or the 16 MB result limit. `$topN`, `$firstN` and `$maxN` keep only N documents per group, so memory stays small.

### 387: How do you handle the 16 MB limit in aggregation results?

The 16 MB limit applies to each output document, not to the whole result, because results come back as a cursor. Problems happen when a stage builds one huge document (for example `$group` with `$push` of everything, or `$facet`). Keep arrays bounded, use `$limit` inside `$facet`, or write to a collection with `$merge`.

### 388: What is `$expr` performance like with indexes?

`$expr` can use indexes for `$eq`, `$lt`, `$lte`, `$gt` and `$gte` when comparing a field with a constant or variable. It cannot use an index when comparing two fields of the same document. For such cases, store the result of the comparison in a field and index that.

### 389: What does `$regex` do with an index?

A case-sensitive prefix regex like `/^abc/` turns into a range scan on the index and is efficient. A regex with `i`, no anchor, or a pattern like `/^.*abc/` must scan all index keys. For "contains" search use Atlas Search (or `mongot`) instead of regex.

### 390: How does the `$or` query get optimized?

Each `$or` clause is planned on its own, and results are combined (`OR` stage) and deduplicated. If even one clause has no index, the whole query becomes a collection scan. Sometimes rewriting `$or` on the same field as `$in` is faster. With a sort, MongoDB may use `SORT_MERGE` across clauses if each clause has an index on the sort.

### 391: What is the `$jsonSchema` `additionalProperties: false` gotcha?

If you set `additionalProperties: false`, you must list `_id` in `properties`, or every insert fails because `_id` is not allowed.

```javascript
{
  $jsonSchema: {
    bsonType: "object",
    additionalProperties: false,
    properties: { _id: { bsonType: "objectId" }, name: { bsonType: "string" } }
  }
}
```

### 392: How do you get details of why a document failed validation?

Since 5.0, the error contains `errInfo.details` with the rules that failed.

```javascript
try {
  db.users.insertOne({ name: 5 });
} catch (e) {
  printjson(e.errInfo.details);
}
```

### 393: How do you enforce relationships (like foreign keys)?

MongoDB does not have foreign key constraints. Options:

- Check references in application code or in a transaction.
- Use `$lookup` in periodic jobs to find orphaned references.
- Design to embed when the data belongs together.
- Use change streams to clean up related data when a parent is deleted.

### 394: How do you encrypt a field with CSFLE in Node.js?

```javascript
import { MongoClient } from "mongodb";

const kmsProviders = { local: { key: localMasterKey } }; // 96-byte key
const client = new MongoClient(uri, {
  autoEncryption: {
    keyVaultNamespace: "encryption.__keyVault",
    kmsProviders,
    schemaMap: {
      "hr.employees": {
        bsonType: "object",
        encryptMetadata: { keyId: [dataKeyId] },
        properties: {
          ssn: {
            encrypt: {
              bsonType: "string",
              algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
            },
          },
        },
      },
    },
  },
});
```

You need the `mongodb-client-encryption` package and the Automatic Encryption Shared Library (`crypt_shared`) for automatic encryption. In production, use a cloud KMS, not a local key.

### 395: How is Queryable Encryption different from CSFLE?

- CSFLE deterministic encryption gives the same ciphertext for the same value, which can leak frequency info. Queryable Encryption uses randomized encryption.
- Queryable Encryption supports equality and range queries, with more query types being added. CSFLE supports only equality on deterministic fields.
- Queryable Encryption stores extra metadata (`__safeContent__` field and metadata collections), so it uses more storage.
- Encrypted fields for Queryable Encryption are defined when the collection is created (`encryptedFields`).

### 396: What is the principle of least privilege in MongoDB, with an example?

Give each application or user only the actions they need on the resources they need.

```javascript
db.getSiblingDB("admin").createRole({
  role: "orderService",
  privileges: [
    {
      resource: { db: "shop", collection: "orders" },
      actions: ["find", "insert", "update"],
    },
    { resource: { db: "shop", collection: "products" }, actions: ["find"] },
  ],
  roles: [],
});
```

Do not use `root` or `dbOwner` for applications.

### 397: How do you rotate keys and passwords without downtime?

- Users: `db.changeUserPassword()` or create a new user, deploy the app with new credentials, then drop the old user.
- Keyfile internal auth: a keyfile can hold several keys. Add the new key to every member, restart them one by one, then remove the old key and do another rolling restart.
- X.509: use `tlsClusterCAFile` and the rolling certificate update process (`net.tls.clusterAuthX509` in 7.0+).
- CSFLE/QE data keys: use `rewrapManyDataKey` to re-encrypt data keys with a new master key.

### 398: What security checklist would you follow for a self-managed deployment?

- Enable authentication and role-based access control.
- Use TLS for all traffic.
- Bind only to private interfaces and use firewalls or security groups.
- Use keyfiles or X.509 for internal member authentication.
- Encrypt data at rest.
- Turn on auditing (Enterprise).
- Disable server-side JavaScript if not needed (`security.javascriptEnabled: false`).
- Run `mongod` as a non-root user.
- Keep MongoDB updated with patch releases.

### 399: What is `setParameter` and `setClusterParameter`?

`setParameter` changes server options on one node at runtime. `setClusterParameter` (6.0+) sets parameters for the whole cluster, stored in the config and replicated.

```javascript
db.adminCommand({ setParameter: 1, logLevel: 1 });
db.adminCommand({
  setClusterParameter: { defaultMaxTimeMS: { readOperations: 5000 } },
});
db.adminCommand({ getClusterParameter: "defaultMaxTimeMS" });
```

### 400: How do you control log verbosity per component?

```javascript
db.setLogLevel(2, "query");
db.setLogLevel(0); // back to default
db.getLogComponents();
```

Or in the config file:

```yaml
systemLog:
  component:
    query:
      verbosity: 1
```

`slowms` and `slowOpSampleRate` control what slow operations get logged.

### 401: What metrics would you monitor in production?

- Operation latency and throughput (`opLatencies`, `opcounters`)
- Replication lag and oplog window
- WiredTiger cache usage, dirty percentage, application-thread eviction
- Queued operations and ticket usage
- Connections (current, available, created per second)
- Disk I/O, disk space, CPU, memory
- Page faults
- Slow queries, collection scans (`metrics.queryExecutor.scanned` vs `scannedObjects`)
- Election and failover events

Tools: Atlas monitoring, Ops Manager, `mongostat`, `mongotop`, or Prometheus with an exporter and Grafana.

### 402: What are `mongostat` and `mongotop`?

- `mongostat` shows a live summary of server activity every second: inserts, queries, updates, deletes, connections, cache usage.
- `mongotop` shows how much time the server spends reading and writing each collection.

```bash
mongostat --uri="mongodb://admin@host:27017/?authSource=admin" 5
mongotop --uri="mongodb://admin@host:27017/?authSource=admin" 10
```

### 403: What causes a sudden spike in connections, and how do you fix it?

Common causes:

- Application creating a new `MongoClient` per request.
- Too many app instances, each with a large `maxPoolSize`.
- A slow database making the pools grow as requests wait.
- Serverless functions opening new clients on each cold start.

Fix: share one client per process, set sensible pool sizes, use `maxConnecting`, cache the client outside the handler in serverless code, and fix the slow queries that cause waiting.

### 404: How do you troubleshoot high CPU on a MongoDB server?

1. Check `db.currentOp()` for long running operations.
2. Look at the slow query log or profiler for `COLLSCAN` and high `keysExamined`/`docsExamined`.
3. Check for inefficient regex, large `$in`, or aggregations without a leading `$match`.
4. Check for heavy index builds or many connections being opened.
5. Look at `serverStatus().wiredTiger.cache` for eviction pressure.
6. Add or fix indexes, then verify with `explain("executionStats")`.

### 405: How do you troubleshoot replication lag?

- Check if the secondary has weaker hardware or a slower disk.
- Check network latency between members.
- Look for large write bursts (`updateMany`, bulk loads) on the primary.
- Check if the secondary is serving heavy reads.
- Check for missing indexes on the secondary (updates and deletes by non-`_id` fields need them).
- Check flow control (`serverStatus().flowControl`), which slows the primary when majority lag grows.

### 406: What is flow control?

Flow control (4.2+) slows down writes on the primary when majority-committed data falls too far behind (default target is 10 seconds of lag). It keeps the majority commit point from falling too far behind, which protects the cache from filling with history. You can see it in `serverStatus().flowControl` and tune it with `flowControlTargetLagSeconds`.

### 407: What is the effect of a long-running query on a secondary?

Long-running reads on a secondary keep an old snapshot open. WiredTiger must keep old versions in the cache, which increases cache pressure. In older versions this could also block oplog application. Use `maxTimeMS` on analytics queries or run them on a dedicated analytics node (hidden member or Atlas analytics node).

### 408: What happens during a failover from the application's point of view?

1. The primary becomes unavailable. Writes fail with network errors or `NotWritablePrimary`.
2. The driver marks the server as unknown and starts server selection.
3. An election takes a few seconds (usually under 12 seconds with default settings).
4. Retryable writes and reads are retried once on the new primary.
5. Operations that cannot be retried (for example non-idempotent multi-updates) return an error and the app must decide what to do.

### 409: Why are `updateMany` and `deleteMany` not retryable?

A retryable write needs the server to remember whether it already applied the operation. That works for single-document writes. Multi-document writes can be partly applied before a failover, so retrying blindly could change the result. Since 6.1 some cases are handled better, but in general you should design multi-updates to be idempotent (for example with a filter that excludes already-updated documents).

### 410: How do you design for zero-downtime schema changes?

- Make the application read both old and new formats.
- Write the new format for new data.
- Migrate old documents in background batches.
- Add validation or new indexes only after the migration is done.
- Remove support for the old format in a later release.

The schema versioning pattern (a `schemaVersion` field) makes this easier.

### 411: How do you test a MongoDB-based application?

- Use a real MongoDB in tests (Docker, Testcontainers or `mongodb-memory-server`), not a mock, so query behavior is real.
- Start it as a single-node replica set if you test transactions or change streams.
- Seed data per test and drop the database after.
- Test indexes with `explain()` assertions for critical queries.

```bash
docker run -d -p 27017:27017 mongo:8.0 --replSet rs0
docker exec -it <container> mongosh --eval "rs.initiate()"
```

### 412: What is the Atlas Local deployment?

The Atlas CLI can run a local Atlas deployment in Docker (`atlas deployments setup --type local`). It includes `mongod` and `mongot`, so you can develop Atlas Search and Vector Search locally. The `mongodb/mongodb-atlas-local` Docker image does the same.

### 413: How does `$out` behave with indexes and concurrent readers?

`$out` writes to a temporary collection and renames it over the target at the end. Existing indexes on the target are kept (rebuilt on the new data) and readers see either the old or the new collection, never half of it. If the pipeline fails, the target is unchanged. It cannot write to a sharded collection, and it cannot be used inside a transaction.

### 414: How does `$merge` behave on failure?

`$merge` writes documents as it goes. If it fails halfway, some documents are already written. It is not atomic across documents. Design it to be safe to re-run (for example `whenMatched: "replace"` or a merge that produces the same result again).

### 415: How do you build a near real-time materialized view?

Combine an initial `$merge` job with a change stream or a scheduled incremental `$merge` that processes only new data (filter by `updatedAt` or `_id`). Atlas Triggers or Atlas Stream Processing can automate this. Store a watermark (last processed time) in a separate collection.

### 416: How do you calculate distinct counts at scale?

`distinct` returns all values in one 16 MB document, so it fails for many values. Use an aggregation:

```javascript
db.events.aggregate([
  { $match: { day: "2026-10-23" } },
  { $group: { _id: "$userId" } },
  { $count: "uniqueUsers" },
]);
```

For very large data, store per-period unique sets in buckets or use approximate methods in your analytics tool.

### 417: What is the `$queryStats` stage?

`$queryStats` (Atlas, 7.1+) returns runtime statistics per query shape: how often it ran, latency, documents examined and returned. It helps find the most expensive query shapes across the cluster.

```javascript
db.getSiblingDB("admin").aggregate([
  { $queryStats: {} },
  { $sort: { "metrics.totalExecMicros.sum": -1 } },
  { $limit: 10 },
]);
```

### 418: What is Performance Advisor in Atlas?

It looks at slow queries and suggests indexes that would help, and indexes that are unused or redundant. It also has schema suggestions, like reducing array sizes or document size. It is a good starting point, but you still need to check the suggestions against your write load.

### 419: What are Atlas cluster tiers and auto-scaling?

Atlas has tiers (M0 free, Flex, and dedicated M10 and up) with different CPU, RAM and storage. Auto-scaling can increase or decrease the cluster tier and storage based on usage. There are also independent shard scaling and different tiers for analytics nodes. Scaling up a tier is a rolling process with no downtime.

### 420: What is Online Archive and Atlas Data Federation?

- Online Archive moves older data from a cluster to cheaper object storage automatically based on a date field, and you can still query it.
- Atlas Data Federation lets you query data across Atlas clusters, S3 buckets and HTTP sources with the MongoDB query language, as if it were one database.

### 421: What is the oplog entry for a multi-document transaction?

A committed transaction is written as an `applyOps` oplog entry (or several linked entries for large transactions) containing all operations. Secondaries apply the whole transaction together, so readers on secondaries do not see a half-applied transaction. Large transactions are split into multiple oplog entries since 4.2, which removed the old 16 MB total limit for transactions.

### 422: How does MongoDB guarantee durability with `w: "majority"` and `j: true`?

A write is in the primary's journal and has been replicated to and journaled on a majority of voting members before it is acknowledged. Even if the primary crashes right after, the new primary (which must have the latest majority data) will have the write.

### 423: What is the majority commit point?

It is the latest oplog time that a majority of members have replicated. Reads with `readConcern: "majority"` return data as of this point. WiredTiger must keep history from this point forward in the cache, which is why a stuck commit point (like in a PSA set with a down secondary) is a problem.

### 424: What happens if you read from a secondary without majority read concern?

You might read data that was later rolled back, and data may be behind the primary. Your own recent writes might not be visible. For most apps that read from secondaries, use `readConcern: "majority"` with causal consistency, or accept eventual consistency for things like analytics.

### 425: What is `linearizable` read concern, and when do you use it?

It guarantees that the read reflects all successful majority writes that completed before the read started, and that the node is still the real primary. It is used when you must not read stale data even during a network partition, such as reading a lock or leader record. It only works for reads that target a single document (by a unique filter) on the primary, and it is slow. Always use it with `maxTimeMS`.

### 426: How do sessions work, and what is `lsid`?

A logical session groups operations from a client, for retryable writes, causal consistency and transactions. Each session has an id (`lsid`). Drivers create implicit sessions for every operation if you do not start one. Sessions expire after 30 minutes of inactivity (`localLogicalSessionTimeoutMinutes`).

### 427: How can you trace a request from the app to the database log?

Use the `comment` option. It appears in the profiler, `currentOp` and slow query logs.

```javascript
await orders
  .find(
    { status: "paid" },
    { comment: { traceId: "a1b2c3", route: "/orders" } },
  )
  .toArray();
```

Many APM tools also hook into the driver's command monitoring events (`commandStarted`, `commandSucceeded`).

### 428: How does the driver discover and monitor servers (SDAM)?

The driver connects to the seed list, runs `hello` on each server and learns the topology (replica set members, `mongos` list). It keeps one monitoring connection per server, polls every `heartbeatFrequencyMS` (10 s), and in newer drivers uses streaming `hello` so it learns about a new primary almost immediately. Server selection then picks a server based on read preference and latency window (`localThresholdMS`).

### 429: What is load balancer mode in drivers?

When MongoDB runs behind a load balancer (for example Atlas serverless or Private Link to sharded clusters), drivers use `loadBalanced=true`. Each connection is pinned for cursors and transactions so that `getMore` and commit go to the same `mongos`.

### 430: What happens if a cursor times out in the middle of iteration?

The server closes idle cursors after 10 minutes (`cursorTimeoutMillis`). The next `getMore` fails with `CursorNotFound`. Fix it by processing faster, using a smaller `batchSize`, or restarting the iteration from the last processed `_id`. `noCursorTimeout` keeps a cursor open, but since 4.4.8 cursors in a session still expire with the session, so prefer resumable logic.

### 431: How does `estimatedDocumentCount()` differ from `countDocuments({})` internally?

- `estimatedDocumentCount()` reads the count from collection metadata. It is instant but can be wrong after an unclean shutdown and includes orphan documents on sharded clusters.
- `countDocuments()` runs an aggregation with `$match` and `$group`, so it is exact but scans an index or the collection.

### 432: How do you implement full text search with relevance and autocomplete in MongoDB?

Create a search index with `autocomplete` mapping and use `$search` with `compound`.

```javascript
db.products.createSearchIndex({
  name: "products_search",
  definition: {
    mappings: {
      dynamic: false,
      fields: {
        name: [
          { type: "string" },
          { type: "autocomplete", minGrams: 2, maxGrams: 15 },
        ],
        brand: { type: "token" },
      },
    },
  },
});

db.products.aggregate([
  {
    $search: {
      index: "products_search",
      compound: {
        must: [{ autocomplete: { query: "iph", path: "name" } }],
        filter: [{ equals: { path: "brand", value: "Apple" } }],
      },
    },
  },
  { $limit: 10 },
]);
```

### 433: How do you combine vector search and keyword search (hybrid search)?

Run `$vectorSearch` and `$search` and merge the results with reciprocal rank fusion. Newer versions provide `$rankFusion` (8.1+) and `$scoreFusion` to do this in one pipeline.

```javascript
db.docs.aggregate([
  {
    $rankFusion: {
      input: {
        pipelines: {
          vector: [
            {
              $vectorSearch: {
                index: "vec",
                path: "embedding",
                queryVector: qv,
                numCandidates: 200,
                limit: 50,
              },
            },
          ],
          text: [
            {
              $search: {
                index: "txt",
                text: { query: "mongodb sharding", path: "body" },
              },
            },
            { $limit: 50 },
          ],
        },
      },
    },
  },
  { $limit: 10 },
]);
```

### 434: What is vector quantization in vector search?

Quantization stores vectors in a smaller format (scalar `int8` or binary `int1`) to reduce memory and speed up search, with a small loss in accuracy. You set it in the index definition with `quantization: "scalar"` or `"binary"`, or store already quantized vectors as BSON `binData` vectors. Use rescoring with full-fidelity vectors when accuracy matters.

### 435: What are `numCandidates` and `limit` in `$vectorSearch`?

Vector search uses an approximate nearest neighbor (HNSW) algorithm. `numCandidates` is how many nearest candidates to consider, and `limit` is how many to return. A higher `numCandidates` (often 10 to 20 times `limit`) gives better recall but is slower. Set `exact: true` to do an exact (brute force) search, which is fine for small filtered sets.

### 436: What is the difference between `mongodump` and file system snapshots for large datasets?

`mongodump` reads all documents through the query layer, which is slow for large data, pollutes the cache, and needs index rebuilds on restore. Snapshots copy files at block level, are fast and include indexes, but need a consistent snapshot (journal on the same volume, or `fsyncLock`). For sharded clusters, consistent backups need coordinated snapshots, which Atlas, Ops Manager or Cloud Manager handle.

### 437: How do you restore to a point in time?

With continuous backup (Atlas, Ops Manager), choose a timestamp and restore. Self-managed, you can restore the last snapshot and then replay the oplog up to the time just before the bad operation.

```bash
mongorestore --oplogReplay --oplogLimit=1761200000:1 /backup/oplog-dump
```

### 438: How do you move data between clusters with minimum downtime?

- Atlas Live Migration (pull from self-managed into Atlas).
- `mongosync` (Cluster-to-Cluster Sync): continuous sync between two clusters, then cutover. Supports reverse sync and filtered sync.
- Initial `mongodump`/`mongorestore` plus change stream replication for smaller setups.

```bash
mongosync --cluster0 "mongodb://src..." --cluster1 "mongodb://dst..."
curl localhost:27182/api/v1/start -XPOST --data '{"source":"cluster0","destination":"cluster1"}'
```

### 439: What is the Relational Migrator?

It is a MongoDB tool that reads a relational schema (Postgres, MySQL, SQL Server, Oracle), helps you map tables to documents (embed or reference), migrates the data (snapshot or continuous with CDC) and can generate application code. It helps teams moving from SQL to MongoDB.

### 440: What is the difference between data modeling for reads vs writes?

Read-heavy workloads benefit from embedding and duplication so one query returns everything needed. Write-heavy workloads benefit from smaller documents, less duplication and fewer indexes, so each write touches less data. Most apps optimize for their most frequent operations, which is why MongoDB modeling starts from the queries, not from the entities.

### 441: How do you keep duplicated (denormalized) data in sync?

- Update all copies in a transaction when the source changes (if it is rare).
- Use change streams or Atlas Triggers to update copies asynchronously.
- Copy only fields that rarely change.
- Accept some staleness for non-critical data and fix with a periodic job.

### 442: Why is `_id` choice important for performance?

`_id` is always indexed and often the most used lookup key. A random `_id` (like UUIDv4) spreads inserts randomly across the B-tree, which uses more cache and causes more page splits than an increasing key like ObjectId. In sharded clusters, `_id` choice also matters if it is part of the shard key. Use ObjectId or time-ordered ids (like UUIDv7) when you can.

### 443: What is the impact of very large documents on performance?

- The whole document is loaded into cache even if you only need one field.
- Updates rewrite the whole document at reconciliation.
- Network transfer is larger (use projection to reduce it).
- Fewer documents fit in the cache.

Keep frequently accessed documents small and move rarely used large fields into separate collections (the subset pattern).

### 444: What are the main improvements in MongoDB 8.0?

- Large performance gains (faster reads, bulk inserts and replication) compared to 7.0.
- Queryable Encryption range queries.
- Query settings (`setQuerySettings`) for persistent index hints and rejecting queries.
- `moveCollection`, `unshardCollection` and faster resharding.
- Config shards.
- `updateOne`/`replaceOne` with `sort`.
- Cluster-wide multi-namespace `bulkWrite` command.
- Express query path for simple point lookups.
- `defaultMaxTimeMS` cluster parameter.
- `$toUUID` and `$convert` improvements.
- Server-side JavaScript (`$where`, `$function`, `$accumulator`) deprecated.

### 445: What are some notable features from 8.1 and 8.2?

These are rapid or minor releases after 8.0, mostly first on Atlas:

- `$rankFusion` and `$scoreFusion` for hybrid search.
- `validationAction: "errorAndLog"`.
- More Queryable Encryption query types (prefix, suffix, substring as preview).
- Search and Vector Search for self-managed Community and Enterprise through `mongot` (public preview in 8.2).
- New expressions and performance work in the query engine.

Always check the release notes for the exact version you run, because rapid release features may change.

### 446: What changed in the Node.js driver in recent major versions?

- v5 removed callbacks. Everything is Promise based.
- v6 changed `findOneAndUpdate`/`findOneAndDelete`/`findOneAndReplace` to return the document directly (not `{ value, ok }`) unless you pass `includeResultMetadata: true`.
- v6 requires a newer Node.js and the `bson` v6 package, and added client-level `bulkWrite` (6.10), `timeoutMS` (CSOT) and explicit resource management support.

```javascript
const doc = await users.findOneAndUpdate(
  { _id: id },
  { $set: { a: 1 } },
  { returnDocument: "after" },
);
// doc is the document or null
```

### 447: How would you debug "Sort exceeded memory limit" or `usedDisk` problems?

1. Run `explain` and find the `SORT` stage.
2. Create an index that matches the sort (and the equality filters before it, by the ESR rule).
3. If sorting after `$group`, reduce the number of groups or add `$limit` right after `$sort` so it becomes a top-N sort.
4. Project away big fields before the sort.
5. Only as a last resort rely on `allowDiskUse`, which is slower.

### 448: Explain a real case where an index made a query slower.

Example: a query `find({ status: "active" }).sort({ createdAt: -1 }).limit(20)` with indexes `{ status: 1 }` and `{ createdAt: -1 }`. The planner may pick `{ createdAt: -1 }` to avoid a sort, but if few documents are `active`, it scans most of the index to find 20 matches. With `{ status: 1 }` it would need a blocking sort on many documents. The right fix is a compound index `{ status: 1, createdAt: -1 }`. Also, the plan cache may lock in a bad plan when early trial results are not representative. Use `explain("allPlansExecution")` to see the competition between plans.

### 449: How would you design an order system that handles inventory correctly under concurrency?

- Use a conditional update so stock never goes negative, instead of read-then-write.

```javascript
const res = await products.updateOne(
  { _id: sku, stock: { $gte: qty } },
  { $inc: { stock: -qty } },
  { session },
);
if (res.modifiedCount === 0) throw new Error("Out of stock");
```

- Wrap stock updates and order creation in a transaction when you update several products.
- Keep products and their stock on the same shard as the order if possible, or accept cross-shard transactions.
- For very hot items, split stock across several "bucket" documents to reduce write conflicts.
- Use idempotency keys (unique index on `requestId`) so client retries do not create duplicate orders.

### 450: How would you approach a MongoDB performance review for an existing application?

1. Gather the workload: top query shapes (profiler, `$queryStats`, logs), read/write ratio, data size and growth.
2. Check hardware: RAM vs working set, disk IOPS, CPU, network.
3. Check indexes: missing indexes for slow queries, unused and redundant indexes (`$indexStats`).
4. Check the schema: unbounded arrays, very large documents, too many collections, wrong data types (dates as strings).
5. Check replication and sharding: lag, oplog window, shard key distribution, scatter-gather queries.
6. Check driver config: one client per process, pool size, timeouts, read and write concerns.
7. Make one change at a time and measure before and after with the same workload.
