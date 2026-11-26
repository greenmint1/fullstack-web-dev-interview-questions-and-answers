# Translate MongoDB into SQL, BigQuery, Redis, Snowflake, DynamoDB, Firebase and Elasticsearch Interview Questions and Answers

_Last updated: November 26, 2026_

450 interview questions about translating MongoDB data models, queries and patterns into SQL, Google BigQuery, Redis, Snowflake, Amazon DynamoDB, Firebase (Cloud Firestore) and Elasticsearch, split into three levels: 150 easy, 150 moderate and 150 advanced. Every answer shows the same idea in each database, in this order: MongoDB, SQL, BigQuery, Redis, Snowflake, DynamoDB, Firebase, Elasticsearch. When a database has no sensible way to do something, it is left out of that answer.

The answers target MongoDB 8 with the official Node.js driver, PostgreSQL 17+ for SQL, BigQuery GoogleSQL, Redis 8 (which has JSON and the Redis Query Engine built in) with `node-redis` v5, Snowflake SQL, DynamoDB with the AWS SDK for JavaScript v3 (`@aws-sdk/lib-dynamodb`), Cloud Firestore with the `firebase-admin` SDK, and Elasticsearch 9 with `@elastic/elasticsearch`. SQL, BigQuery and Snowflake examples are plain SQL. The other examples are JavaScript and use these client objects: `db` (a MongoDB `Db`), `pool` (a `pg` pool), `redis` (a `node-redis` client), `ddb` (a `DynamoDBDocumentClient`), `firestore` (from `getFirestore()`) and `es` (an Elasticsearch `Client`).

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does it mean to translate MongoDB into SQL, BigQuery, Redis, Snowflake, DynamoDB, Firebase or Elasticsearch?](#1-what-does-it-mean-to-translate-mongodb-into-sql-bigquery-redis-snowflake-dynamodb-firebase-or-elasticsearch)
- [2: How are these databases different in nature?](#2-how-are-these-databases-different-in-nature)
- [3: How do the core terms map between the databases?](#3-how-do-the-core-terms-map-between-the-databases)
- [4: How do you connect from Node.js to each database?](#4-how-do-you-connect-from-nodejs-to-each-database)
- [5: How do you create a database?](#5-how-do-you-create-a-database)
- [6: How do you create a collection or table?](#6-how-do-you-create-a-collection-or-table)
- [7: How do you insert one document?](#7-how-do-you-insert-one-document)
- [8: How do you insert many documents at once?](#8-how-do-you-insert-many-documents-at-once)
- [9: How do you find a document by its id?](#9-how-do-you-find-a-document-by-its-id)
- [10: How do you find all documents?](#10-how-do-you-find-all-documents)
- [11: How do you filter by equality on one field?](#11-how-do-you-filter-by-equality-on-one-field)
- [12: How do you filter with comparison operators like $gt and $lt?](#12-how-do-you-filter-with-comparison-operators-like-gt-and-lt)
- [13: How do you translate $in and $nin?](#13-how-do-you-translate-in-and-nin)
- [14: How do you translate $ne?](#14-how-do-you-translate-ne)
- [15: How do you combine conditions with AND?](#15-how-do-you-combine-conditions-with-and)
- [16: How do you translate $or?](#16-how-do-you-translate-or)
- [17: How do you select only some fields (projection)?](#17-how-do-you-select-only-some-fields-projection)
- [18: How do you sort results?](#18-how-do-you-sort-results)
- [19: How do you limit the number of results?](#19-how-do-you-limit-the-number-of-results)
- [20: How do you skip results for simple paging?](#20-how-do-you-skip-results-for-simple-paging)
- [21: How do you count documents?](#21-how-do-you-count-documents)
- [22: How do you check if a field exists ($exists)?](#22-how-do-you-check-if-a-field-exists-exists)
- [23: How do you find documents where a field is null?](#23-how-do-you-find-documents-where-a-field-is-null)
- [24: How do you update one field with $set?](#24-how-do-you-update-one-field-with-set)
- [25: How do you update many documents?](#25-how-do-you-update-many-documents)
- [26: How do you increment a number with $inc?](#26-how-do-you-increment-a-number-with-inc)
- [27: How do you remove a field with $unset?](#27-how-do-you-remove-a-field-with-unset)
- [28: How do you replace a whole document?](#28-how-do-you-replace-a-whole-document)
- [29: How do you delete one document?](#29-how-do-you-delete-one-document)
- [30: How do you delete many documents?](#30-how-do-you-delete-many-documents)
- [31: How do you delete all documents but keep the collection?](#31-how-do-you-delete-all-documents-but-keep-the-collection)
- [32: How do you drop a collection?](#32-how-do-you-drop-a-collection)
- [33: What replaces the _id field and ObjectId?](#33-what-replaces-the-_id-field-and-objectid)
- [34: How do you generate ids in each database?](#34-how-do-you-generate-ids-in-each-database)
- [35: How do data types map between the databases?](#35-how-do-data-types-map-between-the-databases)
- [36: How do you store dates and timestamps?](#36-how-do-you-store-dates-and-timestamps)
- [37: How do you store money and decimal numbers?](#37-how-do-you-store-money-and-decimal-numbers)
- [38: How do you store a nested object (embedded document)?](#38-how-do-you-store-a-nested-object-embedded-document)
- [39: How do you query a nested field with dot notation?](#39-how-do-you-query-a-nested-field-with-dot-notation)
- [40: How do you store an array?](#40-how-do-you-store-an-array)
- [41: How do you find documents where an array contains a value?](#41-how-do-you-find-documents-where-an-array-contains-a-value)
- [42: How do you translate $all?](#42-how-do-you-translate-all)
- [43: How do you query by array length with $size?](#43-how-do-you-query-by-array-length-with-size)
- [44: How do you push a value to an array ($push)?](#44-how-do-you-push-a-value-to-an-array-push)
- [45: How do you translate $addToSet?](#45-how-do-you-translate-addtoset)
- [46: How do you remove a value from an array with $pull?](#46-how-do-you-remove-a-value-from-an-array-with-pull)
- [47: How do you translate $pop (remove the first or last array item)?](#47-how-do-you-translate-pop-remove-the-first-or-last-array-item)
- [48: How do you do a pattern or LIKE search ($regex)?](#48-how-do-you-do-a-pattern-or-like-search-regex)
- [49: How do you do a case-insensitive match?](#49-how-do-you-do-a-case-insensitive-match)
- [50: How do you translate distinct()?](#50-how-do-you-translate-distinct)
- [51: How do you create a simple index?](#51-how-do-you-create-a-simple-index)
- [52: How do you create a unique index?](#52-how-do-you-create-a-unique-index)
- [53: How do you create a compound index?](#53-how-do-you-create-a-compound-index)
- [54: How do you list indexes?](#54-how-do-you-list-indexes)
- [55: How do you drop an index?](#55-how-do-you-drop-an-index)
- [56: How do you see the query plan (explain)?](#56-how-do-you-see-the-query-plan-explain)
- [57: How do you translate an upsert?](#57-how-do-you-translate-an-upsert)
- [58: How do you translate findOneAndUpdate (get the updated document back)?](#58-how-do-you-translate-findoneandupdate-get-the-updated-document-back)
- [59: How do you translate findOneAndDelete?](#59-how-do-you-translate-findoneanddelete)
- [60: How do you translate $setOnInsert?](#60-how-do-you-translate-setoninsert)
- [61: How do you translate the $min and $max update operators?](#61-how-do-you-translate-the-min-and-max-update-operators)
- [62: How do you translate $mul?](#62-how-do-you-translate-mul)
- [63: How do you rename a field with $rename?](#63-how-do-you-rename-a-field-with-rename)
- [64: How do you translate $currentDate?](#64-how-do-you-translate-currentdate)
- [65: How does schemaless MongoDB compare to schemas in the other databases?](#65-how-does-schemaless-mongodb-compare-to-schemas-in-the-other-databases)
- [66: How do you add a new field to existing records?](#66-how-do-you-add-a-new-field-to-existing-records)
- [67: How do you rename a collection?](#67-how-do-you-rename-a-collection)
- [68: How do you query by field type with $type?](#68-how-do-you-query-by-field-type-with-type)
- [69: How do you filter by a range of dates?](#69-how-do-you-filter-by-a-range-of-dates)
- [70: How do you translate $not?](#70-how-do-you-translate-not)
- [71: How do you translate $nor?](#71-how-do-you-translate-nor)
- [72: How do you compare two fields of the same document ($expr)?](#72-how-do-you-compare-two-fields-of-the-same-document-expr)
- [73: How do you translate a simple $group with $sum?](#73-how-do-you-translate-a-simple-group-with-sum)
- [74: How do you translate $match in an aggregation?](#74-how-do-you-translate-match-in-an-aggregation)
- [75: How do you translate $project in an aggregation?](#75-how-do-you-translate-project-in-an-aggregation)
- [76: How do you get the top N groups with $sort and $limit?](#76-how-do-you-get-the-top-n-groups-with-sort-and-limit)
- [77: How do you compute an average with $avg?](#77-how-do-you-compute-an-average-with-avg)
- [78: How do you get the min and max per group?](#78-how-do-you-get-the-min-and-max-per-group)
- [79: How do you count documents per group?](#79-how-do-you-count-documents-per-group)
- [80: How do you translate $unwind?](#80-how-do-you-translate-unwind)
- [81: How do you translate $lookup (a basic join)?](#81-how-do-you-translate-lookup-a-basic-join)
- [82: How do you translate $addFields (or $set) in a pipeline?](#82-how-do-you-translate-addfields-or-set-in-a-pipeline)
- [83: How do you translate the $count stage?](#83-how-do-you-translate-the-count-stage)
- [84: How do you join strings with $concat?](#84-how-do-you-join-strings-with-concat)
- [85: How do you change string case ($toUpper, $toLower)?](#85-how-do-you-change-string-case-toupper-tolower)
- [86: How do you take part of a string ($substrCP)?](#86-how-do-you-take-part-of-a-string-substrcp)
- [87: How do you translate $cond (if/else)?](#87-how-do-you-translate-cond-ifelse)
- [88: How do you translate $ifNull?](#88-how-do-you-translate-ifnull)
- [89: How do you format dates with $dateToString?](#89-how-do-you-format-dates-with-datetostring)
- [90: How do you extract the year and month from a date?](#90-how-do-you-extract-the-year-and-month-from-a-date)
- [91: How do you do math in queries ($add, $multiply, $round)?](#91-how-do-you-do-math-in-queries-add-multiply-round)
- [92: How do you expire data automatically (TTL index)?](#92-how-do-you-expire-data-automatically-ttl-index)
- [93: How do you translate capped collections?](#93-how-do-you-translate-capped-collections)
- [94: How do you store a location point?](#94-how-do-you-store-a-location-point)
- [95: How do you do a basic full-text search ($text)?](#95-how-do-you-do-a-basic-full-text-search-text)
- [96: How do you bulk load data like mongoimport?](#96-how-do-you-bulk-load-data-like-mongoimport)
- [97: How do you export data like mongoexport?](#97-how-do-you-export-data-like-mongoexport)
- [98: How do you back up and restore like mongodump and mongorestore?](#98-how-do-you-back-up-and-restore-like-mongodump-and-mongorestore)
- [99: What command-line shells replace mongosh?](#99-what-command-line-shells-replace-mongosh)
- [100: What GUI tools replace MongoDB Compass?](#100-what-gui-tools-replace-mongodb-compass)
- [101: How do you create a user and grant access?](#101-how-do-you-create-a-user-and-grant-access)
- [102: How do built-in roles like read and readWrite translate?](#102-how-do-built-in-roles-like-read-and-readwrite-translate)
- [103: How do you run a local instance for development?](#103-how-do-you-run-a-local-instance-for-development)
- [104: How do connection strings compare?](#104-how-do-connection-strings-compare)
- [105: How do you size the connection pool and close connections?](#105-how-do-you-size-the-connection-pool-and-close-connections)
- [106: What replaces Mongoose in Node.js?](#106-what-replaces-mongoose-in-nodejs)
- [107: How do you validate data on write ($jsonSchema)?](#107-how-do-you-validate-data-on-write-jsonschema)
- [108: How do you make a field required?](#108-how-do-you-make-a-field-required)
- [109: How do you set a default value for a field?](#109-how-do-you-set-a-default-value-for-a-field)
- [110: How do you store large files like GridFS?](#110-how-do-you-store-large-files-like-gridfs)
- [111: How do you translate a one-to-one relationship?](#111-how-do-you-translate-a-one-to-one-relationship)
- [112: How do you translate one-to-many with embedding?](#112-how-do-you-translate-one-to-many-with-embedding)
- [113: How do you translate one-to-many with references?](#113-how-do-you-translate-one-to-many-with-references)
- [114: How do you translate many-to-many?](#114-how-do-you-translate-many-to-many)
- [115: When should embedded documents become separate tables or items?](#115-when-should-embedded-documents-become-separate-tables-or-items)
- [116: How do you check if a document exists?](#116-how-do-you-check-if-a-document-exists)
- [117: How do you get the latest document?](#117-how-do-you-get-the-latest-document)
- [118: How do you get a random document ($sample)?](#118-how-do-you-get-a-random-document-sample)
- [119: How do you get the new id after an insert?](#119-how-do-you-get-the-new-id-after-an-insert)
- [120: How do you handle duplicate key errors?](#120-how-do-you-handle-duplicate-key-errors)
- [121: How do you read how many documents were changed?](#121-how-do-you-read-how-many-documents-were-changed)
- [122: How do you translate bulkWrite?](#122-how-do-you-translate-bulkwrite)
- [123: How do ordered and unordered inserts translate?](#123-how-do-ordered-and-unordered-inserts-translate)
- [124: How does write concern translate?](#124-how-does-write-concern-translate)
- [125: How does read preference translate?](#125-how-does-read-preference-translate)
- [126: What is the default read consistency in each database?](#126-what-is-the-default-read-consistency-in-each-database)
- [127: Which of these databases support transactions?](#127-which-of-these-databases-support-transactions)
- [128: How do you iterate over results with a cursor?](#128-how-do-you-iterate-over-results-with-a-cursor)
- [129: How do you stream a large result set without loading it all into memory?](#129-how-do-you-stream-a-large-result-set-without-loading-it-all-into-memory)
- [130: How does batchSize translate?](#130-how-does-batchsize-translate)
- [131: How do you set a query timeout like maxTimeMS?](#131-how-do-you-set-a-query-timeout-like-maxtimems)
- [132: How do you get the size of a collection or table?](#132-how-do-you-get-the-size-of-a-collection-or-table)
- [133: How do you list all collections or tables?](#133-how-do-you-list-all-collections-or-tables)
- [134: How do you list all databases?](#134-how-do-you-list-all-databases)
- [135: How do you match one element in an array of objects ($elemMatch)?](#135-how-do-you-match-one-element-in-an-array-of-objects-elemmatch)
- [136: How do you update one element in an array with the positional $ operator?](#136-how-do-you-update-one-element-in-an-array-with-the-positional--operator)
- [137: How do you update every element in an array with $[]?](#137-how-do-you-update-every-element-in-an-array-with-)
- [138: How do you store a map of dynamic keys?](#138-how-do-you-store-a-map-of-dynamic-keys)
- [139: How do you translate an auto-increment counter collection?](#139-how-do-you-translate-an-auto-increment-counter-collection)
- [140: How do you store user sessions?](#140-how-do-you-store-user-sessions)
- [141: How do you cache query results?](#141-how-do-you-cache-query-results)
- [142: How do you translate $sortByCount?](#142-how-do-you-translate-sortbycount)
- [143: How do you translate $replaceRoot?](#143-how-do-you-translate-replaceroot)
- [144: How do you convert types ($toString, $toInt, $convert)?](#144-how-do-you-convert-types-tostring-toint-convert)
- [145: How do you split a string ($split)?](#145-how-do-you-split-a-string-split)
- [146: How do you return an array length in the output ($size)?](#146-how-do-you-return-an-array-length-in-the-output-size)
- [147: How do you get one array element by position ($arrayElemAt)?](#147-how-do-you-get-one-array-element-by-position-arrayelemat)
- [148: How do you return only the first N array elements ($slice)?](#148-how-do-you-return-only-the-first-n-array-elements-slice)
- [149: How do you check the server version and health?](#149-how-do-you-check-the-server-version-and-health)
- [150: What should you check before translating a MongoDB app?](#150-what-should-you-check-before-translating-a-mongodb-app)

### Moderate Questions (151-300)

- [151: How do you translate a multi-document transaction?](#151-how-do-you-translate-a-multi-document-transaction)
- [152: How do you translate $lookup with a pipeline (a correlated join with conditions)?](#152-how-do-you-translate-lookup-with-a-pipeline-a-correlated-join-with-conditions)
- [153: How do you translate $lookup followed by $unwind into an inner join?](#153-how-do-you-translate-lookup-followed-by-unwind-into-an-inner-join)
- [154: How do you keep unmatched rows like a left join ($unwind with preserveNullAndEmptyArrays)?](#154-how-do-you-keep-unmatched-rows-like-a-left-join-unwind-with-preservenullandemptyarrays)
- [155: How do you translate $facet?](#155-how-do-you-translate-facet)
- [156: How do you translate $bucket?](#156-how-do-you-translate-bucket)
- [157: How do you translate $bucketAuto?](#157-how-do-you-translate-bucketauto)
- [158: How do you translate $graphLookup?](#158-how-do-you-translate-graphlookup)
- [159: How do you translate $unionWith?](#159-how-do-you-translate-unionwith)
- [160: How do you translate $out?](#160-how-do-you-translate-out)
- [161: How do you translate $merge?](#161-how-do-you-translate-merge)
- [162: How do you translate $setWindowFields for a running total?](#162-how-do-you-translate-setwindowfields-for-a-running-total)
- [163: How do you rank rows within groups ($rank, $denseRank)?](#163-how-do-you-rank-rows-within-groups-rank-denserank)
- [164: How do you compute a moving average?](#164-how-do-you-compute-a-moving-average)
- [165: How do you translate $first and $last in a $group?](#165-how-do-you-translate-first-and-last-in-a-group)
- [166: How do you collect values into an array with $push in a $group?](#166-how-do-you-collect-values-into-an-array-with-push-in-a-group)
- [167: How do you collect distinct values with $addToSet in a $group?](#167-how-do-you-collect-distinct-values-with-addtoset-in-a-group)
- [168: How do you translate $topN and $bottomN?](#168-how-do-you-translate-topn-and-bottomn)
- [169: How do you fill gaps in time series ($densify and $fill)?](#169-how-do-you-fill-gaps-in-time-series-densify-and-fill)
- [170: How do you group by day or month ($dateTrunc)?](#170-how-do-you-group-by-day-or-month-datetrunc)
- [171: How do you add to or subtract dates ($dateAdd, $dateDiff)?](#171-how-do-you-add-to-or-subtract-dates-dateadd-datediff)
- [172: How do you handle time zones when grouping dates?](#172-how-do-you-handle-time-zones-when-grouping-dates)
- [173: How do you filter elements inside an array ($filter)?](#173-how-do-you-filter-elements-inside-an-array-filter)
- [174: How do you transform each array element ($map)?](#174-how-do-you-transform-each-array-element-map)
- [175: How do you reduce an array to one value ($reduce)?](#175-how-do-you-reduce-an-array-to-one-value-reduce)
- [176: How do you translate $objectToArray and $arrayToObject?](#176-how-do-you-translate-objecttoarray-and-arraytoobject)
- [177: How do you merge objects ($mergeObjects)?](#177-how-do-you-merge-objects-mergeobjects)
- [178: How do you translate $switch?](#178-how-do-you-translate-switch)
- [179: How do you translate $regexMatch and $regexFind?](#179-how-do-you-translate-regexmatch-and-regexfind)
- [180: How do you translate $let variables?](#180-how-do-you-translate-let-variables)
- [181: How do you translate cursor-based (keyset) pagination?](#181-how-do-you-translate-cursor-based-keyset-pagination)
- [182: How do you return a page of results with the total count?](#182-how-do-you-return-a-page-of-results-with-the-total-count)
- [183: How do you translate an update with an aggregation pipeline?](#183-how-do-you-translate-an-update-with-an-aggregation-pipeline)
- [184: How do you translate arrayFilters?](#184-how-do-you-translate-arrayfilters)
- [185: How do you keep a capped list inside a document ($push with $each, $sort, $slice)?](#185-how-do-you-keep-a-capped-list-inside-a-document-push-with-each-sort-slice)
- [186: How do you increment a field inside a map of counters?](#186-how-do-you-increment-a-field-inside-a-map-of-counters)
- [187: How do you translate optimistic locking with a version field?](#187-how-do-you-translate-optimistic-locking-with-a-version-field)
- [188: How do you translate change streams?](#188-how-do-you-translate-change-streams)
- [189: How do you resume a change feed after a crash (resume tokens)?](#189-how-do-you-resume-a-change-feed-after-a-crash-resume-tokens)
- [190: How do you translate partial indexes?](#190-how-do-you-translate-partial-indexes)
- [191: How do you translate sparse indexes?](#191-how-do-you-translate-sparse-indexes)
- [192: How do multikey (array) indexes translate?](#192-how-do-multikey-array-indexes-translate)
- [193: How do you translate a text index with field weights?](#193-how-do-you-translate-a-text-index-with-field-weights)
- [194: How do you translate wildcard indexes?](#194-how-do-you-translate-wildcard-indexes)
- [195: How do you translate hashed indexes?](#195-how-do-you-translate-hashed-indexes)
- [196: How do covered queries translate?](#196-how-do-covered-queries-translate)
- [197: How do you force a specific index (hint)?](#197-how-do-you-force-a-specific-index-hint)
- [198: How do you translate collation (case-insensitive sort and compare)?](#198-how-do-you-translate-collation-case-insensitive-sort-and-compare)
- [199: How does the ESR rule for compound indexes translate?](#199-how-does-the-esr-rule-for-compound-indexes-translate)
- [200: How do you find the nearest places ($near, $geoNear)?](#200-how-do-you-find-the-nearest-places-near-geonear)
- [201: How do you find points inside an area ($geoWithin)?](#201-how-do-you-find-points-inside-an-area-geowithin)
- [202: How do you translate Atlas Search?](#202-how-do-you-translate-atlas-search)
- [203: How do you translate autocomplete search?](#203-how-do-you-translate-autocomplete-search)
- [204: How do you translate fuzzy search (typo tolerance)?](#204-how-do-you-translate-fuzzy-search-typo-tolerance)
- [205: How do you sort search results by relevance score?](#205-how-do-you-sort-search-results-by-relevance-score)
- [206: How do you translate compound search queries (must, should, filter)?](#206-how-do-you-translate-compound-search-queries-must-should-filter)
- [207: How do you highlight matched words in search results?](#207-how-do-you-highlight-matched-words-in-search-results)
- [208: How do you translate time series collections?](#208-how-do-you-translate-time-series-collections)
- [209: How do you change schema rules on a live collection (validationLevel)?](#209-how-do-you-change-schema-rules-on-a-live-collection-validationlevel)
- [210: How do you translate the polymorphic pattern (different shapes in one collection)?](#210-how-do-you-translate-the-polymorphic-pattern-different-shapes-in-one-collection)
- [211: How do you translate the bucket pattern?](#211-how-do-you-translate-the-bucket-pattern)
- [212: How do you translate the computed pattern (precomputed totals)?](#212-how-do-you-translate-the-computed-pattern-precomputed-totals)
- [213: How do you translate the subset pattern?](#213-how-do-you-translate-the-subset-pattern)
- [214: How do you translate the extended reference pattern?](#214-how-do-you-translate-the-extended-reference-pattern)
- [215: How do you translate the outlier pattern?](#215-how-do-you-translate-the-outlier-pattern)
- [216: How do you translate the attribute pattern?](#216-how-do-you-translate-the-attribute-pattern)
- [217: How do you translate a tree with parent references?](#217-how-do-you-translate-a-tree-with-parent-references)
- [218: How do you translate the document versioning pattern?](#218-how-do-you-translate-the-document-versioning-pattern)
- [219: How do you translate an order with line items end to end?](#219-how-do-you-translate-an-order-with-line-items-end-to-end)
- [220: How do you translate a user with multiple addresses?](#220-how-do-you-translate-a-user-with-multiple-addresses)
- [221: How do you translate a blog with posts and comments?](#221-how-do-you-translate-a-blog-with-posts-and-comments)
- [222: How do you translate tags and filtering by tags?](#222-how-do-you-translate-tags-and-filtering-by-tags)
- [223: How do you translate a leaderboard?](#223-how-do-you-translate-a-leaderboard)
- [224: How do you translate a rate limiter?](#224-how-do-you-translate-a-rate-limiter)
- [225: How do you translate a job queue stored in a collection?](#225-how-do-you-translate-a-job-queue-stored-in-a-collection)
- [226: How do you translate pub/sub notifications?](#226-how-do-you-translate-pubsub-notifications)
- [227: How do you translate a distributed lock?](#227-how-do-you-translate-a-distributed-lock)
- [228: How do you translate a shopping cart?](#228-how-do-you-translate-a-shopping-cart)
- [229: How do you translate likes and follower counters?](#229-how-do-you-translate-likes-and-follower-counters)
- [230: How do you translate an activity feed?](#230-how-do-you-translate-an-activity-feed)
- [231: How do you enforce uniqueness on two fields together (compound unique)?](#231-how-do-you-enforce-uniqueness-on-two-fields-together-compound-unique)
- [232: How do you turn MongoDB queries into a DynamoDB single-table design?](#232-how-do-you-turn-mongodb-queries-into-a-dynamodb-single-table-design)
- [233: How do MongoDB secondary indexes become DynamoDB GSIs and LSIs?](#233-how-do-mongodb-secondary-indexes-become-dynamodb-gsis-and-lsis)
- [234: How do you translate a MongoDB search page with many optional filters into DynamoDB?](#234-how-do-you-translate-a-mongodb-search-page-with-many-optional-filters-into-dynamodb)
- [235: When do embedded arrays become Firestore subcollections?](#235-when-do-embedded-arrays-become-firestore-subcollections)
- [236: How do you query across all subcollections with the same name (collection group query)?](#236-how-do-you-query-across-all-subcollections-with-the-same-name-collection-group-query)
- [237: How do you translate $in on arrays (array-contains-any)?](#237-how-do-you-translate-in-on-arrays-array-contains-any)
- [238: How do you translate range filters on two different fields in Firestore?](#238-how-do-you-translate-range-filters-on-two-different-fields-in-firestore)
- [239: How do you push live database changes to a browser?](#239-how-do-you-push-live-database-changes-to-a-browser)
- [240: How do you translate access control into Firestore security rules?](#240-how-do-you-translate-access-control-into-firestore-security-rules)
- [241: How do you model documents in BigQuery with nested and repeated fields?](#241-how-do-you-model-documents-in-bigquery-with-nested-and-repeated-fields)
- [242: How do you query raw JSON documents in BigQuery with the JSON type?](#242-how-do-you-query-raw-json-documents-in-bigquery-with-the-json-type)
- [243: How do you store documents in PostgreSQL with JSONB?](#243-how-do-you-store-documents-in-postgresql-with-jsonb)
- [244: How do you index JSONB fields in PostgreSQL?](#244-how-do-you-index-jsonb-fields-in-postgresql)
- [245: How do you query documents in Snowflake with VARIANT and FLATTEN?](#245-how-do-you-query-documents-in-snowflake-with-variant-and-flatten)
- [246: How do you load MongoDB data into BigQuery?](#246-how-do-you-load-mongodb-data-into-bigquery)
- [247: How do you load MongoDB data into Snowflake?](#247-how-do-you-load-mongodb-data-into-snowflake)
- [248: How do you turn a MongoDB schema into an Elasticsearch mapping?](#248-how-do-you-turn-a-mongodb-schema-into-an-elasticsearch-mapping)
- [249: When should you use nested instead of object fields in Elasticsearch?](#249-when-should-you-use-nested-instead-of-object-fields-in-elasticsearch)
- [250: How do you bulk index documents into Elasticsearch?](#250-how-do-you-bulk-index-documents-into-elasticsearch)
- [251: Why does a new document not show up in Elasticsearch search right away?](#251-why-does-a-new-document-not-show-up-in-elasticsearch-search-right-away)
- [252: How do you translate a full aggregation pipeline into Elasticsearch aggregations?](#252-how-do-you-translate-a-full-aggregation-pipeline-into-elasticsearch-aggregations)
- [253: How do you write the same pipeline with ES|QL?](#253-how-do-you-write-the-same-pipeline-with-esql)
- [254: How do you store and query MongoDB-like documents in Redis with JSON?](#254-how-do-you-store-and-query-mongodb-like-documents-in-redis-with-json)
- [255: How do MongoDB index types map to Redis Query Engine field types?](#255-how-do-mongodb-index-types-map-to-redis-query-engine-field-types)
- [256: When do you use a Redis hash and when Redis JSON?](#256-when-do-you-use-a-redis-hash-and-when-redis-json)
- [257: How do you use sorted sets as a secondary index for range queries?](#257-how-do-you-use-sorted-sets-as-a-secondary-index-for-range-queries)
- [258: How do you expire one field instead of the whole key?](#258-how-do-you-expire-one-field-instead-of-the-whole-key)
- [259: How do you translate a multi-step atomic update into a Redis Lua script or function?](#259-how-do-you-translate-a-multi-step-atomic-update-into-a-redis-lua-script-or-function)
- [260: How do you name Redis keys when translating collections?](#260-how-do-you-name-redis-keys-when-translating-collections)
- [261: How do you translate an event log or change log into Redis Streams?](#261-how-do-you-translate-an-event-log-or-change-log-into-redis-streams)
- [262: How do you translate conditional updates into DynamoDB ConditionExpression?](#262-how-do-you-translate-conditional-updates-into-dynamodb-conditionexpression)
- [263: How do MongoDB update operators map to DynamoDB UpdateExpression?](#263-how-do-mongodb-update-operators-map-to-dynamodb-updateexpression)
- [264: What is the difference between Query and Scan in DynamoDB compared to find() in MongoDB?](#264-what-is-the-difference-between-query-and-scan-in-dynamodb-compared-to-find-in-mongodb)
- [265: How do you process a whole DynamoDB table in parallel?](#265-how-do-you-process-a-whole-dynamodb-table-in-parallel)
- [266: How do you translate a $in on ids into a batch read?](#266-how-do-you-translate-a-in-on-ids-into-a-batch-read)
- [267: How do you read several items consistently at the same moment?](#267-how-do-you-read-several-items-consistently-at-the-same-moment)
- [268: Why do DynamoDB expressions need ExpressionAttributeNames?](#268-why-do-dynamodb-expressions-need-expressionattributenames)
- [269: How do you write SQL-like queries for DynamoDB with PartiQL?](#269-how-do-you-write-sql-like-queries-for-dynamodb-with-partiql)
- [270: When do you use a Firestore transaction and when a batched write?](#270-when-do-you-use-a-firestore-transaction-and-when-a-batched-write)
- [271: How do you replace Mongoose models with Firestore converters?](#271-how-do-you-replace-mongoose-models-with-firestore-converters)
- [272: How do you keep denormalized copies in sync?](#272-how-do-you-keep-denormalized-copies-in-sync)
- [273: How do you translate scheduled jobs (Atlas scheduled triggers)?](#273-how-do-you-translate-scheduled-jobs-atlas-scheduled-triggers)
- [274: How do you translate server-side functions and stored procedures?](#274-how-do-you-translate-server-side-functions-and-stored-procedures)
- [275: How do you translate MongoDB views?](#275-how-do-you-translate-mongodb-views)
- [276: How do you translate on-demand materialized views ($merge into a summary collection)?](#276-how-do-you-translate-on-demand-materialized-views-merge-into-a-summary-collection)
- [277: How do you partition a BigQuery table and why does it matter?](#277-how-do-you-partition-a-bigquery-table-and-why-does-it-matter)
- [278: How does BigQuery clustering compare to MongoDB indexes?](#278-how-does-bigquery-clustering-compare-to-mongodb-indexes)
- [279: How do Snowflake micro-partitions and clustering keys work compared to MongoDB indexes?](#279-how-do-snowflake-micro-partitions-and-clustering-keys-work-compared-to-mongodb-indexes)
- [280: How do you restore old data (Snowflake time travel vs MongoDB point-in-time restore)?](#280-how-do-you-restore-old-data-snowflake-time-travel-vs-mongodb-point-in-time-restore)
- [281: How do you translate copying a database for testing (zero-copy clone)?](#281-how-do-you-translate-copying-a-database-for-testing-zero-copy-clone)
- [282: How do you upsert a batch of changed documents into BigQuery or Snowflake?](#282-how-do-you-upsert-a-batch-of-changed-documents-into-bigquery-or-snowflake)
- [283: How do you handle deletes when syncing MongoDB into a warehouse?](#283-how-do-you-handle-deletes-when-syncing-mongodb-into-a-warehouse)
- [284: How do you stream MongoDB changes into BigQuery or Snowflake (CDC)?](#284-how-do-you-stream-mongodb-changes-into-bigquery-or-snowflake-cdc)
- [285: How do you build an incremental pipeline with Snowflake streams and tasks?](#285-how-do-you-build-an-incremental-pipeline-with-snowflake-streams-and-tasks)
- [286: How do you pass query parameters safely in each database?](#286-how-do-you-pass-query-parameters-safely-in-each-database)
- [287: How does NoSQL injection translate to the other databases?](#287-how-does-nosql-injection-translate-to-the-other-databases)
- [288: How does id sort order change when you replace ObjectId?](#288-how-does-id-sort-order-change-when-you-replace-objectid)
- [289: How do you set created and updated timestamps automatically?](#289-how-do-you-set-created-and-updated-timestamps-automatically)
- [290: How do you translate soft deletes?](#290-how-do-you-translate-soft-deletes)
- [291: How do you translate multi-tenant data?](#291-how-do-you-translate-multi-tenant-data)
- [292: How do you translate Mongoose models into Prisma or Drizzle for SQL?](#292-how-do-you-translate-mongoose-models-into-prisma-or-drizzle-for-sql)
- [293: How do you translate Mongoose middleware (pre and post hooks)?](#293-how-do-you-translate-mongoose-middleware-pre-and-post-hooks)
- [294: How do you translate populate()?](#294-how-do-you-translate-populate)
- [295: How do you get read-your-writes consistency after translating?](#295-how-do-you-get-read-your-writes-consistency-after-translating)
- [296: How do you translate retryable writes and error retries?](#296-how-do-you-translate-retryable-writes-and-error-retries)
- [297: How do you handle connections in serverless functions (Lambda, Cloud Functions)?](#297-how-do-you-handle-connections-in-serverless-functions-lambda-cloud-functions)
- [298: How do you test translated queries locally?](#298-how-do-you-test-translated-queries-locally)
- [299: How do you translate Mongoose virtuals and computed fields?](#299-how-do-you-translate-mongoose-virtuals-and-computed-fields)
- [300: How do you translate a basic CRUD API from MongoDB to each database?](#300-how-do-you-translate-a-basic-crud-api-from-mongodb-to-each-database)

### Advanced Questions (301-450)

- [301: How would you plan a full migration from MongoDB to PostgreSQL?](#301-how-would-you-plan-a-full-migration-from-mongodb-to-postgresql)
- [302: How would you plan a migration from MongoDB to DynamoDB?](#302-how-would-you-plan-a-migration-from-mongodb-to-dynamodb)
- [303: How would you plan a migration from MongoDB to Firestore?](#303-how-would-you-plan-a-migration-from-mongodb-to-firestore)
- [304: How do you plan moving MongoDB analytics to BigQuery or Snowflake?](#304-how-do-you-plan-moving-mongodb-analytics-to-bigquery-or-snowflake)
- [305: How do you add Elasticsearch next to MongoDB for search?](#305-how-do-you-add-elasticsearch-next-to-mongodb-for-search)
- [306: How do you put Redis in front of a database as a cache?](#306-how-do-you-put-redis-in-front-of-a-database-as-a-cache)
- [307: How do you migrate with zero downtime using dual writes?](#307-how-do-you-migrate-with-zero-downtime-using-dual-writes)
- [308: How do you verify that migrated data matches?](#308-how-do-you-verify-that-migrated-data-matches)
- [309: How do you handle schema drift in MongoDB documents during migration?](#309-how-do-you-handle-schema-drift-in-mongodb-documents-during-migration)
- [310: How do you translate ObjectId references while keeping relations intact?](#310-how-do-you-translate-objectid-references-while-keeping-relations-intact)
- [311: How do you turn deeply nested documents into normalized tables?](#311-how-do-you-turn-deeply-nested-documents-into-normalized-tables)
- [312: When should you use JSONB and when normalized columns in PostgreSQL?](#312-when-should-you-use-jsonb-and-when-normalized-columns-in-postgresql)
- [313: How do you translate unbounded arrays?](#313-how-do-you-translate-unbounded-arrays)
- [314: How do size limits compare, and what do you do when a document is too big?](#314-how-do-size-limits-compare-and-what-do-you-do-when-a-document-is-too-big)
- [315: How does MongoDB sharding translate?](#315-how-does-mongodb-sharding-translate)
- [316: How do you choose a partition key compared to a MongoDB shard key?](#316-how-do-you-choose-a-partition-key-compared-to-a-mongodb-shard-key)
- [317: How do you avoid hot partitions?](#317-how-do-you-avoid-hot-partitions)
- [318: How do replica sets and failover translate?](#318-how-do-replica-sets-and-failover-translate)
- [319: How do MongoDB read concern levels map to other databases?](#319-how-do-mongodb-read-concern-levels-map-to-other-databases)
- [320: How do change events stay in order when syncing to another database?](#320-how-do-change-events-stay-in-order-when-syncing-to-another-database)
- [321: How do transaction isolation levels compare?](#321-how-do-transaction-isolation-levels-compare)
- [322: What are the transaction limits in each database?](#322-what-are-the-transaction-limits-in-each-database)
- [323: How do you handle write conflicts and retries in transactions?](#323-how-do-you-handle-write-conflicts-and-retries-in-transactions)
- [324: How do you coordinate a change across two different databases (saga)?](#324-how-do-you-coordinate-a-change-across-two-different-databases-saga)
- [325: How do you translate the transactional outbox pattern?](#325-how-do-you-translate-the-transactional-outbox-pattern)
- [326: How do you make writes idempotent in each database?](#326-how-do-you-make-writes-idempotent-in-each-database)
- [327: How do you load data into BigQuery or Snowflake exactly once?](#327-how-do-you-load-data-into-bigquery-or-snowflake-exactly-once)
- [328: How do you rebuild a search index or cache from scratch without downtime?](#328-how-do-you-rebuild-a-search-index-or-cache-from-scratch-without-downtime)
- [329: How do you keep a cache consistent with the database?](#329-how-do-you-keep-a-cache-consistent-with-the-database)
- [330: How do you prevent a cache stampede?](#330-how-do-you-prevent-a-cache-stampede)
- [331: How durable is Redis compared to MongoDB?](#331-how-durable-is-redis-compared-to-mongodb)
- [332: How do multi-key operations work in Redis Cluster?](#332-how-do-multi-key-operations-work-in-redis-cluster)
- [333: What happens when Redis runs out of memory?](#333-what-happens-when-redis-runs-out-of-memory)
- [334: How do you translate a big aggregation that needs allowDiskUse?](#334-how-do-you-translate-a-big-aggregation-that-needs-allowdiskuse)
- [335: How do you speed up pipelines with many $lookup stages when you translate them?](#335-how-do-you-speed-up-pipelines-with-many-lookup-stages-when-you-translate-them)
- [336: What replaces the MongoDB profiler for finding slow queries?](#336-what-replaces-the-mongodb-profiler-for-finding-slow-queries)
- [337: How do you find unused indexes like $indexStats?](#337-how-do-you-find-unused-indexes-like-indexstats)
- [338: How do you control query cost in BigQuery?](#338-how-do-you-control-query-cost-in-bigquery)
- [339: How do you control cost in Snowflake?](#339-how-do-you-control-cost-in-snowflake)
- [340: How do you control cost in DynamoDB?](#340-how-do-you-control-cost-in-dynamodb)
- [341: How do you control cost in Firestore?](#341-how-do-you-control-cost-in-firestore)
- [342: How do you size Elasticsearch shards?](#342-how-do-you-size-elasticsearch-shards)
- [343: How do you change a field's type in Elasticsearch without downtime?](#343-how-do-you-change-a-fields-type-in-elasticsearch-without-downtime)
- [344: How do you page deep into Elasticsearch results?](#344-how-do-you-page-deep-into-elasticsearch-results)
- [345: How do you translate Atlas Vector Search?](#345-how-do-you-translate-atlas-vector-search)
- [346: How do you translate hybrid search (keywords plus vectors)?](#346-how-do-you-translate-hybrid-search-keywords-plus-vectors)
- [347: How do you translate Queryable Encryption and client-side field-level encryption?](#347-how-do-you-translate-queryable-encryption-and-client-side-field-level-encryption)
- [348: How do encryption at rest and in transit compare?](#348-how-do-encryption-at-rest-and-in-transit-compare)
- [349: How do you translate row-level or document-level security?](#349-how-do-you-translate-row-level-or-document-level-security)
- [350: How do you hide fields from some users like $redact or projections?](#350-how-do-you-hide-fields-from-some-users-like-redact-or-projections)
- [351: How do you translate database auditing?](#351-how-do-you-translate-database-auditing)
- [352: How do you plan disaster recovery (RPO and RTO) for each database?](#352-how-do-you-plan-disaster-recovery-rpo-and-rto-for-each-database)
- [353: How do you translate multi-region, active-active setups?](#353-how-do-you-translate-multi-region-active-active-setups)
- [354: How do you keep data in a specific country or region (data residency)?](#354-how-do-you-keep-data-in-a-specific-country-or-region-data-residency)
- [355: How do you handle time series retention and downsampling at scale?](#355-how-do-you-handle-time-series-retention-and-downsampling-at-scale)
- [356: How do you handle counters with very high write rates?](#356-how-do-you-handle-counters-with-very-high-write-rates)
- [357: How do you generate ids at scale without a central counter?](#357-how-do-you-generate-ids-at-scale-without-a-central-counter)
- [358: How do you model many-to-many at scale in DynamoDB?](#358-how-do-you-model-many-to-many-at-scale-in-dynamodb)
- [359: How do you translate a social graph query like friends of friends?](#359-how-do-you-translate-a-social-graph-query-like-friends-of-friends)
- [360: How do you translate a product catalog with different attributes per category?](#360-how-do-you-translate-a-product-catalog-with-different-attributes-per-category)
- [361: How do you translate a chat app's data model?](#361-how-do-you-translate-a-chat-apps-data-model)
- [362: How do you translate an IoT telemetry system?](#362-how-do-you-translate-an-iot-telemetry-system)
- [363: How do you translate an append-only audit log or event store?](#363-how-do-you-translate-an-append-only-audit-log-or-event-store)
- [364: How do you protect tenants from each other (noisy neighbors) at scale?](#364-how-do-you-protect-tenants-from-each-other-noisy-neighbors-at-scale)
- [365: How do you translate a reporting dashboard built on MongoDB aggregations?](#365-how-do-you-translate-a-reporting-dashboard-built-on-mongodb-aggregations)
- [366: How do you translate a search page with filters, facets and sorting?](#366-how-do-you-translate-a-search-page-with-filters-facets-and-sorting)
- [367: How do you translate a social feed: fan-out on write or on read?](#367-how-do-you-translate-a-social-feed-fan-out-on-write-or-on-read)
- [368: How do you prevent double booking?](#368-how-do-you-prevent-double-booking)
- [369: How do you decrement inventory without overselling?](#369-how-do-you-decrement-inventory-without-overselling)
- [370: How do you translate a wallet or ledger balance?](#370-how-do-you-translate-a-wallet-or-ledger-balance)
- [371: How do you translate "nearby" search at scale?](#371-how-do-you-translate-nearby-search-at-scale)
- [372: How do you translate a GDPR delete (right to be forgotten)?](#372-how-do-you-translate-a-gdpr-delete-right-to-be-forgotten)
- [373: How do you translate archiving old data (Atlas Online Archive)?](#373-how-do-you-translate-archiving-old-data-atlas-online-archive)
- [374: How do you replace $out-based ETL jobs with ELT in a warehouse?](#374-how-do-you-replace-out-based-etl-jobs-with-elt-in-a-warehouse)
- [375: How do BigQuery JSON and Snowflake VARIANT compare for semi-structured data?](#375-how-do-bigquery-json-and-snowflake-variant-compare-for-semi-structured-data)
- [376: How do you handle schema changes from MongoDB in BigQuery and Snowflake?](#376-how-do-you-handle-schema-changes-from-mongodb-in-bigquery-and-snowflake)
- [377: How do you translate approximate distinct counts (HyperLogLog)?](#377-how-do-you-translate-approximate-distinct-counts-hyperloglog)
- [378: How do you compute percentiles like p95?](#378-how-do-you-compute-percentiles-like-p95)
- [379: How do you split events into user sessions (sessionization)?](#379-how-do-you-split-events-into-user-sessions-sessionization)
- [380: How do you translate funnel analysis?](#380-how-do-you-translate-funnel-analysis)
- [381: How do you translate retention cohorts?](#381-how-do-you-translate-retention-cohorts)
- [382: How do you pivot rows into columns?](#382-how-do-you-pivot-rows-into-columns)
- [383: How do you keep only the latest record per key (dedupe)?](#383-how-do-you-keep-only-the-latest-record-per-key-dedupe)
- [384: How do you find streaks or gaps (gaps and islands)?](#384-how-do-you-find-streaks-or-gaps-gaps-and-islands)
- [385: What are your options for joins in Elasticsearch?](#385-what-are-your-options-for-joins-in-elasticsearch)
- [386: How do you decide what to denormalize when there are no joins (DynamoDB, Firestore)?](#386-how-do-you-decide-what-to-denormalize-when-there-are-no-joins-dynamodb-firestore)
- [387: How do you keep references valid without foreign keys?](#387-how-do-you-keep-references-valid-without-foreign-keys)
- [388: How do you translate cascade deletes?](#388-how-do-you-translate-cascade-deletes)
- [389: How does sorting on array fields differ between MongoDB and the others?](#389-how-does-sorting-on-array-fields-differ-between-mongodb-and-the-others)
- [390: How do you configure Elasticsearch text analysis for multiple languages?](#390-how-do-you-configure-elasticsearch-text-analysis-for-multiple-languages)
- [391: How do you translate search synonyms?](#391-how-do-you-translate-search-synonyms)
- [392: How do you make search ignore accents (café matches cafe)?](#392-how-do-you-make-search-ignore-accents-café-matches-cafe)
- [393: How do you stream rows into BigQuery?](#393-how-do-you-stream-rows-into-bigquery)
- [394: How do you stream rows into Snowflake?](#394-how-do-you-stream-rows-into-snowflake)
- [395: How do you run analytics on DynamoDB data?](#395-how-do-you-run-analytics-on-dynamodb-data)
- [396: How do you get Firestore data into BigQuery?](#396-how-do-you-get-firestore-data-into-bigquery)
- [397: What Firestore limits catch people coming from MongoDB?](#397-what-firestore-limits-catch-people-coming-from-mongodb)
- [398: How do large arrays and maps affect Firestore indexes?](#398-how-do-large-arrays-and-maps-affect-firestore-indexes)
- [399: What is the 10 GB item collection limit in DynamoDB?](#399-what-is-the-10-gb-item-collection-limit-in-dynamodb)
- [400: How do DynamoDB partitions, burst and adaptive capacity work?](#400-how-do-dynamodb-partitions-burst-and-adaptive-capacity-work)
- [401: How do DynamoDB global tables handle write conflicts?](#401-how-do-dynamodb-global-tables-handle-write-conflicts)
- [402: How do you partition large tables in PostgreSQL?](#402-how-do-you-partition-large-tables-in-postgresql)
- [403: How does PostgreSQL MVCC compare to MongoDB's WiredTiger, and why does VACUUM matter?](#403-how-does-postgresql-mvcc-compare-to-mongodbs-wiredtiger-and-why-does-vacuum-matter)
- [404: How do you lock a row while you read and update it?](#404-how-do-you-lock-a-row-while-you-read-and-update-it)
- [405: Why do deadlocks show up after moving to SQL, and how do you avoid them?](#405-why-do-deadlocks-show-up-after-moving-to-sql-and-how-do-you-avoid-them)
- [406: How do connection limits differ, and when do you need a pooler?](#406-how-do-connection-limits-differ-and-when-do-you-need-a-pooler)
- [407: How do you handle replica lag when reading from replicas?](#407-how-do-you-handle-replica-lag-when-reading-from-replicas)
- [408: How do you scale PostgreSQL horizontally like a sharded MongoDB cluster?](#408-how-do-you-scale-postgresql-horizontally-like-a-sharded-mongodb-cluster)
- [409: How do storage and compression compare?](#409-how-do-storage-and-compression-compare)
- [410: When do you use Snowflake's search optimization service?](#410-when-do-you-use-snowflakes-search-optimization-service)
- [411: How do BigQuery search indexes work?](#411-how-do-bigquery-search-indexes-work)
- [412: How do BigQuery slots and Snowflake warehouses compare to MongoDB cluster tiers?](#412-how-do-bigquery-slots-and-snowflake-warehouses-compare-to-mongodb-cluster-tiers)
- [413: Can Snowflake replace MongoDB for app workloads with hybrid tables?](#413-can-snowflake-replace-mongodb-for-app-workloads-with-hybrid-tables)
- [414: How do you share data with another team or company?](#414-how-do-you-share-data-with-another-team-or-company)
- [415: How do you query data in place without loading it (federated queries)?](#415-how-do-you-query-data-in-place-without-loading-it-federated-queries)
- [416: What are the risks of using Redis as the primary database instead of MongoDB?](#416-what-are-the-risks-of-using-redis-as-the-primary-database-instead-of-mongodb)
- [417: How do you check "have we seen this before" cheaply (Bloom filters)?](#417-how-do-you-check-have-we-seen-this-before-cheaply-bloom-filters)
- [418: How does Redis client-side caching work?](#418-how-does-redis-client-side-caching-work)
- [419: How do you react to key expiry or changes in Redis (keyspace notifications)?](#419-how-do-you-react-to-key-expiry-or-changes-in-redis-keyspace-notifications)
- [420: What metrics do you watch for each database?](#420-what-metrics-do-you-watch-for-each-database)
- [421: How do you load test a translated database layer?](#421-how-do-you-load-test-a-translated-database-layer)
- [422: How do you define each database as infrastructure as code?](#422-how-do-you-define-each-database-as-infrastructure-as-code)
- [423: How do you run each database in CI?](#423-how-do-you-run-each-database-in-ci)
- [424: How do you translate Mongoose discriminators into SQL?](#424-how-do-you-translate-mongoose-discriminators-into-sql)
- [425: How do you delete millions of rows or documents without hurting the database?](#425-how-do-you-delete-millions-of-rows-or-documents-without-hurting-the-database)
- [426: How do you update millions of records safely?](#426-how-do-you-update-millions-of-records-safely)
- [427: How do you write a migration script that can stop and resume?](#427-how-do-you-write-a-migration-script-that-can-stop-and-resume)
- [428: What replaces migration tools like migrate-mongo?](#428-what-replaces-migration-tools-like-migrate-mongo)
- [429: How do string sorting and comparison rules differ?](#429-how-do-string-sorting-and-comparison-rules-differ)
- [430: How do null and missing fields behave differently?](#430-how-do-null-and-missing-fields-behave-differently)
- [431: How does matching on arrays differ?](#431-how-does-matching-on-arrays-differ)
- [432: What happens when a field has mixed types?](#432-what-happens-when-a-field-has-mixed-types)
- [433: How do you keep 64-bit integers precise in JavaScript?](#433-how-do-you-keep-64-bit-integers-precise-in-javascript)
- [434: How do date precision and time zones differ?](#434-how-do-date-precision-and-time-zones-differ)
- [435: How do case sensitivity defaults differ?](#435-how-do-case-sensitivity-defaults-differ)
- [436: Where do nulls go when sorting?](#436-where-do-nulls-go-when-sorting)
- [437: What field names cause problems when translating?](#437-what-field-names-cause-problems-when-translating)
- [438: How do concurrent upserts cause duplicates, and how do you stop them?](#438-how-do-concurrent-upserts-cause-duplicates-and-how-do-you-stop-them)
- [439: How do you translate queries that use the timestamp inside ObjectId?](#439-how-do-you-translate-queries-that-use-the-timestamp-inside-objectid)
- [440: Why does single-document atomicity break when you normalize?](#440-why-does-single-document-atomicity-break-when-you-normalize)
- [441: How do you keep app code from depending on the database during the migration?](#441-how-do-you-keep-app-code-from-depending-on-the-database-during-the-migration)
- [442: How do you plan a rollback if the new database has problems after cut-over?](#442-how-do-you-plan-a-rollback-if-the-new-database-has-problems-after-cut-over)
- [443: How do you check that translated queries return the same results (shadow testing)?](#443-how-do-you-check-that-translated-queries-return-the-same-results-shadow-testing)
- [444: How do you estimate the cost of the same workload in each database?](#444-how-do-you-estimate-the-cost-of-the-same-workload-in-each-database)
- [445: How do you choose the target database for a MongoDB workload?](#445-how-do-you-choose-the-target-database-for-a-mongodb-workload)
- [446: When should you not move away from MongoDB?](#446-when-should-you-not-move-away-from-mongodb)
- [447: How would you design a polyglot setup using several of these databases together?](#447-how-would-you-design-a-polyglot-setup-using-several-of-these-databases-together)
- [448: Scenario: how would you migrate a MongoDB e-commerce app with slow reports and slow search?](#448-scenario-how-would-you-migrate-a-mongodb-e-commerce-app-with-slow-reports-and-slow-search)
- [449: Scenario: how would you redesign a MongoDB-based mobile chat app for Firestore?](#449-scenario-how-would-you-redesign-a-mongodb-based-mobile-chat-app-for-firestore)
- [450: What are the most common mistakes when translating MongoDB to these databases?](#450-what-are-the-most-common-mistakes-when-translating-mongodb-to-these-databases)

---

# Easy Questions (1-150)

## 1: What does it mean to translate MongoDB into SQL, BigQuery, Redis, Snowflake, DynamoDB, Firebase or Elasticsearch?

It means storing the same data and answering the same questions with another database. You map each MongoDB idea to its closest match: a collection becomes a table, an index, a set of keys or a Firestore collection, a `find()` becomes a `SELECT`, a `Query`, a search request, and so on.

A good translation keeps what the app sees the same and changes only the storage and query code underneath. Most of the work is not syntax. It is learning how each database wants data to be shaped: SQL wants normalized tables, DynamoDB wants you to design around access patterns, Redis wants keys, and Elasticsearch wants denormalized documents built for search.

| MongoDB     | SQL        | BigQuery   | Redis              | Snowflake  | DynamoDB         | Firebase   | Elasticsearch |
| ----------- | ---------- | ---------- | ------------------ | ---------- | ---------------- | ---------- | ------------- |
| Collection  | Table      | Table      | Key prefix + index | Table      | Table            | Collection | Index         |
| Document    | Row        | Row        | Hash / JSON key    | Row        | Item             | Document   | Document      |
| `find()`    | `SELECT`   | `SELECT`   | `FT.SEARCH`        | `SELECT`   | `Query` / `Scan` | `.where()` | `_search`     |
| Aggregation | `GROUP BY` | `GROUP BY` | `FT.AGGREGATE`     | `GROUP BY` | Done in app code | `count()`  | Aggregations  |

## 2: How are these databases different in nature?

- **MongoDB** is a general-purpose document database. It stores flexible JSON-like documents and handles both app queries and a fair amount of analytics.
- **SQL** databases (PostgreSQL, MySQL) store rows in tables with a fixed schema, enforce relations with foreign keys and are strong at joins and transactions.
- **BigQuery** is Google's serverless data warehouse. It is built for scanning huge tables for analytics, not for fast single-row reads and writes.
- **Redis** is an in-memory data store. It is very fast and is mostly used for caching, sessions, counters, queues and real-time data.
- **Snowflake** is a cloud data warehouse, similar in purpose to BigQuery. Storage and compute are separate, and you pay for running warehouses.
- **DynamoDB** is AWS's serverless key-value and document database. It gives fast reads at any scale, but only for queries you planned for when designing keys.
- **Firebase (Cloud Firestore)** is a serverless document database for mobile and web apps, with real-time listeners, offline support and security rules.
- **Elasticsearch** is a search and analytics engine. It is great at full-text search, filtering and aggregations, but it is usually not the main source of truth.

## 3: How do the core terms map between the databases?

| MongoDB      | SQL                 | BigQuery          | Redis                   | Snowflake                  | DynamoDB             | Firebase           | Elasticsearch       |
| ------------ | ------------------- | ----------------- | ----------------------- | -------------------------- | -------------------- | ------------------ | ------------------- |
| Database     | Database / schema   | Dataset           | Logical DB number       | Database + schema          | (account + region)   | Firestore database | Cluster             |
| Collection   | Table               | Table             | Key prefix              | Table                      | Table                | Collection         | Index               |
| Document     | Row                 | Row               | Hash or JSON value      | Row                        | Item                 | Document           | Document            |
| Field        | Column              | Column            | Hash field / path       | Column                     | Attribute            | Field              | Field               |
| `_id`        | Primary key         | (no enforced key) | Key name                | Primary key (not enforced) | Partition + sort key | Document ID        | `_id`               |
| Embedded doc | Joined table / JSON | `STRUCT`          | Nested JSON             | `OBJECT` / `VARIANT`       | Map                  | Map                | `object` / `nested` |
| Array        | Child table / array | `ARRAY`           | List / set / JSON array | `ARRAY`                    | List / set           | Array              | Array (any field)   |

## 4: How do you connect from Node.js to each database?

**MongoDB**

```js
import { MongoClient } from "mongodb";
const client = new MongoClient(process.env.MONGODB_URI);
const db = client.db("shop");
```

**SQL**

```js
import pg from "pg";
const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const { rows } = await pool.query("SELECT now()");
```

**BigQuery**

```js
import { BigQuery } from "@google-cloud/bigquery";
const bigquery = new BigQuery(); // uses Application Default Credentials
const [rows] = await bigquery.query({ query: "SELECT 1 AS ok" });
```

**Redis**

```js
import { createClient } from "redis";
const redis = await createClient({ url: process.env.REDIS_URL })
  .on("error", (err) => console.error(err))
  .connect();
```

**Snowflake**

```js
import snowflake from "snowflake-sdk";
const conn = snowflake.createConnection({
  account: process.env.SF_ACCOUNT,
  username: process.env.SF_USER,
  password: process.env.SF_PASSWORD,
  warehouse: "APP_WH",
  database: "SHOP",
  schema: "PUBLIC",
});
await conn.connectAsync();
```

**DynamoDB**

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient } from "@aws-sdk/lib-dynamodb";
const ddb = DynamoDBDocumentClient.from(
  new DynamoDBClient({ region: "us-east-1" }),
);
```

**Firebase**

```js
import { initializeApp } from "firebase-admin/app";
import { getFirestore } from "firebase-admin/firestore";
initializeApp();
const firestore = getFirestore();
```

**Elasticsearch**

```js
import { Client } from "@elastic/elasticsearch";
const es = new Client({
  node: process.env.ELASTIC_URL,
  auth: { apiKey: process.env.ELASTIC_API_KEY },
});
```

The MongoDB driver connects lazily on the first operation. DynamoDB, BigQuery and Firestore talk HTTPS to a managed API, so there is no connection to open yourself.

## 5: How do you create a database?

**MongoDB**

```js
const db = client.db("shop"); // created on first write
```

**SQL**

```sql
CREATE DATABASE shop;
```

**BigQuery**

```sql
CREATE SCHEMA shop OPTIONS (location = "US"); -- a dataset
```

**Redis**

```js
// No CREATE. A Redis server has numbered logical databases (0-15 by default).
await redis.select(1);
```

**Snowflake**

```sql
CREATE DATABASE shop;
CREATE SCHEMA shop.app;
```

**DynamoDB**

There is no database level. Tables live directly in an AWS account and region.

**Firebase**

```bash
gcloud firestore databases create --database=shop --location=nam5
```

**Elasticsearch**

There is no database level. The cluster holds indices directly.

## 6: How do you create a collection or table?

**MongoDB**

```js
await db.createCollection("users"); // optional, insert also creates it
```

**SQL**

```sql
CREATE TABLE users (
  id         BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name       TEXT NOT NULL,
  email      TEXT UNIQUE NOT NULL,
  age        INT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

**BigQuery**

```sql
CREATE TABLE shop.users (
  id STRING NOT NULL,
  name STRING,
  email STRING,
  age INT64,
  created_at TIMESTAMP
);
```

**Redis**

```js
// No tables. You pick a key prefix like "user:" and optionally add a search index.
await redis.ft.create(
  "idx:users",
  {
    "$.name": { type: "TEXT", AS: "name" },
    "$.age": { type: "NUMERIC", AS: "age" },
  },
  { ON: "JSON", PREFIX: "user:" },
);
```

**Snowflake**

```sql
CREATE TABLE users (
  id NUMBER AUTOINCREMENT PRIMARY KEY,
  name VARCHAR NOT NULL,
  email VARCHAR,
  age NUMBER,
  created_at TIMESTAMP_TZ DEFAULT CURRENT_TIMESTAMP()
);
```

**DynamoDB**

```js
import { DynamoDBClient, CreateTableCommand } from "@aws-sdk/client-dynamodb";
await new DynamoDBClient({}).send(
  new CreateTableCommand({
    TableName: "Users",
    AttributeDefinitions: [{ AttributeName: "id", AttributeType: "S" }],
    KeySchema: [{ AttributeName: "id", KeyType: "HASH" }],
    BillingMode: "PAY_PER_REQUEST",
  }),
);
```

**Firebase**

A collection exists as soon as you write the first document into it.

**Elasticsearch**

```js
await es.indices.create({
  index: "users",
  mappings: {
    properties: {
      name: { type: "text" },
      email: { type: "keyword" },
      age: { type: "integer" },
      createdAt: { type: "date" },
    },
  },
});
```

## 7: How do you insert one document?

**MongoDB**

```js
await db
  .collection("users")
  .insertOne({ name: "Ana", email: "ana@example.com", age: 30 });
```

**SQL**

```sql
INSERT INTO users (name, email, age) VALUES ('Ana', 'ana@example.com', 30);
```

**BigQuery**

```sql
INSERT INTO shop.users (id, name, email, age, created_at)
VALUES (GENERATE_UUID(), 'Ana', 'ana@example.com', 30, CURRENT_TIMESTAMP());
```

**Redis**

```js
await redis.json.set("user:1", "$", {
  name: "Ana",
  email: "ana@example.com",
  age: 30,
});
// or as a flat hash:
await redis.hSet("user:1", { name: "Ana", email: "ana@example.com", age: 30 });
```

**Snowflake**

```sql
INSERT INTO users (name, email, age) VALUES ('Ana', 'ana@example.com', 30);
```

**DynamoDB**

```js
import { PutCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(
  new PutCommand({
    TableName: "Users",
    Item: { id: "u1", name: "Ana", email: "ana@example.com", age: 30 },
  }),
);
```

**Firebase**

```js
await firestore
  .collection("users")
  .add({ name: "Ana", email: "ana@example.com", age: 30 });
```

**Elasticsearch**

```js
await es.index({
  index: "users",
  document: { name: "Ana", email: "ana@example.com", age: 30 },
});
```

## 8: How do you insert many documents at once?

**MongoDB**

```js
await db.collection("users").insertMany([{ name: "Ana" }, { name: "Ben" }]);
```

**SQL**

```sql
INSERT INTO users (name, email) VALUES ('Ana', 'ana@example.com'), ('Ben', 'ben@example.com');
```

**BigQuery**

```sql
INSERT INTO shop.users (id, name) VALUES (GENERATE_UUID(), 'Ana'), (GENERATE_UUID(), 'Ben');
```

**Redis**

```js
await redis
  .multi()
  .json.set("user:1", "$", { name: "Ana" })
  .json.set("user:2", "$", { name: "Ben" })
  .exec();
```

**Snowflake**

```sql
INSERT INTO users (name) VALUES ('Ana'), ('Ben');
```

**DynamoDB**

```js
import { BatchWriteCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(
  new BatchWriteCommand({
    RequestItems: {
      Users: [
        { PutRequest: { Item: { id: "u1", name: "Ana" } } },
        { PutRequest: { Item: { id: "u2", name: "Ben" } } },
      ],
    },
  }),
);
```

**Firebase**

```js
const batch = firestore.batch();
batch.set(firestore.collection("users").doc(), { name: "Ana" });
batch.set(firestore.collection("users").doc(), { name: "Ben" });
await batch.commit();
```

**Elasticsearch**

```js
await es.bulk({
  operations: [
    { index: { _index: "users" } },
    { name: "Ana" },
    { index: { _index: "users" } },
    { name: "Ben" },
  ],
});
```

`BatchWriteItem` takes at most 25 items per call, and it can return `UnprocessedItems` that you must retry. For big loads in BigQuery and Snowflake, use load jobs or `COPY INTO` instead of `INSERT`.

## 9: How do you find a document by its id?

**MongoDB**

```js
import { ObjectId } from "mongodb";
const user = await db.collection("users").findOne({ _id: new ObjectId(id) });
```

**SQL**

```sql
SELECT * FROM users WHERE id = 42;
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE id = 'u1';
```

**Redis**

```js
const user = await redis.json.get("user:1");
```

**Snowflake**

```sql
SELECT * FROM users WHERE id = 42;
```

**DynamoDB**

```js
import { GetCommand } from "@aws-sdk/lib-dynamodb";
const { Item } = await ddb.send(
  new GetCommand({ TableName: "Users", Key: { id: "u1" } }),
);
```

**Firebase**

```js
const snap = await firestore.collection("users").doc("u1").get();
const user = snap.exists ? snap.data() : null;
```

**Elasticsearch**

```js
const { _source } = await es.get({ index: "users", id: "u1" });
```

In BigQuery this scans the table (or the partitions and clusters it can prune), because there is no primary key index for fast lookups. That is fine for analytics but not for serving a web page.

## 10: How do you find all documents?

**MongoDB**

```js
const users = await db.collection("users").find().toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users;
```

**Redis**

```js
const result = await redis.ft.search("idx:users", "*");
// without an index you would SCAN keys: for await (const keys of redis.scanIterator({ MATCH: "user:*" }))
```

**DynamoDB**

```js
import { ScanCommand } from "@aws-sdk/lib-dynamodb";
const { Items } = await ddb.send(new ScanCommand({ TableName: "Users" }));
```

**Firebase**

```js
const snap = await firestore.collection("users").get();
const users = snap.docs.map((d) => ({ id: d.id, ...d.data() }));
```

**Elasticsearch**

```js
const res = await es.search({ index: "users", query: { match_all: {} } });
```

Be careful in each database: a DynamoDB `Scan` returns at most 1 MB per page, Elasticsearch returns 10 hits by default, `FT.SEARCH` returns 10 by default, and `SELECT *` in BigQuery bills every column of the table.

## 11: How do you filter by equality on one field?

**MongoDB**

```js
await db.collection("users").find({ status: "active" }).toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE status = 'active';
```

**Redis**

```js
// status indexed as TAG
await redis.ft.search("idx:users", "@status:{active}");
```

**DynamoDB**

```js
// With a GSI on status (best):
await ddb.send(
  new QueryCommand({
    TableName: "Users",
    IndexName: "status-index",
    KeyConditionExpression: "#s = :s",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: { ":s": "active" },
  }),
);
```

**Firebase**

```js
await firestore.collection("users").where("status", "==", "active").get();
```

**Elasticsearch**

```js
await es.search({ index: "users", query: { term: { status: "active" } } });
```

In Elasticsearch, use `term` on `keyword` fields for exact matches. `match` is for analyzed full-text fields.

## 12: How do you filter with comparison operators like $gt and $lt?

**MongoDB**

```js
await db
  .collection("users")
  .find({ age: { $gte: 18, $lt: 65 } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE age >= 18 AND age < 65;
```

**Redis**

```js
await redis.ft.search("idx:users", "@age:[18 (65]");
```

**DynamoDB**

```js
// Only the sort key can use ranges in KeyConditionExpression. On other attributes use a filter.
await ddb.send(
  new ScanCommand({
    TableName: "Users",
    FilterExpression: "age BETWEEN :a AND :b",
    ExpressionAttributeValues: { ":a": 18, ":b": 64 },
  }),
);
```

**Firebase**

```js
await firestore
  .collection("users")
  .where("age", ">=", 18)
  .where("age", "<", 65)
  .get();
```

**Elasticsearch**

```js
await es.search({
  index: "users",
  query: { range: { age: { gte: 18, lt: 65 } } },
});
```

In RediSearch numeric ranges, `(` means "exclusive". A DynamoDB filter runs after the read, so you still pay for every item scanned.

## 13: How do you translate $in and $nin?

**MongoDB**

```js
await db
  .collection("users")
  .find({ status: { $in: ["active", "trial"] } })
  .toArray();
await db
  .collection("users")
  .find({ status: { $nin: ["banned"] } })
  .toArray();
```

**SQL, Snowflake**

```sql
SELECT * FROM users WHERE status IN ('active', 'trial');
SELECT * FROM users WHERE status NOT IN ('banned');
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE status IN UNNEST(@statuses); -- array query parameter
```

**Redis**

```js
await redis.ft.search("idx:users", "@status:{active | trial}");
await redis.ft.search("idx:users", "-@status:{banned}");
```

**DynamoDB**

```js
FilterExpression: "#s IN (:a, :b)",
ExpressionAttributeNames: { "#s": "status" },
ExpressionAttributeValues: { ":a": "active", ":b": "trial" },
```

**Firebase**

```js
firestore.collection("users").where("status", "in", ["active", "trial"]);
firestore.collection("users").where("status", "not-in", ["banned"]);
```

**Elasticsearch**

```js
query: {
  terms: {
    status: ["active", "trial"];
  }
}
query: {
  bool: {
    must_not: {
      terms: {
        status: ["banned"];
      }
    }
  }
}
```

Watch out for missing fields: MongoDB `$nin` matches documents without the field, SQL `NOT IN` skips `NULL` rows, and Firestore `not-in` skips documents where the field does not exist.

## 14: How do you translate $ne?

**MongoDB**

```js
await db
  .collection("users")
  .find({ status: { $ne: "banned" } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE status <> 'banned' OR status IS NULL;
```

**Redis**

```js
await redis.ft.search("idx:users", "-@status:{banned}");
```

**DynamoDB**

```js
FilterExpression: "#s <> :b",
ExpressionAttributeNames: { "#s": "status" },
ExpressionAttributeValues: { ":b": "banned" },
```

**Firebase**

```js
firestore.collection("users").where("status", "!=", "banned");
```

**Elasticsearch**

```js
query: {
  bool: {
    must_not: {
      term: {
        status: "banned";
      }
    }
  }
}
```

MongoDB `$ne` also returns documents without the field, so the SQL version needs `OR status IS NULL` to match it. Firestore `!=` does not return documents where the field is missing.

## 15: How do you combine conditions with AND?

**MongoDB**

```js
await db
  .collection("users")
  .find({ status: "active", age: { $gte: 18 } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE status = 'active' AND age >= 18;
```

**Redis**

```js
await redis.ft.search("idx:users", "@status:{active} @age:[18 +inf]"); // space means AND
```

**DynamoDB**

```js
FilterExpression: "#s = :s AND age >= :a",
ExpressionAttributeNames: { "#s": "status" },
ExpressionAttributeValues: { ":s": "active", ":a": 18 },
```

**Firebase**

```js
firestore
  .collection("users")
  .where("status", "==", "active")
  .where("age", ">=", 18);
```

**Elasticsearch**

```js
query: {
  bool: {
    filter: [{ term: { status: "active" } }, { range: { age: { gte: 18 } } }],
  },
}
```

Firestore needs a composite index for this query. The error message includes a link that creates it.

## 16: How do you translate $or?

**MongoDB**

```js
await db
  .collection("users")
  .find({ $or: [{ status: "vip" }, { age: { $gte: 65 } }] })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE status = 'vip' OR age >= 65;
```

**Redis**

```js
await redis.ft.search("idx:users", "(@status:{vip}) | (@age:[65 +inf])");
```

**DynamoDB**

```js
FilterExpression: "#s = :vip OR age >= :a",
ExpressionAttributeNames: { "#s": "status" },
ExpressionAttributeValues: { ":vip": "vip", ":a": 65 },
```

**Firebase**

```js
import { Filter } from "firebase-admin/firestore";
firestore
  .collection("users")
  .where(
    Filter.or(
      Filter.where("status", "==", "vip"),
      Filter.where("age", ">=", 65),
    ),
  );
```

**Elasticsearch**

```js
query: {
  bool: {
    should: [{ term: { status: "vip" } }, { range: { age: { gte: 65 } } }],
    minimum_should_match: 1,
  },
}
```

## 17: How do you select only some fields (projection)?

**MongoDB**

```js
await db
  .collection("users")
  .find({}, { projection: { name: 1, email: 1, _id: 0 } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT name, email FROM users;
```

**Redis**

```js
await redis.json.get("user:1", { path: ["$.name", "$.email"] });
await redis.hmGet("user:1", ["name", "email"]); // hash version
await redis.ft.search("idx:users", "*", { RETURN: ["name", "email"] });
```

**DynamoDB**

```js
new GetCommand({
  TableName: "Users",
  Key: { id: "u1" },
  ProjectionExpression: "#n, email",
  ExpressionAttributeNames: { "#n": "name" },
});
```

**Firebase**

```js
await firestore.collection("users").select("name", "email").get();
```

**Elasticsearch**

```js
await es.search({
  index: "users",
  _source: ["name", "email"],
  query: { match_all: {} },
});
```

In BigQuery and Snowflake, picking fewer columns also makes the query cheaper because both store data by column. In DynamoDB the read still costs the full item size.

## 18: How do you sort results?

**MongoDB**

```js
await db.collection("users").find().sort({ age: -1, name: 1 }).toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users ORDER BY age DESC, name ASC;
```

**Redis**

```js
await redis.ft.search("idx:users", "*", {
  SORTBY: { BY: "age", DIRECTION: "DESC" },
});
```

**DynamoDB**

```js
// Only by sort key, inside one partition. ScanIndexForward: false means descending.
new QueryCommand({
  TableName: "Orders",
  KeyConditionExpression: "userId = :u",
  ExpressionAttributeValues: { ":u": "u1" },
  ScanIndexForward: false,
});
```

**Firebase**

```js
firestore.collection("users").orderBy("age", "desc").orderBy("name");
```

**Elasticsearch**

```js
await es.search({
  index: "users",
  sort: [{ age: "desc" }, { "name.keyword": "asc" }],
});
```

DynamoDB cannot sort a `Scan` or by any attribute that is not a sort key. If you need another order, add a GSI with that attribute as its sort key, or sort in your code.

## 19: How do you limit the number of results?

**MongoDB**

```js
await db.collection("users").find().limit(10).toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users LIMIT 10;
```

**Redis**

```js
await redis.ft.search("idx:users", "*", { LIMIT: { from: 0, size: 10 } });
```

**DynamoDB**

```js
new QueryCommand({ /* ... */ Limit: 10 });
```

**Firebase**

```js
firestore.collection("users").limit(10);
```

**Elasticsearch**

```js
await es.search({ index: "users", size: 10 });
```

DynamoDB's `Limit` is the number of items it reads, not the number it returns after a `FilterExpression`. With a filter you can get fewer than 10 items and still have more pages. In BigQuery, `LIMIT` does not reduce the bytes billed on a normal table.

## 20: How do you skip results for simple paging?

**MongoDB**

```js
await db
  .collection("users")
  .find()
  .sort({ _id: 1 })
  .skip(20)
  .limit(10)
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 20;
```

**Redis**

```js
await redis.ft.search("idx:users", "*", { LIMIT: { from: 20, size: 10 } });
```

**Firebase**

```js
firestore.collection("users").orderBy("name").offset(20).limit(10); // billed for skipped docs too
```

**Elasticsearch**

```js
await es.search({ index: "users", from: 20, size: 10 });
```

DynamoDB has no offset. You page with `ExclusiveStartKey`, so skip-style paging is left out for it. In every database, offset paging gets slower as the offset grows; prefer cursor (keyset) paging for big lists.

## 21: How do you count documents?

**MongoDB**

```js
await db.collection("users").countDocuments({ status: "active" });
await db.collection("users").estimatedDocumentCount(); // fast, from metadata
```

**SQL, BigQuery, Snowflake**

```sql
SELECT COUNT(*) FROM users WHERE status = 'active';
```

**Redis**

```js
const { total } = await redis.ft.search("idx:users", "@status:{active}", {
  LIMIT: { from: 0, size: 0 },
});
```

**DynamoDB**

```js
const { Count } = await ddb.send(
  new ScanCommand({
    TableName: "Users",
    Select: "COUNT",
    FilterExpression: "#s = :s",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: { ":s": "active" },
  }),
); // per page; loop over LastEvaluatedKey for the full count
```

**Firebase**

```js
const snap = await firestore
  .collection("users")
  .where("status", "==", "active")
  .count()
  .get();
snap.data().count;
```

**Elasticsearch**

```js
const { count } = await es.count({
  index: "users",
  query: { term: { status: "active" } },
});
```

Counting in DynamoDB reads every matching item, so apps usually keep a counter item that they update on each write.

## 22: How do you check if a field exists ($exists)?

**MongoDB**

```js
await db
  .collection("users")
  .find({ phone: { $exists: true } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE phone IS NOT NULL;
```

**Redis**

```js
await redis.ft.search("idx:users", "-ismissing(@phone)", { DIALECT: 2 }); // field indexed with INDEXMISSING
await redis.hExists("user:1", "phone"); // one key
```

**DynamoDB**

```js
FilterExpression: "attribute_exists(phone)",
```

**Firebase**

```js
firestore.collection("users").orderBy("phone"); // only returns docs that have the field
```

**Elasticsearch**

```js
query: {
  exists: {
    field: "phone";
  }
}
```

SQL has fixed columns, so "missing" and "null" are the same thing: `NULL`. In MongoDB, DynamoDB and Firestore they are different.

## 23: How do you find documents where a field is null?

**MongoDB**

```js
await db.collection("users").find({ deletedAt: null }).toArray(); // null OR missing
await db
  .collection("users")
  .find({ deletedAt: { $type: "null" } })
  .toArray(); // only real null
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE deleted_at IS NULL;
```

**DynamoDB**

```js
FilterExpression: "attribute_not_exists(deletedAt) OR attribute_type(deletedAt, :null)",
ExpressionAttributeValues: { ":null": "NULL" },
```

**Firebase**

```js
firestore.collection("users").where("deletedAt", "==", null); // only docs with an explicit null
```

Firestore cannot query for documents where a field is missing, so store an explicit `null` if you need to find them.

**Elasticsearch**

```js
query: {
  bool: {
    must_not: {
      exists: {
        field: "deletedAt";
      }
    }
  }
} // null and missing look the same
```

`WHERE x = NULL` never matches in SQL; always use `IS NULL`. Redis has no null value, so you just don't store the field.

## 24: How do you update one field with $set?

**MongoDB**

```js
await db
  .collection("users")
  .updateOne({ _id: id }, { $set: { status: "active" } });
```

**SQL, Snowflake**

```sql
UPDATE users SET status = 'active' WHERE id = 42;
```

**BigQuery**

```sql
UPDATE shop.users SET status = 'active' WHERE id = 'u1';
```

**Redis**

```js
await redis.json.set("user:1", "$.status", "active");
await redis.hSet("user:1", "status", "active"); // hash version
```

**DynamoDB**

```js
import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { id: "u1" },
    UpdateExpression: "SET #s = :s",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: { ":s": "active" },
  }),
);
```

**Firebase**

```js
await firestore.collection("users").doc("u1").update({ status: "active" });
```

**Elasticsearch**

```js
await es.update({ index: "users", id: "u1", doc: { status: "active" } });
```

BigQuery DML works, but each statement rewrites data files and has quotas, so it is meant for batch changes, not for updating rows one at a time from an API.

## 25: How do you update many documents?

**MongoDB**

```js
await db
  .collection("users")
  .updateMany({ lastLogin: { $lt: cutoff } }, { $set: { status: "inactive" } });
```

**SQL, BigQuery, Snowflake**

```sql
UPDATE users SET status = 'inactive' WHERE last_login < '2026-01-01';
```

**Redis**

```js
const { documents } = await redis.ft.search(
  "idx:users",
  "@lastLogin:[-inf 1767225600]",
  {
    LIMIT: { from: 0, size: 1000 },
  },
);
const tx = redis.multi();
for (const d of documents) tx.json.set(d.id, "$.status", "inactive");
await tx.exec();
```

**DynamoDB**

There is no update-many. Query or scan for the keys, then send one `UpdateCommand` per item (or `TransactWriteCommand` for up to 100 items that must change together).

**Firebase**

```js
const snap = await firestore
  .collection("users")
  .where("lastLogin", "<", cutoff)
  .get();
const writer = firestore.bulkWriter();
snap.docs.forEach((d) => writer.update(d.ref, { status: "inactive" }));
await writer.close();
```

**Elasticsearch**

```js
await es.updateByQuery({
  index: "users",
  query: { range: { lastLogin: { lt: "2026-01-01" } } },
  script: { source: "ctx._source.status = 'inactive'" },
});
```

## 26: How do you increment a number with $inc?

**MongoDB**

```js
await db.collection("posts").updateOne({ _id: id }, { $inc: { views: 1 } });
```

**SQL, BigQuery, Snowflake**

```sql
UPDATE posts SET views = views + 1 WHERE id = 42;
```

**Redis**

```js
await redis.hIncrBy("post:42", "views", 1);
await redis.json.numIncrBy("post:42", "$.views", 1); // JSON version
await redis.incr("post:42:views"); // plain counter key
```

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Posts",
  Key: { id: "p42" },
  UpdateExpression: "ADD views :one",
  ExpressionAttributeValues: { ":one": 1 },
});
```

**Firebase**

```js
import { FieldValue } from "firebase-admin/firestore";
await firestore.doc("posts/p42").update({ views: FieldValue.increment(1) });
```

**Elasticsearch**

```js
await es.update({
  index: "posts",
  id: "p42",
  script: { source: "ctx._source.views += params.n", params: { n: 1 } },
});
```

All of these are atomic on the server, so two requests at the same time do not lose an increment. Don't read the value, add one in Node.js and write it back.

## 27: How do you remove a field with $unset?

**MongoDB**

```js
await db.collection("users").updateOne({ _id: id }, { $unset: { phone: "" } });
```

**SQL, BigQuery, Snowflake**

```sql
UPDATE users SET phone = NULL WHERE id = 42;
-- to remove the column from the whole table:
ALTER TABLE users DROP COLUMN phone;
```

**Redis**

```js
await redis.hDel("user:1", "phone");
await redis.json.del("user:1", { path: "$.phone" });
```

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Users",
  Key: { id: "u1" },
  UpdateExpression: "REMOVE phone",
});
```

**Firebase**

```js
await firestore.doc("users/u1").update({ phone: FieldValue.delete() });
```

**Elasticsearch**

```js
await es.update({
  index: "users",
  id: "u1",
  script: { source: "ctx._source.remove('phone')" },
});
```

## 28: How do you replace a whole document?

**MongoDB**

```js
await db
  .collection("users")
  .replaceOne({ _id: id }, { name: "Ana", email: "ana@new.com" });
```

**SQL, Snowflake**

```sql
UPDATE users SET name = 'Ana', email = 'ana@new.com', age = NULL, phone = NULL WHERE id = 42;
```

**BigQuery**

```sql
UPDATE shop.users SET name = 'Ana', email = 'ana@new.com', age = NULL WHERE id = 'u1';
```

**Redis**

```js
await redis.json.set("user:1", "$", { name: "Ana", email: "ana@new.com" });
```

**DynamoDB**

```js
await ddb.send(
  new PutCommand({
    TableName: "Users",
    Item: { id: "u1", name: "Ana", email: "ana@new.com" },
  }),
);
```

**Firebase**

```js
await firestore.doc("users/u1").set({ name: "Ana", email: "ana@new.com" }); // without { merge: true }
```

**Elasticsearch**

```js
await es.index({
  index: "users",
  id: "u1",
  document: { name: "Ana", email: "ana@new.com" },
});
```

`PutItem`, Firestore `set()` and Elasticsearch `index` with an id all overwrite the whole record, just like `replaceOne`. A plain Redis `HSET` does not: it only changes the fields you pass, so delete the key first if you want a true replace of a hash.

## 29: How do you delete one document?

**MongoDB**

```js
await db.collection("users").deleteOne({ _id: id });
```

**SQL, BigQuery, Snowflake**

```sql
DELETE FROM users WHERE id = 42;
```

**Redis**

```js
await redis.del("user:1");
```

**DynamoDB**

```js
import { DeleteCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(new DeleteCommand({ TableName: "Users", Key: { id: "u1" } }));
```

**Firebase**

```js
await firestore.doc("users/u1").delete();
```

**Elasticsearch**

```js
await es.delete({ index: "users", id: "u1" });
```

Deleting a Firestore document does not delete its subcollections. You have to delete those separately, for example with `firestore.recursiveDelete(ref)`.

## 30: How do you delete many documents?

**MongoDB**

```js
await db.collection("sessions").deleteMany({ expiresAt: { $lt: new Date() } });
```

**SQL, BigQuery, Snowflake**

```sql
DELETE FROM sessions WHERE expires_at < CURRENT_TIMESTAMP;
```

**Redis**

```js
for await (const keys of redis.scanIterator({
  MATCH: "session:*",
  COUNT: 500,
})) {
  if (keys.length) await redis.unlink(keys);
}
```

**DynamoDB**

Query or scan the keys, then send `BatchWriteCommand` with `DeleteRequest` entries, 25 at a time. Better: set a TTL attribute and let DynamoDB delete expired items for free.

**Firebase**

```js
const snap = await firestore
  .collection("sessions")
  .where("expiresAt", "<", new Date())
  .get();
const writer = firestore.bulkWriter();
snap.docs.forEach((d) => writer.delete(d.ref));
await writer.close();
```

**Elasticsearch**

```js
await es.deleteByQuery({
  index: "sessions",
  query: { range: { expiresAt: { lt: "now" } } },
});
```

In node-redis v5, `scanIterator` yields arrays of keys. `UNLINK` frees memory in the background, so it is safer than `DEL` for big values.

## 31: How do you delete all documents but keep the collection?

**MongoDB**

```js
await db.collection("logs").deleteMany({});
```

**SQL, BigQuery, Snowflake**

```sql
TRUNCATE TABLE logs;
```

**Redis**

```js
await redis.flushDb(); // only if this logical DB holds nothing else
```

**DynamoDB**

No truncate. Either scan and delete every item, or delete and re-create the table (usually faster and cheaper).

**Firebase**

```js
await firestore.recursiveDelete(firestore.collection("logs"));
```

**Elasticsearch**

```js
await es.deleteByQuery({ index: "logs", query: { match_all: {} } });
```

## 32: How do you drop a collection?

**MongoDB**

```js
await db.collection("logs").drop();
```

**SQL, BigQuery, Snowflake**

```sql
DROP TABLE logs;
```

**Redis**

```js
await redis.ft.dropIndex("idx:logs", { DD: true }); // DD also deletes the indexed keys
```

**DynamoDB**

```js
import { DynamoDBClient, DeleteTableCommand } from "@aws-sdk/client-dynamodb";
await new DynamoDBClient({}).send(
  new DeleteTableCommand({ TableName: "Logs" }),
);
```

**Firebase**

```js
await firestore.recursiveDelete(firestore.collection("logs")); // a collection disappears when it is empty
```

**Elasticsearch**

```js
await es.indices.delete({ index: "logs" });
```

Snowflake keeps dropped tables for the time travel period, so `UNDROP TABLE logs;` can bring one back.

## 33: What replaces the _id field and ObjectId?

| MongoDB                     | SQL                  | BigQuery                                | Redis                             | Snowflake                    | DynamoDB                   | Firebase             | Elasticsearch        |
| --------------------------- | -------------------- | --------------------------------------- | --------------------------------- | ---------------------------- | -------------------------- | -------------------- | -------------------- |
| `_id` (ObjectId by default) | `PRIMARY KEY` column | No real key, often a `STRING` id column | Part of the key name, `user:<id>` | `PRIMARY KEY` (not enforced) | Partition key (+ sort key) | Document ID (string) | `_id` metadata field |

An ObjectId is 12 bytes: a timestamp, a random value and a counter. When you move data out, you can keep it as a 24-character hex string, which works everywhere, or switch to the target's own ids. If other records point to it, keep the old value at least during the migration so references still match.

## 34: How do you generate ids in each database?

**MongoDB**

```js
import { ObjectId } from "mongodb";
const id = new ObjectId(); // or let the driver add _id on insert
```

**SQL**

```sql
id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
-- or
id UUID PRIMARY KEY DEFAULT gen_random_uuid()
```

**BigQuery**

```sql
SELECT GENERATE_UUID() AS id;
```

**Redis**

```js
const id = await redis.incr("seq:user"); // simple counter
const key = `user:${crypto.randomUUID()}`; // or a UUID
```

**Snowflake**

```sql
id NUMBER AUTOINCREMENT
-- or
SELECT UUID_STRING();
```

**DynamoDB**

```js
const id = crypto.randomUUID(); // DynamoDB never generates ids for you
```

**Firebase**

```js
const ref = firestore.collection("users").doc(); // random 20-character id
```

**Elasticsearch**

```js
await es.index({ index: "users", document: { name: "Ana" } }); // auto _id when id is omitted
```

Snowflake `AUTOINCREMENT` values are unique but not guaranteed to be gap-free or in order.

## 35: How do data types map between the databases?

| MongoDB (BSON) | SQL (PostgreSQL)    | BigQuery               | Redis                   | Snowflake          | DynamoDB                | Firebase                           | Elasticsearch                  |
| -------------- | ------------------- | ---------------------- | ----------------------- | ------------------ | ----------------------- | ---------------------------------- | ------------------------------ |
| String         | `TEXT` / `VARCHAR`  | `STRING`               | string                  | `VARCHAR`          | `S`                     | string                             | `text` / `keyword`             |
| Int32 / Int64  | `INT` / `BIGINT`    | `INT64`                | string (number in JSON) | `NUMBER(38,0)`     | `N`                     | integer                            | `integer` / `long`             |
| Double         | `DOUBLE PRECISION`  | `FLOAT64`              | string / JSON number    | `FLOAT`            | `N`                     | double                             | `double`                       |
| Decimal128     | `NUMERIC`           | `NUMERIC`/`BIGNUMERIC` | string                  | `NUMBER(p,s)`      | `N` (38 digits)         | (store as string or integer cents) | `scaled_float`                 |
| Boolean        | `BOOLEAN`           | `BOOL`                 | "0"/"1" or JSON boolean | `BOOLEAN`          | `BOOL`                  | boolean                            | `boolean`                      |
| Date           | `TIMESTAMPTZ`       | `TIMESTAMP`            | Unix time number        | `TIMESTAMP_TZ`     | ISO string or epoch `N` | timestamp                          | `date`                         |
| ObjectId       | `CHAR(24)` / `UUID` | `STRING`               | string                  | `VARCHAR`          | `S`                     | document id                        | `keyword`                      |
| Embedded doc   | `JSONB` / table     | `STRUCT` / `JSON`      | JSON object / hash      | `OBJECT`/`VARIANT` | `M` (map)               | map                                | `object` / `nested`            |
| Array          | array / table       | `ARRAY`                | list / set / JSON array | `ARRAY`            | `L`, `SS`, `NS`         | array                              | any field can hold many values |
| Binary         | `BYTEA`             | `BYTES`                | string (binary safe)    | `BINARY`           | `B`                     | bytes                              | `binary`                       |

## 36: How do you store dates and timestamps?

**MongoDB**

```js
await db.collection("events").insertOne({ type: "login", at: new Date() });
```

**SQL**

```sql
CREATE TABLE events (type TEXT, at TIMESTAMPTZ DEFAULT now());
```

**BigQuery**

```sql
CREATE TABLE shop.events (type STRING, at TIMESTAMP);
```

**Redis**

```js
await redis.hSet("event:1", { type: "login", at: Date.now() }); // epoch ms, easy to range-query
```

**Snowflake**

```sql
CREATE TABLE events (type VARCHAR, at TIMESTAMP_TZ DEFAULT CURRENT_TIMESTAMP());
```

**DynamoDB**

```js
Item: { id: "e1", type: "login", at: new Date().toISOString() } // ISO strings sort correctly as text
```

**Firebase**

```js
await firestore
  .collection("events")
  .add({ type: "login", at: FieldValue.serverTimestamp() });
```

**Elasticsearch**

```js
await es.index({
  index: "events",
  document: { type: "login", at: new Date().toISOString() },
});
```

DynamoDB has no date type, so pick one format (ISO 8601 string or epoch seconds) and stick to it. TTL attributes must be epoch seconds.

## 37: How do you store money and decimal numbers?

**MongoDB**

```js
import { Decimal128 } from "mongodb";
await db
  .collection("orders")
  .insertOne({ total: Decimal128.fromString("19.99") });
```

**SQL**

```sql
total NUMERIC(12, 2)
```

**BigQuery**

```sql
total NUMERIC
```

**Redis**

```js
await redis.hSet("order:1", "totalCents", 1999); // store integer cents
```

**Snowflake**

```sql
total NUMBER(12, 2)
```

**DynamoDB**

```js
Item: { id: "o1", totalCents: 1999 } // N is exact up to 38 digits, but JS numbers are doubles
```

**Firebase**

```js
await firestore.collection("orders").add({ totalCents: 1999 });
```

**Elasticsearch**

```js
mappings: { properties: { total: { type: "scaled_float", scaling_factor: 100 } } }
```

Storing money as integer cents is the simplest choice that works the same in every database and avoids floating point errors in JavaScript.

## 38: How do you store a nested object (embedded document)?

**MongoDB**

```js
await db
  .collection("users")
  .insertOne({ name: "Ana", address: { city: "Tbilisi", zip: "0100" } });
```

**SQL**

```sql
-- flat columns
CREATE TABLE users (id BIGINT PRIMARY KEY, name TEXT, address_city TEXT, address_zip TEXT);
-- or a JSONB column
CREATE TABLE users (id BIGINT PRIMARY KEY, name TEXT, address JSONB);
```

**BigQuery**

```sql
CREATE TABLE shop.users (id STRING, name STRING, address STRUCT<city STRING, zip STRING>);
```

**Redis**

```js
await redis.json.set("user:1", "$", {
  name: "Ana",
  address: { city: "Tbilisi", zip: "0100" },
});
```

**Snowflake**

```sql
CREATE TABLE users (id NUMBER, name VARCHAR, address OBJECT);
INSERT INTO users SELECT 1, 'Ana', OBJECT_CONSTRUCT('city', 'Tbilisi', 'zip', '0100');
```

**DynamoDB**

```js
Item: { id: "u1", name: "Ana", address: { city: "Tbilisi", zip: "0100" } } // stored as a map (M)
```

**Firebase**

```js
await firestore
  .collection("users")
  .add({ name: "Ana", address: { city: "Tbilisi", zip: "0100" } });
```

**Elasticsearch**

```js
await es.index({
  index: "users",
  document: { name: "Ana", address: { city: "Tbilisi", zip: "0100" } },
});
```

A Redis hash is flat, so for nested data use JSON, or flatten the keys (`address.city`) yourself.

## 39: How do you query a nested field with dot notation?

**MongoDB**

```js
await db.collection("users").find({ "address.city": "Tbilisi" }).toArray();
```

**SQL**

```sql
SELECT * FROM users WHERE address_city = 'Tbilisi';
SELECT * FROM users WHERE address->>'city' = 'Tbilisi'; -- JSONB
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE address.city = 'Tbilisi';
```

**Redis**

```js
// index "$.address.city" AS city (TAG)
await redis.ft.search("idx:users", "@city:{Tbilisi}");
```

**Snowflake**

```sql
SELECT * FROM users WHERE address:city::STRING = 'Tbilisi';
```

**DynamoDB**

```js
FilterExpression: "address.city = :c",
ExpressionAttributeValues: { ":c": "Tbilisi" },
```

**Firebase**

```js
firestore.collection("users").where("address.city", "==", "Tbilisi");
```

**Elasticsearch**

```js
query: { term: { "address.city": "Tbilisi" } }
```

In Snowflake, `:` reads a path inside a `VARIANT` or `OBJECT`, and `::STRING` casts it, so the comparison is between strings.

## 40: How do you store an array?

**MongoDB**

```js
await db.collection("posts").insertOne({ title: "Hi", tags: ["db", "node"] });
```

**SQL**

```sql
CREATE TABLE posts (id BIGINT PRIMARY KEY, title TEXT, tags TEXT[]);
-- or the normalized way: a post_tags(post_id, tag) table
```

**BigQuery**

```sql
CREATE TABLE shop.posts (id STRING, title STRING, tags ARRAY<STRING>);
```

**Redis**

```js
await redis.sAdd("post:1:tags", ["db", "node"]); // set
await redis.json.set("post:1", "$", { title: "Hi", tags: ["db", "node"] }); // JSON array
```

**Snowflake**

```sql
CREATE TABLE posts (id NUMBER, title VARCHAR, tags ARRAY);
INSERT INTO posts SELECT 1, 'Hi', ARRAY_CONSTRUCT('db', 'node');
```

**DynamoDB**

```js
Item: { id: "p1", title: "Hi", tags: ["db", "node"] } // list (L)
Item: { id: "p1", title: "Hi", tags: new Set(["db", "node"]) } // string set (SS), no duplicates
```

**Firebase**

```js
await firestore.collection("posts").add({ title: "Hi", tags: ["db", "node"] });
```

**Elasticsearch**

```js
await es.index({
  index: "posts",
  document: { title: "Hi", tags: ["db", "node"] },
});
```

Elasticsearch has no array type. Any field can hold one or many values of its mapped type.

## 41: How do you find documents where an array contains a value?

**MongoDB**

```js
await db.collection("posts").find({ tags: "node" }).toArray();
```

**SQL**

```sql
SELECT * FROM posts WHERE 'node' = ANY(tags);
SELECT * FROM posts WHERE tags @> ARRAY['node']; -- can use a GIN index
```

**BigQuery**

```sql
SELECT * FROM shop.posts WHERE 'node' IN UNNEST(tags);
```

**Redis**

```js
// "$.tags[*]" indexed AS tags (TAG)
await redis.ft.search("idx:posts", "@tags:{node}");
```

**Snowflake**

```sql
SELECT * FROM posts WHERE ARRAY_CONTAINS('node'::VARIANT, tags);
```

**DynamoDB**

```js
FilterExpression: "contains(tags, :t)",
ExpressionAttributeValues: { ":t": "node" },
```

**Firebase**

```js
firestore.collection("posts").where("tags", "array-contains", "node");
```

**Elasticsearch**

```js
query: {
  term: {
    tags: "node";
  }
}
```

## 42: How do you translate $all?

**MongoDB**

```js
await db
  .collection("posts")
  .find({ tags: { $all: ["node", "db"] } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM posts WHERE tags @> ARRAY['node', 'db'];
```

**BigQuery**

```sql
SELECT * FROM shop.posts
WHERE (SELECT COUNT(DISTINCT t) FROM UNNEST(tags) t WHERE t IN ('node', 'db')) = 2;
```

**Redis**

```js
await redis.ft.search("idx:posts", "@tags:{node} @tags:{db}");
```

**Snowflake**

```sql
SELECT * FROM posts WHERE ARRAY_CONTAINS('node'::VARIANT, tags) AND ARRAY_CONTAINS('db'::VARIANT, tags);
```

**DynamoDB**

```js
FilterExpression: "contains(tags, :a) AND contains(tags, :b)",
ExpressionAttributeValues: { ":a": "node", ":b": "db" },
```

**Elasticsearch**

```js
query: {
  bool: {
    filter: [{ term: { tags: "node" } }, { term: { tags: "db" } }];
  }
}
```

Firestore allows only one `array-contains` per query. A common workaround is a map field like `tagMap: { node: true, db: true }` and two `==` filters on `tagMap.node` and `tagMap.db`.

## 43: How do you query by array length with $size?

**MongoDB**

```js
await db
  .collection("posts")
  .find({ tags: { $size: 3 } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM posts WHERE cardinality(tags) = 3;
```

**BigQuery**

```sql
SELECT * FROM shop.posts WHERE ARRAY_LENGTH(tags) = 3;
```

**Snowflake**

```sql
SELECT * FROM posts WHERE ARRAY_SIZE(tags) = 3;
```

**DynamoDB**

```js
FilterExpression: "size(tags) = :n",
ExpressionAttributeValues: { ":n": 3 },
```

**Elasticsearch**

```js
query: { script: { script: "doc['tags'].size() == 3" } } // slow, better to store tagCount
```

Firestore and Redis cannot filter by array length. In those, and in Elasticsearch, store a `tagCount` field next to the array and keep it updated.

## 44: How do you push a value to an array ($push)?

**MongoDB**

```js
await db
  .collection("posts")
  .updateOne({ _id: id }, { $push: { tags: "mongo" } });
```

**SQL**

```sql
UPDATE posts SET tags = array_append(tags, 'mongo') WHERE id = 1;
```

**BigQuery**

```sql
UPDATE shop.posts SET tags = ARRAY_CONCAT(tags, ['mongo']) WHERE id = 'p1';
```

**Redis**

```js
await redis.rPush("post:1:tags", "mongo");
await redis.json.arrAppend("post:1", "$.tags", "mongo");
```

**Snowflake**

```sql
UPDATE posts SET tags = ARRAY_APPEND(tags, 'mongo') WHERE id = 1;
```

**DynamoDB**

```js
UpdateExpression: "SET tags = list_append(if_not_exists(tags, :empty), :new)",
ExpressionAttributeValues: { ":new": ["mongo"], ":empty": [] },
```

**Firebase**

Firestore has no plain push that allows duplicates. Use `FieldValue.arrayUnion` (no duplicates) or read, change and write the array in a transaction.

**Elasticsearch**

```js
script: { source: "ctx._source.tags.add(params.t)", params: { t: "mongo" } }
```

## 45: How do you translate $addToSet?

**MongoDB**

```js
await db
  .collection("posts")
  .updateOne({ _id: id }, { $addToSet: { tags: "mongo" } });
```

**SQL**

```sql
UPDATE posts SET tags = array_append(tags, 'mongo') WHERE id = 1 AND NOT ('mongo' = ANY(tags));
```

**BigQuery**

```sql
UPDATE shop.posts SET tags = ARRAY_CONCAT(tags, ['mongo']) WHERE id = 'p1' AND 'mongo' NOT IN UNNEST(tags);
```

**Redis**

```js
await redis.sAdd("post:1:tags", "mongo"); // sets never hold duplicates
```

**Snowflake**

```sql
UPDATE posts SET tags = ARRAY_DISTINCT(ARRAY_APPEND(tags, 'mongo')) WHERE id = 1;
```

**DynamoDB**

```js
UpdateExpression: "ADD tags :t",
ExpressionAttributeValues: { ":t": new Set(["mongo"]) }, // tags must be a string set
```

**Firebase**

```js
await firestore
  .doc("posts/p1")
  .update({ tags: FieldValue.arrayUnion("mongo") });
```

**Elasticsearch**

```js
script: { source: "if (!ctx._source.tags.contains(params.t)) { ctx._source.tags.add(params.t) }", params: { t: "mongo" } }
```

## 46: How do you remove a value from an array with $pull?

**MongoDB**

```js
await db.collection("posts").updateOne({ _id: id }, { $pull: { tags: "old" } });
```

**SQL**

```sql
UPDATE posts SET tags = array_remove(tags, 'old') WHERE id = 1;
```

**BigQuery**

```sql
UPDATE shop.posts SET tags = ARRAY(SELECT t FROM UNNEST(tags) t WHERE t != 'old') WHERE id = 'p1';
```

**Redis**

```js
await redis.sRem("post:1:tags", "old");
await redis.lRem("post:1:tags-list", 0, "old"); // list: remove all copies
```

**Snowflake**

```sql
UPDATE posts SET tags = ARRAY_REMOVE(tags, 'old'::VARIANT) WHERE id = 1;
```

**DynamoDB**

```js
UpdateExpression: "DELETE tags :t",
ExpressionAttributeValues: { ":t": new Set(["old"]) }, // sets only; lists need REMOVE tags[2] by index
```

**Firebase**

```js
await firestore.doc("posts/p1").update({ tags: FieldValue.arrayRemove("old") });
```

**Elasticsearch**

```js
script: { source: "ctx._source.tags.removeIf(t -> t == params.t)", params: { t: "old" } }
```

## 47: How do you translate $pop (remove the first or last array item)?

**MongoDB**

```js
await db.collection("queues").updateOne({ _id: id }, { $pop: { items: 1 } }); // last; -1 for first
```

**SQL**

```sql
UPDATE queues SET items = items[1:cardinality(items) - 1] WHERE id = 1; -- drop last
```

**Redis**

```js
await redis.rPop("queue:1"); // last
await redis.lPop("queue:1"); // first
await redis.json.arrPop("queue:1", { path: "$.items" });
```

**Snowflake**

```sql
UPDATE queues SET items = ARRAY_SLICE(items, 0, ARRAY_SIZE(items) - 1) WHERE id = 1;
```

**DynamoDB**

```js
UpdateExpression: "REMOVE items[0]", // first; for the last you need its index
```

**Elasticsearch**

```js
script: {
  source: "ctx._source.items.remove(ctx._source.items.size() - 1)";
}
```

Redis lists are the most natural fit, because popping from either end is a single fast command.

## 48: How do you do a pattern or LIKE search ($regex)?

**MongoDB**

```js
await db
  .collection("users")
  .find({ email: { $regex: "^ana" } })
  .toArray();
```

**SQL, Snowflake**

```sql
SELECT * FROM users WHERE email LIKE 'ana%';
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE STARTS_WITH(email, 'ana');
SELECT * FROM shop.users WHERE REGEXP_CONTAINS(email, r'^ana');
```

**Redis**

```js
await redis.ft.search("idx:users", "@email:{ana*}"); // prefix on a TAG field
```

**DynamoDB**

```js
FilterExpression: "begins_with(email, :p)",
ExpressionAttributeValues: { ":p": "ana" },
```

**Firebase**

```js
firestore
  .collection("users")
  .where("email", ">=", "ana")
  .where("email", "<", "ana");
```

**Elasticsearch**

```js
query: {
  prefix: {
    email: "ana";
  }
}
query: {
  regexp: {
    email: "ana.*@example\\.com";
  }
}
```

A prefix pattern can use a normal index in MongoDB and SQL. A pattern that starts with a wildcard (`%ana%`) cannot, and in Firestore and DynamoDB it is not possible at all without a search service.

## 49: How do you do a case-insensitive match?

**MongoDB**

```js
await db
  .collection("users")
  .find({ name: { $regex: "^ana$", $options: "i" } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM users WHERE name ILIKE 'ana';
SELECT * FROM users WHERE lower(name) = lower('Ana'); -- can use an index on lower(name)
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE LOWER(name) = 'ana';
```

**Redis**

```js
await redis.ft.search("idx:users", "@name:ana"); // TEXT fields are case-insensitive
```

**Snowflake**

```sql
SELECT * FROM users WHERE name ILIKE 'ana';
```

**DynamoDB**

Store a lowercase copy (`nameLower`) on write and query it.

**Firebase**

Store a lowercase copy (`nameLower`) on write and query it with `==`.

**Elasticsearch**

```js
query: {
  match: {
    name: "ana";
  }
} // the standard analyzer lowercases text
```

In MongoDB, a case-insensitive regex cannot use an index well. A collation index (`{ locale: "en", strength: 2 }`) is the faster way.

## 50: How do you translate distinct()?

**MongoDB**

```js
await db.collection("users").distinct("country");
```

**SQL, BigQuery, Snowflake**

```sql
SELECT DISTINCT country FROM users;
```

**Redis**

```js
const res = await redis.ft.aggregate("idx:users", "*", {
  STEPS: [{ type: "GROUPBY", properties: "@country" }],
});
```

**Firebase**

No distinct. Read the documents and collect values in a `Set`, or keep a separate `countries` collection.

**Elasticsearch**

```js
await es.search({
  index: "users",
  size: 0,
  aggs: { countries: { terms: { field: "country", size: 500 } } },
});
```

DynamoDB has no distinct either. You scan and dedupe in code, or keep a separate item that lists the values.

## 51: How do you create a simple index?

**MongoDB**

```js
await db.collection("users").createIndex({ email: 1 });
```

**SQL**

```sql
CREATE INDEX users_email_idx ON users (email);
```

**BigQuery**

```sql
-- no B-tree indexes; cluster the table instead
CREATE TABLE shop.users_clustered CLUSTER BY email AS SELECT * FROM shop.users;
```

**Redis**

```js
await redis.ft.create(
  "idx:users",
  { "$.email": { type: "TAG", AS: "email" } },
  { ON: "JSON", PREFIX: "user:" },
);
```

**Snowflake**

```sql
-- no indexes on standard tables; use a clustering key or search optimization
ALTER TABLE users CLUSTER BY (email);
```

**DynamoDB**

```js
import { UpdateTableCommand } from "@aws-sdk/client-dynamodb";
new UpdateTableCommand({
  TableName: "Users",
  AttributeDefinitions: [{ AttributeName: "email", AttributeType: "S" }],
  GlobalSecondaryIndexUpdates: [
    {
      Create: {
        IndexName: "email-index",
        KeySchema: [{ AttributeName: "email", KeyType: "HASH" }],
        Projection: { ProjectionType: "ALL" },
      },
    },
  ],
});
```

**Firebase**

Firestore indexes every single field automatically. You only create composite indexes, in `firestore.indexes.json` or the console.

**Elasticsearch**

Every mapped field is indexed by default. You choose the field type in the mapping instead of creating indexes.

## 52: How do you create a unique index?

**MongoDB**

```js
await db.collection("users").createIndex({ email: 1 }, { unique: true });
```

**SQL**

```sql
CREATE UNIQUE INDEX users_email_key ON users (email);
```

**Redis**

```js
// SET with NX only succeeds if the key does not exist yet
const ok = await redis.set(`email:${email}`, userId, { NX: true });
```

**DynamoDB**

```js
// Make the unique value a key, and write it in the same transaction as the user
new TransactWriteCommand({
  TransactItems: [
    {
      Put: {
        TableName: "Users",
        Item: { id: "u1", email },
        ConditionExpression: "attribute_not_exists(id)",
      },
    },
    {
      Put: {
        TableName: "Emails",
        Item: { email, userId: "u1" },
        ConditionExpression: "attribute_not_exists(email)",
      },
    },
  ],
});
```

**Firebase**

```js
// Use the unique value as a document id; create() fails if it exists
await firestore.doc(`emails/${email}`).create({ userId: "u1" });
```

**Elasticsearch**

```js
await es.create({ index: "users", id: email, document: { email } }); // fails with 409 if the id exists
```

BigQuery and Snowflake do not enforce unique constraints. You can declare them, but duplicates are still accepted, so you check with a query or dedupe in `MERGE`.

## 53: How do you create a compound index?

**MongoDB**

```js
await db.collection("orders").createIndex({ userId: 1, createdAt: -1 });
```

**SQL**

```sql
CREATE INDEX orders_user_created_idx ON orders (user_id, created_at DESC);
```

**BigQuery**

```sql
CREATE TABLE shop.orders PARTITION BY DATE(created_at) CLUSTER BY user_id AS SELECT * FROM shop.orders_raw;
```

**Snowflake**

```sql
ALTER TABLE orders CLUSTER BY (user_id, created_at);
```

**DynamoDB**

```js
// partition key + sort key
KeySchema: [
  { AttributeName: "userId", KeyType: "HASH" },
  { AttributeName: "createdAt", KeyType: "RANGE" },
],
```

**Firebase**

```json
{
  "indexes": [
    {
      "collectionGroup": "orders",
      "queryScope": "COLLECTION",
      "fields": [
        { "fieldPath": "userId", "order": "ASCENDING" },
        { "fieldPath": "createdAt", "order": "DESCENDING" }
      ]
    }
  ]
}
```

A MongoDB compound index on `{ userId, createdAt }` maps most closely to a DynamoDB table or GSI with `userId` as partition key and `createdAt` as sort key. Redis and Elasticsearch don't need compound indexes because each field is indexed on its own.

## 54: How do you list indexes?

**MongoDB**

```js
await db.collection("users").indexes();
```

**SQL**

```sql
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';
```

**BigQuery**

```sql
SELECT table_name, clustering_ordinal_position, column_name
FROM shop.INFORMATION_SCHEMA.COLUMNS WHERE clustering_ordinal_position IS NOT NULL;
```

**Redis**

```js
await redis.ft._list();
await redis.ft.info("idx:users");
```

**Snowflake**

```sql
SHOW TABLES LIKE 'USERS'; -- cluster_by column
```

**DynamoDB**

```js
const { Table } = await new DynamoDBClient({}).send(
  new DescribeTableCommand({ TableName: "Users" }),
);
Table.GlobalSecondaryIndexes;
```

**Firebase**

```bash
firebase firestore:indexes
```

**Elasticsearch**

```js
await es.indices.getMapping({ index: "users" });
```

## 55: How do you drop an index?

**MongoDB**

```js
await db.collection("users").dropIndex("email_1");
```

**SQL**

```sql
DROP INDEX users_email_idx;
```

**Redis**

```js
await redis.ft.dropIndex("idx:users"); // keeps the data keys
```

**Snowflake**

```sql
ALTER TABLE users DROP CLUSTERING KEY;
```

**DynamoDB**

```js
GlobalSecondaryIndexUpdates: [{ Delete: { IndexName: "email-index" } }];
```

**Firebase**

Remove the index from `firestore.indexes.json` and run `firebase deploy --only firestore:indexes --force`, or delete it in the console.

**Elasticsearch**

You cannot un-index a single field in place. Create a new index with the new mapping and reindex into it.

## 56: How do you see the query plan (explain)?

**MongoDB**

```js
await db
  .collection("users")
  .find({ email: "a@b.com" })
  .explain("executionStats");
```

**SQL**

```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'a@b.com';
```

**BigQuery**

```bash
bq query --dry_run --use_legacy_sql=false 'SELECT * FROM shop.users' # bytes it would scan
```

**Redis**

```js
await redis.ft.explain("idx:users", "@status:{active} @age:[18 +inf]");
```

**Snowflake**

```sql
EXPLAIN SELECT * FROM users WHERE email = 'a@b.com';
```

**DynamoDB**

No explain. A `Query` reads one partition, a `Scan` reads the whole table. Check `ConsumedCapacity` with `ReturnConsumedCapacity: "TOTAL"`.

**Firebase**

```js
const res = await firestore
  .collection("users")
  .where("email", "==", "a@b.com")
  .explain({ analyze: true });
```

**Elasticsearch**

```js
await es.search({
  index: "users",
  profile: true,
  query: { term: { email: "a@b.com" } },
});
```

In BigQuery, the execution graph in the console after a run is the real plan. Snowflake also shows the Query Profile in Snowsight.

## 57: How do you translate an upsert?

**MongoDB**

```js
await db
  .collection("users")
  .updateOne({ email }, { $set: { name } }, { upsert: true });
```

**SQL**

```sql
INSERT INTO users (email, name) VALUES ($1, $2)
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;
```

**BigQuery**

```sql
MERGE shop.users t
USING (SELECT 'ana@example.com' AS email, 'Ana' AS name) s
ON t.email = s.email
WHEN MATCHED THEN UPDATE SET name = s.name
WHEN NOT MATCHED THEN INSERT (id, email, name) VALUES (GENERATE_UUID(), s.email, s.name);
```

**Redis**

```js
await redis.hSet(`user:${email}`, { name }); // HSET always upserts
```

**Snowflake**

```sql
MERGE INTO users t
USING (SELECT 'ana@example.com' AS email, 'Ana' AS name) s
ON t.email = s.email
WHEN MATCHED THEN UPDATE SET name = s.name
WHEN NOT MATCHED THEN INSERT (email, name) VALUES (s.email, s.name);
```

**DynamoDB**

```js
// UpdateItem creates the item if the key does not exist
new UpdateCommand({
  TableName: "Users",
  Key: { email },
  UpdateExpression: "SET #n = :n",
  ExpressionAttributeNames: { "#n": "name" },
  ExpressionAttributeValues: { ":n": name },
});
```

**Firebase**

```js
await firestore.doc(`users/${id}`).set({ name }, { merge: true });
```

**Elasticsearch**

```js
await es.update({ index: "users", id, doc: { name }, doc_as_upsert: true });
```

## 58: How do you translate findOneAndUpdate (get the updated document back)?

**MongoDB**

```js
const doc = await db
  .collection("users")
  .findOneAndUpdate(
    { _id: id },
    { $inc: { credits: -1 } },
    { returnDocument: "after" },
  );
```

**SQL**

```sql
UPDATE users SET credits = credits - 1 WHERE id = 42 RETURNING *;
```

**Redis**

```js
const credits = await redis.hIncrBy("user:42", "credits", -1); // returns the new value
```

**DynamoDB**

```js
const { Attributes } = await ddb.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { id: "u42" },
    UpdateExpression: "ADD credits :d",
    ExpressionAttributeValues: { ":d": -1 },
    ReturnValues: "ALL_NEW",
  }),
);
```

**Firebase**

```js
const user = await firestore.runTransaction(async (tx) => {
  const ref = firestore.doc("users/u42");
  const snap = await tx.get(ref);
  const credits = snap.get("credits") - 1;
  tx.update(ref, { credits });
  return { ...snap.data(), credits };
});
```

**Elasticsearch**

```js
const res = await es.update({
  index: "users",
  id: "u42",
  script: "ctx._source.credits -= 1",
  _source: true,
});
res.get._source;
```

BigQuery and Snowflake have no way to return updated rows from an `UPDATE`. You run a `SELECT` after it.

## 59: How do you translate findOneAndDelete?

**MongoDB**

```js
const job = await db
  .collection("jobs")
  .findOneAndDelete({ status: "ready" }, { sort: { createdAt: 1 } });
```

**SQL**

```sql
DELETE FROM jobs
WHERE id = (SELECT id FROM jobs WHERE status = 'ready' ORDER BY created_at LIMIT 1 FOR UPDATE SKIP LOCKED)
RETURNING *;
```

**Redis**

```js
const job = await redis.lPop("jobs:ready"); // take the oldest job
```

**DynamoDB**

```js
const { Attributes } = await ddb.send(
  new DeleteCommand({
    TableName: "Jobs",
    Key: { id: "j1" },
    ReturnValues: "ALL_OLD",
  }),
);
```

**Firebase**

```js
await firestore.runTransaction(async (tx) => {
  const snap = await tx.get(
    firestore
      .collection("jobs")
      .where("status", "==", "ready")
      .orderBy("createdAt")
      .limit(1),
  );
  if (snap.empty) return null;
  tx.delete(snap.docs[0].ref);
  return snap.docs[0].data();
});
```

## 60: How do you translate $setOnInsert?

**MongoDB**

```js
await db.collection("users").updateOne(
  { email },
  {
    $set: { lastLogin: new Date() },
    $setOnInsert: { createdAt: new Date() },
  },
  { upsert: true },
);
```

**SQL**

```sql
INSERT INTO users (email, last_login, created_at) VALUES ($1, now(), now())
ON CONFLICT (email) DO UPDATE SET last_login = EXCLUDED.last_login; -- created_at stays
```

**BigQuery, Snowflake**

```sql
MERGE INTO users t USING (SELECT 'ana@example.com' AS email) s ON t.email = s.email
WHEN MATCHED THEN UPDATE SET last_login = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN INSERT (email, last_login, created_at)
  VALUES (s.email, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());
```

**Redis**

```js
await redis.hSetNX(`user:${email}`, "createdAt", Date.now()); // only sets if field is missing
await redis.hSet(`user:${email}`, "lastLogin", Date.now());
```

**DynamoDB**

```js
UpdateExpression: "SET lastLogin = :now, createdAt = if_not_exists(createdAt, :now)",
ExpressionAttributeValues: { ":now": new Date().toISOString() },
```

**Elasticsearch**

```js
await es.update({
  index: "users",
  id: email,
  doc: { lastLogin: new Date() },
  upsert: { createdAt: new Date(), lastLogin: new Date() },
});
```

`if_not_exists` in DynamoDB is the closest match to `$setOnInsert`. In Elasticsearch, the `upsert` document is used only when the document does not exist yet.

## 61: How do you translate the $min and $max update operators?

**MongoDB**

```js
await db
  .collection("scores")
  .updateOne({ _id: id }, { $max: { best: 120 }, $min: { worst: 40 } });
```

**SQL**

```sql
UPDATE scores SET best = GREATEST(best, 120), worst = LEAST(worst, 40) WHERE id = 1;
```

**BigQuery, Snowflake**

```sql
UPDATE scores SET best = GREATEST(best, 120), worst = LEAST(worst, 40) WHERE id = 1;
```

**Redis**

```js
await redis.zAdd("leaderboard", { score: 120, value: "u1" }, { GT: true }); // only raises the score
```

**DynamoDB**

```js
// conditional write: only update if the new value is higher
UpdateExpression: "SET best = :v",
ConditionExpression: "attribute_not_exists(best) OR best < :v",
ExpressionAttributeValues: { ":v": 120 },
```

**Elasticsearch**

```js
script: { source: "ctx._source.best = Math.max(ctx._source.best, params.v)", params: { v: 120 } }
```

PostgreSQL `GREATEST` ignores `NULL` values, but in BigQuery and Snowflake it returns `NULL` if any argument is `NULL`. Wrap the column in `COALESCE` when it can be empty.

## 62: How do you translate $mul?

**MongoDB**

```js
await db.collection("products").updateMany({}, { $mul: { price: 1.1 } });
```

**SQL, BigQuery, Snowflake**

```sql
UPDATE products SET price = ROUND(price * 1.1, 2) WHERE TRUE;
```

**Redis**

Redis has no multiply command. Compute the new value in a Lua script (or with `WATCH` and `MULTI`) so the read and the write happen together.

**DynamoDB**

Read the value, compute it, and write it back with a `ConditionExpression` on the old value. `UpdateExpression` only supports `+` and `-`.

**Elasticsearch**

```js
await es.updateByQuery({
  index: "products",
  script: { source: "ctx._source.price *= 1.1" },
});
```

BigQuery requires a `WHERE` clause on every `UPDATE`, which is why `WHERE TRUE` is there.

## 63: How do you rename a field with $rename?

**MongoDB**

```js
await db.collection("users").updateMany({}, { $rename: { fullname: "name" } });
```

**SQL**

```sql
ALTER TABLE users RENAME COLUMN fullname TO name;
```

**BigQuery**

```sql
ALTER TABLE shop.users RENAME COLUMN fullname TO name;
```

**Redis**

No rename for hash fields. Read the value, `HSET` the new field and `HDEL` the old one in a `MULTI`.

**Snowflake**

```sql
ALTER TABLE users RENAME COLUMN fullname TO name;
```

**DynamoDB**

```js
UpdateExpression: "SET #new = #old REMOVE #old",
ExpressionAttributeNames: { "#new": "name", "#old": "fullname" },
```

**Firebase**

Read each document and write `{ name: data.fullname, fullname: FieldValue.delete() }` with a `BulkWriter`.

**Elasticsearch**

Add the new field to the mapping, then run `_update_by_query` with a script like `ctx._source.name = ctx._source.remove('fullname')`. For a clean result, reindex into a new index.

In SQL and the warehouses, renaming is a metadata change and is instant. In the document stores it means touching every item.

## 64: How do you translate $currentDate?

**MongoDB**

```js
await db
  .collection("users")
  .updateOne({ _id: id }, { $currentDate: { updatedAt: true } });
```

**SQL**

```sql
UPDATE users SET updated_at = now() WHERE id = 42;
```

**BigQuery, Snowflake**

```sql
UPDATE users SET updated_at = CURRENT_TIMESTAMP() WHERE id = 42;
```

**Redis**

```js
const [sec] = await redis.time(); // server time
await redis.hSet("user:42", "updatedAt", sec);
```

**DynamoDB**

```js
UpdateExpression: "SET updatedAt = :now",
ExpressionAttributeValues: { ":now": new Date().toISOString() }, // client time, DynamoDB has no server clock function
```

**Firebase**

```js
await firestore
  .doc("users/u42")
  .update({ updatedAt: FieldValue.serverTimestamp() });
```

**Elasticsearch**

Use an ingest pipeline with a `set` processor and `{{_ingest.timestamp}}`, or send the time from the app.

## 65: How does schemaless MongoDB compare to schemas in the other databases?

- **MongoDB:** flexible by default. Two documents in one collection can have different fields. You can add a `$jsonSchema` validator if you want rules.
- **SQL:** strict. Every column and type is declared up front, and changes need `ALTER TABLE`.
- **BigQuery:** strict schema, but you can add columns easily and use `JSON` or `STRUCT` columns for loose data.
- **Redis:** no schema at all. A search index defines which fields are indexed, but keys can hold anything.
- **Snowflake:** strict columns, plus `VARIANT` for semi-structured data you can query with paths.
- **DynamoDB:** only the key attributes are fixed. Every other attribute is free-form per item.
- **Firebase:** schemaless like MongoDB. Security rules can check fields and types on client writes.
- **Elasticsearch:** dynamic mapping guesses types for new fields, but once a field has a type it cannot change. Set `"dynamic": "strict"` to reject unknown fields.

So when you leave MongoDB, the hidden schema that lives in your code has to be written down somewhere: as DDL, as a mapping, or as validation code.

## 66: How do you add a new field to existing records?

**MongoDB**

```js
await db
  .collection("users")
  .updateMany({ plan: { $exists: false } }, { $set: { plan: "free" } });
```

**SQL**

```sql
ALTER TABLE users ADD COLUMN plan TEXT NOT NULL DEFAULT 'free';
```

**BigQuery**

```sql
ALTER TABLE shop.users ADD COLUMN plan STRING;
ALTER TABLE shop.users ALTER COLUMN plan SET DEFAULT 'free';
UPDATE shop.users SET plan = 'free' WHERE plan IS NULL;
```

**Snowflake**

```sql
ALTER TABLE users ADD COLUMN plan VARCHAR DEFAULT 'free';
```

**DynamoDB**

Nothing to change in the table. Write the field on new items and backfill old ones with a scan and `UpdateCommand`, or treat a missing value as `"free"` when reading.

**Firebase**

Same as DynamoDB: backfill with a `BulkWriter` or default it in code.

**Elasticsearch**

```js
await es.indices.putMapping({
  index: "users",
  properties: { plan: { type: "keyword" } },
});
```

In PostgreSQL 11+, adding a column with a constant default is instant and does not rewrite the table.

## 67: How do you rename a collection?

**MongoDB**

```js
await db.collection("people").rename("users");
```

**SQL, Snowflake**

```sql
ALTER TABLE people RENAME TO users;
```

**BigQuery**

```sql
ALTER TABLE shop.people RENAME TO users;
```

**Redis**

```js
await redis.rename("person:1", "user:1"); // one key at a time; also recreate the index with the new prefix
```

**Elasticsearch**

```js
await es.indices.updateAliases({
  actions: [{ add: { index: "people", alias: "users" } }],
});
```

DynamoDB tables and Firestore collections cannot be renamed. You copy the data to a new one. In Elasticsearch, an alias is the usual way to give an index a new name.

## 68: How do you query by field type with $type?

**MongoDB**

```js
await db
  .collection("users")
  .find({ age: { $type: "string" } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM users WHERE jsonb_typeof(data->'age') = 'string';
```

**BigQuery**

```sql
SELECT * FROM shop.raw_users WHERE JSON_TYPE(data.age) = 'string';
```

**Snowflake**

```sql
SELECT * FROM raw_users WHERE TYPEOF(data:age) = 'VARCHAR';
```

**DynamoDB**

```js
FilterExpression: "attribute_type(age, :t)",
ExpressionAttributeValues: { ":t": "S" },
```

In typed columns this question does not come up, because the column has one type. It only matters for JSON and `VARIANT` columns. Firestore and Elasticsearch cannot filter by type.

## 69: How do you filter by a range of dates?

**MongoDB**

```js
await db
  .collection("orders")
  .find({
    createdAt: { $gte: new Date("2026-01-01"), $lt: new Date("2026-02-01") },
  })
  .toArray();
```

**SQL, Snowflake**

```sql
SELECT * FROM orders WHERE created_at >= '2026-01-01' AND created_at < '2026-02-01';
```

**BigQuery**

```sql
SELECT * FROM shop.orders WHERE created_at >= TIMESTAMP '2026-01-01' AND created_at < TIMESTAMP '2026-02-01';
```

**Redis**

```js
await redis.zRangeByScore(
  "orders:byTime",
  Date.parse("2026-01-01"),
  Date.parse("2026-02-01") - 1,
);
```

**DynamoDB**

```js
KeyConditionExpression: "userId = :u AND createdAt BETWEEN :a AND :b",
ExpressionAttributeValues: { ":u": "u1", ":a": "2026-01-01", ":b": "2026-01-31T23:59:59Z" },
```

**Firebase**

```js
firestore
  .collection("orders")
  .where("createdAt", ">=", new Date("2026-01-01"))
  .where("createdAt", "<", new Date("2026-02-01"));
```

**Elasticsearch**

```js
query: { range: { createdAt: { gte: "2026-01-01", lt: "2026-02-01" } } }
```

Use half-open ranges (`>=` start and `<` end) so you never miss the last millisecond of a day.

## 70: How do you translate $not?

**MongoDB**

```js
await db
  .collection("users")
  .find({ age: { $not: { $gt: 30 } } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE NOT (age > 30) OR age IS NULL;
```

**Redis**

```js
await redis.ft.search("idx:users", "-@age:[(30 +inf]");
```

**DynamoDB**

```js
FilterExpression: "NOT (age > :a)",
ExpressionAttributeValues: { ":a": 30 },
```

**Elasticsearch**

```js
query: {
  bool: {
    must_not: {
      range: {
        age: {
          gt: 30;
        }
      }
    }
  }
}
```

Like `$ne`, `$not` also matches documents where the field is missing, so SQL needs the `IS NULL` part to return the same rows.

## 71: How do you translate $nor?

**MongoDB**

```js
await db
  .collection("users")
  .find({ $nor: [{ status: "banned" }, { age: { $lt: 18 } }] })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM users WHERE NOT (status = 'banned' OR age < 18);
```

**Redis**

```js
await redis.ft.search("idx:users", "-@status:{banned} -@age:[-inf (18]");
```

**DynamoDB**

```js
FilterExpression: "NOT (#s = :b OR age < :a)",
```

**Elasticsearch**

```js
query: {
  bool: {
    must_not: [{ term: { status: "banned" } }, { range: { age: { lt: 18 } } }];
  }
}
```

## 72: How do you compare two fields of the same document ($expr)?

**MongoDB**

```js
await db
  .collection("budgets")
  .find({ $expr: { $gt: ["$spent", "$limit"] } })
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM budgets WHERE spent > "limit"; -- limit is a reserved word, so it is quoted
```

**DynamoDB**

```js
FilterExpression: "spent > #l",
ExpressionAttributeNames: { "#l": "limit" },
```

**Elasticsearch**

```js
query: { script: { script: "doc['spent'].value > doc['limit'].value" } }
```

Firestore cannot compare two fields. Store a computed boolean like `overBudget` when you write the document. In BigQuery, quote reserved words with backticks instead of double quotes.

## 73: How do you translate a simple $group with $sum?

**MongoDB**

```js
await db
  .collection("orders")
  .aggregate([{ $group: { _id: "$userId", total: { $sum: "$amount" } } }])
  .toArray();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id;
```

**Redis**

```js
await redis.ft.aggregate("idx:orders", "*", {
  STEPS: [
    {
      type: "GROUPBY",
      properties: "@userId",
      REDUCE: [{ type: "SUM", property: "@amount", AS: "total" }],
    },
  ],
});
```

**Firebase**

```js
import { AggregateField } from "firebase-admin/firestore";
const snap = await firestore
  .collection("orders")
  .where("userId", "==", "u1")
  .aggregate({ total: AggregateField.sum("amount") })
  .get(); // one group per query
```

**Elasticsearch**

```js
await es.search({
  index: "orders",
  size: 0,
  aggs: {
    byUser: {
      terms: { field: "userId" },
      aggs: { total: { sum: { field: "amount" } } },
    },
  },
});
```

DynamoDB has no aggregation. You either sum in code after a query, or keep running totals that you update on each write.

## 74: How do you translate $match in an aggregation?

**MongoDB**

```js
[
  { $match: { status: "paid" } },
  { $group: { _id: "$userId", total: { $sum: "$amount" } } },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT user_id, SUM(amount) FROM orders WHERE status = 'paid' GROUP BY user_id;
-- a $match after $group becomes HAVING:
SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id HAVING SUM(amount) > 100;
```

**Redis**

```js
await redis.ft.aggregate("idx:orders", "@status:{paid}", {
  STEPS: [/* GROUPBY ... */],
});
```

**Elasticsearch**

```js
await es.search({
  index: "orders",
  size: 0,
  query: { term: { status: "paid" } },
  aggs: { byUser: { terms: { field: "userId" } } },
});
```

Where `$match` sits in the pipeline decides the SQL clause: before `$group` it is `WHERE`, after it is `HAVING`.

## 75: How do you translate $project in an aggregation?

**MongoDB**

```js
[{ $project: { _id: 0, name: 1, yearlyPay: { $multiply: ["$salary", 12] } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT name, salary * 12 AS yearly_pay FROM employees;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "@salary * 12", AS: "yearlyPay" }];
```

**Elasticsearch**

```js
await es.search({
  index: "employees",
  _source: ["name"],
  script_fields: { yearlyPay: { script: "doc['salary'].value * 12" } },
});
```

DynamoDB and Firestore can only pick fields, not compute new ones. Do the math in code after reading.

## 76: How do you get the top N groups with $sort and $limit?

**MongoDB**

```js
[
  { $group: { _id: "$productId", sold: { $sum: "$qty" } } },
  { $sort: { sold: -1 } },
  { $limit: 5 },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT product_id, SUM(qty) AS sold FROM order_items GROUP BY product_id ORDER BY sold DESC LIMIT 5;
```

**Redis**

```js
// keep a sorted set updated on each sale, then read the top 5
await redis.zIncrBy("sold", 2, "p1");
await redis.zRangeWithScores("sold", 0, 4, { REV: true });
```

**Elasticsearch**

```js
aggs: { top: { terms: { field: "productId", size: 5, order: { sold: "desc" } }, aggs: { sold: { sum: { field: "qty" } } } } }
```

Elasticsearch `terms` results on a multi-shard index are approximate for very large numbers of groups. Increase `shard_size` if the exact order matters.

## 77: How do you compute an average with $avg?

**MongoDB**

```js
[{ $group: { _id: "$category", avgPrice: { $avg: "$price" } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT category, AVG(price) AS avg_price FROM products GROUP BY category;
```

**Redis**

```js
STEPS: [
  {
    type: "GROUPBY",
    properties: "@category",
    REDUCE: [{ type: "AVG", property: "@price", AS: "avgPrice" }],
  },
];
```

**Firebase**

```js
await firestore
  .collection("products")
  .where("category", "==", "books")
  .aggregate({ avgPrice: AggregateField.average("price") })
  .get();
```

**Elasticsearch**

```js
aggs: { byCat: { terms: { field: "category" }, aggs: { avgPrice: { avg: { field: "price" } } } } }
```

## 78: How do you get the min and max per group?

**MongoDB**

```js
[
  {
    $group: {
      _id: "$category",
      cheapest: { $min: "$price" },
      priciest: { $max: "$price" },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT category, MIN(price) AS cheapest, MAX(price) AS priciest FROM products GROUP BY category;
```

**Redis**

```js
REDUCE: [
  { type: "MIN", property: "@price", AS: "cheapest" },
  { type: "MAX", property: "@price", AS: "priciest" },
];
```

**Firebase**

```js
// no min/max aggregation; sort and take one
await firestore
  .collection("products")
  .where("category", "==", "books")
  .orderBy("price")
  .limit(1)
  .get();
```

**Elasticsearch**

```js
aggs: { byCat: { terms: { field: "category" }, aggs: { stats: { stats: { field: "price" } } } } } // min, max, avg, sum, count
```

## 79: How do you count documents per group?

**MongoDB**

```js
[{ $group: { _id: "$status", n: { $sum: 1 } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT status, COUNT(*) AS n FROM orders GROUP BY status;
```

**Redis**

```js
STEPS: [
  {
    type: "GROUPBY",
    properties: "@status",
    REDUCE: [{ type: "COUNT", AS: "n" }],
  },
];
```

**Firebase**

One `count()` query per status value: `where("status", "==", s).count().get()`.

**Elasticsearch**

```js
aggs: {
  byStatus: {
    terms: {
      field: "status";
    }
  }
} // each bucket has doc_count
```

## 80: How do you translate $unwind?

**MongoDB**

```js
[{ $unwind: "$tags" }, { $group: { _id: "$tags", n: { $sum: 1 } } }];
```

**SQL**

```sql
SELECT tag, COUNT(*) FROM posts, unnest(tags) AS tag GROUP BY tag;
```

**BigQuery**

```sql
SELECT tag, COUNT(*) AS n FROM shop.posts, UNNEST(tags) AS tag GROUP BY tag;
```

**Snowflake**

```sql
SELECT f.value::STRING AS tag, COUNT(*) AS n
FROM posts, LATERAL FLATTEN(input => tags) f
GROUP BY tag;
```

**Elasticsearch**

```js
aggs: {
  tags: {
    terms: {
      field: "tags";
    }
  }
} // terms on an array field counts each value
```

`unnest` and `FLATTEN` drop rows with empty arrays by default, the same as `$unwind`. Use `LEFT JOIN ... ON TRUE` in SQL or `OUTER => TRUE` in Snowflake to keep them, like `preserveNullAndEmptyArrays`.

## 81: How do you translate $lookup (a basic join)?

**MongoDB**

```js
[
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user",
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT o.*, u.name FROM orders o LEFT JOIN users u ON u.id = o.user_id;
```

**Redis**

```js
const order = await redis.json.get("order:1");
const user = await redis.json.get(`user:${order.userId}`); // join in code
```

**DynamoDB**

```js
// Put orders under the user's partition, then one Query returns both
KeyConditionExpression: "pk = :pk",
ExpressionAttributeValues: { ":pk": "USER#u1" }, // returns the PROFILE item and ORDER# items
```

**Firebase**

```js
const order = (await firestore.doc("orders/o1").get()).data();
const user = (await firestore.doc(`users/${order.userId}`).get()).data();
```

**Elasticsearch**

Copy the fields you need (like `user.name`) into each order document when indexing. Elasticsearch has no general join at query time.

## 82: How do you translate $addFields (or $set) in a pipeline?

**MongoDB**

```js
[{ $addFields: { total: { $multiply: ["$price", "$qty"] } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT *, price * qty AS total FROM order_items;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "@price * @qty", AS: "total" }];
```

**Elasticsearch**

```js
runtime_mappings: { total: { type: "double", script: "emit(doc['price'].value * doc['qty'].value)" } },
fields: ["total"],
```

BigQuery also has `SELECT * REPLACE (price * 1.2 AS price)` for overwriting one column, which is close to `$set` on an existing field.

## 83: How do you translate the $count stage?

**MongoDB**

```js
[{ $match: { status: "paid" } }, { $count: "paidOrders" }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT COUNT(*) AS paid_orders FROM orders WHERE status = 'paid';
```

**Redis**

```js
const { total } = await redis.ft.search("idx:orders", "@status:{paid}", {
  LIMIT: { from: 0, size: 0 },
});
```

**Firebase**

```js
(
  await firestore
    .collection("orders")
    .where("status", "==", "paid")
    .count()
    .get()
).data().count;
```

**Elasticsearch**

```js
await es.count({ index: "orders", query: { term: { status: "paid" } } });
```

## 84: How do you join strings with $concat?

**MongoDB**

```js
[{ $project: { fullName: { $concat: ["$first", " ", "$last"] } } }];
```

**SQL, Snowflake**

```sql
SELECT first || ' ' || last AS full_name FROM users;
SELECT CONCAT_WS(' ', first, last) AS full_name FROM users; -- skips NULLs
```

**BigQuery**

```sql
SELECT CONCAT(first, ' ', last) AS full_name FROM shop.users;
```

**Redis**

```js
STEPS: [
  {
    type: "APPLY",
    expression: 'format("%s %s", @first, @last)',
    AS: "fullName",
  },
];
```

**Elasticsearch**

```js
runtime_mappings: { fullName: { type: "keyword", script: "emit(doc['first'].value + ' ' + doc['last'].value)" } }
```

`$concat` returns `null` if any part is `null`, and so do `||` and `CONCAT` in most SQL dialects. Wrap parts in `COALESCE` if needed.

## 85: How do you change string case ($toUpper, $toLower)?

**MongoDB**

```js
[{ $project: { code: { $toUpper: "$code" }, email: { $toLower: "$email" } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT UPPER(code) AS code, LOWER(email) AS email FROM coupons;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "upper(@code)", AS: "code" }];
```

**Elasticsearch**

Use a `lowercase` normalizer on a `keyword` field so values are lowercased at index time and search time.

## 86: How do you take part of a string ($substrCP)?

**MongoDB**

```js
[{ $project: { prefix: { $substrCP: ["$sku", 0, 3] } } }];
```

**SQL**

```sql
SELECT substring(sku FROM 1 FOR 3) AS prefix FROM products;
```

**BigQuery**

```sql
SELECT SUBSTR(sku, 1, 3) AS prefix FROM shop.products;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "substr(@sku, 0, 3)", AS: "prefix" }];
```

**Snowflake**

```sql
SELECT SUBSTR(sku, 1, 3) AS prefix FROM products;
```

**Elasticsearch**

```js
runtime_mappings: { prefix: { type: "keyword", script: "emit(doc['sku'].value.substring(0, 3))" } }
```

MongoDB and Redis count from 0. SQL, BigQuery and Snowflake count from 1.

## 87: How do you translate $cond (if/else)?

**MongoDB**

```js
[
  {
    $project: { size: { $cond: [{ $gte: ["$total", 100] }, "big", "small"] } },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT CASE WHEN total >= 100 THEN 'big' ELSE 'small' END AS size FROM orders;
-- BigQuery and Snowflake also have IF / IFF:
SELECT IF(total >= 100, 'big', 'small') FROM shop.orders;   -- BigQuery
SELECT IFF(total >= 100, 'big', 'small') FROM orders;       -- Snowflake
```

**Redis**

```js
STEPS: [
  {
    type: "APPLY",
    expression: 'if(@total >= 100, "big", "small")',
    AS: "size",
  },
];
```

**Elasticsearch**

```js
runtime_mappings: { size: { type: "keyword", script: "emit(doc['total'].value >= 100 ? 'big' : 'small')" } }
```

## 88: How do you translate $ifNull?

**MongoDB**

```js
[{ $project: { nickname: { $ifNull: ["$nickname", "$name"] } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT COALESCE(nickname, name) AS nickname FROM users;
```

**Elasticsearch**

```js
runtime_mappings: {
  nick: { type: "keyword", script: "emit(doc['nickname'].size() > 0 ? doc['nickname'].value : doc['name'].value)" },
}
```

In DynamoDB, `if_not_exists(nickname, :default)` works only inside an `UpdateExpression`, not in reads. For reads, apply the fallback in code.

## 89: How do you format dates with $dateToString?

**MongoDB**

```js
[
  {
    $project: {
      day: { $dateToString: { format: "%Y-%m-%d", date: "$createdAt" } },
    },
  },
];
```

**SQL**

```sql
SELECT to_char(created_at, 'YYYY-MM-DD') AS day FROM orders;
```

**BigQuery**

```sql
SELECT FORMAT_TIMESTAMP('%Y-%m-%d', created_at) AS day FROM shop.orders;
```

**Snowflake**

```sql
SELECT TO_CHAR(created_at, 'YYYY-MM-DD') AS day FROM orders;
```

**Elasticsearch**

```js
fields: [{ field: "createdAt", format: "yyyy-MM-dd" }],
```

BigQuery uses the same `%Y-%m-%d` style codes as MongoDB. PostgreSQL and Snowflake use `YYYY-MM-DD` style patterns.

## 90: How do you extract the year and month from a date?

**MongoDB**

```js
[{ $project: { y: { $year: "$createdAt" }, m: { $month: "$createdAt" } } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT EXTRACT(YEAR FROM created_at) AS y, EXTRACT(MONTH FROM created_at) AS m FROM orders;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "year(@createdAt)", AS: "y" }]; // createdAt in epoch seconds
```

**Elasticsearch**

```js
runtime_mappings: { y: { type: "long", script: "emit(doc['createdAt'].value.getYear())" } }
```

## 91: How do you do math in queries ($add, $multiply, $round)?

**MongoDB**

```js
[
  {
    $project: {
      gross: { $round: [{ $multiply: [{ $add: ["$net", "$fee"] }, 1.18] }, 2] },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT ROUND((net + fee) * 1.18, 2) AS gross FROM invoices;
```

**Redis**

```js
STEPS: [
  {
    type: "APPLY",
    expression: "floor((@net + @fee) * 118) / 100",
    AS: "gross",
  },
];
```

**Elasticsearch**

```js
script_fields: {
  gross: {
    script: "Math.round((doc['net'].value + doc['fee'].value) * 118) / 100.0";
  }
}
```

MongoDB `$round` uses "round half to even" for `.5` values, while SQL `ROUND` rounds half away from zero, so a few edge values can differ.

## 92: How do you expire data automatically (TTL index)?

**MongoDB**

```js
await db
  .collection("sessions")
  .createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });
```

**SQL**

```sql
-- no built-in TTL; schedule a delete (pg_cron)
SELECT cron.schedule('0 * * * *', $$DELETE FROM sessions WHERE created_at < now() - interval '1 hour'$$);
```

**BigQuery**

```sql
ALTER TABLE shop.events SET OPTIONS (partition_expiration_days = 90);
```

**Redis**

```js
await redis.set("session:abc", "u1", { EX: 3600 });
await redis.expire("user:1:cart", 86400);
```

**Snowflake**

```sql
CREATE TASK purge_sessions WAREHOUSE = app_wh SCHEDULE = '60 MINUTE'
AS DELETE FROM sessions WHERE created_at < DATEADD(hour, -1, CURRENT_TIMESTAMP());
```

**DynamoDB**

```js
Item: { id: "s1", userId: "u1", expiresAt: Math.floor(Date.now() / 1000) + 3600 }; // TTL attribute, epoch seconds
```

**Firebase**

```bash
gcloud firestore fields ttls update expiresAt --collection-group=sessions --enable-ttl
```

**Elasticsearch**

Use index lifecycle management (ILM) or a data stream retention to delete whole indices by age. Elasticsearch has no per-document TTL.

TTL deletes in MongoDB, DynamoDB and Firestore run in the background and can lag behind (DynamoDB says within a few days, Firestore usually within 24 hours). Filter out expired items in queries if that matters.

## 93: How do you translate capped collections?

**MongoDB**

```js
await db.createCollection("recentLogs", {
  capped: true,
  size: 1_000_000,
  max: 1000,
});
```

**SQL**

```sql
-- delete old rows after insert, keeping the newest 1000
DELETE FROM recent_logs WHERE id <= (SELECT id FROM recent_logs ORDER BY id DESC OFFSET 1000 LIMIT 1);
```

**Redis**

```js
await redis.lPush("logs:recent", JSON.stringify(entry));
await redis.lTrim("logs:recent", 0, 999); // keep only the newest 1000
await redis.xAdd(
  "logs",
  "*",
  { msg: "hi" },
  { TRIM: { strategy: "MAXLEN", threshold: 1000, strategyModifier: "~" } },
);
```

**Elasticsearch**

Use a data stream with a short retention period.

Redis `LPUSH` + `LTRIM`, or a stream with `MAXLEN`, is the most direct match. MongoDB itself now suggests TTL indexes over capped collections for most cases.

## 94: How do you store a location point?

**MongoDB**

```js
await db.collection("shops").insertOne({
  name: "Cafe",
  location: { type: "Point", coordinates: [44.79, 41.71] },
});
await db.collection("shops").createIndex({ location: "2dsphere" });
```

**SQL**

```sql
CREATE EXTENSION postgis;
CREATE TABLE shops (id BIGINT PRIMARY KEY, name TEXT, location geography(Point, 4326));
INSERT INTO shops VALUES (1, 'Cafe', ST_MakePoint(44.79, 41.71));
```

**BigQuery**

```sql
INSERT INTO shop.shops (name, location) VALUES ('Cafe', ST_GEOGPOINT(44.79, 41.71));
```

**Redis**

```js
await redis.geoAdd("shops", {
  longitude: 44.79,
  latitude: 41.71,
  member: "cafe",
});
```

**Snowflake**

```sql
INSERT INTO shops (name, location) SELECT 'Cafe', ST_MAKEPOINT(44.79, 41.71);
```

**Firebase**

```js
import { GeoPoint } from "firebase-admin/firestore";
await firestore
  .collection("shops")
  .add({ name: "Cafe", location: new GeoPoint(41.71, 44.79) });
```

**Elasticsearch**

```js
mappings: {
  properties: {
    location: {
      type: "geo_point";
    }
  }
}
await es.index({
  index: "shops",
  document: { name: "Cafe", location: { lat: 41.71, lon: 44.79 } },
});
```

GeoJSON, PostGIS, BigQuery, Snowflake and Redis take longitude first. Firestore `GeoPoint` takes latitude first. Mixing this up is a very common bug. DynamoDB has no geo type, so you store a geohash string and query by its prefix.

## 95: How do you do a basic full-text search ($text)?

**MongoDB**

```js
await db.collection("posts").createIndex({ title: "text", body: "text" });
await db
  .collection("posts")
  .find({ $text: { $search: "mongodb index" } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM posts
WHERE to_tsvector('english', title || ' ' || body) @@ websearch_to_tsquery('english', 'mongodb index');
```

**BigQuery**

```sql
SELECT * FROM shop.posts WHERE SEARCH(body, 'mongodb index');
```

**Redis**

```js
await redis.ft.search("idx:posts", "mongodb index");
```

**Snowflake**

```sql
SELECT * FROM posts WHERE SEARCH(body, 'mongodb index');
```

**Elasticsearch**

```js
await es.search({
  index: "posts",
  query: { multi_match: { query: "mongodb index", fields: ["title", "body"] } },
});
```

Firestore and DynamoDB have no full-text search. The usual answer is to sync data into Elasticsearch, Algolia or Typesense.

## 96: How do you bulk load data like mongoimport?

**MongoDB**

```bash
mongoimport --uri "$MONGODB_URI" --collection users --file users.json --jsonArray
```

**SQL**

```sql
\copy users (name, email) FROM 'users.csv' WITH (FORMAT csv, HEADER true)
```

**BigQuery**

```bash
bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect shop.users gs://my-bucket/users.json
```

**Redis**

```bash
cat commands.txt | redis-cli --pipe
```

**Snowflake**

```sql
PUT file://users.json @~/staged;
COPY INTO users FROM @~/staged FILE_FORMAT = (TYPE = JSON) MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
```

**DynamoDB**

```bash
aws dynamodb import-table --s3-bucket-source S3Bucket=my-bucket,S3KeyPrefix=users/ \
  --input-format DYNAMODB_JSON --table-creation-parameters file://table.json
```

**Firebase**

```bash
gcloud firestore import gs://my-bucket/2026-11-26 # only for files made by a Firestore export
```

**Elasticsearch**

```js
await es.helpers.bulk({
  datasource: users,
  onDocument: () => ({ index: { _index: "users" } }),
});
```

DynamoDB import from S3 always creates a new table. To load JSON into Firestore that was not exported from Firestore, write a script with `BulkWriter`.

## 97: How do you export data like mongoexport?

**MongoDB**

```bash
mongoexport --uri "$MONGODB_URI" --collection users --out users.json
```

**SQL**

```sql
\copy (SELECT * FROM users) TO 'users.csv' WITH (FORMAT csv, HEADER true)
```

**BigQuery**

```sql
EXPORT DATA OPTIONS (uri = 'gs://my-bucket/users-*.json', format = 'JSON') AS SELECT * FROM shop.users;
```

**Redis**

```bash
redis-cli --scan --pattern 'user:*' | while read k; do redis-cli JSON.GET "$k"; done > users.jsonl
```

**Snowflake**

```sql
COPY INTO @~/export/users FROM users FILE_FORMAT = (TYPE = JSON);
```

**DynamoDB**

```bash
aws dynamodb export-table-to-point-in-time --table-arn "$TABLE_ARN" --s3-bucket my-bucket --export-format DYNAMODB_JSON
```

**Firebase**

```bash
gcloud firestore export gs://my-bucket --collection-ids=users
```

**Elasticsearch**

Page through with `search_after` and a point in time and write the hits to a file, or snapshot the index to a repository.

Snowflake `COPY INTO` a location needs the data as a single `VARIANT` column for JSON, for example `SELECT OBJECT_CONSTRUCT(*) FROM users`.

## 98: How do you back up and restore like mongodump and mongorestore?

| MongoDB                                     | SQL                                         | BigQuery                                    | Redis                        | Snowflake                      | DynamoDB                          | Firebase                        | Elasticsearch            |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ---------------------------- | ------------------------------ | --------------------------------- | ------------------------------- | ------------------------ |
| `mongodump` / `mongorestore`, Atlas backups | `pg_dump` / `pg_restore`, managed snapshots | Table snapshots, time travel (up to 7 days) | RDB snapshot (`BGSAVE`), AOF | Time travel, fail-safe, clones | On-demand backups, PITR (35 days) | Scheduled backups, PITR, export | Snapshot and restore API |

```bash
pg_dump -Fc -d shop -f shop.dump && pg_restore -d shop_copy shop.dump
aws dynamodb create-backup --table-name Users --backup-name users-2026-11-26
gcloud firestore backups schedules create --database='(default)' --recurrence=daily --retention=7d
```

## 99: What command-line shells replace mongosh?

**MongoDB**

```bash
mongosh "$MONGODB_URI"
```

**SQL**

```bash
psql "$DATABASE_URL"
```

**BigQuery**

```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM shop.users'
```

**Redis**

```bash
redis-cli -u "$REDIS_URL"
```

**Snowflake**

```bash
snow sql -q "SELECT CURRENT_VERSION()" # Snowflake CLI; SnowSQL is the older tool
```

**DynamoDB**

```bash
aws dynamodb get-item --table-name Users --key '{"id":{"S":"u1"}}'
```

**Firebase**

```bash
firebase firestore:delete users/u1 # the Firebase CLI has few data commands; most work is done in code or the console
```

**Elasticsearch**

```bash
curl -H "Authorization: ApiKey $ELASTIC_API_KEY" "$ELASTIC_URL/users/_search?q=name:ana"
```

## 100: What GUI tools replace MongoDB Compass?

- **MongoDB:** Compass, Atlas Data Explorer.
- **SQL:** pgAdmin, DBeaver, DataGrip, TablePlus.
- **BigQuery:** the BigQuery Studio page in the Google Cloud console.
- **Redis:** Redis Insight.
- **Snowflake:** Snowsight (the web UI) with worksheets and notebooks.
- **DynamoDB:** the AWS console item explorer and NoSQL Workbench for modeling.
- **Firebase:** the Firebase console data viewer and the Emulator Suite UI.
- **Elasticsearch:** Kibana, mainly Discover and Dev Tools.

DBeaver and DataGrip can also connect to BigQuery and Snowflake, which helps if your team already uses them for SQL.

## 101: How do you create a user and grant access?

**MongoDB**

```js
await db.command({
  createUser: "app",
  pwd: process.env.APP_PWD,
  roles: [{ role: "readWrite", db: "shop" }],
});
```

**SQL**

```sql
CREATE ROLE app LOGIN PASSWORD 'secret';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app;
```

**BigQuery**

```bash
bq add-iam-policy-binding --member=serviceAccount:app@proj.iam.gserviceaccount.com \
  --role=roles/bigquery.dataEditor shop.users
```

**Redis**

```js
await redis.sendCommand([
  "ACL",
  "SETUSER",
  "app",
  "on",
  ">secret",
  "~user:*",
  "+@read",
  "+@write",
]);
```

**Snowflake**

```sql
CREATE ROLE app_rw;
GRANT USAGE ON DATABASE shop TO ROLE app_rw;
GRANT USAGE ON SCHEMA shop.public TO ROLE app_rw;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA shop.public TO ROLE app_rw;
CREATE USER app TYPE = SERVICE DEFAULT_ROLE = app_rw;
GRANT ROLE app_rw TO USER app;
```

**DynamoDB**

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem",
    "dynamodb:PutItem",
    "dynamodb:UpdateItem",
    "dynamodb:Query"
  ],
  "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Users"
}
```

**Firebase**

Server code uses a service account with an IAM role like `roles/datastore.user`. Client apps are controlled with security rules, not users.

**Elasticsearch**

```js
await es.security.putRole({
  name: "users_rw",
  indices: [{ names: ["users"], privileges: ["read", "write"] }],
});
await es.security.putUser({
  username: "app",
  password: "secret",
  roles: ["users_rw"],
});
```

## 102: How do built-in roles like read and readWrite translate?

| MongoDB     | SQL                              | BigQuery                    | Redis ACL        | Snowflake                     | DynamoDB (IAM)                             | Firebase (IAM)           | Elasticsearch     |
| ----------- | -------------------------------- | --------------------------- | ---------------- | ----------------------------- | ------------------------------------------ | ------------------------ | ----------------- |
| `read`      | `GRANT SELECT`                   | `roles/bigquery.dataViewer` | `+@read`         | `GRANT SELECT`                | `dynamodb:GetItem`, `Query`, `Scan`        | `roles/datastore.viewer` | `read` privilege  |
| `readWrite` | `SELECT, INSERT, UPDATE, DELETE` | `roles/bigquery.dataEditor` | `+@read +@write` | plus `INSERT, UPDATE, DELETE` | plus `PutItem`, `UpdateItem`, `DeleteItem` | `roles/datastore.user`   | `read`, `write`   |
| `dbAdmin`   | Table owner                      | `roles/bigquery.admin`      | `+@admin`        | `OWNERSHIP` on schema         | `dynamodb:*` on the table                  | `roles/datastore.owner`  | `manage` on index |

BigQuery also needs `roles/bigquery.jobUser` on the project to run queries at all. That surprises many people coming from MongoDB.

## 103: How do you run a local instance for development?

```bash
docker run -d -p 27017:27017 mongo:8                         # MongoDB
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=dev postgres:17 # SQL
docker run -d -p 9050:9050 ghcr.io/goccy/bigquery-emulator --project=dev # BigQuery (community emulator)
docker run -d -p 6379:6379 redis:8                           # Redis
docker run -d -p 8000:8000 amazon/dynamodb-local             # DynamoDB
firebase emulators:start --only firestore                    # Firebase
docker run -d -p 9200:9200 -e discovery.type=single-node \
  -e xpack.security.enabled=false docker.elastic.co/elasticsearch/elasticsearch:9.2.0 # Elasticsearch
```

Snowflake has no local version. Teams use a separate dev database or a zero-copy clone of production. Point the clients at the local endpoints, for example `new DynamoDBClient({ endpoint: "http://localhost:8000" })` or `FIRESTORE_EMULATOR_HOST=localhost:8080`.

## 104: How do connection strings compare?

| Database      | Example                                                                |
| ------------- | ---------------------------------------------------------------------- |
| MongoDB       | `mongodb+srv://app:pwd@cluster0.abc.mongodb.net/shop?retryWrites=true` |
| SQL           | `postgresql://app:pwd@db.example.com:5432/shop?sslmode=require`        |
| BigQuery      | No string. Project id plus Application Default Credentials.            |
| Redis         | `rediss://default:pwd@redis.example.com:6380/0`                        |
| Snowflake     | Account identifier (`myorg-myaccount`) plus user and key-pair auth     |
| DynamoDB      | No string. AWS region plus IAM credentials.                            |
| Firebase      | No string. Project id plus a service account (or ADC on Google Cloud). |
| Elasticsearch | Cloud id or `https://host:9200` plus an API key                        |

`rediss://` (two s) means TLS, the same way `sslmode=require` does for PostgreSQL. Keep all of these in environment variables or a secrets manager, not in code.

## 105: How do you size the connection pool and close connections?

**MongoDB**

```js
const client = new MongoClient(uri, { maxPoolSize: 20 });
process.on("SIGTERM", () => client.close());
```

**SQL**

```js
const pool = new pg.Pool({ max: 20, idleTimeoutMillis: 30000 });
process.on("SIGTERM", () => pool.end());
```

**Redis**

```js
await redis.close(); // node-redis v5; quit() in older versions
```

**Snowflake**

```js
const pool = snowflake.createPool(connOptions, { max: 10, min: 0 });
await pool.drain().then(() => pool.clear());
```

**Elasticsearch**

```js
await es.close();
```

BigQuery, DynamoDB and Firestore use HTTP clients with keep-alive, so there is no pool to size. Create one client per process and reuse it.

## 106: What replaces Mongoose in Node.js?

| MongoDB          | SQL                              | BigQuery                 | Redis                | Snowflake                 | DynamoDB                               | Firebase                              | Elasticsearch            |
| ---------------- | -------------------------------- | ------------------------ | -------------------- | ------------------------- | -------------------------------------- | ------------------------------------- | ------------------------ |
| Mongoose, Prisma | Prisma, Drizzle, TypeORM, Kysely | `@google-cloud/bigquery` | Redis OM for Node.js | `snowflake-sdk`, Snowpark | ElectroDB, DynamoDB Toolbox, Dynamoose | `firebase-admin` with `withConverter` | `@elastic/elasticsearch` |

Prisma and Drizzle are the closest match for a schema plus typed queries in SQL. In DynamoDB, ElectroDB and DynamoDB Toolbox help with single-table design. Dynamoose copies the Mongoose API, which makes the switch easier but hides how DynamoDB really works. For the warehouses, people mostly write SQL directly or use dbt.

## 107: How do you validate data on write ($jsonSchema)?

**MongoDB**

```js
await db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["email"],
      properties: {
        email: { bsonType: "string" },
        age: { bsonType: "int", minimum: 0 },
      },
    },
  },
});
```

**SQL**

```sql
CREATE TABLE users (
  email TEXT NOT NULL,
  age   INT CHECK (age >= 0)
);
```

**BigQuery**

Column types and `NOT NULL` (`REQUIRED` mode) are checked. There are no `CHECK` constraints, so validate in the pipeline.

**Snowflake**

Types and `NOT NULL` are enforced. Other constraints are not, so validate before loading.

**DynamoDB**

Only key attributes are checked. Validate in code (for example with Zod) before `PutCommand`.

**Firebase**

```js
// firestore.rules (for client writes)
match /users/{id} {
  allow create: if request.resource.data.email is string
                && request.resource.data.age is int
                && request.resource.data.age >= 0;
}
```

**Elasticsearch**

```js
mappings: { dynamic: "strict", properties: { email: { type: "keyword" }, age: { type: "integer" } } }
```

Firestore security rules do not apply to the Admin SDK. Server code must validate on its own.

## 108: How do you make a field required?

**MongoDB**

```js
validator: {
  $jsonSchema: {
    required: ["email"];
  }
}
```

**SQL, Snowflake**

```sql
email TEXT NOT NULL
```

**BigQuery**

```sql
email STRING NOT NULL
```

**DynamoDB**

Make it part of the key, or check it in code. A `ConditionExpression` like `attribute_exists(email)` only works on updates.

**Firebase**

```js
allow create: if request.resource.data.keys().hasAll(["email"]);
```

Elasticsearch and Redis have no required fields. Check in code before writing.

## 109: How do you set a default value for a field?

**MongoDB**

No defaults in the server. Use Mongoose defaults or set the value in code.

**SQL**

```sql
status TEXT NOT NULL DEFAULT 'new'
```

**BigQuery**

```sql
status STRING DEFAULT 'new'
```

**Snowflake**

```sql
status VARCHAR DEFAULT 'new'
```

**DynamoDB**

```js
UpdateExpression: "SET #s = if_not_exists(#s, :def)",
```

**Elasticsearch**

```js
mappings: { properties: { status: { type: "keyword", null_value: "new" } } } // only for explicit nulls
```

An Elasticsearch `null_value` only changes what is indexed for explicit `null` values. It does not change `_source` and does not fill missing fields. Use an ingest pipeline `set` processor with `override: false` for a real default.

## 110: How do you store large files like GridFS?

**MongoDB**

```js
import { GridFSBucket } from "mongodb";
const bucket = new GridFSBucket(db);
fs.createReadStream("video.mp4").pipe(bucket.openUploadStream("video.mp4"));
```

**SQL**

```sql
CREATE TABLE files (id UUID PRIMARY KEY, name TEXT, s3_key TEXT, size BIGINT);
```

**DynamoDB**

```js
Item: { id: "f1", name: "video.mp4", s3Key: "uploads/f1.mp4" } // the file itself goes to S3
```

**Firebase**

```js
import { getStorage } from "firebase-admin/storage";
await getStorage()
  .bucket()
  .upload("video.mp4", { destination: "uploads/f1.mp4" });
await firestore
  .doc("files/f1")
  .set({ name: "video.mp4", path: "uploads/f1.mp4" });
```

The common pattern everywhere is the same: put the file in object storage (S3, Cloud Storage, Firebase Storage) and keep only its metadata and path in the database. DynamoDB items are limited to 400 KB, Firestore documents to 1 MiB and Redis values to 512 MB, so large files never belong in them.

## 111: How do you translate a one-to-one relationship?

**MongoDB**

```js
{ _id: "u1", name: "Ana", profile: { bio: "Hi", avatar: "a.png" } } // embedded
```

**SQL**

```sql
CREATE TABLE profiles (user_id BIGINT PRIMARY KEY REFERENCES users(id), bio TEXT, avatar TEXT);
```

**BigQuery**

```sql
profile STRUCT<bio STRING, avatar STRING> -- keep it embedded
```

**Redis**

```js
await redis.json.set("user:u1", "$", { name: "Ana", profile: { bio: "Hi" } });
```

**Snowflake**

```sql
CREATE TABLE profiles (user_id NUMBER PRIMARY KEY, bio VARCHAR, avatar VARCHAR);
```

**DynamoDB**

```js
{ pk: "USER#u1", sk: "PROFILE", bio: "Hi", avatar: "a.png" }
```

**Firebase**

```js
await firestore.doc("users/u1").set({ name: "Ana", profile: { bio: "Hi" } });
```

**Elasticsearch**

```js
{ name: "Ana", profile: { bio: "Hi", avatar: "a.png" } }
```

Keeping one-to-one data embedded is the usual choice everywhere except SQL, where a separate table helps only if the data is large or rarely read.

## 112: How do you translate one-to-many with embedding?

**MongoDB**

```js
{ _id: "o1", userId: "u1", items: [{ sku: "A", qty: 2 }, { sku: "B", qty: 1 }] }
```

**SQL**

```sql
CREATE TABLE order_items (order_id BIGINT REFERENCES orders(id), sku TEXT, qty INT);
```

**BigQuery**

```sql
CREATE TABLE shop.orders (id STRING, user_id STRING, items ARRAY<STRUCT<sku STRING, qty INT64>>);
```

**Redis**

```js
await redis.json.set("order:o1", "$", {
  userId: "u1",
  items: [{ sku: "A", qty: 2 }],
});
```

**Snowflake**

```sql
CREATE TABLE orders (id VARCHAR, user_id VARCHAR, items ARRAY); -- or a separate order_items table
```

**DynamoDB**

```js
{ pk: "ORDER#o1", sk: "ORDER#o1", userId: "u1", items: [{ sku: "A", qty: 2 }] }
```

**Firebase**

```js
await firestore
  .doc("orders/o1")
  .set({ userId: "u1", items: [{ sku: "A", qty: 2 }] });
```

**Elasticsearch**

```js
mappings: { properties: { items: { type: "nested", properties: { sku: { type: "keyword" }, qty: { type: "integer" } } } } }
```

Small, bounded lists that are always read with the parent stay embedded in every database except SQL. BigQuery's `ARRAY<STRUCT>` is actually the preferred shape there, because it avoids joins.

## 113: How do you translate one-to-many with references?

**MongoDB**

```js
{ _id: "c1", postId: "p1", text: "Nice" } // comments collection
await db.collection("comments").find({ postId: "p1" }).toArray();
```

**SQL**

```sql
CREATE TABLE comments (id BIGINT PRIMARY KEY, post_id BIGINT REFERENCES posts(id), text TEXT);
CREATE INDEX ON comments (post_id);
```

**Redis**

```js
await redis.zAdd("post:p1:comments", { score: Date.now(), value: "c1" });
```

**DynamoDB**

```js
{ pk: "POST#p1", sk: "COMMENT#2026-11-26T10:00:00Z#c1", text: "Nice" }
```

**Firebase**

```js
await firestore.collection("posts/p1/comments").add({ text: "Nice" }); // subcollection
```

**Elasticsearch**

Index comments as their own documents with a `postId` field, or use a `join` field if you really need parent and child in one index.

## 114: How do you translate many-to-many?

**MongoDB**

```js
{ _id: "s1", name: "Ana", courseIds: ["c1", "c2"] }
```

**SQL**

```sql
CREATE TABLE enrollments (
  student_id BIGINT REFERENCES students(id),
  course_id  BIGINT REFERENCES courses(id),
  PRIMARY KEY (student_id, course_id)
);
```

**Redis**

```js
await redis.sAdd("student:s1:courses", "c1");
await redis.sAdd("course:c1:students", "s1");
```

**DynamoDB**

```js
// adjacency list: one item per edge, plus a GSI that swaps pk and sk
{ pk: "STUDENT#s1", sk: "COURSE#c1" }
```

**Firebase**

```js
await firestore
  .doc("enrollments/s1_c1")
  .set({ studentId: "s1", courseId: "c1" });
```

**Elasticsearch**

Store `courseIds` as an array on the student and, if needed, `studentIds` on the course.

BigQuery and Snowflake use the same join table as SQL, or an array of ids that you `UNNEST` / `FLATTEN`.

## 115: When should embedded documents become separate tables or items?

Move embedded data out when:

- The array can grow without limit (comments, events, log lines).
- The child data is read or updated on its own often.
- The document gets close to a size limit: 16 MB in MongoDB, 400 KB in DynamoDB, 1 MiB in Firestore.
- Many parents share the same child data and copies would get out of sync.

Keep it embedded when the list is small, bounded and always read with the parent. In SQL you almost always split it into a table. In BigQuery and Snowflake you often keep it nested on purpose, because scans are cheaper than joins. In DynamoDB you split into separate items under the same partition key, so one `Query` still returns everything.

## 116: How do you check if a document exists?

**MongoDB**

```js
const exists =
  (await db.collection("users").countDocuments({ email }, { limit: 1 })) > 0;
```

**SQL, BigQuery, Snowflake**

```sql
SELECT EXISTS (SELECT 1 FROM users WHERE email = 'a@b.com');
```

**Redis**

```js
const exists = (await redis.exists("user:1")) === 1;
```

**DynamoDB**

```js
const { Item } = await ddb.send(
  new GetCommand({
    TableName: "Users",
    Key: { id: "u1" },
    ProjectionExpression: "id",
  }),
);
const exists = Boolean(Item);
```

**Firebase**

```js
const exists = (await firestore.doc("users/u1").get()).exists;
```

**Elasticsearch**

```js
const exists = await es.exists({ index: "users", id: "u1" });
```

## 117: How do you get the latest document?

**MongoDB**

```js
await db.collection("events").find().sort({ createdAt: -1 }).limit(1).next();
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM events ORDER BY created_at DESC LIMIT 1;
```

**Redis**

```js
await redis.xRevRange("events", "+", "-", { COUNT: 1 });
```

**DynamoDB**

```js
new QueryCommand({
  TableName: "Events",
  KeyConditionExpression: "deviceId = :d",
  ExpressionAttributeValues: { ":d": "d1" },
  ScanIndexForward: false,
  Limit: 1,
});
```

**Firebase**

```js
await firestore
  .collection("events")
  .orderBy("createdAt", "desc")
  .limit(1)
  .get();
```

**Elasticsearch**

```js
await es.search({ index: "events", size: 1, sort: [{ createdAt: "desc" }] });
```

In DynamoDB, "latest" only makes sense within one partition. The latest across the whole table needs a GSI with a fixed partition key, which can get hot.

## 118: How do you get a random document ($sample)?

**MongoDB**

```js
await db
  .collection("quotes")
  .aggregate([{ $sample: { size: 1 } }])
  .toArray();
```

**SQL**

```sql
SELECT * FROM quotes ORDER BY random() LIMIT 1;
SELECT * FROM quotes TABLESAMPLE SYSTEM (1); -- faster on big tables
```

**BigQuery**

```sql
SELECT * FROM shop.quotes TABLESAMPLE SYSTEM (1 PERCENT);
```

**Redis**

```js
await redis.sRandMember("quote:ids");
await redis.randomKey();
```

**Snowflake**

```sql
SELECT * FROM quotes SAMPLE (1 ROWS);
```

**Elasticsearch**

```js
query: { function_score: { query: { match_all: {} }, random_score: {} } }, size: 1
```

DynamoDB and Firestore have no random read. A common trick is storing a random number field and querying `>= Math.random()` with `limit(1)`.

## 119: How do you get the new id after an insert?

**MongoDB**

```js
const { insertedId } = await db.collection("users").insertOne({ name: "Ana" });
```

**SQL**

```sql
INSERT INTO users (name) VALUES ('Ana') RETURNING id;
```

**Redis**

```js
const id = await redis.incr("seq:user"); // you create the id first
```

**Snowflake**

Snowflake does not return generated ids. Generate the id yourself (`UUID_STRING()` or a sequence `seq.NEXTVAL`) before inserting.

**DynamoDB**

You always know it, because you created the key before `PutCommand`.

**Firebase**

```js
const ref = await firestore.collection("users").add({ name: "Ana" });
ref.id;
```

**Elasticsearch**

```js
const { _id } = await es.index({ index: "users", document: { name: "Ana" } });
```

## 120: How do you handle duplicate key errors?

**MongoDB**

```js
try {
  await db.collection("users").insertOne({ email });
} catch (err) {
  if (err.code === 11000) throw new Error("Email already taken");
  throw err;
}
```

**SQL**

```js
try {
  await pool.query("INSERT INTO users (email) VALUES ($1)", [email]);
} catch (err) {
  if (err.code === "23505") throw new Error("Email already taken"); // unique_violation
  throw err;
}
```

**Redis**

```js
const ok = await redis.set(`email:${email}`, userId, { NX: true });
if (ok === null) throw new Error("Email already taken");
```

**DynamoDB**

```js
try {
  await ddb.send(
    new PutCommand({
      TableName: "Emails",
      Item: { email },
      ConditionExpression: "attribute_not_exists(email)",
    }),
  );
} catch (err) {
  if (err.name === "ConditionalCheckFailedException")
    throw new Error("Email already taken");
  throw err;
}
```

**Firebase**

```js
try {
  await firestore.doc(`emails/${email}`).create({ userId });
} catch (err) {
  if (err.code === 6) throw new Error("Email already taken"); // ALREADY_EXISTS
  throw err;
}
```

**Elasticsearch**

```js
try {
  await es.create({ index: "users", id: email, document: { email } });
} catch (err) {
  if (err.meta?.statusCode === 409) throw new Error("Email already taken");
  throw err;
}
```

## 121: How do you read how many documents were changed?

**MongoDB**

```js
const { matchedCount, modifiedCount } = await db
  .collection("users")
  .updateMany(filter, update);
```

**SQL**

```js
const { rowCount } = await pool.query(
  "UPDATE users SET status = 'x' WHERE age > 30",
);
```

**BigQuery**

```js
const [job] = await bigquery.createQueryJob({
  query: "UPDATE shop.users SET status = 'x' WHERE age > 30",
});
await job.getQueryResults();
const [meta] = await job.getMetadata();
meta.statistics.query.numDmlAffectedRows;
```

**Snowflake**

The result has one row with a `number of rows updated` column, and `stmt.getNumUpdatedRows()` in the Node.js driver returns the same number.

**DynamoDB**

Single-item writes change one item or fail. Use `ReturnValues: "ALL_OLD"` to see if the item existed before.

**Elasticsearch**

```js
const { updated, deleted } = await es.updateByQuery({
  index: "users",
  query,
  script,
});
```

## 122: How do you translate bulkWrite?

**MongoDB**

```js
await db
  .collection("users")
  .bulkWrite([
    { insertOne: { document: { _id: "u3", name: "Cy" } } },
    { updateOne: { filter: { _id: "u1" }, update: { $set: { name: "Ana" } } } },
    { deleteOne: { filter: { _id: "u2" } } },
  ]);
```

**SQL**

```sql
BEGIN;
INSERT INTO users (id, name) VALUES ('u3', 'Cy');
UPDATE users SET name = 'Ana' WHERE id = 'u1';
DELETE FROM users WHERE id = 'u2';
COMMIT;
```

**Redis**

```js
await redis
  .multi()
  .json.set("user:u3", "$", { name: "Cy" })
  .json.set("user:u1", "$.name", "Ana")
  .del("user:u2")
  .exec();
```

**DynamoDB**

```js
new BatchWriteCommand({
  RequestItems: {
    Users: [
      { PutRequest: { Item: { id: "u3", name: "Cy" } } },
      { DeleteRequest: { Key: { id: "u2" } } },
    ],
  },
}); // no updates in BatchWrite; use TransactWrite for mixed operations
```

**Firebase**

```js
const writer = firestore.bulkWriter();
writer.create(firestore.doc("users/u3"), { name: "Cy" });
writer.update(firestore.doc("users/u1"), { name: "Ana" });
writer.delete(firestore.doc("users/u2"));
await writer.close();
```

**Elasticsearch**

```js
await es.bulk({
  operations: [
    { index: { _index: "users", _id: "u3" } },
    { name: "Cy" },
    { update: { _index: "users", _id: "u1" } },
    { doc: { name: "Ana" } },
    { delete: { _index: "users", _id: "u2" } },
  ],
});
```

## 123: How do ordered and unordered inserts translate?

MongoDB `insertMany` is ordered by default: it stops at the first error. With `{ ordered: false }` it keeps going and reports all errors at the end.

- **SQL:** one multi-row `INSERT` is all or nothing. For "skip the bad ones", use `ON CONFLICT DO NOTHING` or insert row by row.
- **BigQuery and Snowflake:** a DML statement is all or nothing. Load jobs can skip bad rows with `max_bad_records` (BigQuery) or `ON_ERROR = CONTINUE` (Snowflake).
- **Redis:** commands in `MULTI` all run even if one fails. There is no rollback.
- **DynamoDB:** `BatchWriteItem` works like unordered: some items can fail and come back in `UnprocessedItems`. `TransactWriteItems` is all or nothing.
- **Firebase:** a `batch()` is all or nothing. `BulkWriter` is like unordered and retries failed writes.
- **Elasticsearch:** `_bulk` is unordered. Check `errors` and each item's status in the response.

## 124: How does write concern translate?

MongoDB lets you choose how many replicas must confirm a write (`w: 1`, `w: "majority"`) and whether it must be in the journal (`j: true`). Most other databases make that choice for you:

- **SQL (PostgreSQL):** a commit is durable on the primary. With replicas, `synchronous_commit` and `synchronous_standby_names` control whether a standby must confirm too.
- **BigQuery, Snowflake:** a finished job is durable. No setting.
- **Redis:** writes are in memory first. `appendfsync` sets how often they reach disk, and the `WAIT` command waits for replicas.
- **DynamoDB:** a successful write is stored on several copies across availability zones before it returns.
- **Firebase:** a successful write is committed to a majority of replicas, so it is durable.
- **Elasticsearch:** `wait_for_active_shards` controls how many shard copies must be active before the write starts.

## 125: How does read preference translate?

MongoDB read preference (`primary`, `secondary`, `nearest`) picks which replica serves reads.

- **SQL:** point read-only queries at a replica connection string. Replicas can lag behind.
- **Redis:** connect to a replica, or with Redis Cluster use `READONLY` on a replica connection.
- **DynamoDB:** reads are eventually consistent by default. `ConsistentRead: true` gives a strongly consistent read from the leader (not for GSIs, and it costs twice as much).
- **Firebase:** reads are strongly consistent. There is no replica choice.
- **Elasticsearch:** the `preference` search parameter, for example `_local` or a session id to hit the same shard copies each time.
- **BigQuery, Snowflake:** no replicas to choose from. Queries always see committed data.

## 126: What is the default read consistency in each database?

| MongoDB                                                             | SQL                                     | BigQuery                    | Redis                                     | Snowflake                   | DynamoDB                                                       | Firebase | Elasticsearch                                                                |
| ------------------------------------------------------------------- | --------------------------------------- | --------------------------- | ----------------------------------------- | --------------------------- | -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------- |
| Strong on the primary (`readConcern: "local"`), secondaries may lag | Strong on the primary, replicas may lag | Strong, sees committed data | Strong on the primary, replicas are async | Strong, sees committed data | Eventually consistent, strong if you ask; GSIs always eventual | Strong   | Get by id is real-time, search sees changes after a refresh (about 1 second) |

The two that surprise people most when they leave MongoDB are DynamoDB (a read right after a write may return old data unless you set `ConsistentRead: true`) and Elasticsearch (a new document does not show up in search until the next refresh).

## 127: Which of these databases support transactions?

- **MongoDB:** multi-document ACID transactions on replica sets and sharded clusters.
- **SQL:** full ACID transactions with `BEGIN` and `COMMIT`.
- **BigQuery:** multi-statement transactions inside a script or session (`BEGIN TRANSACTION ... COMMIT TRANSACTION`).
- **Redis:** `MULTI`/`EXEC` runs commands together with no other client in between, but there is no rollback. Lua scripts and functions are also atomic.
- **Snowflake:** `BEGIN ... COMMIT` transactions across tables.
- **DynamoDB:** `TransactWriteItems` and `TransactGetItems`, up to 100 items in one region.
- **Firebase:** `runTransaction()` for read-then-write, and `batch()` for up to 500 writes.
- **Elasticsearch:** no transactions. Each document write is atomic on its own.

## 128: How do you iterate over results with a cursor?

**MongoDB**

```js
for await (const user of db.collection("users").find({ status: "active" })) {
  console.log(user.email);
}
```

**SQL**

```js
import Cursor from "pg-cursor";
const client = await pool.connect();
const cursor = client.query(
  new Cursor("SELECT * FROM users WHERE status = $1", ["active"]),
);
let rows;
while ((rows = await cursor.read(500)).length)
  rows.forEach((r) => console.log(r.email));
await cursor.close();
client.release();
```

**BigQuery**

```js
const [job] = await bigquery.createQueryJob({
  query: "SELECT email FROM shop.users",
});
let [rows, next] = await job.getQueryResults({
  maxResults: 1000,
  autoPaginate: false,
});
// pass next to getQueryResults() again until it is null
```

**Redis**

```js
for await (const keys of redis.scanIterator({ MATCH: "user:*", COUNT: 500 })) {
  for (const key of keys) console.log(key);
}
```

**DynamoDB**

```js
import { paginateScan } from "@aws-sdk/lib-dynamodb";
for await (const page of paginateScan(
  { client: ddb },
  { TableName: "Users" },
)) {
  page.Items.forEach((u) => console.log(u.email));
}
```

**Firebase**

```js
for await (const doc of firestore.collection("users").stream()) {
  console.log(doc.get("email"));
}
```

**Elasticsearch**

```js
for await (const hit of es.helpers.scrollDocuments({
  index: "users",
  query: { match_all: {} },
})) {
  console.log(hit.email);
}
```

## 129: How do you stream a large result set without loading it all into memory?

**MongoDB**

```js
db.collection("events").find().stream().pipe(transform).pipe(output);
```

**SQL**

```js
import QueryStream from "pg-query-stream";
const client = await pool.connect();
client
  .query(new QueryStream("SELECT * FROM events"))
  .pipe(transform)
  .pipe(output);
```

**BigQuery**

```js
bigquery
  .createQueryStream({ query: "SELECT * FROM shop.events" })
  .pipe(transform)
  .pipe(output);
```

**Snowflake**

```js
const stmt = conn.execute({
  sqlText: "SELECT * FROM events",
  streamResult: true,
});
stmt.streamRows().pipe(transform).pipe(output);
```

**Firebase**

```js
firestore.collection("events").stream().pipe(transform).pipe(output);
```

**Elasticsearch**

```js
for await (const doc of es.helpers.scrollDocuments({ index: "events" }))
  output.write(JSON.stringify(doc) + "\n");
```

For DynamoDB, use the paginator from the previous question. It loads one page (up to 1 MB) at a time.

## 130: How does batchSize translate?

MongoDB `batchSize` sets how many documents come back per network round trip of a cursor.

- **SQL:** the number you pass to `cursor.read(n)`, or `FETCH n` on a server-side cursor.
- **BigQuery:** `maxResults` per page of results.
- **Redis:** the `COUNT` hint on `SCAN`, and `LIMIT` on `FT.SEARCH`.
- **Snowflake:** results come in chunks the server picks. You control rows per `streamRows({ start, end })`.
- **DynamoDB:** `Limit` per page, always capped at 1 MB of data.
- **Firebase:** `limit()` on each page when you page with `startAfter`.
- **Elasticsearch:** `size` per scroll or `search_after` page.

## 131: How do you set a query timeout like maxTimeMS?

**MongoDB**

```js
await db.collection("users").find(filter).maxTimeMS(2000).toArray();
```

**SQL**

```sql
SET statement_timeout = '2s';
```

**BigQuery**

```js
await bigquery.query({ query, jobTimeoutMs: 2000 });
```

**Redis**

```js
await redis.ft.search("idx:users", "@status:{active}", { TIMEOUT: 2000 }); // ms, for search queries
```

**Snowflake**

```sql
ALTER SESSION SET STATEMENT_TIMEOUT_IN_SECONDS = 2;
```

**DynamoDB**

```js
await ddb.send(new GetCommand(params), {
  abortSignal: AbortSignal.timeout(2000),
});
```

**Firebase**

The Admin SDK has no per-query timeout option. Race the query against a timer if you need one.

**Elasticsearch**

```js
await es.search(
  { index: "users", timeout: "2s", query },
  { requestTimeout: 2000 },
);
```

The Elasticsearch `timeout` body field returns partial results when time runs out. `requestTimeout` is the client-side limit that aborts the HTTP call.

## 132: How do you get the size of a collection or table?

**MongoDB**

```js
await db.command({ collStats: "users" }); // or $collStats in an aggregation
```

**SQL**

```sql
SELECT pg_size_pretty(pg_total_relation_size('users'));
```

**BigQuery**

```sql
SELECT table_name, total_rows, total_logical_bytes
FROM `region-us`.INFORMATION_SCHEMA.TABLE_STORAGE WHERE table_schema = 'shop';
```

**Redis**

```js
await redis.memoryUsage("user:1"); // one key
await redis.dbSize(); // number of keys
```

**Snowflake**

```sql
SELECT table_name, row_count, bytes FROM shop.information_schema.tables WHERE table_schema = 'PUBLIC';
```

**DynamoDB**

```js
const { Table } = await new DynamoDBClient({}).send(
  new DescribeTableCommand({ TableName: "Users" }),
);
Table.TableSizeBytes;
Table.ItemCount; // updated about every 6 hours
```

**Elasticsearch**

```js
await es.cat.indices({ index: "users", format: "json" });
```

Firestore shows storage size per database in the Cloud console usage pages, not per collection.

## 133: How do you list all collections or tables?

**MongoDB**

```js
await db.listCollections().toArray();
```

**SQL**

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
```

**BigQuery**

```sql
SELECT table_name FROM shop.INFORMATION_SCHEMA.TABLES;
```

**Redis**

```js
await redis.ft._list(); // search indexes are the closest thing to collections
```

**Snowflake**

```sql
SHOW TABLES IN SCHEMA shop.public;
```

**DynamoDB**

```js
import { ListTablesCommand } from "@aws-sdk/client-dynamodb";
const { TableNames } = await new DynamoDBClient({}).send(
  new ListTablesCommand({}),
);
```

**Firebase**

```js
const collections = await firestore.listCollections();
collections.map((c) => c.id);
```

**Elasticsearch**

```js
await es.cat.indices({ format: "json" });
```

## 134: How do you list all databases?

**MongoDB**

```js
await client.db().admin().listDatabases();
```

**SQL**

```sql
SELECT datname FROM pg_database;
```

**BigQuery**

```bash
bq ls --datasets
```

**Redis**

```js
await redis.configGet("databases"); // how many logical DBs exist
await redis.info("keyspace"); // which ones hold keys
```

**Snowflake**

```sql
SHOW DATABASES;
```

**Firebase**

```bash
gcloud firestore databases list
```

DynamoDB and Elasticsearch have no database level, so this question does not apply to them.

## 135: How do you match one element in an array of objects ($elemMatch)?

**MongoDB**

```js
await db
  .collection("orders")
  .find({ items: { $elemMatch: { sku: "A", qty: { $gte: 2 } } } })
  .toArray();
```

**SQL**

```sql
SELECT DISTINCT o.* FROM orders o JOIN order_items i ON i.order_id = o.id WHERE i.sku = 'A' AND i.qty >= 2;
-- with a JSONB column:
SELECT * FROM orders WHERE jsonb_path_exists(items, '$[*] ? (@.sku == "A" && @.qty >= 2)');
```

**BigQuery**

```sql
SELECT * FROM shop.orders o WHERE EXISTS (SELECT 1 FROM UNNEST(o.items) i WHERE i.sku = 'A' AND i.qty >= 2);
```

**Snowflake**

```sql
SELECT DISTINCT o.* FROM orders o, LATERAL FLATTEN(o.items) i WHERE i.value:sku = 'A' AND i.value:qty >= 2;
```

**Elasticsearch**

```js
query: {
  nested: {
    path: "items",
    query: { bool: { filter: [{ term: { "items.sku": "A" } }, { range: { "items.qty": { gte: 2 } } }] } },
  },
}
```

Firestore `array-contains` only matches a whole object exactly, so `{ sku: "A", qty: 2 }` works but `qty >= 2` does not. In Elasticsearch, without the `nested` type, the conditions could match across different array elements.

## 136: How do you update one element in an array with the positional $ operator?

**MongoDB**

```js
await db
  .collection("orders")
  .updateOne({ _id: id, "items.sku": "A" }, { $set: { "items.$.qty": 5 } });
```

**SQL**

```sql
UPDATE order_items SET qty = 5 WHERE order_id = 1 AND sku = 'A';
```

**BigQuery**

```sql
UPDATE shop.orders
SET items = ARRAY(SELECT AS STRUCT i.sku, IF(i.sku = 'A', 5, i.qty) AS qty FROM UNNEST(items) i)
WHERE id = 'o1';
```

**Redis**

```js
await redis.json.set("order:o1", '$.items[?(@.sku=="A")].qty', 5);
```

**DynamoDB**

```js
UpdateExpression: "SET items[0].qty = :q", // you must know the index
ConditionExpression: "items[0].sku = :sku",
```

**Firebase**

Read the document in a transaction, change the array in code and write it back. Firestore cannot update one array element.

**Elasticsearch**

```js
script: { source: "for (i in ctx._source.items) { if (i.sku == params.sku) { i.qty = params.q } }", params: { sku: "A", q: 5 } }
```

## 137: How do you update every element in an array with $[]?

**MongoDB**

```js
await db
  .collection("orders")
  .updateOne({ _id: id }, { $set: { "items.$[].shipped": true } });
```

**SQL**

```sql
UPDATE order_items SET shipped = true WHERE order_id = 1;
```

**BigQuery**

```sql
UPDATE shop.orders SET items = ARRAY(SELECT AS STRUCT i.* REPLACE (TRUE AS shipped) FROM UNNEST(items) i) WHERE id = 'o1';
```

**Redis**

```js
await redis.json.set("order:o1", "$.items[*].shipped", true);
```

**Elasticsearch**

```js
script: {
  source: "for (i in ctx._source.items) { i.shipped = true }";
}
```

In DynamoDB and Firestore you rewrite the whole array.

## 138: How do you store a map of dynamic keys?

**MongoDB**

```js
{ _id: "u1", settings: { theme: "dark", lang: "ka", "beta.search": true } }
```

**SQL**

```sql
CREATE TABLE user_settings (user_id BIGINT, key TEXT, value TEXT, PRIMARY KEY (user_id, key));
-- or settings JSONB
```

**BigQuery**

```sql
settings JSON -- or ARRAY<STRUCT<key STRING, value STRING>>
```

**Redis**

```js
await redis.hSet("user:u1:settings", { theme: "dark", lang: "ka" });
```

**Snowflake**

```sql
settings OBJECT
```

**DynamoDB**

```js
UpdateExpression: "SET settings.#k = :v", ExpressionAttributeNames: { "#k": "theme" },
```

**Firebase**

```js
await firestore.doc("users/u1").update({ "settings.theme": "dark" });
```

**Elasticsearch**

```js
mappings: {
  properties: {
    settings: {
      type: "flattened";
    }
  }
}
```

Use `flattened` in Elasticsearch so thousands of different keys do not blow up the mapping ("mapping explosion").

## 139: How do you translate an auto-increment counter collection?

**MongoDB**

```js
const { seq } = await db
  .collection("counters")
  .findOneAndUpdate(
    { _id: "invoice" },
    { $inc: { seq: 1 } },
    { upsert: true, returnDocument: "after" },
  );
```

**SQL**

```sql
CREATE SEQUENCE invoice_seq;
SELECT nextval('invoice_seq');
```

**BigQuery**

No sequences. Use `GENERATE_UUID()` or `ROW_NUMBER()` when loading.

**Redis**

```js
const seq = await redis.incr("seq:invoice");
```

**Snowflake**

```sql
CREATE SEQUENCE invoice_seq;
SELECT invoice_seq.NEXTVAL;
```

**DynamoDB**

```js
const { Attributes } = await ddb.send(
  new UpdateCommand({
    TableName: "Counters",
    Key: { id: "invoice" },
    UpdateExpression: "ADD seq :one",
    ExpressionAttributeValues: { ":one": 1 },
    ReturnValues: "UPDATED_NEW",
  }),
);
```

**Firebase**

```js
const seq = await firestore.runTransaction(async (tx) => {
  const ref = firestore.doc("counters/invoice");
  const next = ((await tx.get(ref)).get("seq") ?? 0) + 1;
  tx.set(ref, { seq: next });
  return next;
});
```

A single counter document is a hot spot in DynamoDB and Firestore. Firestore handles about one sustained write per second per document well, so use random ids unless you really need numbers.

## 140: How do you store user sessions?

**MongoDB**

```js
await db.collection("sessions").insertOne({ _id: sid, userId, expiresAt }); // plus a TTL index
```

**SQL**

```sql
CREATE TABLE sessions (sid TEXT PRIMARY KEY, user_id BIGINT, data JSONB, expires_at TIMESTAMPTZ);
```

**Redis**

```js
await redis.set(`sess:${sid}`, JSON.stringify({ userId }), { EX: 86400 });
```

**DynamoDB**

```js
Item: { sid, userId, expiresAt: Math.floor(Date.now() / 1000) + 86400 } // TTL on expiresAt
```

**Firebase**

```js
await firestore.doc(`sessions/${sid}`).set({ userId, expiresAt }); // with a TTL policy on expiresAt
```

Redis is the usual choice for sessions because reads are fast and keys expire exactly on time. BigQuery, Snowflake and Elasticsearch are not suitable for session data.

## 141: How do you cache query results?

**MongoDB**

MongoDB keeps hot data in the WiredTiger cache, but it has no query result cache. Apps add Redis in front.

**SQL**

```sql
CREATE MATERIALIZED VIEW top_products AS SELECT ...;
REFRESH MATERIALIZED VIEW top_products;
```

**BigQuery**

Query results are cached for about 24 hours automatically. Running the same query on unchanged tables is free.

**Redis**

```js
const key = `cache:top-products`;
let data = await redis.get(key);
if (!data) {
  data = JSON.stringify(await loadTopProducts());
  await redis.set(key, data, { EX: 60 });
}
return JSON.parse(data);
```

**Snowflake**

Results are cached for 24 hours and reused when the query text and data are the same, without using a warehouse.

**DynamoDB**

DynamoDB Accelerator (DAX) is a managed read-through cache for `GetItem` and `Query`.

**Elasticsearch**

The shard request cache keeps results of `size: 0` aggregation requests until the index refreshes with changes.

## 142: How do you translate $sortByCount?

**MongoDB**

```js
[{ $unwind: "$tags" }, { $sortByCount: "$tags" }];
```

**SQL**

```sql
SELECT tag, COUNT(*) AS count FROM posts, unnest(tags) AS tag GROUP BY tag ORDER BY count DESC;
```

**BigQuery**

```sql
SELECT tag, COUNT(*) AS count FROM shop.posts, UNNEST(tags) tag GROUP BY tag ORDER BY count DESC;
```

**Redis**

```js
STEPS: [
  {
    type: "GROUPBY",
    properties: "@tags",
    REDUCE: [{ type: "COUNT", AS: "count" }],
  },
  { type: "SORTBY", BY: { BY: "@count", DIRECTION: "DESC" } },
];
```

**Snowflake**

```sql
SELECT f.value::STRING AS tag, COUNT(*) AS count FROM posts, LATERAL FLATTEN(tags) f GROUP BY tag ORDER BY count DESC;
```

**Elasticsearch**

```js
aggs: {
  tags: {
    terms: {
      field: "tags";
    }
  }
} // sorted by doc_count desc by default
```

## 143: How do you translate $replaceRoot?

**MongoDB**

```js
[{ $replaceRoot: { newRoot: "$address" } }];
```

**SQL**

```sql
SELECT address_city AS city, address_zip AS zip FROM users;
SELECT a.* FROM users, jsonb_to_record(address) AS a(city TEXT, zip TEXT); -- JSONB
```

**BigQuery**

```sql
SELECT address.* FROM shop.users;
```

**Snowflake**

```sql
SELECT address:city::STRING AS city, address:zip::STRING AS zip FROM users;
```

**Elasticsearch**

```js
_source: ["address"]; // then use hit._source.address in code
```

## 144: How do you convert types ($toString, $toInt, $convert)?

**MongoDB**

```js
[{ $project: { id: { $toString: "$_id" }, qty: { $toInt: "$qtyText" } } }];
```

**SQL**

```sql
SELECT id::TEXT, qty_text::INT FROM items;
```

**BigQuery**

```sql
SELECT CAST(id AS STRING), SAFE_CAST(qty_text AS INT64) FROM shop.items;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: "@qtyText + 0", AS: "qty" }];
```

**Snowflake**

```sql
SELECT id::VARCHAR, TRY_TO_NUMBER(qty_text) FROM items;
```

**Elasticsearch**

```js
runtime_mappings: { qty: { type: "long", script: "emit(Long.parseLong(doc['qtyText'].value))" } }
```

`SAFE_CAST` (BigQuery) and `TRY_TO_NUMBER` (Snowflake) return `NULL` instead of failing, like `$convert` with `onError: null`.

## 145: How do you split a string ($split)?

**MongoDB**

```js
[{ $project: { parts: { $split: ["$path", "/"] } } }];
```

**SQL**

```sql
SELECT string_to_array(path, '/') AS parts FROM files;
```

**BigQuery**

```sql
SELECT SPLIT(path, '/') AS parts FROM shop.files;
```

**Redis**

```js
STEPS: [{ type: "APPLY", expression: 'split(@path, "/")', AS: "parts" }];
```

**Snowflake**

```sql
SELECT SPLIT(path, '/') AS parts FROM files;
```

**Elasticsearch**

Use a `path_hierarchy` tokenizer at index time, or `splitOnToken` in a Painless script.

## 146: How do you return an array length in the output ($size)?

**MongoDB**

```js
[{ $project: { title: 1, tagCount: { $size: "$tags" } } }];
```

**SQL**

```sql
SELECT title, cardinality(tags) AS tag_count FROM posts;
```

**BigQuery**

```sql
SELECT title, ARRAY_LENGTH(tags) AS tag_count FROM shop.posts;
```

**Snowflake**

```sql
SELECT title, ARRAY_SIZE(tags) AS tag_count FROM posts;
```

**Elasticsearch**

```js
script_fields: {
  tagCount: {
    script: "doc['tags'].size()";
  }
}
```

Redis JSON has `JSON.ARRLEN` for one key: `await redis.json.arrLen("post:1", { path: "$.tags" })`.

## 147: How do you get one array element by position ($arrayElemAt)?

**MongoDB**

```js
[
  {
    $project: {
      first: { $arrayElemAt: ["$items", 0] },
      last: { $arrayElemAt: ["$items", -1] },
    },
  },
];
```

**SQL**

```sql
SELECT items[1] AS first, items[cardinality(items)] AS last FROM orders; -- arrays start at 1
```

**BigQuery**

```sql
SELECT items[SAFE_OFFSET(0)] AS first, items[SAFE_OFFSET(ARRAY_LENGTH(items) - 1)] AS last FROM shop.orders;
```

**Redis**

```js
await redis.json.get("order:1", { path: "$.items[0]" });
await redis.lIndex("list:1", -1); // last element of a list
```

**Snowflake**

```sql
SELECT items[0] AS first, items[ARRAY_SIZE(items) - 1] AS last FROM orders;
```

**DynamoDB**

```js
ProjectionExpression: "items[0]",
```

## 148: How do you return only the first N array elements ($slice)?

**MongoDB**

```js
await db
  .collection("posts")
  .find({}, { projection: { comments: { $slice: 3 } } })
  .toArray();
```

**SQL**

```sql
SELECT id, comments[1:3] FROM posts;
```

**BigQuery**

```sql
SELECT id, ARRAY(SELECT c FROM UNNEST(comments) c WITH OFFSET o WHERE o < 3 ORDER BY o) AS comments FROM shop.posts;
```

**Redis**

```js
await redis.lRange("post:1:comments", 0, 2);
```

**Snowflake**

```sql
SELECT id, ARRAY_SLICE(comments, 0, 3) FROM posts;
```

**DynamoDB**

```js
ProjectionExpression: "comments[0], comments[1], comments[2]",
```

## 149: How do you check the server version and health?

**MongoDB**

```js
await db.admin().serverStatus();
await db.command({ buildInfo: 1 });
```

**SQL**

```sql
SELECT version();
SELECT * FROM pg_stat_activity;
```

**BigQuery**

Fully managed, no version. Check the Google Cloud status page and job errors.

**Redis**

```js
await redis.info("server");
await redis.ping();
```

**Snowflake**

```sql
SELECT CURRENT_VERSION();
```

**DynamoDB**

Fully managed. Watch CloudWatch metrics like `ThrottledRequests` and `SystemErrors`.

**Firebase**

Fully managed. Watch the usage and Cloud Monitoring pages.

**Elasticsearch**

```js
await es.info();
await es.cluster.health();
```

## 150: What should you check before translating a MongoDB app?

1. **List the real queries.** Use the profiler, `$indexStats` and the code to find every query, update and aggregation the app runs.
2. **Map the document shapes.** Sample documents (for example with `$sample` or Compass schema analysis) to see optional fields, mixed types and array sizes.
3. **Find the joins.** Every `$lookup` and every `populate()` shows a relation that needs a home in the new design.
4. **Note transactions and consistency needs.** Which writes must succeed together, and which reads must see the latest data?
5. **Check limits.** Document sizes, array lengths and write rates must fit the target (400 KB items, 1 MiB docs, hot partitions).
6. **Pick the target by workload.** OLTP to SQL, DynamoDB or Firestore, analytics to BigQuery or Snowflake, cache and counters to Redis, search to Elasticsearch.

Doing this first saves you from translating queries one to one into a design that will not work at scale.

# Moderate Questions (151-300)

## 151: How do you translate a multi-document transaction?

**MongoDB**

```js
const session = client.startSession();
await session.withTransaction(async () => {
  await db
    .collection("accounts")
    .updateOne({ _id: "a" }, { $inc: { balance: -100 } }, { session });
  await db
    .collection("accounts")
    .updateOne({ _id: "b" }, { $inc: { balance: 100 } }, { session });
});
await session.endSession();
```

**SQL**

```js
const c = await pool.connect();
try {
  await c.query("BEGIN");
  await c.query("UPDATE accounts SET balance = balance - 100 WHERE id = 'a'");
  await c.query("UPDATE accounts SET balance = balance + 100 WHERE id = 'b'");
  await c.query("COMMIT");
} catch (e) {
  await c.query("ROLLBACK");
  throw e;
} finally {
  c.release();
}
```

**BigQuery**

```sql
BEGIN TRANSACTION;
UPDATE shop.accounts SET balance = balance - 100 WHERE id = 'a';
UPDATE shop.accounts SET balance = balance + 100 WHERE id = 'b';
COMMIT TRANSACTION;
```

**Redis**

```js
await redis
  .multi()
  .hIncrBy("account:a", "balance", -100)
  .hIncrBy("account:b", "balance", 100)
  .exec();
```

**Snowflake**

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 'a';
UPDATE accounts SET balance = balance + 100 WHERE id = 'b';
COMMIT;
```

**DynamoDB**

```js
import { TransactWriteCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(
  new TransactWriteCommand({
    TransactItems: [
      {
        Update: {
          TableName: "Accounts",
          Key: { id: "a" },
          UpdateExpression: "ADD balance :neg",
          ConditionExpression: "balance >= :amt",
          ExpressionAttributeValues: { ":neg": -100, ":amt": 100 },
        },
      },
      {
        Update: {
          TableName: "Accounts",
          Key: { id: "b" },
          UpdateExpression: "ADD balance :amt",
          ExpressionAttributeValues: { ":amt": 100 },
        },
      },
    ],
  }),
);
```

**Firebase**

```js
await firestore.runTransaction(async (tx) => {
  const a = firestore.doc("accounts/a");
  const b = firestore.doc("accounts/b");
  const snapA = await tx.get(a);
  if (snapA.get("balance") < 100) throw new Error("Not enough money");
  tx.update(a, { balance: FieldValue.increment(-100) });
  tx.update(b, { balance: FieldValue.increment(100) });
});
```

The MongoDB `withTransaction` helper retries on transient errors. In SQL you write that retry loop yourself, and in Firestore `runTransaction` retries for you. Redis `MULTI` has no rollback and no balance check, so for "only if enough money" you need a Lua script. Elasticsearch has no transactions.

## 152: How do you translate $lookup with a pipeline (a correlated join with conditions)?

**MongoDB**

```js
[
  {
    $lookup: {
      from: "orders",
      let: { uid: "$_id" },
      pipeline: [
        { $match: { $expr: { $eq: ["$userId", "$$uid"] }, status: "paid" } },
        { $sort: { createdAt: -1 } },
        { $limit: 3 },
      ],
      as: "recentOrders",
    },
  },
];
```

**SQL**

```sql
SELECT u.*, r.*
FROM users u
LEFT JOIN LATERAL (
  SELECT * FROM orders o WHERE o.user_id = u.id AND o.status = 'paid' ORDER BY o.created_at DESC LIMIT 3
) r ON true;
```

**BigQuery**

```sql
SELECT u.*,
  ARRAY(SELECT AS STRUCT o.* FROM shop.orders o
        WHERE o.user_id = u.id AND o.status = 'paid' ORDER BY o.created_at DESC LIMIT 3) AS recent_orders
FROM shop.users u;
```

**Snowflake**

```sql
SELECT u.id, o.*
FROM users u
LEFT JOIN orders o ON o.user_id = u.id AND o.status = 'paid'
QUALIFY ROW_NUMBER() OVER (PARTITION BY u.id ORDER BY o.created_at DESC) <= 3;
```

**DynamoDB**

```js
// orders stored under the user partition with sk "ORDER#<date>"
new QueryCommand({
  TableName: "App",
  KeyConditionExpression: "pk = :pk AND begins_with(sk, :o)",
  FilterExpression: "#s = :paid",
  ExpressionAttributeNames: { "#s": "status" },
  ExpressionAttributeValues: {
    ":pk": "USER#u1",
    ":o": "ORDER#",
    ":paid": "paid",
  },
  ScanIndexForward: false,
});
```

The BigQuery form returns an array per user, which is the closest shape to what `$lookup` returns.

## 153: How do you translate $lookup followed by $unwind into an inner join?

**MongoDB**

```js
[
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
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT o.total, u.name FROM orders o JOIN users u ON u.id = o.user_id;
```

**Elasticsearch**

```js
// ES|QL LOOKUP JOIN against a lookup-mode index
await es.esql.query({
  query: "FROM orders | LOOKUP JOIN users_lookup ON userId | KEEP total, name",
});
```

`$unwind` without `preserveNullAndEmptyArrays` drops orders whose user was not found, which is exactly what an inner `JOIN` does. Elasticsearch's `LOOKUP JOIN` needs the right side to be an index created with `index.mode: lookup`.

## 154: How do you keep unmatched rows like a left join ($unwind with preserveNullAndEmptyArrays)?

**MongoDB**

```js
[
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user",
    },
  },
  { $unwind: { path: "$user", preserveNullAndEmptyArrays: true } },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT o.*, u.name FROM orders o LEFT JOIN users u ON u.id = o.user_id;
```

**Snowflake (flatten an array but keep empty ones)**

```sql
SELECT p.id, f.value FROM posts p, LATERAL FLATTEN(input => p.tags, OUTER => TRUE) f;
```

**BigQuery (unnest but keep empty arrays)**

```sql
SELECT p.id, tag FROM shop.posts p LEFT JOIN UNNEST(p.tags) AS tag;
```

## 155: How do you translate $facet?

**MongoDB**

```js
[
  { $match: { category: "books" } },
  {
    $facet: {
      byAuthor: [{ $group: { _id: "$author", n: { $sum: 1 } } }],
      priceStats: [
        {
          $group: {
            _id: null,
            avg: { $avg: "$price" },
            max: { $max: "$price" },
          },
        },
      ],
      page: [{ $sort: { price: 1 } }, { $limit: 10 }],
    },
  },
];
```

**SQL**

```sql
WITH b AS (SELECT * FROM products WHERE category = 'books')
SELECT
  (SELECT json_agg(t) FROM (SELECT author, COUNT(*) n FROM b GROUP BY author) t) AS by_author,
  (SELECT json_build_object('avg', AVG(price), 'max', MAX(price)) FROM b) AS price_stats,
  (SELECT json_agg(t) FROM (SELECT * FROM b ORDER BY price LIMIT 10) t) AS page;
```

**BigQuery**

```sql
SELECT
  ARRAY(SELECT AS STRUCT author, COUNT(*) n FROM shop.products WHERE category = 'books' GROUP BY author) AS by_author,
  (SELECT AS STRUCT AVG(price) avg, MAX(price) max FROM shop.products WHERE category = 'books') AS price_stats;
```

**Redis**

Run one `FT.SEARCH` for the page and one `FT.AGGREGATE` per facet, in parallel with `Promise.all`.

**Elasticsearch**

```js
await es.search({
  index: "products",
  query: { term: { category: "books" } },
  sort: [{ price: "asc" }],
  size: 10,
  aggs: {
    byAuthor: { terms: { field: "author" } },
    priceStats: { stats: { field: "price" } },
  },
});
```

Elasticsearch is the most natural fit: one request returns the hits page and every facet together.

## 156: How do you translate $bucket?

**MongoDB**

```js
[
  {
    $bucket: {
      groupBy: "$price",
      boundaries: [0, 50, 100, 500],
      default: "500+",
      output: { n: { $sum: 1 } },
    },
  },
];
```

**SQL, Snowflake**

```sql
SELECT CASE WHEN price < 50 THEN '0-50' WHEN price < 100 THEN '50-100' WHEN price < 500 THEN '100-500' ELSE '500+' END AS bucket,
       COUNT(*) AS n
FROM products GROUP BY 1;
-- PostgreSQL also has width_bucket(price, ARRAY[0,50,100,500])
```

**BigQuery**

```sql
SELECT RANGE_BUCKET(price, [0, 50, 100, 500]) AS bucket, COUNT(*) AS n FROM shop.products GROUP BY bucket;
```

**Elasticsearch**

```js
aggs: { prices: { range: { field: "price", ranges: [{ to: 50 }, { from: 50, to: 100 }, { from: 100, to: 500 }, { from: 500 }] } } }
```

## 157: How do you translate $bucketAuto?

**MongoDB**

```js
[{ $bucketAuto: { groupBy: "$price", buckets: 4 } }];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT bucket, MIN(price), MAX(price), COUNT(*)
FROM (SELECT price, NTILE(4) OVER (ORDER BY price) AS bucket FROM products) t
GROUP BY bucket ORDER BY bucket;
```

**Elasticsearch**

```js
aggs: { prices: { variable_width_histogram: { field: "price", buckets: 4 } } }
```

`NTILE` splits rows into groups of nearly equal size, which is what `$bucketAuto` tries to do.

## 158: How do you translate $graphLookup?

**MongoDB**

```js
[
  { $match: { _id: "emp1" } },
  {
    $graphLookup: {
      from: "employees",
      startWith: "$managerId",
      connectFromField: "managerId",
      connectToField: "_id",
      as: "chain",
    },
  },
];
```

**SQL**

```sql
WITH RECURSIVE chain AS (
  SELECT id, manager_id, name FROM employees WHERE id = 'emp1'
  UNION ALL
  SELECT e.id, e.manager_id, e.name FROM employees e JOIN chain c ON e.id = c.manager_id
)
SELECT * FROM chain;
```

**BigQuery**

```sql
WITH RECURSIVE chain AS (
  SELECT id, manager_id, name FROM shop.employees WHERE id = 'emp1'
  UNION ALL
  SELECT e.id, e.manager_id, e.name FROM shop.employees e JOIN chain c ON e.id = c.manager_id
)
SELECT * FROM chain;
```

**Snowflake**

```sql
SELECT id, name FROM employees START WITH id = 'emp1' CONNECT BY id = PRIOR manager_id;
```

**DynamoDB, Firebase, Redis**

Walk the chain in code: read the employee, then the manager, and so on. Or store the full path (`path: "/ceo/cto/emp1"`) on each item so one query by prefix finds the subtree.

Snowflake supports both `WITH RECURSIVE` and `CONNECT BY`. Elasticsearch has no graph traversal.

## 159: How do you translate $unionWith?

**MongoDB**

```js
db.collection("orders2025").aggregate([{ $unionWith: "orders2026" }]);
```

**SQL, BigQuery, Snowflake**

```sql
SELECT * FROM orders2025 UNION ALL SELECT * FROM orders2026;
```

**BigQuery (wildcard tables)**

```sql
SELECT * FROM `shop.orders*` WHERE _TABLE_SUFFIX IN ('2025', '2026');
```

**Elasticsearch**

```js
await es.search({ index: "orders2025,orders2026", query: { match_all: {} } });
```

`$unionWith` keeps duplicates, so `UNION ALL` is the right translation, not `UNION`.

## 160: How do you translate $out?

**MongoDB**

```js
[
  { $group: { _id: "$userId", total: { $sum: "$amount" } } },
  { $out: "userTotals" },
];
```

**SQL**

```sql
DROP TABLE IF EXISTS user_totals;
CREATE TABLE user_totals AS SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id;
```

**BigQuery**

```sql
CREATE OR REPLACE TABLE shop.user_totals AS SELECT user_id, SUM(amount) AS total FROM shop.orders GROUP BY user_id;
```

**Snowflake**

```sql
CREATE OR REPLACE TABLE user_totals AS SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id;
```

**Elasticsearch**

Use a pivot transform (`es.transform.putTransform`) that groups `orders` by `userId` and writes to a `user_totals` index.

`$out` replaces the target collection atomically. `CREATE OR REPLACE TABLE ... AS SELECT` does the same in BigQuery and Snowflake.

## 161: How do you translate $merge?

**MongoDB**

```js
[
  { $group: { _id: "$userId", total: { $sum: "$amount" } } },
  {
    $merge: {
      into: "userTotals",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "insert",
    },
  },
];
```

**SQL**

```sql
INSERT INTO user_totals (user_id, total)
SELECT user_id, SUM(amount) FROM orders GROUP BY user_id
ON CONFLICT (user_id) DO UPDATE SET total = EXCLUDED.total;
```

**BigQuery, Snowflake**

```sql
MERGE INTO user_totals t
USING (SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id) s
ON t.user_id = s.user_id
WHEN MATCHED THEN UPDATE SET total = s.total
WHEN NOT MATCHED THEN INSERT (user_id, total) VALUES (s.user_id, s.total);
```

**Elasticsearch**

A continuous pivot transform keeps the destination index updated as new orders arrive.

## 162: How do you translate $setWindowFields for a running total?

**MongoDB**

```js
[
  {
    $setWindowFields: {
      partitionBy: "$userId",
      sortBy: { createdAt: 1 },
      output: {
        runningTotal: {
          $sum: "$amount",
          window: { documents: ["unbounded", "current"] },
        },
      },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT user_id, created_at, amount,
  SUM(amount) OVER (PARTITION BY user_id ORDER BY created_at ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM orders;
```

**Elasticsearch**

```js
aggs: {
  byDay: {
    date_histogram: { field: "createdAt", calendar_interval: "day" },
    aggs: { amount: { sum: { field: "amount" } }, running: { cumulative_sum: { buckets_path: "amount" } } },
  },
}
```

MongoDB window functions map almost word for word to SQL window functions, which is one of the easiest parts of a translation.

## 163: How do you rank rows within groups ($rank, $denseRank)?

**MongoDB**

```js
[
  {
    $setWindowFields: {
      partitionBy: "$category",
      sortBy: { sales: -1 },
      output: { rank: { $rank: {} } },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT category, name, sales,
  RANK() OVER (PARTITION BY category ORDER BY sales DESC) AS rank,
  DENSE_RANK() OVER (PARTITION BY category ORDER BY sales DESC) AS dense_rank
FROM products;
```

**Redis**

```js
await redis.zRevRank("sales:books", "p1"); // 0-based rank within a sorted set
```

To keep only the top 3 per category, BigQuery and Snowflake let you write `QUALIFY RANK() OVER (...) <= 3` instead of a subquery. PostgreSQL needs a subquery or CTE.

## 164: How do you compute a moving average?

**MongoDB**

```js
[
  {
    $setWindowFields: {
      sortBy: { day: 1 },
      output: { avg7: { $avg: "$sales", window: { documents: [-6, 0] } } },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT day, sales, AVG(sales) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS avg7 FROM daily_sales;
```

**Elasticsearch**

```js
aggs: {
  byDay: {
    date_histogram: { field: "day", calendar_interval: "day" },
    aggs: {
      sales: { sum: { field: "sales" } },
      avg7: { moving_fn: { buckets_path: "sales", window: 7, script: "MovingFunctions.unweightedAvg(values)" } },
    },
  },
}
```

Elasticsearch `moving_fn` uses the previous `window` buckets and by default does not include the current one. Set `shift: 1` to include it.

## 165: How do you translate $first and $last in a $group?

**MongoDB**

```js
[
  { $sort: { createdAt: 1 } },
  {
    $group: {
      _id: "$userId",
      firstOrder: { $first: "$createdAt" },
      lastTotal: { $last: "$total" },
    },
  },
];
```

**SQL**

```sql
SELECT DISTINCT ON (user_id) user_id, total AS last_total
FROM orders ORDER BY user_id, created_at DESC;
```

**BigQuery**

```sql
SELECT user_id,
  MIN(created_at) AS first_order,
  ARRAY_AGG(total ORDER BY created_at DESC LIMIT 1)[OFFSET(0)] AS last_total
FROM shop.orders GROUP BY user_id;
```

**Snowflake**

```sql
SELECT user_id, MIN(created_at) AS first_order, MAX_BY(total, created_at) AS last_total FROM orders GROUP BY user_id;
```

**Elasticsearch**

```js
aggs: { byUser: { terms: { field: "userId" }, aggs: { last: { top_hits: { size: 1, sort: [{ createdAt: "desc" }], _source: ["total"] } } } } }
```

`MAX_BY` / `MIN_BY` in Snowflake (and BigQuery `MAX_BY`) are the shortest way to say "value of X at the latest Y".

## 166: How do you collect values into an array with $push in a $group?

**MongoDB**

```js
[{ $group: { _id: "$userId", orderIds: { $push: "$_id" } } }];
```

**SQL**

```sql
SELECT user_id, array_agg(id ORDER BY created_at) AS order_ids FROM orders GROUP BY user_id;
```

**BigQuery**

```sql
SELECT user_id, ARRAY_AGG(id ORDER BY created_at) AS order_ids FROM shop.orders GROUP BY user_id;
```

**Redis**

```js
REDUCE: [{ type: "TOLIST", property: "@orderId", AS: "orderIds" }];
```

**Snowflake**

```sql
SELECT user_id, ARRAY_AGG(id) WITHIN GROUP (ORDER BY created_at) AS order_ids FROM orders GROUP BY user_id;
```

**Elasticsearch**

```js
aggs: { byUser: { terms: { field: "userId" }, aggs: { ids: { top_hits: { size: 100, _source: ["orderId"] } } } } }
```

Redis `TOLIST` returns distinct values, so it is closer to `$addToSet` than `$push`.

## 167: How do you collect distinct values with $addToSet in a $group?

**MongoDB**

```js
[{ $group: { _id: "$userId", categories: { $addToSet: "$category" } } }];
```

**SQL**

```sql
SELECT user_id, array_agg(DISTINCT category) FROM orders GROUP BY user_id;
```

**BigQuery**

```sql
SELECT user_id, ARRAY_AGG(DISTINCT category) FROM shop.orders GROUP BY user_id;
```

**Redis**

```js
REDUCE: [{ type: "TOLIST", property: "@category", AS: "categories" }];
```

**Snowflake**

```sql
SELECT user_id, ARRAY_UNIQUE_AGG(category) FROM orders GROUP BY user_id;
```

**Elasticsearch**

```js
aggs: { byUser: { terms: { field: "userId" }, aggs: { cats: { terms: { field: "category" } } } } }
```

## 168: How do you translate $topN and $bottomN?

**MongoDB**

```js
[
  {
    $group: {
      _id: "$category",
      top3: { $topN: { n: 3, sortBy: { sales: -1 }, output: "$name" } },
    },
  },
];
```

**SQL**

```sql
SELECT category, name, sales FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) rn FROM products
) t WHERE rn <= 3;
```

**BigQuery**

```sql
SELECT category, ARRAY_AGG(name ORDER BY sales DESC LIMIT 3) AS top3 FROM shop.products GROUP BY category;
```

**Snowflake**

```sql
SELECT category, name FROM products
QUALIFY ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) <= 3;
```

**Elasticsearch**

```js
aggs: { byCat: { terms: { field: "category" }, aggs: { top3: { top_hits: { size: 3, sort: [{ sales: "desc" }] } } } } }
```

## 169: How do you fill gaps in time series ($densify and $fill)?

**MongoDB**

```js
[
  {
    $densify: { field: "day", range: { step: 1, unit: "day", bounds: "full" } },
  },
  { $fill: { output: { sales: { value: 0 } } } },
];
```

**SQL**

```sql
SELECT d::date AS day, COALESCE(s.sales, 0) AS sales
FROM generate_series('2026-11-01'::date, '2026-11-30', interval '1 day') d
LEFT JOIN daily_sales s ON s.day = d::date;
```

**BigQuery**

```sql
SELECT day, IFNULL(s.sales, 0) AS sales
FROM UNNEST(GENERATE_DATE_ARRAY('2026-11-01', '2026-11-30')) AS day
LEFT JOIN shop.daily_sales s USING (day);
```

**Snowflake**

```sql
WITH days AS (
  SELECT DATEADD(day, SEQ4(), '2026-11-01'::DATE) AS day FROM TABLE(GENERATOR(ROWCOUNT => 30))
)
SELECT d.day, COALESCE(s.sales, 0) AS sales FROM days d LEFT JOIN daily_sales s ON s.day = d.day;
```

**Elasticsearch**

```js
date_histogram: { field: "day", calendar_interval: "day", min_doc_count: 0, extended_bounds: { min: "2026-11-01", max: "2026-11-30" } }
```

`$fill` with `method: "locf"` (carry the last value forward) maps to `LAST_VALUE(sales IGNORE NULLS) OVER (ORDER BY day)` in BigQuery and Snowflake.

## 170: How do you group by day or month ($dateTrunc)?

**MongoDB**

```js
[
  {
    $group: {
      _id: { $dateTrunc: { date: "$createdAt", unit: "day" } },
      n: { $sum: 1 },
    },
  },
];
```

**SQL**

```sql
SELECT date_trunc('day', created_at) AS day, COUNT(*) FROM orders GROUP BY 1 ORDER BY 1;
```

**BigQuery**

```sql
SELECT TIMESTAMP_TRUNC(created_at, DAY) AS day, COUNT(*) FROM shop.orders GROUP BY day ORDER BY day;
```

**Redis**

```js
STEPS: [
  { type: "APPLY", expression: "floor(@createdAt / 86400) * 86400", AS: "day" },
  { type: "GROUPBY", properties: "@day", REDUCE: [{ type: "COUNT", AS: "n" }] },
];
```

**Snowflake**

```sql
SELECT DATE_TRUNC('day', created_at) AS day, COUNT(*) FROM orders GROUP BY 1 ORDER BY 1;
```

**Elasticsearch**

```js
aggs: { byDay: { date_histogram: { field: "createdAt", calendar_interval: "day" } } }
```

## 171: How do you add to or subtract dates ($dateAdd, $dateDiff)?

**MongoDB**

```js
[
  {
    $project: {
      dueAt: { $dateAdd: { startDate: "$createdAt", unit: "day", amount: 30 } },
      ageDays: {
        $dateDiff: { startDate: "$createdAt", endDate: "$$NOW", unit: "day" },
      },
    },
  },
];
```

**SQL**

```sql
SELECT created_at + interval '30 days' AS due_at, current_date - created_at::date AS age_days FROM invoices;
```

**BigQuery**

```sql
SELECT TIMESTAMP_ADD(created_at, INTERVAL 30 DAY) AS due_at,
       TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) AS age_days
FROM shop.invoices;
```

**Snowflake**

```sql
SELECT DATEADD(day, 30, created_at) AS due_at, DATEDIFF(day, created_at, CURRENT_TIMESTAMP()) AS age_days FROM invoices;
```

**Elasticsearch**

```js
query: {
  range: {
    createdAt: {
      lt: "now-30d/d";
    }
  }
} // date math in queries
```

Snowflake `DATEDIFF` counts boundaries crossed (calendar days), while BigQuery `TIMESTAMP_DIFF` counts full 24-hour periods. The same two timestamps can give different answers.

## 172: How do you handle time zones when grouping dates?

**MongoDB**

```js
{ $dateTrunc: { date: "$createdAt", unit: "day", timezone: "Asia/Tbilisi" } }
```

**SQL**

```sql
SELECT date_trunc('day', created_at AT TIME ZONE 'Asia/Tbilisi') AS day, COUNT(*) FROM orders GROUP BY 1;
```

**BigQuery**

```sql
SELECT DATE(created_at, 'Asia/Tbilisi') AS day, COUNT(*) FROM shop.orders GROUP BY day;
```

**Snowflake**

```sql
SELECT DATE_TRUNC('day', CONVERT_TIMEZONE('Asia/Tbilisi', created_at)) AS day, COUNT(*) FROM orders GROUP BY 1;
```

**Elasticsearch**

```js
date_histogram: { field: "createdAt", calendar_interval: "day", time_zone: "Asia/Tbilisi" }
```

Store everything in UTC and convert only when grouping or displaying. Otherwise "sales per day" changes depending on which server ran the query.

## 173: How do you filter elements inside an array ($filter)?

**MongoDB**

```js
[
  {
    $project: {
      bigItems: {
        $filter: {
          input: "$items",
          as: "i",
          cond: { $gte: ["$$i.price", 100] },
        },
      },
    },
  },
];
```

**SQL**

```sql
SELECT id, jsonb_path_query_array(items, '$[*] ? (@.price >= 100)') AS big_items FROM orders;
```

**BigQuery**

```sql
SELECT id, ARRAY(SELECT i FROM UNNEST(items) i WHERE i.price >= 100) AS big_items FROM shop.orders;
```

**Redis**

```js
await redis.json.get("order:1", { path: "$.items[?(@.price >= 100)]" });
```

**Snowflake**

```sql
SELECT id, FILTER(items, i -> i:price >= 100) AS big_items FROM orders;
```

**Elasticsearch**

```js
query: { nested: { path: "items", query: { range: { "items.price": { gte: 100 } } }, inner_hits: {} } }
```

`inner_hits` returns only the matching nested items, which is close to `$filter`.

## 174: How do you transform each array element ($map)?

**MongoDB**

```js
[
  {
    $project: {
      skus: { $map: { input: "$items", as: "i", in: { $toUpper: "$$i.sku" } } },
    },
  },
];
```

**SQL**

```sql
SELECT id, ARRAY(SELECT upper(e->>'sku') FROM jsonb_array_elements(items) e) AS skus FROM orders;
```

**BigQuery**

```sql
SELECT id, ARRAY(SELECT UPPER(i.sku) FROM UNNEST(items) i) AS skus FROM shop.orders;
```

**Snowflake**

```sql
SELECT id, TRANSFORM(items, i -> UPPER(i:sku::STRING)) AS skus FROM orders;
```

**Elasticsearch**

```js
script_fields: {
  skus: {
    script: "params._source.items.stream().map(i -> i.sku.toUpperCase()).collect(Collectors.toList())";
  }
}
```

## 175: How do you reduce an array to one value ($reduce)?

**MongoDB**

```js
[
  {
    $project: {
      total: {
        $reduce: {
          input: "$items",
          initialValue: 0,
          in: {
            $add: ["$$value", { $multiply: ["$$this.price", "$$this.qty"] }],
          },
        },
      },
    },
  },
];
```

**SQL**

```sql
SELECT o.id, SUM((e->>'price')::numeric * (e->>'qty')::int) AS total
FROM orders o, jsonb_array_elements(o.items) e GROUP BY o.id;
```

**BigQuery**

```sql
SELECT id, (SELECT SUM(i.price * i.qty) FROM UNNEST(items) i) AS total FROM shop.orders;
```

**Snowflake**

```sql
SELECT id, REDUCE(items, 0, (acc, i) -> acc + i:price * i:qty) AS total FROM orders;
```

**Elasticsearch**

```js
script_fields: {
  total: {
    script: "double t = 0; for (i in params._source.items) { t += i.price * i.qty } return t;";
  }
}
```

Most `$reduce` uses are really a sum, and a sum over the unnested array is easier to read in SQL than a fold.

## 176: How do you translate $objectToArray and $arrayToObject?

**MongoDB**

```js
[{ $project: { pairs: { $objectToArray: "$settings" } } }]; // [{ k: "theme", v: "dark" }, ...]
[{ $project: { settings: { $arrayToObject: "$pairs" } } }];
```

**SQL**

```sql
SELECT key, value FROM users, jsonb_each(settings);
SELECT jsonb_object_agg(key, value) FROM user_settings WHERE user_id = 1;
```

**BigQuery**

```sql
SELECT k, JSON_VALUE(settings, CONCAT('$.', k)) AS v FROM shop.users, UNNEST(JSON_KEYS(settings)) k;
```

**Snowflake**

```sql
SELECT f.key, f.value FROM users, LATERAL FLATTEN(input => settings) f;
SELECT OBJECT_AGG(key, value) FROM user_settings WHERE user_id = 1;
```

**Redis**

```js
await redis.hGetAll("user:1:settings"); // a hash already comes back as an object
```

## 177: How do you merge objects ($mergeObjects)?

**MongoDB**

```js
[{ $project: { settings: { $mergeObjects: ["$defaults", "$overrides"] } } }];
```

**SQL**

```sql
SELECT defaults || overrides AS settings FROM users; -- JSONB, right side wins
```

**BigQuery**

```sql
SELECT JSON_SET(defaults, '$.theme', JSON_QUERY(overrides, '$.theme')) FROM shop.users; -- key by key
```

**Snowflake**

```sql
SELECT OBJECT_INSERT(defaults, 'theme', overrides:theme, TRUE) FROM users; -- TRUE allows overwrite
```

**DynamoDB, Firebase**

```js
await firestore.doc("users/u1").set({ settings: overrides }, { merge: true }); // deep merges maps
```

**Redis**

```js
await redis.json.merge("user:1", "$.settings", overrides); // JSON.MERGE
```

PostgreSQL `||` only merges the top level. Firestore `set` with `merge: true` merges nested maps too.

## 178: How do you translate $switch?

**MongoDB**

```js
{ $switch: { branches: [{ case: { $gte: ["$score", 90] }, then: "A" }, { case: { $gte: ["$score", 75] }, then: "B" }], default: "C" } }
```

**SQL, BigQuery, Snowflake**

```sql
SELECT CASE WHEN score >= 90 THEN 'A' WHEN score >= 75 THEN 'B' ELSE 'C' END AS grade FROM results;
```

**Redis**

```js
STEPS: [
  {
    type: "APPLY",
    expression: 'if(@score >= 90, "A", if(@score >= 75, "B", "C"))',
    AS: "grade",
  },
];
```

**Elasticsearch**

```js
runtime_mappings: {
  grade: { type: "keyword", script: "double s = doc['score'].value; emit(s >= 90 ? 'A' : s >= 75 ? 'B' : 'C')" },
}
```

## 179: How do you translate $regexMatch and $regexFind?

**MongoDB**

```js
[
  {
    $project: {
      isGmail: { $regexMatch: { input: "$email", regex: /@gmail\.com$/ } },
    },
  },
];
```

**SQL**

```sql
SELECT email ~ '@gmail\.com$' AS is_gmail, substring(email FROM '@(.*)$') AS domain FROM users;
```

**BigQuery**

```sql
SELECT REGEXP_CONTAINS(email, r'@gmail\.com$') AS is_gmail, REGEXP_EXTRACT(email, r'@(.*)$') AS domain FROM shop.users;
```

**Snowflake**

```sql
SELECT REGEXP_LIKE(email, '.*@gmail\\.com') AS is_gmail, REGEXP_SUBSTR(email, '@(.*)$', 1, 1, 'e') AS domain FROM users;
```

**Elasticsearch**

```js
runtime_mappings: { domain: { type: "keyword", script: "emit(doc['email'].value.substring(doc['email'].value.indexOf('@') + 1))" } }
```

Snowflake `REGEXP_LIKE` must match the whole string, so it needs `.*` at the start. BigQuery `REGEXP_CONTAINS` matches anywhere, like MongoDB.

## 180: How do you translate $let variables?

**MongoDB**

```js
{ $let: { vars: { total: { $multiply: ["$price", "$qty"] } }, in: { $cond: [{ $gt: ["$$total", 100] }, "$$total", 0] } } }
```

**SQL, BigQuery, Snowflake**

```sql
SELECT CASE WHEN total > 100 THEN total ELSE 0 END
FROM (SELECT price * qty AS total FROM order_items) t;
```

**Elasticsearch**

```js
script: "double total = doc['price'].value * doc['qty'].value; return total > 100 ? total : 0;";
```

Snowflake also lets you use a column alias later in the same `SELECT`, for example `SELECT price * qty AS total, IFF(total > 100, total, 0)`.

## 181: How do you translate cursor-based (keyset) pagination?

**MongoDB**

```js
await db
  .collection("posts")
  .find(
    after
      ? {
          $or: [
            { createdAt: { $lt: after.createdAt } },
            { createdAt: after.createdAt, _id: { $lt: after._id } },
          ],
        }
      : {},
  )
  .sort({ createdAt: -1, _id: -1 })
  .limit(20)
  .toArray();
```

**SQL, Snowflake**

```sql
SELECT * FROM posts
WHERE (created_at, id) < ($1, $2)
ORDER BY created_at DESC, id DESC LIMIT 20;
```

**Redis**

```js
await redis.zRangeByScore("posts:byTime", "-inf", `(${afterScore}`, {
  LIMIT: { offset: 0, count: 20 },
});
```

**DynamoDB**

```js
const page = await ddb.send(
  new QueryCommand({ ...params, Limit: 20, ExclusiveStartKey: cursor }),
);
const nextCursor = page.LastEvaluatedKey; // send it to the client as an opaque token
```

**Firebase**

```js
firestore
  .collection("posts")
  .orderBy("createdAt", "desc")
  .startAfter(lastDocSnapshot)
  .limit(20);
```

**Elasticsearch**

```js
await es.search({
  index: "posts",
  size: 20,
  sort: [{ createdAt: "desc" }, { id: "desc" }],
  search_after: [lastCreatedAt, lastId],
});
```

Always add a unique tie-breaker (`_id`, `id`) to the sort, or rows with the same timestamp can be skipped or shown twice. BigQuery is not built for page-by-page UI reads, so it is left out.

## 182: How do you return a page of results with the total count?

**MongoDB**

```js
[
  { $match: filter },
  {
    $facet: {
      total: [{ $count: "n" }],
      items: [{ $sort: { _id: -1 } }, { $skip: 40 }, { $limit: 20 }],
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
SELECT *, COUNT(*) OVER () AS total FROM products WHERE category = 'books' ORDER BY id DESC LIMIT 20 OFFSET 40;
```

**Redis**

```js
const { total, documents } = await redis.ft.search(
  "idx:products",
  "@category:{books}",
  { LIMIT: { from: 40, size: 20 } },
);
```

**Firebase**

```js
const [page, count] = await Promise.all([
  q.offset(40).limit(20).get(),
  q.count().get(),
]);
```

**Elasticsearch**

```js
const res = await es.search({
  index: "products",
  from: 40,
  size: 20,
  track_total_hits: true,
  query,
});
res.hits.total.value;
```

Elasticsearch stops counting at 10,000 by default and reports `"relation": "gte"`. Set `track_total_hits: true` for an exact number, at a cost.

## 183: How do you translate an update with an aggregation pipeline?

**MongoDB**

```js
await db
  .collection("users")
  .updateMany({}, [
    { $set: { fullName: { $concat: ["$first", " ", "$last"] } } },
  ]);
```

**SQL, BigQuery, Snowflake**

```sql
UPDATE users SET full_name = first || ' ' || last WHERE TRUE;
```

**Redis**

No server-side update that reads other fields, except a Lua script or function.

**DynamoDB**

```js
UpdateExpression: "SET total = price + shipping", // only + and - between attributes
```

**Elasticsearch**

```js
await es.updateByQuery({
  index: "users",
  script: {
    source: "ctx._source.fullName = ctx._source.first + ' ' + ctx._source.last",
  },
});
```

In SQL, "set a column from other columns" is just a normal `UPDATE`. It is one of the few things that is simpler than in MongoDB.

## 184: How do you translate arrayFilters?

**MongoDB**

```js
await db
  .collection("orders")
  .updateOne(
    { _id: id },
    { $set: { "items.$[i].status": "shipped" } },
    { arrayFilters: [{ "i.warehouse": "A" }] },
  );
```

**SQL**

```sql
UPDATE order_items SET status = 'shipped' WHERE order_id = 1 AND warehouse = 'A';
```

**BigQuery**

```sql
UPDATE shop.orders
SET items = ARRAY(SELECT AS STRUCT i.* REPLACE (IF(i.warehouse = 'A', 'shipped', i.status) AS status) FROM UNNEST(items) i)
WHERE id = 'o1';
```

**Redis**

```js
await redis.json.set(
  "order:o1",
  '$.items[?(@.warehouse=="A")].status',
  "shipped",
);
```

**Elasticsearch**

```js
script: {
  source: "for (i in ctx._source.items) { if (i.warehouse == 'A') { i.status = 'shipped' } }";
}
```

RedisJSON's JSONPath filter is the closest one-line match to `arrayFilters`.

## 185: How do you keep a capped list inside a document ($push with $each, $sort, $slice)?

**MongoDB**

```js
await db
  .collection("users")
  .updateOne(
    { _id: id },
    { $push: { recent: { $each: [item], $sort: { at: -1 }, $slice: 10 } } },
  );
```

**SQL**

```sql
INSERT INTO user_recent (user_id, item, at) VALUES (1, 'x', now());
DELETE FROM user_recent WHERE user_id = 1 AND at < (
  SELECT at FROM user_recent WHERE user_id = 1 ORDER BY at DESC OFFSET 9 LIMIT 1
);
```

**Redis**

```js
await redis
  .multi()
  .lPush("user:1:recent", item)
  .lTrim("user:1:recent", 0, 9)
  .exec();
```

**DynamoDB**

Read the list, add and trim in code, then write it back with a condition on a version number.

**Firebase**

Same as DynamoDB, inside `runTransaction`.

A "last 10 viewed" list is a perfect fit for Redis `LPUSH` + `LTRIM`.

## 186: How do you increment a field inside a map of counters?

**MongoDB**

```js
await db
  .collection("stats")
  .updateOne(
    { _id: "2026-11-26" },
    { $inc: { "byCountry.GE": 1 } },
    { upsert: true },
  );
```

**SQL**

```sql
INSERT INTO stats (day, country, n) VALUES ('2026-11-26', 'GE', 1)
ON CONFLICT (day, country) DO UPDATE SET n = stats.n + 1;
```

**Redis**

```js
await redis.hIncrBy("stats:2026-11-26", "GE", 1);
```

**DynamoDB**

```js
// one item per day and country
new UpdateCommand({
  TableName: "Stats",
  Key: { pk: "STATS#2026-11-26", sk: "COUNTRY#GE" },
  UpdateExpression: "ADD n :one",
  ExpressionAttributeValues: { ":one": 1 },
});
```

**Firebase**

```js
await firestore
  .doc("stats/2026-11-26")
  .set({ byCountry: { GE: FieldValue.increment(1) } }, { merge: true });
```

DynamoDB cannot `ADD` into a nested map path that does not exist yet, so one item per counter is the simpler design.

## 187: How do you translate optimistic locking with a version field?

**MongoDB**

```js
const res = await db
  .collection("docs")
  .updateOne({ _id: id, version: 3 }, { $set: { body }, $inc: { version: 1 } });
if (res.matchedCount === 0) throw new Error("Someone else changed it");
```

**SQL, Snowflake**

```sql
UPDATE docs SET body = $1, version = version + 1 WHERE id = $2 AND version = 3; -- check rowCount
```

**Redis**

```js
const c = await redis.duplicate().connect(); // WATCH needs its own connection
await c.watch("doc:1");
const doc = await c.json.get("doc:1");
await c.multi().json.set("doc:1", "$.body", newBody).exec(); // fails if doc:1 changed after WATCH
await c.close();
```

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Docs",
  Key: { id },
  UpdateExpression: "SET body = :b, version = version + :one",
  ConditionExpression: "version = :v",
  ExpressionAttributeValues: { ":b": body, ":v": 3, ":one": 1 },
});
```

**Firebase**

```js
await firestore
  .doc("docs/d1")
  .update({ body }, { lastUpdateTime: snap.updateTime }); // precondition
```

**Elasticsearch**

```js
await es.index({
  index: "docs",
  id,
  document,
  if_seq_no: 12,
  if_primary_term: 1,
}); // 409 on conflict
```

## 188: How do you translate change streams?

**MongoDB**

```js
const stream = db
  .collection("orders")
  .watch([{ $match: { operationType: "insert" } }]);
for await (const change of stream) console.log(change.fullDocument);
```

**SQL**

PostgreSQL logical replication (read with Debezium or a library like `pg-logical-replication`), or `LISTEN`/`NOTIFY` from a trigger for simple cases.

**BigQuery**

No change feed out of BigQuery. Use the `APPENDS` / `CHANGES` table-valued functions to read what changed between two times.

**Redis**

```js
// write changes to a stream and read them
for (;;) {
  const res = await redis.xRead(
    { key: "orders:changes", id: lastId },
    { BLOCK: 0 },
  );
  /* handle res */
}
```

**Snowflake**

```sql
CREATE STREAM orders_changes ON TABLE orders;
SELECT * FROM orders_changes; -- rows changed since the stream was last used in a DML
```

**DynamoDB**

Turn on DynamoDB Streams (`NEW_AND_OLD_IMAGES`) and attach a Lambda function.

**Firebase**

```js
import { onDocumentCreated } from "firebase-functions/v2/firestore";
export const onOrder = onDocumentCreated("orders/{id}", (event) =>
  console.log(event.data.data()),
);
```

**Elasticsearch**

No change feed. Poll with a query on an `updatedAt` field, or send changes from the source system.

## 189: How do you resume a change feed after a crash (resume tokens)?

**MongoDB**

```js
const stream = db.collection("orders").watch([], { resumeAfter: savedToken });
for await (const change of stream) {
  await handle(change);
  await saveToken(change._id);
}
```

**SQL**

Logical replication slots remember the last confirmed LSN. Debezium stores its offset in Kafka.

**Redis**

```js
await redis.xReadGroup("workers", "w1", { key: "orders:changes", id: ">" });
await redis.xAck("orders:changes", "workers", messageId); // unacked messages can be claimed again
```

**Snowflake**

A stream's offset moves forward only when a DML statement that reads it commits, so a failed job simply reads the same rows again.

**DynamoDB**

The Lambda event source mapping tracks the shard position for you. Records are kept for 24 hours.

**Firebase**

Cloud Functions triggers are delivered at least once. There is no token to save, but handlers must be idempotent.

A MongoDB resume token only works while the matching entry is still in the oplog. Redis consumer groups, DynamoDB Streams (24 hours) and replication slots have similar limits.

## 190: How do you translate partial indexes?

**MongoDB**

```js
await db
  .collection("orders")
  .createIndex(
    { createdAt: 1 },
    { partialFilterExpression: { status: "open" } },
  );
```

**SQL**

```sql
CREATE INDEX orders_open_idx ON orders (created_at) WHERE status = 'open';
```

**Redis**

```js
await redis.ft.create("idx:openOrders", schema, {
  ON: "JSON",
  PREFIX: "order:",
  FILTER: "@status == 'open'",
});
```

**DynamoDB**

A sparse GSI: only items that have the GSI key attribute are indexed. Set `openSince` only on open orders and remove it when they close.

**Firebase**

Not supported. Firestore indexes every document in the collection group.

**Elasticsearch**

Put open orders in their own index or alias, or filter at query time (filters are cached).

## 191: How do you translate sparse indexes?

**MongoDB**

```js
await db
  .collection("users")
  .createIndex({ referralCode: 1 }, { sparse: true, unique: true });
```

**SQL**

```sql
CREATE UNIQUE INDEX ON users (referral_code) WHERE referral_code IS NOT NULL;
```

**DynamoDB**

A GSI on `referralCode` is sparse automatically, because items without that attribute are not written to the index.

**Firebase**

Single-field indexes skip documents without the field, which is why `orderBy("x")` also filters out documents missing `x`.

In PostgreSQL, unique indexes already allow many `NULL` values by default, so the `WHERE` clause is about index size more than about uniqueness.

## 192: How do multikey (array) indexes translate?

**MongoDB**

```js
await db.collection("posts").createIndex({ tags: 1 }); // one index entry per array element
```

**SQL**

```sql
CREATE INDEX posts_tags_gin ON posts USING GIN (tags);
SELECT * FROM posts WHERE tags @> ARRAY['node'];
```

**BigQuery**

```sql
CREATE SEARCH INDEX posts_search ON shop.posts (tags);
```

**Redis**

```js
{ "$.tags[*]": { type: "TAG", AS: "tags" } }
```

**Snowflake**

```sql
ALTER TABLE posts ADD SEARCH OPTIMIZATION ON EQUALITY(tags);
```

**DynamoDB**

No index on list elements. Write one extra item per tag (`pk: "TAG#node", sk: "POST#p1"`) to look posts up by tag.

**Firebase**

Arrays are indexed automatically for `array-contains`.

**Elasticsearch**

Arrays are indexed like any other values. No extra work.

## 193: How do you translate a text index with field weights?

**MongoDB**

```js
await db
  .collection("posts")
  .createIndex(
    { title: "text", body: "text" },
    { weights: { title: 10, body: 1 } },
  );
```

**SQL**

```sql
ALTER TABLE posts ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
  setweight(to_tsvector('english', title), 'A') || setweight(to_tsvector('english', body), 'D')
) STORED;
CREATE INDEX ON posts USING GIN (tsv);
SELECT *, ts_rank(tsv, q) AS score FROM posts, websearch_to_tsquery('english', 'mongo') q WHERE tsv @@ q ORDER BY score DESC;
```

**Redis**

```js
await redis.ft.create(
  "idx:posts",
  {
    "$.title": { type: "TEXT", WEIGHT: 10, AS: "title" },
    "$.body": { type: "TEXT", AS: "body" },
  },
  { ON: "JSON", PREFIX: "post:" },
);
```

**Elasticsearch**

```js
query: { multi_match: { query: "mongo", fields: ["title^10", "body"] } }
```

Elasticsearch sets weights (boosts) per query, not in the index, so you can tune them without rebuilding anything.

## 194: How do you translate wildcard indexes?

**MongoDB**

```js
await db.collection("products").createIndex({ "attributes.$**": 1 });
```

**SQL**

```sql
CREATE INDEX ON products USING GIN (attributes jsonb_path_ops);
SELECT * FROM products WHERE attributes @> '{"color": "red"}';
```

**BigQuery**

```sql
CREATE SEARCH INDEX products_attrs ON shop.products (ALL COLUMNS);
```

**Snowflake**

```sql
ALTER TABLE products ADD SEARCH OPTIMIZATION ON EQUALITY(attributes);
```

**Elasticsearch**

```js
mappings: {
  properties: {
    attributes: {
      type: "flattened";
    }
  }
}
// or dynamic templates that map every new key under attributes as keyword
```

Firestore indexes every field automatically, which already works like a wildcard index for single-field queries.

## 195: How do you translate hashed indexes?

**MongoDB**

```js
await db.collection("events").createIndex({ deviceId: "hashed" }); // used for hashed sharding
```

**SQL**

```sql
CREATE INDEX ON events USING HASH (device_id);
```

**DynamoDB**

The partition key is always hashed to pick the storage partition. That is the DynamoDB version of a hashed shard key.

**Elasticsearch**

Documents are routed to shards by a hash of `_id` (or of a custom `routing` value).

Hash indexes in every system support only equality lookups, not ranges or sorting.

## 196: How do covered queries translate?

**MongoDB**

```js
// index { email: 1, name: 1 }; the query reads only indexed fields
await db
  .collection("users")
  .find({ email }, { projection: { _id: 0, email: 1, name: 1 } })
  .toArray();
```

**SQL**

```sql
CREATE INDEX ON users (email) INCLUDE (name);
SELECT email, name FROM users WHERE email = 'a@b.com'; -- index-only scan
```

**DynamoDB**

```js
Projection: { ProjectionType: "INCLUDE", NonKeyAttributes: ["name"] } // GSI returns these without the base table
```

**Elasticsearch**

```js
await es.search({
  index: "users",
  _source: false,
  docvalue_fields: ["email", "name"],
  query,
});
```

In BigQuery and Snowflake, every query is "covered" in a sense: they read only the columns you name.

## 197: How do you force a specific index (hint)?

**MongoDB**

```js
await db
  .collection("orders")
  .find(filter)
  .hint({ userId: 1, createdAt: -1 })
  .toArray();
```

**SQL**

PostgreSQL has no hints. Fix statistics (`ANALYZE`), rewrite the query, or use the `pg_hint_plan` extension.

**DynamoDB**

```js
new QueryCommand({
  TableName: "Orders",
  IndexName: "status-createdAt-index" /* ... */,
});
```

**Firebase**

Firestore picks the index. You cannot choose.

In DynamoDB you always pick the index yourself with `IndexName`, so "hint" is not an extra feature, it is how every query works.

## 198: How do you translate collation (case-insensitive sort and compare)?

**MongoDB**

```js
await db
  .collection("users")
  .createIndex({ name: 1 }, { collation: { locale: "en", strength: 2 } });
await db
  .collection("users")
  .find({ name: "ana" })
  .collation({ locale: "en", strength: 2 })
  .toArray();
```

**SQL**

```sql
CREATE COLLATION ci (provider = icu, locale = 'und-u-ks-level2', deterministic = false);
CREATE TABLE users (name TEXT COLLATE ci);
```

**BigQuery**

```sql
SELECT * FROM shop.users WHERE COLLATE(name, 'und:ci') = 'ana';
```

**Snowflake**

```sql
CREATE TABLE users (name VARCHAR COLLATE 'en-ci');
```

**Elasticsearch**

```js
settings: { analysis: { normalizer: { lower: { type: "custom", filter: ["lowercase", "asciifolding"] } } } },
mappings: { properties: { name: { type: "keyword", normalizer: "lower" } } },
```

DynamoDB and Firestore compare bytes only. Store a normalized copy (`nameLower`) for case-insensitive lookups and sorting.

## 199: How does the ESR rule for compound indexes translate?

In MongoDB, a good compound index puts **E**quality fields first, then **S**ort fields, then **R**ange fields. For `find({ status: "paid", total: { $gt: 100 } }).sort({ createdAt: -1 })`, the index is `{ status: 1, createdAt: -1, total: 1 }`.

- **SQL:** the same idea works for B-tree indexes: `CREATE INDEX ON orders (status, created_at DESC, total);`.
- **DynamoDB:** equality goes into the partition key and sort/range goes into the sort key: `pk = "STATUS#paid"`, `sk = createdAt`. Extra ranges become a `FilterExpression` or part of a composite sort key.
- **Firebase:** composite index fields in the order `status ASC, createdAt DESC, total ASC`, and Firestore will tell you if one is missing.
- **BigQuery, Snowflake:** no B-tree indexes. Partition by date and cluster by the equality columns (`status`) instead.
- **Elasticsearch, Redis:** every field is indexed on its own, so there is no order to think about.

## 200: How do you find the nearest places ($near, $geoNear)?

**MongoDB**

```js
await db
  .collection("shops")
  .find({
    location: {
      $near: {
        $geometry: { type: "Point", coordinates: [44.79, 41.71] },
        $maxDistance: 2000,
      },
    },
  })
  .toArray();
```

**SQL**

```sql
SELECT name, ST_Distance(location, ST_MakePoint(44.79, 41.71)::geography) AS meters
FROM shops
WHERE ST_DWithin(location, ST_MakePoint(44.79, 41.71)::geography, 2000)
ORDER BY location <-> ST_MakePoint(44.79, 41.71)::geography LIMIT 20;
```

**BigQuery**

```sql
SELECT name, ST_DISTANCE(location, ST_GEOGPOINT(44.79, 41.71)) AS meters
FROM shop.shops WHERE ST_DWITHIN(location, ST_GEOGPOINT(44.79, 41.71), 2000) ORDER BY meters;
```

**Redis**

```js
await redis.geoSearchWith(
  "shops",
  { longitude: 44.79, latitude: 41.71 },
  { radius: 2, unit: "km" },
  ["WITHDIST"],
  { SORT: "ASC" },
);
```

**Snowflake**

```sql
SELECT name, ST_DISTANCE(location, ST_MAKEPOINT(44.79, 41.71)) AS meters
FROM shops WHERE ST_DWITHIN(location, ST_MAKEPOINT(44.79, 41.71), 2000) ORDER BY meters;
```

**Firebase**

Query a geohash range (with the `geofire-common` library) and then filter by real distance in code.

**Elasticsearch**

```js
query: { geo_distance: { distance: "2km", location: { lat: 41.71, lon: 44.79 } } },
sort: [{ _geo_distance: { location: { lat: 41.71, lon: 44.79 }, order: "asc", unit: "m" } }],
```

## 201: How do you find points inside an area ($geoWithin)?

**MongoDB**

```js
await db
  .collection("shops")
  .find({
    location: {
      $geoWithin: {
        $geometry: {
          type: "Polygon",
          coordinates: [
            [
              [44.7, 41.6],
              [44.9, 41.6],
              [44.9, 41.8],
              [44.7, 41.8],
              [44.7, 41.6],
            ],
          ],
        },
      },
    },
  })
  .toArray();
```

**SQL**

```sql
SELECT * FROM shops WHERE ST_Within(location::geometry, ST_GeomFromText('POLYGON((44.7 41.6, 44.9 41.6, 44.9 41.8, 44.7 41.8, 44.7 41.6))', 4326));
```

**BigQuery**

```sql
SELECT * FROM shop.shops WHERE ST_WITHIN(location, ST_GEOGFROMTEXT('POLYGON((44.7 41.6, 44.9 41.6, 44.9 41.8, 44.7 41.8, 44.7 41.6))'));
```

**Redis**

```js
await redis.geoSearch(
  "shops",
  { longitude: 44.8, latitude: 41.7 },
  { width: 20, height: 20, unit: "km" },
); // box only
```

**Snowflake**

```sql
SELECT * FROM shops WHERE ST_WITHIN(location, TO_GEOGRAPHY('POLYGON((44.7 41.6, 44.9 41.6, 44.9 41.8, 44.7 41.8, 44.7 41.6))'));
```

**Elasticsearch**

```js
query: {
  geo_shape: {
    location: { shape: { type: "polygon", coordinates: [[[44.7, 41.6], [44.9, 41.6], [44.9, 41.8], [44.7, 41.8], [44.7, 41.6]]] }, relation: "within" },
  },
}
```

Redis supports only circles and boxes. For a real polygon, filter the box results in code, or use a `GEOSHAPE` field in the Redis Query Engine.

## 202: How do you translate Atlas Search?

**MongoDB**

```js
[
  {
    $search: {
      index: "default",
      text: { query: "wireless headphones", path: ["name", "description"] },
    },
  },
  { $limit: 10 },
];
```

**SQL**

```sql
SELECT * FROM products
WHERE search_tsv @@ websearch_to_tsquery('english', 'wireless headphones')
ORDER BY ts_rank(search_tsv, websearch_to_tsquery('english', 'wireless headphones')) DESC LIMIT 10;
```

**BigQuery**

```sql
SELECT * FROM shop.products WHERE SEARCH((name, description), 'wireless headphones') LIMIT 10;
```

**Redis**

```js
await redis.ft.search("idx:products", "wireless headphones", {
  LIMIT: { from: 0, size: 10 },
});
```

**Snowflake**

```sql
SELECT * FROM products WHERE SEARCH((name, description), 'wireless headphones') LIMIT 10;
-- or Cortex Search for ranked, semantic search
```

**Elasticsearch**

```js
await es.search({
  index: "products",
  size: 10,
  query: {
    multi_match: {
      query: "wireless headphones",
      fields: ["name", "description"],
    },
  },
});
```

Atlas Search is built on Apache Lucene, the same engine under Elasticsearch, so Elasticsearch is the closest translation. BigQuery and Snowflake `SEARCH` find matching tokens but do not rank by relevance.

## 203: How do you translate autocomplete search?

**MongoDB**

```js
[{ $search: { autocomplete: { query: "head", path: "name" } } }, { $limit: 5 }];
```

**SQL**

```sql
CREATE EXTENSION pg_trgm;
CREATE INDEX ON products USING GIN (name gin_trgm_ops);
SELECT name FROM products WHERE name ILIKE 'head%' LIMIT 5;
```

**Redis**

```js
await redis.ft.sugAdd("ac:products", "Headphones", 1);
await redis.ft.sugGet("ac:products", "head", { FUZZY: true, MAX: 5 });
```

**DynamoDB**

```js
KeyConditionExpression: "pk = :p AND begins_with(sk, :q)",
ExpressionAttributeValues: { ":p": "PRODUCT_NAME", ":q": "head" }, // lowercase names as sort keys
```

**Firebase**

```js
firestore
  .collection("products")
  .where("nameLower", ">=", "head")
  .where("nameLower", "<", "head")
  .limit(5);
```

**Elasticsearch**

```js
mappings: { properties: { name: { type: "search_as_you_type" } } }
query: { multi_match: { query: "head", type: "bool_prefix", fields: ["name", "name._2gram", "name._3gram"] } }
```

## 204: How do you translate fuzzy search (typo tolerance)?

**MongoDB**

```js
[
  {
    $search: {
      text: { query: "hedphones", path: "name", fuzzy: { maxEdits: 1 } },
    },
  },
];
```

**SQL**

```sql
SELECT name, similarity(name, 'hedphones') AS s FROM products WHERE name % 'hedphones' ORDER BY s DESC;
```

**BigQuery**

```sql
SELECT name FROM shop.products WHERE EDIT_DISTANCE(LOWER(name), 'hedphones') <= 2;
```

**Redis**

```js
await redis.ft.search("idx:products", "%hedphones%"); // one % per allowed edit
```

**Snowflake**

```sql
SELECT name FROM products WHERE EDITDISTANCE(LOWER(name), 'hedphones') <= 2;
```

**Elasticsearch**

```js
query: { match: { name: { query: "hedphones", fuzziness: "AUTO" } } }
```

BigQuery and Snowflake compute edit distance on every row, so it is fine for analytics but too slow for a search box on large tables.

## 205: How do you sort search results by relevance score?

**MongoDB**

```js
await db
  .collection("posts")
  .find(
    { $text: { $search: "redis cache" } },
    { projection: { score: { $meta: "textScore" } } },
  )
  .sort({ score: { $meta: "textScore" } })
  .toArray();
```

**SQL**

```sql
SELECT *, ts_rank(tsv, q) AS score FROM posts, plainto_tsquery('english', 'redis cache') q WHERE tsv @@ q ORDER BY score DESC;
```

**Redis**

```js
await redis.ft.search("idx:posts", "redis cache", {
  WITHSCORES: true,
  SCORER: "BM25",
});
```

**Elasticsearch**

```js
await es.search({ index: "posts", query: { match: { body: "redis cache" } } }); // sorted by _score by default
```

Elasticsearch and Redis both use BM25 scoring by default. PostgreSQL `ts_rank` is simpler and does not consider how rare a word is across all documents.

## 206: How do you translate compound search queries (must, should, filter)?

**MongoDB**

```js
[
  {
    $search: {
      compound: {
        must: [{ text: { query: "laptop", path: "name" } }],
        should: [{ text: { query: "lightweight", path: "description" } }],
        filter: [{ range: { path: "price", lte: 1500 } }],
        mustNot: [{ equals: { path: "inStock", value: false } }],
      },
    },
  },
];
```

**Redis**

```js
await redis.ft.search(
  "idx:products",
  "@name:laptop ~@description:lightweight @price:[-inf 1500] -@inStock:{false}",
);
```

**Elasticsearch**

```js
query: {
  bool: {
    must: [{ match: { name: "laptop" } }],
    should: [{ match: { description: "lightweight" } }],
    filter: [{ range: { price: { lte: 1500 } } }],
    must_not: [{ term: { inStock: false } }],
  },
}
```

Atlas Search `compound` and Elasticsearch `bool` are nearly the same structure. In Redis, `~` marks an optional clause that only raises the score. Filters do not affect the score in either Elasticsearch or Atlas Search, and they can be cached.

## 207: How do you highlight matched words in search results?

**MongoDB**

```js
[
  {
    $search: {
      text: { query: "redis", path: "body" },
      highlight: { path: "body" },
    },
  },
  { $project: { highlights: { $meta: "searchHighlights" } } },
];
```

**SQL**

```sql
SELECT ts_headline('english', body, plainto_tsquery('english', 'redis')) FROM posts WHERE tsv @@ plainto_tsquery('english', 'redis');
```

**Redis**

```js
await redis.ft.search("idx:posts", "redis", {
  HIGHLIGHT: { FIELDS: ["body"], TAGS: { open: "<b>", close: "</b>" } },
});
```

**Elasticsearch**

```js
await es.search({
  index: "posts",
  query: { match: { body: "redis" } },
  highlight: { fields: { body: {} } },
});
```

## 208: How do you translate time series collections?

**MongoDB**

```js
await db.createCollection("metrics", {
  timeseries: { timeField: "ts", metaField: "sensor", granularity: "minutes" },
  expireAfterSeconds: 60 * 60 * 24 * 30,
});
```

**SQL**

```sql
CREATE TABLE metrics (ts TIMESTAMPTZ NOT NULL, sensor TEXT, value DOUBLE PRECISION) PARTITION BY RANGE (ts);
-- or the TimescaleDB extension: SELECT create_hypertable('metrics', 'ts');
```

**BigQuery**

```sql
CREATE TABLE shop.metrics (ts TIMESTAMP, sensor STRING, value FLOAT64)
PARTITION BY DATE(ts) CLUSTER BY sensor OPTIONS (partition_expiration_days = 30);
```

**Redis**

```js
await redis.ts.create("ts:sensor:1", {
  RETENTION: 30 * 86400 * 1000,
  LABELS: { sensor: "1" },
});
await redis.ts.add("ts:sensor:1", "*", 21.5);
```

**Snowflake**

```sql
CREATE TABLE metrics (ts TIMESTAMP_NTZ, sensor VARCHAR, value FLOAT) CLUSTER BY (TO_DATE(ts), sensor);
```

**DynamoDB**

```js
{ pk: "SENSOR#1#2026-11-26", sk: "2026-11-26T10:00:00Z", value: 21.5, ttl: 1767225600 }
```

**Elasticsearch**

```js
await es.indices.putIndexTemplate({
  name: "metrics",
  index_patterns: ["metrics-*"],
  data_stream: {},
  template: {
    settings: { "index.mode": "time_series", "index.routing_path": ["sensor"] },
    mappings: {
      properties: {
        sensor: { type: "keyword", time_series_dimension: true },
        value: { type: "double", time_series_metric: "gauge" },
      },
    },
  },
});
```

In DynamoDB, adding the day to the partition key keeps one busy sensor from filling a single partition forever.

## 209: How do you change schema rules on a live collection (validationLevel)?

**MongoDB**

```js
await db.command({
  collMod: "users",
  validator: { $jsonSchema: { required: ["email", "plan"] } },
  validationLevel: "moderate", // only checks inserts and docs that already pass
  validationAction: "warn",
});
```

**SQL**

```sql
ALTER TABLE users ADD CONSTRAINT plan_set CHECK (plan IS NOT NULL) NOT VALID; -- new rows only
ALTER TABLE users VALIDATE CONSTRAINT plan_set; -- later, after the backfill
```

**Snowflake, BigQuery**

Only `NOT NULL` and types are enforced, so you backfill first and then `ALTER COLUMN ... SET NOT NULL`.

**Elasticsearch**

Mappings can only grow. A stricter type or a removed field needs a new index and a reindex.

PostgreSQL `NOT VALID` is the closest match to `validationLevel: "moderate"`: it checks new writes right away and lets you validate old rows later.

## 210: How do you translate the polymorphic pattern (different shapes in one collection)?

**MongoDB**

```js
{ _id: 1, type: "book", title: "X", pages: 300 }
{ _id: 2, type: "movie", title: "Y", minutes: 120 }
```

**SQL**

```sql
-- one table with a type column and nullable columns, or a base table plus one table per type
CREATE TABLE products (id BIGINT PRIMARY KEY, type TEXT NOT NULL, title TEXT, pages INT, minutes INT);
-- or keep the extra fields in JSONB
CREATE TABLE products (id BIGINT PRIMARY KEY, type TEXT NOT NULL, title TEXT, details JSONB);
```

**BigQuery**

```sql
CREATE TABLE shop.products (id STRING, type STRING, title STRING, book STRUCT<pages INT64>, movie STRUCT<minutes INT64>);
```

**Snowflake**

```sql
CREATE TABLE products (id NUMBER, type VARCHAR, title VARCHAR, details VARIANT);
```

**DynamoDB, Firebase, Redis**

Store them as they are, with a `type` field. These databases are schemaless, so the pattern carries over directly.

**Elasticsearch**

One index with all fields mapped works if types share most fields. Very different types belong in separate indices to avoid sparse mappings.

## 211: How do you translate the bucket pattern?

**MongoDB**

```js
// one document per sensor per hour, readings pushed into it
await db
  .collection("readings")
  .updateOne(
    { sensor: "s1", hour: new Date("2026-11-26T10:00Z"), count: { $lt: 200 } },
    { $push: { values: { t: now, v: 21.5 } }, $inc: { count: 1 } },
    { upsert: true },
  );
```

**SQL, BigQuery, Snowflake**

Store one row per reading. Columnar warehouses compress repeated sensor and hour values very well, so manual bucketing is not needed.

**Redis**

```js
await redis.ts.add("ts:s1", Date.now(), 21.5); // TimeSeries already stores data in compressed chunks
```

**DynamoDB**

```js
{ pk: "SENSOR#s1", sk: "2026-11-26T10", values: [/* up to a safe size under 400 KB */] }
```

**Firebase**

Same as MongoDB: one document per sensor per hour with an array of readings, but watch the 1 MiB document limit and the write rate per document.

**Elasticsearch**

One document per reading in a time series data stream.

The bucket pattern exists in MongoDB to cut index size and document count. Most targets either handle that themselves (warehouses, Redis TimeSeries, Elasticsearch TSDS) or punish big growing items (DynamoDB, Firestore).

## 212: How do you translate the computed pattern (precomputed totals)?

**MongoDB**

```js
await db
  .collection("products")
  .updateOne({ _id: pid }, { $inc: { reviewCount: 1, ratingSum: 5 } });
```

**SQL**

```sql
CREATE MATERIALIZED VIEW product_ratings AS
SELECT product_id, COUNT(*) AS review_count, AVG(rating) AS avg_rating FROM reviews GROUP BY product_id;
-- or update counter columns in the same transaction as the insert
```

**BigQuery**

```sql
CREATE MATERIALIZED VIEW shop.product_ratings AS
SELECT product_id, COUNT(*) AS review_count, AVG(rating) AS avg_rating FROM shop.reviews GROUP BY product_id;
```

**Redis**

```js
await redis.hIncrBy(`product:${pid}:rating`, "count", 1);
await redis.hIncrBy(`product:${pid}:rating`, "sum", 5);
```

**Snowflake**

```sql
CREATE DYNAMIC TABLE product_ratings TARGET_LAG = '5 minutes' WAREHOUSE = app_wh AS
SELECT product_id, COUNT(*) AS review_count, AVG(rating) AS avg_rating FROM reviews GROUP BY product_id;
```

**DynamoDB**

```js
UpdateExpression: "ADD reviewCount :one, ratingSum :r",
```

**Firebase**

```js
await firestore.doc(`products/${pid}`).update({
  reviewCount: FieldValue.increment(1),
  ratingSum: FieldValue.increment(5),
});
```

## 213: How do you translate the subset pattern?

The subset pattern keeps only the most used part of a big list (for example, the 10 newest reviews) inside the main document, and the rest in another collection.

- **SQL:** no need. Query the reviews table with `ORDER BY created_at DESC LIMIT 10`, which is fast with an index.
- **BigQuery, Snowflake:** not needed for analytics.
- **Redis:** keep the 10 newest review ids in a list with `LPUSH` + `LTRIM`.
- **DynamoDB:** store the 10 newest reviews on the product item for a single `GetItem`, and all reviews as separate items under `pk = PRODUCT#id`.
- **Firebase:** keep `recentReviews` (10 items) on the product document and the full list in a `reviews` subcollection.
- **Elasticsearch:** index reviews separately. Copy a few top ones into the product document only if the search page shows them.

## 214: How do you translate the extended reference pattern?

The extended reference pattern copies a few fields from a related document (like the customer's name and city into each order) so reads do not need a `$lookup`.

- **SQL:** usually not needed, a join is cheap. Copy only values that must stay frozen in time, like the shipping address at order time.
- **BigQuery, Snowflake:** copying is common, because wide denormalized tables are faster to scan than joins.
- **DynamoDB, Firebase:** copying is the normal way to avoid extra reads, since there are no joins. Keep copies in sync with streams or Cloud Functions triggers.
- **Elasticsearch:** required. Copy what you search or filter on into each document.
- **Redis:** store the copied fields in the order's hash or JSON.

## 215: How do you translate the outlier pattern?

In MongoDB, the outlier pattern handles rare documents that would break limits, like a celebrity with millions of followers. Most documents embed their list, and outliers set `hasOverflow: true` and keep the rest in another collection.

- **SQL:** not needed. A follows table handles one follower or ten million the same way.
- **DynamoDB:** the same problem shows up as a hot or huge partition. Split the outlier's data across several partition keys (`USER#123#0` to `USER#123#9`) and read them in parallel.
- **Firebase:** outliers hit the 1 MiB document limit and write rate limits. Move their lists into subcollections and shard counters.
- **Redis:** big keys slow down the server. Split very large sets or hashes across several keys.
- **Elasticsearch:** very large arrays in one document slow indexing. Index followers as separate documents.

## 216: How do you translate the attribute pattern?

**MongoDB**

```js
{ name: "Shirt", attrs: [{ k: "color", v: "red" }, { k: "size", v: "M" }] }
await db.collection("products").createIndex({ "attrs.k": 1, "attrs.v": 1 });
await db.collection("products").find({ attrs: { $elemMatch: { k: "color", v: "red" } } }).toArray();
```

**SQL**

```sql
CREATE TABLE products (id BIGINT PRIMARY KEY, name TEXT, attrs JSONB);
CREATE INDEX ON products USING GIN (attrs);
SELECT * FROM products WHERE attrs @> '{"color": "red"}';
```

**BigQuery**

```sql
SELECT * FROM shop.products WHERE EXISTS (SELECT 1 FROM UNNEST(attrs) a WHERE a.k = 'color' AND a.v = 'red');
```

**Snowflake**

```sql
SELECT * FROM products WHERE attrs:color::STRING = 'red';
```

**Firebase**

```js
firestore.collection("products").where("attrs.color", "==", "red"); // a map works because every field is indexed
```

**Elasticsearch**

```js
query: { term: { "attrs.color": "red" } } // with attrs mapped as flattened
```

## 217: How do you translate a tree with parent references?

**MongoDB**

```js
{ _id: "laptops", parent: "computers", path: ",electronics,computers," }
await db.collection("categories").find({ path: /,computers,/ }).toArray(); // all descendants
```

**SQL**

```sql
CREATE EXTENSION ltree;
CREATE TABLE categories (id TEXT PRIMARY KEY, path ltree);
SELECT * FROM categories WHERE path <@ 'electronics.computers';
```

**BigQuery, Snowflake**

Use a recursive CTE over `parent` (see the `$graphLookup` answer), or store the `path` string and filter with `STARTS_WITH`.

**DynamoDB**

```js
KeyConditionExpression: "pk = :t AND begins_with(sk, :p)",
ExpressionAttributeValues: { ":t": "CATEGORY", ":p": "electronics#computers#" },
```

**Firebase**

```js
firestore
  .collection("categories")
  .where("ancestors", "array-contains", "computers");
```

**Elasticsearch**

```js
mappings: { properties: { path: { type: "text", analyzer: "path_analyzer" } } } // path_hierarchy tokenizer
```

Storing the materialized path or the ancestor list turns "all descendants" into one indexed query in every database.

## 218: How do you translate the document versioning pattern?

**MongoDB**

```js
await db
  .collection("contractHistory")
  .insertOne({ ...current, contractId: current._id, _id: new ObjectId() });
await db
  .collection("contracts")
  .updateOne({ _id: id }, { $set: changes, $inc: { version: 1 } });
```

**SQL**

```sql
CREATE TABLE contract_history (LIKE contracts, valid_to TIMESTAMPTZ DEFAULT now());
-- a trigger copies the old row into contract_history on each UPDATE
```

**BigQuery**

Keep every version as a row with `valid_from` and `valid_to` (slowly changing dimension type 2), and use time travel for the last 7 days.

**Snowflake**

```sql
SELECT * FROM contracts AT (OFFSET => -3600); -- time travel: the table as of one hour ago
```

**DynamoDB**

```js
{ pk: "CONTRACT#c1", sk: "v0003", ... } // one item per version; "v0000" holds a copy of the latest
```

**Firebase**

Write the old version to a `versions` subcollection in the same transaction as the update.

**Elasticsearch**

Index each version as its own document with `contractId` and `version`, and use `collapse` on `contractId` to show the latest only.

## 219: How do you translate an order with line items end to end?

**MongoDB**

```js
{ _id: "o1", userId: "u1", status: "paid", total: 5998, items: [{ sku: "A", qty: 2, price: 2999 }], createdAt: new Date() }
```

**SQL**

```sql
CREATE TABLE orders (id UUID PRIMARY KEY, user_id UUID REFERENCES users(id), status TEXT, total_cents INT, created_at TIMESTAMPTZ);
CREATE TABLE order_items (order_id UUID REFERENCES orders(id) ON DELETE CASCADE, sku TEXT, qty INT, price_cents INT, PRIMARY KEY (order_id, sku));
```

**BigQuery**

```sql
CREATE TABLE shop.orders (id STRING, user_id STRING, status STRING, total NUMERIC, created_at TIMESTAMP,
  items ARRAY<STRUCT<sku STRING, qty INT64, price NUMERIC>>) PARTITION BY DATE(created_at);
```

**Redis**

```js
await redis.json.set("order:o1", "$", order); // usually only a cache of recent orders
```

**Snowflake**

```sql
CREATE TABLE orders (id VARCHAR, user_id VARCHAR, status VARCHAR, total NUMBER(12,2), created_at TIMESTAMP_TZ, items ARRAY);
```

**DynamoDB**

```js
{ pk: "USER#u1", sk: "ORDER#2026-11-26#o1", status: "paid", total: 5998, items: [...] }
// GSI: gsi1pk = "ORDER#o1" to look up an order by id
```

**Firebase**

```js
await firestore.doc("orders/o1").set({ userId: "u1", status: "paid", total: 5998, items: [...], createdAt: FieldValue.serverTimestamp() });
```

**Elasticsearch**

One document per order with `items` as `nested`, for the admin search page only.

## 220: How do you translate a user with multiple addresses?

**MongoDB**

```js
{ _id: "u1", name: "Ana", addresses: [{ label: "home", city: "Tbilisi" }, { label: "work", city: "Batumi" }] }
```

**SQL**

```sql
CREATE TABLE addresses (id BIGSERIAL PRIMARY KEY, user_id BIGINT REFERENCES users(id), label TEXT, city TEXT);
```

**BigQuery**

```sql
addresses ARRAY<STRUCT<label STRING, city STRING>>
```

**DynamoDB**

```js
{ pk: "USER#u1", sk: "ADDRESS#home", city: "Tbilisi" }
```

**Firebase**

```js
await firestore
  .doc("users/u1")
  .set({ name: "Ana", addresses: [{ label: "home", city: "Tbilisi" }] });
```

**Elasticsearch**

```js
addresses: {
  type: "nested";
} // so "home in Tbilisi" does not match "home" from one and "Tbilisi" from another
```

A short, bounded address list is fine embedded in Firestore and BigQuery. In DynamoDB, separate items let you update one address without rewriting the user.

## 221: How do you translate a blog with posts and comments?

**MongoDB**

```js
await db.collection("comments").createIndex({ postId: 1, createdAt: -1 });
await db
  .collection("comments")
  .find({ postId })
  .sort({ createdAt: -1 })
  .limit(20)
  .toArray();
```

**SQL**

```sql
CREATE TABLE posts (id BIGSERIAL PRIMARY KEY, author_id BIGINT, title TEXT, body TEXT, created_at TIMESTAMPTZ);
CREATE TABLE comments (id BIGSERIAL PRIMARY KEY, post_id BIGINT REFERENCES posts(id) ON DELETE CASCADE, body TEXT, created_at TIMESTAMPTZ);
CREATE INDEX ON comments (post_id, created_at DESC);
```

**Redis**

```js
await redis.zAdd(`post:${pid}:comments`, { score: Date.now(), value: cid }); // ids in time order
```

**DynamoDB**

```js
{ pk: "POST#p1", sk: "META", title: "Hi", commentCount: 2 }
{ pk: "POST#p1", sk: "COMMENT#2026-11-26T10:00:00Z#c1", body: "Nice" }
```

**Firebase**

```js
firestore
  .collection("posts")
  .doc("p1")
  .collection("comments")
  .orderBy("createdAt", "desc")
  .limit(20);
```

**Elasticsearch**

Index posts for search. Comments are usually indexed only if users can search them.

## 222: How do you translate tags and filtering by tags?

**MongoDB**

```js
{ title: "Hi", tags: ["db", "node"] } // multikey index on tags
```

**SQL**

```sql
-- simple: text[] with a GIN index; normalized: tags and post_tags tables
SELECT p.* FROM posts p JOIN post_tags pt ON pt.post_id = p.id JOIN tags t ON t.id = pt.tag_id WHERE t.name = 'db';
```

**Redis**

```js
await redis.sAdd("tag:db", "p1");
await redis.sInter(["tag:db", "tag:node"]); // posts with both tags
```

**DynamoDB**

```js
{ pk: "TAG#db", sk: "POST#p1" } // one item per tag per post, Query by pk
```

**Firebase**

```js
firestore.collection("posts").where("tags", "array-contains", "db");
```

**Elasticsearch**

```js
query: {
  bool: {
    filter: [{ term: { tags: "db" } }, { term: { tags: "node" } }];
  }
}
```

## 223: How do you translate a leaderboard?

**MongoDB**

```js
await db.collection("scores").find().sort({ score: -1 }).limit(10).toArray();
const rank =
  (await db.collection("scores").countDocuments({ score: { $gt: myScore } })) +
  1;
```

**SQL, BigQuery, Snowflake**

```sql
SELECT user_id, score, RANK() OVER (ORDER BY score DESC) AS rank FROM scores ORDER BY score DESC LIMIT 10;
```

**Redis**

```js
await redis.zAdd("lb", { score: 1200, value: "u1" });
await redis.zRangeWithScores("lb", 0, 9, { REV: true });
await redis.zRevRank("lb", "u1"); // 0-based rank, O(log n)
```

**DynamoDB**

A GSI with a fixed partition key (`"LB"`) and `score` as sort key gives the top 10 with `ScanIndexForward: false`. Getting one user's rank needs a count, so many teams keep the leaderboard in Redis.

**Firebase**

```js
firestore.collection("scores").orderBy("score", "desc").limit(10);
const rank =
  (
    await firestore
      .collection("scores")
      .where("score", ">", myScore)
      .count()
      .get()
  ).data().count + 1;
```

Redis sorted sets are the standard answer for live leaderboards. The database stays the source of truth, and Redis holds the ranking.

## 224: How do you translate a rate limiter?

**MongoDB**

```js
await db.collection("rate").updateOne(
  { _id: `${ip}:${minute}` },
  {
    $inc: { n: 1 },
    $setOnInsert: { expiresAt: new Date(Date.now() + 60000) },
  },
  { upsert: true },
);
```

**Redis**

```js
const key = `rate:${ip}:${Math.floor(Date.now() / 60000)}`;
const [n] = await redis.multi().incr(key).expire(key, 60).exec();
if (n > 100) throw new Error("Too many requests");
```

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Rate",
  Key: { id: `${ip}:${minute}` },
  UpdateExpression: "ADD n :one SET expiresAt = if_not_exists(expiresAt, :exp)",
  ConditionExpression: "attribute_not_exists(n) OR n < :max",
  ExpressionAttributeValues: { ":one": 1, ":exp": nowSec + 120, ":max": 100 },
});
```

**SQL**

```sql
INSERT INTO rate (key, n) VALUES ($1, 1) ON CONFLICT (key) DO UPDATE SET n = rate.n + 1 RETURNING n;
```

Redis is the usual tool because it is fast and expires keys exactly. A database works for low traffic, but every request becomes a write.

## 225: How do you translate a job queue stored in a collection?

**MongoDB**

```js
const job = await db
  .collection("jobs")
  .findOneAndUpdate(
    { status: "ready", runAt: { $lte: new Date() } },
    { $set: { status: "running", lockedAt: new Date() } },
    { sort: { runAt: 1 }, returnDocument: "after" },
  );
```

**SQL**

```sql
UPDATE jobs SET status = 'running', locked_at = now()
WHERE id = (SELECT id FROM jobs WHERE status = 'ready' AND run_at <= now() ORDER BY run_at LIMIT 1 FOR UPDATE SKIP LOCKED)
RETURNING *;
```

**Redis**

```js
await redis.xAdd("jobs", "*", { type: "email", to: "a@b.com" });
const res = await redis.xReadGroup(
  "workers",
  "w1",
  { key: "jobs", id: ">" },
  { COUNT: 1, BLOCK: 5000 },
);
```

**DynamoDB**

Use SQS for the queue. If it must be in DynamoDB, claim a job with an `UpdateCommand` that has `ConditionExpression: "#s = :ready"`.

**Firebase**

Use Cloud Tasks, or a transaction that reads one `ready` job and marks it `running`.

`FOR UPDATE SKIP LOCKED` lets many workers pull from the same PostgreSQL table without blocking each other. Libraries like pg-boss and Graphile Worker are built on it, the same way Agenda is built on MongoDB and BullMQ on Redis.

## 226: How do you translate pub/sub notifications?

**MongoDB**

```js
const stream = db
  .collection("notifications")
  .watch([{ $match: { "fullDocument.userId": "u1" } }]);
stream.on("change", (c) => send(c.fullDocument));
```

**SQL**

```sql
LISTEN user_u1;
NOTIFY user_u1, '{"text":"New order"}';
```

**Redis**

```js
const sub = redis.duplicate();
await sub.connect();
await sub.subscribe("user:u1", (msg) => send(JSON.parse(msg)));
await redis.publish("user:u1", JSON.stringify({ text: "New order" }));
```

**DynamoDB**

DynamoDB Streams trigger a Lambda, which pushes to SNS, EventBridge or API Gateway WebSockets.

**Firebase**

```js
firestore
  .collection("notifications")
  .where("userId", "==", "u1")
  .onSnapshot((snap) => {
    snap.docChanges().forEach((c) => c.type === "added" && send(c.doc.data()));
  });
```

Redis pub/sub does not store messages, so a subscriber that is offline misses them. Use Redis Streams if messages must not be lost.

## 227: How do you translate a distributed lock?

**MongoDB**

```js
await db.collection("locks").insertOne({
  _id: "report-job",
  owner: workerId,
  expiresAt: new Date(Date.now() + 30000),
});
// duplicate key error means someone else holds it; a TTL index cleans up stale locks
```

**SQL**

```sql
SELECT pg_try_advisory_lock(hashtext('report-job')); -- true if we got it
SELECT pg_advisory_unlock(hashtext('report-job'));
```

**Redis**

```js
const token = crypto.randomUUID();
const ok = await redis.set("lock:report-job", token, { NX: true, PX: 30000 });
// release only if we still own it
await redis.eval(
  "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",
  {
    keys: ["lock:report-job"],
    arguments: [token],
  },
);
```

**DynamoDB**

```js
new PutCommand({
  TableName: "Locks",
  Item: { id: "report-job", owner: workerId, expiresAt: nowSec + 30 },
  ConditionExpression: "attribute_not_exists(id) OR expiresAt < :now",
  ExpressionAttributeValues: { ":now": nowSec },
});
```

**Firebase**

```js
await firestore.doc("locks/report-job").create({ owner: workerId, expiresAt }); // fails if it exists
```

Every lock needs an expiry, or a crashed worker holds it forever. A lock with an expiry can still be lost while you work, so use a fencing token (an increasing number checked on write) when correctness really matters.

## 228: How do you translate a shopping cart?

**MongoDB**

```js
await db
  .collection("carts")
  .updateOne(
    { _id: userId },
    { $push: { items: { sku, qty } }, $set: { updatedAt: new Date() } },
    { upsert: true },
  );
```

**SQL**

```sql
INSERT INTO cart_items (user_id, sku, qty) VALUES ($1, $2, $3)
ON CONFLICT (user_id, sku) DO UPDATE SET qty = cart_items.qty + EXCLUDED.qty;
```

**Redis**

```js
await redis.hIncrBy(`cart:${userId}`, sku, qty);
await redis.expire(`cart:${userId}`, 60 * 60 * 24 * 30);
await redis.hGetAll(`cart:${userId}`); // { sku1: "2", sku2: "1" }
```

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Carts",
  Key: { pk: `CART#${userId}`, sk: `ITEM#${sku}` },
  UpdateExpression: "ADD qty :q",
  ExpressionAttributeValues: { ":q": qty },
});
```

**Firebase**

```js
await firestore
  .doc(`carts/${userId}`)
  .set({ items: { [sku]: FieldValue.increment(qty) } }, { merge: true });
```

A Redis hash per cart, with the SKU as field and quantity as value, is short and fast. Guest carts can simply expire.

## 229: How do you translate likes and follower counters?

**MongoDB**

```js
await db.collection("likes").insertOne({ _id: `${userId}:${postId}` }); // unique like
await db
  .collection("posts")
  .updateOne({ _id: postId }, { $inc: { likeCount: 1 } });
```

**SQL**

```sql
BEGIN;
INSERT INTO likes (user_id, post_id) VALUES ($1, $2) ON CONFLICT DO NOTHING;
UPDATE posts SET like_count = like_count + 1 WHERE id = $2; -- only if the insert added a row
COMMIT;
```

**Redis**

```js
const added = await redis.sAdd(`post:${postId}:likes`, userId);
const count = await redis.sCard(`post:${postId}:likes`);
```

**DynamoDB**

```js
new TransactWriteCommand({
  TransactItems: [
    {
      Put: {
        TableName: "App",
        Item: { pk: `POST#${postId}`, sk: `LIKE#${userId}` },
        ConditionExpression: "attribute_not_exists(pk)",
      },
    },
    {
      Update: {
        TableName: "App",
        Key: { pk: `POST#${postId}`, sk: "META" },
        UpdateExpression: "ADD likeCount :one",
        ExpressionAttributeValues: { ":one": 1 },
      },
    },
  ],
});
```

**Firebase**

```js
await firestore.runTransaction(async (tx) => {
  const likeRef = firestore.doc(`posts/${postId}/likes/${userId}`);
  if ((await tx.get(likeRef)).exists) return;
  tx.create(likeRef, { at: FieldValue.serverTimestamp() });
  tx.update(firestore.doc(`posts/${postId}`), {
    likeCount: FieldValue.increment(1),
  });
});
```

The like record and the counter must change together, or the count drifts. Very popular posts need a sharded counter in Firestore.

## 230: How do you translate an activity feed?

**MongoDB**

```js
await db
  .collection("feed")
  .find({ followerId: me })
  .sort({ createdAt: -1 })
  .limit(50)
  .toArray();
```

**SQL**

```sql
SELECT a.* FROM activities a JOIN follows f ON f.followee_id = a.actor_id
WHERE f.follower_id = $1 ORDER BY a.created_at DESC LIMIT 50;
```

**Redis**

```js
// fan-out on write: push the activity id into each follower's feed
for (const f of followers)
  await redis.zAdd(`feed:${f}`, { score: Date.now(), value: activityId });
await redis.zRange(`feed:${me}`, 0, 49, { REV: true });
```

**DynamoDB**

```js
{ pk: "FEED#me", sk: "2026-11-26T10:00:00Z#act1", actor: "u5", type: "post" } // written for each follower
```

**Firebase**

```js
firestore.collection(`users/${me}/feed`).orderBy("createdAt", "desc").limit(50);
```

SQL can build the feed at read time with a join. DynamoDB, Firestore and Redis usually copy each activity into every follower's feed at write time, because they cannot join.

## 231: How do you enforce uniqueness on two fields together (compound unique)?

**MongoDB**

```js
await db
  .collection("members")
  .createIndex({ teamId: 1, userId: 1 }, { unique: true });
```

**SQL**

```sql
ALTER TABLE members ADD CONSTRAINT members_team_user_key UNIQUE (team_id, user_id);
```

**Redis**

```js
await redis.set(`member:${teamId}:${userId}`, "1", { NX: true });
```

**DynamoDB**

```js
new PutCommand({
  TableName: "App",
  Item: { pk: `TEAM#${teamId}`, sk: `MEMBER#${userId}` },
  ConditionExpression: "attribute_not_exists(pk)",
});
```

**Firebase**

```js
await firestore
  .doc(`teams/${teamId}/members/${userId}`)
  .create({ role: "member" });
```

**Elasticsearch**

```js
await es.create({
  index: "members",
  id: `${teamId}:${userId}`,
  document: { teamId, userId },
});
```

The trick for every key-value style store is the same: build the key from both fields, then use "create only if missing".

## 232: How do you turn MongoDB queries into a DynamoDB single-table design?

1. **List the access patterns.** For example: get user by id, list a user's orders by date, get order by id, list open orders.
2. **Pick generic keys.** Use `pk` and `sk` string attributes instead of `userId` or `orderId`.
3. **Put related items under one partition.** A user and their orders share `pk = USER#u1`, with `sk = PROFILE` and `sk = ORDER#<date>#<id>`.
4. **Add GSIs for other patterns.** `gsi1pk = ORDER#o1` for lookups by order id, `gsi2pk = STATUS#open` for open orders.

```js
// "user with recent orders" in one request, like $lookup + $sort + $limit
await ddb.send(
  new QueryCommand({
    TableName: "App",
    KeyConditionExpression: "pk = :pk",
    ExpressionAttributeValues: { ":pk": "USER#u1" },
    ScanIndexForward: false,
    Limit: 11,
  }),
);
```

| Access pattern        | Key used                                           |
| --------------------- | -------------------------------------------------- |
| Get user              | `pk = USER#u1, sk = PROFILE`                       |
| User's orders by date | `pk = USER#u1, begins_with(sk, "ORDER#")`          |
| Order by id           | GSI1: `gsi1pk = ORDER#o1`                          |
| Open orders           | GSI2: `gsi2pk = STATUS#open`, `gsi2sk = createdAt` |

This is the biggest mind shift from MongoDB: you design keys for known queries first, and new queries later may need a new GSI or a backfill.

## 233: How do MongoDB secondary indexes become DynamoDB GSIs and LSIs?

| MongoDB index                  | DynamoDB                                                                                 |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| `{ email: 1 }`                 | GSI with partition key `email`                                                           |
| `{ status: 1, createdAt: -1 }` | GSI with partition key `status`, sort key `createdAt`                                    |
| `{ userId: 1, total: 1 }`      | LSI on a table with partition key `userId` and sort key `total` (created with the table) |
| `{ a: 1, b: 1, c: 1 }`         | GSI with partition key `a` and a composite sort key `b#c`                                |

```js
GlobalSecondaryIndexes: [
  {
    IndexName: "status-createdAt",
    KeySchema: [
      { AttributeName: "status", KeyType: "HASH" },
      { AttributeName: "createdAt", KeyType: "RANGE" },
    ],
    Projection: { ProjectionType: "INCLUDE", NonKeyAttributes: ["total", "userId"] },
  },
],
```

GSIs are eventually consistent, can be added at any time, and you can have up to 20 per table. LSIs share the partition key of the table, support strong reads, must be created with the table and limit each partition key to 10 GB.

## 234: How do you translate a MongoDB search page with many optional filters into DynamoDB?

MongoDB handles `find({ status, category, priceRange, brand })` with any combination of filters and a few indexes. DynamoDB cannot do that well, because every `Query` needs an exact partition key.

Options:

- **Pick the most selective required filter as the key** (for example `category`) and apply the rest as a `FilterExpression`. Fine when each category is small.
- **Composite keys for common combinations**, like `gsi1pk = CATEGORY#shoes#BRAND#nike`.
- **Send search to Elasticsearch or OpenSearch** using DynamoDB Streams, and keep DynamoDB for reads by key. This is the usual answer for real search pages.

```js
new QueryCommand({
  TableName: "Products",
  IndexName: "category-price",
  KeyConditionExpression: "category = :c AND price BETWEEN :min AND :max",
  FilterExpression: "brand = :b AND inStock = :t",
  ExpressionAttributeValues: {
    ":c": "shoes",
    ":min": 50,
    ":max": 150,
    ":b": "nike",
    ":t": true,
  },
});
```

## 235: When do embedded arrays become Firestore subcollections?

**MongoDB**

```js
{ _id: "p1", title: "Hi", comments: [{ by: "u2", text: "Nice" }] }
```

**Firebase**

```js
await firestore.doc("posts/p1").set({ title: "Hi", commentCount: 1 });
await firestore
  .collection("posts/p1/comments")
  .add({ by: "u2", text: "Nice", createdAt: FieldValue.serverTimestamp() });
```

Use a subcollection when the list can grow large, when items are paged, or when clients need to listen to new items. Reading a document never loads its subcollections, so the post stays small and cheap to read. Keep small fixed lists (like 3 shipping options) as an array on the document.

## 236: How do you query across all subcollections with the same name (collection group query)?

**MongoDB**

```js
await db.collection("comments").find({ by: "u2" }).toArray(); // all comments live in one collection
```

**Firebase**

```js
const snap = await firestore
  .collectionGroup("comments")
  .where("by", "==", "u2")
  .get();
snap.docs.forEach((d) => console.log(d.ref.parent.parent.id, d.data())); // parent post id
```

**DynamoDB**

```js
// GSI with gsi1pk = "USER#u2" on every comment item
new QueryCommand({
  TableName: "App",
  IndexName: "gsi1",
  KeyConditionExpression: "gsi1pk = :u",
  ExpressionAttributeValues: { ":u": "USER#u2" },
});
```

A collection group query needs a collection group index scope for filtered fields, which you add in `firestore.indexes.json` under `fieldOverrides` or as a composite index with `"queryScope": "COLLECTION_GROUP"`.

## 237: How do you translate $in on arrays (array-contains-any)?

**MongoDB**

```js
await db
  .collection("posts")
  .find({ tags: { $in: ["db", "node"] } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM posts WHERE tags && ARRAY['db', 'node']; -- overlap
```

**BigQuery**

```sql
SELECT * FROM shop.posts WHERE EXISTS (SELECT 1 FROM UNNEST(tags) t WHERE t IN ('db', 'node'));
```

**Redis**

```js
await redis.ft.search("idx:posts", "@tags:{db | node}");
```

**Snowflake**

```sql
SELECT * FROM posts WHERE ARRAYS_OVERLAP(tags, ARRAY_CONSTRUCT('db', 'node'));
```

**DynamoDB**

```js
FilterExpression: "contains(tags, :a) OR contains(tags, :b)",
```

**Firebase**

```js
firestore
  .collection("posts")
  .where("tags", "array-contains-any", ["db", "node"]); // up to 30 values
```

**Elasticsearch**

```js
query: {
  terms: {
    tags: ["db", "node"];
  }
}
```

## 238: How do you translate range filters on two different fields in Firestore?

**MongoDB**

```js
await db
  .collection("products")
  .find({ price: { $gte: 10, $lte: 50 }, rating: { $gte: 4 } })
  .toArray();
```

**Firebase**

```js
firestore
  .collection("products")
  .where("price", ">=", 10)
  .where("price", "<=", 50)
  .where("rating", ">=", 4)
  .orderBy("price")
  .orderBy("rating");
```

Firestore now allows range and inequality filters on more than one field, but it needs a composite index that covers them, and it can be slower and more costly because it reads more index entries. Order the index fields so the most selective range comes first. Older Firestore versions allowed inequality on only one field, so you may still see code that filters the second field in JavaScript.

## 239: How do you push live database changes to a browser?

**MongoDB**

A Node.js server reads a change stream and forwards events over WebSockets or Server-Sent Events.

**SQL**

Supabase Realtime, Hasura subscriptions or ElectricSQL read PostgreSQL logical replication and push changes to clients.

**Redis**

The server subscribes to a pub/sub channel or reads a stream and pushes events to WebSocket clients.

**DynamoDB**

Streams trigger a Lambda that sends messages through API Gateway WebSockets or AWS AppSync subscriptions.

**Firebase**

```js
import { onSnapshot, doc } from "firebase/firestore";
onSnapshot(doc(db, "orders", "o1"), (snap) => render(snap.data())); // runs in the browser
```

Firestore is the only one here where the browser listens to the database directly. With every other database you need a server in between and you control who sees which change.

## 240: How do you translate access control into Firestore security rules?

**MongoDB**

```js
// in an Express route
if (order.userId !== req.user.id) return res.status(403).end();
```

**Firebase**

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /orders/{orderId} {
      allow read: if request.auth != null && resource.data.userId == request.auth.uid;
      allow create: if request.auth != null && request.resource.data.userId == request.auth.uid;
      allow update, delete: if false;
    }
  }
}
```

**SQL**

```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY own_orders ON orders USING (user_id = current_setting('app.user_id')::uuid);
```

**DynamoDB**

IAM policies with the `dynamodb:LeadingKeys` condition limit a Cognito user to items whose partition key equals their user id.

With MongoDB, access checks live in your API code. With Firestore, clients often read the database directly, so the rules are the security layer. Rules are not filters: a query must include `where("userId", "==", uid)` or it is rejected.

## 241: How do you model documents in BigQuery with nested and repeated fields?

**MongoDB**

```js
{ _id: "o1", user: { id: "u1", country: "GE" }, items: [{ sku: "A", qty: 2 }] }
```

**BigQuery**

```sql
CREATE TABLE shop.orders (
  id STRING,
  user STRUCT<id STRING, country STRING>,
  items ARRAY<STRUCT<sku STRING, qty INT64>>
);

SELECT o.id, o.user.country, i.sku, i.qty
FROM shop.orders o, UNNEST(o.items) i
WHERE o.user.country = 'GE';
```

`STRUCT` is an embedded document and `ARRAY<STRUCT>` is an array of embedded documents, so MongoDB documents map to BigQuery tables almost one to one. Google recommends this nested shape over joins for big analytic tables.

## 242: How do you query raw JSON documents in BigQuery with the JSON type?

**MongoDB**

```js
await db.collection("events").find({ "payload.device.os": "ios" }).toArray();
```

**BigQuery**

```sql
CREATE TABLE shop.events (id STRING, payload JSON);

SELECT id, STRING(payload.device.os) AS os, INT64(payload.duration) AS duration
FROM shop.events
WHERE STRING(payload.device.os) = 'ios';
```

Use the `JSON` type when the shape changes often or you load raw MongoDB documents. Move the fields you filter on all the time into real typed columns: they are cheaper to scan and easier to cluster on.

## 243: How do you store documents in PostgreSQL with JSONB?

**MongoDB**

```js
await db
  .collection("products")
  .find({ "specs.ram": 16, tags: "laptop" })
  .toArray();
```

**SQL**

```sql
CREATE TABLE products (id BIGINT PRIMARY KEY, name TEXT NOT NULL, specs JSONB, tags TEXT[]);

SELECT * FROM products WHERE specs @> '{"ram": 16}' AND 'laptop' = ANY(tags);
SELECT specs->>'cpu' AS cpu, (specs->>'ram')::int AS ram FROM products;
UPDATE products SET specs = jsonb_set(specs, '{ram}', '32') WHERE id = 1;
```

A common middle ground is real columns for fields every row has (id, name, price, foreign keys) and a `JSONB` column for the flexible part. That keeps constraints and joins where they matter and MongoDB-like freedom for the rest.

## 244: How do you index JSONB fields in PostgreSQL?

```sql
-- any key/value containment query (@>)
CREATE INDEX products_specs_gin ON products USING GIN (specs jsonb_path_ops);

-- one field used in = or range queries and sorting
CREATE INDEX products_ram_idx ON products (((specs->>'ram')::int));

-- or a generated column with a normal index
ALTER TABLE products ADD COLUMN ram INT GENERATED ALWAYS AS ((specs->>'ram')::int) STORED;
CREATE INDEX ON products (ram);
```

A GIN index is like a MongoDB wildcard index: it covers every key but only for containment and existence queries. An expression index is like a normal single-field MongoDB index and supports ranges and sorting.

## 245: How do you query documents in Snowflake with VARIANT and FLATTEN?

**MongoDB**

```js
await db
  .collection("orders")
  .aggregate([{ $unwind: "$items" }, { $match: { "items.sku": "A" } }])
  .toArray();
```

**Snowflake**

```sql
CREATE TABLE raw_orders (doc VARIANT);

SELECT doc:_id::STRING AS id,
       i.value:sku::STRING AS sku,
       i.value:qty::INT AS qty
FROM raw_orders,
     LATERAL FLATTEN(input => doc:items) i
WHERE i.value:sku::STRING = 'A';
```

`:` walks into the document, `[0]` reads array elements, `::` casts the value, and `FLATTEN` is the `$unwind`. Snowflake stores common paths of `VARIANT` columns in a columnar way, so these queries are usually fast.

## 246: How do you load MongoDB data into BigQuery?

1. Export with `mongoexport` as newline-delimited JSON (or use a managed pipeline like Dataflow's MongoDB to BigQuery template, Datastream, Airbyte or Fivetran).
2. Upload to Cloud Storage.
3. Load it.

```bash
mongoexport --uri "$MONGODB_URI" -c orders --jsonFormat=relaxed --out orders.json
gcloud storage cp orders.json gs://my-bucket/
bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect shop.orders gs://my-bucket/orders.json
```

Things that break: field names with characters BigQuery does not allow, `_id` as `{"$oid": "..."}` objects, dates as `{"$date": ...}`, and fields with mixed types across documents. Clean them in a script first, or load each document into a single `JSON` column and parse later with SQL.

## 247: How do you load MongoDB data into Snowflake?

```sql
CREATE STAGE mongo_stage URL = 's3://my-bucket/mongo/' STORAGE_INTEGRATION = s3_int;
CREATE TABLE raw_orders (doc VARIANT);

COPY INTO raw_orders FROM @mongo_stage/orders/ FILE_FORMAT = (TYPE = JSON);

CREATE TABLE orders AS
SELECT doc:_id."$oid"::STRING AS id,
       doc:userId::STRING AS user_id,
       doc:total::NUMBER(12,2) AS total,
       doc:createdAt."$date"::TIMESTAMP_TZ AS created_at,
       doc:items AS items
FROM raw_orders;
```

The usual pattern is to land raw documents in a `VARIANT` column first ("ELT"), then build typed tables with SQL. For continuous loads, use Snowpipe on the stage or a CDC tool.

## 248: How do you turn a MongoDB schema into an Elasticsearch mapping?

**MongoDB document**

```js
{ _id: "p1", name: "Wireless Mouse", brand: "Logi", price: 29.99, tags: ["usb", "office"], createdAt: new Date("2026-11-01"), specs: { dpi: 1600 } }
```

**Elasticsearch**

```js
await es.indices.create({
  index: "products",
  mappings: {
    dynamic: "strict",
    properties: {
      name: { type: "text", fields: { keyword: { type: "keyword" } } },
      brand: { type: "keyword" },
      price: { type: "scaled_float", scaling_factor: 100 },
      tags: { type: "keyword" },
      createdAt: { type: "date" },
      specs: { type: "flattened" },
    },
  },
});
```

Rules of thumb: free text you search becomes `text`, ids and values you filter or group by become `keyword`, and dynamic maps become `flattened`. MongoDB's `_id` becomes the Elasticsearch document `_id`, so updates replace the right document.

## 249: When should you use nested instead of object fields in Elasticsearch?

**MongoDB**

```js
{
  items: [
    { sku: "A", color: "red" },
    { sku: "B", color: "blue" },
  ];
}
await db
  .collection("orders")
  .find({ items: { $elemMatch: { sku: "A", color: "blue" } } }); // no match
```

**Elasticsearch with object (default)**

Arrays of objects are flattened into `items.sku: [A, B]` and `items.color: [red, blue]`, so a query for `sku A` and `color blue` matches by mistake.

**Elasticsearch with nested**

```js
mappings: { properties: { items: { type: "nested" } } }
query: { nested: { path: "items", query: { bool: { filter: [{ term: { "items.sku": "A" } }, { term: { "items.color": "blue" } }] } } } }
```

Use `nested` whenever you need `$elemMatch` behavior. Each nested object is stored as a hidden document, so large arrays make indexing and queries slower.

## 250: How do you bulk index documents into Elasticsearch?

**MongoDB**

```js
await db.collection("products").insertMany(docs, { ordered: false });
```

**Elasticsearch**

```js
const result = await es.helpers.bulk({
  datasource: db
    .collection("products")
    .find()
    .map(({ _id, ...doc }) => ({ ...doc, mongoId: _id.toString() })),
  onDocument: (doc) => ({ index: { _index: "products", _id: doc.mongoId } }),
  flushBytes: 5_000_000,
  concurrency: 4,
  onDrop: (d) => console.error("failed", d.error),
});
console.log(result.successful, result.failed);
```

For a large first load, set `refresh_interval: "-1"` and `number_of_replicas: 0` on the new index, then restore them when done. `_id` is a metadata field, so it must go in the action line and not inside the document body.

## 251: Why does a new document not show up in Elasticsearch search right away?

In MongoDB, a document is visible to queries as soon as the write returns. In Elasticsearch, new writes go to a buffer and become searchable only after a **refresh**, which happens every second by default (and only on indices that were searched recently).

```js
await es.index({ index: "orders", id: "o1", document, refresh: "wait_for" }); // returns after it is searchable
await es.get({ index: "orders", id: "o1" }); // get by id is real-time, no refresh needed
```

Use `refresh: "wait_for"` in tests or when the user must see their own write in a list. Don't use `refresh: true` on every write in production; it creates many tiny segments and slows the cluster. The other databases here (except DynamoDB GSIs and Redis replicas) show writes right away.

## 252: How do you translate a full aggregation pipeline into Elasticsearch aggregations?

**MongoDB**

```js
[
  { $match: { status: "paid", createdAt: { $gte: new Date("2026-01-01") } } },
  {
    $group: {
      _id: "$country",
      revenue: { $sum: "$total" },
      orders: { $sum: 1 },
      avg: { $avg: "$total" },
    },
  },
  { $match: { revenue: { $gt: 1000 } } },
  { $sort: { revenue: -1 } },
  { $limit: 10 },
];
```

**Elasticsearch**

```js
await es.search({
  index: "orders",
  size: 0,
  query: {
    bool: {
      filter: [
        { term: { status: "paid" } },
        { range: { createdAt: { gte: "2026-01-01" } } },
      ],
    },
  },
  aggs: {
    byCountry: {
      terms: { field: "country", size: 10, order: { revenue: "desc" } },
      aggs: {
        revenue: { sum: { field: "total" } },
        avg: { avg: { field: "total" } },
        onlyBig: {
          bucket_selector: {
            buckets_path: { r: "revenue" },
            script: "params.r > 1000",
          },
        },
      },
    },
  },
});
```

`$match` before `$group` becomes `query`, `$group` becomes a `terms` bucket with metric sub-aggregations, the `$match` after `$group` becomes `bucket_selector`, and `$sort` + `$limit` become `order` and `size` on `terms`. The order count is the bucket's `doc_count`.

## 253: How do you write the same pipeline with ES|QL?

**MongoDB**

```js
[
  { $match: { status: "paid" } },
  { $group: { _id: "$country", revenue: { $sum: "$total" } } },
  { $sort: { revenue: -1 } },
  { $limit: 10 },
];
```

**Elasticsearch (ES|QL)**

```js
const res = await es.esql.query({
  query: `
    FROM orders
    | WHERE status == "paid"
    | STATS revenue = SUM(total) BY country
    | SORT revenue DESC
    | LIMIT 10`,
});
```

ES|QL is a piped query language, so it reads almost like a MongoDB aggregation pipeline written as text. It is often the easiest way to translate analytics pipelines, while the JSON Query DSL is still the main tool for relevance-ranked search.

## 254: How do you store and query MongoDB-like documents in Redis with JSON?

**MongoDB**

```js
await db
  .collection("users")
  .insertOne({ _id: "u1", name: "Ana", age: 30, address: { city: "Tbilisi" } });
await db
  .collection("users")
  .find({ "address.city": "Tbilisi", age: { $gte: 18 } })
  .toArray();
```

**Redis**

```js
await redis.json.set("user:u1", "$", {
  name: "Ana",
  age: 30,
  address: { city: "Tbilisi" },
});

await redis.ft.create(
  "idx:users",
  {
    "$.name": { type: "TEXT", AS: "name" },
    "$.age": { type: "NUMERIC", AS: "age", SORTABLE: true },
    "$.address.city": { type: "TAG", AS: "city" },
  },
  { ON: "JSON", PREFIX: "user:" },
);

const { documents } = await redis.ft.search(
  "idx:users",
  "@city:{Tbilisi} @age:[18 +inf]",
);
await redis.json.numIncrBy("user:u1", "$.age", 1);
```

With Redis 8, JSON and the Query Engine are built in, so Redis can act as a small document database. Keep in mind that all data must fit in memory, and persistence is weaker than MongoDB's unless you tune AOF.

## 255: How do MongoDB index types map to Redis Query Engine field types?

| MongoDB use                       | Redis field type | Query example             |
| --------------------------------- | ---------------- | ------------------------- |
| Exact match on a string, `$in`    | `TAG`            | `@status:{paid \| new}`   |
| `$text` search                    | `TEXT`           | `@name:wireless`          |
| Numbers, dates (as epoch), ranges | `NUMERIC`        | `@price:[10 50]`          |
| `2dsphere` points                 | `GEO`            | `@loc:[44.79 41.71 5 km]` |
| Polygons                          | `GEOSHAPE`       | `@area:[WITHIN $shape]`   |
| Atlas Vector Search               | `VECTOR`         | `*=>[KNN 10 @emb $vec]`   |

Add `SORTABLE` to fields you sort by. Dates need to be stored as numbers (epoch seconds or ms) to support range queries, because Redis has no date type.

## 256: When do you use a Redis hash and when Redis JSON?

**Hash**

```js
await redis.hSet("user:u1", { name: "Ana", age: "30", city: "Tbilisi" });
await redis.hIncrBy("user:u1", "age", 1);
```

**JSON**

```js
await redis.json.set("user:u1", "$", {
  name: "Ana",
  age: 30,
  address: { city: "Tbilisi" },
  tags: ["vip"],
});
```

- Use a **hash** for flat objects with string or number fields: sessions, counters, small profiles. It uses less memory and every command is simple.
- Use **JSON** when the MongoDB document has nested objects or arrays and you want to read or update parts by path.

Both can be indexed by the Redis Query Engine (`ON: "HASH"` or `ON: "JSON"`).

## 257: How do you use sorted sets as a secondary index for range queries?

**MongoDB**

```js
await db.collection("products").createIndex({ price: 1 });
await db
  .collection("products")
  .find({ price: { $gte: 10, $lte: 50 } })
  .toArray();
```

**Redis**

```js
await redis.zAdd("products:byPrice", { score: 29.99, value: "p1" });
const ids = await redis.zRangeByScore("products:byPrice", 10, 50);
const products = await Promise.all(
  ids.map((id) => redis.json.get(`product:${id}`)),
);
```

Before the Query Engine existed, this was the standard way to build indexes in Redis: one sorted set per indexed field, kept in sync by your code in the same `MULTI` as the main write. It is still useful for simple cases and for leaderboards and time-ordered lists.

## 258: How do you expire one field instead of the whole key?

**MongoDB**

```js
// TTL works per document only; to expire part of a doc, unset it in a job
await db
  .collection("users")
  .updateMany(
    { "otp.expiresAt": { $lt: new Date() } },
    { $unset: { otp: "" } },
  );
```

**Redis**

```js
await redis.hSet("user:u1", "otp", "123456");
await redis.hExpire("user:u1", "otp", 300); // HEXPIRE, Redis 7.4+
```

**DynamoDB**

TTL is per item. Put the expiring value in its own item (`sk = "OTP"`) with its own `expiresAt`.

**Firebase**

TTL is per document. Use a separate document in an `otps` collection.

Redis is the only one here that can expire a single hash field.

## 259: How do you translate a multi-step atomic update into a Redis Lua script or function?

**MongoDB**

```js
// decrement stock only if enough is left
await db
  .collection("products")
  .updateOne({ _id: "p1", stock: { $gte: 2 } }, { $inc: { stock: -2 } });
```

**Redis**

```js
const script = `
  local stock = tonumber(redis.call('HGET', KEYS[1], 'stock'))
  if stock and stock >= tonumber(ARGV[1]) then
    return redis.call('HINCRBY', KEYS[1], 'stock', -tonumber(ARGV[1]))
  end
  return -1`;
const left = await redis.eval(script, {
  keys: ["product:p1"],
  arguments: ["2"],
});
```

A Lua script runs on the server with no other command in between, so check-and-update is atomic. For scripts you call often, load them once as Redis Functions (`FUNCTION LOAD`) and call them with `FCALL`. In Redis Cluster, all keys one script touches must be in the same hash slot.

## 260: How do you name Redis keys when translating collections?

Use `<collection>:<id>` and, for related data, `<collection>:<id>:<part>`:

```text
user:u1                 -> JSON or hash with the user
user:u1:sessions        -> set of session ids
user:u1:cart            -> hash of sku -> qty
order:o1                -> JSON order
orders:byUser:u1        -> sorted set of order ids by time
email:ana@example.com   -> string with the user id (unique lookup)
```

- Keep a common prefix per "collection" so a search index can use `PREFIX user:`.
- In Redis Cluster, wrap the shared part in braces (`user:{u1}:cart`) so keys used together land in the same slot.
- Never use `KEYS user:*` in production. It blocks the server. Use `SCAN` or a search index.

## 261: How do you translate an event log or change log into Redis Streams?

**MongoDB**

```js
await db
  .collection("events")
  .insertOne({ type: "order.created", orderId: "o1", at: new Date() });
```

**Redis**

```js
await redis.xAdd(
  "events",
  "*",
  { type: "order.created", orderId: "o1" },
  { TRIM: { strategy: "MAXLEN", strategyModifier: "~", threshold: 100000 } },
);

await redis.xGroupCreate("events", "billing", "0", { MKSTREAM: true });
const res = await redis.xReadGroup(
  "billing",
  "worker-1",
  { key: "events", id: ">" },
  { COUNT: 10, BLOCK: 5000 },
);
for (const { id, message } of res?.[0]?.messages ?? []) {
  await handle(message);
  await redis.xAck("events", "billing", id);
}
```

Streams give each consumer group its own position and a pending list of unacknowledged messages, much like Kafka. Keep the stream trimmed, because it lives in memory.

## 262: How do you translate conditional updates into DynamoDB ConditionExpression?

**MongoDB**

```js
const res = await db
  .collection("orders")
  .updateOne({ _id: "o1", status: "pending" }, { $set: { status: "paid" } });
if (res.matchedCount === 0) throw new Error("Order is not pending");
```

**DynamoDB**

```js
try {
  await ddb.send(
    new UpdateCommand({
      TableName: "Orders",
      Key: { id: "o1" },
      UpdateExpression: "SET #s = :paid",
      ConditionExpression: "#s = :pending",
      ExpressionAttributeNames: { "#s": "status" },
      ExpressionAttributeValues: { ":paid": "paid", ":pending": "pending" },
      ReturnValuesOnConditionCheckFailure: "ALL_OLD",
    }),
  );
} catch (err) {
  if (err.name === "ConditionalCheckFailedException")
    throw new Error(`Order is ${err.Item?.status}`);
  throw err;
}
```

In MongoDB, extra conditions go in the filter. In DynamoDB the key goes in `Key` and every other condition goes in `ConditionExpression`. `ReturnValuesOnConditionCheckFailure` saves you a second read to find out why it failed.

## 263: How do MongoDB update operators map to DynamoDB UpdateExpression?

| MongoDB                  | DynamoDB `UpdateExpression`                     |
| ------------------------ | ----------------------------------------------- |
| `$set: { a: 1 }`         | `SET a = :v`                                    |
| `$unset: { a: "" }`      | `REMOVE a`                                      |
| `$inc: { n: 1 }`         | `ADD n :one` or `SET n = n + :one`              |
| `$push: { list: x }`     | `SET list = list_append(list, :xs)`             |
| `$addToSet: { set: x }`  | `ADD tagsSet :s` (string or number set)         |
| `$pull: { set: x }`      | `DELETE tagsSet :s` (sets only)                 |
| `$setOnInsert: { a: 1 }` | `SET a = if_not_exists(a, :v)`                  |
| `$set: { "a.b": 1 }`     | `SET a.b = :v` (the map `a` must already exist) |
| `$set: { "list.0": x }`  | `SET list[0] = :v`                              |
| `$rename`                | `SET newName = oldName REMOVE oldName`          |

```js
UpdateExpression: "SET #n = :name, updatedAt = :now ADD loginCount :one REMOVE tempToken",
```

All four clauses (`SET`, `REMOVE`, `ADD`, `DELETE`) can appear in one expression, each at most once.

## 264: What is the difference between Query and Scan in DynamoDB compared to find() in MongoDB?

- **Query** reads items from one partition key value, optionally narrowed by a sort key condition. It is fast and costs only what it reads. This is like `find()` that fully uses an index.
- **Scan** reads every item in the table (or index), then applies the filter. It is like `find()` with a `COLLSCAN` in MongoDB, except you pay for every item read.

```js
// good: Query
new QueryCommand({
  TableName: "Orders",
  KeyConditionExpression: "userId = :u",
  ExpressionAttributeValues: { ":u": "u1" },
});

// costly: Scan with a filter
new ScanCommand({
  TableName: "Orders",
  FilterExpression: "userId = :u",
  ExpressionAttributeValues: { ":u": "u1" },
});
```

Every MongoDB query you translate should become a `Query` on the table or a GSI. A `Scan` is fine for admin jobs, exports and small tables only.

## 265: How do you process a whole DynamoDB table in parallel?

**MongoDB**

```js
for await (const doc of db.collection("users").find().batchSize(1000))
  await migrate(doc);
```

**DynamoDB**

```js
const TOTAL = 8;
await Promise.all(
  Array.from({ length: TOTAL }, async (_, segment) => {
    for await (const page of paginateScan(
      { client: ddb },
      { TableName: "Users", Segment: segment, TotalSegments: TOTAL },
    )) {
      for (const item of page.Items) await migrate(item);
    }
  }),
);
```

**Elasticsearch**

```js
await es.reindex({
  source: { index: "users", slice: { id: 0, max: 4 } },
  dest: { index: "users_v2" },
}); // or slices: "auto"
```

A parallel scan splits the table into segments that separate workers read at the same time. It is much faster than one scan, but it can eat all the table's read capacity, so limit it on busy tables.

## 266: How do you translate a $in on ids into a batch read?

**MongoDB**

```js
await db
  .collection("users")
  .find({ _id: { $in: ["u1", "u2", "u3"] } })
  .toArray();
```

**SQL**

```sql
SELECT * FROM users WHERE id = ANY($1); -- pass an array
```

**Redis**

```js
await redis.json.mGet(["user:u1", "user:u2", "user:u3"], "$");
```

**DynamoDB**

```js
import { BatchGetCommand } from "@aws-sdk/lib-dynamodb";
const { Responses, UnprocessedKeys } = await ddb.send(
  new BatchGetCommand({
    RequestItems: {
      Users: { Keys: [{ id: "u1" }, { id: "u2" }, { id: "u3" }] },
    },
  }),
); // up to 100 keys; retry UnprocessedKeys
```

**Firebase**

```js
const snaps = await firestore.getAll(
  firestore.doc("users/u1"),
  firestore.doc("users/u2"),
  firestore.doc("users/u3"),
);
```

**Elasticsearch**

```js
await es.mget({ index: "users", ids: ["u1", "u2", "u3"] });
```

`BatchGetItem` does not return items in the order you asked for, and it skips missing keys silently. Map results by id in code.

## 267: How do you read several items consistently at the same moment?

**MongoDB**

```js
await session.withTransaction(
  async () => {
    const a = await db
      .collection("accounts")
      .findOne({ _id: "a" }, { session });
    const b = await db
      .collection("accounts")
      .findOne({ _id: "b" }, { session });
  },
  { readConcern: { level: "snapshot" } },
);
```

**SQL**

```sql
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT * FROM accounts WHERE id IN ('a', 'b');
COMMIT;
```

**Redis**

```js
await redis.multi().hGetAll("account:a").hGetAll("account:b").exec();
```

**DynamoDB**

```js
import { TransactGetCommand } from "@aws-sdk/lib-dynamodb";
await ddb.send(
  new TransactGetCommand({
    TransactItems: [
      { Get: { TableName: "Accounts", Key: { id: "a" } } },
      { Get: { TableName: "Accounts", Key: { id: "b" } } },
    ],
  }),
);
```

**Firebase**

```js
await firestore.runTransaction(async (tx) =>
  tx.getAll(firestore.doc("accounts/a"), firestore.doc("accounts/b")),
);
```

## 268: Why do DynamoDB expressions need ExpressionAttributeNames?

DynamoDB has a long list of reserved words (`name`, `status`, `date`, `count`, `data`, `size`, `user` and hundreds more). MongoDB lets you use any field name freely, so translated code often hits this error:

```text
ValidationException: Invalid UpdateExpression: Attribute name is a reserved keyword; reserved keyword: status
```

The fix is a placeholder:

```js
UpdateExpression: "SET #s = :s, #n = :n",
ExpressionAttributeNames: { "#s": "status", "#n": "name" },
ExpressionAttributeValues: { ":s": "active", ":n": "Ana" },
```

Names that contain dots or dashes also need placeholders, because `a.b` in an expression means "field b inside map a". Many teams just use `#` placeholders for every attribute name to avoid surprises, and libraries like ElectroDB do it for you.

## 269: How do you write SQL-like queries for DynamoDB with PartiQL?

**MongoDB**

```js
await db.collection("orders").find({ userId: "u1", status: "paid" }).toArray();
```

**DynamoDB**

```js
import { ExecuteStatementCommand } from "@aws-sdk/lib-dynamodb";
const { Items } = await ddb.send(
  new ExecuteStatementCommand({
    Statement: 'SELECT * FROM "Orders" WHERE "userId" = ? AND "status" = ?',
    Parameters: ["u1", "paid"],
  }),
);
```

PartiQL looks like SQL but has the same rules as the normal API: if the `WHERE` does not include the partition key with `=` or `IN`, it becomes a full table scan. There are no joins, no `GROUP BY` and no `ORDER BY` outside the sort key.

## 270: When do you use a Firestore transaction and when a batched write?

**MongoDB**

You use `session.withTransaction()` when a write depends on something you read, and `bulkWrite()` when you only need to write.

**Firebase**

```js
// transaction: reads first, then writes; retried on conflict
await firestore.runTransaction(async (tx) => {
  const snap = await tx.get(firestore.doc("products/p1"));
  if (snap.get("stock") < 1) throw new Error("Sold out");
  tx.update(snap.ref, { stock: FieldValue.increment(-1) });
  tx.create(firestore.collection("orders").doc(), { productId: "p1" });
});

// batch: writes only, all or nothing, up to 500 operations
const batch = firestore.batch();
batch.update(firestore.doc("users/u1"), { plan: "pro" });
batch.set(firestore.doc("audit/a1"), { action: "upgrade" });
await batch.commit();
```

Use a transaction when a write depends on a value you read. Use a batch when you already know what to write. In a Firestore transaction, all reads must come before any writes, which is stricter than MongoDB.

## 271: How do you replace Mongoose models with Firestore converters?

**MongoDB (Mongoose)**

```js
const User = mongoose.model(
  "User",
  new mongoose.Schema({ name: String, createdAt: Date }),
);
const user = await User.findById(id);
```

**Firebase**

```js
const userConverter = {
  toFirestore: (u) => ({ name: u.name, createdAt: u.createdAt }),
  fromFirestore: (snap) => {
    const d = snap.data();
    return { id: snap.id, name: d.name, createdAt: d.createdAt.toDate() };
  },
};
const users = firestore.collection("users").withConverter(userConverter);
const user = (await users.doc(id).get()).data();
```

A converter maps between plain objects and stored documents, so Firestore `Timestamp` values become `Date` and the id is attached. Add validation (for example Zod) inside `toFirestore` to get what Mongoose schemas gave you.

## 272: How do you keep denormalized copies in sync?

**MongoDB**

```js
for await (const c of db
  .collection("users")
  .watch([{ $match: { operationType: "update" } }], {
    fullDocument: "updateLookup",
  })) {
  await db
    .collection("orders")
    .updateMany(
      { "user.id": c.documentKey._id },
      { $set: { "user.name": c.fullDocument.name } },
    );
}
```

**SQL**

Usually not needed, because you join. If you do copy data, use a trigger.

**DynamoDB**

A Lambda on the table's stream updates every item that holds a copy.

**Firebase**

```js
import { onDocumentUpdated } from "firebase-functions/v2/firestore";
export const syncUserName = onDocumentUpdated("users/{uid}", async (event) => {
  const name = event.data.after.get("name");
  if (name === event.data.before.get("name")) return;
  const orders = await getFirestore()
    .collection("orders")
    .where("user.id", "==", event.params.uid)
    .get();
  const writer = getFirestore().bulkWriter();
  orders.forEach((d) => writer.update(d.ref, { "user.name": name }));
  await writer.close();
});
```

**Elasticsearch**

`_update_by_query` on documents with the old value, or reindex the affected documents from the source of truth.

The copies are eventually consistent everywhere. Only copy values that change rarely, like names, not values that change all the time, like balances.

## 273: How do you translate scheduled jobs (Atlas scheduled triggers)?

| MongoDB                            | SQL                 | BigQuery          | Redis                        | Snowflake | DynamoDB                       | Firebase                     | Elasticsearch            |
| ---------------------------------- | ------------------- | ----------------- | ---------------------------- | --------- | ------------------------------ | ---------------------------- | ------------------------ |
| Atlas scheduled triggers, app cron | `pg_cron` extension | Scheduled queries | App cron, BullMQ repeat jobs | Tasks     | EventBridge Scheduler + Lambda | `onSchedule` Cloud Functions | Watcher, ILM, transforms |

```sql
-- Snowflake
CREATE TASK nightly_rollup WAREHOUSE = app_wh SCHEDULE = 'USING CRON 0 2 * * * UTC'
AS INSERT INTO daily_sales SELECT DATE(created_at), SUM(total) FROM orders WHERE DATE(created_at) = CURRENT_DATE - 1 GROUP BY 1;
ALTER TASK nightly_rollup RESUME;
```

```js
// Firebase
import { onSchedule } from "firebase-functions/v2/scheduler";
export const nightly = onSchedule("every day 02:00", async () => rollup());
```

Snowflake tasks are created suspended, so the `RESUME` line is easy to forget.

## 274: How do you translate server-side functions and stored procedures?

MongoDB has no stored procedures (server-side JavaScript in `$where` and `$function` is deprecated). Logic usually lives in the app or in Atlas Functions.

**SQL**

```sql
CREATE FUNCTION transfer(a TEXT, b TEXT, amt NUMERIC) RETURNS void AS $$
BEGIN
  UPDATE accounts SET balance = balance - amt WHERE id = a;
  UPDATE accounts SET balance = balance + amt WHERE id = b;
END $$ LANGUAGE plpgsql;
SELECT transfer('a', 'b', 100);
```

**BigQuery**

```sql
CREATE PROCEDURE shop.refresh_totals() BEGIN
  CREATE OR REPLACE TABLE shop.user_totals AS SELECT user_id, SUM(total) total FROM shop.orders GROUP BY user_id;
END;
CALL shop.refresh_totals();
```

**Redis**

Lua scripts and Redis Functions.

**Snowflake**

```sql
CREATE PROCEDURE refresh_totals() RETURNS STRING LANGUAGE SQL AS
$$ BEGIN CREATE OR REPLACE TABLE user_totals AS SELECT user_id, SUM(total) total FROM orders GROUP BY user_id; RETURN 'ok'; END; $$;
```

**DynamoDB, Firebase**

No server-side code in the database. Use Lambda or Cloud Functions.

**Elasticsearch**

Painless scripts (stored with `_scripts`) and ingest pipelines.

## 275: How do you translate MongoDB views?

**MongoDB**

```js
await db.createCollection("paidOrders", {
  viewOn: "orders",
  pipeline: [{ $match: { status: "paid" } }, { $project: { cardNumber: 0 } }],
});
```

**SQL, BigQuery, Snowflake**

```sql
CREATE VIEW paid_orders AS SELECT id, user_id, total, created_at FROM orders WHERE status = 'paid';
```

**Elasticsearch**

```js
await es.indices.putAlias({
  index: "orders",
  name: "paid_orders",
  filter: { term: { status: "paid" } },
});
```

**Firebase, DynamoDB**

No views. A GSI with a projection, or a separate collection kept in sync, does the same job.

A filtered alias in Elasticsearch works like a read-only view. In BigQuery, an authorized view lets people query the view without access to the base table, which is a common way to hide columns.

## 276: How do you translate on-demand materialized views ($merge into a summary collection)?

**MongoDB**

```js
await db
  .collection("orders")
  .aggregate([
    {
      $group: {
        _id: { $dateTrunc: { date: "$createdAt", unit: "day" } },
        revenue: { $sum: "$total" },
      },
    },
    { $merge: { into: "dailyRevenue", whenMatched: "replace" } },
  ])
  .toArray();
```

**SQL**

```sql
CREATE MATERIALIZED VIEW daily_revenue AS
SELECT date_trunc('day', created_at) AS day, SUM(total) AS revenue FROM orders GROUP BY 1;
CREATE UNIQUE INDEX ON daily_revenue (day);
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_revenue;
```

**BigQuery**

```sql
CREATE MATERIALIZED VIEW shop.daily_revenue AS
SELECT DATE(created_at) AS day, SUM(total) AS revenue FROM shop.orders GROUP BY day;
```

**Snowflake**

```sql
CREATE DYNAMIC TABLE daily_revenue TARGET_LAG = '15 minutes' WAREHOUSE = app_wh AS
SELECT DATE(created_at) AS day, SUM(total) AS revenue FROM orders GROUP BY 1;
```

**Elasticsearch**

A continuous transform that groups `orders` by day into a `daily_revenue` index.

BigQuery materialized views refresh themselves in the background, and queries on the base table can even be rewritten to use them. PostgreSQL views stay stale until you run `REFRESH`.

## 277: How do you partition a BigQuery table and why does it matter?

```sql
CREATE TABLE shop.events (
  id STRING, user_id STRING, type STRING, created_at TIMESTAMP
)
PARTITION BY DATE(created_at)
OPTIONS (require_partition_filter = TRUE, partition_expiration_days = 400);

SELECT COUNT(*) FROM shop.events
WHERE created_at >= TIMESTAMP('2026-11-01') AND created_at < TIMESTAMP('2026-11-27');
```

BigQuery bills by bytes scanned. With partitioning, a query that filters on `created_at` reads only the days it needs. `require_partition_filter` rejects queries that forget the filter, which protects you from a surprise bill. In MongoDB there is no billing link like this; the closest idea is a time-based index plus TTL.

## 278: How does BigQuery clustering compare to MongoDB indexes?

```sql
CREATE TABLE shop.orders
PARTITION BY DATE(created_at)
CLUSTER BY user_id, status
AS SELECT * FROM shop.orders_raw;

SELECT * FROM shop.orders WHERE user_id = 'u1' AND status = 'paid' AND created_at >= '2026-11-01';
```

Clustering sorts the data inside each partition by up to four columns, so BigQuery can skip blocks that cannot match. It works like a compound index prefix: filters on `user_id`, or `user_id` and `status`, get the benefit, but a filter on `status` alone gets much less. Unlike a MongoDB index, it does not make single-row lookups instant. It only reduces how much data is scanned.

## 279: How do Snowflake micro-partitions and clustering keys work compared to MongoDB indexes?

Snowflake stores every table as small, immutable micro-partitions (about 50 to 500 MB of raw data each) and keeps min/max values per column for each one. A query skips micro-partitions whose ranges cannot match ("pruning").

```sql
ALTER TABLE orders CLUSTER BY (TO_DATE(created_at), user_id);
SELECT SYSTEM$CLUSTERING_INFORMATION('orders', '(TO_DATE(created_at), user_id)');
```

For most tables, data loaded in time order is already well clustered by date. Add a clustering key only on large tables (multi-terabyte) where queries filter on columns that are not naturally sorted. Automatic clustering costs credits, so it is not free like creating a MongoDB index. For point lookups on high-cardinality columns, the search optimization service is the better tool.

## 280: How do you restore old data (Snowflake time travel vs MongoDB point-in-time restore)?

**MongoDB**

Atlas continuous backup restores a whole cluster to a point in time, usually into a new cluster.

**SQL**

PostgreSQL PITR replays WAL to a timestamp (`recovery_target_time`), again into a new instance.

**BigQuery**

```sql
SELECT * FROM shop.orders FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);
```

**Snowflake**

```sql
SELECT * FROM orders AT (TIMESTAMP => '2026-11-26 09:00:00'::TIMESTAMP_TZ);
CREATE TABLE orders_restored CLONE orders BEFORE (STATEMENT => '01b2c3d4-0000-1234-0000-000100020003');
UNDROP TABLE orders;
```

**DynamoDB**

```bash
aws dynamodb restore-table-to-point-in-time --source-table-name Orders --target-table-name Orders-restored \
  --restore-date-time 2026-11-26T09:00:00Z
```

**Firebase**

PITR keeps up to 7 days of versions you can read with a `readTime`, and you can restore from a backup into a new database.

Snowflake and BigQuery let you query old data with plain SQL without restoring anything, which is very handy after a bad `UPDATE`.

## 281: How do you translate copying a database for testing (zero-copy clone)?

**MongoDB**

`mongodump` and `mongorestore` into a new cluster, or restore an Atlas snapshot. It copies all the data.

**SQL**

```sql
CREATE DATABASE shop_test TEMPLATE shop; -- copies everything; no active connections to shop allowed
```

**BigQuery**

```sql
CREATE TABLE shop_test.orders CLONE shop.orders; -- you pay only for data that changes later
```

**Snowflake**

```sql
CREATE DATABASE shop_dev CLONE shop; -- instant, shares storage until data changes
```

**DynamoDB**

Restore a backup into a new table.

Snowflake and BigQuery clones are instant and almost free, so every developer or CI run can have a full copy of production-sized data. Mask sensitive columns before sharing clones.

## 282: How do you upsert a batch of changed documents into BigQuery or Snowflake?

**MongoDB**

```js
await db.collection("users").bulkWrite(
  changes.map((u) => ({
    replaceOne: { filter: { _id: u._id }, replacement: u, upsert: true },
  })),
);
```

**BigQuery**

```sql
-- 1. load the batch into a staging table, 2. merge
MERGE shop.users t
USING shop.users_staging s
ON t.id = s.id
WHEN MATCHED AND s.updated_at > t.updated_at THEN UPDATE SET name = s.name, email = s.email, updated_at = s.updated_at
WHEN NOT MATCHED THEN INSERT ROW;
```

**Snowflake**

```sql
MERGE INTO users t
USING users_staging s ON t.id = s.id
WHEN MATCHED AND s.updated_at > t.updated_at THEN UPDATE SET name = s.name, email = s.email, updated_at = s.updated_at
WHEN NOT MATCHED THEN INSERT (id, name, email, updated_at) VALUES (s.id, s.name, s.email, s.updated_at);
```

Do one `MERGE` per batch (every few minutes), not one per document. Warehouses are slow and costly for row-by-row updates. If the staging table can hold the same id twice, dedupe it first with `QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) = 1`, or the `MERGE` fails.

## 283: How do you handle deletes when syncing MongoDB into a warehouse?

A plain export only shows documents that exist, so deleted ones stay in the warehouse forever. Options:

- **CDC with delete events.** A change stream (or Debezium, Fivetran, Airbyte) sends `delete` events with the `_id`. Add an `op` column to staging.
- **Soft delete in MongoDB.** Set `deletedAt` instead of deleting, so updates carry the delete.
- **Full snapshot compare.** For small tables, reload everything and replace the table.

```sql
MERGE INTO users t USING users_changes s ON t.id = s.id
WHEN MATCHED AND s.op = 'delete' THEN DELETE
WHEN MATCHED THEN UPDATE SET name = s.name, updated_at = s.updated_at
WHEN NOT MATCHED AND s.op <> 'delete' THEN INSERT (id, name, updated_at) VALUES (s.id, s.name, s.updated_at);
```

The same `MERGE` works in BigQuery and Snowflake. Many teams keep deleted rows with a flag (`is_deleted`) instead, so reports about the past stay correct.

## 284: How do you stream MongoDB changes into BigQuery or Snowflake (CDC)?

| Tool                                        | Target    | Notes                                               |
| ------------------------------------------- | --------- | --------------------------------------------------- |
| Debezium MongoDB connector + Kafka          | Both      | Self-managed, reads change streams                  |
| Dataflow MongoDB to BigQuery (CDC) template | BigQuery  | Reads change streams, writes with Storage Write API |
| Fivetran, Airbyte                           | Both      | Managed connectors, handle schema changes           |
| Snowflake Openflow / Kafka connector        | Snowflake | Loads into tables, often `VARIANT` columns          |
| Custom: change stream + Node.js             | Both      | Full control, you handle retries and ordering       |

```js
for await (const c of db
  .collection("orders")
  .watch([], { fullDocument: "updateLookup" })) {
  await bigquery
    .dataset("shop")
    .table("orders_changes")
    .insert([
      {
        id: String(c.documentKey._id),
        op: c.operationType,
        doc: JSON.stringify(c.fullDocument ?? null),
        ts: new Date(),
      },
    ]);
  await saveResumeToken(c._id);
}
```

Write changes to an append-only table first, then `MERGE` into the final table on a schedule. That keeps loading simple and makes reprocessing possible.

## 285: How do you build an incremental pipeline with Snowflake streams and tasks?

**MongoDB**

You would write a change stream reader in Node.js that saves a resume token and updates a target collection.

**Snowflake**

```sql
CREATE STREAM raw_orders_stream ON TABLE raw_orders;

CREATE TASK load_orders
  WAREHOUSE = app_wh
  SCHEDULE = '5 MINUTE'
  WHEN SYSTEM$STREAM_HAS_DATA('RAW_ORDERS_STREAM')
AS
  MERGE INTO orders t
  USING (SELECT doc:_id::STRING AS id, doc:total::NUMBER(12,2) AS total, doc:status::STRING AS status FROM raw_orders_stream) s
  ON t.id = s.id
  WHEN MATCHED THEN UPDATE SET total = s.total, status = s.status
  WHEN NOT MATCHED THEN INSERT (id, total, status) VALUES (s.id, s.total, s.status);

ALTER TASK load_orders RESUME;
```

A stream remembers which rows of `raw_orders` were already processed, like a resume token. The `WHEN` clause skips runs (and warehouse cost) when nothing changed. Dynamic tables are a simpler option when the result can be written as one `SELECT`.

## 286: How do you pass query parameters safely in each database?

**MongoDB**

```js
await db.collection("users").findOne({ email: String(req.body.email) });
```

**SQL**

```js
await pool.query("SELECT * FROM users WHERE email = $1", [email]);
```

**BigQuery**

```js
await bigquery.query({
  query: "SELECT * FROM shop.users WHERE email = @email",
  params: { email },
});
```

**Snowflake**

```js
conn.execute({
  sqlText: "SELECT * FROM users WHERE email = ?",
  binds: [email],
  complete: (err, stmt, rows) => {},
});
```

**DynamoDB**

```js
ExpressionAttributeValues: { ":e": email } // values are never parsed as expression code
```

**Redis**

```js
await redis.ft.search("idx:users", "@email:{$email}", {
  PARAMS: { email },
  DIALECT: 2,
});
```

**Elasticsearch**

```js
query: {
  term: {
    email;
  }
} // structured JSON, never build query strings from user input
```

Never build SQL, ES|QL, `query_string` or RediSearch queries by string concatenation. Use bound parameters everywhere.

## 287: How does NoSQL injection translate to the other databases?

**MongoDB**

```js
// attacker sends { "password": { "$ne": null } }
await db
  .collection("users")
  .findOne({ email: req.body.email, password: req.body.password }); // BAD
await db.collection("users").findOne({ email: String(req.body.email) }); // force a string
```

- **SQL:** the classic SQL injection. Fixed by bound parameters (`$1`), never string concatenation.
- **BigQuery, Snowflake:** the same, use named or positional parameters.
- **Redis:** special characters in RediSearch queries (`@`, `{`, `|`, `-`) can change the meaning. Use `PARAMS` or escape them. Never pass user input to `EVAL` as script text.
- **DynamoDB:** values in `ExpressionAttributeValues` are safe. Building `FilterExpression` strings from user input is not.
- **Firebase:** with client access, the attack surface is the security rules, not query strings. Rules must check every field a user can write.
- **Elasticsearch:** `query_string` lets users write Lucene syntax, including expensive wildcards. Use `match` or `simple_query_string` for user input, and never put user input into scripts.

Validate input types (for example with Zod) before they reach any database.

## 288: How does id sort order change when you replace ObjectId?

An ObjectId starts with a timestamp, so `sort({ _id: 1 })` is roughly insertion order, and many apps rely on that without noticing.

| Id type             | Sorts by time? | Used in                             |
| ------------------- | -------------- | ----------------------------------- |
| ObjectId            | Yes (seconds)  | MongoDB                             |
| Identity / sequence | Yes            | SQL, Snowflake                      |
| UUID v4 (random)    | No             | Anywhere (`gen_random_uuid()`)      |
| UUID v7             | Yes (ms)       | PostgreSQL 18 `uuidv7()`, libraries |
| Firestore auto id   | No             | Firebase                            |
| ULID / KSUID        | Yes            | DynamoDB sort keys, anywhere        |

```js
import { ulid } from "ulid";
const sk = `ORDER#${ulid()}`; // sorts by creation time in DynamoDB
```

If the code sorts by `_id` to mean "newest first", translate that to an explicit `createdAt` sort or a time-ordered id. Random UUIDs also make B-tree inserts slower in SQL, which is why UUID v7 is popular.

## 289: How do you set created and updated timestamps automatically?

**MongoDB (Mongoose)**

```js
new mongoose.Schema({ name: String }, { timestamps: true });
```

**SQL**

```sql
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
-- plus a BEFORE UPDATE trigger that sets NEW.updated_at = now()
```

**BigQuery, Snowflake**

```sql
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
```

**DynamoDB**

```js
UpdateExpression: "SET updatedAt = :now, createdAt = if_not_exists(createdAt, :now)",
```

**Firebase**

```js
{ createdAt: FieldValue.serverTimestamp(), updatedAt: FieldValue.serverTimestamp() }
```

**Elasticsearch**

An ingest pipeline with `set` processors on `{{_ingest.timestamp}}`.

Prisma has `@default(now())` and `@updatedAt`, and Drizzle has `.defaultNow()` and `$onUpdate`, which give the same convenience as Mongoose `timestamps`.

## 290: How do you translate soft deletes?

**MongoDB**

```js
await db
  .collection("posts")
  .updateOne({ _id: id }, { $set: { deletedAt: new Date() } });
await db.collection("posts").find({ deletedAt: null }).toArray();
```

**SQL**

```sql
UPDATE posts SET deleted_at = now() WHERE id = 1;
CREATE INDEX posts_live_idx ON posts (created_at) WHERE deleted_at IS NULL;
CREATE VIEW live_posts AS SELECT * FROM posts WHERE deleted_at IS NULL;
```

**DynamoDB**

Set `deletedAt` and remove the GSI key attributes (`gsi1pk`), so the item drops out of list indexes automatically. Add a TTL to purge it later.

**Firebase**

Store `deleted: false` on every document, because Firestore cannot query "field is missing".

**Elasticsearch**

Usually just delete the document from the search index, even if the source database keeps it.

## 291: How do you translate multi-tenant data?

| Approach                | MongoDB                         | SQL                              | BigQuery                          | Redis                    | Snowflake                         | DynamoDB                        | Firebase                         | Elasticsearch                 |
| ----------------------- | ------------------------------- | -------------------------------- | --------------------------------- | ------------------------ | --------------------------------- | ------------------------------- | -------------------------------- | ----------------------------- |
| Shared, tenant id field | `tenantId` in every doc + index | `tenant_id` + row level security | `tenant_id` + row access policies | `t:{tenant}:` key prefix | `tenant_id` + row access policies | `pk = TENANT#t1#...`            | `tenants/{t}/...` subcollections | `tenantId` + filtered aliases |
| Separate per tenant     | Database per tenant             | Schema per tenant                | Dataset per tenant                | DB number or instance    | Database per tenant               | Table per tenant (limits apply) | Database per tenant              | Index per tenant              |

```sql
-- PostgreSQL
CREATE POLICY tenant_isolation ON orders USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

In DynamoDB, putting the tenant id first in the partition key also lets IAM `LeadingKeys` limit access per tenant.

## 292: How do you translate Mongoose models into Prisma or Drizzle for SQL?

**MongoDB (Mongoose)**

```js
const Order = mongoose.model(
  "Order",
  new mongoose.Schema(
    {
      user: { type: mongoose.Types.ObjectId, ref: "User", required: true },
      total: { type: Number, min: 0 },
      status: { type: String, enum: ["new", "paid"], default: "new" },
    },
    { timestamps: true },
  ),
);
```

**SQL (Prisma)**

```prisma
model Order {
  id        String   @id @default(uuid())
  user      User     @relation(fields: [userId], references: [id])
  userId    String
  total     Decimal  @db.Decimal(12, 2)
  status    Status   @default(new)
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

enum Status {
  new
  paid
}
```

**SQL (Drizzle)**

```js
export const orders = pgTable("orders", {
  id: uuid("id").primaryKey().defaultRandom(),
  userId: uuid("user_id")
    .notNull()
    .references(() => users.id),
  total: numeric("total", { precision: 12, scale: 2 }),
  status: text("status", { enum: ["new", "paid"] })
    .notNull()
    .default("new"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});
```

`ref` becomes a real foreign key, `enum` becomes a database enum or a check, and `min: 0` becomes a `CHECK` constraint you add in a migration.

## 293: How do you translate Mongoose middleware (pre and post hooks)?

**MongoDB (Mongoose)**

```js
userSchema.pre("save", async function () {
  if (this.isModified("password"))
    this.password = await bcrypt.hash(this.password, 12);
});
```

**SQL**

Put it in your service layer, or use Prisma client extensions (`$extends` with a `query` hook). Database triggers work for data rules (timestamps, audit rows), but not for things like password hashing.

**DynamoDB**

ElectroDB and DynamoDB Toolbox have attribute `set` functions that run before writes. Otherwise use a small repository module.

**Firebase**

Cloud Functions triggers (`onDocumentWritten`) run after the write, so they are like `post` hooks. For `pre` logic, use a converter or a service function.

The safest translation is usually a plain function, `createUser(data)`, that does the work before calling the database. Hidden hooks are a common source of surprises in Mongoose apps.

## 294: How do you translate populate()?

**MongoDB (Mongoose)**

```js
await Order.find({ status: "paid" }).populate("user", "name email");
```

**SQL (Prisma)**

```js
await prisma.order.findMany({
  where: { status: "paid" },
  include: { user: { select: { name: true, email: true } } },
});
```

**DynamoDB**

```js
const orders = (await ddb.send(new QueryCommand(paidOrdersQuery))).Items;
const userIds = [...new Set(orders.map((o) => o.userId))];
const { Responses } = await ddb.send(
  new BatchGetCommand({
    RequestItems: { Users: { Keys: userIds.map((id) => ({ id })) } },
  }),
);
```

**Firebase**

```js
const orders = await firestore
  .collection("orders")
  .where("status", "==", "paid")
  .get();
const userRefs = [...new Set(orders.docs.map((d) => d.get("userId")))].map(
  (id) => firestore.doc(`users/${id}`),
);
const users = await firestore.getAll(...userRefs);
```

**Elasticsearch**

Copy `user.name` and `user.email` into each order document when indexing.

`populate()` already runs a second query under the hood, so a batch get by ids is the honest translation. In SQL, a join does it in one round trip.

## 295: How do you get read-your-writes consistency after translating?

**MongoDB**

```js
const session = client.startSession({ causalConsistency: true });
await db.collection("posts").insertOne(post, { session });
await db
  .collection("posts")
  .find({ authorId }, { session, readPreference: "secondary" })
  .toArray(); // sees the insert
```

**SQL**

Read from the primary right after a write, or wait for the replica to catch up (`pg_last_wal_replay_lsn()`).

**DynamoDB**

```js
new GetCommand({ TableName: "Posts", Key: { id }, ConsistentRead: true });
// GSI queries cannot be strongly consistent; return the written item from the API instead of re-querying
```

**Firebase**

Strongly consistent by default. The client SDK also shows local writes instantly (latency compensation).

**Elasticsearch**

```js
await es.index({ index: "posts", document: post, refresh: "wait_for" });
```

A simple trick that works everywhere: after a create, return the created object from the API and add it to the list in the UI, instead of querying the list again.

## 296: How do you translate retryable writes and error retries?

MongoDB drivers retry a failed write once by default (`retryWrites=true`) and retry reads too.

- **SQL:** `pg` does not retry. Retry serialization failures (`40001`) and deadlocks (`40P01`) by running the whole transaction again.
- **BigQuery:** the client retries some errors. Use `insertId` with streaming inserts for best-effort dedupe, or the Storage Write API with offsets for exactly-once.
- **Redis:** node-redis reconnects automatically, but a command sent during a drop may fail. Make writes idempotent (`SET` instead of `INCR`) where you can.
- **Snowflake:** retry on network errors; DML is not automatically idempotent.
- **DynamoDB:** the AWS SDK retries throttling and 5xx errors with backoff (3 attempts by default, `maxAttempts` to change). `TransactWriteItems` accepts a `ClientRequestToken` to make retries idempotent for 10 minutes.
- **Firebase:** the SDK retries transient errors, and `runTransaction` retries on contention.
- **Elasticsearch:** the client retries on connection errors (`maxRetries`). Use explicit ids so a retried index call does not create duplicates.

## 297: How do you handle connections in serverless functions (Lambda, Cloud Functions)?

**MongoDB**

```js
let client; // outside the handler, reused between invocations
export const handler = async () => {
  client ??= new MongoClient(process.env.MONGODB_URI, { maxPoolSize: 5 });
  return client.db("shop").collection("users").findOne({});
};
```

**SQL**

Use a pooler between functions and the database (PgBouncer, RDS Proxy, Supabase pooler, Neon's pooled endpoint), or an HTTP driver like `@neondatabase/serverless`. Thousands of functions each opening connections will exhaust PostgreSQL's connection limit fast.

**Redis**

Reuse one client per function instance, or use an HTTP-based Redis service.

**DynamoDB, Firebase, BigQuery**

HTTP APIs with no connection limit. This is a big reason DynamoDB and Firestore are popular with serverless.

**Elasticsearch**

Reuse the client outside the handler, like MongoDB.

## 298: How do you test translated queries locally?

```js
// Testcontainers works for MongoDB, PostgreSQL, Redis, DynamoDB Local and Elasticsearch
import { PostgreSqlContainer } from "@testcontainers/postgresql";
const pg = await new PostgreSqlContainer("postgres:17").start();
const pool = new Pool({ connectionString: pg.getConnectionUri() });
```

| Database      | Local option                                                  |
| ------------- | ------------------------------------------------------------- |
| MongoDB       | `mongodb-memory-server` or a Docker container                 |
| SQL           | PostgreSQL in Docker or Testcontainers, PGlite for unit tests |
| BigQuery      | Community emulator, or a real sandbox dataset per test run    |
| Redis         | Docker `redis:8`                                              |
| Snowflake     | No emulator; a dev database or a clone per CI run             |
| DynamoDB      | DynamoDB Local (Docker or JAR)                                |
| Firebase      | Firebase Emulator Suite, also tests security rules            |
| Elasticsearch | Docker single-node with security turned off                   |

A good habit during a migration: run the same test cases against the old MongoDB query and the new query, and compare the outputs.

## 299: How do you translate Mongoose virtuals and computed fields?

**MongoDB (Mongoose)**

```js
userSchema.virtual("fullName").get(function () {
  return `${this.first} ${this.last}`;
});
```

**SQL**

```sql
ALTER TABLE users ADD COLUMN full_name TEXT GENERATED ALWAYS AS (first || ' ' || last) STORED;
```

**BigQuery**

```sql
CREATE VIEW shop.users_v AS SELECT *, CONCAT(first, ' ', last) AS full_name FROM shop.users;
```

**Snowflake**

```sql
CREATE TABLE users (first VARCHAR, last VARCHAR, full_name VARCHAR AS (first || ' ' || last));
```

**DynamoDB, Firebase, Redis**

Compute it in the converter or repository code when reading, or store it when writing if you need to query by it.

**Elasticsearch**

```js
runtime_mappings: { fullName: { type: "keyword", script: "emit(doc['first'].value + ' ' + doc['last'].value)" } }
```

A stored generated column can be indexed and filtered, which a Mongoose virtual never could.

## 300: How do you translate a basic CRUD API from MongoDB to each database?

| Operation           | MongoDB                 | SQL                             | Redis                | DynamoDB                           | Firebase             | Elasticsearch |
| ------------------- | ----------------------- | ------------------------------- | -------------------- | ---------------------------------- | -------------------- | ------------- |
| `POST /items`       | `insertOne`             | `INSERT ... RETURNING`          | `JSON.SET` with `NX` | `PutItem` + `attribute_not_exists` | `add()` / `create()` | `create`      |
| `GET /items/:id`    | `findOne({ _id })`      | `SELECT ... WHERE id`           | `JSON.GET`           | `GetItem`                          | `doc().get()`        | `get`         |
| `GET /items`        | `find().sort().limit()` | `SELECT ... ORDER BY ... LIMIT` | `FT.SEARCH`          | `Query` on a GSI                   | `orderBy().limit()`  | `search`      |
| `PATCH /items/:id`  | `updateOne($set)`       | `UPDATE ... RETURNING`          | `JSON.SET` on a path | `UpdateItem`                       | `update()`           | `update`      |
| `DELETE /items/:id` | `deleteOne`             | `DELETE`                        | `DEL`                | `DeleteItem`                       | `delete()`           | `delete`      |

BigQuery and Snowflake are left out on purpose: they are for analytics, not for serving a CRUD API. Return `404` the same way everywhere: MongoDB returns `null`, SQL returns zero rows, DynamoDB returns no `Item`, Firestore returns `exists: false`, and Elasticsearch throws a `404` error you must catch.

# Advanced Questions (301-450)

## 301: How would you plan a full migration from MongoDB to PostgreSQL?

1. **Inventory.** List collections, document shapes (with sampling), indexes, queries and aggregations. Note which fields are always present and which are optional.
2. **Design the schema.** Top-level fields that every document has become columns. Embedded objects become columns or child tables. Truly flexible parts become `JSONB`. Every `$lookup` and `ref` becomes a foreign key.
3. **Pick ids.** Keep the ObjectId hex as a `CHAR(24)` or `TEXT` key during the migration so references still match, or map them to UUIDs with a lookup table.
4. **Write migrations** with Prisma, Drizzle or plain SQL, including indexes and constraints.
5. **Backfill** with a script that reads MongoDB in batches and inserts with `COPY` or multi-row `INSERT`.
6. **Keep them in sync** with dual writes or CDC (change streams) until cut-over.
7. **Verify** counts, checksums and a sample of API responses from both sides.
8. **Switch reads, then writes**, behind a feature flag, and keep MongoDB read-only for a while as a fallback.

The hardest part is usually not the data but finding all the places the app relies on MongoDB behavior, like missing fields meaning "default", or arrays that are sometimes a single value.

## 302: How would you plan a migration from MongoDB to DynamoDB?

1. **Write down every access pattern** with its filters, sort and expected volume. DynamoDB design starts here, not from the MongoDB collections.
2. **Design keys** (often single-table): partition keys that spread load, sort keys that give the order you need, and GSIs for other lookups.
3. **Check limits.** Items over 400 KB must be split or moved to S3. Big arrays become separate items.
4. **Plan aggregations.** `$group` and counts become precomputed counters, Streams + Lambda, or exports to Athena, BigQuery or Snowflake.
5. **Plan search.** Text search and multi-filter pages move to OpenSearch or Elasticsearch.
6. **Backfill** with a script using `BatchWriteCommand`, or export MongoDB to S3 and use DynamoDB import from S3 for a new table.
7. **Dual write or CDC**, verify, then cut over.

If many MongoDB queries are ad hoc ("filter by anything, sort by anything"), DynamoDB is likely the wrong target. It is great for known access patterns at any scale and poor for flexible querying.

## 303: How would you plan a migration from MongoDB to Firestore?

1. **Map collections to collections**, and large embedded arrays to subcollections.
2. **List queries** and generate composite indexes (`firestore.indexes.json`). Remember there is no join, no full-text search and limited aggregation (`count`, `sum`, `average`).
3. **Check limits.** Documents up to 1 MiB, about one sustained write per second per document, 500 writes per batch, and per-database write throughput.
4. **Decide on access.** If clients will read Firestore directly, write and test security rules with the emulator before cut-over.
5. **Backfill** with `BulkWriter`, which handles rate limits and retries for you.
6. **Translate types.** `Date` becomes `Timestamp`, `Decimal128` becomes integer cents or a string, ObjectId becomes the document id string.

Firestore Enterprise edition also offers MongoDB compatibility (you connect with MongoDB drivers), which can cut migration effort a lot, but check which operators and features it supports before relying on it.

## 304: How do you plan moving MongoDB analytics to BigQuery or Snowflake?

Keep MongoDB as the app database and copy data into the warehouse for reporting:

1. **Pick a sync method.** Nightly exports for simple cases, CDC (change streams via Debezium, Fivetran, Airbyte or a Dataflow template) for near real time.
2. **Land raw documents first** in a `JSON` (BigQuery) or `VARIANT` (Snowflake) column, with `_id`, operation type and timestamp.
3. **Model with SQL** (often dbt): build typed staging tables, then facts and dimensions. Unwind arrays with `UNNEST` or `FLATTEN`.
4. **Translate pipelines.** Each MongoDB aggregation used for reports becomes a SQL view, table or dbt model.
5. **Partition and cluster** on the columns used in filters (`created_at`, `tenant_id`).
6. **Turn off the heavy aggregations** on MongoDB once the reports read from the warehouse.

This usually lowers load on the primary database and makes reports much faster and cheaper, because warehouses scan columns, not whole documents.

## 305: How do you add Elasticsearch next to MongoDB for search?

1. **Keep MongoDB as the source of truth.** Elasticsearch is a search copy that can be rebuilt at any time.
2. **Design a search document** per entity with copied fields from related collections (author name, category name) so no join is needed.
3. **Sync** with a change stream worker, or Debezium + Kafka Connect. Save the resume token so restarts do not lose events.
4. **Use the MongoDB `_id` as the Elasticsearch `_id`**, so updates and deletes hit the right document and replays are idempotent.
5. **Use an alias** (`products` pointing to `products_v1`) so you can build `products_v2` with a new mapping and switch atomically.
6. **Search returns ids**, and the app loads full records from MongoDB when it needs fresh or private data.

```js
for await (const c of db.collection("products").watch([], {
  fullDocument: "updateLookup",
  resumeAfter: await loadToken(),
})) {
  if (c.operationType === "delete")
    await es.delete(
      { index: "products", id: String(c.documentKey._id) },
      { ignore: [404] },
    );
  else
    await es.index({
      index: "products",
      id: String(c.documentKey._id),
      document: toSearchDoc(c.fullDocument),
    });
  await saveToken(c._id);
}
```

If you are on Atlas, Atlas Search does this without a separate cluster. Elasticsearch makes sense when you need its features, run outside Atlas, or search across many data sources.

## 306: How do you put Redis in front of a database as a cache?

**Cache-aside (most common)**

```js
async function getProduct(id) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);
  const product = await loadFromDb(id); // MongoDB, PostgreSQL, DynamoDB...
  await redis.set(`product:${id}`, JSON.stringify(product), { EX: 300 });
  return product;
}

async function updateProduct(id, changes) {
  await saveToDb(id, changes);
  await redis.del(`product:${id}`); // delete, don't update, to avoid races
}
```

- Always set a TTL, so a missed invalidation fixes itself.
- Delete on write instead of writing the new value; two concurrent writers can otherwise leave old data in the cache.
- Cache objects that are read often and change rarely. Don't cache things that must be exact, like account balances.

The pattern is the same no matter which database is behind Redis. For DynamoDB, DAX is a managed alternative for `GetItem` and `Query`.

## 307: How do you migrate with zero downtime using dual writes?

```text
Phase 1: app writes MongoDB only            -> backfill target from MongoDB
Phase 2: app writes MongoDB, then target    -> compare reads in the background (shadow reads)
Phase 3: app reads target, still writes both -> watch errors and latency
Phase 4: app writes target only             -> MongoDB kept read-only for rollback, then retired
```

Things that go wrong:

- **One write succeeds and the other fails.** Dual writes are not atomic. Either use CDC from MongoDB (single writer, target follows), or log failures and fix them with a reconcile job.
- **Backfill and live writes overlap.** Use an `updatedAt` or version on every record, and let the newer one win in both the backfill and the sync.
- **Different id formats.** Decide the id mapping before Phase 1.

CDC (change streams into the target) is usually safer than dual writes in app code, because MongoDB stays the only writer until cut-over.

## 308: How do you verify that migrated data matches?

1. **Counts** per collection and per important filter (`status`, `tenantId`, day).
2. **Sums and min/max** of numeric fields and dates.
3. **Checksums** of each record, computed the same way on both sides.
4. **Sample deep compares** of random records, field by field after normalizing types.
5. **Query comparisons**: run the top real queries on both and compare result sets.

```js
import { createHash } from "node:crypto";
const hash = (o) =>
  createHash("sha256")
    .update(JSON.stringify(normalize(o)))
    .digest("hex");

for await (const doc of db.collection("users").find().sort({ _id: 1 })) {
  const row = (
    await pool.query("SELECT * FROM users WHERE id = $1", [String(doc._id)])
  ).rows[0];
  if (!row || hash(fromMongo(doc)) !== hash(fromSql(row)))
    mismatches.push(String(doc._id));
}
```

`normalize` must sort keys and convert dates, decimals and ids to the same form, or everything will look different. For warehouses, compare aggregates by day with SQL on the warehouse side and an aggregation on MongoDB.

## 309: How do you handle schema drift in MongoDB documents during migration?

Old MongoDB collections often have the same field in different types (`age: "30"` and `age: 30`), different names (`phone` and `phoneNumber`), or shapes from older app versions.

1. **Measure it.** Run an aggregation over the collection that groups by `$type` of each field.

```js
await db
  .collection("users")
  .aggregate([
    { $project: { t: { $type: "$age" } } },
    { $group: { _id: "$t", n: { $sum: 1 } } },
  ])
  .toArray(); // e.g. [{ _id: "int", n: 9800 }, { _id: "string", n: 200 }, { _id: "missing", n: 50 }]
```

2. **Decide a rule per field**: convert, default, or reject to a "quarantine" table for manual review.
3. **Put the rules in one transform function** used by both the backfill and the live sync.
4. **Make the target strict** (types, `NOT NULL`, `dynamic: strict`), so new drift fails loudly instead of sneaking in.

Warehouses can be more forgiving: land everything in `JSON`/`VARIANT` and use `SAFE_CAST` / `TRY_CAST` in the typed layer.

## 310: How do you translate ObjectId references while keeping relations intact?

Option A: **keep the hex string** as the new id everywhere.

```sql
CREATE TABLE users (id CHAR(24) PRIMARY KEY, ...);
CREATE TABLE orders (id CHAR(24) PRIMARY KEY, user_id CHAR(24) REFERENCES users(id));
```

Simple, and every reference still lines up. It works the same in DynamoDB keys, Firestore document ids and Elasticsearch `_id`.

Option B: **new ids plus a mapping table**.

```sql
CREATE TABLE id_map (mongo_id CHAR(24) PRIMARY KEY, new_id UUID NOT NULL UNIQUE);
```

Load all parents first, record their new ids, then translate every reference in children through the map. Use this when the target needs numeric or UUID keys.

Watch for references hidden in places that are not obvious: arrays of ids, ids inside embedded documents, ids stored as strings in some documents and as ObjectId in others, and ids inside URLs or other systems (payment provider metadata, analytics).

## 311: How do you turn deeply nested documents into normalized tables?

**MongoDB**

```js
{
  _id: "o1",
  customer: { id: "u1", name: "Ana" },
  items: [{ sku: "A", qty: 2, options: [{ name: "color", value: "red" }] }],
  payments: [{ method: "card", amount: 50 }],
}
```

**SQL**

```sql
CREATE TABLE orders (id TEXT PRIMARY KEY, customer_id TEXT REFERENCES customers(id));
CREATE TABLE order_items (id BIGSERIAL PRIMARY KEY, order_id TEXT REFERENCES orders(id), sku TEXT, qty INT);
CREATE TABLE order_item_options (item_id BIGINT REFERENCES order_items(id), name TEXT, value TEXT);
CREATE TABLE payments (id BIGSERIAL PRIMARY KEY, order_id TEXT REFERENCES orders(id), method TEXT, amount_cents INT);
```

Rules:

- Each array of objects becomes a child table with a foreign key to its parent.
- Embedded objects that are copies of another entity (`customer.name`) become a foreign key, unless the copy must stay frozen in time.
- Small leaf structures (`options`) can stay as `JSONB` if you never query them on their own.

In BigQuery you would keep this nested as `ARRAY<STRUCT<...>>` instead, because normalizing would add joins without any benefit.

## 312: When should you use JSONB and when normalized columns in PostgreSQL?

Use **normal columns** when the field:

- exists on every row,
- is used in `WHERE`, `JOIN`, `ORDER BY` or `GROUP BY`,
- needs constraints (foreign key, unique, check), or
- is updated often on its own.

Use **JSONB** when the data:

- has a shape that varies per row (product specs, custom fields, third-party payloads),
- is read and written as a whole,
- is rarely filtered on, or filtered only by containment (`@>`).

Downsides of JSONB to keep in mind: planner statistics are weaker, so estimates can be off; updating one key rewrites the whole value; and there are no foreign keys inside. Moving every MongoDB document into a single `doc JSONB` column "to migrate fast" gives you a slower MongoDB without its tools.

## 313: How do you translate unbounded arrays?

An array that grows forever (log entries, followers, messages) is already a problem in MongoDB because of the 16 MB limit and slow updates. Every target needs it split out:

- **SQL:** a child table with an index on the parent id.
- **BigQuery, Snowflake:** a separate event table, partitioned by date.
- **Redis:** a separate list, set, sorted set or stream per parent, trimmed if it can be.
- **DynamoDB:** one item per element under the parent's partition key (`pk = CHAT#c1`, `sk = MSG#<time>`). If one parent can get huge, add a time bucket to the partition key.
- **Firebase:** a subcollection.
- **Elasticsearch:** separate documents, not a growing array on one document.

## 314: How do size limits compare, and what do you do when a document is too big?

| Database         | Max record size                                                              |
| ---------------- | ---------------------------------------------------------------------------- |
| MongoDB          | 16 MB per document                                                           |
| SQL (PostgreSQL) | 1 GB per field (TOAST), rows can be large                                    |
| BigQuery         | 100 MB per row                                                               |
| Redis            | 512 MB per string value                                                      |
| Snowflake        | 128 MB per `VARIANT` / `VARCHAR` value                                       |
| DynamoDB         | 400 KB per item, including attribute names                                   |
| Firebase         | 1 MiB per document                                                           |
| Elasticsearch    | `http.max_content_length` 100 MB per request by default; large docs are slow |

When a MongoDB document is too big for DynamoDB or Firestore:

1. Move large blobs (images, PDFs, long HTML) to S3 or Cloud Storage and store the path.
2. Split arrays into separate items or a subcollection.
3. Compress big text with gzip and store it as binary (DynamoDB `B` type), if you never query inside it.
4. Use short attribute names in DynamoDB for very large item counts, because names count toward the size.

## 315: How does MongoDB sharding translate?

| MongoDB          | Equivalent                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| SQL (PostgreSQL) | No built-in sharding. Citus, partitioning plus app-level routing, or a distributed SQL database |
| BigQuery         | Not your concern. Storage and compute scale automatically                                       |
| Redis            | Redis Cluster: 16,384 hash slots spread across primaries                                        |
| Snowflake        | Not your concern. Micro-partitions and warehouse size                                           |
| DynamoDB         | Automatic partitions by partition key hash                                                      |
| Firebase         | Automatic. Avoid hot spots like sequential ids and one busy document                            |
| Elasticsearch    | Primary shards set at index creation, routing by `_id` or a custom key                          |

With MongoDB you choose a shard key and manage balancing. DynamoDB and Firestore do the splitting for you, but your key choice still decides whether load spreads well.

## 316: How do you choose a partition key compared to a MongoDB shard key?

The rules are almost the same for a MongoDB shard key, a DynamoDB partition key, a Redis Cluster hash tag, an Elasticsearch routing key and a Citus distribution column:

- **High cardinality.** Many distinct values (`userId`, `deviceId`), not `status` or `country`.
- **Even traffic.** No single value gets a large share of reads or writes.
- **Matches the main query.** Most queries should hit one key value, so they go to one shard or partition.
- **Not monotonic for writes**, unless the system handles it (DynamoDB hashes the key, so a sequential id is fine there; a MongoDB ranged shard key on a timestamp is not).

For DynamoDB, the partition key also decides what you can `Query`, so it is part of the data model, not only a scaling setting.

## 317: How do you avoid hot partitions?

**MongoDB**

Hashed shard keys, or compound keys like `{ tenantId: 1, _id: "hashed" }`.

**DynamoDB**

```js
// write sharding: spread one hot logical key over N partition keys
const shard = Math.floor(Math.random() * 10);
Item: { pk: `COUNTER#pageviews#${shard}`, n: 1 }
// read: Query all 10 keys in parallel and add them up
```

**Firebase**

```js
// distributed counter: N shard documents, increment one at random
await firestore
  .doc(`counters/views/shards/${Math.floor(Math.random() * 10)}`)
  .set({ n: FieldValue.increment(1) }, { merge: true });
```

**Redis Cluster**

Split a very hot key into several keys (`hot:{1}`, `hot:{2}`), or use client-side caching for hot reads.

**Elasticsearch**

Don't route all documents with a custom routing key that one tenant dominates. Use `index.routing_partition_size` to spread a routing value over several shards.

Signs of a hot partition: throttling (`ProvisionedThroughputExceededException`) while total capacity is far from used, or one Redis node at 100% CPU while the others are idle.

## 318: How do replica sets and failover translate?

- **MongoDB:** a replica set of 3+ nodes elects a new primary in seconds. Drivers find the new primary automatically.
- **SQL:** streaming replication with a tool that promotes a standby (Patroni, or managed failover in RDS, Cloud SQL, Azure). Clients reconnect to a DNS name that moves.
- **BigQuery, Snowflake:** fully managed. Snowflake also has replication and failover groups across regions or clouds.
- **Redis:** replicas plus Sentinel, or Redis Cluster with automatic failover. Replication is asynchronous, so a failover can lose the last writes.
- **DynamoDB:** data is copied across three availability zones automatically. Global tables add other regions.
- **Firebase:** multi-region locations (`nam5`, `eur3`) keep working through a regional outage.
- **Elasticsearch:** replica shards are promoted when a primary shard's node goes away. Cross-cluster replication covers other regions.

## 319: How do MongoDB read concern levels map to other databases?

| MongoDB read concern | Meaning                                           | Closest match                                                                                          |
| -------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `local`              | Latest data on this node, may be rolled back      | Redis replica, DynamoDB eventually consistent read                                                     |
| `majority`           | Data acknowledged by most nodes, won't roll back  | PostgreSQL primary with sync replicas, DynamoDB `ConsistentRead`, Firestore reads                      |
| `linearizable`       | Reflects all writes that finished before the read | DynamoDB `ConsistentRead` on the base table, Firestore transactions                                    |
| `snapshot`           | Consistent point-in-time view across documents    | PostgreSQL `REPEATABLE READ`, Snowflake and BigQuery queries (always a snapshot), Firestore `readTime` |

Elasticsearch has no read concern. A search sees the last refresh on whichever shard copy answers.

## 320: How do change events stay in order when syncing to another database?

- **MongoDB change streams** are in oplog order for a replica set, and in cluster-time order across shards.
- **DynamoDB Streams** keep order per item (per partition key), not across the whole table.
- **Firestore triggers** have no order guarantee and can be delivered more than once.
- **Kafka (Debezium)** keeps order per partition, so partition by document id.
- **Redis Streams** are in order per stream.

To apply events safely in any order, store a version or the source timestamp with each record and skip older events:

```sql
INSERT INTO orders (id, status, version) VALUES ($1, $2, $3)
ON CONFLICT (id) DO UPDATE SET status = EXCLUDED.status, version = EXCLUDED.version
WHERE orders.version < EXCLUDED.version;
```

```js
// Elasticsearch: external versioning rejects older versions
await es.index({
  index: "orders",
  id,
  document,
  version: doc.version,
  version_type: "external",
});
```

## 321: How do transaction isolation levels compare?

- **MongoDB:** transactions read from a snapshot (like snapshot isolation). Write conflicts abort one transaction.
- **SQL (PostgreSQL):** `READ COMMITTED` by default, with `REPEATABLE READ` (snapshot) and `SERIALIZABLE` available.
- **BigQuery:** multi-statement transactions use snapshot isolation. Conflicting DML on the same table can fail.
- **Redis:** commands run one at a time, so `MULTI`/`EXEC` and Lua scripts are fully serial while they run, but there is no rollback.
- **Snowflake:** `READ COMMITTED` for tables. Each statement sees data committed before it began.
- **DynamoDB:** transactions are serializable across the items in them. A normal read outside a transaction can see a transaction's writes only after it commits.
- **Firebase:** serializable transactions. Server SDK transactions use pessimistic locks; client transactions use optimistic concurrency.
- **Elasticsearch:** no transactions.

The common surprise when moving to PostgreSQL: its default `READ COMMITTED` allows a second `SELECT` in the same transaction to see new commits. Use `REPEATABLE READ` to get MongoDB-like snapshot behavior.

## 322: What are the transaction limits in each database?

| Database      | Limits                                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------- |
| MongoDB       | 60 seconds by default (`transactionLifetimeLimitSeconds`), oplog entry size limits                  |
| SQL           | Practically none, but long transactions block vacuum and hold locks                                 |
| BigQuery      | Up to 6 hours, limits on DML per table                                                              |
| Redis         | No limit on commands, but a long `MULTI` or script blocks every other client                        |
| Snowflake     | No size limit, but statements waiting for a lock give up after `LOCK_TIMEOUT` (12 hours by default) |
| DynamoDB      | 100 items, 4 MB total, one region, no two operations on the same item                               |
| Firebase      | 270 seconds, 60 seconds idle; 500 writes per batch or transaction (field transforms count)          |
| Elasticsearch | No transactions                                                                                     |

DynamoDB's "100 items" rule shapes design the most: bulk changes must be split, so make each chunk safe to apply on its own.

## 323: How do you handle write conflicts and retries in transactions?

**MongoDB**

```js
await session.withTransaction(fn); // retries TransientTransactionError and UnknownTransactionCommitResult
```

**SQL**

```js
for (let attempt = 1; ; attempt++) {
  try {
    return await runInTransaction("SERIALIZABLE", fn);
  } catch (e) {
    if (!["40001", "40P01"].includes(e.code) || attempt === 5) throw e;
    await new Promise((r) => setTimeout(r, 2 ** attempt * 20));
  }
}
```

**DynamoDB**

```js
catch (err) {
  if (err.name === "TransactionCanceledException") {
    console.log(err.CancellationReasons); // ConditionalCheckFailed, TransactionConflict, ...
  }
}
```

**Firebase**

`runTransaction` retries up to 5 times by default. Your function must have no side effects (like sending emails) because it may run more than once.

Only retry errors that mean "try again" (conflicts, deadlocks, throttling). A failed condition check is a business result, not something to retry.

## 324: How do you coordinate a change across two different databases (saga)?

You cannot have one transaction across MongoDB and Redis, or PostgreSQL and Elasticsearch. A saga splits the work into steps, each with an undo:

```js
async function placeOrder(order) {
  await pg.query("INSERT INTO orders (id, status) VALUES ($1, 'pending')", [
    order.id,
  ]);
  try {
    await reserveStock(order); // DynamoDB conditional update
  } catch (e) {
    await pg.query("UPDATE orders SET status = 'failed' WHERE id = $1", [
      order.id,
    ]); // compensate
    throw e;
  }
  await pg.query("UPDATE orders SET status = 'confirmed' WHERE id = $1", [
    order.id,
  ]);
}
```

For real systems, drive the steps from a durable workflow (AWS Step Functions, Temporal, or a state column plus a retry job), so a crash in the middle is picked up and finished or undone. Each step must be idempotent because it may run twice.

## 325: How do you translate the transactional outbox pattern?

The outbox stores "events to publish" in the same transaction as the data, and a separate process sends them.

**MongoDB**

```js
await session.withTransaction(async () => {
  await db.collection("orders").insertOne(order, { session });
  await db
    .collection("outbox")
    .insertOne(
      { type: "order.created", payload: order, sent: false },
      { session },
    );
});
```

**SQL**

```sql
BEGIN;
INSERT INTO orders (...) VALUES (...);
INSERT INTO outbox (type, payload) VALUES ('order.created', '{"id": "o1"}');
COMMIT;
```

**DynamoDB**

```js
new TransactWriteCommand({
  TransactItems: [
    { Put: { TableName: "App", Item: order } },
    {
      Put: {
        TableName: "App",
        Item: { pk: "OUTBOX", sk: eventId, payload: order },
      },
    },
  ],
});
// or skip the outbox: DynamoDB Streams already publishes every committed change
```

**Firebase**

Write the order and the event document in one batch, and let a Cloud Function on the event collection publish it.

In MongoDB, change streams and DynamoDB Streams can replace the outbox table entirely, because the database itself becomes the reliable event source.

## 326: How do you make writes idempotent in each database?

An idempotent write gives the same result if it runs twice, which matters for retries and at-least-once event delivery.

**MongoDB**

```js
await db
  .collection("payments")
  .updateOne({ _id: paymentId }, { $setOnInsert: payment }, { upsert: true });
```

**SQL**

```sql
INSERT INTO payments (id, amount) VALUES ($1, $2) ON CONFLICT (id) DO NOTHING;
```

**BigQuery, Snowflake**

`MERGE` on a unique event id, so a replayed batch does not double rows.

**Redis**

```js
const first = await redis.set(`processed:${eventId}`, "1", {
  NX: true,
  EX: 86400,
});
if (!first) return; // already handled
```

**DynamoDB**

```js
new PutCommand({
  TableName: "Payments",
  Item: payment,
  ConditionExpression: "attribute_not_exists(id)",
});
```

**Firebase**

```js
await firestore.doc(`payments/${paymentId}`).create(payment); // second call fails with ALREADY_EXISTS
```

**Elasticsearch**

```js
await es.index({ index: "payments", id: paymentId, document: payment }); // same id overwrites, no duplicate
```

The key idea is the same everywhere: use a natural or client-generated id (event id, payment id), not a database-generated one, so the second write finds the first.

## 327: How do you load data into BigQuery or Snowflake exactly once?

**BigQuery**

- Batch: load files from Cloud Storage into a staging table, then `MERGE` on the event id. Re-running the job is harmless.
- Streaming: the Storage Write API in committed mode with stream offsets gives exactly-once per stream. The older `insertAll` with `insertId` is best-effort dedupe only.

**Snowflake**

- `COPY INTO` remembers which files it loaded for 64 days and skips them on the next run (unless `FORCE = TRUE`).
- Snowpipe has the same file-level dedupe.
- Snowpipe Streaming uses channels with offset tokens, so a restarted client continues from the last committed offset.

For both, the safest design is to accept duplicates in a raw table and dedupe in the model with `QUALIFY ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY ingested_at) = 1`. Then any retry anywhere in the pipeline is safe.

## 328: How do you rebuild a search index or cache from scratch without downtime?

**Elasticsearch**

```js
await es.indices.create({ index: "products_v2", mappings: newMappings });
await backfillFromSource("products_v2"); // from MongoDB or the main DB
// replay changes that happened during the backfill (from a saved resume token), then switch
await es.indices.updateAliases({
  actions: [
    { remove: { index: "products_v1", alias: "products" } },
    { add: { index: "products_v2", alias: "products" } },
  ],
});
```

**Redis**

Build the new data under a new prefix or logical name (`v2:product:*`), then switch the app config and let old keys expire. For a search index, `FT.ALIASUPDATE` points an alias to the new index.

**BigQuery, Snowflake**

Build into a new table, then `CREATE OR REPLACE TABLE ... CLONE` or `ALTER TABLE ... SWAP WITH` (Snowflake) to switch at once.

Write the resume token or the time the backfill started before you begin, so changes made during the rebuild are not lost.

## 329: How do you keep a cache consistent with the database?

| Strategy         | How it works                                                       | Risk                                             |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------------------ |
| TTL only         | Cache expires after N seconds                                      | Stale for up to N seconds                        |
| Delete on write  | App deletes the key after updating the DB                          | Race: a slow reader can put old data back        |
| Delete twice     | Delete, write DB, delete again after a short delay                 | Smaller race window                              |
| CDC invalidation | Change stream / DynamoDB Stream / logical replication deletes keys | Small delay, but catches writes from any service |
| Write-through    | App writes DB and cache together                                   | Partial failures leave them different            |

```js
// CDC-driven invalidation from MongoDB
for await (const c of db.collection("products").watch()) {
  await redis.del(`product:${c.documentKey._id}`);
}
```

Combine CDC invalidation with a TTL. CDC catches changes from every service that writes, and the TTL fixes anything it misses.

## 330: How do you prevent a cache stampede?

A stampede happens when a popular key expires and hundreds of requests hit the database at once.

```js
async function getWithLock(key, load, ttl = 300) {
  const hit = await redis.get(key);
  if (hit) return JSON.parse(hit);

  const gotLock = await redis.set(`lock:${key}`, "1", { NX: true, PX: 5000 });
  if (!gotLock) {
    await new Promise((r) => setTimeout(r, 50));
    return getWithLock(key, load, ttl); // someone else is loading
  }
  try {
    const value = await load();
    await redis.set(key, JSON.stringify(value), {
      EX: ttl + Math.floor(Math.random() * 30),
    }); // jitter
    return value;
  } finally {
    await redis.del(`lock:${key}`);
  }
}
```

Other tools: add random jitter to TTLs so keys don't all expire together, refresh hot keys early in the background before they expire, and coalesce identical requests in the app process. MongoDB does not have this problem on its own; it appears as soon as you add any cache in front of any database.

## 331: How durable is Redis compared to MongoDB?

MongoDB writes go to the journal and, with `w: "majority"`, to most replicas before the write is acknowledged. Redis keeps data in memory and has two persistence options:

- **RDB snapshots:** a point-in-time dump every N seconds. You can lose everything since the last snapshot.
- **AOF (append-only file):** every write is logged. With `appendfsync everysec` (the usual setting) you can lose about one second of writes. `always` is safer but slow.
- **Replication is asynchronous**, so a failover can lose recent writes even with AOF. `WAIT` can make a write wait for replicas, but that is not the same as a majority commit.

```text
appendonly yes
appendfsync everysec
```

So when you translate a MongoDB collection into Redis, ask whether losing the last second of data is acceptable. For caches, sessions and rate limits it usually is. For orders and payments it is not, and Redis should not be the only copy.

## 332: How do multi-key operations work in Redis Cluster?

Redis Cluster splits keys into 16,384 hash slots across nodes. Commands that touch several keys (`MULTI`, Lua scripts, `SINTER`, `MGET`) only work if all keys are in the same slot, otherwise you get `CROSSSLOT` errors.

```js
// braces mark the part that is hashed, so these keys share a slot
await cluster
  .multi()
  .hIncrBy("cart:{u1}", "sku1", 1)
  .expire("cart:{u1}", 86400)
  .sAdd("user:{u1}:recent", "sku1")
  .exec();
```

This is the Redis version of "keep related data in the same shard" in MongoDB or "same partition key" in DynamoDB. Be careful not to put too many keys under one tag, or you create a hot slot.

## 333: What happens when Redis runs out of memory?

MongoDB keeps working when data is larger than RAM: it reads from disk, just slower. Redis cannot. When `maxmemory` is reached, the `maxmemory-policy` decides:

| Policy         | Behavior                         | Good for                       |
| -------------- | -------------------------------- | ------------------------------ |
| `noeviction`   | Writes fail with an OOM error    | Primary data you can't lose    |
| `allkeys-lru`  | Evict least recently used keys   | A pure cache                   |
| `allkeys-lfu`  | Evict least frequently used keys | A cache with stable hot keys   |
| `volatile-lru` | Evict only keys with a TTL       | Mixed cache and permanent data |
| `volatile-ttl` | Evict keys closest to expiring   | Short-lived data               |

Keep cache data and important data in separate Redis instances, so a cache policy never evicts sessions or queues. Watch `used_memory` and `evicted_keys` in `INFO`.

## 334: How do you translate a big aggregation that needs allowDiskUse?

**MongoDB**

```js
await db
  .collection("events")
  .aggregate(pipeline, { allowDiskUse: true })
  .toArray(); // stages over 100 MB spill to disk
```

**SQL**

Raise `work_mem` for the session so sorts and hashes stay in memory, or let them spill to temp files (the default). Run on a replica so reporting does not slow down the primary.

**BigQuery**

Nothing to set. Shuffle spills automatically. If a query fails with "resources exceeded", the usual cause is an `ORDER BY` without `LIMIT` on a huge result or a single huge group.

**Snowflake**

Watch "bytes spilled to local/remote storage" in the query profile. Use a bigger warehouse for that query, or reduce data first.

**Elasticsearch**

Large `terms` aggregations hit `search.max_buckets`. Use `composite` aggregations and page through buckets with `after_key`.

```js
aggs: { users: { composite: { size: 1000, sources: [{ userId: { terms: { field: "userId" } } }], after: lastKey } } }
```

If a MongoDB aggregation needs `allowDiskUse` on a regular basis, it is usually a sign the work belongs in a warehouse.

## 335: How do you speed up pipelines with many $lookup stages when you translate them?

- **SQL:** joins are what SQL is built for. Index the foreign keys, check `EXPLAIN ANALYZE` for nested loops on large tables, and the same query that was slow in MongoDB is often fast.
- **BigQuery, Snowflake:** joins work fine at scale, but pre-joined wide tables (or nested arrays in BigQuery) are cheaper for dashboards. Filter both sides before the join.
- **DynamoDB, Firestore:** there is nothing to translate a `$lookup` into. Store the related data together (same partition key or copied fields) so one read is enough.
- **Elasticsearch:** denormalize at index time. ES|QL `LOOKUP JOIN` exists for enrichment with small lookup indices, not for big many-to-many joins.
- **Redis:** fetch related keys in one round trip with pipelining or `JSON.MGET`.

A heavy `$lookup` chain in MongoDB is a hint that the data is relational. That is often the main reason a team moves to SQL.

## 336: What replaces the MongoDB profiler for finding slow queries?

| Database      | Tool                                                                            |
| ------------- | ------------------------------------------------------------------------------- |
| MongoDB       | Database profiler, slow query log, Atlas Query Profiler and Performance Advisor |
| SQL           | `pg_stat_statements`, `auto_explain`, `log_min_duration_statement`              |
| BigQuery      | `INFORMATION_SCHEMA.JOBS` (bytes, slot time), execution graph in the console    |
| Redis         | `SLOWLOG GET`, `LATENCY DOCTOR`, `INFO commandstats`                            |
| Snowflake     | `SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY`, Query Profile in Snowsight             |
| DynamoDB      | CloudWatch metrics, Contributor Insights for hot keys, `ReturnConsumedCapacity` |
| Firebase      | Query Explain (`explain({ analyze: true })`), Query Insights in the console     |
| Elasticsearch | Search slow log, `profile: true`, Kibana Search Profiler                        |

```sql
-- top queries by total time in PostgreSQL
SELECT query, calls, total_exec_time, mean_exec_time FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10;

-- most expensive BigQuery queries this week
SELECT user_email, query, total_bytes_billed FROM `region-us`.INFORMATION_SCHEMA.JOBS
WHERE creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) ORDER BY total_bytes_billed DESC LIMIT 10;
```

## 337: How do you find unused indexes like $indexStats?

**MongoDB**

```js
await db
  .collection("orders")
  .aggregate([{ $indexStats: {} }])
  .toArray(); // accesses.ops per index
```

**SQL**

```sql
SELECT relname, indexrelname, idx_scan FROM pg_stat_user_indexes WHERE idx_scan = 0;
```

**Redis**

```js
await redis.ft.info("idx:orders"); // number of docs, index size; no usage counter
```

**DynamoDB**

CloudWatch `ConsumedReadCapacityUnits` per GSI. A GSI with writes but no reads is costing you for nothing.

**Snowflake**

```sql
SELECT * FROM TABLE(INFORMATION_SCHEMA.SEARCH_OPTIMIZATION_HISTORY());
```

**Elasticsearch**

`GET _field_usage_stats` on an index shows which fields queries actually use.

Unused indexes cost write speed and storage everywhere, and in DynamoDB every GSI also doubles the write cost for items it contains.

## 338: How do you control query cost in BigQuery?

1. **Select only needed columns.** `SELECT *` bills every column, and `LIMIT` does not reduce bytes scanned on regular tables.
2. **Partition and cluster**, and turn on `require_partition_filter`.
3. **Dry run first** to see bytes before running.
4. **Set a limit per query** with `maximumBytesBilled`.
5. **Use materialized views and BI Engine** for dashboards that run the same queries again and again.
6. **Pick a pricing model.** On-demand (pay per TB scanned) or capacity (reserved slots with editions), depending on how steady the load is.

```js
await bigquery.query({ query, maximumBytesBilled: String(10 * 1024 ** 3) }); // fail above 10 GB
```

```bash
bq query --dry_run --use_legacy_sql=false 'SELECT user_id FROM shop.events WHERE DATE(created_at) = "2026-11-26"'
```

MongoDB costs scale with cluster size, not with each query. In BigQuery a single careless query can cost real money, so this needs guardrails from day one.

## 339: How do you control cost in Snowflake?

1. **Right-size warehouses.** Start small (X-Small) and increase only when queries are too slow. Each size up doubles credits per hour.
2. **Auto-suspend quickly** (for example 60 seconds) and auto-resume.
3. **Separate warehouses** for loading, BI and data science, so you can size and track each.
4. **Resource monitors** to notify or suspend when a credit quota is reached.
5. **Watch hidden costs.** Automatic clustering, search optimization, materialized views, serverless tasks and Snowpipe all use credits in the background.

```sql
CREATE WAREHOUSE bi_wh WAREHOUSE_SIZE = XSMALL AUTO_SUSPEND = 60 AUTO_RESUME = TRUE;
CREATE RESOURCE MONITOR monthly_cap WITH CREDIT_QUOTA = 500 TRIGGERS ON 90 PERCENT DO NOTIFY ON 100 PERCENT DO SUSPEND;
ALTER WAREHOUSE bi_wh SET RESOURCE_MONITOR = monthly_cap;
```

## 340: How do you control cost in DynamoDB?

- **Pick capacity mode.** On-demand for spiky or new workloads; provisioned with auto scaling for steady, predictable traffic (often much cheaper at scale).
- **Avoid scans.** Every item a `Scan` reads costs read units, even if the filter throws it away.
- **Use eventually consistent reads** where you can; they cost half.
- **Keep items small** and project only needed attributes into GSIs (`KEYS_ONLY` or `INCLUDE`). A GSI with `ALL` doubles storage and write cost.
- **Use TTL** to delete old items for free instead of paying for deletes.
- **Use Standard-IA table class** for large tables that are rarely read.

| Operation     | Cost unit                   |
| ------------- | --------------------------- |
| Write         | 1 WCU per 1 KB (rounded up) |
| Strong read   | 1 RCU per 4 KB              |
| Eventual read | 0.5 RCU per 4 KB            |
| Transaction   | Twice the normal cost       |

A MongoDB habit like "update one field in a 300 KB document" costs 300 write units each time in DynamoDB, because the whole item size counts.

## 341: How do you control cost in Firestore?

Firestore bills per document read, write and delete, plus storage and network.

- **Every listener update is a read.** A listener on a big query that changes often adds up fast.
- **Use `count()`, `sum()` and `average()`** aggregation queries instead of reading documents to count them (they bill by index entries read, which is much cheaper).
- **Avoid offset.** Skipped documents are still billed. Use `startAfter`.
- **Denormalize to save reads.** One document with everything a screen needs is cheaper than five reads.
- **Exempt fields from indexing** that you never query (large text, arrays), to save index storage and write cost.
- **Cache on the client** with offline persistence.

A MongoDB page that runs `find()` returning 1,000 documents is cheap on MongoDB but costs 1,000 reads in Firestore every time.

## 342: How do you size Elasticsearch shards?

- Aim for shards of about **10 to 50 GB** (and under about 200 million documents each).
- Too many small shards waste memory and slow the cluster. Too few huge shards make recovery and rebalancing slow.
- The number of primary shards is fixed at creation (you can only split or shrink into a new index). For growing data, use **data streams with rollover** instead of one giant index.

```js
await es.ilm.putLifecycle({
  name: "logs",
  policy: {
    phases: {
      hot: {
        actions: {
          rollover: { max_primary_shard_size: "50gb", max_age: "1d" },
        },
      },
      delete: { min_age: "30d", actions: { delete: {} } },
    },
  },
});
```

This is very different from MongoDB, where chunks split and move automatically. In Elasticsearch, shard planning is up to you.

## 343: How do you change a field's type in Elasticsearch without downtime?

MongoDB lets you just write the new type. Elasticsearch cannot change an existing field mapping, so you reindex:

```js
await es.indices.create({
  index: "orders_v2",
  mappings: {
    properties: { total: { type: "scaled_float", scaling_factor: 100 } },
  },
});
await es.reindex({
  source: { index: "orders_v1" },
  dest: { index: "orders_v2" },
  wait_for_completion: false,
});
// after it finishes and the sync has caught up:
await es.indices.updateAliases({
  actions: [
    { remove: { index: "orders_v1", alias: "orders" } },
    { add: { index: "orders_v2", alias: "orders", is_write_index: true } },
  ],
});
```

Always read and write through an alias from the start. Then every mapping change is a background reindex and one atomic alias switch. Adding a new field is the one change that does not need a reindex.

## 344: How do you page deep into Elasticsearch results?

`from + size` is limited to 10,000 results by default (`index.max_result_window`), much like `skip()` getting slow in MongoDB.

```js
const pit = await es.openPointInTime({ index: "orders", keep_alive: "1m" });
let searchAfter;
for (;;) {
  const res = await es.search({
    size: 1000,
    pit: { id: pit.id, keep_alive: "1m" },
    sort: [{ createdAt: "asc" }, { _shard_doc: "asc" }],
    search_after: searchAfter,
    query: { term: { status: "paid" } },
  });
  if (!res.hits.hits.length) break;
  process(res.hits.hits);
  searchAfter = res.hits.hits.at(-1).sort;
}
await es.closePointInTime({ id: pit.id });
```

A point in time (PIT) keeps a consistent view while you page, and `search_after` uses the last sort values like keyset paging in SQL. The old `scroll` API still works but is no longer recommended for deep paging.

## 345: How do you translate Atlas Vector Search?

**MongoDB**

```js
[
  {
    $vectorSearch: {
      index: "vec",
      path: "embedding",
      queryVector: q,
      numCandidates: 200,
      limit: 10,
      filter: { lang: "en" },
    },
  },
];
```

**SQL (pgvector)**

```sql
CREATE EXTENSION vector;
ALTER TABLE docs ADD COLUMN embedding vector(1536);
CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);
SELECT id, title FROM docs WHERE lang = 'en' ORDER BY embedding <=> $1 LIMIT 10;
```

**BigQuery**

```sql
SELECT base.id, distance FROM VECTOR_SEARCH(TABLE shop.docs, 'embedding', (SELECT @q AS embedding), top_k => 10, distance_type => 'COSINE');
```

**Redis**

```js
await redis.ft.search(
  "idx:docs",
  "(@lang:{en})=>[KNN 10 @embedding $vec AS score]",
  {
    PARAMS: { vec: Buffer.from(new Float32Array(q).buffer) },
    SORTBY: "score",
    DIALECT: 2,
  },
);
```

**Snowflake**

```sql
SELECT id, VECTOR_COSINE_SIMILARITY(embedding, $q::VECTOR(FLOAT, 1024)) AS score FROM docs ORDER BY score DESC LIMIT 10;
```

**Firebase**

```js
firestore.collection("docs").where("lang", "==", "en").findNearest({
  vectorField: "embedding",
  queryVector: q,
  limit: 10,
  distanceMeasure: "COSINE",
});
```

**Elasticsearch**

```js
await es.search({
  index: "docs",
  knn: {
    field: "embedding",
    query_vector: q,
    k: 10,
    num_candidates: 200,
    filter: { term: { lang: "en" } },
  },
});
```

DynamoDB has no vector search; teams pair it with OpenSearch or a vector store. Snowflake's `VECTOR_COSINE_SIMILARITY` is a brute-force scan; for large sets Cortex Search is the managed option.

## 346: How do you translate hybrid search (keywords plus vectors)?

**MongoDB**

```js
[
  {
    $rankFusion: {
      input: {
        pipelines: {
          text: [{ $search: { text: { query: "red shoes", path: "title" } } }],
          vec: [{ $vectorSearch: {/* ... */} }],
        },
      },
    },
  },
];
```

**SQL**

Run a full-text query and a pgvector query, then merge them with reciprocal rank fusion (RRF) in SQL:

```sql
WITH t AS (SELECT id, ROW_NUMBER() OVER (ORDER BY ts_rank(tsv, q) DESC) r FROM docs, plainto_tsquery('red shoes') q WHERE tsv @@ q LIMIT 50),
     v AS (SELECT id, ROW_NUMBER() OVER (ORDER BY embedding <=> $1) r FROM docs ORDER BY embedding <=> $1 LIMIT 50)
SELECT id, SUM(1.0 / (60 + r)) AS score FROM (SELECT * FROM t UNION ALL SELECT * FROM v) x GROUP BY id ORDER BY score DESC LIMIT 10;
```

**Redis**

`FT.HYBRID` in recent Redis versions, or run a text and a KNN query and fuse in code.

**Elasticsearch**

```js
await es.search({
  index: "docs",
  retriever: {
    rrf: {
      retrievers: [
        { standard: { query: { match: { title: "red shoes" } } } },
        {
          knn: {
            field: "embedding",
            query_vector: q,
            k: 50,
            num_candidates: 200,
          },
        },
      ],
    },
  },
});
```

RRF only uses ranks, not raw scores, so you don't need to make BM25 scores and vector distances comparable.

## 347: How do you translate Queryable Encryption and client-side field-level encryption?

MongoDB CSFLE and Queryable Encryption encrypt fields in the driver, so the server never sees plaintext, and Queryable Encryption still allows equality and range queries.

- **SQL:** no built-in equivalent in PostgreSQL. Encrypt in the app (for example with AWS KMS envelope encryption) and store a separate keyed hash (HMAC) of the value for equality lookups.
- **BigQuery:** AEAD encryption functions (`AEAD.ENCRYPT`) with Cloud KMS keysets, plus deterministic encryption for joins and equality.
- **Redis:** encrypt values in the app before storing.
- **Snowflake:** `ENCRYPT` / `DECRYPT` functions, or better, tokenization with external functions and masking policies.
- **DynamoDB:** the AWS Database Encryption SDK encrypts attributes client side and supports "beacons" for limited searching on encrypted fields.
- **Firebase:** encrypt in Cloud Functions or the client before writing.
- **Elasticsearch:** no field encryption; encrypted values cannot be searched. Keep sensitive fields out of the index.

```js
// HMAC "blind index" for equality search on an encrypted email in SQL or DynamoDB
const emailHash = createHmac("sha256", process.env.BLIND_INDEX_KEY)
  .update(email.toLowerCase())
  .digest("hex");
```

## 348: How do encryption at rest and in transit compare?

All eight encrypt data at rest in their managed cloud versions (Atlas, RDS/Cloud SQL, BigQuery, Redis Cloud/ElastiCache, Snowflake, DynamoDB, Firestore, Elastic Cloud). The differences are in key control:

| Database      | Customer-managed keys                                                | In transit                       |
| ------------- | -------------------------------------------------------------------- | -------------------------------- |
| MongoDB Atlas | KMS keys from AWS, Azure or GCP                                      | TLS required                     |
| SQL (managed) | KMS keys (RDS, Cloud SQL)                                            | `sslmode=verify-full`            |
| BigQuery      | CMEK with Cloud KMS per dataset or table                             | HTTPS                            |
| Redis         | Depends on the provider; self-hosted Redis has no at-rest encryption | `rediss://` TLS                  |
| Snowflake     | Tri-Secret Secure (Business Critical edition)                        | HTTPS                            |
| DynamoDB      | AWS owned, AWS managed or customer managed KMS key                   | HTTPS                            |
| Firebase      | CMEK for Firestore                                                   | HTTPS                            |
| Elasticsearch | Elastic Cloud BYOK; self-managed uses disk encryption                | TLS on HTTP and transport layers |

Self-hosted Redis and PostgreSQL are the ones where you must set up encryption yourself.

## 349: How do you translate row-level or document-level security?

**MongoDB**

Usually app code, or Atlas App Services rules. Views with `$match` can limit what a role sees.

**SQL**

```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY by_tenant ON orders USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

**BigQuery**

```sql
CREATE ROW ACCESS POLICY eu_only ON shop.orders GRANT TO ('group:eu-team@example.com') FILTER USING (region = 'EU');
```

**Snowflake**

```sql
CREATE ROW ACCESS POLICY by_region AS (region STRING) RETURNS BOOLEAN ->
  EXISTS (SELECT 1 FROM region_access WHERE role_name = CURRENT_ROLE() AND region_access.region = region);
ALTER TABLE orders ADD ROW ACCESS POLICY by_region ON (region);
```

**DynamoDB**

IAM condition `dynamodb:LeadingKeys` limits access to items whose partition key matches the user.

**Firebase**

Security rules (`resource.data.ownerId == request.auth.uid`).

**Elasticsearch**

```js
await es.security.putRole({
  name: "eu",
  indices: [
    {
      names: ["orders"],
      privileges: ["read"],
      query: { term: { region: "EU" } },
    },
  ],
});
```

## 350: How do you hide fields from some users like $redact or projections?

**MongoDB**

```js
[
  {
    $redact: {
      $cond: [{ $in: ["$level", userLevels] }, "$$DESCEND", "$$PRUNE"],
    },
  },
];
```

**SQL**

```sql
REVOKE SELECT ON customers FROM analyst;
GRANT SELECT (id, name, city) ON customers TO analyst; -- column privileges
```

**BigQuery**

Policy tags on columns (Data Catalog) with data masking rules, for example showing only a hash of the email.

**Snowflake**

```sql
CREATE MASKING POLICY email_mask AS (val STRING) RETURNS STRING ->
  CASE WHEN CURRENT_ROLE() IN ('SUPPORT') THEN val ELSE '***' END;
ALTER TABLE customers MODIFY COLUMN email SET MASKING POLICY email_mask;
```

**DynamoDB**

IAM `dynamodb:Attributes` condition limits which attributes a role can read.

**Firebase**

Rules cannot hide single fields. Split private fields into a separate document (`users/{id}/private/data`) with stricter rules.

**Elasticsearch**

Field-level security on a role: `field_security: { grant: ["name", "city"] }`.

## 351: How do you translate database auditing?

| Database      | Audit option                                                                 |
| ------------- | ---------------------------------------------------------------------------- |
| MongoDB       | Atlas database auditing / Enterprise `auditLog`                              |
| SQL           | `pgaudit` extension, plus cloud provider logs                                |
| BigQuery      | Cloud Audit Logs (admin activity and data access), `INFORMATION_SCHEMA.JOBS` |
| Redis         | `ACL LOG` for denied commands; managed services add audit logs               |
| Snowflake     | `ACCOUNT_USAGE.ACCESS_HISTORY`, `LOGIN_HISTORY`, `QUERY_HISTORY`             |
| DynamoDB      | CloudTrail data events for item-level API calls                              |
| Firebase      | Cloud Audit Logs with Data Access logs turned on                             |
| Elasticsearch | Security audit logging (`xpack.security.audit.enabled`)                      |

Database audit logs show who ran which operation. They don't explain business changes ("who changed the price from 10 to 12"). For that, write an audit table or event stream from the app, or use CDC (change streams, DynamoDB Streams) to record before and after values.

## 352: How do you plan disaster recovery (RPO and RTO) for each database?

RPO is how much data you can lose; RTO is how long you can be down.

| Database      | Typical RPO                                                      | Typical RTO                 | Main tools                                    |
| ------------- | ---------------------------------------------------------------- | --------------------------- | --------------------------------------------- |
| MongoDB Atlas | Seconds (PITR)                                                   | Minutes to hours (restore)  | Continuous backup, multi-region clusters      |
| SQL (managed) | Seconds to 5 minutes                                             | Minutes (replica promotion) | PITR, cross-region read replicas              |
| BigQuery      | Near zero within a region                                        | Fast (managed)              | Time travel, cross-region dataset replication |
| Redis         | Up to the last AOF fsync or snapshot                             | Minutes                     | Replicas, AOF, backups to object storage      |
| Snowflake     | Near zero                                                        | Minutes (failover groups)   | Replication and failover across regions       |
| DynamoDB      | Seconds (PITR), about 1 second across regions with global tables | Near zero (global tables)   | PITR, backups, global tables                  |
| Firebase      | Near zero in multi-region                                        | Near zero in multi-region   | Multi-region locations, PITR, backups         |
| Elasticsearch | Since the last snapshot                                          | Restore time                | Snapshots, cross-cluster replication          |

Test the restore, not just the backup. A restore that nobody has tried is not a plan.

## 353: How do you translate multi-region, active-active setups?

- **MongoDB:** global clusters with zone sharding put each user's data in their region. Writes for a document still go to one primary.
- **SQL:** usually one primary region plus read replicas. Active-active needs a distributed SQL database (CockroachDB, Spanner, Aurora DSQL) or careful conflict handling.
- **BigQuery, Snowflake:** analytics usually live in one region with replicas for DR.
- **Redis:** Redis Enterprise / Redis Cloud Active-Active uses CRDTs so every region accepts writes.
- **DynamoDB:** global tables accept writes in every region. Conflicts resolve with "last writer wins" (or strong consistency mode across regions where offered).
- **Firebase:** multi-region locations replicate synchronously within one continent; there is no cross-continent active-active.
- **Elasticsearch:** cross-cluster replication is one-way per index (leader to follower).

With "last writer wins", two users editing the same item in two regions at once means one edit is lost. Design so each item is written in one home region, or use counters and sets that merge safely.

## 354: How do you keep data in a specific country or region (data residency)?

- **MongoDB:** pick the Atlas region; with global clusters, pin documents to zones by a `country` field in the shard key.
- **SQL:** pick the instance region; partition tables by region onto different servers if needed.
- **BigQuery:** dataset location (`EU`, `europe-west3`) is fixed at creation, and queries cannot join datasets in different locations.
- **Redis:** pick the region of the instance.
- **Snowflake:** the account region; use separate accounts for separate jurisdictions.
- **DynamoDB:** tables live in one region unless you add global table replicas, so don't replicate tables that must stay local.
- **Firebase:** the database location is fixed at creation; use separate databases per region.
- **Elasticsearch:** pick the cluster region; use separate clusters per jurisdiction.

The usual design is a separate deployment per region, plus a small global directory that says which region holds each tenant.

## 355: How do you handle time series retention and downsampling at scale?

**MongoDB**

Time series collections with `expireAfterSeconds`, plus a scheduled `$merge` into hourly rollup collections.

**SQL**

```sql
-- TimescaleDB
SELECT add_retention_policy('metrics', INTERVAL '30 days');
CREATE MATERIALIZED VIEW metrics_hourly WITH (timescaledb.continuous) AS
SELECT time_bucket('1 hour', ts) AS hour, sensor, avg(value) FROM metrics GROUP BY 1, 2;
```

**BigQuery**

Partition expiration for raw data, plus a scheduled query or materialized view for hourly data kept longer.

**Redis**

```js
await redis.ts.create("ts:s1:hourly", { RETENTION: 0 });
await redis.ts.createRule("ts:s1", "ts:s1:hourly", "AVG", 3600000); // downsample automatically
```

**Snowflake**

A dynamic table or task builds hourly rollups; a task deletes old raw rows.

**DynamoDB**

TTL deletes raw items; a Stream + Lambda updates hourly aggregate items as data arrives.

**Elasticsearch**

ILM with a `downsample` action in the warm phase and `delete` later.

## 356: How do you handle counters with very high write rates?

A single counter document receiving thousands of `$inc` per second becomes a hot spot in most databases.

- **MongoDB:** handles a lot, but document-level locking still serializes writes. Batch increments in the app or split into several counter docs.
- **SQL:** one hot row causes lock waits. Insert into a small "deltas" table and sum periodically, or keep several counter rows and sum them.
- **Redis:** the best fit. `INCR` handles hundreds of thousands per second per node.
- **DynamoDB:** one item supports up to about 1,000 write units per second (one partition). Shard the counter into N items.
- **Firebase:** about one sustained write per second per document is the safe rate. Use distributed counter shards.
- **Elasticsearch:** updating the same document often is slow (each update reindexes it). Count with aggregations instead.

A common design: count in Redis, flush totals to the database every few seconds.

## 357: How do you generate ids at scale without a central counter?

A MongoDB-style ObjectId (time + random + counter) is generated by the client and needs no coordination. To get the same benefit elsewhere:

- **UUID v7 or ULID:** time-ordered, random enough to never clash, works as a key in every database here.
- **Snowflake-style 64-bit ids** (timestamp + machine id + sequence): fit in a `BIGINT`, sortable. Need a unique machine id per worker.
- **Database sequences** (PostgreSQL, Snowflake): fine for one database; with sharding, use `CACHE` and accept gaps.
- **Redis `INCR`:** simple and fast, but a single point of failure; use `INCRBY 1000` to hand out blocks of ids to workers.
- **Firestore auto ids:** random, so they spread writes well, but they don't sort by time.

Avoid sequential ids as DynamoDB sort keys inside one partition with heavy writes, or as Firestore document ids (Firestore warns about monotonically increasing ids causing hot spots).

## 358: How do you model many-to-many at scale in DynamoDB?

**MongoDB**

```js
{ _id: "s1", courseIds: ["c1", "c2"] } // and an index on courseIds
```

**DynamoDB (adjacency list with an inverted GSI)**

```js
// base table
{ pk: "STUDENT#s1", sk: "COURSE#c1", enrolledAt: "2026-09-01", courseTitle: "Databases" }
{ pk: "STUDENT#s1", sk: "COURSE#c2", enrolledAt: "2026-09-01", courseTitle: "Networks" }
// GSI1 swaps them: gsi1pk = sk, gsi1sk = pk

// courses of a student
new QueryCommand({ TableName: "App", KeyConditionExpression: "pk = :s AND begins_with(sk, :c)", ExpressionAttributeValues: { ":s": "STUDENT#s1", ":c": "COURSE#" } });
// students of a course
new QueryCommand({ TableName: "App", IndexName: "GSI1", KeyConditionExpression: "gsi1pk = :c", ExpressionAttributeValues: { ":c": "COURSE#c1" } });
```

One edge item per relationship scales without limit, unlike an array inside one item. Copy the fields you show in lists (`courseTitle`) onto the edge, so listing needs no extra reads. The same GSI can serve several entity types ("GSI overloading") because keys are generic strings.

## 359: How do you translate a social graph query like friends of friends?

**MongoDB**

```js
[
  { $match: { _id: "u1" } },
  {
    $graphLookup: {
      from: "users",
      startWith: "$friends",
      connectFromField: "friends",
      connectToField: "_id",
      maxDepth: 1,
      as: "network",
    },
  },
];
```

**SQL**

```sql
SELECT DISTINCT f2.friend_id
FROM friendships f1 JOIN friendships f2 ON f2.user_id = f1.friend_id
WHERE f1.user_id = 'u1' AND f2.friend_id <> 'u1';
```

**Redis**

```js
const friends = await redis.sMembers("friends:u1");
await redis.sUnionStore(
  "tmp:fof:u1",
  friends.map((f) => `friends:${f}`),
);
await redis.sDiff(["tmp:fof:u1", "friends:u1"]); // friends of friends who are not already friends
```

**BigQuery, Snowflake**

The same self join as SQL works well for batch "people you may know" jobs over the whole graph.

**DynamoDB, Firebase**

Read the friend list, then read each friend's list in parallel. Precompute suggestions in a batch job if lists are large.

Two hops is fine in any of these. For deep or weighted graph queries, a graph database (Neo4j, Neptune) fits better than all of them.

## 360: How do you translate a product catalog with different attributes per category?

**MongoDB**

```js
{ name: "Laptop X", category: "laptops", price: 1200, attrs: { ram: 16, cpu: "M4" } }
{ name: "Shirt Y", category: "apparel", price: 25, attrs: { size: "M", color: "blue" } }
```

**SQL**

```sql
CREATE TABLE products (id BIGINT PRIMARY KEY, name TEXT, category TEXT, price_cents INT, attrs JSONB);
CREATE INDEX ON products USING GIN (attrs jsonb_path_ops);
SELECT * FROM products WHERE category = 'laptops' AND attrs @> '{"ram": 16}';
```

**BigQuery, Snowflake**

`JSON` / `VARIANT` column for `attrs`, typed columns for shared fields.

**DynamoDB**

Store `attrs` as a map. Serve category pages by `pk = CATEGORY#laptops`; send faceted filtering to OpenSearch.

**Firebase**

`attrs` as a map; each `attrs.x` field is indexed automatically, but combinations need composite indexes for each filter combination.

**Elasticsearch**

```js
mappings: {
  properties: {
    attrs: {
      type: "flattened";
    }
  }
}
// or dynamic_templates mapping attrs.* strings to keyword so facets work per attribute
```

Elasticsearch is usually where the faceted catalog page lives, whatever the main database is.

## 361: How do you translate a chat app's data model?

**MongoDB**

```js
{
  (_id, conversationId, senderId, text, createdAt);
} // index { conversationId: 1, createdAt: -1 }
```

**SQL**

```sql
CREATE TABLE messages (id BIGSERIAL, conversation_id BIGINT, sender_id BIGINT, text TEXT, created_at TIMESTAMPTZ DEFAULT now());
CREATE INDEX ON messages (conversation_id, created_at DESC);
```

**Redis**

```js
await redis.xAdd(`chat:${convId}`, "*", { from: userId, text }); // recent messages + live delivery
```

**DynamoDB**

```js
{ pk: "CONV#c1", sk: "MSG#01JD5T8K...", senderId: "u1", text: "hi" } // ULID sort key = time order
```

**Firebase**

```js
firestore
  .collection(`conversations/${convId}/messages`)
  .orderBy("createdAt", "desc")
  .limit(50)
  .onSnapshot(render);
```

**Elasticsearch**

Index messages only for search across conversations.

Firestore gives live updates to clients for free. With DynamoDB or SQL, you add WebSockets and use Streams or pub/sub to fan out new messages.

## 362: How do you translate an IoT telemetry system?

- **Ingest:** devices send to MQTT or HTTP, then a queue (Kafka, Kinesis, Pub/Sub).
- **Hot data (last hours):** Redis TimeSeries or a time series database for live dashboards.
- **Recent data (days to months):** MongoDB time series collections, TimescaleDB, Elasticsearch TSDS, or DynamoDB with `pk = DEVICE#id#DAY`.
- **History and analytics:** BigQuery or Snowflake, partitioned by day and clustered by device.

```sql
-- BigQuery: hourly average per device for one day
SELECT device_id, TIMESTAMP_TRUNC(ts, HOUR) AS hour, AVG(temp) AS avg_temp
FROM iot.readings WHERE DATE(ts) = '2026-11-26'
GROUP BY device_id, hour;
```

A single MongoDB cluster can do all of these up to a point. When you translate, it is common to split by data age, because no one store is cheapest for hot, warm and cold data at the same time.

## 363: How do you translate an append-only audit log or event store?

**MongoDB**

```js
await db.collection("events").insertOne({
  streamId: "order-o1",
  version: 4,
  type: "OrderShipped",
  data,
  at: new Date(),
});
// unique index { streamId: 1, version: 1 } stops two writers adding version 4
```

**SQL**

```sql
CREATE TABLE events (stream_id TEXT, version INT, type TEXT, data JSONB, at TIMESTAMPTZ DEFAULT now(), PRIMARY KEY (stream_id, version));
REVOKE UPDATE, DELETE ON events FROM app; -- append only
```

**DynamoDB**

```js
new PutCommand({
  TableName: "Events",
  Item: { pk: "order-o1", sk: 4, type: "OrderShipped", data },
  ConditionExpression: "attribute_not_exists(sk)",
});
```

**Redis**

Streams work for short-term events, but don't use Redis as the permanent event store.

**BigQuery, Snowflake**

Load events for analysis; they are append-friendly but not the place to enforce ordering per stream.

**Elasticsearch**

A data stream is append-only by design and great for searching audit logs.

The primary key `(stream_id, version)` gives optimistic concurrency for free in SQL and DynamoDB, exactly like the unique index in MongoDB.

## 364: How do you protect tenants from each other (noisy neighbors) at scale?

- **MongoDB:** big tenants can get their own collections, databases or clusters; zone sharding can pin them.
- **SQL:** connection limits per role, `statement_timeout` per tenant role, and moving big tenants to their own database.
- **BigQuery:** separate reservations or projects for big tenants, and `maximumBytesBilled` per query.
- **Redis:** separate instances for big tenants; a single slow command blocks everyone on that node.
- **Snowflake:** separate warehouses per tenant group, so one tenant's heavy queries don't queue the others.
- **DynamoDB:** partition keys that start with tenant id, write sharding for very hot tenants, and per-tenant rate limits in the API.
- **Firebase:** per-tenant databases for large customers.
- **Elasticsearch:** index per large tenant, shared index with routing for small ones.

A common pattern everywhere: start pooled (shared tables with `tenant_id`), and move the few biggest tenants out to dedicated resources.

## 365: How do you translate a reporting dashboard built on MongoDB aggregations?

1. **List every chart** and the aggregation behind it.
2. **Copy data to a warehouse** (BigQuery or Snowflake) and translate each pipeline into SQL. `$match` to `WHERE`, `$group` to `GROUP BY`, `$lookup` to `JOIN`, `$unwind` to `UNNEST`/`FLATTEN`, `$setWindowFields` to window functions.
3. **Precompute** heavy charts into tables, materialized views or dynamic tables refreshed on a schedule.
4. **Connect a BI tool** (Looker Studio, Looker, Tableau, Power BI, Metabase) to the warehouse.
5. **For live operational counters**, keep a small set of Redis counters or Elasticsearch aggregations.

```sql
-- MongoDB: $match paid, $group by day, $sum total
SELECT DATE(created_at) AS day, SUM(total) AS revenue, COUNT(*) AS orders
FROM shop.orders WHERE status = 'paid' AND created_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY day ORDER BY day;
```

## 366: How do you translate a search page with filters, facets and sorting?

**MongoDB**

```js
[
  {
    $search: {
      compound: {
        must: [{ text: { query: q, path: "name" } }],
        filter: [{ equals: { path: "brand", value: "acme" } }],
      },
    },
  },
  {
    $facet: {
      items: [{ $skip: 0 }, { $limit: 20 }],
      brands: [{ $sortByCount: "$brand" }],
    },
  },
];
```

**Elasticsearch**

```js
await es.search({
  index: "products",
  query: {
    bool: {
      must: [{ match: { name: q } }],
      filter: [{ term: { brand: "acme" } }, { range: { price: { lte: 100 } } }],
    },
  },
  post_filter: { term: { color: "red" } }, // filters hits but not facet counts
  aggs: {
    brands: { terms: { field: "brand" } },
    colors: { terms: { field: "color" } },
    price: { histogram: { field: "price", interval: 25 } },
  },
  sort: [{ _score: "desc" }, { price: "asc" }],
  from: 0,
  size: 20,
});
```

**Redis**

`FT.SEARCH` for the page plus one `FT.AGGREGATE` per facet.

**SQL**

Full-text with `tsvector`, filters in `WHERE`, and one `GROUP BY` query per facet. Fine for small catalogs.

`post_filter` is the key trick for good facets: the selected color filters the results, but the color facet still shows counts for other colors.

## 367: How do you translate a social feed: fan-out on write or on read?

- **Fan-out on read (pull):** at read time, get the people a user follows and query their recent posts. Easy in SQL (`JOIN follows`) and MongoDB (`$in` on author ids), costly when users follow thousands.
- **Fan-out on write (push):** when someone posts, write the post id into each follower's feed. Reads become one cheap query. Costly for users with millions of followers.

| Database | Usual choice                                                             |
| -------- | ------------------------------------------------------------------------ |
| MongoDB  | Pull for most, push into a `feeds` collection for active users           |
| SQL      | Pull with a join and an index on `(author_id, created_at)`               |
| Redis    | Push into a sorted set per user, trimmed to the latest 500               |
| DynamoDB | Push: `pk = FEED#user`, `sk = time#postId`, written by a Stream consumer |
| Firebase | Push into `users/{id}/feed` with a Cloud Function                        |

Most large systems mix both: push for normal users, pull for celebrity accounts, merged at read time.

## 368: How do you prevent double booking?

**MongoDB**

```js
await db
  .collection("bookings")
  .createIndex({ roomId: 1, date: 1 }, { unique: true });
await db
  .collection("bookings")
  .insertOne({ roomId: "r1", date: "2026-12-01", userId });
```

**SQL**

```sql
CREATE EXTENSION btree_gist;
CREATE TABLE bookings (
  room_id BIGINT, during TSTZRANGE,
  EXCLUDE USING gist (room_id WITH =, during WITH &&) -- no overlapping ranges per room
);
```

**Redis**

```js
await redis.set(`hold:r1:2026-12-01`, userId, { NX: true, EX: 600 }); // short hold during checkout
```

**DynamoDB**

```js
new PutCommand({
  TableName: "Bookings",
  Item: { pk: "ROOM#r1", sk: "DATE#2026-12-01", userId },
  ConditionExpression: "attribute_not_exists(pk)",
});
```

**Firebase**

```js
await firestore.doc("rooms/r1/bookings/2026-12-01").create({ userId });
```

For whole days or fixed slots, "one record per slot plus create-if-missing" works everywhere. For free-form time ranges, PostgreSQL's exclusion constraint is the only one that checks overlaps for you; elsewhere, lock per room in a transaction.

## 369: How do you decrement inventory without overselling?

**MongoDB**

```js
const res = await db
  .collection("products")
  .updateOne({ _id: "p1", stock: { $gte: qty } }, { $inc: { stock: -qty } });
if (res.modifiedCount === 0) throw new Error("Out of stock");
```

**SQL**

```sql
UPDATE products SET stock = stock - $1 WHERE id = $2 AND stock >= $1 RETURNING stock; -- 0 rows = out of stock
```

**Redis**

Use a Lua script that checks the stock and decrements it in one step (see question 259).

**DynamoDB**

```js
new UpdateCommand({
  TableName: "Products",
  Key: { id: "p1" },
  UpdateExpression: "SET stock = stock - :q",
  ConditionExpression: "stock >= :q",
  ExpressionAttributeValues: { ":q": qty },
});
```

**Firebase**

```js
await firestore.runTransaction(async (tx) => {
  const snap = await tx.get(ref);
  if (snap.get("stock") < qty) throw new Error("Out of stock");
  tx.update(ref, { stock: FieldValue.increment(-qty) });
});
```

The pattern is "conditional atomic update": the condition and the change happen in one operation. For flash sales, put the counter in Redis and write orders to the database asynchronously.

## 370: How do you translate a wallet or ledger balance?

**MongoDB**

```js
await session.withTransaction(async () => {
  await db
    .collection("ledger")
    .insertOne({ accountId: "a", amount: -100, ref: "t1" }, { session });
  await db
    .collection("accounts")
    .updateOne(
      { _id: "a", balance: { $gte: 100 } },
      { $inc: { balance: -100 } },
      { session },
    );
});
```

**SQL**

```sql
BEGIN;
INSERT INTO ledger (account_id, amount_cents, ref) VALUES ('a', -10000, 't1'), ('b', 10000, 't1');
UPDATE accounts SET balance_cents = balance_cents - 10000 WHERE id = 'a' AND balance_cents >= 10000;
UPDATE accounts SET balance_cents = balance_cents + 10000 WHERE id = 'b';
COMMIT;
```

**DynamoDB**

`TransactWriteItems` with two ledger `Put` items (condition `attribute_not_exists` for idempotency) and two balance `Update` items (condition `balance >= :amt` on the sender).

**Firebase**

`runTransaction` that reads both balances, checks, and writes ledger entries and new balances.

Keep the ledger as the source of truth (append-only, with a unique transfer reference), and the balance as a cached sum you can always rebuild. Use integer cents, never floats. Redis, BigQuery, Snowflake and Elasticsearch are not suitable as the system of record for money.

## 371: How do you translate "nearby" search at scale?

- **MongoDB:** `2dsphere` index with `$near` / `$geoNear`.
- **SQL:** PostGIS `geography` column, GiST index, `ST_DWithin` plus `<->` ordering.
- **BigQuery:** `ST_DWITHIN` with the table clustered on the geography column, for analytics.
- **Redis:** `GEOSEARCH` on a geo set, extremely fast for "drivers near me" with frequent position updates.
- **Snowflake:** `ST_DWITHIN`, with H3 functions (`H3_POINT_TO_CELL`) for grouping.
- **DynamoDB:** store a geohash or H3 cell as the partition key prefix; query the cell and its neighbors, then filter by real distance.
- **Firebase:** geohash queries with `geofire-common`, then filter by distance in code.
- **Elasticsearch:** `geo_distance` query and `_geo_distance` sort, with `geohash_grid` or `geotile_grid` aggregations for maps.

For moving objects (taxis, couriers), keep live positions in Redis and history in a database or warehouse.

## 372: How do you translate a GDPR delete (right to be forgotten)?

1. **Find every copy.** The main database, caches, search indices, warehouse tables, backups, logs, and third-party tools.
2. **Delete or anonymize** in each store:

```js
await db.collection("users").deleteOne({ _id: uid }); // MongoDB
await pool.query("DELETE FROM users WHERE id = $1", [uid]); // SQL (cascades)
await redis.del(`user:${uid}`, `sess:${uid}`); // Redis
await ddb.send(
  new DeleteCommand({
    TableName: "App",
    Key: { pk: `USER#${uid}`, sk: "PROFILE" },
  }),
); // DynamoDB (and every other item under the pk)
await firestore.recursiveDelete(firestore.doc(`users/${uid}`)); // Firebase
await es.deleteByQuery({ index: "*", query: { term: { userId: uid } } }); // Elasticsearch
```

```sql
DELETE FROM shop.events WHERE user_id = @uid;  -- BigQuery
DELETE FROM events WHERE user_id = :uid;       -- Snowflake
```

3. **Handle time travel and backups.** BigQuery and Snowflake keep deleted data for the time travel window; backups keep it until they expire. Document that retention.

A practical trick is crypto-shredding: encrypt each user's personal data with a per-user key and delete the key, which makes every copy unreadable at once.

## 373: How do you translate archiving old data (Atlas Online Archive)?

| Database      | Archive approach                                                                    |
| ------------- | ----------------------------------------------------------------------------------- |
| MongoDB       | Atlas Online Archive moves old documents to cheap storage, still queryable          |
| SQL           | Partition by month and detach or dump old partitions to object storage              |
| BigQuery      | Long-term storage pricing applies automatically to partitions untouched for 90 days |
| Redis         | TTL, plus writing to a database before expiry if you need history                   |
| Snowflake     | Storage is already cheap; drop or unload very old data to a stage                   |
| DynamoDB      | TTL + Streams + Lambda writes expired items to S3, queried with Athena              |
| Firebase      | Scheduled export to Cloud Storage or BigQuery, then delete                          |
| Elasticsearch | ILM moves indices to warm, cold and frozen tiers (searchable snapshots)             |

BigQuery's automatic long-term pricing means you often don't need to do anything; old partitions simply cost about half.

## 374: How do you replace $out-based ETL jobs with ELT in a warehouse?

MongoDB teams often run nightly aggregation pipelines with `$out` or `$merge` to build report collections. In a warehouse, the same thing is usually done with dbt models:

```sql
-- models/daily_revenue.sql (dbt)
{{ config(materialized='incremental', unique_key='day') }}
SELECT DATE(created_at) AS day, SUM(total) AS revenue
FROM {{ ref('stg_orders') }}
WHERE status = 'paid'
{% if is_incremental() %}
  AND created_at >= (SELECT MAX(day) FROM {{ this }})
{% endif %}
GROUP BY 1
```

Benefits over `$out` jobs: models are version controlled, tested (`unique`, `not_null`), documented, and run in dependency order. Incremental models are like `$merge` with `whenMatched: "replace"`, processing only new data.

## 375: How do BigQuery JSON and Snowflake VARIANT compare for semi-structured data?

| Feature           | BigQuery `JSON`                                   | Snowflake `VARIANT`                   |
| ----------------- | ------------------------------------------------- | ------------------------------------- |
| Path access       | `payload.device.os`, `JSON_VALUE(payload, '$.x')` | `payload:device.os`, `payload['x']`   |
| Casting           | `STRING(payload.x)`, `INT64(payload.n)`           | `payload:x::STRING`, `payload:n::INT` |
| Arrays            | `JSON_QUERY_ARRAY` + `UNNEST`                     | `LATERAL FLATTEN`                     |
| Storage           | Columnar shredding of common paths                | Columnar storage of common paths      |
| Max size          | Row limit (100 MB)                                | 128 MB per value                      |
| Typed alternative | `STRUCT` / `ARRAY`                                | `OBJECT` / `ARRAY` / structured types |

Both let you load raw MongoDB documents first and decide the schema later. In both, pull the hot fields into typed columns once you know your queries, so partitioning, clustering and pruning work on them.

## 376: How do you handle schema changes from MongoDB in BigQuery and Snowflake?

New fields appear in MongoDB documents all the time without any migration. In a warehouse you need a plan:

**BigQuery**

```bash
bq load --source_format=NEWLINE_DELIMITED_JSON --schema_update_option=ALLOW_FIELD_ADDITION \
  --schema_update_option=ALLOW_FIELD_RELAXATION shop.orders gs://bucket/orders-*.json schema.json
```

```sql
ALTER TABLE shop.orders ADD COLUMN coupon STRING;
```

**Snowflake**

```sql
ALTER TABLE orders SET ENABLE_SCHEMA_EVOLUTION = TRUE; -- COPY with MATCH_BY_COLUMN_NAME adds new columns
```

Changing a column's type (string to number) is the hard case in both. Common approach: keep the raw document in `JSON`/`VARIANT` forever, and let the typed layer be rebuilt from raw whenever the rules change. That way MongoDB's freedom never breaks the pipeline.

## 377: How do you translate approximate distinct counts (HyperLogLog)?

**MongoDB**

```js
[
  { $group: { _id: null, users: { $addToSet: "$userId" } } },
  { $project: { n: { $size: "$users" } } },
]; // exact, heavy on memory
```

**SQL**

```sql
SELECT COUNT(DISTINCT user_id) FROM events; -- exact; the postgresql-hll extension adds HLL
```

**BigQuery**

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM shop.events;
```

**Redis**

```js
await redis.pfAdd("uniq:2026-11-26", userId);
await redis.pfCount("uniq:2026-11-26"); // about 0.81% error, 12 KB per counter
```

**Snowflake**

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM events;
```

**Elasticsearch**

```js
aggs: { users: { cardinality: { field: "userId", precision_threshold: 3000 } } }
```

For daily active users across billions of events, approximate counts are usually good enough and far cheaper. BigQuery's `HLL_COUNT.INIT` and Snowflake's `HLL_ACCUMULATE` also let you store sketches per day and merge them for weekly or monthly numbers.

## 378: How do you compute percentiles like p95?

**MongoDB**

```js
[
  {
    $group: {
      _id: "$route",
      p95: { $percentile: { input: "$ms", p: [0.95], method: "approximate" } },
    },
  },
];
```

**SQL**

```sql
SELECT route, percentile_cont(0.95) WITHIN GROUP (ORDER BY ms) AS p95 FROM requests GROUP BY route;
```

**BigQuery**

```sql
SELECT route, APPROX_QUANTILES(ms, 100)[OFFSET(95)] AS p95 FROM shop.requests GROUP BY route;
```

**Snowflake**

```sql
SELECT route, APPROX_PERCENTILE(ms, 0.95) AS p95 FROM requests GROUP BY route;
```

**Elasticsearch**

```js
aggs: { byRoute: { terms: { field: "route" }, aggs: { p95: { percentiles: { field: "ms", percents: [95] } } } } }
```

Redis TimeSeries has no percentile reducer across samples, so latency percentiles usually come from Elasticsearch, a warehouse or a metrics tool.

## 379: How do you split events into user sessions (sessionization)?

**MongoDB**

```js
[
  {
    $setWindowFields: {
      partitionBy: "$userId",
      sortBy: { at: 1 },
      output: { prev: { $shift: { output: "$at", by: -1 } } },
    },
  },
  {
    $set: {
      newSession: {
        $or: [
          { $eq: ["$prev", null] },
          { $gt: [{ $subtract: ["$at", "$prev"] }, 1800000] },
        ],
      },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
WITH marked AS (
  SELECT user_id, at,
    CASE WHEN LAG(at) OVER (PARTITION BY user_id ORDER BY at) IS NULL
           OR at > LAG(at) OVER (PARTITION BY user_id ORDER BY at) + INTERVAL '30 minutes'
         THEN 1 ELSE 0 END AS new_session
  FROM events
)
SELECT user_id, at,
  SUM(new_session) OVER (PARTITION BY user_id ORDER BY at) AS session_no
FROM marked;
```

In BigQuery write `TIMESTAMP_ADD(LAG(at) OVER (...), INTERVAL 30 MINUTE)`; in Snowflake `DATEADD(minute, 30, LAG(at) OVER (...))`. The trick is the same in all of them: mark where a gap starts, then a running sum turns the marks into session numbers.

## 380: How do you translate funnel analysis?

**MongoDB**

```js
[
  { $match: { type: { $in: ["view", "cart", "purchase"] } } },
  { $group: { _id: "$userId", steps: { $addToSet: "$type" } } },
  {
    $group: {
      _id: null,
      viewed: { $sum: { $cond: [{ $in: ["view", "$steps"] }, 1, 0] } },
      carted: { $sum: { $cond: [{ $in: ["cart", "$steps"] }, 1, 0] } },
    },
  },
];
```

**SQL, BigQuery, Snowflake**

```sql
WITH firsts AS (
  SELECT user_id,
    MIN(CASE WHEN type = 'view' THEN at END) AS viewed,
    MIN(CASE WHEN type = 'cart' THEN at END) AS carted,
    MIN(CASE WHEN type = 'purchase' THEN at END) AS bought
  FROM events GROUP BY user_id
)
SELECT COUNT(viewed) AS step1,
       COUNT(CASE WHEN carted > viewed THEN 1 END) AS step2,
       COUNT(CASE WHEN bought > carted AND carted > viewed THEN 1 END) AS step3
FROM firsts;
```

**Elasticsearch**

ES|QL or `filters` aggregations can count each step, but strict ordering per user is easier in SQL.

Snowflake also has `MATCH_RECOGNIZE` for pattern matching over ordered rows, which handles complex funnels in one query.

## 381: How do you translate retention cohorts?

**SQL, BigQuery, Snowflake**

```sql
WITH first_seen AS (
  SELECT user_id, DATE_TRUNC('week', MIN(at)) AS cohort FROM events GROUP BY user_id
),
activity AS (
  SELECT DISTINCT user_id, DATE_TRUNC('week', at) AS week FROM events
)
SELECT f.cohort,
       EXTRACT(DAY FROM a.week - f.cohort) / 7 AS week_number,   -- PostgreSQL date math; use DATE_DIFF / DATEDIFF elsewhere
       COUNT(DISTINCT a.user_id) AS users
FROM first_seen f JOIN activity a USING (user_id)
GROUP BY 1, 2 ORDER BY 1, 2;
```

In BigQuery use `DATE_TRUNC(DATE(at), WEEK)` and `DATE_DIFF(a.week, f.cohort, WEEK)`; in Snowflake `DATEDIFF(week, f.cohort, a.week)`. In MongoDB this takes two `$group` stages and a `$lookup`; it is one of the analyses that becomes much shorter in SQL.

## 382: How do you pivot rows into columns?

**MongoDB**

```js
[
  {
    $group: {
      _id: "$productId",
      q1: { $sum: { $cond: [{ $eq: ["$quarter", 1] }, "$sales", 0] } },
      q2: { $sum: { $cond: [{ $eq: ["$quarter", 2] }, "$sales", 0] } },
    },
  },
];
```

**SQL**

```sql
SELECT product_id,
  SUM(sales) FILTER (WHERE quarter = 1) AS q1,
  SUM(sales) FILTER (WHERE quarter = 2) AS q2
FROM sales GROUP BY product_id;
```

**BigQuery**

```sql
SELECT * FROM (SELECT product_id, quarter, sales FROM shop.sales)
PIVOT (SUM(sales) FOR quarter IN (1 AS q1, 2 AS q2, 3 AS q3, 4 AS q4));
```

**Snowflake**

```sql
SELECT * FROM sales PIVOT (SUM(sales) FOR quarter IN (1, 2, 3, 4)) AS p (product_id, q1, q2, q3, q4);
```

**Elasticsearch**

A `terms` aggregation on `productId` with a `filters` sub-aggregation per quarter; the client turns buckets into columns.

## 383: How do you keep only the latest record per key (dedupe)?

**MongoDB**

```js
[
  { $sort: { updatedAt: -1 } },
  { $group: { _id: "$userId", doc: { $first: "$$ROOT" } } },
  { $replaceRoot: { newRoot: "$doc" } },
];
```

**SQL**

```sql
SELECT DISTINCT ON (user_id) * FROM user_changes ORDER BY user_id, updated_at DESC;
```

**BigQuery, Snowflake**

```sql
SELECT * FROM user_changes
QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY updated_at DESC) = 1;
```

**Elasticsearch**

```js
await es.search({
  index: "user_changes",
  collapse: { field: "userId" },
  sort: [{ updatedAt: "desc" }],
});
```

This is the most common query in CDC pipelines, because change tables hold every version and reports want the latest one.

## 384: How do you find streaks or gaps (gaps and islands)?

**SQL, BigQuery, Snowflake**

```sql
-- consecutive login days per user
WITH d AS (
  SELECT DISTINCT user_id, DATE(at) AS day FROM logins
),
g AS (
  SELECT user_id, day,
    DATE_SUB(day, INTERVAL CAST(ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) AS INT64) DAY) AS grp -- BigQuery
  FROM d
)
SELECT user_id, MIN(day) AS start_day, MAX(day) AS end_day, COUNT(*) AS streak
FROM g GROUP BY user_id, grp ORDER BY streak DESC;
```

In PostgreSQL write `day - ROW_NUMBER() OVER (...)::int`, and in Snowflake `DATEADD(day, -ROW_NUMBER() OVER (...), day)`. Consecutive days minus their row number give the same value, so grouping by it finds each streak.

In MongoDB the same thing needs `$setWindowFields` with `$documentNumber` and date math, which works but is harder to read. Redis bitmaps (`SETBIT` per day, `BITPOS`/`BITCOUNT`) are a fast way to track daily activity streaks live.

## 385: What are your options for joins in Elasticsearch?

1. **Denormalize** (most common): copy the needed fields into each document at index time.
2. **`nested`** for arrays of objects inside a document.
3. **`join` field** (parent/child) in one index, queried with `has_child` / `has_parent`. Parents and children must be on the same shard (use `routing`). Slower than nested, but children can be updated alone.
4. **ES|QL `LOOKUP JOIN`** with a lookup-mode index for enrichment.
5. **Enrich processor** at ingest time copies fields from a lookup index into incoming documents.
6. **Application-side join:** search one index, then `mget` related documents.

```js
await es.search({
  index: "qa",
  query: { has_child: { type: "answer", query: { term: { accepted: true } } } },
});
```

Coming from MongoDB `$lookup`, start with denormalization and only reach for `join` fields when copies would change too often to keep in sync.

## 386: How do you decide what to denormalize when there are no joins (DynamoDB, Firestore)?

Copy a field into another record when:

- the screen that reads the record always needs it,
- it rarely changes (names, titles, avatars), and
- showing a slightly old value for a moment is acceptable.

Don't copy when:

- it changes often (stock, balances, online status),
- it must always be exact, or
- one change would rewrite thousands of records (a category name copied into a million products).

For fields you don't copy, do a batch read of the related ids (`BatchGetItem`, `getAll`). Write down every copy and the trigger that keeps it updated, or they drift over time.

## 387: How do you keep references valid without foreign keys?

MongoDB does not enforce references, and neither do DynamoDB, Firestore, Redis or Elasticsearch. BigQuery and Snowflake let you declare keys but don't enforce them. Only SQL checks them.

**SQL**

```sql
ALTER TABLE orders ADD CONSTRAINT orders_user_fk FOREIGN KEY (user_id) REFERENCES users(id);
```

**DynamoDB**

```js
// check the parent exists in the same transaction as the child write
new TransactWriteCommand({
  TransactItems: [
    {
      ConditionCheck: {
        TableName: "App",
        Key: { pk: "USER#u1", sk: "PROFILE" },
        ConditionExpression: "attribute_exists(pk)",
      },
    },
    { Put: { TableName: "App", Item: { pk: "USER#u1", sk: "ORDER#o9" } } },
  ],
});
```

**Firebase**

```js
allow create: if exists(/databases/$(database)/documents/users/$(request.resource.data.userId));
```

Elsewhere, run a periodic job that finds orphans (children whose parent is missing), like a `LEFT JOIN ... WHERE parent IS NULL` query in the warehouse. When migrating from MongoDB to SQL, expect the foreign keys to fail at first on old orphan data; clean it before adding constraints.

## 388: How do you translate cascade deletes?

**MongoDB**

```js
await session.withTransaction(async () => {
  await db.collection("comments").deleteMany({ postId }, { session });
  await db.collection("posts").deleteOne({ _id: postId }, { session });
});
```

**SQL**

```sql
ALTER TABLE comments ADD FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE;
DELETE FROM posts WHERE id = 1; -- comments go too
```

**Redis**

Keep related keys under a common prefix and delete them together, or set the same TTL on all of them.

**DynamoDB**

Query every item under `pk = POST#p1` and batch delete them. For very large sets, delete in a background job driven by the Stream.

**Firebase**

```js
await firestore.recursiveDelete(firestore.doc("posts/p1")); // includes subcollections
```

**Elasticsearch**

`_delete_by_query` on `postId`.

Big cascades should run in the background in every database, so one user action does not lock or slow everything.

## 389: How does sorting on array fields differ between MongoDB and the others?

When you sort MongoDB documents by an array field, ascending order uses the **smallest** element and descending uses the **largest**. Few people know this, and code can depend on it.

- **SQL:** arrays compare element by element (`{1,5} < {2}`). To match MongoDB, sort by `(SELECT min(x) FROM unnest(arr) x)`.
- **BigQuery:** you cannot `ORDER BY` an array. Sort by `(SELECT MIN(x) FROM UNNEST(arr) x)`.
- **Snowflake:** sort by `ARRAY_MIN(arr)` / `ARRAY_MAX(arr)`.
- **Elasticsearch:** set `mode` on the sort: `sort: [{ prices: { order: "asc", mode: "min" } }]` (the default is min for asc and max for desc, the same as MongoDB).
- **DynamoDB, Firestore:** you cannot sort by an array. Store the min or max as its own field.

## 390: How do you configure Elasticsearch text analysis for multiple languages?

MongoDB `$text` indexes take a `default_language` and a per-document `language` field. In Elasticsearch you choose analyzers per field:

```js
await es.indices.create({
  index: "articles",
  mappings: {
    properties: {
      title: {
        type: "text",
        analyzer: "standard",
        fields: { en: { type: "text", analyzer: "english" }, de: { type: "text", analyzer: "german" } },
      },
    },
  },
});
// search the fields that match the user's language
query: { multi_match: { query: "running shoes", fields: ["title", "title.en"] } }
```

Other options: one index per language, or a field per language (`title_en`, `title_ka`). For languages without a built-in analyzer (like Georgian), use `standard` plus custom stop words, or an ICU plugin. PostgreSQL uses text search configurations (`to_tsvector('german', ...)`), and Redis sets `LANGUAGE` on the index or per document.

## 391: How do you translate search synonyms?

**MongoDB (Atlas Search)**

A synonym mapping points to a collection of `{ mappingType: "equivalent", synonyms: ["tv", "television"] }` documents.

**SQL**

A thesaurus or synonym dictionary in a text search configuration. It needs a file on the server, so it is awkward on managed databases.

**Redis**

```js
await redis.ft.synUpdate("idx:products", "grp1", ["tv", "television"]);
```

**Elasticsearch**

```js
await es.synonyms.putSynonym({
  id: "products",
  synonyms_set: [{ synonyms: "tv, television" }],
});
// analyzer: { type: "custom", tokenizer: "standard", filter: ["lowercase", { type: "synonym_graph", synonyms_set: "products", updateable: true }] }
```

Use synonyms at search time (not index time), so you can change them without reindexing. Elasticsearch's synonyms API reloads search analyzers automatically.

## 392: How do you make search ignore accents (café matches cafe)?

**MongoDB**

Collation `strength: 1` ignores accents and case for comparisons; Atlas Search uses the `lucene.standard` analyzer with an ASCII folding filter.

**SQL**

```sql
CREATE EXTENSION unaccent;
SELECT * FROM places WHERE unaccent(lower(name)) = unaccent(lower('Café'));
```

**BigQuery**

```sql
SELECT * FROM shop.places WHERE COLLATE(name, 'und:ci') = 'cafe'; -- or NORMALIZE then strip marks with REGEXP_REPLACE
```

**Redis**

TEXT fields fold accents for many Latin languages by default; TAG fields don't, so normalize before storing.

**Snowflake**

```sql
SELECT * FROM places WHERE COLLATE(name, 'en-ci-ai') = 'cafe';
```

**Elasticsearch**

```js
analyzer: { folded: { tokenizer: "standard", filter: ["lowercase", "asciifolding"] } }
```

**DynamoDB, Firebase**

Store a normalized copy (`name.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase()`) and query that.

## 393: How do you stream rows into BigQuery?

**MongoDB**

```js
await db.collection("events").insertOne(event); // immediately queryable
```

**BigQuery**

```js
// simple streaming insert (legacy insertAll API)
await bigquery
  .dataset("shop")
  .table("events")
  .insert([{ id: "e1", type: "click", ts: new Date().toISOString() }]);
```

For high volume, use the Storage Write API through `@google-cloud/bigquery-storage` (its `managedwriter` module).

The Storage Write API is cheaper than the legacy `insertAll`, and rows are available for queries within seconds. Its default stream gives at-least-once delivery; use a committed-type stream with offsets for exactly-once. `table.insert()` is fine for small, low-volume cases.

## 394: How do you stream rows into Snowflake?

- **Snowpipe:** files land in a stage (S3, GCS, Azure) and are loaded automatically within about a minute. Good for micro-batches.
- **Snowpipe Streaming:** rows are sent over channels with low latency (seconds), without files. Used by the Kafka connector and client SDKs.
- **Plain `INSERT`:** works but is slow and costly for many small writes; batch rows instead.

```sql
CREATE PIPE orders_pipe AUTO_INGEST = TRUE AS
COPY INTO raw_orders FROM @mongo_stage/orders/ FILE_FORMAT = (TYPE = JSON);
```

Coming from MongoDB, where each insert is instantly visible, plan for a few seconds to a minute of delay in Snowflake, and design dashboards around that.

## 395: How do you run analytics on DynamoDB data?

DynamoDB has no `GROUP BY`. Options:

1. **Export to S3** (`ExportTableToPointInTime`, full or incremental) and query with Athena, or load into Snowflake or BigQuery.
2. **Zero-ETL integrations** to Amazon Redshift or OpenSearch.
3. **Streams + Lambda** to keep aggregate items updated in real time (counts per day, totals per user).
4. **Kinesis Data Streams for DynamoDB** into Firehose, landing in S3 or a warehouse.

```bash
aws dynamodb export-table-to-point-in-time --table-arn "$ARN" --s3-bucket analytics-bucket \
  --export-format ION --export-type INCREMENTAL_EXPORT \
  --incremental-export-specification ExportFromTime=1764115200,ExportToTime=1764201600
```

Exports read from the PITR backup, so they don't use table capacity. A MongoDB aggregation that ran on the live database becomes an offline job here.

## 396: How do you get Firestore data into BigQuery?

1. **"Stream Firestore to BigQuery" extension:** writes every change to a raw changelog table and creates a "latest" view.
2. **Scheduled exports** (`gcloud firestore export`) loaded into BigQuery as tables.
3. **Your own Cloud Function** that writes changes with the Storage Write API.

```sql
-- the extension's latest view, then normal SQL
SELECT JSON_VALUE(data, '$.status') AS status, COUNT(*) FROM `proj.firestore_export.orders_raw_latest` GROUP BY status;
```

This is how Firebase apps answer the questions MongoDB answered with `$group`: reporting moves to BigQuery, and the app reads only precomputed counts from Firestore.

## 397: What Firestore limits catch people coming from MongoDB?

| Limit                              | Value                                     |
| ---------------------------------- | ----------------------------------------- |
| Document size                      | 1 MiB                                     |
| Sustained writes to one document   | About 1 per second (soft)                 |
| Writes per batch or transaction    | 500                                       |
| `in` / `array-contains-any` values | 30                                        |
| `not-in` values                    | 10                                        |
| `array-contains` per query         | 1                                         |
| Composite indexes per database     | 200 (without billing), 1,000 with billing |
| Index entries per document         | 40,000                                    |
| Max depth of subcollections        | 100                                       |
| Transaction time limit             | 270 seconds                               |

Plus behavior differences: no joins, no full-text search, no `$regex`, no ad hoc `GROUP BY`, queries need an index for every filter combination, and you pay per document read.

## 398: How do large arrays and maps affect Firestore indexes?

Firestore indexes every field automatically, including every array element and every key in every map. A document with a 5,000-element array or a map with 10,000 keys creates thousands of index entries:

- writes get slower and more expensive,
- you can hit the 40,000 index entries per document limit,
- and the 1 MiB document limit comes sooner than you expect.

```json
{
  "fieldOverrides": [
    {
      "collectionGroup": "products",
      "fieldPath": "rawSpecs",
      "indexes": []
    }
  ]
}
```

Exempt fields you never query (`indexes: []` in `firestore.indexes.json`). MongoDB indexes only the fields you choose, so this default surprises people.

## 399: What is the 10 GB item collection limit in DynamoDB?

If a table has a local secondary index (LSI), all items with the same partition key (an "item collection"), plus their LSI copies, must stay under 10 GB. Writes fail with `ItemCollectionSizeLimitExceededException` when it is reached.

- Tables without LSIs have no such limit; a partition key value can grow without bound (it is split across partitions by sort key).
- Prefer GSIs over LSIs unless you need strongly consistent reads on the alternate sort key.
- If one key can grow huge (a busy tenant or device), add a bucket to the partition key (`TENANT#t1#2026-11`).

MongoDB has a similar idea with "jumbo chunks" when too many documents share one shard key value.

## 400: How do DynamoDB partitions, burst and adaptive capacity work?

- Each physical partition handles up to about **3,000 read units** and **1,000 write units** per second and stores about 10 GB.
- **Burst capacity** keeps up to 5 minutes of unused capacity to absorb short spikes (provisioned mode).
- **Adaptive capacity** shifts throughput to hot partitions automatically and can split a partition by sort key ranges for heavily used items ("split for heat").
- **On-demand mode** can instantly handle up to double the previous peak traffic; beyond that it scales up over time.

So DynamoDB handles uneven traffic better than its reputation, but one partition key value can still never exceed one partition's limits. A single hot item (like a global counter) is capped at 1,000 writes per second no matter what, which is where write sharding comes in.

## 401: How do DynamoDB global tables handle write conflicts?

With global tables, every replica region accepts writes and changes replicate to the others, usually within about a second. If the same item is written in two regions at nearly the same time, **last writer wins** based on a timestamp, and the other write is silently lost. DynamoDB also offers a multi-region strong consistency mode for some region sets, at the cost of higher write latency.

How to design for it:

- Route each user or tenant to a home region for writes, and use other regions for reads and failover.
- Avoid read-modify-write across regions. `ADD` on a counter in two regions at once can lose one increment.
- Conditional writes and transactions are only checked in the region where they run.

MongoDB global clusters avoid this by having one primary per shard zone, so a document is only ever written in one place.

## 402: How do you partition large tables in PostgreSQL?

**MongoDB**

Sharding by range on `createdAt`, or a TTL to keep collections small.

**SQL**

```sql
CREATE TABLE events (id BIGINT, user_id BIGINT, created_at TIMESTAMPTZ NOT NULL, data JSONB)
PARTITION BY RANGE (created_at);

CREATE TABLE events_2026_11 PARTITION OF events FOR VALUES FROM ('2026-11-01') TO ('2026-12-01');
CREATE TABLE events_2026_12 PARTITION OF events FOR VALUES FROM ('2026-12-01') TO ('2027-01-01');

-- dropping a month is instant, unlike DELETE
ALTER TABLE events DETACH PARTITION events_2026_11;
DROP TABLE events_2026_11;
```

Partitioning in PostgreSQL is on one server; it helps with pruning and cheap deletes, not with spreading load across machines. `pg_partman` creates future partitions automatically.

## 403: How does PostgreSQL MVCC compare to MongoDB's WiredTiger, and why does VACUUM matter?

Both keep multiple versions of data so readers don't block writers. The difference is cleanup:

- **WiredTiger** keeps old versions in its cache and history store and cleans them up itself.
- **PostgreSQL** writes a new row version on every `UPDATE` and leaves the old one in the table. `VACUUM` (usually autovacuum) later marks the space reusable.

What this means after a migration:

- Hot rows updated thousands of times per second create "bloat" if autovacuum can't keep up.
- Long-running transactions stop vacuum from removing old versions anywhere in the database.
- Tune autovacuum per table for very busy tables, and design high-frequency counters as inserts or as Redis counters.

```sql
ALTER TABLE counters SET (autovacuum_vacuum_scale_factor = 0.01, fillfactor = 80);
SELECT relname, n_dead_tup, last_autovacuum FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10;
```

## 404: How do you lock a row while you read and update it?

**MongoDB**

```js
// a write in a transaction locks the document; read-then-write needs the update to be in the transaction
await session.withTransaction(async () => {
  const acc = await db
    .collection("accounts")
    .findOneAndUpdate(
      { _id: "a" },
      { $set: { lock: new ObjectId() } },
      { session },
    );
  // ... now safe to compute and write
});
```

**SQL**

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 'a' FOR UPDATE; -- others wait here
UPDATE accounts SET balance = balance - 100 WHERE id = 'a';
COMMIT;
```

**Snowflake**

DML takes table or partition-level locks; there is no `SELECT ... FOR UPDATE`. Do the check inside the `UPDATE ... WHERE`.

**DynamoDB, Firebase, Redis**

No row locks for app code. Use conditional writes (DynamoDB), transactions (Firestore server SDK uses locks for you) or `WATCH` (Redis).

A MongoDB trick to "lock" a document in a transaction is to write a dummy field first. In SQL, `FOR UPDATE` does this directly.

## 405: Why do deadlocks show up after moving to SQL, and how do you avoid them?

MongoDB transactions usually fail fast with a write conflict and retry. PostgreSQL makes transactions wait for locks, so two transactions that lock rows in opposite order wait for each other until PostgreSQL kills one with a deadlock error (`40P01`).

```sql
-- T1: UPDATE accounts ... WHERE id = 'a'; then UPDATE ... WHERE id = 'b';
-- T2: UPDATE accounts ... WHERE id = 'b'; then UPDATE ... WHERE id = 'a';  -> deadlock
```

How to avoid them:

- Always lock rows in the same order (for example by id).
- Keep transactions short; don't call external APIs inside them.
- Use one statement where possible: `UPDATE accounts SET ... WHERE id IN ('a', 'b')` still locks in scan order, so sort ids first.
- Retry on `40P01` and `40001`, like you retry write conflicts in MongoDB.

Snowflake can also deadlock on concurrent DML to the same table, and DynamoDB transactions return `TransactionConflict` instead of waiting.

## 406: How do connection limits differ, and when do you need a pooler?

MongoDB handles thousands of connections fairly well. PostgreSQL uses one process per connection, so a few hundred connections already cost a lot of memory, and `max_connections` is often 100 to 500 on managed services.

| Need                               | Solution                                            |
| ---------------------------------- | --------------------------------------------------- |
| Many app instances                 | Small pool per instance (`max: 5-10`)               |
| Serverless or thousands of clients | PgBouncer in transaction mode, RDS Proxy, Supavisor |
| Edge runtimes                      | HTTP-based drivers (Neon, Supabase, Data API)       |

In transaction pooling mode, session features (`SET`, advisory locks held across transactions, `LISTEN`, some prepared statement setups) don't work as expected. Redis has a high limit (10,000 clients by default), and BigQuery, Snowflake, DynamoDB and Firestore are HTTP APIs, so pooling matters mostly for PostgreSQL.

## 407: How do you handle replica lag when reading from replicas?

**MongoDB**

`readPreference: "secondaryPreferred"` with `maxStalenessSeconds: 90`, or causal sessions for read-your-writes.

**SQL**

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS lag; -- on the replica
```

Route reads that must be fresh (right after a write, or for money) to the primary, and the rest to replicas. Some apps store the time of the user's last write in their session and use the primary for a few seconds after it.

**Redis**

Replicas are asynchronous; `WAIT numreplicas timeout` blocks until replicas confirm a write.

**DynamoDB**

GSIs are like replicas: they lag behind the table (usually under a second).

**Elasticsearch**

Replica shards get writes synchronously, but visibility still depends on refresh.

## 408: How do you scale PostgreSQL horizontally like a sharded MongoDB cluster?

- **Read scaling:** read replicas behind a load balancer.
- **Vertical scaling:** bigger machines go a long way; many teams never need more.
- **Citus** (extension, also Azure Cosmos DB for PostgreSQL): distributed tables by a distribution column, much like a shard key.

```sql
SELECT create_distributed_table('orders', 'tenant_id');
SELECT create_reference_table('countries'); -- copied to every node
```

- **App-level sharding:** separate databases per tenant group with a routing table.
- **Distributed SQL:** CockroachDB, YugabyteDB, Spanner, Aurora DSQL speak a PostgreSQL-like dialect and shard automatically.

Joins and foreign keys across shards are limited in all of these, the same as `$lookup` across shards being costly in MongoDB. Co-locate tables by the same key (`tenant_id`) so most joins stay on one node.

## 409: How do storage and compression compare?

| Database      | Storage format                                   | Compression                                |
| ------------- | ------------------------------------------------ | ------------------------------------------ |
| MongoDB       | BSON documents in WiredTiger (row-like)          | Snappy by default, zstd or zlib optional   |
| SQL           | Rows in 8 KB pages, large values in TOAST        | TOAST compression (pglz or lz4)            |
| BigQuery      | Columnar (Capacitor)                             | Automatic, often 5-10x                     |
| Redis         | In-memory structures                             | Small encodings for small hashes and lists |
| Snowflake     | Columnar micro-partitions                        | Automatic                                  |
| DynamoDB      | Items on SSD, managed                            | None you control; size billed as stored    |
| Firebase      | Managed, billed by document and index size       | None you control                           |
| Elasticsearch | Lucene segments, `_source` plus inverted indexes | LZ4 by default, `best_compression` option  |

Field names are stored in every MongoDB document and every DynamoDB item, so long names cost space. In columnar warehouses, names are stored once per column.

## 410: When do you use Snowflake's search optimization service?

Snowflake has no B-tree indexes. Pruning by min/max works for ranges on sorted data, but a point lookup on a high-cardinality column (`WHERE email = 'a@b.com'`) may scan everything. Search optimization builds a background access path for such lookups:

```sql
ALTER TABLE users ADD SEARCH OPTIMIZATION ON EQUALITY(email), SUBSTRING(name);
ALTER TABLE events ADD SEARCH OPTIMIZATION ON EQUALITY(payload:device.id);
```

It helps equality, `IN`, substring/regex, geo and `VARIANT` path lookups. It costs storage and credits to maintain, so use it on large tables with frequent selective lookups. It is the closest Snowflake gets to a MongoDB single-field index.

## 411: How do BigQuery search indexes work?

```sql
CREATE SEARCH INDEX logs_idx ON shop.logs (ALL COLUMNS);

SELECT * FROM shop.logs WHERE SEARCH(logs, 'error-4231');
SELECT * FROM shop.logs WHERE request_id = 'r-77'; -- equality can also use the index
```

A search index stores tokens from string and JSON columns, so `SEARCH()` and some `=`, `IN`, `LIKE` and `STARTS_WITH` filters can skip most data. It is built for finding needles in huge log tables, not for relevance-ranked search like Atlas Search or Elasticsearch. BigQuery also has vector indexes for `VECTOR_SEARCH`.

## 412: How do BigQuery slots and Snowflake warehouses compare to MongoDB cluster tiers?

- **MongoDB:** you pick a cluster tier (CPU, RAM, disk). All queries share it, and you scale by moving up a tier or adding shards.
- **BigQuery:** compute is measured in **slots**. On-demand gives a large shared pool and bills by bytes scanned. With editions, you buy slot capacity (with autoscaling) and pay for slot-hours instead.
- **Snowflake:** compute is **virtual warehouses** (X-Small to 6X-Large), billed per second while running. Multi-cluster warehouses add clusters when many queries queue.

The big difference is isolation: in Snowflake you can give the BI team, the loaders and data science separate warehouses, so they never slow each other down. In MongoDB, a heavy report and the app share the same cluster unless you use analytics nodes.

## 413: Can Snowflake replace MongoDB for app workloads with hybrid tables?

Snowflake hybrid tables (Unistore) add row-based storage with enforced primary keys, unique and foreign key constraints, and indexes, aimed at fast single-row reads and writes.

```sql
CREATE HYBRID TABLE orders (
  id VARCHAR PRIMARY KEY,
  user_id VARCHAR NOT NULL,
  status VARCHAR,
  INDEX idx_user (user_id)
);
```

They are useful for small operational parts next to analytics (app state, config, workflow status) and for joining live data with warehouse data. They are not a drop-in replacement for a MongoDB cluster serving a busy public API: latency is higher than a dedicated OLTP database, and there are throughput quotas. Most teams still keep the app on MongoDB, PostgreSQL or DynamoDB and sync to Snowflake.

## 414: How do you share data with another team or company?

| Database      | Sharing option                                                                  |
| ------------- | ------------------------------------------------------------------------------- |
| MongoDB       | Separate read-only user, Atlas Data Federation, or exports                      |
| SQL           | Read-only roles, logical replication to their database                          |
| BigQuery      | Grant dataset access across projects, BigQuery sharing (Analytics Hub) listings |
| Redis         | Not designed for sharing; expose an API                                         |
| Snowflake     | Secure data sharing (no copy), listings on the Snowflake Marketplace            |
| DynamoDB      | IAM roles across accounts, or exports to S3                                     |
| Firebase      | Security rules for users; export to BigQuery for analysts                       |
| Elasticsearch | Cross-cluster search with limited roles                                         |

Snowflake shares and BigQuery cross-project access give live data with no copying and no pipelines, and the consumer pays for their own compute. That is very different from the export-and-send approach common with MongoDB.

## 415: How do you query data in place without loading it (federated queries)?

**MongoDB**

Atlas Data Federation queries S3 files and Atlas clusters with MQL.

**SQL**

```sql
CREATE EXTENSION postgres_fdw; -- or file_fdw, or the mongo_fdw extension to read MongoDB
```

**BigQuery**

```sql
CREATE EXTERNAL TABLE shop.raw_events OPTIONS (format = 'PARQUET', uris = ['gs://bucket/events/*.parquet']);
SELECT * FROM EXTERNAL_QUERY('my-conn', 'SELECT id, status FROM orders'); -- Cloud SQL / AlloyDB
```

**Snowflake**

```sql
CREATE EXTERNAL TABLE raw_events WITH LOCATION = @s3_stage/events/ FILE_FORMAT = (TYPE = PARQUET);
-- or Iceberg tables managed in your own storage
```

**Elasticsearch**

Cross-cluster search across clusters; searchable snapshots for old data in object storage.

Federated queries are slower than native tables and often cost more per query, so use them for exploration and rare queries, and load data for anything that runs often.

## 416: What are the risks of using Redis as the primary database instead of MongoDB?

- **Memory bound.** All data must fit in RAM (or use Redis on Flash / tiered storage in some offerings), which is expensive for large data sets.
- **Durability.** Even with AOF every second, a crash can lose recent writes, and failover can lose acknowledged writes because replication is asynchronous.
- **Querying.** The Query Engine covers a lot, but there are no joins, limited transactions and no ad hoc aggregations on non-indexed fields.
- **Operations.** Big keys, slow commands and `KEYS *` block the single main thread.
- **Backups.** Snapshots are point-in-time; there is no PITR like MongoDB Atlas or DynamoDB.

Redis works well as a primary store for data that is small, fast-changing and can be rebuilt (sessions, leaderboards, rate limits, real-time state). For orders, users and payments, keep a durable database as the source of truth.

## 417: How do you check "have we seen this before" cheaply (Bloom filters)?

**MongoDB**

```js
const seen = await db.collection("seenUrls").findOne({ _id: url }); // one indexed lookup per check
```

**Redis**

```js
await redis.bf.reserve("bf:urls", 0.001, 10_000_000); // 0.1% false positives
await redis.bf.add("bf:urls", url);
const maybeSeen = await redis.bf.exists("bf:urls", url); // false means definitely not seen
```

**BigQuery, Snowflake**

Use `APPROX_COUNT_DISTINCT` / HLL for counting; for membership, a `LEFT JOIN` against the seen table in batch jobs.

**Elasticsearch**

`terms` lookups against an index of seen values, mostly for batch use.

A Bloom filter never gives a false "no", only a rare false "yes". Use it in front of an expensive database lookup (has this username been taken, has this URL been crawled) so most checks never reach the database.

## 418: How does Redis client-side caching work?

```js
const redis = await createClient({
  RESP: 3,
  clientSideCache: { ttl: 0, maxEntries: 10000 },
}).connect();
await redis.get("config:features"); // first call hits Redis
await redis.get("config:features"); // served from local memory until Redis says it changed
```

With RESP3, Redis tracks which keys a client has read and sends an invalidation message when one changes, so the local copy is never stale for long. This gives near in-process speed for hot, rarely changing keys (feature flags, config, product data). MongoDB has nothing like it built in; you would combine an in-memory cache with change streams to invalidate it yourself.

## 419: How do you react to key expiry or changes in Redis (keyspace notifications)?

```js
await redis.configSet("notify-keyspace-events", "Ex"); // E = keyevent channel, x = expired events
const sub = redis.duplicate();
await sub.connect();
await sub.subscribe("__keyevent@0__:expired", (key) => {
  if (key.startsWith("hold:")) releaseSeat(key);
});
```

This is the Redis version of a MongoDB change stream, but much weaker: it is fire-and-forget pub/sub (missed if no subscriber is connected), it does not include the value, and expired events fire when Redis actually removes the key, which can be later than the TTL. For reliable processing, also run a periodic job that finds expired holds in the database.

## 420: What metrics do you watch for each database?

| Database      | Key metrics                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------- |
| MongoDB       | Operation latency, cache dirty/used %, replication lag, connections, queues, scanned/returned ratio |
| SQL           | Connections, transaction rate, slow queries, replication lag, cache hit ratio, dead tuples, locks   |
| BigQuery      | Bytes billed, slot usage, query queue time, failed jobs                                             |
| Redis         | Memory used, evicted keys, hit ratio, ops/sec, latency spikes, blocked clients                      |
| Snowflake     | Credits used per warehouse, queued queries, spilled bytes, failed tasks                             |
| DynamoDB      | Consumed vs provisioned capacity, throttled requests, latency, system errors, GSI lag               |
| Firebase      | Reads/writes/deletes per day, latency, rule denials, hot spot warnings                              |
| Elasticsearch | Cluster health, JVM heap, search and indexing latency, rejected threads, disk watermarks            |

The "scanned vs returned" idea from MongoDB carries over everywhere: DynamoDB `ScannedCount` vs `Count`, PostgreSQL rows removed by filter in `EXPLAIN ANALYZE`, and bytes scanned in BigQuery.

## 421: How do you load test a translated database layer?

1. **Replay real traffic.** Capture production query patterns (MongoDB profiler or app logs) and generate the same mix against the new database.
2. **Use realistic data volume and skew.** A test with 1,000 evenly spread users will not show the hot partitions you get with one big tenant.
3. **Test the limits that matter:** DynamoDB throttling per partition, Firestore per-document write rates, PostgreSQL connection counts, Redis memory, Elasticsearch indexing rate during searches.
4. **Watch tail latency** (p95, p99), not just averages.

```js
// k6 script hitting the API that now uses the new database
import http from "k6/http";
export const options = {
  scenarios: {
    steady: {
      executor: "constant-arrival-rate",
      rate: 500,
      timeUnit: "1s",
      duration: "10m",
      preAllocatedVUs: 200,
    },
  },
};
export default () =>
  http.get(`${__ENV.API}/orders?user=${Math.floor(Math.random() * 100000)}`);
```

Warm DynamoDB on-demand tables first (or pre-warm with warm throughput settings) before a big launch, because new tables start with lower capacity.

## 422: How do you define each database as infrastructure as code?

```hcl
# DynamoDB
resource "aws_dynamodb_table" "app" {
  name         = "App"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "pk"
  range_key    = "sk"

  attribute {
    name = "pk"
    type = "S"
  }
  attribute {
    name = "sk"
    type = "S"
  }
  point_in_time_recovery {
    enabled = true
  }
}

# BigQuery
resource "google_bigquery_dataset" "shop" {
  dataset_id = "shop"
  location   = "EU"
}

# Firestore
resource "google_firestore_database" "db" {
  name        = "(default)"
  location_id = "eur3"
  type        = "FIRESTORE_NATIVE"
}

# Snowflake
resource "snowflake_warehouse" "bi" {
  name           = "BI_WH"
  warehouse_size = "XSMALL"
  auto_suspend   = 60
}
```

| Database      | Terraform provider and resource                                                         |
| ------------- | --------------------------------------------------------------------------------------- |
| MongoDB Atlas | `mongodb/mongodbatlas`, `mongodbatlas_advanced_cluster`                                 |
| SQL           | `aws_db_instance`, `google_sql_database_instance`, plus `cyrilgdn/postgresql` for roles |
| BigQuery      | `google_bigquery_dataset`, `google_bigquery_table`                                      |
| Redis         | `aws_elasticache_replication_group`, `google_redis_instance`, Redis Cloud provider      |
| Snowflake     | `snowflakedb/snowflake`, warehouses, databases, roles, grants                           |
| DynamoDB      | `aws_dynamodb_table`                                                                    |
| Firebase      | `google_firestore_database`, `google_firestore_index`                                   |
| Elasticsearch | `elastic/ec` for Elastic Cloud, `elastic/elasticstack` for index templates and ILM      |

Table-level things like SQL schemas, Elasticsearch mappings and Firestore indexes usually live in app migrations or `firestore.indexes.json`, not in Terraform.

## 423: How do you run each database in CI?

```yaml
# GitHub Actions services
services:
  mongo: { image: "mongo:8", ports: ["27017:27017"] }
  postgres:
    {
      image: "postgres:17",
      env: { POSTGRES_PASSWORD: test },
      ports: ["5432:5432"],
    }
  redis: { image: "redis:8", ports: ["6379:6379"] }
  dynamodb: { image: "amazon/dynamodb-local", ports: ["8000:8000"] }
  elasticsearch:
    image: "docker.elastic.co/elasticsearch/elasticsearch:9.2.0"
    env: { discovery.type: single-node, xpack.security.enabled: "false" }
    ports: ["9200:9200"]
```

- **Firebase:** `npx firebase emulators:exec --only firestore "npm test"`.
- **BigQuery and Snowflake:** a dedicated CI project or database, with a unique dataset or schema per run (`ci_${GITHUB_RUN_ID}`) that is dropped afterwards. Snowflake zero-copy clones make this fast.

Seed each test with its own data (unique ids or tenant per test) so tests can run in parallel without cleaning the whole database between them.

## 424: How do you translate Mongoose discriminators into SQL?

**MongoDB (Mongoose)**

```js
const Event = mongoose.model(
  "Event",
  new mongoose.Schema({ at: Date }, { discriminatorKey: "kind" }),
);
const Click = Event.discriminator(
  "Click",
  new mongoose.Schema({ url: String }),
);
const Purchase = Event.discriminator(
  "Purchase",
  new mongoose.Schema({ amount: Number }),
);
```

**SQL: single table**

```sql
CREATE TABLE events (id BIGSERIAL PRIMARY KEY, kind TEXT NOT NULL, at TIMESTAMPTZ, url TEXT, amount NUMERIC,
  CHECK ((kind = 'Click' AND url IS NOT NULL) OR (kind = 'Purchase' AND amount IS NOT NULL)));
```

**SQL: table per type**

```sql
CREATE TABLE events (id BIGSERIAL PRIMARY KEY, kind TEXT NOT NULL, at TIMESTAMPTZ);
CREATE TABLE click_events (id BIGINT PRIMARY KEY REFERENCES events(id), url TEXT NOT NULL);
CREATE TABLE purchase_events (id BIGINT PRIMARY KEY REFERENCES events(id), amount NUMERIC NOT NULL);
```

**DynamoDB, Firebase, Elasticsearch**

Keep one collection or table with a `kind` field, like Mongoose does.

Single-table is simpler and fast for "all events" queries; table-per-type keeps constraints strict. With many types and many optional fields, a `kind` column plus a `JSONB` payload is a practical middle ground.

## 425: How do you delete millions of rows or documents without hurting the database?

**MongoDB**

```js
let n;
do {
  const ids = await db
    .collection("logs")
    .find({ at: { $lt: cutoff } }, { projection: { _id: 1 } })
    .limit(5000)
    .map((d) => d._id)
    .toArray();
  n = (await db.collection("logs").deleteMany({ _id: { $in: ids } }))
    .deletedCount;
  await new Promise((r) => setTimeout(r, 200));
} while (n > 0);
```

**SQL**

```sql
DELETE FROM logs WHERE id IN (SELECT id FROM logs WHERE at < now() - interval '90 days' LIMIT 5000); -- loop it
-- best: drop old partitions instead of deleting rows
```

**BigQuery, Snowflake**

A single `DELETE` is fine; it rewrites storage files and does not block readers. Better still, use partition expiration.

**DynamoDB**

TTL (free, in the background). For a one-off purge, a parallel scan plus `BatchWriteCommand` deletes, limited to a share of capacity.

**Redis**

`SCAN` with `UNLINK` in batches, never `KEYS` + `DEL`.

**Firebase**

`recursiveDelete` or `BulkWriter`, which throttles itself; or set a TTL policy.

**Elasticsearch**

Delete whole indices by time (ILM) instead of `_delete_by_query`, which is slow and leaves deleted documents to be merged away.

## 426: How do you update millions of records safely?

**MongoDB**

```js
await db
  .collection("users")
  .updateMany({ plan: "legacy" }, { $set: { plan: "basic" } }); // one call, but long and heavy on the oplog
```

**SQL**

```sql
-- batch by key range so locks and WAL stay small
UPDATE users SET plan = 'basic' WHERE plan = 'legacy' AND id BETWEEN 1 AND 50000;
-- next range... with a short pause between batches
```

**BigQuery, Snowflake**

One `UPDATE` is fine, or rebuild the table with `CREATE OR REPLACE TABLE ... AS SELECT` with the change applied, which is often faster.

**DynamoDB**

Parallel scan, then `UpdateCommand` per item with a condition (`plan = :legacy`) so a re-run is safe. Rate limit to a share of capacity.

**Firebase**

`BulkWriter` with its built-in throttling (500/50/5 ramp-up rule).

**Elasticsearch**

`_update_by_query` with `slices: "auto"` and `requests_per_second` to throttle, run as a task (`wait_for_completion: false`).

Batching keeps replicas from falling behind and keeps locks short. MongoDB `updateMany` on millions of documents has the same risk, so the advice applies there too.

## 427: How do you write a migration script that can stop and resume?

```js
// MongoDB -> PostgreSQL backfill, resumable by _id
let lastId = (await loadCheckpoint()) ?? null;
for (;;) {
  const batch = await db
    .collection("orders")
    .find(lastId ? { _id: { $gt: lastId } } : {})
    .sort({ _id: 1 })
    .limit(1000)
    .toArray();
  if (!batch.length) break;

  await pool.query(
    `INSERT INTO orders (id, user_id, total_cents, created_at)
     SELECT * FROM unnest($1::text[], $2::text[], $3::int[], $4::timestamptz[])
     ON CONFLICT (id) DO UPDATE SET total_cents = EXCLUDED.total_cents`,
    [
      batch.map((d) => String(d._id)),
      batch.map((d) => String(d.userId)),
      batch.map((d) => toCents(d.total)),
      batch.map((d) => d.createdAt),
    ],
  );

  lastId = batch.at(-1)._id;
  await saveCheckpoint(lastId);
}
```

The same rules apply for any target: walk the source in a stable order (`_id`), write idempotently (upsert on the same id), save a checkpoint after each batch, and log rows that fail validation instead of stopping the whole run.

## 428: What replaces migration tools like migrate-mongo?

| Database      | Common tools                                                                     |
| ------------- | -------------------------------------------------------------------------------- |
| MongoDB       | migrate-mongo, Mongock, scripts in the app                                       |
| SQL           | Prisma Migrate, Drizzle Kit, Knex, node-pg-migrate, Flyway, Liquibase            |
| BigQuery      | dbt, Dataform, Terraform for datasets and tables                                 |
| Redis         | Usually none; version key names (`v2:user:*`) and migrate lazily on read         |
| Snowflake     | schemachange, Flyway, dbt, Terraform                                             |
| DynamoDB      | Terraform/CDK for tables and GSIs; data changes are scripts                      |
| Firebase      | `firestore.indexes.json` and rules in the Firebase CLI; data changes are scripts |
| Elasticsearch | Index templates in code or Terraform; changes are reindex + alias switch         |

In SQL, schema migrations are mandatory and run before the new code. In DynamoDB, Firestore and Redis, a common approach is "lazy migration": code reads both old and new shapes and writes the new shape, plus a background job for the rest.

## 429: How do string sorting and comparison rules differ?

- **MongoDB:** binary comparison by default (`"Z" < "a"`), or a collation you set per index or query.
- **SQL (PostgreSQL):** follows the database collation (often `en_US.UTF-8`), so `"a" < "Z"` and results can differ between servers with different locale settings. Use `COLLATE "C"` for byte order.
- **BigQuery:** byte order by default; `COLLATE` with `und:ci` for case-insensitive.
- **Redis:** sorted sets sort strings by bytes (`ZRANGE ... BYLEX`).
- **Snowflake:** byte order unless a column or expression has a collation.
- **DynamoDB:** sort keys compare by UTF-8 bytes.
- **Firebase:** UTF-8 byte order.
- **Elasticsearch:** `keyword` fields sort by bytes; use an ICU collation keyword field for language-aware sorting.

Tests that compare sorted lists between MongoDB and PostgreSQL often fail only because of collation. Decide whether you want byte order or human order, and set it explicitly.

## 430: How do null and missing fields behave differently?

| Query        | MongoDB                           | SQL                               | DynamoDB                              | Firebase                     | Elasticsearch                    |
| ------------ | --------------------------------- | --------------------------------- | ------------------------------------- | ---------------------------- | -------------------------------- |
| `x == null`  | Matches null and missing          | Use `IS NULL`                     | `attribute_not_exists` or type `NULL` | Matches only explicit `null` | `must_not exists`                |
| `x != 5`     | Includes missing                  | Excludes NULL                     | Includes missing                      | Excludes missing             | `must_not term` includes missing |
| Sort by `x`  | Missing/null sort first ascending | NULLS LAST ascending (PostgreSQL) | n/a                                   | Missing docs are excluded    | Missing last by default          |
| Count of `x` | Counts docs                       | `COUNT(x)` skips NULL             | n/a                                   | n/a                          | `value_count` skips missing      |

Most translation bugs in filters come from this table. Write tests with records that have the field set, set to `null`, and missing.

## 431: How does matching on arrays differ?

In MongoDB, `{ tags: "a" }` matches if the array contains `"a"`, and `{ tags: ["a", "b"] }` matches only the exact array in that order. Other databases differ:

- **SQL:** `tags = ARRAY['a','b']` is exact match (order matters); `'a' = ANY(tags)` for contains; `@>` for "contains all".
- **BigQuery:** arrays can't be compared with `=`; use `'a' IN UNNEST(tags)` or compare `TO_JSON_STRING(tags)`.
- **Snowflake:** `ARRAY_CONTAINS`, or `tags = ARRAY_CONSTRUCT('a','b')` for exact.
- **DynamoDB:** `contains(tags, :a)`; equality compares the whole list.
- **Firebase:** `array-contains` for contains; `==` with an array is an exact match.
- **Elasticsearch:** a `term` query matches if any value equals it; there is no exact array match without a script or a stored joined string.

Also, MongoDB matches a query value against both the array and its elements, so `{ scores: { $gt: 5, $lt: 10 } }` can match with two different elements. Use `$elemMatch` in MongoDB and `EXISTS (... UNNEST ...)` in SQL to require one element for both conditions.

## 432: What happens when a field has mixed types?

MongoDB stores mixed types without complaint and compares across types using a fixed BSON order (null < numbers < strings < objects < arrays < ObjectId < booleans < dates...). So `{ age: { $gt: 30 } }` silently skips documents where `age` is `"35"`.

- **SQL, BigQuery, Snowflake typed columns:** the load fails or the cast fails. You must clean the data first. `VARIANT` and `JSON` columns keep mixed types, and comparisons need explicit casts (`TRY_TO_NUMBER`, `SAFE_CAST`).
- **DynamoDB:** mixed types are allowed, but a key attribute has one fixed type, and comparisons between `S` and `N` never match.
- **Firebase:** allowed; queries compare within a type, and ordering across types follows Firestore's type order.
- **Elasticsearch:** the first document sets the field type; later documents with a different type fail to index (or are ignored with `ignore_malformed`).
- **Redis:** hash values are all strings; JSON keeps types, and numeric indexes skip non-numbers.

Run a `$type` report on every field before migrating (see the schema drift question), so you find these cases early.

## 433: How do you keep 64-bit integers precise in JavaScript?

JavaScript numbers lose precision above `2^53 - 1` (9,007,199,254,740,991). MongoDB `Long`, SQL `BIGINT`, BigQuery `INT64`, Snowflake `NUMBER(38,0)` and DynamoDB `N` can all hold bigger values.

- **MongoDB:** `promoteLongs: false` or `useBigInt64: true` in the driver.
- **SQL (`pg`):** `BIGINT` comes back as a string by default. Parse with `BigInt` if needed: `pg.types.setTypeParser(20, BigInt)`.
- **BigQuery:** use `wrapIntegers: true` to get `BigQueryInt` objects.
- **Snowflake:** `jsTreatIntegerAsBigInt: true` connection option.
- **DynamoDB:** `unmarshallOptions: { wrapNumbers: true }` in the DocumentClient returns `NumberValue` objects as strings.
- **Firebase:** integers are 64-bit; the Node SDK can return `BigInt` with `useBigInt: true` in settings.
- **Elasticsearch:** `long` values above 2^53 lose precision in JSON parsing; store large ids as `keyword`.

Ids like Twitter-style snowflake ids are the usual victims. Store them as strings unless you do math with them.

## 434: How do date precision and time zones differ?

| Database      | Precision                                         | Time zone stored?                                                  |
| ------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| MongoDB       | Milliseconds                                      | No, always UTC                                                     |
| SQL           | Microseconds                                      | `TIMESTAMPTZ` stores UTC; `TIMESTAMP` has no zone (avoid it)       |
| BigQuery      | Microseconds                                      | `TIMESTAMP` is UTC; `DATETIME` has no zone                         |
| Redis         | Whatever you store                                | No date type                                                       |
| Snowflake     | Up to nanoseconds                                 | `TIMESTAMP_TZ` keeps offset, `_LTZ` uses session zone, `_NTZ` none |
| DynamoDB      | Whatever you store                                | No date type                                                       |
| Firebase      | Microseconds                                      | UTC                                                                |
| Elasticsearch | Milliseconds (`date`), nanoseconds (`date_nanos`) | UTC                                                                |

Two common bugs: comparing a microsecond timestamp from PostgreSQL with a millisecond JS `Date` (they never match exactly), and Snowflake `TIMESTAMP_NTZ` columns loaded from local times. Use UTC everywhere and the zone-aware type in each database.

## 435: How do case sensitivity defaults differ?

- **MongoDB:** values are case-sensitive; field names are case-sensitive.
- **SQL (PostgreSQL):** values are case-sensitive; unquoted identifiers are folded to **lowercase** (`createdAt` becomes `createdat` unless quoted). Use snake_case columns to avoid quoting.
- **BigQuery:** values case-sensitive; column names are case-insensitive; table names are case-sensitive.
- **Snowflake:** values case-sensitive; unquoted identifiers are folded to **UPPERCASE**. A JSON key `createdAt` in a `VARIANT` stays case-sensitive (`doc:createdAt`, not `doc:CREATEDAT`).
- **DynamoDB, Firebase, Redis:** everything is case-sensitive.
- **Elasticsearch:** `keyword` is case-sensitive unless you add a lowercase normalizer; `text` is lowercased by the analyzer.

Copying MongoDB camelCase field names into PostgreSQL or Snowflake without thinking leads to quoting everywhere. Convert to snake_case in the migration and map in the app (Prisma `@map`, Drizzle column names).

## 436: Where do nulls go when sorting?

- **MongoDB:** null and missing are the smallest values, so they come first ascending and last descending.
- **SQL (PostgreSQL):** nulls are treated as largest: last ascending, first descending. Change it with `NULLS FIRST` / `NULLS LAST`.
- **BigQuery:** nulls first ascending, last descending (like MongoDB). Supports `NULLS FIRST/LAST`.
- **Snowflake:** nulls last ascending, first descending by default (configurable with `DEFAULT_NULL_ORDERING`).
- **Firebase:** null sorts before other types, and documents without the field are left out of the results.
- **Elasticsearch:** missing values go last for both directions, unless you set `missing: "_first"`.

```sql
SELECT * FROM users ORDER BY last_login DESC NULLS LAST; -- PostgreSQL, to match a typical UI
```

If a paginated list changes order after migration, null ordering is the first thing to check.

## 437: What field names cause problems when translating?

MongoDB allows almost any field name, including spaces, dots (in recent versions), `$` prefixes and unicode.

- **SQL:** names with spaces, dashes or reserved words (`order`, `user`, `limit`) need quoting. Max 63 bytes in PostgreSQL.
- **BigQuery:** letters, numbers and underscores only for standard names (flexible column names allow more), max 300 characters, can't start with a number unless flexible names are on.
- **Snowflake:** quoted identifiers allow anything but make every query need quotes.
- **DynamoDB:** reserved words and names with dots need `ExpressionAttributeNames`.
- **Firebase:** names with dots or special characters need `FieldPath` (`new FieldPath("a.b")`).
- **Elasticsearch:** a dot in a field name means an object path (`a.b` is `{ a: { b } }`); names starting with `_` are reserved for metadata.
- **Redis JSON:** special characters need bracket notation in JSONPath (`$["a.b"]`).

Normalize names during the migration (snake_case, ASCII, no dots) and keep the mapping in one place.

## 438: How do concurrent upserts cause duplicates, and how do you stop them?

Two requests running `updateOne({ email }, ..., { upsert: true })` at the same moment can both find nothing and both insert. MongoDB only prevents this if there is a **unique index** on the filter field (then one insert fails and the driver can retry it as an update).

- **SQL:** `INSERT ... ON CONFLICT` needs a unique constraint too; with one, it is fully safe.
- **BigQuery, Snowflake:** concurrent `MERGE` statements on the same table can both insert the same key because keys are not enforced. Run merges from one job at a time and dedupe.
- **Redis:** single-threaded commands make `HSET` and `SET NX` safe.
- **DynamoDB:** the key is the identity, so two `PutItem` calls with the same key never create two items.
- **Firebase:** using the natural key as document id makes `set` with merge safe.
- **Elasticsearch:** same `_id` means one document; with auto ids you get duplicates.

The fix is always the same: make the natural key the real unique key in the target.

## 439: How do you translate queries that use the timestamp inside ObjectId?

**MongoDB**

```js
const since = ObjectId.createFromTime(
  Math.floor(Date.parse("2026-11-01") / 1000),
);
await db
  .collection("orders")
  .find({ _id: { $gte: since } })
  .toArray(); // "created since Nov 1"
const createdAt = doc._id.getTimestamp();
```

Other databases have no hidden timestamp in the id, so before migrating:

1. Add an explicit `created_at` column (or attribute) and backfill it from `_id.getTimestamp()`.
2. Rewrite every `_id` range query as a `created_at` range query.
3. Index `created_at` (SQL), use it as a sort key (DynamoDB), or partition on it (BigQuery, Snowflake).

```sql
SELECT * FROM orders WHERE created_at >= '2026-11-01';
```

If you keep ObjectId hex strings as ids, `to_timestamp(('x' || substr(id, 1, 8))::bit(32)::int)` in PostgreSQL can still extract the time, but an explicit column is much clearer.

## 440: Why does single-document atomicity break when you normalize?

In MongoDB, updating an order and its embedded items in one `updateOne` is atomic, without a transaction. Many apps rely on this without knowing it.

When the order becomes an `orders` row plus `order_items` rows in SQL, or several items in DynamoDB, the same change touches several records:

```sql
BEGIN;
UPDATE orders SET total_cents = 3000 WHERE id = 'o1';
DELETE FROM order_items WHERE order_id = 'o1' AND sku = 'B';
COMMIT;
```

```js
new TransactWriteCommand({
  TransactItems: [
    {
      Update: {
        TableName: "App",
        Key: { pk: "ORDER#o1", sk: "META" },
        UpdateExpression: "SET total = :t",
        ExpressionAttributeValues: { ":t": 3000 },
      },
    },
    { Delete: { TableName: "App", Key: { pk: "ORDER#o1", sk: "ITEM#B" } } },
  ],
});
```

Go through every multi-field `updateOne` and ask: after the translation, does this touch more than one row or item? If yes, wrap it in a transaction. In BigQuery, keeping the order nested (`ARRAY<STRUCT>`) keeps the update to one row.

## 441: How do you keep app code from depending on the database during the migration?

Put all database access behind a small repository interface, then have one implementation per database:

```js
// orders-repo.js
export const ordersRepo = {
  async getById(id) {},
  async listByUser(userId, { limit, cursor }) {},
  async create(order) {},
  async markPaid(id) {},
};

// mongo-orders-repo.js, pg-orders-repo.js, dynamo-orders-repo.js implement the same functions
const repo = flags.ordersOnPostgres ? pgOrdersRepo : mongoOrdersRepo;
```

Rules that make the switch easy:

- Repositories return plain objects with the same shape (string ids, `Date` objects, cents as numbers), never driver types like `ObjectId` or Firestore `Timestamp`.
- Method names describe business actions (`markPaid`), not queries (`updateOne`).
- Cursors are opaque strings, so MongoDB `_id`, SQL keyset values and DynamoDB `LastEvaluatedKey` all fit.

With this in place you can run both implementations side by side and compare results.

## 442: How do you plan a rollback if the new database has problems after cut-over?

- **Keep the old database up to date** after cut-over with reverse sync (CDC from the new database back to MongoDB) for a few weeks, or at least keep it read-only and know how far behind it is.
- **Switch with a flag**, not a deploy, so going back takes seconds.
- **Move in slices:** one collection, one feature or one tenant group at a time, so a rollback affects a small part.
- **Define rollback triggers** up front: error rate, p99 latency, data mismatch count.
- **Don't drop the old data** until the new system has run through at least one full business cycle (month end, peak sale).

The hardest rollback is after writes have gone only to the new database. That is why reverse sync, or a dual-write period in both directions, is worth the effort for critical data.

## 443: How do you check that translated queries return the same results (shadow testing)?

```js
async function getOrders(userId) {
  const primary = await mongoRepo.listByUser(userId, { limit: 20 });
  queueMicrotask(async () => {
    try {
      const shadow = await pgRepo.listByUser(userId, { limit: 20 });
      if (!sameResult(primary, shadow))
        log.warn(
          { userId, primary: ids(primary), shadow: ids(shadow) },
          "shadow mismatch",
        );
    } catch (err) {
      log.error(err, "shadow query failed");
    }
  });
  return primary; // users always get the old result
}
```

`sameResult` must normalize what is allowed to differ (id format, decimal format, order of tied rows). Watch the mismatch rate per endpoint; once it is near zero and explained, switch reads. Sample a percentage of traffic so the new database is not overloaded during the test.

## 444: How do you estimate the cost of the same workload in each database?

Start from numbers you can measure on MongoDB: data size, documents per second read and written, average document size, query patterns and peak traffic.

| Database      | What you pay for                                               |
| ------------- | -------------------------------------------------------------- |
| MongoDB Atlas | Cluster tier per hour, storage, backup, data transfer          |
| SQL (managed) | Instance per hour, storage and IOPS, replicas                  |
| BigQuery      | Bytes scanned (or slot-hours), storage (active and long-term)  |
| Redis         | Memory size of nodes per hour                                  |
| Snowflake     | Credits per warehouse-second, storage, serverless features     |
| DynamoDB      | Read and write units (per KB), storage, GSIs, backups, streams |
| Firebase      | Document reads, writes and deletes, storage, network           |
| Elasticsearch | Node size and count (or serverless usage), storage tiers       |

For DynamoDB and Firestore, multiply operations by item size and count every index write. For BigQuery, multiply queries per day by bytes scanned per query. The usual surprise: a design that is cheap on MongoDB (big documents read often, scans, counts) can be expensive in pay-per-operation databases, and cheap there after a redesign.

## 445: How do you choose the target database for a MongoDB workload?

| Workload in MongoDB                                       | Good target                             |
| --------------------------------------------------------- | --------------------------------------- |
| Relational data with many `$lookup`s and transactions     | PostgreSQL (SQL)                        |
| Huge scale, simple access by key, serverless on AWS       | DynamoDB                                |
| Mobile or web app with live sync, offline, client access  | Firebase (Firestore)                    |
| Reports and analytics over large history                  | BigQuery or Snowflake                   |
| Caching, sessions, counters, leaderboards, rate limits    | Redis                                   |
| Full-text search, filters, facets, logs                   | Elasticsearch                           |
| Flexible documents with ad hoc queries, at moderate scale | Keep MongoDB (or PostgreSQL with JSONB) |

Also weigh the team's skills, the cloud you are on, and the cost model. Often the answer is not one replacement but a split: the core data moves to one store and the special workloads (search, analytics, cache) move to the right specialized one.

## 446: When should you not move away from MongoDB?

- The data really is document-shaped, with varied structures per record, and the app reads whole documents.
- The team knows MongoDB well and the problems are fixable with indexes, schema patterns or a bigger cluster.
- Queries are ad hoc and change often, which would hurt in DynamoDB or Firestore.
- You need search, vector search and analytics nodes, and Atlas already provides them in one place.
- The migration cost (time, risk, retraining) is bigger than the benefit you can measure.

A good interview answer names the specific pain (cost, joins, consistency, scaling, ops) and shows how the target fixes it. "SQL is better" or "DynamoDB scales" without a measured problem is not a reason.

## 447: How would you design a polyglot setup using several of these databases together?

```text
           +----------------- writes -----------------+
           |                                           v
 API --> PostgreSQL or DynamoDB (source of truth) --> CDC (logical replication / Streams)
           |                                           |
           |                     +---------------------+----------------------+
           v                     v                     v                      v
        Redis cache       Elasticsearch          BigQuery or Snowflake     Firestore
   (sessions, counters)   (search, facets)       (reports, ML)             (live client sync)
```

Principles:

- **One source of truth** per piece of data; everything else is a copy that can be rebuilt.
- **Change data capture** feeds the copies, so writers don't need to know about them.
- **Idempotent consumers** with ids and versions, so replays and out-of-order events are safe.
- **Clear ownership:** reads that must be exact go to the source; others can use the copies.

This is the same idea as MongoDB plus Atlas Search plus a warehouse, just with each piece from a different vendor and more moving parts to monitor.

## 448: Scenario: how would you migrate a MongoDB e-commerce app with slow reports and slow search?

1. **Measure first.** Profiler and Atlas metrics show reports running big `$group` and `$lookup` pipelines on the primary, and search using `$regex` on product names.
2. **Search:** sync products to Elasticsearch with a change stream worker. The product page search, facets and autocomplete move there. MongoDB stays the source of truth.
3. **Reports:** stream orders, users and products to BigQuery (or Snowflake). Rebuild each report as SQL, partitioned by order date. Dashboards read the warehouse.
4. **Hot paths:** cart, sessions and "top sellers" move to Redis.
5. **Core data:** keep it in MongoDB if it works, or move orders and payments to PostgreSQL if the team needs stronger relational guarantees. Do this last and separately.
6. **Verify and cut over** each piece with shadow reads and a flag.

This order fixes the user-facing pain first with low risk, because search and analytics copies can be rebuilt at any time.

## 449: Scenario: how would you redesign a MongoDB-based mobile chat app for Firestore?

1. **Model:** `conversations/{id}` with members and `lastMessage`, and `conversations/{id}/messages/{id}` as a subcollection. A user's chat list is `where("members", "array-contains", uid).orderBy("lastMessageAt", "desc")`.
2. **Real time:** clients listen with `onSnapshot` on the open conversation and the chat list, replacing the WebSocket server that read MongoDB change streams.
3. **Security rules:** only members can read or write a conversation's messages.
4. **Fan-out:** a Cloud Function on new messages updates `lastMessage` and unread counts per member, and sends push notifications.
5. **Search:** sync messages to Elasticsearch or Typesense if users need to search history.
6. **Limits:** busy group chats can exceed the per-document write rate on the conversation document, so update `lastMessage` in a debounced way or shard unread counters.
7. **Analytics:** stream to BigQuery with the Firestore extension.

The big win is dropping the custom real-time server. The cost is designing around reads billed per document and having no server-side joins.

## 450: What are the most common mistakes when translating MongoDB to these databases?

1. **Copying the document model as-is** into DynamoDB or Firestore, then hitting size limits and missing access patterns.
2. **Translating every query one to one** instead of redesigning around how the target works (scans in DynamoDB, joins in Elasticsearch, row-by-row updates in BigQuery).
3. **Ignoring null vs missing** and mixed types, which silently changes query results.
4. **Forgetting hidden behavior:** ObjectId time ordering, single-document atomicity, array matching rules, `$ne` including missing fields.
5. **Using a warehouse as an app database**, or Redis as the only copy of important data.
6. **No plan for counts and aggregations** in DynamoDB and Firestore.
7. **No verification step**, so mismatches are found by users.
8. **Big-bang cut-over** instead of moving one piece at a time behind a flag with a rollback path.
9. **Underestimating cost models:** per-byte scanning in BigQuery, per-document reads in Firestore, per-KB writes in DynamoDB.
10. **Forgetting the copies:** caches, search indices and warehouses that also need updates, deletes and GDPR handling.
