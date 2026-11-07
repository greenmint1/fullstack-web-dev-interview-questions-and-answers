# DynamoDB Interview Questions and Answers

_Last updated: October 29, 2026_

450 Amazon DynamoDB interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target DynamoDB as it works in 2026: on-demand and provisioned capacity, transactions, Streams, global tables (including multi-Region strong consistency), multi-attribute keys in global secondary indexes, and the AWS SDK for JavaScript v3. Code examples use Node.js with the v3 SDK, plus a few AWS CLI and Python (boto3) examples.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is DynamoDB?](#1-what-is-dynamodb)
- [2: What are the main features of DynamoDB?](#2-what-are-the-main-features-of-dynamodb)
- [3: What does it mean that DynamoDB is serverless?](#3-what-does-it-mean-that-dynamodb-is-serverless)
- [4: What are tables, items and attributes?](#4-what-are-tables-items-and-attributes)
- [5: What types of primary keys does DynamoDB support?](#5-what-types-of-primary-keys-does-dynamodb-support)
- [6: What is a partition key?](#6-what-is-a-partition-key)
- [7: What is a sort key?](#7-what-is-a-sort-key)
- [8: Can you give an example of a composite primary key?](#8-can-you-give-an-example-of-a-composite-primary-key)
- [9: What data types does DynamoDB support?](#9-what-data-types-does-dynamodb-support)
- [10: What is the difference between a list and a map?](#10-what-is-the-difference-between-a-list-and-a-map)
- [11: What are sets in DynamoDB and how are they different from lists?](#11-what-are-sets-in-dynamodb-and-how-are-they-different-from-lists)
- [12: What is the maximum size of an item?](#12-what-is-the-maximum-size-of-an-item)
- [13: Is DynamoDB schemaless?](#13-is-dynamodb-schemaless)
- [14: How is DynamoDB different from a relational database?](#14-how-is-dynamodb-different-from-a-relational-database)
- [15: How is DynamoDB different from MongoDB?](#15-how-is-dynamodb-different-from-mongodb)
- [16: When is DynamoDB a good choice?](#16-when-is-dynamodb-a-good-choice)
- [17: When is DynamoDB not a good choice?](#17-when-is-dynamodb-not-a-good-choice)
- [18: How does DynamoDB keep data durable?](#18-how-does-dynamodb-keep-data-durable)
- [19: What is a partition in DynamoDB?](#19-what-is-a-partition-in-dynamodb)
- [20: What read consistency options does DynamoDB have?](#20-what-read-consistency-options-does-dynamodb-have)
- [21: When would you use a strongly consistent read?](#21-when-would-you-use-a-strongly-consistent-read)
- [22: What capacity modes does DynamoDB offer?](#22-what-capacity-modes-does-dynamodb-offer)
- [23: What is on-demand capacity mode?](#23-what-is-on-demand-capacity-mode)
- [24: What is provisioned capacity mode?](#24-what-is-provisioned-capacity-mode)
- [25: What is a read capacity unit (RCU)?](#25-what-is-a-read-capacity-unit-rcu)
- [26: What is a write capacity unit (WCU)?](#26-what-is-a-write-capacity-unit-wcu)
- [27: How do you calculate the capacity needed for a workload?](#27-how-do-you-calculate-the-capacity-needed-for-a-workload)
- [28: What is throttling?](#28-what-is-throttling)
- [29: How do you create a table with the AWS CLI?](#29-how-do-you-create-a-table-with-the-aws-cli)
- [30: How do you create a table with the AWS SDK for JavaScript v3?](#30-how-do-you-create-a-table-with-the-aws-sdk-for-javascript-v3)
- [31: How do you write an item with PutItem?](#31-how-do-you-write-an-item-with-putitem)
- [32: Does PutItem overwrite an existing item?](#32-does-putitem-overwrite-an-existing-item)
- [33: How do you read an item with GetItem?](#33-how-do-you-read-an-item-with-getitem)
- [34: How do you update an item with UpdateItem?](#34-how-do-you-update-an-item-with-updateitem)
- [35: How do you delete an item?](#35-how-do-you-delete-an-item)
- [36: What is a Query operation?](#36-what-is-a-query-operation)
- [37: What is a Scan operation?](#37-what-is-a-scan-operation)
- [38: What is the difference between Query and Scan?](#38-what-is-the-difference-between-query-and-scan)
- [39: What operators can you use in a KeyConditionExpression?](#39-what-operators-can-you-use-in-a-keyconditionexpression)
- [40: What is a FilterExpression?](#40-what-is-a-filterexpression)
- [41: What is a ProjectionExpression?](#41-what-is-a-projectionexpression)
- [42: What are ExpressionAttributeNames?](#42-what-are-expressionattributenames)
- [43: What are ExpressionAttributeValues?](#43-what-are-expressionattributevalues)
- [44: What are reserved words in DynamoDB?](#44-what-are-reserved-words-in-dynamodb)
- [45: What is a condition expression?](#45-what-is-a-condition-expression)
- [46: How do you prevent creating a duplicate item?](#46-how-do-you-prevent-creating-a-duplicate-item)
- [47: What clauses can an UpdateExpression have?](#47-what-clauses-can-an-updateexpression-have)
- [48: How does the SET clause work?](#48-how-does-the-set-clause-work)
- [49: How does the REMOVE clause work?](#49-how-does-the-remove-clause-work)
- [50: How does the ADD clause work?](#50-how-does-the-add-clause-work)
- [51: How does the DELETE clause in an UpdateExpression work?](#51-how-does-the-delete-clause-in-an-updateexpression-work)
- [52: What is an atomic counter?](#52-what-is-an-atomic-counter)
- [53: What does the ReturnValues parameter do?](#53-what-does-the-returnvalues-parameter-do)
- [54: What is a secondary index?](#54-what-is-a-secondary-index)
- [55: What is a global secondary index (GSI)?](#55-what-is-a-global-secondary-index-gsi)
- [56: What is a local secondary index (LSI)?](#56-what-is-a-local-secondary-index-lsi)
- [57: What is the difference between a GSI and an LSI?](#57-what-is-the-difference-between-a-gsi-and-an-lsi)
- [58: What are projected attributes in an index?](#58-what-are-projected-attributes-in-an-index)
- [59: How do you query a GSI?](#59-how-do-you-query-a-gsi)
- [60: What is BatchGetItem?](#60-what-is-batchgetitem)
- [61: What is BatchWriteItem?](#61-what-is-batchwriteitem)
- [62: What are UnprocessedItems and UnprocessedKeys?](#62-what-are-unprocesseditems-and-unprocessedkeys)
- [63: How does pagination work in DynamoDB?](#63-how-does-pagination-work-in-dynamodb)
- [64: What does the Limit parameter do?](#64-what-does-the-limit-parameter-do)
- [65: How do you sort Query results?](#65-how-do-you-sort-query-results)
- [66: How do you count items in DynamoDB?](#66-how-do-you-count-items-in-dynamodb)
- [67: What is Time to Live (TTL)?](#67-what-is-time-to-live-ttl)
- [68: How do you enable TTL on a table?](#68-how-do-you-enable-ttl-on-a-table)
- [69: What is DynamoDB Streams?](#69-what-is-dynamodb-streams)
- [70: What stream view types are there?](#70-what-stream-view-types-are-there)
- [71: Does DynamoDB support transactions?](#71-does-dynamodb-support-transactions)
- [72: How do you use TransactWriteItems?](#72-how-do-you-use-transactwriteitems)
- [73: How do you use TransactGetItems?](#73-how-do-you-use-transactgetitems)
- [74: What are on-demand backups?](#74-what-are-on-demand-backups)
- [75: What is point-in-time recovery (PITR)?](#75-what-is-point-in-time-recovery-pitr)
- [76: What are global tables?](#76-what-are-global-tables)
- [77: What is DAX?](#77-what-is-dax)
- [78: Is data in DynamoDB encrypted?](#78-is-data-in-dynamodb-encrypted)
- [79: How do you control who can access a DynamoDB table?](#79-how-do-you-control-who-can-access-a-dynamodb-table)
- [80: Which packages do you use for DynamoDB in the AWS SDK for JavaScript v3?](#80-which-packages-do-you-use-for-dynamodb-in-the-aws-sdk-for-javascript-v3)
- [81: What is the difference between the low-level client and the Document Client?](#81-what-is-the-difference-between-the-low-level-client-and-the-document-client)
- [82: What do marshall and unmarshall do?](#82-what-do-marshall-and-unmarshall-do)
- [83: What is the DynamoDB JSON format?](#83-what-is-the-dynamodb-json-format)
- [84: How do you use DynamoDB from Python?](#84-how-do-you-use-dynamodb-from-python)
- [85: What is DynamoDB Local?](#85-what-is-dynamodb-local)
- [86: What is NoSQL Workbench?](#86-what-is-nosql-workbench)
- [87: What is PartiQL in DynamoDB?](#87-what-is-partiql-in-dynamodb)
- [88: How do you run a PartiQL statement from code?](#88-how-do-you-run-a-partiql-statement-from-code)
- [89: What table classes are available?](#89-what-table-classes-are-available)
- [90: What is deletion protection?](#90-what-is-deletion-protection)
- [91: What statuses can a table have?](#91-what-statuses-can-a-table-have)
- [92: What are the naming rules for tables and attributes?](#92-what-are-the-naming-rules-for-tables-and-attributes)
- [93: Can you store empty strings in DynamoDB?](#93-can-you-store-empty-strings-in-dynamodb)
- [94: How does the Number type work?](#94-how-does-the-number-type-work)
- [95: When would you use the Binary type?](#95-when-would-you-use-the-binary-type)
- [96: How do you store dates and times?](#96-how-do-you-store-dates-and-times)
- [97: What is an item collection?](#97-what-is-an-item-collection)
- [98: What is a hot partition?](#98-what-is-a-hot-partition)
- [99: How do you choose a good partition key?](#99-how-do-you-choose-a-good-partition-key)
- [100: How do you use the sort key for range queries?](#100-how-do-you-use-the-sort-key-for-range-queries)
- [101: How do you store and query nested JSON documents?](#101-how-do-you-store-and-query-nested-json-documents)
- [102: How do you append items to a list?](#102-how-do-you-append-items-to-a-list)
- [103: What does if_not_exists do?](#103-what-does-if_not_exists-do)
- [104: How do you update an item only if it is in a certain state?](#104-how-do-you-update-an-item-only-if-it-is-in-a-certain-state)
- [105: What is ConditionalCheckFailedException?](#105-what-is-conditionalcheckfailedexception)
- [106: What are the common DynamoDB errors?](#106-what-are-the-common-dynamodb-errors)
- [107: How do the AWS SDKs handle retries?](#107-how-do-the-aws-sdks-handle-retries)
- [108: How is DynamoDB priced?](#108-how-is-dynamodb-priced)
- [109: Is there a free tier for DynamoDB?](#109-is-there-a-free-tier-for-dynamodb)
- [110: Which CloudWatch metrics are most useful for DynamoDB?](#110-which-cloudwatch-metrics-are-most-useful-for-dynamodb)
- [111: What is auto scaling in DynamoDB?](#111-what-is-auto-scaling-in-dynamodb)
- [112: Can you change the primary key of an existing table?](#112-can-you-change-the-primary-key-of-an-existing-table)
- [113: How do you delete all items in a table?](#113-how-do-you-delete-all-items-in-a-table)
- [114: How do you delete a table?](#114-how-do-you-delete-a-table)
- [115: What does DescribeTable return?](#115-what-does-describetable-return)
- [116: How do you list all tables?](#116-how-do-you-list-all-tables)
- [117: What can you change with UpdateTable?](#117-what-can-you-change-with-updatetable)
- [118: What happens if you call UpdateItem on an item that doesn't exist?](#118-what-happens-if-you-call-updateitem-on-an-item-that-doesnt-exist)
- [119: Can you query without the partition key?](#119-can-you-query-without-the-partition-key)
- [120: What happens to items that don't have a GSI's key attribute?](#120-what-happens-to-items-that-dont-have-a-gsis-key-attribute)
- [121: How many secondary indexes can a table have?](#121-how-many-secondary-indexes-can-a-table-have)
- [122: How do you see how much capacity a request used?](#122-how-do-you-see-how-much-capacity-a-request-used)
- [123: What affects DynamoDB latency?](#123-what-affects-dynamodb-latency)
- [124: What is the difference between the Dynamo paper and DynamoDB?](#124-what-is-the-difference-between-the-dynamo-paper-and-dynamodb)
- [125: Is DynamoDB a key-value store or a document database?](#125-is-dynamodb-a-key-value-store-or-a-document-database)
- [126: What does a typical serverless stack with DynamoDB look like?](#126-what-does-a-typical-serverless-stack-with-dynamodb-look-like)
- [127: How should you store files like images with DynamoDB?](#127-how-should-you-store-files-like-images-with-dynamodb)
- [128: Are attribute names and values case-sensitive?](#128-are-attribute-names-and-values-case-sensitive)
- [129: How is item size calculated?](#129-how-is-item-size-calculated)
- [130: What data types can a primary key use?](#130-what-data-types-can-a-primary-key-use)
- [131: Why are scans expensive?](#131-why-are-scans-expensive)
- [132: How do you find an item by a non-key attribute?](#132-how-do-you-find-an-item-by-a-non-key-attribute)
- [133: How do you decide between DynamoDB and RDS?](#133-how-do-you-decide-between-dynamodb-and-rds)
- [134: How do you define a DynamoDB table in CloudFormation?](#134-how-do-you-define-a-dynamodb-table-in-cloudformation)
- [135: How do you define a table with AWS CDK?](#135-how-do-you-define-a-table-with-aws-cdk)
- [136: How do you define a table with Terraform?](#136-how-do-you-define-a-table-with-terraform)
- [137: How does the begins_with function work?](#137-how-does-the-begins_with-function-work)
- [138: What other functions can you use in expressions?](#138-what-other-functions-can-you-use-in-expressions)
- [139: How do you use IN and BETWEEN in filters?](#139-how-do-you-use-in-and-between-in-filters)
- [140: What is import from S3?](#140-what-is-import-from-s3)
- [141: What is export to S3?](#141-what-is-export-to-s3)
- [142: What are common beginner mistakes with DynamoDB?](#142-what-are-common-beginner-mistakes-with-dynamodb)
- [143: What does ScannedCount mean compared to Count?](#143-what-does-scannedcount-mean-compared-to-count)
- [144: How do you scan a table in the AWS CLI?](#144-how-do-you-scan-a-table-in-the-aws-cli)
- [145: How do you query a table with the AWS CLI?](#145-how-do-you-query-a-table-with-the-aws-cli)
- [146: What is a DynamoDB endpoint?](#146-what-is-a-dynamodb-endpoint)
- [147: What is the AWS console item explorer?](#147-what-is-the-aws-console-item-explorer)
- [148: What does it mean that DynamoDB has no joins?](#148-what-does-it-mean-that-dynamodb-has-no-joins)
- [149: What is denormalization in DynamoDB?](#149-what-is-denormalization-in-dynamodb)
- [150: What does a typical DynamoDB item for a user look like?](#150-what-does-a-typical-dynamodb-item-for-a-user-look-like)

### Moderate Questions (151-300)

- [151: What is single-table design?](#151-what-is-single-table-design)
- [152: What are the trade-offs of single-table vs multi-table design?](#152-what-are-the-trade-offs-of-single-table-vs-multi-table-design)
- [153: How do you approach data modeling in DynamoDB?](#153-how-do-you-approach-data-modeling-in-dynamodb)
- [154: How do you model a one-to-many relationship?](#154-how-do-you-model-a-one-to-many-relationship)
- [155: How do you model a many-to-many relationship?](#155-how-do-you-model-a-many-to-many-relationship)
- [156: What is GSI overloading?](#156-what-is-gsi-overloading)
- [157: What is a sparse index and how do you use it?](#157-what-is-a-sparse-index-and-how-do-you-use-it)
- [158: How do you use hierarchical sort keys?](#158-how-do-you-use-hierarchical-sort-keys)
- [159: Why do people use generic key names like pk and sk?](#159-why-do-people-use-generic-key-names-like-pk-and-sk)
- [160: How do you model a user with orders and order items?](#160-how-do-you-model-a-user-with-orders-and-order-items)
- [161: How do you keep a version history of an item?](#161-how-do-you-keep-a-version-history-of-an-item)
- [162: How do you implement optimistic locking?](#162-how-do-you-implement-optimistic-locking)
- [163: How can you build a distributed lock with DynamoDB?](#163-how-can-you-build-a-distributed-lock-with-dynamodb)
- [164: How do you make writes idempotent?](#164-how-do-you-make-writes-idempotent)
- [165: How do you enforce uniqueness on a non-key attribute, like email?](#165-how-do-you-enforce-uniqueness-on-a-non-key-attribute-like-email)
- [166: How do you store time-series data?](#166-how-do-you-store-time-series-data)
- [167: How do you build a leaderboard?](#167-how-do-you-build-a-leaderboard)
- [168: How do you keep counts and totals without scanning?](#168-how-do-you-keep-counts-and-totals-without-scanning)
- [169: How do you implement pagination for an API?](#169-how-do-you-implement-pagination-for-an-api)
- [170: Why can Limit with a FilterExpression return fewer items than expected?](#170-why-can-limit-with-a-filterexpression-return-fewer-items-than-expected)
- [171: What is a parallel scan?](#171-what-is-a-parallel-scan)
- [172: How do you use paginators in SDK v3?](#172-how-do-you-use-paginators-in-sdk-v3)
- [173: How do you write a reliable batch write with retries?](#173-how-do-you-write-a-reliable-batch-write-with-retries)
- [174: How does batch_writer work in boto3?](#174-how-does-batch_writer-work-in-boto3)
- [175: What are the limits and costs of transactions?](#175-what-are-the-limits-and-costs-of-transactions)
- [176: How do you find out why a transaction failed?](#176-how-do-you-find-out-why-a-transaction-failed)
- [177: What does ClientRequestToken do in a transaction?](#177-what-does-clientrequesttoken-do-in-a-transaction)
- [178: What is a ConditionCheck in a transaction?](#178-what-is-a-conditioncheck-in-a-transaction)
- [179: What is a transaction conflict?](#179-what-is-a-transaction-conflict)
- [180: How do you connect DynamoDB Streams to a Lambda function?](#180-how-do-you-connect-dynamodb-streams-to-a-lambda-function)
- [181: What event source mapping settings matter for DynamoDB Streams?](#181-what-event-source-mapping-settings-matter-for-dynamodb-streams)
- [182: How do you report partial batch failures from a stream handler?](#182-how-do-you-report-partial-batch-failures-from-a-stream-handler)
- [183: How do you filter stream events before they reach Lambda?](#183-how-do-you-filter-stream-events-before-they-reach-lambda)
- [184: What ordering does DynamoDB Streams guarantee?](#184-what-ordering-does-dynamodb-streams-guarantee)
- [185: What is the difference between DynamoDB Streams and Kinesis Data Streams for DynamoDB?](#185-what-is-the-difference-between-dynamodb-streams-and-kinesis-data-streams-for-dynamodb)
- [186: How do you archive expired items to S3?](#186-how-do-you-archive-expired-items-to-s3)
- [187: What should you keep in mind when using TTL?](#187-what-should-you-keep-in-mind-when-using-ttl)
- [188: When should you use DAX?](#188-when-should-you-use-dax)
- [189: What caches does DAX have?](#189-what-caches-does-dax-have)
- [190: How does consistency work with DAX?](#190-how-does-consistency-work-with-dax)
- [191: How is DAX different from ElastiCache?](#191-how-is-dax-different-from-elasticache)
- [192: How do you configure auto scaling for a provisioned table?](#192-how-do-you-configure-auto-scaling-for-a-provisioned-table)
- [193: How do you choose between on-demand and provisioned capacity?](#193-how-do-you-choose-between-on-demand-and-provisioned-capacity)
- [194: Can you switch between capacity modes?](#194-can-you-switch-between-capacity-modes)
- [195: What is reserved capacity?](#195-what-is-reserved-capacity)
- [196: What is burst capacity?](#196-what-is-burst-capacity)
- [197: What is adaptive capacity?](#197-what-is-adaptive-capacity)
- [198: What is warm throughput?](#198-what-is-warm-throughput)
- [199: How do you limit the maximum throughput of an on-demand table?](#199-how-do-you-limit-the-maximum-throughput-of-an-on-demand-table)
- [200: What happens when a GSI is throttled?](#200-what-happens-when-a-gsi-is-throttled)
- [201: What does it mean that GSIs are eventually consistent?](#201-what-does-it-mean-that-gsis-are-eventually-consistent)
- [202: What happens when you add a GSI to an existing table?](#202-what-happens-when-you-add-a-gsi-to-an-existing-table)
- [203: How do you choose a projection type for a GSI?](#203-how-do-you-choose-a-projection-type-for-a-gsi)
- [204: What is the 10 GB limit with local secondary indexes?](#204-what-is-the-10-gb-limit-with-local-secondary-indexes)
- [205: What are multi-attribute composite keys in GSIs?](#205-what-are-multi-attribute-composite-keys-in-gsis)
- [206: How do you handle items that might go over 400 KB?](#206-how-do-you-handle-items-that-might-go-over-400-kb)
- [207: What is vertical partitioning of an item?](#207-what-is-vertical-partitioning-of-an-item)
- [208: What is ReturnValuesOnConditionCheckFailure?](#208-what-is-returnvaluesonconditioncheckfailure)
- [209: How do you handle DynamoDB errors in SDK v3?](#209-how-do-you-handle-dynamodb-errors-in-sdk-v3)
- [210: How do you tune timeouts in the SDK v3 client?](#210-how-do-you-tune-timeouts-in-the-sdk-v3-client)
- [211: Why should you create the DynamoDB client outside the Lambda handler?](#211-why-should-you-create-the-dynamodb-client-outside-the-lambda-handler)
- [212: What marshalling options does the Document Client have?](#212-what-marshalling-options-does-the-document-client-have)
- [213: How do you handle large numbers in JavaScript?](#213-how-do-you-handle-large-numbers-in-javascript)
- [214: How do you write sets with the Document Client?](#214-how-do-you-write-sets-with-the-document-client)
- [215: How do you test against DynamoDB Local in CI?](#215-how-do-you-test-against-dynamodb-local-in-ci)
- [216: How do you mock DynamoDB in unit tests?](#216-how-do-you-mock-dynamodb-in-unit-tests)
- [217: How do you handle schema changes in DynamoDB?](#217-how-do-you-handle-schema-changes-in-dynamodb)
- [218: How do you backfill a new attribute for existing items?](#218-how-do-you-backfill-a-new-attribute-for-existing-items)
- [219: What libraries help with DynamoDB modeling in Node.js?](#219-what-libraries-help-with-dynamodb-modeling-in-nodejs)
- [220: Example of an ElectroDB entity?](#220-example-of-an-electrodb-entity)
- [221: What are the pitfalls of using PartiQL?](#221-what-are-the-pitfalls-of-using-partiql)
- [222: How do you run transactions and batches with PartiQL?](#222-how-do-you-run-transactions-and-batches-with-partiql)
- [223: How do you update a value inside a nested map safely?](#223-how-do-you-update-a-value-inside-a-nested-map-safely)
- [224: How do you remove an element from a list when you don't know its index?](#224-how-do-you-remove-an-element-from-a-list-when-you-dont-know-its-index)
- [225: How do you safely decrease inventory?](#225-how-do-you-safely-decrease-inventory)
- [226: How do you do a conditional delete?](#226-how-do-you-do-a-conditional-delete)
- [227: What are Contributor Insights?](#227-what-are-contributor-insights)
- [228: Which alarms should you set for a production DynamoDB table?](#228-which-alarms-should-you-set-for-a-production-dynamodb-table)
- [229: How do you audit who changed data in DynamoDB?](#229-how-do-you-audit-who-changed-data-in-dynamodb)
- [230: How do you write a least-privilege IAM policy for a Lambda?](#230-how-do-you-write-a-least-privilege-iam-policy-for-a-lambda)
- [231: What is fine-grained access control with dynamodb:LeadingKeys?](#231-what-is-fine-grained-access-control-with-dynamodbleadingkeys)
- [232: What are resource-based policies for DynamoDB?](#232-what-are-resource-based-policies-for-dynamodb)
- [233: How do you access DynamoDB privately from a VPC?](#233-how-do-you-access-dynamodb-privately-from-a-vpc)
- [234: Which KMS key option should you choose?](#234-which-kms-key-option-should-you-choose)
- [235: How do you give another AWS account access to a table?](#235-how-do-you-give-another-aws-account-access-to-a-table)
- [236: How do you use AWS Backup with DynamoDB?](#236-how-do-you-use-aws-backup-with-dynamodb)
- [237: What do you need to know about restoring a table from PITR?](#237-what-do-you-need-to-know-about-restoring-a-table-from-pitr)
- [238: How do you set up a global table?](#238-how-do-you-set-up-a-global-table)
- [239: How does conflict resolution work in global tables?](#239-how-does-conflict-resolution-work-in-global-tables)
- [240: What is multi-Region strong consistency (MRSC)?](#240-what-is-multi-region-strong-consistency-mrsc)
- [241: How much do global tables cost?](#241-how-much-do-global-tables-cost)
- [242: How does import from S3 work in practice?](#242-how-does-import-from-s3-work-in-practice)
- [243: How do incremental exports work?](#243-how-do-incremental-exports-work)
- [244: What are zero-ETL integrations for DynamoDB?](#244-what-are-zero-etl-integrations-for-dynamodb)
- [245: How do you run SQL analytics on DynamoDB data?](#245-how-do-you-run-sql-analytics-on-dynamodb-data)
- [246: How do you add full-text search to DynamoDB data?](#246-how-do-you-add-full-text-search-to-dynamodb-data)
- [247: How do you query items by a date range across all users?](#247-how-do-you-query-items-by-a-date-range-across-all-users)
- [248: How do you do geospatial queries in DynamoDB?](#248-how-do-you-do-geospatial-queries-in-dynamodb)
- [249: How do you support case-insensitive lookups?](#249-how-do-you-support-case-insensitive-lookups)
- [250: How do you sort by a non-key attribute?](#250-how-do-you-sort-by-a-non-key-attribute)
- [251: How do you implement soft deletes?](#251-how-do-you-implement-soft-deletes)
- [252: How do you design a multi-tenant table?](#252-how-do-you-design-a-multi-tenant-table)
- [253: What is write sharding?](#253-what-is-write-sharding)
- [254: How do you estimate the monthly cost of a table?](#254-how-do-you-estimate-the-monthly-cost-of-a-table)
- [255: What are practical ways to lower DynamoDB costs?](#255-what-are-practical-ways-to-lower-dynamodb-costs)
- [256: When should you use the Standard-IA table class?](#256-when-should-you-use-the-standard-ia-table-class)
- [257: How do attribute names affect cost?](#257-how-do-attribute-names-affect-cost)
- [258: Why can UpdateItem be cheaper than PutItem?](#258-why-can-updateitem-be-cheaper-than-putitem)
- [259: How do you use begins_with to fetch different entity types?](#259-how-do-you-use-begins_with-to-fetch-different-entity-types)
- [260: How do you model a workflow or state machine in DynamoDB?](#260-how-do-you-model-a-workflow-or-state-machine-in-dynamodb)
- [261: How do you use DynamoDB as a session store?](#261-how-do-you-use-dynamodb-as-a-session-store)
- [262: How do you build a simple rate limiter with DynamoDB?](#262-how-do-you-build-a-simple-rate-limiter-with-dynamodb)
- [263: How can Step Functions use DynamoDB directly?](#263-how-can-step-functions-use-dynamodb-directly)
- [264: How do you call DynamoDB directly from API Gateway?](#264-how-do-you-call-dynamodb-directly-from-api-gateway)
- [265: How does AppSync work with DynamoDB?](#265-how-does-appsync-work-with-dynamodb)
- [266: How do you send DynamoDB changes to other services without Lambda?](#266-how-do-you-send-dynamodb-changes-to-other-services-without-lambda)
- [267: How do you delete many items efficiently?](#267-how-do-you-delete-many-items-efficiently)
- [268: How do you change the primary key of a table that's in production?](#268-how-do-you-change-the-primary-key-of-a-table-thats-in-production)
- [269: What grant methods does the CDK table construct offer?](#269-what-grant-methods-does-the-cdk-table-construct-offer)
- [270: How do you protect a table from being deleted by CloudFormation?](#270-how-do-you-protect-a-table-from-being-deleted-by-cloudformation)
- [271: How do you avoid conflicts between Terraform and auto scaling?](#271-how-do-you-avoid-conflicts-between-terraform-and-auto-scaling)
- [272: Do Query and Scan support strongly consistent reads?](#272-do-query-and-scan-support-strongly-consistent-reads)
- [273: Are GSI keys unique?](#273-are-gsi-keys-unique)
- [274: What causes a ValidationException?](#274-what-causes-a-validationexception)
- [275: How do you model data that is read together and data that is written often?](#275-how-do-you-model-data-that-is-read-together-and-data-that-is-written-often)
- [276: How do you keep duplicated data in sync?](#276-how-do-you-keep-duplicated-data-in-sync)
- [277: How do you handle deleting a parent and its children?](#277-how-do-you-handle-deleting-a-parent-and-its-children)
- [278: How do you get read-after-write consistency?](#278-how-do-you-get-read-after-write-consistency)
- [279: Why might DynamoDB requests be slow from your app?](#279-why-might-dynamodb-requests-be-slow-from-your-app)
- [280: How do you compress data in DynamoDB items?](#280-how-do-you-compress-data-in-dynamodb-items)
- [281: How do you encrypt specific attributes on the client side?](#281-how-do-you-encrypt-specific-attributes-on-the-client-side)
- [282: How can you use DynamoDB for event sourcing?](#282-how-can-you-use-dynamodb-for-event-sourcing)
- [283: How do you implement the outbox pattern with DynamoDB?](#283-how-do-you-implement-the-outbox-pattern-with-dynamodb)
- [284: How does DynamoDB compare to Aurora DSQL?](#284-how-does-dynamodb-compare-to-aurora-dsql)
- [285: How do you choose a partition key for IoT data?](#285-how-do-you-choose-a-partition-key-for-iot-data)
- [286: How do you get the latest N items for a key?](#286-how-do-you-get-the-latest-n-items-for-a-key)
- [287: How do you count items in a large partition?](#287-how-do-you-count-items-in-a-large-partition)
- [288: How do you find out why a query uses so much capacity?](#288-how-do-you-find-out-why-a-query-uses-so-much-capacity)
- [289: How do you handle access patterns that need OR conditions on keys?](#289-how-do-you-handle-access-patterns-that-need-or-conditions-on-keys)
- [290: How do you store and query hierarchical data like categories or folders?](#290-how-do-you-store-and-query-hierarchical-data-like-categories-or-folders)
- [291: What is the difference between a GSI and a materialized view?](#291-what-is-the-difference-between-a-gsi-and-a-materialized-view)
- [292: How do you handle "item not found" vs "access denied" in a multi-tenant app?](#292-how-do-you-handle-item-not-found-vs-access-denied-in-a-multi-tenant-app)
- [293: How do you read many items by key from several tables at once?](#293-how-do-you-read-many-items-by-key-from-several-tables-at-once)
- [294: When should you split one DynamoDB table into several?](#294-when-should-you-split-one-dynamodb-table-into-several)
- [295: How do you handle throttling in your application code?](#295-how-do-you-handle-throttling-in-your-application-code)
- [296: Why does a new on-demand table sometimes throttle?](#296-why-does-a-new-on-demand-table-sometimes-throttle)
- [297: What is the difference between ThrottlingException and ProvisionedThroughputExceededException?](#297-what-is-the-difference-between-throttlingexception-and-provisionedthroughputexceededexception)
- [298: How do you make sure two Lambda invocations don't process the same job?](#298-how-do-you-make-sure-two-lambda-invocations-dont-process-the-same-job)
- [299: How do you search items whose attribute contains a value?](#299-how-do-you-search-items-whose-attribute-contains-a-value)
- [300: What is the difference between a Query on the table and a Query on an LSI?](#300-what-is-the-difference-between-a-query-on-the-table-and-a-query-on-an-lsi)

### Advanced Questions (301-450)

- [301: How does DynamoDB decide which partition stores an item?](#301-how-does-dynamodb-decide-which-partition-stores-an-item)
- [302: What are the per-partition limits and why do they matter?](#302-what-are-the-per-partition-limits-and-why-do-they-matter)
- [303: When does DynamoDB split a partition?](#303-when-does-dynamodb-split-a-partition)
- [304: What is "split for heat"?](#304-what-is-split-for-heat)
- [305: What happens inside DynamoDB when you send a request?](#305-what-happens-inside-dynamodb-when-you-send-a-request)
- [306: How is data replicated inside a Region?](#306-how-is-data-replicated-inside-a-region)
- [307: Why do strongly consistent reads cost more?](#307-why-do-strongly-consistent-reads-cost-more)
- [308: How long can an eventually consistent read be out of date?](#308-how-long-can-an-eventually-consistent-read-be-out-of-date)
- [309: How are GSIs kept up to date?](#309-how-are-gsis-kept-up-to-date)
- [310: Can a GSI return an item that no longer exists in the table?](#310-can-a-gsi-return-an-item-that-no-longer-exists-in-the-table)
- [311: How do DynamoDB transactions work internally?](#311-how-do-dynamodb-transactions-work-internally)
- [312: What isolation levels do DynamoDB transactions give?](#312-what-isolation-levels-do-dynamodb-transactions-give)
- [313: What is the difference between a batch and a transaction?](#313-what-is-the-difference-between-a-batch-and-a-transaction)
- [314: How does replication work in global tables?](#314-how-does-replication-work-in-global-tables)
- [315: What problems can last-writer-wins cause?](#315-what-problems-can-last-writer-wins-cause)
- [316: What are the trade-offs of MRSC global tables?](#316-what-are-the-trade-offs-of-mrsc-global-tables)
- [317: How do DynamoDB Streams shards work?](#317-how-do-dynamodb-streams-shards-work)
- [318: How many consumers can read from one DynamoDB stream?](#318-how-many-consumers-can-read-from-one-dynamodb-stream)
- [319: How is a DAX cluster built?](#319-how-is-a-dax-cluster-built)
- [320: What are common pitfalls with DAX?](#320-what-are-common-pitfalls-with-dax)
- [321: How do you deal with a hot key?](#321-how-do-you-deal-with-a-hot-key)
- [322: How do you read data back from a sharded key?](#322-how-do-you-read-data-back-from-a-sharded-key)
- [323: How do you find out if you have a hot partition?](#323-how-do-you-find-out-if-you-have-a-hot-partition)
- [324: What kinds of throttling exist in DynamoDB?](#324-what-kinds-of-throttling-exist-in-dynamodb)
- [325: How would you design a table for 1 million writes per second?](#325-how-would-you-design-a-table-for-1-million-writes-per-second)
- [326: What happens to pagination if items change while you are paging?](#326-what-happens-to-pagination-if-items-change-while-you-are-paging)
- [327: How does DynamoDB split a table into scan segments?](#327-how-does-dynamodb-split-a-table-into-scan-segments)
- [328: How would you design a URL shortener with DynamoDB?](#328-how-would-you-design-a-url-shortener-with-dynamodb)
- [329: How would you model a chat application?](#329-how-would-you-model-a-chat-application)
- [330: How would you design an e-commerce order system?](#330-how-would-you-design-an-e-commerce-order-system)
- [331: How would you build a social feed?](#331-how-would-you-build-a-social-feed)
- [332: How would you design inventory reservation during checkout?](#332-how-would-you-design-inventory-reservation-during-checkout)
- [333: How would you build a job scheduler or delayed queue?](#333-how-would-you-build-a-job-scheduler-or-delayed-queue)
- [334: How would you build a large-scale leaderboard?](#334-how-would-you-build-a-large-scale-leaderboard)
- [335: How do you isolate tenants of very different sizes?](#335-how-do-you-isolate-tenants-of-very-different-sizes)
- [336: How would you design an audit log in DynamoDB?](#336-how-would-you-design-an-audit-log-in-dynamodb)
- [337: How does the Powertools idempotency utility use DynamoDB?](#337-how-does-the-powertools-idempotency-utility-use-dynamodb)
- [338: What are the weak points of a DynamoDB-based lock?](#338-what-are-the-weak-points-of-a-dynamodb-based-lock)
- [339: How do you get exactly-once processing from DynamoDB Streams?](#339-how-do-you-get-exactly-once-processing-from-dynamodb-streams)
- [340: How do you keep aggregates correct with Streams?](#340-how-do-you-keep-aggregates-correct-with-streams)
- [341: How do you handle a poison record in a stream?](#341-how-do-you-handle-a-poison-record-in-a-stream)
- [342: Is there any ordering across different items in a DynamoDB stream?](#342-is-there-any-ordering-across-different-items-in-a-dynamodb-stream)
- [343: How do you build a change data capture pipeline to a data lake?](#343-how-do-you-build-a-change-data-capture-pipeline-to-a-data-lake)
- [344: What do you do when access patterns change after launch?](#344-what-do-you-do-when-access-patterns-change-after-launch)
- [345: How would you migrate from a relational database to DynamoDB?](#345-how-would-you-migrate-from-a-relational-database-to-dynamodb)
- [346: How do you migrate a live table with zero downtime?](#346-how-do-you-migrate-a-live-table-with-zero-downtime)
- [347: How do you copy a table to another account or Region?](#347-how-do-you-copy-a-table-to-another-account-or-region)
- [348: How do you model costs for a big workload?](#348-how-do-you-model-costs-for-a-big-workload)
- [349: When does provisioned capacity become cheaper than on-demand?](#349-when-does-provisioned-capacity-become-cheaper-than-on-demand)
- [350: Why do GSIs increase write costs so much?](#350-why-do-gsis-increase-write-costs-so-much)
- [351: How does rounding of capacity units affect cost?](#351-how-does-rounding-of-capacity-units-affect-cost)
- [352: How do you reduce the cost of frequent small updates on big items?](#352-how-do-you-reduce-the-cost-of-frequent-small-updates-on-big-items)
- [353: How do you estimate whether Standard-IA saves money?](#353-how-do-you-estimate-whether-standard-ia-saves-money)
- [354: How does TTL help with costs at scale?](#354-how-does-ttl-help-with-costs-at-scale)
- [355: How do you restrict which attributes a user can read or write?](#355-how-do-you-restrict-which-attributes-a-user-can-read-or-write)
- [356: How can you use attribute-based access control (ABAC) with DynamoDB?](#356-how-can-you-use-attribute-based-access-control-abac-with-dynamodb)
- [357: How do you stop data from leaving your network through DynamoDB?](#357-how-do-you-stop-data-from-leaving-your-network-through-dynamodb)
- [358: What happens if a customer managed KMS key is disabled?](#358-what-happens-if-a-customer-managed-kms-key-is-disabled)
- [359: How does searchable encryption work in the AWS Database Encryption SDK?](#359-how-does-searchable-encryption-work-in-the-aws-database-encryption-sdk)
- [360: How do you meet compliance requirements for a DynamoDB table?](#360-how-do-you-meet-compliance-requirements-for-a-dynamodb-table)
- [361: Is PartiQL vulnerable to injection?](#361-is-partiql-vulnerable-to-injection)
- [362: What risks come with building expressions dynamically?](#362-what-risks-come-with-building-expressions-dynamically)
- [363: What are the main hard limits you should know?](#363-what-are-the-main-hard-limits-you-should-know)
- [364: What expression limits can surprise you?](#364-what-expression-limits-can-surprise-you)
- [365: What are the account-level throughput quotas?](#365-what-are-the-account-level-throughput-quotas)
- [366: Why do sort keys with numbers stored as strings sort strangely?](#366-why-do-sort-keys-with-numbers-stored-as-strings-sort-strangely)
- [367: How does DynamoDB compare string values in sort keys?](#367-how-does-dynamodb-compare-string-values-in-sort-keys)
- [368: Why can a Query return zero items but still have a LastEvaluatedKey?](#368-why-can-a-query-return-zero-items-but-still-have-a-lastevaluatedkey)
- [369: What can go wrong if you store TTL in milliseconds?](#369-what-can-go-wrong-if-you-store-ttl-in-milliseconds)
- [370: Why can't a transaction touch the same item twice?](#370-why-cant-a-transaction-touch-the-same-item-twice)
- [371: Do failed conditional writes cost capacity?](#371-do-failed-conditional-writes-cost-capacity)
- [372: Can you rely on DeleteItem to tell you if an item existed?](#372-can-you-rely-on-deleteitem-to-tell-you-if-an-item-existed)
- [373: How do you handle a GSI with low-cardinality keys?](#373-how-do-you-handle-a-gsi-with-low-cardinality-keys)
- [374: Why is a time-based partition key a bad idea?](#374-why-is-a-time-based-partition-key-a-bad-idea)
- [375: What happens when an item collection gets very large?](#375-what-happens-when-an-item-collection-gets-very-large)
- [376: How do you load test a DynamoDB-backed service?](#376-how-do-you-load-test-a-dynamodb-backed-service)
- [377: How do you prepare a table for a known traffic spike?](#377-how-do-you-prepare-a-table-for-a-known-traffic-spike)
- [378: How do you design for a full Region outage?](#378-how-do-you-design-for-a-full-region-outage)
- [379: What are the RPO and RTO of different DynamoDB recovery options?](#379-what-are-the-rpo-and-rto-of-different-dynamodb-recovery-options)
- [380: How do you route writes in an active-active global table setup?](#380-how-do-you-route-writes-in-an-active-active-global-table-setup)
- [381: How do you lower latency from the client side?](#381-how-do-you-lower-latency-from-the-client-side)
- [382: How do retries affect tail latency?](#382-how-do-retries-affect-tail-latency)
- [383: What is a retry storm and how do you avoid it?](#383-what-is-a-retry-storm-and-how-do-you-avoid-it)
- [384: How does Lambda concurrency interact with DynamoDB?](#384-how-does-lambda-concurrency-interact-with-dynamodb)
- [385: How does ParallelizationFactor affect stream processing?](#385-how-does-parallelizationfactor-affect-stream-processing)
- [386: What are tumbling windows in stream processing?](#386-what-are-tumbling-windows-in-stream-processing)
- [387: When would you use EventBridge Pipes instead of a Lambda stream consumer?](#387-when-would-you-use-eventbridge-pipes-instead-of-a-lambda-stream-consumer)
- [388: How do you handle snapshots in an event-sourced DynamoDB model?](#388-how-do-you-handle-snapshots-in-an-event-sourced-dynamodb-model)
- [389: How do you implement CQRS with DynamoDB?](#389-how-do-you-implement-cqrs-with-dynamodb)
- [390: How do you handle graph-like queries in DynamoDB?](#390-how-do-you-handle-graph-like-queries-in-dynamodb)
- [391: How do you replace joins in DynamoDB?](#391-how-do-you-replace-joins-in-dynamodb)
- [392: How do you do aggregations like SUM or GROUP BY?](#392-how-do-you-do-aggregations-like-sum-or-group-by)
- [393: Can DynamoDB do vector or semantic search?](#393-can-dynamodb-do-vector-or-semantic-search)
- [394: How do you design keys that support several sort orders?](#394-how-do-you-design-keys-that-support-several-sort-orders)
- [395: When should you use multi-attribute GSI keys instead of synthetic keys?](#395-when-should-you-use-multi-attribute-gsi-keys-instead-of-synthetic-keys)
- [396: How do you store all versions of a document and query them by date?](#396-how-do-you-store-all-versions-of-a-document-and-query-them-by-date)
- [397: How do you delete all data for a tenant in a shared table?](#397-how-do-you-delete-all-data-for-a-tenant-in-a-shared-table)
- [398: How do you handle GDPR "right to be forgotten" requests?](#398-how-do-you-handle-gdpr-right-to-be-forgotten-requests)
- [399: How do you archive cold data from DynamoDB to S3?](#399-how-do-you-archive-cold-data-from-dynamodb-to-s3)
- [400: How do you produce a large report from DynamoDB data?](#400-how-do-you-produce-a-large-report-from-dynamodb-data)
- [401: How does DynamoDB compare to Cassandra?](#401-how-does-dynamodb-compare-to-cassandra)
- [402: When would DynamoDB be the wrong choice even at high scale?](#402-when-would-dynamodb-be-the-wrong-choice-even-at-high-scale)
- [403: How do you validate items before writing them?](#403-how-do-you-validate-items-before-writing-them)
- [404: How do you get type safety when working with DynamoDB in TypeScript?](#404-how-do-you-get-type-safety-when-working-with-dynamodb-in-typescript)
- [405: How do you structure a data access layer for DynamoDB?](#405-how-do-you-structure-a-data-access-layer-for-dynamodb)
- [406: How does DynamoDB Local differ from the real service?](#406-how-does-dynamodb-local-differ-from-the-real-service)
- [407: How do you trace DynamoDB calls?](#407-how-do-you-trace-dynamodb-calls)
- [408: How would you log consumed capacity per feature?](#408-how-would-you-log-consumed-capacity-per-feature)
- [409: How do you investigate a throttling incident?](#409-how-do-you-investigate-a-throttling-incident)
- [410: Scenario: latency suddenly went up. What do you check?](#410-scenario-latency-suddenly-went-up-what-do-you-check)
- [411: Scenario: your DynamoDB bill doubled. How do you find out why?](#411-scenario-your-dynamodb-bill-doubled-how-do-you-find-out-why)
- [412: Scenario: adding a GSI to a huge table is taking very long. What can you do?](#412-scenario-adding-a-gsi-to-a-huge-table-is-taking-very-long-what-can-you-do)
- [413: Scenario: someone deleted important items by mistake. How do you recover?](#413-scenario-someone-deleted-important-items-by-mistake-how-do-you-recover)
- [414: Scenario: the stream consumer's IteratorAge keeps growing. What do you do?](#414-scenario-the-stream-consumers-iteratorage-keeps-growing-what-do-you-do)
- [415: Scenario: ConditionalCheckFailedRequests suddenly spikes. What could it mean?](#415-scenario-conditionalcheckfailedrequests-suddenly-spikes-what-could-it-mean)
- [416: Scenario: you need a new access pattern on a 5 TB table. How do you add it?](#416-scenario-you-need-a-new-access-pattern-on-a-5-tb-table-how-do-you-add-it)
- [417: Scenario: an item is close to the 400 KB limit. What do you do?](#417-scenario-an-item-is-close-to-the-400-kb-limit-what-do-you-do)
- [418: Scenario: one product is getting most of the traffic during a sale. How do you handle it?](#418-scenario-one-product-is-getting-most-of-the-traffic-during-a-sale-how-do-you-handle-it)
- [419: Scenario: a post goes viral and gets thousands of likes per second. How do you count them?](#419-scenario-a-post-goes-viral-and-gets-thousands-of-likes-per-second-how-do-you-count-them)
- [420: Scenario: both email and username must be unique. How do you design it?](#420-scenario-both-email-and-username-must-be-unique-how-do-you-design-it)
- [421: Scenario: product wants page numbers (page 1, 2, 3 ... 50). How do you handle it?](#421-scenario-product-wants-page-numbers-page-1-2-3--50-how-do-you-handle-it)
- [422: Scenario: you need to update more than 100 items atomically. What can you do?](#422-scenario-you-need-to-update-more-than-100-items-atomically-what-can-you-do)
- [423: Scenario: how would you implement a saga across services with DynamoDB?](#423-scenario-how-would-you-implement-a-saga-across-services-with-dynamodb)
- [424: Scenario: design a token bucket rate limiter that allows bursts.](#424-scenario-design-a-token-bucket-rate-limiter-that-allows-bursts)
- [425: Scenario: data must stay in specific countries. How do you design it?](#425-scenario-data-must-stay-in-specific-countries-how-do-you-design-it)
- [426: Scenario: users read their data from another Region right after writing it. What's the issue?](#426-scenario-users-read-their-data-from-another-region-right-after-writing-it-whats-the-issue)
- [427: How do you plan capacity for GSIs in a global table?](#427-how-do-you-plan-capacity-for-gsis-in-a-global-table)
- [428: What do you need to fix after restoring a table?](#428-what-do-you-need-to-fix-after-restoring-a-table)
- [429: How would you run a disaster recovery drill for DynamoDB?](#429-how-would-you-run-a-disaster-recovery-drill-for-dynamodb)
- [430: How do you test what happens during throttling or failures?](#430-how-do-you-test-what-happens-during-throttling-or-failures)
- [431: How do streams behave with global tables?](#431-how-do-streams-behave-with-global-tables)
- [432: How do you avoid infinite loops with stream consumers that write to the same table?](#432-how-do-you-avoid-infinite-loops-with-stream-consumers-that-write-to-the-same-table)
- [433: What is the difference between a Query with a filter and a sparse GSI, in cost?](#433-what-is-the-difference-between-a-query-with-a-filter-and-a-sparse-gsi-in-cost)
- [434: How would you model a calendar or booking system to prevent double booking?](#434-how-would-you-model-a-calendar-or-booking-system-to-prevent-double-booking)
- [435: How do you handle the clock in conditional logic?](#435-how-do-you-handle-the-clock-in-conditional-logic)
- [436: What is the difference between an item collection and a partition?](#436-what-is-the-difference-between-an-item-collection-and-a-partition)
- [437: How do you choose between Streams + Lambda and transactions for keeping data in sync?](#437-how-do-you-choose-between-streams--lambda-and-transactions-for-keeping-data-in-sync)
- [438: How do you test a data model before building the app?](#438-how-do-you-test-a-data-model-before-building-the-app)
- [439: How do you handle multiple entity versions during a rolling deploy?](#439-how-do-you-handle-multiple-entity-versions-during-a-rolling-deploy)
- [440: How do you protect production tables from risky admin actions?](#440-how-do-you-protect-production-tables-from-risky-admin-actions)
- [441: How would you implement a "recently viewed items" list per user?](#441-how-would-you-implement-a-recently-viewed-items-list-per-user)
- [442: How do you handle data for users in many time zones?](#442-how-do-you-handle-data-for-users-in-many-time-zones)
- [443: What is the impact of using UUIDs vs sortable IDs (like ULID or KSUID) as keys?](#443-what-is-the-impact-of-using-uuids-vs-sortable-ids-like-ulid-or-ksuid-as-keys)
- [444: How do you limit the blast radius of a bad deploy that writes bad data?](#444-how-do-you-limit-the-blast-radius-of-a-bad-deploy-that-writes-bad-data)
- [445: How do you share a DynamoDB table between microservices?](#445-how-do-you-share-a-dynamodb-table-between-microservices)
- [446: What are the trade-offs of storing a whole aggregate in one item?](#446-what-are-the-trade-offs-of-storing-a-whole-aggregate-in-one-item)
- [447: How do you approach DynamoDB in an interview system design question?](#447-how-do-you-approach-dynamodb-in-an-interview-system-design-question)
- [448: What is the "access pattern table" and why is it useful?](#448-what-is-the-access-pattern-table-and-why-is-it-useful)
- [449: What are the most important DynamoDB best practices?](#449-what-are-the-most-important-dynamodb-best-practices)
- [450: How would you explain DynamoDB data modeling to a team coming from SQL?](#450-how-would-you-explain-dynamodb-data-modeling-to-a-team-coming-from-sql)

---

# Easy Questions (1-150)

## 1: What is DynamoDB?

DynamoDB is a fully managed NoSQL database from AWS. It stores data as key-value pairs and documents, and gives you fast reads and writes (usually single-digit milliseconds) at almost any scale.

You don't manage servers, install software, apply patches or plan disk space. You create a table, choose a key, and start reading and writing. AWS handles replication, scaling, backups and hardware failures behind the scenes.

## 2: What are the main features of DynamoDB?

- Key-value and document data model
- Predictable low latency at any size
- Two capacity modes: on-demand and provisioned
- Secondary indexes (global and local)
- ACID transactions
- DynamoDB Streams for change data capture
- Time to Live (TTL) for automatic expiry of items
- Global tables for multi-Region replication
- Point-in-time recovery and on-demand backups
- Encryption at rest by default
- DAX, an in-memory cache in front of DynamoDB

## 3: What does it mean that DynamoDB is serverless?

It means there are no servers or clusters for you to provision or manage. You don't pick instance sizes or node counts. You pay for what you read, write and store (on-demand mode), or for the capacity you reserve (provisioned mode).

Scaling, patching, replication across Availability Zones and recovery from hardware failures are all done by AWS. Your code just calls the DynamoDB API over HTTPS.

## 4: What are tables, items and attributes?

- A **table** is a collection of data, like a table in SQL.
- An **item** is a single record in a table, like a row. Each item is identified by its primary key.
- An **attribute** is a single piece of data in an item, like a column. Apart from the key attributes, items in the same table can have completely different attributes.

```json
{
  "userId": "u-123",
  "name": "Ana",
  "email": "ana@example.com",
  "tags": ["admin", "beta"]
}
```

Here the whole object is one item, and `userId`, `name`, `email` and `tags` are attributes.

## 5: What types of primary keys does DynamoDB support?

There are two types:

1. **Simple primary key**: only a partition key. Each item must have a unique partition key value.
2. **Composite primary key**: a partition key plus a sort key. Many items can share the same partition key, but the combination of partition key and sort key must be unique.

You choose the primary key when you create the table, and you can't change it later.

## 6: What is a partition key?

The partition key (also called the hash key) is the attribute DynamoDB uses to decide where an item is stored. DynamoDB runs the value through an internal hash function, and the result decides which physical partition holds the item.

Every read by key and every `Query` needs the partition key value. A good partition key has many distinct values so that traffic spreads evenly across partitions.

## 7: What is a sort key?

The sort key (also called the range key) is the second part of a composite primary key. Items with the same partition key are stored together and kept sorted by the sort key.

This lets you run range queries inside one partition key, like "all orders for customer 42 placed in 2026" or "the last 10 messages in this chat".

## 8: Can you give an example of a composite primary key?

A table that stores orders per customer:

| customerId (PK) | orderDate (SK)       | total |
| --------------- | -------------------- | ----- |
| c-42            | 2026-01-03T10:00:00Z | 120   |
| c-42            | 2026-02-11T08:30:00Z | 45    |
| c-77            | 2026-02-01T12:00:00Z | 300   |

`customerId` groups the orders, and `orderDate` sorts them. You can fetch all orders for `c-42`, or only the orders between two dates, with a single `Query`.

## 9: What data types does DynamoDB support?

- **Scalar types**: String (S), Number (N), Binary (B), Boolean (BOOL) and Null (NULL)
- **Document types**: List (L) and Map (M)
- **Set types**: String Set (SS), Number Set (NS) and Binary Set (BS)

Key attributes (partition key and sort key) must be String, Number or Binary.

## 10: What is the difference between a list and a map?

A **list** is an ordered collection of values, and the values can be of any type, even mixed: `["red", 5, true]`.

A **map** is an unordered collection of name-value pairs, similar to a JSON object: `{"city": "Tbilisi", "zip": "0100"}`.

Both can be nested inside each other up to 32 levels deep, so you can store fairly complex JSON-like documents in one item.

## 11: What are sets in DynamoDB and how are they different from lists?

A set holds unique values of a single type: all strings, all numbers or all binary values. Duplicates are not allowed and the order is not kept.

A list can hold duplicates, mixed types, and keeps the order.

Sets are handy for things like tags, where you want to add or remove a value without reading the item first. Sets can't be empty. If you remove the last element, the attribute is removed.

## 12: What is the maximum size of an item?

400 KB. This includes both the attribute names and the attribute values, in UTF-8 bytes. If you need to store bigger data, like images or large documents, put the data in Amazon S3 and save the S3 key in the DynamoDB item.

## 13: Is DynamoDB schemaless?

Mostly. The only things DynamoDB enforces are the primary key attributes (and the key attributes of any index you define on the table). Everything else is free-form, so two items in the same table can have completely different attributes.

That doesn't mean you have no schema. The schema lives in your application code and in your access patterns. Many teams validate items in code (for example with Zod or a library like ElectroDB) before writing them.

## 14: How is DynamoDB different from a relational database?

- No joins. You design tables around the queries you need and often duplicate data.
- No fixed schema except for keys.
- You query mostly by primary key or index. Ad hoc queries on any column are not efficient.
- Scaling is horizontal and automatic. You don't scale up a single server.
- You pay for reads and writes, not for a running server.
- SQL databases are usually modeled first and queried later. In DynamoDB you list the access patterns first and model the data to fit them.

## 15: How is DynamoDB different from MongoDB?

Both are NoSQL document stores, but:

- DynamoDB is only available as a managed AWS service. MongoDB can be self-hosted or used through Atlas.
- MongoDB has a rich query language with ad hoc queries, aggregations and many index types. DynamoDB is built around key-based access and a small set of operations.
- DynamoDB is billed by reads, writes and storage. MongoDB Atlas is mostly billed by cluster size.
- DynamoDB has a 400 KB item limit. MongoDB documents can be up to 16 MB.
- DynamoDB scales with no cluster tuning. MongoDB needs sharding decisions at large scale.

## 16: When is DynamoDB a good choice?

- You know your access patterns ahead of time
- You need consistent low latency at high traffic
- You want no database servers to manage
- Serverless apps with Lambda and API Gateway
- Session stores, shopping carts, user profiles, IoT data, game state, leaderboards, metadata stores
- Workloads with unpredictable spikes (on-demand mode)

## 17: When is DynamoDB not a good choice?

- You need many ad hoc queries, complex joins or heavy reporting on the same data
- Your access patterns change all the time and you can't predict them
- You need full-text search (use OpenSearch next to it)
- Items larger than 400 KB that you can't split or move to S3
- Small apps where a relational model is simpler and the team knows SQL well
- Heavy analytics. Export the data to S3 or use zero-ETL to Redshift instead.

## 18: How does DynamoDB keep data durable?

Every write is stored on several storage nodes in three Availability Zones within the Region before DynamoDB confirms it. If one node or even one whole Availability Zone fails, the data is still available.

For extra protection you can turn on point-in-time recovery, create on-demand backups, or use global tables to replicate to other Regions.

## 19: What is a partition in DynamoDB?

A partition is a unit of storage and throughput behind your table. DynamoDB splits a table into partitions based on partition key hashes. Each partition is stored on SSDs and replicated across Availability Zones.

As your table grows in size or traffic, DynamoDB adds more partitions on its own. You never manage partitions directly, but knowing about them helps you choose good keys and avoid hot spots.

## 20: What read consistency options does DynamoDB have?

- **Eventually consistent reads** (the default): the result might not show a write that just happened, but usually catches up within about a second. They cost half as much.
- **Strongly consistent reads**: the result always shows all writes that were confirmed before the read. You ask for them with `ConsistentRead: true`.
- **Transactional reads** with `TransactGetItems`, which give a consistent view across several items.

## 21: When would you use a strongly consistent read?

When your logic needs the latest value right after a write. For example, checking an account balance right after an update, or reading a record a user just saved and showing it back to them.

Keep in mind:

- They cost twice as much as eventually consistent reads
- They are not supported on global secondary indexes
- They can have slightly higher latency

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const doc = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const { Item } = await doc.send(
  new GetCommand({
    TableName: "Accounts",
    Key: { accountId: "a-1" },
    ConsistentRead: true,
  }),
);
```

## 22: What capacity modes does DynamoDB offer?

1. **On-demand**: you don't plan capacity. DynamoDB scales to your traffic, and you pay per request. It's the default and the recommended mode for most new tables.
2. **Provisioned**: you set the number of read capacity units (RCU) and write capacity units (WCU) per second. You can add auto scaling. It can be cheaper for steady, predictable traffic.

## 23: What is on-demand capacity mode?

In on-demand mode you pay for each read and write request (read request units and write request units). There's nothing to plan: the table handles sudden traffic jumps by itself. A table can instantly handle up to double its previous traffic peak, and it keeps adapting from there.

You can also set a maximum throughput on an on-demand table or index to cap cost and protect downstream systems.

## 24: What is provisioned capacity mode?

You tell DynamoDB how many reads and writes per second your table needs, in RCUs and WCUs. You pay for that capacity per hour whether you use it or not. If traffic goes above it, requests can be throttled.

Usually you combine it with auto scaling, which raises and lowers the capacity based on a target utilization. It fits workloads with steady or predictable traffic, where it often costs less than on-demand.

## 25: What is a read capacity unit (RCU)?

One RCU gives you, per second, for an item up to 4 KB:

- 1 strongly consistent read, or
- 2 eventually consistent reads

A transactional read of a 4 KB item costs 2 RCUs. Items bigger than 4 KB need more units, rounded up to the next 4 KB. In on-demand mode the same math applies, but the units are called read request units.

## 26: What is a write capacity unit (WCU)?

One WCU gives you one write per second for an item up to 1 KB. Bigger items need more units, rounded up to the next 1 KB. A transactional write costs 2 WCUs per KB.

So writing a 3.5 KB item once per second needs 4 WCUs. In on-demand mode the units are called write request units.

## 27: How do you calculate the capacity needed for a workload?

Example: you need 50 reads per second of 6 KB items, eventually consistent, and 20 writes per second of 2.5 KB items.

- Reads: 6 KB rounds up to 8 KB, which is 2 units of 4 KB. Strongly consistent would be 2 RCU per read. Eventually consistent is half: 1 RCU. 50 reads x 1 = **50 RCU**.
- Writes: 2.5 KB rounds up to 3 KB, so 3 WCU per write. 20 writes x 3 = **60 WCU**.

## 28: What is throttling?

Throttling happens when your requests go over the capacity that a table, index or partition can handle at that moment. DynamoDB rejects the extra requests with errors like `ProvisionedThroughputExceededException` or `ThrottlingException`.

The AWS SDKs retry throttled requests automatically with exponential backoff. If throttling keeps happening, you need more capacity, on-demand mode, or a better key design to spread the load.

## 29: How do you create a table with the AWS CLI?

```bash
aws dynamodb create-table \
  --table-name Orders \
  --attribute-definitions \
    AttributeName=customerId,AttributeType=S \
    AttributeName=orderDate,AttributeType=S \
  --key-schema \
    AttributeName=customerId,KeyType=HASH \
    AttributeName=orderDate,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

You only define the key attributes in `attribute-definitions`. Other attributes are not declared. `HASH` is the partition key and `RANGE` is the sort key.

## 30: How do you create a table with the AWS SDK for JavaScript v3?

```js
import { DynamoDBClient, CreateTableCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({ region: "us-east-1" });

await client.send(
  new CreateTableCommand({
    TableName: "Users",
    AttributeDefinitions: [{ AttributeName: "userId", AttributeType: "S" }],
    KeySchema: [{ AttributeName: "userId", KeyType: "HASH" }],
    BillingMode: "PAY_PER_REQUEST",
  }),
);
```

Table creation is asynchronous. The table starts in `CREATING` status and becomes `ACTIVE` after a short time. You can wait for it with `waitUntilTableExists` from the same package.

## 31: How do you write an item with PutItem?

```js
import { PutCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new PutCommand({
    TableName: "Users",
    Item: {
      userId: "u-123",
      name: "Ana",
      email: "ana@example.com",
      createdAt: new Date().toISOString(),
    },
  }),
);
```

`PutItem` creates a new item, or fully replaces an existing item with the same primary key.

## 32: Does PutItem overwrite an existing item?

Yes. If an item with the same primary key already exists, `PutItem` replaces the whole item. Attributes that are not in the new item are gone.

To prevent this, add a condition:

```js
await doc.send(
  new PutCommand({
    TableName: "Users",
    Item: { userId: "u-123", name: "Ana" },
    ConditionExpression: "attribute_not_exists(userId)",
  }),
);
```

If the item already exists, the call fails with `ConditionalCheckFailedException`.

## 33: How do you read an item with GetItem?

`GetItem` reads one item by its full primary key. For a composite key you must pass both the partition key and the sort key.

```js
import { GetCommand } from "@aws-sdk/lib-dynamodb";

const { Item } = await doc.send(
  new GetCommand({
    TableName: "Orders",
    Key: { customerId: "c-42", orderDate: "2026-01-03T10:00:00Z" },
  }),
);

if (!Item) {
  console.log("Not found");
}
```

If the item doesn't exist, `Item` is `undefined`. It is not an error.

## 34: How do you update an item with UpdateItem?

`UpdateItem` changes only the attributes you list, leaving the rest of the item alone.

```js
import { UpdateCommand } from "@aws-sdk/lib-dynamodb";

const { Attributes } = await doc.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { userId: "u-123" },
    UpdateExpression: "SET #name = :name, updatedAt = :now",
    ExpressionAttributeNames: { "#name": "name" },
    ExpressionAttributeValues: {
      ":name": "Ana Smith",
      ":now": new Date().toISOString(),
    },
    ReturnValues: "ALL_NEW",
  }),
);
```

If the item doesn't exist, `UpdateItem` creates it, unless you add a condition expression.

## 35: How do you delete an item?

```js
import { DeleteCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new DeleteCommand({
    TableName: "Users",
    Key: { userId: "u-123" },
  }),
);
```

Deleting an item that doesn't exist is not an error. If you need to know whether something was deleted, use `ReturnValues: 'ALL_OLD'` or add `ConditionExpression: 'attribute_exists(userId)'`.

## 36: What is a Query operation?

`Query` returns items that share the same partition key, optionally filtered by a condition on the sort key. Results come back sorted by the sort key. It only reads the items it needs, so it's fast and cheap compared to a scan.

```js
import { QueryCommand } from "@aws-sdk/lib-dynamodb";

const { Items } = await doc.send(
  new QueryCommand({
    TableName: "Orders",
    KeyConditionExpression: "customerId = :c AND orderDate >= :from",
    ExpressionAttributeValues: {
      ":c": "c-42",
      ":from": "2026-01-01",
    },
  }),
);
```

## 37: What is a Scan operation?

`Scan` reads every item in a table or index, page by page, and returns all of them (or the ones that match a filter). It consumes read capacity for every item it reads, even items the filter throws away.

Scans are fine for small tables, one-off scripts, exports or admin tasks. For regular application queries on large tables, use `Query` with a well-designed key or index instead.

## 38: What is the difference between Query and Scan?

| Query                                | Scan                                      |
| ------------------------------------ | ----------------------------------------- |
| Needs a partition key value          | Needs no key                              |
| Reads only matching items in one key | Reads the whole table or index            |
| Cost depends on data read            | Cost depends on the whole table size      |
| Results sorted by sort key           | No useful order                           |
| Use for normal app queries           | Use for exports, migrations, small tables |

## 39: What operators can you use in a KeyConditionExpression?

For the partition key, only equality: `pk = :value`.

For the sort key:

- `=`, `<`, `<=`, `>`, `>=`
- `BETWEEN :a AND :b`
- `begins_with(sk, :prefix)`

You can't use `<>`, `IN`, `contains` or `OR` in a key condition. Those are only allowed in a `FilterExpression`.

## 40: What is a FilterExpression?

A filter that DynamoDB applies after it reads the items for a `Query` or `Scan`, but before it returns them to you.

```js
new QueryCommand({
  TableName: "Orders",
  KeyConditionExpression: "customerId = :c",
  FilterExpression: "#status = :s",
  ExpressionAttributeNames: { "#status": "status" },
  ExpressionAttributeValues: { ":c": "c-42", ":s": "SHIPPED" },
});
```

The important part: filtered-out items still count toward read capacity, because DynamoDB already read them. A filter reduces the data sent over the network, not the cost.

## 41: What is a ProjectionExpression?

It tells DynamoDB which attributes to return, instead of the whole item.

```js
new GetCommand({
  TableName: "Users",
  Key: { userId: "u-123" },
  ProjectionExpression: "#n, email, address.city",
  ExpressionAttributeNames: { "#n": "name" },
});
```

It makes the response smaller, but it doesn't lower the read capacity used. DynamoDB still reads the full item to build the response.

## 42: What are ExpressionAttributeNames?

Placeholders for attribute names, starting with `#`. You need them when:

- The attribute name is a reserved word (like `name`, `status`, `date`, `count`)
- The name has special characters, like a dot or a dash
- You build expressions dynamically and want safe names

```js
UpdateExpression: 'SET #s = :s',
ExpressionAttributeNames: { '#s': 'status' },
```

## 43: What are ExpressionAttributeValues?

Placeholders for values, starting with `:`. You can't put literal values straight into an expression, so you reference them by placeholder.

```js
KeyConditionExpression: 'customerId = :c',
ExpressionAttributeValues: { ':c': 'c-42' },
```

With the Document Client you pass plain JavaScript values. With the low-level client you pass typed values like `{ ':c': { S: 'c-42' } }`.

## 44: What are reserved words in DynamoDB?

DynamoDB has a long list of reserved words (several hundred) that you can't use directly as attribute names inside expressions. Common examples are `name`, `status`, `date`, `year`, `data`, `count`, `size`, `user`, `timestamp`, `value` and `order`.

You can still have attributes with these names. You just reference them through `ExpressionAttributeNames`, like `#name`. Many teams simply alias every attribute name to avoid surprises.

## 45: What is a condition expression?

A condition that must be true for a write (`PutItem`, `UpdateItem`, `DeleteItem`) to happen. DynamoDB checks it against the current item, atomically, at write time. If it's false, the write is rejected with `ConditionalCheckFailedException`.

```js
new UpdateCommand({
  TableName: "Accounts",
  Key: { accountId: "a-1" },
  UpdateExpression: "SET balance = balance - :amt",
  ConditionExpression: "balance >= :amt",
  ExpressionAttributeValues: { ":amt": 50 },
});
```

This prevents the balance from going negative without any locks.

## 46: How do you prevent creating a duplicate item?

Use `attribute_not_exists` on the partition key in a condition:

```js
await doc.send(
  new PutCommand({
    TableName: "Users",
    Item: { userId: "u-123", email: "ana@example.com" },
    ConditionExpression: "attribute_not_exists(userId)",
  }),
);
```

DynamoDB checks whether an item with that primary key already exists. For composite keys, checking the partition key attribute is enough, because the condition is evaluated against the item with that exact full key.

## 47: What clauses can an UpdateExpression have?

- `SET`: add or replace attributes, or do math (`SET views = views + :one`)
- `REMOVE`: delete attributes from the item
- `ADD`: add a number to a numeric attribute, or add elements to a set
- `DELETE`: remove elements from a set

You can combine them in one expression:

```text
SET #name = :n, updatedAt = :now REMOVE tempToken ADD loginCount :one
```

Each clause keyword can appear only once in an expression.

## 48: How does the SET clause work?

`SET` writes one or more attributes. If an attribute exists, it's replaced. If it doesn't, it's created.

```text
SET price = :p, stock = stock - :qty, tags = list_append(tags, :newTags)
```

`SET` can also use functions like `if_not_exists` and `list_append`, and simple `+` and `-` math on numbers.

## 49: How does the REMOVE clause work?

`REMOVE` deletes attributes from an item, or elements from a list by index.

```text
REMOVE resetToken, addresses[1]
```

After removing `addresses[1]`, the list shifts, so the element that was at index 2 is now at index 1. Removing an attribute that doesn't exist is not an error.

## 50: How does the ADD clause work?

For numbers, `ADD` adds a value (use a negative number to subtract). If the attribute doesn't exist, it starts from 0.

For sets, `ADD` adds elements, ignoring ones that are already there.

```js
new UpdateCommand({
  TableName: "Posts",
  Key: { postId: "p-1" },
  UpdateExpression: "ADD likes :one, tags :t",
  ExpressionAttributeValues: {
    ":one": 1,
    ":t": new Set(["dynamodb"]),
  },
});
```

`ADD` only works with top-level attributes and only with numbers and sets.

## 51: How does the DELETE clause in an UpdateExpression work?

`DELETE` removes one or more elements from a set. It only works on set attributes (SS, NS, BS).

```js
new UpdateCommand({
  TableName: "Posts",
  Key: { postId: "p-1" },
  UpdateExpression: "DELETE tags :t",
  ExpressionAttributeValues: { ":t": new Set(["draft"]) },
});
```

Don't confuse it with the `DeleteItem` operation, which deletes the whole item. If the set ends up empty, DynamoDB removes the attribute.

## 52: What is an atomic counter?

A numeric attribute that you increase or decrease with `UpdateItem`, without reading it first. DynamoDB applies the change on the server, so two requests at the same time don't overwrite each other.

```js
new UpdateCommand({
  TableName: "Pages",
  Key: { pageId: "home" },
  UpdateExpression: "SET views = if_not_exists(views, :zero) + :one",
  ExpressionAttributeValues: { ":zero": 0, ":one": 1 },
});
```

Note that updates are not idempotent. If a request times out and the SDK retries it, the counter can be increased twice. That's fine for page views, but not for money.

## 53: What does the ReturnValues parameter do?

It tells DynamoDB what to return after a write:

- `NONE` (default): nothing
- `ALL_OLD`: the whole item as it was before the write
- `UPDATED_OLD`: only the updated attributes, before the write
- `ALL_NEW`: the whole item after the write
- `UPDATED_NEW`: only the updated attributes, after the write

`PutItem` and `DeleteItem` support only `NONE` and `ALL_OLD`. `UpdateItem` supports all five. Returning values doesn't cost extra capacity.

## 54: What is a secondary index?

A secondary index lets you query the table using a different key than the primary key. DynamoDB keeps the index in sync with the table for you.

For example, a `Users` table keyed by `userId` can have an index keyed by `email`, so you can look up a user by email with a `Query` instead of a `Scan`.

There are two types: global secondary indexes (GSI) and local secondary indexes (LSI).

## 55: What is a global secondary index (GSI)?

A GSI has its own partition key and optional sort key, which can be any attributes of the table. It's "global" because queries on it can span all partitions of the base table.

- You can add or remove a GSI at any time
- It's updated asynchronously, so reads are always eventually consistent
- It has its own capacity settings in provisioned mode
- The default limit is 20 GSIs per table

## 56: What is a local secondary index (LSI)?

An LSI uses the same partition key as the table but a different sort key. It's "local" because it only indexes items within the same partition key value.

- You must create it when you create the table. You can't add or remove it later.
- It supports strongly consistent reads
- It shares capacity with the base table
- Max 5 LSIs per table
- If a table has an LSI, each partition key value (item collection) is limited to 10 GB

## 57: What is the difference between a GSI and an LSI?

| Feature                 | GSI                        | LSI                           |
| ----------------------- | -------------------------- | ----------------------------- |
| Partition key           | Any attribute              | Same as the table             |
| Sort key                | Any attribute, optional    | Any attribute, required       |
| When created            | Any time                   | Only at table creation        |
| Consistency             | Eventually consistent only | Eventual or strong            |
| Capacity                | Its own                    | Shared with the table         |
| Size limit              | None                       | 10 GB per partition key value |
| Max per table (default) | 20                         | 5                             |

In practice, GSIs are used much more often. LSIs are only worth it when you need strong consistency on an alternate sort order.

## 58: What are projected attributes in an index?

The attributes copied from the table into the index. There are three options:

- `KEYS_ONLY`: only the table and index keys
- `INCLUDE`: the keys plus a list of attributes you choose
- `ALL`: every attribute of the item

More projected attributes means more storage and more write cost, but you can answer more queries from the index alone. With a GSI, attributes that are not projected can't be returned by a query on that index. You'd need a second `GetItem` on the table.

## 59: How do you query a GSI?

Pass `IndexName` to the `Query` call:

```js
const { Items } = await doc.send(
  new QueryCommand({
    TableName: "Users",
    IndexName: "email-index",
    KeyConditionExpression: "email = :e",
    ExpressionAttributeValues: { ":e": "ana@example.com" },
  }),
);
```

You always get an array back, since GSI keys don't have to be unique. You can't use `GetItem` on an index, only `Query` and `Scan`.

## 60: What is BatchGetItem?

It reads up to 100 items (up to 16 MB in total) from one or more tables in one request. Each item is fetched by its full primary key.

```js
import { BatchGetCommand } from "@aws-sdk/lib-dynamodb";

const { Responses, UnprocessedKeys } = await doc.send(
  new BatchGetCommand({
    RequestItems: {
      Users: {
        Keys: [{ userId: "u-1" }, { userId: "u-2" }],
      },
    },
  }),
);
```

Items come back in no particular order. Missing items are just not in the response.

## 61: What is BatchWriteItem?

It puts or deletes up to 25 items (up to 16 MB) across one or more tables in one request.

```js
import { BatchWriteCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new BatchWriteCommand({
    RequestItems: {
      Users: [
        { PutRequest: { Item: { userId: "u-1", name: "Ana" } } },
        { DeleteRequest: { Key: { userId: "u-2" } } },
      ],
    },
  }),
);
```

It doesn't support updates or condition expressions, and it's not a transaction. Some writes can succeed while others fail.

## 62: What are UnprocessedItems and UnprocessedKeys?

When a batch request can't finish all of its work (usually because of throttling), DynamoDB returns the leftover requests:

- `UnprocessedItems` for `BatchWriteItem`
- `UnprocessedKeys` for `BatchGetItem`

The call itself still succeeds, so you must check these fields and retry them yourself, ideally with exponential backoff. Ignoring them is a common bug that leads to silently missing data.

## 63: How does pagination work in DynamoDB?

A single `Query` or `Scan` returns at most 1 MB of data. If there's more, the response includes `LastEvaluatedKey`. To get the next page, pass that value as `ExclusiveStartKey` in the next request. When `LastEvaluatedKey` is missing, you've reached the end.

```js
let lastKey;
do {
  const page = await doc.send(
    new QueryCommand({
      TableName: "Orders",
      KeyConditionExpression: "customerId = :c",
      ExpressionAttributeValues: { ":c": "c-42" },
      ExclusiveStartKey: lastKey,
    }),
  );
  console.log(page.Items);
  lastKey = page.LastEvaluatedKey;
} while (lastKey);
```

## 64: What does the Limit parameter do?

`Limit` sets the maximum number of items DynamoDB reads (evaluates) in one request, not the number it returns after filtering. If you use a `FilterExpression`, you can get fewer items than the limit, or even zero items, together with a `LastEvaluatedKey`.

It's useful for page sizes, like "give me 20 orders at a time", and for keeping scans from using too much capacity in one call.

## 65: How do you sort Query results?

Results are always sorted by the sort key. Ascending is the default. To get descending order, set `ScanIndexForward: false`.

```js
new QueryCommand({
  TableName: "Messages",
  KeyConditionExpression: "chatId = :c",
  ExpressionAttributeValues: { ":c": "chat-1" },
  ScanIndexForward: false,
  Limit: 20,
});
```

This is the usual way to get "the latest 20 messages". You can't sort by a non-key attribute. For that you need an index with that attribute as the sort key.

## 66: How do you count items in DynamoDB?

Use `Select: 'COUNT'` in a `Query` or `Scan`. It returns `Count` (items that matched after the filter) and `ScannedCount` (items read) without sending the items back.

```js
const { Count } = await doc.send(
  new QueryCommand({
    TableName: "Orders",
    KeyConditionExpression: "customerId = :c",
    ExpressionAttributeValues: { ":c": "c-42" },
    Select: "COUNT",
  }),
);
```

It still reads the items, so it costs the same capacity and is still limited to 1 MB per page. For large or frequent counts, keep a counter attribute instead.

## 67: What is Time to Live (TTL)?

TTL lets DynamoDB delete items automatically after a certain time. You choose an attribute (for example `expiresAt`) that holds a Unix timestamp in seconds. Once the current time passes that value, the item is marked as expired and DynamoDB deletes it in the background.

TTL deletes are free. They don't use write capacity. It's commonly used for sessions, temporary tokens, caches and old logs.

## 68: How do you enable TTL on a table?

```bash
aws dynamodb update-time-to-live \
  --table-name Sessions \
  --time-to-live-specification "Enabled=true, AttributeName=expiresAt"
```

Then write items with that attribute set to a Number in epoch seconds:

```js
const oneDay = 24 * 60 * 60;

await doc.send(
  new PutCommand({
    TableName: "Sessions",
    Item: {
      sessionId: "s-1",
      userId: "u-1",
      expiresAt: Math.floor(Date.now() / 1000) + oneDay,
    },
  }),
);
```

Items without the attribute, or with a value that isn't a Number, are never deleted by TTL.

## 69: What is DynamoDB Streams?

DynamoDB Streams is a time-ordered log of every change (insert, update, delete) to the items in a table. Each change is a stream record, kept for 24 hours.

You usually connect a Lambda function to the stream to react to changes: sending emails, updating a search index, building aggregates, replicating data, or writing an audit log. Records for the same item appear in the order the changes happened.

## 70: What stream view types are there?

When you enable a stream, you choose what each record contains:

- `KEYS_ONLY`: only the key attributes of the changed item
- `NEW_IMAGE`: the item as it looks after the change
- `OLD_IMAGE`: the item as it looked before the change
- `NEW_AND_OLD_IMAGES`: both versions

`NEW_AND_OLD_IMAGES` is the most flexible, since you can see exactly what changed. `KEYS_ONLY` keeps records small.

## 71: Does DynamoDB support transactions?

Yes. DynamoDB has ACID transactions through two operations:

- `TransactWriteItems`: up to 100 write actions (Put, Update, Delete, ConditionCheck) that all succeed or all fail
- `TransactGetItems`: up to 100 Get actions that return a consistent snapshot

Transactions can span multiple tables in the same account and Region. Total size is limited to 4 MB. They cost twice the capacity of normal reads and writes.

## 72: How do you use TransactWriteItems?

Example: transfer money between two accounts.

```js
import { TransactWriteCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new TransactWriteCommand({
    TransactItems: [
      {
        Update: {
          TableName: "Accounts",
          Key: { accountId: "a-1" },
          UpdateExpression: "SET balance = balance - :amt",
          ConditionExpression: "balance >= :amt",
          ExpressionAttributeValues: { ":amt": 100 },
        },
      },
      {
        Update: {
          TableName: "Accounts",
          Key: { accountId: "a-2" },
          UpdateExpression: "SET balance = balance + :amt",
          ExpressionAttributeValues: { ":amt": 100 },
        },
      },
    ],
  }),
);
```

If the first account doesn't have enough money, nothing is written and you get a `TransactionCanceledException`.

## 73: How do you use TransactGetItems?

It reads several items as one consistent snapshot. No other transaction can change them in the middle of the read.

```js
import { TransactGetCommand } from "@aws-sdk/lib-dynamodb";

const { Responses } = await doc.send(
  new TransactGetCommand({
    TransactItems: [
      { Get: { TableName: "Accounts", Key: { accountId: "a-1" } } },
      { Get: { TableName: "Accounts", Key: { accountId: "a-2" } } },
    ],
  }),
);

const [a1, a2] = Responses.map((r) => r.Item);
```

Unlike `BatchGetItem`, responses come back in the same order as the requests.

## 74: What are on-demand backups?

Full backups of a table that you create whenever you want, from the console, CLI, SDK or AWS Backup. They are kept until you delete them, and creating them has no effect on table performance or availability.

```bash
aws dynamodb create-backup --table-name Orders --backup-name orders-2026-10-29
```

You restore a backup into a new table. You can't restore on top of an existing table.

## 75: What is point-in-time recovery (PITR)?

PITR keeps continuous backups of a table, so you can restore it to any second within the recovery period. The default period is 35 days, and you can set it anywhere from 1 to 35 days.

It protects you from accidental deletes or bad writes, like a buggy deploy that overwrote data. Restores always go to a new table.

```bash
aws dynamodb update-continuous-backups \
  --table-name Orders \
  --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
```

## 76: What are global tables?

Global tables replicate a DynamoDB table across multiple AWS Regions. Each replica can accept reads and writes (active-active). Changes made in one Region are copied to the others, usually within about a second.

They are used for low-latency access for users around the world and for disaster recovery if a whole Region goes down. Global tables give 99.999% availability in their SLA, compared to 99.99% for single-Region tables.

## 77: What is DAX?

DynamoDB Accelerator (DAX) is a managed in-memory cache that sits in front of DynamoDB. It's API-compatible with DynamoDB, so you swap the client and keep most of your code. Reads that hit the cache come back in microseconds instead of milliseconds.

It's good for read-heavy workloads with repeated reads of the same items, like product catalogs or game state. It only helps eventually consistent reads. DAX runs as a cluster inside your VPC.

## 78: Is data in DynamoDB encrypted?

Yes. All data at rest is always encrypted, and you can't turn it off. You pick which key is used:

- **AWS owned key** (default, no extra cost)
- **AWS managed key** (`aws/dynamodb`, stored in your account's KMS)
- **Customer managed key** in KMS, which you fully control

Data in transit is encrypted too, since the API is called over HTTPS.

## 79: How do you control who can access a DynamoDB table?

With AWS IAM. You attach policies to users, roles or groups that allow specific actions on specific tables:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem"],
      "Resource": [
        "arn:aws:dynamodb:us-east-1:123456789012:table/Orders",
        "arn:aws:dynamodb:us-east-1:123456789012:table/Orders/index/*"
      ]
    }
  ]
}
```

You can also attach resource-based policies directly to tables and streams, which is useful for cross-account access.

## 80: Which packages do you use for DynamoDB in the AWS SDK for JavaScript v3?

- `@aws-sdk/client-dynamodb`: the low-level client with all commands (`CreateTableCommand`, `PutItemCommand` and so on). Values must be in DynamoDB JSON format.
- `@aws-sdk/lib-dynamodb`: the Document Client (`DynamoDBDocumentClient`) that converts plain JavaScript values for you.
- `@aws-sdk/util-dynamodb`: `marshall` and `unmarshall` helpers.

```bash
npm install @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
```

The old v2 SDK (`aws-sdk` package) is in maintenance mode and has reached end of support, so new code should use v3.

## 81: What is the difference between the low-level client and the Document Client?

With the low-level client, every value needs a type descriptor:

```js
import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";

await new DynamoDBClient({}).send(
  new PutItemCommand({
    TableName: "Users",
    Item: { userId: { S: "u-1" }, age: { N: "30" } },
  }),
);
```

The Document Client wraps it and lets you use normal JavaScript values:

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";

const doc = DynamoDBDocumentClient.from(new DynamoDBClient({}));

await doc.send(
  new PutCommand({
    TableName: "Users",
    Item: { userId: "u-1", age: 30 },
  }),
);
```

Most application code uses the Document Client. The low-level client is used for table management or when you need exact control over types.

## 82: What do marshall and unmarshall do?

They convert between plain JavaScript objects and the DynamoDB JSON format.

```js
import { marshall, unmarshall } from "@aws-sdk/util-dynamodb";

marshall({ userId: "u-1", age: 30, active: true });
// { userId: { S: 'u-1' }, age: { N: '30' }, active: { BOOL: true } }

unmarshall({ userId: { S: "u-1" }, age: { N: "30" } });
// { userId: 'u-1', age: 30 }
```

A common place you need `unmarshall` is in a Lambda function that reads DynamoDB Stream records, because records arrive in DynamoDB JSON.

## 83: What is the DynamoDB JSON format?

It's the wire format DynamoDB uses, where each value is wrapped in an object that says its type:

```json
{
  "userId": { "S": "u-1" },
  "age": { "N": "30" },
  "tags": { "SS": ["a", "b"] },
  "address": { "M": { "city": { "S": "Tbilisi" } } },
  "scores": { "L": [{ "N": "1" }, { "N": "2" }] },
  "active": { "BOOL": true },
  "nickname": { "NULL": true }
}
```

Numbers are sent as strings so that no precision is lost between languages. You see this format in the low-level API, the CLI, stream records and S3 exports.

## 84: How do you use DynamoDB from Python?

With boto3. The resource API is the friendlier option and works with plain Python types:

```python
import boto3
from boto3.dynamodb.conditions import Key

table = boto3.resource("dynamodb").Table("Orders")

table.put_item(Item={"customerId": "c-42", "orderDate": "2026-01-03", "total": 120})

response = table.query(
    KeyConditionExpression=Key("customerId").eq("c-42") & Key("orderDate").begins_with("2026-")
)
print(response["Items"])
```

Numbers come back as `decimal.Decimal`, and you must pass `Decimal` instead of `float` when writing numbers with decimals.

## 85: What is DynamoDB Local?

A downloadable version of DynamoDB that runs on your machine. You use it for development and tests without an AWS account or any cost.

```bash
docker run -p 8000:8000 amazon/dynamodb-local
```

Then point the SDK to it:

```js
const client = new DynamoDBClient({
  endpoint: "http://localhost:8000",
  region: "local",
  credentials: { accessKeyId: "x", secretAccessKey: "x" },
});
```

It supports the same API, but it doesn't copy production behavior like throttling or real performance.

## 86: What is NoSQL Workbench?

A free desktop tool from AWS for DynamoDB. It has three main parts:

- **Data modeler**: design tables, keys and indexes, and add sample data
- **Visualizer**: see how your access patterns map to the table and GSIs
- **Operation builder**: run and build queries against real tables or DynamoDB Local, and generate code for them

It's handy when designing a single-table model and explaining it to the team.

## 87: What is PartiQL in DynamoDB?

PartiQL is a SQL-compatible query language that you can use with DynamoDB. It lets you write `SELECT`, `INSERT`, `UPDATE` and `DELETE` statements instead of using the native API.

```sql
SELECT * FROM "Orders" WHERE customerId = 'c-42' AND orderDate >= '2026-01-01'
```

It doesn't add new features like joins or `GROUP BY`. Under the hood it still runs a `GetItem`, `Query` or `Scan`, so the same rules about keys and cost apply.

## 88: How do you run a PartiQL statement from code?

Use `ExecuteStatementCommand` with parameters, not string concatenation:

```js
import { ExecuteStatementCommand } from "@aws-sdk/lib-dynamodb";

const { Items } = await doc.send(
  new ExecuteStatementCommand({
    Statement: 'SELECT * FROM "Orders" WHERE customerId = ?',
    Parameters: ["c-42"],
  }),
);
```

There's also `BatchExecuteStatement` for batches and `ExecuteTransaction` for transactions.

## 89: What table classes are available?

- **DynamoDB Standard** (default): the normal balance of storage and request costs
- **DynamoDB Standard-Infrequent Access (Standard-IA)**: storage is about 60% cheaper, but reads and writes cost more

Both have the same performance, durability and features. You can switch a table between classes later. Standard-IA makes sense when storage is the biggest part of the bill, like old orders or logs that are rarely read.

## 90: What is deletion protection?

A table setting that blocks the table from being deleted until you turn the setting off. It protects against accidental deletes from the console, CLI, scripts or IaC tools.

```bash
aws dynamodb update-table --table-name Orders --deletion-protection-enabled
```

It's a good default for every production table.

## 91: What statuses can a table have?

- `CREATING`: the table is being created
- `ACTIVE`: ready to use
- `UPDATING`: a change is in progress (like a capacity update or a new GSI). The table is still usable.
- `DELETING`: being deleted
- `ARCHIVING` / `ARCHIVED`: the table's KMS key is no longer accessible and DynamoDB archived it
- `INACCESSIBLE_ENCRYPTION_CREDENTIALS`: the KMS key is disabled or missing

You can read the status with `DescribeTable`.

## 92: What are the naming rules for tables and attributes?

Table and index names:

- 3 to 255 characters
- Allowed: `a-z`, `A-Z`, `0-9`, `_`, `-`, `.`
- Case-sensitive, so `Orders` and `orders` are different tables

Attribute names can be any UTF-8 string from 1 byte up to 64 KB, but key attribute names are limited to 255 bytes. Short names are better, because names count toward the item size.

## 93: Can you store empty strings in DynamoDB?

Yes, for non-key attributes. Empty strings and empty binary values are allowed in normal attributes. They're not allowed as values of a table's primary key, and not as values for index key attributes.

Empty sets are not allowed at all. Empty lists and empty maps are fine.

## 94: How does the Number type work?

Numbers can be positive, negative or zero, integers or decimals, with up to 38 digits of precision. They are sent over the wire as strings, so no precision is lost when moving between languages.

There is no separate integer or float type. In JavaScript, numbers that don't fit into a normal JS number (like big IDs) can lose precision, so either store them as strings or use the `wrapNumbers` option in the Document Client.

## 95: When would you use the Binary type?

For data that isn't text: compressed JSON, encrypted values, small images or thumbnails, hashes or protobuf data. In the SDK you pass a `Uint8Array` or `Buffer`.

```js
import { gzipSync } from "node:zlib";

await doc.send(
  new PutCommand({
    TableName: "Docs",
    Item: {
      docId: "d-1",
      body: gzipSync(JSON.stringify(bigObject)),
    },
  }),
);
```

Binary values count toward the 400 KB item size, so for large files use S3.

## 96: How do you store dates and times?

DynamoDB has no date type, so you use one of these:

- **ISO 8601 string** like `2026-10-29T10:15:00Z`. It's readable and sorts correctly as a string. Good for sort keys.
- **Number** with epoch seconds or milliseconds. Compact and easy for math. Required for TTL (seconds).

Always use UTC and the same format everywhere. Mixing formats breaks sorting and range queries.

## 97: What is an item collection?

All items in a table (and its LSIs) that share the same partition key value. For example, all orders for customer `c-42` form one item collection.

Item collections are what `Query` works with: one query reads from one item collection. If a table has an LSI, each item collection is limited to 10 GB.

## 98: What is a hot partition?

A partition that gets much more traffic than the others. It happens when many requests use the same partition key value, like a `status = ACTIVE` key or a single popular product.

Each partition has a limit on reads and writes per second, so a hot partition can be throttled even when the table as a whole has plenty of capacity. The fix is usually a better partition key with more distinct values.

## 99: How do you choose a good partition key?

- It should have many distinct values (high cardinality), like `userId`, `orderId` or `deviceId`
- Requests should be spread evenly across those values
- It should match how you read the data, since every query needs it

Bad choices: `status`, `country`, `date`, `type`, or any key where a few values get most of the traffic.

## 100: How do you use the sort key for range queries?

Design the sort key so that the values you want sit next to each other. Example: a sort key like `ORDER#2026-10-29T10:00:00Z` allows:

```js
// all orders in October 2026
new QueryCommand({
  TableName: "App",
  KeyConditionExpression: "pk = :pk AND begins_with(sk, :prefix)",
  ExpressionAttributeValues: {
    ":pk": "CUSTOMER#c-42",
    ":prefix": "ORDER#2026-10",
  },
});
```

You can also use `BETWEEN` with two full timestamps for exact ranges.

## 101: How do you store and query nested JSON documents?

Store the document as a map (and lists inside it). You can read or update nested fields using document paths with dots for map keys and brackets for list indexes.

```js
await doc.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { userId: "u-1" },
    UpdateExpression: "SET address.city = :city, phones[0] = :phone",
    ExpressionAttributeValues: { ":city": "Batumi", ":phone": "+995555000000" },
  }),
);
```

The parent map must already exist. `SET address.city = :city` fails if `address` isn't there. You can't use a nested attribute as a table or index key, unless you copy it to a top-level attribute.

## 102: How do you append items to a list?

Use `list_append` in a `SET` clause. Combine it with `if_not_exists` so it works even when the list doesn't exist yet:

```js
new UpdateCommand({
  TableName: "Users",
  Key: { userId: "u-1" },
  UpdateExpression:
    "SET history = list_append(if_not_exists(history, :empty), :new)",
  ExpressionAttributeValues: {
    ":empty": [],
    ":new": [{ action: "login", at: Date.now() }],
  },
});
```

Both arguments to `list_append` must be lists. Swap them to prepend instead of append. Watch out for lists that keep growing, since the item can hit the 400 KB limit.

## 103: What does if_not_exists do?

`if_not_exists(path, value)` returns the current value of the attribute if it exists, and `value` if it doesn't. It's only allowed in `SET`.

Common uses:

- Set a `createdAt` only on the first write: `SET createdAt = if_not_exists(createdAt, :now)`
- Start a counter from zero: `SET views = if_not_exists(views, :zero) + :one`

## 104: How do you update an item only if it is in a certain state?

Add a condition on the current state:

```js
await doc.send(
  new UpdateCommand({
    TableName: "Orders",
    Key: { orderId: "o-1" },
    UpdateExpression: "SET #s = :shipped, shippedAt = :now",
    ConditionExpression: "#s = :paid",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: {
      ":shipped": "SHIPPED",
      ":paid": "PAID",
      ":now": new Date().toISOString(),
    },
  }),
);
```

If the order is not `PAID`, the update fails instead of moving the order into a wrong state.

## 105: What is ConditionalCheckFailedException?

The error DynamoDB returns when a condition expression evaluates to false. It's not a system error. It means your rule worked and blocked the write. You catch it and handle it as a normal business case:

```js
import { ConditionalCheckFailedException } from "@aws-sdk/client-dynamodb";

try {
  await doc.send(putCommand);
} catch (err) {
  if (err instanceof ConditionalCheckFailedException) {
    return { status: 409, message: "User already exists" };
  }
  throw err;
}
```

A failed conditional write still uses write capacity.

## 106: What are the common DynamoDB errors?

- `ConditionalCheckFailedException`: a condition was false
- `ProvisionedThroughputExceededException` / `ThrottlingException`: too many requests
- `ResourceNotFoundException`: the table or index doesn't exist or isn't active
- `ValidationException`: bad request, like a wrong key, a wrong type, or a reserved word used without a placeholder
- `TransactionCanceledException`: a transaction was cancelled
- `ItemCollectionSizeLimitExceededException`: an item collection went over 10 GB (with an LSI)
- `RequestLimitExceeded`: account-level throughput limit reached
- `InternalServerError`: a server-side problem, safe to retry

## 107: How do the AWS SDKs handle retries?

The SDKs retry throttling errors and server errors automatically, with exponential backoff and jitter. In SDK v3 the default is the `standard` retry mode with 3 total attempts. You can change it:

```js
const client = new DynamoDBClient({
  maxAttempts: 5,
  retryMode: "adaptive",
});
```

`adaptive` mode also slows down the client side when it sees throttling. Validation errors and condition failures are never retried, because retrying won't change the result.

## 108: How is DynamoDB priced?

The main parts of the bill:

- **Reads and writes**: per request in on-demand mode, or per provisioned RCU/WCU per hour
- **Storage**: per GB per month (cheaper with Standard-IA)
- **Indexes**: GSI writes and storage are billed like table writes and storage
- **Extras**: backups, PITR, global table replication, Streams reads (free for Lambda triggers), data export and import, DAX nodes, data transfer out

Writes are much more expensive than reads, and big items cost more, so item size and the number of indexes matter a lot.

## 109: Is there a free tier for DynamoDB?

Yes. The AWS Free Tier includes 25 GB of storage and enough provisioned capacity (25 RCU and 25 WCU) for small apps, plus some free Streams reads. This part of the free tier doesn't expire after 12 months.

Check the AWS pricing page for the current details, since free tier terms change from time to time.

## 110: Which CloudWatch metrics are most useful for DynamoDB?

- `ConsumedReadCapacityUnits` / `ConsumedWriteCapacityUnits`
- `ThrottledRequests`, `ReadThrottleEvents`, `WriteThrottleEvents`
- `SuccessfulRequestLatency`
- `SystemErrors` and `UserErrors`
- `ConditionalCheckFailedRequests`
- `ReturnedItemCount`
- For streams: Lambda's `IteratorAge`
- For global tables: `ReplicationLatency`

Set alarms on throttling, system errors and latency for production tables.

## 111: What is auto scaling in DynamoDB?

For provisioned tables and GSIs, auto scaling changes the RCUs and WCUs based on traffic. You set a minimum, a maximum and a target utilization (for example 70%). Application Auto Scaling watches CloudWatch metrics and raises or lowers capacity to stay near that target.

It reacts in minutes, not seconds, so very sudden spikes can still be throttled. For spiky traffic, on-demand mode is usually a better fit.

## 112: Can you change the primary key of an existing table?

No. The key schema is fixed when you create the table. To use a different key you need to:

1. Create a new table with the new key
2. Copy the data (with a script, export to S3 and import, or a stream-based migration)
3. Switch the app to the new table

If you only need a new way to query, add a GSI instead. That's often enough.

## 113: How do you delete all items in a table?

There's no `TRUNCATE`. Your options:

- **Delete and recreate the table**: fastest and cheapest for big tables, but you lose settings unless they're in IaC
- **Scan and delete**: scan the keys and call `BatchWriteItem` with delete requests, 25 at a time. Costs write capacity for every item.
- **TTL**: set an expiry attribute on items so DynamoDB removes them over time for free

For test tables, deleting and recreating is usually the simplest.

## 114: How do you delete a table?

```bash
aws dynamodb delete-table --table-name Orders
```

This deletes the table, all items and all indexes. If deletion protection is on, you have to turn it off first. On-demand backups are kept. If PITR was on, DynamoDB also keeps a system backup of the table for 35 days, so you can still restore it. Taking your own on-demand backup first is still a good habit.

## 115: What does DescribeTable return?

Information about a table:

- Key schema and attribute definitions
- Status (`ACTIVE`, `UPDATING` and so on)
- Billing mode and provisioned throughput
- Approximate item count and size in bytes (updated about every six hours)
- GSIs and LSIs with their status
- Stream settings and stream ARN
- Table class, encryption settings and deletion protection

```bash
aws dynamodb describe-table --table-name Orders
```

## 116: How do you list all tables?

```bash
aws dynamodb list-tables
```

In SDK v3 you can use the paginator so you don't have to handle `LastEvaluatedTableName` yourself:

```js
import { DynamoDBClient, paginateListTables } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({});

for await (const page of paginateListTables({ client }, {})) {
  console.log(page.TableNames);
}
```

Table lists are per Region, so tables in other Regions don't show up.

## 117: What can you change with UpdateTable?

- Billing mode (on-demand or provisioned)
- Provisioned throughput
- Maximum on-demand throughput and warm throughput
- Add or remove GSIs
- Stream settings
- Table class
- Encryption key
- Deletion protection
- Global table replicas

You can't change the primary key or add LSIs.

## 118: What happens if you call UpdateItem on an item that doesn't exist?

DynamoDB creates a new item with the given key and the attributes from the `SET` or `ADD` clauses. This is called an upsert.

If you only want to update existing items, add a condition:

```js
ConditionExpression: "attribute_exists(userId)";
```

Without it, a typo in the key or a request for a deleted item quietly creates a new, half-filled item.

## 119: Can you query without the partition key?

No. `Query` always needs an exact partition key value. If you need to find items by some other attribute:

- Create a GSI with that attribute as the partition key
- Use `Scan` with a filter (only for small tables or rare jobs)

If you find yourself scanning often, the data model is missing an index.

## 120: What happens to items that don't have a GSI's key attribute?

They're not added to the index. A GSI only contains items that have all of its key attributes. This is called a sparse index, and you can use it on purpose. For example, a GSI on `openTicketDate` holds only open tickets, if you remove that attribute when a ticket is closed.

## 121: How many secondary indexes can a table have?

By default up to 20 GSIs (you can ask AWS for more) and up to 5 LSIs. Across all LSIs and GSIs of a table, you can project at most 100 attributes with the `INCLUDE` projection type.

Each GSI adds write cost, because every table write that touches an indexed attribute also writes to the index.

## 122: How do you see how much capacity a request used?

Set `ReturnConsumedCapacity`:

- `TOTAL`: total capacity used
- `INDEXES`: the total plus a breakdown per table and index
- `NONE` (default)

```js
const res = await doc.send(
  new QueryCommand({
    TableName: "Orders",
    KeyConditionExpression: "customerId = :c",
    ExpressionAttributeValues: { ":c": "c-42" },
    ReturnConsumedCapacity: "TOTAL",
  }),
);
console.log(res.ConsumedCapacity);
```

This is very useful when you're trying to understand why something costs more than expected.

## 123: What affects DynamoDB latency?

- Item size and the number of items read
- Strongly consistent vs eventually consistent reads
- Distance between your app and the table's Region
- Network setup, like VPC endpoints vs the public internet
- SDK settings: HTTP keep-alive, connection reuse, timeouts
- Throttling and retries
- Transactions, which add some overhead

DynamoDB itself usually answers in single-digit milliseconds. Most of the extra latency in real apps comes from the client side.

## 124: What is the difference between the Dynamo paper and DynamoDB?

The Dynamo paper (2007) described an internal Amazon key-value store built for the shopping cart. It used leaderless replication, consistent hashing, vector clocks and sloppy quorums.

DynamoDB (2012) is a different, fully managed service inspired by the same ideas. It uses leader-based replication with Multi-Paxos within each partition, supports strongly consistent reads, and is offered as a service to everyone. They share a name and some ideas, but they are not the same system.

## 125: Is DynamoDB a key-value store or a document database?

Both. You access items by key like in a key-value store, but an item can hold nested maps and lists like a JSON document. You can read and update nested fields with document paths.

What it doesn't have is document-database querying by any nested field. You only query by keys and indexes.

## 126: What does a typical serverless stack with DynamoDB look like?

```text
Client -> API Gateway -> Lambda -> DynamoDB
                                     |
                                  Streams -> Lambda -> (email, search, analytics)
```

- API Gateway receives HTTP requests
- Lambda runs business logic and calls DynamoDB through the SDK
- DynamoDB stores the data
- DynamoDB Streams triggers other Lambdas for side effects

Everything scales to zero and you pay per use, which makes it popular for startups and spiky workloads.

## 127: How should you store files like images with DynamoDB?

Store the file in S3 and keep only the metadata and the S3 key in DynamoDB:

```json
{
  "photoId": "p-1",
  "userId": "u-1",
  "s3Key": "photos/u-1/p-1.jpg",
  "contentType": "image/jpeg",
  "size": 2483021,
  "uploadedAt": "2026-10-29T10:00:00Z"
}
```

This keeps items small, cheap and fast, and avoids the 400 KB limit. S3 is much cheaper for large blobs.

## 128: Are attribute names and values case-sensitive?

Yes, both. `Email` and `email` are different attributes, and `"Ana"` and `"ana"` are different values. A query for `email = 'Ana@Example.com'` won't find an item stored as `ana@example.com`.

For case-insensitive lookups, store a normalized copy, like `emailLower`, and query that.

## 129: How is item size calculated?

Item size is the sum of:

- The length of every attribute name in UTF-8 bytes
- The size of every value: strings in UTF-8 bytes, numbers about 1 byte per 2 digits plus 1, binary in raw bytes, booleans and nulls 1 byte
- A small overhead for maps, lists and sets

Because attribute names count, long names like `customerShippingAddressLine1` repeated in millions of items add real storage and capacity cost.

## 130: What data types can a primary key use?

Only scalar types: String, Number or Binary. You can't use a map, list, set or boolean as a key.

Limits:

- Partition key value: 1 to 2048 bytes
- Sort key value: 1 to 1024 bytes

Strings are the most common choice, because they let you build composite values like `USER#123`.

## 131: Why are scans expensive?

A scan reads every item in the table and charges read capacity for all of it, even with a filter. On a 100 GB table, one full scan reads 100 GB worth of data.

Scans also:

- Take a long time, since each page is at most 1 MB
- Can use up capacity and throttle normal traffic in provisioned mode
- Return data in no useful order

Use them for occasional jobs, not for user-facing requests.

## 132: How do you find an item by a non-key attribute?

Add a GSI on that attribute. Example: users are stored by `userId`, but login needs to find them by `email`:

```bash
aws dynamodb update-table \
  --table-name Users \
  --attribute-definitions AttributeName=email,AttributeType=S \
  --global-secondary-index-updates \
    '[{"Create":{"IndexName":"email-index","KeySchema":[{"AttributeName":"email","KeyType":"HASH"}],"Projection":{"ProjectionType":"ALL"}}}]'
```

Then query `email-index` with `email = :e`. For an on-demand table you don't set throughput on the index.

## 133: How do you decide between DynamoDB and RDS?

Pick **DynamoDB** when:

- Access patterns are known and key-based
- You need predictable latency at large scale
- Traffic is spiky or you want no servers to manage

Pick **RDS / Aurora** when:

- You need joins, ad hoc queries and reporting
- The data is highly relational and changes shape often
- The team knows SQL and the scale is moderate

Many systems use both: DynamoDB for high-traffic paths and a relational database for reporting or admin work.

## 134: How do you define a DynamoDB table in CloudFormation?

```yaml
Resources:
  OrdersTable:
    Type: AWS::DynamoDB::Table
    DeletionPolicy: Retain
    Properties:
      TableName: Orders
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: customerId
          AttributeType: S
        - AttributeName: orderDate
          AttributeType: S
      KeySchema:
        - AttributeName: customerId
          KeyType: HASH
        - AttributeName: orderDate
          KeyType: RANGE
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
      DeletionProtectionEnabled: true
```

`DeletionPolicy: Retain` keeps the table if the stack is deleted. There's also `AWS::DynamoDB::GlobalTable` for multi-Region tables.

## 135: How do you define a table with AWS CDK?

Use `TableV2`, the newer construct that also supports global tables:

```ts
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import { RemovalPolicy } from "aws-cdk-lib";

const table = new dynamodb.TableV2(this, "Orders", {
  partitionKey: { name: "pk", type: dynamodb.AttributeType.STRING },
  sortKey: { name: "sk", type: dynamodb.AttributeType.STRING },
  billing: dynamodb.Billing.onDemand(),
  pointInTimeRecoverySpecification: { pointInTimeRecoveryEnabled: true },
  deletionProtection: true,
  removalPolicy: RemovalPolicy.RETAIN,
});

table.grantReadWriteData(myLambda);
```

`grantReadWriteData` adds the right IAM permissions to the Lambda's role.

## 136: How do you define a table with Terraform?

```hcl
resource "aws_dynamodb_table" "orders" {
  name         = "Orders"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "customerId"
  range_key    = "orderDate"

  attribute {
    name = "customerId"
    type = "S"
  }

  attribute {
    name = "orderDate"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }

  deletion_protection_enabled = true
}
```

Only define `attribute` blocks for key attributes of the table and its indexes. Defining extra attributes causes an error.

## 137: How does the begins_with function work?

It checks whether a string or binary value starts with a given prefix. In a key condition it's only allowed on the sort key:

```text
KeyConditionExpression: pk = :pk AND begins_with(sk, :prefix)
```

You can also use it in filter and condition expressions on any string attribute. It's case-sensitive.

## 138: What other functions can you use in expressions?

- `attribute_exists(path)` / `attribute_not_exists(path)`
- `attribute_type(path, type)`, for example `attribute_type(age, :n)` with `:n = 'N'`
- `begins_with(path, substr)`
- `contains(path, operand)`: substring in a string, or element in a set or list
- `size(path)`: length of a string, binary, set, list or map

```text
FilterExpression: contains(tags, :t) AND size(comments) > :zero
```

These work in filter and condition expressions, not in key conditions (except `begins_with` on the sort key).

## 139: How do you use IN and BETWEEN in filters?

```js
new ScanCommand({
  TableName: "Products",
  FilterExpression: "category IN (:a, :b) AND price BETWEEN :min AND :max",
  ExpressionAttributeValues: {
    ":a": "books",
    ":b": "games",
    ":min": 10,
    ":max": 50,
  },
});
```

`IN` can take up to 100 values. `BETWEEN` includes both ends. `BETWEEN` also works in key conditions on the sort key, but `IN` doesn't.

## 140: What is import from S3?

A feature that creates a new DynamoDB table from data in S3. Supported formats are CSV, DynamoDB JSON and Amazon Ion, optionally compressed with GZIP or ZSTD.

It doesn't use write capacity on the table, so it's much cheaper and faster than writing items one by one with a script. The catch: it can only create a new table, not load data into an existing one.

## 141: What is export to S3?

A feature that copies a table's data to an S3 bucket in DynamoDB JSON or Amazon Ion format. It requires PITR to be on and doesn't use read capacity, so it doesn't affect your live traffic.

There are two types:

- **Full export**: a snapshot of the table at a point in time
- **Incremental export**: only the changes between two points in time

Exports are often used for analytics with Athena, Glue or Redshift.

## 142: What are common beginner mistakes with DynamoDB?

- Designing tables like SQL and then trying to join them
- Using `Scan` for normal queries
- Choosing a low-cardinality partition key like `status`
- Not handling `UnprocessedItems` in batch writes
- Thinking `FilterExpression` saves cost
- Forgetting pagination and only reading the first page
- Writing TTL values in milliseconds instead of seconds
- Storing large blobs instead of using S3
- Not turning on PITR and deletion protection in production

## 143: What does ScannedCount mean compared to Count?

- `ScannedCount`: how many items DynamoDB read before applying the filter
- `Count`: how many items matched and were returned

If `ScannedCount` is much bigger than `Count`, your filter is throwing away most of the data, and you're paying for reads you don't use. That's a sign you need a better key or an index.

## 144: How do you scan a table in the AWS CLI?

```bash
aws dynamodb scan \
  --table-name Products \
  --filter-expression "category = :c" \
  --expression-attribute-values '{":c":{"S":"books"}}' \
  --projection-expression "productId, title"
```

The CLI handles pagination by default and keeps fetching pages until it's done. Use `--max-items` to stop early, or `--no-paginate` to get only the first page.

## 145: How do you query a table with the AWS CLI?

```bash
aws dynamodb query \
  --table-name Orders \
  --key-condition-expression "customerId = :c AND begins_with(orderDate, :y)" \
  --expression-attribute-values '{":c":{"S":"c-42"},":y":{"S":"2026"}}' \
  --no-scan-index-forward
```

`--no-scan-index-forward` returns results in descending order. The CLI uses DynamoDB JSON for values, so each value needs a type like `S` or `N`.

## 146: What is a DynamoDB endpoint?

The HTTPS address the SDK sends requests to, for example `https://dynamodb.us-east-1.amazonaws.com`. Each Region has its own endpoint, and a table only exists in one Region (unless it's a global table).

You can reach it over the internet, through a VPC gateway endpoint, or through an interface endpoint (PrivateLink). For local development, you point the SDK to DynamoDB Local's endpoint instead.

## 147: What is the AWS console item explorer?

In the DynamoDB console, "Explore items" lets you browse a table, run `Query` and `Scan` with a form, edit items as JSON, and run PartiQL statements in the PartiQL editor.

It's useful for debugging and small fixes, but be careful in production. A full scan from the console costs read capacity just like one from code.

## 148: What does it mean that DynamoDB has no joins?

You can't combine two tables in one query like `SELECT ... JOIN`. If you need data from several entities together, you either:

- Store them in the same item collection so one `Query` returns them all
- Duplicate the data you need (denormalize)
- Make several requests and combine the results in code

This is why modeling starts from access patterns: you put together the data that's read together.

## 149: What is denormalization in DynamoDB?

Storing the same piece of data in more than one place so that reads are fast. For example, saving the customer's name inside each order item so you don't have to fetch the customer separately.

The cost is that updates are harder. If the customer changes their name, you have to decide whether old orders should change too, and if so, update them (often through Streams). For data that rarely changes, this trade-off is usually worth it.

## 150: What does a typical DynamoDB item for a user look like?

```json
{
  "pk": "USER#u-123",
  "sk": "PROFILE",
  "type": "User",
  "name": "Ana Smith",
  "email": "ana@example.com",
  "plan": "pro",
  "address": { "city": "Tbilisi", "country": "GE" },
  "createdAt": "2026-01-03T10:00:00Z",
  "updatedAt": "2026-10-29T10:00:00Z"
}
```

Generic key names like `pk` and `sk` with prefixes (`USER#`) are common, because they let you store different entity types in the same table later. The `type` attribute makes items easy to tell apart.

# Moderate Questions (151-300)

## 151: What is single-table design?

Single-table design means storing several entity types (users, orders, order items, payments) in one table, with generic key names like `pk` and `sk`. Related items share a partition key so that one `Query` can return them together.

| pk        | sk               | type      | data           |
| --------- | ---------------- | --------- | -------------- |
| USER#u-1  | PROFILE          | User      | name, email    |
| USER#u-1  | ORDER#2026-10-01 | Order     | total, status  |
| USER#u-1  | ORDER#2026-10-15 | Order     | total, status  |
| ORDER#o-9 | ITEM#1           | OrderItem | productId, qty |

The goal is to answer each access pattern with as few requests as possible, which gives you the "join" result without a join.

## 152: What are the trade-offs of single-table vs multi-table design?

Single-table pros:

- Fetch related data in one request
- Fewer tables to manage, monitor and back up
- Shared capacity in provisioned mode

Single-table cons:

- Harder to learn and read, especially for new team members
- Exports and analytics are messier, because many entity types are mixed
- Adding new access patterns later can be harder
- Per-entity settings (like different backup or stream needs) aren't possible

Multi-table design is simpler and is fine when entities are rarely read together. AWS's current guidance is to use single-table where it helps, not as a rule for everything.

## 153: How do you approach data modeling in DynamoDB?

1. Understand the domain and list the entities and their relationships.
2. Write down every access pattern: "get user by id", "list orders for user, newest first", "find order by id", and so on, with rough traffic numbers.
3. Design the primary key so that the most important patterns are a `GetItem` or a `Query`.
4. Add GSIs for the patterns the primary key can't serve.
5. Check each pattern against the model with sample data (NoSQL Workbench helps).
6. Check item sizes, hot keys and write costs.

The key difference from SQL is that the queries come first and the schema follows.

## 154: How do you model a one-to-many relationship?

The common way is to put the parent and its children in the same item collection:

| pk           | sk        |
| ------------ | --------- |
| CUSTOMER#c-1 | PROFILE   |
| CUSTOMER#c-1 | ORDER#o-1 |
| CUSTOMER#c-1 | ORDER#o-2 |

- Get the customer and all orders: `pk = CUSTOMER#c-1`
- Get only orders: `pk = CUSTOMER#c-1 AND begins_with(sk, 'ORDER#')`

Other options: store small, bounded children as a list or map inside the parent item, or use a GSI keyed by the parent id when the children live under their own keys.

## 155: How do you model a many-to-many relationship?

Use the adjacency list pattern: store each relationship as its own item, and add a GSI that flips the keys.

| pk          | sk        | GSI1PK (= sk) | GSI1SK (= pk) |
| ----------- | --------- | ------------- | ------------- |
| STUDENT#s-1 | CLASS#c-1 | CLASS#c-1     | STUDENT#s-1   |
| STUDENT#s-1 | CLASS#c-2 | CLASS#c-2     | STUDENT#s-1   |
| STUDENT#s-2 | CLASS#c-1 | CLASS#c-1     | STUDENT#s-2   |

- Classes for a student: query the table with `pk = STUDENT#s-1`
- Students in a class: query the GSI with `GSI1PK = CLASS#c-1`

You can copy a few useful attributes (like the class name) into the relationship items so you don't need extra lookups.

## 156: What is GSI overloading?

Using one GSI with generic key names (`GSI1PK`, `GSI1SK`) for several different access patterns. Each entity type puts different values in those attributes.

| Entity | GSI1PK         | GSI1SK            |
| ------ | -------------- | ----------------- |
| Order  | STATUS#PENDING | 2026-10-29T10:00Z |
| User   | EMAIL#a@x.com  | USER              |
| Ticket | AGENT#ag-7     | TICKET#2026-10-28 |

One index now serves "orders by status and date", "user by email" and "tickets by agent". It keeps the number of GSIs down, which saves cost and stays well under the GSI limit.

## 157: What is a sparse index and how do you use it?

A GSI where only some items have the index key, so only those items are in the index. Example: you want to list only orders that need review.

```js
// when an order needs review
UpdateExpression: "SET reviewPending = :ts";

// after review
UpdateExpression: "REMOVE reviewPending";
```

A GSI keyed on `reviewPending` contains only the pending orders. Querying or even scanning it is cheap, because the index is small. This works much better than a filter on a big table.

## 158: How do you use hierarchical sort keys?

Build the sort key from several levels joined by a separator, from broad to specific:

```text
sk = COUNTRY#GE#CITY#Tbilisi#STORE#s-42
```

Then `begins_with` lets you query at any level:

- `begins_with(sk, 'COUNTRY#GE')`: all stores in Georgia
- `begins_with(sk, 'COUNTRY#GE#CITY#Tbilisi')`: all stores in Tbilisi

The order of levels matters. You can only filter from the left, so put the levels you query by most often first.

## 159: Why do people use generic key names like pk and sk?

Because in single-table design the same key attribute holds different things for different entities: a user id, an order id, a date. A name like `userId` would be wrong for half the items.

Generic names also make it easier to add new entities and new GSI patterns later without changing the table. The downside is readability, so add a `type` attribute and keep the real fields (`userId`, `orderId`) as normal attributes too.

## 160: How do you model a user with orders and order items?

Access patterns:

1. Get user profile
2. List a user's orders, newest first
3. Get an order with its items
4. Get an order by id

| pk        | sk                   | GSI1PK    | GSI1SK |
| --------- | -------------------- | --------- | ------ |
| USER#u-1  | PROFILE              |           |        |
| USER#u-1  | ORDER#2026-10-29#o-9 | ORDER#o-9 | ORDER  |
| ORDER#o-9 | ITEM#p-1             |           |        |
| ORDER#o-9 | ITEM#p-2             |           |        |

- 1: `GetItem pk=USER#u-1, sk=PROFILE`
- 2: `Query pk=USER#u-1, begins_with(sk, 'ORDER#')`, `ScanIndexForward: false`
- 3: `Query pk=ORDER#o-9`
- 4: `Query GSI1 GSI1PK=ORDER#o-9`

Putting the date in the order sort key gives you the newest-first list for free.

## 161: How do you keep a version history of an item?

A common pattern uses a "v0" item as the latest copy, plus one item per version:

| pk      | sk  | version | content |
| ------- | --- | ------- | ------- |
| DOC#d-1 | v0  | 3       | latest  |
| DOC#d-1 | v1  | 1       | ...     |
| DOC#d-1 | v2  | 2       | ...     |
| DOC#d-1 | v3  | 3       | latest  |

On every change, use a transaction to write the new version item and update `v0` with a condition on the current version number. Reading the latest is a single `GetItem` on `v0`, and the full history is a `Query` on the partition key. Zero-pad version numbers (`v0003`) if you want them to sort correctly as strings.

## 162: How do you implement optimistic locking?

Keep a version number on the item. Read the item, change it, and write it back only if the version hasn't changed:

```js
const { Item } = await doc.send(
  new GetCommand({ TableName: "Docs", Key: { id } }),
);

await doc.send(
  new UpdateCommand({
    TableName: "Docs",
    Key: { id },
    UpdateExpression: "SET content = :c, version = :next",
    ConditionExpression: "version = :current",
    ExpressionAttributeValues: {
      ":c": newContent,
      ":current": Item.version,
      ":next": Item.version + 1,
    },
  }),
);
```

If someone else saved first, you get `ConditionalCheckFailedException`. You can then reload and retry, or show a conflict to the user.

## 163: How can you build a distributed lock with DynamoDB?

Write a lock item with a condition that it doesn't exist or has expired:

```js
const now = Date.now();

await doc.send(
  new PutCommand({
    TableName: "Locks",
    Item: {
      lockId: "job-daily-report",
      owner: workerId,
      expiresAt: now + 30_000,
      ttl: Math.floor(now / 1000) + 3600,
    },
    ConditionExpression: "attribute_not_exists(lockId) OR expiresAt < :now",
    ExpressionAttributeValues: { ":now": now },
  }),
);
```

Release it with a conditional delete (`owner = :me`). The lease time is important, so a crashed worker doesn't hold the lock forever. The `ttl` attribute just cleans up old lock items. Note that clock differences between workers can affect lease timing.

## 164: How do you make writes idempotent?

Use a client-generated id and a condition, so that the same request done twice has the same effect as doing it once:

```js
await doc.send(
  new PutCommand({
    TableName: "Payments",
    Item: { paymentId: requestId, amount: 100, status: "CREATED" },
    ConditionExpression: "attribute_not_exists(paymentId)",
  }),
);
```

If the client retries after a timeout, the second write fails with `ConditionalCheckFailedException`, which you treat as success. For transactions, pass a `ClientRequestToken`. For Lambda handlers, Powertools for AWS Lambda has an idempotency utility that stores records in DynamoDB.

## 165: How do you enforce uniqueness on a non-key attribute, like email?

DynamoDB only enforces unique primary keys. To make email unique, write a second item where the email is the key, in the same transaction:

```js
await doc.send(
  new TransactWriteCommand({
    TransactItems: [
      {
        Put: {
          TableName: "App",
          Item: { pk: `USER#${userId}`, sk: "PROFILE", email },
          ConditionExpression: "attribute_not_exists(pk)",
        },
      },
      {
        Put: {
          TableName: "App",
          Item: { pk: `EMAIL#${email.toLowerCase()}`, sk: "EMAIL", userId },
          ConditionExpression: "attribute_not_exists(pk)",
        },
      },
    ],
  }),
);
```

If either item already exists, the whole transaction fails. When the email changes, delete the old email item and create the new one in another transaction.

## 166: How do you store time-series data?

Typical design: partition key is the source (device, metric, user) plus a time bucket, and the sort key is the timestamp.

```text
pk = DEVICE#d-1#2026-10-29
sk = 2026-10-29T10:15:30.123Z
```

The time bucket (day, hour) keeps item collections from growing forever and spreads writes. Use TTL to drop old data automatically. Some teams also create one table per time period (for example monthly) so old tables can be switched to lower capacity or Standard-IA, or exported and deleted.

## 167: How do you build a leaderboard?

For a single game or small board, use a GSI with a fixed partition key and the score as the sort key:

| pk         | sk     | GSI1PK | GSI1SK (score) |
| ---------- | ------ | ------ | -------------- |
| PLAYER#p-1 | GAME#g | GAME#g | 9800           |
| PLAYER#p-2 | GAME#g | GAME#g | 12000          |

Query `GSI1PK = GAME#g` with `ScanIndexForward: false, Limit: 10` for the top 10. Store scores as Numbers, or as zero-padded strings if you combine them with other values.

If one game has huge write traffic, that GSI partition becomes hot. Then you shard the leaderboard or keep the top N in a cache like ElastiCache.

## 168: How do you keep counts and totals without scanning?

Keep the aggregate in its own item and update it as data changes:

- In the same write, using a transaction (exact but costs more)
- From DynamoDB Streams with a Lambda that updates the counter (cheaper, eventually consistent)

```js
// stream handler
for (const record of event.Records) {
  if (record.eventName === "INSERT") {
    await doc.send(
      new UpdateCommand({
        TableName: "App",
        Key: { pk: "STATS", sk: "ORDERS" },
        UpdateExpression: "ADD orderCount :one",
        ExpressionAttributeValues: { ":one": 1 },
      }),
    );
  }
}
```

Lambda can deliver the same stream batch more than once, so expect occasional double counting, or store processed event ids to skip duplicates.

## 169: How do you implement pagination for an API?

Return `LastEvaluatedKey` to the client as an opaque cursor, and accept it back on the next request:

```js
const encode = (key) =>
  key && Buffer.from(JSON.stringify(key)).toString("base64url");
const decode = (cursor) =>
  cursor && JSON.parse(Buffer.from(cursor, "base64url").toString());

const res = await doc.send(
  new QueryCommand({
    TableName: "Orders",
    KeyConditionExpression: "customerId = :c",
    ExpressionAttributeValues: { ":c": customerId },
    Limit: 20,
    ExclusiveStartKey: decode(req.query.cursor),
  }),
);

return { items: res.Items, nextCursor: encode(res.LastEvaluatedKey) };
```

Validate or sign the cursor if you don't want clients to tamper with it, and check that it belongs to the same partition key they're allowed to read.

## 170: Why can Limit with a FilterExpression return fewer items than expected?

Because `Limit` is applied before the filter. With `Limit: 20` DynamoDB reads 20 items, then the filter removes some. You might get 3 items, or 0, and still have a `LastEvaluatedKey`.

If you need exactly N matching items, keep querying pages until you have N or there's no more data. A better fix is to move the filtered condition into a key or a sparse index, so you don't have to filter at all.

## 171: What is a parallel scan?

A way to split a scan into segments that run at the same time. You choose `TotalSegments`, and each worker scans one `Segment`:

```js
const totalSegments = 4;

const results = await Promise.all(
  Array.from({ length: totalSegments }, async (_, segment) => {
    const items = [];
    let lastKey;
    do {
      const page = await doc.send(
        new ScanCommand({
          TableName: "Logs",
          Segment: segment,
          TotalSegments: totalSegments,
          ExclusiveStartKey: lastKey,
        }),
      );
      items.push(...page.Items);
      lastKey = page.LastEvaluatedKey;
    } while (lastKey);
    return items;
  }),
);
```

It finishes large scans much faster, but it also uses capacity much faster, so it can throttle live traffic. For full-table analytics, export to S3 is usually the better choice.

## 172: How do you use paginators in SDK v3?

`lib-dynamodb` has `paginateQuery` and `paginateScan`, which handle `LastEvaluatedKey` for you:

```js
import { paginateQuery } from "@aws-sdk/lib-dynamodb";

const paginator = paginateQuery(
  { client: doc, pageSize: 100 },
  {
    TableName: "Orders",
    KeyConditionExpression: "customerId = :c",
    ExpressionAttributeValues: { ":c": "c-42" },
  },
);

for await (const page of paginator) {
  for (const item of page.Items ?? []) {
    console.log(item);
  }
}
```

`pageSize` sets the `Limit` per request.

## 173: How do you write a reliable batch write with retries?

Split items into chunks of 25, and retry `UnprocessedItems` with backoff:

```js
import { BatchWriteCommand } from "@aws-sdk/lib-dynamodb";

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function batchPut(table, items) {
  for (let i = 0; i < items.length; i += 25) {
    let request = {
      [table]: items.slice(i, i + 25).map((Item) => ({ PutRequest: { Item } })),
    };

    for (let attempt = 0; request && Object.keys(request).length; attempt++) {
      if (attempt > 0)
        await sleep(Math.min(2 ** attempt * 50, 5000) * Math.random());
      const res = await doc.send(
        new BatchWriteCommand({ RequestItems: request }),
      );
      request = res.UnprocessedItems;
      if (attempt > 8) throw new Error("Too many retries");
    }
  }
}
```

Don't put the same key twice in one batch, or the whole request fails with a `ValidationException`.

## 174: How does batch_writer work in boto3?

It buffers your writes, sends them in batches of 25, and resends unprocessed items for you:

```python
import boto3

table = boto3.resource("dynamodb").Table("Products")

with table.batch_writer(overwrite_by_pkeys=["productId"]) as batch:
    for product in products:
        batch.put_item(Item=product)
```

`overwrite_by_pkeys` removes duplicate keys inside a buffer, so you don't get validation errors when the same item is written twice.

## 175: What are the limits and costs of transactions?

- Up to 100 actions per transaction
- Up to 4 MB total size
- Items must be in the same AWS account and Region
- You can't target the same item twice in one transaction
- Each item costs twice the normal capacity (2 WCU per KB for writes, 2 RCU per 4 KB for reads)

Use transactions when you need all-or-nothing behavior, not as the default way to write. Most writes don't need them.

## 176: How do you find out why a transaction failed?

When a transaction fails, you get `TransactionCanceledException` with a `CancellationReasons` array, one entry per action, in order:

```js
import { TransactionCanceledException } from "@aws-sdk/client-dynamodb";

try {
  await doc.send(transactCommand);
} catch (err) {
  if (err instanceof TransactionCanceledException) {
    err.CancellationReasons?.forEach((reason, i) => {
      console.log(i, reason.Code, reason.Message);
    });
  }
  throw err;
}
```

Codes include `None` (that action was fine), `ConditionalCheckFailed`, `TransactionConflict`, `ItemCollectionSizeLimitExceeded`, `ProvisionedThroughputExceeded`, `ThrottlingError` and `ValidationError`. You can set `ReturnValuesOnConditionCheckFailure: 'ALL_OLD'` on an action to see the current item in the reason.

## 177: What does ClientRequestToken do in a transaction?

It makes `TransactWriteItems` idempotent. If you send the same request with the same token within 10 minutes, DynamoDB doesn't run it again. It returns success without writing twice.

```js
new TransactWriteCommand({
  ClientRequestToken: orderId,
  TransactItems: [...],
});
```

This matters because the SDK can retry a request after a timeout even if the first attempt actually succeeded. If you reuse a token with different parameters, you get an `IdempotentParameterMismatchException`.

## 178: What is a ConditionCheck in a transaction?

An action that checks a condition on an item without changing it. If the condition fails, the whole transaction is cancelled.

```js
{
  ConditionCheck: {
    TableName: 'Users',
    Key: { userId: 'u-1' },
    ConditionExpression: 'accountStatus = :active',
    ExpressionAttributeValues: { ':active': 'ACTIVE' },
  },
}
```

Example: only create an order if the user's account is active. The user item isn't written, but it's protected from changes during the transaction.

## 179: What is a transaction conflict?

A conflict happens when two operations try to change the same item at the same time and at least one of them is a transaction. For example, a `PutItem` on an item that's part of an ongoing `TransactWriteItems`.

The transaction is then cancelled with `TransactionConflict` in the cancellation reasons, or the non-transactional write fails with `TransactionConflictException`. The SDK doesn't fully retry these for you in every case, so handle them with retries and backoff. Lots of conflicts mean too many writers on the same items.

## 180: How do you connect DynamoDB Streams to a Lambda function?

1. Enable a stream on the table (for example `NEW_AND_OLD_IMAGES`).
2. Create an event source mapping from the stream ARN to the Lambda function.
3. Give the function's role permission to read the stream (`dynamodb:GetRecords`, `GetShardIterator`, `DescribeStream`, `ListStreams`).

```js
import { unmarshall } from "@aws-sdk/util-dynamodb";

export const handler = async (event) => {
  for (const record of event.Records) {
    const newItem =
      record.dynamodb.NewImage && unmarshall(record.dynamodb.NewImage);
    const oldItem =
      record.dynamodb.OldImage && unmarshall(record.dynamodb.OldImage);
    console.log(record.eventName, oldItem, newItem);
  }
};
```

`eventName` is `INSERT`, `MODIFY` or `REMOVE`.

## 181: What event source mapping settings matter for DynamoDB Streams?

- `BatchSize`: records per invocation (up to 10,000)
- `MaximumBatchingWindowInSeconds`: wait to collect more records before invoking
- `StartingPosition`: `LATEST` or `TRIM_HORIZON`
- `MaximumRetryAttempts` and `MaximumRecordAgeInSeconds`: when to give up on a failing batch
- `BisectBatchOnFunctionError`: split a failing batch in two to find the bad record
- `DestinationConfig.OnFailure`: send details of failed batches to SQS or SNS
- `ParallelizationFactor`: up to 10 concurrent batches per shard
- `FunctionResponseTypes: ['ReportBatchItemFailures']`: report partial failures
- `FilterCriteria`: only invoke for matching records

The defaults retry forever until the records expire, which can block the shard for up to 24 hours. Always set retry limits and a failure destination.

## 182: How do you report partial batch failures from a stream handler?

Enable `ReportBatchItemFailures` on the event source mapping, and return the sequence number of the first failed record. Lambda then retries from that record instead of the whole batch.

```js
export const handler = async (event) => {
  for (const record of event.Records) {
    try {
      await processRecord(record);
    } catch (err) {
      return {
        batchItemFailures: [{ itemIdentifier: record.dynamodb.SequenceNumber }],
      };
    }
  }
  return { batchItemFailures: [] };
};
```

Stop at the first failure and return it, so records stay in order.

## 183: How do you filter stream events before they reach Lambda?

Add `FilterCriteria` to the event source mapping. Lambda drops records that don't match, and you don't pay for those invocations.

```json
{
  "Filters": [
    {
      "Pattern": "{\"eventName\":[\"INSERT\"],\"dynamodb\":{\"NewImage\":{\"type\":{\"S\":[\"Order\"]}}}}"
    }
  ]
}
```

This runs the function only for new `Order` items. Patterns use the DynamoDB JSON format of the stream record. It's very useful in single-table designs, where one stream carries many entity types.

## 184: What ordering does DynamoDB Streams guarantee?

- Each change appears in the stream exactly once
- Changes to the same item appear in the order they happened
- There's no global order across different items or partitions

Lambda processes one batch per shard at a time by default, which keeps per-item order. With `ParallelizationFactor` above 1, Lambda still keeps order for records with the same partition key.

## 185: What is the difference between DynamoDB Streams and Kinesis Data Streams for DynamoDB?

| Feature      | DynamoDB Streams                        | Kinesis Data Streams for DynamoDB |
| ------------ | --------------------------------------- | --------------------------------- |
| Retention    | 24 hours                                | Up to 365 days                    |
| Duplicates   | No                                      | Possible                          |
| Order        | Kept per item                           | Not guaranteed, use timestamps    |
| Consumers    | About 2 per shard (1 for global tables) | Many, including enhanced fan-out  |
| Integrations | Lambda, KCL adapter                     | Lambda, Firehose, Flink, KCL      |
| Cost         | Free for Lambda triggers                | Kinesis pricing                   |

Use DynamoDB Streams for normal triggers. Use Kinesis when you need longer retention, many consumers, or to send data to Firehose and analytics tools.

## 186: How do you archive expired items to S3?

Enable TTL and a stream with `OLD_IMAGE` or `NEW_AND_OLD_IMAGES`. When TTL deletes an item, the delete appears in the stream. A Lambda (or Firehose through Kinesis) writes the old image to S3.

```js
export const handler = async (event) => {
  const expired = event.Records.filter(
    (r) =>
      r.eventName === "REMOVE" &&
      r.userIdentity?.type === "Service" &&
      r.userIdentity?.principalId === "dynamodb.amazonaws.com",
  );
  // write unmarshall(r.dynamodb.OldImage) to S3
};
```

The `userIdentity` check makes sure you only archive TTL deletes, not deletes made by users.

## 187: What should you keep in mind when using TTL?

- The attribute must be a Number with epoch time in seconds
- Deletion is not instant. It usually happens within a few days of expiry
- Expired items can still show up in reads until they're deleted, so filter them: `expiresAt > :now`
- Items with a TTL far in the past (more than five years) aren't deleted
- TTL deletes are free and replicated to global table replicas
- TTL deletes appear in streams, so stream consumers must handle them

Don't use TTL for anything that needs exact timing, like expiring a coupon at a precise second. Check the time in your code too.

## 188: When should you use DAX?

When you have a read-heavy workload with the same items read many times, and you need microsecond reads or want to cut read costs. Examples: product pages during a sale, configuration data, game state.

DAX is not a good fit when:

- Writes are heavy and reads are rare
- You need strongly consistent reads
- Your app isn't in a VPC
- Your access is mostly scans or unique queries that won't hit the cache

## 189: What caches does DAX have?

- **Item cache**: stores results of `GetItem` and `BatchGetItem` by primary key
- **Query cache**: stores results of `Query` and `Scan`, keyed by the exact request parameters

Each has its own TTL (default 5 minutes). Writes through DAX update the item cache, but they don't update the query cache. So a query can return old results until its cache entry expires. Set the query cache TTL short if that matters.

## 190: How does consistency work with DAX?

- Eventually consistent reads are served from the cache
- Strongly consistent reads and transactional reads go straight to DynamoDB, and the results aren't cached
- Writes go to DynamoDB first, and then DAX updates its item cache (write-through)

If something writes directly to DynamoDB without going through DAX, the cache isn't updated until the item's TTL expires. All writers should use the DAX client if you depend on the item cache being fresh.

## 191: How is DAX different from ElastiCache?

- **DAX** speaks the DynamoDB API, so you don't change your data access code. It only caches DynamoDB, and it handles write-through for you.
- **ElastiCache (Valkey, Redis OSS or Memcached)** is a general cache. You decide what to cache, how to invalidate it, and you write cache logic yourself. It also gives you data structures like sorted sets, pub/sub and so on.

Pick DAX for simple DynamoDB read caching. Pick ElastiCache when you cache data from several sources, need special data structures, or want full control.

## 192: How do you configure auto scaling for a provisioned table?

With the CLI it takes two steps for each dimension (reads and writes):

```bash
aws application-autoscaling register-scalable-target \
  --service-namespace dynamodb \
  --resource-id table/Orders \
  --scalable-dimension dynamodb:table:WriteCapacityUnits \
  --min-capacity 10 --max-capacity 1000

aws application-autoscaling put-scaling-policy \
  --service-namespace dynamodb \
  --resource-id table/Orders \
  --scalable-dimension dynamodb:table:WriteCapacityUnits \
  --policy-name orders-wcu \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration \
    '{"TargetValue":70.0,"PredefinedMetricSpecification":{"PredefinedMetricType":"DynamoDBWriteCapacityUtilization"}}'
```

Do the same for each GSI (`index/IndexName`). A GSI without auto scaling can throttle the table's writes.

## 193: How do you choose between on-demand and provisioned capacity?

On-demand is good for:

- New apps where traffic is unknown
- Spiky or unpredictable traffic
- Low or occasional traffic
- Teams that don't want to manage capacity

Provisioned is good for:

- Steady, predictable traffic with high usage most of the day
- Large workloads where reserved capacity gives big savings

Since the on-demand price cut in late 2024, on-demand is the right default for most tables. Switch to provisioned only when the numbers clearly show savings.

## 194: Can you switch between capacity modes?

Yes, with `UpdateTable`. Switching from provisioned to on-demand can be done a limited number of times in a 24-hour window. Switching from on-demand to provisioned can be done at any time. The switch takes effect without downtime.

When you switch to provisioned, set capacity (or auto scaling) that matches your current peak, or you'll get throttled right after the change.

## 195: What is reserved capacity?

A way to save money on provisioned capacity by committing to a certain number of RCUs and WCUs for one or three years, with an upfront payment. The savings can be large compared to normal provisioned pricing.

It only applies to provisioned mode in the Standard table class, in one Region. It's worth it for stable, long-running workloads where you're sure of the minimum capacity you'll use.

## 196: What is burst capacity?

In provisioned mode, DynamoDB keeps up to 300 seconds of unused read and write capacity. When traffic briefly goes above your provisioned level, it uses this saved capacity before throttling.

It helps with short spikes, but you can't count on it. DynamoDB may also use it for background work. Design for your real peak, not for burst.

## 197: What is adaptive capacity?

A feature that lets DynamoDB give more of the table's throughput to busy partitions, as long as the table total isn't exceeded. It's on automatically for every table.

It also isolates frequently accessed items. If one item gets a lot of traffic, DynamoDB can split partitions so that item gets more room. It helps with uneven traffic, but it can't make a single partition key go above the per-partition limits (3,000 RCU and 1,000 WCU per second).

## 198: What is warm throughput?

Warm throughput shows how many reads and writes per second a table or GSI can handle right away, without having to scale up first. You can see it in `DescribeTable`, and you can raise it ahead of time ("pre-warm").

```bash
aws dynamodb update-table \
  --table-name Orders \
  --warm-throughput ReadUnitsPerSecond=50000,WriteUnitsPerSecond=20000
```

It's useful before a known big event, like a product launch or a sale, so the table is ready for the traffic on day one. Pre-warming has a one-time cost.

## 199: How do you limit the maximum throughput of an on-demand table?

Set `OnDemandThroughput` with a maximum number of read and write request units per second:

```bash
aws dynamodb update-table \
  --table-name Orders \
  --on-demand-throughput MaxReadRequestUnits=10000,MaxWriteRequestUnits=5000
```

Requests above the limit are throttled. It protects you from runaway costs (like a bug that loops writes) and from overwhelming downstream services. You can set it on GSIs too.

## 200: What happens when a GSI is throttled?

If a GSI doesn't have enough write capacity to keep up, writes to the base table that need to update that GSI are throttled too. This is called back pressure. The table can look healthy in its own metrics, but writes still fail.

So in provisioned mode, give every GSI enough write capacity (at least as much as the table for the writes that touch it) and turn on auto scaling for it. Check `WriteThrottleEvents` on each index, not just the table.

## 201: What does it mean that GSIs are eventually consistent?

When you write to the table, DynamoDB updates the GSI asynchronously, usually within a fraction of a second. A query on the GSI right after the write might not see it yet, or might still see the old value.

So:

- Don't read from a GSI right after writing and expect the new value
- Don't use a GSI to check uniqueness
- If you need the newest data, read from the table with a strongly consistent `GetItem` or `Query`

## 202: What happens when you add a GSI to an existing table?

DynamoDB creates the index and backfills it by reading all existing items and writing the ones that have the index keys. During the backfill:

- The table stays fully available
- The index status is `CREATING` and you can't query it yet
- Backfill writes cost write capacity on the index
- For large tables it can take a long time

Items with key attributes of the wrong type are skipped and reported as violations. You can check for them with the `IndexStatus` and `Backfilling` fields in `DescribeTable`.

## 203: How do you choose a projection type for a GSI?

- **KEYS_ONLY**: smallest and cheapest. Good when you only need ids and will fetch full items, or when you only check existence.
- **INCLUDE**: project just the attributes the query shows, like `title` and `price` for a list page.
- **ALL**: simplest, no extra fetches, but doubles storage and write cost for those items.

Think about how the index is read. If a list page needs five fields, `INCLUDE` those five. Fetching 50 items from the table after each index query is slower and often more expensive than projecting them.

## 204: What is the 10 GB limit with local secondary indexes?

If a table has at least one LSI, the total size of an item collection (all items with the same partition key, plus their LSI entries) can't go above 10 GB. Once it does, writes to that partition key fail with `ItemCollectionSizeLimitExceededException`.

Tables without LSIs don't have this limit. Because of it, and because LSIs can't be added later, most designs use GSIs and only use LSIs when strongly consistent reads on an alternate sort key are really needed.

## 205: What are multi-attribute composite keys in GSIs?

Since November 2025, a GSI can use up to four attributes for its partition key and up to four for its sort key. Before that, you had to build a synthetic attribute like `GSI1SK = STATUS#SHIPPED#2026-10-29` in your code.

```js
GlobalSecondaryIndexes: [
  {
    IndexName: "tenant-status-date",
    KeySchema: [
      { AttributeName: "tenantId", KeyType: "HASH" },
      { AttributeName: "region", KeyType: "HASH" },
      { AttributeName: "status", KeyType: "RANGE" },
      { AttributeName: "createdAt", KeyType: "RANGE" },
    ],
    Projection: { ProjectionType: "ALL" },
  },
];
```

Each attribute keeps its own type. When you query, you give equality on all partition key attributes and you can't skip sort key attributes in the middle. A range condition is only allowed on the last sort key attribute you use. Items missing any key attribute aren't indexed.

## 206: How do you handle items that might go over 400 KB?

- Move large fields (files, long text, big JSON) to S3 and keep a pointer
- Compress large text attributes with gzip and store them as Binary
- Split the item into several items under the same partition key (vertical partitioning)
- Cap lists that grow forever, and move old entries to separate items
- Shorten attribute names if there are many of them

Don't wait for the `ValidationException`. Know which entities can grow and design them that way from the start.

## 207: What is vertical partitioning of an item?

Splitting one big logical item into several smaller items with the same partition key, by how they're accessed:

| pk        | sk        | data                  |
| --------- | --------- | --------------------- |
| PRODUCT#1 | META      | name, price, stock    |
| PRODUCT#1 | DESC      | long description      |
| PRODUCT#1 | REVIEWS#1 | first page of reviews |

Reading `META` is cheap and fast for list pages. You fetch `DESC` only on the detail page. Updating `stock` only rewrites the small `META` item, so writes cost less.

## 208: What is ReturnValuesOnConditionCheckFailure?

An option on `PutItem`, `UpdateItem`, `DeleteItem` (and on actions in transactions) that returns the current item when the condition fails. Set it to `ALL_OLD`.

```js
try {
  await doc.send(
    new UpdateCommand({
      TableName: "Docs",
      Key: { id },
      UpdateExpression: "SET content = :c, version = :next",
      ConditionExpression: "version = :current",
      ExpressionAttributeValues: { ":c": content, ":current": 3, ":next": 4 },
      ReturnValuesOnConditionCheckFailure: "ALL_OLD",
    }),
  );
} catch (err) {
  if (err.name === "ConditionalCheckFailedException") {
    console.log("Current item:", err.Item);
  }
}
```

It saves an extra `GetItem` after a failed optimistic lock, and it doesn't use extra read capacity. The returned item can be in DynamoDB JSON format, so run it through `unmarshall` if needed.

## 209: How do you handle DynamoDB errors in SDK v3?

Errors are classes exported from `@aws-sdk/client-dynamodb`. Check them with `instanceof` or by `err.name`:

```js
import {
  ConditionalCheckFailedException,
  ResourceNotFoundException,
} from "@aws-sdk/client-dynamodb";

try {
  await doc.send(command);
} catch (err) {
  if (err instanceof ConditionalCheckFailedException) {
    // business rule failed
  } else if (err instanceof ResourceNotFoundException) {
    // wrong table name or Region
  } else {
    console.error(err.name, err.$metadata?.requestId);
    throw err;
  }
}
```

Log `$metadata.requestId`. AWS Support asks for it when you open a case.

## 210: How do you tune timeouts in the SDK v3 client?

Set them on the HTTP handler. The defaults can be too long for an API that should fail fast:

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { NodeHttpHandler } from "@smithy/node-http-handler";

const client = new DynamoDBClient({
  maxAttempts: 3,
  requestHandler: new NodeHttpHandler({
    connectionTimeout: 1000,
    requestTimeout: 2000,
  }),
});
```

Keep the request timeout well under your Lambda or API timeout, so retries have time to happen.

## 211: Why should you create the DynamoDB client outside the Lambda handler?

Code outside the handler runs once per execution environment, and the result is reused for every invocation. If you create the client inside the handler, each request sets up a new client and possibly new TLS connections, which adds latency.

```js
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const doc = DynamoDBDocumentClient.from(new DynamoDBClient({}));

export const handler = async (event) => {
  const { Item } = await doc.send(
    new GetCommand({ TableName: process.env.TABLE, Key: { id: event.id } }),
  );
  return Item;
};
```

SDK v3 in Node.js uses HTTP keep-alive by default, so connections are reused across invocations too.

## 212: What marshalling options does the Document Client have?

```js
const doc = DynamoDBDocumentClient.from(client, {
  marshallOptions: {
    removeUndefinedValues: true,
    convertEmptyValues: false,
    convertClassInstanceToMap: true,
  },
  unmarshallOptions: {
    wrapNumbers: false,
  },
});
```

- `removeUndefinedValues`: drop `undefined` fields instead of throwing an error
- `convertEmptyValues`: turn empty strings, binary and sets into `NULL` (rarely needed now)
- `convertClassInstanceToMap`: allow class instances, like objects created with `new`
- `wrapNumbers`: return numbers as `NumberValue` to avoid precision loss

`removeUndefinedValues: true` is something almost every project ends up turning on.

## 213: How do you handle large numbers in JavaScript?

JavaScript numbers are safe only up to 2^53 - 1. DynamoDB supports 38 digits. If you read a bigger number into a normal JS number, you lose precision.

Options:

- Store big ids as strings, which is the simplest fix
- Use `wrapNumbers: true`, so numbers come back as `NumberValue` objects that keep the exact string
- Pass `BigInt` values when writing

```js
import { NumberValue } from '@aws-sdk/lib-dynamodb';

Item: { id: 'x', big: NumberValue.from('123456789012345678901234567890') }
```

## 214: How do you write sets with the Document Client?

Pass a JavaScript `Set`. The Document Client turns a set of strings into SS, numbers into NS, and binary into BS:

```js
await doc.send(
  new PutCommand({
    TableName: "Posts",
    Item: { postId: "p-1", tags: new Set(["aws", "dynamodb"]) },
  }),
);
```

When you read it back, you get a `Set`, not an array. `JSON.stringify` turns a `Set` into `{}`, so convert it with `[...item.tags]` before sending it in an API response. An empty `Set` isn't allowed.

## 215: How do you test against DynamoDB Local in CI?

Run it as a service container and create tables before the tests:

```yaml
# GitHub Actions
services:
  dynamodb:
    image: amazon/dynamodb-local
    ports:
      - 8000:8000
```

```js
// test setup
const client = new DynamoDBClient({
  endpoint: process.env.DYNAMODB_ENDPOINT ?? "http://localhost:8000",
  region: "local",
  credentials: { accessKeyId: "local", secretAccessKey: "local" },
});

await client.send(new CreateTableCommand(tableDefinition));
```

Create a fresh table per test file (or use unique key prefixes) so tests don't step on each other. Testcontainers is another common way to start it from inside the test code.

## 216: How do you mock DynamoDB in unit tests?

Use `aws-sdk-client-mock`, which works with SDK v3 commands:

```js
import { mockClient } from "aws-sdk-client-mock";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

const ddbMock = mockClient(DynamoDBDocumentClient);

beforeEach(() => ddbMock.reset());

test("returns the user", async () => {
  ddbMock.on(GetCommand, { Key: { userId: "u-1" } }).resolves({
    Item: { userId: "u-1", name: "Ana" },
  });

  const user = await getUser("u-1");
  expect(user.name).toBe("Ana");
});
```

Mocks are fast but don't check your expressions. Combine them with some integration tests against DynamoDB Local.

## 217: How do you handle schema changes in DynamoDB?

Since there's no fixed schema, you handle changes in code:

- **Add attributes**: just start writing them. Old items don't have them, so treat missing as a default.
- **Rename or change format**: read both old and new shapes, write the new shape, and migrate old items over time (lazily on read, or with a backfill script).
- **New access pattern**: add a GSI. If it needs a new attribute, backfill that attribute.
- Keep a `schemaVersion` attribute on items if formats change often.

Big changes to the primary key need a new table and a data migration.

## 218: How do you backfill a new attribute for existing items?

Scan the table (parallel scan for big tables) and update each item, ideally with a condition so you don't overwrite newer data:

```js
for await (const page of paginateScan({ client: doc }, { TableName: "App" })) {
  for (const item of page.Items) {
    if (item.type !== "Order" || item.GSI2PK) continue;
    await doc.send(
      new UpdateCommand({
        TableName: "App",
        Key: { pk: item.pk, sk: item.sk },
        UpdateExpression: "SET GSI2PK = :v",
        ConditionExpression:
          "attribute_exists(pk) AND attribute_not_exists(GSI2PK)",
        ExpressionAttributeValues: { ":v": `STATUS#${item.status}` },
      }),
    );
  }
}
```

Throttle the script so it doesn't hurt live traffic. Make sure the app code already writes the new attribute before you start, or new items will be missed.

## 219: What libraries help with DynamoDB modeling in Node.js?

- **ElectroDB**: entity and service definitions for single-table design, builds keys and queries for you
- **DynamoDB Toolbox**: schemas, entities and type-safe commands on top of the Document Client
- **Dynamoose**: Mongoose-like models and schemas
- **OneTable**: single-table library with schema validation

They help with key building, validation and TypeScript types. They don't remove the need to understand access patterns, because the generated requests are still `Query`, `GetItem` and so on.

## 220: Example of an ElectroDB entity?

```js
import { Entity } from "electrodb";

const Order = new Entity(
  {
    model: { entity: "order", version: "1", service: "shop" },
    attributes: {
      orderId: { type: "string", required: true },
      customerId: { type: "string", required: true },
      status: { type: ["PENDING", "PAID", "SHIPPED"], required: true },
      createdAt: { type: "string", default: () => new Date().toISOString() },
    },
    indexes: {
      byOrder: {
        pk: { field: "pk", composite: ["orderId"] },
        sk: { field: "sk", composite: [] },
      },
      byCustomer: {
        index: "gsi1",
        pk: { field: "gsi1pk", composite: ["customerId"] },
        sk: { field: "gsi1sk", composite: ["createdAt"] },
      },
    },
  },
  { client: doc, table: "App" },
);

const { data } = await Order.query.byCustomer({ customerId: "c-42" }).go();
```

ElectroDB builds the `pk`/`sk` strings, validates attributes and handles pagination.

## 221: What are the pitfalls of using PartiQL?

- A `SELECT` without an equality condition on the partition key turns into a full table scan, and it doesn't warn you
- `WHERE` conditions on non-key attributes act like filters, so you still pay for all items read
- It looks like SQL, which makes people expect joins, `GROUP BY` or `ORDER BY` on any column, which aren't supported
- `UPDATE` and `DELETE` work on one item at a time and need the full primary key

You can block accidental scans with an IAM policy that denies `dynamodb:PartiQLSelect` unless `dynamodb:FullTableScan` is false.

## 222: How do you run transactions and batches with PartiQL?

```js
import { ExecuteTransactionCommand } from "@aws-sdk/lib-dynamodb";

await doc.send(
  new ExecuteTransactionCommand({
    TransactStatements: [
      {
        Statement:
          'UPDATE "Accounts" SET balance = balance - ? WHERE accountId = ? AND balance >= ?',
        Parameters: [100, "a-1", 100],
      },
      {
        Statement:
          'UPDATE "Accounts" SET balance = balance + ? WHERE accountId = ?',
        Parameters: [100, "a-2"],
      },
    ],
  }),
);
```

`BatchExecuteStatement` runs up to 25 statements in one call, but each runs on its own, like `BatchWriteItem`. Transactions with `ExecuteTransaction` follow the same limits as `TransactWriteItems`.

## 223: How do you update a value inside a nested map safely?

The parent must exist, or the update fails. Create the map first if needed, or use a condition:

```js
// make sure the parent exists
await doc.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { userId: "u-1" },
    UpdateExpression: "SET settings = if_not_exists(settings, :empty)",
    ExpressionAttributeValues: { ":empty": {} },
  }),
);

// then update the nested key
await doc.send(
  new UpdateCommand({
    TableName: "Users",
    Key: { userId: "u-1" },
    UpdateExpression: "SET settings.#theme = :t",
    ExpressionAttributeNames: { "#theme": "theme" },
    ExpressionAttributeValues: { ":t": "dark" },
  }),
);
```

You can't do both in one expression, because DynamoDB doesn't allow overlapping paths (`settings` and `settings.theme`) in the same update.

## 224: How do you remove an element from a list when you don't know its index?

DynamoDB can only remove list elements by index. So you need to:

1. Read the item and find the index
2. Remove it with a condition that the element at that index is still the one you expect

```js
const index = item.cart.findIndex((x) => x.productId === "p-7");

await doc.send(
  new UpdateCommand({
    TableName: "Carts",
    Key: { cartId: "c-1" },
    UpdateExpression: `REMOVE cart[${index}]`,
    ConditionExpression: `cart[${index}].productId = :pid`,
    ExpressionAttributeValues: { ":pid": "p-7" },
  }),
);
```

If you remove by value often, store the data as a map keyed by id, or as separate items, instead of a list.

## 225: How do you safely decrease inventory?

Use a condition so stock never goes below zero:

```js
await doc.send(
  new UpdateCommand({
    TableName: "Products",
    Key: { productId: "p-1" },
    UpdateExpression: "SET stock = stock - :qty",
    ConditionExpression: "stock >= :qty",
    ExpressionAttributeValues: { ":qty": 2 },
    ReturnValues: "UPDATED_NEW",
  }),
);
```

If two customers buy at the same time, both updates run in order on the server. The second one fails if there isn't enough stock left. For orders with several products, use a transaction with one such update per product.

## 226: How do you do a conditional delete?

Add a condition to `DeleteItem`, for example only delete a draft:

```js
await doc.send(
  new DeleteCommand({
    TableName: "Posts",
    Key: { postId: "p-1" },
    ConditionExpression: "#s = :draft AND authorId = :me",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: { ":draft": "DRAFT", ":me": userId },
  }),
);
```

This also works as a simple ownership check on the server: the delete fails if the user doesn't own the post.

## 227: What are Contributor Insights?

CloudWatch Contributor Insights for DynamoDB shows the most accessed and most throttled keys in a table or GSI. You turn it on per table or index.

```bash
aws dynamodb update-contributor-insights \
  --table-name Orders \
  --contributor-insights-action ENABLE
```

It's the easiest way to find hot partition keys. There's a small cost based on the number of events it processes, so some teams turn it on only while debugging.

## 228: Which alarms should you set for a production DynamoDB table?

- `ThrottledRequests` or `ReadThrottleEvents` / `WriteThrottleEvents` above 0 for a few minutes, on the table and every GSI
- `SystemErrors` above 0
- `SuccessfulRequestLatency` p99 above your target
- `ConsumedWriteCapacityUnits` close to provisioned or the on-demand max
- Lambda `IteratorAge` for stream consumers
- `ReplicationLatency` for global tables
- Account-level quota usage (`AccountProvisionedReadCapacityUtilization` and the write version)

Use percentiles for latency, not averages.

## 229: How do you audit who changed data in DynamoDB?

- **CloudTrail management events** log table-level actions (create, delete, update table) by default
- **CloudTrail data events** can log item-level actions (`PutItem`, `GetItem`, `DeleteItem` and so on). You must enable them, and they cost extra.
- **DynamoDB Streams** give you the before and after images of each change, which you can write to an audit log
- Store `updatedBy` and `updatedAt` attributes on items from your app

CloudTrail tells you who called the API. Streams tell you what the data looked like.

## 230: How do you write a least-privilege IAM policy for a Lambda?

Grant only the actions and tables the function needs:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:UpdateItem"],
      "Resource": [
        "arn:aws:dynamodb:eu-central-1:123456789012:table/App",
        "arn:aws:dynamodb:eu-central-1:123456789012:table/App/index/GSI1"
      ]
    }
  ]
}
```

Don't use `dynamodb:*` or `Resource: "*"`. Index ARNs are separate resources, so add them if the function queries an index. In CDK, `table.grantReadData(fn)` and similar methods build these policies for you.

## 231: What is fine-grained access control with dynamodb:LeadingKeys?

An IAM condition that limits which partition keys a user can access. It's often used with Cognito identities, so each user only sees their own items:

```json
{
  "Effect": "Allow",
  "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem"],
  "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/UserData",
  "Condition": {
    "ForAllValues:StringEquals": {
      "dynamodb:LeadingKeys": ["${cognito-identity.amazonaws.com:sub}"]
    }
  }
}
```

The partition key must be the user's id for this to work. It's enforced by IAM, so even buggy client code can't read someone else's data.

## 232: What are resource-based policies for DynamoDB?

Policies attached directly to a table, index or stream, instead of to an IAM user or role. They say which principals can do what on that resource.

They're mostly used for cross-account access: account B's role can read account A's table without assuming a role in account A. You can also use them to add extra restrictions, like denying access unless the request comes through a certain VPC endpoint. A request is allowed only if no policy denies it and at least one allows it.

## 233: How do you access DynamoDB privately from a VPC?

Two options:

- **Gateway VPC endpoint**: free, added to route tables. Traffic from the VPC to DynamoDB stays on the AWS network. It only works from inside that VPC.
- **Interface VPC endpoint (PrivateLink)**: creates network interfaces with private IPs in your subnets. It costs money, but you can reach it from on-premises over VPN or Direct Connect and from peered VPCs.

Both let Lambdas or containers in private subnets use DynamoDB without a NAT gateway. You can add an endpoint policy to limit which tables are reachable.

## 234: Which KMS key option should you choose?

- **AWS owned key**: the default. No cost, no management, but you can't see or audit it in your account.
- **AWS managed key** (`aws/dynamodb`): visible in your account, usage shows up in CloudTrail. There are KMS request charges.
- **Customer managed key**: you control the key policy, rotation and who can use it, and you can disable it to cut off access. Needed for many compliance rules and for some cross-account setups.

If you disable or delete a customer managed key, the table becomes inaccessible, and after a while it's archived. So protect the key carefully.

## 235: How do you give another AWS account access to a table?

Options:

1. **Resource-based policy** on the table that allows the other account's role
2. **Cross-account role**: create a role in your account with DynamoDB permissions and let the other account assume it with `sts:AssumeRole`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::222222222222:role/ReportingRole" },
      "Action": ["dynamodb:Query", "dynamodb:GetItem"],
      "Resource": "arn:aws:dynamodb:us-east-1:111111111111:table/Orders"
    }
  ]
}
```

If the table uses a customer managed KMS key, the other account also needs permission to use that key.

## 236: How do you use AWS Backup with DynamoDB?

AWS Backup lets you manage DynamoDB backups with backup plans: a schedule, a retention period and a vault. Extra features compared to native backups:

- Copy backups to another Region or another account
- Move backups to cold storage after a set time
- Backup vault lock to stop anyone, even admins, from deleting backups
- One place to manage backups for many services

It's a good fit for compliance needs and for protecting against an account being compromised.

## 237: What do you need to know about restoring a table from PITR?

- The restore always creates a new table. You can't overwrite the existing one.
- Restore time depends on the table size, and big tables can take hours
- Data, GSIs and LSIs are restored. You can choose to leave GSIs out.
- Some settings are not restored: auto scaling, IAM policies, CloudWatch alarms, tags, TTL and stream settings
- You can restore to another Region

After a restore, you need to point the app to the new table name (or copy data back), and set up the missing settings. Keeping everything in IaC makes this much easier.

## 238: How do you set up a global table?

With the current version (2019.11.21), you add replicas to an existing table:

```bash
aws dynamodb update-table \
  --table-name Orders \
  --replica-updates '[{"Create":{"RegionName":"eu-west-1"}}]'
```

Requirements:

- DynamoDB Streams with `NEW_AND_OLD_IMAGES` (DynamoDB turns it on for you)
- Same key schema and GSIs in every replica (managed for you)

In CDK, add `replicas: [{ region: 'eu-west-1' }]` to a `TableV2`. Avoid the legacy 2017.11.29 version for new tables.

## 239: How does conflict resolution work in global tables?

With the default multi-Region eventual consistency (MREC), if the same item is changed in two Regions at about the same time, the last writer wins. The write with the latest timestamp is kept everywhere, and the other is lost.

To avoid surprises:

- Route writes for one item to one "home" Region when possible
- Avoid read-modify-write across Regions on the same item
- Use conditional writes with care, because conditions are only checked in the Region you write to
- Or use multi-Region strong consistency (MRSC) for data that must not conflict

## 240: What is multi-Region strong consistency (MRSC)?

A global tables mode, generally available since mid-2025, where writes are replicated synchronously to at least one other Region before they're confirmed. A strongly consistent read in any Region returns the latest data.

Key points:

- It uses exactly three Regions: three replicas, or two replicas and a witness
- You choose the mode when you create the global table
- Writes have higher latency, because they wait for another Region
- No last-writer-wins conflicts: conflicting writes fail with an error instead
- RPO is zero for Region failures

It fits money, inventory and other data where losing a write isn't acceptable.

## 241: How much do global tables cost?

You pay for:

- Replicated writes in every Region (each write is done once per replica)
- Storage in every Region
- Reads in the Region where they happen
- Data transfer between Regions

So a table with three replicas costs roughly three times for writes and storage. Prices for replicated writes were reduced in late 2024, but writes are still the main cost driver.

## 242: How does import from S3 work in practice?

```bash
aws dynamodb import-table \
  --s3-bucket-source S3Bucket=my-bucket,S3KeyPrefix=exports/orders/ \
  --input-format DYNAMODB_JSON \
  --input-compression-type GZIP \
  --table-creation-parameters '{
    "TableName": "OrdersRestored",
    "KeySchema": [{"AttributeName":"customerId","KeyType":"HASH"},{"AttributeName":"orderDate","KeyType":"RANGE"}],
    "AttributeDefinitions": [{"AttributeName":"customerId","AttributeType":"S"},{"AttributeName":"orderDate","AttributeType":"S"}],
    "BillingMode": "PAY_PER_REQUEST"
  }'
```

You pay per GB of source data, which is much cheaper than writing the items yourself. Invalid rows are logged to CloudWatch Logs and skipped. You can define GSIs in the creation parameters, and they're built during the import.

## 243: How do incremental exports work?

An incremental export writes only the items that changed between two times (up to 24 hours apart per export, within the PITR window). Each record has the new and/or old image of the item.

```bash
aws dynamodb export-table-to-point-in-time \
  --table-arn arn:aws:dynamodb:us-east-1:123456789012:table/Orders \
  --s3-bucket my-exports \
  --export-type INCREMENTAL_EXPORT \
  --incremental-export-specification ExportFromTime=1761696000,ExportToTime=1761782400,ExportViewType=NEW_AND_OLD_IMAGES
```

You can run one full export, then incremental ones every hour or day, to keep a data lake in sync without touching the table's capacity.

## 244: What are zero-ETL integrations for DynamoDB?

Managed integrations that copy DynamoDB data to analytics or search services, without you writing pipelines:

- **Amazon OpenSearch Service**: full-text search, fuzzy search and aggregations on DynamoDB data, synced in near real time
- **Amazon Redshift**: SQL analytics and joins
- **Amazon SageMaker Lakehouse**: data in Apache Iceberg format for analytics and ML

They use PITR exports and streams behind the scenes, so they don't use your table's read capacity.

## 245: How do you run SQL analytics on DynamoDB data?

Export the table to S3 (full or incremental), then query it with Athena or load it into Redshift. Or use the zero-ETL integration with Redshift.

```sql
SELECT item.status.s AS status, count(*) AS orders
FROM orders_export
GROUP BY item.status.s;
```

Running heavy analytics directly on DynamoDB with scans is slow and expensive, and it can throttle your live traffic.

## 246: How do you add full-text search to DynamoDB data?

DynamoDB has `begins_with` and `contains`, but no real search with ranking, stemming or fuzzy matching. Common setups:

- Zero-ETL integration with OpenSearch Service
- DynamoDB Streams + Lambda that writes changes to OpenSearch (or Algolia, Typesense, Meilisearch)

The search engine returns matching ids, and you can fetch the full items from DynamoDB with `BatchGetItem` if they're not in the search index already.

## 247: How do you query items by a date range across all users?

You can't query "all orders created yesterday" on the base table if it's keyed by user. Add a GSI with a time bucket as the partition key and the full timestamp as the sort key:

```text
GSI1PK = ORDERDATE#2026-10-28
GSI1SK = 2026-10-28T14:22:10Z#o-123
```

Query one bucket per day. If one day gets too many writes for a single GSI partition, shard the bucket (`ORDERDATE#2026-10-28#3`) and query all shards in parallel.

## 248: How do you do geospatial queries in DynamoDB?

DynamoDB has no geo index. The usual approach is geohashing: encode latitude and longitude into a string where nearby points share a prefix.

```text
pk = GEO#u4pruy      (geohash with a few characters, like a grid cell)
sk = u4pruydqqvj#store-42
```

To find nearby places, compute the geohash cells around the point, query each cell, and then filter by exact distance in code. For heavier geo needs, use OpenSearch, Amazon Location Service or PostGIS next to DynamoDB.

## 249: How do you support case-insensitive lookups?

Store a normalized copy of the value and query that:

```js
Item: {
  pk: `USER#${id}`,
  username: 'AnaSmith',
  usernameLower: 'anasmith',
}
```

Put `usernameLower` in a GSI key, and lowercase the input before querying. Same idea for trimming spaces or removing accents.

## 250: How do you sort by a non-key attribute?

DynamoDB can only sort by the sort key. To sort by something else, like price:

- Add a GSI with the same partition key and the attribute as the sort key, for example `pk = CATEGORY#books`, `sk = price`
- Or, for small result sets, fetch and sort in code

If you need many different sort orders on the same data, you'll need several GSIs, and at some point a search engine or SQL database becomes the better tool.

## 251: How do you implement soft deletes?

Mark the item instead of deleting it:

```js
UpdateExpression: "SET deletedAt = :now REMOVE GSI1PK, GSI1SK";
```

- Removing the GSI keys takes the item out of list indexes, so lists don't need filters
- Set a TTL so the item is really deleted later, for example after 30 days
- Direct `GetItem` calls must check `deletedAt`

This gives you an undo window and an audit trail without keeping deleted data forever.

## 252: How do you design a multi-tenant table?

The most common way is to put the tenant id at the start of every partition key:

```text
pk = TENANT#t-1#USER#u-9
sk = PROFILE
```

Then:

- Every query is naturally limited to one tenant
- You can use `dynamodb:LeadingKeys` in IAM to stop one tenant from reading another's data (with a prefix condition on the tenant)
- Contributor Insights shows which tenants are hot

For large or regulated tenants, a separate table (or even a separate account) per tenant gives stronger isolation and per-tenant backups, at the cost of more tables to manage.

## 253: What is write sharding?

Spreading writes for a hot key across several partition keys by adding a suffix:

```js
const shard = Math.floor(Math.random() * 10);
const pk = `VOTES#candidate-1#${shard}`;
```

Writes now go to 10 different partitions. To read the total, query all 10 keys and add the results. If you need to find a specific item later, use a calculated suffix (like a hash of the item id) instead of a random one, so you can compute which shard it went to.

## 254: How do you estimate the monthly cost of a table?

Work out:

1. Writes per second x item size in KB (rounded up) x number of GSIs that each write touches (plus 1 for the table)
2. Reads per second x item size in 4 KB units, halved for eventually consistent reads
3. Storage in GB, including GSIs
4. Extras: PITR, backups, streams, global table replicas

Then multiply by the price for your Region and mode. The AWS Pricing Calculator does this for you. Item size and GSI count change the result a lot, so measure real items, not guesses.

## 255: What are practical ways to lower DynamoDB costs?

- Use eventually consistent reads when you can
- Keep items small: short attribute names, compression, large data in S3
- Fewer GSIs, and project only what you need
- Use `UpdateItem` on small items instead of rewriting big ones
- Avoid scans. Use queries and sparse indexes.
- Use TTL to delete old data for free
- Use Standard-IA for tables that are mostly storage
- Use provisioned mode with reserved capacity for steady, high traffic
- Put a cache (DAX or an app cache) in front of hot reads

## 256: When should you use the Standard-IA table class?

When storage is the biggest part of the table's cost. AWS suggests that if storage cost is more than about half of the cost of your reads and writes, Standard-IA is likely cheaper.

Good candidates: order history, old chat messages, audit logs, social media posts that are rarely read after a few weeks. You can switch a table's class up to two times in a 30-day period, so you can try it and compare bills.

## 257: How do attribute names affect cost?

Attribute names are stored in every item and count toward item size. With millions of items, long names cost real money in storage and in capacity units, because item size decides how many units each read and write uses.

```text
customerShippingAddressPostalCode  -> 33 bytes per item
zip                                -> 3 bytes per item
```

Don't make names unreadable, but avoid very long ones on high-volume items. Libraries like ElectroDB can map nice names in code to short names in the table.

## 258: Why can UpdateItem be cheaper than PutItem?

It isn't always. Write capacity is based on the size of the item, and for `UpdateItem` it's the larger of the item size before or after the update. So updating one field on a 10 KB item still costs 10 WCU.

What does save cost is splitting items so that frequently updated fields live in a small item. `UpdateItem` is still better than read-then-put for other reasons: it's atomic, it's one request, and it can't overwrite fields other writers changed.

## 259: How do you use begins_with to fetch different entity types?

With a single-table design, the sort key prefix tells you the entity type, so you can query one type or all types under a partition key:

```js
// only invoices of a customer
KeyConditionExpression: 'pk = :pk AND begins_with(sk, :p)',
ExpressionAttributeValues: { ':pk': 'CUSTOMER#c-1', ':p': 'INVOICE#' },

// customer profile + everything else
KeyConditionExpression: 'pk = :pk',
```

Choose prefixes so the ones you read together sort next to each other. You can also read a range like `sk BETWEEN 'INVOICE#' AND 'ORDER#~'` to get two types at once.

## 260: How do you model a workflow or state machine in DynamoDB?

Store the current state on the item and only allow valid transitions with conditions:

```js
const transitions = {
  PENDING: ["PAID", "CANCELLED"],
  PAID: ["SHIPPED", "REFUNDED"],
};

async function moveOrder(orderId, from, to) {
  if (!transitions[from]?.includes(to)) throw new Error("Invalid transition");
  await doc.send(
    new UpdateCommand({
      TableName: "Orders",
      Key: { orderId },
      UpdateExpression:
        "SET #s = :to, #h = list_append(if_not_exists(#h, :e), :entry)",
      ConditionExpression: "#s = :from",
      ExpressionAttributeNames: { "#s": "status", "#h": "history" },
      ExpressionAttributeValues: {
        ":from": from,
        ":to": to,
        ":e": [],
        ":entry": [{ status: to, at: new Date().toISOString() }],
      },
    }),
  );
}
```

Streams can then trigger the next step (send email, start shipping) on each state change.

## 261: How do you use DynamoDB as a session store?

Key by session id, store the session data, and set a TTL:

```js
await doc.send(
  new PutCommand({
    TableName: "Sessions",
    Item: {
      sessionId,
      userId,
      data: { cart: [] },
      expiresAt: Math.floor(Date.now() / 1000) + 60 * 60 * 24,
    },
  }),
);
```

On each read, check `expiresAt` in code, since TTL deletes can be late. Use a long random session id. If session reads are very frequent, DAX or ElastiCache in front can lower latency and cost.

## 262: How do you build a simple rate limiter with DynamoDB?

A fixed-window counter per user and time window, using an atomic update with a condition:

```js
const windowStart = Math.floor(Date.now() / 60000); // 1-minute window

await doc.send(
  new UpdateCommand({
    TableName: "RateLimits",
    Key: { pk: `RL#${userId}#${windowStart}` },
    UpdateExpression: "ADD hits :one SET expiresAt = :ttl",
    ConditionExpression: "attribute_not_exists(hits) OR hits < :max",
    ExpressionAttributeValues: {
      ":one": 1,
      ":max": 100,
      ":ttl": Math.floor(Date.now() / 1000) + 120,
    },
  }),
);
```

A `ConditionalCheckFailedException` means the limit is reached. TTL cleans up old windows. For very high request rates, a cache like ElastiCache is cheaper.

## 263: How can Step Functions use DynamoDB directly?

Step Functions has direct service integrations for `GetItem`, `PutItem`, `UpdateItem`, `DeleteItem` and `Query`, plus any API through the AWS SDK integration. You don't need a Lambda just to read or write an item.

```json
"SaveOrder": {
  "Type": "Task",
  "Resource": "arn:aws:states:::dynamodb:putItem",
  "Arguments": {
    "TableName": "Orders",
    "Item": {
      "orderId": { "S": "{% $states.input.orderId %}" },
      "status": { "S": "CREATED" }
    }
  },
  "Next": "ChargeCard"
}
```

Values use DynamoDB JSON. This cuts cost and latency, and removes code you'd have to maintain.

## 264: How do you call DynamoDB directly from API Gateway?

REST APIs in API Gateway can call DynamoDB actions directly with an AWS service integration and a mapping template, with no Lambda in between:

```velocity
{
  "TableName": "Orders",
  "Key": { "orderId": { "S": "$input.params('id')" } }
}
```

The integration uses an IAM role that API Gateway assumes. It's fast and cheap for simple CRUD, but mapping templates (VTL) are hard to test and debug. Once you need real logic, a Lambda is easier to maintain.

## 265: How does AppSync work with DynamoDB?

AppSync is AWS's managed GraphQL service. A DynamoDB data source lets resolvers call DynamoDB directly. Resolvers are usually written in JavaScript (the `APPSYNC_JS` runtime):

```js
import * as ddb from "@aws-appsync/utils/dynamodb";

export function request(ctx) {
  return ddb.get({ key: { id: ctx.args.id } });
}

export function response(ctx) {
  return ctx.result;
}
```

You can also use pipeline resolvers to call several data sources in order. AppSync subscriptions let clients receive real-time updates when mutations change data.

## 266: How do you send DynamoDB changes to other services without Lambda?

Use EventBridge Pipes with the DynamoDB stream as a source. A pipe can filter events, optionally enrich them, and send them to targets like SQS, SNS, EventBridge buses, Step Functions or Kinesis.

```text
DynamoDB Stream -> Pipe (filter: eventName = INSERT, type = Order) -> EventBridge bus
```

This avoids writing and maintaining glue Lambda code. It's a common way to publish domain events from DynamoDB.

## 267: How do you delete many items efficiently?

- **All items**: delete and recreate the table
- **Items in one partition key**: `Query` for the keys (use `ProjectionExpression` to fetch only keys), then `BatchWriteItem` delete requests in chunks of 25
- **Old items by age**: TTL, which is free
- **Very large deletes**: run a parallel scan in a separate job, slowly, so you don't throttle live traffic

```js
for await (const page of paginateQuery(
  { client: doc },
  {
    TableName: "App",
    KeyConditionExpression: "pk = :pk",
    ExpressionAttributeValues: { ":pk": "TENANT#t-1" },
    ProjectionExpression: "pk, sk",
  },
)) {
  await batchDelete("App", page.Items); // chunks of 25 with retries
}
```

## 268: How do you change the primary key of a table that's in production?

1. Create a new table with the new key design.
2. Change the app to write to both tables (dual writes), or stream changes from the old table to the new one with a Lambda.
3. Backfill old data with a scan or an export/import, converting each item to the new key format. Use conditional writes so you don't overwrite newer data from step 2.
4. Compare counts and spot-check items.
5. Switch reads to the new table, then stop writing to the old one.
6. Keep the old table for a while, then delete it.

## 269: What grant methods does the CDK table construct offer?

- `grantReadData(grantee)`: `GetItem`, `Query`, `Scan`, `BatchGetItem` and related actions
- `grantWriteData(grantee)`: `PutItem`, `UpdateItem`, `DeleteItem`, `BatchWriteItem`
- `grantReadWriteData(grantee)`: both
- `grantFullAccess(grantee)`: all DynamoDB actions on the table
- `grantStreamRead(grantee)`: read the table's stream
- `grant(grantee, ...actions)`: specific actions only

They also add KMS permissions when the table uses a customer managed key, and include the index ARNs. That's easier and safer than writing the policy by hand.

## 270: How do you protect a table from being deleted by CloudFormation?

- `DeletionPolicy: Retain` keeps the table when the resource or stack is deleted
- `UpdateReplacePolicy: Retain` keeps the old table when a change forces a replacement (like changing the key schema or table name)
- `DeletionProtectionEnabled: true` makes DynamoDB itself refuse the delete
- Stack termination protection and stack policies add more safety

Changing the key schema in a template replaces the table. Without these settings, that means losing all the data.

## 271: How do you avoid conflicts between Terraform and auto scaling?

When auto scaling changes `read_capacity` and `write_capacity`, the next `terraform plan` sees a difference and wants to change it back. Tell Terraform to ignore those fields:

```hcl
resource "aws_dynamodb_table" "orders" {
  # ...
  billing_mode   = "PROVISIONED"
  read_capacity  = 10
  write_capacity = 10

  lifecycle {
    ignore_changes = [read_capacity, write_capacity]
  }
}
```

Use `aws_appautoscaling_target` and `aws_appautoscaling_policy` resources for the scaling settings.

## 272: Do Query and Scan support strongly consistent reads?

Yes, both support `ConsistentRead: true` on the table and on LSIs. They don't support it on GSIs. If you set `ConsistentRead: true` on a GSI query, you get a `ValidationException`.

A strongly consistent query costs twice as much as an eventually consistent one, like `GetItem`.

## 273: Are GSI keys unique?

No. Many items can have the same GSI partition key and sort key values. DynamoDB doesn't check uniqueness in an index.

That's why `GetItem` doesn't work on a GSI: there might be several matches. If you need uniqueness (like one user per email), enforce it with a separate item keyed by that value and a conditional write or transaction.

## 274: What causes a ValidationException?

Common causes:

- The key in the request doesn't match the table's key schema (missing sort key, wrong name or wrong type)
- A reserved word used without a placeholder
- A placeholder used in the expression but missing from `ExpressionAttributeValues`, or one defined but not used
- An `undefined` value with the Document Client (fix with `removeUndefinedValues`)
- An empty set, or an empty string as a key value
- Item larger than 400 KB
- Two actions on the same item in a transaction, or a duplicate key in a batch
- `ConsistentRead: true` on a GSI

The error message usually says exactly what's wrong, so read it fully.

## 275: How do you model data that is read together and data that is written often?

Group by access pattern, not by entity:

- Data that's read together should be in the same item or item collection
- Data that changes often should be in a small separate item, so each write is cheap and doesn't conflict with others
- Data that's large and rarely read should be in a separate item or in S3

For example, a product's `viewCount` that changes every second shouldn't live in the same item as its 50 KB description.

## 276: How do you keep duplicated data in sync?

When you denormalize (copy a user's name into their posts), you have to update the copies when the original changes:

- **Streams**: a Lambda reacts to `MODIFY` on the user item and updates the posts. Eventually consistent, but it doesn't slow down the main write.
- **Transactions**: update everything at once. Only possible for up to 100 items.
- **Accept stale data**: for some things (like a name on an old order) the old value is actually correct

Choose by how often the data changes and how many copies exist. Copying data that changes often to many items gets expensive.

## 277: How do you handle deleting a parent and its children?

There's no cascading delete. Options:

- If the children share the parent's partition key, `Query` that key and delete everything with `BatchWriteItem`
- Use a stream: when the parent is deleted, a Lambda deletes its children
- Mark the parent as deleted and let TTL clean up the children
- For up to 100 items, use a transaction if all deletes must happen together

Pick the approach that matches how many children there are and whether partial deletes are a problem.

## 278: How do you get read-after-write consistency?

- Read from the table (not a GSI) with `ConsistentRead: true`
- Or use the `ReturnValues: 'ALL_NEW'` of the write itself, so you don't need to read at all
- With global tables in MREC mode, read from the same Region you wrote to

Returning the new values from the write is often the simplest and cheapest way to show the updated item to the user.

## 279: Why might DynamoDB requests be slow from your app?

- New TLS connections on every request (client created per request, or keep-alive turned off)
- App running in a different Region than the table
- Large items or reading many items you don't need
- Throttling and retries with backoff
- Cold starts in Lambda that include SDK setup
- DNS or NAT gateway issues in a VPC
- Large Scan or Query pages with filters that throw away most data

Compare `SuccessfulRequestLatency` in CloudWatch (server-side) with your app's measured latency. If server latency is low, the problem is in the client or the network.

## 280: How do you compress data in DynamoDB items?

Compress large text or JSON attributes with gzip or brotli and store them as Binary:

```js
import { gzipSync, gunzipSync } from 'node:zlib';

// write
Item: { id, body: gzipSync(JSON.stringify(data)) }

// read
const data = JSON.parse(gunzipSync(Item.body).toString());
```

Compression often makes text 3 to 10 times smaller, which lowers storage and capacity costs. The downside: you can't filter on or update fields inside the compressed value.

## 281: How do you encrypt specific attributes on the client side?

Use the AWS Database Encryption SDK for DynamoDB. It encrypts and signs chosen attributes before they leave your app, so even someone with table access can't read them.

You configure which attributes are encrypted and signed, which are only signed, and which are left alone (keys must stay readable). It also supports searchable encryption with beacons, so you can still query on some encrypted fields.

It's used for sensitive data like personal data or health records, on top of the normal encryption at rest.

## 282: How can you use DynamoDB for event sourcing?

Store each event as an item, keyed by the aggregate id and a sequence number:

```text
pk = ACCOUNT#a-1
sk = EVENT#000000042
type = MoneyDeposited
data = { amount: 100 }
```

- Append with `attribute_not_exists(pk)` to make sure no two events get the same sequence number
- Rebuild state by querying all events for the aggregate in order
- Use Streams to update read models (projections)
- Store snapshots every N events so you don't have to replay everything

## 283: How do you implement the outbox pattern with DynamoDB?

The goal is to save data and publish an event reliably, without a two-phase commit with a message broker. With DynamoDB you often don't need a separate outbox table: Streams already gives you a reliable change log.

1. Write the business item (or the item plus an event item in a transaction)
2. A stream consumer (Lambda or EventBridge Pipes) reads the change and publishes it to SNS, SQS or EventBridge

If publishing fails, the consumer retries. Consumers must be idempotent, because a record can be processed more than once.

## 284: How does DynamoDB compare to Aurora DSQL?

- **DynamoDB**: NoSQL, key-based access, single-digit millisecond latency, mature, huge scale, needs access-pattern-first modeling
- **Aurora DSQL**: serverless distributed SQL database compatible with PostgreSQL, multi-Region active-active, supports SQL and joins, but with some PostgreSQL features missing

Choose DynamoDB for very high throughput with known key-based patterns. Choose DSQL when you want serverless scaling but need SQL, relational modeling and ad hoc queries.

## 285: How do you choose a partition key for IoT data?

Use the device id, often combined with a time bucket:

```text
pk = DEVICE#d-123#2026-10-29
sk = 2026-10-29T10:15:30.123Z
```

- Device id spreads load across many partitions
- The time bucket keeps one busy device from building a huge, hot item collection
- The timestamp sort key allows range queries

If one device sends more than about 1,000 writes per second (or more than 1 MB/s), add a shard suffix, or batch readings into fewer, bigger items.

## 286: How do you get the latest N items for a key?

Query in descending order with a limit:

```js
const { Items } = await doc.send(
  new QueryCommand({
    TableName: "Events",
    KeyConditionExpression: "deviceId = :d",
    ExpressionAttributeValues: { ":d": "d-1" },
    ScanIndexForward: false,
    Limit: 5,
  }),
);
```

For "the single latest item", a separate "latest" item that you overwrite on each write can be cheaper to read, especially if it's read often.

## 287: How do you count items in a large partition?

`Select: 'COUNT'` still reads all items and pages through 1 MB at a time:

```js
let count = 0;
let ExclusiveStartKey;
do {
  const res = await doc.send(
    new QueryCommand({
      TableName: "App",
      KeyConditionExpression: "pk = :pk",
      ExpressionAttributeValues: { ":pk": "TENANT#t-1" },
      Select: "COUNT",
      ExclusiveStartKey,
    }),
  );
  count += res.Count;
  ExclusiveStartKey = res.LastEvaluatedKey;
} while (ExclusiveStartKey);
```

Fine for occasional checks. For counts shown on every page load, keep a counter item updated on each write.

## 288: How do you find out why a query uses so much capacity?

1. Add `ReturnConsumedCapacity: 'INDEXES'` and log the result
2. Compare `ScannedCount` to `Count`. A big difference means filters are doing the work keys should do.
3. Check item sizes. Large items cost more units per read.
4. Check if `ConsistentRead: true` is set without a reason
5. Check if the query reads more pages than needed (missing `Limit` or loops that read everything)

Then fix the model: add a sort key condition, a sparse index, or split large items.

## 289: How do you handle access patterns that need OR conditions on keys?

Key conditions don't support `OR` or `IN`. Options:

- Run several queries in parallel, one per value, and merge the results in code
- Use `BatchGetItem` when you have full keys
- Design a GSI where both cases share a key
- Use a filter, if the extra reads are small

```js
const statuses = ["PENDING", "PAID"];

const results = await Promise.all(
  statuses.map((s) =>
    doc.send(
      new QueryCommand({
        TableName: "App",
        IndexName: "GSI1",
        KeyConditionExpression: "GSI1PK = :pk",
        ExpressionAttributeValues: { ":pk": `STATUS#${s}` },
      }),
    ),
  ),
);
const items = results.flatMap((r) => r.Items);
```

## 290: How do you store and query hierarchical data like categories or folders?

Store the full path in the sort key, so `begins_with` returns a whole subtree:

```text
pk = TENANT#t-1
sk = PATH#/docs/2026/reports/q3.pdf
```

- Everything under `/docs/2026/`: `begins_with(sk, 'PATH#/docs/2026/')`
- Direct children only: query the prefix and filter in code, or also store a `parentPath` attribute in a GSI

Moving a folder means rewriting every item under it, so this works best when the tree doesn't change shape often.

## 291: What is the difference between a GSI and a materialized view?

A GSI is a copy of selected attributes, organized by a different key, that DynamoDB keeps in sync for you. It can't change data: no aggregations, no joins, no calculated values.

A materialized view in DynamoDB is something you build yourself, usually with Streams and a Lambda, for example "total sales per day". It can hold any computed result, but you're responsible for keeping it correct.

## 292: How do you handle "item not found" vs "access denied" in a multi-tenant app?

Include the tenant id in the key, so a request for another tenant's item just doesn't find anything:

```js
const { Item } = await doc.send(
  new GetCommand({
    TableName: "App",
    Key: { pk: `TENANT#${ctx.tenantId}#DOC#${docId}`, sk: "META" },
  }),
);

if (!Item) return notFound();
```

Return 404 in both cases. That way you don't reveal whether an item exists for another tenant. Never trust a tenant id that comes from the request body. Take it from the authenticated token.

## 293: How do you read many items by key from several tables at once?

`BatchGetItem` can read from several tables in one call, up to 100 keys total:

```js
const res = await doc.send(
  new BatchGetCommand({
    RequestItems: {
      Users: {
        Keys: [{ userId: "u-1" }],
        ProjectionExpression: "userId, #n",
        ExpressionAttributeNames: { "#n": "name" },
      },
      Products: { Keys: [{ productId: "p-1" }, { productId: "p-2" }] },
    },
  }),
);

console.log(res.Responses.Users, res.Responses.Products);
```

Retry `UnprocessedKeys`. Each table can have its own projection and consistency settings.

## 294: When should you split one DynamoDB table into several?

- Different entities need different settings: streams, TTL, backups, table class or encryption key
- Access control should be separated per entity
- One entity has very different traffic or cost and you want to see it on its own
- Different teams own different parts of the data
- An entity is often exported or analyzed by itself

Single-table is a tool to answer access patterns efficiently. If entities are never read together, putting them in one table doesn't help much.

## 295: How do you handle throttling in your application code?

- Let the SDK retry, but set a sensible `maxAttempts` and use `adaptive` retry mode for batch jobs
- Make background jobs slow down on their own (fixed rate or token bucket)
- Spread batch writes over time instead of sending everything at once
- Return a clear error (like HTTP 503 with retry-after) instead of hanging
- Find the cause: hot key, too little capacity, a GSI without enough capacity, or the on-demand max

## 296: Why does a new on-demand table sometimes throttle?

On-demand tables can handle up to double their previous peak right away, but a brand new table starts with a certain initial capacity. If your first traffic is much higher than that, for example a migration that writes millions of items in minutes, DynamoDB has to split partitions first, and you can see throttling while it does.

Fixes: pre-warm the table with warm throughput, ramp up traffic gradually, or create it in provisioned mode with high capacity and then switch to on-demand.

## 297: What is the difference between ThrottlingException and ProvisionedThroughputExceededException?

- `ProvisionedThroughputExceededException`: a request went over the capacity of a table, index or partition. Seen in both modes, for example a hot partition in on-demand mode or provisioned capacity that's too low.
- `ThrottlingException`: usually for control-plane calls (like too many `CreateTable` or `UpdateTable` calls), and in some cases for on-demand throughput limits

Newer SDK versions also return throttling reasons in the error details, telling you whether the table, an index or a key hit its limit. Both are retried by the SDK.

## 298: How do you make sure two Lambda invocations don't process the same job?

Claim the job with a conditional update:

```js
await doc.send(
  new UpdateCommand({
    TableName: "Jobs",
    Key: { jobId },
    UpdateExpression: "SET #s = :running, workerId = :me, startedAt = :now",
    ConditionExpression: "#s = :pending",
    ExpressionAttributeNames: { "#s": "status" },
    ExpressionAttributeValues: {
      ":running": "RUNNING",
      ":pending": "PENDING",
      ":me": context.awsRequestId,
      ":now": Date.now(),
    },
  }),
);
```

Only one invocation can move the job from `PENDING` to `RUNNING`. The others get `ConditionalCheckFailedException` and skip it. Add a timeout check so jobs stuck in `RUNNING` can be picked up again.

## 299: How do you search items whose attribute contains a value?

`contains()` works in filter expressions on strings (substring), sets and lists (element):

```js
new QueryCommand({
  TableName: "App",
  KeyConditionExpression: "pk = :pk",
  FilterExpression: "contains(title, :word)",
  ExpressionAttributeValues: { ":pk": "BLOG#b-1", ":word": "DynamoDB" },
});
```

It's case-sensitive and still reads every item in the query. For a small partition that's fine. For real search, use OpenSearch.

## 300: What is the difference between a Query on the table and a Query on an LSI?

- Both use the same partition key value
- The LSI gives you a different sort order or range condition (for example by `price` instead of `createdAt`)
- Both support strongly consistent reads
- If you request attributes that aren't projected into the LSI, DynamoDB fetches them from the table automatically and charges extra reads. A GSI can't do that.

So an LSI is like a second sort key for the same partition.

# Advanced Questions (301-450)

## 301: How does DynamoDB decide which partition stores an item?

DynamoDB hashes the partition key value with an internal hash function. The hash space is split into ranges, and each range belongs to one partition. The item goes to the partition whose range covers its hash.

Because of hashing, keys that look similar (`user-1`, `user-2`) end up in different partitions, which is what spreads load. It also means there's no ordering across partition keys, and you can't do a range query over partition keys.

## 302: What are the per-partition limits and why do they matter?

Each partition supports about:

- 3,000 read capacity units per second
- 1,000 write capacity units per second
- 10 GB of data

These limits apply no matter how much capacity the table has. A single partition key value can't go above them (unless DynamoDB splits that key's items by sort key, see split for heat). So if one key needs 5,000 writes per second, you have to shard it in your design. No setting fixes that for you.

## 303: When does DynamoDB split a partition?

DynamoDB splits partitions when:

- A partition grows past about 10 GB of data
- The table's throughput needs more partitions than it has (for example, you raise provisioned capacity or on-demand traffic grows)
- A partition is constantly hot (split for heat)

Splits happen in the background without downtime. Partitions are never merged back. That's why a table that once had a huge peak keeps many partitions, which helps on-demand handle that peak again.

## 304: What is "split for heat"?

When a partition gets heavy traffic for a while, DynamoDB can split it so the hot keys move to different partitions. If one partition key has a sort key, DynamoDB can even split items of the same partition key across partitions by sort key range.

This doesn't help when every request hits the same single item, or when writes come in strictly increasing sort key order (like timestamps), because new writes always land at the end of the range in the same new partition.

## 305: What happens inside DynamoDB when you send a request?

Roughly:

1. The request reaches a request router, which authenticates it (IAM, SigV4) and checks quotas and throttling.
2. The router looks up partition metadata to find which storage nodes hold the partition for the key.
3. Writes go to the partition's leader replica. Eventually consistent reads can go to any replica.
4. Storage nodes read or write the data and return the result.

The router layer is stateless and scaled out, which is why DynamoDB can absorb huge request rates.

## 306: How is data replicated inside a Region?

Each partition has three replicas in three different Availability Zones. They form a replication group that uses Multi-Paxos to elect a leader.

- Writes go to the leader, which writes to its log and sends them to the other replicas. The write is confirmed when a quorum (two of three) has stored it.
- If the leader fails, the remaining replicas elect a new leader, usually quickly.

This is why a write survives the loss of one Availability Zone.

## 307: Why do strongly consistent reads cost more?

A strongly consistent read must be served by the leader replica, which is the only one guaranteed to have every confirmed write. An eventually consistent read can be served by any of the three replicas, so DynamoDB can spread the load.

Because the leader does more of the work, strongly consistent reads cost twice the capacity, can have slightly higher latency, and are not available on GSIs, which are updated asynchronously.

## 308: How long can an eventually consistent read be out of date?

Usually less than a second, often just milliseconds. A follower replica that missed a recent write catches up very quickly.

AWS doesn't guarantee a maximum lag, so don't build logic that relies on "it's consistent after X milliseconds". If you need the latest value, use strong consistency or use the values returned by the write.

## 309: How are GSIs kept up to date?

When an item is written to the table, DynamoDB writes it on the table partition first and confirms the write. Then the change is sent asynchronously to the GSI's own partitions, which have their own key distribution.

Consequences:

- GSI reads are eventually consistent
- GSI writes have their own throughput and can throttle (and apply back pressure to the table)
- A GSI with a bad key (low cardinality) can be hot even if the table's key is good
- If an update changes the GSI key, the index does a delete plus an insert, costing two writes on the index

## 310: Can a GSI return an item that no longer exists in the table?

For a short time, yes. If you delete an item from the table, the delete reaches the GSI a little later. A query on the GSI during that window can still return the deleted item, or an old version of an updated item.

If it matters, read the item again from the table after querying the index, and skip items that no longer exist or no longer match.

## 311: How do DynamoDB transactions work internally?

DynamoDB uses a transaction coordinator and a two-phase protocol:

1. **Prepare**: the coordinator asks every involved partition to check conditions and lock (prepare) the items.
2. **Commit**: if all prepares succeed, the coordinator tells them to apply the writes. If any fails, it cancels everything.

Transaction state is kept durably so a coordinator failure doesn't leave half-done transactions. Because of the extra round trips, transactions cost twice the capacity and have higher latency than single writes.

## 312: What isolation levels do DynamoDB transactions give?

- Between transactions and other transactions or single-item writes: **serializable**. They behave as if they ran one after another.
- `TransactGetItems` vs other operations: serializable.
- `BatchGetItem`, `Query` and `Scan` vs transactions: **read committed**. You never see uncommitted changes, but a `Query` might see some items from before a transaction and some from after, since it isn't one snapshot.

So if you need a consistent view of several items, use `TransactGetItems`, not a batch or a query.

## 313: What is the difference between a batch and a transaction?

| Batch (BatchWriteItem)            | Transaction (TransactWriteItems)     |
| --------------------------------- | ------------------------------------ |
| Up to 25 puts/deletes             | Up to 100 actions, including updates |
| Each item succeeds or fails alone | All succeed or all fail              |
| No conditions                     | Conditions on each action            |
| Normal capacity cost              | Double capacity cost                 |
| Can return unprocessed items      | Fails as a whole                     |

Use batches for bulk loading where partial success is fine. Use transactions for business rules that span items.

## 314: How does replication work in global tables?

Each replica table has its own stream. A replication service reads changes from each replica and applies them to the other replicas. Every item carries metadata, including a timestamp, used to resolve conflicts.

In MREC mode, replication is asynchronous, usually under a second, but can be longer during issues. Writes are confirmed locally first, so a Region failure can lose the last moments of writes that didn't replicate yet (RPO is not zero). Replication latency is visible as `ReplicationLatency` in CloudWatch.

## 315: What problems can last-writer-wins cause?

- **Lost updates**: two Regions increment a counter at the same time, and one increment is lost because the whole item version from one Region wins
- **Broken conditions**: a condition like `attribute_not_exists` passes in both Regions, so two users "claim" the same username
- **Partial state**: Region A updates field X and Region B updates field Y at the same time. One whole-item version wins, so one change disappears.

Designs that avoid this: a home Region per item or per user, writes routed to one Region, append-only data (new items instead of updates), or MRSC for the sensitive tables.

## 316: What are the trade-offs of MRSC global tables?

Pros:

- Strongly consistent reads in every Region
- Zero RPO when a Region fails
- No silent conflict resolution

Cons:

- Higher write latency, since writes wait for another Region
- Exactly three Regions (or two plus a witness), in specific Region sets
- Concurrent writes to the same item from different Regions fail with a conflict error, so the app must retry
- Some features available on MREC tables may not be supported (check the docs for current limits, like TTL or transactions)

Use MRSC for data where correctness beats latency, and MREC for everything else.

## 317: How do DynamoDB Streams shards work?

A stream is made of shards. Each shard holds records for a part of the table's key space and maps roughly to a table partition. Shards have a lifetime: when a partition splits or over time, a shard is closed and child shards are created.

Consumers must read a parent shard fully before its children to keep per-item order. Lambda and the DynamoDB Streams Kinesis Adapter handle this for you. If you write a custom consumer with `GetShardIterator` and `GetRecords`, you have to manage shard lineage yourself.

## 318: How many consumers can read from one DynamoDB stream?

AWS recommends no more than two processes reading from the same shard at the same time (one for global tables, since replication uses the stream too). More readers lead to throttling on `GetRecords`.

If you need many consumers:

- Use one Lambda that fans out to SNS, SQS or EventBridge
- Use EventBridge Pipes to an event bus
- Use Kinesis Data Streams for DynamoDB, which supports many consumers and enhanced fan-out

## 319: How is a DAX cluster built?

A DAX cluster has one primary node and up to ten read replica nodes in a VPC, ideally spread across Availability Zones. The primary handles writes (write-through to DynamoDB). All nodes serve reads from their caches.

If the primary fails, a replica is promoted. For production, use at least three nodes in different Availability Zones. The DAX client is cluster-aware and routes requests to the right nodes.

## 320: What are common pitfalls with DAX?

- **Stale query cache**: writes update the item cache but not the query cache, so query results can be stale for the query TTL
- **Writes that skip DAX**: other services writing directly to DynamoDB leave the item cache stale
- **Negative caching**: DAX caches "item not found" too, so an item created outside DAX might look missing until the TTL expires
- **Strongly consistent reads** pass through and don't benefit
- **Cost**: DAX nodes run all the time, even with no traffic
- **Lambda**: functions must be in the VPC to reach DAX

## 321: How do you deal with a hot key?

It depends on the type of hotness:

- **Hot reads on one item**: cache it (DAX, ElastiCache, in-process cache with a short TTL, or CloudFront for public data)
- **Hot writes to one item**: shard the item into N items and combine on read, or buffer writes (SQS, Kinesis) and apply them in batches
- **Hot partition with many items**: improve the key so it has more distinct values, or add a shard suffix
- **Hot GSI key**: change the GSI key, add a shard suffix, or make it a sparse index

Contributor Insights shows you which keys are hot.

## 322: How do you read data back from a sharded key?

If you added a random suffix `0..N-1`, query all shards in parallel and merge:

```js
const SHARDS = 10;

const pages = await Promise.all(
  Array.from({ length: SHARDS }, (_, i) =>
    doc.send(
      new QueryCommand({
        TableName: "Events",
        KeyConditionExpression: "pk = :pk AND sk BETWEEN :from AND :to",
        ExpressionAttributeValues: {
          ":pk": `DAY#2026-10-29#${i}`,
          ":from": "2026-10-29T10:00",
          ":to": "2026-10-29T11:00",
        },
      }),
    ),
  ),
);

const items = pages
  .flatMap((p) => p.Items)
  .sort((a, b) => a.sk.localeCompare(b.sk));
```

Pick the number of shards from the expected peak. More shards means more write room but more read requests. Each shard also needs its own pagination.

## 323: How do you find out if you have a hot partition?

- Throttling on the table or a GSI while total consumed capacity is well under the limit
- Contributor Insights showing a few keys with most of the traffic or throttles
- Throttling reasons in newer SDK errors that point to key-level limits
- CloudWatch metrics per operation showing spikes tied to one feature

Then look at the code path behind those keys: a global counter, a status-based GSI, a "today" date key, or a single popular tenant.

## 324: What kinds of throttling exist in DynamoDB?

- **Partition level**: one key or partition goes over 3,000 RCU / 1,000 WCU
- **Table or index level**: provisioned capacity or the on-demand maximum is reached
- **On-demand scaling**: traffic grows faster than double the previous peak
- **GSI back pressure**: table writes throttled because a GSI can't keep up
- **Account level**: the per-account, per-Region throughput quota is reached
- **Control plane**: too many `CreateTable`, `UpdateTable` or similar calls

Each one has a different fix, so first find which one you're hitting.

## 325: How would you design a table for 1 million writes per second?

- Partition key with very high cardinality and even traffic (for example device id or event id)
- Quota increase for the account and table, requested ahead of time
- Pre-warm the table and GSIs with warm throughput
- Keep items small, ideally under 1 KB, so each write is 1 WCU
- Few or no GSIs, since each multiplies writes
- Batch writes from many concurrent workers, with retries and backoff
- Avoid strictly increasing sort keys on the same partition key
- Load test early, watching throttling per key with Contributor Insights

At that scale cost is a big factor, so check whether Kinesis + S3 would fit the use case better.

## 326: What happens to pagination if items change while you are paging?

Pagination isn't a snapshot. `ExclusiveStartKey` just tells DynamoDB to continue after that key. So:

- Items added after the cursor position will show up in later pages
- Items added before the cursor position won't show up
- Deleted items simply don't appear
- An item whose sort key changes (delete + insert) can show up twice or not at all

If you need a stable view, export or copy the data first, or accept and handle these cases in the UI.

## 327: How does DynamoDB split a table into scan segments?

Segments divide the table's key hash space into equal parts. Each segment covers a range of hashes, not a range of items, so segments can have uneven amounts of data if the data is uneven.

Pick `TotalSegments` based on table size (AWS suggests about one segment per 2 GB as a starting point) and the throughput you're willing to use. Each segment still returns 1 MB per page, so each worker loops through its own pages.

## 328: How would you design a URL shortener with DynamoDB?

Access patterns: create short code, resolve code to URL (very hot), list a user's links.

| pk         | sk   | url                 | userId | GSI1PK   | GSI1SK     |
| ---------- | ---- | ------------------- | ------ | -------- | ---------- |
| CODE#aZ3k9 | LINK | https://example.com | u-1    | USER#u-1 | 2026-10-29 |

- Create: generate a random code and `PutItem` with `attribute_not_exists(pk)`. On conflict, generate another code.
- Resolve: `GetItem` by code, cached with DAX or CloudFront
- List: query GSI1 by user
- Click counts: separate counter items, or send click events to Kinesis and aggregate, so the hot link item isn't written on every click
- Expiring links: TTL

## 329: How would you model a chat application?

Access patterns: list a user's conversations ordered by last message, list messages in a conversation (newest first, paginated), send a message.

| pk       | sk                          | notes                     |
| -------- | --------------------------- | ------------------------- |
| CONV#c-1 | MSG#2026-10-29T10:00:00#m-1 | message                   |
| CONV#c-1 | META                        | participants, title       |
| USER#u-1 | CONV#c-1                    | membership, lastMessageAt |

- Messages: query `pk = CONV#c-1`, `begins_with(sk, 'MSG#')`, descending
- User's conversations by last activity: GSI on `USER#u-1` with `lastMessageAt` as the sort key
- On send: put the message, and update `lastMessageAt` on each membership (directly or via a stream)

For very busy group chats, time-bucket the conversation partition key. Use AppSync subscriptions or WebSockets to push new messages.

## 330: How would you design an e-commerce order system?

- Orders keyed by `ORDER#id`, with items under the same partition key
- Customer's orders through `CUSTOMER#id` items or a GSI with date sort key
- Inventory items per product with conditional decrements
- Checkout as a transaction: create order, decrement stock for each product, and record the payment intent
- Order status changes with conditional updates (state machine)
- Streams to send confirmation emails, update search, and publish events
- Admin views ("orders by status today") through a sparse or bucketed GSI
- Reporting through export to S3 or zero-ETL to Redshift, not scans

Keep the transaction small: if an order has more than 100 products, split stock reservation into steps with compensation.

## 331: How would you build a social feed?

Two common approaches:

- **Fan-out on write**: when a user posts, write a feed item to each follower's feed (`pk = FEED#follower`, `sk = timestamp#postId`). Reading is one fast query. Writing is expensive for users with many followers.
- **Fan-out on read**: store posts by author. To build a feed, query recent posts of each followed author and merge. Cheap writes, expensive reads.

Most real systems mix them: fan-out on write for normal users, fan-out on read for celebrities. Fan-out work runs asynchronously from a stream through SQS workers. Use TTL to cap feed length over time.

## 332: How would you design inventory reservation during checkout?

1. On "add to checkout", decrement `available` and increment `reserved` with a condition `available >= :qty`, and create a reservation item with a TTL (for example 15 minutes).
2. On payment success, in a transaction: delete the reservation and decrement `reserved`.
3. On expiry, the TTL delete appears in the stream. A Lambda moves the quantity back from `reserved` to `available`.

Since TTL can be late, also run a scheduled job that releases reservations past their expiry time, and make the release idempotent by deleting the reservation item with a condition.

## 333: How would you build a job scheduler or delayed queue?

Store jobs with a time bucket so a worker can query due jobs:

```text
pk = DUE#2026-10-29T10:15   (minute bucket, maybe sharded)
sk = <runAt>#<jobId>
status = PENDING
```

- A scheduled worker queries the current and past buckets
- It claims each job with a conditional update from `PENDING` to `RUNNING`
- It deletes or marks the job as done when finished

For simple delays, EventBridge Scheduler or SQS delay queues are often easier. DynamoDB works well when you need to query, edit or cancel scheduled jobs.

## 334: How would you build a large-scale leaderboard?

A single GSI partition sorted by score breaks down with many writes. Options:

- **Sharded scores**: write each player to one of N score shards. To get the top 10, query the top 10 of each shard and merge.
- **Score buckets**: partition by score range (`BUCKET#9000-9999`) to find rank ranges
- **Periodic snapshots**: a job computes the top N from an export or from streams and saves it as one item that everyone reads
- **ElastiCache sorted sets** for real-time ranks, with DynamoDB as the durable store

Exact global rank of any player ("you are #84,213") is expensive in DynamoDB, so use approximate ranks or a cache.

## 335: How do you isolate tenants of very different sizes?

A common setup is a pooled table for small tenants (tenant id in the key) and dedicated tables or accounts for large or regulated tenants. Things to handle:

- One big tenant can create hot partitions in a pooled table, so shard its keys or move it out
- Noisy neighbors: watch per-tenant traffic with Contributor Insights and app metrics
- Per-tenant limits in the app layer
- Tenant offboarding: deleting all items for one tenant in a pooled table is slow, while dropping a dedicated table is instant
- Routing: a tenant catalog that tells the app which table holds each tenant

## 336: How would you design an audit log in DynamoDB?

- Write each audit event as a new item (append-only), never update it
- Key: `pk = ENTITY#<type>#<id>`, `sk = <timestamp>#<eventId>` for history per entity
- GSI for "actions by user" with `pk = USER#id`
- Capture events with Streams so app code can't forget to write them
- Use IAM to deny `UpdateItem` and `DeleteItem` on the audit table to everyone except an admin role
- Export old events to S3 with Object Lock for long-term retention, and remove them with TTL

## 337: How does the Powertools idempotency utility use DynamoDB?

Powertools for AWS Lambda (Python, TypeScript, Java, .NET) stores a record per request, keyed by a hash of the event (or a part of it you choose):

1. Before running the handler, it writes an `INPROGRESS` record with `attribute_not_exists`
2. If that fails, a record already exists: it returns the stored result, or raises an error if the first call is still running
3. After success, it saves the result as `COMPLETED` with a TTL

```ts
import { makeIdempotent } from "@aws-lambda-powertools/idempotency";
import { DynamoDBPersistenceLayer } from "@aws-lambda-powertools/idempotency/dynamodb";

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: "IdempotencyTable",
});

export const handler = makeIdempotent(async (event) => processPayment(event), {
  persistenceStore,
});
```

## 338: What are the weak points of a DynamoDB-based lock?

- **Clock skew**: lease expiry depends on clocks of different machines
- **Process pauses**: a worker can pause (GC, CPU starvation) past its lease while still believing it holds the lock
- **Lost releases**: a crashed worker holds the lock until the lease expires

To make it safer, use fencing tokens: increment a counter each time the lock is taken, and have the protected resource reject writes with an older token. Also keep the lease short and renew it with a heartbeat (a conditional update on `owner`). AWS's `DynamoDBLockClient` library for Java does this.

## 339: How do you get exactly-once processing from DynamoDB Streams?

Streams deliver each record once, but Lambda can retry a batch, so your code may see records more than once. To make the effect exactly-once:

- Make side effects idempotent: conditional writes keyed by the record's `eventID` or the item version
- Store processed `eventID`s with a TTL and skip ones you've seen
- When writing to another DynamoDB table, use a condition like `version < :newVersion` so replays and out-of-order applies don't go backwards

"Exactly once" in practice means "at least once delivery plus idempotent processing".

## 340: How do you keep aggregates correct with Streams?

- Process `INSERT`, `MODIFY` and `REMOVE` and compute the difference using old and new images (`NEW_AND_OLD_IMAGES`)
- Don't add the full value on `MODIFY`. Add `new - old`.
- Handle TTL deletes as removals
- Make updates idempotent (store last processed sequence per source item, or use versions)
- Run a periodic job that recomputes aggregates from an export to fix any drift

```js
const delta = (newImage?.amount ?? 0) - (oldImage?.amount ?? 0);
if (delta !== 0) {
  await addToDailyTotal(day, delta);
}
```

## 341: How do you handle a poison record in a stream?

A record that always makes the function fail blocks its shard, because Lambda retries until the record expires (24 hours). To avoid this:

- Set `MaximumRetryAttempts` and `MaximumRecordAgeInSeconds`
- Enable `BisectBatchOnFunctionError` so Lambda narrows down the bad record
- Use `ReportBatchItemFailures`
- Configure an on-failure destination (SQS or SNS) to save details of skipped records
- Catch expected errors in code and send the record to your own dead-letter store

Monitor `IteratorAge`. When it grows steadily, a shard is stuck.

## 342: Is there any ordering across different items in a DynamoDB stream?

No global order. Order is guaranteed only for changes to the same item. Changes to items in different partitions are in different shards and can be processed in any order relative to each other.

If you need order across items, for example "order created" before "payment captured" on different items, put a sequence number or timestamp in the data and let consumers handle late events. Or put both events under the same item collection and process them by key.

## 343: How do you build a change data capture pipeline to a data lake?

Options, from simplest:

1. **Scheduled incremental exports** to S3, then process with Glue or Athena (often in Apache Iceberg format)
2. **Zero-ETL integration** to SageMaker Lakehouse or Redshift
3. **Kinesis Data Streams for DynamoDB** to Amazon Data Firehose to S3 in Parquet, near real time

Things to handle: deduplication (Kinesis can have duplicates), ordering by approximate creation time, deletes (including TTL), and schema differences between entity types in single-table designs.

## 344: What do you do when access patterns change after launch?

1. Check if an existing key or GSI can serve the new pattern with a small change
2. If not, add a GSI (possibly with a multi-attribute key, so you don't need new synthetic attributes)
3. If the GSI needs a new attribute, write it in code first, then backfill old items
4. If the pattern needs aggregated or joined data, build it with Streams into new items
5. If the pattern is analytical, send it to Redshift, Athena or OpenSearch instead

Changes to the base table key are a migration to a new table. That's why the first modeling pass should list access patterns carefully.

## 345: How would you migrate from a relational database to DynamoDB?

1. List every query the app makes today, with frequency and latency needs
2. Design the DynamoDB model around those queries, not around the existing tables
3. Build a translation layer that writes the new item shapes
4. Bulk load the history: export from SQL to S3 and use import from S3, or use AWS DMS
5. Keep them in sync during the cutover: dual writes, or CDC with DMS
6. Compare results by running reads against both and logging differences
7. Switch reads, then writes, and keep the old database for rollback for a while

The hardest part is usually reporting queries. Plan where those will run after the move.

## 346: How do you migrate a live table with zero downtime?

1. Create the new table
2. Start streaming changes from the old table to the new one (Lambda on the stream, converting items)
3. Backfill existing items with a scan or an export/import, with conditions so the backfill doesn't overwrite newer streamed changes (compare a version or `updatedAt`)
4. Verify: item counts, checksums on samples, shadow reads
5. Switch reads to the new table behind a feature flag
6. Switch writes, then stop the stream consumer
7. Keep the old table read-only until you're sure

Version attributes on every item make the conflict checks in step 3 simple.

## 347: How do you copy a table to another account or Region?

- **Export to S3 + import from S3**: export to a bucket the target account can read, then import into a new table there. No read or write capacity used.
- **AWS Backup**: copy a backup to another account or Region and restore it
- **Global tables**: for another Region in the same account, add a replica
- **Restore from PITR** directly into another Region

For ongoing sync between accounts, use a stream consumer that writes to the target table with a cross-account role.

## 348: How do you model costs for a big workload?

Build a small spreadsheet from real numbers:

- For each access pattern: requests per second, items per request, item size, consistency
- For each write: item size and which GSIs it touches (each GSI write is billed separately)
- Storage growth per month, including GSIs and replicas
- Streams, backups, PITR, exports

Then compare on-demand vs provisioned with auto scaling vs provisioned plus reserved capacity. Run a load test and compare `ConsumedCapacity` against your estimates. Real item sizes are often bigger than expected.

## 349: When does provisioned capacity become cheaper than on-demand?

Provisioned is billed for capacity all the time. On-demand is billed per request. So it depends on average utilization: if your provisioned capacity would be used at a high rate most hours (with auto scaling tracking it closely), provisioned is cheaper. If traffic has big peaks and long quiet periods, on-demand wins.

After the late-2024 price cut, the break-even moved toward higher utilization, so many steady workloads are fine on on-demand too. Reserved capacity shifts it back toward provisioned for large, stable tables.

## 350: Why do GSIs increase write costs so much?

Every write to the table that touches indexed attributes also writes to each affected GSI, billed at the GSI's item size. If an update changes a GSI key, it's a delete plus an insert in that index: two writes.

A table with 5 GSIs and `ALL` projection can cost up to 6 times (or more) the writes of the table alone. To keep it under control: use sparse indexes, project only needed attributes, overload GSIs instead of adding new ones, and don't update GSI key attributes unless necessary.

## 351: How does rounding of capacity units affect cost?

Writes round up to 1 KB, reads to 4 KB per item. So:

- A 1.1 KB item costs 2 WCU per write, almost double a 1 KB item
- In a `Query`, reads are summed over all items and then rounded up once, so many small items are efficient
- `BatchGetItem` and `GetItem` round each item separately

Watching item sizes near the boundaries (just above 1 KB) can cut write costs a lot for high-volume tables.

## 352: How do you reduce the cost of frequent small updates on big items?

Each update is billed on the full item size (before or after, whichever is larger), not on the changed bytes. Updating a counter on a 20 KB item costs 20 WCU.

Fix it by moving fast-changing fields to their own small items:

```text
pk = PRODUCT#1, sk = META     (20 KB, rarely changes)
pk = PRODUCT#1, sk = COUNTERS (100 bytes, views, likes)
```

Now each counter update costs 1 WCU.

## 353: How do you estimate whether Standard-IA saves money?

Compare the two bills for your table:

- Standard: storage x Standard price + requests x Standard price
- Standard-IA: storage x lower IA price + requests x higher IA price

If storage is a large part of the cost and requests are low, IA wins. For example, a 2 TB order history table read a few times per day saves a lot. A 10 GB table with heavy traffic costs more on IA. Check with real numbers from Cost Explorer before switching.

## 354: How does TTL help with costs at scale?

- Deleting items with TTL is free, while deleting them yourself costs one WCU each (plus GSI writes)
- Removing old data lowers storage cost, which grows forever without it
- Smaller tables mean faster exports and restores

A typical setup: keep 90 days of events hot in DynamoDB with TTL, and archive deleted items to S3 from the stream for long-term needs.

## 355: How do you restrict which attributes a user can read or write?

Use the `dynamodb:Attributes` condition key together with `dynamodb:Select` and `dynamodb:ReturnValues`:

```json
{
  "Effect": "Allow",
  "Action": ["dynamodb:GetItem", "dynamodb:Query"],
  "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Users",
  "Condition": {
    "ForAllValues:StringEquals": {
      "dynamodb:Attributes": ["userId", "name", "avatarUrl"]
    },
    "StringEqualsIfExists": {
      "dynamodb:Select": "SPECIFIC_ATTRIBUTES"
    }
  }
}
```

Requests must then use a `ProjectionExpression` with only those attributes. This is fine-grained access control at the attribute level. It's harder to manage than app-level checks, so it's mostly used when clients access DynamoDB directly with temporary credentials.

## 356: How can you use attribute-based access control (ABAC) with DynamoDB?

Tag tables (for example `team=payments`, `env=prod`) and write IAM policies that compare principal tags with resource tags:

```json
{
  "Effect": "Allow",
  "Action": "dynamodb:*",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:ResourceTag/team": "${aws:PrincipalTag/team}"
    }
  }
}
```

New tables are covered automatically when they're tagged correctly, so you don't need to update policies for each table. Protect the tagging actions too, or users could tag their way into access.

## 357: How do you stop data from leaving your network through DynamoDB?

- Use VPC endpoints and endpoint policies that allow only your tables
- Add `aws:SourceVpce` or `aws:SourceVpc` conditions in table resource policies so the table can only be reached through your endpoints
- Use SCPs to block access to DynamoDB tables outside your organization (`aws:ResourceOrgID`)
- Turn on CloudTrail data events and alert on unusual access, like large scans or exports
- Limit who can call `ExportTableToPointInTime` and to which buckets

The goal is to block both outsiders reading your tables and insiders copying data to tables or buckets they control.

## 358: What happens if a customer managed KMS key is disabled?

DynamoDB can no longer decrypt the table. Requests start to fail, and the table status changes to `INACCESSIBLE_ENCRYPTION_CREDENTIALS`. If the key stays unavailable for seven days, DynamoDB archives the table (`ARCHIVING`, then `ARCHIVED`). An archived table can't be used, but can be restored from its archive backup once the key is available again.

So key admins can effectively take a table offline. Protect key policies, use key deletion waiting periods, and alarm on key state changes.

## 359: How does searchable encryption work in the AWS Database Encryption SDK?

Encrypted attributes can't be queried directly, because the stored value is random-looking ciphertext. The SDK adds beacons: truncated HMACs of the plaintext stored in extra attributes. You can put a beacon into a GSI key and query it with an exact match.

Beacons are truncated on purpose, so several values share the same beacon. This hides value frequency from someone looking at the table, at the cost of false positives that the SDK filters out after decryption. Choosing beacon length is a trade-off between privacy and query efficiency.

## 360: How do you meet compliance requirements for a DynamoDB table?

- Encryption with a customer managed key and key rotation
- PITR on, plus AWS Backup with vault lock and cross-account copies
- Deletion protection on, and SCPs that deny `DeleteTable` and `DeleteBackup` for most roles
- CloudTrail management and data events, sent to a separate log account
- Least-privilege IAM, resource policies and VPC endpoints
- AWS Config rules to check settings (PITR on, encryption, auto scaling)
- TTL or scheduled deletes for data retention rules
- Client-side encryption for the most sensitive fields

## 361: Is PartiQL vulnerable to injection?

It can be, if you build statements by joining strings with user input:

```js
// unsafe
const Statement = `SELECT * FROM "Users" WHERE userId = '${input}'`;
```

Input like `x' OR begins_with(userId, '')` could change the meaning and turn the query into a scan of other users' data. Always use parameters:

```js
new ExecuteStatementCommand({
  Statement: 'SELECT * FROM "Users" WHERE userId = ?',
  Parameters: [input],
});
```

Also limit IAM permissions so even a mistake can't read tables it shouldn't.

## 362: What risks come with building expressions dynamically?

When you build `UpdateExpression` or `FilterExpression` from user input, such as a list of fields to update:

- Never put user input into the expression string itself
- Map field names through `ExpressionAttributeNames` with generated placeholders
- Only allow known field names (allow-list), so users can't update `role` or `pk`
- Put values only in `ExpressionAttributeValues`

```js
const allowed = new Set(["name", "bio", "avatarUrl"]);
const fields = Object.entries(body).filter(([k]) => allowed.has(k));

const UpdateExpression =
  "SET " + fields.map((_, i) => `#f${i} = :v${i}`).join(", ");
const ExpressionAttributeNames = Object.fromEntries(
  fields.map(([k], i) => [`#f${i}`, k]),
);
const ExpressionAttributeValues = Object.fromEntries(
  fields.map(([, v], i) => [`:v${i}`, v]),
);
```

## 363: What are the main hard limits you should know?

- Item size: 400 KB
- Partition key: 2048 bytes. Sort key: 1024 bytes.
- Query or Scan page: 1 MB
- BatchGetItem: 100 items / 16 MB. BatchWriteItem: 25 items / 16 MB.
- Transactions: 100 actions / 4 MB
- Nested attribute depth: 32 levels
- Expression strings: 4 KB each
- LSIs: 5 per table, 10 GB per item collection when an LSI exists
- Projected attributes in INCLUDE across all indexes: 100
- Stream retention: 24 hours
- Per partition: 3,000 RCU, 1,000 WCU

Adjustable quotas include GSIs per table (default 20), tables per Region, and throughput per table and account.

## 364: What expression limits can surprise you?

- Each expression string (key condition, filter, update, condition, projection) can be at most 4 KB
- `ExpressionAttributeNames` and `ExpressionAttributeValues` together are limited in size (about 2 MB)
- Up to 300 operators or functions in one expression
- `IN` takes up to 100 values
- An update expression can't touch the same path twice or overlapping paths (`a` and `a.b`)

These show up when you generate expressions in code, for example a filter with hundreds of `OR` clauses. When you hit them, the design usually needs an index instead.

## 365: What are the account-level throughput quotas?

Per account and Region, there are default quotas for the total provisioned read and write capacity across all tables, and per-table maximums for on-demand and provisioned throughput (default 40,000 read and 40,000 write units per table). They are adjustable through Service Quotas.

Planning for a big launch includes checking these and asking for increases early. Hitting an account quota looks like throttling that has nothing to do with your key design.

## 366: Why do sort keys with numbers stored as strings sort strangely?

String sort keys are compared byte by byte (UTF-8), so `"10"` comes before `"9"`. If you build string keys with numbers, zero-pad them to a fixed width:

```text
ORDER#00000009
ORDER#00000010
```

Number-type sort keys sort numerically and don't need padding. But composite string keys like `SCORE#000950#PLAYER#p-1` need padding for the number part. For negative numbers in strings, you need an offset so they sort correctly.

## 367: How does DynamoDB compare string values in sort keys?

By the raw bytes of the UTF-8 encoding. This means:

- Uppercase letters sort before lowercase (`"Z"` < `"a"`)
- Accented letters sort after all ASCII letters
- There's no locale-aware collation

Normalize case for sort keys that users see as alphabetical lists, and keep the display value in another attribute. Separators matter too: `#` (0x23) sorts before digits and letters, which is useful for prefix design.

## 368: Why can a Query return zero items but still have a LastEvaluatedKey?

Because of `Limit` and filters. DynamoDB read up to `Limit` items (or 1 MB), the filter removed all of them, and there are more items to read. The result is an empty page with a key to continue.

Code that stops on the first empty page will miss data. Always loop on `LastEvaluatedKey`, not on whether `Items` is empty.

## 369: What can go wrong if you store TTL in milliseconds?

A millisecond timestamp like `1761730000000` read as seconds is far in the future, so the items are never deleted. Your table keeps growing, and no error tells you something is wrong.

Also, values that are more than five years in the past are ignored by TTL. Always use `Math.floor(Date.now() / 1000)` and check after enabling TTL that items are actually being deleted (the `TimeToLiveDeletedItemCount` metric).

## 370: Why can't a transaction touch the same item twice?

DynamoDB rejects a `TransactWriteItems` (or `TransactGetItems`) with two actions on the same primary key, with a `ValidationException`. The transaction locks each item once, so two different changes to one item in the same transaction aren't allowed.

Combine the changes into one action. For example, instead of a `ConditionCheck` and an `Update` on the same item, put the condition on the `Update`.

## 371: Do failed conditional writes cost capacity?

Yes. When a condition fails, DynamoDB still had to read the item to check it, and it charges the write capacity based on the item size, as if the write had happened. Failed transactions are also charged.

So designs that expect many conditional failures, for example many workers racing for the same job, can cost more than expected. Watch `ConditionalCheckFailedRequests` and reduce the races, for example by spreading workers over different keys.

## 372: Can you rely on DeleteItem to tell you if an item existed?

Not by default. Deleting a missing item succeeds and costs one WCU. To know whether it existed:

- `ReturnValues: 'ALL_OLD'`: `Attributes` is empty if nothing was deleted
- `ConditionExpression: 'attribute_exists(pk)'`: fails if the item wasn't there

Use the condition when "not found" should be an error, like a 404 response.

## 373: How do you handle a GSI with low-cardinality keys?

A GSI keyed by something like `status` puts all `PENDING` items in one partition key. With high write rates, that GSI partition gets hot, and back pressure throttles the table.

Fixes:

- Add more attributes to the key, like `status` plus date bucket, or a multi-attribute key (`status` + `region`)
- Shard: `STATUS#PENDING#0..9`
- Use a sparse index that only includes the few items you really need (for example only `PENDING`)

## 374: Why is a time-based partition key a bad idea?

A key like `DATE#2026-10-29` puts all of today's writes into one partition key. All traffic goes to the same partition, which has a fixed limit, while the rest of the table sits idle.

If you need to query by time across all data, add the time bucket as a GSI key with sharding, and keep the base table keyed by something with high cardinality.

## 375: What happens when an item collection gets very large?

Without LSIs, there's no size limit per partition key. DynamoDB can split one item collection across partitions by sort key range. But:

- All writes to that key still share some limits, especially if they go to the same part of the sort key range
- Queries over the whole collection are slow and expensive
- With an LSI, writes fail past 10 GB

Large item collections are usually a sign that the key should include a time bucket or another dimension.

## 376: How do you load test a DynamoDB-backed service?

- Use realistic key distributions, not one test user hitting one key, and not perfectly uniform random keys either
- Use real item sizes
- Ramp up traffic over time, like real users, and also test sudden spikes
- Run against a separate table, not production, but with the same settings and GSIs
- Pre-warm the test table if you're testing a launch scenario
- Watch throttles per table and GSI, latency percentiles, `ConsumedCapacity`, and Contributor Insights
- Include stream consumers in the test, since they often fall behind first

## 377: How do you prepare a table for a known traffic spike?

- Raise warm throughput on the table and each GSI a few days ahead
- In provisioned mode, raise the auto scaling minimum before the event
- Check account and table quotas and raise them early
- Review hot keys: the sale's top products, a single campaign id
- Add caching for the hottest reads
- Raise Lambda concurrency for stream consumers, or increase the parallelization factor
- Prepare a plan to turn off non-critical writes (feature flags) if throttling starts

## 378: How do you design for a full Region outage?

- **Global tables** with replicas in two or more Regions, and the app deployed in each
- Route users with Route 53 health checks or a global load balancer
- Decide the conflict strategy: home Region per entity, or MRSC
- Make sure everything the app needs also exists in the other Region: secrets, KMS keys (multi-Region keys), config
- Practice failover regularly, not just once

If a few seconds of lost writes are acceptable, MREC is enough. If not, use MRSC for the critical tables.

## 379: What are the RPO and RTO of different DynamoDB recovery options?

| Option             | RPO                     | RTO                                       |
| ------------------ | ----------------------- | ----------------------------------------- |
| PITR               | About 5 minutes or less | Restore time, can be hours for big tables |
| On-demand backup   | Time since last backup  | Restore time                              |
| Global tables MREC | Usually seconds         | Minutes, just reroute traffic             |
| Global tables MRSC | Zero                    | Minutes, just reroute traffic             |

Backups protect against bad data (bugs, deletes). Global tables protect against Region failures, but they also replicate bad writes instantly, so you need both.

## 380: How do you route writes in an active-active global table setup?

Common strategies:

- **Home Region per user or tenant**: store each user's home Region, and send their writes there. Reads can come from any Region.
- **Regional ownership of data**: each Region writes only its own items (for example orders created in that Region)
- **Single writer Region**: one Region takes all writes, others are read-only until failover

These avoid concurrent writes to the same item from different Regions, which is where last-writer-wins causes problems.

## 381: How do you lower latency from the client side?

- Keep one client per process and reuse connections (keep-alive)
- Deploy compute in the same Region as the table, and use VPC endpoints
- Use eventually consistent reads where possible
- Fetch only needed attributes, and keep items small
- Run independent requests in parallel with `Promise.all`
- Set short timeouts so slow requests are retried quickly
- Pre-load the SDK and open a connection during Lambda init
- Use DAX or a local cache for hot items

## 382: How do retries affect tail latency?

Most requests finish in a few milliseconds, but a small number take much longer (a slow node, a leader election). Retries help those slow requests finish, but they can also stack: a request that times out three times with backoff can take seconds.

Set a short `requestTimeout`, a small `maxAttempts`, and use jitter on backoff. For very latency-sensitive reads, some teams send a second request if the first doesn't respond in time (hedged requests), at the cost of extra reads.

## 383: What is a retry storm and how do you avoid it?

When DynamoDB throttles, every client retries. If they all retry at the same time, they cause even more throttling, and the system doesn't recover.

To avoid it:

- Exponential backoff with full jitter (the SDK does this)
- `adaptive` retry mode, which slows the client down on throttling
- Limit total retries at each layer. Don't stack SDK retries with app retries and Lambda retries without thinking.
- Circuit breakers or load shedding for non-critical traffic

## 384: How does Lambda concurrency interact with DynamoDB?

Each Lambda instance makes its own requests, so high concurrency means many parallel requests. If the table or a hot key can't handle that, you get throttling, retries and longer Lambda runtimes, which in turn raise concurrency further.

Ways to keep it under control:

- Reserved concurrency on functions that write in bulk
- SQS in front of write-heavy work, with a maximum concurrency on the event source
- Batch writes instead of one write per message

## 385: How does ParallelizationFactor affect stream processing?

By default, Lambda runs one batch per stream shard at a time. With `ParallelizationFactor` set up to 10, Lambda runs up to 10 batches per shard at the same time, grouped by partition key. Records with the same partition key still go to the same batch processor in order.

It helps when a stream is falling behind (rising `IteratorAge`). The trade-off is more concurrent invocations and more parallel writes to downstream systems.

## 386: What are tumbling windows in stream processing?

Lambda can group stream records into fixed time windows (up to 15 minutes) and pass state between invocations within the window. At the end of the window, your function gets a flag and can write the final result.

```js
export const handler = async (event) => {
  const state = event.state ?? { count: 0 };
  state.count += event.Records.filter((r) => r.eventName === "INSERT").length;

  if (event.isFinalInvokeForWindow) {
    await saveCount(event.window.start, state.count);
    return {};
  }
  return { state };
};
```

It's useful for per-minute counts without writing to DynamoDB on every record. State is per shard, so you still combine results from different shards.

## 387: When would you use EventBridge Pipes instead of a Lambda stream consumer?

Pipes are a good fit when you only need filter, small transform and deliver: for example publishing domain events to an EventBridge bus or sending messages to SQS. There's no code to maintain, and retries and dead-letter handling are built in.

Use Lambda when you need real logic: writes to several places, idempotency, aggregations, calls to external APIs. You can also combine them: a Pipe with a Lambda enrichment step.

## 388: How do you handle snapshots in an event-sourced DynamoDB model?

Replaying all events for an aggregate gets slow as events pile up. Store a snapshot every N events:

```text
pk = ACCOUNT#a-1, sk = EVENT#000001200   (event)
pk = ACCOUNT#a-1, sk = SNAPSHOT#000001200 (state after event 1200)
```

To load: query the latest snapshot (`begins_with(sk, 'SNAPSHOT#')`, descending, `Limit: 1`), then query events after its sequence number. Writing a snapshot doesn't need to be atomic with the event, since snapshots are just a cache of computed state.

## 389: How do you implement CQRS with DynamoDB?

- **Write side**: commands update items with conditions and transactions, focused on correctness
- **Change feed**: DynamoDB Streams (or Pipes) publish each change
- **Read side**: consumers build read models in other DynamoDB tables, OpenSearch, or a cache, each shaped for a specific screen or API

The read side is eventually consistent. After a command, the UI might need to show the result from the command response instead of re-reading the read model right away.

## 390: How do you handle graph-like queries in DynamoDB?

DynamoDB can handle simple relationships with adjacency lists (one hop: "followers of X", "groups of Y"). Multi-hop queries like "friends of friends who like Z" need many queries and grow quickly.

Options:

- Precompute the common multi-hop results with Streams
- Limit the depth and size in the product design
- Use Amazon Neptune for real graph traversal, and keep DynamoDB for the main data

## 391: How do you replace joins in DynamoDB?

1. **Pre-join**: store related items in the same item collection, so one query returns them
2. **Denormalize**: copy the few fields you need into the item
3. **Application join**: query, collect ids, then `BatchGetItem` the related items
4. **Materialize**: use Streams to keep a pre-joined view up to date

Option 1 is the core idea of single-table design. Option 3 is fine when the second lookup is small and bounded.

## 392: How do you do aggregations like SUM or GROUP BY?

DynamoDB has no aggregation functions. You choose between:

- **Pre-compute**: keep running totals updated on write (transaction) or from Streams
- **Compute on read**: query the items and sum in code, only for small result sets
- **Offload**: export to S3 for Athena, zero-ETL to Redshift, or OpenSearch aggregations

For dashboards that need fresh numbers, pre-computed aggregates per time bucket (per minute, hour, day) are the usual approach.

## 393: Can DynamoDB do vector or semantic search?

In 2026 AWS announced native vector search for DynamoDB, which lets you store embeddings and run similarity queries on them, with filters on other attributes. Before that, the usual pattern was to keep the source data in DynamoDB and sync embeddings to OpenSearch (through zero-ETL or Streams), or to use a separate vector store.

Since this feature is new, check the current DynamoDB documentation for exact APIs, limits and pricing before designing around it. Questions to ask: which index settings it supports, how recall and latency behave at your data size, and how much it costs compared to OpenSearch.

## 394: How do you design keys that support several sort orders?

Each sort order needs its own key, so you use the table's sort key for one order and GSIs for the others:

- Table: `pk = CATEGORY#books`, `sk = createdAt#productId` (newest)
- GSI1: `pk = CATEGORY#books`, `sk = price#productId` (by price)
- GSI2: `pk = CATEGORY#books`, `sk = rating#productId` (by rating)

Add the item id at the end of the sort key so ties don't collapse or reorder randomly. If users can sort and filter by many fields at once, use a search engine instead of adding GSIs for every combination.

## 395: When should you use multi-attribute GSI keys instead of synthetic keys?

Multi-attribute keys are better when:

- The parts already exist as attributes, so you don't need to write and keep extra concatenated attributes in sync
- Parts have different types (for example a number for priority), which a concatenated string handles badly
- You're adding a new index to a big table and don't want to backfill synthetic attributes first

Synthetic keys are still useful when:

- You overload one GSI across many entity types with different key shapes
- You need key parts that don't exist as attributes, like a shard number or a constant prefix
- You need prefix queries (`begins_with`) across parts of the key

## 396: How do you store all versions of a document and query them by date?

Use the version pattern with dates in the sort key:

```text
pk = DOC#d-1, sk = V#2026-10-29T10:00:00Z   (each version)
pk = DOC#d-1, sk = LATEST                    (pointer or copy)
```

- History: `begins_with(sk, 'V#')`
- Version at a given time: `sk <= 'V#2026-09-01T00:00:00Z'`, descending, `Limit: 1`
- Latest: `GetItem` on `LATEST`

Write the new version and update `LATEST` in a transaction with a condition on the previous version. Move old versions to S3 or use TTL if history grows too much.

## 397: How do you delete all data for a tenant in a shared table?

- If every item's partition key starts with the tenant id but the rest varies, you can't query by tenant directly. Use a GSI with the tenant id as partition key (keys only), or scan.
- Query or scan the keys, then delete with `BatchWriteItem` at a controlled rate
- Or set TTL on all the tenant's items in a background job, and let DynamoDB delete them for free
- Delete from S3 exports, backups (by retention) and downstream systems too

If fast tenant deletion is a requirement, a table per tenant makes it a single `DeleteTable` call.

## 398: How do you handle GDPR "right to be forgotten" requests?

- Know every place a user's data lives: base items, denormalized copies, GSIs (deleted automatically with the item), streams consumers' targets, search indexes, exports and backups
- Delete or anonymize base items, and let streams propagate deletes to derived stores
- Backups can't be edited, so keep a short retention, or keep a list of deleted ids and re-apply deletes after any restore
- Another approach is crypto-shredding: encrypt each user's data with a per-user key and delete the key

Design for this early. Finding all copies of a user's data later is hard in a heavily denormalized model.

## 399: How do you archive cold data from DynamoDB to S3?

- TTL + stream + Lambda or Firehose to S3 (item by item, near real time)
- Scheduled incremental exports to S3 and TTL to remove old items
- For time-partitioned tables (one per month), export the old table to S3 and then delete the table

Store archives in a query-friendly format (Parquet or Iceberg) so Athena can still read them. Keep the archive's schema documented, since single-table items mix many entity types.

## 400: How do you produce a large report from DynamoDB data?

Not with scans on the live table. Options:

- Export to S3 (full or incremental) and run Athena, Glue or Spark
- Zero-ETL to Redshift and run SQL
- If the report is needed often, pre-compute it from Streams into report items

Reports from exports use no table capacity, so they can't hurt production traffic.

## 401: How does DynamoDB compare to Cassandra?

Both use partition keys and clustering (sort) keys, and model data around queries.

- **Cassandra**: open source, you run the cluster (or use Keyspaces or Astra), tunable consistency per query, leaderless replication, CQL language, wide rows with no 400 KB item limit
- **DynamoDB**: fully managed, no cluster, pay per request, leader-based replication per partition, 400 KB items, transactions and streams built in

Amazon Keyspaces is a managed Cassandra-compatible service on AWS, if you want CQL without running clusters.

## 402: When would DynamoDB be the wrong choice even at high scale?

- Workloads dominated by ad hoc analytical queries
- Highly connected data with deep traversal (social graphs, fraud graphs)
- Search-heavy products where most queries are free-text with filters and ranking
- Strong relational integrity needs across many entities, with complex transactions over hundreds of rows
- Very large objects or blobs

In these cases DynamoDB can still be part of the system (for example, the source of truth for core records), but not the only database.

## 403: How do you validate items before writing them?

DynamoDB only checks key types, so validation belongs in your code. A schema library keeps it in one place:

```ts
import { z } from "zod";

const Order = z.object({
  orderId: z.string().min(1),
  customerId: z.string().min(1),
  total: z.number().nonnegative(),
  status: z.enum(["PENDING", "PAID", "SHIPPED"]),
  createdAt: z.string().datetime(),
});

export async function saveOrder(input: unknown) {
  const order = Order.parse(input);
  await doc.send(
    new PutCommand({
      TableName: "App",
      Item: {
        pk: `ORDER#${order.orderId}`,
        sk: "META",
        type: "Order",
        ...order,
      },
    }),
  );
}
```

Validate data coming back too when old items might have an older shape.

## 404: How do you get type safety when working with DynamoDB in TypeScript?

- Define types or schemas per entity, and keep key building in one function per entity
- Use a modeling library with types (ElectroDB, DynamoDB Toolbox) so queries are type-checked against the model
- Parse results with the schema instead of casting `Item as Order`
- Keep a type for each GSI's key shape, so a wrong key name fails at compile time

The SDK's own types only know `Record<string, any>` for items, so the safety has to come from your layer on top.

## 405: How do you structure a data access layer for DynamoDB?

Hide DynamoDB details behind functions named after access patterns:

```ts
export const orderRepo = {
  getById: (orderId: string) => ...,
  listByCustomer: (customerId: string, cursor?: string) => ...,
  markShipped: (orderId: string) => ...,
};
```

- Key formats, expressions and pagination stay inside the repository
- Business code doesn't know about `pk` or `GSI1`
- Each function maps to one documented access pattern, which makes reviewing the model easy

Avoid a generic `find(filter)` method. It hides scans and encourages access patterns the table wasn't built for.

## 406: How does DynamoDB Local differ from the real service?

- No real throttling or capacity limits. Provisioned settings are accepted but ignored.
- Performance doesn't reflect production
- Some features are missing or partly supported, for example global tables, PITR, and some newer APIs
- GSIs may update immediately, so tests that pass locally can fail on real eventual consistency
- Resource policies and IAM aren't enforced

Use it for logic tests, and keep a small set of integration tests against a real AWS table in a test account.

## 407: How do you trace DynamoDB calls?

- AWS X-Ray or OpenTelemetry (AWS Distro for OpenTelemetry) instrument the SDK v3 client and show each DynamoDB call as a span with table name, operation and latency
- Lambda Powertools Tracer can wrap the client
- Log `$metadata.requestId` and consumed capacity on slow or failed calls

```ts
import { Tracer } from "@aws-lambda-powertools/tracer";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";

const tracer = new Tracer();
const client = tracer.captureAWSv3Client(new DynamoDBClient({}));
```

Traces show quickly whether latency comes from DynamoDB itself, retries, or your own code.

## 408: How would you log consumed capacity per feature?

Add `ReturnConsumedCapacity: 'INDEXES'` in your data access layer and emit it as a metric with dimensions like operation and access pattern:

```ts
const res = await doc.send(
  new QueryCommand({ ...params, ReturnConsumedCapacity: "INDEXES" }),
);

metrics.addMetric(
  "DynamoRCU",
  MetricUnit.Count,
  res.ConsumedCapacity?.CapacityUnits ?? 0,
);
metrics.addDimension("accessPattern", "listOrdersByCustomer");
```

This tells you which feature drives cost, which table-level CloudWatch metrics can't show. Sample it if call volume is very high.

## 409: How do you investigate a throttling incident?

1. Find where: table or which GSI, reads or writes (CloudWatch throttle events per index)
2. Find when: match the start to deploys, traffic changes, batch jobs or a campaign
3. Find which keys: Contributor Insights, throttling reasons in error messages, app logs
4. Check limits: provisioned capacity, auto scaling limits, on-demand max, account quotas
5. Short-term fix: raise capacity or warm throughput, pause batch jobs, cache hot reads
6. Long-term fix: change key design, shard hot keys, add GSI capacity, smooth batch jobs

## 410: Scenario: latency suddenly went up. What do you check?

- `SuccessfulRequestLatency` in CloudWatch. If it's normal, the problem is on the client side.
- Throttling and retries in SDK metrics or logs
- A deploy that changed the client setup (new client per request, keep-alive off, wrong Region)
- Item sizes or page sizes that grew
- A new strongly consistent read or transaction path
- Network: NAT gateway saturation, VPC endpoint issues, DNS
- AWS Health Dashboard for service events

Compare p50 and p99. A p99 jump with normal p50 often means retries or a hot key.

## 411: Scenario: your DynamoDB bill doubled. How do you find out why?

- Cost Explorer by usage type: reads, writes, storage, backups, replication, streams
- Per-table tags to see which table grew
- CloudWatch consumed capacity per table and GSI over time
- Recent changes: new GSI with `ALL` projection, a new scan job, a retry loop, a stream consumer rewriting items (and triggering itself), PITR or exports added, new replica Region
- Item size growth (an attribute that keeps growing)

A common cause is a stream consumer that writes back to the same table and creates an endless loop of changes.

## 412: Scenario: adding a GSI to a huge table is taking very long. What can you do?

- Backfill speed depends on the index's write capacity. For provisioned GSIs, raise its WCU during creation. On-demand indexes scale on their own, up to limits.
- Check `OnlineIndexPercentageProgress` in `DescribeTable`
- Keep the projection small: `KEYS_ONLY` or `INCLUDE` writes less data
- Make it sparse so fewer items are copied

You can't query the index until it's `ACTIVE`, so plan the feature launch around the backfill time.

## 413: Scenario: someone deleted important items by mistake. How do you recover?

1. Stop the source of deletes (bad deploy, script)
2. Find the time just before the deletes (CloudTrail data events, stream records, app logs)
3. Restore the table with PITR to that time into a new table
4. Copy only the missing items back to the live table with a script, using `attribute_not_exists` so newer data isn't overwritten
5. Check derived stores (search, caches) and fix them through the normal pipeline

Restoring to a new table and copying back is safer than switching the app to the restored table, because it keeps all writes made after the incident.

## 414: Scenario: the stream consumer's IteratorAge keeps growing. What do you do?

The consumer can't keep up or is stuck.

- Check errors: a poison record retried forever looks the same
- Check duration and throttling of the function and of the systems it writes to
- Raise `BatchSize` and `ParallelizationFactor`
- Make the handler faster: batch writes, parallel calls, fewer per-record round trips
- Check Lambda concurrency limits

Records expire after 24 hours, so act before the lag gets close to that, or you'll lose events.

## 415: Scenario: ConditionalCheckFailedRequests suddenly spikes. What could it mean?

- A retry pattern: the SDK retries a successful write after a timeout, and the conditional retry fails. Usually harmless if you treat it as success.
- Many workers racing for the same items (job claiming, locks)
- A bug in version handling for optimistic locking
- A client sending duplicate requests
- Data in an unexpected state after a migration

Log the failing conditions with `ReturnValuesOnConditionCheckFailure: 'ALL_OLD'` to see the actual item state.

## 416: Scenario: you need a new access pattern on a 5 TB table. How do you add it?

1. Check whether a GSI on existing attributes (including a multi-attribute key) can serve it. If so, create it. Backfill happens automatically.
2. If it needs a new derived attribute: deploy code that writes it on new and updated items first, then backfill old items with a parallel scan job or an export plus a batch job, at a controlled rate.
3. If it needs aggregated data, build it from an export once, then keep it updated with Streams.

Estimate the cost of the backfill first. Rewriting 5 TB of items costs a lot of write capacity, and every GSI multiplies it.

## 417: Scenario: an item is close to the 400 KB limit. What do you do?

- Find what's large: usually a list that grows, like comments or history
- Move the growing part to separate items under the same partition key (one item per comment)
- Compress large text fields
- Move blobs to S3
- Add a limit in code so the item can't grow without bound

Migrate existing big items in a background job, and make reads handle both shapes until the migration is done.

## 418: Scenario: one product is getting most of the traffic during a sale. How do you handle it?

- **Reads**: cache the product with DAX, ElastiCache or CloudFront, with a short TTL
- **Stock writes**: split the stock into N buckets (`STOCK#p-1#0..9`), each with part of the inventory. Each purchase decrements a random bucket with a condition, and moves on to another bucket if that one is empty.
- **Order writes**: key orders by order id, not by product, so they spread out
- **Counters**: buffer view and click counts through Kinesis or SQS, and update in batches

Pre-warm the table and run a load test with the expected hot-product share.

## 419: Scenario: a post goes viral and gets thousands of likes per second. How do you count them?

A single counter item can take about 1,000 writes per second at most, and fewer with bigger items.

- Shard the counter into N items and sum them on read (and cache the sum)
- Or write each like as its own item (`pk = POST#p-1#LIKE#<shard>`, `sk = userId`) to prevent duplicate likes, and update the total from Streams in batches
- Show an approximate count in the UI ("12.4K"), which removes the need for exact real-time totals

Storing each like separately also answers "did I like this post" with a `GetItem`.

## 420: Scenario: both email and username must be unique. How do you design it?

Use one transaction with three items:

```js
await doc.send(
  new TransactWriteCommand({
    TransactItems: [
      {
        Put: {
          TableName: "App",
          Item: { pk: `USER#${id}`, sk: "PROFILE", email, username },
          ConditionExpression: "attribute_not_exists(pk)",
        },
      },
      {
        Put: {
          TableName: "App",
          Item: { pk: `EMAIL#${email}`, sk: "UNIQUE", userId: id },
          ConditionExpression: "attribute_not_exists(pk)",
        },
      },
      {
        Put: {
          TableName: "App",
          Item: { pk: `USERNAME#${username}`, sk: "UNIQUE", userId: id },
          ConditionExpression: "attribute_not_exists(pk)",
        },
      },
    ],
  }),
);
```

Check `CancellationReasons` to tell the user which value is taken. On change, delete the old unique item and put the new one in the same transaction as the profile update. Normalize values (lowercase, trim) before using them as keys.

## 421: Scenario: product wants page numbers (page 1, 2, 3 ... 50). How do you handle it?

DynamoDB only supports cursor-based pagination. You can't jump to page 37 without reading the earlier pages. Options:

- Convince the product side to use "Load more" or infinite scroll with cursors
- Cache cursors for pages the user already visited, so going back is cheap
- For small result sets, read everything and paginate in memory
- For large, searchable lists, use OpenSearch, which supports offset-based paging (with its own limits)

## 422: Scenario: you need to update more than 100 items atomically. What can you do?

A transaction can't do it. Options:

- Redesign so the change touches fewer items, for example store shared data in one item that others reference
- Use a saga: a series of transactions with compensating actions if something fails
- Use a version or "generation" pointer: write all new items under a new version, then flip a single pointer item in one write, so readers switch at once
- Accept eventual consistency and make readers tolerate a mix for a short time

The pointer approach is often the cleanest when readers can follow a version id.

## 423: Scenario: how would you implement a saga across services with DynamoDB?

Use Step Functions (or your own orchestrator) with a DynamoDB item that records the saga's state:

1. Create the saga item: `status = STARTED`
2. Each step does its work with an idempotency key and updates the saga item with a condition on the expected status
3. On failure, run compensating actions in reverse order (refund payment, release stock)
4. Mark the saga as `COMPLETED` or `COMPENSATED`

Conditional updates make sure two workers can't move the saga in different directions. Step Functions can call DynamoDB directly for these updates.

## 424: Scenario: design a token bucket rate limiter that allows bursts.

Store tokens and the last refill time, and compute the refill on each request:

```js
async function take(userId, rate = 10, capacity = 50) {
  const now = Date.now() / 1000;
  const { Item } = await doc.send(
    new GetCommand({
      TableName: "Buckets",
      Key: { pk: userId },
      ConsistentRead: true,
    }),
  );
  const tokens = Math.min(
    capacity,
    (Item?.tokens ?? capacity) + (now - (Item?.ts ?? now)) * rate,
  );
  if (tokens < 1) return false;

  await doc.send(
    new PutCommand({
      TableName: "Buckets",
      Item: { pk: userId, tokens: tokens - 1, ts: now, v: (Item?.v ?? 0) + 1 },
      ConditionExpression: "attribute_not_exists(pk) OR v = :v",
      ExpressionAttributeValues: { ":v": Item?.v ?? 0 },
    }),
  );
  return true;
}
```

The version condition stops two requests from spending the same token. On `ConditionalCheckFailedException`, retry. Each request costs a read and a write, so for very high rates a cache is better.

## 425: Scenario: data must stay in specific countries. How do you design it?

- Use separate tables in Regions inside the required countries, not a global table that copies data everywhere
- Route each user to their home Region and store the routing in a small global directory (only non-sensitive data)
- If you use global tables, choose replica Regions that are all allowed for that data
- Keep exports, backups (including cross-Region copies) and logs in the allowed Regions
- Use SCPs to block DynamoDB in other Regions for those accounts

## 426: Scenario: users read their data from another Region right after writing it. What's the issue?

With MREC global tables, replication is asynchronous, so a read in another Region right after a write can return old data. Fixes:

- Keep a user "sticky" to one Region for reads and writes
- After a write, read from the Region that took the write for a short time
- Return the written data in the response instead of reading again
- Use MRSC, where strongly consistent reads in any Region return the latest data

## 427: How do you plan capacity for GSIs in a global table?

Each replica has its own copies of all GSIs. Every write, whether local or replicated, updates the GSIs in each Region. So in provisioned mode:

- Each replica's table and GSIs need enough write capacity for the total writes from all Regions, not just local writes
- Write auto scaling settings must match across replicas (DynamoDB keeps them in sync for global tables)

In on-demand mode this is handled, but the cost still scales with the number of replicas times the number of GSIs.

## 428: What do you need to fix after restoring a table?

The restored table has data and indexes, but you need to set again:

- Auto scaling policies
- Stream settings and stream consumers (new stream ARN)
- TTL
- Tags, alarms, Contributor Insights
- Resource-based policies
- IAM policies that point to the old table name or ARN
- Deletion protection and PITR

If IaC owns the table, you also need to bring the restored table into the IaC state (import) or copy data back to the original table instead.

## 429: How would you run a disaster recovery drill for DynamoDB?

- Restore a production table from PITR into a test account or a new table, and time it
- Run app smoke tests against the restored table
- For global tables, shift traffic away from one Region and check that writes and reads work in the others
- Check that alarms fired and runbooks were clear
- Record actual RTO and RPO and compare them with the targets

Do it on a schedule. A recovery plan that's never tested usually fails the first time it's needed.

## 430: How do you test what happens during throttling or failures?

- AWS Fault Injection Service has an action that pauses global table replication, so you can test how the app behaves when Regions drift apart
- Wrap the client in tests with a middleware that throws `ProvisionedThroughputExceededException` for some calls
- Run load tests against a table with low provisioned capacity on purpose

```js
client.middlewareStack.add(
  (next) => async (args) => {
    if (Math.random() < 0.1) {
      const err = new Error("throttled");
      err.name = "ProvisionedThroughputExceededException";
      throw err;
    }
    return next(args);
  },
  { step: "finalizeRequest", name: "chaos" },
);
```

Check that the app degrades well: retries, clear errors, no data loss.

## 431: How do streams behave with global tables?

Each replica has its own stream, and each stream contains changes made in that Region and changes replicated from others. Consumers in each Region see all changes.

So if you attach the same consumer (like "send email on new order") in every Region, it runs once per Region. Decide whether a consumer should run in only one Region. If it must run everywhere, store a `writtenInRegion` attribute on each write and have each Region's consumer process only its own local writes.

## 432: How do you avoid infinite loops with stream consumers that write to the same table?

A Lambda that updates items in the table it listens to creates new stream records, which trigger it again.

- Skip records the consumer itself caused (check an attribute like `updatedBy = 'stream-worker'`, or compare old and new images and skip when only the consumer's fields changed)
- Use event filtering so the function only receives the record types it handles
- Write derived data to a different table when possible

Watch for invocation counts and write costs that keep growing after a deploy. That's the usual symptom.

## 433: What is the difference between a Query with a filter and a sparse GSI, in cost?

Example: 1 million orders, 1,000 of them `PENDING`, about 1 KB each.

- Query or scan with `FilterExpression: status = PENDING`: reads about 1 GB, costing about 125,000 RCU (eventually consistent) per full pass
- Sparse GSI with only pending orders: reads about 1 MB, costing about 125 RCU

The GSI adds a little write cost when orders enter or leave the pending state, but reading is 1,000 times cheaper. When you filter out most of the data, that's a sign you need an index.

## 434: How would you model a calendar or booking system to prevent double booking?

Store one item per resource and time slot:

```text
pk = ROOM#r-1#2026-10-29
sk = SLOT#10:00
```

Book with a transaction that puts each slot item with `attribute_not_exists(pk)`, plus the booking item. If any slot is taken, the whole booking fails. For long bookings with many slots, choose a slot size that keeps transactions under 100 items, or use coarser slots.

## 435: How do you handle the clock in conditional logic?

Never trust the client's clock. Pass the server time as a value in the condition, and keep servers on synced time (they are on AWS by default).

```js
ConditionExpression: 'expiresAt > :now',
ExpressionAttributeValues: { ':now': Math.floor(Date.now() / 1000) },
```

DynamoDB itself doesn't have a "current time" function in expressions, so time comparisons always use a value you send. For distributed logic, allow some tolerance for clock skew.

## 436: What is the difference between an item collection and a partition?

An item collection is a logical group: all items with the same partition key value. A partition is a physical storage unit holding many item collections, or part of one very large collection.

You design item collections. DynamoDB manages partitions. Knowing the difference helps with questions like "why is my key hot when the table has lots of capacity": the hot item collection lives on one partition with fixed limits.

## 437: How do you choose between Streams + Lambda and transactions for keeping data in sync?

| Transactions                               | Streams + Lambda                  |
| ------------------------------------------ | --------------------------------- |
| Changes are visible together, right away   | Copies are updated a bit later    |
| Up to 100 items                            | Any number of items               |
| Double write cost, adds latency to request | Normal writes, request stays fast |
| Write fails if any part fails              | Main write succeeds, sync retried |

Use transactions when readers must never see a half-updated state. Use Streams for side effects, denormalized copies and anything that can be eventually consistent.

## 438: How do you test a data model before building the app?

- List access patterns with expected request rates
- Create the model in NoSQL Workbench with sample data that covers edge cases (big tenants, empty collections)
- Write each access pattern as an actual request and check it's a single `GetItem` or `Query`
- Load realistic data into a test table and run a small load test
- Calculate item sizes and costs per pattern

Ask "what about next year's features" early. Patterns that need a full redesign later are much more expensive than one more GSI now.

## 439: How do you handle multiple entity versions during a rolling deploy?

During a deploy, old and new code run at the same time. So:

- New code must read items written by old code (missing new attributes)
- Old code must not break on items written by new code (extra attributes are usually fine, changed meanings are not)
- Change formats in two steps: first deploy code that reads both formats, then deploy code that writes the new format
- Don't remove an attribute or index until no running code depends on it

A `schemaVersion` attribute helps readers choose the right parsing.

## 440: How do you protect production tables from risky admin actions?

- Deletion protection on all production tables
- SCPs denying `DeleteTable`, `DeleteBackup` and `UpdateTable` (or key-related changes) to most roles
- Separate accounts for production
- Read-only console roles for most engineers, with temporary elevated access through an approval process
- CloudTrail alerts on control-plane changes
- IaC as the only path for table changes, with review

## 441: How would you implement a "recently viewed items" list per user?

Options:

- One item per view with `pk = USER#u-1#VIEWS`, `sk = timestamp`, TTL for old ones, query newest first with `Limit: 20`
- A single item with a bounded list: read, prepend, trim to 20, write back with a version condition

The first is simpler with concurrency and avoids read-modify-write. Duplicates (same product viewed twice) can be removed on read, or by using `sk = productId` plus a GSI sorted by time.

## 442: How do you handle data for users in many time zones?

Store all timestamps in UTC (ISO 8601 or epoch). Convert to local time only in the UI or API response.

For keys like "orders per day", decide which "day" you mean. A UTC day bucket is simplest. If the business needs local days (for example daily store reports), include the time zone in the bucket logic and store the local date as a separate attribute for indexing.

## 443: What is the impact of using UUIDs vs sortable IDs (like ULID or KSUID) as keys?

- **Random UUID v4**: spreads perfectly across partitions, but sorting by id gives no useful order
- **ULID, KSUID or UUID v7**: start with a timestamp, so items sort by creation time, which is useful as a sort key

As a partition key, either works, because DynamoDB hashes it. As a sort key, time-sortable ids give you "newest first" without a separate timestamp. The only thing to watch is many writes with increasing sort keys under the same partition key, since they all land at the end of the same key range.

## 444: How do you limit the blast radius of a bad deploy that writes bad data?

- PITR on, so you can restore to before the deploy
- Feature flags for new write paths, turned on gradually
- Validation of items before writing
- Conditional writes that reject unexpected state transitions
- Alarms on unusual write rates or error patterns
- Version attributes so you can find and fix items written by a specific release

Including the app version in an attribute (like `writtenBy: 'api@1.42.0'`) makes it much easier to find the affected items later.

## 445: How do you share a DynamoDB table between microservices?

Generally you don't. Each service should own its tables, and others should use its API or events. Sharing a table couples services to each other's key formats and makes changes risky.

If you must share (for example during a migration):

- Give each service IAM access only to its own key prefixes (with `dynamodb:LeadingKeys`)
- Document the item shapes as a contract
- Publish changes through Streams or events instead of letting others read raw items

## 446: What are the trade-offs of storing a whole aggregate in one item?

Pros:

- One read gets everything
- Updates to the aggregate are atomic without transactions
- Simple code

Cons:

- 400 KB limit
- Every update writes the full item size, which costs more as it grows
- Concurrent updates to different parts conflict (need optimistic locking)
- You can't index or query inner parts

It works well for small, bounded aggregates like a user's settings or a shopping cart. For unbounded parts, split them into separate items.

## 447: How do you approach DynamoDB in an interview system design question?

1. Clarify access patterns and their rates
2. Pick the base table key for the most important pattern
3. Add GSIs for the rest, and say which ones are sparse
4. Discuss hot keys and how you'd shard them
5. Mention consistency: where you need strong reads, transactions, or conditions
6. Cover Streams for side effects and derived data
7. Talk about cost: item size, GSIs, capacity mode
8. Mention backups, global tables and failure handling

Showing that you start from access patterns is usually what interviewers look for.

## 448: What is the "access pattern table" and why is it useful?

A simple table that lists every access pattern and how it's served:

| Access pattern              | Index | Key condition                         | Notes           |
| --------------------------- | ----- | ------------------------------------- | --------------- |
| Get user                    | Table | pk = USER#id, sk = PROFILE            | GetItem         |
| User's orders, newest first | Table | pk = USER#id, begins_with(sk, ORDER#) | desc, paginated |
| Order by id                 | GSI1  | GSI1PK = ORDER#id                     |                 |
| Pending orders today        | GSI2  | GSI2PK = PENDING#date                 | sparse          |

It's the documentation of a DynamoDB design. Reviewers can check every pattern, and new team members can understand the model without reverse engineering the keys.

## 449: What are the most important DynamoDB best practices?

- Start from access patterns, then design keys
- Use high-cardinality partition keys with even traffic
- Use `Query`, not `Scan`, for app traffic
- Keep items small, and move blobs to S3
- Use conditions for correctness, transactions only when needed
- Use sparse and overloaded GSIs, with small projections
- Handle pagination, `UnprocessedItems` and retries correctly
- Use on-demand by default, and pre-warm for big events
- Turn on PITR and deletion protection in production
- Monitor throttles, latency, and stream iterator age
- Keep tables in IaC

## 450: How would you explain DynamoDB data modeling to a team coming from SQL?

In SQL you model the data first and write queries later. The database figures out how to answer them with joins and indexes. In DynamoDB it's the other way around: you list the questions the app will ask, and shape the data so each question is a direct lookup.

So instead of normalized tables joined at read time, you store data together the way it's read, accept some duplication, and use keys with prefixes and GSIs as your "pre-built queries". Writes do a bit more work so reads stay fast and predictable at any scale.

The trade-off is flexibility. New kinds of questions may need a new index or a data migration, so spend time on the access pattern list before writing code.
